# sec11 review notes

## Research inputs

No generated `sec11-deep-research-*.md` file was present in the newly seeded
`genes/ASPFU/sec11/` directory. I did not create a provider-named stand-in.

Direct literature searches on 2026-10-21 for `AfSec1`, `AfSec11`,
`AFUA_3G12840`, `Afu3g12840`, and *Aspergillus fumigatus* signal peptidase
found one PubMed-indexed paper directly assaying this gene:

- PMID:36657388, Kim KH, Kang S, Seo H, Yun CW. 2022/2023. AfSec1 is a signal
  peptidase and removes signal peptides of 1,3-beta-glucanosyltransferases in
  *Aspergillus fumigatus*. The cached record is abstract-only
  (`full_text_available: false`).

The PubMed abstract reports that AfSec1, identified as 3g12840, was induced
during macrophage infection and that the authors constructed an AfSec1
promoter-deletion strain rather than a full deletion strain. Loss of detectable
AfSec1 expression caused accumulation of nonprocessed Gel1, while wild type and
the promoter-complemented strain had mature Gel1. The promoter mutant also had
increased caspofungin sensitivity, about 20% lower beta-glucan, and reduced
virulence in murine infection and human phagocyte assays.

## PAINT and family summary

`sec11`/Q4WYF4 is in PANTHER family `PTHR10806`, subfamily `PTHR10806:SF6`,
the fungal/canonical Sec11 subfamily.

The local `interpro/panther/PTHR10806/PTHR10806-paint.tsv` slice contains
three positive IBD rows:

- `PTN000086749`: `GO:0008233 peptidase activity`, placed at the PTHR10806
  root with no taxon restriction.
- `PTN000086750`: `GO:0005787 signal peptidase complex`, scoped to Eukaryota.
- `PTN000086750`: `GO:0051604 protein maturation`, scoped to Eukaryota.

These placements fit Sec11 inheritance, but the root-level peptidase term is
generic for a protein whose exact activity is signal peptidase activity.
`GO:0051604 protein maturation` correctly captures the eukaryotic Sec11 role in
converting signal-peptide-bearing secretory precursors into mature proteins.

## Annotation decisions

- Accepted the exact `GO:0009003 signal peptidase activity` rows, supported by
  direct A. fumigatus Gel1 processing evidence from PMID:36657388 and by
  fungal Sec11 homology.
- Accepted `GO:0005787 signal peptidase complex` and
  `GO:0005789 endoplasmic reticulum membrane`; these are exact conserved
  Sec11/SPC localization and complex annotations.
- Accepted the broader `GO:0005783 endoplasmic reticulum` row because it is
  still informative and compatible with the more precise ER membrane rows.
- Marked `GO:0008233 peptidase activity` and `GO:0016020 membrane`
  `TOO_GENERAL`; each is entailed by a more precise accepted term in this same
  review.
- Accepted `GO:0004252 serine-type endopeptidase activity` as the
  serine-protease chemistry claim complementary to `GO:0009003 signal
  peptidase activity`.
- Modified both `GO:0051604 protein maturation` rows to the live
  `GO:0016485 protein processing` process term for SPC-catalyzed signal
  peptide cleavage.
- Removed `GO:0045047 protein targeting to ER`. Sec11 removes a signal peptide
  after ER targeting/translocation; it does not execute the upstream
  signal-recognition targeting step.
