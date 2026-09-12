---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T20:17:29.439923'
end_time: '2026-06-28T20:31:47.500205'
duration_seconds: 858.06
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR11801
  interpro_name: SIGNAL TRANSDUCER AND ACTIVATOR OF TRANSCRIPTION
  interpro_short_name: Not specified
  interpro_type: family
  interpro_integrated: IPR001217
  member_databases: Not specified
  n_proteins: '12874'
  n_taxa: '5262'
  n_subfamilies: '14'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: Not specified in InterPro
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 35
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR11801-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR11801-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** PTHR11801
- **Name:** SIGNAL TRANSDUCER AND ACTIVATOR OF TRANSCRIPTION
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR001217
- **Member database signatures:** Not specified
- **Scale:** 12874 proteins across 5262 taxa, 14 subfamilies
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
**PTHR11801 (SIGNAL TRANSDUCER AND ACTIVATOR OF TRANSCRIPTION)**, structured to support GO annotation review.

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
- **Accession:** PTHR11801
- **Name:** SIGNAL TRANSDUCER AND ACTIVATOR OF TRANSCRIPTION
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR001217
- **Member database signatures:** Not specified
- **Scale:** 12874 proteins across 5262 taxa, 14 subfamilies
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
**PTHR11801 (SIGNAL TRANSDUCER AND ACTIVATOR OF TRANSCRIPTION)**, structured to support GO annotation review.

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


# Comprehensive Research Report: PTHR11801 — Signal Transducer and Activator of Transcription (STAT) Family

## InterPro Entry Summary

PTHR11801 is a PANTHER family-level InterPro entry representing the **Signal Transducer and Activator of Transcription (STAT)** protein family. It encompasses 12,874 proteins across 5,262 taxa, organized into 14 subfamilies, and is integrated into the parent entry IPR001217. Notably, **no InterPro2GO terms are currently mapped** to this entry. This report evaluates the family's biochemistry, functional divergence, taxonomic scope, and the appropriateness of the current (absent) InterPro2GO mapping status.

---

## 1. Family Definition and Biochemistry

### Domain Architecture

STAT proteins share a highly conserved multi-domain architecture consisting of six functional domains: (i) an **N-terminal domain (NTD)** involved in dimer–dimer (tetramer) contacts and cooperative DNA binding; (ii) a **coiled-coil domain (CCD)** that mediates protein–protein interactions and receptor recruitment; (iii) a **DNA-binding domain (DBD)** that forms a C-shaped clamp structure recognizing GAS (gamma-activated sequence) and ISRE (interferon-stimulated response element) DNA motifs; (iv) an **α-helical linker domain (LD)** connecting the DBD and SH2 domain; (v) a **Src Homology 2 (SH2) domain**, the most conserved region across the family, which mediates phosphotyrosine recognition and reciprocal dimerization; and (vi) a **C-terminal transactivation domain (TAD)** harboring the critical tyrosine and serine phosphorylation sites (butturini2020redoxregulationof pages 1-3, philips2022thejakstatpathway pages 6-7, diallo2022theroleof pages 1-2, wedeking2024genericmicropatternedpulldown pages 21-24).

### Conserved Residues and Activation Mechanism

The hallmark of STAT activation is phosphorylation of a conserved C-terminal tyrosine residue by Janus kinases (JAKs) or, in some contexts, Src-family kinases. The specific tyrosine positions are: STAT1-Y701, STAT2-Y690, STAT3-Y705, STAT4-Y693, STAT5-Y694, and STAT6-Y641 (philips2022thejakstatpathway pages 6-7). Phosphorylation of this tyrosine on one monomer enables reciprocal binding to the SH2 domain of another monomer, triggering the formation of parallel homodimers or heterodimers that translocate to the nucleus and bind DNA (butturini2020redoxregulationof pages 1-3, philips2022thejakstatpathway pages 6-7, corry2020activationofstat pages 1-3). The SH2 domain contains critical arginine residues in the phosphotyrosine-binding pocket (Arg602 in STAT1, Arg609 in STAT3) that coordinate the phosphate group (butturini2020redoxregulationof pages 1-3). Additional regulatory residues include serine phosphorylation sites (e.g., S727 in STAT3) in the TAD and conserved residues like D170 in the CCD of STAT3 that mediate allosteric interdomain communication (suleman2024probingthedepths pages 2-3, diallo2022theroleof pages 2-4, zhao2022allostericregulationin pages 1-3).

### Structural Fold

STAT proteins adopt two principal conformational states: an antiparallel dimer conformation in the unphosphorylated (latent) state, where CCD–CCD interactions predominate and the DBD cannot contact DNA; and a parallel dimer conformation upon tyrosine phosphorylation, where the SH2-pY interactions reorient the dimer to enable DNA binding (philips2022thejakstatpathway pages 28-34). STATs are unique among transcription factors as the only family containing an SH2 domain (diallo2022theroleof pages 1-2). Crystal structures have been resolved for parallel homodimers bound to DNA for STAT1, STAT3, and STAT6, and antiparallel conformations for STAT3 and STAT5a (philips2022thejakstatpathway pages 28-34).

---

## 2. InterPro2GO Mapping Appropriateness

Since **no GO terms are currently mapped** to PTHR11801, this section evaluates whether GO terms *should* be added, and what risks each candidate term would pose. The following table provides a systematic assessment of plausible GO term candidates:

| Candidate GO term | GO ID (approximate) | Applicability across family | Risk of over-annotation | Recommendation | Notes |
|---|---|---|---|---|---|
| DNA binding | GO:0003677 | Most | Medium | MODIFY | DNA-binding domains are conserved across metazoan STATs and Dictyostelium STATs, supporting sequence-specific DNA interaction as a broad family property; however, the generic term is weakly informative, and a more specific transcription-regulatory DNA-binding term would be preferable if supported by InterPro2GO policy. Conserved, low-level family-wide function, but not very specific (philips2022thejakstatpathway pages 6-7, diallo2022theroleof pages 1-2, song2023theroleof pages 3-4, wang2012comparativeevolutionarygenomics pages 3-6). |
| Transcription factor activity | GO:0003700 | Most | Medium | MODIFY | Canonical STAT proteins are transcription factors that dimerize, translocate to the nucleus, bind DNA, and regulate target genes; however, family members are functionally divergent, some have strong non-canonical roles, and Dictyostelium STATs lack some higher-eukaryote domains, so this should be mapped only if using a carefully chosen DNA-binding transcription regulator term rather than an over-broad legacy term (philips2022thejakstatpathway pages 3-4, song2023theroleof pages 3-4, philips2022thejakstatpathway pages 4-6, wang2012comparativeevolutionarygenomics pages 3-6). |
| Protein dimerization activity | GO:0046983 | Most | Low | ACCEPT | SH2-mediated reciprocal phosphotyrosine-dependent dimerization is a core mechanistic property of STAT activation across the family, and unphosphorylated dimer states also occur in multiple STATs. This is a mechanistic molecular-function-like property broadly supported across STAT proteins and less taxon-restricted than pathway/process terms (butturini2020redoxregulationof pages 1-3, philips2022thejakstatpathway pages 6-7, philips2022thejakstatpathway pages 28-34, corry2020activationofstat pages 1-3). |
| JAK-STAT cascade | GO:0007259 | Some | High | REJECT | Appropriate for many vertebrate STATs but not for all proteins matched by this family because Dictyostelium STATs and likely other non-vertebrate members are not part of canonical cytokine receptor/JAK signaling. This would leak a vertebrate pathway term across a broader evolutionary family (wang2012comparativeevolutionarygenomics pages 1-2, wang2012comparativeevolutionarygenomics pages 8-9, wang2012comparativeevolutionarygenomics pages 3-6). |
| Cytokine-mediated signaling pathway | GO:0019221 | Some | High | REJECT | Many vertebrate STATs are activated downstream of cytokines, but this is not a family-wide property across all taxa represented in PTHR11801. It would over-annotate non-vertebrate and Dictyostelium members and collapse substantial subfamily specialization into an over-broad process term (philips2022thejakstatpathway pages 3-4, song2023theroleof pages 3-4, philips2022thejakstatpathway pages 4-6, wang2012comparativeevolutionarygenomics pages 3-6). |
| Nucleus | GO:0005634 | Most | Medium | KEEP_AS_NON_CORE | Nuclear translocation is central to canonical STAT activity, and many family members function in the nucleus; however, this is a generic cellular component term and does not capture the family’s defining mechanism. Because STATs also have cytoplasmic and organellar non-canonical pools, nucleus is true but not especially informative as a core InterPro2GO mapping (philips2022thejakstatpathway pages 6-7, philips2022thejakstatpathway pages 21-22, philips2022thejakstatpathway pages 11-12). |
| Cytoplasm | GO:0005737 | Most | Medium | KEEP_AS_NON_CORE | Latent STAT proteins are commonly cytoplasmic prior to activation, but this is again a very generic localization term and not a defining family function. It is also complicated by nuclear shuttling and mitochondrial/non-canonical localization, so it adds little value as a core mapping (philips2022thejakstatpathway pages 6-7, philips2022thejakstatpathway pages 11-12, corry2020activationofstat pages 1-3). |
| Phosphotyrosine binding | GO:0001784 | Most | Low | ACCEPT | The SH2 domain is a hallmark of STAT proteins and mediates phosphotyrosine recognition on receptors and partner STAT molecules during activation and dimerization. This is a strong mechanistic family-level property that is better conserved across taxa than vertebrate-specific pathway/process terms (butturini2020redoxregulationof pages 1-3, philips2022thejakstatpathway pages 6-7, diallo2022theroleof pages 1-2, corry2020activationofstat pages 1-3). |


*Table: This table evaluates plausible GO terms for InterPro entry PTHR11801 (STAT family) and highlights which are family-wide enough to support InterPro2GO mapping. It is useful for distinguishing conserved mechanistic functions from vertebrate-specific pathway/process annotations that would over-annotate the family.*

### Key Findings

**Terms that could reasonably be mapped at the family level:** Phosphotyrosine binding (GO:0001784) and protein dimerization activity (GO:0046983) are core mechanistic properties of all STAT proteins — the SH2 domain and reciprocal pY-SH2 dimerization are the defining features of this family (butturini2020redoxregulationof pages 1-3, philips2022thejakstatpathway pages 6-7, corry2020activationofstat pages 1-3). These are molecular function terms that describe the inherent biochemistry of every family member.

**Terms requiring modification if mapped:** DNA binding and transcription factor activity are broadly conserved but would benefit from use of the most appropriate specific terms (e.g., "DNA-binding transcription factor activity, RNA polymerase II-specific" or "sequence-specific DNA binding"), and even then caution is warranted because Dictyostelium STATs lack N-terminal and transactivation domains (wang2012comparativeevolutionarygenomics pages 3-6).

**Terms that should NOT be mapped at the family level:** JAK-STAT cascade (GO:0007259) and cytokine-mediated signaling pathway (GO:0019221) are vertebrate-centric process terms. Dictyostelium STATs (which share <10% sequence identity with mammalian STATs) do not participate in canonical JAK-STAT or cytokine signaling, and invertebrate STATs have variable pathway contexts (wang2012comparativeevolutionarygenomics pages 1-2, wang2012comparativeevolutionarygenomics pages 8-9, wang2012comparativeevolutionarygenomics pages 3-6). Mapping these terms at the PTHR11801 level would systematically over-annotate non-vertebrate members.

---

## 3. Functional Divergence Across the Family

The STAT family exhibits profound functional divergence among its subfamilies, with individual STAT members mediating distinct — and sometimes opposing — biological outcomes. The following table summarizes the key distinctions:

| STAT subfamily member | Primary activating cytokines / stimuli | Key biological role | Unique / distinctive functions | Conserved tyrosine phosphorylation site | Non-canonical roles |
|---|---|---|---|---|---|
| STAT1 | Type I, II, and III interferons; also activated in some contexts by IL-27 and other cytokines (philips2022thejakstatpathway pages 3-4, philips2022thejakstatpathway pages 6-7) | Antiviral defense, immune regulation, induction of apoptosis-associated programs, IFN-responsive transcription (song2023theroleof pages 2-3, song2023theroleof pages 3-4, philips2022thejakstatpathway pages 3-4) | Forms homodimers for IFN-γ responses and heterodimers with STAT2 plus IRF9 in ISGF3; often functionally opposes STAT3 in inflammatory/survival balance (philips2022thejakstatpathway pages 6-7, philips2022thejakstatpathway pages 3-4) | Y701 (philips2022thejakstatpathway pages 6-7, butturini2020redoxregulationof pages 1-3) | Unphosphorylated STAT1 supports constitutive transcription with IRF1, can modify chromatin/3D genome structure, and U-STAT1:U-STAT2 dimers can inhibit STAT1 signaling in IFN-independent contexts (philips2022thejakstatpathway pages 6-7, philips2022thejakstatpathway pages 21-22, philips2022thejakstatpathway pages 18-19) |
| STAT2 | Type I interferons (IFN-α/β); also involved in some type III IFN signaling complexes (song2023theroleof pages 3-4, philips2022thejakstatpathway pages 3-4) | Specialized interferon signal transduction, especially antiviral gene induction through ISGF3 (philips2022thejakstatpathway pages 6-7, philips2022thejakstatpathway pages 3-4) | Distinct from other STATs in being best known as a heterodimeric/complex-forming STAT with STAT1 and IRF9 rather than as a classic homodimeric effector; contributes to antiviral specificity (philips2022thejakstatpathway pages 6-7, philips2022thejakstatpathway pages 3-4) | Y690 (philips2022thejakstatpathway pages 6-7) | U-STAT2 with IRF9 can drive basal ISG expression; T404-phosphorylated U-STAT2 binds STING and inhibits STING-mediated IFN production; also reported to affect mitochondrial shape in some systems (philips2022thejakstatpathway pages 6-7, philips2022thejakstatpathway pages 7-9, song2023theroleof pages 3-4) |
| STAT3 | IL-6 family cytokines; EGF and other growth factors; also can be activated by Rho-family GTPase-linked pathways (philips2022thejakstatpathway pages 3-4, corry2020activationofstat pages 1-3) | Cell growth, survival, acute-phase responses, immune regulation, oxidative stress responses; often pro-survival/oncogenic (song2023theroleof pages 3-4, philips2022thejakstatpathway pages 3-4) | Acts as a major integrator of cytokine and growth-factor signaling; frequently contrasted with STAT1 because of anti-apoptotic and tumor-promoting functions; can heterodimerize with STAT1 (song2023theroleof pages 3-4, philips2022thejakstatpathway pages 3-4) | Y705 (philips2022thejakstatpathway pages 6-7, diallo2022theroleof pages 2-4, zhao2022allostericregulationin pages 1-3) | Mitochondrial STAT3 promotes oxidative phosphorylation, redox balance, respiration, and mitochondrial transcription; U-STAT3 cooperates with NF-κB in gene regulation (e.g., RANTES) independently of canonical activation (villarino2023transcriptionalprogramingof pages 6-6, philips2022thejakstatpathway pages 6-7, philips2022thejakstatpathway pages 11-12) |
| STAT4 | IL-12, IL-23, and type I interferons (philips2022thejakstatpathway pages 3-4) | Lymphoid-biased immune signaling, especially Th1-related differentiation and inflammatory immune programming (song2023theroleof pages 2-3, philips2022thejakstatpathway pages 3-4) | More restricted expression pattern than several other STATs; associated with Th1/Th2 balance and reduction of neurotoxic effects in one reviewed context (song2023theroleof pages 2-3, philips2022thejakstatpathway pages 3-4) | Y693 (philips2022thejakstatpathway pages 6-7) | No well-established family-wide non-canonical role highlighted in the gathered evidence; evidence base is much thinner here than for STAT1/2/3/5/6 (philips2022thejakstatpathway pages 3-4) |
| STAT5A | IL-2, IL-3, GM-CSF, IL-5, and related cytokines/hormonal inputs (philips2022thejakstatpathway pages 3-4) | Hematopoietic and cytokine-responsive transcription; growth and differentiation control (philips2022thejakstatpathway pages 3-4) | Historically linked to mammary gland biology; part of the highly homologous STAT5 pair, with overlapping but not fully identical biology to STAT5B (philips2022thejakstatpathway pages 3-4, wang2012comparativeevolutionarygenomics pages 1-2) | Y694 for STAT5 proteins (family-level evidence does not always separate A vs B) (philips2022thejakstatpathway pages 6-7) | Anti-parallel latent dimers described for STAT5a; unphosphorylated STAT5 family proteins can contribute to chromatin repression/heterochromatin-linked tumor suppressor functions (philips2022thejakstatpathway pages 28-34, philips2022thejakstatpathway pages 6-7, philips2022thejakstatpathway pages 11-12) |
| STAT5B | IL-2, IL-3, GM-CSF, IL-5, and related cytokines/hormonal inputs (philips2022thejakstatpathway pages 3-4) | Hematopoietic, lymphocyte, and cytokine-driven transcriptional regulation (philips2022thejakstatpathway pages 3-4) | Essential in lymphocyte biology and immune gene programs; diverged from STAT5A by gene duplication in mammals and shows overlapping but distinguishable physiological roles (wang2012comparativeevolutionarygenomics pages 1-2, philips2022thejakstatpathway pages 3-4) | Y694 for STAT5 proteins (family-level evidence does not always separate A vs B) (philips2022thejakstatpathway pages 6-7) | U-STAT5 can repress oncogenes via heterochromatin formation; a fraction of STAT5 also localizes to mitochondria in non-canonical contexts (philips2022thejakstatpathway pages 6-7, philips2022thejakstatpathway pages 11-12) |
| STAT6 | IL-4 and IL-13 (song2023theroleof pages 2-3, song2023theroleof pages 3-4, philips2022thejakstatpathway pages 3-4) | Th2-associated transcriptional programming, alternative macrophage polarization, and allergic/inflammatory signaling (song2023theroleof pages 2-3, song2023theroleof pages 3-4, philips2022thejakstatpathway pages 3-4) | Strongly linked to Th2 proliferation and M2 macrophage conversion; functionally distinct from STAT4/STAT1 axes in helper T-cell polarization (song2023theroleof pages 2-3, song2023theroleof pages 3-4) | Y641 (philips2022thejakstatpathway pages 6-7) | U-STAT6 can associate with p300 and drive COX-2 expression; latent interaction repertoire appears distinctive relative to other STATs (philips2022thejakstatpathway pages 6-7) |
| Dictyostelium STATs (dstA-dstD / STATa-d) | Developmental phosphotyrosine signaling in slime molds; not canonical vertebrate cytokine/JAK activation (wang2012comparativeevolutionarygenomics pages 3-6, wang2012comparativeevolutionarygenomics pages 8-9) | Ancient STAT-like transcriptional regulators in Dictyostelium; evidence supports participation in SH2-mediated phosphotyrosine signaling rather than vertebrate-style cytokine immunity (wang2012comparativeevolutionarygenomics pages 3-6) | Form a distinct clade with <10% identity to mammalian STATs; retain DNA-binding and SH2 domains plus phosphotyrosine sites, but lack the N-terminal and transactivation domains typical of higher-organism STATs, indicating major structural and functional divergence (wang2012comparativeevolutionarygenomics pages 3-6) | Conserved phosphotyrosine site present, but residue-equivalent positions to vertebrate Y701/Y705-family sites were not specified in the gathered evidence (wang2012comparativeevolutionarygenomics pages 3-6) | No specific non-canonical roles were defined in the gathered evidence; their major relevance here is that they demonstrate deep evolutionary divergence and caution against over-generalizing vertebrate JAK-STAT/cytokine functions across the entire family (wang2012comparativeevolutionarygenomics pages 3-6, wang2012comparativeevolutionarygenomics pages 8-9) |


*Table: This table summarizes the major functional specializations, activating stimuli, conserved tyrosine sites, and non-canonical behaviors across STAT family subgroups, including the divergent Dictyostelium STATs. It is useful for evaluating whether any single GO term could accurately apply to every member matched by the broad PTHR11801 family signature.*

### Neo-functionalization

Extensive neo-functionalization has occurred within the STAT family. The most striking example is the antagonistic relationship between **STAT1 and STAT3**: STAT1 generally promotes apoptosis and anti-inflammatory responses via interferon signaling, while STAT3 promotes cell survival, proliferation, and anti-apoptotic programs downstream of IL-6 family cytokines and growth factors (song2023theroleof pages 2-3, song2023theroleof pages 3-4, philips2022thejakstatpathway pages 6-7). This functional opposition reflects evolutionary divergence from a common ancestral stat1/stat3 gene. Similarly, STAT4 and STAT6 drive opposing T-helper cell polarization programs (Th1 vs. Th2, respectively) (song2023theroleof pages 2-3, philips2022thejakstatpathway pages 3-4). STAT5A and STAT5B arose from a relatively recent gene duplication in early eutherians (~130–310 Mya) and show overlapping but distinguishable physiological roles in mammary gland biology vs. lymphocyte function (wang2012comparativeevolutionarygenomics pages 1-2, wang2012comparativeevolutionarygenomics pages 6-8, philips2022thejakstatpathway pages 3-4).

### Non-Canonical and Transcription-Independent Roles

A significant fraction of STAT biology involves functions outside the canonical phosphorylation-dimerization-nuclear translocation-transcription paradigm:

- **Mitochondrial STAT3 (mitoSTAT3):** A 5–10% fraction of STAT3 localizes to mitochondria, where serine-phosphorylated (but not necessarily tyrosine-phosphorylated) STAT3 promotes oxidative phosphorylation, redox homeostasis, and mitochondrial genome transcription by interacting with electron transport chain components, pyruvate dehydrogenase complex E1, and cyclophilin D (villarino2023transcriptionalprogramingof pages 6-6, philips2022thejakstatpathway pages 11-12). STAT5 may also localize to mitochondria in non-canonical contexts (philips2022thejakstatpathway pages 11-12).

- **Unphosphorylated STAT (U-STAT) functions:** U-STAT3 cooperates with NF-κB to regulate RANTES expression; U-STAT5 represses oncogenes via heterochromatin formation; U-STAT6 associates with p300 to drive COX-2 expression; U-STAT2:IRF9 complexes drive basal interferon-stimulated gene expression; and U-STAT1:U-STAT2 dimers inhibit STAT1 function in an interferon-independent manner (philips2022thejakstatpathway pages 6-7, philips2022thejakstatpathway pages 21-22, philips2022thejakstatpathway pages 7-9, philips2022thejakstatpathway pages 18-19).

- **Chromatin and 3D genome remodeling:** Unphosphorylated STAT1 modifies chromatin structure and the three-dimensional genome organization (philips2022thejakstatpathway pages 18-19).

### Pseudo-Enzymes

STAT proteins are not enzymes (they are transcription factors), so the concept of "catalytically dead" members is not directly applicable in the enzymatic sense. However, all STAT family members appear to retain their core domain architecture and functional capacity for DNA binding and dimerization, with no well-documented "dead" STAT members that completely lack transcriptional potential identified in the current literature.

---

## 4. Taxonomic Scope

PTHR11801 spans an exceptionally broad evolutionary range (5,262 taxa), reflecting the ancient origins and subsequent diversification of STAT proteins.

**Dictyostelium (Amoebozoa):** The slime mold *Dictyostelium discoideum* possesses four STAT-like genes (dstA–dstD/STATa–d) that form a distinct evolutionary clade with <10% sequence identity to mammalian STATs, though they share 22–38% identity with each other. Dictyostelium STATs contain DNA-binding and SH2 domains plus tyrosine phosphorylation sites but **lack the N-terminal and transactivation domains** characteristic of metazoan STATs, indicating domain accretion occurred later (wang2012comparativeevolutionarygenomics pages 8-9, wang2012comparativeevolutionarygenomics pages 3-6). These organisms do not have canonical cytokine signaling or JAK-STAT pathways in the vertebrate sense.

**Invertebrates:** Lower invertebrates generally possess one or two STAT genes. *C. elegans* has a single stat gene (sta-1), while *Drosophila* and *Apis* have one stat gene each. *Anopheles* has two. Insect STATs achieved the complete six-domain architecture identical to mammalian STATs before deuterostome divergence over a billion years ago (wang2012comparativeevolutionarygenomics pages 1-2, wang2012comparativeevolutionarygenomics pages 3-6, wang2012comparativeevolutionarygenomics pages 11-11). Basal deuterostomes such as echinoderms retain a single STAT, most similar to mammalian STAT5 (wang2012comparativeevolutionarygenomics pages 8-9, wang2012comparativeevolutionarygenomics pages 6-8).

**Vertebrates:** Two rounds of whole genome duplication in ancestral vertebrates (before ~450 Mya) expanded the family from one to six core members (STAT1–4, STAT5, STAT6), organized in three chromosomal clusters. A subsequent duplication in early eutherians produced STAT5A and STAT5B (wang2012comparativeevolutionarygenomics pages 1-2, wang2012comparativeevolutionarygenomics pages 6-8, wang2012comparativeevolutionarygenomics pages 9-10, wang2012comparativeevolutionarygenomics pages 2-3). Birds possess five STATs (STAT1, 3, 4, 5, 6), while mammals have seven. Teleost fish underwent an additional whole genome duplication but subsequently lost most duplicated stat genes (wang2012comparativeevolutionarygenomics pages 6-8, wang2012comparativeevolutionarygenomics pages 9-10).

**Taxonomic implications for GO mapping:** Any process/pathway term mapped to this family must hold across the entire evolutionary spectrum, from Dictyostelium to mammals. Terms like "JAK-STAT cascade" or "cytokine-mediated signaling" are inappropriate at this level because they describe vertebrate-specific pathway biology that does not apply to Dictyostelium or many invertebrate members (wang2012comparativeevolutionarygenomics pages 8-9, wang2012comparativeevolutionarygenomics pages 3-6).

---

## 5. Over-Annotation Verdict

### Current Status Assessment

The current absence of InterPro2GO mappings for PTHR11801 is **largely appropriate and reflects sound curatorial judgment**, given:

1. **Extreme functional divergence:** The seven mammalian STAT subfamily members serve distinct and sometimes opposing biological roles (e.g., STAT1 vs. STAT3 in apoptosis/survival; STAT4 vs. STAT6 in Th1/Th2 polarization) (song2023theroleof pages 2-3, song2023theroleof pages 3-4, philips2022thejakstatpathway pages 6-7, philips2022thejakstatpathway pages 3-4).

2. **Taxonomic breadth:** The family spans from Dictyostelium (amoebozoa) to mammals, and Dictyostelium members lack N-terminal and transactivation domains and do not participate in canonical JAK-STAT or cytokine signaling (wang2012comparativeevolutionarygenomics pages 8-9, wang2012comparativeevolutionarygenomics pages 3-6).

3. **Non-canonical functions:** Multiple STAT members have transcription-independent roles in mitochondria, chromatin remodeling, and protein–protein interactions that would not be captured by standard transcription-factor GO terms (villarino2023transcriptionalprogramingof pages 6-6, philips2022thejakstatpathway pages 6-7, philips2022thejakstatpathway pages 11-12, philips2022thejakstatpathway pages 18-19).

### Recommendation

**Overall verdict: ACCEPT the current absence of InterPro2GO mappings, with minor suggestions.**

The recommended GO action pattern is: **ACCEPT** (the current state of no mapped terms is not over-annotating).

However, if InterPro curators wish to add minimally informative family-level annotations, two molecular function terms could be considered for addition at the PTHR11801 level with low risk:

- **Phosphotyrosine binding** (GO:0001784) — the SH2-mediated phosphotyrosine recognition is the defining biochemical property of this family across all known members.
- **Protein dimerization activity** (GO:0046983) — SH2-mediated reciprocal dimerization is mechanistically conserved across the family.

**Terms that should NOT be added at this level but could be mapped to PANTHER subfamily entries:** JAK-STAT cascade, cytokine-mediated signaling, specific immune response terms, and detailed biological process terms should be reserved for the 14 individual subfamilies where they are taxonomically and functionally appropriate.

**Recommendation for InterPro itself:** Consider leveraging the 14 PANTHER subfamilies within PTHR11801 to assign more specific GO terms at the subfamily level (e.g., STAT1 subfamily → "type I interferon signaling pathway"; STAT3 subfamily → "acute-phase response"; STAT6 subfamily → "interleukin-4-mediated signaling pathway"). This would allow functionally appropriate GO annotations while avoiding the over-annotation risks inherent in mapping process terms to the broad parent family entry.

References

1. (butturini2020redoxregulationof pages 1-3): Elena Butturini, Alessandra Carcereri de Prati, and Sofia Mariotto. Redox regulation of stat1 and stat3 signaling. International Journal of Molecular Sciences, 21:7034, Sep 2020. URL: https://doi.org/10.3390/ijms21197034, doi:10.3390/ijms21197034. This article has 219 citations.

2. (philips2022thejakstatpathway pages 6-7): Rachael L. Philips, Yuxin Wang, HyeonJoo Cheon, Yuka Kanno, Massimo Gadina, Vittorio Sartorelli, Curt M. Horvath, James E. Darnell, George R. Stark, and John J. O’Shea. The jak-stat pathway at 30: much learned, much more to do. Cell, 185:3857-3876, Oct 2022. URL: https://doi.org/10.1016/j.cell.2022.09.023, doi:10.1016/j.cell.2022.09.023. This article has 730 citations and is from a highest quality peer-reviewed journal.

3. (diallo2022theroleof pages 1-2): Mickael Diallo and Federico Herrera. The role of understudied post‐translational modifications for the behavior and function of signal transducer and activator of transcription 3. The FEBS Journal, 289:6235-6255, Jul 2022. URL: https://doi.org/10.1111/febs.16116, doi:10.1111/febs.16116. This article has 37 citations.

4. (wedeking2024genericmicropatternedpulldown pages 21-24): Tim Wedeking. Generic micropatterned pull-down assays for quantifying interaction dynamics and stoichiometry of protein-protein interactions. Text, Feb 2024. URL: https://doi.org/10.48693/505, doi:10.48693/505. This article has 0 citations and is from a peer-reviewed journal.

5. (corry2020activationofstat pages 1-3): Jessica Corry, Helen R. Mott, and Darerca Owen. Activation of stat transcription factors by the rho-family gtpases. Biochemical Society Transactions, 48:2213-2227, Sep 2020. URL: https://doi.org/10.1042/bst20200468, doi:10.1042/bst20200468. This article has 37 citations and is from a peer-reviewed journal.

6. (suleman2024probingthedepths pages 2-3): Muhammad Suleman, Safir Ullah Khan, Shahid Ali, Abdullah Alghamdi, Mohammed Alissa, Rayan Y. Mushtaq, and Sergio Crovella. Probing the depths of molecular complexity: stat3 as a key architect in colorectal cancer pathogenesis. Current gene therapy, Oct 2025. URL: https://doi.org/10.2174/0115665232336447241010094744, doi:10.2174/0115665232336447241010094744. This article has 6 citations and is from a peer-reviewed journal.

7. (diallo2022theroleof pages 2-4): Mickael Diallo and Federico Herrera. The role of understudied post‐translational modifications for the behavior and function of signal transducer and activator of transcription 3. The FEBS Journal, 289:6235-6255, Jul 2022. URL: https://doi.org/10.1111/febs.16116, doi:10.1111/febs.16116. This article has 37 citations.

8. (zhao2022allostericregulationin pages 1-3): Tingting Zhao, Nischal Karki, Brian D. Zoltowski, and Devin A. Matthews. Allosteric regulation in stat3 interdomains is mediated by a rigid core: sh2 domain regulation by ccd in d170a variant. Dec 2022. URL: https://doi.org/10.1371/journal.pcbi.1010794, doi:10.1371/journal.pcbi.1010794. This article has 10 citations and is from a highest quality peer-reviewed journal.

9. (philips2022thejakstatpathway pages 28-34): Rachael L. Philips, Yuxin Wang, HyeonJoo Cheon, Yuka Kanno, Massimo Gadina, Vittorio Sartorelli, Curt M. Horvath, James E. Darnell, George R. Stark, and John J. O’Shea. The jak-stat pathway at 30: much learned, much more to do. Cell, 185:3857-3876, Oct 2022. URL: https://doi.org/10.1016/j.cell.2022.09.023, doi:10.1016/j.cell.2022.09.023. This article has 730 citations and is from a highest quality peer-reviewed journal.

10. (song2023theroleof pages 3-4): Tianzhi Song, Yishu Zhang, Liangrong Zhu, Yuyan Zhang, and Jingmei Song. The role of jak/stat signaling pathway in cerebral ischemia-reperfusion injury and the therapeutic effect of traditional chinese medicine: a narrative review. Medicine, 102:e35890, Nov 2023. URL: https://doi.org/10.1097/md.0000000000035890, doi:10.1097/md.0000000000035890. This article has 27 citations and is from a peer-reviewed journal.

11. (wang2012comparativeevolutionarygenomics pages 3-6): Yaming Wang and David E. Levy. Comparative evolutionary genomics of the stat family of transcription factors. JAK-STAT, 1:23-33, Jan 2012. URL: https://doi.org/10.4161/jkst.19418, doi:10.4161/jkst.19418. This article has 90 citations.

12. (philips2022thejakstatpathway pages 3-4): Rachael L. Philips, Yuxin Wang, HyeonJoo Cheon, Yuka Kanno, Massimo Gadina, Vittorio Sartorelli, Curt M. Horvath, James E. Darnell, George R. Stark, and John J. O’Shea. The jak-stat pathway at 30: much learned, much more to do. Cell, 185:3857-3876, Oct 2022. URL: https://doi.org/10.1016/j.cell.2022.09.023, doi:10.1016/j.cell.2022.09.023. This article has 730 citations and is from a highest quality peer-reviewed journal.

13. (philips2022thejakstatpathway pages 4-6): Rachael L. Philips, Yuxin Wang, HyeonJoo Cheon, Yuka Kanno, Massimo Gadina, Vittorio Sartorelli, Curt M. Horvath, James E. Darnell, George R. Stark, and John J. O’Shea. The jak-stat pathway at 30: much learned, much more to do. Cell, 185:3857-3876, Oct 2022. URL: https://doi.org/10.1016/j.cell.2022.09.023, doi:10.1016/j.cell.2022.09.023. This article has 730 citations and is from a highest quality peer-reviewed journal.

14. (wang2012comparativeevolutionarygenomics pages 1-2): Yaming Wang and David E. Levy. Comparative evolutionary genomics of the stat family of transcription factors. JAK-STAT, 1:23-33, Jan 2012. URL: https://doi.org/10.4161/jkst.19418, doi:10.4161/jkst.19418. This article has 90 citations.

15. (wang2012comparativeevolutionarygenomics pages 8-9): Yaming Wang and David E. Levy. Comparative evolutionary genomics of the stat family of transcription factors. JAK-STAT, 1:23-33, Jan 2012. URL: https://doi.org/10.4161/jkst.19418, doi:10.4161/jkst.19418. This article has 90 citations.

16. (philips2022thejakstatpathway pages 21-22): Rachael L. Philips, Yuxin Wang, HyeonJoo Cheon, Yuka Kanno, Massimo Gadina, Vittorio Sartorelli, Curt M. Horvath, James E. Darnell, George R. Stark, and John J. O’Shea. The jak-stat pathway at 30: much learned, much more to do. Cell, 185:3857-3876, Oct 2022. URL: https://doi.org/10.1016/j.cell.2022.09.023, doi:10.1016/j.cell.2022.09.023. This article has 730 citations and is from a highest quality peer-reviewed journal.

17. (philips2022thejakstatpathway pages 11-12): Rachael L. Philips, Yuxin Wang, HyeonJoo Cheon, Yuka Kanno, Massimo Gadina, Vittorio Sartorelli, Curt M. Horvath, James E. Darnell, George R. Stark, and John J. O’Shea. The jak-stat pathway at 30: much learned, much more to do. Cell, 185:3857-3876, Oct 2022. URL: https://doi.org/10.1016/j.cell.2022.09.023, doi:10.1016/j.cell.2022.09.023. This article has 730 citations and is from a highest quality peer-reviewed journal.

18. (song2023theroleof pages 2-3): Tianzhi Song, Yishu Zhang, Liangrong Zhu, Yuyan Zhang, and Jingmei Song. The role of jak/stat signaling pathway in cerebral ischemia-reperfusion injury and the therapeutic effect of traditional chinese medicine: a narrative review. Medicine, 102:e35890, Nov 2023. URL: https://doi.org/10.1097/md.0000000000035890, doi:10.1097/md.0000000000035890. This article has 27 citations and is from a peer-reviewed journal.

19. (philips2022thejakstatpathway pages 18-19): Rachael L. Philips, Yuxin Wang, HyeonJoo Cheon, Yuka Kanno, Massimo Gadina, Vittorio Sartorelli, Curt M. Horvath, James E. Darnell, George R. Stark, and John J. O’Shea. The jak-stat pathway at 30: much learned, much more to do. Cell, 185:3857-3876, Oct 2022. URL: https://doi.org/10.1016/j.cell.2022.09.023, doi:10.1016/j.cell.2022.09.023. This article has 730 citations and is from a highest quality peer-reviewed journal.

20. (philips2022thejakstatpathway pages 7-9): Rachael L. Philips, Yuxin Wang, HyeonJoo Cheon, Yuka Kanno, Massimo Gadina, Vittorio Sartorelli, Curt M. Horvath, James E. Darnell, George R. Stark, and John J. O’Shea. The jak-stat pathway at 30: much learned, much more to do. Cell, 185:3857-3876, Oct 2022. URL: https://doi.org/10.1016/j.cell.2022.09.023, doi:10.1016/j.cell.2022.09.023. This article has 730 citations and is from a highest quality peer-reviewed journal.

21. (villarino2023transcriptionalprogramingof pages 6-6): Alejandro V. Villarino. Transcriptional programing of t cell metabolism by stat family transcription factors. European Journal of Immunology, Apr 2023. URL: https://doi.org/10.1002/eji.202048825, doi:10.1002/eji.202048825. This article has 20 citations and is from a peer-reviewed journal.

22. (wang2012comparativeevolutionarygenomics pages 6-8): Yaming Wang and David E. Levy. Comparative evolutionary genomics of the stat family of transcription factors. JAK-STAT, 1:23-33, Jan 2012. URL: https://doi.org/10.4161/jkst.19418, doi:10.4161/jkst.19418. This article has 90 citations.

23. (wang2012comparativeevolutionarygenomics pages 11-11): Yaming Wang and David E. Levy. Comparative evolutionary genomics of the stat family of transcription factors. JAK-STAT, 1:23-33, Jan 2012. URL: https://doi.org/10.4161/jkst.19418, doi:10.4161/jkst.19418. This article has 90 citations.

24. (wang2012comparativeevolutionarygenomics pages 9-10): Yaming Wang and David E. Levy. Comparative evolutionary genomics of the stat family of transcription factors. JAK-STAT, 1:23-33, Jan 2012. URL: https://doi.org/10.4161/jkst.19418, doi:10.4161/jkst.19418. This article has 90 citations.

25. (wang2012comparativeevolutionarygenomics pages 2-3): Yaming Wang and David E. Levy. Comparative evolutionary genomics of the stat family of transcription factors. JAK-STAT, 1:23-33, Jan 2012. URL: https://doi.org/10.4161/jkst.19418, doi:10.4161/jkst.19418. This article has 90 citations.

## Artifacts

- [Edison artifact artifact-00](PTHR11801-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR11801-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. philips2022thejakstatpathway pages 6-7
2. butturini2020redoxregulationof pages 1-3
3. philips2022thejakstatpathway pages 28-34
4. diallo2022theroleof pages 1-2
5. wang2012comparativeevolutionarygenomics pages 3-6
6. philips2022thejakstatpathway pages 3-4
7. philips2022thejakstatpathway pages 11-12
8. philips2022thejakstatpathway pages 18-19
9. wedeking2024genericmicropatternedpulldown pages 21-24
10. corry2020activationofstat pages 1-3
11. suleman2024probingthedepths pages 2-3
12. diallo2022theroleof pages 2-4
13. zhao2022allostericregulationin pages 1-3
14. song2023theroleof pages 3-4
15. philips2022thejakstatpathway pages 4-6
16. wang2012comparativeevolutionarygenomics pages 1-2
17. wang2012comparativeevolutionarygenomics pages 8-9
18. philips2022thejakstatpathway pages 21-22
19. song2023theroleof pages 2-3
20. philips2022thejakstatpathway pages 7-9
21. villarino2023transcriptionalprogramingof pages 6-6
22. wang2012comparativeevolutionarygenomics pages 6-8
23. wang2012comparativeevolutionarygenomics pages 11-11
24. wang2012comparativeevolutionarygenomics pages 9-10
25. wang2012comparativeevolutionarygenomics pages 2-3
26. https://doi.org/10.3390/ijms21197034,
27. https://doi.org/10.1016/j.cell.2022.09.023,
28. https://doi.org/10.1111/febs.16116,
29. https://doi.org/10.48693/505,
30. https://doi.org/10.1042/bst20200468,
31. https://doi.org/10.2174/0115665232336447241010094744,
32. https://doi.org/10.1371/journal.pcbi.1010794,
33. https://doi.org/10.1097/md.0000000000035890,
34. https://doi.org/10.4161/jkst.19418,
35. https://doi.org/10.1002/eji.202048825,