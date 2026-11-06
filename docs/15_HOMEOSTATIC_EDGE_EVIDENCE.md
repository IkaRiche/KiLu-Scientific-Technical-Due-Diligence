# Homeostatic regulation and low-resource edge evidence

**Evidence cutoff: 6 November 2026.** This page reports scoped, owner-reported research outcomes for preliminary technical evaluation. The underlying private code, raw logs and experimental traces are not disclosed.

## Why an execution grant is not enough

Independent permission checking asks: **May this action execute?** Homeostatic regulation asks: **How does the system respond when the operating environment deteriorates?** These are different responsibilities.

- **KiLu / DeTAK / AegisAI**: versioned policy and independently verified, bounded execution authority, separate from the language model.
- **Ashby Cells and KiLu Fabric**: bounded, deterministic internal state and stream regulation in response to accumulated disturbances. These layers cannot issue cryptographic grants.
- **BESM**: bounded modulation of load, stress and risk-related state, without final permission or actuator authority.
- **SRC / DRC**: independently owned safety limits, execution constraints and recovery. A physiological hint must not bypass these constraints.

The historical Ashby reference colony, later Ashby MicroColony and lightweight Fabric Profile I **have different mechanisms and hardware profiles**. Ashby Cells and BESM are early homeostatic research constructs, not interchangeable with later LMA Prints/Tissue. The combined portfolio is **not** one fully qualified deployed product.

## Original measurements and experiments

| Mechanism | Observed result | Exact qualification |
|:--|:--|:--|
| 32-cell Ashby reference colony | STM32F411 at 96 MHz: **25.1 µs p95** measured colony step; reference firmware **~15.8 KiB Flash / ~5.3 KiB estimated RAM** | The reference firmware and its measured function, **not** full-stack resource use |
| KiLu Fabric Profile I | STM32H723: **30/30** physical bench checks, **616 bytes fixed state**, selected update worst measured **6.96 µs** at 400 MHz | Lightweight observation/state-pressure profile, **not** a full physiological colony or independently enforced actuator gate |
| BESM | STM32F411: **8/8** on-device vectors; worst observed **187 cycles (1.94 µs)** at 96 MHz; no dynamic memory allocation | Bounded, non-authoritative modulation only; **not** combined runtime WCET |
| Historical immune recovery simulation | **10/10** benign requests forwarded after **20 externally provided recovery ticks** | Recovery under admitted inputs, not unconditional or fully autonomous recovery |
| Fabric plus homeostasis simulation | Modeled LLM-budget signal depleted by **25–59%** in specified failure streams | **Signal depletion, not measured customer money/compute savings** |
| Fabric adaptive routing simulations | Across six routing-sensitive workloads, **6.5–26.3% fewer mean route hops**, while modeled budget changes were **mixed** | Selected synthetic workloads only; no uniform operating-cost advantage |
| Live STM32H723 MAVLink observation | Fabric and BESM observed live/injected stream events while preserving SRC recovery/gate separation | Hardware observation only. In this specific integrated firmware the DeTAK decision was simulated; separate DeTAK MCU crypto was tested elsewhere |
| Native Rust host co-execution | **5/5** host integration checks and **24/24** existing native SRC regressions | Original compiled components and signature test vectors; no physical actuator |
| Candidate homeostatic effect binding | **5/5** focused tests (**10/10** combined host checks), **24/24** SRC regressions | Same otherwise admissible signed action became **test-only NoDispatch** after an Ashby restrictive state; removing the Ashby contribution restored test dispatch. SRC/DeTAK authority remained independent |

The focused 5 checks are **included** in the combined 10 tests; these counts should not be added. Numbers above are from **different profiles and experiments**, not an end-to-end latency SLA.

## Negative findings and open integration boundary

The historical F4 pipeline did **not** apply an Ashby advisory to the final gate. The later restrictive-effect result tested a **candidate host-only ordering**, not production firmware and not physical actuation.

A shared, unpartitioned MicroColony showed **cross-source false suppression** in a negative control: degraded behavior associated with one source affected an otherwise healthy second source. **Multitenant source isolation is therefore NOT established.** The currently supported experimental perimeter is a single defined safety domain; partitioning and its resource budget require separate qualification.

Not yet established: complete combined MCU Flash/RAM/energy/WCET; identity and trust of admitted observations; persistent replay and physical side effects; reliability on the buyer's workloads; independent superiority against equally informed adaptive controllers; customer savings or a deployed production security certification.

## Commercial evaluation perimeter

Two potential, complementary paths can be studied: **cloud/enterprise AI agent authority plus disturbance governance**, and **embedded/Physical AI local regulation plus independently controlled execution**. Neither is a representation that a named buyer already needs or operates the package.

A buyer can review the [claims register](../evidence/CLAIMS_REGISTER.csv), [scope limitations](09_LIMITATIONS_AND_RISKS.md) and [integration criteria](08_INTEGRATION_QUALIFICATION.md) before considering a controlled examination of original evidence under separately agreed confidentiality conditions.
