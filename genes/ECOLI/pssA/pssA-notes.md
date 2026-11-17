# pssA (Escherichia coli K-12, P23830) notes

## Deep research status

Automated deep research was attempted on 2026-11-09 with
`just deep-research-falcon ECOLI P23830 --alias pssA`; the provider failed
authentication ("falcon: 403 Failed to authenticate"), so no provider file
exists. No `-deep-research-*.md` file was written by hand. The review below
rests on the cached publications listed in the review YAML and the curated
UniProt record.

## Literature checked

- PMID:39693441 (full text cached): crystal structures of E. coli PssA with and
  without CDP-diacylglycerol; defines type-I (PLD-superfamily, peripheral) vs
  type-II (CDP-alcohol phosphotransferase, integral) PssA. Active state is on
  the inner membrane surface, cytosolic form inactive
  [PMID:39693441 "the active state of PssA is associated with the inner membrane surface, contributing to PS synthesis, while the cytosolic form is inactive in this synthesis process"].
- PMID:179992 (abstract): pss-8 temperature-sensitive mutant; PE drops from 66%
  to 32% of lipid phosphorus at 44 degrees
  [PMID:179992 "After 3 hours at 44 degrees the level of phosphatidylethanolamine drops from 66 to 32%"].
- PMID:49056 (abstract): replica-printing screen that isolated thermolabile
  phosphatidylserine synthetase mutants.
- PMID:193099 (abstract): plasmid overproduction and purification to
  homogeneity of the synthase; enzyme associates with the ribosomal fraction of
  crude extracts.
- PMID:19072541 (abstract): recombinant E. coli PSS expressed in B. subtilis,
  purified and characterized.
- PMID:10692325 (abstract): biphasic binding of PS synthase to lipid bilayers,
  strengthened by anionic lipids (PA, PG).
- PMID:16294310 (abstract): split-tag TAP and bacterial two-hybrid identify
  PssA in a network with ACP, YbgC and PlsB at the inner membrane.
- PMID:18304323 (full text cached, supplementary table not cached): cytosol
  proteomics of E. coli MC4100; the PssA hit itself is in supplementary data.

## Interpretation

PssA is a type-I phosphatidylserine synthase (PLD superfamily, two HKD motifs,
PTHR12586). The InterPro IPR016270 (PGS1) mapping to GO:0008444 and
GO:0032049 transfers the eukaryotic phosphatidylglycerophosphate synthase
function of the same superfamily lineage; E. coli uses PgsA (a CDP-alcohol
phosphatidyltransferase) for that reaction, so these rows are removed.
