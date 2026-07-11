# SepN (Q3MF16 / Ava_0796) — Anabaena variabilis / Trichormus variabilis ATCC 29413 — research notes

- **UniProt:** Q3MF16 (`Q3MF16_TRIV2`), TrEMBL/unreviewed, 235 aa, 26.7 kDa,
  "Uncharacterized protein".
- **Gene / locus:** OrderedLocusName `Ava_0796` (RefSeq WP_011317653.1).
- **Organism:** *Trichormus variabilis* (strain ATCC 29413 / PCC 7937), formerly
  *Anabaena variabilis*, a filamentous, heterocyst-forming (diazotrophic) cyanobacterium
  of the order Nostocales. NCBITaxon:240292.
- **GOA/QuickGO:** returns **no GO annotations** for Q3MF16 (empty `SepN-goa.tsv`). This
  review is therefore de-novo and orthology-based (ISS).

## This protein is the SepN ortholog (orthology evidence)

Q3MF16 is the **SepN ortholog** of the experimentally characterized SepN (locus all4109)
of *Nostoc* sp. PCC 7120 (UniProt A0ACD7RWW5). The assignment comes from a septal-junction
module genome scan with reciprocal-best-hit (RBH) validation
(`modules/septal_junction/RESULTS.md`):

- **Reciprocal best hit to the PCC 7120 SepN exemplar (A0ACD7RWW5): forward E = 4.6e-151,
  96.6% sequence identity** — a strong, unambiguous ortholog-level match, and reciprocal
  (the 7120 reverse best hit returns to the exemplar). Q3MF16 is also exactly 235 aa, the
  same length as the PCC 7120 SepN.
- **SepN has no Pfam, InterPro, NCBIfam or PANTHER family model**, so this ortholog is
  detectable **only by exemplar homology** to the characterized PCC 7120 protein; there is
  no domain signature to key on. In the same scan SepN is recovered in every
  heterocyst-forming (positive-control) genome and in **no** unicellular
  (negative-control) genome.
- SepN is a **signature protein of the order Nostocales** and **co-occurs with FraD**
  across filamentous cyanobacteria. In *A. variabilis* the FraCDE operon orthologs
  (FraD Q3MGQ1, FraC Q3MGQ2, FraE Q3MGQ0) are also present as reciprocal best hits.

Because the *A. variabilis* protein has not been assayed directly, all functional
statements below are transferred from the PCC 7120 ortholog with **ISS** evidence; no
direct experimental claim is made about Q3MF16.

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
- `sepN` encodes an unknown protein of 235 aa in the characterized ortholog, matching the
  235-aa length of Q3MF16.
  [PMID:36470860 "sepN encodes an unknown protein of 235 aa"]
- Structural modeling positions **five SepN copies as a central pentameric plug** anchored
  by peripheral FraD.
  [PMID:42424141 "Structural modeling positions SepN as the plug-forming component and FraD as a membrane-spanning anchor with a periplasmic domain."]

### Topology / membrane localization
UniProt (Phobius) predicts an **N-terminal transmembrane helix (residues 9-27)** in
Q3MF16, consistent with the bitopic cytoplasmic-membrane topology of the characterized
PCC 7120 ortholog (N-terminal TM helix + large cytoplasmic domain). This anchors the plug
in the cytoplasmic (plasma) membrane.

## Protein family

**SepN has no dedicated Pfam / InterPro / NCBIfam / PANTHER family model.** Querying
InterPro for the SepN exemplar returns zero domain matches, and the Q3MF16 UniProt record
is a bare TrEMBL entry carrying only Phobius-predicted membrane/transmembrane keywords and
no domain annotation. The family is instead defined operationally by (i) exemplar homology
to the characterized PCC 7120 SepN and (ii) obligate co-occurrence with FraD across the
Nostocales. Conserved SepN homologs occur across filamentous cyanobacteria.
[PMID:36470860 "Conserved homologs of SepN can be found in filamentous cyanobacteria of the families Oscillatoriaphycideae, Nostocaceae, and Stigonematales."]
The lack of a formal domain model is expected for a small, lineage-specific structural
protein; detection depends entirely on the exemplar-homology grounding.

## Key references
- PMID:36470860 — Kieninger et al. 2022, *Nat Commun* — identification and characterization
  of SepN as the FraD-interacting SJ plug component (source discovery paper; PCC 7120).
- PMID:42424141 — Kieninger et al. 2026, *Cell Rep* — SepN pentamer forms the plug;
  SepN-FraD structural module (PCC 7120).
- `modules/septal_junction/RESULTS.md` — RBH genome scan establishing Q3MF16 as the
  *A. variabilis* SepN ortholog (forward E = 4.6e-151, 96.6% identity; reciprocal;
  no family model).
