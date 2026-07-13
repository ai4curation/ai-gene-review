---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-06T23:17:58.696111'
end_time: '2026-07-06T23:40:27.612658'
duration_seconds: 1348.92
template_file: templates/module_research.md.j2
template_variables:
  module_title: Mycolic acid biosynthesis boundary module
  module_summary: 'A taxon-neutral boundary module for formation of mycolic acids,
    the long-chain alpha-alkyl beta-hydroxy fatty acids characteristic of mycolate-containing
    bacterial envelopes. This module is intentionally framed as a boundary check for
    organism-specific pathway curation: generic phosphopantetheinyl-transferase and
    malonyl-ACP formation steps can appear in KEGG mycolic-acid maps, but by themselves
    they do not demonstrate that a genome encodes the mycolate-specific elongation,
    modification, condensation, reduction, and envelope-transfer machinery needed
    to synthesize mycolic acids. For Pseudomonas putida KT2440, KEGG ppu00074 contains
    only PP_1183 and fabD; current UniProt/GOA evidence supports siderophore carrier-protein
    activation and type-II fatty-acid biosynthesis, not a satisfiable mycolic-acid
    pathway.'
  module_outline: "- Mycolic acid biosynthesis boundary module\n  - 1. carrier-protein\
    \ phosphopantetheinylation support\n  - Carrier-protein phosphopantetheinylation\n\
    \    - 4'-phosphopantetheinyltransferase (molecular player: holo-[acyl-carrier-protein]\
    \ synthase activity; activity or role: holo-[acyl-carrier-protein] synthase activity)\n\
    \  - 2. malonyl-ACP precursor supply\n  - Malonyl-CoA to malonyl-ACP\n    - Malonyl\
    \ CoA-acyl carrier protein transacylase (molecular player: [acyl-carrier-protein]\
    \ S-malonyltransferase activity; activity or role: [acyl-carrier-protein] S-malonyltransferase\
    \ activity)\n  - 3. mycolate-specific envelope-lipid assembly\n  - Mycolate-specific\
    \ chain assembly and envelope transfer"
  module_connections: No explicit connections.
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 28
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: mycolic_acid_biosynthesis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: mycolic_acid_biosynthesis-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Commissioned Review Brief

## Review Topic

Mycolic acid biosynthesis boundary module

## Working Scope

A taxon-neutral boundary module for formation of mycolic acids, the long-chain alpha-alkyl beta-hydroxy fatty acids characteristic of mycolate-containing bacterial envelopes. This module is intentionally framed as a boundary check for organism-specific pathway curation: generic phosphopantetheinyl-transferase and malonyl-ACP formation steps can appear in KEGG mycolic-acid maps, but by themselves they do not demonstrate that a genome encodes the mycolate-specific elongation, modification, condensation, reduction, and envelope-transfer machinery needed to synthesize mycolic acids. For Pseudomonas putida KT2440, KEGG ppu00074 contains only PP_1183 and fabD; current UniProt/GOA evidence supports siderophore carrier-protein activation and type-II fatty-acid biosynthesis, not a satisfiable mycolic-acid pathway.

## Provisional Biological Outline

- Mycolic acid biosynthesis boundary module
  - 1. carrier-protein phosphopantetheinylation support
  - Carrier-protein phosphopantetheinylation
    - 4'-phosphopantetheinyltransferase (molecular player: holo-[acyl-carrier-protein] synthase activity; activity or role: holo-[acyl-carrier-protein] synthase activity)
  - 2. malonyl-ACP precursor supply
  - Malonyl-CoA to malonyl-ACP
    - Malonyl CoA-acyl carrier protein transacylase (molecular player: [acyl-carrier-protein] S-malonyltransferase activity; activity or role: [acyl-carrier-protein] S-malonyltransferase activity)
  - 3. mycolate-specific envelope-lipid assembly
  - Mycolate-specific chain assembly and envelope transfer

## Known Relationships Among Steps

No explicit connections.

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

Mycolic acid biosynthesis boundary module

## Working Scope

A taxon-neutral boundary module for formation of mycolic acids, the long-chain alpha-alkyl beta-hydroxy fatty acids characteristic of mycolate-containing bacterial envelopes. This module is intentionally framed as a boundary check for organism-specific pathway curation: generic phosphopantetheinyl-transferase and malonyl-ACP formation steps can appear in KEGG mycolic-acid maps, but by themselves they do not demonstrate that a genome encodes the mycolate-specific elongation, modification, condensation, reduction, and envelope-transfer machinery needed to synthesize mycolic acids. For Pseudomonas putida KT2440, KEGG ppu00074 contains only PP_1183 and fabD; current UniProt/GOA evidence supports siderophore carrier-protein activation and type-II fatty-acid biosynthesis, not a satisfiable mycolic-acid pathway.

## Provisional Biological Outline

- Mycolic acid biosynthesis boundary module
  - 1. carrier-protein phosphopantetheinylation support
  - Carrier-protein phosphopantetheinylation
    - 4'-phosphopantetheinyltransferase (molecular player: holo-[acyl-carrier-protein] synthase activity; activity or role: holo-[acyl-carrier-protein] synthase activity)
  - 2. malonyl-ACP precursor supply
  - Malonyl-CoA to malonyl-ACP
    - Malonyl CoA-acyl carrier protein transacylase (molecular player: [acyl-carrier-protein] S-malonyltransferase activity; activity or role: [acyl-carrier-protein] S-malonyltransferase activity)
  - 3. mycolate-specific envelope-lipid assembly
  - Mycolate-specific chain assembly and envelope transfer

## Known Relationships Among Steps

No explicit connections.

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


# Mycolic Acid Biosynthesis Boundary Module: A Review-Style Synthesis

## 1. Executive Summary

Mycolic acids are very-long-chain α-alkyl β-hydroxy fatty acids (typically C60–C90 in mycobacteria) that define the outer membrane of bacteria in the suborder Corynebacterineae (marrakchi2014mycolicacidsstructures pages 2-3). Their biosynthesis requires a coordinated set of enzymatic modules spanning precursor generation, chain elongation, meromycolic modification, Claisen condensation, product reduction, transmembrane transport, and envelope assembly. A critical conceptual and practical challenge in pathway curation is distinguishing the mycolate-specific machinery from the ubiquitous housekeeping enzymes—particularly 4′-phosphopantetheinyl transferases (PPTases) and malonyl-CoA:ACP transacylases (FabD)—that support general fatty acid and secondary metabolite biosynthesis. These generic support enzymes appear in KEGG mycolic acid maps for organisms such as *Pseudomonas putida* KT2440, yet their presence alone is insufficient evidence for a satisfiable mycolic acid pathway. This review defines the boundary module for mycolic acid biosynthesis, describes its core mechanism, maps variation across the Corynebacterineae, and articulates the minimum gene set that must be present before an organism's genome can be considered to encode the mycolate pathway.

## 2. Definition and Biological Boundaries

### 2.1 What Is Included

The mycolic acid biosynthesis pathway encompasses all enzymatic steps from the generation of dedicated acyl-chain precursors through their final deposition in the cell envelope. These steps include: (i) de novo fatty acid synthesis by FAS-I producing C16–C18 and C24–C26 acyl-CoA intermediates; (ii) elongation of the meromycolic chain by the dissociable FAS-II system; (iii) SAM-dependent modification of the meromycolate chain (cyclopropanation, desaturation, methoxylation, ketone formation); (iv) activation of the meromycolic chain by FadD32 and carboxylation of the α-branch by AccD4; (v) Claisen-type condensation by the polyketide synthase Pks13; (vi) reduction of the resulting β-ketoester by CmrA to form trehalose monomycolate (TMM); (vii) export of TMM across the inner membrane by MmpL3; and (viii) periplasmic transfer of mycolates from TMM to arabinogalactan and trehalose acceptors by the Ag85 mycolyltransferase complex (sethiya2020mmpl3inhibitiona pages 3-5, williams2023molecularmechanismsof pages 1-2, batt2020thethickwaxy pages 8-9, gavalda2014thepolyketidesynthase pages 7-8).

### 2.2 What Should Be Treated Separately

Several enzymatic activities that appear in KEGG mycolic acid pathway maps are actually components of general metabolism and should not, by themselves, be interpreted as evidence for mycolic acid biosynthetic capacity:

**4′-Phosphopantetheinyl transferase (PPTase).** PPTases catalyze the post-translational attachment of the 4′-phosphopantetheine moiety to carrier proteins. In mycobacteria, PptT (Rv2794c) is the PPTase required for activating Pks13's ACP and PCP domains (sethiya2020mmpl3inhibitiona pages 3-5, marrakchi2014mycolicacidsstructures pages 8-9). However, PPTases are broadly distributed across bacteria, where they serve in fatty acid biosynthesis (via AcpS-type enzymes), siderophore biosynthesis, and nonribosomal peptide synthesis. In *P. putida* KT2440, the gene PP_1183 encodes a PPTase whose functional annotation supports siderophore carrier-protein activation, not mycolate-specific Pks13 activation.

**Malonyl-CoA:ACP transacylase (FabD).** FabD transfers the malonyl moiety from malonyl-CoA to an acyl carrier protein, providing the two-carbon extender unit for each round of FAS-II elongation (marrakchi2014mycolicacidsstructures pages 4-6, marrakchi2014mycolicacidsstructures pages 8-9). This activity is universal to type II fatty acid biosynthesis and is found in all bacteria that use a dissociable FAS-II system for membrane lipid synthesis, including Gram-negative organisms such as *Pseudomonas*, *Escherichia*, and others that do not produce mycolic acids.

**The case of *Pseudomonas putida* KT2440.** The KEGG pathway ppu00074 assigns PP_1183 and fabD to the mycolic acid biosynthesis map. However, *P. putida* KT2440 is a Gammaproteobacterium that belongs to an entirely different bacterial phylum from the Corynebacterineae (dover2004comparativecellwall pages 14-15). It lacks the core mycolate-specific genes—*pks13*, *fadD32*, *cmrA*, *mmpL3*, *kasA*, *kasB*, the *fbp* (Ag85) family, and the meromycolic modification methyltransferases—that are absolutely required to synthesize, reduce, transport, and deposit mycolic acids. The presence of generic PPTase and FabD activities constitutes a false-positive pathway assignment that should be flagged by any boundary-checking module.

### 2.3 Competing Definitions

Mycolic acids are formally defined as long-chain 2-alkyl, 3-hydroxy fatty acids. This chemical definition is satisfied by the simplest corynomycolic acids (~C32) of *Corynebacterium* as well as by the elaborate C60–C90 mycolic acids of *M. tuberculosis* (marrakchi2014mycolicacidsstructures pages 2-3, dover2004comparativecellwall pages 14-15). Some authors reserve "mycolic acids" for the longer-chain products and use "corynomycolic acids" for the shorter products of *Corynebacterium*, but the biosynthetic logic—Claisen condensation of two fatty acyl chains—is conserved across the entire suborder (marrakchi2014mycolicacidsstructures pages 8-9, dover2004comparativecellwall pages 14-15).

## 3. Mechanistic Overview

### 3.1 Step 1: Precursor Synthesis by FAS-I

Mycobacterial FAS-I (Fas, Rv2524c) is a eukaryotic-type multifunctional enzyme with seven catalytic domains that produces C16–C18 and C24–C26 acyl-CoA products from acetyl-CoA and malonyl-CoA (marrakchi2014mycolicacidsstructures pages 4-6, marrakchi2014mycolicacidsstructures pages 2-3). The C24–C26 products serve as the α-branch of the final mycolic acid, while the shorter products are fed into FAS-II for elongation into the meromycolate chain.

### 3.2 Step 2: Meromycolic Chain Elongation by FAS-II

The FAS-II system is a dissociable multi-enzyme complex responsible for extending acyl chains to C48–C62 meromycolate lengths through iterative two-carbon additions. Each elongation cycle involves five activities: (1) malonyl-CoA:ACP transacylase (MtFabD) transferring the malonyl unit to AcpM; (2) β-ketoacyl-ACP synthase (KasA for early elongation, KasB for later elongation) performing Claisen condensation; (3) β-ketoacyl-ACP reductase (MabA) reducing the β-keto group; (4) β-hydroxyacyl-ACP dehydratase (HadAB/HadBC heterodimers) removing water; and (5) enoyl-ACP reductase (InhA, the target of isoniazid) completing the cycle (williams2023molecularmechanismsof pages 1-2, marrakchi2014mycolicacidsstructures pages 4-6, marrakchi2014mycolicacidsstructures pages 8-9). The bridge between FAS-I and FAS-II is provided by the β-ketoacyl-ACP synthase III (MtFabH, Rv0533c), which initiates the FAS-II cycle by condensing acyl-CoA from FAS-I with malonyl-AcpM (marrakchi2014mycolicacidsstructures pages 8-9).

A model of three specialized FAS-II elongation complexes has been proposed: an initiation complex (with MtFabH), a type-I elongation complex (with KasA), and a type-II elongation complex (with KasB), each sharing a core of InhA, MabA, and MtFabD (marrakchi2014mycolicacidsstructures pages 8-9).

### 3.3 Step 3: Meromycolic Chain Modifications

The nascent meromycolic chain undergoes extensive post-synthetic modifications catalyzed by SAM-dependent methyltransferases and cyclopropane synthases. In *M. tuberculosis*, these include: CmaA1 and CmaA2 (cyclopropane synthases introducing distal and proximal cyclopropane rings), PcaA (proximal cis-cyclopropane synthase for α-mycolates), and MmaA1–MmaA4 (methyltransferases introducing methyl branches, methoxy groups, and keto functional groups) (sethiya2020mmpl3inhibitiona pages 3-5, marrakchi2014mycolicacidsstructures pages 3-4, dover2004comparativecellwall pages 15-16). Desaturases (DesA1, DesA2) introduce double bonds that serve as precursors for cyclopropanation in some species (dover2004comparativecellwall pages 15-16). These modifications generate the three major subclasses of *M. tuberculosis* mycolic acids: α-mycolates (dicyclopropanated), methoxy-mycolates (methoxy + cyclopropane), and keto-mycolates (keto + cyclopropane) (marrakchi2014mycolicacidsstructures pages 2-3, dover2004comparativecellwall pages 15-16).

### 3.4 Step 4: Activation and Condensation (FadD32–Pks13)

The fatty acyl-AMP ligase FadD32 (Rv3801c) activates the mature meromycolic chain by adenylation, producing a meromycolyl-AMP intermediate that is loaded onto the N-terminal ACP domain (PCP-like domain) of Pks13 (batt2020thethickwaxy pages 8-9, marrakchi2014mycolicacidsstructures pages 8-9, gavalda2014thepolyketidesynthase pages 1-3). Simultaneously, the C24–C26 α-branch is carboxylated by the acyl-CoA carboxylase AccD4, and the resulting carboxylated product is loaded onto the C-terminal ACP domain of Pks13 via its acyltransferase (AT) domain (marrakchi2014mycolicacidsstructures pages 8-9, batt2020thethickwaxy pages 8-9).

Pks13 (Rv3800c) is a type I polyketide synthase with five catalytic domains: a peptidyl carrier protein (PCP)-like domain, a ketoacyl synthase (KS) domain, an acyltransferase (AT) domain, an ACP domain, and a thioesterase (TE) domain (marrakchi2014mycolicacidsstructures pages 8-9, johnston2024cryoelectronmicroscopystructure pages 1-3). The KS domain catalyzes the Claisen-type condensation of the meromycolyl and carboxylated α-branch substrates, generating an α-alkyl β-ketoester intermediate. The TE domain then cleaves this product and directly transfers it onto trehalose, forming an α-alkyl β-ketoacyl trehalose intermediate (batt2020thethickwaxy pages 8-9, gavalda2014thepolyketidesynthase pages 7-8). Recent cryo-EM structural studies of the KS–AT di-domain core revealed a homodimeric architecture with the KS domain mediating dimerization and considerable conformational flexibility facilitating the multi-step condensation reaction (johnston2024cryoelectronmicroscopystructure pages 1-3).

Both PptT (the PPTase) and FadD32 are essential for loading substrates onto Pks13; their absence abolishes mycolate production (sethiya2020mmpl3inhibitiona pages 3-5, marrakchi2014mycolicacidsstructures pages 8-9).

### 3.5 Step 5: Reduction by CmrA

CmrA (Rv2509) reduces the β-keto group of the α-alkyl β-ketoacyl trehalose to the β-hydroxy state, generating mature trehalose monomycolate (TMM) (sethiya2020mmpl3inhibitiona pages 3-5, williams2023molecularmechanismsof pages 1-2, batt2020thethickwaxy pages 8-9, gavalda2014thepolyketidesynthase pages 7-8).

### 3.6 Step 6: Export by MmpL3

MmpL3 (Rv0206c) is the sole essential transporter responsible for flipping TMM across the inner membrane from the cytoplasmic face to the periplasmic space (williams2023molecularmechanismsof pages 1-2, rainczuk2020mtrpaputative pages 2-3). MmpL3 is a proton-motive-force-driven lipid transporter belonging to the resistance-nodulation-division (RND) superfamily, and its essentiality has made it a major drug target (williams2023molecularmechanismsof pages 1-2). Phosphorylation by the Ser/Thr kinase PknB negatively regulates MmpL3 function, providing a regulatory checkpoint on mycolate export (le2020theproteinkinase pages 35-35).

### 3.7 Step 7: Envelope Assembly by Ag85 Complex

In the periplasm, the antigen 85 (Ag85) mycolyltransferase complex—comprising Ag85A (FbpA), Ag85B (FbpB), and Ag85C (FbpC2)—transfers mycolate chains from TMM to two classes of acceptors: (i) the arabinan termini of arabinogalactan, forming mycolyl-arabinogalactan (mAG), and (ii) trehalose, forming trehalose dimycolate (TDM, cord factor) (hodges2018imagingmycobacterialgrowth pages 2-2, dover2004comparativecellwall pages 18-19, rainczuk2020mtrpaputative pages 2-3). The released free trehalose is recycled back into the cytoplasm via the LpqY-SugA-SugB-SugC ABC transporter, a process essential for virulence (batt2020thethickwaxy pages 8-9). The Ag85 enzymes show partial functional redundancy: FbpC2 appears to be the major contributor to arabinogalactan mycolylation, while individual knockouts show compensatory activity among the three enzymes (dover2004comparativecellwall pages 18-19).

## 4. Major Molecular Players and Active Assemblies

The following table summarizes the key enzymes, their boundary classification, and essentiality, distinguishing generic support enzymes from mycolate-specific boundary markers.

| Step/Module | Enzyme/Protein | Gene (M. tuberculosis) | Function | Essential? | Boundary Status |
|---|---|---|---|---|---|
| Carrier protein activation | AcpS | acpS (Rv2523c) | Housekeeping 4'-phosphopantetheinyl transferase that activates ACPs used in general fatty-acid metabolism; presence alone does **not** demonstrate mycolate synthesis capability | Likely essential for core lipid metabolism | **Generic/shared**; insufficient as a mycolate boundary marker (marrakchi2014mycolicacidsstructures pages 4-6, sethiya2020mmpl3inhibitiona pages 3-5, marrakchi2014mycolicacidsstructures pages 8-9) |
| Carrier protein activation | PptT | pptT (Rv2794c) | 4'-phosphopantetheinyl transferase that activates ACP/PCP domains of Pks13 and other lipid synthases; required for final mycolate condensation machinery | Essential in mycobacteria | **Mycolate-pathway relevant but not alone sufficient**; supports mycolate-specific assembly when coupled to Pks13/FadD32 (sethiya2020mmpl3inhibitiona pages 3-5, marrakchi2014mycolicacidsstructures pages 8-9) |
| Precursor supply | FabD / MtFabD | fabD (Rv2243) | Malonyl-CoA:ACP transacylase supplying malonyl-AcpM to FAS-II elongation cycles | Functionally essential for FAS-II | **Shared/core fatty-acid step**; not specific for mycolate production by itself (marrakchi2014mycolicacidsstructures pages 4-6, marrakchi2014mycolicacidsstructures pages 8-9) |
| Precursor supply | Acyl-CoA carboxylase | accA3-accD4 | Produces the carboxylated long-chain α-branch substrate used by Pks13 during mycolate condensation | Essential for mycolate condensation | **Partially mycolate-specific**; AccD4 is tightly linked to mycolate assembly (marrakchi2014mycolicacidsstructures pages 8-9, marrakchi2014mycolicacidsstructures pages 3-4) |
| Precursor supply | Acyl-CoA carboxylase | accA3-accD5 | Generates methylmalonyl-CoA pools for branched-chain lipid metabolism; adjacent to but distinct from core mycolate condensation chemistry | Essential for some lipid pathways, not the canonical condensase step | **Neighboring lipid metabolism, not a stand-alone mycolate marker** (marrakchi2014mycolicacidsstructures pages 3-4) |
| Precursor supply | Acyl-CoA carboxylase | accA3-accD6 | Produces malonyl-CoA for fatty-acid elongation and supports FAS-II precursor supply | Essential for core lipid metabolism | **Shared/supporting step**; not specific alone (marrakchi2014mycolicacidsstructures pages 3-4) |
| FAS-I product formation | Fas (FAS-I) | fas (Rv2524c) | Multifunctional FAS-I synthesizing C16-C18 and C24-C26 acyl-CoAs; the longer product provides the mycolate α-branch | Essential | **Context-dependent**: central lipid enzyme but obligatory for mycolate synthesis in mycolate producers (marrakchi2014mycolicacidsstructures pages 4-6, marrakchi2014mycolicacidsstructures pages 2-3) |
| FAS-II initiation | MtFabH | fabH (Rv0533c) | Connects FAS-I and FAS-II by transferring short acyl primers into the meromycolate elongation system | Essential or near-essential for pathway flux | **Mycolate-specific in mycobacteria** because it feeds meromycolate extension machinery (marrakchi2014mycolicacidsstructures pages 8-9, marrakchi2014mycolicacidsstructures pages 2-3) |
| FAS-II elongation | KasA | kasA (Rv2245) | β-ketoacyl-ACP synthase driving early/major meromycolate chain elongation | Essential | **Mycolate-specific core elongation** (sethiya2020mmpl3inhibitiona pages 3-5, williams2023molecularmechanismsof pages 1-2, dover2004comparativecellwall pages 15-16) |
| FAS-II elongation | KasB | kasB (Rv2246) | β-ketoacyl-ACP synthase associated with late elongation and full-length meromycolate production | Important; dispensability can vary by species/condition, but required for mature long-chain mycolates | **Mycolate-specific core elongation** (sethiya2020mmpl3inhibitiona pages 3-5, marrakchi2014mycolicacidsstructures pages 8-9, dover2004comparativecellwall pages 15-16) |
| FAS-II elongation | MabA | mabA (Rv1483) | β-ketoacyl-ACP reductase of the FAS-II cycle | Essential | **Mycolate-specific core elongation** in mycobacteria (williams2023molecularmechanismsof pages 1-2, marrakchi2014mycolicacidsstructures pages 4-6) |
| FAS-II elongation | HadAB / HadBC | hadA-hadB / hadB-hadC (Rv0635-Rv0636 / Rv0636-Rv0637) | β-hydroxyacyl-ACP dehydratase complexes of FAS-II; HadAB and HadBC act at different elongation stages | Essential for pathway integrity | **Mycolate-specific core elongation** (williams2023molecularmechanismsof pages 1-2, marrakchi2014mycolicacidsstructures pages 2-3) |
| FAS-II elongation | InhA | inhA (Rv1484) | trans-2-enoyl-ACP reductase completing each FAS-II elongation cycle; major drug target of isoniazid/ethionamide pathway | Essential | **Mycolate-specific core elongation** in mycobacteria (williams2023molecularmechanismsof pages 1-2, marrakchi2014mycolicacidsstructures pages 4-6) |
| Meromycolic modification | CmaA1 | cmaA1 (Rv3392c) | Cyclopropane synthase/methyltransferase introducing distal cis-cyclopropane modifications | Nonessential for viability, important for mature mycolate structure | **Accessory but mycolate-specific** (sethiya2020mmpl3inhibitiona pages 3-5, dover2004comparativecellwall pages 15-16) |
| Meromycolic modification | CmaA2 | cmaA2 (Rv0503c) | Cyclopropane synthase associated with proximal cyclopropanation and oxygenated mycolate maturation | Nonessential for viability, important for virulence-linked structure | **Accessory but mycolate-specific** (sethiya2020mmpl3inhibitiona pages 3-5, dover2004comparativecellwall pages 15-16) |
| Meromycolic modification | PcaA | pcaA (Rv0470c) | Proximal cis-cyclopropane synthase required for characteristic α-mycolate modification | Nonessential for viability, important for host interaction/virulence | **Accessory but mycolate-specific** (dover2004comparativecellwall pages 15-16) |
| Meromycolic modification | MmaA1-4 | mmaA1 (Rv0645c), mmaA2 (Rv0644c), mmaA3 (Rv0643c), mmaA4 (hma, Rv0642c) | SAM-dependent methyltransferases introducing double-bond, methoxy, keto, and cyclopropane-related oxygenated mycolate features | Generally nonessential for growth, critical for mature species-specific mycolate profiles | **Accessory but mycolate-specific** (sethiya2020mmpl3inhibitiona pages 3-5, marrakchi2014mycolicacidsstructures pages 3-4, dover2004comparativecellwall pages 15-16) |
| Chain activation | FadD32 | fadD32 (Rv3801c) | Fatty acyl-AMP ligase that adenylates the meromycolate and loads it onto the N-terminal carrier domain of Pks13 | Essential | **Obligate mycolate-specific boundary enzyme** (sethiya2020mmpl3inhibitiona pages 3-5, marrakchi2014mycolicacidsstructures pages 8-9, batt2020thethickwaxy pages 8-9, gavalda2014thepolyketidesynthase pages 1-3) |
| Claisen condensation | Pks13 | pks13 (Rv3800c) | Multi-domain condensase (PCP/KS/AT/ACP/TE) performing final Claisen-type coupling of meromycolate and α-branch; TE transfers product to trehalose | Essential | **Obligate mycolate-specific boundary enzyme** (williams2023molecularmechanismsof pages 1-2, marrakchi2014mycolicacidsstructures pages 8-9, batt2020thethickwaxy pages 8-9, gavalda2014thepolyketidesynthase pages 7-8, johnston2024cryoelectronmicroscopystructure pages 1-3) |
| Reduction | CmrA | cmrA (Rv2509) | Reduces the α-alkyl β-ketoacyl trehalose intermediate generated after Pks13 action to form mature trehalose monomycolate (TMM) | Required for mature mycolate production | **Obligate downstream mycolate-specific step** (sethiya2020mmpl3inhibitiona pages 3-5, le2020theproteinkinase pages 35-35, rainczuk2020mtrpaputative pages 2-3, batt2020thethickwaxy pages 8-9, gavalda2014thepolyketidesynthase pages 7-8) |
| TMM transport | MmpL3 | mmpL3 (Rv0206c) | Essential exporter/flippase transporting TMM across the inner membrane to the periplasm | Essential | **Obligate mycolate-specific envelope step** (williams2023molecularmechanismsof pages 1-2, le2020theproteinkinase pages 35-35, rainczuk2020mtrpaputative pages 2-3) |
| Cell wall transfer | Ag85A | fbpA (Rv3804c) | Periplasmic mycolyltransferase transferring mycolates from TMM to arabinogalactan and trehalose acceptors | Important; partial redundancy with Ag85B/C | **Mycolate-specific envelope assembly** (hodges2018imagingmycobacterialgrowth pages 2-2, dover2004comparativecellwall pages 18-19, rainczuk2020mtrpaputative pages 2-3) |
| Cell wall transfer | Ag85B | fbpB (Rv1886c) | Periplasmic mycolyltransferase producing TDM and mycolyl-arabinogalactan from TMM | Important; partial redundancy with Ag85A/C | **Mycolate-specific envelope assembly** (hodges2018imagingmycobacterialgrowth pages 2-2, dover2004comparativecellwall pages 18-19, rainczuk2020mtrpaputative pages 2-3) |
| Cell wall transfer | Ag85C | fbpC / fbpC2 (Rv0129c) | Periplasmic mycolyltransferase with major role in arabinogalactan mycolylation | Important; often strongest single Ag85 contributor to AG mycolylation | **Mycolate-specific envelope assembly** (dover2004comparativecellwall pages 18-19, rainczuk2020mtrpaputative pages 2-3) |


*Table: This table organizes the principal molecular players in mycolic acid biosynthesis by pathway step and explicitly separates generic support functions from obligate mycolate-specific machinery. It is useful for boundary curation because it shows why generic ACP activation or malonyl-ACP supply alone is not enough to infer a satisfiable mycolic acid pathway.*

## 5. Evolutionary and Cell-Biological Variation

### 5.1 Taxonomic Distribution

Mycolic acid biosynthesis is restricted to the suborder Corynebacterineae within the phylum Actinobacteria. The major mycolate-producing genera include *Mycobacterium*, *Corynebacterium*, *Nocardia*, *Rhodococcus*, *Gordonia*, *Tsukamurella*, *Dietzia*, and *Segniliparus* (marrakchi2014mycolicacidsstructures pages 2-3). The pathway is entirely absent from Gammaproteobacteria (including *Pseudomonas*), Firmicutes, Bacteroidetes, and all other phyla outside the Actinobacteria.

### 5.2 Lineage-Specific Variation

The most dramatic variation in the pathway concerns chain length, FAS-II utilization, and meromycolic modification complexity:

| Genus/Group | Total Mycolic Acid Chain Length | Alpha-branch Length | Meromycolic Chain Length | FAS-II Present? | Meromycolic Modifications | Number of Pks genes | Key Structural Differences |
|---|---|---|---|---|---|---|---|
| *Corynebacterium* | Typically ~C22–C36 corynomycolates; *C. diphtheriae* commonly ~C32 (marrakchi2014mycolicacidsstructures pages 2-3, dover2004comparativecellwall pages 14-15) | Usually derived from C8–C18 fatty acids (marrakchi2014mycolicacidsstructures pages 2-3) | Effectively absent as a long specialized mero-chain; products are formed by condensation of relatively short acyl-CoAs rather than a mycobacterial-style extended meromycolate (dover2004comparativecellwall pages 14-15) | No; *Corynebacterium* lacks the mycobacterial FAS-II system and behaves as a natural FAS-II-minus lineage (dover2004comparativecellwall pages 14-15) | Minimal; generally lacks the extensive oxygenation and cyclopropanation seen in mycobacteria (dover2004comparativecellwall pages 15-16, dover2004comparativecellwall pages 14-15) | Usually a single conserved mycolate-condensation *pks* gene (Pks13) rather than a large expanded family (marrakchi2014mycolicacidsstructures pages 8-9) | Short, simple corynomycolates; no long meromycolate branch; lower envelope complexity than mycobacteria (dover2004comparativecellwall pages 14-15) |
| *Rhodococcus* | ~C30–C54 (marrakchi2014mycolicacidsstructures pages 2-3) | Not well resolved in the retrieved evidence; shorter than mycobacterial alpha-branches overall (marrakchi2014mycolicacidsstructures pages 2-3) | Intermediate-length mero-chain relative to mycobacteria; longer than *Corynebacterium* but shorter/simpler than slow-growing mycobacteria (marrakchi2014mycolicacidsstructures pages 2-3) | Yes, inferred from distribution of FAS-II genes across Corynebacteriales outside *Corynebacterium* (marrakchi2014mycolicacidsstructures pages 2-3) | Moderate complexity; generally fewer elaborations than mycobacteria and lacking the full spectrum of methoxy/keto/cyclopropanated forms typical of slow growers (marrakchi2014mycolicacidsstructures pages 2-3) | More than the single conserved *pks13* of *Corynebacterium*, but less clearly expanded/characterized than in *Mycobacterium* in the retrieved evidence; at minimum retains conserved condensation machinery (marrakchi2014mycolicacidsstructures pages 8-9) | Intermediate envelope architecture and mycolate size; more complex than corynebacteria, less specialized than mycobacteria (marrakchi2014mycolicacidsstructures pages 2-3) |
| *Nocardia* | ~C44–C60 (marrakchi2014mycolicacidsstructures pages 2-3) | Typically derived from C12–C18 fatty acids (marrakchi2014mycolicacidsstructures pages 2-3) | Intermediate-to-long mero-chain, but generally less elaborated than in slow-growing mycobacteria (marrakchi2014mycolicacidsstructures pages 2-3) | Yes, consistent with FAS-II gene distribution in mycolate-producing Corynebacteriales outside *Corynebacterium* (marrakchi2014mycolicacidsstructures pages 2-3) | Moderate modifications; simpler than the highly oxygenated/cyclopropanated mycolates of slow-growing mycobacteria (marrakchi2014mycolicacidsstructures pages 2-3, dover2004comparativecellwall pages 15-16) | Conserved mycolate-condensation machinery including Pks13/FadD32 is expected across Corynebacteriales; broader *pks* expansion not established here (marrakchi2014mycolicacidsstructures pages 8-9) | Produces true mycolates longer than corynomycolates, with moderate structural diversity but not the extreme complexity of *M. tuberculosis* (marrakchi2014mycolicacidsstructures pages 2-3) |
| Slow-growing *Mycobacterium* | Commonly ~C60–C90; *M. tuberculosis* classes can extend to ~C84–C88 or higher depending on class definitions (sethiya2020mmpl3inhibitiona pages 3-5, marrakchi2014mycolicacidsstructures pages 2-3) | Usually C22–C26 alpha-branch, with *M. tuberculosis* often using C24–C26 precursors from FAS-I (sethiya2020mmpl3inhibitiona pages 3-5, marrakchi2014mycolicacidsstructures pages 8-9, johnston2024cryoelectronmicroscopystructure pages 1-3) | Typically C48–C62 meromycolate produced by FAS-II elongation before final condensation (williams2023molecularmechanismsof pages 1-2, marrakchi2014mycolicacidsstructures pages 8-9) | Yes; fully developed FAS-II system with MtFabH, KasA/KasB, MabA, HadAB/HadBC, InhA and related components (williams2023molecularmechanismsof pages 1-2, marrakchi2014mycolicacidsstructures pages 4-6, marrakchi2014mycolicacidsstructures pages 8-9) | High complexity: desaturation, cis/trans cyclopropanation, keto and methoxy modifications; fast growers retain more unsaturation, while slow growers emphasize cyclopropanation and oxygenated forms (dover2004comparativecellwall pages 15-16) | Large expanded *pks* repertoire in addition to essential *pks13*; *M. tuberculosis* has >18 type-I *pks* genes overall (marrakchi2014mycolicacidsstructures pages 8-9) | Longest and most complex mycolates; specialized outer membrane, extensive modification machinery, and dedicated export/transfer systems (MmpL3, Ag85) (batt2020thethickwaxy pages 8-9, rainczuk2020mtrpaputative pages 2-3, marrakchi2014mycolicacidsstructures pages 8-9) |
| *Pseudomonas putida* KT2440 | None; does not produce mycolic acids (dover2004comparativecellwall pages 14-15) | Not applicable (dover2004comparativecellwall pages 14-15) | Not applicable (dover2004comparativecellwall pages 14-15) | No mycolate-specific FAS-II module; generic fatty-acid metabolism may be present, but the mycolate pathway is absent (dover2004comparativecellwall pages 14-15) | None (dover2004comparativecellwall pages 14-15) | Lacks the conserved mycolate-condensation system required for mycolic acid synthesis; KEGG assignment is a false positive boundary call when based only on generic support enzymes such as PPTase/FabD (dover2004comparativecellwall pages 14-15, marrakchi2014mycolicacidsstructures pages 8-9) | Gram-negative gammaproteobacterium with no Corynebacteriales-type mycolate envelope; presence of generic ACP activation or malonyl-ACP formation steps does not imply a satisfiable mycolic acid pathway (dover2004comparativecellwall pages 14-15, marrakchi2014mycolicacidsstructures pages 8-9) |


*Table: This table compares the organization and outputs of mycolic acid biosynthesis across major lineages, highlighting where the pathway is complete, simplified, or absent. It is useful for defining the taxonomic boundary of the module and for flagging false-positive annotations such as in *Pseudomonas putida* KT2440.*

*Corynebacterium* represents the simplest mycolate-producing lineage: it lacks the complete FAS-II system and produces short corynomycolates (~C32) by Claisen condensation of two relatively short acyl-CoA substrates (dover2004comparativecellwall pages 14-15). *C. diphtheriae* has been described as a "natural FAS-II mutant," retaining only the Pks13/FadD32 condensation machinery without the meromycolate elongation and modification enzymes (dover2004comparativecellwall pages 14-15). In contrast, *Mycobacterium* species possess the full FAS-II elongation system and an expanded repertoire of modification enzymes, producing the longest and most complex mycolates (marrakchi2014mycolicacidsstructures pages 2-3).

### 5.3 Species-Level Variation Within Mycobacterium

Slow-growing pathogenic mycobacteria (e.g., *M. tuberculosis*) produce extensively cyclopropanated and oxygenated mycolic acids (α-, methoxy-, and keto-mycolates), while fast-growing species (e.g., *M. smegmatis*) produce mycolic acids with a higher proportion of unsaturated rather than cyclopropanated forms (dover2004comparativecellwall pages 15-16). This variation reflects differences in the activity and expression of the methyltransferase/cyclopropane synthase family and is associated with virulence and persistence phenotypes.

### 5.4 Conservation of Core Condensation Machinery

Despite the wide variation in chain length and modifications, the Pks13/FadD32 condensation cassette is universally conserved across all mycolate-producing genera. The genetic organization of the *fadD32-pks13* locus is syntenic across *M. tuberculosis*, *M. leprae*, *C. glutamicum*, and *C. diphtheriae* (marrakchi2014mycolicacidsstructures pages 8-9). While *M. tuberculosis* encodes more than 18 type-I pks genes, *Corynebacterium* species typically possess only the single essential *pks13* gene (marrakchi2014mycolicacidsstructures pages 8-9). This conservation makes the Pks13/FadD32 module the most reliable single marker for the presence of a genuine mycolic acid biosynthesis pathway.

### 5.5 Evolution of the Pathway

Phylogenetic analysis of mycolic acid biosynthesis genes reveals that the condensation machinery (Pks13, FadD32) and the core FAS-II elongation enzymes represent an ancient feature of the Corynebacterineae lineage, with subsequent elaboration through gene duplication and functional diversification (jamet2015evolutionofmycolic pages 2-10). The meromycolic modification enzymes (CmaA, PcaA, MmaA family) appear to be later elaborations, with their expansion and diversification correlating with the emergence of pathogenic mycobacterial lineages. The deep conservation of the fadD32-pks13 condensation module, even in lineages like *Corynebacterium* that lack FAS-II, suggests that the condensation step is the ancestral core of the pathway, and that FAS-II elongation and subsequent modifications were layered on top during the evolutionary diversification of the suborder (marrakchi2014mycolicacidsstructures pages 2-3, marrakchi2014mycolicacidsstructures pages 8-9).

## 6. Constraints, Dependencies, and Failure Modes

### 6.1 Obligatory Order of Steps

The pathway has a strict temporal and logical order: (i) FAS-I must produce the initial acyl-CoA pools; (ii) FAS-II elongation must precede meromycolic modifications (if FAS-II is present); (iii) modifications occur after or during later FAS-II cycles but before condensation; (iv) FadD32 activation of the meromycolate must precede Pks13 condensation; (v) CmrA reduction follows Pks13 condensation; (vi) MmpL3 transport must precede Ag85-mediated cell wall assembly (sethiya2020mmpl3inhibitiona pages 3-5, williams2023molecularmechanismsof pages 1-2, batt2020thethickwaxy pages 8-9, gavalda2014thepolyketidesynthase pages 7-8).

### 6.2 Mutually Exclusive and Compartment-Specific Events

TMM synthesis (cytoplasmic) and mycolate transfer to arabinogalactan (periplasmic) are compartmentally segregated, with MmpL3 serving as the obligatory connection between these two spaces (williams2023molecularmechanismsof pages 1-2, rainczuk2020mtrpaputative pages 2-3). Disruption of MmpL3 causes lethal accumulation of TMM in the inner membrane (williams2023molecularmechanismsof pages 1-2). The TE domain of Pks13 was demonstrated to directly transfer its condensation product onto trehalose before CmrA-mediated reduction, establishing a strict coupling between condensation and trehalose esterification (gavalda2014thepolyketidesynthase pages 7-8).

### 6.3 Drug-Induced Pathway Disruption

Isoniazid (targeting InhA) blocks FAS-II elongation; ethambutol (targeting arabinan polymerization) causes TMM/TDM accumulation due to loss of the arabinogalactan acceptor for mycolate transfer (dover2004comparativecellwall pages 18-19). These failure modes demonstrate the tight coupling between meromycolic chain supply and cell wall assembly.

### 6.4 Regulatory Constraints

PknB-mediated phosphorylation of MmpL3 and other biosynthetic enzymes provides a kinase-dependent regulatory layer that modulates mycolic acid production in response to growth conditions (le2020theproteinkinase pages 35-35). Starvation conditions alter the expression of mycolic acid biosynthesis genes, including coordinated changes in FAS-II components and modification enzymes (jamet2015evolutionofmycolic pages 2-10).

### 6.5 Boundary Rule

The minimum gene set required to infer a satisfiable mycolic acid pathway in a genome should include: *pks13* (or orthologue), *fadD32*, *cmrA*, *mmpL3* (or a functional equivalent for TMM transport), and at least one *fbp* (Ag85) mycolyltransferase. For organisms with long-chain mycolic acids, the FAS-II-specific genes (*kasA*, *kasB*, *inhA*, *mabA*, *hadABC*) must also be present. The presence of generic support enzymes (PPTase, FabD) alone—as in *P. putida* KT2440—is categorically insufficient.

## 7. Controversies and Open Questions

**7.1 Condensation mechanism in Corynebacterium.** Whether corynomycolate condensation proceeds via a decarboxylative or non-decarboxylative Claisen mechanism remains debated. Evidence from *C. matruchotti* using deuterium-labeled substrates suggested retention of 2H labels at positions inconsistent with simple decarboxylation, although this could reflect enzyme active-site retention rather than a fundamentally different mechanism (dover2004comparativecellwall pages 18-19).

**7.2 Pks13 structural dynamics.** Although recent cryo-EM and SAXS studies have revealed the Pks13 di-domain core architecture, the full-length enzyme's conformational dynamics during the catalytic cycle—particularly how the two ACP domains shuttle substrates between domains—remain incompletely understood (johnston2024cryoelectronmicroscopystructure pages 1-3). The pH-dependent monomer-dimer equilibrium adds further complexity.

**7.3 Regulation of meromycolic modifications.** The temporal order and spatial coordination of meromycolic chain modifications during FAS-II elongation are not fully resolved. Whether modifications occur during specific FAS-II elongation cycles or on the completed meromycolate chain before condensation remains an open question (williams2023molecularmechanismsof pages 1-2, dover2004comparativecellwall pages 15-16).

**7.4 Cross-talk between FAS-II and other lipid pathways.** The discovery that KasA interacts with PpsB and PpsD (polyketide modules involved in PDIM biosynthesis) suggests that lipid intermediates may be shared between the mycolic acid and phthiocerol dimycocerosate pathways, potentially increasing lipid diversity but complicating pathway boundary definitions.

**7.5 KEGG pathway annotation challenges.** The KEGG map for mycolic acid biosynthesis (M00074/ko00073) includes generic steps (PPTase activation, malonyl-ACP formation) that can match genes in organisms entirely lacking mycolate production capacity. This creates false-positive pathway assignments for organisms such as *P. putida* KT2440, where only PP_1183 (a PPTase likely functioning in siderophore or NRPS activation) and *fabD* (a housekeeping malonyl-CoA:ACP transacylase) match the map. Current UniProt/GOA evidence for these genes supports siderophore carrier-protein activation and type II fatty acid biosynthesis, respectively, not mycolic acid biosynthesis (dover2004comparativecellwall pages 14-15).

## 8. Key References

- Marrakchi H, Lanéelle MA, Daffé M. Mycolic acids: structures, biosynthesis, and beyond. *Chemistry & Biology*. 2014;21(1):67-85. doi:10.1016/j.chembiol.2013.11.011 (marrakchi2014mycolicacidsstructures pages 4-6, marrakchi2014mycolicacidsstructures pages 8-9, marrakchi2014mycolicacidsstructures pages 3-4, marrakchi2014mycolicacidsstructures pages 2-3)
- Dover LG et al. Comparative cell wall core biosynthesis in the mycolated pathogens, *Mycobacterium tuberculosis* and *Corynebacterium diphtheriae*. *FEMS Microbiology Reviews*. 2004;28(2):225-250. doi:10.1016/j.femsre.2003.10.001 (dover2004comparativecellwall pages 15-16, dover2004comparativecellwall pages 14-15, dover2004comparativecellwall pages 18-19)
- Sethiya JP et al. MmpL3 inhibition: a new approach to treat nontuberculous mycobacterial infections. *Int J Mol Sci*. 2020;21:6202. doi:10.3390/ijms21176202 (sethiya2020mmpl3inhibitiona pages 3-5)
- Williams JT, Abramovitch RB. Molecular mechanisms of MmpL3 function and inhibition. *Microbial Drug Resistance*. 2023;29:190-212. doi:10.1089/mdr.2021.0424 (williams2023molecularmechanismsof pages 1-2)
- Batt SM, Minnikin DE, Besra GS. The thick waxy coat of mycobacteria, a protective layer against antibiotics and the host's immune system. *Biochem J*. 2020;477:1983-2006. doi:10.1042/bcj20200194 (batt2020thethickwaxy pages 8-9)
- Johnston HE et al. Cryo-electron microscopy structure of the di-domain core of *Mycobacterium tuberculosis* polyketide synthase 13. *Microbiology*. 2024;170. doi:10.1099/mic.0.001505 (johnston2024cryoelectronmicroscopystructure pages 1-3)
- Gavalda S et al. The polyketide synthase Pks13 catalyzes a novel mechanism of lipid transfer in mycobacteria. *Chemistry & Biology*. 2014;21(12):1660-9. doi:10.1016/j.chembiol.2014.10.011 (gavalda2014thepolyketidesynthase pages 7-8, gavalda2014thepolyketidesynthase pages 1-3)
- Le NH et al. The protein kinase PknB negatively regulates biosynthesis and trafficking of mycolic acids in mycobacteria. *J Lipid Res*. 2020;61:1180-1191. doi:10.1194/jlr.ra120000747 (le2020theproteinkinase pages 35-35)
- Jamet S et al. Evolution of mycolic acid biosynthesis genes and their regulation during starvation in *Mycobacterium tuberculosis*. *J Bacteriol*. 2015;197:3797-3811. doi:10.1128/jb.00433-15 (jamet2015evolutionofmycolic pages 2-10)
- Hodges HL et al. Imaging mycobacterial growth and division with a fluorogenic probe. *PNAS*. 2018;115:5271-5276. doi:10.1073/pnas.1720996115 (hodges2018imagingmycobacterialgrowth pages 2-2)
- Rainczuk AK et al. MtrP, a putative methyltransferase in Corynebacteria, is required for optimal membrane transport of trehalose mycolates. *J Biol Chem*. 2020;295:6108-6119. doi:10.1074/jbc.ra119.011688 (rainczuk2020mtrpaputative pages 2-3)


References

1. (marrakchi2014mycolicacidsstructures pages 2-3): Hedia Marrakchi, Marie-Antoinette Lanéelle, and Mamadou Daffé. Mycolic acids: structures, biosynthesis, and beyond. Chemistry & biology, 21 1:67-85, Jan 2014. URL: https://doi.org/10.1016/j.chembiol.2013.11.011, doi:10.1016/j.chembiol.2013.11.011. This article has 848 citations.

2. (sethiya2020mmpl3inhibitiona pages 3-5): Jigar P. Sethiya, Melanie A. Sowards, Mary Jackson, and Elton Jeffrey North. Mmpl3 inhibition: a new approach to treat nontuberculous mycobacterial infections. International Journal of Molecular Sciences, 21:6202, Aug 2020. URL: https://doi.org/10.3390/ijms21176202, doi:10.3390/ijms21176202. This article has 46 citations.

3. (williams2023molecularmechanismsof pages 1-2): John T. Williams and Robert B. Abramovitch. Molecular mechanisms of mmpl3 function and inhibition. May 2023. URL: https://doi.org/10.1089/mdr.2021.0424, doi:10.1089/mdr.2021.0424. This article has 35 citations and is from a peer-reviewed journal.

4. (batt2020thethickwaxy pages 8-9): Sarah M. Batt, David E. Minnikin, and Gurdyal S. Besra. The thick waxy coat of mycobacteria, a protective layer against antibiotics and the host's immune system. Biochemical Journal, 477:1983-2006, May 2020. URL: https://doi.org/10.1042/bcj20200194, doi:10.1042/bcj20200194. This article has 209 citations and is from a domain leading peer-reviewed journal.

5. (gavalda2014thepolyketidesynthase pages 7-8): Sabine Gavalda, Fabienne Bardou, Françoise Laval, Cécile Bon, Wladimir Malaga, Christian Chalut, Christophe Guilhot, Lionel Mourey, Mamadou Daffé, and Annaïk Quémard. The polyketide synthase pks13 catalyzes a novel mechanism of lipid transfer in mycobacteria. Chemistry & biology, 21 12:1660-9, Dec 2014. URL: https://doi.org/10.1016/j.chembiol.2014.10.011, doi:10.1016/j.chembiol.2014.10.011. This article has 100 citations.

6. (marrakchi2014mycolicacidsstructures pages 8-9): Hedia Marrakchi, Marie-Antoinette Lanéelle, and Mamadou Daffé. Mycolic acids: structures, biosynthesis, and beyond. Chemistry & biology, 21 1:67-85, Jan 2014. URL: https://doi.org/10.1016/j.chembiol.2013.11.011, doi:10.1016/j.chembiol.2013.11.011. This article has 848 citations.

7. (marrakchi2014mycolicacidsstructures pages 4-6): Hedia Marrakchi, Marie-Antoinette Lanéelle, and Mamadou Daffé. Mycolic acids: structures, biosynthesis, and beyond. Chemistry & biology, 21 1:67-85, Jan 2014. URL: https://doi.org/10.1016/j.chembiol.2013.11.011, doi:10.1016/j.chembiol.2013.11.011. This article has 848 citations.

8. (dover2004comparativecellwall pages 14-15): Lynn G. Dover, Ana M. Cerdeño-Tárraga, Mark J. Pallen, Julian Parkhill, and Gurdyal S. Besra. Comparative cell wall core biosynthesis in the mycolated pathogens, mycobacterium tuberculosis and corynebacterium diphtheriae. FEMS microbiology reviews, 28 2:225-50, May 2004. URL: https://doi.org/10.1016/j.femsre.2003.10.001, doi:10.1016/j.femsre.2003.10.001. This article has 170 citations and is from a domain leading peer-reviewed journal.

9. (marrakchi2014mycolicacidsstructures pages 3-4): Hedia Marrakchi, Marie-Antoinette Lanéelle, and Mamadou Daffé. Mycolic acids: structures, biosynthesis, and beyond. Chemistry & biology, 21 1:67-85, Jan 2014. URL: https://doi.org/10.1016/j.chembiol.2013.11.011, doi:10.1016/j.chembiol.2013.11.011. This article has 848 citations.

10. (dover2004comparativecellwall pages 15-16): Lynn G. Dover, Ana M. Cerdeño-Tárraga, Mark J. Pallen, Julian Parkhill, and Gurdyal S. Besra. Comparative cell wall core biosynthesis in the mycolated pathogens, mycobacterium tuberculosis and corynebacterium diphtheriae. FEMS microbiology reviews, 28 2:225-50, May 2004. URL: https://doi.org/10.1016/j.femsre.2003.10.001, doi:10.1016/j.femsre.2003.10.001. This article has 170 citations and is from a domain leading peer-reviewed journal.

11. (gavalda2014thepolyketidesynthase pages 1-3): Sabine Gavalda, Fabienne Bardou, Françoise Laval, Cécile Bon, Wladimir Malaga, Christian Chalut, Christophe Guilhot, Lionel Mourey, Mamadou Daffé, and Annaïk Quémard. The polyketide synthase pks13 catalyzes a novel mechanism of lipid transfer in mycobacteria. Chemistry & biology, 21 12:1660-9, Dec 2014. URL: https://doi.org/10.1016/j.chembiol.2014.10.011, doi:10.1016/j.chembiol.2014.10.011. This article has 100 citations.

12. (johnston2024cryoelectronmicroscopystructure pages 1-3): Hannah E. Johnston, Sarah M. Batt, Alistair K. Brown, Christos G. Savva, Gurdyal S. Besra, and Klaus Fütterer. Cryo-electron microscopy structure of the di-domain core of mycobacterium tuberculosis polyketide synthase 13, essential for mycobacterial mycolic acid synthesis. Oct 2024. URL: https://doi.org/10.1099/mic.0.001505, doi:10.1099/mic.0.001505. This article has 3 citations and is from a peer-reviewed journal.

13. (rainczuk2020mtrpaputative pages 2-3): Arek K. Rainczuk, Stephan Klatt, Yoshiki Yamaryo-Botté, Rajini Brammananth, Malcolm J. McConville, Ross L. Coppel, and Paul K. Crellin. Mtrp, a putative methyltransferase in corynebacteria, is required for optimal membrane transport of trehalose mycolates. Journal of Biological Chemistry, 295:6108-6119, May 2020. URL: https://doi.org/10.1074/jbc.ra119.011688, doi:10.1074/jbc.ra119.011688. This article has 18 citations and is from a domain leading peer-reviewed journal.

14. (le2020theproteinkinase pages 35-35): Nguyen-Hung Le, Marie Locard-Paulet, Alexandre Stella, Nicolas Tomas, Virginie Molle, Odile Burlet-Schiltz, Mamadou Daffé, and Hedia Marrakchi. The protein kinase pknb negatively regulates biosynthesis and trafficking of mycolic acids in mycobacteria. Journal of Lipid Research, 61:1180-1191, Aug 2020. URL: https://doi.org/10.1194/jlr.ra120000747, doi:10.1194/jlr.ra120000747. This article has 25 citations and is from a peer-reviewed journal.

15. (hodges2018imagingmycobacterialgrowth pages 2-2): Heather L. Hodges, Robert A. Brown, John A. Crooks, Douglas B. Weibel, and Laura L. Kiessling. Imaging mycobacterial growth and division with a fluorogenic probe. Proceedings of the National Academy of Sciences, 115:5271-5276, Apr 2018. URL: https://doi.org/10.1073/pnas.1720996115, doi:10.1073/pnas.1720996115. This article has 113 citations and is from a highest quality peer-reviewed journal.

16. (dover2004comparativecellwall pages 18-19): Lynn G. Dover, Ana M. Cerdeño-Tárraga, Mark J. Pallen, Julian Parkhill, and Gurdyal S. Besra. Comparative cell wall core biosynthesis in the mycolated pathogens, mycobacterium tuberculosis and corynebacterium diphtheriae. FEMS microbiology reviews, 28 2:225-50, May 2004. URL: https://doi.org/10.1016/j.femsre.2003.10.001, doi:10.1016/j.femsre.2003.10.001. This article has 170 citations and is from a domain leading peer-reviewed journal.

17. (jamet2015evolutionofmycolic pages 2-10): Stevie Jamet, Yves Quentin, Coralie Coudray, Pauline Texier, Françoise Laval, Mamadou Daffé, Gwennaele Fichant, and Kaymeuang Cam. Evolution of mycolic acid biosynthesis genes and their regulation during starvation in mycobacterium tuberculosis. Journal of Bacteriology, 197:3797-3811, Dec 2015. URL: https://doi.org/10.1128/jb.00433-15, doi:10.1128/jb.00433-15. This article has 35 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](mycolic_acid_biosynthesis-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](mycolic_acid_biosynthesis-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. marrakchi2014mycolicacidsstructures pages 2-3
2. dover2004comparativecellwall pages 14-15
3. marrakchi2014mycolicacidsstructures pages 8-9
4. dover2004comparativecellwall pages 15-16
5. johnston2024cryoelectronmicroscopystructure pages 1-3
6. williams2023molecularmechanismsof pages 1-2
7. le2020theproteinkinase pages 35-35
8. batt2020thethickwaxy pages 8-9
9. dover2004comparativecellwall pages 18-19
10. marrakchi2014mycolicacidsstructures pages 3-4
11. jamet2015evolutionofmycolic pages 2-10
12. gavalda2014thepolyketidesynthase pages 7-8
13. hodges2018imagingmycobacterialgrowth pages 2-2
14. rainczuk2020mtrpaputative pages 2-3
15. marrakchi2014mycolicacidsstructures pages 4-6
16. gavalda2014thepolyketidesynthase pages 1-3
17. acyl-carrier-protein
18. https://doi.org/10.1016/j.chembiol.2013.11.011,
19. https://doi.org/10.3390/ijms21176202,
20. https://doi.org/10.1089/mdr.2021.0424,
21. https://doi.org/10.1042/bcj20200194,
22. https://doi.org/10.1016/j.chembiol.2014.10.011,
23. https://doi.org/10.1016/j.femsre.2003.10.001,
24. https://doi.org/10.1099/mic.0.001505,
25. https://doi.org/10.1074/jbc.ra119.011688,
26. https://doi.org/10.1194/jlr.ra120000747,
27. https://doi.org/10.1073/pnas.1720996115,
28. https://doi.org/10.1128/jb.00433-15,