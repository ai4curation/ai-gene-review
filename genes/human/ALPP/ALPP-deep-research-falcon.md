---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-01T00:41:08.446171'
end_time: '2026-09-01T00:48:47.707251'
duration_seconds: 459.26
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: ALPP
  gene_symbol: ALPP
  uniprot_accession: P05187
  protein_description: 'RecName: Full=Alkaline phosphatase, placental type; EC=3.1.3.1;
    AltName: Full=Alkaline phosphatase Regan isozyme; AltName: Full=Placental alkaline
    phosphatase 1 {ECO:0000303|PubMed:1939159}; Short=PLAP-1; Flags: Precursor;'
  gene_info: Name=ALPP {ECO:0000312|HGNC:HGNC:439}; Synonyms=PLAP {ECO:0000303|PubMed:1939159};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the alkaline phosphatase family. .
  protein_domains: Alkaline_phosphatase. (IPR001952); Alkaline_phosphatase_AS. (IPR018299);
    Alkaline_phosphatase_core_sf. (IPR017850); Alk_phosphatase (PF00245)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 21
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: ALPP-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** P05187
- **Protein Description:** RecName: Full=Alkaline phosphatase, placental type; EC=3.1.3.1; AltName: Full=Alkaline phosphatase Regan isozyme; AltName: Full=Placental alkaline phosphatase 1 {ECO:0000303|PubMed:1939159}; Short=PLAP-1; Flags: Precursor;
- **Gene Information:** Name=ALPP {ECO:0000312|HGNC:HGNC:439}; Synonyms=PLAP {ECO:0000303|PubMed:1939159};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the alkaline phosphatase family. .
- **Key Domains:** Alkaline_phosphatase. (IPR001952); Alkaline_phosphatase_AS. (IPR018299); Alkaline_phosphatase_core_sf. (IPR017850); Alk_phosphatase (PF00245)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ALPP" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ALPP' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ALPP** (gene ID: ALPP, UniProt: P05187) in human.

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
- **UniProt Accession:** P05187
- **Protein Description:** RecName: Full=Alkaline phosphatase, placental type; EC=3.1.3.1; AltName: Full=Alkaline phosphatase Regan isozyme; AltName: Full=Placental alkaline phosphatase 1 {ECO:0000303|PubMed:1939159}; Short=PLAP-1; Flags: Precursor;
- **Gene Information:** Name=ALPP {ECO:0000312|HGNC:HGNC:439}; Synonyms=PLAP {ECO:0000303|PubMed:1939159};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the alkaline phosphatase family. .
- **Key Domains:** Alkaline_phosphatase. (IPR001952); Alkaline_phosphatase_AS. (IPR018299); Alkaline_phosphatase_core_sf. (IPR017850); Alk_phosphatase (PF00245)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ALPP" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ALPP' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ALPP** (gene ID: ALPP, UniProt: P05187) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Human **ALPP** (UniProt **P05187**) Functional-Annotation Report

## Executive conclusion

The requested identity is verified: **ALPP** encodes human placental alkaline phosphatase (**PLAP**, placental ALP, Regan isozyme; EC 3.1.3.1), not intestinal ALP (**ALPI**), tissue-nonspecific ALP (**ALPL**), or germ-cell/placental-like ALP (**ALPPL2**, sometimes termed ALPG). The literature therefore matches the supplied *Homo sapiens* UniProt record P05187 and its alkaline-phosphatase catalytic domains. The three tissue-specific human ALPs are highly related—approximately 90–98% homologous—and their genes cluster at chromosome 2q34–q37.1, making explicit isozyme discrimination important (makris2023alkalinephosphatasesbiochemistry pages 1-4).

ALPP’s firmly established molecular function is that of a **GPI-anchored, extracellular-facing phosphomonoesterase**. It hydrolyzes phosphate monoesters according to the general reaction:

**phosphate monoester + H₂O → alcohol + inorganic phosphate (Pi)**.

It is a metal-dependent homodimer whose catalytic center contains two Zn²⁺ and one Mg²⁺ and uses Ser92 to form a covalent phosphoseryl intermediate. Its in-vitro substrate range is broad, but the physiologically decisive substrate or pathway specific to placental ALPP remains unresolved. Consequently, assigning ALPP the well-established PPi-mineralization function of ALPL/TNSALP would be an unsupported extrapolation. The clearest native biological evidence instead places ALPP on the syncytiotrophoblast surface, with exceptionally strong induction toward term (millan2006mammalianalkalinephosphatases pages 40-43, makris2023alkalinephosphatasesbiochemistry pages 1-4).

## Evidence summary

| Annotation dimension | Best-supported conclusion | Evidence type/strength | Important caveat |
|---|---|---|---|
| Identity | ALPP (UniProt P05187) is human placental alkaline phosphatase/PLAP, a tissue-specific ALP distinct from ALPI, ALPPL2, and ALPL; the tissue-specific ALPs share 90–98% homology and cluster on chr2q34–q37.1 (makris2023alkalinephosphatasesbiochemistry pages 1-4) | Peer-reviewed review; strong for gene/protein identity | Homology with related ALPs is high, so older literature may use overlapping names such as PLAP/PLALP/germ-cell ALP |
| Reaction / substrates | ALPP catalyzes extracellular hydrolysis of phosphomonoesters at alkaline pH; mammalian ALPs have broad in vitro specificity, but only a few physiological ALP substrates are firmly established overall (PPi, PLP; ATP/osteopontin proposed), not specifically resolved for ALPP in placenta (makris2023alkalinephosphatasesbiochemistry pages 1-4) | Review synthesis; moderate for ALPP-specific physiology, strong for ALP-class chemistry | Much substrate knowledge comes from ALPL/TNSALP or the ALP family broadly rather than direct ALPP-only experiments |
| Catalytic structure / cofactors | ALPP is a ~66 kDa homodimeric metalloenzyme requiring 2 Zn2+ and 1 Mg2+ per active site ensemble; catalysis uses conserved Ser92 to form a phosphoseryl intermediate in a two-step in-line displacement mechanism (makris2023alkalinephosphatasesbiochemistry pages 1-4, millan2006mammalianalkalinephosphatases pages 40-43) | Structural/biochemical evidence; strong | Mechanistic residue numbering and detailed mutagenesis are from structural studies/monograph treatment, not recent ALPP-focused human placenta studies |
| Topology / localization | ALPP is synthesized as a glycoprotein, processed in ER/Golgi, and displayed on the outer leaflet of the plasma membrane via a GPI anchor; soluble ALP can be released by phospholipase cleavage (makris2023alkalinephosphatasesbiochemistry pages 1-4) | Peer-reviewed review; strong | Exact subcellular microdomain context in trophoblast is less directly established here than membrane anchoring itself |
| Gestational expression | In a 2024 placenta mRNA atlas, ALPP rose from TPM 9.39 in first trimester to 2850.47 in third trimester, a 434.3-fold increase (FDR 4.27×10^-297), and was among the most upregulated late-gestation genes (gonzalez2024highthroughputmrnaseqatlas pages 16-20, gonzalez2024highthroughputmrnaseqatlas pages 20-24) | Large transcriptomic study; strong for mRNA dynamics | Preprint status; transcript levels do not by themselves prove enzymatic function |
| Placental biological role | Best-supported direct conclusion is that ALPP is a term syncytiotrophoblast marker associated with late gestational/fetal growth-related placental programs (gonzalez2024highthroughputmrnaseqatlas pages 20-24) | Human transcriptomic/marker evidence; moderate | A precise indispensable ALPP-specific biochemical role in placental physiology remains unresolved; 2024 GPI-pathway knockout data support importance of GPI-anchored trophoblast proteins generally, not ALPP specifically (alvarezsanchez2024thegpianchorbiosynthesis pages 1-2, alvarezsanchez2024thegpianchorbiosynthesis pages 5-6) |
| Tumor diagnostic application | ALPP is an established tumor marker, especially in germ cell tumors; immunohistochemistry across 12,381 cancers/131 tumor types found ALPP expression in 48 tumor categories (36.6%), with strong positivity in 22 (16.8%); highest rates were seminoma 96%, embryonal carcinoma 85%, yolk sac tumor 56% (OpenTargets Search: -ALPP) | Large pathology dataset / target-disease evidence; moderate-strong | Cancer-association evidence is about aberrant expression/biomarker utility, not native placental function |
| CAR-T translation status | PLAP/ALPP is considered an emerging solid-tumor CAR target with reported preclinical anti-tumor activity, but no active CAR clinical trials targeting PLAP were identified as of January 2023 (maher2023carbasedimmunotherapyof pages 11-13, maher2023carbasedimmunotherapyof pages 13-14) | 2023 expert review; moderate | Normal-tissue expression remains a translational concern, especially conflicting gastrointestinal expression data |


*Table: This table summarizes the strongest current evidence for functional annotation of human ALPP/P05187 across identity, enzymology, localization, placental biology, and translational oncology. It is useful for distinguishing well-supported conclusions from important uncertainties and indirect inferences.*

## 1. Identity verification and nomenclature

Humans have four alkaline-phosphatase genes. **ALPI**, **ALPP**, and **ALPPL2** encode the intestinal, placental, and germ-cell/placental-like tissue-specific enzymes, respectively; **ALPL** encodes tissue-nonspecific alkaline phosphatase, whose bone and liver products are post-translational isoforms rather than separate gene products. ALPP is therefore unambiguously the placental enzyme requested here. Human TNSALP is only about 57% identical and 74% homologous to placental ALP, whereas the three chromosome-2 tissue-specific enzymes are much more closely related (makris2023alkalinephosphatasesbiochemistry pages 1-4).

This distinction matters in interpreting publications. “Total ALP,” bone ALP, and most mineralization or hypophosphatasia studies principally concern **ALPL**, not ALPP. Similarly, placental-like or germ-cell ALP can refer to **ALPPL2**. None of those findings should be reassigned automatically to P05187.

The reported protein family and domains are fully consistent with ALPP: the enzyme has the conserved alkaline-phosphatase core and active-site architecture, functions as a dimeric metalloenzyme, and possesses the secretory/GPI-processing organization characteristic of mammalian ALPs (makris2023alkalinephosphatasesbiochemistry pages 1-4, millan2006mammalianalkalinephosphatases pages 40-43).

## 2. Primary molecular function and substrate specificity

### Catalyzed chemistry

ALPP is a phosphomonoester hydrolase active most efficiently under alkaline assay conditions, broadly around pH 8–11. Mammalian ALPs can also support transphosphorylation under suitable in-vitro conditions. Routine biochemical assays exploit hydrolysis of artificial **p-nitrophenyl phosphate**, producing phosphate and p-nitrophenol; under alkaline conditions the latter becomes yellow 4-nitrophenoxide measurable at 405 nm (makris2023alkalinephosphatasesbiochemistry pages 1-4, makris2023alkalinephosphatasesbiochemistry pages 4-7).

### Substrate specificity

The enzyme is **broad-specificity in vitro**, acting on many organic phosphate monoesters rather than recognizing one narrow substrate class. Reviews identify PPi and pyridoxal-5′-phosphate as validated physiological substrates for mammalian ALP biology, with ATP/nucleotides and phosphorylated proteins such as osteopontin proposed in some contexts. However, much of the decisive in-vivo evidence comes from **ALPL/TNSALP**, especially bone and neural physiology—not from ALPP-selective experiments in human placenta (makris2023alkalinephosphatasesbiochemistry pages 1-4).

Accordingly, the most defensible annotation is:

* **Established:** extracellular phosphomonoester hydrolysis and Pi release.
* **Plausible but not demonstrated as ALPP’s defining placental reaction:** hydrolysis of extracellular nucleotides, PPi, PLP, or other phosphorylated metabolites.
* **Not justified:** describing ALPP as the principal human skeletal PPi phosphatase. That function belongs to ALPL/TNSALP.

This uncertainty is echoed by the 2023 expert review, which states that despite intensive study, the exact physiological functions of ALPs remain incompletely resolved (makris2023alkalinephosphatasesbiochemistry pages 1-4, makris2023alkalinephosphatasesbiochemistry pages 7-9).

## 3. Catalytic mechanism, structure, and biochemical properties

ALPP functions as a **homodimer**, with each mature monomer approximately 66 kDa. Catalytic activity requires an active-site metal ensemble of **two Zn²⁺ and one Mg²⁺**. These ions participate directly in chemistry and help stabilize monomer conformation and subunit interactions (makris2023alkalinephosphatasesbiochemistry pages 1-4).

The mechanism is a two-step, in-line displacement:

1. Conserved **Ser92** attacks the substrate phosphorus, releasing the dephosphorylated alcohol and forming a covalent phosphoseryl intermediate.
2. Water hydrolyzes that intermediate, releasing Pi and regenerating Ser92.

Structural work identifies conserved metal-binding/catalytic residues including Asp42, His153, Ser155, Glu311, Asp316, His320, Asp357, His358, His360, and His432. PLAP also contains a distinctive “crown domain” spanning approximately residues 366–430; Glu429 lies near the active-site entrance and contributes to isozyme-specific substrate and inhibitor behavior (millan2006mammalianalkalinephosphatases pages 40-43, millan2006mammalianalkalinephosphatases pages 52-54).

Inorganic phosphate is a competitive inhibitor, whereas several L-amino acids inhibit PLAP uncompetitively. A practically important property is its unusual **heat stability**: placental ALP can resist heating at 65°C for 60 minutes near physiological pH, historically helping laboratories distinguish it from less heat-stable ALP forms (millan2006mammalianalkalinephosphatases pages 52-54).

## 4. Biosynthesis and localization

ALPP is synthesized as a precursor entering the secretory pathway. Glycan chains are installed in the endoplasmic reticulum and Golgi, and the C-terminal membrane-targeting segment is replaced with a **glycosylphosphatidylinositol anchor**. The mature enzyme is consequently displayed on the **external leaflet of the plasma membrane**, with its catalytic domain exposed to extracellular substrates. Soluble enzyme can enter the circulation following phospholipase-mediated release or membrane shedding (makris2023alkalinephosphatasesbiochemistry pages 1-4).

In placenta, ALPP is most strongly associated with the **syncytiotrophoblast**, particularly at term. Thus, the likely physiological reaction compartment is the extracellular surface of the trophoblast at the maternal–fetal interface, including its microvillous membrane and shed membrane material—not the cytosol or nucleus. Placental membrane particles are enriched for alkaline-phosphatase activity, supporting its association with the syncytial membrane compartment.

## 5. Expression across gestation and placental biology

The strongest recent quantitative result comes from the human placental mRNA atlas posted in 2023 and indexed in 2024. ALPP increased from **9.39 TPM in first-trimester chorionic villi to 2,850.47 TPM in third trimester**, a **434.3-fold increase** with FDR **4.27 × 10⁻²⁹⁷**. It was one of the four genes with the greatest third-trimester fold increase and the second-most strongly induced strict DEG described in the discussion (gonzalez2024highthroughputmrnaseqatlas pages 16-20).

The same study found that 86.7% of expressed placental protein-coding transcripts changed significantly between first and third trimester, emphasizing that ALPP should not be treated as a gestationally invariant marker. ALPP is a well-supported **term syncytiotrophoblast marker**, but not an equally reliable first-trimester marker (gonzalez2024highthroughputmrnaseqatlas pages 20-24, gonzalez2024highthroughputmrnaseqatlas pages 16-20).

The atlas associated late ALPP expression with fetal-growth regulation and noted previous links between abnormal ALPP levels, intrauterine growth restriction, and preterm delivery. These are associations, however, and do not establish the molecular substrate through which ALPP would regulate growth. The study’s matched-subject analysis correlated strongly with the full analysis (coefficient 0.98), while acknowledged limitations included modest demographic, BMI, thyroid-disorder, and pregnancy-complication differences. Importantly, this remains transcriptomic evidence and the cited version was a bioRxiv preprint, not proof of enzymatic causality (gonzalez2024highthroughputmrnaseqatlas pages 20-24).

### What can be inferred from the 2024 GPI-pathway study?

A 2024 CRISPR study disrupted **Pigl** or **Pigf** in mouse trophoblast stem cells. Loss of GPI-anchor biosynthesis impaired syncytiotrophoblast development—especially the SynT-II layer—vascularization, fetal–maternal exchange, and induction of early WNT signaling, while causing excessive ER unfolded-protein response. The authors identified 603 DEGs after Pigl knockout and 1,568 after Pigf knockout; transcriptomic experiments used five independent biological replicates per genotype (alvarezsanchez2024thegpianchorbiosynthesis pages 1-2, alvarezsanchez2024thegpianchorbiosynthesis pages 5-6).

This is important contextual evidence that **GPI-anchored proteins as a class** are integral to trophoblast differentiation and placental development. It is **not direct evidence that ALPP itself causes those phenotypes**, because the manipulated genes affect the processing of many GPI-anchored proteins. Expert interpretation should therefore resist converting a GPI-pathway phenotype into an ALPP-specific pathway assignment.

## 6. Pathways and biological-process annotation

The evidence supports the following hierarchy:

1. **Direct molecular pathway:** extracellular phosphate-ester metabolism at the trophoblast plasma membrane.
2. **Cellular process:** maturation and late-gestation specialization of syncytiotrophoblast surface biology, for which ALPP is a robust marker.
3. **Possible physiological consequences:** regulation of local extracellular nucleotide/phosphate chemistry, membrane interactions, and fetal-growth-associated placental function. These remain mechanistic hypotheses rather than definitively mapped ALPP-specific pathways.
4. **Indirect GPI context:** ER/Golgi maturation, GPI-anchor biosynthesis, lipid-raft-like membrane partitioning, surface trafficking, and release by phospholipase or membrane shedding.

There is presently insufficient evidence to place ALPP as a necessary upstream enzyme in WNT, PI3K–AKT, or other canonical signaling pathways under normal placental conditions. Associations with such pathways in cancer datasets should be interpreted as tumor-state correlations unless ALPP perturbation experiments demonstrate causality.

## 7. Current applications and real-world implementation

### Diagnostic pathology and tumor-marker use

PLAP is a classic **oncofetal tumor marker**, especially useful in the pathological evaluation of germ-cell tumors. A large immunohistochemical analysis summarized by Open Targets examined **12,381 cancers across 131 tumor types**. ALPP was detected in 48 tumor categories (36.6%), with strong positivity in 22 (16.8%). Reported positivity was highest in testicular germ-cell tumors: **96% of seminomas, 85% of embryonal carcinomas, and 56% of yolk-sac tumors**. Expression also occurs in subsets of female-genital-tract, gastroesophageal, pancreaticobiliary, colorectal, endometrial, ovarian, cervical, and gastric cancers (OpenTargets Search: -ALPP).

In practice, PLAP immunohistochemistry is used as part of a **marker panel**, not as a universally specific standalone test. Closely related ALP isoenzymes, variable tumor differentiation, and normal reproductive expression complicate interpretation. Total serum ALP assays are even less specific: standard activity assays cannot determine which gene product generated the measured activity and are dominated in ordinary serum by liver and bone sources (makris2023alkalinephosphatasesbiochemistry pages 1-4, makris2023alkalinephosphatasesbiochemistry pages 7-9).

### Research and biotechnology

ALP-class enzymes are routinely used to dephosphorylate DNA or proteins, as immunoassay labels, and as reporter enzymes. PLAP’s heat stability, extracellular topology, and robust histochemical activity have made placental ALP derivatives useful experimental reporters. These are protein-technology applications and should not be mistaken for evidence of the native placental substrate (makris2023alkalinephosphatasesbiochemistry pages 1-4).

### Therapeutic targeting

A 2023 expert survey identified PLAP as an emerging CAR target because it is cell-surface accessible and aberrantly expressed in several solid and germ-cell tumors. PLAP-specific CAR constructs had shown preclinical antitumor activity, but **no active PLAP-directed CAR clinical trial** was found on ClinicalTrials.gov as of 11 January 2023 (maher2023carbasedimmunotherapyof pages 11-13, maher2023carbasedimmunotherapyof pages 13-14).

The principal translational concern is **on-target/off-tumor toxicity**. Although PLAP is described as minimally expressed in most normal tissues and concentrated in reproductive organs, protein-atlas evidence suggested strong gastrointestinal expression, partly conflicting with mRNA data. Until normal-tissue expression, isozyme cross-reactivity, and pregnancy-related risks are resolved, PLAP-directed cellular therapy remains preclinical rather than a real-world treatment (maher2023carbasedimmunotherapyof pages 11-13).

## 8. Overall evidence assessment

**High-confidence annotations** are the identity of P05187 as human ALPP/PLAP; phosphomonoesterase activity; two-Zn/one-Mg catalytic machinery; Ser92-dependent covalent catalysis; homodimerization; glycosylation; GPI anchoring; extracellular-facing membrane topology; and strong late-gestation syncytiotrophoblast expression.

**Moderate-confidence biological interpretation** is that ALPP contributes to extracellular phosphate-metabolite processing at the mature syncytiotrophoblast surface and is associated with fetal-growth-related late placental programs.

**Unresolved questions** are the dominant physiological substrate in placenta, the quantitative contribution of its catalytic activity to maternal–fetal exchange or signaling, and whether ALPP itself is necessary for normal placental development. ALPP-selective knockout or catalytic-dead rescue experiments in human trophoblast organoids and appropriate in-vivo models would be the most direct way to resolve these questions.

## Key recent and authoritative sources

* Makris K, Mousa C, Cavalier E. **“Alkaline Phosphatases: Biochemistry, Functions, and Measurement.”** *Calcified Tissue International* 112, 233–242. Published 2023; online DOI record dated 2022. https://doi.org/10.1007/s00223-022-01048-x (makris2023alkalinephosphatasesbiochemistry pages 1-4)
* González TL et al. **“High-throughput mRNA-seq atlas of human placenta shows vast transcriptome remodeling from first to third trimester.”** bioRxiv version posted June 7, 2023; indexed as 2024. https://doi.org/10.1101/2023.06.06.543972 (gonzalez2024highthroughputmrnaseqatlas pages 20-24, gonzalez2024highthroughputmrnaseqatlas pages 16-20)
* Álvarez-Sánchez A et al. **“The GPI-anchor biosynthesis pathway is critical for syncytiotrophoblast differentiation and placental development.”** *Cellular and Molecular Life Sciences* 81:246. Accepted May 16, 2024. https://doi.org/10.1007/s00018-024-05284-2 (alvarezsanchez2024thegpianchorbiosynthesis pages 1-2, alvarezsanchez2024thegpianchorbiosynthesis pages 5-6)
* Maher J, Davies DM. **“CAR-Based Immunotherapy of Solid Tumours—A Survey of the Emerging Targets.”** *Cancers* 15:1171. Published February 2023. https://doi.org/10.3390/cancers15041171 (maher2023carbasedimmunotherapyof pages 11-13)
* Millán JL. **“Mammalian Alkaline Phosphatases: From Biology to Applications in Medicine and Biotechnology.”** Wiley, 2006. https://doi.org/10.1002/3527608060 (millan2006mammalianalkalinephosphatases pages 40-43, millan2006mammalianalkalinephosphatases pages 52-54)

References

1. (makris2023alkalinephosphatasesbiochemistry pages 1-4): Konstantinos Makris, Chagigia Mousa, and Etienne Cavalier. Alkaline phosphatases: biochemistry, functions, and measurement. Calcified Tissue International, 112:233-242, Dec 2023. URL: https://doi.org/10.1007/s00223-022-01048-x, doi:10.1007/s00223-022-01048-x. This article has 165 citations and is from a peer-reviewed journal.

2. (millan2006mammalianalkalinephosphatases pages 40-43): José Luis Millán. Mammalian alkaline phosphatases: from biology to applications in medicine and biotechnology. ArXiv, Jan 2006. URL: https://doi.org/10.1002/3527608060, doi:10.1002/3527608060. This article has 429 citations.

3. (gonzalez2024highthroughputmrnaseqatlas pages 16-20): Tania L Gonzalez, Sahar Wertheimer, Amy E Flowers, Yizhou Wang, Chintda Santiskulvong, Ekaterina L Clark, Caroline A Jefferies, Kate Lawrenson, Jessica L Chan, Nikhil V Joshi, Yazhen Zhu, Hsian-Rong Tseng, S. Ananth Karumanchi, John Williams, and Margareta D Pisarska. High-throughput mrna-seq atlas of human placenta shows vast transcriptome remodeling from first to third trimester. bioRxiv, Jun 2024. URL: https://doi.org/10.1101/2023.06.06.543972, doi:10.1101/2023.06.06.543972. This article has 11 citations.

4. (gonzalez2024highthroughputmrnaseqatlas pages 20-24): Tania L Gonzalez, Sahar Wertheimer, Amy E Flowers, Yizhou Wang, Chintda Santiskulvong, Ekaterina L Clark, Caroline A Jefferies, Kate Lawrenson, Jessica L Chan, Nikhil V Joshi, Yazhen Zhu, Hsian-Rong Tseng, S. Ananth Karumanchi, John Williams, and Margareta D Pisarska. High-throughput mrna-seq atlas of human placenta shows vast transcriptome remodeling from first to third trimester. bioRxiv, Jun 2024. URL: https://doi.org/10.1101/2023.06.06.543972, doi:10.1101/2023.06.06.543972. This article has 11 citations.

5. (alvarezsanchez2024thegpianchorbiosynthesis pages 1-2): Andrea Álvarez-Sánchez, Johanna Grinat, Paula Doria-Borrell, Maravillas Mellado-López, Érica Pedrera-Alcócer, Marta Malenchini, Salvador Meseguer, Myriam Hemberger, and Vicente Pérez-García. The gpi-anchor biosynthesis pathway is critical for syncytiotrophoblast differentiation and placental development. Cellular and Molecular Life Sciences: CMLS, May 2024. URL: https://doi.org/10.1007/s00018-024-05284-2, doi:10.1007/s00018-024-05284-2. This article has 20 citations.

6. (alvarezsanchez2024thegpianchorbiosynthesis pages 5-6): Andrea Álvarez-Sánchez, Johanna Grinat, Paula Doria-Borrell, Maravillas Mellado-López, Érica Pedrera-Alcócer, Marta Malenchini, Salvador Meseguer, Myriam Hemberger, and Vicente Pérez-García. The gpi-anchor biosynthesis pathway is critical for syncytiotrophoblast differentiation and placental development. Cellular and Molecular Life Sciences: CMLS, May 2024. URL: https://doi.org/10.1007/s00018-024-05284-2, doi:10.1007/s00018-024-05284-2. This article has 20 citations.

7. (OpenTargets Search: -ALPP): Open Targets Query (-ALPP, 9 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

8. (maher2023carbasedimmunotherapyof pages 11-13): John Maher and David M. Davies. Car-based immunotherapy of solid tumours—a survey of the emerging targets. Cancers, 15:1171, Feb 2023. URL: https://doi.org/10.3390/cancers15041171, doi:10.3390/cancers15041171. This article has 24 citations.

9. (maher2023carbasedimmunotherapyof pages 13-14): John Maher and David M. Davies. Car-based immunotherapy of solid tumours—a survey of the emerging targets. Cancers, 15:1171, Feb 2023. URL: https://doi.org/10.3390/cancers15041171, doi:10.3390/cancers15041171. This article has 24 citations.

10. (makris2023alkalinephosphatasesbiochemistry pages 4-7): Konstantinos Makris, Chagigia Mousa, and Etienne Cavalier. Alkaline phosphatases: biochemistry, functions, and measurement. Calcified Tissue International, 112:233-242, Dec 2023. URL: https://doi.org/10.1007/s00223-022-01048-x, doi:10.1007/s00223-022-01048-x. This article has 165 citations and is from a peer-reviewed journal.

11. (makris2023alkalinephosphatasesbiochemistry pages 7-9): Konstantinos Makris, Chagigia Mousa, and Etienne Cavalier. Alkaline phosphatases: biochemistry, functions, and measurement. Calcified Tissue International, 112:233-242, Dec 2023. URL: https://doi.org/10.1007/s00223-022-01048-x, doi:10.1007/s00223-022-01048-x. This article has 165 citations and is from a peer-reviewed journal.

12. (millan2006mammalianalkalinephosphatases pages 52-54): José Luis Millán. Mammalian alkaline phosphatases: from biology to applications in medicine and biotechnology. ArXiv, Jan 2006. URL: https://doi.org/10.1002/3527608060, doi:10.1002/3527608060. This article has 429 citations.

## Artifacts

- [Edison artifact artifact-00](ALPP-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. makris2023alkalinephosphatasesbiochemistry pages 1-4
2. gonzalez2024highthroughputmrnaseqatlas pages 20-24
3. millan2006mammalianalkalinephosphatases pages 52-54
4. gonzalez2024highthroughputmrnaseqatlas pages 16-20
5. maher2023carbasedimmunotherapyof pages 11-13
6. millan2006mammalianalkalinephosphatases pages 40-43
7. alvarezsanchez2024thegpianchorbiosynthesis pages 1-2
8. alvarezsanchez2024thegpianchorbiosynthesis pages 5-6
9. maher2023carbasedimmunotherapyof pages 13-14
10. makris2023alkalinephosphatasesbiochemistry pages 4-7
11. makris2023alkalinephosphatasesbiochemistry pages 7-9
12. https://doi.org/10.1007/s00223-022-01048-x
13. https://doi.org/10.1101/2023.06.06.543972
14. https://doi.org/10.1007/s00018-024-05284-2
15. https://doi.org/10.3390/cancers15041171
16. https://doi.org/10.1002/3527608060
17. https://doi.org/10.1007/s00223-022-01048-x,
18. https://doi.org/10.1002/3527608060,
19. https://doi.org/10.1101/2023.06.06.543972,
20. https://doi.org/10.1007/s00018-024-05284-2,
21. https://doi.org/10.3390/cancers15041171,