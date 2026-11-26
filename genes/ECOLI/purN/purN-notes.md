# purN (Escherichia coli K-12, UniProtKB:P08179) notes

## 2026-11-13 review for the de_novo_purine_synthesis module

PurN is the folate-dependent glycinamide ribonucleotide (GAR) transformylase of Escherichia coli, a soluble cytosolic monomer that transfers the formyl group of 10-formyltetrahydrofolate to GAR to give N-formylglycinamide ribonucleotide (FGAR), the third step of de novo IMP biosynthesis. E. coli has a second, ATP- and formate-dependent GAR transformylase (PurT); only purN purT double mutants require purines.

### Provenance

No provider deep-research report was generated for this gene. These notes were written by the reviewer from: the fetched UniProt record (file:ECOLI/purN/purN-uniprot.txt), the cached primary publications cited below (most abstract-only; full_text_available is recorded in each publications/PMID_*.md file), the PANTHER family reviews under interpro/panther/, and the P. putida, yeast and human orthologue reviews used as precedents.


### Core function evidence

- phosphoribosylglycinamide formyltransferase activity (GO:0004644):
  [PMID:350869 "Upon addition of glycinamide ribotide, N-formylglycinamide ribotide was formed when N10-formyltetrahydrofolate was present"]
  [PMID:2185839 "The protein is a monomer of Mr 23,241 and catalyzes a single reaction."]

### Decisions other than ACCEPT

- GO:0003824 catalytic activity (IEA, GO_REF:0000117): MODIFY -> GO:0004644. Correct but uninformative root activity.
- GO:0005737 cytoplasm (IBA, GO_REF:0000033): MODIFY -> GO:0005829. Correct but general location; the gene also carries the more specific cytosol term.
- GO:0006974 DNA damage response (IEP, PMID:11967071): MARK_AS_OVER_ANNOTATED. Transcriptome-wide expression change after mitomycin C, not a role in the DNA damage response.

Precedents followed: PSEPK pur* reviews, yeast ADE2/ADE5,7 and the PANTHER family reviews (PTHR10520 TOO_DEEP GAR synthetase node; PTHR11609 WRONG_NODE for GO:0004638 and GO:0006144).
