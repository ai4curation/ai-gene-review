# Q66T51 notes

## 2026-11-23

- Started the BRUMA Q66T51 beta-tubulin review after live UniProt searches for
  Brugia PTHR11588 members showed that Q66T51 is a 448 aa PE2 beta-tubulin
  cDNA in the same family as the previously merged `bma-ben-1` review for
  WormBase `Bm4733` / `A0A1U7F2B2`.
- UniProt has no `GN` gene symbol or WormBase/WBParaSite cross-reference for
  Q66T51, so I used the accession as the review slug and did not invent a
  Brugia isotype name. A direct comparison of the Q66T51 and A0A1U7F2B2 SQ
  blocks found 447/448 identical residues, with Q66T51 carrying T352 in the
  `FVEWIPNNVK TTVCDIPPRG` segment where the BMA-BEN-1 sequence carries A352.
  Q66T51 therefore most likely samples the Bma-ben-1 locus as an allelic or
  sequencing variant from the 2004 AY705382 cDNA deposit.
- `just paint-losses BRUMA Q66T51` reported that Q66T51 is in PANTHER
  `PTHR11588` but not as a leaf of the cached PAINT tree, and found no IRD or
  IKR loss on the gene lineage.
- Q66T51 has the same nine GOA rows as the merged `BRUMA/bma-ben-1` review and
  the live ONCVO O61358 beta-tubulin GOA row set.
  Seven are automated beta-tubulin rows for GTPase activity, GTP binding,
  structural constituent of cytoskeleton, microtubule, cytoskeleton,
  microtubule-based process and microtubule cytoskeleton organization. Two
  EnsemblMetazoa biological-process rows transfer C. elegans BEN-1 behavior
  phenotypes to this unassayed B. malayi beta-tubulin.
- The UniProt record ties Q66T51 to EMBL AY705382 / AAU12501.1 from Schwab et
  al. 2005 [PMID:16103581 Detection of benzimidazole resistance-associated
  mutations in the filarial nematode Wuchereria bancrofti and evidence for
  selection by albendazole and ivermectin combination treatment.,
  "Resistance to albendazole in veterinary nematodes is known to be caused by
  either of two single amino acid substitutions from phenylalanine to tyrosine
  in parasite beta-tubulin at position 167 or 200"]. The abstract describes W.
  bancrofti SNP surveillance under albendazole/ivermectin treatment, but does
  not assign Q66T51 to a B. malayi benzimidazole-sensitive isotype.
- Reading the Q66T51 sequence from the local UniProt `SQ` block shows the
  wild-type haplotype at the three canonical resistance positions: F167, E198
  and F200. The single T352/A352 difference from A0A1U7F2B2 is far from these
  codons.
