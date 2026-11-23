---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-26T23:53:25.891025'
end_time: '2026-09-27T00:03:38.328018'
duration_seconds: 612.44
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: RAF1
  gene_symbol: RAF1
  uniprot_accession: P04049
  protein_description: 'RecName: Full=RAF proto-oncogene serine/threonine-protein
    kinase {ECO:0000305}; EC=2.7.11.1 {ECO:0000269|PubMed:17603483}; AltName: Full=Proto-oncogene
    c-RAF; Short=cRaf; AltName: Full=Raf-1;'
  gene_info: Name=RAF1 {ECO:0000312|HGNC:HGNC:9829}; Synonyms=RAF;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the protein kinase superfamily. TKL Ser/Thr
  protein_domains: C1-like_sf. (IPR046349); DAG/PE-bd. (IPR020454); Kinase-like_dom_sf.
    (IPR011009); PKC_DAG/PE. (IPR002219); Prot_kinase_dom. (IPR000719)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 42
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: RAF1-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** P04049
- **Protein Description:** RecName: Full=RAF proto-oncogene serine/threonine-protein kinase {ECO:0000305}; EC=2.7.11.1 {ECO:0000269|PubMed:17603483}; AltName: Full=Proto-oncogene c-RAF; Short=cRaf; AltName: Full=Raf-1;
- **Gene Information:** Name=RAF1 {ECO:0000312|HGNC:HGNC:9829}; Synonyms=RAF;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the protein kinase superfamily. TKL Ser/Thr
- **Key Domains:** C1-like_sf. (IPR046349); DAG/PE-bd. (IPR020454); Kinase-like_dom_sf. (IPR011009); PKC_DAG/PE. (IPR002219); Prot_kinase_dom. (IPR000719)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "RAF1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'RAF1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **RAF1** (gene ID: RAF1, UniProt: P04049) in human.

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
- **UniProt Accession:** P04049
- **Protein Description:** RecName: Full=RAF proto-oncogene serine/threonine-protein kinase {ECO:0000305}; EC=2.7.11.1 {ECO:0000269|PubMed:17603483}; AltName: Full=Proto-oncogene c-RAF; Short=cRaf; AltName: Full=Raf-1;
- **Gene Information:** Name=RAF1 {ECO:0000312|HGNC:HGNC:9829}; Synonyms=RAF;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the protein kinase superfamily. TKL Ser/Thr
- **Key Domains:** C1-like_sf. (IPR046349); DAG/PE-bd. (IPR020454); Kinase-like_dom_sf. (IPR011009); PKC_DAG/PE. (IPR002219); Prot_kinase_dom. (IPR000719)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "RAF1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'RAF1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **RAF1** (gene ID: RAF1, UniProt: P04049) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Human RAF1/CRAF (UniProt P04049): Functional Annotation Research Report

## Executive summary

**Identity is verified.** The requested protein is human **RAF1** (HGNC:9829; UniProt **P04049**), also called **CRAF, c-Raf, or Raf-1**—not BRAF, ARAF, or a similarly named protein from another organism. It is a ubiquitously expressed, approximately 75-kDa RAF-family serine/threonine kinase and a direct effector of activated RAS. Its domain architecture and kinase-family assignment agree with the supplied UniProt record. (riaud2024theroleof pages 1-2, spencersmith2024regulationofraf pages 1-3)

RAF1’s best-established catalytic function is to phosphorylate the activation loops of **MEK1/MAP2K1 and MEK2/MAP2K2**, thereby initiating the MEK–ERK arm of mitogen-activated protein kinase signaling. These remain the only broadly accepted physiological RAF1 substrates; many reported alternatives have substantially weaker validation. RAF1 also has important noncatalytic functions as a dimerization partner and signaling scaffold, particularly in apoptosis control and some KRAS-driven cancers. (matallanas2011raffamilykinases pages 8-9, roskoski2010rafproteinserinethreoninekinases pages 2-3, bahar2023targetingtherasrafmapk pages 9-10)

| Aspect | Best-supported annotation | Evidence strength/caveat |
|---|---|---|
| Identity | Human **RAF1** encodes **CRAF** (also RAF-1/c-Raf), a ubiquitously expressed ~75-kDa RAF-family serine/threonine protein kinase corresponding to UniProt **P04049**. (riaud2024theroleof pages 1-2, spencersmith2024regulationofraf pages 1-3) | **High confidence.** Nomenclature, organism, kinase class, and supplied UniProt identity are concordant; this is not BRAF, ARAF, or a similarly named non-human gene. |
| Domain architecture | The N-terminal regulatory region comprises **CR1**—the RAS-binding domain (RBD) and cysteine-rich domain (CRD/C1-like phospholipid-binding module)—and serine/threonine-rich **CR2**, which contains the inhibitory pSer259 14-3-3 site. C-terminal **CR3** contains the protein-kinase domain and pSer621 14-3-3 site. (wang2023targetingcrafkinase pages 1-2, riaud2024theroleof pages 1-2, scardaci2024novelraf‐directedapproaches pages 1-2) | **High confidence.** This architecture agrees with classification in the protein-kinase superfamily and the TKL Ser/Thr branch; the CRD explains the supplied C1-like/DAG–phorbol-ester-binding InterPro annotations, although RAF1 is not conventionally defined as a DAG-activated kinase. |
| Catalytic reaction | RAF1 transfers the γ-phosphate of MgATP to serine residues in protein substrates: **ATP + protein-L-serine → ADP + protein-O-phospho-L-serine**. Its canonical reaction activates MEK1/2 through dual activation-loop phosphorylation. (matallanas2011raffamilykinases pages 8-9, roskoski2010rafproteinserinethreoninekinases pages 2-3) | **High confidence** for protein-serine phosphorylation. Exact activation-loop numbering is isoform-specific; commonly cited sites are MEK1 Ser218/Ser222 and MEK2 Ser222/Ser226. |
| Direct substrates | **MEK1/MAP2K1 and MEK2/MAP2K2 are the only broadly accepted physiological RAF1 substrates.** RAF kinases have unusually restricted substrate specificity, and CRAF generally has lower intrinsic MEK-kinase activity than BRAF. (matallanas2011raffamilykinases pages 8-9, roskoski2010rafproteinserinethreoninekinases pages 2-3, bahar2023targetingtherasrafmapk pages 6-7) | **High confidence** for MEK1/2. BAD, adenylyl cyclases, RB, MYPT and other reported targets lack equally broad physiological validation; BAD should not be presented as equivalent in certainty to MEK1/2. (matallanas2011raffamilykinases pages 8-9, bahar2023targetingtherasrafmapk pages 9-10, riaud2024theroleof pages 5-6) |
| Activation mechanism | Inactive RAF1 is a closed, cytosolic monomer stabilized by intramolecular CRD–kinase contacts and 14-3-3 binding to pSer259/pSer621. GTP-loaded RAS recruits it through the RBD and CRD to phosphatidylserine-rich plasma membrane; MRAS–SHOC2–PP1C promotes Ser259 dephosphorylation, regulatory phosphorylation and conformational opening permit RAF homo/heterodimerization, and the active dimer phosphorylates MEK. HSP90–CDC37 supports RAF1 folding and stability. (spencersmith2024regulationofraf pages 6-7, riaud2024theroleof pages 1-2, spencersmith2024regulationofraf pages 1-3) | **High confidence** for the overall cycle. Individual phosphorylation events are context-dependent, and structural details have historically been inferred partly from BRAF; recent biochemical/structural studies support both shared RAF regulation and CRAF-specific differences. |
| Canonical localization | RAF1 is predominantly an inactive **cytosolic** complex at baseline and is recruited transiently to the cytoplasmic face of the **plasma membrane** by RAS-GTP, where dimerization, MEK phosphorylation, and canonical MAPK signaling occur. (riaud2024theroleof pages 1-2, bahar2023targetingtherasrafmapk pages 5-6, jeon2024signalingfromras pages 18-20) | **High confidence.** Membrane residence is stimulus-dependent rather than constitutive; evidence in the cited EGF context argues against internalized EGFR endosomes as the principal signaling site. |
| Noncanonical localization | A context-specific RAF1 pool translocates to the **mitochondrial surface**, promoted in some systems by PAK-mediated Ser338/Ser339 phosphorylation or BCL-2 binding, and participates in anti-apoptotic signaling. (riaud2024theroleof pages 5-6, wang2023targetingcrafkinase pages 14-15) | **Moderate confidence and context-dependent.** Mitochondrial BAD phosphorylation has been reported, but BAD is a **proposed/contextual substrate**, not as firmly established as MEK1/2. Endosomal, Golgi, and nuclear RAF1 should not be treated as universal canonical localizations from current evidence. |
| Kinase-independent roles | RAF1 can function as a scaffold that suppresses apoptosis by binding/inhibiting ASK1 and MST2 and can support proliferation, migration, and KRAS-driven tumor maintenance through dimerization or protein interactions even when catalytic activity is dispensable. (riaud2024theroleof pages 5-6, bahar2023targetingtherasrafmapk pages 9-10, wang2023targetingcrafkinase pages 15-16) | **Moderate-to-high confidence**, strongest in genetic and cancer-model studies. The relative contribution of catalytic versus scaffold activity varies by tissue, oncogenic driver, and experimental system. |
| Germline disease | Heterozygous germline **RAF1** variants cause RASopathies, especially **Noonan syndrome 5** and Noonan syndrome with multiple lentigines, often with hypertrophic cardiomyopathy. Variants near the N-terminal 14-3-3 site can weaken autoinhibition; both activating variants such as G361A and catalytically impaired, dimer-activating variants such as D486N are documented. (OpenTargets Search: -RAF1, spencersmith2024regulationofraf pages 6-7, riaud2024theroleof pages 9-10) | **High-confidence gene–disease association.** Pathogenic mechanisms are allele-specific and cannot be reduced to simple gain of intrinsic kinase activity. |
| Somatic cancer | RAF1 is altered by activating mutations, amplification, fusions, overexpression, and adaptive activation. Reported mutation estimates vary from ~0.7% to 2.3% pan-cancer; examples include 5.41% in cutaneous melanoma and amplification in 10.71% of one TCGA bladder-cancer cohort. RAF1 fusions occur in up to 18.5% of pancreatic acinar-cell carcinomas but are much rarer in many common cancers. (wang2023targetingcrafkinase pages 14-15, riaud2024theroleof pages 6-7, wang2023targetingcrafkinase pages 15-16, riaud2024theroleof pages 7-8) | **Moderate-to-high confidence**, but frequencies depend strongly on cohort, assay, and alteration definition. RAF1 is less commonly mutated than BRAF and is often activated downstream of mutant RAS without alteration of RAF1 itself. |
| Therapeutic status | **No selective RAF1/CRAF inhibitor is approved.** Approved BRAF-directed drugs are not RAF1-selective and can induce paradoxical ERK activation in RAS-active/BRAF-wild-type cells through RAF dimers. Type-II pan-RAF or RAF-dimer strategies—including belvarafenib, lifirafenib, naporafenib, tovorafenib and related agents—and pan-RAF–MEK combinations remain investigational. (wang2023targetingcrafkinase pages 21-23, riaud2024theroleof pages 11-12, scardaci2024novelraf‐directedapproaches pages 2-3, wang2023targetingcrafkinase pages 1-2) | **Clinical validation remains incomplete.** Published early-trial response rates vary widely by agent and biomarker (0–64% in studies summarized in 2024), and inhibiting catalytic activity may not eliminate kinase-independent RAF1 functions; selective RAF1 degradation is therefore an attractive but still preclinical strategy. (riaud2024theroleof pages 11-12, riaud2024theroleof pages 10-11) |


*Table: Concise evidence-based annotation of human RAF1/CRAF (UniProt P04049), separating established catalytic and localization functions from contextual or emerging findings. The table also distinguishes validated disease associations from investigational therapeutic strategies.*

## 1. Target verification and molecular organization

### 1.1 Identity

The literature consistently identifies **RAF1 as encoding CRAF/RAF-1**, one of the three mammalian RAF paralogues together with ARAF and BRAF. The descriptions—human protein, RAF-family kinase, RAS effector, and approximately 75-kDa serine/threonine kinase—match UniProt P04049. No evidence was used from a different RAF-like gene or organism. (riaud2024theroleof pages 1-2, scardaci2024novelraf‐directedapproaches pages 1-2, spencersmith2024regulationofraf pages 1-3)

### 1.2 Domains

RAF1 has three conserved regions:

- **CR1**, containing the **RAS-binding domain (RBD)** and **cysteine-rich domain (CRD)**. The latter is a C1-like phospholipid-binding module that contacts RAS and membrane lipids and also participates in autoinhibition.
- **CR2**, a serine/threonine-rich regulatory segment containing the inhibitory **Ser259** 14-3-3-binding site.
- **CR3**, the C-terminal protein-kinase domain, including the DFG motif and regulatory αC helix, followed by a second 14-3-3-binding site around **Ser621**. (wang2023targetingcrafkinase pages 1-2, riaud2024theroleof pages 1-2, scardaci2024novelraf‐directedapproaches pages 1-2)

This organization agrees with the supplied InterPro assignments for a C1-like/DAG–phorbol-ester-binding fold and a protein-kinase domain. The C1-like annotation should not, however, be interpreted to mean that RAF1 is regulated like a conventional DAG-activated protein kinase C; in RAF1, the CRD principally supports RAS, phospholipid, and intramolecular regulatory interactions. (wang2023targetingcrafkinase pages 1-2, spencersmith2024regulationofraf pages 6-7)

## 2. Primary biochemical function

### 2.1 Catalytic reaction

RAF1 is an ATP-dependent protein-serine kinase (EC 2.7.11.1):

**ATP + protein-L-serine → ADP + protein-O-phospho-L-serine.**

The catalytic domain uses MgATP to transfer the γ-phosphate of ATP to substrate serine hydroxyl groups. RAF kinases have unusually restricted physiological substrate specificity. (matallanas2011raffamilykinases pages 8-9, roskoski2010rafproteinserinethreoninekinases pages 2-3)

### 2.2 Substrate specificity

The strongest consensus is that **MEK1 and MEK2 are RAF1’s bona fide physiological substrates**. RAF phosphorylation of two activation-loop serines activates MEK, after which MEK—being a dual-specificity kinase—phosphorylates ERK1/2. Canonical site assignments are MEK1 Ser218/Ser222 and MEK2 Ser222/Ser226, although some older sources use alternative numbering conventions; the robust annotation is therefore dual activation-loop serine phosphorylation rather than dependence on one numbering system. (matallanas2011raffamilykinases pages 8-9, roskoski2010rafproteinserinethreoninekinases pages 2-3, bahar2023targetingtherasrafmapk pages 6-7)

All three RAF proteins can bind and phosphorylate MEK in vitro, but BRAF generally has much higher intrinsic MEK-kinase activity than CRAF. RAF1 should consequently be annotated as a regulated MEK kinase and signaling/dimerization component, not as a broadly promiscuous serine kinase. (matallanas2011raffamilykinases pages 8-9, maurer2011rafkinasesin pages 1-2)

Reported non-MEK targets include BAD, adenylyl cyclases, RB, MYPT and cardiac troponin T. Their physiological validation is not equivalent to that of MEK1/2. In particular, mitochondrial BAD phosphorylation has experimental support in selected systems, but reviews also describe BAD, ASK1 and MST2 as apoptosis-related RAF1 effectors without consistently establishing direct phosphotransfer; ASK1 and MST2 inhibition is often interaction- or scaffold-mediated. (matallanas2011raffamilykinases pages 8-9, bahar2023targetingtherasrafmapk pages 9-10, riaud2024theroleof pages 5-6)

## 3. Regulatory cycle and pathway position

### 3.1 Basal autoinhibition

In unstimulated cells, RAF1 is principally a closed, inactive cytosolic monomer. Intramolecular contacts between its regulatory and kinase regions, inhibitory phosphorylation, and a 14-3-3 dimer spanning the N- and C-terminal phosphoserine sites stabilize this state. Ser259 is particularly important for N-terminal 14-3-3 engagement. RAF1 also depends strongly on the **HSP90–CDC37** chaperone system for folding and protein stability. (spencersmith2024regulationofraf pages 6-7, riaud2024theroleof pages 1-2, spencersmith2024regulationofraf pages 1-3)

### 3.2 RAS-dependent activation

Growth-factor receptor signaling loads RAS with GTP. RAS-GTP recruits RAF1 to the inner plasma membrane through the RBD, while the CRD contacts RAS and phosphatidylserine-rich membrane surfaces. These interactions orient RAF1 and promote release of autoinhibition rather than merely increasing bulk RAS affinity. (spencersmith2024regulationofraf pages 6-7, riaud2024theroleof pages 1-2)

The **MRAS–SHOC2–PP1C** phosphatase complex facilitates dephosphorylation of inhibitory Ser259. Rearrangement of 14-3-3, phosphorylation of activating regulatory sites, kinase-domain conformational changes, and formation of RAF1–RAF1 or RAF1–BRAF/ARAF dimers then produce the active state. The active RAF complex phosphorylates MEK1/2, which activate ERK1/2 and downstream cytoplasmic and nuclear responses. (riaud2024theroleof pages 1-2, spencersmith2024regulationofraf pages 1-3)

RAF1 is subsequently constrained by ERK-dependent feedback, inhibitory phosphorylation, phosphatases and complex disassembly. Ser642 is one reported ERK-feedback site; Ser621 supports 14-3-3 binding and RAF1 stability/MEK-kinase competence. The effects of individual sites remain context-dependent rather than constituting a simple linear activation code. (riaud2024theroleof pages 5-6)

### 3.3 Biological pathway

The canonical sequence is:

**RTK → RAS-GTP → RAF1-containing RAF dimer → MEK1/2 → ERK1/2 → changes in proliferation, differentiation, survival, migration and metabolism.**

RAF1 is therefore a signaling relay between membrane-associated RAS and the core MAPK kinase module. It is not the kinase that directly phosphorylates ERK; MEK performs that reaction. (riaud2024theroleof pages 1-2, bahar2023targetingtherasrafmapk pages 6-7)

## 4. Subcellular localization

### Canonical location

Basal RAF1 is predominantly cytosolic. Following RAS activation, it is transiently recruited to the **cytoplasmic face of the plasma membrane**, the principal compartment in which canonical RAF dimerization and MEK activation occur. Forced membrane retention can generate constitutive, partly RAS-independent signaling, underscoring the functional importance of localization. Recent live-cell analyses support signaling from plasma-membrane-associated RAS–RAF assemblies rather than internalized EGF-receptor endosomes in the examined setting. (bahar2023targetingtherasrafmapk pages 5-6, jeon2024signalingfromras pages 18-20, berlinska2025unravellingkrasbiology pages 10-13)

### Context-specific mitochondrial location

A distinct RAF1 pool can translocate to mitochondria following PAK-dependent Ser338/Ser339 phosphorylation or interaction with BCL-2. At mitochondria, RAF1 participates in anti-apoptotic signaling, including reported BAD inactivation and binding-mediated suppression of ASK1/MST2 pathways. This localization is stimulus- and cell-context-dependent and should not replace the plasma membrane as RAF1’s primary canonical signaling site. (riaud2024theroleof pages 5-6, wang2023targetingcrafkinase pages 14-15)

Evidence retrieved here does not justify treating nuclear, Golgi or endosomal RAF1 as universal functional locations. Observations involving engineered CAAX-tagged RAF constructs suggest possible ER/Golgi trafficking but do not establish a canonical endogenous human RAF1 compartment. (berlinska2025unravellingkrasbiology pages 58-60, berlinska2025unravellingkrasbiology pages 44-48)

## 5. Kinase-independent functions

RAF1’s protein scaffold can be biologically important independently of phosphotransfer. Documented functions include binding and inhibition of the pro-apoptotic kinases **ASK1** and **MST2**, organization of RAF dimers, and support of proliferation or survival in KRAS-driven tumor models even when RAF1 catalytic activity is dispensable. In some models, deleting RAF1 produces a stronger phenotype than rendering its kinase inactive, indicating that protein abundance and interaction surfaces—not simply ATP-site activity—are the relevant dependency. (riaud2024theroleof pages 5-6, bahar2023targetingtherasrafmapk pages 9-10, wang2023targetingcrafkinase pages 15-16)

This dual catalytic/scaffold character explains why selective inhibition of RAF1 kinase activity has produced inconsistent results and why degradation or disruption of specific RAF1 protein interactions is being considered. It also cautions against using reduced ERK phosphorylation as the sole measure of RAF1 biological inhibition. (riaud2024theroleof pages 16-16, wang2023targetingcrafkinase pages 1-2)

## 6. Human disease relevance

### 6.1 Germline disorders

Pathogenic germline RAF1 variants cause RASopathies, particularly **Noonan syndrome 5**, Noonan syndrome, and Noonan syndrome with multiple lentigines/LEOPARD syndrome 2; disease databases also associate RAF1 with cardiomyopathy. (OpenTargets Search: -RAF1)

Many pathogenic variants cluster near regulatory regions, including the N-terminal 14-3-3 site, and weaken autoinhibition. However, RAF1 RASopathy mechanisms are allele-specific: **G361A** is a high-activity mutant, whereas **D486N** is catalytically impaired yet can enhance MEK–ERK signaling through BRAF heterodimerization. RAF1-associated Noonan syndrome has a notable association with hypertrophic cardiomyopathy, so variants should not be interpreted solely from intrinsic kinase activity. (spencersmith2024regulationofraf pages 6-7, wang2023targetingcrafkinase pages 14-15, riaud2024theroleof pages 9-10)

### 6.2 Cancer alterations and statistics

Somatic RAF1 activation occurs through point mutations, amplification, fusions, overexpression and adaptive recruitment downstream of oncogenic RAS. Estimates vary with cohort and alteration definition: reviews report activating mutation frequencies near **0.7%**, whereas one TCGA-oriented analysis reported RAF1 mutations in **2.3% of cancers**. Examples include **5.41% (24/444)** in cutaneous melanoma and **4.54% (24/529)** in uterine endometrial carcinoma. RAF1 amplification was reported in **10.71% (44/411)** of a TCGA bladder-cancer cohort and **3.8% (139/3,844)** in GENIE v3. (wang2023targetingcrafkinase pages 14-15, wang2023targetingcrafkinase pages 15-16, riaud2024theroleof pages 7-8)

RAF1 fusions occur in several cancers and may be especially enriched in pancreatic acinar-cell carcinoma—reported at up to **18.5%**—but generally occur around **0.5–1%** in prostate cancer, melanoma and pancreatic cancers considered more broadly. Named fusions include QKI–RAF1, GOLGA4–RAF1, ATG7–RAF1, LRRFIP2–RAF1 and MTAP–RAF1. (riaud2024theroleof pages 6-7, wang2023targetingcrafkinase pages 15-16, riaud2024theroleof pages 16-16)

Functionally characterized activating or resistance-associated variants include **S257L/P, S259 substitutions, P261 substitutions, G361A/R/S, R391W and E478K**. Many disrupt inhibitory regulation or enhance dimer-dependent signaling. G361A can signal with relative RAS independence, whereas numerous other high-activity mutants remain dimer- and RAS-dependent. In a 2024 synthesis, 9% of tumors carrying oncogenic RAF1 mutations also had oncogenic BRAF alterations, nearly all non-V600. (riaud2024theroleof pages 9-10, riaud2024theroleof pages 10-11, riaud2024theroleof pages 8-9)

RAF1 also mediates acquired resistance without a primary RAF1 driver: increased CRAF expression or RTK–RAS–CRAF signaling can bypass BRAF inhibition; RAF1 mutations and fusions can contribute to KRAS-G12C-inhibitor resistance; and RAF1 amplification has appeared during trametinib resistance. (riaud2024theroleof pages 10-11)

## 7. Recent developments, 2023–2024

### Regulatory and structural understanding

Two authoritative 2024 reviews emphasized that RAF activation is an integrated transition among 14-3-3-bound autoinhibited monomers, RAS/membrane-associated intermediates and active dimers, rather than a simple recruitment event. They also highlighted RAF1’s stronger dependence on HSP90–CDC37 and mechanistic differences between CRAF and BRAF—important because many earlier structural conclusions were extrapolated from BRAF. (spencersmith2024regulationofraf pages 6-7, spencersmith2024regulationofraf pages 1-3)

The 2024 RAS-to-RAF synthesis further framed the functional switch as a multiprotein assembly involving RAF, its MEK substrate and 14-3-3. This model helps explain why mutations, dimerization and ATP-site inhibitors can produce nonintuitive outcomes, including transactivation and paradoxical ERK signaling. (jeon2024signalingfromras pages 18-20)

### Cancer biology

The 2024 *Nature Reviews Cancer* analysis concluded that CRAF contributes to tumor progression through both MAPK-dependent and MAPK-independent mechanisms and is increasingly relevant as a resistance node. It also stressed that “RAF1 alteration” is not one biomarker class: high-activity mutations, low-activity dimer-promoting mutations, fusions and amplifications may require different therapeutic combinations. (riaud2024theroleof pages 5-6, riaud2024theroleof pages 13-14)

## 8. Applications and therapeutic implementation

### Established clinical practice

RAF-pathway inhibitors are clinically established for selected **BRAF-driven** malignancies, but these are not selective RAF1 therapies. As of the reviewed 2023–2024 literature, **no selective RAF1/CRAF inhibitor had regulatory approval**. Vemurafenib, dabrafenib and encorafenib target BRAF-mutant disease; sorafenib is a multikinase inhibitor. Their clinical use should not be described as direct validation of RAF1-selective therapy. (scardaci2024novelraf‐directedapproaches pages 2-3, wang2023targetingcrafkinase pages 1-2)

First-generation BRAF inhibitors can promote RAF1 homodimerization or BRAF–RAF1 heterodimerization in RAS-active, BRAF-wild-type cells, causing **paradoxical MEK–ERK activation**. This is a central reason that BRAF-V600-selective drugs are unsuitable as generic RAF1 inhibitors. (wang2023targetingcrafkinase pages 21-23, scardaci2024novelraf‐directedapproaches pages 2-3)

### Investigational strategies

Type-II pan-RAF or RAF-dimer inhibitors—including **belvarafenib, lifirafenib, naporafenib, tovorafenib, LY3009120, LXH254 and exarafenib**—are designed to inhibit RAF dimers while reducing paradoxical activation. Pan-RAF combinations with MEK, ERK, EGFR, SHP2, CDK4/6 or immunotherapy are being explored according to genotype and resistance mechanism. (riaud2024theroleof pages 13-14, riaud2024theroleof pages 11-12, riaud2024theroleof pages 17-17)

Clinical activity remains heterogeneous. Across early trials summarized in 2024, reported response rates ranged from **0% for LY3009120 to 64% for tovorafenib**, but populations and biomarkers differed and these values cannot be interpreted as RAF1-specific efficacy. A MEK–RAF inhibitor, CH5126766, produced objective responses in **27% of 26 evaluable patients** in phase I study NCT02407509. A retrospective report of 13 RAF1-altered tumors treated with MAPK-targeted combinations observed a **69% response rate**, although the review explicitly cautioned that publication bias likely inflated this estimate. (wang2023targetingcrafkinase pages 21-23, riaud2024theroleof pages 11-12, riaud2024theroleof pages 10-11)

A major emerging idea is **RAF1 degradation**, because removing the protein could eliminate both catalytic and scaffold functions. In 2023–2024 this remained a preclinical rationale rather than a validated clinical implementation; most published RAF degraders were BRAF-directed, and selective RAF1 degradation had not reached an established therapeutic standard. (scardaci2024novelraf‐directedapproaches pages 2-3, wang2023targetingcrafkinase pages 1-2)

## 9. Expert interpretation and annotation confidence

1. **Primary molecular function—high confidence:** ATP-dependent serine phosphorylation of MEK1/2 in the RAS–RAF–MEK–ERK cascade. (matallanas2011raffamilykinases pages 8-9, roskoski2010rafproteinserinethreoninekinases pages 2-3)
2. **Primary site of canonical action—high confidence:** the inner plasma membrane after recruitment from an inactive cytosolic pool by RAS-GTP. (riaud2024theroleof pages 1-2, bahar2023targetingtherasrafmapk pages 5-6)
3. **Regulatory mechanism—high confidence:** autoinhibition by regulatory-domain/kinase-domain contacts and 14-3-3, relieved by membrane engagement, Ser259 dephosphorylation, conformational remodeling and RAF dimerization. (spencersmith2024regulationofraf pages 6-7, riaud2024theroleof pages 1-2)
4. **Noncatalytic/scaffold function—moderate-to-high confidence:** substantial genetic and biochemical support exists, especially for apoptosis control and KRAS-driven tumor maintenance, but its magnitude is tissue- and model-dependent. (riaud2024theroleof pages 5-6, riaud2024theroleof pages 16-16)
5. **Alternative direct substrates—lower confidence:** BAD and other proposed proteins should be annotated as context-dependent or provisional rather than equivalent to MEK1/2. (matallanas2011raffamilykinases pages 8-9, riaud2024theroleof pages 5-6)
6. **Therapeutic tractability—emerging:** RAF1 is actionable biologically, but kinase inhibition alone may not remove its scaffold functions. Biomarker-defined pan-RAF combinations and eventual RAF1-directed degraders are more mechanistically compelling than indiscriminate CRAF ATP-site inhibition, but clinical validation remains incomplete. (riaud2024theroleof pages 13-14, wang2023targetingcrafkinase pages 1-2)

## Key recent sources

- Riaud M. et al. **“The role of CRAF in cancer progression: from molecular mechanisms to precision therapies.”** *Nature Reviews Cancer* 24, 105–122. Published January 2024. https://doi.org/10.1038/s41568-023-00650-x (riaud2024theroleof pages 1-2, riaud2024theroleof pages 13-14)
- Spencer-Smith R., Morrison D.K. **“Regulation of RAF family kinases: new insights from recent structural and biochemical studies.”** *Biochemical Society Transactions* 52, 1061–1069. Published May 2024. https://doi.org/10.1042/BST20230552 (spencersmith2024regulationofraf pages 6-7, spencersmith2024regulationofraf pages 1-3)
- Jeon H., Tkacik E., Eck M.J. **“Signaling from RAS to RAF: The Molecules and Their Mechanisms.”** *Annual Review of Biochemistry* 93, 289–316. Published 2024. https://doi.org/10.1146/annurev-biochem-052521-040754 (jeon2024signalingfromras pages 18-20)
- Scardaci R. et al. **“Novel RAF-directed approaches to overcome current clinical limits and block the RAS/RAF node.”** *Molecular Oncology* 18, 1355–1377. Published February 2024. https://doi.org/10.1002/1878-0261.13605 (scardaci2024novelraf‐directedapproaches pages 1-2, scardaci2024novelraf‐directedapproaches pages 2-3)
- Wang P. et al. **“Targeting CRAF kinase in anti-cancer therapy: progress and opportunities.”** *Molecular Cancer* 22. Published December 2023. https://doi.org/10.1186/s12943-023-01903-x (wang2023targetingcrafkinase pages 1-2, wang2023targetingcrafkinase pages 21-23)
- Bahar M.E. et al. **“Targeting the RAS/RAF/MAPK pathway for cancer therapy: from mechanism to clinical studies.”** *Signal Transduction and Targeted Therapy* 8. Published December 2023. https://doi.org/10.1038/s41392-023-01705-z (bahar2023targetingtherasrafmapk pages 6-7, bahar2023targetingtherasrafmapk pages 5-6)

References

1. (riaud2024theroleof pages 1-2): Melody Riaud, Jennifer Maxwell, Isabel Soria-Bretones, Matthew Dankner, Meredith Li, and April A. N. Rose. The role of craf in cancer progression: from molecular mechanisms to precision therapies. Nature reviews. Cancer, 24:105-122, Jan 2024. URL: https://doi.org/10.1038/s41568-023-00650-x, doi:10.1038/s41568-023-00650-x. This article has 53 citations.

2. (spencersmith2024regulationofraf pages 1-3): Russell Spencer-Smith and Deborah K. Morrison. Regulation of raf family kinases: new insights from recent structural and biochemical studies. Biochemical Society Transactions, 52:1061-1069, May 2024. URL: https://doi.org/10.1042/bst20230552, doi:10.1042/bst20230552. This article has 24 citations and is from a peer-reviewed journal.

3. (matallanas2011raffamilykinases pages 8-9): D. Matallanas, M. Birtwistle, D. Romano, A. Zebisch, J. Rauch, A. von Kriegsheim, and W. Kolch. Raf family kinases: old dogs have learned new tricks. Genes & cancer, 2 3:232-60, Mar 2011. URL: https://doi.org/10.1177/1947601911407323, doi:10.1177/1947601911407323. This article has 543 citations.

4. (roskoski2010rafproteinserinethreoninekinases pages 2-3): Robert Roskoski. Raf protein-serine/threonine kinases: structure and regulation. Biochemical and Biophysical Research Communications, 399(3):313-317, Aug 2010. URL: https://doi.org/10.1016/j.bbrc.2010.07.092, doi:10.1016/j.bbrc.2010.07.092. This article has 540 citations and is from a peer-reviewed journal.

5. (bahar2023targetingtherasrafmapk pages 9-10): Md Entaz Bahar, Hyun Joon Kim, and D. Kim. Targeting the ras/raf/mapk pathway for cancer therapy: from mechanism to clinical studies. Signal Transduction and Targeted Therapy, Dec 2023. URL: https://doi.org/10.1038/s41392-023-01705-z, doi:10.1038/s41392-023-01705-z. This article has 1155 citations and is from a peer-reviewed journal.

6. (wang2023targetingcrafkinase pages 1-2): Penglei Wang, Kyle Laster, Xuechao Jia, Zigang Dong, and Kangdong Liu. Targeting craf kinase in anti-cancer therapy: progress and opportunities. Molecular Cancer, Dec 2023. URL: https://doi.org/10.1186/s12943-023-01903-x, doi:10.1186/s12943-023-01903-x. This article has 34 citations and is from a highest quality peer-reviewed journal.

7. (scardaci2024novelraf‐directedapproaches pages 1-2): Rossella Scardaci, Ewa Berlinska, Pietro Scaparone, Sandra Vietti Michelina, Edoardo Garbo, Silvia Novello, David Santamaria, and Chiara Ambrogio. Novel raf‐directed approaches to overcome current clinical limits and block the ras/raf node. Molecular Oncology, 18:1355-1377, Feb 2024. URL: https://doi.org/10.1002/1878-0261.13605, doi:10.1002/1878-0261.13605. This article has 26 citations and is from a peer-reviewed journal.

8. (bahar2023targetingtherasrafmapk pages 6-7): Md Entaz Bahar, Hyun Joon Kim, and D. Kim. Targeting the ras/raf/mapk pathway for cancer therapy: from mechanism to clinical studies. Signal Transduction and Targeted Therapy, Dec 2023. URL: https://doi.org/10.1038/s41392-023-01705-z, doi:10.1038/s41392-023-01705-z. This article has 1155 citations and is from a peer-reviewed journal.

9. (riaud2024theroleof pages 5-6): Melody Riaud, Jennifer Maxwell, Isabel Soria-Bretones, Matthew Dankner, Meredith Li, and April A. N. Rose. The role of craf in cancer progression: from molecular mechanisms to precision therapies. Nature reviews. Cancer, 24:105-122, Jan 2024. URL: https://doi.org/10.1038/s41568-023-00650-x, doi:10.1038/s41568-023-00650-x. This article has 53 citations.

10. (spencersmith2024regulationofraf pages 6-7): Russell Spencer-Smith and Deborah K. Morrison. Regulation of raf family kinases: new insights from recent structural and biochemical studies. Biochemical Society Transactions, 52:1061-1069, May 2024. URL: https://doi.org/10.1042/bst20230552, doi:10.1042/bst20230552. This article has 24 citations and is from a peer-reviewed journal.

11. (bahar2023targetingtherasrafmapk pages 5-6): Md Entaz Bahar, Hyun Joon Kim, and D. Kim. Targeting the ras/raf/mapk pathway for cancer therapy: from mechanism to clinical studies. Signal Transduction and Targeted Therapy, Dec 2023. URL: https://doi.org/10.1038/s41392-023-01705-z, doi:10.1038/s41392-023-01705-z. This article has 1155 citations and is from a peer-reviewed journal.

12. (jeon2024signalingfromras pages 18-20): Hyesung Jeon, Emre Tkacik, and Michael J. Eck. Signaling from ras to raf: the molecules and their mechanisms. Aug 2024. URL: https://doi.org/10.1146/annurev-biochem-052521-040754, doi:10.1146/annurev-biochem-052521-040754. This article has 73 citations and is from a domain leading peer-reviewed journal.

13. (wang2023targetingcrafkinase pages 14-15): Penglei Wang, Kyle Laster, Xuechao Jia, Zigang Dong, and Kangdong Liu. Targeting craf kinase in anti-cancer therapy: progress and opportunities. Molecular Cancer, Dec 2023. URL: https://doi.org/10.1186/s12943-023-01903-x, doi:10.1186/s12943-023-01903-x. This article has 34 citations and is from a highest quality peer-reviewed journal.

14. (wang2023targetingcrafkinase pages 15-16): Penglei Wang, Kyle Laster, Xuechao Jia, Zigang Dong, and Kangdong Liu. Targeting craf kinase in anti-cancer therapy: progress and opportunities. Molecular Cancer, Dec 2023. URL: https://doi.org/10.1186/s12943-023-01903-x, doi:10.1186/s12943-023-01903-x. This article has 34 citations and is from a highest quality peer-reviewed journal.

15. (OpenTargets Search: -RAF1): Open Targets Query (-RAF1, 10 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

16. (riaud2024theroleof pages 9-10): Melody Riaud, Jennifer Maxwell, Isabel Soria-Bretones, Matthew Dankner, Meredith Li, and April A. N. Rose. The role of craf in cancer progression: from molecular mechanisms to precision therapies. Nature reviews. Cancer, 24:105-122, Jan 2024. URL: https://doi.org/10.1038/s41568-023-00650-x, doi:10.1038/s41568-023-00650-x. This article has 53 citations.

17. (riaud2024theroleof pages 6-7): Melody Riaud, Jennifer Maxwell, Isabel Soria-Bretones, Matthew Dankner, Meredith Li, and April A. N. Rose. The role of craf in cancer progression: from molecular mechanisms to precision therapies. Nature reviews. Cancer, 24:105-122, Jan 2024. URL: https://doi.org/10.1038/s41568-023-00650-x, doi:10.1038/s41568-023-00650-x. This article has 53 citations.

18. (riaud2024theroleof pages 7-8): Melody Riaud, Jennifer Maxwell, Isabel Soria-Bretones, Matthew Dankner, Meredith Li, and April A. N. Rose. The role of craf in cancer progression: from molecular mechanisms to precision therapies. Nature reviews. Cancer, 24:105-122, Jan 2024. URL: https://doi.org/10.1038/s41568-023-00650-x, doi:10.1038/s41568-023-00650-x. This article has 53 citations.

19. (wang2023targetingcrafkinase pages 21-23): Penglei Wang, Kyle Laster, Xuechao Jia, Zigang Dong, and Kangdong Liu. Targeting craf kinase in anti-cancer therapy: progress and opportunities. Molecular Cancer, Dec 2023. URL: https://doi.org/10.1186/s12943-023-01903-x, doi:10.1186/s12943-023-01903-x. This article has 34 citations and is from a highest quality peer-reviewed journal.

20. (riaud2024theroleof pages 11-12): Melody Riaud, Jennifer Maxwell, Isabel Soria-Bretones, Matthew Dankner, Meredith Li, and April A. N. Rose. The role of craf in cancer progression: from molecular mechanisms to precision therapies. Nature reviews. Cancer, 24:105-122, Jan 2024. URL: https://doi.org/10.1038/s41568-023-00650-x, doi:10.1038/s41568-023-00650-x. This article has 53 citations.

21. (scardaci2024novelraf‐directedapproaches pages 2-3): Rossella Scardaci, Ewa Berlinska, Pietro Scaparone, Sandra Vietti Michelina, Edoardo Garbo, Silvia Novello, David Santamaria, and Chiara Ambrogio. Novel raf‐directed approaches to overcome current clinical limits and block the ras/raf node. Molecular Oncology, 18:1355-1377, Feb 2024. URL: https://doi.org/10.1002/1878-0261.13605, doi:10.1002/1878-0261.13605. This article has 26 citations and is from a peer-reviewed journal.

22. (riaud2024theroleof pages 10-11): Melody Riaud, Jennifer Maxwell, Isabel Soria-Bretones, Matthew Dankner, Meredith Li, and April A. N. Rose. The role of craf in cancer progression: from molecular mechanisms to precision therapies. Nature reviews. Cancer, 24:105-122, Jan 2024. URL: https://doi.org/10.1038/s41568-023-00650-x, doi:10.1038/s41568-023-00650-x. This article has 53 citations.

23. (maurer2011rafkinasesin pages 1-2): Gabriele Maurer, B. Tarkowski, and M. Baccarini. Raf kinases in cancer–roles and therapeutic opportunities. Oncogene, 30:3477-3488, Aug 2011. URL: https://doi.org/10.1038/onc.2011.160, doi:10.1038/onc.2011.160. This article has 412 citations and is from a domain leading peer-reviewed journal.

24. (berlinska2025unravellingkrasbiology pages 10-13): E Berlinska. Unravelling kras biology: characterization of the kras-raf signalosome and its functional dynamics at the cell membrane. Unknown journal, 2025.

25. (berlinska2025unravellingkrasbiology pages 58-60): E Berlinska. Unravelling kras biology: characterization of the kras-raf signalosome and its functional dynamics at the cell membrane. Unknown journal, 2025.

26. (berlinska2025unravellingkrasbiology pages 44-48): E Berlinska. Unravelling kras biology: characterization of the kras-raf signalosome and its functional dynamics at the cell membrane. Unknown journal, 2025.

27. (riaud2024theroleof pages 16-16): Melody Riaud, Jennifer Maxwell, Isabel Soria-Bretones, Matthew Dankner, Meredith Li, and April A. N. Rose. The role of craf in cancer progression: from molecular mechanisms to precision therapies. Nature reviews. Cancer, 24:105-122, Jan 2024. URL: https://doi.org/10.1038/s41568-023-00650-x, doi:10.1038/s41568-023-00650-x. This article has 53 citations.

28. (riaud2024theroleof pages 8-9): Melody Riaud, Jennifer Maxwell, Isabel Soria-Bretones, Matthew Dankner, Meredith Li, and April A. N. Rose. The role of craf in cancer progression: from molecular mechanisms to precision therapies. Nature reviews. Cancer, 24:105-122, Jan 2024. URL: https://doi.org/10.1038/s41568-023-00650-x, doi:10.1038/s41568-023-00650-x. This article has 53 citations.

29. (riaud2024theroleof pages 13-14): Melody Riaud, Jennifer Maxwell, Isabel Soria-Bretones, Matthew Dankner, Meredith Li, and April A. N. Rose. The role of craf in cancer progression: from molecular mechanisms to precision therapies. Nature reviews. Cancer, 24:105-122, Jan 2024. URL: https://doi.org/10.1038/s41568-023-00650-x, doi:10.1038/s41568-023-00650-x. This article has 53 citations.

30. (riaud2024theroleof pages 17-17): Melody Riaud, Jennifer Maxwell, Isabel Soria-Bretones, Matthew Dankner, Meredith Li, and April A. N. Rose. The role of craf in cancer progression: from molecular mechanisms to precision therapies. Nature reviews. Cancer, 24:105-122, Jan 2024. URL: https://doi.org/10.1038/s41568-023-00650-x, doi:10.1038/s41568-023-00650-x. This article has 53 citations.

## Artifacts

- [Edison artifact artifact-00](RAF1-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. riaud2024theroleof pages 5-6
2. riaud2024theroleof pages 10-11
3. jeon2024signalingfromras pages 18-20
4. riaud2024theroleof pages 1-2
5. spencersmith2024regulationofraf pages 1-3
6. matallanas2011raffamilykinases pages 8-9
7. roskoski2010rafproteinserinethreoninekinases pages 2-3
8. bahar2023targetingtherasrafmapk pages 9-10
9. wang2023targetingcrafkinase pages 1-2
10. bahar2023targetingtherasrafmapk pages 6-7
11. spencersmith2024regulationofraf pages 6-7
12. bahar2023targetingtherasrafmapk pages 5-6
13. wang2023targetingcrafkinase pages 14-15
14. wang2023targetingcrafkinase pages 15-16
15. riaud2024theroleof pages 9-10
16. riaud2024theroleof pages 6-7
17. riaud2024theroleof pages 7-8
18. wang2023targetingcrafkinase pages 21-23
19. riaud2024theroleof pages 11-12
20. maurer2011rafkinasesin pages 1-2
21. berlinska2025unravellingkrasbiology pages 10-13
22. berlinska2025unravellingkrasbiology pages 58-60
23. berlinska2025unravellingkrasbiology pages 44-48
24. riaud2024theroleof pages 16-16
25. riaud2024theroleof pages 8-9
26. riaud2024theroleof pages 13-14
27. riaud2024theroleof pages 17-17
28. https://doi.org/10.1038/s41568-023-00650-x
29. https://doi.org/10.1042/BST20230552
30. https://doi.org/10.1146/annurev-biochem-052521-040754
31. https://doi.org/10.1002/1878-0261.13605
32. https://doi.org/10.1186/s12943-023-01903-x
33. https://doi.org/10.1038/s41392-023-01705-z
34. https://doi.org/10.1038/s41568-023-00650-x,
35. https://doi.org/10.1042/bst20230552,
36. https://doi.org/10.1177/1947601911407323,
37. https://doi.org/10.1016/j.bbrc.2010.07.092,
38. https://doi.org/10.1038/s41392-023-01705-z,
39. https://doi.org/10.1186/s12943-023-01903-x,
40. https://doi.org/10.1002/1878-0261.13605,
41. https://doi.org/10.1146/annurev-biochem-052521-040754,
42. https://doi.org/10.1038/onc.2011.160,