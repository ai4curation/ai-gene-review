---
title: Human reviewed Swiss-Prot proteins without AI Gene Reviews
description: Family-by-family campaign over reviewed human Swiss-Prot proteins that still lack AI Gene Reviews.
species: [human]
index_group: MAMMAL
---

# Human Unreviewed Families

This project reviews human reviewed UniProtKB/Swiss-Prot proteins that still
lack `genes/human/<GENE>/<GENE>-ai-review.yaml` reviews, working family by
family so PAINT propagation and paralog-specific exceptions are checked at the
same time as individual GOA rows.

Initial survey on 2026-11-21 used the repo's UniProt/PANTHER/GOA-derived data
and existing human review files:

| Count | Meaning |
|---:|---|
| 20,429 | reviewed human Swiss-Prot proteins in the current UniProt stream |
| 3,796 | `genes/human/*/*-ai-review.yaml` files already present |
| 3,795 | existing human review accessions parsed from `id:` lines |
| 16,656 | reviewed human Swiss-Prot accessions with no matching review |
| 14,920 | missing accessions with a primary gene symbol, PANTHER family, GO xrefs, and no ORF-style seed symbol |

The seed triage prefers reviewed Swiss-Prot proteins that already have GOA rows
to audit, are assigned to a PANTHER family present in the local cache, and are
not uncharacterized ORFs. Large families are split by subfamily where the
PantherDB inventory gives usable subfamily assignments.

# STATUS

- [x] **PTHR10003, Cu/Zn superoxide dismutase / CCS family**
  - STATUS: merged in PR #6562.
  - Seed: `CCS` / UniProtKB:O14618, reviewed Swiss-Prot, unreviewed locally,
    with 36 GOA rows and an existing PANTHER review.
  - Human family members in this checkout:
    - [x] `SOD1` / UniProtKB:P00441: already COMPLETE; cross-checked as the
      family catalytic Cu/Zn SOD exemplar.
    - [x] `CCS` / UniProtKB:O14618: new COMPLETE review.
    - [x] `SOD3` / UniProtKB:P08294: new COMPLETE review.
  - PANTHER: `interpro/panther/PTHR10003/PTHR10003-review.yaml` records the
    CCS-specific PAINT `GO:0016532` node gain, anchors CCS exceptions to the
    existing `GO:0004784` superoxide dismutase activity IRD, and requests an
    ADD_IRD at the same CCS clade for `GO:0019430` removal of superoxide
    radicals.
  - Module/GO-CAM split: no new ModuleReview for this PTHR family; human CCS
    and SOD3 do not form a single multi-part module with SOD1. The existing
    `modules/glutathione_thioredoxin_redox_systems.yaml` module already has a
    Cu/Zn SOD family selector for SOD1-type enzymes. The small production SOD3
    GO-CAM `gomodel:69ea894900001492` now has a COMPLETE review and can ship
    with this family PR.

- [x] **PTHR10210, PRPP synthase / PRPS-associated protein family**
  - STATUS: merged in PR #6563.
  - Seed: `PRPSAP1` / UniProtKB:Q14558, reviewed Swiss-Prot, unreviewed
    locally, with GOA rows spanning the catalytic PRPP synthases and the
    non-catalytic PRPSAP paralogs.
  - Human family members reviewed in the family PR:
    - [x] `PRPS1` / UniProtKB:P60891: new COMPLETE review.
    - [x] `PRPS2` / UniProtKB:P11908: new COMPLETE review.
    - [x] `PRPS1L1` / UniProtKB:P21108: new COMPLETE review.
    - [x] `PRPSAP1` / UniProtKB:Q14558: new COMPLETE review.
    - [x] `PRPSAP2` / UniProtKB:O60256: new COMPLETE review.
  - PANTHER: `interpro/panther/PTHR10210/PTHR10210-review.yaml` records the
    catalytic root gains, the PRS2/PRPS2 complex-location loss, and the
    PRPSAP1/2 non-catalytic clade split.
  - Module/GO-CAM split: no module or GO-CAM change was needed for PRPS; the
    core family work was self-contained in gene and PANTHER reviews.

- [ ] **PTHR10030, alpha-L-fucosidase family**
  - STATUS: merged in PR #6567.
  - Seed: `FUCA2` / UniProtKB:Q9BTY2, reviewed Swiss-Prot, unreviewed locally,
    with 35 GOA rows and a compact PANTHER family containing one reviewed human
    paralog.
  - Human family members in this checkout:
    - [x] `FUCA1` / UniProtKB:P04066: already DRAFT; cross-checked as the
      lysosomal/tissue alpha-L-fucosidase exemplar.
    - [x] `FUCA2` / UniProtKB:Q9BTY2: new COMPLETE review.
  - PANTHER: `interpro/panther/PTHR10030/PTHR10030-review.yaml` now records the
    three sound root IBD gains for alpha-L-fucosidase activity, fucose
    metabolism and glycoside catabolism, plus the contradicted off-human
    Drosophila IRD.
  - Module/GO-CAM split: no new ModuleReview or GO-CAM review is needed. The
    existing lysosomal glycoprotein-degradation module intentionally selects the
    FUCA1 subfamily, the mammalian L-fucose-degradation module explicitly
    excludes upstream free-fucose release by FUCA1/FUCA2, and `gocams/index.tsv`
    has no FUCA2 production model.

- [ ] **PTHR10204, NQO1/NQO2 quinone reductase family**
  - STATUS: in review on PR #6570.
  - Seed: `NQO1` / UniProtKB:P15559, reviewed Swiss-Prot, unreviewed locally,
    with 44 GOA rows and a compact two-member human PANTHER family.
  - Human family members in this checkout:
    - [x] `NQO1` / UniProtKB:P15559: new COMPLETE review.
    - [x] `NQO2` / UniProtKB:P16083: already IN_PROGRESS; cross-checked as a
      diverged NRH-preferring quinone reductase that retains weak NADH turnover.
  - PANTHER: `interpro/panther/PTHR10204/PTHR10204-review.yaml` records the two
    sound root IBD gains and the NQO2 cofactor-preference shift; no NQO2 IRD is
    needed because `GO:0003955` remains measurable but secondary in NQO2.
  - Module/GO-CAM split: no new ModuleReview or GO-CAM review is needed. Human
    NQO1 and NQO2 are alternative quinone reductases rather than parts of a
    multi-protein mechanism, and `gocams/index.tsv` has no NQO1/NQO2 production
    model.

- [ ] Next human Swiss-Prot seed family
  - STATUS: queued after one of the two open family PRs is green.
  - NOTES: keep selecting small, biologically characterized, cached PANTHER
    families from the missing-accession table while the FUCA and NQO branches
    wait for review.

# NOTES

## 2026-11-21

- Storage was already above the nominal campaign target at intake: visible
  `/srv/home/cmungall/orca/workspaces/ai-gene-review/*` directories occupied
  about 62 GB, and this checkout occupied about 7 GB. The worktree is a
  registered Orca worktree at
  `/srv/home/cmungall/orca/workspaces/ai-gene-review/aigr-ros-human-families-3`,
  with Git metadata in
  `/srv/home/cmungall/repos/ai-gene-review/.git/worktrees/aigr-ros-human-families-3`.
- The CCS/SOD3 seed exposed a QuickGO fetch regression: requesting
  `includeFields=taxonName` could return empty result sets or time out. The local
  fetcher now omits that display-only field and backfills `TAXON NAME` from the
  stable `taxonId`; `just fetch-gene human CCS --force` then seeded 36 GOA
  annotations and `just fetch-gene human SOD3 --force` seeded 41 annotations.
- `PTHR10003` is a compact first family with one reviewed catalytic member
  (`SOD1`) and two missing reviews (`CCS`, `SOD3`). Its PAINT tree already has
  an IRD at `PTN008300250` removing `GO:0004784` from the CCS clade, which
  makes it a useful seed for checking a real family-level paralog exception
  rather than a one-gene review.
- CCS and SOD3 validate individually, the `gomodel:69ea894900001492` SOD3
  copper-delivery GO-CAM review validates with the production model's
  disconnected nuclear ATOX1 regulatory branch called out, and a full
  `just validate-families` pass leaves `PTHR10003` conflict-free against the
  reviewed gene corpus.
- `PTHR10210` split the PRPP synthase family into catalytic PRPS1/2/1L1
  reviews and non-catalytic PRPSAP1/2 reviews, with the PANTHER review
  documenting the PRPSAP activity losses. PR #6563 merged.
- `PTHR10030` was selected next as a two-human-member alpha-L-fucosidase family:
  FUCA1 is a lysosomal paralog with an existing local DRAFT, while FUCA2 lacked
  a review and exercises the same root alpha-L-fucosidase PAINT gains without
  requiring a family module or GO-CAM split. PR #6567 is open for review.
- `PTHR10204` was selected as a second compact human family: NQO1 lacked a
  review, NQO2 already documented the paralogous shift toward efficient
  NRH-dependent quinone reduction, and the family PAINT assertions are two
  simple root gains rather than an exception-heavy tree.
