---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-23T19:56:06.577880'
end_time: '2026-01-23T20:08:56.447160'
duration_seconds: 769.87
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: RASAL3
  gene_symbol: RASAL3
  uniprot_accession: Q86YV0
  protein_description: 'RecName: Full=RAS protein activator like-3;'
  gene_info: Name=RASAL3;
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: C2_dom. (IPR000008); C2_domain_sf. (IPR035892); Ras_GTPase. (IPR039360);
    RasGAP_CS. (IPR023152); RasGAP_dom. (IPR001936)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 10
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q86YV0
- **Protein Description:** RecName: Full=RAS protein activator like-3;
- **Gene Information:** Name=RASAL3;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** C2_dom. (IPR000008); C2_domain_sf. (IPR035892); Ras_GTPase. (IPR039360); RasGAP_CS. (IPR023152); RasGAP_dom. (IPR001936)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "RASAL3" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'RASAL3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **RASAL3** (gene ID: RASAL3, UniProt: Q86YV0) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# RASAL3 (RAS Protein Activator Like-3): A Comprehensive Review

**Gene:** RASAL3
**UniProt:** Q86YV0
**Organism:** Homo sapiens (Human)
**Aliases:** FLJ21438, RASL3

## 1. Introduction

RASAL3 (RAS protein activator like-3) is a Ras GTPase-activating protein (RasGAP) that functions as a negative regulator of Ras signaling pathways. Encoded by the RASAL3 gene located on human chromosome 19, this approximately 114.7 kDa cytosolic protein belongs to the SynGAP family of RasGAPs and plays essential roles in hematopoietic cell biology [simanshu-2017-rasgaps-review-abstract]. Unlike many other RasGAPs that exhibit broad tissue distribution, RASAL3 is distinguished by its predominant expression in cells of hematopoietic origin, including T cells, B cells, natural killer T (NKT) cells, and neutrophils [saito-2015-nkt-cells-abstract][ishihara-2015-tcell-survival-abstract].

The primary biochemical function of RASAL3 is to accelerate the intrinsic GTPase activity of Ras proteins, converting them from the active GTP-bound state to the inactive GDP-bound state [simanshu-2017-rasgaps-review-abstract]. This activity places RASAL3 as a key negative regulator of the Ras/ERK signaling pathway, which controls cell proliferation, survival, and differentiation. Research over the past decade has revealed that RASAL3 performs non-redundant functions in multiple immune cell types, regulating T cell survival, NKT cell expansion, neutrophil inflammatory responses, and dendritic cell migration [ishihara-2015-tcell-survival-abstract][saito-2015-nkt-cells-abstract][saito-2021-neutrophils-abstract][olivier-2024-ccdc88b-abstract].

## 2. Protein Structure and Domain Architecture

RASAL3 is a member of the SynGAP family of RasGAPs, which also includes SynGAP1, DAB2IP, and RASAL2 [simanshu-2017-rasgaps-review-abstract]. Members of this family are characterized by an approximate molecular weight of 140 kDa and a distinctive domain arrangement featuring a canonical RasGAP module preceded by regulatory domains. The domain architecture of RASAL3 consists of three major functional regions arranged from the N-terminus to C-terminus: a pleckstrin homology (PH) domain, a C2 domain, and a RasGAP catalytic domain [simanshu-2017-rasgaps-review-abstract][ishihara-2015-tcell-survival-abstract].

The pleckstrin homology (PH) domain mediates interactions with phosphatidylinositol lipids in the cell membrane, facilitating membrane recruitment of the protein [ishihara-2015-tcell-survival-abstract]. The C2 domain, approximately 130 residues in length, folds into an eight-stranded antiparallel β-sandwich structure with three calcium-binding loops (CBL1, CBL2, and CBL3) [simanshu-2017-rasgaps-review-abstract]. Recent structural and functional studies on related RasGAP proteins have demonstrated that the C2 domain is not merely a membrane-targeting module but actively participates in augmenting catalytic activity. Research published in 2025 showed that the C2 domain of RasGAP family members directly contacts the allosteric lobe of Ras proteins, with conserved residues such as R707 being essential for full catalytic efficiency [simanshu-2017-rasgaps-review-abstract].

The RasGAP catalytic domain is the defining feature of all RasGAP family members and employs a conserved catalytic mechanism. This domain contains the catalytic arginine residue (the "arginine finger") that inserts into the active site of Ras proteins to stabilize the transition state of GTP hydrolysis [simanshu-2017-rasgaps-review-abstract]. In the p120GAP prototype, this corresponds to Arg789. Through this transition-state stabilization mechanism, RasGAP proteins can accelerate the intrinsic GTPase rate of Ras by several orders of magnitude [simanshu-2017-rasgaps-review-abstract].

A notable structural distinction of SynGAP family members, including RASAL3, from other RasGAPs such as p120GAP/RASA1 is that the PH-C2-RasGAP triple module is located at the amino-terminus rather than the carboxy-terminus of the protein [simanshu-2017-rasgaps-review-abstract]. This arrangement may have functional implications for regulation of GAP activity.

RASAL3 shows stringent evolutionary conservation, with orthologs identified in mouse (Rasal3, Chromosome 17), rat, and zebrafish [mgi-rasal3-ortholog-summary]. The high degree of conservation across vertebrate species, particularly in the catalytic RasGAP domain, underscores the essential nature of RASAL3 function in hematopoietic cell biology. The mouse ortholog has been extensively used for functional studies, and phenotypes observed in Rasal3-deficient mice have provided critical insights into RASAL3 function that are likely translatable to human biology given the typical conservation of immune system components between these species.

## 3. Biochemical Function and Substrate Specificity

The primary biochemical function of RASAL3 is to act as a GTPase-activating protein for Ras family small GTPases. Experimental evidence has directly demonstrated that RASAL3 possesses RasGAP activity and can stimulate p21Ras GTPase activity [ishihara-2015-tcell-survival-abstract][tomida-2018-rac2-abstract]. Importantly, early characterization studies established that RASAL3 exhibits RasGAP activity but lacks Rap1GAP activity, distinguishing it from dual-specificity GAPs such as RASA3 (GAP1IP4BP) that can act on both Ras and Rap1 [ishihara-2015-tcell-survival-abstract].

The specificity of RASAL3 for Ras over Rap1 was demonstrated through experiments showing that while RASAL3 overexpression repressed TCR-stimulated ERK phosphorylation in T cell lines (indicating Ras inactivation), it did not affect TCR-dependent accumulation of GTP-bound Rap1 [ishihara-2015-tcell-survival-abstract]. The molecular basis for this specificity may relate to specific amino acid residues in the RasGAP domain. Although RASAL3 harbors a proline residue at position 641 (corresponding to Pro489 in RASA3, which is important for Rap1GAP activity), functional studies confirmed that RASAL3 does not possess Rap1GAP activity [ishihara-2015-tcell-survival-abstract].

Intriguingly, biochemical studies have revealed that RASAL3 possesses a second, unexpected substrate specificity. Tomida and colleagues demonstrated that the catalytic domain of RASAL3 can interact with and stimulate the GTPase activity of Rac2, a Rho family small GTPase [tomida-2018-rac2-abstract]. Their in vitro assays showed more than 3.5-fold enhancement of GTP hydrolysis when RASAL3-GAP was co-incubated with Rac2, while RASAL3 induced minimal changes in the activity of other Rho family GTPases including Rac1, RhoA, and Cdc42 [tomida-2018-rac2-abstract]. The selectivity for Rac2 over the highly homologous Rac1 (which shares >92% amino acid sequence identity with Rac2) suggests that Ras and Rac2 may share structural similarities in their active sites that are recognized by the RASAL3 GAP domain [tomida-2018-rac2-abstract].

The dual specificity of RASAL3 for both Ras and Rac2 has significant biological implications, particularly in hematopoietic cells where both substrates are expressed. Rac2-AKT signaling is known to be hyperactivated in Philadelphia chromosome-positive leukemias, where the BCR-ABL fusion protein directly activates Rac2 [tomida-2018-rac2-abstract]. RASAL3 may therefore function to control AKT-mediated survival signaling through Rac2 GTPase regulation in addition to its established role in dampening Ras-ERK signaling.

## 4. Cellular Localization

RASAL3 is predominantly a cytoplasmic protein, as demonstrated through subcellular localization studies in T cell lines and other cell types [ishihara-2015-tcell-survival-abstract]. When expressed exogenously, RASAL3 protein localizes near or at the plasma membrane [human-protein-atlas-rasal3-summary]. Data from the Human Protein Atlas indicates that RASAL3 shows predicted localization to the nucleoplasm and plasma membrane, with observed cytoplasmic expression in subsets of immune cells [human-protein-atlas-rasal3-summary].

The cellular localization of RASAL3 is critical for its function because its substrates, Ras GTPases, are membrane-associated proteins. Ras proteins are anchored to the inner leaflet of the plasma membrane through post-translational lipid modifications and must be in this membrane-associated state to be active [simanshu-2017-rasgaps-review-abstract]. Therefore, for RASAL3 to inactivate Ras, it must either be constitutively present at the membrane or capable of translocating to the membrane in response to appropriate signals. The presence of PH and C2 domains in RASAL3 provides mechanisms for regulated membrane recruitment. The PH domain can bind phosphatidylinositol lipids, while the C2 domain can bind phospholipids in a calcium-dependent manner [ishihara-2015-tcell-survival-abstract][simanshu-2017-rasgaps-review-abstract].

Studies on the related protein RASAL1 have demonstrated that the C2 domain binding to lipid membranes and colocalization with Ras are required for RasGAP activity, suggesting that membrane recruitment is essential rather than optional for GAP function [simanshu-2017-rasgaps-review-abstract]. By analogy, RASAL3 likely undergoes regulated translocation from the cytoplasm to the plasma membrane to access its membrane-bound Ras substrates.

## 5. Signaling Pathways and Molecular Mechanisms

RASAL3 functions primarily as a negative regulator of the Ras/ERK (MAPK) signaling pathway, one of the most critical cascades controlling cell proliferation, differentiation, and survival [saito-2015-nkt-cells-abstract][ishihara-2015-tcell-survival-abstract]. By converting active Ras-GTP to inactive Ras-GDP, RASAL3 terminates Ras-mediated activation of the RAF-MEK-ERK kinase cascade. Experimental support for this comes from multiple studies: reduced RASAL3 expression results in increased levels of active Ras-GTP [saito-2021-neutrophils-abstract], overexpression of RASAL3 represses TCR-stimulated ERK phosphorylation [ishihara-2015-tcell-survival-abstract], and RASAL3 deficiency leads to enhanced ERK activation in various immune cell types [saito-2015-nkt-cells-abstract][saito-2021-neutrophils-abstract].

Beyond the canonical Ras-ERK pathway, RASAL3 regulates additional signaling cascades in immune cells. In neutrophils, RASAL3 deficiency leads to hyperactivation of multiple downstream pathways including NF-κB p65, p38 MAPK, and AKT phosphorylation following stimulation with lipopolysaccharide (LPS) [saito-2021-neutrophils-abstract]. This indicates that RASAL3 acts as a broad dampener of inflammatory signaling in these cells, consistent with its role in restraining excessive inflammatory responses.

A recent study identified RASAL3 as a component of a novel protein complex involved in regulating dendritic cell migration [olivier-2024-ccdc88b-abstract]. RASAL3 physically and functionally interacts with CCDC88B (a cytoskeleton-associated scaffold protein) and ARHGEF2 (a guanine nucleotide exchange factor for RhoA). In this complex, ARHGEF2 and RASAL3 act in opposing regulatory fashions: ARHGEF2 activates RhoA to promote cell migration, while RASAL3 restrains this activity [olivier-2024-ccdc88b-abstract]. RASAL3-deficient dendritic cells exhibit enhanced migration velocity and increased RhoA activation, demonstrating that RASAL3 normally acts to limit dendritic cell motility [olivier-2024-ccdc88b-abstract]. This finding reveals a new dimension to RASAL3 function beyond its established role in Ras-ERK signaling.

In T cells, RASAL3 appears to participate in tonic T cell receptor (TCR) signaling, the low-level basal signaling that maintains naive T cell survival in the absence of antigen [ishihara-2015-tcell-survival-abstract]. While the exact mechanism remains to be fully elucidated, RASAL3 is required for maintaining Bcl-2 expression levels in T cells, which is essential for their survival [muro-2018-tcell-inflammatory-abstract]. Loss of RASAL3 results in decreased Bcl-2 expression and increased apoptosis of naive T cells [muro-2018-tcell-inflammatory-abstract].

The identification of protein-protein interaction partners has provided additional insights into RASAL3 function. Proteomic studies using co-immunoprecipitation followed by LC-MS/MS identified CCDC88B and ARHGEF2 as the top physical interactors of RASAL3 [olivier-2024-ccdc88b-abstract]. These interactions were validated by reciprocal co-immunoprecipitation in multiple cell types and by confocal microscopy demonstrating colocalization [olivier-2024-ccdc88b-abstract]. According to the Human Protein Atlas, RASAL3 interacts with a total of 15 proteins, though the full interaction network and the functional significance of most of these interactions remain to be characterized [human-protein-atlas-rasal3-summary].

## 6. Tissue Expression and Biological Roles

RASAL3 exhibits a distinctive tissue expression pattern that sets it apart from most other RasGAP family members. While many RasGAPs show broad or ubiquitous tissue distribution, RASAL3 is predominantly expressed in cells of hematopoietic origin [saito-2015-nkt-cells-abstract][ishihara-2015-tcell-survival-abstract][saito-2021-neutrophils-abstract]. Expression analysis has demonstrated that RASAL3 mRNA is highest in lymphoid tissues including thymus, spleen, blood, and bone marrow [saito-2015-nkt-cells-abstract]. The Human Protein Atlas confirms enrichment in bone marrow, lymphoid tissue, intestine, and lung, with highest expression in spleen (39.2 nTPM), lymph node (30.7 nTPM), and bone marrow (22.2 nTPM) [human-protein-atlas-rasal3-summary].

At the cellular level, RASAL3 shows high expression in multiple immune cell types including T cells, NK cells, B cells, NKT cells, neutrophils, and microglia [human-protein-atlas-rasal3-summary][saito-2021-neutrophils-abstract]. Notably, neutrophils express significantly higher levels of RASAL3 compared to other leukocytes, with approximately twice the expression level seen in T cells, B cells, and monocytes [saito-2021-neutrophils-abstract]. This neutrophil-predominant expression is consistent across tissue microenvironments, being observed in neutrophils from bone marrow, spleen, peripheral blood, liver, and kidney [saito-2021-neutrophils-abstract].

Within the T cell lineage, RASAL3 expression shows dynamic regulation during development. Expression is highest in the thymus, decreases in CD4+CD8+ double-positive thymocytes, then peaks again in CD4 and CD8 single-positive cells. Expression decreases once more in mature peripheral T cells [ishihara-2015-tcell-survival-abstract]. This developmental pattern suggests that RASAL3 may play stage-specific roles in T cell maturation and function.

The biological functions of RASAL3 in immune cells have been characterized through studies of RASAL3-deficient mice. In T cells, RASAL3 is dispensable for thymic development—RASAL3 knockout mice show normal T cell development in the thymus even when tested with TCR transgenic models [ishihara-2015-tcell-survival-abstract]. However, RASAL3 is essential for maintaining peripheral naive T cell populations. RASAL3-deficient mice exhibit significantly reduced numbers of naive CD4+ and CD8+ T cells (but not effector memory T cells) in peripheral lymphoid organs, accompanied by increased apoptosis of these cells [ishihara-2015-tcell-survival-abstract][muro-2018-tcell-inflammatory-abstract]. The survival defect is evident in vivo (by adoptive transfer experiments) but not in vitro in IL-7-supplemented cultures, suggesting RASAL3's survival function relates to tonic TCR signaling rather than cytokine-dependent survival pathways [ishihara-2015-tcell-survival-abstract].

In NKT cells, RASAL3 plays a critical role in cellular expansion and function. RASAL3-deficient mice exhibit a severe decrease in liver NKT cell numbers by 8 weeks of age [saito-2015-nkt-cells-abstract]. Functionally, RASAL3 deficiency results in reduced cytokine production (IL-4 and IFN-γ) following stimulation with the NKT cell agonist α-galactosylceramide, and these mice are protected from α-GalCer-induced liver injury [saito-2015-nkt-cells-abstract].

In neutrophils, RASAL3 functions as a critical negative regulator of inflammatory responses. RASAL3 expression is upregulated (5-15 fold) when neutrophils encounter inflammatory stimuli such as LPS, PMA, or heat-killed bacteria [saito-2021-neutrophils-abstract]. In the absence of RASAL3, neutrophils display augmented inflammatory responses including increased cytokine production (IL-1β, TNF-α, IL-6), enhanced reactive oxygen species generation, and elevated formation of neutrophil extracellular traps (NETs) [saito-2021-neutrophils-abstract].

A striking and somewhat paradoxical observation is that RASAL3 deficiency produces divergent effects in different hematopoietic cell lineages [saito-2021-neutrophils-abstract]. While RASAL3 loss results in reduced numbers and impaired survival of lymphocytes (T cells, NKT cells), it leads to increased numbers of neutrophils and granulocytes in the bone marrow with enhanced pro-inflammatory effector functions [mgi-rasal3-ortholog-summary][saito-2021-neutrophils-abstract]. This cell type-specific divergence suggests that identical perturbations in Ras signaling can produce opposite biological outcomes depending on the cellular context, likely reflecting differences in downstream signaling pathway architecture and transcriptional responses between lymphoid and myeloid lineages. Understanding the mechanistic basis for these discordant effects remains an important area for future investigation.

## 7. Disease Associations and Therapeutic Implications

The loss of RASAL3 function has been linked to several disease-relevant phenotypes, particularly those involving dysregulated inflammation. RASAL3-knockout mice demonstrate accelerated mortality in a septic shock model, with 100% mortality by 48 hours compared to approximately 40% mortality in wild-type controls [saito-2021-neutrophils-abstract]. This increased susceptibility is associated with severe hepatic necrosis and exaggerated systemic inflammation driven by hyperactivated neutrophils [saito-2021-neutrophils-abstract].

Clinically relevant to human disease, neutrophils from patients with sickle cell disease exhibit suppressed RASAL3 expression upon LPS activation, correlating with enhanced inflammatory responses and increased sepsis susceptibility [saito-2021-neutrophils-abstract]. Given that sepsis is a major cause of mortality in sickle cell disease patients, the decreased RASAL3 expression in these cells may contribute to their heightened inflammatory state and increased infection-related mortality [saito-2021-neutrophils-abstract]. These findings suggest that RASAL3 agonists could represent a novel therapeutic approach for managing excessive inflammation in sepsis and other hyperinflammatory conditions [saito-2021-neutrophils-abstract].

In the context of autoimmune and inflammatory diseases, RASAL3 deficiency has complex and somewhat paradoxical effects. Mice lacking RASAL3 show protection against neuroinflammation in experimental autoimmune encephalomyelitis (EAE) and experimental cerebral malaria (ECM) models [olivier-2024-ccdc88b-abstract]. However, these same mice display enhanced susceptibility to DSS-induced colitis and increased colorectal cancer development [olivier-2024-ccdc88b-abstract]. Similarly, RASAL3-deficient mice show ameliorated Th1- and Th2-dependent contact hypersensitivity reactions due to reduced T cell numbers [muro-2018-tcell-inflammatory-abstract]. These observations highlight the dual nature of RASAL3 function: its loss can be protective in certain inflammatory contexts (by reducing T cell-mediated inflammation) while being detrimental in others (by promoting neutrophil-mediated hyperinflammation or compromising barrier immunity).

Despite the general role of RasGAP proteins as tumor suppressors (NF1, RASAL1, RASAL2, and DAB2IP have established tumor suppressor functions), the evidence for RASAL3 as a cancer gene is currently limited [simanshu-2017-rasgaps-review-abstract][omim-616561-rasal3-summary]. According to the Cancer Gene Census (COSMIC), RASAL3 is not classified as a known cancer gene, and mouse insertional mutagenesis experiments do not support its designation as a cancer-causing gene [omim-616561-rasal3-summary]. This is notable given the hematopoietic-restricted expression of RASAL3, which would theoretically position it as a candidate tumor suppressor in hematological malignancies. However, the discovery that RASAL3 can regulate Rac2 GTPase activity has implications for Philadelphia chromosome-positive leukemias, where BCR-ABL directly activates Rac2 to promote cell survival through AKT signaling [tomida-2018-rac2-abstract]. RASAL3 may therefore function as a negative regulator of Rac2-AKT survival signaling in these leukemias, though this hypothesis requires direct experimental validation.

The Human Protein Atlas indicates that RASAL3 shows limited expression in most solid tumors, consistent with its hematopoietic tissue specificity [human-protein-atlas-rasal3-summary]. Some non-Hodgkin lymphomas show moderate cytoplasmic RASAL3 positivity, though the functional significance of this expression in lymphoma biology remains unexplored [human-protein-atlas-rasal3-summary]. The lack of established cancer associations may reflect the specialized nature of RASAL3 in immune cell function rather than general cell cycle control.

## 8. Open Questions

Despite significant progress in understanding RASAL3 function, several important questions remain unanswered:

**Substrate Specificity:** While RASAL3 has been shown to act on Ras and Rac2 in vitro, the relative contributions of these two activities to RASAL3's biological functions in vivo remain unclear. Are there cellular contexts where one activity predominates over the other? Does RASAL3 exhibit differential activity toward the three major Ras isoforms (HRAS, KRAS, NRAS)?

**Regulatory Mechanisms:** How is RASAL3 activity regulated? The mechanisms controlling RASAL3 membrane recruitment, GAP activity, and protein stability remain largely unexplored. Does calcium binding to the C2 domain regulate RASAL3 function as it does for other C2 domain-containing GAPs?

**Structural Biology:** No crystal structure of RASAL3 has been reported. Structural studies would provide insights into the basis for its substrate specificity and inform the design of potential therapeutic modulators.

**Cancer Role:** Does RASAL3 function as a tumor suppressor in hematological malignancies? Are RASAL3 mutations or epigenetic silencing observed in leukemias or lymphomas? What is the functional significance of RASAL3 expression in lymphomas?

**Therapeutic Development:** Can RASAL3 be targeted therapeutically? Would RASAL3 agonists be beneficial in sepsis and hyperinflammatory conditions? Could RASAL3 inhibitors be useful in conditions where enhanced immune cell function is desired?

**Dendritic Cell Function:** The recent discovery of RASAL3's role in dendritic cell migration through RhoA regulation opens new questions. How does RASAL3 integrate its Ras-GAP and RhoA-regulatory activities? Is Rac2 also involved in this context?

**NKT Cell Biology:** Why does RASAL3 deficiency specifically affect liver NKT cells? What is the mechanism by which RASAL3 regulates NKT cell expansion and cytokine production?

**Human Genetics:** Are there human genetic variants in RASAL3 associated with immune disorders, inflammatory diseases, or hematological malignancies? Population-scale genetic studies may reveal disease associations.

## References

* **[ishihara-2015-tcell-survival-abstract]** Ishihara S, Fujita M, Takenaka-Ishikawa S, Tamura M, Koyama Y, Kawamura T, et al. (2015) The Ras GTPase-Activating Protein Rasal3 Supports Survival of Naive T Cells. PLoS ONE 10(3): e0119898. PMID: 25793935. PMCID: PMC4368693. DOI: 10.1371/journal.pone.0119898. URL: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0119898

* **[saito-2015-nkt-cells-abstract]** Saito S, Kawamura T, Higuchi M, Kobayashi T, Yoshita-Takahashi M, Yamazaki M, et al. (2015) RASAL3, a novel hematopoietic RasGAP protein, regulates the number and functions of NKT cells. European Journal of Immunology 45(5):1512-23. PMID: 25652366. DOI: 10.1002/eji.201444977. URL: https://onlinelibrary.wiley.com/doi/full/10.1002/eji.201444977

* **[saito-2021-neutrophils-abstract]** Saito S, Cao DY, Victor AR, Peng Z, Wu HY, Okwan-Duodu D (2021) RASAL3 Is a Putative RasGAP Modulating Inflammatory Response by Neutrophils. Frontiers in Immunology 12:744300. PMID: 34777356. PMCID: PMC8579101. DOI: 10.3389/fimmu.2021.744300. URL: https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2021.744300/full

* **[muro-2018-tcell-inflammatory-abstract]** Muro R, Nitta T, Kitajima M, Okada T, Suzuki H (2018) Rasal3-mediated T cell survival is essential for inflammatory responses. Biochemical and Biophysical Research Communications 496(1):25-30. PMID: 29291408. DOI: 10.1016/j.bbrc.2017.12.159. URL: https://pubmed.ncbi.nlm.nih.gov/29291408/

* **[olivier-2024-ccdc88b-abstract]** Olivier JF, Langlais D, et al. (2024) CCDC88B interacts with RASAL3 and ARHGEF2 and regulates dendritic cell function in neuroinflammation and colitis. Communications Biology 7(1):77. PMID: 38200184. PMCID: PMC10781698. DOI: 10.1038/s42003-023-05751-9. URL: https://www.nature.com/articles/s42003-023-05751-9

* **[tomida-2018-rac2-abstract]** Tomida S, Saito S, Kitagawa M (2018) RASAL3 preferentially stimulates GTP hydrolysis of the Rho family small GTPase Rac2. Biomedical Reports 9(3):255-260. PMCID: PMC6158391. DOI: 10.3892/br.2018.1119. URL: https://www.spandidos-publications.com/10.3892/br.2018.1119

* **[simanshu-2017-rasgaps-review-abstract]** Simanshu DK, Nissley DV, McCormick F (2017) Ras-Specific GTPase-Activating Proteins—Structures, Mechanisms, and Interactions. Cold Spring Harbor Perspectives in Medicine 9(3):a031500. PMID: 28620452. PMCID: PMC6396337. DOI: 10.1101/cshperspect.a031500. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC6396337/

* **[human-protein-atlas-rasal3-summary]** The Human Protein Atlas - RASAL3 (ENSG00000105122). URL: https://www.proteinatlas.org/ENSG00000105122-RASAL3

* **[ncbi-gene-rasal3]** NCBI Gene: RASAL3 RAS protein activator like 3 [Homo sapiens (human)] - Gene ID: 64926. URL: https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=64926

* **[omim-616561-rasal3-summary]** OMIM Entry - *616561 - RAS PROTEIN ACTIVATOR-LIKE 3; RASAL3. URL: https://omim.org/entry/616561

* **[genecards-rasal3]** GeneCards - RASAL3 Gene. URL: https://www.genecards.org/cgi-bin/carddisp.pl?gene=RASAL3

* **[mgi-rasal3-ortholog-summary]** Mouse Genome Informatics - Rasal3 (MGI:2444128). URL: https://www.informatics.jax.org/marker/MGI:2444128


## Citations

1. human-protein-atlas-rasal3-summary.md
2. ishihara-2015-tcell-survival-abstract.md
3. mgi-rasal3-ortholog-summary.md
4. muro-2018-tcell-inflammatory-abstract.md
5. olivier-2024-ccdc88b-abstract.md
6. omim-616561-rasal3-summary.md
7. saito-2015-nkt-cells-abstract.md
8. saito-2021-neutrophils-abstract.md
9. simanshu-2017-rasgaps-review-abstract.md
10. tomida-2018-rac2-abstract.md