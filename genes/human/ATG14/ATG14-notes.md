# ATG14 notes

## 2026-06-02 review setup

- Started review from fetched UniProt/GOA-derived stub. ATG14 is a Beclin 1-associated autophagy factor and PI3KC3-C1 subunit; the UniProt record states that it is "required for both basal and inducible autophagy", determines localization of the autophagy-specific PI3-kinase complex PI3KC3-C1, enhances PIK3C3 activity in a BECN1-dependent manner, and promotes STX17/SNAP29/VAMP8-dependent autophagosome-endolysosome fusion [UniProt:Q6ZNE5].
- Key early complex evidence: human Atg14 and UVRAG form mutually exclusive Beclin 1/Vps34 complexes; Atg14 localizes to autophagic isolation membranes and Atg14 silencing suppresses autophagosome formation [PMID:18843052 "Atg14 is present on autophagic isolation membranes"; PMID:18843052 "Silencing of human Atg14 in HeLa cells suppresses autophagosome formation"].
- Barkor/Atg14L was identified as an autophagy-specific Beclin 1/class III PI3K factor; depletion reduces autophagy and autophagosome formation, whereas overexpression activates autophagy and increases autophagosomes [PMID:19050071 "Elimination of Barkor expression by RNA interference compromises starvation- and rapamycin-induced lipidation of LC3 and autophagosome formation"; PMID:19050071 "Overexpression of Barkor leads to autophagy activation"].
- Atg14L and UVRAG bind Beclin 1 mutually exclusively; Atg14L localizes at ER, isolation membranes, autophagosomes, and unidentified puncta, and Atg14L knockout caused defective autophagosome formation [PMID:19270696 "Atg14L and UVRAG bind to Beclin 1 in a mutually exclusive manner"; PMID:19270696 "Knockout of Atg14L in mouse ES cells caused a defect in autophagosome formation"].
- ER targeting evidence supports phagophore/ER-membrane localization: ATG14L cysteine repeats are required for ER localization and autophagosome formation, and the BATS domain is important for targeting the PI3K complex to the ER and autophagosome biogenesis [PMID:20713597 "Autophagy requires endoplasmic reticulum targeting of the PI3-kinase complex via Atg14L"].
- The C-terminal BATS domain targets Barkor/Atg14L to PtdIns(3)P-rich autophagic membranes and is required for PI3KC3 recruitment and autophagy stimulation [PMID:21518905 "PI3KC3 recruitment and autophagy stimulation by Barkor/Atg14(L) require the BATS domain"].
- Structural and interaction studies place ATG14 as the autophagy-specific organizer of the Beclin 1-VPS34/PIK3C3 complex, supporting class III PI3K complex and protein-membrane adaptor/regulator annotations rather than generic protein binding [PMID:22314358 "Atg14L-containing complex is primarily involved in early stage autophagosome formation"; PMID:25490155 "Architecture and dynamics of the autophagic phosphatidylinositol 3-kinase complex"].
- ATG14 has a later autophagosome fusion role: it binds the STX17-SNAP29 t-SNARE complex on autophagosomes, primes it for VAMP8 interaction, and promotes autophagosome-endolysosome fusion [PMID:25686604 "ATG14 promotes membrane tethering and fusion of autophagosomes to endolysosomes"; UniProt:Q6ZNE5].
- BECN2 also interacts with ATG14 through a metastable coiled-coil to mediate autophagy, consistent with ATG14 acting as a PI3KC3-C1/BECN-family adaptor rather than only as a generic binding protein [PMID:28218432].
- Falcon deep research requested for ATG14 as part of the full review process.
- Falcon deep research timed out after the configured 600 second limit and did not produce `ATG14-deep-research-falcon.md`; final review therefore relies on the cached UniProt, GOA, Reactome, and publication evidence above.

## Description cleanup note

The YAML `description` field was revised to keep it as a standalone biological summary. Project-specific curation framing moved here instead.

- Moved out of the YAML description: the Proteostasis Network framing emphasized ATG14 as an autophagy-initiation/autophagosome-maturation component rather than a generic protein-binding or class I PI3K/AKT signaling factor.
