# Independent scientific review of the MnmA module draft

**Decision: no blocking biological issue found in the reviewed draft.** This assessment applies to module SHA256 `373e71c4e0a5cf941f98f76cc0a0176d417e048416320ef5a560188445fd75ae` (status DRAFT). It is a scientific integration review, not a fresh whole-corpus validation or a claim that bare Boolean satisfiability proves native flux.

## Boundary and route interpretation

The module has multiple substantive roles: cysteine sulfur mobilization, delivery, and ATP-dependent terminal tRNA U34/C2 thiolation. Even the abbreviated Bacillus and Thermus branches retain donor chemistry and terminal MnmA chemistry as separate required roles. U8/U54 thiolation, Ncs6 systems, C5 elaboration, Fe–S scaffold assembly and other IscS destinations are excluded deliberately. Cofactor supply and active enzyme state are appropriate context rather than extra invented universal genes.

The E. coli Tus branch retains all seven proteins and a TusBCD complex with structural B/C units and sulfur-bearing D. KT2440 is explicitly a conserved-function inference, supported by target classifications, locus neighborhood and homologous active-site mappings. A sequence alignment is not presented as a native assay or proof of cotranscription. The module does not make structural TusB/C independent sulfur carriers.

The Bacillus pair is attached to PMID25825430 with an explicit PS832-to-168 derivative bridge. Purified partnership, heterologous rescue and native conditional expression are distinguished. The draft does not turn a failed heterologous substitution into a universal incompatibility claim, or assert a stable obligate complex from a functional partnership.

Both HB27 donor alternatives are grounded in the actual Thermus primary assay, not chosen by an IscS/SufS label. PMID31801798 removes reductants before donor pairing and finds activity with either enzyme. Its native donor allocation remains unresolved. PMID16547008 is properly used to bridge named donor loci; its U54 reaction is not substituted for evidence of MnmA U34 catalysis. The C-type route requires active cluster-bearing enzyme under the characterized assay conditions; this is not projected onto every D-type MnmA.

## All-member consistency

All 19 module accessions exactly match the independently frozen classification panel and COMPLETE gene reviews. `member-review.json` captures the actual descriptions and cores read in this review. The seven E. coli and seven KT2440 roles, Bacillus donor/MnmA pair, and three Thermus proteins are consistent with the module's catalytic, carrier and structural assignments. Reused IscS reviews retain their other sulfur destinations; the module narrows the modeled process without silently narrowing the gene's biology.

PSEPK TusB/C cores express structural participation without an autonomous molecular function; this is compatible with their functionless structural active units in the module. ECOLI TusB/C explicitly contribute to complex sulfurtransferase activity. Neither representation licenses isolated B or C to supply the full complex activity.

## Uncertainty retained correctly

The TusE carrier assertion and delivery connection do not assert conclusively observed covalent loading of an MnmA cysteine. The consulted critical review identifies that exact experimental gap. The draft's qualified reaction-level connection is appropriate and agrees with both gene panels.

The D-type Fe–S dispute is recorded as uncertainty, not as a universal positive or negative. Thermus cluster dependence is source-qualified. Exact C/D type, tRNA substrate and partner compatibility cannot be inferred from shared PTHR11933:SF5 membership.

Family labels remain classifications. PTHR11601:SF34 includes the distinct YrvO partnership; PTHR43586:SF8 also contains positively characterized EgtE. PTHR33279 includes other sulfur destinations. These facts justify the unresolved universal grants and explicit target/partner constraints. The surprising chloroplast label for Thermus SF8 is not evidence against its experimentally supported bacterial role.

## Nonblocking implementation cautions

1. **Capacity must apply the stated biological gates.** The production compiler's Boolean atoms do not themselves establish target activity, a complete compatible TusBCD assembly, same-panel interfaces, substrate supply or active C-type cofactor state. A family match alone must not satisfy these roles. This is a model-execution limitation, not a reason to weaken the family uncertainty. The next capacity consultation will exercise these gates explicitly.
2. **The PTHR11933 descendant warning is not a biological contradiction.** SF5 supports the broader sulfurtransferase genus while exact GO0103016 scope remains unresolved across the entire clade. Positive target-specific MnmA activity is independently supported for the four representatives. Any validator handling of a broader applicable grant versus an unresolved specific grant should be diagnosed in tooling; do not change family science merely to suppress the warning.

No corrective mutation of the module or member reviews is requested from this read. A later status-only change needs a new integration hash, not a claim that this receipt reviewed different bytes.

## Evidence closure and limits

The review verified all 154 new-member, 81 existing-review and 71 family-release manifest paths unchanged, and records 84 directly reviewed input hashes. Primary/review distinctions and publication-access limits follow the frozen evidence ledgers: the initial Tus papers are abstract-only in normal caches with explicit positive findings; the critical Fe–S review and Thermus primary are full text; Bacillus full publisher evidence is in the preserved preflight. No experimental negative conclusion was drawn from inaccessible full text.

Guidance read: `.codex/skills/aigr-pr-review/SKILL.md`, `.claude/skills/module-curation/SKILL.md`, its modeling/research references, and `modules/README.md`. Structural schema/format validation was trusted rather than redundantly rerun. No scientific source, gene, family, module, project or previous receipt was changed.
