# Npc1 (mouse) curation notes

Session: 2026-10-28. Literature synthesis is in `Npc1-deep-research-manual.md`
(hand-written; no deep-research provider was available in this environment).

## Review strategy

GOA ships 107 rows for O35604. They fall into a small number of groups:

1. **The core mechanism** — cholesterol binding (GO:0015485), cholesterol transfer
   activity (GO:0120020), intracellular cholesterol transport (GO:0032367),
   lysosome to ER cholesterol transport (GO:0090120), cholesterol homeostasis
   (GO:0042632), lysosomal membrane (GO:0005765) / late endosome membrane
   (GO:0031902) / lysosome (GO:0005764). These are ACCEPTed.
2. **Correct-but-general terms** that the ontology refines — lipid carrier activity,
   sterol transport, cholesterol transport, intracellular lipid transport, membrane,
   endosome, lysosomal transport. MODIFY to the specific terms the gene already
   carries (GO:0120020, GO:0032367, GO:0005765, GO:0031902, GO:0090120). The five
   root-organelle terms of `projects/ORGANELLES.md` are exempt: `lysosome`,
   `endoplasmic reticulum` and `Golgi apparatus` rows are kept, not refined.
3. **Phenotype-derived process terms** from the *Npc1*-null mouse — gene expression,
   programmed cell death, neurogenesis, sterol metabolic process, endocytosis,
   adult walking behavior, cyclodextrin metabolic process, liver development.
   NPC1 does not do the work of any of these; they record downstream consequences
   of lysosomal cholesterol storage. MARK_AS_OVER_ANNOTATED, with
   `review.source_defects` (WRONG_TERM / CHECK) where the term itself looks like an
   upstream error (neurogenesis for neurodegeneration; cyclodextrin metabolic
   process for a drug-rescue experiment; gene expression for transcript changes).
4. **Substrate-not-participant** — glycoprotein biosynthetic process. NPC1 *is* an
   N-glycoprotein; it does not catalyse or scaffold glycoprotein biosynthesis.
   Both mouse rows are electronic propagations of the human IDA from the topology
   paper (PMID:10821832), so they are REMOVEd with a source defect on the donor.
5. **Paralog-scoped IBA** — plasma membrane `is_active_in` and intestinal
   cholesterol absorption come from a PANTHER node that includes NPC1L1
   (UniProtKB:Q9UHC9), the apical enterocyte sterol permease and ezetimibe target.
   Over-annotation for NPC1 proper; `propagation_review` records the node and the
   failure mode.
6. **Unresolvable rat-sourced rows** — response to cadmium ion and negative
   regulation of epithelial cell apoptotic process, both propagated from RGD:628693
   with no reachable reference. UNDECIDED per the standing rule, with
   `propagation_review.source_entities[].source_status: UNRESOLVED`.

## Specific judgements worth recording

- **GO:0005576 extracellular region (IDA, PMID:22065762)** is an artefact of the
  experimental construct: the authors built a *soluble* NPC1 lumenal domain 2 by
  replacing TM2/TM3 with an antiparallel coiled coil and adding a preprotrypsin
  signal peptide, then purified it from conditioned medium. Native NPC1 is a
  multi-pass lysosomal membrane protein. Full text was read, so this is REMOVE with
  a WRONG_TERM source defect against UniProt (requested_change DELETE_ROW).
- **GO:0005635 nuclear envelope (IDA, PMID:20457914)** cites the torsinA mutant
  mouse paper, in which NPC1 is not mentioned anywhere in the cached full text. The
  NE claim itself is plausible only as an over-reading of ER/perinuclear signal
  (human IDA PMID:12554680), so all four NE rows get MARK_AS_OVER_ANNOTATED and the
  IDA row carries a WRONG_REFERENCE source defect (CHECK) against MGI.
- **GO:0098574 cytoplasmic side of lysosomal membrane (is_active_in)** is too
  specific and on the wrong face: NPC1's cholesterol-receiving NTD and MLD are
  lumenal. MODIFY to GO:0005765 lysosomal membrane.
- **GO:0007041 / GO:0008206 ISS rows** are propagated from UniProtKB:Q7TMD4, which
  is a second (unreviewed) *mouse* Npc1 entry — i.e. an ISS from the same gene in
  the same species. GO:0008206 bile acid metabolic process traces to PMID:16374838,
  a paper about NPC2 in bile; recorded as a source defect against UniProt.
- **GO:1904262 negative regulation of TORC1 signaling** is a genuine second activity
  (SLC38A9 complex, PMID:28336668) and is kept, feeding the single core function's
  `directly_involved_in`.
- **GO:0046718 symbiont entry into host cell** is real and well documented (NPC1 is
  the intracellular filovirus receptor; PMID:21866101, PMID:21866103) but is a
  host-factor role rather than the gene's core function: KEEP_AS_NON_CORE.
- **No NEW rows were added.** Candidates considered and rejected under the
  participation/comparator bar in CLAUDE.md: autophagy regulation beyond the
  existing GO:0016242 rows (phenotype only), neurodegeneration/Purkinje-cell terms
  (consequence of storage, NPC1 performs no step), and sphingolipid metabolism
  (secondary storage, no activity shown). PMID:22147702 (NPC1 knockdown raises
  cellular chloroquine) supports the existing response-to-xenobiotic row rather
  than a new term.
