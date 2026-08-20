import sys
import unittest
from pathlib import Path


SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))

from capacity_planner import required_hours, summarize  # noqa: E402


class CapacityPlannerTests(unittest.TestCase):
    def test_required_hours_includes_setup_and_run_time(self):
        order = {
            "quantity": "10",
            "setup_hours": "2.5",
            "run_hours_per_unit": "0.75",
        }
        self.assertEqual(required_hours(order), 10.0)

    def test_overtime_removes_overload(self):
        orders = [
            {
                "order_id": "SO-001",
                "work_center": "CUT",
                "due_week": "1",
                "quantity": "10",
                "setup_hours": "2",
                "run_hours_per_unit": "4",
                "is_late": "false",
            }
        ]
        capacity = [{"work_center": "CUT", "week": "1", "regular_hours": "35"}]
        result = summarize(orders, capacity)
        by_scenario = {row["scenario"]: row for row in result}

        self.assertEqual(by_scenario["regular"]["overload_hours"], 7.0)
        self.assertEqual(by_scenario["plus_10_ot"]["overload_hours"], 0.0)

    def test_late_orders_are_counted(self):
        orders = [
            {
                "order_id": "SO-002",
                "work_center": "POLISH",
                "due_week": "2",
                "quantity": "1",
                "setup_hours": "1",
                "run_hours_per_unit": "2",
                "is_late": "true",
            }
        ]
        capacity = [{"work_center": "POLISH", "week": "2", "regular_hours": "40"}]
        result = summarize(orders, capacity)
        self.assertTrue(all(row["late_orders"] == 1 for row in result))


if __name__ == "__main__":
    unittest.main()

