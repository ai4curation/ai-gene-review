# NAA38 (N-alpha-acetyltransferase 38, NatC auxiliary subunit / LSMD1 / MAK31) notes

## Identity
- UniProt Q9BRA0; aka LSMD1 (LSM-domain-containing 1), MAK31, PFAAP2. 125 aa, small Sm-like (LSm) fold protein.
- **Small AUXILIARY (non-catalytic) subunit of the human NatC complex** (NatC = NAA30 catalytic + NAA35 + NAA38). Belongs to the snRNP Sm proteins family.

## Function
- Auxiliary component of NatC; NatC acetylates N-terminal Met before bulky/hydrophobic residues.
  [UniProt FUNCTION "Auxillary component of the N-terminal acetyltransferase C (NatC) complex which catalyzes acetylation of N-terminal methionine residues"]
- NatC N-terminal acetylation protects substrates from N-end-rule ubiquitination/degradation. [PMID:37891180]
- NatC KD -> p53-dependent apoptosis. [PMID:19398576]

## Annotation notes
- Sm-like fold -> IEA RNA binding (GO:0003723, InterPro IPR047575). NAA38 is the Sm-like subunit of NatC; there is no evidence it binds RNA in its NatC role. This is a domain-family IEA transfer; likely an over-annotation in the NatC context. MARK_AS_OVER_ANNOTATED.
- NatC complex (IEA/IPI/IDA) — core CC.
- protein binding IPI: PMID:19398576 WITH NAA35 (Q5VZE5) = real NatC partner -> KEEP_AS_NON_CORE. PMID:25416956 (Y2H) WITH PDE9A/PRR20C/N4BP2L2; PMID:32814053 (neurodegeneration interactome) WITH ATN1/KLK6 — isolated HT interactions, unrelated -> MARK_AS_OVER_ANNOTATED.
- negative regulation of apoptotic process (IMP PMID:19398576): NatC KD -> apoptosis; downstream BP -> KEEP_AS_NON_CORE.
- Localizations: cytoplasm (IDA/NAS/IEA) primary; nucleus (IDA PMID:19398576, IEA) and nucleoplasm (IDA HPA) reported -> keep nucleus non-core, cytoplasm accept.
