# SepN (G6FVY1 / FJSC11DRAFT_3072) — Fischerella thermalis JSC-11 — research notes

- **UniProt:** G6FVY1 (`G6FVY1_9CYAN`), TrEMBL/unreviewed, 236 aa, 27.1 kDa,
  "Uncharacterized protein" (PE 4: Predicted).
- **Gene / locus:** ORFName `FJSC11DRAFT_3072` (RefSeq WP_009458007.1).
- **Organism:** *Fischerella thermalis* JSC-11, a filamentous, true-branching
  (heterocyst-forming, diazotrophic) cyanobacterium of the order **Nostocales**, family
  **Hapalosiphonaceae** — a member of the deep-branching **Stigonematales** grade.
  NCBITaxon:741277.
- **GOA/QuickGO:** returns **no GO annotations** for G6FVY1 (empty `SepN-goa.tsv`). This
  review is therefore de-novo and orthology-based (ISS).

## This protein is the SepN ortholog (orthology evidence)

G6FVY1 is the **SepN ortholog** of the experimentally characterized SepN (locus all4109)
of *Nostoc* sp. PCC 7120 (UniProt A0ACD7RWW5). The assignment comes from a septal-junction
module genome scan with reciprocal-best-hit (RBH) validation
(`modules/septal_junction/RESULTS.md`):

- **Reciprocal best hit to the PCC 7120 SepN exemplar (A0ACD7RWW5): forward E = 2.0e-93,
  59.5% sequence identity** — a strong, unambiguous ortholog-level match, and reciprocal
  (the 7120 reverse best hit returns to the exemplar). G6FVY1 is 236 aa, essentially the
  same length as the 235-aa PCC 7120 SepN.
- **SepN has no Pfam, InterPro, NCBIfam or PANTHER family model**, so this ortholog is
  detectable **only by exemplar homology** to the characterized PCC 7120 protein; there is
  no domain signature to key on. In the same scan SepN is recovered in every
  heterocyst-forming (positive-control) genome and in **no** unicellular
  (negative-control) genome.
- SepN is a **signature protein of the order Nostocales** and **co-occurs with FraD**
  across filamentous cyanobacteria. In *F. thermalis* JSC-11 the entire septal-junction
  module is present as reciprocal best hits (48–66% id): FraD G6FUM3, FraC G6FUM4,
  FraE G6FUM2 (syntenic operon FJSC11DRAFT_2571/2570/2569), SepN G6FVY1, SepJ G6FMI5,
  AmiC G6FW05.

**SepN reaches the deep-branching Stigonematales.** The recovery of a bona-fide SepN
ortholog in *Fischerella thermalis* (a true-branching Stigonematales cyanobacterium)
confirms that the SepN plug component extends to the deepest-branching heterocyst-formers,
consistent with the SepN discovery paper's report of conserved SepN homologs across the
Oscillatoriaphycideae, Nostocaceae, and Stigonematales.
[PMID:36470860 "Conserved homologs of SepN can be found in filamentous cyanobacteria of the families Oscillatoriaphycideae, Nostocaceae, and Stigonematales."]

Because the *F. thermalis* protein has not been assayed directly, all functional
statements below are transferred from the PCC 7120 ortholog with **ISS** evidence; no
direct experimental claim is made about G6FVY1.

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
By orthology, SepN is a bitopic cytoplasmic-membrane protein with an N-terminal
transmembrane helix anchoring a large cytoplasmic domain. G6FVY1 has a strongly
hydrophobic N-terminal segment (approximately residues 8–28, `FLTLYIIGVTYTFTKMIESI`)
consistent with this bitopic topology, anchoring the plug in the cytoplasmic (plasma)
membrane.

## Protein family

**SepN has no dedicated Pfam / InterPro / NCBIfam / PANTHER family model.** Querying
InterPro for the SepN exemplar returns zero domain matches, and the G6FVY1 UniProt record
is a bare TrEMBL entry (PE 4: Predicted) with no domain annotation. The family is instead
defined operationally by (i) exemplar homology to the characterized PCC 7120 SepN and
(ii) obligate co-occurrence with FraD across the Nostocales. The lack of a formal domain
model is expected for a small, lineage-specific structural protein; detection depends
entirely on the exemplar-homology grounding.

## Key references
- PMID:36470860 — Kieninger et al. 2022, *Nat Commun* — identification and characterization
  of SepN as the FraD-interacting SJ plug component (source discovery paper; PCC 7120).
- PMID:42424141 — Kieninger et al. 2026, *Cell Rep* — SepN pentamer forms the plug;
  SepN-FraD structural module (PCC 7120).
- `modules/septal_junction/RESULTS.md` — RBH genome scan establishing G6FVY1 as the
  *F. thermalis* JSC-11 SepN ortholog (forward E = 2.0e-93, 59.5% identity; reciprocal;
  no family model; module reaches the Stigonematales).
