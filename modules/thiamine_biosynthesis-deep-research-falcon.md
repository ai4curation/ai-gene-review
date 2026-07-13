---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-07T02:05:17.058623'
end_time: '2026-07-07T02:25:55.674776'
duration_seconds: 1238.62
template_file: templates/module_research.md.j2
template_variables:
  module_title: Thiamine biosynthesis
  module_summary: A bacterial thiamine diphosphate biosynthesis module covering formation
    of the hydroxymethylpyrimidine and thiazole moieties, condensation to thiamine
    monophosphate, and phosphorylation to the active thiamine diphosphate cofactor.
    In Pseudomonas putida KT2440, KEGG ppu00730 also includes shared precursor, sulfur-transfer,
    thiamine-salvage, nucleotide, and ribosome-side entries; those are treated as
    support or boundary context rather than all being strict thiamine-biosynthetic
    enzymes.
  module_outline: "- Thiamine biosynthesis\n  - 1. DXP precursor supply\n  - 1-deoxy-D-xylulose\
    \ 5-phosphate supply\n    - Dxs 1-deoxy-D-xylulose-5-phosphate synthase (molecular\
    \ player: PSEPK dxs; activity or role: 1-deoxy-D-xylulose-5-phosphate synthase\
    \ activity)\n  - 2. HMP-P formation\n  - Hydroxymethylpyrimidine phosphate formation\n\
    \    - ThiC phosphomethylpyrimidine synthase (molecular player: PSEPK thiC; activity\
    \ or role: phosphomethylpyrimidine synthase activity)\n  - 3. HMP phosphorylation\n\
    \  - Hydroxymethylpyrimidine phosphorylation\n    - ThiD hydroxymethylpyrimidine\
    \ kinase (molecular player: PSEPK thiD; activity or role: hydroxymethylpyrimidine\
    \ kinase activity)\n    - ThiD phosphomethylpyrimidine kinase (molecular player:\
    \ PSEPK thiD; activity or role: phosphomethylpyrimidine kinase activity)\n  -\
    \ 4. glyoxyl imine supply\n  - Glycine oxidation for thiazole synthesis\n    -\
    \ ThiO glycine oxidase (molecular player: PSEPK thiO; activity or role: glycine\
    \ oxidase activity)\n  - 5. sulfur transfer to the thiazole branch\n  - ThiS sulfur-carrier\
    \ charging\n    - ThiI sulfurtransferase (molecular player: PSEPK thiI; activity\
    \ or role: tRNA-uracil-4 sulfurtransferase activity)\n  - 6. thiazole phosphate\
    \ formation\n  - Thiazole phosphate formation\n    - ThiG thiazole synthase (molecular\
    \ player: PSEPK thiG; activity or role: thiazole synthase activity)\n  - 7. thiamine\
    \ monophosphate formation\n  - Thiamine monophosphate formation\n    - ThiE thiamine-phosphate\
    \ synthase (molecular player: PSEPK thiE; activity or role: thiamine-phosphate\
    \ diphosphorylase activity)\n  - 8. thiamine diphosphate formation\n  - Thiamine\
    \ diphosphate formation\n    - ThiL thiamine-phosphate kinase (molecular player:\
    \ PSEPK thiL; activity or role: thiamine-phosphate kinase activity)"
  module_connections: No explicit connections.
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 47
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: thiamine_biosynthesis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: thiamine_biosynthesis-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Commissioned Review Brief

## Review Topic

Thiamine biosynthesis

## Working Scope

A bacterial thiamine diphosphate biosynthesis module covering formation of the hydroxymethylpyrimidine and thiazole moieties, condensation to thiamine monophosphate, and phosphorylation to the active thiamine diphosphate cofactor. In Pseudomonas putida KT2440, KEGG ppu00730 also includes shared precursor, sulfur-transfer, thiamine-salvage, nucleotide, and ribosome-side entries; those are treated as support or boundary context rather than all being strict thiamine-biosynthetic enzymes.

## Provisional Biological Outline

- Thiamine biosynthesis
  - 1. DXP precursor supply
  - 1-deoxy-D-xylulose 5-phosphate supply
    - Dxs 1-deoxy-D-xylulose-5-phosphate synthase (molecular player: PSEPK dxs; activity or role: 1-deoxy-D-xylulose-5-phosphate synthase activity)
  - 2. HMP-P formation
  - Hydroxymethylpyrimidine phosphate formation
    - ThiC phosphomethylpyrimidine synthase (molecular player: PSEPK thiC; activity or role: phosphomethylpyrimidine synthase activity)
  - 3. HMP phosphorylation
  - Hydroxymethylpyrimidine phosphorylation
    - ThiD hydroxymethylpyrimidine kinase (molecular player: PSEPK thiD; activity or role: hydroxymethylpyrimidine kinase activity)
    - ThiD phosphomethylpyrimidine kinase (molecular player: PSEPK thiD; activity or role: phosphomethylpyrimidine kinase activity)
  - 4. glyoxyl imine supply
  - Glycine oxidation for thiazole synthesis
    - ThiO glycine oxidase (molecular player: PSEPK thiO; activity or role: glycine oxidase activity)
  - 5. sulfur transfer to the thiazole branch
  - ThiS sulfur-carrier charging
    - ThiI sulfurtransferase (molecular player: PSEPK thiI; activity or role: tRNA-uracil-4 sulfurtransferase activity)
  - 6. thiazole phosphate formation
  - Thiazole phosphate formation
    - ThiG thiazole synthase (molecular player: PSEPK thiG; activity or role: thiazole synthase activity)
  - 7. thiamine monophosphate formation
  - Thiamine monophosphate formation
    - ThiE thiamine-phosphate synthase (molecular player: PSEPK thiE; activity or role: thiamine-phosphate diphosphorylase activity)
  - 8. thiamine diphosphate formation
  - Thiamine diphosphate formation
    - ThiL thiamine-phosphate kinase (molecular player: PSEPK thiL; activity or role: thiamine-phosphate kinase activity)

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

Thiamine biosynthesis

## Working Scope

A bacterial thiamine diphosphate biosynthesis module covering formation of the hydroxymethylpyrimidine and thiazole moieties, condensation to thiamine monophosphate, and phosphorylation to the active thiamine diphosphate cofactor. In Pseudomonas putida KT2440, KEGG ppu00730 also includes shared precursor, sulfur-transfer, thiamine-salvage, nucleotide, and ribosome-side entries; those are treated as support or boundary context rather than all being strict thiamine-biosynthetic enzymes.

## Provisional Biological Outline

- Thiamine biosynthesis
  - 1. DXP precursor supply
  - 1-deoxy-D-xylulose 5-phosphate supply
    - Dxs 1-deoxy-D-xylulose-5-phosphate synthase (molecular player: PSEPK dxs; activity or role: 1-deoxy-D-xylulose-5-phosphate synthase activity)
  - 2. HMP-P formation
  - Hydroxymethylpyrimidine phosphate formation
    - ThiC phosphomethylpyrimidine synthase (molecular player: PSEPK thiC; activity or role: phosphomethylpyrimidine synthase activity)
  - 3. HMP phosphorylation
  - Hydroxymethylpyrimidine phosphorylation
    - ThiD hydroxymethylpyrimidine kinase (molecular player: PSEPK thiD; activity or role: hydroxymethylpyrimidine kinase activity)
    - ThiD phosphomethylpyrimidine kinase (molecular player: PSEPK thiD; activity or role: phosphomethylpyrimidine kinase activity)
  - 4. glyoxyl imine supply
  - Glycine oxidation for thiazole synthesis
    - ThiO glycine oxidase (molecular player: PSEPK thiO; activity or role: glycine oxidase activity)
  - 5. sulfur transfer to the thiazole branch
  - ThiS sulfur-carrier charging
    - ThiI sulfurtransferase (molecular player: PSEPK thiI; activity or role: tRNA-uracil-4 sulfurtransferase activity)
  - 6. thiazole phosphate formation
  - Thiazole phosphate formation
    - ThiG thiazole synthase (molecular player: PSEPK thiG; activity or role: thiazole synthase activity)
  - 7. thiamine monophosphate formation
  - Thiamine monophosphate formation
    - ThiE thiamine-phosphate synthase (molecular player: PSEPK thiE; activity or role: thiamine-phosphate diphosphorylase activity)
  - 8. thiamine diphosphate formation
  - Thiamine diphosphate formation
    - ThiL thiamine-phosphate kinase (molecular player: PSEPK thiL; activity or role: thiamine-phosphate kinase activity)

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

# Bacterial Thiamine Diphosphate Biosynthesis: A Review of Core Mechanisms, Evolutionary Variation, and Open Questions

## 1. Executive Summary

Thiamine diphosphate (ThDP, also called thiamine pyrophosphate, TPP) is an essential cofactor for central metabolic enzymes including pyruvate dehydrogenase, α-ketoglutarate dehydrogenase, and transketolase. Bacteria synthesize ThDP de novo through a modular pathway that independently assembles two heterocyclic precursors—a hydroxymethylpyrimidine diphosphate (HMP-PP) and a thiazole phosphate (THZ-P)—then condenses and phosphorylates them to yield the active cofactor. This review uses the *Pseudomonas putida* KT2440 gene complement (KEGG ppu00730) as a reference framework to describe the eight obligatory enzymatic steps of the canonical bacterial pathway, the support systems at its boundaries (precursor supply, sulfur transfer, salvage, transport, and regulation), and the evolutionary alternatives that distinguish bacterial thiamine biosynthesis from the pathways in archaea, fungi, and plants. Key recent developments include detailed mechanistic studies of the radical SAM enzyme ThiC, the identification of ThiI/ThiL as antibacterial drug targets in *Pseudomonas aeruginosa*, the elucidation of allosteric DXS regulation by MEP pathway products, and growing evidence that thiamine precursor exchange shapes microbial community composition.

## 2. Definition and Biological Boundaries

### 2.1 What the system includes

The bacterial ThDP biosynthesis module, as exemplified in *P. putida* KT2440, encompasses three converging branches and a final phosphorylation step:

1. **The pyrimidine branch**: converts the purine biosynthesis intermediate 5-aminoimidazole ribotide (AIR) to HMP-PP via ThiC and ThiD.
2. **The thiazole branch**: assembles THZ-P from 1-deoxy-D-xylulose 5-phosphate (DXP, supplied by Dxs), a dehydroglycine intermediate (supplied by ThiO or ThiH), and sulfur mobilized through the ThiI–ThiS relay, with ThiG catalyzing ring closure.
3. **The condensation and phosphorylation steps**: ThiE condenses HMP-PP and THZ-P to form thiamine monophosphate (TMP), and ThiL phosphorylates TMP to ThDP (maupinfurlow2018vitaminb1(thiamine) pages 4-7, maupinfurlow2018vitaminb1(thiamine) pages 7-9).

### 2.2 Boundary processes treated separately

KEGG ppu00730 maps several processes that feed into or draw from thiamine metabolism but are not strictly biosynthetic enzymes:

- **Precursor supply**: Dxs is a branch-point enzyme shared with the methylerythritol 4-phosphate (MEP) isoprenoid pathway and pyridoxal phosphate (PLP) biosynthesis (bartee2018targetingtheunique pages 1-3, tramonti2021knownsandunknowns pages 10-12). Similarly, ThiC diverts AIR from purine biosynthesis.
- **Sulfur mobilization**: ThiI participates in both thiamine biosynthesis and tRNA 4-thiouridine modification, with its rhodanese domain being specifically required for sulfur transfer to the thiazole branch (maupinfurlow2018vitaminb1(thiamine) pages 17-19).
- **Salvage pathways**: Bacteria employ salvage enzymes (thiamine pyrophosphokinase, thiamine kinase, TenA aminohydrolases, ThiM thiazole kinase) to recycle exogenous thiamine and its breakdown products (maupinfurlow2018vitaminb1(thiamine) pages 19-22, maupinfurlow2018vitaminb1(thiamine) pages 17-19).
- **Transport**: ABC-type thiamine transporters (ThiBPQ, ThiYXZ) and secondary carriers (PnuT) import intact thiamine or precursors but are not biosynthetic enzymes per se (maupinfurlow2018vitaminb1(thiamine) pages 7-9).
- **Regulation**: TPP riboswitches in 5′ UTRs of biosynthesis and transport operons constitute the primary regulatory layer in most bacteria (hwang2017thinasa pages 3-5, hubenthal2024influenceofantimicrobial pages 104-107).

### 2.3 Competing definitions

The KEGG "Thiamine metabolism" map (map00730) is inclusive, listing salvage, transport, riboswitch-associated, and even ribosome-related entries alongside strictly biosynthetic enzymes. Comparative genomic reconstructions have noted that many organisms possess only a subset of these genes, and the presence of a biosynthetic operon (e.g., *thiSEGCHF-tenI* in Bacteroidetes) does not always imply a complete de novo pathway if critical precursor supply is absent (costliow2017thiamineacquisitionstrategies pages 10-11, costliow2017thiamineacquisitionstrategies pages 2-4).

## 3. Mechanistic Overview

The following table summarizes the core enzymes and their functions in the canonical bacterial thiamine biosynthesis pathway:

| Enzyme name | Gene | EC number | Reaction catalyzed | Substrates | Products | Cofactors/requirements | Evolutionary distribution |
|---|---|---:|---|---|---|---|---|
| 1-Deoxy-D-xylulose-5-phosphate synthase | **dxs** | EC 2.2.1.7 | ThDP-dependent condensation of pyruvate with D-glyceraldehyde-3-phosphate to form DXP, the shared precursor feeding the thiazole branch as well as MEP isoprenoid and PLP biosynthesis | Pyruvate; D-glyceraldehyde-3-phosphate | 1-Deoxy-D-xylulose-5-phosphate (DXP); CO2 | **ThDP** cofactor; active dimer; distinctive ternary-complex mechanism with lactyl-ThDP intermediate | Widespread in bacteria; also found in plants/green algae/protists, but DXP use for **thiamine** biosynthesis is characteristically bacterial (bartee2018targetingtheunique pages 1-3, maupinfurlow2018vitaminb1(thiamine) pages 4-7, di2022allostericfeedbackinhibition pages 7-11) |
| Phosphomethylpyrimidine synthase | **thiC** | EC 4.1.99.17 | Radical-SAM rearrangement converting AIR to HMP-P, establishing the aminopyrimidine branch | 5-Aminoimidazole ribotide (AIR); SAM | 4-Amino-5-hydroxymethyl-2-methylpyrimidine phosphate (HMP-P); methionine; 5'-deoxyadenosine | Radical SAM enzyme; **[4Fe-4S]** cluster; reductive activation of SAM | Conserved in bacteria, archaea, and plant chloroplasts; alternative **THI5**-based HMP formation occurs in fungi/plants and some other lineages (maupinfurlow2018vitaminb1(thiamine) pages 4-7, strakova2024unveilingthegenomic pages 11-13) |
| Hydroxymethylpyrimidine kinase / phosphomethylpyrimidine kinase | **thiD** | EC 2.7.1.49 / EC 2.7.4.7 | Sequential phosphorylation of HMP to HMP-P and HMP-P to HMP-PP (in many bacteria the same ThiD is bifunctional; in the core de novo branch emphasized here, ThiD supplies HMP-PP for ThiE) | HMP or HMP-P; ATP | HMP-P or HMP-PP; ADP | ATP-dependent kinase activity | Broadly distributed in bacteria; archaeal variants can be associated with ThiN-like domain architectures (maupinfurlow2018vitaminb1(thiamine) pages 7-9, strakova2024unveilingthegenomic pages 11-13, maupinfurlow2018vitaminb1(thiamine) pages 4-7) |
| Glycine oxidase | **thiO** | EC 1.4.3.19 | Oxidative deamination of glycine to the imine/dehydroglycine precursor used in thiazole synthesis | Glycine; O2 | Dehydroglycine/2-iminoacetate-derived intermediate (often observed as glyoxylate after spontaneous breakdown); NH3; H2O2 | Typically **FAD-dependent** oxidase; oxygen-dependent chemistry | Broadly distributed in bacteria, including **Pseudomonas putida** (PP_0612); not universal even in bacteria (maupinfurlow2018vitaminb1(thiamine) pages 4-7, turlin2025syntheticc1metabolism pages 4-7) |
| Tyrosine lyase (alternative to ThiO) | **thiH** | EC 4.1.99.- | Radical-SAM cleavage of L-tyrosine to generate dehydroglycine for thiazole synthesis; functional alternative to ThiO in some bacteria | L-Tyrosine; SAM | Dehydroglycine; p-cresol; 5'-deoxyadenosine; methionine | Radical SAM enzyme; **[4Fe-4S]** cluster | Broadly distributed but patchy in bacteria; generally absent from archaea/eukaryotes; interchangeable with ThiO at the level of supplying dehydroglycine (maupinfurlow2018vitaminb1(thiamine) pages 4-7, ruszczycky2024initiationpropagationand pages 14-16) |
| Sulfurtransferase / sulfur relay component | **thiI** | EC 2.8.1.- | Mobilizes sulfane sulfur into the thiazole pathway, transferring sulfur from cysteine-derived persulfide relay to the ThiS carrier system | Sulfur from cysteine via cysteine desulfurase/persulfide relay; ThiS pathway intermediates | ThiS-thiocarboxylate precursor state enabling sulfur insertion into thiazole | Persulfide chemistry; rhodanese-like sulfurtransferase domain in many bacterial ThiI proteins; function linked to IscS-like sulfur mobilization | Bacterial ThiG pathway component; also participates in tRNA thiolation in many organisms, so not every ThiI homolog is dedicated solely to thiamine biosynthesis (maupinfurlow2018vitaminb1(thiamine) pages 17-19, maupinfurlow2018vitaminb1(thiamine) pages 4-7) |
| Sulfur carrier protein | **thiS** | — | Small sulfur-carrier protein that is adenylated/activated and converted to a **thiocarboxylate**, which donates sulfur during thiazole formation by ThiG | Activated ThiS; sulfur relay input from ThiI-linked pathway | ThiS-thiocarboxylate sulfur donor; desulfurized ThiS after transfer | Carrier protein rather than classical enzyme; requires upstream activation/sulfur loading machinery | Characteristic of the bacterial **ThiG-dependent** thiazole pathway; absent from Thi4-based systems (maupinfurlow2018vitaminb1(thiamine) pages 4-7, maupinfurlow2018vitaminb1(thiamine) pages 7-9) |
| Thiazole synthase | **thiG** | EC 2.8.1.10 | Assembly of thiazole phosphate from DXP, dehydroglycine-derived fragment, and sulfur carried by thiocarboxylated ThiS | DXP; dehydroglycine precursor (from ThiO or ThiH); ThiS-thiocarboxylate | Thiazole phosphate (THZ-P / cThz-P) | Requires prior sulfur loading onto ThiS; depends on DXP supply and dehydroglycine supply | Canonical bacterial thiazole synthase; functionally replaced by **Thi4** systems in archaea, fungi, plants, and some bacteria (maupinfurlow2018vitaminb1(thiamine) pages 4-7, costliow2017thiamineacquisitionstrategies pages 10-11, maupinfurlow2018vitaminb1(thiamine) pages 7-9) |
| Thiamine-phosphate synthase | **thiE** | EC 2.5.1.3 | Condensation of HMP-PP with THZ-P to form thiamine monophosphate (TMP/ThMP) | HMP-PP; THZ-P | Thiamine monophosphate (TMP/ThMP); PPi; CO2 | No special redox cofactor required; convergence step of pyrimidine and thiazole branches | Widespread and near-universal in de novo thiamine synthesis; in some lineages function can be replaced or supplemented by ThiN-related enzymes/YjbQ-like alternatives (maupinfurlow2018vitaminb1(thiamine) pages 7-9, strakova2024unveilingthegenomic pages 11-13, costliow2017thiamineacquisitionstrategies pages 10-11) |
| Thiamine monophosphate kinase | **thiL** | EC 2.7.4.16 | ATP-dependent phosphorylation of TMP/ThMP to active ThDP/TPP | Thiamine monophosphate (TMP/ThMP); ATP | Thiamine diphosphate (ThDP/TPP); ADP | ATP-dependent kinase; structural work supports in-line phosphoryl transfer and metal-assisted catalysis | Broadly conserved in bacteria and many archaea; essential in bacteria that rely on both de novo synthesis and salvage to generate active ThDP (sullivan2019crystalstructuresof pages 1-2, hayashi2015characterizationofthiamin pages 4-6, kim2022pharmacologicalperturbationof pages 9-9) |


*Table: This table summarizes the core bacterial thiamine diphosphate biosynthesis module, including the central enzymes, the sulfur-carrier protein ThiS, and the ThiH alternative to ThiO. It is useful as a pathway map for interpreting the canonical bacterial route, especially in the Pseudomonas putida KT2440 framework.*

### 3.1 DXP precursor supply (Step 1)

Dxs (1-deoxy-D-xylulose-5-phosphate synthase; EC 2.2.1.7) catalyzes the ThDP-dependent condensation of pyruvate with D-glyceraldehyde-3-phosphate (D-GAP) to generate DXP and CO₂. This enzyme employs a distinctive random sequential mechanism requiring formation of a ternary complex among the pyruvate-derived C2α-lactylthiamin diphosphate (LThDP) intermediate, D-GAP, and the enzyme, which sets it apart from all other ThDP-dependent enzymes that typically use a ping-pong mechanism (bartee2018targetingtheunique pages 1-3, bartee2018targetingtheunique pages 11-16). DXP is a metabolic branch-point feeding into the MEP isoprenoid pathway (via IspC/DXR), PLP biosynthesis (via PdxA/PdxJ), and the thiazole branch of thiamine biosynthesis (tramonti2021knownsandunknowns pages 10-12, maupinfurlow2018vitaminb1(thiamine) pages 4-7). The active enzyme functions as a homodimer, and its activity is feedback-regulated by the MEP pathway end-products IPP and DMAPP, which allosterically promote monomerization and eventual aggregation of the enzyme (di2023meppathwayproducts pages 5-7, di2023meppathwayproducts pages 1-2). DXP-dependent thiamine biosynthesis is characteristically bacterial; eukaryotes and archaea do not use DXP for this purpose (maupinfurlow2018vitaminb1(thiamine) pages 4-7).

### 3.2 HMP-P formation (Step 2)

ThiC (phosphomethylpyrimidine synthase; EC 4.1.99.17) is a radical S-adenosylmethionine (SAM) enzyme that rearranges AIR into HMP-P, thereby diverting carbon and nitrogen skeletons from purine metabolism into thiamine biosynthesis. The catalytic mechanism is initiated by a [4Fe-4S]⁺ cluster that reductively cleaves SAM to produce methionine and a 5′-deoxyadenosyl radical, which serves as the oxidizing cosubstrate to drive the complex rearrangement reaction (maupinfurlow2018vitaminb1(thiamine) pages 4-7). Recent work by Sharma et al. (2024) trapped five intermediate species during the ThiC reaction, providing mechanistic insights into this radical cascade—one of the most complex known single-enzyme transformations in biology (DOI: 10.1021/acscentsci.4c00125, unobtainable but cited in search results). ThiC is conserved across bacteria, archaea, and plant chloroplasts; fungi and some γ-proteobacteria instead use the unrelated THI5 family, which generates HMP from PLP and histidine (maupinfurlow2018vitaminb1(thiamine) pages 4-7).

### 3.3 HMP phosphorylation (Step 3)

ThiD (hydroxymethylpyrimidine kinase / phosphomethylpyrimidine kinase; EC 2.7.1.49 / EC 2.7.4.7) catalyzes the ATP-dependent phosphorylation of HMP-P to HMP-PP. In many bacteria, ThiD is bifunctional, performing both phosphorylation steps (HMP → HMP-P and HMP-P → HMP-PP), allowing it to serve both the de novo branch and salvage of free HMP imported from the environment (maupinfurlow2018vitaminb1(thiamine) pages 7-9, strakova2024unveilingthegenomic pages 11-13).

### 3.4 Glycine oxidation for thiazole synthesis (Step 4)

The thiazole branch requires a dehydroglycine (iminoglycine) intermediate. Two alternative enzymes supply this substrate in different bacterial lineages. ThiO is an FAD-dependent glycine oxidase that catalyzes the oxidative deamination of glycine to 2-iminoacetate/dehydroglycine, releasing NH₃ and H₂O₂. In *P. putida* KT2440, ThiO is encoded by PP_0612 (turlin2025syntheticc1metabolism pages 4-7). The alternative enzyme, ThiH, is a radical SAM tyrosine lyase that cleaves the Cα–Cβ bond of L-tyrosine to generate dehydroglycine and p-cresol. ThiH employs hydrogen atom abstraction from the amino group of tyrosine and possesses dedicated substrate channels to prevent hydrolysis of the labile dehydroglycine product (maupinfurlow2018vitaminb1(thiamine) pages 4-7, ruszczycky2024initiationpropagationand pages 14-16). Both ThiO (oxygen-dependent) and ThiH (anaerobic/radical SAM) are broadly but patchily distributed in bacteria, reflecting different ecological adaptations; they are generally absent from archaea and eukaryotes (maupinfurlow2018vitaminb1(thiamine) pages 4-7).

### 3.5 Sulfur transfer (Step 5)

The sulfur atom of the thiazole ring is delivered through a protein-based relay. In the canonical bacterial pathway, a cysteine desulfurase (such as IscS) mobilizes sulfane sulfur from L-cysteine, forming an enzyme persulfide intermediate. This sulfur is transferred to ThiI, specifically to its rhodanese domain, which is both necessary and sufficient for sulfur donation to the thiazole pathway in *Salmonella enterica*. ThiI in turn loads sulfur onto the small carrier protein ThiS, converting it to a thiocarboxylated form (ThiS-COSH) that serves as the proximal sulfur donor for ThiG (maupinfurlow2018vitaminb1(thiamine) pages 17-19, maupinfurlow2018vitaminb1(thiamine) pages 4-7). Notably, ThiI is a dual-function protein: it also catalyzes 4-thiouridine modification at position 8 of tRNA, an activity that uses the same sulfur mobilization chemistry but a different acceptor (maupinfurlow2018vitaminb1(thiamine) pages 17-19). The ThiS-ThiI relay mechanism has been compared to the ubiquitin/E1 conjugation system, as ThiS is adenylated before thiocarboxylation (maupinfurlow2018vitaminb1(thiamine) pages 17-19).

### 3.6 Thiazole phosphate formation (Step 6)

ThiG (thiazole synthase; EC 2.8.1.10) catalyzes the assembly of the thiazole ring from three substrates: DXP, the dehydroglycine precursor (from ThiO or ThiH), and thiocarboxylated ThiS. The reaction involves at least six steps and produces thiazole phosphate (THZ-P) (maupinfurlow2018vitaminb1(thiamine) pages 4-7). The ThiG-dependent pathway is characteristically bacterial; it is functionally replaced by Thi4-type thiazole synthases in archaea, fungi, and plants (maupinfurlow2018vitaminb1(thiamine) pages 4-7, maupinfurlow2018vitaminb1(thiamine) pages 7-9).

### 3.7 Thiamine monophosphate formation (Step 7)

ThiE (thiamine-phosphate synthase; EC 2.5.1.3) catalyzes the condensation of HMP-PP and THZ-P to form thiamine monophosphate (TMP), releasing pyrophosphate and CO₂. This convergence step couples the aminopyrimidine and thiazole branches. Crystal structures of ThiE from *Bacillus subtilis* have been solved at 1.25 Å resolution (maupinfurlow2018vitaminb1(thiamine) pages 17-19). In some bacterial lineages, YjbQ can substitute for ThiE, and in archaea and some bacteria, ThiN-domain proteins perform the equivalent condensation reaction (costliow2017thiamineacquisitionstrategies pages 10-11, maupinfurlow2018vitaminb1(thiamine) pages 7-9).

### 3.8 Thiamine diphosphate formation (Step 8)

ThiL (thiamine-monophosphate kinase; EC 2.7.4.16) catalyzes the final ATP-dependent phosphorylation of TMP to ThDP. Crystal structures of ThiL from *Acinetobacter baumannii* in complex with substrates (TMP + AMPPNP) and products (TPP + ADP) support an in-line phosphoryl transfer mechanism with variable metal content at the active site (sullivan2019crystalstructuresof pages 1-2). Key catalytic residues include a conserved arginine (interacting with the β-phosphate of ADP) and a serine (involved in ATP recognition), both conserved across bacterial and archaeal ThiL proteins (hayashi2015characterizationofthiamin pages 4-6, hayashi2015characterizationofthiamin pages 6-6). ThiL is essential for both de novo biosynthesis and salvage in bacteria, as validated in *P. aeruginosa* where it has been identified as a valid antibacterial target (kim2022pharmacologicalperturbationof pages 9-9).

## 4. Major Molecular Players and Active Assemblies

The core biosynthetic module comprises eight enzymes (Dxs, ThiC, ThiD, ThiO, ThiI, ThiG, ThiE, ThiL) plus the sulfur carrier protein ThiS, as detailed in Table 1 above.

## 5. Evolutionary and Cell-Biological Variation

The following table summarizes how thiamine biosynthesis solutions differ across the three domains of life:

| Pathway feature | Bacteria (canonical) | Archaea | Fungi/Yeast | Plants |
|---|---|---|---|---|
| Aminopyrimidine (HMP) synthesis enzyme | **ThiC** radical SAM phosphomethylpyrimidine synthase converts AIR to HMP-P; broadly canonical in bacteria (maupinfurlow2018vitaminb1(thiamine) pages 4-7) | Commonly **ThiC**-type, giving archaea a bacterial-like HMP branch (maupinfurlow2018vitaminb1(thiamine) pages 4-7, maupinfurlow2018vitaminb1(thiamine) pages 9-12, strakova2024unveilingthegenomic pages 11-13) | Often **THI5** family rather than ThiC; THI5-based HMP formation is a key eukaryotic divergence (maupinfurlow2018vitaminb1(thiamine) pages 4-7, maupinfurlow2018vitaminb1(thiamine) pages 14-17) | Mainly **THIC** in chloroplasts, a ThiC homolog and Fe-S/radical SAM enzyme; plant pathway is bacterial-like for the pyrimidine branch (strobbe2021metabolicengineeringprovides pages 1-2, maupinfurlow2018vitaminb1(thiamine) pages 4-7) |
| Thiazole ring synthesis enzyme | Usually **ThiG** thiazole synthase in the canonical bacterial de novo pathway (maupinfurlow2018vitaminb1(thiamine) pages 4-7, maupinfurlow2018vitaminb1(thiamine) pages 7-9) | Commonly **Thi4**-type thiazole synthase; archaeal pathway is often hybrid, with bacterial-like ThiC plus eukaryote-like Thi4 (maupinfurlow2018vitaminb1(thiamine) pages 7-9, hwang2017thinasa pages 3-5, strakova2024unveilingthegenomic pages 11-13) | **THI4** thiazole synthase; in yeast this is the classic thiazole-forming enzyme (maupinfurlow2018vitaminb1(thiamine) pages 7-9, maupinfurlow2018vitaminb1(thiamine) pages 14-17, sun2019partsprospectingfora pages 1-2) | **THI1/THI4-like** thiazole synthase in plastids; plant branch is Thi4-type rather than ThiG-type (strobbe2021metabolicengineeringprovides pages 1-2, sun2019partsprospectingfora pages 1-2, maupinfurlow2018vitaminb1(thiamine) pages 4-7) |
| Thiazole sulfur source mechanism | Sulfur delivered through a **ThiI/ThiS carrier relay** to the ThiG pathway; sulfur ultimately mobilized from cysteine-derived persulfide chemistry (maupinfurlow2018vitaminb1(thiamine) pages 17-19, maupinfurlow2018vitaminb1(thiamine) pages 4-7) | Variable **Thi4** chemistry; some archaeal Thi4 proteins use active-site Cys, whereas histidine-containing methanogen/thermococcal variants use **exogenous sulfide** (maupinfurlow2018vitaminb1(thiamine) pages 7-9, strakova2024unveilingthegenomic pages 11-13) | Classic yeast **suicide THI4** uses an active-site cysteine that is consumed during one turnover (maupinfurlow2018vitaminb1(thiamine) pages 14-17, sun2019partsprospectingfora pages 1-2, sun2019partsprospectingfora pages 10-11) | Plant **THI1** is also largely **suicidal**, donating sulfur from an internal cysteine and then becoming inactivated (strobbe2021metabolicengineeringprovides pages 1-2, sun2019partsprospectingfora pages 1-2) |
| ThMP synthase type | Usually **ThiE** condenses HMP-PP with THZ-P to form ThMP; some bacterial groups also encode **YjbQ** alternatives (costliow2017thiamineacquisitionstrategies pages 10-11, maupinfurlow2018vitaminb1(thiamine) pages 7-9) | **ThiE** and/or **ThiN-domain** fusions or recombinants; ThiN may be catalytic in some archaeal proteins (strakova2024unveilingthegenomic pages 11-13, maupinfurlow2018vitaminb1(thiamine) pages 7-9, hwang2017thinasa pages 3-5) | **Thi6**-type bifunctional enzyme commonly performs HMP-P kinase plus ThMP synthase functions in fungi/yeast (hwang2017thinasa pages 3-5) | **TH1** is bifunctional, combining HMP-P kinase and ThMP pyrophosphorylase activities (strobbe2021metabolicengineeringprovides pages 1-2, strobbe2021metabolicengineeringprovides pages 1-1) |
| TMP to ThDP kinase | Usually **ThiL** thiamine monophosphate kinase, ATP-dependent, conserved in many bacteria (maupinfurlow2018vitaminb1(thiamine) pages 7-9, sullivan2019crystalstructuresof pages 1-2) | Often **ThiL** as well, although salvage logic and kinase complements can vary among archaeal groups (maupinfurlow2018vitaminb1(thiamine) pages 7-9, hayashi2015characterizationofthiamin pages 4-6) | Typically **thiamine pyrophosphokinase (TPK)** rather than bacterial ThiL logic (maupinfurlow2018vitaminb1(thiamine) pages 7-9, maupinfurlow2018vitaminb1(thiamine) pages 19-22) | Predominantly **TPK/TPK-like** pyrophosphorylation in plant cells; bacterial ThiL can augment flux when ectopically expressed (strobbe2021metabolicengineeringprovides pages 1-2) |
| Regulatory mechanism | Frequently **TPP riboswitches** in 5' UTRs controlling biosynthesis/transport genes; common in many bacterial clades (hwang2017thinasa pages 3-5, kim2022pharmacologicalperturbationof pages 9-9, hubenthal2024influenceofantimicrobial pages 104-107) | Often **ThiR**, a ThiN-domain transcriptional repressor/sensor, rather than canonical bacterial riboswitch control (hwang2017thinasa pages 3-5, strakova2024unveilingthegenomic pages 11-13) | **THI-box/TPP riboswitch-like** control can act through alternative splicing, plus transcription factors such as **Thi2p/Thi3p/Pdc2p** in yeast (hwang2017thinasa pages 3-5, maupinfurlow2018vitaminb1(thiamine) pages 19-22) | Strong **TPP riboswitch** control of **THIC** in the 3' UTR; plant regulation is post-transcriptional and end-product responsive (strobbe2021metabolicengineeringprovides pages 1-2, strobbe2021metabolicengineeringprovides pages 16-16) |
| DXP involvement | **Yes**; Dxs makes DXP, a branch-point precursor for the canonical bacterial thiazole pathway and also for MEP isoprenoids/PLP (bartee2018targetingtheunique pages 1-3, maupinfurlow2018vitaminb1(thiamine) pages 4-7) | Generally **no** for thiamine biosynthesis; archaeal thiamine pathways do not use the bacterial DXP-dependent logic (maupinfurlow2018vitaminb1(thiamine) pages 4-7, maupinfurlow2018vitaminb1(thiamine) pages 7-9) | **No**; fungal/yeast thiamine synthesis is not DXP-based (maupinfurlow2018vitaminb1(thiamine) pages 4-7, maupinfurlow2018vitaminb1(thiamine) pages 7-9) | **No** for thiamine branch, despite plastids containing DXS for isoprenoid metabolism; plant thiamine pathway uses THIC/THI1 logic instead (maupinfurlow2018vitaminb1(thiamine) pages 4-7, strobbe2021metabolicengineeringprovides pages 1-2) |
| Notable alternative/variant enzymes | **ThiO** or **ThiH** can alternatively supply dehydroglycine; some bacteria replace ThiG branch with **THI4-like** thiazole synthesis; **YjbQ** can substitute for ThiE in some taxa (costliow2017thiamineacquisitionstrategies pages 10-11, maupinfurlow2018vitaminb1(thiamine) pages 4-7) | Hybrid pathway architecture is a hallmark; **ThiN** domains can be catalytic or regulatory, and Thi4 variants differ in sulfur donor strategy (maupinfurlow2018vitaminb1(thiamine) pages 7-9, hwang2017thinasa pages 3-5, strakova2024unveilingthegenomic pages 11-13) | **Suicide THI4** is the signature variant; THI5 family shows redundancy and lineage-specific distribution (maupinfurlow2018vitaminb1(thiamine) pages 14-17, sun2019partsprospectingfora pages 10-11) | **Nonsuicidal THI4/THI1-like** candidates in some cereals are of engineering interest; branch balancing and salvage capacity strongly constrain biofortification (strobbe2021metabolicengineeringprovides pages 12-12, sun2019partsprospectingfora pages 1-2) |


*Table: This table compares the major evolutionary solutions for thiamine biosynthesis across bacteria, archaea, fungi/yeast, and plants. It highlights which pathway features are deeply conserved, which were replaced in specific lineages, and where hybrid or accessory variants complicate simple cross-domain comparisons.*

### 5.1 Bacteria

The canonical bacterial pathway, as exemplified in *E. coli*, *Salmonella*, and *P. putida*, uses ThiC for the pyrimidine branch, the ThiG/ThiO(ThiH)/ThiI/ThiS module for the thiazole branch, ThiE for condensation, and ThiL for the final phosphorylation. TPP riboswitches typically regulate expression of biosynthetic operons (hwang2017thinasa pages 3-5, hubenthal2024influenceofantimicrobial pages 104-107). Some Bacteroidetes have replaced the canonical ThiG-based thiazole pathway with a THI4-like enzyme, demonstrating intra-bacterial variation (costliow2017thiamineacquisitionstrategies pages 10-11). Of 641 gut-associated microbial genomes surveyed, only 48% encoded a complete de novo pathway; 94% of gut Bacteroidetes specifically encode both biosynthesis and transport genes (costliow2017thiamineacquisitionstrategies pages 8-10).

### 5.2 Archaea

Archaea display a chimeric architecture, typically combining a bacterial-like ThiC for HMP synthesis with a eukaryote-like Thi4 for thiazole synthesis. The DXP-dependent route is absent (maupinfurlow2018vitaminb1(thiamine) pages 4-7, maupinfurlow2018vitaminb1(thiamine) pages 7-9). Archaeal Thi4 variants differ in their sulfur donor strategy: cysteine-containing versions operate via a single-turnover (suicide) mechanism similar to yeast, while histidine-containing versions found in methanogens and thermococci use exogenous sulfide and iron, enabling catalytic turnover (maupinfurlow2018vitaminb1(thiamine) pages 7-9, strakova2024unveilingthegenomic pages 11-13). Regulation in many archaea proceeds through ThiR, a ThiN-domain transcriptional repressor, rather than TPP riboswitches (hwang2017thinasa pages 3-5, strakova2024unveilingthegenomic pages 11-13).

### 5.3 Fungi and yeast

Yeast such as *Saccharomyces cerevisiae* use THI5 (not ThiC) for HMP synthesis and THI4 as a suicide thiazole synthase. Thi6p is a bifunctional enzyme combining HMP-P kinase and ThMP synthase activities. Regulation involves transcription factors (Thi2p/Thi3p/Pdc2p) and TPP-responsive THI-box elements (hwang2017thinasa pages 3-5, maupinfurlow2018vitaminb1(thiamine) pages 14-17). The suicide mechanism of yeast THI4, in which the active-site cysteine is consumed during each catalytic cycle, makes thiamine biosynthesis energetically very expensive (sun2019partsprospectingfora pages 1-2, sun2019partsprospectingfora pages 10-11).

### 5.4 Plants

Plant thiamine biosynthesis is compartmentalized to chloroplasts and uses THIC (a radical SAM enzyme homologous to bacterial ThiC) for HMP-P synthesis and THI1/THI4 for thiazole synthesis. TH1 is a bifunctional HMP-P kinase/TMP pyrophosphorylase. THIC expression is regulated by a TPP riboswitch in the 3′ UTR (strobbe2021metabolicengineeringprovides pages 1-2, strobbe2021metabolicengineeringprovides pages 1-1). Plant THI1 is largely suicidal, and its turnover has been estimated to consume 2–12% of the maintenance energy budget in crop plants, motivating efforts to install nonsuicidal alternatives for yield improvement (sun2019partsprospectingfora pages 1-2, strobbe2021metabolicengineeringprovides pages 12-12).

### 5.5 Conservation and origin

The aminopyrimidine branch (ThiC/ThiD) appears ancient and is conserved across bacteria, archaea, and plant chloroplasts (maupinfurlow2018vitaminb1(thiamine) pages 9-12). The Thi4-type thiazole pathway is also ancient, found in all domains of life, while the ThiG-dependent pathway appears limited to bacteria (maupinfurlow2018vitaminb1(thiamine) pages 4-7, maupinfurlow2018vitaminb1(thiamine) pages 7-9). ThiE-type synthases are near-universal, while ThiN-type synthases appear in archaea and some bacteria but are absent from eukaryotes (maupinfurlow2018vitaminb1(thiamine) pages 7-9). The ThiL kinase is broadly conserved in bacteria and archaea, whereas eukaryotes generally use a distinct thiamine pyrophosphokinase (TPK) to generate ThDP (maupinfurlow2018vitaminb1(thiamine) pages 7-9).

## 6. Constraints, Dependencies, and Failure Modes

### 6.1 Obligatory ordering

The pathway has a strict linear dependency in each branch: HMP-P must be phosphorylated by ThiD before ThiE can condense it with THZ-P; ThiS must be thiocarboxylated before ThiG can incorporate sulfur; and TMP must be formed before ThiL can phosphorylate it. The two branches (pyrimidine and thiazole) are otherwise independent and converge only at the ThiE step (maupinfurlow2018vitaminb1(thiamine) pages 7-9).

### 6.2 Substrate channeling and metabolite leakage

The dehydroglycine intermediate generated by ThiO or ThiH is chemically labile and prone to hydrolysis to glyoxylate. ThiH possesses substrate channels that ferry dehydroglycine to the next active site, preventing its decomposition (ruszczycky2024initiationpropagationand pages 14-16). Similarly, the thiocarboxylated ThiS must be delivered directly to ThiG to prevent sulfur loss.

### 6.3 Precursor sharing and community constraints

Thiamine precursor exchange is an ecological reality. HMP is more frequently shared between bacterial species than THZ, consistent with widespread HMP auxotrophy in natural environments and the absence of known dedicated THZ transporters (sathe2022exchangeofvitamin pages 4-6, sathe2022exchangeofvitamin pages 1-2). Coculture experiments with *E. coli* thiamine auxotrophs demonstrated that ΔthiC–ΔthiE and ΔthiC–ΔthiG pairs can cross-feed, but ΔthiE–ΔthiG pairs cannot, confirming the asymmetric exchangeability of HMP versus THZ (sathe2022exchangeofvitamin pages 4-6, sathe2022exchangeofvitamin pages 6-9).

### 6.4 DXP as a shared resource

DXP supply is a potential bottleneck because Dxs serves three downstream pathways (isoprenoids, PLP, and thiamine). Allosteric feedback inhibition of DXS by IPP/DMAPP, which promotes enzyme monomerization and aggregation, could indirectly constrain thiamine biosynthesis during conditions of high isoprenoid demand (di2023meppathwayproducts pages 5-7, di2023meppathwayproducts pages 1-2).

### 6.5 Oxygen and redox dependencies

ThiO requires molecular oxygen, potentially limiting thiazole synthesis under anaerobic conditions. ThiH provides an oxygen-independent alternative using radical SAM chemistry (maupinfurlow2018vitaminb1(thiamine) pages 4-7). The distribution of ThiO versus ThiH among bacterial species likely reflects adaptation to different oxygen regimes.

## 7. Controversies and Open Questions

### 7.1 ThiC mechanism

The ThiC-catalyzed conversion of AIR to HMP-P is one of the most complex reactions known in enzyme chemistry. Recent intermediate-trapping studies (Sharma et al., 2024; DOI: 10.1021/acscentsci.4c00125) have provided unprecedented mechanistic detail, but the complete reaction coordinate—including the precise timing of radical migration steps and the role of the [4Fe-4S] cluster beyond initial SAM cleavage—remains an active area of investigation (maupinfurlow2018vitaminb1(thiamine) pages 4-7).

### 7.2 THI4 suicide versus catalytic turnover

The discovery that some bacterial and archaeal Thi4 proteins can operate catalytically (with histidine replacing cysteine at the active site and using exogenous sulfide) has raised the question of whether the ancestral Thi4 was suicidal or catalytic. This has practical implications for crop engineering, as installing a nonsuicidal THI4 in plants could substantially reduce the energy cost of thiamine biosynthesis (strobbe2021metabolicengineeringprovides pages 12-12, sun2019partsprospectingfora pages 1-2).

### 7.3 ThiI dual function

ThiI participates in both thiamine biosynthesis (sulfur donation to ThiS) and tRNA modification (s⁴U synthesis). The degree to which these two functions compete for sulfur, and whether they are regulated independently, is incompletely understood. In *P. aeruginosa*, ThiI has been validated as essential for both pathways, making it a promising antibacterial target (maupinfurlow2018vitaminb1(thiamine) pages 17-19, kim2022pharmacologicalperturbationof pages 9-9).

### 7.4 Riboswitch biology in pathogens

TPP riboswitches have been bioinformatically identified in ESKAPE pathogens including *P. aeruginosa*, but in vivo functional validation remains limited to a few model organisms. Whether these riboswitches represent viable targets for new antibacterials is an open pharmacological question (kim2022pharmacologicalperturbationof pages 9-9, hubenthal2024influenceofantimicrobial pages 104-107).

### 7.5 Thiamine precursor exchange ecology

While HMP exchange among microbial species is well documented, the mechanisms and transporters involved in THZ release and uptake remain poorly characterized. The observation that ΔthiE–ΔthiG cocultures fail to grow suggests that THZ is either not released in sufficient quantities or lacks dedicated uptake systems, but the molecular basis for this asymmetry is unclear (sathe2022exchangeofvitamin pages 4-6, sathe2022exchangeofvitamin pages 11-14).

### 7.6 Feedback between transport and biosynthesis

In *Bacteroides thetaiotaomicron*, dual deletion of thiamine transporters (pnuT and OMthi) causes severe growth defects even in the presence of an intact biosynthetic pathway, suggesting an uncharacterized regulatory connection between transport and biosynthesis that may involve feedback mechanisms not yet fully delineated (costliow2017thiamineacquisitionstrategies pages 11-13).

## 8. Key References

The primary literature and reviews supporting this synthesis include:

- Maupin-Furlow JA (2018). Vitamin B1 (thiamine) metabolism and regulation in archaea. *B Group Vitamins – Current Uses and Perspectives*. DOI: 10.5772/intechopen.77170 (maupinfurlow2018vitaminb1(thiamine) pages 4-7, maupinfurlow2018vitaminb1(thiamine) pages 7-9, maupinfurlow2018vitaminb1(thiamine) pages 9-12, maupinfurlow2018vitaminb1(thiamine) pages 17-19, maupinfurlow2018vitaminb1(thiamine) pages 19-22).
- Bartee D and Freel Meyers CL (2018). Targeting the unique mechanism of bacterial 1-deoxy-D-xylulose-5-phosphate synthase. *Biochemistry* 57:4349–4356. DOI: 10.1021/acs.biochem.8b00548 (bartee2018targetingtheunique pages 1-3, bartee2018targetingtheunique pages 11-16).
- Sullivan AH et al. (2019). Crystal structures of thiamine monophosphate kinase from *Acinetobacter baumannii*. *Scientific Reports* 9. DOI: 10.1038/s41598-019-40558-x (sullivan2019crystalstructuresof pages 1-2).
- Costliow ZA and Degnan PH (2017). Thiamine acquisition strategies impact metabolism and competition in the gut microbe *Bacteroides thetaiotaomicron*. *mSystems* 2. DOI: 10.1128/msystems.00116-17 (costliow2017thiamineacquisitionstrategies pages 10-11, costliow2017thiamineacquisitionstrategies pages 8-10, costliow2017thiamineacquisitionstrategies pages 2-4, costliow2017thiamineacquisitionstrategies pages 11-13).
- Hwang S et al. (2017). ThiN as a versatile domain of transcriptional repressors and catalytic enzymes of thiamine biosynthesis. *Journal of Bacteriology* 199. DOI: 10.1128/jb.00810-16 (hwang2017thinasa pages 3-5).
- Sathe RRM et al. (2022). Exchange of vitamin B₁ and its biosynthesis intermediates shapes the composition of synthetic microbial cocultures. *Journal of Bacteriology* 204. DOI: 10.1128/jb.00503-21 (sathe2022exchangeofvitamin pages 4-6, sathe2022exchangeofvitamin pages 6-9, sathe2022exchangeofvitamin pages 1-2, sathe2022exchangeofvitamin pages 2-4, sathe2022exchangeofvitamin pages 11-14).
- Kim HJ et al. (2022). Pharmacological perturbation of thiamine metabolism sensitizes *Pseudomonas aeruginosa* to multiple antibacterial agents. *Cell Chemical Biology* 29:1317–1324. DOI: 10.1016/j.chembiol.2022.07.001 (kim2022pharmacologicalperturbationof pages 9-9).
- Straková D et al. (2024). Unveiling the genomic landscape and adaptive mechanisms of *Halogeometricum*: spotlight on thiamine biosynthesis. *Frontiers in Marine Science* 11. DOI: 10.3389/fmars.2024.1421769 (strakova2024unveilingthegenomic pages 11-13).
- Di X et al. (2023). MEP pathway products allosterically promote monomerization of DXS to feedback-regulate their supply. *Plant Communications* 4:100512. DOI: 10.1016/j.xplc.2022.100512 (di2023meppathwayproducts pages 5-7, di2023meppathwayproducts pages 1-2).
- Strobbe S et al. (2021). Metabolic engineering provides insight into the regulation of thiamin biosynthesis in plants. *Plant Physiology* 186:1832–1847. DOI: 10.1093/plphys/kiab198 (strobbe2021metabolicengineeringprovides pages 1-2, strobbe2021metabolicengineeringprovides pages 1-1, strobbe2021metabolicengineeringprovides pages 12-12).
- Sun J et al. (2019). Parts-prospecting for a high-efficiency thiamin thiazole biosynthesis pathway. *Plant Physiology* 179:958–968. DOI: 10.1104/pp.18.01085 (sun2019partsprospectingfora pages 1-2, sun2019partsprospectingfora pages 10-11).
- Ruszczycky MW and Liu Hw (2024). Initiation, propagation, and termination in the chemistry of radical SAM enzymes. *Biochemistry* 63:3161–3183. DOI: 10.1021/acs.biochem.4c00518 (ruszczycky2024initiationpropagationand pages 14-16).
- Turlin J et al. (2025). Synthetic C1 metabolism in *Pseudomonas putida* enables strict formatotrophy and methylotrophy. *mBio*. DOI: 10.1128/mbio.01976-25 (turlin2025syntheticc1metabolism pages 4-7).
- Hayashi M and Nosaka K (2015). Characterization of thiamin phosphate kinase in the hyperthermophilic archaeon *Pyrobaculum calidifontis*. *J. Nutr. Sci. Vitaminol.* 61:369–374. DOI: 10.3177/jnsv.61.369 (hayashi2015characterizationofthiamin pages 4-6, hayashi2015characterizationofthiamin pages 6-6).
- Tramonti A et al. (2021). Knowns and unknowns of vitamin B₆ metabolism in *Escherichia coli*. *EcoSal Plus* 9. DOI: 10.1128/ecosalplus.esp-0004-2021 (tramonti2021knownsandunknowns pages 10-12).

References

1. (maupinfurlow2018vitaminb1(thiamine) pages 4-7): Julie A. Maupin-Furlow. Vitamin b1 (thiamine) metabolism and regulation in archaea. B Group Vitamins - Current Uses and Perspectives, Sep 2018. URL: https://doi.org/10.5772/intechopen.77170, doi:10.5772/intechopen.77170. This article has 22 citations.

2. (maupinfurlow2018vitaminb1(thiamine) pages 7-9): Julie A. Maupin-Furlow. Vitamin b1 (thiamine) metabolism and regulation in archaea. B Group Vitamins - Current Uses and Perspectives, Sep 2018. URL: https://doi.org/10.5772/intechopen.77170, doi:10.5772/intechopen.77170. This article has 22 citations.

3. (bartee2018targetingtheunique pages 1-3): David Bartee and Caren L. Freel Meyers. Targeting the unique mechanism of bacterial 1-deoxy-d-xylulose-5-phosphate synthase. Biochemistry, 57 29:4349-4356, Jun 2018. URL: https://doi.org/10.1021/acs.biochem.8b00548, doi:10.1021/acs.biochem.8b00548. This article has 42 citations and is from a peer-reviewed journal.

4. (tramonti2021knownsandunknowns pages 10-12): Angela Tramonti, Caterina Nardella, Martino L. di Salvo, Anna Barile, Federico D’Alessio, Valérie de Crécy-Lagard, and Roberto Contestabile. Knowns and unknowns of vitamin b <sub>6</sub> metabolism in escherichia coli. Dec 2021. URL: https://doi.org/10.1128/ecosalplus.esp-0004-2021, doi:10.1128/ecosalplus.esp-0004-2021. This article has 64 citations.

5. (maupinfurlow2018vitaminb1(thiamine) pages 17-19): Julie A. Maupin-Furlow. Vitamin b1 (thiamine) metabolism and regulation in archaea. B Group Vitamins - Current Uses and Perspectives, Sep 2018. URL: https://doi.org/10.5772/intechopen.77170, doi:10.5772/intechopen.77170. This article has 22 citations.

6. (maupinfurlow2018vitaminb1(thiamine) pages 19-22): Julie A. Maupin-Furlow. Vitamin b1 (thiamine) metabolism and regulation in archaea. B Group Vitamins - Current Uses and Perspectives, Sep 2018. URL: https://doi.org/10.5772/intechopen.77170, doi:10.5772/intechopen.77170. This article has 22 citations.

7. (hwang2017thinasa pages 3-5): Sungmin Hwang, Bryan Cordova, Merna Abdo, Friedhelm Pfeiffer, and Julie A. Maupin-Furlow. Thin as a versatile domain of transcriptional repressors and catalytic enzymes of thiamine biosynthesis. Journal of Bacteriology, Apr 2017. URL: https://doi.org/10.1128/jb.00810-16, doi:10.1128/jb.00810-16. This article has 30 citations and is from a peer-reviewed journal.

8. (hubenthal2024influenceofantimicrobial pages 104-107): Anna Hübenthal. Influence of antimicrobial compounds and the rna-binding protein ribr on the activity of b vitamin-responsive bacterial riboswitches. Text, Jan 2024. URL: https://doi.org/10.11588/heidok.00034817, doi:10.11588/heidok.00034817. This article has 0 citations and is from a peer-reviewed journal.

9. (costliow2017thiamineacquisitionstrategies pages 10-11): Zachary A. Costliow and Patrick H. Degnan. Thiamine acquisition strategies impact metabolism and competition in the gut microbe bacteroides thetaiotaomicron. mSystems, Oct 2017. URL: https://doi.org/10.1128/msystems.00116-17, doi:10.1128/msystems.00116-17. This article has 98 citations and is from a peer-reviewed journal.

10. (costliow2017thiamineacquisitionstrategies pages 2-4): Zachary A. Costliow and Patrick H. Degnan. Thiamine acquisition strategies impact metabolism and competition in the gut microbe bacteroides thetaiotaomicron. mSystems, Oct 2017. URL: https://doi.org/10.1128/msystems.00116-17, doi:10.1128/msystems.00116-17. This article has 98 citations and is from a peer-reviewed journal.

11. (di2022allostericfeedbackinhibition pages 7-11): Xueni Di, David Ortega-Alarcon, Ramu Kakumanu, Edward E.K. Baidoo, Adrian Velazquez-Campoy, Manuel Rodríguez-Concepción, and Jordi Perez-Gil. Allosteric feedback inhibition of deoxy-d-xylulose-5-phosphate synthase involves monomerization of the active dimer. bioRxiv, Jun 2022. URL: https://doi.org/10.1101/2022.06.12.495819, doi:10.1101/2022.06.12.495819. This article has 0 citations.

12. (strakova2024unveilingthegenomic pages 11-13): Dáša Straková, Cristina Sánchez-Porro, Rafael R. de la Haba, and Antonio Ventosa. Unveiling the genomic landscape and adaptive mechanisms of the haloarchaeal genus halogeometricum: spotlight on thiamine biosynthesis. Frontiers in Marine Science, Oct 2024. URL: https://doi.org/10.3389/fmars.2024.1421769, doi:10.3389/fmars.2024.1421769. This article has 6 citations.

13. (turlin2025syntheticc1metabolism pages 4-7): Justine Turlin, Maria V G Alván-Vargas, Òscar Puiggené, S. Donati, Sebastian Wenk, and P. Nikel. Synthetic c1 metabolism in pseudomonas putida enables strict formatotrophy and methylotrophy via the reductive glycine pathway. mBio, pages e0197625, Aug 2025. URL: https://doi.org/10.1128/mbio.01976-25, doi:10.1128/mbio.01976-25. This article has 10 citations and is from a domain leading peer-reviewed journal.

14. (ruszczycky2024initiationpropagationand pages 14-16): Mark W. Ruszczycky and Hung-wen Liu. Initiation, propagation, and termination in the chemistry of radical sam enzymes. Biochemistry, 63:3161-3183, Dec 2024. URL: https://doi.org/10.1021/acs.biochem.4c00518, doi:10.1021/acs.biochem.4c00518. This article has 12 citations and is from a peer-reviewed journal.

15. (sullivan2019crystalstructuresof pages 1-2): Amy H. Sullivan, David M. Dranow, Peter S. Horanyi, Donald D. Lorimer, Thomas E. Edwards, and Jan Abendroth. Crystal structures of thiamine monophosphate kinase from acinetobacter baumannii in complex with substrates and products. Scientific Reports, Mar 2019. URL: https://doi.org/10.1038/s41598-019-40558-x, doi:10.1038/s41598-019-40558-x. This article has 8 citations and is from a peer-reviewed journal.

16. (hayashi2015characterizationofthiamin pages 4-6): Maria HAYASHI and Kazuto NOSAKA. Characterization of thiamin phosphate kinase in the hyperthermophilic archaeon pyrobaculum calidifontis. Journal of nutritional science and vitaminology, 61 5:369-74, Jan 2015. URL: https://doi.org/10.3177/jnsv.61.369, doi:10.3177/jnsv.61.369. This article has 9 citations and is from a peer-reviewed journal.

17. (kim2022pharmacologicalperturbationof pages 9-9): Hyung Jun Kim, Yingying Li, Michael Zimmermann, Yunmi Lee, Hui Wen Lim, Alvin Swee Leong Tan, Inhee Choi, Yoonae Ko, Sangchul Lee, Jeong Jea Seo, Mooyoung Seo, Hee Kyoung Jeon, Jonathan Cechetto, Joey Kuok Hoong Yam, Liang Yang, Uwe Sauer, Soojin Jang, and Kevin Pethe. Pharmacological perturbation of thiamine metabolism sensitizes pseudomonas aeruginosa to multiple antibacterial agents. Aug 2022. URL: https://doi.org/10.1016/j.chembiol.2022.07.001, doi:10.1016/j.chembiol.2022.07.001. This article has 14 citations and is from a domain leading peer-reviewed journal.

18. (bartee2018targetingtheunique pages 11-16): David Bartee and Caren L. Freel Meyers. Targeting the unique mechanism of bacterial 1-deoxy-d-xylulose-5-phosphate synthase. Biochemistry, 57 29:4349-4356, Jun 2018. URL: https://doi.org/10.1021/acs.biochem.8b00548, doi:10.1021/acs.biochem.8b00548. This article has 42 citations and is from a peer-reviewed journal.

19. (di2023meppathwayproducts pages 5-7): Xueni Di, David Ortega-Alarcon, Ramu Kakumanu, Javier Iglesias-Fernandez, Lucia Diaz, Edward E.K. Baidoo, Adrian Velazquez-Campoy, Manuel Rodríguez-Concepción, and Jordi Perez-Gil. Mep pathway products allosterically promote monomerization of deoxy-d-xylulose-5-phosphate synthase to feedback-regulate their supply. May 2023. URL: https://doi.org/10.1016/j.xplc.2022.100512, doi:10.1016/j.xplc.2022.100512. This article has 51 citations and is from a peer-reviewed journal.

20. (di2023meppathwayproducts pages 1-2): Xueni Di, David Ortega-Alarcon, Ramu Kakumanu, Javier Iglesias-Fernandez, Lucia Diaz, Edward E.K. Baidoo, Adrian Velazquez-Campoy, Manuel Rodríguez-Concepción, and Jordi Perez-Gil. Mep pathway products allosterically promote monomerization of deoxy-d-xylulose-5-phosphate synthase to feedback-regulate their supply. May 2023. URL: https://doi.org/10.1016/j.xplc.2022.100512, doi:10.1016/j.xplc.2022.100512. This article has 51 citations and is from a peer-reviewed journal.

21. (hayashi2015characterizationofthiamin pages 6-6): Maria HAYASHI and Kazuto NOSAKA. Characterization of thiamin phosphate kinase in the hyperthermophilic archaeon pyrobaculum calidifontis. Journal of nutritional science and vitaminology, 61 5:369-74, Jan 2015. URL: https://doi.org/10.3177/jnsv.61.369, doi:10.3177/jnsv.61.369. This article has 9 citations and is from a peer-reviewed journal.

22. (maupinfurlow2018vitaminb1(thiamine) pages 9-12): Julie A. Maupin-Furlow. Vitamin b1 (thiamine) metabolism and regulation in archaea. B Group Vitamins - Current Uses and Perspectives, Sep 2018. URL: https://doi.org/10.5772/intechopen.77170, doi:10.5772/intechopen.77170. This article has 22 citations.

23. (maupinfurlow2018vitaminb1(thiamine) pages 14-17): Julie A. Maupin-Furlow. Vitamin b1 (thiamine) metabolism and regulation in archaea. B Group Vitamins - Current Uses and Perspectives, Sep 2018. URL: https://doi.org/10.5772/intechopen.77170, doi:10.5772/intechopen.77170. This article has 22 citations.

24. (strobbe2021metabolicengineeringprovides pages 1-2): Simon Strobbe, Jana Verstraete, Christophe Stove, and Dominique Van Der Straeten. Metabolic engineering provides insight into the regulation of thiamin biosynthesis in plants. Plant Physiology, 186:1832-1847, May 2021. URL: https://doi.org/10.1093/plphys/kiab198, doi:10.1093/plphys/kiab198. This article has 23 citations and is from a highest quality peer-reviewed journal.

25. (sun2019partsprospectingfora pages 1-2): Jiayi Sun, Cindy L. Sigler, Guillaume A.W. Beaudoin, Jaya Joshi, Jenelle A. Patterson, Keun H. Cho, Maria A. Ralat, Jesse F. Gregory, David G. Clark, Zhanao Deng, Thomas A. Colquhoun, and Andrew D. Hanson. Parts-prospecting for a high-efficiency thiamin thiazole biosynthesis pathway. Plant Physiology, 179:958-968, Oct 2019. URL: https://doi.org/10.1104/pp.18.01085, doi:10.1104/pp.18.01085. This article has 33 citations and is from a highest quality peer-reviewed journal.

26. (sun2019partsprospectingfora pages 10-11): Jiayi Sun, Cindy L. Sigler, Guillaume A.W. Beaudoin, Jaya Joshi, Jenelle A. Patterson, Keun H. Cho, Maria A. Ralat, Jesse F. Gregory, David G. Clark, Zhanao Deng, Thomas A. Colquhoun, and Andrew D. Hanson. Parts-prospecting for a high-efficiency thiamin thiazole biosynthesis pathway. Plant Physiology, 179:958-968, Oct 2019. URL: https://doi.org/10.1104/pp.18.01085, doi:10.1104/pp.18.01085. This article has 33 citations and is from a highest quality peer-reviewed journal.

27. (strobbe2021metabolicengineeringprovides pages 1-1): Simon Strobbe, Jana Verstraete, Christophe Stove, and Dominique Van Der Straeten. Metabolic engineering provides insight into the regulation of thiamin biosynthesis in plants. Plant Physiology, 186:1832-1847, May 2021. URL: https://doi.org/10.1093/plphys/kiab198, doi:10.1093/plphys/kiab198. This article has 23 citations and is from a highest quality peer-reviewed journal.

28. (strobbe2021metabolicengineeringprovides pages 16-16): Simon Strobbe, Jana Verstraete, Christophe Stove, and Dominique Van Der Straeten. Metabolic engineering provides insight into the regulation of thiamin biosynthesis in plants. Plant Physiology, 186:1832-1847, May 2021. URL: https://doi.org/10.1093/plphys/kiab198, doi:10.1093/plphys/kiab198. This article has 23 citations and is from a highest quality peer-reviewed journal.

29. (strobbe2021metabolicengineeringprovides pages 12-12): Simon Strobbe, Jana Verstraete, Christophe Stove, and Dominique Van Der Straeten. Metabolic engineering provides insight into the regulation of thiamin biosynthesis in plants. Plant Physiology, 186:1832-1847, May 2021. URL: https://doi.org/10.1093/plphys/kiab198, doi:10.1093/plphys/kiab198. This article has 23 citations and is from a highest quality peer-reviewed journal.

30. (costliow2017thiamineacquisitionstrategies pages 8-10): Zachary A. Costliow and Patrick H. Degnan. Thiamine acquisition strategies impact metabolism and competition in the gut microbe bacteroides thetaiotaomicron. mSystems, Oct 2017. URL: https://doi.org/10.1128/msystems.00116-17, doi:10.1128/msystems.00116-17. This article has 98 citations and is from a peer-reviewed journal.

31. (sathe2022exchangeofvitamin pages 4-6): Rupali R. M. Sathe, Ryan W. Paerl, and Amrita B. Hazra. Exchange of vitamin b <sub>1</sub> and its biosynthesis intermediates shapes the composition of synthetic microbial cocultures and reveals complexities of nutrient sharing. Apr 2022. URL: https://doi.org/10.1128/jb.00503-21, doi:10.1128/jb.00503-21. This article has 31 citations and is from a peer-reviewed journal.

32. (sathe2022exchangeofvitamin pages 1-2): Rupali R. M. Sathe, Ryan W. Paerl, and Amrita B. Hazra. Exchange of vitamin b <sub>1</sub> and its biosynthesis intermediates shapes the composition of synthetic microbial cocultures and reveals complexities of nutrient sharing. Apr 2022. URL: https://doi.org/10.1128/jb.00503-21, doi:10.1128/jb.00503-21. This article has 31 citations and is from a peer-reviewed journal.

33. (sathe2022exchangeofvitamin pages 6-9): Rupali R. M. Sathe, Ryan W. Paerl, and Amrita B. Hazra. Exchange of vitamin b <sub>1</sub> and its biosynthesis intermediates shapes the composition of synthetic microbial cocultures and reveals complexities of nutrient sharing. Apr 2022. URL: https://doi.org/10.1128/jb.00503-21, doi:10.1128/jb.00503-21. This article has 31 citations and is from a peer-reviewed journal.

34. (sathe2022exchangeofvitamin pages 11-14): Rupali R. M. Sathe, Ryan W. Paerl, and Amrita B. Hazra. Exchange of vitamin b <sub>1</sub> and its biosynthesis intermediates shapes the composition of synthetic microbial cocultures and reveals complexities of nutrient sharing. Apr 2022. URL: https://doi.org/10.1128/jb.00503-21, doi:10.1128/jb.00503-21. This article has 31 citations and is from a peer-reviewed journal.

35. (costliow2017thiamineacquisitionstrategies pages 11-13): Zachary A. Costliow and Patrick H. Degnan. Thiamine acquisition strategies impact metabolism and competition in the gut microbe bacteroides thetaiotaomicron. mSystems, Oct 2017. URL: https://doi.org/10.1128/msystems.00116-17, doi:10.1128/msystems.00116-17. This article has 98 citations and is from a peer-reviewed journal.

36. (sathe2022exchangeofvitamin pages 2-4): Rupali R. M. Sathe, Ryan W. Paerl, and Amrita B. Hazra. Exchange of vitamin b <sub>1</sub> and its biosynthesis intermediates shapes the composition of synthetic microbial cocultures and reveals complexities of nutrient sharing. Apr 2022. URL: https://doi.org/10.1128/jb.00503-21, doi:10.1128/jb.00503-21. This article has 31 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](thiamine_biosynthesis-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](thiamine_biosynthesis-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. sullivan2019crystalstructuresof pages 1-2
2. kim2022pharmacologicalperturbationof pages 9-9
3. hwang2017thinasa pages 3-5
4. strobbe2021metabolicengineeringprovides pages 1-2
5. costliow2017thiamineacquisitionstrategies pages 10-11
6. costliow2017thiamineacquisitionstrategies pages 8-10
7. ruszczycky2024initiationpropagationand pages 14-16
8. costliow2017thiamineacquisitionstrategies pages 11-13
9. strakova2024unveilingthegenomic pages 11-13
10. tramonti2021knownsandunknowns pages 10-12
11. bartee2018targetingtheunique pages 1-3
12. hubenthal2024influenceofantimicrobial pages 104-107
13. costliow2017thiamineacquisitionstrategies pages 2-4
14. di2022allostericfeedbackinhibition pages 7-11
15. hayashi2015characterizationofthiamin pages 4-6
16. bartee2018targetingtheunique pages 11-16
17. di2023meppathwayproducts pages 5-7
18. di2023meppathwayproducts pages 1-2
19. hayashi2015characterizationofthiamin pages 6-6
20. sun2019partsprospectingfora pages 1-2
21. sun2019partsprospectingfora pages 10-11
22. strobbe2021metabolicengineeringprovides pages 1-1
23. strobbe2021metabolicengineeringprovides pages 16-16
24. strobbe2021metabolicengineeringprovides pages 12-12
25. sathe2022exchangeofvitamin pages 4-6
26. sathe2022exchangeofvitamin pages 1-2
27. sathe2022exchangeofvitamin pages 6-9
28. sathe2022exchangeofvitamin pages 11-14
29. sathe2022exchangeofvitamin pages 2-4
30. 4Fe-4S
31. https://doi.org/10.5772/intechopen.77170,
32. https://doi.org/10.1021/acs.biochem.8b00548,
33. https://doi.org/10.1128/ecosalplus.esp-0004-2021,
34. https://doi.org/10.1128/jb.00810-16,
35. https://doi.org/10.11588/heidok.00034817,
36. https://doi.org/10.1128/msystems.00116-17,
37. https://doi.org/10.1101/2022.06.12.495819,
38. https://doi.org/10.3389/fmars.2024.1421769,
39. https://doi.org/10.1128/mbio.01976-25,
40. https://doi.org/10.1021/acs.biochem.4c00518,
41. https://doi.org/10.1038/s41598-019-40558-x,
42. https://doi.org/10.3177/jnsv.61.369,
43. https://doi.org/10.1016/j.chembiol.2022.07.001,
44. https://doi.org/10.1016/j.xplc.2022.100512,
45. https://doi.org/10.1093/plphys/kiab198,
46. https://doi.org/10.1104/pp.18.01085,
47. https://doi.org/10.1128/jb.00503-21,