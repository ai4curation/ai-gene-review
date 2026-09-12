---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T19:59:49.896621'
end_time: '2026-06-28T20:28:42.689676'
duration_seconds: 1732.79
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR10516
  interpro_name: FKBP-type Peptidyl-prolyl cis-trans Isomerase
  interpro_short_name: FKBP-type_PPIase
  interpro_type: family
  interpro_integrated: IPR050689
  member_databases: Not specified
  n_proteins: '9124'
  n_taxa: '10044'
  n_subfamilies: '26'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: The FKBP-type PPIase family is characterized by its peptidyl-prolyl
    cis-trans isomerase activity, which accelerates the folding of proteins by catalyzing
    the cis-trans isomerization of proline imidic peptide bonds in oligopeptides.
    Members of this family play a role in various cellular processes, including sexual
    development, TGF-beta receptor regulation, and modulation of calcium channel activity.
    They are also known for their interaction with immunosuppressive drugs, being
    inhibited by FK506 and rapamycin, which highlights their potential contribution
    to the pharmacological effects of these compounds.
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 26
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR10516-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR10516-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** PTHR10516
- **Name:** FKBP-type Peptidyl-prolyl cis-trans Isomerase
- **Short name:** FKBP-type_PPIase
- **Entry type:** family
- **Integrated into / parent:** IPR050689
- **Member database signatures:** Not specified
- **Scale:** 9124 proteins across 10044 taxa, 26 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The FKBP-type PPIase family is characterized by its peptidyl-prolyl cis-trans isomerase activity, which accelerates the folding of proteins by catalyzing the cis-trans isomerization of proline imidic peptide bonds in oligopeptides. Members of this family play a role in various cellular processes, including sexual development, TGF-beta receptor regulation, and modulation of calcium channel activity. They are also known for their interaction with immunosuppressive drugs, being inhibited by FK506 and rapamycin, which highlights their potential contribution to the pharmacological effects of these compounds.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR10516 (FKBP-type Peptidyl-prolyl cis-trans Isomerase)**, structured to support GO annotation review.

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
- **Accession:** PTHR10516
- **Name:** FKBP-type Peptidyl-prolyl cis-trans Isomerase
- **Short name:** FKBP-type_PPIase
- **Entry type:** family
- **Integrated into / parent:** IPR050689
- **Member database signatures:** Not specified
- **Scale:** 9124 proteins across 10044 taxa, 26 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The FKBP-type PPIase family is characterized by its peptidyl-prolyl cis-trans isomerase activity, which accelerates the folding of proteins by catalyzing the cis-trans isomerization of proline imidic peptide bonds in oligopeptides. Members of this family play a role in various cellular processes, including sexual development, TGF-beta receptor regulation, and modulation of calcium channel activity. They are also known for their interaction with immunosuppressive drugs, being inhibited by FK506 and rapamycin, which highlights their potential contribution to the pharmacological effects of these compounds.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR10516 (FKBP-type Peptidyl-prolyl cis-trans Isomerase)**, structured to support GO annotation review.

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


# Comprehensive Research Report: PTHR10516 — FKBP-type Peptidyl-Prolyl cis-trans Isomerase Family

## GO Annotation Review for InterPro Entry PTHR10516

---

## 1. Family Definition and Biochemistry

### 1.1 Structural Fold

The FKBP (FK506-Binding Protein) family is defined by a characteristic fold consisting of a five-stranded antiparallel β-sheet wrapped around a short α-helix. A shallow groove between the α-helix and β-sheets forms a solvent-exposed active site that binds the target proline residue (dunyak2016peptidylprolineisomerases(ppiases) pages 2-3). The minimal FKBP fold consists of secondary structure elements in the arrangement β4–β5a–β5b–α–β2–β3, with additional structural variation among subfamilies (maruyama2004archaealpeptidylprolyl pages 7-8, maruyama2004archaealpeptidylprolyl pages 8-11). In archaeal FKBPs, the fold can include insertion sequences in the flap and bulge regions that form additional subdomains with hydrophobic surfaces (maruyama2004archaealpeptidylprolyl pages 8-11). The prototype structure is human FKBP12 (12 kDa), which consists solely of the PPIase domain (dunyak2016peptidylprolineisomerases(ppiases) pages 2-3).

### 1.2 Conserved Catalytic and Binding Residues

Key active site residues in FKBP12 include Trp59, which sits at the base of the catalytic cleft and plays a central structural and dynamic role (lemaster2016conformationaldynamicsin pages 19-20, lemaster2016conformationaldynamicsin pages 17-19, lemaster2016conformationaldynamicsin pages 8-9). The aromatic residues Phe36, Phe48, and Phe99 line the walls of the catalytic cleft cavity (lemaster2016conformationaldynamicsin pages 17-19). Mutagenesis experiments have implicated Asp37 and His87 in forming the hydrogen bond network between the binding pocket and bound substrate (dunyak2016peptidylprolineisomerases(ppiases) pages 2-3). Tyr82 packs tightly against Trp59, and the conformational dynamics of the Trp59 indole ring are allosterically coupled to the 50s loop backbone (lemaster2016conformationaldynamicsin pages 8-9). Notably, FKBP12.6, the closest paralog (85% identity), substitutes Phe59 for Trp59, disrupting conformational coupling (lemaster2016conformationaldynamicsin pages 8-9).

### 1.3 Catalytic Mechanism

FKBP-type PPIases catalyze the cis-trans isomerization of peptidyl-prolyl imide bonds in oligopeptides, a rate-limiting step in protein folding (zgajnar2019biologicalactionsof pages 1-3). The mechanism involves hydrogen bonding networks between the active site floor residues and the proline backbone, supported by hydrophobic interactions. FK506 and rapamycin bind noncovalently to FKBP12 in a broad pocket that includes Trp59, inhibiting PPIase activity (kolos2018fkbpligands—wherewe pages 2-4). Catalytic efficiencies of archaeal FKBPs (e.g., MtFKBP17 and TcFKBP18) reach ~350 mM⁻¹s⁻¹ against tetrapeptide substrates (maruyama2004archaealpeptidylprolyl pages 7-8).

---

## 2. InterPro2GO Mapping Appropriateness

**Current status: No InterPro2GO terms are mapped to PTHR10516.**

This is a notable finding. Despite the family name suggesting universal PPIase activity, the absence of GO mappings at this broad family level is well-justified by the evidence. The following table evaluates candidate GO terms that could theoretically be mapped:

| Candidate GO Term | GO ID | Universally True for All Members? | Assessment | Recommendation |
|---|---|---|---|---|
| peptidyl-prolyl cis-trans isomerase activity | GO:0003755 | No | Core family biochemistry is PPIase activity, but it is not universal across the whole PTHR10516 family because several FKBP-like members are catalytically inactive or conditionally active, including AIPL1 (no detectable PPIase activity), the FK2 domains of FKBP51/52 (inactive), and FKBP38 (normally inactive, Ca2+/CaM-regulated). Applying this term to all 9124 matches would over-annotate pseudoenzymes and divergent signaling/chaperone subfamilies. (dunyak2016peptidylprolineisomerases(ppiases) pages 2-3, kolos2018fkbpligands—wherewe pages 5-6, kolos2018fkbpligands—wherewe pages 16-17, zgajnar2019biologicalactionsof pages 1-3) | MODIFY-to-specific: map only to catalytically validated child families/subfamilies, not the parent family |
| protein folding | GO:0006457 | No | Many FKBPs assist folding or act as chaperones, including ER FKBPs and archaeal FKBP proteins with folding/anti-aggregation activity, but this is not demonstrated or necessarily primary for all members; some are specialized for signaling, receptor regulation, meiosis, collagen biosynthesis, or retina-specific PDE6 chaperoning. The process term is therefore too broad for the full family. (kolos2018fkbpligands—wherewe pages 5-6, maruyama2004archaealpeptidylprolyl pages 1-2, maruyama2004archaealpeptidylprolyl pages 3-4, dunyak2016peptidylprolineisomerases(ppiases) pages 2-3) | MODIFY-to-specific or KEEP_AS_NON_CORE only for validated folding/chaperone subfamilies |
| FK506 binding | GO:0005528 | No | FKBP12 and several canonical FKBPs bind FK506/rapamycin, but not all family members do so detectably; some are better considered FKBP-like proteins and some inactive domains do not bind FK506 well or at all. This property varies strongly across subfamilies and should not be generalized to the parent family. (tong2016fk506bindingproteinsand pages 1-2, kolos2018fkbpligands—wherewe pages 16-17, dunyak2016peptidylprolineisomerases(ppiases) pages 3-5, maruyama2004archaealpeptidylprolyl pages 3-4) | MODIFY-to-specific: restrict to experimentally supported FK506-binding subfamilies |
| cytoplasm | GO:0005737 | No | Family members occupy diverse compartments: cytosol, nucleus, ER lumen, sarcoplasmic/endoplasmic reticulum-associated complexes, mitochondria, and membranes. A universal cytoplasmic assignment would be wrong across eukaryotic secretory-pathway, membrane-anchored, and nuclear FKBPs, and would also be poor across broad bacterial/archaeal diversity. (kolos2018fkbpligands—wherewe pages 5-6, zgajnar2019biologicalactionsof pages 1-3, kolos2018fkbpligands—wherewe pages 4-5, tong2016fk506bindingproteinsand pages 2-3, tong2016fk506bindingproteinsand pages 3-5) | REMOVE / do not map at parent family level |
| peptide binding | GO:0042277 | No | The PPIase active site engages peptide substrates in many catalytic FKBPs, so peptide interaction is mechanistically plausible for a large fraction of members; however, this is not established for all divergent or catalytically dead members, and the term would still overstate universality across pseudoenzymes and highly specialized scaffolds. It is also relatively generic. (dunyak2016peptidylprolineisomerases(ppiases) pages 2-3, maruyama2004archaealpeptidylprolyl pages 3-4, zgajnar2019biologicalactionsof pages 1-3) | KEEP_AS_NON_CORE at most; preferably map only to catalytic child entries if used |
| protein binding | GO:0005515 | No | Protein interaction is widespread in the family (RyR, IP3R, TGFβ receptors, Hsp90, Bcl-2, collagen machinery, PDE6), but the term is too generic to be informative and does not capture family-wide specificity. It also risks becoming a low-value annotation applied to a very heterogeneous family. (kolos2018fkbpligands—wherewe pages 5-6, zgajnar2019biologicalactionsof pages 1-3, g�thel1999peptidylprolylcistransisomerases pages 4-6, tong2016fk506bindingproteinsand pages 3-5) | KEEP_AS_NON_CORE or avoid mapping because it is uninformative/generic |


*Table: This table evaluates candidate GO terms for the broad PTHR10516 FKBP-type PPIase family and shows why most terms are not safe to apply to every matched protein. It is useful for deciding whether the current absence of InterPro2GO mappings should be maintained at the parent family level.*

### Assessment of Key Candidate Terms

**GO:0003755 (peptidyl-prolyl cis-trans isomerase activity):** While this is the defining biochemistry of the family, it cannot be applied universally. Multiple members are catalytically dead (AIPL1) or normally inactive (FKBP38), and some possess PPIase-like domains with no measurable activity (FK2 domains of FKBP51/52) (dunyak2016peptidylprolineisomerases(ppiases) pages 2-3, kolos2018fkbpligands—wherewe pages 5-6). Many FKBPs do not bind FK506 well and are better described as "FKBP-like" proteins (kolos2018fkbpligands—wherewe pages 16-17).

**GO:0006457 (protein folding):** While many members participate in protein folding, others are specialized for signaling (FKBP12 on calcium channels), meiosis (FKBP6), or retinal PDE6 chaperoning (AIPL1), making this term subfamily-specific rather than family-wide (kolos2018fkbpligands—wherewe pages 5-6, galat2019compressionoflarge pages 15-16).

**GO:0005528 (FK506 binding):** Not all members bind FK506 detectably, and the term would over-annotate the family (kolos2018fkbpligands—wherewe pages 16-17, tong2016fk506bindingproteinsand pages 1-2).

**GO:0005737 (cytoplasm):** Members localize to diverse compartments—cytosol, nucleus, ER lumen, mitochondria, and membranes—making any single compartment term inappropriate (kolos2018fkbpligands—wherewe pages 5-6, kolos2018fkbpligands—wherewe pages 4-5, tong2016fk506bindingproteinsand pages 3-5).

---

## 3. Functional Divergence Across the Family

The FKBP family displays extreme functional divergence, with 26 recognized subfamilies encompassing 9,124 proteins across 10,044 taxa. The following table documents this divergence comprehensively:

| FKBP Member | Domain Architecture | PPIase Activity Status | Primary Function | Subcellular Localization | Key Distinguishing Features |
|---|---|---|---|---|---|
| FKBP12 (FKBP1A) | Single FKBP/PPIase domain | Active | Prolyl isomerase; regulates ryanodine receptor, IP3 receptor, TGF-β/activin receptor signaling; mediates FK506/rapamycin-dependent ternary complexes with calcineurin or mTOR | Cytosol; associated with SR/ER membrane receptors | Prototype small FKBP; drug-binding immunophilin; receptor-regulatory roles can be PPIase-independent (g�thel1999peptidylprolylcistransisomerases pages 4-6, tong2016fk506bindingproteinsand pages 2-3, kolos2018fkbpligands—wherewe pages 2-4) |
| FKBP12.6 (FKBP1B) | Single FKBP/PPIase domain | Active | Regulation of Ca2+ release channels, especially cardiac RyR2 | Cytosol; sarcoplasmic reticulum-associated | Closest FKBP12 paralog; preferentially targets RyR2 over RyR1 (kolos2018fkbpligands—wherewe pages 4-5, tong2016fk506bindingproteinsand pages 3-5) |
| FKBP13 (FKBP2) | Single FKBP/PPIase domain plus ER targeting/retention features | Active | ER chaperone in protein folding and immunoglobulin/secretory protein processing | Endoplasmic reticulum lumen | ER-localized small FKBP; specialized in secretory pathway proteostasis (kolos2018fkbpligands—wherewe pages 5-6, kolos2018fkbpligands—wherewe pages 4-5) |
| FKBP25 (FKBP3) | N-terminal basic tilted helix bundle + C-terminal FKBP/PPIase domain | Active | Nuclear protein folding/scaffolding; interactions with DNA, RNA, histone deacetylases, MDM2; microtubule-associated functions | Nucleus | Gains nucleic-acid and chromatin-linked functions beyond classical PPIase role (kolos2018fkbpligands—wherewe pages 5-6, kolos2018fkbpligands—wherewe pages 4-5) |
| FKBP38 (FKBP8) | Single FKBP-like domain + 3 TPR domains + Ca2+/calmodulin-responsive region + C-terminal transmembrane segment | Normally inactive; conditionally activatable by Ca2+/CaM | Regulation of mTOR, apoptosis-related proteins such as Bcl-2/Bcl-xL | ER and mitochondrial membranes | Membrane-anchored FKBP; unusual Ca2+/CaM-dependent activation; major neo-functionalization away from constitutive PPIase activity (zgajnar2019biologicalactionsof pages 1-3, tong2016fk506bindingproteinsand pages 3-5, dunyak2016peptidylprolineisomerases(ppiases) pages 2-3) |
| FKBP51 (FKBP5) | FK1 active PPIase domain + FK2 inactive PPIase-like domain + TPR domain | FK1 active; FK2 inactive | Hsp90 co-chaperone; steroid receptor regulation; stress, metabolism, transcription, tau biology | Cytosol, nucleus, mitochondria | Often opposes FKBP52 in steroid receptor signaling; functional divergence traced partly to FK domains and dynamics (zgajnar2019biologicalactionsof pages 1-3, galat2019compressionoflarge pages 15-16, dunyak2016peptidylprolineisomerases(ppiases) pages 3-5, dunyak2016peptidylprolineisomerases(ppiases) pages 2-3) |
| FKBP52 (FKBP4) | FK1 active PPIase domain + FK2 inactive PPIase-like domain + TPR domain | FK1 active; FK2 inactive | Hsp90 co-chaperone; positive regulator of steroid hormone receptor maturation/trafficking; roles in cytoskeleton and signaling | Cytosol and nucleus | Closely related to FKBP51 but often exerts opposite effects on steroid receptor pathways (zgajnar2019biologicalactionsof pages 1-3, dunyak2016peptidylprolineisomerases(ppiases) pages 3-5, dunyak2016peptidylprolineisomerases(ppiases) pages 2-3) |
| FKBP65 (FKBP10) | Multiple FKBP/PPIase domains + ER signal peptide/retention features | Active | Collagen biosynthesis, folding, and cross-linking; regulation of lysyl hydroxylase 2-associated collagen stability | Endoplasmic reticulum lumen | Specialized secretory-pathway FKBP for extracellular matrix biogenesis (kolos2018fkbpligands—wherewe pages 5-6, tong2016fk506bindingproteinsand pages 2-3) |
| FKBP6 (FKBP36) | FKBP-like family member; additional domains not detailed in retrieved evidence | Divergent/uncertain; family member with specialized noncanonical role | Male fertility and homologous chromosome pairing during meiosis | Nucleus/meiotic cells (functional inference from meiosis role) | Example of strong specialization beyond generic folding catalyst function (galat2019compressionoflarge pages 15-16) |
| AIPL1 | FKBP-like domain with specialized prenyl-binding properties + additional chaperone-related regions | Catalytically dead / no PPIase activity | Obligatory chaperone for PDE6 in retinal neurons | Retina/photoreceptor cells | Pseudo-enzyme within FKBP family; binds farnesyl/geranyl groups rather than acting as an isomerase (kolos2018fkbpligands—wherewe pages 5-6) |
| Bacterial SlyD-type FKBPs | FKBP/PPIase domain often linked to accessory domains (e.g., metal-binding/chaperone modules in known SlyD proteins) | Active | Protein folding/chaperoning in bacteria | Cytosol | Bacterial expansion of FKBP scaffold into multi-domain chaperones; demonstrates non-eukaryotic breadth of family (galat2000sequencediversificationof pages 5-6, galat2000sequencediversificationof pages 2-3, maruyama2000archaealpeptidylprolyl pages 5-8) |
| Bacterial FkpA/Mip-type FKBPs | FKBP/PPIase domain within larger periplasmic or membrane-associated proteins | Active in representative members | Chaperone/PPIase functions, often in envelope or virulence-associated contexts | Typically periplasmic or membrane-associated in bacteria | Shows family members can be adapted for bacterial envelope biology rather than eukaryotic signaling (anchal2021distributionofpeptidylprolyl pages 13-14, maruyama2004archaealpeptidylprolyl pages 3-4) |
| Archaeal short-type FKBPs | Small FKBP domain with archaeal-specific insertions in flap/bulge regions | Active; also chaperone-like | Prolyl isomerization and independent chaperone-like anti-aggregation/refolding functions | Cytosol | Short archaeal FKBPs can couple PPIase and chaperone-like activities; chaperone function can be independent of catalytic activity (maruyama2004archaealpeptidylprolyl pages 1-2, maruyama2000archaealpeptidylprolyl pages 5-8) |
| Archaeal long-type FKBPs | FKBP core plus ~100 aa C-terminal extension; archaeal-specific insertions | Active | Prolyl isomerization; likely protein-folding support in archaeal proteostasis | Cytosol | Present across major archaeal phyla; exemplify archaeal lineage-specific elaboration of FKBP architecture (maruyama2004archaealpeptidylprolyl pages 1-2, anchal2021distributionofpeptidylprolyl pages 13-14, maruyama2000archaealpeptidylprolyl pages 5-8) |


*Table: This table summarizes how major FKBP subfamily members differ in domain architecture, catalytic status, localization, and biological role. It is useful for GO review because it makes clear that the family contains active enzymes, conditionally active proteins, and pseudo-enzymes with highly specialized functions.*

### 3.1 Catalytically Dead (Pseudo-enzyme) Members

**AIPL1:** Harbors an FKBP-like domain but is completely devoid of PPIase activity. Instead, it functions as an obligatory chaperone for phosphodiesterase 6 (PDE6) in retinal neurons, with its FKBP-like domain binding farnesyl and geranyl moieties. Mutations cause Leber congenital amaurosis (kolos2018fkbpligands—wherewe pages 5-6).

**FK2 domains of FKBP51/FKBP52:** These second PPIase-like domains do not bind FK506 or rapamycin and have no measurable isomerase activity in vitro (dunyak2016peptidylprolineisomerases(ppiases) pages 2-3).

**FKBP38:** Its PPIase domain is normally inactive but can be conditionally activated by Ca²⁺/calmodulin binding, which releases an autoinhibitory N-terminal region (dunyak2016peptidylprolineisomerases(ppiases) pages 2-3, tong2016fk506bindingproteinsand pages 3-5).

**FKBP37/PP5:** Negligible or absent PPIase enzymatic activity (zgajnar2019biologicalactionsof pages 1-3).

### 3.2 Neo-functionalization and Opposing Functions

**FKBP51 vs. FKBP52:** Despite sharing ~70% sequence identity, these paralogs exert opposite effects on steroid hormone receptors. FKBP52 positively regulates androgen, glucocorticoid, and progesterone receptors, while FKBP51 acts as a negative regulator. This functional divergence has been traced to differences in the dynamics of the FK1 domain (dunyak2016peptidylprolineisomerases(ppiases) pages 3-5, zgajnar2019biologicalactionsof pages 1-3).

**FKBP6 (FKBP36):** Plays an essential role in male fertility and homologous chromosome pairing during meiosis, representing strong functional specialization far from generic PPIase activity (galat2019compressionoflarge pages 15-16).

**FKBP25:** A nuclear protein that interacts with histone deacetylases, DNA, RNA, and MDM2, with roles in lung cancer proliferation and microtubule-associated functions (kolos2018fkbpligands—wherewe pages 5-6, kolos2018fkbpligands—wherewe pages 4-5).

**FKBP65/FKBP19/FKBP22:** Specialized for collagen biosynthesis, showing substrate specificity for hydroxylated proteins and participation in collagen cross-linking (kolos2018fkbpligands—wherewe pages 5-6).

### 3.3 Chaperone Activities Independent of PPIase

Archaeal short-type FKBPs from *Methanococcus thermolithotrophicus* demonstrate both PPIase activity and chaperone-like activity (anti-aggregation and refolding assistance). Mutational analysis revealed that chaperone activity is independent of PPIase activity, with insertion sequences in the flap region being functionally important for chaperone function (maruyama2004archaealpeptidylprolyl pages 1-2).

---

## 4. Taxonomic Scope

FKBP-type PPIases are ubiquitous across all three domains of life:

**Bacteria:** *E. coli* contains four FKBP isoforms, and FKBPs are found across diverse phyla including Proteobacteria, Firmicutes, and Actinobacteria. Bacterial FKBPs include several structural types: FkpA, FkpB, SlyD, trigger factors, and Mip-type proteins (galat2000sequencediversificationof pages 3-5, galat2000sequencediversificationof pages 2-3, anchal2021distributionofpeptidylprolyl pages 13-14).

**Archaea:** FKBPs are present in all five major archaeal phyla (Euryarchaeota, Thaumarchaeota, Crenarchaeota, Nanoarchaeota, and Korarchaeota). A study of 196 archaeal genomes identified 325 FKBP sequences. Archaeal FKBPs exist as short-type (17–18 kDa) and long-type (26–30 kDa) forms belonging to the SlpA superfamily (anchal2021distributionofpeptidylprolyl pages 13-14, maruyama2000archaealpeptidylprolyl pages 5-8, maruyama2004archaealpeptidylprolyl pages 1-2).

**Eukaryotes:** *S. cerevisiae* has 4 FKBPs, *Arabidopsis thaliana* has 7, *C. elegans* has 6, and the human genome encodes at least 15 FKBP polypeptides (galat2000sequencediversificationof pages 3-5, tong2016fk506bindingproteinsand pages 1-2). Homologues of cytosolic FKBP12 and membrane-associated FKBP13 have been found in all eukaryotes investigated (galat2000sequencediversificationof pages 6-7).

Given this pan-life distribution across 10,044 taxa, any mapped biological process term describing a eukaryote-specific pathway (e.g., "sexual development," "TGF-beta receptor regulation," "calcium channel activity modulation") would systematically over-annotate the vast majority of prokaryotic members that cannot participate in those pathways.

---

## 5. Over-Annotation Verdict and Recommendations

### 5.1 Summary Assessment

The current state of PTHR10516—**no InterPro2GO terms mapped**—is **appropriate and should be maintained** at the parent family level. The FKBP-type PPIase family is a textbook example of a functionally heterogeneous protein family where:

1. **Not all members are catalytically active.** AIPL1 is a pseudo-enzyme; FK2 domains of FKBP51/52 are inactive; FKBP38 is conditionally active; FKBP37/PP5 have negligible activity (dunyak2016peptidylprolineisomerases(ppiases) pages 2-3, kolos2018fkbpligands—wherewe pages 5-6, zgajnar2019biologicalactionsof pages 1-3).

2. **Active members serve radically different biological roles.** FKBP12 regulates calcium channels and TGFβ receptors; FKBP51/52 modulate steroid receptor signaling with opposite effects; FKBP65 participates in collagen biosynthesis; FKBP6 is essential for meiosis; FKBP25 is a nuclear DNA/RNA-binding protein (kolos2018fkbpligands—wherewe pages 5-6, kolos2018fkbpligands—wherewe pages 4-5, galat2019compressionoflarge pages 15-16, tong2016fk506bindingproteinsand pages 2-3, dunyak2016peptidylprolineisomerases(ppiases) pages 3-5).

3. **Subcellular localizations are diverse.** Members reside in the cytosol, nucleus, ER lumen, mitochondrial membranes, and plasma membrane-associated complexes (kolos2018fkbpligands—wherewe pages 5-6, kolos2018fkbpligands—wherewe pages 4-5, tong2016fk506bindingproteinsand pages 3-5).

4. **The family spans all domains of life** (bacteria, archaea, and eukaryotes), making any eukaryote-specific process term (e.g., "TGF-beta receptor regulation") inapplicable to the majority of matched proteins (galat2000sequencediversificationof pages 6-7, galat2000sequencediversificationof pages 3-5, anchal2021distributionofpeptidylprolyl pages 13-14).

### 5.2 Recommended GO Action Pattern

| Recommendation | Justification |
|---|---|
| **ACCEPT** the current absence of InterPro2GO terms at the PTHR10516 parent family level | The family is too functionally heterogeneous for any GO term to be universally true |
| **MODIFY-to-specific** for child entries / subfamilies | GO:0003755 (PPIase activity) should be mapped only to catalytically validated subfamilies. GO:0005528 (FK506 binding) should be restricted to experimentally confirmed FK506-binding clades |
| **KEEP_AS_NON_CORE** for any future generic terms | GO:0005515 (protein binding) and GO:0042277 (peptide binding) are too uninformative to add value |
| **REMOVE / do not add** compartment terms at parent level | GO:0005737 (cytoplasm) and any other localization terms are demonstrably wrong for significant fractions of the family |

### 5.3 Recommendations for InterPro

The 26 recognized subfamilies within PTHR10516 should be leveraged for GO annotation. Specifically:
- **PPIase activity (GO:0003755)** and **protein folding (GO:0006457)** should be pushed down to the subset of subfamilies with experimentally validated catalytic activity (e.g., FKBP12-like, FKBP13-like, FKBP25-like subfamilies).
- **Subfamilies containing pseudo-enzymes** (AIPL1-like) or conditionally active members (FKBP38-like) should be explicitly excluded from PPIase activity mappings.
- The InterPro description for PTHR10516 itself mentions "sexual development, TGF-beta receptor regulation, and modulation of calcium channel activity"—these are subfamily-specific functions that should not be generalized to the parent entry and could be moved to appropriate child entries.

**Overall verdict: The current absence of InterPro2GO mappings for PTHR10516 is SOUND. No new terms should be added at the parent family level. GO annotations should be applied at the subfamily level where functional homogeneity can be verified.**

References

1. (dunyak2016peptidylprolineisomerases(ppiases) pages 2-3): Bryan M. Dunyak and Jason E. Gestwicki. Peptidyl-proline isomerases (ppiases): targets for natural products and natural product-inspired compounds. Journal of medicinal chemistry, 59 21:9622-9644, Jul 2016. URL: https://doi.org/10.1021/acs.jmedchem.6b00411, doi:10.1021/acs.jmedchem.6b00411. This article has 161 citations and is from a highest quality peer-reviewed journal.

2. (maruyama2004archaealpeptidylprolyl pages 7-8): T. Maruyama, R. Suzuki, and M. Furutani. Archaeal peptidyl prolyl cis-trans isomerases (ppiases) update 2004. Frontiers in bioscience : a journal and virtual library, 9:1680-720, May 2004. URL: https://doi.org/10.2741/1361, doi:10.2741/1361. This article has 59 citations.

3. (maruyama2004archaealpeptidylprolyl pages 8-11): T. Maruyama, R. Suzuki, and M. Furutani. Archaeal peptidyl prolyl cis-trans isomerases (ppiases) update 2004. Frontiers in bioscience : a journal and virtual library, 9:1680-720, May 2004. URL: https://doi.org/10.2741/1361, doi:10.2741/1361. This article has 59 citations.

4. (lemaster2016conformationaldynamicsin pages 19-20): David M. LeMaster and Griselda Hernandez. Conformational dynamics in fkbp domains: relevance to molecular signaling and drug design. Current molecular pharmacology, 9 1:5-26, Dec 2016. URL: https://doi.org/10.2174/1874467208666150519113146, doi:10.2174/1874467208666150519113146. This article has 15 citations and is from a peer-reviewed journal.

5. (lemaster2016conformationaldynamicsin pages 17-19): David M. LeMaster and Griselda Hernandez. Conformational dynamics in fkbp domains: relevance to molecular signaling and drug design. Current molecular pharmacology, 9 1:5-26, Dec 2016. URL: https://doi.org/10.2174/1874467208666150519113146, doi:10.2174/1874467208666150519113146. This article has 15 citations and is from a peer-reviewed journal.

6. (lemaster2016conformationaldynamicsin pages 8-9): David M. LeMaster and Griselda Hernandez. Conformational dynamics in fkbp domains: relevance to molecular signaling and drug design. Current molecular pharmacology, 9 1:5-26, Dec 2016. URL: https://doi.org/10.2174/1874467208666150519113146, doi:10.2174/1874467208666150519113146. This article has 15 citations and is from a peer-reviewed journal.

7. (zgajnar2019biologicalactionsof pages 1-3): Nadia Zgajnar, Sonia De Leo, Cecilia Lotufo, Alejandra Erlejman, Graciela Piwien-Pilipuk, and Mario Galigniana. Biological actions of the hsp90-binding immunophilins fkbp51 and fkbp52. Biomolecules, 9:52, Feb 2019. URL: https://doi.org/10.3390/biom9020052, doi:10.3390/biom9020052. This article has 128 citations.

8. (kolos2018fkbpligands—wherewe pages 2-4): Jürgen M. Kolos, Andreas M. Voll, Michael Bauder, and Felix Hausch. Fkbp ligands—where we are and where to go? Frontiers in Pharmacology, Dec 2018. URL: https://doi.org/10.3389/fphar.2018.01425, doi:10.3389/fphar.2018.01425. This article has 198 citations.

9. (kolos2018fkbpligands—wherewe pages 5-6): Jürgen M. Kolos, Andreas M. Voll, Michael Bauder, and Felix Hausch. Fkbp ligands—where we are and where to go? Frontiers in Pharmacology, Dec 2018. URL: https://doi.org/10.3389/fphar.2018.01425, doi:10.3389/fphar.2018.01425. This article has 198 citations.

10. (kolos2018fkbpligands—wherewe pages 16-17): Jürgen M. Kolos, Andreas M. Voll, Michael Bauder, and Felix Hausch. Fkbp ligands—where we are and where to go? Frontiers in Pharmacology, Dec 2018. URL: https://doi.org/10.3389/fphar.2018.01425, doi:10.3389/fphar.2018.01425. This article has 198 citations.

11. (maruyama2004archaealpeptidylprolyl pages 1-2): T. Maruyama, R. Suzuki, and M. Furutani. Archaeal peptidyl prolyl cis-trans isomerases (ppiases) update 2004. Frontiers in bioscience : a journal and virtual library, 9:1680-720, May 2004. URL: https://doi.org/10.2741/1361, doi:10.2741/1361. This article has 59 citations.

12. (maruyama2004archaealpeptidylprolyl pages 3-4): T. Maruyama, R. Suzuki, and M. Furutani. Archaeal peptidyl prolyl cis-trans isomerases (ppiases) update 2004. Frontiers in bioscience : a journal and virtual library, 9:1680-720, May 2004. URL: https://doi.org/10.2741/1361, doi:10.2741/1361. This article has 59 citations.

13. (tong2016fk506bindingproteinsand pages 1-2): Mingming Tong and Yu Jiang. Fk506-binding proteins and their diverse functions. Current molecular pharmacology, 9 1:48-65, Dec 2016. URL: https://doi.org/10.2174/1874467208666150519113541, doi:10.2174/1874467208666150519113541. This article has 168 citations and is from a peer-reviewed journal.

14. (dunyak2016peptidylprolineisomerases(ppiases) pages 3-5): Bryan M. Dunyak and Jason E. Gestwicki. Peptidyl-proline isomerases (ppiases): targets for natural products and natural product-inspired compounds. Journal of medicinal chemistry, 59 21:9622-9644, Jul 2016. URL: https://doi.org/10.1021/acs.jmedchem.6b00411, doi:10.1021/acs.jmedchem.6b00411. This article has 161 citations and is from a highest quality peer-reviewed journal.

15. (kolos2018fkbpligands—wherewe pages 4-5): Jürgen M. Kolos, Andreas M. Voll, Michael Bauder, and Felix Hausch. Fkbp ligands—where we are and where to go? Frontiers in Pharmacology, Dec 2018. URL: https://doi.org/10.3389/fphar.2018.01425, doi:10.3389/fphar.2018.01425. This article has 198 citations.

16. (tong2016fk506bindingproteinsand pages 2-3): Mingming Tong and Yu Jiang. Fk506-binding proteins and their diverse functions. Current molecular pharmacology, 9 1:48-65, Dec 2016. URL: https://doi.org/10.2174/1874467208666150519113541, doi:10.2174/1874467208666150519113541. This article has 168 citations and is from a peer-reviewed journal.

17. (tong2016fk506bindingproteinsand pages 3-5): Mingming Tong and Yu Jiang. Fk506-binding proteins and their diverse functions. Current molecular pharmacology, 9 1:48-65, Dec 2016. URL: https://doi.org/10.2174/1874467208666150519113541, doi:10.2174/1874467208666150519113541. This article has 168 citations and is from a peer-reviewed journal.

18. (g�thel1999peptidylprolylcistransisomerases pages 4-6): S. F. G�thel and M. A. Marahiel. Peptidyl-prolyl cis-trans isomerases, a superfamily of ubiquitous folding catalysts. Cellular and Molecular Life Sciences CMLS, 55:423-436, Mar 1999. URL: https://doi.org/10.1007/s000180050299, doi:10.1007/s000180050299. This article has 893 citations.

19. (galat2019compressionoflarge pages 15-16): Andrzej Galat. Compression of large sets of sequence data reveals fine diversification of functional profiles in multigene families of proteins: a study for peptidyl-prolyl cis/trans isomerases (ppiase). Biomolecules, 9:59, Feb 2019. URL: https://doi.org/10.3390/biom9020059, doi:10.3390/biom9020059. This article has 2 citations.

20. (galat2000sequencediversificationof pages 5-6): Andrzej Galat. Sequence diversification of the fk506-binding proteins in several different genomes. European journal of biochemistry, 267 16:4945-59, Aug 2000. URL: https://doi.org/10.1046/j.1432-1327.2000.01509.x, doi:10.1046/j.1432-1327.2000.01509.x. This article has 86 citations.

21. (galat2000sequencediversificationof pages 2-3): Andrzej Galat. Sequence diversification of the fk506-binding proteins in several different genomes. European journal of biochemistry, 267 16:4945-59, Aug 2000. URL: https://doi.org/10.1046/j.1432-1327.2000.01509.x, doi:10.1046/j.1432-1327.2000.01509.x. This article has 86 citations.

22. (maruyama2000archaealpeptidylprolyl pages 5-8): T. Maruyama and M. Furutani. Archaeal peptidyl prolyl cis-trans isomerases (ppiases). Frontiers in bioscience : a journal and virtual library, 5:D821-36, Sep 2000. URL: https://doi.org/10.2741/maruyama, doi:10.2741/maruyama. This article has 69 citations.

23. (anchal2021distributionofpeptidylprolyl pages 13-14): Anchal, Vineeta Kaushik, and Manisha Goel. Distribution of peptidyl-prolyl isomerase (ppiase) in the archaea. Frontiers in Microbiology, Oct 2021. URL: https://doi.org/10.3389/fmicb.2021.751049, doi:10.3389/fmicb.2021.751049. This article has 6 citations and is from a peer-reviewed journal.

24. (galat2000sequencediversificationof pages 3-5): Andrzej Galat. Sequence diversification of the fk506-binding proteins in several different genomes. European journal of biochemistry, 267 16:4945-59, Aug 2000. URL: https://doi.org/10.1046/j.1432-1327.2000.01509.x, doi:10.1046/j.1432-1327.2000.01509.x. This article has 86 citations.

25. (galat2000sequencediversificationof pages 6-7): Andrzej Galat. Sequence diversification of the fk506-binding proteins in several different genomes. European journal of biochemistry, 267 16:4945-59, Aug 2000. URL: https://doi.org/10.1046/j.1432-1327.2000.01509.x, doi:10.1046/j.1432-1327.2000.01509.x. This article has 86 citations.

## Artifacts

- [Edison artifact artifact-00](PTHR10516-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR10516-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. maruyama2004archaealpeptidylprolyl pages 8-11
2. lemaster2016conformationaldynamicsin pages 17-19
3. lemaster2016conformationaldynamicsin pages 8-9
4. zgajnar2019biologicalactionsof pages 1-3
5. maruyama2004archaealpeptidylprolyl pages 7-8
6. galat2019compressionoflarge pages 15-16
7. maruyama2004archaealpeptidylprolyl pages 1-2
8. galat2000sequencediversificationof pages 6-7
9. lemaster2016conformationaldynamicsin pages 19-20
10. maruyama2004archaealpeptidylprolyl pages 3-4
11. galat2000sequencediversificationof pages 5-6
12. galat2000sequencediversificationof pages 2-3
13. maruyama2000archaealpeptidylprolyl pages 5-8
14. anchal2021distributionofpeptidylprolyl pages 13-14
15. galat2000sequencediversificationof pages 3-5
16. https://doi.org/10.1021/acs.jmedchem.6b00411,
17. https://doi.org/10.2741/1361,
18. https://doi.org/10.2174/1874467208666150519113146,
19. https://doi.org/10.3390/biom9020052,
20. https://doi.org/10.3389/fphar.2018.01425,
21. https://doi.org/10.2174/1874467208666150519113541,
22. https://doi.org/10.1007/s000180050299,
23. https://doi.org/10.3390/biom9020059,
24. https://doi.org/10.1046/j.1432-1327.2000.01509.x,
25. https://doi.org/10.2741/maruyama,
26. https://doi.org/10.3389/fmicb.2021.751049,