---
title: "Pathway satisfiability — independent review"
maturity: IN_PROGRESS
tags: [PIPELINE]
autolink_gene_symbols: false
---

# Independent review: pathway satisfiability

Companion to [Pathway satisfiability](../PATHWAY_SATISFIABILITY.md),
[Methods & reproduction](methods.md) and
[`modules/experimental/gluconeogenesis-context/RESULTS.md`](../../modules/experimental/gluconeogenesis-context/RESULTS.md).

This page records an independent review of (a) the GO annotation reviews for the genes the
project depends on and (b) the logic and scientific validity of the project's stated
conclusions. Everything below was re-derived from the committed code and caches; each finding
names the file and the check that produces it.

> **Status: findings applied.** This page is kept as the audit record. Every finding below has
> since been fixed in the code, modules and prose — see [What was changed](#what-was-changed-in-response)
> at the end for the mapping from finding to fix. Findings are left in the past-tense-free
> original wording so the reasoning stays legible; the fixes are listed separately rather than
> edited in.

## Verdict

**The engineering is sound and every published number reproduces exactly. Three of the
project's headline scientific claims are materially overstated, and one — the microbial
"metabolic dark matter" result — is a false positive that the project's own data source
refutes.**

The separation of logic core from oracle is a genuinely good design, the code does not
fabricate data, and the honest-scope section is unusually candid. The problems are almost all
in the *interpretation* layer: the prose consistently claims more discriminating power for the
boolean circuit than the circuit actually contributes, and reports single-cause explanations
for multi-cause results.

## What was verified (all clean)

| check | command | result |
|---|---|---|
| Engine doctests + unit tests | `uv run pytest --doctest-modules src/ai_gene_review/module_logic.py tests/test_module_logic.py` | 38 passed |
| Gene reviews (10) | `uv run ai-gene-review validate --verbose --terms genes/human/<G>/<G>-ai-review.yaml` | 10/10 valid (1 warning, GPD1) |
| Module YAMLs (4) | `linkml-validate -C ModuleReview` + `module_validator` | 4/4 valid, 0 label warnings |
| Every resolver | `resolve_context / _zonation / _substrates / _genomes / _abduction / _eukaryotic_abduction` | output matches the published tables verbatim |
| Figure provenance | `figures.py` imports the resolvers | colouring is engine-derived, not hardcoded — as claimed |
| Cached GTEx values | `cache/gtex_medians.tsv` | G6PC1 168.9 / 5.55 / 2.83 TPM and OXCT1 heart 59.9, brain 44.8 all match the prose |

No fabricated data was found anywhere. The `gtex_oracle.py` and `kegg_oracle.py` clients are
real API clients, and the "never invent data" note about the human zonation oracle
(RESULTS.md) is an honest call.

## Major findings

### 1. The 54-tissue result is a single-gene filter; the pathway logic contributes nothing

`PATHWAY_SATISFIABILITY.md` presents the GTEx result as the module "lighting up" in exactly
three tissues, with a graded gate. In fact the satisfiable set is **identical to
`G6PC1 ≥ threshold`** at every published threshold:

```
thr=1.0: G6PC1 alone -> Kidney_Cortex, Liver, Small_Intestine_Terminal_Ileum
thr=5.0: G6PC1 alone -> Kidney_Cortex, Liver
thr=10.0: G6PC1 alone -> Liver
```

Every other atom is non-discriminating at the 1 TPM bar:

| gene | tissues passing (of 54) |
|---|---|
| PCK2, SLC37A4, G6PC3 | 54 |
| PC | 53 |
| FBP1 | 42 |
| PCK1 | 16 |
| FBP2 | 5 |
| **G6PC1** | **3** |
| G6PC2 | 2 |

So "recovers textbook biology from data alone", "no false positives, no misses" and the graded
threshold sweep are all properties of *G6PC1's expression profile*, not of the boolean circuit.
A one-line `G6PC1 ≥ 1` filter reproduces the entire figure. The circuit is doing no work here
because the ORs (PCK1|PCK2, FBP1|FBP2) are satisfied by a ubiquitous branch in essentially
every tissue.

Related: **"the engine resists the ubiquitous paralog G6PC3" is not an engine result.** The
exclusion of G6PC2/G6PC3 is a hand-written curator decision in
`modules/gluconeogenesis_human.yaml` (the `notes:` "paralog trap" block on the
`g6pc_catalytic_node`). Nothing in the engine or the expression data derives it. Worse, it is
not derivable from GOA either: the G6PC3 gene review *retains* `GO:0006094` gluconeogenesis
(three rows, all `KEEP_AS_NON_CORE`) and credits "intracellular glucose production" in
`core_functions`, so a module built automatically from GOA would admit G6PC3 for the terminal
step. The claim should be restated as "the curated module grounds the terminal step to G6PC1,
which is what prevents the paralog trap" — an argument for curation, which is a perfectly good
claim, rather than for the engine.

### 2. The zonation result is reported as single-gate but is multi-cause, and is partly carried by the muscle isozyme

Two problems, both verifiable from `cache/halpern_zonation.tsv`.

**(a) The pericentral pole fails at three steps, not one.** Instrumenting `unsatisfied_steps`
directly at the default threshold 0.5:

```
L1 sat=False  failing_steps=['pepck_step', 'fbpase_step', 'glucose_release_step']
```

`resolve_zonation.py` reports only `missing_gate`, which is filtered to `core_atoms`
(`PC`, `G6PC1`, `SLC37A4`) — so it surfaces `G6PC1` alone and hides the PEPCK and FBPase
failures. This is what produces the headline "the same gate atom, G6PC1, operates at two
scales" and Figure 2's caption "blocked at the very same gate atom". The clean two-scale story
is an artifact of the reporting filter. Recommend reporting `unsatisfied_steps` alongside
`missing_gate`.

**(b) Layers 2–4 are satisfiable only via FBP2, the muscle isozyme.**

```
thr=0.5:  L2 FBPase_via=['FBP2']   L3 FBPase_via=['FBP2']
thr=0.7:  L3 FBPase_via=['FBP2']   L4 FBPase_via=['FBP2']
```

Fbp1 falls below the relative bar in those layers and Fbp2 rescues the step — even though
Fbp2's absolute abundance in the Halpern data is ~8,000× lower than Fbp1's
(`Fbp2` L1 = 7.6e-08 vs `Fbp1` L1 = 6.1e-04). This happens because `relative_profile()`
normalises **each gene to its own peak**, which erases absolute abundance entirely: a gene
expressed at essentially zero counts as "present" wherever it sits near its own tiny maximum.
That is precisely the paralog trap the project claims to resist at the G6PC level, occurring
unnoticed at the FBP level, and it contradicts the tissue-level narrative ("never the muscle
isozyme FBP2").

**(c) The gradient is thin.** `G6pc` varies only 2.2-fold across the nine layers
(rel L1 = 0.45), so the pericentral block turns on 0.45 vs a 0.50 cutoff. `Pcx` (1.1×) and
`Slc37a4` (1.3×) are effectively flat. The periportal restriction is real biology, but this
particular derivation of it rests on a threshold slicing a near-flat profile, and the "derived,
not assumed" framing (true of the *orientation*, which is properly inferred from landmarks)
should not be extended to the robustness of the call itself.

### 3. Both microbial "abduction targets" are false positives — KEGG itself encodes the enzyme

This is the most consequential finding. The project's most striking claim is that
*Synechocystis* and *M. jannaschii* are "real metabolic dark matter": organisms that
"make methionine with no canonical enzyme for a step", emitting a lead that "an unannotated /
non-orthologous enzyme must fill this step".

Both genomes encode **K23975, L-aspartate semialdehyde sulfurtransferase (EC 2.8.1.16)**, in
KEGG — the very database the oracle queries:

```
mja  ko:K23975  mja:MJ_0100      (and MJ_0099 -> K23976, the ferredoxin partner)
syn  ko:K23975  syn:slr0689
eco / buc / rpr : absent
```

This is the characterised route by which methanogenic archaea make homocysteine directly from
aspartate semialdehyde and sulfide ([PMID:25938369](https://pubmed.ncbi.nlm.nih.gov/25938369/),
*Biochemistry* 2015), bypassing homoserine acylation entirely. Consequences:

- The gap is **not** dark matter and **not** an unannotated enzyme. The enzyme is identified,
  published, and KO-assigned.
- The correct explanation is the engine's own hypothesis #2, *"an alternative route not
  represented in the module is used"* — the engine emitted the right hypothesis and the prose
  promoted the wrong one to the headline.
- Because the route bypasses homoserine, it is outside the module's declared scope
  (`title: L-methionine biosynthesis (from homoserine)`). A gap for an organism that does not
  use the modelled entry point is a scope artifact, not a discovery.
- The root cause is the 7-entry `STEP_KO` table in `kegg_oracle.py`, which omits K23975/K23976.

Nuance worth preserving: the *Synechocystis* pathway is still described in the literature as
unresolved (the genome lacks MetA/MetB/MetC homologues and the steps before MetH have not been
experimentally determined), so it remains a reasonable target — but "none of the known
candidates are encoded" is true only relative to a seven-KO table, and KEGG already offers
`slr0689` as a candidate.

**Fix:** add K23975/K23976 to the oracle and give the module a third top-level route
(AspSA + sulfide → homocysteine → methylation) that bypasses both `acylation` and
`sulfur_incorporation`. Since `eco`, `buc` and `rpr` lack K23975, this would not disturb the
four prototroph FOUND calls or the *Rickettsia* `CONSISTENT_INACTIVE` result; `syn` and `mja`
would correctly resolve to FOUND (both already have a methylation step: `syn` metH, `mja` metE).

### 4. The oracle cannot distinguish "gene absent" from "step not in my lookup table"

Finding 3 is a specific instance of a structural weakness. In both `resolve_genomes.py` and
`resolve_abduction.py` the predicate is:

```python
def holds(atom, _p=present):
    return bool(atom.gene_symbol) and _p.get(atom.gene_symbol, False)
```

Any atom whose symbol is missing from `STEP_KO` silently evaluates **False** — indistinguishable
from a real genome gap. `metZ` is already in this state: it is a variant in
`modules/methionine_biosynthesis.yaml` and appears in the abduction output's candidate list, but
has no entry in `STEP_KO`. (I checked K10764 across all eight genomes: genuinely absent
everywhere, so no published result changes — but only by luck.)

Since the whole epistemic claim of the abduction step is that a flagged gap is *a genuine
prediction*, an oracle that reports "absent" for "unmapped" undermines it directly. Recommend
the oracle raise or warn on any atom it cannot map, rather than defaulting to False.

## Moderate and minor findings

### 5. The Buchnera framing is inverted

`RESULTS.md` states the engine's gap is "precisely why Buchnera is a methionine auxotroph
dependent on its host." The biology runs the other way: *Buchnera* methionine biosynthesis is a
**shared pathway** with the aphid, in which Buchnera retains the terminal MetE step — notably
the only amino-acid biosynthetic gene keeping its ancestral `metR` regulator — and
**provisions methionine to the host**, with earlier intermediates supplied collaboratively.
Calling it a plain auxotroph inverts the significance of exactly the gene the engine found.

Two notes: `resolve_abduction.py` is more careful than the prose — it deliberately omits `buc`
from `ACTIVITY` with the comment *"methionine requirement is contested / host-complemented;
not asserted here"*, which is the right call and contradicts RESULTS.md. And *Buchnera* is
arguably the project's **best illustration** of the "not cell-autonomous / cross-feeding"
hypothesis it already lists — currently mislabelled as simple auxotrophy.

### 6. OXCT1 liver is 0.46 TPM, not 0

The committed cache has `OXCT1` liver = 0.457 TPM. Both `PATHWAY_SATISFIABILITY.md` ("GTEx
liver = 0 TPM") and `RESULTS.md` ("OXCT1 = 0 TPM in liver") round it to zero. The conclusion is
unaffected (it is ~100× below heart and far under any threshold) but the stated number should
match the cache.

### 7. Unmodelled trunk

`reversible_glycolytic_trunk` has no annotons, so it compiles to `And([])` = permanently True —
roughly seven enzymes of the pathway are not modelled. This is deliberate and disclosed in both
the module description and RESULTS.md, so it is not a defect; noting it only because it further
reduces the number of atoms that could ever gate the circuit (see Finding 1).

## Gene annotation review

All ten reviews pass validation and are, on the whole, good work. Notably **clean on the rules
that matter most**: no `REMOVE` of an experimental annotation on thin evidence, no misuse of
`CIRCULAR_OR_REDUNDANT` for IBA self-sources, no project/curation commentary in any
`description`, and 100% GOA row coverage in every file. Several files handle the hard cases
exactly as `CLAUDE.md` prescribes — OXCT1 explicitly declines to REMOVE the PMID:11756565
OXCT2/SCOT-t paralog IDA, G6PC1 defers to the curator on two "wrong-gene-looking" experimental
rows, and SLC37A4 justifies retaining PMID:21949678 in `reference_review`.

### Issues to fix

**Substantive:**

1. **G6PC1 — the single `REMOVE` is biochemically wrong.** `GO:0016773` (phosphotransferase
   activity, alcohol group as acceptor) is removed on the grounds that transfer to an alcohol
   "mischaracterizes the reaction". Glucose-6-phosphatase's phosphotransferase activity is
   real and classical: the His-176 phosphohistidine intermediate can be resolved by glucose or
   another alcohol as well as by water (EC 2.7.1.62). The paper cited to justify removal
   (PMID:12093795, the phosphohistidine intermediate) is the mechanism that *enables* the
   transferase chemistry. The row is also an `ECO:0000265` Ensembl projection from mouse
   G6pc1, i.e. downstream of experimental evidence. Should be `KEEP_AS_NON_CORE` or `MODIFY`.
2. **No G6PC2 review exists.** `genes/human/G6PC2/` is absent, yet the islet /
   catalytically-inactive-autoantigen claim is load-bearing for the paralog-trap argument in
   two module YAMLs. Worth creating.
3. **GPD1's review points the opposite way from the module.** The module's `gpd1_node` runs
   G3P → DHAP (oxidative, the glycerol-to-glucose direction), but the review demotes exactly
   that (`GO:0046168` glycerol-3-phosphate catabolic process → `KEEP_AS_NON_CORE`) and makes
   the reductive/biosynthetic direction core. Either the review should represent the fasting
   hepatic/renal gluconeogenic direction or the module's glycerol lane is unsupported by its
   own gene review.
4. **LDHA likewise.** `core_functions` cover only the fermentative (pyruvate → lactate)
   direction; the module assigns LDHA the lactate → pyruvate role. LDHB *does* support its
   module role explicitly and well.
5. **G6PC3 `description` has an uncited claim and an outdated mechanism** — the
   1,5-anhydroglucitol-6-phosphate substrate is stated without a citation and is not in the
   cached UniProt record, and the SCN4 mechanism is given in the older ER-stress/apoptosis
   form, omitting the 1,5-AG6P accumulation mechanism (Veiga-da-Cunha 2019) which is in fact
   the strongest available argument for the project's own paralog-trap claim.
6. **LDHA mitochondrion IBA self-contradicts.** Marked `MARK_AS_OVER_ANNOTATED` with
   `propagation_review: PROPAGATION_BAD / COMPARTMENT_OR_COMPLEX_MISMATCH`, while its own
   `supporting_text` affirms mitochondrial LDH — and LDHB keeps the same family-level IBA as
   non-core. Per the IBA rules the challenge should address node placement.
7. **LDHB over-general parents use the wrong action.** `GO:0003824`, `GO:0016491`,
   `GO:0016616` are `MARK_AS_OVER_ANNOTATED` with no `proposed_replacement_terms`; `CLAUDE.md`
   says too-general → `MODIFY` + replacement, which is what LDHA does for the identical terms.
8. **`NEW` entries carry borrowed provenance.** PC's `GO:0006107` is stamped `IBA` /
   `GO_REF:0000033` and GPD1's two `NEW` entries are stamped `IEA` + a `file:` reference,
   asserting evidence for annotations that are not in GOA. A `NEW` proposal should not inherit
   an evidence code implying an existing annotation. This looks like a repo-wide pattern worth
   a lint rule.
9. **ACAT1 minor chemistry slip**: the `GO:0015937` note says CoA is released during thiolytic
   cleavage; thiolysis *consumes* free CoA. The over-annotation verdict itself still stands.
   ACAT1 is otherwise the strongest of the ten — its `REMOVE` of the two SOAT1/SOAT2-derived
   IDA rows is properly grounded in cached full text.

**Consistency and hygiene:**

- `GO:0005783` is `ACCEPT` in G6PC3 but `KEEP_AS_NON_CORE` in G6PC1 for the same situation.
- Redundant parent MF terms are `MARK_AS_OVER_ANNOTATED` in OXCT1/BDH1 but `KEEP_AS_NON_CORE`
  in ACAT1; "identical protein binding" diverges between OXCT1 and ACAT1.
- Eight of ten files are still `status: INITIALIZED` with zero PENDING actions (only G6PC3 and
  ACAT1 are `COMPLETE`).
- OXCT1 has several degenerate `supporting_text` fragments that pass the verbatim check but
  support nothing — "A single approximately", "mediates the", and the bare word "heart".
  G6PC1 reuses one quote across six unrelated response-to-X IEAs.
- `G6PC1-notes.md` and `SLC37A4-notes.md` both end with stray `</content></invoke>` tool
  artifacts.
- ACAT1 has one GOA row fewer than GOA (`GO:0016453` appears twice in GOA, once in the review).

### Module/review tension

The OXCT1 review correctly describes the SCOT reaction as **reversible**; the ketolysis module
calls it "committed, essentially irreversible". The pathway-level directionality claim should
be softened, or the distinction between thermodynamic reversibility and physiological
directionality made explicit.

## Recommended actions, in priority order

1. Add K23975/K23976 to `kegg_oracle.STEP_KO` and add the aspartate-semialdehyde route to
   `modules/methionine_biosynthesis.yaml`; retract or heavily qualify the "metabolic dark
   matter" claim for *M. jannaschii*, and re-scope the *Synechocystis* claim to "the canonical
   route is absent; a candidate (`slr0689`) exists and is uncharacterised".
2. Make the genome oracle fail loudly on atoms it cannot map, instead of returning False.
3. Report `unsatisfied_steps` (not just `missing_gate`) in the zonation resolver, and correct
   the "same gate atom at two scales" claim to reflect the three failing steps.
4. Replace per-gene peak normalisation in the zonation oracle with something that retains
   absolute abundance, or add an absolute floor so a gene at ~1e-07 cannot satisfy a step.
   Re-check the periportal result afterwards.
5. Restate the GTEx result honestly: the discriminating power is G6PC1's expression profile,
   and the value added is the *curated grounding* of the terminal step to G6PC1, not circuit
   evaluation. Consider demonstrating the circuit on a module where the ORs actually
   discriminate — the substrate module is the better candidate, since it does produce a
   genuinely different gate.
6. Correct the *Buchnera* framing in RESULTS.md to match `resolve_abduction.py`'s own caution,
   and promote it as the cross-feeding exemplar.
7. Fix the OXCT1 "0 TPM" figure to 0.46.
8. Work the gene-annotation list above, starting with the G6PC1 `REMOVE` and the missing G6PC2
   review.

## What was changed in response

All findings above were applied. Engine tests went 38 → 41 passing (three new regression cases);
all gene reviews and modules still validate.

**Engine, oracles, modules**

| finding | fix |
|---|---|
| 3 — phantom dark matter | `modules/methionine_biosynthesis.yaml` restructured: top-level steps are now `homocysteine_formation` → `methylation`, and the aspartate-semialdehyde route (`MJ0100`+`MJ0099`, UniProtKB:Q57564/Q57563, PMID:25938369) is a variant of the *whole* acylation + sulfur-incorporation arm. Title dropped "(from homoserine)". 14 routes. |
| 3 — oracle coverage | `STEP_KO` gained K23975, K23976 and the previously-unmapped `metZ` (K10764); KEGG cache rebuilt. `syn`/`mja` now `CONSISTENT_ACTIVE`; `rpr` auxotrophy and all four prototroph reconstructions unchanged; **zero** abduction targets remain. |
| 4 — silent unmapped atoms | new `kegg_oracle.holds_for()` raises `UnmappedStepError` instead of returning `False`; both genome resolvers now use it in place of their duplicated closures. Doctested. |
| 2a — single-gate misreport | `resolve_zonation.py` now reports `failing_steps` (all of them) beside `missing_gate`. L1 shows three failing steps; L2–L3 fail at `fbpase_step` where `missing_gate` is empty. |
| 2b — FBP2 rescue | new `zonation_oracle.expressed()` requires an absolute floor (`ABSOLUTE_FLOOR = 1e-5`, inside a 33-fold empty gap) as well as the relative threshold. Blocked zone grows L1 → L1–L3; the threshold sweep becomes genuinely monotonic. |
| — | `resolve_genomes.route_signature()` rewritten: every branch is decided by a gene that is *present*, never by an `else` default (it had been mislabelling the new route). Hardcoded "8 route combinations" replaced with the computed count. |
| 5 — Buchnera | `resolve_abduction.py`'s exclusion comment expanded to state the shared-pathway biology; RESULTS.md corrected to match, and Buchnera reframed as the cross-feeding exemplar rather than a plain auxotroph. |
| 6 — OXCT1 TPM | corrected to 0.46 in both documents. |
| — | figures regenerated from the corrected engine; `demo_standalone.py`/`demo.html` rebuilt (they embedded the stale module as base64). |

**Prose.** `PATHWAY_SATISFIABILITY.md` and `RESULTS.md` both carry an explicit **retraction** of
the dark-matter claim with its two root causes; the GTEx section now states that the satisfiable
set equals `G6PC1 ≥ threshold` and that the credit belongs to curation, not circuit evaluation;
the zonation section states the multi-step block and the floor; `methods.md` documents both
oracle rules. Finding 1's point is now the page's own framing rather than a criticism of it.

**Gene reviews** (all 11 validate; statuses set to `COMPLETE`)

- **G6PC1** — the erroneous `REMOVE` of `GO:0016773` is now `KEEP_AS_NON_CORE`, with the
  phosphohistidine/EC 2.7.1.62 chemistry explained; 6 degenerate `supporting_text` fragments
  replaced with real quotes and 7 deleted where no supporting quote genuinely exists.
- **G6PC2** — created from scratch (was missing entirely despite anchoring the paralog-trap
  claim): notes with inline provenance, every GOA row reviewed, description, core functions.
- **OXCT1** — 4 degenerate quotes replaced, 4 deleted; PMID:9380443 fetched, verified
  ("SCOT was detected in all tissues except liver") and added with a `reference_review`.
- **ACAT1** — reversed thiolysis/CoA chemistry corrected; the missing second `GO:0016453`
  GOA row added.
- **LDHB/LDHA/GPD1/PC** — over-general parents moved to `MODIFY` + replacement terms; LDHA's
  self-contradicting mitochondrion IBA changed to `KEEP_AS_NON_CORE`; GPD1's oxidative
  (gluconeogenic) direction properly represented; borrowed `IBA`/`IEA` provenance stripped
  from `NEW` entries.
- **Conventions harmonised** across the ketolysis and gate genes (over-general parents →
  `MODIFY`; `identical protein binding` → `MARK_AS_OVER_ANNOTATED`); stray
  `</content></invoke>` artifacts removed from the G6PC1 and SLC37A4 notes.
- **`modules/ketone_body_oxidation.yaml`** — "essentially irreversible" softened to distinguish
  thermodynamic reversibility from net physiological directionality, matching the OXCT1 review.

Not done: the human liver-zonation oracle (still mouse orthologs) remains the project's own
stated next step, and is out of scope for a review pass.

## What holds up

Worth stating plainly, because most of the above is critical:

- The **framing** — that metazoan pathway presence/absence is the wrong question and context
  resolution is the right one — is correct and well argued, and the background survey of the
  hole-filling literature is accurate and fair.
- The **architecture** (pure-logic core, swappable oracle, no biological data in the engine) is
  a good design and is genuinely reused across four contexts unchanged.
- The **eukaryotic ketolysis result is the strongest in the project**: OXCT1 really is the one
  ketolysis enzyme the liver lacks, the expression separation is ~100×, and the conclusion is
  correct and non-trivially derived.
- The **`abduce()` hypothesis set is well designed** — in both cases where the project's prose
  goes wrong (M. jannaschii, Buchnera), the correct explanation was already in the emitted
  hypothesis list. The machinery is more trustworthy than the write-up.
- The **epistemics section is honest** about presence ≠ flux and the mouse-ortholog caveat, and
  the refusal to fabricate a human zonation oracle is the right call.
