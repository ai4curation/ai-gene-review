

# 2026-09-20 IBA re-review

All eight original source assertions reviewed and preserved. Four actions restored to ACCEPT (two signal-transduction rows, signaling receptor activity, membrane); the unsupported author-added Toll-pathway NEW row was withdrawn. No new assertion added.

QuickGO explicitly restricts GO:0006954 to Vertebrata (NCBITaxon:7742). This exact constraint, rather than absence of adaptive immunity, supports retaining REMOVE for inflammation. The frozen 2025 GOA source is PTN000687652, an ancestor of the target. Current PTHR24365 tree and IBD instead place inflammation on off-lineage PTN002808115; current QuickGO lacks the old row. Generic receptor/signaling/plasma-membrane assertions persist at positive PTN002808045. Snapshots and hashes are in TOLL9-ontology-and-lineage.json. The timing and reason for upstream changes are not reconstructed.

PMID:38191283 full text reports target expression after mosGILT disruption: "(AGAP006974, fold change 2, p-value 0.0095)". This is not a TOLL9 perturbation. PMID:33963082 supports genuine Bombyx Toll9 LPS recognition with MD-2-like partners; its chimera uses mouse TLR4 intracellular/transmembrane regions. PMID:21386906 full text finds no basal/inducible antibacterial AMP defect in Drosophila Toll9 knockout under the tested conditions, despite prior overexpression activity. These results motivate an explicit transfer/ligand question rather than a blanket immunity rejection.

The old Spaetzle-to-PRR argument was invalid: GO:0038187 requires combining with a microbial PAMP. This does not prove TOLL9 lacks PRR capacity—the Bombyx result is positive relevant evidence. Keep generic receptor activity while adjudicating specificity. Removed DOI-only background citations and paraphrases previously presented as quotations (s13071-024-06497-x, ppat.1012008, ppat.1012965, biom13071159); they had been used to assign target-specific mechanisms from pathway/other-gene evidence. Preserved the Falcon report and marked its over-specific inference DISPUTED.


## Recovery PR specificity follow-up (2026-09-22)

Link the preserved ontology constraint snapshot directly from the inflammation annotation assessment.


## OpenScientist follow-up (2026-10-10)

Reviewed `TOLL9-hypotheses/toll9-ligand-and-immune-pathway-specificity/openscientist.md`. The report supports the existing conservative boundary: the LRR/TM/TIR architecture and current PTHR24365 placement are sufficient for generic `GO:0038023` signaling receptor activity, `GO:0007165` signal transduction, and plasma membrane, but the evidence still does not justify adding `GO:0038187` pattern-recognition receptor activity or a target-specific Toll immune pathway term for *Anopheles* TOLL9.

The report independently recapitulated the key caveats in the curated file: positive LPS/MD-2 evidence is Bombyx-specific, the signaling readout used a BmToll9/mouse TLR4 chimera, Drosophila Toll-9 loss-of-function lacks an antibacterial phenotype in the tested assays, and the mosGILT result is AGAP006974 co-expression rather than TOLL9 perturbation. No annotation action changes are needed; the report is now recorded as a supporting reference for the unproven-ligand boundary.
