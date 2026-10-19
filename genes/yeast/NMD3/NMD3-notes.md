# NMD3 rereview notes

## IBA rereview

NMD3 has four PAINT IBA rows and all are well placed.

- `PANTHER:PTN000297338` carries `GO:0005634 nucleus` and `GO:0000055 ribosomal large subunit export from nucleus`; the PAINT cache places these on a eukaryotic NMD3 ancestral node with Arabidopsis, yeast, and/or human descendant evidence. This matches the core shuttling-export role: [PMID:11086007 "Nmd3p is a Crm1p-dependent adapter protein for nuclear export of the large ribosomal subunit"] and [PMID:11313466 "Nuclear export of 60s ribosomal subunits depends on Xpo1p and requires a nuclear export sequence-containing factor, Nmd3p"].
- `PANTHER:PTN000978434` carries `GO:0005737 cytoplasm` and `GO:0043023 ribosomal large subunit binding` across the NMD3 family. These are supported in yeast by fractionation and direct 60S binding evidence: [PMID:10022925 "Nmd3p fractionated as a cytoplasmic protein and sedimented in the position of free 60S subunits in sucrose gradients"] and [PMID:11105761 "The interaction was specific for 60S subunits; 40S subunits were not coimmunoprecipitated"].

These are positive-control IBAs: the PAINT family is a dedicated NMD3 family, the yeast protein sits in the NMD3 subfamily, and there is no evidence of yeast-specific loss, paralog confusion, or compartment mismatch.

## Generic protein-binding rows

The IntAct-derived `GO:0005515 protein binding` rows from Krogan 2006, Hackmann 2011, and Michaelis 2023 were legacy `MARK_AS_OVER_ANNOTATED` calls. They should be `REMOVE` under the current project policy because GO:0005515 is uninformative, and the useful biology is already captured by NMD3's specific large-ribosomal-subunit-binding and protein-macromolecule-adaptor activities.

## Newer literature

A search for 2024-2026 NMD3 yeast papers found recent 60S-biogenesis work upstream of Nmd3 loading and one direct 2025 preprint. Chitale et al. used an `RPL10/uL16` loop mutation and found that simultaneous `NMD3` and `TIF6` mutations bypass a late cytoplasmic maturation arrest, allowing defective ribosomes into the translational pool [PMID:41279726 "simultaneous mutations in the late biogenesis factors Nmd3 and Tif6 bypass this block"]. This is consistent with the established Nmd3/Tif6 late-maturation checkpoint role, but it is a bioRxiv preprint and does not change any GO decisions here.

## 2026-10-01 current GOA refresh

`just fetch-gene yeast NMD3 --force` refreshed NMD3 from 19 to 20 live GOA rows.
The four PTHR12746 IBA rows remain positive-control transfers on
`PANTHER:PTN000297338` and `PANTHER:PTN000978434`; current PAINT drops the older
Arabidopsis donor from some `WITH/FROM` columns but leaves the target in the same
well-supported ancestral NMD3 clade.

Two exact historical source rows are no longer live in current GOA and were
kept with `retired: true`: the broad UniProt keyword `GO:0015031 protein
transport` row and the Krogan 2006 `GO:0005515 protein binding` row. Three
new IntAct `GO:0005515` rows now assert Tif6 binding from PMID:18467557,
PMID:27251291, and PMID:37968396; all three were reviewed as `REMOVE` because
the interaction records are generic and Nmd3's informative molecular functions
are already captured by 60S-ribosomal-subunit binding and
protein-macromolecule adaptor activity.
