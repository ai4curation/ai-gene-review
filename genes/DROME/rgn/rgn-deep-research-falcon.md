---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-10T14:34:06.405017'
end_time: '2026-09-10T14:40:38.771146'
duration_seconds: 392.37
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: rgn
  gene_symbol: rgn
  uniprot_accession: M9PFV8
  protein_description: 'SubName: Full=Regeneration, isoform B {ECO:0000313|EMBL:AFH04537.1};
    SubName: Full=Regeneration, isoform C {ECO:0000313|EMBL:AGB94848.1};'
  gene_info: Name=rgn {ECO:0000313|EMBL:AGB94848.1, ECO:0000313|FlyBase:FBgn0261258};
    Synonyms=BcDNA:GH11973 {ECO:0000313|EMBL:AGB94848.1}, Dmel\CG6014 {ECO:0000313|EMBL:AGB94848.1},
    l(3)00534 {ECO:0000313|EMBL:AGB94848.1}, RGN {ECO:0000313|EMBL:AGB94848.1}; ORFNames=CG6014
    {ECO:0000313|EMBL:AGB94848.1, ECO:0000313|FlyBase:FBgn0261258}, Dmel_CG6014 {ECO:0000313|EMBL:AGB94848.1};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Not specified in UniProt
  protein_domains: C-type_lectin-like. (IPR001304); C-type_lectin-like/link_sf. (IPR016186);
    CTDL_fold. (IPR016187); Lectin_C (PF00059)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 14
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: rgn-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** M9PFV8
- **Protein Description:** SubName: Full=Regeneration, isoform B {ECO:0000313|EMBL:AFH04537.1}; SubName: Full=Regeneration, isoform C {ECO:0000313|EMBL:AGB94848.1};
- **Gene Information:** Name=rgn {ECO:0000313|EMBL:AGB94848.1, ECO:0000313|FlyBase:FBgn0261258}; Synonyms=BcDNA:GH11973 {ECO:0000313|EMBL:AGB94848.1}, Dmel\CG6014 {ECO:0000313|EMBL:AGB94848.1}, l(3)00534 {ECO:0000313|EMBL:AGB94848.1}, RGN {ECO:0000313|EMBL:AGB94848.1}; ORFNames=CG6014 {ECO:0000313|EMBL:AGB94848.1, ECO:0000313|FlyBase:FBgn0261258}, Dmel_CG6014 {ECO:0000313|EMBL:AGB94848.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** C-type_lectin-like. (IPR001304); C-type_lectin-like/link_sf. (IPR016186); CTDL_fold. (IPR016187); Lectin_C (PF00059)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "rgn" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'rgn' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **rgn** (gene ID: rgn, UniProt: M9PFV8) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

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

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** M9PFV8
- **Protein Description:** SubName: Full=Regeneration, isoform B {ECO:0000313|EMBL:AFH04537.1}; SubName: Full=Regeneration, isoform C {ECO:0000313|EMBL:AGB94848.1};
- **Gene Information:** Name=rgn {ECO:0000313|EMBL:AGB94848.1, ECO:0000313|FlyBase:FBgn0261258}; Synonyms=BcDNA:GH11973 {ECO:0000313|EMBL:AGB94848.1}, Dmel\CG6014 {ECO:0000313|EMBL:AGB94848.1}, l(3)00534 {ECO:0000313|EMBL:AGB94848.1}, RGN {ECO:0000313|EMBL:AGB94848.1}; ORFNames=CG6014 {ECO:0000313|EMBL:AGB94848.1, ECO:0000313|FlyBase:FBgn0261258}, Dmel_CG6014 {ECO:0000313|EMBL:AGB94848.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** C-type_lectin-like. (IPR001304); C-type_lectin-like/link_sf. (IPR016186); CTDL_fold. (IPR016187); Lectin_C (PF00059)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "rgn" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'rgn' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **rgn** (gene ID: rgn, UniProt: M9PFV8) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Drosophila melanogaster* **rgn** (CG6014; UniProt M9PFV8)

## Executive conclusion

The gene symbol **rgn is ambiguous across organisms**, but the target specified here can be verified as the *Drosophila melanogaster* gene **regeneration** (*rgn*; **CG6014**, **FBgn0261258**), represented by UniProt **M9PFV8** and described with isoforms B and C. It must not be confused with mammalian **RGN/regucalcin**, which is a different protein. The fly literature uses *regeneration/rgn* in the imaginal-disc regeneration context and connects it to blastema formation, matching the supplied identity rather than the mammalian homonym (smithbolton2016drosophilaimaginaldiscsas pages 5-6, bergmann2010apoptosisstemcells pages 5-6).

The strongest defensible functional annotation is:

> **Rgn is a poorly characterized, C-type-lectin-like protein required for the correct temporal and spatial organization of the regenerative blastema in injured Drosophila imaginal discs. Genetic evidence places it among Wingless/Wnt-responsive regeneration genes, but its ligand, biochemical activity, immediate interaction partners, and subcellular location remain unknown.**

Consequently, Rgn should presently be annotated as a **regulator/effector of epithelial tissue regeneration**, not as a proven enzyme, carbohydrate-binding lectin, receptor, or transporter.

| Question/feature | Best-supported conclusion | Evidence type/source/year | Confidence | Key limitation |
|---|---|---|---|---|
| Identity | The research target is *Drosophila melanogaster* **regeneration** (**rgn/CG6014; FBgn0261258; UniProt M9PFV8**), not mammalian **RGN/regucalcin** or another similarly named gene. | Identifier/alias correspondence supplied by UniProt; *Drosophila* literature independently uses **rgn/regeneration** for the imaginal-disc regeneration gene (2010–2016) (smithbolton2016drosophilaimaginaldiscsas pages 5-6, bergmann2010apoptosisstemcells pages 5-6) | High | M9PFV8 is not extensively characterized experimentally; identifier matching does not establish molecular function. |
| Primary biological function | Genetic evidence places **rgn** in the control of regenerative blastema formation after imaginal-disc injury. The primary study is summarized as showing control of blastema **timing, site, and size**, while a later expert review specifically emphasizes control of **timing** (sap2015globalquantitativeproteomics pages 5-8, bergmann2010apoptosisstemcells pages 5-6). | Functional genetics from McClure, Sustar & Schubiger (2008), as summarized in peer-reviewed reviews (2010, 2016) (smithbolton2016drosophilaimaginaldiscsas pages 5-6, bergmann2010apoptosisstemcells pages 5-6) | Moderate–high | Available excerpts do not provide allele identities, rescue tests, effect sizes, or enough primary-study detail to assign separate molecular mechanisms to timing, position, and size. |
| Wg/Wnt pathway placement | **rgn** was identified among conserved **Wingless (Wg/Wnt) target genes** functioning in P35-independent imaginal-disc regeneration, supporting placement downstream of or responsive to Wg during blastema formation (bergmann2010apoptosisstemcells pages 5-6). | Genetic-screen/review synthesis (2010) (bergmann2010apoptosisstemcells pages 5-6) | Moderate | Direct Wg binding to an **rgn** regulatory element, pathway epistasis, and direct transcriptional regulation were not demonstrated in the retrieved material. General requirements for Wg, JNK, and other regenerative pathways must not be attributed automatically to Rgn. |
| Protein architecture | UniProt-supplied annotations assign a **C-type lectin-like domain/fold** (InterPro IPR001304, IPR016186, IPR016187; Pfam Lectin_C/PF00059). This supports a possible ligand-binding or interaction role, but only as a structural/bioinformatic hypothesis. | Computational domain annotation supplied with the target record; no retrieved Rgn-specific structural experiment | Moderate for fold assignment; low for functional inference | A C-type lectin-like fold does not by itself establish carbohydrate binding, calcium dependence, receptor activity, secretion, or substrate specificity. |
| Cellular/subcellular localization | **Unknown.** The retrieved Rgn-specific literature does not establish whether Rgn acts intracellularly, at the plasma membrane, in extracellular space, or in a particular blastema cell population (sap2015globalquantitativeproteomics pages 5-8, smithbolton2016drosophilaimaginaldiscsas pages 5-6). | Absence of direct localization evidence in retrieved experimental/review literature | Low/undetermined | No Rgn-specific antibody imaging, tagged-protein localization, secretion assay, topology experiment, or spatial transcript analysis was found. |
| Biochemical ligand or activity | **Unknown.** No catalytic reaction, substrate, glycan ligand, binding partner, or receptor/adaptor mechanism has been experimentally assigned to Rgn. | Evidence-gap assessment; reviews support a regeneration phenotype but not biochemical mechanism (sap2015globalquantitativeproteomics pages 5-8, smithbolton2016drosophilaimaginaldiscsas pages 5-6, bergmann2010apoptosisstemcells pages 5-6) | High confidence that no assignment is supported by the retrieved evidence | Negative literature retrieval is not proof that no unpublished or database-linked evidence exists; biochemical testing is still required. |
| Ecdysone response | Rgn is an **ecdysone-responsive protein candidate** from a SILAC screen of Kc cells. The experiment quantified **5,748 proteins across six time points from 0–96 h**, and Rgn appeared among a small set changing at early times (sap2015globalquantitativeproteomics pages 5-8). | High-throughput quantitative proteomics, Sap et al. (published February 2015) (sap2015globalquantitativeproteomics pages 5-8) | Low–moderate | No Rgn-specific fold change, peptide validation, immunoblot, perturbation, or functional linkage to ecdysone was reported in the available text; the study’s detailed validation concerned BR-C, not Rgn. |
| Recent research status, 2023–2024 | No **2023–2024 Rgn/CG6014-specific** mechanistic publication was retrieved. Modern regeneration studies refine blastema cell states and pathways, but available text does not explicitly validate **rgn** as a marker or effector (worley2021criticalgeneticprogram pages 24-35, worley2021criticalgeneticprogram pages 16-18). | Targeted literature search plus comparison with a 2021 single-cell imaginal-disc regeneration study | Moderate | Search coverage and text availability are incomplete; failure to retrieve a paper is not definitive evidence of absence. |
| Research applications | **rgn** is currently most defensible as a genetic entry point for studying how Wg-responsive programs coordinate the temporal and spatial organization of epithelial repair. Priority applications are endogenous tagging/localization, injury-resolved single-cell expression, Wg-response tests, genetic rescue/epistasis, and biochemical ligand screens. | Evidence-guided research interpretation based on the established blastema phenotype and unresolved molecular mechanism (smithbolton2016drosophilaimaginaldiscsas pages 5-6, bergmann2010apoptosisstemcells pages 5-6) | Moderate | These are proposed research uses, not established clinical, agricultural, or biotechnology implementations. |


*Table: Evidence-weighted summary for *Drosophila melanogaster* rgn/CG6014, separating functional genetics and proteomics from domain-based inference and unresolved questions. It highlights that blastema regulation is supported, whereas localization and biochemical activity remain unknown.*

## 1. Identity and domain verification

### 1.1 Correct gene and organism

The requested identifiers are mutually consistent: *rgn*, *regeneration*, CG6014/Dmel\CG6014, FBgn0261258, and UniProt M9PFV8 refer to a protein from ***Drosophila melanogaster***. The phenotype literature describes a fly gene named *regeneration/rgn* implicated in imaginal-disc blastema formation, independently supporting the supplied identity (smithbolton2016drosophilaimaginaldiscsas pages 5-6, bergmann2010apoptosisstemcells pages 5-6).

This qualification is essential because **RGN** commonly denotes vertebrate regucalcin in other literature. No regucalcin findings should be transferred to M9PFV8.

### 1.2 Protein architecture

The supplied UniProt record assigns the protein a **C-type lectin-like domain/fold**, including InterPro IPR001304, IPR016186 and IPR016187 and Pfam **Lectin_C/PF00059**. This architecture is compatible with a molecular-recognition or protein-interaction role, but a C-type lectin-like fold does **not** by itself demonstrate carbohydrate binding, calcium dependence, secretion, receptor activity, or a particular ligand.

No retrieved study reported purified Rgn protein, a solved structure, glycan-array analysis, calcium-binding measurements, ligand-binding kinetics, catalytic assays, or mutational analysis of the predicted domain. Accordingly, “C-type lectin-like protein” is an appropriate structural description; “C-type lectin” as an experimentally demonstrated biochemical function is not.

## 2. Primary biological function

### 2.1 Regulation of blastema formation

Rgn was initially identified through genetic screening related to altered tissue identity and outgrowth—transdetermination—and was subsequently tested in fragmented imaginal discs. A later authoritative review states that *rgn*, together with *mmp1* and *alr*, is important for blastema formation after disc fragmentation (smithbolton2016drosophilaimaginaldiscsas pages 5-6).

The 2008 primary study is summarized in later sources as showing that Rgn controls the **timing, site, and size** of blastema formation. A mechanistic review places particular emphasis on **timing**, distinguishing Rgn from Alr, which regulates blastema-cell proliferation and the extent of regeneration, and Mmp1, which limits regenerative proliferation by controlling arrest outside the blastema (sap2015globalquantitativeproteomics pages 5-8, bergmann2010apoptosisstemcells pages 5-6). This distinction suggests that Rgn’s most specific established role is not simply “promoting proliferation”; rather, it helps determine **when and where a regenerative growth zone forms and how it is delimited**.

The accessible evidence does not provide allele-by-allele effect sizes, rescue data, or enough primary-study detail to determine whether the timing, position, and size phenotypes reflect one molecular mechanism or several. Thus, “controls blastema formation” is secure, whereas a more specific biochemical explanation remains premature.

### 2.2 Tissue and biological process

The demonstrated setting is the **larval imaginal disc**, a proliferative epithelial primordium that generates adult structures during metamorphosis. Following fragmentation or spatially restricted damage, proliferative activity becomes concentrated in a blastema near the wound. Cells near the wound produce larger clones than cells outside it, while distant cells reduce proliferation or arrest (smithbolton2016drosophilaimaginaldiscsas pages 5-6). Rgn’s phenotype should therefore be interpreted within **epithelial wound repair, compensatory growth, and appendage-primordium regeneration**.

There is no comparable direct evidence in the retrieved literature for a primary role in adult gut repair, neuronal regeneration, immunity, metabolism, or normal organogenesis. Those functions should not be inferred merely because other C-type lectin-like proteins participate in such processes.

## 3. Pathway placement

### 3.1 Wingless/Wnt signaling

The clearest pathway connection is to **Wingless (Wg), the Drosophila Wnt ligand**. An expert review describes *rgn* as one of at least three conserved Wg target genes functioning in P35-independent tissue regeneration and reports that genetic analysis assigned Rgn a role in blastema timing (bergmann2010apoptosisstemcells pages 5-6).

In injured imaginal discs, Wg is induced near wound edges or in blastema-forming cells; Wg signaling promotes regenerative proliferation and induces growth regulators including Myc and Cyclin E (smithbolton2016drosophilaimaginaldiscsas pages 5-6). These observations provide the physiological setting for *rgn*, but they do not prove that Rgn directly binds Wg, is a Wg receptor, or transduces the canonical pathway. The conservative model is:

**injury → Wg/Wnt response → induction or deployment of Rgn and other regeneration effectors → properly timed and positioned blastema formation.**

Direct transcriptional regulation remains incompletely demonstrated in the retrieved evidence: no Rgn enhancer with TCF/Pangolin occupancy, reporter assay, ChIP result, or decisive epistasis experiment was available. Therefore, “Wg-responsive/target gene” is supported at the genetic-screen level; “direct canonical Wg transcriptional target” remains to be established.

### 3.2 JNK, Hippo/Yorkie, JAK/STAT, EGFR and damage signaling

JNK is activated at damaged disc margins and is needed for wound closure and regenerative growth. JNK-positive cells contribute extensively to regenerated tissue; JNK also promotes Yorkie activity through the Ajuba–Hippo module. Wg, JNK, Yorkie and other pathways collectively organize the blastema (smithbolton2016drosophilaimaginaldiscsas pages 5-6). However, the retrieved literature does **not** demonstrate that Rgn physically or genetically acts in the JNK–Hippo module.

Modern single-cell work identified regeneration-specific epithelial populations and an Ets21C-associated program containing *Ilp8*, *Mmp1*, *upd1–3*, *Wnt4*, *Wnt6* and *wg*. In one dataset, regenerating discs comprised 6,613 epithelial cells, 7,466 myoblasts, 224 hemocytes and 17 tracheal cells; the study resolved two blastema populations that were nearly absent from normally developing discs (worley2021criticalgeneticprogram pages 24-35). Nevertheless, available text did not identify *rgn/CG6014* as a marker or Ets21C target. These recent pathway findings therefore provide context, not direct Rgn annotation.

## 4. Cellular and subcellular localization

The location at which the Rgn protein acts is **unknown**. Its phenotype is expressed at the level of the imaginal-disc blastema, but the retrieved evidence does not resolve whether Rgn is made by blastema epithelial cells, adjacent surviving cells, myoblasts, hemocytes, or another population. Nor does it establish whether the protein is extracellular, membrane-associated, cytoplasmic, organellar, or nuclear (sap2015globalquantitativeproteomics pages 5-8, smithbolton2016drosophilaimaginaldiscsas pages 5-6).

The predicted C-type lectin-like domain may motivate a hypothesis of extracellular or cell-surface molecular recognition, but localization cannot be inferred from the fold alone. A defensible database annotation should therefore avoid assigning “secreted,” “plasma membrane,” or “extracellular matrix” without independent signal-peptide/topology evidence and experimental confirmation.

Priority localization experiments would include endogenous CRISPR tagging with functional rescue, time-resolved imaging after injury, extracellular staining without permeabilization, secretion assays, and spatial transcriptomics or injury-stage single-cell RNA sequencing with explicit CG6014 analysis.

## 5. Biochemical mechanism and substrate specificity

No enzymatic reaction is known for Rgn. There is no evidence that it is a transporter, and no transported substrate has been identified. Likewise, no carbohydrate, glycoprotein, lipid, extracellular-matrix component, or protein ligand has been shown to bind Rgn.

The best current molecular hypothesis is that its C-type lectin-like fold mediates **molecular recognition or assembly of a signaling/adhesion complex** during blastema organization. This remains an inference, not an established function. Suitable tests include recombinant-domain glycan arrays, unbiased affinity purification–mass spectrometry, proximity labeling in regenerating discs, surface-plasmon resonance against candidate ligands, calcium-dependence assays, and structure-guided mutation of conserved domain residues.

## 6. Evidence for hormonal regulation

A 2015 SILAC proteomics study treated Drosophila Kc cells with ecdysone and quantified **5,748 proteins at six time points spanning 0–96 hours**. Rgn was among a small set of proteins whose abundance deviated at early time points, making it a candidate ecdysone-responsive protein (publication: February 2015; DOI/URL: https://doi.org/10.1002/pmic.201400308) (sap2015globalquantitativeproteomics pages 5-8).

This result is suggestive because ecdysone coordinates larval development and metamorphosis, processes that constrain the regenerative window. Nevertheless, it is high-throughput evidence only. The accessible report gives no Rgn-specific fold change, peptide-spectrum validation, immunoblot, transcript confirmation, or functional perturbation. Detailed validation in the study concerned BR-C rather than Rgn (sap2015globalquantitativeproteomics pages 5-8). Rgn should therefore not yet be called an established component of the ecdysone pathway.

## 7. Recent developments and status of the field

No 2023–2024 publication specifically resolving Rgn/CG6014’s mechanism, ligand, structure, or localization was retrieved. The latest relevant advances instead concern the broader architecture of Drosophila regeneration: injury-specific epithelial states, secretory blastema programs, Ets21C-associated transcription, Wg/JNK signaling, and developmental-delay mechanisms. For example, single-cell analysis separated epithelial, myoblast and hemocyte populations and identified two regeneration-associated blastema clusters, but the accessible results did not explicitly implicate *rgn* (worley2021criticalgeneticprogram pages 24-35, worley2021criticalgeneticprogram pages 16-18).

Thus, the gene remains substantially under-annotated despite modern systems-level resources. Absence from accessible text should not be interpreted as biological absence: CG6014 may be expressed below detection thresholds, in a narrow temporal window, or under an alternative identifier in supplementary matrices. Reanalysis of deposited single-cell datasets using FBgn0261258/CG6014 would be informative.

## 8. Applications and real-world implementation

There is no documented clinical, diagnostic, agricultural or industrial implementation of Rgn. Its present application is primarily as a **Drosophila genetic research target** for dissecting how Wnt-responsive injury programs establish the timing, position and extent of regenerative growth.

Potential research uses include:

1. identifying molecular checkpoints that initiate a blastema;
2. separating spatial organization of repair from generic mitogenic signaling;
3. determining whether a lectin-like recognition mechanism links tissue damage to regenerative patterning;
4. testing how endocrine maturation signals intersect with local injury responses; and
5. comparing regenerative programs with aberrant growth, because injury-associated pathways can be co-opted in tumors.

These are experimental opportunities, not established translational applications.

## 9. Evidence-weighted annotation recommendation

**Recommended functional statement:** “C-type lectin-like protein required for normal imaginal-disc regeneration; genetically regulates the timing and spatial organization of blastema formation and is associated with Wingless/Wnt-responsive regenerative signaling.”

**Recommended biological processes:** imaginal-disc regeneration; epithelial wound response; blastema formation; regulation of regenerative growth.

**Pathway:** Wg/Wnt-responsive regeneration, with broader JNK/Hippo/JAK–STAT injury signaling treated as contextual rather than directly demonstrated Rgn pathways.

**Localization:** unknown.

**Molecular activity and ligand:** unknown; no catalytic reaction, transporter substrate, or lectin ligand has been demonstrated.

**Confidence:** moderate-to-high for the blastema phenotype; moderate for Wg-pathway placement; low for any molecular-mechanistic or localization assignment.

## Key references

- McClure KD, Sustar A, Schubiger G. “Three genes control the timing, the site and the size of blastema formation in Drosophila.” *Developmental Biology* (July 2008). DOI/URL: https://doi.org/10.1016/j.ydbio.2008.04.004. The direct genetic study is not fully accessible in the retrieved corpus; its findings are corroborated by subsequent peer-reviewed reviews (sap2015globalquantitativeproteomics pages 5-8, smithbolton2016drosophilaimaginaldiscsas pages 5-6, bergmann2010apoptosisstemcells pages 5-6).
- Bergmann A, Steller H. “Apoptosis, Stem Cells, and Tissue Regeneration.” *Science Signaling* (26 October 2010), 3:re8. https://doi.org/10.1126/scisignal.3145re8 (bergmann2010apoptosisstemcells pages 5-6).
- Sap KA et al. “Global quantitative proteomics reveals novel factors in the ecdysone signaling pathway in Drosophila melanogaster.” *PROTEOMICS* (February 2015), 15:725–738. https://doi.org/10.1002/pmic.201400308 (sap2015globalquantitativeproteomics pages 5-8).
- Smith-Bolton RK. “Drosophila Imaginal Discs as a Model of Epithelial Wound Repair and Regeneration.” *Advances in Wound Care* (June 2016), 5:251–261. https://doi.org/10.1089/wound.2014.0547 (smithbolton2016drosophilaimaginaldiscsas pages 5-6).
- Worley MI et al. “Critical genetic program for Drosophila imaginal disc regeneration revealed by single-cell analysis.” bioRxiv (July 2021). https://doi.org/10.1101/2021.07.08.451678. This supplies current blastema-cell context but no explicit Rgn-specific validation in the accessible text (worley2021criticalgeneticprogram pages 24-35, worley2021criticalgeneticprogram pages 16-18).

References

1. (smithbolton2016drosophilaimaginaldiscsas pages 5-6): Rachel K. Smith-Bolton. <i>drosophila</i>imaginal discs as a model of epithelial wound repair and regeneration. Jun 2016. URL: https://doi.org/10.1089/wound.2014.0547, doi:10.1089/wound.2014.0547. This article has 33 citations and is from a peer-reviewed journal.

2. (bergmann2010apoptosisstemcells pages 5-6): Andreas Bergmann and Hermann Steller. Apoptosis, stem cells, and tissue regeneration. Science Signaling, 3:re8-re8, Oct 2010. URL: https://doi.org/10.1126/scisignal.3145re8, doi:10.1126/scisignal.3145re8. This article has 418 citations and is from a domain leading peer-reviewed journal.

3. (sap2015globalquantitativeproteomics pages 5-8): Karen A. Sap, Karel Bezstarosti, Dick H. W. Dekkers, Mirjam van den Hout, Wilfred van Ijcken, Erikjan Rijkers, and Jeroen A. A. Demmers. Global quantitative proteomics reveals novel factors in the ecdysone signaling pathway in drosophila melanogaster. PROTEOMICS, 15:725-738, Feb 2015. URL: https://doi.org/10.1002/pmic.201400308, doi:10.1002/pmic.201400308. This article has 15 citations and is from a peer-reviewed journal.

4. (worley2021criticalgeneticprogram pages 24-35): Melanie I. Worley, Nicholas J. Everetts, Riku Yasutomi, Nir Yosef, and Iswar K. Hariharan. Critical genetic program for drosophila imaginal disc regeneration revealed by single-cell analysis. bioRxiv, Jul 2021. URL: https://doi.org/10.1101/2021.07.08.451678, doi:10.1101/2021.07.08.451678. This article has 3 citations.

5. (worley2021criticalgeneticprogram pages 16-18): Melanie I. Worley, Nicholas J. Everetts, Riku Yasutomi, Nir Yosef, and Iswar K. Hariharan. Critical genetic program for drosophila imaginal disc regeneration revealed by single-cell analysis. bioRxiv, Jul 2021. URL: https://doi.org/10.1101/2021.07.08.451678, doi:10.1101/2021.07.08.451678. This article has 3 citations.

## Artifacts

- [Edison artifact artifact-00](rgn-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. bergmann2010apoptosisstemcells pages 5-6
2. sap2015globalquantitativeproteomics pages 5-8
3. smithbolton2016drosophilaimaginaldiscsas pages 5-6
4. worley2021criticalgeneticprogram pages 24-35
5. worley2021criticalgeneticprogram pages 16-18
6. https://doi.org/10.1002/pmic.201400308
7. https://doi.org/10.1016/j.ydbio.2008.04.004.
8. https://doi.org/10.1126/scisignal.3145re8
9. https://doi.org/10.1089/wound.2014.0547
10. https://doi.org/10.1101/2021.07.08.451678.
11. https://doi.org/10.1089/wound.2014.0547,
12. https://doi.org/10.1126/scisignal.3145re8,
13. https://doi.org/10.1002/pmic.201400308,
14. https://doi.org/10.1101/2021.07.08.451678,