# UQCRQ (O14949) review notes

## Identity
- UniProt O14949, QCR8_HUMAN. HGNC:29594. 82 aa (mature 2-82; INIT_MET removed).
- Names: Cytochrome b-c1 complex subunit 8 / Complex III subunit 8 / Complex III subunit VIII /
  Ubiquinol-cytochrome c reductase complex 9.5 kDa protein / ubiquinone-binding protein QP-C.
- Family: UQCRQ/QCR8 family. Pfam PF02939 (UcrQ). InterPro IPR004205 / IPR036642.

## Function (from UniProt file:human/UQCRQ/UQCRQ-uniprot.txt)
- Non-catalytic **low-molecular-weight structural subunit** of mitochondrial respiratory Complex III
  (ubiquinol-cytochrome c oxidoreductase / cytochrome b-c1 complex, CIII). One of 6 low-MW subunits
  (UQCRH, UQCRB, UQCRQ, UQCR10, UQCR11, subunit 9). The catalytic redox centres are in cytochrome b,
  the Rieske Fe-S protein (UQCRFS1) and cytochrome c1 — NOT in UQCRQ.
- Historically identified as the "ubiquinone-binding protein QP-C" — contributes to the ubiquinone
  binding environment; no independent catalytic (oxidoreductase) activity.
- CIII catalyses electron transfer from ubiquinol to cytochrome c, coupled to proton translocation
  across the inner membrane (Q cycle).
- Topology: matrix 2-39, single TM helix 40-68, intermembrane 69-82. Single-pass inner-membrane protein.

## Localization
- Mitochondrial inner membrane (GO:0005743); part of respiratory chain complex III (GO:0045275).
- Note: GO:0005750 "mitochondrial respiratory chain complex III" is now OBSOLETE (verified via OLS);
  GOA correctly uses GO:0045275 "respiratory chain complex III". Use GO:0045275 for in_complex.

## Structure / assembly evidence
- Cryo-EM of the human respiratory megacomplex I2III2IV2 assigned UQCRQ within the CIII dimer
  [PMID:28844695]. UQCRQ TOPO_DOM/TRANSMEM features are ECO:0000269|PubMed:28844695.

## Disease
- Mitochondrial complex III deficiency, nuclear type 4 (MC3DN4; MIM:615159): homozygous
  Ser45→Phe (S45F) missense variant; severe neurological disorder (encephalopathy, psychomotor
  retardation, ataxia, failure to thrive, etc.) [PMID:18439546; UniProt DISEASE + VARIANT VAR_045911].
  (PMID:18439546 not in publications/ cache; disease facts cited from UniProt file.)

## GOA review decisions (26 annotations)
- CC complex III (GO:0045275) IBA/IEA/IPI, inner membrane (GO:0005743) IEA/IDA/ISS/TAS, mitochondrion
  (GO:0005739) IDA/HTP: ACCEPT — well-supported structural/localization annotations.
- BP GO:0006122 (mito electron transport ubiquinol->cyt c) IBA/IEA/NAS: ACCEPT — core process CIII
  mediates; UQCRQ contributes as a structural subunit.
- BP GO:0045333 cellular respiration NAS: ACCEPT — correct broader BP.
- 8 brain-development BP terms (GO:0021539 subthalamus, GO:0021548 pons, GO:0021680 cerebellar
  Purkinje cell layer, GO:0021766 hippocampus, GO:0021794 thalamus, GO:0021854 hypothalamus,
  GO:0021860 pyramidal neuron, GO:0030901 midbrain), all IEA GO_REF:0000107 (Ensembl Compara transfer
  from mouse expression/phenotype ECO:0000265): MARK_AS_OVER_ANNOTATED. These reflect the ortholog's
  developmental expression/phenotype, not a UQCRQ-specific developmental function; UQCRQ is a
  ubiquitously required housekeeping respiratory subunit. Not a "clearly-wrong IEA mapping" (deficiency
  does cause a neurological disease), so over-annotation rather than REMOVE.

## Core functions
- molecular_function: GO:0005198 structural molecule activity (subunit-specific; UQCRQ is non-catalytic).
- contributes_to_molecular_function: GO:0009055 electron transfer activity (complex-level activity of CIII).
- directly_involved_in: GO:0006122 (mito electron transport, ubiquinol to cytochrome c); GO:0045333 cellular respiration.
- locations: GO:0005743 mitochondrial inner membrane.
- in_complex: GO:0045275 respiratory chain complex III (GO:0005750 obsolete).

## Verbatim supporting quotes verified
- UniProt FUNCTION: "Component of the ubiquinol-cytochrome c oxidoreductase, a" ... "The cytochrome b-c1
  complex catalyzes electron transfer from ubiquinol to cytochrome c, linking this redox reaction to"
- UniProt SUBUNIT: "6 low-molecular" / "weight protein subunits UQCRH/QCR6, UQCRB/QCR7, UQCRQ/QCR8,"
- UniProt SUBCELLULAR LOCATION: "Mitochondrion inner membrane"
- UniProt DISEASE: "Mitochondrial complex III deficiency, nuclear type 4 (MC3DN4)"
- PMID:34800366: "mitochondrial high-confidence proteome of >1,100 proteins (MitoCoP)"
- PMID:28844695 abstract: "reveals the precise assignment of individual subunits of"
- Reactome R-HSA-164651: "complex III transfers electrons from ubiquinol to cytochrome c"
</content>
</invoke>
