# hom (PA3736, P29365) notes

Review of *Pseudomonas aeruginosa* PAO1 homoserine dehydrogenase for the PseudoCAP
IBA-seed project (worklist rank 25). No deep-research provider was available, so these
notes are from my own reading of UniProt, PubMed and the cached publications.

## Biology

- Hom catalyses the third step from aspartate: L-aspartate 4-semialdehyde + NAD(P)H
  -> L-homoserine. UniProt states it is "the third step in the biosynthesis of
  threonine and methionine from aspartate" (by similarity to *C. glutamicum*-type
  P31116) [file:PSEAE/hom/hom-uniprot.txt CC:FUNCTION].
- Domain architecture: NAD(P)-binding Rossmann domain (PF03447), homoserine
  dehydrogenase catalytic domain (PF00742) and a C-terminal ACT domain (PF01842,
  353-429), consistent with threonine feedback regulation. PANTHER PTHR43331:SF1.
- Clepet et al. 1992 cloned and sequenced the PAO1 thr genes: "hom, thrB and thrC,
  encoding homoserine dehydrogenase (HDH), homoserine kinase (HK) and threonine
  synthase (TS)"; "HDH activity was feedback inhibited by threonine" [PMID:1333566].
  hom and thrC form an apparent bicistronic operon at the thr locus [PMID:1333566].
  The abstract does not say how HDH was assayed (extracts of PAO1 or of a clone).
- Hom is the only homoserine dehydrogenase in the PAO1 proteome (checked against the
  UniProt PAO1 proteome list in `.cache/paint/pao1.tsv`; no second HDH or ThrA-type
  bifunctional protein). So homoserine for both branches comes from Hom: the threonine
  branch (ThrB/ThrH, ThrC) and the methionine branch (MetXS homoserine
  O-succinyltransferase PA0390, MetZ O-succinylhomoserine sulfhydrylase PA3107).
  The methionine ISS row is therefore well founded.

## PMID:10220164 (the PseudoCAP seed reference)

Patte et al. 1999, "ThrH, a homoserine kinase isozyme with in vivo phosphoserine
phosphatase activity". The abstract is entirely about ThrB and ThrH: threonine
auxotrophy "is observed only when both thrB and thrH are simultaneously inactivated"
[PMID:10220164]. It does not mention hom or homoserine dehydrogenase. PseudoCAP used
this same paper (all IDA, same date 20190311) for thrB, hom and thrH
(`.cache/paint/pseudocap.tsv`), which looks like a batch annotation of the thr genes
to one paper. The full text (Microbiology 1999) is not in PMC, so I cannot rule out an
HDH assay in it. Following the repository rule, I do not REMOVE: the claims (HDH
activity, threonine biosynthesis) are correct for this gene, and the 1992 paper from
the same group (PMID:1333566) does report HDH activity and threonine feedback for the
P. aeruginosa enzyme. I record a PSEUDOCAP WRONG_REFERENCE CHECK defect (SUSPECTED).

## PAINT node PTN000752178

From `.cache/paint/IBD.gaf`: GO:0009088 seeded by P29365 only; GO:0004412 seeded by
P29365 and B. subtilis P19582. The 41 leaves (from the PAINT leaf GAF) are all
homoserine dehydrogenases or ThrA/MetM-type HDH proteins across bacteria, archaea,
algae, trypanosomatids and *Nematostella* (e.g. P9WPX1 *M. tuberculosis* hom, Q7DDD6
*N. meningitidis* metM, O67677 *Aquifex* thrA). Every HDH supplies homoserine to the
threonine branch, so L-threonine biosynthetic process suits the clade; it is not the
whole story, since the same step feeds methionine (and, via threonine, isoleucine).
L-homoserine biosynthetic process (GO:0009090) is the most exact BP for the step; a
methionine IBD at the same node would be equally justified.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN000752178 | GO:0009088 L-threonine biosynthetic process | 1 (sole seed) | 41 (35 taxa) | GO:0009088 L-threonine biosynthetic process, IDA, PMID:10220164 (PseudoCAP) | UNVERIFIABLE | The claim is correct (Hom catalyses step 3/5 of threonine synthesis; its activity is feedback-inhibited by threonine, PMID:1333566), so the IBD is biologically sound and suits an all-HDH clade. But the cited paper's abstract is about ThrB/ThrH only and the full text is unavailable; it looks like a batch citation. Better reference: PMID:1333566. The node term is right but partial: HDH equally feeds methionine. |
| PTN000752178 | GO:0004412 homoserine dehydrogenase activity | 2 | 41 (35 taxa) | GO:0004412 homoserine dehydrogenase activity, IDA, PMID:10220164 (PseudoCAP) | UNVERIFIABLE | Activity is certainly right for Hom (PMID:1333566 reports HDH activity of the P. aeruginosa enzyme), and the second seed (B. subtilis P19582) supports the IBD independently. The cited paper does not visibly assay HDH. |

## Decisions summary

- ACCEPT: homoserine dehydrogenase activity (IBA, IDA, IEA, ISS), L-threonine
  biosynthetic process (IBA, IDA, IEA), L-methionine biosynthetic process (ISS).
- MODIFY to GO:0004412: alcohol dehydrogenase (NAD+) activity (IEA Rhea),
  oxidoreductase activity (IEA).
- MODIFY amino acid metabolic process (IEA) to L-homoserine biosynthetic process.
- KEEP_AS_NON_CORE: NADP binding (IEA), NAD+ binding (ISS) (cofactor binding implied by
  the activity).
- Source defect: PSEUDOCAP WRONG_REFERENCE CHECK (SUSPECTED) on both IDA rows.
