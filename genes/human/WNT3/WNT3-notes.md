# WNT3 evidence notes

Deep research note: the `falcon` provider and `perplexity-lite` fallback were
unavailable in this runtime on 2026-11-26; this manual note replaces provider
research for the WNT3 review.

WNT3 is a secreted Wnt-family ligand that binds Frizzled receptors and activates
canonical beta-catenin signaling. The UniProt record describes WNT3 as a
Frizzled-family ligand required for early embryonic patterning, gastrulation and
limb development, while Gazit et al. reported that human WNT3 cooperates with
human FZD1 to induce TCF-dependent transcription and Voloshanenko et al. showed
that WNT3/WNT3A-induced beta-catenin reporter activity depends on FZD receptors
[PMID:10557084; PMID:28733458].

The PTHR12027 PAINT rows that WNT3 inherits at the family root are broad but
largely sound for a secreted Wnt ligand: extracellular region, Frizzled binding,
cell-fate signaling and canonical Wnt signaling. The root `cytokine activity`
row is the wrong molecular-function label for Wnt ligands and should be refined
to a generic receptor-ligand term. The WNT3-specific literature in GOA is
dominated by reporter, Frizzled-binding and developmental cell-culture evidence;
those support the canonical signaling function more directly than they support
every downstream tissue-development row.

Human WNT3 has a well-established disease connection to tetra-amelia, but a
loss-of-function syndrome by itself should not be promoted into a GO process
annotation unless the row names a process in which the WNT3 ligand itself
performs signaling work. Several Reactome component rows place the WNT ligand in
ER, Golgi and endocytic pathway intermediates; these are biogenesis/transit
contexts for a secreted ligand rather than stable WNT3 compartments.
