# agxtb notes

## Setup and provenance

- Fetched with `just fetch-gene` on Q6PHK4 (TrEMBL, 423 aa; synonym agxt); 14 GOA rows (5 IBA, 2 IEA, 6 ISS from
  rat/mouse/human AGXT, 1 IDA from PMID:18618001). ZFIN ZDB-GENE-010302-3, Ensembl ENSDARG00000018478, chromosome 2.
- **Deep research unavailable**: Edison returned 402 Payment Required and the OpenAI key is invalid. Literature
  searched by hand via Europe PMC (same queries as agxta; see `../agxta/agxta-notes.md`).
- DANRE_DUPLICATION batch 4, random draw 11 (seed 20260928); paralog agxta. The pair analysis lives in
  `../agxta/agxta-bioinformatics/` (RESULTS.md, output.txt).

## What is known about the zebrafish gene

- No experimental study of the protein. Predicted MTS and no PTS1 in a bioinformatic survey
  [PMID:35295584 "Interestingly, zebrafish encode another putative AGT (agxtb, Q6PHK4_DANRE) which lacks a PTS1 but possesses an N-terminal MTS."]
  with the survey's explanation of what a mitochondrial AGT does
  [PMID:35295584 "Mitochondrial AGT can transaminate alanine and serine to pyruvate and hydroxypyruvate for gluconeogenesis."].
- The only experimental GOA row is an estrogen-response IDA from a whole-adult microarray study: an AGT probe was
  down-regulated in tissues of fish exposed to estrogenic compounds
  [PMID:18618001 "Alanine-glyoxylate aminotransferase−1.47NS−0.80−0.85−1.82NSNS−1.014#"]. This is a transcript change,
  not a function; marked over-annotated.
- ZFIN curated expression: RT-PCR only (whole larva at long-pec; adult male kidney).

## Background

See `../agxta/agxta-notes.md` for AGT biochemistry and the evolution of its targeting. Key points for this copy:
the mitochondrial form of mammalian AGT comes from an upstream start that adds a cleavable MTS
[PMID:21558762 "Transcription from the upstream start site generates the 1900-nucleotide mRNA for a 45-kDa precursor for SPTm containing a cleavable N-terminal mitochondrial targeting signal of 22 amino acids."],
and mitochondrial AGT handles glyoxylate from hydroxyproline
[PMID:21558762 "In carnivores, its mitochondrial localization appears to be needed to metabolize glyoxylate formed from L-hydroxyproline in mitochondria."].

## My analysis (../agxta/agxta-bioinformatics/RESULTS.md)

- 32-residue Arg-rich N-terminal extension (MMPRTVLSRCARLTQQVPLESALSGKQSVQRG) sharing a motif with the 38-residue
  gar AGXT extension; the annotated start is the first possible Met (in-frame genomic stop 20 codons upstream).
- C-terminus SKA, which does not fit the PTS1 consensus; SKA is also the end of most agxtb orthologues in the
  teleost panel, while gar ends SKV.
- Catalytic K209 and R360 (human numbering) conserved. agxtb is closer to gar than agxta (71.8% vs 61.5%) and has
  fewer lineage-specific changes (32 vs 59).
- Expression largely shared with agxta (liver, kidney, intestine, spleen); agxtb is the higher larval transcript
  (175 vs 50 TPM at day 5).

## GOA review decisions (summary)

- MF rows (IBA, IEA, ISS) accepted; mitochondrion (ISS) accepted as the predicted location.
- Peroxisome IBA and ISS marked over-annotated: the copy lost the C-terminal PTS1 and kept the MTS; propagation
  review recorded on the IBA row. Not removed because nothing has been localized experimentally.
- Pyruvate biosynthetic process kept as non-core; estrogen response IDA marked over-annotated.
