# purH (Escherichia coli K-12, UniProtKB:P15639) notes

## 2026-11-13 review for the de_novo_purine_synthesis module

PurH is the bifunctional AICAR transformylase/IMP cyclohydrolase of Escherichia coli, a soluble cytosolic enzyme that catalyses the last two steps of de novo IMP biosynthesis: formylation of 5-aminoimidazole-4-carboxamide ribonucleotide (AICAR) with 10-formyltetrahydrofolate to FAICAR, and cyclodehydration of FAICAR to IMP. It is encoded with purD in the purHD operon.

### Provenance

No provider deep-research report was generated for this gene. These notes were written by the reviewer from: the fetched UniProt record (file:ECOLI/purH/purH-uniprot.txt), the cached primary publications cited below (most abstract-only; full_text_available is recorded in each publications/PMID_*.md file), the PANTHER family reviews under interpro/panther/, and the P. putida, yeast and human orthologue reviews used as precedents.


### Core function evidence

- phosphoribosylaminoimidazolecarboxamide formyltransferase activity (GO:0004643):
  [PMID:2687276 "The E. coli purH gene, therefore, specifies bifunctional 5'-phosphoribosyl 5-aminoimidazole-4-carboxamide transformylase-IMP cyclohydrolase."]
- IMP cyclohydrolase activity (GO:0003937):
  [PMID:2687276 "The E. coli purH gene, therefore, specifies bifunctional 5'-phosphoribosyl 5-aminoimidazole-4-carboxamide transformylase-IMP cyclohydrolase."]

### Decisions other than ACCEPT

- GO:0006164 purine nucleotide biosynthetic process (IEA, GO_REF:0000002): MODIFY -> GO:0006189. Correct but general process; PurH acts specifically in de novo IMP biosynthesis.

Precedents followed: PSEPK pur* reviews, yeast ADE2/ADE5,7 and the PANTHER family reviews (PTHR10520 TOO_DEEP GAR synthetase node; PTHR11609 WRONG_NODE for GO:0004638 and GO:0006144).
