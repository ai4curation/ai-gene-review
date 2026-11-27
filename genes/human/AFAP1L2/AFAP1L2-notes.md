# AFAP1L2: paired human–horse review notes

## Biological evidence

The primary XB130 study establishes a signaling adaptor that activates Src and links EGF to downstream signaling and gene expression. It reports interaction motifs, kinase activation, knockdown effects and transcriptional reporters. The evidence supports specific kinase/adaptor roles rather than generic binding.

- [PMID:17412687: XB130, a novel adaptor protein for signal transduction.](https://pubmed.ncbi.nlm.nih.gov/17412687/) — abstract cached; full-text availability must be checked separately.

## Exact horse model

The full human818-residue sequence aligns to the horse850-residue model at88.6% identity. This supports the conserved adaptor mechanism and broad downstream cytokine/signaling claims. The cached abstract establishes IL-8; the separate DOI-linked full-paper excerpt documents the IL-6 result. Neither the Edison narrative nor ARBA is used as independent validation.

The reproducible alignment, source paths and hashes are in [the paired comparison](../../HORSE/AFAP1L2/AFAP1L2-bioinformatics/RESULTS.md). Current UniProt sequences have not been proven identical to the original ProtNLM input sequences. Sequence anomalies are therefore recorded as model/transfer limitations, not as proven wrong-input pipeline errors.

## Evidence gaps

The source excerpt file preserves the IL-6 sentence and full-paper URL because the publication cache is abstract-only. Consider tissue/condition-specific assays before treating cytokine phenotypes as universal horse physiology.

## Review scope and checks

Every seeded annotation receives a current assessment. UNDECIDED marks unresolved source-specific or biological evidence; these are initial reviews rather than a claim that every original experimental assay has been independently reproduced or verified. The human Edison report is retained as a research synthesis and source-finding aid; decisive YAML excerpts cite primary publications, source records or reproducible analysis. The validator advisory to cite the deep-research file is deliberately not satisfied by citing AI prose as biological proof.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used. Sources: cached publications, UniProt record, PANTHER/PAINT files, falcon deep research (used only to find primary papers; no claim rests on it).

### Identity
- Q8N4X5 is the reviewed, canonical 818-aa human AFAP1L2/XB130 (isoform 1 displayed; 4 isoforms). It is not a fragment or alternative gene model. Domains: N-terminal SH2/SH3-binding motif region, PH domains 175-271 and 353-447, coiled coil 652-749 (UniProt FT).
- PANTHER PTHR14338:SF4 (ACTIN FILAMENT-ASSOCIATED PROTEIN 1-LIKE 2). This is the 1:1 AFAP1L2 ortholog subfamily, separate from AFAP1 (SF8) and AFAP1L1 (SF1). Mouse Afap1l2 Q5DTU0 and the rat Afap1l2 gene products (UniProt REST: A0A8I5ZSJ9, F1M5W8, etc.) are also SF4. PTHR14338:SF9 has the same name but contains no members in the cached inventory.
- PAINT (interpro/panther/PTHR14338/PTHR14338-paint.tsv): PTN001023816 (Deuterostomia) has cytosol. PTN002682769 (Euteleostomi, AFAP1L2 clade) has GO:0030296, 0006954, 0007346, 0045742 and 0045893. Human Q8N4X5 is the only seed for every term. The curators did NOT propagate SH2/SH3 domain binding or the IL-6/IL-8 terms, and I take that as deliberate.

### Key primary evidence
- [PMID:17412687 "Their co-expression in COS-7 cells resulted in activation of c-Src"] Src binding and activation; knockdown reduces Src activity, IL-8, EGF-Akt and cell cycle.
- [PMID:19060924 "We identified tyrosine 54 of XB130 as the major target of RET/PTC-mediated phosphorylation and a critical binding site for the SH2 domains of p85alpha."] This is the core adaptor mechanism, with Akt selectivity (ERK unaffected).
- [PMID:22496359 "interaction with p85 PI3K leading to increased PI3K activities associated with PI3KAP/XB130"] Independent rat ortholog evidence (SF4).
- [PMID:26446840 "XB130 was found to bind specifically to the fifth SH3 domain of Tks5"] Plus Src Y416, p85, Akt and G1 effects of knockdown.
- [PMID:21084565 "In stimulated cells, XB130 localized to the lamellipodial F-actin meshwork."]
- [PMID:27462298 "this region is directly bound to F-actin in vitro"] Mouse construct (NM_001177796). The region is conserved in human per their Fig 2C, and it is distinct from the AFAP1/AFAP1L1 ABD.
- [PMID:34470464 "XB130 was found mainly on the apical membrane of thyroid follicles."] Mouse KO gives congenital hypothyroidism.

### Changes vs previous review
- Inflammatory response (IBA+IDA): KEEP_AS_NON_CORE changed to MARK_AS_OVER_ANNOTATED. The evidence is a cell-line cytokine readout, already covered by the IL-6/IL-8 production rows.
- Positive regulation of DNA-templated transcription (IBA+IDA): KEEP_AS_NON_CORE changed to MARK_AS_OVER_ANNOTATED. The evidence is a reporter readout for a cytoplasmic adaptor.
- Positive regulation of EGFR signaling (IBA+IDA): ACCEPT changed to KEEP_AS_NON_CORE. EGFR is one of several upstream inputs.
- Cytoplasm, cytosol, SH2/SH3 domain binding and PTK activator activity stay ACCEPT. Cell cycle and IL-6/IL-8 stay KEEP_AS_NON_CORE. Support now adds PMID:19060924 and PMID:26446840.
- NEW: GO:0036312 PI3K regulatory subunit binding (IPI, PMID:19060924); GO:0051897 positive regulation of PI3K/PKB signal transduction (IMP; participation as the p85 docking scaffold; comparator check: human IRS1 and GAB1 carry it in QuickGO); GO:0051015 actin filament binding (ISS from mouse SF4 ortholog); GO:0030027 lamellipodium (IDA); GO:0016324 apical plasma membrane (ISS, mouse SF4 ortholog).
- Not proposed (necessity, not participation): thyroid hormone generation, thyroid follicle/folliculogenesis, cell migration, endocytosis, T-cell survival (Canale 2023) and mitophagy (Ma 2024, HCC). These are recorded here only.
- Status set to COMPLETE; core functions rewritten (p85 adaptor/PI3K-Akt; Src activator; actin scaffold).

### Family/module checks
- interpro/panther/PTHR14338/PTHR14338-review.yaml places Q8N4X5 in SF4, which agrees with UniProt. It has no term assessments, so there is no conflict with these actions.
- No module in modules/ lists AFAP1L2/XB130.
