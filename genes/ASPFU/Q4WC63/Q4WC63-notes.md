# AFUA_8G05580 notes

## 2026-11-17 review

QuickGO returned no rows for Q4WC63/AFUA_8G05580. The UniProt record is named only by accession and ORF, but the EMBL/RefSeq cross-references use the A. fumigatus locus `AFUA_8G05580`, so I used that as `gene_symbol`.

AFUA_8G05580 is in PANTHER `PTHR43609:SF1`, the same single-subfamily Ach1/CoaT family as A. nidulans Q5BD33/CoaT. Fleck and Brock purified the responsible A. nidulans acyl-CoA:carboxylate CoA-transferase and found that it used succinyl-, propionyl- and acetyl-CoA as CoASH donors, while acetyl-CoA hydrolase activity was hardly detectable. That argues for propagating `GO:0008775 acetate CoA-transferase activity` rather than making the old acetyl-CoA hydrolase name the core function.

I searched PubMed/web for `"AFUA_8G05580" ACH1`, `"Aspergillus fumigatus" "AFUA_8G05580"`, and `"Aspergillus nidulans" CoaT AtfA 2025` on 2026-11-17. The newer AtfA ChIP-seq/RNA-seq paper mentions `coaT` as an AtfA-bound target but does not revise the biochemical annotation, so it was not used for a GO proposal.
