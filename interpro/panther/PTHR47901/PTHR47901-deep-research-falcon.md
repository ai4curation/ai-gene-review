---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T21:57:03.841360'
end_time: '2026-06-28T22:21:29.762466'
duration_seconds: 1465.92
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR47901
  interpro_name: CASPASE RECRUITMENT DOMAIN-CONTAINING PROTEIN 18
  interpro_short_name: Not specified
  interpro_type: family
  interpro_integrated: IPR002398
  member_databases: Not specified
  n_proteins: '6464'
  n_taxa: '4282'
  n_subfamilies: '5'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: Not specified in InterPro
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 25
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR47901-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR47901-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** PTHR47901
- **Name:** CASPASE RECRUITMENT DOMAIN-CONTAINING PROTEIN 18
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR002398
- **Member database signatures:** Not specified
- **Scale:** 6464 proteins across 4282 taxa, 5 subfamilies
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
**PTHR47901 (CASPASE RECRUITMENT DOMAIN-CONTAINING PROTEIN 18)**, structured to support GO annotation review.

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
- **Accession:** PTHR47901
- **Name:** CASPASE RECRUITMENT DOMAIN-CONTAINING PROTEIN 18
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR002398
- **Member database signatures:** Not specified
- **Scale:** 6464 proteins across 4282 taxa, 5 subfamilies
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
**PTHR47901 (CASPASE RECRUITMENT DOMAIN-CONTAINING PROTEIN 18)**, structured to support GO annotation review.

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


# InterPro Family Research Report: PTHR47901 — Caspase Recruitment Domain-Containing Protein 18 (CARD18)

## 1. Family Definition and Biochemistry

### 1.1 Molecular Identity

CARD18, also known as ICEBERG, is a CARD-only protein (COP) that was the first identified member of the COP class of inflammasome regulators (devi2020anupdateon pages 7-9). It encodes a small, ~90-amino acid protein consisting solely of a single caspase recruitment domain (CARD) with 52% amino acid sequence homology to the CARD of caspase-1 (devi2020anupdateon pages 7-9, matusiak2015card‐andpyrin‐only pages 4-6). The gene is located on human chromosome 11q22.3, adjacent to the caspase-1 gene and the other COP genes (CARD16 and CARD17) within the proinflammatory caspase gene cluster (matusiak2015card‐andpyrin‐only pages 2-4, hoss2017assemblyandregulation pages 10-11).

### 1.2 Structural Fold

CARD18 adopts the characteristic death domain (DD) superfamily fold: a globular six-helix bundle with anti-parallel helices and a polarized charge distribution on the surface (jin2015activationandassembly pages 1-3, park2019caspaserecruitmentdomains pages 4-6). A distinguishing feature of CARD domains relative to other DD superfamily members is a bent or broken helix H1 (sometimes split into H1a and H1b), which creates a core hydrophobic cluster connecting all six helices (park2019caspaserecruitmentdomains pages 3-4, park2019caspaserecruitmentdomains pages 4-6). The NMR structure of CARD18 has been solved and reveals positively charged residues in α-helices 1, 4, and 6 and negatively charged residues in helices 2 and 5, enabling electrostatic interactions with the caspase-1 CARD (devi2020anupdateon pages 7-9). This charge complementarity drives the CARD–CARD homotypic interactions that underlie CARD18's regulatory function.

### 1.3 Mechanism of Action

CARD18 functions primarily as a dominant-negative regulator of inflammasome signaling (matusiak2015card‐andpyrin‐only pages 4-6, matusiak2015card‐andpyrin‐only pages 2-4). It binds caspase-1 through CARD–CARD interactions and inhibits caspase-1 oligomerization and activation, thereby reducing the maturation and secretion of IL-1β (devi2020anupdateon pages 7-9, matusiak2015card‐andpyrin‐only pages 4-6). Unlike CARD16 (COP/Pseudo-ICE), CARD18 does not bind RIPK2, a key mediator in NF-κB signaling; this difference was traced to an Arg45Asp mutation that impairs RIPK2 recruitment (matusiak2015card‐andpyrin‐only pages 6-7). However, CARD18's mechanism is not fully resolved: while most studies report inhibitory function, at least one report suggests that CARD18 may promote caspase-1 polymerization and filament formation without enhancing IL-1β release, indicating possible context-dependent activity (devi2020anupdateon pages 7-9).

The related COP protein CARD17 (INCA) has been shown by cryo-EM to cap growing caspase-1 CARD filaments. The cryo-EM structure of the caspase-1 CARD filament was determined at 4.8 Å resolution, and INCA's capping mechanism was elucidated using a homology model based on the CARD18 NMR structure (lu2016molecularbasisof pages 1-11). INCA incorporates into the filament through conserved type Ia, IIa, IIIa, and IIIb interfaces but is defective at the type Ib and IIb interfaces, terminating filament elongation (lu2016molecularbasisof pages 1-11).

The following table compares CARD18 with the two other human CARD-only proteins:

| Protein | Aliases | Size / architecture | Domain structure | Fold / structural notes | Mechanism of action | Taxonomic distribution | Chromosomal location / origin | Key interactions | Disease / translational associations |
|---|---|---|---|---|---|---|---|---|---|
| CARD18 | ICEBERG; caspase recruitment domain family member 18 | ~90 aa; CARD-only protein | Single CARD domain only | CARD adopts death-domain superfamily six-helix bundle; CARDs characteristically have a bent/broken H1 helix; CARD18 NMR structure shows polarized charge distribution with positive residues in helices 1/4/6 and negative residues in helices 2/5, enabling electrostatic CARD:CARD contacts (park2019caspaserecruitmentdomains pages 3-4, devi2020anupdateon pages 7-9, jin2015activationandassembly pages 1-3, park2019caspaserecruitmentdomains pages 4-6) | Generally described as a dominant-negative regulator of caspase-1/inflammasome signaling by binding caspase-1 CARD and inhibiting oligomerization/activation and IL-1β maturation; however, some studies/reporting note a context-dependent or controversial effect, including promotion of caspase-1 polymerization without increased IL-1β release (devi2020anupdateon pages 7-9, matusiak2015card‐andpyrin‐only pages 4-6, matusiak2015card‐andpyrin‐only pages 2-4) | True orthologous CARD18 is primate-restricted; reported in human and rhesus monkey, with locus evidence in treeshrew; absent from mouse and rat, and reported absent from chimpanzee in some analyses (le2013pyrinandcardonly pages 4-5, le2013pyrinandcardonly pages 6-8, matusiak2015card‐andpyrin‐only pages 4-6, hoss2017assemblyandregulation pages 10-11) | Human chromosome 11q22.3, adjacent to CASP1 in the proinflammatory caspase cluster; arose via recent CASP1-region duplication during primate evolution (matusiak2015card‐andpyrin‐only pages 2-4, hoss2017assemblyandregulation pages 10-11, stevens2025largescalerestructuringof pages 1-4) | Caspase-1 CARD; unlike some other COPs, does not clearly bind RIPK2; Arg45Asp noted as relevant to differential RIPK2-related behavior (matusiak2015card‐andpyrin‐only pages 4-6, matusiak2015card‐andpyrin‐only pages 6-7, sharma2021structureactivationand pages 20-22) | Expression inversely associated with some inflammatory/cardiovascular contexts; lower ICEBERG reported in severe cardiac disease and downregulation reported in periodontal disease; Open Targets associations exist but are indirect/non-mechanistic and not sufficient for family-level functional assignment (matusiak2015card‐andpyrin‐only pages 4-6, OpenTargets Search: -CARD18) |
| CARD17 | INCA; inhibitory CARD | ~110 aa; CARD-only protein | Single CARD domain only | CARD-only fold inferred as standard CARD/death-domain six-helix bundle; structural modeling and cryo-EM-based analysis show selective interface competence/defects enabling filament capping (lu2016molecularbasisof pages 1-11, park2019caspaserecruitmentdomains pages 3-4, park2019caspaserecruitmentdomains pages 4-6, devi2020anupdateon pages 7-9) | Potent inhibitor of caspase-1 CARD polymerization; caps growing caspase-1 CARD filaments through a distinct capping mechanism, preventing further filament elongation and repressing inflammasome activation (lu2016molecularbasisof pages 1-11, devi2020anupdateon pages 7-9) | Primate-restricted COP; part of the primate CASP1-duplication-derived COP set (le2013pyrinandcardonly pages 4-5, matusiak2015card‐andpyrin‐only pages 2-4, hoss2017assemblyandregulation pages 10-11, le2013pyrinandcardonly pages 6-8) | Human chromosome 11q22 / 11q22.3 near CASP1; derived from recent duplication in the CASP1 cluster (matusiak2015card‐andpyrin‐only pages 2-4, hoss2017assemblyandregulation pages 10-11, stevens2025largescalerestructuringof pages 1-4) | Caspase-1 CARD; lacks self-oligomerization behavior needed for elongation, consistent with capping rather than propagation (lu2016molecularbasisof pages 1-11, devi2020anupdateon pages 7-9) | No strong disease-specific role established from the retrieved evidence; most relevance is as an endogenous inflammasome inhibitor and mechanistic template for anti-inflammasome strategies (lu2016molecularbasisof pages 1-11, devi2020anupdateon pages 7-9) |
| CARD16 | COP; Pseudo-ICE; caspase recruitment domain family member 16 | ~91–97 aa; CARD-only protein | Single CARD domain only | CARD-only fold inferred as standard six-helix bundle of the CARD/death-domain superfamily (park2019caspaserecruitmentdomains pages 3-4, jin2015activationandassembly pages 1-3, park2019caspaserecruitmentdomains pages 4-6, devi2020anupdateon pages 7-9) | Binds caspase-1 CARD and can self-oligomerize; reported as functionally dual/context-dependent, acting either as inhibitor or promoter of caspase-1 assembly/IL-1β processing depending on experimental context and cell type (devi2020anupdateon pages 7-9) | Primate-restricted COP; no orthologs in mouse/rat reported in the reviewed literature (le2013pyrinandcardonly pages 4-5, matusiak2015card‐andpyrin‐only pages 2-4, hoss2017assemblyandregulation pages 10-11, le2013pyrinandcardonly pages 6-8) | Human chromosome 11q22 near CASP1 within the proinflammatory caspase cluster; generated through recent duplication in the CASP1 region (le2013pyrinandcardonly pages 4-5, matusiak2015card‐andpyrin‐only pages 2-4, hoss2017assemblyandregulation pages 10-11, stevens2025largescalerestructuringof pages 1-4) | Caspase-1 CARD; can self-oligomerize, unlike CARD17 and CARD18 (devi2020anupdateon pages 7-9) | Recent experimental literature outside the core COP reviews links CARD16 to tumor phenotypes (e.g., glioma), but this is not yet evidence for conserved family-wide biology; primary established role remains inflammasome modulation (devi2020anupdateon pages 7-9) |


*Table: This table compares the three human CARD-only proteins (CARD16, CARD17, CARD18), summarizing their shared CARD-only architecture and their distinct mechanisms in regulating caspase-1 and inflammasome assembly. It is useful for GO review because it shows that even within the small COP group, function is not uniform enough to justify broad family-level annotation.*

### 1.4 Tissue Expression and Regulation

CARD18 is highly expressed in the heart, placenta, and other tissues (matusiak2015card‐andpyrin‐only pages 4-6). Its expression is upregulated by LPS and pro-inflammatory stimuli, and ICEBERG expression inversely correlates with cardiovascular disease risk, with lower cardiac ICEBERG levels associated with increased need for left ventricular assist device implantation (matusiak2015card‐andpyrin‐only pages 4-6). In periodontal disease, CARD18 is significantly downregulated in gingivitis, chronic periodontitis, and aggressive periodontitis compared to periodontal health, potentially contributing to excessive inflammasome activity (matusiak2015card‐andpyrin‐only pages 4-6). CARD18 is also specifically expressed during late differentiation of keratinocytes.

---

## 2. InterPro2GO Mapping Appropriateness

### 2.1 Current Status

PTHR47901 currently has **no InterPro2GO terms mapped**. This review evaluates whether this absence is appropriate and whether any GO terms should be added.

### 2.2 Critical Family Scope Issue

A fundamental concern is the discrepancy between the PANTHER family's reported scope (6,464 proteins across 4,282 taxa, with 5 subfamilies) and the known biology of CARD18. True CARD18/ICEBERG orthologs are restricted to a small number of primate species (le2013pyrinandcardonly pages 4-5, le2013pyrinandcardonly pages 6-8). The three human COPs (CARD16, CARD17, CARD18) arose from recent caspase-1 gene duplications restricted to primates and hominids (matusiak2015card‐andpyrin‐only pages 2-4, hoss2017assemblyandregulation pages 10-11). Stevens et al. (2025) confirmed that Card16, Card17, and Card18 are found in humans and chimpanzees as a result of Caspase-1 duplication, part of an evolutionary cluster expansion restricted to great apes (stevens2025largescalerestructuringof pages 1-4, stevens2025largescalerestructuringof pages 17-20). The family's coverage of >4,000 taxa therefore strongly suggests that the PANTHER signature is capturing a much broader set of CARD-domain-containing proteins beyond true CARD18 orthologs — likely including CARD-containing regions from caspases, NLR proteins, and other CARD-bearing proteins across diverse organisms.

### 2.3 Evaluation of Potential GO Terms

The following table evaluates GO terms that could plausibly be considered for this entry:

| Potential GO term | Label | Appropriate for **all** proteins matched by PTHR47901? | Verdict | Reason |
|---|---|---|---|---|
| GO:0043027 | caspase inhibitor activity | No | REJECT | Experimental support for true human/primate CARD18/ICEBERG points to inhibition of caspase-1 via CARD:CARD interaction, but PTHR47901 spans 6464 proteins across 4282 taxa, far broader than the primate-restricted true CARD18 ortholog set; therefore this activity cannot be assumed for all matched proteins. In addition, CARD18 function itself is not fully uniform across reports (mostly inhibitory, but some evidence suggests promotion of caspase-1 polymerization in some contexts) (devi2020anupdateon pages 7-9, matusiak2015card‐andpyrin‐only pages 4-6, le2013pyrinandcardonly pages 4-5, le2013pyrinandcardonly pages 6-8, hoss2017assemblyandregulation pages 10-11, stevens2025largescalerestructuringof pages 1-4). |
| GO:0043154 | negative regulation of caspase activity | No | SUBFAMILY-ONLY | This is a reasonable biological summary for validated primate CARD18/ICEBERG proteins, which generally inhibit caspase-1 activation and IL-1β maturation, but it is not safe at the PTHR47901 family level because the signature appears to include many non-CARD18 proteins across taxa; it would only be defensible on a narrower child entry limited to experimentally supported CARD18 orthologs (devi2020anupdateon pages 7-9, matusiak2015card‐andpyrin‐only pages 4-6, le2013pyrinandcardonly pages 4-5, matusiak2015card‐andpyrin‐only pages 2-4, hoss2017assemblyandregulation pages 10-11). |
| GO:0050727 | regulation of inflammatory response | No | SUBFAMILY-ONLY | True CARD18 proteins regulate inflammasome output and IL-1β release, so the term fits the characterized primate COP subfamily at a high level; however it is too broad and likely over-annotating for a family that appears to capture diverse CARD-containing proteins beyond true CARD18, many of which may participate in different pathways or even opposite regulatory effects (devi2020anupdateon pages 7-9, matusiak2015card‐andpyrin‐only pages 4-6, park2019caspaserecruitmentdomains pages 1-3, hoss2017assemblyandregulation pages 10-11, stevens2025largescalerestructuringof pages 1-4). |
| GO:0005829 | cytosol | No | REJECT | Inflammasome signaling proteins including CARD18 function in the cytosolic compartment, but compartment terms should only be added when confidently true for essentially all matched proteins. Given the huge taxonomic breadth of PTHR47901 and likely inclusion of diverse CARD-containing proteins with different architectures and localizations, this term is not safe at family level (park2019caspaserecruitmentdomains pages 1-3, hoss2017assemblyandregulation pages 10-11, stevens2025largescalerestructuringof pages 1-4). |
| GO:0035872 | cellular response to cytokine stimulus | No | REJECT | CARD18 expression can be induced by inflammatory stimuli such as LPS, but that is a context-specific property of studied mammalian COPs rather than a universal function of all proteins matched by this PANTHER family; it should not be propagated across 4282 taxa (matusiak2015card‐andpyrin‐only pages 4-6, hoss2017assemblyandregulation pages 10-11). |
| GO:0140677 | molecular function regulator activity | No | REJECT | Although CARD18 is a non-enzymatic regulator of caspase-1 assembly, this term is too generic to be useful and still unsupported across the full breadth of the family. It would add little information and risks masking major functional heterogeneity (devi2020anupdateon pages 7-9, park2019caspaserecruitmentdomains pages 1-3, hoss2017assemblyandregulation pages 10-11). |
| GO:1900224 | regulation of inflammasome complex assembly | No | SUBFAMILY-ONLY | Mechanistically attractive for true CARD18/COP proteins because they modulate caspase-1 polymerization and inflammasome signaling, but not demonstrably true for all family matches. The broad taxonomic scope of PTHR47901 strongly argues against assigning this pathway-specific term at the current family node (devi2020anupdateon pages 7-9, lu2016molecularbasisof pages 1-11, hoss2017assemblyandregulation pages 10-11, stevens2025largescalerestructuringof pages 1-4). |
| GO:1990440 | negative regulation of NLRP3 inflammasome complex assembly | No | REJECT | Too specific: available evidence places CARD18 primarily at the level of caspase-1 CARD interactions, not as a universal direct NLRP3-specific regulator. Even for human CARD18 this would be an inference, and it is certainly not appropriate across the full family (devi2020anupdateon pages 7-9, matusiak2015card‐andpyrin‐only pages 4-6, lu2016molecularbasisof pages 1-11). |
| GO:0005515 | protein binding | No | REJECT | CARD18 and other CARD proteins mediate protein-protein interactions, but “protein binding” is too generic to be useful for InterPro2GO and would provide little biological specificity while still not being meaningful across this heterogeneous family (park2019caspaserecruitmentdomains pages 3-4, jin2015activationandassembly pages 1-3, park2019caspaserecruitmentdomains pages 1-3). |
| — | **Overall recommendation for PTHR47901** | — | **KEEP NO MAPPING / REMOVE any future broad mappings** | Current absence of InterPro2GO mapping is the correct state. Evidence indicates that true CARD18 is a primate-specific CARD-only inflammasome regulator, whereas PTHR47901 contains thousands of proteins across thousands of taxa and therefore is unlikely to represent a functionally homogeneous CARD18-only family. GO terms describing caspase inhibition, inflammasome regulation, or inflammatory processes should only be considered on a much narrower child/subfamily entry with explicit orthology and experimental support (le2013pyrinandcardonly pages 4-5, le2013pyrinandcardonly pages 6-8, park2019caspaserecruitmentdomains pages 1-3, hoss2017assemblyandregulation pages 10-11, stevens2025largescalerestructuringof pages 1-4, stevens2025largescalerestructuringof pages 17-20). |


*Table: This table evaluates plausible GO terms for PTHR47901 and shows why none are safe for family-wide propagation. It is useful for GO review because it distinguishes terms that may fit true primate CARD18 proteins from terms that would over-annotate the broad PANTHER family.*

### 2.4 Summary of Mapping Appropriateness

The current absence of InterPro2GO mappings for PTHR47901 is **appropriate and should be maintained**. No GO term describing caspase-1 inhibition, inflammasome regulation, or inflammatory signaling can be safely applied across all 6,464 proteins matched by this signature, given the extreme taxonomic breadth and the primate-restricted nature of true CARD18 function.

---

## 3. Functional Divergence Across the Family

### 3.1 Divergence Among Human COPs

Even within the closely related human COP set, functional divergence is evident. CARD16 can self-oligomerize and has been reported to both inhibit and promote IL-1β maturation depending on cell type and experimental context (devi2020anupdateon pages 7-9). CARD17 is a potent inhibitor that specifically caps caspase-1 CARD filaments with low-nanomolar Ki, using a distinct structural capping mechanism where defective type Ib and IIb interfaces prevent further subunit recruitment (lu2016molecularbasisof pages 1-11, devi2020anupdateon pages 7-9). CARD18 generally inhibits caspase-1 oligomerization and IL-1β release, but does not interact with RIPK2 (unlike CARD16), and one study reports it may promote caspase-1 polymerization without increasing IL-1β release (devi2020anupdateon pages 7-9, matusiak2015card‐andpyrin‐only pages 6-7). These COPs also differ in NF-κB regulation: CARD16 and CARD17 interact with RIPK2 and modulate NF-κB, while CARD18's Arg45Asp mutation impairs this interaction (matusiak2015card‐andpyrin‐only pages 6-7).

### 3.2 Pseudo-Enzyme Character

CARD18 is itself a "pseudo-enzyme" by design — it retains the CARD fold of caspase-1 but completely lacks the catalytic cysteine protease domain. It functions purely as a non-catalytic decoy that competes for CARD–CARD interaction surfaces (matusiak2015card‐andpyrin‐only pages 2-4, le2013pyrinandcardonly pages 4-5). All three human COPs share this characteristic of being catalytically dead derivatives of caspase-1 that retain only the protein–protein interaction domain (le2013pyrinandcardonly pages 4-5).

### 3.3 Broader Family Heterogeneity

Given that PTHR47901 matches 6,464 proteins across 4,282 taxa — vastly exceeding the handful of primate species where true CARD18 exists — the family almost certainly encompasses proteins with fundamentally different functions. Approximately 33 CARD-containing proteins have been identified in mammals alone, spanning apoptosis (Apaf-1, caspase-9, RAIDD), innate immunity (RIG-I, NLRC4, NOD1, NOD2), NF-κB signaling (CARD9, BCL10, CARMA proteins), and inflammasome assembly (ASC, caspase-1) (park2019caspaserecruitmentdomains pages 1-3, park2019caspaserecruitmentdomains pages 3-4, hong2002caspaserecruitmentdomain pages 1-3). The CARD domain is a versatile protein interaction module used in divergent signaling pathways, making any single functional annotation inappropriate for a family-level assignment at this breadth.

---

## 4. Taxonomic Scope

### 4.1 True CARD18 Distribution

True CARD18/ICEBERG orthologs are restricted to **higher primates**:

- **Humans**: CARD18 is present on chromosome 11q22.3, well-characterized experimentally (matusiak2015card‐andpyrin‐only pages 2-4).
- **Rhesus monkey** (*Macaca mulatta*): 100% amino acid identity with human CARD18 (matusiak2015card‐andpyrin‐only pages 4-6).
- **Treeshrew**: An ICEBERG locus has been reported, consistent with treeshrew being considered a primate ancestor (le2013pyrinandcardonly pages 6-8).
- **Chimpanzee**: CARD18 is reported absent from the chimpanzee genome, possibly deleted after the human–chimpanzee lineage split, though this may reflect incomplete sequencing (le2013pyrinandcardonly pages 6-8, matusiak2015card‐andpyrin‐only pages 4-6). However, Stevens et al. (2025) note Card16/17/18 in humans and chimpanzees, possibly indicating the gene is present in some chimpanzee assemblies (stevens2025largescalerestructuringof pages 17-20).
- **Non-primate mammals**: Absent from mice, rats, dogs, cows, and other non-primate species (le2013pyrinandcardonly pages 6-8, hoss2017assemblyandregulation pages 10-11).
- **Birds and fish**: Not present; chicken lacks several inflammasome pathway components entirely (stevens2025largescalerestructuringof pages 1-4, stevens2025largescalerestructuringof pages 4-7).

### 4.2 Caspase-1 Cluster Evolution

The proinflammatory caspase gene cluster underwent massive reorganization during mammalian evolution. Caspase-1 translocated to a new chromosomal region in early mammalian evolution, followed by gene duplication giving rise to caspase-11 and caspase-12 in therians, and later duplications producing caspase-4 and caspase-5 in hominids (stevens2025largescalerestructuringof pages 1-4, stevens2025largescalerestructuringof pages 14-17). The CARD-only protein genes (CARD16, CARD17, CARD18) represent the most recent duplication events, restricted to great apes, and were generated from caspase-1 CARD duplications within this unstable chromosomal region (stevens2025largescalerestructuringof pages 17-20).

### 4.3 Implications for the PANTHER Family

The fact that PTHR47901 matches 6,464 proteins across 4,282 taxa is incompatible with the primate-restricted biology of CARD18. The PANTHER family likely detects broader CARD-domain sequence similarity, effectively grouping true CARD18 orthologs with CARD-containing regions from diverse proteins across the tree of life. This makes any single GO term derived from CARD18 biology inappropriate for family-wide propagation.

---

## 5. Over-Annotation Verdict

### 5.1 Current Mapping Status: Sound

The current state of **no InterPro2GO terms** for PTHR47901 is **correct and should be maintained**. The absence of mappings accurately reflects the impossibility of assigning any GO term that would be true for all proteins matched by this signature.

### 5.2 Recommended GO Action Pattern

| Action | Recommendation |
|---|---|
| **Current no-mapping status** | **ACCEPT** — maintain no InterPro2GO terms |
| **Adding caspase inhibitor / inflammasome regulation terms** | **REJECT** — would over-annotate the vast majority of matched proteins |
| **Adding generic terms (protein binding, cytosol)** | **REJECT** — too uninformative and still not universally applicable |
| **Subfamily-level annotations** | **CONSIDER** — if PTHR47901 subfamilies correspond to true CARD18 primate orthologs, terms such as "negative regulation of caspase activity" (GO:0043154) or "regulation of inflammasome complex assembly" (GO:1900224) could be appropriate for those narrow subfamilies only |

### 5.3 Recommendation for InterPro

The PTHR47901 family appears to be over-inclusive, matching far more proteins than true CARD18 orthologs. Recommendations:

1. **No GO terms should be added at the PTHR47901 family level.** The current no-mapping state is appropriate.
2. **Subfamily-level review is warranted.** If any of the 5 subfamilies correspond specifically to experimentally validated CARD18 orthologs from primates, GO terms describing caspase-1 inhibition and inflammasome regulation could be added to those child entries.
3. **InterPro should review whether the PANTHER signature scope is appropriate.** The family named "CASPASE RECRUITMENT DOMAIN-CONTAINING PROTEIN 18" matching >4,000 non-primate taxa is misleading and may benefit from re-evaluation or re-naming to reflect its actual taxonomic and functional breadth.
4. **Overall verdict: ACCEPT current no-mapping; any future proposals to add terms should be MARK_AS_OVER_ANNOTATED unless restricted to a narrow, primate-specific child entry with experimental support.**

References

1. (devi2020anupdateon pages 7-9): Savita Devi, Christian Stehlik, and Andrea Dorfleutner. An update on card only proteins (cops) and pyd only proteins (pops) as inflammasome regulators. International Journal of Molecular Sciences, 21:6901, Sep 2020. URL: https://doi.org/10.3390/ijms21186901, doi:10.3390/ijms21186901. This article has 33 citations.

2. (matusiak2015card‐andpyrin‐only pages 4-6): Magdalena Matusiak, Nina Van Opdenbosch, and Mohamed Lamkanfi. Card‐ and pyrin‐only proteins regulating inflammasome activation and immunity. Immunological Reviews, 265:217-230, May 2015. URL: https://doi.org/10.1111/imr.12282, doi:10.1111/imr.12282. This article has 40 citations and is from a domain leading peer-reviewed journal.

3. (matusiak2015card‐andpyrin‐only pages 2-4): Magdalena Matusiak, Nina Van Opdenbosch, and Mohamed Lamkanfi. Card‐ and pyrin‐only proteins regulating inflammasome activation and immunity. Immunological Reviews, 265:217-230, May 2015. URL: https://doi.org/10.1111/imr.12282, doi:10.1111/imr.12282. This article has 40 citations and is from a domain leading peer-reviewed journal.

4. (hoss2017assemblyandregulation pages 10-11): Florian Hoss, Juan F. Rodriguez-Alcazar, and Eicke Latz. Assembly and regulation of asc specks. Cellular and Molecular Life Sciences, 74:1211-1229, Apr 2017. URL: https://doi.org/10.1007/s00018-016-2396-6, doi:10.1007/s00018-016-2396-6. This article has 190 citations and is from a domain leading peer-reviewed journal.

5. (jin2015activationandassembly pages 1-3): Tengchuan Jin and Tsan Sam Xiao. Activation and assembly of the inflammasomes through conserved protein domain families. Apoptosis, 20:151-156, Feb 2015. URL: https://doi.org/10.1007/s10495-014-1053-5, doi:10.1007/s10495-014-1053-5. This article has 24 citations and is from a peer-reviewed journal.

6. (park2019caspaserecruitmentdomains pages 4-6): H. H. Park. Caspase recruitment domains for protein interactions in cellular signaling (review). International Journal of Molecular Medicine, 43:1119-1127, Jan 2019. URL: https://doi.org/10.3892/ijmm.2019.4060, doi:10.3892/ijmm.2019.4060. This article has 53 citations and is from a peer-reviewed journal.

7. (park2019caspaserecruitmentdomains pages 3-4): H. H. Park. Caspase recruitment domains for protein interactions in cellular signaling (review). International Journal of Molecular Medicine, 43:1119-1127, Jan 2019. URL: https://doi.org/10.3892/ijmm.2019.4060, doi:10.3892/ijmm.2019.4060. This article has 53 citations and is from a peer-reviewed journal.

8. (matusiak2015card‐andpyrin‐only pages 6-7): Magdalena Matusiak, Nina Van Opdenbosch, and Mohamed Lamkanfi. Card‐ and pyrin‐only proteins regulating inflammasome activation and immunity. Immunological Reviews, 265:217-230, May 2015. URL: https://doi.org/10.1111/imr.12282, doi:10.1111/imr.12282. This article has 40 citations and is from a domain leading peer-reviewed journal.

9. (lu2016molecularbasisof pages 1-11): Alvin Lu, Yang Li, Florian I Schmidt, Qian Yin, Shuobing Chen, Tian-Min Fu, Alexander B Tong, Hidde L Ploegh, Youdong Mao, and Hao Wu. Molecular basis of caspase-1 polymerization and its inhibition by a new capping mechanism. Nature Structural &amp; Molecular Biology, 23:416-425, Apr 2016. URL: https://doi.org/10.1038/nsmb.3199, doi:10.1038/nsmb.3199. This article has 212 citations and is from a highest quality peer-reviewed journal.

10. (le2013pyrinandcardonly pages 4-5): Hongnga T. Le and Jonathan A. Harton. Pyrin- and card-only proteins as regulators of nlr functions. Frontiers in Immunology, Sep 2013. URL: https://doi.org/10.3389/fimmu.2013.00275, doi:10.3389/fimmu.2013.00275. This article has 104 citations and is from a peer-reviewed journal.

11. (le2013pyrinandcardonly pages 6-8): Hongnga T. Le and Jonathan A. Harton. Pyrin- and card-only proteins as regulators of nlr functions. Frontiers in Immunology, Sep 2013. URL: https://doi.org/10.3389/fimmu.2013.00275, doi:10.3389/fimmu.2013.00275. This article has 104 citations and is from a peer-reviewed journal.

12. (stevens2025largescalerestructuringof pages 1-4): David Stevens, Tasman Daish, and Frank Grützner. Large-scale restructuring of the caspase-1 gene cluster region in mammals. bioRxiv, Jun 2025. URL: https://doi.org/10.1101/2025.06.19.660630, doi:10.1101/2025.06.19.660630. This article has 0 citations.

13. (sharma2021structureactivationand pages 20-22): Meenakshi Sharma and Eva de Alba. Structure, activation and regulation of nlrp3 and aim2 inflammasomes. International Journal of Molecular Sciences, 22:872, Jan 2021. URL: https://doi.org/10.3390/ijms22020872, doi:10.3390/ijms22020872. This article has 197 citations.

14. (OpenTargets Search: -CARD18): Open Targets Query (-CARD18, 5 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

15. (stevens2025largescalerestructuringof pages 17-20): David Stevens, Tasman Daish, and Frank Grützner. Large-scale restructuring of the caspase-1 gene cluster region in mammals. bioRxiv, Jun 2025. URL: https://doi.org/10.1101/2025.06.19.660630, doi:10.1101/2025.06.19.660630. This article has 0 citations.

16. (park2019caspaserecruitmentdomains pages 1-3): H. H. Park. Caspase recruitment domains for protein interactions in cellular signaling (review). International Journal of Molecular Medicine, 43:1119-1127, Jan 2019. URL: https://doi.org/10.3892/ijmm.2019.4060, doi:10.3892/ijmm.2019.4060. This article has 53 citations and is from a peer-reviewed journal.

17. (hong2002caspaserecruitmentdomain pages 1-3): Gil-Sun Hong and Yong-Keun Jung. Caspase recruitment domain (card) as a bi-functional switch of caspase regulation and nf-kappab signals. Journal of biochemistry and molecular biology, 35 1:19-23, Jan 2002. URL: https://doi.org/10.5483/bmbrep.2002.35.1.019, doi:10.5483/bmbrep.2002.35.1.019. This article has 45 citations.

18. (stevens2025largescalerestructuringof pages 4-7): David Stevens, Tasman Daish, and Frank Grützner. Large-scale restructuring of the caspase-1 gene cluster region in mammals. bioRxiv, Jun 2025. URL: https://doi.org/10.1101/2025.06.19.660630, doi:10.1101/2025.06.19.660630. This article has 0 citations.

19. (stevens2025largescalerestructuringof pages 14-17): David Stevens, Tasman Daish, and Frank Grützner. Large-scale restructuring of the caspase-1 gene cluster region in mammals. bioRxiv, Jun 2025. URL: https://doi.org/10.1101/2025.06.19.660630, doi:10.1101/2025.06.19.660630. This article has 0 citations.

## Artifacts

- [Edison artifact artifact-00](PTHR47901-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR47901-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. devi2020anupdateon pages 7-9
2. lu2016molecularbasisof pages 1-11
3. le2013pyrinandcardonly pages 4-5
4. le2013pyrinandcardonly pages 6-8
5. stevens2025largescalerestructuringof pages 17-20
6. hoss2017assemblyandregulation pages 10-11
7. jin2015activationandassembly pages 1-3
8. park2019caspaserecruitmentdomains pages 4-6
9. park2019caspaserecruitmentdomains pages 3-4
10. stevens2025largescalerestructuringof pages 1-4
11. sharma2021structureactivationand pages 20-22
12. park2019caspaserecruitmentdomains pages 1-3
13. hong2002caspaserecruitmentdomain pages 1-3
14. stevens2025largescalerestructuringof pages 4-7
15. stevens2025largescalerestructuringof pages 14-17
16. https://doi.org/10.3390/ijms21186901,
17. https://doi.org/10.1111/imr.12282,
18. https://doi.org/10.1007/s00018-016-2396-6,
19. https://doi.org/10.1007/s10495-014-1053-5,
20. https://doi.org/10.3892/ijmm.2019.4060,
21. https://doi.org/10.1038/nsmb.3199,
22. https://doi.org/10.3389/fimmu.2013.00275,
23. https://doi.org/10.1101/2025.06.19.660630,
24. https://doi.org/10.3390/ijms22020872,
25. https://doi.org/10.5483/bmbrep.2002.35.1.019,