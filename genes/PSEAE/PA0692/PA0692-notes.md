# PA0692 (PdtB, Q9I5N4) review notes

## Review session 2026-10-28 (PseudoCAP IBA-seed protocol)

Fetched with `just fetch-gene PSEAE PA0692` (first attempt hit an EBI timeout; re-run succeeded).
Accession Q9I5N4 matches the worklist (rank 19). The entry is unreviewed (PE 4, predicted) with a
ProtNLM name; there is no gene symbol in UniProt, so the folder uses the locus tag. No
deep-research provider was used.

### Identity

- PA0692 is PdtB, the TpsB partner of the PA0690 PdtA exoprotein ("phosphate depletion regulated
  TPS partners"). The cached abstract does not give locus tags; the PA0690/PA0692 assignment comes
  from secondary sources found by web search (database summaries of Faure et al. 2014) and agrees
  with the PseudoCAP curator's choice of PA0692 for PMID:25009238. Not independently checked in
  the full text (not in PMC).
- Domains: Pfam PF08479 POTRA_2 (residues 48..121) and PF03865 ShlB (184..459); InterPro
  IPR051544 TPS_OM_transporter; PANTHER PTHR34597 (official name "SLR1661 PROTEIN"),
  subfamily SF6. This is the Omp85-superfamily TpsB architecture (POTRA domains plus a C-terminal
  16-strand beta-barrel) of FhaC, ShlB and HMW1B.
- SignalP signal peptide 1..31. UniProt also shows a lipobox-based lipidation at Cys27 from
  PROSITE-ProRule PRU00303; this conflicts with the SignalP cleavage site and is an automatic
  prediction only; TpsB transporters are not generally lipoproteins.
- The MF IBA (GO:0008320) has WITH/FROM UniProtKB:Q9HVG7, which is PA4624 (CdrB, the TpsB
  partner of CdrA), so PA0692 is not the seed of that annotation.

### Literature

[PMID:25009238 "we identified a functional two-partner secretion (TPS) system, composed of the
PdtA exoprotein and its cognate pore-forming β-barrel PdtB transporter, which is implicated in the
virulence of P. aeruginosa"]; [PMID:25009238 "We also obtained evidence that the transport of PdtA
is strictly dependent on the production of PdtB, a result confirming that these proteins
constitute a functional TPS system"]. PdtA is produced under phosphate limitation and processed
during outer-membrane translocation [PMID:25009238 "We show that PdtA is processed during its
outer-membrane translocation"]. Abstract only; whether PdtB itself was localized (e.g. outer
membrane fractionation) is not stated in the abstract.

### Can an IMP support a complex CC term?

The IMP is a mutant phenotype: no PdtA export without PdtB. That directly supports the process
term (PdtB is the translocation pore, so it performs the step, not just a requirement). It does
not show where PdtB is or what it associates with. GO evidence guidance reserves IMP for CC
mainly to cases where a mutation changes a location; membership of a complex needs IDA (e.g.
fractionation, co-purification) or IPI, or a reasoned IC/ISS. The term itself is right: TpsB is the
beta-barrel of the type Vb (two-partner) system that GO:0098046 explicitly includes, so the
claim is true. The defect is the evidence code, not the term. Recorded as WRONG_EVIDENCE_CODE /
CHECK, confidence SUSPECTED because the full text may contain a localization experiment.

Ontology note: GO:0046819 is defined in autotransporter terms ("proteins mediate their own
secretion ... beta-barrel pore structure formed by the C-terminal domain of the protein
precursor"). Two-partner (type Vb) secretion uses a separate TpsB pore, so the definition does
not fit TPS systems even though GO:0098046 includes them. Raised as a suggested question.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002160772 | GO:0046819 protein secretion by the type V secretion system | 1 (sole seed) | 25 (10 taxa) | GO:0046819, IMP, PMID:25009238 | SOUND | PdtA export strictly depends on PdtB, the cognate beta-barrel transporter; the transporter performs the translocation, so this is participation, not mere necessity. The node is a TpsB subfamily, so the term suits the clade (with the caveat that the GO definition is written for autotransporters). |
| PTN002160772 | GO:0098046 type V protein secretion system complex | 1 (sole seed) | 25 (10 taxa) | GO:0098046, IMP, PMID:25009238 | SOUND (term); evidence code WRONG | A mutant export defect does not show complex membership or location, so IMP is not appropriate for this CC row. The claim is true by family (TpsB is the pore of the type Vb system, which the term includes), so the IBD conclusion is sound, but the seed rests on the wrong kind of evidence and should be IDA (if the full text localizes PdtB) or IC/ISS. |
