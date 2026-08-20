# Project Status and Roadmap

This page distinguishes delivered work from active development and future concepts. A portfolio should not present a design idea as a deployed system.

| Project | Stage | Evidence available here | Next milestone |
|---|---|---|---|
| Geometry Nesting Application | Active development | Generalized requirements, architecture, and validation plan | Complete constrained multi-order nesting and operator testing |
| Manufacturing Price Explorer | Active development | Product design, classification logic, offline-data architecture | Stabilize full-screen chart behavior and package self-contained release |
| Specialty Material Inventory Decision Support | Working tool | Generalized matching logic and validation method | Add backlog demand and composition planning |
| Routing Recommendation Engine | Working prototype | Scale, ranking approach, planned effectiveness analytics | Validate route classifications and operator recommendations |
| Backlog & Capacity Planner | Working model | Runnable sanitized Python demo and tests | Add richer work-center and due-date scenarios |
| Bonded Rod Removal Automation | Deployed workflow | Before/after process and measured time reduction | Maintain business rules as source systems change |
| Automated Excel Report Factory | Reusable pattern | Architecture, controls, and delivery approach | Add another sanitized runnable example |
| Growth Requirements Analysis | In development | Decision model and supply-demand design | Validate yield assumptions and on-hand composition rules |
| Material Allocation Optimizer | Deferred concept | Scope and prerequisites | Revisit only if measurable allocation shortages justify it |
| Quality Document Compliance Tracker | Future concept | Problem definition | Validate ownership and workflow before development |

## Development principles

- Build the smallest tool that improves a real production decision.
- Label unknown data as unknown instead of silently failing it.
- Use warnings for reviewable exceptions and hard stops only for invalid manufacturing conditions.
- Separate authoritative source data, transformation logic, decision rules, and presentation.
- Validate calculated recommendations against actual production outcomes.
