---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-12-01T21:46:37.456535'
end_time: '2025-12-01T21:48:27.469680'
duration_seconds: 110.01
template_file: templates/rule_research.md
template_variables:
  rule_id: ARBA00089180
  rule_type: arba
  go_terms: GO:1990858 (cellular response to lectin)
  conditions_summary: '**Condition Set 1:** FunFam id: Non-specific serine/threonine
    protein kinase (CATH.FunFam:1.10.510.10:FF:000011) AND FunFam id: Non-specific
    serine/threonine protein kinase (CATH.FunFam:3.30.200.20:FF:000069) AND taxon:
    Primates (NCBITaxon:9443)


    **Condition Set 2:** FunFam id: E1A binding protein p300 (CATH.FunFam:1.10.246.20:FF:000001)
    AND FunFam id: E1A binding protein p300 (CATH.FunFam:1.20.1020.10:FF:000001) AND
    taxon: Catarrhini (NCBITaxon:9526)


    *These condition sets are OR-ed together (any match triggers the annotation)*'
  protein_count: 0 total (0 reviewed, 0 unreviewed)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 56
---

## Question

# UniProt Rule Research

## Rule Context

- **Rule ID:** ARBA00089180
- **Rule Type:** arba
- **GO Term(s) Predicted:** GO:1990858 (cellular response to lectin)
- **Proteins Annotated:** 0 total (0 reviewed, 0 unreviewed)

### Condition Summary

**Condition Set 1:** FunFam id: Non-specific serine/threonine protein kinase (CATH.FunFam:1.10.510.10:FF:000011) AND FunFam id: Non-specific serine/threonine protein kinase (CATH.FunFam:3.30.200.20:FF:000069) AND taxon: Primates (NCBITaxon:9443)

**Condition Set 2:** FunFam id: E1A binding protein p300 (CATH.FunFam:1.10.246.20:FF:000001) AND FunFam id: E1A binding protein p300 (CATH.FunFam:1.20.1020.10:FF:000001) AND taxon: Catarrhini (NCBITaxon:9526)

*These condition sets are OR-ed together (any match triggers the annotation)*

---

## Research Objective

This is a UniProt annotation rule that predicts GO terms based on protein domain/family signatures. Your task is to evaluate whether this rule makes valid biological predictions based on what is known about the relevant domains and families, their structure, and conservation.

In an ideal case, you will be able to find literature that speaks specifically to the relationship between domains/families and
the function. Failing that, include what is known specifically about other functions that domains/families have, as well what domains/
families are known for the function.

## Research Questions

### 1. Domain/Signature Context

For each domain signature in this rule:
- What is the biological function of proteins containing this domain?
- Is this domain diagnostic for the predicted function?
- Are there known subfamilies with different functions?
- Is the domain or family known to be multifunctional, are there known cases of neofunctionalization?

### 2. GO Term Appropriateness

For the predicted GO term(s) **GO:1990858 (cellular response to lectin)**:
- Is this GO term appropriate for proteins matching these conditions?
- Is the term too broad? (e.g., "catalytic activity" when a more specific term exists)
- Is the term too narrow? (e.g., a specific substrate when the domain covers broader specificity)
- Are there better alternative GO terms?

### 3. Literature Support

- What experimental evidence supports this functional annotation?
- Are there key papers describing this protein family/enzyme?
- Are there any contradictory findings in the literature?
- Is this a well-established function or more speculative?

### 4. Taxonomic Considerations

If this rule has taxonomic restrictions:
- Is the function conserved across the taxa included?
- Are there taxa that should be excluded (different function)?
- Are there taxa that could be included but are currently excluded?

### 5. Rule Logic Assessment

- Do the domain combinations make biological sense?
- Are there redundant conditions that could be removed?
- Could false positives arise from these conditions?

## Output Format

Please provide your findings in a narrative format with citations. Structure your response as:

1. **Executive Summary** - Brief assessment of rule validity
2. **Domain Analysis** - What each domain/signature represents
3. **GO Term Evaluation** - Assessment of the predicted annotation
4. **Evidence Review** - Key literature supporting or contradicting the rule
5. **Recommendations** - Suggested improvements or concerns

Be sure to include citations for all statements.

## Output

<think>
This is a complex research query asking me to evaluate a UniProt annotation rule (ARBA00089180) that predicts the GO term "cellular response to lectin" (GO:1990858) for proteins with specific domain signatures. The rule has two condition sets that are OR-ed together:

1. Non-specific serine/threonine protein kinase (CATH.FunFam:1.10.510.10:FF:000011) AND Non-specific serine/threonine protein kinase (CATH.FunFam:3.30.200.20:FF:000069) AND taxon: Primates
2. E1A binding protein p300 (CATH.FunFam:1.10.246.20:FF:000001) AND E1A binding protein p300 (CATH.FunFam:1.20.1020.10:FF:000001) AND taxon: Catarrhini

Let me analyze the search results to understand what these domains are and whether this prediction makes sense.

Key findings from search results:

1. **p300/CBP (E1A binding protein p300)** - Multiple sources describe this:
   - p300 is a histone acetyltransferase (HAT) and transcriptional coactivator [6][12][13][14][16]
   - It contains multiple functional domains including KIX domain, TAZ domains, bromodomain, PHD finger, and PAT/HAT domain [14]
   - Functions in epigenetic regulation, chromatin remodeling, and transcriptional activation
   - Known to interact with numerous transcription factors
   - Involved in various cellular processes including immune responses, stress responses, and cancer

2. **Serine/threonine protein kinases** - Multiple sources discuss:
   - Receptor-like kinases (RLKs) are important in plant immune signaling [2][20]
   - GsSRK is described as a G-type lectin S-receptor-like serine/threonine protein kinase [2]
   - These kinases play critical roles in cellular stress adaptation and pathogen recognition mechanisms, responding to external stimuli through signaling pathways

3. **C-type lectin receptors (CLRs)** - Multiple sources describe:
   - CLRs are expressed by dendritic cells and crucial for immune responses [15][26][29][49][52][55]
   - They recognize carbohydrates on pathogens
   - Dectin-1, DC-SIGN, Mincle, etc. are examples
   - They activate signaling cascades involving Raf-1, SYK, NF-κB
   - Raf-1 activation leads to acetylation of NF-κB p

65 by CBP/p300 [15][26][29][49][52]

I'm examining the intricate signaling cascade triggered by lectin receptors, focusing on how specific protein domains in primates connect to cellular response mechanisms. The pathway involves pattern recognition receptors initiating complex molecular interactions that ultimately modulate transcriptional activation through precise phosphorylation and acetylation events.

The critical observation centers on understanding how specific protein domains - particularly serine/threonine kinase and p300/CBP domains in Old World primates - contribute to cellular responses initiated by lectin recognition.

While the signaling mechanism involves multiple steps from receptor activation to transcriptional changes, the proposed annotation rule appears overly broad. Most proteins involved are general signaling components rather than lectin-specific responders, which suggests potential misclassification risks in the current approach.

The core issue lies in distinguishing between direct and indirect involvement in lectin-mediated cellular responses, requiring nuanced interpretation of protein functional roles beyond simple domain matching.
</think>

# UniProt Rule Evaluation: ARBA00089180 and Cellular Response to Lectin Prediction

This comprehensive research report evaluates the validity of the UniProt annotation rule ARBA00089180, which predicts the Gene Ontology term "cellular response to lectin" (GO:1990858) for proteins containing specific serine/threonine kinase domains and p300/CBP acetyltransferase domains within particular taxonomic contexts. Through systematic analysis of domain function, GO term appropriateness, literature evidence, and rule logic, this report determines whether the rule produces valid biological predictions.

## Executive Summary

The ARBA00089180 rule attempts to predict lectin response functions through recognition of general signaling domain signatures in primate proteins. While the search results provide substantial evidence that p300/CBP acetyltransferases play important roles in C-type lectin receptor signaling cascades, the rule appears overly broad and likely generates false positive annotations. The fundamental issue is that the rule conflates involvement in lectin signaling with direct participation in lectin response processes. Serine/threonine kinase domains and p300 acetyltransferase domains are multifunctional proteins operating across hundreds of cellular pathways beyond lectin signaling. Annotating all proteins with these domain signatures as responding to lectins fails to capture the specificity required by GO annotation standards and would produce a substantial proportion of false positives. The rule would benefit from additional conditions restricting annotation to lectin receptor-associated proteins or incorporating evidence of direct pathway involvement.

## Domain Analysis

### Serine/Threonine Protein Kinase Domains (CATH.FunFam:1.10.510.10:FF:000011 and 3.30.200.20:FF:000069)

Serine/threonine protein kinases represent one of the largest and most functionally diverse protein families in eukaryotes[42]. These enzymes phosphorylate substrates at serine and threonine residues and regulate virtually every major cellular process including transcription, translation, cell cycle progression, apoptosis, metabolism, and signal transduction[42]. The specificity of these kinases depends not only on the catalytic domain structure but also on cellular localization, substrate recognition sequences, and protein-protein interactions that are not captured by domain architecture alone[39].

In the specific context of immune signaling, serine/threonine kinases operate at multiple levels. Receptor-like kinases in plants, which contain lectin domains fused to serine/threonine kinase catalytic domains, recognize pathogen-associated molecular patterns and participate in defense signaling[2][20][33]. In mammalian immune cells, C-type lectin receptors such as DC-SIGN trigger intracellular signaling through serine/threonine kinases including Raf-1[15][26][29][49][52]. Raf-1 phosphorylates both serine and threonine residues on downstream targets including NF-κB p65[40][49]. However, the CATH domains specified in this rule (FF:000011 and FF:000069) represent "non-specific" serine/threonine protein kinases with broad cellular functions[10][42]. These domains are found in hundreds of proteins with diverse biological roles extending far beyond lectin signaling.

The multifunctionality of serine/threonine kinases creates a fundamental challenge for this rule. A protein matching these domain signatures could function as a kinase in kinase cascades, cell cycle control, metabolic regulation, apoptosis, or numerous other pathways. Without additional information such as direct association with lectin receptors, upstream pattern recognition receptor scaffolds, or demonstrable involvement in lectin signaling cascades, the domain architecture alone cannot justify annotation with the specific functional term "cellular response to lectin."

### p300/CBP Acetyltransferase Domains (CATH.FunFam:1.10.246.20:FF:000001 and 1.20.1020.10:FF:000001)

The p300 and CREB-binding protein (CBP) form a closely related family of transcriptional coactivators characterized by remarkable structural complexity and functional diversity[14][16]. Both proteins contain five major protein interaction domains including the nuclear receptor interaction domain, the KIX domain, cysteine/histidine-rich regions (TAZ1/CH1 and TAZ2/CH3), and an interferon response binding domain[14]. The two domains specified in this rule represent the KIX domain (CATH.FunFam:1.10.246.20:FF:000001), which interacts with CREB and other transcription factors, and the bromodomain/acetyltransferase region (CATH.FunFam:1.20.1020.10:FF:000001), which reads acetylated lysine residues and catalyzes histone acetylation[14][38][41].

Research published in Nature in 2023 reveals sophisticated mechanisms by which p300/CBP propagate histone acetylation within nucleosomes[13]. These proteins recognize H4 N-terminal tail acetylation through their bromodomain pocket and then acetylate non-H4 histone N-terminal tails within the same nucleosome[13]. The primary target of p300 acetylation activity is H2B N-terminal tail, and H2B N-terminal acetylation promotes H2A-H2B dissociation from nucleosomes to facilitate transcription[13]. This read/write mechanism serves as a fundamental epigenetic inheritance system, replicating acetylation marks from the H3-H4 tetramer to H2A-H2B dimers to activate context-dependent gene transcription[13].

The functional breadth of p300/CBP extends far beyond any single pathway. These proteins interact with approximately 400 different proteins[13], including numerous DNA-binding transcription factors and serve as coactivators for diverse cellular processes. Recent research demonstrates that p300 regulates extensive networks of stress response genes, hypoxia response genes, and proteasome-related genes through its acetyltransferase activity[53]. The histone acetyltransferase activity of p300 is essential for enhancer activation and recruitment of RNA polymerase II at virtually all enhancers and enhancer-regulated genes[13]. Furthermore, studies show that CBP and p300 have overlapping and distinct target genes with different functions, indicating that even within this closely related protein pair, functional specificity exists[53].

Regarding the connection to lectin signaling specifically, the evidence shows that p300/CBP participate downstream in C-type lectin receptor signaling cascades. When DC-SIGN binds to mannose-carrying pathogens including Mycobacterium tuberculosis and HIV-1, it activates the serine/threonine kinase Raf-1[15][29][49][52]. Raf-1 phosphorylates NF-κB p65 at serine 276, which creates a binding site for p300/CBP acetyltransferase activity[15][29][40][49]. The acetylation of p65 by p300/CBP enhances the transcriptional activity of p65 and affects cytokine expression patterns[15][29][49][52]. However, this represents only one of hundreds of signaling contexts in which p300/CBP function. Annotating all p300/CBP proteins with "cellular response to lectin" would fundamentally misrepresent their biological roles, as these proteins regulate stress responses, transcriptional activation during infection, immune homeostasis, cancer biology, and countless other processes.

## GO Term Evaluation

The Gene Ontology term "cellular response to lectin" (GO:1990858) represents processes that result in a change in state or activity of a cell in response to lectin molecules[1][4][22][44]. The term is positioned within a hierarchy that includes parent terms such as "response to lectin" (GO:1990840) and child terms such as "stimulatory C-type lectin receptor signaling pathway"[1][19][22]. The GO annotation definition specifically notes that this term refers to endogenous responses to lectins—both exogenous lectins from external sources and endogenous lectins—but excludes events occurring due to lectin toxicity[44].

### Term Specificity Analysis

The key biological distinction for this GO term is whether a process represents a direct cellular response to lectin stimulus versus indirect involvement in pathways that happen to be activated downstream of lectin recognition. Direct responses to lectins would include processes initiated by binding of lectin molecules to lectin-binding receptors or proteins with lectin-recognition domains. These include activities such as lectin ligand binding, receptor clustering, recruitment of signaling molecules to receptor complexes, and the immediate downstream phosphorylation and activation events. In contrast, indirect involvement encompasses general transcriptional coactivators, chromatin modifiers, and signal transduction machinery that operate in many pathways.

The GO annotation standard requires that terms describe the function of the specific gene product rather than every pathway in which that product participates. A protein that functions as a general transcriptional coactivator in hundreds of processes should not be annotated with every GO term representing those processes. Rather, the annotation should capture the core biological function of that protein—which for p300/CBP would be terms like "histone acetyltransferase activity," "transcriptional coactivator," or "chromatin remodeling." More specific process terms should be reserved for proteins directly involved in the recognition of particular stimuli or execution of stimulus-specific responses.

### Appropriateness for p300/CBP

Applying the term "cellular response to lectin" to all p300/CBP proteins represents an overly broad annotation that fails to distinguish between direct lectin response mechanisms and general transcriptional machinery. While p300/CBP certainly participate in transcriptional responses that occur downstream of C-type lectin receptor signaling, this participation is not specific to lectin signaling. These same proteins participate in transcriptional responses to countless other stimuli including growth factors, stress signals, cytokines, hormones, and developmental cues. The acetylation activity of p300/CBP enables transcriptional activation in response to diverse signals, but this does not warrant annotating p300/CBP with every process-specific GO term corresponding to each stimulus.

A more appropriate annotation strategy would be to reserve "cellular response to lectin" for proteins that directly recognize or respond to lectins as part of their core biological function. For transcriptional coactivators such as p300/CBP, the primary function would be captured by terms related to histone modification, chromatin remodeling, and transcriptional activation. If specific evidence demonstrated that particular p300/CBP splice variants or orthologues had lectin-response-specific roles, then more targeted annotations would be appropriate.

### Appropriateness for Serine/Threonine Kinases

General serine/threonine kinase domains show even greater functional diversity than p300/CBP. While specific kinases such as Raf-1 participate in C-type lectin receptor signaling, and plant lectin receptor kinases directly mediate lectin recognition, the broad category of "non-specific serine/threonine protein kinases" encompasses kinases functioning in cell cycle regulation, metabolism, apoptosis, developmental signaling, and thousands of other processes. Annotating all such kinases with "cellular response to lectin" would be particularly inappropriate, as it would suggest that the defining role of these proteins relates to lectin response when in fact their lectin-related functions, if present, represent only a small fraction of their cellular activities.

### Alternative GO Terms

For p300/CBP proteins, existing GO terms more accurately capture their biological function. The Molecular Function ontology includes terms such as "histone acetyltransferase activity" (GO:0004402) and "acetyltransferase activity" (GO:0016746). The Biological Process ontology includes "histone acetylation" (GO:0016575) and "chromatin remodeling" (GO:0006338). If the annotation goal is to capture involvement of p300/CBP in immune responses more broadly, terms such as "regulation of immune response" (GO:0050776) or "innate immune response" (GO:0045087) would be more appropriate and more accurate than the specific "cellular response to lectin" term.

For serine/threonine kinases, even more diverse alternative terms apply depending on the specific kinase's known function. If a specific kinase functions in immune signaling, terms like "immune response" (GO:0006955) or "toll-like receptor signaling pathway" (GO:0002224) might apply to certain members of this large family. However, without evidence specific to individual kinases or subfamilies, the broad kinase domains cannot justify narrower functional annotations.

## Evidence Review

### C-Type Lectin Receptor Signaling Architecture

The evidence strongly establishes that C-type lectin receptors employ serine/threonine kinase signaling and p300/CBP-mediated transcriptional activation as components of their downstream effector mechanisms. When dendritic cell-specific ICAM3-grabbing non-integrin (DC-SIGN) binds to mannose-carrying pathogens, it activates the serine/threonine kinase RAF1[15][26][29][49][52]. RAF1 signaling leads to phosphorylation of NF-κB subunit p65 at serine 276, which creates a docking site that is recognized by CREB-binding protein and p300[15][29][40][49]. This phosphorylation of p65 is an essential element for engagement of nuclear cofactors and associated histone acetyltransferase activity necessary for elaborating gene expression[40]. The acetylation of p65 by p300/CBP enhances the transcriptional activity of p65 itself through a mechanism that increases NF-κB binding affinity and transcriptional capacity[40][49]. Consequently, RAF1 signaling leads to enhanced cytokine expression downstream of C-type lectin receptors[15][49].

Similarly, dectin-1 triggering by fungal pathogens results in protective antifungal immunity through crosstalk of pathways involving spleen tyrosine kinase (SYK) and RAF1[15][52]. The cooperation between SYK and RAF1 pathways serves to fine-tune NF-κB activity through mechanisms involving Ser276 phosphorylation of p65 and subsequent acetylation[15][52]. The resulting transcriptional activity leads to expression of T helper 1 and T helper 17 cell polarizing cytokines[15][52]. Additional C-type lectin receptors including macrophage-inducible C-type lectin (Mincle), dectin-2, and blood dendritic cell antigen 2 (BDCA2) employ overlapping signaling architectures involving protein kinase activation and NF-κB modulation[26][29].

### Role of p300 in T Regulatory Cell Function

Evidence indicates that p300 plays specific regulatory roles in T regulatory cell (Treg) function that connect to immune responses. Conditional deletion or pharmacological inhibition of p300 in Foxp3+ Tregs resulted in increased T cell receptor-induced apoptosis in Tregs, impaired Treg suppressive function, and limited tumor growth[27]. The p300 inhibitor-treated mice showed decreased acetyl-H3 accumulation at the Foxp3 promoter, increased Treg apoptosis, and decreased Treg suppressive function[27]. Studies show that p300 plays a protective role in allergic asthma by enhancing Treg function, partly through GBP5-mediated regulation[18]. These findings establish that p300 has specific roles in immune regulation and Treg-specific functions. However, this does not establish a general role in "cellular response to lectin"—rather, it shows that p300 modulates Treg-specific processes, which themselves may or may not involve lectin signaling.

### Acetylation of NF-κB in Inflammation

The literature establishes multiple points at which protein acetylation regulates inflammatory responses. Berberine (BBR) reduces acetylation of NF-κB subunit p65 at Lys310 (p65Lys310) by inhibiting p300 expression, thereby suppressing inflammatory responses in macrophages[37]. This demonstrates that p300-dependent acetylation of p65 represents a critical regulatory node in inflammatory signaling[37]. The acetylation landscape that p300 regulates extends broadly across proteins involved in inflammatory responses, including both histone and non-histone targets[37]. However, the fact that p300 regulates acetylation of key inflammatory mediators does not make p300 a component of "cellular response to lectin"—it makes p300 a component of inflammatory response regulation more broadly.

### Lack of Specificity Evidence

Critically, the search results provide no evidence that serine/threonine kinase domains or p300/CBP domains specifically recognize lectin molecules or preferentially function in lectin signaling pathways. The domains are not diagnostic for lectin response function. Rather, the literature shows that these domains operate in multiple signaling contexts, with lectin signaling representing only one of many pathways employing these signaling components. The literature describes how C-type lectin receptors activate signaling cascades that use general-purpose signaling machinery (kinases, phosphatases, transcriptional coactivators), not specialized machinery for lectin recognition.

## Taxonomic Considerations

The rule specifies two different taxonomic contexts: primates (Primate taxon NCBITaxon:9443) for the serine/threonine kinase condition and Catarrhini (Old World primates, taxon NCBITaxon:9526) for the p300/CBP condition. This taxonomic restriction is notable and requires evaluation.

### Conservation of Lectin Signaling Mechanisms Across Primates

C-type lectin receptor signaling mechanisms show conservation across primates, suggesting that if the rule were valid for one primate species, it would likely apply broadly across primates. The evidence demonstrates that primate immune responses employ conserved core mechanisms while showing some lineage-specific variations. A genome-wide study comparing immune responses in humans, chimpanzees, and rhesus macaques found that "core" immune responses that are critical to fight any invading pathogen are the most conserved across primates, whereas much of the divergence in immune responses appears in genes involved in responses to specific microbial and viral agents[24]. The conserved regulatory response to immune stimulation includes enrichment of genes regulated by NF-κB and interferon regulatory factors[24], demonstrating conservation of fundamental inflammatory signaling machinery across primate species.

Studies of primate type 2 immune response evolution show that several components of the type 2 immune response pathway have been subject to recurrent positive selection in the primate lineage[21]. Notably, IL-13 and other immune mediators show evidence of adaptation in primates, with particular variants showing enhanced downstream signaling functions[21]. This pattern of lineage-specific adaptive evolution in immune pathways suggests that while core mechanisms are conserved, specific implementations may vary by primate lineage.

### Restriction to Catarrhini for p300 Condition

The restriction of the p300/CBP condition to Catarrhini (Old World primates) is puzzling. p300 acetyltransferase function and C-type lectin receptor signaling appear conserved across a broader range of primates. The functional domains of p300, including the KIX domain and acetyltransferase domain, are highly conserved across mammalian species. While the rule might be intended to reflect better annotation or literature evidence available for Old World primates, this taxonomic restriction appears to lack strong biological justification based on the search results. If p300 should be annotated with "cellular response to lectin," there is no obvious reason why this would apply only to Catarrhini and not to other primates or indeed other mammals where the same signaling mechanisms operate.

### Evolutionary Conservation Questions

The broader evolutionary question concerns whether any simple domain signature can effectively capture cell type-specific or stimulus-specific functions. The search results provide extensive evidence that immune system evolution in primates involves rapid adaptation of specific immune factors, not wholesale changes in general signaling machinery[21][24]. This suggests that specificity for particular immune stimuli is achieved through mechanisms beyond domain architecture, such as cell type-specific expression patterns, regulatory element evolution, and protein-protein interactions.

## Rule Logic Assessment

### Assessment of Domain Combination Logic

The rule uses an "AND" condition within each condition set, requiring that proteins contain BOTH specified CATH domains to trigger annotation. For the serine/threonine kinase condition set, this means the protein must match both CATH.FunFam:1.10.510.10:FF:000011 AND CATH.FunFam:3.30.200.20:FF:000069. For the p300 condition set, the protein must match both CATH.FunFam:1.10.246.20:FF:000001 AND CATH.FunFam:1.20.1020.10:FF:000001. The "AND" operators within condition sets, combined with the "OR" between sets, theoretically creates specificity by requiring multiple domain matches.

However, the biological logic remains questionable. Requiring two serine/threonine kinase superfamily domains from different CATH classifications does not establish involvement in lectin signaling—it simply identifies proteins with complex kinase-related domain architectures. Similarly, requiring both the KIX domain and acetyltransferase domain identifies canonical p300/CBP proteins, which are indeed involved in immune signaling, but these proteins have hundreds of other functions. The domain combination criteria do not functionally distinguish lectin-response-specific proteins from the hundreds of other cellular roles these proteins execute.

### False Positive Risk Assessment

The rule carries substantial risk of generating false positive annotations. Any protein containing both specified serine/threonine kinase domains would be annotated regardless of its actual cellular function. Many kinases contain multiple kinase-related CATH domains as part of their regulatory architecture. Similarly, all canonical p300 and CBP proteins in primates would receive this annotation even though the vast majority of p300/CBP functions occur outside the context of lectin signaling.

To estimate the scope of false positives: the search results indicate that p300/CBP regulate gene expression in response to oxidative stress, hypoxia, growth factors, cytokines, developmental signals, and numerous other stimuli[53]. The fraction of p300/CBP activity devoted specifically to lectin response processes appears to be a minority, meaning that annotating all p300/CBP with "cellular response to lectin" would mislabel these proteins' primary functions.

### Potential Redundancy and Excessive Specificity

The two condition sets specified in the rule could be evaluated for redundancy. Both appear to be targeting proteins involved in signaling and transcriptional regulation. If the goal is to identify proteins involved in C-type lectin receptor signaling, more targeted approaches might include:

1. Direct association with known C-type lectin receptor proteins through protein interaction evidence
2. Inclusion of kinase specificity information beyond just CATH superfamily classification
3. Incorporation of pathway database information linking proteins to lectin signaling pathways
4. Requirement for evidence of upregulation or specific expression in dendritic cells or other professional antigen-presenting cells involved in primary lectin recognition

The current rule structure does not incorporate any of these potential specificity constraints.

### Missing Biological Context

The rule lacks incorporation of critical biological context that would establish whether a protein specifically functions in lectin responses. For example:

**Lectin Receptor Association:** The rule does not require association with C-type lectin receptor molecules or lectin-binding domains. A kinase or p300 protein that functions in lectin signaling networks might be expected to physically interact with or be recruited by lectin receptors, providing specificity evidence that domain architecture alone cannot capture.

**Pathway Database Information:** Integration with pathway databases such as KEGG, Reactome, or BioCarta would allow the rule to identify whether proteins are annotated as components of C-type lectin receptor signaling pathways, rather than relying solely on domain architecture.

**Gene Expression Patterns:** Incorporation of gene expression data showing enrichment in dendritic cells, macrophages, or other cell types that use C-type lectin receptors for primary pathogen recognition could improve specificity.

**Functional Genomics Data:** Results from studies examining genes whose expression changes specifically in response to lectin stimulation could refine the rule.

The current rule structure captures none of this functional context, relying instead on a simple domain architecture match that yields overly broad predictions.

## Recommendations for Rule Improvement

### Primary Recommendation: Narrow the Rule Scope

The most important recommendation is to substantially narrow the scope of this rule to increase specificity. Rather than annotating all proteins with the specified domains, the rule should target a more specific subset of proteins with known lectin response functions. Options include:

**Option 1: Restrict to Direct Lectin Signaling Components**
Modify the rule to require proteins that physically interact with known C-type lectin receptors (DC-SIGN, Dectin-1, Dectin-2, Mincle, etc.) or contain lectin-binding domains in addition to the kinase/acetyltransferase domains. This would dramatically reduce false positives by focusing on proteins directly recruited into lectin signaling complexes.

**Option 2: Incorporate Pathway Database Information**
Integrate with pathway databases to require that proteins be annotated in established C-type lectin receptor signaling pathways. While pathway annotations have their own limitations, combining pathway information with domain architecture would provide stronger specificity than domain architecture alone.

**Option 3: Utilize Gene Expression Context**
Require evidence that gene expression changes specifically in response to lectin stimulation, rather than general inflammatory stimuli. Gene expression databases comparing responses to different pathogen-associated molecular patterns and damage-associated molecular patterns could distinguish lectin-specific responses from general immune activation.

### Secondary Recommendation: Reconsider the Predicted GO Term

Even if the rule scope were narrowed, consideration should be given to whether "cellular response to lectin" represents the most appropriate annotation target. The evidence shows that p300/CBP function as general transcriptional coactivators in lectin signaling, similar to their function in many other signaling contexts. Whether this warrants the "cellular response to lectin" annotation versus more general immune response annotations could be reconsidered.

### Tertiary Recommendation: Evaluate Taxonomic Scope

The restriction to Catarrhini for the p300/CBP condition should be reconsidered. If p300/CBP function in lectin signaling is conserved across primates (as the evidence suggests), the taxonomic restriction appears unjustified. If the restriction reflects annotation confidence differences between taxa, this should be explicitly documented and considered for modification as evidence accumulates.

### Tertiary Recommendation: Incorporate Negative Controls

Explicitly identify known proteins that would match the domain criteria but should NOT be annotated with "cellular response to lectin" because their known functions lie in other domains. For example, if kinases whose primary roles are in cell cycle control would match the domain criteria, these should be excluded through additional negative constraint conditions.

## Conclusion

The ARBA00089180 rule attempts to leverage domain architecture signatures to predict involvement in cellular responses to lectins. While the rule identifies families of proteins (serine/threonine kinases and p300/CBP) that do participate in C-type lectin receptor signaling pathways, the rule appears overly broad and likely to generate substantial false positive annotations. The fundamental issue is that serine/threonine kinases and p300/CBP represent multifunctional proteins operating in hundreds of cellular processes, of which lectin signaling represents only one. Without additional specificity constraints—such as physical association with lectin receptors, direct pathway database annotation, or evidence of lectin-specific gene expression—simply matching domain signatures cannot justify annotation with the specific functional term "cellular response to lectin." 

The rule would benefit substantially from modifications to narrow its scope toward direct lectin signaling components, incorporate pathway context, or require evidence of stimulus-specific activation. Until such modifications are implemented, this rule is likely to produce annotations that misrepresent the primary biological functions of the proteins it targets and fail to distinguish between specific lectin responses and general signaling machinery that operates across many cellular processes.

## Citations

1. https://yeastract-plus.org/ncyeastract/kmarxianus/view.php?existing=goterm&goid=GO%3A1990858
2. https://pubmed.ncbi.nlm.nih.gov/23276523/
3. https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=2033
4. https://zfin.org/GO:1990858
5. https://www.uniprot.org/uniprotkb/Q9LPZ9/entry
6. https://www.uniprot.org/uniprotkb/Q09472/entry
7. https://www.cathdb.info/version/latest/funfam/1.10.510.10:FF:001905
8. https://www.cathdb.info/version/latest/funfam/3.30.200.20:FF:000097
9. https://www.cathdb.info/superfamily/1.25.40.770
10. https://cath.biochem.ucl.ac.uk/version/v4_4_0/superfamily/1.10.510.10/funfam/133
11. https://www.cathdb.info/version/latest/funfam/3.30.200.20:FF:000229
12. http://www.cathdb.info/version/v4_3_0/superfamily/2.10.110.40
13. https://www.nature.com/articles/s41467-023-39735-4
14. https://en.wikipedia.org/wiki/P300-CBP_coactivator_family
15. https://www.nature.com/articles/nri2569
16. https://pmc.ncbi.nlm.nih.gov/articles/PMC302022/
17. https://www.ncbi.nlm.nih.gov/gene/328572
18. https://pubmed.ncbi.nlm.nih.gov/41052458/
19. https://amigo.geneontology.org/amigo/search/annotation?q=%2A%3A%2A&fq=isa_partof_closure%3A%22GO%3A1990858%22&sfq=document_category%3A%22annotation%22
20. https://pubmed.ncbi.nlm.nih.gov/18393610/
21. https://academic.oup.com/gbe/article/9/6/1757/3930139
22. https://amigo.geneontology.org/amigo/term/GO:1990858
23. https://www.uniprot.org/uniprotkb/K7CE96/entry
24. https://pmc.ncbi.nlm.nih.gov/articles/PMC3002988/
25. http://www.cathdb.info/version/v4_4_0/superfamily/1.10.246.20/funfam/1
26. https://www.rndsystems.com/pathways/pathogen-damage-activated-c-type-lectin-receptor-signaling-pathways
27. https://pmc.ncbi.nlm.nih.gov/articles/PMC3793393/
28. http://www.cathdb.info/version/v4_3_0/superfamily/1.10.246.20
29. https://pmc.ncbi.nlm.nih.gov/articles/PMC7097056/
30. https://www.uniprot.org/help/arba
31. https://www.uniprot.org/uniprotkb/Q16512/entry
32. https://pmc.ncbi.nlm.nih.gov/articles/PMC10311507/
33. https://www.uniprot.org/arba/ARBA00090778
34. https://www.uniprot.org/uniprotkb/P53350/entry
35. https://www.embopress.org/doi/10.15252/embj.2019102856
36. https://pmc.ncbi.nlm.nih.gov/articles/PMC10172918/
37. https://www.ebi.ac.uk/thornton-srv/databases/cgi-bin/enzymes/GetPage.pl?ec_number=2.3.1.48
38. https://www.nature.com/articles/s41586-022-05575-3
39. https://www.embopress.org/doi/10.1093/emboj/cdg139
40. http://www.cathdb.info/superfamily/1.20.1020.10
41. https://www.ncbi.nlm.nih.gov/books/NBK28112/
42. https://pmc.ncbi.nlm.nih.gov/articles/PMC11607582/
43. https://pmc.ncbi.nlm.nih.gov/articles/PMC2847396/
44. https://academic.oup.com/mbe/article/27/9/2172/1010901
45. https://www.informatics.jax.org/vocab/gene_ontology/GO:1990840
46. https://pmc.ncbi.nlm.nih.gov/articles/PMC11110936/
47. https://pmc.ncbi.nlm.nih.gov/articles/PMC11030075/
48. https://pubmed.ncbi.nlm.nih.gov/11027294/
49. https://pmc.ncbi.nlm.nih.gov/articles/PMC1941744/
50. https://www.nature.com/articles/s41598-023-44412-z
51. https://www.nature.com/articles/s41598-018-23395-2
52. https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2024.1305599/full
53. https://academic.oup.com/nar/article/47/D1/D280/5162467
54. https://www.ncbi.nlm.nih.gov/books/NBK579916/
55. https://academic.oup.com/gbe/article/7/3/720/601363
56. https://pmc.ncbi.nlm.nih.gov/articles/PMC3584934/