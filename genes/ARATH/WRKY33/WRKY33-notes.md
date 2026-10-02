# WRKY33 (At2g38470, Q8S8P5) curation notes

## 2026-10-02 initial review

Sources: UniProt record, GOA (40 rows), falcon deep research, cached papers (full text for PMID:21498677, 22392279, 30228125, 15990873, 21203436; others abstract-only).

### Molecular function
- Group I WRKY TF, two WRKY domains; binds W-box. [PMID:17059405 "WRKY33 is localized to the nucleus of plant cells and recognizes DNA molecules containing the TTGACC W-box sequence"]
- EMSA specificity: [PMID:21498677 "Inclusion of unlabeled W-box, but not GCC-box or as-1 box, in the binding reaction effectively competed the binding of WRKY33 to the 32 P-labeled W-box probe"]
- MPK3/MPK6 phosphorylate 5 N-terminal Ser; phosphorylation does not change DNA binding, likely affects transactivation. [PMID:21498677 "Mutation of MPK3/MPK6 phosphorylation sites in WRKY33 compromises its ability to complement the camalexin induction in the wrky33 mutant"]
- SIB1/SIB2 (VQ) coactivators stimulate DNA binding. [PMID:21990940 "The two VQ motif-containing proteins recognize the C-terminal WRKY domain and stimulate the DNA binding activity of WRKY33"]
- MPK4-MKS1 holds WRKY33 in the nucleus until pathogen-triggered release. [PMID:18650934 "in the absence of pathogens, Arabidopsis MAP kinase 4 (MPK4) exists in nuclear complexes with the WRKY33 transcription factor"]

### Camalexin (project curation question 3: necessity vs participation)
- WRKY33 binds PAD3 and CYP71A13 promoters. [PMID:22392279 "For CYP71A13 , we observed strong inducible binding at −2,800 bp, again indicating direct positive regulation by WRKY33"]
- But camalexin induction is only delayed in wrky33 in Birkenbihl et al. [PMID:22392279 "we found that WRKY33 is not absolutely essential to promote Botrytis -induced camalexin production"]
- The biosynthetic steps are catalysed by CYP71A13 and PAD3, not WRKY33, so the IMP "camalexin biosynthetic process" row is MODIFIED to GO:1901183 positive regulation of camalexin biosynthetic process (same choice as genes/ARATH/MPK3; CYP71B15 keeps the biosynthesis term as the enzyme).
- "defense response to fungus" accepted: robust IMP + overexpression phenotype, and WRKY33 does transcriptional work in the response beyond camalexin.

### Other processes (non-core)
- Salt: moderate mutant phenotype [PMID:18839316 "wrky33 null mutants and wrky25wrky33 double mutants showed only a moderate increase in NaCl-sensitivity"]
- Heat: redundant with WRKY25/26; WRKY33 expression repressed by heat [PMID:21336597 "whereas WRKY33 expression was repressed"]
- SAR via ALD1 [PMID:30228125 "Chromatin immunoprecipitation showed that WRKY33 binds to the ALD1 promoter"]
- Autophagy induction [PMID:21395886 "Induction of ATG18a and autophagy by B. cinerea was compromised in the wrky33 mutant"]
- Defense to bacterium: loss-of-function shows no change in Zheng 2006 [PMID:17059405 "The wrky33 mutants do not show altered responses to a virulent strain of the bacterial pathogen Pseudomonas syringae"]; kept as non-core given SAR data.

### Protein binding rows
- SIB1 -> MODIFY to transcription coregulator binding (GO:0001221), demonstrated coactivator.
- MKS1 (x3), MPK4, ATG18a, VQ1, VQ10 -> REMOVE (uninformative; interactions not disputed).

Validation: passes with no warnings.
