# al-3 notes

## 2026-11-23 PTHR12001 review

- `al-3` is UniProt `P24322` and a `PTHR12001:SF44` member, matching the PAINT GGPP synthase node `PTN000243244`.
- PubMed searches for `Neurospora al-3`, `albino-3`, `geranylgeranyl`, and `NCU01427` found the original cloning paper PMID:1826006 and the translational-initiation paper PMID:7929398, both of which identify `al-3` as the Neurospora geranylgeranyl-pyrophosphate synthase. No newer direct biochemical recharacterization was found.
- The UniProt record represents AL-3 as a cytosolic GGPP synthase that can start from DMAPP, recording the DMAPP-to-GPP, GPP-to-FPP, and FPP-to-GGPP reactions. The intermediate activities and processes were therefore kept as non-core rather than removed.
- Comparator check for `GO:0016117 carotenoid biosynthetic process`: QuickGO returned many positive fungal annotations to `GO:0016117` on 2026-11-23, but none for the GGPP synthase accessions `P24322` (N. crassa AL-3), `O95749` (human GGPS1), or `Q12051` (S. cerevisiae BTS1), and the local fungal GOA set has no `GO:0016117` row on SF44 GGPP synthases. No `NEW` carotenoid-biosynthetic-process row was proposed because AL-3 supplies the GGPP precursor rather than performing the carotenoid-modifying reactions.
