# Ruegeria pomeroyi DSS-3 betC-1 / SPO1083 — 2026-11-06

BetC-1 is the choline-sulfatase enzyme assigned to the first step of COS utilization. [PMID:26058574, Comparative genomics and mutagenesis analyses of choline metabolism in the marine Roseobacter clade] reports: “However, this mutant strain failed to utilize COS as a carbon source, confirming that betC is essential for growth on COS.” The mutant still grows on choline and glycine betaine. This is gene-specific native genetics, with the hydrolytic reaction inferred from the independently recognized choline-sulfatase architecture (IPR017785, TIGR03417, PF12411) and characterized homologs; the paper does not purify and assay Ruegeria BetC.

The study's TableS1 primers establish that this is SPO1083, independently corroborated by [PMID:40801533, Novel regulatory mechanism of choline-O-sulfate and choline catabolism by two BetIs in Alphaproteobacteria], which reports: “betI1 was shown to be co-transcribed with betC (SPO1083)”. The later study measures regulatory mechanisms, not a new BetC turnover assay. Its transcriptional and salinity phenotypes do not warrant adding an osmoprotection process to this enzyme.

The broad sulfuric-ester hydrolase row is refined to the already supported choline-sulfatase activity. Cytoplasmic localization is plausible but left UNDECIDED because the accessible DSS-3 experiments do not locate the hydrolytic step, and the review does not force a core compartment. No target-specific metal preference, processed formylglycine residue, kinetic constant, phosphorylcholine reaction or promiscuous phosphatase activity is transferred from another sulfatase. The PANTHER label IDURONATE 2-SULFATASE is a classification label and is not evidence for that substrate.

The proposed COS-catabolic process names the chemistry BetC itself performs. It is not choline catabolism: choline is the hydrolysis product. Its parent is sulfur compound catabolic process. Same-role O69787 and Q88RQ2 comparator checks show enzyme annotations but no exact COS process, and the local GO-CAM index has no target entry. No positive NEW BP is manufactured from deletion necessity alone; a specific ontology term is proposed with the actual catalytic-role evidence.

## Identity and source preservation

The standard normal-fetch workflow seeded the review before any edits. Baseline document, non-review annotation payloads and raw SHA256 hashes are in `.cache/module-audit-logs/choline-sulfate-20261106/ruegeria-new-members-baseline.json`. No raw UniProt/GOA or publication cache was edited. Both primary papers are available as normally fetched full text.

The official 2015 supplement and genomic/protein deposits are preserved in `betC-1-source-analysis/` under the betC-1 directory. Twelve locus-specific mutant primers map uniquely to CP000031.2; AAV94383.1 and AAV94387.1 match the complete frozen Q5LUH1 and Q5LUG7 sequences, respectively. The first is betC-1/SPO1083, not the second BetC-like paralog betC-2/SPO2214. The organism is DSS-3 in both studies and records; no strain substitution is required. `verify_identity.py` reproduces the checks. The analysis records exact source URLs, original/derived-file distinctions and hashes.

## Provider and validation

The normal Falcon command was attempted for this gene and failed with HTTP 403 authentication. Its actual stdout/stderr are logged under `.cache/module-audit-logs/choline-sulfate-20261106/falcon-RUEPO-betC-1.log`. No provider report was fabricated; these are manual research notes. The original annotation payloads and raw hashes are checked again after review, and focused review/history validation is recorded in the same log directory.
