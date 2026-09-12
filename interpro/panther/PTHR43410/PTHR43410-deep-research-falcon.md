---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T21:30:30.041960'
end_time: '2026-06-28T21:53:55.364723'
duration_seconds: 1405.32
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR43410
  interpro_name: Nitric Oxide Synthase (NOS)
  interpro_short_name: NOS
  interpro_type: family
  interpro_integrated: IPR050607
  member_databases: Not specified
  n_proteins: '8119'
  n_taxa: '7081'
  n_subfamilies: '4'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: The Nitric Oxide Synthase (NOS) family is responsible for
    the production of nitric oxide (NO), a versatile messenger molecule with a wide
    range of biological functions. Members of the NOS family catalyze the conversion
    of L-arginine to L-citrulline, releasing NO in the process. NO plays a critical
    role in various physiological processes including neurotransmission, vascular
    smooth muscle relaxation, immune response, and regulation of gene expression.
    The family includes inducible forms that are stimulated by inflammatory signals
    and constitutive forms that are regulated by calcium/calmodulin. Some NOS proteins
    also exhibit nitrosylase activity, mediating the S-nitrosylation of cytoplasmic
    target proteins, which can affect their function and activity.
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 30
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: PTHR43410-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR43410-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: PTHR43410-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# InterPro Family Research for GO Annotation Review

## ⚠️ CRITICAL: Family Identification Context

**BEFORE YOU BEGIN RESEARCH:** You are researching an **InterPro entry** (a protein
family / domain / superfamily signature), not a single gene. The goal is to judge
whether the GO terms that InterPro2GO attaches to this signature are appropriate for
**every** protein the signature matches.

### Target InterPro Entry (from the InterPro API):
- **Accession:** PTHR43410
- **Name:** Nitric Oxide Synthase (NOS)
- **Short name:** NOS
- **Entry type:** family
- **Integrated into / parent:** IPR050607
- **Member database signatures:** Not specified
- **Scale:** 8119 proteins across 7081 taxa, 4 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The Nitric Oxide Synthase (NOS) family is responsible for the production of nitric oxide (NO), a versatile messenger molecule with a wide range of biological functions. Members of the NOS family catalyze the conversion of L-arginine to L-citrulline, releasing NO in the process. NO plays a critical role in various physiological processes including neurotransmission, vascular smooth muscle relaxation, immune response, and regulation of gene expression. The family includes inducible forms that are stimulated by inflammatory signals and constitutive forms that are regulated by calcium/calmodulin. Some NOS proteins also exhibit nitrosylase activity, mediating the S-nitrosylation of cytoplasmic target proteins, which can affect their function and activity.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR43410 (Nitric Oxide Synthase (NOS))**, structured to support GO annotation review.

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
- **Accession:** PTHR43410
- **Name:** Nitric Oxide Synthase (NOS)
- **Short name:** NOS
- **Entry type:** family
- **Integrated into / parent:** IPR050607
- **Member database signatures:** Not specified
- **Scale:** 8119 proteins across 7081 taxa, 4 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The Nitric Oxide Synthase (NOS) family is responsible for the production of nitric oxide (NO), a versatile messenger molecule with a wide range of biological functions. Members of the NOS family catalyze the conversion of L-arginine to L-citrulline, releasing NO in the process. NO plays a critical role in various physiological processes including neurotransmission, vascular smooth muscle relaxation, immune response, and regulation of gene expression. The family includes inducible forms that are stimulated by inflammatory signals and constitutive forms that are regulated by calcium/calmodulin. Some NOS proteins also exhibit nitrosylase activity, mediating the S-nitrosylation of cytoplasmic target proteins, which can affect their function and activity.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR43410 (Nitric Oxide Synthase (NOS))**, structured to support GO annotation review.

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


# Comprehensive Research Report: InterPro Entry PTHR43410 — Nitric Oxide Synthase (NOS) Family

## 1. Family Definition and Biochemistry

### 1.1 Catalytic Mechanism and Reaction

The Nitric Oxide Synthase (NOS) family catalyzes the NADPH- and O₂-dependent oxidation of L-arginine to L-citrulline and nitric oxide (NO) via a five-electron oxidation mechanism (chen2022nitricoxidenitric pages 4-6). The reaction proceeds in two sequential monooxygenation steps: first, L-arginine is hydroxylated at its terminal guanidinium nitrogen to form the intermediate Nω-hydroxy-L-arginine (NOHA); second, NOHA is further oxidized to yield L-citrulline and NO (chen2022nitricoxidenitric pages 4-6).

### 1.2 Domain Architecture

Mammalian NOS enzymes are homodimeric proteins (~131 kDa per subunit for iNOS) with a bi-domain architecture: an N-terminal oxygenase domain containing a cytochrome P-450-type heme active site, tetrahydrobiopterin (BH4) binding site, and substrate-binding pocket, and a C-terminal reductase domain containing FAD, FMN, and NADPH binding sites. These two functional domains are connected by a calmodulin (CaM)-binding linker region (cinelli2020induciblenitricoxide pages 3-5, krol2020humannitricoxide pages 3-5, serreli2023roleofdietary pages 4-5). Electron transfer proceeds from NADPH → FAD → FMN in one subunit, then crosses to the heme in the oxygenase domain of the opposing monomer, requiring a conformational change in which the enzyme "folds nearly in half" to bring FMN into proximity with the heme (cinelli2020induciblenitricoxide pages 3-5).

### 1.3 Cofactors and Conserved Residues

All mammalian NOS enzymes require five cofactors: NADPH, FAD, FMN, heme (iron protoporphyrin IX), and BH4. A catalytically inactive zinc ion at the dimer interface forms a zinc-tetrathiolate cluster that stabilizes the homodimer (cinelli2020induciblenitricoxide pages 3-5, verde2023noandheme pages 13-15). Critical residues in the BH4-binding pocket include Arg375, Trp455, Trp457, and Phe470 (cinelli2020induciblenitricoxide pages 3-5). A conserved proximal cysteine coordinates the heme-iron and interacts with a tryptophan residue to increase heme redox potential. Additional conserved residues (tyrosine, tryptophan, glutamate) form hydrogen bonds with substrate arginine at the heme's distal side (chen2022nitricoxidenitric pages 6-8). The catalytic center features a conserved triangular arrangement of heme, pterin cofactor, and substrate arginine, stabilized by hydrogen bonds (chen2022nitricoxidenitric pages 6-8).

Bacterial NOS (bNOS) enzymes share >40% amino acid sequence identity in the oxygenase domain with mammalian NOS but differ substantially in overall organization. They typically possess only the oxygenase domain, lacking the reductase domain, β-hairpin hook, and canonical Cys-X₄-Cys zinc-binding module (chen2022nitricoxidenitric pages 4-6, chen2022nitricoxidenitric pages 6-8). bNOS enzymes use tetrahydrofolate (FH4) instead of BH4 as their pterin cofactor, with thousand-fold differences in pterin binding affinities relative to mammalian NOS (chen2022nitricoxidenitric pages 14-15). They require separate external reductase partners as electron donors (porrini2020dr.noand pages 13-16).

### 1.4 Structural Fold

NOS belongs to the cytochrome P-450 structural superfamily in its oxygenase domain, while the reductase domain shares homology with cytochrome P-450 reductase/diflavin oxidoreductases. The heme-containing catalytic pocket for substrate binding is highly conserved across all NOS family members, from bacteria to mammals (serreli2023roleofdietary pages 4-5, chen2022nitricoxidenitric pages 14-15).

## 2. InterPro2GO Mapping Appropriateness

The InterPro entry PTHR43410 currently has **no InterPro2GO terms mapped**. This section evaluates whether candidate GO terms would be appropriate if they were to be added. The following table provides a detailed assessment of candidate GO terms:

| GO term ID | GO term name | GO aspect (MF/BP/CC) | Would it be correct for ALL 8119 proteins? | Risk of over-annotation | Recommendation | Rationale |
|---|---|---|---|---|---|---|
| GO:0004517 | nitric oxide synthase activity | MF | Probably not safely for all matches | Medium | MODIFY | This is the closest family-core term because catalytically competent NOS proteins share the conserved heme-centered oxidation of L-arginine to NO and citrulline across metazoan and bacterial NOSs. However, the family includes highly derived/truncated NOS-like proteins in some ctenophores and broad taxonomic diversity, so catalytic competence should ideally be confirmed at child-entry or protein level rather than assumed for every family match (cinelli2020induciblenitricoxide pages 3-5, chen2022nitricoxidenitric pages 4-6, moroz2023nitricoxidesignaling pages 2-4, moroz2023nitricoxidesignaling pages 4-6, chen2022nitricoxidenitric pages 14-15). |
| GO:0006809 | nitric oxide biosynthetic process | BP | Probably not safely for all matches | Medium | KEEP_AS_NON_CORE | If a protein truly has NOS catalytic activity, participation in NO biosynthesis usually follows. But this is a whole-organism/process inference that becomes less safe across truncated/divergent homologs and across taxa with very different biological deployment of NO; better as a non-core consequence of validated catalytic members, not as a blanket family mapping (chen2022nitricoxidenitric pages 4-6, chen2022nitricoxidenitric pages 3-4, moroz2023nitricoxidesignaling pages 2-4, chen2022nitricoxidenitric pages 1-3). |
| GO:0005506 | iron ion binding | MF | No | High | REMOVE | NOS active sites use heme iron, but mapping generic iron ion binding adds little specificity and can be misleading because the relevant chemistry is more specifically heme/cofactor-associated. Generic metal-binding terms are low-information and inferior to heme-related terms where warranted (chen2022nitricoxidenitric pages 6-8, serreli2023roleofdietary pages 4-5, verde2023noandheme pages 13-15, chen2022nitricoxidenitric pages 14-15). |
| GO:0050660 | flavin adenine dinucleotide binding | MF | No | High | REMOVE | Full-length metazoan NOS reductase domains bind FAD, but most bacterial NOS proteins are oxygenase-only and lack the reductase domain entirely. Therefore FAD binding is not true across the family and would systematically over-annotate bNOS and other reduced architectures (cinelli2020induciblenitricoxide pages 3-5, chen2022nitricoxidenitric pages 6-8, chen2022nitricoxidenitric pages 4-6, porrini2020dr.noand pages 13-16, chen2022nitricoxidenitric pages 14-15). |
| GO:0010181 | FMN binding | MF | No | High | REMOVE | As with FAD binding, FMN binding applies to full-length metazoan reductase domains but not to the common bacterial oxygenase-only NOS architecture. This is false for a major fraction of the family and should not be mapped at parent-family level (cinelli2020induciblenitricoxide pages 3-5, krol2020humannitricoxide pages 3-5, chen2022nitricoxidenitric pages 4-6, chen2022nitricoxidenitric pages 6-8, chen2022nitricoxidenitric pages 14-15). |
| GO:0020037 | heme binding | MF | Probably yes for catalytically competent NOSs, but not completely safe for all matches | Medium | MODIFY | Heme is central to NOS catalysis and the oxygenase domain is heme-containing across mammalian and bacterial NOS enzymes. Still, because the entry spans divergent and possibly truncated members, and because heme binding is more generic than the catalytic activity itself, it is better treated cautiously and possibly moved to a more functionally homogeneous child entry if available (chen2022nitricoxidenitric pages 6-8, serreli2023roleofdietary pages 4-5, verde2023noandheme pages 13-15, chen2022nitricoxidenitric pages 14-15). |
| GO:0005829 | cytosol | CC | No | High | REMOVE | Cellular localization differs substantially: eNOS is associated with caveolae/Golgi, nNOS can be scaffolded via PDZ interactions, iNOS can associate with intracellular compartments, and taxa outside vertebrates have very different cell biology. A universal cytosol assignment would be wrong across many clades (giordano2022nitricoxideproduction pages 4-6, locascio2023nitricoxidefunction pages 4-5, serreli2023roleofdietary pages 4-5, chen2022nitricoxidenitric pages 1-3). |
| GO:0007218 | neuropeptide signaling pathway | BP | No | Very high | REMOVE | This is not a core NOS family function. NOS1 participates in neuronal signaling in vertebrates, but many NOS proteins are endothelial, inducible immune, bacterial stress/virulence enzymes, or natural-product biosynthetic enzymes. Applying this at family level would be severe over-annotation (krol2020humannitricoxide pages 3-5, locascio2023nitricoxidefunction pages 4-5, serreli2023roleofdietary pages 4-5, chen2022nitricoxidenitric pages 1-3, chen2022nitricoxidenitric pages 11-12). |
| GO:0045429 | positive regulation of nitric oxide biosynthetic process | BP | No | Very high | REMOVE | NOS enzymes catalyze NO biosynthesis; they are not generally positive regulators of that process in the GO sense. This term describes upstream regulation, not the core enzyme activity, and would confuse catalytic role with regulatory role (cinelli2020induciblenitricoxide pages 3-5, krol2020humannitricoxide pages 3-5, chen2022nitricoxidenitric pages 4-6). |
| GO:0006954 | inflammatory response | BP | No | Very high | REMOVE | Inflammatory-response involvement is specific to vertebrate inducible NOS2/iNOS and related immunobiology. It is inapplicable to bacterial NOS, endothelial NOS, neuronal NOS, and many non-vertebrate NOS homologs (giordano2022nitricoxideproduction pages 4-6, krol2020humannitricoxide pages 3-5, locascio2023nitricoxidefunction pages 4-5, serreli2023roleofdietary pages 2-4, chen2022nitricoxidenitric pages 1-3, porrini2020dr.noand pages 13-16). |
| GO:0042311 | vasodilation | BP | No | Very high | REMOVE | Vasodilation is a vertebrate eNOS/NOS3-associated physiological outcome and is absent from bacteria and non-vascular organisms. Even within vertebrates it is not true for all NOS paralogs, making it unsuitable for the parent family entry (krol2020humannitricoxide pages 3-5, locascio2023nitricoxidefunction pages 4-5, serreli2023roleofdietary pages 2-4, serreli2023roleofdietary pages 4-5). |


*Table: This table evaluates candidate GO terms for the InterPro NOS family PTHR43410 against the requirement that a family-level mapping be correct for all matched proteins. It highlights that only the core catalytic function is potentially supportable, whereas most binding, process, and component terms are over-broad or clade-specific.*

### Summary Assessment

The absence of InterPro2GO terms for PTHR43410 is largely appropriate given the functional heterogeneity of the family. A few candidate GO terms merit discussion:

- **GO:0004517 (nitric oxide synthase activity, MF)**: This is the strongest candidate for family-wide mapping because the core catalytic chemistry (L-arginine → L-citrulline + NO) is conserved across catalytically competent members from bacteria through vertebrates (chen2022nitricoxidenitric pages 4-6, chen2022nitricoxidenitric pages 14-15). However, the family includes truncated and highly derived members (e.g., certain ctenophore NOS with modified FAD-binding domains) whose catalytic competence is uncertain (moroz2023nitricoxidesignaling pages 2-4, moroz2023nitricoxidesignaling pages 4-6). A cautious approach would be to apply this term only at child-entry level.

- **GO:0020037 (heme binding, MF)**: The oxygenase domain is heme-containing across the family, making this plausible, but some highly derived members may have lost functional heme binding (chen2022nitricoxidenitric pages 6-8).

- **FAD binding (GO:0050660) and FMN binding (GO:0010181)**: These would systematically over-annotate bacterial NOS proteins, which typically lack the reductase domain entirely (chen2022nitricoxidenitric pages 4-6, chen2022nitricoxidenitric pages 6-8, porrini2020dr.noand pages 13-16).

- **All biological process terms** (inflammatory response, vasodilation, neurotransmission): These are specific to vertebrate isoforms or even specific vertebrate NOS paralogs and would grossly over-annotate bacterial, fungal, and basal metazoan members (giordano2022nitricoxideproduction pages 4-6, krol2020humannitricoxide pages 3-5, chen2022nitricoxidenitric pages 1-3).

## 3. Functional Divergence Across the Family

### 3.1 Vertebrate NOS Isoforms

The following table compares the major NOS classes:

| NOS class/subfamily | Domain architecture | Key cofactors | Regulation mechanism | Primary biological function | Tissue / organismal distribution | Key structural differences relevant to GO review |
|---|---|---|---|---|---|---|
| NOS1 / nNOS | Full-length metazoan NOS; N-terminal oxygenase domain + calmodulin-binding linker + C-terminal reductase domain; PDZ domain present in NOS1; homodimeric (cinelli2020induciblenitricoxide pages 3-5, locascio2023nitricoxidefunction pages 4-5) | Heme, BH4/H4B, FAD, FMN, NADPH, calmodulin, Zn at dimer interface (cinelli2020induciblenitricoxide pages 3-5, krol2020humannitricoxide pages 3-5, verde2023noandheme pages 13-15) | Constitutive; Ca2+/calmodulin-dependent; activity modulated by localization and post-translational regulation (krol2020humannitricoxide pages 3-5, serreli2023roleofdietary pages 4-5) | NO signaling in neurons and muscle; neurotransmission and regulation of muscle/blood flow rather than immune high-output NO production (krol2020humannitricoxide pages 3-5, locascio2023nitricoxidefunction pages 4-5, serreli2023roleofdietary pages 4-5) | Neurons of central/peripheral nervous system; also skeletal, cardiac, and smooth muscle in vertebrates (krol2020humannitricoxide pages 3-5, serreli2023roleofdietary pages 4-5) | PDZ domain distinguishes it from NOS2/NOS3; not universally present across NOS family; vertebrate-specific functional specialization, so nervous-system process GO terms would not transfer across the family (cinelli2020induciblenitricoxide pages 3-5, locascio2023nitricoxidefunction pages 4-5) |
| NOS2 / iNOS | Full-length metazoan NOS; oxygenase domain + calmodulin-binding region + reductase domain; homodimeric; lacks the inhibitory loop found in NOS1/NOS3 (cinelli2020induciblenitricoxide pages 3-5, locascio2023nitricoxidefunction pages 4-5) | Heme, BH4/H4B, FAD, FMN, NADPH, calmodulin, Zn at dimer interface (cinelli2020induciblenitricoxide pages 3-5, krol2020humannitricoxide pages 3-5, verde2023noandheme pages 13-15) | Inducible transcriptionally; relatively Ca2+-independent once expressed; produces sustained high NO output in inflammatory contexts (giordano2022nitricoxideproduction pages 4-6, krol2020humannitricoxide pages 3-5, serreli2023roleofdietary pages 2-4) | Immune defense / cytotoxic NO production; often associated with phagosomes or inflammatory responses (giordano2022nitricoxideproduction pages 4-6, krol2020humannitricoxide pages 3-5) | Macrophages and many inducible cell types in vertebrates, including glia, vascular smooth muscle, hepatocytes, keratinocytes, chondrocytes, and others (krol2020humannitricoxide pages 3-5, locascio2023nitricoxidefunction pages 4-5, serreli2023roleofdietary pages 2-4) | Lacks inhibitory loop of NOS1/NOS3; immunological role is a lineage-specific metazoan specialization and not portable to bacterial or non-immune eukaryotic NOSs, so defense-response GO terms would over-annotate (giordano2022nitricoxideproduction pages 4-6, locascio2023nitricoxidefunction pages 4-5) |
| NOS3 / eNOS | Full-length metazoan NOS; oxygenase domain + calmodulin-binding linker + reductase domain; homodimeric; contains inhibitory loop; myristoylation/palmitoylation motifs for membrane association (locascio2023nitricoxidefunction pages 4-5, serreli2023roleofdietary pages 4-5) | Heme, BH4/H4B, FAD, FMN, NADPH, calmodulin, Zn at dimer interface (cinelli2020induciblenitricoxide pages 3-5, krol2020humannitricoxide pages 3-5, verde2023noandheme pages 13-15) | Constitutive; Ca2+/calmodulin-dependent; strongly regulated by shear stress, phosphorylation, and subcellular targeting to caveolae/Golgi (locascio2023nitricoxidefunction pages 4-5, serreli2023roleofdietary pages 4-5) | Vascular/endothelial NO signaling, blood-flow and vascular-tone regulation, anti-platelet and homeostatic roles (krol2020humannitricoxide pages 3-5, serreli2023roleofdietary pages 2-4, serreli2023roleofdietary pages 4-5) | Endothelial cells primarily; also myocardium and some brain/circulating cell contexts in vertebrates (krol2020humannitricoxide pages 3-5, locascio2023nitricoxidefunction pages 4-5, serreli2023roleofdietary pages 2-4) | Membrane-targeting lipidation motifs and endothelial specialization are not family-wide; teleost loss of nos3 in most fish further shows this is not universal even within vertebrates, so vascular-process or endothelial-component GO terms are inappropriate for the whole family (giordano2022nitricoxideproduction pages 4-6, locascio2023nitricoxidefunction pages 4-5) |
| Bacterial NOS / bNOS | Usually oxygenase domain only; lacks the eukaryotic reductase domain, β-hairpin hook, and canonical Cys-X4-Cys zinc-binding module; often uses external reductase partners; rare exceptions include multidomain forms such as SyNOS with added globin/reductase features (chen2022nitricoxidenitric pages 4-6, chen2022nitricoxidenitric pages 6-8, porrini2020dr.noand pages 13-16, chen2022nitricoxidenitric pages 14-15, chen2022nitricoxidenitric pages 8-11) | Heme, tetrahydrofolate/FH4-type pterins rather than BH4 in typical bNOS; external electron donor/reductase required in most cases (chen2022nitricoxidenitric pages 6-8, porrini2020dr.noand pages 13-16, chen2022nitricoxidenitric pages 14-15) | Species-specific control; depends on availability of partner reductases and local physiology rather than vertebrate Ca2+/CaM regulatory modes; some specialized variants have additional domains (chen2022nitricoxidenitric pages 4-6, porrini2020dr.noand pages 13-16, chen2022nitricoxidenitric pages 8-11) | Diverse, lineage-specific roles: oxidative-stress protection (Bacillus subtilis), respiration/colonization (Staphylococcus aureus), virulence (Bacillus anthracis), biofilm signaling, and NO supply for natural product nitration in Streptomyces pathways (chen2022nitricoxidenitric pages 3-4, chen2022nitricoxidenitric pages 1-3, porrini2020dr.noand pages 13-16, chen2022nitricoxidenitric pages 11-12) | Mostly bacteria, especially Gram-positive lineages such as Bacillus, Staphylococcus, Streptomyces, Deinococcus; also some archaea and unusual cyanobacterial forms (chen2022nitricoxidenitric pages 4-6, porrini2020dr.noand pages 13-16) | Major architectural and cofactor differences from metazoan NOS; downstream biology is highly species-specific, so only core catalytic activity is plausibly family-wide, whereas immune, neuronal, endothelial, membrane, or multicellular-process GO terms would be severe over-annotation (chen2022nitricoxidenitric pages 6-8, chen2022nitricoxidenitric pages 14-15, chen2022nitricoxidenitric pages 1-3) |
| Cross-family GO implication | Core shared feature across catalytically competent NOS proteins is arginine-dependent NO synthesis via a conserved heme-containing oxygenase catalytic center; however, architecture, cofactors, regulation, and biological roles diverge strongly between vertebrate isoforms and bNOS (cinelli2020induciblenitricoxide pages 3-5, chen2022nitricoxidenitric pages 4-6, chen2022nitricoxidenitric pages 14-15) | Shared catalytic chemistry does not imply shared organismal process or cellular component annotations (giordano2022nitricoxideproduction pages 4-6, chen2022nitricoxidenitric pages 1-3) | Universal GO candidates, if any, should be restricted to carefully supported catalytic molecular-function terms; process/component terms should generally be pushed to child entries or gene-level curation (giordano2022nitricoxideproduction pages 4-6, locascio2023nitricoxidefunction pages 4-5, chen2022nitricoxidenitric pages 1-3) | Family-wide process claims are unsafe because NO is deployed in neurotransmission, vascular homeostasis, immunity, stress resistance, respiration, biofilm biology, and secondary metabolism depending on lineage (krol2020humannitricoxide pages 3-5, serreli2023roleofdietary pages 2-4, chen2022nitricoxidenitric pages 11-12) | Broad taxonomic spread includes bacteria, archaea, fungi, choanoflagellates, basal metazoans, and vertebrates; plants lack canonical NOS, and some lineages show secondary loss or truncation (moroz2023nitricoxidesignaling pages 2-4, moroz2023nitricoxidesignaling pages 4-6, moroz2021neuralversusalternative pages 11-12, moroz2023nitricoxidesignaling pages 1-2) | Practical review outcome: universal GO mapping should be conservative; subfamily- or clade-specific biology should not be attached to the parent family entry PTHR43410 (moroz2023nitricoxidesignaling pages 2-4, chen2022nitricoxidenitric pages 1-3, chen2022nitricoxidenitric pages 14-15) |


*Table: This table compares vertebrate NOS1/NOS2/NOS3 and bacterial NOS across architecture, cofactors, regulation, distribution, and biology. It is useful for GO review because it shows that only a narrow catalytic core is shared broadly, while most process and component annotations are clade- or subfamily-specific.*

In mammals, three NOS isoforms have sharply distinct regulatory properties, expression patterns, and biological roles (krol2020humannitricoxide pages 3-5, locascio2023nitricoxidefunction pages 4-5):
- **NOS1 (nNOS)**: Constitutive, Ca²⁺/calmodulin-dependent, expressed in neurons and skeletal muscle; contains a PDZ domain for scaffolding interactions; functions primarily in neurotransmission and muscle blood flow regulation (krol2020humannitricoxide pages 3-5, serreli2023roleofdietary pages 4-5).
- **NOS2 (iNOS)**: Transcriptionally inducible, relatively Ca²⁺-independent once expressed; lacks the autoinhibitory loop; produces sustained high-output NO for immune defense, particularly in macrophages (giordano2022nitricoxideproduction pages 4-6, krol2020humannitricoxide pages 3-5, serreli2023roleofdietary pages 2-4).
- **NOS3 (eNOS)**: Constitutive, Ca²⁺/calmodulin-dependent; contains myristoylation/palmitoylation motifs for membrane targeting to caveolae; specialized for vascular endothelial homeostasis (locascio2023nitricoxidefunction pages 4-5, serreli2023roleofdietary pages 4-5).

These three genes arose through whole-genome duplication events. Nos1 and Nos2 diverged after the agnathan–gnathostome split, and Nos3 arose from Nos1 during tetrapod evolution (giordano2022nitricoxideproduction pages 4-6). Notably, most teleost fish have lost nos3, retaining only nos1 and nos2 (giordano2022nitricoxideproduction pages 4-6, locascio2023nitricoxidefunction pages 5-7).

### 3.2 Bacterial NOS Divergence

Bacterial NOS enzymes exhibit striking functional neo-functionalization. Their roles are highly species-specific (chen2022nitricoxidenitric pages 3-4, chen2022nitricoxidenitric pages 1-3):
- *Bacillus subtilis* NOS: oxidative stress protection (chen2022nitricoxidenitric pages 3-4)
- *Staphylococcus aureus* NOS: regulation of oxygen-based respiration, virulence, nasal colonization, skin abscess development (porrini2020dr.noand pages 13-16, chen2022nitricoxidenitric pages 11-12)
- *Bacillus anthracis* NOS: pathogen virulence, survival inside macrophages (porrini2020dr.noand pages 13-16)
- *Streptomyces* TxtD/RufN/PtnF: dedicated NOS enzymes providing NO for P450-catalyzed nitration reactions in natural product biosynthesis (thaxtomin A, rufomycin) (chen2022nitricoxidenitric pages 11-12, chen2022nitricoxidenitric pages 8-11)
- *Deinococcus radiodurans* NOS: UV damage recovery (chen2022nitricoxidenitric pages 1-3)

### 3.3 Truncated and Derived Members

The cyanobacterial SyNOS from *Synechococcus* PCC 7335 represents a rare Type II bNOS containing additional globin and reductase-like domains, enabling dual NOS and NO oxygenase activities—a clear case of neo-functionalization (chen2022nitricoxidenitric pages 4-6, chen2022nitricoxidenitric pages 8-11). Some ctenophore NOS genes are truncated with highly modified FAD-binding domains, and their catalytic competence remains unconfirmed (moroz2023nitricoxidesignaling pages 2-4, moroz2023nitricoxidesignaling pages 4-6). Nematodes (including *C. elegans*) have completely lost NOS (moroz2021neuralversusalternative pages 11-12). These examples confirm that the family is not uniformly catalytically active.

## 4. Taxonomic Scope

The PTHR43410 entry encompasses 8,119 proteins across 7,081 taxa with 4 subfamilies. The taxonomic distribution is summarized below:

| Clade/Taxon | NOS presence/absence | Number of NOS genes | Domain architecture notes | Known functions | Key references |
|---|---|---:|---|---|---|
| Bacteria – Gram-positive (e.g., *Bacillus*, *Staphylococcus*, *Streptomyces*, *Deinococcus*) | Present in many lineages, but not universal across prokaryotes | Usually 1 per genome when present | Typically bacterial NOS (bNOS) with oxygenase domain only; lacks eukaryotic reductase domain and usually uses external reductase partners; FH4-type pterin rather than BH4 | Oxidative-stress protection (*B. subtilis*), respiration/colonization and virulence (*S. aureus*), virulence (*B. anthracis*), UV-damage recovery (*D. radiodurans*), NO supply for natural-product nitration in *Streptomyces* pathways | (chen2022nitricoxidenitric pages 4-6, chen2022nitricoxidenitric pages 6-8, chen2022nitricoxidenitric pages 3-4, porrini2020dr.noand pages 13-16, chen2022nitricoxidenitric pages 1-3, chen2022nitricoxidenitric pages 11-12, chen2022nitricoxidenitric pages 14-15) |
| Bacteria – Gram-negative | Rare/patchy; not broadly distributed | Often 0; occasional single-copy examples | Usually absent; notable exception reported in *Sorangium cellulosum* with a more complete NOS-like architecture | Species-specific; not enough evidence for a universal Gram-negative NOS role | (porrini2020dr.noand pages 13-16, chen2022nitricoxidenitric pages 3-4) |
| Bacteria – Cyanobacteria | Present in some lineages only | Usually 1 when present | Unusual multidomain forms exist, e.g., SyNOS with added globin/reductase-like features relative to canonical bNOS | Nitrogen/NO metabolism; SyNOS can couple NOS and NO oxygenase-like activities, indicating specialization rather than a universal function | (chen2022nitricoxidenitric pages 4-6, chen2022nitricoxidenitric pages 8-11) |
| Archaea | Rare but present | At least single-copy examples known | NOS reported in archaeon *Natronomonas pharaonis*; architecture closer to simpler prokaryotic forms than to vertebrate full-length NOS | Specific functions remain poorly characterized; no broad process can be generalized | (chen2022nitricoxidenitric pages 4-6) |
| Fungi | Present in some taxa, absent in others | Not generalized; at least 1 in reported species | Eukaryotic-type NOS reported in fungi such as *Aspergillus* and *Dendrothele* | Functions not sufficiently conserved across fungi to support a universal process annotation | (moroz2023nitricoxidesignaling pages 2-4, moroz2023nitricoxidesignaling pages 4-6) |
| Choanoflagellates | Patchy; mostly lost, with rare retention | Usually 0; one eukaryotic-type NOS reported in *Salpingoeca infusionum*; some species have prokaryotic-type NOS | Most species lost NOS; retained eukaryotic-type NOS lacks some conserved FAD/NAD-binding regions; some prokaryotic-type NOS may reflect HGT | No conserved choanoflagellate-wide function established | (moroz2023nitricoxidesignaling pages 2-4, moroz2023nitricoxidesignaling pages 4-6) |
| Ctenophores | Present in a minority of sampled species; secondarily lost in many | Usually 0 or 1 | Only one NOS gene where present; ctenophore NOSs are highly derived, often truncated/modified, and may lack PDZ domain | NO signaling implicated in cilia control and possibly development/behavior; distribution is too patchy for universal ctenophore process assignment | (moroz2023nitricoxidesignaling pages 2-4, moroz2023nitricoxidesignaling pages 4-6, moroz2021neuralversusalternative pages 11-12, moroz2023nitricoxidesignaling pages 1-2) |
| Sponges (Porifera) | Present | Typically 1 | Single animal-type NOS gene; calcium-dependent NO synthesis documented experimentally in some species | Rhythmic movements, development, metamorphosis, stress responses | (moroz2023nitricoxidesignaling pages 2-4, moroz2021neuralversusalternative pages 11-12, moroz2023nitricoxidesignaling pages 1-2) |
| Placozoa | Present | 3 distinct NOS genes reported | Animal-type NOS repertoire expanded independently; more than one paralogue | Expressed in distinct cell subpopulations with signaling roles; exact functions are lineage-specific | (moroz2023nitricoxidesignaling pages 2-4, moroz2021neuralversusalternative pages 11-12) |
| Cnidaria | Present | Multiple NOS isoforms | Animal-type NOSs; duplications occurred independently relative to vertebrates | Regeneration, feeding, chemosensation; often non-neuronal expression in Hydra | (moroz2023nitricoxidesignaling pages 2-4, moroz2021neuralversusalternative pages 11-12) |
| Invertebrate bilaterians – insects and molluscs | Generally present | Often 1 ancestral-type NOS gene | Usually a single animal NOS rather than vertebrate-style NOS1/2/3 trio | Commonly implicated in neurotransmission, development, metamorphosis, feeding, and other lineage-specific signaling roles | (locascio2023nitricoxidefunction pages 1-2, moroz2021neuralversusalternative pages 11-12) |
| Invertebrate bilaterians – nematodes | Lost in many/entire lineage highlighted as absent | 0 | No canonical NOS retained in the noted lineage | NOS-based processes cannot be assumed because the enzyme is absent | (moroz2021neuralversusalternative pages 11-12) |
| Vertebrates – fish | Present, but repertoire differs from tetrapods | nos1 usually single-copy; nos2 may duplicate; nos3 absent from most teleosts but retained in some non-teleosts/exceptional taxa | Full-length metazoan NOSs with oxygenase + CaM-binding + reductase domains; teleost repertoires shaped by duplication and loss | Neural signaling (Nos1), immune functions (Nos2), endothelial-like functions variably partitioned; fish diversity precludes a single process term across all fish NOS genes | (giordano2022nitricoxideproduction pages 4-6, locascio2023nitricoxidefunction pages 4-5, locascio2023nitricoxidefunction pages 5-7) |
| Vertebrates – amphibians and other sarcopterygians | Present | Typically 3 (Nos1, Nos2, Nos3) | Canonical full-length animal NOS isoforms | Neural signaling, inducible immune defense, endothelial/vascular regulation | (locascio2023nitricoxidefunction pages 4-5, locascio2023nitricoxidefunction pages 5-7) |
| Vertebrates – mammals | Present | 3 (NOS1/nNOS, NOS2/iNOS, NOS3/eNOS) | Full-length homodimeric enzymes with oxygenase and reductase domains; NOS1 has PDZ domain, NOS3 has membrane-targeting motifs, NOS2 lacks inhibitory loop | NOS1: neuronal/muscle signaling; NOS2: inducible immune/cytotoxic NO; NOS3: endothelial vascular homeostasis | (cinelli2020induciblenitricoxide pages 3-5, giordano2022nitricoxideproduction pages 4-6, krol2020humannitricoxide pages 3-5, locascio2023nitricoxidefunction pages 4-5, serreli2023roleofdietary pages 2-4, serreli2023roleofdietary pages 4-5) |
| Plants (land plants) | Canonical NOS absent | 0 canonical NOS genes | Land plants lack conserved canonical NOS family members despite NO biology being important | NO is biologically important in plants, but canonical NOS-based GO terms would be inappropriate because the family is absent | (chen2022nitricoxidenitric pages 1-3) |


*Table: This table summarizes where canonical NOS family members occur across major clades, how many copies are typically present, and how their architectures and biological roles differ. It is useful for GO review because it shows that only the catalytic core is broadly conserved, whereas biological processes are highly lineage-specific and often absent in entire clades.*

Key observations:
- **Bacteria**: NOS is found primarily in Gram-positive lineages (*Bacillus*, *Staphylococcus*, *Streptomyces*, *Deinococcus*), with *Sorangium cellulosum* being the only reported Gram-negative bacterium with a more complete NOS (porrini2020dr.noand pages 13-16). A considerable portion of prokaryotes lack bNOS (chen2022nitricoxidenitric pages 3-4).
- **Archaea**: Rare; documented in *Natronomonas pharaonis* (chen2022nitricoxidenitric pages 4-6).
- **Fungi**: Present in some taxa (*Aspergillus*, *Dendrothele*) (moroz2023nitricoxidesignaling pages 2-4, moroz2023nitricoxidesignaling pages 4-6).
- **Choanoflagellates**: Mostly lost; eukaryotic-type NOS preserved only in *Salpingoeca infusionum* (moroz2023nitricoxidesignaling pages 2-4, moroz2023nitricoxidesignaling pages 4-6).
- **Basal metazoans**: Variable—sponges and placozoans retain NOS (placozoans have 3 genes); cnidarians have multiple isoforms; ctenophores show massive secondary loss with only ~8 species retaining NOS (moroz2023nitricoxidesignaling pages 2-4, moroz2021neuralversusalternative pages 11-12, moroz2023nitricoxidesignaling pages 1-2).
- **Invertebrate bilaterians**: Typically one NOS gene; notably absent in nematodes (locascio2023nitricoxidefunction pages 1-2, moroz2021neuralversusalternative pages 11-12).
- **Vertebrates**: NOS1/NOS2/NOS3 in sarcopterygians; teleosts lost NOS3 in most lineages (giordano2022nitricoxideproduction pages 4-6, locascio2023nitricoxidefunction pages 4-5, locascio2023nitricoxidefunction pages 5-7).
- **Plants**: Land plants lack canonical NOS genes entirely, despite using NO in signaling via other mechanisms (chen2022nitricoxidenitric pages 1-3).

No single biological process GO term can hold across this taxonomic range. Neurotransmission, vascular regulation, and immune defense are vertebrate-specific; oxidative stress protection and natural product biosynthesis are bacterial-specific; and developmental/metamorphic roles are lineage-specific in invertebrates.

## 5. Over-Annotation Verdict

### Current Status: No InterPro2GO Terms Mapped — This Is Appropriate

The absence of mapped GO terms for PTHR43410 is the correct and conservative state for the following reasons:

1. **Architectural heterogeneity**: The family spans full-length homodimeric metazoan NOS (with oxygenase + CaM-binding + reductase domains) and truncated bacterial NOS (oxygenase domain only). Cofactor usage differs (BH4 vs. FH4). Any GO terms relating to FAD/FMN binding, calmodulin binding, or specific cofactor dependencies would be false for large fractions of the family (chen2022nitricoxidenitric pages 4-6, chen2022nitricoxidenitric pages 6-8, porrini2020dr.noand pages 13-16, chen2022nitricoxidenitric pages 14-15).

2. **Functional divergence**: The three vertebrate isoforms alone serve fundamentally different biological processes (neurotransmission, immune defense, vascular homeostasis), and bacterial NOS functions are even more divergent (virulence, stress resistance, natural product biosynthesis) (giordano2022nitricoxideproduction pages 4-6, krol2020humannitricoxide pages 3-5, chen2022nitricoxidenitric pages 1-3, chen2022nitricoxidenitric pages 11-12).

3. **Secondary losses and truncations**: Complete loss in nematodes, most ctenophores, and many choanoflagellates, as well as truncated/modified forms in some retained lineages, mean that even core catalytic activity cannot be assumed for every match (moroz2023nitricoxidesignaling pages 2-4, moroz2023nitricoxidesignaling pages 4-6, moroz2021neuralversusalternative pages 11-12).

4. **The core catalytic activity (GO:0004517, nitric oxide synthase activity)** is the only term that could plausibly be considered, as the heme-centered L-arginine → NO + L-citrulline reaction is conserved across catalytically competent members (chen2022nitricoxidenitric pages 4-6, chen2022nitricoxidenitric pages 14-15). However, given the presence of truncated/derived members, even this term carries some risk at the parent family level.

### Recommended GO Action Pattern

| Action | Recommendation |
|---|---|
| **Overall family-level mapping** | **ACCEPT current state (no terms mapped)** — The absence of InterPro2GO terms is appropriate given the family's architectural and functional heterogeneity. |
| **GO:0004517 (NOS activity)** | **MODIFY-to-specific** — Consider mapping only at more homogeneous child/subfamily entries (e.g., separate entries for vertebrate NOS1/2/3 and for characterized bNOS clades). |
| **Cofactor-binding MF terms** | **REMOVE** if ever proposed at parent level — FAD/FMN binding is false for bNOS; BH4 binding is false for bNOS (which uses FH4). |
| **Any BP terms** (neurotransmission, immune defense, vasodilation, inflammatory response) | **MARK_AS_OVER_ANNOTATED / REMOVE** — These are clade- or isoform-specific and would systematically over-annotate. |
| **Any CC terms** (cytosol, membrane, caveolae) | **REMOVE** — Subcellular localization is isoform- and organism-specific. |
| **Recommendation for InterPro** | If GO terms are desired for NOS proteins, they should be applied at the **subfamily or child-entry level** (e.g., separate PANTHER subfamily entries for NOS1, NOS2, NOS3, and bNOS), not at the parent PTHR43410 level. The 4 subfamilies recognized by InterPro are the appropriate level for any GO mapping. |

In conclusion, the current absence of InterPro2GO terms for PTHR43410 represents sound annotation practice. The NOS family is a textbook example of a functionally heterogeneous protein family where the core catalytic chemistry is broadly conserved but the biological deployment, cofactor requirements, domain architecture, and downstream processes are profoundly divergent across the >7,000 taxa in which this signature occurs.

References

1. (chen2022nitricoxidenitric pages 4-6): Jing-Huei Chen, Lulu Liu, Weiwei Wang, and Haichun Gao. Nitric oxide, nitric oxide formers and their physiological impacts in bacteria. International Journal of Molecular Sciences, 23:10778, Sep 2022. URL: https://doi.org/10.3390/ijms231810778, doi:10.3390/ijms231810778. This article has 51 citations.

2. (cinelli2020induciblenitricoxide pages 3-5): Maris A. Cinelli, Ha T. Do, Galen P. Miley, and Richard B. Silverman. Inducible nitric oxide synthase: regulation, structure, and inhibition. Medicinal Research Reviews, 40:158-189, Jan 2020. URL: https://doi.org/10.1002/med.21599, doi:10.1002/med.21599. This article has 1060 citations and is from a domain leading peer-reviewed journal.

3. (krol2020humannitricoxide pages 3-5): Magdalena Król and Marta Kepinska. Human nitric oxide synthase—its functions, polymorphisms, and inhibitors in the context of inflammation, diabetes and cardiovascular diseases. International Journal of Molecular Sciences, 22:56, Dec 2020. URL: https://doi.org/10.3390/ijms22010056, doi:10.3390/ijms22010056. This article has 260 citations.

4. (serreli2023roleofdietary pages 4-5): Gabriele Serreli and Monica Deiana. Role of dietary polyphenols in the activity and expression of nitric oxide synthases: a review. Antioxidants, 12:147, Jan 2023. URL: https://doi.org/10.3390/antiox12010147, doi:10.3390/antiox12010147. This article has 98 citations.

5. (verde2023noandheme pages 13-15): Cinzia Verde, Daniela Giordano, and Stefano Bruno. No and heme proteins: cross-talk between heme and cysteine residues. Antioxidants, 12:321, Jan 2023. URL: https://doi.org/10.3390/antiox12020321, doi:10.3390/antiox12020321. This article has 13 citations.

6. (chen2022nitricoxidenitric pages 6-8): Jing-Huei Chen, Lulu Liu, Weiwei Wang, and Haichun Gao. Nitric oxide, nitric oxide formers and their physiological impacts in bacteria. International Journal of Molecular Sciences, 23:10778, Sep 2022. URL: https://doi.org/10.3390/ijms231810778, doi:10.3390/ijms231810778. This article has 51 citations.

7. (chen2022nitricoxidenitric pages 14-15): Jing-Huei Chen, Lulu Liu, Weiwei Wang, and Haichun Gao. Nitric oxide, nitric oxide formers and their physiological impacts in bacteria. International Journal of Molecular Sciences, 23:10778, Sep 2022. URL: https://doi.org/10.3390/ijms231810778, doi:10.3390/ijms231810778. This article has 51 citations.

8. (porrini2020dr.noand pages 13-16): Constance Porrini, Nalini Ramarao, and Seav-Ly Tran. Dr. no and mr. toxic – the versatile role of nitric oxide. Dec 2020. URL: https://doi.org/10.1515/hsz-2019-0368, doi:10.1515/hsz-2019-0368. This article has 85 citations and is from a peer-reviewed journal.

9. (moroz2023nitricoxidesignaling pages 2-4): Leonid L. Moroz, Krishanu Mukherjee, and Daria Y. Romanova. Nitric oxide signaling in ctenophores. Frontiers in Neuroscience, Mar 2023. URL: https://doi.org/10.3389/fnins.2023.1125433, doi:10.3389/fnins.2023.1125433. This article has 17 citations and is from a peer-reviewed journal.

10. (moroz2023nitricoxidesignaling pages 4-6): Leonid L. Moroz, Krishanu Mukherjee, and Daria Y. Romanova. Nitric oxide signaling in ctenophores. Frontiers in Neuroscience, Mar 2023. URL: https://doi.org/10.3389/fnins.2023.1125433, doi:10.3389/fnins.2023.1125433. This article has 17 citations and is from a peer-reviewed journal.

11. (chen2022nitricoxidenitric pages 3-4): Jing-Huei Chen, Lulu Liu, Weiwei Wang, and Haichun Gao. Nitric oxide, nitric oxide formers and their physiological impacts in bacteria. International Journal of Molecular Sciences, 23:10778, Sep 2022. URL: https://doi.org/10.3390/ijms231810778, doi:10.3390/ijms231810778. This article has 51 citations.

12. (chen2022nitricoxidenitric pages 1-3): Jing-Huei Chen, Lulu Liu, Weiwei Wang, and Haichun Gao. Nitric oxide, nitric oxide formers and their physiological impacts in bacteria. International Journal of Molecular Sciences, 23:10778, Sep 2022. URL: https://doi.org/10.3390/ijms231810778, doi:10.3390/ijms231810778. This article has 51 citations.

13. (giordano2022nitricoxideproduction pages 4-6): Daniela Giordano, Cinzia Verde, and Paola Corti. Nitric oxide production and regulation in the teleost cardiovascular system. Antioxidants, 11:957, May 2022. URL: https://doi.org/10.3390/antiox11050957, doi:10.3390/antiox11050957. This article has 14 citations.

14. (locascio2023nitricoxidefunction pages 4-5): Annamaria Locascio, Giovanni Annona, Filomena Caccavale, Salvatore D’Aniello, Claudio Agnisola, and Anna Palumbo. Nitric oxide function and nitric oxide synthase evolution in aquatic chordates. International Journal of Molecular Sciences, 24:11182, Jul 2023. URL: https://doi.org/10.3390/ijms241311182, doi:10.3390/ijms241311182. This article has 20 citations.

15. (chen2022nitricoxidenitric pages 11-12): Jing-Huei Chen, Lulu Liu, Weiwei Wang, and Haichun Gao. Nitric oxide, nitric oxide formers and their physiological impacts in bacteria. International Journal of Molecular Sciences, 23:10778, Sep 2022. URL: https://doi.org/10.3390/ijms231810778, doi:10.3390/ijms231810778. This article has 51 citations.

16. (serreli2023roleofdietary pages 2-4): Gabriele Serreli and Monica Deiana. Role of dietary polyphenols in the activity and expression of nitric oxide synthases: a review. Antioxidants, 12:147, Jan 2023. URL: https://doi.org/10.3390/antiox12010147, doi:10.3390/antiox12010147. This article has 98 citations.

17. (chen2022nitricoxidenitric pages 8-11): Jing-Huei Chen, Lulu Liu, Weiwei Wang, and Haichun Gao. Nitric oxide, nitric oxide formers and their physiological impacts in bacteria. International Journal of Molecular Sciences, 23:10778, Sep 2022. URL: https://doi.org/10.3390/ijms231810778, doi:10.3390/ijms231810778. This article has 51 citations.

18. (moroz2021neuralversusalternative pages 11-12): Leonid L. Moroz, Daria Y. Romanova, and Andrea B. Kohn. Neural versus alternative integrative systems: molecular insights into origins of neurotransmitters. Philosophical Transactions of the Royal Society B, 376:20190762, Feb 2021. URL: https://doi.org/10.1098/rstb.2019.0762, doi:10.1098/rstb.2019.0762. This article has 153 citations.

19. (moroz2023nitricoxidesignaling pages 1-2): Leonid L. Moroz, Krishanu Mukherjee, and Daria Y. Romanova. Nitric oxide signaling in ctenophores. Frontiers in Neuroscience, Mar 2023. URL: https://doi.org/10.3389/fnins.2023.1125433, doi:10.3389/fnins.2023.1125433. This article has 17 citations and is from a peer-reviewed journal.

20. (locascio2023nitricoxidefunction pages 5-7): Annamaria Locascio, Giovanni Annona, Filomena Caccavale, Salvatore D’Aniello, Claudio Agnisola, and Anna Palumbo. Nitric oxide function and nitric oxide synthase evolution in aquatic chordates. International Journal of Molecular Sciences, 24:11182, Jul 2023. URL: https://doi.org/10.3390/ijms241311182, doi:10.3390/ijms241311182. This article has 20 citations.

21. (locascio2023nitricoxidefunction pages 1-2): Annamaria Locascio, Giovanni Annona, Filomena Caccavale, Salvatore D’Aniello, Claudio Agnisola, and Anna Palumbo. Nitric oxide function and nitric oxide synthase evolution in aquatic chordates. International Journal of Molecular Sciences, 24:11182, Jul 2023. URL: https://doi.org/10.3390/ijms241311182, doi:10.3390/ijms241311182. This article has 20 citations.

## Artifacts

- [Edison artifact artifact-00](PTHR43410-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR43410-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](PTHR43410-deep-research-falcon_artifacts/artifact-02.md)

## Citations

1. chen2022nitricoxidenitric pages 4-6
2. cinelli2020induciblenitricoxide pages 3-5
3. chen2022nitricoxidenitric pages 6-8
4. chen2022nitricoxidenitric pages 14-15
5. giordano2022nitricoxideproduction pages 4-6
6. chen2022nitricoxidenitric pages 3-4
7. chen2022nitricoxidenitric pages 1-3
8. moroz2021neuralversusalternative pages 11-12
9. krol2020humannitricoxide pages 3-5
10. serreli2023roleofdietary pages 4-5
11. verde2023noandheme pages 13-15
12. moroz2023nitricoxidesignaling pages 2-4
13. moroz2023nitricoxidesignaling pages 4-6
14. locascio2023nitricoxidefunction pages 4-5
15. chen2022nitricoxidenitric pages 11-12
16. serreli2023roleofdietary pages 2-4
17. chen2022nitricoxidenitric pages 8-11
18. moroz2023nitricoxidesignaling pages 1-2
19. locascio2023nitricoxidefunction pages 5-7
20. locascio2023nitricoxidefunction pages 1-2
21. https://doi.org/10.3390/ijms231810778,
22. https://doi.org/10.1002/med.21599,
23. https://doi.org/10.3390/ijms22010056,
24. https://doi.org/10.3390/antiox12010147,
25. https://doi.org/10.3390/antiox12020321,
26. https://doi.org/10.1515/hsz-2019-0368,
27. https://doi.org/10.3389/fnins.2023.1125433,
28. https://doi.org/10.3390/antiox11050957,
29. https://doi.org/10.3390/ijms241311182,
30. https://doi.org/10.1098/rstb.2019.0762,