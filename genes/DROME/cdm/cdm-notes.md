# Cadmus (cdm/Imp13) evidence notes

Q9VEC5 is the 971-residue product of current FlyBase FBgn0261532, formerly CG7212/imp13. PA and PB encode identical proteins (AAF55502/NP_650682 and AGB96076/NP_001262696), as recorded in the saved FlyBase report. The current symbol cdm is retained rather than replacing it with an older literature synonym. [FlyBase](https://flybase.org/reports/FBgn0261532).

[PMID:20122403](https://pubmed.ncbi.nlm.nih.gov/20122403/) explicitly reports a “Drosophila Imp13-Mago-Y14 complex” and a “human Imp13 bound to RanGTP” structure. This identifies direct fly import-cargo recognition and a conserved mechanism; it does not identify the particular cargo responsible for every synaptic phenotype. The cache is abstract-only, so no claims about uninspected residue-level experiments are made. The fly structural observation supplies independent support for the PAINT transport assignments.

[PMID:11447110](https://pubmed.ncbi.nlm.nih.gov/11447110/) reports “Imp13 also shows export activity towards the translation initiation factor eIF1A”. Export in the fly is a conserved importin-13 inference, supported by its diagnostic identity and the phylogenetic annotation, not a claimed direct Drosophila eIF1A transport assay. QuickGO lookup of the older Ran-binding identifier GO:0008536 resolved to GO:0031267; the existing small-GTPase-binding identifier is retained.

[PMID:19403829](https://pmc.ncbi.nlm.nih.gov/articles/PMC4011492/) is cached with full text and establishes the connection between CG7212 mutations, genomic rescue, visual phenotypes and postsynaptic control of presynaptic release. The decisive localization qualification is “Imp13 expression only in the muscle nuclei but not at the synapse” for the rescuing genomic construct; NMJ synaptic fluorescence occurred under overexpression. Accordingly, the process-derived synapse IEA is over-annotated; it is not evidence against the observed synaptic physiological role. Nuclear/perinuclear localization and transport are core; visual and transmission phenotypes are non-core.

[PMID:14504225](https://pubmed.ncbi.nlm.nih.gov/14504225/) remains abstract-only after full-text retrieval was attempted. The 2009 follow-up independently connects the mutant locus to Imp13 and rescues the visual phenotype, so there is no basis to overturn the original curated behavioral/transmission annotations from incomplete access.

The Falcon report completed and its principal fly genetics/localization synthesis agrees with the directly inspected 2009 source. However, it missed the 2010 Drosophila Imp13-Mago-Y14 structure and therefore overstates the absence of characterized fly cargoes. Its claim that cdm is merely an alias is also superseded by the current FlyBase symbol. Those limitations are recorded here; the provider text is preserved untouched. The YAML relies on the primary publications, rather than adding a redundant provider citation to suppress an advisory.

Both ProtNLM GO predictions are LSP: nucleocytoplasmic transport and intracellular protein transport are broader than supported specific protein nuclear import/export. Agreement with ARBA is not used as evidence, and overlap alone is not asserted to establish training-set contamination.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Scope: re-examined all 19 GOA rows, description and core functions without consulting any ProtNLM2 output.

Identity: Q9VEC5 is the full-length 971-aa canonical cdm product (PA/PB identical), not a fragment or isoform; length matches vertebrate IPO13 (963 aa) with the full IBN_N/Xpo1/HEAT repeat architecture.

Evolutionary grounding: UniProt places Q9VEC5 in PANTHER PTHR12363:SF33 (IMPORTIN-13), the same subfamily as human IPO13 (O94829), mouse Ipo13, yeast KAP122 and Arabidopsis MOS14 (interpro/panther/PTHR12363/PTHR12363-entries.csv). Transfer of importin-13 export activity (eIF1A; [PMID:11447110 "Imp13 also shows export activity towards the translation initiation factor eIF1A"]) is therefore subfamily-level, not best-hit. The PTHR12363 family review marks GO:0005049 family-wide as UNRESOLVED (TNPO3 branch differs); no disagreement about subfamily placement of cdm (it is the SF33 representative member there).

Changes vs previous version:
- GO:0051170 import into nucleus (NAS): ACCEPT -> MODIFY to GO:0006606 (cargo is protein).
- GO:0051168 nuclear export (NAS): ACCEPT -> MODIFY to GO:0006611 protein export from nucleus.
- GO:0006886: replacement now lists both GO:0006606 and GO:0006611.
- GO:0043243 positive regulation of protein-containing complex disassembly (NAS, general review): ACCEPT -> MARK_AS_OVER_ANNOTATED. RanGTP (or competing import cargo, [PMID:11447110 "the cytoplasmic release of eIF1A from Imp13 is triggered by the loading of import substrates onto Imp13"]) is the effector; the receptor is a component of the complex being disassembled.
- GO:0050804 modulation of chemical synaptic transmission (IMP): KEEP_AS_NON_CORE -> MARK_AS_OVER_ANNOTATED. Full text: release increase is a homeostatic response to muscle defects, and [PMID:19403829 "In that respect, imp13 might be indirectly linked with synaptic homeostasis."]. Necessity, not participation.
- GO:0007270 and GO:0042331 (IMP, PMID:14504225 abstract-only) kept as non-core; source full text not inspectable.
- Added second core function (export receptor, GO:0005049 / GO:0006611) flagged as subfamily inference; rewrote description; added reference_review entries and suggested questions/experiment.

Relative to review next: human IPO13 (O94829), PANTHER SF33 ortholog with direct import/export biochemistry; no review in repo. No modules cover cdm/importin-13.
