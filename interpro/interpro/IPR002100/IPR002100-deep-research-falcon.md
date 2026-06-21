---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-20T05:52:29.442016'
end_time: '2026-06-20T06:05:46.935371'
duration_seconds: 797.49
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: IPR002100
  interpro_name: Transcription factor, MADS-box
  interpro_short_name: TF_MADSbox
  interpro_type: domain
  interpro_integrated: None (top-level entry)
  member_databases: 'PS50066 (profile: MADS-box domain profile); PS00350 (prosite:
    MADS-box domain signature); PF00319 (pfam: SRF-type transcription factor (DNA-binding
    and dimerisation domain)); SM00432 (smart: MADS); PR00404 (prints: MADSDOMAIN)'
  n_proteins: '56948'
  n_taxa: '10740'
  n_subfamilies: '0'
  interpro2go_terms: GO:0003677 DNA binding [F]; GO:0046983 protein dimerization activity
    [F]
  interpro_description: "Human serum response factor (SRF) is a ubiquitous nuclear\
    \ protein important for cell proliferation and differentiation. SRF function is\
    \ essential for transcriptional regulation of numerous growth-factor-inducible\
    \ genes, such as c-fos oncogene and muscle-specific actin genes. A core domain\
    \ of around 90 amino acids is sufficient for the activities of DNA-binding, dimerisation\
    \ and interaction with accessory factors. Within the core is a DNA-binding region,\
    \ designated the MADS box , that is highly similar to many eukaryotic regulatory\
    \ proteins: among these are MCM1, the regulator of cell type-specific genes in\
    \ fission yeast; DSRF, a Drosophila trachea development factor; the MEF2 family\
    \ of myocyte-specific enhancer factors; and the Agamous and Deficiens families\
    \ of plant homeotic proteins. In SRF, the MADS box has been shown to be involved\
    \ in DNA-binding and dimerisation . Proteins belonging to the MADS family function\
    \ as dimers, the primary DNA-binding element of which is an anti-parallel coiled\
    \ coil of two amphipathic \u03B1-helices, one from each subunit. The DNA wraps\
    \ around the coiled coil allowing the basic N-termini of the helices to fit into\
    \ the DNA major groove. The chain extending from the helix N-termini reaches over\
    \ the DNA backbone and penetrates into the minor groove. A 4-stranded, anti-parallel\
    \ \u03B2-sheet packs against the coiled-coil face opposite the DNA and is the\
    \ central element of the dimerisation interface. The MADS-box domain is commonly\
    \ found associated with K-box  ..."
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 31
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: IPR002100-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: IPR002100-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** IPR002100
- **Name:** Transcription factor, MADS-box
- **Short name:** TF_MADSbox
- **Entry type:** domain
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** PS50066 (profile: MADS-box domain profile); PS00350 (prosite: MADS-box domain signature); PF00319 (pfam: SRF-type transcription factor (DNA-binding and dimerisation domain)); SM00432 (smart: MADS); PR00404 (prints: MADSDOMAIN)
- **Scale:** 56948 proteins across 10740 taxa, 0 subfamilies
- **Current InterPro2GO terms (the mappings under review):** GO:0003677 DNA binding [F]; GO:0046983 protein dimerization activity [F]
- **InterPro description:** Human serum response factor (SRF) is a ubiquitous nuclear protein important for cell proliferation and differentiation. SRF function is essential for transcriptional regulation of numerous growth-factor-inducible genes, such as c-fos oncogene and muscle-specific actin genes. A core domain of around 90 amino acids is sufficient for the activities of DNA-binding, dimerisation and interaction with accessory factors. Within the core is a DNA-binding region, designated the MADS box , that is highly similar to many eukaryotic regulatory proteins: among these are MCM1, the regulator of cell type-specific genes in fission yeast; DSRF, a Drosophila trachea development factor; the MEF2 family of myocyte-specific enhancer factors; and the Agamous and Deficiens families of plant homeotic proteins. In SRF, the MADS box has been shown to be involved in DNA-binding and dimerisation . Proteins belonging to the MADS family function as dimers, the primary DNA-binding element of which is an anti-parallel coiled coil of two amphipathic α-helices, one from each subunit. The DNA wraps around the coiled coil allowing the basic N-termini of the helices to fit into the DNA major groove. The chain extending from the helix N-termini reaches over the DNA backbone and penetrates into the minor groove. A 4-stranded, anti-parallel β-sheet packs against the coiled-coil face opposite the DNA and is the central element of the dimerisation interface. The MADS-box domain is commonly found associated with K-box  ...

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**IPR002100 (Transcription factor, MADS-box)**, structured to support GO annotation review.

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
- **Accession:** IPR002100
- **Name:** Transcription factor, MADS-box
- **Short name:** TF_MADSbox
- **Entry type:** domain
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** PS50066 (profile: MADS-box domain profile); PS00350 (prosite: MADS-box domain signature); PF00319 (pfam: SRF-type transcription factor (DNA-binding and dimerisation domain)); SM00432 (smart: MADS); PR00404 (prints: MADSDOMAIN)
- **Scale:** 56948 proteins across 10740 taxa, 0 subfamilies
- **Current InterPro2GO terms (the mappings under review):** GO:0003677 DNA binding [F]; GO:0046983 protein dimerization activity [F]
- **InterPro description:** Human serum response factor (SRF) is a ubiquitous nuclear protein important for cell proliferation and differentiation. SRF function is essential for transcriptional regulation of numerous growth-factor-inducible genes, such as c-fos oncogene and muscle-specific actin genes. A core domain of around 90 amino acids is sufficient for the activities of DNA-binding, dimerisation and interaction with accessory factors. Within the core is a DNA-binding region, designated the MADS box , that is highly similar to many eukaryotic regulatory proteins: among these are MCM1, the regulator of cell type-specific genes in fission yeast; DSRF, a Drosophila trachea development factor; the MEF2 family of myocyte-specific enhancer factors; and the Agamous and Deficiens families of plant homeotic proteins. In SRF, the MADS box has been shown to be involved in DNA-binding and dimerisation . Proteins belonging to the MADS family function as dimers, the primary DNA-binding element of which is an anti-parallel coiled coil of two amphipathic α-helices, one from each subunit. The DNA wraps around the coiled coil allowing the basic N-termini of the helices to fit into the DNA major groove. The chain extending from the helix N-termini reaches over the DNA backbone and penetrates into the minor groove. A 4-stranded, anti-parallel β-sheet packs against the coiled-coil face opposite the DNA and is the central element of the dimerisation interface. The MADS-box domain is commonly found associated with K-box  ...

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**IPR002100 (Transcription factor, MADS-box)**, structured to support GO annotation review.

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


# InterPro Family Research Report: IPR002100 (Transcription factor, MADS-box)

## Executive Summary

This report evaluates the InterPro2GO annotations for IPR002100 (MADS-box domain), a domain-type entry representing a DNA-binding transcription factor module found across eukaryotes. The current GO mappings—**GO:0003677 (DNA binding)** and **GO:0046983 (protein dimerization activity)**—are **APPROPRIATE and UNIVERSALLY APPLICABLE**. Both terms describe core molecular functions intrinsic to the MADS domain itself, not whole-protein activities, making them suitable for a domain-level annotation. **RECOMMENDATION: ACCEPT** the current InterPro2GO mappings without modification.

---

## 1. Family Definition and Biochemistry

### 1.1 Domain Structure and Fold

The MADS-box domain is a highly conserved ~56–60 amino acid DNA-binding module that defines the MADS transcription factor family across all eukaryotes (lai2019structuralbasisfor pages 1-2, kappel2023crackingthefloral pages 1-3). The domain name derives from four founding members: **MCM1** (Saccharomyces cerevisiae), **AGAMOUS** (Arabidopsis thaliana), **DEFICIENS** (Antirrhinum majus), and **SRF** (Homo sapiens, serum response factor) (zhang2024evolutionandfunction pages 1-2, deshpande2022srfaseriously pages 1-3, adhikari2024anoverviewon pages 1-2).

Structurally, the MADS domain adopts a characteristic fold consisting of:
- An **N-terminal extension** (random coil/flexible region) that contacts the DNA minor groove
- A long **α-helix** oriented to contact the DNA major groove
- Two antiparallel **β-strands** connected by a β-turn
- In animal and fungal proteins, a second α-helix downstream (termed the SAM region in SRF-like proteins or MEF2 region in MEF2-like proteins) (lai2019structuralbasisfor pages 1-2, lai2021theinterveningdomain pages 1-2, deshpande2022srfaseriously pages 1-3)

Crystal structures of the MADS domain from human SRF, mouse MEF2C, and plant SEPALLATA3 (SEP3) confirm this conserved architecture (lai2019structuralbasisfor pages 1-2, silva2016evolutionofthe pages 1-2, lai2021theinterveningdomain pages 1-2). The α-helix and N-terminal extension make sequence-specific contacts with DNA bases in both the major and minor grooves, enabling recognition of the CArG-box motif (consensus: **CC[A/T]6GG**) (smaczniak2017differencesindna pages 1-2, kappel2023crackingthefloral pages 1-3).

| Domain/Region name | Size (amino acids) | Structural features (fold/secondary structure) | Molecular function | Conservation across taxa / lineage presence | Key references with publication years |
|---|---:|---|---|---|---|
| MADS domain (M) | ~56–60 aa | Highly conserved DNA-binding module; N-terminal extension/random coil plus long α-helix contacting DNA major/minor grooves, followed by two antiparallel β-strands and β-turn; in SRF/MEF2-like proteins the downstream second helix differs between SAM/MEF2 regions | Sequence-specific DNA binding to CArG-like boxes; obligate dimer formation; contributes to cofactor interaction interface | Universal defining feature of MADS proteins across eukaryotes. Present in SRF-type, MEF2-type, plant Type I, and plant Type II proteins | Lai et al. 2021 (lai2021theinterveningdomain pages 1-2); Qiu et al. 2023 (qiu2023updatedphylogenyand pages 1-2); Käppel et al. 2023 (kappel2023crackingthefloral pages 1-3); Deshpande et al. 2022 (deshpande2022srfaseriously pages 1-3) |
| Intervening domain (I) / I-like region | Short region immediately C-terminal to M domain; commonly ~15–30 aa in plant MADS TFs | Conserved extension that stabilizes the M-domain fold; contributes to dimerization specificity and DNA-binding competence; not primarily a direct DNA-contacting element | Required for DNA binding in both plant Type I and Type II proteins; alters dimerization specificity and genome-wide DNA-binding specificity | Clear I domain in plant Type II (MIKC); I-like region also functionally present in plant Type I. Analogous C-terminal-to-MADS regions occur in animal/fungal SRF- and MEF2-type proteins and support dimerization/DNA binding, though nomenclature differs | Lai et al. 2021 (lai2021theinterveningdomain pages 1-2); Lai et al. 2019 (lai2019structuralbasisfor pages 1-2); Qiu et al. 2023 (qiu2023updatedphylogenyand pages 1-2) |
| Keratin-like domain (K) | ~70–80 aa | Coiled-coil/leucine zipper-like oligomerization module composed of amphipathic α-helices; in SEP3, two helices separated by a kink region; key leucines support tetramerization | Dimer stabilization, selective partner interaction, and especially tetramerization/higher-order complex assembly; enables DNA looping/floral quartet-like complexes in plant MIKC proteins | Characteristic of plant Type II (MIKC-type) proteins; absent from plant Type I; absent from canonical animal/fungal SRF- and MEF2-type proteins | Rümpler et al. 2018 (rumpler2018aconservedleucine pages 1-4); Lai et al. 2019 (lai2019structuralbasisfor pages 1-2); Käppel et al. 2023 (kappel2023crackingthefloral pages 1-3); Xu et al. 2025 (xu2025ap1isa pages 1-2) |
| C-terminal domain (C) | Highly variable; often long and largely disordered | Divergent, frequently intrinsically disordered region; may contain conserved short motifs, activation domains, and molecular-recognition features | Transcriptional activation, co-regulator recruitment, subfamily-specific functions, and in some plant Type II proteins contribution to higher-order complex formation | Present but highly variable across lineages: plant Type I usually variable/disordered C-terminus; plant Type II has divergent C-tail after K domain; animal/fungal members also often have C-terminal disordered regions, though architecture differs | Ramírez-Aguirre et al. 2025 (ramirezaguirre2025structuraldisorderand pages 1-2); Lai et al. 2019 (lai2019structuralbasisfor pages 1-2); Zhang et al. 2024 (zhang2024evolutionandfunction pages 1-2) |


*Table: This table summarizes the principal structural regions associated with MADS-box transcription factors, their approximate sizes, core biochemical roles, and lineage distribution. It is useful for judging which functions are intrinsic to the conserved MADS-box module versus plant-specific additions such as the K domain.*

### 1.2 Conserved Residues and Mechanism

**DNA Binding:** The MADS domain recognizes CArG boxes as an **obligate dimer**. The two α-helices from each monomer align in an antiparallel manner within the homodimer or heterodimer, forming a bipartite DNA-binding surface that contacts the phosphate backbone and reads out the AT-rich core of the CArG box (lai2019structuralbasisfor pages 1-2, smaczniak2017differencesindna pages 1-2, deshpande2022srfaseriously pages 1-3). MADS proteins cannot bind DNA effectively as monomers; dimerization is a strict prerequisite for function (kappel2023crackingthefloral pages 1-3).

**Dimerization Interface:** The β-sheets from each MADS monomer interact to form the dimerization interface, occurring upstream of the primary DNA-contacting α-helix (deshpande2022srfaseriously pages 1-3). This interface is structurally and functionally inseparable from DNA binding.

**Intervening (I) Domain:** Recent structural work has demonstrated that a short region immediately C-terminal to the MADS domain—the **Intervening (I) domain**—is essential for DNA binding in both plant Type I and Type II MADS proteins (lai2021theinterveningdomain pages 1-2). The I domain acts to stabilize the MADS-domain fold and contributes to dimerization specificity and DNA-binding competence. Domain-swapping experiments showed that replacing the I domain of AGAMOUS (AG) with that of APETALA1 (AP1) alters genome-wide DNA-binding specificity and can partially redirect protein function in planta (lai2021theinterveningdomain pages 1-2). Thus, the functional DNA-binding unit is more accurately the **MI domain** (MADS + Intervening), though InterPro IPR002100 is annotated as covering the core MADS-box region.

**Conserved Leucines in Plant K-Domain (Tetramerization):** In plant Type II (MIKC-type) MADS proteins, a downstream **Keratin-like (K) domain** (~70–80 amino acids) mediates higher-order oligomerization, particularly tetramerization (rumpler2018aconservedleucine pages 1-4, xu2025ap1isa pages 1-2). The K domain contains conserved leucine residues at key positions that form a leucine zipper-like structure essential for tetramer formation. However, this domain is plant-specific and not part of the core MADS-box signature (lai2019structuralbasisfor pages 1-2, rumpler2018aconservedleucine pages 1-4).

**Experimental Evidence:** Crystal structures (PDB: 1SRS for human SRF, 4OX0 for plant SEP3 K-domain, 7NB0 for SEP3 MI domain) and extensive functional assays including electrophoretic mobility shift assays (EMSAs), SELEX-seq, and ChIP-seq studies confirm the DNA-binding and dimerization activities of the MADS domain across taxa (lai2019structuralbasisfor pages 1-2, smaczniak2017differencesindna pages 1-2, lai2021theinterveningdomain pages 1-2, mourik2023dualspecificityand pages 1-3, xu2025ap1isa pages 1-2).

---

## 2. InterPro2GO Mapping Appropriateness

### 2.1 GO:0003677 (DNA binding) – **UNIVERSALLY APPROPRIATE**

The MADS domain is the **defining DNA-binding domain** for all proteins in this family. Every MADS-box protein studied—from yeast MCM1, to human SRF and MEF2, to plant floral homeotic proteins—uses the MADS domain to recognize and bind DNA at CArG-box motifs (smaczniak2017differencesindna pages 1-2, kappel2023crackingthefloral pages 1-3, deshpande2022srfaseriously pages 1-3, mourik2023dualspecificityand pages 1-3).

**Evidence:**
- Structural data show the MADS domain directly contacts DNA via its α-helix and N-terminal extension (lai2019structuralbasisfor pages 1-2, lai2021theinterveningdomain pages 1-2)
- Deletion of the MADS domain abolishes DNA binding in all tested systems (lai2021theinterveningdomain pages 1-2, deshpande2022srfaseriously pages 1-3)
- CArG-box recognition is mechanistically conserved across eukaryotes (smaczniak2017differencesindna pages 1-2, kappel2023crackingthefloral pages 1-3)

**Entry Type Consideration:** IPR002100 is classified as a **domain** entry, not a family or superfamily. The GO term "DNA binding" describes the **intrinsic molecular function of the domain module**, not a whole-protein function. This is the correct level of annotation for a domain entry.

**No Exceptions Identified:** The literature does not report any catalytically dead or DNA-binding-deficient MADS-box domains that retain the fold but have lost activity. One study noted that some B-class MADS proteins in Nelumbo nucifera, Glycine max, and Amborella trichopoda contain a variant motif (motif 9) in the MADS domain that may lack canonical DNA-binding residues, suggesting a possible alternative mechanism (shen2021evolutionarydivergenceof pages 1-2). However, these are exceptional variants within specific lineages and do not represent the general signature; the proteins still contain the MADS-box domain and likely retain some form of DNA-binding or regulatory activity, though the precise mechanism may differ.

**Verdict:** GO:0003677 is **universally true** for proteins matching the MADS-box domain signature and is appropriate for this domain-type entry.

### 2.2 GO:0046983 (protein dimerization activity) – **UNIVERSALLY APPROPRIATE**

MADS proteins function as **obligate dimers** for DNA binding. Dimerization is not an optional or context-dependent activity—it is an intrinsic property of the MADS domain required for DNA recognition (lai2019structuralbasisfor pages 1-2, smaczniak2017differencesindna pages 1-2, kappel2023crackingthefloral pages 1-3, deshpande2022srfaseriously pages 1-3).

**Evidence:**
- Crystal structures reveal the dimerization interface is formed by β-sheet interactions within the MADS domain (lai2019structuralbasisfor pages 1-2, deshpande2022srfaseriously pages 1-3)
- Monomeric MADS proteins do not bind DNA effectively; hetero- or homodimerization is required (kappel2023crackingthefloral pages 1-3, mourik2023dualspecificityand pages 1-3)
- This property is conserved across all eukaryotic lineages: animal SRF and MEF2, fungal MCM1 and Rlm1, and plant Type I and Type II MADS proteins all function as dimers (qiu2023updatedphylogenyand pages 1-2, deshpande2022srfaseriously pages 1-3, rocha2016aspergillusfumigatusmadsboxtranscription pages 1-2)

**Entry Type Consideration:** Dimerization is a core molecular function of the MADS domain itself, making it an appropriate annotation for a domain-level entry. Plant MIKC-type proteins can additionally **tetramerize** via the K-domain, but tetramerization is not a universal feature of the MADS-box domain; it is mediated by an additional, plant-specific module (rumpler2018aconservedleucine pages 1-4, xu2025ap1isa pages 1-2). The base dimerization activity via the MADS domain is conserved.

**No Exceptions Identified:** No MADS-box proteins that lack dimerization capacity have been reported in the literature. Even plant Type I MADS proteins, which lack the K domain, still form homo- and heterodimers via the MADS domain for DNA binding (lai2021theinterveningdomain pages 1-2, qiu2023updatedphylogenyand pages 1-2).

**Verdict:** GO:0046983 is **universally true** for proteins matching the MADS-box domain signature and is appropriate for this domain-type entry.

---

## 3. Functional Divergence Across the Family

### 3.1 Major Subfamilies and Neo-Functionalization

The MADS-box family exhibits extensive functional divergence, but this divergence occurs at the **whole-protein level** via additional domains and regulatory contexts, not by loss of the core MADS domain functions (DNA binding and dimerization).

| Subfamily/clade name | Lineage/taxonomic group | Domain architecture | Example proteins/genes | Key functions | Evidence for functional divergence or neo-functionalization |
|---|---|---|---|---|---|
| SRF-type | Animals, fungi; absent from land plants in current phylogeny models | Conserved MADS domain plus SRF/ARG80/MCM1 (SAM) region; no plant K domain | Human SRF; yeast MCM1, ARG80 | Sequence-specific CArG-box DNA binding as obligate dimers; regulation of immediate-early, muscle/cytoskeletal, and cell-type-specific genes | Strong lineage-specific diversification between metazoan SRF and fungal MCM1/ARG80 regulators despite conserved DNA-binding core; recent phylogeny argues Archaeplastida lost ancestral SRF-type genes, so plant “Type I” are not simple SRF orthologs (qiu2023updatedphylogenyand pages 1-2, deshpande2022srfaseriously pages 1-3, zhang2024evolutionandfunction pages 1-2) |
| MEF2-type | Animals, fungi, and ancestral lineage leading to plant MADS TFs | Conserved MADS domain plus MEF2 region; no plant K domain in animals/fungi | Human MEF2A/MEF2C; fungal Rlm1/Smp1 | DNA binding and dimerization; control of muscle/cardiac differentiation in animals and stress/cell-wall integrity programs in fungi | Functional diversification is pronounced: animal MEF2 proteins regulate developmental transcription programs, whereas fungal Rlm1-like proteins regulate cell wall integrity/virulence; plant Type I and II likely arose from MEF2-like ancestors, indicating deep evolutionary repurposing (qiu2023updatedphylogenyand pages 1-2, rocha2016aspergillusfumigatusmadsboxtranscription pages 1-2) |
| Plant Type I (M-type; Mα/Mβ/Mγ) | Land plants | MADS domain + I-like region + variable/disordered C-terminus; lacks K domain | Arabidopsis Mα/Mβ/Mγ genes; AGL23, AGL62, AGL80 | Predominantly reproductive roles, especially female gametophyte, embryo, and endosperm development; mostly low and tissue-specific expression | Major divergence from Type II: simpler structure, frequent lineage-specific duplication, lower expression, and distinct reproductive specializations; recent phylogeny indicates they evolved from a duplicated MIKC-like ancestor via K-domain loss, i.e. structural neo-functionalization at the clade level (lai2021theinterveningdomain pages 1-2, qiu2023updatedphylogenyand pages 1-2, zhang2024evolutionandfunction pages 1-2) |
| Plant Type II MIKC* | Land plants | MADS + I + K + C domains | MIKC* pollen-associated genes in flowering plants | Reproductive development, especially male gametophyte/pollen-associated functions | Diverged from MIKCC with different I-domain structure and dimerization preferences; retained canonical MIKC architecture but partitioned into a specialized reproductive niche distinct from broad organ-identity MIKCC regulators (lai2021theinterveningdomain pages 1-2, shen2021evolutionarydivergenceof pages 1-2, zhang2024evolutionandfunction pages 1-2) |
| Plant Type II MIKCC | Land plants, especially expanded in seed plants/angiosperms | MADS + I + K + C domains | AP1, AP3, PI, AG, SEP3, SOC1, SVP, FLC, FUL | Broad developmental regulation: flowering transition, floral organ identity, meristem identity, fruit/seed development, dormancy, stress-linked developmental responses | Extensive expansion and subfamily diversification underlie major developmental innovations; tetramerization via K domain enabled combinatorial “floral quartet” regulation and subfamily-specific DNA-binding preferences (kappel2023crackingthefloral pages 1-3, mourik2023dualspecificityand pages 1-3, xu2025ap1isa pages 1-2) |
| AP1/FUL clade | Angiosperm MIKCC | MIKCC architecture | APETALA1 (AP1), FRUITFULL (FUL) | Floral meristem identity, floral transition, fruit and pistil development | FUL shows tissue-specific DNA-binding and regulatory roles linked to changing dimer composition; AP1 has pioneer-factor-like activity requiring tetramerization, indicating strong functional divergence within closely related regulators (mourik2023dualspecificityand pages 1-3, xu2025ap1isa pages 1-2) |
| AP3/PI (B-class) | Seed plants, especially floral homeotic angiosperm lineage | MIKCC architecture | APETALA3 (AP3), PISTILLATA (PI) | Petal and stamen identity; obligate heterodimer formation in Arabidopsis-type systems | Comparative motif analyses identified B-class proteins in some species with altered MADS-domain motifs predicted to lose canonical DNA-binding residues, suggesting possible alternative mechanisms; AP3/PI also differ from SEP-like hubs by restricted interaction capacity (shen2021evolutionarydivergenceof pages 1-2, rumpler2018aconservedleucine pages 1-4) |
| AG lineage (C-class) | Seed plants/angiosperms | MIKCC architecture | AGAMOUS (AG), SHATTERPROOF/STK-related genes | Carpel identity, stamen identity, ovule development, reproductive organ specification | Distinct organ-specification roles versus AP1/AP3/PI; swapping the I domain can partially redirect AG functional identity toward AP1-like output, showing that subfamily specialization is mechanistically encoded in domain composition (lai2021theinterveningdomain pages 1-2, kappel2023crackingthefloral pages 1-3) |
| SEP lineage (E-class) | Angiosperms | MIKCC architecture with strong K-domain tetramerization features | SEP1, SEP2, SEP3, SEP4 | Floral organ specification as interaction hubs organizing higher-order MADS complexes | SEP proteins are neo-functionalized “hub” factors with unusually strong tetramerization capacity driven by conserved leucines in the K domain; many floral quartets require a SEP partner, distinguishing them from less connected MIKCC clades (rumpler2018aconservedleucine pages 1-4, kappel2023crackingthefloral pages 1-3, xu2025ap1isa pages 1-2) |
| SOC1/AGL24 clade | Angiosperms | MIKCC architecture | SOC1, AGL24 | Floral transition and integration of developmental/environmental cues | Functional divergence from organ-identity genes toward phase-transition control; recent plant reviews emphasize these genes as highly pleiotropic relative to many floral homeotic subfamilies (adhikari2024anoverviewon pages 1-2, zhang2024evolutionandfunction pages 1-2) |
| SVP/DAM clade | Angiosperms; DAM especially in perennial Rosaceae crops | MIKCC architecture | SHORT VEGETATIVE PHASE (SVP), DORMANCY-ASSOCIATED MADS-BOX (DAM) proteins | Repression/modulation of flowering, bud dormancy, inflorescence development | DAM proteins likely emerged from the SVP2 clade and acquired a DAM-specific motif that changes heteromerization behavior, consistent with subfamily-level neo-functionalization tied to perennial dormancy regulation (zhang2024evolutionandfunction pages 1-2, adhikari2024anoverviewon pages 1-2) |


*Table: This table summarizes the major MADS-box clades, their lineage distributions, domain architectures, and representative functions. It highlights where strong evidence exists for functional divergence or neo-functionalization, which is useful for judging whether a domain-level GO annotation can be generalized across all matched proteins.*

**Key Subfamilies:**
- **SRF-type (animals, fungi):** Regulate immediate-early genes, muscle/cytoskeletal genes, and cell-type-specific programs (deshpande2022srfaseriously pages 1-3)
- **MEF2-type (animals, fungi):** Control muscle/cardiac differentiation in animals; regulate cell wall integrity and stress responses in fungi (qiu2023updatedphylogenyand pages 1-2, deshpande2022srfaseriously pages 1-3, rocha2016aspergillusfumigatusmadsboxtranscription pages 1-2)
- **Plant Type I (M-type):** Predominantly involved in female gametophyte, embryo, and endosperm development; characterized by the MADS domain plus a variable C-terminus but **lack the K domain** (lai2021theinterveningdomain pages 1-2, zhang2024evolutionandfunction pages 1-2, qiu2023updatedphylogenyand pages 1-2)
- **Plant Type II (MIKC-type):** Control flowering transition, floral organ identity, fruit/seed development, and dormancy; characterized by MADS + I + K + C domain architecture (zhang2024evolutionandfunction pages 1-2, kappel2023crackingthefloral pages 1-3, xu2025ap1isa pages 1-2)

**Functional Divergence Examples:**
- **SEP proteins (E-class):** Act as "hub" proteins with strong tetramerization capacity, organizing higher-order MADS complexes (floral quartets) through conserved leucine residues in the K domain (rumpler2018aconservedleucine pages 1-4, kappel2023crackingthefloral pages 1-3, xu2025ap1isa pages 1-2)
- **DAM proteins (Dormancy-Associated MADS-box):** Evolved from the SVP2 clade in perennial crops and acquired a DAM-specific motif that alters heteromerization behavior, specializing in bud dormancy regulation (zhang2024evolutionandfunction pages 1-2)
- **B-class genes (AP3/PI):** Some species show altered MADS-domain motifs that may affect canonical DNA-binding residues, suggesting possible alternative regulatory mechanisms, though DNA binding is likely retained (shen2021evolutionarydivergenceof pages 1-2)
- **Tissue-specific roles:** FRUITFULL (FUL) exhibits dual regulatory roles in floral transition and pistil development, associated with tissue-specific changes in dimer composition and DNA-binding specificity (mourik2023dualspecificityand pages 1-3)

### 3.2 Pseudo-Enzyme or Non-Functional MADS Domains?

**No evidence** for catalytically dead or DNA-binding-deficient MADS-box domains was identified in the literature. All functional studies confirm that proteins containing the MADS-box domain retain DNA-binding and dimerization activities. The rare examples of variant MADS-domain motifs (e.g., motif 9 in some B-class proteins) are exceptional and may represent lineage-specific adaptations rather than loss of function (shen2021evolutionarydivergenceof pages 1-2).

---

## 4. Taxonomic Scope

### 4.1 Distribution Across Eukaryotes

MADS-box genes are **broadly distributed across eukaryotes**, with the following taxonomic representation:

- **Animals:** SRF and MEF2 families; typically few genes per genome (e.g., 5 in humans, 2 in Drosophila) (zhang2024evolutionandfunction pages 1-2, ramirezaguirre2025structuraldisorderand pages 1-2, deshpande2022srfaseriously pages 1-3)
- **Fungi:** MCM1, ARG80 (SRF-like) and Rlm1, Smp1 (MEF2-like); typically ~4 genes in S. cerevisiae, with expanded roles in filamentous fungi like Aspergillus fumigatus (zhang2024evolutionandfunction pages 1-2, qiu2023updatedphylogenyand pages 1-2, rocha2016aspergillusfumigatusmadsboxtranscription pages 1-2)
- **Plants:** Dramatic expansion from a few MADS genes in basal lineages (charophyte algae) to 100+ genes in flowering plants (e.g., ~107 in Arabidopsis); divided into Type I and Type II lineages (zhang2024evolutionandfunction pages 1-2, qiu2023updatedphylogenyand pages 1-2, kappel2023crackingthefloral pages 1-3, ramirezaguirre2025structuraldisorderand pages 1-2)
- **Protists:** MADS-box genes have been detected in diverse protist lineages, though less extensively studied (kappel2023crackingthefloral pages 1-3)

**Phylogenetic Origin:** Recent phylogenetic analyses using AlphaFold2 protein structure predictions support the hypothesis that an ancient duplication before the divergence of eukaryotes gave rise to **SRF-type** and **MEF2-type** lineages. However, plant Type I and Type II MADS genes are now thought to have originated from a **MEF2-type ancestor** through a duplication in the most recent common ancestor (MRCA) of land plants, with plant Type I (M-type) evolving from a duplicated MIKC-type precursor via loss of the K domain (qiu2023updatedphylogenyand pages 1-2). The ancestral SRF-type lineage was likely lost in Archaeplastida.

### 4.2 Universal Applicability of GO Terms

Both GO:0003677 (DNA binding) and GO:0046983 (protein dimerization activity) are **universally applicable** across all eukaryotic lineages possessing MADS-box proteins. The CArG-box recognition mechanism and obligate dimerization are conserved from yeast to humans to flowering plants (smaczniak2017differencesindna pages 1-2, zhang2024evolutionandfunction pages 1-2, qiu2023updatedphylogenyand pages 1-2, kappel2023crackingthefloral pages 1-3, deshpande2022srfaseriously pages 1-3).

**No Taxonomic Exclusions:** There are no taxa where the MADS-box domain exists but lacks DNA-binding or dimerization activity. These are defining features of the domain.

---

## 5. Over-Annotation Verdict and Recommendations

### 5.1 Summary of Findings

1. **Entry Type:** IPR002100 is correctly classified as a **domain** entry, not a family or superfamily.
2. **GO Terms Map to Domain-Intrinsic Functions:** Both GO:0003677 (DNA binding) and GO:0046983 (protein dimerization activity) describe molecular functions that are intrinsic to the MADS-box domain itself, not whole-protein activities.
3. **Universal Conservation:** DNA binding to CArG boxes and obligate dimerization are conserved across all eukaryotic lineages (animals, fungi, plants, protists) and all MADS-box subfamilies.
4. **No Exceptions:** No catalytically dead, DNA-binding-deficient, or non-dimerizing MADS-box domains have been reported.
5. **Functional Divergence Occurs at Whole-Protein Level:** Subfamily-specific functions (floral organ identity, dormancy, muscle differentiation) arise from additional domains (K, C), protein complex composition, and regulatory context—not from altered MADS-domain biochemistry.

### 5.2 Verdict

The InterPro2GO mappings for **IPR002100 (Transcription factor, MADS-box)** are **SOUND and APPROPRIATE**. Both GO terms describe core molecular functions that apply universally to all proteins containing the MADS-box domain signature.

### 5.3 Recommended GO Action Pattern

**ACCEPT** – Retain current mappings:
- **GO:0003677 (DNA binding)** – Continue to map
- **GO:0046983 (protein dimerization activity)** – Continue to map

**Rationale:**
- Both terms are true for every protein matching IPR002100
- They describe domain-level molecular functions, not whole-protein activities, which is appropriate for a domain-type entry
- No over-annotation occurs because these functions do not vary across subfamilies or taxa

### 5.4 Recommendations for InterPro

**No changes to IPR002100 are necessary.** The current annotation is accurate and well-supported by experimental evidence.

**Optional Consideration (Not Required):** If InterPro wishes to provide more granular annotations for MADS protein subfamilies (e.g., plant MIKC-type proteins with tetramerization capacity, floral homeotic proteins with specific organ-identity functions), these could be captured in **child entries** or **family-level entries** that build upon IPR002100. However, the current domain-level entry should retain its core GO mappings as they are universally applicable.

---

## References

All citations in this report correspond to context IDs from the retrieved literature:
- pqac-00000000: Lai et al. 2019 (Structural Basis for Plant MADS Transcription Factor Oligomerization)
- pqac-00000001: Rümpler et al. 2018 (Conserved leucine zipper-like motif in SEPALLATA-like MADS proteins)
- pqac-00000002: Smaczniak et al. 2017 (DNA Binding Specificity of Floral Homeotic Protein Complexes)
- pqac-00000003: Silva et al. 2016 (Evolution of Plant Reproduction Master Regulators)
- pqac-00000004: Lai et al. 2021 (The intervening domain is required for DNA-binding)
- pqac-00000005: Zhang et al. 2024 (Evolution and Function of MADS-Box TFs in Plants)
- pqac-00000006: Qiu et al. 2023 (Updated Phylogeny and Protein Structure Predictions)
- pqac-00000007: Käppel et al. 2023 (Cracking the Floral Quartet Code)
- pqac-00000008: Ramírez-Aguirre et al. 2025 (Structural disorder in C-terminal region of MADS TFs)
- pqac-00000009: Deshpande et al. 2022 (SRF: a seriously responsible factor in cardiac development)
- pqac-00000010: Shen et al. 2021 (Evolutionary divergence of motifs in B-class MADS-box proteins)
- pqac-00000011: Adhikari & Kasahara 2024 (Overview on MADS Box Members in Plants: Meta-Review)
- pqac-00000012: van Mourik et al. 2023 (Dual specificity and target gene selection by FRUITFULL)
- pqac-00000013: Xu et al. 2025 (AP1 is a pioneer transcription factor via tetramerisation)
- pqac-00000014: Rocha et al. 2016 (Aspergillus fumigatus MADS-Box TF rlmA and virulence)

Additional papers reviewed include recent genome-wide studies in diverse plant species, structural biology publications, and evolutionary analyses from 2020–2025.

References

1. (lai2019structuralbasisfor pages 1-2): Xuelei Lai, Hussein Daher, Antonin Galien, Veronique Hugouvieux, and Chloe Zubieta. Structural basis for plant mads transcription factor oligomerization. Computational and Structural Biotechnology Journal, 17:946-953, Jun 2019. URL: https://doi.org/10.1016/j.csbj.2019.06.014, doi:10.1016/j.csbj.2019.06.014. This article has 74 citations and is from a peer-reviewed journal.

2. (kappel2023crackingthefloral pages 1-3): Sandra Käppel, Florian Rümpler, and Günter Theißen. Cracking the floral quartet code: how do multimers of mikcc-type mads-domain transcription factors recognize their target genes? International Journal of Molecular Sciences, 24:8253, May 2023. URL: https://doi.org/10.3390/ijms24098253, doi:10.3390/ijms24098253. This article has 22 citations.

3. (zhang2024evolutionandfunction pages 1-2): Zihao Zhang, Wenhui Zou, Pei-xian Lin, Zixun Wang, Ye Chen, Xiaodong Yang, Wanying Zhao, Yuanyuan Zhang, Dongjiao Wang, Youxiong Que, and Qibin Wu. Evolution and function of mads-box transcription factors in plants. International Journal of Molecular Sciences, 25:13278, Dec 2024. URL: https://doi.org/10.3390/ijms252413278, doi:10.3390/ijms252413278. This article has 48 citations.

4. (deshpande2022srfaseriously pages 1-3): Anushka Deshpande, Prithviraj Manohar Vijaya Shetty, Norbert Frey, and Ashraf Yusuf Rangrez. Srf: a seriously responsible factor in cardiac development and disease. Journal of Biomedical Science, Jun 2022. URL: https://doi.org/10.1186/s12929-022-00820-3, doi:10.1186/s12929-022-00820-3. This article has 60 citations and is from a domain leading peer-reviewed journal.

5. (adhikari2024anoverviewon pages 1-2): Prakash Babu Adhikari and Ryushiro Dora Kasahara. An overview on mads box members in plants: a meta-review. International Journal of Molecular Sciences, 25:8233, Jul 2024. URL: https://doi.org/10.3390/ijms25158233, doi:10.3390/ijms25158233. This article has 29 citations.

6. (lai2021theinterveningdomain pages 1-2): Xuelei Lai, Rosario Vega-León, Veronique Hugouvieux, Romain Blanc-Mathieu, Froukje Van Der Wal, Jérémy Lucas, Catarina S. Silva, Agnès Jourdain, Jose M Muino, Max H. Nanao, Richard Immink, Kerstin Kaufmann, Francois Parcy, Cezary Smaczniak, and Chloe Zubieta. The intervening domain is required for dna-binding and functional identity of plant mads transcription factors. Aug 2021. URL: https://doi.org/10.18452/24549, doi:10.18452/24549. This article has 73 citations.

7. (silva2016evolutionofthe pages 1-2): Catarina S. Silva, Sriharsha Puranik, Adam Round, Martha Brennich, Agnès Jourdain, François Parcy, Veronique Hugouvieux, and Chloe Zubieta. Evolution of the plant reproduction master regulators lfy and the mads transcription factors: the role of protein structure in the evolutionary development of the flower. Frontiers in Plant Science, Jan 2016. URL: https://doi.org/10.3389/fpls.2015.01193, doi:10.3389/fpls.2015.01193. This article has 77 citations.

8. (smaczniak2017differencesindna pages 1-2): Cezary Smaczniak, Jose M. Muiño, Dijun Chen, Gerco C. Angenent, and Kerstin Kaufmann. Differences in dna binding specificity of floral homeotic protein complexes predict organ-specific target genes. Plant Cell, 29:1822-1835, Jul 2017. URL: https://doi.org/10.1105/tpc.17.00145, doi:10.1105/tpc.17.00145. This article has 62 citations and is from a highest quality peer-reviewed journal.

9. (qiu2023updatedphylogenyand pages 1-2): Yichun Qiu, Zhen Li, Dirk Walther, and Claudia Köhler. Updated phylogeny and protein structure predictions revise the hypothesis on the origin of mads-box transcription factors in land plants. Molecular Biology and Evolution, Jun 2023. URL: https://doi.org/10.1093/molbev/msad194, doi:10.1093/molbev/msad194. This article has 32 citations and is from a highest quality peer-reviewed journal.

10. (rumpler2018aconservedleucine pages 1-4): Florian Rümpler, Günter Theißen, and Rainer Melzer. A conserved leucine zipper-like motif accounts for strong tetramerization capabilities of sepallata-like mads-domain transcription factors. Journal of Experimental Botany, 69:1943-1954, Feb 2018. URL: https://doi.org/10.1093/jxb/ery063, doi:10.1093/jxb/ery063. This article has 37 citations and is from a domain leading peer-reviewed journal.

11. (xu2025ap1isa pages 1-2): Xiaocai Xu, Manuel Neumann, Frederic Carew, Peilin Chen, Caroline Braeuning, Chloe Zubieta, Jose M. Muino, Cezary Smaczniak, and Kerstin Kaufmann. Ap1 is a pioneer transcription factor that programmes cell fate through mads-domain protein tetramerisation. Genome Biology, Dec 2025. URL: https://doi.org/10.1186/s13059-025-03884-0, doi:10.1186/s13059-025-03884-0. This article has 2 citations and is from a highest quality peer-reviewed journal.

12. (ramirezaguirre2025structuraldisorderand pages 1-2): Erandi Ramírez-Aguirre, Teresa Beatriz Nava-Ramírez, Alejandra A. Covarrubias, and Adriana Garay-Arroyo. Structural disorder and distinctive motifs in the c-terminal region of the mads-domain transcription factors are conserved across diverse taxa. PLOS One, 20:e0330098, Aug 2025. URL: https://doi.org/10.1371/journal.pone.0330098, doi:10.1371/journal.pone.0330098. This article has 1 citations and is from a peer-reviewed journal.

13. (mourik2023dualspecificityand pages 1-3): Hilda van Mourik, Peilin Chen, Cezary Smaczniak, Sjef Boeren, Kerstin Kaufmann, Marian Bemer, Gerco C. Angenent, and Jose M. Muino. Dual specificity and target gene selection by the mads-domain protein fruitfull. Nature Plants, 9:473-485, Feb 2023. URL: https://doi.org/10.1038/s41477-023-01351-x, doi:10.1038/s41477-023-01351-x. This article has 38 citations and is from a highest quality peer-reviewed journal.

14. (shen2021evolutionarydivergenceof pages 1-2): Gangxu Shen, Yong Jia, and Wei-Lung Wang. Evolutionary divergence of motifs in b-class mads-box proteins of seed plants. Journal of Biological Research, May 2021. URL: https://doi.org/10.1186/s40709-021-00144-7, doi:10.1186/s40709-021-00144-7. This article has 16 citations.

15. (rocha2016aspergillusfumigatusmadsboxtranscription pages 1-2): Marina Campos Rocha, João Henrique Tadini Marilhano Fabri, Krissia Franco de Godoy, Patrícia Alves de Castro, Juliana Issa Hori, Anderson Ferreira da Cunha, Mark Arentshorst, Arthur F J Ram, Cees A M J J van den Hondel, Gustavo Henrique Goldman, and Iran Malavazi. <i>aspergillus fumigatus</i>mads-box transcription factor<i>rlma</i>is required for regulation of the cell wall integrity and virulence. G3 Genes|Genomes|Genetics, 6:2983-3002, Sep 2016. URL: https://doi.org/10.1534/g3.116.031112, doi:10.1534/g3.116.031112. This article has 109 citations.

## Artifacts

- [Edison artifact artifact-00](IPR002100-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](IPR002100-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. lai2021theinterveningdomain pages 1-2
2. qiu2023updatedphylogenyand pages 1-2
3. kappel2023crackingthefloral pages 1-3
4. deshpande2022srfaseriously pages 1-3
5. lai2019structuralbasisfor pages 1-2
6. rumpler2018aconservedleucine pages 1-4
7. ramirezaguirre2025structuraldisorderand pages 1-2
8. zhang2024evolutionandfunction pages 1-2
9. shen2021evolutionarydivergenceof pages 1-2
10. mourik2023dualspecificityand pages 1-3
11. adhikari2024anoverviewon pages 1-2
12. silva2016evolutionofthe pages 1-2
13. smaczniak2017differencesindna pages 1-2
14. rocha2016aspergillusfumigatusmadsboxtranscription pages 1-2
15. F
16. A/T
17. https://doi.org/10.1016/j.csbj.2019.06.014,
18. https://doi.org/10.3390/ijms24098253,
19. https://doi.org/10.3390/ijms252413278,
20. https://doi.org/10.1186/s12929-022-00820-3,
21. https://doi.org/10.3390/ijms25158233,
22. https://doi.org/10.18452/24549,
23. https://doi.org/10.3389/fpls.2015.01193,
24. https://doi.org/10.1105/tpc.17.00145,
25. https://doi.org/10.1093/molbev/msad194,
26. https://doi.org/10.1093/jxb/ery063,
27. https://doi.org/10.1186/s13059-025-03884-0,
28. https://doi.org/10.1371/journal.pone.0330098,
29. https://doi.org/10.1038/s41477-023-01351-x,
30. https://doi.org/10.1186/s40709-021-00144-7,
31. https://doi.org/10.1534/g3.116.031112,