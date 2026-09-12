---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-11T16:46:06.759813'
end_time: '2026-06-11T17:02:17.022175'
duration_seconds: 970.26
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: exbB
  gene_symbol: exbB
  uniprot_accession: Q88C77
  protein_description: 'RecName: Full=Biopolymer transport protein ExbB {ECO:0000256|ARBA:ARBA00022093};'
  gene_info: Name=exbB {ECO:0000313|EMBL:AAN70871.1}; OrderedLocusNames=PP_5306 {ECO:0000313|EMBL:AAN70871.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the exbB/tolQ family.
  protein_domains: ExbB/TolQ_transport. (IPR050790); MotA_ExbB_proton_chnl. (IPR002898);
    TonB_ExbB_1. (IPR014164); MotA_ExbB (PF01618)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 38
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: exbB-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q88C77
- **Protein Description:** RecName: Full=Biopolymer transport protein ExbB {ECO:0000256|ARBA:ARBA00022093};
- **Gene Information:** Name=exbB {ECO:0000313|EMBL:AAN70871.1}; OrderedLocusNames=PP_5306 {ECO:0000313|EMBL:AAN70871.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the exbB/tolQ family.
- **Key Domains:** ExbB/TolQ_transport. (IPR050790); MotA_ExbB_proton_chnl. (IPR002898); TonB_ExbB_1. (IPR014164); MotA_ExbB (PF01618)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "exbB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'exbB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **exbB** (gene ID: exbB, UniProt: Q88C77) in PSEPK.

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
- **UniProt Accession:** Q88C77
- **Protein Description:** RecName: Full=Biopolymer transport protein ExbB {ECO:0000256|ARBA:ARBA00022093};
- **Gene Information:** Name=exbB {ECO:0000313|EMBL:AAN70871.1}; OrderedLocusNames=PP_5306 {ECO:0000313|EMBL:AAN70871.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the exbB/tolQ family.
- **Key Domains:** ExbB/TolQ_transport. (IPR050790); MotA_ExbB_proton_chnl. (IPR002898); TonB_ExbB_1. (IPR014164); MotA_ExbB (PF01618)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "exbB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'exbB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **exbB** (gene ID: exbB, UniProt: Q88C77) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Research report: Functional annotation of **exbB** (UniProt **Q88C77**; locus **PP_5306**) in *Pseudomonas putida* KT2440

## Executive summary
The *Pseudomonas putida* KT2440 protein ExbB (PP_5306; UniProt Q88C77) is an inner (cytoplasmic) membrane component of the TonB energy-transduction system. ExbB forms an oligomeric motor with ExbD that couples the proton motive force (pmf) of the inner membrane to mechanical work on TonB, thereby powering active transport through TonB-dependent outer-membrane transporters (TBDTs) for scarce nutrients—classically ferric siderophore complexes and heme/other metal complexes—and contributing to stress tolerance phenotypes in pseudomonads. In KT2440, deletion of **exbB–exbD–tonB (PP_5306–PP_5308)** causes strong iron-dependent growth defects and also impacts bioelectrochemical mediator utilization and product yields in an engineered electrogenic process, consistent with a central role in envelope-spanning uptake pathways. (weimer2024systemsmetabolicengineering pages 87-93, weimer2024systemsmetabolicengineering pages 93-97)

## Target verification (critical identity checks)
**Gene symbol and description match:** Independent experimental work in *P. putida* KT2440 explicitly identifies an in-frame deletion spanning **exbB, exbD and tonB** at **PP_5306–PP_5308**, confirming that PP_5306 corresponds to **exbB** in this organism and operon context. (weimer2024systemsmetabolicengineering pages 87-93)

**Family/domain consistency:** Mechanistic reviews of ExbB/ExbD/TonB describe ExbB as a multi-pass inner-membrane motor protein homologous to TolQ/MotA-like proton-coupled systems, consistent with UniProt’s ExbB/TolQ family and MotA/ExbB proton-channel-like domain annotations. (braun2023energizationofouter pages 11-13, braun2024substrateuptakeby pages 11-12)

## 1) Key concepts and definitions (current understanding)

### The TonB–ExbB–ExbD system
**Definition:** The Ton system is an energy-transducing machine in Gram-negative bacteria that powers transport across the **outer membrane** through TBDTs. TBDTs are β-barrel outer-membrane proteins with plug domains; TonB binding to a conserved **TonB box** induces conformational changes that open the transporter for substrate passage into the periplasm. (braun2024substrateuptakeby pages 1-2)

**Role of ExbB:** ExbB is an inner-membrane protein that oligomerizes and associates with ExbD to form the pmf-driven motor that energizes TonB. The ExbB–ExbD complex is widely described as the component that transmits pmf energy from the cytoplasmic membrane to TonB. (braun2023energizationofouter pages 1-3, braun2024substrateuptakeby pages 1-2)

### What ExbB is *not*
ExbB is not a substrate-specific transporter that binds iron/siderophores directly; rather, it is an **energy-coupling motor** required for the activity of many different TBDTs (each of which provides substrate specificity). (braun2024substrateuptakeby pages 1-2, cornelis2010ironuptakeand pages 1-3)

## 2) Molecular function and mechanism (with quantitative/structural details)

### Cellular localization and topology
**Localization:** ExbB is a **cytoplasmic (inner) membrane** protein that assembles into membrane-embedded oligomers. (braun2023energizationofouter pages 1-3, braun2023energizationofouter pages 11-13)

**Topology:** A 2024 mechanistic study summarizes ExbB as having an N-terminus in the periplasm and **three transmembrane segments**; ExbD is N-anchored in the cytoplasmic membrane and extends into the periplasm. (braun2024substrateuptakeby pages 11-12)

### Complex architecture and stoichiometry
A recurring architecture supported by structural studies is **ExbB pentamer enclosing an ExbD dimer** (ExbB5:ExbD2). (braun2023energizationofouter pages 1-3, braun2024substrateuptakeby pages 1-2)

Some biochemical preparations show additional assemblies (e.g., ExbB6·ExbD1 and ExbB5·ExbD1 species), indicating stoichiometry can vary by conditions and preparation, but 5:2 is emphasized as a consensus in several structural contexts. (braun2023energizationofouter pages 4-6, braun2023energizationofouter pages 11-13)

### pmf coupling and mechanochemical transduction
**Proton-coupled mechanism:** ExbB/ExbD are described as generating energy for TonB-dependent transport by **transfer of protons from the periplasm to the cytoplasm**, implying direct coupling to the inner-membrane pmf. (braun2023energizationofouter pages 4-6)

**Key conserved residue:** A conserved **Asp (D25) in ExbD’s transmembrane helix** is repeatedly implicated in proton-linked energization steps and pmf-dependent ExbD–TonB interactions. (braun2023energizationofouter pages 4-6, braun2023energizationofouter pages 13-15)

**Quantitative mechanistic proposal:** One model proposes pmf-driven cycling around ExbD D25 with discrete **~36° rotation steps** (10 cycles to return to starting orientation), providing a concrete hypothesis for how pmf might be converted into mechanical work on TonB. (braun2023energizationofouter pages 13-15)

### Substrates enabled by ExbB (system-level “substrate” of ExbB)
Because ExbB energizes TonB, it supports TBDT-mediated uptake of multiple substrate classes. Reviews explicitly list **Fe3+-siderophores** and **vitamin B12** among TonB-dependent substrates. (braun2023energizationofouter pages 3-4, braun2024substrateuptakeby pages 1-2)

For pseudomonads specifically, iron uptake reviews describe TonB together with ExbB/ExbD transmitting pmf energy to gated outer-membrane receptors for **ferric siderophore** and **heme** uptake. (cornelis2010ironuptakeand pages 1-3)

## 3) Genetic context and pathways in *Pseudomonas putida* KT2440

### Operon context
In KT2440, experimental deletion work identifies the canonical cluster as **PP_5306–PP_5308 = exbB–exbD–tonB**, demonstrating the expected Ton operon organization at the locus of Q88C77. (weimer2024systemsmetabolicengineering pages 87-93)

### Pathway placement
ExbB functions in the envelope-spanning **TonB-dependent transport pathway**, coupling inner-membrane pmf to outer-membrane TBDTs that import scarce nutrients into the periplasm; periplasmic binding proteins and inner-membrane transporters then import into the cytoplasm, where iron is released (by reduction or enzymatic processing) and siderophores may be recycled. (cornelis2010ironuptakeand pages 1-3)

## 4) Phenotypes from mutation / disruption (KT2440-specific and comparative)

### KT2440: ΔexbBD ΔtonB (PP_5306–PP_5308) phenotypes (2024)
A KT2440 **ΔexbBΔexbDΔtonB** mutant showed a pronounced **iron-dependent aerobic growth defect** in minimal medium: at baseline FeCl3 (5.5 µM), the mutant growth rate was reported as ~**7-fold lower** than wild type; **20 µM FeCl3** restored growth to ~**80%** of wild type, while 40 µM FeCl3 was inhibitory to both strains. (weimer2024systemsmetabolicengineering pages 87-93)

In anaerobic bioelectrochemical assays, the same mutant exhibited **lower ferricyanide reduction rate** (**0.026 ± 0.001 mM/h**) versus wild type (**0.056 ± 0.009 mM/h**), suggesting TonB-dependent pathways contribute to mediator exchange/handling beyond purely passive routes. (weimer2024systemsmetabolicengineering pages 87-93)

Process-level impacts were large: with ferricyanide mediator, the mutant had **lower peak current** (**1.0 ± 0.14 mA** vs WT **2.42 ± 0.43 mA**), longer time to full glucose conversion (~**240 h** vs ~**186 h**), and a major product shift from 2-ketogluconate (WT **0.93 ± 0.03 mol/mol**) to gluconate (mutant **0.77 ± 0.08 mol/mol**), consistent with broad physiological consequences of disrupting TonB energization. (weimer2024systemsmetabolicengineering pages 93-97)

### Comparative *Pseudomonas* evidence: exbD disruption in DOT-T1E (2001)
In *P. putida* DOT-T1E (closely related to KT2440), an insertion in **exbD** in the **exbB–exbD–tonB** cluster disrupted the operon transcript (loss of exbD–tonB RT-PCR product) and caused inability to grow under iron limitation with chelator (**8 mM EDDHA**), consistent with a role in TonB-dependent iron uptake. (godoy2001involvementofthe pages 4-5)

This exbD mutant also displayed increased sensitivity to solvents and antibiotics and showed much higher accumulation of radiolabeled 4-hydroxybenzoate (**~200 nmol per U cell turbidity per min**) compared with control (**~15 nmol per U per min**), interpreted as impaired extrusion/efflux-linked tolerance not fully explained by iron limitation alone. (godoy2001involvementofthe pages 4-5, godoy2001involvementofthe pages 6-7)

### High-throughput ecological genetics (2023)
RB-TnSeq fitness profiling across bacterial species exposed to fungal exometabolites reports that **iron-uptake genes** can be required for *P. putida* fitness under those conditions, using thresholds of **log2 fitness < −1** and **t-score < −4** to define significant negative fitness effects. (villalobosescobedo2023genomewidefitnessprofiling pages 10-11)

## 5) Recent developments and latest research (prioritizing 2023–2024)

### Mechanistic refinement of the ExbB–ExbD motor (2023–2024)
Recent authoritative syntheses emphasize high-resolution structural models in which ExbB forms a membrane-embedded oligomer with a central pore that houses ExbD, transmitting pmf energy to TonB and thereby to TBDTs. (braun2023energizationofouter pages 11-13, braun2024substrateuptakeby pages 1-2)

The 2023 review highlights converging structural evidence for ExbB5:ExbD2 and frames ExbB–ExbD as a **molecular motor** analogous to MotA/MotB stators, with testable residue-level predictions involving ExbD D25 and pmf-dependent TonB interactions. (braun2023energizationofouter pages 11-13, braun2023energizationofouter pages 4-6)

A 2024 review further consolidates the “TonB box” interaction concept and reiterates the ExbB5 pore enclosing an ExbD dimer as the energy-transmitting complex enabling substrate uptake through plugged TBDTs. (braun2024substrateuptakeby pages 1-2)

### New *in vivo* interrogation of motor cycling (2024 preprint)
A 2024 bioRxiv study reports detailed topology/complex assembly concepts (e.g., ExbB as a 3-TM membrane protein with large cytoplasmic regions, and models featuring ExbB tetramers scaffolding TonB2/ExbD2), and proposes pmf-dependent structural transitions of ExbD that configure TonB during an energization cycle. These claims are informative but should be treated as preprint-stage evidence. (postle2024invivotests pages 1-5, postle2024invivotests pages 45-51)

## 6) Current applications and real-world implementations

### Trojan-horse antibiotics and selective delivery (2024–2025)
A 2024 review describes practical exploitation of siderophore uptake pathways—powered by the ExbBD–TonB motor—to deliver antibiotics into Gram-negative bacteria (the “Trojan-horse” strategy), and explicitly notes that transport energy is provided by the pmf transduced through the ExbBD–TonB complex. (graff2024siderophoresastools pages 1-2, graff2024siderophoresastools pages 2-4)

A 2025 Nature Reviews Microbiology article frames the TonB–ExbB–ExbD complex as a **molecular motor** transmitting pmf energy to TBDTs and emphasizes translational applications of siderophore pathways including **antibiotic vectorization**, diagnostic sensors, and imaging-agent delivery that depend on transporter specificity. (schalk2025bacterialsiderophoresdiversity pages 42-46)

## 7) Expert synthesis: proposed functional annotation for Q88C77 (PP_5306)

**Recommended primary function statement:** ExbB (PP_5306; Q88C77) is an **inner-membrane energy-transducing subunit** of the TonB system that, together with ExbD, couples the **proton motive force** to energize TonB and thereby drive active uptake through TonB-dependent outer-membrane transporters. (braun2024substrateuptakeby pages 1-2, braun2023energizationofouter pages 1-3)

**Biological processes:** TonB-dependent nutrient acquisition under limitation (especially **iron acquisition via siderophores/heme** in pseudomonads) and broader envelope physiology/stress tolerance phenotypes secondary to impaired TonB energization. (cornelis2010ironuptakeand pages 1-3, weimer2024systemsmetabolicengineering pages 87-93)

**Cellular component:** Cytoplasmic/inner membrane (multi-pass membrane protein), functioning as part of ExbB–ExbD oligomeric motor complex that interacts with TonB. (braun2024substrateuptakeby pages 11-12, braun2023energizationofouter pages 1-3)

**Key mutant phenotypes to record for KT2440:** Severe iron-dependent growth defects in ΔexbBD ΔtonB, partially rescued by added iron, plus altered mediator reduction and bioelectrochemical process performance. (weimer2024systemsmetabolicengineering pages 87-93, weimer2024systemsmetabolicengineering pages 93-97)

## Evidence table of key sources (URLs and dates)
| Source (authors, year) | Publication type | Organism/strain | What was studied (exbB/exbD/tonB, operon) | Key findings (function/localization/phenotypes) | Key quantitative data/statistics | URL/DOI |
|---|---|---|---|---|---|---|
| Braun, Ratliff, Celia & Buchanan, 2023 | Peer-reviewed mechanistic review | Primarily *E. coli* / Gram-negative bacteria | ExbB-ExbD-TonB motor; adjacency of exbB and exbD; conserved TonB energization of TBDTs | ExbB and ExbD are inner-membrane proteins that use proton motive force to energize TonB, which contacts TonB boxes in outer-membrane TonB-dependent transporters for uptake of siderophores, vitamin B12, and other scarce nutrients; ExbB forms a pentameric motor surrounding an ExbD dimer; exb mutants have leaky/partial phenotypes and can be partly complemented by TolQ/TolR (braun2023energizationofouter pages 3-4, braun2023energizationofouter pages 4-6, braun2023energizationofouter pages 1-3, braun2023energizationofouter pages 6-8) | ExbB:ExbD stoichiometry reported as 5:2; exbB mutants retain ~20% cobalamin transport vs WT, while tonB or exbB tolQ double mutants fall to <5% (braun2023energizationofouter pages 4-6) | https://doi.org/10.1128/jb.00035-23 |
| Braun, 2024 | Peer-reviewed review | Gram-negative bacteria | TonB-dependent transporters and ExbB-ExbD energy-transducing complex | TonB is energized by ExbB-ExbD to open plugged outer-membrane TBDTs; ExbB-ExbD supports uptake of Fe3+-siderophores, other metal ions, vitamin B12, glycans, and some proteins/toxins; model supports ExbB pentamer enclosing ExbD dimer (braun2024substrateuptakeby pages 1-2) | ExbB complex described as five ExbB subunits around an ExbD dimer (braun2024substrateuptakeby pages 1-2) | https://doi.org/10.1111/mmi.15332 |
| Weimer, 2024 | Experimental primary study / thesis-style report | *Pseudomonas putida* KT2440 | In-frame deletion of exbB-exbD-tonB (PP_5306-PP_5308); role in mediator uptake/electrogenic metabolism | Directly relevant to Q88C77 context: exbB is PP_5306 in the PP_5306-PP_5308 cluster. ΔexbBD ΔtonB impairs aerobic growth under baseline iron, lowers anaerobic ferricyanide reduction, reduces current generation, prolongs glucose conversion, and shifts product spectrum from 2-ketogluconate to gluconate, supporting a role in TonB-dependent uptake/handling of iron-linked or metal-mediator substrates (weimer2024systemsmetabolicengineering pages 87-93, weimer2024systemsmetabolicengineering pages 97-101, weimer2024systemsmetabolicengineering pages 93-97) | Deletion size difference 2123 bp; mutant aerobic growth rate ~7-fold lower than WT at 5.5 µM FeCl3; 20 µM FeCl3 restores growth to ~80% of WT; anaerobic ferricyanide reduction 0.026 ± 0.001 mM/h vs WT 0.056 ± 0.009 mM/h; ferricyanide max current 1.0 ± 0.14 mA vs WT 2.42 ± 0.43 mA; 2-ketogluconate yield 0.17 ± 0.01 vs WT 0.93 ± 0.03 mol/mol glucose; glucose conversion prolonged to ~240 h vs ~186 h WT (weimer2024systemsmetabolicengineering pages 87-93, weimer2024systemsmetabolicengineering pages 97-101, weimer2024systemsmetabolicengineering pages 93-97) | No DOI/URL available in retrieved context |
| Ainsaar et al., 2019 | Peer-reviewed primary study | *Pseudomonas putida* KT2440 | TonBm-PocAB system; genomic context of TonB homologs in KT2440 | Provides key locus context: *P. putida* has two TonB homologues, PP_4994 and PP_5308; PP_5308 (tonB) is in an operon with exbB and exbD, supporting assignment of Q88C77/PP_5306 as the cognate ExbB in the canonical exbBD-tonB operon. Study mainly analyzed the orthologous TonBm-PocAB system, showing TonB-like envelope motors can affect membrane integrity and flagellar positioning in *P. putida* (from retrieved abstract/snippet in paper search results) | Qualitative snippet only in retrieved context; no direct numeric exbB data available in cited evidence set | https://doi.org/10.1128/jb.00303-19 |
| Godoy, Ramos-González & Ramos, 2001 | Peer-reviewed primary study | *Pseudomonas putida* DOT-T1E (closely related to KT2440) | exbBD-tonB cluster organization and mutant phenotypes from exbD insertion | exbB, exbD, and tonB are closely linked and likely cotranscribed; the TonB-ExbB-ExbD complex is an inner-membrane energy transduction system required for iron uptake and additionally influences solvent/drug tolerance, likely via effects on efflux. Mutating exbD caused sensitivity to 4HBA, toluene, and multiple antibiotics and impaired growth in iron-limited medium; because DOT-T1E proteins are highly similar to KT2440 homologs, this is strong comparative evidence for PP_5306 function (godoy2001involvementofthe pages 6-7, godoy2001involvementofthe pages 1-2, godoy2001involvementofthe pages 4-5) | exbB-exbD separated by 3 bp; exbD and tonB overlap; mutant failed to grow in low iron with 8 mM EDDHA; [14C]4HBA accumulation ~200 nmol/U cell turbidity/min in mutant vs ~15 in control; high-affinity transport can generate up to 1,000-fold concentration gradients (godoy2001involvementofthe pages 6-7, godoy2001involvementofthe pages 4-5) | https://doi.org/10.1128/jb.183.18.5285-5292.2001 |
| Cornelis, 2010 | Peer-reviewed review | Pseudomonads including *P. putida* KT2440 | Iron uptake and metabolism; TonB-ExbB-ExbD support of siderophore/heme uptake | In pseudomonads, TonB together with ExbB and ExbD transmits pmf-derived energy from the inner membrane to outer-membrane receptors for ferric-siderophore and heme uptake. This review supports the inferred primary function of PP_5306/Q88C77 as an inner-membrane energy-coupling subunit for TonB-dependent iron acquisition rather than as a substrate-specific transporter itself (cornelis2010ironuptakeand pages 1-3) | Review notes gated OM receptors are 22-stranded β-barrels (cornelis2010ironuptakeand pages 1-3) | https://doi.org/10.1007/s00253-010-2550-2 |
| Villalobos-Escobedo et al., 2023 | Peer-reviewed primary study (RB-TnSeq) | *P. putida* KT2440 and other plant-associated bacteria | Genome-wide fitness under *Trichoderma atroviride* exometabolites; iron uptake functions | In the mixed-species analysis, TonB/ExbB/ExbD-dependent siderophore transport was especially important in the nitrogen-fixing bacteria tested, while *P. putida* showed dependence on membrane lipid modification pathways overall; additional inspection indicated iron-uptake genes were required for *P. putida* fitness in fungal exudates, consistent with ecological importance of TonB-linked iron acquisition even if exbB was not the dominant hit in the summary text (villalobosescobedo2023genomewidefitnessprofiling pages 3-6, villalobosescobedo2023genomewidefitnessprofiling pages 1-2, villalobosescobedo2023genomewidefitnessprofiling pages 10-11) | Significant fitness thresholds were log2 fitness < -1 with t-score < -4 for negative hits; 41 *P. putida* genes had negative fitness under the stated filter in spent medium experiments (villalobosescobedo2023genomewidefitnessprofiling pages 3-6, villalobosescobedo2023genomewidefitnessprofiling pages 10-11) | https://doi.org/10.1371/journal.pgen.1010909 |


*Table: This table summarizes the main mechanistic and organism-specific sources relevant to annotation of *Pseudomonas putida* KT2440 exbB (PP_5306; UniProt Q88C77). It highlights evidence for operon context, inner-membrane localization, pmf-coupled TonB energization, and experimentally observed phenotypes when the exbBD-tonB system is disrupted.*

## Limitations of available evidence
Direct, single-gene **exbB-only** knockout phenotypes in KT2440 were not present in the retrieved full-text set; KT2440 phenotypes cited here derive from a **cluster deletion (exbB–exbD–tonB)**. Mechanistic, residue-level and stoichiometric details are primarily derived from *E. coli* and other model systems and are inferred to be conserved in *Pseudomonas* based on strong homology and shared operon architecture. (braun2023energizationofouter pages 11-13, weimer2024systemsmetabolicengineering pages 87-93)

References

1. (weimer2024systemsmetabolicengineering pages 87-93): ALA Weimer. Systems metabolic engineering of electrogenic anaerobic pseudomonas putida for enhanced 2-ketogluconate production. Unknown journal, 2024.

2. (weimer2024systemsmetabolicengineering pages 93-97): ALA Weimer. Systems metabolic engineering of electrogenic anaerobic pseudomonas putida for enhanced 2-ketogluconate production. Unknown journal, 2024.

3. (braun2023energizationofouter pages 11-13): Volkmar Braun, Anna C. Ratliff, Herve Celia, and Susan K. Buchanan. Energization of outer membrane transport by the exbb exbd molecular motor. Journal of Bacteriology, Jun 2023. URL: https://doi.org/10.1128/jb.00035-23, doi:10.1128/jb.00035-23. This article has 39 citations and is from a peer-reviewed journal.

4. (braun2024substrateuptakeby pages 11-12): Volkmar Braun. Substrate uptake by tonb‐dependent outer membrane transporters. Molecular Microbiology, 122:929-947, Dec 2024. URL: https://doi.org/10.1111/mmi.15332, doi:10.1111/mmi.15332. This article has 20 citations and is from a domain leading peer-reviewed journal.

5. (braun2024substrateuptakeby pages 1-2): Volkmar Braun. Substrate uptake by tonb‐dependent outer membrane transporters. Molecular Microbiology, 122:929-947, Dec 2024. URL: https://doi.org/10.1111/mmi.15332, doi:10.1111/mmi.15332. This article has 20 citations and is from a domain leading peer-reviewed journal.

6. (braun2023energizationofouter pages 1-3): Volkmar Braun, Anna C. Ratliff, Herve Celia, and Susan K. Buchanan. Energization of outer membrane transport by the exbb exbd molecular motor. Journal of Bacteriology, Jun 2023. URL: https://doi.org/10.1128/jb.00035-23, doi:10.1128/jb.00035-23. This article has 39 citations and is from a peer-reviewed journal.

7. (cornelis2010ironuptakeand pages 1-3): Pierre Cornelis. Iron uptake and metabolism in pseudomonads. Applied Microbiology and Biotechnology, 86:1637-1645, Mar 2010. URL: https://doi.org/10.1007/s00253-010-2550-2, doi:10.1007/s00253-010-2550-2. This article has 549 citations and is from a domain leading peer-reviewed journal.

8. (braun2023energizationofouter pages 4-6): Volkmar Braun, Anna C. Ratliff, Herve Celia, and Susan K. Buchanan. Energization of outer membrane transport by the exbb exbd molecular motor. Journal of Bacteriology, Jun 2023. URL: https://doi.org/10.1128/jb.00035-23, doi:10.1128/jb.00035-23. This article has 39 citations and is from a peer-reviewed journal.

9. (braun2023energizationofouter pages 13-15): Volkmar Braun, Anna C. Ratliff, Herve Celia, and Susan K. Buchanan. Energization of outer membrane transport by the exbb exbd molecular motor. Journal of Bacteriology, Jun 2023. URL: https://doi.org/10.1128/jb.00035-23, doi:10.1128/jb.00035-23. This article has 39 citations and is from a peer-reviewed journal.

10. (braun2023energizationofouter pages 3-4): Volkmar Braun, Anna C. Ratliff, Herve Celia, and Susan K. Buchanan. Energization of outer membrane transport by the exbb exbd molecular motor. Journal of Bacteriology, Jun 2023. URL: https://doi.org/10.1128/jb.00035-23, doi:10.1128/jb.00035-23. This article has 39 citations and is from a peer-reviewed journal.

11. (godoy2001involvementofthe pages 4-5): Patricia Godoy, Marı́a Isabel Ramos-González, and Juan L. Ramos. Involvement of the tonb system in tolerance to solvents and drugs in pseudomonas putida dot-t1e. Journal of Bacteriology, 183:5285-5292, Sep 2001. URL: https://doi.org/10.1128/jb.183.18.5285-5292.2001, doi:10.1128/jb.183.18.5285-5292.2001. This article has 42 citations and is from a peer-reviewed journal.

12. (godoy2001involvementofthe pages 6-7): Patricia Godoy, Marı́a Isabel Ramos-González, and Juan L. Ramos. Involvement of the tonb system in tolerance to solvents and drugs in pseudomonas putida dot-t1e. Journal of Bacteriology, 183:5285-5292, Sep 2001. URL: https://doi.org/10.1128/jb.183.18.5285-5292.2001, doi:10.1128/jb.183.18.5285-5292.2001. This article has 42 citations and is from a peer-reviewed journal.

13. (villalobosescobedo2023genomewidefitnessprofiling pages 10-11): José Manuel Villalobos-Escobedo, Maria Belen Mercado-Esquivias, Catharine Adams, W. Berkeley Kauffman, Rex R. Malmstrom, Adam M. Deutschbauer, and N. Louise Glass. Genome-wide fitness profiling reveals molecular mechanisms that bacteria use to interact with trichoderma atroviride exometabolites. PLOS Genetics, 19:e1010909, Aug 2023. URL: https://doi.org/10.1371/journal.pgen.1010909, doi:10.1371/journal.pgen.1010909. This article has 6 citations and is from a domain leading peer-reviewed journal.

14. (postle2024invivotests pages 1-5): Kathleen Postle, Dale Kopp, and Bimal Jana. In vivo tests of the e. coli tonb system working model—interaction of exbb with unknown proteins, identification of tonb-exbd transmembrane heterodimers and pmf-dependent exbd structures. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.10.602958, doi:10.1101/2024.07.10.602958. This article has 0 citations.

15. (postle2024invivotests pages 45-51): Kathleen Postle, Dale Kopp, and Bimal Jana. In vivo tests of the e. coli tonb system working model—interaction of exbb with unknown proteins, identification of tonb-exbd transmembrane heterodimers and pmf-dependent exbd structures. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.10.602958, doi:10.1101/2024.07.10.602958. This article has 0 citations.

16. (graff2024siderophoresastools pages 1-2): Á. Tamás Gräff and Sarah M. Barry. Siderophores as tools and treatments. npj Antimicrobials and Resistance, Dec 2024. URL: https://doi.org/10.1038/s44259-024-00053-4, doi:10.1038/s44259-024-00053-4. This article has 29 citations and is from a peer-reviewed journal.

17. (graff2024siderophoresastools pages 2-4): Á. Tamás Gräff and Sarah M. Barry. Siderophores as tools and treatments. npj Antimicrobials and Resistance, Dec 2024. URL: https://doi.org/10.1038/s44259-024-00053-4, doi:10.1038/s44259-024-00053-4. This article has 29 citations and is from a peer-reviewed journal.

18. (schalk2025bacterialsiderophoresdiversity pages 42-46): Isabelle J. Schalk. Bacterial siderophores: diversity, uptake pathways and applications. Nature reviews. Microbiology, 23:24-40, Sep 2025. URL: https://doi.org/10.1038/s41579-024-01090-6, doi:10.1038/s41579-024-01090-6. This article has 215 citations.

19. (braun2023energizationofouter pages 6-8): Volkmar Braun, Anna C. Ratliff, Herve Celia, and Susan K. Buchanan. Energization of outer membrane transport by the exbb exbd molecular motor. Journal of Bacteriology, Jun 2023. URL: https://doi.org/10.1128/jb.00035-23, doi:10.1128/jb.00035-23. This article has 39 citations and is from a peer-reviewed journal.

20. (weimer2024systemsmetabolicengineering pages 97-101): ALA Weimer. Systems metabolic engineering of electrogenic anaerobic pseudomonas putida for enhanced 2-ketogluconate production. Unknown journal, 2024.

21. (godoy2001involvementofthe pages 1-2): Patricia Godoy, Marı́a Isabel Ramos-González, and Juan L. Ramos. Involvement of the tonb system in tolerance to solvents and drugs in pseudomonas putida dot-t1e. Journal of Bacteriology, 183:5285-5292, Sep 2001. URL: https://doi.org/10.1128/jb.183.18.5285-5292.2001, doi:10.1128/jb.183.18.5285-5292.2001. This article has 42 citations and is from a peer-reviewed journal.

22. (villalobosescobedo2023genomewidefitnessprofiling pages 3-6): José Manuel Villalobos-Escobedo, Maria Belen Mercado-Esquivias, Catharine Adams, W. Berkeley Kauffman, Rex R. Malmstrom, Adam M. Deutschbauer, and N. Louise Glass. Genome-wide fitness profiling reveals molecular mechanisms that bacteria use to interact with trichoderma atroviride exometabolites. PLOS Genetics, 19:e1010909, Aug 2023. URL: https://doi.org/10.1371/journal.pgen.1010909, doi:10.1371/journal.pgen.1010909. This article has 6 citations and is from a domain leading peer-reviewed journal.

23. (villalobosescobedo2023genomewidefitnessprofiling pages 1-2): José Manuel Villalobos-Escobedo, Maria Belen Mercado-Esquivias, Catharine Adams, W. Berkeley Kauffman, Rex R. Malmstrom, Adam M. Deutschbauer, and N. Louise Glass. Genome-wide fitness profiling reveals molecular mechanisms that bacteria use to interact with trichoderma atroviride exometabolites. PLOS Genetics, 19:e1010909, Aug 2023. URL: https://doi.org/10.1371/journal.pgen.1010909, doi:10.1371/journal.pgen.1010909. This article has 6 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](exbB-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. weimer2024systemsmetabolicengineering pages 87-93
2. braun2024substrateuptakeby pages 1-2
3. braun2024substrateuptakeby pages 11-12
4. braun2023energizationofouter pages 4-6
5. braun2023energizationofouter pages 13-15
6. cornelis2010ironuptakeand pages 1-3
7. weimer2024systemsmetabolicengineering pages 93-97
8. godoy2001involvementofthe pages 4-5
9. villalobosescobedo2023genomewidefitnessprofiling pages 10-11
10. schalk2025bacterialsiderophoresdiversity pages 42-46
11. braun2023energizationofouter pages 11-13
12. braun2023energizationofouter pages 1-3
13. braun2023energizationofouter pages 3-4
14. godoy2001involvementofthe pages 6-7
15. postle2024invivotests pages 1-5
16. postle2024invivotests pages 45-51
17. graff2024siderophoresastools pages 1-2
18. graff2024siderophoresastools pages 2-4
19. braun2023energizationofouter pages 6-8
20. weimer2024systemsmetabolicengineering pages 97-101
21. godoy2001involvementofthe pages 1-2
22. villalobosescobedo2023genomewidefitnessprofiling pages 3-6
23. villalobosescobedo2023genomewidefitnessprofiling pages 1-2
24. 14C
25. https://doi.org/10.1128/jb.00035-23
26. https://doi.org/10.1111/mmi.15332
27. https://doi.org/10.1128/jb.00303-19
28. https://doi.org/10.1128/jb.183.18.5285-5292.2001
29. https://doi.org/10.1007/s00253-010-2550-2
30. https://doi.org/10.1371/journal.pgen.1010909
31. https://doi.org/10.1128/jb.00035-23,
32. https://doi.org/10.1111/mmi.15332,
33. https://doi.org/10.1007/s00253-010-2550-2,
34. https://doi.org/10.1128/jb.183.18.5285-5292.2001,
35. https://doi.org/10.1371/journal.pgen.1010909,
36. https://doi.org/10.1101/2024.07.10.602958,
37. https://doi.org/10.1038/s44259-024-00053-4,
38. https://doi.org/10.1038/s41579-024-01090-6,