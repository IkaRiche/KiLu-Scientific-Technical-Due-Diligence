# Executive overview — authority as a separate infrastructure capability

## Why it matters

An AI agent may produce useful plans but should not be trusted to authorise the side effects of its own suggestions. An audit log after the action is insufficient to establish whether **that exact action** was authorised, for **that runtime**, under **those limits**, before any effect occurred.

## Technical proposition

KiLu separates planning, policy admissibility, human escalation, execution authority and execution. A bounded grant can constrain action identity, time and executor, while an independently checked report/receipt can support post-effect review.

This is a **scoped implementation and evaluation thesis**, not a universal theorem that one architecture is superior or a warranty that all tool paths are protected.

## Components and ownership boundaries

| Component | Engineering role | Evidence ceiling |
|:--|:--|:--|
| AegisAI | Policy/admissibility and conditional Class A decision attestation | Separate internally evidenced governance lane |
| KiLu / DeTAK | Bounded authorisation, single-use control and receipts | Internal scoped synthetic Cloud/Hub tests |
| Android Approver | Human approval interface and signer | Prior device approval reported; exact-action V2 JVM evidence only |
| Linux Hub | Pre-effect grant validation and scoped execution | Compiled executor exercised in isolated CI |
| Offline Verifier | Independent receipt verification | Scoped cross-language verifier result |
| KiLu SDK | Public evaluation/developer interface | Mock examples not equivalent to grants |
| StasysOS | Separately evaluated bounded runtime technology | No automatic end-to-end integration claim |

## Why a buyer might evaluate this

Possible uses include infrastructure automation, tool-calling agents and governed enterprise workflows. Buyer integration value must be established on one real target workflow, with evidence of fail-closed behaviour, operational cost, constraints and lifecycle management. This publication does not identify a buyer, give a valuation, include a transaction offer or promise an integration.

[Qualification](08_INTEGRATION_QUALIFICATION.md) · [Commercial diligence](10_COMMERCIAL_DILIGENCE.md).