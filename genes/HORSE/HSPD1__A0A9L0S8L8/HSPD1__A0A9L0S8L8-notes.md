# HSPD1 (horse, A0A9L0S8L8) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Scope: first review of A0A9L0S8L8, the canonical horse HSPD1 product (Ensembl ENSECAG00000008968, canonical transcript ENSECAT00000137290). All 63 GOA rows were reviewed. No ProtNLM2 file or prediction-evidence folder was opened.

Folder: `genes/HORSE/HSPD1__A0A9L0S8L8`, because `genes/HORSE/HSPD1` is keyed to the alternative gene model F6Z587. Fetched with `just fetch-gene HORSE A0A9L0S8L8 --alias HSPD1__A0A9L0S8L8`.

Deep research: `just deep-research-falcon HORSE HSPD1__A0A9L0S8L8 --fallback perplexity-lite` failed on 2026-10-20. Falcon returned "Edison API request failed: Failed to authenticate" (403 on /auth/login), and the perplexity-lite fallback also failed. No deep-research file exists. Sources used instead: the human HSPD1 review (`genes/human/HSPD1`), its falcon report, and cached primary papers.

### Evidence status in horse

- I found no experimental GO-relevant study of horse Hsp60. A web search turned up only expression studies: immunohistochemistry and western blots of HSP60 in stallion and cryptorchid testes, and seasonal/temperature-dependent HSP60 mRNA in stallion testis. These are expression observations, not functional assays, and support no GO annotation.
- All 63 GOA rows are electronic (IEA: InterPro2GO, ARBA, Ensembl Compara GO_REF:0000107, combined GO_REF:0000120) or IBA. Every functional claim is therefore inferred.

### Evolutionary grounding

- Gene model: A0A9L0S8L8 (587 aa) contains every human P10809 residue (559/573 identical), plus a 14-aa N-terminal extension MKAHLTKRNSASSE before the conserved MLRLP start [file:HORSE/HSPD1/HSPD1-bioinformatics/RESULTS-rereview.md "| A0A9L0S8L8 | 587 | 559/573 (97.6%) | none | 1-14 MKAHLTKRNSASSE |"]. This analysis was done in the F6Z587 re-review and is reused here, not rerun. The extension may reflect an upstream in-frame ATG chosen by the gene build; whether it is translated is untested.
- Family: PANTHER PTHR45633 (Cpn60/GroEL), TIGR02348 GroEL and HAMAP MF_00600 CH60. Ensembl Compara gives a 1:1 ortholog relationship to human P10809 (the source of the GO_REF:0000107 rows).
- PAINT nodes (from `interpro/panther/PTHR45633/PTHR45633-paint.tsv`). PTN000143677 carries protein folding, seeded by GroEL, M. tuberculosis GroEL1/2, yeast and human. PTN000143509 carries the mitochondrial matrix, inner membrane and protein-folding chaperone binding terms. PTN000143510 (Opisthokonta) carries UPRmt and IMS import. PTN002900230 (Euteleostomi, seeded by human, mouse and rat) carries the immune-regulation terms. PTN000888030 (rat seed) carries apoptotic mitochondrial changes. Horse is inside every one of these clades.
- PTN000143509 also has an IBD for GO:0007005 (mitochondrion organization, dated 2025-09-04). It is not yet in horse GOA, and I did not add it as NEW.

### Decisions

- Core (ACCEPT): ATP-dependent protein folding chaperone, protein folding (IEA and IBA), protein refolding, protein-folding chaperone binding (IEA and IBA), mitochondrial matrix (IEA and IBA), and ATP binding.
- MODIFY: mitochondrion → mitochondrial matrix; T cell activation (IBA) → positive regulation of T cell activation; positive regulation of cytokine production (ARBA) → positive regulation of IFN-alpha production. All three match the human review.
- REMOVE: chaperonin-containing T-complex (ARBA). CCT is the type II cytosolic chaperonin of a different family.
- MARK_AS_OVER_ANNOTATED: the endocytic compartments seen with exogenous Hsp60 (early endosome, clathrin-coated pit, coated vesicle); LPS receptor complex; protein-containing complex; and the immune effects that are likely LPS-driven (IL-6, IL-10, B cell proliferation and activation, macrophage activation, MyD88-dependent TLR signalling). IL-6 is also an IBA (PTN002900230); I kept it over-annotated because LPS-free Hsp60 does not induce IL-6 [PMID:18256040 "LPS-free Hsp60 did not induce IL-6, IL-12 or tumor necrosis factor alpha production in APC"].
- UNDECIDED: dsRNA binding, IgG isotype switching (both inherit the human UNDECIDED), and IMS protein import (yeast-only seed, no mammalian test).
- KEEP_AS_NON_CORE: the remaining moonlighting locations, binding activities, apoptosis-related terms, IFN and T cell costimulation terms, UPRmt, and inner membrane.
- No NEW annotations.

Actions follow the human HSPD1 review term by term. Horse adds no independent evidence, so these rows inherit the human judgement, and every transfer is flagged as "no experiment on horse Hsp60".
