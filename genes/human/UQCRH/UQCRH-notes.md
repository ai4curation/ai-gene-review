# UQCRH (P07919) review notes

## Identity
- Cytochrome b-c1 complex subunit 6, mitochondrial (Complex III subunit 6 / subunit VIII).
- AltNames: Mitochondrial hinge protein; Cytochrome c1 non-heme 11 kDa protein; Ubiquinol-cytochrome c reductase complex 11 kDa protein.
- 91 aa precursor; TRANSIT 1-13 (mitochondrial); mature chain 14-91. Belongs to UQCRH/QCR6 family.
- Small, non-catalytic **structural subunit** of mitochondrial respiratory Complex III (cytochrome bc1).

## Core biology (verified)
- **Hinge protein**: "Mitochondrial hinge protein is a subunit of ubiquinol-cytochrome-c reductase in the respiratory chain and 'hinges' cytochrome c with cytochrome c1" [PMID:2826252 abstract].
- Structural component linking cytochromes c and c1: "Functional CIII is organised as a dimeric complex (CIII2) and UQCRH is thought to be a structural component linking the cytochromes c and c1 (Ohta et al, 1987)" [PMID:34750991].
- Deletion → impaired CIII activity (~50-60% residual), reduced holoenzyme MW, altered supercomplex distribution → CIII deficiency disease (MC3DN11) [PMID:34750991 IMP].
- One of the eight CIII subunits whose exact molecular role "remains to be fully elucidated" — i.e. non-catalytic; catalytic centres are MT-CYB, CYC1, UQCRFS1 [PMID:34750991].
- Location: mitochondrial inner membrane; peripheral membrane protein, intermembrane side [UniProt SUBCELLULAR LOCATION].

## GOA aspect/label anchors (use these exact current terms)
- CC: GO:0045275 respiratory chain complex III (NOT obsolete GO:0005750); GO:0005743 mitochondrial inner membrane; GO:0005739 mitochondrion; GO:0016020 membrane; GO:0098803 respiratory chain complex.
- BP: GO:0006122 mitochondrial electron transport, ubiquinol to cytochrome c; GO:0045333 cellular respiration; GO:0006119 oxidative phosphorylation; GO:0009060 aerobic respiration; GO:1902600 proton transmembrane transport.
- MF: GO:0008121 quinol-cytochrome-c reductase activity (the whole-complex activity; UQCRH is non-catalytic so this is contributes_to, not enables); GO:0005515 protein binding.

## Curation decisions
- Structural subunit, non-catalytic. MF for core_functions = **GO:0005198 structural molecule activity**, plus contributes_to GO:0008121 (the complex catalytic activity). Do NOT invent a catalytic MF for the subunit itself.
- The two `enables GO:0008121` annotations (IMP PMID:34750991; TAS PMID:2826252) attribute the WHOLE-COMPLEX activity to the subunit. UQCRH is non-catalytic, so `enables` is an over-annotation of the subunit's function. IMP shows deletion reduces CIII activity (consistent with structural/assembly role) but does not show UQCRH itself is the catalytic entity → MODIFY toward structural molecule activity / MARK_AS_OVER_ANNOTATED. IMP not verifiable-as-catalytic; keep as over-annotated (do not REMOVE experimental).
- Bare `protein binding` IPIs (PMID:25416956, PMID:32296183): high-throughput Y2H binary interactions with non-CIII proteins (ARL8A, ENTREP3, NDFIP1/2, PRRG1, RNF24). MARK_AS_OVER_ANNOTATED (uninformative + likely non-physiological for a mito inner-membrane subunit).
- GO:0016020 membrane (IEA ARBA): too general given inner-membrane evidence → MARK_AS_OVER_ANNOTATED.
- GO:0098803 respiratory chain complex (IEA + TAS): correct but generic parent of GO:0045275 → KEEP_AS_NON_CORE.
- GO:0005739 mitochondrion (HTP/HDA): correct but generic parent of GO:0005743 → KEEP_AS_NON_CORE.
- GO:1902600 proton transmembrane transport (IEA from GO:0008121 inter-ontology link): the complex translocates protons via the Q-cycle; for the non-catalytic hinge subunit this is a complex-level/context role → KEEP_AS_NON_CORE.
- GO:0006119 oxidative phosphorylation, GO:0009060 aerobic respiration, GO:0045333 cellular respiration: broader BP context; core BP is GO:0006122 → KEEP_AS_NON_CORE.
</content>
</invoke>
