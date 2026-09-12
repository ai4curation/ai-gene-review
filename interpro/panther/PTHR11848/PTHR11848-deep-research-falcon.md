---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T20:22:43.799756'
end_time: '2026-06-28T20:45:56.565163'
duration_seconds: 1392.77
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR11848
  interpro_name: TGF-BETA FAMILY
  interpro_short_name: Not specified
  interpro_type: family
  interpro_integrated: IPR015615
  member_databases: Not specified
  n_proteins: '35513'
  n_taxa: '7580'
  n_subfamilies: '71'
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
  path: PTHR11848-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR11848-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** PTHR11848
- **Name:** TGF-BETA FAMILY
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR015615
- **Member database signatures:** Not specified
- **Scale:** 35513 proteins across 7580 taxa, 71 subfamilies
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
**PTHR11848 (TGF-BETA FAMILY)**, structured to support GO annotation review.

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
- **Accession:** PTHR11848
- **Name:** TGF-BETA FAMILY
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR015615
- **Member database signatures:** Not specified
- **Scale:** 35513 proteins across 7580 taxa, 71 subfamilies
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
**PTHR11848 (TGF-BETA FAMILY)**, structured to support GO annotation review.

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


# Comprehensive Research Report: PTHR11848 (TGF-BETA FAMILY) — InterPro Family for GO Annotation Review

## 1. Family Definition and Biochemistry

### 1.1 Definition and Membership

PTHR11848 corresponds to the TGF-β (Transforming Growth Factor-Beta) superfamily, one of the largest and most functionally diverse families of secreted signaling proteins in metazoans. More than 60 TGF-β superfamily members have been identified across multicellular organisms, with 33 members encoded in the human genome (stepurko2023molecularinsightsinto pages 26-31, liu2022molecularevolutionof pages 1-2). The superfamily can be classified into TGF-βs, activins, inhibins, bone morphogenetic proteins (BMPs), growth and differentiation factors (GDFs), Nodals, Myostatins, MIS/AMH (Müllerian-inhibiting substance / Anti-Müllerian Hormone), and Lefty proteins (liu2022molecularevolutionof pages 1-2). PTHR11848 currently encompasses approximately 35,513 proteins across 7,580 taxa with 71 subfamilies, reflecting the pan-metazoan scope of this entry.

### 1.2 Conserved Structural Fold: The Cystine Knot

The defining structural feature of TGF-β superfamily members is the cystine knot motif in the mature signaling domain. This motif is composed of six core cysteine residues forming three intramolecular disulfide bonds with a characteristic topology: two disulfide bonds join distant parts of the polypeptide chain, while a third bond passes through the middle of the ring formed by the first two, creating a "knot" structure (stepurko2023molecularinsightsinto pages 44-48). Some subfamily members, including TGF-βs, inhibin β, myostatin/GDF-8, GDF-11, and GDF-15, possess two additional cysteines that link the thumb region to the N-terminus of the first β-strand, bringing the total to seven to nine cysteines in the mature domain (stepurko2023molecularinsightsinto pages 44-48). Despite sequence variation as low as ~30% between distant members (e.g., GDF15 versus TGF-β1), monomers from different subfamilies adopt remarkably similar three-dimensional backbone conformations with root mean square deviations of approximately 1 Å, and cystine knot domains overlay almost perfectly across subfamilies (stepurko2023molecularinsightsinto pages 44-48). Structural variations are concentrated in the heel/wrist region, thumb, and fingertips—regions critical for receptor and modulator binding (stepurko2023molecularinsightsinto pages 44-48). The three core cystine knot disulfides are essential for both structural stability and receptor binding; disruption of any one results in misfolding and loss of function (wieteska2026prodomaindependentfoldingand pages 7-10).

### 1.3 Signaling Mechanism

TGF-β superfamily members are synthesized as pre-proproteins that undergo proteolytic processing to release the mature signaling domain (liu2022molecularevolutionof pages 1-2, hachana2022tgfβsuperfamilysignaling pages 2-4). Mature ligands function as homodimers or heterodimers linked by an additional (seventh) cysteine-mediated interchain disulfide bond (xu2025theroleof pages 3-4). Signaling proceeds through transmembrane serine/threonine kinase receptor complexes composed of type I and type II receptors. Ligand binding to type II receptors leads to phosphorylation of type I receptors, which in turn activate downstream SMAD transcription factors. Two major signaling branches exist: TGF-β isoforms, activins, and Nodal activate SMAD2/3, while BMPs and most GDFs activate SMAD1/5/8 (stepurko2023molecularinsightsinto pages 26-31). Non-canonical (SMAD-independent) pathways including MAPK, PI3K/Akt, and Rho GTPase signaling are also activated by these ligands (cecerskaheryc2025tgfβsignalingin pages 2-4).

## 2. InterPro2GO Mapping Appropriateness

### 2.1 Current Status

PTHR11848 currently has **no InterPro2GO terms mapped**. This is a noteworthy and, as the analysis below demonstrates, well-justified absence.

### 2.2 Assessment of Candidate GO Terms

The following table evaluates candidate GO terms that might hypothetically be considered for this entry and explains why each is inappropriate for universal application:

| Candidate GO Term | GO ID (approximate) | Applicability Assessment | Problem Category | Recommendation |
|---|---|---|---|---|
| growth factor activity | GO:0008083 | Not safe for all PTHR11848 matches. Many members are bona fide secreted signaling ligands, but the family includes antagonistic or highly divergent members such as inhibins, Lefty proteins, and GDF15, whose activities are not well captured by a single generic growth-factor term across all taxa and subfamilies (xu2025theroleof pages 3-4, howard2022molecularmechanismsof pages 2-3, krill2024analysisofgrowth pages 23-25, filippini2025themultifacetedrole pages 4-6). | (a) subfamily-specific truth; (c) overly generic | REMOVE at parent-family level; if needed, move to more homogeneous child entries |
| cytokine activity | GO:0005125 | Too broad and not demonstrably universal for every match. TGF-β family members are often described as cytokines, but the superfamily spans developmental morphogens, endocrine ligands, antagonists, and highly divergent metabolic factors; applying this to all 35k proteins would over-generalize function (liu2022molecularevolutionof pages 1-2, stepurko2023molecularinsightsinto pages 44-48, hachana2022tgfβsuperfamilysignaling pages 2-4). | (c) overly generic; (a) not universally true | KEEP UNMAPPED at PTHR11848 |
| transforming growth factor beta receptor binding | GO:0005160 | Incorrect for the full family. Only a subset binds canonical TGF-β receptors; BMPs use distinct receptor combinations, AMH uses AMHR2 plus BMP-type receptors, and GDF15 signals through GFRAL rather than canonical type I/II TGF-β receptors (stepurko2023molecularinsightsinto pages 26-31, howard2022molecularmechanismsof pages 4-6, howard2022molecularmechanismsof pages 1-2, krill2024analysisofgrowth pages 23-25, filippini2025themultifacetedrole pages 20-21). | (a) only true for a subfamily | REMOVE from parent; reserve for true TGFB child families only |
| SMAD protein signal transduction | GO:0060395 | Not appropriate as a universal process term. Many family members do signal via SMADs, but through different branches (SMAD2/3 versus SMAD1/5/8), while some are antagonists (Lefty, inhibin) or use non-canonical receptor systems (GDF15-GFRAL) (stepurko2023molecularinsightsinto pages 26-31, howard2022molecularmechanismsof pages 4-6, cecerskaheryc2025tgfβsignalingin pages 2-4, krill2024analysisofgrowth pages 23-25, filippini2025themultifacetedrole pages 20-21). | (a) subfamily-specific; (b) whole-protein pathway term too broad for heterogeneous family | REMOVE / do not map at this level |
| extracellular space | GO:0005615 | Broadly plausible because most members are secreted extracellular ligands, but still not ideal for family-level GO because it is very generic and may not be consistently demonstrated for every predicted family match across deep metazoan taxa (howard2022molecularmechanismsof pages 2-3, liu2022molecularevolutionof pages 1-2, hachana2022tgfβsuperfamilysignaling pages 2-4). | (c) overly generic | KEEP_AS_NON_CORE at most; preferably leave unmapped |
| regulation of cell proliferation | GO:0042127 | Over-broad and unsafe. Some members inhibit proliferation, others promote it, and effects are tissue-, stage-, and ligand-dependent; even opposite effects are reported for TGF-β and BMP branches in different contexts (stepurko2023molecularinsightsinto pages 44-48, wu2024therolesand pages 16-17, liu2022molecularevolutionof pages 1-2). | (a) not universally true; process term too context-dependent | REMOVE / do not map at parent-family level |
| receptor ligand activity | GO:0048018 | Closer to a shared property than most candidates, but still not fully universal because antagonistic members and strongly divergent ligands complicate the claim that every family member functions as a cognate receptor-activating ligand in the same sense (cecerskaheryc2025tgfβsignalingin pages 2-4, krill2024analysisofgrowth pages 23-25, filippini2025themultifacetedrole pages 4-6). | (a) exceptions within family; (c) still broad | MODIFY-to-specific only on homogeneous child entries |
| signaling receptor binding | GO:0005102 | Broadly compatible with many ligands, but too nonspecific and still vulnerable to family exceptions and divergent receptor systems; conveys little review value for GO quality control (cecerskaheryc2025tgfβsignalingin pages 2-4, hachana2022tgfβsuperfamilysignaling pages 2-4, krill2024analysisofgrowth pages 23-25). | (c) overly generic | KEEP UNMAPPED at PTHR11848 |
| current state: no InterPro2GO term mapped | N/A | This is the most defensible state. The family is pan-metazoan, structurally conserved but functionally heterogeneous, including canonical TGF-βs, BMPs, activins/inhibins, AMH, Nodal/Lefty-related functions, and highly divergent GDF15; no reviewed GO term was found to be true for every match (liu2022molecularevolutionof pages 1-2, lo2022evolutionanddiversity pages 1-2, krill2024analysisofgrowth pages 23-25, lo2022evolutionanddiversity pages 7-9). | N/A | ACCEPT current no-mapping status |


*Table: This table evaluates plausible GO terms for the TGF-beta family entry PTHR11848 and explains why each would or would not be appropriate for all proteins matched by the family. It is useful for showing that the current absence of InterPro2GO mappings is likely the correct annotation decision.*

### 2.3 Key Justifications for the Absence of GO Mappings

Several lines of evidence support the conclusion that no GO term can be safely applied to all 35,513 proteins matched by PTHR11848:

- **Receptor usage is not universal.** Most members signal through canonical type I/II serine-threonine kinase receptors and SMADs, but GDF15 signals exclusively through GFRAL (a non-TGF-β receptor), sharing only ~30% sequence homology with other family members in the conserved domain (krill2024analysisofgrowth pages 23-25, filippini2025themultifacetedrole pages 4-6, filippini2025themultifacetedrole pages 20-21). AMH uses a unique dedicated type II receptor (AMHR2) found nowhere else in the family (howard2022molecularmechanismsof pages 2-3, howard2022molecularmechanismsof pages 1-2).

- **Not all members are agonists.** Lefty proteins function as antagonists of Nodal signaling (liu2022molecularevolutionof pages 1-2). Inhibins are αβ heterodimers that antagonize activin signaling rather than activating a canonical growth factor response (xu2025theroleof pages 3-4, hachana2022tgfβsuperfamilysignaling pages 2-4).

- **SMAD pathway branching.** The family splits into two fundamentally different SMAD branches: SMAD2/3 (TGF-β/activin/Nodal) versus SMAD1/5/8 (BMP/GDF). Annotating a single "SMAD protein signal transduction" term would obscure this critical functional distinction (stepurko2023molecularinsightsinto pages 26-31).

- **Opposing biological effects.** BMPs and TGF-βs have opposite functions in articular cartilage homeostasis (wu2024therolesand pages 16-17). TGF-β inhibits proliferation in many cell types while BMPs promote osteogenesis and differentiation (stepurko2023molecularinsightsinto pages 44-48, wu2024therolesand pages 16-17). No single biological process term could capture these opposing roles.

## 3. Functional Divergence Across the Family

### 3.1 Major Subfamilies and Their Distinct Functions

The TGF-β superfamily exhibits extreme functional heterogeneity across its constituent subfamilies:

| Subfamily | Representative Members | Primary SMAD Pathway | Key Biological Functions | Unique Features / Divergence |
|---|---|---|---|---|
| TGF-β | TGFB1, TGFB2, TGFB3 | Mainly SMAD2/3 via TGFBR1/ALK5-type signaling | Cytostasis/growth inhibition in many cell types, apoptosis or survival depending on context, fibrosis, immune regulation, tissue homeostasis (stepurko2023molecularinsightsinto pages 44-48, stepurko2023molecularinsightsinto pages 26-31, liu2022molecularevolutionof pages 1-2) | "True" TGF-β subfamily is deuterostome-specific rather than pan-metazoan; mature ligands are produced from latent complexes requiring regulated activation, unlike many other family members (liu2022molecularevolutionof pages 1-2) |
| BMP | BMP2-BMP15 | Mainly SMAD1/5/8 | Bone, cartilage, tooth, limb, vascular, and reproductive development; osteogenesis; tissue patterning and homeostasis (stepurko2023molecularinsightsinto pages 44-48, wu2024therolesand pages 16-17, hachana2022tgfβsuperfamilysignaling pages 2-4) | Largest ligand class in many summaries; can oppose TGF-β functions in some tissues, e.g. opposite roles in articular cartilage homeostasis (wu2024therolesand pages 16-17, hachana2022tgfβsuperfamilysignaling pages 2-4) |
| GDF | GDF1-GDF15 (excluding AMH/Lefty treated separately here) | Mixed: many GDFs use SMAD1/5/8; some are functionally specialized and non-canonical | Development, skeletal patterning, muscle mass control, metabolism, stress responses, reproduction (stepurko2023molecularinsightsinto pages 44-48, hachana2022tgfβsuperfamilysignaling pages 2-4, ganjoo2022bonemorphogeneticproteins pages 3-5) | Extreme internal diversity: myostatin/GDF8 inhibits muscle growth, GDF11 regulates development, and GDF15 is so divergent it is often treated separately (stepurko2023molecularinsightsinto pages 44-48, krill2024analysisofgrowth pages 23-25, filippini2025themultifacetedrole pages 4-6) |
| Activin | INHBA homodimer (Activin A), INHBB homodimer (Activin B), INHBA/INHBB heterodimer (Activin AB) | Mainly SMAD2/3 | Reproductive regulation including FSH stimulation, mesodermal/developmental signaling, proliferation/differentiation control, immune functions (xu2025theroleof pages 3-4, ganjoo2022bonemorphogeneticproteins pages 3-5) | Homodimeric/heterodimeric β-subunit ligands; functionally contrasted by inhibins, which antagonize activin signaling (xu2025theroleof pages 3-4, hachana2022tgfβsuperfamilysignaling pages 2-4) |
| Inhibin | Inhibin A (INHA+INHBA), Inhibin B (INHA+INHBB) | No single canonical ligand-specific SMAD output equivalent to activin; acts chiefly as activin antagonist | Endocrine/reproductive regulation, especially inhibition of FSH secretion (xu2025theroleof pages 3-4, hachana2022tgfβsuperfamilysignaling pages 2-4) | αβ heterodimers with antagonistic role toward activin; this alone makes blanket "growth factor activity" or single signaling GO terms unsafe for the whole family (xu2025theroleof pages 3-4, hachana2022tgfβsuperfamilysignaling pages 2-4) |
| AMH | AMH / MIS | BMP-like SMAD1/5/9 using ALK2/ALK3 with dedicated AMHR2 type II receptor | Reproductive tract development and ovarian reserve/ovarian function regulation (howard2022molecularmechanismsof pages 2-3, howard2022molecularmechanismsof pages 4-6, howard2022molecularmechanismsof pages 1-2) | Unique dedicated type II receptor AMHR2; largest prodomain in family; structurally distinct type I receptor interface despite using BMP-type SMAD outputs (howard2022molecularmechanismsof pages 2-3, howard2022molecularmechanismsof pages 4-6, howard2022molecularmechanismsof pages 1-2) |
| Nodal | NODAL | Mainly SMAD2/3 | Early embryonic patterning, mesoderm formation, left-right axis development (xu2025theroleof pages 3-4, hachana2022tgfβsuperfamilysignaling pages 2-4) | Developmentally restricted signaling role, not a general homeostasis/fibrosis ligand; strongly tied to vertebrate embryogenesis and left-right patterning networks (xu2025theroleof pages 3-4, hachana2022tgfβsuperfamilysignaling pages 2-4) |
| Lefty | LEFTY1, LEFTY2 | Not a standard agonist SMAD pathway; functions primarily as antagonist of Nodal/TGF-β-family signaling | Left-right patterning by restricting Nodal signaling (liu2022molecularevolutionof pages 1-2) | Antagonistic rather than agonistic behavior; a strong example that not all PTHR11848 members are receptor-activating ligands (liu2022molecularevolutionof pages 1-2) |
| GDF15 | GDF15 | Not canonical type I/type II receptor SMAD signaling; signals via GFRAL | Appetite/energy balance, cachexia-associated signaling, stress-response biology, disease biomarker roles (krill2024analysisofgrowth pages 23-25, filippini2025themultifacetedrole pages 4-6, filippini2025themultifacetedrole pages 2-4, filippini2025themultifacetedrole pages 20-21) | Highly divergent: only ~30% sequence homology to TGFβ1 in conserved domain and uses GFRAL rather than canonical TGF-β receptors; arguably a near single-member offshoot within the superfamily (krill2024analysisofgrowth pages 23-25, filippini2025themultifacetedrole pages 4-6, filippini2025themultifacetedrole pages 20-21) |


*Table: This table summarizes the major subfamilies within PTHR11848 and shows that they differ markedly in signaling mode, biology, and even receptor usage. The breadth of divergence supports the conclusion that broad family-level GO annotation would be unsafe or over-generalized.*

### 3.2 Neo-functionalization

Multiple clear examples of neo-functionalization have been documented:

**Nematode DAF-7 pathway diversification.** In the nematode *Pristionchus pacificus*, TGF-β pathway gene duplications have produced seven copies of the DAF-7 ligand, three copies of the DAF-4 receptor, and four copies of the DAF-3 Co-SMAD (lo2022evolutionanddiversity pages 7-9, lo2022evolutionanddiversity pages 1-2). These duplicated genes have acquired novel functions including regulation of phenotypically plastic mouth morphology, kin-recognition signaling, and cuticle development—none of which are associated with DAF-7 in *C. elegans* (lo2022evolutionanddiversity pages 1-2, lo2022evolutionanddiversity pages 9-11). Despite canonical association with dauer stage regulation in *C. elegans*, the DAF-7 pathway shows functional divergence across nematode species, with some losing the dauer-regulatory role entirely (lo2022evolutionanddiversity pages 7-9).

**GDF15 as a near-independent lineage.** GDF15 retains the cystine knot fold but shares only ~30% amino acid sequence homology with other family members and signals through GFRAL rather than canonical TGF-β receptors (krill2024analysisofgrowth pages 23-25, filippini2025themultifacetedrole pages 4-6). Its functions in appetite regulation, energy expenditure, and cachexia are mechanistically distinct from those of other superfamily members (filippini2025themultifacetedrole pages 2-4). GDF15 has been described as potentially warranting classification as a separate, single-member family (filippini2025themultifacetedrole pages 4-6).

**Parasitic mimics.** The helminth *Heligmosomoides polygyrus* produces TGM proteins that structurally mimic TGF-β receptor binding despite being built on a complement control protein scaffold rather than a cystine knot. These have neo-functionalized specifically for host immune suppression through Treg induction (mukundan2022convergentevolutionof pages 12-13).

### 3.3 Antagonistic Members

The family contains intrinsic antagonists that illustrate functional polarity within the superfamily. Inhibins (αβ heterodimers) antagonize activin (ββ homodimer) signaling—both are composed of shared subunits but have diametrically opposed effects on FSH secretion and reproductive physiology (xu2025theroleof pages 3-4). Lefty proteins similarly act as feedback inhibitors of Nodal signaling during left-right axis patterning (liu2022molecularevolutionof pages 1-2). These members cannot be accurately described by GO terms such as "growth factor activity" or "positive regulation of signaling."

## 4. Taxonomic Scope

### 4.1 Pan-Metazoan Distribution

TGF-β superfamily signaling is among the most ancient signaling pathways in Metazoa. Conserved members are present across essentially all metazoans studied (liu2022molecularevolutionof pages 1-2, lo2022evolutionanddiversity pages 1-2):

- **Sponges (Porifera):** Eight TGF-β ligands and five receptors identified (lo2022evolutionanddiversity pages 1-2).
- **Placozoans:** *Trichoplax adhaerens* has at least four receptors and four SMADs (lo2022evolutionanddiversity pages 1-2).
- **Nematodes:** *C. elegans* has five TGF-β family ligands organized into two main pathways (DAF-7 and DBL-1) (lo2022evolutionanddiversity pages 1-2, lo2022evolutionanddiversity pages 2-3).
- **Insects:** *Drosophila melanogaster* has seven TGF-β family members including Decapentaplegic (Dpp), Glass bottom boat (Gbb), and others (lo2022evolutionanddiversity pages 1-2, stepurko2023molecularinsightsinto pages 26-31).
- **Echinoderms:** Sea urchins and sea cucumbers contain conserved TGF-β ligands and receptors (nonkhwao2025characterizationandexpression pages 13-14).
- **Vertebrates:** 33 members in humans, with expansion through whole-genome duplication events (stepurko2023molecularinsightsinto pages 26-31, lo2022evolutionanddiversity pages 1-2).

### 4.2 Subfamily-Specific Taxonomic Restrictions

Critically, the "true" TGF-β subfamily (TGF-β1, β2, β3) is restricted to deuterostomes and is not found in protostomes or basal metazoans (liu2022molecularevolutionof pages 1-2). BMPs/GDFs were the first TGF-β superfamily members to emerge, followed by activins/inhibins; the TGF-β subfamily sensu stricto evolved later (liu2022molecularevolutionof pages 1-2). This means that any GO term specific to TGF-β isoform biology (e.g., latent complex activation, TGF-β-specific receptor binding) would be systematically incorrect for the thousands of invertebrate proteins in PTHR11848.

### 4.3 Functional Divergence Across Taxa

Even conserved pathway functions show significant variation across taxa. In nematodes, TGF-β signaling controls body size (DBL-1 pathway) and dauer formation/metabolism (DAF-7 pathway) (lo2022evolutionanddiversity pages 1-2, lo2022evolutionanddiversity pages 2-3), which are functions without direct vertebrate equivalents. In *Drosophila*, Dpp functions as a morphogen gradient for dorsal-ventral axis patterning. In vertebrates, TGF-β isoforms are primarily immunomodulatory and anti-proliferative (liu2022molecularevolutionof pages 1-2). This functional drift means that even broadly worded process terms like "regulation of cell proliferation" cannot be safely applied across all taxa.

## 5. Over-Annotation Verdict

### 5.1 Summary Assessment

The current state of **no InterPro2GO mappings** for PTHR11848 is **sound and appropriate**. This family-level PANTHER entry encompasses the entire TGF-β superfamily—a structurally unified but functionally profoundly heterogeneous collection of signaling ligands, antagonists, and divergent members spanning all Metazoa. The following factors converge to make any family-wide GO annotation unsound:

1. **Functional polarity:** The family includes both signaling agonists and intrinsic antagonists (inhibins vs. activins; Lefty vs. Nodal) (xu2025theroleof pages 3-4, liu2022molecularevolutionof pages 1-2).
2. **Divergent receptor systems:** GDF15 signals through GFRAL, AMH through dedicated AMHR2, and other members through various combinations of type I/II receptors (howard2022molecularmechanismsof pages 2-3, krill2024analysisofgrowth pages 23-25).
3. **Opposing SMAD pathways:** SMAD2/3 versus SMAD1/5/8 branches mediate fundamentally different transcriptional programs (stepurko2023molecularinsightsinto pages 26-31).
4. **Opposing biological outcomes:** BMPs and TGF-βs have opposite roles in cartilage homeostasis and other contexts (wu2024therolesand pages 16-17).
5. **Neo-functionalization:** Extensive gene duplication and neo-functionalization in nematodes and other lineages have generated novel functions not shared across the family (lo2022evolutionanddiversity pages 7-9, lo2022evolutionanddiversity pages 1-2, lo2022evolutionanddiversity pages 9-11).
6. **Taxonomic breadth:** Pan-metazoan distribution from sponges to humans, with different biological roles in different phyla (lo2022evolutionanddiversity pages 1-2).

### 5.2 Recommended GO Action Pattern

| Action | Recommendation |
|--------|---------------|
| **For PTHR11848 (parent family)** | **ACCEPT** the current no-mapping status. No GO term is universally valid for all matched proteins. |
| **For any proposed new GO terms** | **Do not add** molecular function, biological process, or cellular component terms at this level. |
| **For the 71 subfamilies** | GO terms should be mapped at the **subfamily level** (child entries) where functional homogeneity can be verified. For example, BMP-subfamily entries could receive "BMP signaling pathway" annotations; TGF-β-specific entries could receive "transforming growth factor beta receptor binding." |
| **Recommendation for InterPro** | Consider whether the parent PTHR11848 entry should be flagged as a structurally defined but functionally heterogeneous superfamily, encouraging curators to push GO annotations down to the 71 child subfamily entries where biological specificity can be maintained. |

In summary, the absence of InterPro2GO mappings for PTHR11848 is the correct annotation decision. The TGF-β superfamily is unified by its conserved cystine knot fold but encompasses such extreme functional diversity—from bone-inducing BMPs to growth-inhibiting TGF-βs, from reproductive inhibins to appetite-regulating GDF15, from developmental Nodal to its own antagonist Lefty—that no single GO term can accurately describe all 35,513 matched proteins across 7,580 taxa. Functional annotations should be delegated exclusively to the subfamily-level child entries.

References

1. (stepurko2023molecularinsightsinto pages 26-31): Molecular insights into signalling mechanisms within TGF-β superfamily This article has 1 citations.

2. (liu2022molecularevolutionof pages 1-2): Siqi Liu, Junfu Guo, Xianda Cheng, Wenna Li, Shuangyu Lyu, Xuanyi Chen, Qingwei Li, and Hao Wang. Molecular evolution of transforming growth factor-β (tgf-β) gene family and the functional characterization of lamprey tgf-β2. Frontiers in Immunology, Mar 2022. URL: https://doi.org/10.3389/fimmu.2022.836226, doi:10.3389/fimmu.2022.836226. This article has 34 citations and is from a peer-reviewed journal.

3. (stepurko2023molecularinsightsinto pages 44-48): Molecular insights into signalling mechanisms within TGF-β superfamily This article has 1 citations.

4. (wieteska2026prodomaindependentfoldingand pages 7-10): Łukasz Wieteska, Cynthia S. Hinck, Ananya Mukundan, Troy Krzysiak, Maarten van Dinther, Thibault Vantieghem, Rick M. Maizels, Peter ten Dijke, Caroline S. Hill, and Andrew P. Hinck. Pro-domain-dependent folding and co-receptor-mediated targeting to optimize an antagonistic tgf-β monomer for gene-based delivery. bioRxiv, Mar 2026. URL: https://doi.org/10.64898/2026.03.23.713733, doi:10.64898/2026.03.23.713733. This article has 0 citations.

5. (hachana2022tgfβsuperfamilysignaling pages 2-4): Soumaya Hachana and Bruno Larrivée. Tgf-β superfamily signaling in the eye: implications for ocular pathologies. Cells, 11:2336, Jul 2022. URL: https://doi.org/10.3390/cells11152336, doi:10.3390/cells11152336. This article has 109 citations.

6. (xu2025theroleof pages 3-4): Xinyi Xu, Jun Li, He Lin, Zhengyang Lin, and Guangcheng Ji. The role of tgf-β superfamily in endometriosis: a systematic review. Frontiers in Immunology, Aug 2025. URL: https://doi.org/10.3389/fimmu.2025.1638604, doi:10.3389/fimmu.2025.1638604. This article has 17 citations and is from a peer-reviewed journal.

7. (cecerskaheryc2025tgfβsignalingin pages 2-4): Elżbieta Cecerska-Heryć, Adrianna Jerzyk, Małgorzata Goszka, Aleksandra Polikowska, Julita Rachwalska, Natalia Serwin, Bartosz Wojciuk, and Barbara Dołęgowska. Tgf-β signaling in cancer: mechanisms of progression and therapeutic targets. International Journal of Molecular Sciences, 26:7326, Jul 2025. URL: https://doi.org/10.3390/ijms26157326, doi:10.3390/ijms26157326. This article has 44 citations.

8. (howard2022molecularmechanismsof pages 2-3): James A. Howard, Kaitlin N. Hart, and Thomas B. Thompson. Molecular mechanisms of amh signaling. Frontiers in Endocrinology, Jun 2022. URL: https://doi.org/10.3389/fendo.2022.927824, doi:10.3389/fendo.2022.927824. This article has 65 citations.

9. (krill2024analysisofgrowth pages 23-25): Moritz Johannes Krill. Analysis of growth differentiation factor 15 and its role in acute and chronic kidney injury. Dissertation, Jan 2024. URL: https://doi.org/10.5282/edoc.33996, doi:10.5282/edoc.33996. This article has 0 citations.

10. (filippini2025themultifacetedrole pages 4-6): Daria Maria Filippini, Donatella Romaniello, Francesca Carosi, Laura Fabbri, Andrea Carlini, Raffaele Giusti, Massimo Di Maio, Salvatore Alfieri, Mattia Lauriola, Maria Abbondanza Pantaleo, Lorena Arribas, Marc Oliva, Paolo Bossi, and Laura Deborah Locati. The multifaceted role of growth differentiation factor 15 (gdf15): a narrative review from cancer cachexia to target therapy. Biomedicines, 13:1931, Aug 2025. URL: https://doi.org/10.3390/biomedicines13081931, doi:10.3390/biomedicines13081931. This article has 11 citations.

11. (howard2022molecularmechanismsof pages 4-6): James A. Howard, Kaitlin N. Hart, and Thomas B. Thompson. Molecular mechanisms of amh signaling. Frontiers in Endocrinology, Jun 2022. URL: https://doi.org/10.3389/fendo.2022.927824, doi:10.3389/fendo.2022.927824. This article has 65 citations.

12. (howard2022molecularmechanismsof pages 1-2): James A. Howard, Kaitlin N. Hart, and Thomas B. Thompson. Molecular mechanisms of amh signaling. Frontiers in Endocrinology, Jun 2022. URL: https://doi.org/10.3389/fendo.2022.927824, doi:10.3389/fendo.2022.927824. This article has 65 citations.

13. (filippini2025themultifacetedrole pages 20-21): Daria Maria Filippini, Donatella Romaniello, Francesca Carosi, Laura Fabbri, Andrea Carlini, Raffaele Giusti, Massimo Di Maio, Salvatore Alfieri, Mattia Lauriola, Maria Abbondanza Pantaleo, Lorena Arribas, Marc Oliva, Paolo Bossi, and Laura Deborah Locati. The multifaceted role of growth differentiation factor 15 (gdf15): a narrative review from cancer cachexia to target therapy. Biomedicines, 13:1931, Aug 2025. URL: https://doi.org/10.3390/biomedicines13081931, doi:10.3390/biomedicines13081931. This article has 11 citations.

14. (wu2024therolesand pages 16-17): Mengrui Wu, Shali Wu, Wei Chen, and Yi-Ping Li. The roles and regulatory mechanisms of tgf-β and bmp signaling in bone and cartilage development, homeostasis and disease. Cell Research, 34:101-123, Jan 2024. URL: https://doi.org/10.1038/s41422-023-00918-9, doi:10.1038/s41422-023-00918-9. This article has 469 citations and is from a domain leading peer-reviewed journal.

15. (lo2022evolutionanddiversity pages 1-2): Wen-Sui Lo, Marianne Roca, Mohannad Dardiry, Marisa Mackie, Gabi Eberhardt, Hanh Witte, Ray Hong, Ralf J Sommer, and James W Lightfoot. Evolution and diversity of tgf-β pathways are linked with novel developmental and behavioral traits. Molecular Biology and Evolution, Dec 2022. URL: https://doi.org/10.1093/molbev/msac252, doi:10.1093/molbev/msac252. This article has 21 citations and is from a highest quality peer-reviewed journal.

16. (lo2022evolutionanddiversity pages 7-9): Wen-Sui Lo, Marianne Roca, Mohannad Dardiry, Marisa Mackie, Gabi Eberhardt, Hanh Witte, Ray Hong, Ralf J Sommer, and James W Lightfoot. Evolution and diversity of tgf-β pathways are linked with novel developmental and behavioral traits. Molecular Biology and Evolution, Dec 2022. URL: https://doi.org/10.1093/molbev/msac252, doi:10.1093/molbev/msac252. This article has 21 citations and is from a highest quality peer-reviewed journal.

17. (ganjoo2022bonemorphogeneticproteins pages 3-5): Shonik Ganjoo, Nahum Puebla-Osorio, Selene Nanez, Ethan Hsu, Tiffany Voss, Hampartsoum Barsoumian, Lisa K. Duong, James W. Welsh, and Maria Angelica Cortez. Bone morphogenetic proteins, activins, and growth and differentiation factors in tumor immunology and immunotherapy resistance. Frontiers in Immunology, Oct 2022. URL: https://doi.org/10.3389/fimmu.2022.1033642, doi:10.3389/fimmu.2022.1033642. This article has 14 citations and is from a peer-reviewed journal.

18. (filippini2025themultifacetedrole pages 2-4): Daria Maria Filippini, Donatella Romaniello, Francesca Carosi, Laura Fabbri, Andrea Carlini, Raffaele Giusti, Massimo Di Maio, Salvatore Alfieri, Mattia Lauriola, Maria Abbondanza Pantaleo, Lorena Arribas, Marc Oliva, Paolo Bossi, and Laura Deborah Locati. The multifaceted role of growth differentiation factor 15 (gdf15): a narrative review from cancer cachexia to target therapy. Biomedicines, 13:1931, Aug 2025. URL: https://doi.org/10.3390/biomedicines13081931, doi:10.3390/biomedicines13081931. This article has 11 citations.

19. (lo2022evolutionanddiversity pages 9-11): Wen-Sui Lo, Marianne Roca, Mohannad Dardiry, Marisa Mackie, Gabi Eberhardt, Hanh Witte, Ray Hong, Ralf J Sommer, and James W Lightfoot. Evolution and diversity of tgf-β pathways are linked with novel developmental and behavioral traits. Molecular Biology and Evolution, Dec 2022. URL: https://doi.org/10.1093/molbev/msac252, doi:10.1093/molbev/msac252. This article has 21 citations and is from a highest quality peer-reviewed journal.

20. (mukundan2022convergentevolutionof pages 12-13): Ananya Mukundan, Chang-Hyeock Byeon, Cynthia S. Hinck, Kyle Cunningham, Tiffany Campion, Danielle J. Smyth, Rick M. Maizels, and Andrew P. Hinck. Convergent evolution of a parasite-encoded complement control protein-scaffold to mimic binding of mammalian tgf-β to its receptors, tβri and tβrii. Journal of Biological Chemistry, 298:101994, Jun 2022. URL: https://doi.org/10.1016/j.jbc.2022.101994, doi:10.1016/j.jbc.2022.101994. This article has 29 citations and is from a domain leading peer-reviewed journal.

21. (lo2022evolutionanddiversity pages 2-3): Wen-Sui Lo, Marianne Roca, Mohannad Dardiry, Marisa Mackie, Gabi Eberhardt, Hanh Witte, Ray Hong, Ralf J Sommer, and James W Lightfoot. Evolution and diversity of tgf-β pathways are linked with novel developmental and behavioral traits. Molecular Biology and Evolution, Dec 2022. URL: https://doi.org/10.1093/molbev/msac252, doi:10.1093/molbev/msac252. This article has 21 citations and is from a highest quality peer-reviewed journal.

22. (nonkhwao2025characterizationandexpression pages 13-14): Siriporn Nonkhwao, Jarupa Charoenrit, Chanachon Ratanamungklanon, Lanlalin Sojikul, Supawadee Duangprom, Sineenart Songkoomkrong, Jirawat Saetan, Nipawan Nuemket, Prateep Amonruttanapun, Prasert Sobhon, and Napamanee Kornthong. Characterization and expression of tgf-β proteins and receptor in sea cucumber (holothuria scabra): insights into potential applications via molecular docking predictions. International Journal of Molecular Sciences, 26:6998, Jul 2025. URL: https://doi.org/10.3390/ijms26146998, doi:10.3390/ijms26146998. This article has 1 citations.

## Artifacts

- [Edison artifact artifact-00](PTHR11848-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR11848-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. liu2022molecularevolutionof pages 1-2
2. stepurko2023molecularinsightsinto pages 44-48
3. wieteska2026prodomaindependentfoldingand pages 7-10
4. xu2025theroleof pages 3-4
5. stepurko2023molecularinsightsinto pages 26-31
6. wu2024therolesand pages 16-17
7. lo2022evolutionanddiversity pages 7-9
8. filippini2025themultifacetedrole pages 2-4
9. filippini2025themultifacetedrole pages 4-6
10. mukundan2022convergentevolutionof pages 12-13
11. lo2022evolutionanddiversity pages 1-2
12. nonkhwao2025characterizationandexpression pages 13-14
13. howard2022molecularmechanismsof pages 2-3
14. krill2024analysisofgrowth pages 23-25
15. howard2022molecularmechanismsof pages 4-6
16. howard2022molecularmechanismsof pages 1-2
17. filippini2025themultifacetedrole pages 20-21
18. ganjoo2022bonemorphogeneticproteins pages 3-5
19. lo2022evolutionanddiversity pages 9-11
20. lo2022evolutionanddiversity pages 2-3
21. https://doi.org/10.3389/fimmu.2022.836226,
22. https://doi.org/10.64898/2026.03.23.713733,
23. https://doi.org/10.3390/cells11152336,
24. https://doi.org/10.3389/fimmu.2025.1638604,
25. https://doi.org/10.3390/ijms26157326,
26. https://doi.org/10.3389/fendo.2022.927824,
27. https://doi.org/10.5282/edoc.33996,
28. https://doi.org/10.3390/biomedicines13081931,
29. https://doi.org/10.1038/s41422-023-00918-9,
30. https://doi.org/10.1093/molbev/msac252,
31. https://doi.org/10.3389/fimmu.2022.1033642,
32. https://doi.org/10.1016/j.jbc.2022.101994,
33. https://doi.org/10.3390/ijms26146998,