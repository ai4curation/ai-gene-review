# STOM notes

## 2026-10-20 ORGANELLES batch 1 (mitochondrion rows)

- GO:0005739 rows: IDA (AgBase, PMID:25262680) and IEA (GO_REF:0000107 Ensembl projection from mouse Stom P54116).
- QuickGO shows mouse P54116's mitochondrion annotations are an AgBase IDA to the same PMID:25262680 plus ISO/IEA projected back from human P27105, so the human IEA row is circular and adds nothing independent.
- The cached abstract of PMID:25262680 is about HCV replicase on raft-like membranes and does not mention mitochondria [PMID:25262680 "the HCV RdRp and stomatin are associated with the lipid raft-like domain of membranous structures"]; full text not available to us, so the IDA is not second-guessed.
- The other line is STOM peptides in a large-scale N-terminome of human mitochondrial preparations (UniProt RP "IDENTIFICATION BY MASS SPECTROMETRY [LARGE SCALE ANALYSIS]", PMID:25944712); the earlier review overstated this as "experimental support". Raft/plasma-membrane contamination of crude mitochondrial fractions is plausible.
- STOM has no transit peptide; one N-terminal intramembrane hairpin (UniProt INTRAMEM 26-54). The mitochondrial stomatin-family member is STOML2.
- Outcome: both rows stay KEEP_AS_NON_CORE (IEA reason rewritten to record the check); no sub-compartment. Candidate for a later re-check if full text of PMID:25262680 becomes available; if it shows no mitochondrial data, the IEA row would become MARK_AS_OVER_ANNOTATED.

## 2026-10-24 full text of PMID:25262680 (ORGANELLES)

- Full text read from a copy supplied by the user (Kim et al. 2014, J Microbiol Biotechnol 24(12):1744-1754, doi:10.4014/jmb.1409.09063). The cached publication is abstract-only, so these quotes cannot go into `supported_by`; they are recorded here and in projects/ORGANELLES.md.
- The fraction behind the IDA is a crude heavy-membrane (P15) fraction that also carries ER markers: "This fraction was enriched with mitochondria, as evidenced by the presence of Hsp60, a mitochondrial matrix protein [28]. In this fraction, we also detected the ER marker Grp78, probably because of the physical linkages between some fractions of the ER and mitochondria."
- On Percoll sub-fractionation "HCV NS proteins had co-fractionated with stomatin, Hsp60, and calreticulin, an ER lumen marker".
- Detergent separates the two: "When the P15 fraction was treated with 1% NP40, NS5B and stomatin remained in the same fraction, while Hsp60, which was released from mitochondria-derived compartments, was detected in the bottom fractions".
- The authors read the stomatin compartment as MAM, not mitochondria: "our results suggest that the DRM in the P15 fraction might represent the mitochondria-associated membranes, which are known to be reversibly tethered to mitochondria and consist of a region of ER [44]."
- Immunofluorescence: "Stomatin exhibited a distinct cytoplasmic and perinuclear localization (Fig. 2C)." No mitochondrial co-stain.
- Outcome: both GO:0005739 rows (IDA, and the circular IEA Ensembl projection) changed KEEP_AS_NON_CORE -> MARK_AS_OVER_ANNOTATED. Not REMOVE: the co-fractionation is real and the paper is the curator's source. GO:0044233 (mitochondria-associated ER membrane contact site) matches the authors' reading, but one detergent-resistance experiment with no MAM marker is not enough for a NEW row.
- PMID:25262680 reference gained a reference_review (relevance HIGH, correctness VERIFIED, notes that it does not support mitochondrion).
- GO:0005783 endoplasmic reticulum IDA (same paper): reason refreshed from the full text after review of PR #5469. In uninfected Huh7 cells "stomatin was detected in both the P15 and the P100 fractions in the Huh7 cells", and the P100 fraction "is known to be enriched with microsomes [28]", carrying Grp78 without Hsp60. Action stays KEEP_AS_NON_CORE.
