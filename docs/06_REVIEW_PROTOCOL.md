# Adversarial technical review protocol

**Purpose:** decide what the disclosed evidence actually supports, without disclosing proprietary mechanisms or misrepresenting private evidence as independently verified.

| Stage | Question | Acceptable outcome |
|:--|:--|:--|
| 1. Identity | What exact claim and tested version are at issue? | Unambiguous claim ID and scope |
| 2. Provenance | Is the primary evidence public, internal or absent? | Source classification, no invented provenance |
| 3. Mechanism | Does the test exercise the actual pre-effect enforcement path? | Explicit execution boundary and assumptions |
| 4. Counterexample | What cheaper/conventional mechanism or bypass could explain the result? | Fair negative control or unresolved alternative |
| 5. Mutations | Do scope, runtime, action and replay substitutions reject? | Specific passing and failing test cases |
| 6. Independent check | Could an independent reviewer reproduce the asserted result? | External PASS or EVIDENCE_INSUFFICIENT |
| 7. Qualification | What smallest next integration is defensible? | Scoped pilot and rejection criteria |

Avoid combining independent test suites into a non-observed full-system validation. Do not turn a public documentation CI badge into a software security certificate.

**Deliverable:** written verdict per claim with the strongest counter-hypothesis, accessible evidence, unresolved proof gap and an acceptance/rejection test. If confidential proof cannot be shared, state it without implying third-party access.

[Claims](../evidence/CLAIMS_REGISTER.csv) · [Threat model](11_THREAT_MODEL.md).