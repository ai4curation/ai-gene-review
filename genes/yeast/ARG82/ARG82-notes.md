# ARG82 (YDR173C, P07250) notes

- Inositol polyphosphate multikinase (IPMK; ArgRIII/Ipk2/Gsl3). Predominant in vivo route Ins(1,4,5)P3 -> Ins(1,4,5,6)P4 -> Ins(1,3,4,5,6)P5 [UniProt:P07250 "Its predominant in vivo catalytic function is to convert Ins(1,4,5)P3 to Ins(1,4,5,6)P4 to Ins(1,3,4,5,6)P5 via 6- and 3-kinase activities"].
- Purified yeast IP3 kinase is a 6-kinase [PMID:7945194 "The yeast enzyme is thus an Ins(1,4,5)P3 6-kinase."]; identified as Arg82 [PMID:10720331 "designated Ipk2, was found to be identical to Arg82"].
- Converts IP3 to higher IPs [PMID:10574768 "the yeast protein, ArgRIII, is an inositol-polyphosphate kinase that can convert InsP(3) to InsP(4), InsP(5) and InsP(6)"]; IP6 step is actually Ipk1.
- Also IP4(1,3,4,5) 6-kinase and IP5 pyrophosphorylation to PP-IP4 [PMID:11311242 "Arg82 phosphorylates inositol 1,3,4,5-tetrakisphosphate to inositol pentakisphosphate, which is itself converted to two isomers of diphosphoinositol tetrakisphosphate"].
- arg82 null: IP3 up 170-fold, IP6 down 100-fold, mRNA export defect [PMID:10683435 "increased cellular [InsP(3)] 170-fold and decreased [InsP(6)] 100-fold"]; sole IP3 kinase [PMID:22992733 "Arg82, is the sole inositol-trisphosphate kinase"].
- Nuclear [PMID:3311884 "the three ARGR proteins are localized in the nucleus"]; nuclear PI3K activity reported [PMID:16123124 "phosphoinositide 3-kinase activity of inositol polyphosphate multikinase, which is localized to nuclei and unaffected by wortmannin"] - kept non-core.
- Kinase-independent role: stabilizes Mcm1/Arg80 via polyaspartate domain [PMID:10632874 "the impairment of arginine regulation in an argRIII deletant strain is a result of a lack of stability of ArgRI and Mcm1"]; [PMID:12828642 "Mcm1p and Arg80p chaperoning by Arg82p does not involve the inositol polyphosphate kinase activity of Arg82p, but requires its polyaspartate domain"]; [PMID:22992733 "catalytically inactive Arg82 fully restored the arginine-dependent transcriptional response"].
- Not a stable component of the DNA-bound complex [PMID:10632874 "ArgRIII is not present in the protein complex formed with the 'arginine boxes'"] -> RNAPII TF complex NAS marked over-annotated.
- PHO/NCR effects need kinase activity (indirect via PP-InsPs) [PMID:12828642 "Only the catalytic activity of both kinases was required for PHO gene repression by phosphate and for NCR gene activation"].

## Curation decisions
- GO:0120517 (IP5 -> IP6) from YeastPathways RCA is a mis-mapping of the IP5 -> PP-IP4 reaction: MODIFY to GO:0000827. The same mis-mapping affects KCS1.
- Cytoplasm IBA (IP6K/ITPK donors) and cytosol RCA (pathway default) marked over-annotated; all yeast data say nuclear.
- Macroautophagy IMP from a genome-wide mitophagy screen (PMID:19793921) marked over-annotated (pleiotropic deletion).
