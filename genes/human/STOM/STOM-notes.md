# STOM notes

## 2026-10-20 ORGANELLES batch 1 (mitochondrion rows)

- GO:0005739 rows: IDA (AgBase, PMID:25262680) and IEA (GO_REF:0000107 Ensembl projection from mouse Stom P54116).
- QuickGO shows mouse P54116's mitochondrion annotations are an AgBase IDA to the same PMID:25262680 plus ISO/IEA projected back from human P27105, so the human IEA row is circular and adds nothing independent.
- The cached abstract of PMID:25262680 is about HCV replicase on raft-like membranes and does not mention mitochondria [PMID:25262680 "the HCV RdRp and stomatin are associated with the lipid raft-like domain of membranous structures"]; full text not available to us, so the IDA is not second-guessed.
- The other line is STOM peptides in a large-scale N-terminome of human mitochondrial preparations (UniProt RP "IDENTIFICATION BY MASS SPECTROMETRY [LARGE SCALE ANALYSIS]", PMID:25944712); the earlier review overstated this as "experimental support". Raft/plasma-membrane contamination of crude mitochondrial fractions is plausible.
- STOM has no transit peptide; one N-terminal intramembrane hairpin (UniProt INTRAMEM 26-54). The mitochondrial stomatin-family member is STOML2.
- Outcome: both rows stay KEEP_AS_NON_CORE (IEA reason rewritten to record the check); no sub-compartment. Candidate for a later re-check if full text of PMID:25262680 becomes available; if it shows no mitochondrial data, the IEA row would become MARK_AS_OVER_ANNOTATED.
