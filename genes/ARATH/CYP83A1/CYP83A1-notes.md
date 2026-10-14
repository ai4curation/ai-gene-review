# CYP83A1 (REF2) - Arabidopsis thaliana - review notes

UniProt: P48421 · At4g13770 · EC 1.14.14.43 · Taxon 3702
Context: second step of aliphatic GSL core structure (module annoton cyp83a1_activity).
No falcon deep-research file was present at review time.

## Core function
- Oxidizes aliphatic methylthioalkanaldoximes; product conjugated to glutathione
  (S-alkylthiohydroximate-GSH), EC 1.14.14.43 / RHEA:51992.
  [PMID:12970475 "we show that aliphatic oximes derived from chain-elongated homologs of methionine are efficiently metabolized by CYP83A1, whereas CYP83B1 metabolizes these substrates with very low efficiency."]
  [PMID:12970475 "The product is most likely the S -alkylthiohydroximate designated S -(4-methylthiobutylhydroximoyl)-glutathione"]
  Km for aliphatic oximes 20-150 uM [PMID:12970475].
- Also metabolizes aromatic oximes with lower affinity; indole-3-acetaldoxime is the
  physiological substrate of CYP83B1, not CYP83A1.
  [PMID:11553739 "Instead, CYP83A1 catalyzes the initial conversion of aldoximes to thiohydroximates in the synthesis of glucosinolates not derived from tryptophan."]
- Genetics: ref2 reduces all aliphatic GSLs, increases indole GSLs.
  [PMID:12509530 "These results show that CYP83A1 is involved in the biosynthesis of both short-chain and long-chain aliphatic glucosinolates"]

## Pleiotropic phenotype (not core)
- ref2 phenylpropanoid defects (sinapoylmalate, sinapoylcholine, syringyl lignin) are
  attributed to aldoxime inhibition of O-methyltransferases (COMT).
  [PMID:12509530 "the phenylpropanoid phenotypes of the mutant may be attributable to the inhibition of O -methyltransferase activities by one or more aldoximes accumulated in the mutant"]
  No phenylpropanoid GO terms proposed.

## GO term gap
- No GO MF for EC 1.14.14.43 (checked go.db: only obsolete aldoxime process terms). Proposed NTR
  "(methylsulfanyl)alkanaldoxime N-monooxygenase activity" under GO:0016712 (same branch as the
  CYP79F term GO:0120526). core_functions uses proposed_molecular_function.

## Decisions
- GO:0016709 IDA (PMID:12970475) -> MODIFY to NTR + GO:0016712
- GO:0019761 IDA (PMID:11553739) -> ACCEPT (core BP)
- GO:0005789 ER membrane IEA -> ACCEPT (activity assayed in microsomes with ATR1)
- GO:0016491 IBA, monooxygenase, 0016705, heme, iron IEA -> KEEP_AS_NON_CORE
- cytosol HDA (PMID:28887381) -> MARK_AS_OVER_ANNOTATED; response to insect IEP -> KEEP_AS_NON_CORE
