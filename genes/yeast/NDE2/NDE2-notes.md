# NDE2 (YDL085W, UniProt Q07500) notes

Module: `oxphos` (external NDH-2, minor paralog). Absent from YeastCyc PWY3O-188 gene list.

## Evidence journal
- nde2 single mutant has no effect on mitochondrial NADH oxidation; contribution only seen in nde1 nde2 [PMID:9733747 "rates of mitochondrial NADH oxidation were about 3-fold reduced in an nde1Delta mutant and unaffected in an nde2Delta mutant."].
- [PMID:9696750 "Disruption of a closely related gene designated NDH2 has no effect on these properties."]
- Mitochondrial supercomplex member [PMID:11502169 "two external NADH-dehydrogenases Nde1p and Nde2p"]; IMS location from proteomics [UniProt:Q07500].
- No purified-enzyme data; MF activity annotations are ISS/IEA, supported indirectly by double-mutant phenotype.

## Curation decisions
- Core MF GO:0120555 (by family + genetics), BP GO:0006120 (not in GOA; not added as NEW because NDE2-specific evidence is only the double mutant), CC inner membrane.
- pyruvate fermentation to ethanol: MARK_AS_OVER_ANNOTATED (indirect).
