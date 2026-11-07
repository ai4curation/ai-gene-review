# MnmA preflight — 2026-11-07

The reusable boundary should cover bacterial **MnmA-dependent C2 thiolation of tRNA U34**, retaining the existing Tus relay as one implementation and adding evidence-qualified direct-donor alternatives. Keep sulfur mobilization and terminal ATP-dependent thiolation as separate substantive roles. The Bacillus pair is strongly supported by native conditional genetics plus purified chemistry and heterologous rescue. The Thermus pairings establish biochemical capacity; native donor choice remains unresolved.

## Pinned baseline and live overlaps

Local `origin/main` and GitHub main both resolve to `bb89a377830600d2850d64215e0da94a47a06c6a`. The current DRAFT module is explicitly Tus-dependent/Gammaproteobacterial; preserve its five role steps within the broader route. Its SHA256 is `fb25ca211bab9caa5df89108f79e91e7f8e227b5c7d6d86d2b868e8185bca887`.

Seven current KT2440 reviews have 32 ordered rows, including four historical/active NEW proposals. Six are DRAFT; IscS is COMPLETE. Reusable ECOLI/iscS adds 41 rows and is COMPLETE. `final-baseline.json` hashes 103 relevant main files, including old histories, family/raw/provider files and referenced normal publication caches. It records exact review counts and family presence. These are an immutable baseline, not authorization to reset source files to main. The working root has unrelated existing changes, which this consultation did not edit.

Two complete scans of all 282 open PR file lists found the same overlaps (`final-open-pr-files.json`, `final-overlap.json`):

- [PR5077](https://github.com/ai4curation/ai-gene-review/pull/5077), head `1d49413be24fee4ced690c3d0ee6504894964d39`: existing PTHR11601 review only. Its replacement is a generic PAINT-derived review with SF34 localization grants that do not distinguish bacterial/eukaryotic members. Preserve the richer current-main review and latest Isc evidence; do not import this older replacement wholesale.
- [PR5078](https://github.com/ai4curation/ai-gene-review/pull/5078), head `4477f7e8948736e948949285b68a94d347e2d9af`: PTHR34874, PTHR37010, PTHR37526 and PTHR38780 reviews, all absent as reviews on main. These are coordination inputs, not already accepted judgments. Exact PR files and API metadata are saved.

No module, existing target gene, proposed new gene or PTHR43586 overlap was found. This is a dated live-head result, not a guarantee against later PR changes. `overlap.json` is the initial narrower scan; **final-overlap.json supersedes it**, covering absent family reviews and new candidate paths too.

## Exact proposed new reviews

| Organism | Symbol/folder | Accession | Strain / locus |
|---|---|---|---|
| ECOLI | tusA | P0A890 | K-12, b3470 |
| ECOLI | tusB | P45530 | K-12, b3343 |
| ECOLI | tusC | P45531 | K-12, b3344 |
| ECOLI | tusD | P45532 | K-12, b3345 |
| ECOLI | tusE | P0AB18 | K-12, b0969 |
| ECOLI | mnmA | P25745 | K-12, b1133 |
| BACSU | iscS1 | O34599 | 168, BSU27510; primary alias yrvO |
| BACSU | mnmA | O35020 | 168, BSU27500 |
| THET2 | mnmA | Q72GX1 | HB27, TT_C1727 |
| THET2 | TT_C0087 | Q72LH2 | HB27; primary name IscS |
| THET2 | TT_C1373 | Q72HV9 | HB27; primary name SufS |

Reuse ECOLI/iscS P0A6B7 and all seven PSEPK reviews. This yields 19 potential reviewed representatives across four strain panels/three major bacterial lineages. It does not imply four equivalently demonstrated native flux panels. KT2440 remains ortholog/locus-supported; E. coli is the canonical experimental relay; Bacillus PS832 is explicitly a 168 derivative; Thermus is a purified-capacity panel. Current official UniProt records, taxonomy, sequences and classifications are in `candidate-identities.json` with source hashes. The HB8 MnmA Q5SLN5 is a comparator, **not a substitute for assayed HB27 Q72GX1**.

The Thermus bridge is explicit: 31801798 clones HB27 TT_C1727 and cites 16547008 for IscS/SufS purification. The indexed publisher methods of 16547008 specify HB27 and cloned donor loci TTC0087/TTC1373; official UniProt maps these to the two HB27 accessions above. That earlier paper's U54 results must not be relabeled as MnmA U34 assays.

## Classification versus function

| Role | Verified classification | Boundary |
|---|---|---|
| E. coli/PSEPK IscS, Bacillus YrvO, Thermus IscS | PTHR11601:SF34 | Common cysteine-desulfurase chemistry does not license every sulfur acceptor or universal Fe-S assembly. Reassess the current SF34-wide Fe-S grant in light of dedicated YrvO; absence of heterologous rescue is not a native loss proof. |
| Thermus SufS | PTHR43586:SF8 | Official SF name is **CYSTEINE DESULFURASE 1, CHLOROPLASTIC**, despite verified bacterial membership. New family/raw acquisition is needed; do not guess a different family to repair the name. |
| MnmA | PTHR11933:SF5 | All three bacterial experimental MnmAs and human TRMU O75648 share SF5. Official SF name is **MITOCHONDRIAL TRNA-SPECIFIC 2-THIOURIDYLASE 1**; parent misleadingly says methyltransferase. Identity is verified, but donor, compartment and cofactor regime are not universal. |
| TusA | PTHR33279:SF2 | Exact ECOLI/PSEPK classification; carrier family identity alone does not specify U34 versus another sulfur pathway. |
| TusD | PTHR34874:SF3 | Exact ECOLI/PSEPK classification. PR5078 places the U34/complex/carrier terms on the TusD descendant; future review must inspect actual tree rather than treat parent YchN as all TusD. |
| TusE | PTHR37010:SF1 | Exact ECOLI/PSEPK classification; preserve positive carrier role, inspect phylogenetic scope before universal grants. |
| TusB / TusC | PTHR37526:SF1 / PTHR38780:SF1 | Structural complex participants; do not assign autonomous covalent sulfur-carrier chemistry merely from pathway membership. |

Current main has a review only for PTHR11601 among these eight families. Seven original target-family raw sets exist; PTHR33279 lacks a PAINT slice. PTHR43586 is wholly absent. No new PTN placement or family-wide verdict was fabricated in preflight.

## Mechanistic decisions for the eventual module

- Retain the canonical IscS→TusA→TusBCD→TusE→MnmA route. Two-enzyme E. coli reconstitution is a biochemical boundary control, not proof that its native Tus relay is dispensable.
- Add the cognate Bacillus YrvO/MnmA route. Both proteins are needed in the published heterologous complementation; common family IDs cannot prove cross-species compatibility. The tested single-replacement failures should constrain those cases, not every conceivable engineered condition.
- Add qualified Thermus IscS/MnmA and SufS/MnmA biochemical alternatives. The 2020 paper removes reductants before the cysteine-fed donor assay. It explicitly allows unidentified native carriers; do not assert which donor dominates in vivo.
- ATP/Mg-dependent substrate activation and an appropriate U34 tRNA are enabling conditions. PLP is the donor-enzyme cofactor. C-type Thermus MnmA requires a reconstituted [4Fe-4S] cluster in the demonstrated assay. The D-type E. coli Fe-S requirement is disputed by full 2021 and 2024 primary results; keep that uncertainty explicit rather than impose universal presence/absence. The 2021 correction changes author names only.
- Keep U34/C2 separate from ThiI-U8, TtcA-C32 and TtuA-U54. Do not convert PP-loop or broad sulfur-enzyme membership into exact substrate-position activity. Current QuickGO definitions were captured independently.
- Correct the inherited MnmC “downstream” wording: C5 elaboration is a distinct branch, not a universally subsequent prerequisite or product step of C2 thiolation. It remains outside this module.
- The new PDB9HLV lead cites a paper “To be published.” It cannot settle the disputed native D-type mechanism or justify another full native panel by itself.

`source-ledger.json` gives genuine review/primary distinctions, access status, assay context, short verified excerpts and limits. Some original Tus primary full texts remain inaccessible; this is disclosed rather than converted into evidence of error. No genes, families, module, project, normal publications, or frozen Mla artifacts were edited. No worktree, staging, commit, push or PR action was performed.

## Rechecking the frozen handoff

Run `uv run python .cache/module-audit-logs/mnma-preflight-20261107/verify.py` from the root checkout. It reads pinned Git objects, official response snapshots and the frozen manifest without rewriting any artifact. Root working copies may lag origin/main; verification does not confuse those copies with the pinned baseline. Acquisition/build scripts describe provenance and are not freeze-safe rerun commands. No full-corpus or curation validation was required for this read-only preflight.
