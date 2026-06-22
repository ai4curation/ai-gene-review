---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-21T21:00:07.310218'
end_time: '2026-06-21T21:13:20.187894'
duration_seconds: 792.88
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR24067
  interpro_name: Ubiquitin-conjugating enzyme
  interpro_short_name: Ub_conjugating_enzyme
  interpro_type: family
  interpro_integrated: IPR050113
  member_databases: Not specified
  n_proteins: '69450'
  n_taxa: '12422'
  n_subfamilies: '70'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: The ubiquitin-conjugating enzyme family is involved in the
    post-translational modification process known as ubiquitination, which tags proteins
    for various cellular processes. Members of this family accept ubiquitin from E1
    activating enzymes and transfer it to target proteins, often with the help of
    E3 ligases. This modification can signal for protein degradation, alter protein
    function or localization, and affect protein-protein interactions. Ubiquitination
    plays a critical role in cell cycle regulation, DNA repair, signal transduction,
    and immune responses. Some family members also work with ubiquitin-like proteins
    such as NEDD8 and SUMO, expanding the functional repertoire to processes like
    nuclear architecture, chromosome segregation, and vesicle trafficking.
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
  path: PTHR24067-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR24067-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** PTHR24067
- **Name:** Ubiquitin-conjugating enzyme
- **Short name:** Ub_conjugating_enzyme
- **Entry type:** family
- **Integrated into / parent:** IPR050113
- **Member database signatures:** Not specified
- **Scale:** 69450 proteins across 12422 taxa, 70 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The ubiquitin-conjugating enzyme family is involved in the post-translational modification process known as ubiquitination, which tags proteins for various cellular processes. Members of this family accept ubiquitin from E1 activating enzymes and transfer it to target proteins, often with the help of E3 ligases. This modification can signal for protein degradation, alter protein function or localization, and affect protein-protein interactions. Ubiquitination plays a critical role in cell cycle regulation, DNA repair, signal transduction, and immune responses. Some family members also work with ubiquitin-like proteins such as NEDD8 and SUMO, expanding the functional repertoire to processes like nuclear architecture, chromosome segregation, and vesicle trafficking.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR24067 (Ubiquitin-conjugating enzyme)**, structured to support GO annotation review.

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
- **Accession:** PTHR24067
- **Name:** Ubiquitin-conjugating enzyme
- **Short name:** Ub_conjugating_enzyme
- **Entry type:** family
- **Integrated into / parent:** IPR050113
- **Member database signatures:** Not specified
- **Scale:** 69450 proteins across 12422 taxa, 70 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The ubiquitin-conjugating enzyme family is involved in the post-translational modification process known as ubiquitination, which tags proteins for various cellular processes. Members of this family accept ubiquitin from E1 activating enzymes and transfer it to target proteins, often with the help of E3 ligases. This modification can signal for protein degradation, alter protein function or localization, and affect protein-protein interactions. Ubiquitination plays a critical role in cell cycle regulation, DNA repair, signal transduction, and immune responses. Some family members also work with ubiquitin-like proteins such as NEDD8 and SUMO, expanding the functional repertoire to processes like nuclear architecture, chromosome segregation, and vesicle trafficking.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR24067 (Ubiquitin-conjugating enzyme)**, structured to support GO annotation review.

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


# InterPro Family Research Report: PTHR24067 (Ubiquitin-conjugating enzyme)

## Executive Summary

InterPro entry PTHR24067 represents the ubiquitin-conjugating enzyme (E2) family, a type="family" signature covering 69,450 proteins across 12,422 taxa with 70 subfamilies. Currently, **no InterPro2GO terms are mapped** to this entry. Based on comprehensive literature review, this absence of GO mappings is **appropriate and avoids over-annotation** given the extensive functional diversification within this family. While core molecular function terms describing E2 catalytic activity would be suitable for most members, specific biological process and cellular component terms would systematically over-annotate due to subfamily-specific specializations.

---

## 1. Family Definition and Biochemistry

### 1.1 Core Structure and Fold

Ubiquitin-conjugating enzymes are defined by a conserved **ubiquitin-conjugating (UBC) catalytic domain** of approximately 150-200 amino acids (liu2020theubiquitinconjugating pages 3-5, cappadocia2018ubiquitinlikeproteinconjugation pages 11-12). The canonical UBC fold comprises four α-helices and an antiparallel β-sheet with four β-strands, creating a characteristic canyon-like architecture (cappadocia2018ubiquitinlikeproteinconjugation pages 11-12). This fold has remained highly conserved throughout eukaryotic evolution despite extensive sequence divergence outside core catalytic motifs (kaminskaya2024trackingofubiquitin pages 1-2).

| Feature | Description | Conservation level | Key references |
|---|---|---|---|
| UBC catalytic core domain | E2 enzymes contain a conserved ubiquitin-conjugating (UBC) domain of ~150-200 amino acids that serves as the catalytic core for ubiquitin/Ubl transfer. This domain is the defining structural unit of the family. | Highly conserved across eukaryotic E2s | (liu2020theubiquitinconjugating pages 3-5, cappadocia2018ubiquitinlikeproteinconjugation pages 11-12) |
| Fold topology | The canonical UBC fold is composed mainly of four α-helices and an antiparallel β-sheet/four β-strands, with the catalytic center embedded in conserved active-site loops. This fold is shared by canonical E2s despite extensive sequence divergence outside core motifs. | Highly conserved fold; sequence more variable | (liu2020theubiquitinconjugating pages 3-5, cappadocia2018ubiquitinlikeproteinconjugation pages 11-12) |
| Catalytic cysteine | The active-site cysteine forms the thioester intermediate with ubiquitin transferred from E1, making it essential for transthiolation and downstream Ub transfer. Loss of this residue abolishes conjugating activity. | Universally conserved in catalytically active E2s; absent in UEVs | (liu2020theubiquitinconjugating pages 3-5, swarnkar2024determinantsofchemoselectivity pages 1-2, wu2024structureguidedengineeringenables pages 1-2) |
| HPN motif | Most canonical E2s contain a conserved His-Pro-Asn (HPN) motif located ~10 residues N-terminal to the catalytic cysteine. This motif is a hallmark of canonical E2s and contributes to active-site organization and catalysis. | Highly conserved in canonical E2s; altered in some noncanonical families | (liu2020theubiquitinconjugating pages 3-5, rehman2024discoveryandcharacterization pages 1-2, lv2024theroleof pages 1-2) |
| Conserved asparagine role | The conserved Asn in the HPN/active-site region is not simply an oxyanion stabilizer; computational and structural work supports a role in positioning the electrophile/substrate for nucleophilic attack and organizing the active-site loop. | Broadly conserved but mechanistic role can vary by E2 | (jones2019aconservedasparagine pages 1-2, cappadocia2018ubiquitinlikeproteinconjugation pages 11-12) |
| Additional active-site residues | Beyond the catalytic Cys and HPN motif, nearby residues such as Tyr/Asp/Asn equivalents and loop elements shape the microenvironment, suppress nucleophile pKa, position the thioester, and tune discharge chemistry. Exact identities differ among E2s. | Partly conserved architecture, residue-level variability | (cappadocia2018ubiquitinlikeproteinconjugation pages 11-12, swarnkar2024determinantsofchemoselectivity pages 1-2) |
| Active-site gate dynamics | Some E2s possess a dynamic active-site gate motif/loop near the catalytic cysteine that modulates thioester reactivity and chain-type specificity; open vs closed conformations differ between subfamilies such as Ubc13 and E2-25K. | Conserved regulatory principle, not identical residues/states | (rout2018activesitegate pages 1-2) |
| Closed E2~Ub conformation | Productive ubiquitin transfer often requires the donor ubiquitin to adopt a conserved “closed” orientation relative to the E2 UBC domain, frequently stabilized by E3 binding or E2-specific contacts. | Widely conserved mechanistic state among many E2s | (williams2019structuralinsightsinto pages 1-2, liess2019autoinhibitionmechanismof pages 1-3, lorenz2016crystalstructureof pages 1-2) |
| Additional N-/C-terminal extensions | E2s are commonly classified by appended regions: Class I contains only the UBC domain, while Classes II-IV include N-terminal and/or C-terminal extensions. These additions influence E1/E3 interactions, localization, substrate choice, or ubiquitin-chain specificity. | Variable across subfamilies | (liu2020theubiquitinconjugating pages 3-5, williams2019structuralinsightsinto pages 1-2) |
| Inserted or appended binding domains | Some E2s carry extra modules such as UBA domains or long tails/extensions that help bind ubiquitin chains, stabilize closed conformations, or promote linkage-specific chain assembly. | Subfamily-specific | (williams2019structuralinsightsinto pages 1-2) |
| UEV/pseudoenzyme variants | Ubiquitin E2 variants (UEVs) resemble E2s in sequence/structure but lack the catalytic cysteine, so they cannot form E2~Ub thioesters. Instead, they act as cofactors, e.g., forming functional heterodimers with active E2s such as UBC13 for K63-linked chains. | Conserved inactive subclass within wider E2 superfamily | (liu2020theubiquitinconjugating pages 3-5, liu2020theubiquitinconjugating pages 7-9) |
| Noncanonical chemistry in some subfamilies | While most E2s transfer Ub to lysine amino groups, certain families/subfamilies can also support noncanonical esterification of serine/threonine or even other hydroxyl-bearing acceptors, reflecting divergence built on the same core fold. | Restricted to specific subfamilies, not universal | (swarnkar2024determinantsofchemoselectivity pages 1-2, rehman2024discoveryandcharacterization pages 1-2) |


*Table: This table summarizes the conserved structural and biochemical hallmarks of ubiquitin-conjugating enzymes, highlighting which features are family-wide versus subfamily-specific. It is useful for judging whether a broad InterPro family can support universal functional annotation.*

### 1.2 Catalytic Mechanism and Conserved Residues

The **catalytic cysteine** is the signature active-site residue, positioned between β-strand 4 and α-helix 2 in the UBC fold (liu2020theubiquitinconjugating pages 3-5, swarnkar2024determinantsofchemoselectivity pages 1-2). This cysteine forms a thioester bond with the C-terminal glycine of ubiquitin transferred from the E1 activating enzyme, creating the E2~Ub intermediate essential for subsequent transfer to substrate proteins (liu2020theubiquitinconjugating pages 3-5, cappadocia2018ubiquitinlikeproteinconjugation pages 5-6, wu2024structureguidedengineeringenables pages 1-2).

The **HPN motif** (histidine-proline-asparagine tripeptide) is located approximately 10 residues N-terminal to the catalytic cysteine and represents a hallmark of canonical E2 enzymes (liu2020theubiquitinconjugating pages 3-5, rehman2024discoveryandcharacterization pages 1-2, lv2024theroleof pages 1-2). While historically proposed as an oxyanion hole, computational and structural studies reveal the conserved asparagine primarily functions to position the electrophile (thioester substrate) for nucleophilic attack and organize the active-site loop architecture (jones2019aconservedasparagine pages 1-2, cappadocia2018ubiquitinlikeproteinconjugation pages 11-12).

Additional active-site residues create a microenvironment that suppresses the pKa of incoming lysine nucleophiles and optimally positions the thioester bond for catalysis. Studies of E2UBC9 identified Asn85, Tyr87, and Asp127 as critical contributors, though the exact residue identities vary across E2 subfamilies while maintaining functional equivalence (cappadocia2018ubiquitinlikeproteinconjugation pages 11-12).

Recent crystallographic and molecular dynamics studies have revealed **active-site gate dynamics** that modulate E2 reactivity. For example, E2-25K adopts a closed gate conformation with precise balancing of opening/closing rates, while Ubc13 maintains an open configuration, correlating with their distinct linkage specificities (K48 vs. K63) (rout2018activesitegate pages 1-2).

### 1.3 Catalytic Cycle

E2 enzymes catalyze the central step in the ubiquitin conjugation cascade through sequential reactions (cappadocia2018ubiquitinlikeproteinconjugation pages 11-12):

1. **Transthiolation**: Ubiquitin transfer from E1~Ub thioester to the E2 catalytic cysteine
2. **Aminolysis**: Transfer of ubiquitin from E2~Ub to the ε-amino group of a substrate lysine (or, in some cases, to an E3 ligase cysteine for HECT/RBR E3s)

The aminolysis reaction proceeds through a tetrahedral zwitterionic intermediate where the deprotonated lysine amine acts as nucleophile attacking the E2~Ub thioester carbonyl (jones2019aconservedasparagine pages 1-2, cappadocia2018ubiquitinlikeproteinconjugation pages 11-12). Computational studies indicate that forming this intermediate is rate-limiting (jones2019aconservedasparagine pages 1-2).

---

## 2. InterPro2GO Mapping Appropriateness

### 2.1 Current Mapping Status

**PTHR24067 currently has NO InterPro2GO terms mapped.** This is noteworthy given that this is a large family signature.

### 2.2 Evaluation of Potential GO Terms

#### Molecular Function (MF) Terms - APPROPRIATE for Family-Level Annotation

The following core MF terms would be accurate for the vast majority of family members:

- **GO:0061631** (ubiquitin conjugating enzyme activity) - This term accurately describes the core biochemical function shared by catalytically active E2s (liu2020theubiquitinconjugating pages 3-5, bui2021ubiquitinconjugatingenzymesin pages 1-2, romantrufero2022theube2dubiquitin pages 1-2)
- **GO:0016740** (transferase activity) - Appropriate as E2s transfer ubiquitin moieties
- **GO:0005515** (protein binding) - E2s must interact with E1 and E3 enzymes

However, even at the MF level, complications arise:

**CAUTION - UEV Proteins (Ubiquitin E2 Variants)**: A significant subset of E2-like proteins **lack the catalytic cysteine** and therefore cannot form E2~Ub thioesters (liu2020theubiquitinconjugating pages 3-5, liu2020theubiquitinconjugating pages 7-9). These UEV proteins (e.g., MMS2, UBE2V1, UBE2V2, COP10-type variants) serve as non-catalytic cofactors, forming heterodimers with active E2s to support K63-linked chain assembly (liu2020theubiquitinconjugating pages 7-9). Annotating these with "ubiquitin conjugating enzyme activity" would be **biochemically incorrect**. If UEVs are included in PTHR24067 (which is likely given the family's breadth), blanket MF terms would over-annotate this subset.

#### Biological Process (BP) Terms - OVER-ANNOTATION RISK

Potential BP terms face severe over-annotation issues:

- **GO:0016567** (protein ubiquitination) - While accurate for many E2s, this would be **too specific** because:
  - Some E2s transfer ubiquitin-**like** proteins (SUMO, NEDD8) rather than ubiquitin itself (paubel2024dynamicexpressionof pages 1-2, cappadocia2018ubiquitinlikeproteinconjugation pages 11-12)
  - UEV proteins do not directly catalyze ubiquitination
  
- **Proteasomal degradation pathways** - Only appropriate for K48-chain-specific E2s (e.g., E2-25K, Cdc34), not for K63-specific E2s involved in DNA repair and signaling (liu2020theubiquitinconjugating pages 7-9, rout2018activesitegate pages 1-2)

- **DNA repair** - Specific to UBC13/UBE2N and error-free DNA damage tolerance pathways, not a family-wide function (liu2020theubiquitinconjugating pages 7-9)

- **Cell cycle regulation** - True for some members (Cdc34, UBE2C) but not universal (bui2021ubiquitinconjugatingenzymesin pages 1-2, williams2019structuralinsightsinto pages 1-2)

#### Cellular Component (CC) Terms - SUBFAMILY-SPECIFIC

- **Endoplasmic reticulum** - Appropriate only for ER-associated degradation (ERAD) E2s like UBE2J1/J2, not for nuclear or cytosolic E2s (swarnkar2024determinantsofchemoselectivity pages 1-2)
- **Nucleus vs. Cytoplasm** - E2 localization varies extensively by subfamily

---

## 3. Functional Divergence Across the Family

The ubiquitin-conjugating enzyme family exhibits **profound functional diversification** despite sharing the core UBC fold:

| E2 subfamily/class | Functional specialization | Structural distinctive features | Representative members | Whether function is shared across all family members |
|---|---|---|---|---|
| Canonical class I E2s (UBC domain only) | Core ubiquitin transfer; many act with RING, HECT, or RBR E3s to transfer ubiquitin to lysine residues on substrates | Minimal architecture centered on the conserved ~150–200 aa UBC domain with catalytic Cys and usually the HPN motif; no major N/C-terminal extensions | UBE2D family, UBE2L3, UBE2N/UBC13 | **No.** The class shares the core conjugating fold, but substrate choice, E3 partners, and chain/linkage outputs differ widely across members (liu2020theubiquitinconjugating pages 3-5, romantrufero2022theube2dubiquitin pages 1-2, cappadocia2018ubiquitinlikeproteinconjugation pages 11-12) |
| Canonical classes II–IV E2s (with N- and/or C-terminal extensions) | Ubiquitin transfer plus specialization through localization, E3 interaction, substrate recognition, or chain assembly tuning | UBC core plus N-terminal, C-terminal, or both extensions; some extensions stabilize closed E2~Ub conformations or add regulatory interactions | Cdc34/UBE2R1, UBE2J1/2, UBE2O | **No.** The appended regions drive substantial specialization, so extension-bearing E2s are not functionally uniform beyond being E2-like conjugating enzymes (liu2020theubiquitinconjugating pages 3-5, williams2019structuralinsightsinto pages 1-2, lv2024theroleof pages 1-2) |
| K48-chain-specialized E2s | Preferential synthesis of K48-linked polyubiquitin chains, commonly associated with proteasomal targeting | Canonical UBC fold but with subfamily-specific active-site gate dynamics or auxiliary ubiquitin-binding features; UBE2K/Ubc1 uniquely carries a UBA domain that promotes branched-chain contexts | E2-25K/UBE2K, Ubc1, Cdc34 | **No.** K48 specificity is restricted to certain subfamilies and is not a universal property of all ubiquitin-conjugating enzymes (rout2018activesitegate pages 1-2, williams2019structuralinsightsinto pages 1-2, lorenz2016crystalstructureof pages 1-2) |
| K63-chain-specialized E2s | Assembly of K63-linked chains important in DNA-damage tolerance, signaling, and immunity | Active E2 pairs with a catalytically inactive UEV cofactor; Ubc13/UBE2N has an open/atypical active-site-gate configuration compared with some K48 E2s | UBC13/UBE2N with MMS2/UBE2V1 or UBE2V2 | **No.** K63-chain assembly is a hallmark of the UBC13 lineage plus UEV cofactors, not of the family as a whole (liu2020theubiquitinconjugating pages 7-9, rout2018activesitegate pages 1-2, jones2019aconservedasparagine pages 1-2) |
| UEV proteins (E2 variants / pseudoenzymes) | Non-catalytic cofactors that support ubiquitin-chain assembly, especially K63-linked pathways, by partnering with active E2s | E2-like fold but lacking the catalytic cysteine, so they cannot form E2~Ub thioesters; retain interaction surfaces for heterodimer formation | MMS2, UBE2V1, UBE2V2, COP10-type UEVs | **No.** Loss of catalytic Cys means these are not active conjugating enzymes, so any family-level annotation implying catalytic ubiquitin-conjugating activity would over-annotate these variants if they are included (liu2020theubiquitinconjugating pages 3-5, liu2020theubiquitinconjugating pages 7-9) |
| J-family / membrane-associated noncanonical E2s | Support noncanonical ubiquitination on serine and/or threonine, especially in ERAD-related contexts, in addition to or instead of standard lysine chemistry | Conserved E2 fold with remodeled active site; in Ubc6/Ube2J2 a conserved histidine supports general-base catalysis for serine attack and altered thioester reactivity | Yeast Ubc6, human UBE2J2, UBE2J1 | **No.** Ser/Thr ubiquitination is a specialized innovation of a subset of E2s and cannot be generalized to the entire family (swarnkar2024determinantsofchemoselectivity pages 1-2, rehman2024discoveryandcharacterization pages 1-2) |
| UBE2Q family / noncanonical E2s | Noncanonical discharge of ubiquitin to serine/threonine and even other hydroxyl-containing biomolecules | Diverges from canonical E2s by lacking the well-conserved HPN triad and carrying an extended N-terminus; modeling/mutagenesis identified distinct activity determinants | UBE2Q family | **No.** This chemistry is subfamily-restricted and highlights that even within E2-like proteins, catalytic mechanism and target chemistry can diverge substantially (rehman2024discoveryandcharacterization pages 1-2) |
| E3-independent or highly autonomous E2s | Can ubiquitinate certain substrates or peptides with limited or no E3 requirement, useful for synthetic ubiquitination systems | Core UBC fold plus subfamily-specific surfaces that recognize short sequence motifs or enable intrinsic discharge; some are unusually permissive in vitro | UBE2E1, UBC22, UBE2O | **No.** E3-independent activity is exceptional, not a general E2 property; most E2s require an E3 for efficient physiological substrate modification (wu2024structureguidedengineeringenables pages 1-2, liu2020theubiquitinconjugating pages 7-9, gao2024unravelingtherole pages 1-3) |
| UBE2O / E2-E3 hybrid enzymes | Combines conjugating and ligase-like properties, enabling unusually direct substrate ubiquitination | Large multidomain protein with a conserved UBC catalytic core plus extensive additional regions supporting hybrid E2/E3 behavior | UBE2O | **No.** This is a highly derived specialization and should not be projected onto ordinary E2 family members (gao2024unravelingtherole pages 1-3, paubel2024dynamicexpressionof pages 1-2) |
| SUMO/NEDD8-related E2-like conjugases in broader E2 superfamily literature | Transfer ubiquitin-like proteins rather than ubiquitin itself; central to SUMOylation or neddylation rather than canonical ubiquitination | Retain E2/UBC-like fold but use pathway-specific interaction surfaces and catalytic microenvironments | UBC9/UBE2I, UBE2M, UBE2F | **No.** These demonstrate that an E2-like fold does not guarantee ubiquitin conjugation specifically; GO terms must distinguish ubiquitin from other Ubl pathways (cappadocia2018ubiquitinlikeproteinconjugation pages 11-12, paubel2024dynamicexpressionof pages 1-2) |


*Table: This table summarizes major axes of specialization within ubiquitin-conjugating enzymes, including linkage specificity, noncanonical chemistry, pseudoenzyme variants, and unusual E3 independence. It is useful for judging which functions are family-wide versus restricted to specific subfamilies, an important consideration for GO annotation review.*

### 3.1 Structural Classification

E2s are traditionally classified into four classes based on N- and C-terminal extensions (liu2020theubiquitinconjugating pages 3-5, williams2019structuralinsightsinto pages 1-2):

- **Class I**: UBC domain only
- **Class II**: N-terminal extension + UBC domain
- **Class III**: UBC domain + C-terminal extension  
- **Class IV**: N-terminal + UBC + C-terminal extensions

Phylogenetic analyses have further subdivided E2s into **17 distinct families** (kaminskaya2024trackingofubiquitin pages 1-2). Recent whole-genome analyses revealed 39 UBE2 genes in sperm whale, ~37-40 in humans, 14 in S. cerevisiae, 40 in Arabidopsis, 48 in rice, and 75 in maize (liu2020theubiquitinconjugating pages 3-5, liu2020theubiquitinconjugating pages 7-9, lv2024theroleof pages 1-2).

### 3.2 Functional Subfamilies with Divergent Activities

#### K48-Linkage Specialists
E2s like E2-25K/UBE2K and Cdc34 preferentially synthesize K48-linked polyubiquitin chains that signal proteasomal degradation (rout2018activesitegate pages 1-2, williams2019structuralinsightsinto pages 1-2). UBE2K uniquely contains a UBA domain that facilitates assembly of K48/K63-branched chains (williams2019structuralinsightsinto pages 1-2). These E2s adopt a canonical closed active-site gate conformation (rout2018activesitegate pages 1-2).

#### K63-Linkage Specialists  
UBC13/UBE2N operates with UEV cofactors (MMS2, UBE2V1, UBE2V2) to assemble K63-linked chains involved in DNA damage tolerance, signaling, and immunity rather than degradation (liu2020theubiquitinconjugating pages 7-9, jones2019aconservedasparagine pages 1-2). Structurally, UBC13 maintains an atypical open active-site gate (rout2018activesitegate pages 1-2).

#### Noncanonical Chemistry: Serine/Threonine Ubiquitination

The **J-family E2s** (yeast Ubc6, human UBE2J2) represent a major functional innovation: they can ubiquitinate **serine and threonine hydroxyl groups** in addition to or instead of lysine (swarnkar2024determinantsofchemoselectivity pages 1-2, rehman2024discoveryandcharacterization pages 1-2). Crystal structures and molecular dynamics simulations revealed a two-layered mechanism:

1. **Active-site remodeling** that enhances thioester reactivity toward weaker nucleophiles
2. **General base catalysis** by a conserved histidine (His94 in Ubc6) that activates substrate serine residues (swarnkar2024determinantsofchemoselectivity pages 1-2)

This chemistry is particularly important in ER-associated degradation (ERAD) pathways for processing substrates lacking surface lysines (swarnkar2024determinantsofchemoselectivity pages 1-2).

Similarly, the **UBE2Q family** mediates noncanonical ubiquitination of serine, threonine, and even non-protein biomolecules like glucose. UBE2Q enzymes diverge from canonical E2s by lacking the conserved HPN motif and possessing extended N-termini with distinct activity determinants (rehman2024discoveryandcharacterization pages 1-2).

#### E3-Independent E2s

While most E2s require E3 ligases for efficient substrate modification, **UBE2E1** can directly ubiquitinate substrates bearing specific short peptide motifs (e.g., KEGYES hexapeptide in SETDB1) without E3 involvement (wu2024structureguidedengineeringenables pages 1-2). Crystal structures revealed how UBE2E1 recognizes peptide sequence features to enable E3-free ubiquitination, providing a foundation for synthetic ubiquitination systems (wu2024structureguidedengineeringenables pages 1-2).

UBE2O represents an extreme case: this ~140 kDa **E2/E3 hybrid enzyme** combines a UBC catalytic core with extensive additional domains that confer ligase-like substrate recognition, enabling autonomous ubiquitination of diverse targets including ribosomal proteins, AMPKα2, and BMAL1 (gao2024unravelingtherole pages 1-3, paubel2024dynamicexpressionof pages 1-2).

### 3.3 Catalytically Inactive Pseudoenzymes (UEVs)

**Ubiquitin E2 Variants (UEVs)** retain the E2-like fold but lack the catalytic cysteine, rendering them incapable of forming E2~Ub thioesters (liu2020theubiquitinconjugating pages 3-5, liu2020theubiquitinconjugating pages 7-9). Despite being catalytically dead, UEVs play essential roles:

- **MMS2** (yeast) and **UBE2V1/V2** (mammals) form obligate heterodimers with UBC13 to enable K63-linked chain assembly critical for error-free DNA damage tolerance (liu2020theubiquitinconjugating pages 7-9)
- **COP10** participates in photomorphogenesis and protein degradation pathways (liu2020theubiquitinconjugating pages 7-9)

The existence of UEVs within the broader E2 family demonstrates that structural homology does not guarantee catalytic activity—a critical consideration for GO annotation.

### 3.4 Ubiquitin-Like Protein Conjugases

Some E2-like enzymes transfer **ubiquitin-like proteins** (Ubls) rather than ubiquitin itself:

- **UBC9/UBE2I**: SUMO-conjugating enzyme involved in SUMOylation pathways (paubel2024dynamicexpressionof pages 1-2, cappadocia2018ubiquitinlikeproteinconjugation pages 11-12)
- **UBE2M and UBE2F**: NEDD8-conjugating enzymes for neddylation of cullin-RING ligases (paubel2024dynamicexpressionof pages 1-2)

While these retain the E2/UBC fold, they operate in distinct post-translational modification pathways with different biological outcomes (cappadocia2018ubiquitinlikeproteinconjugation pages 11-12).

---

## 4. Taxonomic Scope

### 4.1 Evolutionary Conservation

The ubiquitin-conjugating enzyme superfamily is **universally present across eukaryotes** but essentially absent from bacteria and archaea (except for some proto-ubiquitin systems) (kaminskaya2024trackingofubiquitin pages 1-2). Phylogenomic analysis spanning 3.5 billion years demonstrates:

- The **E2 superfamily existed in its current form in the last common metazoan ancestor** and shows minimal divergence across metazoan phyla (kaminskaya2024trackingofubiquitin pages 1-2)
- The **UBC domain structure** (4 α-helices, 4 β-strands, catalytic cysteine) has remained remarkably conserved throughout eukaryotic evolution (kaminskaya2024trackingofubiquitin pages 1-2, romantrufero2022theube2dubiquitin pages 1-2)
- E2s are found in all major eukaryotic lineages: fungi, plants, animals, protists (liu2020theubiquitinconjugating pages 7-9, kaminskaya2024trackingofubiquitin pages 1-2)

### 4.2 Taxonomic Distribution Across PTHR24067

Given that PTHR24067 spans **69,450 proteins across 12,422 taxa**, this signature clearly includes E2s from:

- **Metazoans** (animals): Humans, mice, C. elegans, Drosophila
- **Fungi**: S. cerevisiae, Schizosaccharomyces pombe  
- **Plants**: Arabidopsis, rice, maize, tomato, wheat
- **Protists and other eukaryotes**

### 4.3 Cross-Taxa Process/Component Term Validity

Most **biological process terms would NOT hold across all taxa**:

- ERAD pathways (specific to organisms with ER)
- Proteasomal degradation machinery (configuration varies)
- Cell cycle checkpoints (mechanisms differ between yeast and mammals)
- Immune signaling (vertebrate-specific in many cases)

**Cellular component terms** are similarly problematic:

- Nuclear vs. cytoplasmic localization varies by E2 subfamily
- ER association applies only to ERAD-specialized E2s
- Chromatin association is subfamily-specific

---

## 5. Over-Annotation Verdict and Recommendations

### 5.1 Current Status: Appropriate

**PTHR24067 currently has NO InterPro2GO terms**, and this is **APPROPRIATE** given the entry type (family) and documented functional diversity.

### 5.2 Rationale for No Annotation

1. **Functional heterogeneity**: The 70 subfamilies within PTHR24067 exhibit markedly different functions including:
   - Different ubiquitin chain linkages (K48 vs. K63)
   - Canonical lysine vs. noncanonical serine/threonine chemistry
   - E3-dependent vs. E3-independent mechanisms
   - Ubiquitin vs. ubiquitin-like protein conjugation
   - Catalytically active vs. inactive (UEV) variants

2. **Entry type = family**: As a family-level signature (not domain or superfamily), PTHR24067 captures whole-protein functions, but those functions are **subfamily-specific** rather than family-wide.

3. **Risk of systematic over-annotation**: Applying any biological process or cellular component GO term at this level would systematically misannotate tens of thousands of proteins.

### 5.3 Recommended GO Annotation Strategy

**For PTHR24067 (family level): ACCEPT current NO-TERM status**

OR, if annotation is required:

**MODIFY to subfamily-specific mapping**:
- Move detailed functional annotations to the 70 subfamily entries
- At the family level, consider ONLY the most generic molecular function terms with caveats:
  - GO:0061631 (ubiquitin conjugating enzyme activity) — **BUT EXCLUDE UEV proteins**
  - GO:0016740 (transferase activity) — Safe for catalytically active members
  - GO:0005515 (protein binding) — Universal for E1/E3 interactions

**KEEP_AS_NON_CORE** any process/component terms — they are subfamily-specific and should map to child entries, not the parent family.

### 5.4 Recommended InterPro Actions

1. **Verify UEV inclusion**: Determine if PTHR24067 includes UEV proteins lacking catalytic cysteines. If yes, ANY annotation with "conjugating enzyme activity" over-annotates UEVs.

2. **Promote subfamily-level annotation**: The 70 subfamilies within PTHR24067 are the appropriate granularity for specific functional GO terms:
   - K48-chain specialists → proteasomal degradation terms
   - K63-chain specialists → DNA repair, signaling terms
   - J-family → ERAD-specific terms
   - SUMO/NEDD8 conjugases → distinct pathway terms

3. **Consider demoting to "homologous superfamily"**: If the goal is to group proteins by evolutionary homology rather than shared function, reclassifying as a superfamily would justify minimal GO annotation while child families/domains carry specific terms.

---

## Summary

InterPro entry PTHR24067 represents a functionally diverse family of ubiquitin-conjugating enzymes sharing a conserved UBC domain fold but exhibiting extensive specialization across 70 subfamilies. The core biochemistry—thioester formation between ubiquitin and a catalytic cysteine, followed by transfer to substrates—is conserved among catalytically active members (liu2020theubiquitinconjugating pages 3-5, swarnkar2024determinantsofchemoselectivity pages 1-2, wu2024structureguidedengineeringenables pages 1-2). However, subfamily-specific innovations include:

- **Pseudoenzyme variants** (UEVs) lacking catalytic activity (liu2020theubiquitinconjugating pages 3-5, liu2020theubiquitinconjugating pages 7-9)
- **Noncanonical chemistry** targeting serine/threonine (swarnkar2024determinantsofchemoselectivity pages 1-2, rehman2024discoveryandcharacterization pages 1-2)
- **Linkage specificity** (K48 vs. K63) determining distinct biological outcomes (liu2020theubiquitinconjugating pages 7-9, rout2018activesitegate pages 1-2)
- **E3-independent mechanisms** (wu2024structureguidedengineeringenables pages 1-2)
- **Ubiquitin-like protein conjugation** (paubel2024dynamicexpressionof pages 1-2, cappadocia2018ubiquitinlikeproteinconjugation pages 11-12)

Given this functional heterogeneity and the presence of catalytically inactive UEV proteins, **the current absence of InterPro2GO terms is appropriate and avoids systematic over-annotation**. Recommended action: **ACCEPT current status** or **MODIFY to subfamily-level mapping** with only the most generic molecular function terms at the family level, clearly excluding UEV proteins from conjugating activity annotations.

**Final Verdict: The InterPro2GO annotation strategy for PTHR24067 should be ACCEPT (no terms) or KEEP_AS_NON_CORE for any specific process/component terms, with detailed functional annotation delegated to the 70 child subfamily entries where functional homogeneity can be ensured.**

References

1. (liu2020theubiquitinconjugating pages 3-5): Weigang Liu, Xun Tang, Xuehong Qi, Xue Fu, Shantwana Ghimire, Rui Ma, Shigui Li, Ning Zhang, and Huaijun Si. The ubiquitin conjugating enzyme: an important ubiquitin transfer platform in ubiquitin-proteasome system. International Journal of Molecular Sciences, 21:2894, Apr 2020. URL: https://doi.org/10.3390/ijms21082894, doi:10.3390/ijms21082894. This article has 172 citations.

2. (cappadocia2018ubiquitinlikeproteinconjugation pages 11-12): Laurent Cappadocia and Christopher D. Lima. Ubiquitin-like protein conjugation: structures, chemistry, and mechanism. Chemical Reviews, 118:889-918, Feb 2018. URL: https://doi.org/10.1021/acs.chemrev.6b00737, doi:10.1021/acs.chemrev.6b00737. This article has 708 citations and is from a highest quality peer-reviewed journal.

3. (kaminskaya2024trackingofubiquitin pages 1-2): Alena N. Kaminskaya, Alena S. Evpak, Alexey A. Belogurov, and Anna A. Kudriaeva. Tracking of ubiquitin signaling through 3.5 billion years of combinatorial conjugation. Aug 2024. URL: https://doi.org/10.3390/ijms25168671, doi:10.3390/ijms25168671. This article has 4 citations.

4. (swarnkar2024determinantsofchemoselectivity pages 1-2): Anuruti Swarnkar, Florian Leidner, Ashok K Rout, Sofia Ainatzi, Claudia C Schmidt, Stefan Becker, Henning Urlaub, Christian Griesinger, Helmut Grubmüller, and Alexander Stein. Determinants of chemoselectivity in ubiquitination by the j2 family of ubiquitin-conjugating enzymes. The EMBO Journal, 43:6705-6739, Nov 2024. URL: https://doi.org/10.1038/s44318-024-00301-3, doi:10.1038/s44318-024-00301-3. This article has 7 citations.

5. (wu2024structureguidedengineeringenables pages 1-2): Xiangwei Wu, Yunxiang Du, Lu-Jun Liang, Ruichao Ding, Tianyi Zhang, Hongyi Cai, Xiaolin Tian, Man Pan, and Lei Liu. Structure-guided engineering enables e3 ligase-free and versatile protein ubiquitination via ube2e1. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45635-y, doi:10.1038/s41467-024-45635-y. This article has 39 citations and is from a highest quality peer-reviewed journal.

6. (rehman2024discoveryandcharacterization pages 1-2): Syed Arif Abdul Rehman, Chiara Cazzaniga, Elena Di Nisio, Odetta Antico, Axel Knebel, Clare Johnson, Alp T. Şahin, Peter E. G. F. Ibrahim, Frederic Lamoliatte, Rodolfo Negri, Miratul M K Muqit, and Virginia De Cesare. Discovery and characterization of noncanonical e2-conjugating enzymes. Science Advances, Mar 2024. URL: https://doi.org/10.1126/sciadv.adh0123, doi:10.1126/sciadv.adh0123. This article has 22 citations and is from a highest quality peer-reviewed journal.

7. (lv2024theroleof pages 1-2): Peng Lv, Jihong Liu, and Xiaming Liu. The role of ubiquitin-conjugating enzyme in the process of spermatogenesis. Reproductive Biology and Endocrinology : RB&E, Aug 2024. URL: https://doi.org/10.1186/s12958-024-01282-y, doi:10.1186/s12958-024-01282-y. This article has 9 citations.

8. (jones2019aconservedasparagine pages 1-2): Walker M. Jones, Aaron G. Davis, R. Hunter Wilson, Katherine L. Elliott, and Isaiah Sumner. A conserved asparagine in a ubiquitin‐conjugating enzyme positions the substrate for nucleophilic attack. May 2019. URL: https://doi.org/10.1002/jcc.25852, doi:10.1002/jcc.25852. This article has 11 citations and is from a peer-reviewed journal.

9. (rout2018activesitegate pages 1-2): Manoj K. Rout, Brian L. Lee, Aiyang Lin, Wei Xiao, and Leo Spyracopoulos. Active site gate dynamics modulate the catalytic activity of the ubiquitination enzyme e2-25k. Scientific Reports, May 2018. URL: https://doi.org/10.1038/s41598-018-25476-8, doi:10.1038/s41598-018-25476-8. This article has 19 citations and is from a peer-reviewed journal.

10. (williams2019structuralinsightsinto pages 1-2): Katelyn M. Williams, Shuo Qie, James H. Atkison, Sabrina Salazar-Arango, J. Alan Diehl, and Shaun K. Olsen. Structural insights into e1 recognition and the ubiquitin-conjugating activity of the e2 enzyme cdc34. Nature Communications, Jul 2019. URL: https://doi.org/10.1038/s41467-019-11061-8, doi:10.1038/s41467-019-11061-8. This article has 69 citations and is from a highest quality peer-reviewed journal.

11. (liess2019autoinhibitionmechanismof pages 1-3): Anna K.L. Liess, Alena Kucerova, Kristian Schweimer, Lu Yu, Theodoros I. Roumeliotis, Mathias Diebold, Olexandr Dybkov, Christoph Sotriffer, Henning Urlaub, Jyoti S. Choudhary, Jörg Mansfeld, and Sonja Lorenz. Autoinhibition mechanism of the ubiquitin-conjugating enzyme ube2s by autoubiquitination. Structure, 27:1195-1210.e7, Aug 2019. URL: https://doi.org/10.1016/j.str.2019.05.008, doi:10.1016/j.str.2019.05.008. This article has 37 citations and is from a domain leading peer-reviewed journal.

12. (lorenz2016crystalstructureof pages 1-2): S. Lorenz, Moitrayee Bhattacharyya, C. Feiler, M. Rapé, and J. Kuriyan. Crystal structure of a ube2s-ubiquitin conjugate. Feb 2016. URL: https://doi.org/10.2210/pdb5bnb/pdb, doi:10.2210/pdb5bnb/pdb. This article has 33 citations.

13. (liu2020theubiquitinconjugating pages 7-9): Weigang Liu, Xun Tang, Xuehong Qi, Xue Fu, Shantwana Ghimire, Rui Ma, Shigui Li, Ning Zhang, and Huaijun Si. The ubiquitin conjugating enzyme: an important ubiquitin transfer platform in ubiquitin-proteasome system. International Journal of Molecular Sciences, 21:2894, Apr 2020. URL: https://doi.org/10.3390/ijms21082894, doi:10.3390/ijms21082894. This article has 172 citations.

14. (cappadocia2018ubiquitinlikeproteinconjugation pages 5-6): Laurent Cappadocia and Christopher D. Lima. Ubiquitin-like protein conjugation: structures, chemistry, and mechanism. Chemical Reviews, 118:889-918, Feb 2018. URL: https://doi.org/10.1021/acs.chemrev.6b00737, doi:10.1021/acs.chemrev.6b00737. This article has 708 citations and is from a highest quality peer-reviewed journal.

15. (bui2021ubiquitinconjugatingenzymesin pages 1-2): Quyen Thu Bui, Jeong Hee Hong, Minseok Kwak, Ji Yeon Lee, and Peter Chang-Whan Lee. Ubiquitin-conjugating enzymes in cancer. Cells, 10:1383, Jun 2021. URL: https://doi.org/10.3390/cells10061383, doi:10.3390/cells10061383. This article has 65 citations.

16. (romantrufero2022theube2dubiquitin pages 1-2): Monica Roman-Trufero and Niall Dillon. The ube2d ubiquitin conjugating enzymes: potential regulatory hubs in development, disease and evolution. Frontiers in Cell and Developmental Biology, Dec 2022. URL: https://doi.org/10.3389/fcell.2022.1058751, doi:10.3389/fcell.2022.1058751. This article has 35 citations.

17. (paubel2024dynamicexpressionof pages 1-2): Agathe Paubel, Sylviane Marouillat, Audrey Dangoumau, Cindy Maurel, Shanez Haouari, Hélène Blasco, Philippe Corcia, Frédéric Laumonnier, Christian R. Andres, and Patrick Vourc’h. Dynamic expression of genes encoding ubiquitin conjugating enzymes (e2s) during neuronal differentiation and maturation: implications for neurodevelopmental disorders and neurodegenerative diseases. Genes, 15:1381, Oct 2024. URL: https://doi.org/10.3390/genes15111381, doi:10.3390/genes15111381. This article has 4 citations.

18. (gao2024unravelingtherole pages 1-3): Chang Gao, Yan-Jun Liu, Jing Yu, Ran Wang, Jin-Jin Shi, Ru-Yi Chen, Guan-Jun Yang, and Jiong Chen. Unraveling the role of ubiquitin-conjugating enzyme ube2t in tumorigenesis: a comprehensive review. Cells, 14:15, Dec 2024. URL: https://doi.org/10.3390/cells14010015, doi:10.3390/cells14010015. This article has 13 citations.

## Artifacts

- [Edison artifact artifact-00](PTHR24067-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR24067-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. cappadocia2018ubiquitinlikeproteinconjugation pages 11-12
2. kaminskaya2024trackingofubiquitin pages 1-2
3. rout2018activesitegate pages 1-2
4. williams2019structuralinsightsinto pages 1-2
5. jones2019aconservedasparagine pages 1-2
6. liu2020theubiquitinconjugating pages 7-9
7. swarnkar2024determinantsofchemoselectivity pages 1-2
8. rehman2024discoveryandcharacterization pages 1-2
9. wu2024structureguidedengineeringenables pages 1-2
10. paubel2024dynamicexpressionof pages 1-2
11. liu2020theubiquitinconjugating pages 3-5
12. lv2024theroleof pages 1-2
13. liess2019autoinhibitionmechanismof pages 1-3
14. lorenz2016crystalstructureof pages 1-2
15. cappadocia2018ubiquitinlikeproteinconjugation pages 5-6
16. bui2021ubiquitinconjugatingenzymesin pages 1-2
17. gao2024unravelingtherole pages 1-3
18. https://doi.org/10.3390/ijms21082894,
19. https://doi.org/10.1021/acs.chemrev.6b00737,
20. https://doi.org/10.3390/ijms25168671,
21. https://doi.org/10.1038/s44318-024-00301-3,
22. https://doi.org/10.1038/s41467-024-45635-y,
23. https://doi.org/10.1126/sciadv.adh0123,
24. https://doi.org/10.1186/s12958-024-01282-y,
25. https://doi.org/10.1002/jcc.25852,
26. https://doi.org/10.1038/s41598-018-25476-8,
27. https://doi.org/10.1038/s41467-019-11061-8,
28. https://doi.org/10.1016/j.str.2019.05.008,
29. https://doi.org/10.2210/pdb5bnb/pdb,
30. https://doi.org/10.3390/cells10061383,
31. https://doi.org/10.3389/fcell.2022.1058751,
32. https://doi.org/10.3390/genes15111381,
33. https://doi.org/10.3390/cells14010015,