# PDIA4 (donkey, A0A8C4LTV9) - review notes

DONKEY40 cohort. 11 IEA GOA rows.

## Chimeric gene model (key finding)
- The entry is 1197 aa; human PDIA4 (P13667) is 645 aa. Donkey record: [file:EQUAS/PDIA4/PDIA4-uniprot.txt "SIMILARITY: Belongs to the krueppel C2H2-type zinc-finger protein family."] and ["SIMILARITY: Belongs to the protein disulfide isomerase family."]; domains: KRAB (9-80), ten C2H2 zinc fingers, then thioredoxin domains.
- [file:EQUAS/PDIA4/PDIA4-bioinformatics/ALT_ENTRY.md "A0A8C4LTV9 (1197 aa) residues 571-1197 align locally to P13667 (645 aa) residues 17-645"]. The human signal peptide (1-20) has no contiguous counterpart: [file:EQUAS/PDIA4/PDIA4-bioinformatics/RESULTS.md "SIGNAL : human [1, 20] MA -> donkey [1, 541] MS"] (residues scattered over 541 donkey positions by the global aligner).
- Second donkey entry from the same Ensembl gene, A0A8C4PKQ4 (664 aa), also begins with a KRAB A-box-like sequence: [ALT_ENTRY.md "First 30 residues of A0A8C4PKQ4: MAEPARLPLTFEDVAIYFSEQEWQKLEAWQ"], and is 100% identical to A0A8C4LTV9 over the PDI region.
- Interpretation: Ensembl gene-model fusion of a neighbouring KRAB-ZNF gene to PDIA4 (signal-peptide exon missed). Horse also has a 1248-aa PDIA4 entry (F6WGL8) besides 645-aa entries (UniProt search, 2026-10-14), consistent with an annotation issue in equid assemblies. Not experimentally verified.
- PDI catalytic sites conserved: ["DISULFID Redox-active: human [91, 94] CC -> donkey [643, 646] CC"], ["DISULFID Redox-active: human [555, 558] CC -> donkey [1107, 1110] CC"]; C-terminal REEL vs human KEEL.

## Function
- [PMID:16677074 "An examination of the pH-dependence and nature of the rate limiting step for the peptide thiol-disulfide oxidase activity of these enzymes reveals that, with the exception of PDIr, they are all remarkably similar."] (ERp72 = PDIA4 among the six).
- Human UniProt: [file:EQUAS/PDIA4/PDIA4-bioinformatics/human-P13667-uniprot.txt "SUBCELLULAR LOCATION: Endoplasmic reticulum lumen"]; chaperone complex with HSPA5/HSP90B1/PDIA6.

## Decisions
- Accept PDI activity, ER lumen, protein folding. REMOVE nucleus and regulation of DNA-templated transcription (both from the fused KRAB-ZNF part). Melanosome and cell redox homeostasis over-annotated.
- ProtNLM2 GO:0003690 double-stranded DNA binding: driven by the zinc-finger segment (evidence phmmer hit to mouse ZNF148, Q61624); not PDIA4 biology -> NPI, WRONG_INPUT_SEQUENCE.
