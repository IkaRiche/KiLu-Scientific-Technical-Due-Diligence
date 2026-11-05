# KiLu security model — remove the AI model from authority

**Security principle:** untrusted text, AI-generated plans and model output do not constitute execution permission. Trusted grant issuance and checked execution live outside the language model.

## Key control boundaries

| Threat or failure mode | Independent KiLu / DeTAK control | Evidence |
|:--|:--|:--|
| **Prompt injection of an upstream AI** | The authorization gate evaluates typed rules and cryptographic grants, **not natural-language orders** | Deterministic design; 1,748 synthetic AegisAI injection-category cases with zero defined safety failures |
| **Agent attempts to self-authorize** | Agent does not possess issuer authority or separate Android Approver private key | Split-trust design and Android local key storage |
| **Changed action after approval** | Signature commitment binds exact action/plan and intended runtime/toolchain | CREG-003 Android JVM/Cloud mutation controls |
| **Out-of-scope runtime or tool** | Execution grant carries enforced runtime/toolchain binding | KiLu Cloud/compiled Hub tests |
| **Replay of an existing authority token** | JTI is issued and consumed with replay rejection | KiLu scoped JTI CI tests |
| **Unverifiable post-effect account** | Signed execution report, issuer receipt and Go offline verification | CREG-001/002 controlled CI |
| **Unapproved expansion of permissions** | Bounded grant checks time, steps and signed constraints | CREG-003 synthetic constraint/expiry regression |

## What the model cannot do

A successful prompt injection may change a model's suggested command. **It does not give that model a valid human signature, an issuer credential or an enforceable grant.** On an executor route that checks KiLu authority, the model's instruction is not an authorization primitive.

This security property is a key infrastructure differentiator, distinct from asking a model to self-police or merely storing audit logs after execution.

## Review boundaries

Security statements apply to the actual integrated enforcement path and named experiments. A separate deployment evaluation must confirm that all selected side effects pass through the gate and that the separate Android authority device is controlled by its intended operator. StrongBox/per-signature hardware biometric enforcement, a newly deployed all-V2 trace and external security certification are additional, separately scoped questions — **not failures of the proven deterministic gate**.

[Architecture](02_ARCHITECTURE_BOUNDARIES.md) · [Approver evidence](05_APPROVAL_EVIDENCE.md) · [Detailed mechanisms and measurements](14_DETERMINISTIC_GATE_EVIDENCE.md).
