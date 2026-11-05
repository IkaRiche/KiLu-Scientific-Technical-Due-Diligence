# Evidence inventory and access levels

**Evidence cutoff: 2026-11-05.** This is an access-classified index rather than a publication of proprietary primary evidence.

| Source ID | What it represents | Access | Interpretation |
|:--|:--|:--|:--|
| `PUB-ANDROID-SRC` | [Public Android client](https://github.com/IkaRiche/kilu-pocket-agent) | Public | Implemented surface and reported historic milestones; not whole-system audit |
| `PUB-ANDROID-V2-CI` | [Public Android JVM run](https://github.com/IkaRiche/kilu-pocket-agent/actions/runs/42079529380) | Public | Format, digest and negative-control JVM tests; not device biometrics |
| `PUB-SDK-SRC` | [Public SDK](https://github.com/IkaRiche/kilu-sdk) | Public | Mock/evaluation integrations, not canonical issued-token proof |
| `INT-AEGIS-CLASSA` | Internal Class A DecisionTrace evidence | Restricted | Owner-reported; original proof unavailable publicly |
| `INT-KILU-E2E` | Scoped Cloud/Hub/Go verifier integration | Restricted | Private synthetic CI; `PASS_SCOPED_INTERNAL` |
| `INT-KILU-ONE-SHOT` | One benign CI effect, receipt and JTI checks | Restricted | One-shot; not repeatable by the historic consent |
| `INT-KILU-V2` | Action binding and mutation checks for experimental V2 | Restricted | Synthetic tests and regression correction; no production or device ceremony |
| `INT-ANDROID-HISTORY` | Historical mobile approval/execution milestones | Restricted original / public summaries | Older protocol, not V2 |

| `INT-AEGIS-BENCH` | Historic AegisAI 10,000-case no-LLM benchmark, mean 0.22 ms and p95 0.35 ms | Restricted | Internal scoped measurement; not a cloud end-to-end SLA |
| `INT-DETAK-H7` | STM32H7 Ed25519 verify ~7.85 ms and gate ~7.933 ms | Restricted | Separate embedded hardware test path; not the same as host policy timing |

An `INT-*` entry **does not** confer outside access, independent reproducibility or a cryptographic external proof object. A `PUB-*` entry allows inspection of only the public surface and the assertions actually checked there.

[Claims register](CLAIMS_REGISTER.csv) · [Review protocol](../docs/06_REVIEW_PROTOCOL.md) · [Reproducibility](../docs/12_PUBLIC_REPRODUCIBILITY.md).