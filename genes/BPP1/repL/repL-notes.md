# repL (P19654) — Curation Notes

## Summary
- **Gene symbol**: `repL`
- **UniProtKB**: `P19654` (`REPL_BPP1`, 281 aa, 30.9 kDa)
- **Organism**: Escherichia phage P1 (`NCBITaxon:2886926`)
- **Function**: Lytic replication initiator protein RepL encoded in the C1-controlled `kilA-repL` operon. Essential for initiating bidirectional theta-mode viral DNA replication during the lytic cycle from the lytic origin `oriL`, which is embedded within the distal half of the `repL` coding sequence.

## Literature Evidence
- **Hansen 1989 (`PMID:2661830`)**:
  - Sequenced the P1 lytic (`L`) replicon (`X14937`) and identified the promoter-distal 281-codon `repL` open reading frame (30.9 kDa) essential for L-replicon autonomous plasmid replication when derepressed from C1 operator `Op53`.
  - Quote: `"A promoter-distal open reading frame (repL) of 281 codons, encoding a 30.9-kilodalton peptide, was shown by amber mutations and a frame-shift mutation to be essential for replicon function."`
- **Sternberg & Cohen 1989 (`PMID:2661831`)**:
  - Demonstrated that the L-replicon is the principal replicon used for P1 DNA replication during the lytic cycle and is contained within a 1093-bp DNA segment encoding the 281-codon `repL` gene under the control of the C1-repressible `P53` promoter.
  - Quote: `"Evidence is provided here that the L-replicon is the principal replicon used for DNA replication during the lytic cycle. The L-replicon (exclusive of its promoter) is shown to be contained within a 1093-base-pair DNA segment that includes a 281-codon open reading frame, designated repL."`
  - Quote: `"The kilA gene was shown to be non-essential for both replication and lytic development whereas the repL gene probably encodes an essential replication protein."`
- **Łobocka et al. 2004 (`PMID:15489417`)**:
  - Summarized the organization of the P1 lytic replicon (`kilA-repL`): lytic replication initiates bidirectionally in the theta mode from `oriL`, which is located within the C-terminal half of the `repL` coding sequence (containing two DnaA boxes and an A+T-rich region) and requires the RepL initiator protein as well as host DnaA and transcription through `oriL`.
  - Quote: `"Lytic replication initiates bidirectionally in the theta mode from an origin, oriL , distinct from the plasmid origin and located within the essential replication gene, repL"`

## Annotation Review Decisions
- `GO:0006260` (`DNA replication`, IEA: `GO_REF:0000043`): **MODIFY** to `GO:0006270` (`DNA replication initiation`) and `GO:0039693` (`viral DNA genome replication`). RepL is specifically the lytic replication initiator protein that initiates bidirectional theta-mode viral genome replication from `oriL` (`PMID:2661830`, `PMID:2661831`, `PMID:15489417`).
