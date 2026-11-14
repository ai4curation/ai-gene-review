# PR #6150: biological review follow-up

Reviewed head: `b4a3149dfba627e423b9356c74b7b757018a09fa`. The annotation-reviewer and aigr-pr-review skills were applied to the changes-requested review and [review comment](https://github.com/ai4curation/ai-gene-review/pull/6150#issuecomment-6698643325). `round1-action-reversal-ledger.yaml` records all **16**, rather than approximately 15, action reversals in the five previously reviewed bacterial members relative to `5f8f3b5c5e22a179b67559485e8ef3b47cb0d815`. It gives source-order row indices, original evidence/reference fields, prior reasons, and final evidence-backed reasons. No annotation is deleted, added, or reordered by this follow-up.

## Transcription mapping: one structural criterion

The two IPR025703-derived transcription rows in **BRADU and SINMM change MARK_AS_OVER_ANNOTATED to REMOVE**. Like the already rejected CfPutA and GsPutA mappings, these are transfers of a specialized RHH-mediated regulatory function to a solved, non-RHH bifunctional architecture. The sequence-matched BjPutA and SmPutA structures are positive evidence about domain architecture, not merely missing experiments. PMID:28990412 explicitly distinguishes class 1C regulatory PutAs; PMID:27679491 identifies their N-terminal RHH extension. The same electronic mapping error warrants the same action in all four structurally characterized non-RHH targets.

This does not claim a negative DNA-binding assay for Bj/Sm/Gs/Cf or exclude every conceivable unconventional regulatory interaction. HELPG retains REMOVE with an additional line of evidence: PMID:16452403 reports negative promoter gel shifts at up to 100-fold protein excess for **J99** PutA. That is comparative evidence for the non-RHH **G27** target, not a direct G27 experiment. Its existing strain qualification remains intact. This evidence gradient strengthens HELPG's judgment without changing what the common electronic-mapping action means.

## Membrane-face location: preserve the actual source differences

**PSEPK PutA GO:0009898 changes ACCEPT to UNDECIDED.** Its frozen UniProt cross-reference identifies TreeGrafter; there is no independently curated target subcellular-location statement. The available tree did not resolve the target's placement. Promoter genetics and the sequence-matched PpPutA45 DNA-binding fragment do not locate full-length KT2440 catalysis. The general quinone-coupling review establishes plausibility, but its flavin-switch sentence was insufficient support for this exact location. The replacement quotation states the family membrane-coupling mechanism explicitly, while the reason distinguishes that mechanism from target localization. The existing core synthesis already omitted a precise location.

The remaining location decisions are source-specific:

| Target | Decision and evidential basis |
|---|---|
| GEOSL | ACCEPT as a mechanistic inference supported by the target quinone-site structure and implied membrane-approach geometry, PMID:24550478. It is not a native-cell localization assay. |
| BRADU | ACCEPT retains a PAINT inference, with no applicable cached IRD/IKR, in the experimentally characterized quinone-coupled catalytic architecture. This is phylogenetic/mechanistic support, not a target localization measurement. |
| SINMM | ACCEPT as mechanistic inference from the sequence-matched target structure, demonstrated coupled turnover with ubiquinone-1 (PMID:27679491), and the family membrane-coupling mechanism. The soluble model-quinone assay does not itself measure native localization. |
| 9CORY | UNDECIDED: the source-derived recombinant construct, unspecified native source strain, and unresolved TreeGrafter placement do not establish native membrane-face localization. Model-acceptor turnover alone is insufficient. |
| HELPG | UNDECIDED: the J99 study uses DCPIP and does not assay Helicobacter membrane binding or sidedness; the G27 TreeGrafter assertion remains unresolved. |

Thus ACCEPT is not reserved exclusively for direct localization experiments, but neither is generic quinone-family membership treated as sufficient to settle every target's precise location. These retained inferences remain less direct than a measured membrane-side assay.

## Existing action reversals: retain justified chemistry, repair the unsupported location

The retained reversals reflect annotation truth and centrality, not upgrades in evidence code. The full row-level ledger includes:

- **ECOLI PutA homodimerization and FAD binding:** specific central mechanisms, supported respectively by native-protein/PutA47 dimer evidence (PMIDs:1618807,15155740) and catalytic/redox-switch FAD chemistry (PMID:22040654). They do not become peripheral merely because they support another function.
- **SALTY proline binding:** the same experimentally investigated site participates in catalysis and induction (PMID:7730362). This was the sixteenth reversal omitted from the reviewer's approximate count.
- **ECOLI and SALTY L-glutamate formation:** the enzyme itself catalyzes the product-forming reaction. The existing IDA assertions are retained, with the full-length versus PutA669 fragment distinction and abstract-only limitations preserved. GO:0097054 is not restricted to GDH/GOGAT or de novo anabolism. Its biosynthetic ancestry does not negate direct formation of glutamate during proline utilization. These existing rows can describe central chemistry alongside GO:0006562; no new process rows are proposed.
- **Yeast PUT2 consistency:** its existing GO:0097054 IDA row now changes KEEP_AS_NON_CORE to ACCEPT, and this process is included beside proline catabolism in the core synthesis. PMID:387737 independently establishes the native proline-to-glutamate pathway and Put2's terminal enzyme role. The original bibliographic-only PMID:4145181 row is preserved and is not represented as a newly read experiment. Neither yeast nor bacterial synthesis is described as the principal source of cellular glutamate.
- **ECOLI versus PSEPK PutP sodium binding:** both remain ACCEPT, with a real evidence gradient. PMID:1567896 directly supports Na+-dependent protection without proline for ECOLI. PSEPK has a specific Na/proline symporter family assignment (TIGR02121), curated RuleBase:RU366012 function, and conserved mechanistic inference. It has no target sodium-only binding result, measured affinity, or stoichiometry. GO:0031402 simply denotes sodium binding; it does not require an autonomous binding role separate from symport. The PSEPK reason now states the cross-target evidence difference explicitly.
- **Broad binding and DNA-binding refinements:** MODIFY follows the repository rule for a true broad term with supported descendants. Changing these to TOO_GENERAL solely because a specific term is present would conflict with that rule. PSEPK GO:0000976 refines to the sequence-specific descendant GO:0000987, supported by the exact-match PpPutA45 DNA-binding construct (PMID:18767154).

## Live ontology checks

Official QuickGO services were retrieved on 2026-11-06; exact responses and ancestry are cached in `.cache/module-audit-logs/puta-20261106/round1/GO_*.json`. The UI pages were unavailable to the browser, so the official JSON service supplied the checks. `round1-ontology-checks.yaml` records the verified results and URLs.

- GO:0097054 is defined by chemical reactions/pathways resulting in L-glutamate formation; the definition contains no de novo-only restriction. Its amino-acid biosynthetic ancestry was read, not ignored.
- GO:0031402 is binding to sodium ion; it contains no independence-from-transport requirement.
- GO:0050660 FAD binding and GO:1901973 proline binding are descendants of both GO:0043168 anion binding and GO:1901363 heterocyclic compound binding.
- GO:0051287 NAD binding is below GO:1901363 **but not GO:0043168**. The unequal two-versus-three replacement lists are intentional and correct; no NAD term was added to the anion replacement lists.
- GO:0000987 is a descendant of GO:0000976.

## Coverage checker: curation consistency, not independent assay verification

The checker no longer uses ACCEPT as the only source of true activities. It collects retained ACCEPT and KEEP_AS_NON_CORE claims, MODIFY replacement terms, and molecular functions in the core synthesis. Retired/negated rows and historical NEW proposals are excluded. It records the contributing row index, curation action, original evidence type/reference, or core-synthesis index for each required activity. These are **provenance of reviewed claims**, not an automated re-evaluation of the cited experiments.

The same 44 curation-coverage cases and six mechanism mutations still pass. Ten additional extraction checks verify that peripheral-but-true activity remains usable, valid replacements/core synthesis are recognized, and rejected, undecided, proposed, retired, or negated rows do not supply positive row evidence. Explicit same-polypeptide and same-strain rules remain necessary; the compiler does not interpret the free-text fusion descriptor. Family-control assignments and synthetic counterfactuals are still declared inputs. No conclusion about native flux or uniform independent experimental coverage follows from PASS.

## Other review points and scope

PSEPK and HELPG PutP quotations now finish the L-proline substrate name across the UniProt line wrap. The SINMM biosynthesis rejection now leads with the actual pathway-segregation passage from PMID:27679491. The coordinator separately corrected the family `reviewed_by` attribution to `claude-code; codex` and generated its provenance record; this consultation does not change the family, module, or shared trackers. Six gene histories were generated with `just new-history`. Focused validation, rendering and preservation results are recorded separately; full-repository validation and PR publication belong to the coordinator.
