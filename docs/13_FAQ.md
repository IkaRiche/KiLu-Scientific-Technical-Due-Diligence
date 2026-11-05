# Frequently asked questions

### Is KiLu an AI agent framework?

No. The execution-authority thesis is to decouple proposed actions from authorisation and make actual side effects require a scoped grant in the integrated path.

### Can I use legacy `/v1/intent` `ALLOW` to execute a real tool?

No. The [public SDK](https://github.com/IkaRiche/kilu-sdk) explicitly warns that an intent decision alone is not a canonical executor-bound grant.

### Is everything open source?

No. This repository is **documentation-only and all-rights-reserved**. Some client/SDK material is already publicly available under its own terms; the core proprietary source and primary evidence remain closed.

### Was Android biometric approval already tested?

Earlier physical Android approval and execution milestones were reported. The **new exact-action V2 ceremony** has public JVM and private Cloud tests but no joined on-device V2 proof. These are distinct statements.

### Can an external reviewer independently prove the entire AegisAI–KiLu chain from this repo?

No. The complete primary chain is not publicly available and its joined experimental proof is not yet established.

### How can I evaluate buyer relevance?

Use the [qualification design](08_INTEGRATION_QUALIFICATION.md) and choose a single controlled workflow with an explicit negative-control battery.

### What does a green Actions badge mean?

Only that this repository's **documentation-integrity** workflow passed, not that a security property or closed-source system was formally validated.

[Start here](00_START_HERE.md).