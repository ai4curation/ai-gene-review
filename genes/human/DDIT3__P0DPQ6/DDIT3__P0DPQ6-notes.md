# DDIT3__P0DPQ6 notes (AltDDIT3, DDIT3/CHOP uORF peptide)

## Identity
- UniProt P0DPQ6 (DT3UO_HUMAN), 34 aa, "DDIT3 upstream open reading frame protein", alt name AltDDIT3.
  Sequence MLKMSGWQRQSQNQSWNLRRECSRRKCIFIHHHT. Filed under host gene symbol DDIT3 (HGNC:2726);
  canonical CHOP is P35638 (separate entry, not reviewed here).
- Encoded by the conserved uORF in the 5' leader of DDIT3/CHOP mRNA, spanning the exon 1/exon 2
  junction [PMID:29083303 "Its coding sequence overlaps the end of exon 1 and the beginning of exon 2 of the DDIT3/CHOP/GADD153 gene"].
- Literature describes it as 31 aa (rodent/earlier annotation); UniProt human entry is 34 aa
  [PMID:29083303 "AltDDIT3 is a 31 amino acid alternative protein conserved in vertebrates"].
- UniProt FUNCTION comment is ECO:0000250 by similarity to A0A2R8VHR8 and describes the cis
  role (uORF translation prevents CHOP translation in absence of stress).

## Two separable roles

### 1. Cis-regulatory role of the uORF (property of the mRNA / act of translating it)
- Jousse 2001: conserved uORF encodes a peptide that inhibits downstream ORF expression;
  mutational analysis suggested peptide sequence matters
  [PMID:11691921 "encodes a 31 amino acid peptide that inhibits the expression of the downstream ORF"],
  [PMID:11691921 "the peptide itself inhibits expression of the downstream ORF"].
- Palam 2011: uORF acts as barrier in basal conditions, bypassed upon eIF2 phosphorylation
  [PMID:21285359 "In the absence of stress and low eIF2 phosphorylation, translation of the uORF serves as a barrier that prevents translation of the downstream CHOP coding region"].
- Young 2016: an Ile-Phe-Ile sequence in the uORF-encoded nascent chain stalls elongating
  ribosomes and limits reinitiation at the CHOP CDS (the human peptide ends ...CIFIHHHT)
  [PMID:26817837 "specific sequences within the CHOP uORF serve to stall elongating ribosomes and prevent ribosome reinitiation at the downstream CHOP coding sequence"].
- ENDOU (PMID:33511665) and KEPI (PMID:35031423) modulate uORF-mediated inhibition in trans.
- Interpretation: the repression is executed by the ribosome translating the uORF, with the
  nascent chain acting while still in the ribosome exit tunnel. The released 34-aa product is
  not the agent. A GO process annotation (e.g. negative regulation of translation, GO:0017148)
  to the mature peptide entry would conflate the cis-acting mRNA element/nascent chain with
  the released gene product. Not proposed as NEW; raised as a question.

### 2. Possible trans functions of the released peptide
- Samandi 2017 (eLife): AltDDIT3-GFP (overexpressed, HeLa) is mainly nuclear and partly
  cytoplasmic, co-localizes with DDIT3-mCherry and co-IPs with it
  [PMID:29083303 "Both proteins were mainly localized in the nucleus and partially localized in the cytoplasm"],
  [PMID:29083303 "confirming an interaction between the small altDDTI3 and the large DDIT3 proteins encoded in the same gene"].
  Endogenous expression evidence was from TIS ribosome profiling, not antibody detection; authors
  note earlier uORF work did not seek the protein
  [PMID:29083303 "but evidence of endogenous expression of the corresponding small protein was not sought"].
- Chen 2020 (Science, CRISPR/tagging study of noncanonical ORFs): DDIT3 uORF peptide is one of
  five uORF peptides that form a stable complex with the downstream canonical protein
  [PMID:32139545 "formed a stable physical complex with the downstream-encoded, canonical protein on"].
  Independent confirmation of the CHOP interaction.
- PIPPI paper (Nucleic Acids Res 2025) (pooled overexpression screen): altDDIT3 overexpression was the top hit
  for survival under 6-thioguanine; GFP tag abolished the protective effect
  [PMID:41206043 "cells expressing altDDIT3 proliferated better than parental cells after a 6-TG treatment but not in untreated conditions"],
  [PMID:41206043 "including the GFP tag inhibited the protective activity of altDDIT3"].
  Overexpression phenotype only; mechanism unknown. Not enough for a BP annotation.
  Note the tag caveat also applies to the GFP-based localization data.

## GOA review decisions
- protein binding IPI (with P35638): interaction with CHOP, a DNA-binding TF, shown by two
  independent groups -> MODIFY to GO:0140297 DNA-binding transcription factor binding.
  Functional consequence of binding is unknown.
- nucleus IDA / IEA, cytoplasm IDA / IEA: GFP-tagged overexpression in HeLa; a ~32 kDa GFP
  fusion of a 4 kDa peptide can distribute passively, but co-localization with DDIT3 is consistent.
  ACCEPT nucleus; cytoplasm ACCEPT (partial pool, site of synthesis).

## Literature gaps
- No endogenous antibody detection or knockout specific to the peptide (with uORF translation preserved).
- No PubMed hits beyond those above for a trans function.
