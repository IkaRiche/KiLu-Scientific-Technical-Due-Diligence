# Deterministic authority — tested injection controls, latency and split trust

## The distinguishing security property

**No LLM interprets instructions to issue execution authority in the deterministic gate.** The planner is an input source, not an authorization principal. A malicious prompt can alter an agent's proposal, but it cannot directly cause the independent gate to rewrite typed rules, produce a trusted Ed25519 signature or bypass a required runtime-scoped grant check.

This is a structural defence at the **execution boundary**, unlike relying on a model's prompt obedience.

## Two measured computing environments

| Mechanism | Measured outcome | Source configuration | Practical significance |
|:--|:--|:--|:--|
| **AegisAI deterministic governance** | **10,000 decisions; mean 0.22 ms; p95 0.35 ms** | Internally frozen seeded fixture benchmark; no live LLM inference | Fast tested policy evaluation |
| **Adversarial policy fixtures** | **1,748 prompt-injection cases; 0 security failures** | Same benchmark; failure = BLOCK expected but ALLOW received | Tested adversarial inputs did not become unauthorized grants in the defined cases |
| **Embedded DeTAK Ed25519** | **~7.85 ms** | STM32H7, compact Ed25519 backend | Grant-signature verification feasible on MCU-class target |
| **Embedded DeTAK valid-grant gate** | **~7.933 ms, 15/15 checks** | STM32H723-class hardware at 400 MHz | Measured local authorization decision including grant verification |

**These are real, separately reported measurements.** AegisAI's software governance timing is not the same as STM32H7's signature-verification latency. Neither has been advertised here as the entire duration of an external bank transaction.

The original private reproducibility logs are retained by the rights holder. This public review reports the measurements without releasing their raw evidence or proprietary bench implementation.

## Human key custody belongs outside the agent

The intended KiLu split-trust configuration keeps the **human Approver on a separate Android device**. Its private signing key is not sent to the remote model, Linux Hub or agent.

The [public Android app](https://github.com/IkaRiche/kilu-pocket-agent) demonstrates local Ed25519 key generation, BouncyCastle signing and encrypted key storage through EncryptedSharedPreferences with a Keystore-backed master key. An independent BiometricPrompt gates the approval UI in the implemented workflow.

**Supported security property:** the AI agent cannot directly sign as the human solely because it controls its own prompt or task execution environment.

**Distinct hardware-key property:** the reviewed Ed25519 key is software-generated and temporarily materialized in the Android app for signing, while biometric success is checked at the application layer and may also use device credentials. This is not proof of StrongBox-backed Ed25519 custody or a per-signature hardware-enforced biometric CryptoObject. Neither condition is needed to make the architecture's separation of the remote agent from the Approver key intelligible.

## How this reduces integration risk

KiLu can be introduced at the point where a buyer's executor consumes a proposed action. A proper deployment requires the executor to check bounded authority rather than treating a model-generated command as permission.

The relevant acceptance evidence is concrete: exact action binding, runtime/toolchain denial, consumed-JTI replay refusal, grant expiry, signed report and independent receipt verification.

**The decisive buyer advantage:** even when the upstream AI behaves unexpectedly, it does not automatically acquire new execution privileges. Controls operate in an independently enforced deterministic layer.

## What stronger evaluations remain separate

General protection against every software bug, all conceivable executor bypasses, bank-specific compliance and a newly deployed, fully joined Class A + Android V2 authorization trace are not implied by the named experiments. Those are additional system qualifications, not reasons to downgrade the already measured gate.

[Architecture](02_ARCHITECTURE_BOUNDARIES.md) · [Evidence register](../evidence/CLAIMS_REGISTER.csv) · [Commercial value](10_COMMERCIAL_DILIGENCE.md) · [Detailed scope register](09_LIMITATIONS_AND_RISKS.md).
