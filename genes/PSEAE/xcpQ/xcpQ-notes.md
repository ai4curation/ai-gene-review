# xcpQ (PA3105, P35818) review notes

## Review session 2026-10-28 (PseudoCAP IBA-seed protocol)

Fetched with `just fetch-gene PSEAE xcpQ`; accession P35818 matches the worklist entry
(rank 52, PA3105, reviewed Swiss-Prot entry GSPD_PSEAE). No deep-research provider key was
available, so these notes are manual, from the cached publications, the UniProt record and
the cached PAINT table `interpro/panther/PTHR30332/PTHR30332-paint.tsv`.

### What XcpQ is

- XcpQ is the GspD-family secretin, the outer-membrane channel of the Xcp type II secretion
  system (T2SS) of *P. aeruginosa*. UniProt: "Belongs to the bacterial secretin family. GSP D
  subfamily"; NCBIfam TIGR02517 (type_II_gspD), Pfam PF00263 Secretin + PF03958 Secretin_N,
  PANTHER PTHR30332.
- It is an outer-membrane protein that oligomerises into a ring-shaped channel large enough to
  pass folded exoproteins [PMID:9466268 "C-terminal part of XcpQ is sufficient for the formation
  of the multimer."; "the XcpQ multimers revealed large, ring-shaped structures with an apparent"
  central cavity of 95 Å]. Cryo-EM of the purified ~1-MDa complex shows a pentadecamer
  [PMID:29042496 "class averages revealed that XcpQ is a pentadecameric secretin complex"].
- UniProt places it in the cell outer membrane with most of the mass in the periplasm, and
  divides it into periplasmic N0-N3 domains plus the membrane-embedded secretin and S domains
  (`CC:SUBCELLULAR LOCATION`, `CC:DOMAIN`, both ECO:0000305 from PubMed:29042493/29042496).
- Loss of XcpQ abolishes Xcp-dependent export: UniProt `CC:DISRUPTION PHENOTYPE` (from
  PubMed:29042493) records "Loss of export of PrpL, elastase LasB, chitin binding protein D",
  and the nanobody-interference work compares its secretome to "an xcpQ deletion mutant"
  [PMID:29042493]. The Xcp machine with XcpQ exports many hydrolases [PMID:29042496 "The T2SS
  containing XcpQ is responsible for the secretion of at least 19 substrates"].
- XcpQ is unusual among *P. aeruginosa* secretins in inserting into the outer membrane without
  the Bam/Lol machineries and in assembling spontaneously into liposomes [PMID:22147293 "XcpQ,
  but not PilQ or PscC, was shown to assemble spontaneously into liposomes as multimers."].
- The homo-oligomer is the functional unit, and a point substitution traps an assembly
  intermediate in both PulD and XcpQ [PMID:24657091 "in the Pseudomonas aeruginosa secretin
  XcpQ"].

### PseudoCAP row details

- `GO:0015627` IDA PMID:9466268 (Bitter et al. 1998): primary paper, abstract-only in the cache.
  It purifies XcpQ as a stable homomultimer and images ring structures; this is direct evidence
  for the secretin channel, and later cryo-EM (PMID:29042496) confirms the pentadecameric T2SS
  secretin complex. Term correct, evidence code appropriate.
- `GO:0015628` IDA PMID:9818381: Filloux, Michel & Bally 1998 is a **review** (PubMed
  publication type Review; `publication_type: REVIEW` in the cached file). The same row and the
  same mis-coding was found in the xcpX review (`genes/PSEAE/xcpX`), so this is a systematic
  PseudoCAP pattern across the xcp cluster, not a one-off. The term itself is correct for XcpQ —
  it is the outer-membrane channel of the machine, and deletion abolishes export of the Xcp
  substrates. Recorded as a `WRONG_EVIDENCE_CODE` source defect (re-key to a primary paper, e.g.
  PMID:29042493 for the deletion phenotype, or downgrade to TAS for the review).

### PAINT node context

`interpro/panther/PTHR30332/PTHR30332-paint.tsv` shows the family carries two IBD-bearing nodes:
PTN000768388 (T2SS: GO:0015627 seeded by P35818/Q9I2M7/Q9I5P0, GO:0015628 sole-seeded by
P35818) and PTN009110345 (T3SS: GO:0030257 seeded by P35672, GO:0030254 sole-seeded by pscC
Q9I319), with an IRD at PTN009110348 removing the T3SS terms in a plant-associated subclade.
The family therefore keeps the T2SS and T3SS secretin assertions on separate nodes, which is the
right shape: a shared "bacterial secretin" node would propagate T2SS terms onto T3SS members.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN000768388 | GO:0015627 type II protein secretion system complex | 3 (not sole) | 23 (13 taxa) | GO:0015627, IDA, PMID:9466268 | SOUND | XcpQ is the GspD secretin of the Xcp T2SS, purified as a ring-forming homomultimer (PMID:9466268) and resolved as a pentadecameric secretin complex by cryo-EM (PMID:29042496). The node is the GspD-specific subnode of PTHR30332 (the T3SS secretins sit on PTN009110345), so a T2SS-complex term fits the clade. |
| PTN000768388 | GO:0015628 protein secretion by the type II secretion system | 1 (sole seed) | 23 (13 taxa) | GO:0015628, IDA, PMID:9818381 | SOUND (term); evidence code WRONG (cited paper is a review with no original secretion data; full text checked) | The claim is correct — XcpQ is the outer-membrane conduit of the Xcp T2SS and its deletion abolishes export of the Xcp substrates (UniProt disruption phenotype from PMID:29042493). But PMID:9818381 is a review, so IDA cannot stand; the IBD conclusion is unaffected and the seed should be re-keyed rather than the node dropped. Same defect as the xcpX seed on the identical reference. |
| PTN001251149 | GO:0009306 protein secretion | 2 (not sole) | 0 | GO:0015628, IDA, PMID:9818381 | SOUND (term) | The general node carries no leaf IBAs, so nothing propagates; the parent term is true of XcpQ. The same wrong evidence code applies to the underlying row. |

## Open questions

- Whether the `GO:0042802` identical protein binding row (IPI PMID:24657091, WITH P35818) is
  worth keeping now that the homo-oligomer stoichiometry is known (15-mer, PMID:29042496): the
  self-association is the channel, so a complex-membership statement arguably says more.
