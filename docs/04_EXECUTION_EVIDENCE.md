# KiLu execution evidence — grants, anti-replay and verified receipts

KiLu was built to enforce permissions at the effect boundary rather than merely observe model output. The historical live milestones and the later controlled CI experiments establish **distinct, complementary engineering results**.

## Earlier operational validation

R1/E2 included real Android approval, executor-mediated task completion and delivered DONE evidence in historical smoke tests. E3.2 included workflow grants and a recorded revocation path: when a covered step failed, remaining work was not automatically granted fresh authority.

These observations establish the prior device/runtime workflow in its recorded version. They should not be discarded because the newer V2 signing format has a separate test scope.

## CREG-001 — issued-grant and receipt path

In isolated CI with synthetic identities, an issuer-authorized execution path exercised a compiled Linux Hub, bounded grant/step tokens, report submission, signed receipt creation and independent Go verification. Mutation controls rejected selected changed artifact fields. The cross-language CREG-001 regression was successfully repeated after a narrow V2-compatibility correction.

**Value:** authority evidence follows the action through execution and independent verification, rather than ending at an approval UI.

## CREG-002 — actual controlled effect

One authorized CI action was admitted exactly once in the designated experiment. The harness checked the exact expected file bytes, one recorded execution start, an issued and consumed JTI, a completed task state and a signed receipt verified by Go Offline Verifier.

**Verdict:** `PASS_SCOPED_INTERNAL` for one predefined effect on a private isolated runner. The original one-time consent is exhausted; no rerun is authorized.

## CREG-003 — exact-action binding

The experimental V2 signing format connects plan, AVO, exact action digest, runtime and toolchain. Public Android JVM tests and internal Cloud/SQLite tests exercised matching signatures and refusal on action/binding/scope mutation. A test-fixture compatibility regression was corrected and the relevant CI returned PASS.

**Value:** a signed approval is tied to a particular action rather than to a vague instruction to an agent.

## Commercial reading of the evidence

The technology portfolio already includes operational Android history, measured enforcement components, compiled executor checks, anti-replay tests and independently checked receipts. These results support evaluation for buyer-controlled integration. The public dossier intentionally omits internal raw artifacts and does not present separate milestones as one newly certified production V2 deployment.

[Evidence inventory](../evidence/INDEX.md) · [Full claim register](../evidence/CLAIMS_REGISTER.csv) · [Integration evaluation](08_INTEGRATION_QUALIFICATION.md).
