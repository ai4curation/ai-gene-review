---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-23T21:48:12.643795'
end_time: '2026-01-23T21:58:02.490021'
duration_seconds: 589.85
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: STOML3
  gene_symbol: STOML3
  uniprot_accession: Q8TAV4
  protein_description: 'RecName: Full=Stomatin-like protein 3; Short=SLP-3;'
  gene_info: Name=STOML3;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the band 7/mec-2 family. .
  protein_domains: Band-7_stomatin-like. (IPR043202); Band_7. (IPR001107); Band_7/SPFH_dom_sf.
    (IPR036013); Band_7/stomatin-like_CS. (IPR018080); Stomatin_HflK_fam. (IPR001972)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 16
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q8TAV4
- **Protein Description:** RecName: Full=Stomatin-like protein 3; Short=SLP-3;
- **Gene Information:** Name=STOML3;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the band 7/mec-2 family. .
- **Key Domains:** Band-7_stomatin-like. (IPR043202); Band_7. (IPR001107); Band_7/SPFH_dom_sf. (IPR036013); Band_7/stomatin-like_CS. (IPR018080); Stomatin_HflK_fam. (IPR001972)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "STOML3" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'STOML3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **STOML3** (gene ID: STOML3, UniProt: Q8TAV4) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# STOML3 (Stomatin-like Protein 3): A Comprehensive Research Report

## 1. Introduction and Summary

Stomatin-like protein 3 (STOML3, also known as SLP3 or SRO) is a membrane-associated scaffolding protein that plays essential roles in sensory transduction, particularly in mechanosensation and, more recently discovered, in olfaction. STOML3 belongs to the highly conserved stomatin/prohibitin/flotillin/HflK (SPFH) domain protein family, which is characterized by a structurally conserved core domain of approximately 120 amino acids called the stomatin domain [lapatsina-2011-stomatin-review-abstract]. The protein was first identified in mouse olfactory epithelium in 2002 and was subsequently demonstrated to be essential for touch sensation in mammals through its ability to modulate the activity of mechanosensitive ion channels [wetzel-2006-stoml3-touch-abstract].

STOML3 functions as a membrane-bound scaffolding protein that sensitizes mechanically gated ion channels, including the Piezo family of mechanosensitive channels (Piezo1 and Piezo2), to detect molecular-scale displacements as small as ~13 nanometers [poole-2014-piezo-stoml3-summary]. This remarkable sensitivity is achieved through STOML3's ability to bind cholesterol and stiffen the plasma membrane, thereby facilitating efficient force transfer to the associated ion channels [qi-2015-cholesterol-stoml3-summary]. The protein forms oligomeric complexes and localizes to cholesterol-rich lipid rafts and mobile vesicle pools within sensory neurons.

The importance of STOML3 for mammalian mechanosensation was established through studies demonstrating that approximately 35% of skin mechanoreceptors fail to respond to mechanical stimuli in STOML3 knockout mice [wetzel-2006-stoml3-touch-abstract]. Furthermore, STOML3 has emerged as a therapeutic target for chronic pain, as small-molecule inhibitors of STOML3 oligomerization can reverse mechanical hypersensitivity in neuropathic pain models [wetzel-2016-stoml3-inhibitors-abstract].

## 2. Gene and Protein Structure

### 2.1 Gene Information

The human STOML3 gene is located on chromosome 13 (13q13.3) and encodes a protein of 287 amino acids with a calculated molecular weight of approximately 32 kDa (UniProt: Q8TAV4). The protein belongs to the band 7/mec-2 family, which includes other stomatin-related proteins such as stomatin, STOML1, STOML2, and podocin [lapatsina-2011-stomatin-review-abstract].

### 2.2 Domain Architecture

STOML3 contains several characteristic structural features:

The **Band-7/stomatin domain** (IPR001107, IPR043202) forms the core of the protein and is highly conserved across species, from bacteria to humans. This domain mediates oligomerization and is essential for STOML3 function in modulating ion channel activity [lapatsina-2011-stomatin-review-abstract]. Structure-function experiments have demonstrated that the stomatin domain is specifically required for STOML3's ability to sensitize Piezo channels, with higher-order scaffolds being a prerequisite for function [poole-2014-piezo-stoml3-summary].

A **hydrophobic membrane insertion region** near the N-terminus anchors STOML3 to the plasma membrane. This region contains a critical proline residue at position 40 (P40) that is highly conserved among stomatin family members and is essential for the protein's association with cholesterol-rich lipid rafts [qi-2015-cholesterol-stoml3-summary]. The P40 residue is essential for the hairpin-loop membrane topology; mutation of this proline to serine (P40S) converts STOML3 to a single-pass transmembrane form that cannot associate with cholesterol or modulate mechanosensitive channels [qi-2015-cholesterol-stoml3-summary].

The **N-terminal hydrophobic region** is required for vesicular localization of STOML3 and regulates its physical and functional interaction with acid-sensing ion channels (ASICs) [lapatsina-2012-asic-vesicle-summary].

## 3. Primary Molecular Function

STOML3 functions as a membrane scaffolding protein that sensitizes mechanically gated ion channels to detect mechanical stimuli. The protein does not itself form ion channels but rather modulates the activity of existing mechanosensitive channels through several interconnected mechanisms.

### 3.1 Sensitization of Piezo Channels

The most well-characterized function of STOML3 is its ability to sensitize Piezo1 and Piezo2 mechanosensitive ion channels. According to PubMed, Poole et al. (2014) demonstrated that STOML3 brings the activation threshold for Piezo channels down to approximately 10 nanometers, a roughly 10-fold sensitization compared to channels lacking STOML3 [DOI: 10.1038/ncomms4520] [poole-2014-piezo-stoml3-summary]. This sensitization is specific to STOML3 among stomatin-domain proteins tested; stomatin, STOML1, and STOML2 were not able to achieve similar effects.

The sensitization mechanism involves STOML3's ability to form oligomeric scaffolds. Disruption of STOML3 oligomerization with small-molecule inhibitors reversibly reduces the sensitivity of mechanically gated currents in sensory neurons [wetzel-2016-stoml3-inhibitors-abstract].

### 3.2 Membrane Stiffening via Cholesterol Recruitment

A major mechanistic insight came from the work of Qi et al. (2015), which demonstrated that STOML3 controls membrane mechanics by binding cholesterol and forming stiffened membrane microdomains [DOI: 10.1038/ncomms9512] [qi-2015-cholesterol-stoml3-summary]. Using atomic force spectroscopy (AFS), the authors showed that:

- STOML3 knockout sensory neurons have softer membranes compared to wild-type
- STOML3-deficient neurons have lower membrane tension
- STOML3-deficient neurons have increased membrane viscosity

This stiffened membrane facilitates force transfer to mechanosensitive channels. The model proposes that cholesterol recruited by STOML3 creates a specialized membrane platform that redirects, rescales, and confines mechanical force, making it available to gate associated ion channels [qi-2015-cholesterol-stoml3-summary].

### 3.3 Modulation of ASIC Channels

STOML3 also interacts with and modulates acid-sensing ion channels (ASICs). According to PubMed, Lapatsina et al. (2012) demonstrated that STOML3 interacts with stomatin and ASIC subunits, and that this interaction occurs in a highly mobile vesicle pool in dorsal root ganglia neurons [DOI: 10.1098/rsob.120096] [lapatsina-2012-asic-vesicle-summary]. STOML3 suppresses the magnitude and modulates the inactivation kinetics of proton-gated currents carried by recombinant ASICs.

Studies using double knockout mice have revealed complex interactions between stomatin-domain proteins and ASICs. According to PubMed, Moshourab et al. (2013) found that the loss of STOML3 in ASIC3 knockout mice markedly exacerbates deficits in the mechanosensitivity of nociceptors [DOI: 10.1113/jphysiol.2013.261180] [moshourab-2013-asic-interaction-summary], demonstrating functional cooperation between these proteins.

## 4. Subcellular Localization

STOML3 exhibits specific subcellular localization patterns that are critical for its function in sensory transduction.

### 4.1 Plasma Membrane and Lipid Rafts

STOML3 is enriched in cholesterol-rich membrane fractions, as demonstrated by sucrose-density-gradient centrifugation experiments [qi-2015-cholesterol-stoml3-summary]. In sensory neurons, STOML3 displays a punctate pattern in neurites, consistent with localization to discrete membrane microdomains [poole-2014-piezo-stoml3-fulltext].

The association with lipid rafts is dependent on the conserved proline residue at position 40. The P40S mutant is mainly detected in non-raft fractions and displays uniform distribution rather than the punctate pattern seen with wild-type STOML3 [qi-2015-cholesterol-stoml3-summary].

### 4.2 Mobile Vesicle Pool

A significant fraction of STOML3 localizes to a highly mobile vesicle pool in DRG neurons [lapatsina-2012-asic-vesicle-summary]. These vesicles are:

- Rab11-positive (indicating recycling endosomes)
- Not part of early-endosomal, lysosomal, or Rab14-dependent biosynthetic compartments
- Microtubule-dependent for their movement

The authors proposed that this vesicular pool may represent a "transducosome" – a mobile compartment containing molecules critical for sensory transduction. Disruption of microtubule dynamics leads to incorporation of STOML3 into the plasma membrane and increased acid-gated currents, suggesting that trafficking between vesicular and plasma membrane pools is physiologically regulated [lapatsina-2012-asic-vesicle-summary].

### 4.3 Olfactory Cilia

In olfactory sensory neurons (OSNs), STOML3 is predominantly localized to the dendritic knob and proximal portions of olfactory cilia, the site of olfactory transduction [agostinelli-2021-olfaction-summary]. This localization places STOML3 in proximity to key olfactory transduction components including adenylyl cyclase III (ACIII), which has been shown to physically interact with STOML3.

## 5. Biological Processes and Pathways

### 5.1 Touch Sensation and Mechanotransduction

STOML3 is essential for normal touch sensation in mammals. The seminal 2006 study by Wetzel et al. demonstrated that approximately 35% of skin mechanoreceptors do not respond to mechanical stimuli in STOML3 knockout mice [DOI: 10.1038/nature05394] [wetzel-2006-stoml3-touch-abstract]. Both rapidly adapting (RA) and slowly adapting (SA) mechanoreceptors are affected, although the proportion of affected fibers varies by type.

STOML3 appears to function downstream of channel gating, as evidenced by the finding that cholesterol depletion affects both RA channels (which require a protein tether) and SA channels (which are thought to be directly stretch-activated). This suggests STOML3 modulates mechanosensitivity through a general mechanism involving membrane mechanics rather than through direct effects on channel gating [qi-2015-cholesterol-stoml3-fulltext].

The mechanistic pathway involves:
1. STOML3 binding to cholesterol to form stiffened membrane platforms
2. Efficient force transfer from the extracellular matrix to membrane-embedded channels
3. Lowered activation threshold of mechanosensitive channels (Piezo1, Piezo2)
4. Generation of receptor potentials leading to action potential firing

### 5.2 Pain and Nociception

STOML3 plays important roles in both normal and pathological pain processing. In knockout mice, tactile-driven behaviors are impaired, including touch-evoked pain caused by neuropathic injury [wetzel-2006-stoml3-touch-abstract].

The interactions between STOML3 and ASICs are particularly important for nociceptor function. According to PubMed, double knockout studies revealed that loss of stomatin or STOML3 in ASIC knockout mice markedly exacerbates deficits in the mechanosensitivity of A∂- and C-fiber nociceptors without affecting mechanoreceptor function [moshourab-2013-asic-interaction-summary]. This suggests that STOML3-ASIC interactions are particularly important for mechanical pain sensing.

Importantly, STOML3 has been validated as a therapeutic target for chronic pain. According to PubMed, Wetzel et al. (2016) identified small-molecule inhibitors of STOML3 oligomerization (such as OB-1) that reversibly reduce the sensitivity of mechanically gated currents in sensory neurons and silence mechanoreceptors in vivo [DOI: 10.1038/nn.4454] [wetzel-2016-stoml3-inhibitors-abstract]. These inhibitors can reverse mechanical hypersensitivity in models of neuropathic pain and diabetic neuropathy, demonstrating that peripheral targeting of STOML3 represents a viable pain treatment strategy.

### 5.3 Olfaction

Recent studies have revealed an unexpected role for STOML3 in olfactory transduction. According to PubMed, Agostinelli et al. (2021) showed that STOML3 knockout mice have altered spontaneous firing patterns in OSNs, with lower mean firing frequency and shifted interspike interval distributions [DOI: 10.1523/ENEURO.0565-20.2021] [agostinelli-2021-olfaction-summary]. Furthermore, evoked responses to odorants and IBMX (a phosphodiesterase inhibitor used to mimic odorant stimulation) showed reduced spike numbers and shorter response durations.

According to PubMed, Liang et al. (2023) extended these findings by generating STOML3 knockout mice and performing behavioral tests [DOI: 10.1523/ENEURO.0457-22.2023] [liang-2023-olfaction-behavior-summary]. They found that:

- STOML3 is not required for basic odor detection
- STOML3 knockout mice can detect attractive odors normally
- STOML3 is required for efficient odor discrimination
- STOML3 knockout mice fail to distinguish between familiar and novel odors

This conserved role in olfaction is also present in C. elegans, where the STOML3 homolog mec-2 is required for olfactory behavior. The conservation across species suggests a fundamental role for stomatin-domain proteins in sensory neuron function beyond mechanotransduction [liang-2023-olfaction-behavior-summary].

### 5.4 Proprioception

Recent work has also implicated STOML3 in proprioception and nerve regeneration. According to PubMed, Haseleu et al. (2025) demonstrated that STOML3 is required for functional plasticity following peripheral nerve regeneration [DOI: 10.1113/EP092428]. In cross-anastomosis experiments where muscle afferents were redirected to innervate skin, wild-type muscle afferents could form functional mechanosensitive receptive fields appropriate for the new target. However, in STOML3 knockout mice, muscle afferents largely failed to form functional mechanosensitive receptive fields despite making anatomically appropriate endings in the skin.

## 6. Evolutionary Conservation

STOML3 is the mammalian homolog of MEC-2, a protein essential for touch sensation in the nematode Caenorhabditis elegans. According to PubMed, Huang et al. (1995) first identified MEC-2 as a stomatin-like protein required for the function of touch receptor neurons in C. elegans [DOI: 10.1038/378292a0] [huang-1995-mec2-abstract]. MEC-2 mutants are touch-insensitive despite having morphologically normal touch cells.

According to PubMed, Goodman et al. (2002) demonstrated that MEC-2 regulates the MEC-4/MEC-10 DEG/ENaC channels, increasing their activity approximately 40-fold [DOI: 10.1038/4151039a] [goodman-2002-mec2-abstract]. This functional paradigm of stomatin-domain proteins regulating mechanosensitive channels has been conserved from worms to mammals.

The high degree of conservation in the stomatin domain (50% identity between bacterial and human homologs) suggests that stomatin-family proteins have a unifying cellular function that has been preserved throughout evolution [lapatsina-2011-stomatin-review-abstract]. In both C. elegans and mammals:

- Stomatin-domain proteins associate with membranes
- They form oligomeric complexes
- They modulate ion channel activity
- They are essential for mechanosensation and olfaction

## 7. Clinical and Therapeutic Relevance

### 7.1 Pain Therapy

The most developed therapeutic application of STOML3 research is in pain treatment. Since STOML3 is required for normal mechanoreceptor sensitivity, inhibiting its function can reduce mechanical hypersensitivity in pathological pain states.

According to PubMed, the OB-1 inhibitor and related compounds that disrupt STOML3 oligomerization can:
- Reversibly reduce mechanically gated currents in sensory neurons
- Silence mechanoreceptors in vivo
- Attenuate fine touch perception in normal mice (reversibly)
- Reverse mechanical allodynia following nerve injury
- Reverse mechanical hypersensitivity in diabetic neuropathy models [wetzel-2016-stoml3-inhibitors-abstract]

The advantage of targeting STOML3 for pain therapy is that it acts peripherally in the skin, potentially avoiding central nervous system side effects. Additionally, the effect is reversible, providing a safety margin.

### 7.2 Disease Associations

STOML3 gene amplification has been observed in some cancers. According to PubMed, Nagaishi et al. (2012) found that amplification of the STOML3 gene (along with FREM2 and LHFP) is associated with mesenchymal differentiation in gliosarcoma [DOI: 10.1016/j.ajpath.2012.01.027]. STOML3 amplification was found in 22% of mesenchymal tumor areas but not in glial tumor areas.

STOML3 has also been implicated in Bardet-Biedl syndrome (BBS), a ciliopathy characterized by multiple systemic abnormalities. According to PubMed, Tan et al. (2007) found that ablation of BBS1 and BBS4 leads to defective trafficking of STOML3 in sensory neurons, with concomitant defects in peripheral thermosensation and mechanosensation [DOI: 10.1073/pnas.0706618104].

## 8. Open Questions

Several important questions about STOML3 function remain to be addressed:

1. **Structural basis of function:** While the stomatin domain is known to be essential for STOML3 function, detailed structural information about STOML3 oligomers and their interaction with Piezo channels is lacking. Cryo-EM or crystallographic studies of STOML3-channel complexes would provide mechanistic insights.

2. **Specificity determinants:** Why does STOML3, but not other stomatin-domain proteins, sensitize Piezo channels? What molecular features determine the specificity of stomatin-channel interactions?

3. **Dual sensory roles:** How does STOML3 function in both mechanosensation and olfaction? Does it interact with different channel partners in different sensory neurons, or does it modulate membrane properties in a channel-independent manner?

4. **Vesicle trafficking regulation:** What signals control STOML3 trafficking between the vesicular pool and the plasma membrane? Is this trafficking physiologically regulated in response to sensory stimuli?

5. **Therapeutic development:** Can more potent and selective STOML3 inhibitors be developed for clinical pain therapy? What are the potential side effects of chronic STOML3 inhibition on touch sensation and other functions?

6. **STOML3 in other tissues:** STOML3 expression appears restricted to sensory neurons, but are there additional tissues where it plays functional roles?

7. **Isoform-specific functions:** In C. elegans, different mec-2 isoforms have distinct functions in mechanosensation versus olfaction. Do human STOML3 splice variants have similar functional specificity?

## 9. References

1. **agostinelli-2021-olfaction:** Agostinelli E, Gonzalez-Velandia KY, Hernandez-Clavijo A, Kumar Maurya D, Xerxa E, Lewin GR, Dibattista M, Menini A, Pifferi S. A Role for STOML3 in Olfactory Sensory Transduction. eNeuro. 2021 Mar 12;8(2):ENEURO.0565-20.2021. DOI: [10.1523/ENEURO.0565-20.2021](https://doi.org/10.1523/ENEURO.0565-20.2021). PMID: 33637538; PMCID: PMC7986538.

2. **goodman-2002-mec2:** Goodman MB, Ernstrom GG, Chelur DS, O'Hagan R, Yao CA, Chalfie M. MEC-2 regulates C. elegans DEG/ENaC channels needed for mechanosensation. Nature. 2002 Feb 28;415(6875):1039-42. DOI: [10.1038/4151039a](https://doi.org/10.1038/4151039a). PMID: 11875573.

3. **huang-1995-mec2:** Huang M, Gu G, Ferguson EL, Chalfie M. A stomatin-like protein necessary for mechanosensation in C. elegans. Nature. 1995 Nov 16;378(6554):292-5. DOI: [10.1038/378292a0](https://doi.org/10.1038/378292a0). PMID: 7477350.

4. **lapatsina-2011-stomatin-review:** Lapatsina L, Brand J, Poole K, Daumke O, Lewin GR. Stomatin-domain proteins. Eur J Cell Biol. 2012 Apr;91(4):240-5. DOI: [10.1016/j.ejcb.2011.01.018](https://doi.org/10.1016/j.ejcb.2011.01.018). PMID: 21501885.

5. **lapatsina-2012-asic-vesicle:** Lapatsina L, Jira JA, Smith ES, Poole K, Kozlenkov A, Bilbao D, Lewin GR, Heppenstall PA. Regulation of ASIC channels by a stomatin/STOML3 complex located in a mobile vesicle pool in sensory neurons. Open Biol. 2012 Jun;2(6):120096. DOI: [10.1098/rsob.120096](https://doi.org/10.1098/rsob.120096). PMID: 22773952; PMCID: PMC3390797.

6. **liang-2023-olfaction-behavior:** Liang X, Taylor M, Napier-Jameson R, Calovich-Benne C, Norris A. A Conserved Role for Stomatin Domain Genes in Olfactory Behavior. eNeuro. 2023 Mar 22;10(3):ENEURO.0457-22.2023. DOI: [10.1523/ENEURO.0457-22.2023](https://doi.org/10.1523/ENEURO.0457-22.2023). PMID: 36858824; PMCID: PMC10035767.

7. **moshourab-2013-asic-interaction:** Moshourab RA, Wetzel C, Martinez-Salgado C, Lewin GR. Stomatin-domain protein interactions with acid-sensing ion channels modulate nociceptor mechanosensitivity. J Physiol. 2013 Nov 15;591(22):5555-74. DOI: [10.1113/jphysiol.2013.261180](https://doi.org/10.1113/jphysiol.2013.261180). PMID: 23959680; PMCID: PMC3853495.

8. **poole-2014-matrix-review:** Poole K, Moroni M, Lewin GR. Sensory mechanotransduction at membrane-matrix interfaces. Pflugers Arch. 2015 Jan;467(1):121-32. DOI: [10.1007/s00424-014-1563-6](https://doi.org/10.1007/s00424-014-1563-6). PMID: 24981693; PMCID: PMC4281363.

9. **poole-2014-piezo-stoml3:** Poole K, Herget R, Lapatsina L, Ngo HD, Lewin GR. Tuning Piezo ion channels to detect molecular-scale movements relevant for fine touch. Nat Commun. 2014 Mar 24;5:3520. DOI: [10.1038/ncomms4520](https://doi.org/10.1038/ncomms4520). PMID: 24662763; PMCID: PMC3973071.

10. **qi-2015-cholesterol-stoml3:** Qi Y, Andolfi L, Frattini F, Mayer F, Lazzarino M, Hu J. Membrane stiffening by STOML3 facilitates mechanosensation in sensory neurons. Nat Commun. 2015 Oct 7;6:8512. DOI: [10.1038/ncomms9512](https://doi.org/10.1038/ncomms9512). PMID: 26443885; PMCID: PMC4633829.

11. **wetzel-2006-stoml3-touch:** Wetzel C, Hu J, Riethmacher D, Benckendorff A, Harder L, Eilers A, Moshourab R, Kozlenkov A, Labuz D, Caspani O, Erdmann B, Machelska H, Heppenstall PA, Lewin GR. A stomatin-domain protein essential for touch sensation in the mouse. Nature. 2006 Dec 14;445(7124):206-9. DOI: [10.1038/nature05394](https://doi.org/10.1038/nature05394). PMID: 17167420.

12. **wetzel-2016-stoml3-inhibitors:** Wetzel C, Pifferi S, Picci C, Gök C, Hoffmann D, Bali KK, Lampe A, Lapatsina L, Fleischer R, Smith ESJ, Bégay V, Moroni M, Estebanez L, Kühnemund J, Walcher J, Specker E, Neuenschwander M, von Kries JP, Haucke V, Kuner R, Poulet JFA, Schmoranzer J, Poole K, Lewin GR. Small-molecule inhibition of STOML3 oligomerization reverses pathological mechanical hypersensitivity. Nat Neurosci. 2017 Feb;20(2):209-218. DOI: [10.1038/nn.4454](https://doi.org/10.1038/nn.4454). PMID: 27941788.


## Citations

1. agostinelli-2021-olfaction-summary.md
2. goodman-2002-mec2-abstract.md
3. huang-1995-mec2-abstract.md
4. lapatsina-2011-stomatin-review-abstract.md
5. lapatsina-2012-asic-vesicle-fulltext.txt
6. lapatsina-2012-asic-vesicle-summary.md
7. liang-2023-olfaction-behavior-summary.md
8. moshourab-2013-asic-interaction-fulltext.txt
9. moshourab-2013-asic-interaction-summary.md
10. poole-2014-matrix-review-abstract.md
11. poole-2014-piezo-stoml3-fulltext.txt
12. poole-2014-piezo-stoml3-summary.md
13. qi-2015-cholesterol-stoml3-fulltext.txt
14. qi-2015-cholesterol-stoml3-summary.md
15. wetzel-2006-stoml3-touch-abstract.md
16. wetzel-2016-stoml3-inhibitors-abstract.md