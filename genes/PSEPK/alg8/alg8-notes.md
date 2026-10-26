# alg8 notes

## Full-gene metabolic-scope re-review, 2026-09-20

Extracellular matrix assembly is retained as a conditional non-core context of alginate polymerization. Alg8 performs polymer-building work, and a broader process need not be its most specific core description. PMID:17601783 states "Alginate influenced biofilm architecture" but explicitly assays P. putida mt-2, not KT2440. PMID:25968647 directly assays the P. aeruginosa Alg8-Alg44 complex. The existing OpenScientist operon synthesis was read and incorporated with this strain-transfer caveat; its direct-KT2440 attribution is disputed. Hyaluronan terms remain incorrect because Alg8 uses GDP-mannuronate for alginate rather than the alternating hyaluronan substrates; the erroneous vertebrate-only rationale was removed. No source annotation was deleted and no new term was added.

## 2026-10-25 cross-species polymerization/export audit

Target Q88NC5/PP_1287 has PANTHER PTHR22913:SF12 MANNURONAN SYNTHASE within the broad HYALURONAN SYNTHASE family; the broad classification does not establish polymer specificity. Retained rejection of hyaluronan-specific propagation on target curated function, alginate operon and native Pa evidence, not on taxonomic stereotyping. The pre-existing NEW alginate synthase MF matches the live GO definition GDP-D-mannuronate + alginate(n) = GDP + alginate(n+1). Related-strain mt-2 algD physiology supports conditional matrix relevance, not a KT2440 alg8 experiment.

Normal fetch-gene and fetch-gene-pmids were run. Existing source files that differed from remote were preserved; only pipeline-backed qualifier/supporting-entity backfills were accepted. All original GOA rows were independently assessed. Annotation-state GOA files, module output and unnecessary broad family exports were removed from the evidence bibliography. Primary articles and curated target family/function statements replace unqualified provider synthesis. Existing genuine Falcon reports for AlgG/K/E were read and retained as secondary context. Missing alg8 research was attempted concurrently with publication caching; Falcon authentication and fallback credit/quota failures are recorded in /tmp/polymer-PSEPK-alg8-deep.log, so no provider report was fabricated or repeated for alg44/algL. Fitness fetch was attempted for all six and failed for missing local data/unreachable FEBA, documented in /tmp/polymer-PSEPK-alg8-fetch-fitness.log; no fitness inference is made.

Source access: PMID25968647,25817996,20159471,36494359,34990713 and refreshed24398681 have full cached text. PMID17601783,12775688,12581364,16401084,16866359 and21778407 have abstract-only caches; explicit abstract findings are quoted and no absent full-text experiment is rejected. The AlgE full article was additionally inspected on PMC; the cache limitation remains truthful. All molecular-function proposals are backed by enzyme/structural/family evidence; this audit adds no new process term. No relevant accession appeared in gocams/index.tsv. Source fields are preserved and record sections are backfilled with the helper.

Final validation: just validate PSEPK alg8 passed. Original annotation fields were compared with the pre-fetch snapshot and remain unchanged, apart from supported pipeline additions. Final rows: 6; actions {'ACCEPT': 2, 'REMOVE': 2, 'KEEP_AS_NON_CORE': 1, 'NEW': 1}. Existing Falcon-report citation advisories are intentionally tolerated where direct primary sources replace the report in row evidence.


## PR #5552 follow-up, 2026-10-26

Hyaluronan-specific propagation is treated consistently as REMOVE across the three Alg8 reviews; supported alginate roles remain independently represented. Live UniProt PANTHER cross-references show that SF12 itself contains S. pyogenes HasA P0C0H0 (hyaluronan chemistry; PMID:8276791) and NodC P04340/P26024, in addition to the three Alg8 proteins. The SF12 label MANNURONAN SYNTHASE is therefore not a substrate-specific selector. GO:0085029 was checked live: matrix aggregation/arrangement/bonding, with no animal restriction. Retained the evidence gradient: Pa target-specific architecture, KT2440 related-strain inference, Azotobacter over-annotation without a comparable matrix-architecture result. Substituting a biofilm term would change the biological claim rather than simply refine it.


## 2026-10-26 — ISS source trace

Named P. aeruginosa Alg8 Q52463 as the sequence source for the retained KT2440 NEW ISS proposal. Added the direct ortholog polymerization/active-site evidence from PMID:16391057 and PMID:18524915, rather than relying on interaction evidence alone. All original GOA rows and the existing proposal count are unchanged.
