# Technical buyer review — assess the proven mechanisms

**Review objective:** determine how KiLu's independent execution authority can be integrated with an AI platform, enterprise executor or controlled transaction system. The evidence dossier gives reviewers a short path from claimed capability to a named measurement or test.

## 60-minute evaluation agenda

| Time | Capability | Demonstrated evidence | Evaluation question |
|:--|:--|:--|:--|
| 0–10 | Separation of model and authority | Deterministic, non-LLM policy/gate contracts | Can the model unilaterally authorise an effect? |
| 10–20 | Measured deterministic decisions | 10,000-case AegisAI benchmark; 0.22 ms mean, 0.35 ms p95 | Does the selected deployment preserve the tested bound? |
| 20–30 | Signed grants and anti-replay | KiLu Cloud/Hub issued and consumed JTI tests | Is the target action bound to grant and runtime? |
| 30–40 | Split-trust human authority | Historical Android E2E; local key custody; V2 mutation checks | Does the untrusted agent ever receive the Approver key? |
| 40–50 | Execution evidence | One controlled effect, signed report, Go Offline Verifier | Can an independent verifier reject tampered artifacts? |
| 50–60 | Integration economics | Proposed buyer-controlled acceptance procedure | Does this replace bespoke approval and evidence plumbing at acceptable cost? |

## Due-diligence protocol

1. **Select a claim ID and its intended scope.** The [claim register](../evidence/CLAIMS_REGISTER.csv) distinguishes measured results from architecture contracts and next-version qualifications.
2. **Identify original evidence.** Public Android and SDK materials can be reviewed directly; certain CI and benchmark records remain internal and are described as owner-reported.
3. **Inspect the mechanism at its actual boundary.** A permission is checked before the covered effect; policy admissibility, issuance, execution and receipt have separate owners.
4. **Test the relevant denial property.** Wrong action/runtime, missing approval, expired or reused JTI, and changed receipt fields are the decisive controls.
5. **Evaluate adoption.** Compare existing approaches on actual integration cost, latency, operator workload and verifiability rather than on generic AI-safety slogans.
6. **Record precise qualifications.** Preserve historic positive results; do not accidentally describe a past exercised path as an untested future architecture.

**Review outputs:** scoped verified capabilities, a buyer-specific integration boundary, unanswered acceptance questions, and defined technical assets eligible for discussion.

## What this public review provides

Evidence summaries, benchmark measurements and architectural boundaries without disclosing proprietary source, raw records, keys or unpublished claims. The complete asset/title and original-record review remains a separate legal and technical process.

[Buyer briefing](01_EXECUTIVE_OVERVIEW.md) · [Evidence index](../evidence/INDEX.md) · [Integration acceptance](08_INTEGRATION_QUALIFICATION.md) · [Limitations and version scope](09_LIMITATIONS_AND_RISKS.md).
