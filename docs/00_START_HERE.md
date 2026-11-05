# Reviewer starting guide

This repository is a **public claims index** with intentionally limited disclosure. It is not a complete reproducible source distribution.

Suggested sequence: [executive overview](01_EXECUTIVE_OVERVIEW.md) → [trust boundaries](02_ARCHITECTURE_BOUNDARIES.md) → [claims register](../evidence/CLAIMS_REGISTER.csv) → [evidence index](../evidence/INDEX.md) → [adversarial review](06_REVIEW_PROTOCOL.md).

**Interpretive rules:** public source inspection is not external security certification; private CI is owner-reported until an external evaluator can inspect the primary artifacts; historical Android E2E, synthetic execution, and AegisAI policy attestation are separate evidence owners. Do not combine them into a nonexistent complete system result.

The review deliverable is a claim-level verdict, reasons for non-verifiability, strongest alternative explanation, and the smallest justified qualification question. Use `PASS`, `FAIL`, `INCONCLUSIVE` and `EVIDENCE_INSUFFICIENT` as appropriate.

No source access, production credentials, raw logs, legal records or private repositories are granted by the public review pack.