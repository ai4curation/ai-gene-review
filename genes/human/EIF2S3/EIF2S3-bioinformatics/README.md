# EIF2S3 database evidence replay

Run `python3 reproduce.py` from any directory, using Python 3.9 or later. No network, installation or external Python package is needed. The program verifies every input and parser hash, reconstructs the results from the archived data, and compares them with `expected-results.json`. `--output PATH` optionally saves the small verification result. Temporary extraction is removed on exit.

The archive contains database records and protein-interaction datasets, not original article bodies. `inputs.json` identifies every member, hash and original filename. Available acquisition URLs are copied from the saved receipts. For reused datasets the PMID identifies provenance; an exact download endpoint is not invented where it was not recorded here. Reactome inputs contain only verbatim official-page blocks from the original responses; unrelated retrieved text is excluded.

Three independent computations run:

1. `reconstruct_paint.py` walks the complete saved PTHR42854 tree, matches the target MSA sequence to official P41091, joins each of the four IBA assertions to a positive IBD on that lineage, and retains the complete lineage IBD/IRD records and selected literal donor annotations. Neither donor count nor target self-evidence is treated as a defect.
2. `replay_interactions.py` joins each of the 41 imported generic-binding contexts to the full saved 197-record IntAct export, retaining exact partner IDs, publication IDs, methods, taxa, features and record identifiers. It independently filters complete OpenCell/BioPlex tables and the AP-MS graph for EIF2S3, preserving row positions and mixed accession groups.
3. `replay_reactome.py` follows only forward input/output/component edges to the human gamma entity. A reverse membership link is not a participation witness. These bounded paths establish the target's modeled component/location context; they do not assign a different component's catalytic activity to gamma or prove exhaustive graph closure.

`source-contexts.json` inside the archive contains the 81 imported source dictionaries, without review decisions. The extraction code does not choose annotation actions. A verified screen edge alone does not establish a native complex, purified binary contact, or functional partner-class refinement. Those judgments require the separate source assessments in [the source guide](../EIF2S3-source-evidence.yaml).

The archive and expected output are fixed observations, not a claim that external databases never change. Missing matches in any bounded table are not evidence of nonbinding. The normal publication caches are separate repository sources and are not edited by this analysis.
