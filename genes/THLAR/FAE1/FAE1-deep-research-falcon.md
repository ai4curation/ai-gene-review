---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-30T05:11:45.473746'
end_time: '2026-09-30T05:23:57.041961'
duration_seconds: 731.57
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: THLAR
  gene_id: FAE1
  gene_symbol: Fae1
  uniprot_accession: V9XY07
  protein_description: 'RecName: Full=3-ketoacyl-CoA synthase {ECO:0000256|PIRNR:PIRNR036417};
    EC=2.3.1.- {ECO:0000256|PIRNR:PIRNR036417};'
  gene_info: Name=Fae1 {ECO:0000313|EMBL:AHE13915.1}; Synonyms=FAE1 {ECO:0000313|EMBL:AGR03732.1};
  organism_full: Thlaspi arvense (Field penny-cress).
  protein_family: Belongs to the thiolase-like superfamily. Chalcone/stilbene
  protein_domains: 3-ktacl-CoA_syn. (IPR012392); ACP_syn_III_C. (IPR013747); FAE1_typ3_polyketide_synth.
    (IPR013601); Thiolase-like. (IPR016039); ACP_syn_III_C (PF08541)
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
  path: FAE1-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** V9XY07
- **Protein Description:** RecName: Full=3-ketoacyl-CoA synthase {ECO:0000256|PIRNR:PIRNR036417}; EC=2.3.1.- {ECO:0000256|PIRNR:PIRNR036417};
- **Gene Information:** Name=Fae1 {ECO:0000313|EMBL:AHE13915.1}; Synonyms=FAE1 {ECO:0000313|EMBL:AGR03732.1};
- **Organism (full):** Thlaspi arvense (Field penny-cress).
- **Protein Family:** Belongs to the thiolase-like superfamily. Chalcone/stilbene
- **Key Domains:** 3-ktacl-CoA_syn. (IPR012392); ACP_syn_III_C. (IPR013747); FAE1_typ3_polyketide_synth. (IPR013601); Thiolase-like. (IPR016039); ACP_syn_III_C (PF08541)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Fae1" matches the protein description above**
2. **Verify the organism is correct:** Thlaspi arvense (Field penny-cress).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Fae1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Fae1** (gene ID: FAE1, UniProt: V9XY07) in THLAR.

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
- **UniProt Accession:** V9XY07
- **Protein Description:** RecName: Full=3-ketoacyl-CoA synthase {ECO:0000256|PIRNR:PIRNR036417}; EC=2.3.1.- {ECO:0000256|PIRNR:PIRNR036417};
- **Gene Information:** Name=Fae1 {ECO:0000313|EMBL:AHE13915.1}; Synonyms=FAE1 {ECO:0000313|EMBL:AGR03732.1};
- **Organism (full):** Thlaspi arvense (Field penny-cress).
- **Protein Family:** Belongs to the thiolase-like superfamily. Chalcone/stilbene
- **Key Domains:** 3-ktacl-CoA_syn. (IPR012392); ACP_syn_III_C. (IPR013747); FAE1_typ3_polyketide_synth. (IPR013601); Thiolase-like. (IPR016039); ACP_syn_III_C (PF08541)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Fae1" matches the protein description above**
2. **Verify the organism is correct:** Thlaspi arvense (Field penny-cress).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Fae1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Fae1** (gene ID: FAE1, UniProt: V9XY07) in THLAR.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: FAE1 Gene in *Thlaspi arvense* (Field Pennycress)

## Gene Identity Verification

The gene Fae1 (FAE1, FATTY ACID ELONGATION1) in *Thlaspi arvense* (field pennycress) encodes a β-ketoacyl-CoA synthase (EC 2.3.1.-) that functions as the condensing enzyme in the fatty acid elongation complex (mcginn2019moleculartoolsenabling pages 9-11). This identification is consistent with the UniProt entry V9XY07 describing the protein as a 3-ketoacyl-CoA synthase. The pennycress FAE1 gene (TaFAE1) is a single-copy, intronless gene of 1,521 nucleotides sharing 87.8% nucleotide sequence identity with *Arabidopsis thaliana* FAE1 (AT4G34520) (mcginn2019moleculartoolsenabling pages 9-11). The gene symbol is unambiguous in the literature, with extensive specific research on this gene in pennycress domestication and oil quality improvement.

## Primary Enzymatic Function and Substrate Specificity

### Catalytic Mechanism

FAE1 encodes β-ketoacyl-CoA synthase (KCS), the rate-limiting condensing enzyme of the endoplasmic reticulum (ER) fatty acid elongation complex (mcginn2019moleculartoolsenabling pages 9-11, bashiri2024engineeringerucicacid pages 1-2). The enzyme catalyzes the first step of each two-carbon elongation cycle: the decarboxylative condensation of a long-chain acyl-CoA substrate with malonyl-CoA to produce a β-ketoacyl-CoA intermediate that is two carbons longer, releasing CoA and CO₂ (khan2023comparativephylogenomicinsights pages 1-2, zhukov2022synthesisofc20–38 pages 6-7, zhukov2022synthesisofc20–38 pages 12-14). This condensation reaction is the key substrate-specificity-determining step of the elongation pathway.

### Substrate Specificity

In pennycress seed metabolism, FAE1 acts primarily on oleoyl-CoA (C18:1-CoA) as its initial substrate, converting it through successive elongation cycles first to eicosenoyl-CoA (20:1-CoA) and then to erucoyl-CoA (22:1-CoA) (mcginn2019moleculartoolsenabling pages 9-11, jarvis2021crisprcas9inducedfad2and pages 2-3). Notably, functional characterization has revealed that pennycress FAE1 exhibits higher affinity for 20:1-CoA compared to the *Arabidopsis* ortholog, which helps explain the characteristically high erucic acid content (30-35% of total fatty acids) in pennycress seed oil (claver2024transcriptomicandlipidomic pages 2-3, claver2024transcriptomicandlipidomic pages 1-2).

### Reaction Products

The sequential action of FAE1-containing elongase complexes produces two main very-long-chain fatty acids (VLCFAs):

1. **Eicosenoic acid (20:1, cis-11-eicosenoic acid)** - the intermediate product
2. **Erucic acid (22:1, cis-13-docosenoic acid)** - the final major product

Genetic evidence strongly supports FAE1's essential role: CRISPR/Cas9-induced loss-of-function mutations in TaFAE1 reduce seed oil erucic acid and eicosenoic acid to negligible levels (<1%), while increasing oleic acid (18:1), linoleic acid (18:2), and linolenic acid (18:3) (mcginn2019moleculartoolsenabling pages 9-11).

## Subcellular Localization

FAE1 functions as part of an **endoplasmic reticulum (ER) membrane-bound fatty acid elongation complex** (patra2025heterologousexpressionin pages 6-9, patra2025heterologousexpressionin pages 1-4, claver2024transcriptomicandlipidomic pages 1-2). While fatty acids are initially synthesized de novo in plastids, elongation of C18 fatty acids to VLCFAs (C20-C22) occurs at the ER membrane (zhukov2022synthesisofc20–38 pages 4-6, zhukov2022synthesisofc20–38 pages 6-7). The pennycress-specific literature explicitly confirms that TaFAE1-mediated erucic acid biosynthesis takes place in the endoplasmic reticulum through sequential elongation of C18 acyl-CoA substrates (claver2024transcriptomicandlipidomic pages 1-2).

## Biochemical Pathway and Complex Components

### The Fatty Acid Elongation Complex

FAE1 operates as one component of a multi-enzyme complex that catalyzes a repeating four-step elongation cycle. The complete complex contains four distinct enzymatic activities (khan2023comparativephylogenomicinsights pages 1-2, zhukov2022synthesisofc20–38 pages 8-10, zhukov2022synthesisofc20–38 pages 7-8):

1. **β-ketoacyl-CoA synthase (KCS/FAE1)** - catalyzes condensation of acyl-CoA with malonyl-CoA
2. **β-ketoacyl-CoA reductase (KCR)** - reduces the β-keto group using NADPH
3. **β-hydroxyacyl-CoA dehydratase (HCD)** - removes water to form trans-2,3-enoyl-CoA
4. **trans-2,3-enoyl-CoA reductase (ECR)** - reduces the double bond using NADPH to yield elongated acyl-CoA

Each complete cycle extends the acyl-CoA chain by two carbon atoms (fatima2026fae1andfad2 pages 2-4, zhukov2022synthesisofc20–38 pages 6-7, zhukov2022synthesisofc20–38 pages 12-14). FAE1, as the KCS component, is responsible for substrate specificity and serves as the principal determinant of which chain lengths are produced by the elongation system.

### Integration with Triacylglycerol Biosynthesis

The erucic acid produced by FAE1 is incorporated into seed storage triacylglycerols (TAGs) through multiple pathways (jarvis2021crisprcas9inducedfad2and pages 2-3, claver2024transcriptomicandlipidomic pages 1-2). Recent transcriptomic and lipidomic studies from 2024 have revealed strong temporal coordination between the elongation pathway and TAG assembly routes during seed maturation (claver2024transcriptomicandlipidomic pages 1-2). The Kennedy pathway enzymes (GPAT, LPAT, DGAT1) show increasing expression during mid-to-late maturation stages, coinciding with accumulation of 22:1-containing TAG species. Additionally, acyl-editing pathways involving phosphatidylcholine (PC)-derived diacylglycerol and enzymes like DGAT2, PDAT1, and LPCAT contribute to erucic acid incorporation, with particularly high activity early in seed development (claver2024transcriptomicandlipidomic pages 3-5, jarvis2021crisprcas9inducedfad2and pages 2-3, claver2024transcriptomicandlipidomic pages 1-2).

## Tissue-Specific Expression and Developmental Regulation

FAE1 expression is predominantly associated with **developing seed embryos during oil accumulation** (park2022applicationsandprospects pages 4-5). Transcriptomic analysis across five pennycress seed maturation stages (from 12 to 45 days after flowering) has shown that fatty acid biosynthetic genes, including FAE1, are expressed early in seed development, with erucic acid being incorporated into TAG progressively throughout maturation (claver2024transcriptomicandlipidomic pages 3-5, jarvis2021crisprcas9inducedfad2and pages 2-3, claver2024transcriptomicandlipidomic pages 1-2). 

Spatial analysis using MALDI-MS imaging has revealed that erucic acid is highly enriched in the **cotyledons**, which serve as the primary storage organs in mature seeds (jarvis2021crisprcas9inducedfad2and pages 1-2). This distribution pattern suggests erucic acid's role as a dense energy reserve supporting seedling emergence and early growth. In contrast, polyunsaturated fatty acids are enriched in the embryonic axis, likely supporting membrane expansion during germination (jarvis2021crisprcas9inducedfad2and pages 1-2).

## Biological Role and Physiological Function

### Energy Storage Function

Erucic acid produced by FAE1 typically comprises 27-39% of pennycress seed oil fatty acids and is stored as a component of triacylglycerols (mcginn2019moleculartoolsenabling pages 9-11, esfahanian2021generatingpennycress(thlaspi pages 1-2, claver2024transcriptomicandlipidomic pages 2-3). TAGs constitute approximately 80-90% of total seed lipids and represent the major carbon and energy reserve that fuels seed germination and early seedling development (claver2024transcriptomicandlipidomic pages 2-3, claver2024transcriptomicandlipidomic pages 1-2). The high concentration of erucic acid in cotyledon TAGs specifically positions it as an energy source for the emerging seedling (jarvis2021crisprcas9inducedfad2and pages 1-2).

### Impact on Oil Properties

The presence of erucic acid confers several important properties to pennycress seed oil:

- **Industrial applications**: Erucic acid provides high lubricity and can be hydrocracked to produce dodecane and other compounds suitable for aviation fuel and biodiesel (jarvis2021crisprcas9inducedfad2and pages 1-2)
- **Biofuel characteristics**: The oil has a high cetane number, favorable low-temperature behavior, and relatively low oxidative susceptibility compared to polyunsaturated fatty acid-rich oils (claver2024transcriptomicandlipidomic pages 2-3)
- **Food limitations**: High erucic acid content (>5%) is undesirable for human consumption due to potential health concerns, making FAE1 knockout a priority for edible oil development (jarvis2021crisprcas9inducedfad2and pages 2-3)

## Recent Developments and Applications (2023-2024)

### Crop Improvement Through Gene Editing

CRISPR/Cas9-mediated knockout of TaFAE1 has emerged as a central strategy in pennycress domestication efforts (ma2023researchprogresson pages 1-2, mcginn2019moleculartoolsenabling pages 9-11). Multiple stable, heritable loss-of-function alleles have been generated, including a 4-bp deletion (fae1-3), single-nucleotide insertions (fae1-4, fae1-5), all of which produce seed oil with negligible erucic acid and elevated oleic acid content comparable to canola (mcginn2019moleculartoolsenabling pages 9-11). A 2023 review identified this FAE1 editing as a key domestication trait enabling pennycress development as an off-season oilseed cash cover crop with edible oil quality (ma2023researchprogresson pages 1-2).

### Pathway Coordination Studies (2024)

A comprehensive 2024 transcriptomic and lipidomic analysis revealed the temporal dynamics of erucic acid incorporation into TAG during pennycress seed maturation (claver2024transcriptomicandlipidomic pages 1-2). This study demonstrated strong coordination between FAE1-dependent elongation, multiple TAG biosynthetic pathways (Kennedy pathway, acyl-editing, PC-derived DAG routes), and different DGAT isoforms. The findings showed that DGAT2 is particularly important early in maturation for rapid 22:1 incorporation, while DGAT1 becomes more prominent later, suggesting differential roles for these acyltransferases in erucic acid-enriched TAG assembly (claver2024transcriptomicandlipidomic pages 1-2).

### Stress Tolerance Research (2026)

Recent forward-looking research published in 2026 has explored the pleiotropic effects of FAE1 mutations. Studies on fae1 mutants stacked with fad2 mutations revealed that altered fatty acid composition affects heat stress tolerance during flowering and seed development, with implications for adapting pennycress to warming climates (jarvis2021crisprcas9inducedfad2and pages 1-2). Additionally, research on FAE1 and FAD2 gene expression under salt stress in Brassica species has provided insights into lipid metabolism-mediated stress adaptation mechanisms relevant to oilseed production on marginal lands (fatima2026fae1andfad2 pages 1-2).

### Oil Body Dynamics (2025)

A 2025 proteomic study characterized oil body-associated proteins during pennycress seed maturation, providing context for understanding how FAE1-produced erucic acid is packaged into storage lipid droplets (claver2025transcriptomicandproteomic pages 1-2). This work identified differential expression patterns of oleosins, SEIPINs, and other structural proteins that stabilize TAG-containing oil bodies, complementing the biochemical understanding of erucic acid synthesis with insights into its physical storage.

## Summary Table

| Feature | Description |
|---|---|
| Gene name and synonyms | **Gene:** *Fae1* / *FAE1*; commonly expanded as **FATTY ACID ELONGATION1** and also described as **TaFAE1** in *Thlaspi arvense* (field pennycress). The target protein is UniProt **V9XY07**. The experimentally identified pennycress ortholog has an intronless 1,521-nt open reading frame with 87.8% nucleotide identity to *Arabidopsis thaliana FAE1/KCS18* (*AT4G34520*) (mcginn2019moleculartoolsenabling pages 9-11). |
| Protein function/enzyme activity | FAE1 is a **3-ketoacyl-CoA synthase**, also called **β-ketoacyl-CoA synthase (KCS)**. It is the condensing and principal substrate/chain-length–selecting component of the microsomal fatty-acid elongase system that generates seed very-long-chain fatty acids (VLCFAs) (mcginn2019moleculartoolsenabling pages 9-11, zhukov2022synthesisofc20–38 pages 6-7). |
| Enzymatic reaction catalyzed | FAE1 catalyzes the first, decarboxylative condensation in each elongation cycle: **acyl-CoA + malonyl-CoA → 3-ketoacyl-CoA elongated by two carbons + CoA + CO₂**. The complete elongase cycle subsequently consumes reducing power in two NADPH-dependent reductions, but those reductions are catalyzed by KCR and ECR rather than FAE1 itself (khan2023comparativephylogenomicinsights pages 1-2, zhukov2022synthesisofc20–38 pages 6-7, zhukov2022synthesisofc20–38 pages 12-14). |
| Substrate specificity | In pennycress seed lipid metabolism, the physiologically important starting substrate is **oleoyl-CoA (18:1-CoA)**. Sequential cycles use 18:1-CoA and then the resulting **20:1-CoA** to form longer monounsaturated acyl-CoAs. Functional comparisons indicate that pennycress FAE1 has greater affinity for 20:1-CoA than the *Arabidopsis* enzyme, helping explain pennycress’s high erucic-acid accumulation (claver2024transcriptomicandlipidomic pages 2-3, mcginn2019moleculartoolsenabling pages 9-11). |
| Products generated | One cycle converts the C18:1 substrate toward **eicosenoyl-CoA (20:1-CoA)**; a second cycle produces **erucoyl-CoA (22:1-CoA)**, whose fatty-acid moiety is erucic acid. CRISPR loss-of-function alleles reduce both eicosenoic and erucic acids to negligible levels, providing strong genetic evidence that TaFAE1 is required for these products (jarvis2021crisprcas9inducedfad2and pages 2-3, mcginn2019moleculartoolsenabling pages 9-11). |
| Subcellular localization | TaFAE1 activity is associated with an **endoplasmic-reticulum (ER) membrane-bound elongase complex**. C18 fatty acids originate through plastidial synthesis, but elongation of their CoA esters to C20–C22 products occurs at the ER; the pennycress-specific literature explicitly places erucic-acid synthesis by TaFAE1 in the ER (claver2024transcriptomicandlipidomic pages 1-2, zhukov2022synthesisofc20–38 pages 4-6). |
| Biochemical pathway | FAE1 functions in the **ER very-long-chain fatty-acid elongation pathway**, specifically the branch converting oleoyl-CoA into C20:1 and C22:1 acyl-CoAs. These products feed seed triacylglycerol (TAG) biosynthesis through Kennedy-pathway and acyl-editing/PC-derived routes; 2024 multi-omics data show temporal coordination among these routes during seed maturation (jarvis2021crisprcas9inducedfad2and pages 2-3, claver2024transcriptomicandlipidomic pages 1-2). |
| Complex components (other enzymes) | The four-step elongase cycle comprises: **KCS/FAE1**, condensation and specificity selection; **KCR**, 3-ketoacyl-CoA reduction; **HCD**, 3-hydroxyacyl-CoA dehydration; and **ECR**, trans-2,3-enoyl-CoA reduction. Each completed cycle adds two carbons to the acyl-CoA chain (zhukov2022synthesisofc20–38 pages 8-10, zhukov2022synthesisofc20–38 pages 7-8, zhukov2022synthesisofc20–38 pages 6-7). |
| Tissue/developmental expression | The best-supported physiological context is the **developing seed embryo during oil accumulation**. Erucic acid enters TAG early in maturation and progressively accumulates as seeds mature; recent transcriptomic/lipidomic work sampled five stages from 12 to 45 days after flowering and found early expression of fatty-acid-biosynthetic genes followed by increasing Kennedy-pathway activity and accumulation of 22:1-containing TAGs (claver2024transcriptomicandlipidomic pages 3-5, jarvis2021crisprcas9inducedfad2and pages 2-3, claver2024transcriptomicandlipidomic pages 1-2). |
| Biological role | FAE1 determines much of pennycress seed-oil chain-length composition by directing oleoyl-CoA into eicosenoic and erucic acids. Erucic acid commonly represents about **27–39%** of seed-TAG fatty acids and is enriched in cotyledon storage lipids, which supply carbon and energy during germination. FAE1 disruption redirects flux toward C18 oleic, linoleic, and linolenic acids (jarvis2021crisprcas9inducedfad2and pages 1-2, mcginn2019moleculartoolsenabling pages 9-11, jarvis2021crisprcas9inducedfad2and pages 2-3). |
| Recent applications (2023–2024) | A 2023 review identified **CRISPR/Cas9 editing of TaFAE1** as a leading pennycress domestication strategy for producing low-/zero-erucic, canola-like edible oil; the underlying edited alleles yield negligible C20:1 and C22:1. In 2024, transcriptomic and lipidomic profiling refined the pathway model by showing coordinated, maturation-stage-dependent incorporation of erucic acid into TAG, informing future engineering of either low-erucic food oils or high-erucic industrial/biofuel oils (ma2023researchprogresson pages 1-2, mcginn2019moleculartoolsenabling pages 9-11, claver2024transcriptomicandlipidomic pages 1-2). |


*Table: This table summarizes the verified identity, catalytic function, substrate specificity, ER localization, pathway context, biological role, and recent biotechnology applications of FAE1 in field pennycress.*

## Conclusions

FAE1 in *Thlaspi arvense* is a well-characterized β-ketoacyl-CoA synthase that plays a central role in determining seed oil composition through its function in the ER fatty acid elongation pathway. The enzyme specifically converts oleoyl-CoA (18:1-CoA) to eicosenoyl-CoA (20:1-CoA) and erucoyl-CoA (22:1-CoA) as the condensing, substrate-selecting component of a four-enzyme elongation complex. The high affinity of pennycress FAE1 for 20:1-CoA substrates explains the characteristically high erucic acid content in wild-type pennycress seed oil.

The enzyme localizes to the endoplasmic reticulum membrane, where it operates as part of a multi-component complex including KCR, HCD, and ECR enzymes that complete the elongation cycle. The resulting erucic acid is incorporated into seed storage triacylglycerols through coordinated action of Kennedy pathway and acyl-editing routes, with particularly high accumulation in cotyledon storage tissues that fuel seedling emergence.

Recent research from 2023-2024 has established CRISPR/Cas9 editing of TaFAE1 as a key domestication strategy for pennycress, enabling production of both low-erucic edible oils and high-erucic industrial/biofuel feedstocks. Advanced multi-omics studies continue to refine our understanding of pathway coordination and regulation, while emerging work explores pleiotropic effects on stress tolerance. These developments position FAE1 as both a model for understanding plant lipid metabolism and a practical target for oilseed crop improvement.

References

1. (mcginn2019moleculartoolsenabling pages 9-11): Michaela McGinn, Winthrop B. Phippen, Ratan Chopra, Sunil Bansal, Brice A. Jarvis, Mary E. Phippen, Kevin M. Dorn, Maliheh Esfahanian, Tara J. Nazarenus, Edgar B. Cahoon, Timothy P. Durrett, M. David Marks, and John C. Sedbrook. Molecular tools enabling pennycress (thlaspi arvense) as a model plant and oilseed cash cover crop. Plant Biotechnology Journal, 17:776-788, Oct 2019. URL: https://doi.org/10.1111/pbi.13014, doi:10.1111/pbi.13014. This article has 162 citations and is from a highest quality peer-reviewed journal.

2. (bashiri2024engineeringerucicacid pages 1-2): Hoda Bashiri, Danial Kahrizi, Ali Hatef Salmanian, Hassan Rahnama, and Pejman Azadi. Engineering erucic acid biosynthesis in camelina (camelina sativa) via fae1 gene cloning and antisense technology. Cellular and molecular biology, 70 7:243-251, Jul 2024. URL: https://doi.org/10.14715/cmb/2024.70.7.35, doi:10.14715/cmb/2024.70.7.35. This article has 7 citations.

3. (khan2023comparativephylogenomicinsights pages 1-2): Uzair Muhammad Khan, Iqrar Ahmad Rana, Nabeel Shaheen, Qasim Raza, Hafiz Mamoon Rehman, Rizwana Maqbool, Iqrar Ahmad Khan, and Rana Muhammad Atif. Comparative phylogenomic insights of kcs and elo gene families in brassica species indicate their role in seed development and stress responsiveness. Scientific Reports, Mar 2023. URL: https://doi.org/10.1038/s41598-023-28665-2, doi:10.1038/s41598-023-28665-2. This article has 13 citations and is from a peer-reviewed journal.

4. (zhukov2022synthesisofc20–38 pages 6-7): Anatoly Zhukov and Valery Popov. Synthesis of c20–38 fatty acids in plant tissues. International Journal of Molecular Sciences, 23:4731, Apr 2022. URL: https://doi.org/10.3390/ijms23094731, doi:10.3390/ijms23094731. This article has 31 citations.

5. (zhukov2022synthesisofc20–38 pages 12-14): Anatoly Zhukov and Valery Popov. Synthesis of c20–38 fatty acids in plant tissues. International Journal of Molecular Sciences, 23:4731, Apr 2022. URL: https://doi.org/10.3390/ijms23094731, doi:10.3390/ijms23094731. This article has 31 citations.

6. (jarvis2021crisprcas9inducedfad2and pages 2-3): Brice A. Jarvis, Trevor B. Romsdahl, Michaela G. McGinn, Tara J. Nazarenus, Edgar B. Cahoon, Kent D. Chapman, and John C. Sedbrook. Crispr/cas9-induced fad2 and rod1 mutations stacked with fae1 confer high oleic acid seed oil in pennycress (thlaspi arvense l.). Frontiers in Plant Science, Apr 2021. URL: https://doi.org/10.3389/fpls.2021.652319, doi:10.3389/fpls.2021.652319. This article has 83 citations.

7. (claver2024transcriptomicandlipidomic pages 2-3): Ana Claver, María Ángeles Luján, José Manuel Escuín, Marion Schilling, Juliette Jouhet, María Savirón, M. Victoria López, Rafael Picorel, Carmen Jarne, Vicente L. Cebolla, and Miguel Alfonso. Transcriptomic and lipidomic analysis of the differential pathway contribution to the incorporation of erucic acid to triacylglycerol during pennycress seed maturation. Frontiers in Plant Science, Apr 2024. URL: https://doi.org/10.3389/fpls.2024.1386023, doi:10.3389/fpls.2024.1386023. This article has 18 citations.

8. (claver2024transcriptomicandlipidomic pages 1-2): Ana Claver, María Ángeles Luján, José Manuel Escuín, Marion Schilling, Juliette Jouhet, María Savirón, M. Victoria López, Rafael Picorel, Carmen Jarne, Vicente L. Cebolla, and Miguel Alfonso. Transcriptomic and lipidomic analysis of the differential pathway contribution to the incorporation of erucic acid to triacylglycerol during pennycress seed maturation. Frontiers in Plant Science, Apr 2024. URL: https://doi.org/10.3389/fpls.2024.1386023, doi:10.3389/fpls.2024.1386023. This article has 18 citations.

9. (patra2025heterologousexpressionin pages 6-9): Neelesh Patra, Susamoy Sarkar, and Mrinal K. Maiti. Heterologous expression in saccharomyces and chlamydomonas reveals host-dependent activity of brassica juncea fatty acid elongase1 isozymes. bioRxiv, May 2025. URL: https://doi.org/10.1101/2025.05.20.655142, doi:10.1101/2025.05.20.655142. This article has 1 citations.

10. (patra2025heterologousexpressionin pages 1-4): Neelesh Patra, Susamoy Sarkar, and Mrinal K. Maiti. Heterologous expression in saccharomyces and chlamydomonas reveals host-dependent activity of brassica juncea fatty acid elongase1 isozymes. bioRxiv, May 2025. URL: https://doi.org/10.1101/2025.05.20.655142, doi:10.1101/2025.05.20.655142. This article has 1 citations.

11. (zhukov2022synthesisofc20–38 pages 4-6): Anatoly Zhukov and Valery Popov. Synthesis of c20–38 fatty acids in plant tissues. International Journal of Molecular Sciences, 23:4731, Apr 2022. URL: https://doi.org/10.3390/ijms23094731, doi:10.3390/ijms23094731. This article has 31 citations.

12. (zhukov2022synthesisofc20–38 pages 8-10): Anatoly Zhukov and Valery Popov. Synthesis of c20–38 fatty acids in plant tissues. International Journal of Molecular Sciences, 23:4731, Apr 2022. URL: https://doi.org/10.3390/ijms23094731, doi:10.3390/ijms23094731. This article has 31 citations.

13. (zhukov2022synthesisofc20–38 pages 7-8): Anatoly Zhukov and Valery Popov. Synthesis of c20–38 fatty acids in plant tissues. International Journal of Molecular Sciences, 23:4731, Apr 2022. URL: https://doi.org/10.3390/ijms23094731, doi:10.3390/ijms23094731. This article has 31 citations.

14. (fatima2026fae1andfad2 pages 2-4): Samia Fatima, Nadia Iqbal, Shengqiao Lu, Muhammad Omar Khan, Muhammad Aamer Mehmood, Sameer H. Qari, Atif Jamal, Zhengyi Wei, and Niaz Ahmad. Fae1 and fad2 gene expression dynamics and fatty acid modulation in brassica under salt stress: a molecular insight. PLOS One, 21:e0345945, Apr 2026. URL: https://doi.org/10.1371/journal.pone.0345945, doi:10.1371/journal.pone.0345945. This article has 2 citations and is from a peer-reviewed journal.

15. (claver2024transcriptomicandlipidomic pages 3-5): Ana Claver, María Ángeles Luján, José Manuel Escuín, Marion Schilling, Juliette Jouhet, María Savirón, M. Victoria López, Rafael Picorel, Carmen Jarne, Vicente L. Cebolla, and Miguel Alfonso. Transcriptomic and lipidomic analysis of the differential pathway contribution to the incorporation of erucic acid to triacylglycerol during pennycress seed maturation. Frontiers in Plant Science, Apr 2024. URL: https://doi.org/10.3389/fpls.2024.1386023, doi:10.3389/fpls.2024.1386023. This article has 18 citations.

16. (park2022applicationsandprospects pages 4-5): Mid-Eum Park and Hyun Uk Kim. Applications and prospects of genome editing in plant fatty acid and triacylglycerol biosynthesis. Frontiers in Plant Science, Aug 2022. URL: https://doi.org/10.3389/fpls.2022.969844, doi:10.3389/fpls.2022.969844. This article has 31 citations.

17. (jarvis2021crisprcas9inducedfad2and pages 1-2): Brice A. Jarvis, Trevor B. Romsdahl, Michaela G. McGinn, Tara J. Nazarenus, Edgar B. Cahoon, Kent D. Chapman, and John C. Sedbrook. Crispr/cas9-induced fad2 and rod1 mutations stacked with fae1 confer high oleic acid seed oil in pennycress (thlaspi arvense l.). Frontiers in Plant Science, Apr 2021. URL: https://doi.org/10.3389/fpls.2021.652319, doi:10.3389/fpls.2021.652319. This article has 83 citations.

18. (esfahanian2021generatingpennycress(thlaspi pages 1-2): Maliheh Esfahanian, Tara J. Nazarenus, Meghan M. Freund, Gary McIntosh, Winthrop B. Phippen, Mary E. Phippen, Timothy P. Durrett, Edgar B. Cahoon, and John C. Sedbrook. Generating pennycress (thlaspi arvense) seed triacylglycerols and acetyl-triacylglycerols containing medium-chain fatty acids. Frontiers in Energy Research, Jan 2021. URL: https://doi.org/10.3389/fenrg.2021.620118, doi:10.3389/fenrg.2021.620118. This article has 28 citations.

19. (ma2023researchprogresson pages 1-2): Jianyu Ma, Haoyu Wang, and Yuhong Zhang. Research progress on the development of pennycress (thlaspi arvense l.) as a new seed oil crop: a review. Frontiers in Plant Science, Nov 2023. URL: https://doi.org/10.3389/fpls.2023.1268085, doi:10.3389/fpls.2023.1268085. This article has 10 citations.

20. (fatima2026fae1andfad2 pages 1-2): Samia Fatima, Nadia Iqbal, Shengqiao Lu, Muhammad Omar Khan, Muhammad Aamer Mehmood, Sameer H. Qari, Atif Jamal, Zhengyi Wei, and Niaz Ahmad. Fae1 and fad2 gene expression dynamics and fatty acid modulation in brassica under salt stress: a molecular insight. PLOS One, 21:e0345945, Apr 2026. URL: https://doi.org/10.1371/journal.pone.0345945, doi:10.1371/journal.pone.0345945. This article has 2 citations and is from a peer-reviewed journal.

21. (claver2025transcriptomicandproteomic pages 1-2): Ana Claver, Patricia Lorente, Victoria Lo ´ pez, Miguel Alfonso, Giovanni Stefano, Adrian Troncoso, and An-Shan Hsiao. Transcriptomic and proteomic analysis of oil body associated protein dynamics in the biofuel feedstock pennycress (thlaspi arvense). Frontiers in Plant Science, Feb 2025. URL: https://doi.org/10.3389/fpls.2025.1530718, doi:10.3389/fpls.2025.1530718. This article has 5 citations.

## Artifacts

- [Edison artifact artifact-00](FAE1-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. mcginn2019moleculartoolsenabling pages 9-11
2. claver2024transcriptomicandlipidomic pages 1-2
3. park2022applicationsandprospects pages 4-5
4. claver2024transcriptomicandlipidomic pages 2-3
5. ma2023researchprogresson pages 1-2
6. claver2025transcriptomicandproteomic pages 1-2
7. bashiri2024engineeringerucicacid pages 1-2
8. khan2023comparativephylogenomicinsights pages 1-2
9. patra2025heterologousexpressionin pages 6-9
10. patra2025heterologousexpressionin pages 1-4
11. claver2024transcriptomicandlipidomic pages 3-5
12. https://doi.org/10.1111/pbi.13014,
13. https://doi.org/10.14715/cmb/2024.70.7.35,
14. https://doi.org/10.1038/s41598-023-28665-2,
15. https://doi.org/10.3390/ijms23094731,
16. https://doi.org/10.3389/fpls.2021.652319,
17. https://doi.org/10.3389/fpls.2024.1386023,
18. https://doi.org/10.1101/2025.05.20.655142,
19. https://doi.org/10.1371/journal.pone.0345945,
20. https://doi.org/10.3389/fpls.2022.969844,
21. https://doi.org/10.3389/fenrg.2021.620118,
22. https://doi.org/10.3389/fpls.2023.1268085,
23. https://doi.org/10.3389/fpls.2025.1530718,