# PDGFB notes

## 2026-05-13 Falcon deep research integration

Falcon synthesis supports PDGFB as a secreted PDGF ligand rather than a receptor
kinase or downstream signaling enzyme
[file:human/PDGFB/PDGFB-deep-research-falcon.md "This report summarizes **GO-relevant evidence for PDGFB as a secreted PDGF ligand**: disulfide-linked dimer formation (PDGF‑BB; PDGF‑AB), **direct binding/activation of PDGF receptor dimers (PDGFRA/PDGFRB)**, secretion/localization (extracellular space; ER/Golgi processing; ECM/HS retention), platelet α‑granule localization (only where explicitly stated), and **ligand-attributable biological processes** (pericyte recruitment/coverage; angiogenesis/blood vessel morphogenesis; limited wound-healing evidence)."].

The review decisions therefore keep receptor binding, growth factor/receptor
ligand activity, extracellular/extracellular-matrix localization, dimerization,
PDGF receptor signaling, angiogenesis, chemotaxis, and supported mural-cell or
mesenchymal responses. Receptor autophosphorylation, PI3K/AKT, ERK/MAPK,
ROS/NADPH oxidase, and transcription/miRNA terms were marked as downstream
over-annotations or modified to PDGF receptor signaling where the source really
supported ligand-triggered receptor activation
[file:human/PDGFB/PDGFB-deep-research-falcon.md "Do **not** annotate PDGFB with receptor enzymatic activities (e.g., **protein tyrosine kinase activity**, **peptidyl-tyrosine phosphorylation**) or generic downstream pathways (PI3K/AKT, ERK/MAPK, ROS) based solely on PDGFR signaling descriptions; these belong to PDGF receptors or downstream effectors, not the PDGFB ligand itself"].

## Source-defect re-review (2026-11-10)

An independent re-review of this gene's wrong-gene / wrong-reference source defects changed the following; where earlier notes above say otherwise, this section supersedes them.

- GO:0042802 / PMID:23139410: defect withdrawn (evidence depth: FULL_TEXT). Full text (PMC3523867, via WebFetch) describes the PDGF-BB homodimer in the SOMAmer co-crystal ("PDGF-BB homodimer bound to SOMAmer SL5", aptamer "crossing the homodimer interface"). IntAct curates the chains of a crystal structure as a physical association, so the paper does support PDGFB self-association. Defect deleted; reason rewritten; the abstract quote moved to review.supported_by.
