"""Regenerate a readable synthetic result from the checked-in fictional fixtures."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent / 'src'))
from capacity_planner import read_csv, summarize

HERE = Path(__file__).resolve().parent
rows = summarize(read_csv(HERE/'data/orders.csv'), read_csv(HERE/'data/capacity.csv'))
lines = ['# Synthetic Capacity Scenario Results', '', '**Entirely fictional. Not an employer result or a production scheduling forecast.**', '',
         'The checked-in example covers four weeks and three fictional work centers. Overtime is additional available work-center hours per week. The input late flag is descriptive and does not change with overtime.', '',
         '| Week | Center | Scenario | Required h | Available h | Load % | Overload h | Input late flags |',
         '|---|---|---|---|---|---|---|---|']
for row in rows:
    load = 'undefined' if row['utilization_pct'] is None else str(row['utilization_pct'])
    lines.append(f"| {row['week']} | {row['work_center']} | {row['scenario']} | {row['required_hours']} | {row['available_hours']} | {load} | {row['overload_hours']} | {row['late_orders']} |")
lines += ['', '## Decision example', '',
          'For CUT in week 1, the fictional demand requires 50.3 hours against 40 regular hours. Adding ten hours still leaves 0.3 hours of aggregate overload. This flags a capacity question; it does not establish which order will finish late or whether overtime is feasible.', '',
          'The model makes no material, skill, downtime, routing-precedence, or sequencing check. Zero-capacity utilization is undefined; missing or duplicate capacity keys and invalid hours fail explicitly.', '',
          '[Run and inspect the model](README.md)', '']
(HERE/'EXAMPLE_RESULTS.md').write_text('\n'.join(lines))
print(f'Rendered {len(rows)} fictional scenario rows')
