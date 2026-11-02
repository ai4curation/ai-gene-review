# elo1 (SPAC1639.01c, UniProt Q7LKX0) notes

Fetch: `just fetch-gene SCHPO elo1` fetched the correct accession (ELOH2_SCHPO, Q7LKX0, 365 aa).

## Naming trap
- PomBase **elo1** = UniProt "Putative fatty acid elongase 2" (named by similarity to S. cerevisiae ELO2, P25358).
  Conversely PomBase **elo2** (SPAC1B2.03c, Q9UTF7) is labelled "Fatty acid elongase 1" in UniProt (per module representative label).
  The PomBase numbering is NOT the budding-yeast ELO1/ELO2/ELO3 numbering; pombe elo1 is not the orthologue of the C14->C16 S. cerevisiae ELO1.
  The module lists elo1 among ELO-family representatives without claiming a one-to-one ortholog; the closest S. cerevisiae reviews used for
  consistency are ELO2/ELO3.

## Evidence
- [UniProt:Q7LKX0] "May be involved in the synthesis of very long chain fatty acids" (ECO:0000250 from P25358); EC 2.3.1.199; ELO family.
- Location: ER membrane and nucleus membrane (PMID:30975915, EXP per UniProt and GOA). The paper's abstract focuses on Elo2:
  [PMID:30975915 "We found that the very-long-chain fatty acid elongase Elo2 is located in the nuclear membrane"].
- [PMID:30975915 "t20:0/24:0 phytoceramide (a conjugate of C20:0 phytosphingosine and C24:0 fatty acid) is a major ceramide species in S. pombe"].
- ORFeome HDA: nucleus and cytosol (PMID:16823372) - cytosol implausible for a multipass membrane protein.
- No direct elo1 enzymology or chain-length data cached.

## GO-CAM
- gomodel:678073a900002931: elo1 (6792e70800000033) enables GO:0009922 in ER membrane, part_of GO:0042761, parallel to elo2. Agrees.

## Decisions (consistent with genes/yeast/ELO2, ELO3)
- Core MF GO:0009922, BP GO:0042761, ER membrane.
- membrane -> MODIFY ER membrane; MUFA elongation MARK_AS_OVER_ANNOTATED; PUFA elongation REMOVE; sphingolipid biosynthesis KEEP_AS_NON_CORE;
  cytosol HDA MARK_AS_OVER_ANNOTATED; nucleus/nuclear membrane KEEP_AS_NON_CORE.
