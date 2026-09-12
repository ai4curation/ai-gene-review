# FraD (B2IXC8 / Npun_R1226) — Nostoc punctiforme PCC 73102 — research notes

- **UniProt:** B2IXC8 (`B2IXC8_NOSP7`), unreviewed (TrEMBL), 335 aa, 37.8 kDa.
- **Gene / locus:** `Npun_R1226` (OrderedLocusName). Product currently annotated only as
  "DUF5357 domain-containing protein" (ProtNLM); it is the **FraD ortholog** in this
  organism (see below).
- **Organism:** *Nostoc punctiforme* (strain ATCC 29133 / PCC 73102), a filamentous,
  heterocyst-forming (diazotrophic) cyanobacterium. NCBITaxon:63737.
- **GOA status:** QuickGO/GOA returns **no GO annotations** for B2IXC8 (empty
  `FraD-goa.tsv`). This review is therefore de-novo and inferred by orthology (ISS).

## This protein is the FraD ortholog (orthology evidence)

The characterized reference protein is *Nostoc* sp. PCC 7120 **FraD** (`alr2393`,
UniProt **P46079**), the membrane-spanning / periplasmic anchor of the septal junction.
B2IXC8 is its ortholog on three independent, mutually reinforcing lines of evidence from a
reproducible module genome scan (`modules/septal_junction/RESULTS.md`):

- **Sequence homology.** phmmer of the PCC 7120 FraD exemplar (P46079) against the
  *N. punctiforme* proteome recovers B2IXC8 as the best hit with **E = 7.4e-165 and 70.3%
  amino-acid identity** — an unambiguous ortholog-level match (near-identical length: 335 aa
  vs 343 aa).
- **Diagnostic protein family.** B2IXC8 is a member of the FraD-specific family
  **InterPro IPR020360** ("Uncharacterised protein family alr2393"; Pfam **PF17310**,
  DUF5357; NCBIfam **NF037953** "frad"). This family is **diagnostic**: it is present in
  every heterocyst-forming cyanobacterial genome examined and absent from every unicellular
  cyanobacterial genome, marking a dedicated septal-junction role.
- **Conserved operon synteny.** The FraC/FraD/FraE best hits carry **consecutive
  accessions** in *N. punctiforme* — **B2IXC9 (FraC) – B2IXC8 (FraD) – B2IXC7 (FraE)** —
  reproducing the intact, syntenic **fraC–fraD–fraE operon** of PCC 7120
  (`alr2392`–`alr2393`–`alr2394`). Genomic context therefore corroborates the FraD
  assignment for B2IXC8.

Because GOA carries no annotations for B2IXC8, its function is inferred from this
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

### Topology (B2IXC8, Phobius / UniProt features)
UniProt B2IXC8 is annotated Membrane / Transmembrane with four Phobius-predicted helices
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
- **PANTHER:** no classification for this family; the FraD family is captured by the
  DUF5357 / IPR020360 / NF037953 models above.

The family's restriction to multicellular (filamentous, heterocyst-forming) cyanobacteria
and absence from unicellular cyanobacteria and all other bacteria is consistent with a
dedicated role in septal-junction-based cell–cell communication rather than a housekeeping
membrane function.

## GO annotation status and proposed terms
- GOA is empty for B2IXC8; proposed core functions (all ISS by orthology to P46079) are
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
- `modules/septal_junction/RESULTS.md` — reproducible module scan providing the homology
  (7.4e-165, 70.3% id), family (IPR020360), and operon-synteny (B2IXC9/B2IXC8/B2IXC7)
  evidence for the FraD ortholog call.
