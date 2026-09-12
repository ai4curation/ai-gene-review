# FraD (G6FUM3 / FJSC11DRAFT_2570) — Fischerella thermalis JSC-11 — research notes

- **UniProt:** G6FUM3 (`G6FUM3_9CYAN`), unreviewed (TrEMBL), 337 aa, 38.0 kDa.
- **Gene / locus:** `FJSC11DRAFT_2570` (ORFName). Product currently annotated only as
  "DUF5357 domain-containing protein" (ProtNLM); it is the **FraD ortholog** in this
  organism (see below).
- **Organism:** *Fischerella thermalis* JSC-11, a filamentous, heterocyst-forming
  (diazotrophic) cyanobacterium of the order **Stigonematales** (Nostocales sensu lato;
  Hapalosiphonaceae/Fischerella) — a **true-branching**, deep-branching heterocyst-forming
  lineage. NCBITaxon:741277.
- **GOA status:** QuickGO/GOA returns **no GO annotations** for G6FUM3 (empty
  `FraD-goa.tsv`; header row only). This review is therefore de-novo and inferred by
  orthology (ISS).

## This protein is the FraD ortholog (orthology evidence)

The characterized reference protein is *Nostoc* sp. PCC 7120 **FraD** (`alr2393`,
UniProt **P46079**), the membrane-spanning / periplasmic anchor of the septal junction.
G6FUM3 is its ortholog on three independent, mutually reinforcing lines of evidence from a
reproducible module genome scan (`modules/septal_junction/RESULTS.md`):

- **Reciprocal-best-hit orthology.** G6FUM3 is the **reciprocal best hit** of the PCC 7120
  FraD exemplar (P46079) between the two proteomes: the forward phmmer of P46079 against the
  *F. thermalis* proteome recovers G6FUM3 with **E = 4.5e-124 and 55.0% amino-acid
  identity**, and the reverse best hit returns P46079 — an unambiguous 1:1 ortholog-level
  match (337 aa vs 343 aa). *F. thermalis* is a **Stigonematalean**, the most
  deeply-branching heterocyst-forming lineage sampled here, so the lower identity (55.0% vs
  ~98% for the closely related *Anabaena variabilis*) is expected while still comfortably
  within the ortholog range and far above the twilight zone.
- **Diagnostic protein family.** G6FUM3 is a member of the FraD-specific family
  **InterPro IPR020360** ("Uncharacterised protein family alr2393"; Pfam **PF17310**,
  DUF5357; NCBIfam **NF037953** "frad"). This family is **diagnostic**: it is present in
  heterocyst-forming cyanobacterial genomes and absent from unicellular cyanobacterial
  genomes, marking a dedicated septal-junction role.
- **Conserved operon synteny.** The FraC/FraD/FraE best hits carry **consecutive
  accessions** in *F. thermalis* — **FJSC11DRAFT_2571 (fraC, G6FUM4) – FJSC11DRAFT_2570
  (fraD, G6FUM3) – FJSC11DRAFT_2569 (fraE, G6FUM2)** — reproducing the intact, syntenic
  **fraC–fraD–fraE operon** of PCC 7120 (`alr2392`–`alr2393`–`alr2394`). Genomic context
  therefore corroborates the FraD assignment for G6FUM3.

Because GOA carries no annotations for G6FUM3, its function is inferred from this
orthology to the experimentally characterized PCC 7120 FraD, and all proposed annotations
use evidence_type **ISS** (inferred from sequence/structural similarity).

## Significance: the septal-junction module reaches the Stigonematales

*F. thermalis* is a **Stigonematalean** (true-branching) cyanobacterium — the
**deepest-branching heterocyst-forming lineage** examined in the septal-junction module
scan. The recovery here of a complete, syntenic **fraC–fraD–fraE operon** with a
reciprocal-best-hit FraD ortholog demonstrates that the FraD-based septal-junction anchor
module is **conserved across the entire radiation of multicellular (heterocyst-forming)
cyanobacteria**, from *Nostoc/Anabaena* to the true-branching Stigonematales. This makes
FraD (and its SJ partners) part of the **ancestral toolkit** of cyanobacterial
multicellularity rather than a *Nostoc/Anabaena*-specific innovation. (The module scan also
finds that *F. thermalis* carries both AmiC1 and AmiC2 septal amidase homologs, consistent
with an ancestral septal-junction/nanopore-forming apparatus in this lineage.)

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

### Topology (G6FUM3, Phobius / UniProt features)
UniProt G6FUM3 is annotated Membrane / Transmembrane with four Phobius-predicted helices
(FT TRANSMEM 30–46, 53–73, 79–102, 151–171), matching the N-terminal transmembrane bundle
of PCC 7120 FraD (five helices, ~aa 30–172) followed by a large C-terminal periplasmic
domain. The conserved architecture is consistent with the same membrane-anchor +
periplasmic-anchor role.

## Protein family

FraD is the reference member of a small, taxonomically restricted family confined to
filamentous, heterocyst-forming cyanobacteria:

- **InterPro IPR020360** — "Uncharacterised protein family alr2393"; members are components
  of cyanobacterial septal junctions in heterocyst-forming cyanobacteria.
- **Pfam PF17310** — DUF5357 ("Family of unknown function").
- **NCBIfam NF037953** — dedicated FraD HMM ("frad"); G6FUM3 is a hit.
- The family co-occurs phylogenetically with its septal-junction plug partner SepN
  [PMID:36470860 "SepN always co-occurs with FraD."].

The family's restriction to multicellular (filamentous, heterocyst-forming) cyanobacteria
and absence from unicellular cyanobacteria and all other bacteria is consistent with a
dedicated role in septal-junction-based cell–cell communication rather than a housekeeping
membrane function.

## GO annotation status and proposed terms
- GOA is empty for G6FUM3; proposed core functions (all ISS by orthology to P46079) are
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
  homology (forward E = 4.5e-124, 55.0% id; reciprocal), family (IPR020360), and
  operon-synteny (FJSC11DRAFT_2571/2570/2569; G6FUM4/G6FUM3/G6FUM2) evidence for the FraD
  ortholog call, and the finding that the septal-junction module reaches the Stigonematales.
