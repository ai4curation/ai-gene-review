---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-08T18:24:30.038915'
end_time: '2026-09-08T18:32:11.072478'
duration_seconds: 461.03
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: IKKepsilon
  gene_symbol: IKKepsilon
  uniprot_accession: Q9V3Y8
  protein_description: 'SubName: Full=I-kappaB kinase epsilon, isoform B {ECO:0000313|EMBL:AAN11082.1};
    SubName: Full=I-kappaB kinase epsilon, isoform C {ECO:0000313|EMBL:AAF53911.2};
    EC=2.7.11.1 {ECO:0000313|EMBL:AAF53911.2, ECO:0000313|EMBL:AAN11082.1};'
  gene_info: Name=IKKepsilon {ECO:0000313|EMBL:AAF53911.2, ECO:0000313|FlyBase:FBgn0086657};
    Synonyms=38D.31 {ECO:0000313|EMBL:AAF53911.2}, APTX7 {ECO:0000313|EMBL:AAF53911.2},
    DIK2 {ECO:0000313|EMBL:AAF53911.2}, Dik2 {ECO:0000313|EMBL:AAF53911.2}, dik2 {ECO:0000313|EMBL:AAF53911.2},
    dIKK {ECO:0000313|EMBL:AAF53911.2}, dIKKepsilon {ECO:0000313|EMBL:AAF53911.2},
    Dmel\CG2615 {ECO:0000313|EMBL:AAF53911.2}, Dmik2 {ECO:0000313|EMBL:AAF53911.2},
    DmIKKepsilon {ECO:0000313|EMBL:AAF53911.2}, DmIKKepsilon/dIK2 {ECO:0000313|EMBL:AAF53911.2},
    dTBK1 {ECO:0000313|EMBL:AAF53911.2}, IK2 {ECO:0000313|EMBL:AAF53911.2}, Ik2 {ECO:0000313|EMBL:AAF53911.2},
    ik2 {ECO:0000313|EMBL:AAF53911.2}, Ik2/DmIKK {ECO:0000313|EMBL:AAF53911.2}, IKK
    {ECO:0000313|EMBL:AAF53911.2}, ikkepsilon {ECO:0000313|EMBL:AAF53911.2}, l(2)38Ea
    {ECO:0000313|EMBL:AAF53911.2}; ORFNames=CG2615 {ECO:0000313|EMBL:AAF53911.2, ECO:0000313|FlyBase:FBgn0086657},
    Dmel_CG2615 {ECO:0000313|EMBL:AAF53911.2};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Not specified in UniProt
  protein_domains: IKK. (IPR051180); Kinase-like_dom_sf. (IPR011009); Prot_kinase_dom.
    (IPR000719); Protein_kinase_ATP_BS. (IPR017441); TBK1_CC1. (IPR041309)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 19
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: IKKepsilon-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q9V3Y8
- **Protein Description:** SubName: Full=I-kappaB kinase epsilon, isoform B {ECO:0000313|EMBL:AAN11082.1}; SubName: Full=I-kappaB kinase epsilon, isoform C {ECO:0000313|EMBL:AAF53911.2}; EC=2.7.11.1 {ECO:0000313|EMBL:AAF53911.2, ECO:0000313|EMBL:AAN11082.1};
- **Gene Information:** Name=IKKepsilon {ECO:0000313|EMBL:AAF53911.2, ECO:0000313|FlyBase:FBgn0086657}; Synonyms=38D.31 {ECO:0000313|EMBL:AAF53911.2}, APTX7 {ECO:0000313|EMBL:AAF53911.2}, DIK2 {ECO:0000313|EMBL:AAF53911.2}, Dik2 {ECO:0000313|EMBL:AAF53911.2}, dik2 {ECO:0000313|EMBL:AAF53911.2}, dIKK {ECO:0000313|EMBL:AAF53911.2}, dIKKepsilon {ECO:0000313|EMBL:AAF53911.2}, Dmel\CG2615 {ECO:0000313|EMBL:AAF53911.2}, Dmik2 {ECO:0000313|EMBL:AAF53911.2}, DmIKKepsilon {ECO:0000313|EMBL:AAF53911.2}, DmIKKepsilon/dIK2 {ECO:0000313|EMBL:AAF53911.2}, dTBK1 {ECO:0000313|EMBL:AAF53911.2}, IK2 {ECO:0000313|EMBL:AAF53911.2}, Ik2 {ECO:0000313|EMBL:AAF53911.2}, ik2 {ECO:0000313|EMBL:AAF53911.2}, Ik2/DmIKK {ECO:0000313|EMBL:AAF53911.2}, IKK {ECO:0000313|EMBL:AAF53911.2}, ikkepsilon {ECO:0000313|EMBL:AAF53911.2}, l(2)38Ea {ECO:0000313|EMBL:AAF53911.2}; ORFNames=CG2615 {ECO:0000313|EMBL:AAF53911.2, ECO:0000313|FlyBase:FBgn0086657}, Dmel_CG2615 {ECO:0000313|EMBL:AAF53911.2};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** IKK. (IPR051180); Kinase-like_dom_sf. (IPR011009); Prot_kinase_dom. (IPR000719); Protein_kinase_ATP_BS. (IPR017441); TBK1_CC1. (IPR041309)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "IKKepsilon" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'IKKepsilon' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **IKKepsilon** (gene ID: IKKepsilon, UniProt: Q9V3Y8) in DROME.

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
- **UniProt Accession:** Q9V3Y8
- **Protein Description:** SubName: Full=I-kappaB kinase epsilon, isoform B {ECO:0000313|EMBL:AAN11082.1}; SubName: Full=I-kappaB kinase epsilon, isoform C {ECO:0000313|EMBL:AAF53911.2}; EC=2.7.11.1 {ECO:0000313|EMBL:AAF53911.2, ECO:0000313|EMBL:AAN11082.1};
- **Gene Information:** Name=IKKepsilon {ECO:0000313|EMBL:AAF53911.2, ECO:0000313|FlyBase:FBgn0086657}; Synonyms=38D.31 {ECO:0000313|EMBL:AAF53911.2}, APTX7 {ECO:0000313|EMBL:AAF53911.2}, DIK2 {ECO:0000313|EMBL:AAF53911.2}, Dik2 {ECO:0000313|EMBL:AAF53911.2}, dik2 {ECO:0000313|EMBL:AAF53911.2}, dIKK {ECO:0000313|EMBL:AAF53911.2}, dIKKepsilon {ECO:0000313|EMBL:AAF53911.2}, Dmel\CG2615 {ECO:0000313|EMBL:AAF53911.2}, Dmik2 {ECO:0000313|EMBL:AAF53911.2}, DmIKKepsilon {ECO:0000313|EMBL:AAF53911.2}, DmIKKepsilon/dIK2 {ECO:0000313|EMBL:AAF53911.2}, dTBK1 {ECO:0000313|EMBL:AAF53911.2}, IK2 {ECO:0000313|EMBL:AAF53911.2}, Ik2 {ECO:0000313|EMBL:AAF53911.2}, ik2 {ECO:0000313|EMBL:AAF53911.2}, Ik2/DmIKK {ECO:0000313|EMBL:AAF53911.2}, IKK {ECO:0000313|EMBL:AAF53911.2}, ikkepsilon {ECO:0000313|EMBL:AAF53911.2}, l(2)38Ea {ECO:0000313|EMBL:AAF53911.2}; ORFNames=CG2615 {ECO:0000313|EMBL:AAF53911.2, ECO:0000313|FlyBase:FBgn0086657}, Dmel_CG2615 {ECO:0000313|EMBL:AAF53911.2};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** IKK. (IPR051180); Kinase-like_dom_sf. (IPR011009); Prot_kinase_dom. (IPR000719); Protein_kinase_ATP_BS. (IPR017441); TBK1_CC1. (IPR041309)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "IKKepsilon" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'IKKepsilon' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **IKKepsilon** (gene ID: IKKepsilon, UniProt: Q9V3Y8) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Drosophila melanogaster* IKKepsilon/Ik2 (UniProt Q9V3Y8)

## Executive conclusion

The requested protein is correctly identified as the *Drosophila melanogaster* noncanonical IKK-family kinase encoded by **CG2615**, most often called **Ik2**, **IKKepsilon/DmIKKε**, or **dTBK1**. It must not be confused with either (i) *Drosophila* **Ird5/DmIKKβ**, the canonical IKK required for Relish/NF-κB antibacterial signaling, or (ii) human **IKBKE** or **TBK1**. Fly Ik2 is slightly more similar in sequence to human TBK1 (35.5% identity) than to human IKBKE (34.5%), but these names denote homology rather than biochemical identity. Human IKBKE/TBK1 findings were therefore not transferred automatically to Q9V3Y8. (shapiro2006drosophilaik2a pages 1-2, dubinbar2008thedrosophilaikkrelated pages 1-2, lu2020ik2tbk1andhookdynein pages 2-3)

The best-supported primary function is that of an intracellular **protein serine/threonine kinase** coordinating polarized cytoskeletal and membrane-trafficking events. Its clearest direct substrate is the coiled-coil protein **Spindle-F (Spn-F)**. Through Spn-F-containing complexes, Ik2 regulates microtubule/dynein organization, localized mRNA transport, Rab11 activation, endosomal traffic, cell elongation, and developmental dendrite pruning. A second major pathway involves kinase-dependent loss of **DIAP1**, permitting spatially limited nonapoptotic caspase activity and F-actin remodeling; however, DIAP1 has not been established as conclusively as a directly phosphorylated substrate. (dubinbar2008thedrosophilaikkrelated pages 1-2, dubinbar2008thedrosophilaikkrelated pages 2-4, lin2020rab11activationby pages 1-2, lin2015spindlefisthe pages 17-18)

| Annotation category | Best-supported conclusion | Evidence type | Key caveat |
|---|---|---|---|
| Identity and nomenclature | Q9V3Y8 corresponds to *Drosophila melanogaster* CG2615, commonly called **Ik2**, **IKKepsilon/DmIKKε**, or **dTBK1**. It is distinct from **Ird5/DmIKKβ**, the canonical fly IKK involved in Relish/NF-κB antibacterial signaling. Ik2 shares greater sequence identity with human TBK1 (35.5%) and IKBKE (34.5%) than with human IKKβ (18.7%). (shapiro2006drosophilaik2a pages 1-2, dubinbar2008thedrosophilaikkrelated pages 1-2, lu2020ik2tbk1andhookdynein pages 2-3) | Gene-specific genetics, sequence comparison, and pathway discrimination | “dTBK1” and “IKKepsilon” denote homology, not biochemical identity with either human TBK1 or IKBKE; mammalian findings cannot automatically be assigned to Q9V3Y8. |
| Catalytic class and domains | Ik2 is a noncanonical IKK-family **protein serine/threonine kinase** (EC 2.7.11.1) with an N-terminal protein-kinase domain and a C-terminal coiled-coil regulatory region consistent with the TBK1/IKKε branch. Kinase-domain substitutions and kinase-dead K41A/G250D variants disrupt biological function. (shapiro2006drosophilaik2a pages 1-2, lee2009drosophilaikkrelatedkinase pages 2-2) | Conserved-domain annotation, mutant alleles, and kinase-dead rescue/dominant-negative experiments | No gene-specific kinetic constants, ATP affinity, substrate consensus sequence, or comprehensive phosphoproteomic specificity map has been established. |
| Direct substrate: Spindle-F | **Spn-F is the best-established direct regulatory substrate.** Ik2 binds Spn-F directly, with reported binding affinity *K*D ≈ 407.2 nM, and induces phosphatase-reversible phosphorylation. Phosphorylation reduces Spn-F self-association and enables redistribution of Ik2–Spn-F–dynein complexes during dendrite pruning. (dubinbar2008thedrosophilaikkrelated pages 2-4, lin2015spindlefisthe pages 17-18) | Yeast two-hybrid, co-immunoprecipitation, direct binding kinetics, electrophoretic mobility/phosphatase assays, and phosphomutant genetics | The exact physiological phosphosite set and site-specific catalytic parameters remain incompletely resolved; phosphorylation does not target Spn-F for degradation. |
| DIAP1/caspase pathway | Ik2 binds DIAP1 and promotes its **kinase-dependent degradation**, relieving caspase inhibition and enabling spatially limited, nonapoptotic caspase activity that regulates F-actin-dependent morphogenesis. (lin2015spindlefisthe pages 17-18, dubinbar2008thedrosophilaikkrelated pages 1-2) | Genetic interactions, protein-association/degradation studies, kinase dependence, and nonlethal morphogenesis phenotypes | DIAP1 is a strong pathway target, but available evidence does not conclusively establish it as a directly phosphorylated Ik2 substrate or define a phosphosite. |
| Subcellular localization | Ik2 is primarily intracellular and context-dependent: it colocalizes with Spn-F at the **anterior ring of the oocyte**, in **punctate nurse-cell structures**, and in cytoplasmic puncta in S2/S2R+ cells. Ik2 and Spn-F are mutually required for correct oocyte localization. (dubinbar2008thedrosophilaikkrelated pages 1-2, dubinbar2008thedrosophilaikkrelated pages 2-4) | Immunofluorescence and fluorescent-protein colocalization in ovaries and cultured cells | Localization is dynamic and developmentally regulated; no single constitutive organelle assignment or extracellular role is supported. |
| Oogenesis and mRNA localization | Ik2 organizes cortical actin and microtubule minus ends needed for **gurken**, **oskar**, and, less strongly, **bicoid** mRNA localization. Loss of function produces ventralized or bicaudal embryos and abnormal microtubule accumulation near the oocyte nucleus. (shapiro2006drosophilaik2a pages 1-2, shapiro2006drosophilaik2a pages 7-8) | Maternal-mutant genetics, RNA localization assays, cytoskeletal imaging, and embryonic-patterning phenotypes | The localized mRNAs and cytoskeletal components are downstream cargo/processes, not demonstrated direct kinase substrates. The pathway is NF-κB independent. |
| F-actin morphogenesis and cell elongation | Ik2 controls the fidelity of polarized F-actin assembly in elongated bristles, arista laterals, and tracheal terminal cells; loss causes abnormal branching, whereas excess Ik2 destabilizes F-actin structures. (dubinbar2008thedrosophilaikkrelated pages 1-2) | Loss- and gain-of-function genetics, cytoskeletal imaging, and DIAP1/DRONC dosage modification | The precise immediate cytoskeletal substrate is unresolved, and some effects may be mediated indirectly through DIAP1 and nonapoptotic caspases. |
| Dendrite pruning | Temporally activated Ik2 is necessary and sufficient to initiate proximal dendrite severing in class-IV sensory neurons, acting through Spn-F, dynein, and microtubule-remodeling machinery. In controls, 77% of ddaC neurons had at least one severed dendrite by 5 h after puparium formation (*n*=120), and 100% had removed severed dendrites by 16 h (*n*=75). (lee2009drosophilaikkrelatedkinase pages 2-2, lee2009drosophilaikkrelatedkinase pages 1-2, lin2015spindlefisthe pages 2-3) | RNAi, kinase-dead mutants, mosaic analysis, temporal overexpression, live imaging, and quantitative developmental phenotyping | Ik2 is not required for initial larval dendrite formation, and DIAP1/caspase signaling alone does not fully explain the pruning mechanism. |
| Rab11 and endosomal traffic | Ik2 kinase activity and Ik2–Spn-F–Rab11 complex formation promote the active GTP-bound state of **Rab11**, linking the pathway to recycling-endosome function during dendrite pruning. Ik2–Spn-F also connects genetically and physically to Hook/dynein-mediated early-endosome transport. (lu2020ik2tbk1andhookdynein pages 1-2, lu2020ik2tbk1andhookdynein pages 2-3, lin2020rab11activationby pages 1-2) | Genetic epistasis and rescue, live imaging, protein-complex assays, Rab11 activation assays, and interactome analysis | Rab11 is activated downstream of or parallel to Ik2; it has not been shown to be a direct phosphorylation substrate of Ik2. Early- and recycling-endosome findings arise from related but not necessarily identical cellular contexts. |
| Disease-model application | In a fly model expressing FTD-associated **CHMP2BIntron5**, partial Ik2 loss enhances retinal toxicity, while neuronal Ik2 overexpression suppresses synaptic and motor phenotypes. This makes the Ik2–Spn-F–Hook/dynein axis a functional probe of endosomal dysfunction relevant to frontotemporal dementia. (lu2020ik2tbk1andhookdynein pages 1-2, lu2020ik2tbk1andhookdynein pages 2-3) | In vivo modifier screen, RNAi/heterozygous loss, overexpression rescue, neuromuscular-junction analysis, and interactomics | This is a preclinical *Drosophila* disease model, not a therapeutic implementation; human relevance is inferential and may relate more closely to TBK1 than to IKBKE. |
| 2023–2024 research status | Targeted searches found **no substantive 2023–2024 primary study specifically focused on Q9V3Y8/CG2615**. The latest directly relevant mechanistic work identified here is the 2020 Rab11 and CHMP2B/endosomal-transport research. (lu2020ik2tbk1andhookdynein pages 1-2, lin2020rab11activationby pages 1-2) | Accession- and alias-aware literature assessment | Absence from the retrieved literature is not proof that no publication exists; recent mammalian TBK1/IKBKE studies were deliberately excluded because they concern different proteins and organisms. |


*Table: Evidence-weighted annotation of Drosophila Ik2/IKKepsilon (Q9V3Y8), separating direct biochemical findings from pathway inference and ortholog-based interpretation. The table highlights substrates, localization, pathways, quantitative phenotypes, disease-model use, and research gaps.*

## 1. Identity and domain verification

The literature describes two IKK-family proteins in *Drosophila*. **Ird5/DmIKKβ** performs the canonical immune role involving Relish activation, whereas **Ik2/CG2615** acts principally in NF-κB-independent cytoskeletal and trafficking pathways. Maternal removal experiments and mutant phenotypes further show that Ik2 is not the kinase responsible for degradation of the fly IκB protein Cactus. Thus, the UniProt description and the gene-specific literature refer to the same *D. melanogaster* protein, but the label “I-kappaB kinase epsilon” is potentially misleading if interpreted as evidence that Cactus/IκB is its physiological substrate. (shapiro2006drosophilaik2a pages 1-2, dubinbar2008thedrosophilaikkrelated pages 1-2, shapiro2006drosophilaik2a pages 7-8)

The supplied InterPro assignments—protein-kinase domain, kinase ATP-binding site, kinase-like superfamily, IKK family, and TBK1-like CC1 region—accord with the literature’s placement of Ik2 in the noncanonical TBK1/IKKε branch. Functional support comes from six recessive-lethal kinase-domain alleles, including G19D, N69I, G109A, D160N, G250D, and F297I, and from kinase-dead K41A and G250D constructs that disrupt Ik2-dependent processes. Most mutant animals die as first-instar larvae, with adult escapers occurring at less than 1% under favorable conditions. (shapiro2006drosophilaik2a pages 1-2, lee2009drosophilaikkrelatedkinase pages 2-2)

## 2. Catalytic function and substrate specificity

As EC 2.7.11.1, the expected reaction is transfer of the γ-phosphate of ATP to serine or threonine residues on protein substrates:

**ATP + protein–Ser/Thr–OH → ADP + protein–Ser/Thr–O–phosphate.**

### Spn-F: strongest direct substrate assignment

Spn-F is the most securely established substrate. Ik2–Spn-F association was detected by yeast two-hybrid analysis, co-immunoprecipitation in S2 cells and transgenic ovaries, and direct interaction measurements. The reported kinetic binding constants were *k*a = 4.15 × 10³ M⁻¹s⁻¹, *k*d = 1.69 × 10⁻³ s⁻¹, and equilibrium *K*D ≈ 407.2 nM. Co-expression with Ik2 produced a mobility shift in Spn-F that was reversed by alkaline phosphatase, supporting phosphorylation. Importantly, phosphorylation does **not** target Spn-F for degradation. (dubinbar2008thedrosophilaikkrelated pages 1-2, dubinbar2008thedrosophilaikkrelated pages 2-4)

During neuronal pruning, Ik2-dependent phosphorylation reduces Spn-F self-association and disperses Spn-F puncta. Spn-F then acts as an adaptor linking Ik2 to cytoplasmic dynein; dynein redistributes the complex toward microtubule minus ends. CC3 is required for Ik2 binding, while deletion of the C-terminal SCD weakens association with dynein light chain/Ctp. Eight-site phosphomimetic and nonphosphorylatable Spn-F constructs have been used experimentally, but the retrieved evidence does not establish a fully validated physiological phosphosite map or site-specific kinetics. (lin2015spindlefisthe pages 14-17, lin2015spindlefisthe pages 17-18)

### DIAP1: strong pathway target, less certain direct substrate

Ik2 binds DIAP1 and promotes its degradation in a kinase-dependent manner. Reduced DIAP1 permits restricted activity of caspases, including the initiator caspase DRONC, without causing wholesale apoptosis. Genetic modification by DIAP1 and DRONC dosage supports this pathway’s contribution to F-actin-dependent morphogenesis. Nevertheless, the available evidence does not conclusively show that Ik2 directly phosphorylates DIAP1 or identify a DIAP1 phosphosite; it is therefore most accurate to call DIAP1 a **kinase-dependent pathway target**, not a definitively established direct substrate. (lin2015spindlefisthe pages 17-18, dubinbar2008thedrosophilaikkrelated pages 1-2)

No comprehensive peptide-recognition motif, phosphoproteomic substrate inventory, ATP affinity, turnover number, or catalytic-efficiency measurement has been reported in the retrieved gene-specific literature. Rab11 is activated functionally downstream of the Ik2–Spn-F complex, but there is no evidence that Rab11 itself is directly phosphorylated by Ik2. (lin2020rab11activationby pages 1-2)

## 3. Cellular localization

Ik2 is an intracellular, dynamically localized kinase rather than a secreted or integral membrane protein. In ovaries it colocalizes with Spn-F at the **anterior ring of the oocyte** and in **punctate structures in nurse cells**; each protein is needed for proper localization of the other. Ik2 and Spn-F also colocalize in cytoplasmic puncta in S2/S2R+ cells. These observations place catalytic action in localized cytoplasmic cytoskeletal/transport complexes. (dubinbar2008thedrosophilaikkrelated pages 1-2, dubinbar2008thedrosophilaikkrelated pages 2-4)

Localization changes with developmental context. In sensory neurons, Ik2 becomes active after puparium formation, phosphorylates Spn-F, and enables dynein-dependent redistribution of Ik2–Spn-F complexes. In polarized bristles, the pathway participates in distal transport/retention and recycling-endosome-dependent elongation. The evidence therefore favors a model of transient association with microtubule motors, cortical structures, and endosomal compartments rather than residence in one invariant organelle. (lin2015spindlefisthe pages 2-3, lin2015spindlefisthe pages 17-18)

## 4. Principal pathways and biological processes

### 4.1 Oogenesis, cytoskeletal polarity, and localized mRNA transport

Maternal Ik2 is required for correct localization of **gurken**, **oskar**, and, more modestly, **bicoid** mRNAs. Loss of function disrupts actin organization, microtubule-minus-end anchoring, and perinuclear microtubule organization, leading to ventralized or bicaudal embryos. The best interpretation is that Ik2–Spn-F complexes organize interactions among the actin-rich cortex, microtubule minus ends, and dynein-dependent RNA transport. The RNAs themselves are cargo, not kinase substrates. (shapiro2006drosophilaik2a pages 1-2, dubinbar2008thedrosophilaikkrelated pages 1-2, shapiro2006drosophilaik2a pages 7-8)

### 4.2 F-actin morphogenesis and polarized cell elongation

Ik2 controls the fidelity of F-actin assembly in elongated bristles, arista laterals, and tracheal terminal cells. Loss of function causes abnormal branching, whereas excessive Ik2 destabilizes F-actin-rich structures. DIAP1 degradation and nonapoptotic caspase activity provide one mechanism, while recycling-endosome shuttling supplies membrane and polarity components during elongation. These effects are not adequately described as classical NF-κB signaling. (dubinbar2008thedrosophilaikkrelated pages 1-2)

### 4.3 Dendrite pruning

Ik2 is necessary and temporally sufficient for severing larval dendrites of class-IV dendritic-arborization neurons during metamorphosis. Kinase-dead Ik2-K41A or Ik2-G250D, RNAi, and loss-of-function clones retain proximal dendrites; premature Ik2 activation induces precocious severing. Ik2 is not required for initial larval dendritic morphogenesis and is not generally required for programmed neuronal death. (lee2009drosophilaikkrelatedkinase pages 2-2, lee2009drosophilaikkrelatedkinase pages 1-2)

The mechanism includes temporally activated Ik2, phosphorylation and redistribution of Spn-F, dynein-complex engagement, local microtubule remodeling, and Rab11 activation. In wild type, 77% of ddaC neurons had at least one dendrite severed at 5 h after puparium formation (*n*=120), and 100% had removed severed dendrites by 16 h (*n*=75). Severing generally occurs at 4–6 h, followed by fragmentation and epidermal clearance by approximately 16–18 h. (lee2009drosophilaikkrelatedkinase pages 2-2, lee2009drosophilaikkrelatedkinase pages 1-2, lin2015spindlefisthe pages 2-3)

### 4.4 Rab11 and endosomal transport

Genetic, imaging, and biochemical experiments place active GTP-bound **Rab11** downstream of or parallel to Ik2. Ik2 kinase activity and formation of Ik2–Spn-F–Rab11 complexes promote Rab11 activation during pruning; Rab11 loss does not prevent upstream Ik2 activation. An Spn-F interactome also connected Ik2 with Hook and dynein light chain, supporting a broader role in early-endosome transport. These findings connect Ik2’s cytoskeletal actions with recycling and endosomal membrane traffic. (lu2020ik2tbk1andhookdynein pages 1-2, lu2020ik2tbk1andhookdynein pages 2-3, lin2020rab11activationby pages 1-2)

## 5. Current applications and translational relevance

The most developed application is use of Ik2 pathway genetics to dissect neuronal remodeling and endosomal dysfunction in intact flies. In a frontotemporal-dementia model expressing mutant **CHMP2BIntron5**, heterozygous Ik2 loss or Ik2 RNAi enhanced retinal toxicity, whereas neuronal Ik2 overexpression suppressed mutant CHMP2B-associated synaptic overgrowth and motor defects. Loss of Spn-F, Hook, or dynein components produced related enhancement, implicating an Ik2–Spn-F–Hook/dynein transport axis. (lu2020ik2tbk1andhookdynein pages 1-2, lu2020ik2tbk1andhookdynein pages 2-3)

This is a research model, not a clinical implementation. It supports conserved relevance to endosomal transport and possibly TBK1-associated neurodegeneration, but it does not establish Ik2 as a therapeutic target or justify treating human IKBKE and TBK1 as interchangeable with fly Q9V3Y8.

## 6. Current understanding and recent-research status

The expert consensus emerging from the primary studies is that the name “IKKepsilon” obscures the protein’s dominant demonstrated role: Ik2 is **not principally a fly IκB/NF-κB kinase**. It is a spatial regulator of cytoskeletal and membrane-transport machinery whose output depends on tissue and developmental timing. Spn-F phosphorylation is the best-defined catalytic event; DIAP1/caspase regulation and Rab11 activation represent additional pathway outputs with different levels of directness. (dubinbar2008thedrosophilaikkrelated pages 1-2, shapiro2006drosophilaik2a pages 7-8, lin2020rab11activationby pages 1-2, lin2015spindlefisthe pages 17-18)

Targeted searches using Q9V3Y8, CG2615, Ik2, dIKKepsilon, and related aliases found no substantive 2023–2024 primary study specifically centered on this *Drosophila* protein. The latest directly relevant retrieved studies were published in 2020: one established Ik2–Spn-F-dependent Rab11 activation in pruning, and another implicated Ik2/Spn-F/Hook/dynein in mutant-CHMP2B toxicity. Recent mammalian IKBKE or TBK1 papers were deliberately excluded because they address different gene products. (lu2020ik2tbk1andhookdynein pages 1-2, lin2020rab11activationby pages 1-2)

## 7. Evidence-weighted annotation and open questions

**High-confidence annotation:** intracellular noncanonical IKK-family serine/threonine kinase; directly binds and phosphorylates Spn-F; controls localized cytoskeletal and endosomal-transport events in oogenesis, polarized elongation, and dendrite pruning.

**Moderate-confidence annotation:** promotes DIAP1 degradation and nonapoptotic caspase signaling; promotes Rab11 activation; participates in Hook/dynein-dependent endosome transport. These are strongly supported pathway functions, but DIAP1 and Rab11 should not yet be annotated as proven direct phosphosubstrates. (lu2020ik2tbk1andhookdynein pages 1-2, lin2020rab11activationby pages 1-2, dubinbar2008thedrosophilaikkrelated pages 1-2)

**Major unresolved questions:** the complete physiological substrate repertoire; precise Spn-F phosphosites and their individual functions; Ik2 activation mechanism; structural basis of substrate selection; quantitative enzyme kinetics; whether early- and recycling-endosome activities share one molecular mechanism; and the degree to which fly Ik2 models human TBK1 versus IKBKE.

## Key source URLs and publication dates

- Shapiro & Anderson, *Development*, April 2006: https://doi.org/10.1242/dev.02318. (shapiro2006drosophilaik2a pages 1-2)
- Dubin-Bar et al., *BMC Cell Biology*, September 2008: https://doi.org/10.1186/1471-2121-9-51. (dubinbar2008thedrosophilaikkrelated pages 1-2)
- Lee, Jan & Jan, *PNAS*, April 2009: https://doi.org/10.1073/pnas.0902051106. (lee2009drosophilaikkrelatedkinase pages 2-2)
- Lin et al., *PLOS Genetics*, November 2015: https://doi.org/10.1371/journal.pgen.1005642. (lin2015spindlefisthe pages 2-3)
- Lin et al., *PLOS Genetics*, February 2020: https://doi.org/10.1371/journal.pgen.1008626. (lin2020rab11activationby pages 1-2)
- Lu et al., *Scientific Reports*, August 2020: https://doi.org/10.1038/s41598-020-71097-5. (lu2020ik2tbk1andhookdynein pages 1-2)

References

1. (shapiro2006drosophilaik2a pages 1-2): Risa S. Shapiro and Kathryn V. Anderson. Drosophila ik2, a member of the iκb kinase family, is required for mrna localization during oogenesis. Development, 133:1467-1475, Apr 2006. URL: https://doi.org/10.1242/dev.02318, doi:10.1242/dev.02318. This article has 46 citations and is from a domain leading peer-reviewed journal.

2. (dubinbar2008thedrosophilaikkrelated pages 1-2): Dikla Dubin-Bar, Amir Bitan, Anna Bakhrat, Rotem Kaiden-Hasson, Sharon Etzion, Boaz Shaanan, and Uri Abdu. The drosophila ikk-related kinase (ik2) and spindle-f proteins are part of a complex that regulates cytoskeleton organization during oogenesis. Sep 2008. URL: https://doi.org/10.1186/1471-2121-9-51, doi:10.1186/1471-2121-9-51. This article has 41 citations.

3. (lu2020ik2tbk1andhookdynein pages 2-3): Yubing Lu, Ryan J. H. West, Marine Pons, Sean T. Sweeney, and Fen-Biao Gao. Ik2/tbk1 and hook/dynein, an adaptor complex for early endosome transport, are genetic modifiers of ftd-associated mutant chmp2b toxicity in drosophila. Scientific Reports, Aug 2020. URL: https://doi.org/10.1038/s41598-020-71097-5, doi:10.1038/s41598-020-71097-5. This article has 15 citations and is from a peer-reviewed journal.

4. (dubinbar2008thedrosophilaikkrelated pages 2-4): Dikla Dubin-Bar, Amir Bitan, Anna Bakhrat, Rotem Kaiden-Hasson, Sharon Etzion, Boaz Shaanan, and Uri Abdu. The drosophila ikk-related kinase (ik2) and spindle-f proteins are part of a complex that regulates cytoskeleton organization during oogenesis. Sep 2008. URL: https://doi.org/10.1186/1471-2121-9-51, doi:10.1186/1471-2121-9-51. This article has 41 citations.

5. (lin2020rab11activationby pages 1-2): Tzu Lin, Hao-Hsiang Kao, Che-Hsuan Chou, Chih-Yu Chou, Yu-Ching Liao, and Hsiu-Hsiang Lee. Rab11 activation by ik2 kinase is required for dendrite pruning in drosophila sensory neurons. Feb 2020. URL: https://doi.org/10.1371/journal.pgen.1008626, doi:10.1371/journal.pgen.1008626. This article has 11 citations and is from a domain leading peer-reviewed journal.

6. (lin2015spindlefisthe pages 17-18): Tzu Lin, Po-Yuan Pan, Yu-Ting Lai, Kai-Wen Chiang, Hsin-Lun Hsieh, Yi-Ping Wu, Jian-Ming Ke, Myong-Chol Lee, Shih-Sian Liao, Hsueh-Tzu Shih, Chiou-Yang Tang, Shi-Bing Yang, Hsu-Chen Cheng, June-Tai Wu, Yuh-Nung Jan, and Hsiu-Hsiang Lee. Spindle-f is the central mediator of ik2 kinase-dependent dendrite pruning in drosophila sensory neurons. Nov 2015. URL: https://doi.org/10.1371/journal.pgen.1005642, doi:10.1371/journal.pgen.1005642. This article has 27 citations and is from a domain leading peer-reviewed journal.

7. (lee2009drosophilaikkrelatedkinase pages 2-2): Hsiu-Hsiang Lee, Lily Yeh Jan, and Yuh-Nung Jan. Drosophila ikk-related kinase ik2 and katanin p60-like 1 regulate dendrite pruning of sensory neuron during metamorphosis. Proceedings of the National Academy of Sciences, 106:6363-6368, Apr 2009. URL: https://doi.org/10.1073/pnas.0902051106, doi:10.1073/pnas.0902051106. This article has 156 citations and is from a highest quality peer-reviewed journal.

8. (shapiro2006drosophilaik2a pages 7-8): Risa S. Shapiro and Kathryn V. Anderson. Drosophila ik2, a member of the iκb kinase family, is required for mrna localization during oogenesis. Development, 133:1467-1475, Apr 2006. URL: https://doi.org/10.1242/dev.02318, doi:10.1242/dev.02318. This article has 46 citations and is from a domain leading peer-reviewed journal.

9. (lee2009drosophilaikkrelatedkinase pages 1-2): Hsiu-Hsiang Lee, Lily Yeh Jan, and Yuh-Nung Jan. Drosophila ikk-related kinase ik2 and katanin p60-like 1 regulate dendrite pruning of sensory neuron during metamorphosis. Proceedings of the National Academy of Sciences, 106:6363-6368, Apr 2009. URL: https://doi.org/10.1073/pnas.0902051106, doi:10.1073/pnas.0902051106. This article has 156 citations and is from a highest quality peer-reviewed journal.

10. (lin2015spindlefisthe pages 2-3): Tzu Lin, Po-Yuan Pan, Yu-Ting Lai, Kai-Wen Chiang, Hsin-Lun Hsieh, Yi-Ping Wu, Jian-Ming Ke, Myong-Chol Lee, Shih-Sian Liao, Hsueh-Tzu Shih, Chiou-Yang Tang, Shi-Bing Yang, Hsu-Chen Cheng, June-Tai Wu, Yuh-Nung Jan, and Hsiu-Hsiang Lee. Spindle-f is the central mediator of ik2 kinase-dependent dendrite pruning in drosophila sensory neurons. Nov 2015. URL: https://doi.org/10.1371/journal.pgen.1005642, doi:10.1371/journal.pgen.1005642. This article has 27 citations and is from a domain leading peer-reviewed journal.

11. (lu2020ik2tbk1andhookdynein pages 1-2): Yubing Lu, Ryan J. H. West, Marine Pons, Sean T. Sweeney, and Fen-Biao Gao. Ik2/tbk1 and hook/dynein, an adaptor complex for early endosome transport, are genetic modifiers of ftd-associated mutant chmp2b toxicity in drosophila. Scientific Reports, Aug 2020. URL: https://doi.org/10.1038/s41598-020-71097-5, doi:10.1038/s41598-020-71097-5. This article has 15 citations and is from a peer-reviewed journal.

12. (lin2015spindlefisthe pages 14-17): Tzu Lin, Po-Yuan Pan, Yu-Ting Lai, Kai-Wen Chiang, Hsin-Lun Hsieh, Yi-Ping Wu, Jian-Ming Ke, Myong-Chol Lee, Shih-Sian Liao, Hsueh-Tzu Shih, Chiou-Yang Tang, Shi-Bing Yang, Hsu-Chen Cheng, June-Tai Wu, Yuh-Nung Jan, and Hsiu-Hsiang Lee. Spindle-f is the central mediator of ik2 kinase-dependent dendrite pruning in drosophila sensory neurons. Nov 2015. URL: https://doi.org/10.1371/journal.pgen.1005642, doi:10.1371/journal.pgen.1005642. This article has 27 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](IKKepsilon-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. dubinbar2008thedrosophilaikkrelated pages 1-2
2. lee2009drosophilaikkrelatedkinase pages 2-2
3. lin2015spindlefisthe pages 2-3
4. dubinbar2008thedrosophilaikkrelated pages 2-4
5. lin2015spindlefisthe pages 17-18
6. lee2009drosophilaikkrelatedkinase pages 1-2
7. lin2015spindlefisthe pages 14-17
8. https://doi.org/10.1242/dev.02318.
9. https://doi.org/10.1186/1471-2121-9-51.
10. https://doi.org/10.1073/pnas.0902051106.
11. https://doi.org/10.1371/journal.pgen.1005642.
12. https://doi.org/10.1371/journal.pgen.1008626.
13. https://doi.org/10.1038/s41598-020-71097-5.
14. https://doi.org/10.1242/dev.02318,
15. https://doi.org/10.1186/1471-2121-9-51,
16. https://doi.org/10.1038/s41598-020-71097-5,
17. https://doi.org/10.1371/journal.pgen.1008626,
18. https://doi.org/10.1371/journal.pgen.1005642,
19. https://doi.org/10.1073/pnas.0902051106,