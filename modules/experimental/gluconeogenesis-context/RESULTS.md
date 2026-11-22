# Expression-grounded pathway satisfiability: human gluconeogenesis

**Result: the textbook set of gluconeogenic tissues — and the metabolic gate that
defines it — is *derived*, not looked up, purely from pathway logic + tissue
expression.**

This is a first, self-contained demonstration of *context-resolved pathway
satisfiability* in a eukaryote. In microbes (GapMind) the question is "does the
**genome** encode each step?". In a metazoan every cell has the whole genome, so
the discriminating variable is **expression**: "is each isozyme **expressed** in
this tissue?". This prototype evaluates the human gluconeogenesis module against
GTEx v8 tissue expression and resolves which route is active where.

## What it does

1. **`src/ai_gene_review/module_logic.py`** compiles a `ModuleReview` YAML into a monotone boolean
   circuit — `parts`/`annotons` → AND, `variant_sets` → OR — then enumerates the
   *routes* (one choice per variant set) and the *AND-core* (atoms required by
   every route = gate candidates). Pure logic, no data dependency, doctested.
2. **`gtex_oracle.py`** fetches GTEx v8 median TPM per tissue for each isozyme
   (resolving symbol → versioned GENCODE id; alias-aware, e.g. `G6PC1`→`G6PC` for
   GENCODE v26) and caches a gene × tissue matrix (`cache/gtex_medians.tsv`).
3. **`resolve_context.py`** marks each atom expressed/absent per tissue
   (median TPM ≥ threshold), evaluates the circuit, and reports satisfiable
   tissues + the missing gate atom for the rest.

## The result (threshold: median TPM ≥ 1)

```
Routes through the module: 4
Gate (atoms required by every route): ['PC', 'G6PC1', 'SLC37A4']

SATISFIABLE in exactly: Liver, Kidney_Cortex, Small_Intestine_Terminal_Ileum
  (each realises 2 routes: PCK1 or PCK2 × FBP1; never the muscle isozyme FBP2)

NON-gluconeogenic tissues (Muscle, Brain, Heart, Blood, Adipose, Lung, …):
  all fail at the SAME gate atom -> G6PC1

Validation vs textbook gluconeogenic tissues:
  recovered = expected = {Liver, Kidney_Cortex, Small_Intestine}   (no false +, no misses)
```

So the engine independently recovers that **gluconeogenesis is liver / kidney-cortex
/ intestine**, that the **terminal G6PC1·SLC37A4 ER system is the gate** (which is
*why* muscle and brain cannot release free glucose), and that the realised route
uses **FBP1, not the muscle FBP2** isozyme.

### How much of this is the circuit? (honestly: none of it, here)

The satisfiable set above is *exactly* `G6PC1 ≥ threshold`, at every threshold in the
sweep. Counting how many of the 54 tissues each atom passes at the 1 TPM bar:

```
PCK2, SLC37A4, G6PC3  54/54      FBP1  42/54      FBP2   5/54
PC                    53/54      PCK1  16/54      G6PC1  3/54   <- the only discriminating atom
```

Every non-`G6PC1` atom is either near-ubiquitous or shielded by an OR branch that is,
so a one-line single-gene filter reproduces the whole figure. The boolean circuit adds
no discriminating power in *this* module. That is not a defect of the engine — it is
what a correct engine should report for a pathway with one tissue-restricted step — but
the result must not be sold as circuit evaluation recovering textbook biology. It is
**curation** recovering textbook biology (see next section). For a case where the
circuit genuinely does the work, see the substrate-resolved module below, where adding
the glycerol branch changes the AND-core.

### It resists the paralog trap — because a curator said so

`G6PC3` ("G6Pase-β") is expressed in essentially every tissue (10–40 TPM). A naive
"is *some* glucose-6-phosphatase paralog expressed?" rule would wrongly call most
tissues gluconeogenic. The module grounds the gluconeogenic terminal step specifically
to **G6PC1**, with `G6PC2`/`G6PC3` recorded as a *paralog trap* in the module notes, so
they cannot satisfy the gate. This is the eukaryotic form of the "permissibility ≠
presence" / paralog-overannotation caution.

Worth being precise about where that exclusion comes from: it is a **hand-written
curator judgement in the module YAML**, not something the engine or the expression data
derives — and it is not derivable from GOA either, since the curated `G6PC3` review
retains `GO:0006094` gluconeogenesis (as `KEEP_AS_NON_CORE`) and credits intracellular
glucose production. A module auto-built from GOA would admit `G6PC3` for the terminal
step and call most tissues gluconeogenic. The paralog trap is therefore a genuine
argument *for curated modules*, which is a stronger claim than an engine result.

### The gate is graded (and that matches physiology)

| threshold (median TPM) | satisfiable tissues |
|---|---|
| ≥ 1  | Liver, Kidney_Cortex, Small_Intestine |
| ≥ 5  | Liver, Kidney_Cortex |
| ≥ 10 | Liver |

G6PC1 is 169 TPM in liver, 5.6 in kidney cortex, 2.8 in intestine — so the order in
which tissues drop out as the bar rises recapitulates their known quantitative
contribution to gluconeogenesis (liver dominant, kidney secondary, intestine minor).

## Same engine, one scale down: intra-liver zonation

The bulk-tissue result says liver does gluconeogenesis. But the liver is not
homogeneous: hepatocytes are organised along the porto-central lobule axis, and
gluconeogenesis is known to be **periportal**. Reusing the *identical* circuit
engine with a different oracle — the reconstructed nine-layer zonation profiles of
Halpern et al. 2017 (Nature, PMID:28166538, Supplementary Table S3) — resolves
satisfiability *within* the liver, per lobule layer.

The porto-central orientation is **inferred from the data**, not assumed: landmark
genes (pericentral Glul/Cyp2e1/Oat; periportal Ass1/Asl/Aldob) place the periportal
pole at Layer 9. The gluconeogenic genes themselves are not used to orient, so the
result is a genuine derivation, not a circular re-statement.

```
Periportal pole inferred at Layer 9 (opposite end = pericentral)
Gate atoms (required by all routes): ['PC', 'G6PC1', 'SLC37A4']

layer  zone         gluconeogenesis  missing-gate  all-failing-steps
  L1   pericentral  blocked          ['G6PC1']     ['pepck_step','fbpase_step','glucose_release_step']
  L2   pericentral  blocked          []            ['fbpase_step']
  L3   pericentral  blocked          []            ['fbpase_step']
  L4-9 mid/periportal  SATISFIABLE   []            []

validation:  periportal pole (L9) satisfiable = True
             pericentral pole (L1) satisfiable = False

threshold sweep (rel = profile/peak, with absolute floor):  L1=pericentral .. L9=periportal
  rel>=0.3   .########   layers 2-9
  rel>=0.5   ...######   layers 4-9
  rel>=0.7   ....#####   layers 5-9
  rel>=0.9   ......###   layers 7-9   (periportal third only)
```

**Gluconeogenesis is restricted to the periportal and mid lobule, blocked in the
pericentral third.** As the relative-expression bar is raised the satisfiable zone
contracts monotonically toward the periportal pole — the graded, periportal-restricted
picture of hepatic gluconeogenesis, recovered from logic + measured zonation alone.

Two corrections to how this was previously reported (see
`projects/PATHWAY_SATISFIABILITY/REVIEW.md`):

**The block is multi-step, not single-gate.** L1 fails at `pepck_step`, `fbpase_step`
*and* `glucose_release_step` at once; L2–L3 fail at `fbpase_step` only — a step where
`missing_gate` is empty, because FBPase is not a core atom. The earlier write-up claimed
"the same gate atom, G6PC1, operates at two scales", which was an artifact of reporting
only `core_atoms` and filtering out the other failures. The resolver now prints every
failing step. G6PC1 is *a* reason the pericentral pole is blocked, not the reason.

**Per-gene peak normalisation needed an absolute floor.** `relative_profile` divides each
gene by its own maximum, which discards absolute abundance entirely — so `Fbp2` (max
1.07e-06, i.e. not expressed by mouse liver) reached relative 1.0 at its own peak and
*satisfied the FBPase step* in layers 2–4, rescuing layers that `Fbp1` could not carry.
That is the same paralog trap the terminal step is deliberately grounded against,
recurring one level down. `zonation_oracle.expressed()` now requires both the relative
threshold and an absolute floor of 1e-5; the floor sits inside a 33-fold empty gap
(highest "off" gene 3.9e-06, lowest genuinely-expressed 1.3e-04), so any value in
~[4e-6, 1.2e-4] gives the same answer. With the floor the blocked zone grows from L1 to
L1–L3 and the sweep becomes genuinely monotonic — a cleaner and more defensible result
than the one it replaces.

(Data note: Halpern Table S3 is mouse; the human module symbols are mapped to mouse
orthologs — `G6PC1`→`G6pc`, `PCK1`→`Pck1`, `PC`→`Pcx`, etc. The large raw download
is re-fetched on demand via Europe PMC; only the 15-gene derived matrix
`cache/halpern_zonation.tsv` is committed.)

## Which precursor? Substrate-resolved routes

`gluconeogenesis_human_substrates.yaml` makes the carbon source explicit. Lactate
(via LDHA/LDHB) and the amino acid alanine (via GPT/GPT2) enter as **pyruvate** and
so need the PC + PEPCK carboxylation backbone; **glycerol** (via GK + GPD1) enters at
dihydroxyacetone phosphate, *bypassing PC and PEPCK*. All routes converge on the
shared FBPase and terminal G6PC1·SLC37A4 gate. Consequence, recovered automatically:

```
Routes: 18   Universal gate (atoms in EVERY route): ['G6PC1', 'SLC37A4']
```

Because glycerol skips the carboxylation arm, **PC is no longer universal** — it drops
out of the AND-core, leaving the terminal ER system as the single gate shared by all
precursor routes. Resolving against GTEx then answers *which precursor each tissue can
use* (not just whether it can make glucose):

```
tissue                      precursors                 capacity (lac / ala / gly, TPM)
Liver                       lactate,alanine,glycerol   243 / 128 / 14
Kidney_Cortex               lactate,alanine,glycerol   622 /  17 /  7
Small_Intestine             lactate,alanine,glycerol   232 /  19 /  7
Muscle/Brain/Adipose        — (gated at terminal G6PC1·SLC37A4 regardless of precursor)
```

All three gluconeogenic tissues are equipped for all three precursors, but with
physiologically faithful skews: **kidney cortex is lactate-dominant** (LDHB ≈ 620 TPM)
while **liver has by far the greatest alanine capacity** (GPT ≈ 128 vs ~17), matching
the liver's central role in the alanine cycle. Gated tissues cannot release free
glucose from *any* precursor — the precursor question is moot once the terminal gate
fails.

### Note on the human zonation oracle

Removing the mouse-ortholog caveat on the zonation result would need a **human**
gene×zone matrix. The relevant human studies (e.g. the Nature 2026 live-donor liver
spatial atlas; GEO GSE239480) publish raw spatial/snRNA data that require a full
zonation-reconstruction pipeline rather than a ready-to-parse table, so a faithful
human zonation oracle is not buildable from a single fetch here — and fabricating one
would violate the project's "never invent data" rule. The mouse Halpern result stands
as the zonation evidence; the human spatial atlas is the validation target. The
substrate extension above was built instead because it is fully grounded in human
GTEx data already in hand.

## Same engine, the other kingdom: GapMind-style genome reconstruction

The expression oracles answer "is this isozyme *expressed* in this context?". In a
microbe the question reverts to GapMind's: "is this step's ortholog *encoded* in this
genome?". The **same circuit engine** handles it — only the oracle changes. The
template `modules/methionine_biosynthesis.yaml` defines L-methionine biosynthesis from
homoserine with an alternative at every step (acylation metA|metX; sulfur incorporation
trans-sulfuration metB+metC | direct sulfhydrylation metY; methylation metE|metH), so no
enzyme is universal. `kegg_oracle.py` decides per-genome step presence via KEGG Orthology
(the step→KO table is the oracle's "step definitions", exactly GapMind's split between a
pathway and its candidate definitions), and `resolve_genomes.py` reconstructs the pathway:

```
[FOUND] eco  E. coli K-12        metA(succinyl) | trans-sulfuration | metE or metH   (2 routes)
[FOUND] bsu  B. subtilis 168     metA(succinyl) | trans-sulfuration | metE           (1 route)
[FOUND] hin  H. influenzae Rd    metX(ACETYL)   | trans-sulfuration | metE           (1 route)
[FOUND] cgl  C. glutamicum       metX(acetyl)   | DIRECT (metY)     | metE or metH   (2 routes)
[FOUND] syn  Synechocystis 6803  aspartate-semialdehyde sulfurtransfer | metH        (1 route)
[FOUND] mja  M. jannaschii       aspartate-semialdehyde sulfurtransfer | metE        (1 route)
[GAP]   buc  Buchnera aphidicola only metE present -> missing step: homocysteine_formation
[GAP]   rpr  Rickettsia prowazekii nothing encoded -> homocysteine_formation, methylation
```

Recovered automatically, matching known biology:

* **Route selection differs by genome.** *H. influenzae* uses the *acetyl* acylation route
  (metX), not the succinyl route (metA) of *E. coli*; *C. glutamicum* uses *direct
  sulfhydrylation* (metY). Each genome's encoded route is the one the engine reports.
* **OR really matters.** *C. glutamicum* has metB but **lacks metC**, so its
  trans-sulfuration branch is incomplete — yet the pathway is still FOUND because the engine
  routes through the alternative direct-sulfhydrylation branch (metY). A naive "all of metB,
  metC" check would have produced a false gap.
* **A whole alternative entry, not just an alternative enzyme.** *Synechocystis* and
  *M. jannaschii* encode **no** acyltransferase and **no** O-acyl-homoserine sulfhydrylase.
  They reach homocysteine directly from L-aspartate semialdehyde via the two-subunit
  sulfurtransferase K23975+K23976 (`syn:slr0689`/`slr2059`, `mja:MJ_0100`/`MJ_0099`;
  PMID:25938369), bypassing homoserine entirely. The module represents this as a variant of
  the whole homocysteine-formation step rather than of any single enzyme.
* **Gap detection.** *Rickettsia prowazekii* encodes nothing in the pathway and is an obligate
  intracellular methionine auxotroph — the engine correctly predicts the auxotrophy.
  *Buchnera aphidicola* (a genome-reduced aphid endosymbiont) encodes only metE, and the
  engine flags `homocysteine_formation` as the gap. **Do not read Buchnera as a plain
  auxotroph**: its methionine pathway is *shared* with the aphid host — it retains the
  terminal MetE step (the only amino-acid biosynthetic gene keeping its ancestral metR
  regulator) and the consortium provisions methionine *to* the host, with earlier
  intermediates supplied collaboratively. It is the natural illustration of the "not
  cell-autonomous / cross-feeding" hypothesis, which is why `resolve_abduction.py` asserts no
  phenotype for it either way.

`unsatisfied_steps()` (the GapMind "which required step is missing" diagnostic) is now a
first-class engine primitive in `src/ai_gene_review/module_logic.py`. The upshot: one
satisfiability core spans **prokaryote genome-presence and eukaryote expression-gating** —
the original framing, demonstrated end to end.

## Abduction: a gap is a hypothesis, not a verdict

A missing step only *means* something once you know whether the pathway is actually
running. `abduce()` (engine primitive) crosses circuit satisfiability with an
**independent** activity claim — here the organism's documented growth phenotype on
defined media, which says nothing about its gene content. `resolve_abduction.py` runs
this for methionine biosynthesis:

```
CONSISTENT_ACTIVE   eco, bsu, cgl, syn, mja   prototrophs, pathway reconstructable  (explained)
ABDUCTION_TARGET    (none)
CONSISTENT_INACTIVE rpr                       auxotroph; gap correctly predicts it
```

Every prototroph in the panel is reconstructable and the only gap is a genuine auxotroph,
so there are **no** microbial abduction targets. That is the correct answer, and getting
there required retracting the previous one.

#### Retracted: *Synechocystis* / *M. jannaschii* as "metabolic dark matter"

An earlier version of this document reported `syn` and `mja` as `ABDUCTION_TARGET`s —
autotrophs that make methionine while encoding no canonical acylation or
sulfur-incorporation enzyme — and called them "real metabolic dark matter" warranting a
search for an unannotated enzyme. **That was a false positive, and the fault was in this
project, not in the annotation.**

Both organisms encode **K23975** (L-aspartate semialdehyde sulfurtransferase, EC 2.8.1.16)
and its iron–sulfur partner **K23976**, *in KEGG* — the same database this oracle queries:
`syn:slr0689`/`slr2059` and `mja:MJ_0100`/`MJ_0099`. The enzyme makes homocysteine directly
from aspartate semialdehyde and sulfide, bypassing homoserine and its acylation altogether
(PMID:25938369, *Biochemistry* 2015). Two compounding causes:

1. **Module scope.** The template was titled "from homoserine" and modelled only the
   O-acyl-homoserine entry, so an organism using the direct route could not be represented
   as satisfiable at all — a gap was structurally guaranteed.
2. **Oracle coverage, failing silently.** `STEP_KO` listed seven KOs and omitted these two,
   and the predicate returned `False` for any symbol it could not map. "Not in my lookup
   table" and "not in this genome" were therefore indistinguishable. `metZ` was in the same
   state — a module variant with no KO entry — and only escaped notice because it happens to
   be absent from all eight genomes anyway.

Both are fixed. The module carries the aspartate-semialdehyde route as a variant of the
whole homocysteine-formation step; `STEP_KO` gained K23975/K23976 and metZ; and
`kegg_oracle.holds_for()` now raises `UnmappedStepError` instead of guessing. `syn` and
`mja` resolve to `CONSISTENT_ACTIVE` via the correct route, and every other verdict —
including *Rickettsia*'s auxotrophy — is unchanged. `tests/test_module_logic.py` carries
this as a regression case.

Epistemics, restated with the lesson folded in: the activity column is independent of the
ortholog oracle (growth phenotype, not gene set), so a gap scored against it *can* be a
genuine prediction rather than a circular restatement. But independence of the phenotype
axis does not make the gap axis correct. **A gap is evidence about the model before it is
evidence about the organism**, and must survive two model-side checks before it is treated
as a lead: can the module *represent* the route this organism might use, and does the
oracle *cover* every atom in the module? The engine's hypothesis list already carried the
right answer here — "an alternative route not represented in the module is used" — and the
write-up promoted the most exciting hypothesis over the most likely one.

## Abduction on the eukaryotic side (tissue function vs expression)

The same `abduce()` runs against GTEx, with the independent claim now a *documented
tissue function* rather than a growth phenotype (`resolve_eukaryotic_abduction.py`). A
eukaryotic gap carries an extra meaning microbes lack — a pathway can be split across
organs/cell types — so a new explanation, "not cell-autonomous (intermediate supplied by
another cell/organ)", was added to the hypothesis set.

**Ketone-body oxidation (ketolysis = BDH1 → OXCT1/SCOT → ACAT1):**

```
CONSISTENT_ACTIVE   Heart, Brain, Skeletal muscle, Kidney cortex   (all three enzymes expressed)
CONSISTENT_INACTIVE Liver  -> gap at OXCT1 (SCOT)                (OXCT1 = 0.46 TPM in liver)
```

This is the eukaryotic counterpart of the *Rickettsia* result: the liver gap is **correct**.
OXCT1/SCOT is the one ketolysis enzyme the liver effectively does not express (GTEx liver
median 0.46 TPM — well under any threshold used here, though not literally zero — vs
heart 60, brain 45), so the engine reproduces the textbook molecular reason the liver
**exports** the ketone bodies it makes instead of consuming them — and it pinpoints the exact
enzyme, not just "the pathway".

**Gluconeogenesis at a stringent expression bar (TPM ≥ 5):**

```
CONSISTENT_ACTIVE   Liver, Kidney cortex
ABDUCTION_TARGET    Small intestine -> gap at the terminal G6PC1 step  (intestinal G6PC1 ≈ 3 TPM)
```

Intestinal gluconeogenesis is independently *reported* but genuinely *debated*, precisely
because intestinal glucose-6-phosphatase is low. Asserting it active surfaces it as an
`ABDUCTION_TARGET` at the terminal G6PC1 step, with the four leads (non-canonical enzyme;
unmodelled route; **not cell-autonomous / inter-organ**; or the activity claim itself being
the error). The engine does not adjudicate the controversy — it localises it to one step and
one gene, which is exactly what a reviewer wants.

The gap-as-hypothesis machinery is kingdom-agnostic: the only thing that changes is which
oracle (genome presence vs tissue expression) and which extra explanation (cross-feeding vs
inter-organ) is in play. After the retraction above, the eukaryotic intestinal-gluconeogenesis
case is the one live abduction target in the project — appropriately, since it is a genuine
open question in the literature rather than an artifact of our own model.

## Honest scope / epistemics

- **Expression is used asymmetrically:** absence excludes a route (no enzyme → no
  flux, the strong signal); presence only *permits* (it does not prove flux — protein
  level, allostery, and hormonal state still gate real activity). The satisfiable set
  is therefore an *upper bound* on capacity, not an assertion of active flux.
- **A gap indicts the model first.** Before reading a gap as biology, check that the module
  can *represent* the route the organism might use and that the oracle *covers* every atom
  in the module. Skipping those two checks is what produced the retracted dark-matter
  result. Only the residue is a lead.
- **Oracles must refuse to answer what they cannot answer.** The genome oracle now raises
  `UnmappedStepError` for an atom with no KO rather than returning `False`, because a
  silent default made incomplete coverage look identical to a genome gap.
- **Relative measures need an absolute floor.** Normalising each gene to its own peak
  discards abundance and let an unexpressed isozyme satisfy a step; `zonation_oracle`
  now requires both.
- **In the bulk-tissue module, the circuit is not what discriminates** — the satisfiable
  set equals `G6PC1 ≥ threshold`. The curated grounding of the terminal step is what does
  the work. The substrate-resolved module is where the logic itself changes the answer.
- **The reversible glycolytic trunk** is treated as constitutively satisfiable
  (broadly expressed housekeeping enzymes), so it is never the gate; the
  tissue-restricting logic lives entirely in the bypass reactions, as in biology. Note this
  leaves ~7 enzymes unmodelled, further reducing the number of atoms that could ever gate.
- Bulk-tissue GTEx mixes cell types; the natural next step is single-cell / spatial
  data to derive **periportal zonation** of hepatic gluconeogenesis on the same engine.

## Why this is novel and useful

- KEGG/Reactome pathway-completeness is genome-level — every human cell "has"
  gluconeogenesis. This instead resolves **which route is wired up in which context**
  as a logic problem, and flags the **gate** that explains tissue restriction.
- The gate/abduction framing generalises: where a pathway is *independently known*
  active in a context but a required atom is unexpressed, that is a flagged gap — a
  missed isozyme, a non-canonical route, or a regulation-only explanation.

## Reproduce

```bash
# Engine (from the repo root) — promoted to src/ai_gene_review/module_logic.py
uv run pytest --doctest-modules src/ai_gene_review/module_logic.py   # logic doctests
uv run pytest tests/test_module_logic.py -q                          # engine unit tests
#   route enumeration + gate for a module, ad hoc:
uv run python -c "from ai_gene_review.module_logic import compile_module_file, enumerate_routes, core_atoms; c=compile_module_file('modules/gluconeogenesis_human.yaml'); print(len(enumerate_routes(c)), 'routes; gate', [a.gene_symbol for a in core_atoms(c)])"

# Oracles + per-context resolvers (from this directory)
cd modules/experimental/gluconeogenesis-context
uv run python gtex_oracle.py                          # refresh cache from GTEx v8
uv run python resolve_context.py                      # per-tissue resolution + validation
uv run python resolve_context.py --threshold 5        # graded gate

uv run --with openpyxl python zonation_oracle.py      # fetch/cache Halpern zonation
uv run python resolve_zonation.py                     # per-lobule-layer resolution + sweep

uv run python resolve_substrates.py                   # which precursor can each tissue use?

uv run python kegg_oracle.py                           # cache KEGG ortholog presence per genome
uv run python resolve_genomes.py                       # GapMind-style methionine reconstruction
uv run python resolve_abduction.py                     # microbial gaps vs phenotype -> leads / auxotrophy
uv run python resolve_eukaryotic_abduction.py          # tissue gaps vs function (ketolysis, gluconeogenesis)
```

## Next steps

1. ~~Single-cell / spatial oracle → derive hepatic gluconeogenesis **zonation**.~~
   **Done** (`resolve_zonation.py`): periportal restriction recovered from Halpern 2017.
   Next: a human spatial/scRNA oracle (e.g. the 2025 human-liver spatial atlas) to
   confirm the same zonation directly in human rather than via mouse orthologs.
2. ~~Add the substrate-entry OR-branches (lactate / alanine / glycerol).~~ **Done**
   (`gluconeogenesis_human_substrates.yaml` + `resolve_substrates.py`): glycerol
   bypasses PC/PEPCK, collapsing the universal gate to the terminal step; per-tissue
   precursor capability resolved against GTEx.
3. ~~Promote `module_logic.py` into `src/ai_gene_review/` with pytest coverage.~~
   **Done**: the engine now lives at `src/ai_gene_review/module_logic.py` (frozen
   `Atom`, doctested, mypy-clean) with `tests/test_module_logic.py`; the oracles
   here import it (`from ai_gene_review.module_logic import ...`).
4. ~~Apply the engine to a microbial GapMind-style module (genome-presence oracle)
   to prove the core spans prokaryote→eukaryote.~~ **Done**
   (`modules/methionine_biosynthesis.yaml` + `kegg_oracle.py` + `resolve_genomes.py`):
   route selection and gap/auxotrophy detection across five genomes from KEGG.
5. ~~Wire the "known-active + unexpressed required atom = gap" abduction path and emit
   gaps as reviewable predictions.~~ **Done** (`abduce()` + `resolve_abduction.py`):
   Synechocystis and M. jannaschii surfaced as real methionine "dark matter" leads;
   Rickettsia's gap correctly classified as a predicted auxotrophy.
6. Carry the abduction path to the eukaryotic side: assert a tissue/zone where a pathway
   is independently known active and flag any unexpressed required atom as a lead.
