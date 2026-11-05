# wbpW (PA5452, Q9HTB7) notes

## Identity

TrEMBL entry, 479 aa, bifunctional phosphomannose isomerase / GDP-mannose
pyrophosphorylase (type II PMI family; NCBIfam TIGR01479 GMP_PMI; PANTHER
PTHR46390:SF1). It sits at the 5' end of the A-band (common polysaccharide
antigen) O-antigen cluster next to gmd (PA5453) and rmd (PA5454). Paralogues
in PAO1: AlgA (PA3551, alginate; ~same domain architecture) and PslB
(PA2232, Psl; ORF488 in Rocchetta et al.).
[file:PSEAE/wbpW/wbpW-uniprot.txt "GMP_PMI"]

UniProt name and FUNCTION text for this TrEMBL entry come from ARBA: the name
"Alginate biosynthesis protein AlgA" and "Produces a precursor for alginate
polymerization" belong to the paralogue AlgA. wbpW serves A-band LPS (and,
redundantly, Psl), not alginate. Not cited as support anywhere in the review.

## Literature

**Rocchetta, Pacan and Lam 1998, PMID:9781879 (abstract only; no PMC).**
- Complementation of E. coli PMI and GMP mutants (K30 capsule) by wbpW:
  [PMID:9781879 "To confirm the enzymatic activity of WbpW, Escherichia coli PMI and GMP mutants deficient in the K30 capsule were complemented with wbpW, and restoration of K30 capsule production was observed."]
  [PMID:9781879 "This indicates that WbpW, like AlgA, is a bifunctional enzyme that possesses both PMI and GMP activities for the synthesis of GDP-D-Man."]
- wbpW chromosomal mutants make very little A-band:
  [PMID:9781879 "The Rmd mutants do not produce A-band LPS, while the WbpW mutants synthesize very low amounts of A band after 18 h of growth."]
- The abstract reports no enzyme assay with WbpW protein; the activity claim
  rests on heterologous genetic complementation. The PseudoCAP IDA for
  GDP-mannose biosynthetic process (the seed) is therefore most likely an
  IGI-type experiment coded IDA. The term itself is right.

**Byrd et al. 2009, PMID:19659934 (full text cached).** wbpW and pslB are
redundant PMI/GMPs for A-band LPS and Psl:
[PMID:19659934 "In contrast to the other strains, the pslB wbpW double mutant failed to produce detectable A-band polysaccharide"]
[PMID:19659934 "indicating that A-band LPS synthesis requires the redundant PMI/GMP activity of either PslB or WbpW to generate product."]
[PMID:19659934 "Together, the attachment, immunoblot, and ELISA data confirm that, in a pslB mutant, WbpW is the PMI/GMP responsible for generating the GDP-d-Man essential in the production of Psl."]
The O antigen biosynthetic process row from this paper is coded IDA, but the
data are deletion mutants analysed by immunoblot: IMP (CONFIRMED
WRONG_EVIDENCE_CODE, full text read).

## Consistency with gmd and algA

gmd (PA5453, same A-band pathway) has LPS and O antigen biosynthetic process
ACCEPTed; wbpW rows for the same processes are ACCEPTed in the same way.
GDP-mannose is the shared precursor for A-band (via Gmd, Rmd), Psl and (via
AlgA) alginate. algA is reviewed in the same batch and shares PAINT node
PTN000283179.

## PseudoCAP IBA-seed assessment

Seeds from .cache/paint/IBD.gaf; E. coli ManC (P24174) experimental rows from
QuickGO 2026-11-05: GO:0004475 IDA PMID:4908790 (EcoCyc); GO:0009298 EXP
PMID:12514000 (EcoCyc, acts_upstream_of_or_within).

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000283179 | GO:0009298 GDP-mannose biosynthetic process | 2 | 30 (26 taxa) | GO:0009298, IDA, PMID:9781879 | SOUND | WbpW complements E. coli PMI and GMP mutants and is needed for A-band, a GDP-D-Man-derived polymer; the term is right. Evidence is heterologous complementation (IGI), not IDA: PSEUDOCAP WRONG_EVIDENCE_CODE, PROBABLE. Term suits a ManC/AlgA-type bifunctional PMI-GMP clade. | E. coli ManC P24174 (EXP, PMID:12514000) | Yes |

The sister IBD at the same node, GO:0004475 mannose-1-phosphate
guanylyltransferase (GTP) activity, is seeded by ManC (IDA) and AlgA (P07874,
PseudoCAP IDA, purified enzyme); see genes/PSEAE/algA. Both node IBDs stand;
no GO_CENTRAL defect for PTN000283179 (none needed, so none recorded on
either gene).

## Review decisions

- ACCEPT: GDP-mannose biosynthetic process (IBA, IDA, IEA); mannose-1-phosphate
  guanylyltransferase (GTP) activity (IBA, IEA); mannose-6-phosphate isomerase
  activity (IEA); LPS biosynthetic process (IMP); O antigen biosynthetic
  process (IDA, with evidence-code defect).
- TOO_GENERAL: polysaccharide biosynthetic process, polysaccharide metabolic
  process (O antigen biosynthetic process accepted), nucleotidyltransferase
  activity (GO:0004475 accepted).
