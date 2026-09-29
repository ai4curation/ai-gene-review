# SNF5 (yeast, P18480 / YBR289W) - curation notes

## 2026-09-29 - IBA and protein-binding rereview

Current `SNF5-goa.tsv` has no `GO_REF:0000033`/IBA rows, so there is no PAINT propagation
assignment to classify for this entry. The rereview instead focused on the ten remaining
`GO:0005515 protein binding` rows that validation flagged as bare generic binding.

Read the cached interaction and SWI/SNF-assembly references for the generic IntAct rows:

* The large-scale interactome or complex-mapping papers (PMID:16429126, PMID:16554755,
  PMID:18719252, PMID:37968396) support physical association but do not establish a specific
  Snf5 molecular function beyond its established SWI/SNF-complex membership.
* The SWI/SNF subunit papers (PMID:17496903, PMID:8016655, PMID:8127913, PMID:8668146,
  PMID:9726966) likewise support complex composition or Swi3/Anc1/Arp-subunit architecture,
  not a separate specific SNF5-side binding activity.
* The SWI/SNF-nucleosome cryo-EM paper (PMID:32188938) is different: it directly places the
  Snf5 C-terminus against the histones and acidic patch, so GOA's generic IntAct row was
  removed and a precise `GO:0031491 nucleosome binding` `NEW` row was added from the same
  paper.

Also searched 2025-2026 literature for SNF5/Snf5/SWI-SNF and cached the directly relevant
recent SWI/SNF papers found after the 2025 deep-research runs:

* PMID:42748234, a 2026 *Science Advances* comparative structural analysis of fungal SWI/SNF
  and RSC, structurally corroborates the conserved Base/scaffold and nucleosome-binding lobe
  model but works on *Chaetomium thermophilum* rather than budding-yeast Snf5.
* PMID:42380116, a 2026 *Nature Communications* study of Swi-Snf/Tup1-Cyc8 interplay in
  *S. cerevisiae*, refines complex-level transcriptional repression biology without adding a
  SNF5-specific GO assertion.
* PMID:42175696, a 2026 *Molecular and Cellular Biology* Yap8/SAGA/SWI-SNF recruitment paper,
  is abstract-only in the local cache and supports another activator-specific SWI/SNF
  recruitment context rather than a new core SNF5 molecular function.

No new IBA decision was needed; no direct 2025-2026 paper contradicted the established
description of Snf5 as a non-ATPase SWI/SNF core subunit that helps engage nucleosomes and
recruit the complex to transcription-factor-bound promoters.
