# Manufacturing Analytics Portfolio

Manufacturing analytics, decision-support, and process-improvement work by **Michael Everhart**.

I build practical tools that connect production data to daily decisions: what to make, what material can be used, where capacity is constrained, how a part should be routed, and what historical pricing supports a quote.

## Focus areas

- Production planning and capacity analysis
- Inventory, WIP, and material-allocation decision support
- SQL-backed reporting and analytics applications
- Excel, Power Query, and VBA automation
- C#/.NET desktop application development
- Manufacturing process improvement and ERP validation

## Featured projects

| Project | Business problem | Stack | Status |
|---|---|---|---|
| [Geometry Nesting Application](projects/corenest/README.md) | Convert measured raw-material geometry into manufacturable layouts | C#, .NET 8, WPF, computational geometry, DXF | Active development |
| [Manufacturing Price Explorer](projects/price-explorer/README.md) | Give Sales and Quoting fast access to comparable historical transactions | C#, WPF, SQL Server, SQLite, Excel export | Active development |
| [Specialty Material Inventory Decision Support](projects/cr4-inventory/README.md) | Match demand to finished inventory, recoverable material, and raw stock | SQL Server, Excel 365, Power Query, VBA | Working tool |
| [Routing Recommendation Engine](projects/routing-engine/README.md) | Find relevant historical manufacturing routes across thousands of parts | SQL Server, SAP Business One data, analytics | Working prototype |
| [Backlog & Capacity Planner](projects/capacity-planner/README.md) | Test regular-time and overtime capacity against an eight-week backlog | Python, Excel, scenario modeling | Portfolio demo included |
| [Bonded Rod Removal Automation](projects/bonded-rod-automation/README.md) | Replace multi-source preparation and manual document generation | Excel, VBA, SQL/Power Query | Deployed workflow |
| [Automated Excel Report Factory](projects/report-factory/README.md) | Turn repeatable data pulls into consistent refreshable reports | SQL, Python, Excel, Power Query, VBA | Reusable pattern |
| [Growth Requirements Analysis](projects/growth-requirements/README.md) | Translate demand, yield, and on-hand supply into future material needs | SQL, Excel, production planning | In development |
| [Selected Process Improvements](projects/process-improvement/README.md) | Reduce cost, travel, cycle time, defects, and supply risk | Lean Six Sigma, Excel, SQL | Completed work |

The [complete project catalog](docs/project-catalog.md) also records supporting tools, merged ideas, scheduling prototypes, and deferred concepts without overstating their maturity.

## Demonstration code

The [`demo/capacity_planner`](demo/capacity_planner/README.md) folder contains a runnable, dependency-free Python example using fictional orders and work centers. It calculates required hours by week, compares three capacity scenarios, and flags overloads and late work.

```bash
cd demo/capacity_planner
python -m unittest discover -s tests -v
python src/capacity_planner.py \
  --orders data/orders.csv \
  --capacity data/capacity.csv \
  --output output/capacity_summary.csv
```

## Selected results

- Reworked a SQL-backed pricing workflow so interactive research completed in seconds instead of minutes.
- Built and production-validated a material-matching workflow whose recommended candidates met the required tolerance in the documented test.
- Automated a multi-source production-document workflow, reducing preparation time and common lookup, calculation, and archive errors.
- Led cost-justified improvements in defect reduction, equipment loading, point-of-use staging, supplier performance, and production flow.

## Technical toolkit

`SQL Server` · `SAP Business One` · `Excel 365` · `Power Query` · `VBA` · `Python` · `C#` · `.NET 8` · `WPF` · `Tableau` · `R`

## How I work

1. Define the production decision, not just the report.
2. Identify the authoritative data and expose missing assumptions.
3. Encode business rules so results are reproducible.
4. Validate recommendations against real outcomes.
5. Keep operators and analysts in control through warnings, overrides, and traceable outputs.

## Confidentiality

This public repository uses generalized descriptions, fictional sample data, independently written demonstration code, and deliberately non-specific outcomes. It does not contain employer source code, customer or order information, internal credentials, server names, proprietary drawings, pricing, controlled technical data, or exact internal performance figures. See [Data and confidentiality](docs/data-and-confidentiality.md).

## About

Michael Everhart is a manufacturing and production-control analyst with a B.S. in Mathematics and an M.S. in Business Analytics. His background spans production planning, supply chain, continuous improvement, pricing analysis, ERP migration support, and hands-on manufacturing.
