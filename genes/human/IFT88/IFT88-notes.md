# IFT88 notes

Deep research: not run. In this environment falcon times out after 600 s and perplexity-lite is not
installed. The review uses the cached GOA-cited publications, two extra cached papers
(PMID:11062270, PMID:14603322) and the UniProt record.

## Key points
- Core IFT-B1 subunit. [PMID:11062270 "Complex B is composed of IFT88 and 10 other proteins including IFT172, IFT81, and IFT57"]
- Required for cilium assembly. [PMID:11062270 "This indicates that IFT is important for primary cilia assembly in mammals."]
- Pre-docks at the ciliary base and is released into the cilium by CEP19-RABL2. [PMID:28625565 "SIM revealed that IFT88 almost perfectly colocalized with RABL2B at the ciliary base"]
- Mouse polaris/Ift88 is needed for Hedgehog signalling. [PMID:14603322 "Genetic analysis shows that Wim, Polaris and the IFT motor protein Kif3a are required for Hedgehog signalling at a step downstream of Patched1"]

## Curation decisions
- REMOVE: IFT-A (GO:0030991) IDA from PMID:26980730. IFT88 is a canonical IFT-B subunit, and the
  same paper supports the retained IFT-B annotation. This looks like a wrong-complex term choice.
- REMOVE: response to silicon dioxide (a rat expression IEA) and all generic protein binding rows.
- MODIFY: positive regulation / regulation of cilium assembly changed to cilium assembly (IFT88 is part of the machinery, not a regulator).
- Reactome aggrephagy "cytosol" rows list IFT88 as a misfolded ciliary-protein substrate. They are kept as non-core.
- Core MF: contributes_to GO:0140597 (the GO label is now "protein carrier chaperone"), in IFT-B. No better
  single-subunit MF term exists for an IFT-B scaffold.
