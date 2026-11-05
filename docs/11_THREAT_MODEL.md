# Reviewer threat model (public abstraction)

**Assets:** the distinction between a proposed action and permitted execution, the approver's meaningful assent, the executor's grant checks, JTI non-reuse and receipt provenance.

**Trust boundaries:** LLM/planner → policy service; displayed action → human signature; policy approval → grant issuer; issuer → executor; executor → signed report; receipt → offline verifier.

| Threat | Required defence at the tested boundary | Current public evidence ceiling |
|---|---|---|
| Planner-issued pseudo-authority | A plan alone cannot mint an executable grant | Architectural contract, implementation-specific tests |
| Action substitution | Executed payload bound to approved digest | Scoped Cloud V2 and Android JVM tests |
| Wrong runtime / toolchain | Exact runtime/toolchain binding enforced before effect | Scoped executor tests |
| Token replay | Issued and consumed token/JTI state checked | Scoped internal synthetic test |
| Approval impersonation | Registered approver key and signed bytes verified | Experimental synthetic signature tests |
| Display/signature mismatch | Exact displayed payload linked to signature, including device UX conditions | New physical-device V2 ceremony **not established** |
| Receipt laundering | Issuer and executor provenance verified, covered mutations rejected | Scoped independent Go receipt verifier |
| Bypass of grant-mediated route | All relevant side effects cross actual enforcement boundary | **Not established universally** |

**Out of scope:** all external executor code paths, production physical effects, hosted-platform security, independent penetration testing and any guarantee that a human fully understood a presented action.

This file reveals no operational attack details and is not a security assessment of live services.

[Evidence](../evidence/INDEX.md) · [Limitations](09_LIMITATIONS_AND_RISKS.md).