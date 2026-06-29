---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T20:49:54.695888'
end_time: '2026-06-28T21:07:36.867168'
duration_seconds: 1062.17
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR22969
  interpro_name: Inhibitor of nuclear factor kappa-B kinase
  interpro_short_name: IKK
  interpro_type: family
  interpro_integrated: IPR051180
  member_databases: Not specified
  n_proteins: '6839'
  n_taxa: '4084'
  n_subfamilies: '6'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: The I-kappa-B kinase (IKK) family comprises serine/threonine
    kinases essential for the NF-kappa-B signaling pathway, which is activated by
    various stimuli including inflammatory cytokines, bacterial or viral products,
    DNA damage, and other cellular stresses. Family members phosphorylate inhibitors
    of NF-kappa-B, leading to their ubiquitination and degradation, and subsequent
    nuclear translocation of NF-kappa-B to activate gene transcription involved in
    immune response, growth control, and apoptosis protection. Additionally, the family
    plays roles in antiviral responses by phosphorylating interferon regulatory factors
    and in energy balance regulation. Some members also phosphorylate histones, modulating
    chromatin accessibility, and have roles in autophagy, cell survival, and lymphoid
    organogenesis. The family's activity is regulated by phosphorylation and is crucial
    for both canonical and non-canonical NF-kappa-B signaling pathways, as well as
    for maintaining a balance between type I and type II interferon responses.
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 39
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR22969-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR22969-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** PTHR22969
- **Name:** Inhibitor of nuclear factor kappa-B kinase
- **Short name:** IKK
- **Entry type:** family
- **Integrated into / parent:** IPR051180
- **Member database signatures:** Not specified
- **Scale:** 6839 proteins across 4084 taxa, 6 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The I-kappa-B kinase (IKK) family comprises serine/threonine kinases essential for the NF-kappa-B signaling pathway, which is activated by various stimuli including inflammatory cytokines, bacterial or viral products, DNA damage, and other cellular stresses. Family members phosphorylate inhibitors of NF-kappa-B, leading to their ubiquitination and degradation, and subsequent nuclear translocation of NF-kappa-B to activate gene transcription involved in immune response, growth control, and apoptosis protection. Additionally, the family plays roles in antiviral responses by phosphorylating interferon regulatory factors and in energy balance regulation. Some members also phosphorylate histones, modulating chromatin accessibility, and have roles in autophagy, cell survival, and lymphoid organogenesis. The family's activity is regulated by phosphorylation and is crucial for both canonical and non-canonical NF-kappa-B signaling pathways, as well as for maintaining a balance between type I and type II interferon responses.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR22969 (Inhibitor of nuclear factor kappa-B kinase)**, structured to support GO annotation review.

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
- **Accession:** PTHR22969
- **Name:** Inhibitor of nuclear factor kappa-B kinase
- **Short name:** IKK
- **Entry type:** family
- **Integrated into / parent:** IPR051180
- **Member database signatures:** Not specified
- **Scale:** 6839 proteins across 4084 taxa, 6 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The I-kappa-B kinase (IKK) family comprises serine/threonine kinases essential for the NF-kappa-B signaling pathway, which is activated by various stimuli including inflammatory cytokines, bacterial or viral products, DNA damage, and other cellular stresses. Family members phosphorylate inhibitors of NF-kappa-B, leading to their ubiquitination and degradation, and subsequent nuclear translocation of NF-kappa-B to activate gene transcription involved in immune response, growth control, and apoptosis protection. Additionally, the family plays roles in antiviral responses by phosphorylating interferon regulatory factors and in energy balance regulation. Some members also phosphorylate histones, modulating chromatin accessibility, and have roles in autophagy, cell survival, and lymphoid organogenesis. The family's activity is regulated by phosphorylation and is crucial for both canonical and non-canonical NF-kappa-B signaling pathways, as well as for maintaining a balance between type I and type II interferon responses.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR22969 (Inhibitor of nuclear factor kappa-B kinase)**, structured to support GO annotation review.

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


# Comprehensive Research Report: PTHR22969 — Inhibitor of Nuclear Factor Kappa-B Kinase (IKK) Family

## 1. Family Definition and Biochemistry

### 1.1 Family Composition and Domain Architecture

PTHR22969 encompasses the I-kappa-B kinase (IKK) family, a group of serine/threonine kinases that are central regulators of immune signaling. In mammals, the family comprises four catalytic members divided into two subfamilies: (i) the classical IKKs — IKKα (CHUK) and IKKβ (IKBKB), which share 52% amino acid identity and associate with the regulatory subunit NEMO/IKKγ; and (ii) the IKK-related kinases — TBK1 and IKKε (IKBKE), which share 64–67% sequence identity with each other but only ~30% homology with IKKα/IKKβ (ramadass2020smallmoleculenfκb pages 13-15, luo2025anexaminationof pages 8-10).

All four kinases share a conserved multi-domain architecture. IKKα and IKKβ contain an N-terminal kinase domain (KD, residues ~1–307 in IKKβ), a ubiquitin-like domain (ULD, residues ~308–404), a scaffold/dimerization domain (SDD, residues ~410–664), and a C-terminal NEMO-binding domain (NBD) (zhang2023iκbkinaseβ pages 1-2, paul2018inhibitoryκbkinase(ikk) pages 12-14, li2024molecularmechanismof pages 1-2). TBK1 and IKKε share analogous architecture with KD, ULD, and C-terminal SDD comprising coiled-coil domains, though they lack a canonical NEMO-binding domain (zhou2020tbk1acentral pages 2-2, luo2025anexaminationof pages 8-10).

### 1.2 Kinase Fold and Catalytic Mechanism

The IKK kinase domain adopts the canonical bi-lobed protein kinase fold, with ATP binding in a deep cleft between the N-terminal and C-terminal lobes (paul2018inhibitoryκbkinase(ikk) pages 12-14). The activation loop contains closely spaced serine residues critical for kinase activation: Ser176/Ser180 in IKKα and Ser177/Ser181 in IKKβ (paul2018inhibitoryκbkinase(ikk) pages 12-14, zhang2023iκbkinaseβ pages 1-2). Activation occurs primarily through oligomerization-mediated trans-autophosphorylation, with TAK1 initially phosphorylating Ser177 of IKKβ, which then primes autophosphorylation of Ser181 (zhang2023iκbkinaseβ pages 1-2). Mutating these serines to phosphomimetic glutamates generates constitutively active IKK in vivo (hotchkiss2021discoveryofan pages 4-7). Crystal structures of IKK2 (PDB: 4E3C) and IKK1 homodimers have been determined, revealing that protomers adopt asymmetric activation loop conformations in active versus inactive states (hotchkiss2021discoveryofan pages 1-4, hotchkiss2021discoveryofan pages 7-9).

### 1.3 Substrate Recognition

A recent landmark study identified a conserved YDDΦxΦ substrate-docking motif shared among canonical and non-canonical NF-κB substrates (IκBα, IκBβ, p100), which mediates interaction with the IKK catalytic dimer interface. Phosphorylation of the conserved tyrosine in this motif suppresses the docking interaction, providing a regulatory feedback mechanism. IKK dimerization is essential for substrate binding and recognition (li2024molecularmechanismof pages 1-2). IKKβ phosphorylates IκBα at Ser32 and Ser36, triggering its ubiquitination and proteasomal degradation (zhang2023iκbkinaseβ pages 1-2).

TBK1 forms stable homodimers where the three main domains (KD, ULD, SDD) create a joint interface with kinase active sites positioned away from each other (zhou2020tbk1acentral pages 2-2). An allosteric site at the interface between the KD and SDD can be targeted by inhibitors to prevent activation loop phosphorylation (hotchkiss2021discoveryofan pages 1-4).

The following table summarizes the key characteristics of the major IKK family members:

| Family member | Gene / ortholog | Subfamily | Primary pathway(s) | Representative substrates / targets | Conserved structural features | Major functional roles | Evidence |
|---|---|---|---|---|---|---|---|
| IKKα | **CHUK** | Classical IKKs | Non-canonical NF-κB; also contributes to canonical NF-κB | p100/NFKB2; IKKβ activation loop; Aurora A; CBP; β-catenin; steroid receptor regulators | N-terminal kinase domain, ubiquitin-like domain (ULD), scaffold/dimerization domain (SDD), C-terminal NEMO-binding region; activation-loop Ser176/Ser180; active Ser/Thr kinase fold shared with IKKβ | p100 processing to p52-RelB; nuclear signaling; chromatin/transcriptional control; cell-cycle and differentiation functions; some NF-κB-independent signaling | (paul2018inhibitoryκbkinase(ikk) pages 12-14, guo2024nfκbinbiology pages 2-3, li2024molecularmechanismof pages 1-2, antonia2021expandingtheview pages 6-7, paul2018inhibitoryκbkinase(ikk) pages 3-5) |
| IKKβ | **IKBKB** | Classical IKKs | Canonical NF-κB; also metabolism/stress signaling | IκBα (Ser32/Ser36), IκBβ, AMPK, XBP1, TSC1, PUMA/Bad-related signaling nodes | N-terminal kinase domain, ULD, SDD, C-terminal NEMO-binding region; activation-loop Ser177/Ser181; bi-lobed kinase core; substrate docking requires dimer interface | Principal kinase for inducible IκB phosphorylation and NF-κB activation; inflammatory signaling; cell survival; metabolic regulation | (zhang2023iκbkinaseβ pages 1-2, li2024molecularmechanismof pages 1-2, ramadass2020smallmoleculenfκb pages 13-15, antonia2021expandingtheview pages 4-6) |
| TBK1 | **TBK1** | IKK-related kinases | Type I IFN / IRF signaling; innate nucleic-acid sensing; selective autophagy / mitophagy | IRF3, IRF7, OPTN, SQSTM1/p62, NDP52, TAX1BP1, RAB7A, STX17 | N-terminal kinase domain, ULD, C-terminal SDD with coiled-coils; stable homodimer; related to IKKε but functionally distinct from IKKα/β | Central kinase downstream of STING/MAVS/TRIF; antiviral signaling; cytokine control; autophagy, mitophagy, bacteriophagy; tissue-homeostasis roles | (zhou2020tbk1acentral pages 2-2, antonia2021expandingtheview pages 9-11, revach2020targetingtankbindingkinase pages 4-6, revach2020targetingtankbindingkinase pages 18-19) |
| IKKε | **IKBKE** | IKK-related kinases | Type I IFN / IRF signaling; innate immunity; some NF-κB modulation; metabolism | IRF3, IRF7, STING-associated targets, RAB7A, TAX1BP1 | N-terminal kinase domain with C-terminal ubiquitin-like / coiled-coil scaffold organization closely related to TBK1; active Ser/Thr kinase | Inducible antiviral signaling kinase; partially redundant with TBK1 in IFN responses; contributes to inflammatory control, autophagy-related signaling, and energy-balance/obesity phenotypes | (luo2025anexaminationof pages 8-10, ramadass2020smallmoleculenfκb pages 13-15, antonia2021expandingtheview pages 9-11, white2025phosphorylationofthe pages 1-2) |
| Ird5 (Drosophila) | **ird5** (IKKβ homolog) | Insect IKKβ-like | IMD pathway / insect NF-κB-like immunity; antiviral STING–NF-κB in flies | Relish | Catalytic IKKβ-like kinase in fly IKK complex with Kenny/IKKγ; pathway activated by TAK1; conserved IKK-family kinase architecture inferred from homology | Phosphorylates Relish in the IMD pathway; required for antibacterial and antiviral innate immune signaling in insects | (cammaratamouchtouris2022dynamicregulationof pages 2-4, cammaratamouchtouris2022dynamicregulationof pages 4-6) |


*Table: This table summarizes the main IKK family members and a key insect homolog, highlighting their subfamily placement, pathways, substrates, conserved architecture, and major biological roles. It is useful for judging whether a broad family-level GO annotation would overgeneralize across functionally divergent kinases.*

## 2. InterPro2GO Mapping Appropriateness

### 2.1 Current Status

PTHR22969 currently has **no InterPro2GO terms mapped**. This analysis evaluates whether this absence is appropriate and whether any GO terms could be safely applied at the family level.

### 2.2 Evaluation of Candidate GO Terms

Given the profound functional divergence within this family, most pathway-specific or process-specific GO terms would systematically over-annotate a significant proportion of matched proteins. The evaluation of specific candidate GO terms is presented below:

| GO Term | GO ID | Category (MF/BP/CC) | Applicable to all members? (Yes/No) | Risk of over-annotation | Recommendation (ACCEPT/REJECT/SUBFAMILY-ONLY) | Rationale |
|---|---|---|---|---|---|---|
| protein serine/threonine kinase activity | GO:0004674 | MF | Yes | Low | ACCEPT | Core catalytic activity is shared across IKK family members, which are active Ser/Thr kinases with conserved kinase-domain architecture and activation-loop regulation; this is the safest family-level functional term, though still broad (paul2018inhibitoryκbkinase(ikk) pages 12-14, zhou2020tbk1acentral pages 2-2, zhang2023iκbkinaseβ pages 1-2, li2024molecularmechanismof pages 1-2). |
| ATP binding | GO:0005524 | MF | Yes | Medium | ACCEPT | All IKK family members are protein kinases and therefore require ATP binding, but this term is very generic and contributes little specificity; acceptable only as a non-informative core enzymatic attribute (paul2018inhibitoryκbkinase(ikk) pages 12-14). |
| IkappaB kinase activity | GO:0008384 | MF | No | High | SUBFAMILY-ONLY | Appropriate for canonical/non-canonical IKKα/IKKβ proteins that phosphorylate IκB family substrates and p100, but not for TBK1/IKKε, whose hallmark substrates are IRF3/IRF7 and autophagy adaptors rather than classical IκBs (ramadass2020smallmoleculenfκb pages 13-15, antonia2021expandingtheview pages 1-2, zhou2020tbk1acentral pages 2-2, li2024molecularmechanismof pages 1-2). |
| NF-kappaB signaling | GO:0043122 | BP | No | High | SUBFAMILY-ONLY | IKKα/IKKβ are central NF-κB-pathway kinases, and insect IKKβ homologs also signal to NF-κB-like factors, but TBK1/IKKε are primarily innate antiviral and IFN-pathway kinases with broader non-NF-κB roles; family-wide mapping would conflate distinct pathways (ramadass2020smallmoleculenfκb pages 13-15, antonia2021expandingtheview pages 1-2, zhou2020tbk1acentral pages 2-2, cammaratamouchtouris2022dynamicregulationof pages 2-4, cammaratamouchtouris2022dynamicregulationof pages 4-6). |
| I-kappaB kinase/NF-kappaB signaling | GO:0007249 | BP | No | High | SUBFAMILY-ONLY | Too specific for the CHUK/IKBKB branch and not true for the TBK1/IKKε branch, which often acts in IRF/type I IFN and autophagy signaling; would over-annotate many family matches outside classical IKK complex biology (ramadass2020smallmoleculenfκb pages 13-15, antonia2021expandingtheview pages 1-2, zhou2020tbk1acentral pages 2-2, guo2024nfκbinbiology pages 2-3). |
| innate immune response | GO:0045087 | BP | No | Medium | REJECT | Many IKK family members participate in immunity, but not uniformly or exclusively; several members also have major developmental, metabolic, chromatin, cell-cycle, and autophagy roles, so this is not reliably true for every matched protein across taxa (antonia2021expandingtheview pages 6-7, paul2018inhibitoryκbkinase(ikk) pages 3-5, antonia2021expandingtheview pages 3-4, antonia2021expandingtheview pages 9-11). |
| type I interferon signaling pathway | GO:0060337 | BP | No | High | SUBFAMILY-ONLY | This is strongly supported for TBK1/IKKε, which phosphorylate IRF3/IRF7 downstream of STING/MAVS/TRIF, but not for IKKα/IKKβ, so it should be restricted to the IKK-related kinase branch only (ramadass2020smallmoleculenfκb pages 13-15, zhou2020tbk1acentral pages 2-2). |
| regulation of autophagy | GO:0010506 | BP | No | High | SUBFAMILY-ONLY | TBK1 clearly regulates selective autophagy/mitophagy/xenophagy by phosphorylating OPTN, p62, NDP52, TAX1BP1, RAB7A, and related factors; IKKα/IKKβ and IKKε also have some autophagy-linked roles, but this is not a universal family property (antonia2021expandingtheview pages 9-11, antonia2021expandingtheview pages 7-9, revach2020targetingtankbindingkinase pages 4-6, revach2020targetingtankbindingkinase pages 18-19, antonia2021expandingtheview pages 3-4). |
| protein phosphorylation | GO:0006468 | BP | Yes | Medium | ACCEPT | All family members catalyze phosphorylation of protein substrates, so this process term is broadly correct; however, it is generic and should be considered low-information compared with more specific molecular-function annotations (paul2018inhibitoryκbkinase(ikk) pages 12-14, zhang2023iκbkinaseβ pages 1-2, li2024molecularmechanismof pages 1-2). |
| cytoplasm | GO:0005737 | CC | No | Medium | REJECT | Many IKK proteins localize in the cytoplasm, but localization is not exclusive or universal: IKKα has important nuclear functions, and several family members shuttle or act at signaling organelles/complexes; a blanket cytoplasm term would understate functional compartment diversity (antonia2021expandingtheview pages 6-7, paul2018inhibitoryκbkinase(ikk) pages 3-5). |


*Table: This table evaluates candidate GO terms for the broad IKK family entry PTHR22969 and highlights which terms are safe at family level versus those that should be restricted to subfamilies. It is useful for avoiding over-annotation caused by the strong functional divergence between IKKα/IKKβ and TBK1/IKKε branches.*

### 2.3 Assessment Summary

Only two GO terms could be considered safe at the family level: **protein serine/threonine kinase activity** (GO:0004674) and **protein phosphorylation** (GO:0006468), as these reflect the universally conserved catalytic function shared by all IKK family members (paul2018inhibitoryκbkinase(ikk) pages 12-14, zhou2020tbk1acentral pages 2-2, zhang2023iκbkinaseβ pages 1-2). However, even these are generic and carry limited informational value.

**IκB kinase activity** (GO:0008384) — the term most closely associated with the family name — would be inappropriate at the PTHR22969 level because TBK1 and IKKε primarily phosphorylate IRF3/IRF7 rather than classical IκB substrates (ramadass2020smallmoleculenfκb pages 13-15, antonia2021expandingtheview pages 1-2, zhou2020tbk1acentral pages 2-2). Similarly, **NF-κB signaling** terms would exclude TBK1/IKKε, whose principal roles lie in type I interferon induction through STING/MAVS/TRIF signaling platforms (zhou2020tbk1acentral pages 2-2).

## 3. Functional Divergence Across the Family

### 3.1 Two Major Functional Branches

The IKK family splits into two major branches with fundamentally different primary signaling roles:

**IKKα/IKKβ branch (canonical/non-canonical NF-κB):** IKKβ is the principal kinase for inducible IκB phosphorylation in the canonical NF-κB pathway, activated by TAK1 in response to inflammatory stimuli (ramadass2020smallmoleculenfκb pages 13-15, guo2024nfκbinbiology pages 2-3). IKKα functions in the non-canonical NF-κB pathway, phosphorylated by NIK in response to CD40, RANK, LTβR, and BAFF-R receptor engagement, leading to p100 processing to p52 (guo2024nfκbinbiology pages 2-3).

**TBK1/IKKε branch (type I interferon and autophagy):** TBK1 and IKKε are central kinases in innate immune nucleic acid sensing, activating IRF3 and IRF7 to induce type I interferon expression (zhou2020tbk1acentral pages 2-2). TBK1 is constitutively expressed while IKKε expression is inducible (antonia2021expandingtheview pages 6-7). They exhibit partial redundancy — IKKε compensates for loss of TBK1 protein through increased protein stability (antonia2021expandingtheview pages 6-7).

### 3.2 Intra-Branch Functional Divergence

Even within the IKKα/IKKβ pair, substantial functional divergence exists. IKKα localizes to both nucleus and cytoplasm and phosphorylates nuclear proteins including Aurora A, CBP, β-catenin, E2F1, steroid hormone receptors (ER, AR), and chromatin modulators (antonia2021expandingtheview pages 6-7, paul2018inhibitoryκbkinase(ikk) pages 3-5). IKKβ is primarily cytoplasmic and focused on IκB phosphorylation and metabolic regulation through substrates such as AMPK, XBP1, and TSC1 (antonia2021expandingtheview pages 6-7, antonia2021expandingtheview pages 3-4). The two kinases can have opposing effects when phosphorylating the same substrate — IKKα inhibits while IKKβ promotes β-catenin transcription (antonia2021expandingtheview pages 6-7).

Similarly, TBK1 and IKKε show substrate-specific divergence: TBK1 phosphorylates p62/SQSTM1 in VHL-deficient renal cancer cells, a function not shared by IKKε (antonia2021expandingtheview pages 6-7). IKKε has distinct roles in energy homeostasis — IKKε knockout mice resist high-fat diet-induced obesity through regulation of UCP1, PDE3B, and adipose tissue macrophage recruitment (antonia2021expandingtheview pages 9-11).

### 3.3 Extensive NF-κB-Independent Functions

A major finding from recent research is that IKK family members have ~50 identified phosphorylation substrates beyond their canonical pathway roles (antonia2021expandingtheview pages 1-2). These include substrates involved in autophagy regulation (TBK1 phosphorylates OPTN, p62, NDP52, TAX1BP1, and RAB7A for selective autophagy, mitophagy, and bacteriophagy) (antonia2021expandingtheview pages 9-11, white2025phosphorylationofthe pages 1-2, white2025phosphorylationofthe pages 8-10), cell cycle regulation (IKKα phosphorylates Aurora A and cyclin D1) (paul2018inhibitoryκbkinase(ikk) pages 3-5), mTOR pathway modulation (antonia2021expandingtheview pages 3-4), and RNA metabolism (HuR, Regnase-1) (antonia2021expandingtheview pages 2-3). TBK1 also regulates mitosis through phosphorylation of PLK1 and centrosome-associated proteins CEP170 and NUMA (antonia2021expandingtheview pages 11-11).

### 3.4 Pseudo-Enzyme Members

No catalytically dead (pseudokinase) members have been identified within the IKK family proper. All four mammalian members retain active kinase catalytic function. However, the regulatory subunit IKKγ/NEMO, which lacks kinase activity entirely, is not part of this PANTHER family classification.

## 4. Taxonomic Scope

### 4.1 Evolutionary Distribution

The PTHR22969 family spans 6,839 proteins across 4,084 taxa, indicating wide distribution. IKK and NF-κB homologs have been identified across a remarkably broad taxonomic range:

- **Vertebrates:** Full complement of IKKα, IKKβ, TBK1, IKKε with diversified canonical, non-canonical, and IFN signaling (williams2020lookingdownon pages 3-5).
- **Insects (Drosophila):** IKKβ homolog Ird5 functions with Kenny (IKKγ) in the IMD (immunodeficiency) pathway, phosphorylating the NF-κB factor Relish for antibacterial and antiviral immunity (cammaratamouchtouris2022dynamicregulationof pages 2-4, cammaratamouchtouris2022dynamicregulationof pages 4-6). The Drosophila cGAS-STING pathway converges on IKKβ for NF-κB-dependent antiviral responses rather than interferon induction, representing a fundamentally different downstream logic than vertebrate STING-TBK1-IRF3 signaling.
- **Cnidarians (corals, sea anemones, jellyfish):** IKK homologs are present and mediate phosphorylation-dependent processing of NF-κB/p100-like proteins (williams2020lookingdownon pages 10-12, williams2020lookingdownon pages 12-14).
- **Sponges (Porifera):** IKK-dependent phosphorylation and proteasomal processing of NF-κB emerged in sponges, the earliest-branching animal lineage studied. *Amphimedon queenslandica* contains NF-κB with structural features similar to human p100 (williams2020lookingdownon pages 12-14, williams2020lookingdownon pages 7-10).
- **Protists:** Capsaspora owczarzaki and some choanoflagellates possess RHD-containing NF-κB proteins, though with divergent activation mechanisms (caspase cleavage rather than IKK phosphorylation in *Capsaspora*) (williams2020lookingdownon pages 12-14, williams2020lookingdownon pages 5-7).

### 4.2 Notable Absences

NF-κB and IKK homologs are notably **absent from nematodes** (*C. elegans*, *C. briggsae*) and ctenophores, indicating that the pathway was lost in these lineages (williams2020lookingdownon pages 3-5, williams2020lookingdownon pages 5-7). This represents a significant caveat for any GO terms referencing NF-κB signaling, as not all taxa in which IKK-like sequences might be detected necessarily possess the full NF-κB pathway.

### 4.3 Taxonomic Implications for GO Annotation

Process-level GO terms such as "NF-κB signaling" or "I-kappaB kinase/NF-kappaB signaling" cannot be assumed to hold across all taxa matched by PTHR22969. In insects, IKK functions through a Relish/IMD pathway rather than canonical vertebrate NF-κB signaling, while in basal metazoans (sponges, cnidarians), the pathway appears to have dual developmental and immune roles that differ from vertebrate biology (williams2020lookingdownon pages 1-3, williams2020lookingdownon pages 18-20). The TBK1/IKKε-mediated interferon response pathway is vertebrate-specific, as insects lack an interferon system entirely.

## 5. Over-Annotation Verdict

### 5.1 Current State Assessment

The current state of **no InterPro2GO terms mapped** to PTHR22969 is **appropriate and should be maintained.** This is a sound decision for the following reasons:

1. **Functional heterogeneity within the family is extreme.** The family encompasses kinases with fundamentally different primary substrates (IκBs vs. IRF3/IRF7 vs. autophagy receptors), different primary signaling outputs (NF-κB activation vs. type I IFN induction vs. selective autophagy), and even opposing effects on the same substrates within the same subfamily (antonia2021expandingtheview pages 6-7).

2. **Pathway-specific terms would systematically over-annotate one branch.** "IκB kinase activity" would misannotate TBK1/IKKε; "type I interferon signaling" would misannotate IKKα/IKKβ. "NF-κB signaling" would misannotate TBK1/IKKε and would be inaccurate for organisms lacking the vertebrate NF-κB pathway architecture (ramadass2020smallmoleculenfκb pages 13-15, zhou2020tbk1acentral pages 2-2).

3. **Taxonomic breadth introduces additional complexity.** The family spans protists to vertebrates, with highly variable downstream signaling logic across lineages (williams2020lookingdownon pages 3-5, williams2020lookingdownon pages 12-14, cammaratamouchtouris2022dynamicregulationof pages 2-4).

4. **Even "safe" generic terms provide minimal informational value.** While "protein serine/threonine kinase activity" and "ATP binding" are technically correct for all members, these are so broad as to be uninformative.

### 5.2 Recommended GO Action Pattern

| Action | Recommendation |
|--------|---------------|
| **Family-level mapping** | **ACCEPT** the current no-mapping state. No GO terms should be added at the PTHR22969 family level. |
| **Generic kinase terms** | Could be mapped at family level if desired (GO:0004674, GO:0005524, GO:0006468), but these are low-value. Recommend **KEEP_AS_NON_CORE** if added. |
| **IκB kinase activity / NF-κB signaling** | **MARK_AS_OVER_ANNOTATED** if ever applied at family level; these are appropriate only for IKKα/IKKβ-containing subfamilies. |
| **Type I IFN signaling / IRF phosphorylation** | **SUBFAMILY-ONLY** — appropriate for TBK1/IKKε subfamilies only. |
| **Innate immune response** | **REJECT** at family level due to extensive non-immune functions (metabolism, cell cycle, development). |
| **Autophagy-related terms** | **SUBFAMILY-ONLY** — primarily appropriate for TBK1/IKKε. |

### 5.3 Recommendations for InterPro

The PTHR22969 family entry's 6 subfamilies should be the appropriate level at which specific GO terms are applied. The recommended strategy is:

- **Move pathway-specific GO terms to child/subfamily entries** corresponding to (a) IKKα, (b) IKKβ, (c) TBK1, and (d) IKKε, where more precise functional annotations can be safely applied.
- **At the family level**, only protein kinase molecular function terms (if any) should be considered, and even these should be treated as non-core/low-priority annotations.
- **Do not add "inhibitor of nuclear factor kappa-B kinase"** as a GO molecular function at the family level, despite the family name, because TBK1/IKKε members do not primarily function as IκB kinases (ramadass2020smallmoleculenfκb pages 13-15, antonia2021expandingtheview pages 1-2).

This approach prevents systematic over-annotation of the ~50% of family members (TBK1/IKKε branch) that function primarily in interferon signaling and autophagy rather than NF-κB signaling, while also avoiding inappropriate propagation of vertebrate-specific pathway terms to invertebrate and basal metazoan IKK homologs.

References

1. (ramadass2020smallmoleculenfκb pages 13-15): Venkataramanan Ramadass, Thamilselvan Vaiyapuri, and Vinay Tergaonkar. Small molecule nf-κb pathway inhibitors in clinic. International Journal of Molecular Sciences, 21:5164, Jul 2020. URL: https://doi.org/10.3390/ijms21145164, doi:10.3390/ijms21145164. This article has 258 citations.

2. (luo2025anexaminationof pages 8-10): Ruiqin Luo, Yuexin Yao, Zhuo Chen, and Xiaoming Sun. An examination of the lps-tlr4 immune response through the analysis of molecular structures and protein–protein interactions. Cell Communication and Signaling : CCS, Mar 2025. URL: https://doi.org/10.1186/s12964-025-02149-4, doi:10.1186/s12964-025-02149-4. This article has 152 citations.

3. (zhang2023iκbkinaseβ pages 1-2): Juan Zhang, Rui Zhang, Wei Li, Xiao-Chi Ma, Feng Qiu, and Cheng-Peng Sun. Iκb kinase β (ikkβ): structure, transduction mechanism, biological function, and discovery of its inhibitors. International Journal of Biological Sciences, 19:4181-4203, Aug 2023. URL: https://doi.org/10.7150/ijbs.85158, doi:10.7150/ijbs.85158. This article has 76 citations and is from a peer-reviewed journal.

4. (paul2018inhibitoryκbkinase(ikk) pages 12-14): Andrew Paul, Joanne Edwards, Christopher Pepper, and Simon Mackay. Inhibitory-κb kinase (ikk) α and nuclear factor-κb (nfκb)-inducing kinase (nik) as anti-cancer drug targets. Cells, 7:176, Oct 2018. URL: https://doi.org/10.3390/cells7100176, doi:10.3390/cells7100176. This article has 97 citations.

5. (li2024molecularmechanismof pages 1-2): Changqing Li, Stefano Moro, Kateryna Shostak, Francis J. O’Reilly, Mariel Donzeau, Andrea Graziadei, Alastair G. McEwen, Dominique Desplancq, Pierre Poussin-Courmontagne, Thomas Bachelart, Mert Fiskin, Nicolas Berrodier, Simon Pichard, Karl Brillet, Georges Orfanoudakis, Arnaud Poterszman, Vladimir Torbeev, Juri Rappsilber, Norman E. Davey, Alain Chariot, and Katia Zanier. Molecular mechanism of ikk catalytic dimer docking to nf-κb substrates. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-52076-0, doi:10.1038/s41467-024-52076-0. This article has 48 citations and is from a highest quality peer-reviewed journal.

6. (zhou2020tbk1acentral pages 2-2): Ruyuan Zhou, Qian Zhang, and Pinglong Xu. Tbk1, a central kinase in innate immune sensing of nucleic acids and beyond. Acta biochimica et biophysica Sinica, 52:757-767, May 2020. URL: https://doi.org/10.1093/abbs/gmaa051, doi:10.1093/abbs/gmaa051. This article has 109 citations and is from a peer-reviewed journal.

7. (hotchkiss2021discoveryofan pages 4-7): Sonjiala Jackson Hotchkiss, Maria Carmen Mulero, Garrett J. Chan, Tapan Biswas, Smarajit Polley, Christine Ohn, Srihari Konduri, Dionicio Siegel, Özlem Demir, Rommie E. Amaro, and Gourisankar Ghosh. Discovery of an ikk2 site that allosterically controls its activation. bioRxiv, Jan 2021. URL: https://doi.org/10.1101/2021.01.27.428502, doi:10.1101/2021.01.27.428502. This article has 1 citations.

8. (hotchkiss2021discoveryofan pages 1-4): Sonjiala Jackson Hotchkiss, Maria Carmen Mulero, Garrett J. Chan, Tapan Biswas, Smarajit Polley, Christine Ohn, Srihari Konduri, Dionicio Siegel, Özlem Demir, Rommie E. Amaro, and Gourisankar Ghosh. Discovery of an ikk2 site that allosterically controls its activation. bioRxiv, Jan 2021. URL: https://doi.org/10.1101/2021.01.27.428502, doi:10.1101/2021.01.27.428502. This article has 1 citations.

9. (hotchkiss2021discoveryofan pages 7-9): Sonjiala Jackson Hotchkiss, Maria Carmen Mulero, Garrett J. Chan, Tapan Biswas, Smarajit Polley, Christine Ohn, Srihari Konduri, Dionicio Siegel, Özlem Demir, Rommie E. Amaro, and Gourisankar Ghosh. Discovery of an ikk2 site that allosterically controls its activation. bioRxiv, Jan 2021. URL: https://doi.org/10.1101/2021.01.27.428502, doi:10.1101/2021.01.27.428502. This article has 1 citations.

10. (guo2024nfκbinbiology pages 2-3): Qing Guo, Yizi Jin, Xinyu Chen, Xiaomin Ye, Xin Shen, Mingxi Lin, C. Zeng, Teng Zhou, and Jian Zhang. Nf-κb in biology and targeted therapy: new insights and translational implications. Signal Transduction and Targeted Therapy, Mar 2024. URL: https://doi.org/10.1038/s41392-024-01757-9, doi:10.1038/s41392-024-01757-9. This article has 2220 citations and is from a peer-reviewed journal.

11. (antonia2021expandingtheview pages 6-7): Ricardo J. Antonia, Robert S. Hagan, and Albert S. Baldwin. Expanding the view of ikk: new substrates and new biology. Mar 2021. URL: https://doi.org/10.1016/j.tcb.2020.12.003, doi:10.1016/j.tcb.2020.12.003. This article has 109 citations and is from a domain leading peer-reviewed journal.

12. (paul2018inhibitoryκbkinase(ikk) pages 3-5): Andrew Paul, Joanne Edwards, Christopher Pepper, and Simon Mackay. Inhibitory-κb kinase (ikk) α and nuclear factor-κb (nfκb)-inducing kinase (nik) as anti-cancer drug targets. Cells, 7:176, Oct 2018. URL: https://doi.org/10.3390/cells7100176, doi:10.3390/cells7100176. This article has 97 citations.

13. (antonia2021expandingtheview pages 4-6): Ricardo J. Antonia, Robert S. Hagan, and Albert S. Baldwin. Expanding the view of ikk: new substrates and new biology. Mar 2021. URL: https://doi.org/10.1016/j.tcb.2020.12.003, doi:10.1016/j.tcb.2020.12.003. This article has 109 citations and is from a domain leading peer-reviewed journal.

14. (antonia2021expandingtheview pages 9-11): Ricardo J. Antonia, Robert S. Hagan, and Albert S. Baldwin. Expanding the view of ikk: new substrates and new biology. Mar 2021. URL: https://doi.org/10.1016/j.tcb.2020.12.003, doi:10.1016/j.tcb.2020.12.003. This article has 109 citations and is from a domain leading peer-reviewed journal.

15. (revach2020targetingtankbindingkinase pages 4-6): Or-Yam Revach, Shuming Liu, and Russell W. Jenkins. Targeting tank-binding kinase 1 (tbk1) in cancer. Oct 2020. URL: https://doi.org/10.1080/14728222.2020.1826929, doi:10.1080/14728222.2020.1826929. This article has 62 citations and is from a peer-reviewed journal.

16. (revach2020targetingtankbindingkinase pages 18-19): Or-Yam Revach, Shuming Liu, and Russell W. Jenkins. Targeting tank-binding kinase 1 (tbk1) in cancer. Oct 2020. URL: https://doi.org/10.1080/14728222.2020.1826929, doi:10.1080/14728222.2020.1826929. This article has 62 citations and is from a peer-reviewed journal.

17. (white2025phosphorylationofthe pages 1-2): Jesse White, Young Bong Choi, Jiawen Zhang, Mai Tram Vo, Chaoxia He, Kashif Shaikh, and Edward W. Harhaj. Phosphorylation of the selective autophagy receptor tax1bp1 by tbk1 and ikbke/ikki promotes atg8-family protein-dependent clearance of mavs aggregates. Autophagy, 21:160-177, Sep 2025. URL: https://doi.org/10.1080/15548627.2024.2394306, doi:10.1080/15548627.2024.2394306. This article has 22 citations and is from a domain leading peer-reviewed journal.

18. (cammaratamouchtouris2022dynamicregulationof pages 2-4): Alexandre Cammarata-Mouchtouris, Adrian Acker, Akira Goto, Di Chen, Nicolas Matt, and Vincent Leclerc. Dynamic regulation of nf-κb response in innate immunity: the case of the imd pathway in drosophila. Biomedicines, 10:2304, Sep 2022. URL: https://doi.org/10.3390/biomedicines10092304, doi:10.3390/biomedicines10092304. This article has 46 citations.

19. (cammaratamouchtouris2022dynamicregulationof pages 4-6): Alexandre Cammarata-Mouchtouris, Adrian Acker, Akira Goto, Di Chen, Nicolas Matt, and Vincent Leclerc. Dynamic regulation of nf-κb response in innate immunity: the case of the imd pathway in drosophila. Biomedicines, 10:2304, Sep 2022. URL: https://doi.org/10.3390/biomedicines10092304, doi:10.3390/biomedicines10092304. This article has 46 citations.

20. (antonia2021expandingtheview pages 1-2): Ricardo J. Antonia, Robert S. Hagan, and Albert S. Baldwin. Expanding the view of ikk: new substrates and new biology. Mar 2021. URL: https://doi.org/10.1016/j.tcb.2020.12.003, doi:10.1016/j.tcb.2020.12.003. This article has 109 citations and is from a domain leading peer-reviewed journal.

21. (antonia2021expandingtheview pages 3-4): Ricardo J. Antonia, Robert S. Hagan, and Albert S. Baldwin. Expanding the view of ikk: new substrates and new biology. Mar 2021. URL: https://doi.org/10.1016/j.tcb.2020.12.003, doi:10.1016/j.tcb.2020.12.003. This article has 109 citations and is from a domain leading peer-reviewed journal.

22. (antonia2021expandingtheview pages 7-9): Ricardo J. Antonia, Robert S. Hagan, and Albert S. Baldwin. Expanding the view of ikk: new substrates and new biology. Mar 2021. URL: https://doi.org/10.1016/j.tcb.2020.12.003, doi:10.1016/j.tcb.2020.12.003. This article has 109 citations and is from a domain leading peer-reviewed journal.

23. (white2025phosphorylationofthe pages 8-10): Jesse White, Young Bong Choi, Jiawen Zhang, Mai Tram Vo, Chaoxia He, Kashif Shaikh, and Edward W. Harhaj. Phosphorylation of the selective autophagy receptor tax1bp1 by tbk1 and ikbke/ikki promotes atg8-family protein-dependent clearance of mavs aggregates. Autophagy, 21:160-177, Sep 2025. URL: https://doi.org/10.1080/15548627.2024.2394306, doi:10.1080/15548627.2024.2394306. This article has 22 citations and is from a domain leading peer-reviewed journal.

24. (antonia2021expandingtheview pages 2-3): Ricardo J. Antonia, Robert S. Hagan, and Albert S. Baldwin. Expanding the view of ikk: new substrates and new biology. Mar 2021. URL: https://doi.org/10.1016/j.tcb.2020.12.003, doi:10.1016/j.tcb.2020.12.003. This article has 109 citations and is from a domain leading peer-reviewed journal.

25. (antonia2021expandingtheview pages 11-11): Ricardo J. Antonia, Robert S. Hagan, and Albert S. Baldwin. Expanding the view of ikk: new substrates and new biology. Mar 2021. URL: https://doi.org/10.1016/j.tcb.2020.12.003, doi:10.1016/j.tcb.2020.12.003. This article has 109 citations and is from a domain leading peer-reviewed journal.

26. (williams2020lookingdownon pages 3-5): Leah M. Williams and Thomas D. Gilmore. Looking down on nf-<i>κ</i>b. Jul 2020. URL: https://doi.org/10.1128/mcb.00104-20, doi:10.1128/mcb.00104-20. This article has 162 citations and is from a domain leading peer-reviewed journal.

27. (williams2020lookingdownon pages 10-12): Leah M. Williams and Thomas D. Gilmore. Looking down on nf-<i>κ</i>b. Jul 2020. URL: https://doi.org/10.1128/mcb.00104-20, doi:10.1128/mcb.00104-20. This article has 162 citations and is from a domain leading peer-reviewed journal.

28. (williams2020lookingdownon pages 12-14): Leah M. Williams and Thomas D. Gilmore. Looking down on nf-<i>κ</i>b. Jul 2020. URL: https://doi.org/10.1128/mcb.00104-20, doi:10.1128/mcb.00104-20. This article has 162 citations and is from a domain leading peer-reviewed journal.

29. (williams2020lookingdownon pages 7-10): Leah M. Williams and Thomas D. Gilmore. Looking down on nf-<i>κ</i>b. Jul 2020. URL: https://doi.org/10.1128/mcb.00104-20, doi:10.1128/mcb.00104-20. This article has 162 citations and is from a domain leading peer-reviewed journal.

30. (williams2020lookingdownon pages 5-7): Leah M. Williams and Thomas D. Gilmore. Looking down on nf-<i>κ</i>b. Jul 2020. URL: https://doi.org/10.1128/mcb.00104-20, doi:10.1128/mcb.00104-20. This article has 162 citations and is from a domain leading peer-reviewed journal.

31. (williams2020lookingdownon pages 1-3): Leah M. Williams and Thomas D. Gilmore. Looking down on nf-<i>κ</i>b. Jul 2020. URL: https://doi.org/10.1128/mcb.00104-20, doi:10.1128/mcb.00104-20. This article has 162 citations and is from a domain leading peer-reviewed journal.

32. (williams2020lookingdownon pages 18-20): Leah M. Williams and Thomas D. Gilmore. Looking down on nf-<i>κ</i>b. Jul 2020. URL: https://doi.org/10.1128/mcb.00104-20, doi:10.1128/mcb.00104-20. This article has 162 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PTHR22969-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR22969-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. hotchkiss2021discoveryofan pages 4-7
2. li2024molecularmechanismof pages 1-2
3. hotchkiss2021discoveryofan pages 1-4
4. antonia2021expandingtheview pages 6-7
5. antonia2021expandingtheview pages 9-11
6. antonia2021expandingtheview pages 1-2
7. antonia2021expandingtheview pages 3-4
8. antonia2021expandingtheview pages 2-3
9. antonia2021expandingtheview pages 11-11
10. williams2020lookingdownon pages 3-5
11. luo2025anexaminationof pages 8-10
12. hotchkiss2021discoveryofan pages 7-9
13. antonia2021expandingtheview pages 4-6
14. revach2020targetingtankbindingkinase pages 4-6
15. revach2020targetingtankbindingkinase pages 18-19
16. white2025phosphorylationofthe pages 1-2
17. cammaratamouchtouris2022dynamicregulationof pages 2-4
18. cammaratamouchtouris2022dynamicregulationof pages 4-6
19. antonia2021expandingtheview pages 7-9
20. white2025phosphorylationofthe pages 8-10
21. williams2020lookingdownon pages 10-12
22. williams2020lookingdownon pages 12-14
23. williams2020lookingdownon pages 7-10
24. williams2020lookingdownon pages 5-7
25. williams2020lookingdownon pages 1-3
26. williams2020lookingdownon pages 18-20
27. https://doi.org/10.3390/ijms21145164,
28. https://doi.org/10.1186/s12964-025-02149-4,
29. https://doi.org/10.7150/ijbs.85158,
30. https://doi.org/10.3390/cells7100176,
31. https://doi.org/10.1038/s41467-024-52076-0,
32. https://doi.org/10.1093/abbs/gmaa051,
33. https://doi.org/10.1101/2021.01.27.428502,
34. https://doi.org/10.1038/s41392-024-01757-9,
35. https://doi.org/10.1016/j.tcb.2020.12.003,
36. https://doi.org/10.1080/14728222.2020.1826929,
37. https://doi.org/10.1080/15548627.2024.2394306,
38. https://doi.org/10.3390/biomedicines10092304,
39. https://doi.org/10.1128/mcb.00104-20,