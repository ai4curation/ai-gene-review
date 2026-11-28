# Nitrogen-regulatory PTS family consultation

Completed three new FamilyReviews, nine term assessments and four assessments of actual PAINT IBD assertions. All family names and declared subfamily labels match the materialized official panther.obo. No raw entries, metadata, PAINT slices, trees, genes, module, project records or earlier seals were edited.

## Scientific boundaries

| Family | Supported synthesis | Boundary |
|---|---|---|
| PTHR46244 | Shared PEP-to-protein phosphotransfer chemistry, GO:0008965; actual common-node gain SOUND | SF1 misses NA1000 PtsP, while SF6 includes both NA1000 PtsP and E. coli sugar-PTS PtsI. Chemistry does not establish native acceptor, transported sugar or GAF ligand. |
| PTHR33705 | Native characterized HPr/NPr proteins perform nitrogenous-acceptor phosphotransfer | SF2 includes B. subtilis sugar-PTS HPr as well as NPr. SF1 also includes an unassessed Dictyostelium HPr-domain protein. Broad activity/process grants remain UNRESOLVED; this preserves all positive native chemistry and avoids an unverified universal claim. |
| PTHR47738 | SF1 supports the molecular-function-regulator genus GO:0098772 as a conservative synthesis of native PtsN effectors | Parent family includes sugar EIIA proteins. SF1 does not imply universal kinase activation, a single phosphostate rule or conserved target. E. coli activation remains positive; KT2440/NA1000 kinase judgments remain unresolved. |

The proposed module can therefore omit exact PANTHER IDs for the role-specific PtsP/NPr descriptors while recording their verified broader classifications. PTHR47738:SF1 is defensible for terminal PtsN classification together with native partner/relay evidence and the common regulator genus. A broad family match alone is insufficient to admit any protein into a native nitrogen-regulatory route. No physical assembly, universal serial flux, cross-species partner interchange or obligatory chain under bypass conditions follows from these reviews.

## Actual PAINT and tree assessment

| Family | Node | Term | Snapshot | Verdict |
|---|---|---|---|---|
| PTHR46244 | PTN000532509 | GO:0008965 phosphoenolpyruvate-protein phosphotransferase activity | 20260530 | SOUND |
| PTHR46244 | PTN000532509 | GO:0015764 N-acetylglucosamine transport | 20240827 | UNRESOLVED |
| PTHR33705 | PTN002135312 | GO:0009401 phosphoenolpyruvate-dependent sugar phosphotransferase system | 20241008 | UNRESOLVED |
| PTHR47738 | PTN002021052 | GO:0030295 protein kinase activator activity | 20180524 | UNRESOLVED |

The actual PEP-enzyme node spans 43 reference leaves and has P08839/P37177 as activity seeds. Its N-acetylglucosamine process assertion is seeded by Q9HXN5; the seed's complete native transport context was not adjudicated and no loss or pruning branch is invented. The HPr sugar-process node spans 35 leaves, including E. coli NPr, B. subtilis HPr and Crh. The kinase-activation node spans 17 leaves and includes E. coli GatA as well as PtsN. E. coli PtsN is a genuine experimental seed, so the broad-node concern does not invalidate its own activation claim. The four ancestor-to-leaf lists and member/SF assignments were independently recomputed from the frozen raw gzip tree payloads and matched to the compact snapshots.

No missing KT2440 or NA1000 leaf was interpreted as evidence of absence or evolutionary loss. No SF-to-PTN clade equivalence, residue-site loss, new PAINT node, negative exception or inferred IRD was invented. UNRESOLVED means the broad node/function claim was investigated but remains unsettled; it is not a blanket negative or an instruction to reverse the completed gene judgments.

## Primary support and limits

PMID:10473571 reports: “EI(Ntr) phosphorylated NPr but not HPr, whereas Enzyme I exhibited a strong preference for HPr.” This purified E. coli specificity supports distinct native entry roles despite shared chemistry.

PMID:7876255 reports: “Purified IIANtr and NPr exchange phosphate appropriately with Enzyme I, HPr, and Enzyme IIA proteins of the phosphoenolpyruvate: sugar phosphotransferase system.” This is real cross-system biochemical exchange, not sufficient by itself to establish native coupled sugar transport; the E. coli NPr sugar IBA remains UNDECIDED.

PMID:18296519 establishes the principal native KT2440-derived PEP→PtsP→NPr→PtsN route and fructose-dependent FruB cross-talk. Native mutant/phosphostate evidence is not recast as isolated target kinetic measurements.

PMID:19400808 directly supports E. coli KdpD activation. PMID:26224366 supports target KT2440 PtsN–KdpD interaction and transporter-promoter repression but does not resolve kinase versus phosphatase modulation. PMID:21236318 supports native cellular/extract PDH inhibition; PMID:27109061 supports NA1000 phosphostate-dependent SpoT hydrolase regulation. These distinct native outputs justify a common regulator genus while withholding a universal kinase output. PMID:8596444 demonstrates the B. subtilis phosphoserine-HPr/CcpA transcriptional cofactor mechanism; it is not transferred to all NPr proteins.

## Verification

- Focused LinkML FamilyReview schema and GO term/label checks passed all three final documents.
- Production reference validation passed; the independent local check additionally verified all 49 quoted snippets, including raw local classification/PAINT snippets, and 14 cited PMID title occurrences.
- Targeted production PANTHER name/member and PAINT node checks: 33 PASS, no failures or unresolved membership. The small member lookup was assembled in memory from frozen entries and target UniProt DR records; no global member index or IBD download was built.
- Production family/gene cross-check functions consumed all 12 panel gene reviews and emitted zero findings. Their scope is exact-term consistency, not proof of every inferred ontology entailment; the native scientific comparisons are documented above.
- Three helper-generated codex histories passed HistoryRecord validation. History kind `other` with explicit family-review target paths is used because the helper/schema has no `family` target kind.
- Conformance recomputation, quote/title closure and all 79 protected input byte/mode checks passed. The helper passes Ruff after formatting; the initial style failure and subsequent successful receipt are both retained.
- No full corpus validation, global family-index build, rendering, git staging, commit or push was performed.

The flat source/input dependency map distinguishes the referenced underlying sources from the 12 gene reviews used solely as consistency-check inputs. Gene review YAMLs are never cited as biological support. Abstract-only primary statements are used within their reported scope; full native papers and frozen classification/tree sources are used where available.
