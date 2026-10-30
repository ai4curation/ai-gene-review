# Human ribosome-associated quality control module — curation notes

## 2026-10-30 — initial build (issue #3952)

Built the module for
[#3952](https://github.com/ai4curation/ai-gene-review/issues/3952), which asked
for two things: an RQC module spanning collision sensing, splitting and
nascent-chain handling, and a cross-check of the six production GO-CAMs that
already model parts of the pathway against the curated gene reviews. No gene
fetching was needed — all thirteen candidates on
[RIBOSOME_QUALITY_CONTROL](../projects/RIBOSOME_QUALITY_CONTROL.md) already have
complete reviews from the Proteostasis batches.

### Scope

`CONCRETE`, human. The issue asks for "the human ribosome quality control
module" and the project page names *Homo sapiens* as the primary model species,
so this is a deliberately concrete instance rather than a reusable motif. The
pathway is deeply conserved (Hel2, Mbf1, Dom34-Hbs1, Rqc2, Ltn1, Rqc1, Vms1,
Cdc48), and the yeast counterpart is modelled in
`gomodel:63f809ec00000635`; the taxon descriptor says so without claiming
identical composition elsewhere. Participants use `GENE_PRODUCT` and
`PROTEIN_COMPLEX` selectors with UniProt groundings rather than PANTHER
families, which follows from the concrete scope.

### Where the molecular functions came from

Every `function` in the module is the participant's own reviewed core function,
read out of `genes/human/<GENE>/<GENE>-ai-review.yaml`, not out of GOA. The
module QC function-consistency check reports `CORE_SUPPORTED` for all 19
grounded functions (the twentieth entry is the complex-wide activity of the RQC
complex annoton, which has no single UniProt participant to compare against).
TCF25 is the one member with no molecular function of its own: its review records
`contributes_to_molecular_function: GO:0061630`, so it is modelled as a
role-bearing `active_unit` of the RQC complex with a `role` and no `function`.

### Composition and boundary

Six ordered parts:

1. **Collision sensing** — ZNF598 sensor activity and E3 activity, EDF1 40S
   binding.
2. **Initiation repression** (optional) — GIGYF2 adaptor, EIF4E2 cap binding,
   ZNF598 protein-RNA adaptor activity.
3. **Subunit dissociation** — a `ONE_OR_MORE` variant set over two routes: the
   ubiquitin-dependent RQT/ASCC route and the A-site-vacancy
   PELO-HBS1L-ABCE1 route.
4. **RQC complex** — NEMF/LTN1/TCF25 ubiquitination, plus NEMF CAT tailing.
5. **Peptidyl-tRNA release** — ANKZF1.
6. **Nascent-chain extraction** — VCP/p97.

EIF4E2 was added beyond the project page's thirteen genes because the GIGYF2 arm
is not a complete repression step without the cap-binding protein it recruits;
its review already exists. ASCC1 and TRIP4 are named inside the RQT complex
descriptor but carry no annoton, because neither has a review here yet. The SKI
complex, KLHDC10, ELAC1 and TRNT1 appear in the cited GO-CAMs and are recorded
only as evidence and boundary prose.

The variant set is `ONE_OR_MORE` rather than `EXACTLY_ONE` deliberately: the two
routes converge on the same 60S-peptidyl-tRNA product, and two of the cited
models (`63f809ec00000512`, `63f809ec00000560`) place ABCE1 and ASCC3 in a single
dissociation step, so treating the routes as mutually exclusive would contradict
curated models.

### GO-CAM cross-check (the second task in #3952)

All six human production models were read against the reviews. Agreements:
ZNF598 `GO:0170011`/`GO:0061630`, ASCC2 `GO:0070530`, ASCC3 `GO:0016887`, PELO
`GO:0170011`, HBS1L `GO:0003924`, NEMF `GO:0043023`/`GO:1904678`, LTN1
`GO:0061630`, EIF4E2 `GO:0000340`.

Three divergences, recorded in the module `notes` rather than resolved
unilaterally:

| Model | Asserted | Review says | Module follows |
| --- | --- | --- | --- |
| `63e5937500001279`, `63f809ec00000512`, `63f809ec00000560` | ABCE1 `GO:0017111` ribonucleoside triphosphate phosphatase activity | core function is the child `GO:0016887` ATP hydrolysis activity | the review |
| `63f809ec00000701` | ANKZF1 `GO:0004521` RNA endonuclease activity | that GOA row is `MODIFY` → `GO:0004549` tRNA-specific ribonuclease activity (substrate is the tRNA acceptor arm) | the review; the same refinement would apply to the model |
| `63e5937500000997` | ZNF598 `GO:0140517` protein-RNA adaptor activity | retained as `KEEP_AS_NON_CORE`, secondary to the ligase role | keeps it, in the repression node, flagged non-core |

Three coverage gaps in the model set, as distinct from disagreements. **EDF1** is
in none of the six, although it is a reviewed collision sensor with a
cryo-EM-resolved 40S site ([PMID:32744497](https://pubmed.ncbi.nlm.nih.gov/32744497/)).
**TCF25** is in none, although it is a reviewed RQC complex subunit that sets the
K48 linkage ([PMID:30244831](https://pubmed.ncbi.nlm.nih.gov/30244831/)).
**VCP** is in none of the human models, although the yeast
`gomodel:63f809ec00000635` includes CDC48 in exactly this role. These are
curation gaps in the models, not biological uncertainty, so they are notes rather
than `knowledge_gaps`.

### Knowledge gaps

Three, each anchored to a verbatim admission of ignorance in a cached
publication, and each closable only by new experiments:

- the mechanism by which the ASCC3 helicase converts ATP hydrolysis into subunit
  separation ([PMID:32579943](https://pubmed.ncbi.nlm.nih.gov/32579943/),
  Discussion);
- the mechanism of VCP/p97 extraction of the ubiquitinated nascent chain from the
  60S subunit, and what TCF25 and NEMF contribute to it
  ([PMID:25578875](https://pubmed.ncbi.nlm.nih.gov/25578875/), Discussion);
- how TCF25 imposes K48 linkage specificity, and where it sits on the RNC
  ([PMID:30244831](https://pubmed.ncbi.nlm.nih.gov/30244831/), Introduction).

### Outstanding

- No module-level deep research report exists yet
  (`module_deep_research: has_deep_research: false`). Generate one with
  `just module-deep-research-perplexity ribosome-quality-control` when provider
  credentials are available; do not hand-write a `-deep-research-*.md` file.
- ASCC1 and TRIP4 have no gene reviews. Reviewing them would let the RQT complex
  descriptor carry all four subunits as active units.
- The three GO-CAM divergences above are candidates for an upstream report.
