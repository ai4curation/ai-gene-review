# IFT140 notes

Deep research: not run. In this environment falcon times out after 600 s and perplexity-lite is not
installed. The review uses the cached GOA-cited publications and the UniProt record.

## Key points
- IFT-A core subunit (with IFT122 and IFT144). [PMID:27932497 "proposed that Chlamydomonas IFT122, IFT140, and IFT144 create a stable core, with which IFT43 and IFT139 can interact"]
- Retrograde IFT. [PMID:22503633 "IFT140 is one of the six currently known components of the intraflagellar transport complex A (IFT-A) that regulates retrograde protein transport in ciliated cells."]
- Ciliary entry of GPCRs via the TULP3 adaptor. [PMID:20889716 "TULP3 and IFT-A, in turn, promote trafficking of a subset of G protein-coupled receptors (GPCRs), but not Smoothened, to cilia."]
- Human IFT-A cryo-EM structure. [PMID:36775821 "TULP3, the cargo adapter, interacts with IFT-A through its N-terminal region, and interface mutations disrupt cargo transport."]

## Curation decisions
- Generic protein binding rows (IFT144, IFT122) removed; IFT-A membership is already captured.
- Regulation of cilium assembly (IMP) changed to cilium assembly.
- PMID:40472089 (GPR45/TULP3) supports the IFT-A rows only through the TULP3-IFT-A adapter
  statement. No IFT140-specific assay was found in the cached text, so I deferred to the curator.
