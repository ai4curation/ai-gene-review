---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T20:47:17.715268'
end_time: '2026-06-28T21:15:50.692023'
duration_seconds: 1712.98
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR14334
  interpro_name: B-CELL ANTIGEN RECEPTOR COMPLEX-ASSOCIATED PROTEIN
  interpro_short_name: Not specified
  interpro_type: family
  interpro_integrated: None (top-level entry)
  member_databases: Not specified
  n_proteins: '2081'
  n_taxa: '2274'
  n_subfamilies: '3'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: Not specified in InterPro
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
  path: PTHR14334-deep-research-falcon_artifacts/artifact-00.md
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
- **Accession:** PTHR14334
- **Name:** B-CELL ANTIGEN RECEPTOR COMPLEX-ASSOCIATED PROTEIN
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** Not specified
- **Scale:** 2081 proteins across 2274 taxa, 3 subfamilies
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
**PTHR14334 (B-CELL ANTIGEN RECEPTOR COMPLEX-ASSOCIATED PROTEIN)**, structured to support GO annotation review.

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
- **Accession:** PTHR14334
- **Name:** B-CELL ANTIGEN RECEPTOR COMPLEX-ASSOCIATED PROTEIN
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** Not specified
- **Scale:** 2081 proteins across 2274 taxa, 3 subfamilies
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
**PTHR14334 (B-CELL ANTIGEN RECEPTOR COMPLEX-ASSOCIATED PROTEIN)**, structured to support GO annotation review.

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


# InterPro Family Research Report: PTHR14334 — B-Cell Antigen Receptor Complex-Associated Protein

## 1. Family Definition and Biochemistry

### Identity and Composition
PTHR14334 is a PANTHER family-level entry encompassing the **B-cell antigen receptor complex-associated proteins**, specifically CD79A (Igα, also known as mb-1) and CD79B (Igβ, also known as B29). These proteins form a disulfide-linked heterodimer that constitutes the signaling module of the B-cell receptor (BCR) complex. The BCR consists of a membrane-bound immunoglobulin (mIg) non-covalently associated with a single CD79A/CD79B heterodimer in a 1:1 stoichiometry (xie2023astructuralplatform pages 1-2, reth2023discoveringimmunoreceptorcoupling pages 1-2).

### Domain Architecture
Each CD79 chain contains three functionally distinct regions:
- **Extracellular domain**: A single immunoglobulin superfamily (IgSF) C-like domain, connected by a disulfide bond between CD79A and CD79B. This is the least conserved region with significant interspecies variability (tkachenko2023bcellreceptorsignaling pages 3-5, lefranc2020immunoglobulinsorantibodies pages 6-9).
- **Transmembrane domain**: Single-pass alpha-helical segments that form a compact four-helix bundle with the two heavy chain transmembrane helices of mIg, stabilized by conserved hydrogen bonds within the hydrophobic membrane environment (xie2023astructuralplatform pages 1-2, tolar2022unveilingtheb pages 1-2).
- **Intracellular domain**: Contains immunoreceptor tyrosine-based activation motifs (ITAMs) with the conserved consensus sequence **(D/E)xxYxx(L/I)x₆₋₈Yxx(L/I)**, comprising 26 amino acid residues with two critical tyrosine residues (lefranc2020immunoglobulinsorantibodies pages 6-9, tkachenko2023bcellreceptorsignaling pages 3-5).

### Structural Insights from Cryo-EM
Landmark cryo-EM structures of the full-length BCR complex published in 2022 by three independent groups revealed the molecular principles of BCR assembly. These structures demonstrated that mIg associates asymmetrically with the CD79A/CD79B heterodimer — predominantly through one of the two heavy chains — with transmembrane domain interactions playing a dominant stabilizing role (reth2023discoveringimmunoreceptorcoupling pages 1-2, do2025dynamicsandactivation pages 1-4, tolar2022unveilingtheb pages 1-2). A membrane-proximal connecting peptide of mIg adopts an interdigitated topology with CD79A/CD79B, creating a braided network essential for complex stability. Notably, the cytoplasmic ITAM tails are not resolved in the structures, indicating high flexibility (xie2023astructuralplatform pages 1-2, tolar2022unveilingtheb pages 2-3).

### Signaling Mechanism
Upon antigen binding, Src-family tyrosine kinases (Lyn, Fyn, Blk) phosphorylate the ITAM tyrosine residues on CD79A and CD79B. Mono-phosphorylation recruits Lyn kinase, while bis-phosphorylation recruits SYK kinase, which in turn activates downstream signaling cascades including PI3K/AKT, NF-κB, and MAPK pathways through adaptors such as BLNK, BTK, and PLCγ2 (tkachenko2023bcellreceptorsignaling pages 5-7, tkachenko2023bcellreceptorsignaling pages 8-10, tkachenko2023bcellreceptorsignaling pages 7-8). CD79A contains classical ITAM tyrosines at positions 188 and 199 (mouse numbering), as well as non-ITAM tyrosines (Y176 and Y204 in mouse), all of which are functionally important (tkachenko2023bcellreceptorsignaling pages 7-8).

## 2. InterPro2GO Mapping Appropriateness

PTHR14334 currently has **no InterPro2GO terms mapped**. Given the well-characterized, functionally homogeneous nature of this family, this represents an **under-annotation** rather than an over-annotation problem.

### Recommended GO Terms for Addition

The following GO terms would be appropriate for family-level mapping because they are true for **all** members (both CD79A and CD79B, across all jawed vertebrate taxa):

| GO Term | Category | Justification | Recommendation |
|---------|----------|---------------|----------------|
| GO:0050853 (B cell receptor signaling pathway) | Biological Process | Both CD79A and CD79B are essential, obligate signaling subunits of the BCR; all family members function in this pathway (tkachenko2023bcellreceptorsignaling pages 3-5, tkachenko2023bcellreceptorsignaling pages 5-7, tkachenko2023bcellreceptorsignaling pages 1-2) | **ADD** — core family-safe term |
| GO:0005886 (plasma membrane) | Cellular Component | All members are type I transmembrane proteins that function at the cell surface as BCR components (tkachenko2023bcellreceptorsignaling pages 3-5, bhattacharyya2023combinationofhighresolution pages 2-4) | **ADD** — core family-safe term |
| GO:0042113 (B cell activation) | Biological Process | Both CD79A and CD79B participate in B cell activation through BCR signaling (huse2022mechanismofcd79a pages 1-3, tkachenko2023bcellreceptorsignaling pages 3-5) | **ADD with caution** — secondary term |
| GO:0016021 (integral component of membrane) | Cellular Component | All members have single-pass transmembrane domains (xie2023astructuralplatform pages 1-2, tolar2022unveilingtheb pages 1-2) | **ADD** — structural fact for all members |

### Terms to Avoid at Family Level
- Specific kinase-interaction terms (e.g., SYK binding) — CD79A and CD79B recruit different kinases with different phosphorylation patterns (tkachenko2023bcellreceptorsignaling pages 8-10)
- NF-κB activation terms — the specific NF-κB pathway activated differs between CD79A and CD79B contexts (tkachenko2023bcellreceptorsignaling pages 13-14)
- Antigen receptor activity — CD79A/CD79B are signaling subunits within a receptor complex, not the antigen-binding components themselves

## 3. Functional Divergence Across the Family

### CD79A vs. CD79B Subfamilies
PTHR14334 contains 3 subfamilies across 2081 proteins, most likely corresponding to CD79A, CD79B, and possibly a less-characterized group of divergent orthologs. Despite sharing the same overall architecture and core BCR-signaling function, CD79A and CD79B exhibit important functional differences:

- **CD79B mutations** are significantly enriched in activated B-cell-like diffuse large B-cell lymphoma (ABC-DLBCL), occurring in up to 30% of cases, and commonly target the first ITAM tyrosine (Y196). These mutations promote chronic active BCR signaling through augmented BCR surface levels, enhanced clustering, and impaired Lyn-mediated negative feedback (tkachenko2023bcellreceptorsignaling pages 10-11, tkachenko2023bcellreceptorsignaling pages 11-13).
- **CD79A mutations** are less frequent (3–4% in NHL) and predominantly affect tonic BCR signaling in GCB-DLBCL, often resulting in removal of the entire ITAM region rather than point mutations (tkachenko2023bcellreceptorsignaling pages 10-11, tkachenko2023bcellreceptorsignaling pages 8-10).
- **CD79B** acts as a signaling hub mediating crosstalk between BCR and co-receptors (CD19, BAFFR), localizes near CD19 independently, and interacts with negative regulator TRAF3 (tkachenko2023bcellreceptorsignaling pages 8-10, tkachenko2023bcellreceptorsignaling pages 13-14).
- **CD79A** is more critically involved in PI3K/AKT/mTOR pro-survival signaling in mantle cell lymphoma and GCB-DLBCL (tkachenko2023bcellreceptorsignaling pages 13-14).

### No Pseudo-enzyme or Catalytically Dead Members
Neither CD79A nor CD79B is an enzyme, so the concept of catalytically dead members does not directly apply. However, both are scaffolding proteins that can harbor loss-of-function mutations causing agammaglobulinemia. In humans, CD79B G137S disrupts the disulfide bond required for heterodimerization with CD79A, resulting in severely reduced mature peripheral B cells (huse2022mechanismofcd79a pages 10-11). Both CD79A and CD79B are essential and interdependent — deletion of either blocks B cell development at the bone marrow checkpoint and prevents emergence of mature B cells (huse2022mechanismofcd79a pages 1-3).

## 4. Taxonomic Scope

### Jawed Vertebrate Restriction
The PTHR14334 family is restricted to **jawed vertebrates (Gnathostomata)**, which are the only animals possessing an immunoglobulin-based adaptive immune system with BCRs. CD79A and CD79B orthologs have been identified across:

- **Cartilaginous fish (Chondrichthyes)**: CD79A-like genes and BCR-associated B-cell programs are present in sharks, including the white-spotted bamboo shark, where B cells are characterized by markers including blnk, btk, and igll1-like (wang2024singlecellrnasequencing pages 1-2).
- **Bony fish (Teleostei)**: CD79A is used as a B-cell marker in zebrafish and Chinese tongue sole; CD79A and CD79B have been characterized in multiple teleost species including rainbow trout, turbot, and Sichuan taimen (wang2024singlecellrnasequencing pages 1-2, chen2023multitissuescrnaseqreveals pages 5-6).
- **Tetrapods**: Conserved across amphibians, reptiles, birds, and mammals.

### Taxonomic Safety of GO Terms
Since the family is inherently restricted to organisms with BCR-based adaptive immunity, B-cell-specific GO terms such as "B cell receptor signaling pathway" do not pose a taxa-leak problem. The biological pathway and cellular compartment are present in all species where the family occurs. OpenTargets data confirms strong disease associations for both CD79A and CD79B with agammaglobulinemia and diffuse large B-cell lymphoma in humans (OpenTargets Search: -CD79A,CD79B).

## 5. Over-Annotation Verdict

The summary of the GO annotation review for PTHR14334 is presented below:

| Assessment Category | Finding | Recommendation |
|---|---|---|
| Family definition and functional homogeneity | PTHR14334 corresponds to the B-cell receptor signaling subunits CD79A/Igα and CD79B/Igβ. Across the family, members are type I single-pass membrane proteins with an extracellular Ig-like domain and cytoplasmic ITAM, functioning as the signaling module of the BCR; recent structural work shows conserved 1:1 assembly with membrane Ig in a four-helix transmembrane bundle, supporting substantial family-level functional homogeneity for core BCR-signaling roles (tkachenko2023bcellreceptorsignaling pages 3-5, lefranc2020immunoglobulinsorantibodies pages 6-9, xie2023astructuralplatform pages 1-2, tolar2022unveilingtheb pages 1-2). | Family-level GO terms can be justified for shared core roles tied to BCR signaling, but only when they are true for both CD79A and CD79B across taxa. |
| Current InterPro2GO status | No InterPro2GO terms are currently mapped to this family. Given the conserved role of both CD79A and CD79B in BCR assembly, surface expression, and ITAM-based signaling, the absence of any mapping appears conservative rather than erroneous (tkachenko2023bcellreceptorsignaling pages 3-5, tkachenko2023bcellreceptorsignaling pages 5-7, huse2022mechanismofcd79a pages 10-11, huse2022mechanismofcd79a pages 1-3). | Do not mark the current state as over-annotating; instead review for possible addition of a small number of core, family-safe GO terms. |
| Recommended GO terms to add with justification | Strongest family-safe candidates are process/component terms directly reflecting shared biology: **B cell receptor signaling pathway** (GO:0050853) because both CD79A and CD79B are essential BCR signaling subunits; **plasma membrane** (GO:0005886) because both are surface BCR components; and potentially **B cell activation** (GO:0042113) as a participating process, though this is broader and should be added more cautiously. A molecular-function term such as **transmembrane signaling receptor activity** may be arguable but is less ideal because CD79A/CD79B are signaling subunits within a receptor complex rather than antigen-binding receptors themselves (tkachenko2023bcellreceptorsignaling pages 3-5, tkachenko2023bcellreceptorsignaling pages 5-7, bhattacharyya2023combinationofhighresolution pages 2-4). | Prefer adding **GO:0050853** and **GO:0005886**. Consider **GO:0042113** as secondary/supporting. Avoid overly generic or potentially misleading MF terms unless InterPro curators confirm they are consistently used for signaling subunits. |
| Functional divergence between subfamilies | CD79A and CD79B are not fully interchangeable: CD79B mutations are enriched in ABC-DLBCL and often affect Y196, whereas CD79A mutations are less frequent and often remove more of the ITAM region; CD79B also has distinctive roles in BCR clustering, endocytosis, and signaling modulation. These differences indicate subfamily-specific nuances despite conserved core function (tkachenko2023bcellreceptorsignaling pages 10-11, tkachenko2023bcellreceptorsignaling pages 11-13, tkachenko2023bcellreceptorsignaling pages 8-10). | Keep family-level GO mappings restricted to shared core BCR roles. Put finer-grained signaling or disease-relevant annotations, if any, on CD79A- or CD79B-specific child entries rather than the parent family. |
| Taxonomic scope | The family is restricted to jawed vertebrates with adaptive BCR-based immunity. Evidence from cartilaginous fish and teleosts shows conservation of B-cell programs and CD79A/CD79B-associated B-cell markers, supporting deep gnathostome conservation but not applicability outside vertebrate B-cell biology (wang2024singlecellrnasequencing pages 1-2, chen2023multitissuescrnaseqreveals pages 5-6, guslund2026igmmediatedprotectiondrives pages 1-2). | Any GO term added should remain within B-cell/BCR biology and avoid broader eukaryotic assumptions. No taxa-leak issue is expected for B-cell-specific terms because the family itself is taxonomically restricted. |
| Over-annotation verdict and recommended action | Because there are currently no mappings, there is no present over-annotation. However, adding broad or mechanistically overstated terms could create future over-annotation, especially if they imply direct ligand-binding receptor activity or CD79A/CD79B-specific regulatory details. Overall verdict: **sound but incomplete** parent-family annotation state (tkachenko2023bcellreceptorsignaling pages 3-5, tkachenko2023bcellreceptorsignaling pages 10-11, huse2022mechanismofcd79a pages 1-3). | **Action: MODIFY-to-specific / ADD conservative core terms.** Add only family-safe BCR terms (preferably GO:0050853 and GO:0005886), keep subfamily-specific functions on child entries, and avoid overly broad MF/process terms that exceed the evidence. |


*Table: This table summarizes the GO annotation review for the PTHR14334 B-cell antigen receptor complex-associated protein family. It highlights which aspects are safe to annotate at the family level versus those that should be restricted to CD79A- or CD79B-specific subfamilies.*

### Overall Assessment
**Current status: SOUND BUT INCOMPLETE (under-annotated)**

PTHR14334 currently has no InterPro2GO terms mapped. This is not an over-annotation problem but rather a gap in annotation. The family is functionally homogeneous at its core — all members are BCR signaling subunits with conserved ITAM motifs, transmembrane architecture, and B-cell-specific expression. The absence of GO mappings means that automated annotation pipelines relying on InterPro2GO will fail to annotate newly sequenced CD79A/CD79B orthologs with even the most fundamental functional terms.

### Recommended Action Pattern

**For the parent family PTHR14334: ADD conservative core terms**
- Add GO:0050853 (B cell receptor signaling pathway) — Biological Process
- Add GO:0005886 (plasma membrane) — Cellular Component
- Add GO:0016021 (integral component of membrane) — Cellular Component
- Consider GO:0042113 (B cell activation) — Biological Process (secondary)

**For subfamilies (CD79A-specific, CD79B-specific): KEEP_AS_NON_CORE**
- Subfamily-specific terms for differential signaling roles (e.g., specific kinase interactions, NF-κB pathway nuances) should be placed on child entries rather than the parent family.
- CD79B-specific terms related to BCR endocytosis regulation or CD19 co-signaling should not be elevated to family level.

**No terms need to be REMOVED or MARKED_AS_OVER_ANNOTATED**, as there are currently no mappings to evaluate for removal.

### Recommendation for InterPro Itself
The current family-level entry is appropriate. However, InterPro curators should consider:
1. Ensuring the 3 subfamilies clearly distinguish CD79A, CD79B, and any additional divergent members.
2. Adding subfamily-level InterPro2GO mappings for CD79A- and CD79B-specific GO terms once subfamily boundaries are confirmed.
3. Mapping a small set of core, family-safe GO terms to the parent entry to ensure baseline annotation coverage for all matched proteins.

References

1. (xie2023astructuralplatform pages 1-2): Wei Xie, Kai Wucherpfennig, and Dinshaw J. Patel. A structural platform for b cell receptor signaling. Cell Research, 33:95-96, Sep 2023. URL: https://doi.org/10.1038/s41422-022-00724-9, doi:10.1038/s41422-022-00724-9. This article has 15 citations and is from a domain leading peer-reviewed journal.

2. (reth2023discoveringimmunoreceptorcoupling pages 1-2): Michael Reth. Discovering immunoreceptor coupling and organization motifs. Frontiers in Immunology, Sep 2023. URL: https://doi.org/10.3389/fimmu.2023.1253412, doi:10.3389/fimmu.2023.1253412. This article has 9 citations and is from a peer-reviewed journal.

3. (tkachenko2023bcellreceptorsignaling pages 3-5): Anton Tkachenko, Kristyna Kupcova, and Ondrej Havranek. B-cell receptor signaling and beyond: the role of igα (cd79a)/igβ (cd79b) in normal and malignant b cells. International Journal of Molecular Sciences, 25:10, Dec 2023. URL: https://doi.org/10.3390/ijms25010010, doi:10.3390/ijms25010010. This article has 95 citations.

4. (lefranc2020immunoglobulinsorantibodies pages 6-9): Marie-Paule Lefranc and Gérard Lefranc. Immunoglobulins or antibodies: imgt® bridging genes, structures and functions. Biomedicines, 8:319, Aug 2020. URL: https://doi.org/10.3390/biomedicines8090319, doi:10.3390/biomedicines8090319. This article has 102 citations.

5. (tolar2022unveilingtheb pages 1-2): Pavel Tolar and Susan K. Pierce. Unveiling the b cell receptor structure. Science, 377:819-820, Aug 2022. URL: https://doi.org/10.1126/science.add8065, doi:10.1126/science.add8065. This article has 14 citations and is from a highest quality peer-reviewed journal.

6. (do2025dynamicsandactivation pages 1-4): Hung N. Do, Mingfei Zhao, S. Munir Alam, and S. Gnanakaran. Dynamics and activation of membrane-bound b cell receptor assembly. bioRxiv, Jul 2025. URL: https://doi.org/10.1101/2024.07.10.602784, doi:10.1101/2024.07.10.602784. This article has 2 citations.

7. (tolar2022unveilingtheb pages 2-3): Pavel Tolar and Susan K. Pierce. Unveiling the b cell receptor structure. Science, 377:819-820, Aug 2022. URL: https://doi.org/10.1126/science.add8065, doi:10.1126/science.add8065. This article has 14 citations and is from a highest quality peer-reviewed journal.

8. (tkachenko2023bcellreceptorsignaling pages 5-7): Anton Tkachenko, Kristyna Kupcova, and Ondrej Havranek. B-cell receptor signaling and beyond: the role of igα (cd79a)/igβ (cd79b) in normal and malignant b cells. International Journal of Molecular Sciences, 25:10, Dec 2023. URL: https://doi.org/10.3390/ijms25010010, doi:10.3390/ijms25010010. This article has 95 citations.

9. (tkachenko2023bcellreceptorsignaling pages 8-10): Anton Tkachenko, Kristyna Kupcova, and Ondrej Havranek. B-cell receptor signaling and beyond: the role of igα (cd79a)/igβ (cd79b) in normal and malignant b cells. International Journal of Molecular Sciences, 25:10, Dec 2023. URL: https://doi.org/10.3390/ijms25010010, doi:10.3390/ijms25010010. This article has 95 citations.

10. (tkachenko2023bcellreceptorsignaling pages 7-8): Anton Tkachenko, Kristyna Kupcova, and Ondrej Havranek. B-cell receptor signaling and beyond: the role of igα (cd79a)/igβ (cd79b) in normal and malignant b cells. International Journal of Molecular Sciences, 25:10, Dec 2023. URL: https://doi.org/10.3390/ijms25010010, doi:10.3390/ijms25010010. This article has 95 citations.

11. (tkachenko2023bcellreceptorsignaling pages 1-2): Anton Tkachenko, Kristyna Kupcova, and Ondrej Havranek. B-cell receptor signaling and beyond: the role of igα (cd79a)/igβ (cd79b) in normal and malignant b cells. International Journal of Molecular Sciences, 25:10, Dec 2023. URL: https://doi.org/10.3390/ijms25010010, doi:10.3390/ijms25010010. This article has 95 citations.

12. (bhattacharyya2023combinationofhighresolution pages 2-4): Puja Bhattacharyya, Richard I. Christopherson, Kristen K. Skarratt, Jake Z. Chen, Thomas Balle, and Stephen J. Fuller. Combination of high-resolution structures for the b cell receptor and co-receptors provides an understanding of their interactions with therapeutic antibodies. Cancers, 15:2881, May 2023. URL: https://doi.org/10.3390/cancers15112881, doi:10.3390/cancers15112881. This article has 7 citations.

13. (huse2022mechanismofcd79a pages 1-3): Kanutte Huse, Baoyan Bai, Vera I Hilden, Lise K Bollum, Thea K Våtsveen, Ludvig A Munthe, Erlend B Smeland, Jonathan M Irish, Sébastien Wälchli, and June H Myklebust. Mechanism of cd79a and cd79b support for igm+ b cell fitness through b cell receptor surface expression. The Journal of Immunology, 209:2042-2053, Nov 2022. URL: https://doi.org/10.4049/jimmunol.2200144, doi:10.4049/jimmunol.2200144. This article has 76 citations.

14. (tkachenko2023bcellreceptorsignaling pages 13-14): Anton Tkachenko, Kristyna Kupcova, and Ondrej Havranek. B-cell receptor signaling and beyond: the role of igα (cd79a)/igβ (cd79b) in normal and malignant b cells. International Journal of Molecular Sciences, 25:10, Dec 2023. URL: https://doi.org/10.3390/ijms25010010, doi:10.3390/ijms25010010. This article has 95 citations.

15. (tkachenko2023bcellreceptorsignaling pages 10-11): Anton Tkachenko, Kristyna Kupcova, and Ondrej Havranek. B-cell receptor signaling and beyond: the role of igα (cd79a)/igβ (cd79b) in normal and malignant b cells. International Journal of Molecular Sciences, 25:10, Dec 2023. URL: https://doi.org/10.3390/ijms25010010, doi:10.3390/ijms25010010. This article has 95 citations.

16. (tkachenko2023bcellreceptorsignaling pages 11-13): Anton Tkachenko, Kristyna Kupcova, and Ondrej Havranek. B-cell receptor signaling and beyond: the role of igα (cd79a)/igβ (cd79b) in normal and malignant b cells. International Journal of Molecular Sciences, 25:10, Dec 2023. URL: https://doi.org/10.3390/ijms25010010, doi:10.3390/ijms25010010. This article has 95 citations.

17. (huse2022mechanismofcd79a pages 10-11): Kanutte Huse, Baoyan Bai, Vera I Hilden, Lise K Bollum, Thea K Våtsveen, Ludvig A Munthe, Erlend B Smeland, Jonathan M Irish, Sébastien Wälchli, and June H Myklebust. Mechanism of cd79a and cd79b support for igm+ b cell fitness through b cell receptor surface expression. The Journal of Immunology, 209:2042-2053, Nov 2022. URL: https://doi.org/10.4049/jimmunol.2200144, doi:10.4049/jimmunol.2200144. This article has 76 citations.

18. (wang2024singlecellrnasequencing pages 1-2): Hong-Yan Wang, Jian-Yang Chen, Yanan Li, Xianghui Zhang, Xiang Liu, Yifang Lu, Hang He, Yubang Li, Hongxi Chen, Qun Liu, Yingyi Huang, Zhao Jia, Shuo Li, Yangqing Zhang, Shenglei Han, Shuhong Jiang, Mingming Yang, Yingying Zhang, Li Zhou, Fujian Tan, Qianyue Ji, Liang Meng, Rui Wang, Yuyan Liu, Kaiqiang Liu, Qian Wang, Inge Seim, Jun Zou, Guangyi Fan, Shanshan Liu, and Changwei Shao. Single-cell rna sequencing illuminates the ontogeny, conservation and diversification of cartilaginous and bony fish lymphocytes. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-51761-4, doi:10.1038/s41467-024-51761-4. This article has 18 citations and is from a highest quality peer-reviewed journal.

19. (chen2023multitissuescrnaseqreveals pages 5-6): Weijie Chen, Jianchang Huang, Wei Wang, Ying C Wang, and Dahai Yang. Multi-tissue scrna-seq reveals immune cell landscape of turbot (scophthalmus maximus). Developmental &amp; Comparative Immunology, 148:105032, Nov 2023. URL: https://doi.org/10.1016/j.dci.2023.105032, doi:10.1016/j.dci.2023.105032. This article has 38 citations and is from a peer-reviewed journal.

20. (OpenTargets Search: -CD79A,CD79B): Open Targets Query (-CD79A,CD79B, 10 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

21. (guslund2026igmmediatedprotectiondrives pages 1-2): Naomi Croft Guslund, Alexandra Jonsson, Anders K. Krabberød, Adrián López-Porras, Simen F. Nørstebø, Henning Sørum, Kjetill S. Jakobsen, Finn-Eirik Johansen, and Shuo-Wang Qiao. Igm-mediated protection drives early b-cell activation and mucosal containment of vibrio anguillarum in atlantic cod (gadus morhua). Frontiers in Immunology, Mar 2026. URL: https://doi.org/10.3389/fimmu.2026.1771403, doi:10.3389/fimmu.2026.1771403. This article has 0 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PTHR14334-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. tkachenko2023bcellreceptorsignaling pages 7-8
2. tkachenko2023bcellreceptorsignaling pages 8-10
3. tkachenko2023bcellreceptorsignaling pages 13-14
4. wang2024singlecellrnasequencing pages 1-2
5. xie2023astructuralplatform pages 1-2
6. reth2023discoveringimmunoreceptorcoupling pages 1-2
7. tkachenko2023bcellreceptorsignaling pages 3-5
8. lefranc2020immunoglobulinsorantibodies pages 6-9
9. tolar2022unveilingtheb pages 1-2
10. do2025dynamicsandactivation pages 1-4
11. tolar2022unveilingtheb pages 2-3
12. tkachenko2023bcellreceptorsignaling pages 5-7
13. tkachenko2023bcellreceptorsignaling pages 1-2
14. bhattacharyya2023combinationofhighresolution pages 2-4
15. tkachenko2023bcellreceptorsignaling pages 10-11
16. tkachenko2023bcellreceptorsignaling pages 11-13
17. chen2023multitissuescrnaseqreveals pages 5-6
18. guslund2026igmmediatedprotectiondrives pages 1-2
19. https://doi.org/10.1038/s41422-022-00724-9,
20. https://doi.org/10.3389/fimmu.2023.1253412,
21. https://doi.org/10.3390/ijms25010010,
22. https://doi.org/10.3390/biomedicines8090319,
23. https://doi.org/10.1126/science.add8065,
24. https://doi.org/10.1101/2024.07.10.602784,
25. https://doi.org/10.3390/cancers15112881,
26. https://doi.org/10.4049/jimmunol.2200144,
27. https://doi.org/10.1038/s41467-024-51761-4,
28. https://doi.org/10.1016/j.dci.2023.105032,
29. https://doi.org/10.3389/fimmu.2026.1771403,