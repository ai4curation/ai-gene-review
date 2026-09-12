# BACE1 notes

## Review status

- First-pass review completed on 2026-06-19.
- `just fetch-gene human BACE1` created local UniProt, GOA, publication, and PANTHER-family evidence files; `just fetch-gene-pmids human BACE1` confirmed all 38 PMID-backed publication caches were present.
- Falcon deep research was attempted with `timeout 180 just deep-research-falcon human BACE1 --fallback perplexity-lite`, but the process timed out and no provider deep-research artifact was written. These notes rely on cached UniProt, GOA, and publication files.
- `just validate human BACE1` passes cleanly.

## Functional synthesis

BACE1 is beta-secretase 1, a membrane aspartyl endopeptidase that initiates amyloidogenic APP processing. The original BACE characterization supports beta-site APP cleavage: [PMID:10531052 "Overexpression of this protease, termed BACE (for beta-site APP-cleaving enzyme) increased the amount of beta-secretase cleavage products"] A parallel memapsin-2 study supports the same catalytic assignment: [PMID:10677483 "memapsin 2 cleaved the beta-secretase site of APP"] and frames BACE1 as rate-limiting for amyloid-beta production: [PMID:10677483 "catalyzes the rate-limiting step of the in vivo production of the beta-amyloid (Abeta) peptide"].

BACE1 localization and trafficking are part of the core function because compartment access controls APP cleavage. BACE1 is largely in late Golgi/TGN and endosomal routes, with smaller cell-surface, ER, lysosomal, and recycling-endosome pools. The BACE1 transmembrane-domain paper states that BACE1 localization is required for APP access: [PMID:11466313 "BACE1 is required for the access of BACE1 enzymatic activity to the cellular APP substrate"] GGA trafficking supports endosome-to-TGN retrieval: [PMID:15886016 "GGA1 regulates the retrograde transport of internalized BACE1 from endosomal compartments to the TGN"] SNX6 and ubiquitin/lysosome papers support the same trafficking-control model: [PMID:20354142 "SNX6 negatively modulates BACE1-mediated cleavage of APP"].

Many non-APP annotations are plausible but secondary. BACE1 has non-APP neuronal substrates and trafficking regulators that produce synaptic, sensory, behavioral, apoptotic, and stress-response phenotypes. Those were retained as non-core unless the term directly described BACE1 protease activity, APP catabolism, amyloid-beta formation/metabolism, or BACE1 trafficking compartments.

## Annotation decisions

- Accepted aspartic-type endopeptidase, beta-aspartyl-peptidase, endopeptidase/peptidase activity, proteolysis, protein processing, membrane ectodomain proteolysis, APP catabolic process, amyloid-beta formation/metabolism, and core TGN/endosomal/cell-surface/lysosomal locations.
- Modified `amyloid fibril formation` to amyloid-beta formation and APP catabolic processing because BACE1 generates amyloid-beta but does not assemble fibrils.
- Modified `amyloid-beta binding` to APP catabolic processing and aspartic-type endopeptidase activity because the cited evidence supports BACE1-APP/SORL1 processing interactions rather than amyloid-beta binding as a core BACE1 activity.
- Marked generic `protein binding` annotations as over-annotated.
- Kept behavioral, synaptic, metal-response, insulin-like growth factor response, neuron-apoptosis, and regulator-binding annotations as non-core.

Final action distribution: 94 ACCEPT, 24 KEEP_AS_NON_CORE, 20 MARK_AS_OVER_ANNOTATED, 2 MODIFY.

## Knowledge gaps and experiments

- The key mechanistic gap is how BACE1 trafficking regulators partition BACE1 between APP-accessible compartments and degradative routes in human neurons.
- Useful experiments would use endogenous BACE1 tagging plus APP beta-cleavage reporters under perturbation of GGA, SNX6, BIN1, USP8, and lysosomal-routing pathways.
- Non-APP substrate biology should be separated from Alzheimer amyloid biology by comparing APP, CHL1, neuregulin, SEZ6-family, and other neuronal substrates in BACE1 wild-type and catalytic-dead human neurons.

## 2026-06-20 second-pass audit

The second-pass audit added manual `reference_review` metadata for the BACE1 beta-secretase discovery papers, the late-Golgi/APP-access localization paper, and the GGA/SNX6 trafficking-control papers. No annotation action changes were needed: BACE1 remains curated as a membrane aspartyl endopeptidase whose core biology is APP beta-cleavage, amyloid-beta generation, and compartment-controlled substrate access, with non-APP neuronal and behavioral outputs retained as non-core.

## Falcon deep research integration (2026-06-21)

The grounded Falcon (Edison) report is in `BACE1-deep-research-falcon.md` (13 citations, real DOIs); it strongly corroborates the existing review's core picture (type-I transmembrane aspartyl protease / EC 3.4.23.46 = beta-secretase that performs the rate-limiting beta-site APP cleavage initiating amyloid-beta generation, acting in acidic TGN/endosomal/lysosomal compartments) and adds no contradictions, only refinements. All Falcon-sourced citations below are not yet independently verified against full text.

New or refined points beyond the existing notes/review:

- Dual amyloidogenic/amyloidolytic activity: beyond beta-site APP cleavage, BACE1 also cleaves longer Abeta (Abeta40/42) at the beta34 site to generate non-toxic, non-aggregating Abeta34, so the BACE1/APP ratio sets the amyloidogenic-vs-amyloidolytic balance [Ulku et al., Sci Rep 2023, doi:10.1038/s41598-023-28846-z]. This is a genuinely new functional angle (Abeta-clearance), not currently reflected in the review.
- gp130 (IL6ST) identified as a physiologically relevant BACE1 substrate: shedding reduces membrane gp130 / raises soluble gp130, attenuating neuronal IL-6 signaling and affecting neuronal survival [Roselli et al., Cell Mol Neurobiol 2023, doi:10.1007/s10571-023-01374-0]. New substrate beyond CHL1/NRG1/SEZ6 already noted.
- Catalytic detail: two catalytic aspartates D93 and D289 in the ectodomain; antiparallel hairpin flap (~Y128-G138) gates substrate access; pH optimum ~4.5 [Taylor et al., Obes Rev 2022, doi:10.1111/obr.13430].
- Trafficking machinery refinement: post-Golgi export depends on AP-1 and Arf1/Arf4; APP and BACE1 follow distinct post-Golgi routes that limit colocalization, and early endosomes are the major neuronal APP beta-cleavage site [Tan et al., Mol Biol Cell 2020, doi:10.1091/mbc.e19-09-0487].
- PTM control: glycosylation, phosphorylation (notably Ser498, regulating trafficking/amyloidogenic processing), palmitoylation, and acetylation regulate maturation/trafficking/stability [Wen et al., 2022, doi:10.2174/1570159x19666210121163224].
- Broad substrate repertoire (~70 substrates) confirms BACE1 myelination role via NRG1 cleavage, plus inflammatory/metabolic substrates (PSGL-1, IL-1R2, insulin receptor, VEGFR1/Flt1, Jagged1/2) — APP is noted to be a relatively poor substrate [Taylor et al., Obes Rev 2022, doi:10.1111/obr.13430].
- AD drug-target context: BACE1 is a major disease-modifying target, but BACE inhibitor trials hit mechanism-based / on-target side effects (e.g. cognitive worsening) from processing of physiological substrates [Patel et al., 2022, doi:10.2174/1570159x19666211201094031; Roselli et al., 2023].

Discrepancies / annotations to consider: No discrepancies with existing annotations. The one substantive gap is the new amyloidolytic Abeta34 function — the existing GO:0050435 (amyloid-beta metabolic process, ACCEPT/core) already subsumes both Abeta generation and Abeta34 clearance, so no action is strictly required, but if the curated picture is later expanded the Abeta34/amyloidolytic activity is the candidate to surface (e.g. an Abeta-catabolic/clearance framing alongside the existing GO:0034205 amyloid-beta formation). The myelination-via-NRG1 and gp130/IL6-signaling roles remain appropriately non-core (downstream of the same aspartyl endopeptidase activity). All of the above are Falcon-sourced and unverified against full text; no `reference_review`/YAML changes were made.
