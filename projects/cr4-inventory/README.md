# Specialty Material Inventory Decision Support

## Portfolio-safe overview

This working decision-support tool helps planners compare demand with finished inventory, reusable stock, and eligible upstream material. It replaces fragmented manual searches with a controlled, reviewable workflow.

## Transferable technical work

- Combine SQL Server data through Power Query into an Excel 365 interface.
- Normalize units and parameter definitions before applying eligibility rules.
- Separate candidate generation from final planner allocation.
- Preserve incomplete records for review instead of silently treating them as failures.
- Compare calculated recommendations with later production outcomes.
- Record false positives and refine the rules iteratively.

```mermaid
flowchart LR
    A[Demand] --> B[Normalized supply]
    B --> C[Eligibility rules]
    C --> D[Ranked candidates]
    D --> E[Planner review]
```

## Status

Working tool with production validation. The public repository excludes material specifications, thresholds, identifiers, quantities, source queries, and internal results.

