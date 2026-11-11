# EFNB1 evidence replay results

The executed saved-data replay reproduces the following results from the original inputs:

| Evidence | Reproduced result |
| --- | --- |
| IntAct | 259 query records; 17 selected records for the reviewed pairs; 34 matching official reference-sequence checksums. The 17 include two microscopy records that are retained as colocalization, not counted as binding experiments. |
| PAINT | 389 tree nodes; exact 346-aa human target sequence; six literal IBDs on its ancestral path. |
| Reactome | All 30 imported location assertions resolve to P98172 at plasma membrane, through 66 positive paths using 83 nodes. Additional successfully retrieved ephrin branches are included for reproducibility. |
| PMID:35922511 | Human EFNB1 prefix of 240 residues; six reciprocal raw assay cells for EPHA2, EPHB2 and EPHA4; corresponding source-network and affinity entries. |
| PMID:40205054 | One selected EFNB1→EPHB2 AP-MS edge among 39 incident EFNB1 edges in the original network. |
| PMID:19056867 | One EFNB1/NP_004420 table row with one peptide; the final table value 2 identifies the cited publication. |

For PMID:35922511, the source-reported SPR dissociation constants are 41,000 nM for EPHA2 and 25,000 nM for EPHA4. The EPHB2 value of 0.66 nM is marked Published, and is not a newly measured value from that study. The measured recombinant product consists of the human 1–240 prefix and fusion tags, rather than the full membrane-bound ligand or intracellular fragment. Raw reciprocal cells and source rows remain visible in `source-projections.json`; no native membrane affinity is inferred.

The independently established partner classes are:

| Partner | Official source | Class used and limit |
| --- | --- | --- |
| ERBB2/P04626 | [UniProt](https://www.uniprot.org/uniprotkb/P04626/entry) | Signaling receptor. Association does not by itself establish EFNB1 receptor agonism or kinase activity. |
| EPHB2/P29323 | [UniProt](https://www.uniprot.org/uniprotkb/P29323/entry) | Eph receptor; supports ephrin receptor binding. |
| EPHA2/P29317 | [UniProt](https://www.uniprot.org/uniprotkb/P29317/entry) | Eph receptor; the extracellular assay supports binding without a general cross-class activation claim. |
| EPHA4/P54764 | [UniProt](https://www.uniprot.org/uniprotkb/P54764/entry) | Eph receptor with broad ligand recognition; individual assay scope is retained. |
| ANKRD46/Q86W74-2 | [UniProt](https://www.uniprot.org/uniprotkb/Q86W74/entry) | Displayed product officially named isoform 1, with ankyrin repeats. No independently established narrower functional partner class was assigned. |
| Mouse PICK1/Q62083 | [UniProt](https://www.uniprot.org/uniprotkb/Q62083/entry) | PDZ-containing partner in a literal positive Y2H record. Its domain architecture alone does not identify the assayed EFNB1 interface in the unavailable full original. |

The PAINT placement is evaluated as a curated ancestral assertion, not a donor-count vote. Human EFNB1’s inclusion among evidence sources is valid target grounding. Rat cortical synaptic experiments and current donor annotations support the neuronal contexts; a donor extension naming hippocampus is kept distinct from the inspected cortical culture Methods.

HPA reports plasma membrane with per-location reliability supported for the exact EFNB1 target. No image pixels were independently interpreted. The earlier non-target lookup is excluded from this public input bundle and all biological conclusions.

The calculations authenticate source records and reproduce measured values. They do not prove actual full-length insert identity solely from a reference ROGID, independently revalidate urinary peptide spectra, establish a native physiological role for every screen pair, or assign other Reactome participants’ catalytic activities to EFNB1.
