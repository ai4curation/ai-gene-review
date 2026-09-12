# RPL36A curation notes

Date: 2026-07-18

## Retrieval record

- Fetched the reviewed UniProt record, all 58 GOA groups, and all eleven cited
  PubMed records.
- Inspected the human 80S/pre-60S structural sources, the mRNA interactome,
  protein-interaction screens, and the full RPL3L muscle paper.
- Falcon failed with HTTP 402; the Perplexity-lite fallback failed with HTTP 401.
  Manual synthesis is in `RPL36A-deep-research-manual.md`.

## Core conclusion

RPL36A encodes eL42, a structural constituent of the human cytosolic 60S
ribosomal subunit that participates in cytoplasmic translation. The reviewed
UniProt record directly states "Component of the large ribosomal subunit" and
human cryo-EM structures include the full 106-residue chain.

## Annotation decisions

- ACCEPT all specific cytoplasmic-translation, structural-constituent,
  cytosolic-large-subunit, cytosolic-ribosome, cytoplasm, and cytosol records.
- MODIFY broad GO:0006412 translation to GO:0002181 cytoplasmic translation.
- MODIFY broad GO:0005840 ribosome to GO:0022625 cytosolic large ribosomal
  subunit.
- KEEP_AS_NON_CORE the HPA endoplasmic-reticulum localization because it can
  reflect rough-ER-bound cytosolic ribosomes.
- MARK_AS_OVER_ANNOTATED both generic protein-binding annotations. The viral
  Npro pulldown recovered many ribosomal proteins and allows indirect complex
  capture [PMID:24965446, "the other proteins are pulled down in the same
  complex"].
- MARK_AS_OVER_ANNOTATED generic RNA binding from the mRNA-bound proteome; the
  experiment does not distinguish direct autonomous binding from recovery of a
  translating ribosome.
- MARK_AS_OVER_ANNOTATED striated muscle contraction and negative regulation of
  myoblast fusion. Their cited sources study RPL3L, not RPL36A
  [PMID:26684695, "RPL3L expression significantly impaired myotube growth"].
- No NEW annotation is needed: the experimental and phylogenetic records already
  capture the core molecular role.

## Experimental priorities

1. Use paralog-specific proteomics to determine the relative incorporation of
   RPL36A and RPL36AL into native human ribosomes across tissues.
2. Test whether the HPA ER signal disappears after polysome runoff or disruption
   of SRP-dependent ER targeting.
3. Map direct eL42 contacts to rRNA and mRNA at nucleotide resolution rather than
   inferring RNA binding from whole-ribosome capture.
