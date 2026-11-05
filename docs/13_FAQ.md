# KiLu — frequently asked questions

### Why doesn't KiLu just use an LLM-based safety prompt?

Because **permission to execute is not a language-model decision**. KiLu's deterministic authority and signature checks are independent of a planner's generated text. A model may suggest an action; it cannot forge grant authority by persuasive instructions.

### What evidence exists for its performance?

AegisAI's frozen no-LLM 10,000-case governance benchmark measured **0.22 ms mean / 0.35 ms p95**. Separate physical STM32H7 DeTAK experiments reported **~7.85 ms Ed25519** verification and **~7.933 ms** for a valid-grant gate. The numbers measure different paths; neither is a full settlement SLA.

### Doesn't prompt injection defeat an autonomous agent?

It may manipulate an untrusted agent's intent, but the KiLu-controlled executor does not treat that intent as proof of authorization. The gate checks the trusted grant and bindings instead. This is the purpose of independent execution authority.

### Where are human approval keys?

On a **separate Android Approver**, not given to the remote agent. The public Android client implements local Ed25519 key generation and encrypted app storage. The current public key custody is not a claim of hardware-nonexportable StrongBox Ed25519.

### Was the Android approval actually tested?

Yes — previous device approval and execution milestones were exercised in the historic R1/E2 path. The newer exact-action V2 signature format has independent Android JVM and Cloud/SQLite tests; a complete physical V2 ceremony is a distinct later qualification.

### Can the receipt be verified without the online issuer?

An independent Go Offline Verifier was exercised against signed receipts in the scoped Cloud/Hub CI path. The verifier establishes covered cryptographic linkage; it does not observe every outside physical consequence.

### Does the SDK quickstart prove end-to-end granted execution?

No. The current public [SDK](https://github.com/IkaRiche/kilu-sdk) is an evaluation-stage interface whose examples use mock authorities. Canonical grant-mediated tests are maintained separately.

### Is KiLu an Android app, or a technology that can be integrated elsewhere?

It is a **technology architecture and authority protocol** with Android, Linux, Cloud, SDK and embedded verification components. The buyer can evaluate one selected integration without replacing its AI model.

### Is KiLu open source?

The public dossier is all-rights-reserved. Public Android and SDK components retain their own terms. Core proprietary source, original raw evidence and undisclosed inventions are not offered for download here.

[Technology overview](01_EXECUTIVE_OVERVIEW.md) · [Engineering results](04_EXECUTION_EVIDENCE.md) · [Technical scope](09_LIMITATIONS_AND_RISKS.md).
