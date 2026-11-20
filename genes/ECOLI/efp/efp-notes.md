# efp (E. coli K-12, UniProtKB:P0A6N4) review notes

## Deep research status

Provider deep research (`just deep-research*`) was not run: no provider API keys were
available in this environment. No `-deep-research-*.md` file exists for this gene. The
literature basis for the review is the curated UniProt entry (`efp-uniprot.txt`) and the
cached publications listed below. They were fetched with `just fetch-gene-pmids ECOLI efp`,
and most are abstract-only.

Publications checked: PMID:1105576, PMID:18201202, PMID:23239623, PMID:23239624,
PMID:25843707 (full text), PMID:26009254 (full text), PMID:29100052, PMID:39622818 (full
text), PMID:9405429, PMID:20729861, PMID:21841797 (full text), PMID:22128152, PMID:22706199.

## Function

- Discovery: a soluble factor that stimulates fMet-puromycin synthesis on 70S ribosomes, named EF-P
  [PMID:1105576 "regard it as a new factor required for peptide chain elongation, which we call EF-P"].
- Localization: [PMID:1105576 "Over 90% of this activity was found in the ribosome-free cytoplasm of Escherichia coli extracts."]
- Polyproline rescue (2013):
  [PMID:23239623 "In the absence of EF-P, ribosomes stall at polyproline stretches, whereas the presence of EF-P alleviates the translational stalling."]
  [PMID:23239624 "EF-P promotes peptide-bond formation and stabilizes the peptidyl-transfer RNA in the catalytic center of the ribosome."]
- Structure: [PMID:29100052 "Binding of EF-P stabilizes the P-site tRNA, particularly via interactions between its modification and the CCA end"];
  UniProt SUBUNIT: "In stalled 70S ribosomes binds in the tRNA E-site, stabilizing the peptidyl-tRNA".
- In vivo profiling: [PMID:25843707 "We find that loss of EFP amplifies pausing at the vast majority of instances of Pro-Pro in the genome."]
  The same effect is seen in epmA/epmB mutants but not in epmC mutants.
- Frameshifting: [PMID:26009254 "Suppression of +1FS errors requires the m(1)G37 methylation of tRNA(Pro) on the 3' side of the anticodon and the translation factor EF-P."]
- Paralog EfpL overlap and EF-P-induced pauses: [PMID:39622818 "Notably, the two factors can also induce pauses."]
- Essentiality: [PMID:9405429 "We conclude that the efp gene is essential for cell viability and is required for protein synthesis."]
  Other strain backgrounds grow very slowly instead (UniProt DISRUPTION PHENOTYPE, PMID:20729861).

## Modification (Lys34)

- EpmA (PoxA/GenX/YjeA) lysylates EF-P [PMID:20729861 "it specifically aminoacylates EF-P with lysine"].
- (R)-beta-lysine is the functional moiety [PMID:21841797 "EF-P was efficiently functionally modified with (R)-β-lysine but not (S)-β-lysine"].
- The modification is needed for activity [PMID:22128152 "The mutant lacking the modification site lysine (K34A) was inactive."].
- EpmC (YfcM) adds a final hydroxylation [PMID:22706199 "lacks a final hydroxylation step mediated by YfcM"].

## Curation decisions and consistency with genes/PSEPK/efp

- The shared terms (GO:0003746, GO:0006414, GO:0072344, cytoplasm, cytosol) are ACCEPTed. GO:0006417 regulation of
  translation and GO:0043043 peptide biosynthetic process are KEEP_AS_NON_CORE. All of these match the P. putida EF-P review.
- GO:0043043: in the current GO, translation is under GO:0160307 protein biosynthetic process and is no
  longer an is_a descendant of peptide biosynthetic process. The InterPro2GO mapping from IPR015365 is therefore
  a weak fit. It is kept as non-core for sibling consistency; the mapping could be raised upstream.
- GO:0043022 ribosome binding (IDA, PMID:18201202) is KEEP_AS_NON_CORE. Binding is mechanistically real, but the core MF is the
  elongation factor activity.
- GO:2001125 negative regulation of translational frameshifting (IMP, PMID:26009254) is KEEP_AS_NON_CORE. It is a secondary
  result of P-site tRNA(Pro) stabilization.
