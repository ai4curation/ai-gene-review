# coq7 (PP_0427, Q88QR1) - Pseudomonas putida KT2440 - curation notes

## 2026-11-11 audit (ubiquinone_biosynthesis module)

No Perplexity/Falcon/OpenAI deep research available (no provider keys); OpenScientist report
read. Reviewed UniProt entry (HAMAP MF_01658). No KT2440 experiment.

- Does P. putida use Coq7 for the late hydroxylation? Yes, by three lines: (1) KT2440 has no
  UbiF (its two UbiH/COQ6-family proteins are UbiI PP_5197 and UbiH PP_5199; see
  `../visC/visC-bioinformatics/RESULTS.md` and the project pathway report); (2)
  [PMID:27822549 "Pseudomonas aeruginosa and Thiobacillus ferrooxidans ... lack ubiF but
  possess instead a Coq7 homolog"]; (3) [PMID:11435415 "We have cloned COQ7 from Pseudomonas
  aeruginosa ... and show that indeed this gene complements an Escherichia coli mutant that
  lacks an unrelated 5-demethoxyubiquinone hydroxylase."]
- Mechanism (human ortholog): [PMID:23445365 "functions as a 5-demethoxyubiquinone-hydroxylase,
  utilizing its carboxylate-bridged diiron center."]
- Numbering: Pelosi 2016 calls this C-6; older papers and the deep research say C-5.
- PAINT PTHR11237: root PTN004246703 GO:0006744 (seeds incl. P. aeruginosa Q9I5R6) and
  GO:0160224 (NADH-specific DMQ hydroxylase, eukaryotic seeds). Not proposed as NEW because the
  bacterial electron donor is unknown.
- Decisions: GO:0008682, GO:0006744, GO:0005886 ACCEPT; GO:0004497 MODIFY to GO:0008682.

Module agreement: `coq7_demethoxyubiquinol_hydroxylase_activity` (GO:0008682, plasma
membrane). Consistent.
