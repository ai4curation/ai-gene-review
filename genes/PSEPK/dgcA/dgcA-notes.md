# dgcA curation notes

- Q88R24 is the soluble flavoprotein component of the Pseudomonas DgcAB system. The `OxRdtase_FMN_N` fold name alone does not establish FMN binding.
- The characterized DgcA-like Q1QYW1 enzyme carries noncovalently bound FAD [PMID:32631860, "a monomer of 79 kDa with a noncovalently bound flavin adenine dinucleotide"].
- Pseudomonas genetics and isotope tracing support DgcAB-dependent conversion of dimethylglycine to sarcosine. [PMID:17951379, "conversion of DMG to sarcosine."]
- UniProt's `EC 1.5.8.-` assignment implies a flavin acceptor, while the
  pathway model uses the more specific ferredoxin-linked `EC 1.5.7.3` reaction
  and places DgcB before ETF. GO:0047865 is retained as the best available
  substrate-specific term, with a new ferredoxin-linked child term proposed to
  capture the acceptor distinction.

## 2026-11-04 completion session

No provider deep research was generated in this session (no API keys).
- Orthology check (`dgcA-bioinformatics/`): Q88R24 vs DdhC Q1QYW1 is 81.2%
  identical over the full length, and Q88R23 vs Csal_0991 is 72.2%.
- GO:0047865 is dropped from the MODIFY and from core_functions. Its
  definition requires ETF as the acceptor, but the curated DdhC reaction is
  EC 1.5.7.3 (ferredoxin acceptor; ETF is downstream of the ferredoxin). The
  MODIFY target is now the existing GO:0033694 (CH-NH donors, iron-sulfur
  protein as acceptor) plus the NTR "N,N-dimethylglycine/sarcosine
  dehydrogenase (ferredoxin) activity", named after EC 1.5.7.3, with parent
  GO:0033694 (previously GO:0016645).
- The FMN binding row is resolved from UNDECIDED to MARK_AS_OVER_ANNOTATED, to
  match the DdhC review: FAD is the only demonstrated flavin in the subfamily.
- NEW glycine betaine catabolic process (ISS from the P. aeruginosa genetics).


## Independent module audit — 2026-11-06

All four rows reviewed. Retain FMN over-annotation and inherited FAD/BP proposals; refine the general redox row to CH-NH donor chemistry without fixing an unmeasured acceptor. DdhC product stoichiometry and dye assays establish oxidation, while the ferredoxin/ETF sequence remains a model. The historical ferredoxin NTR remains conditional, outside the core. PA14 dgcB, not every dgc gene, was directly traced by NMR.

Sources: [PMID:32631860] full text: “DMGDH activity was measured with the dye-linked assay systems, with PMS as the electron intermediator and DCPIP or NBT as the terminal electron acceptor.” The mechanism paragraph explicitly says “a possible reaction mechanism of DdhC toward DMG was proposed”. [PMID:17951379] full text: PA14 mutants, PAO1 locus numbering, direct NMR on dgcB and soxA. KT2440 functional transfer remains an orthology inference.

All original annotation payloads and inherited NEW rows retained unchanged. No NEW rows added. Raw UniProt/GOA and existing provider artifacts preserved. Default Falcon research genuinely attempted; failed with HTTP 403 authentication/access error. Manual source assessment is recorded here; no provider report was fabricated.
