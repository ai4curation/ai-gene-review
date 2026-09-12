---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-20T04:52:21.243832'
end_time: '2026-06-20T05:02:13.277338'
duration_seconds: 592.03
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: IPR001424
  interpro_name: Superoxide dismutase, copper/zinc binding domain
  interpro_short_name: SOD_Cu_Zn_dom
  interpro_type: domain
  interpro_integrated: None (top-level entry)
  member_databases: 'cd00305 (cdd: Cu-Zn_Superoxide_Dismutase); PF00080 (pfam: Copper/zinc
    superoxide dismutase (SODC)); PR00068 (prints: CUZNDISMTASE)'
  n_proteins: '21202'
  n_taxa: '19282'
  n_subfamilies: '0'
  interpro2go_terms: GO:0046872 metal ion binding [F]; GO:0006801 superoxide metabolic
    process [P]
  interpro_description: 'Superoxide dismutases (SODs) are ubiquitous metalloproteins
    that prevent damage by oxygen-mediated free radicals by catalysing the dismutation
    of superoxide into molecular oxygen and hydrogen peroxide . Superoxide is a normal
    by-product of aerobic respiration and is produced by a number of reactions, including
    oxidative phosphorylation and photosynthesis. The dismutase enzymes have a very
    high catalytic efficiency due to the attraction of superoxide to the ions bound
    at the active site [[cite:PUB00004789], [cite:PUB00001545]]. There are three forms
    of superoxide dismutase, depending on the metal cofactor: Cu/Zn (which binds both
    copper and zinc), Fe and Mn types. The Fe and Mn forms are similar in their primary,
    secondary and tertiary structures, but are distinct from the Cu/Zn form . Prokaryotes
    and protists contain Mn, Fe or both types, while most eukaryotic organisms utilise
    the Cu/Zn type. Defects in the human SOD1 gene causes familial amyotrophic lateral
    sclerosis (Lou Gehrig''s disease). Cytoplasmic and periplasmic SODs exist as dimers,
    whereas chloroplastic and extracellular enzymes exist as tetramers. Structural
    analysis supports the notion of independent functional evolution in prokaryotes
    (P-class) and eukaryotes (E-class) [[cite:PUB00080003], [cite:PUB00032612], [cite:PUB00022943],
    [cite:PUB00023102], [cite:PUB00032697], [cite:PUB00026910], [cite:PUB00080004],
    [cite:PUB00001002]].'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 45
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: IPR001424-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: IPR001424-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** IPR001424
- **Name:** Superoxide dismutase, copper/zinc binding domain
- **Short name:** SOD_Cu_Zn_dom
- **Entry type:** domain
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** cd00305 (cdd: Cu-Zn_Superoxide_Dismutase); PF00080 (pfam: Copper/zinc superoxide dismutase (SODC)); PR00068 (prints: CUZNDISMTASE)
- **Scale:** 21202 proteins across 19282 taxa, 0 subfamilies
- **Current InterPro2GO terms (the mappings under review):** GO:0046872 metal ion binding [F]; GO:0006801 superoxide metabolic process [P]
- **InterPro description:** Superoxide dismutases (SODs) are ubiquitous metalloproteins that prevent damage by oxygen-mediated free radicals by catalysing the dismutation of superoxide into molecular oxygen and hydrogen peroxide . Superoxide is a normal by-product of aerobic respiration and is produced by a number of reactions, including oxidative phosphorylation and photosynthesis. The dismutase enzymes have a very high catalytic efficiency due to the attraction of superoxide to the ions bound at the active site [[cite:PUB00004789], [cite:PUB00001545]]. There are three forms of superoxide dismutase, depending on the metal cofactor: Cu/Zn (which binds both copper and zinc), Fe and Mn types. The Fe and Mn forms are similar in their primary, secondary and tertiary structures, but are distinct from the Cu/Zn form . Prokaryotes and protists contain Mn, Fe or both types, while most eukaryotic organisms utilise the Cu/Zn type. Defects in the human SOD1 gene causes familial amyotrophic lateral sclerosis (Lou Gehrig's disease). Cytoplasmic and periplasmic SODs exist as dimers, whereas chloroplastic and extracellular enzymes exist as tetramers. Structural analysis supports the notion of independent functional evolution in prokaryotes (P-class) and eukaryotes (E-class) [[cite:PUB00080003], [cite:PUB00032612], [cite:PUB00022943], [cite:PUB00023102], [cite:PUB00032697], [cite:PUB00026910], [cite:PUB00080004], [cite:PUB00001002]].

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**IPR001424 (Superoxide dismutase, copper/zinc binding domain)**, structured to support GO annotation review.

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
- **Accession:** IPR001424
- **Name:** Superoxide dismutase, copper/zinc binding domain
- **Short name:** SOD_Cu_Zn_dom
- **Entry type:** domain
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** cd00305 (cdd: Cu-Zn_Superoxide_Dismutase); PF00080 (pfam: Copper/zinc superoxide dismutase (SODC)); PR00068 (prints: CUZNDISMTASE)
- **Scale:** 21202 proteins across 19282 taxa, 0 subfamilies
- **Current InterPro2GO terms (the mappings under review):** GO:0046872 metal ion binding [F]; GO:0006801 superoxide metabolic process [P]
- **InterPro description:** Superoxide dismutases (SODs) are ubiquitous metalloproteins that prevent damage by oxygen-mediated free radicals by catalysing the dismutation of superoxide into molecular oxygen and hydrogen peroxide . Superoxide is a normal by-product of aerobic respiration and is produced by a number of reactions, including oxidative phosphorylation and photosynthesis. The dismutase enzymes have a very high catalytic efficiency due to the attraction of superoxide to the ions bound at the active site [[cite:PUB00004789], [cite:PUB00001545]]. There are three forms of superoxide dismutase, depending on the metal cofactor: Cu/Zn (which binds both copper and zinc), Fe and Mn types. The Fe and Mn forms are similar in their primary, secondary and tertiary structures, but are distinct from the Cu/Zn form . Prokaryotes and protists contain Mn, Fe or both types, while most eukaryotic organisms utilise the Cu/Zn type. Defects in the human SOD1 gene causes familial amyotrophic lateral sclerosis (Lou Gehrig's disease). Cytoplasmic and periplasmic SODs exist as dimers, whereas chloroplastic and extracellular enzymes exist as tetramers. Structural analysis supports the notion of independent functional evolution in prokaryotes (P-class) and eukaryotes (E-class) [[cite:PUB00080003], [cite:PUB00032612], [cite:PUB00022943], [cite:PUB00023102], [cite:PUB00032697], [cite:PUB00026910], [cite:PUB00080004], [cite:PUB00001002]].

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**IPR001424 (Superoxide dismutase, copper/zinc binding domain)**, structured to support GO annotation review.

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


# Comprehensive Research Report: InterPro IPR001424 (Superoxide Dismutase, Copper/Zinc Binding Domain) — GO Annotation Review

## 1. Family Definition and Biochemistry

The IPR001424 entry corresponds to the copper/zinc superoxide dismutase (Cu/Zn SOD) domain, a structurally conserved module found across bacteria, plants, fungi, and animals. Canonical members adopt an eight-stranded antiparallel Greek-key β-barrel fold. This domain coordinates a redox-active copper ion at the catalytic site, typically through four histidine residues, and often a structural zinc ion via two histidines and an aspartate. The fold is further stabilized by an intramolecular disulfide bridge (canonical in most forms), an active site arginine that facilitates substrate orientation, and an extended electrostatic loop that enhances superoxide attraction and catalytic efficiency. The domain supports extraordinarily rapid, diffusion-limited dismutation of superoxide anion (O2·–) into O2 and H2O2 via two sequential half-reactions of copper redox cycling (wright2019thebiophysicsof pages 2-3, robinett2018eukaryoticcopperonlysuperoxide pages 1-2, wright2019thebiophysicsof pages 3-4).

Recent work confirms that this core structure and mechanism underlie both cytosolic SOD1 and some extracellular/tetrameric SOD3 forms. However, the domain also occurs in variant contexts, including copper-only SODs (lacking canonical Zn binding) and cysteine-less SODs (compensating for absence of the disulfide with alternative stabilizing interactions) (robinett2018eukaryoticcopperonlysuperoxide pages 2-3, furukawa2023characterizationofa pages 1-2). Some animal and fungal proteins exhibit tandem SOD-repeat architectures (CSRPs), providing additional complexity (tan2025copperonlysod pages 1-2).

See the following structured summary table for key features, supporting evidence, and annotation implications:
| Feature type | Description | Conserved residues/characteristics | Evidence from literature with citations | Implications for GO annotation |
|---|---|---|---|---|
| Core fold | Canonical Cu/Zn SOD domains adopt an eight-stranded antiparallel Greek-key β-barrel; this is the defining structural scaffold shared across intracellular, extracellular, and many bacterial Cu/Zn SODs. | Greek-key β-barrel; compact β-sheet-rich monomer; often dimeric or tetrameric at whole-protein level. | Reviews and structural summaries describe Cu/Zn SODs as Greek-key β-barrel proteins, with each monomer contributing the canonical barrel scaffold; bacterial and eukaryotic members share this core despite assembly differences. (pratt2015structuralfunctionaland pages 1-5, robinett2018eukaryoticcopperonlysuperoxide pages 1-2, wright2019thebiophysicsof pages 3-4) | Supports a structural-domain annotation. By itself, the fold does **not** justify whole-protein GO process terms for every match, especially on a domain entry. |
| Copper-binding catalytic site | Catalysis depends on a redox-active Cu ion bound in the active site; Cu cycles between Cu(II) and Cu(I) during superoxide disproportionation. | Typically four Cu ligands are histidines; one “dynamic” histidine also bridges Zn in canonical Cu/Zn SODs. | Cu is the catalytic cofactor in Cu/Zn SODs; canonical Cu/Zn SODs use a histidine-coordinated Cu center, and the dynamic histidine changes coordination during catalysis. (robinett2018eukaryoticcopperonlysuperoxide pages 2-3, robinett2018eukaryoticcopperonlysuperoxide pages 1-2, anwar2025therapeuticapplicationsand pages 3-5) | A more informative molecular-function term than generic **metal ion binding** would be **superoxide dismutase activity** when assigned to a functionally homogeneous protein family, but that is risky on a domain entry spanning divergent variants. |
| Zinc-binding structural site | In canonical Cu/Zn SODs, Zn stabilizes the active-site architecture and helps maintain catalytic competence and pH robustness, but is not itself the redox center. | Zn typically coordinated by the dynamic histidine plus two additional histidines and an aspartate in canonical forms. | Zn is described as structurally supportive rather than directly catalytic; it stabilizes protein structure and assists catalysis indirectly in canonical Cu/Zn enzymes. (robinett2018eukaryoticcopperonlysuperoxide pages 2-3, robinett2018eukaryoticcopperonlysuperoxide pages 1-2, anwar2025therapeuticapplicationsand pages 3-5) | Generic GO:0046872 **metal ion binding** is true for many canonical members but is overly broad and low-information; moreover, some homologous variants lose canonical Zn binding. |
| Catalytic mechanism | Superoxide disproportionation proceeds in two half-reactions: Cu(II) is reduced by one superoxide to Cu(I) with release of O2, then Cu(I) is reoxidized by a second superoxide plus 2H+ to yield H2O2. | Redox cycling at Cu center; substrate guidance by active-site environment; diffusion-limited catalysis in canonical enzymes. | Canonical reaction scheme and Cu redox cycling are summarized repeatedly in modern reviews of SOD1/CuZnSOD biology. (wright2019thebiophysicsof pages 2-3, robinett2018eukaryoticcopperonlysuperoxide pages 1-2, trist2021superoxidedismutase1 pages 3-4) | This supports linkage to superoxide metabolism for catalytically active enzymes, but because IPR001424 is a **domain** and includes divergent forms, GO:0006801 **superoxide metabolic process** risks over-annotation. |
| Active-site arginine and electrostatic steering | A conserved active-site Arg and the electrostatic loop help attract and orient anionic superoxide into the catalytic Cu center, contributing to very high catalytic rates. | Conserved Arg near active-site entry; charged residues in loop VII/electrostatic loop. | The active-site Arg and electrostatic loop are described as critical for substrate attraction/funneling and catalytic efficiency in canonical Cu/Zn SODs. (robinett2018eukaryoticcopperonlysuperoxide pages 2-3, furukawa2023characterizationofa pages 1-2) | Presence of the domain does not guarantee full conservation of electrostatic steering features; process/function GO terms should not be propagated blindly from the canonical paradigm. |
| Electrostatic loop (loop VII) | Extended loop VII, often termed the electrostatic loop (ESL), is a hallmark of canonical Cu/Zn SODs and contributes to substrate guidance and metal-site organization. | Loop VII / ESL present and often charged in canonical Cu/Zn SODs. | Structural work and reviews identify loop VII as the electrostatic loop; some divergent SOD-like proteins have truncated or missing ESL segments. (robinett2018eukaryoticcopperonlysuperoxide pages 2-3, robinett2018eukaryoticcopperonlysuperoxide pages 1-2, wright2019thebiophysicsof pages 3-4) | Loss or remodeling of the ESL in some homologs weakens the case that every domain match has canonical superoxide dismutase biochemistry. |
| Conserved disulfide bond | Canonical Cu/Zn SODs contain an intramolecular disulfide that stabilizes the active conformation, helps position loops around the active site, and contributes to maturation/stability. | Conserved intramolecular disulfide, classically between two cysteines equivalent to human SOD1 Cys57/Cys146. | Structural and biochemical analyses show the disulfide is highly conserved in canonical Cu/Zn SODs and important for maintaining catalytically competent conformation. (furukawa2023characterizationofa pages 1-2, wright2019thebiophysicsof pages 3-4) | A domain-level GO mapping should not assume this maturation/stability feature is universal across all matches, because bona fide variants lacking the disulfide exist. |
| Canonical oligomeric context | Whole proteins containing this domain can be homodimers, tetramers, or in some bacterial cases monomers; oligomeric state is not encoded by the domain alone. | Dimeric SOD1, tetrameric extracellular SOD, some monomeric bacterial forms. | Reviews note Cu/Zn SODs can be homodimeric, tetrameric, or more rarely monomeric, depending on lineage and whole-protein context. (pratt2015structuralfunctionaland pages 1-5, robinett2018eukaryoticcopperonlysuperoxide pages 1-2) | Reinforces that IPR001424 is a **module**, not a single uniform whole-protein family; whole-protein GO terms are especially hazardous on this entry. |
| Copper-only SOD variants | Some homologs retain the Cu/Zn SOD-like fold and Cu catalytic site but have lost canonical Zn-binding residues; they function with Cu alone. | Missing two non-dynamic Zn-binding histidines in known Cu-only examples; may retain active-site Arg and parts of Cu-site architecture. | Mycobacterial and fungal Cu-only SODs retain the Greek-key fold but lack canonical Zn-binding residues; some also have altered/open active sites and still show high catalytic efficiency. (robinett2018eukaryoticcopperonlysuperoxide pages 2-3, robinett2018eukaryoticcopperonlysuperoxide pages 1-2, tan2025copperonlysod pages 1-2) | Strong evidence against treating this domain as uniformly “Cu/Zn-binding.” GO:0046872 **metal ion binding** is too generic, and any implicit assumption of Zn binding is not universal. |
| Cysteine-less Cu/Zn SOD variants | Recently characterized bacterial homologs can lack the otherwise conserved cysteines/disulfide yet still retain substantial SOD activity using compensatory interactions. | No Cys residues; no canonical disulfide; Cu/Zn SOD domain retained; alternative hydrophobic/H-bond stabilizing interactions. | A Paenibacillus lautus Cu/Zn SOD was shown experimentally to be cysteine-less, missing the conserved disulfide, yet still active; its structure revealed compensatory interactions. (furukawa2023characterizationofa pages 1-2) | Shows that even highly conserved mechanistic expectations are not universal. Domain matches should not automatically inherit fine-grained assumptions about canonical maturation or metal-site architecture. |
| SOD-repeat proteins (CSRPs) | In animals and related eukaryotes, Cu-only SOD-like domains can occur as tandem repeats within large extracellular proteins (CSRPs), rather than as standalone canonical Cu/Zn SOD enzymes. | Tandem repeated SOD-like domains; often predicted extracellular/GPI-anchored; related to fungal Cu-only SODs. | Reviews identified CSRPs as large multidomain proteins bearing repeated Cu-only SOD-like domains; recent oyster work provided functional evidence that at least one CSRP can act as an extracellular SOD. (robinett2018eukaryoticcopperonlysuperoxide pages 1-2, tan2025copperonlysod pages 1-2) | Domain occurrence inside large repeat proteins makes whole-protein GO propagation especially problematic. Even if some CSRPs are active, a domain-level process term remains over-broad. |
| Functional divergence across taxa | Cu/Zn SOD-domain proteins occur in bacteria, cyanobacteria, fungi, protists, plants, and animals, with lineage-specific innovations in localization, oligomerization, Zn dependence, and loop architecture. | Broad phylogenetic distribution; canonical and divergent subclasses. | CuZnSOD genes are phylogenetically widespread, including in cyanobacteria and across eukaryotes; comparative reviews emphasize convergent/independent diversification of SOD systems and broad compartmental usage. (boden2021timingtheevolution pages 1-2, valle2022superoxidedismutasesin pages 1-3, lyall2020comparativeanalysisof pages 1-3) | A process term such as GO:0006801 may describe many members, but on such a broad **domain** entry it is unsafe to assume validity for every match across all clades. |
| GO review summary | The domain strongly indicates a Cu/Zn-SOD-like structural module associated with metal-assisted redox chemistry, but the entry spans canonical Cu/Zn SODs, Cu-only derivatives, cysteine-less variants, and multidomain repeat proteins. | Structural homology is robust; biochemical uniformity is not absolute. | Multiple sources document both conserved canonical SOD biochemistry and significant departures in Zn binding, disulfide conservation, and domain organization. (tan2025copperonlysod pages 1-2, robinett2018eukaryoticcopperonlysuperoxide pages 2-3, robinett2018eukaryoticcopperonlysuperoxide pages 1-2, furukawa2023characterizationofa pages 1-2) | Recommended review stance: **GO:0006801 superoxide metabolic process = over-broad on a domain entry; GO:0046872 metal ion binding = generic/low-value and not uniformly informative.** Prefer removing or demoting these from the top-level domain entry and mapping more specific catalytic/process terms only on functionally homogeneous child families or curated protein families. |


*Table: This table summarizes the defining structural and mechanistic properties of the IPR001424 Cu/Zn superoxide dismutase domain and highlights major divergent variants. It is useful for judging whether current InterPro2GO mappings are universally valid across all proteins matched by this domain entry.*

## 2. InterPro2GO Mapping Appropriateness

The current InterPro2GO mappings for IPR001424 are:
- GO:0046872 metal ion binding [Molecular Function]
- GO:0006801 superoxide metabolic process [Biological Process]

**Review findings:**
- **GO:0046872 metal ion binding** is generic and technically true for most, but not all, domain matches (e.g., copper-only/cysteine-less variants or repeat proteins may lack canonical Zn binding). Its genericity makes it low-value for biological inference.
- **GO:0006801 superoxide metabolic process** is a whole-protein/process-level term and is not appropriate for domain entries that match non-catalytic or pseudo-enzyme SOD-like domains, repeat architectures, or divergent forms that do not engage in this process.

The structured recommendation/evidence table is as follows:
| GO term ID and name | GO ontology (MF/BP/CC) | Current mapping validity | Problems/concerns with domain-level annotation | Recommended action | Rationale/evidence with citations |
|---|---|---|---|---|---|
| GO:0046872 metal ion binding | MF | Partially true but too generic and not safely informative for all matches | IPR001424 is a **domain** entry, not a whole-protein family. Although canonical Cu/Zn SODs bind Cu and usually Zn, the domain also occurs in **copper-only** variants that have lost canonical Zn-binding residues, in **cysteine-less** variants with altered stabilizing features, and in **multidomain SOD-repeat proteins** where domain presence alone does not justify broad protein-level metal-binding annotation. The term is also excessively generic and low-value. | KEEP_AS_NON_CORE | Canonical Cu/Zn SODs use a catalytic Cu and usually a structural Zn, with conserved histidine-based metal coordination in the Greek-key β-barrel scaffold; however, Cu-only homologs in bacteria/fungi and SOD-repeat proteins in animals show that Zn-binding is not universal across the structural lineage. Because the entry is a top-level domain, propagating a broad MF term to all matches is weakly informative and risks misleading specificity. If InterPro keeps any MF here, a more specific catalytic term should be attached only to a functionally homogeneous child family, not this domain-level entry. (robinett2018eukaryoticcopperonlysuperoxide pages 2-3, robinett2018eukaryoticcopperonlysuperoxide pages 1-2, furukawa2023characterizationofa pages 1-2, wright2019thebiophysicsof pages 3-4, tan2025copperonlysod pages 1-2) |
| GO:0006801 superoxide metabolic process | BP | Not valid as a universal domain-level mapping | This is a **whole-protein biological process** term attached to a **domain** signature. Many matches are canonical SOD enzymes participating in superoxide metabolism, but the entry spans broad taxonomic diversity and structurally divergent forms, including copper-only and repeated-domain proteins; domain presence alone does not prove that every matched protein performs the process. This is classic over-annotation from a module to a whole-protein/process role. | REMOVE | Canonical Cu/Zn SODs catalyze superoxide disproportionation and clearly participate in superoxide metabolism, but that conclusion is drawn from the activity of complete enzymes, not merely from presence of the domain. The signature spans bacteria, cyanobacteria, fungi, plants, animals, and protists, with lineage-specific innovations including altered Zn dependence, modified electrostatic loops, disulfide loss, and tandem repeat architectures. Because InterPro entry IPR001424 is a domain rather than a functionally homogeneous family, the BP term overgeneralizes from canonical single-domain enzymes to all domain-containing proteins. If a process term is desired, it should be moved to a narrower child/family entry or inferred from curated full-length protein families only. (pratt2015structuralfunctionaland pages 1-5, robinett2018eukaryoticcopperonlysuperoxide pages 1-2, boden2021timingtheevolution pages 1-2, valle2022superoxidedismutasesin pages 1-3, boden2021timingtheevolution pages 2-5, lyall2020comparativeanalysisof pages 1-3, tan2025copperonlysod pages 1-2, furukawa2023characterizationofa pages 1-2) |


*Table: This table evaluates the current InterPro2GO mappings for the Cu/Zn superoxide dismutase domain and highlights why domain-level propagation is problematic. It is useful for deciding which mappings should be retained only as non-core hints versus removed as over-broad annotations.*

## 3. Functional Divergence Across the Family

Evidence demonstrates substantial functional divergence beyond canonical Cu/Zn SODs:
- **Copper-only SODs** (in bacteria, fungi, mollusks): Lack canonical Zn site and use a single copper for catalysis. Some fungal/oomycete/animal copper-only SODs also lack the electrostatic loop, have open-active sites, or exist as tandem repeats (CSRPs).
- **Cysteine-less SODs**: Certain bacterial lineages (furukawa2023characterizationofa pages 1-2) show SOD domains with no cysteines/disulfide, stabilizing the fold with hydrophobic/hydrogen-bonding contacts yet retaining SOD activity.
- **Tandem SOD-repeat proteins (CSRPs):** Many animal and some protistan lineages encode large, multi-domain SOD-repeat proteins, with SOD-like domains that can be catalytically active or inactive, complicating global process annotation.

Thus, not every domain match signifies a catalytic SOD or participation in superoxide metabolism (tan2025copperonlysod pages 1-2, robinett2018eukaryoticcopperonlysuperoxide pages 2-3, robinett2018eukaryoticcopperonlysuperoxide pages 1-2, furukawa2023characterizationofa pages 1-2).

## 4. Taxonomic Scope

The IPR001424 domain is widespread. It occurs in:
- Bacteria (boden2021timingtheevolution pages 1-2, boden2021timingtheevolution pages 2-5)
- Eukaryotes: Animals, plants, fungi, protists
- Rarely in Archaea

While the domain is broadly conserved, specific SOD activity, metal dependence, and functional context can vary within and across taxa (valle2022superoxidedismutasesin pages 1-3, lyall2020comparativeanalysisof pages 1-3, valle2022superoxidedismutasesin pages 3-4).

## 5. Over-annotation Verdict and Recommendations

**Summary:**
- **GO:0046872 (metal ion binding):** Retain as a non-core, weakly-informative annotation only. Presence of the domain does not guarantee canonical Cu/Zn binding biochemistry nor high functional specificity.
- **GO:0006801 (superoxide metabolic process):** Remove from the domain-level IPR001424 entry. This Biological Process term is systematically over-broad for a structural/functional module and risks propagating an incorrect or misleading functional assertion across taxa and divergent proteins.

**Recommended GO action pattern:**
- **GO:0046872 metal ion binding:** KEEP_AS_NON_CORE
- **GO:0006801 superoxide metabolic process:** REMOVE

**Recommendation for InterPro:**
- If available, map specific catalytic and process terms only onto well-characterized, functionally homogeneous child/family entries where all or nearly all members have demonstrated superoxide dismutase activity and canonical metal binding.
- Avoid domain-level propagation of whole-protein/process terms.

**Experimental evidence and recent reviews** (robinett2018eukaryoticcopperonlysuperoxide pages 2-3, robinett2018eukaryoticcopperonlysuperoxide pages 1-2, furukawa2023characterizationofa pages 1-2, wright2019thebiophysicsof pages 3-4) form the core of this judgment. The recommendation is also in line with good annotation practice per recent biocuration guidelines.

**URLs and publication details:**
- Wright GS, Antonyuk SV, Hasnain SS (2019) The biophysics of superoxide dismutase-1 and amyotrophic lateral sclerosis. Quarterly Reviews of Biophysics 52:e12. [https://doi.org/10.1017/S003358351900012X] (wright2019thebiophysicsof pages 2-3, wright2019thebiophysicsof pages 3-4)
- Robinett NG, Peterson RL, Culotta VC (2018) Eukaryotic copper-only superoxide dismutases (SODs): A new class of SOD enzymes and SOD-like protein domains. J Biol Chem 293:4636–4643. [https://doi.org/10.1074/jbc.tm117.000182] (robinett2018eukaryoticcopperonlysuperoxide pages 2-3, robinett2018eukaryoticcopperonlysuperoxide pages 1-2)
- Furukawa Y, et al. (2023). Characterization of a novel cysteine-less Cu/Zn-superoxide dismutase in Paenibacillus lautus missing a conserved disulfide bond. J Biol Chem 299:105040. [https://doi.org/10.1016/j.jbc.2023.105040] (furukawa2023characterizationofa pages 1-2)
- Boden JS, et al. (2021). Timing the evolution of antioxidant enzymes in cyanobacteria. Nat Commun 12:4742. [https://doi.org/10.1038/s41467-021-24396-y] (boden2021timingtheevolution pages 1-2, boden2021timingtheevolution pages 2-5)

For further details, see the embedded tables above for rapid curation reference.

References

1. (wright2019thebiophysicsof pages 2-3): Gareth S. A. Wright, Svetlana V. Antonyuk, and S. Samar Hasnain. The biophysics of superoxide dismutase-1 and amyotrophic lateral sclerosis. Quarterly Reviews of Biophysics, Nov 2019. URL: https://doi.org/10.1017/s003358351900012x, doi:10.1017/s003358351900012x. This article has 99 citations and is from a peer-reviewed journal.

2. (robinett2018eukaryoticcopperonlysuperoxide pages 1-2): Natalie G. Robinett, Ryan L. Peterson, and Valeria C. Culotta. Eukaryotic copper-only superoxide dismutases (sods): a new class of sod enzymes and sod-like protein domains. Journal of Biological Chemistry, 293:4636-4643, Mar 2018. URL: https://doi.org/10.1074/jbc.tm117.000182, doi:10.1074/jbc.tm117.000182. This article has 146 citations and is from a domain leading peer-reviewed journal.

3. (wright2019thebiophysicsof pages 3-4): Gareth S. A. Wright, Svetlana V. Antonyuk, and S. Samar Hasnain. The biophysics of superoxide dismutase-1 and amyotrophic lateral sclerosis. Quarterly Reviews of Biophysics, Nov 2019. URL: https://doi.org/10.1017/s003358351900012x, doi:10.1017/s003358351900012x. This article has 99 citations and is from a peer-reviewed journal.

4. (robinett2018eukaryoticcopperonlysuperoxide pages 2-3): Natalie G. Robinett, Ryan L. Peterson, and Valeria C. Culotta. Eukaryotic copper-only superoxide dismutases (sods): a new class of sod enzymes and sod-like protein domains. Journal of Biological Chemistry, 293:4636-4643, Mar 2018. URL: https://doi.org/10.1074/jbc.tm117.000182, doi:10.1074/jbc.tm117.000182. This article has 146 citations and is from a domain leading peer-reviewed journal.

5. (furukawa2023characterizationofa pages 1-2): Yoshiaki Furukawa, Atsuko Shintani, Shuhei Narikiyo, Kaori Sue, Masato Akutsu, and Norifumi Muraki. Characterization of a novel cysteine-less cu/zn-superoxide dismutase in paenibacillus lautus missing a conserved disulfide bond. Journal of Biological Chemistry, 299:105040, Aug 2023. URL: https://doi.org/10.1016/j.jbc.2023.105040, doi:10.1016/j.jbc.2023.105040. This article has 6 citations and is from a domain leading peer-reviewed journal.

6. (tan2025copperonlysod pages 1-2): Li Tan, Youli Liu, Yueyang Sun, Sheng Liu, Zhihua Lin, and Qinggang Xue. Copper only sod repeat proteins likely act as an extracellular superoxide dismutase in oyster antioxidant defense. Scientific Reports, Jul 2025. URL: https://doi.org/10.1038/s41598-025-06156-w, doi:10.1038/s41598-025-06156-w. This article has 9 citations and is from a peer-reviewed journal.

7. (pratt2015structuralfunctionaland pages 1-5): Ashley J. Pratt, Michael DiDonato, David S. Shin, Diane E. Cabelli, Cami K. Bruns, Carol A. Belzer, Andrew R. Gorringe, Paul R. Langford, Louisa B. Tabatabai, J. Simon Kroll, John A. Tainer, and Elizabeth D. Getzoff. Structural, functional, and immunogenic insights on cu,zn superoxide dismutase pathogenic virulence factors from neisseria meningitidis and brucella abortus. Journal of Bacteriology, 197:3834-3847, Dec 2015. URL: https://doi.org/10.1128/jb.00343-15, doi:10.1128/jb.00343-15. This article has 37 citations and is from a peer-reviewed journal.

8. (anwar2025therapeuticapplicationsand pages 3-5): S. Anwar, Tarique Sarwar, Amjad Ali Khan, and A. Rahmani. Therapeutic applications and mechanisms of superoxide dismutase (sod) in different pathogenesis. Biomolecules, Aug 2025. URL: https://doi.org/10.3390/biom15081130, doi:10.3390/biom15081130. This article has 60 citations.

9. (trist2021superoxidedismutase1 pages 3-4): Benjamin G. Trist, James B. Hilton, Dominic J. Hare, Peter J. Crouch, and Kay L. Double. Superoxide dismutase 1 in health and disease: how a frontline antioxidant becomes neurotoxic. Nov 2021. URL: https://doi.org/10.1002/anie.202000451, doi:10.1002/anie.202000451. This article has 260 citations.

10. (boden2021timingtheevolution pages 1-2): Joanne S. Boden, Kurt O. Konhauser, Leslie J. Robbins, and Patricia Sánchez-Baracaldo. Timing the evolution of antioxidant enzymes in cyanobacteria. Nature Communications, Aug 2021. URL: https://doi.org/10.1038/s41467-021-24396-y, doi:10.1038/s41467-021-24396-y. This article has 144 citations and is from a highest quality peer-reviewed journal.

11. (valle2022superoxidedismutasesin pages 1-3): Alvaro de Obeso Fernandez del Valle and Christian Quintus Scheckhuber. Superoxide dismutases in eukaryotic microorganisms: four case studies. Antioxidants, 11:188, Jan 2022. URL: https://doi.org/10.3390/antiox11020188, doi:10.3390/antiox11020188. This article has 24 citations.

12. (lyall2020comparativeanalysisof pages 1-3): Rafe Lyall, Zoran Nikoloski, and Tsanko Gechev. Comparative analysis of ros network genes in extremophile eukaryotes. International Journal of Molecular Sciences, 21:9131, Nov 2020. URL: https://doi.org/10.3390/ijms21239131, doi:10.3390/ijms21239131. This article has 18 citations.

13. (boden2021timingtheevolution pages 2-5): Joanne S. Boden, Kurt O. Konhauser, Leslie J. Robbins, and Patricia Sánchez-Baracaldo. Timing the evolution of antioxidant enzymes in cyanobacteria. Nature Communications, Aug 2021. URL: https://doi.org/10.1038/s41467-021-24396-y, doi:10.1038/s41467-021-24396-y. This article has 144 citations and is from a highest quality peer-reviewed journal.

14. (valle2022superoxidedismutasesin pages 3-4): Alvaro de Obeso Fernandez del Valle and Christian Quintus Scheckhuber. Superoxide dismutases in eukaryotic microorganisms: four case studies. Antioxidants, 11:188, Jan 2022. URL: https://doi.org/10.3390/antiox11020188, doi:10.3390/antiox11020188. This article has 24 citations.

## Artifacts

- [Edison artifact artifact-00](IPR001424-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](IPR001424-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. tan2025copperonlysod pages 1-2
2. furukawa2023characterizationofa pages 1-2
3. wright2019thebiophysicsof pages 2-3
4. robinett2018eukaryoticcopperonlysuperoxide pages 1-2
5. wright2019thebiophysicsof pages 3-4
6. robinett2018eukaryoticcopperonlysuperoxide pages 2-3
7. pratt2015structuralfunctionaland pages 1-5
8. anwar2025therapeuticapplicationsand pages 3-5
9. boden2021timingtheevolution pages 1-2
10. valle2022superoxidedismutasesin pages 1-3
11. lyall2020comparativeanalysisof pages 1-3
12. boden2021timingtheevolution pages 2-5
13. valle2022superoxidedismutasesin pages 3-4
14. F
15. P
16. [cite:PUB00004789
17. cite:PUB00001545
18. [cite:PUB00080003
19. cite:PUB00032612
20. cite:PUB00022943
21. cite:PUB00023102
22. cite:PUB00032697
23. cite:PUB00026910
24. cite:PUB00080004
25. cite:PUB00001002
26. Molecular Function
27. Biological Process
28. https://doi.org/10.1017/S003358351900012X
29. https://doi.org/10.1074/jbc.tm117.000182
30. https://doi.org/10.1016/j.jbc.2023.105040
31. https://doi.org/10.1038/s41467-021-24396-y
32. https://doi.org/10.1017/S003358351900012X]
33. https://doi.org/10.1074/jbc.tm117.000182]
34. https://doi.org/10.1016/j.jbc.2023.105040]
35. https://doi.org/10.1038/s41467-021-24396-y]
36. https://doi.org/10.1017/s003358351900012x,
37. https://doi.org/10.1074/jbc.tm117.000182,
38. https://doi.org/10.1016/j.jbc.2023.105040,
39. https://doi.org/10.1038/s41598-025-06156-w,
40. https://doi.org/10.1128/jb.00343-15,
41. https://doi.org/10.3390/biom15081130,
42. https://doi.org/10.1002/anie.202000451,
43. https://doi.org/10.1038/s41467-021-24396-y,
44. https://doi.org/10.3390/antiox11020188,
45. https://doi.org/10.3390/ijms21239131,