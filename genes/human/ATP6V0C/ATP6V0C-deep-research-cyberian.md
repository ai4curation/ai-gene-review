---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-24T01:20:59.090331'
end_time: '2026-01-24T01:33:45.346022'
duration_seconds: 766.26
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: ATP6V0C
  gene_symbol: ATP6V0C
  uniprot_accession: P27449
  protein_description: 'RecName: Full=V-type proton ATPase 16 kDa proteolipid subunit
    c {ECO:0000305}; Short=V-ATPase 16 kDa proteolipid subunit c {ECO:0000305}; AltName:
    Full=Vacuolar proton pump 16 kDa proteolipid subunit c {ECO:0000305};'
  gene_info: Name=ATP6V0C; Synonyms=ATP6C, ATP6L, ATPL;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the V-ATPase proteolipid subunit family.
  protein_domains: ATPase_proteolipid_c-like_dom. (IPR002379); ATPase_proteolipid_csu.
    (IPR000245); ATPase_proteolipid_su_C_euk. (IPR011555); F/V-ATP_Csub_sf. (IPR035921);
    ATP-synt_C (PF00137)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 29
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P27449
- **Protein Description:** RecName: Full=V-type proton ATPase 16 kDa proteolipid subunit c {ECO:0000305}; Short=V-ATPase 16 kDa proteolipid subunit c {ECO:0000305}; AltName: Full=Vacuolar proton pump 16 kDa proteolipid subunit c {ECO:0000305};
- **Gene Information:** Name=ATP6V0C; Synonyms=ATP6C, ATP6L, ATPL;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the V-ATPase proteolipid subunit family.
- **Key Domains:** ATPase_proteolipid_c-like_dom. (IPR002379); ATPase_proteolipid_csu. (IPR000245); ATPase_proteolipid_su_C_euk. (IPR011555); F/V-ATP_Csub_sf. (IPR035921); ATP-synt_C (PF00137)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ATP6V0C" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ATP6V0C' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ATP6V0C** (gene ID: ATP6V0C, UniProt: P27449) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# ATP6V0C: V-type Proton ATPase 16 kDa Proteolipid Subunit c

## Introduction

ATP6V0C (also known as ATP6C, ATP6L, ATPL) encodes the 16 kDa proteolipid subunit c of the vacuolar H+-ATPase (V-ATPase), one of the most fundamental proton-translocating enzymes in eukaryotic cells. The human ATP6V0C gene is located on chromosome 16p13.3 and produces a small, highly hydrophobic integral membrane protein that is essential for the proton-pumping function of V-ATPases [mucha-2018-microdeletion-abstract]. As a core component of the V0 membrane sector, ATP6V0C forms the proteolipid ring that constitutes the proton channel through which protons are translocated across membranes. V-ATPases are responsible for acidifying numerous intracellular compartments including lysosomes, endosomes, the Golgi apparatus, and synaptic vesicles, and are also present at the plasma membrane of specialized cell types [cotter-2015-insights-abstract].

The V-ATPase is among the most ancient and conserved enzyme complexes, with clear evolutionary relationships to the F-type ATP synthases of mitochondria and bacteria [forgac-1992-structure-function-abstract]. The c-subunit proteolipid belongs to the ATPase proteolipid subunit family characterized by the highly conserved Pfam domain PF00137. Understanding the precise molecular function of ATP6V0C is essential not only for comprehending fundamental cellular physiology but also for addressing its emerging roles in disease, particularly neurological disorders [colacurcio-2016-lysosomal-acidification-abstract].

## Structure of the V-ATPase Complex and the c-Subunit

The V-ATPase holoenzyme is a large multisubunit complex of approximately 900 kDa, organized into two distinct functional domains: the peripheral V1 sector and the membrane-integral V0 sector [cipriano-2008-structure-regulation-abstract]. The V1 sector contains eight different subunits (A-H) and is responsible for ATP hydrolysis. The V0 sector contains six different subunits in yeast (a, c, c', c'', d, and e) or five in mammals (where c' and c'' are replaced by additional copies of c), and is responsible for proton translocation across the membrane [vasanthakumar-2020-structure-roles-abstract].

ATP6V0C is a small, extremely hydrophobic protein of 155 amino acids in humans that spans the membrane four times with both termini facing the cytoplasm. The protein contains two hairpin structures, each consisting of two transmembrane helices connected by short loops [roh-2018-cryoem-abstract]. This four-helix bundle topology is characteristic of V-ATPase c-subunits and represents a duplication compared to the two-helix c-subunits found in F-type ATPases, where approximately 10-15 copies form the c-ring. Consequently, V-ATPases require fewer c-subunit copies to form a complete proteolipid ring [powell-2000-proton-pore-abstract].

Cryo-electron microscopy studies of the yeast V-ATPase have revealed that the proteolipid ring contains ten c-subunits arranged in a ring structure [zhao-2015-cryoem-rotational-abstract]. This stoichiometry sets the ATP:H+ ratio for proton pumping at 3:10, meaning that for every three ATP molecules hydrolyzed, ten protons are translocated across the membrane. The 3.5 Å resolution structure of the yeast V0 sector has provided detailed atomic information about the proton pathway at the interface between the proteolipid ring and subunit a [roh-2018-cryoem-abstract]. Importantly, this structure revealed that a helix from the assembly factor Voa1 remains bound inside the proteolipid ring in the mature complex, contributing to its stability.

## Molecular Function: Proton Translocation Mechanism

The primary molecular function of ATP6V0C is to provide the proton-binding sites and form the rotary conduit for proton translocation in V-ATPases. The mechanism operates through a rotary catalysis process analogous to F-type ATP synthases but functioning in the ATP-hydrolysis direction to pump protons rather than synthesize ATP [oot-2017-breaking-up-abstract].

Central to the proton translocation function is a highly conserved glutamate residue located in the fourth transmembrane helix of ATP6V0C. In human ATP6V0C, this is Glu137, which corresponds to the essential acidic residue found in all c-subunit homologs. This glutamate residue serves as the proton-binding site that transiently binds and releases protons during the rotary cycle [wang-2004-TM-interaction-abstract]. Protonation and deprotonation of this glutamate is coupled to the rotation of the c-ring relative to subunit a.

The proton translocation mechanism involves protons entering from the cytoplasmic side through a hemichannel in subunit a, binding to the glutamate residue on a c-subunit, rotating almost a full turn with the c-ring, and then being released into the luminal (or extracellular) hemichannel in subunit a [roh-2018-cryoem-abstract]. A critical arginine residue (Arg735 in yeast subunit a) is positioned at the interface between the two hemichannels and is essential for preventing proton leakage and maintaining unidirectional transport. Cross-linking studies have demonstrated direct interaction between the helical face of transmembrane helix 7 of subunit a containing this arginine and the helical face of the c-subunit containing the essential glutamate [wang-2004-TM-interaction-abstract].

The c-subunit is also the binding target for the potent V-ATPase inhibitors bafilomycin A1 and concanamycin A. Photoaffinity labeling studies demonstrated that these plecomacrolide antibiotics bind specifically and exclusively to the c-subunit proteolipid, inhibiting proton transport by preventing rotation of the c-ring [huss-2002-concanamycin-binding-abstract]. This pharmacological targeting has made bafilomycin A1 an invaluable tool for studying V-ATPase function in cells.

## Subcellular Localization

ATP6V0C functions as part of V-ATPase complexes localized to multiple cellular membranes. The primary sites of V-ATPase activity and thus ATP6V0C localization include the membranes of lysosomes, endosomes, the trans-Golgi network, secretory granules, synaptic vesicles, and clathrin-coated vesicles [cipriano-2008-structure-regulation-abstract]. In certain specialized cell types, V-ATPases are also present at the plasma membrane.

In lysosomes, V-ATPases maintain the acidic pH (approximately 4.5-5.0) required for the activity of lysosomal hydrolases that degrade proteins, lipids, carbohydrates, and nucleic acids [colacurcio-2016-lysosomal-acidification-abstract]. In endosomes, progressive acidification along the endocytic pathway is essential for ligand-receptor dissociation and receptor recycling [forgac-1992-structure-function-abstract]. The trans-Golgi network requires moderate acidification for proper protein sorting and processing.

In synaptic vesicles, V-ATPases generate the electrochemical gradient that drives neurotransmitter uptake via vesicular neurotransmitter transporters [elfar-2011-synaptic-vesicle-abstract]. The acidification establishes both a pH gradient and a membrane potential across the synaptic vesicle membrane. In the zebrafish nervous system, expression studies of a neuron-specific ATP6V0C isoform (atp6v0c2) revealed co-localization with the presynaptic marker SV2, consistent with its role in neurotransmitter storage and release [chung-2010-zebrafish-abstract].

At the plasma membrane of specialized cells such as osteoclasts, renal intercalated cells, and certain tumor cells, V-ATPases pump protons out of the cell [cotter-2015-insights-abstract]. In osteoclasts, plasma membrane V-ATPases are essential for creating the acidic resorption lacuna that dissolves bone mineral. In renal intercalated cells, they contribute to urinary acidification and systemic pH homeostasis.

## Role in Cellular Processes and Signaling Pathways

Beyond its fundamental role in acidification, ATP6V0C participates in several critical cellular pathways.

### Lysosomal Function and Autophagy

V-ATPase activity is essential for lysosomal degradative function and thus for autophagy. Proper lysosomal acidification is required for the activity of cathepsins and other acid hydrolases [colacurcio-2016-lysosomal-acidification-abstract]. When V-ATPase function is impaired, autophagosomes accumulate because fusion with lysosomes is compromised and lysosomal degradation fails. Interestingly, studies using the V-ATPase inhibitor bafilomycin A1 have revealed that it blocks autophagy through two distinct mechanisms: V-ATPase-dependent inhibition of acidification and Ca-P60A/SERCA-dependent inhibition of autophagosome-lysosome fusion [mauvezin-2015-bafilomycin-abstract].

A groundbreaking discovery revealed that the V-ATPase, and specifically ATP6V0C, plays a direct role in initiating xenophagy (antibacterial autophagy). Upon vacuolar damage caused by intracellular bacteria, the V-ATPase recruits ATG16L1 to the damaged compartment, initiating autophagosomal engulfment [xu-2019-bacterial-effector-abstract]. The Salmonella effector protein SopF was found to ADP-ribosylate Gln124 of ATP6V0C, blocking this xenophagy-initiating function. This represents a non-canonical function of ATP6V0C that is independent of proton pumping.

### mTORC1 Signaling

V-ATPases function as a key platform for mTORC1 signaling at the lysosomal membrane. The V-ATPase directly interacts with the Ragulator complex, and this interaction is required for amino acid-dependent activation of mTORC1 [abu-remaileh-2017-lysosomal-metabolomics-abstract]. Lysosomal metabolomics studies have shown that mTOR inhibition strongly reduces lysosomal amino acid efflux, converting the lysosome into a cellular depot for essential amino acids [abu-remaileh-2017-lysosomal-metabolomics-abstract]. The E2F1 transcription factor was shown to regulate V-ATPase activity and lysosomal positioning, thereby influencing mTORC1 activation [meo-evoli-2015-e2f1-abstract].

### Neurotransmitter Release

Beyond its established role in synaptic vesicle acidification for neurotransmitter loading, accumulating evidence indicates that the V0 sector, including ATP6V0C, may have a direct role in the membrane fusion event underlying neurotransmitter release [elfar-2011-synaptic-vesicle-abstract]. The c-subunit has been shown to directly interact with the v-SNARE VAMP2 (synaptobrevin), and this interaction appears to function at a late step in transmitter release.

Chromophore-assisted light inactivation (CALI) experiments demonstrated that specific inactivation of ATP6V0C rapidly inhibited neurotransmission in hippocampal neurons, and this effect occurred downstream of synaptic vesicle acidification [rama-2018-neurotransmitter-abstract]. Studies using gene transfer of ATP6V0C into striatal cells of parkinsonian mice showed that ATP6V0C could mediate dopamine release, and this improved motor performance, supporting a functional role in neurotransmitter release beyond acidification [jin-2012-dopamine-abstract].

## Regulation

V-ATPase activity is regulated at multiple levels, with reversible dissociation of the V1 and V0 sectors being a particularly important mechanism [cipriano-2008-structure-regulation-abstract]. In yeast, glucose deprivation triggers rapid dissociation of V1 from V0, which silences ATP hydrolysis while preventing proton leakage through V0. Reassembly occurs upon glucose restoration and requires the RAVE complex (Regulator of the ATPase of Vacuolar and Endosomal membranes) [kane-2003-assembly-regulation-abstract].

Assembly of the V0 sector occurs in the endoplasmic reticulum and requires dedicated assembly factors including Vma21p, Vma12p, Vma22p, Pkr1p, and Voa1p in yeast [ryan-2008-voa1-assembly-abstract; davis-kaplan-2006-pkr1-abstract]. These factors assist in the proper folding and assembly of the c-subunit proteolipid ring. The Voa1 factor was found to remain associated with the C-terminus bound inside the assembled proteolipid ring even in the mature complex [roh-2018-cryoem-abstract].

ATP6V0C protein levels are also regulated by ubiquitin-mediated degradation. The brain-enriched E3 ubiquitin ligase RNF182, which is upregulated in Alzheimer's disease brains, was shown to directly interact with ATP6V0C and target it for proteasomal degradation [liu-2008-rnf182-abstract]. This provides a potential mechanism linking V-ATPase dysfunction to neurodegeneration.

## Disease Associations

Mutations affecting V-ATPase subunits are associated with multiple human diseases, and emerging evidence implicates ATP6V0C specifically in neurological disorders.

### Epilepsy and Developmental Delay

De novo mutations in ATP6V0C have been identified as causative for epilepsy with intellectual disability. Whole-exome sequencing identified a novel heterozygous stop-loss mutation (c.467A>T, p.*156Leuext*35) in ATP6V0C in a patient with epilepsy and intellectual disability [ittiwut-2020-epilepsy-abstract]. The finding that the mutant RNA level was approximately half that of controls suggested haploinsufficiency as the pathogenic mechanism. More recently, two unrelated patients with Dravet-like syndrome were identified with heterozygous de novo missense variants in ATP6V0C (c.319G>C, p.Gly107Arg and c.284C>T, p.Ala95Val), placing ATP6V0C variants at the severe end of the epileptic encephalopathy spectrum [rong-2025-dravet-abstract].

### 16p13.3 Microdeletion Syndrome

A contiguous gene deletion syndrome involving ATP6V0C along with TBC1D24 and PDPK1 on chromosome 16p13.3 causes microcephaly, developmental delay, intellectual disability, and epilepsy [mucha-2018-microdeletion-abstract]. All eight individuals identified with overlapping 205-504 kb deletions displayed developmental delay, intellectual disability, and seizures, with six being microcephalic. This syndrome illustrates that ATP6V0C haploinsufficiency contributes to neurodevelopmental pathology.

### Neurodegenerative Disease

Alterations in V-ATPase function and lysosomal acidification have been implicated in Alzheimer's disease and Parkinson's disease [colacurcio-2016-lysosomal-acidification-abstract]. The discovery that RNF182, an E3 ligase upregulated in AD brains, targets ATP6V0C for degradation provides a potential molecular link [liu-2008-rnf182-abstract]. Impaired lysosomal acidification leads to defective autophagy and accumulation of protein aggregates characteristic of these diseases.

## Open Questions

Several important questions about ATP6V0C function remain to be resolved:

1. **Stoichiometry in humans**: While the yeast V-ATPase has been shown to contain 10 c-subunits in its proteolipid ring, the precise stoichiometry in human V-ATPases has not been directly determined structurally. Does the human complex have the same 10-subunit ring, and is the ATP:H+ coupling ratio identical?

2. **Non-canonical fusion function**: The evidence for a direct role of ATP6V0C in membrane fusion events independent of its proton-pumping function is intriguing but mechanistically incomplete. What is the precise structural basis for the interaction between ATP6V0C and VAMP2, and how does this interaction facilitate fusion?

3. **Tissue-specific functions**: Unlike some other V-ATPase subunits that have tissue-specific isoforms (e.g., the a-subunit), humans have only one ATP6V0C gene. How is tissue-specific V-ATPase function regulated in the absence of c-subunit isoforms? Are there post-translational modifications that confer tissue-specific properties?

4. **Disease mechanisms**: While haploinsufficiency appears to be the mechanism for ATP6V0C-associated epilepsy, the precise cellular defects leading to seizures are unclear. Is the phenotype primarily due to impaired synaptic vesicle acidification, defective autophagy, or the proposed fusion function?

5. **Therapeutic targeting**: Given the essential role of V-ATPases in multiple cell types, can ATP6V0C or V-ATPase function be therapeutically modulated in specific tissues without systemic toxicity? What is the therapeutic window for V-ATPase inhibitors in cancer or osteoporosis treatment?

6. **Xenophagy signaling**: The ADP-ribosylation of Gln124 by bacterial effectors reveals a specific signaling function, but does this residue have a physiological role in normal cellular autophagy regulation?

## References

* cotter-2015-insights-abstract - Cotter K, Stransky L, McGuire C, Forgac M. Recent Insights into the Structure, Regulation, and Function of the V-ATPases. Trends Biochem Sci. 2015 Oct;40(10):611-622. PMID: 26410601. DOI: https://doi.org/10.1016/j.tibs.2015.08.005

* roh-2018-cryoem-abstract - Roh SH, Stam NJ, Hryc CF, Couoh-Cardel S, Pintilie G, Chiu W, Wilkens S. The 3.5-Å CryoEM Structure of Nanodisc-Reconstituted Yeast Vacuolar ATPase V0 Proton Channel. Mol Cell. 2018;69(6):993-1004.e3. PMID: 29526695. DOI: https://doi.org/10.1016/j.molcel.2018.02.006

* zhao-2015-cryoem-rotational-abstract - Zhao J, Benlekbir S, Rubinstein JL. Electron cryomicroscopy observation of rotational states in a eukaryotic V-ATPase. Nature. 2015;521(7551):241-5. PMID: 25971514. DOI: https://doi.org/10.1038/nature14365

* cipriano-2008-structure-regulation-abstract - Cipriano DJ, Wang Y, Bond S, Hinton A, Jefferies KC, Qi J, Forgac M. Structure and regulation of the vacuolar ATPases. Biochim Biophys Acta. 2008;1777(7-8):599-604. PMID: 18423392. DOI: https://doi.org/10.1016/j.bbabio.2008.03.013

* vasanthakumar-2020-structure-roles-abstract - Vasanthakumar T, Rubinstein JL. Structure and Roles of V-type ATPases. Trends Biochem Sci. 2020;45(4):295-307. PMID: 32001091. DOI: https://doi.org/10.1016/j.tibs.2019.12.007

* forgac-1992-structure-function-abstract - Forgac M. Structure, function and regulation of the coated vesicle V-ATPase. J Exp Biol. 1992;172:155-69. PMID: 1491223. DOI: https://doi.org/10.1242/jeb.172.1.155

* oot-2017-breaking-up-abstract - Oot RA, Couoh-Cardel S, Sharma S, Stam NJ, Wilkens S. Breaking up and making up: The secret life of the vacuolar H+-ATPase. Protein Sci. 2017;26(5):896-909. PMID: 28247968. DOI: https://doi.org/10.1002/pro.3147

* colacurcio-2016-lysosomal-acidification-abstract - Colacurcio DJ, Nixon RA. Disorders of lysosomal acidification-The emerging role of v-ATPase in aging and neurodegenerative disease. Ageing Res Rev. 2016;32:75-88. PMID: 27197071. DOI: https://doi.org/10.1016/j.arr.2016.05.004

* xu-2019-bacterial-effector-abstract - Xu Y, Zhou P, Cheng S, et al. A Bacterial Effector Reveals the V-ATPase-ATG16L1 Axis that Initiates Xenophagy. Cell. 2019;178(3):552-566.e20. PMID: 31327526. DOI: https://doi.org/10.1016/j.cell.2019.06.007

* elfar-2011-synaptic-vesicle-abstract - El Far O, Seagar M. A role for V-ATPase subunits in synaptic vesicle fusion? J Neurochem. 2011;117(4):603-12. PMID: 21375531. DOI: https://doi.org/10.1111/j.1471-4159.2011.07234.x

* rama-2018-neurotransmitter-abstract - Rama S, Boumedine-Guignon N, Sangiardi M, et al. Chromophore-Assisted Light Inactivation of the V-ATPase V0c Subunit Inhibits Neurotransmitter Release Downstream of Synaptic Vesicle Acidification. Mol Neurobiol. 2018;56(5):3591-3602. PMID: 30155790. DOI: https://doi.org/10.1007/s12035-018-1324-1

* huss-2002-concanamycin-binding-abstract - Huss M, Ingenhorst G, König S, et al. Concanamycin A, the specific inhibitor of V-ATPases, binds to the V(o) subunit c. J Biol Chem. 2002;277(43):40544-8. PMID: 12186879. DOI: https://doi.org/10.1074/jbc.M207345200

* wang-2004-TM-interaction-abstract - Wang Y, Inoue T, Forgac M. TM2 but not TM4 of subunit c'' interacts with TM7 of subunit a of the yeast V-ATPase as defined by disulfide-mediated cross-linking. J Biol Chem. 2004;279(43):44628-38. PMID: 15322078. DOI: https://doi.org/10.1074/jbc.M407345200

* mucha-2018-microdeletion-abstract - Mucha BE, Banka S, Ajeawung NF, et al. A new microdeletion syndrome involving TBC1D24, ATP6V0C, and PDPK1 causes epilepsy, microcephaly, and developmental delay. Genet Med. 2018;21(5):1058-1064. PMID: 30245510. DOI: https://doi.org/10.1038/s41436-018-0290-3

* ittiwut-2020-epilepsy-abstract - Ittiwut C, Poonmaksatit S, Boonsimma P, et al. Novel de novo mutation substantiates ATP6V0C as a gene causing epilepsy with intellectual disability. Brain Dev. 2020;43(3):490-494. PMID: 33190975. DOI: https://doi.org/10.1016/j.braindev.2020.10.016

* rong-2025-dravet-abstract - Rong M, Marques PT, Ali QZ, et al. Variants in ATP6V0C are associated with Dravet-like developmental and epileptic encephalopathy. Epilepsia. 2025;66(6):2046-2052. PMID: 40085430. DOI: https://doi.org/10.1111/epi.18346

* liu-2008-rnf182-abstract - Liu QY, Lei JX, Sikorska M, Liu R. A novel brain-enriched E3 ubiquitin ligase RNF182 is up regulated in the brains of Alzheimer's patients and targets ATP6V0C for degradation. Mol Neurodegener. 2008;3:4. PMID: 18298843. DOI: https://doi.org/10.1186/1750-1326-3-4

* mauvezin-2015-bafilomycin-abstract - Mauvezin C, Neufeld TP. Bafilomycin A1 disrupts autophagic flux by inhibiting both V-ATPase-dependent acidification and Ca-P60A/SERCA-dependent autophagosome-lysosome fusion. Autophagy. 2015;11(8):1437-8. PMID: 26156798. DOI: https://doi.org/10.1080/15548627.2015.1066957

* abu-remaileh-2017-lysosomal-metabolomics-abstract - Abu-Remaileh M, Wyant GA, Kim C, et al. Lysosomal metabolomics reveals V-ATPase- and mTOR-dependent regulation of amino acid efflux from lysosomes. Science. 2017;358(6364):807-813. PMID: 29074583. DOI: https://doi.org/10.1126/science.aan6298

* meo-evoli-2015-e2f1-abstract - Meo-Evoli N, Almacellas E, Massucci FA, et al. V-ATPase: a master effector of E2F1-mediated lysosomal trafficking, mTORC1 activation and autophagy. Oncotarget. 2015;6(29):28057-70. PMID: 26356814. DOI: https://doi.org/10.18632/oncotarget.4812

* jin-2012-dopamine-abstract - Jin D, Muramatsu S, Shimizu N, et al. Dopamine release via the vacuolar ATPase V0 sector c-subunit, confirmed in N18 neuroblastoma cells, results in behavioral recovery in hemiparkinsonian mice. Neurochem Int. 2012;61(6):907-12. PMID: 22265874. DOI: https://doi.org/10.1016/j.neuint.2011.12.021

* kane-2003-assembly-regulation-abstract - Kane PM, Smardon AM. Assembly and regulation of the yeast vacuolar H+-ATPase. J Bioenerg Biomembr. 2003;35(4):313-21. PMID: 14635777. DOI: https://doi.org/10.1023/a:1025724814656

* ryan-2008-voa1-assembly-abstract - Ryan M, Graham LA, Stevens TH. Voa1p functions in V-ATPase assembly in the yeast endoplasmic reticulum. Mol Biol Cell. 2008;19(12):5131-42. PMID: 18799613. DOI: https://doi.org/10.1091/mbc.e08-06-0629

* davis-kaplan-2006-pkr1-abstract - Davis-Kaplan SR, Compton MA, Flannery AR, et al. PKR1 encodes an assembly factor for the yeast V-type ATPase. J Biol Chem. 2006;281(42):32025-35. PMID: 16926153. DOI: https://doi.org/10.1074/jbc.M606451200

* chung-2010-zebrafish-abstract - Chung AY, Kim MJ, Kim D, et al. Neuron-specific expression of atp6v0c2 in zebrafish CNS. Dev Dyn. 2010;239(9):2501-8. PMID: 20839327. DOI: https://doi.org/10.1002/dvdy.22383

* powell-2000-proton-pore-abstract - Powell B, Graham LA, Stevens TH. Molecular characterization of the yeast vacuolar H+-ATPase proton pore. J Biol Chem. 2000;275(31):23654-60. PMID: 10825180. DOI: https://doi.org/10.1074/jbc.M004440200


## Citations

1. abu-remaileh-2017-lysosomal-metabolomics-abstract.md
2. chung-2010-zebrafish-abstract.md
3. cipriano-2008-structure-regulation-abstract.md
4. colacurcio-2016-lysosomal-acidification-abstract.md
5. cotter-2015-insights-abstract.md
6. davis-kaplan-2006-pkr1-abstract.md
7. elfar-2011-synaptic-vesicle-abstract.md
8. elfar-2011-synaptic-vesicle-summary.md
9. forgac-1992-structure-function-abstract.md
10. huss-2002-concanamycin-binding-abstract.md
11. ittiwut-2020-epilepsy-abstract.md
12. jin-2012-dopamine-abstract.md
13. kane-2003-assembly-regulation-abstract.md
14. liu-2008-rnf182-abstract.md
15. mauvezin-2015-bafilomycin-abstract.md
16. meo-evoli-2015-e2f1-abstract.md
17. mucha-2018-microdeletion-abstract.md
18. oot-2017-breaking-up-abstract.md
19. powell-2000-proton-pore-abstract.md
20. rama-2018-neurotransmitter-abstract.md
21. roh-2018-cryoem-abstract.md
22. rong-2025-dravet-abstract.md
23. ryan-2008-voa1-assembly-abstract.md
24. vasanthakumar-2020-structure-roles-abstract.md
25. wang-2004-TM-interaction-abstract.md
26. xu-2019-bacterial-effector-abstract.md
27. xu-2019-bacterial-effector-summary.md
28. zhao-2015-cryoem-rotational-abstract.md
29. zhao-2015-cryoem-rotational-summary.md