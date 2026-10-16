---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-27T15:56:37.136526'
end_time: '2026-09-27T16:05:28.689326'
duration_seconds: 531.55
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: worm
  gene_id: cat-1
  gene_symbol: cat-1
  uniprot_accession: Q9GNP0
  protein_description: 'SubName: Full=Major facilitator superfamily (MFS) profile
    domain-containing protein {ECO:0000313|EMBL:CCD68669.1};'
  gene_info: Name=cat-1 {ECO:0000313|EMBL:CCD68669.1, ECO:0000313|WormBase:W01C8.6};
    ORFNames=CELE_W01C8.6 {ECO:0000313|EMBL:CCD68669.1}, W01C8.6 {ECO:0000313|WormBase:W01C8.6};
  organism_full: Caenorhabditis elegans.
  protein_family: Not specified in UniProt
  protein_domains: MFS. (IPR011701); MFS_dom. (IPR020846); MFS_trans_sf. (IPR036259);
    MFS_Vesicular_Transporter. (IPR050930); MFS_1 (PF07690)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 41
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: cat-1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9GNP0
- **Protein Description:** SubName: Full=Major facilitator superfamily (MFS) profile domain-containing protein {ECO:0000313|EMBL:CCD68669.1};
- **Gene Information:** Name=cat-1 {ECO:0000313|EMBL:CCD68669.1, ECO:0000313|WormBase:W01C8.6}; ORFNames=CELE_W01C8.6 {ECO:0000313|EMBL:CCD68669.1}, W01C8.6 {ECO:0000313|WormBase:W01C8.6};
- **Organism (full):** Caenorhabditis elegans.
- **Protein Family:** Not specified in UniProt
- **Key Domains:** MFS. (IPR011701); MFS_dom. (IPR020846); MFS_trans_sf. (IPR036259); MFS_Vesicular_Transporter. (IPR050930); MFS_1 (PF07690)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "cat-1" matches the protein description above**
2. **Verify the organism is correct:** Caenorhabditis elegans.
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'cat-1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **cat-1** (gene ID: cat-1, UniProt: Q9GNP0) in worm.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9GNP0
- **Protein Description:** SubName: Full=Major facilitator superfamily (MFS) profile domain-containing protein {ECO:0000313|EMBL:CCD68669.1};
- **Gene Information:** Name=cat-1 {ECO:0000313|EMBL:CCD68669.1, ECO:0000313|WormBase:W01C8.6}; ORFNames=CELE_W01C8.6 {ECO:0000313|EMBL:CCD68669.1}, W01C8.6 {ECO:0000313|WormBase:W01C8.6};
- **Organism (full):** Caenorhabditis elegans.
- **Protein Family:** Not specified in UniProt
- **Key Domains:** MFS. (IPR011701); MFS_dom. (IPR020846); MFS_trans_sf. (IPR036259); MFS_Vesicular_Transporter. (IPR050930); MFS_1 (PF07690)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "cat-1" matches the protein description above**
2. **Verify the organism is correct:** Caenorhabditis elegans.
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'cat-1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **cat-1** (gene ID: cat-1, UniProt: Q9GNP0) in worm.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Caenorhabditis elegans cat-1* / CAT-1

## Executive conclusion

The requested target is correctly identified as *C. elegans cat-1*, locus **W01C8.6**, corresponding to the supplied UniProt accession **Q9GNP0**. The experimentally established product is **CAT-1, the sole canonical vesicular monoamine transporter (VMAT) of the worm**. Its primary function is to import cytosolic monoamines—most clearly dopamine and serotonin—into neuronal secretory/synaptic vesicles, thereby enabling vesicular storage and regulated release. CAT-1 is not a plasma-membrane dopamine-reuptake transporter and is not an enzyme.

Confidence is high for transporter identity, broad substrate specificity, vesicular localization, and physiological necessity. The detailed amine/H⁺ exchange cycle and approximately 2H⁺:1 amine stoichiometry are well-supported properties of conserved SLC18 transporters but have not been measured directly for purified CAT-1.

## 1. Mandatory identity verification and ambiguity control

The foundational molecular study characterized *C. elegans cat-1* as encoding a **553-amino-acid protein with 12 predicted transmembrane segments**, 47% identical to human VMAT1 and 49% identical to human VMAT2. Expression in heterologous cells conferred dopamine and serotonin transport, while *cat-1* mutations eliminated or impaired the corresponding protein and monoamine-dependent functions. This firmly aligns W01C8.6/Q9GNP0 with a vesicular monoamine transporter rather than merely an uncharacterized generic MFS protein. The supplied InterPro/Pfam assignments—MFS, MFS transporter superfamily, and vesicular-transporter-related profiles—are therefore fully concordant with experimental literature. (duerr1999thecat1gene pages 3-3, duerr1999thecat1gene pages 6-8)

The symbol is nevertheless hazardous in broad searches. In other contexts, “CAT-1” can denote catalase, a cationic amino-acid transporter, or unrelated genes. Moreover, ***rcat-1*** in *C. elegans* is a distinct gene, formerly R02D3.7, encoding a transcriptional regulator of *cat-1* and *cat-2*; it is not CAT-1/VMAT itself. Literature concerning those entities was not used as evidence for the molecular function of Q9GNP0. (jeong2022deficiencyinrcat1 pages 1-2, jeong2022deficiencyinrcat1 pages 8-10)

A compact evidence summary follows.

| Question / feature | Best-supported annotation | Evidence type | Key quantitative detail | Source / date / DOI URL |
|---|---|---|---|---|
| Identity and topology | *C. elegans cat-1* (W01C8.6; Q9GNP0) encodes the worm vesicular monoamine transporter (CAT-1/VMAT), a 553-aa protein with a predicted 12-transmembrane MFS/SLC18-like architecture. | Direct cloning, sequence analysis, and functional expression; topology predicted rather than experimentally mapped | 47% amino-acid identity to human VMAT1 and 49% to VMAT2 | Duerr et al., January 1999, [DOI](https://doi.org/10.1523/JNEUROSCI.19-01-00072.1999) (duerr1999thecat1gene pages 3-3) |
| Subcellular and cellular localization | CAT-1 is associated with synaptic vesicles in monoaminergic neurons; immunoreactivity occurs in neuronal processes and somata, including ADF, RIH, ADE/PDE/CEP, NSM, AIM, RIC, CAN, and developmentally in VC4/VC5. Vesicle association is supported by altered localization in *unc-104* mutants. | Direct CAT-1 immunofluorescence and vesicle-trafficking genetics | Strong reproducible staining in 20 neurons, with weak or variable staining in five more | Duerr et al., January 1999, [DOI](https://doi.org/10.1523/JNEUROSCI.19-01-00072.1999) (duerr1999thecat1gene pages 6-8, duerr1999thecat1gene pages 5-6) |
| Physiological substrates | CAT-1 directly transports dopamine and serotonin and recognizes tyramine, norepinephrine, octopamine, and histamine. These data support broad vesicular biogenic-amine specificity rather than dopamine selectivity. | Direct uptake and competition assays in permeabilized CAT-1-expressing CV-1 cells | Competitor EC50 values for serotonin uptake (mM): dopamine 0.07, tyramine 0.06, serotonin 0.91, norepinephrine 2.8, octopamine 3.4, histamine 120; for dopamine uptake: 0.04, 0.04, 0.51, 1.7, 1.5, and 117, respectively | Duerr et al., January 1999, [DOI](https://doi.org/10.1523/JNEUROSCI.19-01-00072.1999) (duerr1999thecat1gene pages 6-8) |
| Pharmacology and energetic dependence | CAT-1-mediated uptake is inhibited by the canonical VMAT inhibitors reserpine and tetrabenazine and by the protonophore FCCP, supporting dependence on a proton electrochemical gradient. | Direct CAT-1 transport assay | Dopamine uptake was inhibited by 100 nM reserpine, 1 mM tetrabenazine, and 5 mM FCCP; these are assay concentrations, not reported CAT-1 Ki values | Duerr et al., January 1999, [DOI](https://doi.org/10.1523/JNEUROSCI.19-01-00072.1999) (duerr1999thecat1gene pages 5-6) |
| Molecular mechanism | The best-supported model is vesicular amine/H+ antiport: V-type ATPase acidifies the vesicle, and CAT-1 uses the resulting proton gradient to concentrate cytosolic monoamines for regulated exocytotic release. A 2 H+:1 amine stoichiometry is plausible but has not been measured directly for CAT-1. | Proton dependence supported directly for CAT-1; antiport stoichiometry and detailed cycle inferred from conserved SLC18/MFS biology | Conserved-family model exchanges approximately two lumenal protons per accumulated amine | Eiden et al., February 2004, [DOI](https://doi.org/10.1007/s00424-003-1100-5); Lawal & Krantz, April 2013, [DOI](https://doi.org/10.1016/j.mam.2012.07.005) (eiden2004thevesicularamine pages 3-4, lawal2013slc18vesicularneurotransmitter pages 1-2, eiden2004thevesicularamine pages 1-3) |
| Loss-of-function phenotypes and rescue | CAT-1 is required for normal vesicular monoamine signaling, including food-associated slowing/grazing, pharyngeal pumping, egg laying, and male mating. Worm CAT-1 genomic constructs rescue mutants; human VMAT1 or VMAT2 can partially substitute, supporting functional orthology. | Direct mutant, transgenic-rescue, and behavioral experiments | Pharyngeal pumping: wild type 275/min, *cat-1* 160/min, human VMAT1 rescue 202/min, human VMAT2 rescue 208/min; fewer than half of mutant males mated successfully | Duerr et al., January 1999, [DOI](https://doi.org/10.1523/JNEUROSCI.19-01-00072.1999) (duerr1999thecat1gene pages 9-11, duerr1999thecat1gene pages 3-3) |
| 2024 neurotransmitter-atlas update | CRISPR knock-in reporters and NeuroPAL support CAT-1 as a marker of vesicular monoamine use across serotonin, dopamine, tyramine, and octopamine systems, while identifying additional sex-specific, glial, and non-neural expression. Monoamine staining alone is insufficient: AIM can take up serotonin through MOD-5 but lacks CAT-1 and therefore is not established as a conventional vesicular serotonergic neuron. | Direct endogenous-locus reporter mapping plus pathway-based interpretation | The male nervous system contains almost 30% more neurons than the hermaphrodite; exact CAT-1-positive cell totals were not provided in the retrieved evidence | Wang et al., October 2024, [DOI](https://doi.org/10.7554/eLife.95402.3) (wang2024aneurotransmitteratlas pages 37-38, wang2024aneurotransmitteratlas pages 3-5) |
| Human disease-model application | A *cat-1*-null background has been used to express human SLC18A2/VMAT2 and disease variants P237H and P387L, modeling brain dopamine–serotonin vesicular transport disease. Mutant human proteins impaired monoamine-dependent grazing and pharyngeal pumping relative to wild-type human VMAT2. | Direct transgenic disease modeling; interpretation limited by heterologous expression pattern | Three MosSCI-integrated lines expressed wild-type, P237H, or P387L human VMAT2; serotonin rescued the pumping phenotype in preliminary experiments | Young et al., first posted September 28, 2018, [DOI](https://doi.org/10.1242/dmm.035709) (young2018modellingbraindopamineserotonin pages 3-5, young2018modellingbraindopamineserotonin pages 1-3) |
| Neurotoxicology and metabolomics application | The null-like *cat-1(ok411)* deletion models deficient vesicular monoamine sequestration and increases dopaminergic-neuron vulnerability to MPP+. It also alters tyrosine and broader metabolic pathways without causing a general swimming defect. | Direct CAT-1 loss-of-function, toxicant exposure, imaging, behavior, and untargeted metabolomics | No detectable CAT-1 protein; strain-by-MPP+ interaction p<0.001 (total n=587); 114 mutant-associated and 199 MPP+-associated features at p<0.05, with 14 overlapping | Bradner et al., online February 4, 2021, [journal DOI](https://doi.org/10.1093/toxsci/kfab011); [preprint DOI](https://doi.org/10.1101/2020.10.02.324095) (bradner2021geneticortoxicant pages 1-2, bradner2021geneticortoxicant pages 6-7, bradner2021geneticortoxicant pages 4-6) |
| Major uncertainty | CAT-1’s transporter identity, vesicular localization, and broad monoamine specificity are strong; however, no CAT-1 structure, direct proton/amine stoichiometry, absolute vesicular affinities for all candidate substrates, or complete endogenous cell-by-cell release map was found. Competition EC50 values should not be treated as Km or Ki values, and CAT-1 expression alone does not identify which monoamine a cell synthesizes. | Evidence-gap assessment; conserved-family inference must remain distinct from direct CAT-1 measurement | The foundational study reported predicted—not structurally determined—12-TM topology; modern atlas assignments require co-expression with biosynthetic enzymes | Duerr et al., January 1999, [DOI](https://doi.org/10.1523/JNEUROSCI.19-01-00072.1999); Wang et al., October 2024, [DOI](https://doi.org/10.7554/eLife.95402.3) (duerr1999thecat1gene pages 3-3, wang2024aneurotransmitteratlas pages 3-5, lawal2013slc18vesicularneurotransmitter pages 7-8) |


*Table: Compact evidence matrix separating direct experiments on C. elegans CAT-1/Q9GNP0 from mechanism inferred through conserved SLC18/VMAT biology. It summarizes molecular function, localization, quantitative findings, current applications, and principal uncertainties.*

## 2. Primary molecular function

### 2.1 Transported substrates

Direct uptake experiments in digitonin-permeabilized CV-1 cells expressing worm CAT-1 demonstrated time-dependent, saturable transport of radiolabeled **dopamine** and **serotonin**. Uptake was absent from vector controls and was inhibited by excess unlabeled monoamines, establishing CAT-1 as a broad-specificity biogenic-amine transporter. (duerr1999thecat1gene pages 3-3, duerr1999thecat1gene pages 5-6)

Competition assays showed recognition of dopamine, serotonin, tyramine, norepinephrine, octopamine, and histamine. For inhibition of serotonin uptake, reported EC50 values were 0.07 mM dopamine, 0.06 mM tyramine, 0.91 mM serotonin, 2.8 mM norepinephrine, 3.4 mM octopamine, and 120 mM histamine. Corresponding values against dopamine uptake were 0.04, 0.04, 0.51, 1.7, 1.5, and 117 mM. These are competition EC50 values—not substrate Km or binding Ki values—and should not be interpreted as absolute transport affinities. (duerr1999thecat1gene pages 6-8)

The most defensible physiological substrates are therefore:

* **Dopamine and serotonin:** directly transported and strongly supported in vivo.
* **Tyramine and octopamine:** strongly plausible physiological substrates because they compete effectively and CAT-1 is expressed in the relevant monoaminergic cells.
* **Norepinephrine and histamine:** transported/recognized in vitro, but neither is established as a conventional endogenous worm neurotransmitter; histamine recognition mainly supports CAT-1’s VMAT2-like pharmacological profile. The 2023 comparative review likewise notes that histamine is not considered a native *C. elegans* neurotransmitter. (duerr1999thecat1gene pages 6-8, rosikon2023regulationandmodulation pages 16-17)

### 2.2 Mechanism and protein family

SLC18 vesicular transporters are members of the **Drug:H⁺ Antiporter-1 branch of the Major Facilitator Superfamily**. In the accepted model, vesicular V-type ATPase pumps protons into the vesicle, generating an acidic lumen and electrochemical gradient. VMAT then exchanges lumenal protons for cytosolic monoamine, concentrating transmitter inside the vesicle for subsequent regulated exocytosis. Conserved-family analyses commonly give an approximate stoichiometry of **two protons exchanged per accumulated amine**. (eiden2004thevesicularamine pages 3-4, lawal2013slc18vesicularneurotransmitter pages 1-2, fei2009vesicularneurotransmittertransporters pages 5-7, eiden2004thevesicularamine pages 1-3)

For CAT-1 specifically, sensitivity to the protonophore FCCP directly supports proton-gradient dependence: dopamine uptake was inhibited by 5 mM FCCP. Uptake was also inhibited by the canonical VMAT antagonists reserpine and tetrabenazine at assay concentrations of 100 nM and 1 mM, respectively. However, direct CAT-1 proton-flux measurements, transport stoichiometry, purified-protein kinetics, and a high-resolution CAT-1 structure remain unavailable in the retrieved literature. (duerr1999thecat1gene pages 5-6)

Thus, the precise annotation should be: **vesicular monoamine/H⁺ antiporter**, with direct evidence for monoamine transport and proton-gradient dependence, but family-level inference for the complete alternating-access cycle and 2H⁺:1-amine stoichiometry.

## 3. Site of action and localization

CAT-1 acts in the **membrane of neuronal secretory/synaptic vesicles**, not primarily at the cell surface. Anti-CAT-1 immunofluorescence was concentrated in neuronal processes and synaptic regions. In *unc-104* kinesin mutants, which fail to transport synaptic vesicles normally into axons, CAT-1-containing material accumulated in cell bodies; this trafficking dependence supports vesicular association. (duerr1999thecat1gene pages 6-8, duerr1999thecat1gene pages 5-6)

The original analysis observed strong, reproducible staining in approximately **20 neurons**, plus weak or variable staining in five additional neurons. Identified cells included dopaminergic ADE, PDE, and CEP neurons; serotonergic ADF and NSM neurons; AIM, RIC, RIH, and CAN cells; and developmentally acquired staining in VC4/VC5 around the L4 stage. This distribution encompassed all then-recognized dopamine- and serotonin-containing neurons plus additional candidate aminergic cells. (duerr1999thecat1gene pages 6-8, duerr1999thecat1gene pages 5-6)

The 2024 endogenous-reporter neurotransmitter atlas refined this interpretation. CAT-1 expression is appropriately combined with biosynthetic markers to assign transmitter identity: *tph-1 + bas-1 + cat-1* for serotonin, *cat-2 + bas-1 + cat-1* for dopamine, *tdc-1 + cat-1* for tyramine, and *tdc-1 + tbh-1 + cat-1* for octopamine. CAT-1 expression was also detected in previously underappreciated sex-specific, glial, and non-neural contexts, including glia associated with male spicule neurons and the male vas deferens. (wang2024aneurotransmitteratlas pages 37-38, wang2024aneurotransmitteratlas pages 3-5)

An important atlas-era caution is that tissue monoamine content does not by itself prove vesicular neurotransmission. For example, AIM can acquire serotonin through the plasma-membrane transporter MOD-5 but lacks CAT-1; serotonin staining in AIM therefore does not establish conventional vesicular serotonergic release. Conversely, CAT-1 alone does not identify which monoamine a cell uses; biosynthetic enzymes and physiological release evidence are also needed. (wang2024aneurotransmitteratlas pages 37-38)

## 4. Position in biochemical and signaling pathways

CAT-1 occupies the **packaging step** between monoamine synthesis and exocytotic signaling:

1. Dopamine is synthesized through CAT-2/tyrosine hydroxylase and BAS-1/aromatic amino-acid decarboxylase; serotonin uses TPH-1 and BAS-1; tyramine and octopamine use TDC-1 and, for octopamine, TBH-1.
2. CAT-1 moves the resulting cytosolic amine into acidified secretory vesicles.
3. Vesicles undergo regulated exocytosis, releasing transmitter to activate dopamine, serotonin, tyramine, or octopamine receptors.
4. Plasma-membrane transporters such as DAT-1 or MOD-5 clear extracellular transmitter; these proteins are functionally distinct from CAT-1. (wang2024aneurotransmitteratlas pages 3-5, lawal2013slc18vesicularneurotransmitter pages 1-2, eiden2004thevesicularamine pages 1-3)

Accordingly, *cat-1* loss simultaneously weakens several aminergic systems. A *cat-1* mutant should not automatically be described as a dopamine-specific mutant or a simple serotonin-deficient model. The 2023 dopamine review appropriately treats it as a vesicular-packaging mutant affecting both dopamine and serotonin, and potentially the other worm monoamines. (mcmillen2023neuralmechanismsof pages 6-7)

The cellular benefit is twofold: CAT-1 supplies vesicles with releasable transmitter and lowers potentially reactive cytosolic monoamine. Conserved VMAT biology predicts that sequestration limits dopamine oxidation and reactive metabolites; the enhanced MPP⁺ susceptibility of CAT-1-deficient neurons is consistent with this protective function. (bradner2021geneticortoxicant pages 1-2, guillot2009protectiveactionsof pages 15-16)

## 5. Genetic and physiological evidence

The *e1111* nonsense allele eliminates detectable CAT-1 immunoreactivity, whereas *n733*, affecting transmembrane domain 5, retains near-normal staining but has impaired serotonin transport. Genomic worm CAT-1 transgenes restored transporter staining and monoamine-associated fluorescence, demonstrating locus-specific rescue. Human VMAT1 and VMAT2 transgenes also localized to synaptic regions and partially rescued behavior, providing strong functional-orthology evidence despite expression in only a minority of transgenic animals. (duerr1999thecat1gene pages 9-11, duerr1999thecat1gene pages 6-8)

Representative quantitative data include pharyngeal-pumping rates of approximately **275 pumps/min in wild type, 160/min in *cat-1*, 202/min after human VMAT1 expression, and 208/min after human VMAT2 expression**. Mutants also failed to slow normally on entering bacterial food, showed deficient grazing, mild temperature-sensitive egg-laying impairment, and reduced male mating success; fewer than half of mutant males mated successfully, and almost none sired more than 50 cross-progeny. These are downstream consequences of impaired monoamine packaging, not evidence that CAT-1 directly controls muscles or sensory transduction. (duerr1999thecat1gene pages 9-11, duerr1999thecat1gene pages 3-3)

The later *ok411* allele contains an approximately 400–429-bp deletion affecting the first coding exon and produces no detectable CAT-1 protein. It reproduces grazing, pumping, and egg-laying defects, while ten automated swimming measurements showed no significant generalized motility deficit. That dissociation argues that several behavioral phenotypes reflect specific aminergic signaling defects rather than global sickness or paralysis. (bradner2021geneticortoxicant pages 4-6, bradner2021geneticortoxicant pages 3-4)

## 6. Recent developments, 2023–2024

The major recent advance was not a revision of CAT-1 biochemistry but improved cellular-resolution interpretation. Wang and colleagues’ **2024 eLife neurotransmitter atlas**, published in October 2024, used CRISPR/Cas9 endogenous knock-in reporters and NeuroPAL neuron identification rather than relying primarily on multicopy promoter reporters. It expanded evidence for cotransmission, sexual dimorphism, glial expression, and non-neural monoamine-pathway components; the male nervous system contains almost 30% more neurons than the hermaphrodite nervous system, making sex-resolved mapping especially important. [DOI URL](https://doi.org/10.7554/eLife.95402.3). (wang2024aneurotransmitteratlas pages 37-38, wang2024aneurotransmitteratlas pages 3-5)

Two 2023 reviews place CAT-1 in contemporary systems neuroscience. Rosikon et al., published February 2023, emphasize VMAT and plasma-membrane DAT as complementary regulators of dopamine homeostasis and identify direct DAT–VMAT coordination as an unresolved problem. [DOI URL](https://doi.org/10.3389/fphys.2023.970405). McMillen and Chew, published December 2023, describe *cat-1* mutants as tools for dissecting dopaminergic contributions to learning and memory while warning implicitly that vesicular serotonin is disrupted concurrently. [DOI URL](https://doi.org/10.1042/NS20230057). (mcmillen2023neuralmechanismsof pages 6-7, rosikon2023regulationandmodulation pages 16-17)

No retrieved 2023–2024 primary study superseded the 1999 substrate measurements or provided a CAT-1 structure, direct vesicular transport stoichiometry, or definitive endogenous kinetic constants. The current annotation therefore rests on unusually strong foundational functional experiments, interpreted through newer endogenous expression maps.

## 7. Current applications and real-world relevance

### Human SLC18A2 disease modeling

Because CAT-1 is functionally homologous to human VMAT2, a *cat-1*-null background has been used to test human **SLC18A2** and disease variants P237H and P387L. Three MosSCI-integrated lines expressed wild-type or mutant human VMAT2 under a neuronal synaptobrevin promoter. Both disease variants impaired grazing and pharyngeal pumping relative to wild-type human VMAT2, and preliminary serotonin supplementation restored pumping. The model is useful for variant-function and therapeutic-rescue studies, although heterologous promoter expression may not exactly reproduce endogenous CAT-1 or human VMAT2 cellular distribution. Published online September 28, 2018; [DOI URL](https://doi.org/10.1242/dmm.035709). (young2018modellingbraindopamineserotonin pages 3-5, young2018modellingbraindopamineserotonin pages 1-3)

### Neurotoxicology and Parkinson-relevant mechanisms

CAT-1 loss is used to model inadequate vesicular dopamine sequestration. In a DAT-1::GFP reporter background, *cat-1(ok411)* animals showed greater dopaminergic-neuron damage at lower MPP⁺ doses, with a significant strain-by-treatment interaction (**p<0.001; total n=587 across four experiments**). This supports the expert model that vesicular sequestration protects dopamine neurons by limiting reactive cytosolic dopamine and toxicant exposure. (bradner2021geneticortoxicant pages 6-7, bradner2021geneticortoxicant pages 4-6)

Untargeted metabolomics identified **114 features** differing between *cat-1* mutants and wild type at p<0.05 and **199 features** after four-hour MPP⁺ exposure, with 14 overlapping. Tyrosine, tryptophan, glycerophospholipid, and related pathways were implicated. These results are hypothesis-generating rather than proof of individual metabolite identities because pathway assignment relied substantially on untargeted mass features. Journal publication was online February 4, 2021; [journal DOI](https://doi.org/10.1093/toxsci/kfab011), [preprint DOI](https://doi.org/10.1101/2020.10.02.324095), and [raw-data URL](https://doi.org/10.5061/dryad.0zpc866x0). (bradner2021geneticortoxicant pages 3-4, bradner2021geneticortoxicant pages 1-2, bradner2021geneticortoxicant pages 6-7)

### Pharmacology and behavioral screening

Reserpine and tetrabenazine sensitivity makes CAT-1 a conserved pharmacological node for studying vesicular storage, while *cat-1* mutants help separate requirements for vesicular release from plasma-membrane transport or receptor action. This has supported studies of monoamine-dependent feeding, egg laying, mating, food-search behavior, learning, and responses to psychostimulants. Interpretation must remain pathway-aware because CAT-1 perturbs multiple monoamines simultaneously. (duerr1999thecat1gene pages 9-11, duerr1999thecat1gene pages 5-6, mcmillen2023neuralmechanismsof pages 6-7)

### Regulation of transporter abundance

The distinct transcriptional regulator **RCAT-1/R02D3.7** binds within *cat-1* and near the *cat-2* promoter. In *rcat-1(ok1745)* mutants, *cat-1* and *cat-2* transcripts increased nearly threefold, suggesting coordinated negative regulation of dopamine synthesis and vesicular packaging. Direct synaptic dopamine measurements were not performed, so altered behavior cannot yet be assigned quantitatively to CAT-1 abundance alone. Published February 21, 2022; [DOI URL](https://doi.org/10.3390/ijms23042393). (jeong2022deficiencyinrcat1 pages 8-10)

## 8. Evidence-weighted annotation and remaining uncertainties

**Recommended primary annotation:** “Proton-gradient-dependent vesicular monoamine transporter that packages dopamine, serotonin, tyramine, and probably octopamine into neuronal secretory vesicles for regulated release.”

**Localization annotation:** “Integral membrane protein of synaptic/secretory vesicles in monoaminergic neurons, with additional sex-specific glial and non-neural expression reported by endogenous-locus mapping.”

**Evidence strength:**

* **High:** gene identity; predicted 12-TM VMAT architecture; direct dopamine and serotonin transport; broad monoamine recognition; synaptic-vesicle association; reserpine/tetrabenazine/FCCP sensitivity; requirement for normal monoamine-dependent behavior.
* **Moderate-to-high:** physiological transport of tyramine and octopamine, based on in-vitro recognition plus expression in the relevant cells.
* **Conserved-family inference rather than CAT-1-specific measurement:** exact 2H⁺:1-amine stoichiometry, detailed alternating-access mechanism, and specific trafficking motifs.
* **Unresolved:** high-resolution structure, absolute substrate Km values in native worm vesicles, vesicular concentrations and quantal effects, complete sex- and stage-resolved release map, and how CAT-1 trafficking is coordinated with plasma-membrane monoamine transporters.

Overall, Q9GNP0 is not merely an MFS-domain candidate: it is a functionally validated vesicular monoamine transporter. Its most precise biological role is the conversion of newly synthesized cytosolic monoamine into a protected, exocytosis-competent vesicular pool.

References

1. (duerr1999thecat1gene pages 3-3): Janet S. Duerr, Dennis L. Frisby, Jennifer Gaskin, Angie Duke, Karen Asermely, David Huddleston, Lee E. Eiden, and James B. Rand. The cat-1 gene of caenorhabditis elegansencodes a vesicular monoamine transporter required for specific monoamine-dependent behaviors. The Journal of Neuroscience, 19:72-84, Jan 1999. URL: https://doi.org/10.1523/jneurosci.19-01-00072.1999, doi:10.1523/jneurosci.19-01-00072.1999. This article has 345 citations.

2. (duerr1999thecat1gene pages 6-8): Janet S. Duerr, Dennis L. Frisby, Jennifer Gaskin, Angie Duke, Karen Asermely, David Huddleston, Lee E. Eiden, and James B. Rand. The cat-1 gene of caenorhabditis elegansencodes a vesicular monoamine transporter required for specific monoamine-dependent behaviors. The Journal of Neuroscience, 19:72-84, Jan 1999. URL: https://doi.org/10.1523/jneurosci.19-01-00072.1999, doi:10.1523/jneurosci.19-01-00072.1999. This article has 345 citations.

3. (jeong2022deficiencyinrcat1 pages 1-2): Haelim Jeong, Jun Young Park, Ji-Hyun Lee, Ja-Hyun Baik, Chae-Yeon Kim, Jin-Young Cho, Monica Driscoll, and Young-Ki Paik. Deficiency in rcat-1 function causes dopamine metabolism related behavioral disorders in caenorhabditis elegans. International Journal of Molecular Sciences, 23:2393, Feb 2022. URL: https://doi.org/10.3390/ijms23042393, doi:10.3390/ijms23042393. This article has 8 citations.

4. (jeong2022deficiencyinrcat1 pages 8-10): Haelim Jeong, Jun Young Park, Ji-Hyun Lee, Ja-Hyun Baik, Chae-Yeon Kim, Jin-Young Cho, Monica Driscoll, and Young-Ki Paik. Deficiency in rcat-1 function causes dopamine metabolism related behavioral disorders in caenorhabditis elegans. International Journal of Molecular Sciences, 23:2393, Feb 2022. URL: https://doi.org/10.3390/ijms23042393, doi:10.3390/ijms23042393. This article has 8 citations.

5. (duerr1999thecat1gene pages 5-6): Janet S. Duerr, Dennis L. Frisby, Jennifer Gaskin, Angie Duke, Karen Asermely, David Huddleston, Lee E. Eiden, and James B. Rand. The cat-1 gene of caenorhabditis elegansencodes a vesicular monoamine transporter required for specific monoamine-dependent behaviors. The Journal of Neuroscience, 19:72-84, Jan 1999. URL: https://doi.org/10.1523/jneurosci.19-01-00072.1999, doi:10.1523/jneurosci.19-01-00072.1999. This article has 345 citations.

6. (eiden2004thevesicularamine pages 3-4): Lee E. Eiden, Martin K.-H. Sch�fer, Eberhard Weihe, and Burkhard Sch�tz. The vesicular amine transporter family (slc18): amine/proton antiporters required for vesicular accumulation and regulated exocytotic secretion of monoamines and acetylcholine. Pflügers Archiv, 447:636-640, Feb 2004. URL: https://doi.org/10.1007/s00424-003-1100-5, doi:10.1007/s00424-003-1100-5. This article has 323 citations.

7. (lawal2013slc18vesicularneurotransmitter pages 1-2): Hakeem O. Lawal and David E. Krantz. Slc18: vesicular neurotransmitter transporters for monoamines and acetylcholine. Molecular aspects of medicine, 34 2-3:360-72, Apr 2013. URL: https://doi.org/10.1016/j.mam.2012.07.005, doi:10.1016/j.mam.2012.07.005. This article has 142 citations and is from a highest quality peer-reviewed journal.

8. (eiden2004thevesicularamine pages 1-3): Lee E. Eiden, Martin K.-H. Sch�fer, Eberhard Weihe, and Burkhard Sch�tz. The vesicular amine transporter family (slc18): amine/proton antiporters required for vesicular accumulation and regulated exocytotic secretion of monoamines and acetylcholine. Pflügers Archiv, 447:636-640, Feb 2004. URL: https://doi.org/10.1007/s00424-003-1100-5, doi:10.1007/s00424-003-1100-5. This article has 323 citations.

9. (duerr1999thecat1gene pages 9-11): Janet S. Duerr, Dennis L. Frisby, Jennifer Gaskin, Angie Duke, Karen Asermely, David Huddleston, Lee E. Eiden, and James B. Rand. The cat-1 gene of caenorhabditis elegansencodes a vesicular monoamine transporter required for specific monoamine-dependent behaviors. The Journal of Neuroscience, 19:72-84, Jan 1999. URL: https://doi.org/10.1523/jneurosci.19-01-00072.1999, doi:10.1523/jneurosci.19-01-00072.1999. This article has 345 citations.

10. (wang2024aneurotransmitteratlas pages 37-38): Chen Wang, Berta Vidal, Surojit Sural, Curtis Loer, G Robert Aguilar, Daniel M Merritt, Itai Antoine Toker, Merly C Vogt, Cyril C Cros, and Oliver Hobert. A neurotransmitter atlas of c. elegans males and hermaphrodites. Oct 2024. URL: https://doi.org/10.7554/elife.95402.3, doi:10.7554/elife.95402.3. This article has 52 citations and is from a domain leading peer-reviewed journal.

11. (wang2024aneurotransmitteratlas pages 3-5): Chen Wang, Berta Vidal, Surojit Sural, Curtis Loer, G Robert Aguilar, Daniel M Merritt, Itai Antoine Toker, Merly C Vogt, Cyril C Cros, and Oliver Hobert. A neurotransmitter atlas of c. elegans males and hermaphrodites. Oct 2024. URL: https://doi.org/10.7554/elife.95402.3, doi:10.7554/elife.95402.3. This article has 52 citations and is from a domain leading peer-reviewed journal.

12. (young2018modellingbraindopamineserotonin pages 3-5): Alexander T. Young, Kien N. Ly, Callum Wilson, Klaus Lehnert, Russell G. Snell, Suzanne J. Reid, and Jessie C. Jacobsen. Modelling brain dopamine-serotonin vesicular transport disease in caenorhabditis elegans. Disease Models & Mechanisms, Nov 2018. URL: https://doi.org/10.1242/dmm.035709, doi:10.1242/dmm.035709. This article has 11 citations and is from a domain leading peer-reviewed journal.

13. (young2018modellingbraindopamineserotonin pages 1-3): Alexander T. Young, Kien N. Ly, Callum Wilson, Klaus Lehnert, Russell G. Snell, Suzanne J. Reid, and Jessie C. Jacobsen. Modelling brain dopamine-serotonin vesicular transport disease in caenorhabditis elegans. Disease Models & Mechanisms, Nov 2018. URL: https://doi.org/10.1242/dmm.035709, doi:10.1242/dmm.035709. This article has 11 citations and is from a domain leading peer-reviewed journal.

14. (bradner2021geneticortoxicant pages 1-2): Joshua M. Bradner, V. Kalia, Fion K. Lau, Monica Sharma, Meghan L. Bucher, Michelle A. Johnson, Merry Chen, D. Walker, Dean P. Jones, and G. Miller. Genetic or toxicant induced disruption of vesicular monoamine storage and global metabolic profiling in caenorhabditis elegans. bioRxiv, Oct 2021. URL: https://doi.org/10.1101/2020.10.02.324095, doi:10.1101/2020.10.02.324095. This article has 11 citations.

15. (bradner2021geneticortoxicant pages 6-7): Joshua M. Bradner, V. Kalia, Fion K. Lau, Monica Sharma, Meghan L. Bucher, Michelle A. Johnson, Merry Chen, D. Walker, Dean P. Jones, and G. Miller. Genetic or toxicant induced disruption of vesicular monoamine storage and global metabolic profiling in caenorhabditis elegans. bioRxiv, Oct 2021. URL: https://doi.org/10.1101/2020.10.02.324095, doi:10.1101/2020.10.02.324095. This article has 11 citations.

16. (bradner2021geneticortoxicant pages 4-6): Joshua M. Bradner, V. Kalia, Fion K. Lau, Monica Sharma, Meghan L. Bucher, Michelle A. Johnson, Merry Chen, D. Walker, Dean P. Jones, and G. Miller. Genetic or toxicant induced disruption of vesicular monoamine storage and global metabolic profiling in caenorhabditis elegans. bioRxiv, Oct 2021. URL: https://doi.org/10.1101/2020.10.02.324095, doi:10.1101/2020.10.02.324095. This article has 11 citations.

17. (lawal2013slc18vesicularneurotransmitter pages 7-8): Hakeem O. Lawal and David E. Krantz. Slc18: vesicular neurotransmitter transporters for monoamines and acetylcholine. Molecular aspects of medicine, 34 2-3:360-72, Apr 2013. URL: https://doi.org/10.1016/j.mam.2012.07.005, doi:10.1016/j.mam.2012.07.005. This article has 142 citations and is from a highest quality peer-reviewed journal.

18. (rosikon2023regulationandmodulation pages 16-17): Katarzyna D. Rosikon, Megan C. Bone, and Hakeem O. Lawal. Regulation and modulation of biogenic amine neurotransmission in drosophila and caenorhabditis elegans. Frontiers in Physiology, Feb 2023. URL: https://doi.org/10.3389/fphys.2023.970405, doi:10.3389/fphys.2023.970405. This article has 55 citations.

19. (fei2009vesicularneurotransmittertransporters pages 5-7): H. Fei and D. E. Krantz. Vesicular Neurotransmitter Transporters, pages 87-137. Springer US, Jan 2009. URL: https://doi.org/10.1007/978-0-387-30370-3\_7, doi:10.1007/978-0-387-30370-3\_7. This article has 5 citations.

20. (mcmillen2023neuralmechanismsof pages 6-7): Anna McMillen and Yee Lian Chew. Neural mechanisms of dopamine function in learning and memory in caenorhabditis elegans. Neuronal Signaling, Dec 2023. URL: https://doi.org/10.1042/ns20230057, doi:10.1042/ns20230057. This article has 17 citations and is from a peer-reviewed journal.

21. (guillot2009protectiveactionsof pages 15-16): Thomas S. Guillot and Gary W. Miller. Protective actions of the vesicular monoamine transporter 2 (vmat2) in monoaminergic neurons. Molecular Neurobiology, 39:149-170, Mar 2009. URL: https://doi.org/10.1007/s12035-009-8059-y, doi:10.1007/s12035-009-8059-y. This article has 271 citations and is from a peer-reviewed journal.

22. (bradner2021geneticortoxicant pages 3-4): Joshua M. Bradner, V. Kalia, Fion K. Lau, Monica Sharma, Meghan L. Bucher, Michelle A. Johnson, Merry Chen, D. Walker, Dean P. Jones, and G. Miller. Genetic or toxicant induced disruption of vesicular monoamine storage and global metabolic profiling in caenorhabditis elegans. bioRxiv, Oct 2021. URL: https://doi.org/10.1101/2020.10.02.324095, doi:10.1101/2020.10.02.324095. This article has 11 citations.

## Artifacts

- [Edison artifact artifact-00](cat-1-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. wang2024aneurotransmitteratlas pages 37-38
2. mcmillen2023neuralmechanismsof pages 6-7
3. eiden2004thevesicularamine pages 3-4
4. eiden2004thevesicularamine pages 1-3
5. wang2024aneurotransmitteratlas pages 3-5
6. young2018modellingbraindopamineserotonin pages 3-5
7. young2018modellingbraindopamineserotonin pages 1-3
8. bradner2021geneticortoxicant pages 1-2
9. bradner2021geneticortoxicant pages 6-7
10. bradner2021geneticortoxicant pages 4-6
11. rosikon2023regulationandmodulation pages 16-17
12. fei2009vesicularneurotransmittertransporters pages 5-7
13. guillot2009protectiveactionsof pages 15-16
14. bradner2021geneticortoxicant pages 3-4
15. DOI
16. journal DOI
17. preprint DOI
18. DOI URL
19. raw-data URL
20. https://doi.org/10.1523/JNEUROSCI.19-01-00072.1999
21. https://doi.org/10.1007/s00424-003-1100-5
22. https://doi.org/10.1016/j.mam.2012.07.005
23. https://doi.org/10.7554/eLife.95402.3
24. https://doi.org/10.1242/dmm.035709
25. https://doi.org/10.1093/toxsci/kfab011
26. https://doi.org/10.1101/2020.10.02.324095
27. https://doi.org/10.3389/fphys.2023.970405
28. https://doi.org/10.1042/NS20230057
29. https://doi.org/10.5061/dryad.0zpc866x0
30. https://doi.org/10.3390/ijms23042393
31. https://doi.org/10.1523/jneurosci.19-01-00072.1999,
32. https://doi.org/10.3390/ijms23042393,
33. https://doi.org/10.1007/s00424-003-1100-5,
34. https://doi.org/10.1016/j.mam.2012.07.005,
35. https://doi.org/10.7554/elife.95402.3,
36. https://doi.org/10.1242/dmm.035709,
37. https://doi.org/10.1101/2020.10.02.324095,
38. https://doi.org/10.3389/fphys.2023.970405,
39. https://doi.org/10.1007/978-0-387-30370-3\_7,
40. https://doi.org/10.1042/ns20230057,
41. https://doi.org/10.1007/s12035-009-8059-y,