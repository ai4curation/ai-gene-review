---
title: "Pfam entry reviews (proposed GO + verified rejections)"
---

# Pfam entry reviews — proposed GO where InterPro can't, with member verification

> Index of the curated **per-Pfam entry reviews** under `interpro/pfam/<PFAM>/<PFAM>-review.yaml` (schema: `src/ai_gene_review/schema/pfam_entry_review.yaml`). Each proposal is grounded in **characterized SwissProt members** and tested against **counter-examples**; a family whose own members are functionally heterogeneous is recorded as **REJECTED**. Validate with `just validate-pfam-reviews`. See [parent project](../PFAM.md).

## Proposed (5 families)

| Pfam | family | review | relation | proposed GO | aspect | conf. | example |
|---|---|---|---|---|---|---|---|
| PF02431 | Chalcone | [`PF02431-review.yaml`](../../interpro/pfam/PF02431/PF02431-review.yaml) | enables | GO:0045430 chalcone isomerase activity | MF | HIGH | UniProt:P41088 |
| PF07228 | SpoIIE | [`PF07228-review.yaml`](../../interpro/pfam/PF07228/PF07228-review.yaml) | involved in | GO:0030435 sporulation resulting in formation of a cellular spore | BP | HIGH | UniProt:P37475 |
| PF09043 | Lys-AminoMut_A | [`PF09043-review.yaml`](../../interpro/pfam/PF09043/PF09043-review.yaml) | enables | GO:0047826 D-lysine 5,6-aminomutase activity | MF | MEDIUM | UniProt:E3PRJ5 |
| PF16552 | OAM_alpha | [`PF16552-review.yaml`](../../interpro/pfam/PF16552/PF16552-review.yaml) | enables | GO:0047831 D-ornithine 4,5-aminomutase activity | MF | MEDIUM | UniProt:E3PY96 |
| PF27512 | LeuD | [`PF27512-review.yaml`](../../interpro/pfam/PF27512/PF27512-review.yaml) | enables | GO:0003861 3-isopropylmalate dehydratase activity | MF | HIGH | UniProt:P30126 |
| PF27512 | LeuD | [`PF27512-review.yaml`](../../interpro/pfam/PF27512/PF27512-review.yaml) | involved in | GO:0009098 L-leucine biosynthetic process | BP | HIGH | UniProt:P30126 |

## Rejected on member verification (4 families)

These families are named for a function but their reviewed members are functionally heterogeneous (counter-examples in the *same* family), so the term would over-annotate even at the Pfam level.

| Pfam | family | review | term that does NOT hold | why (same-family counter-example) |
|---|---|---|---|---|
| PF13360 | PQQ_2 | [`PF13360-review.yaml`](../../interpro/pfam/PF13360/PF13360-review.yaml) | GO:0043165 Gram-negative-bacterium-type cell outer membrane assembly | RQKA_DEIRA (DNA-damage-responsive Ser/Thr protein kinase RqkA) (2.7.11.1) |
| PF13561 | adh_short_C2 | [`PF13561-review.yaml`](../../interpro/pfam/PF13561/PF13561-review.yaml) | GO:0016631 enoyl-[acyl-carrier-protein] reductase [NAD(P)H] activity | FABG_ECOLI (3-oxoacyl-[acyl-carrier-protein] reductase FabG) (1.1.1.100) |
| PF14681 | UPRTase | [`PF14681-review.yaml`](../../interpro/pfam/PF14681/PF14681-review.yaml) | GO:0004845 uracil phosphoribosyltransferase activity | UCKL1_HUMAN (uridine-cytidine kinase-like 1) (2.7.1.48) |
| PF16363 | GDP_Man_Dehyd | [`PF16363-review.yaml`](../../interpro/pfam/PF16363/PF16363-review.yaml) | GO:0008446 GDP-mannose 4,6-dehydratase activity | GALE_HUMAN (UDP-glucose 4-epimerase) (5.1.3.2) |

