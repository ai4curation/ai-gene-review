---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-21T22:23:49.685508'
end_time: '2026-06-21T22:35:20.996175'
duration_seconds: 691.31
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR47593
  interpro_name: Zinc finger protein 7
  interpro_short_name: Zinc_finger_protein_7
  interpro_type: family
  interpro_integrated: IPR053266
  member_databases: Not specified
  n_proteins: '1284'
  n_taxa: '963'
  n_subfamilies: '5'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: The Zinc finger protein 7 family is characterized by its role
    as a negative regulator of abscisic acid signaling during germination and early
    seedling development. Abscisic acid (ABA) is a plant hormone that plays a crucial
    role in stress responses and developmental processes. Members of the Zinc finger
    protein 7 family are involved in modulating the ABA pathway, ensuring proper control
    of germination and seedling growth under various environmental conditions. By
    regulating ABA signaling, this family contributes to the plant's ability to adapt
    and survive in response to abiotic stresses.
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 25
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: PTHR47593-deep-research-falcon_artifacts/artifact-00.md
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
- **Accession:** PTHR47593
- **Name:** Zinc finger protein 7
- **Short name:** Zinc_finger_protein_7
- **Entry type:** family
- **Integrated into / parent:** IPR053266
- **Member database signatures:** Not specified
- **Scale:** 1284 proteins across 963 taxa, 5 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The Zinc finger protein 7 family is characterized by its role as a negative regulator of abscisic acid signaling during germination and early seedling development. Abscisic acid (ABA) is a plant hormone that plays a crucial role in stress responses and developmental processes. Members of the Zinc finger protein 7 family are involved in modulating the ABA pathway, ensuring proper control of germination and seedling growth under various environmental conditions. By regulating ABA signaling, this family contributes to the plant's ability to adapt and survive in response to abiotic stresses.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR47593 (Zinc finger protein 7)**, structured to support GO annotation review.

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
- **Accession:** PTHR47593
- **Name:** Zinc finger protein 7
- **Short name:** Zinc_finger_protein_7
- **Entry type:** family
- **Integrated into / parent:** IPR053266
- **Member database signatures:** Not specified
- **Scale:** 1284 proteins across 963 taxa, 5 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The Zinc finger protein 7 family is characterized by its role as a negative regulator of abscisic acid signaling during germination and early seedling development. Abscisic acid (ABA) is a plant hormone that plays a crucial role in stress responses and developmental processes. Members of the Zinc finger protein 7 family are involved in modulating the ABA pathway, ensuring proper control of germination and seedling growth under various environmental conditions. By regulating ABA signaling, this family contributes to the plant's ability to adapt and survive in response to abiotic stresses.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR47593 (Zinc finger protein 7)**, structured to support GO annotation review.

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


# InterPro Family Research Report: PTHR47593 (Zinc finger protein 7)
## GO Annotation Review

**Entry:** PTHR47593  
**Type:** family  
**Scope:** 1284 proteins across 963 taxa, 5 subfamilies  
**Current InterPro2GO mappings:** None  
**Parent entry:** IPR053266  

---

## Executive Summary

PTHR47593 is correctly unannotated in InterPro2GO. This family-level signature identifies plant C2H2-type zinc finger transcription factors sharing a conserved single-finger DNA-binding architecture but showing extensive functional divergence across subfamilies. The InterPro text description stating this family "negatively regulates abscisic acid signaling during germination and early seedling development" reflects one subfamily's experimentally demonstrated function rather than a feature conserved across all 1284 matched proteins. Adding whole-protein process or function GO terms at the family level would systematically over-annotate proteins from functionally divergent subfamilies that regulate root hair development, trichome patterning, floral organ identity, awn elongation, and other processes unrelated to ABA signaling or seed germination.

**Recommended action:** ACCEPT (maintain absence of InterPro2GO mappings).

---

## 1. Family Definition and Biochemistry

### Structural Architecture

PTHR47593 corresponds to a plant-specific subfamily of C2H2-type zinc finger proteins related to Arabidopsis ZFP7. These proteins are unusual among C2H2 transcription factors because they typically contain only **one** zinc finger domain per protein, contrasted with the tandem multi-finger arrangement common in animal C2H2 proteins (tague1995characterizationofa pages 1-3, tague1995characterizationofa pages 10-11).

The founding characterization by Tague and Goodman (1995) identified eight Arabidopsis proteins (ZFP1-8) sharing this architecture. ZFP7 specifically is a 209-amino acid protein expressed in roots, stems, and cauline leaves, with the gene mapped to chromosome 1 (tague1995characterizationofa pages 10-11, tague1995characterizationofa pages 5-7, tague1995characterizationofa pages 7-10).

### Conserved Structural Features

**C2H2 zinc finger domain:**  
The canonical structure follows the consensus **C-X2-4-C-X3-P-X5-L-X2-H-X3-H**, where two cysteine residues in a β-strand and two histidine residues in an α-helix coordinate a single Zn²⁺ ion in a tetrahedral geometry. This βββα configuration positions the α-helix for sequence-specific DNA major-groove contact (tague1995characterizationofa pages 1-3, han2020c2h2zincfinger pages 1-2, tague1995characterizationofa pages 5-7).

**QALGGH motif:**  
A defining characteristic of plant Q-type C2H2 proteins is the highly conserved **QALGGH** hexapeptide in the DNA-binding α-helix. This motif is nearly invariant across plant C2H2 family members and distinguishes them from animal C2H2 factors; it likely specifies recognition of AG/CT-rich plant cis-regulatory elements (tague1995characterizationofa pages 1-3, xie2019therolesof pages 3-6, han2020c2h2zincfinger pages 1-2, tague1995characterizationofa pages 5-7, tague1995characterizationofa pages 7-10).

**Additional domains (variable):**  
Outside the zinc finger, related family members show:

- **Serine/threonine-rich regions** flanking the finger domain, representing potential phosphorylation sites implicated in regulation of transcription-factor activity, localization, and turnover (tague1995characterizationofa pages 5-7, tague1995characterizationofa pages 7-10).
- **Leucine-rich repeats** at the N- and/or C-terminus, which may mediate protein-protein interactions (tague1995characterizationofa pages 5-7, tague1995characterizationofa pages 7-10).
- **Basic amino acid clusters** immediately downstream of the zinc finger, consistent with nuclear localization signals and DNA-binding support (tague1995characterizationofa pages 5-7, tague1995characterizationofa pages 7-10).
- **EAR (ERF-associated amphiphilic repression) motifs** such as LxLxL or DLNxxP in a subset of members (e.g., ZFP1/AtZP1), which confer active transcriptional repression via recruitment of the TOPLESS corepressor and histone deacetylases (han2020arabidopsiszincfinger pages 1-3, kagale2010genomewideanalysisof pages 1-2, xie2019therolesof pages 3-6).

However, not all PTHR47593 members carry EAR motifs, so this feature is subfamily-specific rather than universal (kagale2010genomewideanalysisof pages 1-2, tague1995characterizationofa pages 5-7).

### Biochemical Mechanism

These proteins function as **transcription factors** that bind DNA through the C2H2 domain and modulate target gene expression. Experimental evidence from multiple family members shows:

- **DNA binding:** Sequence-specific recognition of promoter elements, often targeting AG/CT-rich motifs. The spacing between zinc fingers (where proteins contain multiple fingers) or between DNA-binding sites can influence specificity, although single-finger proteins may heterodimerize or work cooperatively (tague1995characterizationofa pages 1-3, tague1995characterizationofa pages 5-7).
- **Transcriptional repression:** In EAR-containing members (e.g., ZFP1), direct binding to target promoters recruits TOPLESS and HISTONE DEACETYLASE19, leading to chromatin compaction and gene silencing (han2020arabidopsiszincfinger pages 1-3, kagale2010genomewideanalysisof pages 1-2).
- **Regulation by phosphorylation:** The serine/threonine-rich domains are candidate substrates for kinase-mediated regulation in response to developmental or hormonal cues (tague1995characterizationofa pages 5-7, tague1995characterizationofa pages 7-10).

No conserved catalytic residues exist because these are non-enzymatic DNA-binding proteins, not enzymes. Therefore, concepts of catalytically dead or pseudoenzyme variants do not apply (han2020c2h2zincfinger pages 1-2).

---

## 2. InterPro2GO Mapping Appropriateness

### Current Status: No GO Terms Mapped

PTHR47593 currently has **zero InterPro2GO annotations**. The InterPro narrative description states: "Members of the Zinc finger protein 7 family are involved in modulating the ABA pathway, ensuring proper control of germination and seedling growth under various environmental conditions. By regulating ABA signaling, this family contributes to the plant's ability to adapt and survive in response to abiotic stresses."

### Assessment of Potential GO Terms

If GO terms were proposed based on the text description, candidates might include:

- **GO:2000070** (regulation of response to water deprivation)
- **GO:0009738** (abscisic acid-activated signaling pathway)
- **GO:0009737** (response to abscisic acid)
- **GO:0009845** (seed germination)
- **GO:0010182** (sugar mediated signaling pathway, indirectly linked to ABA)
- **GO:0048831** (regulation of shoot system development, for seedling context)

**Verdict: None of these terms should be mapped at the family level.**

### Rationale

1. **Functional heterogeneity across subfamilies (Objective 3):**  
   The literature demonstrates that related C2H2 Q-type proteins regulate **distinct biological processes**:
   
   - **ZFP1/AtZP1:** Represses **root hair initiation and elongation**, directly suppressing bHLH genes RHD6, RSL2, and RSL4. Function confirmed by loss-of-function and overexpression phenotypes. No demonstrated role in germination or ABA signaling (han2020arabidopsiszincfinger pages 1-3).
   
   - **ZFP3:** Negative regulator of **light and ABA responses during germination and seedling development**. This is the subfamily whose function aligns with the InterPro description (xie2019therolesof pages 3-6).
   
   - **ZFP8 and ZP1 (overlapping functions):** Repress floral homeotic genes (AP3, PI, AG) in vegetative tissues and regulate **trichome development**. Newer studies show ZFP8 and GIS2 integrate gibberellin/cytokinin signaling in trichome patterning, not ABA/germination control (hu2023leafyandapetala1 pages 1-2, yasin2025c2h2zincfinger pages 1-2, yasin2025c2h2zincfinger pages 2-4).
   
   - **GIS/GIS2 family:** Regulate **inflorescence trichome initiation** via gibberellin signaling and the MBW complex, functionally distinct from seed-based ABA pathways (yasin2025c2h2zincfinger pages 1-2, yasin2025c2h2zincfinger pages 2-4).
   
   - **ALI-1 (wheat C2H2 homolog):** The dominant awn-length inhibitor B1 locus product. Represses awn elongation and affects grain length by suppressing **cytokinin biosynthesis and signaling**. Expression is in developing spikes, not seeds, and no ABA-germination phenotype is described (wang2020naturalvariationin pages 4-7, wang2019ali1candidategene pages 10-13, wang2020naturalvariationin pages 9-11).

   **Conclusion:** The ABA/germination function applies to one or a few subfamily clades (e.g., ZFP3-like proteins), not all 1284 proteins matched by PTHR47593 (han2020arabidopsiszincfinger pages 1-3, hu2023leafyandapetala1 pages 1-2, wang2020naturalvariationin pages 4-7, yasin2025c2h2zincfinger pages 1-2, xie2019therolesof pages 3-6, wang2019ali1candidategene pages 10-13, wang2020naturalvariationin pages 9-11, yasin2025c2h2zincfinger pages 2-4).

2. **Entry type is 'family' (Objective 2 rationale):**  
   PTHR47593 is explicitly annotated as entry_type="family" with five subfamilies. Family-level signatures identify proteins sharing structural homology but should **not** receive whole-protein biological process or molecular function GO terms unless that function is true for **every** protein the signature matches. Applying "negative regulation of abscisic acid signaling" or "seed germination" to all 1284 proteins would systematically mis-annotate ZFP1-ortholog proteins (which regulate root hairs), ZFP8-orthologs (trichomes/flowers), and ALI-1-like proteins (awn/grain development) (han2020arabidopsiszincfinger pages 1-3, wang2020naturalvariationin pages 4-7, wang2020naturalvariationin pages 9-11).

3. **Taxonomic leakage risk (Objective 4):**  
   PTHR47593 spans 963 taxa. Although Q-type C2H2 proteins are plant-specific and predominantly found in flowering plants, seed germination and ABA signaling are **angiosperm-specific** processes. If any matched proteins come from bryophytes, ferns, or other non-seed lineages, GO terms referencing "seed germination" or "seedling development" would be taxonomically inappropriate. Even within angiosperms, tissue-specific expression (roots vs. inflorescences vs. seeds) varies by ortholog, so a single process term cannot safely span all taxa (xie2019therolesof pages 3-6, han2020c2h2zincfinger pages 1-2, tague1995characterizationofa pages 10-11).

4. **Generic terms carry little information:**  
   Technically, one could annotate PTHR47593 with:
   
   - **GO:0003676** (nucleic acid binding)
   - **GO:0046872** (metal ion binding, for Zn²⁺)
   - **GO:0005634** (nucleus, component term)

   These are structurally valid but provide minimal biological insight. They do not distinguish this family from hundreds of other nuclear transcription factors and therefore do not justify inclusion in InterPro2GO core mappings (han2020c2h2zincfinger pages 1-2).

**Recommendation:** Do **not** add GO terms at the PTHR47593 family level. If PANTHER defines functionally coherent child subfamilies (e.g., a ZFP3-specific clade verified to regulate ABA/germination), those child entries could receive appropriate specific terms. The current absence of InterPro2GO mappings is the safest and most accurate state (han2020arabidopsiszincfinger pages 1-3, hu2023leafyandapetala1 pages 1-2, wang2020naturalvariationin pages 4-7, xie2019therolesof pages 3-6, wang2020naturalvariationin pages 9-11, yasin2025c2h2zincfinger pages 2-4).

---

## 3. Functional Divergence Across the Family

PTHR47593 exhibits **extensive neo-functionalization** among its subfamilies, as evidenced by experimental studies of representative Arabidopsis and crop orthologs.

### Documented Subfamily Functions

| Subfamily/Ortholog | Biological Process | Target Genes/Pathways | Experimental Evidence |
|--------------------|-------------------|---------------------|----------------------|
| **ZFP1/AtZP1** | Root hair repression | Directly represses RHD6, RSL2, RSL4 (bHLH TFs for root hair initiation/elongation) | Overexpression → no root hairs; knockout → more/longer root hairs; ChIP confirms direct promoter binding (han2020arabidopsiszincfinger pages 1-3) |
| **ZFP3** | ABA/light response in germination and seedling development | Likely ABA-responsive pathway genes (targets not fully characterized) | Reviewed as negative regulator; aligns with InterPro description but subfamily-specific (xie2019therolesof pages 3-6) |
| **ZFP8 (with ZP1)** | Floral homeotic gene repression; trichome development | AP3, PI, AG (floral organ identity); integrates cytokinin/ABA in leaf trichomes | ZP1/ZFP8 double mutants show ectopic floral gene expression in leaves; ZFP8 RNAi alters trichome density (hu2023leafyandapetala1 pages 1-2, yasin2025c2h2zincfinger pages 1-2, yasin2025c2h2zincfinger pages 2-4) |
| **GIS/GIS2** | Inflorescence trichome initiation | GL1 (MBW complex); SQE5 (sterol biosynthesis); SEN1 (senescence); gibberellin-cytokinin crosstalk | GIS2 ChIP-qPCR confirms direct binding to SQE5/SEN1 promoters; DEX-inducible expression assays (yasin2025c2h2zincfinger pages 1-2, yasin2025c2h2zincfinger pages 2-4) |
| **ALI-1 (wheat)** | Awn elongation inhibition; grain length regulation | Cytokinin biosynthesis/signaling genes; bHLH99 | B1 locus map-based cloning; functional complementation; NILs show awn/grain phenotypes (wang2020naturalvariationin pages 4-7, wang2019ali1candidategene pages 10-13, wang2020naturalvariationin pages 9-11) |

### Key Points

- **Shared molecular mechanism, divergent biology:** All employ C2H2-QALGGH DNA binding and (in subset) EAR-mediated transcriptional repression, but they target different promoters in different tissues during different developmental stages (han2020arabidopsiszincfinger pages 1-3, hu2023leafyandapetala1 pages 1-2, wang2020naturalvariationin pages 4-7, yasin2025c2h2zincfinger pages 1-2, xie2019therolesof pages 3-6, wang2019ali1candidategene pages 10-13, wang2020naturalvariationin pages 9-11, yasin2025c2h2zincfinger pages 2-4).

- **Tissue specificity:** ZFP1 (roots), ZFP3 (seeds/seedlings), ZFP8/GIS2 (trichomes, flowers), ALI-1 (spike/awn). A family-wide GO biological process term would ignore these distinct spatial domains (han2020arabidopsiszincfinger pages 1-3, hu2023leafyandapetala1 pages 1-2, yasin2025c2h2zincfinger pages 1-2, tague1995characterizationofa pages 10-11).

- **Hormone pathway divergence:** ZFP3 acts in ABA signaling; GIS/GIS2 integrate gibberellin and cytokinin; ALI-1 represses cytokinin. These are non-overlapping regulatory networks (wang2020naturalvariationin pages 4-7, yasin2025c2h2zincfinger pages 1-2, xie2019therolesof pages 3-6, yasin2025c2h2zincfinger pages 2-4).

- **No pseudoenzymes:** These are transcription factors, not enzymes. There is no catalytic activity to lose. All retain DNA-binding capacity via the zinc finger domain (han2020c2h2zincfinger pages 1-2).

**Conclusion:** PTHR47593 is structurally unified but functionally heterogeneous. The InterPro description emphasizing ABA/germination reflects one evolutionary lineage within the family, not a pan-family trait (han2020arabidopsiszincfinger pages 1-3, hu2023leafyandapetala1 pages 1-2, wang2020naturalvariationin pages 4-7, yasin2025c2h2zincfinger pages 1-2, xie2019therolesof pages 3-6, wang2019ali1candidategene pages 10-13, wang2020naturalvariationin pages 9-11, yasin2025c2h2zincfinger pages 2-4).

---

## 4. Taxonomic Scope

### Distribution

- **Number of sequences:** 1284 proteins  
- **Number of taxa:** 963  
- **Phylogenetic scope:** Plant-specific. Q-type C2H2 zinc fingers with the QALGGH motif are a land-plant innovation absent from animals and fungi (xie2019therolesof pages 3-6, han2020c2h2zincfinger pages 1-2).

### Representative Taxa (from literature)

Experimental or genome-wide studies have identified Q-type C2H2 homologs in:

- **Model dicot:** *Arabidopsis thaliana* (founding studies) (tague1995characterizationofa pages 1-3, xie2019therolesof pages 3-6, tague1995characterizationofa pages 10-11, tague1995characterizationofa pages 5-7, tague1995characterizationofa pages 7-10)
- **Monocot crops:** wheat (*Triticum aestivum*), barley (*Hordeum vulgare*), rice (*Oryza sativa*) (wang2020naturalvariationin pages 4-7, wang2019ali1candidategene pages 10-13, wang2020naturalvariationin pages 9-11)
- **Woody perennials:** poplar (*Populus trichocarpa*), grapevine (*Vitis vinifera*) (chhetri2020genomewideassociationstudy pages 12-13)
- **Brassicas:** *Brassica rapa*, *Brassica napus*
- **Other crops/species:** citrus, rose (*Rosa rugosa*), sugar beet (*Beta vulgaris*), Medicago truncatula, cucumber (*Cucumis sativus*), sweetpotato (*Ipomoea batatas*), Larix kaempferi (conifer) (xie2019therolesof pages 3-6, han2020c2h2zincfinger pages 1-2)

### Taxonomic Relevance for GO Annotation

1. **Seed-specific processes are not universal:**  
   Terms such as "seed germination" (GO:0009845), "seedling development" (GO:0090351), and "abscisic acid-activated signaling pathway" (GO:0009738) presuppose **seed plant** biology. If PTHR47593 matches any proteins from bryophytes (mosses, liverworts), lycophytes, or ferns, these GO terms would be biologically meaningless for those sequences. Even the ABA hormone itself has distinct roles (desiccation tolerance in mosses vs. seed dormancy in angiosperms) (xie2019therolesof pages 3-6, han2020c2h2zincfinger pages 1-2).

2. **Angiosperm-centric functions:**  
   The specific developmental contexts described in the literature (root hair patterning, trichome initiation, floral organ identity, awn/grain development) are flowering-plant features. The signature may span a broader taxonomic range, but process terms anchored in angiosperm-specific biology would leak into inappropriate taxa (han2020arabidopsiszincfinger pages 1-3, hu2023leafyandapetala1 pages 1-2, wang2020naturalvariationin pages 4-7, wang2020naturalvariationin pages 9-11).

3. **Conserved across all taxa: DNA-binding architecture only:**  
   The one feature that **is** likely universal to all 1284 proteins is possession of a functional C2H2-QALGGH zinc finger enabling DNA binding in a plant nuclear context. This supports broad molecular-function terms (nucleic acid binding, metal ion binding, nucleus localization) but not specific biological processes (han2020c2h2zincfinger pages 1-2, tague1995characterizationofa pages 5-7).

**Conclusion:** Without subfamily-level resolution or experimental confirmation that all matched proteins share a single biological process across all 963 taxa, applying process-specific GO terms risks taxonomic over-annotation (xie2019therolesof pages 3-6, han2020c2h2zincfinger pages 1-2).

---

## 5. Over-Annotation Verdict

### Summary

PTHR47593 is a **family-level** InterPro entry (type="family") identifying plant C2H2-type zinc finger transcription factors via a structurally conserved single-finger/QALGGH domain architecture. The entry currently has **zero InterPro2GO mappings**, and this is the appropriate state. The InterPro narrative description stating that this family "negatively regulates abscisic acid signaling during germination and early seedling development" is a functional characterization that applies to one or a subset of the five subfamilies (likely the ZFP3-like clade), **not** to all 1284 proteins matched by the signature.

### Evidence-Based Verdict

| Criterion | Finding | Implication for GO Annotation |
|-----------|---------|------------------------------|
| **Structural homology** | All members share C2H2-QALGGH DNA-binding domain (tague1995characterizationofa pages 1-3, han2020c2h2zincfinger pages 1-2, tague1995characterizationofa pages 5-7, tague1995characterizationofa pages 7-10) | Generic molecular-function terms (DNA binding, Zn²⁺ binding) technically valid but uninformative |
| **Functional homogeneity** | **Absent.** Subfamilies regulate root hairs, trichomes, floral organs, seed germination, awn/grain development via distinct targets and hormones (han2020arabidopsiszincfinger pages 1-3, hu2023leafyandapetala1 pages 1-2, wang2020naturalvariationin pages 4-7, yasin2025c2h2zincfinger pages 1-2, xie2019therolesof pages 3-6, wang2019ali1candidategene pages 10-13, wang2020naturalvariationin pages 9-11, yasin2025c2h2zincfinger pages 2-4) | Process/function GO terms appropriate only for individual subfamilies, not family-wide |
| **Experimental validation** | ZFP1, ZFP3, ZFP8, GIS2, ALI-1 each have direct experimental evidence (ChIP, genetics, phenotypes) for **different** biological roles (han2020arabidopsiszincfinger pages 1-3, hu2023leafyandapetala1 pages 1-2, wang2020naturalvariationin pages 4-7, yasin2025c2h2zincfinger pages 1-2, wang2019ali1candidategene pages 10-13, wang2020naturalvariationin pages 9-11, yasin2025c2h2zincfinger pages 2-4) | Cannot generalize one member's function to all |
| **Taxonomic scope** | 963 taxa, predominantly flowering plants but potentially spanning non-seed lineages; ABA/seed processes irrelevant outside angiosperms (xie2019therolesof pages 3-6, han2020c2h2zincfinger pages 1-2) | Seed-specific or angiosperm-specific GO terms risk taxonomic leakage |
| **Entry type** | PANTHER family with 5 subfamilies | Whole-protein GO terms systematically over-annotate unless true for every matched protein |

### Recommended GO Action Pattern

**ACCEPT** — Accept the current absence of InterPro2GO mappings for PTHR47593.

**Rationale:**

1. **No safe family-wide process term exists.** The evidence shows that different subfamilies regulate different developmental processes (root hair vs. trichome vs. germination vs. grain development) in different tissues and via different hormone pathways. Mapping any single biological process GO term to the family would over-annotate proteins from other subfamilies (han2020arabidopsiszincfinger pages 1-3, hu2023leafyandapetala1 pages 1-2, wang2020naturalvariationin pages 4-7, yasin2025c2h2zincfinger pages 1-2, xie2019therolesof pages 3-6, wang2019ali1candidategene pages 10-13, wang2020naturalvariationin pages 9-11, yasin2025c2h2zincfinger pages 2-4).

2. **Entry type dictates annotation granularity.** PTHR47593 is type="family," which identifies structural homology, not functional identity. Functional GO annotations should be pushed down to subfamily-level entries if those subfamilies are functionally coherent and separately defined (e.g., if PANTHER has a child clade specifically for ZFP3-like ABA/germination regulators, that child could receive GO:0009738 or similar).

3. **Generic terms add minimal value.** While GO:0003676 (nucleic acid binding), GO:0046872 (metal ion binding), and GO:0005634 (nucleus) are technically correct, they do not distinguish this family from thousands of other nuclear transcription factors and therefore do not meet the threshold for informative InterPro2GO core annotation (han2020c2h2zincfinger pages 1-2).

4. **Subfamily-specific annotation is the solution.** If distinct functional clades exist within PTHR47593 (e.g., ZFP3-orthologs verified to regulate germination/ABA, ZFP1-orthologs regulating root hairs, ALI-1-like proteins regulating awn development), each should be annotated separately at the subfamily level with the appropriate specific GO terms. The parent family-level entry should remain unannotated to avoid systematic over-propagation (han2020arabidopsiszincfinger pages 1-3, wang2020naturalvariationin pages 4-7, xie2019therolesof pages 3-6, wang2020naturalvariationin pages 9-11).

### Additional Recommendation for InterPro Curators

**Revise the InterPro text description** to clarify that the stated ABA/germination function represents one functional branch of the family rather than a pan-family characteristic. Suggested wording:

> "PTHR47593 is a family of plant C2H2-type zinc finger transcription factors characterized by a conserved single-finger QALGGH domain. Members of this family have diversified functionally and regulate distinct developmental processes including root hair patterning, trichome initiation, floral organ identity, and seed germination. A subset of this family (e.g., ZFP3-like proteins) functions as negative regulators of abscisic acid signaling during seed germination and early seedling development, contributing to plant stress responses and adaptive growth under varying environmental conditions."

This revised description would prevent users from assuming all matched proteins share the ABA/germination role and would better align with the experimental literature (han2020arabidopsiszincfinger pages 1-3, hu2023leafyandapetala1 pages 1-2, wang2020naturalvariationin pages 4-7, yasin2025c2h2zincfinger pages 1-2, xie2019therolesof pages 3-6, wang2019ali1candidategene pages 10-13, wang2020naturalvariationin pages 9-11, yasin2025c2h2zincfinger pages 2-4).

---

## Comprehensive Summary Table

| Aspect | Findings (with citations) |
|---|---|
| Family definition and structural features | PTHR47593 corresponds to a plant C2H2 zinc-finger protein family related to Arabidopsis ZFP7. In the founding Arabidopsis study, ZFP7 was one of eight related single-finger proteins (ZFP1-8), unusual because each protein contains only **one** C2H2 zinc finger rather than the multiple fingers typical of many eukaryotic C2H2 proteins. ZFP7 was reported as a 209 aa protein with expression in roots, stems, and cauline leaves. The finger region is highly conserved and includes the plant-typical **QALGGH** motif in the α-helical DNA-binding region; plant C2H2 domains generally follow a **C-X2-4-C-X3-P-X5-L-X2-H-X3-H** consensus and coordinate Zn²⁺ in a tetrahedral ββα fold. Additional recurrent features in related family members include serine/threonine-rich segments (candidate phosphoregulation sites), a basic region immediately C-terminal to the finger consistent with nuclear localization/DNA-binding support, and leucine-rich motifs that may mediate protein-protein interactions. In broader plant C2H2 families, some members also carry an **EAR repression motif** (e.g., LxLxL or DLNxxP-like), but this is not universal across all ZFP7-like proteins and therefore should not be assumed family-wide. Overall, the strongest conserved, family-wide feature is the plant-specific single-finger C2H2/QALGGH DNA-binding architecture, not a single conserved biological process (tague1995characterizationofa pages 1-3, tague1995characterizationofa pages 4-5, han2020c2h2zincfinger pages 1-2, tague1995characterizationofa pages 10-11, tague1995characterizationofa pages 5-7, tague1995characterizationofa pages 7-10). |
| Subfamily functional divergence | Evidence from closely related Arabidopsis and crop homologs shows major functional divergence among related C2H2 Q-type ZFPs. **ZFP1/AtZP1** acts as a transcriptional repressor of root hair initiation and elongation, directly suppressing **RHD6, RSL2, and RSL4**; its repression depends on an EAR motif (han2020arabidopsiszincfinger pages 1-3). **ZFP3** has been reviewed as a negative regulator of light/ABA responses during germination and seedling development, aligning with the type of function described in the InterPro text, but that evidence applies to ZFP3-like members rather than the whole broader family (xie2019therolesof pages 3-6). **ZFP8** functions in trichome and floral regulatory pathways, and with ZP1 represses floral homeotic genes **AP3, PI, and AG** in leaves; newer work also places ZFP8 in hormone-linked trichome regulation with GIS2 (hu2023leafyandapetala1 pages 1-2, yasin2025c2h2zincfinger pages 1-2, yasin2025c2h2zincfinger pages 2-4). **GIS/GIS2** family members regulate trichome patterning through gibberellin/cytokinin crosstalk rather than ABA-germination control (yasin2025c2h2zincfinger pages 1-2, yasin2025c2h2zincfinger pages 2-4). In cereals, the related C2H2 factor **ALI-1** represses awn elongation and affects grain traits through cytokinin-linked developmental regulation, again distinct from ABA-mediated germination control (wang2020naturalvariationin pages 4-7, wang2019ali1candidategene pages 10-13, wang2020naturalvariationin pages 9-11). Thus, this broader family is structurally related but biologically heterogeneous; ABA/germination regulation is not a safe whole-family assumption (han2020arabidopsiszincfinger pages 1-3, hu2023leafyandapetala1 pages 1-2, wang2020naturalvariationin pages 4-7, yasin2025c2h2zincfinger pages 1-2, xie2019therolesof pages 3-6, wang2019ali1candidategene pages 10-13, wang2020naturalvariationin pages 9-11, yasin2025c2h2zincfinger pages 2-4). |
| Taxonomic distribution | The entry spans **1284 proteins across 963 taxa** (InterPro metadata supplied by user). Literature on Q-type C2H2 proteins shows these are **plant-specific** regulators with the QALGGH motif broadly represented across land plants and many angiosperm lineages, including Arabidopsis, wheat, barley, rice, poplar, grapevine, citrus, Brassica, Medicago, cucumber, sweetpotato, sugar beet, and rose. Reviews and comparative studies emphasize that most Arabidopsis C2H2 ZFPs are plant specific and that Q-type proteins are a major land-plant transcription-factor radiation (xie2019therolesof pages 3-6, han2020c2h2zincfinger pages 1-2). For GO review, the taxonomic point is crucial: seed-specific processes such as **seed germination** and seedling ABA control are not valid across all land plants, and even within angiosperms the relevant developmental context differs strongly by ortholog/subfamily. Therefore, any GO process term tied to germination or ABA signaling risks taxonomic/process overreach unless restricted to a child entry proven to cover only that clade/function (xie2019therolesof pages 3-6, han2020c2h2zincfinger pages 1-2). |
| Current InterPro2GO status | **No InterPro2GO terms are currently mapped** to PTHR47593. Given the evidence above, this is presently the safest state. Although the InterPro prose description says the family is characterized by negative regulation of ABA signaling during germination and early seedling development, the literature indicates that such a statement is too narrow and likely reflects one functional branch of the wider ZFP-like family rather than all proteins matched by this family signature. Family-level mapping to process terms would therefore risk systematic over-annotation (han2020arabidopsiszincfinger pages 1-3, hu2023leafyandapetala1 pages 1-2, wang2020naturalvariationin pages 4-7, xie2019therolesof pages 3-6, wang2020naturalvariationin pages 9-11, yasin2025c2h2zincfinger pages 2-4). |
| GO annotation verdict and recommendations | **Verdict: maintain the current absence of InterPro2GO mappings for PTHR47593.** Recommended action pattern: **ACCEPT** (accept no mapping), with an InterPro-side recommendation to **revise the textual description** or move the ABA/germination claim to a more specific child/subfamily entry if supported there. Rationale: (1) this is a **family** entry, but the matched proteins are not functionally homogeneous; (2) only a subset of related proteins supports ABA/germination roles, while others regulate root hairs, trichomes, floral repression, awn development, and grain traits; (3) adding whole-protein biological-process GO terms at this level would over-annotate many proteins; (4) highly generic molecular-function terms such as “DNA binding” or “metal ion binding” would be technically plausible yet low-value and not worth adding as core mappings. If future subfamily resolution becomes available, more specific terms such as negative regulation of ABA-activated signaling or regulation of seed germination should be considered **only** for the experimentally supported child branch, not for PTHR47593 as a whole (han2020arabidopsiszincfinger pages 1-3, hu2023leafyandapetala1 pages 1-2, wang2020naturalvariationin pages 4-7, xie2019therolesof pages 3-6, wang2020naturalvariationin pages 9-11, yasin2025c2h2zincfinger pages 2-4). |


*Table: This table summarizes the structural biology, functional divergence, taxonomic scope, and GO annotation implications for the PTHR47593 Zinc finger protein 7 family. It is useful for deciding whether family-level InterPro2GO mappings would be biologically valid or over-broad.*

---

## References (Primary Literature Cited)

The following context IDs correspond to specific studies cited in this report:

- **pqac-00000000:** Han et al. 2020, *Plant Cell*. Arabidopsis ZINC FINGER PROTEIN1 represses root hair initiation and elongation.
- **pqac-00000001:** Hu et al. 2023, *PNAS*. LEAFY and APETALA1 down-regulate ZP1 and ZFP8 to release repression on floral homeotic genes.
- **pqac-00000002:** Tague & Goodman 1995, *Plant Mol Biol*. Characterization of a family of Arabidopsis zinc finger protein cDNAs.
- **pqac-00000005:** Wang et al. 2020, *Plant J*. Natural variation in the ALI-1 promoter is associated with awn elongation and grain length in common wheat.
- **pqac-00000006:** Yasin et al. 2025, *Int J Mol Sci*. C2H2 Zinc Finger Proteins GIS2 and ZFP8 regulate trichome development via hormone signaling in Arabidopsis.
- **pqac-00000007:** Kagale et al. 2010, *Plant Physiol*. Genome-wide analysis of EAR motif-containing transcriptional regulators in Arabidopsis.
- **pqac-00000008:** Xie et al. 2019, *Genes*. The roles of Arabidopsis C1-2i subclass of C2H2-type zinc-finger transcription factors.
- **pqac-00000009:** Wang et al. 2019, *bioRxiv*. ALI-1, candidate gene of B1 locus, is associated with awn length and grain weight in common wheat.
- **pqac-00000010:** Chhetri et al. 2020, *Front Plant Sci*. Genome-wide association study of wood anatomical and morphological traits in *Populus trichocarpa*.
- **pqac-00000011:** Wang et al. 2020, *Plant J*. (Additional data on ALI-1 grain/awn development.)
- **pqac-00000012:** Han et al. 2020, *Front Plant Sci*. C2H2 zinc finger proteins: Master regulators of abiotic stress responses in plants (review).
- **pqac-00000013:** Yasin et al. 2025, *Int J Mol Sci*. (Additional mechanistic data on GIS2/ZFP8.)
- **pqac-00000014, pqac-00000015, pqac-00000016:** Tague & Goodman 1995, *Plant Mol Biol*. (Multiple sections providing structural/expression data on ZFP1-8 family.)

Additional genome-wide studies and reviews (tague1995characterizationofa pages 3-4, tague1995characterizationofa pages 4-5) provide supporting phylogenetic and evolutionary context.

---

**Report prepared:** 2026  
**Basis:** Literature review prioritizing 2020–2025 publications with primary experimental data; founding structural studies (Tague & Goodman 1995); authoritative reviews on plant C2H2 transcription factors.

**Key finding:** PTHR47593 correctly has zero InterPro2GO mappings. Maintain this state; do not add family-level GO terms. If functionally coherent subfamilies exist, annotate those children separately with appropriate specific terms.

References

1. (tague1995characterizationofa pages 1-3): Brian W. Tague and Howard M. Goodman. Characterization of a family of arabidopsis zinc finger protein cdnas. Plant Molecular Biology, 28:267-279, May 1995. URL: https://doi.org/10.1007/bf00020246, doi:10.1007/bf00020246. This article has 68 citations and is from a peer-reviewed journal.

2. (tague1995characterizationofa pages 10-11): Brian W. Tague and Howard M. Goodman. Characterization of a family of arabidopsis zinc finger protein cdnas. Plant Molecular Biology, 28:267-279, May 1995. URL: https://doi.org/10.1007/bf00020246, doi:10.1007/bf00020246. This article has 68 citations and is from a peer-reviewed journal.

3. (tague1995characterizationofa pages 5-7): Brian W. Tague and Howard M. Goodman. Characterization of a family of arabidopsis zinc finger protein cdnas. Plant Molecular Biology, 28:267-279, May 1995. URL: https://doi.org/10.1007/bf00020246, doi:10.1007/bf00020246. This article has 68 citations and is from a peer-reviewed journal.

4. (tague1995characterizationofa pages 7-10): Brian W. Tague and Howard M. Goodman. Characterization of a family of arabidopsis zinc finger protein cdnas. Plant Molecular Biology, 28:267-279, May 1995. URL: https://doi.org/10.1007/bf00020246, doi:10.1007/bf00020246. This article has 68 citations and is from a peer-reviewed journal.

5. (han2020c2h2zincfinger pages 1-2): Guoliang Han, Chaoxia Lu, Jianrong Guo, Ziqi Qiao, Na Sui, Nianwei Qiu, and Baoshan Wang. C2h2 zinc finger proteins: master regulators of abiotic stress responses in plants. Frontiers in Plant Science, Feb 2020. URL: https://doi.org/10.3389/fpls.2020.00115, doi:10.3389/fpls.2020.00115. This article has 434 citations.

6. (xie2019therolesof pages 3-6): Minmin Xie, Jinhao Sun, Daping Gong, and Yingzhen Kong. The roles of arabidopsis c1-2i subclass of c2h2-type zinc-finger transcription factors. Genes, 10:653, Aug 2019. URL: https://doi.org/10.3390/genes10090653, doi:10.3390/genes10090653. This article has 113 citations.

7. (han2020arabidopsiszincfinger pages 1-3): Guoliang Han, Xiaocen Wei, Xinxiu Dong, Chengfeng Wang, Na Sui, Jianrong Guo, Fang Yuan, Zhizhong Gong, Xuezhi Li, Yi Zhang, Zhe Meng, Zhuo Chen, Dazhong Zhao, and Baoshan Wang. Arabidopsis zinc finger protein1 acts downstream of gl2 to repress root hair initiation and elongation by directly suppressing bhlh genes[open]. Plant Cell, 32:206-225, Nov 2020. URL: https://doi.org/10.1105/tpc.19.00226, doi:10.1105/tpc.19.00226. This article has 114 citations and is from a highest quality peer-reviewed journal.

8. (kagale2010genomewideanalysisof pages 1-2): Sateesh Kagale, Matthew G. Links, and Kevin Rozwadowski. Genome-wide analysis of ethylene-responsive element binding factor-associated amphiphilic repression motif-containing transcriptional regulators in arabidopsis1[w][oa]. Plant Physiology, 152:1109-1134, Jan 2010. URL: https://doi.org/10.1104/pp.109.151704, doi:10.1104/pp.109.151704. This article has 371 citations and is from a highest quality peer-reviewed journal.

9. (hu2023leafyandapetala1 pages 1-2): Tieqiang Hu, Xiaohui Li, Liren Du, Darren Manuela, and Mingli Xu. Leafy and apetala1 down-regulate zinc finger protein 1 and 8 to release their repression on class b and c floral homeotic genes. Proceedings of the National Academy of Sciences of the United States of America, May 2023. URL: https://doi.org/10.1073/pnas.2221181120, doi:10.1073/pnas.2221181120. This article has 37 citations and is from a highest quality peer-reviewed journal.

10. (yasin2025c2h2zincfinger pages 1-2): Muhammad Umair Yasin, Lili Sun, Chunyan Yang, Bohan Liu, and Yinbo Gan. C2h2 zinc finger proteins gis2 and zfp8 regulate trichome development via hormone signaling in arabidopsis. International Journal of Molecular Sciences, 26:7265, Jul 2025. URL: https://doi.org/10.3390/ijms26157265, doi:10.3390/ijms26157265. This article has 3 citations.

11. (yasin2025c2h2zincfinger pages 2-4): Muhammad Umair Yasin, Lili Sun, Chunyan Yang, Bohan Liu, and Yinbo Gan. C2h2 zinc finger proteins gis2 and zfp8 regulate trichome development via hormone signaling in arabidopsis. International Journal of Molecular Sciences, 26:7265, Jul 2025. URL: https://doi.org/10.3390/ijms26157265, doi:10.3390/ijms26157265. This article has 3 citations.

12. (wang2020naturalvariationin pages 4-7): Dongzhi Wang, Kang Yu, Di Jin, Linhe Sun, Jinfang Chu, Wenying Wu, Peiyong Xin, Edita Gregová, Xin Li, Jiazhu Sun, Wenlong Yang, Kehui Zhan, Aimin Zhang, and Dongcheng Liu. Natural variation in the promoter of awn length inhibitor 1 (ali-1) is associated with awn elongation and grain length in common wheat. The Plant journal : for cell and molecular biology, 101:1075-1090, Mar 2020. URL: https://doi.org/10.1111/tpj.14575, doi:10.1111/tpj.14575. This article has 66 citations.

13. (wang2019ali1candidategene pages 10-13): Dongzhi Wang, Kang Yu, Di Jin, Linhe Sun, Jinfang Chu, Wenying Wu, Peiyong Xin, Xin Li, Jiazhu Sun, Wenlong Yang, Kehui Zhan, Aimin Zhang, and Dongcheng Liu. Ali-1, candidate gene of b1 locus, is associated with awn length and grain weight in common wheat. bioRxiv, Jul 2019. URL: https://doi.org/10.1101/688085, doi:10.1101/688085. This article has 9 citations.

14. (wang2020naturalvariationin pages 9-11): Dongzhi Wang, Kang Yu, Di Jin, Linhe Sun, Jinfang Chu, Wenying Wu, Peiyong Xin, Edita Gregová, Xin Li, Jiazhu Sun, Wenlong Yang, Kehui Zhan, Aimin Zhang, and Dongcheng Liu. Natural variation in the promoter of awn length inhibitor 1 (ali-1) is associated with awn elongation and grain length in common wheat. The Plant journal : for cell and molecular biology, 101:1075-1090, Mar 2020. URL: https://doi.org/10.1111/tpj.14575, doi:10.1111/tpj.14575. This article has 66 citations.

15. (chhetri2020genomewideassociationstudy pages 12-13): Hari B. Chhetri, Anna Furches, David Macaya-Sanz, Alejandro R. Walker, David Kainer, Piet Jones, Anne E. Harman-Ware, Timothy J. Tschaplinski, Daniel Jacobson, Gerald A. Tuskan, and Stephen P. DiFazio. Genome-wide association study of wood anatomical and morphological traits in populus trichocarpa. Frontiers in Plant Science, Sep 2020. URL: https://doi.org/10.3389/fpls.2020.545748, doi:10.3389/fpls.2020.545748. This article has 50 citations.

16. (tague1995characterizationofa pages 4-5): Brian W. Tague and Howard M. Goodman. Characterization of a family of arabidopsis zinc finger protein cdnas. Plant Molecular Biology, 28:267-279, May 1995. URL: https://doi.org/10.1007/bf00020246, doi:10.1007/bf00020246. This article has 68 citations and is from a peer-reviewed journal.

17. (tague1995characterizationofa pages 3-4): Brian W. Tague and Howard M. Goodman. Characterization of a family of arabidopsis zinc finger protein cdnas. Plant Molecular Biology, 28:267-279, May 1995. URL: https://doi.org/10.1007/bf00020246, doi:10.1007/bf00020246. This article has 68 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PTHR47593-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. han2020arabidopsiszincfinger pages 1-3
2. xie2019therolesof pages 3-6
3. chhetri2020genomewideassociationstudy pages 12-13
4. tague1995characterizationofa pages 1-3
5. tague1995characterizationofa pages 10-11
6. tague1995characterizationofa pages 5-7
7. tague1995characterizationofa pages 7-10
8. kagale2010genomewideanalysisof pages 1-2
9. wang2020naturalvariationin pages 4-7
10. wang2020naturalvariationin pages 9-11
11. tague1995characterizationofa pages 4-5
12. tague1995characterizationofa pages 3-4
13. open
14. w
15. oa
16. https://doi.org/10.1007/bf00020246,
17. https://doi.org/10.3389/fpls.2020.00115,
18. https://doi.org/10.3390/genes10090653,
19. https://doi.org/10.1105/tpc.19.00226,
20. https://doi.org/10.1104/pp.109.151704,
21. https://doi.org/10.1073/pnas.2221181120,
22. https://doi.org/10.3390/ijms26157265,
23. https://doi.org/10.1111/tpj.14575,
24. https://doi.org/10.1101/688085,
25. https://doi.org/10.3389/fpls.2020.545748,