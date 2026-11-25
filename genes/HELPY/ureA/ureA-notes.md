# ureA (P14916, H. pylori 26695) - curation notes

Deep research: `just deep-research HELPY ureG --provider perplexity` was attempted once
(2026-10-23) and failed - the installed providers are `falcon` and `openscientist` only
("Provider 'perplexity' not available"). No `-deep-research-*.md` file was generated; notes
below are from the cached publications, UniProt and PubMed lookups.

## Subunit nomenclature (the thing to get right first)

H. pylori urease has **two** chains, not three. `ureA` is a natural fusion of the gamma and
beta subunits of canonical bacterial ureases, and `ureB` is the catalytic alpha subunit
(equivalent to UreC elsewhere) [PMID:22013070 "the ureA gene encodes the β and γ subunits as
a fusion protein, and the ureB gene encodes the α subunit"]. UniProt's own DE lines call
P14916 "Urease subunit alpha" and P69996 "Urease subunit beta", with a CAUTION noting the
orthologous protein is the gamma/beta subunit (UreAB) in most other bacteria. Reviews must
follow the biology, not the DE line: the dinickel active site is on UreB.

## Evidence used

- Dodecameric structure: ((UreA-UreB)3)4, 1.1 MDa, active down to pH 3
  [PMID:11373617 "We have determined the crystal structure of H. pylori urease, which has a
  1.1 MDa spherical assembly of 12 catalytic units with an outer diameter of approximately
  160 A."].
- UreA+UreB alone give an assembled but inactive apoenzyme - assembly is accessory-protein
  independent, activation is not [PMID:1612735 "Clones containing only ureA and ureB also
  produced an assembled but inactive enzyme."]. This underpins the structural-molecule
  reading of UreA and the MODIFY on accessory-protein "complex assembly" terms elsewhere in
  this module.
- ureA is required for urease activity in the E. coli reconstitution [PMID:1313413 "Of the
  nine urease genes identified, ureA, ureB, ureF, ureG, and ureH were shown to be required
  for urease expression in E. coli"], which is also the source of the UniProt disruption
  phenotype.

## Decisions

- `GO:0009039 urease activity` (IBA + IEA, both `enables`): MARK_AS_OVER_ANNOTATED. The PAINT
  node PTN002129956 covers single-chain ureases where the alpha region is in the same
  polypeptide; here it is not. Expressed in `core_functions` as
  `GO:0005198` structural molecule activity + `contributes_to` `GO:0009039`, mirroring
  genes/PSEPK/ureA and genes/PSEPK/ureB.
- `GO:0016151 nickel cation binding`: REMOVE. Nickel ligands and the carbamylated Lys219 are
  on UreB; no metal-binding feature in the P14916 record.
- Two bare `GO:0005515` rows: REMOVE per the protein-binding policy (the UreA-UreB contact is
  recorded instead as `GO:0035550` membership).
- `GO:0005198` added as NEW (IDA, PMID:11373617).
