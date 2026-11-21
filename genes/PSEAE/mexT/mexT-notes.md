# mexT (PA2492, Q9I0Z0) notes

Sources read on 2026-11-05: UniProt Q9I0Z0 (MEXT_PSEAE), the GOA file, cached abstracts
of PMID:9044268, PMID:10515918, PMID:20727012, and cached full texts of PMID:21075931,
PMID:19846594, PMID:31722511, PMID:39708318, PMID:41128522. PMID:31859619 (PAO1 subline
mexT variability) is cited by UniProt but not cached and was not read. No deep-research
provider file (no keys). LysR comparators already reviewed: genes/PSEAE/ampR, trpI
(different PAINT node, PTN000794521).

## Biology

- MexT is a LysR-type activator encoded upstream of mexEF-oprN; nfxC-type mutants
  overexpress the pump
  [PMID:10515918 "Sequencing of the DNA region upstream of the mexEF-oprN operon revealed the presence of an open reading frame (ORF) of 304 amino acids encoding a LysR-type transcriptional activator, termed MexT."];
  MexT also activates qrh (mexS)
  [PMID:10515918 "Expression of a qrh::lacZ fusion was also found to be activated by MexT."].
- Purified MexT binds the mexT-proximal nod box of the mexE promoter
  [PMID:20727012 "The mexT-proximal nod box was identified as the MexT-binding site by gel-shift assays using purified MexT."];
  DNase I footprinting finds two sites
  [PMID:31722511 "A DNase I footprinting assay of full-length MexT identified two MexT-binding sequence in the mexEF oprN promoter."].
- MexT directly activates a regulon of ~12 genes with a conserved motif, independent of
  MexEF-OprN [PMID:19846594 "Thus, a novel regulon directly modulated by MexT, that includes but is independent of mexEF-oprN, has been identified."].
- Full-length MexT is a homotetramer (SEC-MALS), RD a dimer
  [PMID:31722511 "FL MexT and MexT RD were homotetrameric and homodimeric in solution, respectively, as determined using SEC-MALS"].
- Indirect/pleiotropic roles: in PAO1, mexT (with mexS) represses T3SS (ExoS secretion),
  elastase and pyocyanin (PMID:21075931, full text); loss of MexT raises aminoglycoside
  and colistin resistance and virulence (PMID:39708318); MexT shapes the QS hierarchy,
  mostly through MexEF-OprN export of quinolones
  [PMID:41128522 "we hypothesized that constitutive MexT activity induces mexEF-oprN expression, leading to the repression of PQS QS, delayed pqsE expression, and delayed RhlR activation."].

## Annotation judgements (summary)

- Core: GO:0001216 activator activity, GO:0000976 cis-regulatory region binding,
  GO:0045893 positive regulation of transcription (ACCEPT on all experimental and IBA
  rows).
- GO:0003700, GO:0006355: TOO_GENERAL (entailed by GO:0001216 / GO:0045893).
- GO:0001217 repressor activity (UniProt IMP, PMID:41128522): the full text attributes
  pqs repression to MexEF-OprN, not to MexT binding the pqs promoter. MARK_AS_OVER_ANNOTATED.
- GO:0045892 negative regulation of transcription (same paper): KEEP_AS_NON_CORE (true in
  the indirect sense).
- GO:0045861 negative regulation of proteolysis (PseudoCAP, PMID:21075931): rests on more
  elastase in the mutant. MexT is a transcription factor; it does not act on proteolysis.
  REMOVE with PSEUDOCAP WRONG_TERM (CONFIRMED, full text read).
- GO:0050709 negative regulation of protein secretion (PseudoCAP): mexT mutant secretes
  more ExoS; MexT represses T3SS through MexS. KEEP_AS_NON_CORE.
- GO:1900377 negative regulation of secondary metabolite biosynthetic process (PseudoCAP):
  pyocyanin; MODIFY to GO:1900981 negative regulation of phenazine biosynthetic process
  (no negative pyocyanine-regulation term exists).
- GO:0046677 response to antibiotic: resistance phenotypes, not a response.
  MARK_AS_OVER_ANNOTATED.
- GO:0009372 quorum sensing, GO:0010629 negative regulation of gene expression:
  KEEP_AS_NON_CORE.

## PseudoCAP IBA-seed assessment

Other seeds' experimental support queried live in QuickGO on 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001248361 | GO:0006355 regulation of DNA-templated transcription | 3 | 46 (9 taxa) | GO:0045893, IMP, PMID:10515918 (PseudoCAP) | SOUND | Abstract: mexE::lacZ and qrh::lacZ are activated by MexT. Direct binding shown later (PMID:20727012, PMID:31722511). | E. coli LeuO P10151 (EcoCyc IMP GO:0006355, PMID:9422614), S. Typhimurium LeuO P46924 (CollecTF IPI/IEP GO:0000976, GO:0001216, GO:0045893, PMID:22149171); MexT also has CollecTF and UniProt rows | Yes; both LeuO seeds have experimental support |

The node term is generic and suits a 9-taxon clade of LysR regulators. No PSEUDOCAP
defect on the seed row and no GO_CENTRAL defect on PTN001248361. The node's other IBDs
(GO:0001216, GO:0000976, GO:0032993) are seeded by MexT and S. Typhimurium LeuO and are
also sound. ampR and trpI sit on PTN000794521, not this node.

Defects recorded: PSEUDOCAP WRONG_TERM on GO:0045861 (CONFIRMED). GO:1900377 is a
refinement (MODIFY to GO:1900981), not an error, so no defect.
