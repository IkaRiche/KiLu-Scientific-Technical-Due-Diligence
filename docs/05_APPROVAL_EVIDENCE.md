# Android Approver — human authority outside the AI agent

**KiLu's split-trust design keeps the human approval key separate from the agent.** An AI worker on a Linux/Android Hub can request an action, but it is not handed the signing secret belonging to the separate Android Approver.

## Implemented boundary

The [public Android client](https://github.com/IkaRiche/kilu-pocket-agent) includes Ed25519 key generation and signing within the Android application, encrypted on-device storage via EncryptedSharedPreferences and an Android Keystore-backed master key, plus a separate BiometricPrompt confirmation interface. The agent process on a **different device** is not given the Approver private key.

The important, evidenced split-trust property is **separation of principals and custody**. There is no need to present an Android device key as part of the agent's operating environment.

## Operational and cryptographic evidence

- **Historical R1/E2:** on-device human approval and subsequent governed execution were previously exercised.
- **CREG-003 V2:** a new exact-action signing contract binds plan identity, action digest, runtime and toolchain. [Public JVM CI](https://github.com/IkaRiche/kilu-pocket-agent/actions/runs/42079529380) checked canonical framing, hashes and mutation rejection; Cloud checked matching signatures in a synthetic SQLite harness.

The earlier device tests and later V2 crypto tests are **two positive evidence lanes**. A physically performed new V2 signing ceremony is a separate qualification step, not a missing proof of historical Android functionality.

## Key-custody qualification

Current public Ed25519 keys are generated in software and protected in app-encrypted storage. The biometric prompt runs as a separate app-level approval step and also permits device credentials. Therefore the validated claim is **Android-resident signing key isolated from a remote agent**; not that current Ed25519 signatures require hardware-backed StrongBox authentication per operation.

[Split-trust architecture](02_ARCHITECTURE_BOUNDARIES.md) · [Claims register](../evidence/CLAIMS_REGISTER.csv) · [Detailed technical boundary](14_DETERMINISTIC_GATE_EVIDENCE.md).
