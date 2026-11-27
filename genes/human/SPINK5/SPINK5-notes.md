# SPINK5 (Q9NQ38) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: SPINK5 was reviewed as the closest experimentally characterised relative of fly CG32354 (Q9VSK1).
No ProtNLM2 output was consulted.

### Deep research
`just deep-research-falcon human SPINK5 --fallback perplexity-lite` failed: Edison (falcon) returned
`403 Forbidden` at authentication, and the perplexity-lite fallback timed out after 600 s. No deep-research
file exists. The review rests on the cached primary literature listed below (mostly abstract-only;
PMID:17596512 and PMID:19414552 have full text).

### Evolutionary grounding
- PANTHER 19.0: PTHR10913 (FOLLISTATIN-RELATED), subfamily SF71 "SERINE PROTEASE INHIBITOR KAZAL-TYPE 5".
  UniProt still cross-references the older PTHR47499:SF1.
- Tree analysis (`SPINK5-bioinformatics/panther_tree.py`, RESULTS.md): the serine-type endopeptidase
  inhibitor IBD node PTN000099251 (Theria) covers only 12 therian SPINK5 orthologs. Mouse Spink5 (Q148R4)
  is inside it, so mouse findings transfer. TMEFF2 diverges at the Euteleostomi duplication; fly CG32354 and
  Fs share only the Bilateria speciation node PTN000857333.
- Implication for transfer to fly: the inhibitor activity should not be projected to Q9VSK1. PAINT placed
  the IBD at Theria deliberately.

### Function (experimental, human protein unless stated)
- Trypsin inhibition by native domain HF7665 [PMID:10419450 "An inhibitory effect of HF7665 on trypsin activity is demonstrated."]
- Full-length recombinant LEKTI inhibits plasmin, subtilisin A, cathepsin G, elastase and trypsin, but not
  chymotrypsin or cysteine proteinases [PMID:12667078 "rLEKTI did not inhibit the cysteine proteinase papain or cathepsin K, L, or S."]
- Domain 6 inhibits KLK5 and KLK7 [PMID:16307658 "LEKTI domain 6 is a potent inhibitor of hK5 and hK7"]
- Furin fragments inhibit KLK5, KLK7 and KLK14; pH-dependent release of KLK5
  [PMID:17596512 "All LEKTI fragments, except D1, showed specific and differential inhibition of human kallikreins 5, 7, and 14."]
- Caspase 14 inhibition in vitro, single study [PMID:20533828]; not used for GO.
- Localization: lamellar granules, then extracellular space of the stratum granulosum [PMID:15675955].
- Mouse genetics: Spink5-null mice show DSG1 degradation and barrier loss [PMID:15619623], increased
  profilaggrin processing [PMID:15590704], KLK5-PAR2-TSLP inflammation [PMID:19414552], and increased
  cathelicidin antimicrobial activity [PMID:17012259].

### Decisions in brief
- Core MF: GO:0004867 (ACCEPT IBA + two IDA). GO:0030414 MODIFY to GO:0004867.
- Extracellular region rows MODIFY to extracellular space (GO:0005615). Lamellar body ACCEPT.
- Differentiation terms (epidermal, epithelial, IBA cell differentiation) MARK_AS_OVER_ANNOTATED: the
  evidence is that LEKTI is a differentiation marker, or the phenotype is downstream of protease
  hyperactivity.
- REMOVE: negative regulation of angiogenesis (no evidence), hair cell differentiation (sensory hair cell
  term; Netherton hair defect is a hair shaft defect).
- Cytosol IDA is from a signal-peptide-deleted mutant, so MARK_AS_OVER_ANNOTATED.
- No NEW terms. Desquamation and skin barrier are processes that LEKTI regulates rather than performs, and
  GO has no "regulation of corneocyte desquamation" term; this is raised as a question in the review.
