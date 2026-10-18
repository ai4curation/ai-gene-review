---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-25T01:05:54.679049'
end_time: '2026-09-25T01:11:55.219625'
duration_seconds: 360.54
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: PLK1
  gene_symbol: PLK1
  uniprot_accession: P53350
  protein_description: 'RecName: Full=Serine/threonine-protein kinase PLK1; EC=2.7.11.21
    {ECO:0000269|PubMed:11202906, ECO:0000269|PubMed:12207013, ECO:0000269|PubMed:21880710,
    ECO:0000269|PubMed:28512243, ECO:0000269|PubMed:37440612, ECO:0000269|PubMed:37674080};
    AltName: Full=Polo-like kinase 1; Short=PLK-1; AltName: Full=Serine/threonine-protein
    kinase 13; Short=STPK13;'
  gene_info: Name=PLK1; Synonyms=PLK;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the protein kinase superfamily. Ser/Thr protein
  protein_domains: Kinase-like_dom_sf. (IPR011009); PLK1_cat. (IPR033702); POLO_box_1.
    (IPR033701); POLO_box_2. (IPR033695); POLO_box_dom. (IPR000959)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: PLK1-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** P53350
- **Protein Description:** RecName: Full=Serine/threonine-protein kinase PLK1; EC=2.7.11.21 {ECO:0000269|PubMed:11202906, ECO:0000269|PubMed:12207013, ECO:0000269|PubMed:21880710, ECO:0000269|PubMed:28512243, ECO:0000269|PubMed:37440612, ECO:0000269|PubMed:37674080}; AltName: Full=Polo-like kinase 1; Short=PLK-1; AltName: Full=Serine/threonine-protein kinase 13; Short=STPK13;
- **Gene Information:** Name=PLK1; Synonyms=PLK;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the protein kinase superfamily. Ser/Thr protein
- **Key Domains:** Kinase-like_dom_sf. (IPR011009); PLK1_cat. (IPR033702); POLO_box_1. (IPR033701); POLO_box_2. (IPR033695); POLO_box_dom. (IPR000959)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PLK1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PLK1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PLK1** (gene ID: PLK1, UniProt: P53350) in human.

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
- **UniProt Accession:** P53350
- **Protein Description:** RecName: Full=Serine/threonine-protein kinase PLK1; EC=2.7.11.21 {ECO:0000269|PubMed:11202906, ECO:0000269|PubMed:12207013, ECO:0000269|PubMed:21880710, ECO:0000269|PubMed:28512243, ECO:0000269|PubMed:37440612, ECO:0000269|PubMed:37674080}; AltName: Full=Polo-like kinase 1; Short=PLK-1; AltName: Full=Serine/threonine-protein kinase 13; Short=STPK13;
- **Gene Information:** Name=PLK1; Synonyms=PLK;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the protein kinase superfamily. Ser/Thr protein
- **Key Domains:** Kinase-like_dom_sf. (IPR011009); PLK1_cat. (IPR033702); POLO_box_1. (IPR033701); POLO_box_2. (IPR033695); POLO_box_dom. (IPR000959)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PLK1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PLK1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PLK1** (gene ID: PLK1, UniProt: P53350) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Human PLK1 (UniProt P53350): Functional-Annotation Research Report

## Executive summary

The requested target is unambiguous: **PLK1**, encoding human polo-like kinase 1 (**Homo sapiens**, UniProt **P53350**), not the similarly named PLK1-interacting protein **MPLKIP** or a non-human Polo-family ortholog. The supplied identity, enzyme class, and domains agree with the literature: PLK1 is a 603-residue, ATP-dependent serine/threonine protein kinase comprising an N-terminal catalytic domain and a C-terminal phosphopeptide-binding polo-box domain (PBD). Its principal biological function is to impose spatial and temporal order on the G2/M transition, centrosome maturation, spindle formation, kinetochore behavior, chromosome segregation, mitotic exit, and cytokinesis. The kinase domain phosphorylates protein Ser/Thr residues, while the tandem polo boxes recruit and regulate PLK1 through phosphodependent interactions with primed substrates and scaffold proteins. (wyatt2024insightsintothe pages 3-7, wyatt2024insightsintothe pages 1-3)

PLK1 is activated in G2 principally through Aurora-A–BORA-dependent phosphorylation of Thr210 and then moves through a characteristic sequence of locations—centrosomes, kinetochores and spindle, spindle midzone, and finally the cytokinetic bridge/midbody. It drives the CDK1–cyclin-B mitotic switch by activating CDC25C and antagonizing WEE1 and PKMYT1, while acting on numerous centrosomal, kinetochore, spindle, checkpoint, and cytokinetic proteins. Consequently, loss or acute inhibition produces failed bipolar-spindle formation, chromosome-alignment defects, spindle-checkpoint activation, mitotic arrest, chromosome mis-segregation, or cell death. (milletti2023cyclers’kinasesin pages 9-10, athwal2024centrosomesandassociated pages 3-4, cheng2024discoveryofinhibitors pages 45-49)

## 1. Mandatory identity verification

**Gene-symbol match.** The literature consistently identifies human **PLK1** as “polo-like kinase 1,” a serine/threonine kinase and major mitotic regulator. This matches the provided UniProt recommended name, accession P53350, synonyms PLK/PLK-1/STPK13, and EC 2.7.11.21. No evidence indicated that the requested symbol should be reassigned to another protein. Open Targets separately distinguishes PLK1 (ENSG00000166851; approved name “polo like kinase 1”) from **MPLKIP**, confirming that these are different human genes. (OpenTargets Search: -PLK1)

**Organism.** The target assessed here is **Homo sapiens** PLK1. Evidence from other organisms is useful for evolutionary or structural inference but is not treated as establishing human-specific function unless conserved human data support it.

**Family and domain agreement.** A 2024 structural analysis divides full-length PLK1 into residues 1–38, a kinase domain at 39–325, an interdomain linker at 326–364, and the C-terminal PBD at 365–603. This is fully consistent with the supplied protein-kinase, PLK1 catalytic, polo-box-1, polo-box-2, and composite polo-box annotations. The PBD contains tandem polo boxes rather than a second catalytic domain. (wyatt2024insightsintothe pages 3-7)

| Topic | Mechanistic annotation/evidence | Key quantitative or spatial detail | Source/date/URL |
|---|---|---|---|
| Identity and domain architecture | Human **PLK1** is a serine/threonine protein kinase whose N-terminal catalytic domain is coupled to a C-terminal polo-box domain (PBD) that mediates phosphopeptide recognition, localization, and autoinhibition. This matches **UniProt P53350** and the supplied tandem polo-box annotations. | **603 aa**: N-terminus 1–38; kinase domain 39–325; interdomain linker 326–364; PBD 365–603. | Wyatt & McInnes, **21 Oct 2024**, bioRxiv preprint, [DOI](https://doi.org/10.1101/2024.10.21.618045) (wyatt2024insightsintothe pages 3-7, wyatt2024insightsintothe pages 1-3) |
| Catalytic reaction and substrate recognition | Catalyzes ATP-dependent transfer of the γ-phosphate to protein serine/threonine residues: **ATP + protein-OH → ADP + protein-O-phosphate**. Catalytic-site sequence preference and PBD docking operate together; the PBD recognizes pre-existing phosphoserine/phosphothreonine motifs, concentrating the kinase at appropriate substrates. The gathered excerpts do not justify one universal sequence consensus for all substrates. | PBD-mediated docking is phosphodependent; linker-2 residues **490–502** contact substrate residues C-terminal to phosphothreonine. | Wyatt & McInnes, **21 Oct 2024**, bioRxiv preprint, [DOI](https://doi.org/10.1101/2024.10.21.618045) (wyatt2024insightsintothe pages 1-3, wyatt2024insightsintothe pages 7-8) |
| Activation and regulation | In G2, **Aurora A–BORA** phosphorylates PLK1 at **Thr210**; BORA promotes conformational exposure of Thr210, dimerization, and nuclear localization. The PBD–kinase interaction supports a closed autoinhibited state before activating phosphorylation or partner binding. | Activating site: **T210**; **S137** is also reported as regulatory, but its timing/function remain unresolved. Disrupting the nuclear-localization signal causes G2 arrest. | Milletti et al., **July 2023**, peer-reviewed, [DOI](https://doi.org/10.1038/s41418-023-01196-z); Wyatt & McInnes, **21 Oct 2024**, preprint, [DOI](https://doi.org/10.1101/2024.10.21.618045) (milletti2023cyclers’kinasesin pages 9-10, wyatt2024insightsintothe pages 7-8) |
| Localization and core functions | PLK1 is recruited to G2/M centrosomes by **CEP192**, supports pericentriolar-material expansion, centrosome maturation/separation, bipolar-spindle assembly, and mitotic entry. It subsequently occupies kinetochores and spindle structures, then relocates to the spindle midzone and cytokinetic bridge/midbody to coordinate chromosome segregation and cytokinesis. | Spatial progression: cytoplasm/centrosomes → spindle and kinetochores → spindle midzone → cytokinetic bridge/midbody. | Athwal et al., **March 2024**, peer-reviewed, [DOI](https://doi.org/10.3389/fonc.2024.1370565); Cheng, **January 2024**, thesis/research text, [DOI](https://doi.org/10.25916/sut.26281879) (athwal2024centrosomesandassociated pages 7-8, cheng2024discoveryofinhibitors pages 45-49) |
| Representative substrates and effectors | PLK1 promotes CDK1–cyclin-B activation by stimulating **CDC25C**, promoting **WEE1** degradation, and inhibiting **PKMYT1/MYT1**; it phosphorylates cyclin B and CDC25C to facilitate nuclear entry. Centrosomal/mitotic effectors include **NLP**, survivin, NEK2, and AURKA localization. **TCTP-S46 phosphorylation** is used experimentally as a PLK1-activity readout. | These reactions connect PLK1 activation to the G2/M switch, centrosome separation, spindle assembly, and Aurora-B-associated mitotic signaling. | Milletti et al., **July 2023**, peer-reviewed, [DOI](https://doi.org/10.1038/s41418-023-01196-z); Athwal et al., **March 2024**, peer-reviewed, [DOI](https://doi.org/10.3389/fonc.2024.1370565) (milletti2023cyclers’kinasesin pages 9-10, black2024chk2sustainsplk1 pages 5-9, athwal2024centrosomesandassociated pages 3-4) |
| Chk2-dependent maintenance of PLK1 activity | A 2024 study found that Chk2 inhibition or loss reduced mitotic PLK1 output across cancerous and noncancerous cells; biochemical controls indicated that the effect was indirect rather than direct inhibition of isolated PLK1 or Aurora A. | Chk2-deficient A549 cells showed approximately **30% less p-TCTP**. A PLK1 FRET sensor decreased approximately **7%** after Chk2 inhibition versus approximately **30%** after direct PLK1 inhibition over 1 hour. | Black et al., **March 2024**, bioRxiv preprint, [DOI](https://doi.org/10.1101/2024.03.08.584115) (black2024chk2sustainsplk1 pages 5-9) |
| Cancer relevance | PLK1 overexpression is reported in several malignancies and is associated with high proliferation, chromosome-segregation defects, genomic instability, aggressive behavior, treatment resistance, and poor prognosis. These associations and inhibitor phenotypes support PLK1 as an oncology target, but do not by themselves establish it as a tumor-initiating driver or validated predictive biomarker. | Reported across breast, liver, colorectal, lung-squamous, prostate, gastric, ovarian, and other cancers; inhibition can cause spindle failure, spindle-checkpoint activation, mitotic arrest, and apoptosis. | Milletti et al., **July 2023**, peer-reviewed, [DOI](https://doi.org/10.1038/s41418-023-01196-z); Athwal et al., **March 2024**, peer-reviewed, [DOI](https://doi.org/10.3389/fonc.2024.1370565) (milletti2023cyclers’kinasesin pages 16-17, athwal2024centrosomesandassociated pages 3-4, cheng2024discoveryofinhibitors pages 45-49) |
| Inhibitor potency and development | ATP-competitive inhibitors demonstrate high biochemical potency, but PLK1's essential role in dividing normal cells constrains therapeutic selectivity. **BI 2536** and **volasertib** reached clinical testing; the evidence gathered supports development status and potency, not routine clinical use or definitive response benefit. | BI 2536 IC50: **0.83 nM** for PLK1, 3.5 nM for PLK2, 9.0 nM for PLK3; volasertib PLK1 IC50: **0.87 nM**. BI 2536 reached Phase II; volasertib was tested in Phase II AML. | Athwal et al., **March 2024**, peer-reviewed, [DOI](https://doi.org/10.3389/fonc.2024.1370565) (athwal2024centrosomesandassociated pages 7-8) |
| Onvansertib–alpelisib combination | In PIK3CA-mutant HR-positive breast-cancer models resistant to endocrine therapy and palbociclib, onvansertib plus alpelisib synergistically reduced viability, suppressed PI3K signaling, induced G2/M arrest and apoptosis, and outperformed either monotherapy in vivo. This is **preclinical**, not evidence of patient benefit. | Tested in **three** resistant PIK3CA-mutant patient-derived xenograft models. Approximately **40%** of HR-positive breast cancers harbor PIK3CA alterations. | Sreekumar et al., **September 2024**, peer-reviewed, [DOI](https://doi.org/10.3390/cancers16193259) (sreekumar2024plk1inhibitoronvansertib pages 1-2) |


*Table: Concise evidence map linking human PLK1 identity, enzymology, spatial mitotic functions, representative effectors, recent mechanistic findings, and therapeutic development. Preclinical, preprint, and peer-reviewed evidence are explicitly distinguished.*

## 2. Primary molecular function and reaction

PLK1 is a protein serine/threonine kinase. Its net reaction is:

**ATP + protein–Ser/Thr–OH → ADP + protein–Ser/Thr–O-phosphate.**

Thus, the physiological substrates are proteins rather than small metabolites. Specificity is combinatorial rather than being determined by one short linear sequence alone: the catalytic cleft favors appropriate local sequences around an acceptor Ser/Thr, while the C-terminal PBD binds phosphoserine/phosphothreonine-containing docking motifs on previously “primed” proteins. This couples catalysis to localization and lets PLK1 phosphorylate nearby sites on recruited substrates. The available evidence supports phosphodependent targeting but does **not** justify treating one consensus motif as universally predictive of every cellular PLK1 substrate. (black2024chk2sustainsplk1 pages 38-40, wyatt2024insightsintothe pages 1-3)

Structural work further indicates that the PBD regulates the catalytic domain. AlphaFold modeling, supported by a kinase-domain/PBD structure, places full-length PLK1 in a closed autoinhibited state. Linker-2 residues 490–502 change conformation between closed and phosphopeptide-bound states and contact residues C-terminal to a substrate phosphothreonine. In the predicted closed state, an extensive hydrophobic interface—especially involving PBD residue L505—stabilizes kinase–PBD association. These findings provide a structural explanation for how phosphopeptide binding and activating modifications can coordinate opening, localization, and catalysis, although the 2024 analysis is a preprint and parts of the full-length model remain inferential. (wyatt2024insightsintothe pages 3-7, wyatt2024insightsintothe pages 7-8)

## 3. Activation and cell-cycle control

PLK1 abundance and activity increase toward G2/M. In G2, BORA promotes a PLK1 conformation that exposes activation-loop **Thr210** to Aurora A; Thr210 phosphorylation is the principal activating event. BORA also supports dimerization and nuclear localization. Ser137 is another reported regulatory phosphorylation site, but its timing and functional importance remain unsettled. Disrupting the PLK1 nuclear-localization sequence causes G2 arrest, demonstrating that nuclear entry is functionally important for mitotic commitment. (milletti2023cyclers’kinasesin pages 9-10)

Activated PLK1 reinforces the bistable mitotic-entry network. It activates CDC25C and promotes its nuclear localization, thereby removing inhibitory phosphates from CDK1; it promotes WEE1 destruction and inhibits PKMYT1/MYT1, reducing the opposing phosphorylation of CDK1; and it phosphorylates cyclin B to support nuclear accumulation of the CDK1–cyclin-B complex. PLK1 is therefore not merely a downstream marker of mitosis—it is a feed-forward amplifier that helps convert a gradual G2 signal into decisive CDK1 activation. (milletti2023cyclers’kinasesin pages 16-17, milletti2023cyclers’kinasesin pages 9-10)

## 4. Subcellular localization and spatial function

PLK1 is predominantly an intracellular, dynamically localized enzyme:

- **G2/prophase—centrosomes:** CEP192 recruits PLK1 to centrosomes, where it expands pericentriolar material and coordinates centrosome maturation and separation with Aurora A, NEK2, CEP250, NLP and other centrosomal factors. These events establish competent bipolar spindle poles. (athwal2024centrosomesandassociated pages 7-8, athwal2024centrosomesandassociated pages 3-4)
- **Prometaphase/metaphase—kinetochores and spindle:** PLK1 supports kinetochore assembly and signaling, chromosome congression, kinetochore–microtubule attachment, spindle-checkpoint control, and protection of centromere/kinetochore architecture. (black2024chk2sustainsplk1 pages 38-40)
- **Anaphase—spindle midzone:** PLK1 relocates as cells leave metaphase and helps establish the central spindle and cleavage-plane machinery. (cheng2024discoveryofinhibitors pages 45-49)
- **Telophase/cytokinesis—cytokinetic bridge and midbody:** PLK1 coordinates late cytokinetic events and must itself be downregulated appropriately for successful abscission and mitotic exit. (wyatt2024insightsintothe pages 1-3, cheng2024discoveryofinhibitors pages 45-49)

This spatial itinerary explains why the PBD is indispensable: it repeatedly retargets the same catalytic module to different phosphorylated scaffolds as mitosis progresses.

## 5. Representative substrates and pathways

PLK1 has many substrates, but the most informative functional groups are:

1. **Mitotic-entry network:** CDC25C, cyclin B, WEE1 and PKMYT1/MYT1 connect PLK1 to CDK1 activation and nuclear mitotic entry. (milletti2023cyclers’kinasesin pages 9-10)
2. **Centrosome and spindle machinery:** PLK1 regulates NEK2 activity and Aurora-A localization and phosphorylates NLP, promoting its mitotic release from centrosomes. These events contribute to centrosome separation, pericentriolar-material remodeling and spindle assembly. (athwal2024centrosomesandassociated pages 3-4)
3. **Chromosome/kinetochore and checkpoint machinery:** phosphodependent PBD recruitment through proteins such as PBIP1, together with regulation of MPS1, MYPT1 and kinetochore phosphatases, positions PLK1 within the network controlling attachment, congression and spindle-checkpoint behavior. (black2024chk2sustainsplk1 pages 38-40)
4. **TCTP:** phosphorylation at TCTP Ser46 is widely used as a cellular PLK1-output marker. It is especially useful experimentally because changes in p-TCTP can be compared with Thr210 phosphorylation or PLK1 FRET sensors. (black2024chk2sustainsplk1 pages 5-9)
5. **Survivin/Aurora-B-linked signaling:** PLK1-dependent survivin phosphorylation has been connected to Aurora-B activation and mitotic progression, although this is one element of a broader chromosome-passenger network rather than the sole mechanism controlling Aurora B. (athwal2024centrosomesandassociated pages 3-4)

PLK1 also participates in DNA-damage recovery and repair signaling. This should be interpreted as an extension of its cell-cycle function: PLK1 helps determine whether a G2-arrested cell remains checkpoint-arrested or re-enters mitosis, rather than acting as a conventional DNA-repair enzyme. (black2024chk2sustainsplk1 pages 38-40)

## 6. Recent developments, 2023–2024

### Structural regulation

The October 21, 2024 AlphaFold analysis proposed a residue-level closed full-length conformation, identified linker and PBD contacts stabilizing autoinhibition, and suggested how phosphopeptide binding could favor an open state. This advances mechanistic understanding but remains preprint evidence requiring direct full-length structural and mutational validation. URL: https://doi.org/10.1101/2024.10.21.618045. (wyatt2024insightsintothe pages 3-7, wyatt2024insightsintothe pages 7-8)

### Chk2 sustains mitotic PLK1 output

A March 2024 preprint found that inhibiting or deleting Chk2 reduced mitotic PLK1 activity in cancerous and noncancerous cells without directly inhibiting isolated PLK1 or Aurora A. Chk2-deficient A549 cells exhibited approximately **30% less phospho-TCTP** than wild-type cells. Over one hour, a PLK1 FRET sensor decreased by approximately **7%** after Chk2 inhibition, compared with approximately **30%** after direct PLK1 inhibition. These data imply that Chk2 indirectly sustains maximal mitotic PLK1 activity and chromosome-segregation fidelity, although the pathway between Chk2 and PLK1 was not fully resolved. Posted March 12, 2024; URL: https://doi.org/10.1101/2024.03.08.584115. (black2024chk2sustainsplk1 pages 5-9)

### Centrosomes and chromosomal instability

A March 2024 review emphasized PLK1’s recruitment by CEP192, cooperation with Aurora A and NEK2, and relationship to centrosome amplification and chromosomal instability in breast cancer. The authoritative interpretation is that PLK1 dysregulation can amplify mitotic errors and tumor evolution, but expression correlations alone do not show that PLK1 overexpression initiated a given tumor. URL: https://doi.org/10.3389/fonc.2024.1370565. (athwal2024centrosomesandassociated pages 3-4, athwal2024centrosomesandassociated pages 7-8)

### Combination therapy in resistant breast cancer

In September 2024, onvansertib plus the PI3Kα inhibitor alpelisib synergistically reduced viability, suppressed PI3K signaling, induced G2/M arrest and apoptosis, and outperformed either single agent in **three** PIK3CA-mutant HR-positive breast-cancer patient-derived xenograft models resistant to endocrine therapy and palbociclib. Approximately **40%** of HR-positive breast cancers harbor PIK3CA alterations, making the proposed combination biologically relevant. This remains preclinical evidence; it does not establish clinical efficacy. URL: https://doi.org/10.3390/cancers16193259. (sreekumar2024plk1inhibitoronvansertib pages 1-2)

## 7. Disease relevance and applications

PLK1 is frequently overexpressed in proliferative malignancies, including breast, colorectal, liver, lung-squamous, prostate, gastric and ovarian cancers. High expression is commonly associated with proliferation, chromosome-segregation defects, genomic instability, aggressiveness, treatment resistance and poor prognosis. Mechanistically, tumors may become unusually dependent on PLK1 because they must divide despite centrosome amplification, replication stress, DNA damage and weakened checkpoints. Nevertheless, PLK1 is also essential in normal proliferating tissues; it is better regarded as a context-dependent cancer dependency than as a universally tumor-specific driver. (milletti2023cyclers’kinasesin pages 16-17, athwal2024centrosomesandassociated pages 3-4, cheng2024discoveryofinhibitors pages 45-49)

The principal current application is **drug development**. ATP-competitive inhibitors include BI 2536, volasertib and onvansertib; alternative strategies seek greater selectivity through PBD/allosteric inhibition, targeted degradation, tumor-selective delivery, rational combinations, and biomarkers of PLK1 dependency. BI 2536 has reported biochemical IC50 values of **0.83 nM for PLK1**, 3.5 nM for PLK2 and 9.0 nM for PLK3; volasertib inhibits PLK1 at approximately **0.87 nM**. BI 2536 reached Phase II testing and volasertib underwent Phase II AML evaluation. These potencies demonstrate target engagement, not therapeutic index or patient benefit. (athwal2024centrosomesandassociated pages 7-8)

Clinical development remains investigational. Retrieved registry records show onvansertib studies in small-cell lung cancer, triple-negative breast cancer, RAS-mutant metastatic colorectal cancer, pancreatic cancer, prostate cancer, AML, and CMML/MDS–MPN overlap disease, spanning Phase I and Phase II programs. Examples include a 68-participant Phase I/II KRAS-mutant metastatic-colorectal-cancer study, a 110-participant randomized Phase II first-line RAS-mutant colorectal-cancer study, a 50-participant Phase I/II TNBC study, and a 37-participant Phase II small-cell-lung-cancer study. Registry status demonstrates implementation in patients but should not be confused with regulatory approval or proven efficacy.

The major translational obstacle, emphasized by recent experts, is the narrow biological separation between malignant and normal dividing cells. On-target suppression can damage bone marrow and other proliferative tissues, while mitotic arrest can end in apoptosis, slippage, polyploidy, or survival depending on cellular context. Biomarker-based selection and combination dosing may therefore be more promising than unselected PLK1-inhibitor monotherapy. (milletti2023cyclers’kinasesin pages 16-17, athwal2024centrosomesandassociated pages 7-8)

## 8. Evidence-based functional annotation

**Recommended concise annotation:** Human PLK1 is a dynamically localized, cell-cycle-regulated Ser/Thr kinase that uses an N-terminal catalytic domain and C-terminal tandem polo-box phosphopeptide-binding module to phosphorylate spatially recruited substrates. Activated principally by Aurora-A–BORA phosphorylation of Thr210 in G2, it promotes CDK1–cyclin-B activation, centrosome maturation/separation, bipolar-spindle formation, kinetochore and spindle-checkpoint regulation, chromosome segregation, spindle-midzone organization and cytokinesis. It acts at centrosomes, kinetochores/spindle, central spindle, and midbody rather than in one constitutive compartment. (wyatt2024insightsintothe pages 3-7, milletti2023cyclers’kinasesin pages 9-10, athwal2024centrosomesandassociated pages 7-8, cheng2024discoveryofinhibitors pages 45-49)

**Confidence assessment:** Identity, enzyme class, domain organization, Thr210 activation, dynamic mitotic localization, and essential roles in mitosis are high-confidence annotations. Individual substrate relationships vary in evidential strength and context. The 2024 full-length structural model and Chk2-regulatory mechanism are promising but partly preprint-based. Cancer-expression associations are robust but are not equivalent to proof of causal oncogenesis or predictive clinical utility. PLK1 inhibition is clinically implemented only through investigational trials in the retrieved evidence; no routine therapeutic use should be inferred.

References

1. (wyatt2024insightsintothe pages 3-7): Michael D. Wyatt and Campbell McInnes. Insights into the structural regulation of polo-like kinase activity using alphafold. bioRxiv, Oct 2024. URL: https://doi.org/10.1101/2024.10.21.618045, doi:10.1101/2024.10.21.618045. This article has 4 citations.

2. (wyatt2024insightsintothe pages 1-3): Michael D. Wyatt and Campbell McInnes. Insights into the structural regulation of polo-like kinase activity using alphafold. bioRxiv, Oct 2024. URL: https://doi.org/10.1101/2024.10.21.618045, doi:10.1101/2024.10.21.618045. This article has 4 citations.

3. (milletti2023cyclers’kinasesin pages 9-10): Giacomo Milletti, Valeria Colicchia, and Francesco Cecconi. Cyclers’ kinases in cell division: from molecules to cancer therapy. Cell Death &amp; Differentiation, 30:2035-2052, Jul 2023. URL: https://doi.org/10.1038/s41418-023-01196-z, doi:10.1038/s41418-023-01196-z. This article has 46 citations and is from a domain leading peer-reviewed journal.

4. (athwal2024centrosomesandassociated pages 3-4): Harjot Athwal, Arpitha Kochiyanil, Vasudeva Bhat, Alison L. Allan, and Armen Parsyan. Centrosomes and associated proteins in pathogenesis and treatment of breast cancer. Frontiers in Oncology, Mar 2024. URL: https://doi.org/10.3389/fonc.2024.1370565, doi:10.3389/fonc.2024.1370565. This article has 9 citations.

5. (cheng2024discoveryofinhibitors pages 45-49): Zixuan Cheng. Discovery of inhibitors targeting p38γ and plk1 using combined virtual screening, molecular dynamics simulations and biological evaluation. Text, Jan 2024. URL: https://doi.org/10.25916/sut.26281879, doi:10.25916/sut.26281879. This article has 1 citations and is from a peer-reviewed journal.

6. (OpenTargets Search: -PLK1): Open Targets Query (-PLK1, 8 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

7. (wyatt2024insightsintothe pages 7-8): Michael D. Wyatt and Campbell McInnes. Insights into the structural regulation of polo-like kinase activity using alphafold. bioRxiv, Oct 2024. URL: https://doi.org/10.1101/2024.10.21.618045, doi:10.1101/2024.10.21.618045. This article has 4 citations.

8. (athwal2024centrosomesandassociated pages 7-8): Harjot Athwal, Arpitha Kochiyanil, Vasudeva Bhat, Alison L. Allan, and Armen Parsyan. Centrosomes and associated proteins in pathogenesis and treatment of breast cancer. Frontiers in Oncology, Mar 2024. URL: https://doi.org/10.3389/fonc.2024.1370565, doi:10.3389/fonc.2024.1370565. This article has 9 citations.

9. (black2024chk2sustainsplk1 pages 5-9): Elizabeth M. Black, Carlos Andrés Ramírez Parrado, Isabelle Trier, Wenxue Li, Yoon Ki Joo, Jennifer Pichurin, Yansheng Liu, and Lilian Kabeche. Chk2 sustains plk1 activity in mitosis to ensure proper chromosome segregation. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.08.584115, doi:10.1101/2024.03.08.584115. This article has 12 citations.

10. (milletti2023cyclers’kinasesin pages 16-17): Giacomo Milletti, Valeria Colicchia, and Francesco Cecconi. Cyclers’ kinases in cell division: from molecules to cancer therapy. Cell Death &amp; Differentiation, 30:2035-2052, Jul 2023. URL: https://doi.org/10.1038/s41418-023-01196-z, doi:10.1038/s41418-023-01196-z. This article has 46 citations and is from a domain leading peer-reviewed journal.

11. (sreekumar2024plk1inhibitoronvansertib pages 1-2): Sreeja Sreekumar, Elodie Montaudon, Davis Klein, Migdalia E. Gonzalez, Pierre Painsec, Héloise Derrien, Laura Sourd, Tod Smeal, Elisabetta Marangoni, and Maya Ridinger. Plk1 inhibitor onvansertib enhances the efficacy of alpelisib in pik3ca-mutated hr-positive breast cancer resistant to palbociclib and endocrine therapy: preclinical insights. Sep 2024. URL: https://doi.org/10.3390/cancers16193259, doi:10.3390/cancers16193259. This article has 6 citations.

12. (black2024chk2sustainsplk1 pages 38-40): Elizabeth M. Black, Carlos Andrés Ramírez Parrado, Isabelle Trier, Wenxue Li, Yoon Ki Joo, Jennifer Pichurin, Yansheng Liu, and Lilian Kabeche. Chk2 sustains plk1 activity in mitosis to ensure proper chromosome segregation. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.08.584115, doi:10.1101/2024.03.08.584115. This article has 12 citations.

## Artifacts

- [Edison artifact artifact-00](PLK1-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. wyatt2024insightsintothe pages 3-7
2. athwal2024centrosomesandassociated pages 7-8
3. cheng2024discoveryofinhibitors pages 45-49
4. athwal2024centrosomesandassociated pages 3-4
5. wyatt2024insightsintothe pages 1-3
6. wyatt2024insightsintothe pages 7-8
7. DOI
8. https://doi.org/10.1101/2024.10.21.618045
9. https://doi.org/10.1038/s41418-023-01196-z
10. https://doi.org/10.3389/fonc.2024.1370565
11. https://doi.org/10.25916/sut.26281879
12. https://doi.org/10.1101/2024.03.08.584115
13. https://doi.org/10.3390/cancers16193259
14. https://doi.org/10.1101/2024.10.21.618045.
15. https://doi.org/10.1101/2024.03.08.584115.
16. https://doi.org/10.3389/fonc.2024.1370565.
17. https://doi.org/10.3390/cancers16193259.
18. https://doi.org/10.1101/2024.10.21.618045,
19. https://doi.org/10.1038/s41418-023-01196-z,
20. https://doi.org/10.3389/fonc.2024.1370565,
21. https://doi.org/10.25916/sut.26281879,
22. https://doi.org/10.1101/2024.03.08.584115,
23. https://doi.org/10.3390/cancers16193259,