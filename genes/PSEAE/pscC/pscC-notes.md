# pscC (PA1716, Q9I319) review notes

## Review session 2026-10-28 (PseudoCAP IBA-seed protocol)

Fetched with `just fetch-gene PSEAE pscC`; accession Q9I319 matches the worklist entry (rank 43,
PA1716). The entry is UniProtKB/TrEMBL (unreviewed), annotated by HAMAP-Rule MF_02219, with
protein existence "Inferred from homology". No deep-research provider key was available, so these
notes are manual, from the cached publications, the UniProt record and the cached PAINT table
`interpro/panther/PTHR30332/PTHR30332-paint.tsv`.

### What PscC is

- PscC (SctC) is the outer-membrane secretin of the *P. aeruginosa* type III secretion system
  (T3SS, injectisome): the ring-forming channel of the base through which effectors leave the
  bacterium. UniProt (HAMAP-Rule MF_02219): "Forms a ring-shaped multimeric structure with an
  apparent central pore in the outer membrane"; "Belongs to the bacterial secretin family. T3SS
  SctC subfamily"; NCBIfam TIGR02516 (type_III_yscC), PANTHER PTHR30332:SF5.
- The membrane-inserted multimer has been purified and imaged: cryo-EM of cell-free-synthesised
  PscC gives a barrel with a "cup and saucer" architecture and a plugged central chamber, closely
  similar to the T2SS secretin PulD [PMID:25156426 "The membrane-inserted, multimeric regions of
  PscC, the" Pseudomonas aeruginosa type III secretion system secretin ... "of two distinct rings,
  with that of PulD being less segmented than that of PscC."].
- Its outer-membrane localisation has been examined directly in PAO1 depletion strains
  [PMID:22147293 "PilQ, XcpQ, and PscC form multimeric ring-like structures in the OM"], where
  PscC levels fall on LolB depletion but are little affected by BamA depletion.
- The gene was identified in the *exsD-pscB-L* operon of the T3SS locus, whose members are
  homologues of the Yersinia Ysc export apparatus, and transposon insertions in that region
  abolish exoenzyme S production [PMID:8971719 "isolated which exhibited an exoenzyme S-deficient
  phenotype (388::Tn5Tc 469," "unique. The other 11 ORFs demonstrated high homology to the YscB-L
  proteins of" the yersiniae].
- Later work used *pscC* mutants as the standard secretion-apparatus-defective control and
  described the gene accordingly: "mutant in pscC, encoding a structural component of the type III
  translocase" [PMID:12421316]; "or pscC, which encodes" an essential component of the secretion
  apparatus, significantly attenuated in a mouse pneumonia model [PMID:14977975]; plasmid
  insertion in *pscC* reduces T3SS-mediated killing of endothelial cells [PMID:12385743].

### PseudoCAP row details

- `GO:0030254` IMP PMID:8971719 (Yahr, Goranson & Frank 1996) is the sole seed of the
  PTN009110345 IBD for this term (25 leaf IBAs over 15 taxa). The cached record is abstract-only
  and does not say which of the twelve ORFs the mapped Tn5Tc insertions (469, 550) lie in, so the
  gene-level attribution cannot be confirmed from what is available here; the curator read the
  full text. The claim itself is not in doubt: the operon is the T3SS export apparatus, and three
  independent later studies treat *pscC* mutants as secretion-apparatus-null (PMID:12421316,
  PMID:14977975, PMID:12385743). No source defect is recorded - this is exactly the case where the
  repository guidance says not to second-guess an experimental annotation whose full text we have
  not read.
- Note the contrast with the xcp cluster: the xcpQ/xcpR/xcpX `GO:0015628` rows are keyed to a
  review article (PMID:9818381) and so carry a wrong evidence code, whereas this row is keyed to a
  primary transposon-mutagenesis paper and the evidence code is appropriate.

### PAINT node context

`interpro/panther/PTHR30332/PTHR30332-paint.tsv` shows PTN009110345 carrying both T3SS terms -
`GO:0030254` sole-seeded by this gene (Q9I319) and `GO:0030257` seeded by another T3SS secretin
(P35672) - while the T2SS terms sit on a separate node, PTN000768388 (seeded by XcpQ and two other
*P. aeruginosa* secretins). An IRD at the child node PTN009110348 withdraws both T3SS terms in a
subclade (taxon:3880), so the curators have actively pruned the propagation rather than letting
the family root carry secretion-system-specific terms. That is the right shape for a family that
mixes T2SS secretins, T3SS secretins and other NolW-like channels.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN009110345 | GO:0030254 protein secretion by the type III secretion system | 1 (sole seed) | 25 (15 taxa) | GO:0030254, IMP, PMID:8971719 | SOUND | The term is right for an SctC secretin, and PscC specifically is treated as the T3SS secretion-apparatus component whose loss abolishes effector secretion and attenuates virulence (PMID:12421316, PMID:14977975, PMID:12385743); the purified multimer is the T3SS outer-membrane channel (PMID:25156426). The node is the T3SS-specific subnode of PTHR30332, with an IRD pruning a divergent subclade, so the term suits the clade that inherits it. Caveat, not a defect: the cached abstract of the seed paper does not pin the transposon insertions to pscC, so the gene-level attribution rests on the curator's reading of the full text. |
| PTN001251149 | GO:0009306 protein secretion | 2 (not sole) | 0 | GO:0030254, IMP, PMID:8971719 | SOUND (term) | The generic parent term is true of PscC, and the node carries no leaf IBAs, so nothing propagates from it. |

## Open questions

- No experimental annotation exists for the outer-membrane location of PscC in PAO1 even though
  PMID:22147293 assays it directly in depletion strains; the location rows are all HAMAP/UniRule
  or InterPro mappings. A curation-level gap rather than a knowledge gap.
- Whether the plug and hairpin seen in the cell-free-synthesised PscC multimer (PMID:25156426)
  reflect the gated state of the assembled injectisome base is unresolved.
