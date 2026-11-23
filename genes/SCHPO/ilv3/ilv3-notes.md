# ilv3 (SPAC17G8.06c, UniProt Q10318) notes

- Dihydroxy-acid dehydratase (EC 4.2.1.9), ortholog of S. cerevisiae ILV3. UniProt has no gene name (ORF only), so fetched by accession.
- Experimental basis (full text, Ohtsuka et al. 2022, Fig. 2): [PMID:35325114 "The deletion mutant of SPAC17G8.06c can grow in yeast extract complete medium but cannot grow in Edinburgh minimal medium (EMM) with Leu."]; [PMID:35325114 "The defective growth of the ΔSPAC17G8.06c mutant was complemented not only by the expression of S. pombe SPAC17G8.06c itself but also by the S. cerevisiae ILV3."]; [PMID:35325114 "On this basis, we called SPAC17G8.06c ilv3+."]
- Unexplained phenotype: [PMID:35325114 "However, even if Leu, Ile, and Val are added, this mutant cannot grow in EMM, whereas it can surprisingly grow in synthetic dextrose medium with these BCAAs."] -> recorded as a knowledge gap.
- Mitochondrial: [PMID:35325114 "Like ALS and Ilv5, Ilv3 is also localized in the mitochondria"]; UniProt transit peptide 1-18 and [2Fe-2S] cofactor by similarity to P39522.
- IBA donors include PomBase:SPAC17G8.06c itself - expected (own IMP grounding), not circular.
- Decisions: all accepted except root "catalytic activity" -> MODIFY to GO:0004160. Consistent with S. cerevisiae ILV3 review; adds GO:0009098 to core BPs because S. pombe IMP data and GO-CAM (ilv3 causally upstream of leu3) support it.
