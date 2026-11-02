# Vmn2r73 (D3Z7M3) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 output was opened or used.

### Identity

- D3Z7M3 is the 851-residue Ensembl-canonical product (ENSMUST00000077478) of mouse Vmn2r73
  (MGI:3646433, ENSMUSG00000070458). The sibling folder `genes/mouse/Vmn2r73/` reviews A0A3B2WCZ5,
  a 496-residue non-canonical gene model of the same gene that lacks the 7TM domain
  [file:mouse/Vmn2r73/Vmn2r73-bioinformatics/RESULTS-rereview.md "UniProt records no TRANSMEM feature
  on A0A3B2WCZ5, against seven on D3Z7M3 (584-606 to 800-822)"].
- UniProt D3Z7M3 (unreviewed, PE 4): SignalP signal peptide 1-18, seven Phobius TM helices 584-822,
  Pfam ANF_receptor + NCD3G + 7tm_3, CDD cd15283 7tmC_V2R_pheromone, PANTHER PTHR24061:SF413
  ("VOMERONASAL 2, RECEPTOR 66-RELATED").

### Deep research

- `just deep-research-falcon mouse Vmn2r73__D3Z7M3 --fallback perplexity-lite` failed on 2026-10-21:
  falcon "Exception: Failed to authenticate"; perplexity-lite fallback HTTP 401 (insufficient quota).
  No deep-research file was produced for this folder.
- Used instead the existing falcon report for the same gene (run under the sibling accession):
  `genes/mouse/Vmn2r73/Vmn2r73-deep-research-falcon.md`, which found no Vmn2r73-specific
  ligand, localisation, signaling, knockout or behavioural study.
- Europe PMC search for "Vmn2r73" (2026-10-21): 3 hits (PMID:35384748, 23468633, 25279261), all
  incidental appearances in QTL candidate lists or expression profiles; none is a functional study.

### PAINT node PTN002373557 (evolutionary grounding)

- GPCR activity donors (resolved via Alliance API): Casr (MGI:1351351), Gprc6a (MGI:2429498),
  human CASR (P41180) and eight V2Rs: Vmn2r26, Vmn2r81, Vmn2r65, Vmn2r120, Vmn2r83, Vmn2r1, Vmn2r82,
  Vmn2r116.
- QuickGO: the V2R donors carry experimental annotations to descendants of GO:0004930:
  GO:0038022 (G protein-coupled olfactory receptor activity; Vmn2r1 IMP, Vmn2r65/81/82/83/120 IGI,
  PMID:29465786) and GO:0016503 (pheromone receptor activity; Vmn2r116 IGI, PMID:20596023).
- The curator propagated only GO:0004930, not the olfactory/pheromone receptor descendants. Treated
  as deliberate: those terms depend on the ligand.
- PANTHER subfamilies of the V2R donors (UniProt): SF545, SF457, SF398, SF547, SF546 -- none is
  SF413 (Vmn2r73). So no subfamily-specific ligand (ESP1, MHC peptides, etc.) is transferred.
- Plasma membrane IBA donors: Casr (mouse, rat, human), Gprc6a (mouse, rat), human TAS1R2/TAS1R3.
  No V2R donor; accepted because it is the expected location of a 7TM class C receptor and the
  product has the topology.

### Decisions

- GO:0004930 IBA + IEA: ACCEPT (core; inferred, not experimental).
- GO:0005886 IBA + IEA: ACCEPT (IEA source is ARBA, not cited as support; topology cited instead).
- GO:0007186 IEA: ACCEPT (receptor's own step).
- GO:0016020 IEA: MODIFY -> GO:0005886.
- No NEW terms. Pheromone receptor activity / detection of pheromone / sensory perception of smell
  not proposed: ligand unknown and PAINT curators declined to propagate them.
- For transfer purposes: nothing about Vmn2r73 is experimentally established in mouse. Everything is
  family-level inference.
