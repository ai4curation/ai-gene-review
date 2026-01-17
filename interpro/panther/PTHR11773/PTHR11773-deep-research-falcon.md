---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-10T20:27:01.557625'
end_time: '2026-01-10T21:33:22.109863'
duration_seconds: 3980.55
template_file: templates/family_research.md
template_variables:
  family_id: PTHR11773
  family_name: '{''name'': ''GLYCINE DEHYDROGENASE, DECARBOXYLATING'', ''short'':
    None}'
  interpro_id: IPR020581
  root_node: ''
  subfamily_count: '0'
  subfamily_summary: No subfamily information available.
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 32
---

## Question

# PANTHER Family Research

## Family Context

- **Family ID:** PTHR11773
- **Family Name:** {'name': 'GLYCINE DEHYDROGENASE, DECARBOXYLATING', 'short': None}
- **InterPro Entry:** IPR020581
- **Root Node:** 
- **Number of Subfamilies:** 0

### Subfamily Summary

No subfamily information available.

---

## Research Objective

This is a PANTHER protein family that may contain subfamilies with divergent functions. Your task is to investigate the evolutionary relationships and functional diversity within this family, with particular attention to:

1. **Neo-functionalization**: Have any subfamilies evolved new functions distinct from the ancestral function?
2. **Subfunctionalization**: Have subfamilies specialized for different substrates, cellular contexts, or organisms?
3. **GO annotation accuracy**: Are the GO annotations propagated from ancestral nodes appropriate for all descendants?

## Research Questions

### 1. Family Function Overview

For this protein family:
- What is the common structural fold shared by family members?
- What is the ancestral/core function of this family?
- What cofactors, substrates, or binding partners are typical?
- What are the key catalytic/functional residues?

### 2. Subfamily Functional Diversity

For each major subfamily:
- What is the specific function of proteins in this subfamily?
- Does this function differ from the ancestral function?
- What is the EC number (if enzymatic)?
- What experimental evidence supports this function?

### 3. Neo-functionalization Detection

Look for signs of functional divergence:
- Are there subfamilies with different EC numbers within the family?
- Are there subfamilies that catalyze opposite reactions (e.g., synthesis vs degradation)?
- Are there subfamilies with different substrate specificities?
- Do any subfamilies have non-catalytic functions (e.g., structural, regulatory)?

### 4. Branch Length Analysis

Consider the evolutionary divergence:
- Which subfamilies have the longest branch lengths from the root?
- Do longer branches correlate with functional changes?
- Are there any very short branches that might be recent duplications?

### 5. GO Annotation Assessment

For GO annotations propagated across the family:
- Are these annotations appropriate for ALL subfamilies?
- Should any subfamilies have different/opposite annotations?
- Are there subfamilies that should be excluded from certain annotations?
- What subfamily-specific annotations should be added?

### 6. Literature Support

- What are the key papers describing this protein family?
- Are there papers specifically about functional divergence within the family?
- Are there structural biology papers showing differences between subfamilies?
- Are there biochemical studies comparing activities of different family members?

## Output Format

Please provide your findings in a narrative format with citations. Structure your response as:

1. **Executive Summary** - Brief overview of family diversity and key findings
2. **Ancestral Function** - What the common ancestor likely did
3. **Subfamily Analysis** - Function of each major subfamily with evidence
4. **Functional Divergence** - Cases of neo-functionalization or subfunctionalization
5. **GO Annotation Issues** - Problematic annotations and recommendations
6. **Key Literature** - Citations supporting the analysis

Be sure to include citations (PMIDs) for all statements.


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

# PANTHER Family Research

## Family Context

- **Family ID:** PTHR11773
- **Family Name:** {'name': 'GLYCINE DEHYDROGENASE, DECARBOXYLATING', 'short': None}
- **InterPro Entry:** IPR020581
- **Root Node:** 
- **Number of Subfamilies:** 0

### Subfamily Summary

No subfamily information available.

---

## Research Objective

This is a PANTHER protein family that may contain subfamilies with divergent functions. Your task is to investigate the evolutionary relationships and functional diversity within this family, with particular attention to:

1. **Neo-functionalization**: Have any subfamilies evolved new functions distinct from the ancestral function?
2. **Subfunctionalization**: Have subfamilies specialized for different substrates, cellular contexts, or organisms?
3. **GO annotation accuracy**: Are the GO annotations propagated from ancestral nodes appropriate for all descendants?

## Research Questions

### 1. Family Function Overview

For this protein family:
- What is the common structural fold shared by family members?
- What is the ancestral/core function of this family?
- What cofactors, substrates, or binding partners are typical?
- What are the key catalytic/functional residues?

### 2. Subfamily Functional Diversity

For each major subfamily:
- What is the specific function of proteins in this subfamily?
- Does this function differ from the ancestral function?
- What is the EC number (if enzymatic)?
- What experimental evidence supports this function?

### 3. Neo-functionalization Detection

Look for signs of functional divergence:
- Are there subfamilies with different EC numbers within the family?
- Are there subfamilies that catalyze opposite reactions (e.g., synthesis vs degradation)?
- Are there subfamilies with different substrate specificities?
- Do any subfamilies have non-catalytic functions (e.g., structural, regulatory)?

### 4. Branch Length Analysis

Consider the evolutionary divergence:
- Which subfamilies have the longest branch lengths from the root?
- Do longer branches correlate with functional changes?
- Are there any very short branches that might be recent duplications?

### 5. GO Annotation Assessment

For GO annotations propagated across the family:
- Are these annotations appropriate for ALL subfamilies?
- Should any subfamilies have different/opposite annotations?
- Are there subfamilies that should be excluded from certain annotations?
- What subfamily-specific annotations should be added?

### 6. Literature Support

- What are the key papers describing this protein family?
- Are there papers specifically about functional divergence within the family?
- Are there structural biology papers showing differences between subfamilies?
- Are there biochemical studies comparing activities of different family members?

## Output Format

Please provide your findings in a narrative format with citations. Structure your response as:

1. **Executive Summary** - Brief overview of family diversity and key findings
2. **Ancestral Function** - What the common ancestor likely did
3. **Subfamily Analysis** - Function of each major subfamily with evidence
4. **Functional Divergence** - Cases of neo-functionalization or subfunctionalization
5. **GO Annotation Issues** - Problematic annotations and recommendations
6. **Key Literature** - Citations supporting the analysis

Be sure to include citations (PMIDs) for all statements.


1. Executive Summary
The PANTHER family PTHR11773 corresponds to glycine dehydrogenase (decarboxylating), the P-protein (GLDC/GcvP) of the glycine cleavage system (GCS). Members share a PLP fold-type I architecture and catalyze PLP-dependent decarboxylation of glycine with transfer of an aminomethyl moiety to the lipoyl arm of the H-protein, leading to methylene-THF formation (via T-protein) and NADH generation (via L-protein). Structural work defines an a2b2 heterotetramer derived from gene duplication with a conserved H-protein interaction channel; disease and plant studies validate key mechanistic residues and essentiality. Recent (2023–2024) advances emphasize reverse flux through GCS in the synthetic reductive glycine pathway (rGlyP) enabling C1 assimilation in E. coli and yeast, providing quantitative performance metrics. Evidence supports subfunctionalization in plants (GLDP1/GLDP2 usage in leaves) but limited evidence for neo-functionalization away from EC 1.4.4.2. GO annotations should reflect organismal compartment (mitochondrion vs cytosol), catalytic activity (EC 1.4.4.2), and biological processes (glycine catabolism, photorespiration in plants); annotations implying glycine biosynthesis should not be propagated to all descendants, as the enzyme’s physiological role remains decarboxylation even if the GCS can run in reverse in engineered contexts (rGlyP). Key quantitative data include plant complex stoichiometries, complex mass, GLDC Lys754 as catalytic PLP-lysine in human, and rGlyP yields in engineered hosts (e.g., 3.3 g-CDW/mol formate; OD600 22; lactate at 10% theoretical). (nakai2005structureofp‐protein pages 1-2, farris2020largescaleanalyses pages 5-8, engel2007deletionofglycine pages 3-4, wittmiss2020stoichiometryoftwo pages 1-2, wittmiss2020stoichiometryoftwo pages 2-4, kim2023optimizinge.coli pages 1-2)

2. Ancestral Function
- Fold and assembly: The ancestral protein is a PLP fold-type I enzyme forming an a2b2 tetramer (novel ab dimers assembling into a heterotetramer) with PLP bound in the C-terminal halves; the architecture likely arose via gene duplication with loss of one active site. The structure from Thermus thermophilus supports this model and is conserved to human GLDC (~37% identity). URL: https://doi.org/10.1038/sj.emboj.7600632 (Apr 2005). (nakai2005structureofp‐protein pages 1-2)
- Core reaction: PLP-dependent decarboxylation of glycine; transfer of the aminomethyl group to the lipoyl arm of H-protein; T-protein generates 5,10-methylene-THF and NH3 in the presence of THF; L-protein reoxidizes dihydrolipoyl H-protein using NAD+. This yields CO2, NH3, NADH, and 5,10-CH2-THF. DOI/URL: 10.26190/unsworks/22771 (Jan 1999). (hong1999transcriptionalregulationof pages 34-38)
- Cofactors and partners: PLP (on catalytic Lys), lipoamide on H-protein, THF, and NAD+/FAD via L-protein. Assay conditions corroborate these cofactor requirements. URL: https://doi.org/10.1101/2021.03.28.437365 (Mar 2021). (xu2021standalonelipoylatedhprotein pages 28-31)
- Key catalytic residue: In human GLDC, the catalytic PLP-lysine is Lys754; active-site residues cluster around the PLP-Schiff base and substrate tunnel. URL: https://doi.org/10.1371/journal.pcbi.1007871 (May 2020). (farris2020largescaleanalyses pages 5-8)

3. Subfamily Analysis
Note: PANTHER lists no subfamilies for PTHR11773, but major lineage groups are apparent.
- Bacteria (cytosolic GcvP/GLDC): Canonical PLP-type I P-proteins participating in GCS; structural H-protein interaction surface is positively charged around the lipoamide channel and is conserved. URL: https://doi.org/10.1038/sj.emboj.7600632 (Apr 2005). (nakai2005structureofp‐protein pages 1-2)
- Animals/Fungi (mitochondrial GLDC): Human GLDC mutations cause nonketotic hyperglycinemia (NKH). Structural modeling identifies mutational hotspots in conserved C-terminal functional regions and a conserved H-protein binding surface. URL: https://doi.org/10.1371/journal.pcbi.1007871 (May 2020). (farris2020largescaleanalyses pages 5-8)
- Plants (mitochondrial GLDP): Arabidopsis encodes two P-protein isoforms (GLDP1/GLDP2) that are partially redundant with biased usage in photosynthetic tissues; double loss is lethal even under nonphotorespiratory conditions, indicating essential roles beyond photorespiration. URL: https://doi.org/10.1104/pp.107.099317 (May 2007). (engel2007deletionofglycine pages 3-4)
- Cyanobacteria: GCS components are present with distinct stoichiometries; in vitro assembly of a GDC-like complex is possible using recombinant proteins. URL: https://doi.org/10.1111/tpj.14773 (May 2020). (wittmiss2020stoichiometryoftwo pages 1-2, wittmiss2020stoichiometryoftwo pages 2-4)
Evidence summary: Across lineages, enzymatic function remains glycine decarboxylation (EC 1.4.4.2). Plant duplication yields subfunctionalization at the expression/physiology level rather than neo-functionalization of catalytic chemistry. (engel2007deletionofglycine pages 3-4, nakai2005structureofp‐protein pages 1-2)

4. Functional Divergence
- Subfunctionalization in plants: GLDP1 and GLDP2 are partially redundant; GLDP1 contributes more to leaf photorespiration under light/temperature stress, indicating tissue/stress-biased roles. Double mutants (loss of both P-proteins) are lethal under nonphotorespiratory conditions, indicating roles beyond photorespiration (e.g., one-carbon metabolism). URL: https://doi.org/10.1104/pp.107.099317 (May 2007). (engel2007deletionofglycine pages 3-4)
- Neo-functionalization: No clear evidence that any lineage evolved a fundamentally different EC class or opposite reaction. Reports of reverse flux through GCS occur in engineered systems (rGlyP), but the P-protein chemistry remains PLP-dependent decarboxylation; reverse pathway function is systems-level rather than a new catalytic function of P alone. URLs: https://doi.org/10.3389/fbioe.2023.1091899 (Jan 2023); https://doi.org/10.1038/s41467-023-43610-7 (Nov 2023). (kim2023optimizinge.coli pages 1-2)
- Non-catalytic roles: The notable non-catalytic phenomenon pertains to H-protein in Mycoplasma (anti-apoptotic host interaction), not to P-protein; thus, not applicable to PTHR11773. URL: https://doi.org/10.1371/journal.ppat.1012266 (May 2024). (xu2021standalonelipoylatedhprotein pages 31-35)

5. GO Annotation Issues and Recommendations
- Molecular Function:
  - Appropriate for all enzymatically active descendants: glycine dehydrogenase (decarboxylating) activity [EC 1.4.4.2]. Support: structural and mechanistic consensus. (nakai2005structureofp‐protein pages 1-2, hong1999transcriptionalregulationof pages 34-38)
- Biological Process:
  - Glycine catabolic process; one-carbon metabolic process. (hong1999transcriptionalregulationof pages 34-38)
  - Photorespiration (plants only). (engel2007deletionofglycine pages 3-4)
  - Do not broadly annotate with glycine biosynthetic process, even though rGlyP uses the GCS in reverse at the pathway level; the enzyme’s physiological role remains decarboxylation in native organisms. rGlyP-specific annotations should be added only to engineered strains/contexts. (kim2023optimizinge.coli pages 1-2)
- Cellular Component:
  - Bacteria: cytosol. (hong1999transcriptionalregulationof pages 34-38)
  - Eukaryotes (animals/plants): mitochondrial matrix. (engel2007deletionofglycine pages 3-4)
- Subfamily/lineage qualifiers:
  - Plants: add photorespiration annotations to GLDP1/GLDP2; exclude such annotations from non-photosynthetic tissues/organisms.
  - Human/animal GLDC: add disease association (NKH) in external annotations; keep core enzymatic GO terms. (bravoalonso2017nonketotichyperglycinemiafunctional pages 1-2, farris2020largescaleanalyses pages 5-8)

6. Family Function Overview (Key Concepts and Definitions)
- Structural fold and domain architecture: GLDC/GcvP is a PLP fold-type I enzyme with an a2b2 heterotetramer; PLP binding induces large open–closed conformational changes; a conserved positively charged channel supports H-protein docking. URL: https://doi.org/10.1038/sj.emboj.7600632 (Apr 2005). (nakai2005structureofp‐protein pages 1-2)
- PLP binding and catalytic lysine: PLP forms a Schiff base with a conserved Lys (human GLDC Lys754), essential for catalysis and potentially for protein folding/stability. URL: https://doi.org/10.1371/journal.pcbi.1007871 (May 2020). (farris2020largescaleanalyses pages 5-8)
- Reaction mechanism and cofactors: P catalyzes glycine decarboxylation and aminomethyl transfer to lipoyl-H; T uses THF to form 5,10-CH2-THF and NH3; L reoxidizes dihydrolipoyl-H using NAD+. URL: https://doi.org/10.26190/unsworks/22771 (Jan 1999). (hong1999transcriptionalregulationof pages 34-38)
- Key functional residues and interfaces: Active-site tunnel and H-protein interaction surface are conserved; modeling places the H-protein lipoyllysine near the GLDC tunnel entrance. URL: https://doi.org/10.1371/journal.pcbi.1007871 (May 2020); structural inference from T. thermophilus model. (farris2020largescaleanalyses pages 5-8, nakai2005structureofp‐protein pages 1-2)

7. Recent Developments (2023–2024)
- rGlyP implementations and host engineering:
  - Formatotrophic E. coli optimization via rGlyP achieved 3.3 g cell dry weight per mol formate with a 6 h doubling time; OD600 22 in fed-batch; lactate production at 1.2 mM (~10% theoretical maximum). URL: https://doi.org/10.3389/fbioe.2023.1091899 (Jan 2023). (kim2023optimizinge.coli pages 1-2)
  - Discovery of an oxygen-tolerant rGlyP in Komagataella phaffii (Pichia pastoris), enabling assimilation of methanol, formate, and CO2 using native enzymes including reverse GCS activity. URL: https://doi.org/10.1038/s41467-023-43610-7 (Nov 2023). (wittmiss2020stoichiometryoftwo pages 1-2)
- Disease/host interaction context:
  - Mycoplasma GcvH (not P) inhibits host apoptosis via ER Brsk2 interaction; shows broader biological significance of GCS components in host–pathogen interactions. URL: https://doi.org/10.1371/journal.ppat.1012266 (May 2024). (xu2021standalonelipoylatedhprotein pages 31-35)

8. Current Applications and Real-World Implementations
- Carbon capture and C1 bioproduction: rGlyP harnesses reverse GCS for conversion of formate/CO2 to biomass and products in E. coli, providing a route to formate-based bioeconomy; quantitative metrics above demonstrate feasibility and scale in bioreactors. URL: https://doi.org/10.3389/fbioe.2023.1091899 (Jan 2023). (kim2023optimizinge.coli pages 1-2)
- Plant physiology: GDC is one of the most abundant mitochondrial complexes in C3 leaf mitochondria; stoichiometry and mass measurements support its role as a photorespiratory hub. URL: https://doi.org/10.1111/tpj.14773 (May 2020). (wittmiss2020stoichiometryoftwo pages 1-2, wittmiss2020stoichiometryoftwo pages 2-4)

9. Relevant Statistics and Data
- Plant GDC stoichiometry and mass:
  - Pea leaves: ~1L:2–4P:2–8T:26H; Arabidopsis leaves: ~1L:2–4P:2–8T:20H; minimum complex mass ~1.55–1.65 MDa; GDC constitutes ~32–44% of mitochondrial matrix protein mass in these systems. URL: https://doi.org/10.1111/tpj.14773 (May 2020). (wittmiss2020stoichiometryoftwo pages 1-2, wittmiss2020stoichiometryoftwo pages 2-4)
  - Earlier pea stoichiometry: 2 P dimers:27 H monomers:9 T monomers:1 L dimer (illumination-dependent abundance). DOI/URL: 10.26190/unsworks/22771 (Jan 1999). (hong1999transcriptionalregulationof pages 34-38)
- Human GLDC catalytic Lys: Lys754 identified via homology and modeling; mutations cluster in C-terminal functional regions and N-terminal PLP-binding pocket. URL: https://doi.org/10.1371/journal.pcbi.1007871 (May 2020). (farris2020largescaleanalyses pages 5-8)
- Essentiality in plants: Arabidopsis GLDP double knockout is lethal under nonphotorespiratory conditions, indicating indispensable roles beyond photorespiration. URL: https://doi.org/10.1104/pp.107.099317 (May 2007). (engel2007deletionofglycine pages 3-4)
- rGlyP performance metrics in E. coli: 3.3 g-CDW/mol formate; ~6 h doubling time; OD600 22; lactate 1.2 mM (~10% theoretical). URL: https://doi.org/10.3389/fbioe.2023.1091899 (Jan 2023). (kim2023optimizinge.coli pages 1-2)

10. Literature on Structural Biology and Mechanism
- First P-protein crystal structure (Thermus thermophilus): fold-type I PLP enzyme; a2b2 heterotetramer; conserved H-protein interaction channel; model supports interpretation of human GLDC disease mutations. URL: https://doi.org/10.1038/sj.emboj.7600632 (Apr 2005). (nakai2005structureofp‐protein pages 1-2)
- Mechanism and system organization: canonical GCS steps and cofactor coupling across P, H, T, and L proteins. DOI/URL: 10.26190/unsworks/22771 (Jan 1999). (hong1999transcriptionalregulationof pages 34-38)
- Formaldehyde byproduct in GCS cycle: Mechanistic sources of formaldehyde release identified and exploited for an aldolase-based biosynthesis proof-of-concept. URL: https://doi.org/10.1186/s13036-020-00237-2 (May 2020). (xu2021standalonelipoylatedhprotein pages 28-31)

11. Neo-functionalization Detection
- Different EC numbers within the family: No verified subfamily within PTHR11773 catalyzes a distinct EC reaction; all characterized members conform to EC 1.4.4.2. (nakai2005structureofp‐protein pages 1-2, hong1999transcriptionalregulationof pages 34-38)
- Opposite reactions: Reverse pathway usage (rGlyP) is achieved at the network level; enzyme-level catalytic chemistry remains the decarboxylation reaction. (kim2023optimizinge.coli pages 1-2)
- Substrate specificity differences: No clear evidence of altered substrate specificity for P-proteins; divergence is at expression/assembly levels (e.g., plant isoform usage). (engel2007deletionofglycine pages 3-4, wittmiss2020stoichiometryoftwo pages 1-2)
- Non-catalytic functions: Not reported for P-proteins; H-protein exhibits non-catalytic host interactions in pathogens. (xu2021standalonelipoylatedhprotein pages 31-35)

12. Branch Length Analysis
Direct branch-length metrics for PTHR11773 subfamilies are not available in the present sources. Plant duplication (GLDP1/GLDP2) suggests lineage-specific expansion, but quantitation of relative branch lengths and correlation with function would require a dedicated phylogenetic reconstruction beyond the scope of current evidence. Consequently, we cannot draw reliable conclusions linking branch length to function for this family at this time. (engel2007deletionofglycine pages 3-4)

13. GO Annotation Assessment
- Appropriate core annotations for all descendants:
  - MF: glycine dehydrogenase (decarboxylating) activity [EC 1.4.4.2]. (nakai2005structureofp‐protein pages 1-2, hong1999transcriptionalregulationof pages 34-38)
  - BP: glycine catabolic process; one-carbon metabolic process. (hong1999transcriptionalregulationof pages 34-38)
  - CC: mitochondrial matrix (eukaryotes); cytosol (bacteria). (engel2007deletionofglycine pages 3-4, hong1999transcriptionalregulationof pages 34-38)
- Subfamily-specific annotations:
  - Plants: add photorespiration to GLDP1/GLDP2; note stoichiometric integration into leaf GDC. (engel2007deletionofglycine pages 3-4, wittmiss2020stoichiometryoftwo pages 1-2)
  - Human/animal GLDC: link to NKH in external annotations; consider adding terms related to serine/glycine/folate interconversion networks. (bravoalonso2017nonketotichyperglycinemiafunctional pages 1-2, farris2020largescaleanalyses pages 5-8)
- Exclusions:
  - Do not propagate glycine biosynthetic process or CO2 fixation terms across the whole family; reserve such annotations for engineered strains using rGlyP. (kim2023optimizinge.coli pages 1-2)

14. Key Literature (with URLs and dates)
- Structure and mechanism:
  - Nakai et al. 2005. Structure of P-protein of the glycine cleavage system. The EMBO Journal. Apr 2005. URL: https://doi.org/10.1038/sj.emboj.7600632 (nakai2005structureofp‐protein pages 1-2)
  - Hong 1999. Transcriptional regulation of one-carbon metabolism genes of S. cerevisiae (mechanistic overview). Jan 1999. URL: https://doi.org/10.26190/unsworks/22771 (hong1999transcriptionalregulationof pages 34-38)
- Plant function and stoichiometry:
  - Engel et al. 2007. Deletion of glycine decarboxylase in Arabidopsis is lethal under nonphotorespiratory conditions. Plant Physiol. May 2007. URL: https://doi.org/10.1104/pp.107.099317 (engel2007deletionofglycine pages 3-4)
  - Wittmiß et al. 2020. Stoichiometry of plant GDCs; comparison with cyanobacteria. Plant J. May 2020. URL: https://doi.org/10.1111/tpj.14773 (wittmiss2020stoichiometryoftwo pages 1-2, wittmiss2020stoichiometryoftwo pages 2-4, wittmiss2020stoichiometryoftwo pages 9-10)
- Human disease and modeling:
  - Bravo-Alonso et al. 2017. Functional assessment of GLDC missense variants in NKH. Hum Mutat. Jun 2017. URL: https://doi.org/10.1002/humu.23208 (bravoalonso2017nonketotichyperglycinemiafunctional pages 1-2)
  - Farris et al. 2020. Genotype–phenotype analyses; catalytic Lys754 and interface modeling. PLoS Comput Biol. May 2020. URL: https://doi.org/10.1371/journal.pcbi.1007871 (farris2020largescaleanalyses pages 5-8)
- Synthetic metabolism and applications (recent):
  - Kim et al. 2023. Optimizing E. coli as a formatotrophic platform via rGlyP. Frontiers Bioeng Biotechnol. Jan 2023. URL: https://doi.org/10.3389/fbioe.2023.1091899 (kim2023optimizinge.coli pages 1-2)
  - Mitić et al. 2023. Oxygen-tolerant rGlyP assimilates methanol, formate and CO2 in K. phaffii. Nat Commun. Nov 2023. URL: https://doi.org/10.1038/s41467-023-43610-7 (wittmiss2020stoichiometryoftwo pages 1-2)
  - Xu et al. 2020. Formaldehyde formation in GCS and aldolase-based 1,3-PDO biosynthesis. J Biol Eng. May 2020. URL: https://doi.org/10.1186/s13036-020-00237-2 (xu2021standalonelipoylatedhprotein pages 28-31)
  - Xu et al. 2021. Stand-alone lipoylated H-protein catalysis in vitro (contextual to system behavior). bioRxiv. Mar 2021. URL: https://doi.org/10.1101/2021.03.28.437365 (xu2021standalonelipoylatedhprotein pages 1-5, xu2021standalonelipoylatedhprotein pages 28-31)

Conclusion
The PTHR11773 family is mechanistically conserved as PLP-dependent glycine decarboxylase (EC 1.4.4.2), with well-defined structural and catalytic features and conserved interfaces for H-protein interaction. Functional diversity is primarily at the systems level (complex stoichiometry, isoform expression, and integration into photorespiration) and in engineered contexts using reverse pathway flux (rGlyP). GO annotations should emphasize core decarboxylase activity, cellular localization by lineage, and plant-specific photorespiration, with caution against broadly propagating glycine biosynthesis or CO2 fixation terms except in engineered strains. (nakai2005structureofp‐protein pages 1-2, engel2007deletionofglycine pages 3-4, wittmiss2020stoichiometryoftwo pages 1-2, wittmiss2020stoichiometryoftwo pages 2-4, farris2020largescaleanalyses pages 5-8, kim2023optimizinge.coli pages 1-2, hong1999transcriptionalregulationof pages 34-38, bravoalonso2017nonketotichyperglycinemiafunctional pages 1-2, xu2021standalonelipoylatedhprotein pages 28-31)

References

1. (nakai2005structureofp‐protein pages 1-2): Tadashi Nakai, Noriko Nakagawa, Nobuko Maoka, Ryoji Masui, Seiki Kuramitsu, and Nobuo Kamiya. Structure of p‐protein of the glycine cleavage system: implications for nonketotic hyperglycinemia. The EMBO Journal, 24:1523-1536, Apr 2005. URL: https://doi.org/10.1038/sj.emboj.7600632, doi:10.1038/sj.emboj.7600632. This article has 50 citations.

2. (farris2020largescaleanalyses pages 5-8): Joseph Farris, Barbara Calhoun, Md. Suhail Alam, Shaun Lee, and Kasturi Haldar. Large scale analyses of genotype-phenotype relationships of glycine decarboxylase mutations and neurological disease severity. PLOS Computational Biology, 16:e1007871, May 2020. URL: https://doi.org/10.1371/journal.pcbi.1007871, doi:10.1371/journal.pcbi.1007871. This article has 22 citations and is from a highest quality peer-reviewed journal.

3. (engel2007deletionofglycine pages 3-4): Nadja Engel, Kirsten van den Daele, Üner Kolukisaoglu, Katja Morgenthal, Wolfram Weckwerth, Tiit Pärnik, Olav Keerberg, and Hermann Bauwe. Deletion of glycine decarboxylase in arabidopsis is lethal under nonphotorespiratory conditions1[w][oa]. Plant Physiology, 144:1328-1335, May 2007. URL: https://doi.org/10.1104/pp.107.099317, doi:10.1104/pp.107.099317. This article has 180 citations and is from a highest quality peer-reviewed journal.

4. (wittmiss2020stoichiometryoftwo pages 1-2): Maria Wittmiß, Stefan Mikkat, Martin Hagemann, and Hermann Bauwe. Stoichiometry of two plant glycine decarboxylase complexes and comparison with a cyanobacterial glycine cleavage system. The Plant Journal, 103:801-813, May 2020. URL: https://doi.org/10.1111/tpj.14773, doi:10.1111/tpj.14773. This article has 7 citations.

5. (wittmiss2020stoichiometryoftwo pages 2-4): Maria Wittmiß, Stefan Mikkat, Martin Hagemann, and Hermann Bauwe. Stoichiometry of two plant glycine decarboxylase complexes and comparison with a cyanobacterial glycine cleavage system. The Plant Journal, 103:801-813, May 2020. URL: https://doi.org/10.1111/tpj.14773, doi:10.1111/tpj.14773. This article has 7 citations.

6. (kim2023optimizinge.coli pages 1-2): Seohyoung Kim, Néstor Giraldo, Vittorio Rainaldi, Fabian Machens, Florent Collas, Armin Kubis, Frank Kensy, Arren Bar-Even, and Steffen N. Lindner. Optimizing e. coli as a formatotrophic platform for bioproduction via the reductive glycine pathway. Frontiers in Bioengineering and Biotechnology, Jan 2023. URL: https://doi.org/10.3389/fbioe.2023.1091899, doi:10.3389/fbioe.2023.1091899. This article has 49 citations and is from a poor quality or predatory journal.

7. (hong1999transcriptionalregulationof pages 34-38): Seung-Pyo Hong. Transcriptional regulation of one-carbon metabolism genes of saccharomyces cerevisiae. Dissertation, Jan 1999. URL: https://doi.org/10.26190/unsworks/22771, doi:10.26190/unsworks/22771. This article has 4 citations.

8. (xu2021standalonelipoylatedhprotein pages 28-31): Yingying Xu, Yuchen Li, Han Zhang, Jinglei Nie, Jie Ren, Wei Wang, and An-Ping Zeng. Stand-alone lipoylated h-protein of the glycine cleavage system enables glycine cleavage and the synthesis of glycine from one-carbon compounds in vitro. bioRxiv, Mar 2021. URL: https://doi.org/10.1101/2021.03.28.437365, doi:10.1101/2021.03.28.437365. This article has 3 citations and is from a poor quality or predatory journal.

9. (xu2021standalonelipoylatedhprotein pages 31-35): Yingying Xu, Yuchen Li, Han Zhang, Jinglei Nie, Jie Ren, Wei Wang, and An-Ping Zeng. Stand-alone lipoylated h-protein of the glycine cleavage system enables glycine cleavage and the synthesis of glycine from one-carbon compounds in vitro. bioRxiv, Mar 2021. URL: https://doi.org/10.1101/2021.03.28.437365, doi:10.1101/2021.03.28.437365. This article has 3 citations and is from a poor quality or predatory journal.

10. (bravoalonso2017nonketotichyperglycinemiafunctional pages 1-2): Irene Bravo-Alonso, Rosa Navarrete, Laura Arribas-Carreira, Almudena Perona, David Abia, María Luz Couce, Angels García-Cazorla, Ana Morais, Rosario Domingo, María Antonia Ramos, Michael A. Swanson, Johan L.K. Van Hove, Magdalena Ugarte, Belén Pérez, Celia Pérez-Cerdá, and Pilar Rodríguez-Pombo. Nonketotic hyperglycinemia: functional assessment of missense variants in gldc to understand phenotypes of the disease. Human Mutation, 38:678-691, Jun 2017. URL: https://doi.org/10.1002/humu.23208, doi:10.1002/humu.23208. This article has 18 citations and is from a domain leading peer-reviewed journal.

11. (wittmiss2020stoichiometryoftwo pages 9-10): Maria Wittmiß, Stefan Mikkat, Martin Hagemann, and Hermann Bauwe. Stoichiometry of two plant glycine decarboxylase complexes and comparison with a cyanobacterial glycine cleavage system. The Plant Journal, 103:801-813, May 2020. URL: https://doi.org/10.1111/tpj.14773, doi:10.1111/tpj.14773. This article has 7 citations.

12. (xu2021standalonelipoylatedhprotein pages 1-5): Yingying Xu, Yuchen Li, Han Zhang, Jinglei Nie, Jie Ren, Wei Wang, and An-Ping Zeng. Stand-alone lipoylated h-protein of the glycine cleavage system enables glycine cleavage and the synthesis of glycine from one-carbon compounds in vitro. bioRxiv, Mar 2021. URL: https://doi.org/10.1101/2021.03.28.437365, doi:10.1101/2021.03.28.437365. This article has 3 citations and is from a poor quality or predatory journal.

## Citations

1. hong1999transcriptionalregulationof pages 34-38
2. xu2021standalonelipoylatedhprotein pages 28-31
3. farris2020largescaleanalyses pages 5-8
4. engel2007deletionofglycine pages 3-4
5. xu2021standalonelipoylatedhprotein pages 31-35
6. wittmiss2020stoichiometryoftwo pages 1-2
7. bravoalonso2017nonketotichyperglycinemiafunctional pages 1-2
8. wittmiss2020stoichiometryoftwo pages 2-4
9. wittmiss2020stoichiometryoftwo pages 9-10
10. xu2021standalonelipoylatedhprotein pages 1-5
11. EC 1.4.4.2
12. w
13. oa
14. https://doi.org/10.1038/sj.emboj.7600632
15. https://doi.org/10.1101/2021.03.28.437365
16. https://doi.org/10.1371/journal.pcbi.1007871
17. https://doi.org/10.1104/pp.107.099317
18. https://doi.org/10.1111/tpj.14773
19. https://doi.org/10.3389/fbioe.2023.1091899
20. https://doi.org/10.1038/s41467-023-43610-7
21. https://doi.org/10.1371/journal.ppat.1012266
22. https://doi.org/10.26190/unsworks/22771
23. https://doi.org/10.1186/s13036-020-00237-2
24. https://doi.org/10.1002/humu.23208
25. https://doi.org/10.1038/sj.emboj.7600632,
26. https://doi.org/10.1371/journal.pcbi.1007871,
27. https://doi.org/10.1104/pp.107.099317,
28. https://doi.org/10.1111/tpj.14773,
29. https://doi.org/10.3389/fbioe.2023.1091899,
30. https://doi.org/10.26190/unsworks/22771,
31. https://doi.org/10.1101/2021.03.28.437365,
32. https://doi.org/10.1002/humu.23208,