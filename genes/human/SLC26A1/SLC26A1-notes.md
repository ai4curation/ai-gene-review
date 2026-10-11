# SLC26A1 (Q9H2B4) review notes

Deep research: `just deep-research-falcon human SLC26A1` failed ("All providers failed"), so the literature
work below was done manually from PubMed and the cached `publications/` files.

## Function
- Human SLC26A1 (SAT1) is a Na-independent, electroneutral anion exchanger moving sulfate, oxalate, bicarbonate
  and thiosulfate; chloride mainly acts as an allosteric activator [PMID:27125215 "electroneutral sodium-independent
  anion exchanger transporting sulfate, oxalate,"]. Cloning: [PMID:12713736 "induces sulfate, chloride, and oxalate
  transport in"]; expressed mostly in kidney and liver.
- No Cl-/HCO3- exchange shown for SLC26A1; chloride handling is "divergent" [PMID:27125215], hence the IBA to
  GO:0140900 is marked over-annotated (functional divergence from SLC26A3/A4/A6).

## Physiology and disease
- Sulfate: human homozygous loss of function causes renal sulfate wasting and hyposulfatemia; rare damaging variants
  lower plasma sulfate at population level [PMID:36719378 "we identify SLC26A1 as a sulfate transporter in humans and
  experimentally validate several loss-of-function alleles"]. OMIM 620372 hypersulfaturia.
- Oxalate (contested): first Sat1-null mouse had hyperoxaluria and CaOx stones [PMID:20160351]; a second knockout line
  did not [PMID:30383413 "Additionally, SAT-1-KO mice were neither hyperoxaluric nor hyperoxalemic."]. Biallelic
  variants in two CaOx stone formers [PMID:27210743]. Pfau et al.: "Thus, the role of SLC26A1 may be predominantly
  related to sulfate homeostasis, whereas its role in oxalate homeostasis requires further study." [PMID:36719378]
- dismech counterpart: kb/disorders/SLC26A1-Related_Oxalate_Transporter_Deficiency.yaml (oxalate and sulfate
  transporter activity DECREASED; oxalate mechanism flagged as a knowledge gap).

## Core functions chosen
1. GO:0015383 sulfate:bicarbonate antiporter activity / GO:1902358 sulfate transmembrane transport / basolateral PM.
2. GO:0019531 oxalate transmembrane transporter activity / GO:0019532 oxalate transport (physiological weight contested).
