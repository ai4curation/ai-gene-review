# PPP2R1B Research Notes

## Gene Identity
- **Gene:** PPP2R1B (HGNC:9303)
- **Protein:** PP2A scaffold subunit A-beta (PR65-beta), UniProt P30154
- **Chromosomal location:** 11q23, a region frequently deleted in human cancers

## Core Function
PPP2R1B encodes the beta isoform of the PP2A structural/scaffold A subunit (PR65-beta). It is the minor A subunit isoform, comprising approximately 5-10% of total PP2A scaffold in the cell, with PPP2R1A (Aalpha) being the dominant isoform (~86% sequence identity) [PMID:17540176 "PP2A complexes containing Abeta represent a small fraction of the total PP2A complexes"].

The primary molecular function is scaffolding: PPP2R1B coordinates assembly of the PP2A heterotrimeric holoenzyme (A-B-C). HEAT repeats 1-10 bind regulatory B subunits, while HEAT repeats 11-15 bind the catalytic C subunit [deep-research-falcon, referencing Lambrecht 2013 and Xing 2006].

## Key Literature Findings

### Tumor Suppressor Function via RalA
PMID:17540176 (Sablina et al., Cell, 2007) is a landmark paper demonstrating PPP2R1B is a bona fide tumor suppressor. Key findings:
- Suppression of PP2A Abeta expression permits immortalized human cells to achieve a tumorigenic state [PMID:17540176 "suppression of PP2A Abeta expression permits immortalized human cells to achieve a tumorigenic state"]
- PP2A Abeta specifically forms complexes with RalA GTPase (PP2A Aalpha does not) [PMID:17540176 "the small GTPase protein RalA was the only protein that specifically formed complexes with Abeta subunit"]
- PP2A Abeta-containing complexes dephosphorylate RalA at Ser183 and Ser194 [PMID:17540176 "PP2A Abeta-containing complexes dephosphorylate RalA at Ser183 and Ser194, inactivating RalA"]
- Cancer-associated Abeta mutants fail to form productive PP2A complexes and cannot bind RalA [PMID:17540176 "cancer-associated Abeta mutants are defective in binding to B and/or C subunits"]
- Aalpha does NOT functionally substitute for Abeta loss [PMID:17540176 "Overexpression of PP2A Aalpha in these cells failed to revert the transformed phenotype induced by Abeta suppression"]

### UNC5H2/B-PP2A-DAPk Apoptosis Pathway
PMID:21172653 (Guenebeaud et al., Mol Cell, 2010) identifies PR65-beta specifically:
- siRNA screen identified PR65-beta (PPP2R1B) as required for UNC5H2-induced apoptosis [PMID:21172653 "we identified the structural subunit PR65beta of the holoenzyme protein phosphatase 2A (PP2A)"]
- UNC5H2/B recruits a complex including PR65-beta and DAPk [PMID:21172653 "UNC5H2/B recruits a protein complex that includes PR65beta and DAPk and retains PP2A activity"]
- PP2A dephosphorylates DAPk, activating it and triggering apoptosis
- Netrin-1 binding prevents this by allowing CIP2A (PP2A inhibitor) to interact with UNC5H2/B

### PP2A B56 and ERK Dephosphorylation
PMID:16456541 (Letourneux et al., EMBO J, 2006): The IPI annotation to PPP2R5C (Q13362, B56gamma) is based on interaction from this study that characterized B56-containing PP2A holoenzymes and their role in ERK dephosphorylation. The A subunit here would be providing the scaffolding role.

### PP2A Interaction Proteomics
Multiple high-throughput studies confirm PPP2R1B interactions:
- PMID:19156129 (Glatter et al., Mol Syst Biol): systematic AP-MS mapping of PP2A system
- PMID:18782753 (Goudreault et al., Mol Cell Proteomics): PP2A interaction network, STRIPAK complex
- PMID:28330616 (Yadav et al., Cell Syst): systematic phosphatase interactome

### Structural Features
- 15 HEAT repeats forming an elongated horseshoe scaffold
- Conformational flexibility, especially around HEAT 12-13 hinge region
- N-terminal HEAT repeats (1-10): B subunit binding
- C-terminal HEAT repeats (11-15): C subunit binding

## Localization
- Context-dependent, driven primarily by B subunit composition
- IBA annotations for nucleus, cytoplasm, cytosol are appropriate for a broadly distributed scaffold
- Membrane raft localization (IDA from PMID:21172653) in context of UNC5H2/B signaling
- Synapse-related IEA annotations are based on mouse ortholog data

## Key Interactions (from UniProt/IntAct)
- PPP2CA (P67775): catalytic subunit -- core interaction
- PPP2R1A (P30153): paralog, self-association or co-purification
- PPP2R2A (P63151, B55alpha): B subunit
- PPP2R5A (Q15172, B56alpha): B subunit
- PPP2R5C (Q13362, B56gamma): B subunit
- PPP2R5D (Q14738, B56delta): B subunit
- PPP2R5E (Q16537, B56epsilon): B subunit
- RALA (P11233): specific substrate/interactor for Abeta but NOT Aalpha
- Clock (O08785, mouse): circadian-related interaction
- Unc5b (O08722, mouse): dependence receptor apoptotic pathway

## Cancer Relevance
- Somatic mutations in 8-15% colon cancers, 15% lung cancers, 13% breast cancers
- Gene at 11q23 -- frequently deleted locus
- Cancer-associated mutants are functionally null (cannot form PP2A complexes or regulate RalA)
- Biallelic inactivation needed for transformation

## Annotation Review Considerations
- "Protein binding" (GO:0005515) is uninformative per curation guidelines; however these IPI annotations from IntAct reflect real physical interactions (PP2A subunit assembly, substrate binding). The underlying interactions are valid but the GO term is too generic.
- The IBA annotations for PP2A complex, phosphatase regulator activity, and localization terms are well-supported and represent core functions.
- Spindle assembly and meiotic sister chromatid cohesion IBAs are appropriate -- PP2A-B56 is well-known to protect centromeric cohesion via Shugoshin, and PPP2R1B interacts with SGO1 (UniProt).
- The apoptosis annotations from PMID:21172653 specifically name PR65-beta but represent a specialized pathway rather than a core evolved function.
- PMID:8392071 (Hendrix et al.) is about PR72 regulatory subunit characterization but PPP2R1B (PP2A C subunit) was co-purified showing interaction.
