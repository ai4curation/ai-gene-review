# mei-41 (Drosophila ATR) review notes

## Identity
- UniProt Q9VXG8 (ATR_DROME), CG4252; PI3/PI4-kinase family, ATM subfamily; partner mus304 (ATRIP).

## Literature journal
- Checkpoint: mei-41, grapes (Chk1) and 14-3-3epsilon regulate the IR-induced checkpoint in the eye disc [PMID:10733527 "We show that several Drosophila homologs of checkpoint genes, mei-41, grapes, and 14-3-3epsilon, regulate a DNA damage checkpoint in the developing eye."]
- Replication checkpoint in embryos: [PMID:11676920 "indicating that a mei-41-dependent checkpoint acts to delay the entry into mitosis in response to incomplete DNA replication"]; [PMID:29746464 "The Mei41-dependent replication checkpoint is essential during cycle 13 to prevent premature entry into mitosis"].
- Claspin mediates HU but not IR G2 arrest, whereas mei-41 is needed for both [PMID:22796626 "IR-induced G2 arrest, which was severely defective in mei-41/ATR and grp/Chk1 mutants, occurred normally in the Claspin mutant"].
- DSB repair: [PMID:17194776 "We found that mei-41 mutants are defective in completing the later steps of homologous recombination repair, but have no defects in end-joining repair."]; SDSA defect is in the late steps [PMID:17194776 "Our results suggest that the diminished ability of mei-41 mutants to repair DSBs through SDSA occurs during the final steps—annealing and ligation"]. SSA effect is modest [PMID:17194776 "In mei-41 mutants, 82% of the progeny resulted from SSA."].
- Telomeres: redundant with ATM [PMID:16203987 "the loss of ATM leads to the fusion of some telomeres, whereas the loss of both ATM and ATR renders all telomeres susceptible to fusion"].
- Meiosis: ATR needed for meiotic checkpoint; phosphorylates H2Av [PMID:22024169 "ATR mutant analysis indicated that it is required for checkpoint activity, whereas ATM may not be. Both kinases phosphorylate H2AV"]. PCH2 checkpoint delays do not depend on mei-41 [PMID:18957704 "the delays in meiotic progression do not depend on DSB formation or on mei-41"].
- Chromosome condensation IGI is indirect [PMID:17227890 "indicating that the defect in chromosome condensation is independent of checkpoint activation and that, in the absence of the checkpoint, the severity of the chromosome condensation defect is enhanced"].

## Curation decisions
- Core: protein Ser/Thr kinase activity in DNA damage and replication checkpoint signaling, in the ATR-ATRIP complex; secondary core role in SDSA completion.
- GO:0000706 (meiotic DSB processing = resection) marked over-annotated; ATR is not a resection enzyme.
- Developmental TAS terms from a general review (cellularization, imaginal disc development) marked over-annotated.
- PMID:10559981 is an S. pombe Rad3-Rad26 paper used as NAS/IPI; locations/complex kept as biologically correct.
- Deep research (falcon) completed after a retry; see update below.

## Deep research (falcon) update
- [file:DROME/mei-41/mei-41-deep-research-falcon.md "Mei-41 has a specific role beyond a generic cell-cycle checkpoint in generating normally patterned female meiotic crossovers."] (Brady et al. 2018), so reciprocal meiotic recombination was upgraded from non-core to ACCEPT.
- The deep research notes that mei-41 RNAi did not suppress DSB-induced apoptosis in Wg-compromised wing discs (2024), so MEI-41 is not needed for every damage-induced apoptotic output.
