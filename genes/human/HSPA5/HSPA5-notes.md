# HSPA5 (BiP/GRP78, human, P11021) review notes

Deep research: not run (falcon times out in this environment; perplexity-lite unavailable).
Review based on cached GOA-cited publications, the UniProt entry, the rat Hspa5 review
(genes/rat/Hspa5) and the PTHR19375 family review, for consistency.

## Key findings
- ATP-dependent Hsp70 cycle structurally characterized for human BiP
  [PMID:26655470 "ATP binding allosterically accelerates polypeptide binding and release."]
- Represses PERK [PMID:11907036 "this ER chaperone serves as a repressor of PEK activity"] and IRE1alpha
  [PMID:19538957 "the regulation of mammalian IRE1alpha strongly depends on the dissociation of BiP."]
- Auxiliary translocation component with Sec62/Sec63 [PMID:29719251].
- ERdj4/ERdj5 stimulate BiP ATPase for ERAD of misfolded SP-C [PMID:18400946].

## Curation decisions
- 107 protein binding rows: co-chaperone/chaperone partners (DNAJB11, DNAJB9, DNAJC10, Dnajc3, SIL1, HYOU1, HSP90B1) MODIFY to GO:0051087 protein-folding chaperone binding; all others REMOVE (UPR sensor interactions are captured by sequestering/kinase inhibitor/regulation terms).
- Proteomics-only locations (focal adhesion, COP9 signalosome, midbody, cadherin binding, bare membrane) marked over-annotated; nucleus/cytoplasm/cell surface kept non-core (consistent with rat Hspa5).
- `positive regulation of transcription by RNA polymerase II` (TAS) REMOVE.
- `ubiquitin protein ligase binding` (PMID:8666824, calreticulin paper, abstract only) UNDECIDED.
- NEW: GO:0140662 ATP-dependent protein folding chaperone (MF refinement, as for yeast KAR2).
