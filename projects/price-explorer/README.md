# Manufacturing Price Explorer

## Portfolio-safe overview

This active desktop analytics project helps authorized commercial users find relevant historical records and summarize comparable transactions. The public portfolio excludes all prices, customers, part identifiers, source queries, and internal classification rules.

## Transferable technical work

- Build a responsive C#/.NET WPF search interface over structured data.
- Normalize detailed source values into user-facing analytical categories.
- Calculate auditable summary statistics and time trends.
- Separate source access from application logic so connected and offline users can share one interface.
- Produce a formatted Excel export with criteria, refresh metadata, summaries, chart data, and detail.
- Move expensive filters and aggregation closer to the data source for interactive performance.

```mermaid
flowchart LR
    A[Authorized source] --> B[Data-access layer]
    B --> C[WPF analysis]
    C --> D[Auditable export]
```

## Status

Active development. No historical transactions, customer behavior, proprietary categories, credentials, or employer code are included.

