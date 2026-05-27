# jar (Jaguar / Myosin heavy chain 95F) - Deep Research Notes

## Gene Identity

- **Gene symbol**: jar (jaguar)
- **Synonyms**: Mhc95F, 95F MHC, CG5695
- **UniProt**: Q01989 (MYS9_DROME)
- **FlyBase**: FBgn0011225
- **Species**: Drosophila melanogaster
- **Protein**: Myosin heavy chain 95F (class VI unconventional myosin)
- **Human ortholog**: MYO6 (unconventional myosin VI)

## Core Biology

jar encodes the sole Drosophila class VI unconventional myosin. Myosin VI is unique among all known myosins because it moves toward the minus (pointed) end of actin filaments, opposite to all other characterized myosins [PMID:12134162 "MyoVI is a pointed-end-directed, actin-based motor protein"]. This reversal in directionality is due to a unique insert in the converter domain that repositions the lever arm.

### Domain Architecture

From UniProt and InterPro:
- N-terminal SH3-like domain (residues 3-54)
- Myosin motor domain (residues 57-766) with ATP-binding site (residues 151-158)
- Actin-binding region (residues 647-666)
- Class VI-specific lever arm (IPR049016, residues 765-913) -- responsible for minus-end directionality
- IQ domain (residues 808-837) for light chain binding
- Coiled-coil region (residues 900-1022) for dimerization
- Cargo-binding domain (IPR032412, residues 1145-1231)

### Isoforms

Four known isoforms from alternative splicing:
- Isoform B (Q01989-1): canonical, expressed throughout life cycle
- Isoform H (Q01989-2): VSP_003343, insert at position 1047
- Isoform I (Q01989-3): VSP_003344/345, altered/truncated C-terminus
- Isoform 145 kDa (Q01989-4): head-specific isoform

## Key Functions (Literature Evidence)

### 1. Cytoplasmic Particle Transport in Embryos

The founding functional study showed that jar/95F myosin catalyzes actin-based, ATP-dependent transport of cytoplasmic particles in living Drosophila embryos [PMID:8202156 "this transport is actin-based, ATP-dependent and catalysed by one such unconventional myosin, the 95F myosin"]. This was the first direct observation of transport by an unconventional myosin in living cells.

### 2. Syncytial Blastoderm Organization

Antibody-inhibition studies showed jar is required for proper pseudocleavage furrow formation, nuclear positioning, and actin cap/furrow organization in the syncytial blastoderm [PMID:7790355 "95F myosin function is required to generate normal actin-based transient membrane furrows"]. Disruption leads to aberrant nuclear morphology, actin cytoskeleton disorganization, and spindle defects.

### 3. Spermatid Individualization

jar is essential for spermatogenesis. It localizes to the leading edge of the individualization complex (IC), which resolves shared membranes into individual spermatid membranes [PMID:10588662 "95F myosin is a component of the IC whose function is essential for individualization"]. Partial loss-of-function mutations cause male sterility. jar stabilizes the branched actin network in actin cones (investment cones) that mediate spermatid separation [PMID:16571671 "myosin VI stabilizes a branched actin network in actin structures (cones) that mediate the separation of the syncytial spermatids"]. FRAP experiments showed jar remains bound to F-actin for minutes, suggesting a tethering rather than transport role in cones [PMID:16571671].

The cargo-binding domain sites are critical for actin structure specialization during individualization [PMID:21853045 "The head (motor) and globular tail (cargo-binding) domains were both needed for localization at the cone front and dense meshwork formation"].

### 4. Oogenesis Transport

jar is involved in intra- and intercellular transport during oogenesis. It is found at ring canals and mediates microfilament-dependent transport of particles (including mitochondria) from nurse cells into the oocyte [PMID:9351468 "this unconventional myosin of class VI is involved in the transport processes...myosin-VI molecules located at the rim of the ring canals seem to be involved in particle transport into the oocyte"].

### 5. Neuroblast Asymmetric Division

jar is required for basal targeting of the cell fate determinant Miranda and correct spindle orientation in mitotic neuroblasts [PMID:12586070 "Miranda localization requires the unconventional myosin VI Jaguar (Jar). In jar null mutant embryos, Miranda is delocalized and the spindle is misoriented"]. Miranda directly binds to jar, suggesting active transport of determinants.

### 6. Border Cell Migration

jar is required for E-cadherin-mediated border cell migration during oogenesis. It stabilizes E-cadherin and Armadillo (beta-catenin) at the membrane [PMID:12134162 "MyoVI is required for border cell migration where it stabilizes E-cadherin and Arm"].

### 7. Epithelial Morphogenesis and Dorsal Closure

jar plays a role in cell-cell adhesion during dorsal closure. Lethal mutants show detaching cells and irregular epithelial sheets [PMID:15454264 "Myosin VI is crucial for correct cell morphology and maintenance of adhesive cellular contacts within epithelial cell layers"]. Required for egg chamber and imaginal disc morphogenesis [PMID:10523504].

### 8. Actin-Microtubule Crosstalk

jar co-immunoprecipitates with D-CLIP-190 (homolog of CLIP-170), a microtubule-binding protein. They colocalize in neurons and at the posterior pole of embryos [PMID:9472041 "The association of a myosin and a homologue of a microtubule-binding protein...leads us to speculate that these two proteins may functionally link the actin and microtubule cytoskeletons"].

### 9. Mitochondrial Transport Regulation

RNAi depletion of myosin VI in Drosophila neurons increases retrograde mitochondrial transport, suggesting it opposes (rather than promotes) microtubule-based transport, possibly facilitating organelle docking [PMID:20592219 "myosin V and VI play related but distinct roles in regulating MT-based mitochondrial movement: they oppose, rather than complement, protracted MT-based movements and perhaps facilitate organelle docking"].

### 10. Cargo Binding and Exocytosis

Proteomics identified multiple cargo-binding partners including Cornetto (microtubule-associated protein). jar and Cornetto are both required for Hedgehog secretion, indicating a role in exocytic trafficking [PMID:21368190 "the microtubule-associated protein Cornetto bound myosin VI, and we demonstrated a role for both in secretion of the lipidated morphogen Hedgehog"].

### 11. Light Chain Partners

- Androcam (Acam): testis-specific light chain for jar. Colocalizes at actin cone leading edges. Binds both IQ-motif light chain binding sites with high affinity [PMID:16790438 "Acam and not CaM acts as a myosin VI light chain in the Drosophila testis"].
- Essential light chain (ELC, mlc-c/sqh): identified by mass spectrometry as binding partner [PMID:16917818 "We identify four myosins (myosin II, myosin V, myosin VI and myosin VIIA)...as binding partners for the essential light chain"].
- Calmodulin: likely light chain in non-testis tissues.

## Verification of BioReason References

All PMIDs cited in the GOA annotations are REAL and verified:
- PMID:1429838 -- Kellerman & Miller 1992, J Cell Biol -- VERIFIED (initial cloning of 95F MHC)
- PMID:7790355 -- Mermall & Miller 1995, J Cell Biol -- VERIFIED (syncytial blastoderm)
- PMID:8202156 -- Mermall et al 1994, Nature -- VERIFIED (cytoplasmic particle transport)
- PMID:9351468 -- Bohrmann 1997, Cell Mol Life Sci -- VERIFIED (oogenesis transport)
- PMID:9472041 -- Lantz & Miller 1998, J Cell Biol -- VERIFIED (CLIP-190 association)
- PMID:10523504 -- Deng et al 1999, J Cell Sci -- VERIFIED (egg chamber/imaginal disc morphogenesis)
- PMID:10588662 -- Hicks et al 1999, Mol Biol Cell -- VERIFIED (spermatogenesis)
- PMID:12134162 -- Geisbrecht & Montell 2002, Nat Cell Biol -- VERIFIED (border cell migration)
- PMID:12432073 -- Rogat & Miller 2002, J Cell Sci -- VERIFIED (actin dynamics in spermatogenesis)
- PMID:12586070 -- Petritsch et al 2003, Dev Cell -- VERIFIED (neuroblast asymmetric division)
- PMID:12620217 -- Tuxworth & Chia 2003, Mol Cell -- VERIFIED (review/commentary on neuroblast finding)
- PMID:15454264 -- Millo et al 2004, Mech Dev -- VERIFIED (cell-cell adhesion, dorsal closure)
- PMID:16126191 -- Mermall et al 2005, Dev Biol -- VERIFIED (myosin V in spermatid individualization)
- PMID:16571671 -- Noguchi et al 2006, Mol Biol Cell -- VERIFIED (actin stabilization in spermatid individualization)
- PMID:16790438 -- Frank et al 2006, J Biol Chem -- VERIFIED (Androcam as testis light chain)
- PMID:16917818 -- Franke et al 2006, Cell Motil Cytoskeleton -- VERIFIED (nonmuscle myosin II light chain binding)
- PMID:19204120 -- Sousa-Nunes et al 2009, Genes Dev -- VERIFIED (PP4/Miranda localization)
- PMID:20592219 -- Pathak et al 2010, J Neurosci -- VERIFIED (mitochondrial transport)
- PMID:21368190 -- Finan et al 2011, PNAS -- VERIFIED (cargo-binding proteins, Hedgehog secretion)
- PMID:21853045 -- Isaji et al 2011, PLoS One -- VERIFIED (cargo-binding domain in actin cone)
- PMID:25694447 -- Beaven et al 2015, Mol Biol Cell -- VERIFIED (CLIP-190 in nervous system)

## Notes on PMID:16126191 and PMID:16917818

PMID:16126191 is primarily about Drosophila myosin V, not myosin VI. The annotation for sperm individualization (GO:0007291) from this paper may be based on the finding that myosin V and myosin VI cooperate during individualization -- the paper studies myosin V mutants and mentions myosin VI context.

PMID:16917818 is about nonmuscle myosin II light chains. Myosin VI (jar) was identified as a binding partner for the essential light chain by mass spectrometry. The myosin VI complex (GO:0031476) and myosin light chain binding (GO:0032027) annotations from this paper are based on co-precipitation data.

## BioReason Deep Research Assessment

The BioReason thinking trace is largely domain-architecture driven. It correctly infers many of the activities from the InterPro domains (motor, lever arm, cargo binding). However:

1. It mentions "GO:0033275 actin retrograde transport" -- this is not an actual GO term ID. The BioReason model occasionally fabricates GO term IDs.
2. It mentions "GO:0007303 cytoplasmic transport, nurse cell to oocyte" -- this is also not a standard GO ID; the correct term is GO:0007300 (ovarian nurse cell to oocyte transport).
3. It mentions "GO:0007301 follicle cell of egg chamber stalk formation" -- this appears fabricated; not a real GO term.
4. It mentions "GO:0007405 neuroblast proliferation" -- the correct term is GO:0055057 (neuroblast division).
5. The BioReason model does not make specific GO term predictions in the prediction section (MF, BP, CC sections are empty).
6. The functional summary is reasonable but generic -- it reads like a general myosin VI description and does not capture Drosophila-specific biology like the spermatid individualization tethering function.
