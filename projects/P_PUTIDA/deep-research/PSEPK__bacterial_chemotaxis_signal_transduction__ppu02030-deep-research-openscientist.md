---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T17:11:01.205558'
end_time: '2026-08-31T17:43:44.859554'
duration_seconds: 1963.65
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial chemotaxis signal transduction to flagellar motor output
  module_summary: Reusable bacterial chemotaxis signaling module linking chemoreceptor
    input to CheA autophosphorylation, CheY response-regulator phosphorylation, flagellar
    switch control, and MotAB-powered motor output. Receptor repertoires and attractant
    specificity vary by species; exact Pseudomonas putida exemplars ground one realization
    without making the module species-specific.
  module_outline: "- Chemoreceptor-to-flagellar-motor signaling\n  - 1. chemical stimulus\
    \ detection\n  - Methyl-accepting chemotaxis receptor input\n    - Chemotaxis\
    \ receptor activity (molecular player: methyl-accepting chemotaxis receptor family;\
    \ activity or role: transmembrane signaling receptor activity)\n  - 2. histidine-kinase\
    \ phosphotransfer\n  - CheA autophosphorylation and phosphotransfer\n    - CheA\
    \ histidine kinase (molecular player: chemotaxis CheA family; activity or role:\
    \ protein histidine kinase activity)\n  - 3. response-regulator control and reset\n\
    \  - CheY phosphorylation state controls motor bias\n    - CheY response regulator\
    \ (molecular player: two-component response regulator family; activity or role:\
    \ phosphorelay response regulator activity)\n    - CheZ phosphatase reset (molecular\
    \ player: CheZ phosphatase family; activity or role: phosphoprotein phosphatase\
    \ activity)\n  - 4. motor-switch response\n  - FliG flagellar switch output\n\
    \    - FliG motor switch component (molecular player: flagellar motor switch FliG\
    \ family)\n  - 5. proton-driven motor output\n  - MotAB stator-driven flagellar\
    \ rotation\n    - MotA stator subunit (molecular player: MotA family)\n    - MotB\
    \ stator subunit (molecular player: MotB family)"
  module_connections: '- Methyl-accepting chemotaxis receptor input promotes CheA
    autophosphorylation and phosphotransfer

    - CheA autophosphorylation and phosphotransfer feeds into CheY phosphorylation
    state controls motor bias

    - CheY phosphorylation state controls motor bias causes FliG flagellar switch
    output

    - FliG flagellar switch output causes MotAB stator-driven flagellar rotation'
  pathway_query: ppu02030
  pathway_id: ppu02030
  pathway_name: Bacterial chemotaxis
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu02030 with 41 primary genes; module
    area: transport_motility_signaling.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '48'
  candidate_genes: '- PP_0317: PP_0317 | Q88R17 | Methyl-accepting chemotaxis transducer
    (primary bucket kegg:ppu02030)

    - mcpH: PP_0320 | Q88R14 | Methyl-accepting chemotaxis protein McpH (primary bucket
    kegg:ppu02030)

    - ctpL: PP_0562 | Q88QD2 | Methyl-accepting chemotaxis protein CtpL (primary bucket
    kegg:ppu02030)

    - PP_0584: PP_0584 | Q88QB0 | Methyl-accepting chemotaxis transducer (primary
    bucket kegg:ppu02030)

    - PP_0779: PP_0779 | Q88PR9 | Methyl-accepting chemotaxis transducer/sensory box
    protein (primary bucket kegg:ppu02030)

    - PP_0802: PP_0802 | Q88PP6 | Chemotaxis protein (primary bucket kegg:ppu02030)

    - dppA-I: PP_0882 | Q88PG8 | Dipeptide ABC transporter-periplasmic binding protein
    (EC 3.6.3.23) (EC 3.6.3.23; primary bucket kegg:ppu02030)

    - dppA-II: PP_0884 | Q88PG6 | Dipeptide ABC transporter-periplasmic binding protein
    (EC 3.6.3.23) (EC 3.6.3.23; primary bucket kegg:ppu02030)

    - dppA-III: PP_0885 | Q88PG5 | Dipeptide ABC transporter-periplasmic binding protein
    (EC 3.6.3.23) (EC 3.6.3.23; primary bucket kegg:ppu02030)

    - mcpU: PP_1228 | Q88NI1 | Methyl-accepting chemotaxis protein McpU (primary bucket
    kegg:ppu02030)

    - mcpG: PP_1371 | Q88N45 | Methyl-accepting chemotaxis protein McpG (primary bucket
    kegg:ppu02030)

    - PP_1819: PP_1819 | Q88LV8 | Methyl-accepting chemotaxis transducer (primary
    bucket kegg:ppu02030)

    - PP_1940: PP_1940 | Q88LJ2 | Methyl-accepting chemotaxis transducer (primary
    bucket kegg:ppu02030)

    - PP_2111: PP_2111 | Q88L25 | Aerotaxis receptor (primary bucket kegg:ppu02030)

    - ctpH: PP_2120 | Q88L17 | Methyl-accepting chemotaxis protein CtpH (primary bucket
    kegg:ppu02030)

    - PP_2128: PP_2128 | Q88L09 | CheV-like chemotaxis protein (primary bucket kegg:ppu02030)

    - mcpA: PP_2249 | Q88KP1 | Methyl-accepting chemotaxis protein McpA (primary bucket
    kegg:ppu02030)

    - PP_2257: PP_2257 | Q88KN3 | Aerotaxis receptor (primary bucket kegg:ppu02030)

    - rbsB: PP_2454 | Q88K38 | Ribose ABC transporter, periplasmic ribose-binding
    subunit (primary bucket kegg:ppu02030)

    - pcaY: PP_2643 | Q88JK6 | Methyl-accepting chemotaxis protein PcaY (PcaY_PP)
    (primary bucket kegg:ppu02030)

    - PP_2757: PP_2757 | Q88J92 | Sugar-binding protein (primary bucket kegg:ppu02030)

    - PP_2758: PP_2758 | Q88J91 | Ribose ABC transporter, periplasmic ribose-binding
    protein (primary bucket kegg:ppu02030)

    - PP_2823: PP_2823 | Q88J26 | Methyl-accepting chemotaxis transducer (primary
    bucket kegg:ppu02030)

    - mcpP: PP_2861 | Q88IY8 | Methyl-accepting chemotaxis protein McpP (primary bucket
    kegg:ppu02030)

    - PP_3414: PP_3414 | Q88HE6 | Methyl-accepting chemotaxis transducer/sensory box
    protein (primary bucket kegg:ppu02030)

    - PP_3557: PP_3557 | Q88H08 | Methyl-accepting chemotaxis transducer (primary
    bucket kegg:ppu02030)

    - PP_3759: PP_3759 | Q88GG5 | protein-glutamate methylesterase (EC 3.1.1.61) (EC
    3.1.1.61; primary bucket kegg:ppu02030)

    - cheR3: PP_3760 | Q88GG4 | Putative methyltransferase Cher3 (EC 2.1.1.-) (EC
    2.1.1.-; primary bucket kegg:ppu02030)

    - PP_4332: PP_4332 | Q88EX0 | Chemotaxis protein CheW (primary bucket kegg:ppu02030)

    - PP_4333: PP_4333 | Q88EW9 | CheW domain protein (primary bucket kegg:ppu02030)

    - PP_4335: PP_4335 | Q88EW7 | Flagellar motor protein (primary bucket kegg:ppu02040)

    - PP_4336: PP_4336 | Q88EW6 | Flagellar motor rotation protein (primary bucket
    kegg:ppu02040)

    - cheB1: PP_4337 | Q88EW5 | Protein-glutamate methylesterase/protein-glutamine
    glutaminase of group 1 operon (EC 3.1.1.61) (EC 3.5.1.44) (EC 3.1.1.61; 3.5.1.44;
    primary bucket kegg:ppu02030)

    - cheA: PP_4338 | Q88EW4 | Chemotaxis protein CheA (EC 2.7.13.3) (EC 2.7.13.3;
    primary bucket kegg:ppu02030)

    - cheZ: PP_4339 | Q88EW3 | Protein phosphatase CheZ (EC 3.1.3.-) (Chemotaxis protein
    CheZ) (EC 3.1.3.-; primary bucket kegg:ppu02030)

    - cheY: PP_4340 | Q88EW2 | Response regulator for chemotactic signal transduction
    (primary bucket kegg:ppu02030)

    - fliN: PP_4357 | Q88EU6 | Flagellar motor switch protein FliN (primary bucket
    kegg:ppu02040)

    - fliM: PP_4358 | Q88EU5 | Flagellar motor switch protein FliM (primary bucket
    kegg:ppu02040)

    - fliG: PP_4368 | Q88ET5 | Flagellar motor switch protein FliG (primary bucket
    kegg:ppu02040)

    - cheR2: PP_4392 | Q88ER1 | Chemotaxis protein methyltransferase Cher2 (EC 2.1.1.80)
    (EC 2.1.1.80; primary bucket kegg:ppu02030)

    - PP_4393: PP_4393 | Q88ER0 | Chemotaxis protein (primary bucket kegg:ppu02030)

    - PP_4521: PP_4521 | Q88EE4 | Aerotaxis receptor (primary bucket kegg:ppu02030)

    - mcpS: PP_4658 | Q88E10 | Methyl-accepting chemotaxis protein McpS (primary bucket
    kegg:ppu02030)

    - motB: PP_4904 | Q88DC3 | Flagellar motor rotation protein (primary bucket kegg:ppu02040)

    - motA: PP_4905 | Q88DC2 | Flagellar motor rotation protein (primary bucket kegg:ppu02040)

    - mcpQ: PP_5020 | Q88D09 | Methyl-accepting chemotaxis protein McpQ (primary bucket
    kegg:ppu02030)

    - PP_5021: PP_5021 | Q88D08 | Methyl-accepting chemotaxis transducer (primary
    bucket kegg:ppu02030)

    - dppA-IV: PP_5283 | Q88C98 | Periplasmic dipeptide transport protein (primary
    bucket kegg:ppu02030)'
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 21
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__bacterial_chemotaxis_signal_transduction__ppu02030-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial_chemotaxis_signal_transduction__ppu02030-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial chemotaxis signal transduction to flagellar motor output in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu02030
- Resolved ID: ppu02030
- Resolved name: Bacterial chemotaxis
- Source: KEGG

Resolved local bucket kegg:ppu02030 with 41 primary genes; module area: transport_motility_signaling.

## Candidate Genes From Local Metadata

Candidate gene count: 48

- PP_0317: PP_0317 | Q88R17 | Methyl-accepting chemotaxis transducer (primary bucket kegg:ppu02030)
- mcpH: PP_0320 | Q88R14 | Methyl-accepting chemotaxis protein McpH (primary bucket kegg:ppu02030)
- ctpL: PP_0562 | Q88QD2 | Methyl-accepting chemotaxis protein CtpL (primary bucket kegg:ppu02030)
- PP_0584: PP_0584 | Q88QB0 | Methyl-accepting chemotaxis transducer (primary bucket kegg:ppu02030)
- PP_0779: PP_0779 | Q88PR9 | Methyl-accepting chemotaxis transducer/sensory box protein (primary bucket kegg:ppu02030)
- PP_0802: PP_0802 | Q88PP6 | Chemotaxis protein (primary bucket kegg:ppu02030)
- dppA-I: PP_0882 | Q88PG8 | Dipeptide ABC transporter-periplasmic binding protein (EC 3.6.3.23) (EC 3.6.3.23; primary bucket kegg:ppu02030)
- dppA-II: PP_0884 | Q88PG6 | Dipeptide ABC transporter-periplasmic binding protein (EC 3.6.3.23) (EC 3.6.3.23; primary bucket kegg:ppu02030)
- dppA-III: PP_0885 | Q88PG5 | Dipeptide ABC transporter-periplasmic binding protein (EC 3.6.3.23) (EC 3.6.3.23; primary bucket kegg:ppu02030)
- mcpU: PP_1228 | Q88NI1 | Methyl-accepting chemotaxis protein McpU (primary bucket kegg:ppu02030)
- mcpG: PP_1371 | Q88N45 | Methyl-accepting chemotaxis protein McpG (primary bucket kegg:ppu02030)
- PP_1819: PP_1819 | Q88LV8 | Methyl-accepting chemotaxis transducer (primary bucket kegg:ppu02030)
- PP_1940: PP_1940 | Q88LJ2 | Methyl-accepting chemotaxis transducer (primary bucket kegg:ppu02030)
- PP_2111: PP_2111 | Q88L25 | Aerotaxis receptor (primary bucket kegg:ppu02030)
- ctpH: PP_2120 | Q88L17 | Methyl-accepting chemotaxis protein CtpH (primary bucket kegg:ppu02030)
- PP_2128: PP_2128 | Q88L09 | CheV-like chemotaxis protein (primary bucket kegg:ppu02030)
- mcpA: PP_2249 | Q88KP1 | Methyl-accepting chemotaxis protein McpA (primary bucket kegg:ppu02030)
- PP_2257: PP_2257 | Q88KN3 | Aerotaxis receptor (primary bucket kegg:ppu02030)
- rbsB: PP_2454 | Q88K38 | Ribose ABC transporter, periplasmic ribose-binding subunit (primary bucket kegg:ppu02030)
- pcaY: PP_2643 | Q88JK6 | Methyl-accepting chemotaxis protein PcaY (PcaY_PP) (primary bucket kegg:ppu02030)
- PP_2757: PP_2757 | Q88J92 | Sugar-binding protein (primary bucket kegg:ppu02030)
- PP_2758: PP_2758 | Q88J91 | Ribose ABC transporter, periplasmic ribose-binding protein (primary bucket kegg:ppu02030)
- PP_2823: PP_2823 | Q88J26 | Methyl-accepting chemotaxis transducer (primary bucket kegg:ppu02030)
- mcpP: PP_2861 | Q88IY8 | Methyl-accepting chemotaxis protein McpP (primary bucket kegg:ppu02030)
- PP_3414: PP_3414 | Q88HE6 | Methyl-accepting chemotaxis transducer/sensory box protein (primary bucket kegg:ppu02030)
- PP_3557: PP_3557 | Q88H08 | Methyl-accepting chemotaxis transducer (primary bucket kegg:ppu02030)
- PP_3759: PP_3759 | Q88GG5 | protein-glutamate methylesterase (EC 3.1.1.61) (EC 3.1.1.61; primary bucket kegg:ppu02030)
- cheR3: PP_3760 | Q88GG4 | Putative methyltransferase Cher3 (EC 2.1.1.-) (EC 2.1.1.-; primary bucket kegg:ppu02030)
- PP_4332: PP_4332 | Q88EX0 | Chemotaxis protein CheW (primary bucket kegg:ppu02030)
- PP_4333: PP_4333 | Q88EW9 | CheW domain protein (primary bucket kegg:ppu02030)
- PP_4335: PP_4335 | Q88EW7 | Flagellar motor protein (primary bucket kegg:ppu02040)
- PP_4336: PP_4336 | Q88EW6 | Flagellar motor rotation protein (primary bucket kegg:ppu02040)
- cheB1: PP_4337 | Q88EW5 | Protein-glutamate methylesterase/protein-glutamine glutaminase of group 1 operon (EC 3.1.1.61) (EC 3.5.1.44) (EC 3.1.1.61; 3.5.1.44; primary bucket kegg:ppu02030)
- cheA: PP_4338 | Q88EW4 | Chemotaxis protein CheA (EC 2.7.13.3) (EC 2.7.13.3; primary bucket kegg:ppu02030)
- cheZ: PP_4339 | Q88EW3 | Protein phosphatase CheZ (EC 3.1.3.-) (Chemotaxis protein CheZ) (EC 3.1.3.-; primary bucket kegg:ppu02030)
- cheY: PP_4340 | Q88EW2 | Response regulator for chemotactic signal transduction (primary bucket kegg:ppu02030)
- fliN: PP_4357 | Q88EU6 | Flagellar motor switch protein FliN (primary bucket kegg:ppu02040)
- fliM: PP_4358 | Q88EU5 | Flagellar motor switch protein FliM (primary bucket kegg:ppu02040)
- fliG: PP_4368 | Q88ET5 | Flagellar motor switch protein FliG (primary bucket kegg:ppu02040)
- cheR2: PP_4392 | Q88ER1 | Chemotaxis protein methyltransferase Cher2 (EC 2.1.1.80) (EC 2.1.1.80; primary bucket kegg:ppu02030)
- PP_4393: PP_4393 | Q88ER0 | Chemotaxis protein (primary bucket kegg:ppu02030)
- PP_4521: PP_4521 | Q88EE4 | Aerotaxis receptor (primary bucket kegg:ppu02030)
- mcpS: PP_4658 | Q88E10 | Methyl-accepting chemotaxis protein McpS (primary bucket kegg:ppu02030)
- motB: PP_4904 | Q88DC3 | Flagellar motor rotation protein (primary bucket kegg:ppu02040)
- motA: PP_4905 | Q88DC2 | Flagellar motor rotation protein (primary bucket kegg:ppu02040)
- mcpQ: PP_5020 | Q88D09 | Methyl-accepting chemotaxis protein McpQ (primary bucket kegg:ppu02030)
- PP_5021: PP_5021 | Q88D08 | Methyl-accepting chemotaxis transducer (primary bucket kegg:ppu02030)
- dppA-IV: PP_5283 | Q88C98 | Periplasmic dipeptide transport protein (primary bucket kegg:ppu02030)

## Generic Module Context

### Working Scope

Reusable bacterial chemotaxis signaling module linking chemoreceptor input to CheA autophosphorylation, CheY response-regulator phosphorylation, flagellar switch control, and MotAB-powered motor output. Receptor repertoires and attractant specificity vary by species; exact Pseudomonas putida exemplars ground one realization without making the module species-specific.

### Provisional Biological Outline

- Chemoreceptor-to-flagellar-motor signaling
  - 1. chemical stimulus detection
  - Methyl-accepting chemotaxis receptor input
    - Chemotaxis receptor activity (molecular player: methyl-accepting chemotaxis receptor family; activity or role: transmembrane signaling receptor activity)
  - 2. histidine-kinase phosphotransfer
  - CheA autophosphorylation and phosphotransfer
    - CheA histidine kinase (molecular player: chemotaxis CheA family; activity or role: protein histidine kinase activity)
  - 3. response-regulator control and reset
  - CheY phosphorylation state controls motor bias
    - CheY response regulator (molecular player: two-component response regulator family; activity or role: phosphorelay response regulator activity)
    - CheZ phosphatase reset (molecular player: CheZ phosphatase family; activity or role: phosphoprotein phosphatase activity)
  - 4. motor-switch response
  - FliG flagellar switch output
    - FliG motor switch component (molecular player: flagellar motor switch FliG family)
  - 5. proton-driven motor output
  - MotAB stator-driven flagellar rotation
    - MotA stator subunit (molecular player: MotA family)
    - MotB stator subunit (molecular player: MotB family)

### Known Relationships Among Steps

- Methyl-accepting chemotaxis receptor input promotes CheA autophosphorylation and phosphotransfer
- CheA autophosphorylation and phosphotransfer feeds into CheY phosphorylation state controls motor bias
- CheY phosphorylation state controls motor bias causes FliG flagellar switch output
- FliG flagellar switch output causes MotAB stator-driven flagellar rotation

## Assignment

Write a species-aware review of this module/pathway in the target organism. The
goal is not a generic pathway essay; the goal is to support manual module
satisfiability and gene annotation curation.

Treat the candidate gene list as a starting point, not ground truth. Use the
literature and authoritative resources to decide whether each expected pathway
step is present, absent, ambiguous, replaced by a lineage-specific alternative,
or represented by a likely over-propagated annotation.

Prioritize direct evidence from the target species/strain. When using evidence
from related organisms, state the organism and explain whether transfer to the
target taxon is strong, weak, or uncertain. Distinguish *Pseudomonas putida*
KT2440 evidence from broader *Pseudomonas* or generic bacterial evidence.

## Questions To Address

1. **Pathway boundaries**
   - What exact biochemical or cellular process is included?
   - Which neighboring pathways or broad overview maps should be kept separate?
   - Are there alternate names or database-specific definitions for this pathway?

2. **Satisfiability in the target taxon**
   - Which expected steps are encoded by candidate genes?
   - Which steps are missing from the metadata but likely present under a
     different gene name, paralog, or enzyme family?
   - Which steps are probably not expected in this organism?

3. **Candidate gene assessment**
   - For each high-confidence gene, summarize the likely role, evidence type,
     and any curation-relevant caveats.
   - Identify paralog ambiguity, broad EC/GO mappings, and likely annotation
     over-propagation.
   - Note genes that should be promoted to full `fetch-gene` review.

4. **Module implications**
   - What module steps should be marked covered, candidate_uncertain, gap,
     not_expected_in_target_taxon, or module_needs_revision?
   - Are existing generic module boundaries wrong for this organism?
   - Are new module documents or GO term requests likely needed?

5. **Evidence and open questions**
   - Which conclusions are supported by direct experiments?
   - Which are inferred from homology, pathway databases, or neighboring genes?
   - What experiments or expert questions would resolve the important gaps?

## Output Format

Use concise review sections:

1. Executive summary
2. Target-organism pathway definition
3. Expected step model
4. Candidate genes and evidence
5. Gaps, ambiguities, and likely over-annotations
6. Module and GO-curation recommendations
7. Genes to promote to full review
8. Key references

Include citations for major claims, preferably PMIDs or DOIs. Be explicit about
uncertainty, species transfer, and whether evidence is direct for the target
organism.

## Output

# Module/Pathway/Taxon Review: Bacterial Chemotaxis Signal Transduction to Flagellar Motor Output in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target pathway/bucket:** KEGG ppu02030 — Bacterial chemotaxis (module area: transport_motility_signaling)
**Companion bucket:** KEGG ppu02040 — Flagellar assembly (motor switch + stator genes)
**Candidate genes assessed:** 48 loci from local metadata

---

## 1. Executive Summary

The chemoreceptor-to-flagellar-motor signaling module is **fully satisfiable** in *Pseudomonas putida* KT2440. Every canonical step of the generic module — chemoreceptor input, CheA autophosphorylation/phosphotransfer, CheY/CheZ response-regulator control, FliG/FliM/FliN switch output, and MotAB-powered motor rotation — is encoded in the KT2440 genome, and the core signaling cascade has direct target-strain evidence. The KT2440 flagellar/chemotaxis gene cluster is experimentally defined as a single large region (≈59 genes in ≈11 operons), the core Che genes are organized in the *cheYZA* and *cheB-motAB* operons, and the whole apparatus is under a three-tier FleQ→σ⁵⁴→σ²⁸(FliA) regulatory cascade with a confirmed nonmotile *fliA* phenotype. This is far stronger than homology-only satisfaction.

The chemoreceptor input step is the best-characterized part of the module in this organism. KT2440 is predicted to encode **27 chemoreceptors (MCPs)**, and the Krell laboratory generated the complete set of chemoreceptor deletion mutants. At least **seven receptors have directly determined ligand specificities in KT2440 or closely related *P. putida***: McpS (TCA-cycle intermediates + butyrate), McpQ (citrate/metal complexes), McpP (C2/C3 carboxylic acids), McpU (polyamines), McpA (amino acids), McpG (GABA), and PcaY_PP (aromatic/hydroaromatic acids). These are high-confidence, promotion-worthy annotations.

Two boundary corrections are required for accurate curation. **First**, the motor-output step is incomplete as modeled: *P. putida* uses **two non-redundant stators, MotAB and MotCD**, and the candidate metadata captures only MotAB — the module should be marked `module_needs_revision`. **Second**, several candidate genes are **likely KEGG over-propagations**: the ABC-transporter periplasmic substrate-binding proteins (dppA-I..IV, rbsB, PP_2757/PP_2758) and Wsp/c-di-GMP chemosensory-like MCP loci do not represent flagellar chemotaxis-satisfying components in this organism and should be flagged `candidate_uncertain`. The CtpH/CtpL phosphate receptors rest on *P. aeruginosa* evidence (with CtpL working via a PstS binding-protein shuttle) and remain `candidate_uncertain` pending direct KT2440 data.

---

## 2. Target-Organism Pathway Definition

### 2.1 What the module includes

The module is the **flagellar chemotaxis signal-transduction pathway**: the information flow from transmembrane methyl-accepting chemotaxis proteins (MCPs), through the CheA/CheW signaling array and the CheY response regulator, to the FliM/FliN/FliG switch complex that biases the direction of rotation of the MotAB/MotCD-powered flagellar motor. Adaptation/reset components (CheR methyltransferase, CheB methylesterase, CheZ phosphatase, and CheV) are part of the pathway because they set the dynamic operating point of the receptor array and terminate the CheY-P signal.

In KT2440 the behavioral readout is a **"run-reverse-turn"** swimming pattern typical of polar-flagellated pseudomonads, rather than the enterobacterial "run-and-tumble" ([PMID: 23728820](https://pubmed.ncbi.nlm.nih.gov/23728820/)). The motor spends roughly equal time in CW and CCW rotation, which is mechanistically relevant to how CheY-P bias is interpreted at the switch.

### 2.2 Neighboring pathways that must be kept separate

- **KEGG ppu02040 (Flagellar assembly).** The structural flagellar genes (*fliM*, *fliN*, *fliG*, *motA*, *motB*, and the PP_4335/PP_4336 cluster-I motor genes) are annotated to ppu02040. The switch and stator components sit at the interface and are legitimately shared, but flagellar **biosynthesis** proper is a distinct map.
- **The Wsp chemosensory-like c-di-GMP pathway.** This is a *separate* signal-transduction system for surface sensing/biofilm, not flagellar chemotaxis. Its receptor WspA initiates a phosphorylation cascade activating the diguanylate cyclase WspR, producing c-di-GMP rather than controlling motor bias ([PMID: 35476526](https://pubmed.ncbi.nlm.nih.gov/35476526/)). KT2440 possesses a WspA homologue that controls biofilm ([PMID: 26662997](https://pubmed.ncbi.nlm.nih.gov/26662997/)). Some MCP-like loci in the candidate list belong to this Wsp/F-type cluster and must not be counted toward flagellar chemotaxis.
- **c-di-GMP → motility modulation via FlgZ/YcgR-type control.** In *P. putida*, PP4397/FlgZ links c-di-GMP signaling (from PP2258) to flagellar motility ([PMID: 30111852](https://pubmed.ncbi.nlm.nih.gov/30111852/)). This is a second-messenger modulation layer, not the core Che phosphorelay.

### 2.3 Alternate names / database definitions

KEGG "Bacterial chemotaxis" (map02030 / ppu02030) is the canonical reference. The pathway is also captured in GO under chemotaxis / signal transduction and taxis terms and in the module framework as a reusable "chemoreceptor-to-flagellar-motor signaling" module. Receptor gene names vary by database (systematic PP_ locus tags vs. functional names such as McpS, McpP, McpU, McpG, PcaY).

---

## 3. Expected Step Model

The generic module and its known step relationships map onto KT2440 as follows:

```
[1] Chemical stimulus detection
    MCP chemoreceptors (≈27 in KT2440)  ── ligand binding at LBD ──►
        promotes
[2] Histidine-kinase phosphotransfer
    CheA (PP_4338) autophosphorylation, via CheW (PP_4332/PP_4333) coupling ──►
        feeds into
[3] Response-regulator control + reset
    CheY (PP_4340) phosphorylation state ◄── CheZ (PP_4339) phosphatase reset
    Adaptation: CheR (PP_4392/PP_3760), CheB (PP_4337/PP_3759), CheV (PP_2128) ──►
        causes
[4] Motor-switch response
    FliG (PP_4368) / FliM (PP_4358) / FliN (PP_4357) switch ──►
        causes
[5] Proton-driven motor output
    MotAB (PP_4905/PP_4904)  +  MotCD  (SECOND STATOR — not in metadata)
```

| Step | Expected player | KT2440 candidate | Status |
|------|-----------------|------------------|--------|
| 1. Stimulus detection | MCP family | 27 receptors; 7 characterized | **covered** (input richly documented) |
| 2. CheA + coupling | CheA histidine kinase; CheW | cheA PP_4338; CheW PP_4332/PP_4333; CheV PP_2128 | **covered** |
| 3a. CheY response regulator | CheY | cheY PP_4340 | **covered** |
| 3b. CheZ reset | CheZ phosphatase | cheZ PP_4339 | **covered** |
| 3c. Adaptation | CheR / CheB | cheR2 PP_4392, cheR3 PP_3760, cheB1 PP_4337, PP_3759 | **covered** (paralog ambiguity) |
| 4. Switch | FliG/FliM/FliN | fliG PP_4368, fliM PP_4358, fliN PP_4357 | **covered** (ppu02040) |
| 5. Motor output | MotA/MotB | motA PP_4905, motB PP_4904 (+ PP_4335/PP_4336) | **module_needs_revision** (MotCD missing) |

---

## 4. Candidate Genes and Evidence

### 4.1 Chemoreceptor input — high-confidence, target-strain evidence

KT2440 is repeatedly described as *"predicted to have 27 chemoreceptors, most of which uncharacterized"* ([PMID: 26463109](https://pubmed.ncbi.nlm.nih.gov/26463109/)), and the complete set of chemoreceptor deletion mutants has been generated: *"Here we report the generation of the complete set of chemoreceptor mutants of Pseudomonas putida KT2440"* ([PMID: 26662997](https://pubmed.ncbi.nlm.nih.gov/26662997/)). The candidate list contains ~30 MCP/aerotaxis loci, consistent with — but not identical to — this experimentally curated repertoire (some candidate MCP-like loci belong to Wsp/other chemosensory clusters).

**Directly characterized receptors (promote to full review):**

| Receptor | Locus | Ligands | Evidence | PMID |
|----------|-------|---------|----------|------|
| McpS | PP_4658 | 6 TCA-cycle intermediates + butyrate; citrate–metal discrimination | ITC + chemotaxis, KT2440 | [20498372](https://pubmed.ncbi.nlm.nih.gov/20498372/), [21360620](https://pubmed.ncbi.nlm.nih.gov/21360620/) |
| McpQ | PP_5020 | citrate/metal-ion complexes (McpS paralogue) | Direct, KT2440 | [26463109](https://pubmed.ncbi.nlm.nih.gov/26463109/) |
| McpP | PP_2861 | acetate, pyruvate, propionate, L-lactate (KD 34–107 µM) | ITC, KT2440 | [26048936](https://pubmed.ncbi.nlm.nih.gov/26048936/) |
| McpU | PP_1228 | putrescine, cadaverine, spermidine (first polyamine receptor) | ITC + structure (dCACHE) | [29758259](https://pubmed.ncbi.nlm.nih.gov/29758259/) |
| McpA | PP_2249 | 12 proteinogenic amino acids | Direct, KT2440 | [26662997](https://pubmed.ncbi.nlm.nih.gov/26662997/) |
| McpG | PP_1371 | GABA (specific); root-colonization phenotype | ITC + chimera + Δmcp, KT2440 | [25921834](https://pubmed.ncbi.nlm.nih.gov/25921834/) |
| PcaY_PP | PP_2643 | aromatic/hydroaromatic acids (broad: C6 ring + carboxyl) | Structure + binding, KT2440 | [33021055](https://pubmed.ncbi.nlm.nih.gov/33021055/) |

Key direct-evidence quotes:
- McpS: *"We report the identification of McpS as the specific chemoreceptor for 6 tricarboxylic acid (TCA) cycle intermediates and butyrate in Pseudomonas putida"* ([PMID: 20498372](https://pubmed.ncbi.nlm.nih.gov/20498372/)).
- McpP: *"we identify PP2861 (termed McpP) of Pseudomonas putida KT2440 as a chemoreceptor with a novel ligand profile ... recognizes acetate, pyruvate, propionate, and l-lactate"* ([PMID: 26048936](https://pubmed.ncbi.nlm.nih.gov/26048936/)).
- McpU: *"the McpU chemoreceptor from Pseudomonas putida was identified as the first chemoreceptor that bound specifically polyamines"* ([PMID: 29758259](https://pubmed.ncbi.nlm.nih.gov/29758259/)).
- McpG: *"We report the identification of McpG as a specific GABA chemoreceptor in non-pathogenic Pseudomonas putida KT2440"* ([PMID: 25921834](https://pubmed.ncbi.nlm.nih.gov/25921834/)), with Δ*mcpG* reducing tomato-root colonization and GABA detected in root exudates.
- PcaY_PP: *"characterized by an unusually broad signal range, and minimal requisites for signal binding are the presence of a C6-membered ring and that of a carboxyl group"* ([PMID: 33021055](https://pubmed.ncbi.nlm.nih.gov/33021055/)).

**Caveats for receptor curation:** Many characterized *Pseudomonas* receptors are **promiscuous/multifunctional**. PcaY_PP has an "unusually broad signal range" ([PMID: 33021055](https://pubmed.ncbi.nlm.nih.gov/33021055/)); PcpI of *P. putida* responds to two different phytohormones (salicylate and IAA) without binding IAA directly ([PMID: 35088505](https://pubmed.ncbi.nlm.nih.gov/35088505/)). Receptor–ligand annotations should therefore record a specificity *range*, not a single ligand, and should flag metabolism-independent vs. metabolism-coupled taxis (e.g., PcaY links chemotaxis, transport, and catabolism; [PMID: 25582673](https://pubmed.ncbi.nlm.nih.gov/25582673/)).

### 4.2 Core signaling cascade — target-strain operon/regulatory evidence

The KT2440 flagella/chemotaxis cluster is experimentally defined. Rodríguez-Herva 2010 shows the cluster *"is comprised of four independent transcriptional units: flhAF, fleNfliA, cheYZA and cheBmotAB"* and that a nonpolar *fliA* (σ²⁸) mutant is nonmotile ([PMID: 23766109](https://pubmed.ncbi.nlm.nih.gov/23766109/)). Leal-Morales 2022 shows the flagellar cluster is a single ≈59-gene region in ≈11 operons, with the core chemotaxis machinery under a *"three-tier cascade in which fleQ is a Class I gene"* → σ⁵⁴ → σ²⁸(FliA) ([PMID: 34859548](https://pubmed.ncbi.nlm.nih.gov/34859548/)).

| Component | Locus | Role | Evidence tier |
|-----------|-------|------|---------------|
| CheA (EC 2.7.13.3) | PP_4338 | Histidine kinase, autophosphorylation | Operon-defined (*cheYZA*), KT2440 |
| CheY | PP_4340 | Response regulator; sets motor bias | Operon-defined, KT2440 |
| CheZ (EC 3.1.3.-) | PP_4339 | Phosphatase reset of CheY-P | Operon-defined, KT2440 |
| CheB1 (EC 3.1.1.61/3.5.1.44) | PP_4337 | Methylesterase (adaptation); *cheB-motAB* operon | Operon-defined, KT2440 |
| CheR2 (EC 2.1.1.80) | PP_4392 | Methyltransferase (adaptation) | Homology + operon context |
| CheW | PP_4332 / PP_4333 | CheA–MCP coupling | Homology, cluster context |
| CheV-like | PP_2128 | CheW-CheY hybrid coupling/adaptation | Homology |

A *P. putida* chemoreceptor forms **active signaling complexes when reconstituted with *E. coli* CheA/CheW/CheY**, with methylation-dependent adaptation ([PMID: 22745269](https://pubmed.ncbi.nlm.nih.gov/22745269/)), functionally confirming the receptor→kinase→CheY logic is conserved.

### 4.3 Switch and motor — covered, with a required revision

FliG (PP_4368), FliM (PP_4358), FliN (PP_4357), MotA (PP_4905), and MotB (PP_4904) cover the switch and one stator. However, **motor torque in *P. putida* is generated by two stators**: *"the motor torque for flagellar rotation is generated by the two stators MotAB and MotCD"* ([PMID: 36409076](https://pubmed.ncbi.nlm.nih.gov/36409076/)). MotAB is essential for swimming in liquid; MotCD is required for spreading in semisolid agar — the two are **non-redundant**. The candidate metadata lists only MotAB (plus PP_4335/PP_4336 cluster-I motor genes) and does not flag the MotCD set. This is the single clearest module-boundary correction.

### 4.4 Aerotaxis / energy taxis receptors

PP_2111, PP_2257, PP_4521 are annotated as aerotaxis receptors. Energy/aerotaxis is a legitimate sub-branch of chemotaxis (Aer-type receptors feed the same CheA/CheY cascade). Phylogenetic and functional work on Aer receptors in pseudomonads supports their role in energy taxis ([PMID: 31639075](https://pubmed.ncbi.nlm.nih.gov/31639075/); [PMID: 35264479](https://pubmed.ncbi.nlm.nih.gov/35264479/)). Direct KT2440 functional data are thinner than for the carboxylate/amino-acid receptors; treat as `covered` at the family level but `candidate_uncertain` for individual locus assignment.

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1 Substrate-binding proteins — likely KEGG over-propagation

The candidate list includes **dppA-I..IV (PP_0882/0884/0885/5283), rbsB (PP_2454), and PP_2757/PP_2758** (ribose/sugar-binding), all assigned to kegg:ppu02030. These are ABC-transporter periplasmic **substrate-binding proteins (SBPs)**. KEGG map02030 includes SBPs because in *E. coli* certain SBPs (DppA, RbsB, MglB) hand ligands to the Tap/Trg MCPs; this ortholog assignment is auto-propagated to ppu02030. **No direct KT2440 evidence links these SBPs to chemoreceptor signaling.** The characterized KT2440 receptors bind ligands **directly via their own LBDs** (McpS, McpP, McpU, McpG, PcaY) rather than through SBP intermediaries. → Flag `candidate_uncertain` / over-propagation.

**Calibration caveat.** SBP-mediated chemotaxis is not impossible in *Pseudomonas*. In *P. aeruginosa*, the periplasmic Pi-binding protein **PstS** binds phosphate and then stimulates the CtpL receptor — a genuine SBP shuttle: *"We identify the periplasmic ligand binding protein PstS as the protein that binds in its Pi loaded state to CtpL, resulting in receptor stimulation. PstS forms part of the Pi transporter and has thus a double function in Pi transport and chemotaxis"* ([PMID: 27353565](https://pubmed.ncbi.nlm.nih.gov/27353565/)). So the mechanism exists in the genus; the flag is "unsupported for these specific loci in KT2440," not "impossible."

### 5.2 CtpH/CtpL phosphate chemotaxis — species-transfer uncertainty

ctpH (PP_2120) and ctpL (PP_0562) are named by homology. The phosphate-taxis evidence originates in ***P. aeruginosa***: *"Two chemotactic transducers for inorganic phosphate (Pi), designated CtpH and CtpL, have been identified in Pseudomonas aeruginosa"* ([PMID: 10852870](https://pubmed.ncbi.nlm.nih.gov/10852870/)), with CtpH binding Pi directly and CtpL requiring the PstS shuttle ([PMID: 27353565](https://pubmed.ncbi.nlm.nih.gov/27353565/)). No direct KT2440 phosphate-taxis data were found. Species transfer is **plausible but unverified** → `candidate_uncertain`.

### 5.3 Wsp / c-di-GMP chemosensory-like loci — wrong pathway

Some MCP-like loci in the candidate set belong to the **Wsp (c-di-GMP/biofilm)** system, which is distinct from flagellar chemotaxis: *"The methyl-accepting chemotaxis protein WspA recognizes an unknown surface-associated signal and initiates a phosphorylation cascade that activates the diguanylate cyclase WspR"* ([PMID: 35476526](https://pubmed.ncbi.nlm.nih.gov/35476526/); see also [PMID: 26662997](https://pubmed.ncbi.nlm.nih.gov/26662997/)). Related Wsp-like systems in other bacteria confirm this architecture (e.g., *Halomonas* HtChe2/Htc10 controlling a diguanylate cyclase; [PMID: 39529381](https://pubmed.ncbi.nlm.nih.gov/39529381/)). These loci should not be counted as flagellar chemotaxis-satisfying → `candidate_uncertain` / reassign.

### 5.4 CheR/CheB paralog ambiguity

KT2440 encodes multiple adaptation-enzyme paralogs: CheR2 (PP_4392) and CheR3 (PP_3760); CheB1 (PP_4337) and a second methylesterase PP_3759. The broad EC mappings (EC 3.1.1.61, EC 2.1.1.-) and multiple paralogs mean locus-level assignment to "the" flagellar Che pathway vs. auxiliary chemosensory clusters needs case-by-case curation. The *cheB-motAB* operon anchors CheB1/PP_4337 to the flagellar cascade with high confidence; the others are `candidate_uncertain`.

### 5.5 CheW duplication

PP_4332 (CheW) and PP_4333 (CheW domain protein) are adjacent paralogs. Both plausibly participate in array coupling; assignment of distinct roles (or redundancy) is unresolved.

---

## 6. Module and GO-Curation Recommendations

| Module step | Recommended status | Rationale |
|-------------|--------------------|-----------|
| Chemoreceptor input | **covered** | 27 receptors; 7 with direct ligand data (McpS, McpQ, McpP, McpU, McpA, McpG, PcaY_PP) |
| CheA autophosphorylation/phosphotransfer | **covered** | cheA PP_4338, operon-defined (*cheYZA*); reconstituted signaling shown |
| CheY response regulator | **covered** | cheY PP_4340, operon-defined |
| CheZ reset | **covered** | cheZ PP_4339, operon-defined |
| Adaptation (CheR/CheB/CheV) | **covered** (with paralog caveats) | CheB1/PP_4337 operon-anchored; paralogs `candidate_uncertain` |
| FliG/FliM/FliN switch | **covered** | ppu02040 loci present |
| MotAB stator | **covered** | motA/motB present |
| **Second stator (MotCD)** | **module_needs_revision** | *P. putida* has two non-redundant stators; MotCD absent from metadata |
| SBPs (dppA, rbsB, PP_2757/2758) | **candidate_uncertain / over-annotation** | KEGG auto-propagation; no KT2440 chemotaxis link |
| CtpH/CtpL phosphate taxis | **candidate_uncertain** | *P. aeruginosa* evidence; species transfer unverified |
| Wsp/c-di-GMP MCP-like loci | **candidate_uncertain / reassign** | Belongs to biofilm c-di-GMP system, not flagellar output |

**Module boundary revision needed:** The generic module's single "MotAB stator-driven flagellar rotation" step should be generalized to a **dual-stator (MotAB + MotCD)** motor-output step for *P. putida* and related pseudomonads, capturing the non-redundant liquid-vs-surface division of labor.

**Possible new module/GO requests:**
- A separate **Wsp / c-di-GMP surface-sensing chemosensory module** to receive the MCP-like loci that are currently mis-bucketed into ppu02030.
- A **c-di-GMP → FlgZ/YcgR motility-modulation** annotation to capture PP4397/FlgZ ([PMID: 30111852](https://pubmed.ncbi.nlm.nih.gov/30111852/)) as a distinct regulatory layer.
- GO annotation extensions recording receptor **ligand-range** rather than single-ligand specificity for promiscuous receptors (PcaY_PP, PcpI).

---

## 7. Genes to Promote to Full `fetch-gene` Review

**High priority (direct KT2440 functional data — confirm annotations and record ligand ranges):**
- **McpS (PP_4658)**, **McpQ (PP_5020)**, **McpP (PP_2861)**, **McpU (PP_1228)**, **McpA (PP_2249)**, **McpG (PP_1371)**, **PcaY_PP (PP_2643)** — characterized receptors.
- **cheA (PP_4338)**, **cheY (PP_4340)**, **cheZ (PP_4339)**, **cheB1 (PP_4337)** — operon-anchored core cascade.
- **motA (PP_4905)**, **motB (PP_4904)** — resolve dual-stator status; locate/annotate the MotCD stator pair.

**Medium priority (ambiguity/over-annotation to resolve):**
- **ctpH (PP_2120)** / **ctpL (PP_0562)** — verify or downgrade phosphate-taxis assignment for KT2440.
- **cheR2 (PP_4392)** / **cheR3 (PP_3760)** / **PP_3759** — resolve which paralogs serve the flagellar cascade.
- **PP_4332 / PP_4333** — resolve CheW paralog roles.
- **dppA-I..IV, rbsB (PP_2454), PP_2757/PP_2758** — confirm reassignment out of chemotaxis (transport only).
- Aerotaxis loci **PP_2111, PP_2257, PP_4521** — confirm energy-taxis role and cluster membership.
- Uncharacterized MCP loci (PP_0317, PP_0320/mcpH, PP_0584, PP_0779, PP_0802, PP_1819, PP_1940, PP_2823, PP_3414, PP_3557, PP_5021) — triage Che vs. Wsp cluster membership.

---

## 8. Limitations and Knowledge Gaps

1. **MotCD locus not identified in metadata.** The dual-stator conclusion is from the literature ([PMID: 36409076](https://pubmed.ncbi.nlm.nih.gov/36409076/)); the specific PP_ loci for MotCD were not resolved in this review and should be located during curation.
2. **~20 of 27 receptors remain functionally uncharacterized**, so input-step coverage is documented at the family level, with specific ligand assignments for only 7.
3. **Cluster membership of many MCP-like loci is not individually resolved** (Che flagellar vs. Wsp c-di-GMP vs. other chemosensory arrays). This is the largest single source of over-annotation risk.
4. **CtpH/CtpL and several other assignments rest on homology transfer from *P. aeruginosa* or *P. putida* F1**, not direct KT2440 experiments.
5. Receptor promiscuity means single-ligand annotations will understate true specificity ranges.

---

## 9. Proposed Follow-up Experiments / Actions

- **Curation:** Locate the MotCD stator loci in KT2440 and add a dual-stator motor-output step to the module. Reassign SBP and Wsp loci out of ppu02030.
- **Bioinformatic triage:** Classify all 27 MCP-like loci by chemosensory-cluster membership (Che vs. Wsp vs. Aer) using operon context and array-type signatures, resolving the candidate list against the experimentally curated 27-receptor set.
- **Targeted experiments (if wet-lab follow-up is possible):** ITC/chemotaxis screens for the uncharacterized MCPs; direct phosphate-taxis assay in KT2440 to test CtpH/CtpL; motility phenotyping of single/double stator mutants in liquid vs. semisolid to confirm MotAB/MotCD division of labor.
- **Expert questions:** Which CheR/CheB paralogs and CheW copies are dedicated to the flagellar array vs. auxiliary systems? Does KT2440 use SBP-shuttle chemotaxis for any ligand (as *P. aeruginosa* does via PstS)?

---

## 10. Key References

| PMID | Contribution |
|------|--------------|
| [26463109](https://pubmed.ncbi.nlm.nih.gov/26463109/) | 27-receptor count; McpQ citrate specificity |
| [26662997](https://pubmed.ncbi.nlm.nih.gov/26662997/) | Complete KT2440 receptor mutant set; McpA; biofilm |
| [20498372](https://pubmed.ncbi.nlm.nih.gov/20498372/) | McpS = TCA-cycle intermediate receptor |
| [21360620](https://pubmed.ncbi.nlm.nih.gov/21360620/) | McpS citrate–metal discrimination |
| [26048936](https://pubmed.ncbi.nlm.nih.gov/26048936/) | McpP = C2/C3 carboxylic-acid receptor |
| [29758259](https://pubmed.ncbi.nlm.nih.gov/29758259/) | McpU polyamine receptor structure |
| [33021055](https://pubmed.ncbi.nlm.nih.gov/33021055/) | PcaY_PP broad aromatic specificity |
| [25921834](https://pubmed.ncbi.nlm.nih.gov/25921834/) | McpG = GABA receptor; root colonization |
| [25582673](https://pubmed.ncbi.nlm.nih.gov/25582673/) | PcaY links chemotaxis/transport/catabolism |
| [35088505](https://pubmed.ncbi.nlm.nih.gov/35088505/) | PcpI dual-phytohormone (receptor promiscuity) |
| [22745269](https://pubmed.ncbi.nlm.nih.gov/22745269/) | *P. putida* receptor signals in *E. coli* Che complex |
| [23766109](https://pubmed.ncbi.nlm.nih.gov/23766109/) | KT2440 *cheYZA*/*cheB-motAB* operons; *fliA* nonmotile |
| [34859548](https://pubmed.ncbi.nlm.nih.gov/34859548/) | FleQ→σ⁵⁴→FliA regulatory cascade |
| [36409076](https://pubmed.ncbi.nlm.nih.gov/36409076/) | Two stators MotAB + MotCD |
| [23728820](https://pubmed.ncbi.nlm.nih.gov/23728820/) | Run-reverse-turn motility paradigm |
| [35476526](https://pubmed.ncbi.nlm.nih.gov/35476526/) | Wsp c-di-GMP pathway distinct from chemotaxis |
| [30111852](https://pubmed.ncbi.nlm.nih.gov/30111852/) | FlgZ c-di-GMP motility modulation |
| [27353565](https://pubmed.ncbi.nlm.nih.gov/27353565/) | PstS shuttle for CtpL (SBP calibration) |
| [10852870](https://pubmed.ncbi.nlm.nih.gov/10852870/) | CtpH/CtpL phosphate taxis (*P. aeruginosa*) |
| [39529381](https://pubmed.ncbi.nlm.nih.gov/39529381/) | Wsp-like DGC-controlling receptor (comparative) |
| [24148021](https://pubmed.ncbi.nlm.nih.gov/24148021/) | Metabolic cost of flagellar motility in KT2440 |
| [31639075](https://pubmed.ncbi.nlm.nih.gov/31639075/) | Aer energy-taxis receptor phylogeny |

---

*Review scope note:* Conclusions on the core cascade, operon organization, regulation, and the seven characterized receptors are supported by **direct *P. putida* KT2440 (or closely related *P. putida*) experiments**. The dual-stator architecture is direct *P. putida* evidence. CtpH/CtpL phosphate taxis and the SBP-shuttle mechanism derive from ***P. aeruginosa*** and require verification before transfer to KT2440. SBP and Wsp over-annotation flags are inferences from pathway-database propagation logic combined with the absence of KT2440-specific chemotaxis evidence.


## Artifacts

- [OpenScientist final report](PSEPK__bacterial_chemotaxis_signal_transduction__ppu02030-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial_chemotaxis_signal_transduction__ppu02030-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:23728820
2. PMID:35476526
3. PMID:26662997
4. PMID:30111852
5. PMID:26463109
6. PMID:20498372
7. PMID:26048936
8. PMID:29758259
9. PMID:25921834
10. PMID:33021055
11. PMID:35088505
12. PMID:25582673
13. PMID:23766109
14. PMID:34859548
15. PMID:22745269
16. PMID:36409076
17. PMID:31639075
18. PMID:35264479
19. PMID:27353565
20. PMID:10852870
21. PMID:39529381