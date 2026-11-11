# murD (P14900) — E. coli K-12 — curation notes

No provider deep-research file was generated for this gene; these notes are a manual
literature review built from the cached publications, the UniProt record and targeted
web lookups (2026-10-31).

## Identity and reaction

- MurD is UDP-N-acetylmuramoyl-L-alanine--D-glutamate ligase (EC 6.3.2.9), second Mur
  ligase; adds D-Glu to UDP-MurNAc-L-Ala (UMA)
  [PMID:9218784 "UDP-N-acetylmuramoyl-L-alanine:D-glutamate ligase (MurD) is a cytoplasmic
  enzyme involved in the biosynthesis of peptidoglycan which catalyzes the addition of
  D-glutamate to the nucleotide precursor UDP-N-acetylmuramoyl-L-alanine (UMA)"].
- Reaction: UMA + D-Glu + ATP = UDP-MurNAc-L-Ala-D-Glu + ADP + Pi (RHEA:16429)
  [file:ECOLI/murD/murD-uniprot.txt "Reaction=UDP-N-acetyl-alpha-D-muramoyl-L-alanine + D-glutamate + ATP ="].
- Mechanism: acyl-phosphate intermediate common to the Mur/FPGS ligase superfamily
  [PMID:9166795 "both enzyme families proceed through an ordered kinetic mechanism and
  form product via an acyl phosphate intermediate"].

## Kinetics and cofactor

- Km 7.5 uM UMA, 55 uM D-Glu, 138 uM ATP/Mg2+; kcat 931 min-1; <=1000 copies/cell;
  strongly dependent on potassium phosphate and Mg2+; reverse reaction catalysed
  [PMID:1765076 "The purified activity was highly dependent on the concentration of
  potassium phosphate and Mg2+"].
- Mg2+ cofactor (UniProt COFACTOR, ECO:0000305 from PMID:1765076). Optimum 5 mM Mg2+.
- D-Glu is the physiological acceptor (D-stereospecific; substrate pool supplied by MurI
  glutamate racemase). The cached sources do not report L-Glu activity quantitatively.

## Structure / oligomeric state

- Three domains of nucleotide-binding-fold topology; UMA site defined; ATP site
  inferred by comparison [PMID:9218784]. Open/closed domain movements of the C-terminal
  domain [PMID:10966819].
- E. coli MurD crystal structures (1UAG, 1EEH, 5A5E, 8V8X) are monomers; PDB/PISA list
  5A5E biological unit as monomeric (web lookup, NCBI Structure / SWISS-MODEL template
  pages). No biochemical evidence for a functional MurD homodimer. The GOA "identical
  protein binding" row is from a high-throughput Y2H self-interaction [PMID:24561554];
  treated as over-annotation.

## Physiology

- Essential gene in the dcw cluster (mra region, 2 min). Precursor pathway reconstituted
  in a cell-free system with E. coli Mur enzymes producing UDP-MurNAc-pentapeptide
  [PMID:24389752 "the activities of Mur enzymes derived from CFPS system were validated by
  the synthesis of the final product UDP-N-acetylmuramyl pentapeptide"].
- FEBA fitness data not reachable from this environment (`just fetch-fitness` failed).

## Keyword-derived process IEAs

- "regulation of cell shape" (GO:0008360) and "cell division" (GO:0051301) come from
  InterPro2GO (IPR005762, MurD family). MurD makes a soluble precursor; shape and division
  defects of mur mutants are indirect consequences of loss of peptidoglycan. Marked as
  over-annotation (consistent with genes/PSEPK/murD review).

## Interactions

- AP-MS [PMID:15690043] partner; Y2H TrxC (P0AGG4) [UniProt INTERACTION]. Generic protein
  binding removed per protein-binding policy.

## Module consistency

- modules/peptidoglycan_precursor_biosynthesis.yaml: MurD annoton = GO:0008764,
  substrates UMA, D-Glu, ATP; products UDP-MurNAc-L-Ala-D-Glu, ADP, phosphate. Matches.
  Module lists no Mg2+ cofactor (optional enhancement).
