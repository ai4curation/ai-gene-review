---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-10-09T21:20:36.768315'
end_time: '2026-10-09T21:30:02.623655'
duration_seconds: 565.86
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: Enoph
  gene_symbol: Enoph
  uniprot_accession: Q9VN95
  protein_description: 'RecName: Full=Enolase-phosphatase E1 {ECO:0000255|HAMAP-Rule:MF_03117};
    EC=3.1.3.77 {ECO:0000255|HAMAP-Rule:MF_03117}; AltName: Full=2,3-diketo-5-methylthio-1-phosphopentane
    phosphatase {ECO:0000255|HAMAP-Rule:MF_03117};'
  gene_info: Name=Enoph {ECO:0000312|FlyBase:FBgn0037305}; ORFNames=CG12173 {ECO:0000312|FlyBase:FBgn0037305};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Belongs to the HAD-like hydrolase superfamily. MasA/MtnC
  protein_domains: Enolase-ppase_E1. (IPR023943); ENOPH1_eukaryotes. (IPR027511);
    HAD-like_sf. (IPR036412); HAD-SF_hydro_IA. (IPR006439); HAD_sf. (IPR023214)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 29
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Enoph-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q9VN95
- **Protein Description:** RecName: Full=Enolase-phosphatase E1 {ECO:0000255|HAMAP-Rule:MF_03117}; EC=3.1.3.77 {ECO:0000255|HAMAP-Rule:MF_03117}; AltName: Full=2,3-diketo-5-methylthio-1-phosphopentane phosphatase {ECO:0000255|HAMAP-Rule:MF_03117};
- **Gene Information:** Name=Enoph {ECO:0000312|FlyBase:FBgn0037305}; ORFNames=CG12173 {ECO:0000312|FlyBase:FBgn0037305};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the HAD-like hydrolase superfamily. MasA/MtnC
- **Key Domains:** Enolase-ppase_E1. (IPR023943); ENOPH1_eukaryotes. (IPR027511); HAD-like_sf. (IPR036412); HAD-SF_hydro_IA. (IPR006439); HAD_sf. (IPR023214)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Enoph" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Enoph' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Enoph** (gene ID: Enoph, UniProt: Q9VN95) in DROME.

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
- **UniProt Accession:** Q9VN95
- **Protein Description:** RecName: Full=Enolase-phosphatase E1 {ECO:0000255|HAMAP-Rule:MF_03117}; EC=3.1.3.77 {ECO:0000255|HAMAP-Rule:MF_03117}; AltName: Full=2,3-diketo-5-methylthio-1-phosphopentane phosphatase {ECO:0000255|HAMAP-Rule:MF_03117};
- **Gene Information:** Name=Enoph {ECO:0000312|FlyBase:FBgn0037305}; ORFNames=CG12173 {ECO:0000312|FlyBase:FBgn0037305};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the HAD-like hydrolase superfamily. MasA/MtnC
- **Key Domains:** Enolase-ppase_E1. (IPR023943); ENOPH1_eukaryotes. (IPR027511); HAD-like_sf. (IPR036412); HAD-SF_hydro_IA. (IPR006439); HAD_sf. (IPR023214)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Enoph" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Enoph' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Enoph** (gene ID: Enoph, UniProt: Q9VN95) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation of *Drosophila melanogaster* Enoph (Q9VN95)

**Identity and evidence status.** The requested protein is fly **Enoph**, ORF **CG12173**, FlyBase **FBgn0037305**, UniProt **Q9VN95** ([UniProt record](https://www.uniprot.org/uniprotkb/Q9VN95/entry); [FlyBase record](https://flybase.org/reports/FBgn0037305.html)). The supplied annotation identifies it as **enolase-phosphatase E1** (EC 3.1.3.77), in the MasA/MtnC branch of the HAD-like hydrolase superfamily. **The gene symbol “Enoph” is ambiguous or literature is limited for this specific protein:** the retrieved mechanistic and genetic studies concern human, yeast, or bacterial enzymes, not an experimentally characterized Q9VN95. Human **ENOPH1** is relevant comparative evidence, but it is **not** the fly gene. The functional assignment below is therefore principally an inference from the supplied UniProt family/domain annotation and experimentally studied pathway counterparts, not a demonstrated fly-specific activity. (camille2012functionalidentificationof pages 1-3, pirkov2008acompleteinventory pages 1-2, wang2005purificationcrystallizationand pages 1-2)

## Primary biochemical function

The best-supported predicted function is the **bifunctional enolase–phosphatase step of methionine salvage**. The expected physiological substrate is **2,3-diketo-5-methylthio-1-phosphopentane** (also termed 2,3-diketo-5-methylthiopentyl-1-phosphate or DK-MTP-1-P). Enolization first yields **2-hydroxy-3-keto-5-methylthiopentenyl-1-phosphate**; dephosphorylation then releases inorganic phosphate and the **acireductone 1,2-dihydroxy-3-keto-5-methylthiopentene**. In human E1/MASA, the two transformations are attributed to one enzyme. In *Bacillus subtilis*, by contrast, the corresponding enolization and dephosphorylation are performed by separate proteins, MtnW and MtnX. These reactions should **not** be confused with the phosphoenolpyruvate-producing reaction of glycolytic enolase, or with the preceding methionine-salvage **dehydratase** reaction catalyzed by human APIP. (wang2005purificationcrystallizationand pages 1-2, sekowska2019revisitingthemethionine pages 9-10, camille2012functionalidentificationof pages 1-3)

This is a **predicted substrate assignment for fly Enoph**, not evidence that purified Q9VN95 has been assayed. No fly-specific substrate panel, kinetic constants, competing-substrate measurements, or test of whether it performs both half-reactions was identified. Accordingly, specificity for DK-MTP-1-P is better supported than any assertion that fly Enoph acts *exclusively* on that molecule. (wang2005purificationcrystallizationand pages 1-2, sekowska2019revisitingthemethionine pages 9-10)

The HAD-like designation is chemically consistent with a magnesium-assisted phosphatase. Studies of the related bacterial MtnX phosphatase resolved an active-site **Mg²⁺** and conserved HAD catalytic motifs, and proposed phosphate hydrolysis through a phosphorylated aspartate intermediate. Earlier work summarized for MASA also reports a magnesium requirement. Those findings support a plausible mechanism for Enoph’s phosphatase activity, but neither the metal requirement nor catalytic residues have been experimentally established for **fly Q9VN95** in the sources retrieved. (xu2007crystalstructureof pages 4-6, wang2005purificationcrystallizationand pages 1-2)

## Biological process and site of action

Methionine salvage recovers the sulfur-containing portion of **5′-methylthioadenosine (MTA)**, produced during polyamine synthesis from S-adenosylmethionine. Enoph is assigned **after** the methylthioribulose-1-phosphate dehydratase step and **before** acireductone dioxygenase; subsequent reactions yield the methionine precursor 4-methylthio-2-oxobutanoate and finally methionine. Its precise proposed role is thus **recycling MTA-derived sulfur into methionine**, rather than directly catalyzing polyamine synthesis, methylation, or a signaling reaction. (camille2012functionalidentificationof pages 1-3, pirkov2008acompleteinventory pages 1-2, sekowska2019revisitingthemethionine pages 9-10)

**Cytosol is the most defensible predicted site of action**, because the eukaryotic methionine-salvage pathway is described as cytosolic. This is a pathway-level inference: the retrieved work does **not** demonstrate Enoph localization in fly cells by imaging, fractionation, or another protein-specific experiment. In particular, cytoplasmic immunostaining reported for human **APIP** concerns a *different*, upstream pathway enzyme and cannot establish where fly Enoph resides. An extracellular, membrane-transport, or specific organellar role is likewise not established by the evidence examined. (camille2012functionalidentificationof pages 1-3)

## Experimental support and its limits

The clearest eukaryotic genetic support comes from **yeast Utr4p**, assigned to the same enolase/phosphatase step. Deleting *UTR4* significantly impaired growth when **MTA replaced methionine** as the supplement in the tested methionine-auxotrophic strains (**P < 0.001**, Student’s *t*-test; six degrees of freedom). The study also measured intracellular MTA accumulation in pathway mutants; its authors concluded that Utr4p, rather than another candidate homolog, supplies this yeast step. These results show that an experimentally assigned eukaryotic counterpart is needed for MTA-based methionine salvage **in yeast**; they are not a fly knockout or direct fly-enzyme assay. (pirkov2008acompleteinventory pages 1-2, pirkov2008acompleteinventory pages 2-4, pirkov2008acompleteinventory pages 4-5)

The evidence can be summarized as follows:

| Question | Strongest evidence | Confidence specifically for fly |
|---|---|---|
| Identity | User-provided UniProt annotation links **Q9VN95** to *Drosophila melanogaster* **Enoph**, FlyBase **FBgn0037305**, ORF **CG12173**, and the HAD-like MasA/MtnC family. No retrieved primary paper independently characterized these exact fly identifiers. | **High** for database identity; **low** for direct experimental validation. |
| Primary reaction | Human E1/MASA converts **2,3-diketo-5-methylthio-1-phosphopentane (DK-MTP-1-P)** to the acireductone **1,2-dihydroxy-3-keto-5-methylthiopentene**, through enolization followed by dephosphorylation/phosphate release; comparative review evidence identifies bifunctional MtnC as the widespread one-protein solution (wang2005purificationcrystallizationand pages 1-2, sekowska2019revisitingthemethionine pages 9-10). | **Moderate**: strongly supported by orthology/domain annotation, but not assayed for Q9VN95. |
| Substrate specificity | The family-level reaction defines DK-MTP-1-P as the physiological substrate, but no direct *Drosophila* substrate panel, kinetics, alternative-substrate assay, or catalytic-mutant study was found. HAD-family cap domains commonly contribute to substrate discrimination (wang2005purificationcrystallizationand pages 1-2). | **Moderate–low** for exclusive fly substrate specificity. |
| Catalytic mechanism/cofactor | Human and microbial evidence supports a **Mg²⁺-dependent HAD-like phosphatase mechanism** involving conserved catalytic motifs and a phosphoaspartyl intermediate; bacterial MtnX structural work resolved active-site Mg²⁺ and conserved HAD residues, but that protein performs only the phosphatase half-reaction (wang2005purificationcrystallizationand pages 1-2, xu2007crystalstructureof pages 4-6). | **Moderate** as a mechanistic inference; fly residues and metal dependence were not experimentally tested. |
| Pathway role | Enoph is annotated at the enolase/phosphatase step of the **methionine-salvage pathway**, downstream of methylthioribulose-1-phosphate dehydratase and upstream of acireductone dioxygenase. Yeast **utr4Δ**, deleting the functional eukaryotic ortholog, significantly impaired growth when MTA replaced methionine (**P < 0.001; df = 6**) and caused pathway-metabolite accumulation (pirkov2008acompleteinventory pages 1-2, pirkov2008acompleteinventory pages 2-4). | **Moderate–high** for a conserved biochemical role; no fly knockout/rescue experiment was found. |
| Cellular localization | The eukaryotic methionine-salvage pathway is generally described as **cytosolic**, and human APIP—an adjacent pathway enzyme, not ENOPH1—showed predominantly cytoplasmic staining (camille2012functionalidentificationof pages 1-3). This is pathway-level context rather than localization of fly Enoph. | **Low–moderate**; cytosolic action is plausible but unvalidated for Q9VN95. |
| Recent evidence | A 2023 plant root proteomics study detected a DEP1-family protein among methionine-metabolism proteins associated with mycorrhizal salt treatment, but it neither studied *Drosophila* nor assayed Enoph catalysis (chang2023labelfreequantitativeproteomics pages 8-10). No 2023–2024 fly-specific Enoph study was identified. | **Very low** relevance to fly-specific annotation. |
| Overall status | The proposed annotation is supported by concordant accession/domain information and experimental work on human, yeast, plant, and microbial orthologs, while direct biochemical, localization, kinetic, and organismal evidence for *D. melanogaster* Q9VN95 remains absent from the retrieved literature. | **Moderate** functional-annotation confidence; **low** direct-evidence confidence. |


*Table: Evidence supporting the functional annotation of fly Enoph is separated from experiments performed on orthologs. The table highlights where catalytic and pathway conclusions are strong evolutionary inferences but remain unvalidated directly in Drosophila.*

## Recent literature and applications

The strongest source material for **this particular catalytic assignment** predates 2023. A **2023** plant-root proteomics study reported a DEP1-family protein among proteins associated with methionine-metabolism responses to mycorrhizal salt treatment. It supplies an example of contemporary pathway-level use of this enzyme annotation, **not** a measurement of fly Enoph activity, localization, or stress function. A **2024** review discusses the broader connection of polyamine-derived MTA to methionine recycling, without resolving Q9VN95 function. Neither source warrants assigning a salt-response or cancer phenotype to fly Enoph. No validated fly-specific application, therapeutic implementation, or quantitative Enoph kinetic measurement emerged from the literature examined. (chang2023labelfreequantitativeproteomics pages 8-10, majumder2024thepivotalrole pages 3-4)

**Conclusion.** For functional annotation, Enoph/Q9VN95 is best described as a **putative cytosolic, HAD-family bifunctional enolase–phosphatase that converts the phosphorylated diketone intermediate of the MTA/methionine-salvage pathway to an acireductone plus phosphate**. The pathway position and reaction are well supported in characterized counterparts; **substrate specificity, compartment, catalytic mechanism, and physiological requirement remain unverified directly for the fly protein**. (wang2005purificationcrystallizationand pages 1-2, sekowska2019revisitingthemethionine pages 9-10, pirkov2008acompleteinventory pages 1-2, camille2012functionalidentificationof pages 1-3)

### Key sources, with publication dates

- Wang *et al.* **28 April 2005** (online). Human E1 purification and structural study; reaction description and HAD-family context. https://doi.org/10.1107/S174430910501184X (wang2005purificationcrystallizationand pages 1-2)
- Xu *et al.* **2007**. Bacterial MtnX phosphatase structure and active-site Mg²⁺; relevant mechanistic comparison, **not** the bifunctional fly enzyme. https://doi.org/10.1002/prot.21602 (xu2007crystalstructureof pages 1-3, xu2007crystalstructureof pages 4-6)
- Pirkov *et al.* **August 2008**. Genetic and metabolic identification of yeast Utr4p in methionine salvage. https://doi.org/10.1111/j.1742-4658.2008.06552.x (pirkov2008acompleteinventory pages 1-2, pirkov2008acompleteinventory pages 2-4)
- Mary *et al.* **28 December 2012**. Human methionine-salvage pathway and identification of **APIP as the distinct upstream dehydratase**. https://doi.org/10.1371/journal.pone.0052877 (camille2012functionalidentificationof pages 1-3)
- Sekowska, Ashida and Danchin. **2019 journal volume** (manuscript accepted **14 September 2018**). Comparative review distinguishing bifunctional MtnC from bacterial MtnW/MtnX. https://doi.org/10.1111/1751-7915.13324 (sekowska2019revisitingthemethionine pages 9-10, sekowska2019revisitingthemethionine pages 1-2)
- Chang *et al.* **January 2023**. Plant proteomics; recent but indirect comparative context. https://doi.org/10.3389/fpls.2022.1098260 (chang2023labelfreequantitativeproteomics pages 8-10)
- Majumder, Bano and Nayak. **October 2024**. Broad one-carbon-metabolism review mentioning MTA salvage, **not** fly Enoph experimentation. https://doi.org/10.3390/biom14111387 (majumder2024thepivotalrole pages 3-4)

References

1. (camille2012functionalidentificationof pages 1-3): Camille Mary, Paula Duek, Lisa Salleron, Petra Tienz, Dirk Bumann, Amos Bairoch, and Lydie Lane. Functional identification of apip as human mtnb, a key enzyme in the methionine salvage pathway. PLoS ONE, Dec 2012. URL: https://doi.org/10.1371/journal.pone.0052877, doi:10.1371/journal.pone.0052877. This article has 37 citations and is from a peer-reviewed journal.

2. (pirkov2008acompleteinventory pages 1-2): Ivan Pirkov, Joakim Norbeck, Lena Gustafsson, and Eva Albers. A complete inventory of all enzymes in the eukaryotic methionine salvage pathway. The FEBS Journal, 275:4111-4120, Aug 2008. URL: https://doi.org/10.1111/j.1742-4658.2008.06552.x, doi:10.1111/j.1742-4658.2008.06552.x. This article has 121 citations.

3. (wang2005purificationcrystallizationand pages 1-2): Hui Wang, Hai Pang, Yi Ding, Yi Li, Xiao'ai Wu, and Zihe Rao. Purification, crystallization and preliminary x-ray diffraction analysis of human enolase-phosphatase e1. Acta crystallographica. Section F, Structural biology and crystallization communications, 61 Pt 5:521-3, May 2005. URL: https://doi.org/10.1107/s174430910501184x, doi:10.1107/s174430910501184x. This article has 6 citations.

4. (sekowska2019revisitingthemethionine pages 9-10): Agnieszka Sekowska, Hiroki Ashida, and Antoine Danchin. Revisiting the methionine salvage pathway and its paralogues. Microbial Biotechnology, 12:77-97, Oct 2019. URL: https://doi.org/10.1111/1751-7915.13324, doi:10.1111/1751-7915.13324. This article has 81 citations and is from a peer-reviewed journal.

5. (xu2007crystalstructureof pages 4-6): Qingping Xu, Kumar Singh Saikatendu, S. Sri Krishna, Daniel McMullan, Polat Abdubek, Sanjay Agarwalla, Eileen Ambing, Tamara Astakhova, Herbert L. Axelrod, Dennis Carlton, Hsiu‐Ju Chiu, Thomas Clayton, Michael DiDonato, Lian Duan, Marc‐André Elsliger, Julie Feuerhelm, Slawomir K. Grzechnik, Joanna Hale, Eric Hampton, Gye Won Han, Justin Haugen, Lukasz Jaroszewski, Kevin K. Jin, Heath E. Klock, Mark W. Knuth, Eric Koesema, Mitchell D. Miller, Andrew T. Morse, Edward Nigoghossian, Linda Okach, Silvya Oommachen, Jessica Paulsen, Ron Reyes, Christopher L. Rife, Robert Schwarzenbacher, Henry van den Bedem, Aprilfawn White, Guenter Wolf, Keith O. Hodgson, John Wooley, Ashley M. Deacon, Adam Godzik, Scott A. Lesley, and Ian A. Wilson. Crystal structure of mtnx phosphatase from bacillus subtilis at 2.0 å resolution provides a structural basis for bipartite phosphomonoester hydrolysis of 2‐hydroxy‐3‐keto‐5‐methylthiopentenyl‐1‐phosphate. Proteins: Structure, 69:433-439, Nov 2007. URL: https://doi.org/10.1002/prot.21602, doi:10.1002/prot.21602. This article has 10 citations.

6. (pirkov2008acompleteinventory pages 2-4): Ivan Pirkov, Joakim Norbeck, Lena Gustafsson, and Eva Albers. A complete inventory of all enzymes in the eukaryotic methionine salvage pathway. The FEBS Journal, 275:4111-4120, Aug 2008. URL: https://doi.org/10.1111/j.1742-4658.2008.06552.x, doi:10.1111/j.1742-4658.2008.06552.x. This article has 121 citations.

7. (pirkov2008acompleteinventory pages 4-5): Ivan Pirkov, Joakim Norbeck, Lena Gustafsson, and Eva Albers. A complete inventory of all enzymes in the eukaryotic methionine salvage pathway. The FEBS Journal, 275:4111-4120, Aug 2008. URL: https://doi.org/10.1111/j.1742-4658.2008.06552.x, doi:10.1111/j.1742-4658.2008.06552.x. This article has 121 citations.

8. (chang2023labelfreequantitativeproteomics pages 8-10): Wei-Tung Chang, Yan Zhang, Yuan Ping, Kun Li, Dandan Qi, and Fu-qiang Song. Label-free quantitative proteomics of arbuscular mycorrhizal elaeagnus angustifolia seedlings provides insights into salt-stress tolerance mechanisms. Frontiers in Plant Science, Jan 2023. URL: https://doi.org/10.3389/fpls.2022.1098260, doi:10.3389/fpls.2022.1098260. This article has 18 citations.

9. (majumder2024thepivotalrole pages 3-4): Avisek Majumder, Shabana Bano, and Kasturi Bala Nayak. The pivotal role of one-carbon metabolism in neoplastic progression during the aging process. Biomolecules, 14:1387, Oct 2024. URL: https://doi.org/10.3390/biom14111387, doi:10.3390/biom14111387. This article has 9 citations.

10. (xu2007crystalstructureof pages 1-3): Qingping Xu, Kumar Singh Saikatendu, S. Sri Krishna, Daniel McMullan, Polat Abdubek, Sanjay Agarwalla, Eileen Ambing, Tamara Astakhova, Herbert L. Axelrod, Dennis Carlton, Hsiu‐Ju Chiu, Thomas Clayton, Michael DiDonato, Lian Duan, Marc‐André Elsliger, Julie Feuerhelm, Slawomir K. Grzechnik, Joanna Hale, Eric Hampton, Gye Won Han, Justin Haugen, Lukasz Jaroszewski, Kevin K. Jin, Heath E. Klock, Mark W. Knuth, Eric Koesema, Mitchell D. Miller, Andrew T. Morse, Edward Nigoghossian, Linda Okach, Silvya Oommachen, Jessica Paulsen, Ron Reyes, Christopher L. Rife, Robert Schwarzenbacher, Henry van den Bedem, Aprilfawn White, Guenter Wolf, Keith O. Hodgson, John Wooley, Ashley M. Deacon, Adam Godzik, Scott A. Lesley, and Ian A. Wilson. Crystal structure of mtnx phosphatase from bacillus subtilis at 2.0 å resolution provides a structural basis for bipartite phosphomonoester hydrolysis of 2‐hydroxy‐3‐keto‐5‐methylthiopentenyl‐1‐phosphate. Proteins: Structure, 69:433-439, Nov 2007. URL: https://doi.org/10.1002/prot.21602, doi:10.1002/prot.21602. This article has 10 citations.

11. (sekowska2019revisitingthemethionine pages 1-2): Agnieszka Sekowska, Hiroki Ashida, and Antoine Danchin. Revisiting the methionine salvage pathway and its paralogues. Microbial Biotechnology, 12:77-97, Oct 2019. URL: https://doi.org/10.1111/1751-7915.13324, doi:10.1111/1751-7915.13324. This article has 81 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Enoph-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. camille2012functionalidentificationof pages 1-3
2. wang2005purificationcrystallizationand pages 1-2
3. chang2023labelfreequantitativeproteomics pages 8-10
4. majumder2024thepivotalrole pages 3-4
5. pirkov2008acompleteinventory pages 1-2
6. sekowska2019revisitingthemethionine pages 9-10
7. xu2007crystalstructureof pages 4-6
8. pirkov2008acompleteinventory pages 2-4
9. pirkov2008acompleteinventory pages 4-5
10. xu2007crystalstructureof pages 1-3
11. sekowska2019revisitingthemethionine pages 1-2
12. UniProt record
13. FlyBase record
14. https://www.uniprot.org/uniprotkb/Q9VN95/entry
15. https://flybase.org/reports/FBgn0037305.html
16. https://doi.org/10.1107/S174430910501184X
17. https://doi.org/10.1002/prot.21602
18. https://doi.org/10.1111/j.1742-4658.2008.06552.x
19. https://doi.org/10.1371/journal.pone.0052877
20. https://doi.org/10.1111/1751-7915.13324
21. https://doi.org/10.3389/fpls.2022.1098260
22. https://doi.org/10.3390/biom14111387
23. https://doi.org/10.1371/journal.pone.0052877,
24. https://doi.org/10.1111/j.1742-4658.2008.06552.x,
25. https://doi.org/10.1107/s174430910501184x,
26. https://doi.org/10.1111/1751-7915.13324,
27. https://doi.org/10.1002/prot.21602,
28. https://doi.org/10.3389/fpls.2022.1098260,
29. https://doi.org/10.3390/biom14111387,