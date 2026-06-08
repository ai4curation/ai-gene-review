# NAA35 (N-alpha-acetyltransferase 35, NatC auxiliary subunit / MAK10 / EGAP) notes

## Identity
- UniProt Q5VZE5; HGNC; aka MAK10, EGAP (embryonic growth-associated protein homolog). 725 aa.
- **AUXILIARY (non-catalytic) subunit of the human NatC complex** (NatC = NAA30 catalytic + NAA35 + NAA38). MAK10 family.

## Function
- Auxiliary component of NatC; NatC acetylates N-terminal Met before bulky/hydrophobic residues.
  [UniProt FUNCTION "Auxillary component of the N-terminal acetyltransferase C (NatC) complex which catalyzes acetylation of N-terminal methionine residues"]
- NatC N-terminal acetylation protects substrates from N-end-rule ubiquitination/degradation. [PMID:37891180]
- Knockdown of NatC subunits -> p53-dependent apoptosis. [PMID:19398576]
- EGAP (mouse ortholog) implicated in smooth-muscle-cell proliferation / embryonic vascular development. [PMID:16484612 title "Embryonic growth-associated protein is one subunit of a novel N-terminal acetyltransferase complex essential for embryonic vascular development"] -> origin of GO:0048659 (ISS/IEA from mouse).

## Complex / structure
- Component of NatC (NAA35 + NAA38 + NAA30). [UniProt SUBUNIT]
- Cryo-EM structures of human/Candida NatC (PDB 7MX2, 7RB3) show NAA35/Mak10 as the large scaffold subunit.

## Annotation notes
- NO catalytic acetyltransferase MF on NAA35 in GOA (correct — it is non-catalytic). Core CC = NatC complex.
- GO:0031417 NatC complex (IBA/IEA/IPI/IDA) — core CC, accept.
- protein binding IPI: PMID:19398576 WITH NAA30 (Q147X3) and NAA38 (Q9BRA0) = real complex partners -> KEEP_AS_NON_CORE (subsumed by NatC). PMID:33961781 same partners. PMID:40205054 WITH NAA30. PMID:32296183 (HuRI binary screen) WITH TRIM7 (Q9C029) = isolated HT interaction, unrelated -> MARK_AS_OVER_ANNOTATED.
- negative regulation of apoptotic process (IBA, IMP PMID:19398576): NatC KD -> p53-dependent apoptosis, i.e. NatC normally suppresses apoptosis. Downstream BP of complex function -> KEEP_AS_NON_CORE.
- smooth muscle cell proliferation (ISS/IEA from mouse EGAP): peripheral developmental/vascular role, organism-specific -> KEEP_AS_NON_CORE.
- cytoplasm/cytosol localizations (IDA/NAS/ISS/IEA) consistent -> accept; cytoplasm is primary.
