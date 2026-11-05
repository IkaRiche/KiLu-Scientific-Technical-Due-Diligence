# Executive overview — execution authority for an agentic world

## The infrastructure gap

AI agents already generate commands, operate tools and initiate transactions. The hard problem is not whether a model can suggest the next action. It is whether **an independent authority** can determine that a particular action, on a particular runtime and within a particular window, is permitted **before** a side effect occurs.

Prompt engineering cannot substitute for execution authority. Access to a broad service credential does not prove that an individual action was authorized.

## The KiLu proposition

**KiLu introduces a deterministic, cryptographically bounded authority layer between AI intent and execution.** Planning can be stochastic. The execution decision does not need to be.

The capability is composed of complementary responsibilities:

1. **Policy admissibility:** AegisAI assesses structured proposals, with a separate Class A signed decision-attestation lane.
2. **Human authority when needed:** a separately placed Android Approver retains the human signing key; a remote agent does not receive it.
3. **Bounded cryptographic permission:** KiLu issues runtime/toolchain-linked grants with expiry, action scope and consumed-JTI controls.
4. **Executor enforcement:** a Linux Hub checks permission before executing; embedded DeTAK demonstrates a grant-checking profile on STM32H7.
5. **Evidence of authorization:** execution reports and signed receipts are checked by an independent Go Offline Verifier in the tested scope.

These are separable technologies with distinct qualification records, not necessarily one deployed composite product.

## Quantified technical assets

| Result | Recorded observation | Why it matters |
|:--|:--|:--|
| AegisAI policy benchmark | **10,000** deterministic fixture decisions; **0.22 ms mean**, **0.35 ms p95** | Local policy-governance computation is measurable without LLM inference overhead |
| Injection category in that benchmark | **1,748** fixtures; **0** safety failures by the fixed test definition | Adversarially labeled inputs did not become disallowed permissions in the measured cases |
| Embedded DeTAK | Ed25519 check **~7.85 ms**; valid-grant gate **~7.933 ms** on STM32H7 | Bounded signed authority can be checked on MCU-class hardware |
| KiLu execution chain | One consented synthetic action, JTI consumed, signed receipt verified in Go | A tested path from permission to effect to independently checked outcome |
| Android and workflow history | Earlier real-device E2E and tested workflow grant/revocation paths | A human authority surface and operational split-trust history exist |
| Exact-action V2 | Android JVM and Cloud/SQLite signature and mutation checks | Specific-action signing and issue-time checks have executable regression evidence |

The first two rows are one synthetic AegisAI run. The hardware and CI rows are separate measured boundaries. [Detailed methodology](14_DETERMINISTIC_GATE_EVIDENCE.md) · [Full claims register](../evidence/CLAIMS_REGISTER.csv).

## Differentiated buyer value

**AI infrastructure:** govern tool executions independently of model alignment or prompt behavior.

**Enterprise agents:** restrict high-impact actions and preserve a receipt trail linking authorization to execution in the covered integration.

**Agentic finance:** apply a deterministic authority check between a stochastic payment initiator and the existing payment rail. This is a candidate integration market, not a declaration of live banking clearance.

**Edge and autonomous equipment:** verify signed grants locally on MCU-class devices without delegating the decision to a remote LLM.

The architecture does not require replacing the buyer's agent framework, models or executor fleet. Its value is the independently enforced boundary across those components.

## Transaction relevance

Potential transaction structures include licensing, strategic integration or acquisition of a defined technology/IP perimeter. The separate AegisAI, KiLu, DeTAK, Android, SDK and optional runtime assets must be individually identified and their ownership/title verified before a formal transaction. Public documentation does not disclose proprietary source or original raw evidence.

[Integration qualification](08_INTEGRATION_QUALIFICATION.md) · [Commercial and IP review](10_COMMERCIAL_DILIGENCE.md) · [Technical scopes](09_LIMITATIONS_AND_RISKS.md).
