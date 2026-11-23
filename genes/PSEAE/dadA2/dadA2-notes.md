# dadA2 (PA5084, Q9HU99) notes

Second DadA-family D-amino acid dehydrogenase of PAO1 (PE 3, homology only). No deep-research
provider was available. PubMed search ("PA5084 OR dadA2 Pseudomonas aeruginosa D-amino acid
dehydrogenase") returned no hits. Cached PMID:17021207 full text read.

## Literature

- PMID:17021207 (Sonawane et al. 2006, Appl Environ Microbiol), the only paper GOA cites for
  this gene: the AauR-AauS two-component system of Pseudomonas putida KT2440 ["Here, we show
  that the two-component system encoded by PP1067-PP1066 ( aauS-aauR ) is required for efficient
  growth of P. putida KT2440 on acidic amino acids (Glu and Asp) and their amides (Gln and
  Asn)."]. Enzymes assayed: PGA, aspartase, glutamate dehydrogenase, glutamine synthetase,
  GOGAT. DadA, PA5084 and D-amino acid dehydrogenase are not mentioned anywhere in the text.
- PMID:21378189 (paralog DadA1): the dadA1 mutant alone loses D-Ala use, and DadA1 is ["the
  enzyme solely responsible for the proposed D-amino acid dehydrogenase activity"], so DadA2
  does not substitute under those conditions.
- UniProt Q9HU99: HAMAP MF_01202 DadA, FAD cofactor by similarity; function by similarity only.

## Review decisions

- GO:0008718 IBA and IEA: ACCEPT (DadA family homology; node stands on other seeds).
- GO:0008718 IDA (PseudoCAP, PMID:17021207): ACCEPT the term on homology, but the citation is
  wrong; PSEUDOCAP WRONG_REFERENCE defect, DELETE_ROW, CONFIRMED (full text read, title names
  P. putida).
- GO:0019478 IEA: ACCEPT. GO:0055130 D-alanine catabolic IBA: MARK_AS_OVER_ANNOTATED (the
  D-alanine role belongs to DadA1), with propagation_review.
- Cytoplasm, plasma membrane IBA: KEEP_AS_NON_CORE.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN008552203 | GO:0008718 D-amino-acid dehydrogenase activity | 3 | 10 (8 taxa) | GO:0008718, IDA, PMID:17021207 (PseudoCAP) | WRONG | Full text read: the paper is about the P. putida KT2440 AauR-AauS system and never mentions DadA or PA5084; no D-amino acid dehydrogenase assay. The term itself is plausible by homology. | E. coli DadA P0A6J5 (IDA); DadA1 Q9HTQ0 (PseudoCAP IDA PMID:21378189, SOUND) | Yes, on E. coli DadA and DadA1 |

Defects: 1 PSEUDOCAP (WRONG_REFERENCE, CONFIRMED), recorded here once for the shared node;
dadA1 notes cross-reference it. No GO_CENTRAL defect (IBD sound without this seed; node term
fits the clade).
