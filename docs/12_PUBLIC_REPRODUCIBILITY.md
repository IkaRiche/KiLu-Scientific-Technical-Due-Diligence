# What can be checked independently?

| Material | Public? | Verifiable result |
|---|---|---|
| This repository's Markdown/CSV and structural checks | Yes | Internal links, claim/source IDs, prohibited disclosure patterns |
| Android JVM action-binding tests | Yes, through the linked public CI | Kotlin digest and message formatting under the tested revision |
| KiLu SDK examples | Yes | Mock-based developer examples, **not** live execution grants |
| CREG Cloud/Go executor / offline verifier logs | No | Owner-reported outcomes only in this index |
| AegisAI original Class A artifacts and source | No | Described internally, not independently reproducible here |
| Full cross-layer end-to-end evidence | No | Explicitly unverified |

### Local documentation verification

```bash
python3 tools/validate_public_package.py
```

The checker validates only the public package's controlled inventory, references, and basic text patterns. Its success is **not** evidence of scientific correctness, secret absence, security certification or legal disclosure clearance.

[Evidence inventory](../evidence/INDEX.md) · [Claims register](../evidence/CLAIMS_REGISTER.csv).