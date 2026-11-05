# Deterministic authority: injection resistance, measured gates and key separation

**Scope:** a controlled, code-enforced authority layer. This page distinguishes verified observations, architectural invariants and stronger claims that have not been established. No proprietary implementation, raw trace, private source URL or patent mechanism is disclosed here.

## 1. Why a prompt cannot override the deterministic gate

A planner may be an LLM, another program or a human. It **proposes** an action; it does not become the grant issuer. In the reviewed deterministic authority mechanisms, executable authorization is obtained from typed rules, bounds, cryptographic verification and a checked grant — not by asking an LLM to obey an instruction.

A malicious instruction inserted into a model prompt cannot **directly** rewrite the gate's rules or forge a trusted authorization signature. A compromised model might still *propose* an unwanted action. Whether the gate blocks that action depends on what the configured policy, exact action binding and identity/runtimes actually cover.

**Supported formulation:** *The deterministic KiLu/DeTAK authority check is not prompt-driven. Prompt injection against an upstream AI does not directly override the gate's independent policy and cryptographic checks.*

**Not established:** immunity of the entire AI-agent product to every prompt injection, policy-design error, implementation bug or bypass around the enforced executor.

## 2. Measured latency — different mechanisms, different scopes

| Verified internally / reported measurement | Observed result | Configuration | What it means |
|:--|:--|:--|:--|
| AegisAI deterministic governance benchmark | **10,000 decisions; mean 0.22 ms; p95 0.35 ms** | Frozen synthetic fixture benchmark, seeded, no live LLM calls in measured loop | Evidence for tested policy-decision path; **not** end-to-end financial settlement |
| AegisAI adversarial fixtures | **1,748 prompt-injection cases; 0 security failures** in that category | Same 10,000-case report, defined `BLOCK expected / ALLOW received` failure metric | Empirical result under fixture taxonomy; not universal immunity |
| Embedded DeTAK Ed25519 verification | **~7.85 ms** | STM32H7 hardware benchmark, compact Ed25519 backend | Cost of grant signature verification on a constrained MCU |
| Embedded DeTAK valid-grant gate | **~7.933 ms; 15/15 checks** | STM32H723-class target at 400 MHz, scoped hardware gate tests | Measured MCU authority-gate path; not the AegisAI host benchmark |

The figures above belong to **separate benchmarks**. A compact MCU Ed25519 gate and an in-process host governance check must not be compared as though they were the same operation.

An older conceptual presentation illustrated **sub-1 ms** deterministic decisions and **sub-5 ms** financial policy checks. The AegisAI fixture measurements are consistent with sub-1 ms *mean/p95 in that fixture*, but they do not establish any sub-1 ms limit for all inputs, nor sub-5 ms bank transaction processing. The 7.933 ms **MCU** measurement must not be represented as sub-5 ms.

Raw logs, internal source commits, hardware identifiers and exact test configurations remain restricted. For an external reviewer, these are **owner-reported scoped measurements**, not independently replicated benchmarks.

## 3. Android: the agent does not own the human approval key

The intended split-trust deployment places the **Approver on a separate Android authority device**, outside the agent's execution environment. The agent may request permission but should not possess, retrieve or exercise the Approver's signing private key.

The [public Android implementation](https://github.com/IkaRiche/kilu-pocket-agent) generates Ed25519 keys inside the Android application and stores the private key in **EncryptedSharedPreferences**, with an Android Keystore-backed master key. Thus the agent running on a *separate* Hub/host is not given the Approver's key. This is a real separation-of-responsibility design, not a mere prompt instruction.

It is **different** from a stronger hardware property. The reviewed implementation's Ed25519 key is software-generated and loaded into application memory for signing; the separate `BiometricPrompt` is an application-level gate and can also accept a device credential. The reviewed code does **not** establish hardware-non-exportability of Ed25519 or cryptographically forced fresh biometric authentication for each signature. None of that means that the separate remote AI agent already possesses the Android secret.

## 4. What reviewers should challenge

- For a deterministic policy check: compare exact inputs and policy versions, including input mutation and permitted-but-unwanted actions.
- For the embedded grant verifier: inspect the scope and timing boundary of the MCU test; do not substitute host benchmark figures.
- For split trust: verify that the agent has no signing-key interface and cannot bypass the grant-mediated path, while distinguishing a compromised Approver device from an untrusted remote agent.
- For whole-system safety: inspect the actual executor boundary, not merely the agent or its prompt.

These points sharpen prior evidence without opening a new experiment. [Claim register](../evidence/CLAIMS_REGISTER.csv) · [Threat model](11_THREAT_MODEL.md) · [Approval evidence](05_APPROVAL_EVIDENCE.md) · [Disclosure policy](07_DISCLOSURE_BOUNDARY.md).
