---
title: "FUNG-GROWTH killer calls joined to GOA"
autolink_gene_symbols: false
---

# FUNG-GROWTH killer calls joined to GOA

[Back to the project page](../FUNG_GROWTH.md)

**Bottom line:** we joined the FUNG-GROWTH plate calls for the 11 species
reviewed in this repository to their GOA annotations. The four pairs we set
out to check were cellobiose in *S. pombe*, *S. cerevisiae* and
*C. albicans*, and starch in *U. maydis*. The GO process terms for these
substrates are barely used. `cellobiose catabolic process` (GO:2000892) has
no annotation in any of the 11 species, and `starch catabolic process`
(GO:0005983) has none in *U. maydis*. Any claim that these fungi use the
substrate therefore sits on enzyme-activity terms. With a second tier of
substrate-specific activities, and with killer calls that a sister plate of
the same polymer contradicts removed, 21 rows on 12 gene products are
flagged, 11 of them IEA. One pair held a clear error: two *C. albicans* GH3
β-glucosidases carried an IEA `cellulose catabolic process` from a
UniPathway mapping. Both genes now have reviews that remove that row and keep
the β-glucosidase activity. *S. cerevisiae* has no cellobiose-implying
annotation at all, which agrees with its plate.

## Method

| Step | Script | Output |
|---|---|---|
| Map carbon sources to GO by label; resolve every id in OLS4 (exact label, current, right namespace) | `build_go_map.py` | `data/carbon_source_go_map.tsv`, `data/carbon_source_go_activity_map.tsv` |
| Query QuickGO for each species × term, taxon and term descendants included | `goa_join.py` | `data/goa_carbon_annotations.tsv` (1,865 rows) |
| Flag positive annotations wherever the species has a killer call on a plate the term speaks to | `goa_join.py` | `data/goa_killer_flags.tsv` (21 rows) |
| Species × term summary with evidence-class counts | `goa_join.py` | `data/goa_species_process.tsv` |

**Process tier.** 25 of the 35 plates map to a catabolic process; 16
distinct GO terms. Crude biomass (brans, pulps, alfalfa meal) and casein have
no single process and are left unmapped. Arabic gum and arabinogalactan are
unmapped because GO has no arabinogalactan catabolic process term (checked in
OLS4; GO has only plant AGP metabolism terms).

**Activity tier.** 13 terms for the substrates with killer calls in these
species: cellobiose, starch, pectin and xylan. Term scope matters here.
`beta-glucosidase activity` (GO:0008422) has 20 descendants, most acting on
other substrates. These include the cell-wall 1,3- and 1,6-β-glucanases
(GO:0042973, GO:0004338, GO:0046557) and steryl-β-glucosidase (GO:0050295).
It is therefore queried as the exact term only, alongside its
cellobiose-specific children `cellobiose glucosidase activity` (GO:0080079)
and `glucan 1,4-beta-glucosidase activity` (GO:0031217).

**Killer calls** come from `killer_phenotypes.py` with the sister-plate
rule: a no-growth call on one preparation of pectin (apple, citrus) or xylan
(beechwood, birchwood, oat spelt) is kept only if every other preparation
scored for that strain is also no growth. The rule rejects 36 of the 299
earlier calls (`data/killer_rejected_sister.tsv`), leaving 263 in 139
strains.

**Taxa** come from the OX lines of the repo's own UniProt files. Five are
species-level (5270, 5076, 5061, 51453, 318829), so queries include
descendant taxa. *Penicillium rubens* Wisconsin 54-1255 has no GOA rows under
its own name; every row returned is for *P. chrysogenum* (5076).

## The four target pairs

| Species | Plate (rating/control) | Process tier | Activity tier | Reading |
|---|---|---|---|---|
| *S. cerevisiae* | cellobiose 2/2, no growth | none | none | GOA and plate agree: no cellobiose-implying annotation exists. |
| *C. albicans* | cellobiose 1/1, no growth | none | BGL22 and CAALFM_C301820WA: β-glucosidase (IEA EC:3.2.1.21, IBA), **cellulose catabolic process (IEA, UniPathway UPA00696, GO_REF:0000041)**; CAALFM_C505360CA: β-glucosidase (IBA) | **Reviewed: cellulose row removed** (details below). The β-glucosidase activities are kept; the plate cannot rule them out on other β-glucosides. |
| *S. pombe* | cellobiose 0/0, no growth | none | SPBC1683.04: β-glucosidase (IEA EC:3.2.1.21, IBA); adg3, psu1, SPBC2G2.17c: β-glucosidase (ISM, PomBase, SUN-family Pfam PF03856 / IPR005556) | Low priority. The SUN-family proteins act on the cell wall, so a no-growth plate says nothing about them. SPBC1683.04 (GH3) is the only row the plate bears on. |
| *U. maydis* | soluble starch 4/4, no growth | none | UMAG_02740: glucoamylase (IEA EC:3.2.1.3); UMAG_04064: glucoamylase (IEA, InterPro IPR000165/IPR008291) and starch binding (IEA, IPR008291) | Weak flag. *U. maydis* scores 4 on its no-carbon plate, the highest control among these species, so "no better than control" is a coarse call at that baseline. Check the growth curves and plate photos before acting. |

## *C. albicans* reviews

Candida albicans SC5314 scores 1 on cellobiose and 1 on crystalline cellulose, the same as its no-carbon control plate.
Candida albicans has no GOA annotation to cellulase activity (GO:0008810), and its only annotations to cellulose catabolic process (GO:0030245) are the two UniPathway rows on BGL22 and CAALFM_C301820WA.
The plate agrees with an independent survey of 215 typical *C. albicans*
strains, none of which assimilated cellobiose or the β-glucoside salicin
(PMID:7007420).

New reviews `genes/CANAL/BGL22` and `genes/CANAL/CAALFM_C301820WA` (status
DRAFT) act on all seven GOA rows of each gene:

| Annotation | Evidence | Action |
|---|---|---|
| cellulose catabolic process (GO:0030245) | IEA, UniPathway UPA00696 | REMOVE: over-propagated pathway mapping; the organism has no cellulose breakdown |
| beta-glucosidase activity (GO:0008422) | IBA and IEA (EC:3.2.1.21) | ACCEPT: GH3 active-site signature present; describes the enzyme, not growth on cellobiose |
| glucan catabolic process (GO:0009251) | IBA | KEEP_AS_NON_CORE: compatible, substrate unknown |
| hydrolase activity, hydrolyzing O-glycosyl compounds; carbohydrate metabolic process | IEA, InterPro | KEEP_AS_NON_CORE: correct, general |
| cellular_component | ND | ACCEPT |

BGL22 has a predicted signal peptide, which makes a secreted β-glucosidase
in a yeast that cannot use cellobiose an open question; the reviews record it
as one.

## Calls removed by the sister-plate rule

These pairs were flagged before the rule and are no longer:

| Species | Former killer plate | Sister plates | Rows no longer flagged |
|---|---|---|---|
| *U. maydis* | citrus pectin 4/4 | apple pectin 5/4 (weak) | UMAG_02510, UMAG_04708, UMAG_11322, UMAG_12233, pgu1 (13 rows, IEA and IBA) |
| *P. rubens* | birchwood xylan 0/0 | beechwood 5/0, oat spelt 5/0 (both growth) | 11 xylanases and xylosidases (21 IEA rows) |
| *S. cerevisiae* | apple pectin 1/2 | citrus pectin 4/2 (weak) | PGU1 polygalacturonase and pectin catabolic process (IDA, IBA, IEA) |
| *S. pombe* | apple pectin 0/0 | citrus pectin 4/0 (growth) | none (no pectin annotations) |

*U. maydis* cellobiose (4/4) stays flagged: GH3 β-glucosidases UMAG_00446,
UMAG_04032 and UMAG_06075 (IEA EC and IBA), with the same high-baseline
caveat as starch.

## What this says about the approach

- **Plate phenotypes meet GO mostly through MF terms.** For di- and
  polysaccharides, the process terms that would say "this organism uses X"
  are sparsely annotated in fungi. The signal is in hydrolase activities,
  which state what an enzyme does, not that the organism grows on the
  product. A no-growth plate is therefore rarely enough on its own to
  remove an activity annotation. It is most useful against *process* rows
  inferred from pathway or EC mappings, as in the *C. albicans* case.
- **Sister plates are a built-in control.** Two FUNG-GROWTH polymers come
  as two or three preparations (pectin ×2, xylan ×3). `killer_phenotypes.py`
  now requires agreement across them, which removed 36 calls and every
  flag set we had discounted by hand.
- **The control baseline limits sensitivity.** Yeast-like growers with a high
  no-carbon score (*U. maydis* 4, *S. cerevisiae* 2) have little room
  between "control" and "growth" on the 0–10 scale.

## Next

- Read the *U. maydis* growth curves (`data/fung_growth_ratings.tsv`) for
  starch and cellobiose before treating those calls as real.
- Consider whether the *S. pombe* GH3 protein SPBC1683.04 warrants the same
  review as the *C. albicans* pair; it carries no cellulose process row, so
  the case is weaker.
