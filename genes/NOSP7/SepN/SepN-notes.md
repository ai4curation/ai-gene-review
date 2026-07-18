# SepN (B2IXD4 / Npun_F1232) — Nostoc punctiforme PCC 73102 — research notes

- **UniProt:** B2IXD4 (`B2IXD4_NOSP7`), TrEMBL/unreviewed, 232 aa, 26.5 kDa,
  "Uncharacterized protein".
- **Gene / locus:** OrderedLocusName `Npun_F1232` (RefSeq WP_012407977.1).
- **Organism:** *Nostoc punctiforme* (strain ATCC 29133 / PCC 73102), a filamentous,
  heterocyst-forming (diazotrophic) cyanobacterium of the order Nostocales.
  NCBITaxon:63737.
- **GOA/QuickGO:** returns **no GO annotations** for B2IXD4 (empty `SepN-goa.tsv`). This
  review is therefore de-novo and orthology-based (ISS).

## This protein is the SepN ortholog (orthology evidence)

B2IXD4 is the **SepN ortholog** of the experimentally characterized SepN (locus all4109)
of *Nostoc* sp. PCC 7120 (UniProt A0ACD7RWW5). The assignment comes from a septal-junction
module genome scan (`modules/septal_junction/RESULTS.md`):

- **phmmer homology to the PCC 7120 SepN exemplar (A0ACD7RWW5): E = 5.8e-127, 81.5%
  sequence identity** — a strong, unambiguous ortholog-level match.
- **SepN has no Pfam, InterPro, NCBIfam or PANTHER family model**, so this ortholog is
  detectable **only by exemplar homology** to the characterized PCC 7120 protein; there is
  no domain signature to key on. In the same scan SepN is recovered in every
  heterocyst-forming (positive-control) genome and in **no** unicellular
  (negative-control) genome.
- SepN is a **signature protein of the order Nostocales** and **co-occurs with FraD**
  across filamentous cyanobacteria.

Because the *N. punctiforme* protein has not been assayed directly, all functional
statements below are transferred from the PCC 7120 ortholog with **ISS** evidence; no
direct experimental claim is made about B2IXD4.

## Function transferred from the characterized ortholog (PCC 7120 SepN)

SepN is a bitopic cytoplasmic (inner)-membrane protein that forms the **plug** module of
the **septal junction (SJ)** — the gap-junction-like intercellular channel that traverses
the septal peptidoglycan and connects adjacent cells in a cyanobacterial filament to allow
gated cell-cell molecular exchange. SepN is the FraD-interacting component that gates
(opens/closes) molecular diffusion through the SJ.

- SepN was discovered as a **second structural component of septal junctions** essential
  for gating intercellular communication.
  [PMID:36470860 "Here, we identified a second structural component of septal junctions and demonstrated its essential role in gating intercellular communication."]
- It forms a **cytoplasmic membrane-embedded plug module** of the SJ.
  [PMID:36470860 "a cytoplasmic membrane-embedded plug module"]
- Loss of SepN abolishes gated cell-cell communication.
  [PMID:36470860 "SepN is a septal junction component required for gated cell-cell communication in the filamentous cyanobacterium Nostoc."]
- Structural modeling positions **five SepN copies as a central pentameric plug** anchored
  by peripheral FraD.
  [PMID:42424141 "Structural modeling positions SepN as the plug-forming component and FraD as a membrane-spanning anchor with a periplasmic domain."]

### Topology / membrane localization
UniProt (Phobius) predicts an **N-terminal transmembrane helix (residues 7-26)** in
B2IXD4, consistent with the bitopic cytoplasmic-membrane topology of the characterized
PCC 7120 ortholog (N-terminal TM helix + large cytoplasmic domain). This anchors the plug
in the cytoplasmic (plasma) membrane.

## Protein family

**SepN has no dedicated Pfam / InterPro / NCBIfam / PANTHER family model.** Querying
InterPro for the SepN exemplar returns zero domain matches, and the B2IXD4 UniProt record
is a bare TrEMBL entry carrying only Phobius-predicted membrane/transmembrane keywords and
no domain annotation. The family is instead defined operationally by (i) exemplar homology
to the characterized PCC 7120 SepN and (ii) obligate co-occurrence with FraD across the
Nostocales. Conserved SepN homologs occur across filamentous cyanobacteria of the families
Oscillatoriophycideae, Nostocaceae, and Stigonematales.
[PMID:36470860 "Conserved homologs of SepN can be found in filamentous cyanobacteria of the families Oscillatoriaphycideae, Nostocaceae, and Stigonematales."]
The lack of a formal domain model is expected for a small, lineage-specific structural
protein; detection depends entirely on the exemplar-homology grounding.

## Key references
- PMID:36470860 — Kieninger et al. 2022, *Nat Commun* — identification and characterization
  of SepN as the FraD-interacting SJ plug component (source discovery paper; PCC 7120).
- PMID:42424141 — Kieninger et al. 2026, *Cell Rep* — SepN pentamer forms the plug;
  SepN-FraD structural module (PCC 7120).
- `modules/septal_junction/RESULTS.md` — genome scan establishing B2IXD4 as the
  *N. punctiforme* SepN ortholog (E = 5.8e-127, 81.5% identity; no family model).
