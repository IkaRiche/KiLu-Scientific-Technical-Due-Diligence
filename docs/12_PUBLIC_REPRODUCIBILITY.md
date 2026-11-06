# Evidence and reproducibility — what is directly inspectable

KiLu's public dossier provides a **claim-to-evidence map**. Proprietary originals stay in protected custody; public tests can be inspected where the component's publication boundary permits.

| Evidence type | Reader access | Verified or reported result |
|:--|:--|:--|
| [Android source](https://github.com/IkaRiche/kilu-pocket-agent) | Public | Local key generation/storage and historical implementation surface |
| [Android V2 JVM run](https://github.com/IkaRiche/kilu-pocket-agent/actions/runs/42079529380) | Public | Exact-action signed-message format and selected negative tests |
| [KiLu SDK](https://github.com/IkaRiche/kilu-sdk) | Public | Evaluation-stage integration API and mock demonstrations |
| AegisAI frozen 10,000-case benchmark | Original private | 0.22 ms mean, 0.35 ms p95; 1,748 injection-category scenarios with zero defined safety failures |
| STM32H7 DeTAK D2/D3 benchmark | Original private | Local Ed25519 verify ~7.85 ms; valid-grant gate ~7.933 ms |
| Ashby/Fabric historical MCU reports | Original private | 32-cell F411 reference colony p95 25.1 µs; distinct Fabric H723 616-byte state and update up to 6.96 µs |
| BESM MCU report | Original private | STM32F411 8/8 on-device vectors, worst observed 1.94 µs |
| Candidate host-only cross-core study | Original private | 5/5 focused, 10/10 combined and 24/24 SRC regression tests; negative shared-source isolation finding |
| KiLu Cloud/Hub/Go CREG-001/002/003 | Original private | Controlled grants, denied substitutions, one selected effect, verified receipt |
| This public repository's CI | Public | Documentation inventory, local links, public claim/source relationships and selected disclosure-pattern checks |

**Reading a result correctly:** `PASS_SCOPED_INTERNAL` is a positive technical finding under its experiment; it does not become false merely because original proprietary records cannot be distributed. The external evaluator must still distinguish an owner-reported result from independently inspected primary artifacts.

### Re-run documentation integrity

```bash
python3 tools/validate_public_package.py
```

This checks the package **as documentation**. It is not a replacement for original bench tests, source inspection, independent security certification or legal disclosure review.

[Evidence inventory](../evidence/INDEX.md) · [Claims register](../evidence/CLAIMS_REGISTER.csv) · [Buyer review](06_REVIEW_PROTOCOL.md).
