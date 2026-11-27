---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-25T00:05:23.825846'
end_time: '2026-09-25T00:22:00.340730'
duration_seconds: 996.51
template_file: templates/module_research.md.j2
template_variables:
  module_title: Kit signaling pathway module
  module_summary: Stem cell factor (KIT ligand) binds and dimerizes the class III
    receptor tyrosine kinase KIT, whose autophosphorylated intracellular tyrosines
    recruit SH2-domain effectors (GRB2, PI3K p85, SHP2, Src-family kinases) that drive
    Ras-MAPK, PI3K-AKT, and STAT5 outputs controlling survival, proliferation, and
    migration of hematopoietic progenitors, mast cells, melanocytes, germ cells, and
    interstitial cells of Cajal.
  module_outline: "- Kit signaling pathway\n  - 1. scf ligand-receptor engagement\n\
    \  - SCF engages KIT\n    - SCF ligand (molecular player: KITLG; activity or role:\
    \ stem cell factor receptor binding)\n    - KIT receptor (molecular player: KIT\
    \ receptor family/ortholog group; activity or role: stem cell factor receptor\
    \ activity)\n  - 2. phosphotyrosine effector recruitment\n  - KIT phosphotyrosine\
    \ effector recruitment\n    - GRB2 adaptor (molecular player: GRB2 adaptor family/ortholog\
    \ group; activity or role: phosphotyrosine residue binding)\n    - PI3K p85 adaptor\
    \ (molecular player: PI3K p85 adaptor family/ortholog group; activity or role:\
    \ 1-phosphatidylinositol-3-kinase regulator activity)\n    - SHP2 phosphatase\
    \ (molecular player: SHP2 (PTPN11) phosphatase family/ortholog group; activity\
    \ or role: non-membrane spanning protein tyrosine phosphatase activity)\n    -\
    \ Src-family kinase (molecular player: Src-family tyrosine kinase family/ortholog\
    \ group; activity or role: non-membrane spanning protein tyrosine kinase activity)\n\
    \  - 3. ras-mapk, pi3k-akt, and stat output\n  - Ras-MAPK, PI3K-AKT, and STAT5\
    \ output\n    - SOS Ras GEF (molecular player: SOS Ras guanine nucleotide exchange\
    \ factor family/ortholog group; activity or role: guanyl-nucleotide exchange factor\
    \ activity)\n    - PI3K catalytic subunit (molecular player: PI3K catalytic subunit\
    \ family/ortholog group; activity or role: 1-phosphatidylinositol-4,5-bisphosphate\
    \ 3-kinase activity)\n    - STAT5 transcription factor (molecular player: STAT\
    \ transcription factor family/ortholog group; activity or role: DNA-binding transcription\
    \ factor activity, RNA polymerase II-specific)"
  module_connections: '- SCF engages KIT causes KIT phosphotyrosine effector recruitment:
    Ligand-driven dimerization and autophosphorylation create the phosphotyrosine
    docking sites that recruit SH2 effectors.

    - KIT phosphotyrosine effector recruitment causes Ras-MAPK, PI3K-AKT, and STAT5
    output: Receptor-bound GRB2, p85, SHP2, and Src-family kinases activate the Ras-MAPK,
    PI3K-AKT, and STAT5 branches.'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 46
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: kit_signaling-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Commissioned Review Brief

## Review Topic

Kit signaling pathway module

## Working Scope

Stem cell factor (KIT ligand) binds and dimerizes the class III receptor tyrosine kinase KIT, whose autophosphorylated intracellular tyrosines recruit SH2-domain effectors (GRB2, PI3K p85, SHP2, Src-family kinases) that drive Ras-MAPK, PI3K-AKT, and STAT5 outputs controlling survival, proliferation, and migration of hematopoietic progenitors, mast cells, melanocytes, germ cells, and interstitial cells of Cajal.

## Provisional Biological Outline

- Kit signaling pathway
  - 1. scf ligand-receptor engagement
  - SCF engages KIT
    - SCF ligand (molecular player: KITLG; activity or role: stem cell factor receptor binding)
    - KIT receptor (molecular player: KIT receptor family/ortholog group; activity or role: stem cell factor receptor activity)
  - 2. phosphotyrosine effector recruitment
  - KIT phosphotyrosine effector recruitment
    - GRB2 adaptor (molecular player: GRB2 adaptor family/ortholog group; activity or role: phosphotyrosine residue binding)
    - PI3K p85 adaptor (molecular player: PI3K p85 adaptor family/ortholog group; activity or role: 1-phosphatidylinositol-3-kinase regulator activity)
    - SHP2 phosphatase (molecular player: SHP2 (PTPN11) phosphatase family/ortholog group; activity or role: non-membrane spanning protein tyrosine phosphatase activity)
    - Src-family kinase (molecular player: Src-family tyrosine kinase family/ortholog group; activity or role: non-membrane spanning protein tyrosine kinase activity)
  - 3. ras-mapk, pi3k-akt, and stat output
  - Ras-MAPK, PI3K-AKT, and STAT5 output
    - SOS Ras GEF (molecular player: SOS Ras guanine nucleotide exchange factor family/ortholog group; activity or role: guanyl-nucleotide exchange factor activity)
    - PI3K catalytic subunit (molecular player: PI3K catalytic subunit family/ortholog group; activity or role: 1-phosphatidylinositol-4,5-bisphosphate 3-kinase activity)
    - STAT5 transcription factor (molecular player: STAT transcription factor family/ortholog group; activity or role: DNA-binding transcription factor activity, RNA polymerase II-specific)

## Known Relationships Among Steps

- SCF engages KIT causes KIT phosphotyrosine effector recruitment: Ligand-driven dimerization and autophosphorylation create the phosphotyrosine docking sites that recruit SH2 effectors.
- KIT phosphotyrosine effector recruitment causes Ras-MAPK, PI3K-AKT, and STAT5 output: Receptor-bound GRB2, p85, SHP2, and Src-family kinases activate the Ras-MAPK, PI3K-AKT, and STAT5 branches.

## Assignment

Write a rigorous, review-style synthesis suitable for a molecular biology
audience. Treat the topic as a biological system whose boundaries, core
mechanisms, variants, and unresolved points should be made clear to readers who
know the field but are not specialists in this specific process.

The review should be explanatory rather than encyclopedic. Anchor broad claims
in primary literature or authoritative reviews, but keep the focus on how the
system works and how its parts fit together.

## Questions To Address

1. **Scope and boundaries**
   - What exactly is included in this biological system?
   - Which neighboring pathways, organelle processes, complexes, or regulatory
     events are often confused with it but should be treated separately?
   - Are there competing definitions in the literature?

2. **Core mechanism**
   - What is the best current model for the sequence of events?
   - Which steps are obligatory, which are conditional, and which are accessory?
   - What molecular assemblies, enzymes, receptors, adaptors, transporters, or
     structural units carry out each major step?

3. **Variation**
   - How does the system vary across major evolutionary lineages?
   - Are there well-supported differences between cell types, tissues,
     developmental stages, physiological states, or compartments?
   - Where are there alternative routes that achieve a similar outcome by
     different molecular means?

4. **Conservation and origin**
   - What is the deepest plausible evolutionary origin of the system?
   - Which parts appear ancient and conserved, and which appear to be later
     elaborations, replacements, or lineage-specific losses?
   - When a protein family has expanded, which family members are the best
     representatives for understanding the ancestral role?

5. **Physical and biological constraints**
   - What steps must occur in a particular order?
   - Which events are mutually exclusive, compartment-specific, cell-type
     specific, substrate-specific, or stage-specific?
   - What evidence rules out otherwise plausible paths through the system?

6. **Evidence and controversy**
   - Which mechanistic claims are strongly supported by experiments?
   - Where does the literature disagree, rely on indirect evidence, or mix data
     from organisms that may not be comparable?
   - What are the most important open questions?

## Output Format

Use the style and structure of a concise review article:

1. Executive summary
2. Definition and biological boundaries
3. Mechanistic overview
4. Major molecular players and active assemblies
5. Evolutionary and cell-biological variation
6. Constraints, dependencies, and failure modes
7. Controversies and open questions
8. Key references

Include citations for major claims, preferably PMIDs or DOIs. Be explicit about
uncertainty and avoid overgeneralizing from one organism, cell type, or assay
system to all biology.

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

# Commissioned Review Brief

## Review Topic

Kit signaling pathway module

## Working Scope

Stem cell factor (KIT ligand) binds and dimerizes the class III receptor tyrosine kinase KIT, whose autophosphorylated intracellular tyrosines recruit SH2-domain effectors (GRB2, PI3K p85, SHP2, Src-family kinases) that drive Ras-MAPK, PI3K-AKT, and STAT5 outputs controlling survival, proliferation, and migration of hematopoietic progenitors, mast cells, melanocytes, germ cells, and interstitial cells of Cajal.

## Provisional Biological Outline

- Kit signaling pathway
  - 1. scf ligand-receptor engagement
  - SCF engages KIT
    - SCF ligand (molecular player: KITLG; activity or role: stem cell factor receptor binding)
    - KIT receptor (molecular player: KIT receptor family/ortholog group; activity or role: stem cell factor receptor activity)
  - 2. phosphotyrosine effector recruitment
  - KIT phosphotyrosine effector recruitment
    - GRB2 adaptor (molecular player: GRB2 adaptor family/ortholog group; activity or role: phosphotyrosine residue binding)
    - PI3K p85 adaptor (molecular player: PI3K p85 adaptor family/ortholog group; activity or role: 1-phosphatidylinositol-3-kinase regulator activity)
    - SHP2 phosphatase (molecular player: SHP2 (PTPN11) phosphatase family/ortholog group; activity or role: non-membrane spanning protein tyrosine phosphatase activity)
    - Src-family kinase (molecular player: Src-family tyrosine kinase family/ortholog group; activity or role: non-membrane spanning protein tyrosine kinase activity)
  - 3. ras-mapk, pi3k-akt, and stat output
  - Ras-MAPK, PI3K-AKT, and STAT5 output
    - SOS Ras GEF (molecular player: SOS Ras guanine nucleotide exchange factor family/ortholog group; activity or role: guanyl-nucleotide exchange factor activity)
    - PI3K catalytic subunit (molecular player: PI3K catalytic subunit family/ortholog group; activity or role: 1-phosphatidylinositol-4,5-bisphosphate 3-kinase activity)
    - STAT5 transcription factor (molecular player: STAT transcription factor family/ortholog group; activity or role: DNA-binding transcription factor activity, RNA polymerase II-specific)

## Known Relationships Among Steps

- SCF engages KIT causes KIT phosphotyrosine effector recruitment: Ligand-driven dimerization and autophosphorylation create the phosphotyrosine docking sites that recruit SH2 effectors.
- KIT phosphotyrosine effector recruitment causes Ras-MAPK, PI3K-AKT, and STAT5 output: Receptor-bound GRB2, p85, SHP2, and Src-family kinases activate the Ras-MAPK, PI3K-AKT, and STAT5 branches.

## Assignment

Write a rigorous, review-style synthesis suitable for a molecular biology
audience. Treat the topic as a biological system whose boundaries, core
mechanisms, variants, and unresolved points should be made clear to readers who
know the field but are not specialists in this specific process.

The review should be explanatory rather than encyclopedic. Anchor broad claims
in primary literature or authoritative reviews, but keep the focus on how the
system works and how its parts fit together.

## Questions To Address

1. **Scope and boundaries**
   - What exactly is included in this biological system?
   - Which neighboring pathways, organelle processes, complexes, or regulatory
     events are often confused with it but should be treated separately?
   - Are there competing definitions in the literature?

2. **Core mechanism**
   - What is the best current model for the sequence of events?
   - Which steps are obligatory, which are conditional, and which are accessory?
   - What molecular assemblies, enzymes, receptors, adaptors, transporters, or
     structural units carry out each major step?

3. **Variation**
   - How does the system vary across major evolutionary lineages?
   - Are there well-supported differences between cell types, tissues,
     developmental stages, physiological states, or compartments?
   - Where are there alternative routes that achieve a similar outcome by
     different molecular means?

4. **Conservation and origin**
   - What is the deepest plausible evolutionary origin of the system?
   - Which parts appear ancient and conserved, and which appear to be later
     elaborations, replacements, or lineage-specific losses?
   - When a protein family has expanded, which family members are the best
     representatives for understanding the ancestral role?

5. **Physical and biological constraints**
   - What steps must occur in a particular order?
   - Which events are mutually exclusive, compartment-specific, cell-type
     specific, substrate-specific, or stage-specific?
   - What evidence rules out otherwise plausible paths through the system?

6. **Evidence and controversy**
   - Which mechanistic claims are strongly supported by experiments?
   - Where does the literature disagree, rely on indirect evidence, or mix data
     from organisms that may not be comparable?
   - What are the most important open questions?

## Output Format

Use the style and structure of a concise review article:

1. Executive summary
2. Definition and biological boundaries
3. Mechanistic overview
4. Major molecular players and active assemblies
5. Evolutionary and cell-biological variation
6. Constraints, dependencies, and failure modes
7. Controversies and open questions
8. Key references

Include citations for major claims, preferably PMIDs or DOIs. Be explicit about
uncertainty and avoid overgeneralizing from one organism, cell type, or assay
system to all biology.

# KIT signaling pathway module

## 1. Executive summary

The KIT module is best defined as signaling initiated when dimeric stem cell factor (SCF; KITLG) engages the class III receptor tyrosine kinase KIT/CD117, stabilizes a receptor dimer, activates the split intracellular kinase, and generates phosphotyrosine docking sites for SH2- or PTB-domain proteins. The immediate outputs are not three independent linear pathways but a coupled, partly redundant network: GRB2–SOS and SHP2/scaffold complexes feed Ras–RAF–MEK–ERK; PI3K p85–p110 generates PIP3 and activates AKT and related effectors; Src-family kinases (SFKs) amplify receptor and cytoskeletal signals; and STAT5 activation occurs in some contexts through KIT-associated JAK2/SFK machinery. The STAT branch is substantially less universal than MAPK or PI3K–AKT. (r�nnstrand2004signaltransductionvia pages 1-2, lennartsson2005normalandoncogenic pages 4-6, lennartsson2005normalandoncogenic pages 6-8, roskoski2005signalingbykit pages 1-2)

This module controls survival, proliferation, adhesion and migration in hematopoietic stem/progenitor cells, mast cells, melanocytes, germ cells and interstitial cells of Cajal (ICC). Cell identity is not specified by a unique “KIT pathway”; rather, membrane versus soluble SCF, receptor isoform, phosphosite availability, adaptor abundance, cooperating receptors, signal duration and transcriptional state determine the biological response. Genetic loss of KIT/KITLG disrupts hematopoiesis, pigmentation, fertility, mast-cell biology and gastrointestinal motility, whereas activating KIT mutations uncouple signaling from SCF in gastrointestinal stromal tumour (GIST), systemic mastocytosis and selected leukemias. (r�nnstrand2004signaltransductionvia pages 1-2, heldin2013structuralandfunctional pages 9-10, roskoski2005signalingbykit pages 1-2, lennartsson2005normalandoncogenic pages 1-2)

The strongest recent translational development is mutation-conformation-matched KIT inhibition. More than 90% of mastocytosis cases have a somatic activating KIT mutation, most commonly D816V, and avapritinib has established KIT D816V as a therapeutically tractable driver. In GIST, treatment remains genotype- and line-specific because juxtamembrane, ATP-pocket and activation-loop variants differ in conformational state and inhibitor susceptibility. Open Targets independently ranks KIT as the dominant target association for GIST (association score 0.893 in the retrieved database result), far above KITLG (0.118). (OpenTargets Search: gastrointestinal stromal tumor,systemic mastocytosis-KIT,KITLG, cilloni2024detectionofkit pages 12-14, corrionero2026kineticfingerprintsas pages 2-2)

## 2. Definition and biological boundaries

### Operational definition

The **core KIT signaling module** includes:

1. KITLG production and presentation as membrane-associated or soluble SCF;
2. SCF–KIT binding, receptor dimerization, kinase activation and trans-autophosphorylation;
3. recruitment or activation of KIT-proximal adaptors and enzymes, especially GRB2, SHC, PI3K p85, SFKs, SHP2, GAB2, PLCγ and—in selected cells—JAK/STAT machinery;
4. propagation through Ras–MAPK, PI3K–AKT, cytoskeletal/calcium and conditional STAT outputs; and
5. proximal attenuation through phosphatases, CBL-dependent ubiquitination, internalization and endolysosomal sorting. (heldin2013structuralandfunctional pages 9-10, lennartsson2005normalandoncogenic pages 4-6, r�nnstrand2004signaltransductionvia pages 8-9, roskoski2005signalingbykit pages 1-2)

### Boundaries and neighboring systems

Several connected processes should not be collapsed into the core module.

* **SCF production and niche specification** regulate pathway input but are not themselves KIT signal transduction. Endothelial, fibroblastic and perivascular stromal programs that determine KITLG abundance belong to niche biology.
* **General endocytosis, lysosomal degradation and ubiquitin homeostasis** are broader organelle processes. Only their KIT-directed recruitment and immediate consequences belong within the pathway boundary.
* **Integrin, CXCL12–CXCR4, VEGF, erythropoietin and FcεRI pathways** cooperate with KIT but remain distinct receptor systems. Their cross-talk can make PI3K, MAPK or STAT phosphorylation appear KIT-specific when it is not.
* **MITF-, CREB- and lineage-specific transcriptional circuits** are downstream or feedback programs rather than universal proximal components.
* **Constitutively active mutant KIT signaling** uses many wild-type effectors but bypasses the obligatory extracellular sequence; it should be treated as pathological rewiring, not simply stronger physiological SCF signaling. (lennartsson2005normalandoncogenic pages 6-8, lennartsson2005normalandoncogenic pages 19-20, lennartsson2005normalandoncogenic pages 1-2)

“SCF/KIT pathway” is therefore used in two ways in the literature: narrowly, for receptor-proximal events; and broadly, for the entire developmental or disease program influenced by KIT. The narrow definition is preferable mechanistically. It prevents KIT expression, KIT immunoreactivity or downstream ERK phosphorylation from being mistaken for evidence that a phenotype is directly KIT-dependent.

## 3. Mechanistic overview

### 3.1 Ligand presentation and receptor activation

KITLG is a noncovalent homodimer. Alternative splicing around exon 6 and subsequent proteolysis generate a readily cleaved soluble ligand and a more persistent membrane-associated ligand. Fibroblasts and endothelial cells are major sources. Membrane SCF provides spatially restricted, contact-dependent signaling and generally produces more sustained KIT phosphorylation and ERK/p38 activity; soluble SCF more often generates a rapid transient response. This difference is biologically important in stem-cell niches and cannot be modeled simply as a difference in ligand concentration. (heldin2013structuralandfunctional pages 9-10, lennartsson2005normalandoncogenic pages 4-6, lennartsson2005normalandoncogenic pages 1-2)

KIT contains five extracellular immunoglobulin-like domains, one transmembrane helix, an autoinhibitory juxtamembrane segment and a kinase domain interrupted by a kinase insert. A single SCF dimer binds two KIT molecules through the membrane-distal extracellular domains, while receptor–receptor contacts involving Ig-like domain 4 further stabilize the active assembly. Kinase activation then permits trans-autophosphorylation of tyrosines outside the catalytic core. Physiological wild-type signaling therefore has a constrained order: ligand engagement precedes productive dimerization, kinase activation precedes docking-site formation, and docking precedes most downstream output. (lennartsson2005normalandoncogenic pages 4-6, roskoski2005signalingbykit pages 1-2, lennartsson2005normalandoncogenic pages 1-2)

### 3.2 Phosphotyrosine effector recruitment

Human KIT phosphosites organize overlapping assemblies rather than one-effector/one-output channels:

* **Y568** recruits SFKs, SHP2 and APS-family adaptors.
* **Y570** recruits SHP1 and SHC and contributes to juxtamembrane signaling.
* **Y703 and Y936** bind GRB2; Y936 also binds GRB7 and APS.
* **Y721** is the principal direct PI3K p85 docking site.
* **Y730** recruits PLCγ.
* **Y900** can support PI3K-associated and indirect CRK complexes.

The exact residue numbering differs between human and mouse KIT—for example, human Y568/Y721 correspond approximately to mouse Y567/Y719—so cross-species papers should not be combined without normalization. (lennartsson2005normalandoncogenic pages 4-6, r�nnstrand2004signaltransductionvia pages 8-9, roskoski2005signalingbykit pages 1-2)

### 3.3 Ras–MAPK

GRB2 couples KIT to SOS either directly through Y703/Y936 or indirectly through SHC and SHP2-containing assemblies. SOS catalyses GDP–GTP exchange on RAS, initiating RAF–MEK–ERK signaling. SHP2 is mechanistically notable: despite being a phosphatase, it usually promotes full ERK activation, probably by remodeling inhibitory phosphotyrosine interactions and scaffolds rather than merely “turning signals off.” GAB2 provides an additional phosphotyrosine scaffold linking SHP2, GRB2 and PI3K. Gab2-deficient mast cells show impaired SCF-dependent growth and reduced ERK and AKT activation, but this does not make GAB2 obligatory in every KIT-expressing lineage. (r�nnstrand2004signaltransductionvia pages 8-9, roskoski2005signalingbykit pages 1-2)

### 3.4 PI3K–AKT

The p85 regulatory subunit binds primarily to KIT Y721 and recruits the p110 catalytic subunit, which converts phosphatidylinositol-4,5-bisphosphate to PIP3. PIP3 recruits PH-domain proteins, including AKT pathway components, to the membrane. This branch supports survival, proliferation, adhesion and migration. Genetic and docking-site studies show that direct KIT–PI3K association is important but not universally indispensable: Y721/Y719 mutants retain selected survival or developmental outputs because SFKs, GAB2 and cooperating receptors provide alternative routes. Combined SFK and PI3K docking activity can be sufficient for chemotaxis and calcium mobilization in tested systems. (lennartsson2005normalandoncogenic pages 4-6, lennartsson2005normalandoncogenic pages 6-8)

### 3.5 STAT5

STAT5 should be described as a **conditional KIT output**, not as an invariant direct substrate. SCF can transiently activate KIT-associated JAK2; STAT1 and STAT5A/B can associate with KIT and become tyrosine phosphorylated, and the KIT C-terminal region is required for full STAT5 activation in some systems. However, studies disagree about magnitude and JAK dependence. JAK2 contributes to SCF-driven progenitor growth and differentiation but appears less important in mast-cell responses. Timing, lineage, receptor expression, phosphatase inhibition and cell handling explain part—but probably not all—of the disagreement. There is no universally accepted KIT phosphotyrosine that functions as a dedicated direct STAT5 docking site. (lennartsson2005normalandoncogenic pages 6-8)

The resulting mechanistic synthesis is summarized below.

| Layer/step | Molecular event and principal players | Representative human KIT phosphosites | Status | Biological output | Evidence/uncertainty |
|---|---|---|---|---|---|
| Ligand presentation | Dimeric KITLG/SCF is membrane-bound or released by proteolytic cleavage as soluble SCF | — | Ligand required for physiological wild-type signaling; form is conditional | Membrane SCF generally produces more sustained KIT–ERK/p38 signaling; soluble SCF often gives a transient response | Strong biochemical and genetic support; effects vary with processing, dose and cell context |
| Receptor activation | One SCF dimer engages two KIT molecules; extracellular contacts stabilize the dimer, activate the split kinase domains and induce trans-autophosphorylation | Y568, Y570, Y703, Y721, Y730, Y900 and Y936 | Obligatory for canonical wild-type signaling | Creates SH2/PTB docking sites and initiates signaling | Strong structural, mutational and biochemical support; the temporal order of individual phosphosites remains incompletely resolved |
| SFK branch | Src-family kinases bind the juxtamembrane region and phosphorylate KIT or associated substrates | Y568; Y570 contributes to the juxtamembrane platform | Conditional but prominent in migration and cytoskeletal responses | Chemotaxis, adhesion, calcium mobilization and PI3K/MAPK amplification | Supported by docking-site mutants and inhibitors; the responsible SFK paralog varies by cell type |
| GRB2–SOS–Ras–MAPK | GRB2 binds KIT directly or through SHC/SHP2 assemblies; its SH3 domains recruit SOS, activating RAS–RAF–MEK–ERK | Y703 and Y936; Y570 can recruit SHC indirectly | Major branch, but no single docking route is universally obligatory | Proliferation, differentiation, immediate-early transcription and migration | Strong pathway evidence; redundancy among direct GRB2, SHC and scaffold-mediated routes complicates site attribution |
| PI3K–AKT | PI3K p85 binds phosphorylated KIT and recruits p110, producing PIP3 and activating AKT | Y721 directly; Y900 can support PI3K-associated complexes | Major but partly redundant and conditional | Survival, proliferation, adhesion, motility and fertility-associated functions | Strong genetic and biochemical evidence; Y721 mutation attenuates many outputs but does not abolish all responses |
| SHP2–GAB2 scaffold | SHP2 and GRB2-associated GAB2 organize additional RAS–ERK and PI3K–AKT signaling; GAB2 is phosphorylated after SCF stimulation | SHP2 mainly associated with Y568; GAB2 generally indirect | Accessory amplifier; strongly cell-type dependent | Sustained ERK/AKT activity and mast-cell growth | GAB2 loss gives clear mast-cell phenotypes; SHP2 is usually ERK-positive despite being a phosphatase, but its direct substrates remain uncertain |
| STAT output | KIT-associated JAK2, SFKs or KIT-linked complexes can phosphorylate STAT5A/B, enabling dimerization and transcription | Requires the KIT C-terminal region; no universally accepted direct STAT5 docking site | Conditional, not a universal core output | Survival, proliferation and lineage-specific transcription | Disputed branch: magnitude and JAK2 dependence vary with lineage, kinetics and assay conditions; JAK2 contributes in some progenitors but is less important in mast cells |
| Signal attenuation | SHP1 dephosphorylates KIT; CBL binds directly or through adaptors, ubiquitinates KIT and promotes internalization and lysosomal degradation | SHP1: Y570; CBL-regulatory contacts: Y568 and Y936 | Required for normal termination, with partial redundancy | Limits signal amplitude and duration and clears receptor | Strong mutational and loss-of-function evidence; CBL E3-ligase defects prolong MAPK/AKT signaling and can produce mastocytosis/myeloproliferation |
| Cell-type implementation | Shared branches are weighted differently in HSPCs, mast cells, melanocytes, germ cells and interstitial cells of Cajal | Same sites, but different adaptor abundance and feedback states | Conditional on lineage, stage and compartment | HSPC maintenance; mast-cell survival; pigmentation; gametogenesis; gastrointestinal pacemaker-cell maintenance | Strong organismal genetics; dominant intracellular branches differ across tissues, and membrane SCF is especially important in contact-dependent niches |
| Oncogenic bypass | Juxtamembrane mutations relieve autoinhibition; activation-loop mutations such as D816V stabilize active signaling without SCF | Mutant regions rather than docking sites; downstream use of Y721 and other sites can persist | Ligand and normal activation order become dispensable | Constitutive PI3K–AKT, STAT and/or MAPK signaling in GIST, mastocytosis and selected leukemias | Strong genetic, biochemical and therapeutic evidence; pathway use and inhibitor sensitivity depend on mutation class and kinase conformation |
| Teleost variation | Fish-specific genome duplication produced kita/kitb and kitlga/kitlgb, followed by subfunctionalization | Orthologous sites not uniformly mapped functionally | Lineage-specific alternative architecture | Kita–Kitlga retains major pigmentation functions; both ligands can cooperate with Epo in erythroid expansion, whereas Kitb does not compensate for Kita in tested settings | Supported by zebrafish genetics and gain/loss-of-function studies; ligand redundancy is tissue- and assay-dependent |


*Table: Compact synthesis of the SCF–KIT signaling sequence, phosphosite-linked assemblies, context-dependent outputs, attenuation mechanisms, oncogenic bypass and teleost variation. It distinguishes obligatory events from conditional branches and highlights major evidentiary uncertainties.*

## 4. Major molecular players and active assemblies

### SCF–KIT signaling complex

The minimal obligatory assembly is a dimeric SCF–KIT complex containing catalytically competent receptor molecules. By contrast, no single downstream adaptor is universally obligatory because KIT has multiple docking sites and substantial network redundancy. The principal functional assemblies are:

* **KIT–SFK–cytoskeletal complexes**, prominent in migration, adhesion and calcium responses;
* **KIT–GRB2–SOS and KIT–SHC–GRB2–SOS complexes**, which activate Ras–MAPK;
* **KIT–p85–p110 PI3K**, supplemented by indirect PI3K recruitment through GAB2;
* **KIT–SHP2–GAB2–GRB2 assemblies**, which amplify ERK and AKT signaling; and
* **KIT–JAK2/SFK–STAT complexes**, whose composition and necessity vary by cell type. (lennartsson2005normalandoncogenic pages 4-6, r�nnstrand2004signaltransductionvia pages 8-9, lennartsson2005normalandoncogenic pages 6-8, roskoski2005signalingbykit pages 1-2)

### Negative-regulatory assemblies

SHP1 binds the juxtamembrane region, particularly Y570, and negatively regulates receptor phosphorylation. CBL provides a second control layer. Primary studies identify KIT Y568 and Y936 as CBL-binding determinants required for efficient ligand-induced ubiquitination, internalization and degradation. Consistent with that mechanism, E3-defective CBL mutants prevent normal KIT ubiquitination/endocytosis, increase basal KIT phosphorylation, prolong MAPK and PI3K–AKT signaling and produce generalized mastocytosis/myeloproliferation in transplantation models. In one study, six mice developed mast-cell sarcomas and two developed myeloid leukemia. SFK inhibition abolished proliferation and clonogenic growth of CBL-mutant cells in the reported assays, illustrating how defective attenuation can shift pathway dependence toward SFKs. (r�nnstrand2004signaltransductionvia pages 8-9, bandi2009e3ligasedefectivecbl pages 9-10, cilloni2024detectionofkit pages 12-14)

The endpoint is predominantly lysosomal disposal of monoubiquitinated receptor, although proteasomal inhibitors can affect trafficking indirectly. Thus, “proteasomal degradation of KIT” should not be used as a blanket description. Internalized receptors may also signal transiently before degradation, making trafficking part of signal shaping rather than merely termination. (heldin2013structuralandfunctional pages 9-10, bandi2009e3ligasedefectivecbl pages 9-10)

## 5. Evolutionary and cell-biological variation

### Evolution and conservation

Protein-tyrosine-kinase signaling predates animals: related RTKs occur in choanoflagellates, and ancient kinase modules were subsequently elaborated during multicellular evolution. KIT itself belongs to the vertebrate class III RTK family with PDGF receptors, CSF1R and FLT3. Vertebrate genome duplications expanded this receptor repertoire; the precise point at which a fully recognizable KIT–KITLG pair originated is less securely established than the older origin of RTK enzymology and should not be projected onto distant invertebrate RTKs. (roskoski2005signalingbykit pages 1-2)

Teleost whole-genome duplication produced two KIT receptors and two ligands in zebrafish: **kita/kitb** and **kitlga/kitlgb**. Functional partitioning is incomplete. Kita–Kitlga retains the clearest ancestral pigmentation role: kitlga knockdown phenocopies kita deficiency in melanocyte migration and survival, whereas kitlgb does not fully substitute. In erythropoiesis, both ligands can cooperate with erythropoietin in vivo, but ex vivo Kitlga is more active, and neither ligand rescues the response in kita mutants; Kitb therefore does not compensate in that tested context. These results warn against assuming a one-to-one equivalence between zebrafish paralogs and mammalian KIT/KITLG. (oltova2020zebrafishkitligands pages 12-15, oltova2020zebrafishkitligands pages 19-24)

### Cell type and developmental state

* **Hematopoietic stem/progenitor cells.** KIT is common in primitive progenitors and cooperates with thrombopoietin, erythropoietin, G-CSF and niche signals. It promotes maintenance or expansion but does not alone define stemness. Membrane SCF is especially suited to contact-dependent niche support. Recent niche reviews emphasize developmental changes in the cellular sources of SCF and caution that cell-type-specific deletion studies can be confounded by promiscuous Cre drivers and compensation. (lennartsson2005normalandoncogenic pages 1-2, karima2024unlockingtheregenerative pages 20-21, sanchezlanzas2024theevolvinghematopoietic pages 5-5)
* **Mast cells.** KIT is unusually persistent after differentiation and remains central to survival, proliferation and function. Primary human skin-mast-cell work published in December 2023 showed that CREB inhibition or knockdown reduces KIT expression and severely impairs SCF-induced ERK, AKT and STAT5 activation, anti-apoptosis and cell-cycle progression. Because KIT also activates CREB, these data support a positive feedback loop, but they do not establish that the loop operates identically in every mast-cell tissue subtype.
* **Melanocytes.** KIT controls precursor migration/survival and adult pigmentary responses in cooperation with MITF and paracrine skin signals. Loss-of-function produces piebald phenotypes; excessive or ectopic signaling can alter pigmentation. (r�nnstrand2004signaltransductionvia pages 1-2, lennartsson2005normalandoncogenic pages 1-2)
* **Germ cells.** KIT supports primordial-germ-cell survival/migration and gametogenesis. Fertility defects associated with disrupted PI3K docking indicate a particularly important PI3K branch, although species and developmental stage matter. (heldin2013structuralandfunctional pages 9-10)
* **Interstitial cells of Cajal.** KIT is required for development and maintenance of major ICC populations, thereby affecting gastrointestinal electrical pacemaking and motility. Not every KIT-positive interstitial or “telocyte” population is an ICC, and some intestinal ICC development can show partial KIT independence; marker expression alone is therefore insufficient. (heldin2013structuralandfunctional pages 9-10, roskoski2005signalingbykit pages 1-2)

Receptor splice variation adds another layer. Human GNNK− KIT generally undergoes stronger ligand-induced phosphorylation, faster internalization and stronger ERK activation than GNNK+ KIT in experimental systems. Four human isoforms have been described, including extracellular juxtamembrane and kinase-insert variants. Their tissue distribution and physiological relevance remain less well resolved than the canonical phosphosite map. (r�nnstrand2004signaltransductionvia pages 1-2, heldin2013structuralandfunctional pages 9-10)

## 6. Constraints, dependencies and failure modes

### Obligatory order

For wild-type KIT, SCF binding must precede stable receptor dimerization; catalytic activation must precede phosphotyrosine-dependent effector recruitment; and nuclear STAT output requires phosphorylation before STAT dimerization and DNA binding. Direct SH2 recruitment cannot precede creation of the corresponding phosphotyrosine. These physical constraints rule out models in which unphosphorylated wild-type KIT directly recruits p85, GRB2 or SHP2 through their SH2 domains. (lennartsson2005normalandoncogenic pages 4-6, roskoski2005signalingbykit pages 1-2)

### Conditional and mutually competing events

Phosphosite occupancy is dynamic and competitive. At Y568, signaling adaptors, phosphatases and CBL-related regulatory machinery can use overlapping receptor states. Direct p85 docking at Y721 and indirect recruitment through GAB2 can substitute partly for one another. Similarly, Ras can be reached through direct GRB2 binding, SHC or SHP2/GAB2 scaffolds. The network therefore resists simplistic claims that one phosphosite “is” one biological response. (lennartsson2005normalandoncogenic pages 4-6, r�nnstrand2004signaltransductionvia pages 8-9, lennartsson2005normalandoncogenic pages 6-8)

Membrane and soluble SCF are not mutually exclusive at the organism level, but an individual ligand molecule has one presentation state at a given time. Their different dwell times and spatial ranges impose distinct signaling constraints. Likewise, receptor signaling from the plasma membrane and from endosomes occupies different compartments and temporal windows.

### Pathological failure modes

1. **Loss of receptor or ligand:** anemia, mast-cell deficiency, hypopigmentation, infertility and gastrointestinal dysmotility; complete disruption can be lethal. (roskoski2005signalingbykit pages 1-2)
2. **Juxtamembrane mutation:** loss of autoinhibition, common in GIST, often retaining dependence on familiar ERK and AKT effectors and sensitivity to inhibitors such as imatinib. (r�nnstrand2004signaltransductionvia pages 1-2, lennartsson2005normalandoncogenic pages 19-20)
3. **Activation-loop mutation:** D816 variants stabilize active signaling, frequently activate PI3K and STAT programs, and are poorly inhibited by drugs that require an inactive kinase conformation. (lennartsson2005normalandoncogenic pages 19-20, corrionero2026kineticfingerprintsas pages 2-2)
4. **Defective attenuation:** loss of CBL E3 function prolongs KIT/SFK–MAPK–AKT signaling and can produce mastocytosis or myeloproliferation. (bandi2009e3ligasedefectivecbl pages 9-10)
5. **Misinterpretation of KIT expression:** CD117 positivity is neither proof of pathway activation nor proof that a tumour is KIT-driven; mutation, phosphorylation and inhibitor-response evidence are needed.

## 7. Current applications, recent developments and real-world implementation

### GIST precision therapy

KIT is one of the clearest clinically validated oncogenic RTK targets. Imatinib is effective against many juxtamembrane KIT mutants, while sunitinib and regorafenib address subsets of resistant kinase-domain variants. Ripretinib is a broad switch-control inhibitor used in later-line GIST; avapritinib is particularly active against active-conformation PDGFRA D842V and selected KIT activation-loop variants. A 2024 two-centre retrospective series included 34 metastatic/unresectable GIST patients who received both avapritinib and ripretinib. Response rates were 12–18% for each drug depending on sequence; median time to progression was approximately 3.65–4.73 months for ripretinib and 4.11–5.39 months for avapritinib. Median overall survival after initiation of the two-drug sequence was 29.63 versus 33.7 months, with no evidence that sequence determined efficacy. These small, selected cohorts should not be treated as randomized comparative evidence.

### Systemic mastocytosis

The D816V activation-loop mutation drives the large majority of adult systemic mastocytosis. A 2024 molecular-diagnostics review estimates that more than 90% of patients with mastocytosis carry a somatic activating KIT mutation, often at variant-allele fractions below routine NGS detection limits; highly sensitive allele-specific PCR or digital PCR is therefore required when clinical suspicion is high. (cilloni2024detectionofkit pages 12-14, corrionero2026kineticfingerprintsas pages 2-2)

The randomized PIONEER study of avapritinib in indolent systemic mastocytosis was published in **May 2023** in *NEJM Evidence* (DOI: [10.1056/EVIDoa2200339](https://doi.org/10.1056/EVIDoa2200339)). It established that low-dose mutant-KIT inhibition can improve mediator-related symptom burden while reducing objective mast-cell disease measures, moving treatment beyond symptomatic blockade alone. The US FDA expanded avapritinib to adults with indolent systemic mastocytosis in **May 2023**. The clinical principle is important: KIT inhibition can reduce clonal mast-cell burden, whereas antihistamines, leukotriene modifiers and related drugs primarily control released mediators. However, intracranial bleeding risk, cognitive effects, cytopenias and reproductive considerations require indication- and dose-specific monitoring.

### Regenerative and cell-manufacturing applications

SCF is routinely used with other cytokines to culture or expand hematopoietic progenitors and appears in mobilization and ex-vivo engineering protocols. Its use alone is limited because KIT activation favors proliferation and survival but does not reproduce the spatial, adhesive and temporal organization of a native niche. Membrane-tethered ligand or biomaterial presentation is therefore conceptually attractive for engineered niches. Recent regenerative reviews also emphasize a safety problem: systemic SCF can expand or activate mast cells and melanocytes, so local delivery and controlled presentation are preferable to unrestricted exposure. (lennartsson2005normalandoncogenic pages 1-2, karima2024unlockingtheregenerative pages 20-21)

## 8. Controversies and open questions

1. **What is the direct route to STAT5?** KIT-dependent STAT5 phosphorylation is reproducible in some cells, but the relative contributions of JAK2, SFKs and receptor-associated complexes remain unsettled. A dedicated direct docking site has not been established. (lennartsson2005normalandoncogenic pages 6-8)
2. **How are phosphosite combinations decoded in single cells?** Most maps derive from population immunoprecipitation or mutant receptors. They do not reveal which combinations coexist on one receptor dimer or how occupancy changes between plasma membrane and endosomes.
3. **What determines membrane-SCF superiority?** Persistence, geometry, mechanical retention and reduced receptor downregulation are plausible contributors. Their relative importance in authentic human niches remains unresolved.
4. **How general is SHP2’s positive role?** SHP2 is usually required for full ERK output, but direct substrates and the balance between catalytic and scaffolding functions remain context dependent. Earlier literature even classified SHP2 with negative phosphatases; genetic support is stronger for a positive ERK role than for a universal negative role. (lennartsson2005normalandoncogenic pages 4-6, r�nnstrand2004signaltransductionvia pages 8-9)
5. **How do normal and oncogenic KIT signalosomes differ?** D816V does more than remove ligand dependence: it alters kinase conformation, substrate use, trafficking and inhibitor binding. Extrapolating SCF-stimulated wild-type wiring to D816V disease is unsafe. (lennartsson2005normalandoncogenic pages 19-20, corrionero2026kineticfingerprintsas pages 2-2)
6. **Which evolutionary functions are ancestral?** Pigment, germ-cell and hematopoietic functions have redistributed after teleost duplication. Comparative studies need matched ligand–receptor pairs and cannot assume Kitb or Kitlgb is a redundant copy. (oltova2020zebrafishkitligands pages 12-15)
7. **Can KIT be targeted without unacceptable normal-cell injury?** The receptor is shared by normal HSPCs, mast cells, melanocytes, germ cells and ICC. Mutation-selective inhibitors, kinetic selectivity, antibody approaches and localized ligand engineering are promising, but lineage toxicity remains an inherent constraint.

## 9. Key references

1. Rönnstrand L. “Signal transduction via the stem cell factor receptor/c-Kit.” *Cell Mol Life Sci.* Published October 2004. DOI: [10.1007/s00018-004-4189-6](https://doi.org/10.1007/s00018-004-4189-6). Authoritative receptor-proximal review. (r�nnstrand2004signaltransductionvia pages 1-2, r�nnstrand2004signaltransductionvia pages 8-9)
2. Lennartsson J, Jelacic T, Linnekin D, Shivakrupa R. “Normal and Oncogenic Forms of the Receptor Tyrosine Kinase Kit.” *Stem Cells.* Published January 2005. DOI: [10.1634/stemcells.2004-0117](https://doi.org/10.1634/stemcells.2004-0117). Detailed phosphosite and oncogenic-signaling synthesis. (lennartsson2005normalandoncogenic pages 4-6, lennartsson2005normalandoncogenic pages 6-8, lennartsson2005normalandoncogenic pages 19-20, lennartsson2005normalandoncogenic pages 1-2)
3. Roskoski R. “Signaling by Kit protein-tyrosine kinase—the stem cell factor receptor.” *Biochem Biophys Res Commun.* Published November 2005. DOI: [10.1016/j.bbrc.2005.08.055](https://doi.org/10.1016/j.bbrc.2005.08.055). Concise architecture and phosphosite map. (roskoski2005signalingbykit pages 1-2)
4. Heldin C-H, Lennartsson J. “Structural and functional properties of platelet-derived growth factor and stem cell factor receptors.” *Cold Spring Harb Perspect Biol.* Published August 2013. DOI: [10.1101/cshperspect.a009100](https://doi.org/10.1101/cshperspect.a009100). Integrative structural and regulatory review. (heldin2013structuralandfunctional pages 9-10)
5. Masson K, Heiss E, Band H, Rönnstrand L. “Direct binding of Cbl to Tyr568 and Tyr936 of the stem cell factor receptor/c-Kit is required for ligand-induced ubiquitination, internalization and degradation.” *Biochem J.* Published October 2006. DOI: [10.1042/BJ20060464](https://doi.org/10.1042/BJ20060464). Primary trafficking mechanism. (cilloni2024detectionofkit pages 12-14)
6. Bandi SR et al. “E3 ligase-defective Cbl mutants lead to a generalized mastocytosis and myeloproliferative disease.” *Blood.* Published November 2009. DOI: [10.1182/blood-2008-12-190934](https://doi.org/10.1182/blood-2008-12-190934). Primary genetic evidence for pathological failure of attenuation. (bandi2009e3ligasedefectivecbl pages 9-10)
7. Bal G et al. “CREB Is Indispensable to KIT Function in Human Skin Mast Cells—A Positive Feedback Loop between CREB and KIT Orchestrates Skin Mast Cell Fate.” *Cells.* Published December 2023; 13:42. DOI: [10.3390/cells13010042](https://doi.org/10.3390/cells13010042).
8. Gotlib J et al. “Avapritinib versus Placebo in Indolent Systemic Mastocytosis.” *NEJM Evidence.* Published May 2023. DOI: [10.1056/EVIDoa2200339](https://doi.org/10.1056/EVIDoa2200339).
9. Cilloni D et al. “Detection of KIT Mutations in Systemic Mastocytosis: How, When, and Why.” *Int J Mol Sci.* Published October 2024;25:10885. DOI: [10.3390/ijms252010885](https://doi.org/10.3390/ijms252010885). (cilloni2024detectionofkit pages 12-14)
10. Sánchez-Lanzas R, Jiménez-Pompa A, Ganuza M. “The evolving hematopoietic niche during development.” *Front Mol Biosci.* Published October 2024. DOI: [10.3389/fmolb.2024.1488199](https://doi.org/10.3389/fmolb.2024.1488199). (sanchezlanzas2024theevolvinghematopoietic pages 5-5)
11. Oltova J et al. “Zebrafish Kit ligands cooperate with erythropoietin to promote erythroid cell expansion.” bioRxiv preprint, published February 2020. DOI: [10.1101/2020.02.03.931634](https://doi.org/10.1101/2020.02.03.931634). Preprint evidence should be weighted below peer-reviewed genetic studies. (oltova2020zebrafishkitligands pages 12-15, oltova2020zebrafishkitligands pages 19-24)
12. Karima G, Kim HD. “Unlocking the regenerative key: Targeting stem cell factors for bone renewal.” *J Tissue Eng.* Published 2024. DOI: [10.1177/20417314241287491](https://doi.org/10.1177/20417314241287491). (karima2024unlockingtheregenerative pages 20-21)

**Overall assessment.** The ligand–dimerization–autophosphorylation model and the major KIT docking sites are strongly established. PI3K–AKT and Ras–MAPK are robust but redundantly wired outputs; STAT5 is real in selected settings but should not be presented as universally obligatory. The field’s principal current shift is from a static pathway diagram toward a state-dependent signalosome shaped by ligand presentation, receptor isoform, cell lineage, trafficking and kinase conformation.

References

1. (r�nnstrand2004signaltransductionvia pages 1-2): L. R�nnstrand. Signal transduction via the stem cell factor receptor/c-kit. Cellular and Molecular Life Sciences CMLS, 61:2535-2548, Oct 2004. URL: https://doi.org/10.1007/s00018-004-4189-6, doi:10.1007/s00018-004-4189-6. This article has 643 citations.

2. (lennartsson2005normalandoncogenic pages 4-6): Johan Lennartsson, Tanya Jelacic, Diana Linnekin, and R. Shivakrupa. Normal and oncogenic forms of the receptor tyrosine kinase kit. STEM CELLS, 23:16-43, Jan 2005. URL: https://doi.org/10.1634/stemcells.2004-0117, doi:10.1634/stemcells.2004-0117. This article has 381 citations and is from a highest quality peer-reviewed journal.

3. (lennartsson2005normalandoncogenic pages 6-8): Johan Lennartsson, Tanya Jelacic, Diana Linnekin, and R. Shivakrupa. Normal and oncogenic forms of the receptor tyrosine kinase kit. STEM CELLS, 23:16-43, Jan 2005. URL: https://doi.org/10.1634/stemcells.2004-0117, doi:10.1634/stemcells.2004-0117. This article has 381 citations and is from a highest quality peer-reviewed journal.

4. (roskoski2005signalingbykit pages 1-2): Robert Roskoski. Signaling by kit protein-tyrosine kinase—the stem cell factor receptor. Biochemical and Biophysical Research Communications, 337(1):1-13, Nov 2005. URL: https://doi.org/10.1016/j.bbrc.2005.08.055, doi:10.1016/j.bbrc.2005.08.055. This article has 368 citations and is from a peer-reviewed journal.

5. (heldin2013structuralandfunctional pages 9-10): C.-H. Heldin and J. Lennartsson. Structural and functional properties of platelet-derived growth factor and stem cell factor receptors. Cold Spring Harbor perspectives in biology, 5 8:a009100, Aug 2013. URL: https://doi.org/10.1101/cshperspect.a009100, doi:10.1101/cshperspect.a009100. This article has 244 citations and is from a peer-reviewed journal.

6. (lennartsson2005normalandoncogenic pages 1-2): Johan Lennartsson, Tanya Jelacic, Diana Linnekin, and R. Shivakrupa. Normal and oncogenic forms of the receptor tyrosine kinase kit. STEM CELLS, 23:16-43, Jan 2005. URL: https://doi.org/10.1634/stemcells.2004-0117, doi:10.1634/stemcells.2004-0117. This article has 381 citations and is from a highest quality peer-reviewed journal.

7. (OpenTargets Search: gastrointestinal stromal tumor,systemic mastocytosis-KIT,KITLG): Open Targets Query (gastrointestinal stromal tumor,systemic mastocytosis-KIT,KITLG, 16 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

8. (cilloni2024detectionofkit pages 12-14): Daniela Cilloni, Beatrice Maffeo, Arianna Savi, Alice Costanza Danzero, Valentina Bonuomo, and Carmen Fava. Detection of kit mutations in systemic mastocytosis: how, when, and why. Oct 2024. URL: https://doi.org/10.3390/ijms252010885, doi:10.3390/ijms252010885. This article has 24 citations.

9. (corrionero2026kineticfingerprintsas pages 2-2): Ana Corrionero, Niall Prendiville, Tatiana Cazorla, Maria Baena‐Nuevo, Röhm Sandra, Emilio Camafeita, Stefan Knapp, and Patricia Alfonso. Kinetic fingerprints as mechanistic and clinical roadmaps across kit activation states. Jun 2026. URL: https://doi.org/10.1002/cmdc.70331, doi:10.1002/cmdc.70331. This article has 1 citations and is from a peer-reviewed journal.

10. (r�nnstrand2004signaltransductionvia pages 8-9): L. R�nnstrand. Signal transduction via the stem cell factor receptor/c-kit. Cellular and Molecular Life Sciences CMLS, 61:2535-2548, Oct 2004. URL: https://doi.org/10.1007/s00018-004-4189-6, doi:10.1007/s00018-004-4189-6. This article has 643 citations.

11. (lennartsson2005normalandoncogenic pages 19-20): Johan Lennartsson, Tanya Jelacic, Diana Linnekin, and R. Shivakrupa. Normal and oncogenic forms of the receptor tyrosine kinase kit. STEM CELLS, 23:16-43, Jan 2005. URL: https://doi.org/10.1634/stemcells.2004-0117, doi:10.1634/stemcells.2004-0117. This article has 381 citations and is from a highest quality peer-reviewed journal.

12. (bandi2009e3ligasedefectivecbl pages 9-10): Srinivasa Rao Bandi, Christian Brandts, Marion Rensinghoff, Rebekka Grundler, Lara Tickenbrock, Gabriele Köhler, Justus Duyster, Wolfgang E. Berdel, Carsten Müller-Tidow, Hubert Serve, and Bülent Sargin. E3 ligase-defective cbl mutants lead to a generalized mastocytosis and myeloproliferative disease. Blood, 114 19:4197-208, Nov 2009. URL: https://doi.org/10.1182/blood-2008-12-190934, doi:10.1182/blood-2008-12-190934. This article has 63 citations and is from a highest quality peer-reviewed journal.

13. (oltova2020zebrafishkitligands pages 12-15): Jana Oltova, Ondrej Svoboda, Olga Machonova, Petra Svatonova, David Traver, Michal Kolar, and Petr Bartunek. Zebrafish kit ligands cooperate with erythropoietin to promote erythroid cell expansion. bioRxiv, Feb 2020. URL: https://doi.org/10.1101/2020.02.03.931634, doi:10.1101/2020.02.03.931634. This article has 9 citations.

14. (oltova2020zebrafishkitligands pages 19-24): Jana Oltova, Ondrej Svoboda, Olga Machonova, Petra Svatonova, David Traver, Michal Kolar, and Petr Bartunek. Zebrafish kit ligands cooperate with erythropoietin to promote erythroid cell expansion. bioRxiv, Feb 2020. URL: https://doi.org/10.1101/2020.02.03.931634, doi:10.1101/2020.02.03.931634. This article has 9 citations.

15. (karima2024unlockingtheregenerative pages 20-21): Gul Karima and Hwan D. Kim. Unlocking the regenerative key: targeting stem cell factors for bone renewal. Journal of Tissue Engineering, Jan 2024. URL: https://doi.org/10.1177/20417314241287491, doi:10.1177/20417314241287491. This article has 7 citations and is from a domain leading peer-reviewed journal.

16. (sanchezlanzas2024theevolvinghematopoietic pages 5-5): Raúl Sánchez-Lanzas, Amanda Jiménez-Pompa, and Miguel Ganuza. The evolving hematopoietic niche during development. Frontiers in Molecular Biosciences, Oct 2024. URL: https://doi.org/10.3389/fmolb.2024.1488199, doi:10.3389/fmolb.2024.1488199. This article has 17 citations.

## Artifacts

- [Edison artifact artifact-00](kit_signaling-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. lennartsson2005normalandoncogenic pages 6-8
2. roskoski2005signalingbykit pages 1-2
3. heldin2013structuralandfunctional pages 9-10
4. oltova2020zebrafishkitligands pages 12-15
5. cilloni2024detectionofkit pages 12-14
6. sanchezlanzas2024theevolvinghematopoietic pages 5-5
7. karima2024unlockingtheregenerative pages 20-21
8. lennartsson2005normalandoncogenic pages 4-6
9. lennartsson2005normalandoncogenic pages 1-2
10. corrionero2026kineticfingerprintsas pages 2-2
11. lennartsson2005normalandoncogenic pages 19-20
12. oltova2020zebrafishkitligands pages 19-24
13. 10.1056/EVIDoa2200339
14. 10.1007/s00018-004-4189-6
15. 10.1634/stemcells.2004-0117
16. 10.1016/j.bbrc.2005.08.055
17. 10.1101/cshperspect.a009100
18. 10.1042/BJ20060464
19. 10.1182/blood-2008-12-190934
20. 10.3390/cells13010042
21. 10.3390/ijms252010885
22. 10.3389/fmolb.2024.1488199
23. 10.1101/2020.02.03.931634
24. 10.1177/20417314241287491
25. https://doi.org/10.1056/EVIDoa2200339
26. https://doi.org/10.1007/s00018-004-4189-6
27. https://doi.org/10.1634/stemcells.2004-0117
28. https://doi.org/10.1016/j.bbrc.2005.08.055
29. https://doi.org/10.1101/cshperspect.a009100
30. https://doi.org/10.1042/BJ20060464
31. https://doi.org/10.1182/blood-2008-12-190934
32. https://doi.org/10.3390/cells13010042
33. https://doi.org/10.3390/ijms252010885
34. https://doi.org/10.3389/fmolb.2024.1488199
35. https://doi.org/10.1101/2020.02.03.931634
36. https://doi.org/10.1177/20417314241287491
37. https://doi.org/10.1007/s00018-004-4189-6,
38. https://doi.org/10.1634/stemcells.2004-0117,
39. https://doi.org/10.1016/j.bbrc.2005.08.055,
40. https://doi.org/10.1101/cshperspect.a009100,
41. https://doi.org/10.3390/ijms252010885,
42. https://doi.org/10.1002/cmdc.70331,
43. https://doi.org/10.1182/blood-2008-12-190934,
44. https://doi.org/10.1101/2020.02.03.931634,
45. https://doi.org/10.1177/20417314241287491,
46. https://doi.org/10.3389/fmolb.2024.1488199,