# purM (Escherichia coli K-12, UniProtKB:P08178) notes

## 2026-11-13 review for the de_novo_purine_synthesis module

PurM is the aminoimidazole ribonucleotide (AIR) synthetase of Escherichia coli, a soluble homodimeric ATP-dependent cyclo-ligase that closes the imidazole ring of formylglycinamidine ribonucleotide (FGAM) to form AIR, the fifth step of de novo IMP biosynthesis. It is a standalone enzyme; in animals and fungi the same activity is a domain of multifunctional GART or ADE5,7-type proteins.

### Provenance

No provider deep-research report was generated for this gene. These notes were written by the reviewer from: the fetched UniProt record (file:ECOLI/purM/purM-uniprot.txt), the cached primary publications cited below (most abstract-only; full_text_available is recorded in each publications/PMID_*.md file), the PANTHER family reviews under interpro/panther/, and the P. putida, yeast and human orthologue reviews used as precedents.


### Core function evidence

- phosphoribosylformylglycinamidine cyclo-ligase activity (GO:0004641):
  [PMID:3530323 "AIR synthetase has been shown to catalyze the transfer of the formyl oxygen of [18O]formylglycinamide ribonucleotide to Pi."]

### Decisions other than ACCEPT

- GO:0004637 phosphoribosylamine-glycine ligase activity (IBA, GO_REF:0000033): REMOVE. GAR synthetase activity belongs to the GARS domain of eukaryotic fusions, which PurM lacks.
- GO:0005737 cytoplasm (IEA, GO_REF:0000120): MODIFY -> GO:0005829. Correct but general location; the gene also carries the more specific cytosol term.
- GO:0006164 purine nucleotide biosynthetic process (IBA, GO_REF:0000033): MODIFY -> GO:0006189. Correct but general process; PurM acts specifically in de novo IMP biosynthesis.
- GO:0046084 adenine biosynthetic process (IBA, GO_REF:0000033): MODIFY -> GO:0006189. Adenine (free base) biosynthesis is not what PurM does; the pathway yields IMP.

Precedents followed: PSEPK pur* reviews, yeast ADE2/ADE5,7 and the PANTHER family reviews (PTHR10520 TOO_DEEP GAR synthetase node; PTHR11609 WRONG_NODE for GO:0004638 and GO:0006144).
