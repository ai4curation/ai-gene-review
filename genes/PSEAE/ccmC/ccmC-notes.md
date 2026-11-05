# ccmC (PA1477, Q9I3N5) notes

## Identity

- Heme exporter protein C / cytochrome c-type biogenesis protein CcmC, 252 aa,
  six predicted TM helices, CcmC/CycZ/HelC family (TIGR01191, IPR003557,
  IPR045062 WWD domain). UniProt PE 3 (homology); function statement is
  ECO:0000250 ("Required for the export of heme to the periplasm for the
  biogenesis of c-type cytochromes").
- Part of System I cytochrome c maturation (CcmABCDEFGH). CcmC is the
  membrane subunit of the CcmA2B1C1(D) ABC-type complex that loads heme onto
  the periplasmic heme chaperone CcmE.

## Mechanism (E. coli orthologue, P0ABM1)

- [PMID:11384983 "CcmC is necessary and sufficient to incorporate heme into CcmE. Here, we report that the CcmC protein directly interacts with heme."]
- [PMID:20599545 "For the first time, evidence that the external WWD domain of CcmC interacts directly with heme is presented."]
- [PMID:16824107 "In the absence of CcmA or CcmB, holo(haem)CcmE binds to CcmC in a stable dead-end complex, indicating high affinity binding of haem to CcmC."] (E. coli; MeSH terms list Escherichia coli and no Pseudomonas.)
- [PMID:36307425 "We locate the ATP-binding site in CcmA and the heme-binding site in CcmC."]
- [PMID:37626034 "Our data suggest that the complex flops a heme group from the inner to the outer leaflet at its CcmBC interfaces, driven by ATP hydrolysis at CcmA."]
- [PMID:37626034 "A conserved heme-handling motif (WxWD) at the periplasmic side of CcmC rotates the heme by 90° for covalent attachment to the heme chaperone CcmE"]
- Whether CcmABCD transports heme across the membrane or only ligates
  membrane heme to CcmE and releases holoCcmE is still debated; the 2023
  structure favours a flippase-like heme translocation.

## P. aeruginosa / Pseudomonas genetics

- Baert et al. 2008 (PMID:18174132), the P. aeruginosa ccmC mutant paper:
  [PMID:18174132 "Only in the case of the ccmC mutant was cytochrome c production totally abrogated."]
  Pleiotropic phenotypes: low pyoverdine, increased pyochelin, reduced
  pyocyanin, swarming and twitching motility, rhamnolipid; porphyrin
  accumulation; [PMID:18174132 "catalase production was undetectable, consistent with the increased sensitivity to hydrogen peroxide"]; reduced [Fe-S]
  clusters; complemented by P. fluorescens ccmC.
- P. fluorescens ATCC 17400: ccmC mutant is cytochrome c-deficient and
  pyoverdine-deficient; residue substitutions partly separate the two
  phenotypes [PMID:9822820 "Simultaneous replacements of residues Trp-115 and Gly-116 in the second periplasmic loop substantially affected pyoverdine production/utilization but not cytochrome c production."]
- Pyoverdine maturation defect attributed to periplasmic redox:
  [PMID:12123798 "We suggest that the conversion of ferribactin to pyoverdine does not take place in the DeltaccmC mutant because of lack of oxidizing power in the periplasm."]
- Catalase defect attributed to heme supply to heme catalases:
  [PMID:14663086 "Significantly reduced resistance to oxidative stress mediated by haem-containing catalases was observed for the ccmC mutant."]
  and [PMID:14663086 "It was concluded that CcmC, apart from its known function in cytochrome c biogenesis, plays a role in haem biosynthesis."]

## Reference problem in PseudoCAP rows

All six PseudoCAP IMP rows (catalase activity, pyoverdine biosynthesis,
glycolipid biosynthesis, type IV pilus motility, swimming, swarming; dated
2019-03-11) cite PMID:16824107 (Feissner et al. 2006, Kranz lab). Its
abstract describes biochemistry of the CcmABC complex without naming the
organism; MeSH indexes Escherichia coli and not Pseudomonas, and neither
abstract nor MeSH contains a P. aeruginosa mutant or any of these phenotypes. The phenotypes match,
one for one, the abstract of Baert et al. 2008 (PMID:18174132), the
P. aeruginosa ccmC mutant paper (swimming is not in that abstract; it may be
in the full text). Most likely the PseudoCAP rows were keyed to the wrong
PMID. Neither paper's full text was available here (both abstract-only,
no PMC copy; rechecked 2026-10-29), so the WRONG_REFERENCE defects stay
PROBABLE, not CONFIRMED.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN001247822 | GO:0004096 catalase activity | 1 (sole seed) | 143 (59 taxa) | GO:0004096 catalase activity, IMP, PMID:16824107 (PseudoCAP) | INDIRECT-PHENOTYPE (also WRONG reference) | CcmC is a 6-TM heme-handling subunit of the Ccm heme-delivery complex with no catalase domain or catalytic residues. The only evidence is loss of catalase activity in the P. aeruginosa ccmC mutant (PMID:18174132, abstract), explained by impaired heme supply to the heme catalases (KatA/KatB). The cited PMID:16824107 is an E. coli Ccm biochemistry paper that does not assay catalase. The seed is unsound, so the IBD and all 143 catalase-activity IBAs from PTN001247822 (including the one back onto ccmC) and the derived IEA "cellular oxidant detoxification" are unsupported and should be withdrawn. |

The same node correctly carries plasma membrane and cytochrome c
biosynthetic process (seeded by E. coli CcmC P0ABM1 and P35162), which are
retained.

## Decisions summary

- REMOVE: catalase activity (IMP and IBA), cellular oxidant detoxification
  (IEA from catalase), glycolipid biosynthesis (IMP), type IV pilus motility
  (IMP), swarming motility (IMP).
- MARK_AS_OVER_ANNOTATED: pyoverdine biosynthesis (IMP; necessity is real,
  mechanism unknown and possibly partly separable from cytochrome c), swimming
  motility (IMP; not in the abstract, at most an indirect phenotype).
- ACCEPT: plasma membrane (IBA, IEA), heme binding, heme transmembrane
  transporter activity, heme transport, cytochrome c biosynthetic process.
- MODIFY: membrane -> plasma membrane; cytochrome complex assembly ->
  cytochrome c biosynthetic process.
