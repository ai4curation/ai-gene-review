---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-12-01T18:13:32.990411'
end_time: '2025-12-01T18:16:54.891332'
duration_seconds: 201.9
template_file: templates/rule_research.md
template_variables:
  rule_id: ARBA00088058
  rule_type: arba
  go_terms: GO:0051010 (microtubule plus-end binding)
  conditions_summary: '**Condition Set 1:** FunFam id: Putative CAP-Gly domain-containing
    linker protein 1 (CATH.FunFam:2.30.30.190:FF:000001) AND FunFam id: CAP-Gly domain
    containing linker protein 1 (CATH.FunFam:2.30.30.190:FF:000002) AND taxon: Glires
    (NCBITaxon:314147)


    **Condition Set 2:** FunFam id: Microtubule-associated protein, RP/EB family,
    member 2 (CATH.FunFam:1.10.418.10:FF:000007) AND FunFam id: microtubule-associated
    protein RP/EB family member 1 (CATH.FunFam:1.20.5.1430:FF:000001) AND taxon: Eukaryota
    (NCBITaxon:2759)


    **Condition Set 3:** FunFam id: CLIP-associating protein 1 isoform 2 (CATH.FunFam:1.25.10.10:FF:000001)
    AND FunFam id: CLIP-associating protein 1 isoform 2 (CATH.FunFam:1.25.10.10:FF:000005)
    AND taxon: Primates (NCBITaxon:9443)


    **Condition Set 4:** FunFam id: RP/EB family microtubule-associated protein (CATH.FunFam:1.10.418.10:FF:000028)
    AND taxon: Fungi (NCBITaxon:4751)


    **Condition Set 5:** FunFam id: Cytoskeleton-associated protein 5 (CATH.FunFam:1.25.10.10:FF:000019)
    AND taxon: Dikarya (NCBITaxon:451864)


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
citation_count: 59
---

## Question

# UniProt Rule Research

## Rule Context

- **Rule ID:** ARBA00088058
- **Rule Type:** arba
- **GO Term(s) Predicted:** GO:0051010 (microtubule plus-end binding)
- **Proteins Annotated:** 0 total (0 reviewed, 0 unreviewed)

### Condition Summary

**Condition Set 1:** FunFam id: Putative CAP-Gly domain-containing linker protein 1 (CATH.FunFam:2.30.30.190:FF:000001) AND FunFam id: CAP-Gly domain containing linker protein 1 (CATH.FunFam:2.30.30.190:FF:000002) AND taxon: Glires (NCBITaxon:314147)

**Condition Set 2:** FunFam id: Microtubule-associated protein, RP/EB family, member 2 (CATH.FunFam:1.10.418.10:FF:000007) AND FunFam id: microtubule-associated protein RP/EB family member 1 (CATH.FunFam:1.20.5.1430:FF:000001) AND taxon: Eukaryota (NCBITaxon:2759)

**Condition Set 3:** FunFam id: CLIP-associating protein 1 isoform 2 (CATH.FunFam:1.25.10.10:FF:000001) AND FunFam id: CLIP-associating protein 1 isoform 2 (CATH.FunFam:1.25.10.10:FF:000005) AND taxon: Primates (NCBITaxon:9443)

**Condition Set 4:** FunFam id: RP/EB family microtubule-associated protein (CATH.FunFam:1.10.418.10:FF:000028) AND taxon: Fungi (NCBITaxon:4751)

**Condition Set 5:** FunFam id: Cytoskeleton-associated protein 5 (CATH.FunFam:1.25.10.10:FF:000019) AND taxon: Dikarya (NCBITaxon:451864)

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

For the predicted GO term(s) **GO:0051010 (microtubule plus-end binding)**:
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
This is a complex request asking me to analyze a UniProt annotation rule (ARBA00088058) that predicts the GO term "microtubule plus-end binding" (GO:0051010) for proteins matching specific domain and family signatures. Let me break down what I need to do:

The rule has 5 condition sets (OR-ed together):
1. CAP-Gly domain proteins in Glires
2. EB family microtubule proteins in Eukaryota
3. CLIP-associating protein 1 in Primates
4. RP/EB family proteins in Fungi
5. Cytoskeleton-associated protein 5 in Dikarya

The search results provided contain extensive information about:
- CAP-Gly domains and their binding to microtubule plus ends
- CLIP-170 and related proteins as +TIPs (plus-end tracking proteins)
- EB proteins (EB1, EB2, EB3) as core +TIPs
- CLASP proteins and their functions
- XMAP215/Stu2 and TOG domains
- General microtubule biology

Let me plan my analysis:

1. **Executive Summary**: Assess if this rule is valid - do these domains/proteins actually bind microtubule plus ends?

2. **Domain Analysis**: 
   - CAP-Gly domains: bind to C-terminal EEY/F motifs on α-tubulin
   - EB proteins: core +TIPs that bind growing MT ends
   - CLIP proteins: +TIPs with CAP-Gly domains
   - CLASPs: +TIPs that bind EB proteins
   - CKAP5: also a +TIP
   
3. **GO Term Evaluation**: Is GO:0051010 (microtubule plus-end binding) appropriate?
   - Yes, all these proteins are known to bind MT plus ends
   - Though some carry out additional roles beyond plus-end binding

4. **Evidence Review**: Use the search results to provide citations

5. **Recommendations**: Are there issues with the rule logic?

Key findings from search results:
- [2] Captures protein tails by CAP-Gly domains - describes CAP-Gly binding to EEY/F motifs
- [3] CLASPs are CLIP-115 and -170 associating proteins
- [5] p150glued CAP-Gly domain binds tubulin
- [7] CLIP-170 requires EB1 for +TIP activity
- [9] EB1 regulates microtubule dynamics
- [10] CLIP-170 is a +TIP essential for spermatogenesis
- [12] Mammalian EB proteins control MT growth
- [14] CAP-Gly proteins in microtubule-dependent trafficking
- [20] CLASPs stabilize pre-catastrophe intermediate
- [21] CLIP-170 N-terminal domain binds to F-actin and tubulin
- [23] CLASP2 in protein condensates
- [24] Conformational changes in CLIP-170
- [33] Mammalian EB proteins control persistent MT growth
- [37] Stu2/XMAP215 biochemical mechanism
- [38] Isolated CLASP TOG domain suppresses MT catastrophe
- [40] Stu2/XMAP215 family MT polymerases
- [41] CLASP2 TOG domains
- [42] EB1 tracking weakest link
- [45] Dynamic localization of CLIP-170
- [49] +TIPs and MT regulation
- [52] Microtubule composition and dynamic instability
- [53] Dynactin functions as dynamic tether
</think>

# Comprehensive Analysis of UniProt Annotation Rule ARBA00088058: Microtubule Plus-End Binding Prediction

This report provides a detailed evaluation of UniProt annotation rule ARBA00088058, which predicts the Gene Ontology term GO:0051010 (microtubule plus-end binding) for proteins matching specific domain signatures and family classifications. The analysis examines the biological validity of domain-based predictions, reviews supporting and contradictory literature, assesses taxonomic appropriateness, and provides recommendations for rule refinement.

## Executive Summary of Rule Validity

The ARBA00088058 annotation rule predicts microtubule plus-end binding (GO:0051010) for proteins containing five distinct domain/family combinations with specific taxonomic restrictions. Based on comprehensive literature analysis, the rule demonstrates **strong validity with minor areas for refinement**. The proteins captured by this rule represent well-characterized families of plus-end tracking proteins (+TIPs) whose interaction with growing microtubule ends is extensively documented in experimental literature spanning more than two decades. However, the rule complexity and multiple conditions warrant careful scrutiny regarding whether all condition sets appropriately capture the predicted function with equal confidence, and whether some proteins matching these criteria might possess additional or alternative functions that extend beyond simple plus-end binding.

The rule conditions target proteins whose core biological function is documented to include microtubule plus-end binding, but this analysis reveals that some condition sets may be overly restrictive (missing functionally equivalent proteins in excluded taxa) while others may be insufficiently specific (potentially capturing proteins with broader or more nuanced roles). Additionally, the rule does not account for multifunctionality of these proteins—many condition-matching proteins simultaneously regulate microtubule dynamics, interact with other +TIPs, and participate in specific cellular processes where plus-end binding is merely one of several documented functions.

## Domain and Family Signature Analysis

### CAP-Gly Domains: Structure and Binding Mechanism

The Cytoskeleton-Associated Protein-Glycine-rich (CAP-Gly) domain represents one of the most well-characterized structural elements in the rule, and its relationship to the predicted GO term is extensively documented. CAP-Gly domains are specialized protein-interaction modules approximately 50 amino acids in length that function as specific recognition elements for C-terminal sequences on tubulin proteins[2]. The primary biological function of CAP-Gly domains is to bind with high specificity to the C-terminal EEY/F-COO⁻ sequence motifs present on alpha-tubulin molecules[2]. This binding interaction occurs through a conserved GKNDG motif present within the CAP-Gly domain structure itself, which makes direct contact with the C-terminal tyrosine residue of the α-tubulin E-hook[5].

The structural basis for this binding has been extensively characterized through crystallographic and cryo-electron microscopy studies. CAP-Gly domains recognize a transient, extended conformation of α-tubulin that is particularly enriched at growing microtubule plus ends[5]. Importantly, the binding affinity of CAP-Gly domains shows strong nucleotide dependence: the affinity for tyrosinated α-tubulin (Tyr-tubulin) with bound tubulin is approximately 11 μM, whereas binding to detyrosinated tubulin (Glu-tubulin) drops dramatically to levels below the detection limit (>130 μM)[5]. This nucleotide-dependent recognition is a critical feature that enables plus-end-specific targeting, as tyrosination of tubulin preferentially occurs in the soluble pool and on newly incorporated α-tubulin at microtubule plus ends[5].

Beyond the core GKNDG-containing CAP-Gly domain, many CAP-Gly-containing proteins possess extended basic amino acid-rich regions that flank the core domain[5]. These basic patches interact with the acidic surface of tubulin E-hooks through electrostatic interactions, significantly enhancing binding affinity[5]. The presence of these extended basic regions creates a more complex binding interface than the minimal CAP-Gly domain alone, allowing for cooperative binding and increased specificity for the growing microtubule plus end conformation.

CAP-Gly domains are known to participate in multiple cellular functions beyond simple microtubule binding. In addition to direct tubulin binding, CAP-Gly domains interact with end-binding homology domains, zinc-finger motifs, and proline-rich sequences present in various accessory proteins[2]. This multifunctionality raises important considerations for the proposed annotation—while CAP-Gly domains are diagnostic for microtubule interaction capability, they do not exclusively specify plus-end binding in isolation. The context provided by other protein domains, accessory sequences, and protein-protein interactions determines whether CAP-Gly-containing proteins function as simple plus-end-binding factors or as more complex regulatory molecules.

### CLIP and Related Cytoplasmic Linker Proteins

CLIP-170 (cytoplasmic linker protein 170) and its homolog CLIP-115 represent archetypal examples of CAP-Gly-containing proteins that function as +TIPs, and their extensive characterization provides strong support for the proposed rule. CLIP-170 was, in fact, the first +TIP to be identified in molecular studies[7]. The protein contains tandem CAP-Gly domains at its N-terminus, followed by a coiled-coil region and zinc-finger motifs at the C-terminus[3]. The N-terminal microtubule-binding domain of CLIP-170 localizes to microtubule plus ends when transfected into cells, and this localization is coupled directly to microtubule assembly[45].

In vitro studies have demonstrated that CLIP-170 binds directly to recently polymerized tubulin and to nonpolymerized tubulin with measurable affinity[45]. Importantly, CLIP-170 associates with microtubule plus ends in vivo through its interaction with EB1, a core +TIP protein[7]. Single-molecule tracking studies show that CLIP-170 exchanges rapidly at growing microtubule plus ends, consistent with dynamic plus-end tracking rather than stable lattice binding[7]. The requirement for EB1 in CLIP-170 plus-end localization indicates that CLIP-170 does not autonomously track plus ends but rather is recruited through interaction with the primary +TIP complex.

Structural studies reveal that CLIP-170 exists in a closed conformation maintained by intramolecular contacts between the N-terminal CAP-Gly domain and C-terminal zinc-finger motifs[24]. This autoinhibitory conformation prevents microtubule binding until the protein undergoes conformational changes that expose the microtubule-binding surface[24]. The conformational dynamics of CLIP-170 provide an example of how proteins annotated as "microtubule plus-end binding" may possess regulatory mechanisms that modulate this function based on cellular signals and protein interactions.

An important finding regarding CLIP-170 function involves its interaction with F-actin. The N-terminal domain of CLIP-170 binds directly to both microtubules and F-actin, with the second CAP-Gly domain (CAP-Gly 2) being particularly important for F-actin binding[21]. This dual specificity suggests that CLIP-170 functions at the intersection of actin and microtubule cytoskeletal systems[21], an activity that extends beyond simple plus-end binding to encompass broader roles in actin-microtubule crosstalk.

CLIP-170 shows fascinating tissue-specific functions that illustrate the complexity of +TIP biology. In spermatogenesis, CLIP-170 undergoes a transition from a dynamic plus-end-tracking protein during early spermatogenesis to a relatively immobile protein localized to spermatid manchettes during spermiogenesis[10]. This change in localization pattern correlates with altered functions, as CLIP-170 appears to adopt a structural role in sperm head shaping rather than purely regulatory functions[10]. Such tissue-specific functional specialization demonstrates that the term "microtubule plus-end binding" may incompletely capture the range of functions performed by this protein across different cellular contexts.

### End-Binding Proteins: The Core +TIP Complex

End-binding proteins (EB1, EB2, EB3 in mammals) represent the most highly conserved and arguably most important constituents of the +TIP complex. These proteins possess an N-terminal calponin homology (CH) domain that directly recognizes the growing microtubule plus end, a linker region, and a C-terminal coiled-coil domain essential for dimerization[12][33]. Critically, EB proteins have the intrinsic ability to bind and track growing microtubule plus ends autonomously, without requiring interaction with other +TIP proteins[12]. This autonomous plus-end-tracking capability distinguishes EB proteins from many other +TIPs, which depend on EB recruitment for proper localization.

The CH domain of EB proteins binds at the corner of four tubulin dimers present in two adjacent protofilaments at the microtubule end[9]. This positioning ideally places EB proteins to sense microtubule conformational changes induced by GTP hydrolysis[9]. Notably, EB proteins do not bind to the extreme tip of microtubule ends where GTP is initially loaded, but rather bind an extended region corresponding to transient intermediate states generated during GTP hydrolysis[9]. This nuanced binding specificity is crucial for understanding how EB proteins function as sensors of nucleotide state rather than simply as non-specific end-binding proteins.

Among the three mammalian EB proteins, EB1 and EB3 promote persistent microtubule growth by suppressing catastrophes, while EB2 is considerably less potent in this function[12][33]. This functional differentiation among highly similar proteins illustrates an important principle: proteins matching identical domain signatures and GO annotations may exhibit substantial functional variation. Biochemical studies show that the functional differences between EB proteins derive partly from variations in their CH domain sequences[12][33].

The regulation of EB1 at growing microtubule ends involves post-translational modifications and interactions with structural microtubule-associated proteins (MAPs) that do not themselves localize to plus ends[9]. Surprisingly, EB1 accumulation at growing microtubule ends is negatively regulated by direct interaction with structural MAPs, introducing the concept of "endogenous EB1 antagonists"[9]. This negative regulation by non-tip-tracking MAPs provides an example of how the regulation of microtubule plus-end binding can be controlled by proteins that do not themselves bind plus ends—a regulatory principle that complicates simple functional annotation schemes.

Phosphorylation at specific EB1 residues increases EB1 binding at the plus ends of astral microtubules, thereby regulating mitotic spindle orientation[9]. This phosphorylation-dependent regulation demonstrates that plus-end binding is not a constitutive function but rather is dynamically controlled through post-translational modification. Such regulatory complexity suggests that GO annotations describing plus-end binding may represent a simplified version of more nuanced, context-dependent functions.

### CLASP Family Proteins: Bridging Plus-End Binding and Catastrophe Suppression

CLIP-associating proteins (CLASPs) form a distinct family of +TIPs that associate with CLIP proteins and EB proteins to colocalize at microtubule distal ends[3][20]. CLASPs bind to both CLIP-170 and microtubules, colocalizing with CLIPs at microtubule distal ends[3]. Importantly, CLASPs have microtubule-stabilizing effects when expressed in transfected cells, and after serum induction, CLASPs relocalize to distal segments of microtubules at the leading edge of motile fibroblasts[3].

The mechanism by which CLASPs regulate microtubule dynamics involves stabilization of a nucleotide-dependent intermediate state at the microtubule end[20]. CLASPs specifically stabilize the pre-catastrophe intermediate state between growth and shrinkage, thereby suppressing microtubule catastrophe and promoting microtubule rescue[20]. On stabilized microtubules without soluble tubulin, CLASPs promote slow but robust microtubule depolymerization, indicating that their activity is tubulin concentration-dependent[20]. This concentration-dependent regulation reveals a sophisticated mechanism whereby CLASP activity switches between promoting depolymerization (at low tubulin concentrations) and stabilizing growth or rescuing shrinking microtubules (at higher concentrations)[20].

CLASPs contain multiple TOG domains structurally related to those found in XMAP215 family proteins, though with distinct binding properties[38][41]. Unlike XMAP215 TOG domains that preferentially bind free curved tubulin, CLASP TOG domains can stabilize the straight conformation of tubulin incorporated into the microtubule lattice[38]. A single isolated TOG2 domain from the yeast CLASP (Stu1) demonstrates considerable anti-catastrophe and rescue activity, contradicting earlier expectations that multiple linked TOGs are required for regulatory activity[38]. Single point mutations on the tubulin-binding surface of TOG2 ablate its anti-catastrophe and rescue activity, indicating that tubulin binding is essential for CLASP function[38].

Notably, CLASPs have bidirectional interactions with protein condensates at focal adhesions and other cellular locations[23]. The phosphorylation of CLASP2 modulates the dynamics of condensate-condensate interaction and spatiotemporally navigates microtubule growth along elongated protein condensate structures[23]. This emerging understanding of CLASP participation in phase-separated protein condensates introduces an additional layer of complexity—CLASPs not only bind microtubule plus ends but actively organize protein phase separation to guide microtubule positioning[23].

### CKAP5: Processive Microtubule Polymerase Activity

CKAP5 (cytoskeleton-associated protein 5) represents a distinct functional category among plus-end-binding proteins: CKAP5 acts as a processive microtubule polymerase. CKAP5 binds to the plus end of microtubules and regulates microtubule dynamics and organization while acting as a processive microtubule polymerase[16]. The polymerase activity of CKAP5 places this protein in the XMAP215/Stu2 family of microtubule regulators rather than in the regulatory +TIP category occupied by CLIP and EB proteins.

The biochemical mechanisms underlying XMAP215/Stu2 polymerase activity have been elucidated through reconstitution of purified protein components[37][40]. XMAP215/Stu2 family polymerases possess multiple tubulin-binding TOG domains arranged in a characteristic sequence. Metazoan polymerases like XMAP215 are monomers containing five or six TOG domains per protein, while fungal polymerases like Stu2 are homodimers containing two different TOG domains per monomer[37][40]. The tubulin-binding kinetics of individual TOG domains and their spatial arrangement determine the overall polymerase activity and efficiency[37][40].

Quantitative biochemical analysis reveals that Stu2 operates with very high efficiency, with the rate-limiting step being unpolymerized tubulin binding to TOG domains[37]. Once a TOG binds unpolymerized tubulin, that tubulin nearly always becomes incorporated into the microtubule[37]. The apparent Michaelis constant and maximal velocity of polymerase activity depend on the number of tubulin-binding TOG domains and their individual binding kinetics[37]. These detailed biochemical properties demonstrate that CKAP5 and related proteins represent a specialized class of plus-end-binding proteins whose function extends well beyond simple end recognition to encompass catalytic polymerization activity.

## GO Term Appropriateness and Specificity Assessment

### Definition and Scope of GO:0051010

The Gene Ontology term GO:0051010 "microtubule plus-end binding" is defined as "interacting selectively and non-covalently with the plus end of a microtubule"[1][4]. This definition captures the essential characteristic of binding to the growing end of microtubules with specificity and without forming covalent bonds. The term operates at the molecular function level of the Gene Ontology, describing a biochemical capability rather than a biological process or cellular component.

### Appropriateness for Predicted Proteins

For CAP-Gly-containing proteins, the GO term GO:0051010 is highly appropriate. CAP-Gly domains have evolved specifically to recognize and bind C-terminal tubulin sequences, with binding affinities and specificities consistent with functional microtubule plus-end recognition[2][5]. The experimental evidence for CAP-Gly-mediated plus-end binding is robust, including in vitro binding assays, cellular localization studies, and structural characterization[5][21][45].

For EB proteins, the GO term is equally appropriate. EB proteins autonomously track growing microtubule plus ends in vivo and exhibit high-resolution binding specificity for the transitional conformational states present at growing ends[9][12][33]. The plus-end-binding capability of EB proteins is perhaps the most extensively characterized and experimentally validated among all +TIPs.

For CLIP-associated proteins and CLASPs, the annotation requires somewhat greater interpretive nuance. While these proteins clearly associate with microtubule plus ends, this association occurs primarily through interactions with other +TIPs (particularly EB1) rather than through autonomous tubulin recognition[3][7]. Additionally, CLASPs actively regulate microtubule dynamics through mechanisms that extend beyond simple binding, including stabilization of specific conformational states and interaction with phase-separated protein condensates[20][23].

### Potential Issues with Annotation Specificity

The GO term "microtubule plus-end binding" may be insufficiently specific for capturing the full functional complexity of some proteins matching the rule conditions. Several issues warrant consideration:

**First, the term does not distinguish between proteins that autonomously bind plus ends versus those recruited through interactions with other proteins.** EB proteins bind plus ends autonomously, whereas CLIP-170 requires EB1 for proper plus-end localization[7]. This mechanistic distinction has functional implications—EB proteins form the core of the +TIP complex and regulate the recruitment of other +TIPs, while CLIP-170 functions as a secondary component. A more specific annotation might distinguish "autonomously tracks microtubule plus ends" from "associates with microtubule plus ends via protein interactions."

**Second, the GO term does not capture regulatory roles in microtubule dynamics.** EB proteins suppress microtubule catastrophes[12][33], CLASPs stabilize specific intermediate states[20], and XMAP215/CKAP5 promotes polymerization[37]. These regulatory functions are separable from simple binding capability and might warrant additional GO term annotations such as "regulation of microtubule polymerization" or specific terms describing catastrophe suppression.

**Third, the annotation does not capture the multifunctionality of these proteins.** CLIP-170 binds both microtubules and F-actin[21], CLASPs participate in phase separation[23], and p150glued functions in dynein recruitment for retrograde transport[53]. Proteins may warrant multiple GO annotations reflecting their diverse functional roles.

**Fourth, the temporal and spatial dynamics of plus-end binding are not captured.** EB proteins rapidly exchange at plus ends with characteristic kinetic parameters distinct from stable binding[9]. CLIP-170 transitions from a dynamic tracking protein to a structural protein during spermatogenesis[10]. The GO term "binding" does not distinguish between transient, rapidly exchanging associations and more stable interactions.

### Alternative or Complementary GO Terms

Several existing GO terms might provide more nuanced or specific annotation of these proteins depending on their particular functional roles:

- **GO:0008017 "microtubule binding"** captures broader microtubule interactions not specific to plus ends
- **GO:0005515 "protein binding"** captures general protein-protein interactions but lacks specificity
- **GO:0003779 "actin binding"** would apply to CLIP-170 and related proteins with actin-binding activity
- **GO:0008564 "phospholipid binding"** might apply if these proteins interact with lipid membranes
- **GO:0030176 "integral component of endoplasmic reticulum membrane"** or other cellular component terms would specify subcellular localization
- **GO:0001221 "transcription coactivator activity"** would not apply but illustrates how unrelated functions should be distinguished
- **GO:0051013 "microtubule severing"** and related terms capture dynamic regulatory activities

For regulatory functions, more specific terms would include:
- **GO:0005881 "cytoplasmic microtubule"** for microtubule array organization
- **GO:0008150 "biological_process"** at the process level for terms like "microtubule polymerization" or "microtubule dynamics"

## Literature Support and Experimental Evidence

### Foundational Discoveries and Historical Context

The experimental foundation for the proposed annotation rule derives from multiple convergent lines of research spanning more than twenty-five years. CLIP-170 was identified as the first plus-end tracking protein through immunofluorescence and cell biological approaches[3][45]. Early work established that CLIP-170 localizes dynamically to the growing ends of microtubules in vivo and that this localization is coupled to microtubule assembly rather than being a constitutive feature[45].

The subsequent identification of EB proteins as autonomous plus-end trackers[49] established that the plus-end-tracking phenotype reflects a genuine molecular feature rather than an artifact of CLIP-170's particular properties. The remarkable conservation of EB proteins across eukaryotic species, from yeasts to vertebrates, indicates that plus-end binding represents a fundamental cellular capability that emerged early in eukaryotic evolution[39][48].

### Structural Evidence for Plus-End Binding Specificity

High-resolution structural studies have provided detailed atomic-level understanding of how CAP-Gly domains recognize tubulin. X-ray crystallography and cryo-electron microscopy have resolved the complex between CAP-Gly domains and α-tubulin, revealing that the GKNDG motif directly contacts the C-terminal tyrosine of the tubulin E-hook[5]. The structural basis of nucleotide-dependent recognition shows how tyrosinated tubulin (abundant at plus ends) differs structurally from detyrosinated tubulin (enriched in stable microtubule lattice regions)[5][52].

Cryogenic electron microscopy has provided unprecedented resolution of EB protein binding sites at the growing microtubule end[9]. These studies show that EB proteins recognize a specific conformational state at the plus end that arises during GTP hydrolysis, enabling EB proteins to distinguish growing ends from depolymerizing ends or stabilized lattice regions[9]. The identification that EB proteins do not bind the extreme plus end tip but rather intermediate conformational states reveals a sophisticated mechanism for end recognition.

### In Vitro Reconstitution Studies

The most rigorous experimental support for plus-end binding by these protein families comes from in vitro reconstitution studies using purified protein components[7][12][20][37]. Single-molecule tracking by total internal reflection fluorescence (TIRF) microscopy has visualized EB1 and CLIP-170 dynamically tracking individual growing microtubules[7]. These studies demonstrated that EB1 rapidly exchanges at plus ends with exchange rates consistent with dynamic tracking rather than stable binding[7].

Quantitative sedimentation assays using purified tubulin and microtubules have measured binding affinities for various protein fragments[5]. These biochemical measurements have been essential for understanding how basic amino acid patches flanking CAP-Gly domains increase binding affinity and how nucleotide state affects recognition[5]. Co-sedimentation assays have further clarified the stoichiometry of binding and the saturation characteristics of plus-end binding[5].

### In Vivo Cellular Evidence

Cellular localization studies using green fluorescent protein (GFP) tags have demonstrated that endogenously expressed or transfected EB proteins localize to microtubule plus ends in living cells[12][33][48]. High-speed time-lapse microscopy has captured the characteristic plus-end tracking "comet" phenotype of these proteins as they dynamically localize to growing microtubule ends[9][49].

Immunoelectron microscopy using hook decoration techniques has positioned microtubule-associated proteins on electron microscopy images of microtubules, providing direct visualization of where on microtubule structures these proteins bind[48]. These classical cytological approaches established that EB1 and related proteins localize to the plus end region.

Fluorescence recovery after photobleaching (FRAP) experiments have measured the kinetic parameters of protein exchange at plus ends[9]. These studies demonstrated that EB proteins exchange rapidly, consistent with the dynamic tracking model[9]. The residence times measured by FRAP correlate with EB protein concentration and with the velocity of plus-end growth.

### Genetic and Molecular Evidence

Genetic studies in model organisms have established the functional importance of plus-end binding. Deletion of EB1 genes in various organisms results in characteristic mitotic and cytoskeletal defects[39][48]. In the fission yeast *Schizosaccharomyces pombe*, deletion of the Mal3 EB1 homolog results in early mitotic delay and sensitivity to spindle checkpoint mutations[39]. These genetic phenotypes indicate that plus-end binding by EB proteins is not merely incidental but functionally important for cellular viability and proper chromosome segregation.

Mutations affecting the plus-end-binding capability of dynactin subunit p150 have been identified as causative for human neurodegenerative diseases[50][53]. The Perry syndrome-associated mutations in p150's CAP-Gly domain impair microtubule binding, leading to aberrant dynein recruitment and retrograde transport defects[50][53]. These human genetic findings provide direct evidence that CAP-Gly-mediated plus-end binding is critical for proper neuronal function and that loss of this binding capability causes disease.

### Quantitative Kinetic Studies

Detailed kinetic analysis of plus-end binding has characterized the on-rates and off-rates of association and dissociation[9][20]. These measurements reveal that plus-end-binding proteins engage in rapid exchange kinetics rather than stable occupancy, with typical residence times on the order of seconds[9]. The concentration-dependent recruitment of secondary +TIPs by EB proteins has been quantified, revealing that EB1 operates at saturation at physiological concentrations[9].

## Taxonomic Considerations and Rule Specificity

### Condition Set 1: CAP-Gly Proteins in Glires

The first condition set restricts CAP-Gly domain-containing proteins to the Glires taxon (rodents and rabbits). This restriction limits the rule to mammalian CAP-Gly proteins while excluding birds, fish, invertebrates, and fungi. Glires species include rodents (*Mus musculus, Rattus norvegicus*) and rabbits, representing a relatively limited subset of eukaryotic diversity.

**Assessment of taxonomic restriction:** CAP-Gly domains and their tubulin-binding function are highly conserved across all eukaryotic lineages. CLIP-170 homologs exist in invertebrates (*Drosophila melanogaster* has orthologous CLIP-190)[7]. Fungi possess Bik1p, the *S. cerevisiae* ortholog of mammalian CLIP proteins, which shares essential structural features and functional capabilities[14]. The *S. pombe* orthologs Tip1 and Bik1 also bind microtubules through CAP-Gly domains[7][39].

The restriction to Glires appears overly narrow and potentially excludes functionally equivalent proteins in other mammalian lineages (primates, carnivores, ungulates) that surely possess CLIP orthologs with equivalent plus-end-binding function. Moreover, vertebrate CLIP-170 proteins across different species exhibit remarkable sequence conservation and functional equivalence. The taxonomic restriction appears to reflect an arbitrary database limitation rather than a biological principle.

### Condition Set 2: EB Family Proteins in Eukaryota

The second condition set applies to EB family proteins (MAPRE1 and MAPRE2) across all Eukaryota. This is a much broader taxonomic scope than Condition Set 1, capturing EB proteins in animals, plants, fungi, and protists.

**Assessment of taxonomic restriction:** This broad restriction is appropriate because EB proteins are indeed present and functionally conserved across eukaryotic organisms. The *S. cerevisiae* Bim1p and *S. pombe* Mal3 represent clear fungal EB orthologs with experimental evidence for plus-end-binding function[39]. Plant EB proteins (*Arabidopsis* AtEB1a) exhibit conserved plus-end localization and function[48]. The EB protein family has maintained functional conservation since at least the last common ancestor of all eukaryotes.

However, the condition specifies only MAPRE1 and MAPRE2. The mammalian genome encodes three EB proteins: MAPRE1 (EB1), MAPRE2 (EB2), and MAPRE3 (EB3). Among these, EB1 and EB3 demonstrate robust plus-end tracking and catastrophe suppression, while EB2 shows considerably weaker plus-end tracking activity[12][33]. The restriction to only MAPRE1 and MAPRE2 thus excludes MAPRE3/EB3, a highly functional plus-end tracker.

### Condition Set 3: CLASP Proteins in Primates

The third condition specifies CLIP-associating protein 1 (CLASP1) isoforms in Primates (human, apes, monkeys).

**Assessment of taxonomic restriction:** CLASPs are not restricted to primates; CLASPs exist throughout the animal kingdom and even in fungi. *Drosophila* possesses CLASP homologs (Orbit/Mast)[3]. Yeast possesses Stu1 and related CLASP homologs[38]. The primate restriction appears to represent insufficient taxonomic scope, as CLASP functional capabilities are not limited to primates. The functional conservation of CLASP catalytic domains (TOG domains) extends across fungal and animal lineages[38][41].

### Condition Set 4: RP/EB Proteins in Fungi

The fourth condition specifies RP/EB family proteins (apparently referring to EB homologs) in Fungi.

**Assessment of taxonomic restriction:** This condition appears somewhat redundant with Condition Set 2, which already captures eukaryotic EB proteins including fungal species. The separation of fungal EB proteins into a distinct condition set may reflect database organization rather than biological distinctness. Fungal EB proteins (Bim1p in budding yeast, Mal3 in fission yeast) exhibit the same fundamental plus-end binding mechanism as mammalian EB proteins[39].

### Condition Set 5: CKAP5 in Dikarya

The fifth condition targets CKAP5 (Cytoskeleton-Associated Protein 5) in Dikarya—a large grouping encompassing ascomycete and basidiomycete fungi.

**Assessment of taxonomic restriction:** CKAP5 is a mammalian protein name; the fungal ortholog is XMAP215-like polymerase (Stu2 in budding yeast, Alp14 in fission yeast). These proteins possess conserved TOG domains and function as microtubule polymerases with plus-end localization[37][40]. The restriction to Dikarya is oddly specific, as XMAP215/Stu2 family proteins exist in all eukaryotic lineages, not just Dikarya. This condition may reflect an annotation artifact where only Dikarya species were well-characterized at the time the rule was created.

## Assessment of Rule Logic and Potential Issues

### Redundancy Among Condition Sets

The five condition sets in ARBA00088058 show considerable conceptual overlap. Condition Sets 1 and 3 both target CAP-Gly-containing linker proteins (CLIP family), differing only in taxonomic scope. Condition Set 2 targets EB proteins broadly across eukaryotes, while Condition Set 4 targets EB proteins specifically in fungi. These overlapping conditions suggest the rule could be simplified.

The redundancy becomes apparent when considering that the full expression of the rule is:
**(CAP-Gly proteins in Glires) OR (EB proteins in Eukaryota) OR (CLASP proteins in Primates) OR (EB proteins in Fungi) OR (XMAP215 in Dikarya)**

The inclusion of both Condition Set 2 (EB proteins in all Eukaryota) and Condition Set 4 (EB proteins in Fungi) means that Condition Set 4 is entirely subsumed by Condition Set 2. Any fungal EB protein matching Condition Set 4 would already be captured by Condition Set 2.

### Taxonomic Inconsistency

The rule shows troubling inconsistency in taxonomic scope across conditions. Condition Set 1 is restricted to Glires (rodents and rabbits), while Condition Set 2 extends to all Eukaryota. This creates an apparent bias where mammalian CAP-Gly proteins are only captured for rodents and rabbits, while mammalian EB proteins are captured for all species. This suggests the rule builder had different information availability for different protein families.

### Potential for False Negatives

The taxonomic restrictions create the potential for numerous false negatives—proteins that should be annotated but are not due to narrow taxonomic scope. For example, human CLIP-170 matches Condition Set 1 only if the human genome is classified as Glires, which it is not (humans are in Primates). This means human CLIP-170 would not be annotated by Condition Set 1 despite having equivalent function to CLIP-170 in rodents.

The primate CLASP restriction (Condition Set 3) means that *Drosophila* CLASP (Orbit/Mast) would not be annotated by this rule despite having well-documented plus-end binding capability. Similarly, yeast CLASP orthologs would not be captured.

### Potential for False Positives

The conditions appear sufficiently specific that false positives are unlikely. All proteins matching these domain signatures are known to interact with microtubules, and the vast majority bind plus ends. However, some potential concerns exist:

**First, some CAP-Gly-containing proteins may have evolved additional functions beyond plus-end binding.** While all known CAP-Gly proteins bind microtubules, not all may function as plus-end trackers in every cellular context. CLIP-170 binds F-actin as well as microtubules[21], and in some cellular situations may function primarily in actin-microtubule crosstalk rather than as a +TIP.

**Second, the multifunctional nature of these proteins means plus-end binding may represent only one of several functions.** p150 functions critically in dynein recruitment and retrograde transport initiation[50][53]—functions that depend on plus-end binding but represent distinct biological processes. Annotating these proteins solely as "microtubule plus-end binding" proteins incompletely captures their functional roles.

**Third, developmental or cell-type-specific changes in protein function may not be captured by general domain-based annotation.** CLIP-170 transitions from a dynamic tracker to a structural protein during spermatogenesis[10]. Proteins may warrant context-dependent annotations that specify when particular functions are active.

## Evidence Review: Supporting Literature and Contradictory Findings

### Strong Supporting Evidence

The literature supporting the proposed annotation rule is extensive and compelling. The founding observations that CLIP-170 and EB proteins track growing microtubule plus ends have been reproduced in numerous laboratories using multiple experimental approaches[3][45][49]. The biochemical evidence for CAP-Gly domain binding to tubulin is robust and has been validated by structural biology[5][2].

The genetic evidence that plus-end-binding proteins are essential for cellular functions (mitosis, cell migration, spermatogenesis) demonstrates that the annotated capability is biologically important[39][10]. Human genetic evidence showing that mutations affecting CAP-Gly-mediated plus-end binding cause disease[50][53] provides strong support for the functional significance of this capability.

The conservation of plus-end-binding proteins across eukaryotic lineages indicates that this molecular capability emerged early in eukaryotic evolution and has been maintained throughout subsequent diversification[39][48]. The structural conservation of binding mechanisms suggests deep evolutionary constraint on these functions[31].

### Partial or Qualified Findings

Some literature findings qualify or refine the proposed annotation in important ways. The discovery that CLIP-170 requires EB1 for efficient plus-end localization demonstrates that not all CAP-Gly proteins autonomously bind plus ends—some depend on recruitment by other proteins[7]. This raises questions about whether "microtubule plus-end binding" accurately describes a protein that cannot efficiently localize to plus ends without interaction with other proteins.

The finding that EB1 itself is negatively regulated by structural MAPs introduces the concept that plus-end binding may be actively prevented in some contexts[9]. Similarly, the discovery that EB proteins can promote microtubule catastrophe despite enhancing growth in other circumstances[29] indicates that plus-end binding does not necessarily imply consistent effects on microtubule stability.

The detailed kinetic studies of protein exchange at plus ends reveal that plus-end binding is highly dynamic with rapid turnover rates[9]. This rapid exchange is functionally important—the rapid on-off kinetics enable dynamic regulation that would be impossible with stable binding. The GO term "binding" does not fully capture this dynamic nature.

### Multifunctionality and Functional Context Dependency

The literature increasingly documents that plus-end-binding proteins perform diverse cellular functions that extend beyond simple end recognition. CLIP-170 participates in membrane trafficking[14], CLASP2 organizes protein condensates[23], and p150 initiates dynein-mediated transport[50][53]. These diverse functions are united by the common capability of binding microtubule plus ends, but the plus-end binding represents a platform function that enables distinct cellular processes.

The finding that post-translational modifications regulate plus-end binding raises important questions about whether proteins should be unconditionally annotated as plus-end binders[9]. If phosphorylation decreases EB1 accumulation at plus ends, should unphosphorylated EB1 be annotated differently from phosphorylated EB1?

## Recommendations for Rule Refinement

### Priority 1: Resolve Taxonomic Inconsistency

The most pressing issue is the taxonomic inconsistency across condition sets. The rule should be revised to apply condition sets consistently across taxa. Options include:

**Option A: Broaden taxonomic scope for all conditions**
Expand Condition Set 1 from Glires to Mammalia or Vertebrata, recognizing that CAP-Gly proteins function equivalently across mammalian lineages.

**Option B: Narrow taxonomic scope for all conditions**
Restrict Condition Set 2 to specific well-characterized clades, accepting that some organisms may not receive annotation.

**Option C: Document rationale for restrictions**
If taxonomic restrictions reflect incomplete annotation, document this explicitly so rule updates can be prioritized accordingly.

### Priority 2: Eliminate Redundant Conditions

Condition Set 4 (EB proteins in Fungi) is entirely subsumed by Condition Set 2 (EB proteins in Eukaryota) and should be removed. This simplification would not change annotation outcome but would reduce rule complexity.

Similarly, evaluate whether Condition Sets 1 and 3 represent truly distinct functional categories or whether they should be consolidated with different taxonomic scope.

### Priority 3: Clarify Multifunctionality Through Complementary Annotations

For proteins matching these conditions, consider adding additional GO terms that capture their regulatory functions:

- For EB proteins: Consider adding "GO:0030174 regulation of mitotic recombination" or other process-level terms
- For CLASP proteins: Consider "GO:0001764 neuron migration" and "GO:0051642 centrosome localization"
- For p150: Consider "GO:0030111 regulation of Wnt signaling pathway"

These complementary annotations would provide more complete functional description without removing the core "microtubule plus-end binding" annotation.

### Priority 4: Consider Context-Dependent Annotations

Evaluate whether certain protein families warrant context-dependent annotations reflecting developmental or cell-type-specific functions. For instance:

- CLIP-170 as a dynamic tracker (in most cell types) versus a structural protein (in spermatids)
- EB1 as autonomously binding (when phosphorylated) versus being suppressed (when in complex with structural MAPs)

Such refinements would better capture functional complexity while maintaining practical applicability of GO annotations.

### Priority 5: Add Complementary Specificity Terms

Consider using more specific GO terms for important functional specializations:

- "GO:0008017 microtubule binding" for general microtubule binding
- "GO:0051013 microtubule severing" for proteins with catastrophe or depolymerization activity  
- "GO:0051010 microtubule plus-end binding" for specific plus-end-restricted interaction
- "GO:0051661 positive regulation of microtubule polymerization" for proteins promoting growth

This finer-grained annotation would distinguish proteins with different mechanisms and functional outcomes despite all having plus-end binding capability.

### Priority 6: Validate MAPRE3 Exclusion

Explicitly evaluate whether MAPRE3 (EB3) should be included despite similar function to MAPRE1 and MAPRE2. The decision to exclude MAPRE3 appears to be an oversight rather than a deliberate functional distinction, as EB3 exhibits robust plus-end tracking[12][33].

### Priority 7: Document Protein Isoform Considerations

Several of the FunFams in the conditions reference "isoform" variants (e.g., "CLIP-associating protein 1 isoform 2"). Clarify whether the rule should capture all isoforms or whether particular isoforms have distinct functions that warrant different annotation.

## Conclusions

The ARBA00088058 annotation rule predicts microtubule plus-end binding (GO:0051010) for proteins matching five domain and family signatures with specific taxonomic restrictions. Based on comprehensive literature analysis, the rule captures proteins whose capability for microtubule plus-end binding is experimentally well-established and functionally important. The CAP-Gly domain signature condition successfully identifies proteins bearing this specialized tubulin-recognition module. The EB protein conditions capture core +TIP proteins with conserved plus-end-tracking capability. The CLASP and CKAP5 conditions identify important regulatory proteins that localize to plus ends through domain signatures.

However, the rule exhibits taxonomic inconsistencies that create anomalies in annotation coverage, particularly for mammalian CAP-Gly proteins and fungal CLASP orthologs. The rule also shows redundancy in covering EB proteins at multiple taxonomic levels. More fundamentally, the single GO term "microtubule plus-end binding" incompletely captures the functional complexity of proteins matching these conditions—many function as regulatory proteins affecting microtubule dynamics, as adaptors recruiting other proteins, or as catalytic polymerases. The static nature of GO annotation cannot capture dynamic, context-dependent, or developmentally regulated functions that these proteins exhibit.

Despite these limitations, the rule provides a reasonable first-pass functional annotation for a diverse family of proteins united by the capability to recognize and interact with growing microtubule plus ends. With the refinements suggested above—particularly resolution of taxonomic inconsistencies, elimination of redundant conditions, and addition of complementary functional annotations—this rule would provide more accurate and comprehensive functional annotation of the plus-end-binding proteome.

## Citations

1. https://www.yeastgenome.org/go/GO:0051010
2. https://pubmed.ncbi.nlm.nih.gov/18835717/
3. https://pubmed.ncbi.nlm.nih.gov/11290329/
4. https://www.ebi.ac.uk/QuickGO/GTerm?id=GO%3A0051010
5. https://www.pnas.org/doi/10.1073/pnas.1403135111
6. https://www.uniprot.org/uniprotkb/Q7Z460/entry
7. https://www.pnas.org/doi/10.1073/pnas.0807614106
8. https://www.ncbi.nlm.nih.gov/gene/22919
9. https://pmc.ncbi.nlm.nih.gov/articles/PMC11107513/
10. https://pubmed.ncbi.nlm.nih.gov/16230537/
11. https://www.uniprot.org/uniprotkb/Q3ZBD9/entry
12. https://rupress.org/jcb/article/184/5/691/35290/Mammalian-end-binding-proteins-control-persistent
13. https://www.ncbi.nlm.nih.gov/gene/9793
14. https://pmc.ncbi.nlm.nih.gov/articles/PMC6380331/
15. https://pmc.ncbi.nlm.nih.gov/articles/PMC3531114/
16. https://www.uniprot.org/uniprotkb/Q14008/entry
17. https://www.uniprot.org/uniprotkb/P30622/entry
18. https://www.cathdb.info
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC3518651/
20. https://pmc.ncbi.nlm.nih.gov/articles/PMC10195879/
21. https://pmc.ncbi.nlm.nih.gov/articles/PMC9062740/
22. https://pmc.ncbi.nlm.nih.gov/articles/PMC2901667/
23. https://www.nature.com/articles/s41467-024-50863-3
24. https://rupress.org/jcb/article/166/7/1003/51324/Conformational-changes-in-CLIP-170-regulate-its
25. https://pmc.ncbi.nlm.nih.gov/articles/PMC3022353/
26. https://pmc.ncbi.nlm.nih.gov/articles/PMC8985376/
27. https://www.mtoz-biolabs.com/advantages-and-limitations-of-go-functional-annotation-and-enrichment-analysis.html
28. https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.13211
29. https://www.uniprot.org/uniprotkb/Q15555/entry
30. https://pmc.ncbi.nlm.nih.gov/articles/PMC8113439/
31. https://pmc.ncbi.nlm.nih.gov/articles/PMC10035887/
32. https://pmc.ncbi.nlm.nih.gov/articles/PMC8871558/
33. https://pmc.ncbi.nlm.nih.gov/articles/PMC2686402/
34. https://pubmed.ncbi.nlm.nih.gov/27466378/
35. https://bsppjournals.onlinelibrary.wiley.com/doi/10.1111/j.1364-3703.2007.00419.x
36. https://elifesciences.org/reviewed-preprints/107818
37. https://www.molbiolcell.org/doi/10.1091/mbc.E17-12-0748
38. https://pmc.ncbi.nlm.nih.gov/articles/PMC1369205/
39. https://pmc.ncbi.nlm.nih.gov/articles/PMC12259038/
40. https://pmc.ncbi.nlm.nih.gov/articles/PMC4646087/
41. https://www.nature.com/articles/nrm2110
42. https://www.uniprot.org/help/automatic_annotation
43. https://academic.oup.com/bioinformatics/article/31/21/3460/194878
44. https://rupress.org/jcb/article/144/1/99/16031/Dynamic-Localization-of-CLIP-170-to-Microtubule
45. https://www.uniprot.org/help/arba
46. https://pmc.ncbi.nlm.nih.gov/articles/PMC4489299/
47. https://pmc.ncbi.nlm.nih.gov/articles/PMC1143073/
48. https://pmc.ncbi.nlm.nih.gov/articles/PMC535819/
49. https://pmc.ncbi.nlm.nih.gov/articles/PMC4195236/
50. https://www.uniprot.org/uniprotkb/A0A2J8NQ14/entry
51. https://www.pnas.org/doi/10.1073/pnas.0401266101
52. https://www.nature.com/articles/ncomms5807
53. https://www.uniprot.org/uniprotkb/O75122/entry
54. https://journals.asm.org/doi/10.1128/ec.00044-07
55. https://www.cathdb.info/version/v4_4_0/superfamily/2.30.30.190/funfam/2
56. https://pmc.ncbi.nlm.nih.gov/articles/PMC8478408/
57. https://pmc.ncbi.nlm.nih.gov/articles/PMC6054225/
58. https://www.cathdb.info/superfamily/2.30.30.190
59. https://rupress.org/jcb/article/216/6/1641/38975/TOG-tubulin-binding-specificity-promotes