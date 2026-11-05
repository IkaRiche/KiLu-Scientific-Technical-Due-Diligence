# KiLu: execution, anti-replay and receipts

## Historical live observations

Earlier R1/E2/E3.2 milestones reported human approval, runtime-bound task execution and DONE outcomes, plus grant revocation. They are evidence about the historical carrier, **not** deployment of later experimental CREG modifications.

## Controlled execution on 5 November 2026

Private CI with synthetic identities and loopback services tested an existing compiled Linux Hub executing one benign, predefined local action. The experiment inspected exact output bytes, one recorded start, minted/consumed JTI and a signed receipt validated by a separate Go verifier. Verdict: `PASS_SCOPED_INTERNAL`. It was a single authorised experimental effect, not a globally enforced physical exactly-once guarantee. **The one-shot experiment must not be rerun.**

## Cross-language verification

A separate scoped experimental path checked Cloud/SQLite records, issuer-signed step tokens, a runtime-bound executor report and an independent Go Offline Verifier. Matched receipts succeeded and selected mutation controls failed. These observations are **private** to the rights holder; the public index does not include raw artifacts, private workflow links or source.

## New CREG-003 binding

Cloud/SQLite tests checked the exact action payload, bounded scope and changed-action rejection. A documented regression affecting a historical JTI test fixture was corrected; follow-up CI completed successfully in scope. That does not establish atomicity for all concurrent database state transitions or production deployment.

**Not established:** AegisAI live policy trace → human V2 device signature → deployed grant → real external effect → complete offline third-party verification as one joined chain.

[Evidence inventory](../evidence/INDEX.md) · [Review protocol](06_REVIEW_PROTOCOL.md).