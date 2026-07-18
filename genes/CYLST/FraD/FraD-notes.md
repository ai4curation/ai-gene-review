# FraD (K9WUY7 / Cylst_1329) — Cylindrospermum stagnale PCC 7417 — research notes

- **UniProt:** K9WUY7 (`K9WUY7_9NOST`), unreviewed (TrEMBL), 335 aa, 37.9 kDa.
- **Gene / locus:** `Cylst_1329` (ORFName). Product currently annotated only as
  "DUF5357 domain-containing protein" (ProtNLM); it is the **FraD ortholog** in this
  organism (see below).
- **Organism:** *Cylindrospermum stagnale* PCC 7417, a filamentous, heterocyst-forming
  (diazotrophic) cyanobacterium (Nostocales; Nostocaceae). NCBITaxon:56107.
- **GOA status:** QuickGO/GOA returns **no GO annotations** for K9WUY7 (empty
  `FraD-goa.tsv`; header row only). This review is therefore de-novo and inferred by
  orthology (ISS).

## This protein is the FraD ortholog (orthology evidence)

The characterized reference protein is *Nostoc* sp. PCC 7120 **FraD** (`alr2393`,
UniProt **P46079**), the membrane-spanning / periplasmic anchor of the septal junction.
K9WUY7 is its ortholog on three independent, mutually reinforcing lines of evidence from a
reproducible module genome scan (`modules/septal_junction/RESULTS.md`):

- **Reciprocal-best-hit orthology.** K9WUY7 is the **reciprocal best hit** of the PCC 7120
  FraD exemplar (P46079) between the two proteomes: the forward phmmer of P46079 against the
  *C. stagnale* proteome recovers K9WUY7 with **E = 7.9e-154 and 66.7% amino-acid
  identity**, and the reverse best hit returns P46079 — an unambiguous 1:1 ortholog-level
  match. *C. stagnale* is a more divergent Nostocalean than the closely related *Anabaena*,
  so the lower identity (66.7% vs ~98% for *A. variabilis*) is expected while still
  comfortably within the ortholog range.
- **Diagnostic protein family.** K9WUY7 is a member of the FraD-specific family
  **InterPro IPR020360** ("Uncharacterised protein family alr2393"; Pfam **PF17310**,
  DUF5357; NCBIfam **NF037953** "frad"). This family is **diagnostic**: it is present in
  heterocyst-forming cyanobacterial genomes and absent from unicellular cyanobacterial
  genomes, marking a dedicated septal-junction role.
- **Conserved operon synteny.** The FraC/FraD/FraE best hits carry **consecutive
  accessions** in *C. stagnale* — **Cylst_1330 (fraC) – Cylst_1329 (fraD) – Cylst_1328
  (fraE)** — reproducing the intact, syntenic **fraC–fraD–fraE operon** of PCC 7120
  (`alr2392`–`alr2393`–`alr2394`). Genomic context therefore corroborates the FraD
  assignment for K9WUY7.

Because GOA carries no annotations for K9WUY7, its function is inferred from this
orthology to the experimentally characterized PCC 7120 FraD, and all proposed annotations
use evidence_type **ISS** (inferred from sequence/structural similarity).

## Function inferred by orthology to PCC 7120 FraD

FraD is a polytopic cytoplasmic (inner)-membrane protein that acts as the
**membrane-spanning and periplasmic anchor** of the **septal junction (SJ)** — the
gap-junction-like intercellular channel that traverses the septal peptidoglycan and
connects adjacent cells in a cyanobacterial filament, mediating gated cell–cell molecular
exchange.

- In PCC 7120, structural modeling positions FraD as the membrane-spanning anchor with a
  periplasmic domain that surrounds the SepN plug of the septal junction
  [PMID:42424141 "Structural modeling positions SepN as the plug-forming component and FraD as a membrane-spanning anchor with a periplasmic domain."].
  The determination combined cryo-electron tomography, AlphaFold 3 and molecular dynamics
  [PMID:42424141 "we combine cryo-electron tomography, AlphaFold 3 structure prediction, and molecular dynamics simulation"].
- The FraD periplasmic domain is required for septal-junction assembly and function
  [PMID:42424141 "Functional analyses demonstrate that the FraD periplasmic domain is required for proper nanopore formation, SJ assembly, and diazotrophic growth."].
- FraD localizes to the intercellular septa (GFP fusions) in PCC 7120
  [PMID:20487302 "As shown with GFP fusions, FraC and FraD are also located at the intercellular septa."]
  and *fra* mutants are defective in gated intercellular exchange
  [PMID:20487302 "hampered in the intercellular transfer of the fluorescent probe calcein"],
  failing diazotrophic growth despite forming heterocysts
  [PMID:20487302 "did not grow diazotrophically, although they formed heterocysts"].

### Topology (K9WUY7, Phobius / UniProt features)
UniProt K9WUY7 is annotated Membrane / Transmembrane with four Phobius-predicted helices
(FT TRANSMEM 32–51, 58–76, 82–103, 152–172), matching the N-terminal transmembrane bundle
of PCC 7120 FraD (five helices, ~aa 30–172) followed by a large C-terminal periplasmic
domain. The conserved architecture is consistent with the same membrane-anchor +
periplasmic-anchor role.

## Protein family

FraD is the reference member of a small, taxonomically restricted family confined to
filamentous, heterocyst-forming cyanobacteria:

- **InterPro IPR020360** — "Uncharacterised protein family alr2393"; members are components
  of cyanobacterial septal junctions in heterocyst-forming cyanobacteria.
- **Pfam PF17310** — DUF5357 ("Family of unknown function").
- **NCBIfam NF037953** — dedicated FraD HMM ("frad").
- The family co-occurs phylogenetically with its septal-junction plug partner SepN
  [PMID:36470860 "SepN always co-occurs with FraD."].

The family's restriction to multicellular (filamentous, heterocyst-forming) cyanobacteria
and absence from unicellular cyanobacteria and all other bacteria is consistent with a
dedicated role in septal-junction-based cell–cell communication rather than a housekeeping
membrane function.

## GO annotation status and proposed terms
- GOA is empty for K9WUY7; proposed core functions (all ISS by orthology to P46079) are
  recorded in `FraD-ai-review.yaml`:
  - GO:0005198 structural molecule activity (MF)
  - GO:0005886 plasma membrane (CC)
  - GO:0042597 periplasmic space (CC)
  - GO:0007267 cell-cell signaling (BP)
- No dedicated GO cellular-component term exists for the bacterial **septal junction**
  (GO:0005918 "septate junction" is the arthropod epithelial junction, not this structure).

## Key references
- PMID:42424141 — Kieninger et al. 2026, *Cell Rep* — SepN–FraD structural module (PCC 7120).
- PMID:36470860 — Kieninger et al. 2022, *Nat Commun* — SepN identified as FraD-interacting SJ plug component.
- PMID:20487302 — Merino-Puerto et al. 2010, *Mol Microbiol* — Fra proteins; fraCDE operon; septal localization (PCC 7120).
- `modules/septal_junction/RESULTS.md` — reproducible module scan providing the RBH
  homology (forward E = 7.9e-154, 66.7% id; reciprocal), family (IPR020360), and
  operon-synteny (Cylst_1330/Cylst_1329/Cylst_1328) evidence for the FraD ortholog call.
