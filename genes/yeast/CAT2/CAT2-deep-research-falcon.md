---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-30T09:22:35.872613'
end_time: '2026-05-30T09:41:26.931374'
duration_seconds: 1131.06
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: yeast
  gene_id: CAT2
  gene_symbol: CAT2
  uniprot_accession: P32796
  protein_description: 'RecName: Full=Carnitine O-acetyltransferase, mitochondrial
    {ECO:0000303|PubMed:8420957}; Short=Carnitine acetylase {ECO:0000303|PubMed:8420957};
    EC=2.3.1.7 {ECO:0000269|PubMed:8420957}; Flags: Precursor;'
  gene_info: Name=CAT2; Synonyms=CAT, YCAT; OrderedLocusNames=YML042W; ORFNames=YM8054.01;
  organism_full: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
  protein_family: Belongs to the carnitine/choline acetyltransferase family.
  protein_domains: Carn_acyl_trans. (IPR000542); CAT-like_dom_sf. (IPR023213); Cho/carn_acyl_trans.
    (IPR039551); Cho/carn_acyl_trans_2. (IPR042231); Carn_acyltransf (PF00755)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 17
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: CAT2-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** P32796
- **Protein Description:** RecName: Full=Carnitine O-acetyltransferase, mitochondrial {ECO:0000303|PubMed:8420957}; Short=Carnitine acetylase {ECO:0000303|PubMed:8420957}; EC=2.3.1.7 {ECO:0000269|PubMed:8420957}; Flags: Precursor;
- **Gene Information:** Name=CAT2; Synonyms=CAT, YCAT; OrderedLocusNames=YML042W; ORFNames=YM8054.01;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the carnitine/choline acetyltransferase family.
- **Key Domains:** Carn_acyl_trans. (IPR000542); CAT-like_dom_sf. (IPR023213); Cho/carn_acyl_trans. (IPR039551); Cho/carn_acyl_trans_2. (IPR042231); Carn_acyltransf (PF00755)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CAT2" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CAT2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CAT2** (gene ID: CAT2, UniProt: P32796) in yeast.

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
- **UniProt Accession:** P32796
- **Protein Description:** RecName: Full=Carnitine O-acetyltransferase, mitochondrial {ECO:0000303|PubMed:8420957}; Short=Carnitine acetylase {ECO:0000303|PubMed:8420957}; EC=2.3.1.7 {ECO:0000269|PubMed:8420957}; Flags: Precursor;
- **Gene Information:** Name=CAT2; Synonyms=CAT, YCAT; OrderedLocusNames=YML042W; ORFNames=YM8054.01;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the carnitine/choline acetyltransferase family.
- **Key Domains:** Carn_acyl_trans. (IPR000542); CAT-like_dom_sf. (IPR023213); Cho/carn_acyl_trans. (IPR039551); Cho/carn_acyl_trans_2. (IPR042231); Carn_acyltransf (PF00755)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CAT2" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CAT2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CAT2** (gene ID: CAT2, UniProt: P32796) in yeast.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Research Report: Functional Annotation of *Saccharomyces cerevisiae* **CAT2** (UniProt P32796; ORF YML042W)

## 0. Executive summary (verified target)
The research target **CAT2** in *Saccharomyces cerevisiae* (strain S288c; ORF **YML042W**) encodes **Cat2p**, a carnitine O-acetyltransferase/carnitine acetyltransferase that is **dually localized to peroxisomes and mitochondria** and catalyzes **reversible transfer of acetyl groups between acetyl-CoA and L-carnitine**, generating **acetylcarnitine** as a membrane-permeant carrier of acetyl units. (roermund1999molecularcharacterizationof pages 1-2, swiegers2001carnitine‐dependentmetabolicactivities pages 1-2)

Functionally, Cat2p is the principal enzymatic component of the yeast **carnitine shuttle** for acetyl-unit transfer between organelles, operating in parallel with a glyoxylate-cycle-mediated route (CIT2-dependent); loss of both systems (e.g., **Δcit2 Δcat2**) abolishes growth on fatty acids such as oleate. (roermund1999molecularcharacterizationof pages 1-2, swiegers2001carnitine‐dependentmetabolicactivities pages 1-2)

Recent work (2023–2024) continues to use Cat2 as a mechanistic handle for inter-organelle metabolism and for **real-world metabolic engineering**, including peroxisomal surface display of Cat2 to increase cytosolic acetyl-CoA supply and achieve **gram-per-liter** terpene titers in engineered yeast. (zhang2024denovoproduction pages 8-10)

## 1. Target identity verification and disambiguation
### 1.1 Verified gene/protein identity
Primary yeast studies identify **CAT2** as encoding a single gene product that yields both **peroxisomal and mitochondrial carnitine acetyltransferase activities** (Cat2p) in oleate-grown cells. (roermund1999molecularcharacterizationof pages 5-8, roermund1999molecularcharacterizationof pages 1-2)

A 2024 review of dual targeting also lists **CAT2 (YML042W)** as “carnitine acetyl-CoA transferase” among proteins that occur in both mitochondria and peroxisomes, consistent with UniProt P32796’s description of a mitochondrial precursor enzyme. (freitag2024mitochondriaperoxisomesand pages 1-3)

### 1.2 Distinguishing CAT2 from related carnitine-shuttle components
A frequent source of confusion is the distinction between:
- **CAT2 (YML042W)**: the **enzyme** catalyzing acetyl transfer to/from carnitine (Cat2p). (roermund1999molecularcharacterizationof pages 1-2, swiegers2001carnitine‐dependentmetabolicactivities pages 1-2)
- **YOR100C / CAC / CRC1**: the **mitochondrial carrier/translocase** involved in acetylcarnitine transport across the inner mitochondrial membrane, identified separately in genetic screens for carnitine-dependent acetyl-unit transport. (roermund1999molecularcharacterizationof pages 1-2, swiegers2001carnitine‐dependentmetabolicactivities pages 2-4)

This report is restricted to the *S. cerevisiae* CAT2 enzyme as specified.

## 2. Key concepts and definitions (current understanding)
### 2.1 Carnitine acetyltransferase / carnitine O-acetyltransferase
Carnitine acetyltransferases (CATs) catalyze a **reversible acyl-transfer** between CoA thioesters and carnitine. In yeast CAT biology, the central reaction is:

**acetyl-CoA + L-carnitine ⇄ CoA + acetyl-L-carnitine**

This reversibility is explicitly described in yeast: peroxisomal CAT forms acetylcarnitine from acetyl-CoA for transport, and mitochondrial CAT catalyzes the reverse reaction to regenerate acetyl-CoA for the TCA cycle. (swiegers2001carnitine‐dependentmetabolicactivities pages 2-4, swiegers2001carnitine‐dependentmetabolicactivities pages 1-2)

### 2.2 The carnitine shuttle in yeast
Because **acetyl-CoA cannot cross organellar membranes directly**, yeast uses a **carnitine-dependent shuttle** to move acetyl units between compartments. In the canonical peroxisome→mitochondrion direction during fatty-acid growth, intraperoxisomal acetyl-CoA is converted to acetylcarnitine by Cat2p and then transported to mitochondria, where acetyl-CoA is regenerated. (roermund1999molecularcharacterizationof pages 1-2, swiegers2001carnitine‐dependentmetabolicactivities pages 2-4)

Yeast also has a parallel acetyl-unit utilization/transport route via glyoxylate-cycle intermediates (CIT2 pathway), explaining genetic redundancy. (roermund1999molecularcharacterizationof pages 1-2)

## 3. Molecular function: reaction catalyzed and substrate specificity
### 3.1 Primary biochemical role
Cat2p catalyzes the **intraperoxisomal conversion of acetyl-CoA into acetylcarnitine** (acetyl transfer to carnitine), enabling acetyl-unit transfer out of peroxisomes. (roermund1999molecularcharacterizationof pages 1-2)

Swiegers et al. (2001) further describe the two-direction model: peroxisomal CAT transfers acetyl groups from acetyl-CoA to carnitine, while mitochondrial CAT catalyzes the reverse reaction to generate acetyl-CoA for the TCA cycle. (swiegers2001carnitine‐dependentmetabolicactivities pages 2-4)

### 3.2 Substrate specificity: acetyl versus long-chain acyl groups
In the evidence retrieved here, yeast Cat2 is consistently discussed as **acetyltransferase** acting on acetyl-CoA/acetylcarnitine (not long-chain acylcarnitines). Additionally, a yeast-focused review/thesis source notes that in *S. cerevisiae* “only carnitine acetyl-transferase activity has been described,” and that yeast lacks long-chain carnitine acyltransferase activity. (franken2009carnitinemetabolismand pages 32-36)

## 4. Subcellular localization and targeting
### 4.1 Dual peroxisome + mitochondrion localization
Multiple sources describe Cat2p as present in **both peroxisomes and mitochondria**. (roermund1999molecularcharacterizationof pages 1-2, swiegers2001carnitine‐dependentmetabolicactivities pages 1-2)

A yeast review/thesis summary explains dual targeting as mediated by alternative translation initiation/dual targeting signals: **two ATG codons** can produce isoforms, one containing an N-terminal mitochondrial targeting signal, while a **C-terminal PTS1 (AKL)** provides peroxisomal targeting potential. (franken2009carnitinemetabolismand pages 32-36)

### 4.2 2024 experimental update: tag position affects observed localization
A 2024 integrative omics study reports that Cat2 localization is sensitive to tagging: **N-terminal fluorescent tags** yielded a punctate/peroxisomal pattern, whereas **C-terminal tags** abolished puncta—consistent with disruption of a C-terminal peroxisomal targeting signal—leading to predominant mitochondrial localization. (kosir2024integrativeomicsreveals pages 4-8)

### 4.3 Expert interpretation (2024): tethering can influence routing of dually targeted proteins
A 2024 review on dual targeting and organelle tethering proposes that efficient tethering can counteract removal from mitochondria and subsequent peroxisomal targeting for presequence-pathway proteins, affecting Cat2 “to some extent.” (freitag2024mitochondriaperoxisomesand pages 3-4)

## 5. Biological processes and pathway context
### 5.1 Role in fatty-acid utilization: peroxisome-to-mitochondrion acetyl transfer
During growth on fatty acids (e.g., oleate), β-oxidation in yeast occurs in peroxisomes, creating acetyl-CoA that must be handled/transported. Cat2p functions in the **carnitine-dependent pathway** for transport of acetyl units to mitochondria. (roermund1999molecularcharacterizationof pages 1-2)

### 5.2 Parallel pathway redundancy with CIT2 (glyoxylate cycle)
Genetic evidence shows redundancy between the carnitine shuttle and glyoxylate-cycle route:
- **cat2Δ alone** may not impair growth on oleate in some backgrounds/conditions.
- **Δcit2 Δcat2** double mutants fail to grow on oleate, consistent with loss of both acetyl-unit transfer/utilization routes. (roermund1999molecularcharacterizationof pages 1-2, swiegers2001carnitine‐dependentmetabolicactivities pages 1-2)

Swiegers et al. also report that although single deletions can be tolerated, in a **cit2-disrupted** background, L-carnitine and carnitine acetyltransferases become essential for growth on non-fermentable carbon sources. (swiegers2001carnitine‐dependentmetabolicactivities pages 1-2)

### 5.3 Relationship to other yeast carnitine acetyltransferases (YAT1, YAT2)
Yeast contains at least three carnitine acetyltransferases involved in the shuttle system:
- **CAT2**: peroxisomal and mitochondrial (major activity).
- **YAT1**: described as associated with the **outer mitochondrial membrane**.
- **YAT2 (YER024w)**: described as **cytosolic** in review/thesis summaries and contributes substantially under ethanol growth. (franken2009carnitinemetabolismand pages 32-36, swiegers2001carnitine‐dependentmetabolicactivities pages 1-2)

In ethanol-grown cells, YAT2 was reported to account for ~**50%** of total CAT activity in the conditions tested, indicating condition-dependent sharing of measured CAT activity among family members. (swiegers2001carnitine‐dependentmetabolicactivities pages 7-9, swiegers2001carnitine‐dependentmetabolicactivities pages 2-4)

## 6. Quantitative evidence and statistics
### 6.1 Contribution to total cellular CAT activity
Cat2p is consistently reported as the **dominant** CAT activity in yeast:
- ~**95%** of total carnitine acetyltransferase activity in **oleate-grown** cells. (roermund1999molecularcharacterizationof pages 1-2)
- **>99%** of total CAT activity in **galactose-grown** cells (per Swiegers et al.). (swiegers2001carnitine‐dependentmetabolicactivities pages 1-2)

### 6.2 Organelle fraction activity values (secondary excerpt)
A literature excerpt reports enzyme activity in density-gradient peak fractions for *S. cerevisiae* grown on oleate: **82.2 nmol/min/mg** (peroxisomal peak) and **122.6 nmol/min/mg** (mitochondrial peak). (strijbisUnknownyeartheroleof pages 56-58, strijbisUnknownyeartheroleofa pages 56-58)

Note: the same excerpt contains an internal inconsistency (“five times more” in mitochondria) not supported by the provided numeric values; therefore, the numeric values are reported directly and should be interpreted cautiously without the original figure. (strijbisUnknownyeartheroleof pages 56-58)

## 7. Recent developments (prioritizing 2023–2024)
### 7.1 Organelle biology: dual targeting and tethering perspectives (2024)
A 2024 review positions Cat2 among dually targeted proteins whose steady-state distribution can be influenced by organelle tethering/contact-site mechanisms, providing an updated conceptual framework for how a protein like Cat2 can populate both mitochondria and peroxisomes. (freitag2024mitochondriaperoxisomesand pages 3-4)

### 7.2 Systems/omics: peroxisome-deficient yeast and Cat2 localization constraints (2024)
Kosir et al. (bioRxiv, March 2024) provide a modern, high-throughput context (matched proteomics + transcriptomics) and an experimental caution: Cat2’s observed peroxisomal localization can be lost with C-terminal tags (consistent with PTS1 disruption), which is directly relevant to functional annotation pipelines that use tagged libraries. (kosir2024integrativeomicsreveals pages 4-8)

### 7.3 Synthetic biology/metabolic engineering: peroxisomal surface display of Cat2 (2024)
Zhang et al. (Microbial Cell Factories, May 2024) explicitly leverage Cat2 enzymology and bidirectionality: they anchor Cat2 to the **peroxisome surface** (via a Pex15 C-terminal anchor) to facilitate **direct cytosolic conversion of acetylcarnitine into acetyl-CoA**, improving precursor supply for sesterterpenoid biosynthesis. (zhang2024denovoproduction pages 8-10)

Quantitative engineering outcomes reported include intermediate and final production metrics (see Applications). (zhang2024denovoproduction pages 8-10)

## 8. Current applications and real-world implementations
### 8.1 Improving cytosolic acetyl-CoA supply for high-value biosynthesis (2024 case study)
**Use case:** High-titer production of sesterterpenoid ophiobolins requires large acetyl-CoA supply.

**Implementation:** Zhang et al. (2024) describe that Cat2 transfers acetyl groups to carnitine forming acetylcarnitine, which can be shuttled across membranes; by exploiting bidirectionality, they position Cat2 on the peroxisome surface to convert acetylcarnitine into **cytosolic acetyl-CoA** (Fig. 2E in their paper). (zhang2024denovoproduction pages 8-10)

**Reported titers/statistics:**
- **178 mg/L** ophiobolin F (OphF) on oleic acid substrate in one condition.
- **649.6 mg/L** OphF with tPOS5 overexpression.
- **742.3 mg/L** OphF in strain Yoph19 (reported as a 14% increase vs comparator).
- **5.1 g/L** OphF after 72 h in fed-batch whole-cell transformation with intermittent addition of **75 g/L ethanol** and **20 g/L oleic acid**, in the Cat2 peroxisomal-surface strain (Yoph20). (zhang2024denovoproduction pages 8-10)

This is an example of Cat2 being used as an engineered metabolic “valve” connecting peroxisomal β-oxidation-derived acetyl units to cytosolic acetyl-CoA-demanding biosynthetic pathways. (zhang2024denovoproduction pages 8-10)

## 9. Expert synthesis and interpretation
1. **CAT2 is best annotated as an inter-organelle acetyl-unit transfer enzyme**, not merely a “mitochondrial enzyme,” because its physiological role depends on dual localization and the directionality of acetylcarnitine movement between compartments. (roermund1999molecularcharacterizationof pages 1-2, swiegers2001carnitine‐dependentmetabolicactivities pages 1-2)
2. **Redundancy with CIT2** indicates Cat2’s pathway is conditionally essential—particularly during fatty-acid growth or when the glyoxylate route is compromised—so phenotype interpretation requires carbon-source and background awareness. (roermund1999molecularcharacterizationof pages 1-2, swiegers2001carnitine‐dependentmetabolicactivities pages 1-2)
3. Modern studies emphasize that **localization is experimentally fragile** (e.g., C-terminal tagging can disrupt PTS1-mediated import), which can mislead high-throughput annotation unless tag design is considered. (kosir2024integrativeomicsreveals pages 4-8)
4. The 2024 synthetic biology example illustrates that Cat2’s **reversibility** is practically exploitable: placing Cat2 at new subcellular locales can rewire acetyl-CoA availability and substantially change production outcomes. (zhang2024denovoproduction pages 8-10)

## 10. Evidence map (table)
The following table summarizes the main supported claims, quantitative values, and metadata.

| Category | Specific finding | Key quantitative data (if any) | Source (first author year) | Publication date (month/year if known) | URL/DOI |
|---|---|---|---|---|---|
| Identity | **CAT2 (YML042W)** in *S. cerevisiae* encodes **Cat2p**, the major carnitine acetyltransferase/carnitine O-acetyltransferase in yeast; literature distinguishes it from the mitochondrial carnitine carrier gene (**YOR100C/CAC/CRC1**). (roermund1999molecularcharacterizationof pages 1-2, roermund1999molecularcharacterizationof pages 5-8, freitag2024mitochondriaperoxisomesand pages 1-3) | Major CAT enzyme in yeast | van Roermund 1999; Freitag 2024 | Nov 1999; Jan 2024 | https://doi.org/10.1093/emboj/18.21.5843 ; https://doi.org/10.1177/25152564241264254 |
| Reaction | Cat2p catalyzes **reversible transfer of acetyl groups between acetyl-CoA and L-carnitine**, i.e. acetyl-CoA + carnitine ⇄ CoA + acetylcarnitine; in the peroxisome it forms acetylcarnitine, and in mitochondria the reverse reaction regenerates acetyl-CoA for the TCA cycle. (swiegers2001carnitine‐dependentmetabolicactivities pages 1-2, roermund1999molecularcharacterizationof pages 1-2, swiegers2001carnitine‐dependentmetabolicactivities pages 2-4) | Reversible acetyl transfer; no kinetic constants retrieved in context | Swiegers 2001; van Roermund 1999 | May 2001; Nov 1999 | https://doi.org/10.1002/yea.712 ; https://doi.org/10.1093/emboj/18.21.5843 |
| Localization | Cat2p is **dually localized to peroxisomes and mitochondria**; review and thesis evidence describe dual targeting mediated by N-terminal mitochondrial targeting information plus a C-terminal peroxisomal targeting signal, with two ATG codons contributing to alternative targeting. (franken2009carnitinemetabolismand pages 32-36, roermund1999molecularcharacterizationof pages 1-2, freitag2024mitochondriaperoxisomesand pages 1-3) | Dual organellar localization | van Roermund 1999; Franken 2009; Freitag 2024 | Nov 1999; 2009; Jan 2024 | https://doi.org/10.1093/emboj/18.21.5843 ; https://doi.org/10.1177/25152564241264254 |
| Pathway role | Cat2p is central to the **carnitine shuttle** that moves acetyl units from peroxisomes to mitochondria when acetyl-CoA itself cannot cross membranes; this pathway complements the glyoxylate-cycle route for acetyl-unit utilization. (roermund1999molecularcharacterizationof pages 1-2, swiegers2001carnitine‐dependentmetabolicactivities pages 1-2) | Functions in one of two parallel acetyl-unit transport routes | van Roermund 1999; Swiegers 2001 | Nov 1999; May 2001 | https://doi.org/10.1093/emboj/18.21.5843 ; https://doi.org/10.1002/yea.712 |
| Genetics & phenotypes | **cat2Δ single mutants** can grow similarly to wild type on tested carbon sources, but **Δcit2 Δcat2** double mutants fail on oleate/non-fermentable carbon sources, showing redundancy between Cat2-mediated shuttle and the glyoxylate-cycle pathway. (swiegers2001carnitine‐dependentmetabolicactivities pages 7-9, swiegers2001carnitine‐dependentmetabolicactivities pages 5-7, roermund1999molecularcharacterizationof pages 1-2) | Double-mutant synthetic growth defect/loss on oleate and related conditions | van Roermund 1999; Swiegers 2001 | Nov 1999; May 2001 | https://doi.org/10.1093/emboj/18.21.5843 ; https://doi.org/10.1002/yea.712 |
| Genetics & phenotypes | All three yeast carnitine acetyltransferases—**CAT2, YAT1, YAT2**—are required for a fully functional carnitine shuttle in a **cit2-disrupted** background, and they do **not cross-complement**, implying distinct subcellular roles. (franken2009carnitinemetabolismand pages 32-36, swiegers2001carnitine‐dependentmetabolicactivities pages 2-4) | YAT2 contributes ~50% of total CAT activity on ethanol; no cross-complementation | Swiegers 2001; Franken 2009 | May 2001; 2009 | https://doi.org/10.1002/yea.712 |
| Quantitative activity | Cat2p provides the **majority of total carnitine acetyltransferase activity** in yeast. Reported contributions vary with growth condition: **~95% in oleate-grown cells**, **>99% in galactose-grown cells**, and **~95% overall dominance** in review/thesis summaries. (swiegers2001carnitine‐dependentmetabolicactivities pages 1-2, roermund1999molecularcharacterizationof pages 1-2) | ~95% (oleate); >99% (galactose) | van Roermund 1999; Swiegers 2001 | Nov 1999; May 2001 | https://doi.org/10.1093/emboj/18.21.5843 ; https://doi.org/10.1002/yea.712 |
| Quantitative activity | Fractionation/enzyme-assay excerpts report bimodal Cat activity in *S. cerevisiae* organelle fractions, with **82.2 nmol/min/mg** in the peroxisomal peak and **122.6 nmol/min/mg** in the mitochondrial peak; the same source states CAT2 contributes about **95%** of total activity in oleate-grown cells. (strijbisUnknownyeartheroleof pages 56-58, strijbisUnknownyeartheroleofa pages 56-58) | 82.2 vs 122.6 nmol/min/mg; ~95% of total activity | Strijbis et al. unknown year excerpt | Unknown | URL not available in gathered context |
| Recent 2023-2024 developments | A 2024 review places Cat2 among **dually targeted mitochondria/peroxisome proteins** and notes that organelle tethering can influence whether such proteins remain mitochondrial or proceed to peroxisomes, affecting Cat2 “to some extent.” (freitag2024mitochondriaperoxisomesand pages 3-4) | No Cat2-specific numeric values reported | Freitag 2024 | Jan 2024 | https://doi.org/10.1177/25152564241264254 |
| Recent 2023-2024 developments | In acetate-grown cells, **Cat2 with an N-terminal fluorescent tag showed punctate/peroxisomal localization**, whereas **C-terminal tagging disrupted the PTS1-dependent punctate pattern**, yielding predominant mitochondrial localization; this supports dual targeting and sensitivity of Cat2 localization to tag placement. (kosir2024integrativeomicsreveals pages 4-8) | Proteomics/transcriptomics used 3 biological replicates; analysis thresholds ≥1.5 or ≤0.66 fold, p=0.05, but no Cat2-specific fold-change given | Kosir 2024 | Mar 2024 | https://doi.org/10.1101/2024.03.20.585854 |
| Applications & engineering | Cat2 has been repurposed in **metabolic engineering**: anchoring **Cat2 to the peroxisome surface** was used to channel acetyl units from peroxisomal β-oxidation toward the cytosolic acetyl-CoA pool for ophiobolin biosynthesis; authors explicitly exploit the **bidirectionality** of Cat2 catalysis. (zhang2024denovoproduction pages 8-10) | Surface-localized Cat2 strain (**Yoph20**) reached **5.1 g/L** ophiobolin F after 72 h fed-batch whole-cell transformation; other reported titers include **178 mg/L**, **649.6 mg/L**, and **742.3 mg/L** OphF in intermediate strains/conditions | Zhang 2024 | May 2024 | https://doi.org/10.1186/s12934-024-02406-0 |


*Table: This table summarizes verified findings on *S. cerevisiae* CAT2/Cat2p, covering identity, biochemical function, localization, pathway context, genetics, quantitative activity, and recent 2023-2024 developments. It is useful as a compact evidence map linking classic yeast genetics with current organelle biology and metabolic engineering work.*

## 11. Key references (with URLs and dates where available)
- van Roermund et al. 1999. *The EMBO Journal* (Nov 1999). “Molecular characterization of carnitine-dependent transport of acetyl-CoA from peroxisomes to mitochondria…” https://doi.org/10.1093/emboj/18.21.5843 (roermund1999molecularcharacterizationof pages 1-2, roermund1999molecularcharacterizationof pages 5-8)
- Swiegers et al. 2001. *Yeast* (May 2001). “Carnitine-dependent metabolic activities in Saccharomyces cerevisiae…” https://doi.org/10.1002/yea.712 (swiegers2001carnitine‐dependentmetabolicactivities pages 1-2, swiegers2001carnitine‐dependentmetabolicactivities pages 2-4)
- Freitag et al. 2024. *Contact* (Jan 2024). “Mitochondria, Peroxisomes and Beyond—How Dual Targeting Regulates Organelle Tethering” https://doi.org/10.1177/25152564241264254 (freitag2024mitochondriaperoxisomesand pages 1-3, freitag2024mitochondriaperoxisomesand pages 3-4)
- Kosir et al. 2024. bioRxiv (Mar 2024). “Integrative Omics reveals changes in the cellular landscape of yeast without peroxisomes” https://doi.org/10.1101/2024.03.20.585854 (kosir2024integrativeomicsreveals pages 4-8)
- Zhang et al. 2024. *Microbial Cell Factories* (May 2024). “De novo production of bioactive sesterterpenoid ophiobolins in Saccharomyces cerevisiae cell factories” https://doi.org/10.1186/s12934-024-02406-0 (zhang2024denovoproduction pages 8-10)

## 12. Limitations of this evidence set
- Direct extraction of figure/table images from the Swiegers et al. (2001) PDF failed in the current runtime environment; all quantitative claims included above are therefore taken from text excerpts rather than figure crops.
- Some localization-mechanism details (e.g., specific dual-start codon mapping to isoforms) are drawn from a thesis/review-style source in the retrieved set rather than the original 1995 primary study mentioned therein. (franken2009carnitinemetabolismand pages 32-36)


References

1. (roermund1999molecularcharacterizationof pages 1-2): C. V. van Roermund, E. Hettema, M. van den Berg, H. Tabak, and R. Wanders. Molecular characterization of carnitine‐dependent transport of acetyl‐coa from peroxisomes to mitochondria in saccharomyces cerevisiae and identification of a plasma membrane carnitine transporter, agp2p. The EMBO Journal, 18:5843-5852, Nov 1999. URL: https://doi.org/10.1093/emboj/18.21.5843, doi:10.1093/emboj/18.21.5843. This article has 249 citations.

2. (swiegers2001carnitine‐dependentmetabolicactivities pages 1-2): Jan H. Swiegers, Nola Dippenaar, Isak S. Pretorius, and Florian F. Bauer. Carnitine‐dependent metabolic activities in saccharomyces cerevisiae: three carnitine acetyltransferases are essential in a carnitine‐dependent strain. Yeast, 18:585-595, May 2001. URL: https://doi.org/10.1002/yea.712, doi:10.1002/yea.712. This article has 130 citations and is from a peer-reviewed journal.

3. (zhang2024denovoproduction pages 8-10): Caizhe Zhang, Jun Wu, Qing Sun, Shuaishuai Ding, Hua Tao, Yuhua He, Hui Qiu, Bei Shu, Dongqing Zhu, Hengcheng Zhu, and Kui Hong. De novo production of bioactive sesterterpenoid ophiobolins in saccharomyces cerevisiae cell factories. Microbial Cell Factories, May 2024. URL: https://doi.org/10.1186/s12934-024-02406-0, doi:10.1186/s12934-024-02406-0. This article has 11 citations and is from a peer-reviewed journal.

4. (roermund1999molecularcharacterizationof pages 5-8): C. V. van Roermund, E. Hettema, M. van den Berg, H. Tabak, and R. Wanders. Molecular characterization of carnitine‐dependent transport of acetyl‐coa from peroxisomes to mitochondria in saccharomyces cerevisiae and identification of a plasma membrane carnitine transporter, agp2p. The EMBO Journal, 18:5843-5852, Nov 1999. URL: https://doi.org/10.1093/emboj/18.21.5843, doi:10.1093/emboj/18.21.5843. This article has 249 citations.

5. (freitag2024mitochondriaperoxisomesand pages 1-3): Johannes Freitag, Thorsten Stehlik, and Gert Bange. Mitochondria, peroxisomes and beyond—how dual targeting regulates organelle tethering. Contact, Jan 2024. URL: https://doi.org/10.1177/25152564241264254, doi:10.1177/25152564241264254. This article has 1 citations.

6. (swiegers2001carnitine‐dependentmetabolicactivities pages 2-4): Jan H. Swiegers, Nola Dippenaar, Isak S. Pretorius, and Florian F. Bauer. Carnitine‐dependent metabolic activities in saccharomyces cerevisiae: three carnitine acetyltransferases are essential in a carnitine‐dependent strain. Yeast, 18:585-595, May 2001. URL: https://doi.org/10.1002/yea.712, doi:10.1002/yea.712. This article has 130 citations and is from a peer-reviewed journal.

7. (franken2009carnitinemetabolismand pages 32-36): J Franken. Carnitine metabolism and biosynthesis in the yeast saccharomyces cerevisiae. Unknown journal, 2009.

8. (kosir2024integrativeomicsreveals pages 4-8): Tjasa Kosir, Hirak Das, Marc Pilegaard Pedersen, Marco Anteghini, Silke Oeljeklaus, Vitor Martins dos Santos, Ida J. van der Klei, and Bettina Warscheid. Integrative omics reveals changes in the cellular landscape of yeast without peroxisomes. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.20.585854, doi:10.1101/2024.03.20.585854. This article has 3 citations.

9. (freitag2024mitochondriaperoxisomesand pages 3-4): Johannes Freitag, Thorsten Stehlik, and Gert Bange. Mitochondria, peroxisomes and beyond—how dual targeting regulates organelle tethering. Contact, Jan 2024. URL: https://doi.org/10.1177/25152564241264254, doi:10.1177/25152564241264254. This article has 1 citations.

10. (swiegers2001carnitine‐dependentmetabolicactivities pages 7-9): Jan H. Swiegers, Nola Dippenaar, Isak S. Pretorius, and Florian F. Bauer. Carnitine‐dependent metabolic activities in saccharomyces cerevisiae: three carnitine acetyltransferases are essential in a carnitine‐dependent strain. Yeast, 18:585-595, May 2001. URL: https://doi.org/10.1002/yea.712, doi:10.1002/yea.712. This article has 130 citations and is from a peer-reviewed journal.

11. (strijbisUnknownyeartheroleof pages 56-58): K Strijbis, C van Roermund, and M van de Berg. The role of candida albicans peroxisomal and mitochondrial carnitine acetyl-tranferases in intracellular acetyl unit transport. Unknown journal, Unknown year.

12. (strijbisUnknownyeartheroleofa pages 56-58): K Strijbis, C van Roermund, and M van de Berg. The role of candida albicans peroxisomal and mitochondrial carnitine acetyl-tranferases in intracellular acetyl unit transport. Unknown journal, Unknown year.

13. (swiegers2001carnitine‐dependentmetabolicactivities pages 5-7): Jan H. Swiegers, Nola Dippenaar, Isak S. Pretorius, and Florian F. Bauer. Carnitine‐dependent metabolic activities in saccharomyces cerevisiae: three carnitine acetyltransferases are essential in a carnitine‐dependent strain. Yeast, 18:585-595, May 2001. URL: https://doi.org/10.1002/yea.712, doi:10.1002/yea.712. This article has 130 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](CAT2-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. zhang2024denovoproduction pages 8-10
2. freitag2024mitochondriaperoxisomesand pages 1-3
3. roermund1999molecularcharacterizationof pages 1-2
4. franken2009carnitinemetabolismand pages 32-36
5. kosir2024integrativeomicsreveals pages 4-8
6. freitag2024mitochondriaperoxisomesand pages 3-4
7. roermund1999molecularcharacterizationof pages 5-8
8. https://doi.org/10.1093/emboj/18.21.5843
9. https://doi.org/10.1177/25152564241264254
10. https://doi.org/10.1002/yea.712
11. https://doi.org/10.1101/2024.03.20.585854
12. https://doi.org/10.1186/s12934-024-02406-0
13. https://doi.org/10.1093/emboj/18.21.5843,
14. https://doi.org/10.1002/yea.712,
15. https://doi.org/10.1186/s12934-024-02406-0,
16. https://doi.org/10.1177/25152564241264254,
17. https://doi.org/10.1101/2024.03.20.585854,