# Svil (Supervillin, FBgn0266696; UniProt M9MRN1) - manual literature review

No deep-research API was available in this session; this file records a manual
literature search done with PubMed and the cached publications.

## Search record

- PubMed query `supervillin Drosophila` returned 2 records: PMID:36067835 (Mib2,
  border cell migration) and PMID:15506930 (review of flightless I and the gelsolin
  family; no Drosophila supervillin data).
- PubMed query `(Svil OR CG42669 OR CG33232 OR CG45186) AND Drosophila AND (villin OR
  gelsolin OR actin)` returned 4 records; the only one naming Svil is PMID:29873978,
  a transcript-level survey of ovaries after space flight (Svil mRNA lower).
- PMID:22530061 (gene-trap olfactory screen) was read in full.
- No Drosophila paper was found that studies the Svil protein biochemically,
  localizes it, or characterizes a specific Svil mutant allele.

## Findings

### Gene structure and the M9MRN1 product

- Svil is a large, alternatively spliced locus on 3L that merged many earlier CG
  models (synonyms in UniProt include CG42669, CG33232, CG1141, CG45186)
  [file:DROME/Svil/Svil-uniprot.txt "Synonyms=c62E-11"].
- UniProt lists more than 25 Svil products. Only some (e.g. X2JAM4, isoform AE,
  4526 aa) carry the villin headpiece and gelsolin-like signatures; M9MRN1 (isoforms
  AG/AH, 1872 aa) carries none [file:DROME/Svil/Svil-bioinformatics/RESULTS.md
  "M9MRN1 therefore lacks every gelsolin-like repeat and the headpiece domain."].
- M9MRN1 residues 1-1292 equal X2JAM4 62-1353; the C-terminal 580 residues are
  isoform-specific and end in a Phobius-predicted TM helix (1853-1871)
  [file:DROME/Svil/Svil-uniprot.txt "TRANSMEM        1853..1871"].
- UniProt protein existence is level 4 (predicted); M9MRN1 itself has never been
  studied as a protein.

### Olfactory screen (PMID:22530061)

- Gene-trap line BG02427 was mapped by BDGP to CG42669 (now part of Svil, 62E1), but
  3' RACE showed the vector spliced to CG42699 at 5C2, and both genes remained
  candidates [PMID:22530061 "For both these lines we were unable to obtain polytene
  chromosome in situ results and thus for each line both genes remain candidates"].
- BG02427 flies showed reduced olfactory trap responses in both sexes
  [PMID:22530061 "The male olfactory trap data shows significant differences in RI
  compared to the wild type control for four of the lines; BG00076, BG00973,
  BG01171, and BG02427"], but no excision reversion was done for this line (only
  BG00076 and BG00973 were tested), and EAG responses were normal for all lines.
- Conclusion: the olfactory behaviour phenotype cannot be assigned to Svil with
  confidence, and even if it were, it is a phenotype in a screen, not evidence of
  how Svil participates in olfaction.

### Mib2 interaction and border cell migration (PMID:36067835, abstract only)

- Mib2 complexes purified from Drosophila contain Supervillin, and depletion of
  Supervillin affects border cell migration [PMID:36067835 "We also found that three
  Mib2 interacting proteins, RhoGAP19D, Supervillin, and Myosin heavy chain-like,
  affect border cell migration."].
- Full text is not in PMC, so the isoforms detected, the reagents used and the size
  of the effect could not be checked.

### Vertebrate supervillin background (PMID:15506930)

- Supervillin is a member of the gelsolin family, whose members contain gelsolin-like
  repeats and may carry a C-terminal villin headpiece [PMID:15506930 "Members of the
  gelsolin family generally contain three or six copies of a 125-amino-acid residue
  gelsolin-related repeating unit, and may contain additional domains including the
  C-terminal villin-related 'headpiece'"].
- Vertebrate supervillin has also been implicated in nuclear-receptor signalling
  [PMID:15506930 "Recent studies indicate that supervillin, gelsolin and FliI are
  involved in intracellular signalling via nuclear hormone receptors"]. Nothing
  comparable has been shown in Drosophila.

## Summary

Drosophila Svil is a gelsolin-family (supervillin) gene with no direct functional
characterization. The M9MRN1 product lacks the actin-binding gelsolin and headpiece
regions. The only gene-specific functional observations are a candidate-level
olfactory behaviour phenotype with an ambiguous gene assignment and an abstract-level
report that Supervillin co-purifies with Mib2 and affects border cell migration.
