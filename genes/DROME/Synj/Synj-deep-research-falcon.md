---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-10T14:33:26.348956'
end_time: '2026-09-10T14:42:06.378157'
duration_seconds: 520.03
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: Synj
  gene_symbol: Synj
  uniprot_accession: Q5U0V7
  protein_description: 'RecName: Full=phosphoinositide 5-phosphatase {ECO:0000256|ARBA:ARBA00013044};
    EC=3.1.3.36 {ECO:0000256|ARBA:ARBA00013044};'
  gene_info: Name=Synj {ECO:0000313|FlyBase:FBgn0034691}; Synonyms=synaptojanin {ECO:0000313|EMBL:AAV37020.1},
    synj {ECO:0000313|FlyBase:FBgn0034691}; ORFNames=CG6562 {ECO:0000313|FlyBase:FBgn0034691};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: In the central section; belongs to the inositol 1,4,5-
  protein_domains: Endo/exonu/phosph_ase_sf. (IPR036691); IP5. (IPR046985); IPPc.
    (IPR000300); Nucleotide-bd_a/b_plait_sf. (IPR012677); RBD_domain_sf. (IPR035979)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 34
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Synj-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q5U0V7
- **Protein Description:** RecName: Full=phosphoinositide 5-phosphatase {ECO:0000256|ARBA:ARBA00013044}; EC=3.1.3.36 {ECO:0000256|ARBA:ARBA00013044};
- **Gene Information:** Name=Synj {ECO:0000313|FlyBase:FBgn0034691}; Synonyms=synaptojanin {ECO:0000313|EMBL:AAV37020.1}, synj {ECO:0000313|FlyBase:FBgn0034691}; ORFNames=CG6562 {ECO:0000313|FlyBase:FBgn0034691};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** In the central section; belongs to the inositol 1,4,5-
- **Key Domains:** Endo/exonu/phosph_ase_sf. (IPR036691); IP5. (IPR046985); IPPc. (IPR000300); Nucleotide-bd_a/b_plait_sf. (IPR012677); RBD_domain_sf. (IPR035979)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Synj" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Synj' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Synj** (gene ID: Synj, UniProt: Q5U0V7) in DROME.

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
- **UniProt Accession:** Q5U0V7
- **Protein Description:** RecName: Full=phosphoinositide 5-phosphatase {ECO:0000256|ARBA:ARBA00013044}; EC=3.1.3.36 {ECO:0000256|ARBA:ARBA00013044};
- **Gene Information:** Name=Synj {ECO:0000313|FlyBase:FBgn0034691}; Synonyms=synaptojanin {ECO:0000313|EMBL:AAV37020.1}, synj {ECO:0000313|FlyBase:FBgn0034691}; ORFNames=CG6562 {ECO:0000313|FlyBase:FBgn0034691};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** In the central section; belongs to the inositol 1,4,5-
- **Key Domains:** Endo/exonu/phosph_ase_sf. (IPR036691); IP5. (IPR046985); IPPc. (IPR000300); Nucleotide-bd_a/b_plait_sf. (IPR012677); RBD_domain_sf. (IPR035979)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Synj" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Synj' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Synj** (gene ID: Synj, UniProt: Q5U0V7) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Drosophila melanogaster* **Synj** (UniProt Q5U0V7)

## Executive conclusion

The requested target is correctly identified as the *Drosophila melanogaster* **Synj/synj** gene product, also called synaptojanin and CG6562—not a similarly named protein from another organism. The supplied UniProt identity is consistent with classical fly genetics: *synj* alleles were mapped, sequenced, tested by deficiency complementation, and rescued with the synaptojanin genomic locus. The encoded protein has the characteristic synaptojanin architecture: an N-terminal SAC1 phosphatase domain, a central inositol-polyphosphate 5-phosphatase domain, and a C-terminal proline-rich interaction region. This matches the supplied IPPc/IP5 and phosphatase-superfamily annotations. No conflicting use of “Synj” for a different *Drosophila* protein was found. (verstreken2015synaptojaninisrecruited pages 3-5)

Synj is best annotated as a **presynaptically enriched, dual-specificity phosphoinositide phosphatase and endocytic effector**. Its principal established role is to remodel phosphoinositide identity on newly retrieved synaptic membranes—especially conversion of PI(4,5)P₂ to PI(4)P—thereby promoting clathrin-coat/adaptor removal and synaptic-vesicle recycling. Its SAC1 domain additionally controls other phosphoinositides and has separable functions in activity-dependent bulk endocytosis and presynaptic autophagosome maturation. Outside neurons, fly evidence supports a more limited role in fine-tuning Hedgehog signaling through PI(4)P and Smoothened. (peng2021minibrainkinaseand pages 10-12, verstreken2015synaptojaninisrecruited pages 1-2, vanhauwaert2017thesac1domain pages 1-2, ahaley2018synaptojaninregulateshedgehog pages 1-2)

## 1. Identity verification and nomenclature

**Verified target:** UniProt **Q5U0V7**; organism *Drosophila melanogaster*; gene **Synj**; synonyms **synj**, **synaptojanin**, and **CG6562**. The direct literature generally uses *synj* for the fly gene and Synj for its protein. Human/mammalian **SYNJ1/Synj1** studies are useful for evolutionary and structural context but do not independently establish properties of Q5U0V7.

The foundational fly study identified two strong loss-of-function alleles: *synj¹* contains a nonsense mutation at residue 460, whereas *synj²* carries G65D. Genetic mapping used at least 7,000 flies per insertion, and recombination, deficiency complementation, sequencing, and genomic rescue converged on the synaptojanin locus. The same study described one fly protein containing SAC1, inositol 5-phosphatase, and proline-rich regions. (verstreken2015synaptojaninisrecruited pages 3-5)

The supplied InterPro terms are therefore coherent with the literature. IPPc/IP5 correspond to the central inositol-polyphosphate 5-phosphatase catalytic module; the broad endo/exonuclease/phosphatase-superfamily annotation is consistent with phosphoester hydrolysis. Some generic fold annotations in the supplied record, such as nucleotide-binding or RBD-like superfamilies, are not prominent in the experimental fly literature and should not be promoted to established biological functions without additional structural evidence.

## 2. Molecular function and reaction chemistry

### 2.1 Central 5-phosphatase activity

The most securely demonstrated fly reaction is:

**PI(4,5)P₂ + H₂O → PI(4)P + inorganic phosphate.**

A catalytically defective 5-phosphatase-domain Synj lacks PI(4,5)P₂-to-PI(4)P activity and fails to restore FM1-43 uptake associated with clathrin-mediated synaptic-vesicle endocytosis. Thus, EC 3.1.3.36 is functionally appropriate, although “phosphoinositide 5-phosphatase” is more informative than a generic phosphatase label. (peng2021minibrainkinaseand pages 10-12, peng2021minibrainkinaseand pages 21-23)

Broader domain-level specificity reported for synaptojanin includes 5-phosphate hydrolysis from PI(3,5)P₂ and PI(3,4,5)P₃ as well as PI(4,5)P₂. For Q5U0V7, however, PI(4,5)P₂ is the best-supported physiological substrate because fly catalytic mutants, lipid manipulation, and endocytic phenotypes converge on this lipid. The broader substrate list should be treated as supported biochemical capability rather than proof that all substrates are equally important in every fly tissue. (ahaley2018synaptojaninregulateshedgehog pages 1-2)

### 2.2 SAC1-domain activity

The N-terminal SAC1 domain hydrolyzes PI(3)P, PI(4)P, and PI(3,5)P₂. Fly catalytic mutants abolish measurable SAC1 activity while preserving separable 5-phosphatase functions, demonstrating that Synj is genuinely a dual phosphatase rather than a single active site with broad specificity. (vanhauwaert2017thesac1domain pages 1-2, peng2021minibrainkinaseand pages 21-23)

The two catalytic modules have overlapping but nonidentical biological outputs. The central 5-phosphatase is indispensable for efficient conventional clathrin-mediated endocytosis, whereas SAC1 activity is particularly important for activity-dependent bulk endocytosis and autophagosome maturation. This domain separation is one of the strongest mechanistic conclusions from the fly system. (peng2021minibrainkinaseand pages 10-12, vanhauwaert2017thesac1domain pages 1-2)

### 2.3 Proline-rich interaction region

The C-terminal proline-rich domain is not catalytic. It mediates protein interactions, most notably with Endophilin. Deleting it blocks Synj–Endophilin binding and reduces Synj stability, although it can be comparatively dispensable in some bulk-endocytosis assays. Fly Synj’s proline-rich region differs substantially in sequence from its mammalian orthologue, so individual phosphorylation or interaction motifs should not be transferred automatically from mammalian SYNJ1. (chen2014activitydependentfacilitationof pages 11-12, peng2021minibrainkinaseand pages 21-23)

| Functional module/domain | Biochemical or cellular role | Direct evidence in fly | Principal substrate/product or localization | Key source/date/DOI |
|---|---|---|---|---|
| SAC1 phosphatase domain | Hydrolyzes phosphoinositides and supports bulk endocytosis and presynaptic autophagosome maturation | **Direct fly evidence:** catalytic-dead and Parkinsonism-associated SAC1 mutants abolish SAC1 activity; endogenous R228Q causes Atg18a accumulation on nascent autophagosomes, impaired maturation, and neurodegeneration while leaving conventional endocytosis largely intact (peng2021minibrainkinaseand pages 10-12, vanhauwaert2017thesac1domain pages 1-2, peng2021minibrainkinaseand pages 21-23) | PI(3)P, PI(4)P, and PI(3,5)P₂; presynaptic terminals and nascent autophagosomes | Vanhauwaert et al., 22 Mar 2017, [10.15252/embj.201695773](https://doi.org/10.15252/embj.201695773); Peng et al., Oct 2021, [10.1083/jcb.202011028](https://doi.org/10.1083/jcb.202011028) |
| Central inositol 5-phosphatase domain | Removes the 5-phosphate from PI(4,5)P₂, lowering an endocytic membrane-identity signal and enabling efficient vesicle recycling | **Direct fly evidence:** a 5-phosphatase-defective Synj lacks PI(4,5)P₂-to-PI(4)P activity and fails to restore FM1-43 uptake during clathrin-mediated endocytosis (peng2021minibrainkinaseand pages 10-12, peng2021minibrainkinaseand pages 21-23) | Principal demonstrated reaction: PI(4,5)P₂ + H₂O → PI(4)P + inorganic phosphate; broader specificity for PI(3,5)P₂ and PI(3,4,5)P₃ is reported from domain-level biochemical knowledge (ahaley2018synaptojaninregulateshedgehog pages 1-2) | Peng et al., Oct 2021, [10.1083/jcb.202011028](https://doi.org/10.1083/jcb.202011028); Ahaley, Sep 2018, [10.1007/s12038-018-9799-5](https://doi.org/10.1007/s12038-018-9799-5) |
| C-terminal proline-rich domain (PRD)–Endophilin module | Recruits or stabilizes Synj on newly formed vesicles and couples lipid dephosphorylation to coat removal | **Direct fly evidence:** Synj and Endophilin colocalize and interact; Endophilin loss mislocalizes and destabilizes Synj, while PRD deletion blocks Synj–Endophilin binding (verstreken2015synaptojaninisrecruited pages 1-2, peng2021minibrainkinaseand pages 21-23) | Protein–protein interaction at presynaptic boutons and synaptic-vesicle membranes | Verstreken et al., 13 Nov 2003, [10.1016/S0896-6273(03)00644-5](https://doi.org/10.1016/S0896-6273(03)00644-5); Peng et al., Oct 2021, [10.1083/jcb.202011028](https://doi.org/10.1083/jcb.202011028) |
| Synaptic-vesicle clathrin-mediated endocytosis and uncoating | Promotes removal of PI(4,5)P₂-dependent adaptors and clathrin coats so retrieved membranes can regenerate functional synaptic vesicles | **Direct fly evidence:** synj mutants accumulate coated vesicles and show behavioral, electrophysiological, and ultrastructural defects resembling endophilin mutants; genomic mapping/rescue established the causal synaptojanin locus (verstreken2015synaptojaninisrecruited pages 1-2, verstreken2015synaptojaninisrecruited pages 3-5) | Specifically enriched in larval NMJ boutons and photoreceptor presynaptic terminals; associated with synaptic vesicles (verstreken2015synaptojaninisrecruited pages 1-2, verstreken2015synaptojaninisrecruited pages 3-5) | Verstreken et al., 13 Nov 2003, [10.1016/S0896-6273(03)00644-5](https://doi.org/10.1016/S0896-6273(03)00644-5) |
| Activity-regulated Synj / S1029 phosphorylation | Tunes phosphatase activity and allocates membrane retrieval between active-cycling and reserve vesicle pools | **Direct fly evidence:** Minibrain/DYRK1A phosphorylates S1029, increasing Synj activity and favoring active-pool retrieval; dephosphorylation favors reserve-pool retrieval. Minibrain and calcineurin coordinate the switch between endocytic modes (peng2021minibrainkinaseand pages 10-12, geng2016phosphorylationofsynaptojanin pages 1-2) | Presynaptic endocytic zones at the larval NMJ; phosphorylation changes Synj–Endophilin interactions and PI(4,5)P₂ turnover | Geng et al., 24 Aug 2016, [10.1523/JNEUROSCI.1470-16.2016](https://doi.org/10.1523/JNEUROSCI.1470-16.2016); Peng et al., Oct 2021, [10.1083/jcb.202011028](https://doi.org/10.1083/jcb.202011028) |
| Activity-dependent bulk endocytosis (ADBE) | Controls large-scale membrane retrieval during intense neuronal stimulation | **Direct fly evidence:** 5-phosphatase loss increases dextran uptake, showing that PI(4,5)P₂ hydrolysis suppresses ADBE, whereas intact SAC1 activity is required for normal ADBE; PRD–Endophilin binding is comparatively dispensable in this assay (peng2021minibrainkinaseand pages 10-12) | Presynaptic periactive/endocytic membrane; PI(4,5)P₂ and SAC1-domain phosphoinositide substrates | Peng et al., Oct 2021, [10.1083/jcb.202011028](https://doi.org/10.1083/jcb.202011028) |
| Presynaptic autophagy | Enables Atg18a release and maturation of nascent autophagosomes, linking phosphoinositide turnover to neuronal proteostasis | **Direct fly evidence:** endogenous Synj R228Q selectively impairs autophagosome maturation, causes presynaptic Atg18a retention, and produces dopaminergic-neuron loss despite preserved protein abundance and broadly normal endocytosis (vanhauwaert2017thesac1domain pages 1-2) | PI(3)P/PI(3,5)P₂-rich nascent autophagosomes at presynaptic terminals | Vanhauwaert et al., 22 Mar 2017, [10.15252/embj.201695773](https://doi.org/10.15252/embj.201695773) |
| Hedgehog signaling in wing imaginal discs | Acts as a negative fine-tuner of Smoothened activation by limiting PI(4)P | **Direct fly evidence:** Synj knockdown elevates PI(4)P, activated Smoothened, and the low-threshold target *dpp*, without equivalent induction of high-threshold targets; approximately 50 wings per genotype were evaluated (ahaley2018synaptojaninregulateshedgehog pages 1-2) | PI(4)P in wing-disc cells; Smoothened/Hedgehog signaling compartment | Ahaley, Sep 2018, [10.1007/s12038-018-9799-5](https://doi.org/10.1007/s12038-018-9799-5) |
| Auxilin/DNAJC6 Parkinsonism model | Experimental disease-modifier application connecting phosphoinositide metabolism, clathrin trafficking, lipid homeostasis, and neuronal survival | **Direct fly disease-model evidence:** neuronal Synj overexpression partially rescues function, neurodegeneration, and multiple lipid abnormalities in pathogenic *dAux* mutants with reduced long-chain PUFA-containing phosphoinositides (jacquemyn2023parkinsonismmutationsin pages 8-9) | Proposed Golgi and synaptic trafficking compartments; altered phosphatidylinositol lipid species | Jacquemyn et al., Feb 2023, [10.1038/s41531-023-00459-3](https://doi.org/10.1038/s41531-023-00459-3) |
| Structural catalytic mechanism | Explains recognition and hydrolysis by the conserved 5-phosphatase fold | **Ortholog-based inference—not direct Q5U0V7 evidence:** substrate-bound mammalian SYNJ1 structures support conservation of 5-phosphatase chemistry, but fly-specific residues and kinetics should not be assumed without direct testing | Structural substrate: diC8-PI(3,4,5)P₃; conserved inositol-polyphosphate 5-phosphatase active site | Paesmans et al., Dec 2020, [10.7554/eLife.64922](https://doi.org/10.7554/eLife.64922) |


*Table: Evidence map linking the verified fly Synj protein’s catalytic modules to synaptic trafficking, autophagy, Hedgehog signaling, and disease-model applications. Direct Drosophila findings are explicitly separated from ortholog-based structural inference.*

## 3. Subcellular localization

Synj is an intracellular, membrane-associated peripheral protein rather than a secreted protein or integral transporter. Direct immunostaining places it in **presynaptic terminals**, including larval neuromuscular-junction boutons and photoreceptor terminals, with enrichment at synaptic contact sites. It is associated with synaptic vesicles and newly endocytosed membrane intermediates. (verstreken2015synaptojaninisrecruited pages 1-2, verstreken2015synaptojaninisrecruited pages 3-5)

Localization is dynamic and interaction dependent. Synj colocalizes and interacts with Endophilin; loss of Endophilin mislocalizes and destabilizes Synj, supporting a model in which Endophilin recruits or retains it on newly formed endocytic vesicles. Minibrain kinase is mobilized toward presynaptic endocytic zones during neuronal stimulation and partially colocalizes with Synj, providing an activity-dependent regulatory layer. (verstreken2015synaptojaninisrecruited pages 1-2, chen2014activitydependentfacilitationof pages 5-6, chen2014activitydependentfacilitationof pages 1-2)

A second functionally important compartment is the **nascent presynaptic autophagosome**. Here SAC1-mediated phosphoinositide turnover enables removal or redistribution of the PI(3)P/PI(3,5)P₂-binding protein Atg18a and permits autophagosome maturation. Wing-imaginal-disc cells constitute a non-neuronal context in which Synj influences PI(4)P-dependent Hedgehog signaling. (vanhauwaert2017thesac1domain pages 1-2, ahaley2018synaptojaninregulateshedgehog pages 1-2)

## 4. Core biological process: synaptic-vesicle endocytosis and uncoating

During exocytosis, synaptic-vesicle membrane is added to the presynaptic plasma membrane. PI(4,5)P₂ recruits and stabilizes clathrin adaptors and other endocytic machinery. After membrane scission, Synj hydrolyzes PI(4,5)P₂; the resulting loss of PI(4,5)P₂-dependent interactions promotes dissociation of adaptors and clathrin, allowing the retrieved membrane to become a reusable synaptic vesicle.

The direct fly evidence is unusually strong. Synj is presynaptic and vesicle associated; *synj* mutants accumulate coated vesicles and display behavioral, electrophysiological, and ultrastructural defects resembling *endophilin* mutants. Synj and Endophilin colocalize and bind, Synj is destabilized or mislocalized in the absence of Endophilin, and Endophilin overexpression partially rescues *synj* loss-of-function phenotypes. These findings place Synj downstream of or together with Endophilin in the late stages of clathrin-mediated vesicle retrieval and uncoating. (verstreken2015synaptojaninisrecruited pages 1-2, verstreken2015synaptojaninisrecruited pages 15-16)

The conclusion is not merely that Synj broadly “affects endocytosis.” Domain-selective experiments show that loss of PI(4,5)P₂ 5-phosphatase activity fails to rescue FM1-43 uptake, directly tying the lipid reaction to conventional clathrin-mediated retrieval. (peng2021minibrainkinaseand pages 10-12)

## 5. Activity-dependent control of vesicle-retrieval modes

Synj activity is regulated by **Minibrain (Mnb), the fly DYRK1A homologue**, and by calcineurin. Mnb binds and phosphorylates Synj in vitro and in vivo; neuronal stimulation mobilizes Mnb to endocytic zones and promotes Synj phosphorylation. This changes Synj’s phosphatase activity and its interactions with Endophilin, Dap160/intersectin, and dynamin. (chen2014activitydependentfacilitationof pages 5-6, chen2014activitydependentfacilitationof pages 1-2, chen2014activitydependentfacilitationof pages 11-11)

Mnb phosphorylates fly Synj at **S1029**. Phosphorylation increases phosphatase activity and favors retrieval of the actively cycling vesicle pool, whereas dephosphorylated Synj favors reserve-pool retrieval and restoration of the total vesicle pool. This supports an expert interpretation of Synj as a regulated allocation point—not simply an on/off component—between functionally distinct recycling routes. (geng2016phosphorylationofsynaptojanin pages 1-2)

Under intense stimulation, neurons also use activity-dependent bulk endocytosis (ADBE). Here the domains have counterbalanced effects: disabling the 5-phosphatase increases dextran uptake, indicating that PI(4,5)P₂ hydrolysis normally restrains ADBE, while intact SAC1 activity is required for normal bulk retrieval. The PRD–Endophilin interaction is less essential in this context. Minibrain and calcineurin coordinate Synj phosphorylation state and thereby shift the predominant retrieval mode with stimulus intensity. (peng2021minibrainkinaseand pages 10-12)

## 6. Presynaptic autophagy and neuronal maintenance

A Parkinsonism-associated SAC1 mutation provided a clean separation of Synj functions. The human R258Q change corresponds to R228Q in fly Synj and was introduced into the endogenous *synj* locus. Mutant protein abundance was comparable to wild type, and conventional endocytosis was broadly preserved. Nevertheless, Atg18a accumulated on nascent presynaptic autophagosomes, maturation was blocked, and flies developed neurodegeneration, including dopaminergic-neuron loss. (vanhauwaert2017thesac1domain pages 1-2)

This result indicates that the SAC1 domain is not merely auxiliary to PI(4,5)P₂ turnover. It regulates a distinct PI(3)P/PI(3,5)P₂-dependent step in autophagosome maturation and neuronal proteostasis. The phenotype also makes *Drosophila* Synj a mechanistically useful model for distinguishing trafficking failure from autophagy failure in SYNJ1-associated neurological disease. (vanhauwaert2017thesac1domain pages 1-2)

## 7. Hedgehog signaling

In wing imaginal discs, Synj acts as a **negative fine-tuner of Hedgehog signaling**. Synj knockdown increased PI(4)P, Smoothened activation, and expression of the low-threshold target *dpp*, while high-threshold pathway targets were not equivalently induced. Knockdown also enhanced the dominant Moonrat gain-of-function wing phenotype. These observations favor a model in which Synj’s SAC1-associated control of PI(4)P adjusts Smoothened responsiveness rather than serving as an obligatory core Hedgehog component. (ahaley2018synaptojaninregulateshedgehog pages 1-2)

This conclusion is based on immunostaining for Synj, PI(4)P, PI(4,5)P₂, Smoothened, and pathway outputs, with approximately 50 wings examined per genotype. It is a credible secondary function, but its evidence base is smaller than that for presynaptic vesicle recycling. (ahaley2018synaptojaninregulateshedgehog pages 1-2)

## 8. Recent developments and applications, 2023–2024

The most directly relevant recent study was published in **February 2023**. A *Drosophila* knock-in model of pathogenic DNAJC6/Auxilin showed synaptic dysfunction, neurological abnormalities, neurodegeneration, and reduced long-chain polyunsaturated fatty-acid-containing lipids, including phosphatidylinositol species. Neuronal Synj overexpression partially rescued functional defects, neurodegeneration, and many lipid abnormalities. The authors proposed that Synj improves Auxilin-associated Golgi and synaptic trafficking and lipid delivery. This establishes a functional relationship between two phosphoinositide/clathrin-trafficking proteins implicated in Parkinsonism. DOI: https://doi.org/10.1038/s41531-023-00459-3. (jacquemyn2023parkinsonismmutationsin pages 8-9)

This application is a genetic disease-modifier experiment, not evidence that Synj itself is currently a clinical therapy. There are no real-world therapeutic implementations of fly Q5U0V7. Current practical uses are research applications: dissecting clathrin uncoating, measuring vesicle-pool recycling with FM1-43, distinguishing conventional from bulk endocytosis using dye/dextran assays, modeling SYNJ1-associated Parkinsonism and epilepsy mechanisms, and probing presynaptic autophagy.

No 2023–2024 Q5U0V7-specific study was found that supersedes the mechanistic conclusions from the 2003–2021 primary literature. Recent work principally extends Synj into neurodegeneration and lipid-homeostasis models. This scarcity should not be obscured by substituting human SYNJ1 studies for direct fly evidence.

## 9. Quantitative evidence and study scale

* The original genetic mapping analyzed at least **7,000 flies per insertion**, with independent genetic and rescue evidence establishing the *synj* locus. (verstreken2015synaptojaninisrecruited pages 3-5)
* The Hedgehog study assessed approximately **50 wings per genotype**, supporting reproducibility of the wing-phenotype comparisons but not providing a full biochemical kinetic characterization. (ahaley2018synaptojaninregulateshedgehog pages 1-2)
* Domain-selective NMJ experiments reported genotype-specific sample sizes of approximately **6–15 preparations**, with one stated control group of **n=34** and a mutant comparison of **n=15**; values were reported as mean ± SEM with significance at **P<0.05**. These data support domain-specific functional differences, although the retrieved text does not permit reliable extraction of every effect size. (peng2021minibrainkinaseand pages 21-23)
* The endogenous SAC1 R228Q model retained comparable protein abundance; a transgenic expression comparison was approximately **1.2-fold**, helping exclude simple instability as the cause of its autophagy phenotype. (vanhauwaert2017thesac1domain pages 1-2)

## 10. Evidence-weighted annotation

**High-confidence primary function:** presynaptic phosphoinositide phosphatase controlling synaptic-vesicle endocytosis, coat removal, and vesicle-pool recycling.

**High-confidence reaction:** 5-dephosphorylation of PI(4,5)P₂ to PI(4)P. SAC1-domain hydrolysis of PI(3)P, PI(4)P, and PI(3,5)P₂ is also well supported. (peng2021minibrainkinaseand pages 10-12, vanhauwaert2017thesac1domain pages 1-2)

**High-confidence localization:** cytoplasmic face of presynaptic/endocytic membranes, larval NMJ boutons, photoreceptor terminals, synaptic-vesicle intermediates, and nascent presynaptic autophagosomes. (verstreken2015synaptojaninisrecruited pages 1-2, verstreken2015synaptojaninisrecruited pages 3-5, vanhauwaert2017thesac1domain pages 1-2)

**High-confidence pathway partners:** Endophilin, clathrin-associated endocytic machinery, Dap160/intersectin, dynamin, Minibrain/DYRK1A, calcineurin, and Atg18a. (verstreken2015synaptojaninisrecruited pages 1-2, chen2014activitydependentfacilitationof pages 11-11, peng2021minibrainkinaseand pages 10-12, vanhauwaert2017thesac1domain pages 1-2)

**Moderate-confidence secondary role:** negative modulation of PI(4)P–Smoothened–Hedgehog signaling in wing discs. (ahaley2018synaptojaninregulateshedgehog pages 1-2)

**Ortholog-based inference requiring caution:** mammalian SYNJ1 structural and disease literature supports conserved catalytic principles, but fly-specific kinetics, interaction motifs, and disease effects should not be asserted without direct Q5U0V7 experiments. Notably, the fly PRD lacks close sequence similarity to the mammalian region despite conserved pathway-level function. (chen2014activitydependentfacilitationof pages 11-12)

## Overall interpretation

Q5U0V7/Synj is a membrane-identity-resetting enzyme. Its central 5-phosphatase removes PI(4,5)P₂ from retrieved presynaptic membrane, weakening lipid-dependent coat interactions and enabling vesicle uncoating and reuse. Its SAC1 domain broadens the lipid repertoire and connects Synj to bulk endocytosis, autophagosome maturation, and PI(4)P-dependent signaling. Endophilin provides spatial recruitment, while Minibrain and calcineurin provide activity-dependent regulation. The combination of catalytic-domain mutants, endogenous disease alleles, localization, interaction assays, ultrastructure, physiology, and genetic rescue makes the presynaptic functional annotation substantially stronger than any broad pleiotropic description.

References

1. (verstreken2015synaptojaninisrecruited pages 3-5): Patrik Verstreken, Tong-Wey Koh, Karen L. Schulze, R.Grace Zhai, P.Robin Hiesinger, Yi Zhou, Sunil Q. Mehta, Yu Cao, Jack Roos, and Hugo J. Bellen. Synaptojanin is recruited by endophilin to promote synaptic vesicle uncoating. Neuron, 40:733-748, Nov 2003. URL: https://doi.org/10.1016/s0896-6273(03)00644-5, doi:10.1016/s0896-6273(03)00644-5. This article has 502 citations and is from a highest quality peer-reviewed journal.

2. (peng2021minibrainkinaseand pages 10-12): Yi-Jheng Peng, Junhua Geng, Ying Wu, Cristian Pinales, Jennifer Langen, Yen-Ching Chang, Christopher Buser, and Karen T. Chang. Minibrain kinase and calcineurin coordinate activity-dependent bulk endocytosis through synaptojanin. The Journal of Cell Biology, Oct 2021. URL: https://doi.org/10.1083/jcb.202011028, doi:10.1083/jcb.202011028. This article has 13 citations.

3. (verstreken2015synaptojaninisrecruited pages 1-2): Patrik Verstreken, Tong-Wey Koh, Karen L. Schulze, R.Grace Zhai, P.Robin Hiesinger, Yi Zhou, Sunil Q. Mehta, Yu Cao, Jack Roos, and Hugo J. Bellen. Synaptojanin is recruited by endophilin to promote synaptic vesicle uncoating. Neuron, 40:733-748, Nov 2003. URL: https://doi.org/10.1016/s0896-6273(03)00644-5, doi:10.1016/s0896-6273(03)00644-5. This article has 502 citations and is from a highest quality peer-reviewed journal.

4. (vanhauwaert2017thesac1domain pages 1-2): Roeland Vanhauwaert, Sabine Kuenen, Roy Masius, Adekunle Bademosi, Julia Manetsberger, Nils Schoovaerts, Laura Bounti, Serguei Gontcharenko, Jef Swerts, Sven Vilain, Marina Picillo, Paolo Barone, Shashini T Munshi, Femke MS de Vrij, Steven A Kushner, Natalia V Gounko, Wim Mandemakers, Vincenzo Bonifati, Frederic A Meunier, Sandra‐Fausia Soukup, and Patrik Verstreken. The sac1 domain in synaptojanin is required for autophagosome maturation at presynaptic terminals. The EMBO Journal, 36:1392-1411, May 2017. URL: https://doi.org/10.15252/embj.201695773, doi:10.15252/embj.201695773. This article has 242 citations.

5. (ahaley2018synaptojaninregulateshedgehog pages 1-2): Shital Sarah Ahaley. Synaptojanin regulates hedgehog signalling by modulating phosphatidylinositol 4-phosphate levels. Journal of Biosciences, 43:867-876, Sep 2018. URL: https://doi.org/10.1007/s12038-018-9799-5, doi:10.1007/s12038-018-9799-5. This article has 3 citations and is from a peer-reviewed journal.

6. (peng2021minibrainkinaseand pages 21-23): Yi-Jheng Peng, Junhua Geng, Ying Wu, Cristian Pinales, Jennifer Langen, Yen-Ching Chang, Christopher Buser, and Karen T. Chang. Minibrain kinase and calcineurin coordinate activity-dependent bulk endocytosis through synaptojanin. The Journal of Cell Biology, Oct 2021. URL: https://doi.org/10.1083/jcb.202011028, doi:10.1083/jcb.202011028. This article has 13 citations.

7. (chen2014activitydependentfacilitationof pages 11-12): Chun-Kan Chen, Catherine Bregere, Jeremy Paluch, Jason F. Lu, Dion K. Dickman, and Karen T. Chang. Activity-dependent facilitation of synaptojanin and synaptic vesicle recycling by the minibrain kinase. Nature communications, 5:4246-4246, Jun 2014. URL: https://doi.org/10.1038/ncomms5246, doi:10.1038/ncomms5246. This article has 85 citations and is from a highest quality peer-reviewed journal.

8. (geng2016phosphorylationofsynaptojanin pages 1-2): Junhua Geng, Liping Wang, Joo Yeun Lee, Chun-Kan Chen, and Karen T. Chang. Phosphorylation of synaptojanin differentially regulates endocytosis of functionally distinct synaptic vesicle pools. The Journal of Neuroscience, 36:8882-8894, Aug 2016. URL: https://doi.org/10.1523/jneurosci.1470-16.2016, doi:10.1523/jneurosci.1470-16.2016. This article has 35 citations.

9. (jacquemyn2023parkinsonismmutationsin pages 8-9): Julie Jacquemyn, Sabine Kuenen, Jef Swerts, Benjamin Pavie, Vinoy Vijayan, Ayse Kilic, Dries Chabot, Yu-Chun Wang, Nils Schoovaerts, Nikky Corthout, and Patrik Verstreken. Parkinsonism mutations in dnajc6 cause lipid defects and neurodegeneration that are rescued by synj1. Feb 2023. URL: https://doi.org/10.1038/s41531-023-00459-3, doi:10.1038/s41531-023-00459-3. This article has 28 citations and is from a domain leading peer-reviewed journal.

10. (chen2014activitydependentfacilitationof pages 5-6): Chun-Kan Chen, Catherine Bregere, Jeremy Paluch, Jason F. Lu, Dion K. Dickman, and Karen T. Chang. Activity-dependent facilitation of synaptojanin and synaptic vesicle recycling by the minibrain kinase. Nature communications, 5:4246-4246, Jun 2014. URL: https://doi.org/10.1038/ncomms5246, doi:10.1038/ncomms5246. This article has 85 citations and is from a highest quality peer-reviewed journal.

11. (chen2014activitydependentfacilitationof pages 1-2): Chun-Kan Chen, Catherine Bregere, Jeremy Paluch, Jason F. Lu, Dion K. Dickman, and Karen T. Chang. Activity-dependent facilitation of synaptojanin and synaptic vesicle recycling by the minibrain kinase. Nature communications, 5:4246-4246, Jun 2014. URL: https://doi.org/10.1038/ncomms5246, doi:10.1038/ncomms5246. This article has 85 citations and is from a highest quality peer-reviewed journal.

12. (verstreken2015synaptojaninisrecruited pages 15-16): Patrik Verstreken, Tong-Wey Koh, Karen L. Schulze, R.Grace Zhai, P.Robin Hiesinger, Yi Zhou, Sunil Q. Mehta, Yu Cao, Jack Roos, and Hugo J. Bellen. Synaptojanin is recruited by endophilin to promote synaptic vesicle uncoating. Neuron, 40:733-748, Nov 2003. URL: https://doi.org/10.1016/s0896-6273(03)00644-5, doi:10.1016/s0896-6273(03)00644-5. This article has 502 citations and is from a highest quality peer-reviewed journal.

13. (chen2014activitydependentfacilitationof pages 11-11): Chun-Kan Chen, Catherine Bregere, Jeremy Paluch, Jason F. Lu, Dion K. Dickman, and Karen T. Chang. Activity-dependent facilitation of synaptojanin and synaptic vesicle recycling by the minibrain kinase. Nature communications, 5:4246-4246, Jun 2014. URL: https://doi.org/10.1038/ncomms5246, doi:10.1038/ncomms5246. This article has 85 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Synj-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. verstreken2015synaptojaninisrecruited pages 3-5
2. ahaley2018synaptojaninregulateshedgehog pages 1-2
3. peng2021minibrainkinaseand pages 10-12
4. jacquemyn2023parkinsonismmutationsin pages 8-9
5. geng2016phosphorylationofsynaptojanin pages 1-2
6. peng2021minibrainkinaseand pages 21-23
7. chen2014activitydependentfacilitationof pages 11-12
8. verstreken2015synaptojaninisrecruited pages 1-2
9. chen2014activitydependentfacilitationof pages 5-6
10. chen2014activitydependentfacilitationof pages 1-2
11. verstreken2015synaptojaninisrecruited pages 15-16
12. chen2014activitydependentfacilitationof pages 11-11
13. 10.15252/embj.201695773
14. 10.1083/jcb.202011028
15. 10.1007/s12038-018-9799-5
16. 10.1016/S0896-6273(03)00644-5
17. 10.1523/JNEUROSCI.1470-16.2016
18. 10.1038/s41531-023-00459-3
19. 10.7554/eLife.64922
20. https://doi.org/10.15252/embj.201695773
21. https://doi.org/10.1083/jcb.202011028
22. https://doi.org/10.1007/s12038-018-9799-5
23. https://doi.org/10.1016/S0896-6273(03
24. https://doi.org/10.1523/JNEUROSCI.1470-16.2016
25. https://doi.org/10.1038/s41531-023-00459-3
26. https://doi.org/10.7554/eLife.64922
27. https://doi.org/10.1038/s41531-023-00459-3.
28. https://doi.org/10.1016/s0896-6273(03
29. https://doi.org/10.1083/jcb.202011028,
30. https://doi.org/10.15252/embj.201695773,
31. https://doi.org/10.1007/s12038-018-9799-5,
32. https://doi.org/10.1038/ncomms5246,
33. https://doi.org/10.1523/jneurosci.1470-16.2016,
34. https://doi.org/10.1038/s41531-023-00459-3,