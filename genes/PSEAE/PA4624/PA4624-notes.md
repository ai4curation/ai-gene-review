# PA4624 (Q9HVG7, CdrB) notes

## Review session 2026-10-28 (PseudoCAP IBA-seed protocol)

Fetched with `just fetch-gene PSEAE PA4624` (first run completed). Accession
Q9HVG7 matches the worklist (rank 45). Unreviewed entry (PE 3), named "POTRA
domain-containing protein"; UniProt has no gene symbol, so the folder uses the
locus tag (the literature name is CdrB). No deep-research provider was used.
PubMed searches for CdrB found only the founding paper, PMID:20088866.

### Identity

- CdrB is the TpsB partner of the CdrA adhesin (PA4625) [PMID:20088866 "We have
  designated PA4625 and PA4624 as cdrA (cyclic diguanylate-regulated TPS partner
  A) and cdrB"]; cdrAB is a dicistronic, c-di-GMP-induced operon.
- Domains: SignalP 1..23; POTRA (PS51779, 71..146); Pfam PF08479 POTRA_2 and
  PF03865 ShlB; InterPro IPR051544 TPS_OM_transporter; PANTHER PTHR34597:SF6.
  Structure prediction placed it with FhaC [PMID:20088866 "The secondary
  structure and function of CdrB was predicted by I-TASSER (Zhang, 2008) to be
  most similar to FhaC which forms a β-barrel channel in the outer membrane for
  the outward translocation of FHA."]
- The paralog PA0692 (PdtB) sits in the same PAINT node PTN002160772 and was
  reviewed in `genes/PSEAE/PA0692/`; that review accepted the GO:0008320 IBA
  seeded by CdrB.

### Evidence for the PseudoCAP rows (PMID:20088866, full text read)

- Transport: CdrA was found in supernatants only when cdrB was co-expressed
  [PMID:20088866 "No CdrA was seen in the supernatant of the strain
  overexpressing only cdrA, presumably because of the absence of CdrB to
  transport CdrA across the outer membrane."]; [PMID:20088866 "The detection of
  CdrA in supernatants was dependent upon CdrB."] These are arabinose-inducible
  pBADcdrA versus pBADcdrAB constructs in PAO1, not a cdrB deletion.
- Biofilm: mutants made were cdrA deletions; cdrAB overexpression increased
  biofilm [PMID:20088866 "Biofilm formation was increased 6.4-fold when cdrAB was
  overexpressed as compared with the vector control (pMJT-1) (Fig. 4A)."], and
  [PMID:20088866 "Overexpression of cdrA or cdrB independently does not result in
  auto-aggregation."] So CdrB's role in biofilm is via secretion of CdrA.

### Can IMP support an MF?

Yes, when the perturbation removes the activity and the readout is the activity
itself rather than a downstream phenotype (EcoCyc, for instance, uses IMP for
nickel transporter activity of NikB/NikC on uptake assays of mutants). Here the
readout is CdrA crossing the outer membrane into the supernatant, which is the
transport step, and the perturbation is the absence of cdrB from the expression
construct. That is a direct in vivo readout of the TpsB activity, though
weakened by being an overexpression comparison with chromosomal cdrB still
present. Together with the TpsB architecture (the protein is the channel), it is
adequate. By contrast, the biofilm IMP is a downstream phenotype of the partner
and does not show CdrB participates in matrix formation.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002160772 | GO:0008320 transmembrane protein transporter activity | 1 (sole) | 25 (10 taxa) | GO:0008320, IMP, PMID:20088866 (PseudoCAP) | SOUND | CdrA reaches the supernatant only with CdrB (in vivo readout of the transport step), and CdrB is an FhaC-like POTRA/ShlB beta-barrel. The node is a TpsB subfamily (FhaC, HxuB, HpmB, CdiB, PdtB, B. japonicum and Leptospira members), whose shared activity is translocating a partner protein across the outer membrane, so the term suits the clade. Caveat: the CdrB experiment is an overexpression comparison, not a deletion. |

Not seeding but reviewed: the biofilm IMP row is an indirect phenotype of the
partner (MARK_AS_OVER_ANNOTATED, with a SUSPECTED WRONG_QUALIFIER defect to
PSEUDOCAP suggesting acts_upstream_of_or_within).

## Decisions summary

- ACCEPT: transmembrane protein transporter activity (IBA, IMP), cell outer
  membrane (IEA), protein secretion by the type V secretion system (IBA), type V
  protein secretion system complex (IBA, ISS).
- MARK_AS_OVER_ANNOTATED: single-species biofilm formation (IMP).
