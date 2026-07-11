---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T20:05:45.919673'
end_time: '2026-06-28T20:22:41.192611'
duration_seconds: 1015.27
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR11528
  interpro_name: HEAT SHOCK PROTEIN 90 FAMILY MEMBER
  interpro_short_name: Not specified
  interpro_type: family
  interpro_integrated: IPR001404
  member_databases: Not specified
  n_proteins: '43519'
  n_taxa: '31125'
  n_subfamilies: '32'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: Not specified in InterPro
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 27
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR11528-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR11528-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** PTHR11528
- **Name:** HEAT SHOCK PROTEIN 90 FAMILY MEMBER
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR001404
- **Member database signatures:** Not specified
- **Scale:** 43519 proteins across 31125 taxa, 32 subfamilies
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
**PTHR11528 (HEAT SHOCK PROTEIN 90 FAMILY MEMBER)**, structured to support GO annotation review.

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
- **Accession:** PTHR11528
- **Name:** HEAT SHOCK PROTEIN 90 FAMILY MEMBER
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR001404
- **Member database signatures:** Not specified
- **Scale:** 43519 proteins across 31125 taxa, 32 subfamilies
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
**PTHR11528 (HEAT SHOCK PROTEIN 90 FAMILY MEMBER)**, structured to support GO annotation review.

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


# Comprehensive Research Report: PTHR11528 — HEAT SHOCK PROTEIN 90 FAMILY MEMBER

## InterPro2GO Annotation Review for PTHR11528

---

## 1. Family Definition and Biochemistry

### Structural Organization

PTHR11528 corresponds to the PANTHER classification of the HSP90 (Heat Shock Protein 90) family, integrated into the InterPro parent entry IPR001404. The family encompasses 43,519 proteins across 31,125 taxa with 32 subfamilies, making it one of the most broadly distributed chaperone families in biology.

All HSP90 family members share a conserved tripartite domain architecture consisting of: (i) an N-terminal domain (NTD, ~25 kDa) that contains an α/β sandwich structure with a nucleotide-binding pocket belonging to the GHKL ATPase/kinase superfamily; (ii) a middle domain (MD, ~40 kDa) with a three-layer α-β-α sandwich that serves as the primary client-protein and co-chaperone binding site; and (iii) a C-terminal domain (CTD, ~12 kDa) responsible for constitutive homodimerization (wickramaratne2024hsp90ateam pages 4-6, minari2024newinsightsinto pages 8-10). In eukaryotic cytosolic isoforms, the CTD contains a conserved MEEVD pentapeptide motif that mediates interactions with tetratricopeptide repeat (TPR)-domain co-chaperones (prodromou2022advancestowardsunderstanding pages 1-3, minari2024newinsightsinto pages 8-10). A flexible charged linker region connects the NTD and MD in eukaryotic cytosolic forms, though this element is absent from bacterial HtpG and mitochondrial TRAP1 (basset2023thechaperonesystem pages 2-4).

### Catalytic Mechanism and Conserved Residues

The ATP-binding site resides in the NTD and is completed by catalytic-loop residues from the MD. Critical catalytic residues include:
- **Glu-33** (yeast numbering): essential for ATP hydrolysis, acting as a general base in the catalytic mechanism (mader2020conformationaldynamicsmodulate pages 1-2, prodromou2022advancestowardsunderstanding pages 3-4).
- **Arg-380** (yeast numbering): located in the MD catalytic loop, directly contacts the γ-phosphate of ATP and forms a salt bridge with Glu-33, serving as a conformational sensor linking ATP binding to structural changes (mader2020conformationaldynamicsmodulate pages 1-2, prodromou2022advancestowardsunderstanding pages 1-3, prodromou2022advancestowardsunderstanding pages 3-4).
- **Asn-37**: crucial for coordinating the catalytically important Mg²⁺ ion required for ATP hydrolysis (mader2020conformationaldynamicsmodulate pages 1-2).

Mutations in these residues (E33A, R380A, N37A) substantially impair ATPase activity (mader2020conformationaldynamicsmodulate pages 1-2). The ATPase-driven conformational cycle involves coordinated N-terminal dimerization, lid closure over the ATP pocket, cross-subunit β-strand swapping, and NTD–MD association on a sub-millisecond timescale (prodromou2022advancestowardsunderstanding pages 3-4).

HSP90 functions as a homodimeric molecular chaperone that assists in the folding, maturation, and activation of a diverse array of client proteins through this ATP-dependent conformational cycle (minari2024newinsightsinto pages 6-8, zuppini2025heatshockproteins pages 6-7). The protein constitutes 1–2% of total cellular protein under normal conditions, increasing to 4–6% under stress (hu2022heatshockproteins pages 2-4).

---

## 2. InterPro2GO Mapping Appropriateness

### Current Status

PTHR11528 currently has **no InterPro2GO mappings**. This assessment evaluates whether this absence is appropriate and whether any GO terms could or should be added.

### Assessment of Potential GO Mappings

The following table evaluates candidate GO terms that could be considered for mapping to PTHR11528:

| Candidate GO Term | GO ID | GO Aspect (MF/BP/CC) | Universal Across All PTHR11528 Members? | Problematic Subfamilies/Taxa | Recommendation |
|---|---|---|---|---|---|
| ATP binding | GO:0005524 | MF | Yes, the conserved N-terminal HSP90/GHKL ATP-binding domain is shared across bacterial HtpG and eukaryotic HSP90 paralogs, although ATP hydrolysis rates and dependence vary | None identified for ATP binding itself; caution that this is informative but generic (mader2020conformationaldynamicsmodulate pages 1-2, wickramaratne2024hsp90ateam pages 4-6, zuppini2025heatshockproteins pages 6-7) | ACCEPT for whole family |
| unfolded protein binding | GO:0051082 | MF | Likely yes at the broad family level because HSP90 paralogs function as molecular chaperones that engage non-native client proteins, but client repertoires differ strongly by compartment and lineage | Specific client classes differ greatly in GRP94, TRAP1, HtpG, and chloroplast HSP90C; evidence is stronger for broad chaperone function than for identical substrate scope (kim2021correctionkimet pages 2-4, kim2021cellsurfacegrp94 pages 2-4, zuppini2025heatshockproteins pages 6-7, singh2024heatshockresponse pages 9-11) | ACCEPT for whole family |
| protein folding | GO:0006457 | BP | Yes at a broad level; all major HSP90-family branches are described as ATP-dependent molecular chaperones promoting folding/refolding/proteostasis | Mechanistic context differs across cytosol, ER, mitochondria, chloroplast, and bacteria, but the core folding role is retained (zuppini2025heatshockproteins pages 6-7, hu2022heatshockproteins pages 2-4, singh2024heatshockresponse pages 9-11) | ACCEPT for whole family |
| chaperone binding | GO:0051087 | MF | No | TRAP1 can function autonomously without canonical co-chaperones; bacterial HtpG lacks the eukaryotic co-chaperone network; even among eukaryotes, cochaperone usage differs substantially (wei2024heatshockprotein pages 2-4) | DO NOT MAP |
| protein homodimerization activity | GO:0042803 | MF | Structurally yes, because HSP90 family proteins act as dimers, but GO use here is not ideal because dimerization is a structural state rather than the most informative family-level molecular activity | Generic/low-information term; may add little value compared with core chaperone terms (mader2020conformationaldynamicsmodulate pages 1-2, wickramaratne2024hsp90ateam pages 4-6, hu2022heatshockproteins pages 2-4) | DO NOT MAP |
| response to heat | GO:0009408 | BP | No | TRAP1 is not a canonical heat-inducible cytosolic heat-shock protein; GRP94 is induced by ER stress rather than classic heat shock; bacterial and organellar homologs vary widely in regulation (albakova2022hsp70andhsp90 pages 5-6, wei2024heatshockprotein pages 2-4) | DO NOT MAP |
| response to stress | GO:0006950 | BP | No, too broad and not uniformly demonstrated in the same way across all subfamilies | Over-broad across taxa and compartments; many members have housekeeping roles rather than a specifically stress-induced role; regulation differs strongly among HSP90α, HSP90β, GRP94, TRAP1, and HtpG (wei2024heatshockprotein pages 2-4, maiti2022cytosolichsp90isoformspecific pages 1-2, albakova2022hsp70andhsp90 pages 5-6) | DO NOT MAP |
| cytoplasm | GO:0005737 | CC | No | Incorrect for GRP94 (ER), TRAP1 (mitochondria), HSP90C (chloroplast), and bacterial HtpG annotations if propagated as a universal location (wei2024heatshockprotein pages 2-4, maiti2022cytosolichsp90isoformspecific pages 1-2) | MOVE TO CHILD ENTRY |
| endoplasmic reticulum | GO:0005783 | CC | No | Only appropriate for GRP94/HSP90B1-like child groups; fungi reportedly lack GRP94, and cytosolic/mitochondrial/bacterial/plastid forms are not ER proteins (singh2024heatshockresponse pages 9-11, kim2021correctionkimet pages 2-4) | MOVE TO CHILD ENTRY |
| mitochondrion | GO:0005739 | CC | No | Only appropriate for TRAP1-like mitochondrial child groups; not valid for cytosolic HSP90s, GRP94, HtpG, or chloroplast HSP90C (wei2024heatshockprotein pages 2-4, basset2023thechaperonesystem pages 2-4) | MOVE TO CHILD ENTRY |
| chloroplast | GO:0009507 | CC | No | Restricted to plant/plastid HSP90C branch and absent from animals, fungi, most protists, and bacteria (maiti2022cytosolichsp90isoformspecific pages 1-2, maiti2022cytosolichsp90isoformspecific pages 2-4) | MOVE TO CHILD ENTRY |
| endoplasmic reticulum chaperone complex / immune receptor folding-related terms | Various | BP/CC | No | GRP94-specific specialization for TLRs, integrins, immunoglobulins, and ER proteostasis; not shared by cytosolic, mitochondrial, plastid, or bacterial homologs (kim2021correctionkimet pages 2-4, kim2021cellsurfacegrp94 pages 2-4, kim2021correctionkimet pages 14-15, kim2021cellsurfacegrp94 pages 14-15) | MOVE TO CHILD ENTRY |
| mitochondrial metabolic process / respiration regulation | Various | BP | No | TRAP1-specific metabolic and respiratory roles are not general HSP90-family properties (albakova2022hsp70andhsp90 pages 5-6, wei2024heatshockprotein pages 2-4) | MOVE TO CHILD ENTRY |


*Table: This table evaluates candidate GO terms for the broad HSP90 family PTHR11528 and distinguishes universal family-level annotations from terms that should be restricted to subfamilies or avoided. It is useful for judging whether adding InterPro2GO mappings would be safe or would over-annotate compartment-specific HSP90 paralogs.*

**Summary of GO term assessment:** A small number of core Molecular Function and Biological Process terms—specifically **ATP binding (GO:0005524)**, **unfolded protein binding (GO:0051082)**, and **protein folding (GO:0006457)**—are universally supported across all HSP90 family members and could be safely mapped at the PTHR11528 level (mader2020conformationaldynamicsmodulate pages 1-2, wickramaratne2024hsp90ateam pages 4-6, zuppini2025heatshockproteins pages 6-7, hu2022heatshockproteins pages 2-4). All other candidate terms, particularly Cellular Component terms (cytoplasm, ER, mitochondrion, chloroplast) and specific Biological Process terms (response to heat, immune function, metabolic regulation), apply only to specific subfamilies and would systematically over-annotate members from other branches if mapped to the parent family.

---

## 3. Functional Divergence Across the Family

The HSP90 family is functionally heterogeneous, comprising at least five major paralog groups with distinct subcellular localizations, client specificities, and regulatory mechanisms:

| Subfamily/Paralog | Gene Name (human) | Subcellular Localization | Taxonomic Distribution | Key Functions | Client Proteins | GO Annotation Suitability |
|---|---|---|---|---|---|---|
| HSP90α | **HSP90AA1** | Cytosol/nucleus; can also appear extracellularly in some metazoan contexts | Animals and other eukaryotes with cytosolic HSP90 isoforms; stress-inducible cytosolic paralog in mammals | ATP-dependent molecular chaperone; folding/maturation of signaling proteins; stress-responsive proteostasis; specialized extracellular and inflammation-linked roles in some animals (wei2024heatshockprotein pages 2-4, maiti2022cytosolichsp90isoformspecific pages 1-2, zuppini2025heatshockproteins pages 6-7) | Broad and heterogeneous client repertoire, especially signaling proteins such as kinases and steroid receptors; not a single fixed client set across taxa (hu2022heatshockproteins pages 2-4, singh2024heatshockresponse pages 9-11) | Safe only for broad core terms such as **ATP binding** and **protein folding/chaperone activity** if InterPro chooses to map them; **not** suitable for animal-specific localization, extracellular HSP90, inflammation, or cancer-process terms at the parent family level (zuppini2025heatshockproteins pages 6-7, wei2024heatshockprotein pages 2-4) |
| HSP90β | **HSP90AB1** | Cytosol/nucleus | Broadly conserved cytosolic eukaryotic paralog; constitutively expressed in mammals | Housekeeping ATP-dependent chaperone; essential constitutive proteostasis; overlaps with HSP90α but with isoform-specific developmental roles in mammals (wei2024heatshockprotein pages 2-4, maiti2022cytosolichsp90isoformspecific pages 1-2, maiti2022cytosolichsp90isoformspecific pages 2-4) | Broad signaling and proteostasis clients; not restricted to a single pathway or substrate class across all taxa (hu2022heatshockproteins pages 2-4, singh2024heatshockresponse pages 9-11) | Same as HSP90α: broad MF/BP terms may be defensible, but cytosolic-component terms and mammal-specific developmental/process terms should not be propagated from PTHR11528 to all members (maiti2022cytosolichsp90isoformspecific pages 1-2, zuppini2025heatshockproteins pages 6-7) |
| GRP94 / gp96 / endoplasmin | **HSP90B1** | Endoplasmic reticulum lumen | Eukaryotes with ER HSP90; reported absent from fungi (singh2024heatshockresponse pages 9-11) | ER-resident chaperone specialized for secreted and membrane protein biogenesis; calcium homeostasis; immune receptor biogenesis; ER stress-responsive rather than canonical heat-shock responsive (kim2021correctionkimet pages 2-4, kim2021cellsurfacegrp94 pages 2-4, wei2024heatshockprotein pages 2-4) | Toll-like receptors, integrins, immunoglobulins, glycoprotein IX, IGFs, proinsulin (kim2021correctionkimet pages 2-4, kim2021cellsurfacegrp94 pages 2-4, kim2021correctionkimet pages 14-15, kim2021cellsurfacegrp94 pages 14-15) | **Do not** assign ER component terms or immune-related process terms to the whole family, because these are GRP94-specific and absent from bacterial, mitochondrial, chloroplast, and fungal branches; child-entry mapping would be more appropriate (singh2024heatshockresponse pages 9-11, kim2021correctionkimet pages 2-4, kim2021cellsurfacegrp94 pages 2-4) |
| TRAP1 | **TRAP1** | Mitochondrial matrix/stroma | Eukaryotic mitochondrial HSP90 paralog; more similar to bacterial HtpG than to cytosolic HSP90 in some respects (basset2023thechaperonesystem pages 2-4, wei2024heatshockprotein pages 2-4) | Mitochondrial proteostasis and metabolic regulation; stress adaptation; functions autonomously without canonical HSP90 co-chaperones; higher ATP affinity than cytosolic HSP90 (wei2024heatshockprotein pages 2-4, albakova2022hsp70andhsp90 pages 5-6) | Interacts with mitochondrial/metabolic partners rather than the canonical broad cytosolic client system; examples include c-Src-associated and respiration-linked interactors (albakova2022hsp70andhsp90 pages 5-6) | **Do not** assign mitochondrial component terms, respiration/metabolism terms, or heat-response terms to all PTHR11528 matches; TRAP1 supports only broad family-core terms at the parent level (albakova2022hsp70andhsp90 pages 5-6, wei2024heatshockprotein pages 2-4) |
| HtpG | No human ortholog | Bacterial cytosol | Bacteria; HSP90 family generally absent from archaea (basset2023thechaperonesystem pages 2-4, wickramaratne2024hsp90ateam pages 2-4, hu2022heatshockproteins pages 2-4) | Bacterial ATP-dependent chaperone involved in protein quality control and stress response; often dispensable under standard conditions and functionally simpler than eukaryotic HSP90 systems (basset2023thechaperonesystem pages 2-4, wickramaratne2024hsp90ateam pages 2-4) | Bacterial proteostasis substrates; no universal eukaryotic-style client set or co-chaperone network (wickramaratne2024hsp90ateam pages 4-6, wickramaratne2024hsp90ateam pages 2-4) | Bacterial members make eukaryotic compartment/process terms clearly unsafe at the parent family level; only very broad core terms are candidates, while many eukaryotic pathway terms would over-annotate bacterial proteins (wickramaratne2024hsp90ateam pages 4-6, wickramaratne2024hsp90ateam pages 2-4, hu2022heatshockproteins pages 2-4) |
| HSP90C (chloroplast HSP90) | No human ortholog | Chloroplast/plastid | Plants and photosynthetic eukaryotes with plastids (maiti2022cytosolichsp90isoformspecific pages 1-2, maiti2022cytosolichsp90isoformspecific pages 2-4) | Plastid/chloroplast proteostasis; plant development and stress-related protein folding in plastids (maiti2022cytosolichsp90isoformspecific pages 1-2, maiti2022cytosolichsp90isoformspecific pages 2-4) | Plastid-localized protein-folding substrates; distinct from cytosolic, ER, mitochondrial, and bacterial client sets (maiti2022cytosolichsp90isoformspecific pages 2-4) | **Do not** assign chloroplast/plastid component or plant-development process terms to the whole family; these are lineage-specific and incompatible with animal, fungal, and bacterial members (maiti2022cytosolichsp90isoformspecific pages 1-2, maiti2022cytosolichsp90isoformspecific pages 2-4) |


*Table: This table summarizes the principal HSP90-family branches represented within PTHR11528, highlighting their compartment-specific biology and why only very broad core GO terms are plausible at the parent family level. It is useful for judging whether GO annotations should remain absent, stay broad, or be pushed down to child entries.*

### Key Divergences

**HSP90α vs. HSP90β (cytosolic isoforms):** In mammals, these two paralogs share 84–85% sequence identity but differ in regulation: HSP90α (encoded by HSP90AA1) is stress-inducible, while HSP90β (HSP90AB1) is constitutively expressed and essential for early embryonic development (maiti2022cytosolichsp90isoformspecific pages 1-2, maiti2022cytosolichsp90isoformspecific pages 2-4). HSP90α promotes chronic inflammation in cancer-associated fibroblasts, whereas HSP90β regulates lipid homeostasis and cell migration (wei2024heatshockprotein pages 2-4). The conformational dynamics of human HSP90 have evolved to populate broader ensembles of conformational states compared to yeast, based on changes at just two residues in otherwise conserved structural elements (mader2020conformationaldynamicsmodulate pages 1-2).

**GRP94 (HSP90B1/gp96/endoplasmin):** This ER-resident paralog shares approximately 50% homology with cytoplasmic HSP90 and is specialized for folding secreted and membrane-associated client proteins, including Toll-like receptors, integrins, immunoglobulins, glycoprotein IX, insulin-like growth factors, and proinsulin (kim2021correctionkimet pages 2-4, kim2021cellsurfacegrp94 pages 2-4, kim2021cellsurfacegrp94 pages 14-15). GRP94 is induced by ER stress rather than heat stress and functions as a master chaperone for innate immune receptor biogenesis (albakova2022hsp70andhsp90 pages 5-6, kim2021correctionkimet pages 14-15). Notably, GRP94 is reportedly absent from fungi (singh2024heatshockresponse pages 9-11), representing a significant taxonomic gap.

**TRAP1 (TNF receptor-associated protein 1):** The mitochondrial HSP90 paralog is more homologous to bacterial HtpG than to eukaryotic cytosolic HSP90 (basset2023thechaperonesystem pages 2-4). TRAP1 functions autonomously without co-chaperone assistance and has approximately 10-fold higher ATP affinity than cytosolic HSP90 (wei2024heatshockprotein pages 2-4). It plays a distinct role in mitochondrial metabolic regulation, mediating the balance between oxidative phosphorylation and glycolysis (albakova2022hsp70andhsp90 pages 5-6). Critically, TRAP1 does not respond to classical heat stress in the manner of cytosolic HSP90 isoforms (albakova2022hsp70andhsp90 pages 5-6).

**HtpG (bacterial HSP90):** Bacteria typically possess a single HSP90 homolog that is often dispensable under normal growth conditions (basset2023thechaperonesystem pages 2-4, wickramaratne2024hsp90ateam pages 2-4). Bacterial HtpG lacks the charged linker region and the MEEVD motif characteristic of eukaryotic cytosolic HSP90s, and operates without the complex co-chaperone network found in eukaryotes (wickramaratne2024hsp90ateam pages 4-6, basset2023thechaperonesystem pages 2-4).

**HSP90C (chloroplast HSP90):** Found exclusively in plants and photosynthetic eukaryotes, this paralog localizes to chloroplasts/plastids and participates in plastid-specific proteostasis and developmental signaling (maiti2022cytosolichsp90isoformspecific pages 1-2, maiti2022cytosolichsp90isoformspecific pages 2-4).

### Pseudo-enzymes and ATPase Dispensability

No true catalytically dead (pseudo-enzyme) HSP90 family members have been identified. However, recent work has demonstrated that the ATPase hydrolysis activity is surprisingly dispensable for viability: the E33A mutation, which completely blocks ATP hydrolysis, was initially considered lethal but has been shown to support cell viability in yeast, and hydrolysis-defective variants from multiple species—including both human isoforms and *S. pombe*—can sustain growth (reidy2025atpplaysa pages 1-2). This suggests that ATP may serve a structural role in promoting the conformational states required for client maturation, rather than being essential as an energy source (reidy2025atpplaysa pages 1-2).

---

## 4. Taxonomic Scope

HSP90 family members are distributed across bacteria and all major eukaryotic lineages but are **notably absent from archaea** (basset2023thechaperonesystem pages 2-4, wickramaratne2024hsp90ateam pages 2-4, hu2022heatshockproteins pages 2-4). The taxonomic distribution of paralogs is non-uniform:

- **Bacteria:** Single HtpG copy, often dispensable; present in most bacterial genomes (basset2023thechaperonesystem pages 2-4, wickramaratne2024hsp90ateam pages 2-4).
- **Fungi:** Cytosolic HSP90 isoforms present; GRP94 is absent (singh2024heatshockresponse pages 9-11).
- **Plants:** Cytosolic HSP90α/β, GRP94, TRAP1, and the unique chloroplast-localized HSP90C (maiti2022cytosolichsp90isoformspecific pages 1-2, maiti2022cytosolichsp90isoformspecific pages 2-4).
- **Animals:** HSP90α, HSP90β, GRP94, and TRAP1; mammals have the most complex co-chaperone network (maiti2022cytosolichsp90isoformspecific pages 1-2, maiti2022cytosolichsp90isoformspecific pages 2-4).
- **Protists:** Multiple HSP90 isoforms, including parasite-specific adaptations such as PfGp96 in *Plasmodium falciparum*.

The scale of PTHR11528 (43,519 proteins, 31,125 taxa, 32 subfamilies) reflects this enormous taxonomic and functional breadth. Any GO term mapped at this level propagates to bacterial, fungal, plant, animal, and protist proteins simultaneously, making compartment-specific or pathway-specific terms inherently risky.

**Cross-taxon applicability of universal terms:** The core molecular functions of ATP binding and chaperone-mediated protein folding are shared across all clades. However, specific biological processes (e.g., immune receptor biogenesis for GRP94, mitochondrial metabolic regulation for TRAP1, heat stress response for cytosolic HSP90α) are strictly lineage- and paralog-specific.

---

## 5. Over-Annotation Verdict

### Current State Assessment

The absence of InterPro2GO mappings for PTHR11528 is **largely appropriate** given the substantial functional heterogeneity across the 32 subfamilies. The family spans five major paralog groups (HSP90α, HSP90β, GRP94, TRAP1, HtpG, plus plant HSP90C) with distinct subcellular localizations (cytosol, ER, mitochondria, chloroplast, bacterial cytoplasm), different client repertoires, different co-chaperone dependencies, and different stress-response profiles.

### Recommended GO Action Pattern

| Category | Verdict |
|---|---|
| **Overall assessment** | Current no-mapping state is defensible but slightly conservative |
| **Molecular Function terms** | **MODIFY-to-specific**: A small set of core MF terms could be safely added — specifically GO:0005524 (ATP binding) and GO:0051082 (unfolded protein binding), as these are structurally and functionally universal across all HSP90 paralogs |
| **Biological Process terms** | **KEEP_AS_NON_CORE**: GO:0006457 (protein folding) could potentially be added as a broad-level annotation, but more specific process terms (response to heat, immune function, metabolic regulation) must remain at the subfamily level |
| **Cellular Component terms** | **REMOVE / DO NOT MAP**: No CC term is appropriate at this level; all compartment localizations are paralog-specific |

### Recommendations for InterPro

1. **For PTHR11528 (parent family):** Consider adding only the most universal GO terms: GO:0005524 (ATP binding) and GO:0051082 (unfolded protein binding) as Molecular Function annotations, and GO:0006457 (protein folding) as a Biological Process annotation. These three terms are supported across all major paralogs and taxa.

2. **For subfamily/child entries:** Compartment-specific, process-specific, and client-specific GO terms should be mapped at the appropriate PANTHER subfamily level (e.g., TRAP1 subfamily → GO:0005739 mitochondrion; GRP94 subfamily → GO:0005783 endoplasmic reticulum; cytosolic HSP90 subfamilies → GO:0005737 cytoplasm). Terms relating to immune receptor folding, metabolic regulation, and heat stress response should similarly be restricted to their respective subfamilies.

3. **Avoid mapping to the parent family:** GO terms for response to heat (GO:0009408), chaperone binding (GO:0051087), any Cellular Component term, and any disease- or pathway-specific process terms.

This approach balances the desire to capture the family's conserved core biochemistry while respecting the significant functional diversification that has occurred across its 32 subfamilies spanning bacteria to humans.

References

1. (wickramaratne2024hsp90ateam pages 4-6): Anushka C. Wickramaratne, Sue Wickner, and Andrea N. Kravats. Hsp90, a team player in protein quality control and the stress response in bacteria. Microbiology and Molecular Biology Reviews, Jun 2024. URL: https://doi.org/10.1128/mmbr.00176-22, doi:10.1128/mmbr.00176-22. This article has 18 citations and is from a domain leading peer-reviewed journal.

2. (minari2024newinsightsinto pages 8-10): Karine Minari, Vitor Hugo Balasco Serrão, and Júlio César Borges. New insights into hsp90 structural plasticity revealed by cryoem. BioChem, 4:62-89, Apr 2024. URL: https://doi.org/10.3390/biochem4020004, doi:10.3390/biochem4020004. This article has 7 citations.

3. (prodromou2022advancestowardsunderstanding pages 1-3): Chrisostomos Prodromou and Dennis M. Bjorklund. Advances towards understanding the mechanism of action of the hsp90 complex. Biomolecules, 12:600, Apr 2022. URL: https://doi.org/10.3390/biom12050600, doi:10.3390/biom12050600. This article has 55 citations.

4. (basset2023thechaperonesystem pages 2-4): Charbel A. Basset, Everly Conway de Macario, Lavinia Giovanna Leone, Alberto J.L. Macario, and Angelo Leone. The chaperone system in cancer therapies: hsp90. Journal of Molecular Histology, 54:105-118, Mar 2023. URL: https://doi.org/10.1007/s10735-023-10119-8, doi:10.1007/s10735-023-10119-8. This article has 40 citations and is from a peer-reviewed journal.

5. (mader2020conformationaldynamicsmodulate pages 1-2): Sophie L. Mader, Abraham Lopez, Jannis Lawatscheck, Qi Luo, Daniel A. Rutz, Ana P. Gamiz-Hernandez, Michael Sattler, Johannes Buchner, and Ville R. I. Kaila. Conformational dynamics modulate the catalytic activity of the molecular chaperone hsp90. Nature Communications, Mar 2020. URL: https://doi.org/10.1038/s41467-020-15050-0, doi:10.1038/s41467-020-15050-0. This article has 100 citations and is from a highest quality peer-reviewed journal.

6. (prodromou2022advancestowardsunderstanding pages 3-4): Chrisostomos Prodromou and Dennis M. Bjorklund. Advances towards understanding the mechanism of action of the hsp90 complex. Biomolecules, 12:600, Apr 2022. URL: https://doi.org/10.3390/biom12050600, doi:10.3390/biom12050600. This article has 55 citations.

7. (minari2024newinsightsinto pages 6-8): Karine Minari, Vitor Hugo Balasco Serrão, and Júlio César Borges. New insights into hsp90 structural plasticity revealed by cryoem. BioChem, 4:62-89, Apr 2024. URL: https://doi.org/10.3390/biochem4020004, doi:10.3390/biochem4020004. This article has 7 citations.

8. (zuppini2025heatshockproteins pages 6-7): Francesca Zuppini, Lucia Renzullo, Francesca Tornatore, Pietro Poggio, and Mara Brancaccio. Heat shock proteins at the crossroads of endosomal trafficking pathways. Cell Biology and Toxicology, Dec 2025. URL: https://doi.org/10.1007/s10565-025-10101-y, doi:10.1007/s10565-025-10101-y. This article has 4 citations and is from a peer-reviewed journal.

9. (hu2022heatshockproteins pages 2-4): Chen Hu, Jing Yang, Ziping Qi, Hong Wu, Beilei Wang, Fengming Zou, Husheng Mei, Jing Liu, Wenchao Wang, and Qingsong Liu. Heat shock proteins: biological functions, pathological roles, and therapeutic opportunities. MedComm, Aug 2022. URL: https://doi.org/10.1002/mco2.161, doi:10.1002/mco2.161. This article has 905 citations.

10. (kim2021correctionkimet pages 2-4): J. W. Kim, Yea Bin Cho, and Sukmook Lee. Correction: kim et al. cell surface grp94 as a novel emerging therapeutic target for monoclonal antibody cancer therapy. cells 2021, 10, 670. Cells, 10:1198, May 2021. URL: https://doi.org/10.3390/cells10051198, doi:10.3390/cells10051198. This article has 1 citations.

11. (kim2021cellsurfacegrp94 pages 2-4): Ji Woong Kim, Yea Bin Cho, and Sukmook Lee. Cell surface grp94 as a novel emerging therapeutic target for monoclonal antibody cancer therapy. Cells, 10:670, Mar 2021. URL: https://doi.org/10.3390/cells10030670, doi:10.3390/cells10030670. This article has 46 citations.

12. (singh2024heatshockresponse pages 9-11): Manish Kumar Singh, Yoonhwa Shin, Songhyun Ju, Sunhee Han, Wonchae Choe, Kyung-Sik Yoon, Sung Soo Kim, and Insug Kang. Heat shock response and heat shock proteins: current understanding and future opportunities in human diseases. International Journal of Molecular Sciences, 25:4209, Apr 2024. URL: https://doi.org/10.3390/ijms25084209, doi:10.3390/ijms25084209. This article has 232 citations.

13. (wei2024heatshockprotein pages 2-4): Huiyun Wei, Yingying Zhang, Yilin Jia, Xunan Chen, Tengda Niu, Aniruddha Chatterjee, Pengxing He, and Guiqin Hou. Heat shock protein 90: biological functions, diseases, and therapeutic targets. MedComm, Jan 2024. URL: https://doi.org/10.1002/mco2.470, doi:10.1002/mco2.470. This article has 106 citations.

14. (albakova2022hsp70andhsp90 pages 5-6): Zarema Albakova, Yana Mangasarova, Akhmet Albakov, and Liliya Gorenkova. Hsp70 and hsp90 in cancer: cytosolic, endoplasmic reticulum and mitochondrial chaperones of tumorigenesis. Frontiers in Oncology, Jan 2022. URL: https://doi.org/10.3389/fonc.2022.829520, doi:10.3389/fonc.2022.829520. This article has 94 citations.

15. (maiti2022cytosolichsp90isoformspecific pages 1-2): Samarpan Maiti and Didier Picard. Cytosolic hsp90 isoform-specific functions and clinical significance. Biomolecules, 12:1166, Aug 2022. URL: https://doi.org/10.3390/biom12091166, doi:10.3390/biom12091166. This article has 93 citations.

16. (maiti2022cytosolichsp90isoformspecific pages 2-4): Samarpan Maiti and Didier Picard. Cytosolic hsp90 isoform-specific functions and clinical significance. Biomolecules, 12:1166, Aug 2022. URL: https://doi.org/10.3390/biom12091166, doi:10.3390/biom12091166. This article has 93 citations.

17. (kim2021correctionkimet pages 14-15): J. W. Kim, Yea Bin Cho, and Sukmook Lee. Correction: kim et al. cell surface grp94 as a novel emerging therapeutic target for monoclonal antibody cancer therapy. cells 2021, 10, 670. Cells, 10:1198, May 2021. URL: https://doi.org/10.3390/cells10051198, doi:10.3390/cells10051198. This article has 1 citations.

18. (kim2021cellsurfacegrp94 pages 14-15): Ji Woong Kim, Yea Bin Cho, and Sukmook Lee. Cell surface grp94 as a novel emerging therapeutic target for monoclonal antibody cancer therapy. Cells, 10:670, Mar 2021. URL: https://doi.org/10.3390/cells10030670, doi:10.3390/cells10030670. This article has 46 citations.

19. (wickramaratne2024hsp90ateam pages 2-4): Anushka C. Wickramaratne, Sue Wickner, and Andrea N. Kravats. Hsp90, a team player in protein quality control and the stress response in bacteria. Microbiology and Molecular Biology Reviews, Jun 2024. URL: https://doi.org/10.1128/mmbr.00176-22, doi:10.1128/mmbr.00176-22. This article has 18 citations and is from a domain leading peer-reviewed journal.

20. (reidy2025atpplaysa pages 1-2): Michael Reidy and Daniel C. Masison. Atp plays a structural role in hsp90 function. Nature communications, 16 1:6710, Jul 2025. URL: https://doi.org/10.1038/s41467-025-61962-0, doi:10.1038/s41467-025-61962-0. This article has 7 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PTHR11528-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR11528-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. basset2023thechaperonesystem pages 2-4
2. mader2020conformationaldynamicsmodulate pages 1-2
3. prodromou2022advancestowardsunderstanding pages 3-4
4. hu2022heatshockproteins pages 2-4
5. wei2024heatshockprotein pages 2-4
6. singh2024heatshockresponse pages 9-11
7. reidy2025atpplaysa pages 1-2
8. minari2024newinsightsinto pages 8-10
9. prodromou2022advancestowardsunderstanding pages 1-3
10. minari2024newinsightsinto pages 6-8
11. zuppini2025heatshockproteins pages 6-7
12. kim2021correctionkimet pages 2-4
13. kim2021correctionkimet pages 14-15
14. https://doi.org/10.1128/mmbr.00176-22,
15. https://doi.org/10.3390/biochem4020004,
16. https://doi.org/10.3390/biom12050600,
17. https://doi.org/10.1007/s10735-023-10119-8,
18. https://doi.org/10.1038/s41467-020-15050-0,
19. https://doi.org/10.1007/s10565-025-10101-y,
20. https://doi.org/10.1002/mco2.161,
21. https://doi.org/10.3390/cells10051198,
22. https://doi.org/10.3390/cells10030670,
23. https://doi.org/10.3390/ijms25084209,
24. https://doi.org/10.1002/mco2.470,
25. https://doi.org/10.3389/fonc.2022.829520,
26. https://doi.org/10.3390/biom12091166,
27. https://doi.org/10.1038/s41467-025-61962-0,