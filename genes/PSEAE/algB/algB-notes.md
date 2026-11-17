# algB (PA5483, P23747) review notes

## Literature summary

- AlgB is an NtrC-subclass regulator that controls algD expression and alginate output [PMID:1738315 "regulates the expression of the alginate biosynthetic gene, algD, thereby resulting in increased expression of alginate in mucoid P. aeruginosa"; "The predicted amino acid sequence of AlgB revealed a high degree of similarity to the regulatory proteins in the NtrC subclass"].
- AlgB is needed for algD transcription [PMID:1899859 "AlgB was shown to be involved in the transcription of algD"] and binds PalgD directly [PMID:17981963 "Chromosome immunoprecipitation revealed that AlgB bound in vivo to PalgD but did not bind when AlgB had an R442E substitution that disrupted the DNA binding domain."], activating a sigma-22 promoter [PMID:17981963 "in this case to stimulate transcription from the sigma(22)-dependent PalgD promoter"].
- The algD role is phosphorylation-independent [PMID:9473053 "Despite the defect in AlgB phosphorylation, P. aeruginosa strains expressing AlgB.D59N or H-AlgB delta1-145 remained mucoid."]; KinB is the cognate kinase [PMID:9473053 "kinB was identified downstream of algB and was shown to encode the cognate histidine protein kinase that efficiently phosphorylates AlgB"].
- In a kinB background, phosphorylated AlgB represses acute virulence [PMID:23024348 "These data suggest that in the absence of KinB, AlgB must be phosphorylated in order to repress virulence."]; deleting algB restores pyocyanin/elastase [PMID:23024348 "Similarly, algB deletion in PA14Δ kinB also restores wild-type levels of pyocyanin and elastase"] and complementation restores the reduced motility [PMID:23024348 "Episomal complementation of the algB deletion in the PA14Δ algB Δ kinB strain restores the reduced pyocyanin, elastase, and motility phenotypes of the PA14Δ kinB strain"].
- algB is needed for AlgW-dependent MucA degradation in a kinB mutant [PMID:19168621 "Our results also indicate that AlgW-mediated MucA degradation required algB and rpoN in the kinB mutant."]; that paper does not mention biofilm.

Literature search (2026-11-05): PubMed MCP and NCBI E-utilities failed all session; Europe PMC title search found
the AlgB papers. Full text read for PMID:23024348 and PMID:19168621 (the two multi-phenotype PseudoCAP sources);
PMID:1738315, 1899859, 17981963, 9473053 are abstract-only in cache.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000787214 | GO:0045893 positive regulation of DNA-templated transcription | 10 | 214 (28 taxa) | GO:0045893, IMP, PMID:1738315 | SOUND | AlgB activates algD transcription (algB mutant loses algD expression; AlgB binds PalgD by ChIP/EMSA/SELEX). | E. coli GlrR, PspF, RtcR, PrpR, AtoC (EcoCyc IDA/IMP); FhlA/NorR via other node terms; FleQ, CbrB, Vibrio/Xanthomonas/Geobacter EBPs (CollecTF) | Yes; many EcoCyc IDA seeds |

Node-level assessment for PTN000787214 is recorded once on fleQ (genes/PSEAE/fleQ/fleQ-notes.md), the gene with the
most direct evidence in this batch. The node is a sigma-54 enhancer-binding-protein clade (PTHR32071); its four IBD
terms (GO:0000987, GO:0001216, GO:0032993, GO:0045893) each rest on several independent experimental seeds and suit
the clade, so no GO_CENTRAL defect is filed. AlgB's own PseudoCAP IMP appearing in the WITH/FROM is expected.

## Source defects (non-seed PseudoCAP rows)

These rows are not IBD seeds; they are PseudoCAP annotations on algB from two multi-phenotype papers whose full text
was read:

- GO:0042121 alginic acid biosynthetic process (IMP, PMID:1738315, and the UniPathway IEA): AlgB is a regulator of
  algD, not an alginate enzyme. MODIFY to GO:0032885; PSEUDOCAP WRONG_TERM, CONFIRMED. A positive-regulation-of-alginate
  term is proposed.
- GO:1900378 positive regulation of secondary metabolite biosynthesis (IMP, PMID:23024348): sign inverted (AlgB
  represses pyocyanin in the kinB background). MODIFY to GO:1900377; PSEUDOCAP WRONG_TERM, CONFIRMED.
- GO:2000147 positive regulation of cell motility (IMP, PMID:23024348): sign inverted. MODIFY to GO:2000146;
  PSEUDOCAP WRONG_TERM, CONFIRMED.
- GO:0045862 positive regulation of proteolysis (IMP, PMID:23024348): the cited paper has no proteolysis assay;
  MARK_AS_OVER_ANNOTATED with a PSEUDOCAP WRONG_REFERENCE/CHECK defect (the MucA-proteolysis result is in PMID:19168621).
- GO:1900232 negative regulation of biofilm formation (IMP, PMID:19168621): the cited paper does not mention biofilm;
  UNDECIDED with a PSEUDOCAP WRONG_REFERENCE/CHECK defect.

## Action summary

15 rows. ACCEPT 4; MODIFY 4 (GO:0042121 x2, GO:1900378, GO:2000147); KEEP_AS_NON_CORE 3 (GO:0032993, GO:0000160,
GO:0005524); TOO_GENERAL 2 (GO:0006355, GO:0043565); MARK_AS_OVER_ANNOTATED 1 (GO:0045862); UNDECIDED 1 (GO:1900232).
