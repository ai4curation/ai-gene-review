# olfm3b notes

## Setup and provenance

- Fetched with `just fetch-gene` on A0A8N7UT25 (TrEMBL, RefSeq XP_690154.2, "Noelin-3 isoform
  X1", 457 aa); 4 GOA rows (2 IBA, 2 IEA), none with a PMID. ZFIN ZDB-GENE-070912-606, Ensembl
  ENSDARG00000039174, chromosome 2.
- **Deep research unavailable**: Edison returned 402 Payment Required and the OpenAI key is
  invalid. Literature searched by hand via Europe PMC (`olfm3b` returns no hits; see
  `genes/DANRE/olfm3a/olfm3a-notes.md` for the wider OLFM3 searches).
- DANRE_DUPLICATION batch 3 (random draw 10, seed 20260928); paralog olfm3a.

## Zebrafish literature

None. ZFIN has no curated expression.

## Mammalian OLFM3

See olfm3a notes: secreted [PMID:12019210 "Both optimedin and myocilin are localized in Golgi and are secreted proteins."];
noelins are extracellular AMPA-receptor complex constituents
[PMID:37591201 "Noelin tetramers tightly assemble with the extracellular domains of AMPARs and interconnect them in a network-like configuration with a variety of secreted and membrane-anchored proteins including Neurexin1, Neuritin1, and Seizure 6-like."].

## Own analyses

Shared pair analysis in `genes/DANRE/olfm3a/olfm3a-bioinformatics/` (RESULTS.md).
- 83.2% identical to olfm3a; 81.0% to human OLFM3 isoform Q96PB7-3. OLF domain 85.0%, coiled
  coil 82.3% identical to human; all 6 human cysteines kept (plus 2 extra); Olfm1 calcium-site
  residues kept; sequons at the same positions as olfm3a.
- E-ERAD-475: 0-1 TPM at every stage to day 5 (olfm3a reaches 9-11 TPM in larvae).
- Bgee: brain 55.0, intestine 50.2, early embryo, blastula, ovary, tail, bone (low scores).
- Ensembl Compara disagrees with PANTHER on the duplication node for this pair (it places the
  olfm3a/olfm3b split at Gnathostomata and gives olfm3b, not olfm3a, the 1:1 gar and human
  orthologs); PANTHER calls it TGD_tree.

## Curation decisions

Extracellular region accepted; signal transduction IBA over-annotated (as for olfm3a); synapse
kept as non-core for this weakly neural copy. No NEW terms.
