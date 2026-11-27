# CSF2 evidence and review notes

CSF2 is the only reviewed human member of PTHR10059. The family is a compact
mammalian GM-CSF cytokine family with one PAINT node, PTN000006643, for
`GO:0005576`, `GO:0005125`, and `GO:0030099`; human CSF2 is an IBD seed for all
three rows, and mouse and/or rat Csf2 are the other donors. The three PAINT
assertions were therefore kept as sound.

The molecular core is the secreted GM-CSF ligand binding the CSF2RA/CSF2RB
receptor. The 1985 expression-cloning paper reports conditioned-medium activity
that "stimulates the formation of granulocyte and macrophage colonies", the
2008 structure paper reports the "human GM-CSF/GM-CSF receptor ternary
complex", and the 2016 binary/ternary structures show receptor subunit
recruitment and affinity conversion. The direct core rows keep
`GO:0005129`, `GO:0005125`, `GO:0030526`, `GO:0038157`, `GO:0007259`,
`GO:0030099`, and extracellular region.

The 24 Reactome TAS extracellular rows are deliberately kept as 24
`existing_annotations` entries. They are duplicate at the term level but are
separate GOA rows with different references, so the review preserves the row
multiplicity rather than collapsing them. UniProt's secreted-location statement
is enough for the extracellular-region call, so these rows do not need separate
Reactome event summaries as supporting evidence.

The six IntAct `GO:0005515` rows also stay separate, including the three
`PMID:32814053` rows with A2M, HTT and DNM2-2 as different WITH/FROM partners.
All six are removed under the bare-protein-binding policy: the CSF2RB structural
interaction is better represented by GM-CSF receptor binding and the receptor
complex, while the MEOX2/A2M/HTT/DNM2 large-scale interactions do not define
core GM-CSF biology.

The old cell-culture process rows were bounded to their own cached evidence. The
PF4 paper says PF4 effects were "GM-CSF-independent", so its positive gene
expression and apoptosis rows are left `UNDECIDED`. The podosome and CD4
ligation abstracts likewise do not expose their GM-CSF controls. The foam-cell
paper used GM-CSF only to differentiate primary human macrophages before lipid
loading and IL-1 beta/TNF alpha treatment, so the foam-cell differentiation row
is over-annotated rather than a direct CSF2 effect.
