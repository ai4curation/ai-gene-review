# murF (P11880, b0086) notes

## Identity
- UDP-N-acetylmuramoyl-tripeptide--D-alanyl-D-alanine ligase (D-Ala-D-Ala-adding enzyme), EC 6.3.2.10; MurCDEF family, MurF subfamily (HAMAP MF_02019; TIGR01143; PANTHER PTHR43024:SF1). Monomer (PMID:2186811). Structure PDB 1GG4.
- No deep-research file; notes from cached publications, UniProt and web searches. FEBA fitness fetch failed.

## Function
- Final cytoplasmic step: adds D-Ala-D-Ala to UDP-MurNAc-L-Ala-gamma-D-Glu-meso-A2pm to make UDP-MurNAc-pentapeptide [PMID:2186811 "catalyzes the final cytoplasmic step in the biosynthesis of the bacterial peptidoglycan precursor"]; monomer, turnover 784 min-1 [PMID:2186811 "The enzyme is a monomer of molecular weight 49,000, and it has a turnover number of 784 min-1 for ATP-driven amide bond formation."].
- Third-position tolerance: kinetics similar with DAP-, cystathionine- and lanthionine-containing tripeptides [PMID:8021219 "The kinetic parameters of the MurF synthetase catalyzing the addition of D-alanyl-D-alanine were very similar for the meso-A2pm-,L-allo-cystathionine-, and meso-lanthionine-containing UDP-MurNAc tripeptides."]. Barreteau et al. 2008 review (PMID:18266853, web full text; cache is abstract only) states "The two forms of UDP-MurNAc-tripeptide (meso-A2pm and l-Lys) are equally effective as substrates." So E. coli MurF can use the Lys-tripeptide in vitro, but in vivo its substrate is the DAP-tripeptide because MurE excludes L-Lys.
- Assay substrate for inhibitor screening was the DAP-tripeptide made by Mpl [PMID:16377691 "UDP-MurNAc-L-Ala-gamma-D-Glu-diaminopimelate substrate prepared in a novel way by using muropeptide ligase enzyme"].

## GO term structure (checked via QuickGO, 2026-10-31)
- GO:0047480 "UDP-N-acetylmuramoyl-tripeptide-D-alanyl-D-alanine ligase activity" is defined on the L-lysine tripeptide (UDP-MurNAc-L-Ala-D-Glu-L-Lys).
- GO:0008766 "...2,6-diaminopimelate-D-alanyl-D-alanine ligase activity" is defined on the meso-DAP tripeptide (Rhea 28374, the reaction in UniProt P11880).
- They are siblings under GO:0016881 acid-amino acid ligase activity. GO:0008766 is the physiological activity of E. coli MurF; GO:0047480 is a real but non-physiological (in vitro) activity. The IBA for GO:0047480 (PTN000566380, donor S. aureus Q2FWH4) is a Lys-type activity propagated into a DAP-type organism.

## Genetics
- ts mutant (murF2, A288T) with temperature-sensitive D-Ala-D-Ala adding enzyme, impaired murein synthesis and accumulation of UDP-MurNAc-tripeptide [PMID:4552998 "One mutant possesses a temperature-sensitive d-alanyl-d-alanine adding enzyme, has an impaired rate of murein synthesis in vivo at both 30 and 42 C"].

## Module discrepancy
- `modules/peptidoglycan_precursor_biosynthesis.yaml` MurF annoton uses GO:0047480 (L-Lys tripeptide form) with E. coli P11880 and P. putida Q88N80 as representatives; both are DAP-type organisms. The module should use GO:0008766 (or a DAP/Lys variant set mirroring the MurE node). Not edited here (out of scope).
