# SLC16A9 (MCT9) curation notes

- UniProt Q7RTY1; SLC16/MCT family (MFS, TC 2.A.1.13). Not a classical lactate carrier.
- Creatine transporter: direct Xenopus-oocyte assay, extracellular-pH- and Na(+)-sensitive, low-affinity [PMID:31784090 "Kinetic analysis of hMCT9-mediated creatine uptake revealed that uptake consisted of two components, with apparent Km values of 237 mm (low-affinity) and 23.7 mm (high-affinity)"]. Km values are far above physiological plasma creatine (~25-100 uM), so physiological weight of the creatine activity is uncertain.
- Carnitine efflux transporter: experimentally validated [PMID:21886157 "we experimentally validated the predicted function of SLC16A9 as a carnitine efflux transporter"]; corroborated by Felmlee et al. 2020 [PMID:32144120 "MCT9 has been characterized as a carnitine efflux transporter"].
- Urate: common SLC16A9 variants are robustly GWAS-associated with serum uric acid / gout [PMID:19503597 "SLC16A9 (p = 1.1x10(-8))"], but no urate transport or metabolic step is demonstrated -> GO:0046415 urate metabolic process MARK_AS_OVER_ANNOTATED (association, not participation).
- Review: core MF GO:0005308 creatine TMT + GO:0015226 carnitine TMT at the plasma membrane; GO:0008028 KEEP_AS_NON_CORE (true family-level term, creatine is_a monocarboxylate); bare GO:0005515 REMOVE (x3); generic terms TOO_GENERAL. Batch 25.
