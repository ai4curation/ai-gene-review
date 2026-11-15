# LPS transport capacity consultation

The reviewed module supports two complete canonical component panels (ECOLI and
PSEPK), plus a partial meningococcal terminal/carrier panel. This audit executes
the production Boolean compiler and supplies a separately documented biological
oracle. It assesses **demonstrated or curated compatible capacity**, not native
transport rates, essentiality in every organism, or universal biological absence.

## Executable checks

From the worktree root:

```sh
uv run python analysis/module_audits/bacterial_lps_transport/capacity-consultation/check_capacity.py
uv run python analysis/module_audits/bacterial_lps_transport/capacity-consultation/check_closure.py
uv run ruff check analysis/module_audits/bacterial_lps_transport/capacity-consultation
```

`check_capacity.py` invokes the actual `ai_gene_review.module_logic.compile_node`,
`iter_atoms`, `core_atoms`, `count_routes`, and `is_satisfied`. It does not replace
the module with a hand-built Boolean graph. Inputs and outputs are `members.json`,
`cases.json`, and `results.json`. `check_closure.py` verifies released consultation
hashes, all seed payloads, protected sources, historical records, quoted evidence,
and the exact H44/76 identity bridges. Its `--draft` option permits the pending
family manifest only for development; a frozen handoff requires final PASS.

The test suite contains 56 cases, 14 model mutations, and seven explicit gate
sensitivities. A separate deliberately naive GO-only oracle demonstrates a false
positive for an unqualified collection of general functions.

## Compiler limits and oracle contract

The compiler produces eight atoms and 12 formal combinations. The three atoms
required by every route are the LptB2FG extractor, LptC anchor, and LptA bridge.
Complex `active_units` are **not** expanded into independent Boolean requirements.
Taxon/context, substrate, physical compatibility, and catalytic energy are not
enforced by the compiler. `EXACTLY_ONE` is evaluated as OR; it does not reject a
context satisfying both alternatives. These combinations are logical branches,
not 12 independently established natural pathways.

The oracle reads the actual module participants and active units and requires:

- Positive, exact reviewed roles, grounded in the current core functions and
  preserved source support. ATP hydrolysis for B, transfer for A/C, and complex
  contribution for F/G/D/E are distinct. Generic ABC activity, LPS binding, or a
  family label alone is insufficient. The M/Y contributions cannot replace D.
- The appropriate distinct F and G participants, an enabling LptB ATPase, and a
  complete matched canonical D/E pair. The B2 stoichiometry uses copies of one
  gene product; two distinct B genes are not required. No universal LptA oligomer
  count is imposed.
- LPS/LOS substrate, a diderm envelope, and positive compatible-interface support.
  The starting substrate is already in the outer inner-membrane leaflet; synthesis,
  MsbA flipping, and O-antigen elaboration do not substitute for any Lpt role.
- A matched panel and the applicable lineage. Each of seven cross-panel component
  replacements fails the licensed profile without positive interface evidence;
  this does not prove that engineered heterologous complementation is impossible.
- For the meningococcal profile, a compatible native bridge context, D and carrier
  H, with the exact H44/76 natural-CDS bridge for the MC58 reference E/H proteins.
  No mere shared species label licenses a strain transfer.

The external terminal test requires a carrier/bridge context as well as the
terminal components. It is not an isolated LptD transport assertion. Terminal
structural capacity can remain true when ATP is unavailable, while the whole
ATP-driven profile is false; neither output asserts ongoing flux.

One mutation, deletion of the explicit A atom, is detected by the production
`core_atoms` contract. Its case results remain protected by the independent
terminal bridge gate, which also requires A. The result file explicitly
separates that structural-contract detection from case-based mutation detection.
The other mutations test erased components, obligatory accessory roles, a forced
Neisseria E requirement, generalized E bypass, and changed activity identities.

## Biological boundaries exercised

| Context | Whole profile | Terminal profile | Interpretation |
| --- | --- | --- | --- |
| ECOLI A/B/C/D/E/F/G | Yes | Yes | Native component roles supported by primary work and curation; no rate prediction. |
| PSEPK A/B/C/D/E/F/G | Yes | Yes | Complete KT2440 reviewed panel; biochemical mechanism is curated ortholog inference, not a new native KT2440 transport assay. |
| ECOLI with M and/or Y | Yes | Yes | Accessory support can enhance terminal work and organization; no universal requirement or quantitative enhancement inferred. |
| H44-compatible D/H/E or D/H | No | Yes | LptE-independent surface detectability in native H44-derived assays; the three reviewed exemplars do not include a complete extractor panel. |
| Isolated D, E, H, or M/Y | No | No | Complex contribution is not autonomous whole-system activity. |
| Missing any canonical A–G component | No | Component-dependent | Canonical profile fails; this is not universal lethality or impossibility. |
| Missing C in the documented suppressor context | No | Yes | PMID:27529623 describes selected LptF-dependent conditional bypass outside the canonical profile. The negative canonical result deliberately does not deny that observation. |
| LPS-free diderm or unqualified family/GO hits | No | No | Native substrate and positive role evidence are not supplied by diderm anatomy or family membership. |

The frozen family tree places Q9RS08 in LptA SF1, Q9RSJ0 in LptB SF10, Q9RVF4
in LptG SF2, and Q9X257 in LptD SF1. Their contexts illustrate why the broad
selectors do not license every member for LPS export. The four substitution
controls do not assert loss of all lipid transport or of every intrinsic
interaction with LPS. Exact current memberships are verified against the frozen
tree snapshot and original tree-source hashes.

## Evidence and identity closure

The closure verifies 19 COMPLETE reviews, all 214 ordered source annotation rows,
and all six active historical NEW proposals. No new-panel NEW assertions were
added. It checks 92 protected seed-source hashes and 40 pre-existing gene-history
files against the frozen commit. It also checks every released file from the
ECOLI, PSEPK, Neisseria, accessory, literature, and family consultations.

All 302 gene/module quotations are matched to their immutable publication or
local source; the nine additional full-text literature quotations are checked
against the separately archived accessed text. These are mechanical provenance
checks alongside the source-specific scientific assessments, not substitutes for
those assessments. The three exact Neisseria protein matches are independently
recomputed from all 2,423 translated CDSs in the archived H44/76 assembly and the
official UniProt JSON sequences. Natural protein identity does not establish
identical expression constructs, native regulation, or a native MC58 phenotype.

The principal evidence limits remain visible:

- PMID:21705335 measures surface accessibility and LptD abundance in H44/76/HB-1
  backgrounds; E dispensability for that endpoint does not establish absence of
  all E contributions. H/C/F/G mutants differ from the E mutant. Viability after
  LPS loss is not evidence of preserved transport.
- PMID:15192148 supports the H44/76 D surface-delivery role through independent
  accessibility/modification assays, not purified isolated-D turnover.
- PMID:41407669 concerns PAO1-LAC proteins expressed in E. coli, with partially
  functional tagged LptB complementation. It does not establish native KT2440
  kinetics. Prior Pa-LptC complementation can depend on elevated LptB expression;
  an absolute cross-species incompatibility claim would be wrong.
- PMID:41285762 and PMID:37821449 support E. coli accessory structure, interactions,
  maturation and conditional cellular roles. M/Y are optional to this capacity
  profile, not biologically inert; structural models are not direct observation
  of each transport stroke.

No gene, module, family, project, publication, provider, or raw source was edited
by this consultation. No member-index refresh, full-corpus run, commit, or push
was performed. The final `handoff.json` freezes this audit and its input closure
against the parent's final module.
