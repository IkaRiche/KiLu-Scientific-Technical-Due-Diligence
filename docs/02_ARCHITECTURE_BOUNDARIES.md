# KiLu architecture — separate intention, permission and execution

![Conceptual authority path](../assets/authority-flow.svg)

**The central security property is structural:** AI-proposed intent does not constitute permission. A language model cannot obtain executor authority merely by generating persuasive or malicious instructions.

## Authority is allocated to different principals

| Component | Responsibility | Authority it does not receive |
|:--|:--|:--|
| AI model, planner or workflow manager | Propose a structured action | Cannot self-issue a KiLu execution grant |
| AegisAI | Evaluate admissibility under versioned policy and emit signed governance evidence in its Class A path | Does not execute an action or issue the KiLu grant |
| Android Approver | Human-controlled approval and local signing surface | The remote agent is not given the private key |
| **KiLu Network** | **Issue bounded grants, maintain JTI authority, receive report and issue receipt** | Does not choose the agent's goal or perform the effect |
| Executor / Linux Hub | Verify the scoped grant before carrying out a covered action | Cannot create a human approval or issuer signature |
| **DeTAK MCU profile** | **Check signed granted authority locally on constrained hardware** | Embedded verification is not an AI policy planner |
| Go Offline Verifier | Independently check receipt cryptography and covered artifact linkages | Cannot invent facts about external effects |
| StasysOS | Separately developed bounded-runtime option | Not automatically included in an exercised KiLu path |

## Tested engineering interfaces

The execution experiments exercised **Cloud/SQLite → signed grant → compiled Linux Hub → controlled effect → signed execution report → receipt → independent Go Offline Verifier**. They checked exact output, one authorized start in the fixture, consumed JTI and denials for selected mutations. The March/April history covers earlier Android E2E and workflow-grant scenarios.

Separately, the embedded DeTAK verifier was measured on STM32H7 and passed hardware-specific gate scenarios. It is **not** the grant issuer. An AegisAI Class A governance attestation is a different signed object from a KiLu grant; exact V2 action-binding tests are a separate research increment.

**Design advantage:** a compromised planner still cannot invent the separate human signature or trusted grant-issuer signature. Coverage is determined by the executor paths actually integrated with KiLu.

[Security mechanism](11_THREAT_MODEL.md) · [Execution proof](04_EXECUTION_EVIDENCE.md) · [Evidence scopes](09_LIMITATIONS_AND_RISKS.md).
