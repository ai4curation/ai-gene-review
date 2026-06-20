---
title: "Proposed Pfam → GO Annotations (entry-centric reviews)"
---

# Proposed Pfam → GO Annotations — where an InterPro mapping is not viable

> Index of the curated **per-Pfam entry reviews** under `interpro/pfam/<PFAM>/<PFAM>-review.yaml` (schema: `src/ai_gene_review/schema/pfam_entry_review.yaml`). Seeded + structurally verified by `seed_pfam_reviews.py` (GO id non-obsolete; Pfam membership; parent entry heterogeneous; parent entry carries no equivalent term). Each proposed annotation is a **candidate needing curator / experimental validation**. See [parent project](../PFAM.md).

**11 proposed annotations** across **9 Pfam families**. Each Pfam is curated as its own entry (with parent-entry + sibling context, per-term relation/aspect/evidence/confidence/status) rather than as a flat mapping row.

| Pfam | family | review file | relation | proposed GO | aspect | conf. |
|---|---|---|---|---|---|---|
| PF14681 | UPRTase | [`PF14681-review.yaml`](../../interpro/pfam/PF14681/PF14681-review.yaml) | enables | GO:0004845 uracil phosphoribosyltransferase activity | MF | HIGH |
|  |  |  | involved in | GO:0044206 UMP salvage | BP | HIGH |
| PF16363 | GDP_Man_Dehyd | [`PF16363-review.yaml`](../../interpro/pfam/PF16363/PF16363-review.yaml) | enables | GO:0008446 GDP-mannose 4,6-dehydratase activity | MF | HIGH |
| PF09043 | Lys-AminoMut_A | [`PF09043-review.yaml`](../../interpro/pfam/PF09043/PF09043-review.yaml) | enables | GO:0047826 D-lysine 5,6-aminomutase activity | MF | HIGH |
| PF16552 | OAM_alpha | [`PF16552-review.yaml`](../../interpro/pfam/PF16552/PF16552-review.yaml) | enables | GO:0047831 D-ornithine 4,5-aminomutase activity | MF | HIGH |
| PF27512 | LeuD | [`PF27512-review.yaml`](../../interpro/pfam/PF27512/PF27512-review.yaml) | enables | GO:0003861 3-isopropylmalate dehydratase activity | MF | HIGH |
|  |  |  | involved in | GO:0009098 L-leucine biosynthetic process | BP | HIGH |
| PF02431 | Chalcone | [`PF02431-review.yaml`](../../interpro/pfam/PF02431/PF02431-review.yaml) | enables | GO:0045430 chalcone isomerase activity | MF | HIGH |
| PF13360 | PQQ_2 | [`PF13360-review.yaml`](../../interpro/pfam/PF13360/PF13360-review.yaml) | involved in | GO:0043165 Gram-negative-bacterium-type cell outer membrane assembly | BP | HIGH |
| PF07228 | SpoIIE | [`PF07228-review.yaml`](../../interpro/pfam/PF07228/PF07228-review.yaml) | involved in | GO:0030435 sporulation resulting in formation of a cellular spore | BP | MEDIUM |
| PF13561 | adh_short_C2 | [`PF13561-review.yaml`](../../interpro/pfam/PF13561/PF13561-review.yaml) | enables | GO:0016631 enoyl-[acyl-carrier-protein] reductase [NAD(P)H] activity | MF | MEDIUM |

Each review records: parent InterPro entry (id/type/#members), `interpro_go_status`, `interpro_mapping_viability` + reason, the lumped sibling families, and the proposed annotations. Validate all with `just validate-pfam-reviews`.

