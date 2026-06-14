# CASP-like (CASPL) family curation

Cross-cutting curation of the plant **CASP / CASP-like (CASPL)** membrane-scaffold family,
extending the *Populus trichocarpa* CASPL gene-review batch to its Arabidopsis orthologs,
the underlying PANTHER families, and a reproducible orthology analysis.

## Background

CASP / CASPL proteins are small, non-enzymatic, four-transmembrane-span (tetraspan)
plasma-membrane proteins related to the MARVEL-domain superfamily. The five bona fide CASPs
(CASP1–CASP5 in Arabidopsis) build the **Casparian strip** by recruiting the lignin-polymerization
machinery in the root endodermis ([PMID:21593871], [PMID:24920445]). The much larger **CASPL**
subfamily is mostly uncharacterized, but specific clades have defined functions (below).

## Components

### 1. Poplar CASPL reviews (20 genes)
The 20 reviewed *P. trichocarpa* CASPLs (`genes/POPTR/CASPL*`). All carry a single IEA
plasma-membrane annotation; five were enriched with characterized-ortholog context.

### 2. Arabidopsis ortholog curation (5 genes, real deep research)
Full reviews of the characterized Arabidopsis orthologs with **falcon** deep research
(`genes/ARATH/CASPL{1B1,1B2,1D1,1D2,4C1}`):

- **CASPL1B/1D** — expressed in suberized endodermis; interact with aquaporin **PIP2;1**;
  implicated in suberization / water-transport modulation ([PMID:30767240]).
- **CASPL4C1** — cold-inducible; negative regulator of growth/biomass/flowering; vascular role
  beyond the Casparian strip ([PMID:26399665]).

### 3. PANTHER families (2 reviewed)
- **PTHR33573** "Casparian Strip Membrane" — corrected the LLM description to separate the bona
  fide CASP1–5 clade from the dominant, uncharacterized CASPL subfamily.
- **PTHR36488** (InterPro **IPR044173**, "CASPL") — added a description for this divergent CASPL
  clade (the 1U + 1B/1D subgroups, including the aquaporin-interacting CASPL1B/1D members).

### 4. Bioinformatics — orthology validation
`projects/CASPL_FAMILY/bioinformatics/` — reproducible Biopython pairwise-identity / reciprocal-best-hit
analysis of all 20 poplar + 34 Arabidopsis CASPLs. Confirms that **every** poplar CASPL's best
Arabidopsis hit is in the **same Roppolo group**, validating group-level (not strict 1:1) functional
transfer. See `bioinformatics/RESULTS.md`.

## Scope notes

- **Peanut / watermelon have no reviewed (Swiss-Prot) CASPL entries** — the genome-wide peanut
  set ([PMID:39124195]) and watermelon ClCASPL ([PMID:26399665]) are TrEMBL only, so they cannot be
  curated to the repository's reviewed-entry standard. Rice (29) and maize (23) *do* have reviewed
  CASPL entries and are the curatable cross-species extension if desired.
