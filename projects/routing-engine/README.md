# Manufacturing Routing Decision Support

**Data foundation complete; classification in progress; similarity and recommendations planned.**

## Problem

Historical process plans contain inconsistent identifiers and changing practices. Selecting a superficially similar item can propagate an obsolete or incompatible process.

## Contribution and approach

Prepared SQL extractions and a Power Query analytical model joining item attributes with historical routing information. Source documentation records identifier cleanup, duplicate elimination, validation, and a one-row-per-item view. Manufacturing classification is being developed before similarity scoring.

## Domain judgment

Classify process compatibility before comparing historical items. A frequent route is not automatically the correct route, and exceptions need context before being treated as best practice. Recommendations must remain explainable and subject to engineering review.

## Result and boundary

The prepared data foundation is the completed artifact. Similarity ranking, confidence scores, recommendation generation, and the review dashboard are planned, not deployed. No routing-time reduction is claimed.

**Technical evidence:** SQL and Power Query. Python similarity libraries are planned; they are not counted as implemented evidence here. Internal routing sequences, dimensions, thresholds, and data volumes are excluded.

[Portfolio home](../../README.md)
