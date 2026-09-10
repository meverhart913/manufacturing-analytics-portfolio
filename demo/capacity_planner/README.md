# Synthetic Capacity Planner Demo

This dependency-free Python demonstration compares aggregate work-center demand with regular and overtime capacity. The checked-in fixtures cover **four weeks**. Every identifier, quantity, duration, and result is fictional and unrelated to employer data.

[View the generated scenario table](EXAMPLE_RESULTS.md) · [Read the case summary](../../projects/capacity-planner/README.md)

## Run from this directory

```bash
python -m unittest discover -s tests -v
python src/capacity_planner.py --orders data/orders.csv --capacity data/capacity.csv --output output/capacity_summary.csv
python render_example.py
```

## Fictional input specification

| File | Grain | Fields |
|---|---|---|
| orders.csv | One operation demand row for a fictional order | order_id, work_center, due_week, quantity, setup_hours, run_hours_per_unit, is_late |
| capacity.csv | One work center and week | work_center, week, regular_hours |

Required hours = setup hours + quantity × run hours per unit. Setup is charged once per input demand row. Weeks are scenario buckets, not dates. Overtime adds five or ten work-center hours to each supplied center/week. Negative or non-finite hour inputs, negative quantities, duplicate capacity keys, and demand without a capacity key are rejected.

`is_late` counts existing input flags; it is not a predicted completion status. Utilization with zero capacity is undefined (blank in CSV); overload still reports the uncovered hours. The model assumes supplied identifiers, weeks, and late flags are well-formed. It is a small analytical example, not a general-purpose import validator.

## Interpretation and provenance

Fixtures and the original Python model were present in this public portfolio before this continuation. This run checked the example, added integrity guards, and regenerated the readable output. This demonstration must not be described as a newly delivered employer project or used to support historical savings claims.

No finite scheduling, material availability, resource-sharing, downtime, labor-skill, or yield calculation is included. Aggregate overload identifies a review question, not a promised shipment date.
