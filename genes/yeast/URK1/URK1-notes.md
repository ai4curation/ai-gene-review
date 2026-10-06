# URK1 (P27515, YNR012W) notes

Module: `pyrimidine_salvage`, role = uridine/cytidine kinase (EC 2.7.1.48; YeastCyc also EC 2.7.1.213 with GTP).
YeastCyc: URIDINEKIN-RXN and CYTIDINEKIN-RXN (YEAST-RNT-SALV), RXN-14093 deoxycytidine kinase (YEAST-SALV-PYRMID-DNTP; no citation on reaction).

## Evidence journal
- Cytidine kinase [PMID:10501935 "cytidine is phosphorylated into CMP by the uridine kinase (Urk1p)"]
- Uridine salvage genetics [PMID:11872485 "which is also deficient in uridine kinase (urk1), leads to the inability of the mutant to utilize uridine as the sole source of pyrimidines"]
- Function, cytoplasm+nucleus GFP, PRK and UPRTase-like Pfam domains, interactions with DAS2 and FUR1 [UniProt:P27515]
- Deoxycytidine: YeastCyc pathway comment attributes in vivo dC metabolism by Urk1 to PMID:12111094, whose abstract only covers Urh1 [PMID:12111094 "We have shown that not only uridine and cytidine, but also 5-fluorouridine, 5-fluorocytidine and deoxycytidine are substrates for this enzyme."] (Urh1). Not verified for Urk1.

## Decisions
- Kinase MF and salvage BPs ACCEPT; core = uridine kinase (UMP salvage) + cytidine kinase (CTP salvage).
- protein binding x9 REMOVE. Nucleus non-core. Generic kinase MODIFY. Deoxyribonucleoside salvage KEEP_AS_NON_CORE.
- GO-CAM YEAST-SALV-PYRMID-DNTP types the dC reaction with uridine kinase activity (GO:0004849) rather than deoxycytidine kinase (GO:0004137).
