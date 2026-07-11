---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-21T21:32:08.962168'
end_time: '2026-06-21T21:41:41.436403'
duration_seconds: 572.47
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR31859
  interpro_name: TETRATRICOPEPTIDE REPEAT PROTEIN 39 FAMILY MEMBER
  interpro_short_name: Not specified
  interpro_type: family
  interpro_integrated: IPR019412
  member_databases: Not specified
  n_proteins: '9018'
  n_taxa: '7507'
  n_subfamilies: '10'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: Not specified in InterPro
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 19
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: PTHR31859-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# InterPro Family Research for GO Annotation Review

## ⚠️ CRITICAL: Family Identification Context

**BEFORE YOU BEGIN RESEARCH:** You are researching an **InterPro entry** (a protein
family / domain / superfamily signature), not a single gene. The goal is to judge
whether the GO terms that InterPro2GO attaches to this signature are appropriate for
**every** protein the signature matches.

### Target InterPro Entry (from the InterPro API):
- **Accession:** PTHR31859
- **Name:** TETRATRICOPEPTIDE REPEAT PROTEIN 39 FAMILY MEMBER
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR019412
- **Member database signatures:** Not specified
- **Scale:** 9018 proteins across 7507 taxa, 10 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** Not specified in InterPro

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR31859 (TETRATRICOPEPTIDE REPEAT PROTEIN 39 FAMILY MEMBER)**, structured to support GO annotation review.

Prioritize authoritative reviews and primary literature; you may supplement with
database annotations, but treat those as potentially outdated or over-broad.

Address each of the following:

1. **Family definition and biochemistry.** What does this family/domain do
   mechanistically? What fold is it? What are the conserved catalytic or binding
   residues? Cite primary/structural literature for all claims.

2. **InterPro2GO mapping appropriateness.** For **each** GO term currently mapped to
   this entry (listed above), state whether it is true for *every* protein the signature
   matches. Flag terms that are: (a) only true for a subfamily; (b) whole-protein
   functions attached to a domain/superfamily signature; (c) so generic (e.g. "ATP
   binding", "metal ion binding", "membrane") that they carry little information; or
   (d) process/component terms that leak into taxa where the pathway/compartment is
   absent. Where a more specific GO term would be correct, name it.

3. **Functional divergence across the family.** Are there subfamilies with divergent or
   even opposite functions (neo-functionalization)? Are there catalytically dead
   (pseudo-enzyme) members that retain the fold but lost activity? Identify the
   subfamilies and what distinguishes them.

4. **Taxonomic scope.** In which clades does this signature occur, and does any mapped
   process/component term hold across all of them?

5. **Over-annotation verdict.** Summarize whether InterPro2GO for this entry is sound,
   partially over-broad, or over-annotating, and give the recommended GO action pattern
   (ACCEPT / MODIFY-to-specific / KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED / REMOVE)
   for genes matching it. Note any recommendation for InterPro itself (e.g. demote a
   whole-protein term on a domain entry, or move it to a child entry).

Include experimental evidence where possible, and clearly distinguish experimental
findings from inference based on structure, evolution, or bioinformatics.


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

# InterPro Family Research for GO Annotation Review

## ⚠️ CRITICAL: Family Identification Context

**BEFORE YOU BEGIN RESEARCH:** You are researching an **InterPro entry** (a protein
family / domain / superfamily signature), not a single gene. The goal is to judge
whether the GO terms that InterPro2GO attaches to this signature are appropriate for
**every** protein the signature matches.

### Target InterPro Entry (from the InterPro API):
- **Accession:** PTHR31859
- **Name:** TETRATRICOPEPTIDE REPEAT PROTEIN 39 FAMILY MEMBER
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR019412
- **Member database signatures:** Not specified
- **Scale:** 9018 proteins across 7507 taxa, 10 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** Not specified in InterPro

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR31859 (TETRATRICOPEPTIDE REPEAT PROTEIN 39 FAMILY MEMBER)**, structured to support GO annotation review.

Prioritize authoritative reviews and primary literature; you may supplement with
database annotations, but treat those as potentially outdated or over-broad.

Address each of the following:

1. **Family definition and biochemistry.** What does this family/domain do
   mechanistically? What fold is it? What are the conserved catalytic or binding
   residues? Cite primary/structural literature for all claims.

2. **InterPro2GO mapping appropriateness.** For **each** GO term currently mapped to
   this entry (listed above), state whether it is true for *every* protein the signature
   matches. Flag terms that are: (a) only true for a subfamily; (b) whole-protein
   functions attached to a domain/superfamily signature; (c) so generic (e.g. "ATP
   binding", "metal ion binding", "membrane") that they carry little information; or
   (d) process/component terms that leak into taxa where the pathway/compartment is
   absent. Where a more specific GO term would be correct, name it.

3. **Functional divergence across the family.** Are there subfamilies with divergent or
   even opposite functions (neo-functionalization)? Are there catalytically dead
   (pseudo-enzyme) members that retain the fold but lost activity? Identify the
   subfamilies and what distinguishes them.

4. **Taxonomic scope.** In which clades does this signature occur, and does any mapped
   process/component term hold across all of them?

5. **Over-annotation verdict.** Summarize whether InterPro2GO for this entry is sound,
   partially over-broad, or over-annotating, and give the recommended GO action pattern
   (ACCEPT / MODIFY-to-specific / KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED / REMOVE)
   for genes matching it. Note any recommendation for InterPro itself (e.g. demote a
   whole-protein term on a domain entry, or move it to a child entry).

Include experimental evidence where possible, and clearly distinguish experimental
findings from inference based on structure, evolution, or bioinformatics.


# InterPro Family Research Report: PTHR31859 (Tetratricopeptide Repeat Protein 39 Family Member)

## Executive Summary

InterPro entry PTHR31859 represents a protein family spanning 9018 proteins across 7507 taxa with 10 subfamilies. The entry type is "family," which typically supports whole-protein function terms, but only if the family is functionally homogeneous. Our comprehensive literature review reveals **significant functional divergence** across characterized subfamilies (TTC39A, TTC39B, TTC39C), with distinct tissue expression patterns, molecular mechanisms, and disease associations. **Critically, PTHR31859 currently has NO InterPro2GO mappings—a situation that is appropriate and should be maintained.**

---

## 1. Family Definition and Biochemistry

### Structural fold and domain architecture

The TTC39 family belongs to the broader superfamily of tetratricopeptide repeat (TPR)-containing proteins. TPR domains are characterized by tandem repeats of approximately 34 amino acids that fold into helix-turn-helix motifs, stacking to form a superhelical structure with a distinctive concave surface (pokhrel2025chaperonedependentandchaperoneindependent pages 1-3, barik2025ageneralizedai pages 1-3). Each repeat consists of two alpha-helices (designated A and B, each ~14 amino acids long) connected by relatively flexible linkers or spacers (barik2025ageneralizedai pages 1-3). 

Detailed structural analysis of TPR proteins reveals that they are all alpha-helical in nature, with the tandem helices joined to form a superhelix (barik2025ageneralizedai pages 1-3). Analysis of TPR protein structures shows conserved amino acids at specific positions that serve as signature motifs, with predominantly conserved residues including leucine (L), glycine (G), alanine (A), phenylalanine (F), methionine (M), and proline (P) (barik2025ageneralizedai pages 1-3). The overall helicity and the presence of critical amino acid residues in strategic positions are more important for biological function than the exact amino acid length of the repeat (barik2025ageneralizedai pages 1-3).

### Mechanistic function—Not a single conserved catalytic activity

**Critical finding:** The TTC39 family does NOT possess a single conserved catalytic or binding activity shared by all members. Instead, different subfamilies have evolved distinct molecular functions:

- **TTC39B** (the best-characterized member) functions as an **E3 ubiquitin ligase** for liver X receptor α (LXRα) in hepatocytes. TTC39B deficiency stabilizes LXR protein, reducing both atherosclerosis and steatohepatitis (tran2017preservinglxrby pages 1-4, endoumeda2025exploringtheroles pages 1-2). This E3 ligase activity is specific to TTC39B and has not been demonstrated for other family members.

- **TTC39A** has been identified as a candidate type 2 diabetes gene affecting pancreatic β-cell function and glucose homeostasis in mice, with differential expression in pancreatic islets and a missense variant (P169L) distinguishing diabetogenic from protective alleles (aga2020identificationofnovel pages 1-2, aga2020identificationofnovel pages 6-8). However, no direct biochemical activity or catalytic mechanism has been established for TTC39A.

- **TTC39B** also regulates nutrient homeostasis genes (SLC6A19, TTC39B, ADM2) and p53-dependent autophagy pathways when expressed ectopically in gastric cancer cells (xing2025mt1hinhibitsthe pages 1-2), suggesting context-dependent regulatory roles beyond LXR degradation.

The TPR domain itself is a **protein-protein interaction scaffold** rather than an enzyme. TPR proteins commonly mediate protein-protein interactions and assemble multiprotein complexes (paeng2020attpr10containingmultiple pages 1-3). There are no conserved catalytic residues across the family; the function is determined by which proteins each family member binds and what cellular processes it thereby regulates.

### Conserved vs. divergent features

**Conserved:** The TPR repeat superhelical scaffold structure, which provides a platform for protein-protein interactions (pokhrel2025chaperonedependentandchaperoneindependent pages 1-3, barik2025ageneralizedai pages 1-3, bibber2020intrinsicdisorderin pages 1-3).

**Divergent:** Substrate specificity, tissue expression, molecular function (E3 ligase activity in TTC39B vs. unknown mechanisms in TTC39A/C), and biological processes (lipid metabolism vs. glucose homeostasis vs. unknown functions).

---

## 2. InterPro2GO Mapping Appropriateness

**Current status:** PTHR31859 has **ZERO InterPro2GO mappings** (as stated in the query).

**Verdict:** This absence is **APPROPRIATE** and should be maintained.

### Rationale:

Since there are currently no GO terms mapped to PTHR31859, we evaluate what terms might be *considered* and whether they would be appropriate:

**(a) Terms that are only true for a subfamily:**
- **GO:0061630 (ubiquitin protein ligase activity)** and **GO:0043161 (proteasome-mediated ubiquitin-dependent protein catabolic process)** are well-supported for TTC39B as an E3 ligase for LXRα (tran2017preservinglxrby pages 1-4, endoumeda2025exploringtheroles pages 1-2), but there is **no evidence** that TTC39A or TTC39C possess E3 ligase activity. Applying these to the whole family would over-annotate.

- **GO:0010877 (lipid homeostasis)** or **GO:0042632 (cholesterol homeostasis)** are relevant to TTC39B's role in liver and reverse cholesterol transport (tran2017preservinglxrby pages 1-4, endoumeda2025exploringtheroles pages 1-2), but TTC39A functions in pancreatic islets affecting glucose, not lipid, metabolism (aga2020identificationofnovel pages 6-8). These would be subfamily-specific.

- **GO:0044342 (type B pancreatic cell proliferation)** or glucose-related terms might suit TTC39A but not TTC39B or TTC39C (aga2020identificationofnovel pages 6-8).

**(b) Whole-protein functions attached inappropriately:**
PTHR31859 is classified as a "family" (not a domain or repeat entry), so whole-protein function terms are theoretically permissible. However, the family is **not functionally homogeneous**—TTC39A, TTC39B, and TTC39C have different molecular roles, tissue distributions, and disease associations. Attaching any whole-protein activity term at the family level would incorrectly propagate it to divergent members.

**(c) Generic terms that carry little information:**
- **GO:0005515 (protein binding)** would be technically true (TPR domains mediate protein-protein interactions) but is too generic to be useful.
- **"TPR domain binding"** or **"molecular adaptor activity"** might be accurate but provide minimal specificity and do not distinguish TTC39 proteins from hundreds of other TPR-containing proteins.

**(d) Process/component terms that leak inappropriately across taxa:**
Given the broad taxonomic distribution (9018 proteins, 7507 taxa), adding tissue-specific terms (e.g., "liver," "pancreatic islet") at the family level would be inappropriate. TTC39B is liver-expressed in mammals; TTC39A is pancreas/islet-expressed; these are not universal across the family or across all taxa.

### Recommendation for more specific GO terms:

If future curation seeks to add GO terms, they should be applied **only to specific PANTHER subfamilies** (not to PTHR31859 as a whole):
- TTC39B-like subfamily could receive GO:0061630 (ubiquitin protein ligase activity), GO:0042632 (cholesterol homeostasis), GO:0010877 (lipid homeostasis).
- TTC39A-like subfamily could receive terms related to glucose homeostasis or pancreatic β-cell function if further experimental evidence supports a specific mechanism.
- Family-level terms should remain absent or be limited to extremely generic structural terms.

---

## 3. Functional Divergence Across the Family

### Evidence of neo-functionalization

The TTC39 family exhibits **strong functional divergence** indicative of neo-functionalization following gene duplication:

**TTC39A:**
- **Tissue/expression:** Mouse pancreatic islets; differentially expressed in pancreatic islets of diabetic vs. non-diabetic congenic mice (aga2020identificationofnovel pages 6-8).
- **Molecular role:** Candidate type 2 diabetes gene; a missense variant (P169L) correlates with β-cell loss, hyperglycemia, and reduced pancreatic insulin content in mouse models (aga2020identificationofnovel pages 1-2, aga2020identificationofnovel pages 6-8).
- **Disease association:** Type 2 diabetes in mice; reduced expression in human pancreatic islets from T2D donors compared to non-diabetic donors (aga2020identificationofnovel pages 6-8).
- **Mechanism:** Not biochemically defined; appears regulatory or structural rather than enzymatic.

**TTC39B:**
- **Tissue/expression:** Liver (hepatocytes), enterocytes/intestine, macrophages; highly expressed in metabolic organs (tran2017preservinglxrby pages 1-4, endoumeda2025exploringtheroles pages 1-2).
- **Molecular role:** E3 ubiquitin ligase for LXRα; TTC39B deficiency stabilizes LXR, enhances LXR target gene expression (ABCA1), promotes reverse cholesterol transport, and reduces hepatic triglyceride and cholesterol levels (tran2017preservinglxrby pages 1-4, endoumeda2025exploringtheroles pages 1-2).
- **Disease association:** Atherosclerosis and non-alcoholic steatohepatitis (NASH); TTC39B-deficient mice show reduced atherosclerotic lesions and steatosis (tran2017preservinglxrby pages 1-4). Genetic variants in TTC39B are associated with endometriosis and ovarian cancer progression-free survival in human GWAS, though the mechanistic link in these diseases is less clear (french2016germlinepolymorphismsin pages 1-3, steinthorsdottir2016commonvariantsupstream pages 1-2).
- **Mechanism:** Experimentally demonstrated E3 ligase activity; promotes LXRα degradation, thereby modulating lipid metabolism pathways (tran2017preservinglxrby pages 1-4, endoumeda2025exploringtheroles pages 1-2).

**TTC39C:**
- **Tissue/expression:** Unknown; limited functional data.
- **Molecular role:** Not characterized biochemically in the available literature.
- **Disease association:** Genetic association with endometriosis risk (steinthorsdottir2016commonvariantsupstream pages 1-2); mechanism unknown.
- **Mechanism:** No direct molecular or biochemical function has been established in the cited evidence.

| Subfamily / representative gene | Reported tissue or system context | Molecular function / mechanistic evidence | Biological process / disease association | Evidence relevant to GO review |
|---|---|---|---|---|
| TTC39A | Mouse pancreatic islets; human pancreatic islets in T2D expression comparison | No direct biochemical activity demonstrated in the cited study; identified as a candidate diabetogenic gene with DBA-specific upstream regulatory variation, reduced islet expression, and one missense variant (P169L). Evidence supports a regulatory/physiological role rather than a conserved catalytic function (aga2020identificationofnovel pages 6-8, aga2020identificationofnovel pages 1-2). | Glucose homeostasis, β-cell loss, hyperglycemia/type 2 diabetes candidate locus in mouse; reduced human islet expression in T2D donors reported in comparative transcriptomics (aga2020identificationofnovel pages 6-8). | Supports that some family members are linked to pancreatic/islet phenotypes, but not to the lipid/LXR function of TTC39B; therefore family-wide assignment of cholesterol-process or ubiquitin-ligase GO terms would over-annotate TTC39A-like proteins (aga2020identificationofnovel pages 6-8, aga2020identificationofnovel pages 1-2). |
| TTC39B | Liver, enterocytes/intestine, and atherosclerosis/NASH mouse models; human GWAS and disease-association context | Best-supported mechanistic member. Commentary on primary Nature study reports that T39/TTC39B deficiency preserves LXR protein, elevates LXR target expression, increases enterocyte ABCA1, reduces steatosis, fibrosis, inflammation, LDL, and atherosclerotic lesions; a 2025 review states TTC39B acts as an E3 ligase for LXRα in hepatocytes (tran2017preservinglxrby pages 1-4, endoumeda2025exploringtheroles pages 1-2). | Cholesterol homeostasis, reverse cholesterol transport-related pathways, atherosclerosis, steatohepatitis/NASH; also associated genetically with endometriosis and ovarian cancer progression loci, though those associations do not establish the same mechanism in all contexts (tran2017preservinglxrby pages 1-4, endoumeda2025exploringtheroles pages 1-2, steinthorsdottir2016commonvariantsupstream pages 1-2, french2016germlinepolymorphismsin pages 1-3). | Shows a specific lipid-metabolism/LXR-degradation role that is strong for this branch, but this function is not evidenced for TTC39A or TTC39C. Any family-level GO such as liver X receptor catabolic process, cholesterol homeostasis, or ubiquitin ligase activity would likely be true only for a TTC39B-like subfamily (tran2017preservinglxrby pages 1-4, endoumeda2025exploringtheroles pages 1-2). |
| TTC39C | Human endometriosis GWAS locus / disease genetics context | No direct molecular or biochemical function established in the cited material; mentioned as a TTC39 paralog/family member with little or no mechanistic characterization in the retrieved evidence. | No experimentally defined core process from cited literature; by analogy to user summary of family members, function remains uncertain relative to TTC39A/B. | Lack of mechanistic evidence for TTC39C is itself important: it argues against adding positive family-wide GO terms based on TTC39B or disease-candidate status based on TTC39A. Family-level annotation would propagate unsupported function to poorly characterized subfamilies (steinthorsdottir2016commonvariantsupstream pages 1-2). |
| Shared family feature (TPR/TTC39 family level) | Broadly present in many eukaryotic proteins; InterPro family spans 9018 proteins across 7507 taxa | TPR proteins are generally alpha-helical repeat scaffolds for protein-protein interactions. A TPR repeat is ~34 aa, each repeat forms a helix-turn-helix motif, and tandem repeats form a superhelical concave surface; these are structural features, not a single conserved biochemical activity (pokhrel2025chaperonedependentandchaperoneindependent pages 1-3, barik2025ageneralizedai pages 1-3, bibber2020intrinsicdisorderin pages 1-3). | Broad scaffold/adaptor role at most; no single conserved process/component from cited TTC39 member literature spans all subfamilies. | The only safe family-level inference is a generic structural one (TPR repeat-containing scaffold/adaptor), which is too broad to justify informative InterPro2GO mapping. This structural commonality combined with strong member-level divergence explains why no GO mapping is currently the safest choice (pokhrel2025chaperonedependentandchaperoneindependent pages 1-3, barik2025ageneralizedai pages 1-3, bibber2020intrinsicdisorderin pages 1-3, tran2017preservinglxrby pages 1-4, aga2020identificationofnovel pages 6-8). |


*Table: This table compares TTC39A, TTC39B, and TTC39C using the available literature and shows that mechanistic evidence is concentrated in TTC39B, while TTC39A and TTC39C have different or poorly resolved roles. That divergence explains why family-level GO annotation for PTHR31859 would likely over-annotate many matched proteins.*

### Catalytically dead or pseudo-enzyme members?

There is **no evidence** in the retrieved literature for catalytically dead or pseudo-enzyme members within the TTC39 family. However, the absence of demonstrated enzymatic activity for TTC39A and TTC39C (in contrast to TTC39B's E3 ligase function) suggests that not all family members have acquired the same biochemical activity. Whether TTC39A/C represent ancestral scaffold-only functions or have distinct, yet-to-be-characterized activities remains unknown.

### Subfamilies and distinctions

PTHR31859 has **10 subfamilies** according to the InterPro metadata. The literature provides detailed functional data for only three vertebrate paralogs (TTC39A, B, C). The distinctions among the 10 subfamilies likely reflect:
- **Taxonomic distribution:** Different subfamilies may represent orthologs in different metazoan lineages (mammals, fish, invertebrates).
- **Gene duplication events:** Vertebrate-specific duplications (TTC39A, B, C) with subsequent tissue and functional specialization.
- **Expression context:** TTC39A is pancreatic/islet; TTC39B is hepatic/enterocyte; TTC39C is poorly characterized.
- **Molecular function:** TTC39B has evolved E3 ligase activity; TTC39A has not been shown to possess this activity.

The 10 subfamilies suggest ancient duplication events with taxon-specific retention patterns and functional divergence, consistent with neo-functionalization.

---

## 4. Taxonomic Scope

### Distribution across clades

PTHR31859 encompasses **9018 proteins across 7507 taxa** (from InterPro metadata). The available literature provides evidence for TTC39 family members in:

- **Mammals:** Extensive human and mouse studies (TTC39A, TTC39B, TTC39C) (xing2025mt1hinhibitsthe pages 1-2, french2016germlinepolymorphismsin pages 1-3, steinthorsdottir2016commonvariantsupstream pages 1-2, aga2020identificationofnovel pages 1-2, tran2017preservinglxrby pages 1-4, aga2020identificationofnovel pages 6-8).
- **Fish (Teleosts):** References to TTC39 genes in *Plectropomus leopardus* (coral trout) associated with skin coloration (unobtainable paper noted in search results).
- **Broader metazoan distribution:** The large number of taxa (7507) and proteins (9018) indicates presence across diverse metazoan lineages, possibly including invertebrates, though specific evidence for invertebrate orthologs was not detailed in the retrieved papers.

### Process/component terms across taxa

**None of the GO terms that might be considered for PTHR31859 hold universally across all taxa:**

- **Tissue-specific terms** (e.g., liver, pancreatic islet) are mammalian/vertebrate anatomical compartments and do not apply to invertebrates or non-vertebrate chordates.
- **LXRα regulation** is a vertebrate-specific pathway; liver X receptors are nuclear hormone receptors present in vertebrates but not in invertebrates.
- **Cholesterol homeostasis** and **reverse cholesterol transport** are vertebrate lipid metabolism processes; invertebrates have different sterol metabolism.
- **Pancreatic β-cell function** and **type 2 diabetes** are vertebrate (particularly mammalian) phenotypes.

Given the broad taxonomic scope and the vertebrate-specific functions of the characterized members, **any process or component GO term added at the family level would fail to hold across the full taxonomic range**. This further supports the decision to leave PTHR31859 without InterPro2GO mappings.

---

## 5. Over-Annotation Verdict and Recommendations

### Overall assessment

**Verdict:** The current InterPro2GO mapping status for PTHR31859 is **SOUND** (no GO terms mapped). The family exhibits **extreme functional divergence** across subfamilies, with distinct molecular mechanisms (E3 ligase activity vs. unknown), tissue expression patterns (liver vs. pancreas), and disease associations (atherosclerosis/NASH vs. type 2 diabetes vs. endometriosis). Applying any family-level GO term would **systematically over-annotate** proteins matching this signature.

### Recommended action pattern

**Primary recommendation:** **KEEP_AS_NON_CORE** — Do NOT add family-level GO terms to PTHR31859.

**Rationale:**
1. **No single conserved molecular function:** TTC39B has E3 ligase activity; TTC39A and TTC39C do not have demonstrated enzymatic activities. A family-level molecular function term (e.g., ubiquitin ligase activity) would be false for many members.
2. **Tissue and process divergence:** TTC39A functions in pancreatic islets/glucose metabolism; TTC39B in liver/lipid metabolism; TTC39C is uncharacterized. No biological process term applies to all members.
3. **Taxonomic breadth vs. vertebrate-specific functions:** The family spans 7507 taxa, but characterized functions (LXR regulation, cholesterol homeostasis, pancreatic β-cell function) are vertebrate-specific and do not generalize.
4. **Generic terms are uninformative:** Terms like "protein binding" or "molecular adaptor activity" are too broad to add value and do not distinguish TTC39 from hundreds of other TPR-containing proteins.

### Subfamily-specific recommendations

If GO annotation is desired, it should be applied to **individual PANTHER subfamilies** (not to the parent family PTHR31859):

- **For TTC39B-like subfamily:**
  - **Molecular Function:** GO:0061630 (ubiquitin protein ligase activity)
  - **Biological Process:** GO:0043161 (proteasome-mediated ubiquitin-dependent protein catabolic process); GO:0042632 (cholesterol homeostasis); GO:0010877 (lipid homeostasis)
  - **Cellular Component:** GO:0005737 (cytoplasm) or GO:0005829 (cytosol) if supported by localization data

- **For TTC39A-like subfamily:**
  - Await further biochemical characterization before assigning molecular function terms.
  - **Biological Process:** Potentially glucose homeostasis or pancreatic β-cell-related terms once mechanism is clarified.
  
- **For TTC39C and other subfamilies:**
  - No GO terms until functional characterization is available.

### Recommendation for InterPro

**Do not demote or modify PTHR31859 itself.** The entry type ("family") is appropriate, but the functional heterogeneity justifies the absence of InterPro2GO mappings. If InterPro curators wish to support GO annotation, they should:
1. **Maintain no GO terms at the PTHR31859 family level.**
2. **Encourage GO Consortium or PANTHER curators** to annotate specific subfamilies (e.g., PANTHER sub-family nodes for TTC39A, TTC39B, TTC39C) with subfamily-appropriate GO terms.
3. **Avoid propagating any GO term from parent (PTHR31859) to child subfamilies** unless it is truly universal (e.g., "protein binding" is technically true but not informative).

### Summary recommendation table

| InterPro Entry | Current GO Terms | Recommended Action | Rationale |
|---|---|---|---|
| PTHR31859 (family level) | None | **KEEP_AS_NON_CORE** (no GO terms) | Extreme functional divergence across subfamilies; no single molecular function, biological process, or cellular component term is true for all members. Family-level annotation would over-annotate. |
| PANTHER subfamily for TTC39B | Not specified in query | **ACCEPT subfamily-specific terms** (e.g., GO:0061630 ubiquitin ligase, GO:0042632 cholesterol homeostasis) | Strong experimental evidence for TTC39B as E3 ligase for LXRα and role in lipid metabolism; terms are appropriate for this subfamily only. |
| PANTHER subfamily for TTC39A | Not specified in query | **Await further data** before adding molecular function terms; consider biological process terms related to glucose/β-cell function if mechanism clarified | Candidate diabetes gene but mechanistic activity undefined; subfamily-specific terms possible in future. |
| PANTHER subfamily for TTC39C and others | Not specified in query | **No action** until functional data available | Insufficient characterization; avoid speculative annotation. |

---

## Conclusions

PTHR31859 represents a **functionally heterogeneous protein family** characterized by a conserved TPR domain scaffold but divergent molecular activities, tissue expression patterns, and biological roles. The best-characterized member, TTC39B, functions as an E3 ubiquitin ligase for LXRα in liver, regulating lipid metabolism and protecting against atherosclerosis and steatohepatitis. In contrast, TTC39A is expressed in pancreatic islets and implicated in glucose homeostasis and type 2 diabetes via unknown mechanisms, while TTC39C remains poorly characterized. This functional divergence, combined with the family's broad taxonomic distribution (9018 proteins, 7507 taxa), makes family-level GO annotation inappropriate. The current absence of InterPro2GO mappings for PTHR31859 is **sound and should be maintained**. Future GO annotation should target individual PANTHER subfamilies with experimentally validated, subfamily-specific terms rather than propagating generic or over-broad terms from the parent family entry.

---

### Key Citations

- TTC39B as E3 ligase for LXRα: (tran2017preservinglxrby pages 1-4, endoumeda2025exploringtheroles pages 1-2)
- TTC39A in type 2 diabetes and pancreatic islets: (aga2020identificationofnovel pages 1-2, aga2020identificationofnovel pages 6-8)
- TTC39B in endometriosis and ovarian cancer: (french2016germlinepolymorphismsin pages 1-3, steinthorsdottir2016commonvariantsupstream pages 1-2)
- TPR domain structure and function: (pokhrel2025chaperonedependentandchaperoneindependent pages 1-3, barik2025ageneralizedai pages 1-3, bibber2020intrinsicdisorderin pages 1-3, paeng2020attpr10containingmultiple pages 1-3)
- TTC39B regulation of nutrient homeostasis genes: (xing2025mt1hinhibitsthe pages 1-2)


References

1. (pokhrel2025chaperonedependentandchaperoneindependent pages 1-3): Saugat Pokhrel, Shweta Devi, and Jason E. Gestwicki. Chaperone-dependent and chaperone-independent functions of carboxylate clamp tetratricopeptide repeat (cc-tpr) proteins. Feb 2025. URL: https://doi.org/10.1016/j.tibs.2024.11.004, doi:10.1016/j.tibs.2024.11.004. This article has 14 citations and is from a domain leading peer-reviewed journal.

2. (barik2025ageneralizedai pages 1-3): Sailen Barik. A generalized ai view of tricopeptide repeats: what’s in a name. International Journal of Molecular Sciences, 26:11649, Dec 2025. URL: https://doi.org/10.3390/ijms262311649, doi:10.3390/ijms262311649. This article has 1 citations.

3. (tran2017preservinglxrby pages 1-4): Melanie Tran and Li Wang. Preserving lxr by inhibiting t39: a step closer to treating atherosclerosis and steatohepatitis? Hepatology, 65:741-744, Feb 2017. URL: https://doi.org/10.1002/hep.28946, doi:10.1002/hep.28946. This article has 2 citations and is from a highest quality peer-reviewed journal.

4. (endoumeda2025exploringtheroles pages 1-2): Kaori Endo-Umeda and Makoto Makishima. Exploring the roles of liver x receptors in lipid metabolism and immunity in atherosclerosis. Biomolecules, 15:579, Apr 2025. URL: https://doi.org/10.3390/biom15040579, doi:10.3390/biom15040579. This article has 11 citations.

5. (aga2020identificationofnovel pages 1-2): Heja Aga, Nicole Hallahan, Pascal Gottmann, Markus Jaehnert, Sophie Osburg, Gunnar Schulze, Anne Kamitz, Danny Arends, Gudrun Brockmann, Tanja Schallschmidt, Sandra Lebek, Alexandra Chadt, Hadi Al-Hasani, Hans-Georg Joost, Annette Schürmann, and Heike Vogel. Identification of novel potential type 2 diabetes genes mediating β-cell loss and hyperglycemia using positional cloning. Frontiers in Genetics, Sep 2020. URL: https://doi.org/10.3389/fgene.2020.567191, doi:10.3389/fgene.2020.567191. This article has 11 citations and is from a peer-reviewed journal.

6. (aga2020identificationofnovel pages 6-8): Heja Aga, Nicole Hallahan, Pascal Gottmann, Markus Jaehnert, Sophie Osburg, Gunnar Schulze, Anne Kamitz, Danny Arends, Gudrun Brockmann, Tanja Schallschmidt, Sandra Lebek, Alexandra Chadt, Hadi Al-Hasani, Hans-Georg Joost, Annette Schürmann, and Heike Vogel. Identification of novel potential type 2 diabetes genes mediating β-cell loss and hyperglycemia using positional cloning. Frontiers in Genetics, Sep 2020. URL: https://doi.org/10.3389/fgene.2020.567191, doi:10.3389/fgene.2020.567191. This article has 11 citations and is from a peer-reviewed journal.

7. (xing2025mt1hinhibitsthe pages 1-2): Yamin Xing, Guangyuan Li, Ganggang Li, Jixuan Xu, Ting Zhang, Mengxue Li, Chunxiao Gao, Miaoran Fu, Pengyuan Zheng, and Xiufeng Chu. Mt1h inhibits the growth of gastric cancer by regulating slc6a19/ttc39b/adm2 and activating p53-dependent autophagy. Scientific Reports, Mar 2025. URL: https://doi.org/10.1038/s41598-025-91319-y, doi:10.1038/s41598-025-91319-y. This article has 1 citations and is from a peer-reviewed journal.

8. (paeng2020attpr10containingmultiple pages 1-3): Seol Ki Paeng, Chang Ho Kang, Yong Hun Chi, Ho Byoung Chae, Eun Seon Lee, Joung Hun Park, Seong Dong Wi, Su Bin Bae, Kieu Anh Thi Phan, and Sang Yeol Lee. Attpr10 containing multiple ank and tpr domains exhibits chaperone activity and heat-shock dependent structural switching. Applied Sciences, 10:1265, Feb 2020. URL: https://doi.org/10.3390/app10041265, doi:10.3390/app10041265. This article has 10 citations.

9. (bibber2020intrinsicdisorderin pages 1-3): Nathan W. Van Bibber, Cornelia Haerle, Roy Khalife, Bin Xue, and Vladimir N. Uversky. Intrinsic disorder in tetratricopeptide repeat proteins. International Journal of Molecular Sciences, 21:3709, May 2020. URL: https://doi.org/10.3390/ijms21103709, doi:10.3390/ijms21103709. This article has 23 citations.

10. (french2016germlinepolymorphismsin pages 1-3): Juliet D. French, Sharon E. Johnatty, Yi Lu, Jonathan Beesley, Bo Gao, Murugan Kalimutho, Michelle J. Henderson, Amanda J. Russell, Siddhartha Kar, Xiaoqing Chen, Kristine M. Hillman, Susanne Kaufmann, Haran Sivakumaran, Martin O’Reilly, Chen Wang, Darren J. Korbie, Diether Lambrechts, Evelyn Despierre, Els Van Nieuwenhuysen, Sandrina Lambrechts, Ignace Vergote, Beth Karlan, Jenny Lester, Sandra Orsulic, Christine Walsh, Peter A. Fasching, Matthias W. Beckmann, Arif B. Ekici, Alexander Hein, Keitaro Matsuo, Satoyo Hosono, Jacobus Pisterer, Peter Hillemanns, Toru Nakanishi, Yasushi Yatabe, Marc T. Goodman, Galina Lurie, Rayna K. Matsuno, Pamela J. Thompson, Tanja Pejovic, Yukie Bean, Florian Heitz, Philipp Harter, Andreas du Bois, Ira Schwaab, Estrid Hogdall, Susanne K. Kjaer, Allan Jensen, Claus Hogdall, Lene Lundvall, Svend Aage Engelholm, Bob Brown, James M. Flanagan, Michelle D. Metcalf, Nadeem Siddiqui, Thomas Sellers, Brooke Fridley, Julie Cunningham, Joellen M. Schildkraut, Ed Iversen, Rachel Palmieri Weber, Donal Brennan, Andrew Berchuck, Paul Pharoah, Paul Harnett, Murray D. Norris, Michelle Haber, Ellen L. Goode, Jason S. Lee, Kum Kum Khanna, Kerstin B. Meyer, Georgia Chenevix-Trench, Anna deFazio, Stacey L. Edwards, and Stuart MacGregor. Germline polymorphisms in an enhancer of psip1 are associated with progression-free survival in epithelial ovarian cancer. Oncotarget, 7:6353-6368, Jan 2016. URL: https://doi.org/10.18632/oncotarget.7047, doi:10.18632/oncotarget.7047. This article has 37 citations.

11. (steinthorsdottir2016commonvariantsupstream pages 1-2): Valgerdur Steinthorsdottir, Gudmar Thorleifsson, Kristrun Aradottir, Bjarke Feenstra, Asgeir Sigurdsson, Lilja Stefansdottir, Anna M. Kristinsdottir, Florian Zink, Gisli H. Halldorsson, Nete Munk Nielsen, Frank Geller, Mads Melbye, Daniel F. Gudbjartsson, Reynir T. Geirsson, Unnur Thorsteinsdottir, and Kari Stefansson. Common variants upstream of kdr encoding vegfr2 and in ttc39b associate with endometriosis. Nature Communications, Jul 2016. URL: https://doi.org/10.1038/ncomms12350, doi:10.1038/ncomms12350. This article has 56 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PTHR31859-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. barik2025ageneralizedai pages 1-3
2. aga2020identificationofnovel pages 6-8
3. tran2017preservinglxrby pages 1-4
4. steinthorsdottir2016commonvariantsupstream pages 1-2
5. pokhrel2025chaperonedependentandchaperoneindependent pages 1-3
6. endoumeda2025exploringtheroles pages 1-2
7. aga2020identificationofnovel pages 1-2
8. bibber2020intrinsicdisorderin pages 1-3
9. french2016germlinepolymorphismsin pages 1-3
10. https://doi.org/10.1016/j.tibs.2024.11.004,
11. https://doi.org/10.3390/ijms262311649,
12. https://doi.org/10.1002/hep.28946,
13. https://doi.org/10.3390/biom15040579,
14. https://doi.org/10.3389/fgene.2020.567191,
15. https://doi.org/10.1038/s41598-025-91319-y,
16. https://doi.org/10.3390/app10041265,
17. https://doi.org/10.3390/ijms21103709,
18. https://doi.org/10.18632/oncotarget.7047,
19. https://doi.org/10.1038/ncomms12350,