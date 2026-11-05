# Mlnr (rat) review notes

## Session 1

- `just fetch-gene rat Mlnr` resolved UniProt A0ACM8Q218 (TrEMBL, unreviewed), GeneID
  252859, RGD:621262, as requested. GOA has 8 rows keyed to A0ACM8Q218.
- Despite the symbol `Mlnr` (motilin receptor), the sequence and all literature are the
  rodent TRH receptor type 2 (TRH-R2, former symbol Trhr2). NCBI lists alias `Trhr2`.
  The genuine MLNR was pseudogenized in rodents ["We speculate that the MLNR gene became
  a pseudogene before the divergence of the squirrel and other rodents about 75 mya"
  PMID:19696113]. The review is therefore of TRH-R2 function; flagged as a question.
- Core function: Gq/PLC-coupled TRH receptor [PMID:9735333 "specific binding of TRH to
  TRHR2 was observed with Kd value of 9 nM"; PMID:10499553 "similar binding and
  stimulated signaling activity via the phosphoinositide-calcium transduction pathway"].
  Notable high constitutive activity [PMID:10499553].
- Location: plasma membrane (GPCR, internalizes after agonist [PMID:12683933]); neuronal
  cell bodies of TMN histaminergic neurons [PMID:17760865 "Specific antibodies revealed
  that TRH-R2 (green) was expressed within histaminergic cell bodies in the TMN of rats"].
- Decisions: general GPCR/membrane/signal transduction IEA rows MODIFY to TRH receptor
  activity, plasma membrane, PLC-activating GPCR signaling pathway (GO:0007200).
  No NEW process terms: feeding/arousal roles in PMID:17760865 rest on co-localization
  plus TRH (ligand) injection, not receptor-specific perturbation.
- PMID:9735333 is abstract-only; binding data in abstract supports the IDA.
