# Pten review notes

Falcon deep research attempt timed out on 2026-05-04 while running
`just deep-research-falcon mouse Pten`; no `Pten-deep-research-falcon.md` file
was produced. Review decisions used the cached UniProt record, cached
publications, and existing BioReason/Perplexity research.

Core function judgment: PTEN is primarily a dual-specificity phosphatase whose
most characteristic activity is dephosphorylation of PtdIns(3,4,5)P3 at the D3
position, thereby antagonizing PI3K-AKT signaling. UniProt describes lipid
phosphatase activity on PtdIns(3,4,5)P3 with preference for PtdIns(3,4,5)P3 and
also describes protein tyrosine-, serine-, and threonine-phosphatase activity
[UniProt:O08586 "Dual-specificity protein phosphatase... Also functions as a
lipid phosphatase"]. The experimental mouse literature supports the tumor
suppressor and PI3K/AKT pathway role [PMID:9778245 "Negative regulation of
PKB/Akt-dependent cell survival by the tumor suppressor PTEN"; PMID:9990064
"Mutation of Pten/Mmac1 in mice causes neoplasia in multiple organ systems"].

Curation stance: direct phosphatase activities and phosphatidylinositol
dephosphorylation are core. Cell proliferation, apoptosis, migration,
neurodevelopment, synaptic, and organismal phenotypes are generally kept as
non-core unless the term directly describes PTEN enzymatic action. Generic
binding terms remain over-annotated unless they capture a specific mechanistic
interaction.
