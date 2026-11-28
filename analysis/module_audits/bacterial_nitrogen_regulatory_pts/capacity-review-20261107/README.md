# Independent finite-panel nitrogen-PTS capacity audit

The reviewed draft is biologically applicable to the three documented native triplets. No additional scientific correction is required by this consultation. This is a bounded assessment of twelve reviewed proteins, not a universal Pseudomonadota classifier or a prediction of physiological flux.

The baseline module is preserved byte-exact as `module-tested.yaml.txt` (SHA256 `567216e4d7a2d077d4a0b42e6caa42ce578fe57e8ceb7c35c1dd8e8e989caaf6`). Root is separately finalizing its status, labels, terminal node type and source presentation. Those later changes must have an explicit successor/rerun receipt; they are not silently folded into this result.

## Independent evidence model

`evidence-ledger.json` records primary-derived native transfer edges, target outputs, assay limits, the twelve accession-to-review identities, and independently read mechanistic quotation anchors. It is not extracted from the module's representative lists. In particular:

- **E. coli:** PMID10473571 explicitly reports purified EI(Ntr) phosphorylation of NPr and discrimination against HPr. PMID7876255 establishes purified phosphate exchange and also cross-system compatibility. PMID19400808 establishes a kinase-activation output. These cached abstracts are sufficient for the stated positive findings but are not represented as full inspected methods or a universal specificity barrier.
- **P. putida:** PMID18296519 establishes the native PtsP–NPr–PtsN phosphostate route and fructose-dependent FruB input. The separately acquired full Methods identify MAD2 as a rifampin-resistant KT2440 derivative carrying additional reporter/regulator constructs; tagged PtsN complements the disrupted native copy. This is native-derived pathway genetics, not purified binary kinetics. The canonical cache's full-text flag does not make its Abstract/Discussion excerpt complete. PMID21236318 connects PtsN with AceE and cell-extract PDH inhibition, not isolated binary inhibition kinetics.
- **NA1000:** PMID27109061 identifies the exact CCNA loci. PtsP phosphorylation uses EI-containing fractions, HPr competence includes heterologous complementation, and PtsN output combines BTH with engineered native hydrolase measurements. PMID26489861 PtsP–SpoT co-complex evidence does not make that association a mandatory relay part or establish isolated binding/activation.

A role is qualified only if independently supported by a native transfer edge, its current reviewed core enables the required activity, its source evidence resolves, and any declared family classification is present in the immutable UniProt record. The PtsN output must additionally have its own source anchor. Two connected primary-supported edges must share the actual carrier within one native context. Unknown members and untested combinations remain UNRESOLVED. The assay-tier differences above are retained; successful capacity does not mean every edge has been independently reconstituted with purified proteins.

## Actual checks

The production `ai_gene_review.module_logic.compile_module` and `is_satisfied` functions are used. Results: **55 cases, 19 model mutations, 21 evidence/core sensitivities**, all passing. Three additional same-chemistry controls and twelve actual UniProt family placements are independently verified. The current reviewed cores support GO0098772 through the official is_a ancestry of kinase activation, enzyme inhibition and transporter inhibition.

Cases include all three native positives; all 24 foreign triplets; removal of every role; every single-role subset; empty sets; carbohydrate EI with the same GO0008965 chemistry; E. coli HPr and Bacillus HPr with the same GO0016775 chemistry; Bacillus SF2 HPr tested with the taxon filter disabled; unknown carrier/terminal; and a fructose-bypass context that still lacks canonical entry. The negative result in the latter is limited to the canonical model, not all PtsN phosphorylation. There is no universal GAF, KdpD, SpoT, target direction, or output-protein requirement.

Declaration mutations cover optional/missing parts, ATP-specific entry or hybrid-kinase carrier chemistry, universal kinase output, misleading family selectors, reversed/deleted flow edges, absent applicability context, wrong taxon, missing or invented evidence, wrong representatives, and a wrong selector type. Two controls use genuine source quotations: an NA1000 strain-identification sentence and a kinase-activation sentence both fail as evidence for carrier transfer. Thus verbatim matching alone is not treated as biological support.

Sensitivities delete each native core, break each native-edge evidence anchor, replace each carrier's enabled MF with complex-contribution-only support, and remove each terminal output anchor. These are in-memory counterfactuals only; original qualifiers and curated files remain unchanged. Existing GOA rows are never used as the positive capacity oracle.

## Production compiler limits

The unaugmented static compiler does not interpret taxon/condition prose, native protein partnerships, source evidence or the biological meaning of connections. Actual witnesses show that representative-presence evaluation accepts a foreign mixed triplet and that deleting the two connections leaves static satisfiability unchanged. The independent graph/evidence checks supply these missing constraints for this finite audit. A green static circuit alone is not evidence of a native route. These limitations should remain explicit in reuse of the module.

## Preservation and source closure

The twelve reviews contain 103 ordered rows and seven historical NEW rows: six active and the already-retired PSEPK ptsH GO0016772 proposal. No row or lifecycle change was made here. All five sealed gene/control/family release manifests are checked. The only accepted pre-existing hash successors are root's three control-helper formatting changes; original archives, exact before/after hashes and independently normalized AST equality are verified. No scientific file is exempted.

`results.json` checks 292 quotation occurrences across the module, all twelve member/control reviews and all three relevant family reviews, with 125 current source dependencies. It also verifies the five prior handoffs. The final handoff adds exact ontology snapshots, raw classification records, full-body/provenance dependencies, compiler implementation and formatting-successor evidence. No new source fetch or global index/IBD build was performed.

The initial closure failure on a changed control helper and the interim AST-normalizer failure are preserved in `run.log` and `run-final.log`. The latter was a checker issue: a local variable rename also affected a function argument. Adding argument normalization reproduced root's bounded formatting proof; no broader deviation was allowed. `run-family-closure.log` and `run-source-binding.log` record successful subsequent checks.

## Reproduce additively

Use the existing environment, the current worktree's src on PYTHONPATH, and no bytecode/sync:

```sh
PYTHONPATH="$PWD/src" PYTHONDONTWRITEBYTECODE=1 \
/Users/cjm/orca/workspaces/ai-gene-review/aigr-modules-taxon/.venv/bin/python -P \
analysis/module_audits/bacterial_nitrogen_regulatory_pts/capacity-review-20261107/check_capacity.py \
--output-dir analysis/module_audits/bacterial_nitrogen_regulatory_pts/NEW-ADDITIVE-RESULT-DIRECTORY
```

The output-dir option changes only receipt placement and was added after the final scientific run so future finalization cannot overwrite its baseline. Preserve this directory and its handoff. The script reads the live module; a post-finalization result must therefore record its new hash and parsed change boundary. No full-corpus validation, curated edit, commit or push was performed by this consultation.
