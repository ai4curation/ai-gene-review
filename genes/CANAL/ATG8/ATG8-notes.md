# CANAL ATG8 manual review notes

## 2026-10-21

Reviewed the seeded C. albicans SC5314 ATG8 rows for the PTHR10969 fungal PAINT
tranche. Deep-research providers were unavailable, so this file records the
manual literature pass instead of a generated `ATG8-deep-research-*.md`.

### Inputs checked

- `genes/CANAL/ATG8/ATG8-ai-review.yaml` contained twelve seeded rows: seven
  PTHR10969 IBAs, two UniProt SubCell IEAs, one CGD `molecular_function` ND
  placeholder, the UniProt EXP vacuolar-membrane row from PMID:31284951, and the
  CGD IGI unfolded-protein-response row from PMID:29544880.
- `interpro/panther/PTHR10969/PTHR10969-paint.tsv` contains the core eukaryotic
  ATG8/LC3/GABARAP node `PTN000103522` with autophagosome membrane,
  phosphatidylethanolamine binding, autophagosome assembly, mitophagy, cellular
  response to nitrogen starvation and autophagosome maturation; it also contains
  the fungal node `PTN000861115` for fungal-type vacuole membrane.
- `PMID:29544880` is abstract-only locally. The abstract explicitly reports that
  deleting both `SERP1/YSY6` and `ATG8` causes tunicamycin hypersensitivity,
  mitochondrial dysfunction and attenuated HAC1 splicing/UPR activation under ER
  stress, so the CGD IGI UPR row is retained as a non-core ATG8 role.
- `PMID:31284951` is abstract-only locally. The abstract reports GFP-Atg8
  transport/degradation assays in an `atg11` mutant under nitrogen starvation
  and hypha-inducing conditions, supporting the UniProt vacuolar-membrane
  localization context.
- `PMID:36328097` was added because UniProt cites it for C. albicans ATG8
  function and it postdates the seeded GOA literature. Its abstract reports that
  `atg8 ire1` double mutants are more sensitive to ER stress and have stronger
  UPR and ER-phagy/vacuolar-fusion defects than either single mutant.

### PubMed and Europe PMC 2024-2026 search

Searched PubMed and Europe PMC on 2026-10-21 for `Candida albicans` with
`ATG8` or `autophagy` in 2024-2026. The search returned a broad Candida
autophagy set dominated by transcriptional regulators, P-body/TORC1 regulators,
PP2A/TORC1 drug-resistance papers, and antifungal-perturbation studies that use
GFP-Atg8 processing, vacuolar GFP-Atg8, or ATG8 mRNA as autophagy readouts. The
most directly ATG8-relevant new hit was PMID:42361441, a 2026 Microbiol. Res.
paper reporting temperature-dependent effects on autophagic Erg11 degradation
with Atg8 redistribution under heat stress. None of the 2024-2026 abstracts or
open result snippets changed the conserved PTHR10969 curation decisions or
justified adding a new direct C. albicans ATG8 GO term.

### Curation decisions

- Accepted all PTN000103522 IBA rows. The node is a eukaryotic ancestral
  placement for the conserved Atg8/LC3/GABARAP lipidated ubiquitin-like
  modifier, and the Candida protein is a canonical fungal PTHR10969 member.
- Accepted the PTN000861115 fungal-type vacuole-membrane IBA. It is scoped to
  fungi and is concordant with UniProt's PMID:31284951-backed vacuole-membrane
  statement.
- Accepted both UniProt SubCell rows because they duplicate curated
  autophagosome/vacuole membrane locations rather than making unsupported
  transfers.
- Removed only the CGD `GO:0003674 molecular_function` ND row. The more
  informative PE-binding MF row supersedes this no-data placeholder.
- Kept `GO:0030968 endoplasmic reticulum unfolded protein response` as
  non-core. It has direct Candida double-mutant support, but it is a contextual
  ER-stress role rather than the conserved core ATG8 activity.
