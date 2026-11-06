# Evidence inventory — proven technology, traceable qualifications

**Cutoff: 5 November 2026.** KiLu's authority mechanism has tested Cloud, Android, compiled executor, cross-language verifier and MCU evidence owners. The distinction between a **positive internally demonstrated result** and an **externally downloadable original** is explicit.

## Engineering evidence

| ID | Technology result | Access | Reviewer interpretation |
|:--|:--|:--|:--|
| `INT-AEGIS-BENCH` | **10,000** deterministic governance decisions, **0.22 ms mean / 0.35 ms p95**, 1,748 injection-category cases without defined safety failures | Restricted original | Internally frozen no-LLM benchmark |
| `INT-DETAK-H7` | Physical MCU grant verification **~7.85 ms** Ed25519, valid gate **~7.933 ms** | Restricted original | Scoped STM32H7 hardware result |
| `INT-KILU-E2E` | Compiled Linux Hub, issued and consumed JTI, signed report and Go Offline Verifier | Restricted original | Internal scoped cross-language integration |
| `INT-KILU-ONE-SHOT` | One approved effect, exact output bytes, consumed JTI and verified receipt | Restricted original | One-shot controlled test; consent exhausted |
| `INT-KILU-V2` | Exact-action/plan/runtime/toolchain signatures and refusal on mutation | Restricted original | Private Cloud/SQLite V2 tests |
| `INT-ANDROID-HISTORY` | Human approval and execution on real devices in previous milestones | Restricted original; public summaries | Historical R1/E2/E3.2 |
| `INT-AEGIS-CLASSA` | Signed Class A DecisionTrace attestation | Restricted original | Internally tested configured governance lane |

## Directly inspectable public surfaces

| ID | Source | What can be inspected |
|:--|:--|:--|
| `PUB-ANDROID-SRC` | [Android Approver/Hub](https://github.com/IkaRiche/kilu-pocket-agent) | Key custody, app approval controls and public milestone descriptions |
| `PUB-ANDROID-V2-CI` | [Android exact-action CI](https://github.com/IkaRiche/kilu-pocket-agent/actions/runs/42079529380) | JVM digest, signing-format and mutation tests |
| `PUB-SDK-SRC` | [KiLu SDK](https://github.com/IkaRiche/kilu-sdk) | Evaluation-stage APIs, mock examples and integration notes |

The [claims register](CLAIMS_REGISTER.csv) pairs each claim with one source and a bounded interpretation. Confidential raw evidence and source are not published because the technology is proprietary. Their absence from GitHub does not negate the results; external reviewers must nevertheless label them as owner-reported rather than independently examined.

[Review method](../docs/06_REVIEW_PROTOCOL.md) · [Benchmarks](../docs/14_DETERMINISTIC_GATE_EVIDENCE.md) · [Public reproducibility](../docs/12_PUBLIC_REPRODUCIBILITY.md).

## Homeostatic and embedded evidence (6 November 2026)

| ID | Evidence summary | Disclosure |
|:--|:--|:--|
| `INT-ASHBY-MCU` | Historical 32-cell STM32F411 colony, p95 25.1 µs step; separate firmware footprint | Private source and original bench |
| `INT-FABRIC-H7` | Embedded Profile I, 616-byte state; 30/30 STM32H723 checks, worst measured selected update 6.96 µs | Private hardware record |
| `INT-BESM-F411` | Bounded non-authoritative BESM 8/8 STM32F411 vectors; 1.94 µs worst observed update | Private hardware record |
| `INT-ASHBY-RECOVERY` | Simulation recovered 10/10 benign forwarding after externally supplied cooldown | Private experiment; conditional recovery |
| `INT-NEB-EDGE-HOST` | 5/5 host co-execution checks and 24/24 SRC regressions | Private, original compiled Rust sources |
| `INT-NEB-EDGE-EFFECT` | 5/5 focused candidate tests, 10/10 total, 24/24 SRC; restriction with Ashby, no restriction after ablation; cross-source failure | Private host-only experiment; not production firmware |

[Public summary](../docs/15_HOMEOSTATIC_EDGE_EVIDENCE.md).
