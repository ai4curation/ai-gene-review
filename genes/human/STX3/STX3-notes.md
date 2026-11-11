# STX3 (human, Q13277) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: Q13277 is the closest experimentally characterised relative of the
HORSE STX3 benchmark gene (A0A3Q2H352); both sit in PANTHER subfamily
PTHR19957:SF34 (SYNTAXIN-3) per `interpro/panther/PTHR19957/PTHR19957-entries.csv`
(rat Q08849, mouse Q64704 and human Q13277 are the three reviewed members listed).
ProtNLM2 output was not opened or used.

### Deep research

`just deep-research-falcon human STX3 --fallback perplexity-lite` failed on
2026-10-21: falcon raised "Failed to authenticate" and the perplexity-lite
fallback returned HTTP 401 (insufficient quota). No deep-research file exists.
The review is built from cached publications in `publications/` (GOA-cited
papers plus 13 already-cached STX3 papers) and the UniProt record.

### Evolutionary grounding (PAINT)

From `interpro/panther/PTHR19957/PTHR19957-paint.tsv`:

- PTN000461349 (family-wide syntaxin node, no taxon constraint): IBD for
  SNARE binding (GO:0000149), helical-bundle zippering fusogenic activity
  (GO:0005484), SNARE complex (GO:0031201), vesicle fusion (GO:0006906),
  intracellular protein transport (GO:0006886) and endomembrane system
  (GO:0012505). Q13277 is itself a seed for GO:0012505.
- PTN000461524 (plasma-membrane syntaxin clade, taxon:2759): IBD for plasma
  membrane (GO:0005886; Q13277 is a seed) and exocytosis (GO:0006887, dated
  20260828, i.e. newer than the GOA snapshot; the human gene has no GOA
  exocytosis row yet). Proposed as NEW, backed by the PAINT node plus mast-cell,
  beta-cell and enterocyte experiments.
- PTN002717040 (Euteleostomi STX3 orthology node, taxon:117571), seeded only by
  mouse Stx3 (MGI:103077): postsynapse (GO:0098794) and exocytic insertion of
  neurotransmitter receptor to postsynaptic membrane (GO:0098967). This is a
  narrow, STX3-orthologue node; the evidence is murine and there is no human
  experiment. Kept as non-core.

Horse STX3 inherits PTN000461349 and PTN000461524 annotations.

### What is experimentally established in human

- Apical plasma membrane t-SNARE of epithelia: localisation in human Caco-2
  cells and intestinal epithelium [PMID:11003604; PMID:9701566]; loss-of-function
  causes variant microvillus inclusion disease with subapical vesicle
  accumulation [PMID:24726755 "STX3 is an apical receptor involved in membrane
  fusion of apical vesicles in enterocytes."].
- Needed for apical delivery of sucrase-isomaltase in Caco-2 [PMID:11003604].
- Complex with Munc18-2 (STXBP2) at the apical membrane [PMID:9701566;
  PMID:10788461]; in neutrophils Munc18-2 interacts with STX3 on granules
  [PMID:18588921].
- HeLa knockdown reduces surface integrin and accumulates integrins in
  cytoplasmic vesicles [PMID:21720706]; downstream adhesion, chemotaxis and
  survival effects are indirect.
- Retina: human STX3 (mostly STX3B) in photoreceptor inner and outer segments
  and ribbon synapse terminals [PMID:33974130]; patient variants affecting
  STX3B cause early-onset retinal dystrophy.
- Soluble isoform Stx3S (Q13277-3) enters the nucleus via RanBP5/IPO5, binds
  ETV4 and ATF2, and alters gene expression [PMID:29475951].

### Established only in other species (rodent/fish) and carried by orthology

- t-SNARE fusogenic activity of STX3B with SNAP25 and VAMP2 in vitro (mouse
  retina proteins) [PMID:18683220].
- Mast cell compound exocytosis (mouse cKO) [PMID:30563839]; STX3 silencing
  blocks granule fusion in mast cells [PMID:24323579].
- Insulin newcomer granule exocytosis (mouse islets, INS-1) [PMID:23132338].
- CFTR exocytosis in rat jejunum and Caco-2 [PMID:20844248].
- Photoreceptor OS protein trafficking (mouse cKO) [PMID:32778589].
- Axonal targeting in rat hippocampal neurons [PMID:27662481].

### Decisions of note

- GO:0090174 organelle membrane fusion (IMP, PMID:24726755) -> MODIFY to
  GO:0099500 vesicle fusion to plasma membrane; the defect is in fusion of
  apical vesicles with the apical plasma membrane.
- Positive regulation of cell adhesion / chemotaxis / cell proliferation (IMP,
  PMID:21720706): downstream phenotypes of integrin delivery; marked
  over-annotated. The abstract reports apoptosis, not proliferation, and the
  soluble isoform paper reports the opposite sign (Stx3S knockdown promotes
  proliferation).
- Vacuole (TAS, PMID:16339081): abstract does not mention vacuoles; may refer
  to the vacuolar apical compartment of non-polarised cells, which is not the
  GO lytic vacuole. UNDECIDED.
- Cell-cell junction (IDA, PMID:15576373): abstract is about STX4; full text
  not cached. UNDECIDED rather than overrule.
- All GO:0005515 rows removed per the protein-binding policy, except
  PMID:29475951, modified to DNA-binding transcription factor binding
  (ETV4, ATF2).
