# DNAJB13 research notes

## Identity
- UniProt P59910 (DJB13_HUMAN), 316 aa. HGNC:30718. Synonyms TSARG3, TSARG6 (testis/spermatogenesis).
- DnaJ homolog subfamily B member 13; HSP40/J-domain co-chaperone family. J domain at residues 4-68.

## Core function
- Structural/co-chaperone component of the axonemal **radial spoke complex** (radial spoke stalk),
  essential for motility of sperm flagella and motile (respiratory) cilia.
  [PMID:27486783 "Functions as part of axonemal radial spoke complexes that play an important part in the motility of sperm and cilia." (UniProt FUNCTION)]
- The Chlamydomonas ortholog localizes to radial spokes [PMID:27486783 "a gene encoding a HSP40 co-chaperone whose ortholog in the flagellated alga Chlamydomonas localizes to the radial spokes."].
- Homodimer; component of radial spoke complex 1 (RS1) spoke stalk together with RSPH14, DYDC1, ROPN1L, NME5 (UniProt SUBUNIT).
- RS1 composition / function in mammalian flagella confirmed by Iqub mouse model [PMID:36417862].

## Localization
- Cell projection: cilium, flagellum. Epithelial motile cilium and sperm flagellum [PMID:27486783 IDA].
- In spermatids enriched at the head-tail coupling apparatus; in mature sperm distributed along flagellum (By similarity to mouse Q80Y75).
- Tissue: testis and trachea.

## Disease
- Biallelic mutations cause **primary ciliary dyskinesia type 34 (CILD34, MIM:617091)**, autosomal recessive, with central-complex (CC) defects but normal dynein arms; male infertility from sperm flagellar dysfunction.
  [PMID:27486783 "this study, which establishes mutations in DNAJB13 as a cause of PCD, unveils the key role played by DNAJB13 in the proper formation and function of ciliary and flagellar axonemes in humans."]
- p.Met278Arg (CILD34 variant): protein instability, proteasomal degradation; loss of endogenous DNAJB13 in cilia/sperm. No effect on homodimerization.

## Chaperone activity
- Despite J-domain (HSP40), the established in vivo role is structural within the radial spoke, not a classic
  cytosolic HSP70-stimulating chaperone. IBA terms "protein-folding chaperone binding", "unfolded protein binding",
  "protein folding", and "cytosol" are transferred from family/PANTHER and are weakly supported for THIS protein's
  documented axonemal function. No direct demonstration of HSP70 ATPase stimulation for DNAJB13.

## Interactome (PMID:32296183, "A reference map of the human binary protein interactome" — HuRI Y2H)
- IPI partners: PLK4 (O00444), TOM1L1 (O75674-2), PIBF1 (Q4G0R1), MSS51 (Q4VC12), ZC3H12A (Q5D1E8),
  SEPTIN1 (Q8WYJ6), LHX4 (Q969G2), RAB3IP (Q96QF0-7), MDFI (Q99750), GORASP2 (Q9H8Y8), PICK1 (Q9NRD5), ZRANB1 (Q9UGI0).
- These are high-throughput binary Y2H hits, none of which map onto the radial-spoke biology; bare "protein binding", uninformative.

## GO annotation review reasoning
- Strong/accept: motile cilium, sperm flagellum (IDA, PMID:27486783); radial spoke (ISS/NAS/ComplexPortal); axoneme; axonemal central apparatus assembly (IMP, PMID:27486783); flagellated sperm motility / cilium movement (NAS).
- HPA sperm sub-compartments (midpiece/principal piece/end piece, IDA) — consistent with flagellar localization, keep.
- microtubule-based process (IEA/ARBA) — generic but consistent with axonemal role; keep as non-core.
- protein folding / chaperone binding / unfolded protein binding (IBA/IEA) — family-transferred, not demonstrated for this protein's documented function; mark as over-annotated or non-core.
