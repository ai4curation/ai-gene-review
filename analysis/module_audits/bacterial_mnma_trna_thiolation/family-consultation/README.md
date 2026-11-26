# MnmA family consultation

Eight family reviews distinguish evolutionary classification from exact substrate, sulfur acceptor, cofactor and cognate-partner requirements. All 19 panel accessions have the expected official classifications; these do not alone establish a complete native sulfur-delivery route. No gene, module or project was edited by this consultation.

## Decisions

| Family | Classification and functional boundary |
|---|---|
| PTHR11601 | Preserve the current Isc6175 review, its five PAINT node assessments and all unrelated judgments. Qualify only the universal SF34 iron–sulfur assembly grant as UNRESOLVED: SF34 also contains dedicated Bacillus YrvO/IscS1. This is not a claim that YrvO cannot support any secondary Fe–S chemistry. |
| PTHR11933 | The main MnmA/MTU1 clade is SF5; the actual tree also has eight SF6 leaves outside it. Broad sulfur transfer and U34 modification fit SF5. Exact modified-uridine substrate, compartment, complex membership and Fe–S requirement do not have universal scope. Preserve all eight PAINT assertion payloads, including the tick IRD; its molecular-loss interpretation remains unresolved. |
| PTHR33279 | TusA SF2 identifies the two bacterial panel members. YedF and archaeal alternatives prevent a universal MnmA-delivery grant. Normal PAINT acquisition resolved 96 nodes but returned no assertions; none were invented. |
| PTHR34874 | Preserve valid PR5078 TusD SF3 scope and all original node judgments. The family also contains YchN SF1. Cys78-dependent sulfur carriage belongs to TusD, not automatically to the structurally related proteins. |
| PTHR37010 | Preserve TusE carrier/U34 family scope and the PR5078 node judgment. This does not universalize the complete E. coli Tus relay or establish an identical terminal-persulfide mechanism in every organism. |
| PTHR37526 / PTHR38780 | Preserve the TusB/TusC complex and U34 process grants and PR5078 node judgments. These subunits contribute to the delivery assembly; they are not independently assigned TusD's covalent carrier chemistry. |
| PTHR43586 | Preserve the newly fetched genuine root IBD. Its universal cysteine-desulfurase interpretation is UNRESOLVED because the family includes positively characterized EgtE and SepCysS chemistry. EgtE shares SF8 with Thermus SufS. Alternate activities do not prove absence of secondary desulfurase activity or justify an invented loss node. |

The PR5078 source bytes remain in the unchanged preflight archive. All ten imported node identities, seeds, dates, taxa, judgments and original supporting evidence are preserved; added evidence and prose replace donor-count arguments. The older PR5077 Isc review was not substituted for current main.

## Evidence and access

The source ledger below states the level actually used. All quoted occurrences are checked against immutable source bytes by `verify.py`. Official tree/MSA response bodies are gzip snapshots with acquisition provenance. `tree-scope.json` contains exact leaf sets, node ancestry and the alignment observations; `classification.json` records all 19 official flatfile classifications.

| Source | Access and evidential scope |
|---|---|
| PMID25825430 | Normal cache is abstract-only; genuine full publisher text is preserved in the transferred preflight captures. Bacillus YrvO directly supplies MnmA; this does not demonstrate negative Fe–S activity. |
| PMID31801798 | Full normal cache. Purified Thermus MnmA and desulfurase pairing supports direct delivery; native donor preference remains unresolved. |
| PMID33744947, PMID39660893, PMID41970532 | Full sources distinguish the E. coli Fe–S result, later conflicting findings and review synthesis. They do not license a universal C-type/D-type cofactor rule from SF5 membership. |
| PMID16387657, PMID16472754 | Protected abstract-only normal caches explicitly describe the positive Tus relay and TusD Cys78 result. Existing PAINT judgments are retained with that access limit; no experimental negative claim is manufactured from missing full text. |
| PMID26149121 | Full normal cache. Recombinant M. smegmatis EgtE acts on ergothioneine-pathway sulfoxide and thioether substrates. No negative L-cysteine assay is inferred. |
| PMID15790858 | Abstract-only normal cache explicitly describes SepCysS conversion of Sep-tRNA(Cys) to Cys-tRNA(Cys). Positive alternative chemistry establishes heterogeneity, not absence of any other activity. |
| Official UniProt A0R5M7/Q59072/O67046 | Archived current records and provenance distinguish experimentally curated EgtE/SepCysS functions from the unreviewed SF6 protein, whose precise MnmA activity is not established. |

The E. coli/Bacillus D-type residues were inspected in the actual family MSA. Thermus Q72GX1 is absent from that sampled tree/MSA; its cofactor claim rests on target primary evidence, not an invented alignment placement. A missing tree leaf is not a verified negative loss trace. PANTHER's surprising chloroplast wording for Thermus SufS SF8 is retained as classification, not used to reject bacterial function.

## Checks and preservation

- Eight family schema and ontology checks pass; references pass. The final PTHR43586 evidence additions were separately revalidated.
- Production residue/member/PTN grounding: 140 passes, zero failures, zero unresolved checks.
- Production family/gene crosscheck: zero conflicts and zero actionable comparisons. This does **not** independently verify all 19 gene functions; gene curation was concurrent and remains owned by the gene consultants.
- The one incremental index refresh completed. Seventeen target accessions have indexed matching rows; O34599 and Q72LH2 were not yet cited by the then-current module/family representatives and have no index row. Both have exact official SF34 assignments. A later root module refresh may include them.
- Strict preservation checks protect 22 original family source files, five current Isc nodes, ten imported Tus node objects and all 24 PAINT assertion payloads. Eight new helper-generated histories validate. All 81 quoted occurrences match their sources.
- The input closure freezes 164 source paths, including 38 gene raw files, original family inputs, quoted sources and the transferred preflight. Concurrent gene reviews/module/project are deliberately outside this family's receipt.
- No family-specific HTML renderer is available; the shared family index was not regenerated. No full-corpus validation or commit was performed.

Run the read-only final verification from the repository root:

```sh
uv run python analysis/module_audits/bacterial_mnma_trna_thiolation/family-consultation/verify.py
```

The acquisition, analysis, capture and curation scripts record how the artifacts were prepared. Do not rerun builders over a frozen release; `verify.py` is the release verification entry point. In particular, `curate.py` records the initial manual synthesis, and the final two primary PTHR43586 supports were added after that synthesis. The final YAML, generated history and exact handoff hashes are authoritative.
