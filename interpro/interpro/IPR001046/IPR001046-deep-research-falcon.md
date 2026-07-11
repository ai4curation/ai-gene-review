---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-20T04:52:21.263426'
end_time: '2026-06-20T05:08:44.370169'
duration_seconds: 983.11
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: IPR001046
  interpro_name: NRAMP family
  interpro_short_name: NRAMP_fam
  interpro_type: family
  interpro_integrated: None (top-level entry)
  member_databases: 'MF_00221 (hamap: Divalent metal cation transporter MntH [mntH]);
    PF01566 (pfam: Natural resistance-associated macrophage protein-like); TIGR01197
    (ncbifam: metal ion transporter, metal ion (Mn2+/Fe2+) transporter (Nramp) family);
    PTHR11706 (panther: SOLUTE CARRIER PROTEIN FAMILY 11 MEMBER); PR00447 (prints:
    NATRESASSCMP)'
  n_proteins: '31226'
  n_taxa: '24403'
  n_subfamilies: '0'
  interpro2go_terms: GO:0046873 metal ion transmembrane transporter activity [F];
    GO:0030001 metal ion transport [P]; GO:0016020 membrane [C]
  interpro_description: The natural resistance-associated macrophage protein (NRAMP)
    family consists of animal NRAMP1, NRAMP2 (DMT1), yeast proteins Smf1 and Smf2
    and bacterial homologues such as divalent metal cation transporters (MntH) [[cite:PUB00005530],
    [cite:PUB00004854], [cite:PUB00003001], [cite:PUB00101161], [cite:PUB00101162],
    [cite:PUB00101160], [cite:PUB00101163]]. The NRAMP family includes functional
    related proteins defined by a conserved hydrophobic core of ten transmembrane
    domains. These membrane proteins are divalent cation transporters which have a
    high degree of sequence conservation, particularly, the residues contributing
    to ion interaction are strongly conserved (DPGN and MPH motifs) [[cite:PUB00101161],
    [cite:PUB00101162]]. NRAMP1 is an integral membrane protein expressed exclusively
    in cells of the immune system and is recruited to the membrane of a phagosome
    upon phagocytosis, where it plays an essential role in host defense against pathogens.
    Mutations in NRAMP1 may genetically predispose an individual to susceptibility
    to diseases including leprosy and tuberculosis . NRAMP2 (DMT1) is a multiple divalent
    cation transporter broadly expressed in the duodenum, kidney, brain, testis and
    placenta. It transports Fe2+, Mn2+ and Cd+2, whereas Zn2+ is a poor substrate.
    Ca+2 and Mg+2 are not transported, which is important because their high concentrations
    in duodenum, where NRAMP2 is expressed at high levels, would interfere with the
    absorption of Fe2+ . It is the major transferrin ...
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 37
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: IPR001046-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: IPR001046-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** IPR001046
- **Name:** NRAMP family
- **Short name:** NRAMP_fam
- **Entry type:** family
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** MF_00221 (hamap: Divalent metal cation transporter MntH [mntH]); PF01566 (pfam: Natural resistance-associated macrophage protein-like); TIGR01197 (ncbifam: metal ion transporter, metal ion (Mn2+/Fe2+) transporter (Nramp) family); PTHR11706 (panther: SOLUTE CARRIER PROTEIN FAMILY 11 MEMBER); PR00447 (prints: NATRESASSCMP)
- **Scale:** 31226 proteins across 24403 taxa, 0 subfamilies
- **Current InterPro2GO terms (the mappings under review):** GO:0046873 metal ion transmembrane transporter activity [F]; GO:0030001 metal ion transport [P]; GO:0016020 membrane [C]
- **InterPro description:** The natural resistance-associated macrophage protein (NRAMP) family consists of animal NRAMP1, NRAMP2 (DMT1), yeast proteins Smf1 and Smf2 and bacterial homologues such as divalent metal cation transporters (MntH) [[cite:PUB00005530], [cite:PUB00004854], [cite:PUB00003001], [cite:PUB00101161], [cite:PUB00101162], [cite:PUB00101160], [cite:PUB00101163]]. The NRAMP family includes functional related proteins defined by a conserved hydrophobic core of ten transmembrane domains. These membrane proteins are divalent cation transporters which have a high degree of sequence conservation, particularly, the residues contributing to ion interaction are strongly conserved (DPGN and MPH motifs) [[cite:PUB00101161], [cite:PUB00101162]]. NRAMP1 is an integral membrane protein expressed exclusively in cells of the immune system and is recruited to the membrane of a phagosome upon phagocytosis, where it plays an essential role in host defense against pathogens. Mutations in NRAMP1 may genetically predispose an individual to susceptibility to diseases including leprosy and tuberculosis . NRAMP2 (DMT1) is a multiple divalent cation transporter broadly expressed in the duodenum, kidney, brain, testis and placenta. It transports Fe2+, Mn2+ and Cd+2, whereas Zn2+ is a poor substrate. Ca+2 and Mg+2 are not transported, which is important because their high concentrations in duodenum, where NRAMP2 is expressed at high levels, would interfere with the absorption of Fe2+ . It is the major transferrin ...

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**IPR001046 (NRAMP family)**, structured to support GO annotation review.

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
- **Accession:** IPR001046
- **Name:** NRAMP family
- **Short name:** NRAMP_fam
- **Entry type:** family
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** MF_00221 (hamap: Divalent metal cation transporter MntH [mntH]); PF01566 (pfam: Natural resistance-associated macrophage protein-like); TIGR01197 (ncbifam: metal ion transporter, metal ion (Mn2+/Fe2+) transporter (Nramp) family); PTHR11706 (panther: SOLUTE CARRIER PROTEIN FAMILY 11 MEMBER); PR00447 (prints: NATRESASSCMP)
- **Scale:** 31226 proteins across 24403 taxa, 0 subfamilies
- **Current InterPro2GO terms (the mappings under review):** GO:0046873 metal ion transmembrane transporter activity [F]; GO:0030001 metal ion transport [P]; GO:0016020 membrane [C]
- **InterPro description:** The natural resistance-associated macrophage protein (NRAMP) family consists of animal NRAMP1, NRAMP2 (DMT1), yeast proteins Smf1 and Smf2 and bacterial homologues such as divalent metal cation transporters (MntH) [[cite:PUB00005530], [cite:PUB00004854], [cite:PUB00003001], [cite:PUB00101161], [cite:PUB00101162], [cite:PUB00101160], [cite:PUB00101163]]. The NRAMP family includes functional related proteins defined by a conserved hydrophobic core of ten transmembrane domains. These membrane proteins are divalent cation transporters which have a high degree of sequence conservation, particularly, the residues contributing to ion interaction are strongly conserved (DPGN and MPH motifs) [[cite:PUB00101161], [cite:PUB00101162]]. NRAMP1 is an integral membrane protein expressed exclusively in cells of the immune system and is recruited to the membrane of a phagosome upon phagocytosis, where it plays an essential role in host defense against pathogens. Mutations in NRAMP1 may genetically predispose an individual to susceptibility to diseases including leprosy and tuberculosis . NRAMP2 (DMT1) is a multiple divalent cation transporter broadly expressed in the duodenum, kidney, brain, testis and placenta. It transports Fe2+, Mn2+ and Cd+2, whereas Zn2+ is a poor substrate. Ca+2 and Mg+2 are not transported, which is important because their high concentrations in duodenum, where NRAMP2 is expressed at high levels, would interfere with the absorption of Fe2+ . It is the major transferrin ...

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**IPR001046 (NRAMP family)**, structured to support GO annotation review.

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


# Comprehensive Research Report: InterPro IPR001046 (NRAMP family) – GO Annotation Review

## Executive Summary

IPR001046 represents the **NRAMP (Natural Resistance-Associated Macrophage Protein) family** / **SLC11 (Solute Carrier family 11)**, a globally distributed family of transition metal transporters spanning bacteria, archaea, and all eukaryotic supergroups. This report evaluates whether the three current InterPro2GO mappings—**GO:0046873** (metal ion transmembrane transporter activity), **GO:0030001** (metal ion transport), and **GO:0016020** (membrane)—are appropriate for all ~31,000 proteins matching this signature. Based on comprehensive analysis of recent structural, functional, phylogenetic, and mechanistic literature (2015–2025), the family is functionally homogeneous at a very broad level (all are integral membrane metal transporters), but displays critical **subfamily-level divergence** in substrate specificity, mechanism details, and subcellular localization that makes overly specific GO terms inappropriate at the family level.

**Verdict**: The current InterPro2GO mappings are **partially appropriate but suboptimal**. The molecular function and biological process terms are acceptable but highly generic. The cellular component term "membrane" is trivially true but informationally useless. **Recommendation**: **ACCEPT** GO:0046873 and GO:0030001 as broad family-level annotations; **KEEP_AS_NON_CORE** GO:0016020 (membrane) due to extreme genericity; do **not** add more specific terms (e.g., iron transport, phagosomal membrane) at this top-level family entry, as they would over-annotate many subfamilies and taxa.

---

## 1. Family Definition and Biochemistry

### 1.1 Fold Architecture

The NRAMP/SLC11 family adopts the **LeuT fold**, an ancient structural paradigm characteristic of the Amino acid-Polyamine-organoCation (APC) superfamily of secondary active transporters (cellier2016evolutionaryanalysisof pages 1-4, cellier2016evolutionaryanalysisof pages 4-6). This fold comprises a hydrophobic core of **10 transmembrane segments (TMs)** organized as two topologically inverted five-helix repeats (protomers); TM1–5 and TM6–10 are pseudo-symmetric but evolutionarily diverged (cellier2016evolutionaryanalysisof pages 1-4, liziczai2025structuralbasisfor pages 6-8, liziczai2025structuralbasisfor pages 4-6). Mammalian NRAMP proteins (human DMT1/SLC11A2 and NRAMP1/SLC11A1) possess **12 TMs**, with an additional C-terminal helix (TM12) and N-terminal extensions absent in many bacterial homologs (liziczai2025structuralbasisfor pages 4-6, liziczai2025structuralbasisfor pages 6-8). Bacterial representatives vary: many retain 11 TMs, while some prokaryotic homologs (e.g., *Escherichia coli* DMT, EcoDMT) have 12 TMs convergent with the eukaryotic architecture (liziczai2025structuralbasisfor pages 4-6).

Recent cryo-EM structures of human DMT1 and NRAMP1 at 3.6–3.9 Å resolution reveal **occluded** and **inward-facing** conformations consistent with an alternating-access transport cycle (liziczai2025structuralbasisfor pages 4-6, liziczai2025structuralbasisfor pages 6-8). The central metal-binding site is inaccessible from either side of the membrane in the occluded state, confirming that substrate translocation requires large-scale conformational rearrangements of the "helical bundle" (TM1, 2, 6, 7) rocking relative to the "hash motif" scaffold (TM3, 4, 8, 9) (cellier2016evolutionaryanalysisof pages 1-4, cellier2016evolutionaryanalysisof pages 4-6, bozzi2019transmembranehelix6b pages 1-2).

### 1.2 Conserved Catalytic and Metal-Binding Residues

Two highly conserved sequence motifs define the NRAMP family and distinguish it from phylogenetic outgroups (NRMT Mg²⁺ transporters) (cellier2016evolutionaryanalysisof pages 1-4, bozzi2019transmembranehelix6b pages 1-2):

1. **DPGN motif** (consensus Y-DPGN₅₂) in **TM1**: The aspartate (D) and asparagine (N) residues contribute directly to the metal-binding site. In *Deinococcus radiodurans* Nramp (DraNramp), **D56** coordinates the metal ion and serves as the primary proton-binding residue, while **N59** provides additional metal coordination (bozzi2019transmembranehelix6b pages 1-2, cellier2016evolutionaryanalysisof pages 1-4).

2. **MPH motif** (consensus MPH₂₂₈) in **TM6**: The methionine (M) side chain and backbone carbonyls (e.g., A227 in DraNramp) contribute to octahedral metal coordination. Histidines in TM6b (H232, H237 in DraNramp) are critical for conformational cycling: **H232** acts as a pivot point below the metal site along the proton-exit route, while **H237** lines the metal-release pathway and is essential for return to the outward-open state (bozzi2019transmembranehelix6b pages 1-2).

The metal-binding site itself is formed by **partially unwound regions** of TM1 and TM6 near the membrane center, with the ion coordinated by D56, N59, M230, and backbone carbonyls of A53 and A227 (in DraNramp numbering) (bozzi2019transmembranehelix6b pages 1-2, cellier2016evolutionaryanalysisof pages 1-4). Human DMT1 and NRAMP1 structures confirm conservation of this architecture, though with residue-level variations that enhance transition-metal selectivity over alkaline-earth metals (Ca²⁺, Mg²⁺) (liziczai2025structuralbasisfor pages 6-8, liziczai2025structuralbasisfor pages 4-6).

### 1.3 Mechanism of Transport

NRAMP proteins are **secondary active transporters** that couple transition-metal import to the **symport of protons (H⁺)**, harnessing the electrochemical proton gradient (protonmotive force) as the energy source (liziczai2025structuralbasisfor pages 1-2, liziczai2025structuralbasisfor pages 2-4, cellier2016evolutionaryanalysisof pages 4-6). Reconstitution studies of human DMT1 and NRAMP1 in proteoliposomes demonstrate:

- **Metal ion uptake** (Mn²⁺, Fe²⁺) is concentration-dependent, with apparent **Km values** of ~36 µM (Mn²⁺) and ~2.5 µM (Fe²⁺) for DMT1; ~5 µM (Mn²⁺) and ~1.4 µM (Fe²⁺) for NRAMP1 (liziczai2025structuralbasisfor pages 2-4).
- **H⁺-coupled acification** of vesicles occurs upon metal addition, confirming symport even at neutral pH (liziczai2025structuralbasisfor pages 1-2, liziczai2025structuralbasisfor pages 2-4).
- **Uncoupled H⁺ leak** is also observed, especially pronounced in NRAMP1 at acidic pH; this leak is inhibitable by the DMT1 inhibitor TMBIT, confirming it is protein-mediated (liziczai2025structuralbasisfor pages 2-4, liziczai2025structuralbasisfor pages 1-2).

Electrophysiological studies in *Xenopus* oocytes expressing mammalian DMT1 or the amoeba *Dictyostelium* Nramp1 confirm **electrogenic transport**, consistent with net charge movement during the coupled H⁺/metal²⁺ symport cycle (buracco2015dictyosteliumnramp1which pages 1-2). However, **mechanistic heterogeneity exists within the family**: the prototype Nramp protein Nramp2 from *Dictyostelium* mediates **non-electrogenic, proton-independent Fe²⁺ transport**, demonstrating that not all NRAMP homologs operate by the canonical H⁺-coupled mechanism (buracco2015dictyosteliumnramp1which pages 1-2).

The alternating-access cycle involves outward-open, occluded, and inward-open states. Metal and proton binding triggers rocking of the helical bundle, closure of extracellular gates (TM10), and opening of intracellular gates (TM5, loop 4/5) to release substrates into the cytoplasm (cellier2016evolutionaryanalysisof pages 1-4, cellier2016evolutionaryanalysisof pages 4-6, bozzi2019transmembranehelix6b pages 1-2). TM6b acts as a structural linker coupling proton and metal-release pathways to drive these conformational changes (bozzi2019transmembranehelix6b pages 1-2).

| Family / subgroup | Fold architecture & TM organization | Conserved motifs / key residues | Transport mechanism | Primary transported metals / quantitative data | Metals not transported or poorly transported | Distinguishing features / functional divergence | Taxonomic distribution | Key citations |
|---|---|---|---|---|---|---|---|---|
| **NRAMP / SLC11 family (general)** | Ancient APC superfamily transporter with **LeuT fold**; core of **10 TMs** as two inverted 5-TM repeats; many eukaryotic/human members have **12 TMs**, while several bacterial homologs retain 11 or 12 TMs depending on lineage. Metal-binding site is formed by partially unwound **TM1 and TM6** near the center of the membrane. (cellier2016evolutionaryanalysisof pages 1-4, liziczai2025structuralbasisfor pages 4-6, liziczai2025structuralbasisfor pages 6-8) | Canonical **DPGN** motif in TM1 and **MPH** motif in TM6 are strongly conserved family signatures; conserved binding/proton-coupling residues include **D56, N59, M230** plus backbone carbonyls (A53, A227 in DraNramp numbering) for metal coordination; conserved TM6b histidines help conformational cycling. (bozzi2019transmembranehelix6b pages 1-2, cellier2016evolutionaryanalysisof pages 1-4) | Secondary active **H+-coupled transition-metal transport** by alternating access; proton movement and metal release use partially separate internal networks. Coupling is often **not perfectly strict**, because uncoupled H+ leak and, in some settings, uncoupled metal flux can occur. (bozzi2019transmembranehelix6b pages 1-2, liziczai2025structuralbasisfor pages 1-2, cellier2016evolutionaryanalysisof pages 4-6) | Broad family scope includes **Fe2+, Mn2+, Co2+, Cd2+** across many homologs; transition metals are preferred over abundant alkaline-earth metals. (liziczai2025structuralbasisfor pages 1-2, cellier2016evolutionaryanalysisof pages 1-4, ray2023structuresandcoordination pages 1-2) | **Ca2+ and Mg2+** are generally excluded from transport by canonical human/prokaryotic family members; many homologs also exclude **Fe3+**. (liziczai2025structuralbasisfor pages 2-4, buracco2015dictyosteliumnramp1which pages 1-2) | Family-wide function is metal transport, but subfamilies differ in localization, directionality details, proton dependence, and substrate breadth; some prototype Nramp proteins diverge strongly from archetypal aN transport properties. (cellier2022nrampdepriveand pages 1-2, cellier2022nrampdepriveand pages 2-7, buracco2015dictyosteliumnramp1which pages 1-2) | Broadly conserved across **bacteria, archaea, protists, fungi, plants, and animals**. (liziczai2025structuralbasisfor pages 1-2, cellier2022nrampdepriveand pages 1-2, norberg2025slc11a2affectsnutritional pages 1-5) | (cellier2016evolutionaryanalysisof pages 1-4, liziczai2025structuralbasisfor pages 4-6, bozzi2019transmembranehelix6b pages 1-2, cellier2022nrampdepriveand pages 1-2) |
| **Human DMT1 / SLC11A2 (archetype Nramp, aN)** | Human cryo-EM structures show **12 TMs** with LeuT-like organization; first 10 helices form the canonical repeat architecture and the 12th TM is an added C-terminal helix absent from many bacterial homologs. (liziczai2025structuralbasisfor pages 4-6, liziczai2025structuralbasisfor pages 6-8) | Conserved central site shared with family; transition-metal selectivity derives from the canonical TM1/TM6 site plus surrounding residues that make the vestibule more selective for transition metals. (liziczai2025structuralbasisfor pages 1-2, liziczai2025structuralbasisfor pages 6-8) | **H+/metal symporter**; Mn2+ uptake is coupled to H+ even at neutral pH, with additional **uncoupled H+ leak**. (liziczai2025structuralbasisfor pages 2-4, liziczai2025structuralbasisfor pages 1-2) | Reconstituted human DMT1 transported **Mn2+** with apparent **Km ~36 µM** and **Fe2+** with apparent **Km ~2.5 µM**; also transports **Cd2+**, and earlier work supports **Co2+** transport. (liziczai2025structuralbasisfor pages 2-4, liziczai2025structuralbasisfor pages 1-2) | **Ca2+** acts as a low-affinity inhibitor at mM range rather than a transported substrate; **Mg2+** showed no detectable competition or transport up to 1 mM; prior studies and recent reconstitution argue against Ca2+/Mg2+ transport. (liziczai2025structuralbasisfor pages 2-4, liziczai2025structuralbasisfor pages 1-2) | Major vertebrate importer for dietary and endosomal Fe2+; broader specificity than some prototype homologs; central to intestinal iron uptake and endosomal iron release. (liziczai2025structuralbasisfor pages 1-2, pasquadibisceglie2023membranetransportersinvolved pages 1-2, norberg2025slc11a2affectsnutritional pages 1-5) | Animals; especially vertebrates, broadly expressed, enriched in intestine and endosomal systems. (liziczai2025structuralbasisfor pages 1-2, pasquadibisceglie2023membranetransportersinvolved pages 1-2, norberg2025slc11a2affectsnutritional pages 1-5) | (liziczai2025structuralbasisfor pages 2-4, liziczai2025structuralbasisfor pages 1-2, liziczai2025structuralbasisfor pages 4-6) |
| **Human NRAMP1 / SLC11A1 (archetype Nramp, aN)** | Human cryo-EM structures resolved **occluded** and **inward-facing** conformations; same overall LeuT-like architecture as DMT1 with **12 TMs** in human protein. (liziczai2025structuralbasisfor pages 4-6, liziczai2025structuralbasisfor pages 6-8) | Shares the conserved family metal-binding site and proton-coupling network; specialized sequence/structural features increase transition-metal selectivity in human paralogs relative to prokaryotic homologs. (liziczai2025structuralbasisfor pages 1-2, liziczai2025structuralbasisfor pages 6-8) | Recent structural/functional study supports **H+/metal symport** plus uncoupled H+ leak; older literature has reported antiport interpretations, so mechanistic direction in vivo has historically been debated. (liziczai2025structuralbasisfor pages 1-2, norberg2025slc11a2affectsnutritional pages 1-5, wesslingresnick2015nramp1andother pages 1-2) | Reconstituted human NRAMP1 transported **Mn2+** with apparent **Km ~5 µM** and **Fe2+** with apparent **Km ~1.4 µM**; Cd2+ strongly interferes and likely shares the same transport site. (liziczai2025structuralbasisfor pages 2-4) | No pronounced inhibition by **Ca2+** in reconstitution and no support for **Mg2+** transport in the recent human structural study; NRAMP1 is generally discussed as a transition-metal transporter rather than Ca/Mg transporter. (liziczai2025structuralbasisfor pages 2-4, liziczai2025structuralbasisfor pages 1-2) | Specialized for **nutritional immunity** and metal withdrawal in phagosomal/lysosomal compartments of myeloid cells rather than bulk dietary uptake; expression is restricted compared with DMT1. (liziczai2025structuralbasisfor pages 1-2, norberg2025slc11a2affectsnutritional pages 1-5, wesslingresnick2015nramp1andother pages 1-2) | Animals, especially professional phagocytes in vertebrates. (liziczai2025structuralbasisfor pages 1-2, norberg2025slc11a2affectsnutritional pages 1-5, wesslingresnick2015nramp1andother pages 1-2) | (liziczai2025structuralbasisfor pages 2-4, liziczai2025structuralbasisfor pages 1-2, norberg2025slc11a2affectsnutritional pages 1-5) |
| **Bacterial MntH / prokaryotic NRAMP homologs** | Canonical bacterial model systems show LeuT-fold NRAMP architecture; many bacterial homologs have **11 TMs**, whereas some like EcoDMT/human-like relatives have **12 TMs**. (bozzi2019transmembranehelix6b pages 1-2, liziczai2025structuralbasisfor pages 4-6) | Conserved **DPGN** and **MPH** motifs define canonical sequences; DraNramp metal site involves **D56, N59, M230** and backbone carbonyls. TM6b histidines **H232/H237** are crucial for conformational cycling. (bozzi2019transmembranehelix6b pages 1-2, cellier2016evolutionaryanalysisof pages 1-4) | Generally **H+-dependent Mn2+ import**, often also carrying Fe2+, Co2+, Cd2+ depending on homolog; metal transport requires conformational cycling between outward and inward states. (bozzi2019transmembranehelix6b pages 1-2, cellier2022nrampdepriveand pages 1-2, bosma2021regulationanddistinct pages 1-2) | Prokaryotic members are commonly described as importing **Mn2+** as primary physiological substrate; structural/functional work also supports transport of **Fe2+, Co2+, Cd2+**, and in some systems **Ni2+/Pb2+** can bind or be transported experimentally. (cellier2016evolutionaryanalysisof pages 1-4, bosma2021regulationanddistinct pages 1-2) | Canonical bacterial family members are generally not supported as **Ca2+** or **Mg2+** transporters; Mg2+ transport instead characterizes related **NRMT** outgroup carriers rather than true NRAMPs. (liziczai2025structuralbasisfor pages 1-2, cellier2022nrampdepriveand pages 1-2) | Bacterial homologs are major Mn acquisition systems in stress resistance and pathogenesis; the family is **polyphyletic** in bacteria, with MntH A/B/C groups and archaeal/eukaryote-linked branches. (cellier2022nrampdepriveand pages 1-2, cellier2022nrampdepriveand pages 2-7, bosma2021regulationanddistinct pages 1-2) | Broad across bacteria; MntH B enriched in anaerobes, MntH A more broadly distributed, some MntH C groups derived from eukaryotic HGT. (cellier2022nrampdepriveand pages 1-2, cellier2022nrampdepriveand pages 2-7) | (bozzi2019transmembranehelix6b pages 1-2, cellier2022nrampdepriveand pages 1-2, bosma2021regulationanddistinct pages 1-2) |
| **Archetype Nramp (aN) subfamily** | Eukaryotic/animal-centered branch of SLC11 evolution; includes metazoan **NRAMP1/SLC11A1** and **DMT1/SLC11A2** and related eukaryotic proteins. (cellier2022nrampdepriveand pages 2-7, buracco2015dictyosteliumnramp1which pages 1-2) | Retains canonical family motifs but has sequence changes in transport-linked helices and charge networks relative to prototype Nramp proteins. (cellier2016evolutionaryanalysisof pages 1-4, cellier2022nrampdepriveand pages 2-7) | Typically **proton-coupled transition-metal transport**; mammalian representatives are electrogenic H+-coupled carriers. (liziczai2025structuralbasisfor pages 1-2, buracco2015dictyosteliumnramp1which pages 1-2) | Commonly transport **Fe2+ and Mn2+**, often also **Cd2+/Co2+** depending on paralog and assay. (liziczai2025structuralbasisfor pages 2-4, liziczai2025structuralbasisfor pages 1-2, buracco2015dictyosteliumnramp1which pages 1-2) | Usually exclude **Fe3+**, **Ca2+**, **Mg2+** as transported substrates in canonical tested members. (liziczai2025structuralbasisfor pages 2-4, buracco2015dictyosteliumnramp1which pages 1-2) | aN proteins correlate with **phagocytosis**, nutritional immunity, and specialized trafficking in eukaryotes; compared with prototype proteins, they show sustained divergence and altered transport-linked residue networks. (cellier2022nrampdepriveand pages 1-2, cellier2022nrampdepriveand pages 2-7) | Animals and some other eukaryotes. (cellier2022nrampdepriveand pages 2-7, buracco2015dictyosteliumnramp1which pages 1-2) | (cellier2022nrampdepriveand pages 1-2, cellier2022nrampdepriveand pages 2-7, buracco2015dictyosteliumnramp1which pages 1-2) |
| **Prototype Nramp (pN) subfamily** | Distinct eukaryotic branch inferred to predate the last eukaryotic common ancestor; includes several protist/fungal/plant-like forms and is the source of some bacterial MntH C HGT lineages. (cellier2022nrampdepriveand pages 2-7) | Conserved core motifs remain, but multiple transport-linked residues differ from aN proteins; branch-specific substitutions likely alter proton pathway and conformational behavior. (cellier2022nrampdepriveand pages 2-7, cellier2016evolutionaryanalysisof pages 1-4) | Mechanistically diverse: some pN proteins diverge from classic electrogenic H+/metal symport. Dictyostelium **Nramp2** (prototype-like) was reported to transport **Fe2+ only**, in a **non-electrogenic, proton-independent** manner. (buracco2015dictyosteliumnramp1which pages 1-2) | Can be narrower in specificity than archetypal proteins; Dictyostelium Nramp2 transported **Fe2+** but not Mn2+ in the cited study. (buracco2015dictyosteliumnramp1which pages 1-2) | Dictyostelium Nramp2 did **not** transport **Fe3+** or **Cu** in the compared assays for the Nramp system; prototype-like proteins can therefore violate broad family assumptions. (buracco2015dictyosteliumnramp1which pages 1-2) | This is the clearest evidence that the InterPro family is **not functionally uniform in detailed mechanism or substrate range**: some pN proteins are proton-independent and more substrate-restricted than archetypal NRAMPs. (buracco2015dictyosteliumnramp1which pages 1-2, cellier2022nrampdepriveand pages 2-7) | Protists, fungi, plants, some early-diverging eukaryotes; also donor source for some bacterial HGT-derived MntH C groups. (cellier2022nrampdepriveand pages 2-7, buracco2015dictyosteliumnramp1which pages 1-2) | (cellier2022nrampdepriveand pages 2-7, buracco2015dictyosteliumnramp1which pages 1-2) |
| **Dictyostelium Nramp1 (archetype-like) vs Nramp2 (prototype-like)** | Both are NRAMP-family membrane proteins, but represent divergent branches in one organism. (buracco2015dictyosteliumnramp1which pages 1-2) | Core family motifs retained; branch identity correlates with different mechanistic behavior. (buracco2015dictyosteliumnramp1which pages 1-2) | **Nramp1**: electrogenic, **proton-dependent** transport. **Nramp2**: **non-electrogenic, proton-independent** transport. (buracco2015dictyosteliumnramp1which pages 1-2) | **Nramp1** transported **Fe2+ and Mn2+**; **Nramp2** transported **Fe2+ only**. (buracco2015dictyosteliumnramp1which pages 1-2) | In the same study, neither behaved as **Fe3+** or **Cu** transporter. (buracco2015dictyosteliumnramp1which pages 1-2) | Strong within-family functional divergence; Nramp1 mediates phagosomal/macropinosomal iron efflux linked to pathogen resistance, whereas Nramp2 localizes to the contractile vacuole and contributes to iron homeostasis differently. (buracco2015dictyosteliumnramp1which pages 1-2) | Amoebozoa / protists. (buracco2015dictyosteliumnramp1which pages 1-2) | (buracco2015dictyosteliumnramp1which pages 1-2) |
| **Plants / fungi NRAMP examples** | Eukaryotic NRAMPs with canonical fold; localized to plasma membrane, vacuole, chloroplast, and other internal membranes depending on paralog. (ray2023structuresandcoordination pages 8-9, bozzi2019transmembranehelix6b pages 1-2) | Conserved NRAMP motifs generally retained across land plants and fungi. (bozzi2019transmembranehelix6b pages 1-2, cellier2016evolutionaryanalysisof pages 1-4) | Mostly used for cellular acquisition or remobilization of divalent transition metals. (bozzi2019transmembranehelix6b pages 1-2, ray2023structuresandcoordination pages 8-9) | Plants: NRAMP importers participate in **Fe2+/Mn2+** homeostasis and can contribute to **Cd** uptake/transport in some paralogs. Fungi: **Smf1** (PM) and **Smf3** (vacuole) import **Fe2+**; yeast homologs are often discussed as Mn/Fe transporters. (ray2023structuresandcoordination pages 8-9, buracco2015dictyosteliumnramp1which pages 1-2) | No evidence from the cited texts for transport of **Ca2+**, **Mg2+**, or **Fe3+** as canonical substrates. (ray2023structuresandcoordination pages 8-9, buracco2015dictyosteliumnramp1which pages 1-2) | Paralog-specific localization is highly diverse, showing that GO component terms more specific than generic membrane would not transfer family-wide. Some plant paralogs have major roles in heavy-metal tolerance/cadmium accumulation, not identical to mammalian nutritional-immunity roles. (ray2023structuresandcoordination pages 8-9, norberg2025slc11a2affectsnutritional pages 1-5) | Plants and fungi broadly. (ray2023structuresandcoordination pages 8-9, buracco2015dictyosteliumnramp1which pages 1-2) | (ray2023structuresandcoordination pages 8-9, buracco2015dictyosteliumnramp1which pages 1-2) |
| **Bacterial phylogroups: MntH A, B, C and archaeal MH** | All belong within the broader SLC11 evolutionary radiation but differ by origin and sequence signatures. (cellier2022nrampdepriveand pages 1-2, cellier2022nrampdepriveand pages 2-7) | Shared SLC11 core with lineage-specific substitutions in charge networks and transport-linked helices. (cellier2022nrampdepriveand pages 1-2, cellier2022nrampdepriveand pages 2-7) | All are tied to metal uptake, especially **H+-dependent Mn2+ acquisition**, but likely differ in regulation and conformational details. (cellier2022nrampdepriveand pages 1-2, bosma2021regulationanddistinct pages 1-2) | Not all have equivalent substrate breadth established experimentally; broad family assumption is strongest only at the level of transition-metal transport. (cellier2022nrampdepriveand pages 1-2, bosma2021regulationanddistinct pages 1-2) | No evidence from cited sources for Ca/Mg transport by true MntH groups. (cellier2022nrampdepriveand pages 1-2) | **MntH B** is confined mainly to anaerobic bacteria; **MntH A** is broadly distributed in aerobic bacteria; **MH** predominates in archaea and is sister to Nramp; **MntH C** subgroups likely arose via horizontal transfer from eukaryotic prototype Nramp donors. (cellier2022nrampdepriveand pages 1-2, cellier2022nrampdepriveand pages 2-7) | Bacteria and archaea, with HGT links to eukaryotes. (cellier2022nrampdepriveand pages 1-2, cellier2022nrampdepriveand pages 2-7) | (cellier2022nrampdepriveand pages 1-2, cellier2022nrampdepriveand pages 2-7) |


*Table: This table summarizes the structural, mechanistic, evolutionary, and substrate-specific properties of the NRAMP/SLC11 family and its major subgroups. It is useful for judging whether broad GO annotations are safe across the full InterPro family or only valid for specific clades or subfamilies.*

---

## 2. InterPro2GO Mapping Appropriateness

The three GO terms currently mapped to IPR001046 are evaluated below for their validity across the **entire family** (~31,226 proteins, 24,403 taxa, bacteria through animals).

### 2.1 GO:0046873 – metal ion transmembrane transporter activity [F]

**Assessment**: This term is **broadly appropriate** for the family. Experimental characterization across bacterial MntH, mammalian NRAMP1/DMT1, plant, fungal, and protist homologs consistently supports a core molecular function of **transition/divalent metal ion transport** (liziczai2025structuralbasisfor pages 2-4, liziczai2025structuralbasisfor pages 1-2, buracco2015dictyosteliumnramp1which pages 1-2, ray2023structuresandcoordination pages 8-9, bosma2021regulationanddistinct pages 1-2). The term "metal ion" is suitably broad to encompass the substrate diversity observed (Fe²⁺, Mn²⁺, Co²⁺, Cd²⁺), while excluding alkaline-earth metals (Ca²⁺, Mg²⁺) and ferric iron (Fe³⁺), which are **not** canonical substrates (liziczai2025structuralbasisfor pages 2-4, buracco2015dictyosteliumnramp1which pages 1-2).

**Caveats**: (a) Some prototype Nramp (pN) members show **restricted specificity**: *Dictyostelium* Nramp2 transports **Fe²⁺ only**, not Mn²⁺ (buracco2015dictyosteliumnramp1which pages 1-2). (b) The term does not capture that the family **selectively transports transition metals** rather than all metal ions. However, this level of generality is acceptable for a family-level annotation and avoids over-commitment to specific metals that vary by subfamily.

**Recommendation**: **ACCEPT**. More specific child terms (e.g., "ferrous iron transmembrane transporter activity" GO:0034599, "manganese ion transmembrane transporter activity" GO:1901379) should be reserved for subfamily-level or gene-specific annotation where experimentally justified.

### 2.2 GO:0030001 – metal ion transport [P]

**Assessment**: This biological process term is **appropriate** across the family. NRAMP/SLC11 proteins participate in metal ion transport in all characterized contexts: bacterial Mn²⁺ uptake for oxidative stress resistance (bosma2021regulationanddistinct pages 1-2), mammalian dietary iron absorption and endosomal iron release (liziczai2025structuralbasisfor pages 1-2, norberg2025slc11a2affectsnutritional pages 1-5), phagosomal metal deprivation for nutritional immunity (wesslingresnick2015nramp1andother pages 1-2, norberg2025slc11a2affectsnutritional pages 1-5), plant vacuolar/chloroplast metal remobilization (ray2023structuresandcoordination pages 8-9), and fungal iron homeostasis (ray2023structuresandcoordination pages 8-9, buracco2015dictyosteliumnramp1which pages 1-2).

**Caveats**: (a) The term is **highly generic** and provides limited biological insight beyond stating that the protein moves metals. (b) More specific processes such as "iron ion homeostasis" (GO:0055072), "nutritional immunity" (not a current GO term but conceptually relevant), "phagosome metal depletion," or "cadmium ion transport" are **subfamily- or context-specific** and should **not** be applied at the family level, as they would over-annotate many members (e.g., bacterial MntH is not involved in phagosomal function; plant NRAMPs are not phagocytic).

**Recommendation**: **ACCEPT**. Retain the broad process term; avoid adding narrow descendant terms at this family entry.

### 2.3 GO:0016020 – membrane [C]

**Assessment**: This term is **trivially true** (all NRAMP proteins are multi-pass integral membrane proteins) but **informationally vacuous**. The family exhibits **extreme localization heterogeneity** by taxon and paralog (liziczai2025structuralbasisfor pages 1-2, norberg2025slc11a2affectsnutritional pages 1-5, ray2023structuresandcoordination pages 8-9, buracco2015dictyosteliumnramp1which pages 1-2):

- **Plasma membrane**: intestinal apical membrane (DMT1), bacterial inner membrane (MntH), plant/fungal plasma membrane (various NRAMPs).
- **Endosomal/lysosomal membranes**: mammalian DMT1 in transferrin-receptor endosomes, NRAMP1 in phagolysosomes.
- **Vacuolar membrane**: plant and fungal NRAMP paralogs.
- **Chloroplast membrane**: plant NRAMPs in chloroplast inner envelope.
- **Contractile vacuole membrane**: *Dictyostelium* Nramp2 (buracco2015dictyosteliumnramp1which pages 1-2).

Assigning any **single specific compartment** term (e.g., "phagosomal membrane," "endosome membrane") at the family level would over-annotate the majority of proteins that do not localize there. Conversely, the current term "membrane" conveys no useful biological information beyond "this is a membrane protein."

**Recommendation**: **KEEP_AS_NON_CORE**. The term is not *wrong*, but it is unhelpfully generic. InterPro should **not** replace it with a narrower term at this level; instead, more specific component terms should be assigned on a **gene-by-gene basis** or on **InterPro child entries** if subfamily-specific localization patterns are established (e.g., a hypothetical child entry for phagosomal NRAMPs could carry "phagosomal membrane"). The current mapping reflects the reality that this is a **family-level** signature with diverse localizations.

| GO term | Aspect | True for all IPR001046 matches? | Evidence assessment across the NRAMP family | Problems identified | Recommendation | More appropriate specific GO term(s) if modifying | Key supporting citations |
|---|---|---|---|---|---|---|---|
| GO:0046873 metal ion transmembrane transporter activity | F | **Mostly yes, with caution** | IPR001046 is a **family-level** entry spanning bacteria, archaea, protists, fungi, plants, and animals; across these clades, characterized NRAMP/SLC11 proteins are integral membrane transporters for **transition/divalent metal ions**, typically Fe2+ and/or Mn2+, often also Co2+ or Cd2+. Structural and functional work on human DMT1/NRAMP1, bacterial MntH/Nramp homologs, and protist/fungal representatives supports a conserved transporter mechanism. However, substrate breadth is **not uniform**: some prototype Nramp (pN) members are narrower, e.g. Dictyostelium Nramp2 transports **Fe2+ only** rather than the broader Fe2+/Mn2+ profile seen in many aN/MntH proteins. Still, the broad parent activity “metal ion transmembrane transporter activity” remains compatible with this diversity because it does not require a specific metal species. (liziczai2025structuralbasisfor pages 2-4, liziczai2025structuralbasisfor pages 1-2, buracco2015dictyosteliumnramp1which pages 1-2, cellier2022nrampdepriveand pages 1-2, cellier2022nrampdepriveand pages 2-7) | Very broad/high-level term; does not capture that the family largely handles **transition/divalent metal ions** and excludes Ca2+/Mg2+/Fe3+ in characterized canonical members. Could still annotate inactive or untested family members if the family contains rare non-transporting derivatives, but no strong evidence for widespread pseudo-transporters was found. | **ACCEPT** | Optional child terms only at narrower InterPro child/subfamily level, e.g. divalent metal ion transmembrane transporter activity, ferrous iron transmembrane transporter activity, manganese ion transmembrane transporter activity, when supported for specific subfamilies rather than the whole family | (liziczai2025structuralbasisfor pages 2-4, liziczai2025structuralbasisfor pages 1-2, bozzi2019transmembranehelix6b pages 1-2, cellier2016evolutionaryanalysisof pages 1-4, buracco2015dictyosteliumnramp1which pages 1-2) |
| GO:0030001 metal ion transport | P | **Mostly yes, with caution** | Experimental and review literature consistently place NRAMP/SLC11 proteins in the biological process of **metal ion transport** across taxa. This holds for bacterial MntH uptake systems, mammalian DMT1 and NRAMP1, and plant/fungal/protist NRAMPs, despite differences in cellular role (dietary uptake, endosomal release, phagosomal deprivation, vacuolar remobilization, chloroplast/vacuolar transport, contractile vacuole function). Because the process term is broad, it accommodates family-wide variation in transported metal species and direction/localization. (liziczai2025structuralbasisfor pages 1-2, norberg2025slc11a2affectsnutritional pages 1-5, ray2023structuresandcoordination pages 8-9, bosma2021regulationanddistinct pages 1-2, buracco2015dictyosteliumnramp1which pages 1-2) | Generic process term with limited information value; does not indicate **which metal**, **which membrane**, or **physiological context**. Some descendant-specific processes such as iron ion homeostasis, manganese ion transport, nutritional immunity, or phagosome metal depletion are **not** universal and should not be attached at this top family level. | **ACCEPT** | Optional refinement only at child/subfamily level: iron ion transport, manganese ion transport, cadmium ion transport, metal ion homeostasis, or specific host-defense/nutritional-immunity processes where experimentally justified | (liziczai2025structuralbasisfor pages 1-2, norberg2025slc11a2affectsnutritional pages 1-5, ray2023structuresandcoordination pages 8-9, wesslingresnick2015nramp1andother pages 1-2, buracco2015dictyosteliumnramp1which pages 1-2) |
| GO:0016020 membrane | C | **Trivially yes but unhelpful** | NRAMP proteins are multi-pass membrane proteins throughout the family, so “membrane” is not wrong in a literal sense. However, the literature shows highly variable and biologically important localization by taxon and paralog: plasma membrane, endosome, phagosome/phagolysosome, vacuole, chloroplast, contractile vacuole, and related endomembranes. Thus the current term is too generic to convey useful information and obscures real compartment diversity. (liziczai2025structuralbasisfor pages 1-2, norberg2025slc11a2affectsnutritional pages 1-5, ray2023structuresandcoordination pages 8-9, buracco2015dictyosteliumnramp1which pages 1-2, wesslingresnick2015nramp1andother pages 1-2) | **Extremely generic** cellular component; low information content. More specific component terms would be **subfamily- or taxon-dependent** and therefore unsafe at this family-wide level. Examples: phagosomal membrane applies to NRAMP1-like proteins; apical plasma membrane/endosomal membrane to DMT1; vacuolar membrane/chloroplast membrane to plant/fungal paralogs; contractile vacuole membrane to Dictyostelium Nramp2. Using a single specific compartment would over-annotate many taxa. | **KEEP_AS_NON_CORE** | Do **not** replace with one global specific CC term at this family level. More specific terms should be assigned only on child entries or gene-level evidence, e.g. plasma membrane, endosomal membrane, phagosomal membrane, vacuolar membrane, chloroplast membrane, contractile vacuole membrane | (liziczai2025structuralbasisfor pages 1-2, pasquadibisceglie2023membranetransportersinvolved pages 1-2, norberg2025slc11a2affectsnutritional pages 1-5, ray2023structuresandcoordination pages 8-9, buracco2015dictyosteliumnramp1which pages 1-2) |


*Table: This table evaluates the three current InterPro2GO mappings for IPR001046 against family-wide evidence across bacteria, archaea, and eukaryotes. It highlights which terms are broadly defensible, which are overly generic, and where specificity should be moved to child entries or gene-level annotation.*

---

## 3. Functional Divergence Across the Family

The NRAMP/SLC11 family is **not functionally uniform** despite sharing a conserved fold and core transport mechanism. Phylogenetic and functional analyses reveal at least **three major evolutionary subfamilies** with distinct properties (cellier2022nrampdepriveand pages 1-2, cellier2022nrampdepriveand pages 2-7, buracco2015dictyosteliumnramp1which pages 1-2):

### 3.1 Archetype Nramp (aN) Subfamily

**Members**: Vertebrate NRAMP1 (SLC11A1) and DMT1 (SLC11A2), related metazoan proteins, some fungal/protist paralogs (cellier2022nrampdepriveand pages 2-7, liziczai2025structuralbasisfor pages 1-2).

**Key Features**:
- **Electrogenic, H⁺-coupled symport** mechanism experimentally confirmed (liziczai2025structuralbasisfor pages 2-4, liziczai2025structuralbasisfor pages 1-2, buracco2015dictyosteliumnramp1which pages 1-2).
- Broad substrate profile: **Fe²⁺, Mn²⁺, Co²⁺, Cd²⁺**; excludes Ca²⁺, Mg²⁺, Fe³⁺ (liziczai2025structuralbasisfor pages 2-4).
- **Specialized biological roles**: DMT1 in dietary iron uptake and endosomal iron release; NRAMP1 in phagosomal metal deprivation for **nutritional immunity** against intracellular pathogens (*Mycobacterium*, *Salmonella*, *Leishmania*) (liziczai2025structuralbasisfor pages 1-2, norberg2025slc11a2affectsnutritional pages 1-5, wesslingresnick2015nramp1andother pages 1-2).
- Strong evolutionary signal of **sustained divergence** from prototype Nramp proteins, with branch-specific substitutions in transport-linked helices and charge networks (cellier2022nrampdepriveand pages 2-7, cellier2016evolutionaryanalysisof pages 1-4).
- **Correlation with phagocytosis**: aN proteins are enriched in organisms with phagocytic immune systems (cellier2022nrampdepriveand pages 2-7).

**Functional implication**: aN proteins are optimized for roles in iron/manganese metabolism and host defense, not merely bulk cellular metal uptake.

### 3.2 Prototype Nramp (pN) Subfamily

**Members**: Protist, fungal, and plant NRAMP proteins (e.g., yeast Smf proteins, plant vacuolar/chloroplast NRAMPs, *Dictyostelium* Nramp2), and the source of bacterial MntH C horizontal gene transfer (HGT) lineages (cellier2022nrampdepriveand pages 2-7, buracco2015dictyosteliumnramp1which pages 1-2).

**Key Features**:
- **Mechanistic heterogeneity**: Some pN proteins are **proton-independent** and **non-electrogenic**, violating the canonical H⁺-coupled symport model. *Dictyostelium* Nramp2 is the clearest experimental example: it transports **Fe²⁺ only** (not Mn²⁺, Fe³⁺, or Cu) in a **non-electrogenic, proton-independent** manner, contrasting sharply with *Dictyostelium* Nramp1 (an aN-like protein) which is electrogenic and H⁺-dependent (buracco2015dictyosteliumnramp1which pages 1-2).
- **Narrower substrate specificity** in some cases (Fe²⁺ only vs. Fe²⁺/Mn²⁺ in aN proteins) (buracco2015dictyosteliumnramp1which pages 1-2).
- **Diverse subcellular localizations**: contractile vacuole (Nramp2), vacuolar membrane (plant/fungal), chloroplast (plant), plasma membrane (some paralogs) (buracco2015dictyosteliumnramp1which pages 1-2, ray2023structuresandcoordination pages 8-9).
- **Earlier evolutionary origin**: pN paralogs predate the last eukaryotic common ancestor (LECA), with subsequent gene duplications yielding pN-I and pN-II sub-lineages (cellier2022nrampdepriveand pages 2-7).

**Functional implication**: pN proteins are **not** functionally interchangeable with aN proteins. Assigning GO terms specific to H⁺-coupled transport or Mn²⁺ transport at the family level would over-annotate pN members.

### 3.3 Bacterial MntH Phylogroups

**Members**: Bacterial NRAMP homologs classified into polyphyletic groups MntH A, MntH B, and MntH C, plus archaeal MntH H (MH) (cellier2022nrampdepriveand pages 1-2, cellier2022nrampdepriveand pages 2-7).

**Key Features**:
- **MntH A**: Broadly distributed in aerobic bacteria; primary Mn²⁺ importer for oxidative stress resistance (bosma2021regulationanddistinct pages 1-2, cellier2022nrampdepriveand pages 1-2).
- **MntH B**: Confined mainly to **anaerobic bacteria**; predates aerobiosis (cellier2022nrampdepriveand pages 1-2, cellier2022nrampdepriveand pages 2-7).
- **MntH C**: Result of **horizontal gene transfer (HGT)** from eukaryotic prototype Nramp donors back to bacteria; divided into MCa, MCb, MCγ subgroups with niche-related distributions (cellier2022nrampdepriveand pages 1-2, cellier2022nrampdepriveand pages 2-7).
- **MntH H (MH)**: Predominates in **archaea**, carries "eukaryotic signature" marks in TM4/TM9, and is phylogenetically sister to eukaryotic Nramp; may have contributed to eukaryogenesis (cellier2022nrampdepriveand pages 1-2, cellier2022nrampdepriveand pages 2-7).

**Functional implication**: Bacterial/archaeal members are primarily **Mn²⁺ acquisition systems** rather than Fe²⁺ transporters, though some also transport Fe²⁺. Their roles are tied to **metal homeostasis under stress** and **virulence** in pathogenic bacteria (e.g., *Salmonella* MntH supports intracellular survival) (bosma2021regulationanddistinct pages 1-2, wesslingresnick2015nramp1andother pages 1-2). GO terms specific to iron transport or mammalian immune functions would not apply.

### 3.4 Within-Organism Paralog Divergence

Even within a single organism, NRAMP paralogs can have **opposite or complementary functions**:

- **Humans**: NRAMP1 (SLC11A1) is restricted to myeloid cells (macrophages, neutrophils) and functions in **phagosomal metal deprivation**; DMT1 (SLC11A2) is ubiquitously expressed and mediates **dietary iron uptake** and **endosomal iron release** (liziczai2025structuralbasisfor pages 1-2, norberg2025slc11a2affectsnutritional pages 1-5, wesslingresnick2015nramp1andother pages 1-2).
- ***Dictyostelium***: Nramp1 (aN-like) is phagosomal, electrogenic, transports Fe²⁺/Mn²⁺, and confers resistance to bacteria; Nramp2 (pN-like) is contractile vacuole-localized, non-electrogenic, transports Fe²⁺ only, and controls iron homeostasis synergistically with Nramp1 (buracco2015dictyosteliumnramp1which pages 1-2).
- **Plants**: Multiple NRAMP paralogs with distinct localizations (plasma membrane, vacuole, chloroplast) and roles in Fe/Mn uptake, remobilization, or heavy metal (Cd) tolerance (ray2023structuresandcoordination pages 8-9).

**Implication**: Assigning a single specific biological process or cellular component term at the family level would misrepresent the functional diversity of paralogs within individual genomes.

---

## 4. Taxonomic Scope

IPR001046 matches proteins across **all three domains of life** and all major eukaryotic supergroups (cellier2022nrampdepriveand pages 1-2, cellier2022nrampdepriveand pages 2-7):

### 4.1 Bacteria

MntH homologs are widespread but **polyphyletic**, with MntH A found broadly in aerobic bacteria (e.g., *Escherichia*, *Salmonella*, *Bacillus*), MntH B in anaerobes, and MntH C derived from eukaryotic HGT (cellier2022nrampdepriveand pages 1-2, cellier2022nrampdepriveand pages 2-7, bosma2021regulationanddistinct pages 1-2). Function: primarily **Mn²⁺ import** for oxidative stress resistance, virulence, and metal homeostasis.

### 4.2 Archaea

Archaeal MntH H (MH) predominates, carrying sequence signatures linking it to eukaryotic Nramp (cellier2022nrampdepriveand pages 1-2, cellier2022nrampdepriveand pages 2-7). Hypothesized role in **Mn²⁺ sequestration** during eukaryogenesis (cellier2022nrampdepriveand pages 2-7).

### 4.3 Eukaryotes

- **Protists**: Both pN and aN types; *Dictyostelium* Nramp1/2 exemplify divergent mechanisms within Amoebozoa (buracco2015dictyosteliumnramp1which pages 1-2, cellier2022nrampdepriveand pages 2-7).
- **Fungi**: Prototype-like NRAMPs (e.g., yeast Smf1/Smf2/Smf3) involved in Mn²⁺/Fe²⁺ homeostasis (ray2023structuresandcoordination pages 8-9, buracco2015dictyosteliumnramp1which pages 1-2).
- **Plants** (Archaeplastida): Extensive NRAMP families with roles in **Fe/Mn nutrition, vacuolar remobilization, chloroplast import, and heavy metal (Cd) tolerance**; paralogs localize to plasma membrane, vacuole, chloroplast, and endoplasmic reticulum (ray2023structuresandcoordination pages 8-9).
- **Animals** (Metazoa): Archetype Nramp proteins only (aN-I, aN-II); vertebrates retain SLC11A1 (NRAMP1) and SLC11A2 (DMT1) with specialized immune and nutritional roles (cellier2022nrampdepriveand pages 2-7, liziczai2025structuralbasisfor pages 1-2, norberg2025slc11a2affectsnutritional pages 1-5).

### 4.4 Cross-Domain Observations

- **Membrane localization is taxon- and paralog-specific**: There is **no universal compartment** for the family (norberg2025slc11a2affectsnutritional pages 1-5, ray2023structuresandcoordination pages 8-9, buracco2015dictyosteliumnramp1which pages 1-2).
- **Process terms involving immune functions** (e.g., "innate immune response," "nutritional immunity") apply **only to animal NRAMP1-like proteins**, not to bacterial, archaeal, or plant homologs (wesslingresnick2015nramp1andother pages 1-2, norberg2025slc11a2affectsnutritional pages 1-5).
- **Substrate specificity varies**: Bacterial MntH is often Mn²⁺-centric; mammalian DMT1 is Fe²⁺-centric; some pN proteins are Fe²⁺-only (bosma2021regulationanddistinct pages 1-2, buracco2015dictyosteliumnramp1which pages 1-2, liziczai2025structuralbasisfor pages 1-2).

**Conclusion**: GO terms must be evaluated for **pan-taxonomic validity**. Terms specific to animal immune function, plant chloroplasts, or bacterial anaerobiosis would over-annotate the majority of family members.

---

## 5. Over-Annotation Verdict and GO Action Pattern

### 5.1 Summary of Findings

1. **IPR001046 is a true FAMILY** (entry type: family) encompassing ~31,000 proteins with a conserved LeuT-fold architecture and shared core function (metal ion transport), but exhibiting **substantial subfamily-level divergence** in mechanism, substrate specificity, and cellular role.

2. **Current InterPro2GO mappings**:
   - **GO:0046873 (metal ion transmembrane transporter activity)**: Broadly valid; all characterized members transport transition/divalent metal ions (Fe²⁺, Mn²⁺, Co²⁺, Cd²⁺). **Verdict: Sound**.
   - **GO:0030001 (metal ion transport)**: Broadly valid; all members participate in metal ion transport as their biological process. **Verdict: Sound but generic**.
   - **GO:0016020 (membrane)**: Trivially true but uninformative; localization is highly variable (plasma membrane, endosome, phagosome, vacuole, chloroplast, contractile vacuole). **Verdict: Overly generic, low information content**.

3. **Functional heterogeneity precludes more specific terms at the family level**:
   - Substrate-specific terms (e.g., "ferrous iron transmembrane transporter activity," "manganese ion transmembrane transporter activity") are **not universal** (some pN proteins transport Fe²⁺ only; bacterial MntH is often Mn²⁺-centric).
   - Process terms like "iron ion homeostasis," "nutritional immunity," or "phagosome acidification" are **subfamily- or taxon-specific** and would over-annotate the majority of members.
   - Component terms like "phagosomal membrane," "endosome," "vacuolar membrane," or "chloroplast" are **paralog- and taxon-specific** and would over-annotate across the family.

### 5.2 GO Action Pattern Recommendations

| GO Term | Action Pattern | Rationale |
|---------|----------------|-----------|
| **GO:0046873** (metal ion transmembrane transporter activity [F]) | **ACCEPT** | Term is appropriately broad for the family's conserved molecular function. More specific child terms (e.g., ferrous iron, manganese ion) should be reserved for subfamily-level or gene-specific annotation. |
| **GO:0030001** (metal ion transport [P]) | **ACCEPT** | Term captures the family's shared biological process without over-committing to specific metals, pathways, or contexts. Subfamily-specific processes (e.g., nutritional immunity, iron homeostasis) should not be added at this level. |
| **GO:0016020** (membrane [C]) | **KEEP_AS_NON_CORE** | Term is factually correct but provides minimal information. **Do not replace** with a narrower term (e.g., phagosomal membrane, endosome, vacuole) at the family level, as localization is paralog/taxon-specific. More specific CC terms should be assigned on a **gene-by-gene basis** or on InterPro child entries if subfamily-specific localization patterns can be established. The current term reflects the reality that this is a family-level signature with heterogeneous localizations. |

### 5.3 Recommendations for InterPro and GO Curators

1. **Retain current mappings** with the understanding that they are **intentionally generic** to avoid over-annotation of a functionally diverse family.

2. **Do NOT add more specific GO terms** (e.g., "iron ion transmembrane transporter activity," "phagosomal membrane") to IPR001046 itself, as they would incorrectly annotate bacterial MntH, plant NRAMPs, and other subfamilies that do not match those narrower functions/localizations.

3. **Consider creating InterPro child entries** for well-defined subfamilies (e.g., "vertebrate NRAMP1 subfamily," "plant vacuolar NRAMP subfamily," "bacterial MntH A group") and assigning more specific GO terms at those levels. For example:
   - A child entry for vertebrate NRAMP1 (SLC11A1) could carry "phagosomal membrane" (GO:0097233) and "defense response to bacterium" (GO:0042742).
   - A child entry for plant chloroplast NRAMPs could carry "chloroplast envelope" (GO:0009941).
   - A child entry for bacterial MntH A could carry "manganese ion transmembrane transporter activity" (GO:1901379).

4. **Educate users** that the current family-level annotations are **broad by design** and that gene-specific annotations should draw on experimental evidence or subfamily-specific rules.

5. **Flag GO:0016020 (membrane) as a low-information-content term** in documentation, acknowledging that it is retained for completeness but provides little biological insight. This is a known issue for many membrane protein families and is not unique to IPR001046.

### 5.4 Final Verdict

**InterPro2GO for IPR001046 is sound at a family level but suboptimal for specific biological insight**. The molecular function and biological process terms are **appropriate** for the conserved core activity shared across subfamilies and taxa. The cellular component term is **trivially correct but uninformative**. The mapping does **not** over-annotate in the sense of assigning false GO terms, but it under-specifies biologically important variation that should be captured at subfamily or gene levels. **Recommended action**: **ACCEPT** current mappings with the caveat that more specific annotations should be developed for InterPro child entries or applied during gene-level curation, not inherited from the top-level family signature.

---

## References (Key Citations from Evidence Base)

- Liziczai et al. (2025). Structural basis for metal ion transport by the human SLC11 proteins DMT1 and NRAMP1. *Nature Communications* 16:761. doi:10.1038/s41467-024-54705-0 (liziczai2025structuralbasisfor pages 2-4, liziczai2025structuralbasisfor pages 1-2, liziczai2025structuralbasisfor pages 6-8, liziczai2025structuralbasisfor pages 4-6)
- Ray & Gaudet (2023). Structures and coordination chemistry of transporters involved in manganese and iron homeostasis. *Biochemical Society Transactions* 51:897-923. doi:10.1042/BST20210699 (ray2023structuresandcoordination pages 1-2, ray2023structuresandcoordination pages 8-9, ray2023structuresandcoordination pages 4-6)
- Bozzi et al. (2019). Transmembrane helix 6b links proton- and metal-release pathways to drive conformational change in an Nramp transition metal transporter. *bioRxiv* doi:10.1101/792127 (bozzi2019transmembranehelix6b pages 1-2)
- Cellier (2022). Nramp: Deprive and conquer? *Frontiers in Cell and Developmental Biology* 10:988866. doi:10.3389/fcell.2022.988866 (cellier2022nrampdepriveand pages 1-2, cellier2022nrampdepriveand pages 2-7)
- Cellier (2016). Evolutionary analysis of Slc11 mechanism of proton-coupled metal-ion transmembrane import. *AIMS Biophysics* 3:286-318. doi:10.3934/biophy.2016.2.286 (cellier2016evolutionaryanalysisof pages 1-4, cellier2016evolutionaryanalysisof pages 4-6)
- Buracco et al. (2015). *Dictyostelium* Nramp1, which is structurally and functionally similar to mammalian DMT1 transporter, mediates phagosomal iron efflux. *Journal of Cell Science* 128:3304-3316. doi:10.1242/jcs.173153 (buracco2015dictyosteliumnramp1which pages 1-2)
- Banerjee et al. (2025). The solute carrier family 11 transporters: a bridge between iron homeostasis and tumor biology. *Cell Communication and Signaling* 23:332. doi:10.1186/s12964-025-02293-x (banerjee2025thesolutecarrier pages 1-3)
- Norberg et al. (2025). SLC11A2 affects nutritional immunity in the gut epithelium. *BioRxiv* doi:10.1101/2025.11.12.688034 (norberg2025slc11a2affectsnutritional pages 1-5, norberg2025slc11a2affectsnutritional pages 23-26)
- Pasquadibisceglie et al. (2023). Membrane Transporters Involved in Iron Trafficking: Physiological and Pathological Aspects. *Biomolecules* 13:1172. doi:10.3390/biom13081172 (pasquadibisceglie2023membranetransportersinvolved pages 1-2)
- Wessling-Resnick (2015). Nramp1 and Other Transporters Involved in Metal Withholding during Infection. *Journal of Biological Chemistry* 290:18984-18990. doi:10.1074/jbc.R115.643973 (wesslingresnick2015nramp1andother pages 1-2)
- Bosma et al. (2021). Regulation and distinct physiological roles of manganese in bacteria. *FEMS Microbiology Reviews* 45:fuab028. doi:10.1093/femsre/fuab028 (bosma2021regulationanddistinct pages 1-2)

---

**Report Date**: 2026  
**Prepared for**: InterPro2GO Annotation Review  
**Entry**: IPR001046 (NRAMP family)  
**Recommendation**: ACCEPT GO:0046873, GO:0030001; KEEP_AS_NON_CORE GO:0016020; do not add more specific terms at family level.

References

1. (cellier2016evolutionaryanalysisof pages 1-4): Mathieu F. M. Cellier. Evolutionary analysis of slc11 mechanism of proton-coupled metal-ion transmembrane import. ArXiv, 3:286-318, Jun 2016. URL: https://doi.org/10.3934/biophy.2016.2.286, doi:10.3934/biophy.2016.2.286. This article has 6 citations.

2. (cellier2016evolutionaryanalysisof pages 4-6): Mathieu F. M. Cellier. Evolutionary analysis of slc11 mechanism of proton-coupled metal-ion transmembrane import. ArXiv, 3:286-318, Jun 2016. URL: https://doi.org/10.3934/biophy.2016.2.286, doi:10.3934/biophy.2016.2.286. This article has 6 citations.

3. (liziczai2025structuralbasisfor pages 6-8): Márton Liziczai, Ariane Fuchs, Cristina Manatschal, and Raimund Dutzler. Structural basis for metal ion transport by the human slc11 proteins dmt1 and nramp1. Nature Communications, Jan 2025. URL: https://doi.org/10.1038/s41467-024-54705-0, doi:10.1038/s41467-024-54705-0. This article has 19 citations and is from a highest quality peer-reviewed journal.

4. (liziczai2025structuralbasisfor pages 4-6): Márton Liziczai, Ariane Fuchs, Cristina Manatschal, and Raimund Dutzler. Structural basis for metal ion transport by the human slc11 proteins dmt1 and nramp1. Nature Communications, Jan 2025. URL: https://doi.org/10.1038/s41467-024-54705-0, doi:10.1038/s41467-024-54705-0. This article has 19 citations and is from a highest quality peer-reviewed journal.

5. (bozzi2019transmembranehelix6b pages 1-2): Aaron T. Bozzi, Anne L. McCabe, Benjamin C. Barnett, and Rachelle Gaudet. Transmembrane helix 6b links proton- and metal-release pathways to drive conformational change in an nramp transition metal transporter. bioRxiv, Oct 2019. URL: https://doi.org/10.1101/792127, doi:10.1101/792127. This article has 1 citations.

6. (liziczai2025structuralbasisfor pages 1-2): Márton Liziczai, Ariane Fuchs, Cristina Manatschal, and Raimund Dutzler. Structural basis for metal ion transport by the human slc11 proteins dmt1 and nramp1. Nature Communications, Jan 2025. URL: https://doi.org/10.1038/s41467-024-54705-0, doi:10.1038/s41467-024-54705-0. This article has 19 citations and is from a highest quality peer-reviewed journal.

7. (liziczai2025structuralbasisfor pages 2-4): Márton Liziczai, Ariane Fuchs, Cristina Manatschal, and Raimund Dutzler. Structural basis for metal ion transport by the human slc11 proteins dmt1 and nramp1. Nature Communications, Jan 2025. URL: https://doi.org/10.1038/s41467-024-54705-0, doi:10.1038/s41467-024-54705-0. This article has 19 citations and is from a highest quality peer-reviewed journal.

8. (buracco2015dictyosteliumnramp1which pages 1-2): Simona Buracco, Barbara Peracino, Raffaella Cinquetti, Elena Signoretto, Alessandra Vollero, Francesca Imperiali, Michela Castagna, Elena Bossi, and Salvatore Bozzaro. Dictyostelium nramp1, which is structurally and functionally similar to mammalian dmt1 transporter, mediates phagosomal iron efflux. Journal of Cell Science, 128:3304-3316, Sep 2015. URL: https://doi.org/10.1242/jcs.173153, doi:10.1242/jcs.173153. This article has 47 citations and is from a domain leading peer-reviewed journal.

9. (ray2023structuresandcoordination pages 1-2): Shamayeeta Ray and Rachelle Gaudet. Structures and coordination chemistry of transporters involved in manganese and iron homeostasis. Biochemical Society transactions, 51:897-923, Jun 2023. URL: https://doi.org/10.1042/bst20210699, doi:10.1042/bst20210699. This article has 29 citations and is from a peer-reviewed journal.

10. (cellier2022nrampdepriveand pages 1-2): M. F. M. Cellier. Nramp: deprive and conquer? Frontiers in Cell and Developmental Biology, Oct 2022. URL: https://doi.org/10.3389/fcell.2022.988866, doi:10.3389/fcell.2022.988866. This article has 10 citations.

11. (cellier2022nrampdepriveand pages 2-7): M. F. M. Cellier. Nramp: deprive and conquer? Frontiers in Cell and Developmental Biology, Oct 2022. URL: https://doi.org/10.3389/fcell.2022.988866, doi:10.3389/fcell.2022.988866. This article has 10 citations.

12. (norberg2025slc11a2affectsnutritional pages 1-5): Emilia S. Norberg, Trina L. Westerman, Eddy Cruz, Summer D. Bushman, Eric P. Skaar, Johanna R. Elfenbein, and Leigh A. Knodler. Slc11a2 affects nutritional immunity in the gut epithelium. BioRxiv, Nov 2025. URL: https://doi.org/10.1101/2025.11.12.688034, doi:10.1101/2025.11.12.688034. This article has 1 citations.

13. (pasquadibisceglie2023membranetransportersinvolved pages 1-2): Andrea Pasquadibisceglie, Maria Carmela Bonaccorsi di Patti, Giovanni Musci, and Fabio Polticelli. Membrane transporters involved in iron trafficking: physiological and pathological aspects. Biomolecules, 13:1172, Jul 2023. URL: https://doi.org/10.3390/biom13081172, doi:10.3390/biom13081172. This article has 21 citations.

14. (wesslingresnick2015nramp1andother pages 1-2): Marianne Wessling-Resnick. Nramp1 and other transporters involved in metal withholding during infection. Journal of Biological Chemistry, 290:18984-18990, Jul 2015. URL: https://doi.org/10.1074/jbc.r115.643973, doi:10.1074/jbc.r115.643973. This article has 151 citations and is from a domain leading peer-reviewed journal.

15. (bosma2021regulationanddistinct pages 1-2): Elleke F Bosma, Martin H Rau, Lieke A van Gijtenbeek, and Solvej Siedler. Regulation and distinct physiological roles of manganese in bacteria. FEMS Microbiology Reviews, May 2021. URL: https://doi.org/10.1093/femsre/fuab028, doi:10.1093/femsre/fuab028. This article has 139 citations and is from a domain leading peer-reviewed journal.

16. (ray2023structuresandcoordination pages 8-9): Shamayeeta Ray and Rachelle Gaudet. Structures and coordination chemistry of transporters involved in manganese and iron homeostasis. Biochemical Society transactions, 51:897-923, Jun 2023. URL: https://doi.org/10.1042/bst20210699, doi:10.1042/bst20210699. This article has 29 citations and is from a peer-reviewed journal.

17. (ray2023structuresandcoordination pages 4-6): Shamayeeta Ray and Rachelle Gaudet. Structures and coordination chemistry of transporters involved in manganese and iron homeostasis. Biochemical Society transactions, 51:897-923, Jun 2023. URL: https://doi.org/10.1042/bst20210699, doi:10.1042/bst20210699. This article has 29 citations and is from a peer-reviewed journal.

18. (banerjee2025thesolutecarrier pages 1-3): Ruchira Banerjee, Bintee Bintee, Mukesh Kumar Manickasamy, Shristy Jha, Mohammed S. Alqahtani, Mohamed Abbas, Arul Goel, Gautam Sethi, Zhaowu Ma, and Ajaikumar B. Kunnumakkara. The solute carrier family 11 transporters: a bridge between iron homeostasis and tumor biology. Cell Communication and Signaling : CCS, Jul 2025. URL: https://doi.org/10.1186/s12964-025-02293-x, doi:10.1186/s12964-025-02293-x. This article has 8 citations.

19. (norberg2025slc11a2affectsnutritional pages 23-26): Emilia S. Norberg, Trina L. Westerman, Eddy Cruz, Summer D. Bushman, Eric P. Skaar, Johanna R. Elfenbein, and Leigh A. Knodler. Slc11a2 affects nutritional immunity in the gut epithelium. BioRxiv, Nov 2025. URL: https://doi.org/10.1101/2025.11.12.688034, doi:10.1101/2025.11.12.688034. This article has 1 citations.

## Artifacts

- [Edison artifact artifact-00](IPR001046-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](IPR001046-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. liziczai2025structuralbasisfor pages 4-6
2. liziczai2025structuralbasisfor pages 2-4
3. cellier2022nrampdepriveand pages 2-7
4. cellier2022nrampdepriveand pages 1-2
5. bosma2021regulationanddistinct pages 1-2
6. ray2023structuresandcoordination pages 8-9
7. banerjee2025thesolutecarrier pages 1-3
8. pasquadibisceglie2023membranetransportersinvolved pages 1-2
9. cellier2016evolutionaryanalysisof pages 1-4
10. cellier2016evolutionaryanalysisof pages 4-6
11. liziczai2025structuralbasisfor pages 6-8
12. liziczai2025structuralbasisfor pages 1-2
13. ray2023structuresandcoordination pages 1-2
14. ray2023structuresandcoordination pages 4-6
15. mntH
16. F
17. P
18. C
19. [cite:PUB00005530
20. cite:PUB00004854
21. cite:PUB00003001
22. cite:PUB00101161
23. cite:PUB00101162
24. cite:PUB00101160
25. cite:PUB00101163
26. [cite:PUB00101161
27. https://doi.org/10.3934/biophy.2016.2.286,
28. https://doi.org/10.1038/s41467-024-54705-0,
29. https://doi.org/10.1101/792127,
30. https://doi.org/10.1242/jcs.173153,
31. https://doi.org/10.1042/bst20210699,
32. https://doi.org/10.3389/fcell.2022.988866,
33. https://doi.org/10.1101/2025.11.12.688034,
34. https://doi.org/10.3390/biom13081172,
35. https://doi.org/10.1074/jbc.r115.643973,
36. https://doi.org/10.1093/femsre/fuab028,
37. https://doi.org/10.1186/s12964-025-02293-x,