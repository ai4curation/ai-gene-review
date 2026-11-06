# Ruegeria pomeroyi DSS-3 SPO1087 / BetT — 2026-11-06

The standard symbol remains the locus SPO1087, as in the fetched UniProt record; betT is recorded as an experimentally assigned alias. The primary studies identify the same locus. The frozen record contains a 400-residue multipass membrane protein with eleven predicted helices, but no PANTHER/InterPro/Pfam family assignment. The 2015 paper calls it BCCT-type; no family ID is invented from that label.

[PMID:26058574, Comparative genomics and mutagenesis analyses of choline metabolism in the marine Roseobacter clade] reports: “Consequentially, the rate of choline depletion was also severely reduced (84%) compared with that of the wild‐type”. This follows deletion-mutant growth and ion-chromatographic measurements of culture-medium choline. It supports a choline-transporter assignment by IMP; it is not an isolated-protein, initial-rate tracer or reconstituted membrane-flux measurement. The co-transcribed betA and insertion design mean that a clean nonpolar deletion/complementation experiment would further resolve downstream effects.

The COS phenotype is not absent: growth remains but slows 38% (0.027 versus 0.043 per hour). This is consistent with a contribution to COS utilization, but does not identify transported cargo. The methods explicitly state: “All amines and ammonium, apart from COS, were quantified using a cation‐exchange ion chromatograph”. Thus no COS depletion or uptake rate was measured. Retained growth cannot prove that BetT excludes COS, and decreased growth cannot prove that it directly transports COS.

[PMID:40801533, Novel regulatory mechanism of choline-O-sulfate and choline catabolism by two BetIs in Alphaproteobacteria] Figure1 labels BetT a choline/COS transporter. The actual work addresses BetI-mediated regulation and confirms co-transcription of betT-betA (SPO1087–1088); neither the diagram nor induction by COS is a new substrate-flux assay. COS cargo remains unresolved, not rejected. The unchanged glycine-betaine growth phenotype similarly does not justify a NOT-transport annotation.

Two NEW proposals are supported: choline transmembrane transporter activity (IMP) and plasma membrane (IC from uptake function plus eleven predicted helices). Choline transport BP is already on the MF's part_of path, so a redundant NEW BP is omitted. No sodium/proton coupling, glycine-betaine exclusion, direct COS transport, osmoprotection or downstream catabolic process is asserted. E.coli BetT P0ABC9 supplies a same-role annotation-convention check, not evidence for target-specific substrate or coupling properties. No GO-CAM index entry was found.

## Identity and source preservation

The standard normal-fetch workflow seeded the review before any edits. Baseline document, non-review annotation payloads and raw SHA256 hashes are in `.cache/module-audit-logs/choline-sulfate-20261106/ruegeria-new-members-baseline.json`. No raw UniProt/GOA or publication cache was edited. Both primary papers are available as normally fetched full text.

The official 2015 supplement and genomic/protein deposits are preserved in `betC-1-source-analysis/` under the betC-1 directory. Twelve locus-specific mutant primers map uniquely to CP000031.2; AAV94383.1 and AAV94387.1 match the complete frozen Q5LUH1 and Q5LUG7 sequences, respectively. The first is betC-1/SPO1083, not the second BetC-like paralog betC-2/SPO2214. The organism is DSS-3 in both studies and records; no strain substitution is required. `verify_identity.py` reproduces the checks. The analysis records exact source URLs, original/derived-file distinctions and hashes.

## Provider and validation

The normal Falcon command was attempted for this gene and failed with HTTP 403 authentication. Its actual stdout/stderr are logged under `.cache/module-audit-logs/choline-sulfate-20261106/falcon-RUEPO-SPO1087.log`. No provider report was fabricated; these are manual research notes. The original annotation payloads and raw hashes are checked again after review, and focused review/history validation is recorded in the same log directory.
