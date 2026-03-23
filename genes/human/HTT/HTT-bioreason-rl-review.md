# BioReason-Pro RL Review: HTT (human)

Source: HTT-deep-research-bioreason-rl.md

- **Correctness**: 3/5
- **Completeness**: 2/5

The BioReason-Pro RL analysis correctly identifies HTT as a large HEAT/armadillo repeat scaffold protein involved in intracellular transport, and accurately notes the absence of enzymatic activity. The domain architecture analysis is sound: N-terminal HEAT repeats, central armadillo superhelical core, and C-terminal bridge region are all correctly characterized. The prediction that HTT functions as a cytoplasmic scaffold for vesicle transport and cytoskeletal organization is broadly correct.

However, the analysis has significant gaps and some errors of emphasis:

**What it got right:**
- HEAT/armadillo repeat scaffold architecture
- Protein binding as a core molecular function
- Cytoplasmic localization
- Role in intracellular vesicle transport and cytoskeletal dynamics
- Interaction with dynein/dynactin for vesicle trafficking

**What it missed or got wrong:**
- No mention of the polyglutamine (polyQ) tract, which is the defining feature of HTT and central to Huntington's disease pathology. This is a major omission for any HTT analysis.
- No mention of HTT's role in selective macroautophagy (PMID:25686248, PMID:28445460), which is a well-documented function
- No mention of transcriptional regulation, despite multiple IPI annotations showing HTT interacts with p53, CBP, Sp1, and TAFII130 (PMID:10823891, PMID:11988536)
- No mention of neuronal biology: synaptic vesicle transport, neurogenesis, CNS development, learning and memory
- No mention of anti-apoptotic functions (regulation of Pak2 cleavage, caspase regulation)
- No mention of calcium signaling regulation (IP3R interaction via HAP1)
- The analysis assigns only three GO terms (protein binding, intracellular protein transport, cytoplasm), which is extremely reductive for a protein with over 100 annotated GO terms

**Failure modes observed:**
- Fold-bias: The analysis reasons entirely from domain architecture (HEAT/armadillo repeats) and extrapolates generic scaffold functions. While not wrong, this approach misses the highly specific and well-characterized biology of HTT.
- The functional summary reads like a generic description of any HEAT-repeat protein rather than HTT specifically
- The BioReason system appears to lack access to literature, relying solely on InterPro domain signatures. This is particularly limiting for a protein like HTT where the biology goes far beyond what domain architecture alone can predict.

Note: The curated AI review is itself mostly a stub (all annotations PENDING), so direct comparison of annotation decisions is not possible. However, the curated review at least captures the breadth of HTT biology through its GOA annotation entries.
