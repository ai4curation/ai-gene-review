# SLC18A3 evidence notes


## 2026-10-26: complete source-specific acetylcholine panel audit

Human VAChT cDNA in PC12 cells supports proton-gradient-dependent acetylcholine uptake (PMID:8910293); PMID:20225888 provides target mutagenesis. PMID:25355561 measures both acetylcholine and serotonin uptake by a human VAChT fusion reconstituted in proteoliposomes. Thus monoamine/proton antiport and serotonin uptake are retained as measured non-core capacities, without claiming native serotonergic vesicle loading. PMID:27590285 was fetched normally (abstract-only) as additional human disease context.

AP-1/AP-2 interaction is not AP-complex subunit identity: PMID:14724281 studies cargo-tail/adaptin association. The GO component definitions specify four-subunit adaptor assemblies; VAChT is cargo, so the two IBA complex-membership assertions are removed while vesicle targeting and membrane localization remain. This role judgment was independently checked with the annotation-reviewer peer. Positive LTP and neuromuscular development are comparative mouse phenotypes, not transport stoichiometry or proof of an obligate human network. Surface retrieval is real transient localization, not a reason to reject plasma membrane.

Methods and limits: reviewed all 47 original annotations, preserving every machine-sourced term, qualifier, reference, partner and evidence field. No new annotation was added. Genuine Falcon and fallback provider attempts were made in the foundation batch and failed with authentication/quota errors; no provider report was fabricated. Normal PMID fetching and targeted public-source recovery were used instead, with access limitations stated per claim. Logs are retained under `.cache/module-audit-logs/acetylcholine-foundation-fetch/`; cached source files were not hand-edited. This review follows the current bare-protein-binding and root-organelle policies.

Actions: ACCEPT 31, KEEP_AS_NON_CORE 6, MODIFY 5, REMOVE 5. Focused strict/schema, ontology-term and source-quote checks, record-section backfill and HTML rendering are recorded in the final audit report; remaining biological uncertainties above are not validation failures.


### Independent QA correction: transporter activity versus location

The GO:0022857 row (zero-based index 24) inadvertently received a cellular-component rationale and replacements. Corrected its MF refinement to GO:0005278 acetylcholine:proton antiporter activity plus the already-retained GO:0015311 monoamine:proton antiporter activity. The latter preserves directly measured serotonin transport by the human fusion construct in PMID:25355561 without asserting native serotonergic loading. The same breadth correction adds existing GO:0051610 serotonin uptake alongside acetylcholine uptake in the three broad BP transport refinements. Original annotation payloads and action counts remain unchanged; membrane localization rows are untouched.


### Terminal compartment correction after independent QA

Live QuickGO definitions on 2026-10-26 confirm GO:0051630 acetylcholine uptake and GO:0051610 serotonin uptake require transport **into a cell**. The human VAChT assays measure vesicle or reconstituted-liposome loading. Accordingly all original uptake rows are MODIFY, not REMOVE: acetylcholine transport GO:0015870 replaces the acetylcholine uptake claims and core process; amine transport GO:0015837 replaces the serotonin uptake claim with the actual serotonin substrate and fusion/proteoliposome context explicit. Both current transport definitions permit movement within a cell. GO:0006837 serotonin transport and GO:0015844 monoamine transport are obsolete; no obsolete replacement or inferred native serotonergic vesicle-loading process is introduced. General transport refinements likewise use the current transport terms. Molecular antiporter assignments remain intact. Earlier journal statements describing uptake-term retention/refinement are superseded by this definition-level correction; the measured chemistry remains supported.
