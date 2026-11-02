# si:dkey-283b1.7 notes

ZFIN si:dkey-283b1.7 (ZDB-GENE-120215-126, chromosome 3); NCBI Gene 562406 (same symbol; RefSeq
protein named "Brorin"); Ensembl ENSDARG00000053460; UniProt E7F8B1 (TrEMBL, 242 aa, PE 4). PANTHER
PTHR46252:SF5 ("BRORIN-LIKE") within the brorin family. In panther_tgd_pairs.tsv it is the TGD_tree 1:1
partner of vwc2, with human ortholog VWC2 (O). Reviewed as part of DANRE_DUPLICATION batch 3 (random
sample).

## Deep research

Deep research was not available for this batch (Edison returned 402 Payment Required, and the
OpenAI key is invalid). I searched Europe PMC for "si:dkey-283b1.7": 0 hits. The gene is not
mentioned in the two zebrafish brorin-family papers (PMID:28448525, which covers vwc2; PMID:19852960,
which covers vwc2l). No literature exists for this gene. Everything below comes from my own analyses in
file:DANRE/si_dkey-283b1.7/si_dkey-283b1.7-bioinformatics/RESULTS.md.

## Which human gene?

- PANTHER calls it a VWC2 co-ortholog (O) and pairs it with vwc2 (LDO) on the Neopterygii|Teleostei branch.
- By sequence it is ambiguous. The core (VWFC 1+2) is 59.8% identical to human VWC2 and 54.9% to
  VWC2L. Over the full length it is 32.0% identical to VWC2 and 40.2% to VWC2L, because it lacks VWC2's
  long N-terminal region.
- Ensembl Compara (compara_check_output.md) relates it to both vwc2 and vwc2l only as "other paralogs" at
  the Bilateria level. It gives no gar or human ortholog.
- A true VWC2L ortholog exists separately (zebrafish vwc2l, B0UZC8, 95% core identity to human VWC2L).
  So si:dkey-283b1.7 is not the VWC2L ortholog. It is either a fast-evolving VWC2 ohnolog (PANTHER) or a
  separate lineage.
- Synteny with gar (synteny_output.md): the vwc2 region (chr 13) shares fignl1, ikzf1 and the SPMIP7
  ortholog with the gar vwc2 region. The si:dkey-283b1.7 region (chr 3) shares none of them, and no
  gene gives double-conserved synteny. The TGD origin therefore rests on the PANTHER tree alone. It is
  not established, and it conflicts with Ensembl Compara.

## Protein features

- Signal peptide 1-18. It has an intact cysteine-rich core (20/20 human VWC2 core cysteines) and a
  basic C-terminal tail. It does not have the RGD motif of human VWC2, which is not conserved in any fish.

## Expression

- Bgee RNA-Seq calls: retina (61.2), brain (58.2), larva. No ZFIN curated expression.

## Decisions

- Extracellular region (IBA, IEA) and negative regulation of BMP signaling (IBA): ACCEPT. The PAINT node
  PTN002921765 spans both VWC2 and VWC2L, so the inference holds whatever the exact orthology. The BMP
  activity is untested for this gene.
- AMPAR complex (IBA) and synapse (IEA): KEEP_AS_NON_CORE.
- No NEW annotations.
