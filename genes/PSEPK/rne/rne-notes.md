# rne curation notes

## 2026-08-31

RNase E is retained as both the defining endoribonuclease and the organizing
scaffold of the RNase E-centered degradosome. The conserved scaffold claim is
supported by full-text work in *E. coli*, where PNPase, RhlB, and enolase bind
the C-terminal scaffold region [PMID:16275923 "the C-terminal \"scaffold\"
region of RNase E to form a complex termed the RNA degradosome."].
Same-genus PMID:40096066 directly maps PNPase and RhlB binding plus membrane
attachment motifs on the P. aeruginosa RNase E scaffold; these findings support
the architecture while leaving KT2440 partner composition to be tested.

That paper does not establish the exact accessory composition in *P. putida*.
The existing KT2440 eno review explicitly says its degradosome role has not
been demonstrated. The species-aware OpenScientist report also identifies
unresolved RhlB-versus-RhlE and PNPase-versus-RNase R partner choices in
KT2440. The revised module therefore treats all three accessory choices as
variant or experimental questions rather than fixed species facts.

OpenScientist also flagged the UniProt family-text conflict: Q88LM4 carries a
large C-terminal scaffold and intact RNase E architecture, while KT2440 encodes
a separate RNase G. The direct KT2440 deletion study analyzed RNase E and RNase
G as distinct endoribonucleases and found species-specific physiological effects
[PMID:33089610 "Each mutant lacked either one exoribonuclease (PNPase, RNase R)
or one endoribonuclease (RNase E, RNase III, RNase G)."].

## 2026-09-01 wave134 annotation-reviewer pass

All 14 seeded GOA rows were rechecked against the local UniProt record and the
cached literature. No action changes were required. Broad parent functions and
locations remain non-core, while RNase E activity, RNA binding, RNA processing,
mRNA catabolism, metal binding, and the cytoplasmic membrane-face localization
remain accepted. The direct KT2440 deletion paper supports biological relevance
but is not used to claim a purified KT2440 degradosome.
