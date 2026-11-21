---
title: Human reviewed Swiss-Prot proteins without AI Gene Reviews
species: [human]
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
| 3,790 | `genes/human/*/*-ai-review.yaml` files already present |
| 3,789 | existing human review accessions parsed from `id:` lines |
| 16,661 | reviewed human Swiss-Prot accessions with no matching review |
| 14,920 | missing accessions with a primary gene symbol, PANTHER family, GO xrefs, and no ORF-style seed symbol |

The seed triage prefers reviewed Swiss-Prot proteins that already have GOA rows
to audit, are assigned to a PANTHER family present in the local cache, and are
not uncharacterized ORFs. Large families are split by subfamily where the
PantherDB inventory gives usable subfamily assignments.

# STATUS

- [x] **PTHR10003, Cu/Zn superoxide dismutase / CCS family**
  - STATUS: validated; ready for the first family PR.
  - Seed: `CCS` / UniProtKB:O14618, reviewed Swiss-Prot, unreviewed locally,
    with 36 GOA rows and an existing PANTHER review.
  - Human family members in this checkout:
    - [x] `SOD1` / UniProtKB:P00441: already COMPLETE; cross-checked as the
      family catalytic Cu/Zn SOD exemplar.
    - [x] `CCS` / UniProtKB:O14618: new COMPLETE review.
    - [x] `SOD3` / UniProtKB:P08294: new COMPLETE review.
  - PANTHER: `interpro/panther/PTHR10003/PTHR10003-review.yaml` now records the
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

- [ ] Next human Swiss-Prot seed family
  - STATUS: queued after the PTHR10003 branch validates and is ready for PR.
  - NOTES: pick another small, biologically characterized, cached PANTHER family
    from the missing-accession table rather than opening a second branch before
    the first has a clean validation baseline.

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
