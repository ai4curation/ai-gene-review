---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-12-01T19:49:16.349594'
end_time: '2025-12-01T19:51:11.498422'
duration_seconds: 115.15
template_file: templates/rule_research.md
template_variables:
  rule_id: ARBA00089176
  rule_type: arba
  go_terms: GO:1990840 (response to lectin)
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
citation_count: 52
---

## Question

# UniProt Rule Research

## Rule Context

- **Rule ID:** ARBA00089176
- **Rule Type:** arba
- **GO Term(s) Predicted:** GO:1990840 (response to lectin)
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

For the predicted GO term(s) **GO:1990840 (response to lectin)**:
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
Let me analyze this UniProt rule research query. The user is asking me to evaluate whether an annotation rule makes valid biological predictions. The rule predicts "GO:1990840 (response to lectin)" based on specific domain/family signatures.

Let me break down what I'm being asked to do:

1. Evaluate whether the rule ARBA00089176 makes valid biological predictions
2. For each domain signature, understand its biological function
3. Assess if the GO term is appropriate
4. Find literature support
5. Consider taxonomic restrictions
6. Assess the overall rule logic

The rule has two main conditions:
- Condition Set 1: Non-specific serine/threonine protein kinase (CATH.FunFam:1.10.510.10:FF:000011) AND Non-specific serine/threonine protein kinase (CATH.FunFam:3.30.200.20:FF:000069) AND taxon: Primates
- Condition Set 2: E1A binding protein p300 (CATH.FunFam:1.10.246.20:FF:000001) AND E1A binding protein p300 (CATH.FunFam:1.20.1020.10:FF:000001) AND taxon: Catarrhini

Looking at my search results:

For serine/threonine kinases and response to lectin:
- Search result [6] discusses C-type lectin receptors and DC-SIGN signaling, mentioning that DC-SIGN induces RAF1 (a serine/threonine kinase) activation
- Search result [9] and [39] specifically discuss DC-SIGN triggering RAF1 activation
- Search result [18] discusses c-Raf and its role in signaling
- Search result [30] discusses Raf-1 autoregulation
- Search result [42] discusses serine/threonine kinases in B cells


- For p300/CBP, the literature shows these proteins function as coactivators in immune responses and stress pathways. Search results [7], [12], [15], [19], [22], [37], [40], [49], and [52] collectively indicate p300/CBP involvement in transcriptional regulation, histone acetylation, and cellular stress responses, though direct lectin response connections are less explicit than the kinase pathway.

- Lectin response itself is characterized in results [3], [5], [26], [29] as endogenous cellular reactions to lectin stimulation.

The prediction rule linking domain signatures and taxa to lectin response function seems problematic at first—serine/threonine kinases and p300 are broadly used across many signaling contexts, so their presence alone shouldn't necessarily indicate lectin specificity. But the evidence suggests this pathway does operate: DC-SIGN, a C-type lectin receptor, activates RAF1 (a serine/threonine kinase) when responding to pathogenic lectins, and RAF1-mediated signaling appears to connect to downstream transcriptional responses.
</think>

# Comprehensive Evaluation of UniProt Rule ARBA00089176: Predicting Response to Lectin Function

## Executive Summary

The annotation rule ARBA00089176 predicts the Gene Ontology term "response to lectin" (GO:1990840) for proteins matching either of two condition sets involving serine/threonine protein kinases and E1A binding protein p300 with taxonomic restrictions to primates or catarrhines. While there is credible literature support for a biological connection between these molecular signatures and lectin-induced signaling responses, particularly through the DC-SIGN-RAF1-p300 pathway, the rule exhibits significant limitations that could produce both false positives and false negatives. The rule conflates general signaling machinery with specific pathway participation and relies on domain signatures that are inherently multifunctional across numerous cellular contexts.

---

## Domain Analysis: Molecular Signatures and Biological Functions

### Serine/Threonine Protein Kinases (CATH.FunFam:1.10.510.10:FF:000011 and 3.30.200.20:FF:000069)

**General Function and Domain Architecture**

Serine/threonine protein kinases represent one of the largest families of signaling enzymes in eukaryotic cells[18]. These enzymes catalyze the phosphorylation of hydroxyl groups on serine or threonine residues within target proteins, thereby modulating protein activity, localization, and protein-protein interactions[42]. The RAF proto-oncogene serine/threonine-protein kinase (RAF1, also known as c-Raf), which is specifically implicated in lectin signaling pathways, is part of the mitogen-activated protein kinase kinase kinase (MAP3K) family and functions downstream of Ras proteins in the classic ERK1/2 signaling cascade[18][21].

The architectural features of RAF1 include a Ras-binding domain (RBD) at its N-terminus and a cysteine-rich domain (C1 domain) that mediates lipid interactions and provides regulatory functions[18]. The C1 domain, unlike the corresponding domains in protein kinase C enzymes, does not bind diacylglycerol but instead interacts with ceramide and phosphatidic acid while facilitating recognition of activated Ras proteins[18]. Between the autoinhibitory regulatory domains and the catalytic kinase domain lies a highly flexible, serine-enriched hinge region that permits conformational rearrangements essential for activation[18].

**Multifunctionality and Subfamilies**

The serine/threonine kinase family demonstrates remarkable functional diversity. Within B cells, for example, multiple STKs including Akt, MAPK, and Raf regulate distinct aspects of cell survival, proliferation, differentiation, and apoptosis[42]. Different members regulate BCR signaling, germinal center B cell class switching, and somatic hypermutation through non-redundant mechanisms[42]. In bacterial pathogens, serine/threonine kinases regulate virulence and cell wall homeostasis, demonstrating that these enzymes serve fundamentally different biological roles depending on cellular context and substrate specificity[45].

**Relevance to Lectin Signaling**

The connection between serine/threonine kinases and lectin responses emerges specifically through RAF1's documented role in C-type lectin receptor (CLR) signaling. When DC-SIGN, a C-type lectin receptor expressed on dendritic cells, binds to mannose-carrying pathogens including *Mycobacterium tuberculosis*, HIV-1, and *Candida albicans*, it induces an intracellular signaling cascade with RAF1 as the central component[6][9][36][39]. Following pathogen binding, DC-SIGN triggers the activation of Ras through an as-yet unidentified Ras guanine exchange factor, allowing GTP-loaded Ras to interact with RAF1's N-terminal Ras-binding domain[39]. This interaction alone proves insufficient for full RAF1 activation; the kinase additionally requires phosphorylation at tyrosine residues 340/341 by Src-family kinases (particularly Lyn, Hck, or Fgr in dendritic cells) and at serine residue 338 by p21-activated kinases (PAKs) downstream of Rho GTPases[39].

### E1A Binding Protein p300 (CATH.FunFam:1.10.246.20:FF:000001 and 1.20.1020.10:FF:000001)

**Core Functions as Transcriptional Coactivator**

The E1A-associated protein of 300 kDa (p300) and its highly homologous paralog CREB-binding protein (CBP) represent founding members of the KAT3 family of histone acetyltransferases[7][40]. These proteins function as master coactivators of transcription through multiple complementary mechanisms: they physically bridge transcription factors to the RNA polymerase II machinery, acetylate histone tails to create an open chromatin architecture, and acetylate nonhistone protein substrates including transcription factors themselves[7][15][40].

The protein architecture of p300 encompasses several functionally significant domains: an N-terminal KIX domain mediating interactions with CREB and other transcription factors, a RING finger domain with E3 ubiquitin ligase activity, plant homeodomain (PHD) fingers involved in histone recognition, a bromodomain that specifically recognizes acetylated lysine residues, a TAZ2 domain mediating protein-protein interactions, and the catalytic HAT domain[15][37][40]. Notably, an autoinhibitory loop within the HAT domain (amino acids 1532-1564 in human p300) regulates enzymatic activity through transautoacetylation, a mechanism whereby p300 molecules cooperate to relieve inhibition[15].

**Substrate Specificity and Catalytic Mechanism**

The HAT domain of p300 acetylates lysine residues on all four core histones (H2A, H2B, H3, and H4) as well as numerous nonhistone substrates including transcription factors such as p65/RelA, NFATc1, and STAT proteins[40][37]. Structural studies reveal that the catalytic mechanism proceeds through a Theorell-Chance or "hit-and-run" pathway in which acetyl-CoA substrate binding is followed by lysine substrate binding and acetyl transfer, without formation of a long-lived ternary complex[40]. Two critical glutamic acid residues (E1505 and potentially D1628) participate in a h-bond network anchoring peptide substrates, with further stabilization through recognition of positively charged residues at positions two to three amino acids upstream or downstream of the primary acetylation site[40].

**Multifunctionality and Context-Dependent Roles**

p300 and CBP, while closely related paralogs sharing high sequence homology, display distinct and sometimes opposing functional roles depending on biological context. In regulatory T cell (Treg) development, CBP and p300 cooperate with transcription factors including NFAT, Runx1, and CREB to promote Foxp3 expression and maintain Treg stability through acetylation of both histone and nonhistone substrates[7]. In oxidative stress conditions within synovial fibroblasts, p300 serves as the major regulator of stress response pathways, with predominant involvement in hypoxia response genes and proteasome-related genes, while CBP specifically mediates DNA damage response pathways[12]. In Alzheimer's disease neurons, p300 leads an epigenetic response to neurodegeneration[10].

The regulation of p300 itself demonstrates hierarchical control through multiple post-translational modifications: autoacetylation enhances HAT activity by exposing substrate-binding sites, phosphorylation by extracellular signal-regulated kinase 2 (ERK2) at the C-terminus augments HAT activity and promotes recruitment to specific promoters, phosphorylation by ataxia-telangiectasia mutated kinase links DNA damage response to p300 function, and phosphorylation by mTORC1 regulates autophagy and metabolic processes[15][31].

**p300 in Response to Lectin Signaling**

The specific connection between p300 and lectin signaling emerges through RAF1-dependent acetylation of NF-κB. When DC-SIGN is activated by pathogenic lectins, RAF1 activation leads to acetylation of the p65/RelA subunit of NF-κB at serine residue 276[6][36][39]. This acetylation event requires p300, as RAF1 does not directly acetylate p65—rather, RAF1 activation appears to stabilize or facilitate p300's access to p65, or to phosphorylate cofactors that enhance p300 recruitment. The resulting acetylated p65 exhibits enhanced transcriptional activity, driving expression of cytokine genes including IL-10, which shapes T helper cell polarization and the adaptive immune response to pathogens bearing lectins[6][36].

---

## GO Term Evaluation: "Response to Lectin" (GO:1990840)

### Term Definition and Scope

The Gene Ontology term GO:1990840 is formally defined as "any process that results in a change in state or activity of a cell or an organism" in response to lectins (endogenous or exogenous), specifically excluding events arising from lectin toxicity[3][5][26][29]. This represents a biological process-level annotation, reflecting dynamic cellular responses rather than static molecular functions or cellular compartments.

### Appropriateness of the Predicted Annotation

**Arguments Supporting Appropriateness**

The literature provides substantial evidence linking the molecular signatures in the rule to lectin-responsive processes:

1. **DC-SIGN signaling pathway**: DC-SIGN, a C-type lectin receptor, directly binds mannose residues on pathogenic organisms and triggers downstream signaling through RAF1[6][36][39]. This represents a cell's recognition of and response to lectin-bearing pathogens.

2. **RAF1-mediated transcriptional regulation**: RAF1 activation in response to DC-SIGN engagement leads to phosphorylation and acetylation of NF-κB, modulating expression of immune genes including IL-10[6][36][39]. This cascade represents a clear example of "response to lectin."

3. **Dectin-1 signaling**: An alternative C-type lectin receptor, dectin-1, triggers protective antifungal immunity through coordinated signaling via both SYK and RAF1 kinases, again demonstrating RAF1's central role in lectin-induced immune responses[6][36].

4. **p300 in immune regulation**: p300's role in acetylating key transcription factors including p65 places it downstream of RAF1 in the lectin response pathway, making it a component of the overall response mechanism[6][36].

**Potential Concerns Regarding Specificity**

Despite this biological support, several concerns emerge regarding the rule's specificity:

1. **Domain promiscuity**: The serine/threonine kinase domains specified (CATH.FunFam:1.10.510.10:FF:000011 and 3.30.200.20:FF:000069) are shared by hundreds of kinases serving diverse biological functions. RAF1 is one of three RAF family members (RAF1, BRAF, KRAF2), and other kinases containing these domains participate in growth factor signaling, stress responses, immune activation, and metabolic regulation—often without any connection to lectin signaling[18][21][42][50].

2. **p300 ubiquity**: p300 functions in hundreds of distinct biological processes including embryogenesis, cell cycle regulation, differentiation, apoptosis, and response to diverse environmental stimuli[7][10][12][15][19][22][40][49]. The two FunFam domains specified for p300 represent general acetyltransferase functions rather than lectin-specific roles.

3. **Requirement for cofactors**: The DC-SIGN-RAF1-p300 pathway functions as an integrated signaling cascade. Presence of RAF1 and p300 alone does not necessarily indicate lectin responsiveness; the specific upstream C-type lectin receptor (DC-SIGN, dectin-1, etc.) and appropriate downstream targets are equally essential[6][39].

### Comparison to Alternative GO Terms

The predicted term GO:1990840 (response to lectin) occupies a specific position within the Gene Ontology hierarchy. More general parent terms include "response to chemical" (GO:0042221) and "response to stimulus" (GO:0050896), while specific child terms include responses to particular lectin types. For proteins matching this rule, alternative annotations might be appropriate depending on additional evidence:

1. **"Response to chemical stimulus" (GO:0042221)**: More broadly applicable to signaling molecules generally.

2. **"Innate immune response" (GO:0045087)**: Particularly relevant since DC-SIGN-mediated lectin response participates in innate immunity.

3. **"Inflammatory response" (GO:0006954)**: Appropriate given the IL-10 and NF-κB activation downstream of DC-SIGN signaling.

4. **"Positive regulation of transcription by RNA polymerase II" (GO:0045944)**: Represents p300's direct molecular function rather than the cellular response context.

The appropriateness of GO:1990840 versus these alternatives depends on whether the annotation should capture the immediate molecular mechanism (p300's acetyltransferase activity) or the integrated cellular response context (DC-SIGN-mediated recognition of pathogenic lectins).

---

## Evidence Review: Literature Support and Limitations

### Primary Evidence Supporting the Rule

**RAF1 as Central Mediator of Lectin Signaling**

The most robust evidence supporting this rule comes from detailed mechanistic studies of dendritic cell signaling through C-type lectin receptors. When DC-SIGN on dendritic cells encounters mannose residues present on the surface of *Mycobacterium tuberculosis*, HIV-1, measles virus, and *Candida albicans*, the receptor trimerizes and initiates an intracellular cascade[6][9][36][39]. This cascade requires sequential activation of Ras proteins (through an unidentified guanine exchange factor), recruitment of RAF1 to the membrane through Ras-RBD interaction, and phosphorylation of RAF1 by both Src-family kinases and PAKs[39]. The resulting activated RAF1 then executes at least two distinct downstream signaling branches: one leading to ERK1/2 phosphorylation and one leading to direct p65 acetylation through p300 recruitment[6][36][39].

The experimental evidence for p300 involvement is particularly strong. RFC1-dependent acetylation of p65 at Ser276 increases the transcriptional activity of p65 itself[6][36]. Simultaneously, this phosphorylation inhibits the transcriptional activity of the NF-κB subunit RELB by sequestering it in p65-RELB heterodimers, which are transcriptionally inactive[6][36]. This demonstrates a sophisticated regulatory mechanism wherein lectin recognition through RAF1 leads to p300-mediated acetylation that reshapes NF-κB function.

**Dectin-1 Signaling as Complementary Evidence**

An alternative lectin receptor, dectin-1, triggers protective antifungal immunity through crosstalk between SYK and RAF1 kinases[6][36]. This pathway further emphasizes RAF1's central role in fungal pathogen recognition and demonstrates that lectin-induced immunity engages RAF1 signaling across multiple C-type lectin receptor families[6][36].

**CBP in Immune Response**

While the rule specifically mentions p300, the related protein CBP demonstrates parallel functions in immune regulation. CBP is essential for regulatory T cell development and function, where it cooperates with transcription factors to promote Foxp3 production[7]. The broader family of CBP/p300 proteins appears integral to immune response regulation across multiple contexts[7][15].

### Literature on Domain Functions Without Specific Lectin Connection

A substantial body of literature documents serine/threonine kinases and p300 in biological processes entirely unrelated to lectin signaling, creating a background of "noise" regarding false positives:

1. **General mitogenic signaling**: RAF1 participates in growth factor-induced ERK1/2 activation through binding to GTP-loaded Ras proteins activated by receptor tyrosine kinases[18]. This growth signaling occurs in all cell types and contexts.

2. **Cell cycle regulation**: p300 regulates cyclin genes and other cell cycle regulators as part of fundamental cell division machinery[7][15][40].

3. **Stress response**: p300 responds to oxidative stress, hypoxia, DNA damage, and ER stress through multiple mechanisms unrelated to lectin signaling[12][19][34].

4. **Developmental processes**: Both RAF1 and p300 participate in embryogenesis, tissue differentiation, and organ formation[7][15][40][49].

5. **Bacterial signaling**: Many bacteria encode their own serine/threonine kinases to evade or manipulate host immune responses, and host serine/threonine kinases participate in responses to bacterial PAMPs distinct from lectin-mediated pathways[45].

### Contradictory or Limiting Evidence

Several findings suggest the rule may generate false positives:

1. **Taxonomic overlap without functional specificity**: While the rule restricts annotation to primates and catarrhines, RAF1 and p300 function identically in these taxa and in other mammals. The restriction to primates/catarrhines appears to reflect a curated annotation bias rather than a biological difference in lectin responsiveness.

2. **Missing pathway components**: The rule specifies kinase domains and p300 but makes no requirement for upstream C-type lectin receptors (DC-SIGN, dectin-1, etc.). A protein could contain these domains without ever engaging with lectins if the relevant C-type lectin receptors are not co-expressed.

3. **Alternative p65 acetylators**: Multiple acetyltransferases besides p300, including CBP, p/CAF, Tip60, and SIRT1, can acetylate p65[31]. The presence of p300 does not guarantee its specific involvement in lectin-mediated p65 acetylation versus other acetylation events.

4. **Context-dependent RAF1 signaling**: RAF1 activation through growth factor pathways versus lectin pathways occurs through mechanistically distinct processes and leads to different downstream outcomes. Presence of RAF1 alone cannot distinguish between these contexts[39].

---

## Taxonomic Considerations

### Evolutionary Conservation of the Lectin Pathway

**Primate-Specific Immune Features**

The rule restricts the first condition set to primates (NCBITaxon:9443) and the second to catarrhines (Old World primates including humans, apes, and monkeys; NCBITaxon:9526). Recent research has demonstrated that apes mount markedly stronger early transcriptional responses to both bacterial and viral immune stimuli compared to African and Asian monkeys, with this difference attributable to lineage-specific evolution of pattern recognition receptor signaling[48][51]. Specifically, genes encoding C-type lectin receptors and related immune regulators show pronounced taxonomic variation among primates, suggesting that immune strategies—including lectin-mediated responses—have evolved differentially across primate lineages[27][51].

**Evidence for Conservation of Core Mechanism**

Despite these species differences, the core DC-SIGN-RAF1-p300 pathway appears fundamentally conserved across primates and even across mammals more broadly. RAF1, dectin-1, and p300 are present in all these organisms with high sequence conservation in their catalytic domains[18][50]. The three-tier MAPK cascade involving RAF, MEK, and ERK represents an evolutionarily ancient signaling system present even in early vertebrates like the Nile tilapia[50].

**Concerns Regarding Taxonomic Restriction**

The taxonomic restrictions in this rule create a paradox: if the DC-SIGN-RAF1-p300 pathway mediates lectin responses, then all mammals and even other vertebrates should be capable of this response, not just primates. The restriction to primates/catarrhines appears to reflect an attempt to increase rule specificity by limiting to taxa where this annotation may have been most thoroughly studied, rather than reflecting true biological differences. This restriction likely excludes valid lectin-responsive proteins in other primates, rodents, and other mammals.

---

## Rule Logic Assessment

### Evaluation of Domain Combination Logic

**Condition Set 1 Analysis**

The first condition requires concurrent presence of two serine/threonine kinase FunFams (1.10.510.10:FF:000011 and 3.30.200.20:FF:000069) in a primate organism. This combination appears problematic:

1. **Redundancy**: Both FunFam IDs likely represent generic serine/threonine kinase families. The requirement for BOTH domains in the same protein suggests either (a) multi-domain proteins with redundant kinase domains or (b) an overly specific restriction that excludes relevant single-domain kinases.

2. **Missing specificity**: RAF1 is a single-domain serine/threonine kinase that participates in lectin signaling. If this rule is intended to capture RAF1 function, requiring two kinase domains would exclude RAF1-containing proteins.

3. **High false positive risk**: Any protein containing two serine/threonine kinase domains, regardless of whether it participates in lectin signaling, would match this condition. Cell cycle checkpoints, stress response kinases, and developmental signaling proteins often contain multiple kinase domains for regulatory purposes.

**Condition Set 2 Analysis**

The second condition requires concurrent presence of two p300 FunFam domains (1.10.246.20:FF:000001 and 1.20.1020.10:FF:000001) in a catarrhine organism. This also presents issues:

1. **Potential redundancy or architecture specificity**: If these two FunFam IDs represent different domains within the same p300 protein, their co-occurrence is expected in all p300 orthologs. The requirement for both domains may simply be recapitulating the full-length p300 protein structure.

2. **Lack of pathway context**: The presence of p300 indicates transcriptional coactivation capacity but does not specify participation in lectin signaling. p300 participates in transcriptional regulation for hundreds of genes and biological processes.

3. **Taxonomic restriction without functional justification**: The restriction to catarrhines appears arbitrary. p300 function is conserved across primates and mammals. This restriction likely reflects annotation database biases rather than biological differences.

### Could False Positives Arise?

Yes, substantially. Consider specific scenarios:

1. **Protein kinases in mitotic checkpoints**: A protein with two serine/threonine kinase domains might participate entirely in cell cycle control with no involvement in lectin signaling. Examples could include kinases regulating spindle formation or kinetochore assembly.

2. **p300 in development**: p300 participates in numerous developmental processes through identical acetyltransferase mechanisms that drive lectin-pathway transcription. A developmental regulator containing p300 domains would match the condition but may never encounter or respond to lectins.

3. **Orphan kinases with unknown function**: Many primate kinases have not been functionally characterized. Presence of the specified domains does not guarantee their assignment to the correct biological context.

### Could False Negatives Arise?

Also yes. The rule might fail to identify true lectin-responsive proteins:

1. **Alternative kinase families**: Lectin signaling might proceed through serine/threonine kinases outside the specified FunFams. For example, PAKs (p21-activated kinases) and Src-family kinases both contribute to RAF1 phosphorylation in DC-SIGN signaling, but their domains may not match the specified signatures.

2. **Splice variants and truncated forms**: Primate genomes encode alternatively spliced variants of RAF1 and other kinases. Variants lacking one or both specified domains would be excluded despite potentially participating in lectin signaling.

3. **p300-independent lectin responses**: Some lectin-mediated responses might proceed through alternative acetyltransferases (CBP, Tip60) or entirely through histone deacetylase complexes in specific contexts.

---

## Recommendations for Rule Refinement

### Immediate Concerns Requiring Revision

1. **Reconceptualize domain requirement logic**: Rather than requiring two kinase domains, the rule should specify particular kinase families known to participate in lectin signaling (RAF1, PAK, Src-family kinases) or use a more targeted FunFam classification that reflects functional specificity rather than structural classification alone.

2. **Include upstream context**: Consider incorporating requirements for co-occurrence or proximity to C-type lectin receptor genes or their known cofactors. This would increase specificity by requiring the complete pathway context rather than just downstream effector domains.

3. **Expand taxonomic scope**: If lectin-responsive pathways are conserved across mammals (which the evidence suggests), expand the rule to include all mammalia or all vertebrata rather than restricting to primates/catarrhines. Alternatively, provide explicit biological justification for the taxonomic restriction.

4. **Distinguish between general coactivators and pathway-specific roles**: p300's universal involvement in transcriptional regulation necessitates additional context to distinguish its role in lectin signaling from its hundreds of other functions. Consider combining p300 requirements with:
   - Co-occurrence with genes encoding C-type lectin receptors
   - Expression in cell types known to mount lectin responses (dendritic cells, macrophages)
   - Association with NF-κB or interferon-responsive genes specifically

### Evidence Integration Recommendations

1. **Incorporate mechanistic pathway knowledge**: Modern annotation systems could leverage network data showing physical and functional interactions between DC-SIGN, RAF1, p300, p65, and other components of the canonical lectin signaling cascade[6][36][39].

2. **Utilize protein-protein interaction databases**: Require evidence of direct or indirect interaction with known lectin pathway components. A kinase that physically associates with dectin-1 or DC-SIGN would have higher confidence for lectin-pathway assignment than a kinase lacking such associations.

3. **Apply expression context filters**: Integrate tissue and cell-type expression data. A protein matching these domain criteria but expressed exclusively in testis or hair follicles (non-immune tissues) would have lower confidence for lectin-response annotation than the same protein expressed in dendritic cells or macrophages.

### Validation Recommendations

1. **Benchmark against known lectin-responsive proteins**: Apply the rule to known DC-SIGN, dectin-1, and other CLR pathway components and verify that true positives (RAF1, PAK1, p300) are captured while false positives are minimized.

2. **Literature mining for exceptions**: Systematically identify serine/threonine kinases or p300 orthologs in primates that do NOT participate in lectin signaling, and ensure the rule correctly excludes these.

3. **Phylogenetic analysis**: Construct phylogenetic trees of primate serine/threonine kinases and map known lectin-pathway participants. This would help identify whether lectin signaling capacity is truly restricted to specific kinase clades or if the current rule overgeneralizes.

---

## Conclusion

The annotation rule ARBA00089176 captures a genuine biological reality: the DC-SIGN-RAF1-p300 pathway represents a well-characterized mechanism by which primate cells recognize and respond to pathogenic lectins. This pathway is extensively documented in the literature, with clear evidence that RAF1 kinase activation by DC-SIGN engagement leads to p300-mediated acetylation of NF-κB and subsequent transcriptional responses[6][9][36][39].

However, the rule as currently structured demonstrates significant limitations that would substantially reduce its predictive accuracy:

1. The domain signatures specified are shared by hundreds of serine/threonine kinases and acetyltransferases serving diverse biological functions unrelated to lectin signaling.

2. The requirement for concurrent presence of two serine/threonine kinase domains appears arbitrary and may exclude functionally relevant RAF1 molecules while including multi-domain kinases unrelated to the pathway.

3. The taxonomic restriction to primates and catarrhines lacks clear biological justification and likely represents annotation database biases rather than true functional differences across mammals.

4. The rule lacks pathway context, requiring only the presence of molecular components without specification of upstream C-type lectin receptors or downstream NF-κB-regulated targets that would confirm genuine lectin-responsive context.

For robust deployment, this rule would benefit from integration of network pathway knowledge, expression context filters, more specific kinase family designations, and mechanistic validation demonstrating that rule-positive proteins actually participate in DC-SIGN, dectin-1, or other C-type lectin receptor signaling cascades. Without such refinements, the rule risks generating false positives at a high rate, potentially misannotating proteins with lectin-responsive functions when their true biological roles lie entirely outside immune and stress response contexts.

## Citations

1. https://www.cathdb.info/version/latest/funfam/1.10.510.10:FF:000011
2. http://www.cathdb.info/version/latest/superfamily/2.10.110.40/funfam/1
3. https://www.zhanggroup.org/UniBioMap/index.html?page=details.html%3Fid%3DGO%3A1990840%26unibiomap_id%3DUBMGO3302
4. https://www.cathdb.info/version/latest/funfam/1.20.1020.10:FF:000001
5. https://amigo.geneontology.org/amigo/term/GO:1990840
6. https://www.nature.com/articles/nri2569
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC4386456/
8. https://www.cathdb.info/version/v4_4_0/superfamily/3.30.200.20/funfam/24
9. https://pubmed.ncbi.nlm.nih.gov/18998127/
10. https://www.activemotif.com/blog-p300-alzheimers-disease-affected-neurons
11. http://cath.biochem.ucl.ac.uk/version/v4_2_0/domain/1u46A01
12. https://www.nature.com/articles/s41598-023-44412-z
13. https://en.wikipedia.org/wiki/Mannan-binding_lectin
14. https://www.uniprot.org/help/complete_go_annotation
15. https://pmc.ncbi.nlm.nih.gov/articles/PMC12547938/
16. https://pmc.ncbi.nlm.nih.gov/articles/PMC10855846/
17. https://www.uniprot.org/help/arba
18. https://en.wikipedia.org/wiki/C-Raf
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC7116894/
20. https://academic.oup.com/bioinformatics/article/37/8/1099/5949022
21. https://www.ncbi.nlm.nih.gov/gene/5894
22. https://pubmed.ncbi.nlm.nih.gov/19496744/
23. https://pmc.ncbi.nlm.nih.gov/articles/PMC3531114/
24. https://pmc.ncbi.nlm.nih.gov/articles/PMC3929681/
25. https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=338339
26. https://www.informatics.jax.org/vocab/gene_ontology/GO:1990840
27. https://www.nature.com/articles/s41435-025-00363-1
28. https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=64581
29. https://www.pnas.org/doi/10.1073/pnas.95.16.9214
30. https://academic.oup.com/nar/article/39/14/5907/1372130
31. https://www.science.org/doi/10.1126/sciadv.abf0984
32. https://pmc.ncbi.nlm.nih.gov/articles/PMC1411962/
33. https://pmc.ncbi.nlm.nih.gov/articles/PMC8830517/
34. https://www.nature.com/articles/s41467-023-39735-4
35. https://pmc.ncbi.nlm.nih.gov/articles/PMC9743508/
36. https://pmc.ncbi.nlm.nih.gov/articles/PMC11030075/
37. https://pmc.ncbi.nlm.nih.gov/articles/PMC4037238/
38. https://academic.oup.com/nar/article/51/D1/D523/6835362
39. https://pmc.ncbi.nlm.nih.gov/articles/PMC11496051/
40. https://www.cathdb.info/version/latest/funfam/1.20.1020.10:FF:000002
41. https://www.cd-genomics.com/blog/gene-ontology-go-analysis-comprehensive-guide/
42. https://www.science.org/doi/10.1126/scisignal.adt8686
43. https://pmc.ncbi.nlm.nih.gov/articles/PMC3706743/
44. https://pmc.ncbi.nlm.nih.gov/articles/PMC8020666/
45. https://academic.oup.com/nar/article/38/16/5396/1079970
46. https://pmc.ncbi.nlm.nih.gov/articles/PMC7062195/
47. https://www.nature.com/articles/s41467-022-35375-2
48. https://www.jstor.org/stable/24907965
49. https://pmc.ncbi.nlm.nih.gov/articles/PMC3584934/
50. https://www.ebi.ac.uk/QuickGO/term/GO:0009636
51. https://www.nature.com/articles/s41598-018-25020-8
52. https://www.informatics.jax.org/vocab/gene_ontology/GO:0042221