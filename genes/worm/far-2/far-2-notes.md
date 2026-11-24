# worm far-2 notes

## 2026-11-24 review

- Fetched `worm` `far-2` directly from UniProtKB accession `P34383` into
  `genes/worm/far-2/`.
- UniProtKB identifies P34383 as *Caenorhabditis elegans* `far-2`/F02A9.3, a
  reviewed 182-aa precursor with a predicted residues 1-17 signal peptide, a
  Gp-FAR-1 domain, and PANTHER family `PTHR31418:SF19`.
- PANTHER `PTHR31418:SF19` separates FAR-2 from the filarial-FAR-1 subfamily:
  P34383/FAR-2 is in SF19, while *C. elegans* P34382/FAR-1, *Brugia malayi*
  Q93142/FAR-1 and *Onchocerca volvulus* Q25619/FAR-1 are all in
  `PTHR31418:SF7`.
- The GOA ISS rows for fatty-acid and retinol binding cite PMID:12592563, an
  abstract-only review about FAR proteins and C. elegans as a model. The direct
  cached biochemical evidence for FAR-2 is PMID:12502713: recombinant Ce-FAR-1
  through Ce-FAR-6 bound DAUDA, cis-parinaric acid and retinol in
  fluorescence-based assays with micromolar dissociation constants.
- The WormBase gene description states that far-2 is expressed in body-wall
  muscle and vulval cells of adult hermaphrodites and that transcript levels
  progressively increase during development. I could not trace those expression
  claims in the cached abstracts and left them unverified.
- External provider deep research was attempted with Falcon and
  Perplexity-lite fallback, but only the `claude_code` provider was available
  in this environment. No manual content was written under a provider
  `-deep-research` filename.

FAR-2 has direct recombinant ligand-binding evidence but no cached
loss-of-function or native-cargo study tying P34383 to a specific C. elegans
biological process.
