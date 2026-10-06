# BRC1 (TCP18, At3g18550, UniProt A1YKT1) curation notes

Folder/symbol uses the standard Arabidopsis name BRC1 (UniProt primary name TCP18); fetched by accession
(`just fetch-gene ARATH A1YKT1 --alias BRC1`). Context: `strigolactone_signaling_shoot_branching`
module. Falcon deep research failed; notes from cached publications.

## Function
- Bud-expressed TCP factor that arrests bud development, downstream of MAX pathway [PMID:17307924 "BRC1 is expressed in developing buds, where it arrests bud development."].
- Nuclear GFP:BRC1 [PMID:17307924 "GFP:BRC1 and GFP:BRC2 were targeted to the nuclei in all tissues analyzed"].
- Required for shade-induced bud suppression [PMID:23524661].
- Binds GGgcCCmc motif, directly activates HB21/HB40/HB53 -> NCED3/ABA in buds [PMID:28028241].
- SL induces BRC1 via SMXL6/7/8 degradation [PMID:26546446 "the BRC1 gene was strongly repressed in max2-1 and max3-9 but was induced in smxl6/7/8"]; [PMID:32528176].
- BRC1 not strictly necessary/sufficient; sets bud activation potential [PMID:28289131 "Buds lacking BRC1 expression can remain inhibited and sensitive to inhibition by strigolactone."].
- brc1brc2 reduced but significant SL response [PMID:30865619].

## Curation decisions
- secondary shoot formation (IMP, shade) -> MODIFY to GO:0097207 bud dormancy process.
- HT Y2H protein binding -> REMOVE; Y1H cis-regulatory binding (PMID:25533953) -> non-core.
- Core: DNA-binding transcription factor activity in nucleus; regulation of secondary shoot
  formation; bud dormancy process; response to strigolactone.
