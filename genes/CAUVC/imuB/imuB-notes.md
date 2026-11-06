# imuB (CC_3212, Q9A3J2) curation notes

- No provider deep research is available for this gene; no `-deep-research-*.md` file was
  generated in this session. The review rests on the two cached primary papers and UniProt.
- imuB and dnaE2 act in one damage-tolerance pathway; the double mutant is not additive.
  [PMID:15886391, "The imuB dnaE2 double mutant does not exhibit an exacerbated phenotype, indicating again that these genes cooperate in the same pathway of damage tolerance."]
- The UV mutational signature is changed identically in imuB and dnaE2 mutants, which is
  what makes the pathway's output mutagenic rather than merely protective.
  [PMID:15886391, "The mutation signature of UV light is remarkably similar in dnaE2 and imuB strains."]
- DinB is not part of this pathway in C. crescentus: a dinB imuB double mutant is no worse
  than imuB alone.
  [PMID:15886391, "The dinB imuB strain presents the same levels of UV-induced mutagenesis as the imuB single mutant, confirming that DinB is not implicated in error-prone repair in the conditions tested."]
- The adaptor role (GO:0030674) is transferred from the mycobacterial ortholog, where it
  rests on two-hybrid data plus a clamp-binding separation-of-function allele.
  [PMID:20615954, "Yeast two-hybrid analyses indicate that ImuB interacts with both ImuA' and DnaE2, as well as with the beta-clamp."]
  The same paper states the catalytic residues are missing in ImuB proteins generally.
  [PMID:20615954, "Despite retaining structural features characteristic of Y-family members, ImuB homologs lack conserved active-site amino acids required for polymerase activity."]
- The single existing GOA row (GO:0006281, DNA repair) is a UniProt combined-pipeline IEA
  whose basis is the UmuC domain IPR001126 plus TreeGrafter node PANTHER:PTN000118183. It
  is a TreeGrafter route, not a PAINT IBA; PTHR35369's only PAINT node is PTN002176549
  (GO:0006281, seeded by M. tuberculosis O50419).
