---
title: "PSEPK ppu00071 bacterial fatty acid beta-oxidation batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [fadE, fadB, fadA]
autolink_gene_symbols: false
---

# PSEPK ppu00071: bacterial fatty acid beta-oxidation

The four-reaction core starts with an already activated fatty acyl-CoA. FadE-mediated dehydrogenation, hydration, NAD-dependent hydroxyacyl-CoA oxidation and thiolysis release acetyl-CoA and a shortened chain only when the selected proteins accept that substrate. Transport, activation, cofactor recycling, unsaturated-substrate auxiliary reactions and odd-chain product disposal are external requirements.

| Member | Supported role | Evidence boundary |
|---|---|---|
| PP1893 / Q88LN6 (fadE) | Acyl-CoA dehydrogenation, acceptor unspecified | Inferred role; PMID32826213 identifies PP0368/PP0370 as stronger native dehydrogenase candidates. No demonstrated ETF coupling or isolated kinetics. |
| PP2136 / Q88L02 (fadB) | Hydration and NAD-dependent oxidation | Curated multidomain chemistry and native fitness support; chain range and purified complex kinetics unresolved. |
| PP2137 / Q88L01 (fadA) | CoA-dependent thiolysis with the compatible alpha partner | Native pairing inference is distinct from isolated kinetics. Phenylacetate annotation remains UNDECIDED; a canonical beta-oxidation role does not exclude a secondary role. |

The comparative module uses exact reviewed members from E. coli, Salmonella, Pseudomonas putida, P. fragi, P. aeruginosa, M. tuberculosis and B. subtilis. Its four reaction classes have distinct family implementations and matched-partner/substrate conditions. P. fragi and H37Rv structural pairs establish partial TFE chemistry without assigning a native first-step dehydrogenase. The PAO1 dehydrogenase constructs are distinguished from PA14 mutant growth and clinical-isolate proteomics.

## Status

- [x] Complete the three KT2440 gene reviews and comparative literature assessment.
- [x] Complete 19 exemplar reviews and eight family reviews.
- [x] Preserve original annotation payloads and raw/provider sources.
- [x] Pass focused checks and full-corpus validation.
- [ ] Publish the module PR and shepherd it to actual merge.

## 2026-11-06 — comparative audit

Comparative beta-oxidation curation covers 19 COMPLETE gene reviews across seven species and three bacterial phyla, preserving all 211 original annotation payloads, both inherited NEW rows and 40 raw/provider files. Six supported additions yield 217 rows. Seventeen references, including four review articles, supply 21 mined findings. Four required reactions use ten alternatives and eight reviewed protein families. Unknown physiological electron acceptors, matched partner requirements, substrate limits and distinct native versus biochemical endpoints are explicit. The source-scoped checker uses the production module circuit with 54 cases and 12 mutation checks; passing cases do not replace the literature assessment. Focused checks and full-corpus validation passed on 2026-11-06 (10,688 reviews; zero blocking errors). Corpus advisory reference issues outside this panel remain recorded in the validation proof. A dedicated PR, independent review, CI and actual merge remain pending.

The broad [KEGG candidate inventory](ppu00071_fatty_acid_beta_oxidation.tsv) is retained. Candidate membership alone does not establish catalytic role or native flux. Provider source files remain unchanged; no old running-research status is treated as a live process.
