# ybbO (b0493, P0AFP4) — Escherichia coli K-12 — curation notes

## 2026-10-30 session

- Deep research providers (falcon, perplexity) are not configured in this environment;
  literature found by PubMed search (`ybbO[tiab]`, `YbbO AND coli`) and cached.
- Classical SDR, PTHR43313 (SDR family 9C) subfamily SF1. One-to-one orthologue of
  Salmonella STM0505 (Q7CR11): reciprocal best hit, conserved ybbN/cnoX-ybbO-tesA-ybbA
  neighbourhood, 90.6% identity (file:SALTY/ybbO/ybbO-bioinformatics/RESULTS.md).
  E. coli numbering is +13 relative to Salmonella because P0AFP4 carries a 13-residue
  N-terminal extension (MTHKATEILTGKV); UniProt ACT_SITE Tyr159 = Salmonella Tyr146.

### Activity evidence (all from metabolic-engineering contexts)

- Short/medium-chain aldehydes, in vitro, purified enzyme:
  [PMID:25108218 "YbbO showed broad substrate activity toward all the C2–C10 aldehydes
  with the highest activity toward hexanal and octanal"]; "all five appear to be strictly
  NADPH dependent with the substrates tested"; about 10-fold lower than DkgA/YahK.
- Long-chain fatty aldehydes: [PMID:27134112 "deletion of ybbO gene, which encodes NADP(+)
  dependent aldehyde reductase, led to >90% reduction in long chain fatty alcohol
  production"]; kinetics C6-C18, best affinity C18, best efficiency C16 (abstract only).
- Retinal: [PMID:25726762 "Retinol was produced by the ybbO gene of E. coli which encodes
  oxidoreductase"]; overexpression raises the retinol fraction. Independently,
  [PMID:34361955 "deletion of the ybbO gene, which decreased retinoic acid titer through
  the reduction of retinal to retinol"] and [PMID:41093029 "knocking out aldehyde
  reductase ybbO could prevent retinal loss"]. YbbO is used heterologously as the retinal
  reductase for retinol production in yeast (PMID:38647788, PMID:39307776).
  Retinal reduction fits the SDR9C family, whose vertebrate members (RDH16, RDH5,
  HSD17B6, DHRS9) are retinol / hydroxysteroid dehydrogenases.
- Negative: ybbO deletion had no effect on glutaraldehyde survival
  [PMID:34248896 "None of the genes classified as aldehyde reductases (yahK, ybbO, yghA,
  and ahr) had an impact in glutaraldehyde survival"].

### Open issues

- Physiological substrate unknown: E. coli makes neither retinoids nor much free
  long-chain fatty aldehyde. Neighbour tesA (acyl-CoA thioesterase / lysophospholipase)
  hints at lipid metabolism but is not evidence.
- The 13-residue N-terminal extension is shared with Shigella, Klebsiella and
  E. marmotae entries but absent from most Enterobacterales orthologues (256-261 aa); it
  may reflect an upstream start call. Not recorded as a gene_model_issue: no proteomic or
  N-terminal sequencing evidence was examined.

## Decisions

- GO:0008106 IDA x2: ACCEPT.
- GO:0016491 IBA: MODIFY -> GO:0008106 (same as Salmonella review).
- NEW GO:0052650 all-trans-retinol dehydrogenase (NADP+) activity, IMP, from PMID:25726762
  and PMID:34361955; non-physiological substrate in E. coli, kept out of core function
  label but mentioned.
