# FraD (alr2393) — Nostoc sp. PCC 7120 — research notes

- **UniProt:** P46079 (`Y2393_NOSS1`), reviewed, 343 aa, 39.3 kDa.
- **Gene / locus:** `fraD` = `alr2393`. Third gene of the `fraC`–`fraD`–`fraE` operon
  (`alr2392`–`alr2393`–`alr2394`).
- **Organism:** *Nostoc* sp. (strain PCC 7120 / SAG 25.82 / UTEX 2576), a filamentous,
  heterocyst-forming (diazotrophic) cyanobacterium. NCBITaxon:103690.
- **Family / classification:**
  - TCDB `1.V.1.1.1` — "the filamentous cyanobacterial septal pore (septum) family"
    [file:NOSS1/FraD/FraD-uniprot.txt "TCDB; 1.V.1.1.1; the filamentous cyanobacterial septal pore (septum) family."].
  - NCBIfam `NF037953` ("frad") — dedicated FraD HMM
    [file:NOSS1/FraD/FraD-uniprot.txt "NCBIfam; NF037953; frad; 1."].
  - Pfam `PF17310` (DUF5357); InterPro `IPR020360`.

## Function summary

FraD is a polytopic cytoplasmic (inner)-membrane protein that acts as the
**membrane-spanning and periplasmic anchor** of the **septal junction (SJ)** — the
gap-junction-like intercellular channel that traverses the septal peptidoglycan and
connects adjacent cells in a cyanobacterial filament, mediating gated cell–cell
molecular exchange.

### Topology (from Cell Reports 2026, Phobius prediction + cryoET fitting)
- Short N-terminal cytoplasmic segment (aa 1–28/29).
- **Five transmembrane helices** (aa ~30–172; helices at 30–51, 58–76, 82–103, 115–132,
  152–172) embedded in the cytoplasmic membrane.
- **Large C-terminal periplasmic domain** (aa 173–343) that forms the SJ periplasmic
  anchoring module.
  [PMID:42424141 "Structural modeling positions SepN as the plug-forming component and FraD as a membrane-spanning anchor with a periplasmic domain."]

### Role in the septal junction
- FraD provides the transmembrane and periplasmic **anchor** of the SJ; five FraD
  molecules surround a central SepN pentamer (the plug), extending from the cytoplasmic
  membrane into the periplasm. Cryo-ET subtomogram averaging shows the periplasmic-anchor
  density present in WT but **absent in the `fraD∆PP` (periplasmic-domain deletion)**
  mutant, confirming FraD forms that structure (Cell Reports 2026, Fig 3H–I).
- FraD is an essential **assembly platform** required for formation of both the plug and
  cap SJ modules; the `∆fraD` knockout loses these structures and can no longer gate
  cell–cell communication.

### Loss-of-function phenotypes
- `∆fraD`: filament fragmentation under N-deprivation, loss of SJ plug/cap, uncontrolled
  molecular exchange, strongly reduced septal nanopore number, enlarged septa, and
  **failure to grow diazotrophically** despite forming (non-functional) heterocysts.
  [PMID:20487302 "Single mutants of these genes showed filament fragmentation under nitrogen deprivation and did not grow diazotrophically, although they formed heterocysts."]
- FraD (and FraC) localize to the intercellular septa and are needed for proper SepJ
  localization and for intercellular calcein transfer.
  [PMID:20487302 "As shown with GFP fusions, FraC and FraD are also located at the intercellular septa."]
  [PMID:20487302 "The fraC and fraD mutants showed an impaired localization of SepJ at the intercellular septa and were hampered in the intercellular transfer of the fluorescent probe calcein."]
- Domain dissection (Cell Reports 2026): the **transmembrane region** is essential for SJ
  assembly and closure; the **periplasmic extension** contributes to nanopore
  organization, structural stability, and SJ **reopening** after stress. `fraD∆TM`
  (periplasmic domain alone) mislocalizes to the cytoplasm and complements nothing;
  `fraD∆PP` (TM domain, no periplasmic domain) can close but not reliably reopen SJs and
  **still fails to grow diazotrophically** (reduced nitrogenase activity, aberrant
  heterocyst septa).
  [PMID:42424141 "Functional analyses demonstrate that the FraD periplasmic domain is required for proper nanopore formation, SJ assembly, and diazotrophic growth."]

### Operon / discovery
- `fraC` (`alr2392`) is constitutively expressed as an operon with the downstream
  `alr2393` (`fraD`) and `alr2394` (`fraE`).
  [PMID:20487302 "was constitutively expressed as an operon together with two downstream genes,"]
- The founding `fraD` mutant was isolated as a short-filament / fragmentation mutant of
  Anabaena (Nostoc) PCC 7120 [PMID:7883709]. Note UniProt ref [2] (PMID:7883709) sequenced
  only aa 1–172 and carries a sequence conflict at 164–172.

## Protein family

FraD is the founding/reference member of a small, taxonomically restricted family:

- **InterPro IPR020360** — "Uncharacterised protein family alr2393". InterPro describes
  members as *"components of cyanobacterial septal junctions (microplasmodesmata) in
  heterocyst-forming cyanobacteria."* ~161 proteins across ~436 taxa (86 AlphaFold models).
- **Pfam PF17310** — "Family of unknown function (DUF5357)" (~161 proteins).
- **NCBIfam NF037953** — "septal junction protein FraD" (dedicated FraD HMM).
- **TCDB 1.V.1.1.1** — "the filamentous cyanobacterial septal pore (septum) family."

The family is confined to **filamentous, heterocyst-forming / multicellular cyanobacteria**
(Nostocales and relatives); there is no known homolog outside this lineage. FraD and its
partner **SepN co-occur** phylogenetically — SepN is essentially never found without FraD
[PMID:36470860 "SepN always co-occurs with FraD."]. The absence of the family from
unicellular cyanobacteria and all other bacteria is consistent with its dedicated role in
septal-junction-based multicellular cell-cell communication rather than a housekeeping
membrane function.

## GO annotation status
- GOA/QuickGO returns **no GO annotations** for P46079 (empty `FraD-goa.tsv`). This review
  is therefore de-novo; proposed core functions are recorded in `FraD-ai-review.yaml`.
- No dedicated GO cellular-component term exists for the bacterial **septal junction**
  (GO:0005918 "septate junction" is the arthropod epithelial junction, not this structure).
  Candidate for a new term — see `core_functions`/`proposed_new_terms`.

## Key references
- PMID:42424141 — Kieninger et al. 2026, *Cell Rep* — SepN–FraD structural module (source paper for this review).
- PMID:36470860 — Kieninger et al. 2022, *Nat Commun* — SepN identified as FraD-interacting SJ plug component.
- PMID:20487302 — Merino-Puerto et al. 2010, *Mol Microbiol* — Fra proteins; fraCDE operon; septal localization.
- PMID:7883709 — Bauer et al. 1995, *J Bacteriol* — original short-filament fraD mutant.
