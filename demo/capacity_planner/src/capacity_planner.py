"""Small, dependency-free manufacturing capacity scenario model."""

from __future__ import annotations

import argparse
import csv
import math
from collections import defaultdict
from pathlib import Path
from typing import Iterable


SCENARIOS = {
    "regular": 0.0,
    "plus_5_ot": 5.0,
    "plus_10_ot": 10.0,
}


def required_hours(order: dict[str, str]) -> float:
    """Return setup hours plus quantity times run hours per unit."""
    quantity = int(order["quantity"])
    setup = float(order["setup_hours"])
    run = float(order["run_hours_per_unit"])
    if quantity < 0 or not all(math.isfinite(x) and x >= 0 for x in (setup, run)):
        raise ValueError("Quantity and required-hour inputs must be finite and nonnegative")
    hours = setup + quantity * run
    if not math.isfinite(hours):
        raise ValueError("Required hours exceed the supported numeric range")
    return hours


def summarize(
    orders: Iterable[dict[str, str]],
    capacity_rows: Iterable[dict[str, str]],
) -> list[dict[str, object]]:
    demand: dict[tuple[str, int], dict[str, float]] = defaultdict(
        lambda: {"required_hours": 0.0, "late_orders": 0.0}
    )

    for order in orders:
        key = (order["work_center"], int(order["due_week"]))
        demand[key]["required_hours"] += required_hours(order)
        demand[key]["late_orders"] += int(order["is_late"].strip().lower() == "true")

    capacity_rows = list(capacity_rows)
    capacity_keys = [(row["work_center"], int(row["week"])) for row in capacity_rows]
    if len(capacity_keys) != len(set(capacity_keys)):
        raise ValueError("Duplicate capacity key: work center and week must be unique")
    missing = set(demand) - set(capacity_keys)
    if missing:
        raise ValueError(f"Missing capacity for demand keys: {sorted(missing)}")

    results: list[dict[str, object]] = []
    for capacity in capacity_rows:
        work_center = capacity["work_center"]
        week = int(capacity["week"])
        regular_hours = float(capacity["regular_hours"])
        if not math.isfinite(regular_hours) or regular_hours < 0:
            raise ValueError("Regular capacity must be finite and nonnegative")
        required = demand[(work_center, week)]["required_hours"]
        late_orders = int(demand[(work_center, week)]["late_orders"])

        for scenario, overtime_hours in SCENARIOS.items():
            available = regular_hours + overtime_hours
            utilization = required / available if available else None
            results.append(
                {
                    "work_center": work_center,
                    "week": week,
                    "scenario": scenario,
                    "required_hours": round(required, 2),
                    "available_hours": round(available, 2),
                    "utilization_pct": round(utilization * 100, 1) if utilization is not None else None,
                    "overload_hours": round(max(required - available, 0.0), 2),
                    "late_orders": late_orders,
                }
            )

    return sorted(results, key=lambda row: (row["week"], row["work_center"], row["scenario"]))


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "work_center",
        "week",
        "scenario",
        "required_hours",
        "available_hours",
        "utilization_pct",
        "overload_hours",
        "late_orders",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--orders", type=Path, required=True)
    parser.add_argument("--capacity", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rows = summarize(read_csv(args.orders), read_csv(args.capacity))
    write_csv(args.output, rows)
    print(f"Wrote {len(rows)} scenario rows to {args.output}")


if __name__ == "__main__":
    main()
