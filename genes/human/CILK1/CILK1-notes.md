# CILK1 (ICK) notes

Deep research: not run. In this environment falcon times out after 600 s and perplexity-lite is not
installed. The review uses the cached GOA-cited publications, PMID:24853502 and the UniProt record.
CILK1 is the human ortholog of C. elegans DYF-5 and Chlamydomonas LF4.

## Key points
- Kinase for KIF3A at the ciliary tip. [PMID:24797473 "ICK directly phosphorylated Kif3a, while inhibition of this Kif3a phosphorylation affected ciliary formation"]
- IFT turnaround. [PMID:24797473 "Loss of ICK caused the accumulation of IFT-A, IFT-B, and BBSome components at the ciliary tips."]
- Cilium length control. [PMID:24853502 "down-regulation of Ick or overexpression of kinase-dead or ECO syndrome mutant ICK resulted in an elongation of primary cilia and abnormal Shh signaling"]
- ECO syndrome R272Q. [PMID:19185282 "We also demonstrate that the R272Q mutant fails to localize at the nucleus and has diminished kinase activity."]

## Curation decisions
- Nucleus rows (GFP overexpression) and generic signal transduction rows are kept as non-core.
  HSP90/FKBP5/SMYD2 protein binding rows are removed.
- The IFT process rows were accepted, consistent with the DYF-5 ortholog review. CILK1's role is
  regulatory (it acts on the motor), and whether regulation terms (GO:1905796/GO:1905799) would be
  more accurate is raised as a suggested question. No NEW cilium-length term was added, because
  loss-of-function phenotypes differ by cell type (elongation versus impaired ciliogenesis).
