# murC (P17952) — E. coli K-12 — curation notes

No provider deep-research file was generated for this gene; these notes are a manual
literature review built from the cached publications, the UniProt record and targeted
web lookups (2026-10-31).

## Identity and reaction

- MurC is UDP-N-acetylmuramate--L-alanine ligase (EC 6.3.2.8), the first of the four
  ATP-dependent Mur amide ligases (MurC, MurD, MurE, MurF) that build the stem peptide on
  UDP-MurNAc in the cytoplasm [file:ECOLI/murC/murC-uniprot.txt "Catalyzes the formation
  of the amide bond between UDP-N-acetylmuramic acid (UDP-MurNAc) and L-alanine"].
- Reaction: UDP-MurNAc + L-Ala + ATP = UDP-MurNAc-L-Ala + ADP + Pi (RHEA:23372)
  [file:ECOLI/murC/murC-uniprot.txt "Reaction=UDP-N-acetyl-alpha-D-muramate + L-alanine + ATP = UDP-N-"].
- ATP is hydrolysed to ADP + Pi, not AMP + PPi [PMID:8634271 "an ATP molecule is
  hydrolyzed concomitantly to produce ADP and orthophosphate"]. 18O transfer from the
  MurNAc carboxylate to Pi shows an acyl-phosphate intermediate [PMID:8634271 "ATP
  therefore assists in the process of the peptide bond formation by donating its
  gamma-phosphoryl group to activate the carboxyl group of UDP-N-acetylmuramic acid"].
  The same mechanism is shared by the whole Mur/folylpolyglutamate synthetase
  superfamily [PMID:9166795 "both enzyme families proceed through an ordered kinetic
  mechanism and form product via an acyl phosphate intermediate"].

## Kinetics and substrate specificity

- Purified, overproduced enzyme: Km 100 uM UDP-MurNAc, 20 uM L-Ala, 450 uM ATP/Mg2+;
  turnover 928 min-1; ~600 copies/cell; reverse reaction also catalysed
  [PMID:7601127 "The Km values for UDP-N-acetylmuramic acid, L-alanine and ATP/Mg2+ were
  estimated at 100, 20 and 450 microM"].
- Alternative amino acids in vitro: L-Ser (Km 850 uM) and Gly (Km 2500 uM), with much
  lower efficiency [file:ECOLI/murC/murC-uniprot.txt "It can also use L-serine and glycine,"].
  So the physiological acceptor is L-Ala; L-Ser/Gly use is an in vitro promiscuity
  (relevant to organisms that put Gly/Ser at position 1). Not annotated separately.
- Alanine analogues (3-fluoro-, 3-chloro-, 3-cyano-L-Ala) inhibit (UniProt CC ACTIVITY
  REGULATION, from PMID:7601127).

## Metal

- Mg2+ observed in the 2.6 A crystal structure (PDB 2F00; ligands are only MG, chains A
  and B, verified via PDBe ligand API) at residue 199 [file:ECOLI/murC/murC-uniprot.txt
  FT BINDING 199 Mg(2+), evidence PubMed:17139082, PDB:2F00]. ATP/Mg2+ is the substrate
  form [PMID:7601127].
- 2F00 contains no nucleotide, so the IDA "ATP binding" row from PMID:17139082 rests on
  structural comparison rather than an observed ATP complex; ATP binding is nonetheless
  certainly true (it is a substrate with a measured Km). Keep as non-core.

## Oligomeric state

- Sedimentation equilibrium: monomer-dimer equilibrium, Kd ~1.1 uM at 37 C; specific
  activity independent of oligomeric state [PMID:8634272 "the enzyme is active both as
  dimers and as monomers and that the specific activity is independent of the
  oligomerization state"].
- Crystal structure has a dimer and a "dimerization motif" found in ~50% of MurC
  sequences [PMID:17139082 "indicate the presence of a ;dimerization' motif in almost
  50% of the MurC enzymes"].
- Conclusion: homodimerization is real but not required for catalysis; non-core.

## Genetics / physiology

- murC ts mutant: very low L-Ala-adding activity, lyses at 42 C, reduced murein synthesis
  [PMID:4552998 "The other mutant possesses an l-alanine adding enzyme with a very low in
  vitro activity at both 30 and 42 C"]. murC3 allele = G344D [PMID:9166795].
- Genes map in the mra cluster (dcw cluster at 2 min) [PMID:4563986].
- Essential gene (Keio: no deletion mutant; consistent with ts lethality). FEBA fitness
  data not reachable from this environment (`just fetch-fitness` failed).

## Interactions (high-throughput)

- Y2H: FlxA, YtfT [PMID:24561554]; AP-MS: Butland et al. [PMID:15690043]. No functional
  consequence demonstrated; generic protein binding rows removed per protein-binding policy.
  The IPI row from PMID:17139082 with EcoliWiki:murC as partner is a self-interaction ->
  modified to protein homodimerization activity.

## Location

- Soluble cytoplasmic enzyme (UniProt Cytoplasm, ECO:0000305). The substrate UDP-MurNAc
  and product are soluble nucleotide precursors.

## Process annotations

- Peptidoglycan biosynthetic process: direct participant (catalyses the stem-peptide
  step). Accept.
- No regulation-of-cell-shape / cell-division / cell-wall-organization keyword IEAs exist
  on murC in GOA (unlike murD).

## Module consistency

- modules/peptidoglycan_precursor_biosynthesis.yaml: MurC annoton = GO:0008763, substrates
  UDP-MurNAc, L-Ala, ATP; products UDP-MurNAc-L-Ala, ADP, phosphate. Matches. Module does
  not list Mg2+ as a cofactor (MurB lists FAD); optional enhancement.
