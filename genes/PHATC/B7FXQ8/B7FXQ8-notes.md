# B7FXQ8 (HSP20A, PHATRDRAFT_35158) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used.

### Identity
- UniProt B7FXQ8 (TrEMBL, PE 3), 163 aa, gene model PHATRDRAFT_35158 on chromosome 7.
- This is the full-length product, not a fragment or isoform. It has a complete ACD
  (PROSITE PS01031, 47-155), an aromatic-rich N-terminal region and a C-terminal
  extension with the I-X-I motif (IAI 150-152). No signal peptide or transit
  peptide is annotated.
- GOA has no annotations for this accession, so `existing_annotations` holds only
  proposed NEW rows.

### Evolutionary placement (B7FXQ8-bioinformatics/RESULTS.md, shsp_tree.py)
- InterPro places it in PTHR11527 at family level only, with no subfamily.
  P. tricornutum is not a PANTHER 19 genome (pantherdb supportedgenomes), so it
  is not in the PANTHER tree and receives no IBA rows.
- PTHR11527 root = PTN000163021 (LUCA). Root IBDs: GO:0006457, GO:0009408,
  GO:0009651, GO:0042542, GO:0051259. No MF is placed at the root, because
  GO:0051082 is obsolete. The T. pseudonana PTHR11527:SF175 members B8CD87 and
  B8BTA8 carry all five as IBA.
- ACD NJ tree: B7FXQ8 is sister to T. pseudonana B8CD87 (SF175), with 52.5% ACD
  identity. That lineage is diatom-only and uncharacterised. The characterised
  relatives (Arabidopsis HSP17.6A and HSP17.7, rice and wheat class I, yeast
  HSP26, S. pombe hsp16) are family-level relatives that share only the root node.
  None is an ortholog.

### Decisions
- Core MF: proposed `holdase chaperone activity` (NTR), following the repo sHSP
  convention (HSP17.7, HSP26), in place of GO:0044183. GO:0044183 requires assisting
  folding. The earlier draft's GO:0044183 choice came from the OpenScientist run
  and was not kept.
- Processes: NEW `response to heat` and `protein complex oligomerization`, both
  root-node IBDs. The protein does part of the work of each (it holds clients and
  assembles itself).
- Not proposed: `response to salt stress` and `response to hydrogen peroxide`. They
  are root IBDs, but they rest on plant phenotypes, and the family review marks them
  UNRESOLVED. Also not proposed: `protein folding`, since a holdase does not fold
  its clients and the family review leaves this UNRESOLVED. Removed from core: the
  earlier `cellular response to unfolded protein` (no evidence) and `cytoplasm`
  (not measured).
- The earlier draft's quotes from the deep-research file did not match it
  verbatim. Its UniProt DOMAIN quote was a composite. All of them were replaced by
  verifiable quotes.

### Relative to review next
- No characterised ortholog exists. The nearest characterised family members with
  complete repo reviews are ARATH HSP17.7 (O81822, COMPLETE) and yeast HSP26
  (P15992, COMPLETE). HSP17.7 is reported as the relative (family_member, shared
  PTHR11527 root node only).

### Modules
- modules/heat_shock_response.yaml (HSF-driven cytosolic heat shock response,
  with sHSPs as outputs). modules/plant_hsfa1_heat_stress_response.yaml is
  Arabidopsis-specific context only.
