# AegisAI — deterministic policy admissibility

AegisAI evaluates structured actions against explicit policy. **An upstream LLM can propose an action; it does not decide the deterministic authorization outcome.** AegisAI keeps decision evidence separate from the grant authority of KiLu Network.

## Measured governance behavior

An internally recorded, seeded **10,000-case benchmark** of the policy path, with **no live LLM calls**, reported:

- **0.22 ms mean decision latency; 0.35 ms p95** in the measured fixture.
- **0 safety failures in 1,748 prompt-injection-category fixtures**, under the test's predefined failure criterion.
- A Class A **Ed25519 DecisionTraceAttestation** path for signed governance outcomes when a signing key is configured.

These numbers show a fast deterministic policy-evaluation path in a specified harness. They are not a payment-processing benchmark, cloud-network SLA or general-purpose immunity certificate.

## Role in the product family

AegisAI supplies admissibility evidence. **KiLu** independently issues execution grants and receipts. The Android Approver supplies human signatures when approval is required; the Hub enforces a grant before performing the covered operation. Each responsibility is deliberate: no language-model prompt becomes a substitute for trusted authorization.

The later experimental V2 exact-action path has separate Android JVM and Cloud signing tests. A unified live Class A/V2 trace across all components is a distinct qualification objective, **not a reason to discount the proved AegisAI and KiLu mechanisms**.

[Benchmarks and trust boundaries](14_DETERMINISTIC_GATE_EVIDENCE.md) · [Architecture](02_ARCHITECTURE_BOUNDARIES.md) · [Claims](../evidence/CLAIMS_REGISTER.csv).
