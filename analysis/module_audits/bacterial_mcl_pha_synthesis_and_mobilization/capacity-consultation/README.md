# Medium-chain PHA capacity consultation

This audit evaluates the bounded combination of intracellular MCL storage-polymer synthesis and mobilization. It runs the repository's production `module_logic` compiler on the actual curated module. Independent, manually adjudicated member fixtures supply the biological role and evidence qualifications; they do not generate the module topology or expected case outcomes. No gene, family or module file is edited by this consultation.

## Biological evidence and profiles

The KT2440 and GPo1 panels support this combined profile, with either cognate synthase sufficient to represent the synthesis role. This is supported/inferred capacity under a supplied compatible substrate pool, not a claim that every enzyme has independently measured purified-target kinetics or that either synthase necessarily carries equal native flux. The matching-panel rule is conservative: it excludes unverified mixed panels, without claiming that cross-species engineering is impossible.

* KT2440 Q88D25/Q88D23: native pathway context and family chemistry support alternative PhaC roles. PMID31468725's combined engineering does not isolate each isozyme; PMID38608840's supplementary fraction detection is not a demonstration of selective enrichment for every protein. The released PSEPK review explicitly preserves these limits.
* KT2440 Q88D24: direct KT2442 depolymerase chemistry in PMID17170116/41055782 is combined with native KT2440 detection/perturbation evidence. A complete KT2442 construct-to-Q88D24 sequence bridge is unresolved. Consequently this is a close-strain inference, not a direct target assay. Weak tributyrin activity is not equated with native glycerolipid flux.
* GPo1 P26494/P26496/P26495: the M58445 coding sequences exactly match the reviewed proteins. PMID1989978 supplies genetic synthase/degradation roles, while the full PMID11133449 supports native polymer turnover with a leaky phaZ mutant and a rescuing C1-plus-Z fragment. Neither proves purified PhaZ product oligomers of size 1–5, so the module's broader ester-hydrolase realizer is preserved.
* O85207 and PAO1 Q51553: optional precursor routing is supported by native/heterologous genetics and comparative chemistry. PMID35338129's forward product-sink/FadD controls favor net ACP-to-CoA transfer; they are not purified forward acyl-ACP kinetics. PMID12200450 measures reverse transfer. PP0763 is therefore not a universally required extra step. PAO1 is a partial routing exemplar, not an invented complete turnover panel.
* H16 P23608: PMID10612741 and PMID35341893 positively support MCL-unit incorporation into SCL–MCL copolyesters in altered precursor contexts. They do not establish the characterized MCL storage-polymer profile with a matched intracellular mobilizer. Its separate `comonomer_incorporation` result remains positive while combined-profile and bounded synthesis results are unestablished. This is not a class I inactivity assertion. The 2000 construct sequence itself was not independently verified; the reference protein and 2022 H16 strain link are documented in the frozen class-I consultation.

The short checked quotations and exact identity records remain in the frozen literature, class-I, gene and family consultations. `check_closure.py` independently rechecks the eleven literature excerpts and two class-I primary abstract phrases, follows local/PMID citations, includes every fixture primary, and verifies all released file hashes. It does not confuse abstract access, failed downloads or curator interpretation with independently reproduced experiments.

## Tests and interpretation

`check_capacity.py` uses `compile_node`, `iter_atoms`, `core_atoms`, `enumerate_routes` and `is_satisfied`. The current circuit has four atoms: optional PhaG, PhaC, and two alternative intracellular PhaZ realizers. The stable `class_ii_phac_polymerase` identifier is historical; there is no class-II-specific domain requirement. Synthetic replacement of the class-II domain with a class-I domain while retaining hypothetical positive MCL-storage evidence is accepted, proving the absence of a hidden class gate. This synthetic sensitivity check is not a new assertion about H16.

The 32 cases include both complete panels, either/both synthases, missing synthesis or mobilization, partial PAO1 routing, optional FAS routing versus external input, absent precursor pools, mismatched panels, H16 copolymer evidence, incompatible polymer/access, strict purified-target uncertainty, and explicitly synthetic generic-acyltransferase, monoacylglycerol, family-only, secreted-hydrolase and PHB-only controls.

Seven mutations remove a mandatory role, make routing mandatory, substitute a wrong synthase family, require both PhaZ lineages, force the precise KT2440 hydrolysis term onto GPo1, or make mobilization optional. Independent expectations must detect each mutation. Seven sensitivity checks demonstrate that disabling role, product, activity, intracellular access, compatible panel or source-evidence gates creates the corresponding false positive; the seventh checks class independence.

The production compiler evaluates finite AND/OR logic. The biological wrapper additionally checks source-qualified role, family/activity/domain compatibility, polymer composition, intracellular accessibility, matching panel and input availability. Those gates are explicit external constraints, not claims that the compiler itself understands chemistry. ONE_OR_MORE alternatives establish existential sufficiency, not stoichiometry, expression, rate, essentiality or dominance. A failed evidence gate means the bounded profile is not established, not that the organism can never perform the activity. Granule organization, phasins, beta-oxidation and broader native growth remain outside the encoded reaction boundary.

Review-core alignment is a consistency check only. It is not an independent evidence oracle and does not count ACCEPT rows as assay coverage. The strict purified-target profile is evaluated from the absence of a fixture assertion of a purified forward target assay; all current complete panels remain uncertain at that stronger threshold.

## Reproduction and preservation

From the worktree root:

```sh
uv run python analysis/module_audits/bacterial_mcl_pha_synthesis_and_mobilization/capacity-consultation/check_capacity.py
uv run python analysis/module_audits/bacterial_mcl_pha_synthesis_and_mobilization/capacity-consultation/check_closure.py
uv run ruff check analysis/module_audits/bacterial_mcl_pha_synthesis_and_mobilization/capacity-consultation
```

The closure's one-time `--capture` is used only after all seven releases and the COMPLETE module are final; it refuses to replace an existing snapshot. Ordinary reruns verify that snapshot. The three baselines retain all 23 original ordered payloads. Five historical NEW rows remain present; the authorized KT2440 PhaZ granule proposal alone is retired, with action and payload preserved. One explicitly authored PAO1 PhaG IC molecular-function row is the only added annotation. Prior handoffs, sources and proofs remain unchanged. Final result and handoff hashes identify the exact inputs evaluated.

## Final validation boundary

Root’s final module validator passes with four family-function scope warnings. These are retained: broad PhaG, synthase and PhaZ family membership does not universally establish the exact activity. The exact-member/source gates in this audit are consequently substantive, and the finite positive panels do not resolve all branches of those families. The family audit itself reports 95 grounding checks passed with no unresolved membership; functional scope uncertainty is a different issue. The final closure covers seven immutable releases, their seven root receipts, 400 input files (including 69 baseline-protected sources), the final module render/history, and thirteen rechecked excerpts.
