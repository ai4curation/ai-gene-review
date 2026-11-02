# Ing5 (Q9VJY8) review notes

- ING family; subunit of Enok complex. [PMID:27198229 "MudPIT analysis of Flag affinity purifications of Flag-HA-tagged Enok, Br140, Eaf6, and Ing5 showed copurification of these four components."]
- Required for H3K23ac. [PMID:27198229 "Depletion of any of the four subunits led to reductions in the H3K23ac levels without affecting the H3K14ac levels"]
- Decisions: shared Enok complex conventions (see enok-notes.md); H3K4me3 reader IBA accepted (conserved ING PHD); protein-containing complex IEA MODIFY -> MOZ/MORF complex.

## Deep research (falcon, added after initial review)
- `Ing5-deep-research-falcon.md` agrees that Ing5 is a non-enzymatic Enok complex subunit that promotes Enok chromatin association and H3K23ac ["Its experimentally demonstrated contribution is to promote Enok association with nuclear chromatin and appropriate histone H3 lysine-23 acetylation"]. It reports a regulated cytosolic pool (Tctp binds the PHD region and retains Ing5) and developmental roles (EGFR, Hippo/Yki) from a 2023 study not in GOA. It cautions that H3K4me3 reading is inferred from the ING family, not measured in fly; the IBA is kept as a phylogenetic inference. No annotation decisions changed.

## PR 4481 review fixes
- Core molecular function changed from GO:0140002 H3K4me3 reader (IBA only, no fly measurement) to GO:0010698 acetyltransferase activator activity plus contributes_to GO:0043994; H3K4me3 recognition is now described in prose as a family inference. The IBA row stays ACCEPT as a phylogenetic inference.
