# Results: DSM2067 HBE construct mapping

## Checklist
- [x] Comparison script has no hardcoded inputs, outputs, accession expectations or biological conclusions.
- [x] Tested on four different proteins: the kinase positive match and three other pathway proteins.
- [x] Analysis completed normally with all four records parsed.
- [x] Raw input and exact_matches.tsv are retained here.
- [x] Source provenance and the limits of the inference are stated below.

## Direct sequence result
A0A2L1CCT7 is identical across all 306 amino acids to the CDS translation of GenBank PP708527.1 (protein WZW45421.1). The deposited construct identifies HldAMM, derives from Methanococcus maripaludis DSM 2067, and cites WP_104838492 as its source protein. Its reference title is The beta-D-manno-heptoses are immune agonists across kingdoms. Thus the archived hldE_2 record maps exactly to the published HldA_MM kinase construct. Codon optimization did not change the encoded protein sequence.

No exact translated match to A0A2L1CCQ9, A0A2L1CD41 or A0A2L1CCN4 occurs among these 27 deposited constructs. This is not evidence of inactivity or exclusion from the experiment; the deposited subset contains synthetic constructs and need not contain every genome-amplified gene. The exact assayed construct mapping for these three remains unverified because supplementary tables were inaccessible.

## Genomic context and interpretation
The public original genome CP026606 (ENA EMBL record inspected 2026-10-25) places gmhB MMJJ_17670/AVB77138.1, hldE_2 MMJJ_17680/AVB77139.1, hldE_3 MMJJ_17690/AVB77140.1 and gmhA1 MMJJ_17700/AVB77141.1 consecutively. Archived UniProt records independently carry these EMBL cross-references. Their GmhB, RfaE domain I, RfaE domain II and GmhA classifications identify a complete four-step ensemble. This context supports assignments of the three unlinked proteins but is distinct from an exact experimental-construct identity. Another annotated hldE_1 occurs at MMJJ_00480, so neither gene-name similarity nor the presence of a pathway is sufficient to claim every hldE-like protein was assayed.

The main article was read from the author-uploaded full text at https://www.researchgate.net/publication/382971859_The_b-_d_-_manno_-heptoses_are_immune_agonists_across_kingdoms . It reports production of ADP-heptose after four DSM2067 HBE genes were expressed in the HBE-negative S2 recipient. This is an engineered archaeal system, not endogenous S2 production. Supplementary figure S11 and tables S1–S9 were not accessible through the publisher (HTTP403); the publication cache remains abstract-only. No publisher supplement content is represented as inspected here.

## Source integrity
GenBank input SHA256: 1219849c53cc29e29529896c2a4ad7c57a78b6e43bb235fc87aa9250277b3769
Download URL and rerun command are in justfile. Archived UniProt versions: A0A2L1CCT7 v22, A0A2L1CCQ9 v23, A0A2L1CD41 v23, A0A2L1CCN4 v24; all last present in UniProt release 2026_01 and sequence version 1. Their deletion was non-reference-proteome retirement, not evidence of invalid protein sequences.
