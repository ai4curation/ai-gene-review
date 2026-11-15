# Independent Kdp boundary and capacity audit

The revised module supports the intended evidence-qualified profiles without making KdpF or cognate KdpD universal requirements. No remaining blocking scientific inconsistency was found in the audited boundaries. Its Boolean circuit alone is deliberately insufficient to establish a compatible pump or regulatory system: the evidence oracle must supply that qualification.

## Positive capacity witnesses

| Profile | Result | Evidence scope |
|---|---|---|
| E. coli FABC plus canonical KdpD/KdpE | Supported complete module capacity | Native structural/function evidence and cognate relay/output assays |
| E. coli ABC plus canonical regulation, native 0.1 mM potassium | Supported complete module capacity | PMID10608856 growth/deletion result in the stated setting; no claim of detergent stability |
| P. putida KT2440 FABC plus canonical regulation | Supported inferred module capacity | Corrected native operon, reviewed family/sequence roles and compatible target proteins; no native purified pump or relay measurements claimed |
| Caulobacter NA1000 ABC plus KdpE output | Supported native profile with inferred chemistry | Native genetics, promoter occupancy and expression; the upstream phosphorylation donor is unresolved |
| Caulobacter profile with cognate KdpD omitted | Still supported | KdpD is not the sole obligatory activating input in this experimental profile |

These are capacity assessments. An assembled pump may be inhibited; neither its inventory nor a satisfied circuit is a measured potassium flux. KdpB inhibitory serine phosphorylation is evaluated as a separate state overlay grounded in PMID38622146, not as a negative structural component in the monotone circuit. Physiological flux rates, expression states and inhibition in other taxa are not inferred.

## Reproducible tests

Run `uv run python analysis/module_audits/bacterial_kdp_potassium_homeostasis/capacity-consultation/check_capacity.py` from the repository root. The script uses the production `compile_node`, `iter_atoms`, `core_atoms` and `is_satisfied`; it does not substitute a hand-written positive-profile Boolean. It reads current review IDs/taxa, verifies their correspondence to the immutable UniProt accession/taxon fields, derives family membership from raw cross-references, and reads reviewed molecular functions, complex contributions and promoter-output claims.

The oracle independently requires every ABC(F) role, distinct physical subunits, KdpA potassium binding, KdpB ATP hydrolysis, reviewed contribution to the pump, a compatible same-panel assembly, and source-qualified conditions for omitting F. Receiver and promoter output must coexist in the same KdpE polypeptide. Family matching alone cannot supply a cognate partner relationship, native physiology, or an activity missing from the reviewed target.

All 32 scenario/sensitivity cases pass. Negative cases include lone DESVH KdpB; missing A, B or C; loss of required A/B molecular activity; generic P-type ATPase or generic OmpR family descriptions; split receiver/output fragments; arbitrary mixed-panel pump or regulator inventories; incompatible taxonomy; short Dgeo ASK replacing the histidine-kinase witness; and an optional kinase or ligand-binding protein alone. Generic-family and fragment cases are explicitly synthetic feature mutations of known records, not new biological assertions about real uncurated proteins. A false result means no supported compatible witness in this supplied evidence set, not biological impossibility or proven genomic absence.

Sensitivity tests intentionally remove one gate at a time. Without the source gate, PSEPK ABC is wrongly accepted despite unestablished native F dispensability. Without compatibility, a mixed ECOLI/PSEPK assembly is accepted. Without same-polypeptide enforcement, separate receiver and DNA-output fragments suffice. Without family specificity, generic classifier descriptions suffice; without activity checking, membership substitutes for the structural contribution. These controlled failures expose the protection each gate provides.

Three additional mutations remove A, B or C from the module's declared complex units. The independent role contract rejects each. Four dedicated optional-step profiles test PSEPK, Caulobacter, Staphylococcus and Deinococcus activity boundaries; the E. coli optional activities are also evaluated in the positive inventory. The compiled document has ten atoms and an empty `core_atoms` list because the alternative profiles use distinct atom IDs; this is not evidence that no biological role is required. A deliberately weak activity-only oracle accepts lone DESVH KdpB as transport, showing that the production compiler's single complex annoton must not be treated as an assembled-complex witness merely because one protein contributes its function.

## Regulatory scope and source quality

The optional KdpD phosphatase step distinguishes E. coli reconstitution from Caulobacter native genetic inference. PSEPK gains neither a new phosphatase nor ASK capability from family membership. Dgeo Q1J2K3 supplies directly measured serine phosphorylation and c-di-AMP stimulation, not histidine kinase, native pump capacity, or directly measured ligand binding. The supplemental construct proof identifies the Dgeo kinase and a heterologous E. coli KdpFABC substrate with KdpB D307N. This phosphorylation assay does not measure native Dgeo transport or inhibition of a catalytically active Dgeo pump.

Staphylococcus Q2FWH7 supplies a sequence-grounded ligand-binding comparison: the checker independently reproduces the 885/885 match to A0A0H2XIE2 from the official captured donor sequence and immutable target record. The module's negative edge is scoped to S. aureus and targets the expression-control profile. Its description distinguishes measured expression inhibition from an unestablished direct autokinase effect. Dgeo stimulation and Staphylococcus expression inhibition are different readouts, not conflicting universal signs for all KdpD proteins. No Dgeo GO:0180001 binding term is manufactured.

`source-quotes.json` contains checked primary excerpts and access-level metadata; `evidence-gates.json` distinguishes native, inferred and assay-limited roles. The E. coli F-independent condition uses an abstract-accessible positive observation and does not use an inaccessible full text to overturn an experimental annotation. The KT2440 complete-operon statement is traced through the separately preserved publisher-access analysis rather than falsely relabeling its protected abstract cache as full text.

## Preservation, closure and limitations

This consultation changes only its audit artifacts. `frozen-input-releases.json` archives exact prior handoff data; the checker verifies every file in the PSEPK, family and regulatory-comparator releases against those hashes. `release-receipt.json` records those unchanged releases. Current module, twenty gene review/raw pairs, family reviews, primary sources, sequence bridge, construct provenance, oracle inputs and compiler are hashed in `results.json`. `boundary-snapshot.json` captures the actual tested variant sets, required/optional parts, notes and regulatory edges. This makes subsequent module or source changes detectable.

Ruff passes for the checker. No gene/family/module edits, new annotation assertions, full-corpus validation, commits or pushes were performed. The production compiler does not enforce active-unit compatibility, taxon restrictions, EXACTLY_ONE exclusivity or regulatory state itself; the oracle supplies the first two, interprets alternatives as evidence-qualified capacity options rather than mutually exclusive lineages, and reports state separately. Future evaluation must preserve these source gates rather than consume only family hits or the empty structural core.
