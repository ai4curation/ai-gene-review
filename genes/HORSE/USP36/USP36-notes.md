# USP36 (horse, Equus caballus) - F6W2H6

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Cohort: DONKEY40 + DONKEY40_HORSE_PARTNER (horse partner of donkey USP36 A0A9L0JCH5). No prior review existed; folder created with `just fetch-gene HORSE F6W2H6 --alias USP36` (stub id confirmed F6W2H6). ProtNLM2 output was not consulted.

### Deep research
`just deep-research-falcon HORSE USP36 --fallback perplexity-lite` failed: Edison/falcon returned 403 "Failed to authenticate" and perplexity returned 401 insufficient_quota. Review proceeded from cached literature and the human UniProt record.

### Identity
- F6W2H6 is unreviewed TrEMBL, 1123 aa, PE 3; USP domain 122-423, ACT_SITE Cys131 / His382.
- Full-length ortholog of human USP36 Q9P275 (1123 aa): 77.8% identity overall, 96.0% in the USP domain, 81.3% in the C-terminal nucleolar-targeting block, 67.2% in the disordered middle; catalytic residues conserved [file:HORSE/USP36/USP36-bioinformatics/RESULTS.md]. Not a fragment, isoform or defective model.
- PANTHER: PTHR24006:SF653 (UBIQUITIN CARBOXYL-TERMINAL HYDROLASE 36) for both horse and human (UniProt DR lines) -> same subfamily, function transfer justified. No family review exists under interpro/panther/PTHR24006 (only paint/entries/metadata files), so no subfamily disagreement to report.
- IBA nodes: PTN002541993 (family-wide; DUB activity, nucleus, cytosol, regulation of protein stability; human USP36 is a donor for the last) and PTN002541928 (regulation of apoptotic process; seeds FBgn0260936 and Q0WX57).

### Biology (human/mouse/yeast ortholog evidence)
- Nucleolar DUB of nucleophosmin and fibrillarin; depletion lowers rRNA transcription/processing [PMID:19208757 "USP36 deubiquitylated the nucleolar proteins nucleophosmin/B23 and fibrillarin, and stabilized them by counteracting ubiquitylation-mediated proteasomal degradation"].
- Nucleolar targeting by C-terminal basic stretches [PMID:19208757 "USP36 localized to nucleoli via the C-terminal region, which contains basic amino acid stretches"].
- DHX33 stabilization; mouse knockout preimplantation lethal [PMID:29273634 "USP36 reduces the ubiquitination levels and increases the stability of the DEAH-box RNA helicase DHX33"].
- Yeast Ubp10 ortholog; human USP36 complements ubp10 deletion [PMID:22902402 "USP36, the human ortholog of Ubp10, complements the ubp10Δ allele for RNAPI stability, pre-rRNA processing, and cell growth in yeast"].
- MYC deubiquitination in nucleolus [PMID:25775507]; H2Bub1 deubiquitinase [PMID:29274341 "USP36 interacts with H2B and deubiquitinates H2Bub1 in cells and in vitro"]; K48 deubiquitination of CEP63 [PMID:35989368]; restrains p62-dependent selective autophagy [PMID:22622177]; cytoplasmic pool regulating NEDD4L/TrkA [PMID:27445338]; SUMO ligase for EXOSC10 [PMID:36912080, not in GOA; raised as question, not added as NEW].

### Decisions (20 rows)
- ACCEPT (8): DUB activity (IBA, IEA), nucleolus, protein deubiquitination, protein stabilization, H2B DUB, K48-linked DUB, regulation of rRNA processing.
- MODIFY (4): nucleus IBA -> nucleolus; chromatin organization -> chromatin remodeling; regulation of protein stability (IBA, IEA) -> protein stabilization.
- KEEP_AS_NON_CORE (7): cytoplasm, cytosol, chromatin remodeling, nucleolus organization, negative regulation of macroautophagy, nuclear speck, regulation of apoptotic process (IBA; downstream of impaired ribosome biogenesis).
- MARK_AS_OVER_ANNOTATED (1): ubiquitin-dependent protein catabolic process (UniRule) - USP36 opposes degradation of its substrates.

### Relative / modules
- Next relative: human USP36 (Q9P275), same PANTHER subfamily SF653; no review in repo (no genes/human/USP36, no mouse Usp36). Donkey USP36 (genes/EQUAS/USP36) is the cohort partner, reviewed separately.
- No module in modules/ mentions USP36/Q9P275.
