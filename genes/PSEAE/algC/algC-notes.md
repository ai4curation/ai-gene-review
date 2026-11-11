# algC (P26276, PA5322) — Pseudomonas aeruginosa PAO1 — curation notes

## Deep research

- 2026-10-23: `just deep-research PSEAE algC --provider perplexity` failed
  ("Provider 'perplexity' not available. Available: falcon, openscientist").
  No deep-research file was generated; the review is built from cached primary
  literature and the curated UniProt entry. Additional papers were cached with
  `just fetch-pmid` (PMIDs 10481091, 11839312, 14725765, 11716469, 16595672,
  16880541, 18690721, 22242625).

## Enzymology

- Bifunctional PMM/PGM, monomer of 50 kDa [PMID:8050998 "The enzyme was determined to be a monomer with a molecular mass of 50 kDa."]
- Both reactions on purified enzyme [PMID:8050998 "The enzyme catalyzed the interconversion of mannose 1-phosphate (M1P) and mannose 6-phosphate, as well as that of glucose 1-phosphate (G1P) and glucose 6-phosphate."]
- Km values and efficiency [PMID:8050998 "The apparent Km values for M1P and G1P were 17 and 22 microM, respectively."; "the catalytic efficiency for G1P was about twofold higher than that for M1P"]
- Mg2+ requirement [PMID:8050998 "Purified PMM/phosphoglucomutase (PGM) required Mg2+ for maximum activity"]; Mg2+-binding loop in structure [PMID:16880541 "a metal-binding loop which coordinates the Mg 2+ ion necessary for activity"]; Zn2+ in crystals gives inactive enzyme [PMID:16880541 "catalytically inactive owing to substitution of Zn 2+ in the Mg 2+ -binding site"].
- Mechanism: phosphoenzyme at Ser108, bisphosphate intermediate reorients [PMID:11716469 "the enzyme phosphorylates the substrate to generate a bisphosphorylated intermediate that reorients in the active site to return its original phosphoryl group to the enzyme"]; processive reorientation [PMID:16595672 "Reorientation of the intermediate occurs without dissociation from the active site of the enzyme"].
- Dual substrate recognition in one site [PMID:14725765 "The ability of PMM/PGM to accommodate these four diverse substrates in a single active site is consistent with its highly reversible phosphoryl transfer reaction"].
- General base His329 [PMID:23517223 "His329 is appropriately positioned to abstract a proton from the O1/O6 hydroxyl of the phosphosugar substrates, and thus may serve as the general base in the reaction"].
- Four-domain structure, domain 4 closes active site [PMID:11839312 "Residues from all four domains of the protein contribute to the formation of a large active site cleft"; PMID:18690721 "binding of substrates produces a rotation of the C-terminal domain"].

## Physiological roles (genetics)

- Alginate: algC identified as the PMM gene of the alginate pathway, AlgR-activated [PMID:1903398 "suggesting that the algR1 gene product activates the transcription of the algC gene"].
- LPS core and O antigen [PMID:7515870 "did not express lipopolysaccharide (LPS) O side chains or the A-band (common antigen) polysaccharide"; "the synthesis of glucose 1-phosphate is necessary in the biosynthesis of the P. aeruginosa LPS core"].
- Both activities absent in algC mutants [PMID:8050998 "PMM and PGM activities could not be detected in nonmucoid algC mutant strain 8858 and in LPS-rough algC mutant strain AK1012"].
- Rhamnolipid [PMID:10481091 "presumably catalyzing the first step in the deoxy-thymidine-diphospho-L-rhamnose (dTDP-L-rhamnose) pathway, the conversion of glucose-6-phosphate to glucose-1-phosphate"].
- Psl and Pel; precursor checkpoint [PMID:22513190 "AlgC, a key enzyme that provides sugar precursors for the synthesis of alginate and lipopolysaccharides (LPS) is also required for both Psl and Pel production"; "we propose that AlgC is a key checkpoint enzyme"].

## Curation decisions

- MF: GO:0004614 and GO:0004615 accepted on all evidence codes; GO:0016868 MODIFY to both.
- GO:0000287 magnesium ion binding accepted (IDA and IEA): one Mg2+ per subunit, structurally resolved, kinetically required.
- Process: direct products are mannose 1-P (-> GDP-mannose via AlgA -> alginate, A-band, Psl) and glucose 1-P (-> UDP-glucose -> LPS outer-core glucose; -> dTDP-rhamnose). Accepted GDP-mannose biosynthesis (GO:0009298), alginate (GO:0042121), LPS core (GO:0009244). Proposed GO:0120530 UDP-alpha-D-glucose biosynthetic process as replacement for GO:1901137. GO:0005975 and GO:0009103 MODIFY to the specific terms the gene already carries.
- O antigen (GO:0009243): KEEP_AS_NON_CORE; the defect is secondary to core truncation (B-band) and to GDP-mannose-derived A-band precursors, upstream of O-antigen assembly.
- Rhamnolipid biosynthesis (GO:0106236) not added as NEW: evidence is necessity (mutant phenotype) for a precursor step; left as a suggested question pending a comparator check against RmlA-D annotation.
- No subcellular location asserted in core functions: no direct localization evidence in cached sources (soluble enzyme expected).
