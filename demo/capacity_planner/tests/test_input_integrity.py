import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from capacity_planner import summarize, required_hours

class InputIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.order = dict(order_id='DEMO-1',work_center='DEMO-A',due_week='1',quantity='2',setup_hours='1',run_hours_per_unit='2',is_late='false')
        self.capacity = dict(work_center='DEMO-A',week='1',regular_hours='0')

    def test_missing_capacity_cannot_hide_demand(self):
        with self.assertRaisesRegex(ValueError, 'Missing capacity'):
            summarize([self.order], [])

    def test_duplicate_capacity_cannot_duplicate_load(self):
        with self.assertRaisesRegex(ValueError, 'Duplicate capacity'):
            summarize([self.order], [self.capacity, self.capacity])

    def test_zero_capacity_is_undefined_utilization_with_overload(self):
        row = next(r for r in summarize([self.order], [self.capacity]) if r['scenario']=='regular')
        self.assertIsNone(row['utilization_pct'])
        self.assertEqual(row['overload_hours'],5)

    def test_invalid_hours_cannot_reduce_or_poison_load(self):
        for field in ['setup_hours','run_hours_per_unit']:
            for value in ['-1','nan','inf']:
                with self.subTest(field=field,value=value), self.assertRaises(ValueError):
                    required_hours({**self.order,field:value})
        with self.assertRaises(ValueError):
            required_hours({**self.order,'quantity':'-1'})
        for value in ['-1','nan','inf']:
            with self.subTest(capacity=value), self.assertRaises(ValueError):
                summarize([self.order],[{**self.capacity,'regular_hours':value}])
