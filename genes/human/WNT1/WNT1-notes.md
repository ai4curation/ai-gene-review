# WNT1 evidence notes

Deep research note: `just deep-research-falcon human WNT1 --fallback perplexity-lite`
failed on 2026-11-26 because the local deep-research-client environment exposed
only the `claude_code` provider. This manual note records the literature and
database synthesis used instead.

WNT1 is a secreted, lipid-modified Wnt ligand that binds Frizzled receptors and
primarily activates the canonical beta-catenin/TCF Wnt pathway. UniProt
summarizes it as a Frizzled-family ligand that promotes
beta-catenin-dependent transcription and is secreted to the extracellular
matrix; Voloshanenko et al. grouped human WNT1 with WNT3/WNT3A canonical Wnts
and showed WNT1-dependent reporter activation could be restored by FZD2 or FZD7
in FZD1/2/7-deficient HEK293T cells [PMID:28733458].

WNT1's direct and inherited Wnt-family rows for extracellular region, Frizzled
binding/receptor ligand activity, and canonical Wnt signaling are therefore
core. Human WNT1 evidence also supports roles in bone homeostasis and in tumor
or neuroblastoma cell proliferation, but most CNS patterning and dopaminergic
neuron terms in GOA are transferred from mouse or are pathway-review summaries;
these should be kept as conserved, non-core developmental context or left
undecided where the exact original evidence is not accessible.

Reactome captures Wnt biogenesis and trafficking through ER, Golgi, WLS and
exosomal/plasma-membrane intermediates. Those are pathway locations visited by
the nascent ligand, not resident compartments of the mature secreted WNT1
protein, so ER/Golgi/endocytic-vesicle component rows from Reactome should be
treated as over-annotated transit locations rather than core WNT1 sites.
