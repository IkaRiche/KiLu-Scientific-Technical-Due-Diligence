# Android Approver: preserve historical evidence, distinguish V2

Earlier R1/E2 validations reported human-approved task execution with an actual Android device. Those are historical positive results and must not be discarded because a later protocol has a narrower experimental record.

The proposed exact-action V2 adds a length-framed signature over plan identity, AVO digest, action digest, runtime and toolchain. A [public JVM run](https://github.com/IkaRiche/kilu-pocket-agent/actions/runs/42079529380) checked Kotlin message framing, SHA-256 and mutation rejection; corresponding private Cloud/SQLite cases checked registered-key signature and binding consistency.

**Different claim:** these JVM tests do not prove the V2 approval view was reviewed and biometrically signed on a physical handset.

An additional important limit is visible in the reviewed Android code: software BouncyCastle Ed25519 signing with private-key bytes protected by EncryptedSharedPreferences, and a separate BiometricPrompt which also permits device credentials. That is not cryptographic evidence of a hardware-nonexportable Ed25519 private key requiring fresh biometric authorisation per signature. This does **not** contradict the older observed device-flow milestones.

Neither rebuilding the Android product nor extending V2 hardware testing is a prerequisite for publishing this scoped evidence index. It may become a prerequisite for a *specific stronger buyer claim*.

[Known limits](09_LIMITATIONS_AND_RISKS.md) · [Public client](https://github.com/IkaRiche/kilu-pocket-agent).