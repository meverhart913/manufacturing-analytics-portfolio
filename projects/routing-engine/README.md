# Manufacturing Routing Recommendation Engine

## Portfolio-safe overview

This prototype helps an analyst find relevant historical process plans when reviewing a new or unusual manufactured item. It presents comparisons for human review rather than automatically declaring a route correct.

## Transferable technical work

- Join a large item history with structured attributes and ordered process steps.
- Normalize inconsistent historical records before comparison.
- Rank potentially comparable items using several available attributes.
- Expose important differences alongside every recommendation.
- Distinguish standard history from exceptional or corrective history before measuring effectiveness.
- Validate recommendations with subject-matter experts before operational use.

```mermaid
flowchart LR
    A[Historical records] --> B[Normalized features]
    B --> C[Similarity ranking]
    C --> D[Analyst review]
```

## Status

Working prototype. The public repository excludes operation sequences, part attributes, routing logic, source queries, item identifiers, and internal performance results.

