# YAH1 (YPL252C, UniProt Q12184) – review notes

- Adrenodoxin-type [2Fe-2S] ferredoxin of the mitochondrial matrix; essential [PMID:10375636 "We show that the protein is targeted to the mitochondrial matrix"]. Reduced by ARH1 (NADPH) and donates electrons to several acceptors [UniProt:Q12184 "Transfers electrons from adrenodoxin reductase ARH1 to heme A synthase COX15"].
- Fe-S cluster biogenesis: [PMID:10655482 "we identify the essential ferredoxin Yah1p of Saccharomyces cerevisiae mitochondria as a central component of the Fe/S protein biosynthesis machinery"]; [PMID:12970193 "Depletion of the cysteine desulfurase Nfs1p, the ferredoxin Yah1p or the yeast frataxin homologue Yfh1p by regulated gene expression causes a strong decrease in the de novo synthesis of Fe/S clusters on Isu1p"].
- Heme A synthesis (electron donor to Cox15): [PMID:11788607 "three lines of evidence confirm a requirement of ferredoxin in heme A synthesis"].
- CoQ biosynthesis: [PMID:20534343 "the mitochondrial ferredoxin Yah1p and the ferredoxin reductase Arh1p are required for Q(6) biosynthesis, probably for the first hydroxylation of the pathway"]; [PMID:21944752 "the ferredoxin Yah1 and the ferredoxin reductase Arh1 may be the in vivo source of electrons for Coq6"]. Note GO:0120538 (C1 hydroxylase) and the Coq6 C5 hydroxylation use reduced ferredoxin as donor; Yah1 would feed Coq6 and possibly Coq4/C1 chemistry.
- GO issues:
  - GO:0016653 (NAD(P)H oxidoreductase, heme protein as acceptor; IMP/IGI PMID:11788607) describes the whole Arh1-Yah1-Cox15 chain; Yah1 itself does not oxidize NAD(P)H -> MODIFY to electron transfer activity.
  - GO:0140647 P450-containing electron transport chain (InterPro2GO) – S. cerevisiae has no mitochondrial P450 [PMID:9727014 "to date, no mitochondrial cytochrome P450 has been identified"] -> REMOVE.
- Not in YeastCyc CoQ pathways. Module uses YAH1 as representative of the mitochondrial ferredoxin electron supply (GO:0009055) – consistent.
