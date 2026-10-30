# NMB (Neuromedin-B) — Curation Notes

## Identity and Family Context
- **Gene symbol:** `NMB` (`UniProtKB:P08949`)
- **PANTHER family:** `PANTHER:PTHR16866` (`GASTRIN-RELEASING PEPTIDE`), subfamily `PANTHER:PTHR16866:SF0` (`NEUROMEDIN-B`)
- **Mature peptide processing:** Synthesized as a 121-aa preprohormone (or 116-aa isoform) with an N-terminal signal peptide (aa 1–24), processed by proteolytic cleavage and C-terminal alpha-amidation into neuromedin B-32 (`NMB-32`, aa 25–56) and the C-terminally amidated decapeptide neuromedin B (`NMB-10`, aa 47–56), the mammalian homolog of amphibian ranatensin (`PMID:2458345`, `PMID:10544247`).

## Signaling Pathway and Receptor Specificity
- **Receptor and signaling cascade:** `NMB` is one of two mammalian bombesin-like peptides (alongside `GRP`) and acts as the high-affinity endogenous agonist for the Gq/11-coupled neuromedin-B receptor (`NMBR`, `UniProtKB:P28336`) (`Reactome:R-HSA-375384`, `PMID:31601264`).
- **Missing GO biological process annotation (Category A gap):** In GOA, `NMBR`, `GRPR`, and `BRS3` are annotated to `GO:0031989` (*bombesin receptor signaling pathway*), whereas `NMB` carries `GO:0031710` (*neuromedin B receptor binding*), `GO:0005184` (*neuropeptide hormone activity*), and `GO:0007218` (*neuropeptide signaling pathway*) plus generic `GO:0007165` (*signal transduction*, `TAS` `PMID:2458345`), but lacks `GO:0031989`.
- **Curation action:** Propose `NEW` (`IC`) `GO:0031989` (*bombesin receptor signaling pathway*) supported by `Reactome:R-HSA-375384`, and `MODIFY` the generic `GO:0005179` (*hormone activity*, `TAS` `PMID:2458345`) and `GO:0007165` (*signal transduction*, `TAS` `PMID:2458345`) rows to their specific descendants `GO:0005184` and `GO:0031989` / `GO:0007218`.
