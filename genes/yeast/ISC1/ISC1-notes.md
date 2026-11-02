# ISC1 (YER019W) notes

UniProt P40015, inositol phosphosphingolipid phospholipase C (IPS-PLC), neutral sphingomyelinase family; Mg2+-dependent [UniProt:P40015].

- Identified as IPS-PLC: [PMID:11006294 "Here we show that ISC1 (YER019w), which has homology to bacterial neutral sphingomyelinase (SMase), encodes IPS phospholipase C (IPS-PLC)."]; deletion abolishes activity [PMID:11006294 "Deletion of ISC1 eliminated endogenous IPS-PLC activities."]. Hydrolyses IPC, MIPC and M(IP)2C to ceramide; also SM in vitro (not physiological in yeast, which lacks SM) [UniProt:P40015].
- Localization: ER early in growth, mitochondria (outer membrane) in late log/post-diauxic phase [PMID:14699160 "Confocal microscopy revealed that the enzyme was predominantly in the ER during early growth but became associated with mitochondria in late logarithmic growth."]; integral OMM protein [PMID:17880915 "epitope-tagged Isc1p localized to the outer mitochondrial membrane as an integral membrane protein"].
- Generates mitochondrial alpha-hydroxylated phytoceramides [PMID:17880915 "These results suggest that Isc1p generates ceramide in mitochondria"].
- HU resistance via C18:1-phytoceramide / Cdc55-PP2A [PMID:23620586 "a specific sphingolipid, C18:1-phytoceramide, produced by Isc1"]; spindle checkpoint role [PMID:32205408 "We herein provide biochemical and biological evidence that ISC1 functions in the spindle assembly checkpoint."]. These are downstream signalling roles of its ceramide product.

## Pathway context
- YeastPathways places Isc1 on "phosphatidylcholine + H2O -> DAG + phosphocholine" (EC 3.1.4.3, PC-PLC) in phospholipid degradation (LIPASYN-PWY-1). No evidence Isc1 hydrolyses PC; its substrates are inositol phosphosphingolipids (and SM in vitro). The PC-PLC assignment is a YeastCyc error; RCA rows derived from it (PC-PLC activity, cytosol) are rejected.
