# cbrA (PP_4695, Q88DX3) review notes

## Provenance

- Deep research: `just deep-research PSEPK cbrA --provider falcon` was attempted on 2026-10-23 and failed
  ("Failed to authenticate"); no other provider key is configured in this environment. The review is
  therefore built from UniProt and cached primary literature only. No `-deep-research-*.md` file exists.
- UniProt Q88DX3 is unreviewed and carries only the locus name PP_4695; the KT2440 literature names the
  locus `cbrA` [PMID:32214184 "To individually delete cbrA (PP_4695) and cbrB (PP_4696) from the genome of P. putida KT2440"].

## Function

- Sensor kinase: [PMID:32214184 "We show in in vitro experiments that CbrA autophosphorylates at the position of His766, and that the phosphoryl group is transferred to the response regulator CbrB."]
  No phosphatase activity [PMID:32214184 "A CbrA-dependent dephosphorylation of CbrB~P is not observed."]
- His766 is needed in vivo for crcZ activation [PMID:32214184 "Contrary to wild type CbrA, CbrA-H766N did not activate expression of crcZ indicating that the conserved histidine in the DHp domain (site of phosphorylation) is essential for signal transduction."]
- Transporter: [PMID:32214184 "It is demonstrated that CbrA can bind and transport L-histidine. Transport is specific for L-histidine and probably driven by an electrochemical proton gradient."]
  Corroborated in P. fluorescens SBW25 [PMID:26148710 "Our combined data implicate the SSSF domain of CbrA in histidine transport and suggest that transport is coupled to signal transduction."]
- The signal is unknown [PMID:32214184 "The lack of an effect of L-histidine leaves open the possibility that a yet to be identified intracellular metabolite is perceived by CbrA as a signal."]
- Conservation beyond Pseudomonas: in Azotobacter vinelandii (Pseudomonadaceae) [PMID:28404995 "While the histidine kinase CbrA was essential for glucose utilization, over-expression of the Crc protein arrested cell growth when glucose was the sole carbon source."]

## Curation decisions

- Accept GO:0000155 and GO:0000160 as core; general kinase/transferase/signal transduction terms are MODIFY to these.
- membrane -> plasma membrane; transporter terms refined to L-histidine (GO:0005290, GO:0089709).
- regulation of DNA-templated transcription (PAS InterPro2GO) marked over-annotated: CbrA acts on
  transcription only through CbrB.
- No NEW carbon catabolite repression row was added; the process is recorded on CbrB, whose activator
  output is the direct link to crcZ/crcY.
