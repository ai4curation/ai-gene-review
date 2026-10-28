# Icam1 (rat) review notes

## Setup
- `just fetch-gene rat Icam1` resolved Q00238 (ICAM1_RAT, RGD:2857, GeneID 25464); GOA has
  88 rows, all keyed to Q00238. First attempt hit a UniProt 429; retry succeeded.
- Publications cached via `just fetch-gene-pmids`; additionally cached PMID:3349522
  (Staunton 1988, ICAM-1 primary structure, LFA-1 ligand) and PMID:1675157 (Diamond 1991,
  Mac-1 binds Ig domain 3).
- No deep-research provider available; see `Icam1-deep-research-manual.md`.

## Key reading
- PMID:17662049 (full text): rat brain endothelial RBE4 cells; ICAM-1 antibody cross-linking
  induces stress fibres via RhoA and cortactin tyrosine phosphorylation by Src; SHP-2 is
  required; PECAM-1 engagement reverses this [PMID:17662049 "ICAM-1 cross-linking induced the
  formation of numerous actin stress fibers across RBE4 cells"]. Supports the IDA
  "positive regulation of actin filament polymerization" as an outside-in signalling
  role (kept non-core).
- PMID:10556544: rat LFA-1 binds immobilised rat ICAM-1 in a cell-free assay; the RGD IPI
  row "protein-containing complex binding" with Itgal/Itgb2 is better expressed as
  integrin binding.
- PMID:10201790: anti-ICAM-1 *reduced* pancreatitis-associated gut endothelial barrier
  dysfunction, i.e. ICAM-1 contributes to barrier loss in that model; the IMP row
  "establishment of endothelial intestinal barrier" appears to have the wrong direction.
  Flag for expert.

## Decisions summary
- Core: integrin (LFA-1/Mac-1) counter-receptor at the plasma membrane mediating
  leukocyte adhesion to endothelium and leukocyte cell-cell adhesion (immunological synapse).
- IEP "response to X" rows (expression changes): MARK_AS_OVER_ANNOTATED.
- Antibody-blockade rows describing downstream consequences of leukocyte recruitment
  (vasoconstriction, NO biosynthesis, NF-kB, calcium transport): MARK_AS_OVER_ANNOTATED.
- Generic cell adhesion / cell-cell adhesion / membrane / protein-containing complex binding:
  MODIFY to the specific terms already carried.
