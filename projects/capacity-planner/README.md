# Backlog & Capacity Planner

**Runnable synthetic portfolio model; employer deployment not established.**

## Problem and contribution

A planner needs to compare required work with available work-center hours and examine the effect of overtime. This repository contains an independently written Python demonstration of that analytical pattern.

## Approach

Required hours are setup hours plus quantity multiplied by run hours per unit. Demand is grouped by due week and work center, then compared with regular capacity and two illustrative overtime scenarios.

## Domain reasoning

Aggregate hours identify a potential constraint. They do not prove a feasible sequence or promise a shipment date. Material availability, labor skills, maintenance, precedence, and shared resources are outside this example.

## Outputs and limits

Required/available hours, overload, utilization, and counts of orders **already flagged late in the input**. Overtime does not predict new completion dates. Missing capacity is an error; zero capacity has undefined utilization. The model does not calculate weeks of backlog or perform finite scheduling.

[Run the synthetic demo and inspect its output](../../demo/capacity_planner/README.md). All inputs and results are fictional, with no relationship to employer values. This is technical proof, not a new historical career accomplishment.

[Portfolio home](../../README.md)
