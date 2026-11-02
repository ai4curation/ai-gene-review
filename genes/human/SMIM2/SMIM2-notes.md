# SMIM2 (Q9BVW6) review notes

## 2026-10-03 Tier 2 microprotein review

### Identity
- UniProt Q9BVW6 SMIM2_HUMAN, 85 aa, PE1; alias C13orf44. One predicted helical TM segment
  (residues 21-43) and a disordered C-terminal region (51-85); UniProt places it in "Membrane;
  Single-pass membrane protein" by curator inference (ECO:0000305), not experiment.
- Family: InterPro IPR062622 / Pfam PF29500 (SMIM2 family only). No PANTHER family listed in the entry.
- Expression: HPA "Tissue enriched (testis)" (UniProt DR HPA line). HPA JSON (proteinatlas.org,
  fetched 2026-10-03) reports testis nTPM 22.5 and an antibody-based subcellular location of
  nucleoplasm/nuclear bodies. A nuclear-body signal for a single-pass membrane protein is hard to reconcile
  with its topology. It is a single-antibody HPA call that GOA has not ingested, so it is not
  used for annotation.

### Literature search
- PubMed `SMIM2[tiab] OR C13orf44[tiab]` -> 2 hits (PMID:38482248 m7G lncRNA signature;
  PMID:34527442 sarcopenia cut-offs, where "SMI" is skeletal muscle index). Neither concerns the protein.
- No functional study of SMIM2 exists.

### GOA rows
- 3 x protein binding (IPI) from the two Y2H interactome maps: UBQLN1 (Q9UMX0, and isoform
  Q9UMX0-2) from HI-II-14 [PMID:25416956] and UBQLN2 (Q9UHD9) from HuRI [PMID:32296183].
  Ubiquilins are cytosolic chaperones for exposed transmembrane domains
  [PMID:27345149 "We show that Ubiquilin family proteins bind transmembrane domains in the cytosol
  to prevent aggregation and temporarily allow opportunities for membrane
  targeting."]. A Y2H hit between a single-pass TM peptide and UBQLN1/2 is what TMD-client
  recognition predicts; it reports hydrophobicity and says nothing about SMIM2 function. -> REMOVE (no
  informative MF can be substituted).
- membrane (IEA, GO_REF:0000044 from SubCell SL-0162) -> ACCEPT. Consistent with the single TM helix.

### Conclusion
Nothing is known about SMIM2 function. No core function, no NEW terms.
