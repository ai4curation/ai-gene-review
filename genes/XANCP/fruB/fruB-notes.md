# fruB (Xanthomonas campestris pv. campestris, P45597) curation notes

## 2026-11-05 — initial review (Claude, AI-assisted)

Deep research: `just deep-research XANCP fruB --provider perplexity` was tried
once and failed ("Provider 'perplexity' not available. Available: falcon,
openscientist, claude_code"). No deep-research file was generated; the review
rests on the UniProt record and the two cached primary papers (both
abstract-only in the cache).

Literature (from the UniProt RN/RX lines):

- PMID:7496537 (de Crécy-Lagard, Binet & Danchin 1995, Microbiology) cloned
  fruB and constructed the mutant [PMID:7496537 "This PTS involves a
  multiphosphoryl transfer protein (MTP) encoded by the fruB gene, which was
  cloned and sequenced."; "The construction of a fruB mutant confirmed the
  role of the MTP in fructose transport and phosphorylation in X.
  campestris."]. Domain boundaries: EIIA-like 1-148, HPr-like 161-251,
  enzyme-I-like 274-837.
- PMID:1655739 (1991, J Biol Chem) characterised the fructose PTS, FruA and
  FruK [PMID:1655739 "In Xanthomonas campestris pv. campestris, fructose is
  transported and phosphorylated into fructose 1-phosphate through a
  phosphoenolpyruvate-dependent phosphotransferase system."].

UniProt (Swiss-Prot, PE 3): FUNCTION and DISRUPTION PHENOTYPE carry
ECO:0000269|PubMed:7496537; the catalytic activity and active sites are by
similarity to E. coli enzyme I (P08839). PANTHER PTHR46244:SF6.

Experimental evidence on P45597 is genetic (mutant phenotype) plus sequence;
no purified-protein phosphotransfer assay is reported in the abstract.

Decisions:

- GO:0008965 (IBA, IEA, ISS): ACCEPT; core function.
- GO:0009401 (IEA): ACCEPT.
- GO:0005737 (IEA, SubCell): ACCEPT.
- GO:0015764 N-acetylglucosamine transport (IBA from PTN000532509, seed
  Q9HXN5 only): REMOVE as over-propagation from the root node; consistent with
  the TOO_DEEP assessment of this node in the PTHR46244 family review.
- GO:0016772 (IEA InterPro2GO): TOO_GENERAL, entailed by GO:0008965.
- Proposed term "PTS EIIA-to-EIIB phosphotransferase activity" kept identical
  to the P. putida FruB (Q88PQ5) proposal.

Open point: the mutant also fails on mannose, mannitol and sucrose (UniProt
disruption phenotype); whether these sugars are routed through fructose or
whether FruB serves other EII permeases is unknown (suggested question).
