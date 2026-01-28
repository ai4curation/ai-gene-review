---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-22T17:09:02.460852'
end_time: '2026-01-22T17:32:05.496265'
duration_seconds: 1383.04
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: DPT
  gene_symbol: DPT
  uniprot_accession: Q07507
  protein_description: 'RecName: Full=Dermatopontin; AltName: Full=Tyrosine-rich acidic
    matrix protein; Short=TRAMP; Flags: Precursor;'
  gene_info: Name=DPT;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the dermatopontin family. .
  protein_domains: Dermatopontin. (IPR026645); DERM (PF14704)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 19
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q07507
- **Protein Description:** RecName: Full=Dermatopontin; AltName: Full=Tyrosine-rich acidic matrix protein; Short=TRAMP; Flags: Precursor;
- **Gene Information:** Name=DPT;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the dermatopontin family. .
- **Key Domains:** Dermatopontin. (IPR026645); DERM (PF14704)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "DPT" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'DPT' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **DPT** (gene ID: DPT, UniProt: Q07507) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Dermatopontin (DPT): A Comprehensive Functional Annotation Report

## 1. Introduction and Overview

Dermatopontin (DPT), also known as tyrosine-rich acidic matrix protein (TRAMP), is a small non-collagenous extracellular matrix (ECM) protein encoded by the DPT gene in humans (UniProt: Q07507). The protein was first identified in 1993 by Cronshaw and colleagues at the University of Edinburgh, who isolated a 24 kDa protein that co-purified with lysyl oxidase from porcine skin [cronshaw-1993-discovery-abstract]. Sequence analysis revealed this protein was identical to a previously described bovine skin protein associated with dermatan sulfate proteoglycans. Due to its high tyrosine content and acidic nature (isoelectric point 4.1-4.4), the investigators proposed the name TRAMP (Tyrosine Rich Acidic Matrix Protein) [cronshaw-1993-discovery-abstract].

The mature protein has a molecular weight of approximately 22 kDa and is estimated to comprise approximately 12 mg/kg of wet dermis weight, making it a relatively abundant component of the dermal extracellular matrix [okamoto-2006-review-abstract]. In 1994, Forbes and colleagues demonstrated using polyclonal antiserum that TRAMP/dermatopontin has a widespread tissue distribution, including skin, skeletal muscle, heart, lung, kidney, cartilage, and bone [forbes-1994-tramp-abstract]. Their experiments with human skin fibroblast cultures showed that the protein incorporates both [³⁵S]sulfate and [³H]tyrosine before being secreted into the medium, providing early evidence for tyrosine sulfation as a key post-translational modification [forbes-1994-tramp-abstract].

The protein is composed of 183 amino acids, of which 20 are tyrosine residues, explaining its alternative designation as a "tyrosine-rich" matrix protein. A distinctive biochemical feature of DPT is that it undergoes tyrosine sulfation as a post-translational modification but is not glycosylated [jensen-2022-collagen-binding-abstract]. The presence of up to six sulfotyrosine residues has been confirmed in purified DPT variants, with the major circulating form containing four such modifications [jensen-2022-collagen-binding-abstract]. This sulfation pattern is functionally significant for collagen binding, as discussed below.

In vertebrates, the primary functions of dermatopontin encompass four major roles: serving as a structural component of the ECM through interaction with decorin and modification of collagen fibrillogenesis; mediating cell adhesion; modulating TGF-β activity; and regulating cellular quiescence and proliferation [okamoto-2006-review-abstract]. The protein is evolutionarily conserved, with homologues identified across mammals and several invertebrate species, including mollusks where dermatopontin has been co-opted for shell matrix formation [sarashina-2006-evolution-abstract].

## 2. Protein Structure and Domains

Dermatopontin belongs to the dermatopontin protein family (InterPro: IPR026645) and contains the characteristic DERM domain (Pfam: PF14704). The protein contains three disulfide-bonded loop structures that enclose conserved hexapeptide motifs, which are thought to be important for its structural integrity and function [kim-2019-myogenesis-abstract]. In molluscan homologues, a characteristic sequence motif (D-R-X-W/F/Y-X-F/Y/I/L/M-X1–2-C) has been identified that is repeated three times in the entire sequence [sarashina-2006-evolution-abstract].

Although the three-dimensional crystal structure of DPT has not been experimentally determined, computational modeling efforts have provided structural predictions. Kim and colleagues used threading-based automated protein modeling to generate a 3D structure, with the best model produced by SPARKS-X showing 87.4% of residues in the favored region of the Ramachandran plot [kim-2019-myogenesis-abstract]. This predicted structure has been deposited in the Protein Model Data Base (ID: PM0081951) [kim-2019-myogenesis-abstract].

The protein is acidic in nature, rich in tyrosine residues, and is secreted into the extracellular space following removal of a signal peptide during processing. A critical cell-adhesion active sequence, GQVVVAVR (an eight-amino acid peptide), has been identified within the protein and is essential for keratinocyte adhesion activity [okamoto-2010-keratinocyte-abstract].

## 3. Collagen Binding and Fibrillogenesis

One of the most well-characterized functions of dermatopontin is its role in collagen fibrillogenesis. DPT accelerates the formation of collagen fibrils and modifies the properties of newly formed fibrils, determining their size and arrangement within the extracellular matrix [takeda-2002-knockout-abstract]. This function has been demonstrated both through in vitro reconstitution experiments and through knockout mouse studies.

The molecular basis of DPT-collagen interaction was elucidated in a comprehensive 2022 study by Jensen and colleagues, who used Collagen Toolkit peptide arrays to map DPT binding sites on triple-helical collagens II and III [jensen-2022-collagen-binding-abstract]. They discovered that DPT binds preferentially to arginine-rich, positively-charged sequences on collagen that also contain hydrophobic residues. Critically, DPT-binding loci include the triple helix crosslinking sites and the collagenase cleavage site, suggesting that DPT may protect these functionally important regions [jensen-2022-collagen-binding-abstract].

The collagen-binding signature of DPT is remarkably similar to that of HSP47 (SERPINH1), the intracellular collagen-specific chaperone. Based on this finding, Jensen et al. proposed that DPT may assume the role of HSP47 as a collagen chaperone during and after secretion into the extracellular space [jensen-2022-collagen-binding-abstract]. Mutagenesis studies confirmed the importance of specific arginine residues: substituting any of the three arginine residues in the sequence GLAGQRGIVGLOGQRGER resulted in almost complete loss of DPT binding [jensen-2022-collagen-binding-abstract]. This observation has potential clinical significance, as missense mutations substituting corresponding arginine residues in collagens α-1(I) and α-1(II) are associated with connective tissue disorders including osteogenesis imperfecta and spondyloepiphyseal dysplasia [jensen-2022-collagen-binding-abstract].

The functional importance of DPT in collagen organization was definitively demonstrated through targeted gene disruption studies. Takeda and colleagues generated dermatopontin knockout mice and, although the animals showed no obvious anatomical abnormalities, their skin exhibited increased elasticity and reduced tensile strength [takeda-2002-knockout-abstract]. Electron microscopic analysis revealed that collagen fibrils in DPT-null mice displayed great variety in diameter and irregular contours, contrasting with the uniform fibrils seen in wild-type animals [takeda-2002-knockout-abstract]. Furthermore, skin collagen content was reduced by 40% in knockout mice compared to wild-type controls, and the relative thickness of the dermis was significantly decreased [takeda-2002-knockout-abstract]. These phenotypic features resemble aspects of Ehlers-Danlos syndrome, a group of connective tissue disorders characterized by abnormal collagen structure and function [okamoto-2006-review-abstract].

## 4. Role in Corneal Stromal Organization

The importance of dermatopontin in collagen organization extends beyond the skin to other tissues, notably the cornea. Cooper and colleagues investigated DPT function in corneal matrix organization using knockout mice and found significant structural abnormalities [cooper-2006-cornea-abstract].

Light microscopy demonstrated that DPT-deficient corneas showed a 24% reduction in average stromal thickness compared to wild-type animals (81.8 ± 21.5 μm versus 107.3 ± 21.2 μm; P < 0.001) [cooper-2006-cornea-abstract]. Transmission electron microscopy revealed significant disruption of fibril spacing within the posterior lamellae, characterized by less well-defined lamellae with little or no obvious banding compared to wild-type controls [cooper-2006-cornea-abstract]. Interestingly, the anterior and mid-stromal regions remained largely unaffected, suggesting regional specificity in DPT function within the cornea [cooper-2006-cornea-abstract].

The keratocytes (corneal fibroblasts) and epithelium appeared morphologically normal in knockout animals. Collagen fibrils displayed lower volume fractions and altered posterior organization but no changes in fibril diameter [cooper-2006-cornea-abstract]. The authors suggested that DPT may interact with corneal proteoglycans to maintain stromal architecture, particularly in the posterior region [cooper-2006-cornea-abstract]. These findings, combined with the high concentration of DPT in porcine corneal stroma (~0.02% by mass) [jensen-2022-collagen-binding-abstract], indicate an important role for this protein in corneal structure and potentially transparency.

## 5. Interaction with Fibronectin and ECM Assembly

Beyond its effects on collagen, dermatopontin plays important roles in the assembly of other ECM components, particularly fibronectin. Kato and colleagues demonstrated that DPT directly interacts with fibronectin and promotes the formation of fibronectin fibrils [kato-2011-fibronectin-abstract].

Using solid-phase binding assays and recombinant fibronectin domains, the study identified that DPT binds strongly to fibronectin type III repeats, particularly III13 and III14, with III1 serving as a potential cryptic binding site [kato-2011-fibronectin-abstract]. Mechanistically, DPT enhances the interaction between fibronectin's I1-5 domain and III12-14 repeats while partially disrupting the intramolecular interaction between III2-3 and III12-14. This disruption is significant because the III2-3 to III12-14 interaction is crucial for maintaining the compact conformation of native fibronectin; thus, DPT binding induces conformational changes that expose cryptic self-association sites and promote fibril formation [kato-2011-fibronectin-abstract].

Electron microscopy revealed that when incubated with DPT, fibronectin formed an insoluble complex of fibrils appearing as structures 50-200 nm in diameter with irregular, tortuous morphology [kato-2011-fibronectin-abstract]. Functionally, the ternary complex of DPT, fibronectin, and fibrin dramatically enhanced fibroblast adhesion (approximately 10-fold) compared to fibrin-fibronectin complexes alone, and this adhesion was mediated through α5β1 integrin receptors [kato-2011-fibronectin-abstract]. These findings position DPT as an important regulator of provisional matrix assembly during tissue repair.

## 6. Cell Adhesion Mechanisms

Dermatopontin mediates cell adhesion through interactions with cell surface receptors, primarily integrins. This function links communication between the cell surface of fibroblasts and other cell types with their surrounding ECM environment [okamoto-2010-keratinocyte-abstract].

Studies using human epidermal keratinocytes (HaCaT cells) demonstrated that these cells spread on dermatopontin substrates and form organized actin stress fibers [okamoto-2010-keratinocyte-abstract]. The adhesion mechanism involves two receptor systems: the α3β1 integrin and heparan sulfate proteoglycan-type receptors, likely syndecans [okamoto-2010-keratinocyte-abstract]. This dual receptor system was confirmed by experiments showing that adhesion was inhibited by both EDTA (disrupting integrin function) and heparin (competing with proteoglycan binding) [okamoto-2010-keratinocyte-abstract].

The α3β1 integrin receptor is particularly important for DPT-mediated cellular responses. In cardiac fibroblasts, integrin α3β1 was identified as at least one receptor mediating adhesion, spreading, and migration responses to DPT [liu-2013-cardiac-abstract]. The significance of this interaction extends to endothelial cells, where exogenously supplied DPT modulates the expression of both TGF-β1 and integrin α3β1, proteins with crucial roles in endothelial cell behavior during angiogenesis [liu-2013-cardiac-abstract].

## 7. Modulation of TGF-β Signaling

One of the most functionally significant aspects of dermatopontin biology is its ability to modulate transforming growth factor-β (TGF-β) signaling. This was first characterized by Okamoto and colleagues, who demonstrated that DPT interacts with both decorin and TGF-β1 to enhance TGF-β biological activity [okamoto-1999-tgfb-abstract].

Using solid-phase binding assays, the study found that dermatopontin binds decorin with an apparent dissociation constant (Kd) of 100 nM [okamoto-1999-tgfb-abstract]. Importantly, dermatopontin inhibits the formation of the decorin-TGF-β1 complex, and decorin reciprocally competes with dermatopontin for TGF-β1 binding [okamoto-1999-tgfb-abstract]. However, when both proteins are present together, the dermatopontin-decorin complex binds 3-fold more TGF-β1 than either component individually [okamoto-1999-tgfb-abstract]. This suggests a complex regulatory mechanism where the stoichiometry of these interactions determines local TGF-β availability.

Functional studies using mink lung epithelial cells transfected with a plasminogen activator inhibitor (PAI-1) promoter-luciferase construct confirmed the biological significance of these interactions. Dermatopontin augmented TGF-β1-induced luciferase expression, demonstrating enhanced TGF-β biological activity [okamoto-1999-tgfb-abstract]. While dermatopontin alone showed only weak inhibitory effects on cell proliferation, it significantly enhanced the growth-inhibitory activity of TGF-β on these cells [okamoto-1999-tgfb-abstract]. The authors concluded that dermatopontin modifies the behavior of TGF-β through interaction with decorin in the microenvironment of the extracellular matrix, effectively increasing cellular responsiveness to this cytokine [okamoto-1999-tgfb-abstract].

## 8. Cellular Localization and Tissue Distribution

Dermatopontin is an extensively distributed component of the extracellular matrix. The original tissue distribution studies by Forbes et al. using polyclonal antiserum demonstrated widespread expression including skin, skeletal muscle, heart, lung, kidney, cartilage, and bone [forbes-1994-tramp-abstract]. In the skin, DPT is located predominantly on the surface of collagen fibers and is particularly abundant in the dermis [okamoto-2006-review-abstract].

The subcellular localization of DPT is extracellular, consistent with its function as a secreted ECM component. Following translation and removal of the signal peptide, the protein is secreted and becomes associated with collagen fibers and other ECM components. In the skin, DPT distributes throughout the dermal layer and participates in the structural organization of the collagenous matrix [takeda-2002-knockout-abstract]. In the cornea, DPT is present at relatively high concentrations (~0.02% by mass) in the stromal ECM [jensen-2022-collagen-binding-abstract].

Expression patterns vary under pathological conditions. Notably, fibroblasts from patients with systemic sclerosis and hypertrophic scars show significantly reduced DPT expression compared to normal skin fibroblasts [kuroda-1999-fibrosis-abstract]. This reduced expression appears to be functionally significant for fibrosis pathogenesis. In vitro studies demonstrated that TGF-β1 increases DPT mRNA and protein levels, while interleukin-4 reduces expression [kuroda-1999-fibrosis-abstract]. Interestingly, type I collagen substrate suppresses DPT expression, with more pronounced reduction observed in three-dimensional collagen matrices [kuroda-1999-fibrosis-abstract].

## 9. Role in Wound Healing and Tissue Repair

The cell adhesion and ECM assembly functions of dermatopontin position it as an important player in wound healing. During normal wound repair, DPT promotes cell adhesion to fibrin fibers of the provisional matrix in a dose-dependent manner and facilitates fibrillation of both collagen and fibronectin [krishnaswamy-2014-wounds-abstract].

### Re-epithelialization

A critical aspect of DPT function in wound healing is its role in re-epithelialization, the process by which keratinocytes migrate to cover the wound surface. Krishnaswamy and Korrapati demonstrated that DPT promotes keratinocyte migration in a dose-dependent fashion but, importantly, does not stimulate keratinocyte proliferation [krishnaswamy-2014-reepithelialization-abstract]. This separation of migratory and proliferative effects suggests that DPT functions specifically to facilitate cell movement rather than cell division during the re-epithelialization process.

Molecular analysis revealed a striking pattern of tissue-specific expression: DPT shows negligible expression in the epidermis but demonstrates prominent presence in the dermis [krishnaswamy-2014-reepithelialization-abstract]. This distribution indicates that DPT facilitates wound healing through paracrine mechanisms, with dermal-derived DPT acting on epidermal keratinocytes from below to enhance their migratory capacity [krishnaswamy-2014-reepithelialization-abstract]. This paracrine mode of action positions DPT as a key mediator of dermal-epidermal communication during tissue repair.

### Cardiac Repair

Evidence for DPT's role in tissue repair comes from studies of myocardial infarction. Following experimentally induced myocardial infarction in rats, dermatopontin mRNA expression increased progressively in the infarct zone, with levels rising to 2.4-fold by day 7, 4.1-fold by day 14, and 4.2-fold by day 28 compared to pre-ligation hearts [takemoto-2002-infarct-abstract]. In situ hybridization localized the expression to macrophages and mesenchymal cells within the infarct zone, and the temporal pattern paralleled that of decorin and type I collagen, suggesting coordinated participation in ECM reformation [takemoto-2002-infarct-abstract].

In the heart, DPT promotes adhesion, spreading, and migration of cardiac fibroblasts, and these effects are mediated through integrin α3β1 [liu-2013-cardiac-abstract]. Hypoxia and serum deprivation, conditions mimicking the ischemic environment of infarcted tissue, stimulate DPT expression and secretion from cardiac cells [liu-2013-cardiac-abstract]. These findings suggest that DPT may represent a therapeutic target for modulating ventricular remodeling following myocardial infarction.

In contrast to normal wound healing, chronic cutaneous wounds show a paradoxical pattern: despite elevated DPT mRNA levels, protein levels are markedly reduced in both wound tissue and wound exudates [krishnaswamy-2014-wounds-abstract]. This discrepancy is explained by protease-mediated degradation; the elevated proteolytic environment characteristic of chronic wounds leads to DPT destruction, contributing to impaired healing [krishnaswamy-2014-wounds-abstract]. During normal healing, a balance exists between pro-migration dermatopontin and anti-migration decorin, with mutual regulation of their activities [krishnaswamy-2014-wounds-abstract].

DPT also possesses pro-angiogenic properties, enhancing endothelial cell motility, inducing lamellipodia formation, and stimulating tube formation on matrigel substrates [liu-2013-cardiac-abstract]. Additionally, DPT accelerates fibrin fibril formation and the resulting fibrin fibrils with DPT enhance endothelial cell attachment, spreading, and cytoskeletal organization [kato-2011-fibronectin-abstract].

## 10. Role in Myogenesis and Muscle Regeneration

Recent work has expanded our understanding of DPT function to include skeletal muscle biology. Kim and colleagues demonstrated that DPT actively regulates muscle development through three mechanisms: enhancing cell adhesion, reducing cell proliferation, and promoting myoblast differentiation [kim-2019-myogenesis-abstract].

In the context of skeletal muscle ECM, DPT works synergistically with fibromodulin (FMOD) to promote myogenesis, with the two proteins positively regulating each other [kim-2019-myogenesis-abstract]. In contrast, DPT and fibronectin exhibit opposing effects on myoblast behavior [kim-2019-myogenesis-abstract]. During muscle regeneration following injury, DPT expression increases during differentiation phases, confirming its essential role in muscle recovery processes [kim-2019-myogenesis-abstract].

## 11. Role in Adipose Tissue and Obesity

Recent research has identified dermatopontin as a novel adipokine with important roles in adipose tissue biology and obesity-associated complications. Unamuno and colleagues demonstrated that obesity and obesity-associated type 2 diabetes are accompanied by increased circulating levels of DPT, with elevated gene expression in visceral adipose tissue (VAT) of obese patients [unamuno-2020-adipokine-abstract].

In human visceral adipocytes, DPT expression is dynamically regulated by inflammatory signals. Pro-inflammatory stimuli including lipopolysaccharide (LPS), TGF-β, and palmitic acid enhance DPT gene expression, while anti-inflammatory cytokines IL-4 and IL-13 produce downregulation [unamuno-2020-adipokine-abstract]. This regulatory pattern suggests DPT expression is integrated into adipose tissue inflammatory responses.

Functionally, DPT promotes both ECM remodeling and inflammation in adipocytes. Treatment with DPT increased expression of ECM-related genes including COL6A3 (collagen VI), ELN (elastin), MMP9 (matrix metalloproteinase 9), and TNMD (tenomodulin), as well as inflammation-related factors IL6, IL8, and TNF [unamuno-2020-adipokine-abstract]. These findings indicate that DPT contributes to the structural and inflammatory changes characteristic of dysfunctional adipose tissue in obesity, providing a mechanistic link between ECM remodeling and metabolic dysfunction.

## 12. Evolutionary Conservation

Dermatopontin is evolutionarily conserved across metazoans, with homologues identified in mammals, other vertebrates, and invertebrates. The evolutionary history of dermatopontin in mollusks has been particularly well studied, revealing interesting patterns of functional diversification.

Sarashina and colleagues identified 14 molluscan dermatopontin homologues from eight snail species belonging to the orders Basommatophora (pond snails) and Stylommatophora (land snails) [sarashina-2006-evolution-abstract]. A major shell matrix protein originally obtained from a freshwater snail was identified as a molluscan homologue of dermatopontin. In the basommatophoran lineage, three dermatopontin types were identified: one appears to function as a shell matrix protein involved in biomineralization, while the others have more general ECM functions based on gene expression analyses [sarashina-2006-evolution-abstract].

Significantly, the study revealed that potential N-glycosylation sites were found exclusively in the dermatopontin variants associated with shell calcification, suggesting this modification may be important for biomineralization function [sarashina-2006-evolution-abstract]. In the two gastropod lineages examined, recruitment of dermatopontin to the shell matrix occurred at least twice independently following lineage divergence, indicating convergent evolution of this function [sarashina-2006-evolution-abstract].

In the pearl oyster Pinctada martensii, DPT mRNA is constitutively expressed in all studied tissues with the most abundant expression in the mantle, which is the tissue responsible for nacre (mother-of-pearl) formation. These findings suggest that dermatopontin has been repeatedly co-opted for roles in biomineralization in invertebrates, while retaining its ancestral ECM functions in vertebrates.

## 13. Disease Associations and Clinical Relevance

Reduced dermatopontin expression has been associated with several pathological conditions. In fibrotic diseases including systemic sclerosis and hypertrophic scarring, fibroblasts show decreased DPT expression, which may contribute to aberrant collagen deposition and tissue architecture [kuroda-1999-fibrosis-abstract].

The knockout mouse phenotype, resembling Ehlers-Danlos syndrome with increased skin elasticity, reduced tensile strength, and abnormal collagen fibril morphology, suggests that DPT deficiency or dysfunction could contribute to connective tissue disorders in humans [takeda-2002-knockout-abstract]. The discovery that DPT binds to specific arginine-containing sequences on collagen that are mutated in osteogenesis imperfecta and spondyloepiphyseal dysplasia further supports a potential role for disrupted DPT-collagen interactions in skeletal connective tissue diseases [jensen-2022-collagen-binding-abstract].

### Cancer Associations

Downregulation of DPT has been observed in several cancers, and accumulating evidence suggests DPT may function as a tumor suppressor. The most detailed mechanistic study was conducted by Fu and colleagues in hepatocellular carcinoma (HCC) [fu-2014-hcc-abstract]. They demonstrated that DPT was significantly downregulated in 202 HCC clinical samples, and its expression level was closely correlated with indicators of tumor metastasis (such as vascular invasion and tumor thrombosis) and patient prognosis [fu-2014-hcc-abstract].

The silencing of DPT in HCC was shown to occur through epigenetic mechanisms, specifically DNA methylation of the DPT promoter region [fu-2014-hcc-abstract]. Functionally, overexpression of DPT dramatically suppressed HCC cell migration in vitro and intrahepatic metastasis in vivo. The inhibitory effects of DPT on HCC cell motility were associated with dysregulated focal adhesion assembly, decreased RhoA activity, and reduced phosphorylation of focal adhesion kinase (FAK) and Src tyrosine kinase. These alterations required α3β1 integrin signaling [fu-2014-hcc-abstract].

The authors proposed that DPT serves as a novel prognostic marker and metastasis suppressor in HCC, and suggested that demethylating agents to restore DPT expression may have therapeutic potential [fu-2014-hcc-abstract]. DPT downregulation has also been reported in other cancers including uterine leiomyomas, with studies suggesting DPT can inhibit various tumor-related signaling pathways including Wnt/β-catenin, TGF-β, Hippo/YAP, and ERK/MAPK pathways.

### Cholangiocarcinoma and Tumor Immune Microenvironment

More recent work has extended the understanding of DPT's tumor suppressor function to cholangiocarcinoma (CHOL) and has revealed an important role in modulating the tumor immune microenvironment. Xu and colleagues demonstrated that CHOL patients with low DPT expression have significantly poorer prognosis [xu-2024-cholangiocarcinoma-abstract]. Enrichment analysis showed a positive correlation between DPT expression levels and infiltration of immune cells and immunomodulatory factors [xu-2024-cholangiocarcinoma-abstract].

Mechanistically, the study revealed that DPT downregulation in cholangiocarcinoma cells suppresses the secretion of CCL19, a chemokine crucial for immune cell recruitment, by macrophages [xu-2024-cholangiocarcinoma-abstract]. CCL19 normally functions to attract T cells and dendritic cells to tumor sites. This finding suggests that DPT may enhance anti-tumor immunity by promoting macrophage secretion of immune-recruiting chemokines, thereby increasing immune cell infiltration into the tumor microenvironment.

Importantly, enhanced DPT levels were correlated with improved responses to anti-PD-1/PD-L1 immunotherapy in cholangiocarcinoma, suggesting that DPT expression status may serve as a biomarker for immunotherapy responsiveness [xu-2024-cholangiocarcinoma-abstract]. These findings expand the tumor suppressor function of DPT beyond direct effects on cancer cell migration to include modulation of the tumor immune microenvironment.

## 14. Open Questions

Several important questions about dermatopontin biology remain to be addressed:

1. **Structural basis of function**: While computational models of DPT structure exist, experimental determination of the three-dimensional structure by X-ray crystallography or cryo-EM would provide crucial insights into the molecular basis of its diverse interactions with collagen, fibronectin, decorin, and TGF-β.

2. **Role of tyrosine sulfation**: Although DPT is tyrosine-sulfated, the precise contribution of this modification to collagen binding and other functions remains incompletely understood. Studies using desulfated or sulfation-site mutant DPT would clarify this.

3. **Therapeutic potential**: Given DPT's roles in wound healing, cardiac remodeling, and tumor suppression, could recombinant DPT or DPT-derived peptides be developed as therapeutics for chronic wounds, cardiac fibrosis, or cancer?

4. **Regulation of expression**: What are the complete transcriptional and post-transcriptional mechanisms controlling DPT expression in different tissues and under various physiological and pathological conditions?

5. **Human genetic variants**: Are there common or rare variants in the human DPT gene associated with connective tissue disorders, wound healing abnormalities, or other phenotypes?

6. **Interaction network**: The full spectrum of DPT binding partners in the ECM and on cell surfaces remains to be comprehensively defined using unbiased proteomic approaches.

7. **Regional specificity in cornea**: Why is DPT function most critical for the posterior stroma of the cornea? What proteoglycans or other factors are involved?

8. **Evolutionary questions**: What drove the independent recruitment of dermatopontin to shell matrix function in multiple mollusk lineages, and how do N-glycosylation modifications enable this new function?

## References

1. **cronshaw-1993-discovery**: Cronshaw AD, MacBeath JR, Shackleton DR, Collins JF, Fothergill-Gilmore LA, Hulmes DJ. TRAMP (tyrosine rich acidic matrix protein), a protein that co-purifies with lysyl oxidase from porcine skin. Identification of TRAMP as the dermatan sulphate proteoglycan-associated 22K extracellular matrix protein. Matrix. 1993;13(3):255-66. DOI: 10.1016/s0934-8832(11)80009-0. PMID: 8100985.

2. **forbes-1994-tramp**: Forbes EG, Cronshaw AD, MacBeath JR, Hulmes DJ. Tyrosine-rich acidic matrix protein (TRAMP) is a tyrosine-sulphated and widely distributed protein of the extracellular matrix. FEBS Letters. 1994;351(3):433-6. DOI: 10.1016/0014-5793(94)00907-4. PMID: 8082810.

3. **okamoto-2006-review**: Okamoto O, Fujiwara S. Dermatopontin, a novel player in the biology of the extracellular matrix. Connective Tissue Research. 2006;47(4):177-189. DOI: 10.1080/03008200600846564. PMID: 16987749.

4. **takeda-2002-knockout**: Takeda U, Utani A, Wu J, Adachi E, Koseki H, Taniguchi M, Matsumoto T, Ohashi T, Sato M, Shinkai H. Targeted disruption of dermatopontin causes abnormal collagen fibrillogenesis. Journal of Investigative Dermatology. 2002;119(3):678-83. DOI: 10.1046/j.1523-1747.2002.01863.x. PMID: 12230512.

5. **okamoto-1999-tgfb**: Okamoto O, Fujiwara S, Abe M, Sato Y. Dermatopontin interacts with transforming growth factor beta and enhances its biological activity. Biochemical Journal. 1999;337(Pt 3):537-41. PMCID: PMC1220007. PMID: 9895299.

6. **kato-2011-fibronectin**: Kato A, Okamoto O, Ishikawa K, Sumiyoshi H, Matsuo N, Yoshioka H, Nomizu M, Shimada T, Fujiwara S. Dermatopontin interacts with fibronectin, promotes fibronectin fibril formation, and enhances cell adhesion. Journal of Biological Chemistry. 2011;286(17):14861-14869. DOI: 10.1074/jbc.M110.179762. PMCID: PMC3083196. PMID: 21388961.

7. **krishnaswamy-2014-wounds**: Krishnaswamy VR, Manikandan M, Munirajan AK, Vijayaraghavan D, Korrapati PS. Expression and integrity of dermatopontin in chronic cutaneous wounds: a crucial factor in impaired wound healing. Cell and Tissue Research. 2014;358(3):833-41. DOI: 10.1007/s00441-014-2000-z. PMID: 25260909.

8. **okamoto-2010-keratinocyte**: Okamoto O, Hozumi K, Katagiri F, Takahashi N, Sumiyoshi H, Matsuo N, Yoshioka H, Nomizu M, Fujiwara S. Dermatopontin promotes epidermal keratinocyte adhesion via alpha3beta1 integrin and a proteoglycan receptor. Biochemistry. 2010;49(1):147-55. DOI: 10.1021/bi901066f. PMID: 19928997.

9. **kuroda-1999-fibrosis**: Kuroda K, Okamoto O, Shinkai H. Dermatopontin expression is decreased in hypertrophic scar and systemic sclerosis skin fibroblasts and is regulated by transforming growth factor-beta1, interleukin-4, and matrix collagen. Journal of Investigative Dermatology. 1999;112(5):706-10. DOI: 10.1046/j.1523-1747.1999.00563.x. PMID: 10233760.

10. **kim-2019-myogenesis**: Kim T, Ahmad K, Shaikh S, Jan AT, Seo MG, Lee EJ, Choi I. Dermatopontin in Skeletal Muscle Extracellular Matrix Regulates Myogenesis. Cells. 2019;8(4):332. DOI: 10.3390/cells8040332. PMCID: PMC6523808. PMID: 30970550.

11. **liu-2013-cardiac**: Liu X, Meng L, Shi Q, Liu S, Cui C, Hu S, Wei Y. Dermatopontin promotes adhesion, spreading and migration of cardiac fibroblasts in vitro. Matrix Biology. 2013;32(1):23-31. DOI: 10.1016/j.matbio.2012.11.014. PMID: 23262218.

12. **takemoto-2002-infarct**: Takemoto S, Murakami T, Kusachi S, Iwabu A, Hirohata S, Nakamura K, Sezaki S, Hayashi J, Suezawa C, Ninomiya Y, Tsuji T. Increased expression of dermatopontin mRNA in the infarct zone of experimentally induced myocardial infarction in rats: comparison with decorin and type I collagen mRNAs. Basic Research in Cardiology. 2002;97(6):461-468. DOI: 10.1007/s00395-002-0371-x. PMID: 12395208.

13. **jensen-2022-collagen-binding**: Jensen MM, Bonna A, Frederiksen SJ, Hamaia SW, Højrup P, Farndale RW, Karring H. Tyrosine-sulfated dermatopontin shares multiple binding sites and recognition determinants on triple-helical collagens with proteins implicated in cell adhesion and collagen folding, fibrillogenesis, cross-linking, and degradation. Biochimica et Biophysica Acta - Proteins and Proteomics. 2022;1870(5):140771. DOI: 10.1016/j.bbapap.2022.140771. PMID: 35306228.

14. **cooper-2006-cornea**: Cooper LJ, Bentley AJ, Nieduszynski IA, Talabani S, Thomson A, Utani A, Shinkai H, Fullwood NJ, Brown GM. The role of dermatopontin in the stromal organization of the cornea. Investigative Ophthalmology & Visual Science. 2006;47(8):3303-10. DOI: 10.1167/iovs.05-1426. PMCID: PMC1868961. PMID: 16877395.

15. **fu-2014-hcc**: Fu Y, Feng MX, Yu J, Ma MZ, Liu XJ, Li J, Yang XM, Wang YH, Zhang YL, Ao JP, Xue F, Qin W, Gu J, Xia Q, Zhang ZG. DNA methylation-mediated silencing of matricellular protein dermatopontin promotes hepatocellular carcinoma metastasis by α3β1 integrin-Rho GTPase signaling. Oncotarget. 2014;5(16):6701-15. DOI: 10.18632/oncotarget.2239. PMCID: PMC4196157. PMID: 25149533.

16. **sarashina-2006-evolution**: Sarashina I, Yamaguchi H, Haga T, Iijima M, Chiba S, Endo K. Molecular evolution and functionally important structures of molluscan Dermatopontin: implications for the origins of molluscan shell matrix proteins. Journal of Molecular Evolution. 2006;62(3):307-18. DOI: 10.1007/s00239-005-0095-2. PMID: 16474978.

17. **krishnaswamy-2014-reepithelialization**: Krishnaswamy VR, Korrapati PS. Role of dermatopontin in re-epithelialization: implications on keratinocyte migration and proliferation. Scientific Reports. 2014;4:7385. DOI: 10.1038/srep07385. PMCID: PMC4260223. PMID: 25486882.

18. **unamuno-2020-adipokine**: Unamuno X, Gómez-Ambrosi J, Ramírez B, Rodríguez A, Becerril S, Valentí V, Moncada R, Silva C, Salvador J, Frühbeck G, Catalán V. Dermatopontin, A Novel Adipokine Promoting Adipose Tissue Extracellular Matrix Remodelling and Inflammation in Obesity. Journal of Clinical Medicine. 2020;9(4):1069. DOI: 10.3390/jcm9041069. PMCID: PMC7230369. PMID: 32283761.

19. **xu-2024-cholangiocarcinoma**: Xu P, Li S, Liu K, Fan R, Liu F, Zhang H, Liu D, Shen D. Downregulation of dermatopontin in cholangiocarcinoma cells suppresses CCL19 secretion of macrophages and immune infiltration. Journal of Cancer Research and Clinical Oncology. 2024;150(2):66. DOI: 10.1007/s00432-023-05532-1. PMCID: PMC10834663. PMID: 38300311.


## Citations

1. cooper-2006-cornea-abstract.md
2. cronshaw-1993-discovery-abstract.md
3. forbes-1994-tramp-abstract.md
4. fu-2014-hcc-abstract.md
5. jensen-2022-collagen-binding-abstract.md
6. kato-2011-fibronectin-abstract.md
7. kim-2019-myogenesis-abstract.md
8. krishnaswamy-2014-reepithelialization-abstract.md
9. krishnaswamy-2014-wounds-abstract.md
10. kuroda-1999-fibrosis-abstract.md
11. liu-2013-cardiac-abstract.md
12. okamoto-1999-tgfb-abstract.md
13. okamoto-2006-review-abstract.md
14. okamoto-2010-keratinocyte-abstract.md
15. sarashina-2006-evolution-abstract.md
16. takeda-2002-knockout-abstract.md
17. takemoto-2002-infarct-abstract.md
18. unamuno-2020-adipokine-abstract.md
19. xu-2024-cholangiocarcinoma-abstract.md