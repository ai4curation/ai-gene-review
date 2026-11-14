# tpbB / yfiN (PA1120, Q9I4L5) review notes

No deep-research provider was available; literature checked by hand on 2026-11-05
(cached publications, PMC web pages, Europe PMC search "PA1120", "YfiN", "TpbB").

## Function

- TpbB/YfiN is an inner-membrane diguanylate cyclase (2 TM helices, periplasmic PAS-like
  domain, cytoplasmic HAMP and GGDEF domains; UniProt topology).
- A purified truncated YfiN makes c-di-GMP from GTP [PMID:20300602 "In accordance with these
  findings, truncated-YfiN-His6 generated c-di-GMP from GTP, confirming that YfiN functions as a
  DGC (Figure 2A)."].
- YfiR represses it and YfiB relieves that repression [PMID:20300602 "Together, these data
  strongly suggest that YfiR functions to negatively regulate YfiN, and that the ΔyfiR SCV
  phenotype results from de-repression of YfiN DGC activity, leading to increased levels of
  c-di-GMP."].
- The cytosolic HAMP-GGDEF construct is active in real time, and it is not product-inhibited
  [PMID:24278422 "Here we show that, unlike other DGC enzymes, YfiN does not undergo product
  feedback inhibition, and that the in vitro activity depends on the presence of the HAMP
  domain."].
- Genetics: loss of tpbB suppresses the tpbA (phosphatase) mutant's high-c-di-GMP phenotypes
  [PMID:19543378 "Loss of an uncharacterized GGDEF protein, PA1120 (TpbB), suppressed these
  phenotypes, indicating that TpbA controls c-di-GMP production through TpbB."].

## Verbatim excerpts from PMID:16477007 full text (PMC1413825, PMC web page, read 2026-11-05)

Table 1 (cells overexpressing each gene in PA14, c-di-GMP measured by HPLC):

- PA1120 GGDEF +(134)
- PA0847 GGDEF +(16)
- DGC activity is measured as pmol of c-diGMP produced per mg wet cell weight.
- Given the limits of sensitivity of the HPLC assay (12 pmol/mg cell wet weight), we cannot conclude that any particular DGC or PDE domain does not have the corresponding enzymatic activity in vivo .

Text: "To detect DGC activity, cultures overexpressing genes that encode DGC-containing proteins
were extracted and analyzed for c-di-GMP content".

## PseudoCAP IBA-seed assessment

Seeds from .cache/paint/IBD.gaf; other seeds' experimental rows from QuickGO, 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN005315326 | GO:0052621 diguanylate cyclase activity | 5 | 35 (16 taxa) | GO:0052621, IDA, PMID:16477007 (PseudoCAP) | SOUND | PA1120-overexpressing cells held 134 pmol c-di-GMP/mg (Table 1, full text read), well above the 12 pmol/mg limit; confirmed with purified protein (PMID:20300602, PMID:24278422). | PA0847 Q9I594 (purified PAS-GGDEF active, PMID:31114257); V. cholerae VCA0965 Q9KKY5 (IDA PMID:24490592, CACAO); E. coli DgcT P75908 (IMP PMID:18713317, PMID:20576684, EcoCyc); Dictyostelium DgcA DDB_G0283453 | Yes |
| PTN005315326 | GO:0052621 diguanylate cyclase activity | 5 | 35 (16 taxa) | GO:0052621, IMP, PMID:19543378 (PseudoCAP) | SOUND | Full text read. Genetic epistasis: tpbB loss suppresses the high-c-di-GMP tpbA phenotypes; the activity itself is shown elsewhere. Weak as MF evidence but not wrong. | as above | Yes |

The node term (the catalytic activity) suits a clade of GGDEF DGCs with intact catalytic
sites. No PSEUDOCAP or GO_CENTRAL defect. The PA0847 seed on the same node is assessed in
PA0847-notes.md (also SOUND); the two verdicts agree.

GO:0061939 c-di-GMP signaling (IBA on the same node, seeded only by DgcA): accepted; TpbB's
c-di-GMP output drives Pel/Psl production.
