# MT-ND1 notes

## Literature work

Deep research was not run for this gene; the literature was assembled from the cached
GOA references, the UniProt record and four mammalian Complex I structure papers,
retrieved through the PubMed MCP and cached with `just fetch-pmid`.

## Function

- MT-ND1 encodes a core subunit of Complex I [file:human/MT-ND1/MT-ND1-uniprot.txt "Core subunit of the mitochondrial membrane respiratory chain"].
- ND1 forms part of the ubiquinone channel. The Q10 isoprenoid chain runs "along the NDUFS2-NDUFS7 then ND1-NDUFS7 interfaces to exit from ND1" [PMID:35589726], and ubiquinone "is thought to worm its way up a channel at the hydrophilic/hydrophobic domain interface of the NDUFS2, NDUFS7, ND1 and ND3 subunits" [PMID:32747785].
- ND1 also contributes to the E-channel proton path: ND3, ND6 and ND4L "form, together with part of ND1, the E-channel containing key glutamates" [PMID:36920092].
- Patient cells: "The ND1/3460 mutation exhibits 80% reduction in rotenone-sensitive and ubiquinone-dependent electron transfer activity" [PMID:1959619].
- Assembly: "We conclude that the loss of ND1 stalls complex I assembly during the early stages of its biogenesis" [PMID:26929434].

## Curation decisions

- The core MF is ubiquinone binding (GO:0048039), added as NEW (ISS from mammalian structures), with contributes_to NADH dehydrogenase (ubiquinone) activity (GO:0008137).
- The `enables` GO:0008137 rows are MODIFY: they keep the term but should use contributes_to. The holoenzyme activity needs the peripheral-arm FMN and Fe-S subunits.
- Complex I assembly is kept as non-core. ND1 is a building block that the assembly pathway incorporates, not an assembly factor.
- The three protein binding IPIs (NAMPT, PARK7, MAP1S) are REMOVE as uninformative.

## Disease context

MT-ND1 variants cause LHON (m.3460G>A) and are reported in MELAS (UniProt disease lines).
dismech `MELAS_Syndrome` binds ND1 on the node "Complex I structural subunit defect" with
GO:0008137 DECREASED. That is consistent with the contributes_to core function here.
