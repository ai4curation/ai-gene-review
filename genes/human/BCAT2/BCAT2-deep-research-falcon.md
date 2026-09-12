---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-05T19:32:24.755484'
end_time: '2026-07-05T19:56:21.996993'
duration_seconds: 1437.24
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: BCAT2
  gene_symbol: BCAT2
  uniprot_accession: O15382
  protein_description: 'RecName: Full=Branched-chain-amino-acid aminotransferase,
    mitochondrial {ECO:0000303|PubMed:9165094}; Short=BCAT(m) {ECO:0000303|PubMed:9165094};
    EC=2.6.1.42 {ECO:0000269|PubMed:8702755}; AltName: Full=Placental protein 18 {ECO:0000303|PubMed:11170829};
    Short=PP18 {ECO:0000303|PubMed:11170829}; Flags: Precursor;'
  gene_info: Name=BCAT2 {ECO:0000303|PubMed:31177572, ECO:0000312|HGNC:HGNC:977};
    Synonyms=BCATM {ECO:0000303|PubMed:9165094}, BCT2, ECA40 {ECO:0000303|PubMed:8702755};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the class-IV pyridoxal-phosphate-dependent
  protein_domains: Aminotrans_IV. (IPR001544); Aminotrans_IV_CS. (IPR018300); Aminotransferase-like.
    (IPR036038); B_amino_transII. (IPR005786); BCAT-like_C. (IPR043132)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 46
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: BCAT2-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: BCAT2-deep-research-falcon_artifacts/artifact-01.md
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
- **UniProt Accession:** O15382
- **Protein Description:** RecName: Full=Branched-chain-amino-acid aminotransferase, mitochondrial {ECO:0000303|PubMed:9165094}; Short=BCAT(m) {ECO:0000303|PubMed:9165094}; EC=2.6.1.42 {ECO:0000269|PubMed:8702755}; AltName: Full=Placental protein 18 {ECO:0000303|PubMed:11170829}; Short=PP18 {ECO:0000303|PubMed:11170829}; Flags: Precursor;
- **Gene Information:** Name=BCAT2 {ECO:0000303|PubMed:31177572, ECO:0000312|HGNC:HGNC:977}; Synonyms=BCATM {ECO:0000303|PubMed:9165094}, BCT2, ECA40 {ECO:0000303|PubMed:8702755};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the class-IV pyridoxal-phosphate-dependent
- **Key Domains:** Aminotrans_IV. (IPR001544); Aminotrans_IV_CS. (IPR018300); Aminotransferase-like. (IPR036038); B_amino_transII. (IPR005786); BCAT-like_C. (IPR043132)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "BCAT2" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'BCAT2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **BCAT2** (gene ID: BCAT2, UniProt: O15382) in human.

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
- **UniProt Accession:** O15382
- **Protein Description:** RecName: Full=Branched-chain-amino-acid aminotransferase, mitochondrial {ECO:0000303|PubMed:9165094}; Short=BCAT(m) {ECO:0000303|PubMed:9165094}; EC=2.6.1.42 {ECO:0000269|PubMed:8702755}; AltName: Full=Placental protein 18 {ECO:0000303|PubMed:11170829}; Short=PP18 {ECO:0000303|PubMed:11170829}; Flags: Precursor;
- **Gene Information:** Name=BCAT2 {ECO:0000303|PubMed:31177572, ECO:0000312|HGNC:HGNC:977}; Synonyms=BCATM {ECO:0000303|PubMed:9165094}, BCT2, ECA40 {ECO:0000303|PubMed:8702755};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the class-IV pyridoxal-phosphate-dependent
- **Key Domains:** Aminotrans_IV. (IPR001544); Aminotrans_IV_CS. (IPR018300); Aminotransferase-like. (IPR036038); B_amino_transII. (IPR005786); BCAT-like_C. (IPR043132)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "BCAT2" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'BCAT2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **BCAT2** (gene ID: BCAT2, UniProt: O15382) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: BCAT2 (Branched-Chain Amino Acid Aminotransferase 2, Mitochondrial)

**Gene:** BCAT2 (also known as BCATM, BCT2, ECA40) | **UniProt:** O15382 | **Organism:** Homo sapiens | **EC:** 2.6.1.42 | **Chromosomal Location:** 19q13.33

---

## 1. Gene Identity and Protein Description

BCAT2 encodes the mitochondrial isoform of the branched-chain aminotransferase (also designated BCATm), a pyridoxal-5'-phosphate (PLP)-dependent enzyme that catalyzes the first step in the catabolism of the three branched-chain amino acids (BCAAs)—leucine, isoleucine, and valine (bo2024primaryrolesof pages 9-11, conway2021emergingmoonlightingfunctions pages 7-9). The protein is synthesized as a precursor containing a mitochondrial targeting sequence that is cleaved upon import into the mitochondrial matrix (conway2021emergingmoonlightingfunctions pages 3-5). BCAT2 is distinguished from its paralog BCAT1 (BCATc), which is cytosolic and exhibits restricted tissue expression primarily in neuronal tissues (bo2024primaryrolesof pages 9-11, conway2021emergingmoonlightingfunctions pages 3-5). The two isoforms share approximately 58% sequence identity and have nearly identical active sites, yet differ fundamentally in subcellular localization, tissue distribution, and regulatory properties (conway2021emergingmoonlightingfunctions pages 9-11).

The following table summarizes the key distinctions between the two human BCAT isoforms:

| Isoform | Gene name | Protein name | Subcellular localization | Tissue expression | Chromosomal location | Key structural features | PDB code | Role in disease |
|---|---|---|---|---|---|---|---|---|
| BCAT1 | **BCAT1** | Branched-chain-amino-acid aminotransferase, cytosolic (BCATc) | Cytosol (bo2024primaryrolesof pages 9-11, conway2021emergingmoonlightingfunctions pages 3-5) | Restricted; enriched in neuronal tissues (brain, spinal cord, retina), and also ovary, testes, placenta, pancreas (bo2024primaryrolesof pages 9-11) | Not established from gathered evidence | Redox-active CXXC motif **C335/C338**; PLP-dependent active site with catalytic lysine reported as **Lys222** in structural evidence (conway2021emergingmoonlightingfunctions pages 13-15, conway2021emergingmoonlightingfunctions pages 47-51) | **2COJ** (conway2021emergingmoonlightingfunctions pages 47-51) | Prominent in neurologic/glutamate metabolism; aberrantly expressed in several cancers and linked to tumor progression; bi-allelic variants reported in candidate neurometabolic disorder literature retrieved during search (sperringer2017branchedchainaminoacids pages 6-7, conway2021emergingmoonlightingfunctions pages 7-9) |
| BCAT2 | **BCAT2** | Branched-chain-amino-acid aminotransferase, mitochondrial (BCATm); also called placental protein 18/PP18 in older nomenclature | Mitochondria (bo2024primaryrolesof pages 9-11, conway2021emergingmoonlightingfunctions pages 3-5) | Broad/ubiquitous; highest in skeletal muscle, colon, kidney, pancreas; low in liver (bo2024primaryrolesof pages 9-11, conway2021emergingmoonlightingfunctions pages 3-5) | **19q13.33** (conway2021emergingmoonlightingfunctions pages 3-5) | Redox-active CXXC motif **C315/C318**; PLP-dependent active site with catalytic lysine reported as **Lys202** in BCATm crystal structure; functions as homodimer (conway2021emergingmoonlightingfunctions pages 11-13, knerr2019expandingthegenetic pages 2-4, conway2021emergingmoonlightingfunctions pages 47-51) | **1EKF** (reduced form); additional BCATm forms **1KTA**, **1KT8** (knerr2019expandingthegenetic pages 2-4, conway2021emergingmoonlightingfunctions pages 47-51, conway2021emergingmoonlightingfunctions pages 13-15) | Causal gene for ultra-rare **BCAT2 deficiency** with elevated plasma BCAAs and low/normal BCKAs; also implicated in cancer metabolism, ferroptosis resistance, pancreatic cancer growth, melanoma progression, prostate cancer survival signaling, and metabolic disease/insulin-resistance pathways (wang2021branchedchainaminoacid pages 1-2, lei2020acetylationpromotesbcat2 pages 5-7, knerr2019expandingthegenetic pages 5-7, knerr2019expandingthegenetic pages 7-8, bo2024primaryrolesof pages 18-19, bo2024primaryrolesof pages 11-13) |


*Table: This table compares the human BCAT1 and BCAT2 isoforms across localization, tissue expression, structural features, and disease relevance. It is useful for distinguishing the cytosolic neuronal isoform from the mitochondrial broadly expressed isoform central to BCAA catabolism.*

---

## 2. Enzymatic Function and Catalytic Mechanism

### 2.1. Reaction Catalyzed

BCAT2 catalyzes the reversible transamination of all three BCAAs with α-ketoglutarate (2-oxoglutarate) as the amino group acceptor, producing the corresponding branched-chain α-keto acids (BCKAs) and L-glutamate (bo2024primaryrolesof pages 9-11, conway2021emergingmoonlightingfunctions pages 7-9). Specifically, leucine is converted to α-ketoisocaproate (KIC), isoleucine to α-keto-β-methylvalerate (KMV), and valine to α-ketoisovalerate (KIV) (bo2024primaryrolesof pages 9-11). The enzyme shows no strong discrimination among the three BCAAs, acting on all three substrates with comparable catalytic efficiency (bo2024primaryrolesof pages 9-11).

### 2.2. Cofactor and Mechanism

The reaction requires pyridoxal-5'-phosphate (PLP, a vitamin B6 derivative) as an essential cofactor, which is covalently bound to the enzyme via a Schiff base (internal aldimine) linkage with a conserved lysine residue (Lys202 in BCATm) (conway2021emergingmoonlightingfunctions pages 47-51, conway2021emergingmoonlightingfunctions pages 7-9). The catalytic cycle proceeds through a classical ping-pong (bi-bi) kinetic mechanism comprising two half-reactions (conway2021emergingmoonlightingfunctions pages 7-9). In the first half-reaction, the amino acid substrate displaces the active site lysine from the PLP cofactor through transaldimination, forming an external aldimine between the substrate and PLP. A subsequent 1,3-prototropic shift, in which the lysine residue acts as a catalytic base, generates a ketimine intermediate. Hydrolysis of this intermediate releases the α-keto acid product and converts PLP to pyridoxamine phosphate (PMP) (conway2021emergingmoonlightingfunctions pages 7-9). The second half-reaction proceeds in reverse with α-ketoglutarate as substrate, regenerating PLP and producing glutamate (conway2021emergingmoonlightingfunctions pages 7-9).

### 2.3. Substrate Specificity and Reversibility

The reaction is thermodynamically near equilibrium and fully reversible, meaning BCAT2 can also catalyze the re-amination of BCKAs to BCAAs (knerr2019expandingthegenetic pages 2-4, bo2024primaryrolesof pages 9-11). This reversibility has physiological significance: in tissues such as the brain, BCAT isoforms participate in a BCAA-BCKA nitrogen shuttle cycle that contributes to glutamate neurotransmitter synthesis (sperringer2017branchedchainaminoacids pages 6-7, sperringer2017branchedchainaminoacids pages 4-6).

---

## 3. Protein Structure

### 3.1. Overall Architecture

The crystal structure of human BCAT2 (BCATm) has been resolved (PDB: 1EKF in the reduced form; additional structures 1KTA and 1KT8 represent the pyridoxamine and ketimine intermediate forms, respectively) (knerr2019expandingthegenetic pages 2-4, conway2021emergingmoonlightingfunctions pages 47-51, conway2021emergingmoonlightingfunctions pages 13-15). BCAT2 functions as a homodimer, with each monomer consisting of a small domain (approximately residues 1–175) and a large domain (residues 176–365), connected by an interdomain loop (conway2021emergingmoonlightingfunctions pages 9-11). Two PLP cofactors are positioned at the dimer interface, each within an active site (conway2021emergingmoonlightingfunctions pages 9-11, knerr2019expandingthegenetic pages 2-4). The substrate-binding pocket is lined with hydrophobic residues including Tyr207, Phe75, and Tyr70, which create a favorable environment for anchoring the branched aliphatic side chains of the BCAA substrates (conway2021emergingmoonlightingfunctions pages 9-11).

### 3.2. The CXXC Redox Motif

A unique and functionally critical feature of BCAT proteins is a conserved CXXC redox-active motif (C315 and C318 in BCATm) located near the active site (conway2021emergingmoonlightingfunctions pages 11-13, conway2021emergingmoonlightingfunctions pages 47-51). The N-terminal cysteine (C315) serves as the redox sensor, while C318 functions as the resolving cysteine, enabling reversible regulation through thiol-disulfide interconversion (conway2021emergingmoonlightingfunctions pages 13-15, conway2021emergingmoonlightingfunctions pages 11-13). Oxidation by hydrogen peroxide causes a dose-dependent loss of enzymatic activity, with up to 4-fold reductions in kcat and 5–10-fold increases in Kd for BCAA substrates (conway2021emergingmoonlightingfunctions pages 11-13). Reduced thioredoxin can partially restore activity after oxidation, indicating redox cycling capability (conway2021emergingmoonlightingfunctions pages 11-13). Beyond regulating aminotransferase activity, the CXXC motif endows BCAT with a novel thiol oxidoreductase/chaperone function: oxidized BCAT proteins can catalyze dithiol-disulfide exchange reactions similar to protein disulfide isomerases (PDIs), facilitating insertion of disulfide bonds into substrate proteins (conway2021emergingmoonlightingfunctions pages 17-19, conway2021emergingmoonlightingfunctions pages 1-3, conway2021emergingmoonlightingfunctions pages 55-56). BCATm has been shown to co-localize with PDI and Mia40 in the mitochondrial intermembrane space, supporting a moonlighting role as a redox-active chaperone involved in protein folding (conway2021emergingmoonlightingfunctions pages 55-56).

---

## 4. Subcellular Localization and Tissue Expression

BCAT2 is a mitochondrial matrix protein, consistent with its role in the initial catabolism of BCAAs within this organelle (bo2024primaryrolesof pages 9-11, conway2021emergingmoonlightingfunctions pages 3-5). Its expression is ubiquitous across most human tissues, with particularly high levels in skeletal muscle, colon, kidney, and pancreas, and notably low expression in the liver (bo2024primaryrolesof pages 9-11, conway2021emergingmoonlightingfunctions pages 3-5). This tissue distribution is functionally significant: because BCAT2 expression is high in muscle but low in liver, skeletal muscle serves as the primary site of BCAA transamination, while the liver—which expresses abundant BCKDH but little BCAT2—preferentially oxidizes the muscle-derived BCKAs (bo2024primaryrolesof pages 9-11, sperringer2017branchedchainaminoacids pages 4-6). This inter-organ division of labor underlies the efficient systemic catabolism of BCAAs.

---

## 5. Biochemical Pathway Context and Metabolon Formation

### 5.1. The BCAA Catabolic Pathway

BCAT2 catalyzes the first step in mitochondrial BCAA catabolism. The second and rate-limiting committed step is performed by the branched-chain α-ketoacid dehydrogenase (BCKDH) complex, a multienzyme assembly (E1, E2, E3) that catalyzes the irreversible oxidative decarboxylation of BCKAs to their corresponding branched-chain acyl-CoA derivatives (isovaleryl-CoA from leucine, 2-methylbutyryl-CoA from isoleucine, isobutyryl-CoA from valine) (bo2024primaryrolesof pages 11-13, mei2026branchedchainaminoacids pages 3-5, conway2021emergingmoonlightingfunctions pages 47-51). These acyl-CoA products are further metabolized through dedicated pathways to produce acetyl-CoA and/or succinyl-CoA, which enter the TCA cycle (mei2026branchedchainaminoacids pages 3-5, sperringer2017branchedchainaminoacids pages 2-4). The BCKDH complex is regulated by a phosphorylation–dephosphorylation cycle: BCKDK (branched-chain ketoacid dehydrogenase kinase) phosphorylates and inactivates BCKDH, whereas PPM1K (protein phosphatase 2Cm) dephosphorylates and activates it (mei2026branchedchainaminoacids pages 3-5, sperringer2017branchedchainaminoacids pages 4-6).

The following table summarizes the pathway steps:

| Step number | Enzyme | Reaction | Substrates | Products | Compartment | Regulatory mechanism |
|---|---|---|---|---|---|---|
| 1 | **BCAT2 (branched-chain amino acid aminotransferase, mitochondrial)** | Reversible PLP-dependent transamination of branched-chain amino acids to branched-chain α-keto acids (BCKAs) | Leucine, isoleucine, valine + α-ketoglutarate | 2-ketoisocaproate (KIC), 2-keto-3-methylvalerate (KMV), 2-ketoisovalerate (KIV) + glutamate | Mitochondria, especially in extrahepatic tissues such as skeletal muscle | Requires **PLP** cofactor; activity is redox-sensitive via the **CXXC motif (C315/C318)**, where oxidation decreases activity and alters substrate affinity; BCAT2 can physically associate with BCKDH to support substrate channeling; BCAT2 stability is regulated by **K44 acetylation**—**CBP** promotes acetylation and ubiquitin-proteasome degradation, whereas **SIRT4** deacetylates and stabilizes BCAT2 (bo2024primaryrolesof pages 9-11, conway2021emergingmoonlightingfunctions pages 7-9, conway2021emergingmoonlightingfunctions pages 11-13, conway2021emergingmoonlightingfunctions pages 15-17, lei2020acetylationpromotesbcat2 pages 5-7, lei2020acetylationpromotesbcat2 pages 4-5, lei2020acetylationpromotesbcat2 pages 2-4) |
| 2 | **BCKDH complex** (branched-chain α-ketoacid dehydrogenase; E1/E2/E3) | Oxidative decarboxylation of BCKAs to branched-chain acyl-CoA derivatives; committed/rate-limiting step of BCAA oxidation | KIC, KMV, KIV | Isovaleryl-CoA, 2-methylbutyryl-CoA, isobutyryl-CoA + reducing equivalents | Mitochondrial matrix | Activity is inhibited by **BCKDK-mediated phosphorylation** and activated by **PPM1K-mediated dephosphorylation**; BCAT2 interaction with BCKDH supports metabolon formation and efficient transfer of BCKA products; BCAT2 loss can abolish effective BCKDH function in this pathway context (bo2024primaryrolesof pages 11-13, mei2026branchedchainaminoacids pages 3-5, conway2021emergingmoonlightingfunctions pages 47-51, sperringer2017branchedchainaminoacids pages 4-6, sperringer2017branchedchainaminoacids pages 2-4) |
| 3 | **Downstream BCAA oxidation enzymes** (multiple acyl-CoA dehydrogenation/hydration/cleavage steps) | Conversion of branched-chain acyl-CoA intermediates to central carbon metabolites that feed the TCA cycle | Isovaleryl-CoA, 2-methylbutyryl-CoA, isobutyryl-CoA and subsequent intermediates | Acetyl-CoA and/or succinyl-CoA (depending on BCAA species), which enter the TCA cycle for energy metabolism and biosynthesis | Mitochondria | Flux through this stage depends on upstream BCAT2/BCKDH activity and whole-pathway control of BCAA catabolism; impaired upstream catabolism contributes to BCAA/BCKA accumulation linked to metabolic disease, while intact downstream oxidation supports mitochondrial energy production and metabolic flexibility (mei2026branchedchainaminoacids pages 3-5, conway2021emergingmoonlightingfunctions pages 47-51, sperringer2017branchedchainaminoacids pages 2-4, bo2024primaryrolesof pages 18-19, bo2024primaryrolesof pages 11-13) |


*Table: This table summarizes the core mitochondrial steps of branched-chain amino acid catabolism involving BCAT2, from transamination through BCKDH-mediated oxidation to TCA cycle entry. It also highlights the main regulatory layers controlling pathway flux, including redox regulation, post-translational control of BCAT2, and BCKDH phosphorylation status.*

### 5.2. Metabolon Formation and Substrate Channeling

BCAT2 and the BCKDH complex physically interact within the mitochondrial matrix to form a metabolon that enables substrate channeling (conway2021emergingmoonlightingfunctions pages 15-17, bo2024primaryrolesof pages 11-13). For this interaction, BCATm must be in its reduced PLP form and adopt an open conformation; the PLP-bound form of BCATm binds directly to the E1α subunit of BCKDH, increasing the kinetic rate of BCKA decarboxylation (conway2021emergingmoonlightingfunctions pages 15-17). After transamination converts BCATm-PLP to BCATm-PMP, the enzyme is released from E1 (conway2021emergingmoonlightingfunctions pages 15-17). Critically, when BCAT2 is absent, BCKDH activity is effectively abolished, demonstrating the functional dependence of efficient BCAA oxidation on this protein–protein interaction (bo2024primaryrolesof pages 11-13). BCATm may also interact with glutamate dehydrogenase (GDH) for regeneration of α-ketoglutarate, completing the metabolic cycle (conway2021emergingmoonlightingfunctions pages 15-17). Oxidation of the CXXC motif or mutation of the reactive cysteines prevents metabolon formation (conway2021emergingmoonlightingfunctions pages 15-17).

### 5.3. Role in Nitrogen Metabolism

BCAT proteins serve as critical nitrogen donors in interorgan and intercellular nitrogen shuttling (sperringer2017branchedchainaminoacids pages 1-2). In the brain, BCAAs readily cross the blood–brain barrier and contribute approximately 20–30% of brain glutamate synthesis, the major excitatory neurotransmitter (sperringer2017branchedchainaminoacids pages 6-7, conway2021emergingmoonlightingfunctions pages 7-9, conway2021emergingmoonlightingfunctions pages 5-7). In rodent models, a BCAA-BCKA shuttle cycle operates between astrocytes and neurons: BCATm in astrocytes transaminates leucine to produce KIC and glutamate; KIC is released and taken up by neurons, where BCATc re-aminates it with glutamate, regenerating leucine and supporting neurotransmitter pools (sperringer2017branchedchainaminoacids pages 6-7, sperringer2017branchedchainaminoacids pages 4-6). In the human brain, BCATm is localized to capillary endothelial cells rather than astrocytes, suggesting species-specific differences in this shuttle mechanism (sperringer2017branchedchainaminoacids pages 6-7, conway2021emergingmoonlightingfunctions pages 7-9).

---

## 6. Post-Translational Regulation of BCAT2

### 6.1. Acetylation at Lysine 44

BCAT2 protein stability is regulated by acetylation at the evolutionarily conserved residue lysine 44 (K44). The acetyltransferase CBP (CREB-binding protein) catalyzes K44 acetylation, which promotes BCAT2 ubiquitination and degradation through the ubiquitin–proteasome pathway (lei2020acetylationpromotesbcat2 pages 5-7, lei2020acetylationpromotesbcat2 pages 4-5, lei2020acetylationpromotesbcat2 pages 2-4). The mitochondrial sirtuin SIRT4 opposes this modification by deacetylating K44, stabilizing BCAT2 protein levels (lei2020acetylationpromotesbcat2 pages 5-7, lei2020acetylationpromotesbcat2 pages 4-5). Importantly, K44 acetylation does not directly affect BCAT2 enzymatic activity but controls protein abundance (lei2020acetylationpromotesbcat2 pages 2-4). BCAA deprivation stimulates K44 acetylation, providing a nutrient-sensing feedback mechanism that links amino acid availability to BCAT2 degradation (lei2020acetylationpromotesbcat2 pages 1-2, lei2020acetylationpromotesbcat2 pages 2-4). A non-acetylatable K44R mutant is more stable, promotes increased BCAA catabolism, and enhances pancreatic tumor growth in vivo (lei2020acetylationpromotesbcat2 pages 5-7, lei2020acetylationpromotesbcat2 pages 1-2).

### 6.2. Additional Post-Translational Modifications

Beyond acetylation, BCAT2 stability is regulated by deubiquitination at K229 mediated by USP1, and by phosphorylation at Y228 through a KRAS-SYK-TRIM21 signaling axis—both mechanisms contributing to BCAT2 stabilization in pancreatic cancer (zhang2026branchedchainaminoacid pages 4-5).

---

## 7. Disease Associations

### 7.1. BCAT2 Deficiency (Inborn Error of Metabolism)

BCAT2 deficiency (MIM 113530) is an ultra-rare autosomal recessive inborn error of BCAA catabolism caused by biallelic loss-of-function mutations in BCAT2 (knerr2019expandingthegenetic pages 5-7, knerr2019expandingthegenetic pages 1-2). The biochemical hallmark is markedly elevated plasma BCAAs—with disproportionately high valine levels—combined with low-normal or undetectable BCKAs and absent L-allo-isoleucine, clearly distinguishing it from maple syrup urine disease (MSUD), which shows elevation of both BCAAs and BCKAs (knerr2019expandingthegenetic pages 5-7, knerr2019expandingthegenetic pages 7-8, knerr2019expandingthegenetic pages 2-4). Knerr et al. (2019) characterized five individuals from four families with homozygous or compound heterozygous BCAT2 mutations, reporting that clinical phenotypes ranged from asymptomatic adulthood to developmental delay, intellectual disability, speech impairment, and autism spectrum features (knerr2019expandingthegenetic pages 5-7, knerr2019expandingthegenetic pages 7-8). Notably, unlike MSUD, no individual with BCAT2 deficiency developed acute encephalopathy even with exceptionally elevated BCAA levels (knerr2019expandingthegenetic pages 7-8, knerr2019expandingthegenetic pages 1-2). The authors suggested that the neurodevelopmental phenotype may relate to disturbed glutamate and GABA homeostasis, since BCAAs serve as nitrogen donors for these neurotransmitters (knerr2019expandingthegenetic pages 8-9). Western blot analysis demonstrated absent BCAT2 protein in some patients, and fibroblast studies confirmed markedly reduced leucine and valine decarboxylation capacity (knerr2019expandingthegenetic pages 4-5). Dietary protein restriction and pyridoxine supplementation appeared to reduce BCAA levels (knerr2019expandingthegenetic pages 4-5, haydar2018branchedchainamino pages 2-4).

### 7.2. Cancer

BCAT2 has emerged as a significant player in cancer metabolism with context-dependent roles across multiple tumor types. In **pancreatic ductal adenocarcinoma (PDAC)**, BCAT2 is consistently upregulated and its expression is stabilized by KRAS-dependent mechanisms; knockdown suppresses tumor growth both in vitro and in vivo (he2026bcaasandrelated pages 7-8, lei2020acetylationpromotesbcat2 pages 5-7, zhang2026branchedchainaminoacid pages 4-5). In **hepatocellular carcinoma**, BCAT2 was identified through a genome-wide CRISPR/Cas9 screen as a novel suppressor of ferroptosis: BCAT2 regulates intracellular glutamate levels and antagonizes system Xc⁻ inhibition, protecting cancer cells from ferroptotic death induced by sorafenib and erastin (wang2021branchedchainaminoacid pages 1-2). Ferroptosis inducers activate the AMPK/SREBP1 signaling pathway, which inhibits BCAT2 transcription, and co-treatment with sorafenib and sulfasalazine synergistically downregulates BCAT2 to trigger ferroptosis (wang2021branchedchainaminoacid pages 1-2). In **melanoma**, BCAT2 promotes lipogenesis by regulating FASN and ACLY expression through P300-dependent histone acetylation, with ZEB1 acting as an upstream transcriptional activator (zhang2026branchedchainaminoacid pages 13-14, zhang2026branchedchainaminoacid pages 15-17). In **prostate cancer**, BCAT2 inhibits autophagy-dependent apoptosis and ferroptosis through interaction with PCBP1 at Leucine 239 to co-regulate the PI3K/AKT signaling pathway (zhang2026branchedchainaminoacid pages 13-14, zhang2026branchedchainaminoacid pages 11-13, zhang2026branchedchainaminoacid pages 15-17). In **bladder cancer**, BCAT2 suppresses cytotoxic T-cell recruitment, creating an immunosuppressive tumor microenvironment; inhibiting BCAT2 synergizes with anti-PD-1 therapy (zhang2026branchedchainaminoacid pages 13-14). BCAT1 and BCAT2 exhibit a transcriptional compensatory relationship that together maintains BCAA catabolic stability in tumors (zhang2026branchedchainaminoacid pages 11-13).

### 7.3. Diabetes and Metabolic Disease

Elevated circulating BCAA levels are a consistent and predictive biomarker of insulin resistance and type 2 diabetes mellitus (T2DM) (conway2021emergingmoonlightingfunctions pages 5-7, mei2026branchedchainaminoacids pages 5-6, mei2026branchedchainaminoacids pages 1-2). Impaired BCAT2-mediated BCAA catabolism in skeletal muscle and adipose tissue contributes to this elevation, leading to sustained mTORC1 activation, serine phosphorylation of IRS-1, and attenuation of insulin signaling (mei2026branchedchainaminoacids pages 5-6, mei2026branchedchainaminoacids pages 2-3). In BCAT2-knockout mice, blood BCAA concentrations increase more than 10-fold, though paradoxically, body weight and adiposity decrease due to increased energy expenditure (bo2024primaryrolesof pages 11-13). The compound BT2, which inhibits BCKDK and thereby reactivates the BCKDH complex, has been shown to reduce circulating BCAAs and potentiate metformin's glucose-lowering effects in obese mice (mei2026branchedchainaminoacids pages 6-8). Recent work has also implicated BCAT2 in **diabetic atherosclerotic calcification**, where BCAT2 is upregulated in vascular smooth muscle cells and its catabolism of BCAAs to BCKAs promotes osteogenic differentiation through BCKA-derived propionyl-CoA and histone propionylation at the RUNX2 promoter (Zhang et al., 2026).

---

## 8. Summary

BCAT2 is the ubiquitously expressed, mitochondrial isoform of branched-chain amino acid aminotransferase that catalyzes the reversible, PLP-dependent transamination of leucine, isoleucine, and valine to their corresponding branched-chain α-keto acids, with concomitant conversion of α-ketoglutarate to glutamate (bo2024primaryrolesof pages 9-11, conway2021emergingmoonlightingfunctions pages 7-9). It functions within the mitochondrial matrix, where it physically associates with the BCKDH complex in a metabolon that enables efficient substrate channeling and complete BCAA oxidation (conway2021emergingmoonlightingfunctions pages 15-17, bo2024primaryrolesof pages 11-13). Its activity is regulated at multiple levels: at the cofactor level by PLP availability, at the protein level by redox-sensitive CXXC motif oxidation (C315/C318), and at the stability level by K44 acetylation mediated by CBP/SIRT4 (conway2021emergingmoonlightingfunctions pages 11-13, lei2020acetylationpromotesbcat2 pages 5-7). BCAT2 deficiency is an ultra-rare inborn error of metabolism characterized by elevated BCAAs with low BCKAs and variable neurodevelopmental phenotypes (knerr2019expandingthegenetic pages 5-7, knerr2019expandingthegenetic pages 1-2). In the broader disease context, BCAT2 has emerged as a nexus between amino acid metabolism and cancer biology—regulating ferroptosis sensitivity, tumor proliferation, and immune evasion in a cancer type-dependent manner—and as a contributor to BCAA-mediated insulin resistance in metabolic disease (he2026bcaasandrelated pages 7-8, wang2021branchedchainaminoacid pages 1-2, conway2021emergingmoonlightingfunctions pages 5-7, mei2026branchedchainaminoacids pages 5-6).

References

1. (bo2024primaryrolesof pages 9-11): Tomoki Bo and Junichi Fujii. Primary roles of branched chain amino acids (bcaas) and their metabolism in physiology and metabolic disorders. Molecules, 30:56, Dec 2024. URL: https://doi.org/10.3390/molecules30010056, doi:10.3390/molecules30010056. This article has 61 citations.

2. (conway2021emergingmoonlightingfunctions pages 7-9): Myra Elizabeth Conway. Emerging moonlighting functions of the branched-chain aminotransferase proteins. May 2021. URL: https://doi.org/10.1089/ars.2020.8118, doi:10.1089/ars.2020.8118. This article has 28 citations and is from a domain leading peer-reviewed journal.

3. (conway2021emergingmoonlightingfunctions pages 3-5): Myra Elizabeth Conway. Emerging moonlighting functions of the branched-chain aminotransferase proteins. May 2021. URL: https://doi.org/10.1089/ars.2020.8118, doi:10.1089/ars.2020.8118. This article has 28 citations and is from a domain leading peer-reviewed journal.

4. (conway2021emergingmoonlightingfunctions pages 9-11): Myra Elizabeth Conway. Emerging moonlighting functions of the branched-chain aminotransferase proteins. May 2021. URL: https://doi.org/10.1089/ars.2020.8118, doi:10.1089/ars.2020.8118. This article has 28 citations and is from a domain leading peer-reviewed journal.

5. (conway2021emergingmoonlightingfunctions pages 13-15): Myra Elizabeth Conway. Emerging moonlighting functions of the branched-chain aminotransferase proteins. May 2021. URL: https://doi.org/10.1089/ars.2020.8118, doi:10.1089/ars.2020.8118. This article has 28 citations and is from a domain leading peer-reviewed journal.

6. (conway2021emergingmoonlightingfunctions pages 47-51): Myra Elizabeth Conway. Emerging moonlighting functions of the branched-chain aminotransferase proteins. May 2021. URL: https://doi.org/10.1089/ars.2020.8118, doi:10.1089/ars.2020.8118. This article has 28 citations and is from a domain leading peer-reviewed journal.

7. (sperringer2017branchedchainaminoacids pages 6-7): Justin E. Sperringer, Adele Addington, and Susan M. Hutson. Branched-chain amino acids and brain metabolism. Neurochemical Research, 42:1697-1709, Apr 2017. URL: https://doi.org/10.1007/s11064-017-2261-5, doi:10.1007/s11064-017-2261-5. This article has 265 citations and is from a peer-reviewed journal.

8. (conway2021emergingmoonlightingfunctions pages 11-13): Myra Elizabeth Conway. Emerging moonlighting functions of the branched-chain aminotransferase proteins. May 2021. URL: https://doi.org/10.1089/ars.2020.8118, doi:10.1089/ars.2020.8118. This article has 28 citations and is from a domain leading peer-reviewed journal.

9. (knerr2019expandingthegenetic pages 2-4): Ina Knerr, Roberto Colombo, Jill Urquhart, Ana Morais, Begona Merinero, Alfonso Oyarzabal, Belén Pérez, Simon A. Jones, Rahat Perveen, Mary A. Preece, Yvonne Rogers, Eileen P. Treacy, Philip Mayne, Giuseppe Zampino, Sabrina MacKinnon, Evangeline Wassmer, Wyatt W. Yue, Ian Robinson, Pilar Rodríguez‐Pombo, Simon E. Olpin, and Siddharth Banka. Expanding the genetic and phenotypic spectrum of branched‐chain amino acid transferase 2 deficiency. Journal of Inherited Metabolic Disease, 42:809-817, Aug 2019. URL: https://doi.org/10.1002/jimd.12135, doi:10.1002/jimd.12135. This article has 32 citations and is from a peer-reviewed journal.

10. (wang2021branchedchainaminoacid pages 1-2): Kang Wang, Zhengyang Zhang, Hsiang-i Tsai, Yanfang Liu, Jie Gao, Ming Wang, Lian Song, Xiongfeng Cao, Zhanxue Xu, Hongbo Chen, Aihua Gong, Dongqing Wang, Fang Cheng, and Haitao Zhu. Branched-chain amino acid aminotransferase 2 regulates ferroptotic cell death in cancer cells. Cell Death &amp; Differentiation, 28:1222-1236, Oct 2021. URL: https://doi.org/10.1038/s41418-020-00644-4, doi:10.1038/s41418-020-00644-4. This article has 218 citations and is from a domain leading peer-reviewed journal.

11. (lei2020acetylationpromotesbcat2 pages 5-7): Ming-Zhu Lei, Xu-Xu Li, Ye Zhang, Jin-Tao Li, Fan Zhang, Yi-Ping Wang, Miao Yin, Jia Qu, and Qun-Ying Lei. Acetylation promotes bcat2 degradation to suppress bcaa catabolism and pancreatic cancer growth. Signal Transduction and Targeted Therapy, May 2020. URL: https://doi.org/10.1038/s41392-020-0168-0, doi:10.1038/s41392-020-0168-0. This article has 132 citations and is from a peer-reviewed journal.

12. (knerr2019expandingthegenetic pages 5-7): Ina Knerr, Roberto Colombo, Jill Urquhart, Ana Morais, Begona Merinero, Alfonso Oyarzabal, Belén Pérez, Simon A. Jones, Rahat Perveen, Mary A. Preece, Yvonne Rogers, Eileen P. Treacy, Philip Mayne, Giuseppe Zampino, Sabrina MacKinnon, Evangeline Wassmer, Wyatt W. Yue, Ian Robinson, Pilar Rodríguez‐Pombo, Simon E. Olpin, and Siddharth Banka. Expanding the genetic and phenotypic spectrum of branched‐chain amino acid transferase 2 deficiency. Journal of Inherited Metabolic Disease, 42:809-817, Aug 2019. URL: https://doi.org/10.1002/jimd.12135, doi:10.1002/jimd.12135. This article has 32 citations and is from a peer-reviewed journal.

13. (knerr2019expandingthegenetic pages 7-8): Ina Knerr, Roberto Colombo, Jill Urquhart, Ana Morais, Begona Merinero, Alfonso Oyarzabal, Belén Pérez, Simon A. Jones, Rahat Perveen, Mary A. Preece, Yvonne Rogers, Eileen P. Treacy, Philip Mayne, Giuseppe Zampino, Sabrina MacKinnon, Evangeline Wassmer, Wyatt W. Yue, Ian Robinson, Pilar Rodríguez‐Pombo, Simon E. Olpin, and Siddharth Banka. Expanding the genetic and phenotypic spectrum of branched‐chain amino acid transferase 2 deficiency. Journal of Inherited Metabolic Disease, 42:809-817, Aug 2019. URL: https://doi.org/10.1002/jimd.12135, doi:10.1002/jimd.12135. This article has 32 citations and is from a peer-reviewed journal.

14. (bo2024primaryrolesof pages 18-19): Tomoki Bo and Junichi Fujii. Primary roles of branched chain amino acids (bcaas) and their metabolism in physiology and metabolic disorders. Molecules, 30:56, Dec 2024. URL: https://doi.org/10.3390/molecules30010056, doi:10.3390/molecules30010056. This article has 61 citations.

15. (bo2024primaryrolesof pages 11-13): Tomoki Bo and Junichi Fujii. Primary roles of branched chain amino acids (bcaas) and their metabolism in physiology and metabolic disorders. Molecules, 30:56, Dec 2024. URL: https://doi.org/10.3390/molecules30010056, doi:10.3390/molecules30010056. This article has 61 citations.

16. (sperringer2017branchedchainaminoacids pages 4-6): Justin E. Sperringer, Adele Addington, and Susan M. Hutson. Branched-chain amino acids and brain metabolism. Neurochemical Research, 42:1697-1709, Apr 2017. URL: https://doi.org/10.1007/s11064-017-2261-5, doi:10.1007/s11064-017-2261-5. This article has 265 citations and is from a peer-reviewed journal.

17. (conway2021emergingmoonlightingfunctions pages 17-19): Myra Elizabeth Conway. Emerging moonlighting functions of the branched-chain aminotransferase proteins. May 2021. URL: https://doi.org/10.1089/ars.2020.8118, doi:10.1089/ars.2020.8118. This article has 28 citations and is from a domain leading peer-reviewed journal.

18. (conway2021emergingmoonlightingfunctions pages 1-3): Myra Elizabeth Conway. Emerging moonlighting functions of the branched-chain aminotransferase proteins. May 2021. URL: https://doi.org/10.1089/ars.2020.8118, doi:10.1089/ars.2020.8118. This article has 28 citations and is from a domain leading peer-reviewed journal.

19. (conway2021emergingmoonlightingfunctions pages 55-56): Myra Elizabeth Conway. Emerging moonlighting functions of the branched-chain aminotransferase proteins. May 2021. URL: https://doi.org/10.1089/ars.2020.8118, doi:10.1089/ars.2020.8118. This article has 28 citations and is from a domain leading peer-reviewed journal.

20. (mei2026branchedchainaminoacids pages 3-5): Jie Mei, Fu-yuan Yang, and Quan Gong. Branched-chain amino acids and insulin resistance in type 2 diabetes: from metabolic dysregulation to therapeutic targets. Frontiers in Endocrinology, Feb 2026. URL: https://doi.org/10.3389/fendo.2025.1643231, doi:10.3389/fendo.2025.1643231. This article has 4 citations.

21. (sperringer2017branchedchainaminoacids pages 2-4): Justin E. Sperringer, Adele Addington, and Susan M. Hutson. Branched-chain amino acids and brain metabolism. Neurochemical Research, 42:1697-1709, Apr 2017. URL: https://doi.org/10.1007/s11064-017-2261-5, doi:10.1007/s11064-017-2261-5. This article has 265 citations and is from a peer-reviewed journal.

22. (conway2021emergingmoonlightingfunctions pages 15-17): Myra Elizabeth Conway. Emerging moonlighting functions of the branched-chain aminotransferase proteins. May 2021. URL: https://doi.org/10.1089/ars.2020.8118, doi:10.1089/ars.2020.8118. This article has 28 citations and is from a domain leading peer-reviewed journal.

23. (lei2020acetylationpromotesbcat2 pages 4-5): Ming-Zhu Lei, Xu-Xu Li, Ye Zhang, Jin-Tao Li, Fan Zhang, Yi-Ping Wang, Miao Yin, Jia Qu, and Qun-Ying Lei. Acetylation promotes bcat2 degradation to suppress bcaa catabolism and pancreatic cancer growth. Signal Transduction and Targeted Therapy, May 2020. URL: https://doi.org/10.1038/s41392-020-0168-0, doi:10.1038/s41392-020-0168-0. This article has 132 citations and is from a peer-reviewed journal.

24. (lei2020acetylationpromotesbcat2 pages 2-4): Ming-Zhu Lei, Xu-Xu Li, Ye Zhang, Jin-Tao Li, Fan Zhang, Yi-Ping Wang, Miao Yin, Jia Qu, and Qun-Ying Lei. Acetylation promotes bcat2 degradation to suppress bcaa catabolism and pancreatic cancer growth. Signal Transduction and Targeted Therapy, May 2020. URL: https://doi.org/10.1038/s41392-020-0168-0, doi:10.1038/s41392-020-0168-0. This article has 132 citations and is from a peer-reviewed journal.

25. (sperringer2017branchedchainaminoacids pages 1-2): Justin E. Sperringer, Adele Addington, and Susan M. Hutson. Branched-chain amino acids and brain metabolism. Neurochemical Research, 42:1697-1709, Apr 2017. URL: https://doi.org/10.1007/s11064-017-2261-5, doi:10.1007/s11064-017-2261-5. This article has 265 citations and is from a peer-reviewed journal.

26. (conway2021emergingmoonlightingfunctions pages 5-7): Myra Elizabeth Conway. Emerging moonlighting functions of the branched-chain aminotransferase proteins. May 2021. URL: https://doi.org/10.1089/ars.2020.8118, doi:10.1089/ars.2020.8118. This article has 28 citations and is from a domain leading peer-reviewed journal.

27. (lei2020acetylationpromotesbcat2 pages 1-2): Ming-Zhu Lei, Xu-Xu Li, Ye Zhang, Jin-Tao Li, Fan Zhang, Yi-Ping Wang, Miao Yin, Jia Qu, and Qun-Ying Lei. Acetylation promotes bcat2 degradation to suppress bcaa catabolism and pancreatic cancer growth. Signal Transduction and Targeted Therapy, May 2020. URL: https://doi.org/10.1038/s41392-020-0168-0, doi:10.1038/s41392-020-0168-0. This article has 132 citations and is from a peer-reviewed journal.

28. (zhang2026branchedchainaminoacid pages 4-5): Weiran Zhang, Jie Shen, Xuanyin Ding, Hele Liu, Xu Wang, and Dan Feng. Branched-chain amino acid transaminases as promising targets in tumor therapy. Frontiers in Cell and Developmental Biology, Feb 2026. URL: https://doi.org/10.3389/fcell.2026.1712076, doi:10.3389/fcell.2026.1712076. This article has 1 citations.

29. (knerr2019expandingthegenetic pages 1-2): Ina Knerr, Roberto Colombo, Jill Urquhart, Ana Morais, Begona Merinero, Alfonso Oyarzabal, Belén Pérez, Simon A. Jones, Rahat Perveen, Mary A. Preece, Yvonne Rogers, Eileen P. Treacy, Philip Mayne, Giuseppe Zampino, Sabrina MacKinnon, Evangeline Wassmer, Wyatt W. Yue, Ian Robinson, Pilar Rodríguez‐Pombo, Simon E. Olpin, and Siddharth Banka. Expanding the genetic and phenotypic spectrum of branched‐chain amino acid transferase 2 deficiency. Journal of Inherited Metabolic Disease, 42:809-817, Aug 2019. URL: https://doi.org/10.1002/jimd.12135, doi:10.1002/jimd.12135. This article has 32 citations and is from a peer-reviewed journal.

30. (knerr2019expandingthegenetic pages 8-9): Ina Knerr, Roberto Colombo, Jill Urquhart, Ana Morais, Begona Merinero, Alfonso Oyarzabal, Belén Pérez, Simon A. Jones, Rahat Perveen, Mary A. Preece, Yvonne Rogers, Eileen P. Treacy, Philip Mayne, Giuseppe Zampino, Sabrina MacKinnon, Evangeline Wassmer, Wyatt W. Yue, Ian Robinson, Pilar Rodríguez‐Pombo, Simon E. Olpin, and Siddharth Banka. Expanding the genetic and phenotypic spectrum of branched‐chain amino acid transferase 2 deficiency. Journal of Inherited Metabolic Disease, 42:809-817, Aug 2019. URL: https://doi.org/10.1002/jimd.12135, doi:10.1002/jimd.12135. This article has 32 citations and is from a peer-reviewed journal.

31. (knerr2019expandingthegenetic pages 4-5): Ina Knerr, Roberto Colombo, Jill Urquhart, Ana Morais, Begona Merinero, Alfonso Oyarzabal, Belén Pérez, Simon A. Jones, Rahat Perveen, Mary A. Preece, Yvonne Rogers, Eileen P. Treacy, Philip Mayne, Giuseppe Zampino, Sabrina MacKinnon, Evangeline Wassmer, Wyatt W. Yue, Ian Robinson, Pilar Rodríguez‐Pombo, Simon E. Olpin, and Siddharth Banka. Expanding the genetic and phenotypic spectrum of branched‐chain amino acid transferase 2 deficiency. Journal of Inherited Metabolic Disease, 42:809-817, Aug 2019. URL: https://doi.org/10.1002/jimd.12135, doi:10.1002/jimd.12135. This article has 32 citations and is from a peer-reviewed journal.

32. (haydar2018branchedchainamino pages 2-4): Sara Haydar, C. Lautier, and F. Grigorescu. Branched chain amino acids at the edge between mendelian and complex disorders. Acta endocrinologica, 14 2:238-247, Apr 2018. URL: https://doi.org/10.4183/aeb.2018.238, doi:10.4183/aeb.2018.238. This article has 11 citations.

33. (he2026bcaasandrelated pages 7-8): Binfan He, Lingxi Li, Ye Liu, Mengmeng Hao, Ling Zhang, and Rongzhang He. Bcaas and related metabolic enzymes: partners in crime driving tumor development. Frontiers in Cell and Developmental Biology, Feb 2026. URL: https://doi.org/10.3389/fcell.2026.1748587, doi:10.3389/fcell.2026.1748587. This article has 0 citations.

34. (zhang2026branchedchainaminoacid pages 13-14): Weiran Zhang, Jie Shen, Xuanyin Ding, Hele Liu, Xu Wang, and Dan Feng. Branched-chain amino acid transaminases as promising targets in tumor therapy. Frontiers in Cell and Developmental Biology, Feb 2026. URL: https://doi.org/10.3389/fcell.2026.1712076, doi:10.3389/fcell.2026.1712076. This article has 1 citations.

35. (zhang2026branchedchainaminoacid pages 15-17): Weiran Zhang, Jie Shen, Xuanyin Ding, Hele Liu, Xu Wang, and Dan Feng. Branched-chain amino acid transaminases as promising targets in tumor therapy. Frontiers in Cell and Developmental Biology, Feb 2026. URL: https://doi.org/10.3389/fcell.2026.1712076, doi:10.3389/fcell.2026.1712076. This article has 1 citations.

36. (zhang2026branchedchainaminoacid pages 11-13): Weiran Zhang, Jie Shen, Xuanyin Ding, Hele Liu, Xu Wang, and Dan Feng. Branched-chain amino acid transaminases as promising targets in tumor therapy. Frontiers in Cell and Developmental Biology, Feb 2026. URL: https://doi.org/10.3389/fcell.2026.1712076, doi:10.3389/fcell.2026.1712076. This article has 1 citations.

37. (mei2026branchedchainaminoacids pages 5-6): Jie Mei, Fu-yuan Yang, and Quan Gong. Branched-chain amino acids and insulin resistance in type 2 diabetes: from metabolic dysregulation to therapeutic targets. Frontiers in Endocrinology, Feb 2026. URL: https://doi.org/10.3389/fendo.2025.1643231, doi:10.3389/fendo.2025.1643231. This article has 4 citations.

38. (mei2026branchedchainaminoacids pages 1-2): Jie Mei, Fu-yuan Yang, and Quan Gong. Branched-chain amino acids and insulin resistance in type 2 diabetes: from metabolic dysregulation to therapeutic targets. Frontiers in Endocrinology, Feb 2026. URL: https://doi.org/10.3389/fendo.2025.1643231, doi:10.3389/fendo.2025.1643231. This article has 4 citations.

39. (mei2026branchedchainaminoacids pages 2-3): Jie Mei, Fu-yuan Yang, and Quan Gong. Branched-chain amino acids and insulin resistance in type 2 diabetes: from metabolic dysregulation to therapeutic targets. Frontiers in Endocrinology, Feb 2026. URL: https://doi.org/10.3389/fendo.2025.1643231, doi:10.3389/fendo.2025.1643231. This article has 4 citations.

40. (mei2026branchedchainaminoacids pages 6-8): Jie Mei, Fu-yuan Yang, and Quan Gong. Branched-chain amino acids and insulin resistance in type 2 diabetes: from metabolic dysregulation to therapeutic targets. Frontiers in Endocrinology, Feb 2026. URL: https://doi.org/10.3389/fendo.2025.1643231, doi:10.3389/fendo.2025.1643231. This article has 4 citations.

## Artifacts

- [Edison artifact artifact-00](BCAT2-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](BCAT2-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. conway2021emergingmoonlightingfunctions pages 3-5
2. conway2021emergingmoonlightingfunctions pages 9-11
3. bo2024primaryrolesof pages 9-11
4. conway2021emergingmoonlightingfunctions pages 47-51
5. conway2021emergingmoonlightingfunctions pages 7-9
6. conway2021emergingmoonlightingfunctions pages 11-13
7. conway2021emergingmoonlightingfunctions pages 55-56
8. conway2021emergingmoonlightingfunctions pages 15-17
9. bo2024primaryrolesof pages 11-13
10. sperringer2017branchedchainaminoacids pages 1-2
11. zhang2026branchedchainaminoacid pages 4-5
12. knerr2019expandingthegenetic pages 8-9
13. knerr2019expandingthegenetic pages 4-5
14. wang2021branchedchainaminoacid pages 1-2
15. zhang2026branchedchainaminoacid pages 13-14
16. zhang2026branchedchainaminoacid pages 11-13
17. mei2026branchedchainaminoacids pages 6-8
18. conway2021emergingmoonlightingfunctions pages 13-15
19. sperringer2017branchedchainaminoacids pages 6-7
20. knerr2019expandingthegenetic pages 2-4
21. knerr2019expandingthegenetic pages 5-7
22. knerr2019expandingthegenetic pages 7-8
23. bo2024primaryrolesof pages 18-19
24. sperringer2017branchedchainaminoacids pages 4-6
25. conway2021emergingmoonlightingfunctions pages 17-19
26. conway2021emergingmoonlightingfunctions pages 1-3
27. mei2026branchedchainaminoacids pages 3-5
28. sperringer2017branchedchainaminoacids pages 2-4
29. conway2021emergingmoonlightingfunctions pages 5-7
30. knerr2019expandingthegenetic pages 1-2
31. haydar2018branchedchainamino pages 2-4
32. he2026bcaasandrelated pages 7-8
33. zhang2026branchedchainaminoacid pages 15-17
34. mei2026branchedchainaminoacids pages 5-6
35. mei2026branchedchainaminoacids pages 1-2
36. mei2026branchedchainaminoacids pages 2-3
37. https://doi.org/10.3390/molecules30010056,
38. https://doi.org/10.1089/ars.2020.8118,
39. https://doi.org/10.1007/s11064-017-2261-5,
40. https://doi.org/10.1002/jimd.12135,
41. https://doi.org/10.1038/s41418-020-00644-4,
42. https://doi.org/10.1038/s41392-020-0168-0,
43. https://doi.org/10.3389/fendo.2025.1643231,
44. https://doi.org/10.3389/fcell.2026.1712076,
45. https://doi.org/10.4183/aeb.2018.238,
46. https://doi.org/10.3389/fcell.2026.1748587,