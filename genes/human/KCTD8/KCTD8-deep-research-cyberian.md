---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-22T21:09:06.786273'
end_time: '2026-01-22T21:24:14.124126'
duration_seconds: 907.34
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: KCTD8
  gene_symbol: KCTD8
  uniprot_accession: Q6ZWB6
  protein_description: 'RecName: Full=BTB/POZ domain-containing protein KCTD8;'
  gene_info: Name=KCTD8;
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: BTB/POZ_dom. (IPR000210); H1_KCTD8. (IPR049904); SKP1/BTB/POZ_sf.
    (IPR011333); T1-type_BTB. (IPR003131); BTB_2 (PF02214)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 15
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q6ZWB6
- **Protein Description:** RecName: Full=BTB/POZ domain-containing protein KCTD8;
- **Gene Information:** Name=KCTD8;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** BTB/POZ_dom. (IPR000210); H1_KCTD8. (IPR049904); SKP1/BTB/POZ_sf. (IPR011333); T1-type_BTB. (IPR003131); BTB_2 (PF02214)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "KCTD8" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'KCTD8' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **KCTD8** (gene ID: KCTD8, UniProt: Q6ZWB6) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# KCTD8: A Comprehensive Review of Function, Localization, and Signaling Pathways

## Introduction and Summary

KCTD8 (Potassium Channel Tetramerization Domain Containing 8) is a 473-amino acid cytoplasmic protein encoded by the KCTD8 gene located on human chromosome 4p13 (UniProt: Q6ZWB6, NCBI Gene ID: 386617). The protein is characterized by an N-terminal BTB/POZ (bric-a-brac, tramtrak, and broad complex/poxvirus zinc finger) domain and a unique C-terminal domain architecture comprising H1 and H2 homology domains. The primary molecular function of KCTD8 is to serve as an auxiliary subunit of GABAB receptors, where it modulates receptor pharmacology and signaling kinetics[schwenk-2010-gabab-kctd-auxiliary-abstract]. As a member of the KCTD family clade F alongside KCTD12 and KCTD16, KCTD8 plays a specialized role in neural signaling by producing non-desensitizing receptor responses and facilitating the axonal trafficking of GABAB receptors to presynaptic terminals[seddik-2012-kctd-desensitization-abstract][ren-2022-kctd8-habenula-abstract].

The discovery of KCTD proteins as auxiliary subunits of GABAB receptors in 2010 resolved a long-standing puzzle in neuroscience: why cloned GABAB1/GABAB2 heteromeric receptors failed to reproduce the functional diversity observed in native receptors. Using functional proteomics, Schwenk and colleagues demonstrated that native GABAB receptors are high-molecular-mass complexes containing not only the principal GABAB1 and GABAB2 subunits but also tetrameric (now understood to be pentameric) assemblies of KCTD8, KCTD12, KCTD12b, or KCTD16[schwenk-2010-gabab-kctd-auxiliary-abstract]. This foundational work established that KCTD proteins determine the pharmacology and kinetics of GABAB receptor responses through their effects on agonist potency, G-protein signaling onset, and receptor desensitization.

## Structural Features and Domain Architecture

KCTD8 possesses a modular structural organization that is critical for its function as a GABAB receptor auxiliary subunit. The protein contains three major functional domains: the N-terminal BTB/POZ tetramerization domain (T1), the H1 homology domain, and uniquely among GABAB-associated KCTDs, an additional C-terminal H2 homology domain[seddik-2012-kctd-desensitization-abstract]. This three-domain architecture distinguishes KCTD8 from KCTD12 and KCTD12b, which lack the H2 domain, and has important functional consequences for receptor signaling.

The BTB domain of KCTD8 shares 33-43% sequence homology with the T1 domains of voltage-gated potassium (Kv) channels, from which the KCTD family derives its name[teng-2019-kctd-neurodevelopment-abstract]. However, despite this sequence similarity, KCTD BTB domains form pentameric rather than tetrameric assemblies. Structural studies using electron microscopy and crystallography have confirmed that KCTD8 forms stable pentamers through its BTB domain, and AlphaFold predictions support this oligomeric state as the biologically relevant form[esposito-2022-alphafold-kctd-abstract]. The pentameric BTB assembly creates an asymmetric arrangement that wraps around the C-terminal tail of the GABAB2 receptor subunit, with key phenylalanine residues making extensive contacts critical for binding[zheng-2019-kctd-structural-abstract].

The crystal structure of the human KCTD8 H1 domain has been solved at 2.80 angstrom resolution (PDB: 6G57)[pinkas-2018-kctd8-h1-structure-summary]. The H1 domain adopts a distinctive propeller-like architecture where five subunits assemble to generate a central cavity delimited by terminal beta-strands that constitute the blades of the propeller. Notably, the structure reveals an "sticky" nature of exposed beta-strands that can mediate additional protein-protein interactions. For KCTD8, KCTD12, and KCTD16, the BTB and CTD domains are separated by a large unstructured stretch, and the opening of the pentamer is functionally important as it favors binding to the GABAB2 receptor[esposito-2022-alphafold-kctd-abstract].

A defining structural feature of KCTD8 is its conserved H2 homology domain, which is not sequence-related to the H1 domain. The H2 domain functions as an antagonist of receptor desensitization, counteracting the desensitization-promoting activity of the H1 domain[seddik-2012-kctd-desensitization-abstract]. This molecular mechanism explains why KCTD8-containing GABAB receptors generate largely non-desensitizing responses, in contrast to KCTD12-containing receptors which exhibit pronounced desensitization due to the absence of an inhibitory H2 domain and the presence of a critical T/NFLEQ motif in their H1 domains.

## Primary Molecular Function: GABAB Receptor Auxiliary Subunit

The primary molecular function of KCTD8 is to serve as an auxiliary subunit of GABAB receptors, the principal G-protein-coupled receptors for gamma-aminobutyric acid (GABA), the main inhibitory neurotransmitter in the brain[schwenk-2010-gabab-kctd-auxiliary-abstract]. GABAB receptors regulate synaptic transmission and signal propagation by controlling the activity of voltage-gated calcium channels and G-protein-coupled inwardly rectifying potassium (GIRK/Kir3) channels. The incorporation of KCTD8 into GABAB receptor complexes fundamentally alters the pharmacological and kinetic properties of receptor signaling.

KCTD8 associates with the cytoplasmic C-terminal tail of the GABAB2 subunit as a pentameric assembly. This co-assembly increases agonist potency at GABAB receptors and markedly alters G-protein signaling by accelerating the onset of receptor responses[schwenk-2010-gabab-kctd-auxiliary-abstract]. The mechanism involves the H1 domain of KCTD proteins engaging Gbeta-gamma subunits with high affinity (approximately 185 nM for the related KCTD12), exhibiting remarkable cooperativity where only full 5:5 KCTD-Gbeta-gamma complexes form under substoichiometric conditions[zheng-2019-kctd-structural-abstract].

The critical functional distinction of KCTD8 compared to other GABAB-associated KCTDs lies in its effect on receptor desensitization. KCTD12 and KCTD12b produce strongly desensitizing receptor responses, while KCTD8 and KCTD16 generate largely non-desensitizing responses[seddik-2012-kctd-desensitization-abstract]. This difference arises from the presence of the H2 domain in KCTD8, which antagonizes the desensitization-promoting activity of the H1 domain. The H2 domain of KCTD8 effectively prevents the receptor desensitization that would otherwise be induced by the H1 domain, leading to sustained signaling upon prolonged agonist exposure.

Beyond homo-oligomeric assembly, KCTD proteins can form hetero-oligomers that confer unique kinetic properties to GABAB receptor responses. Fritzius and colleagues demonstrated that approximately two-thirds of KCTD16 proteins in the adult mouse hippocampus associate with KCTD12 to form hetero-oligomers[fritzius-2017-kctd-hetero-oligomers-abstract]. These hetero-oligomeric assemblies directly bind to both the receptor and the associated G-protein, producing moderately desensitizing potassium currents that differ from the strongly desensitizing or slowly deactivating responses produced by individual KCTD proteins. This capacity for hetero-oligomerization substantially increases the molecular and functional repertoire of native GABAB receptors.

## Cellular Localization and Tissue Distribution

KCTD8 is a cytoplasmic protein that functions at synaptic membranes through its association with membrane-anchored GABAB receptor complexes. Unlike integral membrane proteins, KCTD8 lacks transmembrane domains and instead localizes to synaptic compartments by binding to the intracellular C-terminal tail of the GABAB2 subunit[schwenk-2010-gabab-kctd-auxiliary-abstract]. Gene Ontology annotations predict that KCTD8 is active at both postsynaptic and presynaptic regions, specifically localizing to the postsynaptic membrane, presynaptic membrane, and presynaptic active zone membrane structures.

The tissue distribution of KCTD8 is notably restricted compared to other GABAB-associated KCTDs. While KCTD12 and KCTD16 exhibit widespread expression throughout the brain, KCTD8 and KCTD12b have more limited expression patterns[metz-2011-kctd-distribution-brain-abstract]. In the adult mouse brain, KCTD8 is strongly expressed in the medial habenula (MHb) and, to a lesser extent, in interpeduncular nucleus (IPN) neurons. Outside these regions, KCTD8 shows only weak expression in the cerebellum and superior colliculus. This restricted expression pattern suggests that KCTD8 serves specialized functions in particular neural circuits rather than broadly modulating GABAB signaling throughout the brain.

Human Protein Atlas data confirm that KCTD8 shows cytoplasmic expression in the brain, with the highest levels in the cerebellum (16.9 nTPM), followed by basal ganglia (9.3 nTPM), spinal cord (7.8 nTPM), and cerebral cortex (7.2 nTPM). The gene is classified as "group enriched" with specificity for brain and retina tissues, achieving a Tau specificity score of 0.83. Outside the nervous system, KCTD8 expression is minimal, with low levels detected in the retina (6.3 nTPM) and thyroid gland (2.8 nTPM), while most other tissues show undetectable or negligible expression.

Within the medial habenula, KCTD8 co-localizes with cholinergic markers and GABAB receptors. Immunohistochemistry studies have demonstrated the distribution of KCTD8 in the MHb of wild-type mice, with immunoreactivities showing co-localization with choline acetyltransferase (ChAT), confirming expression in cholinergic neurons[turecek-2021-kctd8-cav23-abstract]. In ventral MHb terminals projecting to the rostral IPN, KCTD8, KCTD12b, and Cav2.3 calcium channels co-localize at presynaptic active zones, with over 97% of Cav2.3-positive active zones also containing KCTD8 and GABAB1.

## Signaling Pathways and Mechanisms

KCTD8 participates in GABAB receptor signaling through the regulation of G-protein-coupled inwardly rectifying potassium (GIRK) channels and voltage-gated calcium channels. The central mechanism involves the sequestration of Gbeta-gamma subunits following GABAB receptor activation, which controls the temporal dynamics of downstream effector activation[zheng-2019-kctd-structural-abstract].

Upon GABAB receptor activation by GABA, the heterotrimeric G-protein (Gi/o) bound to the receptor dissociates into Galpha-GDP and Gbeta-gamma subunits. The released Gbeta-gamma directly activates GIRK channels, producing inhibitory potassium currents that hyperpolarize neurons. KCTD proteins tethered to the receptor's cytoplasmic tail can engage and sequester these Gbeta-gamma subunits through their H1 domains, effectively stripping them from GIRK channels through higher-affinity binding[zheng-2019-kctd-structural-abstract]. This Gbeta-gamma sequestration mechanism enables rapid desensitization of GIRK currents following receptor activation, providing tight temporal control of signaling that is not achievable with the slower beta-arrestin pathway used to desensitize most GPCRs.

However, KCTD8 produces distinct signaling outcomes compared to desensitizing KCTDs like KCTD12. The presence of the H2 domain in KCTD8 antagonizes desensitization, resulting in sustained GIRK channel activation during prolonged agonist exposure[seddik-2012-kctd-desensitization-abstract]. This means that KCTD8-containing GABAB receptors generate non-desensitizing or slowly deactivating potassium currents, maintaining inhibitory signaling over extended periods.

Beyond modulating GIRK channel kinetics, KCTD8 has emerged as a direct regulator of voltage-gated calcium channels at presynaptic terminals. Turecek and colleagues demonstrated that KCTD8 and KCTD12b, but not KCTD12, bind directly to Cav2.3 (R-type) calcium channels at the plasma membrane[turecek-2021-kctd8-cav23-abstract]. Importantly, KCTD8 potentiates Cav2.3-mediated calcium currents, with significant increases in current density observed in cells co-expressing KCTD8 compared to control cells. This potentiation of presynaptic calcium channels by KCTD8 increases neurotransmitter release probability, representing a GABAB receptor-independent function of this auxiliary subunit.

The functional consequences of KCTD8-Cav2.3 interaction are evident in the MHb-IPN pathway. KCTD8 localizes to the peri-synaptic region with lower particle densities inside the active zone proper. In KCTD12b knockout mice, a compensatory mechanism increases KCTD8 density in the active zone approximately twofold, correlating with enhanced release probability[turecek-2021-kctd8-cav23-abstract]. This finding reveals that KCTD8 can modulate synaptic transmission through direct effects on calcium channel function, independent of its role in GABAB receptor desensitization.

KCTD8 also plays a critical role in the axonal trafficking of GABAB receptors to presynaptic terminals. Ren and colleagues demonstrated that KCTD8 and KCTD12 facilitate GABAB receptor expression in axonal terminals of habenula cholinergic neurons[ren-2022-kctd8-habenula-abstract]. Knockout of KCTD8/12/16 substantially reduced GABAB-mediated potentiation of glutamate release, an effect specific to axonal terminals rather than neuronal cell bodies. Overexpression of either KCTD8 or KCTD12 reversed these reductions, confirming the essential role of these auxiliary subunits in presynaptic GABAB receptor function.

## Role in Neural Circuits and Behavior

The restricted expression of KCTD8 in the medial habenula and interpeduncular nucleus positions it as a key regulator of the habenulo-interpeduncular pathway, a brain circuit involved in aversion, fear, and reward processing. The medial habenula receives input from limbic forebrain structures and projects via the fasciculus retroflexus to the interpeduncular nucleus, which in turn influences midbrain monoaminergic systems. GABAB receptors in this pathway produce unusual excitatory effects by enhancing glutamate release from MHb terminals, and KCTD8 is essential for this presynaptic excitation[ren-2022-kctd8-habenula-abstract].

Studies in mice have demonstrated that KCTD8/12 auxiliary subunits modulate the expression and function of GABAB receptors in habenula cholinergic neurons, thereby affecting aversion memory processing in adult mice[ren-2022-kctd8-habenula-abstract]. The pathway modulates aversion-related memory processes, and the isoform-specific roles of KCTD proteins in enriching axonal GABAB receptor expression have direct impacts on fear memory formation.

## KCTD8 and Brain Development

A genome-wide association study (GWAS) identified KCTD8 as a genetic modifier of brain size in human populations, particularly in the context of adverse intrauterine environments[paus-2012-kctd8-brain-gwas-abstract]. Paus and colleagues found that genetic variation in the KCTD8 locus (rs716890) is significantly associated with brain size in female adolescents (P = 5.40 x 10^-09). Remarkably, the KCTD8 locus showed a strong gene-environment interaction with prenatal exposure to maternal cigarette smoking (PEMCS), explaining up to 21% of variance in cortical area and cortical folding in exposed girls. This association was replicated in an independent cohort using head circumference measurements at age 7 years.

The proposed mechanism for this gene-environment interaction involves KCTD8's potential role in modulating hypoxia-induced loss of intracellular potassium, which could promote apoptosis in the developing brain[paus-2012-kctd8-brain-gwas-abstract]. During the first trimester, such an effect would reduce the number of progenitor cells, with exponential consequences on the final number of neurons and cortical area. During the second and third trimesters, this mechanism could lead to a reduction of postmitotic neurons. Notably, this interaction was observed exclusively in female offspring, suggesting sex-specific effects of KCTD8 on brain development that may be related to differential androgen exposure or other sex-linked factors.

This GWAS finding suggests that KCTD8 may have developmental functions beyond its established role as a GABAB receptor auxiliary subunit, potentially involving regulation of cellular potassium homeostasis or apoptosis during brain development. The sex-specificity and environmental interaction of this association highlight the complex interplay between genetic variation and environmental factors in shaping brain structure.

## Cancer Biology: A Non-Canonical Function

Beyond its well-characterized neuronal functions, KCTD8 has recently been identified as a tumor suppressor in hepatocellular carcinoma (HCC), revealing an unexpected role in cancer biology[zhou-2024-kctd8-cancer-abstract]. Zhou and colleagues found that KCTD8 is epigenetically silenced through promoter DNA methylation in 44.83% of HCC cases, and this methylation pattern serves as an independent poor prognostic marker.

The tumor-suppressive function of KCTD8 in HCC operates through inhibition of the PI3K/AKT/mTOR signaling pathway, which is distinct from its neuronal function as a GABAB receptor auxiliary subunit. Reintroduction of KCTD8 into cancer cells suppresses proliferation, migration, and invasion while inducing apoptosis both in vitro and in vivo. The mechanism involves physical interaction between KCTD8 and IMPDH2 (inosine monophosphate dehydrogenase 2), which is involved in PI3K signaling. KCTD8 expression reduces levels of PI3K110beta, phospho-AKT, and phospho-mTOR, indicating inhibition of this oncogenic signaling cascade[zhou-2024-kctd8-cancer-abstract].

This finding expands the functional repertoire of KCTD8 beyond neuroscience and suggests that KCTD proteins may have tissue-specific functions determined by their local interaction partners. The epigenetic silencing of KCTD8 in cancer also highlights potential therapeutic strategies targeting methylation to restore KCTD8 expression in malignancies.

## Evolutionary and Family Context

KCTD8 belongs to a family of 25-26 KCTD proteins in humans, which share the defining BTB/POZ domain but exhibit diverse functions across different cellular contexts[teng-2019-kctd-neurodevelopment-abstract]. Within this family, KCTD8, KCTD12, and KCTD16 constitute clade F, which shares the specialized function of associating with GABAB receptors. KCTD12b is found in mice but not humans. The phylogenetic relationship among clade F members is reflected in their shared domain architecture, with KCTD8 and KCTD16 both possessing the H2 domain while KCTD12 and KCTD12b lack this element.

The evolutionary conservation of KCTD8 across mammals suggests important physiological functions. Mouse Kctd8 shows 476 amino acids compared to human KCTD8's 473 amino acids, with highly conserved domain architecture. The restricted expression pattern of KCTD8 in specific brain nuclei is also conserved between species, indicating that specialized roles in habenular circuitry represent an evolutionarily maintained function.

The nomenclature "potassium channel tetramerization domain" reflects the original observation that KCTD BTB domains share sequence homology with T1 domains of Kv channels. However, it is now clear that KCTD proteins do not directly associate with or regulate potassium channels in the manner implied by this name. Instead, the BTB domains mediate pentamerization of KCTD subunits and interaction with partner proteins such as GABAB2 or Cullin3 E3 ubiquitin ligases[esposito-2022-alphafold-kctd-abstract].

## Open Questions

Several important questions remain regarding KCTD8 function and regulation:

1. **Hetero-oligomerization specificity**: While KCTD proteins can form hetero-oligomers, the rules governing which combinations form in vivo and how these are regulated remain unclear. Whether KCTD8 preferentially hetero-oligomerizes with KCTD12 or KCTD16 in the medial habenula, and how this affects signaling, requires further investigation.

2. **Developmental regulation**: The expression of KCTD8 changes during brain development, but the functional significance of these changes and the transcriptional mechanisms controlling KCTD8 expression are not well understood.

3. **GABAB receptor-independent functions**: The discovery that KCTD8 directly binds and potentiates Cav2.3 calcium channels raises questions about other potential binding partners and functions that operate independently of GABAB receptors.

4. **Cancer biology mechanisms**: The tumor-suppressive function of KCTD8 through IMPDH2 interaction and PI3K pathway inhibition requires further mechanistic characterization. Whether this represents a tissue-specific function or a more general property of KCTD8 in non-neuronal cells remains to be determined.

5. **Therapeutic potential**: Given the role of KCTD proteins in modulating GABAB receptor pharmacology and their association with neuropsychiatric disorders, whether KCTD8-selective modulators could have therapeutic applications warrants exploration.

6. **Structural dynamics**: How the H2 domain mechanistically antagonizes H1-mediated desensitization at the molecular level remains incompletely understood and would benefit from additional structural studies of full-length KCTD8 in complex with GABAB receptors.

7. **Relationship to habenular dysfunction**: Given the strong expression of KCTD8 in the medial habenula and the role of this structure in depression, anxiety, and addiction, whether KCTD8 variants or expression changes contribute to these disorders merits investigation.

## References

- **schwenk-2010-gabab-kctd-auxiliary-abstract**: Schwenk J, Metz M, Zolles G, et al. (2010) Native GABA(B) receptors are heteromultimers with a family of auxiliary subunits. Nature 465(7295):231-235. DOI: 10.1038/nature08964. PMID: 20400944.

- **seddik-2012-kctd-desensitization-abstract**: Seddik R, Jungblut SP, Silander OK, et al. (2012) Opposite Effects of KCTD Subunit Domains on GABAB Receptor-mediated Desensitization. Journal of Biological Chemistry 287(47):39869-39877. DOI: 10.1074/jbc.M112.412767. PMID: 23035123.

- **zheng-2019-kctd-structural-abstract**: Zheng S, Abreu N, Levitz J, Kruse AC. (2019) Structural basis for KCTD-mediated rapid desensitization of GABAB signaling. Nature 567(7746):127-131. DOI: 10.1038/s41586-019-0990-0. PMID: 30814734.

- **metz-2011-kctd-distribution-brain-abstract**: Metz M, Gassmann M, Fakler B, Schaeren-Wiemers N, Bettler B. (2011) Distribution of the auxiliary GABAB receptor subunits KCTD8, 12, 12b, and 16 in the mouse brain. Journal of Comparative Neurology 519(8):1435-1454. DOI: 10.1002/cne.22610. PMID: 21452234.

- **teng-2019-kctd-neurodevelopment-abstract**: Teng X, Aouacheria A, Lionnard L, et al. (2019) KCTD: A new gene family involved in neurodevelopmental and neuropsychiatric disorders. CNS Neuroscience & Therapeutics 25(7):887-902. DOI: 10.1111/cns.13156. PMID: 31111690.

- **ren-2022-kctd8-habenula-abstract**: Ren Y, Liu Y, Zheng S, Luo M. (2022) KCTD8 and KCTD12 Facilitate Axonal Expression of GABAB Receptors in Habenula Cholinergic Neurons. Journal of Neuroscience 42(9):1648-1665. DOI: 10.1523/JNEUROSCI.1676-21.2021. PMID: 35017224.

- **fritzius-2017-kctd-hetero-oligomers-abstract**: Fritzius T, Turecek R, Seddik R, et al. (2017) KCTD Hetero-oligomers Confer Unique Kinetic Properties on Hippocampal GABAB Receptor-Induced K+ Currents. Journal of Neuroscience 37(5):1162-1175. DOI: 10.1523/JNEUROSCI.2181-16.2016. PMID: 28003345.

- **zhou-2024-kctd8-cancer-abstract**: Zhou J, Zhang M, Gao A, Herman JG, Guo M. (2024) Epigenetic silencing of KCTD8 promotes hepatocellular carcinoma growth by activating PI3K/AKT signaling. Epigenomics 16(13):929-944. DOI: 10.1080/17501911.2024.2370590. PMID: 39016152.

- **turecek-2021-kctd8-cav23-abstract**: Turecek R, Fritzius T, Bhumbra SA, Gassmann M, Bettler B. (2021) GABAB receptor auxiliary subunits modulate Cav2.3-mediated release from medial habenula terminals. eLife 10:e68274. DOI: 10.7554/eLife.68274. PMID: 34018460.

- **pinkas-2018-kctd8-h1-structure-summary**: Pinkas DM, von Delft F, Arrowsmith CH, Bullock AN. (2018) Structure of the H1 domain of human KCTD8. PDB ID: 6G57. Released 2019-03-20.

- **esposito-2022-alphafold-kctd-abstract**: Esposito L, Balasco N, Ruggiero A, Berisio R, Vitagliano L. (2022) Alphafold Predictions Provide Insights into the Structural Features of the Functional Oligomers of All Members of the KCTD Family. International Journal of Molecular Sciences 23(21):13346. DOI: 10.3390/ijms232113346.

- **paus-2012-kctd8-brain-gwas-abstract**: Paus T, Bernard M, Chakravarty MM, et al. (2012) KCTD8 Gene and Brain Growth in Adverse Intrauterine Environment: A Genome-wide Association Study. Cerebral Cortex 22(11):2634-2642. DOI: 10.1093/cercor/bhr350. PMID: 22156575.


## Citations

1. esposito-2022-alphafold-kctd-abstract.md
2. fritzius-2017-kctd-hetero-oligomers-abstract.md
3. metz-2011-kctd-distribution-brain-abstract.md
4. paus-2012-kctd8-brain-gwas-abstract.md
5. pinkas-2018-kctd8-h1-structure-summary.md
6. ren-2022-kctd8-habenula-abstract.md
7. schwenk-2010-gabab-kctd-auxiliary-abstract.md
8. schwenk-2010-gabab-kctd-auxiliary-summary.md
9. seddik-2012-kctd-desensitization-abstract.md
10. seddik-2012-kctd-desensitization-summary.md
11. teng-2019-kctd-neurodevelopment-abstract.md
12. turecek-2021-kctd8-cav23-abstract.md
13. zheng-2019-kctd-structural-abstract.md
14. zheng-2019-kctd-structural-summary.md
15. zhou-2024-kctd8-cancer-abstract.md