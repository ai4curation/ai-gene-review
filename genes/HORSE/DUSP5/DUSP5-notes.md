# DUSP5 (horse, F7ALT2) - review notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Cohort: DONKEY40 horse partner (donkey target A0A8C4MED2 is reviewed separately in genes/EQUAS/DUSP5). ProtNLM2 output was not opened or used.

### Deep research
- `just deep-research-falcon HORSE DUSP5 --fallback perplexity-lite` failed: Edison/falcon returned 403 on login ("Failed to authenticate") and the perplexity-lite fallback returned 401 insufficient_quota. No deep-research file exists; the review uses cached literature on the human ortholog.

### Identity
- F7ALT2 is 384 aa, the same length as human canonical DUSP5 Q16690 (384 aa), 94.5% identical with no gaps [file:HORSE/DUSP5/DUSP5-bioinformatics/RESULTS.md "identity 363/384 paired residues = 94.53%"]. Not a fragment, isoform or alternative gene model.
- Catalytic Cys263 and the HCEAGISRS P-loop are conserved; the 22-residue NLS mapped in human DUSP5 is identical.
- PANTHER: UniProt places F7ALT2 in PTHR10159:SF40 (DUAL SPECIFICITY PROTEIN PHOSPHATASE 5), the same subfamily as human Q16690 and rat O54838 (interpro/panther/PTHR10159/PTHR10159-entries.csv). This is the evolutionary basis for transferring human DUSP5 function. No PTHR10159 family review exists in interpro/panther/ (only entries and metadata files), so there is no placement disagreement to report.

### Literature (human ortholog)
- [PMID:15713638 "We conclude that DUSP5 is an inducible nuclear ERK-specific MAP kinase phosphatase that functions as both an inactivator of and a nuclear anchor for ERK2 in mammalian cells."]
- Specificity: [PMID:15713638 "it inactivates ERK2 but not Jun N-terminal protein kinase or p38 MAP kinase"].
- Nuclear: [PMID:15713638 "DUSP5 can thus be regarded as a nuclear equivalent of the cytoplasmic ERK-specific phosphatase MKP-3/DUSP6."]
- Original cloning (B23/hVH3), dual-specificity activity highest toward phospho-ERK1 [PMID:7961985, abstract only].

### IBA node analysis
- Endoderm formation (PTN000017039): single donor ZFIN:ZDB-GENE-040426-709 = zebrafish dusp4 (UniProt Q7SZF3, checked via UniProt REST). Paralog, developmental phenotype -> MARK_AS_OVER_ANNOTATED.
- Cytoplasm (PTN001605855): seeded by cytoplasmic MKPs (DUSP6/7/9/16, yeast/plant); DUSP5 is nuclear -> MARK_AS_OVER_ANNOTATED. Note PAINT placed the nucleus IBD at the inducible-nuclear-MKP node PTN000806857 (DUSP1/2/4 donors) -> ACCEPT.
- Phosphoprotein phosphatase (PTN004128558) includes human DUSP5 Q16690 as donor -> MODIFY to GO:0017017.
- Negative regulation of MAPK cascade -> MODIFY to GO:0070373 (ERK-selective). Signal transduction -> MODIFY to GO:0070373 (regulator, not relay).

### Decisions
- Core: GO:0017017 (ACCEPT, InterPro2GO), nucleus (ACCEPT x2), GO:0070373 via MODIFY.
- GO:0004722 and GO:0004725 (EC mapping) ACCEPT: GO:0017017 is not their descendant (OLS ancestors of GO:0017017 are GO:0033549, GO:0008138, GO:0004721...), so they are non-redundant halves of the dual activity.
- GO:0008138, GO:0016791, GO:0016787 -> MODIFY to GO:0017017.
- No NEW terms. Nuclear anchoring of ERK2 raised as a suggested question instead of a protein-localization process term.

### Relative
- Human DUSP5 (Q16690), ortholog in PTHR10159:SF40; no review exists in genes/human/ -> needs review.
- Modules: modules/erk_cascade.yaml has a DUSP/MKP negative-feedback step (PTHR10159, DUSP6 representative); DUSP5 is not listed but is a nuclear member of that step.
