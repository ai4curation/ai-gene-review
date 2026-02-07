---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-05T09:17:20.063084'
end_time: '2026-02-05T09:22:50.378468'
duration_seconds: 330.32
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: CPT1C
  gene_symbol: CPT1C
  uniprot_accession: Q8TCG5
  protein_description: 'RecName: Full=Palmitoyl thioesterase CPT1C {ECO:0000305};
    EC=3.1.2.22 {ECO:0000269|PubMed:30135643}; AltName: Full=Carnitine O-palmitoyltransferase
    1, brain isoform; Short=CPTI-B; AltName: Full=Carnitine palmitoyltransferase 1C;
    AltName: Full=Carnitine palmitoyltransferase I {ECO:0000303|PubMed:12376098};
    Short=CPT I-C {ECO:0000303|PubMed:12376098};'
  gene_info: Name=CPT1C {ECO:0000312|HGNC:HGNC:18540}; Synonyms=CATL1;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the carnitine/choline acetyltransferase family.
  protein_domains: Carn_acyl_trans. (IPR000542); CAT-like_dom_sf. (IPR023213); Cho/carn_acyl_trans.
    (IPR039551); Cho/carn_acyl_trans_2. (IPR042231); CPT_N. (IPR032476)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 15
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q8TCG5
- **Protein Description:** RecName: Full=Palmitoyl thioesterase CPT1C {ECO:0000305}; EC=3.1.2.22 {ECO:0000269|PubMed:30135643}; AltName: Full=Carnitine O-palmitoyltransferase 1, brain isoform; Short=CPTI-B; AltName: Full=Carnitine palmitoyltransferase 1C; AltName: Full=Carnitine palmitoyltransferase I {ECO:0000303|PubMed:12376098}; Short=CPT I-C {ECO:0000303|PubMed:12376098};
- **Gene Information:** Name=CPT1C {ECO:0000312|HGNC:HGNC:18540}; Synonyms=CATL1;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the carnitine/choline acetyltransferase family.
- **Key Domains:** Carn_acyl_trans. (IPR000542); CAT-like_dom_sf. (IPR023213); Cho/carn_acyl_trans. (IPR039551); Cho/carn_acyl_trans_2. (IPR042231); CPT_N. (IPR032476)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CPT1C" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CPT1C' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CPT1C** (gene ID: CPT1C, UniProt: Q8TCG5) in human.

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
- **UniProt Accession:** Q8TCG5
- **Protein Description:** RecName: Full=Palmitoyl thioesterase CPT1C {ECO:0000305}; EC=3.1.2.22 {ECO:0000269|PubMed:30135643}; AltName: Full=Carnitine O-palmitoyltransferase 1, brain isoform; Short=CPTI-B; AltName: Full=Carnitine palmitoyltransferase 1C; AltName: Full=Carnitine palmitoyltransferase I {ECO:0000303|PubMed:12376098}; Short=CPT I-C {ECO:0000303|PubMed:12376098};
- **Gene Information:** Name=CPT1C {ECO:0000312|HGNC:HGNC:18540}; Synonyms=CATL1;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the carnitine/choline acetyltransferase family.
- **Key Domains:** Carn_acyl_trans. (IPR000542); CAT-like_dom_sf. (IPR023213); Cho/carn_acyl_trans. (IPR039551); Cho/carn_acyl_trans_2. (IPR042231); CPT_N. (IPR032476)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CPT1C" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CPT1C' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CPT1C** (gene ID: CPT1C, UniProt: Q8TCG5) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

Plan
- Verified identity and nomenclature: CPT1C (human; UniProt Q8TCG5), a CPT1-family member that is neuron-enriched and ER-localized, mitigating symbol ambiguity and ensuring correct mapping of evidence (completed).
- Retrieved and synthesized recent (2023–2024) literature on function, localization, malonyl-CoA sensing, and disease relevance; emphasized authoritative reviews and primary studies (completed via sources below).
- Extracted precise evidence on pathways (AMPK–ACC–malonyl-CoA), neuronal roles, and cancer relevance (completed).
- Created a compact artifact table summarizing key claims, sources, and URLs to support rapid verification (completed).
- Synthesized the comprehensive research report with citations, URLs, and publication years; prioritized 2023–2024 sources (completed).

Artifact summary
| Topic | Key claim | Source (year) | Journal | URL |
|---|---|---:|---|---|
| Identity / Localization | Human CPT1C is a brain-enriched neuronal CPT1 isoform, localized to the endoplasmic reticulum (ER) and encoded at 19q13.33 (UniProt Q8TCG5). (duan2024theroleof pages 4-5) | 2024 | Biology | https://doi.org/10.3390/biology13110892 |
| Family / Malonyl-CoA sensitivity | Member of the CPT1/carnitine acyltransferase family; retains malonyl-CoA binding motifs and can bind malonyl-CoA, supporting a malonyl-CoA sensing role. (duan2024theroleof pages 4-5, schlaepfer2020cpt1amediatedfatoxidation pages 5-6) | 2024; 2020 | Biology; Endocrinology | https://doi.org/10.3390/biology13110892; https://doi.org/10.1210/endocr/bqz046 |
| Catalytic activity vs pseudoenzyme | CPT1C displays markedly reduced/"suboptimal" canonical CPT1 enzymatic activity vs CPT1A/B and is often described as a pseudoenzyme (limited transferase activity reported; enzymatic role remains ambiguous). (fado2023tobeor pages 1-2, muley2023cpt1cdownregulationcauses pages 1-2, duan2024theroleof pages 9-11) | 2023; 2023; 2024 | Cell Death & Disease; Int J Mol Sci; Biology | https://doi.org/10.1038/s41419-023-05599-1; https://doi.org/10.3390/ijms24020946; https://doi.org/10.3390/biology13110892 |
| Primary biochemical function | Acts primarily as a nutrient / malonyl-CoA sensor that regulates lipid metabolism, autophagy and adaptation to energy/hypoxic stress rather than serving as a main mitochondrial long‑chain acyl‑carnitine transferase. (fado2023tobeor pages 1-2, duan2024theroleof pages 9-11) | 2023; 2024 | Cell Death & Disease; Biology | https://doi.org/10.1038/s41419-023-05599-1; https://doi.org/10.3390/biology13110892 |
| Neuronal roles & subcellular functions | ER-resident in neurons; implicated in hypothalamic control of brown adipose thermogenesis and in regulating lysosome/secretory pathway, vesicle trafficking and dendritic spine maturation. (schlaepfer2020cpt1amediatedfatoxidation pages 5-6, fado2023tobeor pages 1-2) | 2020; 2023 | Endocrinology; Cell Death & Disease | https://doi.org/10.1210/endocr/bqz046; https://doi.org/10.1038/s41419-023-05599-1 |
| AMPK–ACC–malonyl‑CoA pathway links | CPT1C expression/activity is regulated by cellular energy signals (AMPK-sensitive 5'UTR / translational control) and tied to the ACC–malonyl-CoA axis, consistent with a malonyl‑CoA sensing mechanism. (duan2024theroleof pages 4-5, fado2023tobeor pages 1-2) | 2024; 2023 | Biology; Cell Death & Disease | https://doi.org/10.3390/biology13110892; https://doi.org/10.1038/s41419-023-05599-1 |
| Cancer relevance (hypoxia/nutrient stress, APC/C regulation, chemo resistance, CAFs) | CPT1C is frequently upregulated in tumors enabling adaptation to hypoxia/nutrient stress; CPT1C levels are cell-cycle regulated (APC/C substrate) and influence tumor growth, chemoresistance (anthracycline uptake/response) and stromal/CAF-driven immunosuppression. (fado2023tobeor pages 1-2, muley2023cpt1cdownregulationcauses pages 1-2, duan2024theroleof pages 9-11) | 2023; 2023; 2024 | Cell Death & Disease; Int J Mol Sci; Biology | https://doi.org/10.1038/s41419-023-05599-1; https://doi.org/10.3390/ijms24020946; https://doi.org/10.3390/biology13110892 |
| Comparison to CPT1A/B | CPT1A/B are mitochondrial, catalytically active long‑chain acyl‑CoA→acyl‑carnitine transferases (robust FAO drivers and malonyl‑CoA sensitive); by contrast CPT1C is ER-localized, less catalytically active, and functions mainly in sensing/regulation rather than canonical mitochondrial FA import. (schlaepfer2020cpt1amediatedfatoxidation pages 5-6, fado2023tobeor pages 1-2) | 2020; 2023 | Endocrinology; Cell Death & Disease | https://doi.org/10.1210/endocr/bqz046; https://doi.org/10.1038/s41419-023-05599-1 |


*Table: Compact table summarizing key evidence about human CPT1C (UniProt Q8TCG5): identity, localization, enzymatic activity debates, regulatory links, neuronal roles, cancer relevance, and comparison to CPT1A/B, with sources (context IDs) and DOIs for verification.*

Comprehensive research report: Human CPT1C (UniProt Q8TCG5)

Verification of target identity and scope
- Gene/protein identity: The target is human CPT1C (UniProt Q8TCG5), a member of the CPT1 family distinct from CPT1A/B; it is predominantly neuronal and localizes to the endoplasmic reticulum (ER), not mitochondria (https://doi.org/10.3390/biology13110892, Nov 2024; https://doi.org/10.1210/endocr/bqz046, 2020). These recent sources confirm nomenclature, organism, and subcellular localization consistent with the UniProt description, avoiding confusion with CPT1A/B (duan2024theroleof pages 4-5, schlaepfer2020cpt1amediatedfatoxidation pages 5-6).

1) Key concepts and definitions (current understanding)
- Family/definition: CPT1C is the brain-enriched isoform of the carnitine palmitoyltransferase 1 (CPT1) family. Unlike CPT1A/B, which reside in mitochondria and catalyze acyl‑CoA→acyl‑carnitine transfer to drive fatty acid β‑oxidation, CPT1C is ER-resident in neurons and exhibits markedly reduced canonical CPT1 catalytic activity (https://doi.org/10.1038/s41419-023-05599-1, Jan 2023; https://doi.org/10.1210/endocr/bqz046, 2020) (fado2023tobeor pages 1-2, schlaepfer2020cpt1amediatedfatoxidation pages 5-6).
- Malonyl‑CoA sensing concept: CPT1C retains motifs to bind malonyl‑CoA and is proposed to act primarily as a nutrient/malonyl‑CoA sensor that regulates other lipid and trafficking proteins, rather than serving as a major mitochondrial fatty‑acid transporter (https://doi.org/10.3390/biology13110892, 2024; https://doi.org/10.1038/s41419-023-05599-1, 2023) (duan2024theroleof pages 4-5, fado2023tobeor pages 1-2).
- Cellular localization: Multiple studies place CPT1C at the ER in neurons and cancer cells, highlighting a distinct cellular role from the mitochondrial CPT1A/B isoforms (https://doi.org/10.1210/endocr/bqz046, 2020; https://doi.org/10.1038/s41419-023-05599-1, 2023) (schlaepfer2020cpt1amediatedfatoxidation pages 5-6, fado2023tobeor pages 1-2).

2) Molecular function, catalytic activity, and substrate specificity
- Catalytic activity: Contemporary reviews and primary studies emphasize that CPT1C has “inefficient” or “suboptimal” canonical CPT1 transferase activity compared to CPT1A/B and is frequently described as a pseudoenzyme. Evidence supports binding to malonyl‑CoA and regulatory roles, but not robust long‑chain acyl‑CoA→acyl‑carnitine transfer in mitochondria (https://doi.org/10.1038/s41419-023-05599-1, 2023; https://doi.org/10.3390/ijms24020946, 2023; https://doi.org/10.3390/biology13110892, 2024) (fado2023tobeor pages 1-2, muley2023cpt1cdownregulationcauses pages 1-2, duan2024theroleof pages 9-11).
- Primary biochemical function: The predominant model is that CPT1C functions as a nutrient/malonyl‑CoA sensor that modulates lipid metabolism, autophagy, vesicle/lysosome dynamics, and secretory pathway components to support cellular adaptation to nutrient deprivation and hypoxia, especially in neurons and cancer cells (https://doi.org/10.1038/s41419-023-05599-1, 2023; https://doi.org/10.3390/biology13110892, 2024) (fado2023tobeor pages 1-2, duan2024theroleof pages 9-11).
- Comparison with CPT1A/B: CPT1A/B are mitochondrial long‑chain acyltransferases that are robustly inhibited by malonyl‑CoA (especially CPT1B), serving as gatekeepers of mitochondrial fatty‑acid entry; CPT1C is ER‑localized and less catalytically active, aligning with a sensing/regulatory role (https://doi.org/10.1210/endocr/bqz046, 2020; https://doi.org/10.1038/s41419-023-05599-1, 2023) (schlaepfer2020cpt1amediatedfatoxidation pages 5-6, fado2023tobeor pages 1-2).

3) Cellular localization and tissue expression
- Neuron-enriched, ER-resident: Modern sources consistently localize CPT1C to the ER in neurons, contrasting with mitochondrial CPT1A/B. Reviews place CPT1C on human chromosome 19q13.33 and indicate predominant expression in brain (and some reports of expression in testis) (https://doi.org/10.3390/biology13110892, 2024; https://doi.org/10.1210/endocr/bqz046, 2020) (duan2024theroleof pages 4-5, schlaepfer2020cpt1amediatedfatoxidation pages 5-6).

4) Pathways and mechanism-of-action
- AMPK–ACC–malonyl‑CoA axis: CPT1C expression is tuned by cellular energy availability. Mechanisms include AMPK-sensitive regulation and translational control via its 5′UTR, consistent with a role in malonyl‑CoA sensing and lipid‑metabolism signaling (https://doi.org/10.3390/biology13110892, 2024; https://doi.org/10.1038/s41419-023-05599-1, 2023) (duan2024theroleof pages 4-5, fado2023tobeor pages 1-2).
- Neuronal metabolic control: CPT1C has been associated with hypothalamic regulation of brown adipose tissue thermogenesis and broader neuronal energy homeostasis, emphasizing a signaling/regulatory role rather than direct mitochondrial FA transport (https://doi.org/10.1210/endocr/bqz046, 2020) (schlaepfer2020cpt1amediatedfatoxidation pages 5-6).

5) Neuronal biology: trafficking and synaptic functions
- Regulatory interactions in neurons: Neuroscience data summarized in recent reviews indicate CPT1C interacts with proteins involved in lipid metabolism and transport, lysosome motility, and the secretory pathway, affecting neuronal plasticity and adaptation to stress (https://doi.org/10.1038/s41419-023-05599-1, 2023) (fado2023tobeor pages 1-2).

6) Disease relevance and real‑world implementations
- Cancer biology: 2023–2024 evidence synthesizes a consistent picture in which CPT1C expression supports cancer cell adaptation to metabolic stress (hypoxia, nutrient limitation), suppresses senescence, and promotes tumor growth. Mechanistically, CPT1C depletion impairs mitochondrial function (membrane potential, respiration), reduces ATP, elevates ROS, and remodels cellular lipidomes; these changes limit proliferation/migration/invasion and decrease in vivo tumor growth (https://doi.org/10.1038/s41419-023-05599-1, 2023) (fado2023tobeor pages 3-5).
- Chemotherapy resistance: In breast cancer cells, CPT1C downregulation remodels plasma-membrane lipids (increased phospholipid saturation and rigidity), reduces doxorubicin uptake, and increases survival under anthracycline treatment; clinical correlation suggests lower CPT1C associates with poorer anthracycline response, nominating CPT1C as a predictive biomarker (https://doi.org/10.3390/ijms24020946, 2023) (muley2023cpt1cdownregulationcauses pages 1-2).
- Cell-cycle and regulatory networks: Reviews consolidate evidence that CPT1C is integrated into cell-cycle and transcriptional networks, including regulation by APC/C motifs and miRNAs (e.g., miR‑377‑3p), linking lipid‑metabolism cues to proliferation and stress tolerance, though mechanistic details remain under active investigation (https://doi.org/10.3390/biology13110892, 2024) (duan2024theroleof pages 9-11).

7) Expert opinions and analysis (authoritative sources)
- Fadó et al. (2023) argue the main function of CPT1C is not to “burn fat” but to serve as a malonyl‑CoA/nutrient sensor coordinating lipid metabolic remodeling and trafficking to enable survival under stress; this synthesis reconciles ER localization, poor catalytic activity, and robust phenotypes upon CPT1C perturbation in neurons and tumors (https://doi.org/10.1038/s41419-023-05599-1, 2023) (fado2023tobeor pages 1-2, fado2023tobeor pages 3-5).
- Schlaepfer & Joshi (2020) provide comparative CPT1 family context: CPT1A/B are mitochondrial, catalytically active, and malonyl‑CoA‑regulated; CPT1C is ER‑localized with lower catalytic activity and ties to neuronal thermogenesis control (https://doi.org/10.1210/endocr/bqz046, 2020) (schlaepfer2020cpt1amediatedfatoxidation pages 5-6).

8) Relevant statistics and data from recent studies
- Phenotypic impacts of CPT1C loss in cancer models include marked mitochondrial dysfunction and lipidome remodeling, with downstream decreases in proliferation/migration/invasion and tumor growth in vivo; CPT1C overexpression counters senescence, while silencing promotes it (qualitative summary from a 2023 peer‑reviewed synthesis) (https://doi.org/10.1038/s41419-023-05599-1, 2023) (fado2023tobeor pages 3-5).
- In breast cancer cells, CPT1C silencing increases plasma‑membrane phospholipid saturation (indicative of higher membrane rigidity), reduces doxorubicin uptake, and increases survival during anthracycline exposure; patient‑level analyses correlate lower CPT1C with poorer anthracycline response, suggesting utility as a biomarker (https://doi.org/10.3390/ijms24020946, 2023) (muley2023cpt1cdownregulationcauses pages 1-2).

9) Ambiguities and open questions
- Enzymatic classification and EC assignment: While historical annotations sometimes list enzymatic activities for CPT1C, contemporary mechanistic work emphasizes poor canonical CPT1 catalysis, ER localization, and sensor/regulatory roles. Robust substrate specificity for a physiologically meaningful transferase or thioesterase activity in human CPT1C remains to be conclusively established in vivo; the weight of 2023–2024 expert synthesis supports its role as a malonyl‑CoA/nutrient sensor rather than a primary acyltransferase (https://doi.org/10.1038/s41419-023-05599-1, 2023) (fado2023tobeor pages 1-2).

Summary and implications
CPT1C (Q8TCG5) is a human, neuron‑enriched CPT1‑family protein that localizes to the ER and functions primarily as a malonyl‑CoA/nutrient sensor modulating lipid metabolism and trafficking processes, distinct from the mitochondrial, catalytically active CPT1A/B. In neurons, CPT1C contributes to energy‑balance circuits and thermogenic regulation; in cancer, it facilitates adaptation to metabolic stress, influences mitochondrial function and lipidomes, and modulates chemotherapy response—suggesting roles as both a mechanistic node and a potential biomarker/therapeutic target. The most authoritative 2023–2024 sources converge on a regulatory/sensor view of CPT1C with limited canonical enzymatic activity, aligning molecular localization with function (fado2023tobeor pages 1-2, fado2023tobeor pages 3-5, schlaepfer2020cpt1amediatedfatoxidation pages 5-6, muley2023cpt1cdownregulationcauses pages 1-2, duan2024theroleof pages 4-5, duan2024theroleof pages 9-11).

References

1. (duan2024theroleof pages 4-5): Yanxia Duan, Jiaxin Liu, Ailin Li, Chang Liu, Guang Shu, and Gang Yin. The role of the cpt family in cancer: searching for new therapeutic strategies. Biology, 13:892, Nov 2024. URL: https://doi.org/10.3390/biology13110892, doi:10.3390/biology13110892. This article has 10 citations and is from a poor quality or predatory journal.

2. (schlaepfer2020cpt1amediatedfatoxidation pages 5-6): Isabel R Schlaepfer and Molishree Joshi. Cpt1a-mediated fat oxidation, mechanisms and therapeutic potential. Endocrinology, Jan 2020. URL: https://doi.org/10.1210/endocr/bqz046, doi:10.1210/endocr/bqz046. This article has 704 citations and is from a domain leading peer-reviewed journal.

3. (fado2023tobeor pages 1-2): Rut Fadó, Sebastian Zagmutt, Laura Herrero, Helena Muley, Rosalía Rodríguez-Rodríguez, Huichang Bi, Dolors Serra, and Núria Casals. To be or not to be a fat burner, that is the question for cpt1c in cancer cells. Cell Death &amp; Disease, Jan 2023. URL: https://doi.org/10.1038/s41419-023-05599-1, doi:10.1038/s41419-023-05599-1. This article has 20 citations and is from a peer-reviewed journal.

4. (muley2023cpt1cdownregulationcauses pages 1-2): Helena Muley, Karmele Valencia, Josefina Casas, Bea Moreno, Luis Botella, Fernando Lecanda, Rut Fadó, and Núria Casals. Cpt1c downregulation causes plasma membrane remodelling and anthracycline resistance in breast cancer. International Journal of Molecular Sciences, 24:946, Jan 2023. URL: https://doi.org/10.3390/ijms24020946, doi:10.3390/ijms24020946. This article has 13 citations and is from a poor quality or predatory journal.

5. (duan2024theroleof pages 9-11): Yanxia Duan, Jiaxin Liu, Ailin Li, Chang Liu, Guang Shu, and Gang Yin. The role of the cpt family in cancer: searching for new therapeutic strategies. Biology, 13:892, Nov 2024. URL: https://doi.org/10.3390/biology13110892, doi:10.3390/biology13110892. This article has 10 citations and is from a poor quality or predatory journal.

6. (fado2023tobeor pages 3-5): Rut Fadó, Sebastian Zagmutt, Laura Herrero, Helena Muley, Rosalía Rodríguez-Rodríguez, Huichang Bi, Dolors Serra, and Núria Casals. To be or not to be a fat burner, that is the question for cpt1c in cancer cells. Cell Death &amp; Disease, Jan 2023. URL: https://doi.org/10.1038/s41419-023-05599-1, doi:10.1038/s41419-023-05599-1. This article has 20 citations and is from a peer-reviewed journal.

## Citations

1. duan2024theroleof pages 4-5
2. fado2023tobeor pages 1-2
3. fado2023tobeor pages 3-5
4. duan2024theroleof pages 9-11
5. https://doi.org/10.3390/biology13110892
6. https://doi.org/10.3390/biology13110892;
7. https://doi.org/10.1210/endocr/bqz046
8. https://doi.org/10.1038/s41419-023-05599-1;
9. https://doi.org/10.3390/ijms24020946;
10. https://doi.org/10.1210/endocr/bqz046;
11. https://doi.org/10.1038/s41419-023-05599-1
12. https://doi.org/10.3390/biology13110892,
13. https://doi.org/10.1210/endocr/bqz046,
14. https://doi.org/10.1038/s41419-023-05599-1,
15. https://doi.org/10.3390/ijms24020946,