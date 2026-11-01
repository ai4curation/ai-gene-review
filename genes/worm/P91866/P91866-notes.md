# P91866 (F32H2.6) review notes

## 2026-10-28 initial review

- fetch-gene resolved P91866 itself (GeneID 185214, WBGene00009343); GOA has one row:
  GO:0016746 acyltransferase activity, IEA, InterPro2GO via IPR016039 (Thiolase-like).
- Only literature: Kniazeva et al. 2004 (PMID:15340492), which calls F32H2.6 a shorter homolog of
  fasn-1 (F32H2.5) that "can only encode the N-terminal portion of the protein", and warns that RNAi
  of one could affect the other [PMID:15340492 "These genes share extended nucleotide identity, and
  RNAi of one could thus possibly affect the other."].
- Alignment (P91866-bioinformatics/RESULTS.md): matches FASN-1 28-194 at 67% identity, ending just
  before the KS catalytic Cys (human FASN C161); no catalytic His either; no KS C-terminal subdomain.
- Decision: REMOVE the IEA acyltransferase row (InterPro2GO applied to a fragment lacking every KS
  catalytic residue; a demonstrably wrong electronic mapping for this product). Recorded as a
  source defect against InterPro (resource OTHER).
- No NEW terms: the RNAi phenotype is confounded by cross-targeting of fasn-1, and phenotypes are
  not evidence of participation anyway. No core function asserted; core_functions left empty.
- Open: is F32H2.6 a transcribed pseudogene / partial duplication? Is a protein made?
