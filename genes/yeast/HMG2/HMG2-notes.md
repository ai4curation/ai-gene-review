# HMG2 (YLR450W) notes

UniProt P12684; HMG-CoA reductase 2, EC 1.1.1.34; ER/nuclear envelope; regulated ERAD substrate [UniProt:P12684].

## Evidence journal
- Functional isozyme [PMID:2828155 "The two yeast genes for 3-hydroxy-3-methylglutaryl-coenzyme A (HMG-CoA) reductase, HMG1 and HMG2, each encode a functional isozyme."]; Hmg1 gives >=83% of activity [PMID:3526336].
- Localisation: NE at native levels, peripheral ER when overexpressed [PMID:8744950 "increased levels of Hmg1p were concentrated in the nuclear envelope, whereas increased levels of Hmg2p were concentrated in the peripheral ER."]
- ERAD substrate [PMID:27226596 "Two other polytopic membrane proteins undergoing ERAD, Ste6*p and Hmg2p, also displayed the same outcomes observed for Pca1p."]
- Nsg1 [PMID:16270032 "Yeast Nsgs inhibit degradation of Hmg2p in a highly specific manner, by directly interacting with the sterol-sensing domain (SSD)-containing transmembrane region."]

## Decisions
- Proteasome complex IPI (PMID:27226596) REMOVE: Hmg2 is the ERAD substrate captured with the proteasome, not a subunit.
- protein binding IPI x6 (Hmg1, Nsg1) REMOVE (uninformative; interactions not disputed).
- Peroxisomal membrane IBA REMOVE; cytosol RCA MODIFY -> ER membrane; CoA metabolic process MARK_AS_OVER_ANNOTATED; oxidoreductase MODIFY -> GO:0004420. Rest ACCEPT.
