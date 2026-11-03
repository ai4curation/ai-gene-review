# Integrated stress response module — curation notes

Companion to `modules/integrated_stress_response.yaml`. Built for
[issue #3951](https://github.com/ai4curation/ai-gene-review/issues/3951), whose
remaining non-gene work was "Build an ISR module including the OMA1-DELE1
mitochondrial branch". The structural rationale lives in the module's own
`notes:` field; this file records how the module was built, what was checked, and
what is still open.

## Why this is a module and not a gene note

The ISR has the property that makes a reusable module worth writing: four
unrelated inputs are funnelled through one shared mechanism and one shared
output. Writing it per gene would state the shared mechanism five times over
(once per kinase plus once on eIF2S1) and would not record where the branches
converge. The module has five required parts and one optional part, well above
the two-substantive-parts floor in `.claude/skills/module-curation`.

## Boundary decisions

| Decision | Reason |
|---|---|
| Relay only; effector genes excluded | ASNS, amino-acid transporters, chaperone and redox genes are what the output *does*, not steps of the signalling. ASNS is a project candidate and has a COMPLETE review, but asparagine synthase activity is not an ISR step. |
| Mammalia context, human representatives | All five parts, including the DELE1 relay and both PP1 targeting subunits, are established in mammals. The phospho-eIF2α core is far older (yeast runs it with Gcn2 and Gcn4), so the kinase set is a ROUTE set, not a claim that every lineage has four inputs. |
| eIF2 and eIF2B as complex participants with active units | Keeps the regulatory subunit (EIF2S1, Ser51) and the catalytic subunit (EIF2B5/ε) visible to module reasoning. Matches the EIF2B1–EIF2B4 reviews, which assert `contributes_to` GO:0005085 within GO:0005851 rather than the activity itself. |
| GADD34 and CReP as a REALIZER variant set, `ONE_OR_MORE` | Same role, different timing: CReP is constitutive and sets the basal phospho-eIF2α level, GADD34 is ISR-induced and acts late. Both are present in a stressed cell, so `EXACTLY_ONE` would be wrong. |
| Kinase set declared `ROUTE` | All four carry GO:0004694, so the REALIZER inference would otherwise fire. What distinguishes the branches is the input sensed, which is a route distinction. |

## Composition, not duplication

The OMA1→DELE1→HRI relay is already modelled in
[`mitochondrial_upr`](mitochondrial_upr.yaml) as
`mammalian_oma1_dele1_hri_route`, which contains nodes `oma1_dele1_cleavage` and
`dele1_hri_activation`. The HRI branch takes those two nodes by `module_ref`
rather than re-authoring the OMA1 and DELE1 annotons. Both referencing parts are
`optional: true`, because HRI is also activated by heme limitation and by
cytosolic protein misfolding (PMID:31273097), neither of which needs DELE1.
Referencing the two child nodes rather than the whole route node was deliberate:
the route node also carries its own HRI and eIF2α annotons, which would duplicate
this module's parts 1 and 2.

The PERK branch deliberately does **not** use a `module_ref`.
`er_unfolded_protein_response#perk_arm` covers the same chemistry but also
carries its own eIF2α and ATF4 annotons, so including it would duplicate parts 2
and 4. The relationship is recorded in prose on the PERK variant instead.

Compiled logic check (`ai_gene_review.module_logic.compile_module_file`):
15 atom occurrences, 4 core atoms (eIF2, eIF2B, ATF4, PPP1CA), both `module_ref`
targets resolving to nested `OMA1` and `DELE1` atoms, and both optional parts
compiling to `ZERO_OR_MORE` sets.

## The ontology gap at the centre of the pathway

GO has no molecular-function term for the activity of phosphorylated eIF2 toward
eIF2B — which is the mechanistic core of the ISR. The hub annoton therefore
records eIF2's ordinary translation initiation factor activity (GO:0003743) and
states the inhibitory role in `role_description` and on the
`eif2_complex → eif2b_gef` `NEGATIVELY_REGULATES` connection. The same tension is
recorded on the worm `eif-2alpha` annoton of `er_unfolded_protein_response`. This
is an ontology question, not a `knowledge_gaps` entry, per the project rule that
ontology gaps belong in notes or `proposed_new_terms`. It is not raised as a
`proposed_new_terms` entry here because a module document has no such slot;
whoever next reviews human EIF2S1 is the right place to propose it, and the two
open EIF2S1 PRs are the natural home.

GO-CAM curators type EIF2S1 as GO:0160296 *cap-dependent translation initiation
factor activity*. The module uses the parent GO:0003743 because eIF2 acts in both
cap-dependent and IRES-mediated initiation — `gomodel:6606056e00000903` types
EIF2S1 twice, once as GO:0160296 and once as GO:0160297.

## Gene-review coverage at the time of writing (2026-11-03)

Cited as `file:` evidence where a review exists:

- **COMPLETE**: EIF2AK1, EIF2AK3, EIF2AK4, DELE1, OMA1, ATF4, ATF3, GCN1, EIF2B3, ASNS
- **DRAFT**: EIF2B1, EIF2B2, EIF2B4, EIF2B5, EIF2S3
- **No review yet**: EIF2S1 (the hub), EIF2AK2, DDIT3, PPP1R15A, PPP1R15B, EIF2S2, PPP1CA

The six uncovered participants are grounded on verified UniProt accessions and on
production GO-CAM activities, and each such annoton carries a `notes:` field
saying so. Five of the six (EIF2S1, EIF2AK2, DDIT3, PPP1R15A, PPP1R15B) have open
pull requests against #3951 — PRs #5901/#5732/#5722 (EIF2S1, three competing
branches), #5821 (EIF2AK2), #5855 (DDIT3), #5747 (PPP1R15A), #5779 (PPP1R15B).
When those merge, the corresponding annotons should gain `file:` evidence and the
`notes:` disclaimers should be removed. That is curation work, not a knowledge
gap.

## Accession verification

Every UniProt accession in the module was checked against
`rest.uniprot.org` rather than taken from the project page: EIF2AK1 Q9BQI3,
EIF2AK2 P19525, EIF2AK3 Q9NZJ5, EIF2AK4 Q9P2K8, GCN1 Q92616, EIF2S1 P05198,
EIF2S2 P20042, EIF2S3 P41091, EIF2B1 Q14232, EIF2B2 P49770, EIF2B3 Q9NR50,
EIF2B4 Q9UI10, EIF2B5 Q13144, ATF4 P18848, DDIT3 P35638, ATF3 P18847, PPP1R15A
O75807, PPP1R15B Q5SWA1, PPP1CA P62136, OMA1 Q96E52, DELE1 Q14154.

One citation trap worth recording: `PMID:12882984` is **not** the Jousse *et al.*
CReP paper, despite being a plausible-looking 2003 identifier. The CReP paper is
`PMID:14638860` (J Cell Biol 2003;163:767-75), confirmed by PubMed title match
before use. The GADD34 paper is `PMID:11381086`.

## Open biological questions

Two `knowledge_gaps` entries, both `BIOLOGY`/`BP_DARK`, both of the
"a wet-lab experiment would close this" kind:

1. **What sets the adaptive/apoptotic threshold.** The same mark and the same
   ATF4 output end in recovery or in CHOP-driven death. No measured property of
   the relay — phospho-eIF2α stoichiometry, duration, ATF4 or CHOP level — has
   been shown to be the determinant rather than a correlate. Matters because
   ISR-modulating drugs for neurodegeneration and cancer need to know whether to
   raise or lower signalling.
2. **Whether the four branches are interchangeable.** The module models them as
   alternative routes to one mark. Kinase-specific substrates or kinase-specific
   gene programs would make them distinct pathways sharing a hub, which would
   change the variant-set semantics from ROUTE-to-one-output to four separate
   modules.

## Validation run

```
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml \
  -C ModuleReview modules/integrated_stress_response.yaml          # No issues found
uv run python -m ai_gene_review.validation.module_validator \
  modules/integrated_stress_response.yaml                          # passed, 0 warnings
just render-module modules/integrated_stress_response.yaml         # ok
```

All `supporting_text` values were extracted from the cached
`publications/PMID_*.md` files rather than typed from memory, including the
Unicode `eIF2α` forms that appear in PMID:14638860 and PMID:27629041.
