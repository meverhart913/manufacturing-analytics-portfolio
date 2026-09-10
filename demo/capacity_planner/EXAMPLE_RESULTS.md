# Synthetic Capacity Scenario Results

**Entirely fictional. Not an employer result or a production scheduling forecast.**

The checked-in example covers four weeks and three fictional work centers. Overtime is additional available work-center hours per week. The input late flag is descriptive and does not change with overtime.

| Week | Center | Scenario | Required h | Available h | Load % | Overload h | Input late flags |
|---|---|---|---|---|---|---|---|
| 1 | COAT | plus_10_ot | 0.0 | 50.0 | 0.0 | 0.0 | 0 |
| 1 | COAT | plus_5_ot | 0.0 | 45.0 | 0.0 | 0.0 | 0 |
| 1 | COAT | regular | 0.0 | 40.0 | 0.0 | 0.0 | 0 |
| 1 | CUT | plus_10_ot | 50.3 | 50.0 | 100.6 | 0.3 | 1 |
| 1 | CUT | plus_5_ot | 50.3 | 45.0 | 111.8 | 5.3 | 1 |
| 1 | CUT | regular | 50.3 | 40.0 | 125.7 | 10.3 | 1 |
| 1 | POLISH | plus_10_ot | 34.2 | 50.0 | 68.4 | 0.0 | 0 |
| 1 | POLISH | plus_5_ot | 34.2 | 45.0 | 76.0 | 0.0 | 0 |
| 1 | POLISH | regular | 34.2 | 40.0 | 85.5 | 0.0 | 0 |
| 2 | COAT | plus_10_ot | 37.0 | 50.0 | 74.0 | 0.0 | 0 |
| 2 | COAT | plus_5_ot | 37.0 | 45.0 | 82.2 | 0.0 | 0 |
| 2 | COAT | regular | 37.0 | 40.0 | 92.5 | 0.0 | 0 |
| 2 | CUT | plus_10_ot | 0.0 | 50.0 | 0.0 | 0.0 | 0 |
| 2 | CUT | plus_5_ot | 0.0 | 45.0 | 0.0 | 0.0 | 0 |
| 2 | CUT | regular | 0.0 | 40.0 | 0.0 | 0.0 | 0 |
| 2 | POLISH | plus_10_ot | 41.7 | 50.0 | 83.4 | 0.0 | 0 |
| 2 | POLISH | plus_5_ot | 41.7 | 45.0 | 92.7 | 0.0 | 0 |
| 2 | POLISH | regular | 41.7 | 40.0 | 104.2 | 1.7 | 0 |
| 3 | COAT | plus_10_ot | 38.7 | 50.0 | 77.4 | 0.0 | 0 |
| 3 | COAT | plus_5_ot | 38.7 | 45.0 | 86.0 | 0.0 | 0 |
| 3 | COAT | regular | 38.7 | 40.0 | 96.8 | 0.0 | 0 |
| 3 | CUT | plus_10_ot | 35.0 | 50.0 | 70.0 | 0.0 | 0 |
| 3 | CUT | plus_5_ot | 35.0 | 45.0 | 77.8 | 0.0 | 0 |
| 3 | CUT | regular | 35.0 | 40.0 | 87.5 | 0.0 | 0 |
| 3 | POLISH | plus_10_ot | 0.0 | 50.0 | 0.0 | 0.0 | 0 |
| 3 | POLISH | plus_5_ot | 0.0 | 45.0 | 0.0 | 0.0 | 0 |
| 3 | POLISH | regular | 0.0 | 40.0 | 0.0 | 0.0 | 0 |
| 4 | COAT | plus_10_ot | 0.0 | 50.0 | 0.0 | 0.0 | 0 |
| 4 | COAT | plus_5_ot | 0.0 | 45.0 | 0.0 | 0.0 | 0 |
| 4 | COAT | regular | 0.0 | 40.0 | 0.0 | 0.0 | 0 |
| 4 | CUT | plus_10_ot | 0.0 | 50.0 | 0.0 | 0.0 | 0 |
| 4 | CUT | plus_5_ot | 0.0 | 45.0 | 0.0 | 0.0 | 0 |
| 4 | CUT | regular | 0.0 | 40.0 | 0.0 | 0.0 | 0 |
| 4 | POLISH | plus_10_ot | 43.0 | 50.0 | 86.0 | 0.0 | 0 |
| 4 | POLISH | plus_5_ot | 43.0 | 45.0 | 95.6 | 0.0 | 0 |
| 4 | POLISH | regular | 43.0 | 40.0 | 107.5 | 3.0 | 0 |

## Decision example

For CUT in week 1, the fictional demand requires 50.3 hours against 40 regular hours. Adding ten hours still leaves 0.3 hours of aggregate overload. This flags a capacity question; it does not establish which order will finish late or whether overtime is feasible.

The model makes no material, skill, downtime, routing-precedence, or sequencing check. Zero-capacity utilization is undefined; missing or duplicate capacity keys and invalid hours fail explicitly.

[Run and inspect the model](README.md)
