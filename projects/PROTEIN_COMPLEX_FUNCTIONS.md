---
species: [human]
---

# Protein Complex Functions Project

## Overview

This project explores how gene function should be attributed when the experimentally observed
activity is performed by a protein-containing complex rather than by a single polypeptide. The
central question is:

> When a complex has a molecular function, which gene products should receive that function,
> which should receive a `contributes_to` style annotation, and which should instead be annotated
> to assembly, stabilization, localization, regulation, or complex membership?

The project is motivated by recurring annotation problems in large complexes: catalytic or
transport activities are often assigned to all subunits, even when only a catalytic core or
subcomplex directly performs the activity. This can turn complex membership into an apparent
molecular function and can obscure the roles of accessory, regulatory, structural, and assembly
subunits.

## Source Material

- [OXPHOS project](OXPHOS.md) -- working case set for mitochondrial respiratory complexes,
  ATP synthase, mobile carriers, and assembly factors.
- [GO-CAM-modeling issue #1](https://github.com/geneontology/GO-CAM-modeling/issues/1) --
  current GO-CAM discussion of catalytically active OXPHOS subcomplexes inside larger
  complexes. The issue frames the problem as distinguishing catalytic core members from
  accessory or supernumerary subunits when exporting molecular function annotations.
- [GO-CAM call slide deck, 2026-01-27](https://docs.google.com/presentation/d/1TD0w8TNDbzgUoh7M3w3VgpOYYFjDGR55iSrctKMeq1s/edit?slide=id.p#slide=id.p) --
  concrete OXPHOS examples, current GO guidance, Noctua export options, and the
  2026-03-06 proposal to add active-member and accessory/structural-member relations.

## Core Attribution Problem

Protein complexes create a spectrum of attribution cases:

| Level | Appropriate when | Example pattern | Annotation risk |
|-------|------------------|-----------------|-----------------|
| Individual gene product | The purified subunit has the activity, contains the active site, or directly binds substrate/cofactor in a way that defines the function | Catalytic enzyme subunit, receptor ligand-binding chain | Under-annotation if only the whole complex is annotated |
| Catalytic or functional subcomplex | A subset of complex members directly enables the activity, but the complete complex includes additional accessory members | OXPHOS catalytic cores inside larger complexes | Over-annotation if all complex members inherit the activity |
| Whole complex | The activity is an emergent property of the assembled complex and cannot be cleanly attributed to one gene product | Rotary ATP synthase, ribosome, proteasome holoenzyme | Loss of mechanistic detail if every subunit receives the same MF |
| Structural or scaffold subunit | The subunit is needed for architecture, stability, or substrate positioning but is not itself the activity executor | Membrane anchors, stalks, scaffold proteins | False catalytic labels on structural genes |
| Regulatory subunit | The subunit changes activity, assembly state, tissue specificity, or response to conditions | Inhibitory subunits, isoform-specific regulators | Conflating regulation with execution |
| Assembly or maturation factor | The gene product helps build, insert cofactors into, or quality-control the complex but is not part of the mature activity | OXPHOS assembly factors, chaperones | Assigning pathway activity to biogenesis proteins |

The desired output is not a single rule. It is a decision framework that preserves the distinction
between "this gene product performs the function", "this gene product directly contributes to a
complex function", and "loss of this gene product perturbs the function indirectly because the
complex fails to assemble or operate normally".

## Working Principles

1. Do not use complex membership alone as evidence for a molecular function.
2. A subunit can be essential for a complex activity without being the molecular executor of that
   activity.
3. `contributes_to` should be reserved for gene products that directly participate in a complex
   activity, such as catalytic-core subunits, electron-relay subunits, substrate-binding subunits,
   or mechanically coupled subunits whose role is part of the activity mechanism.
4. Accessory and supernumerary subunits should usually be described with more specific roles:
   assembly, stability, regulation, localization, tissue specificity, substrate recruitment, or
   complex organization.
5. Assembly factors should not be annotated to the mature complex activity unless there is direct
   evidence that they remain in the active complex and participate in the activity.
6. If the correct functional unit is a stable catalytic subcomplex but no GO cellular component
   term exists for it, the review should record that modeling gap rather than broadening the
   activity to all members of the larger complex.
7. Gene review summaries should state the attribution level explicitly in `core_functions`, rather
   than hiding the distinction in supporting text.

## GO-CAM and Export Position

The GO-CAM slide deck sharpens the immediate practical problem: OXPHOS complex membership should
export CC and BP annotations broadly enough to preserve complex context, but MF export should not
turn every supernumerary or accessory subunit into a contributor to catalysis.

The most useful near-term model is the proposed relation split:

| Relation in model | Meaning | GPAD export behavior |
|-------------------|---------|----------------------|
| `has active member` | Member directly participates in the activity unit | Export `contributes_to` MF |
| `has accessory/structural member` | Member is part of the complex but not a direct executor of this activity | Do not export MF |
| `has member` | Membership known, active/accessory role not asserted | Do not export MF by default |

This project should treat that as the primary practical target. It preserves the full complex in
GO-CAM, avoids incorrect MF annotations for non-catalytic subunits, and gives curators a manageable
way to model catalytic cores without creating GO cellular-component terms for every catalytic
subcomplex.

For complexes with more than one activity, the activity unit should drive the member role. The same
member can be active for one activity and accessory for another. The ribosome and proteasome are
important test cases: they cannot be represented faithfully by one global "active subunit" list.

Regulatory subunits should usually be modeled as separate activity units causally upstream of the
complex activity, rather than as active members of the catalytic activity itself. For example, an
inhibitor or allosteric subunit may regulate ATP synthase activity without contributing to ATP
synthesis in the same sense as the catalytic beta subunit or proton-channel rotor.

## Decision Questions for Gene Review

Use these questions when reviewing complex-associated genes:

1. What was assayed: purified subunit, reconstituted subcomplex, full complex, membrane fraction,
   cell extract, genetic perturbation, or organismal phenotype?
2. Does the subunit contain the active site, cofactor-binding residues, ligand-binding surface,
   substrate channel, electron-relay group, or mechanical element needed for the activity?
3. Is the subunit present in the mature active complex, or only during assembly and maturation?
4. Does loss of the subunit abolish activity because the activity mechanism is impaired, or because
   the complex fails to assemble, localize, or remain stable?
5. Is the activity distributed across an interface between multiple subunits?
6. Is there a named catalytic core or subcomplex with a consistent composition across species?
7. Does the evidence support the same attribution across paralogs, isoforms, tissues, and species?
8. Would assigning the activity to this gene product improve downstream interpretation, or would it
   inflate a gene set with indirect participants?

## Use Cases and Analysis Impact

### GO curators and GO-CAM modelers

Curators need to know whether a molecular activity should be enabled by a single gene product, a
complex, or a set of directly contributing subunits. For GO-CAMs, the modeling problem is not just
which term to use, but which entity enables the activity and how the activity connects to upstream
and downstream activities.

### Gene review authors

AI gene reviews need to summarize core functions without promoting every phenotype or complex
membership fact to a core molecular function. Complex attribution gives reviewers a disciplined way
to mark catalytic-core roles as core while keeping assembly, structural, or regulatory roles
separate.

### Gene set enrichment and pathway analysis users

If every member of a large complex is annotated to the same catalytic activity, enrichment analyses
can overcount that activity and make an accessory-subunit hit look equivalent to a catalytic-subunit
hit. Better attribution helps analysts distinguish "the pathway is catalytically impaired" from
"the complex may fail to assemble or be regulated incorrectly".

### Variant and disease interpretation users

Clinical and functional genomics users need to know whether a variant affects chemistry, electron
transfer, substrate binding, mechanical coupling, assembly, stability, or regulation. The same
disease phenotype can arise from different mechanistic classes, and annotations should not erase
that distinction.

### Functional prediction and ML benchmark users

Training labels that assign whole-complex activities to all subunits teach models to predict
complex membership rather than molecular role. Evaluation datasets, including function-attribution
benchmarks, need labels that distinguish executor, contributor, regulator, and indirect perturbation
classes.

### Orthology and phylogenetic propagation users

Complexes often conserve membership while redistributing accessory, tissue-specific, or regulatory
roles. PAINT/IBA-style propagation needs guardrails so that catalytic activity is transferred to
orthologous catalytic cores, not to all homologous or co-complex members.

### Database integrators

ComplexPortal, Reactome, UniProt, GO, model organism databases, and pathway tools represent
different parts of the same biology. A clear attribution model makes it easier to align complex
membership, reaction participants, GO annotations, and pathway diagrams without flattening them into
one gene-to-function edge.

## Initial Case Study: OXPHOS

The OXPHOS project provides a strong first test because respiratory complexes contain catalytic
cores, electron-transfer modules, accessory subunits, membrane anchors, regulatory subunits,
tissue-specific isoforms, and many assembly factors.

### Complex I

Complex I has a catalytic/electron-transfer core plus many accessory subunits. The high-priority
question is whether NADH:ubiquinone oxidoreductase activity should be attributed to catalytic-core
subunits such as NDUFV1, NDUFS1, NDUFS2, NDUFS7, NDUFS8, NDUFV2, and NDUFS3, while keeping
accessory and assembly roles distinct for genes such as NDUFS4, NDUFA13, ACAD9, NDUFAF2,
TMEM126B, and NUBPL.

### Complex II

Complex II is a useful contrast because all four structural subunits participate in the mature
succinate dehydrogenase complex, but they do so in different ways. SDHA and SDHB are closer to the
catalytic and electron-transfer center; SDHC and SDHD anchor the complex and contribute to
ubiquinone interaction. The project should test whether the review language and GO annotations
preserve those distinctions.

### Complex III

Complex III illustrates the catalytic-core versus structural-core problem. CYC1 and UQCRFS1 have
direct electron-transfer roles, while UQCRC1 and UQCRC2 are core structural proteins. BCS1L, LYRM7,
and TTC19 are better treated as assembly, insertion, chaperone, or turnover factors, not as
executors of cytochrome bc1 activity.

### Complex IV

Complex IV raises the issue of regulatory and isoform-specific subunits. COX4I1, COX4I2, COX6A1,
COX6B1, and NDUFA4 should be reviewed for whether they directly contribute to cytochrome c oxidase
activity, regulate or stabilize it, or primarily mark complex membership. SURF1, SCO1, SCO2, COX10,
COX15, and LRPPRC provide assembly, copper delivery, heme biosynthesis, and mRNA-stability cases.

### Complex V

ATP synthase is a whole-machine case. ATP5F1B is a catalytic beta subunit; ATP5F1A is regulatory
within the F1 head; ATP5F1C, ATP5MC1/2/3, and ATP5PO contribute mechanical coupling, proton
channel, rotor, or stator functions; ATP5IF1 is an inhibitor. This case can test whether molecular
function annotations preserve machine architecture instead of assigning the same ATP synthesis label
to every component.

## Additional Candidate Complex Classes

| Complex class | Why it matters | Initial question |
|---------------|----------------|------------------|
| Proteasome | Catalytic beta subunits, structural alpha rings, regulatory particles, and assembly chaperones are separable | Which genes should receive protease activity versus proteasome assembly or substrate-recognition roles? |
| Ribosome | Peptide-bond formation is a ribonucleoprotein complex function with many structural protein participants | Should ribosomal proteins be molecular executors, structural constituents, or contributors to translation? |
| Spliceosome | Dynamic complexes include RNA components, ATPases, scaffolds, and transient factors | How should transient catalytic versus remodeling roles be represented? |
| Exosome and RNA degradation complexes | Catalytic and non-catalytic subunits coexist in related complexes | Which subunits directly degrade RNA and which recruit, scaffold, or regulate? |
| Cellulosome | Scaffoldins and catalytic enzymes combine into a larger extracellular machine | How do we distinguish enzyme activity from complex organization and substrate targeting? |
| Receptor complexes | Ligand binding, signaling, trafficking, and adapter functions may occur in different chains | Which chain enables signaling versus ligand recognition or localization? |

## Review Rubric

| Evidence pattern | Recommended review handling |
|------------------|-----------------------------|
| Purified subunit has activity | Treat as individual gene-product molecular function if the assay is specific and reproducible |
| Active site or cofactor center is located in the subunit | Treat as core function or direct contribution, depending on whether the subunit acts alone or only in a complex |
| Activity requires a stable subcomplex | Annotate direct members of the subcomplex as contributors; record need for a catalytic-subcomplex modeling target if absent |
| Knockout reduces complex activity by destabilizing assembly | Prefer assembly, stability, or complex organization terms over catalytic activity |
| Subunit changes rate, tissue specificity, substrate preference, or inhibitor response | Prefer regulatory or modulator language unless direct activity execution is shown |
| Subunit is only transiently present during maturation | Prefer assembly or maturation terms; avoid mature complex activity |
| Evidence is only co-complex membership or co-purification | Do not infer molecular function beyond complex membership or localization |

## Project Outputs

1. A reusable decision framework for complex function attribution in AI gene reviews.
2. A table of reviewed examples with attribution class: executor, direct contributor, structural,
   regulatory, assembly/maturation, localization, substrate recruitment, or indirect phenotype.
3. Recommendations for when `contributes_to` is appropriate in existing annotations and
   `core_functions`.
4. Candidate modeling gaps, especially stable catalytic subcomplexes that lack GO cellular
   component terms or clear GO-CAM representation.
5. A short guide for downstream users explaining how complex function attribution affects
   enrichment, variant interpretation, and ML training labels.
6. A prototype GO-CAM-to-GPAD export policy for active, accessory/structural, regulatory, and
   unknown complex members.

## Structure Pilot Artifacts

- [Complex IV COX2 copper-maturation Boltz viewer](PROTEIN_COMPLEX_FUNCTIONS/complex_iv_cox2_copper_maturation_boltz_viewer.html)
  shows the highest-confidence hosted BioLM Complex IV pilot retained in this project: the
  MT-CO2/SCO1/SCO2 domain-only Model C run with copper pocket constraints. This is a static GitHub
  Pages-compatible viewer. The model is still hypothesis-generating and should not be used as
  evidence for GO curation.
- `analysis/complex_iv_boltz/RESULTS_MODEL_C_FULL_CU_BIOLM.md` and
  `analysis/complex_iv_boltz/RESULTS_MODEL_C_DOMAINS_CU_BIOLM.md` record hosted BioLM Boltz2 runs
  of the same Model C inputs with larger sampling settings. These improved domain confidence but
  did not produce high-confidence COX2 interfaces.
- `analysis/complex_iv_boltz/RESULTS_MODEL_A_COX2_SCO1_DOMAINS_CU_BIOLM.md` records a hosted
  pairwise MT-CO2:SCO1 domain run. This is the direct terminal-donor control for Model C.
- `analysis/complex_iii_boltz/RESULTS_CYC1_UQCRFS1_BIOLM.md` records a hosted BioLM Boltz2 run
  for the Complex III active electron-transfer interface between CYC1 and UQCRFS1.
- `analysis/proteasome_boltz/RESULTS_PSMB5_PSMA1_BIOLM.md` records a non-OXPHOS hosted BioLM
  Boltz2 run for proteasome attribution: catalytic beta subunit PSMB5 versus structural alpha
  subunit PSMA1.

## Structure Prediction API Access

API access should separate retrieval from prediction. For existing structures, use RCSB PDB and
AlphaFold DB APIs first. For new complex predictions, use a hosted prediction API when we want a
quick no-infrastructure result. This pilot used BioLM's hosted Boltz2 endpoint and archived the
returned CIF, confidence summary, input payload, and analysis notes under `analysis/`. Local
`boltz predict` can still be useful for reproducibility or batch work, but local run outputs are not
part of this project PR.

### Candidate replacement: ESMFold2 (Biohub / biohub.ai)

ESMFold2 is a strong candidate to use alongside or in place of the BioLM Boltz2 endpoint for the
complex-interface pilots in this project. It is the structure/interaction model in Biohub's
("a world model of protein biology", formerly EvolutionaryScale Forge) release and is directly
relevant to our attribution question because it is built around protein-protein and
antibody-antigen interface prediction. See the 2026-05-29 NOTES entry for the full evaluation. Net
position: adopt ESMFold2 as an additional hosted endpoint and re-run the existing archived inputs
head-to-head, keeping the Boltz2 outputs for provenance. All such predictions remain
hypothesis-generating and must not be used as curation evidence.

## Related Projects

- [OXPHOS](OXPHOS.md) -- primary case study for catalytic cores and assembly factors.
- [PROTEOSTASIS](PROTEOSTASIS.md) -- relevant for proteasome and chaperone systems.
- [RIBOSOME_QUALITY_CONTROL](RIBOSOME_QUALITY_CONTROL.md) -- relevant for ribosome-associated
  complex attribution.
- [CELLULOSOME](CELLULOSOME.md) -- bacterial extracellular complex with scaffold and catalytic
  components.
- [OVER_ANNOTATION_PATTERNS](OVER_ANNOTATION_PATTERNS.md) -- broader annotation-error context.
- [IBA_REVIEW](IBA_REVIEW.md) -- propagation risks when complex membership is mistaken for
  function.

---

# STATUS

- [x] Project created
- [x] OXPHOS project incorporated as initial case set
- [x] GO-CAM modeling issue #1 incorporated as motivating modeling problem
- [x] GO-CAM call slide deck incorporated into modeling/export position
- [x] Add static Complex IV BioLM Boltz2 structure viewer under this project
- [x] Add hosted BioLM Boltz2 API access notes, payload generator, and endpoint caller
- [x] Run hosted BioLM Boltz2 Model C pilot for full/mature and domain-only inputs
- [x] Run hosted BioLM pairwise MT-CO2:SCO1 domain control
- [x] Run hosted BioLM Complex III CYC1:UQCRFS1 active-interface pilot
- [x] Run hosted BioLM proteasome PSMB5:PSMA1 attribution pilot
- [x] Complete PSMA1 and PSMB5 reviews as the first non-OXPHOS attribution pair
- [x] Add a second complex class outside mitochondria, likely proteasome or ribosome
- [ ] Build an OXPHOS attribution matrix for reviewed and pending genes
- [ ] Audit existing OXPHOS reviews for direct-function, `contributes_to`, and assembly-factor
      consistency
- [ ] Draft downstream-user guidance for enrichment and ML-label consumers
- [x] Investigate ESMFold2 (Biohub/biohub.ai) as an alternative to BioLM Boltz2 for complex pilots
- [ ] Re-run archived complex inputs (CYC1:UQCRFS1, PSMB5:PSMA1, COX2 Model C) on ESMFold2 as a
      head-to-head against the Boltz2 confidence summaries

# NOTES

## 2026-05-19

Created the project from two inputs:

1. The local OXPHOS project, which already distinguishes catalytic subunits, accessory subunits,
   assembly factors, mobile carriers, and disease contexts.
2. GO-CAM-modeling issue #1, which explicitly raises the problem of catalytic OXPHOS subcomplexes
   inside larger complexes and asks how to avoid exporting catalytic activity to non-catalytic
   accessory subunits.

The main design choice is to treat this as a cross-cutting annotation-quality and modeling project,
not only an OXPHOS project. OXPHOS supplies the first concrete cases, but the same issue affects
proteasome, ribosome, spliceosome, exosome, cellulosome, receptor, and other protein-containing
complex annotations.

## 2026-05-19 GO-CAM slide deck follow-up

Read the GO-CAM call deck on annotating activities of complexes and subcomplexes. Key points added
to the project:

1. Current GO guidance already says complex membership is not sufficient for `contributes_to`.
2. GO-CC terms for catalytic core subcomplexes are considered out of scope, so solving this only by
   adding named subcomplex terms is not attractive.
3. The practical failure mode is Noctua/GPAD export: if complex MF is inferred to every listed
   member, supernumerary OXPHOS subunits incorrectly receive `contributes_to` catalytic activity.
4. The strongest proposal is to distinguish active members from accessory/structural members in
   the model and export MF only for active members.
5. For multi-activity complexes, activity units should each have their own active/accessory member
   assignments.

Opinion after reading the deck: option 3, with explicit active-member and accessory/structural
member relations, is the best bridge between current GO practice and future structure-aware
biology. It is more curator work than status quo, but the complexity is real biology, and it can be
hidden from casual pathway-viewer users while still producing correct GPAD labels.

## 2026-05-20 hosted BioLM Model C runs

Submitted full/mature and domain-only Model C payloads to BioLM's hosted Boltz2 API using
`recycling_steps=3`, `sampling_steps=200`, and `diffusion_samples=5`.

The full/mature hosted run produced `confidence_score 0.573` but still had low ternary interface
confidence (`ipTM 0.237`). SCO1 and SCO2 CxxxC motifs remained ~72 A from the COX2 CuA cysteines,
so this is not evidence for direct COX2 engagement.

The domain-only hosted run was more informative: `confidence_score 0.642`, `ipTM 0.389`, and
SCO1:SCO2 pair-chain ipTM 0.540. However, MT-CO2:SCO1 and MT-CO2:SCO2 pair ipTMs remained low
(`0.165` and `0.196`), and the relevant cysteine motifs were outside the transfer-distance
threshold from COX2 CuA. This supports a cautious interpretation: Boltz2 can find a plausible
SCO1/SCO2 domain interface, but these runs do not establish a stable ternary COX2/SCO1/SCO2
copper-transfer complex.

## 2026-05-20 hosted BioLM Model A pairwise control

Ran a pairwise MT-CO2 CuA domain + SCO1 metallochaperone domain control to test whether the
expected terminal donor interface appears when SCO2 is removed. This was the most direct follow-up
to the Model C result.

The pairwise run had `confidence_score 0.582`, `ipTM 0.158`, and MT-CO2:SCO1 pair-chain ipTM
0.151. The closest SCO1 CxxxC-to-COX2 CuA distance was near but still outside the heuristic transfer
threshold: 13.97 A CA and 13.75 A SG-SG. This does not support using the model as evidence for
direct SCO1-to-COX2 transfer. It is more evidence that the structural-prediction workflow is useful
for framing hypotheses, but the current GO annotation decision remains literature-driven.

## 2026-05-20 hosted BioLM Complex III CYC1:UQCRFS1 pilot

Switched to a different complex and hypothesis: whether Boltz2 can recover the active
electron-transfer interface between Complex III cytochrome c1 (`CYC1`) and the Rieske Fe-S protein
(`UQCRFS1`). This is a cleaner active-member test than the transient Complex IV maturation module:
CYC1 and UQCRFS1 are stable mature Complex III subunits with direct electron-transfer roles, while
UQCRC1/UQCRC2 are structural core proteins.

The hosted BioLM run used CYC1 residues 85-281 and UQCRFS1 residues 141-274. It found a short
motif-level distance between the CYC1 heme-binding region and UQCRFS1 Rieske region: 6.20 A CA
between CYC1 H125 and UQCRFS1 H219. However, the interface confidence was weak
(`confidence_score 0.414`, `ipTM 0.241`, pair-chain ipTM 0.241, pair-chain iPAE 23.7 A). The
interpretation is therefore cautious: the geometry is encouraging, but the prediction is not
curation-grade. This is a good example of why structure prediction readouts need both geometry and
confidence thresholds.

## 2026-05-20 hosted BioLM proteasome PSMB5:PSMA1 pilot

Ran a non-OXPHOS attribution test using the human 20S proteasome core. The hypothesis was not
"do these subunits touch?", but "does an interface justify exporting protease activity?". `PSMB5`
is the beta5 catalytic subunit with UniProt active-site nucleophile Thr60; `PSMA1` is an alpha-ring
structural subunit.

The hosted BioLM run used mature PSMB5 residues 60-263 and PSMA1 residues 1-263. It produced
`confidence_score 0.595`, `ipTM 0.230`, pair-chain ipTM 0.230, and 79 residue-residue contacts at
5 A. PSMB5 active-site Thr60 was 9.68 A from the nearest PSMA1 atom in the predicted model, but
the interface confidence was weak.

Interpretation: this is not curation-grade structural evidence, but it is conceptually useful.
Even if a PSMB5:PSMA1 structural interface were high-confidence, the threonine-type endopeptidase
activity should stay with PSMB5 and other catalytic beta subunits, not with alpha-ring structural
members. This is the clearest non-OXPHOS example so far of why complex membership and molecular
function execution need separate annotation edges.

## 2026-05-29 ESMFold2 (Biohub / biohub.ai) evaluation vs BioLM Boltz2

Investigated whether ESMFold2 at https://biohub.ai/esm/protein should replace the hosted BioLM
Boltz2 endpoint used for the complex-interface pilots above.

### What biohub.ai/esm is

`biohub.ai` is the new home of the EvolutionaryScale / Forge platform, now operating as Biohub.ai
and releasing what they call "a world model of protein biology". The release has three pieces:

- **ESMC** (Evolutionary Scale Modeling Cambrian): a protein language model trained on ~2.8B
  sequences; available at multiple scales on Hugging Face (e.g. `esmc-600m-2024-12`).
- **ESMFold2**: the structure/interaction prediction and design engine built on ESMC, hosted as
  `esmfold2-fast-2026-05`. MSA-free (no alignment step, unlike AlphaFold2).
- **ESM Atlas**: a navigable database of ~6.8B sequences and ~1.1B predicted structures.

Licensing is MIT (commercial and non-commercial), with open weights on Hugging Face plus a hosted
inference API. Biohub states the models are "freely available to the global scientific community";
I could not confirm exact free-tier quotas or rate limits from public pages (the biohub.ai product
pages are a JS app and did not render details to the fetcher), so quota needs verifying against an
actual token before committing to batch runs.

### Why it is a good fit for this project specifically

1. **It is interface-first.** Unlike the original ESMFold (single-chain only), ESMFold2 explicitly
   predicts multi-chain biomolecular complexes, and its headline claim is interface accuracy:
   "surpasses other models in DockQ pass-rate on FoldBench protein-protein and antibody-antigen
   complexes," and "performed favorably when compared against Chai-1, Boltz-1, and AlphaFold 3."
   That is exactly the regime our pilots live in (does an interface justify exporting a molecular
   function to a subunit), where Boltz2 gave us weak ipTM signals (0.15-0.39) across every run.
2. **Same confidence vocabulary.** The hosted API returns pLDDT (mean), pTM, and ipTM - the same
   metrics our analysis notes already key on - so our interpretation thresholds and analysis
   scripts port over with minimal change. (PAE / pair-chain iPAE, which we used for CYC1:UQCRFS1,
   was not confirmed in the hosted API surface and should be checked; it may only be in the local
   weights path.)
3. **Ligand and nucleic-acid support.** The input builder exposes `ProteinInput`, `DNAInput`, and
   `LigandInput`. This is directly relevant to the unfinished hard cases in this project - copper
   delivery (COX2 CuA / SCO1 / SCO2), heme-bearing electron transfer (CYC1), and Fe-S centers
   (UQCRFS1) - which Boltz2 ran as apo domains. Whether non-standard metals (Cu) and cofactors can
   be parameterized cleanly still needs a concrete test.
4. **Open weights + MIT.** Better reproducibility story than a closed hosted endpoint: we can pin a
   model version, and a local path exists for batch work without depending on a third-party host.

### Access pattern (hosted)

```python
from esm.sdk.forge import SequenceStructureForgeInferenceClient
client = SequenceStructureForgeInferenceClient(
    model="esmfold2-fast-2026-05",
    url="https://biohub.ai",
    token="<API token>",
)
```

Multi-chain complexes are assembled from `ProteinInput` / `DNAInput` / `LigandInput` components
with distinct chain IDs. This is a different client surface from the BioLM Boltz2 caller, so the
existing payload generator / endpoint caller under `analysis/` would need an ESMFold2 adapter
rather than a drop-in URL swap.

### Recommendation

Adopt ESMFold2 as an **additional** hosted endpoint rather than a hard replacement, and run a
head-to-head on the three archived inputs we already have Boltz2 summaries for: CYC1:UQCRFS1
(active electron-transfer interface), PSMB5:PSMA1 (catalytic-vs-structural control), and the COX2
Model C copper-maturation module. Because ipTM was the limiting signal in every Boltz2 pilot, a
model that is genuinely stronger on complexes could change those conclusions - which is the whole
reason to test it on identical inputs and keep the Boltz2 outputs side by side for provenance. The
curation guardrail is unchanged: any ESMFold2 model remains hypothesis-generating and must not be
cited as GO evidence.

Open items before relying on it: confirm free-tier/rate limits with a real token; confirm whether
PAE/iPAE is exposed by the hosted API; confirm metal/cofactor (Cu, heme, Fe-S) parameterization in
the ligand input.
