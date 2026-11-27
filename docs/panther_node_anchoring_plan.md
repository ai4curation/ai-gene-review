# Plan: anchor PANTHER claims on tree nodes, and prepare for PANTHER 20

Status: Phase 0 done (2026-11-15); Phase 1 reduced to guidance; Phase 2 has its dry-run
report (`just panther-release-diff`); Phase 3 not started. The decisions below keep churn to curated files minimal: no schema changes,
and no edits to existing modules or reviews until PANTHER 20 forces them.

## Summary

PANTHER 20 is described in Mi et al., "PANTHER: the protein tree and function
resource in 2027", *Nucleic Acids Res* 2026, doi:10.1093/nar/gkag1150. Its family
and sequence classifications are already on the PANTHER FTP site. PAINT and the
tree API still serve version 19. When they switch, about a quarter of the
subfamily (SF) ids this repo cites will stop resolving or will carry a different
name. Tree-node (PTN) ids are designed to carry forward between releases, and
most do.

This plan does three things:

1. **Phase 0 (done):** stop the pipeline from silently mixing PANTHER releases.
2. **Phase 1:** prefer PTNs over SFs for new claims about where a function sits.
   Existing SF anchors stay as they are.
3. **Phase 2:** at the switch to 20, remap through representative members and edit
   only the files whose ids actually changed.

Phase 3 lists the new PANTHER 20 features worth using afterwards.

## Background: PANTHER identifiers

| Identifier | Example | What it names | Stable across releases? | Has a name? |
|---|---|---|---|---|
| Family | `PTHR11801` | A family of homologous genes, with its own HMM | Mostly (0.5% of human proteins change family, 19 to 20) | Yes |
| Subfamily (SF) | `PTHR11801:SF12` | A named group of sequences inside a family, with its own HMM; roughly one ortholog group | No (see measurements) | Yes |
| Tree node (PTN) | `PTN000927860` | One node of the family's gene tree: a speciation, duplication or horizontal-transfer node, or a leaf | By design; 81–96% carried forward between releases | No |
| Annotation node (AN) | `PTHR11801:AN12` | The same node, numbered within one release only | No | No |

PAINT annotates PTNs: every IBD, IRD and IKR row is about a PTN, and every IBA
names its source PTN in WITH/FROM. Each SF is rooted at one node of the tree, so
every SF corresponds to a PTN, but most PTNs are not SF roots. A PAINT
annotation can sit above or below SF level. We store PTNs and never ANs; the
`PAINT_TreeGrafter_Annotations_TOTAL` file maps one to the other.

## Convention

- **Claims about where a function sits, or which lineage has it:** anchor on a
  PTN, stored with its family id (PTN ids are not family-unique in our PAINT
  slices; see Risks). Node assessments and `ancestral_nodes` already do this.
- **Claims about membership ("protein P is one of these"):** use the family id
  and `representative_members`. Only HMMs can classify a sequence from outside
  the reference genomes, and the member index is built from HMM classifications.
- **SF ids:** a release-specific, readable label. Existing SF anchors stay; new
  work should not make an SF the only anchor of a placement claim.
- **`representative_members` stay required beside a PTN.** They are how we
  detect that a surviving node now holds different genes.

## Decisions (2026-11-15)

- **No mass migration.** The 1,771 SF anchors in modules stay as they are. Waiting
  loses nothing: the version 19 subfamily-to-node mapping can be rebuilt later from
  files PANTHER keeps per release (see Phase 1).
- **No `panther_release` slot.** The pinned constants in code are the single record
  of which release the repo is checked against. Every file is re-validated at a bump,
  so a per-file release would add backfill churn without adding a check.
- **No `clade_nodes` slot yet.** It will be added only when a module needs a clade
  that is not a subfamily root and has no PAINT annotation.

## Phase 0: version guards (done)

Before this phase, the repo pinned `PANTHER_RELEASE = "19.0"` for the family and
member data, but read PAINT from `paint/current/` and trees from the live API into
an unversioned cache. Once PAINT moved to 20, a family review could have combined a
19.0 member index, 20.0 PAINT nodes and a tree from either release.

| Item | Change | Status |
|---|---|---|
| 0.1 | PAINT is read from `paint/<PANTHER_RELEASE>/<PAINT_SNAPSHOT>/` (both constants in `src/ai_gene_review/etl/panther_families.py`). The PAINT URLs are defined once. | Done |
| 0.2 | PAINT downloads are cached in a `paint-<release>-<snapshot>/` folder under the existing cache roots (`paint_cache_dir`), so a bump never reuses older files. | Done |
| 0.3 | Trees are cached under `.cache/panther_trees/<release>/`. A tree the API serves for another release is refused: `load_family` returns `None` and the checks report "not checked". | Done |
| 0.4 | `just check-panther-release` compares the pins with PANTHER's FTP site and API. It exits 1 on a newer PAINT snapshot or when PAINT or the API serve another release, and reports newer library releases as notices. It is a command, not a test, because integration tests replay recorded responses and cannot see drift. | Done |
| — | Keep internal-node event type, subfamily and taxon in the compact tree cache. | Dropped for now; add with the first check that needs it (Phase 3) |

First run (2026-11-15): "PANTHER 20.0 family classifications are published; PAINT
and the tree API may not serve it yet". No stale pins.

## Phase 1: prefer PTNs for new claims

Modules can cite PTNs today only through `FamilyDescriptor.ancestral_nodes`. That
slot means "the function arose at this node", and `validate_paint_ptns`
(`src/ai_gene_review/validation/module_validator.py`) requires a positive IBD
there. Family reviews already link subfamilies to PTNs through
`subfamilies[].clade_node_id` (253 uses). Current module anchors (`id:`
occurrences under `modules/`): 1,771 SF, 1,567 family, 1,231 PTN.

| Item | Change | Status |
|---|---|---|
| 1.1 | Guidance: one line in the PANTHER section of `CLAUDE.md`. | Done |
| 1.2 | `clade_nodes` slot on `FamilyDescriptor`, meaning "the clade rooted at this PTN", with no claim that a function arose there. Validated against the release-matched tree: the node is in the declared family and the representative members are below it. No IBD needed. | Deferred until a module needs it |
| 1.3 | Tool mapping each SF to the PTN at its root. | Deferred; only needed if anchors are converted |

If 1.3 is ever needed after the switch, the version 19 mapping can be rebuilt from
files PANTHER keeps per release (releases back to 14.1 are still on the FTP site):

- `downloads/paint/19.0/<date>/PAINT_TreeGrafter_Annotations_TOTAL.txt.gz` maps every
  tree node (AN number) to its PTN;
- `downloads/TreeGrafter/PANTHER19.0_data_trees_hmms_only.tar.gz` (3.1 GB) has the tree
  topology, with AN numbers;
- `sequence_classifications/19.0/` gives each leaf's subfamily, so an SF's root is the
  lowest node above all of its leaves.

## Phase 2: the switch to PANTHER 20

Start when `just check-panther-release` reports that PAINT and the API serve 20.

**Dry run, available now.** `just panther-release-diff 20.0` writes
`reports/panther-release-diff-19.0-to-20.0.yaml` (git-ignored) and edits nothing. It
lists:

- every family or subfamily id cited in modules and family reviews that is gone or
  renamed, with how far the name moved;
- every anchor with representative members (module family descriptors and
  family-review subfamilies) whose members fall into a different id in the target
  release, with a proposed id when they agree. A member row that records only a bare
  family never yields a proposal to coarsen a subfamily anchor. Anchors whose members
  were already split or unclassified in 19.0 are counted but not listed, since the bump
  did not cause them;
- every quote of `interpro/panther/panther.obo` that verifies today but would fail once
  that committed artifact is rebuilt for the target release.

Two kinds of file are not scanned for ids, on purpose:

- **Rule reviews** (`rules/`) cite PANTHER ids inside `rule.condition_sets`, a verbatim
  transcription of the published ARBA or UniRule rule. Rewriting them would falsify the
  receipt; they change only when the rule is re-fetched after UniProt updates it.
- **Gene reviews** mention subfamilies in prose and quote UniProt's `DR PANTHER` lines,
  which move on UniProt's schedule, not with this repository's pinned release.

On 2026-11-17 it found:

- 6,086 cited ids: 334 gone, 262 renamed to a divergent name, 139 partially renamed,
  388 cosmetically renamed, and 2 in neither release.
- 5,416 anchors: 495 with a proposed remap, 220 newly split across ids, 6 no longer
  classified; 688 have members outside the classified organisms in both releases.
- 514 files hold a listed anchor, and 535 cite an id that is gone or substantively
  renamed. The two sets overlap.
- 10 quotes of `panther.obo`, in 10 files (7 family reviews, 3 gene reviews), would
  break when it is rebuilt. The other ~700 citations of `panther.obo` are
  `references:` entries with no quoted text, which a rebuild cannot break. Quotes of
  `-entries.csv` files are InterPro snapshots that change only when a family is
  re-fetched, not at the bump.

**No mega-migration PR.** About 500 files change, so the switch is split:

1. A transition PR (before the switch, or with it) lets validators accept an id that is
   valid in the previous release but changed in the new one, as a warning carrying the
   report's proposal, instead of an error. It is switched on by setting
   `PANTHER_PREVIOUS_RELEASE` in `etl/panther_families.py`.
   - **Family reviews: done.** `check_panther_ids` reports such ids, labels and
     memberships as UNRESOLVED. In a simulated bump to 20.0 over all family reviews
     (PANTHER checks only, 2026-11-17), total failures go from 67 today to 2,400 without
     the allowance (2,333 new: 547 ids, 1,182 labels, 604 memberships) and stay at 67
     with it. Those 67 are the same set as today's except for one swap: a new, real
     failure (P0ABZ4, first classified in 20.0, sits outside its declared subfamily,
     which the bump did not change) and one existing failure that 20.0 resolves.
     Release-independent scope errors (a family id in a subfamily slot, another
     family's subfamily) still fail during the window. The previous release is read
     from the cache only; `just ensure-panther-members` fills it while a switch is on,
     and without it the allowance is off with a warning.
   - **Modules: done.** PANTHER terms whose label matches the previous release are
     set aside with a warning before OAK term validation
     (`defer_previous_release_panther_terms`), and `validate_family_members` treats a
     family that matched the members in the previous release as a warning. In a
     simulated bump over all modules (2026-11-17), term errors go from 2 today to 463
     without it and stay at 2 with it; membership errors go from 55 to 56 without it
     and stay at 55 with it.
   - **Labels are not laundered.** In both halves an id is deferred only while it
     carries the previous release's name; a label wrong in both releases fails. During
     the window `just fix-panther-labels` holds back, rather than rewrites, any label on
     an id whose name changed between the releases, even with `--allow-divergent`,
     because the id may now name something else. Those go through the remap batches.
     The hold-back reads the previous release's names from the cache, so with a cold
     cache (the switch on but its names file absent, or no member index for the
     grounding guard) `fix-panther-labels --apply` refuses to run rather than
     relabel unguarded; a dry run reports the same and continues. With a partial
     index, a descriptor none of whose representative members has been looked up
     yet is skipped and listed, like a disputed one, until the index is refreshed.
     One that no member can ever confirm (its members were all looked up and have no
     PANTHER family, or it names no UniProtKB member) is relabelled, since no refresh
     will change that, but listed for a check by hand.
2. The bump PR changes the pinned constants, rebuilds the caches and `panther.obo`
   (2.1), and re-quotes the `panther.obo` quotes the report lists (10 today), so
   `just validate-quotes` stays green. That is too few to need a transition allowance
   in the quote check.
3. Remap PRs follow in batches of about 50 files each, one directory at a time
   (modules, then family reviews), each regenerated from the report and checked by a
   curator.
4. A final PR removes the transition allowance.

| Item | Change | Done when |
|---|---|---|
| 2.1 | Bump `PANTHER_RELEASE` and `PAINT_SNAPSHOT` together; rebuild `interpro/panther/panther.obo` and the member index (`just refresh-panther-members --rebuild`); re-fetch PAINT slices and trees. | All caches carry 20.0 paths. |
| 2.2 | Re-check every cited PTN against the version 20 trees and sort them into: survives with the same representative members below it; survives with different members; gone. A gone node is re-located through its representative members (their lowest common ancestor in the new tree). It is never silently removed. | A report lists every PTN in each group, with proposed re-locations for review. |
| 2.3 | Remap SF ids through representative members to the version 20 SF (`just panther-release-diff 20.0`), not by label, and edit only files whose cited ids are gone or renamed. Bulk relabelling with `just fix-panther-labels` is not allowed for this step: some ids now name a different protein (for example `PTHR10133:SF27` changes from "DNA POLYMERASE NU" to "HELICASE AND POLYMERASE-CONTAINING PROTEIN TEBICHI"). | Validation passes; remaps are reviewed in a PR. |
| 2.4 | Re-check the reviewed human genes whose family changes (17; listed in the appendix) and the families they appear in. | Each one has a family review and module check. |
| 2.5 | Expect IBA rows to turn into TreeGrafter IEA rows (GO_REF:0000118) for species dropped from PANTHER 20. In this repo that is `genes/PHAVU/LBA` and `genes/SOLTU/{CCOAOMT,JOKA2,PATB1}`. Re-review them after the next `just fetch-gene`. Poplar stays in PANTHER, so the CASPL project is unaffected. | Reviews updated after the GOA refresh. |
| 2.6 | Re-check the open upstream discrepancies in `projects/PANTHER_FAMILY_ASSIGNMENT_DISCREPANCIES.md` and the DNAH12 case in `projects/IBA_REVIEW.md`. Both are unchanged in the 20.0 classification files, so the upstream reports still stand. | Pages updated with the version 20 status. |

## Phase 3: PANTHER 20 features worth using afterwards

- **Species tree via the API**, with NCBI taxon ids. This is the most useful one
  for PAINT reviews: it would let a validator check `node_taxon`,
  `target_node_taxon` and "placed too deep" verdicts mechanically (for example,
  the JAK-STAT annotation at the Unikonts node in PTHR11801).
- **Expanded PAINT coverage.** PANTHER finished a first pass of every family with
  at least one experimental annotation (about 11,500). Gene coverage rose about
  90% for bacteria and archaea, 60% for plants and 20% for vertebrates. The new,
  mostly plant and prokaryote node annotations are the least checked and are good
  family-review targets. They could be found from IBD dates.
- **Rebuild the human no-IBA list** for `projects/PAINT.md` from current GOA.
  Separate genes in the roughly 3,500 families with no experimental annotation
  (nothing for PAINT to build on) from families that are annotated but lack an
  IBD for one aspect.
- **Benchmark.** Feuermann et al. 2025 (*Nature* 640:146–154,
  doi:10.1038/s41586-025-08592-0) puts PAINT accuracy at 90–97%. This is a
  comparator for the failure rates in `projects/IBA_REVIEW.md`. It is not cached
  in `publications/` yet.
- **Citable example.** Figure 1 of the PANTHER paper shows a molecular function
  placed at the opisthokont ancestor (delta7-sterol 5(6)-desaturase activity)
  while the processes sit on separate branches (cholesterol biosynthesis in
  animals, ergosterol biosynthesis in fungi). This supports the "placed too deep"
  reasoning for processes in `projects/IBA_REVIEW.md`.
- **TreeGrafter in InterProScan** (`-goterms`) can place any sequence on a PANTHER
  tree: corrected gene models, RefSeq-only isoforms, species outside PANTHER. A
  local install with PANTHER data is large compared with the campaign storage
  budget. Whether the output names the grafted node has not been checked.

## Non-goals

- Removing or converting existing SF ids.
- Changing what `ancestral_nodes` means, or relaxing its IBD requirement.
- Rewriting history records or old receipts.

## Risks

- **PTN ids are not family-unique in our PAINT slices.** 283 of 6,094 nodes appear
  under more than one family (`family_residue_validator.py`). This is why every PTN
  is stored with its family id.
- **A surviving PTN can change content.** Genomes added or dropped between
  releases change what lies below a node. `representative_members` are the check.
- **Duplication and horizontal-transfer nodes carry forward least** (85% and 81%
  between 17 and 19, Table 2 of the paper). Proposed IBD moves usually point at
  them.
- **pantherdb.org is now behind Cloudflare.** On 2026-11-14 `treeinfo` returned 200,
  but the OpenAPI spec page returned 403. Prefer `data.pantherdb.org` downloads,
  cache trees, and rate-limit API calls.
- **The API will probably stop serving version 19 trees at the switch.** No
  versioned tree endpoint is known. Trees already cached under `19.0/` stay usable,
  and the per-release FTP archives listed in Phase 1 remain.

## Appendix: measurements (2026-11-14)

All counts come from files on `data.pantherdb.org` and from this repo at commit
`984b61419e`. They are a snapshot, not maintained values.

**Release status.**

- `hmm_classifications/` and `sequence_classifications/` have a `20.0/` folder
  dated 2026-09-24; `current_release/` still holds 19.0.
- `paint/current/` holds `Pthr_GO_19.0.tsv.tar.gz`; its files are dated 2026-08-28,
  built from the GO release of 2026-08-05, and match `paint/19.0/2026-08-28/`.
- `treeinfo` reports `version: 19`; `supportedgenomes` lists 144 genomes. The paper
  gives 131 for version 20.

**Identifier churn, 19.0 to 20.0** (HMM classification files).

- Families: 15,683 to 15,790; 39 removed, 146 new. The paper's own counts (15,795
  families, 85 new) use a different basis.
- Subfamilies: 128,012 to 117,735; 33,240 removed, 22,963 new, and 29,211 kept with
  a new name. Some renames are cosmetic ("SYNAPTOTAGMIN-7" to "SYNAPTOTAGMIN 7,
  ISOFORM A"); some name a different protein.

| SF ids cited in | Unique ids | Gone in 20 | Renamed in 20 |
|---|---|---|---|
| `interpro/panther/` (family reviews) | 3,239 | 286 (9%) | 587 (18%) |
| `modules/` | 1,555 | 87 (6%) | 308 (20%) |
| `rules/` | 133 | 8 (6%) | 31 (23%) |

Family ids cited in family reviews and modules: 2,111 unique; 1 retired
(`PTHR44170`, the DCC family) and 11 renamed. PTN ids cited: 2,973 unique;
`target_node_id` is used 6 times.

**Sequence classification churn** (proteins present in both releases).

| Organism | Family changed | Subfamily changed, same family |
|---|---|---|
| Human | 99 (0.5%) | 1,439 (7.4%) |
| Mouse | 15 (0.1%) | 1,899 (9.1%) |
| *C. elegans* | 3 (0.0%) | 3,396 (23.9%) |

Reviewed human genes (3,651 review files): 17 change family, 342 change subfamily
only, 7 are newly classified and 7 are no longer classified. The 17 family
changes: AASDH, ANKRD11, ANKRD34A, ANKRD34B, ARID2, BRD4, CACNA1G, DCC, DNAJC7, DYSF,
LEMD2, NTN1, NTN3, RFWD3, SCN1A, SCN9A, USH2A.

**Genome set.** PANTHER 20 drops 13 plant genomes: Amborella, banana, bean, bell
pepper, canola, cucumber, eelgrass, flooded gum, millet, orange, potato, spikemoss
and yellow monkey flower. It adds a charophyte green alga. The *Ustilago* and
*Cryptococcus* files appear to be renamed ("corn_smut", "encapsulated_yeast")
rather than dropped; this has not been checked against their contents.

**Tree-node stability** (paper, Table 2, nodes carried forward from 17 to 19 with
constrained alignments): speciation 95.9%, leaf 94.1%, duplication 85.4%,
horizontal transfer 80.9%.
