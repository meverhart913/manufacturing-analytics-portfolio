# Sanitized Capacity Planner Demo

This dependency-free Python example demonstrates the analytical core of an eight-week manufacturing capacity model using fictional orders and work centers.

## Run

```bash
python -m unittest discover -s tests -v
python src/capacity_planner.py \
  --orders data/orders.csv \
  --capacity data/capacity.csv \
  --output output/capacity_summary.csv
```

## Inputs

`orders.csv`

- `order_id`
- `work_center`
- `due_week`
- `quantity`
- `setup_hours`
- `run_hours_per_unit`
- `is_late`

`capacity.csv`

- `work_center`
- `week`
- `regular_hours`

## Output

One row per work-center/week/scenario with required hours, available hours, utilization, overload hours, and late-order count.

All names and values are fictional.

