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

- [x] **PTHR10030, alpha-L-fucosidase family**
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
  - Module/GO-CAM split: no new ModuleReview or GO-CAM review was needed. The
    existing lysosomal glycoprotein-degradation module intentionally selects the
    FUCA1 subfamily, the mammalian L-fucose-degradation module explicitly
    excludes upstream free-fucose release by FUCA1/FUCA2, and `gocams/index.tsv`
    has no FUCA2 production model.

- [ ] **PTHR12604, Ku autoantigen DNA helicase family**
  - STATUS: in progress on XRCC5/XRCC6.
  - Seed: `XRCC5` / UniProtKB:P13010, reviewed Swiss-Prot, unreviewed locally,
    with 166 GOA rows in a compact two-member human PANTHER family.
  - Human family members in this checkout:
    - [x] `XRCC5` / UniProtKB:P13010: new DRAFT review.
    - [x] `XRCC6` / UniProtKB:P12956: new DRAFT review.
  - PANTHER: `interpro/panther/PTHR12604/PTHR12604-review.yaml` records five
    sound root IBD gains for the Ku70:Ku80 complex, double-stranded DNA binding,
    telomeric DNA binding, telomere maintenance and NHEJ, plus the off-human
    Drosophila IRDs that do not affect the reviewed human Ku70/Ku80 lineages.
  - Module/GO-CAM split: no new ModuleReview or GO-CAM review is needed. The
    existing `modules/nonhomologous_end_joining.yaml` review already models
    Ku70/Ku80 DNA-end binding as the first c-NHEJ step, and no human production
    GO-CAM in `gocams/index.tsv` covers the core Ku/DNA-PK/XRCC4-LIG4 machinery.

- [ ] Next human Swiss-Prot seed family
  - STATUS: queued after the PTHR12604 branch validates and is ready for PR.
  - NOTES: pick another small, biologically characterized, cached PANTHER family
    from the missing-accession table while this family PR waits for review.

# NOTES

## 2026-11-21

- Storage was already above the nominal campaign target at intake: visible
  `/srv/home/cmungall/orca/workspaces/ai-gene-review/*` directories occupied
  about 62 GB, and this checkout occupied about 7 GB. The worktree is a
  registered Orca worktree at
  `/srv/home/cmungall/orca/workspaces/ai-gene-review/aigr-ros-human-families`,
  with Git metadata in
  `/srv/home/cmungall/repos/ai-gene-review/.git/worktrees/aigr-ros-human-families`.
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
