# Can an autonomous agent run a COBRApy job? (OpenScientist probe)

**Question behind the probe.** Chowdhury et al. 2026 (ChatGEM, bioRxiv
[10.64898/2026.07.20.739662](https://doi.org/10.64898/2026.07.20.739662)) build a bespoke
multi-agent platform (ADEPT: Keycloak, PostgreSQL, Redis, ChromaDB, MCP tool servers, A2A
federation) plus a RAG corpus of 52 curated COBRApy scripts, and report that RAG grounding
lifts a mean Overall Performance Score from 2.63 to 4.20 across three GEM tasks. How much of
that stack is load-bearing? This probe asks whether a *general-purpose* autonomous research
agent, with no GEM-specific RAG corpus and no bespoke framework, can execute the same class
of task.

The task is the analogue of ChatGEM's benchmark tier 1 (FBA + targeted knockout), chosen
because this project already holds a **held-out answer** for it
([`../../METABOLIC_MODEL_ANALYSIS.md`](../METABOLIC_MODEL_ANALYSIS.md), "FBA Experiment:
Validating Annotation Error Impact"): in published iML1515 an `rbsD` knockout has no effect
on ribose growth, while in a model where rbsD is represented as D-ribose pyranase the
knockout is lethal. The prompt ([`cobrapy_rbsD_task.md`](cobrapy_rbsD_task.md)) asks for the
numbers neutrally and never states which way the result should come out.

## What was run

```bash
uv run deep-research-client -v research \
  --template projects/METABOLIC_MODEL_ANALYSIS/openscientist/cobrapy_rbsD_task.md \
  --provider openscientist \
  --output projects/METABOLIC_MODEL_ANALYSIS/openscientist/rbsD-fba-openscientist.md \
  --param max_iterations=3 --param timeout=7200
```

Job `9e841c7f-3045-4451-a058-d92e6b95bdd9`, 3 iterations, 1549 s wall clock.
Report: [`rbsD-fba-openscientist.md`](rbsD-fba-openscientist.md).

## Verdict: it ran the job, and every checkable number replicates

The run reported that COBRApy is not importable inside its `execute_code` sandbox (import
allowlist), so it `pip install`-ed cobra and executed in a subprocess — i.e. it routed around
a sandbox restriction rather than giving up or faking a result.

Independent replication ([`verify_rbsD_fba.py`](verify_rbsD_fba.py), run in a throwaway venv;
`cobra` is deliberately **not** a repo dependency):

| Quantity | OpenScientist | Local replication | Match |
|---|---|---|---|
| iML1515 md5 | `9579313bc1458acf4ef0ec44bf852ede` | `9579313bc1458acf4ef0ec44bf852ede` | ✓ |
| iML1515 sha256 | `b0f9199f0487…55fbf5` | `b0f9199f0487…55fbf5` | ✓ |
| model size | 2712 rxn / 1877 met / 1516 genes | 2712 / 1877 / 1516 | ✓ |
| cobra version / solver | 0.32.1 / GLPK via optlang | 0.32.1 / `optlang.glpk_interface` | ✓ |
| glucose baseline WT | 0.876997 | 0.876997 | ✓ |
| ribose WT (both variants) | 0.688913 | 0.688913 | ✓ |
| **(a) published, b3748 KO** | **0.688913 (KO/WT 1.000)** | **0.688913 (KO/WT 1.000)** | ✓ |
| **(b) reannotated, b3748 KO** | **0.000000 (KO/WT 0.000)** | **0.000000 (KO/WT 0.000)** | ✓ |
| ALT 1 (RBK anomer-agnostic) | 1.000 | 1.000 | ✓ |
| no-carbon control | 0.000000 | 0.000000 (infeasible) | ✓ |

The `RIBabcpp` GPR it quoted is verbatim correct, including the detail that carries the whole
result — `b3748` sits inside **one of three OR branches**, so deleting it alone kills zero
reactions in the published model. It also correctly identified `RBK` (GPR `b3752`) as
untouched by the deletion. This matches the held-out conclusion in the project page, reached
without being told it.

**It added something the project page does not have.** Unprompted, it ran a sensitivity
analysis showing the essentiality result *hinges on ribokinase being anomer-specific*: if
`RBK` is left able to phosphorylate `rib__D_c` directly, the pyranase carries no obligatory
flux and the knockout is non-lethal again (KO/WT = 1.0). It also bracketed a gene-less
spontaneous-mutarotation route at several caps (KO/WT 0.014 → 0.481 → 1.0). That is the
correct epistemic caveat: the "lethal" result is a property of the modelling choice, not a
free-standing fact. The project page currently states the lethality without that caveat.

## Where it fell short

1. **Executed-code provenance was not delivered.** The prompt required verbatim code plus
   stdout. The report *names* artifacts (`cobra_iML1515_rbsD.py`, `cobra_output.txt`,
   `fba_rbsD_iML1515.py`, `cobra_alternatives.py`) but only `final_report.html` and
   `final_report.pdf` came back through the client's artifact endpoint. Nothing in the report
   was locally checkable on delivery — which is exactly why `verify_rbsD_fba.py` exists. The
   numbers turned out to be right, but that was established by re-running, not by the report.
2. **It missed the primary reference this repo already holds.** It wrote that "Ryu/Kim,
   *J. Biol. Chem.* 2004" was "not retrievable through this PubMed index". According to
   PubMed that paper is PMID:15060078,
   [DOI](https://doi.org/10.1074/jbc.M402016200) — the paper that established RbsD as the
   ribose pyranase, and the reference already cited on the project page. Worse for its own
   argument: that abstract states "the anomeric exchange of only ribofuranose, not
   ribopyranose, occurs spontaneously in solution", which *undercuts* the run's own hedge
   that a real Δ*rbsD* strain grows slowly via spontaneous mutarotation.
3. **Citation weight is overstated in two places** (per the repo's `reference_review`
   distinctions — the quotes are verbatim, but what they support is weaker than claimed):
   - PMID:23651393, [DOI](https://doi.org/10.1111/1574-6968.12172) — the quoted split
     ("RbsABC forms the ABC-type high-affinity d-ribose transporter, while RbsD and RbsK are
     involved in the conversion of d-ribose into d-ribose 5-phosphate") is verbatim, but it is
     *background prose in the abstract* of a paper about RbsR regulation of purine nucleotide
     synthesis, not a result of that paper. The run called it "the primary *E. coli*
     literature". Review-level support, not experimental.
   - PMID:33129664, [DOI](https://doi.org/10.1016/j.micres.2020.126625) — the quote is
     ellipsis-stitched across two sentences and would fail this repo's verbatim
     `supporting_text` substring check. The elision also hides that the source attributes the
     no-growth phenotype to "absence of ribose pyranase rbsD … **and absence of or mutations
     in numerous other genes**". It is a correlative comparative-genomics observation in
     *Fructilactobacillus sanfranciscensis*, not *E. coli*.
   - PMID:21276853, [DOI](https://doi.org/10.1016/j.jsb.2011.01.007) — verbatim and fairly
     characterised as mechanism support, though the paper is about a *S. aureus* homolog.

## Bearing on the "is ChatGEM overkill?" question

A general-purpose agent with **no GEM-specific RAG corpus, no curated script library, and no
bespoke platform** produced a correct, cross-validated, caveat-aware answer to a tier-1
ChatGEM task in 26 minutes, including a sensitivity analysis nobody asked for. That is
evidence that the ADEPT apparatus is deployment infrastructure rather than scientific method,
and that the 52-script RAG corpus — the part of ChatGEM that actually moved the score — is
substitutable by a well-scoped prompt for tasks of this complexity. It says nothing about
their tier-2/3 tasks (OptKnock, ecOptMDFPathway), which were not tested here.

It also sharpens the criticism of ChatGEM's evaluation. Their only quality gate is an LLM
judge scoring code style (Coding Accuracy / Code Completeness → OPS). That gate would have
scored this run highly **and would not have caught either real defect**: the undelivered code
provenance, or the miscited literature. Both were caught by deterministic checks — re-running
the model, and verifying quotes against PubMed — which is the verification posture this repo
already uses for annotations and does not yet use for its own metabolic-model work.

**Concrete follow-up for this project:** the FBA experiment on the project page has the same
gap this run did — its script and corrected model (`fba_annotation_experiment.py`,
`iML1515_with_pyranase.json`) are referenced but not committed. `verify_rbsD_fba.py` closes
that gap for the rbsD case and should be extended to the glgX case.
