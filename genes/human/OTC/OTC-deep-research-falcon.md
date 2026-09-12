---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-05T12:48:25.917869'
end_time: '2026-07-05T13:05:56.505604'
duration_seconds: 1050.59
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: OTC
  gene_symbol: OTC
  uniprot_accession: P00480
  protein_description: 'RecName: Full=Ornithine transcarbamylase, mitochondrial {ECO:0000305|PubMed:3895227,
    ECO:0000305|PubMed:6372096}; Short=OTCase {ECO:0000303|PubMed:6372096}; EC=2.1.3.3
    {ECO:0000269|PubMed:2556444, ECO:0000269|PubMed:6372096, ECO:0000269|PubMed:8112735};
    AltName: Full=Ornithine carbamoyltransferase, mitochondrial; Flags: Precursor;'
  gene_info: Name=OTC {ECO:0000312|HGNC:HGNC:8512};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the aspartate/ornithine carbamoyltransferase
  protein_domains: Asp/Orn_carbamoyltranf_P-bd. (IPR006132); Asp/Orn_carbamoylTrfase.
    (IPR006130); Asp/Orn_carbamoylTrfase_sf. (IPR036901); Asp_carbamoyltransf_Asp/Orn-bd.
    (IPR006131); Orn/put_carbamltrans. (IPR002292)
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
  path: OTC-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** P00480
- **Protein Description:** RecName: Full=Ornithine transcarbamylase, mitochondrial {ECO:0000305|PubMed:3895227, ECO:0000305|PubMed:6372096}; Short=OTCase {ECO:0000303|PubMed:6372096}; EC=2.1.3.3 {ECO:0000269|PubMed:2556444, ECO:0000269|PubMed:6372096, ECO:0000269|PubMed:8112735}; AltName: Full=Ornithine carbamoyltransferase, mitochondrial; Flags: Precursor;
- **Gene Information:** Name=OTC {ECO:0000312|HGNC:HGNC:8512};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the aspartate/ornithine carbamoyltransferase
- **Key Domains:** Asp/Orn_carbamoyltranf_P-bd. (IPR006132); Asp/Orn_carbamoylTrfase. (IPR006130); Asp/Orn_carbamoylTrfase_sf. (IPR036901); Asp_carbamoyltransf_Asp/Orn-bd. (IPR006131); Orn/put_carbamltrans. (IPR002292)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "OTC" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'OTC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **OTC** (gene ID: OTC, UniProt: P00480) in human.

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
- **UniProt Accession:** P00480
- **Protein Description:** RecName: Full=Ornithine transcarbamylase, mitochondrial {ECO:0000305|PubMed:3895227, ECO:0000305|PubMed:6372096}; Short=OTCase {ECO:0000303|PubMed:6372096}; EC=2.1.3.3 {ECO:0000269|PubMed:2556444, ECO:0000269|PubMed:6372096, ECO:0000269|PubMed:8112735}; AltName: Full=Ornithine carbamoyltransferase, mitochondrial; Flags: Precursor;
- **Gene Information:** Name=OTC {ECO:0000312|HGNC:HGNC:8512};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the aspartate/ornithine carbamoyltransferase
- **Key Domains:** Asp/Orn_carbamoyltranf_P-bd. (IPR006132); Asp/Orn_carbamoylTrfase. (IPR006130); Asp/Orn_carbamoylTrfase_sf. (IPR036901); Asp_carbamoyltransf_Asp/Orn-bd. (IPR006131); Orn/put_carbamltrans. (IPR002292)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "OTC" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'OTC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **OTC** (gene ID: OTC, UniProt: P00480) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: Human Ornithine Transcarbamylase (OTC)

**Gene:** OTC | **UniProt:** P00480 | **EC:** 2.1.3.3 | **Organism:** *Homo sapiens*

---

## 1. Gene Identity and Genomic Organization

The human OTC gene is located on the short arm of the X chromosome at position Xp21.1, spans approximately 73 kb, and contains 10 exons and 9 introns (diazmunoz2010molecularandbiochemical pages 2-3, arranz2007estimationofthe pages 1-2, couchet2021ornithinetranscarbamylase– pages 3-4). Exon 3 encodes the carbamoyl phosphate (CP)-binding site, while exon 9 encodes the ornithine (ORN)-binding site (couchet2021ornithinetranscarbamylase– pages 3-4). The gene encodes a 354-residue precursor polypeptide with a molecular weight of approximately 39.9 kDa (couchet2021ornithinetranscarbamylase– pages 3-4, diazmunoz2010molecularandbiochemical pages 1-2). The X-linked inheritance of the OTC gene has significant clinical implications, as hemizygous males with loss-of-function mutations present with severe disease, while heterozygous females display variable phenotypes influenced by X-chromosome inactivation patterns (yilmaz2023genetictherapyapproaches pages 1-2, couchet2021ornithinetranscarbamylase– pages 7-8).

## 2. Protein Structure and Quaternary Assembly

The key biochemical properties of human OTC are summarized below:

| Property | Human OTC summary |
|---|---|
| Gene symbol | **OTC** (ornithine transcarbamylase) (diazmunoz2010molecularandbiochemical pages 2-3, couchet2021ornithinetranscarbamylase– pages 3-4) |
| UniProt ID | **P00480** |
| EC number | **EC 2.1.3.3** (couchet2021ornithinetranscarbamylase– pages 1-3, couchet2021ornithinetranscarbamylase– pages 7-8) |
| Gene location | **Xp21.1** on the short arm of the X chromosome (arranz2007estimationofthe pages 1-2, couchet2021ornithinetranscarbamylase– pages 3-4) |
| Gene size | **~73 kb** (diazmunoz2010molecularandbiochemical pages 2-3, arranz2007estimationofthe pages 1-2, couchet2021ornithinetranscarbamylase– pages 3-4) |
| Number of exons | **10 exons** and **9 introns** (diazmunoz2010molecularandbiochemical pages 2-3, arranz2007estimationofthe pages 1-2, couchet2021ornithinetranscarbamylase– pages 3-4) |
| Precursor molecular weight | **~39.9 kDa** precursor (couchet2021ornithinetranscarbamylase– pages 3-4, diazmunoz2010molecularandbiochemical pages 1-2) |
| Mature protein molecular weight | **~36.1 kDa** mature protein (couchet2021ornithinetranscarbamylase– pages 3-4) |
| Amino acids | **354 aa precursor**; **322 aa mature** reported in older review and gene-structure sources, and **321 aa mature** reported in a newer review after leader peptide cleavage (32 aa leader) (diazmunoz2010molecularandbiochemical pages 2-3, arranz2007estimationofthe pages 1-2, couchet2021ornithinetranscarbamylase– pages 3-4) |
| Quaternary structure | **Obligate homotrimer**; dish-like trimer with 3-fold symmetry; active sites formed at subunit interfaces (couchet2021ornithinetranscarbamylase– pages 4-6, couchet2021ornithinetranscarbamylase– pages 1-3, diazmunoz2010molecularandbiochemical pages 1-2) |
| Subcellular localization | **Mitochondrial matrix**, with partial/non-covalent association to the **inner mitochondrial membrane** and participation in multienzyme/channeling assemblies (couchet2021ornithinetranscarbamylase– pages 3-4, couchet2021ornithinetranscarbamylase– pages 4-6, couchet2021ornithinetranscarbamylase– pages 1-3) |
| Primary tissues of expression | Highest physiologic expression/activity in **liver** and **small intestine/intestinal mucosa** (couchet2021ornithinetranscarbamylase– pages 1-3, couchet2021ornithinetranscarbamylase– pages 4-6, erdal2025aminoacidmetabolism pages 10-12) |
| Km for carbamoyl phosphate | Reported **0.26 mM** in a recent review; older review cites **26 μM** (couchet2021ornithinetranscarbamylase– pages 6-7, diazmunoz2010molecularandbiochemical pages 1-2) |
| Km for ornithine | Reported **0.4 mM** in a recent review; older review cites **40 μM** (couchet2021ornithinetranscarbamylase– pages 6-7, diazmunoz2010molecularandbiochemical pages 1-2) |
| pH optimum | **~pH 8** (diazmunoz2010molecularandbiochemical pages 2-3) |
| Reaction catalyzed | **Carbamoyl phosphate + L-ornithine → L-citrulline + phosphate (+ H⁺)**; transfer of the carbamoyl group to the δ-amino group of ornithine (couchet2021ornithinetranscarbamylase– pages 6-7, couchet2021ornithinetranscarbamylase– pages 4-6, couchet2021ornithinetranscarbamylase– pages 1-3) |
| Key catalytic residues / motifs | Active site spans adjacent subunits; important residues/motifs include **Asp231**, **His168**, **Arg141**, **Arg330**, **Cys303**, **Leu304**; conserved **STRTR** motif in the carbamoyl-phosphate-binding region and **HCLP** motif in the ornithine-binding/catalytic region (shi2000crystalstructureof pages 4-6, allewell1999molecularrecognitionby pages 4-6, diazmunoz2010molecularandbiochemical pages 1-2) |
| Inhibitors | **L-norvaline** (reported **Ki = 71 μM**), **L-α-aminobutyrate**, **γ-aminobutyrate**, **L-leucine**, **L-isoleucine**, **L-valine**, **L-lysine** (alternative substrate/inhibitory competitor), **inorganic phosphate** (product inhibition), **Zn(II)**, and reducing agents (couchet2021ornithinetranscarbamylase– pages 6-7, diazmunoz2010molecularandbiochemical pages 1-2) |


*Table: This table summarizes the core biochemical, structural, genetic, and localization properties of human ornithine transcarbamylase (OTC). It is useful as a quick reference for functional annotation and for distinguishing catalytic mechanism, cellular context, and clinically relevant biochemical features.*

### Domain Organization

Each OTC monomer has a bilobal structure composed of two distinct structural domains surrounding a deep cleft: an N-terminal domain that binds CP and a C-terminal domain that binds ORN (couchet2021ornithinetranscarbamylase– pages 3-4, couchet2021ornithinetranscarbamylase– pages 4-6). Both domains share an αβα-topology with a central 5-stranded parallel β-sheet flanked by α-helices, organized as a 3-layer (α/β) sandwich structure (diazmunoz2010molecularandbiochemical pages 1-2, couchet2021ornithinetranscarbamylase– pages 4-6). The two domains are connected by two long interdomain helices (h5 and h12) (couchet2021ornithinetranscarbamylase– pages 4-6). The N-terminal domain contains a conserved Ser-Thr-Arg-Thr-Arg (STRTR) motif for CP binding, while the C-terminal domain contains the conserved Leu-His-Cys-Leu-Pro (LHCLP) motif critical for catalysis (diazmunoz2010molecularandbiochemical pages 1-2). Additionally, human OTC contains an internal trefoil knot structure that contributes to protein stability (diazmunoz2010molecularandbiochemical pages 2-3).

### Trimeric Assembly

The mature protein assembles into obligate homotrimers forming a dish-like structure with 3-fold rotational symmetry and approximately 100 Å diameter (couchet2021ornithinetranscarbamylase– pages 4-6). All three active sites open to the concave face of the dish-like structure, and importantly, active sites are formed at the interfaces between adjacent monomers, with each active site receiving contributions from residues of a neighboring subunit (diazmunoz2010molecularandbiochemical pages 1-2, couchet2021ornithinetranscarbamylase– pages 4-6). This trimeric assembly is obligatory for catalytic function (couchet2021ornithinetranscarbamylase– pages 4-6).

The crystal structure of human OTC complexed with CP and the ornithine analog L-norvaline has been resolved at 1.9 Å resolution, providing detailed insight into the active site architecture and catalytic mechanism (shi2000crystalstructureof pages 4-6).

## 3. Enzymatic Reaction and Catalytic Mechanism

### Reaction Catalyzed

OTC (EC 2.1.3.3) is a carbamoyl transferase that catalyzes the transfer of a carbamoyl group from carbamoyl phosphate to the δ-amino group of L-ornithine, producing L-citrulline, inorganic phosphate, and a proton (couchet2021ornithinetranscarbamylase– pages 6-7, couchet2021ornithinetranscarbamylase– pages 4-6, couchet2021ornithinetranscarbamylase– pages 1-3). This reaction is highly thermodynamically favorable, with a ΔG° of approximately −63 kcal/mol (couchet2021ornithinetranscarbamylase– pages 6-7).

### Kinetic Mechanism

The reaction follows an ordered bi-bi mechanism with Michaelis-Menten kinetics. CP binds first to the deeper pocket of the active site, forming a binary complex that induces a global closure of the active site cleft between the two domains (couchet2021ornithinetranscarbamylase– pages 6-7, couchet2021ornithinetranscarbamylase– pages 4-6). This conformational change then allows ORN binding, which triggers a further induced-fit mechanism moving the SMG loop to shield and fix the active site (couchet2021ornithinetranscarbamylase– pages 4-6). Product release is also ordered, with citrulline released before inorganic phosphate (couchet2021ornithinetranscarbamylase– pages 6-7). The Km values for the substrates have been reported as 0.26 mM for CP and 0.4 mM for ORN at pH 7.7 (couchet2021ornithinetranscarbamylase– pages 6-7), with optimal catalytic activity around pH 8 (diazmunoz2010molecularandbiochemical pages 2-3).

### Catalytic Residues and Mechanism

The catalytic mechanism involves several key steps. The δ-amino group of ornithine performs a nucleophilic attack on the carbonyl carbon of CP (couchet2021ornithinetranscarbamylase– pages 4-6, allewell1999molecularrecognitionby pages 4-6). Cys-303 functions as a general base, abstracting a proton from the δ-amino group of ornithine; the basicity of Cys-303 is enhanced by a hydrogen bond to Asp-263 (shi2000crystalstructureof pages 4-6, allewell1999molecularrecognitionby pages 4-6). A tetrahedral intermediate is formed and stabilized by positively charged residues His-168, Arg-141, and Arg-330, which interact with the partially negatively charged carbonyl oxygen of CP (shi2000crystalstructureof pages 4-6). His-168 also participates in proton transfer to facilitate product release (shi2000crystalstructureof pages 4-6). The residues C303 and L304 stabilize the transition state (couchet2021ornithinetranscarbamylase– pages 4-6). Additional key substrate-binding residues include Asp-231, Met-236, Leu-125, Ser-235, and Asn-167, which form the ORN-binding pocket through electrostatic, hydrophobic, and hydrogen-bonding interactions (allewell1999molecularrecognitionby pages 4-6).

### Substrate Specificity and Inhibition

While OTC is highly specific for L-ornithine, the enzyme can also accept other basic amino acids as alternative substrates. Notably, L-lysine can serve as an alternative substrate, producing homocitrulline (couchet2021ornithinetranscarbamylase– pages 6-7). OTC activity is competitively inhibited by several amino acids, including L-norvaline (Ki = 71 μM), L-α-aminobutyrate, γ-aminobutyrate, L-leucine, L-isoleucine, and L-valine (couchet2021ornithinetranscarbamylase– pages 6-7, diazmunoz2010molecularandbiochemical pages 1-2). Inorganic phosphate acts as a product inhibitor, and the enzyme is also inhibited by Zn(II) and reducing agents (diazmunoz2010molecularandbiochemical pages 1-2).

## 4. Subcellular Localization and Mitochondrial Import

### Mitochondrial Targeting and Import

OTC is encoded by a nuclear gene and synthesized as a 39.9 kDa precursor protein (pre-OTC) on free ribosomes in the cytoplasm (mori1982ornithinetranscarbamylasein pages 1-3, mori1982ornithinetranscarbamylasein pages 3-4). The precursor contains a canonical N-terminal signal peptide of 32 amino acids (approximately 3,400–4,000 daltons) that serves as a mitochondrial targeting sequence (couchet2021ornithinetranscarbamylase– pages 3-4, mori1982ornithinetranscarbamylasein pages 1-3). After synthesis, the precursor is released into the cytosol and then transported across both the outer and inner mitochondrial membranes into the matrix in an energy-dependent process requiring membrane potential, mitochondrial integrity, potassium and magnesium ions, cytosolic proteins, and specific mitochondrial matrix proteases (mori1982ornithinetranscarbamylasein pages 1-3, mori1982ornithinetranscarbamylasein pages 9-12). The half-life of the precursor in the cytosol is approximately 12 minutes (mori1982ornithinetranscarbamylasein pages 1-3). Processing of the precursor to the mature 36.1 kDa form occurs during, rather than after, transport into mitochondria, mediated by processing proteases located mainly in the matrix and partly in the intermembrane space (mori1982ornithinetranscarbamylasein pages 9-12).

### Localization Within Mitochondria

The mature OTC protein resides in the mitochondrial matrix, where it assembles into homotrimers and attaches to the inner mitochondrial membrane through non-covalent interactions with anionic phospholipids, particularly cardiolipin (couchet2021ornithinetranscarbamylase– pages 3-4, couchet2021ornithinetranscarbamylase– pages 4-6, couchet2021ornithinetranscarbamylase– pages 1-3). In liver tissue, OTC represents approximately 3–4% of total mitochondrial proteins, and the half-life of active OTC in rat liver ranges from 6–9 days (couchet2021ornithinetranscarbamylase– pages 3-4). Importantly, OTC co-localizes with carbamoyl phosphate synthetase 1 (CPS1) at the inner membrane, forming part of a multi-enzyme channeling assembly with other mitochondrial urea cycle enzymes (NAGS, CPS1, and OTC) that facilitates metabolite flux (couchet2021ornithinetranscarbamylase– pages 4-6).

### Tissue Distribution

OTC is predominantly expressed in two organs: the liver, where it functions as an integral part of the urea cycle for ammonia detoxification, and the small intestine, where it synthesizes citrulline for systemic export (couchet2021ornithinetranscarbamylase– pages 1-3, couchet2021ornithinetranscarbamylase– pages 4-6). Hepatic OTC activity is substantially higher than intestinal activity (4,110 μmol·g⁻¹·h⁻¹ in liver vs. 100 μmol·g⁻¹·h⁻¹ in intestinal mucosa) (couchet2021ornithinetranscarbamylase– pages 6-7). Under certain pathological conditions, such as hepatotoxicity or active liver regeneration, OTC can be released from mitochondria into the bloodstream, where it may function as a signaling molecule (diazmunoz2010molecularandbiochemical pages 1-2).

## 5. Role in the Urea Cycle and Metabolic Pathways

### The Urea Cycle

OTC catalyzes the second step of the hepatic urea cycle, directly downstream of CPS1, which catalyzes the rate-limiting first step by producing CP from ammonia, bicarbonate, and ATP (couchet2021ornithinetranscarbamylase– pages 4-6, erdal2025aminoacidmetabolism pages 10-12). The citrulline produced by OTC is then exported from the mitochondrial matrix to the cytosol, where it is condensed with aspartate by argininosuccinate synthetase (ASS1), cleaved by argininosuccinate lyase (ASL) to produce arginine and fumarate, and finally hydrolyzed by arginase to yield urea and regenerate ornithine, completing the cycle (couchet2021ornithinetranscarbamylase– pages 1-3). Ornithine is imported back into the mitochondrial matrix via the ornithine carriers ORC1/ORNT1 and ORC2/ORNT2 located in the inner mitochondrial membrane and is channeled directly to OTC bound at this location (couchet2021ornithinetranscarbamylase– pages 4-6).

### Intestinal Citrulline Production

In the intestine, OTC plays a distinct role from its hepatic function. Intestinal OTC synthesizes citrulline that is exported systemically into the plasma rather than being channeled into a local urea cycle (couchet2021ornithinetranscarbamylase– pages 1-3, couchet2021ornithinetranscarbamylase– pages 8-9). This intestinal citrulline contributes to whole-body arginine biosynthesis through the renal arginine synthesis pathway and plays a major role in amino acid homeostasis, particularly of L-glutamine and L-arginine (couchet2021ornithinetranscarbamylase– pages 1-3, couchet2021ornithinetranscarbamylase– pages 8-9).

### Regulation of OTC Expression and Activity

OTC expression is regulated at multiple levels. Transcriptionally, the OTC gene promoter is activated by hepatocyte nuclear factor 4 (HNF-4) and the mitochondrial metabolism regulator PGC1α, while COUP-TF2 provides inhibitory regulation (couchet2021ornithinetranscarbamylase– pages 1-3). The promoter also contains cAMP response elements and glucocorticoid receptor binding sequences, as well as a urea cycle element (diazmunoz2010molecularandbiochemical pages 2-3). OTC expression responds to nutritional state: high-protein diets increase OTC mRNA and protein expression through mechanisms potentially involving AMPK signaling (couchet2021ornithinetranscarbamylase– pages 3-4). The tumor suppressor p53 represses translation of both CPS1 and OTC (couchet2021ornithinetranscarbamylase– pages 3-4).

Post-translationally, OTC activity is regulated through reversible acetylation: acetylation at K88 reduces enzymatic activity in response to nutrient signals, while Sirt3-mediated deacetylation increases OTC activity during fasting states, thereby linking OTC function to the metabolic demands of the organism (couchet2021ornithinetranscarbamylase– pages 3-4). Additionally, the enzyme shows developmental regulation, with rapid accumulation in the first three weeks of postnatal life in rats, reaching adult levels by weaning (couchet2021ornithinetranscarbamylase– pages 6-7).

## 6. Clinical Significance: OTC Deficiency

### Prevalence and Inheritance

OTC deficiency (OTCD) is an X-linked disorder and the most common urea cycle disorder, accounting for approximately 50% of all urea cycle hereditary disorders (couchet2021ornithinetranscarbamylase– pages 7-8). Prevalence estimates range from 1 in 14,000 to 1 in 80,000 live births (yilmaz2023genetictherapyapproaches pages 1-2, couchet2021ornithinetranscarbamylase– pages 7-8).

### Clinical Manifestations

Hemizygous males with complete OTC deficiency typically present with severe neonatal-onset hyperammonemia, characterized by hypotonia, somnolence, and potentially hyperammonemic coma or death (couchet2021ornithinetranscarbamylase– pages 7-8, yilmaz2023genetictherapyapproaches pages 2-4). Patients with partial OTC deficiency present later with milder symptoms. Heterozygous females display highly variable phenotypes due to random X-chromosome inactivation, ranging from asymptomatic states to severe metabolic and neuropsychiatric manifestations (zarantebahamon2025chronicandvariable pages 5-6). Clinical deterioration is often triggered by catabolic stressors such as febrile illness, infection, or pregnancy (zarantebahamon2025chronicandvariable pages 5-6). Corticosteroid administration can exacerbate hyperammonemia not only through protein catabolism but also by suppressing urea-cycle-related gene expressions (couchet2021ornithinetranscarbamylase– pages 3-4).

### Current Treatments and Gene Therapy

Current standard care includes protein-restricted diets, ammonia scavenger drugs (sodium benzoate, sodium phenylbutyrate), and arginine/citrulline supplementation, though these measures do not prevent all hyperammonemic episodes (yilmaz2023genetictherapyapproaches pages 1-2, couchet2021ornithinetranscarbamylase– pages 7-8, yilmaz2023genetictherapyapproaches pages 2-4). Liver transplantation remains the only currently curative option but is limited by donor shortage, surgical challenges in young infants, and lifelong immunosuppression requirements (yilmaz2023genetictherapyapproaches pages 1-2, yilmaz2023genetictherapyapproaches pages 2-4).

As a well-characterized monogenic disorder, OTCD is a prime candidate for gene therapy. Multiple modalities are under active development, including adeno-associated virus (AAV)-based gene addition therapy, mRNA therapy encapsulated in lipid nanoparticles, and CRISPR/Cas9 genome editing (yilmaz2023genetictherapyapproaches pages 1-2, yilmaz2023genetictherapyapproaches pages 7-9, yilmaz2023genetictherapyapproaches pages 9-10). Phase 3 clinical trials with AAV8 vectors have shown positive outcomes, with patients achieving metabolic stability and discontinuing ammonia-scavenger medications and protein-restricted diets (yilmaz2023genetictherapyapproaches pages 7-9). Restoring even 10% of normal OTC enzyme activity can significantly improve the clinical phenotype (yilmaz2023genetictherapyapproaches pages 2-4). Pharmacological chaperone approaches have also been explored, with recent high-throughput screening identifying compounds that stabilize OTC protein and enhance enzymatic activity and ureagenesis in patient-derived hepatocytes (couchet2021ornithinetranscarbamylase– pages 7-8).

## 7. Emerging Roles in Cancer and Chronic Disease

Beyond its classical role in nitrogen metabolism, OTC has emerging significance in cancer and chronic disease. Many tumor types—including colorectal carcinoma, hepatocellular carcinoma, glioblastoma, and pediatric sarcomas—show deficient OTC expression (couchet2021ornithinetranscarbamylase– pages 8-9). This metabolic reprogramming redirects nitrogen away from the urea cycle toward anabolic pathways that favor tumor growth, simultaneously increasing tumor dependency on exogenous arginine and making arginine deprivation therapy a potential therapeutic approach (couchet2021ornithinetranscarbamylase– pages 8-9). In hepatocellular carcinoma, lower OTC expression correlates with larger tumor size and advanced grade, while OTC silencing increases cell proliferation (couchet2021ornithinetranscarbamylase– pages 9-10). Downregulated OTC expression has also been observed in non-alcoholic steatohepatitis, contributing to hyperammonemia and increased liver fibrosis risk (couchet2021ornithinetranscarbamylase– pages 9-10).

## 8. Summary

Human ornithine transcarbamylase (OTC; P00480) is a mitochondrial matrix enzyme that catalyzes the transfer of a carbamoyl group from carbamoyl phosphate to L-ornithine, producing L-citrulline and inorganic phosphate. This reaction constitutes the second step of the hepatic urea cycle and is essential for ammonia detoxification. OTC is synthesized as a cytoplasmic precursor with an N-terminal mitochondrial targeting peptide, imported into mitochondria, and processed to its mature form, which assembles into obligate homotrimers at the inner mitochondrial membrane. The enzyme is predominantly expressed in liver and intestine, with distinct metabolic roles in each tissue: hepatic ureagenesis and intestinal citrulline export for systemic arginine biosynthesis. OTC activity is regulated transcriptionally by HNF-4 and PGC1α, and post-translationally through reversible acetylation. Deficiency of OTC causes the most common urea cycle disorder, an X-linked condition with significant morbidity and mortality that is now a leading candidate for gene therapy approaches. Emerging evidence also implicates OTC dysregulation in cancer metabolism and chronic liver disease.

References

1. (diazmunoz2010molecularandbiochemical pages 2-3): Mauricio Diaz-Munoz and Rolando Hernandez-Munoz. Molecular and biochemical features of the mitochondrial enzyme ornithine transcarbamylase: a possible new role as a signaling factor. Jul 2010. URL: https://doi.org/10.2174/092986710791331031, doi:10.2174/092986710791331031. This article has 17 citations and is from a peer-reviewed journal.

2. (arranz2007estimationofthe pages 1-2): J. A. Arranz, Encarnació Riudor, C. Marco-Marín, and Vicente Rubio. Estimation of the total number of disease-causing mutations in ornithine transcarbamylase (otc) deficiency. value of the otc structure in predicting a mutation pathogenic potential. Journal of Inherited Metabolic Disease, 30:217-226, Mar 2007. URL: https://doi.org/10.1007/s10545-007-0429-x, doi:10.1007/s10545-007-0429-x. This article has 53 citations and is from a peer-reviewed journal.

3. (couchet2021ornithinetranscarbamylase– pages 3-4): Morgane Couchet, Charlotte Breuillard, Christelle Corne, John Rendu, Béatrice Morio, Uwe Schlattner, and Christophe Moinard. Ornithine transcarbamylase – from structure to metabolism: an update. Frontiers in Physiology, Oct 2021. URL: https://doi.org/10.3389/fphys.2021.748249, doi:10.3389/fphys.2021.748249. This article has 82 citations.

4. (diazmunoz2010molecularandbiochemical pages 1-2): Mauricio Diaz-Munoz and Rolando Hernandez-Munoz. Molecular and biochemical features of the mitochondrial enzyme ornithine transcarbamylase: a possible new role as a signaling factor. Jul 2010. URL: https://doi.org/10.2174/092986710791331031, doi:10.2174/092986710791331031. This article has 17 citations and is from a peer-reviewed journal.

5. (yilmaz2023genetictherapyapproaches pages 1-2): Berna Seker Yilmaz and Paul Gissen. Genetic therapy approaches for ornithine transcarbamylase deficiency. Biomedicines, 11:2227, Aug 2023. URL: https://doi.org/10.3390/biomedicines11082227, doi:10.3390/biomedicines11082227. This article has 36 citations.

6. (couchet2021ornithinetranscarbamylase– pages 7-8): Morgane Couchet, Charlotte Breuillard, Christelle Corne, John Rendu, Béatrice Morio, Uwe Schlattner, and Christophe Moinard. Ornithine transcarbamylase – from structure to metabolism: an update. Frontiers in Physiology, Oct 2021. URL: https://doi.org/10.3389/fphys.2021.748249, doi:10.3389/fphys.2021.748249. This article has 82 citations.

7. (couchet2021ornithinetranscarbamylase– pages 1-3): Morgane Couchet, Charlotte Breuillard, Christelle Corne, John Rendu, Béatrice Morio, Uwe Schlattner, and Christophe Moinard. Ornithine transcarbamylase – from structure to metabolism: an update. Frontiers in Physiology, Oct 2021. URL: https://doi.org/10.3389/fphys.2021.748249, doi:10.3389/fphys.2021.748249. This article has 82 citations.

8. (couchet2021ornithinetranscarbamylase– pages 4-6): Morgane Couchet, Charlotte Breuillard, Christelle Corne, John Rendu, Béatrice Morio, Uwe Schlattner, and Christophe Moinard. Ornithine transcarbamylase – from structure to metabolism: an update. Frontiers in Physiology, Oct 2021. URL: https://doi.org/10.3389/fphys.2021.748249, doi:10.3389/fphys.2021.748249. This article has 82 citations.

9. (erdal2025aminoacidmetabolism pages 10-12): Ranya Erdal, Kıvanç Birsoy, and Gokhan Unlu. Amino acid metabolism in liver mitochondria: from homeostasis to disease. Metabolites, 15:446, Jul 2025. URL: https://doi.org/10.3390/metabo15070446, doi:10.3390/metabo15070446. This article has 7 citations.

10. (couchet2021ornithinetranscarbamylase– pages 6-7): Morgane Couchet, Charlotte Breuillard, Christelle Corne, John Rendu, Béatrice Morio, Uwe Schlattner, and Christophe Moinard. Ornithine transcarbamylase – from structure to metabolism: an update. Frontiers in Physiology, Oct 2021. URL: https://doi.org/10.3389/fphys.2021.748249, doi:10.3389/fphys.2021.748249. This article has 82 citations.

11. (shi2000crystalstructureof pages 4-6): Dashuang Shi, Hiroki Morizono, Mika Aoyagi, Mendel Tuchman, and Norma M. Allewell. Crystal structure of human ornithine transcarbamylase complexed with carbamoyl phosphate and l‐norvaline at 1.9 å resolution. Proteins: Structure, 39:271-277, Jun 2000. URL: https://doi.org/10.1002/(sici)1097-0134(20000601)39:4<271::aid-prot10>3.0.co;2-e, doi:10.1002/(sici)1097-0134(20000601)39:4<271::aid-prot10>3.0.co;2-e. This article has 53 citations.

12. (allewell1999molecularrecognitionby pages 4-6): Norma M. Allewell, Dashuang Shi, Hiroki Morizono, and Mendel Tuchman. Molecular recognition by ornithine and aspartate transcarbamylases. Aug 1999. URL: https://doi.org/10.1021/ar950262j, doi:10.1021/ar950262j. This article has 25 citations and is from a domain leading peer-reviewed journal.

13. (mori1982ornithinetranscarbamylasein pages 1-3): Masataka Mori, Satoshi Miura, Tetsuo Morita, Masaki Takiguchi, and Masamiti Tatibana. Ornithine transcarbamylase in liver mitochondria. Molecular and Cellular Biochemistry, 49:97-111, Nov 1982. URL: https://doi.org/10.1007/bf00242488, doi:10.1007/bf00242488. This article has 62 citations and is from a peer-reviewed journal.

14. (mori1982ornithinetranscarbamylasein pages 3-4): Masataka Mori, Satoshi Miura, Tetsuo Morita, Masaki Takiguchi, and Masamiti Tatibana. Ornithine transcarbamylase in liver mitochondria. Molecular and Cellular Biochemistry, 49:97-111, Nov 1982. URL: https://doi.org/10.1007/bf00242488, doi:10.1007/bf00242488. This article has 62 citations and is from a peer-reviewed journal.

15. (mori1982ornithinetranscarbamylasein pages 9-12): Masataka Mori, Satoshi Miura, Tetsuo Morita, Masaki Takiguchi, and Masamiti Tatibana. Ornithine transcarbamylase in liver mitochondria. Molecular and Cellular Biochemistry, 49:97-111, Nov 1982. URL: https://doi.org/10.1007/bf00242488, doi:10.1007/bf00242488. This article has 62 citations and is from a peer-reviewed journal.

16. (couchet2021ornithinetranscarbamylase– pages 8-9): Morgane Couchet, Charlotte Breuillard, Christelle Corne, John Rendu, Béatrice Morio, Uwe Schlattner, and Christophe Moinard. Ornithine transcarbamylase – from structure to metabolism: an update. Frontiers in Physiology, Oct 2021. URL: https://doi.org/10.3389/fphys.2021.748249, doi:10.3389/fphys.2021.748249. This article has 82 citations.

17. (yilmaz2023genetictherapyapproaches pages 2-4): Berna Seker Yilmaz and Paul Gissen. Genetic therapy approaches for ornithine transcarbamylase deficiency. Biomedicines, 11:2227, Aug 2023. URL: https://doi.org/10.3390/biomedicines11082227, doi:10.3390/biomedicines11082227. This article has 36 citations.

18. (zarantebahamon2025chronicandvariable pages 5-6): Ana María Zarante-Bahamón, Jenniffer A. Romero-Morales, and Jorge Luis Ramón-Gómez. Chronic and variable manifestations of ornithine transcarbamylase deficiency in heterozygous carriers: a case series of three colombian patients. Journal of Inborn Errors of Metabolism and Screening, Jan 2025. URL: https://doi.org/10.1590/2326-4594-jiems-2025-0002, doi:10.1590/2326-4594-jiems-2025-0002. This article has 0 citations.

19. (yilmaz2023genetictherapyapproaches pages 7-9): Berna Seker Yilmaz and Paul Gissen. Genetic therapy approaches for ornithine transcarbamylase deficiency. Biomedicines, 11:2227, Aug 2023. URL: https://doi.org/10.3390/biomedicines11082227, doi:10.3390/biomedicines11082227. This article has 36 citations.

20. (yilmaz2023genetictherapyapproaches pages 9-10): Berna Seker Yilmaz and Paul Gissen. Genetic therapy approaches for ornithine transcarbamylase deficiency. Biomedicines, 11:2227, Aug 2023. URL: https://doi.org/10.3390/biomedicines11082227, doi:10.3390/biomedicines11082227. This article has 36 citations.

21. (couchet2021ornithinetranscarbamylase– pages 9-10): Morgane Couchet, Charlotte Breuillard, Christelle Corne, John Rendu, Béatrice Morio, Uwe Schlattner, and Christophe Moinard. Ornithine transcarbamylase – from structure to metabolism: an update. Frontiers in Physiology, Oct 2021. URL: https://doi.org/10.3389/fphys.2021.748249, doi:10.3389/fphys.2021.748249. This article has 82 citations.

## Artifacts

- [Edison artifact artifact-00](OTC-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. diazmunoz2010molecularandbiochemical pages 2-3
2. diazmunoz2010molecularandbiochemical pages 1-2
3. shi2000crystalstructureof pages 4-6
4. allewell1999molecularrecognitionby pages 4-6
5. mori1982ornithinetranscarbamylasein pages 1-3
6. mori1982ornithinetranscarbamylasein pages 9-12
7. zarantebahamon2025chronicandvariable pages 5-6
8. yilmaz2023genetictherapyapproaches pages 7-9
9. yilmaz2023genetictherapyapproaches pages 2-4
10. arranz2007estimationofthe pages 1-2
11. yilmaz2023genetictherapyapproaches pages 1-2
12. erdal2025aminoacidmetabolism pages 10-12
13. mori1982ornithinetranscarbamylasein pages 3-4
14. yilmaz2023genetictherapyapproaches pages 9-10
15. https://doi.org/10.2174/092986710791331031,
16. https://doi.org/10.1007/s10545-007-0429-x,
17. https://doi.org/10.3389/fphys.2021.748249,
18. https://doi.org/10.3390/biomedicines11082227,
19. https://doi.org/10.3390/metabo15070446,
20. https://doi.org/10.1002/(sici
21. https://doi.org/10.1021/ar950262j,
22. https://doi.org/10.1007/bf00242488,
23. https://doi.org/10.1590/2326-4594-jiems-2025-0002,