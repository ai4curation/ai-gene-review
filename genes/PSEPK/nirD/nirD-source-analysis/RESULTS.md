# NirD three-target ligand counts

The calculation reports Q88M68 Cys18/Cys95 and His87; P0A9I8 Cys8/Cys20/Cys84 and His35/His62/His94; A0QPK3 Cys22/Cys79/Cys98 and His15/His54. Only Q88M68 lacks enough histidines for the canonical two-Cys/two-His Rieske set. The result does not justify imposing that same count-based REMOVE rationale on P0A9I8 or A0QPK3. Sufficient counts are not positive evidence of a ligand site or a bound cluster. Noncanonical binding remains untested in all three.

## Methods and checks

Python/Biopython 1.85 from the repository uv environment. The script parses each existing UniProt flat file and enumerates exact one-based positions without alignment, motif thresholds or hardcoded expected outcomes. `panel-ligands.json` records the results and SHA256 of every input. The single-target invocation reproduces the existing `ligands.json` byte-for-byte; the multi-target invocation produces a separate result.

- [x] All input and output paths are explicit CLI arguments; no target sequence or expected ligand count is hardcoded.
- [x] The script was tested on three independent input records, including two targets beyond the original PSEPK protein.
- [x] Both panel and single-target just recipes complete successfully.
- [x] Direct calculated results are present beside the script; input hashes identify the unchanged raw records.
- [x] README.md identifies the comparative structure (PMID:22965870), counts, action limits and noncanonical-binding uncertainty.

This is a composition check. A geometrical binding-site or structural correspondence analysis would be a different analysis and has not been claimed. The sequence-analysis script does not alter its input or any review file; integrated reviews can cite these results separately.
