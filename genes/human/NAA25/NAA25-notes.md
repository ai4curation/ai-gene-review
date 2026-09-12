# NAA25 (N-alpha-acetyltransferase 25, NatB auxiliary subunit / MDM20) research notes

## Identity
- UniProt Q14CX7; HGNC:25783; aka MDM20, NAP1, C12orf30, p120. 972 aa, TPR-repeat / α-solenoid protein.
- **AUXILIARY (non-catalytic) subunit of the human NatB N-terminal acetyltransferase complex.** NatB = NAA20 (catalytic) + NAA25 (auxiliary). The catalytic subunit (acetyltransferase activity) is NAA20, NOT NAA25.

## Core function
- Non-catalytic scaffold of NatB; NatB acetylates N-terminal Met of substrates retaining iMet before acidic/amide residues (Met-Asp, Met-Glu, Met-Asn, Met-Gln).
  [PMID:18570629 "They form a stable complex and in vitro display sequence-specific N(alpha)-acetyltransferase activity on a peptide with the N-terminus Met-Asp-"]
- NatB acts co-translationally; subunits co-sediment with ribosomes.
  [PMID:18570629 "hNAT3 and hMDM20 co-sediment with ribosomal pellets, thus supporting a model where hNatB acts co-translationally on nascent polypeptides"]
- hMDM20/NAA25 is required for normal cell-cycle progression; knockdown disrupts cell cycle.
  [PMID:18570629 "Specific knockdown of hNAT3 and hMDM20 disrupts normal cell-cycle progression, and induces growth inhibition in HeLa cells"]
- NatB N-terminal acetylation of actin/tropomyosin in yeast is linked to actin cytoskeleton/tropomyosin function (origin of the IBA "cytoskeleton organization" annotation from yeast/fly NatB phenotypes). In humans this is an inferred downstream BP, not a direct molecular activity of NAA25.

## Structure / complex
- NatB complex composed of NAA20 + NAA25. [UniProt SUBUNIT "composed of NAA20 and NAA25"; PMID:34230638]
- Cryo-EM structures of human NatB (PDB 6VP9, 7STX, 8G0L) confirm NAA25 as the large α-solenoid auxiliary subunit cradling catalytic NAA20.
- NAA20 missense variants impairing NatB cause autosomal-recessive developmental delay/ID/microcephaly. [PMID:34230638]

## Annotation notes
- GO:0010698 acetyltransferase activator activity (IBA) — appropriate MF for an auxiliary subunit that activates/scaffolds the catalytic subunit; this is the best available non-catalytic MF. ACCEPT as core (auxiliary role).
- GO:0031416 NatB complex (part_of) — well supported (IBA/IPI/ComplexPortal). Core CC.
- GO:0007010 cytoskeleton organization (IBA) — downstream BP from yeast NatB substrate (tropomyosin/actin); keep non-core.
- protein binding IPI (PMID:18570629, PMID:34230638) both WITH NAA20 (P61599) — the real catalytic partner; better captured by NatB complex membership. Non-core / modify-adjacent; KEEP_AS_NON_CORE.
- cytoplasm/cytosol localizations consistent (IDA HPA, IDA ComplexPortal, IEA). Golgi IDA (HPA) is in UniProt DR but not in the GOA stub — not reviewed.
