# SepN (Cylst_2059) — Cylindrospermum stagnale PCC 7417 — research notes

- **UniProt:** K9WXR0 (`K9WXR0_9NOST`), TrEMBL/unreviewed, 234 aa, 26.5 kDa.
- **Gene / locus:** `Cylst_2059` (ORFName; RefSeq WP_015207557.1). Assigned gene symbol
  **SepN** by orthology to the experimentally characterized *Nostoc* sp. PCC 7120 SepN
  (locus `all4109`, UniProt A0ACD7RWW5).
- **Organism:** *Cylindrospermum stagnale* PCC 7417, a filamentous, heterocyst-forming
  (diazotrophic) cyanobacterium of the order Nostocales (family Nostocaceae).
  NCBITaxon:56107.
- **UniProt annotation status:** bare TrEMBL record, "Uncharacterized protein"; the only
  computed feature is a Phobius-predicted N-terminal transmembrane helix
  (`FT TRANSMEM 6..23`, Helical), consistent with the bitopic membrane topology of the
  characterized ortholog.

## Orthology evidence (basis for function transfer, ISS)

SepN function is transferred to K9WXR0 by **orthology** to *Nostoc* sp. PCC 7120 SepN
(A0ACD7RWW5), not by direct assay on the *C. stagnale* protein.

- **Reciprocal best hit (RBH):** K9WXR0 (Cylst_2059) is the reciprocal best hit of the
  PCC 7120 SepN exemplar A0ACD7RWW5 (forward E = 9.3e-111, **69.4% sequence identity**;
  reverse best hit returns to A0ACD7RWW5). See `modules/septal_junction/RESULTS.md` for the
  scan methodology (`ai-gene-review scan-module`, phmmer homology + `--rbh` reciprocity).
- **No family model:** SepN has **no dedicated Pfam / InterPro / PANTHER / NCBIfam
  signature** — it is detectable only by exemplar homology to the representative member.
  This matches the PCC 7120 ortholog, whose InterPro query returns zero matches.
  [PMID:36470860 "Conserved homologs of SepN can be found in filamentous cyanobacteria of the families Oscillatoriaphycideae, Nostocaceae, and Stigonematales."]
- **Nostocales signature:** SepN is a signature protein of the order Nostocales and
  (with one exception) always co-occurs with FraD. *C. stagnale* PCC 7417 is a Nostocales
  member, consistent with carrying a genuine SepN ortholog.
  [PMID:36470860 "SepN always co-occurs with FraD."]

## Function summary (transferred by orthology)

In the characterized *Nostoc* PCC 7120 ortholog, SepN is a bitopic cytoplasmic
(inner)-membrane protein that forms the **plug** module of the **septal junction (SJ)** —
the gap-junction-like intercellular channel connecting adjacent cells in a filament. Five
SepN copies assemble into a central pentameric plug surrounded by peripheral FraD anchors;
SepN is the FraD-interacting component that gates (opens/closes) molecular diffusion
through the SJ, controlling cell-cell communication along the filament.

- **Structural (non-catalytic) role — GO:0005198 structural molecule activity.**
  [PMID:36470860 "Here, we identified a second structural component of septal junctions and demonstrated its essential role in gating intercellular communication."]
- **Cytoplasmic (plasma) membrane location — GO:0005886 plasma membrane.**
  [PMID:36470860 "a cytoplasmic membrane-embedded plug module"] — and the K9WXR0 Phobius
  TM helix (residues 6–23) supports membrane anchoring.
- **Gated cell-cell communication — GO:0007267 cell-cell signaling.**
  [PMID:36470860 "SepN is a septal junction component required for gated cell-cell communication in the filamentous cyanobacterium Nostoc."]
- **Structural model / plug identity:**
  [PMID:42424141 "Structural modeling positions SepN as the plug-forming component and FraD as a membrane-spanning anchor with a periplasmic domain."]

## GO annotation status

- GOA/QuickGO returns **no GO annotations** for K9WXR0 (empty `SepN-goa.tsv`). This review
  is de-novo: proposed core functions are recorded in `SepN-ai-review.yaml` as `action: NEW`
  with `evidence_type: ISS` (inferred from sequence/structural similarity to the PCC 7120
  ortholog). No direct assays on the *C. stagnale* protein are claimed.
- No dedicated GO cellular-component term exists for the bacterial **septal junction**
  (GO:0005918 "septate junction" is the arthropod epithelial junction). Candidate new term.

## Key references

- PMID:36470860 — Kieninger et al. 2022, *Nat Commun* — identification/characterization of
  SepN as the FraD-interacting SJ plug component (source discovery paper, PCC 7120).
- PMID:42424141 — Kieninger et al. 2026, *Cell Rep* — SepN pentamer forms the plug;
  SepN–FraD architecture (abstract in cache).
