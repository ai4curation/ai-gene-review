---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-22T22:17:36.764713'
end_time: '2026-01-22T22:30:57.898232'
duration_seconds: 801.13
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: MAP7D2
  gene_symbol: MAP7D2
  uniprot_accession: Q96T17
  protein_description: 'RecName: Full=MAP7 domain-containing protein 2;'
  gene_info: Name=MAP7D2;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the MAP7 family. .
  protein_domains: MAP7_domain-containing. (IPR051483); MAP7_fam. (IPR008604); MAP7
    (PF05672)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 12
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q96T17
- **Protein Description:** RecName: Full=MAP7 domain-containing protein 2;
- **Gene Information:** Name=MAP7D2;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the MAP7 family. .
- **Key Domains:** MAP7_domain-containing. (IPR051483); MAP7_fam. (IPR008604); MAP7 (PF05672)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "MAP7D2" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'MAP7D2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **MAP7D2** (gene ID: MAP7D2, UniProt: Q96T17) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# MAP7D2: A Microtubule-Associated Protein Regulating Kinesin-1-Mediated Axonal Transport

## Introduction

MAP7D2 (MAP7 domain-containing protein 2) is a microtubule-associated protein encoded by the MAP7D2 gene located on chromosome Xp22.12 in humans (UniProt: Q96T17). The protein belongs to the MAP7 family, which in mammals comprises four members: MAP7 (also known as ensconsin or E-MAP-115), MAP7D1, MAP7D2, and MAP7D3 [hooikaas-2019-map7-kinesin-abstract]. Unlike traditional microtubule-associated proteins such as tau or MAP2, the MAP7 family members are distinguished by their unique ability to interact with both microtubules and the motor protein kinesin-1, functioning as essential cofactors for kinesin-1-driven intracellular transport [hooikaas-2019-map7-kinesin-summary].

MAP7D2 serves a dual function: it directly stabilizes microtubules through physical binding, and it acts as a critical cofactor for kinesin-1-mediated cargo transport [kikuchi-2022-map7d2-stabilization-abstract]. The protein is predominantly expressed in the brain and testis, with particularly high expression in the glomerular layer of the olfactory bulb and Sertoli cells [kikuchi-2022-map7d2-stabilization-summary]. In neurons, MAP7D2 exhibits a distinctive subcellular localization pattern, concentrating at the proximal axon where it overlaps with the axon initial segment (AIS), a critical region for controlling cargo entry into the axon [pan-2019-map7d2-proximal-axon-abstract].

## Protein Structure and Domain Organization

Human MAP7D2 is a 773-amino acid protein (approximately 82 kDa) sharing the characteristic structural organization of MAP7 family members [pan-2019-map7d2-proximal-axon-summary]. The protein contains two principal functional domains connected by an unstructured linker region. The N-terminal domain harbors a conserved coiled-coil motif that mediates direct binding to microtubules, while the C-terminal domain contains a second coiled-coil region responsible for interaction with the stalk region of kinesin-1 heavy chains [hooikaas-2019-map7-kinesin-abstract].

Structure-function studies have demonstrated that the N-terminal microtubule-binding domain (approximately amino acids 151-387) is sufficient for directing MAP7D2 to its characteristic subcellular localization at the proximal axon [pan-2019-map7d2-proximal-axon-summary]. Truncation constructs lacking this region show diffuse cytoplasmic distribution, while the isolated N-terminal fragment recapitulates the proximal axon accumulation pattern [pan-2019-map7d2-proximal-axon-summary]. The C-terminal kinesin-binding domain, when expressed alone, distributes diffusely throughout the neuron and accumulates at axon tips, likely reflecting transport by kinesin-1 [pan-2019-map7d2-proximal-axon-summary].

While no high-resolution structure of MAP7D2 itself has been determined, structural insights from the founding family member MAP7 provide relevant context. Cryo-electron microscopy studies revealed that the MAP7 microtubule-binding domain (MTBD) binds microtubules as an extended alpha-helix positioned between the protofilament ridge and the site of lateral contact [ferro-2022-map7-structure-abstract]. This binding site partially overlaps with the kinesin-1 binding site on microtubules, leading to complex regulatory consequences [ferro-2022-map7-structure-abstract].

## Molecular Functions

### Microtubule Binding and Stabilization

The primary molecular function of MAP7D2 is direct binding to microtubules, which it accomplishes through its N-terminal region. Using recombinant rat MAP7D2 protein, Kikuchi and colleagues demonstrated that MAP7D2 binds to microtubules through its N-terminal half and facilitates microtubule stabilization in vitro [kikuchi-2022-map7d2-stabilization-abstract]. Quantitative analysis using microtubule co-sedimentation assays determined that MAP7D2 binds microtubules with a dissociation constant (Kd) of approximately 6 × 10⁻⁷ M (600 nM), which is comparable to the binding affinities of well-characterized MAPs such as tau and CLIP-170 [kikuchi-2022-map7d2-stabilization-abstract]. The stoichiometry of MAP7D2 binding to tubulin was calculated to be one MAP7D2 molecule per approximately 10 tubulin α/β heterodimers, a ratio also comparable to that observed for MAP7 [kikuchi-2022-map7d2-stabilization-abstract].

Importantly, MAP7D2 employs a distinct mechanism of microtubule stabilization compared to its paralog MAP7D1. When MAP7D2 is depleted from cells, resistance to the microtubule-destabilizing agent nocodazole decreases without affecting levels of acetylated or detyrosinated tubulin, which are markers of stable microtubule populations [kikuchi-2022-map7d2-stabilization-summary]. This finding indicates that MAP7D2 stabilizes microtubules via direct physical binding rather than by promoting post-translational modifications. In contrast, MAP7D1 is required for maintaining acetylated stable microtubules, demonstrating that these paralogs have evolved mechanistically distinct approaches to microtubule regulation [kikuchi-2022-map7d2-stabilization-abstract].

### Kinesin-1 Recruitment and Activation

Beyond microtubule stabilization, MAP7D2 functions as a critical cofactor for kinesin-1 motor function. Biochemical studies have demonstrated that MAP7D2 interacts with all three mammalian kinesin-1 family members (KIF5A, KIF5B, and KIF5C) through pull-down experiments and mass spectrometry [pan-2019-map7d2-proximal-axon-abstract]. Notably, MAP7D2 does not interact with kinesin-3 motors, indicating specificity in its motor regulation [pan-2019-map7d2-proximal-axon-summary].

The mechanism by which MAP7 family proteins activate kinesin-1 has been elucidated through extensive in vitro reconstitution studies. These proteins enhance both the microtubule landing rate and processivity of kinesin-1 motors through a dual mechanism [hooikaas-2019-map7-kinesin-summary]. First, they directly recruit kinesin-1 to microtubules through their N-terminal microtubule-binding domain and unstructured linker region. Second, they exert an allosteric activation effect through their C-terminal kinesin-binding domain [hooikaas-2019-map7-kinesin-abstract]. The C-terminal domain alone can efficiently increase kinesin-1 landing rates despite having minimal microtubule affinity, demonstrating that the activation mechanism involves more than simple tethering [hooikaas-2019-map7-kinesin-summary].

## Subcellular Localization and Spatial Function

### Concentration at the Proximal Axon

A distinguishing feature of MAP7D2 is its specific localization to the proximal axon in neurons, a pattern that differentiates it from other MAP7 family members. While MAP7 and MAP7D1 are predominantly found in the somatodendritic compartment, MAP7D2 and MAP7D3 concentrate at the proximal axon where they overlap with AIS markers including TRIM46 and Ankyrin-G [pan-2019-map7d2-proximal-axon-abstract].

The proximal axon localization of MAP7D2 depends critically on TRIM46, a microtubule-bundling protein that organizes parallel microtubule arrays at the AIS. When TRIM46 is depleted, MAP7D2 fails to accumulate at the proximal axon [pan-2019-map7d2-proximal-axon-summary]. This dependency suggests that MAP7D2 may recognize specific modifications or conformational changes in the microtubule lattice induced by TRIM46-mediated bundling, rather than simply binding to any available microtubule [pan-2019-map7d2-proximal-axon-summary].

### Centrosomal and Cytoplasmic Distribution

In addition to its axonal localization, MAP7D2 prominently localizes to the centrosome and distributes partially along cytoplasmic microtubules in neuronal cells [kikuchi-2022-map7d2-stabilization-abstract]. This centrosomal enrichment suggests potential roles in microtubule nucleation or organization emanating from this microtubule-organizing center. The protein accumulates at sites of active microtubule bundling during cell division and neurite formation, consistent with its function as a microtubule-binding and stabilizing protein [kikuchi-2022-map7d2-stabilization-summary].

## Biological Processes and Pathways

### Regulation of Axonal Cargo Transport

The strategic localization of MAP7D2 at the proximal axon positions it to regulate a critical decision point in neuronal cargo sorting. The axon initial segment serves as a gateway controlling which cargoes enter the axon versus remaining in the somatodendritic compartment. MAP7D2 functions at this location to locally promote kinesin-1-mediated cargo entry into the axon [pan-2019-map7d2-proximal-axon-abstract].

Depletion of MAP7D2 significantly reduces axonal entry of kinesin-1-dependent cargoes, including mitochondria, lysosomes, and endoplasmic reticulum [pan-2019-map7d2-proximal-axon-summary]. This transport defect is specific to kinesin-1-dependent processes, as Rab3-positive vesicles that depend on kinesin-3 for transport are unaffected by MAP7D2 loss [pan-2019-map7d2-proximal-axon-summary]. The proposed model suggests that MAP7D2 acts as a spatially restricted activator of kinesin-1, enhancing motor recruitment and activity specifically at the proximal axon to facilitate cargo transition from the soma into the axonal compartment.

### Control of Cell Motility and Neurite Outgrowth

Loss-of-function studies have revealed that MAP7D2 plays important roles in regulating cell migration and neurite extension. Unexpectedly, MAP7D2 depletion or knockout leads to increased rates of random cell migration and neurite outgrowth [kikuchi-2022-map7d2-stabilization-summary]. This seemingly paradoxical result is interpreted as reflecting a disturbance in the balance between microtubule stabilization and destabilization, with excessive dynamicity promoting these processes [kikuchi-2022-map7d2-stabilization-summary].

In developing neurons, MAP7D2 depletion causes reduced axon branching and defects in axon formation and outgrowth [pan-2019-map7d2-proximal-axon-abstract]. These phenotypes can be rescued by re-expression of MAP7D2 but not by MAP7D1, despite the two proteins sharing significant sequence homology [pan-2019-map7d2-proximal-axon-summary]. This specificity likely reflects their distinct subcellular localizations, with MAP7D1 unable to compensate for MAP7D2 function at the proximal axon.

### Neuronal Migration

During brain development, MAP7D2 contributes to proper neuronal migration. Depletion of MAP7D2 results in migration defects in embryonic brain slices, indicating that the protein's function in regulating microtubule stability and kinesin-1-mediated transport is important for the cellular motility required during cortical development [pan-2019-map7d2-proximal-axon-abstract].

## Tissue Expression and Physiological Context

MAP7D2 exhibits a highly restricted tissue expression pattern, being detected primarily in brain and testis, with brain expression being more abundant [kikuchi-2022-map7d2-stabilization-abstract]. This pattern contrasts with MAP7, which shows more ubiquitous expression. Within the brain, MAP7D2 is highly expressed in the glomerular layer of the olfactory bulb, a region characterized by dense accumulation of axons from olfactory sensory neurons [kikuchi-2022-map7d2-stabilization-summary]. This localization pattern is consistent with the protein's function in axonal biology.

In the testis, MAP7D2 is expressed specifically in Sertoli cells, the somatic support cells of the seminiferous epithelium that nurture developing germ cells [kikuchi-2022-map7d2-stabilization-summary]. The functional significance of MAP7D2 in Sertoli cells has not been extensively characterized, but given the importance of microtubule-based transport in these cells for supporting spermatogenesis, MAP7D2 likely contributes to cargo transport processes within this specialized cell type.

At the cellular level in neurons, MAP7D2 shows expression enriched in hippocampal neurons, where it localizes specifically to the proximal axon through its N-terminal microtubule-binding domain [pan-2019-map7d2-proximal-axon-summary]. The Human Protein Atlas reports cytoplasmic expression in neurons and cells of the seminiferous duct testis, with some nuclear/nucleoplasmic localization also observed.

## Relationship to MAP7 Family Members

Understanding MAP7D2 requires appreciation of its position within the larger MAP7 protein family. All four mammalian family members share the conserved domain architecture with N-terminal microtubule-binding and C-terminal kinesin-binding regions [hooikaas-2019-map7-kinesin-abstract]. They all function as positive regulators of kinesin-1, in contrast to classical neuronal MAPs such as tau and MAP2 that inhibit kinesin-1-driven motility [hooikaas-2019-map7-kinesin-summary].

Despite these shared features, the family members exhibit important functional specialization. MAP7 is immobile on microtubules and requires high local density to affect kinesin-1 processivity, while MAP7D3 has higher kinesin-1 affinity but lower microtubule affinity and can be co-transported with motors [hooikaas-2019-map7-kinesin-summary]. The subcellular localization patterns also differ markedly: MAP7 and MAP7D1 localize to the somatodendritic compartment, while MAP7D2 and MAP7D3 concentrate at the proximal axon [pan-2019-map7d2-proximal-axon-abstract].

In terms of microtubule stabilization mechanisms, MAP7D2 and MAP7D1 employ distinct approaches despite both promoting stability. MAP7D2 operates through direct binding to the microtubule lattice, while MAP7D1 maintains stability through preserving acetylated tubulin populations [kikuchi-2022-map7d2-stabilization-summary]. This mechanistic diversity may allow for nuanced control of microtubule dynamics in different cellular contexts.

## Evolutionary Conservation

The MAP7 family represents an evolutionarily conserved class of kinesin-1 regulators. In Drosophila, a single homolog called ensconsin (also known as E-MAP-115) performs the functions that are distributed among four paralogs in mammals [hooikaas-2019-map7-kinesin-abstract]. Studies of Drosophila ensconsin have been instrumental in establishing the essential role of this protein family in kinesin-1-dependent processes.

Ensconsin is required for all known kinesin-1-dependent processes in Drosophila, including spindle positioning, centrosome separation, and polarized cargo transport in oocytes [metivier-2019-ensconsin-abstract]. The fly protein shares the same domain architecture as mammalian MAP7D2, with an N-terminal microtubule-binding domain and a C-terminal kinesin-binding domain. Mechanistic studies in Drosophila revealed that the kinesin-binding domain alone can stimulate kinesin-1 targeting to microtubules both in vivo and in vitro, while full-length ensconsin provides optimal motor recruitment through dual regulation involving both domains [metivier-2019-ensconsin-abstract].

The evolutionary expansion from a single ancestral ensconsin gene in invertebrates to four paralogs in mammals (MAP7, MAP7D1, MAP7D2, MAP7D3) appears to have enabled functional diversification. This diversification is manifest in the distinct subcellular localization patterns (somatodendritic versus axonal) and different mechanisms of microtubule stabilization (direct binding versus acetylation maintenance) exhibited by the mammalian paralogs. The conservation of the core biochemical functions—microtubule binding and kinesin-1 activation—across hundreds of millions of years of evolution underscores the fundamental importance of this regulatory mechanism in cellular biology.

## Gene Ontology Annotations

The functional annotations for MAP7D2 in the Gene Ontology database reflect its characterized molecular activities and biological roles. In terms of Molecular Function, MAP7D2 is annotated with microtubule binding (GO:0008017) and kinesin binding, consistent with its demonstrated ability to directly interact with both microtubules and kinesin-1 motor proteins. The protein is also annotated with structural molecule activity, reflecting its role in stabilizing the microtubule cytoskeleton.

For Biological Process annotations, MAP7D2 is associated with microtubule cytoskeleton organization (GO:0000226) and axon development (GO:0061564). These annotations capture its roles in maintaining microtubule stability and regulating axonal cargo transport during neuronal development.

Cellular Component annotations place MAP7D2 in the microtubule cytoskeleton (GO:0015630), axon (GO:0030424), and centrosome (GO:0005813), consistent with experimental observations of its subcellular localization in neuronal cells.

## Disease Associations and Cancer Biology

While no Mendelian diseases have been directly attributed to MAP7D2 mutations, emerging evidence links the protein to cancer biology. Recent work has identified MAP7D2 as significantly upregulated in microsatellite stable (MSS) colorectal cancer, where it adversely correlates with the presence of antitumor T lymphocytes [wu-2023-map7d2-colorectal-cancer-abstract].

Mechanistically, MAP7D2 binds to MYH9, a non-muscle myosin II heavy chain, and protects it from ubiquitin-mediated degradation [wu-2023-map7d2-colorectal-cancer-abstract]. This MAP7D2-mediated MYH9 stabilization reduces secretion of HMGB1, a damage-associated molecular pattern that normally acts as a chemokine to recruit T lymphocytes into the tumor microenvironment. Consequently, elevated MAP7D2 expression promotes an immunosuppressive microenvironment by reducing CD8+ cytotoxic T lymphocyte infiltration [wu-2023-map7d2-colorectal-cancer-abstract].

From a therapeutic perspective, knockdown of MAP7D2 in colorectal cancer models significantly increases CD8+ T cell infiltration, inhibits tumor progression, and improves the efficacy of immune checkpoint inhibitors such as anti-PD-1 antibodies [wu-2023-map7d2-colorectal-cancer-abstract]. This work suggests that MAP7D2 may represent a potential therapeutic target for improving immunotherapy responses in MSS colorectal cancer, a tumor type that typically responds poorly to checkpoint blockade.

The Human Protein Atlas classifies MAP7D2 as a prognostic marker in bladder urothelial carcinoma and pancreatic adenocarcinoma, though the protein shows relatively low cancer specificity overall. Database associations also link MAP7D2 to esophageal adenosquamous carcinoma, though detailed mechanistic studies in these cancer types are lacking.

## Open Questions

Several important questions remain regarding MAP7D2 biology:

1. **Structural basis of MAP7D2 function**: While structural studies of MAP7 have provided insights into microtubule binding and kinesin-1 regulation, high-resolution structures of MAP7D2 specifically would clarify whether the family members employ identical or distinct molecular mechanisms.

2. **TRIM46-dependent localization mechanism**: The molecular basis by which MAP7D2 recognizes TRIM46-organized microtubule bundles at the AIS remains unclear. Whether this involves direct TRIM46 interaction, recognition of specific tubulin post-translational modifications, or sensing of microtubule geometry warrants investigation.

3. **Testis function**: The specific role of MAP7D2 in Sertoli cells is essentially uncharacterized. Given the importance of microtubule-based transport in supporting spermatogenesis, understanding MAP7D2 function in this context could reveal important reproductive biology.

4. **Centrosomal function**: The prominent centrosomal localization of MAP7D2 suggests potential roles beyond axonal transport, possibly in microtubule nucleation or organization. These potential functions remain unexplored.

5. **Disease relevance beyond cancer**: Whether MAP7D2 dysfunction contributes to neurological or neurodevelopmental disorders, given its critical roles in axonal biology, merits systematic investigation.

6. **Regulation of MAP7D2**: The mechanisms controlling MAP7D2 expression, localization, and activity are poorly understood. Post-translational modifications or binding partners that modulate its function have not been characterized.

7. **Functional redundancy vs. specificity**: While MAP7 family members show functional redundancy in some assays, the distinct localization patterns and mechanisms suggest specialized roles that warrant further delineation.

## References

1. **[kikuchi-2022-map7d2-stabilization]** Kikuchi K, Sakamoto Y, Uezu A, Yamamoto H, Ishiguro KI, Shimamura K, Saito T, Hisanaga SI, Nakanishi H. Map7D2 and Map7D1 facilitate microtubule stabilization through distinct mechanisms in neuronal cells. Life Sci Alliance. 2022 Apr 25;5(8):e202201390. PMID: 35470240; PMCID: PMC9039348; DOI: 10.26508/lsa.202201390. URL: https://www.life-science-alliance.org/content/5/8/e202201390

2. **[pan-2019-map7d2-proximal-axon]** Pan X, Cao Y, Stucchi R, Hooikaas PJ, Portegies S, Will L, Martin M, Akhmanova A, Harterink M, Hoogenraad CC. MAP7D2 Localizes to the Proximal Axon and Locally Promotes Kinesin-1-Mediated Cargo Transport into the Axon. Cell Rep. 2019 Feb 19;26(8):1988-1999.e6. PMID: 30784582; PMCID: PMC6381606; DOI: 10.1016/j.celrep.2019.01.084. URL: https://www.sciencedirect.com/science/article/pii/S2211124719301202

3. **[hooikaas-2019-map7-kinesin]** Hooikaas PJ, Martin M, Mühlethaler T, Kuijntjes GJ, Peeters CAE, Katrukha EA, Ferrari L, Stucchi R, Verhagen DGF, van Riel WE, Grigoriev I, Altelaar AFM, Hoogenraad CC, Rüdiger SGD, Steinmetz MO, Kapitein LC, Akhmanova A. MAP7 family proteins regulate kinesin-1 recruitment and activation. J Cell Biol. 2019 Apr 1;218(4):1298-1318. PMID: 30770434; PMCID: PMC6446838; DOI: 10.1083/jcb.201808065. URL: https://rupress.org/jcb/article/218/4/1298/61853/MAP7-family-proteins-regulate-kinesin-1

4. **[ferro-2022-map7-structure]** Ferro LS, Fang Q, Eshun-Wilson L, Fernandes J, et al. Structural and functional insight into regulation of kinesin-1 by microtubule-associated protein MAP7. Science. 2022 Jan 21;375(6578):326-331. PMID: 35050657; PMCID: PMC8985661; DOI: 10.1126/science.abf6154. URL: https://www.science.org/doi/10.1126/science.abf6154

5. **[tymanskyj-2018-map7-axon]** Tymanskyj SR, Yang BH, Verhey KJ, Ma L. MAP7 regulates axon morphogenesis by recruiting kinesin-1 to microtubules and modulating organelle transport. eLife. 2018;7:e36374. PMID: 30015618; PMCID: PMC6133550; DOI: 10.7554/eLife.36374. URL: https://elifesciences.org/articles/36374

6. **[wu-2023-map7d2-colorectal-cancer]** Wu Q, Yue X, Liu H, Zhu Y, Ke H, Yang X, Yin S, Li Z, Zhang Y, Hu T, Lan P, Wu X. MAP7D2 reduces CD8+ cytotoxic T lymphocyte infiltration through MYH9-HMGB1 axis in colorectal cancer. Mol Ther. 2023 Jan 4;31(1):90-104. PMID: 36081350; PMCID: PMC9840115; DOI: 10.1016/j.ymthe.2022.09.001. URL: https://www.cell.com/molecular-therapy-family/molecular-therapy/fulltext/S1525-0016(22)00544-1

7. **[metivier-2019-ensconsin]** Métivier M, Monroy BY, Gallaud E, et al. Dual control of Kinesin-1 recruitment to microtubules by Ensconsin in Drosophila neuroblasts and oocytes. Development. 2019 Apr 17;146(8):dev171579. PMID: 30936181; PMCID: PMC6503980; DOI: 10.1242/dev.171579. URL: https://pubmed.ncbi.nlm.nih.gov/30936181/

8. **[omim-301121]** OMIM Entry 301121: MAP7 DOMAIN-CONTAINING PROTEIN 2; MAP7D2. URL: https://omim.org/entry/301121

9. **[uniprot-q96t17]** UniProt Entry Q96T17: MAP7 domain-containing protein 2 - Homo sapiens (Human). URL: https://www.uniprot.org/uniprotkb/Q96T17/entry

10. **[human-protein-atlas-map7d2]** Human Protein Atlas: MAP7D2 protein expression summary. URL: https://www.proteinatlas.org/ENSG00000184368-MAP7D2


## Citations

1. ferro-2022-map7-structure-abstract.md
2. ferro-2022-map7-structure-summary.md
3. hooikaas-2019-map7-kinesin-abstract.md
4. hooikaas-2019-map7-kinesin-summary.md
5. kikuchi-2022-map7d2-stabilization-abstract.md
6. kikuchi-2022-map7d2-stabilization-summary.md
7. metivier-2019-ensconsin-abstract.md
8. pan-2019-map7d2-proximal-axon-abstract.md
9. pan-2019-map7d2-proximal-axon-summary.md
10. tymanskyj-2018-map7-axon-abstract.md
11. wu-2023-map7d2-colorectal-cancer-abstract.md
12. wu-2023-map7d2-colorectal-cancer-summary.md