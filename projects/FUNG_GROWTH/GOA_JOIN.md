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
substrate therefore sits on enzyme-activity terms. Adding a second tier of
substrate-specific activities gives 60 flagged rows on 29 gene products,
40 of them IEA. One pair holds a clear review candidate: two *C. albicans*
GH3 β-glucosidases carry an IEA `cellulose catabolic process` from a
UniPathway mapping. *S. cerevisiae* has no cellobiose-implying annotation at
all, which agrees with its plate. Three of the remaining flag sets come from
plates that disagree with a sister plate of the same polymer and should be
discounted. No annotation has been changed.

## Method

| Step | Script | Output |
|---|---|---|
| Map carbon sources to GO by label; resolve every id in OLS4 (exact label, current, right namespace) | `build_go_map.py` | `data/carbon_source_go_map.tsv`, `data/carbon_source_go_activity_map.tsv` |
| Query QuickGO for each species × term, taxon and term descendants included | `goa_join.py` | `data/goa_carbon_annotations.tsv` (1,865 rows) |
| Flag positive annotations wherever the species has a killer call on a plate the term speaks to | `goa_join.py` | `data/goa_killer_flags.tsv` (60 rows) |
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

**Taxa** come from the OX lines of the repo's own UniProt files. Five are
species-level (5270, 5076, 5061, 51453, 318829), so queries include
descendant taxa. *Penicillium rubens* Wisconsin 54-1255 has no GOA rows under
its own name; every row returned is for *P. chrysogenum* (5076).

## The four target pairs

| Species | Plate (rating/control) | Process tier | Activity tier | Reading |
|---|---|---|---|---|
| *S. cerevisiae* | cellobiose 2/2, no growth | none | none | GOA and plate agree: no cellobiose-implying annotation exists. |
| *C. albicans* | cellobiose 1/1, no growth | none | BGL22 and CAALFM_C301820WA: β-glucosidase (IEA EC:3.2.1.21, IBA), **cellulose catabolic process (IEA, UniPathway UPA00696, GO_REF:0000041)**; CAALFM_C505360CA: β-glucosidase (IBA) | **Review candidate.** The cellulose process row comes from a pathway mapping, not from anything known about *C. albicans*, and the plate shows no use of the pathway's end product. The β-glucosidase activities may be real on other β-glucosides; the plate cannot rule that out. |
| *S. pombe* | cellobiose 0/0, no growth | none | SPBC1683.04: β-glucosidase (IEA EC:3.2.1.21, IBA); adg3, psu1, SPBC2G2.17c: β-glucosidase (ISM, PomBase, SUN-family Pfam PF03856 / IPR005556) | Low priority. The SUN-family proteins act on the cell wall, so a no-growth plate says nothing about them. SPBC1683.04 (GH3) is the only row the plate bears on. |
| *U. maydis* | soluble starch 4/4, no growth | none | UMAG_02740: glucoamylase (IEA EC:3.2.1.3); UMAG_04064: glucoamylase (IEA, InterPro IPR000165/IPR008291) and starch binding (IEA, IPR008291) | Weak flag. *U. maydis* scores 4 on its no-carbon plate, the highest control among these species, so "no better than control" is a coarse call at that baseline. Check the growth curves and plate photos before acting. |

## Other flagged pairs

| Species | Killer plate | Sister plates | Flagged rows | Reading |
|---|---|---|---|---|
| *U. maydis* | cellobiose 4/4 | — | GH3 β-glucosidases UMAG_00446, UMAG_04032, UMAG_06075 (IEA EC + IBA) | Same high-baseline caveat as starch. |
| *U. maydis* | citrus pectin 4/4 | apple pectin 5/4 (weak) | UMAG_02510, UMAG_04708, UMAG_11322, UMAG_12233, pgu1 (13 rows, IEA and IBA) | Discount: the two pectin plates disagree. |
| *P. rubens* | birchwood xylan 0/0 | beechwood 5/0, oat spelt 5/0 (both growth) | 11 xylanases and xylosidases (21 IEA rows) | Discount: the strain grows on two other xylans, so this plate is an artefact or an entry error. |
| *S. cerevisiae* | apple pectin 1/2 | citrus pectin 4/2 (weak) | PGU1: polygalacturonase and pectin catabolic process (IDA, PMID:10650215, PMID:10028181; IBA; IEA) | Keep. Experimental, and the plates disagree. *S. cerevisiae* can depolymerise pectin with PGU1 without growing on the products, so enzyme activity and plate growth are separate claims. |

## What this says about the approach

- **Plate phenotypes meet GO mostly through MF terms.** For di- and
  polysaccharides, the process terms that would say "this organism uses X"
  are sparsely annotated in fungi. The signal is in hydrolase activities,
  which state what an enzyme does, not that the organism grows on the
  product. A no-growth plate is therefore rarely enough on its own to
  remove an activity annotation. It is most useful against *process* rows
  inferred from pathway or EC mappings, as in the *C. albicans* case.
- **Sister plates are a built-in control.** Three FUNG-GROWTH polymers come
  as two or three preparations (pectin ×2, xylan ×3). A killer call that a
  sister plate contradicts should not be used. `killer_phenotypes.py` could
  require agreement across sister plates before calling.
- **The control baseline limits sensitivity.** Yeast-like growers with a high
  no-carbon score (*U. maydis* 4, *S. cerevisiae* 2) have little room
  between "control" and "growth" on the 0–10 scale.

## Next

- Review the *C. albicans* BGL22 and CAALFM_C301820WA cellulose-catabolism
  IEA rows as gene reviews (candidate MARK_AS_OVER_ANNOTATED), after
  checking the literature on *C. albicans* cellobiose assimilation.
- Add a sister-plate agreement rule to the killer calls.
- Read the *U. maydis* growth curves (`data/fung_growth_ratings.tsv`) for
  starch, cellobiose and the pectins before treating those calls as real.
