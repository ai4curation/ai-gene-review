# miaB (P0AEI1) notes

Deep research was unavailable for this gene (falcon returned 403; asta returned nothing useful in
Phase 1 of the RADICAL_SAM project). The review was built from cached primary papers, the UniProt
record and QuickGO term lookups.

## Function

- MiaB converts i6A37 to ms2i6A37 in tRNAs reading UNN codons. Genetic identification in
  S. typhimurium and E. coli: [PMID:10572129 "The tRNA from the E. coli miaB strains showed an
  accumulation of i 6 A, whereas ms 2 i 6 A was absent (data not shown)."]
- The same paper argued MiaB did only thiolation: [PMID:10572129 "Only a weak similarity to an
  AdoMet-binding site was found, favoring the idea that the MiaB protein is involved in the
  thiolation step and not in the methylating reaction"]. Overturned by in vitro reconstitution:
  [PMID:15339930 "This study demonstrates that MiaB protein is a bifunctional system, involved in
  both thiolation and methylation of i(6)A."]
- Two SAM per turnover: [PMID:15339930 "one molecule of AdoMet is converted to 5'-deoxyadenosine
  ... and a second molecule of AdoMet is used as a methyl donor as shown by labeling experiments."]
  Abstract does not name the organism; PubMed MeSH lists Escherichia coli Proteins (and
  Thermotoga maritima). Evidence code for the NEW SAM-binding row set to IDA on that basis.
- Fe-S: [PMID:11882645 "UV-visible and EPR spectroscopy of MiaB indicate the presence of a [4Fe-4S]
  cluster under reducing and anaerobic conditions"]; Cys157/161/164 required.
- Both clusters retained; exogenous sulfur: [PMID:23542644 "the MTTases MiaB and RimO are true
  enzymes whose [4Fe-4S] clusters are not sacrificed as sulfur donors."] (T. maritima enzymes).
- Fe-S delivery: GrxD and NfuA bind MiaB; NfuA transfers its cluster [PMID:23543739 "We furthermore
  demonstrate that NfuA is able to transfer its cluster in vitro to MiaB, whereas GrxD is unable to
  do so."]. The IPI protein binding row was removed as uninformative (MiaB is the cluster acceptor).
- Cytosol: [PMID:18304323 "we identified 1103 proteins from the cytosolic fraction of the
  Escherichia coli strain MC4100"].

## Term decisions

- Core MF GO:0035597; BP GO:0035600; CC GO:0005829; GO:0051539; NEW GO:1904047 (IDA PMID:15339930).
  Same terms as genes/human/CDK5RAP1 (MiaB-subfamily ortholog).
- GO:0030488 tRNA methylation (IMP) -> MODIFY GO:0035600 (lateral; GO:0035600 is not under GO:0030488
  in QuickGO). GO:0006400 -> GO:0035600. GO:0016740, GO:0035596, GO:0003824 -> GO:0035597.
  GO:0051536 -> GO:0051539. GO:0005737 -> GO:0005829.
- No translational-fidelity BP added: requirement, not participation; not in E. coli GOA.

## Context

- Module modules/trna_ms2io6a37_hydroxylation (MiaE step, P. putida) treats MiaA/MiaB as upstream
  context; E. coli stops at ms2i6A (no MiaE).
