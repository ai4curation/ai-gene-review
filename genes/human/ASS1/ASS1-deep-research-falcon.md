---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-05T13:10:15.219680'
end_time: '2026-07-05T13:33:02.628505'
duration_seconds: 1367.41
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: ASS1
  gene_symbol: ASS1
  uniprot_accession: P00966
  protein_description: 'RecName: Full=Argininosuccinate synthase {ECO:0000305}; EC=6.3.4.5
    {ECO:0000269|PubMed:18473344, ECO:0000269|PubMed:27287393, ECO:0000269|PubMed:8792870};
    AltName: Full=Citrulline--aspartate ligase;'
  gene_info: Name=ASS1 {ECO:0000312|HGNC:HGNC:758}; Synonyms=ASS {ECO:0000312|HGNC:HGNC:758};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the argininosuccinate synthase family. Type 1
  protein_domains: Arginosuc_syn_C. (IPR048268); Arginosuc_syn_N. (IPR048267); Arginosuc_synth.
    (IPR001518); Arginosuc_synth_CS. (IPR018223); Arginosuc_synth_type_1_subfam. (IPR023434)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 32
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: ASS1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: ASS1-deep-research-falcon_artifacts/artifact-01.md
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
- **UniProt Accession:** P00966
- **Protein Description:** RecName: Full=Argininosuccinate synthase {ECO:0000305}; EC=6.3.4.5 {ECO:0000269|PubMed:18473344, ECO:0000269|PubMed:27287393, ECO:0000269|PubMed:8792870}; AltName: Full=Citrulline--aspartate ligase;
- **Gene Information:** Name=ASS1 {ECO:0000312|HGNC:HGNC:758}; Synonyms=ASS {ECO:0000312|HGNC:HGNC:758};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the argininosuccinate synthase family. Type 1
- **Key Domains:** Arginosuc_syn_C. (IPR048268); Arginosuc_syn_N. (IPR048267); Arginosuc_synth. (IPR001518); Arginosuc_synth_CS. (IPR018223); Arginosuc_synth_type_1_subfam. (IPR023434)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ASS1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ASS1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ASS1** (gene ID: ASS1, UniProt: P00966) in human.

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
- **UniProt Accession:** P00966
- **Protein Description:** RecName: Full=Argininosuccinate synthase {ECO:0000305}; EC=6.3.4.5 {ECO:0000269|PubMed:18473344, ECO:0000269|PubMed:27287393, ECO:0000269|PubMed:8792870}; AltName: Full=Citrulline--aspartate ligase;
- **Gene Information:** Name=ASS1 {ECO:0000312|HGNC:HGNC:758}; Synonyms=ASS {ECO:0000312|HGNC:HGNC:758};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the argininosuccinate synthase family. Type 1
- **Key Domains:** Arginosuc_syn_C. (IPR048268); Arginosuc_syn_N. (IPR048267); Arginosuc_synth. (IPR001518); Arginosuc_synth_CS. (IPR018223); Arginosuc_synth_type_1_subfam. (IPR023434)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ASS1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ASS1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ASS1** (gene ID: ASS1, UniProt: P00966) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: Human ASS1 (Argininosuccinate Synthase 1)

## 1. Gene and Protein Identity

ASS1 (also known as ASS; HGNC:758) encodes argininosuccinate synthase 1 (UniProt: P00966), a 412-residue (~46 kDa) cytosolic enzyme classified under EC 6.3.4.5 (diezfernandez2017mutationsinthe pages 1-6, karlberg2008structureofhuman pages 1-2). The protein belongs to the argininosuccinate synthase family, type 1 subfamily, and is one of the most extensively studied urea cycle enzymes in humans.

The following table summarizes the key properties of ASS1:

| Property | Summary |
|---|---|
| Gene name | **ASS1**; synonym: **ASS** (human argininosuccinate synthase 1) (karlberg2008structureofhuman pages 1-2, diezfernandez2017mutationsinthe pages 1-6) |
| Protein name | **Argininosuccinate synthase 1**; catalyzes argininosuccinate formation in arginine biosynthesis/urea cycle (karlberg2008structureofhuman pages 1-2, fung2025arginineatthe pages 2-3) |
| UniProt ID | **P00966** |
| EC number | **EC 6.3.4.5** (argininosuccinate synthase) (karlberg2008structureofhuman pages 1-2) |
| Organism | **Homo sapiens (Human)** |
| Molecular weight | Monomer is approximately **46 kDa** (diezfernandez2017mutationsinthe pages 1-6) |
| Oligomeric state | **Homotetramer**; tetrameric state is conserved and required for activity (diezfernandez2017mutationsinthe pages 1-6, karlberg2008structureofhuman pages 3-5) |
| Subcellular localization | Primarily **cytosolic**; in liver associated with periportal hepatocyte urea-cycle function; can accumulate in the **nucleus** during DNA damage responses; reported association with **caveolae** in endothelial cells (lim2024ass1metabolicallycontributes pages 6-6, finnie2020investigatingass1and pages 100-105) |
| Primary substrates | **Citrulline**, **L-aspartate**, and **ATP** (karlberg2008structureofhuman pages 1-2, karlberg2008structureofhuman pages 5-6) |
| Primary products | **Argininosuccinate**, **AMP**, and **pyrophosphate (PPi)** (karlberg2008structureofhuman pages 1-2) |
| Catalyzed reaction | ATP-dependent condensation of citrulline with aspartate to form argininosuccinate; rate-limiting step of de novo arginine synthesis and a key urea-cycle step (karlberg2008structureofhuman pages 1-2, delage2010argininedeprivationand pages 2-3) |
| Key active-site residues | Residues implicated in substrate binding/catalysis include **Glu270, Tyr282, Arg127, Asn123, Tyr87, Ser189, Thr119, Gln40**; Arg127 and Asn123 help bind substrates, and domain movement helps position citrulline for attack on ATP (karlberg2008structureofhuman pages 5-6, karlberg2008structureofhuman pages 6-7) |
| Domain architecture | Three-part architecture: **nucleotide-binding domain**, **synthetase domain**, and **C-terminal oligomerization helix** (diezfernandez2017mutationsinthe pages 1-6, karlberg2008structureofhuman pages 3-5) |
| Key regulatory modifications | **CLOCK-mediated acetylation** at **K165/K176** rhythmically inhibits ASS1 activity and drives circadian ureagenesis; **Cys132 nitrosylation** has been reported as an inactivating mammalian regulatory modification (lin2017clockacetylatesass1 pages 8-9, lin2017clockacetylatesass1 pages 3-4, lin2017clockacetylatesass1 pages 6-7, karlberg2008structureofhuman pages 5-6) |
| Major pathway roles | Functions in the **urea cycle**, **de novo arginine biosynthesis**, and **citrulline–NO cycle**; also influences nucleotide synthesis by competing for aspartate and can link ureagenesis to hepatic **AMPK/lipid metabolism** (fung2025arginineatthe pages 2-3, delage2010argininedeprivationand pages 2-3, sun2022argininosuccinatesynthase1 pages 2-4, madiraju2016argininosuccinatesynthetaseregulates pages 5-5) |
| Recent non-canonical functions | In 2024, ASS1 was shown to have a **nuclear DNA-damage-response role**: after DNA damage it accumulates in the nucleus, generates fumarate with ASL, promotes **SMARCC1 succination**, and modulates p53-regulated chromatin accessibility/transcription (lim2024ass1metabolicallycontributes pages 6-6, lim2024ass1metabolicallycontributes pages 4-5) |
| Associated diseases/contexts | **Citrullinemia type I (CTLN1)** from biallelic ASS1 deficiency causes hyperammonemia and elevated citrulline; in cancer, **ASS1 silencing** creates **arginine auxotrophy** and therapeutic vulnerability to arginine deprivation (diezfernandez2017mutationsinthe pages 10-14, diezfernandez2017mutationsinthe pages 14-18, ribas2022hyperammonemiaininherited pages 4-5, rogers2022canonicalandnoncanonical pages 13-17, delage2010argininedeprivationand pages 3-5) |
| PDB structure ID | **2NZ2** (human ASS1 crystal structure) (diezfernandez2017mutationsinthe pages 22-27) |
| Protein family | **Argininosuccinate synthase family**, type 1 subfamily; structurally conserved tetrameric enzyme family (diezfernandez2017mutationsinthe pages 1-6, karlberg2008structureofhuman pages 3-5) |


*Table: This table summarizes the core biochemical, structural, localization, regulatory, and disease-associated properties of human ASS1. It is useful as a compact reference for functional annotation and interpretation of recent ASS1 literature.*

## 2. Enzymatic Function: Reaction, Substrates, and Mechanism

### 2.1 Catalyzed Reaction

ASS1 catalyzes the ATP-dependent condensation of L-citrulline and L-aspartate to form argininosuccinate, with concomitant production of AMP and pyrophosphate (PPi) (karlberg2008structureofhuman pages 1-2). This reaction constitutes the rate-limiting step in both the urea cycle and de novo arginine biosynthesis (delage2010argininedeprivationand pages 2-3). The overall reaction is:

**L-Citrulline + L-Aspartate + ATP → Argininosuccinate + AMP + PPi**

### 2.2 Catalytic Mechanism

The crystal structure of human ASS1 (PDB: 2NZ2), solved at 2.4 Å resolution, reveals the structural basis for catalysis (karlberg2008structureofhuman pages 2-3, karlberg2008structureofhuman pages 5-6). The mechanism proceeds through an ATP-dependent, two-step process. ATP binds to the nucleotide-binding domain, triggering a conformational change in which this domain approaches the synthetase domain in a hinge-like movement (lakhalnaouar2012leishmaniadonovaniargininosuccinate pages 2-3). In the human enzyme, the nucleophilic oxygen atom of citrulline is positioned approximately 4.8 Å from the ATP α-phosphate, considerably shorter than the 7.9 Å distance observed in bacterial ASS, suggesting that smaller conformational changes are required for catalysis in the human enzyme (karlberg2008structureofhuman pages 5-6). During catalysis, citrulline undergoes nucleophilic attack on the α-phosphate of ATP, forming a citrullyl-AMP intermediate, which is subsequently attacked by the amino group of aspartate to yield argininosuccinate.

Key active-site residues involved in substrate binding and catalysis include Glu270, Tyr282, Arg127, Asn123, Tyr87, and Ser189, which coordinate citrulline through salt bridges and hydrogen bonds (karlberg2008structureofhuman pages 5-6). Aspartate is coordinated by Asn123 and Thr119, while Gln40 forms a hydrogen bond with the adenine moiety of ATP (karlberg2008structureofhuman pages 5-6, karlberg2008structureofhuman pages 6-7). A conserved mammalian residue, Cys132, positioned approximately 10.1 Å from ATP, can undergo S-nitrosylation, providing a mechanism for feedback inhibition by nitric oxide (karlberg2008structureofhuman pages 5-6, diezfernandez2017mutationsinthe pages 22-27).

## 3. Structural Biology

### 3.1 Domain Architecture

Each ASS1 monomer comprises three distinct structural domains: (i) an N-terminal nucleotide-binding domain containing an ATP pyrophosphatase consensus sequence, (ii) a central synthetase domain that harbors the substrate-binding cavity for citrulline and aspartate, and (iii) a C-terminal α-helical oligomerization domain that mediates tetramerization (diezfernandez2017mutationsinthe pages 1-6, karlberg2008structureofhuman pages 3-5, lakhalnaouar2012leishmaniadonovaniargininosuccinate pages 2-3). The two catalytic domains are tightly integrated, with helices from the nucleotide-binding domain traversing through the synthetase domain core (karlberg2008structureofhuman pages 3-5).

### 3.2 Quaternary Structure

ASS1 functions as a homotetramer composed of two identical dimers (karlberg2008structureofhuman pages 3-5). The dimer interface is formed exclusively between synthetase domains and involves helices 10 and 11, strands 11 and 14, a β-hairpin (residues 84–87), and an extended loop (residues 198–202), stabilized by two sets of five salt bridges and numerous polar interactions (karlberg2008structureofhuman pages 3-5). The tetramer interface is primarily hydrophobic, formed by helices 11 and 12 from the synthetase domains and helix 14 from the C-terminal oligomerization tail, surrounding a solvent-filled central cavity (karlberg2008structureofhuman pages 3-5). Mutations affecting the oligomerization helix, such as p.Gly390Arg, abolish enzymatic activity, demonstrating the essential nature of the tetrameric assembly (diezfernandez2017mutationsinthe pages 1-6, diezfernandez2017mutationsinthe pages 10-14).

## 4. Subcellular Localization

### 4.1 Cytosolic Localization

ASS1 is primarily a cytosolic enzyme in most tissues (finnie2020investigatingass1and pages 100-105, lim2024ass1metabolicallycontributes pages 6-6). In the liver, it functions within the cytosol of periportal hepatocytes as part of the urea cycle, where it is highly expressed (finnie2020investigatingass1and pages 100-105, diezfernandez2017mutationsinthe pages 10-14). In the kidney, ASS1 is predominantly cytosolic and confined to proximal tubular epithelial cells across all three segments of the proximal tubule, with very low expression in the rest of the nephron (finnie2020investigatingass1and pages 100-105). In endothelial cells, ASS1 associates with caveolae at relatively low expression levels, where it supports nitric oxide synthesis by coupling with NOS isoforms (finnie2020investigatingass1and pages 100-105).

### 4.2 Nuclear Localization

A landmark 2024 study by Lim et al. in *Nature Metabolism* revealed that ASS1 also functions in the nucleus following DNA damage (lim2024ass1metabolicallycontributes pages 6-6, lim2024ass1metabolicallycontributes pages 4-5). Upon DNA damage induction (e.g., by doxorubicin), ASS1 is translocated to the nucleus via the importin IPO7 in a partially p53-dependent manner (lim2024ass1metabolicallycontributes pages 4-5, lim2024ass1metabolicallycontributes pages 2-3). In the nucleus, ASS1 is chromatin-bound and its binding intensifies upon DNA damage (lim2024ass1metabolicallycontributes pages 6-6).

## 5. Biological Pathways and Functions

The following table provides a comprehensive summary of the metabolic pathways and biological processes involving ASS1:

| Pathway/Process | Role of ASS1 | Tissue Context | Key Interacting Enzymes/Proteins | References |
|---|---|---|---|---|
| Urea cycle (ammonia detoxification) | Catalyzes the ATP-dependent condensation of citrulline and aspartate to form argininosuccinate, a rate-limiting cytosolic step of the urea cycle that supports ammonia disposal as urea. | Highest functional importance in liver, especially periportal hepatocytes; also relevant in inherited urea-cycle disease. | ASL, CPS1, OTC, ARG1 | (karlberg2008structureofhuman pages 1-2, delage2010argininedeprivationand pages 2-3, diezfernandez2017mutationsinthe pages 10-14, diezfernandez2017mutationsinthe pages 14-18) |
| De novo arginine biosynthesis | Produces argininosuccinate for subsequent conversion to arginine, supporting endogenous arginine synthesis from citrulline and aspartate. | Broadly expressed across tissues; especially important in kidney for systemic arginine production and in liver for integrated nitrogen metabolism. | ASL, citrulline supply pathways | (fung2025arginineatthe pages 2-3, finnie2020investigatingass1and pages 100-105, sun2022argininosuccinatesynthase1 pages 1-2) |
| Citrulline-NO recycling cycle | Regenerates arginine from citrulline to sustain nitric oxide production; acts as a key control point in the citrulline-NO cycle. | Endothelial and other NO-producing cells; also relevant in liver injury contexts with NOS2 induction. | NOS isoforms, ASL, caveolae-associated partners | (delage2010argininedeprivationand pages 2-3, leung2012argininosuccinatesynthaseconditions pages 3-5, finnie2020investigatingass1and pages 100-105) |
| Aspartate competition/pyrimidine synthesis | Consumes aspartate for argininosuccinate synthesis; when ASS1 is lost or silenced, aspartate is redirected toward pyrimidine/nucleotide biosynthesis, promoting proliferation. | Especially prominent in ASS1-low or ASS1-silenced cancers. | Pyrimidine synthesis network, p53-linked metabolic regulators | (sun2022argininosuccinatesynthase1 pages 2-4, fung2025arginineatthe pages 9-10, rogers2022canonicalandnoncanonical pages 17-21, lim2024ass1metabolicallycontributes pages 6-6) |
| AMPK/lipid metabolism linkage | Couples ureagenesis and amino-acid catabolism to hepatic AMPK activation and lipid oxidation; ASS1 knockdown suppresses ureagenesis and AMPK signaling. | Liver, particularly fasting/protein catabolism metabolic states. | AMPK and downstream hepatic lipid metabolism effectors | (madiraju2016argininosuccinatesynthetaseregulates pages 5-5) |
| Nuclear DNA damage response (p53/SMARCC1) | After DNA damage, ASS1 accumulates in nucleus and cytosol; in nucleus it works with ASL to generate fumarate, promotes SMARCC1 succination, alters SWI/SNF complex behavior, and modulates p53-regulated cell-cycle transcription. | Demonstrated in cultured human cancer cells and supported by liver nuclear studies; relevant to tumor suppression and genome maintenance. | p53, IPO7, ASL, SMARCC1, SNF5, SWI/SNF chromatin-remodeling complex | (lim2024ass1metabolicallycontributes pages 6-6, lim2024ass1metabolicallycontributes pages 4-5, lim2024ass1metabolicallycontributes pages 1-2, lim2024ass1metabolicallycontributes pages 2-3, lim2024ass1metabolicallycontributes pages 7-8) |
| Circadian regulation of ureagenesis (CLOCK acetylation) | Undergoes rhythmic CLOCK/BMAL1-dependent acetylation at K165/K176, which inhibits ASS1 activity and drives circadian oscillation of ureagenesis and arginine-cycle metabolites. | Hepatocytes and mouse liver. | CLOCK, BMAL1, HDACs | (lin2017clockacetylatesass1 pages 8-9, lin2017clockacetylatesass1 pages 10-11, lin2017clockacetylatesass1 pages 3-4, lin2017clockacetylatesass1 pages 6-7, lin2017clockacetylatesass1 pages 4-5, lin2017clockacetylatesass1 pages 9-10) |


*Table: This table summarizes the major metabolic pathways and biological processes involving human ASS1, including canonical urea-cycle functions and newer non-canonical roles in nuclear DNA-damage signaling and circadian regulation. It is useful for functional annotation because it links ASS1 biochemistry to tissue context and interacting partners.*

### 5.1 Urea Cycle

In the hepatic urea cycle, ASS1 catalyzes the cytosolic condensation of citrulline (produced from carbamoyl phosphate and ornithine in the mitochondria by OTC) with aspartate to generate argininosuccinate (karlberg2008structureofhuman pages 1-2, fung2025arginineatthe pages 2-3). This is the rate-limiting step of ureagenesis, which detoxifies neurotoxic ammonia by converting it to urea for renal excretion (delage2010argininedeprivationand pages 2-3, diezfernandez2017mutationsinthe pages 10-14). ASS1 expression is highest in periportal hepatocytes, consistent with the zonation pattern of urea cycle enzymes (diezfernandez2017mutationsinthe pages 10-14).

### 5.2 De Novo Arginine Biosynthesis

Beyond the liver, ASS1 operates together with argininosuccinate lyase (ASL) to convert citrulline and aspartate into arginine (fung2025arginineatthe pages 2-3, finnie2020investigatingass1and pages 100-105). The kidney is the primary site of systemic arginine production in the body, where proximal tubular cells express high levels of ASS1 to convert circulating citrulline (derived from intestinal metabolism of dietary glutamine) into arginine (finnie2020investigatingass1and pages 100-105, fung2025arginineatthe pages 2-3). ASS1 is widely expressed across healthy tissues and supports de novo arginine synthesis in most cell types (fung2025arginineatthe pages 2-3).

### 5.3 Citrulline-NO Recycling Cycle

In nitric oxide (NO)-producing cells, ASS1 participates in the citrulline-NO recycling cycle: nitric oxide synthases (NOS) convert arginine to NO and citrulline, and ASS1 regenerates arginine from citrulline, completing the cycle and sustaining NO production (fung2025arginineatthe pages 2-3, delage2010argininedeprivationand pages 2-3, leung2012argininosuccinatesynthaseconditions pages 3-5). ASS1 functions as a potential enzymatic "switch" that provides substrate for NOS-induced NO synthesis and may have a rate-limiting role in high-output NO generation (leung2012argininosuccinatesynthaseconditions pages 3-5). However, at the whole-body level, citrulline availability—rather than ASS1 activity per se—is the ultimate limiting factor for endogenous arginine and NO synthesis (delage2010argininedeprivationand pages 2-3).

### 5.4 Aspartate Partitioning and Pyrimidine Metabolism

ASS1 competes with pyrimidine/nucleotide biosynthesis pathways for cytosolic aspartate (sun2022argininosuccinatesynthase1 pages 2-4, fung2025arginineatthe pages 9-10, lim2024ass1metabolicallycontributes pages 6-6). When ASS1 is present and active, it diverts aspartate toward argininosuccinate synthesis; when ASS1 is silenced or lost, aspartate is redirected toward pyrimidine nucleotide synthesis, supporting increased cell proliferation and potentially contributing to nucleotide imbalance and mutagenesis (lim2024ass1metabolicallycontributes pages 6-6, rogers2022canonicalandnoncanonical pages 17-21).

### 5.5 AMPK and Hepatic Lipid Metabolism

Madiraju et al. (2016) demonstrated that ASS1 regulates hepatic AMPK, linking protein catabolism and ureagenesis to hepatic lipid metabolism (madiraju2016argininosuccinatesynthetaseregulates pages 5-5). ASS1 knockdown inhibits both ureagenesis and AMPK activity in the liver, suggesting that ASS1 contributes to a protein-sparing metabolic switch during fasting or caloric restriction by connecting amino acid flux to fatty acid oxidation (madiraju2016argininosuccinatesynthetaseregulates pages 5-5).

### 5.6 Nuclear DNA Damage Response

In 2024, Lim et al. discovered a non-canonical nuclear function for ASS1 in the p53-mediated DNA damage response (lim2024ass1metabolicallycontributes pages 6-6, lim2024ass1metabolicallycontributes pages 1-2). Following DNA damage, ASS1 expression is elevated in both the cytosol and nucleus with at least partial dependency on p53 (lim2024ass1metabolicallycontributes pages 1-2, lim2024ass1metabolicallycontributes pages 2-3). In the cytosol, ASS1 metabolically restrains cell cycle progression by restricting nucleotide synthesis through aspartate consumption (lim2024ass1metabolicallycontributes pages 6-6). In the nucleus, ASS1 cooperates with ASL to generate fumarate, which promotes succination of SMARCC1, a subunit of the SWI/SNF chromatin-remodeling complex (lim2024ass1metabolicallycontributes pages 6-6, lim2024ass1metabolicallycontributes pages 5-6). This succination destabilizes the SMARCC1–SNF5 interaction, reducing chromatin accessibility at a subset of p53-regulated cell cycle gene promoters and thereby decreasing their transcription (lim2024ass1metabolicallycontributes pages 6-6, lim2024ass1metabolicallycontributes pages 1-2). Loss of ASS1 results in decreased SMARCC1 succination, enhanced chromatin accessibility, increased DNA damage, and accelerated cell cycle progression, likely contributing to cancer mutagenesis (lim2024ass1metabolicallycontributes pages 6-6, lim2024ass1metabolicallycontributes pages 1-2).

### 5.7 Circadian Regulation of Ureagenesis

Lin et al. (2017) demonstrated that the circadian clock protein CLOCK, facilitated by BMAL1, directly acetylates ASS1 at lysine residues K165 and K176, inhibiting ASS1 enzymatic activity by up to 50% (lin2017clockacetylatesass1 pages 3-4, lin2017clockacetylatesass1 pages 6-7). This acetylation exhibits circadian oscillation in both human cells and mouse liver, driven by rhythmic CLOCK–ASS1 interaction, and is reversed by HDACs (lin2017clockacetylatesass1 pages 8-9, lin2017clockacetylatesass1 pages 4-5). This post-translational modification mechanism drives the circadian rhythm of ureagenesis without altering ASS1 mRNA or protein levels (lin2017clockacetylatesass1 pages 3-4, lin2017clockacetylatesass1 pages 9-10). Acetylation-defective mutants (K165R/K176R) maintain elevated enzymatic activity regardless of CLOCK status, confirming these residues as the critical regulatory sites (lin2017clockacetylatesass1 pages 7-8, lin2017clockacetylatesass1 pages 6-7).

## 6. Post-Translational Regulation

In addition to CLOCK-mediated acetylation at K165/K176, ASS1 is regulated by several other post-translational modifications. Cys132, a conserved mammalian residue, undergoes S-nitrosylation, which inactivates the enzyme and provides a feedback inhibition mechanism linking NO production to arginine biosynthesis (karlberg2008structureofhuman pages 5-6, diezfernandez2017mutationsinthe pages 22-27). Phosphorylation at Ser328 has also been identified as a post-translational modification site (diezfernandez2017mutationsinthe pages 22-27). The p53 tumor suppressor directly transactivates ASS1 expression in response to genotoxic stress, revealing transcriptional regulation linked to cellular stress responses (lim2024ass1metabolicallycontributes pages 2-3).

## 7. Disease Associations

### 7.1 Citrullinemia Type I (CTLN1)

Biallelic loss-of-function mutations in ASS1 cause citrullinemia type I (CTLN1), an autosomal recessive urea cycle disorder with an incidence of approximately 1 in 250,000 live births (ribas2022hyperammonemiaininherited pages 4-5). The clinical spectrum ranges from severe neonatal-onset disease with life-threatening hyperammonemia (lethargy, somnolence, feeding refusal, vomiting, cerebral edema, convulsions, and coma) to milder late-onset forms presenting with recurrent neurological symptoms or even asymptomatic biochemical abnormalities (diezfernandez2017mutationsinthe pages 10-14, diezfernandez2017mutationsinthe pages 14-18). Biochemically, CTLN1 is characterized by markedly elevated plasma citrulline (often >2000 μmol/L), elevated ammonia and glutamine, low plasma arginine, and urinary orotic aciduria (diezfernandez2017mutationsinthe pages 14-18, ribas2022hyperammonemiaininherited pages 4-5). Mutations affecting the oligomerization interface (e.g., p.Gly324Ser, p.Arg363 mutations) tend to cause neonatal-onset disease, while some missense mutations in less critical regions may permit residual activity and milder presentations (diezfernandez2017mutationsinthe pages 10-14).

### 7.2 Cancer and Arginine Auxotrophy

Many aggressive tumors silence ASS1 expression, rendering them arginine-auxotrophic—dependent on extracellular arginine for survival (rogers2022canonicalandnoncanonical pages 13-17, delage2010argininedeprivationand pages 3-5, sun2022argininosuccinatesynthase1 pages 1-2). ASS1 silencing occurs predominantly through epigenetic mechanisms, including CpG island hypermethylation of the ASS1 promoter, HIF-1α-mediated transcriptional repression under hypoxic conditions, METTL14-mediated N6-methyladenosine modification, and miRNA-mediated suppression (sun2022argininosuccinatesynthase1 pages 1-2, sun2022argininosuccinatesynthase1 pages 2-4, rogers2022canonicalandnoncanonical pages 21-25). Tumors with frequent ASS1 loss include melanoma, hepatocellular carcinoma, mesothelioma, sarcomas (up to 88%), renal cell carcinoma, pancreatic cancer, and prostate cancer (delage2010argininedeprivationand pages 3-5, rogers2022canonicalandnoncanonical pages 13-17). The loss of ASS1 redirects aspartate toward pyrimidine synthesis to support proliferation and simultaneously impairs NO-dependent tumor suppressive signaling (sun2022argininosuccinatesynthase1 pages 2-4).

This vulnerability is exploited therapeutically by arginine deprivation therapy using ADI-PEG20 (pegylated arginine deiminase from *Mycoplasma*), which degrades extracellular arginine and selectively kills ASS1-deficient cancer cells (delage2010argininedeprivationand pages 3-5, rogers2022canonicalandnoncanonical pages 17-21, sun2022argininosuccinatesynthase1 pages 4-5). ADI-PEG20 has been evaluated in clinical trials for malignant pleural mesothelioma, pancreatic adenocarcinoma, non-small cell lung cancer, and other ASS1-low tumor types (sun2022argininosuccinatesynthase1 pages 7-7, sun2022argininosuccinatesynthase1 pages 4-5). Resistance mechanisms include ASS1 re-expression via promoter demethylation, autophagy-mediated intracellular arginine recycling, and extracellular vesicle-mediated arginine provision from stromal fibroblasts (rogers2022canonicalandnoncanonical pages 21-25, rogers2022canonicalandnoncanonical pages 13-17).

## 8. Summary

ASS1 is a multifunctional metabolic enzyme whose primary role—the ATP-dependent condensation of citrulline and aspartate to form argininosuccinate—positions it at the nexus of nitrogen metabolism in humans. Operating principally in the cytosol, ASS1 is rate-limiting for the urea cycle, de novo arginine biosynthesis, and the citrulline-NO recycling pathway (fung2025arginineatthe pages 2-3, delage2010argininedeprivationand pages 2-3). Recent research has expanded the functional repertoire of ASS1 to include nuclear roles in the p53-mediated DNA damage response via fumarate-dependent chromatin remodeling (lim2024ass1metabolicallycontributes pages 6-6), circadian regulation of ureagenesis through CLOCK-mediated acetylation (lin2017clockacetylatesass1 pages 3-4), and coupling of ureagenesis to hepatic lipid metabolism through AMPK (madiraju2016argininosuccinatesynthetaseregulates pages 5-5). Loss of ASS1 function underlies the inherited metabolic disorder citrullinemia type I and creates a metabolic vulnerability in numerous cancers that has been therapeutically targeted through arginine deprivation strategies (ribas2022hyperammonemiaininherited pages 4-5, delage2010argininedeprivationand pages 3-5).

References

1. (diezfernandez2017mutationsinthe pages 1-6): Carmen Diez-Fernandez, Véronique Rüfenacht, and Johannes Häberle. Mutations in the human argininosuccinate synthetase (ass1) gene, impact on patients, common changes, and structural considerations. Human Mutation, 38:471-484, May 2017. URL: https://doi.org/10.1002/humu.23184, doi:10.1002/humu.23184. This article has 69 citations and is from a domain leading peer-reviewed journal.

2. (karlberg2008structureofhuman pages 1-2): Tobias Karlberg, Ruairi Collins, Susanne van den Berg, Alex Flores, Martin Hammarström, Martin Högbom, Lovisa Holmberg Schiavone, and Jonas Uppenberg. Structure of human argininosuccinate synthetase. Acta crystallographica. Section D, Biological crystallography, 64 Pt 3:279-86, Mar 2008. URL: https://doi.org/10.1107/s0907444907067455, doi:10.1107/s0907444907067455. This article has 56 citations.

3. (fung2025arginineatthe pages 2-3): Tak Shun Fung, Keun Woo Ryu, and Craig B Thompson. Arginine: at the crossroads of nitrogen metabolism. The EMBO Journal, 44:1275-1293, Feb 2025. URL: https://doi.org/10.1038/s44318-025-00379-3, doi:10.1038/s44318-025-00379-3. This article has 94 citations.

4. (karlberg2008structureofhuman pages 3-5): Tobias Karlberg, Ruairi Collins, Susanne van den Berg, Alex Flores, Martin Hammarström, Martin Högbom, Lovisa Holmberg Schiavone, and Jonas Uppenberg. Structure of human argininosuccinate synthetase. Acta crystallographica. Section D, Biological crystallography, 64 Pt 3:279-86, Mar 2008. URL: https://doi.org/10.1107/s0907444907067455, doi:10.1107/s0907444907067455. This article has 56 citations.

5. (lim2024ass1metabolicallycontributes pages 6-6): Lisha Qiu Jin Lim, Lital Adler, Emma Hajaj, Leandro R. Soria, Rotem Ben-Tov Perry, Naama Darzi, Ruchama Brody, Noa Furth, Michal Lichtenstein, Elizabeta Bab-Dinitz, Ziv Porat, Tevie Melman, Alexander Brandis, Sergey Malitsky, Maxim Itkin, Yael Aylon, Shifra Ben-Dor, Irit Orr, Amir Pri-Or, Rony Seger, Yoav Shaul, Eytan Ruppin, Moshe Oren, Minervo Perez, Jordan Meier, Nicola Brunetti-Pierri, Efrat Shema, Igor Ulitsky, and Ayelet Erez. Ass1 metabolically contributes to the nuclear and cytosolic p53-mediated dna damage response. Nature Metabolism, 6:1294-1309, Jun 2024. URL: https://doi.org/10.1038/s42255-024-01060-5, doi:10.1038/s42255-024-01060-5. This article has 38 citations and is from a domain leading peer-reviewed journal.

6. (finnie2020investigatingass1and pages 100-105): Sarah Louise Finnie. Investigating ass1 and its role in renal fibrosis. ArXiv, Jun 2020. URL: https://doi.org/10.7488/era/258, doi:10.7488/era/258. This article has 0 citations.

7. (karlberg2008structureofhuman pages 5-6): Tobias Karlberg, Ruairi Collins, Susanne van den Berg, Alex Flores, Martin Hammarström, Martin Högbom, Lovisa Holmberg Schiavone, and Jonas Uppenberg. Structure of human argininosuccinate synthetase. Acta crystallographica. Section D, Biological crystallography, 64 Pt 3:279-86, Mar 2008. URL: https://doi.org/10.1107/s0907444907067455, doi:10.1107/s0907444907067455. This article has 56 citations.

8. (delage2010argininedeprivationand pages 2-3): Barbara Delage, Dean A. Fennell, Linda Nicholson, Iain McNeish, Nicholas R. Lemoine, Tim Crook, and Peter W. Szlosarek. Arginine deprivation and argininosuccinate synthetase expression in the treatment of cancer. International Journal of Cancer, 126:2762-2772, Jun 2010. URL: https://doi.org/10.1002/ijc.25202, doi:10.1002/ijc.25202. This article has 524 citations and is from a domain leading peer-reviewed journal.

9. (karlberg2008structureofhuman pages 6-7): Tobias Karlberg, Ruairi Collins, Susanne van den Berg, Alex Flores, Martin Hammarström, Martin Högbom, Lovisa Holmberg Schiavone, and Jonas Uppenberg. Structure of human argininosuccinate synthetase. Acta crystallographica. Section D, Biological crystallography, 64 Pt 3:279-86, Mar 2008. URL: https://doi.org/10.1107/s0907444907067455, doi:10.1107/s0907444907067455. This article has 56 citations.

10. (lin2017clockacetylatesass1 pages 8-9): Ran Lin, Yan Mo, Haihong Zha, Zhipeng Qu, Pancheng Xie, Zheng-Jiang Zhu, Ying Xu, Yue Xiong, and Kun-Liang Guan. Clock acetylates ass1 to drive circadian rhythm of ureagenesis. Molecular cell, 68 1:198-209.e6, Oct 2017. URL: https://doi.org/10.1016/j.molcel.2017.09.008, doi:10.1016/j.molcel.2017.09.008. This article has 84 citations and is from a highest quality peer-reviewed journal.

11. (lin2017clockacetylatesass1 pages 3-4): Ran Lin, Yan Mo, Haihong Zha, Zhipeng Qu, Pancheng Xie, Zheng-Jiang Zhu, Ying Xu, Yue Xiong, and Kun-Liang Guan. Clock acetylates ass1 to drive circadian rhythm of ureagenesis. Molecular cell, 68 1:198-209.e6, Oct 2017. URL: https://doi.org/10.1016/j.molcel.2017.09.008, doi:10.1016/j.molcel.2017.09.008. This article has 84 citations and is from a highest quality peer-reviewed journal.

12. (lin2017clockacetylatesass1 pages 6-7): Ran Lin, Yan Mo, Haihong Zha, Zhipeng Qu, Pancheng Xie, Zheng-Jiang Zhu, Ying Xu, Yue Xiong, and Kun-Liang Guan. Clock acetylates ass1 to drive circadian rhythm of ureagenesis. Molecular cell, 68 1:198-209.e6, Oct 2017. URL: https://doi.org/10.1016/j.molcel.2017.09.008, doi:10.1016/j.molcel.2017.09.008. This article has 84 citations and is from a highest quality peer-reviewed journal.

13. (sun2022argininosuccinatesynthase1 pages 2-4): Naihui Sun and Xing Zhao. Argininosuccinate synthase 1, arginine deprivation therapy and cancer management. Frontiers in Pharmacology, Jul 2022. URL: https://doi.org/10.3389/fphar.2022.935553, doi:10.3389/fphar.2022.935553. This article has 47 citations.

14. (madiraju2016argininosuccinatesynthetaseregulates pages 5-5): Anila K. Madiraju, Tiago Alves, Xiaojian Zhao, Gary W. Cline, Dongyan Zhang, Sanjay Bhanot, Varman T. Samuel, Richard G. Kibbey, and Gerald I. Shulman. Argininosuccinate synthetase regulates hepatic ampk linking protein catabolism and ureagenesis to hepatic lipid metabolism. Proceedings of the National Academy of Sciences, 113:E3423-E3430, May 2016. URL: https://doi.org/10.1073/pnas.1606022113, doi:10.1073/pnas.1606022113. This article has 77 citations and is from a highest quality peer-reviewed journal.

15. (lim2024ass1metabolicallycontributes pages 4-5): Lisha Qiu Jin Lim, Lital Adler, Emma Hajaj, Leandro R. Soria, Rotem Ben-Tov Perry, Naama Darzi, Ruchama Brody, Noa Furth, Michal Lichtenstein, Elizabeta Bab-Dinitz, Ziv Porat, Tevie Melman, Alexander Brandis, Sergey Malitsky, Maxim Itkin, Yael Aylon, Shifra Ben-Dor, Irit Orr, Amir Pri-Or, Rony Seger, Yoav Shaul, Eytan Ruppin, Moshe Oren, Minervo Perez, Jordan Meier, Nicola Brunetti-Pierri, Efrat Shema, Igor Ulitsky, and Ayelet Erez. Ass1 metabolically contributes to the nuclear and cytosolic p53-mediated dna damage response. Nature Metabolism, 6:1294-1309, Jun 2024. URL: https://doi.org/10.1038/s42255-024-01060-5, doi:10.1038/s42255-024-01060-5. This article has 38 citations and is from a domain leading peer-reviewed journal.

16. (diezfernandez2017mutationsinthe pages 10-14): Carmen Diez-Fernandez, Véronique Rüfenacht, and Johannes Häberle. Mutations in the human argininosuccinate synthetase (ass1) gene, impact on patients, common changes, and structural considerations. Human Mutation, 38:471-484, May 2017. URL: https://doi.org/10.1002/humu.23184, doi:10.1002/humu.23184. This article has 69 citations and is from a domain leading peer-reviewed journal.

17. (diezfernandez2017mutationsinthe pages 14-18): Carmen Diez-Fernandez, Véronique Rüfenacht, and Johannes Häberle. Mutations in the human argininosuccinate synthetase (ass1) gene, impact on patients, common changes, and structural considerations. Human Mutation, 38:471-484, May 2017. URL: https://doi.org/10.1002/humu.23184, doi:10.1002/humu.23184. This article has 69 citations and is from a domain leading peer-reviewed journal.

18. (ribas2022hyperammonemiaininherited pages 4-5): Graziela Schmitt Ribas, Franciele Fátima Lopes, Marion Deon, and Carmen Regla Vargas. Hyperammonemia in inherited metabolic diseases. Cellular and Molecular Neurobiology, 42:2593-2610, Oct 2022. URL: https://doi.org/10.1007/s10571-021-01156-6, doi:10.1007/s10571-021-01156-6. This article has 92 citations and is from a peer-reviewed journal.

19. (rogers2022canonicalandnoncanonical pages 13-17): Canonical and Noncanonical Mechanisms of Resistance to Arginine Starvation in Cancer This article has 0 citations.

20. (delage2010argininedeprivationand pages 3-5): Barbara Delage, Dean A. Fennell, Linda Nicholson, Iain McNeish, Nicholas R. Lemoine, Tim Crook, and Peter W. Szlosarek. Arginine deprivation and argininosuccinate synthetase expression in the treatment of cancer. International Journal of Cancer, 126:2762-2772, Jun 2010. URL: https://doi.org/10.1002/ijc.25202, doi:10.1002/ijc.25202. This article has 524 citations and is from a domain leading peer-reviewed journal.

21. (diezfernandez2017mutationsinthe pages 22-27): Carmen Diez-Fernandez, Véronique Rüfenacht, and Johannes Häberle. Mutations in the human argininosuccinate synthetase (ass1) gene, impact on patients, common changes, and structural considerations. Human Mutation, 38:471-484, May 2017. URL: https://doi.org/10.1002/humu.23184, doi:10.1002/humu.23184. This article has 69 citations and is from a domain leading peer-reviewed journal.

22. (karlberg2008structureofhuman pages 2-3): Tobias Karlberg, Ruairi Collins, Susanne van den Berg, Alex Flores, Martin Hammarström, Martin Högbom, Lovisa Holmberg Schiavone, and Jonas Uppenberg. Structure of human argininosuccinate synthetase. Acta crystallographica. Section D, Biological crystallography, 64 Pt 3:279-86, Mar 2008. URL: https://doi.org/10.1107/s0907444907067455, doi:10.1107/s0907444907067455. This article has 56 citations.

23. (lakhalnaouar2012leishmaniadonovaniargininosuccinate pages 2-3): Ines Lakhal-Naouar, Armando Jardim, Rona Strasser, Shen Luo, Yukiko Kozakai, Hira L. Nakhasi, and Robert C. Duncan. Leishmania donovani argininosuccinate synthase is an active enzyme associated with parasite pathogenesis. PLoS Neglected Tropical Diseases, 6:e1849, Oct 2012. URL: https://doi.org/10.1371/journal.pntd.0001849, doi:10.1371/journal.pntd.0001849. This article has 25 citations and is from a domain leading peer-reviewed journal.

24. (lim2024ass1metabolicallycontributes pages 2-3): Lisha Qiu Jin Lim, Lital Adler, Emma Hajaj, Leandro R. Soria, Rotem Ben-Tov Perry, Naama Darzi, Ruchama Brody, Noa Furth, Michal Lichtenstein, Elizabeta Bab-Dinitz, Ziv Porat, Tevie Melman, Alexander Brandis, Sergey Malitsky, Maxim Itkin, Yael Aylon, Shifra Ben-Dor, Irit Orr, Amir Pri-Or, Rony Seger, Yoav Shaul, Eytan Ruppin, Moshe Oren, Minervo Perez, Jordan Meier, Nicola Brunetti-Pierri, Efrat Shema, Igor Ulitsky, and Ayelet Erez. Ass1 metabolically contributes to the nuclear and cytosolic p53-mediated dna damage response. Nature Metabolism, 6:1294-1309, Jun 2024. URL: https://doi.org/10.1038/s42255-024-01060-5, doi:10.1038/s42255-024-01060-5. This article has 38 citations and is from a domain leading peer-reviewed journal.

25. (sun2022argininosuccinatesynthase1 pages 1-2): Naihui Sun and Xing Zhao. Argininosuccinate synthase 1, arginine deprivation therapy and cancer management. Frontiers in Pharmacology, Jul 2022. URL: https://doi.org/10.3389/fphar.2022.935553, doi:10.3389/fphar.2022.935553. This article has 47 citations.

26. (leung2012argininosuccinatesynthaseconditions pages 3-5): Tung Ming Leung, Yongke Lu, Wei Yan, José A. Morón-Concepción, Stephen C. Ward, Xiaodong Ge, Laura Conde de la Rosa, and Natalia Nieto. Argininosuccinate synthase conditions the response to acute and chronic ethanol‐induced liver injury in mice. Hepatology, 55:1596-1609, May 2012. URL: https://doi.org/10.1002/hep.25543, doi:10.1002/hep.25543. This article has 75 citations and is from a highest quality peer-reviewed journal.

27. (fung2025arginineatthe pages 9-10): Tak Shun Fung, Keun Woo Ryu, and Craig B Thompson. Arginine: at the crossroads of nitrogen metabolism. The EMBO Journal, 44:1275-1293, Feb 2025. URL: https://doi.org/10.1038/s44318-025-00379-3, doi:10.1038/s44318-025-00379-3. This article has 94 citations.

28. (rogers2022canonicalandnoncanonical pages 17-21): Canonical and Noncanonical Mechanisms of Resistance to Arginine Starvation in Cancer This article has 0 citations.

29. (lim2024ass1metabolicallycontributes pages 1-2): Lisha Qiu Jin Lim, Lital Adler, Emma Hajaj, Leandro R. Soria, Rotem Ben-Tov Perry, Naama Darzi, Ruchama Brody, Noa Furth, Michal Lichtenstein, Elizabeta Bab-Dinitz, Ziv Porat, Tevie Melman, Alexander Brandis, Sergey Malitsky, Maxim Itkin, Yael Aylon, Shifra Ben-Dor, Irit Orr, Amir Pri-Or, Rony Seger, Yoav Shaul, Eytan Ruppin, Moshe Oren, Minervo Perez, Jordan Meier, Nicola Brunetti-Pierri, Efrat Shema, Igor Ulitsky, and Ayelet Erez. Ass1 metabolically contributes to the nuclear and cytosolic p53-mediated dna damage response. Nature Metabolism, 6:1294-1309, Jun 2024. URL: https://doi.org/10.1038/s42255-024-01060-5, doi:10.1038/s42255-024-01060-5. This article has 38 citations and is from a domain leading peer-reviewed journal.

30. (lim2024ass1metabolicallycontributes pages 7-8): Lisha Qiu Jin Lim, Lital Adler, Emma Hajaj, Leandro R. Soria, Rotem Ben-Tov Perry, Naama Darzi, Ruchama Brody, Noa Furth, Michal Lichtenstein, Elizabeta Bab-Dinitz, Ziv Porat, Tevie Melman, Alexander Brandis, Sergey Malitsky, Maxim Itkin, Yael Aylon, Shifra Ben-Dor, Irit Orr, Amir Pri-Or, Rony Seger, Yoav Shaul, Eytan Ruppin, Moshe Oren, Minervo Perez, Jordan Meier, Nicola Brunetti-Pierri, Efrat Shema, Igor Ulitsky, and Ayelet Erez. Ass1 metabolically contributes to the nuclear and cytosolic p53-mediated dna damage response. Nature Metabolism, 6:1294-1309, Jun 2024. URL: https://doi.org/10.1038/s42255-024-01060-5, doi:10.1038/s42255-024-01060-5. This article has 38 citations and is from a domain leading peer-reviewed journal.

31. (lin2017clockacetylatesass1 pages 10-11): Ran Lin, Yan Mo, Haihong Zha, Zhipeng Qu, Pancheng Xie, Zheng-Jiang Zhu, Ying Xu, Yue Xiong, and Kun-Liang Guan. Clock acetylates ass1 to drive circadian rhythm of ureagenesis. Molecular cell, 68 1:198-209.e6, Oct 2017. URL: https://doi.org/10.1016/j.molcel.2017.09.008, doi:10.1016/j.molcel.2017.09.008. This article has 84 citations and is from a highest quality peer-reviewed journal.

32. (lin2017clockacetylatesass1 pages 4-5): Ran Lin, Yan Mo, Haihong Zha, Zhipeng Qu, Pancheng Xie, Zheng-Jiang Zhu, Ying Xu, Yue Xiong, and Kun-Liang Guan. Clock acetylates ass1 to drive circadian rhythm of ureagenesis. Molecular cell, 68 1:198-209.e6, Oct 2017. URL: https://doi.org/10.1016/j.molcel.2017.09.008, doi:10.1016/j.molcel.2017.09.008. This article has 84 citations and is from a highest quality peer-reviewed journal.

33. (lin2017clockacetylatesass1 pages 9-10): Ran Lin, Yan Mo, Haihong Zha, Zhipeng Qu, Pancheng Xie, Zheng-Jiang Zhu, Ying Xu, Yue Xiong, and Kun-Liang Guan. Clock acetylates ass1 to drive circadian rhythm of ureagenesis. Molecular cell, 68 1:198-209.e6, Oct 2017. URL: https://doi.org/10.1016/j.molcel.2017.09.008, doi:10.1016/j.molcel.2017.09.008. This article has 84 citations and is from a highest quality peer-reviewed journal.

34. (lim2024ass1metabolicallycontributes pages 5-6): Lisha Qiu Jin Lim, Lital Adler, Emma Hajaj, Leandro R. Soria, Rotem Ben-Tov Perry, Naama Darzi, Ruchama Brody, Noa Furth, Michal Lichtenstein, Elizabeta Bab-Dinitz, Ziv Porat, Tevie Melman, Alexander Brandis, Sergey Malitsky, Maxim Itkin, Yael Aylon, Shifra Ben-Dor, Irit Orr, Amir Pri-Or, Rony Seger, Yoav Shaul, Eytan Ruppin, Moshe Oren, Minervo Perez, Jordan Meier, Nicola Brunetti-Pierri, Efrat Shema, Igor Ulitsky, and Ayelet Erez. Ass1 metabolically contributes to the nuclear and cytosolic p53-mediated dna damage response. Nature Metabolism, 6:1294-1309, Jun 2024. URL: https://doi.org/10.1038/s42255-024-01060-5, doi:10.1038/s42255-024-01060-5. This article has 38 citations and is from a domain leading peer-reviewed journal.

35. (lin2017clockacetylatesass1 pages 7-8): Ran Lin, Yan Mo, Haihong Zha, Zhipeng Qu, Pancheng Xie, Zheng-Jiang Zhu, Ying Xu, Yue Xiong, and Kun-Liang Guan. Clock acetylates ass1 to drive circadian rhythm of ureagenesis. Molecular cell, 68 1:198-209.e6, Oct 2017. URL: https://doi.org/10.1016/j.molcel.2017.09.008, doi:10.1016/j.molcel.2017.09.008. This article has 84 citations and is from a highest quality peer-reviewed journal.

36. (rogers2022canonicalandnoncanonical pages 21-25): Canonical and Noncanonical Mechanisms of Resistance to Arginine Starvation in Cancer This article has 0 citations.

37. (sun2022argininosuccinatesynthase1 pages 4-5): Naihui Sun and Xing Zhao. Argininosuccinate synthase 1, arginine deprivation therapy and cancer management. Frontiers in Pharmacology, Jul 2022. URL: https://doi.org/10.3389/fphar.2022.935553, doi:10.3389/fphar.2022.935553. This article has 47 citations.

38. (sun2022argininosuccinatesynthase1 pages 7-7): Naihui Sun and Xing Zhao. Argininosuccinate synthase 1, arginine deprivation therapy and cancer management. Frontiers in Pharmacology, Jul 2022. URL: https://doi.org/10.3389/fphar.2022.935553, doi:10.3389/fphar.2022.935553. This article has 47 citations.

## Artifacts

- [Edison artifact artifact-00](ASS1-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](ASS1-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. karlberg2008structureofhuman pages 1-2
2. diezfernandez2017mutationsinthe pages 1-6
3. diezfernandez2017mutationsinthe pages 22-27
4. delage2010argininedeprivationand pages 2-3
5. lakhalnaouar2012leishmaniadonovaniargininosuccinate pages 2-3
6. karlberg2008structureofhuman pages 5-6
7. karlberg2008structureofhuman pages 3-5
8. madiraju2016argininosuccinatesynthetaseregulates pages 5-5
9. diezfernandez2017mutationsinthe pages 10-14
10. fung2025arginineatthe pages 2-3
11. leung2012argininosuccinatesynthaseconditions pages 3-5
12. ribas2022hyperammonemiaininherited pages 4-5
13. karlberg2008structureofhuman pages 6-7
14. diezfernandez2017mutationsinthe pages 14-18
15. rogers2022canonicalandnoncanonical pages 13-17
16. delage2010argininedeprivationand pages 3-5
17. karlberg2008structureofhuman pages 2-3
18. fung2025arginineatthe pages 9-10
19. rogers2022canonicalandnoncanonical pages 17-21
20. rogers2022canonicalandnoncanonical pages 21-25
21. https://doi.org/10.1002/humu.23184,
22. https://doi.org/10.1107/s0907444907067455,
23. https://doi.org/10.1038/s44318-025-00379-3,
24. https://doi.org/10.1038/s42255-024-01060-5,
25. https://doi.org/10.7488/era/258,
26. https://doi.org/10.1002/ijc.25202,
27. https://doi.org/10.1016/j.molcel.2017.09.008,
28. https://doi.org/10.3389/fphar.2022.935553,
29. https://doi.org/10.1073/pnas.1606022113,
30. https://doi.org/10.1007/s10571-021-01156-6,
31. https://doi.org/10.1371/journal.pntd.0001849,
32. https://doi.org/10.1002/hep.25543,