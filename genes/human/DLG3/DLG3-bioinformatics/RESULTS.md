# DLG3 PDZ fragmentomics: reproducible source measurements and sequence crosswalk

The published workbook contains **1,344 DLG3 domain–motif measurements**, 448 each for DLG3_1, DLG3_2 and DLG3_3. The 396 imported PMID:36115835 annotation rows yield **1,221 accession-candidate joins** to those measurements. Of these, 1,200 match the supplied current product sequence through the workbook's `natural_10mer` field; 21 do not. Three AXIN1 internal-peptide rows additionally match through the actual peptide sequence, giving **1,203 sequence-supported scientific selections**. A selection is an identification/mapping decision, not a positive-binding verdict.

## Sources and reproducibility

The source is [Gogl et al., 2022, PMID:36115835](https://doi.org/10.1038/s41467-022-33018-0), Supplementary Data 1, sheet **PDZ-PBM interactome**. The [public supplementary archive](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9482650/supplementaryFiles) contains `41467_2022_33018_MOESM4_ESM.xlsx`; that workbook's SHA-256 is `ada912921164f0a79630c6a714b9ff264a7217ad3e646153ef498eb456206795`.

[reproduce.py](reproduce.py) downloads that archive or reads a local workbook, verifies the workbook version, and extracts the original rows without imputing affinities. It reads imported partner accessions from the adjacent review and checks their explicit [sequence inputs](identity-sequences.fasta) against [identity provenance](identity-provenance.tsv). The provenance records official UniProt URLs, record and sequence digests, product lengths, taxa and alternative-sequence features. The frozen sequences are data inputs, not predicted sequences or inferred activity. [README.md](README.md) gives runnable commands.

| Output | Contents |
|---|---|
| [measurements.tsv](measurements.tsv) | All 1,344 DLG3 rows, original one-based sheet row numbers, and all 39 source columns. The single unnamed source column has an explicit generated header. |
| [source-row-crosswalk.tsv](source-row-crosswalk.tsv) | All 1,221 candidate joins, imported zero-based annotation index and literal accession, original peptide, separate sequence-mapping flags, and selection flag. |
| [run-summary.json](run-summary.json) | Counts and source/input digests computed by the parser. |

All 53,760 extracted cells were compared with the independently saved original-workbook projection. All 1,221 candidate mappings and their natural-sequence positions match the prior source crosswalk; the 1,203 selected row identifiers match the individually reviewed source projection. The same parser was also run against DLG4 and its own identity inputs: it extracted 1,344 measurements, 388 source rows and 1,197 candidate joins. That second-input check establishes parser generality, not a DLG4 scientific verdict.

## What the measurements establish

The study tests recombinant PDZ domains against synthetic motifs. LYSC uses bacterial lysates; SAPF and DAPF use single- and double-affinity-purified domain preparations. The stated binding-intensity thresholds are 0.1 for LYSC/SAPF and 0.05 for DAPF. The workbook's COMP field selects the preferred assay estimate; it is not an average of discordant assays. Each original assay field is retained separately.

A zero-coded composite indicates that the selected experiment did not supply a quantifiable affinity under its detection conditions. It is not a measured zero affinity, an affinity of 1 M, or proof of biological noninteraction. The authors explicitly discuss possible binding below the detection threshold. Conversely, a non-negative interaction-database flag is not an independent positive affinity measurement.

Positive motif binding supports molecular recognition at the actual fragment, modification and construct scope. It does not by itself establish a native full-length complex, colocalization, receptor activation, partner regulation, or activity of every DLG3 splice product. The review retains supported generic associations as non-core unless independent target-specific context supports a more informative partner-class function. GluN2 receptor recognition, FRMPD4/Preso binding and ERBB4-tail binding have such additional context, described in the [evidence guide](../DLG3-evidence-guide.md).

## Mapping cases that require explicit interpretation

| Imported row / partner | Source measurement and scope |
|---|---|
| 28 / GAGE12J | SD1 rows 9021, 55785 and 64021 test PEEGKKQSQC; row 9021 has composite pKd 4.03522737. The supplied current A6NER3 product has PEEGEKQSQC. These remain unmatched candidate rows; they are not counted among the 1,203 sequence-supported selections. A positive mismatched peptide does not settle the literal current-product assertion. |
| 47 / AXIN1 | The `natural_10mer` field is an internal-motif placeholder. Rows 8454, 34568 and 47894 specify the actual amidated internal ligand `Biotin-GSGSGS-TLSLTDSSVDGIPPYR-CONH2`; its amino-acid core matches AXIN1. These are the three additional selected rows. Row 8454 is positive; selection of the other two does not make their zero composites positive. |
| 93 / SARS-CoV-2 E | Row 21885 has LYSC/CALIP pKd 4.09810075 but selected DAPF/COMP zero. The discrepancy is retained rather than relabeled as universally undetected or proven native binding. |
| 166–167 / PDLIM4 products | The paper's isoform names differ from current UniProt names. Candidate accession joins are broader than exact sequence matches; literal product sequences determine the matched tails. Both mapped native tails are below quantification. |
| 226 / RPS6KA1 | Composite-positive measurements are confined to the minus-one-phosphorylated motif. The minus-three-phosphorylated motif also has a discordant LYSC/CALIP estimate at row 21824, while its selected composite is zero. No unmodified-tail affinity is inferred. |
| 383 / WHRN | The internal synthetic ligand ends in Y where the corresponding current sequence ends in F. The native C-terminal motif is below quantification. The internal positive is therefore retained among unmatched candidate observations, not exact native-product support. |
| 253 / ARHGAP17 and 408 / DLGAP4 | Tail measurements are below quantification, but independently curated AP-MS associations support non-core retention. Those captures do not establish the isolated-tail mechanism. |

The 120 unresolved source assertions comprise 117 below-quantification cases and the GAGE12J, SARS-CoV-2 E and WHRN identity/assay discrepancies. The evidence was inspected; the uncertainty is biological or measurement-specific rather than a claim that the paper was inaccessible. Imported supporting entities remain source metadata and are not rewritten to peptide identifiers.

## Reproducibility checks

- [x] The code reads explicit source and identity inputs; no result counts, affinity values, GO actions or gene-specific conclusions are hardcoded.
- [x] The published workbook version and identity sequence digests are checked before extraction.
- [x] All output values and mappings were compared with the separately saved original source projections.
- [x] The script completed on DLG3 and a distinct DLG4 input.
- [x] Direct outputs, dependency versions, commands and scientific limits are included here.
