# KTI11 / DPH3 (YBL071W-A, Q3E840) notes

Module `diphthamide_biosynthesis`, step 1 electron donor; also Elongator partner.

- Electron donor to Dph1-Dph2 [PMID:24422557 "yeast Dph3 (also known as KTI11), a CSL-type zinc finger protein, can bind iron and in the reduced state can serve as an electron donor to reduce the Fe-S cluster in Dph1-Dph2"]; Zn form inactive [PMID:24422557 "the colorless Zn2+-bound Dph3 and found that it cannot serve as the electron donor"].
- Iron donation to rebuild [4Fe-4S] [PMID:34154323 "Dph3 donates one Fe atom to convert the [3Fe-4S] cluster in Dph1-Dph2 to a functional [4Fe-4S] cluster"].
- Reduced by Cbr1/NADH; required for both diphthamide and wobble uridine tRNA modifications [PMID:27694803].
- Rubredoxin-like, Fe and Zn [PMID:18021800 "contained both iron and zinc"].
- Kti11/Kti13 heterodimer required for both modifications [PMID:25543256]; interacts with Elp2/Elp5 and Dph1/Dph2 [PMID:18627462].

Observations: GO:0016730 (oxidoreductase acting on Fe-S proteins as donors) is the wrong concept for an electron carrier -> MODIFY to GO:0009055. GO:0090560 "enables" IDA rows overstate Dph3's role (it is reductant/iron donor) -> MARK_AS_OVER_ANNOTATED. 10 protein-binding rows removed.
