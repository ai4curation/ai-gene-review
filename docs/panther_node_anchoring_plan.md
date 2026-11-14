# Plan: anchor PANTHER claims on tree nodes, and prepare for PANTHER 20

Status: proposed, 2026-11-14. Nothing here is implemented yet.

## Summary

PANTHER 20 is described in Mi et al., "PANTHER: the protein tree and function
resource in 2027", *Nucleic Acids Res* 2026, doi:10.1093/nar/gkag1150. Its family
and sequence classifications are already on the PANTHER FTP site. PAINT and the
tree API still serve version 19. When they switch, about a quarter of the
subfamily (SF) ids this repo cites will stop resolving or will carry a different
name. Tree-node (PTN) ids are designed to carry forward between releases, and
most do.

This plan does three things:

1. **Phase 0:** stop the pipeline from silently mixing PANTHER releases (now).
2. **Phase 1:** make PTNs, not SFs, the anchor for claims about where a function
   sits in a family, and convert existing SF anchors while version 19 is still
   live.
3. **Phase 2:** prepare a checked, member-based procedure for the switch to 20.

Phase 3 lists the new PANTHER 20 features worth using afterwards.

## Background: three PANTHER identifiers

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

## Convention to adopt

- **Claims about where a function sits, or which lineage has it:** anchor on a
  PTN, always stored with its family id (PTN ids are not family-unique in our
  PAINT slices; see Risks) and the PANTHER release it was checked against.
- **Claims about membership ("protein P is one of these"):** use the family id
  and `representative_members`. Only HMMs can classify a sequence from outside
  the reference genomes, and the member index is built from HMM classifications.
- **SF ids:** an optional, release-pinned, readable label beside a PTN. An SF is
  never the only anchor of a claim.
- **`representative_members` stay required beside a PTN.** They are how we
  detect that a surviving node now holds different genes.

## Phase 0: version guards (do now)

The repo pins `PANTHER_RELEASE = "19.0"` in `src/ai_gene_review/etl/panther_families.py`,
but other inputs follow whatever PANTHER serves today:

- `etl/panther_paint.py` downloads `IBD.gaf`, the leaf IBA GAF and the TreeGrafter
  node table from `paint/current/`.
- `etl/panther_trees.py` fetches trees from the live `treeinfo` API into
  `.cache/panther_trees/<FAM>.json.gz`, with no version in the path or the file.

Once PAINT moves to 20, a family review could combine a 19.0 member index, 20.0
PAINT nodes and a tree from either release.

| Item | Change | Done when |
|---|---|---|
| 0.1 | Use one release constant for all PANTHER inputs. Download PAINT from the numbered folder (`paint/19.0/` exists) instead of `paint/current/`. | `panther_paint.py` and `panther_families.py` read the same constant; a test asserts the PAINT URL contains it. |
| 0.2 | Key the tree cache by release: `.cache/panther_trees/<release>/<FAM>.json.gz`. Read the release from the response (`search.product.version`) and fail if it differs from the constant. | A doctest covers the mismatch; old unversioned cache files are ignored, not reused. |
| 0.3 | Keep more of each tree in the compact cache: internal-node `event_type` (speciation, duplication, horizontal transfer), `sf_id` and species label. `compact_tree` keeps only leaves' subfamilies today. | Phase 1.3 and the Phase 3 taxon checks can run from the cache alone. |
| 0.4 | Add a `panther_release` slot to `FamilyReview` (top level) and to module `FamilyDescriptor`. `paint_snapshot` records a PAINT row date, not which tree a `target_node_id` was checked against. | Schema updated; `just validate-families` and `just validate-modules` pass; existing files default to 19.0 through a one-off backfill. |
| 0.5 | Add a release-drift check: compare the constant with the `paint/current` README and tarball name and with `treeinfo`'s reported version, and warn when PANTHER has moved on. | Runs as an integration test, not in normal CI, because it needs the network. |

## Phase 1: PTN clade anchors in modules

Modules can cite PTNs today only through `FamilyDescriptor.ancestral_nodes`.
That slot means "the function arose at this node", and `validate_paint_ptns`
(`src/ai_gene_review/validation/module_validator.py`) rightly requires a positive
IBD there. A module that only wants to name a clade, such as "the plant CASPL4C
orthologs", has nowhere to put a PTN, so it uses an SF.

Current module anchors (`id:` occurrences under `modules/`): 1,771 SF, 1,567 family,
1,231 PTN. Family reviews already link SFs to PTNs through
`subfamilies[].clade_node_id` (253 uses).

| Item | Change | Done when |
|---|---|---|
| 1.1 | Schema: add `clade_nodes` to `FamilyDescriptor`, meaning "the clade rooted at this PTN is what this descriptor names". It makes no claim that a function arose there. Leave `ancestral_nodes` and its meaning unchanged. | Schema and docstrings explain the difference between the two slots. |
| 1.2 | Validator for `clade_nodes`: the node exists in the release-matched cached tree of the declared family, and the representative members are leaves below it (an error if none are, a warning if some are not). No IBD required. | Tests use real cached trees, not mocks. |
| 1.3 | Tool to map each SF to the PTN at its root, from version 19 trees: the lowest node whose leaves include every leaf carrying the SF, cross-checked against internal `sf_id` once 0.3 lands. An SF whose leaves do not form one clade is reported, not mapped. | Output goes to `.cache/` and is not committed; the tool reports how many SFs were mapped, how many were not one clade, and how many were missing. |
| 1.4 | Migration: for each SF anchor in `modules/`, add the root PTN as a `clade_nodes` entry and keep the SF as its readable label. For family reviews, fill `clade_node_id` on subfamilies that lack it. | Module and family validation pass; a short receipt in the PR gives counts and lists anchors that could not be mapped. |
| 1.5 | Guidance: update the PANTHER section of `CLAUDE.md`, the `module-curation` skill and the family-review docs to the convention above. | Reviewed and merged with 1.4. |

Do 1.3 and 1.4 before Phase 2. While 19 is live, every SF still resolves in its
own tree. After the switch, the same mapping needs member-based detective work.

## Phase 2: the switch to PANTHER 20

Start only when `paint/current` and `treeinfo` both report 20 (the 0.5 check).

| Item | Change | Done when |
|---|---|---|
| 2.1 | Bump the release constant; rebuild `interpro/panther/panther.obo` and the member index (`just refresh-panther-members --rebuild`); re-fetch PAINT slices and trees. | All caches carry 20.0 paths. |
| 2.2 | Re-check every cited PTN against the version 20 trees and sort them into: survives with the same representative members below it; survives with different members; gone. A gone node is re-located through its representative members (their lowest common ancestor in the new tree). It is never silently removed. | A report lists every PTN in each group, with proposed re-locations for review. |
| 2.3 | Remap SF ids through representative members to the version 20 SF, not by label. Bulk relabelling with `just fix-panther-labels` is not allowed for this step: some ids now name a different protein (for example `PTHR10133:SF27` changes from "DNA POLYMERASE NU" to "HELICASE AND POLYMERASE-CONTAINING PROTEIN TEBICHI"). | Validation passes; remaps are reviewed in a PR. |
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

- Removing SF ids wholesale. They remain useful labels.
- Changing what `ancestral_nodes` means, or relaxing its IBD requirement.
- Rewriting history records or old receipts.

## Risks and open questions

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
- **Open question:** the slot name `clade_nodes`, and whether `panther_release`
  belongs on each node or once per file.
- **Open question:** will PANTHER keep serving version 19 trees after the switch?
  `paint/19.0/` exists on the FTP site; no versioned tree endpoint is known.

## Appendix: measurements (2026-11-14)

All counts come from files on `data.pantherdb.org` and from this repo at commit
`984b61419e`. They are a snapshot, not maintained values. Phase 0 should add a
script that regenerates them.

**Release status.**

- `hmm_classifications/` and `sequence_classifications/` have a `20.0/` folder
  dated 2026-09-24; `current_release/` still holds 19.0.
- `paint/current/` holds `Pthr_GO_19.0.tsv.tar.gz`; its files are dated 2026-08-28,
  built from the GO release of 2026-08-05.
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
