# Gsk3b (rat) review notes

## Session 2026-10-28

- `just fetch-gene rat Gsk3b` resolved P18266 (GSK3B_RAT, RGD:70982, GeneID 84027);
  GOA file keyed to P18266, 280 rows. `just fetch-gene-pmids` cached all 52 PMIDs;
  PMID:20042609 cached (full text) and read.
- No deep-research provider was available; literature synthesis is in
  `Gsk3b-deep-research-manual.md`.
- Most cited rat papers are abstract-only in the cache; experimental rows from those
  papers were not removed.

## Decisions worth flagging

- GO:0005874 microtubule IDA PMID:8576078: the paper (title and abstract) is about
  localisation of TPKI/GSK-3beta in cerebellar mitochondria [PMID:8576078 "was present
  in mitochondria, but GSK-3 alpha was not"]. Row set to UNDECIDED with a
  WRONG_TERM source defect (CHECK); a NEW mitochondrion IDA row was added.
- GO:0045886/GO:0045887 (regulation of synaptic assembly at neuromuscular junction)
  IMP PMID:25764078: the rat experiments were in cultured hippocampal neurons; the NMJ
  data are Drosophila only (full text read) [PMID:25764078 "a comparative study
  between the neuromuscular junction of Drosophila larvae and cultured hippocampal rat
  neurons"]. MODIFY to GO:0051963 regulation of synapse assembly, plus a source defect.
- GO:2000463 positive regulation of EPSP IMP PMID:20007479: the abstract describes
  GSK-3beta activation as mediating suppression of NMDA receptor currents, which reads
  as negative regulation. UNDECIDED with a WRONG_TERM (sign) CHECK defect.
- GO:0019901 protein kinase binding IPI PMID:16478782 with RGD:620632 (Dvl1, not a
  kinase): UNDECIDED with a WRONG_WITH_FROM/term CHECK defect.
- GO:0005515 IPI PMID:9482734 lists UniProtKB:P49841 (human GSK3B) as the partner,
  whereas the paper's interactor is rat Axin; suspected With/From error.
- Location rows with IMP evidence (glutamatergic synapse, Schaffer collateral-CA1
  synapse; PMID:23864697) kept like the term's other rows, with WRONG_EVIDENCE_CODE
  CHECK defects.

## Core functions chosen

1. Protein Ser/Thr kinase activity (priming-dependent; Ser-9 inhibition by
   Akt/PKA/CaMKII).
2. Beta-catenin destruction complex kinase; negative regulation of canonical Wnt.
3. Insulin-regulated inhibition of glycogen synthesis.
4. Tau-protein kinase; regulation of microtubule cytoskeleton organisation.
5. Postsynaptic PSD-95 Thr-19 kinase in LTD / AMPA receptor mobilisation.
