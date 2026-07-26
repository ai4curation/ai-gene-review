# RAD51 (FANCR) — AIGR vs Affinage

**Affinage record:** run 2026-06-10 · 45 discoveries · self-eval pairwise = win, faith 100% · gates passed.

RAD51 is the central eukaryotic recombinase — the RecA/Rad51 ortholog that assembles the
ATP-dependent nucleoprotein (presynaptic) filament on ssDNA and catalyzes homology search and DNA
strand exchange. The AIGR review is exceptionally large (256 existing annotations) and mature: 3
`core_functions`, ~83 generic protein-binding IPI rows demoted as over-annotated, meiotic/telomere/
mitochondrial roles kept non-core, and a corrected "presynaptic filament" misnomer. The Affinage
record is a 45-PMID mechanistic narrative densely covering filament assembly, mediator networks
(BRCA2/RAD52/RAD54/paralogs/HOP2-MND1/FANCD2-I), fork protection, and several non-canonical roles.

## Agreement (brief)

Both sources place the same reaction at the center: an ATP-dependent RAD51-ssDNA presynaptic
filament that performs homology search and strand exchange (AIGR core_function GO:0000150 strand
exchange + GO:0003697 ssDNA binding + GO:0016887 ATP hydrolysis; Affinage narrative anchored on
PMID:9012806/8929543/7988572). Both treat BRCA2 as the loader that overcomes rate-limiting
nucleation by displacing RPA and blocking ATP hydrolysis (AIGR references PMID:20729832/20729859/
37499663; Affinage PMID:20729832/36976771/37919288), the RAD51 paralog complexes as filament
remodelers/stabilizers, and replication-fork protection/restart and ICL repair as genuine functions.
Both correctly read RAD51's "presynaptic filament" as the recombination nucleoprotein filament, not
a neuronal structure (AIGR MODIFY of GO:0099182; Affinage narrative + PMID:18003859-type usage).

## Disagreements

| Topic | Affinage says | AIGR review says | Verdict (who is right + why) |
|---|---|---|---|
| Mechanism-profile GO layer | `molecular_activity` = `GO:0003677 DNA binding`, `GO:0140657 ATP-dependent activity`, `GO:0140097 catalytic activity acting on DNA`, `GO:0003723 RNA binding`; `localization` flattens to nucleus/nuclear chromosome | Uses the specific recombinase MF `GO:0000150 DNA strand exchange activity`, `GO:0003697 ssDNA binding`, `GO:0016887 ATP hydrolysis`; specific damage-site/nucleoplasm CCs | **AIGR right.** Affinage's own note flags this layer as coarse (collapses to general parents). `catalytic activity acting on DNA` / `ATP-dependent activity` are non-informative parents of the curated terms; not imported. |
| `protein binding` (GO:0005515) | Narrative leans on a large PPI network (BRCA2, RAD52, RAD54, RADX, FANCD2/I, HELQ, paralogs, DMC1, PSF, TOPBP1, TOPORS…) | 83 IPI `protein binding` rows MARK_AS_OVER_ANNOTATED; interactions retained via specific process/complex rows, UniProt SUBUNIT, and references | **AIGR right** per curation policy; Affinage does not assert the generic term, so no true conflict. `GO:0042802 identical protein binding` correctly kept (homo-oligomerization = filament). |
| RNA binding / TERRA R-loops | Lists `GO:0003723 RNA binding`; narrative: RAD51 binds TERRA lncRNA and catalyzes R-loop formation at telomeres (PMID:33057192) | No RNA-binding annotation (absent from GOA) | **Affinage surfaces a real but niche activity.** RAD51–TERRA binding/R-loop formation is published (Nature). Left un-annotated here: single-paper, telomere-context, not in GOA; recorded as a candidate rather than added, per conservative scope. |
| STING / innate immunity | RAD51 loss → MRE11-degraded nascent DNA → cytosolic self-DNA → STING innate immune activation (PMID:28334891) | Not annotated | **AIGR right to exclude.** This is a downstream consequence of *losing* RAD51 fork protection, not a molecular function RAD51 performs; annotating innate immunity to RAD51 would be an over-reach. |
| MiDAS / centromere / redox (PMID:34508092, 36702125, 36058112) | Presents each as a distinct RAD51 role | Covered implicitly under fork/DSB core and non-core localizations; not separately annotated | **AIGR reasonable.** These are context specializations of the same recombinase/fork activity; no wrong-branch GO offered and each rests on single studies. Not added. |
| Fork reversal bypassing CMG; abasic-site protection (PMID:37104614, 39178838) | Distinct mechanistic findings | Captured by core_function `GO:0031297 replication fork processing` | **Agreement in substance.** Affinage's detail is finer-grained than the GO term but not in conflict. |

## Papers incorporated into the review

| PMID | Supports | How used |
|---|---|---|
| PMID:9012806 | Recombinase strand exchange (GO:0000150) + ATP-hydrolysis coupling (GO:0016887) | New reference (reference_review HIGH/VERIFIED). Foundational human-RAD51 paper absent from the review; two verbatim `supported_by` quotes attached to core_functions 1 and 3. |
| PMID:20729832 | BRCA2-mediated RAD51 filament loading | Already a reference (only under over-annotated protein-binding rows); added `reference_review` HIGH/VERIFIED documenting the BRCA2→RAD51 loading mechanism. |
| PMID:26811421 | RAD51 Ser14 phosphorylation → chromatin loading (DSB repair; chromosome localization) | Already a reference / original_reference for DSB-repair + chromosome rows; added `reference_review` MEDIUM/VERIFIED. |

All `supporting_text` strings are exact verbatim substrings of the cached full text (PMID:9012806
fetched/cached via `fetch-pmid`; the other two already cached). GO terms unchanged and previously
validated.

## Net assessment

AIGR and Affinage agree on RAD51's core identity as the DNA-strand-exchange recombinase and on the
BRCA2/mediator logic of filament loading. Affinage's `mechanism_profile` GO/Reactome layer is coarse
and partly wrong-altitude (generic "catalytic activity acting on DNA"/"ATP-dependent activity"
parents; a flattened nucleus localization) and was correctly not imported over the review's curated
`core_functions`. Affinage's real value was its citation density: it surfaced the foundational Gupta/
Radding 1997 human-RAD51 recombinase paper (PMID:9012806), now added as a verified reference wired
into two core_functions, and it prompted verified `reference_review` adjudication of two overlapping
citations. One genuine but niche activity it highlights — RAD51 RNA/TERRA binding and R-loop
formation (PMID:33057192) — is noted as a candidate but left un-annotated (single-paper, telomere-
specific, absent from GOA), and its STING/innate-immunity framing was correctly excluded as a
loss-of-function consequence rather than a RAD51 function. No existing AIGR decision was weakened.
File remains ✓ Valid (1 benign deep-research-file warning).
