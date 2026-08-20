# Backlog & Capacity Planner

## Problem

Production teams need a fast answer to whether the next eight weeks of demand fit available work-center hours and how much overtime would change the risk.

## Solution

A scenario model that calculates required hours as:

```text
required hours = setup hours + quantity × run hours per unit
```

It groups work by due week and work center, then compares demand against regular time, regular time plus five overtime hours, and regular time plus ten overtime hours.

## Outputs

- Required and available hours by work center/week
- Overload hours and utilization
- Late-order count
- Weeks of backlog
- Scenario comparison for overtime decisions

## Scope boundary

This is a tactical capacity model. It is not an ERP/MRP replacement, BOM or routing manager, inventory-allocation engine, or finite scheduler.

## Demonstration

A runnable fictional example is available in [`demo/capacity_planner`](../../demo/capacity_planner/README.md). The demo uses only Python's standard library and includes unit tests.

