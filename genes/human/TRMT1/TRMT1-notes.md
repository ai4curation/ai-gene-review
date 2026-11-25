# TRMT1 family review notes

TRMT1 is the G26-specific human member of the PTHR10631 Trm1/TRMT1 tRNA
guanine dimethyltransferase family. The cloned human hTRM1 enzyme was shown to
target G26 of spliced and unspliced tRNA(Tyr) substrates [PMID:10982862, "It
targeted solely position G(26)"], and later human-cell work showed that TRMT1 is
responsible for m2,2G formation on both nuclear-encoded and mitochondrial-encoded
tRNAs [PMID:28784718, "TRMT1 is responsible for catalyzing the
dimethylguanosine (m2,2G) base modification in both nucleus- and
mitochondrion-encoded tRNAs"].

The TRMT1/TRMT1L paralog split is now resolved. Zhang et al. used comprehensive
tRNA sequencing to show that TRMT1 methylates known G26-containing tRNAs,
whereas TRMT1L is the G27 enzyme for tyrosine tRNAs [PMID:39786990, "TRMT1
methylates all known tRNAs containing guanosine at position 26"]. That result
matches the PAINT split: the G26 IBD at `PTN000066880` reaches human TRMT1, and
the TRMT1L branch carries an IRD that prevents the same G26 term from reaching
the G27 paralog.

TRMT1 has mitochondrial and nucleo-cytoplasmic pools. UniProt assigns isoform 1
to mitochondrion and isoform 3 to nucleus/cytoplasm by curator inference from
three localization papers, while direct GFP imaging after SARS-CoV-2 Nsp5
cleavage saw a cytoplasmic signal with nuclear puncta and partial overlap with a
mitochondrial marker [PMID:38814682, "Full-length TRMT1-GFP exhibited
cytoplasmic localization along with a punctate signal in the nucleus"].

Rows removed from the review are limited to bare `GO:0005515` protein-binding
interactions from high-throughput IntAct screens. The screens are not disputed,
but untyped protein binding is not an informative molecular function for this
enzyme.
