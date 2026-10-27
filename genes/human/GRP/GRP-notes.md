# GRP (Gastrin-releasing peptide) — Curation Notes

## Identity and Family Context
- **Gene symbol:** `GRP` (`UniProtKB:P07492`)
- **PANTHER family:** `PANTHER:PTHR16866` (`GASTRIN-RELEASING PEPTIDE`), subfamily `PANTHER:PTHR16866:SF3` (`GASTRIN-RELEASING PEPTIDE`)
- **Mature peptide processing:** Synthesized as a 148-aa preprohormone with an N-terminal signal peptide (aa 1–23), mature gastrin-releasing peptide (`GRP1-27`, aa 24–50, C-terminally alpha-amidated at Met-50, with internal cleavage yielding neuromedin C / `GRP-10`, aa 41–50), and C-terminal flanking peptides (`PMID:3211139`).

## Signaling Pathway and Receptor Specificity
- **Receptor and signaling cascade:** `GRP` is one of two mammalian bombesin-like peptide homologs (alongside `NMB`) and acts as the high-affinity endogenous agonist for the Gq/11-coupled gastrin-releasing peptide receptor (`GRPR`, `UniProtKB:P30550`) (`Reactome:R-HSA-375384`).
- **Missing GO biological process annotation (Category A gap):** In GOA, `GRPR`, `NMBR`, and `BRS3` are annotated to `GO:0031989` (*bombesin receptor signaling pathway*), whereas `GRP` carries `GO:0007218` (*neuropeptide signaling pathway*) and `GO:1900738` (*positive regulation of phospholipase C-activating G protein-coupled receptor signaling pathway*) plus generic `GO:0007165` (*signal transduction*, `NAS` `PMID:3027901`), but lacks `GO:0031989`.
- **Curation action:** Propose `NEW` (`IC`) `GO:0031989` (*bombesin receptor signaling pathway*) supported by `Reactome:R-HSA-375384`, and `MODIFY` the generic `GO:0007165` (`NAS` `PMID:3027901`) and `GO:0005102` (`NAS` `PMID:3027901`) rows to their specific descendants `GO:0031989` / `GO:0007218` and `GO:0005184`.
