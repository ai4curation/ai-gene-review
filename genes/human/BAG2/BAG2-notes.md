# BAG2 (O95816) research notes

## Identity / domain architecture
- BAG family molecular chaperone regulator 2 (BAG-2 / Bcl-2-associated athanogene 2). 211 aa. Single BAG domain (residues 109-189) and an N-terminal coiled coil (20-61). [file:human/BAG2/BAG2-uniprot.txt "DOMAIN          109..189"]
- Unlike BAG1, BAG2 lacks a ubiquitin-like (UBL) domain. [PMID:19228967 "However, BAG2 lacks the ubiquitin-like domain ( Lüders et al., 2000 ; Alberti et al., 2002 ), and therefore, may be suited to triage client proteins independently of ubiquitin."]

## Core molecular function: HSP70/HSC70 nucleotide-exchange factor (co-chaperone)
- BAG2 is a co-chaperone for HSP70/HSC70, acting as a nucleotide-exchange factor (NEF) that promotes ADP release and thereby client release. [file:human/BAG2/BAG2-uniprot.txt "Acts as\nCC       a nucleotide-exchange factor (NEF) promoting the release of ADP from"]
- Member of an evolutionarily conserved family of Hsp70/Hsc70 regulators; binds with high affinity (KD ~1-10 nM) to the ATPase domain of Hsc70 and modulates chaperone activity in a Hip-repressible manner. [PMID:9873016 "The human BAG-1, BAG-2, and BAG-3 proteins bind with high affinity (KD congruent with 1-10 nM) to the ATPase domain of Hsc70 and inhibit its chaperone activity in a Hip-repressible manner."]
- Direct biochemical confirmation of NEF / Hsp70-binding activity: BAG2 binds Hsp72 (HSPA1A) and acts in nucleotide/peptide release assays (though with notably lower affinity than BAG1/BAG3). [PMID:24318877 "Proteins with Bcl2-associated anthanogene (BAG) domains act as nucleotide exchange factors (NEFs) for the molecular chaperone heat shock protein 70 (Hsp70)."] [PMID:24318877 "their relative affinity values predicted their potency in nucleotide and peptide release assays"]

## CHIP (STUB1) E3 ligase inhibition / protein triage
- BAG2 is a main component of CHIP complexes and inhibits CHIP ubiquitin ligase activity by abrogating the CHIP/E2 cooperation. [PMID:16207813 "BAG-2 inhibits the ubiquitin ligase activity of CHIP by abrogating the CHIP/E2 cooperation and stimulates the chaperone-assisted maturation of CFTR."]
- This is a negative regulation of ubiquitination of chaperone clients; BAG2 stimulates CFTR maturation (a transmembrane transporter client). [PMID:16207813 "stimulates the chaperone-assisted maturation of CFTR"]
- BAG2 stabilizes immature CFTR conformations in addition to inhibiting CHIP. [PMID:16207813 "the stimulating activity of BAG-2 in CFTR maturation seems to reflect not only its ability to inhibit the CHIP-mediated ubiquitylation of CFTR, but also to stabilize immature CFTR conformations."]
- BAG2 interacts with STUB1 (CHIP) per UniProt interaction table. [file:human/BAG2/BAG2-uniprot.txt "Q9UNE7: STUB1"]

## Tau triage at the microtubule (neuronal context)
- The BAG2/Hsp70 complex is tethered to the microtubule and captures/delivers tau to the proteasome for ubiquitin-independent degradation; preferentially degrades Sarkosyl-insoluble and phosphorylated tau. [PMID:19228967 "The BAG2/Hsp70 complex is tethered to the microtubule and this complex can capture and deliver Tau to the proteasome for ubiquitin-independent degradation. This complex preferentially degrades Sarkosyl insoluble Tau and phosphorylated Tau."]
- BAG2 can associate with microtubules even without tau. [PMID:19228967 "BAG2 can associate with microtubules in the absence of Tau"]
- By inhibiting CHIP, BAG2 directs the Hsp70-tau complex away from ubiquitination. [PMID:19228967 "By inhibiting CHIP ( Qian et al., 2006 ), BAG2 directs the Hsp70-Tau complex away from ubiquitination."]
- This pathway is ubiquitin-INDEPENDENT and proteasome-dependent. [PMID:19228967 "these findings suggest that BAG2 mediates ubiquitin independent degradation of Tau through the proteasome."]
- NOTE on the negated annotation GO:0032436 (positive regulation of proteasomal ubiquitin-dependent protein catabolic process, NOT): consistent with BAG2 routing tau to a ubiquitin-INDEPENDENT proteasomal route while inhibiting the ubiquitin-dependent CHIP route. The NOT is well justified.

## Substrate stabilization by reducing ubiquitination (disease-relevant clients)
- BAG2 directly binds and stabilizes PINK1 by decreasing its ubiquitination. [PMID:24383081 "BAG2 (Bcl-2-associated athanogene family protein 2), a member of the BAG family, which directly binds with and stabilises PINK1 by decreasing its ubiquitination."]
- BAG2 (with BAG5) stabilizes pathogenic ataxin3-80Q by inhibiting its ubiquitination. [PMID:25006867 "BAG2 ... and BAG5 ... stabilise pathogenic ataxin3-80Q by inhibiting its ubiquitination"]

## Localization
- Cytosolic (Reactome TAS). Neuronal axon/dendrite/(dendritic) microtubule colocalization annotations derive from ARUK-UCL ISS based on the tau-triage microtubule work (PMID:19228967), which demonstrated microtubule tethering. These are real but context-specific (neuronal) localizations.

## Synthesis of core vs non-core
- CORE: HSP70/HSC70 nucleotide-exchange factor activity (GO:0000774), heat shock protein / chaperone binding, co-chaperone in a protein-folding chaperone complex, negative regulation of CHIP-mediated protein ubiquitination (GO:0031397), protein stabilization (GO:0050821) of chaperone clients.
- NON-CORE / context: tau binding & neuronal microtubule/axon/dendrite localization (neuronal protein-triage context); CFTR (transmembrane transporter) maturation.
- OVER-ANNOTATED / uninformative: the many high-throughput "protein binding" (GO:0005515) IPI annotations from interactome maps (spliceosome, viral perturbation, histone crosslinking, EGFR network, kinase networks, OpenCell, etc.).
- Broad/indirect BP terms (positive regulation of protein metabolic process GO:0051247; protein metabolic process GO:0019538) are over-broad parent terms.
