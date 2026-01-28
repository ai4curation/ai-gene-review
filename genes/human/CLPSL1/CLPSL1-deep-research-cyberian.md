---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-24T01:47:36.799591'
end_time: '2026-01-24T02:01:03.612154'
duration_seconds: 806.81
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: CLPSL1
  gene_symbol: CLPSL1
  uniprot_accession: A2RUU4
  protein_description: 'RecName: Full=Colipase-like protein 1; Flags: Precursor;'
  gene_info: Name=CLPSL1; Synonyms=C6orf127;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the colipase family. {ECO:0000255|PROSITE-
  protein_domains: Colipase. (IPR001981)
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
- **UniProt Accession:** A2RUU4
- **Protein Description:** RecName: Full=Colipase-like protein 1; Flags: Precursor;
- **Gene Information:** Name=CLPSL1; Synonyms=C6orf127;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the colipase family. {ECO:0000255|PROSITE-
- **Key Domains:** Colipase. (IPR001981)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CLPSL1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CLPSL1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CLPSL1** (gene ID: CLPSL1, UniProt: A2RUU4) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Research Report: CLPSL1 (Colipase-like Protein 1)

## Introduction and Summary

CLPSL1 (Colipase-like protein 1), also known as C6orf127 or ESP32, is a protein-coding gene in humans located on chromosome 6p21.31 (UniProt accession A2RUU4). The protein belongs to the colipase family and contains a colipase domain (InterPro IPR001981), suggesting structural and potentially functional relationships to the well-characterized pancreatic colipase (CLPS). However, unlike the canonical colipase which serves as an essential cofactor for pancreatic lipase in dietary fat digestion, CLPSL1 appears to have evolved a specialized function in the male reproductive tract, with predominant expression in the epididymis.

Direct literature on CLPSL1 is extremely limited. According to PubMed searches, only one publication directly mentions CLPSL1 by name [li-2020-colorectal-biomarker-abstract], and this study identifies it merely as a biomarker in colorectal cancer without investigating its biological function. Therefore, understanding of CLPSL1 must be derived primarily from: (1) database annotations and expression data, (2) studies of its paralog CLPSL2, which shares structural features and epididymal expression, and (3) knowledge of the canonical colipase CLPS for comparative context.

Based on expression data from the Human Protein Atlas, CLPSL1 is classified as "group enriched" in the epididymis (572.6 nTPM) and pancreas (165.3 nTPM), with highest single-cell expression in epididymal principal cells (1,181.2 nCPM) and pancreatic acinar cells (347.3 nCPM) [human-protein-atlas-clpsl1]. The protein is predicted to be secreted and is annotated as "secreted in male reproductive system" with cytoplasmic expression detected by immunohistochemistry in epididymis tissue. These expression patterns suggest that CLPSL1, like its paralog CLPSL2, may function in sperm maturation during epididymal transit.

## The Colipase Protein Family

Colipase (CLPS) is a small protein (~10 kDa) that serves as an essential cofactor for pancreatic triglyceride lipase (PTL), enabling efficient dietary fat hydrolysis in the intestine. Structurally, colipase is characterized by a relatively flat architecture (approximately 25×30×35 Å) stabilized by five conserved disulfide bonds and limited secondary structure [vantilbeurgh-1999-colipase-structure-abstract]. The protein binds to the C-terminal, non-catalytic domain of pancreatic lipase, thereby stabilizing the enzyme's active conformation and creating a large hydrophobic binding surface that anchors the lipase-colipase complex at lipid-water interfaces [lowe-2002-triglyceride-lipases-abstract].

In the intestinal lumen, bile acids inhibit pancreatic lipase activity by displacing the enzyme from lipid droplet surfaces. Colipase counteracts this inhibition by acting as a molecular bridge: it binds to both the lipase and bile acids, anchoring the enzyme to the droplet surface and preventing its displacement. This functional relationship is critical for efficient dietary triglyceride digestion [kumar-2021-pancreatic-lipase-inhibitors-abstract].

Colipase is secreted as a precursor protein called procolipase, which is activated in the intestinal lumen by trypsin cleavage. This cleavage releases a pentapeptide from the N-terminus called enterostatin, which has independent signaling functions in regulating fat intake [erlanson-albertsson-1997-enterostatin-abstract]. The procolipase gene is upregulated by high-fat diets, and enterostatin acts as an anorectic signal that selectively reduces fat consumption.

The colipase domain (InterPro IPR001981) has been identified in several proteins beyond the canonical pancreatic colipase, including the colipase-like proteins CLPSL1 and CLPSL2 in humans. Interestingly, structural analogies have been recognized between colipase and domains in developmental proteins (such as Dickkopf), as well as domains in lipoxygenases and alpha-toxin that mediate membrane interactions [vantilbeurgh-1999-colipase-structure-abstract].

## Expression Patterns and Tissue Distribution

According to the Human Protein Atlas, CLPSL1 shows a distinctive tissue expression pattern that differs markedly from the canonical colipase CLPS, which is highly expressed in the pancreas for digestive function. CLPSL1 expression is highest in the epididymis (572.6 nTPM), with secondary expression in the pancreas (165.3 nTPM) and lower expression in salivary gland (1.4 nTPM), seminal vesicle (2.2 nTPM), and breast tissue (4.0 nTPM) [human-protein-atlas-clpsl1].

At the single-cell level, CLPSL1 is most highly expressed in epididymal principal cells (1,181.2 nCPM), which are the predominant epithelial cell type lining the epididymal duct and are responsible for secreting proteins into the luminal fluid that bathes maturing spermatozoa. CLPSL1 is also expressed in epididymal clear cells and basal cells, as well as pancreatic acinar cells (347.3 nCPM).

The tissue expression cluster for CLPSL1 is annotated as "Epididymis - Male reproductive secretion (mainly)," indicating that its primary biological role is likely related to male reproductive function rather than digestive lipase activation. The protein is predicted to be secreted, consistent with a role in the epididymal luminal environment where sperm maturation occurs.

Interestingly, CLPSL1 also shows some expression in the brain, particularly in the cerebral cortex (5.5 nTPM), hippocampal formation (4.0 nTPM), and other regions, with expression classified in the brain cluster "Neurons - Mixed function (mainly)" [human-protein-atlas-clpsl1]. The functional significance of this neural expression, if any, is unknown.

## Functional Inferences from the Paralog CLPSL2

Given the scarcity of direct functional studies on CLPSL1, the most relevant functional insights come from studies of its paralog CLPSL2 (Colipase-like 2). CLPSL2 is also exclusively expressed in the epididymis, though specifically in the caput (head) region, whereas CLPSL1 is reported to be expressed in the corpus (body) region [genecards-clpsl1]. Both proteins belong to the colipase family and share structural features, suggesting potentially related or complementary functions.

According to PubMed, Lu et al. (2018) characterized CLPSL2 as a novel epididymis-specific secretory protein that is conserved across mammals. The protein is secreted into the epididymal lumen where it binds to the acrosome region and principal piece of the spermatozoa tail [lu-2018-clpsl2-epididymis-abstract]. Importantly, the study found that although CLPSL2 has the highest sequence identity with pancreatic colipase (CLPS), it lacks the conserved amino acid residues that are essential for lipase interaction. Consequently, recombinant CLPSL2 protein did not possess the classical colipase function of promoting lipase-mediated hydrolysis of glycerol trioleate. However, sequence analysis indicated that CLPSL2 retains the potential to bind lipids [lu-2018-clpsl2-epididymis-abstract].

Using lentivirus-mediated RNAi knockdown in vivo, Lu et al. reported that reduced CLPSL2 expression caused attenuation of sperm motility, suppressed acrosomal reaction, decreased cauda epididymal sperm numbers, and subfertility in mice. Based on these findings, the authors concluded that CLPSL2 is involved in the regulation of sperm motility, acrosomal integrity, and male fertility [lu-2018-clpsl2-epididymis-abstract].

However, these RNAi-based findings were subsequently challenged by Noda et al. (2019), who generated complete CLPSL2 knockout mice using CRISPR/Cas9 gene editing [noda-2019-nine-genes-dispensable-abstract]. Strikingly, the Clpsl2 knockout males showed completely normal fertility, with litter sizes statistically indistinguishable from wild-type controls (9.8 ± 0.8 for controls vs. 9.1 ± 0.5 for Clpsl2 KO; p = 0.20). No apparent differences were observed in epididymal histology or sperm morphology between knockout and control animals. The authors suggested that the discrepancy between the RNAi and knockout results may be due to off-target effects of the RNAi approach [noda-2019-nine-genes-dispensable-abstract].

These findings for CLPSL2 suggest that while colipase-like proteins may bind to sperm and potentially contribute to some aspect of sperm maturation or function, they are not individually essential for male fertility, at least in mice. It remains possible that CLPSL1 and CLPSL2 have redundant functions, and that loss of one can be compensated by the other or by additional mechanisms.

## Subcellular Localization and Secretion

CLPSL1 is predicted to be both a secreted protein and to have intracellular localization, with different isoforms potentially showing different distributions [human-protein-atlas-clpsl1]. The gene produces two protein-coding transcripts, and both secreted and intracellular forms are predicted.

The extracellular/secreted form is annotated as being "secreted in male reproductive system," consistent with a role in the epididymal lumen. Immunohistochemistry shows cytoplasmic expression in the epididymis. Given that epididymal principal cells actively secrete numerous proteins into the luminal fluid that interacts with maturing spermatozoa, CLPSL1 secretion into this compartment would position it to interact with sperm or regulate the luminal microenvironment.

## Gene Ontology Annotations

Gene Ontology (GO) annotations for CLPSL1 include:

**Molecular Function:**
- Enzyme activator activity (GO:0008047)

**Biological Process:**
- Digestion (GO:0007586)
- Lipid catabolic process (GO:0016042)
- Response to food (GO:0032094)

These annotations appear to be inferred from the colipase domain and homology to the canonical colipase rather than from direct experimental evidence. The "enzyme activator activity" annotation reflects the known function of colipase as a cofactor that activates pancreatic lipase. However, as noted from studies of CLPSL2, the colipase-like proteins may lack the specific residues required for lipase activation, so these functional annotations may not accurately reflect CLPSL1's actual biological role [lu-2018-clpsl2-epididymis-abstract].

## Relationship to Cancer Biomarkers

The only published study that directly mentions CLPSL1 is a bioinformatics analysis by Li et al. (2020) that identified a four-mRNA signature associated with lymphatic metastasis for prognosis of colorectal cancer [li-2020-colorectal-biomarker-abstract]. In this study, CLPSL1 was identified along with EPHA8, KRT85, and GABRA3 as independent prognostic indicators for colorectal cancer.

The authors found that 329 mRNAs were upregulated in colorectal cancer tissues with lymph node metastasis, and CLPSL1 was among the genes in this set. However, the study did not investigate the biological function of CLPSL1 in cancer or provide mechanistic insights into why CLPSL1 expression might be associated with metastatic progression. The finding may reflect aberrant expression of tissue-specific genes in cancer cells (ectopic expression) rather than a functional role in tumorigenesis.

According to the Human Protein Atlas cancer expression data, moderate to strong cytoplasmic staining for CLPSL1 has been detected in renal cancer cases, while other cancer types show weak or negative staining [human-protein-atlas-clpsl1].

## Comparative Analysis: CLPSL1 vs. CLPSL2 vs. CLPS

The three members of the colipase family in humans (CLPS, CLPSL1, and CLPSL2) show distinct expression patterns and likely have divergent functions despite their shared domain structure:

| Feature | CLPS (Colipase) | CLPSL1 | CLPSL2 |
|---------|-----------------|--------|--------|
| Primary tissue | Pancreas | Epididymis (corpus) | Epididymis (caput) |
| Known function | Lipase cofactor | Unknown | Unknown |
| Lipase activation | Yes | Likely not | No |
| Essential for fertility | N/A | Unknown | No (in mice) |
| Lipid binding potential | Yes | Predicted | Yes |

This pattern suggests that the colipase-like proteins have been co-opted during evolution from their ancestral role in digestive fat hydrolysis to serve specialized functions in the male reproductive tract. The retention of lipid-binding potential without lipase activation capability suggests that these proteins may interact with membrane lipids or lipid-associated molecules on sperm surfaces.

## Protein-Protein Interactions

According to BioGRID, CLPSL1 has 46 documented interactors and 59 total interactions [biogrid-clpsl1]. These interaction data are likely derived from high-throughput screens rather than targeted studies, and the biological relevance of individual interactions remains to be validated. The nature of these interactions and whether they relate to CLPSL1's function in the reproductive tract is unknown.

## Biological Context: Lipid Metabolism in the Epididymis

The epididymis plays a critical role in post-testicular sperm maturation, providing the microenvironment necessary for spermatozoa to gain progressive motility and fertilization capacity. During transit through the epididymis, the sperm plasma membrane undergoes extensive remodeling, with significant changes in phospholipid composition and cholesterol content [cornwall-2009-epididymis-review]. This membrane remodeling is essential for proper sperm function, as cholesterol removal from the sperm membrane is one of the first steps triggering signal transduction cascades during capacitation.

Several secreted proteins in the epididymis have been shown to participate in lipid-related processes during sperm maturation. For example, Group III secreted phospholipase A2 (sPLA2-III), expressed in the proximal epididymal epithelium, is essential for proper sperm maturation and fertility in mice [shida-2008-spla2-iii]. During epididymal transit, this enzyme facilitates dramatic remodeling of sperm membrane phospholipids, shifting the fatty acid composition toward more unsaturated species (docosapentaenoic and docosahexaenoic acids) that enhance membrane fluidity. Knockout of sPLA2-III leads to compromised lipid remodeling and male infertility.

Lipid rafts, specialized membrane microdomains enriched in cholesterol and sphingolipids, have been described in spermatozoa from multiple species including humans. These rafts serve as signaling platforms that reorganize during capacitation, concentrating key proteins required for fertilization [cornwall-2009-epididymis-review]. Epididymosomes, extracellular vesicles secreted by the epididymal epithelium, also transfer proteins and lipids to maturing spermatozoa through membrane fusion.

Given this biological context, CLPSL1's expression pattern and predicted lipid-binding capacity (based on its colipase domain) are consistent with a potential role in the lipid-related aspects of sperm maturation. However, unlike sPLA2-III which has direct enzymatic activity, CLPSL1 appears to lack the residues required for lipase activation (based on studies of CLPSL2), suggesting it may function through direct lipid binding or protein-protein interactions rather than enzymatic catalysis. The exact nature of CLPSL1's contribution to epididymal lipid metabolism, if any, remains to be determined experimentally.

## Evolutionary Conservation

CLPSL1 is conserved across mammals, with orthologs identified in 34 organisms according to GeneCards. The conservation of both CLPSL1 and CLPSL2 across mammalian species suggests that these genes serve biologically important functions, even if loss of individual family members is tolerated for fertility in mice. The presence of two colipase-like paralogs specifically expressed in different regions of the epididymis (CLPSL1 in corpus, CLPSL2 in caput) suggests that they may have complementary or partially redundant roles in sperm maturation.

## Open Questions

Despite the available annotation and expression data, numerous fundamental questions about CLPSL1 remain unanswered:

1. **Molecular function:** Does CLPSL1 retain any capacity to activate lipases, or has it completely lost this ancestral function? What is its precise molecular function in the epididymis?

2. **Substrate specificity:** If CLPSL1 binds lipids, what are its preferred lipid substrates? Does it interact with specific membrane components of spermatozoa?

3. **Sperm interaction:** Does CLPSL1, like CLPSL2, bind to specific regions of spermatozoa? If so, what is the functional consequence of this binding?

4. **Genetic redundancy:** Do CLPSL1 and CLPSL2 have redundant functions that would only be revealed in double-knockout animals?

5. **Human fertility:** Is CLPSL1 expression or function altered in cases of human male infertility? Are there genetic variants associated with reproductive disorders?

6. **Signaling role:** Does CLPSL1, like procolipase/enterostatin, have signaling functions beyond its structural role?

7. **Cancer association:** Why is CLPSL1 upregulated in colorectal cancer with lymph node metastasis? Is this functionally significant or merely a consequence of aberrant gene expression in cancer cells?

8. **Brain expression:** What is the functional significance, if any, of CLPSL1 expression in neurons?

These questions would require targeted experimental studies including generation of CLPSL1 knockout mice (and ideally CLPSL1/CLPSL2 double knockouts), biochemical characterization of recombinant CLPSL1 protein, and identification of interacting proteins and lipids in the epididymal context.

## References

1. **li-2020-colorectal-biomarker-abstract**: Li X, Zhang Q, Zhao L, et al. A Combined four-mRNA Signature Associated with Lymphatic Metastasis for Prognosis of Colorectal Cancer. J Cancer. 2020;11(8):2139-2149. PMID: 32127941. DOI: [10.7150/jca.38796](https://doi.org/10.7150/jca.38796)

2. **lu-2018-clpsl2-epididymis-abstract**: Lu X, Ding F, Lian Z, et al. An epididymis-specific secretory protein Clpsl2 critically regulates sperm motility, acrosomal integrity, and male fertility. J Cell Biochem. 2018;119(6):4760-4774. PMID: 29323738. DOI: [10.1002/jcb.26668](https://doi.org/10.1002/jcb.26668)

3. **noda-2019-nine-genes-dispensable-abstract**: Noda T, Sakurai N, Nozawa K, et al. Nine genes abundantly expressed in the epididymis are not essential for male fecundity in mice. Andrology. 2019;7(5):644-653. PMID: 30927342. PMCID: PMC6688925. DOI: [10.1111/andr.12621](https://doi.org/10.1111/andr.12621)

4. **robertson-2020-reproductive-tract-genes-abstract**: Robertson MJ, Kent K, Tharp N, et al. Large-scale discovery of male reproductive tract-specific genes through analysis of RNA-seq datasets. BMC Biol. 2020;18(1):103. PMID: 32814578. PMCID: PMC7436996. DOI: [10.1186/s12915-020-00826-z](https://doi.org/10.1186/s12915-020-00826-z)

5. **vantilbeurgh-1999-colipase-structure-abstract**: van Tilbeurgh H, Bezzine S, Cambillau C, Verger R, Carrière F. Colipase: structure and interaction with pancreatic lipase. Biochim Biophys Acta. 1999;1441(2-3):173-84. PMID: 10570245. DOI: [10.1016/s1388-1981(99)00149-3](https://doi.org/10.1016/s1388-1981(99)00149-3)

6. **lowe-2002-triglyceride-lipases-abstract**: Lowe ME. The triglyceride lipases of the pancreas. J Lipid Res. 2002;43(12):2007-16. PMID: 12454260. DOI: [10.1194/jlr.r200012-jlr200](https://doi.org/10.1194/jlr.r200012-jlr200)

7. **erlanson-albertsson-1997-enterostatin-abstract**: Erlanson-Albertsson C, York D. Enterostatin--a peptide regulating fat intake. Obes Res. 1997;5(4):360-72. PMID: 9285845. DOI: [10.1002/j.1550-8528.1997.tb00565.x](https://doi.org/10.1002/j.1550-8528.1997.tb00565.x)

8. **kumar-2021-pancreatic-lipase-inhibitors-abstract**: Kumar A, Chauhan S. Pancreatic lipase inhibitors: The road voyaged and successes. Life Sci. 2021;271:119115. PMID: 33515565. DOI: [10.1016/j.lfs.2021.119115](https://doi.org/10.1016/j.lfs.2021.119115)

9. **human-protein-atlas-clpsl1**: Human Protein Atlas - CLPSL1. https://www.proteinatlas.org/ENSG00000204140-CLPSL1

10. **genecards-clpsl1**: GeneCards - CLPSL1 Gene. https://www.genecards.org/cgi-bin/carddisp.pl?gene=CLPSL1

11. **biogrid-clpsl1**: BioGRID - CLPSL1 Interactions. https://thebiogrid.org/131012/table/homo-sapiens/clpsl1.html

12. **cornwall-2009-epididymis-review**: Cornwall GA. New insights into epididymal biology and function. Hum Reprod Update. 2009;15(2):213-227. PMCID: PMC2639084. https://pmc.ncbi.nlm.nih.gov/articles/PMC2639084/

13. **shida-2008-spla2-iii**: Sato H, et al. Group III secreted phospholipase A2 regulates epididymal sperm maturation and fertility in mice. J Biol Chem. 2010;285(17):12224-12232. PMCID: PMC2860917. https://pmc.ncbi.nlm.nih.gov/articles/PMC2860917/


## Citations

1. cornwall-2009-epididymis-review-summary.md
2. erlanson-albertsson-1997-enterostatin-abstract.md
3. kumar-2021-pancreatic-lipase-inhibitors-abstract.md
4. li-2020-colorectal-biomarker-abstract.md
5. lowe-2002-triglyceride-lipases-abstract.md
6. lu-2018-clpsl2-epididymis-abstract.md
7. lu-2018-clpsl2-epididymis-summary.md
8. noda-2019-nine-genes-dispensable-abstract.md
9. noda-2019-nine-genes-dispensable-summary.md
10. robertson-2020-reproductive-tract-genes-abstract.md
11. shida-2008-spla2-iii-summary.md
12. vantilbeurgh-1999-colipase-structure-abstract.md