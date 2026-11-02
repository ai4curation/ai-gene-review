# abi1b notes

## Setup and provenance

- Fetched with `just fetch-gene` on A0A286YAJ7 (TrEMBL, RefSeq XP_005171233.1, "isoform X1",
  507 aa; secondary accession A0A8M2BIW1); 8 GOA rows (5 IBA, 3 IEA), none with a PMID.
  ZFIN ZDB-GENE-060929-1182, Ensembl ENSDARG00000062991, chromosome 2.
- **Deep research unavailable**: Edison returned 402 Payment Required and the OpenAI key is
  invalid. Literature searched by hand via Europe PMC (same searches as abi1a; see
  `genes/DANRE/abi1a/abi1a-notes.md`).
- DANRE_DUPLICATION batch 3 (random draw 7, seed 20260928); paralog abi1a.

## Zebrafish literature

No study of abi1b function. The only mention with a claim is a speculation, in a paper that
knocked down the paralog abi1a
[PMID:32368696 "Zebrafish, unlike mouse or human, have 2 orthologs for ABI1 (abi1a and abi1b) with abi1b likely compensating to maintain normal cardiac development."].
It was not tested.

## Mammalian ABI1

See abi1a notes. Core points: WAVE-complex assembly subunit
[PMID:15048123 "Thus, Abi1 orchestrates the proper assembly of the WAVE2 complex and mediates its activation at the leading edge in vivo."];
mouse knockout lethal at mid-gestation with heart and brain defects
[PMID:21482783 "Thus, Abi1-signaling events are not required for gastrulation but are critical during brain and heart development."].

## Own analyses

Shared pair analysis in `genes/DANRE/abi1a/abi1a-bioinformatics/` (RESULTS.md).
- abi1b is 77.5% identical to human ABI1 (abi1a 81.6%); WAVE-binding N-terminus 91.9%,
  coiled coil 100%, SH3 91.7% identical to human; divergence sits in the disordered linker.
- 13-residue N-terminal extension in the predicted isoform X1 (not verified by cDNA here).
- Not significantly faster-evolving than abi1a (gar relative-rate test).
- abi1b is the maternal/cleavage-stage copy (peak 28 TPM at 128-cell), 3-7 TPM after
  gastrulation; Bgee calls limited to early embryo, retina, brain, ovary, bone.

## Curation decisions

Same actions as abi1a for all 8 family-level rows (the protein and the IBA nodes are shared).
No NEW terms.
