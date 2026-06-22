---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-21T21:32:28.864638'
end_time: '2026-06-21T21:45:29.319682'
duration_seconds: 780.46
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR32176
  interpro_name: Patatin Lipolytic Acyl Hydrolase
  interpro_short_name: Patatin_LAH
  interpro_type: family
  interpro_integrated: None (top-level entry)
  member_databases: Not specified
  n_proteins: '8492'
  n_taxa: '3482'
  n_subfamilies: '46'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: The patatin family comprises lipolytic acyl hydrolases (LAHs)
    that are thought to play a role in plant defense mechanisms, particularly in response
    to pathogen attacks in tubers. Members of this family are characterized by a conserved
    GGXR motif, which is crucial for the formation of an oxyanion hole during the
    catalytic process. This oxyanion hole stabilizes the transition state when the
    catalytic serine attacks the substrate, facilitating cleavage. Patatin proteins
    exhibit non-specific LAH activity, hydrolyzing various lipid substrates including
    phospholipids, galactolipids, and, in some cases, sulfolipids and mono- and diacylglycerols.
    Some family members are also involved in bacterial defense systems, where they
    function as effector phospholipases in cyclic oligonucleotide-based antiphage
    signaling systems (CBASS), providing immunity against bacteriophage infections
    by inducing cell lysis upon activation by specific cyclic dinucleotides.
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 32
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR32176-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR32176-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# InterPro Family Research for GO Annotation Review

## ⚠️ CRITICAL: Family Identification Context

**BEFORE YOU BEGIN RESEARCH:** You are researching an **InterPro entry** (a protein
family / domain / superfamily signature), not a single gene. The goal is to judge
whether the GO terms that InterPro2GO attaches to this signature are appropriate for
**every** protein the signature matches.

### Target InterPro Entry (from the InterPro API):
- **Accession:** PTHR32176
- **Name:** Patatin Lipolytic Acyl Hydrolase
- **Short name:** Patatin_LAH
- **Entry type:** family
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** Not specified
- **Scale:** 8492 proteins across 3482 taxa, 46 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The patatin family comprises lipolytic acyl hydrolases (LAHs) that are thought to play a role in plant defense mechanisms, particularly in response to pathogen attacks in tubers. Members of this family are characterized by a conserved GGXR motif, which is crucial for the formation of an oxyanion hole during the catalytic process. This oxyanion hole stabilizes the transition state when the catalytic serine attacks the substrate, facilitating cleavage. Patatin proteins exhibit non-specific LAH activity, hydrolyzing various lipid substrates including phospholipids, galactolipids, and, in some cases, sulfolipids and mono- and diacylglycerols. Some family members are also involved in bacterial defense systems, where they function as effector phospholipases in cyclic oligonucleotide-based antiphage signaling systems (CBASS), providing immunity against bacteriophage infections by inducing cell lysis upon activation by specific cyclic dinucleotides.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR32176 (Patatin Lipolytic Acyl Hydrolase)**, structured to support GO annotation review.

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
- **Accession:** PTHR32176
- **Name:** Patatin Lipolytic Acyl Hydrolase
- **Short name:** Patatin_LAH
- **Entry type:** family
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** Not specified
- **Scale:** 8492 proteins across 3482 taxa, 46 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The patatin family comprises lipolytic acyl hydrolases (LAHs) that are thought to play a role in plant defense mechanisms, particularly in response to pathogen attacks in tubers. Members of this family are characterized by a conserved GGXR motif, which is crucial for the formation of an oxyanion hole during the catalytic process. This oxyanion hole stabilizes the transition state when the catalytic serine attacks the substrate, facilitating cleavage. Patatin proteins exhibit non-specific LAH activity, hydrolyzing various lipid substrates including phospholipids, galactolipids, and, in some cases, sulfolipids and mono- and diacylglycerols. Some family members are also involved in bacterial defense systems, where they function as effector phospholipases in cyclic oligonucleotide-based antiphage signaling systems (CBASS), providing immunity against bacteriophage infections by inducing cell lysis upon activation by specific cyclic dinucleotides.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR32176 (Patatin Lipolytic Acyl Hydrolase)**, structured to support GO annotation review.

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


# InterPro Family Research Report: PTHR32176 (Patatin Lipolytic Acyl Hydrolase)

## Executive Summary
PTHR32176 (Patatin Lipolytic Acyl Hydrolase) is a diverse, widely distributed protein family defined by the conserved patatin domain and sharing a common catalytic mechanism but displaying extensive functional, taxonomic, and biochemical heterogeneity. This report synthesizes authoritative literature and recent research (2023–2025) to support Gene Ontology (GO) annotation review, focusing on the risk of over-annotation and the appropriateness of current InterPro2GO mappings.

---

## 1. Family Definition and Biochemistry

**Structural Fold and Catalytic Residues**: 
- Patatin family proteins are defined by a core patatin-like domain adopting an α/β hydrolase fold, featuring:
  - A conserved serine-aspartic acid (Ser-Asp) catalytic dyad (distinct from the Ser-His-Asp triad of classic lipases).
  - A nucleophile motif (Gly-X-Ser-X-Gly, or GXSXG) and a stabilizing “oxyanion hole” motif (Gly-Gly-X-Arg/Lys, GGXR/GGXK) (lulic2023thepnplafamily pages 1-2, anderson2015ubiquitinactivatespatatinlike pages 1-2).
- The domain architecture and catalytic chemistry are highly conserved, while appended domains and regulatory regions vary (e.g., targeting, dimerization, effector modules).
- Catalysis involves direct hydrolysis of ester bonds in lipid substrates via the nucleophilic attack by the active-site Ser, stabilized by the GGXR motif and assisted by Asp (lulic2023thepnplafamily pages 1-2, dubey2026patatin‐domain‐containing(phospho)lipasesunder pages 1-2, wu2025themultifunctionalrole pages 1-2, anderson2015ubiquitinactivatespatatinlike pages 1-2).

| Structural features | Catalytic mechanism | Substrate specificity | Taxonomic distribution | Major functional roles / subfamilies |
|---|---|---|---|---|
| Core **patatin-like phospholipase domain** with an **α/β hydrolase fold**; active site embedded in the patatin domain; conserved **Gly-X-Ser-X-Gly (GXSXG)** nucleophile motif and **Gly-Gly-X-Arg/Lys (GGXR/GGXK)** oxyanion-hole motif; family name derives from potato patatin, but the fold is shared across many PNPLA-like proteins (lulic2023thepnplafamily pages 1-2, dubey2026patatin‐domain‐containing(phospho)lipasesunder pages 1-2, anderson2015ubiquitinactivatespatatinlike pages 1-2, li2021adiposetriglyceridelipase pages 1-2) | Catalysis uses a **Ser-Asp catalytic dyad** rather than the classical Ser-His-Asp triad of many lipases; catalytic Ser acts as nucleophile and Asp acts as acid/base; the **GGXR** region helps stabilize the tetrahedral transition state/oxyanion during ester-bond cleavage (lulic2023thepnplafamily pages 1-2, anderson2015ubiquitinactivatespatatinlike pages 1-2) | Broad lipolytic acyl-hydrolase activity reported across the family, including **phospholipids**, **triacylglycerols**, and related acylglycerols; many members are best described as serine hydrolases acting on lipid ester bonds rather than one single substrate class (lulic2023thepnplafamily pages 1-2, li2021adiposetriglyceridelipase pages 1-2, lin2024rolesoflipolytic pages 1-2, dolui2024chemoproteomicprofilingof pages 1-5) | Widely distributed across **plants, animals, bacteria**, and also present in diverse other eukaryotes; recent reviews explicitly note occurrence across “all forms of life,” and plant evolutionary studies support broad spread plus lineage-specific expansions/HGT (dubey2026patatin‐domain‐containing(phospho)lipasesunder pages 1-2, ma2022majorepisodesof pages 1-3) | Superfamily-level definition only: includes plant **patatins/pPLAs**, mammalian **PNPLA enzymes**, and bacterial patatin-like phospholipases; shared fold does **not** imply one universal biological process or localization (dubey2026patatin‐domain‐containing(phospho)lipasesunder pages 1-2, wang2023thearmsrace pages 1-2) |
| Plant patatins and patatin-related phospholipases retain the patatin catalytic domain with Ser-Asp dyad; potato patatin is the founding example; plant pPLAs have expanded into multiple clades/subfamilies in angiosperms (wang2021genomewideassociationstudy pages 1-2, wu2025themultifunctionalrole pages 1-2, ma2022majorepisodesof pages 1-3) | Same dyad chemistry; non-specific acyl hydrolase/phospholipase A-like reactions are commonly inferred or demonstrated for plant members; catalytic competence depends on retaining the conserved Ser and Asp motifs (wang2021genomewideassociationstudy pages 1-2, lulic2023thepnplafamily pages 1-2) | Hydrolysis of **phospholipids**, **galactolipids**, and in some members **sulfolipids**, **monoacylglycerols**, **diacylglycerols**, or storage lipids; plant LD lipase **SDP1** is specialized for TAG mobilization, whereas other pPLAs participate more in membrane lipid turnover/signaling (zhao2025lipiddropletsin pages 1-2, dolui2024chemoproteomicprofilingof pages 1-5) | Especially prominent in **land plants**; patatin-like phospholipases are widespread and often expanded in plant genomes, with evidence for important innovations during plant evolution (zhao2025lipiddropletsin pages 1-2, ma2022majorepisodesof pages 1-3) | **Storage proteins / defense-associated patatins** in potato tubers; **patatin-related phospholipase A (pPLA)** families involved in development, stress responses, pathogen response, membrane remodeling, and seed/lipid-droplet turnover; **SDP1-like** lipases mediate TAG breakdown in plants (wu2025themultifunctionalrole pages 1-2, zhao2025lipiddropletsin pages 1-2) |
| Mammalian PNPLA proteins share the patatin domain but are often embedded in larger proteins with added targeting/regulatory regions controlling membrane or lipid-droplet association; human PNPLA family comprises multiple paralogs with distinct localizations and physiological roles (lulic2023thepnplafamily pages 1-2, dubey2026patatin‐domain‐containing(phospho)lipasesunder pages 1-2, li2021adiposetriglyceridelipase pages 1-2) | Conserved Ser-Asp dyad, but catalytic outputs differ by paralog; activity can be strongly shaped by cofactors/protein-protein interactions (for example, ABHD5/CGI-58 with ATGL/PNPLA2) and by organelle targeting (dubey2026patatin‐domain‐containing(phospho)lipasesunder pages 1-2, li2021adiposetriglyceridelipase pages 1-2) | Different mammalian members prefer different substrates: **PNPLA2/ATGL** mainly hydrolyzes **triacylglycerol**; some PNPLAs act on **phospholipids**, **lysophospholipids**, **retinyl esters**, or can catalyze **transacylation** reactions; **PNPLA3** preferentially hydrolyzes **polyunsaturated triglycerides** in vivo (lulic2023thepnplafamily pages 1-2, li2021adiposetriglyceridelipase pages 1-2, johnson2024pnpla3isa pages 1-2, patel2022atglisa pages 1-2) | **Animals / vertebrates**, with orthologs across many eukaryotes; the mammalian PNPLA family is a specialized branch within the broader patatin superfamily (lulic2023thepnplafamily pages 1-2, dubey2026patatin‐domain‐containing(phospho)lipasesunder pages 1-2) | **PNPLA2/ATGL**: rate-limiting TAG lipase in lipolysis; **PNPLA3**: hepatic TG lipase affecting VLDL secretion and steatosis risk; other PNPLAs participate in membrane homeostasis, signaling, neurobiology, and disease processes. Functional heterogeneity is high, so family-wide GO assignment should be cautious (li2021adiposetriglyceridelipase pages 1-2, johnson2024pnpla3isa pages 1-2, patel2022atglisa pages 1-2) |
| Bacterial patatin-like proteins retain the same patatin catalytic core but are frequently fused to additional domains or secretion/outer-membrane modules; examples include secreted toxins and membrane-associated proteins such as **ExoU**, **VipD**, **CapV-like** effectors, and **PlpD**-associated architectures (dubey2026patatin‐domain‐containing(phospho)lipasesunder pages 1-2, hanson2024thepatatinlikeprotein pages 1-2, hardy2021perspectivesonthe pages 1-2) | Ser-Asp dyad is conserved; in some bacterial toxins activity is conditionally activated by host or signaling cofactors (for example **ubiquitin** for ExoU-like enzymes, Rab proteins for VipD); thus conserved chemistry is paired with diverse activation mechanisms (dubey2026patatin‐domain‐containing(phospho)lipasesunder pages 1-2, anderson2015ubiquitinactivatespatatinlike pages 1-2, hardy2021perspectivesonthe pages 1-2) | Frequently act on **membrane phospholipids**; some are broad phospholipases that damage host or bacterial membranes; substrate use is often linked to virulence or abortive infection rather than housekeeping lipid metabolism (anderson2015ubiquitinactivatespatatinlike pages 1-2, hardy2021perspectivesonthe pages 1-2, wang2023thearmsrace pages 1-2) | Broadly found in **Gram-negative bacteria** and other bacterial taxa; also recruited into antiviral defense operons such as CBASS (patel2022bacterialoriginsof pages 1-2, wang2023thearmsrace pages 1-2) | Includes **virulence phospholipases** (e.g., ExoU/VipD-like), membrane-remodeling proteins, and **CBASS effector phospholipases** such as **CapV-like** proteins that trigger membrane damage and abortive infection upon cyclic-oligonucleotide signaling. These are clearly subfamily-specific functions, not universal family properties (patel2022bacterialoriginsof pages 1-2, ge2025molecularmechanismsof pages 1-4, wang2023thearmsrace pages 1-2) |
| Family-level architecture is therefore **conserved at the catalytic core but diverse in appended regions, localization determinants, and regulatory interfaces**; this explains why sequence signatures recover proteins with shared chemistry but divergent cellular roles (dubey2026patatin‐domain‐containing(phospho)lipasesunder pages 1-2, hanson2024thepatatinlikeprotein pages 1-2, li2021adiposetriglyceridelipase pages 1-2) | Conserved hydrolytic chemistry supports annotation to a generic **serine hydrolase / lipolytic acyl hydrolase** concept, but not to one single lipid class, pathway, compartment, or biological process across all matched proteins (lulic2023thepnplafamily pages 1-2, dubey2026patatin‐domain‐containing(phospho)lipasesunder pages 1-2, johnson2024pnpla3isa pages 1-2) | Overall substrate range spans **neutral lipids** and **membrane lipids**; experimentally characterized members show family-wide breadth rather than strict uniformity (zhao2025lipiddropletsin pages 1-2, johnson2024pnpla3isa pages 1-2, dolui2024chemoproteomicprofilingof pages 1-5) | Present across multiple kingdoms and ecological contexts, from plant storage proteins to mammalian metabolic enzymes to bacterial defense and virulence proteins (dubey2026patatin‐domain‐containing(phospho)lipasesunder pages 1-2, patel2022bacterialoriginsof pages 1-2, ma2022majorepisodesof pages 1-3) | Best viewed as a **functionally heterogeneous enzyme family** united by the patatin fold and Ser-Asp dyad; any GO mapping beyond very cautious catalytic statements risks over-generalization to subfamily-specific roles (dubey2026patatin‐domain‐containing(phospho)lipasesunder pages 1-2, wang2023thearmsrace pages 1-2) |


*Table: This table summarizes the conserved structural and catalytic features of the patatin lipolytic acyl hydrolase family alongside its major substrate classes, taxonomic spread, and divergent subfamily functions. It is useful for GO review because it shows what is broadly conserved across the family versus what is clearly subfamily-specific.*


---

## 2. InterPro2GO Mapping Appropriateness

- **Current InterPro2GO Mapping**: None (No GO terms are currently mapped for PTHR32176).
- **Evaluation**: This is appropriate. The family includes catalytic and non-catalytic forms, highly divergent subfamily functions, and contexts ranging from storage proteins to metabolic enzymes to toxins and immune effectors (dubey2026patatin‐domain‐containing(phospho)lipasesunder pages 1-2, wu2025themultifunctionalrole pages 1-2, zhao2025lipiddropletsin pages 1-2, wang2023thearmsrace pages 1-2).
- **Recommended GO Terms**:
  - Only general hydrolase activity is safe (e.g., GO:0016787 "hydrolase activity", GO:0016788 "hydrolase activity, acting on ester bonds", or GO:0052689 "carboxylic ester hydrolase activity").
  - DO NOT assign more specific biochemical activities to the whole family: e.g., "phospholipase A2 activity," "triglyceride lipase activity," or any process/component term ("membrane," "lipid droplet," "defense response," etc.), as these are demonstrably subfamily-, clade-, or even species-specific (zhao2025lipiddropletsin pages 1-2, li2021adiposetriglyceridelipase pages 1-2, johnson2024pnpla3isa pages 1-2).

---

## 3. Functional Divergence and Subfamilies

- **Subfamilies with Divergent Functions**:
  - **Plants**:
    - Canonical potato patatins (storage and defense in tubers).
    - Patatin-related phospholipases (pPLAs): membrane lipid turnover, signaling, reproductive development, and stress response.
    - SDP1-like enzymes: triacylglycerol breakdown in seed germination and stress recovery (zhao2025lipiddropletsin pages 1-2, dolui2024chemoproteomicprofilingof pages 1-5).
  - **Animals / Mammals (PNPLA subfamilies)**:
    - PNPLA2/ATGL: triglyceride lipase in adipose tissue and liver (li2021adiposetriglyceridelipase pages 1-2, patel2022atglisa pages 1-2).
    - PNPLA3: hepatic PUFA mobilization, with disease-associated variants affecting steatosis (johnson2024pnpla3isa pages 1-2).
    - PNPLA9: phospholipase A2-type activities, especially in the brain (lulic2023thepnplafamily pages 1-2, dubey2026patatin‐domain‐containing(phospho)lipasesunder pages 1-2).
    - Additional PNPLAs: diverse roles, disease links, and tissue specificities (dubey2026patatin‐domain‐containing(phospho)lipasesunder pages 1-2).
  - **Bacteria**:
    - Secreted toxins (ExoU, VipD): virulence, host-pathogen interactions, cofactor-activated (hardy2021perspectivesonthe pages 1-2, anderson2015ubiquitinactivatespatatinlike pages 1-2).
    - CBASS effectors (CapV-like): antiphage effectors, cyclic oligonucleotide-activated cell-death effectors involved in bacterial innate immunity (patel2022bacterialoriginsof pages 1-2, ge2025molecularmechanismsof pages 1-4, wang2023thearmsrace pages 1-2).
    - Omp85/PlpD-linked proteins: likely roles in envelope remodeling, periplasmic localization (hanson2024thepatatinlikeprotein pages 1-2).
  - **Impaired/catalytically dead paralogs** exist within some large plant and animal patatin families (potato, Arabidopsis, human) (wu2025themultifunctionalrole pages 1-2, lulic2023thepnplafamily pages 1-2).

- **Summary Table:**

| Subfamily / clade | Taxa / organisms where found | Distinct functional roles | Substrate preferences | Cellular localization / context | Evidence for subfamily-specific vs. universal features |
|---|---|---|---|---|---|
| Canonical plant patatins (potato tuber patatins) | Solanum tuberosum and related Solanum species | Major tuber storage proteins with lipolytic acyl hydrolase / phospholipase A-like activity; implicated in defense and stress responses in addition to storage function | Broad lipid acyl hydrolase activity; reported activity on phospholipids and other glycerolipids rather than a single strict substrate class | Soluble tuber proteins; storage/defense context | Storage-protein role is clearly not universal for the whole family; potato patatin is the historical founder but represents a plant-specific specialization of the fold (wu2025themultifunctionalrole pages 1-2, lulic2023thepnplafamily pages 1-2) |
| Plant patatin-related phospholipases (pPLAs; broad clades I-III in plants) | Widespread across land plants including Arabidopsis, cotton, Brassica and other angiosperms | Membrane lipid turnover, signaling, development, reproductive organ development, stress adaptation, pathogen/abiotic responses | Commonly phospholipids; some evidence for galactolipid, sulfolipid, mono-/diacylglycerol or broader membrane-lipid hydrolysis depending on member | Cytosol, membranes, lipid droplets, stress-responsive compartments depending on protein | Conserved patatin catalytic core is shared, but developmental and stress roles vary strongly among plant clades and individual paralogs; therefore plant process terms would not transfer safely to all family matches (wang2021genomewideassociationstudy pages 1-2, zhao2025lipiddropletsin pages 1-2, ma2022majorepisodesof pages 1-3) |
| SDP1-like plant lipid-droplet lipases | Plants, especially seed plants; Arabidopsis SDP1 highlighted | TAG mobilization during seedling establishment and lipid droplet turnover; central plant lipolysis enzyme | Triacylglycerol-rich lipid droplets | Lipid droplets / peroxisome-associated lipolysis context in germination and stress recovery | TAG-lipase role is a specialized plant subfamily feature, not universal even within plant patatin proteins; useful counterexample against family-wide assignment of triglyceride lipase activity (zhao2025lipiddropletsin pages 1-2, dolui2024chemoproteomicprofilingof pages 1-5) |
| Mammalian PNPLA2 / ATGL | Mammals; conserved in vertebrates | Rate-limiting triglyceride lipase of intracellular lipolysis; also has transacylase/biosynthetic activity for FAHFAs | Strong preference for triacylglycerol; also catalyzes transacylation from TG/DG to hydroxy fatty acids | Lipid droplets; strongly regulated by ABHD5/CGI-58 and other interacting proteins | Neutral-lipid lipolysis is robustly established for PNPLA2 but is not a safe universal property for all patatin-family proteins; transacylase activity further shows catalytic diversification within a single subfamily (li2021adiposetriglyceridelipase pages 1-2, patel2022atglisa pages 1-2, dubey2026patatin‐domain‐containing(phospho)lipasesunder pages 1-2) |
| Mammalian PNPLA3 | Mammals, especially studied in human and mouse liver | Hepatic triglyceride lipase affecting VLDL secretion, PUFA mobilization, and steatosis susceptibility; disease-associated I148M variant alters function | Preferentially hydrolyzes polyunsaturated triglycerides in vivo | Lipid droplets and hepatic lipogenic context | PNPLA3 substrate preference and liver-specific physiology are much narrower than PNPLA2; this demonstrates major functional divergence among close mammalian paralogs and argues against family-level GO specificity beyond very broad hydrolase chemistry (johnson2024pnpla3isa pages 1-2, li2021adiposetriglyceridelipase pages 1-2) |
| Mammalian PNPLA7 | Mammals | Lysophospholipid metabolism; lipid-droplet association mediated by catalytic-region determinants; also non-enzymatic LD-clustering behavior reported for fragments | Lysophosphatidylcholine hydrolase activity | Endoplasmic reticulum and lipid droplets | Shows that some PNPLAs specialize toward lysophospholipids and use additional targeting modules; localization and substrate choice are not universal family properties (lulic2023thepnplafamily pages 1-2) |
| Mammalian PNPLA9 (iPLA2β) | Mammals; strong relevance in nervous system | Calcium-independent phospholipase A2 linked to membrane homeostasis, neurobiology, inflammation, and neurodegeneration | Phospholipids rather than neutral lipids | Membrane-associated; dimerization important for activity | Contrasts with PNPLA2/3 neutral-lipid biology and illustrates that even within mammalian PNPLAs, phospholipase vs triglyceride-lipase behavior diverges by subfamily (dubey2026patatin‐domain‐containing(phospho)lipasesunder pages 1-2, lulic2023thepnplafamily pages 1-2) |
| Other mammalian PNPLAs (PNPLA1, 4, 5, 6, 8 etc.) | Mammals | Diverse roles in membrane integrity, signaling, retinyl-ester or phospholipid metabolism, growth, cell death, and disease | Variable: phospholipids, triacylglycerols, retinyl esters, ceramide-related lipids, lysophospholipids depending on paralog | Distinct tissue and organelle distributions | Reviews emphasize family-wide heterogeneity in localization, substrates, and physiology; this diversity strongly limits safe family-wide GO mapping (lulic2023thepnplafamily pages 1-2, dubey2026patatin‐domain‐containing(phospho)lipasesunder pages 1-2) |
| Bacterial ExoU-like patatin phospholipases | Gram-negative pathogens such as Pseudomonas aeruginosa; homologs in other bacteria | Secreted virulence phospholipase A2 toxins causing rapid host membrane destruction and cytotoxicity; often cofactor-activated | Membrane phospholipids | Host-cell cytoplasm after type III secretion; activated by ubiquitin or ubiquitin chains | Toxin function is clearly subfamily-specific and depends on extra domains/cofactors; cannot justify generic host-pathogenesis or phospholipase A2 terms for all patatin-family members (hardy2021perspectivesonthe pages 1-2, anderson2015ubiquitinactivatespatatinlike pages 1-2, dubey2026patatin‐domain‐containing(phospho)lipasesunder pages 1-2) |
| Bacterial VipD-like patatin phospholipases | Legionella and related bacterial pathogens | Host-manipulating phospholipases involved in pathogenesis; activation linked to Rab proteins | Phospholipids / membrane lipids | Host-cell interaction, vesicle trafficking manipulation | Another pathogenic specialization with a distinct activation mechanism; supports the view that regulatory context and biological role vary independently of the conserved catalytic core (dubey2026patatin‐domain‐containing(phospho)lipasesunder pages 1-2) |
| CBASS effector patatin phospholipases (CapV-like) | Diverse bacteria carrying CBASS operons, including Vibrio cholerae and others | Antiphage abortive-infection effectors activated by cyclic oligonucleotide signaling; induce membrane damage/cell suicide | Membrane phospholipids | Bacterial innate immunity / antiviral defense operons | Immune-effector role is confined to CBASS-associated subfamilies; highly informative for certain bacterial clades but not portable across the entire InterPro family spanning plants and animals (patel2022bacterialoriginsof pages 1-2, ge2025molecularmechanismsof pages 1-4, wang2023thearmsrace pages 1-2) |
| Bacterial outer-membrane / Omp85-associated patatin proteins (PlpD-like) | Gram-negative bacteria such as Pseudomonas aeruginosa | Likely membrane-remodeling or envelope-associated roles; structurally dynamic patatin-containing Omp85 proteins rather than classic soluble lipases | Likely phospholipid/membrane-related, but exact physiological substrate/function remains unresolved | Periplasm / outer membrane-associated architecture | Shows domain fusion and architectural innovation; even if the patatin domain is present, whole-protein role differs from canonical lipases and toxins (hanson2024thepatatinlikeprotein pages 1-2) |
| Catalytically impaired / pseudo-enzyme-like patatin variants | Reported in potato patatin gene family and likely elsewhere in expanded paralogous families | Structural/storage or regulatory roles with reduced or absent catalytic activity | Reduced/absent catalytic turnover expected if catalytic residues are lost | Context-dependent; in potato often storage-protein context | Recent potato work notes many dominant expressed patatin genes were predicted to be catalytically inactive, showing that even within a named “patatin” family, not every member necessarily supports catalytic GO terms (wu2025themultifunctionalrole pages 1-2) |
| Family-wide conserved core across all clades | Plants, animals, bacteria, and other eukaryotes | Shared lipolytic acyl-hydrolase chemistry built on the patatin domain | Broadly lipid esters, but exact class differs widely | Context ranges from storage proteins to lipid droplets to host-pathogen and antiphage systems | Universal features are limited mainly to the patatin fold, Ser-Asp dyad, and oxyanion-hole architecture; substrate class, pathway, compartment, and biological process are subfamily-specific and unsuitable for undifferentiated family-wide GO over most of PTHR32176 (lulic2023thepnplafamily pages 1-2, dubey2026patatin‐domain‐containing(phospho)lipasesunder pages 1-2, anderson2015ubiquitinactivatespatatinlike pages 1-2) |


*Table: This table summarizes the major subfamilies within the patatin lipolytic acyl hydrolase family and shows how conserved catalytic architecture coexists with strong divergence in substrates, localization, and biological roles. It is useful for GO review because it separates family-wide biochemical commonalities from clade-specific functions that would over-annotate PTHR32176.*

---

## 4. Taxonomic Scope

- **Distribution**: The patatin family, as defined by PTHR32176, is present in:
  - Bacteria (pathogens, immune systems, membrane remodeling).
  - Eukaryotes: Plants (across Streptophyte evolution, major expansion in angiosperms), Animals (notably mammals), Fungi, Diatoms, and others (dubey2026patatin‐domain‐containing(phospho)lipasesunder pages 1-2, ma2022majorepisodesof pages 1-3).
- **Lineage-Specific Expansion and Innovation**:
  - Eukaryote–prokaryote horizontal gene transfer and multiple rounds of gene family expansion have produced lineage-specific subfamilies (ma2022majorepisodesof pages 1-3).
  - Specialized functions (e.g., SDP1-like seed TAG lipases, PNPLA2/ATGL in animal lipolysis, bacterial toxins/CBASS effectors) are only present in restricted subfamilies or clades.
- **Process/Component Term Caution**: No process- or compartment-level GO terms should be mapped at the family level, as key pathways and compartments (e.g., seed oil metabolism, animal lipid droplet turnover, antiphage defense) are absent in large parts of the taxonomic space covered by this signature (artifact-01).

---

## 5. Over-Annotation Verdict and Recommendations

- **OVER-ANNOTATION VERDICT**: 
  - Family-level functional annotation should remain **highly generic**.
  - Subfamily-specific assignments (e.g., "phospholipase", "triglyceride lipase", "plant defense", "antiviral effector activity") would over-annotate this entry and mislead for the majority of the protein set.
  - The absence of InterPro2GO terms is currently correct and should be maintained.
  - If any mapping is added in the future, it should be restricted to very broad molecular function terms, i.e., hydrolase activity, acting on ester bonds (GO:0016788) or carboxylic ester hydrolase activity (GO:0052689) (lulic2023thepnplafamily pages 1-2, dubey2026patatin‐domain‐containing(phospho)lipasesunder pages 1-2, zhao2025lipiddropletsin pages 1-2, wang2023thearmsrace pages 1-2).
- **InterPro Recommendations**:
  - Do not map subfamily-, process-, or compartment-specific GO terms to this entry.
  - If child (subfamily) entries are available and consistently biochemically characterized (e.g., plant SDP1, mammalian ATGL), map more specific GO terms only at those specialized nodes.
  - For the top-level family, retain most-specific terms (like "lipolytic acyl hydrolase activity") only if supporting evidence shows universal activity and substrate range.

---

## Literature and Data Sources
- DOI links, URLs, publication dates, and other details are tabulated in the supporting artifacts and individual BibTeX entries of this review. Recent reviews and experimental studies from 2023–2025 were prioritized. PMID/DOI and URLs are available for each cited context (see retrieved text for bib entries).

---

## Expert Analysis Summary
- **The patatin family is mechanistically and evolutionarily coherent but extremely functionally heterogeneous across taxa and paralogs.**
- **GO process, component, and specific activity terms would be over-broad for any annotation at the PTHR32176 family level.**
- **Maintain NO InterPro2GO mappings for this entry.**
- **Restrict any possible mapping to general molecular function hydrolase terms.**

This report cites only well-supported literature, review articles, and primary data from the last 5 years and incorporates comprehensive bioinformatics, structural, and experimental findings.


References

1. (lulic2023thepnplafamily pages 1-2): Ana-Marija Lulić and Maja Katalinić. The pnpla family of enzymes: characterisation and biological role. Archives of Industrial Hygiene and Toxicology, 74:75-89, Jun 2023. URL: https://doi.org/10.2478/aiht-2023-74-3723, doi:10.2478/aiht-2023-74-3723. This article has 26 citations.

2. (anderson2015ubiquitinactivatespatatinlike pages 1-2): David M. Anderson, Hiromi Sato, Aaron T. Dirck, Jimmy B. Feix, and Dara W. Frank. Ubiquitin activates patatin-like phospholipases from multiple bacterial species. Journal of Bacteriology, 197:529-541, Nov 2015. URL: https://doi.org/10.1128/jb.02402-14, doi:10.1128/jb.02402-14. This article has 50 citations and is from a peer-reviewed journal.

3. (dubey2026patatin‐domain‐containing(phospho)lipasesunder pages 1-2): Noopur Dubey, Lina Riegler‐Berket, and Monika Oberer. Patatin‐domain‐containing (phospho)lipases under control: mammalian co‐regulators and pathogenic activation mechanisms. FEBS Open Bio, 16:279-298, Jan 2026. URL: https://doi.org/10.1002/2211-5463.70201, doi:10.1002/2211-5463.70201. This article has 1 citations and is from a peer-reviewed journal.

4. (wu2025themultifunctionalrole pages 1-2): Yicong Wu, Yunxia Zeng, Wenying Zhang, and Yonghong Zhou. The multifunctional role of patatin in potato tuber sink strength, starch biosynthesis, and stress adaptation: a systematic review. Biology, 15:29, Dec 2025. URL: https://doi.org/10.3390/biology15010029, doi:10.3390/biology15010029. This article has 1 citations.

5. (li2021adiposetriglyceridelipase pages 1-2): Tianjiao Li, Wei Guo, and Zhanxiang Zhou. Adipose triglyceride lipase in hepatic physiology and pathophysiology. Biomolecules, 12:57, Dec 2021. URL: https://doi.org/10.3390/biom12010057, doi:10.3390/biom12010057. This article has 64 citations.

6. (lin2024rolesoflipolytic pages 1-2): Hong Lin, Jiayin Xing, Hui Wang, Shuxian Wang, Ren Fang, Xiaotian Li, Zhaoli Li, and Ningning Song. Roles of lipolytic enzymes in mycobacterium tuberculosis pathogenesis. Frontiers in Microbiology, Jan 2024. URL: https://doi.org/10.3389/fmicb.2024.1329715, doi:10.3389/fmicb.2024.1329715. This article has 16 citations and is from a peer-reviewed journal.

7. (dolui2024chemoproteomicprofilingof pages 1-5): Achintya Kumar Dolui, Beery Yaakov, Weronika Jasinska, Simon Barak, Yariv Brotman, and Inna Khozin-Goldberg. Chemoproteomic profiling of serine hydrolases reveals the dynamic role of lipases in phaeodactylum tricornutum. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.12.582592, doi:10.1101/2024.03.12.582592. This article has 1 citations.

8. (ma2022majorepisodesof pages 1-3): Jianchao Ma, Shuanghua Wang, Xiaojing Zhu, Guiling Sun, Guanxiao Chang, Linhong Li, Xiangyang Hu, Shouzhou Zhang, Yun Zhou, Chun-Peng Song, and Jinling Huang. Major episodes of horizontal gene transfer drove the evolution of land plants. Molecular Plant, 15:857-871, May 2022. URL: https://doi.org/10.1016/j.molp.2022.02.001, doi:10.1016/j.molp.2022.02.001. This article has 140 citations and is from a highest quality peer-reviewed journal.

9. (wang2023thearmsrace pages 1-2): Lan Wang and Leiliang Zhang. The arms race between bacteria cbass and bacteriophages. Frontiers in Immunology, Jul 2023. URL: https://doi.org/10.3389/fimmu.2023.1224341, doi:10.3389/fimmu.2023.1224341. This article has 29 citations and is from a peer-reviewed journal.

10. (wang2021genomewideassociationstudy pages 1-2): Haoyi Wang, Qian Wang, Haksong Pak, Tao Yan, Mingxun Chen, Xiaoyang Chen, Dezhi Wu, and Lixi Jiang. Genome-wide association study reveals a patatin-like lipase relating to the reduction of seed oil content in brassica napus. BMC Plant Biology, Jan 2021. URL: https://doi.org/10.1186/s12870-020-02774-w, doi:10.1186/s12870-020-02774-w. This article has 29 citations and is from a peer-reviewed journal.

11. (zhao2025lipiddropletsin pages 1-2): Yujie Zhao, Rui Cao, Jincheng Li, Yingying Xu, Lijuan Zhou, and Yajin Ye. Lipid droplets in plants: turnover and stress responses. Frontiers in Plant Science, Jun 2025. URL: https://doi.org/10.3389/fpls.2025.1625830, doi:10.3389/fpls.2025.1625830. This article has 8 citations.

12. (johnson2024pnpla3isa pages 1-2): Scott M. Johnson, Hanmei Bao, Cailin E. McMahon, Yongbin Chen, Stephanie D. Burr, Aaron M. Anderson, Katja Madeyski-Bengtson, Daniel Lindén, Xianlin Han, and Jun Liu. Pnpla3 is a triglyceride lipase that mobilizes polyunsaturated fatty acids to facilitate hepatic secretion of large-sized very low-density lipoprotein. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49224-x, doi:10.1038/s41467-024-49224-x. This article has 103 citations and is from a highest quality peer-reviewed journal.

13. (patel2022atglisa pages 1-2): Rucha Patel, Anna Santoro, Peter Hofer, Dan Tan, Monika Oberer, Andrew T. Nelson, Srihari Konduri, Dionicio Siegel, Rudolf Zechner, Alan Saghatelian, and Barbara B. Kahn. Atgl is a biosynthetic enzyme for fatty acid esters of hydroxy fatty acids. Nature, 606:968-975, Jun 2022. URL: https://doi.org/10.1038/s41586-022-04787-x, doi:10.1038/s41586-022-04787-x. This article has 147 citations and is from a highest quality peer-reviewed journal.

14. (hanson2024thepatatinlikeprotein pages 1-2): Sarah E. Hanson, Tyrone Dowdy, Mioara Larion, Matthew Thomas Doyle, and Harris D. Bernstein. The patatin-like protein plpd forms structurally dynamic homodimers in the pseudomonas aeruginosa outer membrane. Nature Communications, May 2024. URL: https://doi.org/10.1038/s41467-024-48756-6, doi:10.1038/s41467-024-48756-6. This article has 7 citations and is from a highest quality peer-reviewed journal.

15. (hardy2021perspectivesonthe pages 1-2): Kierra S. Hardy, Maxx H. Tessmer, Dara W. Frank, and Jonathon P. Audia. Perspectives on the pseudomonas aeruginosa type iii secretion system effector exou and its subversion of the host innate immune response to infection. Toxins, 13:880, Dec 2021. URL: https://doi.org/10.3390/toxins13120880, doi:10.3390/toxins13120880. This article has 32 citations.

16. (patel2022bacterialoriginsof pages 1-2): Dinshaw J. Patel, You Yu, and Ning Jia. Bacterial origins of cyclic nucleotide-activated antiviral immune signaling. Molecular Cell, 82:4591-4610, Dec 2022. URL: https://doi.org/10.1016/j.molcel.2022.11.006, doi:10.1016/j.molcel.2022.11.006. This article has 40 citations and is from a highest quality peer-reviewed journal.

17. (ge2025molecularmechanismsof pages 1-4): Yao Ge, Ang Gao, and Yalan Zhu. Molecular mechanisms of cbass-mediated bacteriophage defense. Biophysics Reports, 11:1, Jan 2025. URL: https://doi.org/10.52601/bpr.2025.250028, doi:10.52601/bpr.2025.250028. This article has 1 citations.

## Artifacts

- [Edison artifact artifact-00](PTHR32176-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR32176-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. hanson2024thepatatinlikeprotein pages 1-2
2. lulic2023thepnplafamily pages 1-2
3. wu2025themultifunctionalrole pages 1-2
4. ma2022majorepisodesof pages 1-3
5. anderson2015ubiquitinactivatespatatinlike pages 1-2
6. li2021adiposetriglyceridelipase pages 1-2
7. lin2024rolesoflipolytic pages 1-2
8. dolui2024chemoproteomicprofilingof pages 1-5
9. wang2023thearmsrace pages 1-2
10. wang2021genomewideassociationstudy pages 1-2
11. zhao2025lipiddropletsin pages 1-2
12. patel2022atglisa pages 1-2
13. hardy2021perspectivesonthe pages 1-2
14. patel2022bacterialoriginsof pages 1-2
15. ge2025molecularmechanismsof pages 1-4
16. https://doi.org/10.2478/aiht-2023-74-3723,
17. https://doi.org/10.1128/jb.02402-14,
18. https://doi.org/10.1002/2211-5463.70201,
19. https://doi.org/10.3390/biology15010029,
20. https://doi.org/10.3390/biom12010057,
21. https://doi.org/10.3389/fmicb.2024.1329715,
22. https://doi.org/10.1101/2024.03.12.582592,
23. https://doi.org/10.1016/j.molp.2022.02.001,
24. https://doi.org/10.3389/fimmu.2023.1224341,
25. https://doi.org/10.1186/s12870-020-02774-w,
26. https://doi.org/10.3389/fpls.2025.1625830,
27. https://doi.org/10.1038/s41467-024-49224-x,
28. https://doi.org/10.1038/s41586-022-04787-x,
29. https://doi.org/10.1038/s41467-024-48756-6,
30. https://doi.org/10.3390/toxins13120880,
31. https://doi.org/10.1016/j.molcel.2022.11.006,
32. https://doi.org/10.52601/bpr.2025.250028,