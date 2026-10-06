---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-30T05:42:00.265119'
end_time: '2026-09-30T05:57:07.967478'
duration_seconds: 907.7
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: FGFR1
  gene_symbol: FGFR1
  uniprot_accession: P11362
  protein_description: 'RecName: Full=Fibroblast growth factor receptor 1; Short=FGFR-1;
    EC=2.7.10.1 {ECO:0000269|PubMed:1379697, ECO:0000269|PubMed:15117958, ECO:0000269|PubMed:18480409,
    ECO:0000269|PubMed:19224897, ECO:0000269|PubMed:19665973, ECO:0000269|PubMed:20133753,
    ECO:0000269|PubMed:8622701}; AltName: Full=Basic fibroblast growth factor receptor
    1; Short=BFGFR; Short=bFGF-R-1; AltName: Full=Fms-like tyrosine kinase 2; Short=FLT-2;
    AltName: Full=N-sam; AltName: CD_antigen=CD331; Flags: Precursor;'
  gene_info: Name=FGFR1; Synonyms=BFGFR, CEK, FGFBR, FLG, FLT2, HBGFR;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the protein kinase superfamily. Tyr protein
  protein_domains: FGF_rcpt_1. (IPR028174); FGF_rcpt_fam. (IPR016248); Ig-like_dom.
    (IPR007110); Ig-like_dom_sf. (IPR036179); Ig-like_fold. (IPR013783)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 38
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: FGFR1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: FGFR1-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P11362
- **Protein Description:** RecName: Full=Fibroblast growth factor receptor 1; Short=FGFR-1; EC=2.7.10.1 {ECO:0000269|PubMed:1379697, ECO:0000269|PubMed:15117958, ECO:0000269|PubMed:18480409, ECO:0000269|PubMed:19224897, ECO:0000269|PubMed:19665973, ECO:0000269|PubMed:20133753, ECO:0000269|PubMed:8622701}; AltName: Full=Basic fibroblast growth factor receptor 1; Short=BFGFR; Short=bFGF-R-1; AltName: Full=Fms-like tyrosine kinase 2; Short=FLT-2; AltName: Full=N-sam; AltName: CD_antigen=CD331; Flags: Precursor;
- **Gene Information:** Name=FGFR1; Synonyms=BFGFR, CEK, FGFBR, FLG, FLT2, HBGFR;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the protein kinase superfamily. Tyr protein
- **Key Domains:** FGF_rcpt_1. (IPR028174); FGF_rcpt_fam. (IPR016248); Ig-like_dom. (IPR007110); Ig-like_dom_sf. (IPR036179); Ig-like_fold. (IPR013783)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "FGFR1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'FGFR1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **FGFR1** (gene ID: FGFR1, UniProt: P11362) in human.

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
- **UniProt Accession:** P11362
- **Protein Description:** RecName: Full=Fibroblast growth factor receptor 1; Short=FGFR-1; EC=2.7.10.1 {ECO:0000269|PubMed:1379697, ECO:0000269|PubMed:15117958, ECO:0000269|PubMed:18480409, ECO:0000269|PubMed:19224897, ECO:0000269|PubMed:19665973, ECO:0000269|PubMed:20133753, ECO:0000269|PubMed:8622701}; AltName: Full=Basic fibroblast growth factor receptor 1; Short=BFGFR; Short=bFGF-R-1; AltName: Full=Fms-like tyrosine kinase 2; Short=FLT-2; AltName: Full=N-sam; AltName: CD_antigen=CD331; Flags: Precursor;
- **Gene Information:** Name=FGFR1; Synonyms=BFGFR, CEK, FGFBR, FLG, FLT2, HBGFR;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the protein kinase superfamily. Tyr protein
- **Key Domains:** FGF_rcpt_1. (IPR028174); FGF_rcpt_fam. (IPR016248); Ig-like_dom. (IPR007110); Ig-like_dom_sf. (IPR036179); Ig-like_fold. (IPR013783)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "FGFR1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'FGFR1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **FGFR1** (gene ID: FGFR1, UniProt: P11362) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: FGFR1 (Fibroblast Growth Factor Receptor 1)

## Gene Identity and Overview

FGFR1 (UniProt ID: P11362) encodes fibroblast growth factor receptor 1, a receptor tyrosine kinase (EC 2.7.10.1) that belongs to the protein kinase superfamily and specifically to the tyrosine protein kinase family (fan2024pharmacologicalandbiological pages 1-2, zheng2022signalingpathwayand pages 1-2). The gene is also known by synonyms including BFGFR, CEK, FGFBR, FLG, FLT2, and HBGFR, and the protein is designated as CD331 (fan2024pharmacologicalandbiological pages 1-2). FGFR1 is one of four major FGF receptors (FGFR1-4) that transduce signals from fibroblast growth factors to regulate fundamental cellular processes (chen2025fgfbaseddrugdiscovery pages 2-4, chen2025fgfbaseddrugdiscovery pages 5-6).

## Structural Organization and Functional Domains

FGFR1 is organized as a single-pass transmembrane receptor tyrosine kinase consisting of three major regions (fan2024pharmacologicalandbiological pages 1-2, zheng2022signalingpathwayand pages 1-2, domenichini2025receptortyrosinekinases pages 9-12). The extracellular region comprises three immunoglobulin-like domains designated D1, D2, and D3, with an acidic box (a serine- and aspartate-rich sequence) located between D1 and D2 (fan2024pharmacologicalandbiological pages 1-2, nguyen2024thecomplexityand pages 6-8, nguyen2024thecomplexityand pages 4-6). The D2 and D3 domains, together with the linker between them, constitute the principal ligand-binding region and determine FGF-binding specificity, while D1 and the acidic box contribute to receptor autoinhibition in the absence of ligand (zheng2022signalingpathwayand pages 1-2, domenichini2025receptortyrosinekinases pages 9-12).

The receptor is anchored in the membrane by a single transmembrane helix that supports receptor dimerization (zheng2022signalingpathwayand pages 1-2). The intracellular region contains a bilobed tyrosine kinase domain of approximately 300 amino acids (zheng2022signalingpathwayand pages 1-2, zheng2022signalingpathwayand pages 2-5). The N-terminal lobe includes a five-stranded β-sheet, an αC helix, and a flexible glycine-rich P-loop that forms the ATP-binding site, while the C-terminal lobe contains multiple α-helices and key regulatory elements (zheng2022signalingpathwayand pages 2-5). Critical functional regions within the kinase domain include the ATP-binding pocket, the activation loop (A-loop) containing the DFG motif and phosphorylation sites Y653 and Y654, and the catalytic loop with the conserved HRD motif (zheng2022signalingpathwayand pages 2-5).

FGFR1 undergoes alternative splicing in the immunoglobulin-like domain III region, producing FGFR1b (IIIb) and FGFR1c (IIIc) isoforms that differ in ligand-binding specificity and tissue distribution (nguyen2024thecomplexityand pages 6-8, zheng2022signalingpathwayand pages 1-2, nguyen2024thecomplexityand pages 4-6). The IIIb isoform is predominantly expressed in epithelial tissues, while IIIc is found primarily in mesenchymal tissues (nguyen2024thecomplexityand pages 6-8, edirisinghe2024decodingfgffgfrsignaling pages 3-4).

## Primary Enzymatic Function and Catalytic Mechanism

### Tyrosine Kinase Activity

FGFR1 functions as an ATP-dependent protein tyrosine kinase that catalyzes the transfer of phosphate groups from ATP to tyrosine residues on protein substrates (zheng2022signalingpathwayand pages 2-5, yaronbarir2024theintrinsicsubstrate pages 19-22, zheng2022signalingpathwayand pages 1-2). The catalytic mechanism involves the HRD motif aspartate interacting with the hydroxyl group of the substrate tyrosine to facilitate phosphotransfer (zheng2022signalingpathwayand pages 2-5).

### Receptor Activation and Autophosphorylation

Activation occurs through a precisely orchestrated sequence of events (fan2024pharmacologicalandbiological pages 2-4, zheng2022signalingpathwayand pages 2-5, fan2024pharmacologicalandbiological pages 1-2). FGF ligand binding to the extracellular D2 and D3 domains, assisted by heparan sulfate proteoglycans (for paracrine FGFs) or Klotho proteins (for endocrine FGFs), promotes formation of a 2FGF:2FGFR1 complex and receptor dimerization (fan2024pharmacologicalandbiological pages 2-4, fan2024pharmacologicalandbiological pages 1-2, chen2025fgfbaseddrugdiscovery pages 5-6). Dimerization brings the intracellular kinase domains into proximity, enabling trans-autophosphorylation (zheng2022signalingpathwayand pages 2-5, fan2024pharmacologicalandbiological pages 1-2).

The kinase domain undergoes a conformational transition from an inactive DFG-out state to an active DFG-in state, in which the DFG aspartate is positioned to coordinate ATP and magnesium (fan2024pharmacologicalandbiological pages 2-4, zheng2022signalingpathwayand pages 2-5, fan2024pharmacologicalandbiological pages 1-2). The αC helix shifts from an αCout to αCin position, forming a stabilizing salt bridge with the β3-strand lysine, and the regulatory and catalytic spines align to stabilize the active conformation (fan2024pharmacologicalandbiological pages 2-4).

FGFR1 autophosphorylates multiple tyrosine residues in an ordered sequence, including Y463, Y583, Y585, Y653, Y654, Y730, and Y766 (zheng2022signalingpathwayand pages 2-5, palollathil2026proteomewideanalysisof pages 1-2). Phosphorylation of the activation-loop residues Y653 and Y654 is particularly critical, as it markedly increases substrate phosphorylation rates, relieves autoinhibition, and is essential for full catalytic activation (zheng2022signalingpathwayand pages 2-5, palollathil2026proteomewideanalysisof pages 1-2).

### Substrate Specificity and Direct Substrates

The primary physiological substrate of activated FGFR1 is FRS2α (FGFR substrate 2α), an adaptor protein that constitutively associates with the receptor's juxtamembrane region through its phosphotyrosine-binding domain (zheng2022signalingpathwayand pages 2-5). Upon FGFR1 activation, FRS2α is phosphorylated on multiple tyrosine residues, creating docking sites for downstream signaling proteins including SHP2, GRB2, GAB1, and SOS (zheng2022signalingpathwayand pages 2-5).

FGFR1 also directly phosphorylates PLCγ1 (phospholipase C gamma 1), which is recruited to the phosphorylated Y766 site on the activated receptor (palollathil2026proteomewideanalysisof pages 1-2, chen2025fgfbaseddrugdiscovery pages 5-6). Additional substrates and phosphorylation targets emerge through the formation of multi-protein signaling complexes (chen2025fgfbaseddrugdiscovery pages 5-6, zheng2022signalingpathwayand pages 2-5).

## Downstream Signaling Pathways and Molecular Mechanisms

FGFR1 activates four major intracellular signaling pathways that collectively regulate cell proliferation, survival, differentiation, migration, and metabolism. A comprehensive summary of these pathways is provided below.

| Pathway Name | Key Adaptor Proteins | Major Effector Molecules | Biological Outcomes |
|---|---|---|---|
| RAS–RAF–MEK–ERK (MAPK) | FGFR1 phosphorylates receptor-bound **FRS2α**, which recruits **GRB2–SOS1** and **SHP2**; CRKL can also participate in the FRS2α complex. | RAS-GTP → RAF → MEK1/2 → ERK1/2 → ETS-family and other transcription factors | Cell-cycle entry, proliferation, differentiation, developmental patterning, angiogenesis, and context-dependent migration; signal amplitude and duration help determine the response. (chen2025fgfbaseddrugdiscovery pages 5-6, zheng2022signalingpathwayand pages 2-5, edirisinghe2024decodingfgffgfrsignaling pages 1-3, clark2024diversefgfr1signalingpathwaysand pages 1-3) |
| PI3K–AKT–mTOR | Phosphorylated **FRS2α** recruits **GRB2**, which binds **GAB1** and thereby engages PI3K; related FRS2 complexes can also connect to CRK–DOCK1 signaling. | PI3K → PIP3 → AKT → mTORC1 and downstream survival/metabolic effectors; CDC42/RAC1 can support cytoskeletal responses. | Cell survival and anti-apoptotic signaling, growth, metabolism, proliferation, migration, cytoskeletal remodeling, and regenerative responses. (chen2025fgfbaseddrugdiscovery pages 5-6, zheng2022signalingpathwayand pages 2-5, edirisinghe2024decodingfgffgfrsignaling pages 1-3) |
| PLCγ1–PKC–Ca²⁺ | **PLCγ1** is recruited directly to activated FGFR1—particularly through the phosphorylated Y766 docking site—and is phosphorylated by the receptor. | PLCγ1 hydrolyzes PIP2 → IP3 + DAG; IP3 releases intracellular Ca²⁺, while DAG and Ca²⁺ activate PKC. | Calcium-dependent signaling, PKC activation, changes in motility and cytoskeletal organization, secretion, proliferation, and context-dependent tumor-cell migration or metastasis. (palollathil2026proteomewideanalysisof pages 1-2, chen2025fgfbaseddrugdiscovery pages 5-6, edirisinghe2024decodingfgffgfrsignaling pages 1-3) |
| JAK–STAT | This branch is less completely defined for FGFR1 than the FRS2α and PLCγ1 branches; receptor activation can engage JAK-associated signaling and promote STAT phosphorylation. | JAK-family kinases; STAT1, STAT3, and STAT5, which dimerize and translocate to the nucleus as transcription factors. | Transcriptional regulation of survival, proliferation, differentiation, inflammation, tissue repair, invasion, and—when dysregulated—tumor progression and immune evasion. (zheng2022signalingpathwayand pages 2-5, edirisinghe2024decodingfgffgfrsignaling pages 1-3, liu2023fgfrfamiliesbiological pages 2-4) |


*Table: This table maps the four principal FGFR1 signaling branches from receptor-associated adaptors to downstream effectors and biological outputs. It distinguishes the well-defined FRS2α- and PLCγ1-mediated mechanisms from the comparatively context-dependent JAK–STAT branch.*

### RAS–RAF–MEK–ERK (MAPK) Pathway

Following FGFR1 activation and FRS2α phosphorylation, the GRB2–SOS1 complex is recruited to FRS2α (chen2025fgfbaseddrugdiscovery pages 5-6, zheng2022signalingpathwayand pages 2-5, edirisinghe2024decodingfgffgfrsignaling pages 1-3). SOS1 functions as a guanine nucleotide exchange factor that activates RAS GTPases, initiating the RAF–MEK1/2–ERK1/2 kinase cascade (chen2025fgfbaseddrugdiscovery pages 5-6, edirisinghe2024decodingfgffgfrsignaling pages 1-3). Activated ERK1/2 phosphorylates transcription factors including ETS-family members, driving gene expression programs that promote cell proliferation, differentiation, angiogenesis, and developmental patterning (edirisinghe2024decodingfgffgfrsignaling pages 1-3, clark2024diversefgfr1signalingpathwaysand pages 1-3).

### PI3K–AKT–mTOR Pathway

The FRS2α–GRB2 complex recruits GAB1 (GRB2-associated binder 1), which activates phosphoinositide 3-kinase (PI3K) (chen2025fgfbaseddrugdiscovery pages 5-6, edirisinghe2024decodingfgffgfrsignaling pages 1-3, nguyen2024thecomplexityand pages 6-8). PI3K generates PIP3 (phosphatidylinositol 3,4,5-trisphosphate), leading to AKT activation and subsequent engagement of mTORC1 and other downstream effectors (chen2025fgfbaseddrugdiscovery pages 5-6). This pathway supports cell survival, growth, metabolism, and proliferation (chen2025fgfbaseddrugdiscovery pages 5-6, edirisinghe2024decodingfgffgfrsignaling pages 1-3, fan2024pharmacologicalandbiological pages 1-2). The FRS2α complex can also recruit CRK–DOCK1, which activates CDC42 and RAC1 GTPases to regulate cytoskeletal organization and cell migration (chen2025fgfbaseddrugdiscovery pages 5-6).

### PLCγ–PKC–Calcium Pathway

Direct phosphorylation of PLCγ1 by FGFR1 promotes its membrane recruitment and enzymatic activation (chen2025fgfbaseddrugdiscovery pages 5-6, edirisinghe2024decodingfgffgfrsignaling pages 1-3). PLCγ1 hydrolyzes PIP2 into inositol 1,4,5-trisphosphate (IP3) and diacylglycerol (DAG) (chen2025fgfbaseddrugdiscovery pages 5-6). IP3 triggers release of intracellular Ca²⁺ from the endoplasmic reticulum, while DAG and Ca²⁺ together activate protein kinase C (PKC) (chen2025fgfbaseddrugdiscovery pages 5-6, edirisinghe2024decodingfgffgfrsignaling pages 1-3). This pathway regulates calcium-dependent processes, cell motility, cytoskeletal remodeling, and context-dependent migration (chen2025fgfbaseddrugdiscovery pages 5-6).

### JAK–STAT Pathway

FGFR signaling can also activate the JAK–STAT pathway, leading to phosphorylation of STAT1, STAT3, and STAT5 transcription factors, which dimerize and translocate to the nucleus (zheng2022signalingpathwayand pages 2-5, edirisinghe2024decodingfgffgfrsignaling pages 1-3). This pathway contributes to transcriptional regulation of genes involved in proliferation, differentiation, inflammation, tissue repair, and—when aberrantly activated—tumor progression and immune evasion (zheng2022signalingpathwayand pages 2-5, edirisinghe2024decodingfgffgfrsignaling pages 1-3, liu2023fgfrfamiliesbiological pages 2-4).

## Subcellular Localization and Trafficking

FGFR1 exhibits complex subcellular trafficking that regulates its signaling output and biological function.

| Subcellular Compartment | Mechanism of Localization | Function at This Location | Key Regulatory Factors |
|---|---|---|---|
| Plasma membrane | Biosynthetic delivery places this single-pass receptor at the cell surface. Proper N-glycosylation of both D2 and D3 promotes efficient membrane trafficking; FGF and heparan sulfate stabilize receptor dimers and initiate trans-autophosphorylation. | Principal site of extracellular ligand recognition and canonical signaling through FRS2α, PLCγ1, RAS–ERK and PI3K–AKT. | D2 and D3 N-glycans; heparan-sulfate proteoglycans; FGF identity; receptor splice isoform; regulated anterograde transport. (nguyen2024thecomplexityand pages 6-8, fan2024pharmacologicalandbiological pages 1-2, edirisinghe2024decodingfgffgfrsignaling pages 3-4, chen2025fgfbaseddrugdiscovery pages 5-6) |
| Early and late endosomes | Activated or clustered FGFR1 is internalized, commonly through clathrin-mediated endocytosis, and sorted through EEA1-positive early and RAB7-positive later endosomes; receptors may recycle or proceed toward lysosomal degradation. | Regulates signal duration, spatial signaling, receptor recycling and signal termination; altered sorting can increase endosomal accumulation and modify developmental output. | Receptor phosphorylation and clustering; EPS15; CBL-mediated ubiquitination; endocytic regulators; Y730-associated protein interactions. (zheng2022signalingpathwayand pages 2-5, clark2024diversefgfr1signalingpathwaysand pages 12-13, domenichini2025receptortyrosinekinases pages 33-35, clark2024diversefgfr1signalingpathwaysand pages 1-3) |
| Nuclear envelope | Hypoglycosylated or secretion-impaired FGFR1 can be redirected from the secretory pathway to the nuclear envelope. D2 glycosylation suppresses nuclear-envelope accumulation, whereas combined D2 and D3 glycosylation favors plasma-membrane delivery. | Serves as a trafficking destination and potential noncanonical signaling compartment; nuclear-envelope-localized FGFR1 can exhibit ligand-independent autoactivation and a distinct interactome. | N-glycosylation status; receptor folding and endoplasmic-reticulum quality control; secretion efficiency; D2 and D3 glycan occupancy. (nguyen2024thecomplexityand pages 6-8, gregorczyk2023nglycosylationactsas pages 1-2) |
| Nucleus and nuclear lumen | Nuclear accumulation can involve FGF2-associated, importin-β-linked transport or proteolytic release of an intracellular FGFR1 fragment; the route is context dependent and remains incompletely resolved. | Supports chromatin-associated transcriptional regulation. FGFR1 occupies transcription-start regions and interacts with FOXA1, phosphorylated RNA polymerase II and transcriptional coactivators; in breast-cancer models, nuclear FGFR1 promotes proliferative programs and endocrine resistance. | FGF2; importin-β; RSK1; granzyme-B cleavage; FOXA1; p300 and CBP; reactive oxygen species; N-glycosylation. (suh2022nuclearlocalizationof pages 6-8, gregorczyk2023nglycosylationactsas pages 1-2, servetto2021nuclearfgfr1regulates pages 1-2, servetto2021nuclearfgfr1regulates pages 8-9, servetto2021nuclearfgfr1regulates pages 13-14) |
| Primary cilia | Emerging cell-biological evidence reports ciliary localization of FGFR1 and FGFR2, although trafficking mechanisms have been characterized more thoroughly for FGFR2; cilia are not considered the principal location of FGFR1. | May enable spatially restricted FGF sensing, but the FGFR1-specific physiological contribution remains less established than its plasma-membrane and endosomal functions. | Likely ciliary-entry and intraflagellar-transport machinery; FGFR1-specific determinants require further validation. |


*Table: FGFR1 functions principally at the plasma membrane but also traffics through endosomal, nuclear-envelope and nuclear compartments that alter signaling output. The table distinguishes established localization mechanisms from emerging evidence for primary-cilium residence.*

### Plasma Membrane Localization

The plasma membrane is the primary functional location of FGFR1, where the receptor binds extracellular FGF ligands and initiates canonical tyrosine kinase signaling (fan2024pharmacologicalandbiological pages 1-2, edirisinghe2024decodingfgffgfrsignaling pages 3-4, nguyen2024thecomplexityand pages 4-6, karl2024ligandbiasunderlies pages 2-4). Proper N-glycosylation of both the D2 and D3 extracellular domains is required for efficient trafficking from the endoplasmic reticulum and Golgi to the plasma membrane (nguyen2024thecomplexityand pages 6-8, fan2024pharmacologicalandbiological pages 1-2). Heparan sulfate proteoglycans at the cell surface act as coreceptors that facilitate FGF binding, receptor dimerization, and kinase activation (edirisinghe2024decodingfgffgfrsignaling pages 3-4, chen2025fgfbaseddrugdiscovery pages 5-6).

### Endosomal Trafficking

Following activation, FGFR1 undergoes endocytosis, commonly through clathrin-mediated pathways, and traffics through early endosomes (marked by EEA1) and late endosomes (marked by RAB7) (clark2024diversefgfr1signalingpathwaysand pages 12-13, domenichini2025receptortyrosinekinases pages 33-35, clark2024diversefgfr1signalingpathwaysand pages 1-3). Endosomal localization serves multiple functions: it enables spatially restricted signaling, regulates signal duration, and determines whether the receptor will be recycled to the plasma membrane or degraded in lysosomes (clark2024diversefgfr1signalingpathwaysand pages 12-13, clark2024diversefgfr1signalingpathwaysand pages 1-3). Receptor phosphorylation, clustering state, and interactions with endocytic regulatory proteins including EPS15 and CBL influence the trafficking route (clark2024diversefgfr1signalingpathwaysand pages 12-13, clark2024diversefgfr1signalingpathwaysand pages 1-3). Mutations affecting the Y730 phosphorylation site alter endosomal trafficking patterns and receptor distribution (clark2024diversefgfr1signalingpathwaysand pages 12-13).

### Nuclear Envelope and Nuclear Localization

FGFR1 can also localize to the nuclear envelope and nucleus, representing a noncanonical function distinct from its plasma membrane receptor activity (nguyen2024thecomplexityand pages 6-8, suh2022nuclearlocalizationof pages 6-8, gregorczyk2023nglycosylationactsas pages 1-2, servetto2021nuclearfgfr1regulates pages 1-2). The glycosylation status of FGFR1 acts as a molecular switch regulating trafficking between the plasma membrane and nuclear envelope: hypoglycosylated FGFR1 or receptor with impaired secretion preferentially accumulates at the nuclear envelope, while proper N-glycosylation of both D2 and D3 domains promotes plasma membrane delivery (nguyen2024thecomplexityand pages 6-8, gregorczyk2023nglycosylationactsas pages 1-2). Nuclear-envelope-localized FGFR1 can exhibit ligand-independent autoactivation and possesses a distinct protein interactome compared to plasma membrane-localized receptor (gregorczyk2023nglycosylationactsas pages 1-2).

Nuclear translocation of FGFR1 can occur through multiple mechanisms. FGF2, which contains a nuclear localization signal (NLS), can promote importin-β-mediated transport of FGFR1 into the nucleus (suh2022nuclearlocalizationof pages 6-8, suh2022nuclearlocalizationof pages 1-2, servetto2021nuclearfgfr1regulates pages 13-14). Alternatively, proteolytic cleavage by granzyme B can release a soluble C-terminal fragment that enters the nucleus (gregorczyk2023nglycosylationactsas pages 1-2, servetto2021nuclearfgfr1regulates pages 8-9). Reactive oxygen species (ROS) also promote nuclear accumulation of FGFR1, as ROS scavengers block FGF2-induced nuclear localization (suh2022nuclearlocalizationof pages 6-8, suh2022nuclearlocalizationof pages 1-2, suh2022nuclearlocalizationof pages 5-6).

Within the nucleus, FGFR1 functions as a chromatin-associated transcriptional regulator rather than a conventional plasma membrane signaling receptor (servetto2021nuclearfgfr1regulates pages 1-2, servetto2021nuclearfgfr1regulates pages 8-9, servetto2021nuclearfgfr1regulates pages 13-14). Nuclear FGFR1 occupies transcription start sites and promoter regions, overlapping with active transcription histone marks (servetto2021nuclearfgfr1regulates pages 1-2, servetto2021nuclearfgfr1regulates pages 8-9). It physically interacts with phosphorylated RNA polymerase II (including Ser5- and Ser2-phosphorylated forms), the pioneer transcription factor FOXA1, and transcriptional coactivators p300 and CBP (servetto2021nuclearfgfr1regulates pages 1-2, servetto2021nuclearfgfr1regulates pages 8-9, suh2022nuclearlocalizationof pages 5-6, servetto2021nuclearfgfr1regulates pages 13-14). FOXA1 is critical for recruiting FGFR1 to chromatin, as FOXA1 knockdown reduces FGFR1 binding to genomic sites and decreases expression of FGFR1-regulated genes (servetto2021nuclearfgfr1regulates pages 13-14).

Functionally, nuclear FGFR1 promotes gene expression programs associated with cell proliferation and, in cancer contexts, endocrine resistance (suh2022nuclearlocalizationof pages 6-8, servetto2021nuclearfgfr1regulates pages 1-2, servetto2021nuclearfgfr1regulates pages 8-9). Importantly, nuclear FGFR1 transcriptional activity is largely independent of its tyrosine kinase activity, as FGFR tyrosine kinase inhibitors do not prevent nuclear translocation or genomic activity (servetto2021nuclearfgfr1regulates pages 1-2, servetto2021nuclearfgfr1regulates pages 13-14).

## Ligand Specificity and Cofactor Requirements

FGFR1 binds multiple FGF ligands with specificity determined by receptor isoform, ligand structure, and cofactor availability (nguyen2024thecomplexityand pages 2-4, edirisinghe2024decodingfgffgfrsignaling pages 8-10, nguyen2024thecomplexityand pages 4-6). FGF1 and FGF2 are universal ligands that bind both FGFR1b and FGFR1c isoforms (nguyen2024thecomplexityand pages 2-4, nguyen2024thecomplexityand pages 4-6, edirisinghe2024decodingfgffgfrsignaling pages 3-4). FGF4, FGF6, and FGF16 preferentially bind the FGFR1c isoform, while FGF9 binds FGFR1b (nguyen2024thecomplexityand pages 2-4, edirisinghe2024decodingfgffgfrsignaling pages 8-10). FGF20 binds FGFR1, and FGF22 specifically signals through FGFR1b and FGFR2b in neural contexts (nguyen2024thecomplexityand pages 2-4, edirisinghe2024decodingfgffgfrsignaling pages 8-10). The endocrine FGFs—FGF21 and FGF23—bind FGFR1 in conjunction with Klotho coreceptors: FGF21 requires βKlotho, while FGF23 utilizes αKlotho and preferentially engages the FGFR1c isoform (nguyen2024thecomplexityand pages 2-4).

Paracrine FGFs generally require heparan sulfate proteoglycans as coreceptors, which stabilize the FGF–FGFR complex, restrict ligand diffusion, and promote receptor dimerization (zheng2022signalingpathwayand pages 1-2, nguyen2024thecomplexityand pages 2-4, domenichini2025receptortyrosinekinases pages 9-12, chen2025fgfbaseddrugdiscovery pages 2-4). In contrast, endocrine FGFs have reduced heparan sulfate affinity and depend on Klotho proteins for effective signaling (nguyen2024thecomplexityand pages 2-4, domenichini2025receptortyrosinekinases pages 9-12).

## Biological Processes and Physiological Roles

FGFR1 plays critical and diverse roles in embryonic development, tissue homeostasis, and cellular regulation (liu2023fgfrfamiliesbiological pages 1-2, liu2023fgfrfamiliesbiological pages 2-4, edirisinghe2024decodingfgffgfrsignaling pages 8-10, edirisinghe2024decodingfgffgfrsignaling pages 1-3).

### Development and Differentiation

During embryogenesis, FGFR1 supports cell proliferation, survival, migration, angiogenesis, and organ development (liu2023fgfrfamiliesbiological pages 1-2, liu2023fgfrfamiliesbiological pages 2-4, edirisinghe2024decodingfgffgfrsignaling pages 1-3). In early development, FGFR1 can be activated by mechanical stress independently of FGF ligands, promoting ERK-mediated remodeling of F-actin, cadherins, and tight junctions to support anterior–posterior patterning (liu2023fgfrfamiliesbiological pages 1-2). FGFR1 contributes to skeletal development, with distinct roles in skull vault development compared to FGFR2 (liu2023fgfrfamiliesbiological pages 19-20). In the nervous system, FGFR1 is required for proliferation of hippocampal progenitor cells and normal hippocampal growth (liu2023fgfrfamiliesbiological pages 19-20, edirisinghe2024decodingfgffgfrsignaling pages 8-10).

FGFR1 signaling influences cellular differentiation in context-dependent ways. It promotes proliferation of mouse myoblasts while delaying differentiation (liu2023fgfrfamiliesbiological pages 2-4). FGFR1 expression increases during adipocyte differentiation, though its precise role varies by cell type and developmental stage (liu2023fgfrfamiliesbiological pages 2-4).

### Tissue Homeostasis and Regeneration

In adult tissues, FGFR1 supports neovascularization, tissue repair, and wound healing (liu2023fgfrfamiliesbiological pages 1-2, liu2023fgfrfamiliesbiological pages 2-4). The FGF22–FGFR1b pathway contributes to neural homeostasis and, after spinal cord injury, promotes synaptic remodeling, reduces neuronal stress and apoptosis, and facilitates axon regeneration (edirisinghe2024decodingfgffgfrsignaling pages 8-10). In the liver, FGFR1b signaling (together with FGFR2b) stimulates hepatocyte proliferation and survival through AKT-β-catenin signaling, protecting against liver injury and supporting regeneration (edirisinghe2024decodingfgffgfrsignaling pages 8-10). FGFR1 also participates in angiogenesis and can influence plaque stability in atherosclerotic lesions (liu2023fgfrfamiliesbiological pages 2-4).

### Metabolic and Endocrine Functions

The FGFR1c isoform is a receptor for the endocrine hormone FGF23, which regulates phosphate homeostasis in the kidney (edirisinghe2024decodingfgffgfrsignaling pages 17-20). In complex with the αKlotho coreceptor, FGF23–FGFR1c signaling activates ERK1/2 and SGK1 pathways, leading to phosphorylation of NHERF1 and internalization of sodium-phosphate cotransporters NPT2a and NPT2c, thereby promoting renal phosphate wasting (edirisinghe2024decodingfgffgfrsignaling pages 17-20). FGF23–FGFR1c signaling also affects bone, where it can inhibit osteocyte differentiation through PI3K-AKT-mTOR activation (edirisinghe2024decodingfgffgfrsignaling pages 17-20).

## Summary and Conclusions

FGFR1 (P11362) is a multifunctional receptor tyrosine kinase that integrates extracellular FGF signals to regulate fundamental cellular processes including proliferation, differentiation, survival, migration, and metabolism. Structurally, it is organized as a single-pass transmembrane receptor with three extracellular immunoglobulin-like domains (D1–D3), a transmembrane helix, and an intracellular tyrosine kinase domain. Ligand binding, assisted by heparan sulfate or Klotho coreceptors, promotes receptor dimerization and trans-autophosphorylation, initiating four major signaling pathways: RAS–MAPK, PI3K–AKT, PLCγ–PKC–Ca²⁺, and JAK–STAT.

FGFR1 functions primarily at the plasma membrane but also undergoes endocytic trafficking and can localize to the nuclear envelope and nucleus, where it regulates gene transcription independently of its tyrosine kinase activity. Alternative splicing generates tissue-specific isoforms (FGFR1b and FGFR1c) with distinct ligand-binding preferences and physiological roles. Through these mechanisms, FGFR1 plays essential roles in embryonic development, neural and skeletal morphogenesis, tissue homeostasis, angiogenesis, wound healing, liver regeneration, and metabolic regulation.

The evidence presented in this report is based on recent authoritative reviews and primary research articles published primarily between 2022 and 2025, ensuring comprehensive and current understanding of FGFR1 biology.

References

1. (fan2024pharmacologicalandbiological pages 1-2): Shuai Fan, Yuxin Chen, Wenyu Wang, Wanting Xu, Mei Tian, Yuetong Liu, Yutong Zhou, Dan Liu, Qin Xia, and Lei Dong. Pharmacological and biological targeting of fgfr1 in cancer. Nov 2024. URL: https://doi.org/10.3390/cimb46110783, doi:10.3390/cimb46110783. This article has 34 citations.

2. (zheng2022signalingpathwayand pages 1-2): Jia Zheng, Wei Zhang, Linfeng Li, Yi He, Yue Wei, Yongjun Dang, Shenyou Nie, and Zufeng Guo. Signaling pathway and small-molecule drug discovery of fgfr: a comprehensive review. Frontiers in Chemistry, Apr 2022. URL: https://doi.org/10.3389/fchem.2022.860985, doi:10.3389/fchem.2022.860985. This article has 85 citations.

3. (chen2025fgfbaseddrugdiscovery pages 2-4): Gaozhi Chen, Lingfeng Chen, Xiaokun Li, and Moosa Mohammadi. Fgf-based drug discovery: advances and challenges. Nature reviews. Drug discovery, Jan 2025. URL: https://doi.org/10.1038/s41573-024-01125-w, doi:10.1038/s41573-024-01125-w. This article has 52 citations.

4. (chen2025fgfbaseddrugdiscovery pages 5-6): Gaozhi Chen, Lingfeng Chen, Xiaokun Li, and Moosa Mohammadi. Fgf-based drug discovery: advances and challenges. Nature reviews. Drug discovery, Jan 2025. URL: https://doi.org/10.1038/s41573-024-01125-w, doi:10.1038/s41573-024-01125-w. This article has 52 citations.

5. (domenichini2025receptortyrosinekinases pages 9-12): M Domenichini. Receptor tyrosine kinases alterations in cancer modulates mechano-properties and drug response in tumoral and endothelial cells. Unknown journal, 2025.

6. (nguyen2024thecomplexityand pages 6-8): Anh L. Nguyen, Caroline O. B. Facey, and Bruce M. Boman. The complexity and significance of fibroblast growth factor (fgf) signaling for fgf-targeted cancer therapies. Cancers, 17:82, Dec 2024. URL: https://doi.org/10.3390/cancers17010082, doi:10.3390/cancers17010082. This article has 21 citations.

7. (nguyen2024thecomplexityand pages 4-6): Anh L. Nguyen, Caroline O. B. Facey, and Bruce M. Boman. The complexity and significance of fibroblast growth factor (fgf) signaling for fgf-targeted cancer therapies. Cancers, 17:82, Dec 2024. URL: https://doi.org/10.3390/cancers17010082, doi:10.3390/cancers17010082. This article has 21 citations.

8. (zheng2022signalingpathwayand pages 2-5): Jia Zheng, Wei Zhang, Linfeng Li, Yi He, Yue Wei, Yongjun Dang, Shenyou Nie, and Zufeng Guo. Signaling pathway and small-molecule drug discovery of fgfr: a comprehensive review. Frontiers in Chemistry, Apr 2022. URL: https://doi.org/10.3389/fchem.2022.860985, doi:10.3389/fchem.2022.860985. This article has 85 citations.

9. (edirisinghe2024decodingfgffgfrsignaling pages 3-4): Oshadi Edirisinghe, Gaëtane Ternier, Zeina Alraawi, and Thallapuranam Krishnaswamy Suresh Kumar. Decoding fgf/fgfr signaling: insights into biological functions and disease relevance. Biomolecules, 14:1622, Dec 2024. URL: https://doi.org/10.3390/biom14121622, doi:10.3390/biom14121622. This article has 67 citations.

10. (yaronbarir2024theintrinsicsubstrate pages 19-22): Tomer M. Yaron-Barir, Brian A. Joughin, Emily M. Huntsman, Alexander Kerelsky, Daniel M. Cizin, Benjamin M. Cohen, Amit Regev, Junho Song, Neil Vasan, Ting-Yu Lin, Jose M. Orozco, Christina Schoenherr, Cari Sagum, Mark T. Bedford, R. Max Wynn, Shih-Chia Tso, David T. Chuang, Lei Li, Shawn S.-C. Li, Pau Creixell, Konstantin Krismer, Mina Takegami, Harin Lee, Bin Zhang, Jingyi Lu, Ian Cossentino, Sean D. Landry, Mohamed Uduman, John Blenis, Olivier Elemento, Margaret C. Frame, Peter V. Hornbeck, Lewis C. Cantley, Benjamin E. Turk, Michael B. Yaffe, and Jared L. Johnson. The intrinsic substrate specificity of the human tyrosine kinome. Nature, 629:1174-1181, May 2024. URL: https://doi.org/10.1038/s41586-024-07407-y, doi:10.1038/s41586-024-07407-y. This article has 187 citations and is from a highest quality peer-reviewed journal.

11. (fan2024pharmacologicalandbiological pages 2-4): Shuai Fan, Yuxin Chen, Wenyu Wang, Wanting Xu, Mei Tian, Yuetong Liu, Yutong Zhou, Dan Liu, Qin Xia, and Lei Dong. Pharmacological and biological targeting of fgfr1 in cancer. Nov 2024. URL: https://doi.org/10.3390/cimb46110783, doi:10.3390/cimb46110783. This article has 34 citations.

12. (palollathil2026proteomewideanalysisof pages 1-2): Akhina Palollathil, Althaf Mahin, Athira Perunelly Gopalakrishnan, Tejaswini R Poojari, Alimath Sambreena, Prathik Basthikoppa Shivamurthy, and Rajesh Raju. Proteome-wide analysis of functional phosphosites in the fgfr family of proteins: insights from large-scale phosphoproteomic analysis. Proteomes, 14:8, Feb 2026. URL: https://doi.org/10.3390/proteomes14010008, doi:10.3390/proteomes14010008. This article has 3 citations.

13. (edirisinghe2024decodingfgffgfrsignaling pages 1-3): Oshadi Edirisinghe, Gaëtane Ternier, Zeina Alraawi, and Thallapuranam Krishnaswamy Suresh Kumar. Decoding fgf/fgfr signaling: insights into biological functions and disease relevance. Biomolecules, 14:1622, Dec 2024. URL: https://doi.org/10.3390/biom14121622, doi:10.3390/biom14121622. This article has 67 citations.

14. (clark2024diversefgfr1signalingpathwaysand pages 1-3): James F. Clark and Philippe Soriano. Diverse<i>fgfr1</i>signaling pathways and endocytic trafficking regulate mesoderm development. Jun 2024. URL: https://doi.org/10.1101/gad.351593.124, doi:10.1101/gad.351593.124. This article has 13 citations and is from a highest quality peer-reviewed journal.

15. (liu2023fgfrfamiliesbiological pages 2-4): Qing Liu, Jiyu Huang, Weiwei Yan, Zhen Liu, Shu Liu, and Weiyi Fang. Fgfr families: biological functions and therapeutic interventions in tumors. MedComm, Sep 2023. URL: https://doi.org/10.1002/mco2.367, doi:10.1002/mco2.367. This article has 85 citations.

16. (clark2024diversefgfr1signalingpathwaysand pages 12-13): James F. Clark and Philippe Soriano. Diverse<i>fgfr1</i>signaling pathways and endocytic trafficking regulate mesoderm development. Jun 2024. URL: https://doi.org/10.1101/gad.351593.124, doi:10.1101/gad.351593.124. This article has 13 citations and is from a highest quality peer-reviewed journal.

17. (domenichini2025receptortyrosinekinases pages 33-35): M Domenichini. Receptor tyrosine kinases alterations in cancer modulates mechano-properties and drug response in tumoral and endothelial cells. Unknown journal, 2025.

18. (gregorczyk2023nglycosylationactsas pages 1-2): Paulina Gregorczyk, Natalia Porębska, Dominika Żukowska, Aleksandra Chorążewska, Aleksandra Gędaj, Agata Malinowska, Jacek Otlewski, Małgorzata Zakrzewska, and Łukasz Opaliński. N-glycosylation acts as a switch for fgfr1 trafficking between the plasma membrane and nuclear envelope. Cell Communication and Signaling : CCS, Jul 2023. URL: https://doi.org/10.1186/s12964-023-01203-3, doi:10.1186/s12964-023-01203-3. This article has 19 citations.

19. (suh2022nuclearlocalizationof pages 6-8): Jinyoung Suh, Do-Hee Kim, Su-Jung Kim, Nam-Chul Cho, Yeon-Hwa Lee, Jeong-Hoon Jang, and Young-Joon Surh. Nuclear localization of fibroblast growth factor receptor 1 in breast cancer cells interacting with cancer associated fibroblasts. Journal of Cancer Prevention, 27:68-76, Mar 2022. URL: https://doi.org/10.15430/jcp.2022.27.1.68, doi:10.15430/jcp.2022.27.1.68. This article has 14 citations.

20. (servetto2021nuclearfgfr1regulates pages 1-2): Alberto Servetto, Rahul Kollipara, Luigi Formisano, Chang-Ching Lin, Kyung-Min Lee, Dhivya R. Sudhan, Paula I. Gonzalez-Ericsson, Sumanta Chatterjee, Angel Guerrero-Zotano, Saurabh Mendiratta, Hiroaki Akamatsu, Nicholas James, Roberto Bianco, Ariella B. Hanker, Ralf Kittler, and Carlos L. Arteaga. Nuclear fgfr1 regulates gene transcription and promotes antiestrogen resistance in er+ breast cancer. Clinical Cancer Research, 27:4379-4396, May 2021. URL: https://doi.org/10.1158/1078-0432.ccr-20-3905, doi:10.1158/1078-0432.ccr-20-3905. This article has 77 citations and is from a highest quality peer-reviewed journal.

21. (servetto2021nuclearfgfr1regulates pages 8-9): Alberto Servetto, Rahul Kollipara, Luigi Formisano, Chang-Ching Lin, Kyung-Min Lee, Dhivya R. Sudhan, Paula I. Gonzalez-Ericsson, Sumanta Chatterjee, Angel Guerrero-Zotano, Saurabh Mendiratta, Hiroaki Akamatsu, Nicholas James, Roberto Bianco, Ariella B. Hanker, Ralf Kittler, and Carlos L. Arteaga. Nuclear fgfr1 regulates gene transcription and promotes antiestrogen resistance in er+ breast cancer. Clinical Cancer Research, 27:4379-4396, May 2021. URL: https://doi.org/10.1158/1078-0432.ccr-20-3905, doi:10.1158/1078-0432.ccr-20-3905. This article has 77 citations and is from a highest quality peer-reviewed journal.

22. (servetto2021nuclearfgfr1regulates pages 13-14): Alberto Servetto, Rahul Kollipara, Luigi Formisano, Chang-Ching Lin, Kyung-Min Lee, Dhivya R. Sudhan, Paula I. Gonzalez-Ericsson, Sumanta Chatterjee, Angel Guerrero-Zotano, Saurabh Mendiratta, Hiroaki Akamatsu, Nicholas James, Roberto Bianco, Ariella B. Hanker, Ralf Kittler, and Carlos L. Arteaga. Nuclear fgfr1 regulates gene transcription and promotes antiestrogen resistance in er+ breast cancer. Clinical Cancer Research, 27:4379-4396, May 2021. URL: https://doi.org/10.1158/1078-0432.ccr-20-3905, doi:10.1158/1078-0432.ccr-20-3905. This article has 77 citations and is from a highest quality peer-reviewed journal.

23. (karl2024ligandbiasunderlies pages 2-4): Kelly Karl, Nuala Del Piccolo, Taylor Light, Tanaya Roy, Pooja Dudeja, Vlad-Constantin Ursachi, Bohumil Fafilek, Pavel Krejci, and Kalina Hristova. Ligand bias underlies differential signaling of multiple fgfs via fgfr1. ArXiv, Aug 2024. URL: https://doi.org/10.7554/elife.88144.2, doi:10.7554/elife.88144.2. This article has 18 citations.

24. (suh2022nuclearlocalizationof pages 1-2): Jinyoung Suh, Do-Hee Kim, Su-Jung Kim, Nam-Chul Cho, Yeon-Hwa Lee, Jeong-Hoon Jang, and Young-Joon Surh. Nuclear localization of fibroblast growth factor receptor 1 in breast cancer cells interacting with cancer associated fibroblasts. Journal of Cancer Prevention, 27:68-76, Mar 2022. URL: https://doi.org/10.15430/jcp.2022.27.1.68, doi:10.15430/jcp.2022.27.1.68. This article has 14 citations.

25. (suh2022nuclearlocalizationof pages 5-6): Jinyoung Suh, Do-Hee Kim, Su-Jung Kim, Nam-Chul Cho, Yeon-Hwa Lee, Jeong-Hoon Jang, and Young-Joon Surh. Nuclear localization of fibroblast growth factor receptor 1 in breast cancer cells interacting with cancer associated fibroblasts. Journal of Cancer Prevention, 27:68-76, Mar 2022. URL: https://doi.org/10.15430/jcp.2022.27.1.68, doi:10.15430/jcp.2022.27.1.68. This article has 14 citations.

26. (nguyen2024thecomplexityand pages 2-4): Anh L. Nguyen, Caroline O. B. Facey, and Bruce M. Boman. The complexity and significance of fibroblast growth factor (fgf) signaling for fgf-targeted cancer therapies. Cancers, 17:82, Dec 2024. URL: https://doi.org/10.3390/cancers17010082, doi:10.3390/cancers17010082. This article has 21 citations.

27. (edirisinghe2024decodingfgffgfrsignaling pages 8-10): Oshadi Edirisinghe, Gaëtane Ternier, Zeina Alraawi, and Thallapuranam Krishnaswamy Suresh Kumar. Decoding fgf/fgfr signaling: insights into biological functions and disease relevance. Biomolecules, 14:1622, Dec 2024. URL: https://doi.org/10.3390/biom14121622, doi:10.3390/biom14121622. This article has 67 citations.

28. (liu2023fgfrfamiliesbiological pages 1-2): Qing Liu, Jiyu Huang, Weiwei Yan, Zhen Liu, Shu Liu, and Weiyi Fang. Fgfr families: biological functions and therapeutic interventions in tumors. MedComm, Sep 2023. URL: https://doi.org/10.1002/mco2.367, doi:10.1002/mco2.367. This article has 85 citations.

29. (liu2023fgfrfamiliesbiological pages 19-20): Qing Liu, Jiyu Huang, Weiwei Yan, Zhen Liu, Shu Liu, and Weiyi Fang. Fgfr families: biological functions and therapeutic interventions in tumors. MedComm, Sep 2023. URL: https://doi.org/10.1002/mco2.367, doi:10.1002/mco2.367. This article has 85 citations.

30. (edirisinghe2024decodingfgffgfrsignaling pages 17-20): Oshadi Edirisinghe, Gaëtane Ternier, Zeina Alraawi, and Thallapuranam Krishnaswamy Suresh Kumar. Decoding fgf/fgfr signaling: insights into biological functions and disease relevance. Biomolecules, 14:1622, Dec 2024. URL: https://doi.org/10.3390/biom14121622, doi:10.3390/biom14121622. This article has 67 citations.

## Artifacts

- [Edison artifact artifact-00](FGFR1-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](FGFR1-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. fan2024pharmacologicalandbiological pages 1-2
2. zheng2022signalingpathwayand pages 1-2
3. zheng2022signalingpathwayand pages 2-5
4. fan2024pharmacologicalandbiological pages 2-4
5. chen2025fgfbaseddrugdiscovery pages 5-6
6. gregorczyk2023nglycosylationactsas pages 1-2
7. nguyen2024thecomplexityand pages 2-4
8. liu2023fgfrfamiliesbiological pages 1-2
9. liu2023fgfrfamiliesbiological pages 19-20
10. liu2023fgfrfamiliesbiological pages 2-4
11. edirisinghe2024decodingfgffgfrsignaling pages 8-10
12. edirisinghe2024decodingfgffgfrsignaling pages 17-20
13. chen2025fgfbaseddrugdiscovery pages 2-4
14. domenichini2025receptortyrosinekinases pages 9-12
15. nguyen2024thecomplexityand pages 6-8
16. nguyen2024thecomplexityand pages 4-6
17. edirisinghe2024decodingfgffgfrsignaling pages 3-4
18. yaronbarir2024theintrinsicsubstrate pages 19-22
19. palollathil2026proteomewideanalysisof pages 1-2
20. edirisinghe2024decodingfgffgfrsignaling pages 1-3
21. domenichini2025receptortyrosinekinases pages 33-35
22. suh2022nuclearlocalizationof pages 6-8
23. karl2024ligandbiasunderlies pages 2-4
24. suh2022nuclearlocalizationof pages 1-2
25. suh2022nuclearlocalizationof pages 5-6
26. https://doi.org/10.3390/cimb46110783,
27. https://doi.org/10.3389/fchem.2022.860985,
28. https://doi.org/10.1038/s41573-024-01125-w,
29. https://doi.org/10.3390/cancers17010082,
30. https://doi.org/10.3390/biom14121622,
31. https://doi.org/10.1038/s41586-024-07407-y,
32. https://doi.org/10.3390/proteomes14010008,
33. https://doi.org/10.1101/gad.351593.124,
34. https://doi.org/10.1002/mco2.367,
35. https://doi.org/10.1186/s12964-023-01203-3,
36. https://doi.org/10.15430/jcp.2022.27.1.68,
37. https://doi.org/10.1158/1078-0432.ccr-20-3905,
38. https://doi.org/10.7554/elife.88144.2,