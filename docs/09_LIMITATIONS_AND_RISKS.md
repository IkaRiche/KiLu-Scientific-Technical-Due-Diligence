# Technical qualification and version boundaries

This document is the dedicated **scope register** for diligence. It keeps variant-level qualifications clear without obscuring the product's already exercised capabilities on the README.

## Capabilities established within named evidence owners

| Layer | Recorded capability | Evidence scope |
|:--|:--|:--|
| AegisAI | Deterministic policy evaluation without live LLM calls | 10,000 fixture cases, 0.22 ms mean / 0.35 ms p95; 1,748 injection-category fixtures with zero defined safety failures |
| KiLu Network | Signed grant issuance, consumed JTI, runtime-checked execution | Internal scoped Cloud/SQLite and compiled Linux Hub tests |
| Offline verification | Issuer-signed receipts and negative tamper controls | Synthetic cross-language JS/Go path |
| Android Approver | Device-resident human signing key; historic approvals | Public Android code and earlier E2E records |
| V2 approval contract | Exact action/plan/runtime/toolchain binding | Public JVM and private Cloud mutation tests |
| DeTAK embedded | Local signed-grant verification on MCU | STM32H7: Ed25519 ~7.85 ms; valid-grant gate ~7.933 ms |

These are positive results, not hypotheses. They are reported here with their required boundaries to preserve scientific and commercial credibility.

## Separate qualification questions for stronger claims

- **Joined production trace:** independent verification of one newly deployed AegisAI Class A → physical Android V2 → Cloud grant → executor → receipt chain is not part of the existing combined evidence. Individual historical layers remain validated in their own scopes.
- **Hardware key custody:** the current Android Ed25519 signing key is locally encrypted rather than an established per-signature StrongBox-bound Ed25519 secret. The agent still does **not** receive the Approver's key in the intended separate-device architecture.
- **External effect completeness:** one tested CI execution and JTI consumption do not mean every conceivable external system guarantees exactly-once physical effects.
- **Certification and external assurance:** formal platform-wide verification, bank-specific qualification and independent penetration-test claims require their own completed review.
- **Public SDK example scope:** the evaluation-stage SDK has mock examples; legacy `/v1/intent` `ALLOW` alone is not a canonical execution token.
- **Independent raw verification:** some original artifacts are restricted by the IP disclosure policy; reviewers must label those results as owner-reported where source access is unavailable.
- **Optional asset separation:** StasysOS and individual embedded research projects are not silently represented as one deployed combined product.

## Recorded correction and provenance

A V2 SQL scope-validation change initially caused a regression in the historical issued-JTI fixture. The issue was corrected in the experimental research branch; subsequent V2, JTI, mint/runtime and CREG-001 regression CI completed successfully. A negative intermediate test is retained in the internal evidence ledger, not used to erase the successful corrected path.

**Engineering distinction:** the deterministic authorization mechanism does not interpret LLM prompts as permission. Its exact claim is independent gate authority on the integrated route, not a universal assertion that no other software or deployment fault can ever occur.

[Claims register](../evidence/CLAIMS_REGISTER.csv) · [Measured results](14_DETERMINISTIC_GATE_EVIDENCE.md) · [Integration acceptance](08_INTEGRATION_QUALIFICATION.md).
