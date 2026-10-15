# LYK4 (At2g23770, O64825) notes

## Sources
- UniProt O64825; GOA (19 rows); deep research `LYK4-deep-research-falcon.md`.
- Cached papers: PMID:22744984 (Wan 2012; Discussion/Conclusion in full text, no Results), PMID:25340959 (Cao 2014, full text), PMID:31270545 (Xue 2019, abstract only), PMID:32284410 (Cheval 2020, full text).

## Identity and domains
- Signal peptide 1-22, extracellular 23-275 with 3 LysM motifs, TM 276-296, cytoplasmic kinase-like domain (UniProt).
- Pseudokinase: [PMID:22744984 "LYK4 also appears to be an inactive kinase, since the comparison of the LYK4 kinase domain with other typical kinases revealed that certain key residues are missing"]; [PMID:22744984 "kinase assays using recombinant LYK4 protein isolated after expression in Escherichia coli failed to show phosphorylation of the common kinase substrate Myelin Basic Protein"].
- So kinase activity IEAs (InterPro, EC, Rhea) are removed; ATP binding marked over-annotated (same as LYK5).

## Chitin perception
- Chitin-bead pull-down: [PMID:22744984 "We repeated this experiment and also found that LYK1, LYK4, LYK5, and CEBiP-like1 were pulled down by chitin magnetic beads and eluted by chitooctaose"]. Weak competition: [PMID:25340959 "whereas the binding with AtCERK1 or AtLYK4 was only slightly reduced by the same competitors"]. No Kd for LYK4.
- Redundancy with LYK5: [PMID:25340959 "Atlyk4/Atlyk5-2 double mutant plants show a complete lack of response to chitin, similar to the Atcerk1 mutants"].
- Complex: [PMID:25340959 "AtLYK4 interacts with AtCERK1 independently of the presence of chitin"]; [PMID:31270545 "our data suggest that LYK4 functions as a LYK5-associated co-receptor or scaffold protein that enhances chitin-induced signaling in Arabidopsis"].
- MF choice: coreceptor activity (GO:0015026) proposed NEW rather than PRR activity (GO:0038187, used for LYK5 and for the LYK4/LYK5 family annoton in modules/chitin_perception.yaml). Rationale: authors call LYK4 a co-receptor/scaffold; LYK5 is the main binder. Flagged as a question.

## Bacterial response
- lyk4 more susceptible to Pst DC3000, but [PMID:22744984 "the mutations in LYK1 and LYK4 have a negligible impact on fls22 or elf26 signaling"]; bacterial ligand only speculated. GO:0071219 rows (IBA, IEP) marked over-annotated.

## Plasmodesmata
- [PMID:32284410 "We detected PDLP5-HA and LYK4-HA in purified plasmodesmata extracts, but not LYK5-HA or H+-ATPase"]; [PMID:32284410 "Thus, LYK4 and LYK5 are required for chitin-triggered plasmodesmata closure and are candidate partners for LYM2-mediated signaling."]. CERK1 is not required for this branch. Added plasmodesma (GO:0009506) as NEW location. No regulation-of-plasmodesmal-transport GO term exists (see LYM2 review proposal).

## Other
- Chloroplast ISM removed (signal peptide misread).
- Erwig 2017 (PMID:28513921) abstract concerns LYK5/CERK1 only; deep research claims LYK4 is trans-phosphorylated by CERK1 and CPK5/6, not verifiable from cached abstracts, so not used.
