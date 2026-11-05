# Proposed integration qualification

This is a **future experimental design**, not a claim about an agreed pilot.

**Candidate use case:** one agent-managed enterprise tool or infrastructure action with a controlled sandbox effect. The buyer chooses a narrow permitted operation, denial conditions, constraints and acceptable operator overhead.

### Minimum evaluation contract

1. Capture the exact proposed action and policy context.
2. Deny unapproved, changed, expired, wrong-runtime or replayed action **before** effect.
3. When approval is required, record what the approver actually reviewed and the precise cryptographic commitment.
4. Make the executor verify the issued token on the operational code path.
5. Produce a receipt that a separately pinned verifier accepts, and rejects if any covered field changes.
6. Keep target system safety, identities, external side effects and access credentials within the buyer-approved sandbox.

### Primary and competing explanations

**H1:** the grant-mediated path constrains the selected operation before any side effect. **H0:** a conventional access-control gate or test harness alone explains the observed result. Compare matched information and observed rejection outcomes rather than claiming inherent superiority.

**Failure criteria:** any unauthorised effect, invalid token accepted, altered binding accepted, receipt accepted after covered-field mutation, or missing provenance. Record partial failures, latency and integration cost; no manufactured PASS.

This package is not authorisation to run against any external organisation's live infrastructure.

[Review protocol](06_REVIEW_PROTOCOL.md) · [Commercial diligence](10_COMMERCIAL_DILIGENCE.md).