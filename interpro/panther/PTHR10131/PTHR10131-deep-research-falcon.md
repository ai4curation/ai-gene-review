---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T19:39:34.292994'
end_time: '2026-06-28T19:59:47.909680'
duration_seconds: 1213.62
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR10131
  interpro_name: TNF RECEPTOR ASSOCIATED FACTOR
  interpro_short_name: Not specified
  interpro_type: family
  interpro_integrated: None (top-level entry)
  member_databases: Not specified
  n_proteins: '17591'
  n_taxa: '8155'
  n_subfamilies: '29'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: Not specified in InterPro
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 33
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR10131-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR10131-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** PTHR10131
- **Name:** TNF RECEPTOR ASSOCIATED FACTOR
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** Not specified
- **Scale:** 17591 proteins across 8155 taxa, 29 subfamilies
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
**PTHR10131 (TNF RECEPTOR ASSOCIATED FACTOR)**, structured to support GO annotation review.

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
- **Accession:** PTHR10131
- **Name:** TNF RECEPTOR ASSOCIATED FACTOR
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** Not specified
- **Scale:** 17591 proteins across 8155 taxa, 29 subfamilies
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
**PTHR10131 (TNF RECEPTOR ASSOCIATED FACTOR)**, structured to support GO annotation review.

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


# Comprehensive Research Report: PTHR10131 — TNF Receptor Associated Factor (TRAF) Family

## InterPro Entry Overview and GO Annotation Review

**InterPro Accession:** PTHR10131  
**Name:** TNF RECEPTOR ASSOCIATED FACTOR  
**Entry Type:** Family  
**Scale:** 17,591 proteins across 8,155 taxa, 29 subfamilies  
**Current InterPro2GO Mappings:** None (no GO terms mapped)

---

## 1. Family Definition and Biochemistry

### 1.1 Domain Architecture

The TRAF (TNF Receptor-Associated Factor) family comprises cytoplasmic signaling adaptor proteins that function downstream of the TNF receptor superfamily (TNFRSF), Toll-like receptor (TLR)/interleukin-1 receptor (IL-1R) superfamily, and unconventional cytokine receptors such as IL-6R and IL-17R (so2022theimmunologicalsignificance pages 2-3). Seven mammalian members (TRAF1–TRAF7) have been identified, each with a multi-domain architecture that is only partially shared across the family (so2022theimmunologicalsignificance pages 2-3).

The canonical TRAF domain architecture (shared by TRAF2, TRAF3, TRAF4, TRAF5, and TRAF6) consists of:

- **N-terminal RING domain** (~60 residues): A variant of the C3HC4 "cross-brace" zinc-binding motif that functions as an E3 ubiquitin ligase module. In TRAF6, this domain differs from the typical RING finger by substituting the C-terminal cysteine with an aspartate residue for zinc ligation (mercier2007structureinteractionsand pages 1-2).
- **Zinc-finger domains** (variable number): Cysteine-rich domains positioned between the RING and coiled-coil regions. In TRAF2 and TRAF5, the zinc fingers cooperate in ubiquitin binding and chain assembly (so2022theimmunologicalsignificance pages 2-3).
- **Coiled-coil domain (TRAF-N)**: Mediates trimerization and forms the "stalk" of the mushroom-shaped trimer structure (mercier2007structureinteractionsand pages 1-2, zapata2001adiversefamily pages 1-1).
- **TRAF-C domain (also known as MATH domain)**: An eight-stranded antiparallel β-sandwich fold of approximately 180 amino acids that is the hallmark of the family. This domain contains a surface crevice responsible for binding peptidyl motifs in the cytoplasmic domains of TNF family receptors (zapata2001adiversefamily pages 1-1, mercier2007structureinteractionsand pages 1-2).

### 1.2 Structural Exceptions

Two family members deviate significantly from this canonical architecture:

- **TRAF1** lacks the N-terminal RING domain entirely while retaining zinc-finger, coiled-coil, and TRAF-C domains (so2022theimmunologicalsignificance pages 2-3). This makes TRAF1 a pseudo-enzyme member that lacks intrinsic E3 ubiquitin ligase activity and functions primarily as a signaling adaptor.
- **TRAF7** possesses a RING domain, zinc fingers, and coiled-coil motif, but **lacks the TRAF-C/MATH domain entirely**, replacing it with seven C-terminal WD40 repeats (so2022theimmunologicalsignificance pages 2-3, tsitsikov2023traf7isan pages 1-2). TRAF7 is thus the most structurally divergent mammalian family member.

### 1.3 Dual Biochemical Functions

TRAF proteins function through two principal mechanisms: as **adaptor proteins** that scaffold signaling complexes, and as **E3 ubiquitin ligases** that catalyze polyubiquitination (gao2026thestructureand pages 3-5, hacker2011expandingtraffunction pages 2-3). The best-characterized catalytic member is TRAF6, which cooperates with the E2 ubiquitin-conjugating enzyme heterodimer Ubc13-Uev1A to generate K63-linked polyubiquitin chains. These chains do not target proteins for degradation but instead serve as scaffolds for activating downstream kinases including TAK1 and IKK (mercier2007structureinteractionsand pages 1-2, so2022theimmunologicalsignificance pages 3-4, li2024tumornecrosisfactor pages 2-4). The RING domain of TRAF6 forms homodimers to promote ubiquitin transfer (so2022theimmunologicalsignificance pages 3-4). TRAF3 also undergoes K63-linked ubiquitination, likely through self-ubiquitination via its RING finger domain (hildebrand2011rolesoftumor pages 11-13).

### 1.4 Receptor-Binding Specificity

Different TRAFs recognize distinct peptide motifs in receptor cytoplasmic tails. TRAFs 1, 2, 3, and 5 share binding to Px(Q/E)E, Px(Q/E)xxD, and PxQxT motifs, while TRAF4 preferentially recognizes the RLxA motif, and TRAF6 recognizes PxExx(Ar/Ac) motifs (so2022theimmunologicalsignificance pages 2-3). This differential specificity underlies the recruitment of specific TRAFs to different receptor complexes.

---

## 2. Functional Divergence Across the Family

The following table provides a comprehensive comparison of TRAF1–7:

| TRAF Member | Domain Architecture | RING Domain | TRAF-C/MATH Domain | E3 Ligase Activity | Key Signaling Functions | NF-kB Role | Peptide Motif | Notable Features |
|---|---|---|---|---|---|---|---|---|
| TRAF1 | Zinc fingers + coiled-coil (TRAF-N) + TRAF-C; lacks canonical N-terminal RING compared with TRAF2-6 | Absent | Present | No intrinsic RING-type E3 ligase activity inferred from domain loss; acts mainly as adaptor/regulator (so2022theimmunologicalsignificance pages 2-3) | TNFR-family signaling; promotes lymphocyte survival; important for CD8+ T-cell memory; can limit NEMO linear ubiquitination in inflammatory signaling (so2022theimmunologicalsignificance pages 6-6, so2022theimmunologicalsignificance pages 6-7) | Context dependent, often modulatory/negative in innate inflammatory NF-kB signaling, but can support pro-survival TNFR outputs (so2022theimmunologicalsignificance pages 6-6, so2022theimmunologicalsignificance pages 6-7) | Shares classical TRAF1/2/3/5 receptor-binding classes including Px(Q/E)E, Px(Q/E)xxD, and PxQxT motifs at family level (so2022theimmunologicalsignificance pages 2-3) | Unique among mammalian TRAFs in lacking RING domain; functionally diverged pseudo-ligase/adaptor-like member (so2022theimmunologicalsignificance pages 2-3) |
| TRAF2 | RING + zinc fingers + coiled-coil (TRAF-N) + TRAF-C | Present | Present | Yes; also recruits cIAP1/2, and its zinc fingers bind ubiquitin to support chain assembly (hacker2011expandingtraffunction pages 2-3, so2022theimmunologicalsignificance pages 2-3) | Central mediator downstream of TNFR1/TNFR2, CD40 and related receptors; promotes NF-kB/MAPK/JNK signaling; supports humoral immunity and class-switch recombination (so2022theimmunologicalsignificance pages 7-8, so2022theimmunologicalsignificance pages 2-3) | Mostly positive for canonical NF-kB; also part of TRAF2-TRAF3-cIAP complex restraining noncanonical NF-kB via NIK turnover (hildebrand2011rolesoftumor pages 10-11, hildebrand2011rolesoftumor pages 11-13) | TRAF1/2/3/5 class motifs: Px(Q/E)E, Px(Q/E)xxD, PxQxT (so2022theimmunologicalsignificance pages 2-3) | Ubiquitously expressed; major scaffold and E3-associated hub; frequently implicated in cancer and survival signaling (so2022theimmunologicalsignificance pages 6-6, albini2025inflammationandcancer pages 2-3) |
| TRAF3 | RING + zinc fingers + coiled-coil (TRAF-N) + TRAF-C | Present | Present | Yes/likely self-K63 ubiquitination through RING domain in signaling complexes; also undergoes regulated K48 degradation (hildebrand2011rolesoftumor pages 11-13, hacker2011expandingtraffunction pages 2-3) | Positive regulator of type I interferon pathways; negative regulator of canonical/noncanonical NF-kB and some MAPK outputs; restrains BCR and IL-17R signaling (hildebrand2011rolesoftumor pages 11-13, hildebrand2011rolesoftumor pages 10-11, so2022theimmunologicalsignificance pages 7-8) | Predominantly negative for NF-kB, especially noncanonical pathway via NIK control, but positive for antiviral IFN signaling (hildebrand2011rolesoftumor pages 11-13) | TRAF1/2/3/5 class motifs: Px(Q/E)E, Px(Q/E)xxD, PxQxT (so2022theimmunologicalsignificance pages 2-3) | Tri-functional immune regulator; tumor-suppressive in some contexts; ubiquitously expressed (hildebrand2011rolesoftumor pages 11-13, so2022theimmunologicalsignificance pages 6-6) |
| TRAF4 | RING + zinc fingers + coiled-coil (TRAF-N) + TRAF-C; includes reported nuclear localization signal | Present | Present | Yes, inferred from conserved RING architecture and family behavior (so2022theimmunologicalsignificance pages 2-3, gao2026thestructureand pages 3-5) | Developmental roles including tracheal morphogenesis; participates in IL-17A and IL-25 signaling; can have tissue-restricted functions (so2022theimmunologicalsignificance pages 6-7, gao2026thestructureand pages 3-5) | Context dependent; can positively or negatively tune signaling depending on pathway (so2022theimmunologicalsignificance pages 6-7) | Distinct TRAF4 preference: RLxA (so2022theimmunologicalsignificance pages 2-3) | More specialized than TRAF2/3/6; notable tissue specificity and nuclear-localization-related divergence (gao2026thestructureand pages 3-5, so2022theimmunologicalsignificance pages 6-7) |
| TRAF5 | RING + zinc fingers + coiled-coil (TRAF-N) + TRAF-C | Present | Present | Yes, inferred from conserved RING architecture; zinc fingers also cooperate in ubiquitin-related signaling (so2022theimmunologicalsignificance pages 2-3) | Lymphocyte-enriched signaling adaptor; positive regulator of OX40-mediated NF-kB; can inhibit IL-6/JAK-STAT signaling and restrain Th17 differentiation in some contexts (hildebrand2011rolesoftumor pages 10-11, so2022theimmunologicalsignificance pages 7-8) | Usually positive for NF-kB in TNFR-family signaling, but negative in selected cytokine pathways such as IL-6R signaling (hildebrand2011rolesoftumor pages 10-11, so2022theimmunologicalsignificance pages 7-8) | TRAF1/2/3/5 class motifs: Px(Q/E)E, Px(Q/E)xxD, PxQxT (so2022theimmunologicalsignificance pages 2-3) | Highly expressed in lymphocytes; function overlaps partly with TRAF2 but is not equivalent (so2022theimmunologicalsignificance pages 6-7, hildebrand2011rolesoftumor pages 10-11) |
| TRAF6 | RING + zinc fingers + coiled-coil (TRAF-N) + TRAF-C | Present | Present | Strongly established RING-type E3 ligase; cooperates with Ubc13-Uev1A to generate K63-linked polyubiquitin chains (mercier2007structureinteractionsand pages 1-2, so2022theimmunologicalsignificance pages 3-4) | Key mediator downstream of TLR/IL-1R, IL-17R and some TNFR-family pathways; activates TAK1 and IKK; essential in innate immunity, osteoclastogenesis, lymph node organogenesis, and antiviral responses (mercier2007structureinteractionsand pages 1-2, so2022theimmunologicalsignificance pages 7-8, li2024tumornecrosisfactor pages 2-4) | Predominantly positive for canonical NF-kB and inflammatory signaling (mercier2007structureinteractionsand pages 1-2, so2022theimmunologicalsignificance pages 3-4) | Distinct TRAF6 preference: PxExx(Ar/Ac) (so2022theimmunologicalsignificance pages 2-3) | Best-characterized catalytic TRAF; K63-chain builder and major inflammatory node; overexpressed in multiple cancers (mercier2007structureinteractionsand pages 1-2, li2024tumornecrosisfactor pages 2-4) |
| TRAF7 | RING + zinc fingers + coiled-coil + C-terminal WD40 repeats; lacks classical TRAF-C domain | Present | Absent; replaced by WD40 domain (so2022theimmunologicalsignificance pages 2-3, tsitsikov2023traf7isan pages 1-2) | Likely RING-type E3 ligase, but not interchangeable with TRAF1-6 because receptor-recognition module is different (tsitsikov2023traf7isan pages 1-2) | Regulates MEKK3-associated signaling and vascular integrity during development; implicated in meningioma and developmental disorders (tsitsikov2023traf7isan pages 1-2, so2022theimmunologicalsignificance pages 7-8) | Not a canonical TRAF-C-based NF-kB adaptor; pathway usage is distinct and context specific (tsitsikov2023traf7isan pages 1-2, so2022theimmunologicalsignificance pages 7-8) | Not applicable to classical TRAF-C peptide motifs because TRAF-C/MATH domain is absent (tsitsikov2023traf7isan pages 1-2) | Most structurally divergent mammalian TRAF; mutated in ~30% of meningiomas; C-terminal missense mutations often affect WD40 region (tsitsikov2023traf7isan pages 1-2) |


*Table: This table compares the seven mammalian TRAF family members by domain structure, catalytic potential, signaling roles, NF-kB behavior, and motif recognition. It is useful for assessing whether a broad family-level annotation could validly apply across all members.*

### 2.1 Key Functional Divergences

**Opposing NF-κB regulatory roles:** TRAF2 and TRAF5 are predominantly **positive regulators** of canonical NF-κB signaling downstream of OX40 and other TNFR superfamily members (hildebrand2011rolesoftumor pages 10-11). In contrast, TRAF3 functions as a **negative regulator** of both canonical and non-canonical NF-κB pathways, suppressing NF-κB-inducing kinase (NIK) levels by sequestering NIK in a TRAF2-TRAF3-cIAP1/2 complex that tags NIK for degradation (hildebrand2011rolesoftumor pages 11-13). Traf3-deficient mice experience constitutive and lethal activation of non-canonical NF-κB signaling (so2022theimmunologicalsignificance pages 6-7). TRAF3 is simultaneously a **positive regulator** of type I interferon production, earning it the designation of a "tri-faced immune regulator" (hacker2011expandingtraffunction pages 2-3, hildebrand2011rolesoftumor pages 11-13).

**Pseudo-enzyme member (TRAF1):** TRAF1 lacks the RING domain and therefore has no intrinsic E3 ubiquitin ligase activity (so2022theimmunologicalsignificance pages 2-3). It functions as a negative regulator of NF-κB activation by limiting linear ubiquitination of NEMO through binding to the LUBAC complex (so2022theimmunologicalsignificance pages 6-7), while also promoting lymphocyte survival and CD8+ T-cell memory formation (so2022theimmunologicalsignificance pages 6-6).

**Structurally divergent TRAF7:** TRAF7 lacks the TRAF-C domain entirely, substituting WD40 repeats that mediate distinct protein-protein interactions (tsitsikov2023traf7isan pages 1-2). TRAF7 is mutated in approximately 30% of meningiomas, the most common primary CNS tumor, with reported hemizygous missense mutations concentrated in the C-terminal WD40 region, suggesting gain-of-function or dominant-negative effects (tsitsikov2023traf7isan pages 1-2). TRAF7 is also essential for blood vessel integrity during embryonic and neonatal development (tsitsikov2023traf7isan pages 1-2).

**Tissue-specific and developmental roles:** TRAF4 contains a nuclear localization signal and shows preferential expression in breast carcinoma; Traf4-deficient mice display tracheal developmental defects but normal immune cell development (so2022theimmunologicalsignificance pages 6-7, gao2026thestructureand pages 3-5). TRAF6 is critical for osteoclastogenesis, lymph node organogenesis, and antiviral responses (so2022theimmunologicalsignificance pages 7-8).

**Neo-functionalization in cancer:** TRAF2 is predominantly described as a **tumor promoter**, with its expression correlated with increased metastatic potential and poorer prognosis across multiple cancer types. TRAF2 promotes tumor survival through NF-κB activation, supports angiogenesis, and facilitates immune suppression via regulatory T cells (albini2025inflammationandcancer pages 2-3, albini2025inflammationandcancer pages 1-2). In contrast, TRAF3 can act as a **tumor suppressor** through its inhibition of NF-κB signaling (hildebrand2011rolesoftumor pages 11-13). TRAF6 is overexpressed in multiple cancers including colon and lung cancer (li2024tumornecrosisfactor pages 2-4).

---

## 3. Taxonomic Scope

The PTHR10131 family encompasses 17,591 proteins across 8,155 taxa and 29 subfamilies, indicating a remarkably broad taxonomic distribution.

**Classical TRAFs (TRAF1–6):** Phylogenetic analyses indicate that classical TRAF proteins containing the canonical TRAF-C domain are found exclusively in **animal genomes**, from sponges (Porifera) to vertebrates (marin2012originanddiversification pages 7-8, marin2012originanddiversification pages 6-7). The TRAF1-TRAF2 pair and the broader TRAF3/5/6 groups appear to have diverged within the metazoan lineage.

**TRAF domain-containing proteins (TEFs):** Beyond classical TRAFs, TRAF domain (MATH domain)-containing proteins have a much wider eukaryotic distribution. Zapata et al. (2001) identified approximately 260 homologous TEF family proteins across fungi (yeast), protozoa, invertebrates, plants (monocots and dicots), amphibians, and mammals (zapata2001adiversefamily pages 6-6, zapata2001adiversefamily pages 1-1). The Arabidopsis EST database alone contains over 100 cDNA sequences encoding polypeptides with TRAF domain homology (zapata2001adiversefamily pages 9-10). These plant TRAF domain proteins include the MUSE13/14 and SINAT families involved in plant immunity and NLR regulation (ao2022characterizationoftwo pages 145-149). No TRAF domain proteins have been identified in prokaryotes (bacteria or archaea) (zapata2001adiversefamily pages 6-6).

**Evolutionary relationships:** Classical animal TRAF proteins appear to represent a more recent evolutionary lineage restricted to animals, while variant TRAF-domain-containing proteins (including MUL/TRIM37, USP7/HAUSP, and SPOP) have broader phylogenetic distributions extending to plants and unicellular eukaryotes, suggesting that the TRAF domain arose early in eukaryotic evolution (zapata2001adiversefamily pages 6-7, zapata2001adiversefamily pages 6-6). TRAF proteins may share evolutionary ancestry with TRIM ubiquitin ligases, both containing RING fingers and MATH domains (marin2012originanddiversification pages 7-8, marin2012originanddiversification pages 6-7).

The broad taxonomic scope (8,155 taxa) of PTHR10131 means that any GO terms mapped at the family level must hold across animals, plants, fungi, and potentially protists—a requirement that severely constrains viable annotations.

---

## 4. InterPro2GO Mapping Appropriateness

The current state of PTHR10131 is that **no InterPro2GO terms are mapped**. Given the extreme functional heterogeneity documented above, this absence is well-justified. The following table systematically evaluates candidate GO terms that might be considered:

| Candidate GO Term | GO ID | Category (MF/BP/CC) | True for All Members? | Problem if Applied | Recommendation | Rationale |
|---|---|---|---|---|---|---|
| protein binding | GO:0005515 | MF | Probably broad but not safely universal | Too generic to be informative; not experimentally justified for every matched protein across animals, plants, fungi, and divergent TRAF-like proteins | KEEP_AS_NON_CORE / generally avoid adding | Most TRAF-family proteins act through protein-protein interactions, but this term adds little value and may still fail for poorly characterized divergent members; InterPro2GO should prefer specific transferable functions (zapata2001adiversefamily pages 1-1, zapata2001adiversefamily pages 6-6, zapata2001adiversefamily pages 6-7) |
| signal transduction | GO:0007165 | BP | No | Over-broad process term; many members are regulators/adaptors in different pathways, and plant/fungal/TEF-like proteins need not participate in the same signaling processes | REMOVE | The family is functionally heterogeneous across classical TRAFs, TRAF7, and wider TRAF-domain proteins; no single signaling-process term is valid for all 17,591 proteins (so2022theimmunologicalsignificance pages 7-8, zapata2001adiversefamily pages 6-6, zapata2001adiversefamily pages 6-7, tsitsikov2023traf7isan pages 1-2) |
| ubiquitin-protein transferase activity | GO:0004842 | MF | No | False for TRAF1, which lacks a RING domain; also unsafe for divergent TRAF-domain proteins and some family branches where catalytic activity is unproven | MARK_AS_OVER_ANNOTATED / move to specific child entries only | TRAF2-6 generally have RING domains and E3-associated function, but TRAF1 lacks the RING domain and is a pseudo-ligase/adaptor-like member; TRAF7 is also structurally distinct (so2022theimmunologicalsignificance pages 2-3, hacker2011expandingtraffunction pages 2-3) |
| ubiquitin ligase activity | GO:0061630 | MF | No | Same over-annotation problem as above; not valid for all members and not proven across the full taxonomic breadth | MARK_AS_OVER_ANNOTATED / child-only if supported | Family-wide assignment would misannotate TRAF1 and likely many divergent TRAF-domain proteins outside the classical mammalian set (so2022theimmunologicalsignificance pages 2-3, mercier2007structureinteractionsand pages 1-2) |
| K63-linked polyubiquitin modification-dependent protein binding / K63-linked ubiquitination-related activity | N/A | MF | No | TRAF6-specialized mechanism; not a family-wide property | MOVE_TO_CHILD / TRAF6-centered entries only | TRAF6 is the best-established catalytic TRAF for Ubc13-Uev1A-dependent K63-chain assembly; extending this to the whole family would be incorrect (mercier2007structureinteractionsand pages 1-2, li2024tumornecrosisfactor pages 2-4, so2022theimmunologicalsignificance pages 3-4) |
| positive regulation of NF-kappaB signaling | GO:0043123 | BP | No | Opposite polarity across subfamilies; TRAF3 is a negative regulator in major contexts | MARK_AS_OVER_ANNOTATED | TRAF2/5/6 often promote NF-kB signaling, whereas TRAF3 restrains canonical/noncanonical NF-kB in multiple systems; a single positive-regulation term is not universally true (hildebrand2011rolesoftumor pages 11-13, hildebrand2011rolesoftumor pages 10-11, so2022theimmunologicalsignificance pages 7-8) |
| negative regulation of NF-kappaB signaling | GO:0032088 | BP | No | Also polarity-conflicted; many TRAFs are positive rather than negative regulators | MARK_AS_OVER_ANNOTATED | TRAF3 can inhibit NF-kB, but TRAF2/5/6 often enhance NF-kB pathway activation; the family contains both positive and negative regulators (hildebrand2011rolesoftumor pages 11-13, hildebrand2011rolesoftumor pages 10-11, so2022theimmunologicalsignificance pages 3-4) |
| NF-kappaB signaling | GO:0043122 | BP | No | Pathway leakage and overgeneralization across divergent taxa and subfamilies | REMOVE | NF-kB involvement is central for many animal TRAFs, but not demonstrably universal across non-animal TRAF-domain proteins or even all mammalian branches such as TRAF7-like variants (so2022theimmunologicalsignificance pages 7-8, marin2012originanddiversification pages 7-8, tsitsikov2023traf7isan pages 1-2) |
| tumor necrosis factor receptor binding | GO:0005164 | MF | No | Too specific to receptor-coupled animal TRAFs; many family proteins bind other receptors/adaptors, and non-animal members may lack TNFR contexts entirely | MOVE_TO_CHILD / specific receptor-associated subfamilies only | Classical TRAFs were defined through TNFR-family interactions, but many members also function downstream of TLR/IL-1R, RIG-I, IL-17R, and divergent proteins outside animals may not see TNFRs at all (so2022theimmunologicalsignificance pages 2-3, li2013structuralbasisof pages 1-4, zapata2001adiversefamily pages 6-6, zapata2001adiversefamily pages 6-7) |
| innate immune response | GO:0045087 | BP | No | Taxonomic leakage; applies to many animal TRAFs but not broadly across plants/fungi/protists or all subfamilies | REMOVE | Some TRAFs, especially TRAF3/6, are major innate immune regulators, but this is not safe for the full InterPro family spanning broad eukaryotic diversity (so2022theimmunologicalsignificance pages 7-8, so2022theimmunologicalsignificance pages 6-6, zapata2001adiversefamily pages 6-6, ao2022characterizationoftwo pages 145-149) |
| immune system process | GO:0002376 | BP | No | Taxon-restricted and over-broad | REMOVE | Immune-related roles are prominent in vertebrate and some invertebrate classical TRAFs, but not an across-the-board property for all family matches (so2022theimmunologicalsignificance pages 7-8, zapata2001adiversefamily pages 6-6, zapata2001adiversefamily pages 6-7) |
| cytoplasm | GO:0005737 | CC | No | Overly generic and not universal; some members show nuclear or specialized localization, and localization can be context dependent | REMOVE | TRAFs are often cytoplasmic adaptors, but TRAF4 has nuclear-localization-associated behavior and other family members can redistribute in signaling complexes; generic CC terms add little value (gao2026thestructureand pages 3-5, so2022theimmunologicalsignificance pages 6-7) |
| intracellular signal transduction | GO:0035556 | BP | No | Broad, process-level over-annotation across divergent taxa and branches | REMOVE | Although many classical TRAFs are intracellular signaling adaptors, the family is too heterogeneous to support this as a universal annotation (so2022theimmunologicalsignificance pages 2-3, so2022theimmunologicalsignificance pages 7-8, tsitsikov2023traf7isan pages 1-2) |
| receptor signaling complex scaffold/adaptor activity | N/A | MF | No stable GO term applicable family-wide | Mechanistically attractive but still not universal across divergent branches and taxonomic spread | MODIFY-to-specific / apply at child entries only | Classical animal TRAFs act as adaptors/scaffolds, yet TRAF7 and wider TRAF-domain proteins differ substantially in domain organization and pathway usage (so2022theimmunologicalsignificance pages 2-3, li2013structuralbasisof pages 1-4, tsitsikov2023traf7isan pages 1-2) |


*Table: This table evaluates candidate GO terms that might be considered for PTHR10131 and explains why most would over-annotate this highly diverse TRAF family. It is useful for deciding whether the current absence of InterPro2GO mappings should be retained.*

### 4.1 Specific Issues Precluding Family-Wide GO Annotations

1. **E3 ubiquitin ligase activity (GO:0061630 / GO:0004842):** Cannot apply to the entire family because TRAF1 lacks the RING domain and has no intrinsic E3 ligase activity (so2022theimmunologicalsignificance pages 2-3). TRAF7, while possessing a RING domain, has a fundamentally different C-terminal architecture (tsitsikov2023traf7isan pages 1-2).

2. **NF-κB signaling terms (GO:0043123 / GO:0032088):** Members have **opposing** regulatory roles—TRAF2/5/6 promote NF-κB activation while TRAF3 inhibits it (hildebrand2011rolesoftumor pages 11-13, hildebrand2011rolesoftumor pages 10-11). Neither positive nor negative regulation terms can be safely applied family-wide.

3. **TNF receptor binding (GO:0005164):** While classical TRAFs interact with TNFRSF members, they also function downstream of TLRs, IL-1R, RIG-I, and IL-17R (so2022theimmunologicalsignificance pages 2-3, li2013structuralbasisof pages 1-4). Plant and fungal TRAF-domain proteins likely lack TNFR interaction contexts entirely.

4. **Innate immune response (GO:0045087):** This is a taxon-restricted process term. Plant TRAF-domain proteins participate in plant immunity through different mechanisms (NLR regulation), and many TRAF-domain proteins across fungi and protists may have entirely unrelated functions (zapata2001adiversefamily pages 6-6, ao2022characterizationoftwo pages 145-149).

5. **Cytoplasm (GO:0005737):** TRAF4 has nuclear localization behavior, and TRAF members can redistribute to signaling complexes at membranes (gao2026thestructureand pages 3-5, so2022theimmunologicalsignificance pages 6-7).

---

## 5. Over-Annotation Verdict

### Summary Assessment

The current absence of InterPro2GO terms for PTHR10131 (TNF RECEPTOR ASSOCIATED FACTOR) is **appropriate and should be maintained**. This is a functionally **highly heterogeneous** family-level entry with:

- **29 subfamilies** spanning extraordinarily diverse biology
- Members with **opposing signaling roles** (TRAF2/5 vs. TRAF3 in NF-κB regulation)
- A **pseudo-enzyme member** lacking the catalytic RING domain (TRAF1)
- A **structurally divergent member** lacking the defining TRAF-C/MATH domain (TRAF7)
- Distribution across **8,155 taxa** including animals, plants, fungi, and protists with divergent biological contexts
- **Plant TRAF-domain proteins** that function in NLR-mediated immunity rather than TNFR signaling

### Recommended GO Action Pattern

**For the top-level PTHR10131 entry:** **ACCEPT** the current state (no InterPro2GO terms). No family-wide GO terms are appropriate.

**For subfamily entries:** **MODIFY-to-specific** — GO terms should be applied at the subfamily or child entry level where functional homogeneity can be established. For example:
- TRAF6-specific subfamilies could receive: GO:0004842 (ubiquitin-protein transferase activity), GO:0043123 (positive regulation of I-kappaB kinase/NF-kappaB signaling)
- TRAF3-specific subfamilies could receive: GO:0032088 (negative regulation of NF-kappaB transcription factor activity), GO:0032481 (positive regulation of type I interferon production)
- TRAF2-specific subfamilies could receive: GO:0004842 (ubiquitin-protein transferase activity), GO:0043123 (positive regulation of NF-kappaB signaling)

### Recommendation for InterPro

Any future attempt to add InterPro2GO terms to PTHR10131 should be **rejected** unless restricted to extremely generic terms (e.g., GO:0005515 protein binding), which themselves carry insufficient informational value to justify inclusion. GO annotation efforts should instead be directed to the 29 child subfamilies where functionally coherent annotations can be applied without risk of systematic over-annotation across the 17,591 matched proteins. The structural and functional diversity within this family—including pseudo-enzyme members, structurally divergent members, opposing regulatory polarities, and cross-kingdom taxonomic breadth—makes this among the clearest cases for keeping family-level GO mappings empty and pushing annotations to lower hierarchical levels.

---

## Key References

- So T. (2022) *International Immunology* 34:7–20. Comprehensive review of TRAF immunological significance.
- Zapata JM et al. (2001) *J Biol Chem* 276:24242–24252. Discovery of TRAF domain diversity across eukaryotes.
- Häcker H et al. (2011) *Nature Reviews Immunology* 11:457–468. TRAF3 as tri-faced immune regulator.
- Hildebrand JM et al. (2011) *Immunological Reviews* 244:55–74. TRAF3 and TRAF5 immune functions.
- Mercier P et al. (2007) *Protein Science* 16:602–614. TRAF6 RING domain structure.
- Dhillon B et al. (2019) *Frontiers in Immunology* 10:104. Evolving role of TRAFs in inflammation.
- Tsitsikov EN et al. (2023) *iScience* 26:107474. TRAF7 in blood vessel integrity and meningioma.
- Li T et al. (2024) *Journal of Cancer* 15:560–576. TRAF6 in human cancer.
- Albini A et al. (2025) *Cell Death & Disease* 16. TRAF2 in inflammation and cancer.
- Marín I. (2012) *PLoS ONE* 7:e50030. TRIM/TRAF evolutionary relationships.
- Gao L et al. (2026) *Frontiers in Oncology* 16. TRAF structure/function in leukemia.

References

1. (so2022theimmunologicalsignificance pages 2-3): Takanori So. The immunological significance of tumor necrosis factor receptor-associated factors (trafs). International immunology, 34:7-20, Aug 2022. URL: https://doi.org/10.1093/intimm/dxab058, doi:10.1093/intimm/dxab058. This article has 54 citations and is from a peer-reviewed journal.

2. (mercier2007structureinteractionsand pages 1-2): Pascal Mercier, Michael J. Lewis, D. Duong Hau, Linda F. Saltibus, Wei Xiao, and Leo Spyracopoulos. Structure, interactions, and dynamics of the ring domain from human traf6. Protein Science, 16:602-614, Apr 2007. URL: https://doi.org/10.1110/ps.062358007, doi:10.1110/ps.062358007. This article has 42 citations and is from a peer-reviewed journal.

3. (zapata2001adiversefamily pages 1-1): Juan M. Zapata, Krzysztof Pawlowski, Elvira Haas, Carl F. Ware, Adam Godzik, and John C. Reed. A diverse family of proteins containing tumor necrosis factor receptor-associated factor domains*. The Journal of Biological Chemistry, 276:24242-24252, Jun 2001. URL: https://doi.org/10.1074/jbc.m100354200, doi:10.1074/jbc.m100354200. This article has 297 citations.

4. (tsitsikov2023traf7isan pages 1-2): Erdyni N. Tsitsikov, Khanh P. Phan, Yufeng Liu, Alla V. Tsytsykova, Mike Kinter, Lauren Selland, Lori Garman, Courtney Griffin, and Ian F. Dunn. Traf7 is an essential regulator of blood vessel integrity during mouse embryonic and neonatal development. iScience, 26:107474, Aug 2023. URL: https://doi.org/10.1016/j.isci.2023.107474, doi:10.1016/j.isci.2023.107474. This article has 9 citations and is from a peer-reviewed journal.

5. (gao2026thestructureand pages 3-5): Le Gao, Mei-hua Yan, Ruochen Xu, Linping Xu, Yongping Song, Wei Li, and Xudong Li. The structure and functions of traf families and recent advances of trafs in leukemia. Frontiers in Oncology, Feb 2026. URL: https://doi.org/10.3389/fonc.2026.1738210, doi:10.3389/fonc.2026.1738210. This article has 0 citations.

6. (hacker2011expandingtraffunction pages 2-3): Hans Häcker, Ping-Hui Tseng, and Michael Karin. Expanding traf function: traf3 as a tri-faced immune regulator. Nature Reviews Immunology, 11:457-468, Jul 2011. URL: https://doi.org/10.1038/nri2998, doi:10.1038/nri2998. This article has 581 citations and is from a highest quality peer-reviewed journal.

7. (so2022theimmunologicalsignificance pages 3-4): Takanori So. The immunological significance of tumor necrosis factor receptor-associated factors (trafs). International immunology, 34:7-20, Aug 2022. URL: https://doi.org/10.1093/intimm/dxab058, doi:10.1093/intimm/dxab058. This article has 54 citations and is from a peer-reviewed journal.

8. (li2024tumornecrosisfactor pages 2-4): Tingting Li, Zhe Lei, Lin Wei, Kai Yang, Jinhong Shen, and Lin Hu. Tumor necrosis factor receptor-associated factor 6 and human cancer: a systematic review of mechanistic insights, functional roles, and therapeutic potential. Journal of Cancer, 15:560-576, Jan 2024. URL: https://doi.org/10.7150/jca.90059, doi:10.7150/jca.90059. This article has 14 citations and is from a peer-reviewed journal.

9. (hildebrand2011rolesoftumor pages 11-13): Joanne M. Hildebrand, Zuoan Yi, Claire M. Buchta, Jayakumar Poovassery, Laura L. Stunz, and Gail A. Bishop. Roles of tumor necrosis factor receptor associated factor 3 (traf3) and traf5 in immune cell functions. Immunological Reviews, 244:55-74, Nov 2011. URL: https://doi.org/10.1111/j.1600-065x.2011.01055.x, doi:10.1111/j.1600-065x.2011.01055.x. This article has 129 citations and is from a domain leading peer-reviewed journal.

10. (so2022theimmunologicalsignificance pages 6-6): Takanori So. The immunological significance of tumor necrosis factor receptor-associated factors (trafs). International immunology, 34:7-20, Aug 2022. URL: https://doi.org/10.1093/intimm/dxab058, doi:10.1093/intimm/dxab058. This article has 54 citations and is from a peer-reviewed journal.

11. (so2022theimmunologicalsignificance pages 6-7): Takanori So. The immunological significance of tumor necrosis factor receptor-associated factors (trafs). International immunology, 34:7-20, Aug 2022. URL: https://doi.org/10.1093/intimm/dxab058, doi:10.1093/intimm/dxab058. This article has 54 citations and is from a peer-reviewed journal.

12. (so2022theimmunologicalsignificance pages 7-8): Takanori So. The immunological significance of tumor necrosis factor receptor-associated factors (trafs). International immunology, 34:7-20, Aug 2022. URL: https://doi.org/10.1093/intimm/dxab058, doi:10.1093/intimm/dxab058. This article has 54 citations and is from a peer-reviewed journal.

13. (hildebrand2011rolesoftumor pages 10-11): Joanne M. Hildebrand, Zuoan Yi, Claire M. Buchta, Jayakumar Poovassery, Laura L. Stunz, and Gail A. Bishop. Roles of tumor necrosis factor receptor associated factor 3 (traf3) and traf5 in immune cell functions. Immunological Reviews, 244:55-74, Nov 2011. URL: https://doi.org/10.1111/j.1600-065x.2011.01055.x, doi:10.1111/j.1600-065x.2011.01055.x. This article has 129 citations and is from a domain leading peer-reviewed journal.

14. (albini2025inflammationandcancer pages 2-3): Adriana Albini, Luisa Di Paola, Giampiero Mei, Denisa Baci, Nicola Fusco, Giovanni Corso, and Douglas Noonan. Inflammation and cancer cell survival: traf2 as a key player. Cell Death & Disease, Apr 2025. URL: https://doi.org/10.1038/s41419-025-07609-w, doi:10.1038/s41419-025-07609-w. This article has 28 citations and is from a peer-reviewed journal.

15. (albini2025inflammationandcancer pages 1-2): Adriana Albini, Luisa Di Paola, Giampiero Mei, Denisa Baci, Nicola Fusco, Giovanni Corso, and Douglas Noonan. Inflammation and cancer cell survival: traf2 as a key player. Cell Death & Disease, Apr 2025. URL: https://doi.org/10.1038/s41419-025-07609-w, doi:10.1038/s41419-025-07609-w. This article has 28 citations and is from a peer-reviewed journal.

16. (marin2012originanddiversification pages 7-8): I. Marín. Origin and diversification of trim ubiquitin ligases. PLoS ONE, Nov 2012. URL: https://doi.org/10.1371/journal.pone.0050030, doi:10.1371/journal.pone.0050030. This article has 78 citations and is from a peer-reviewed journal.

17. (marin2012originanddiversification pages 6-7): I. Marín. Origin and diversification of trim ubiquitin ligases. PLoS ONE, Nov 2012. URL: https://doi.org/10.1371/journal.pone.0050030, doi:10.1371/journal.pone.0050030. This article has 78 citations and is from a peer-reviewed journal.

18. (zapata2001adiversefamily pages 6-6): Juan M. Zapata, Krzysztof Pawlowski, Elvira Haas, Carl F. Ware, Adam Godzik, and John C. Reed. A diverse family of proteins containing tumor necrosis factor receptor-associated factor domains*. The Journal of Biological Chemistry, 276:24242-24252, Jun 2001. URL: https://doi.org/10.1074/jbc.m100354200, doi:10.1074/jbc.m100354200. This article has 297 citations.

19. (zapata2001adiversefamily pages 9-10): Juan M. Zapata, Krzysztof Pawlowski, Elvira Haas, Carl F. Ware, Adam Godzik, and John C. Reed. A diverse family of proteins containing tumor necrosis factor receptor-associated factor domains*. The Journal of Biological Chemistry, 276:24242-24252, Jun 2001. URL: https://doi.org/10.1074/jbc.m100354200, doi:10.1074/jbc.m100354200. This article has 297 citations.

20. (ao2022characterizationoftwo pages 145-149): Kevin Ao. Characterization of two regulators in plant immune receptor-mediated defense. Text, Jan 2022. URL: https://doi.org/10.14288/1.0421623, doi:10.14288/1.0421623. This article has 0 citations and is from a peer-reviewed journal.

21. (zapata2001adiversefamily pages 6-7): Juan M. Zapata, Krzysztof Pawlowski, Elvira Haas, Carl F. Ware, Adam Godzik, and John C. Reed. A diverse family of proteins containing tumor necrosis factor receptor-associated factor domains*. The Journal of Biological Chemistry, 276:24242-24252, Jun 2001. URL: https://doi.org/10.1074/jbc.m100354200, doi:10.1074/jbc.m100354200. This article has 297 citations.

22. (li2013structuralbasisof pages 1-4): Jixi Li, Qian Yin, and Hao Wu. Structural basis of signal transduction in the tnf receptor superfamily. Advances in immunology, 119:135-53, Jan 2013. URL: https://doi.org/10.1016/b978-0-12-407707-2.00005-9, doi:10.1016/b978-0-12-407707-2.00005-9. This article has 154 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PTHR10131-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR10131-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. so2022theimmunologicalsignificance pages 2-3
2. mercier2007structureinteractionsand pages 1-2
3. so2022theimmunologicalsignificance pages 3-4
4. hildebrand2011rolesoftumor pages 11-13
5. so2022theimmunologicalsignificance pages 6-7
6. hildebrand2011rolesoftumor pages 10-11
7. so2022theimmunologicalsignificance pages 6-6
8. so2022theimmunologicalsignificance pages 7-8
9. li2024tumornecrosisfactor pages 2-4
10. zapata2001adiversefamily pages 9-10
11. ao2022characterizationoftwo pages 145-149
12. zapata2001adiversefamily pages 6-6
13. zapata2001adiversefamily pages 1-1
14. gao2026thestructureand pages 3-5
15. hacker2011expandingtraffunction pages 2-3
16. albini2025inflammationandcancer pages 2-3
17. albini2025inflammationandcancer pages 1-2
18. marin2012originanddiversification pages 7-8
19. marin2012originanddiversification pages 6-7
20. zapata2001adiversefamily pages 6-7
21. li2013structuralbasisof pages 1-4
22. https://doi.org/10.1093/intimm/dxab058,
23. https://doi.org/10.1110/ps.062358007,
24. https://doi.org/10.1074/jbc.m100354200,
25. https://doi.org/10.1016/j.isci.2023.107474,
26. https://doi.org/10.3389/fonc.2026.1738210,
27. https://doi.org/10.1038/nri2998,
28. https://doi.org/10.7150/jca.90059,
29. https://doi.org/10.1111/j.1600-065x.2011.01055.x,
30. https://doi.org/10.1038/s41419-025-07609-w,
31. https://doi.org/10.1371/journal.pone.0050030,
32. https://doi.org/10.14288/1.0421623,
33. https://doi.org/10.1016/b978-0-12-407707-2.00005-9,