# ATP7B (Wilson Disease Protein) - Research Notes

## Gene Identity
- **UniProt:** P35670 (ATP7B_HUMAN)
- **Gene symbol:** ATP7B (synonyms: PWD, WC1, WND)
- **Full name:** Copper-transporting ATPase 2 (EC 7.2.2.8)
- **Disease:** Wilson disease (WD) [MIM:277900]

## Core Function Summary

ATP7B is a P1B-type copper-transporting ATPase predominantly expressed in liver hepatocytes. Its two main physiological roles are:

1. **Copper incorporation into ceruloplasmin** at the TGN [PMID:12763797 "copper is incorporated into various cuproenzymes such as ceruloplasmin in hepatocytes (mediated by ATP7B)"]
2. **Biliary copper excretion** via vesicular sequestration and exocytosis [PMID:16472602 "the primary mechanism of biliary copper excretion involves ATP7B-mediated vesicular sequestration of copper rather than direct copper translocation across the canalicular membrane"]

## Key Structural Features

- Six N-terminal heavy metal-associated (HMA) domains, each with a GMXCXXC copper-binding motif [PMID:14709553 "six soluble N-terminal metal-binding domains containing a conserved CXXC metal-binding motif"]
- Eight transmembrane domains with a conserved CPC (Cys-Pro-Cys) motif essential for copper transport [PMID:9837819 "Mutation of the CPC motif resulted in a nonfunctional protein, which demonstrates that this motif is essential for copper transport by ATP7B"]
- Nucleotide-binding (N) domain, phosphorylation domain (DKTGTIT), phosphatase domain (TGE) [PMID:16567646]
- Can bind ~5.5 copper atoms per molecule [UniProt, PMID:20032459]

## Copper-Dependent Trafficking

ATP7B undergoes copper-responsive subcellular trafficking:
- **Low copper:** Resides at the TGN [PMID:16939419 "ATP7B...mediates the excretion of excess copper from hepatocytes into bile. Excess copper causes the protein to traffic from the TGN to subapical vesicles"]
- **High copper:** Redistributes to cytoplasmic/pericanalicular vesicles [PMID:16472602 "elevated copper levels stimulated trafficking of ATP7B to pericanalicular vesicles and not to the canalicular membrane"]
- **Copper removal:** Returns to TGN [UniProt CC, PMID:10942420]
- Trafficking is coupled to catalytic cycle: acyl-phosphorylation required for anterograde trafficking, dephosphorylation for TGN retrieval [PMID:16939419]

## Subcellular Localization Debate

There is a genuine controversy about the steady-state localization of ATP7B:
- **TGN model (majority view):** Most studies report TGN localization at basal copper, with copper-induced trafficking to vesicles [PMID:9837819, PMID:16472602, PMID:16939419, PMID:17919502]
- **Late endosome model (Harada group):** Harada et al. consistently report late endosome localization with Rab7 and NPC1 co-localization, arguing ATP7B is NOT a Golgi resident [PMID:15681833 "ATP7B is a late endosome-associated membrane protein...not a Golgi resident protein"]
- **Resolution:** The late endosome data may represent a post-Golgi compartment that ATP7B traffics through. The TGN model is more widely accepted and consistent with ceruloplasmin biosynthesis role.

## Important: ATP7B is NOT a Plasma Membrane Transporter

Key distinction: ATP7B primarily mediates copper excretion via **vesicular sequestration**, NOT direct translocation across the plasma membrane [PMID:16472602]. This is different from ATP7A which traffics to the basolateral plasma membrane [PMID:15269005].

## Protein Interactions

- **ATOX1 (copper chaperone):** Delivers copper to ATP7B N-terminal domains, stimulates catalytic activity [PMID:12029094 "Atox1 transfers copper to the purified amino-terminal domain of WNDP in a dose-dependent and saturable manner...leads to the stimulation of the WNDP catalytic activity"]
- **COMMD1/MURR1:** Interacts with ATP7B; mutations cause copper toxicosis in Bedlington terriers; involved in biliary copper excretion pathway [PMID:12968035, PMID:17919502]
- **DCTN4 (dynactin p62):** Copper-dependent interaction, may facilitate retrograde microtubule-mediated trafficking [PMID:16554302]
- **GRX1 (glutaredoxin):** Copper-dependent interaction, may facilitate copper binding by reducing disulphide bridges [PMID:16884690]
- **ZBTB16/PLZF:** Hepatocytic isoform interacts with C-terminus; connected to ERK signaling [PMID:16676348]

## Critical Issues with Current GO Annotations

1. **GO:0015677 copper ion import (IBA):** This is WRONG for ATP7B. ATP7B mediates copper EXPORT (into bile/vesicles/Golgi lumen), not import into the cell. This appears to be a phylogenetic inference error.

2. **GO:0005886 plasma membrane (IBA):** Questionable. ATP7B does NOT primarily traffic to the plasma membrane. It traffics to pericanalicular VESICLES. This is a key distinction from ATP7A [PMID:16472602].

3. **GO:1990961 xenobiotic detoxification by transmembrane export across the plasma membrane (IC):** The mechanism is vesicular sequestration, not direct plasma membrane export [PMID:16472602].

4. **GO:0005515 protein binding:** Multiple uninformative "protein binding" annotations should be replaced with specific interaction terms.

5. **GO:0016323 basolateral plasma membrane (IDA, PMID:15269005):** This paper is about ATP7A (Menkes), NOT ATP7B! This is a mis-annotation.

6. **GO:0005739 mitochondrion (IEA/HTP):** Based on a proteolytic fragment (WND/140 kDa) reported by one group [PMID:9600907]. Not widely reproduced. Dubious for the full-length protein.

7. **Redundant annotations:** Many terms appear with multiple evidence codes (e.g., GO:0140581 appears 6 times).

## Isoforms

- Isoform 1 (canonical): Golgi membrane localization
- Isoform 2: Lacks transmembrane domains, cytoplasmic localization, expressed in brain but not liver [PMID:9307043]
- Isoform 1 may be proteolytically cleaved to produce WND/140 kDa form (mitochondrial)
