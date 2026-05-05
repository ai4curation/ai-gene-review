# Grpel2 curation notes

Deep research status: `just deep-research-falcon mouse Grpel2 --fallback perplexity-lite --timeout 60` was first run on 2026-05-03. Falcon timed out, and the requested `perplexity-lite` fallback failed with a 401 insufficient-quota error. Per course correction, `just deep-research-falcon mouse Grpel2 --timeout 1800 --fallback perplexity-lite` was then run one gene at a time and succeeded, producing `Grpel2-deep-research-falcon.md`.

Core evidence: Grpel2 is a mitochondrial GrpE-family nucleotide exchange factor for mitochondrial Hsp70/HSPA9 and a component of the PAM import motor. The core molecular function is adenyl-nucleotide exchange factor activity, not direct unfolded-substrate binding.

Falcon synthesis: The Falcon report verifies GRPEL2 as a mitochondrial matrix GrpE-family co-chaperone in the mtHSP70/HSPA9 system. It adds an important paralog-specific nuance: recent biochemical work supports GRPEL1 as the dominant housekeeping NEF for ADP-bound mtHSP70, while GRPEL2 appears weaker and more redox/stress-modulated, with conditional roles in mitochondrial matrix proteostasis and disease/stress models such as diabetic cardiomyopathy [file:mouse/Grpel2/Grpel2-deep-research-falcon.md].

Experimental evidence: Naylor et al. report that the mammalian mitochondrial GrpE-like proteins "specifically interact with and stimulate the ATPase activity of mammalian mitochondrial Hsp70 (mt-Hsp70)" [PMID:9694873]. This supports nucleotide-exchange/co-chaperone activity and Hsp70/chaperone binding.

Localization evidence: UniProt annotates Grpel2 as mitochondrial matrix localized and describes a mitochondrial transit peptide; mitochondrial proteomics annotations are supporting but less specific than the matrix/PAM-complex biology.

Curation rule: GO:0051082 unfolded protein binding should be modified for Grpel2 because GrpE is a nucleotide exchange factor for Hsp70 rather than a direct unfolded substrate-binding chaperone. GO:0044183 protein folding chaperone is a better replacement for the co-chaperone role.
