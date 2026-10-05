# ARMC3 review notes

## Affinage gate
- The affinage record tripped the BLOCKING "possible symbol collision" gate because its narrative opens with yeast Vac8.
- I inspected it (`--out` to scratch): it is about ARMC3, but most findings are yeast Vac8 biology, via the "mouse ARMC3 is the homolog of Vac8" claim (PMID:34428398). I wrote it with `--force` and marked it LOW_QUALITY in reference_review.
- PANTHER places ARMC3 in PTHR46618 and yeast Vac8 (P39968) in PTHR47249, so the Vac8 findings were not transferred.

## Sources
- PMID:34428398 (Dev Cell, abstract only): Armc3-null mice are infertile, with blocked spermatid ribophagy.
- PMID:39221575 (abstract): human homozygous splice variant causes asthenozoospermia.
- PMID:26923438 (full text): bovine ARMC3 frameshift with tail-stump sperm defect.
- Mouse Armc3 (A2AU72) donor rows in QuickGO: IMP for ribophagy, spermatid development and sperm motility (PMID:34428398).

## Decisions
- Ribophagy (ISS) → ACCEPT, core.
- Spermatid development (ISS), sperm motility (ISS) and extracellular exosome (HDA) → KEEP_AS_NON_CORE.
- No NEW: the mouse PI3K-CI binding is abstract-only and by analogy to Vac8.
