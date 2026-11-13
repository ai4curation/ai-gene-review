# purB (Escherichia coli K-12, UniProtKB:P0AB89) notes

## 2026-11-13 review for the de_novo_purine_synthesis module

PurB is the adenylosuccinate lyase of Escherichia coli, a homotetrameric cytosolic enzyme of the fumarase/argininosuccinate lyase superfamily. It catalyses two beta-elimination reactions releasing fumarate: cleavage of SAICAR to AICAR in de novo IMP biosynthesis, and cleavage of adenylosuccinate to AMP in AMP synthesis from IMP. During infection by phages that encode 2-aminoadenine (Z) DNA synthesis, it also cleaves the phage-made dZ precursor.

### Provenance

No provider deep-research report was generated for this gene. These notes were written by the reviewer from: the fetched UniProt record (file:ECOLI/purB/purB-uniprot.txt), the cached primary publications cited below (most abstract-only; full_text_available is recorded in each publications/PMID_*.md file), the PANTHER family reviews under interpro/panther/, and the P. putida, yeast and human orthologue reviews used as precedents.

- During infection by phages that make 2-aminoadenine (Z) DNA, PurB converts the phage-made 2-amino-2'-deoxyadenylosuccinate to dZMP and fumarate (UniProt, citing PMID:33926954). [file:ECOLI/purB/purB-uniprot.txt "deoxyadenylo-succinate to dZMP and fumarate, when the bacterium is"]

### Core function evidence

- (S)-2-(5-amino-1-(5-phospho-D-ribosyl)imidazole-4-carboxamido) succinate lyase (fumarate-forming) activity (GO:0070626):
  [PMID:17531264 "Adenylosuccinate lyase (ADL) catalyzes the breakdown of 5-aminoimidazole- (N-succinylocarboxamide) ribotide (SAICAR) to 5-aminoimidazole-4-carboxamide ribotide (AICAR) and fumarate, and of adenylosuccinate (ADS) to adenosine monophosphate (AMP) and fumarate in the de novo purine biosynthetic pathway."]
- N6-(1,2-dicarboxyethyl)AMP AMP-lyase (fumarate-forming) activity (GO:0004018):
  [PMID:17531264 "Adenylosuccinate lyase (ADL) catalyzes the breakdown of 5-aminoimidazole- (N-succinylocarboxamide) ribotide (SAICAR) to 5-aminoimidazole-4-carboxamide ribotide (AICAR) and fumarate, and of adenylosuccinate (ADS) to adenosine monophosphate (AMP) and fumarate in the de novo purine biosynthetic pathway."]

### Decisions other than ACCEPT

- GO:0003824 catalytic activity (IEA, GO_REF:0000002): MODIFY -> GO:0004018, GO:0070626. Correct but uninformative root activity.
- GO:0005515 protein binding (IPI, PMID:15690043): REMOVE. Bare protein binding from a high-throughput interaction screen.
- GO:0006163 purine nucleotide metabolic process (IBA, GO_REF:0000033): MODIFY -> GO:0006189, GO:0044208. Correct but very general; PurB acts in both de novo IMP and AMP synthesis.
- GO:0006188 IMP biosynthetic process (IEA, GO_REF:0000002): MODIFY -> GO:0006189. Correct but general; the specific de novo term applies.
- GO:0006974 DNA damage response (IEP, PMID:11967071): MARK_AS_OVER_ANNOTATED. Transcriptome-wide expression change after mitomycin C, not a role in the DNA damage response.
- GO:0009152 purine ribonucleotide biosynthetic process (IEA, GO_REF:0000002): MODIFY -> GO:0006189, GO:0044208. Correct but general; PurB acts in both de novo IMP and AMP synthesis.
- GO:0016829 lyase activity (IEA, GO_REF:0000117): MODIFY -> GO:0004018, GO:0070626. Correct but general enzyme class.
- GO:0097216 guanosine tetraphosphate binding (IDA, PMID:30559427): KEEP_AS_NON_CORE. PurB was a ppGpp-capture hit, without binding validation.

Precedents followed: PSEPK pur* reviews, yeast ADE2/ADE5,7 and the PANTHER family reviews (PTHR10520 TOO_DEEP GAR synthetase node; PTHR11609 WRONG_NODE for GO:0004638 and GO:0006144).
