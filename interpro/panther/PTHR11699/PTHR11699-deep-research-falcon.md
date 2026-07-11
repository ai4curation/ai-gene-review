---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T20:08:04.327684'
end_time: '2026-06-28T20:28:50.458813'
duration_seconds: 1246.13
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR11699
  interpro_name: Aldehyde dehydrogenase
  interpro_short_name: Aldehyde_dehydrogenase
  interpro_type: family
  interpro_integrated: None (top-level entry)
  member_databases: Not specified
  n_proteins: '121927'
  n_taxa: '29468'
  n_subfamilies: '47'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: The aldehyde dehydrogenase family is involved in the oxidation
    of aldehydes to their corresponding carboxylic acids using NAD(+) or NADP(+) as
    cofactors. Members of this family play a role in various metabolic pathways, including
    the degradation of amino acids such as putrescine and lysine, and the biosynthesis
    of osmoprotectants like glycine betaine. They are also implicated in the detoxification
    of aldehydes produced from alcohol, lipid peroxidation, and as intermediates in
    the metabolism of neurotransmitters, corticosteroids, and biogenic amines. Some
    subfamilies within this protein family are specialized in specific functions,
    such as the oxidation of gamma-aminobutyraldehyde to gamma-aminobutyrate (GABA)
    in putrescine degradation or the conversion of betaine aldehyde to betaine in
    osmoprotectant biosynthesis. The family includes enzymes with broad substrate
    specificity and those involved in the biosynthesis of secondary metabolites and
    structural components of the eye lens.
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 51
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR11699-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR11699-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** PTHR11699
- **Name:** Aldehyde dehydrogenase
- **Short name:** Aldehyde_dehydrogenase
- **Entry type:** family
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** Not specified
- **Scale:** 121927 proteins across 29468 taxa, 47 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The aldehyde dehydrogenase family is involved in the oxidation of aldehydes to their corresponding carboxylic acids using NAD(+) or NADP(+) as cofactors. Members of this family play a role in various metabolic pathways, including the degradation of amino acids such as putrescine and lysine, and the biosynthesis of osmoprotectants like glycine betaine. They are also implicated in the detoxification of aldehydes produced from alcohol, lipid peroxidation, and as intermediates in the metabolism of neurotransmitters, corticosteroids, and biogenic amines. Some subfamilies within this protein family are specialized in specific functions, such as the oxidation of gamma-aminobutyraldehyde to gamma-aminobutyrate (GABA) in putrescine degradation or the conversion of betaine aldehyde to betaine in osmoprotectant biosynthesis. The family includes enzymes with broad substrate specificity and those involved in the biosynthesis of secondary metabolites and structural components of the eye lens.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR11699 (Aldehyde dehydrogenase)**, structured to support GO annotation review.

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
- **Accession:** PTHR11699
- **Name:** Aldehyde dehydrogenase
- **Short name:** Aldehyde_dehydrogenase
- **Entry type:** family
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** Not specified
- **Scale:** 121927 proteins across 29468 taxa, 47 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The aldehyde dehydrogenase family is involved in the oxidation of aldehydes to their corresponding carboxylic acids using NAD(+) or NADP(+) as cofactors. Members of this family play a role in various metabolic pathways, including the degradation of amino acids such as putrescine and lysine, and the biosynthesis of osmoprotectants like glycine betaine. They are also implicated in the detoxification of aldehydes produced from alcohol, lipid peroxidation, and as intermediates in the metabolism of neurotransmitters, corticosteroids, and biogenic amines. Some subfamilies within this protein family are specialized in specific functions, such as the oxidation of gamma-aminobutyraldehyde to gamma-aminobutyrate (GABA) in putrescine degradation or the conversion of betaine aldehyde to betaine in osmoprotectant biosynthesis. The family includes enzymes with broad substrate specificity and those involved in the biosynthesis of secondary metabolites and structural components of the eye lens.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR11699 (Aldehyde dehydrogenase)**, structured to support GO annotation review.

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


# Comprehensive Research Report: PTHR11699 (Aldehyde Dehydrogenase Family) — InterPro2GO Annotation Review

## 1. Family Definition and Biochemistry

### 1.1 Protein Fold and Domain Architecture

The aldehyde dehydrogenase (ALDH) superfamily adopts a conserved three-domain architecture consisting of an N-terminal NAD(P)+-binding domain featuring a Rossmann fold, a catalytic domain of roughly equal size, and a smaller C-terminal oligomerization domain (heider2025thealdehydedehydrogenase pages 1-3, heider2025thealdehydedehydrogenase pages 3-5). Structural alignments across the superfamily reveal remarkably similar folds with RMSD values of 0.67–1.4 Å despite substantial sequence divergence (heider2025thealdehydedehydrogenase pages 3-5). Canonical ALDH enzymes are approximately 500 amino acids per monomer, with Class 1 and Class 2 ALDHs typically forming homotetramers (sharing ~70% sequence identity), while Class 3 members are homodimeric with ~450 amino acids and only ~25% identity to other classes (shortall2021insightsintoaldehyde pages 2-4).

### 1.2 Catalytic Mechanism and Conserved Residues

The catalytic mechanism is centered on a universally conserved catalytic triad: Asn169/170 (oxyanion hole), Glu268/269 (general base), and Cys302/303 (catalytic nucleophile), using the human ALDH2 numbering convention (heider2025thealdehydedehydrogenase pages 5-8, heider2025thealdehydedehydrogenase pages 3-5). The mechanism proceeds through five steps: (1) deprotonation of Cys302 to a thiolate by Glu268 via a bridging water molecule; (2) nucleophilic attack on the incoming aldehyde substrate to form a thiohemiacetal intermediate, stabilized by an oxyanion hole from Asn170; (3) hydride transfer from the thiohemiacetal to NAD(P)+ to form a covalently bound thioester; (4) NADH release; and (5) water-mediated hydrolysis of the thioester to release the carboxylic acid product (heider2025thealdehydedehydrogenase pages 5-8, shortall2021insightsintoaldehyde pages 2-4, heider2025thealdehydedehydrogenase pages 3-5).

Alignment of 145 ALDH sequences identified only 4 strictly invariant residues and 12 highly conserved residues (present in ≥95% of sequences), with glycines and prolines being highly represented among conserved positions, indicating evolutionary pressure preserving chain-bending sites (shortall2021insightsintoaldehyde pages 2-4, hempel1993aldehydedehydrogenaseswidespread pages 1-2). Additional conserved cofactor-binding residues include Lys192, Glu195, and Ile166 for adenosyl ribose binding, and Gln349, Glu399, and Phe401 for nicotinamide interactions (heider2025thealdehydedehydrogenase pages 3-5). A conserved Phe residue near the catalytic Cys (e.g., Phe466) directs incoming aldehydes toward the thiolate group (heider2025thealdehydedehydrogenase pages 5-8). Of the ~500 residues, only approximately 10% (53 residues) are conserved above the 80% level across the extended family (perozich2008relationshipswithinthe pages 4-5).

## 2. InterPro2GO Mapping Appropriateness

PTHR11699 currently has **no InterPro2GO terms mapped**, which is the correct state for this entry. The following analysis explains why no GO terms should be added at this top-level family:

The following table summarizes the functional heterogeneity across major ALDH subfamilies and assesses whether a generic "aldehyde dehydrogenase [NAD(P)+] activity" GO term would be appropriate for each:

| Family/Subfamily | Primary Substrate | Reaction Type | Notable Features | Would "aldehyde dehydrogenase [NAD(P)+] activity" GO term be accurate? |
|---|---|---|---|---|
| ALDH1A | Retinaldehyde | NAD(P)+-dependent oxidation of aldehyde to carboxylic acid (retinoic acid biosynthesis) | Retinal dehydrogenases; major role in retinoic acid production and development; bona fide ALDH enzymes (moretti2016biochemicalandstructural pages 11-14, yoshida1998humanaldehydedehydrogenase pages 1-2) | Yes — for catalytically active ALDH1A enzymes this is accurate, though a more specific retinaldehyde dehydrogenase term would be preferable where supported (moretti2016biochemicalandstructural pages 11-14, yoshida1998humanaldehydedehydrogenase pages 1-2) |
| ALDH2 | Acetaldehyde | NAD+-dependent oxidation of aldehyde to acetate | Canonical mitochondrial acetaldehyde dehydrogenase in ethanol metabolism; archetypal ALDH fold/mechanism (moretti2016biochemicalandstructural pages 11-14, yoshida1998humanaldehydedehydrogenase pages 1-2) | Yes (moretti2016biochemicalandstructural pages 11-14, yoshida1998humanaldehydedehydrogenase pages 1-2) |
| ALDH3A | Aromatic and medium-/long-chain aliphatic aldehydes | NAD(P)+-dependent oxidation of aldehydes to acids | Broad substrate specificity; detoxification; some members also serve non-enzymatic corneal/lens crystallin roles in eye tissues (vasiliou2013aldehydedehydrogenasesfrom pages 3-4, chen2013ocularaldehydedehydrogenases pages 2-4) | Yes for catalytic activity, but this would miss important additional crystallin/structural roles; process/component eye terms should not be generalized to all family members (vasiliou2013aldehydedehydrogenasesfrom pages 3-4, chen2013ocularaldehydedehydrogenases pages 2-4) |
| ALDH4A1 | Glutamate-γ-semialdehyde / pyrroline-5-carboxylate pathway intermediate | NAD+-dependent oxidation in proline catabolism | Specialized semialdehyde dehydrogenase in proline/glutamate metabolism, not a broad aldehyde detox enzyme (moretti2016biochemicalandstructural pages 11-14, vasiliou2013aldehydedehydrogenasesfrom pages 3-4) | Yes at the molecular-function level if GO permits this chemistry under aldehyde dehydrogenase activity; more specific pathway-linked terms are preferable (moretti2016biochemicalandstructural pages 11-14, vasiliou2013aldehydedehydrogenasesfrom pages 3-4) |
| ALDH5A1 | Succinic semialdehyde | NAD+-dependent oxidation to succinate in GABA catabolism | Specialized succinic semialdehyde dehydrogenase in neurotransmitter metabolism (moretti2016biochemicalandstructural pages 11-14, yoshida1998humanaldehydedehydrogenase pages 1-2) | Yes, but a more specific succinic semialdehyde dehydrogenase term would be better (moretti2016biochemicalandstructural pages 11-14, yoshida1998humanaldehydedehydrogenase pages 1-2) |
| ALDH6A1 | Methylmalonate semialdehyde | NAD(P)+-dependent oxidation in valine/pyrimidine catabolism | Specialized metabolic enzyme; not representative of generic aldehyde detoxification (moretti2016biochemicalandstructural pages 11-14, vasiliou2013aldehydedehydrogenasesfrom pages 3-4) | Yes, but a more specific methylmalonate-semialdehyde dehydrogenase term would be better (moretti2016biochemicalandstructural pages 11-14, vasiliou2013aldehydedehydrogenasesfrom pages 3-4) |
| ALDH7A1 | α-Aminoadipic semialdehyde / related aldehydes | NAD(P)+-dependent oxidation in lysine catabolism | Antiquitin family; key role in lysine/pipecolate pathway; disease-associated in humans (moretti2016biochemicalandstructural pages 11-14, vasiliou2013aldehydedehydrogenasesfrom pages 3-4) | Yes, but a more specific aminoadipate-semialdehyde dehydrogenase term would be preferable (moretti2016biochemicalandstructural pages 11-14, vasiliou2013aldehydedehydrogenasesfrom pages 3-4) |
| ALDH1L1 | 10-Formyl-tetrahydrofolate (formyl group donor in folate metabolism) | NADP+-dependent oxidation of formyl-THF to THF + CO2 | Natural fusion protein with N-terminal folate-binding domain, acyl-carrier-like intermediate domain, and C-terminal ALDH domain; functions in one-carbon/folate metabolism, not canonical small-aldehyde metabolism (heider2025thealdehydedehydrogenase pages 9-10, tsybovsky2022structureofputative pages 1-2, krupenko2009fdhanaldehyde pages 1-2) | No — too broad/misleading for the whole protein; the ALDH domain is real, but whole-protein function is 10-formyltetrahydrofolate dehydrogenase, not generic aldehyde dehydrogenase activity (heider2025thealdehydedehydrogenase pages 9-10, tsybovsky2022structureofputative pages 1-2, krupenko2009fdhanaldehyde pages 1-2) |
| ALDH16A1 | No confirmed aldehyde substrate; pseudoenzyme | No demonstrable canonical ALDH catalytic activity | Pseudoenzyme lacking catalytic triad / catalytic Cys and unable to bind cofactors like canonical ALDHs; likely scaffold or protein-interaction regulator (xanthis2023humanaldehydedehydrogenases pages 12-13, liu2019crystalstructureof pages 11-13, liu2019crystalstructureof pages 8-10) | No — this would be incorrect over-annotation (xanthis2023humanaldehydedehydrogenases pages 12-13, liu2019crystalstructureof pages 11-13, liu2019crystalstructureof pages 8-10) |
| ALDH18A1 (P5CS) | γ-Glutamyl phosphate in proline/ornithine biosynthesis | NADPH-dependent reduction as part of bifunctional P5CS reaction, not aldehyde oxidation | Bifunctional enzyme with N-terminal amino-acid kinase and C-terminal ALDH-like reductase domain; modified catalytic machinery; role in proline biosynthesis/osmostress, not canonical ALDH oxidation (brocker2013aldehydedehydrogenase(aldh) pages 14-18, heider2025thealdehydedehydrogenase pages 12-13, tola2020recentdevelopmenton pages 5-6) | No — not accurate for the whole protein or for its principal chemistry (brocker2013aldehydedehydrogenase(aldh) pages 14-18, heider2025thealdehydedehydrogenase pages 12-13, tola2020recentdevelopmenton pages 5-6) |


*Table: This table summarizes major ALDH families/subfamilies, their substrates and reaction types, and whether a generic aldehyde dehydrogenase activity GO term would be appropriate. It is useful for judging why a top-level InterPro family spanning these proteins should not receive a single broad catalytic GO annotation.*

### 2.1 Why No GO Terms Should Be Added

- **Molecular Function terms**: Even the most general GO term such as "aldehyde dehydrogenase [NAD(P)+] activity" (GO:0016620) would be incorrect for ALDH16A1, which is a confirmed pseudoenzyme lacking the catalytic triad and unable to bind NAD+/NADH (xanthis2023humanaldehydedehydrogenases pages 12-13, liu2019crystalstructureof pages 11-13, liu2019crystalstructureof pages 8-10). It would also be misleading for ALDH18A1 (P5CS), which functions as a reductase in proline biosynthesis rather than an oxidase, with a modified catalytic machinery where the conserved Asn and Glu are replaced by Arg and His (heider2025thealdehydedehydrogenase pages 12-13). Similarly, ALDH1L1/1L2 are multi-domain fusion proteins where the ALDH domain is part of a folate-metabolizing enzyme whose overall reaction (10-formyl-THF → THF + CO₂) is not standard aldehyde oxidation (heider2025thealdehydedehydrogenase pages 9-10, tsybovsky2022structureofputative pages 1-2).

- **NAD/NADP binding terms**: Cofactor usage is not uniform across the family. Some members use NAD+, others use NADP+, and ALDH16A1 cannot bind either cofactor (liu2019crystalstructureof pages 8-10).

- **Biological Process terms**: Members participate in vastly different metabolic pathways including retinoic acid biosynthesis, ethanol detoxification, GABA catabolism, lysine catabolism, proline biosynthesis, folate one-carbon metabolism, and osmoprotectant biosynthesis (moretti2016biochemicalandstructural pages 11-14, vasiliou2013aldehydedehydrogenasesfrom pages 3-4, yoshida1998humanaldehydedehydrogenase pages 1-2). No single process term applies universally.

- **Cellular Component terms**: Members are found in cytoplasm, mitochondria, microsomes, and specific tissues (e.g., cornea, lens), with distribution varying by subfamily (yoshida1998humanaldehydedehydrogenase pages 1-2).

## 3. Functional Divergence Across the Family

### 3.1 Major Functional Groups

The ALDH superfamily is extraordinarily functionally diverse. In humans alone, 19 genes encode enzymes classified into 10 families (cuatlayotlolarte2023aldehydedehydrogenasediversity pages 1-2, vasiliou2005analysisandupdate pages 2-3). In eukaryotes more broadly, 18 families comprising 35 subfamilies have been identified, while prokaryotes show even greater diversity—42 families were found in 258 Pseudomonas genomes alone (cuatlayotlolarte2023aldehydedehydrogenasediversity pages 1-2). Key functional groups include:

- **ALDH1A subfamily (1A1, 1A2, 1A3)**: Retinaldehyde dehydrogenases involved in retinoic acid biosynthesis and embryonic development (moretti2016biochemicalandstructural pages 11-14).
- **ALDH2**: Mitochondrial acetaldehyde dehydrogenase, the primary enzyme of ethanol metabolism (moretti2016biochemicalandstructural pages 11-14, yoshida1998humanaldehydedehydrogenase pages 1-2).
- **ALDH3A subfamily**: Metabolizes medium- and long-chain aliphatic and aromatic aldehydes; ALDH3A1 also functions as a corneal crystallin (chen2013ocularaldehydedehydrogenases pages 2-4, vasiliou2013aldehydedehydrogenasesfrom pages 3-4).
- **ALDH4A1**: Glutamate γ-semialdehyde dehydrogenase in proline catabolism (moretti2016biochemicalandstructural pages 11-14, vasiliou2013aldehydedehydrogenasesfrom pages 3-4).
- **ALDH5A1**: Succinic semialdehyde dehydrogenase in GABA catabolism (moretti2016biochemicalandstructural pages 11-14, vasiliou2013aldehydedehydrogenasesfrom pages 3-4).
- **ALDH6A1**: Methylmalonate semialdehyde dehydrogenase in valine and pyrimidine catabolism (moretti2016biochemicalandstructural pages 11-14, vasiliou2013aldehydedehydrogenasesfrom pages 3-4).
- **ALDH7A1 (antiquitin)**: α-Aminoadipic semialdehyde dehydrogenase in lysine catabolism (moretti2016biochemicalandstructural pages 11-14, vasiliou2013aldehydedehydrogenasesfrom pages 3-4).
- **ALDH1L1/1L2**: 10-Formyltetrahydrofolate dehydrogenases—multi-domain fusion proteins containing an ALDH C-terminal domain, an N-terminal folate-binding domain, and an intermediate acyl carrier protein-like domain, functioning in folate one-carbon metabolism (heider2025thealdehydedehydrogenase pages 9-10, tsybovsky2022structureofputative pages 1-2, krupenko2009fdhanaldehyde pages 1-2).
- **ALDH18A1 (P5CS)**: Bifunctional Δ¹-pyrroline-5-carboxylate synthetase with an N-terminal amino-acid kinase domain and a C-terminal ALDH-like reductase domain. Catalyzes NADPH-dependent reduction (not oxidation) in proline and ornithine biosynthesis (brocker2013aldehydedehydrogenase(aldh) pages 14-18, heider2025thealdehydedehydrogenase pages 12-13, tola2020recentdevelopmenton pages 5-6).

### 3.2 Pseudoenzymes and Catalytically Dead Members

**ALDH16A1** is the best-characterized pseudoenzyme in the family. It lacks the catalytic Cys302 in mammalian and fish orthologs, cannot bind NAD+/NADH, and shows no measurable aldehyde oxidation activity when tested with multiple substrates including propanal, nonanal, acetaldehyde, and aminoadipate semialdehyde (liu2019crystalstructureof pages 11-13, liu2019crystalstructureof pages 8-10). Crystallographic analysis reveals it also lacks Asn165 and Glu261, the other two members of the catalytic triad (liu2019crystalstructureof pages 11-13). Structurally, ALDH16 is distinctive: it has an atypical C-terminal domain containing a 5-stranded Rossmann fold and β-flap, and it dimerizes via a novel interface not seen in other ALDHs (liu2019crystalstructureof pages 1-2, liu2019crystalstructureof pages 2-4). ALDH16A1 functions instead as a protein-interaction scaffold, associating with maspardin (linked to Mast syndrome/SPG21), and a missense mutation in ALDH16A1 is associated with hyperuricemia and gout, possibly through disrupted interaction with HPRT1 (liu2019crystalstructureof pages 11-13, vasiliou2013aldehydedehydrogenasesfrom pages 3-4, xanthis2023humanaldehydedehydrogenases pages 12-13). Recent work has also shown ALDH16A1 mediates thioredoxin lysosomal degradation in cancer cells (Bi et al. 2025).

Notably, frog and invertebrate ALDH16 orthologs retain the catalytic Cys, suggesting the pseudoenzyme state evolved independently in the mammalian/fish lineage (vasiliou2013aldehydedehydrogenasesfrom pages 4-6, vasiliou2013aldehydedehydrogenasesfrom pages 3-4).

### 3.3 Non-Enzymatic (Crystallin) Functions

Several ALDH family members have been co-opted as structural crystallin proteins in the eye. ALDH1A1 functions as a lens crystallin, while ALDH3A1 serves as a corneal crystallin (vasiliou2013aldehydedehydrogenasesfrom pages 3-4, vasiliou2013aldehydedehydrogenasesfrom pages 4-6, chen2013ocularaldehydedehydrogenases pages 2-4). In marine organisms, ALDH1A8 (η-crystallin) and ALDH1A9 (Ω-crystallin in scallop and cephalopods) serve as eye lens structural proteins (vasiliou2013aldehydedehydrogenasesfrom pages 4-6, xanthis2023humanaldehydedehydrogenases pages 30-31). These proteins provide UV radiation absorption, contribute to tissue transparency and refractive properties, and serve antioxidant functions beyond their catalytic roles (vasiliou2013aldehydedehydrogenasesfrom pages 4-6, chen2013ocularaldehydedehydrogenases pages 2-4). ALDH proteins also function as binding proteins for hormones, drugs, and endogenous compounds—ALDH1A1 binds androgens, thyroid hormones, and cholesterol (vasiliou2013aldehydedehydrogenasesfrom pages 3-4).

### 3.4 Fusion Enzymes

ALDH1L1 (FDH) is a product of natural fusion of three unrelated genes: an N-terminal methionyl-tRNA formyltransferase-like domain, an intermediate acyl carrier protein domain, and a C-terminal ALDH domain (tsybovsky2022structureofputative pages 1-2, strickland2011phylogenyandevolution pages 1-2). The ALDH domain retains all critical catalytic residues (including Cys707) and can oxidize short-chain aldehydes in vitro, but the whole-protein function is NADP+-dependent conversion of 10-formyltetrahydrofolate to tetrahydrofolate and CO₂ (tsybovsky2022structureofputative pages 1-2, strickland2011enzymaticpropertiesof pages 1-2). ALDH18A1 (P5CS) is similarly a bifunctional fusion protein (brocker2013aldehydedehydrogenase(aldh) pages 14-18, heider2025thealdehydedehydrogenase pages 12-13).

## 4. Taxonomic Scope

The ALDH superfamily is evolutionarily ancient and represented in all three domains of life: Archaea, Bacteria, and Eukarya (yoshida1998humanaldehydedehydrogenase pages 1-2, heider2025thealdehydedehydrogenase pages 5-8). Phylogenetic analysis indicates that present-day human ALDH genes derived from four ancestral genes that existed before the divergence of Eubacteria and Eukaryotes (yoshida1998humanaldehydedehydrogenase pages 1-2). The InterPro PTHR11699 entry spans 121,927 proteins across 29,468 taxa with 47 subfamilies.

In terms of family-specific distributions:
- **Humans** have 19 ALDH genes in 10 families (cuatlayotlolarte2023aldehydedehydrogenasediversity pages 1-2, vasiliou2005analysisandupdate pages 2-3).
- **Plants** have 14 families, with 10 core families shared among vascular plants and 8 of these also present in algae (zhang2012genomewideidentificationand pages 2-3, brocker2013aldehydedehydrogenase(aldh) pages 14-18).
- **Prokaryotes** show far greater diversity: 42 ALDH families were identified in 258 Pseudomonas genomes (6,510 total ALDHs), and 17 families with 31 subfamilies were found in Azospirillum (cuatlayotlolarte2023aldehydedehydrogenasediversity pages 1-2, cuatlayotlolarte2023aldehydedehydrogenasediversity pages 6-7).
- Some families show lineage-restricted distributions: ALDH10 has no mammalian orthologues, ALDH19 has been found only in tomato, ALDH21 and ALDH23 appear unique to mosses, and type II GGSALDHs (PutA proteins) occur only in bacteria (perozich2008relationshipswithinthe pages 7-8, zhang2012genomewideidentificationand pages 2-3, brocker2013aldehydedehydrogenase(aldh) pages 14-18).

This extreme taxonomic breadth means no single biological process GO term could be universally valid across all matched proteins. Processes like retinoic acid biosynthesis, ethanol detoxification, or GABA catabolism are lineage-specific and would incorrectly annotate prokaryotic or plant members.

## 5. Over-Annotation Verdict

The detailed assessment of whether GO terms should be added to PTHR11699 is summarized below:

| Assessment Aspect | Finding | Recommendation |
|---|---|---|
| Current mapping status | PTHR11699 currently has no InterPro2GO mappings. This top-level family spans 121,927 proteins across 29,468 taxa and includes many functionally distinct ALDH lineages, fusion proteins, and at least one pseudoenzyme, indicating strong functional heterogeneity at the family level (cuatlayotlolarte2023aldehydedehydrogenasediversity pages 1-2, liu2019crystalstructureof pages 11-13, xanthis2023humanaldehydedehydrogenases pages 12-13). | **ACCEPT** current state; keep no GO terms at this top-level entry. |
| Should generic aldehyde dehydrogenase activity be added? | No. Although many members catalyze NAD(P)+-dependent aldehyde oxidation, the family also includes ALDH16A1, which lacks the catalytic triad and measurable ALDH activity, and ALDH18A1/P5CS, whose ALDH-like domain participates in proline biosynthesis with modified chemistry rather than canonical aldehyde oxidation (xanthis2023humanaldehydedehydrogenases pages 12-13, heider2025thealdehydedehydrogenase pages 12-13, liu2019crystalstructureof pages 11-13). | **Do not add** a generic catalytic GO term at PTHR11699; if needed, map catalytic terms only to narrower child entries/subfamilies where universally valid. |
| Should NAD binding be added? | No. Cofactor usage is not uniform: canonical ALDHs may use NAD+ or NADP+, ALDH1L1/ALDH1L2 are specialized folate-enzyme fusions using NADP+, and ALDH16A1 appears unable to bind NAD+/NADH in the canonical way. A generic "NAD binding" term would therefore be both over-broad and inaccurate for some members (heider2025thealdehydedehydrogenase pages 3-5, liu2019crystalstructureof pages 8-10, heider2025thealdehydedehydrogenase pages 9-10, tsybovsky2022structureofputative pages 1-2). | **Do not add** NAD/NADP binding terms at this family level. |
| Should any biological process term be added? | No. Members participate in many unrelated processes across taxa, including retinoic acid biosynthesis, ethanol/acetaldehyde detoxification, GABA catabolism, lysine catabolism, proline biosynthesis, folate/one-carbon metabolism, osmoprotection, and eye crystallin-associated structural/protective roles. No single process term is true for every matched protein across Bacteria, Archaea, and Eukarya (moretti2016biochemicalandstructural pages 11-14, vasiliou2013aldehydedehydrogenasesfrom pages 3-4, brocker2013aldehydedehydrogenase(aldh) pages 14-18, tola2020recentdevelopmenton pages 5-6, yoshida1998humanaldehydedehydrogenase pages 1-2, heider2025thealdehydedehydrogenase pages 5-8, heider2025thealdehydedehydrogenase pages 9-10). | **Do not add** any process term to PTHR11699; place pathway/process GO terms only on specific descendant families. |
| Overall verdict | The absence of GO terms is appropriate because PTHR11699 is a broad, top-level ALDH family containing canonical enzymes, specialized semialdehyde dehydrogenases, fusion enzymes, multifunctional proteins, and pseudoenzymes. Any family-wide GO mapping would likely over-annotate at least some matched proteins (cuatlayotlolarte2023aldehydedehydrogenasediversity pages 1-2, brocker2013aldehydedehydrogenase(aldh) pages 14-18, liu2019crystalstructureof pages 11-13, heider2025thealdehydedehydrogenase pages 9-10). | **ACCEPT** — retain no InterPro2GO mappings for PTHR11699; annotate only at more specific child/subfamily levels. |


*Table: This table summarizes whether GO terms should be added to the broad InterPro family PTHR11699. It shows that the current absence of InterPro2GO mappings is appropriate because the family is too functionally heterogeneous for safe family-wide annotation.*

### 5.1 Summary Verdict: **ACCEPT — No GO Terms at This Level**

The current state of PTHR11699 having **no InterPro2GO mappings** is **appropriate and should be maintained**. The rationale is:

1. **Entry type is "family"**, which in principle can support whole-protein function terms—but only when the family is functionally homogeneous. PTHR11699 is demonstrably **not** functionally homogeneous, encompassing at least 47 subfamilies with divergent substrate specificities, reaction directions, and even non-catalytic members (heider2025thealdehydedehydrogenase pages 1-3, heider2025thealdehydedehydrogenase pages 18-20).

2. **Pseudoenzyme members** (ALDH16A1) lack catalytic activity entirely and would be incorrectly annotated with any enzymatic GO term (xanthis2023humanaldehydedehydrogenases pages 12-13, liu2019crystalstructureof pages 11-13, liu2019crystalstructureof pages 8-10).

3. **Reductase members** (ALDH18A1/P5CS) catalyze the opposite direction of the canonical ALDH reaction—NADPH-dependent reduction rather than NAD(P)+-dependent oxidation—with a modified catalytic triad (heider2025thealdehydedehydrogenase pages 12-13).

4. **Fusion enzyme members** (ALDH1L1/1L2) use the ALDH domain in a non-standard metabolic context (folate metabolism), making generic ALDH activity terms misleading at the whole-protein level (heider2025thealdehydedehydrogenase pages 9-10, tsybovsky2022structureofputative pages 1-2).

5. **Non-enzymatic functions** (crystallins, hormone binding) are specific to certain lineages and subfamily members (vasiliou2013aldehydedehydrogenasesfrom pages 3-4, vasiliou2013aldehydedehydrogenasesfrom pages 4-6).

### 5.2 Recommended GO Action Pattern

| Action | Details |
|---|---|
| **For PTHR11699 (top-level)** | **ACCEPT** current no-mapping state. Do not add any GO terms. |
| **For PTHR11699 subfamilies** | **Recommend** mapping appropriate GO terms to specific child entries/subfamilies where functional homogeneity is established. For example, ALDH2-specific subfamilies could receive "aldehyde dehydrogenase [NAD+] activity" (GO:0004029) and "ethanol oxidation" process terms. |
| **InterPro recommendation** | The 47 subfamilies structure already provides the framework for subfamily-level GO annotation. InterPro should ensure that PANTHER subfamily signatures (PTHR11699:SFxxxxx) carry appropriate, subfamily-specific GO terms rather than attempting family-wide mappings. |

This approach ensures that the ~121,927 proteins matched by PTHR11699 are not uniformly stamped with GO terms that are only valid for a subset, while still enabling accurate annotation through the subfamily hierarchy.

References

1. (heider2025thealdehydedehydrogenase pages 1-3): Johann Heider and Dominik Hege. The aldehyde dehydrogenase superfamilies: correlations and deviations in structure and function. Applied Microbiology and Biotechnology, Apr 2025. URL: https://doi.org/10.1007/s00253-025-13467-5, doi:10.1007/s00253-025-13467-5. This article has 13 citations and is from a domain leading peer-reviewed journal.

2. (heider2025thealdehydedehydrogenase pages 3-5): Johann Heider and Dominik Hege. The aldehyde dehydrogenase superfamilies: correlations and deviations in structure and function. Applied Microbiology and Biotechnology, Apr 2025. URL: https://doi.org/10.1007/s00253-025-13467-5, doi:10.1007/s00253-025-13467-5. This article has 13 citations and is from a domain leading peer-reviewed journal.

3. (shortall2021insightsintoaldehyde pages 2-4): Kim Shortall, Ahmed Djeghader, Edmond Magner, and Tewfik Soulimane. Insights into aldehyde dehydrogenase enzymes: a structural perspective. Frontiers in Molecular Biosciences, May 2021. URL: https://doi.org/10.3389/fmolb.2021.659550, doi:10.3389/fmolb.2021.659550. This article has 203 citations.

4. (heider2025thealdehydedehydrogenase pages 5-8): Johann Heider and Dominik Hege. The aldehyde dehydrogenase superfamilies: correlations and deviations in structure and function. Applied Microbiology and Biotechnology, Apr 2025. URL: https://doi.org/10.1007/s00253-025-13467-5, doi:10.1007/s00253-025-13467-5. This article has 13 citations and is from a domain leading peer-reviewed journal.

5. (hempel1993aldehydedehydrogenaseswidespread pages 1-2): John Hempel, Hugh Nicholas, and Ronald Lindahl. Aldehyde dehydrogenases: widespread structural and functional diversity within a shared framework. Protein Science, 2:1890-1900, Nov 1993. URL: https://doi.org/10.1002/pro.5560021111, doi:10.1002/pro.5560021111. This article has 230 citations and is from a peer-reviewed journal.

6. (perozich2008relationshipswithinthe pages 4-5): John Perozich, Hugh Nicholas, Bi‐Cheng Wang, Ronald Lindahl, and John Hempel. Relationships within the aldehyde dehydrogenase extended family. Protein Science, 8:137-146, Dec 2008. URL: https://doi.org/10.1110/ps.8.1.137, doi:10.1110/ps.8.1.137. This article has 368 citations and is from a peer-reviewed journal.

7. (moretti2016biochemicalandstructural pages 11-14): ANDREA MORETTI. Biochemical and structural investigation on human aldh1a3. Text, Jan 2016. URL: https://doi.org/10.20373/uniupo/openthesis/115178, doi:10.20373/uniupo/openthesis/115178. This article has 0 citations and is from a peer-reviewed journal.

8. (yoshida1998humanaldehydedehydrogenase pages 1-2): Akira Yoshida, Andrey Rzhetsky, Lily C. Hsu, and Cheng Chang. Human aldehyde dehydrogenase gene family. European journal of biochemistry, 251 3:549-57, Feb 1998. URL: https://doi.org/10.1046/j.1432-1327.1998.2510549.x, doi:10.1046/j.1432-1327.1998.2510549.x. This article has 629 citations.

9. (vasiliou2013aldehydedehydrogenasesfrom pages 3-4): Vasilis Vasiliou, David C. Thompson, Clay Smith, Mayumi Fujita, and Ying Chen. Aldehyde dehydrogenases: from eye crystallins to metabolic disease and cancer stem cells. Chemico-biological interactions, 202 1-3:2-10, Feb 2013. URL: https://doi.org/10.1016/j.cbi.2012.10.026, doi:10.1016/j.cbi.2012.10.026. This article has 185 citations and is from a peer-reviewed journal.

10. (chen2013ocularaldehydedehydrogenases pages 2-4): Ying Chen, David C. Thompson, Vindhya Koppaka, James V. Jester, and Vasilis Vasiliou. Ocular aldehyde dehydrogenases: protection against ultraviolet damage and maintenance of transparency for vision. Progress in Retinal and Eye Research, 33:28-39, Mar 2013. URL: https://doi.org/10.1016/j.preteyeres.2012.10.001, doi:10.1016/j.preteyeres.2012.10.001. This article has 117 citations and is from a highest quality peer-reviewed journal.

11. (heider2025thealdehydedehydrogenase pages 9-10): Johann Heider and Dominik Hege. The aldehyde dehydrogenase superfamilies: correlations and deviations in structure and function. Applied Microbiology and Biotechnology, Apr 2025. URL: https://doi.org/10.1007/s00253-025-13467-5, doi:10.1007/s00253-025-13467-5. This article has 13 citations and is from a domain leading peer-reviewed journal.

12. (tsybovsky2022structureofputative pages 1-2): Yaroslav Tsybovsky, Valentin Sereda, Marcin Golczak, Natalia I. Krupenko, and Sergey A. Krupenko. Structure of putative tumor suppressor aldh1l1. Communications Biology, Jan 2022. URL: https://doi.org/10.1038/s42003-021-02963-9, doi:10.1038/s42003-021-02963-9. This article has 13 citations and is from a peer-reviewed journal.

13. (krupenko2009fdhanaldehyde pages 1-2): Sergey A. Krupenko. Fdh: an aldehyde dehydrogenase fusion enzyme in folate metabolism. Chemico-biological interactions, 178 1-3:84-93, Mar 2009. URL: https://doi.org/10.1016/j.cbi.2008.09.007, doi:10.1016/j.cbi.2008.09.007. This article has 123 citations and is from a peer-reviewed journal.

14. (xanthis2023humanaldehydedehydrogenases pages 12-13): Vasileios Xanthis, Theodora Mantso, Anna Dimtsi, Aglaia Pappa, and Vasiliki E. Fadouloglou. Human aldehyde dehydrogenases: a superfamily of similar yet different proteins highly related to cancer. Cancers, 15:4419, Sep 2023. URL: https://doi.org/10.3390/cancers15174419, doi:10.3390/cancers15174419. This article has 32 citations.

15. (liu2019crystalstructureof pages 11-13): Li-Kai Liu and John J. Tanner. Crystal structure of aldehyde dehydrogenase 16 reveals trans-hierarchical structural similarity and a new dimer. Journal of molecular biology, 431 3:524-541, Feb 2019. URL: https://doi.org/10.1016/j.jmb.2018.11.030, doi:10.1016/j.jmb.2018.11.030. This article has 27 citations and is from a domain leading peer-reviewed journal.

16. (liu2019crystalstructureof pages 8-10): Li-Kai Liu and John J. Tanner. Crystal structure of aldehyde dehydrogenase 16 reveals trans-hierarchical structural similarity and a new dimer. Journal of molecular biology, 431 3:524-541, Feb 2019. URL: https://doi.org/10.1016/j.jmb.2018.11.030, doi:10.1016/j.jmb.2018.11.030. This article has 27 citations and is from a domain leading peer-reviewed journal.

17. (brocker2013aldehydedehydrogenase(aldh) pages 14-18): Chad Brocker, Melpomene Vasiliou, Sarah Carpenter, Christopher Carpenter, Yucheng Zhang, Xiping Wang, Simeon O. Kotchoni, Andrew J. Wood, Hans-Hubert Kirch, David Kopečný, Daniel W. Nebert, and Vasilis Vasiliou. Aldehyde dehydrogenase (aldh) superfamily in plants: gene nomenclature and comparative genomics. Planta, 237:189-210, Sep 2013. URL: https://doi.org/10.1007/s00425-012-1749-0, doi:10.1007/s00425-012-1749-0. This article has 228 citations and is from a peer-reviewed journal.

18. (heider2025thealdehydedehydrogenase pages 12-13): Johann Heider and Dominik Hege. The aldehyde dehydrogenase superfamilies: correlations and deviations in structure and function. Applied Microbiology and Biotechnology, Apr 2025. URL: https://doi.org/10.1007/s00253-025-13467-5, doi:10.1007/s00253-025-13467-5. This article has 13 citations and is from a domain leading peer-reviewed journal.

19. (tola2020recentdevelopmenton pages 5-6): Adesola J. Tola, Amal Jaballi, Hugo Germain, and Tagnon D. Missihoun. Recent development on plant aldehyde dehydrogenase enzymes and their functions in plant development and stress signaling. Genes, 12:51, Dec 2020. URL: https://doi.org/10.3390/genes12010051, doi:10.3390/genes12010051. This article has 106 citations.

20. (cuatlayotlolarte2023aldehydedehydrogenasediversity pages 1-2): Ricardo Cuatlayotl-Olarte, María Luisa Xiqui-Vázquez, Sandra Raquel Reyes-Carmona, Claudia Mancilla-Simbro, Beatriz Eugenia Baca, and Alberto Ramírez-Mata. Aldehyde dehydrogenase diversity in azospirillum genomes. Diversity, 15:1178, Nov 2023. URL: https://doi.org/10.3390/d15121178, doi:10.3390/d15121178. This article has 5 citations.

21. (vasiliou2005analysisandupdate pages 2-3): Vasilis Vasiliou and Daniel W. Nebert. Analysis and update of the human aldehyde dehydrogenase (aldh) gene family. Human Genomics, 2:138-143, Jun 2005. URL: https://doi.org/10.1186/1479-7364-2-2-138, doi:10.1186/1479-7364-2-2-138. This article has 546 citations and is from a peer-reviewed journal.

22. (liu2019crystalstructureof pages 1-2): Li-Kai Liu and John J. Tanner. Crystal structure of aldehyde dehydrogenase 16 reveals trans-hierarchical structural similarity and a new dimer. Journal of molecular biology, 431 3:524-541, Feb 2019. URL: https://doi.org/10.1016/j.jmb.2018.11.030, doi:10.1016/j.jmb.2018.11.030. This article has 27 citations and is from a domain leading peer-reviewed journal.

23. (liu2019crystalstructureof pages 2-4): Li-Kai Liu and John J. Tanner. Crystal structure of aldehyde dehydrogenase 16 reveals trans-hierarchical structural similarity and a new dimer. Journal of molecular biology, 431 3:524-541, Feb 2019. URL: https://doi.org/10.1016/j.jmb.2018.11.030, doi:10.1016/j.jmb.2018.11.030. This article has 27 citations and is from a domain leading peer-reviewed journal.

24. (vasiliou2013aldehydedehydrogenasesfrom pages 4-6): Vasilis Vasiliou, David C. Thompson, Clay Smith, Mayumi Fujita, and Ying Chen. Aldehyde dehydrogenases: from eye crystallins to metabolic disease and cancer stem cells. Chemico-biological interactions, 202 1-3:2-10, Feb 2013. URL: https://doi.org/10.1016/j.cbi.2012.10.026, doi:10.1016/j.cbi.2012.10.026. This article has 185 citations and is from a peer-reviewed journal.

25. (xanthis2023humanaldehydedehydrogenases pages 30-31): Vasileios Xanthis, Theodora Mantso, Anna Dimtsi, Aglaia Pappa, and Vasiliki E. Fadouloglou. Human aldehyde dehydrogenases: a superfamily of similar yet different proteins highly related to cancer. Cancers, 15:4419, Sep 2023. URL: https://doi.org/10.3390/cancers15174419, doi:10.3390/cancers15174419. This article has 32 citations.

26. (strickland2011phylogenyandevolution pages 1-2): Kyle C. Strickland, Roger S. Holmes, Natalia V. Oleinik, Natalia I. Krupenko, and Sergey A. Krupenko. Phylogeny and evolution of aldehyde dehydrogenase-homologous folate enzymes. Chemico-biological interactions, 191 1-3:122-8, May 2011. URL: https://doi.org/10.1016/j.cbi.2010.12.025, doi:10.1016/j.cbi.2010.12.025. This article has 18 citations and is from a peer-reviewed journal.

27. (strickland2011enzymaticpropertiesof pages 1-2): Kyle C. Strickland, Natalia I. Krupenko, Marianne E. Dubard, Calvin J. Hu, Yaroslav Tsybovsky, and Sergey A. Krupenko. Enzymatic properties of aldh1l2, a mitochondrial 10-formyltetrahydrofolate dehydrogenase. Chemico-biological interactions, 191 1-3:129-36, May 2011. URL: https://doi.org/10.1016/j.cbi.2011.01.008, doi:10.1016/j.cbi.2011.01.008. This article has 51 citations and is from a peer-reviewed journal.

28. (zhang2012genomewideidentificationand pages 2-3): Yucheng Zhang, Linyong Mao, Hua Wang, Chad Brocker, Xiangjing Yin, Vasilis Vasiliou, Zhangjun Fei, and Xiping Wang. Genome-wide identification and analysis of grape aldehyde dehydrogenase (aldh) gene superfamily. PLoS ONE, 7:e32153, Feb 2012. URL: https://doi.org/10.1371/journal.pone.0032153, doi:10.1371/journal.pone.0032153. This article has 152 citations and is from a peer-reviewed journal.

29. (cuatlayotlolarte2023aldehydedehydrogenasediversity pages 6-7): Ricardo Cuatlayotl-Olarte, María Luisa Xiqui-Vázquez, Sandra Raquel Reyes-Carmona, Claudia Mancilla-Simbro, Beatriz Eugenia Baca, and Alberto Ramírez-Mata. Aldehyde dehydrogenase diversity in azospirillum genomes. Diversity, 15:1178, Nov 2023. URL: https://doi.org/10.3390/d15121178, doi:10.3390/d15121178. This article has 5 citations.

30. (perozich2008relationshipswithinthe pages 7-8): John Perozich, Hugh Nicholas, Bi‐Cheng Wang, Ronald Lindahl, and John Hempel. Relationships within the aldehyde dehydrogenase extended family. Protein Science, 8:137-146, Dec 2008. URL: https://doi.org/10.1110/ps.8.1.137, doi:10.1110/ps.8.1.137. This article has 368 citations and is from a peer-reviewed journal.

31. (heider2025thealdehydedehydrogenase pages 18-20): Johann Heider and Dominik Hege. The aldehyde dehydrogenase superfamilies: correlations and deviations in structure and function. Applied Microbiology and Biotechnology, Apr 2025. URL: https://doi.org/10.1007/s00253-025-13467-5, doi:10.1007/s00253-025-13467-5. This article has 13 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PTHR11699-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR11699-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. heider2025thealdehydedehydrogenase pages 3-5
2. shortall2021insightsintoaldehyde pages 2-4
3. heider2025thealdehydedehydrogenase pages 5-8
4. perozich2008relationshipswithinthe pages 4-5
5. heider2025thealdehydedehydrogenase pages 12-13
6. liu2019crystalstructureof pages 8-10
7. yoshida1998humanaldehydedehydrogenase pages 1-2
8. cuatlayotlolarte2023aldehydedehydrogenasediversity pages 1-2
9. moretti2016biochemicalandstructural pages 11-14
10. liu2019crystalstructureof pages 11-13
11. vasiliou2013aldehydedehydrogenasesfrom pages 3-4
12. heider2025thealdehydedehydrogenase pages 1-3
13. hempel1993aldehydedehydrogenaseswidespread pages 1-2
14. chen2013ocularaldehydedehydrogenases pages 2-4
15. heider2025thealdehydedehydrogenase pages 9-10
16. tsybovsky2022structureofputative pages 1-2
17. krupenko2009fdhanaldehyde pages 1-2
18. xanthis2023humanaldehydedehydrogenases pages 12-13
19. tola2020recentdevelopmenton pages 5-6
20. vasiliou2005analysisandupdate pages 2-3
21. liu2019crystalstructureof pages 1-2
22. liu2019crystalstructureof pages 2-4
23. vasiliou2013aldehydedehydrogenasesfrom pages 4-6
24. xanthis2023humanaldehydedehydrogenases pages 30-31
25. strickland2011phylogenyandevolution pages 1-2
26. strickland2011enzymaticpropertiesof pages 1-2
27. zhang2012genomewideidentificationand pages 2-3
28. cuatlayotlolarte2023aldehydedehydrogenasediversity pages 6-7
29. perozich2008relationshipswithinthe pages 7-8
30. heider2025thealdehydedehydrogenase pages 18-20
31. NAD(P)+
32. NAD+
33. https://doi.org/10.1007/s00253-025-13467-5,
34. https://doi.org/10.3389/fmolb.2021.659550,
35. https://doi.org/10.1002/pro.5560021111,
36. https://doi.org/10.1110/ps.8.1.137,
37. https://doi.org/10.20373/uniupo/openthesis/115178,
38. https://doi.org/10.1046/j.1432-1327.1998.2510549.x,
39. https://doi.org/10.1016/j.cbi.2012.10.026,
40. https://doi.org/10.1016/j.preteyeres.2012.10.001,
41. https://doi.org/10.1038/s42003-021-02963-9,
42. https://doi.org/10.1016/j.cbi.2008.09.007,
43. https://doi.org/10.3390/cancers15174419,
44. https://doi.org/10.1016/j.jmb.2018.11.030,
45. https://doi.org/10.1007/s00425-012-1749-0,
46. https://doi.org/10.3390/genes12010051,
47. https://doi.org/10.3390/d15121178,
48. https://doi.org/10.1186/1479-7364-2-2-138,
49. https://doi.org/10.1016/j.cbi.2010.12.025,
50. https://doi.org/10.1016/j.cbi.2011.01.008,
51. https://doi.org/10.1371/journal.pone.0032153,