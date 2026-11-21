# worm far-1 notes

## 2026-11-21 review

- The fetched local GOA snapshot for P34382/FAR1_CAEEL contains only the TSV
  header even after rerunning `just fetch-gene worm far-1` on 2026-11-21.
  Direct QuickGO queries for `geneProductId=UniProtKB:P34382` on 2026-11-21
  returned the two IEA rows that also appear on the UniProtKB record:
  `GO:0005576` extracellular region from `GO_REF:0000044`/UniProtKB-SubCell
  and `GO:0008289` lipid binding from `GO_REF:0000002`/InterPro.
- UniProtKB identifies P34382 as *Caenorhabditis elegans* `far-1`/F02A9.2, a
  reviewed 182-aa precursor with a predicted residues 1-17 signal peptide, a
  Gp-FAR-1 domain, and PANTHER family `PTHR31418:SF7`.
- PANTHER `PTHR31418:SF7` places *C. elegans* FAR-1 in the same subfamily as
  *Brugia malayi* Q93142/FAR-1 and *Onchocerca volvulus* Q25619/FAR-1, while
  *C. elegans* FAR-2 P34383 is in `PTHR31418:SF19`. These assignments are
  recorded in `interpro/panther/PTHR31418/PTHR31418-entries.csv`.
- PMID:12502713 is the direct *C. elegans* FAR biochemical paper: recombinant
  Ce-FAR-1 through Ce-FAR-6 bound the fatty-acid probes DAUDA and
  cis-parinaric acid and retinol in fluorescence-based assays with micromolar
  dissociation constants [PMID:12502713 The FAR protein family of the nematode
  Caenorhabditis elegans. Differential lipid binding properties, structural
  characteristics, and developmental regulation., "Ce-FAR-1 to -6 bound
  DAUDA"].
- The WormBase gene description states that far-1 expression is highest in L3
  stage larvae and adult males. The cached PMID:12502713 abstract says the
  Ce-FAR genes were differentially transcribed and names Ce-far-3, Ce-far-4,
  and Ce-far-7 stage or sex peaks, but it does not state the far-1 pattern.
  Because no full text was cached, I left the far-1 expression pattern
  unverified and did not use it for biological-process curation.
- External provider deep research was attempted with Falcon and
  Perplexity-lite fallback, but only the `claude_code` provider was available
  in this environment. No manual content was written under a provider
  `-deep-research` filename.

FAR-1 has direct recombinant ligand-binding evidence but no cached
loss-of-function or native-cargo study tying P34382 to a specific C. elegans
biological process.
