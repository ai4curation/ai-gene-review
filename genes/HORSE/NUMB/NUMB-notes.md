# NUMB (horse, A0A5F5PK46) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 file or prediction-evidence folder was opened for this review.

### Setup

- `just fetch-gene HORSE A0A5F5PK46 --alias NUMB` created the folder; stub id is
  A0A5F5PK46 (confirmed). 21 GOA rows (4 IBA, 17 IEA; no experimental rows on the
  horse entry itself).
- Deep research: `just deep-research-falcon HORSE NUMB --fallback perplexity-lite`
  FAILED (falcon: "Failed to authenticate"; perplexity-lite: HTTP 401 insufficient
  quota). No deep-research file exists. The review is based on cached primary
  literature (fetched with `just fetch-pmid`) and QuickGO queries of the
  experimental annotations of human P49757 and mouse Q9QZS3.

### Identity and phylogenetic placement

- A0A5F5PK46 is 652 aa, PE 4 (TrEMBL, Ensembl ENSECAP00000048868). Global
  alignment (`NUMB-bioinformatics/compare_sequences.py`, `RESULTS.md`) to human
  NUMB P49757 (651 aa, canonical isoform 1) gives 630 identical positions with only
  three 1-aa indels; to mouse Q9QZS3 (653 aa) 614 identical positions. It is a
  full-length canonical product (both alternatively spliced PTB and PRR inserts
  present by length), not a fragment or short isoform.
- PANTHER PTHR47368:SF5 (PROTEIN NUMB HOMOLOG), the same subfamily as human
  P49757, mouse Q9QZS3 and rat Q2LC84. NUMBL paralogs are SF4; Drosophila numb and
  C. elegans num-1 are SF2. So the horse protein is the 1:1 NUMB ortholog, and
  transfer of mammalian NUMB experimental functions is phylogenetically grounded.
  The repo PANTHER family folder (`interpro/panther/PTHR47368/`) agrees with
  UniProt on subfamily placement; there is no family review YAML.
- IBA rows come from PTN000132807 (cytoplasm; broad node including zebrafish
  numb/numbl and mouse Numb/Numbl), PTN002599555 (basolateral plasma membrane,
  cytoplasmic vesicle) and PTN008318191 (positive regulation of neurogenesis).
  Notably PAINT did NOT propagate Drosophila numb's "negative regulation of Notch
  signaling pathway" (many IMP/IGI rows on P16554, SF2) to the vertebrate
  nodes; I treat that as a deliberate decision and do not add it as NEW.

### Literature (mammalian NUMB, SF5)

- Santolini et al. 2000 [PMID:11121447 "Here, we demonstrate that Numb is an
  endocytic protein."]; immuno-EM places Numb on "endosomes, clathrin-coated pits,
  and vesicles" and it "associates with the appendage domain of alpha adaptin".
- Li et al. 2014 [PMID:24336247 "Numb, a clathrin adaptor, specifically recognized
  this motif and recruited clathrin for internalization."] — NUMB PTB binds the
  NPC1L1 YVNXXF motif; this is direct clathrin-cargo adaptor activity.
- Sorensen & Conner 2008 [PMID:18657069] — AAK1 phosphorylates Numb (T102);
  Numb at plasma membrane / coated pits, required for transferrin and LDL uptake.
- Rasin et al. 2007 [PMID:17589506 "Numb accumulates in the apical end-feet, where
  it localizes to adherens junction-associated vesicles and interacts with
  cadherins."] — source of cadherin/alpha-/beta-catenin binding, apical part of
  cell, basolateral membrane annotations (mouse IPI/IDA).
- Kuo et al. 2006 [PMID:17174898] — source of lateral ventricle development and
  "neuroblast division in SVZ" (mouse IMP). Full text: the phenotype is SVZ
  neuroblast *survival* and ependymal integrity, and the authors state that
  accumulation of neuroblasts "was not caused by over-proliferation". I mark
  the division term as over-annotated for the horse transfer.
- Petersen et al. 2002 [PMID:12410312] — Numb/Numbl maintain neural progenitors;
  source of positive regulation of neurogenesis (mouse IMP).
- McGill & McGlade 2003 [PMID:12682059] — mammalian Numb promotes Notch1
  ubiquitination via Itch (abstract only). Not proposed as a NEW BP because
  PAINT/vertebrate MOD curators have not made the Notch annotation for SF5;
  raised as a question.
- Nishimura et al. 2006 [PMID:16394100] — dendritic spines, intersectin.
- Zhou et al. 2015 [PMID:26621723] — Numb required for mGlu1 internalization and
  recycling in Purkinje cells (glutamatergic synapse, receptor internalization).
- Teckchandani et al. 2009 [PMID:19581412] — Dab2 paper; full text shows Numb
  depletion raises surface integrin alpha5 and inhibits migration (source of human
  IMP rows for cell migration and protein localization to plasma membrane).
- Colaluca et al. 2008 [PMID:18172499] — NUMB/p53/HDM2 tricomplex; context only.

### Decisions summary

Core: clathrin-cargo endocytic adaptor (PTB domain, AP-2/EPS15 binding) at
clathrin-coated pits/vesicles and endosomes. NEW: GO:0035615 clathrin-cargo
adaptor activity and GO:0072583 clathrin-dependent endocytosis (NUMB itself
performs the adaptor step; not a substrate). Cytoplasm and cytoplasmic vesicle
MODIFY to clathrin-coated vesicle / pit. Developmental and cell-type-specific
process terms KEEP_AS_NON_CORE; neuroblast division MARK_AS_OVER_ANNOTATED.

### Relative

Closest characterised relative by PANTHER SF5 placement: human NUMB (P49757).
No human or mouse NUMB review exists in `genes/` (searched by symbol and
accession). Donkey NUMB (genes/EQUAS/NUMB) is the paired cohort target, not the
relative.

### Modules

Only `modules/intestinal_sterol_absorption_and_efflux.yaml` mentions NUMB (as an
NPC1L1 endocytic partner).
