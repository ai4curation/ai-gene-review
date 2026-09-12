---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-11T22:04:34.879252'
end_time: '2026-06-11T22:15:27.415963'
duration_seconds: 652.54
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: recB
  gene_symbol: recB
  uniprot_accession: Q88DZ5
  protein_description: 'RecName: Full=RecBCD enzyme subunit RecB {ECO:0000256|HAMAP-Rule:MF_01485};
    EC=3.1.11.5 {ECO:0000256|HAMAP-Rule:MF_01485}; EC=5.6.2.4 {ECO:0000256|HAMAP-Rule:MF_01485};
    AltName: Full=DNA 3''-5'' helicase subunit RecB {ECO:0000256|HAMAP-Rule:MF_01485};
    AltName: Full=Exonuclease V subunit RecB {ECO:0000256|HAMAP-Rule:MF_01485}; Short=ExoV
    subunit RecB {ECO:0000256|HAMAP-Rule:MF_01485}; AltName: Full=Helicase/nuclease
    RecBCD subunit RecB {ECO:0000256|HAMAP-Rule:MF_01485};'
  gene_info: Name=recB {ECO:0000256|HAMAP-Rule:MF_01485, ECO:0000313|EMBL:AAN70246.1};
    OrderedLocusNames=PP_4673 {ECO:0000313|EMBL:AAN70246.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the helicase family. UvrD subfamily.
  protein_domains: DNA_helicase_UvrD-like_C. (IPR014017); DNA_helicase_UvrD/REP. (IPR000212);
    P-loop_NTPase. (IPR027417); PDDEXK-like_dom_sf. (IPR011604); PDDEXK_AddAB-type.
    (IPR038726)
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
  path: recB-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q88DZ5
- **Protein Description:** RecName: Full=RecBCD enzyme subunit RecB {ECO:0000256|HAMAP-Rule:MF_01485}; EC=3.1.11.5 {ECO:0000256|HAMAP-Rule:MF_01485}; EC=5.6.2.4 {ECO:0000256|HAMAP-Rule:MF_01485}; AltName: Full=DNA 3'-5' helicase subunit RecB {ECO:0000256|HAMAP-Rule:MF_01485}; AltName: Full=Exonuclease V subunit RecB {ECO:0000256|HAMAP-Rule:MF_01485}; Short=ExoV subunit RecB {ECO:0000256|HAMAP-Rule:MF_01485}; AltName: Full=Helicase/nuclease RecBCD subunit RecB {ECO:0000256|HAMAP-Rule:MF_01485};
- **Gene Information:** Name=recB {ECO:0000256|HAMAP-Rule:MF_01485, ECO:0000313|EMBL:AAN70246.1}; OrderedLocusNames=PP_4673 {ECO:0000313|EMBL:AAN70246.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the helicase family. UvrD subfamily.
- **Key Domains:** DNA_helicase_UvrD-like_C. (IPR014017); DNA_helicase_UvrD/REP. (IPR000212); P-loop_NTPase. (IPR027417); PDDEXK-like_dom_sf. (IPR011604); PDDEXK_AddAB-type. (IPR038726)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "recB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'recB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **recB** (gene ID: recB, UniProt: Q88DZ5) in PSEPK.

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
- **UniProt Accession:** Q88DZ5
- **Protein Description:** RecName: Full=RecBCD enzyme subunit RecB {ECO:0000256|HAMAP-Rule:MF_01485}; EC=3.1.11.5 {ECO:0000256|HAMAP-Rule:MF_01485}; EC=5.6.2.4 {ECO:0000256|HAMAP-Rule:MF_01485}; AltName: Full=DNA 3'-5' helicase subunit RecB {ECO:0000256|HAMAP-Rule:MF_01485}; AltName: Full=Exonuclease V subunit RecB {ECO:0000256|HAMAP-Rule:MF_01485}; Short=ExoV subunit RecB {ECO:0000256|HAMAP-Rule:MF_01485}; AltName: Full=Helicase/nuclease RecBCD subunit RecB {ECO:0000256|HAMAP-Rule:MF_01485};
- **Gene Information:** Name=recB {ECO:0000256|HAMAP-Rule:MF_01485, ECO:0000313|EMBL:AAN70246.1}; OrderedLocusNames=PP_4673 {ECO:0000313|EMBL:AAN70246.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the helicase family. UvrD subfamily.
- **Key Domains:** DNA_helicase_UvrD-like_C. (IPR014017); DNA_helicase_UvrD/REP. (IPR000212); P-loop_NTPase. (IPR027417); PDDEXK-like_dom_sf. (IPR011604); PDDEXK_AddAB-type. (IPR038726)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "recB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'recB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **recB** (gene ID: recB, UniProt: Q88DZ5) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Research report: **recB (UniProt Q88DZ5)** — RecBCD enzyme subunit RecB in *Pseudomonas putida* KT2440

## 0. Gene/protein identity verification (critical)
The user-specified target is UniProt **Q88DZ5**, annotated as **RecBCD enzyme subunit RecB (Exonuclease V / DNA 3′→5′ helicase subunit RecB)** from *Pseudomonas putida* KT2440. Within the retrieved literature corpus, I did **not** find a primary source that explicitly maps **UniProt Q88DZ5** (or locus **PP_4673**) to a specific experimental construct or phenotype in *P. putida* KT2440; therefore, organism-specific interpretation for KT2440 necessarily relies on (i) general RecBCD/RecB mechanistic literature and (ii) *Pseudomonas* (non-KT2440) RecBCD studies plus KT2440 pathway-context studies. This report **does not** reassign the gene to another identity.

## 1. Key concepts and current understanding

### 1.1 What RecB is (definition)
**RecB** is the multifunctional helicase–nuclease subunit of the **RecBCD** complex (RecB–RecC–RecD), historically called **Exonuclease V**. RecBCD initiates the major bacterial pathway for processing DNA double-strand ends (DSEs) into recombinogenic substrates for homologous recombination (HR) and double-strand break (DSB) repair. (Dec 2023 review: Amundsen & Smith, *Microbiology and Molecular Biology Reviews*, 2023-12-20, https://doi.org/10.1128/mmbr.00041-23) (amundsen2023recbcdenzymemechanistic pages 1-2)

### 1.2 Biochemical activities attributed to RecB within RecBCD
RecBCD is an **ATP-dependent helicase–nuclease** that binds blunt or nearly blunt dsDNA ends, unwinds DNA extremely rapidly and processively, and degrades DNA strands during unwinding. The complex can unwind at ~**1 kb/s** and can be highly processive (≥100 kb), with RecB contributing the **3′→5′ motor/translocase** activity and a **Mg2+-dependent nuclease domain** responsible for end-processing. (Amundsen & Smith 2023, https://doi.org/10.1128/mmbr.00041-23) (amundsen2023recbcdenzymemechanistic pages 4-6)

Mechanistically, RecBCD’s coordinated motors drive strand separation: RecB translocates along the 3′-ended strand while RecD translocates along the 5′-ended strand, creating asymmetric intermediates (ssDNA tails/loops) and enabling coupled nuclease processing. (Amundsen & Smith 2023, https://doi.org/10.1128/mmbr.00041-23) (amundsen2023recbcdenzymemechanistic pages 2-4)

### 1.3 Chi (χ) sites and the RecBCD “activity switch”
A defining concept for RecBCD-mediated repair is **Chi (χ)**: short, oriented recombination hotspot sequences that regulate RecBCD’s nuclease and recombination-promoting activities. In *E. coli*, Chi is the octamer **5′-GCTGGTGG-3′** and is recognized when present in the correct orientation relative to the DNA end at which RecBCD loaded. Chi recognition triggers a switch in RecBCD behavior such that RecB nicks the 3′-ended strand ~**5 nt** to the 3′ side of Chi and RecBCD then promotes **RecA loading** on the emergent 3′ ssDNA tail. (Amundsen & Smith 2023, https://doi.org/10.1128/mmbr.00041-23; Smith 2012, *MMBR*, 2012-06-01, https://doi.org/10.1128/mmbr.05026-11) (amundsen2023recbcdenzymemechanistic pages 4-6, smith2012howrecbcdenzyme pages 2-4)

Chi recognition is **species-specific** in many bacteria. In *Pseudomonas syringae* Lz4W, a cognate Chi-like octamer (**ChiPs**) was identified as **5′-GCTGGCGC-3′**, illustrating that pseudomonads can use a different regulatory octamer than *E. coli*. (Pavankumar et al., *PLOS ONE*, 2018-05-16, https://doi.org/10.1371/journal.pone.0197476) (pavankumar2018biochemicalcharacterizationof pages 1-2)

### 1.4 Domain architecture and RecA-loading function of RecB
RecB is functionally bipartite (helicase/translocase + nuclease/RecA-loading functions), and interdomain connectivity is mechanistically important. RecB’s nuclease domain is connected to the helicase domain via a short tether in models synthesized from genetics/structures, and Chi-triggered control involves conformational communication between RecC (Chi recognition tunnel) and RecB (nuclease/RecA loading). (Amundsen & Smith 2023, https://doi.org/10.1128/mmbr.00041-23) (amundsen2023recbcdenzymemechanistic pages 4-6)

A 2024 mechanistic study further refined the model of Chi-dependent RecA loading by showing that the **RecB nuclease domain** can **trans-complement** a truncated RecBCD complex lacking that domain, supporting a Chi-induced rearrangement that exposes the RecA-loading surface rather than requiring a strictly tethered “swing-out” action. (Pavankumar et al., *Nucleic Acids Research*, 2024-01-16, https://doi.org/10.1093/nar/gkae007) (pavankumar2024transcomplementationbythe pages 1-2)

### 1.5 Pathway placement (biological process context)
RecBCD-mediated processing is central to bacterial DSB repair and also to replication-fork rescue: RecBCD acts on DSEs produced by collapsed forks (one-ended DSBs) and other replication stress events, generating the 3′ ssDNA substrate for RecA-mediated strand invasion, with downstream branch migration/resolution involving RuvABC. (Sinha et al., *FEMS Microbiology Reviews*, 2020-04-01, https://doi.org/10.1093/femsre/fuaa009) (sinha2020therolesof pages 2-3)

### 1.6 Subcellular localization (where RecB acts)
No KT2440-specific localization imaging for RecB was retrieved. Functionally, RecBCD acts on chromosomal DNA ends and replication-associated DNA structures; thus, the relevant localization is **cytoplasmic/nucleoid-associated**, not membrane-embedded or secreted. (Amundsen & Smith 2023; Sinha et al. 2020) (amundsen2023recbcdenzymemechanistic pages 4-6, sinha2020therolesof pages 2-3)

## 2. Pseudomonas-specific evidence relevant to interpreting *P. putida* recB

### 2.1 Genetic evidence in a pseudomonad: RecB is required for DNA repair and stress growth, with motor activity prioritized
In the Antarctic pseudomonad *Pseudomonas syringae* Lz4W, **null mutations** of **recB**, **recC**, or **recD** (or deletion of the full recCBD operon) cause sensitivity to **UV** and **mitomycin C** and a strong **growth/viability defect at 4°C**, with accumulation of **linear chromosomal DNA** and short DNA fragments—phenotypes consistent with defective DSB processing/repair. (Pavankumar et al., *PLOS ONE*, 2010-02-17, https://doi.org/10.1371/journal.pone.0009412) (pavankumar2010allthreesubunits pages 1-2, pavankumar2010allthreesubunits pages 4-7)

Crucially, targeted active-site mutants separated RecB functions:
- **ATPase/helicase motor** mutants in RecB (RecB K28Q/K29Q in that study’s notation) and RecD (RecD K229Q) were defective in DNA repair phenotypes and cold growth, indicating ATP-dependent motor functions are essential in vivo. (pavankumar2010allthreesubunits pages 1-2, pavankumar2010allthreesubunits pages 7-8)
- By contrast, a **RecB nuclease-center** mutant (D1118A) was highly deficient for exonuclease activity yet could still support UV/MMC resistance and near-wild-type low-temperature growth in that system, implying that under some conditions the nuclease contribution is less critical than the ATP-dependent unwinding/translocation functions. (pavankumar2010allthreesubunits pages 7-8)

Complementation data also support conservation of core RecBCD function: plasmid-borne **E. coli recBCD** could complement defects of a *P. syringae* ΔrecCBD strain. (pavankumar2010allthreesubunits pages 1-2)

### 2.2 Species-specific Chi recognition within Pseudomonas
Biochemical characterization of RecBCD from *P. syringae* Lz4W identified the species-specific Chi-like octamer **5′-GCTGGCGC-3′** (ChiPs) and noted functional differences relative to *E. coli* RecBCD (e.g., RecD indispensability for specific Chi-like fragment production). (Pavankumar et al., *PLOS ONE*, 2018-05-16, https://doi.org/10.1371/journal.pone.0197476) (pavankumar2018biochemicalcharacterizationof pages 1-2)

This matters for *P. putida* KT2440 annotation: even if RecB is homologous, the **exact Chi sequence and switching kinetics** may differ across pseudomonads and should not be assumed to match *E. coli* without direct evidence.

## 3. *Pseudomonas putida* KT2440-specific evidence (available in retrieved corpus)

### 3.1 DNA-damage tolerance in KT2440 is strongly influenced by prophage load; recombination capacity appears unchanged
A high-citation study in *Environmental Microbiology* examined the “proviral load” of *P. putida* KT2440 and created a prophage-free derivative (Δall-Φ). In UV assays, KT2440 was reported to be extraordinarily UV sensitive relative to *E. coli* (30 J/m² leaving *E. coli* “virtually intact” but reducing KT2440 survival by >4 orders of magnitude), and deleting all prophages increased UV tolerance—especially at 15–30 J/m². (Martínez-García et al., *Environmental Microbiology*, 2015-06-01, https://doi.org/10.1111/1462-2920.12492) (martinez‐garcia2015freeingpseudomonasputida pages 7-10)

Importantly for functional annotation: the same work reports that measures of **RecA-mediated homologous recombination** showed **no significant difference** between wild type KT2440 and Δall-Φ, and spontaneous mutation rates (rifampicin resistance) were comparable, suggesting that increased DNA-damage tolerance in Δall-Φ is not due to a global increase in HR capacity but likely due to eliminating SOS-triggered lethal prophage induction. (martinez‐garcia2015freeingpseudomonasputida pages 7-10, martinez‐garcia2015freeingpseudomonasputida pages 10-12)

Although this study mentions directed **recA** and **recB** mutants in its experimental framing, the retrieved text segments did not provide direct, quantitative recB-mutant phenotype readouts. Therefore, it provides **pathway context** for DNA damage and SOS induction in KT2440, but not a direct functional dissection of PP_4673/Q88DZ5.

## 4. Recent developments (prioritizing 2023–2024)

### 4.1 Authoritative synthesis of RecB/RecBCD mechanism (Dec 2023)
A 2023 *MMBR* review consolidated structural/genetic/biochemical evidence that RecBCD is an exceptionally fast and processive helicase–nuclease and emphasized RecB’s tethered nuclease domain and Chi-dependent switching that yields a nick near Chi and subsequent RecA loading. (Amundsen & Smith, 2023-12-20, https://doi.org/10.1128/mmbr.00041-23) (amundsen2023recbcdenzymemechanistic pages 4-6, amundsen2023recbcdenzymemechanistic pages 1-2)

### 4.2 New mechanistic insight into Chi-dependent RecA loading (Jan 2024)
A 2024 paper in *Nucleic Acids Research* tested the long-discussed model that Chi recognition undocks the RecB nuclease domain to reveal a RecA-loading interface. Reconstitution experiments showed that a severed RecB nuclease domain can still functionally enable RecA loading when paired with a truncated RecBCD lacking that domain, supporting a Chi-induced rearrangement mechanism in which the RecA-loading surface is exposed by conformational change rather than a purely tether-constrained “swing-out.” (Pavankumar et al., 2024-01-16, https://doi.org/10.1093/nar/gkae007) (pavankumar2024transcomplementationbythe pages 1-2)

## 5. Current applications and real-world implementations

### 5.1 Genome editing and recombineering in Pseudomonas: RecBCD is a barrier and/or modulator
While not an assay of KT2440 RecB function per se, modern Pseudomonas genome engineering often contends with host nucleases that degrade linear DNA substrates; RecBCD is frequently a key factor in this context.

A 2023 study demonstrating improved CRISPR/Cas9 editing in *E. coli* and *Pseudomonas* showed that DSB repair outcomes in bacterial genome editing can occur independently of RecA and RecBCD under certain engineered conditions (SSB-mediated effects), illustrating how host DSB-repair factors are relevant design variables in applied editing workflows. (Chai et al., *Microorganisms*, 2023-03-30, https://doi.org/10.3390/microorganisms11040850) (pavankumar2018biochemicalcharacterizationof pages 1-2)

KT2440 is also an active platform for recombineering-based engineering (e.g., integration/deletion of large genomic regions), underscoring the practical importance of understanding DNA repair and end-processing systems in this chassis even when individual studies do not isolate recB phenotypes. (Martínez-García et al. 2015 discusses extensive phenotyping under >1000 conditions and DNA-damage assays in KT2440 backgrounds.) (martinez‐garcia2015freeingpseudomonasputida pages 7-10)

## 6. Expert opinions / authoritative interpretations

### 6.1 Consensus view: RecBCD (RecB) sits at the initiation of DSB repair and recombination
Highly cited authoritative reviews describe RecBCD as the entry point to DSB repair by HR, combining end binding, unwinding, regulated nucleolysis, and RecA loading controlled by Chi sequences. (Smith 2012, https://doi.org/10.1128/mmbr.05026-11; Sinha et al. 2020, https://doi.org/10.1093/femsre/fuaa009; Amundsen & Smith 2023, https://doi.org/10.1128/mmbr.00041-23) (smith2012howrecbcdenzyme pages 2-4, sinha2020therolesof pages 2-3, amundsen2023recbcdenzymemechanistic pages 4-6)

### 6.2 Nuanced view: “nuclease” vs “motor” importance can be context-dependent
The *Pseudomonas syringae* genetic dissection provides an expert-relevant nuance: in that organism’s cold-stress context, ATP-dependent motor function of RecB/RecD is essential, while the RecB nuclease center can be partially bypassed/compensated (e.g., by RecJ), highlighting that **in vivo criticality of RecB subfunctions can vary with physiology and redundant pathways**. (Pavankumar et al. 2010, https://doi.org/10.1371/journal.pone.0009412) (pavankumar2010allthreesubunits pages 7-8, pavankumar2010allthreesubunits pages 8-9)

## 7. Relevant statistics and quantitative data

### 7.1 Enzyme kinetics/behavior
- RecBCD unwinding can reach ~**1 kb/s** and be highly processive (≥100 kb) under conditions summarized in recent review literature. (Amundsen & Smith 2023) (amundsen2023recbcdenzymemechanistic pages 4-6)

### 7.2 Sequence features
- *E. coli* Chi: **5′-GCTGGTGG-3′** (Smith 2012; Amundsen & Smith 2023). (smith2012howrecbcdenzyme pages 2-4, amundsen2023recbcdenzymemechanistic pages 4-6)
- *P. syringae* ChiPs: **5′-GCTGGCGC-3′** (Pavankumar et al. 2018). (pavankumar2018biochemicalcharacterizationof pages 1-2)

### 7.3 Cellular abundance (mostly from *E. coli* single-cell/synthesis measurements)
RecB is repeatedly described as a **low-copy** DNA repair protein, on the order of only a few molecules per cell in *E. coli*. A synthesis review cites ~**5 RecB molecules/cell**, and a later single-cell study measured ~**3.9 ± 0.6 molecules/cell** (with recB mRNA mean ~0.62 molecules/cell). While these values are not from *P. putida*, they underscore that RecB is tightly regulated due to its potent DNA-processing activity. (Vincent & Uphoff, *Biochemical Society Transactions*, 2020-03-23, https://doi.org/10.1042/bst20190364; Kalita et al., *eLife*, 2025-08-21, https://doi.org/10.7554/elife.94918) (vincent2020bacterialphenotypicheterogeneity pages 2-4, kalita2025anhfqdependentposttranscriptional pages 2-3)

## 8. Structured functional annotation summary
| Category | Summary |
|---|---|
| Identity/Complex | UniProt Q88DZ5 is annotated as RecBCD enzyme subunit RecB from *Pseudomonas putida* KT2440; available mechanistic literature supports RecB as the helicase–nuclease subunit of the heterotrimeric RecBCD complex (RecB/RecC/RecD), also called Exonuclease V, with RecB carrying helicase/ATPase and nuclease-linked functions (amundsen2023recbcdenzymemechanistic pages 4-6, amundsen2023recbcdenzymemechanistic pages 1-2, amundsen2023recbcdenzymemechanistic pages 2-4). |
| Enzymatic activities | RecB contributes ATP-dependent 3′→5′ translocation/helicase activity, while its C-terminal nuclease domain cleaves DNA in a Mg2+-dependent manner; after Chi recognition, RecBCD nicks the 3′-ended strand and promotes RecA loading onto the resulting 3′ ssDNA tail (amundsen2023recbcdenzymemechanistic pages 4-6, sinha2020therolesof pages 2-3, pavankumar2024transcomplementationbythe pages 1-2, smith2012howrecbcdenzyme pages 2-4). |
| Substrates | RecBCD acts primarily on blunt or nearly blunt dsDNA ends, including two-ended DSBs and one-ended broken replication forks; during processing it unwinds duplex DNA and degrades emerging ssDNA to short oligonucleotides, ultimately generating recombinogenic 3′-tailed DNA (amundsen2023recbcdenzymemechanistic pages 4-6, pavankumar2018biochemicalcharacterizationof pages 1-2, sinha2020therolesof pages 2-3, amundsen2023recbcdenzymemechanistic pages 2-4). |
| Chi regulation | Canonical *E. coli* Chi is 5′-GCTGGTGG-3′ and triggers a switch from degradative to recombination-promoting processing; in *Pseudomonas syringae* Lz4W the cognate octamer is ChiPs 5′-GCTGGCGC-3′, showing that Chi recognition is species-specific within pseudomonads (amundsen2023recbcdenzymemechanistic pages 4-6, pavankumar2018biochemicalcharacterizationof pages 1-2, amundsen2023recbcdenzymemechanistic pages 8-11, smith2012howrecbcdenzyme pages 2-4). |
| Pathway role | RecB functions in the major bacterial homologous recombination pathway for DSB repair, replication-fork rescue, and genome maintenance by helping RecBCD create a 3′ overhang and load RecA, followed by downstream RuvABC-mediated branch migration/resolution (pavankumar2018biochemicalcharacterizationof pages 1-2, sinha2020therolesof pages 2-3, amundsen2023recbcdenzymemechanistic pages 1-2, amundsen2023recbcdenzymemechanistic pages 2-4). |
| Localization | No direct localization study for Q88DZ5 in KT2440 was retrieved, but RecBCD acts on chromosomal DNA ends and stalled/broken replication forks; this supports a cytoplasmic, nucleoid-associated functional location rather than membrane or extracellular localization (amundsen2023recbcdenzymemechanistic pages 4-6, sinha2020therolesof pages 2-3, amundsen2023recbcdenzymemechanistic pages 2-4). |
| Pseudomonas-specific evidence | In *P. syringae* Lz4W, recB/recC/recD mutants are UV- and mitomycin C-sensitive, fail to grow at 4°C, and accumulate linear/fragmented chromosomal DNA; RecB and RecD ATPase/helicase activities are essential in vivo, whereas RecB nuclease activity is partly dispensable and can be compensated by RecJ in some contexts (pavankumar2010allthreesubunits pages 1-2, pavankumar2010allthreesubunits pages 7-8, pavankumar2010allthreesubunits pages 8-9, pavankumar2010allthreesubunits pages 10-13). |
| KT2440-specific evidence | Direct experimental evidence for PP_4673/Q88DZ5 in *P. putida* KT2440 is limited in the retrieved corpus. KT2440 studies instead show that DNA-damage tolerance and SOS-linked phenotypes can be assayed genetically in this strain, and that prophage-free KT2440 is more UV-tolerant without detectable change in RecA-mediated homologous recombination; these data provide pathway context but not a direct recB functional test (martinez‐garcia2015freeingpseudomonasputida pages 7-10, martinez‐garcia2015freeingpseudomonasputida pages 12-15, martinez‐garcia2015freeingpseudomonasputida pages 10-12). |
| Recent (2023-2024) advances | Recent work refined RecB-centered mechanism: a 2023 review synthesized mutant/structural evidence for RecB tethering, Chi-triggered conformational control, and inter-subunit signaling; a 2024 study showed the RecB nuclease domain can trans-complement truncated RecBCD, supporting a Chi-induced rearrangement that exposes the RecA-loading surface rather than a simple tethered “swing-out” model (amundsen2023recbcdenzymemechanistic pages 4-6, amundsen2023recbcdenzymemechanistic pages 1-2, pavankumar2024transcomplementationbythe pages 1-2). |
| Quantitative stats | RecBCD is among the fastest/processive bacterial helicase–nucleases, reported at ~1 kb/s and ≥100 kb processivity in recent review literature; older review values cite ~300 bp/s depending on assay conditions. In *E. coli*, RecB is low abundance (~5 molecules/cell in one synthesis; ~3.9 ± 0.6 molecules/cell in a later single-cell study), indicating tight expression control for this potentially DNA-destructive activity (amundsen2023recbcdenzymemechanistic pages 4-6, smith2012howrecbcdenzyme pages 2-4, kalita2025anhfqdependentposttranscriptional pages 2-3, vincent2020bacterialphenotypicheterogeneity pages 2-4). |


*Table: This table summarizes the evidence-supported functional annotation of RecB/RecBCD for *Pseudomonas putida* KT2440, while clearly separating broad conserved RecBCD biology from the more limited KT2440-specific evidence. It is useful for identifying what can be stated confidently for Q88DZ5 and where inference relies on pseudomonad or model-organism studies.*

## 9. Practical conclusions for functional annotation of **recB (Q88DZ5) in *P. putida* KT2440**
1. **Primary molecular function (high confidence, conserved):** RecB is the ATP-dependent helicase–nuclease subunit of RecBCD that initiates processing of blunt/nearly blunt dsDNA ends into a recombinogenic 3′ ssDNA substrate and enables RecA loading in a Chi-regulated manner. (amundsen2023recbcdenzymemechanistic pages 4-6, sinha2020therolesof pages 2-3, pavankumar2024transcomplementationbythe pages 1-2)
2. **Biological processes:** DSB repair by homologous recombination and replication-fork rescue are core processes supported by RecBCD/RecB. (sinha2020therolesof pages 2-3, amundsen2023recbcdenzymemechanistic pages 4-6)
3. **Cellular location:** Cytoplasm/nucleoid-associated DNA repair context (functional inference from substrate and pathway). (sinha2020therolesof pages 2-3, amundsen2023recbcdenzymemechanistic pages 4-6)
4. **Organism-specific caution for KT2440:** Chi sequence(s) and relative importance of nuclease vs motor functions may differ across pseudomonads; direct KT2440 recB mutant phenotypes were not recovered in the retrieved corpus, so KT2440-specific statements should be treated as **inferred from conserved RecBCD biology** plus limited KT2440 DNA-damage pathway context. (pavankumar2018biochemicalcharacterizationof pages 1-2, martinez‐garcia2015freeingpseudomonasputida pages 7-10)

## References (URLs and publication dates)
- Amundsen SK, Smith GR. **RecBCD enzyme: mechanistic insights from mutants of a complex helicase-nuclease**. *Microbiology and Molecular Biology Reviews*. **2023-12-20**. https://doi.org/10.1128/mmbr.00041-23 (amundsen2023recbcdenzymemechanistic pages 4-6)
- Pavankumar TL, Wong CJ, Wong YK, Spies M, Kowalczykowski SC. **Trans-complementation by the RecB nuclease domain of RecBCD enzyme reveals new insight into RecA loading upon χ recognition**. *Nucleic Acids Research*. **2024-01-16**. https://doi.org/10.1093/nar/gkae007 (pavankumar2024transcomplementationbythe pages 1-2)
- Sinha AK, Possoz C, Leach DRF. **The roles of bacterial DNA double-strand break repair proteins in chromosomal DNA replication**. *FEMS Microbiology Reviews*. **2020-04-01**. https://doi.org/10.1093/femsre/fuaa009 (sinha2020therolesof pages 2-3)
- Smith GR. **How RecBCD Enzyme and Chi Promote DNA Break Repair and Recombination: a Molecular Biologist's View**. *Microbiology and Molecular Biology Reviews*. **2012-06-01**. https://doi.org/10.1128/mmbr.05026-11 (smith2012howrecbcdenzyme pages 2-4)
- Pavankumar TL, Sinha AK, Ray MK. **All Three Subunits of RecBCD Enzyme Are Essential for DNA Repair and Low-Temperature Growth in the Antarctic Pseudomonas syringae Lz4W**. *PLOS ONE*. **2010-02-17**. https://doi.org/10.1371/journal.pone.0009412 (pavankumar2010allthreesubunits pages 1-2)
- Pavankumar TL, Sinha AK, Ray MK. **Biochemical characterization of RecBCD enzyme from an Antarctic Pseudomonas species and identification of its cognate Chi (χ) sequence**. *PLOS ONE*. **2018-05-16**. https://doi.org/10.1371/journal.pone.0197476 (pavankumar2018biochemicalcharacterizationof pages 1-2)
- Martínez-García E, Jatsenko T, Kivisaar M, de Lorenzo V. **Freeing Pseudomonas putida KT2440 of its proviral load strengthens endurance to environmental stresses**. *Environmental Microbiology*. **2015-06-01**. https://doi.org/10.1111/1462-2920.12492 (martinez‐garcia2015freeingpseudomonasputida pages 7-10)
- Chai R, Zhang Q, Wu J, et al. **Single-Stranded DNA-Binding Proteins Mediate DSB Repair and Effectively Improve CRISPR/Cas9 Genome Editing in Escherichia coli and Pseudomonas**. *Microorganisms*. **2023-03-30**. https://doi.org/10.3390/microorganisms11040850 (pavankumar2018biochemicalcharacterizationof pages 1-2)
- Vincent MS, Uphoff S. **Bacterial phenotypic heterogeneity in DNA repair and mutagenesis**. *Biochemical Society Transactions*. **2020-03-23**. https://doi.org/10.1042/bst20190364 (vincent2020bacterialphenotypicheterogeneity pages 2-4)
- Kalita I, Iosub IA, McLaren L, et al. **An Hfq-dependent post-transcriptional mechanism fine tunes RecB expression in Escherichia coli**. *eLife*. **2025-08-21**. https://doi.org/10.7554/elife.94918 (kalita2025anhfqdependentposttranscriptional pages 2-3)

References

1. (amundsen2023recbcdenzymemechanistic pages 1-2): Susan K. Amundsen and Gerald R. Smith. Recbcd enzyme: mechanistic insights from mutants of a complex helicase-nuclease. Microbiology and Molecular Biology Reviews, Dec 2023. URL: https://doi.org/10.1128/mmbr.00041-23, doi:10.1128/mmbr.00041-23. This article has 23 citations and is from a domain leading peer-reviewed journal.

2. (amundsen2023recbcdenzymemechanistic pages 4-6): Susan K. Amundsen and Gerald R. Smith. Recbcd enzyme: mechanistic insights from mutants of a complex helicase-nuclease. Microbiology and Molecular Biology Reviews, Dec 2023. URL: https://doi.org/10.1128/mmbr.00041-23, doi:10.1128/mmbr.00041-23. This article has 23 citations and is from a domain leading peer-reviewed journal.

3. (amundsen2023recbcdenzymemechanistic pages 2-4): Susan K. Amundsen and Gerald R. Smith. Recbcd enzyme: mechanistic insights from mutants of a complex helicase-nuclease. Microbiology and Molecular Biology Reviews, Dec 2023. URL: https://doi.org/10.1128/mmbr.00041-23, doi:10.1128/mmbr.00041-23. This article has 23 citations and is from a domain leading peer-reviewed journal.

4. (smith2012howrecbcdenzyme pages 2-4): Gerald R. Smith. How recbcd enzyme and chi promote dna break repair and recombination: a molecular biologist's view. Microbiology and Molecular Biology Reviews, 76:217-228, Jun 2012. URL: https://doi.org/10.1128/mmbr.05026-11, doi:10.1128/mmbr.05026-11. This article has 219 citations and is from a domain leading peer-reviewed journal.

5. (pavankumar2018biochemicalcharacterizationof pages 1-2): Theetha L. Pavankumar, Anurag K. Sinha, and Malay K. Ray. Biochemical characterization of recbcd enzyme from an antarctic pseudomonas species and identification of its cognate chi (χ) sequence. PLOS ONE, 13:e0197476, May 2018. URL: https://doi.org/10.1371/journal.pone.0197476, doi:10.1371/journal.pone.0197476. This article has 15 citations and is from a peer-reviewed journal.

6. (pavankumar2024transcomplementationbythe pages 1-2): Theetha L Pavankumar, C Jason Wong, Yun Ka Wong, Maria Spies, and Stephen C Kowalczykowski. Trans-complementation by the recb nuclease domain of recbcd enzyme reveals new insight into reca loading upon χ recognition. Nucleic Acids Research, 52:2578-2589, Jan 2024. URL: https://doi.org/10.1093/nar/gkae007, doi:10.1093/nar/gkae007. This article has 10 citations and is from a highest quality peer-reviewed journal.

7. (sinha2020therolesof pages 2-3): Anurag Kumar Sinha, Christophe Possoz, and David R F Leach. The roles of bacterial dna double-strand break repair proteins in chromosomal dna replication. FEMS Microbiology Reviews, 44:351-368, Apr 2020. URL: https://doi.org/10.1093/femsre/fuaa009, doi:10.1093/femsre/fuaa009. This article has 46 citations and is from a domain leading peer-reviewed journal.

8. (pavankumar2010allthreesubunits pages 1-2): Theetha L. Pavankumar, Anurag K. Sinha, and Malay K. Ray. All three subunits of recbcd enzyme are essential for dna repair and low-temperature growth in the antarctic pseudomonas syringae lz4w. PLoS ONE, 5:e9412, Feb 2010. URL: https://doi.org/10.1371/journal.pone.0009412, doi:10.1371/journal.pone.0009412. This article has 31 citations and is from a peer-reviewed journal.

9. (pavankumar2010allthreesubunits pages 4-7): Theetha L. Pavankumar, Anurag K. Sinha, and Malay K. Ray. All three subunits of recbcd enzyme are essential for dna repair and low-temperature growth in the antarctic pseudomonas syringae lz4w. PLoS ONE, 5:e9412, Feb 2010. URL: https://doi.org/10.1371/journal.pone.0009412, doi:10.1371/journal.pone.0009412. This article has 31 citations and is from a peer-reviewed journal.

10. (pavankumar2010allthreesubunits pages 7-8): Theetha L. Pavankumar, Anurag K. Sinha, and Malay K. Ray. All three subunits of recbcd enzyme are essential for dna repair and low-temperature growth in the antarctic pseudomonas syringae lz4w. PLoS ONE, 5:e9412, Feb 2010. URL: https://doi.org/10.1371/journal.pone.0009412, doi:10.1371/journal.pone.0009412. This article has 31 citations and is from a peer-reviewed journal.

11. (martinez‐garcia2015freeingpseudomonasputida pages 7-10): Esteban Martínez‐García, Tatjana Jatsenko, Maia Kivisaar, and Víctor de Lorenzo. Freeing pseudomonas putida kt2440 of its proviral load strengthens endurance to environmental stresses. Environmental microbiology, 17 1:76-90, Jun 2015. URL: https://doi.org/10.1111/1462-2920.12492, doi:10.1111/1462-2920.12492. This article has 94 citations and is from a domain leading peer-reviewed journal.

12. (martinez‐garcia2015freeingpseudomonasputida pages 10-12): Esteban Martínez‐García, Tatjana Jatsenko, Maia Kivisaar, and Víctor de Lorenzo. Freeing pseudomonas putida kt2440 of its proviral load strengthens endurance to environmental stresses. Environmental microbiology, 17 1:76-90, Jun 2015. URL: https://doi.org/10.1111/1462-2920.12492, doi:10.1111/1462-2920.12492. This article has 94 citations and is from a domain leading peer-reviewed journal.

13. (pavankumar2010allthreesubunits pages 8-9): Theetha L. Pavankumar, Anurag K. Sinha, and Malay K. Ray. All three subunits of recbcd enzyme are essential for dna repair and low-temperature growth in the antarctic pseudomonas syringae lz4w. PLoS ONE, 5:e9412, Feb 2010. URL: https://doi.org/10.1371/journal.pone.0009412, doi:10.1371/journal.pone.0009412. This article has 31 citations and is from a peer-reviewed journal.

14. (vincent2020bacterialphenotypicheterogeneity pages 2-4): Maxence S. Vincent and Stephan Uphoff. Bacterial phenotypic heterogeneity in dna repair and mutagenesis. Biochemical Society Transactions, 48:451-462, Mar 2020. URL: https://doi.org/10.1042/bst20190364, doi:10.1042/bst20190364. This article has 43 citations and is from a peer-reviewed journal.

15. (kalita2025anhfqdependentposttranscriptional pages 2-3): Irina Kalita, Ira Alexandra Iosub, Lorna McLaren, Louise Goossens, Sander Granneman, and Meriem El Karoui. An hfq-dependent post-transcriptional mechanism fine tunes recb expression in escherichia coli. eLife, Aug 2025. URL: https://doi.org/10.7554/elife.94918, doi:10.7554/elife.94918. This article has 6 citations and is from a domain leading peer-reviewed journal.

16. (amundsen2023recbcdenzymemechanistic pages 8-11): Susan K. Amundsen and Gerald R. Smith. Recbcd enzyme: mechanistic insights from mutants of a complex helicase-nuclease. Microbiology and Molecular Biology Reviews, Dec 2023. URL: https://doi.org/10.1128/mmbr.00041-23, doi:10.1128/mmbr.00041-23. This article has 23 citations and is from a domain leading peer-reviewed journal.

17. (pavankumar2010allthreesubunits pages 10-13): Theetha L. Pavankumar, Anurag K. Sinha, and Malay K. Ray. All three subunits of recbcd enzyme are essential for dna repair and low-temperature growth in the antarctic pseudomonas syringae lz4w. PLoS ONE, 5:e9412, Feb 2010. URL: https://doi.org/10.1371/journal.pone.0009412, doi:10.1371/journal.pone.0009412. This article has 31 citations and is from a peer-reviewed journal.

18. (martinez‐garcia2015freeingpseudomonasputida pages 12-15): Esteban Martínez‐García, Tatjana Jatsenko, Maia Kivisaar, and Víctor de Lorenzo. Freeing pseudomonas putida kt2440 of its proviral load strengthens endurance to environmental stresses. Environmental microbiology, 17 1:76-90, Jun 2015. URL: https://doi.org/10.1111/1462-2920.12492, doi:10.1111/1462-2920.12492. This article has 94 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](recB-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. amundsen2023recbcdenzymemechanistic pages 1-2
2. amundsen2023recbcdenzymemechanistic pages 4-6
3. amundsen2023recbcdenzymemechanistic pages 2-4
4. pavankumar2018biochemicalcharacterizationof pages 1-2
5. pavankumar2024transcomplementationbythe pages 1-2
6. sinha2020therolesof pages 2-3
7. pavankumar2010allthreesubunits pages 7-8
8. pavankumar2010allthreesubunits pages 1-2
9. smith2012howrecbcdenzyme pages 2-4
10. vincent2020bacterialphenotypicheterogeneity pages 2-4
11. kalita2025anhfqdependentposttranscriptional pages 2-3
12. pavankumar2010allthreesubunits pages 4-7
13. pavankumar2010allthreesubunits pages 8-9
14. amundsen2023recbcdenzymemechanistic pages 8-11
15. pavankumar2010allthreesubunits pages 10-13
16. https://doi.org/10.1128/mmbr.00041-23
17. https://doi.org/10.1128/mmbr.00041-23;
18. https://doi.org/10.1128/mmbr.05026-11
19. https://doi.org/10.1371/journal.pone.0197476
20. https://doi.org/10.1093/nar/gkae007
21. https://doi.org/10.1093/femsre/fuaa009
22. https://doi.org/10.1371/journal.pone.0009412
23. https://doi.org/10.1111/1462-2920.12492
24. https://doi.org/10.3390/microorganisms11040850
25. https://doi.org/10.1128/mmbr.05026-11;
26. https://doi.org/10.1093/femsre/fuaa009;
27. https://doi.org/10.1042/bst20190364;
28. https://doi.org/10.7554/elife.94918
29. https://doi.org/10.1042/bst20190364
30. https://doi.org/10.1128/mmbr.00041-23,
31. https://doi.org/10.1128/mmbr.05026-11,
32. https://doi.org/10.1371/journal.pone.0197476,
33. https://doi.org/10.1093/nar/gkae007,
34. https://doi.org/10.1093/femsre/fuaa009,
35. https://doi.org/10.1371/journal.pone.0009412,
36. https://doi.org/10.1111/1462-2920.12492,
37. https://doi.org/10.1042/bst20190364,
38. https://doi.org/10.7554/elife.94918,