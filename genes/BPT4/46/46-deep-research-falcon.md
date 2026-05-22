---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-21T19:56:58.246144'
end_time: '2026-05-21T20:12:15.134949'
duration_seconds: 916.89
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: BPT4
  gene_id: '46'
  gene_symbol: '46'
  uniprot_accession: P04522
  protein_description: 'RecName: Full=Exonuclease subunit 2; EC=3.1.11.-; AltName:
    Full=Gene product 46; Short=gp46;'
  gene_info: Name=46;
  organism_full: Enterobacteria phage T4 (Bacteriophage T4).
  protein_family: To phage T5 protein D13 and to yeast RAD52. .
  protein_domains: P-loop_NTPase. (IPR027417); Rad50/SbcC_AAA. (IPR038729); AAA_23
    (PF13476)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 39
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 1
  edison_message_content: 1
artifacts:
- filename: artifact-00.md
  path: 46-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: image-1.png
  path: 46-deep-research-falcon_artifacts/image-1.png
  media_type: image/png
  source: edison_message_content
  data_storage_id: null
  description: '## Context ID: pqac-00000012 I have extracted Table 1, Table 2, and
    Figure 2 from the document, which provide the information on protein interactions
    and exonuc'
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P04522
- **Protein Description:** RecName: Full=Exonuclease subunit 2; EC=3.1.11.-; AltName: Full=Gene product 46; Short=gp46;
- **Gene Information:** Name=46;
- **Organism (full):** Enterobacteria phage T4 (Bacteriophage T4).
- **Protein Family:** To phage T5 protein D13 and to yeast RAD52. .
- **Key Domains:** P-loop_NTPase. (IPR027417); Rad50/SbcC_AAA. (IPR038729); AAA_23 (PF13476)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "46" matches the protein description above**
2. **Verify the organism is correct:** Enterobacteria phage T4 (Bacteriophage T4).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol '46' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **46** (gene ID: 46, UniProt: P04522) in BPT4.

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
- **UniProt Accession:** P04522
- **Protein Description:** RecName: Full=Exonuclease subunit 2; EC=3.1.11.-; AltName: Full=Gene product 46; Short=gp46;
- **Gene Information:** Name=46;
- **Organism (full):** Enterobacteria phage T4 (Bacteriophage T4).
- **Protein Family:** To phage T5 protein D13 and to yeast RAD52. .
- **Key Domains:** P-loop_NTPase. (IPR027417); Rad50/SbcC_AAA. (IPR038729); AAA_23 (PF13476)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "46" matches the protein description above**
2. **Verify the organism is correct:** Enterobacteria phage T4 (Bacteriophage T4).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol '46' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **46** (gene ID: 46, UniProt: P04522) in BPT4.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Research report: functional annotation of bacteriophage T4 gene 46 (gp46; UniProt P04522)

### Executive summary (identity verified)
The target protein is **gene product 46 (gp46)** from **Enterobacteria phage T4**, UniProt **P04522**, historically annotated as part of a T4 **exonuclease complex**. The modern consensus from genetics and biochemistry is that gp46 is the **Rad50-family ATPase subunit** of a phage **Mre11–Rad50 (MR)–like DNA end-processing complex** formed with **gp47 (Mre11 homolog)**; this complex is required in vivo for **homologous recombination, recombination-dependent DNA replication (RDR), and double-strand break (DSB) repair**. (kreuzer1995recombinationdependentdnareplication pages 1-2, albrecht2012disruptionofthe pages 1-2, herdendorf2014catalyticmechanismof pages 1-2)

| Aspect | Evidence-backed summary | Key source(s) |
|---|---|---|
| identity/domains | **Verified target:** Enterobacteria phage T4 **gene 46 / gp46** corresponds to the **Rad50 homolog** of the T4 gp46/gp47 DNA end-processing complex, matching the UniProt P04522 context. Biochemical and genetic literature consistently treats gp46 as an **ABC/SMC-like ATPase** with a conserved nucleotide-binding domain; this aligns with UniProt/InterPro assignment to **P-loop NTPase / Rad50-SbcC AAA+ family**. | Herdendorf & Nelson 2014, *Biochemistry*, doi:10.1021/bi500558d, https://doi.org/10.1021/bi500558d; Albrecht et al. 2012, *J Biol Chem*, doi:10.1074/jbc.M112.392316, https://doi.org/10.1074/jbc.M112.392316 (herdendorf2014catalyticmechanismof pages 1-2, albrecht2012disruptionofthe pages 1-2) |
| complex partners | gp46 functions with **gp47 (the T4 Mre11 homolog)** as the T4 **MR complex**; biochemical interaction data also support association of gp46/gp47 with **UvsY**, linking DNA end resection to presynaptic filament assembly during recombination. | Bleuit et al. 2001, *PNAS*, doi:10.1073/pnas.131007498, https://doi.org/10.1073/pnas.131007498; Albrecht et al. 2012, *J Biol Chem*, https://doi.org/10.1074/jbc.M112.392316 (bleuit2001mediatorproteinsorchestrate pages 2-3, albrecht2012disruptionofthe pages 1-2, bleuit2001mediatorproteinsorchestrate media 03c6cc3c) |
| enzymatic activities | The **primary catalytic activity of the complex is 5′→3′ dsDNA exonuclease activity**, genetically assigned to gp46/gp47 and biochemically observed in reconstituted assays; **gp46 itself is also an ATP-binding/hydrolyzing enzyme** whose ATPase is strongly stimulated by gp47 and DNA. Thus, gp46 is best annotated as the **ATPase/structural motor subunit** of an exonuclease complex rather than the nuclease active site itself. | Bleuit et al. 2001, *PNAS*, https://doi.org/10.1073/pnas.131007498; Herdendorf & Nelson 2014, *Biochemistry*, https://doi.org/10.1021/bi500558d (bleuit2001mediatorproteinsorchestrate pages 2-3, herdendorf2014catalyticmechanismof pages 1-2) |
| substrate specificity | Available data support activity on **DNA ends**, especially **double-stranded DNA substrates requiring 5′-strand resection** to generate recombinogenic 3′ ssDNA tails. Structural/mechanistic work indicates Rad50 can partially occlude nuclease sites such that **ssDNA more readily accesses Mre11/gp47 nuclease sites**, consistent with staged processing of DNA ends rather than indiscriminate nucleolysis. | Mosig 1998, *Annu Rev Genet*, doi:10.1146/annurev.genet.32.1.379, https://doi.org/10.1146/annurev.genet.32.1.379; Albrecht et al. 2012, *J Biol Chem*, https://doi.org/10.1074/jbc.M112.392316 (mosig1998recombinationandrecombinationdependent pages 8-10, albrecht2012disruptionofthe pages 2-3) |
| mechanistic model | Current model: gp46 **binds/hydrolyzes ATP at the Rad50 head dimer interface**; ATP-driven conformational cycling promotes assembly at DNA ends and transitions to a **translocation state** that supports processive nuclease action by gp47. Work on the T4 MR system supports a **two-state mechanism** (initiation/assembly vs translocation), with allosteric communication from gp47 to gp46 required for full ATPase activation. | Albrecht et al. 2012, *J Biol Chem*, https://doi.org/10.1074/jbc.M112.392316; Herdendorf & Nelson 2014, *Biochemistry*, https://doi.org/10.1021/bi500558d (albrecht2012disruptionofthe pages 2-3, herdendorf2014catalyticmechanismof pages 1-2, albrecht2012disruptionofthe pages 10-11) |
| pathway/biological role | gp46 is **essential in vivo** for **homologous recombination**, **double-strand break repair**, and **recombination-dependent DNA replication (RDR)** in bacteriophage T4. Genetic studies show gene 46 mutants are strongly recombination-defective, and plasmid/phage assays place gp46 among the core factors needed to repair DSBs through replication-coupled pathways. | Kreuzer et al. 1995, *J Bacteriol*, doi:10.1128/jb.177.23.6844-6853.1995, https://doi.org/10.1128/jb.177.23.6844-6853.1995; George & Kreuzer 1996, *Genetics*, doi:10.1093/genetics/143.4.1507, https://doi.org/10.1093/genetics/143.4.1507; Mosig 1998, https://doi.org/10.1146/annurev.genet.32.1.379 (kreuzer1995recombinationdependentdnareplication pages 1-2, mosig1998recombinationandrecombinationdependent pages 8-10) |
| localization/cellular context | No evidence supports a virion structural role or extracellular localization. Function is best placed in the **infected E. coli cytoplasm**, where gp46 acts on **phage DNA replication/recombination intermediates** and damaged DNA ends; older work also reported a **membrane-associated DNase activity controlled by genes 46/47**, but the strongest modern interpretation is a DNA-metabolic role in intracellular nucleoprotein complexes rather than stable membrane localization. | Claudia & Wiberg 1981, *J Virol*, doi:10.1128/JVI.40.1.65-77.1981, https://doi.org/10.1128/JVI.40.1.65-77.1981; Liu & Morrical 2010, *Virology Journal*, doi:10.1186/1743-422X-7-357, https://doi.org/10.1186/1743-422X-7-357 (mosig1998recombinationandrecombinationdependent pages 8-10, bleuit2001mediatorproteinsorchestrate pages 2-3) |
| key quantitative data | Reported quantitative findings include: **gp46 ATPase kcat ≈ 0.15 s⁻¹ alone** and **≈ 3.2 s⁻¹ with gp47 + dsDNA** (~20-fold activation); ATPase cooperativity increases from **Hill ~1.4 (gp46 alone)** to **~2.4 (MR-D complex)**. In a dsDNA exonuclease assay, retained label fell from **100% control to 44% with gp46 alone** and to **14% with gp46+gp47**, supporting gp47 stimulation of nuclease function. An Mre11-interface mutant reduced dsDNA exonuclease activity by **~10-fold** under processive conditions. | Herdendorf & Nelson 2014, *Biochemistry*, https://doi.org/10.1021/bi500558d; Bleuit et al. 2001, *PNAS*, https://doi.org/10.1073/pnas.131007498; Albrecht et al. 2012, *J Biol Chem*, https://doi.org/10.1074/jbc.M112.392316 (albrecht2012disruptionofthe pages 2-3, herdendorf2014catalyticmechanismof pages 1-2, herdendorf2014catalyticmechanismof pages 2-3, bleuit2001mediatorproteinsorchestrate pages 2-3, bleuit2001mediatorproteinsorchestrate media 03c6cc3c) |
| recent 2023-2024 developments | Direct 2023-2024 gp46-specific primary literature appears limited, but recent cross-system structural work strengthened inference: a **2024 yeast MR cryo-EM study** mapped conserved Rad50 ATP- and DNA-contacting residues and explicitly linked corresponding **T4 gp46 residues** to reduced ATP binding/hydrolysis and defective gp47-dependent nuclease activity, reinforcing mechanistic conservation between phage and eukaryotic MR complexes. | Petrini et al. 2024, *Research Square* preprint, doi:10.21203/rs.3.rs-5390974/v1, https://doi.org/10.21203/rs.3.rs-5390974/v1 (petrini2024structureguidedfunctional pages 4-7, petrini2024structureguidedfunctional pages 7-9) |
| applications | **No established 2023-2024 biotechnology application specifically uses gp46** itself. Modern T4-derived applications in diagnostics primarily exploit other recombination proteins (**UvsX, UvsY, gp32**) in RPA/SIBA isothermal amplification platforms. Therefore, gp46 is currently more important as a **mechanistic model for MR/Rad50 biology** than as a routine applied reagent. | Morrical 2025, *EcoSal Plus*, doi:10.1128/ecosalplus.esp-0003-2025, https://doi.org/10.1128/ecosalplus.esp-0003-2025; Liu et al. 2024, *Front Cell Infect Microbiol*, doi:10.3389/fcimb.2024.1281827, https://doi.org/10.3389/fcimb.2024.1281827; Anbazhagan et al. 2024, *3 Biotech*, doi:10.1007/s13205-024-04055-x, https://doi.org/10.1007/s13205-024-04055-x (morrical2025thebacteriophaget4 pages 9-12) |


*Table: This table condenses the strongest evidence on the identity, biochemical role, pathway function, mechanistic model, and recent context for Enterobacteria phage T4 gene 46 (gp46; UniProt P04522). It is useful as a compact functional annotation that distinguishes direct evidence from broader pathway and comparative inferences.*

---

## 1) Key concepts and definitions (current understanding)

### 1.1 Recombination-dependent replication (RDR)
**RDR** in phage T4 is a replication initiation/restart mode that uses recombination intermediates (e.g., D-loops, broken DNA ends) to reconstitute active replication forks. A classic synthesis is Mosig’s review, which emphasizes that recombination and DNA replication are tightly coupled in T4 and that **genes 46 and 47 are essential for recombination** and are implicated in processing DNA to create recombinogenic substrates for strand invasion and restart. (Mosig 1998, published Dec 1998; https://doi.org/10.1146/annurev.genet.32.1.379) (mosig1998recombinationandrecombinationdependent pages 8-10)

### 1.2 The phage T4 MR complex (gp46/gp47)
The T4 gp46/gp47 complex is functionally analogous to cellular **Mre11–Rad50** systems that recognize and process DSB ends. In T4, **gp46 is the Rad50 homolog** (ATPase/motor-like subunit), while **gp47 is the Mre11 homolog** (nuclease subunit). Disrupting the Mre11-like subunit’s interface can impair allosteric activation of gp46 ATP hydrolysis and reduce processive exonuclease activity, supporting a coupled motor–nuclease mechanism. (Albrecht et al. 2012, published Sep 2012; https://doi.org/10.1074/jbc.M112.392316) (albrecht2012disruptionofthe pages 1-2, albrecht2012disruptionofthe pages 10-11)

### 1.3 “Exonuclease subunit 2” and what is catalytically active
Although UniProt labels P04522 as “**Exonuclease subunit 2**,” the best-supported mechanistic interpretation from biochemical studies is:
- The **MR complex displays 5′→3′ dsDNA exonuclease activity**, genetically assigned to gp46/47 and measurable in reconstituted systems. (bleuit2001mediatorproteinsorchestrate pages 2-3)
- **gp46’s primary biochemical role is ATP binding/hydrolysis** (Rad50-like ABC/SMC ATPase), which is strongly stimulated by gp47 and DNA and helps drive conformational changes and translocation states that enable processive nuclease function. (herdendorf2014catalyticmechanismof pages 1-2, albrecht2012disruptionofthe pages 2-3)

---

## 2) Primary function, reaction, and substrate specificity

### 2.1 Enzymatic activities
**(A) ATPase activity (gp46 as Rad50 ATPase)**
Gp46 is an ABC/SMC-like ATPase whose ATP turnover is **weak alone** but **strongly activated** in the presence of gp47 and dsDNA. Quantitatively, gp46 ATPase has **kcat ≈ 0.15 s⁻¹** alone and increases to **kcat ≈ 3.2 s⁻¹** with gp47 and dsDNA (≈20-fold activation), consistent with an ATP-driven conformational cycle in the assembled MR–DNA complex. (Albrecht et al. 2012; https://doi.org/10.1074/jbc.M112.392316) (albrecht2012disruptionofthe pages 2-3)
Kinetic dissection of ATP hydrolysis indicates increased **positive cooperativity** in the activated state (Hill coefficient **~2.4** for MR–DNA vs **~1.4** for gp46 alone) and supports a model in which ATP hydrolysis proceeds through an **asymmetric, dissociative-like transition state**, with chemistry likely rate-limiting under the examined conditions. (Herdendorf & Nelson 2014, published Aug 2014; https://doi.org/10.1021/bi500558d) (herdendorf2014catalyticmechanismof pages 1-2, herdendorf2014catalyticmechanismof pages 2-3)

**(B) Exonuclease activity (MR complex)**
In vitro assays consistent with exonuclease action show that gp46 alone causes partial degradation of a blunt dsDNA substrate, and addition of gp47 strongly increases degradation. In a representative experiment, the **retained label** on uniformly labeled dsDNA fell from **100% (control)** to **44% with gp46**, and to **14% with gp46+gp47**. (Bleuit et al. 2001, published Jul 2001; https://doi.org/10.1073/pnas.131007498) (bleuit2001mediatorproteinsorchestrate pages 2-3)
The corresponding assay summary table and model figure were extracted from the source (Table 2 and Figure 2). (bleuit2001mediatorproteinsorchestrate media e27cae80, bleuit2001mediatorproteinsorchestrate media 665e248d)

### 2.2 Substrate specificity and biochemical role at DNA ends
Genetic and mechanistic syntheses support that gene 46/47 functions generate or process DNA structures needed for recombination—e.g., converting nicks to gaps or processing ends to generate ssDNA for recombinase loading. (mosig1998recombinationandrecombinationdependent pages 8-10)
Mechanistically, the MR complex is interpreted as acting at **DNA ends** produced by DSBs or replication fork collapse, coordinating ATP-driven transitions with nuclease processing. A two-state scheme (initiation/assembly vs translocation) has been proposed for nuclease progression, where ATP hydrolysis promotes a translocation state enabling processive nucleotide removal; a mutation disrupting the Mre11 dimer interface reduces dsDNA exonuclease activity ~10-fold under processive conditions. (albrecht2012disruptionofthe pages 1-2)

---

## 3) Biological processes and pathways in infected cells

### 3.1 Essentiality for recombination, DSB repair, and RDR (in vivo)
**Severe recombination deficiency:** Mutations in genes 46 and 47 cause a “most severe recombination deficiency,” consistent with central roles in T4 homologous recombination pathways. (Mosig 1998; https://doi.org/10.1146/annurev.genet.32.1.379) (mosig1998recombinationandrecombinationdependent pages 8-10)

**RDR stimulated by DSBs:** In vivo systems that model DSB-stimulated RDR identify gp46 and gp47 among key factors required for recombination-dependent replication, even though some earlier in vitro reconstitutions did not require them—highlighting that gp46/47 likely act on DNA–protein architectures or intermediates present in vivo. (Kreuzer et al. 1995, published Dec 1995; https://doi.org/10.1128/jb.177.23.6844-6853.1995) (kreuzer1995recombinationdependentdnareplication pages 1-2)

### 3.2 Functional coupling to presynaptic filament assembly
Biochemical interaction data indicate physical association of gp46 and gp47 with each other and with the recombination mediator **UvsY**, suggesting coordination between end processing (resection) and assembly of recombinase filaments on ssDNA. (Bleuit et al. 2001; https://doi.org/10.1073/pnas.131007498) (bleuit2001mediatorproteinsorchestrate pages 2-3)
A schematic model explicitly links **gp46/47-catalyzed resection** to **UvsY-mediated presynaptic filament assembly** (Figure 2). (bleuit2001mediatorproteinsorchestrate media 665e248d)

---

## 4) Cellular localization / where gp46 functions
Direct subcellular localization evidence is limited in the retrieved corpus. However, all functional evidence places gp46’s role within **intracellular DNA metabolism** during infection (processing phage DNA ends and recombination intermediates), i.e., in the **E. coli cytoplasm** where phage DNA replication and recombination occur. This is supported by pathway placement in genetic/biochemical studies of RDR and DSB repair in infected cells. (kreuzer1995recombinationdependentdnareplication pages 1-2, mosig1998recombinationandrecombinationdependent pages 8-10)
Older studies reported a **membrane-associated DNase activity** controlled by genes 46/47, which may reflect association of nuclease activity with cellular fractions under certain experimental conditions rather than an obligate membrane-localized function. (Claudia & Wiberg 1981, published Oct 1981; https://doi.org/10.1128/JVI.40.1.65-77.1981) (mosig1998recombinationandrecombinationdependent pages 8-10)

---

## 5) Expert synthesis and authoritative perspectives

### 5.1 Conservation across life and mechanistic analogy
A notable theme in the T4 literature is deep conservation of recombination/repair systems. For example, yeast RAD52 can complement T4 gene 46 or 47 defects in E. coli-based assays, suggesting mechanistic overlap in recombination functions (though not specifying enzymology). (Bernstein & Bernstein 1989, published May 1989; https://doi.org/10.1128/jb.171.5.2265-2270.1989) (bernstein1989bacteriophaget4genetic pages 3-4)

### 5.2 “What gp46 does” in one sentence
The best evidence-supported functional annotation is:
**gp46 is a Rad50-family ATPase that, in complex with gp47 (Mre11 nuclease), uses ATP-driven conformational cycling to support processive DNA end processing (exonucleolytic resection) required for T4 homologous recombination, DSB repair, and recombination-dependent DNA replication.** (herdendorf2014catalyticmechanismof pages 1-2, albrecht2012disruptionofthe pages 1-2, bleuit2001mediatorproteinsorchestrate pages 2-3, kreuzer1995recombinationdependentdnareplication pages 1-2)

---

## 6) Recent developments (prioritizing 2023–2024)

### 6.1 2024 structural insight reinforcing T4 gp46 functional inference
Direct 2023–2024 primary literature on **T4 gp46 itself** was sparse in retrieval. However, 2024 high-resolution cryo-EM and structure-guided functional analysis of the **yeast MR complex** mapped conserved Rad50 ATP-coordinating residues and explicitly connected them to prior mutational/biochemical results in **bacteriophage T4 Rad50 (gp46)**. The manuscript notes that mutating the corresponding residues in T4 gp46 **severely reduces ATP binding affinity and hydrolysis** and also impairs **gp47-dependent nuclease activity**, strengthening the mechanistic linkage between conserved ATP coordination and nuclease function across evolution. (Petrini et al. 2024, published Dec 2024; https://doi.org/10.21203/rs.3.rs-5390974/v1) (petrini2024structureguidedfunctional pages 4-7, petrini2024structureguidedfunctional pages 7-9)

---

## 7) Current applications and real-world implementations

### 7.1 T4 recombination proteins in diagnostics (but not gp46)
Modern, real-world implementations of T4 recombination proteins are strongest in **isothermal nucleic acid amplification** (e.g., recombinase polymerase amplification, RPA), which uses T4 proteins such as **UvsX, UvsY, and gp32**. A 2024 RPA-based diagnostic study reports reaction times on the order of minutes and clinically evaluated performance (e.g., agreement vs qPCR), explicitly listing these T4 recombination proteins among core components. (Liu et al. 2024, published Feb 2024; https://doi.org/10.3389/fcimb.2024.1281827) (mosig1998recombinationandrecombinationdependent pages 8-10)
A 2024 review of RPA–CRISPR integrations similarly describes the roles of **UvsX (recombinase), UvsY (loading factor), and gp32 (SSB)** in amplification workflows. (Anbazhagan et al. 2024, published Aug 2024; https://doi.org/10.1007/s13205-024-04055-x) (mosig1998recombinationandrecombinationdependent pages 8-10)

### 7.2 Implication for gp46
In the retrieved applied literature and a recent systems-level review of T4 homologous recombination applications, **gp46/gp47 are not described as core reagents** for the widely used RPA/SIBA amplification technologies, which primarily use UvsX/UvsY/gp32 plus a strand-displacing polymerase. Thus, gp46’s current “real-world” impact is mainly as a **mechanistic model** for Mre11–Rad50 biology rather than as a routine biotechnology enzyme component. (Morrical 2025, published Dec 2025; https://doi.org/10.1128/ecosalplus.esp-0003-2025) (morrical2025thebacteriophaget4 pages 9-12)

---

## 8) Key statistics/data points (from recent and classic studies)

- **ATPase turnover (gp46 alone):** kcat ≈ **0.15 s⁻¹** (Albrecht et al. 2012; https://doi.org/10.1074/jbc.M112.392316). (albrecht2012disruptionofthe pages 2-3)
- **ATPase turnover (gp46 + gp47 + dsDNA):** kcat ≈ **3.2 s⁻¹** (~20-fold stimulation). (albrecht2012disruptionofthe pages 2-3)
- **Cooperativity (Hill coefficient):** ~**1.4** (gp46) vs ~**2.4** (MR–DNA). (Herdendorf & Nelson 2014; https://doi.org/10.1021/bi500558d). (herdendorf2014catalyticmechanismof pages 1-2)
- **Exonuclease assay (retained label):** **44%** with gp46 alone and **14%** with gp46+gp47 (vs 100% control), indicating gp47 stimulation of nuclease action in vitro. (Bleuit et al. 2001; https://doi.org/10.1073/pnas.131007498). (bleuit2001mediatorproteinsorchestrate pages 2-3)
- **Processivity phenotype:** Mre11 dimer-interface disruption reduces dsDNA exonuclease activity by ~**10-fold** under processive conditions, consistent with ATPase-driven translocation and state switching. (Albrecht et al. 2012). (albrecht2012disruptionofthe pages 1-2)

The key tables/figure supporting interaction and nuclease assay claims are shown in extracted images (Table 1, Table 2, Figure 2). (bleuit2001mediatorproteinsorchestrate media 03c6cc3c, bleuit2001mediatorproteinsorchestrate media e27cae80, bleuit2001mediatorproteinsorchestrate media 665e248d)

---

## 9) Limitations and confidence

- **High confidence (direct experimental evidence):** gp46 is a Rad50-like ATPase; its ATPase is stimulated by gp47+DNA; gp46/gp47 shows exonuclease activity in vitro; gp46 is required in vivo for RDR/DSB repair. (herdendorf2014catalyticmechanismof pages 1-2, albrecht2012disruptionofthe pages 2-3, bleuit2001mediatorproteinsorchestrate pages 2-3, kreuzer1995recombinationdependentdnareplication pages 1-2)
- **Moderate confidence (inference supported by genetics/biophysics):** substrate preference for DNA ends and staged processing to produce recombinogenic ssDNA tails; ATP-driven conformational cycling enabling translocation. (mosig1998recombinationandrecombinationdependent pages 8-10, albrecht2012disruptionofthe pages 10-11)
- **Lower confidence (limited direct evidence in retrieved set):** precise intracellular spatial localization (e.g., membrane vs nucleoid-associated replication centers) and complete kinetic parameters for nuclease steps (Km for DNA, processivity lengths, detailed rate constants of resection). (mosig1998recombinationandrecombinationdependent pages 8-10)

---

## References (publication date and URL)

- Mosig G. **1998-12**. *Annual Review of Genetics*. “Recombination and recombination-dependent DNA replication in bacteriophage T4.” https://doi.org/10.1146/annurev.genet.32.1.379 (mosig1998recombinationandrecombinationdependent pages 8-10)
- Kreuzer K, Saunders M, Weislo LJ, Kreuzer H. **1995-12**. *Journal of Bacteriology*. “Recombination-dependent DNA replication stimulated by double-strand breaks in bacteriophage T4.” https://doi.org/10.1128/jb.177.23.6844-6853.1995 (kreuzer1995recombinationdependentdnareplication pages 1-2)
- Bleuit JS et al. **2001-07**. *PNAS*. “Mediator proteins orchestrate enzyme-ssDNA assembly during T4 recombination-dependent DNA replication and repair.” https://doi.org/10.1073/pnas.131007498 (bleuit2001mediatorproteinsorchestrate pages 2-3)
- Albrecht DW et al. **2012-09**. *J Biol Chem*. “Disruption of the Bacteriophage T4 Mre11 Dimer Interface Reveals a Two-state Mechanism for Exonuclease Activity.” https://doi.org/10.1074/jbc.M112.392316 (albrecht2012disruptionofthe pages 1-2)
- Herdendorf TJ, Nelson SW. **2014-08**. *Biochemistry*. “Catalytic mechanism of bacteriophage T4 Rad50 ATP hydrolysis.” https://doi.org/10.1021/bi500558d (herdendorf2014catalyticmechanismof pages 1-2)
- Petrini J et al. **2024-12**. *Research Square (preprint)*. “Structure guided functional analysis of the S. cerevisiae Mre11 complex.” https://doi.org/10.21203/rs.3.rs-5390974/v1 (petrini2024structureguidedfunctional pages 4-7)
- Liu M et al. **2024-02**. *Frontiers in Cellular and Infection Microbiology*. “Establishment and application of a rapid molecular diagnostic platform… based on recombinase polymerase.” https://doi.org/10.3389/fcimb.2024.1281827 (mosig1998recombinationandrecombinationdependent pages 8-10)
- Anbazhagan P et al. **2024-08**. *3 Biotech*. “Advances in plant pathogen detection: integrating recombinase polymerase amplification with CRISPR/Cas systems.” https://doi.org/10.1007/s13205-024-04055-x (mosig1998recombinationandrecombinationdependent pages 8-10)
- Morrical SW. **2025-12**. *EcoSal Plus*. “The bacteriophage T4 homologous recombination system: mechanism, applications, conservation, and environmental significance.” https://doi.org/10.1128/ecosalplus.esp-0003-2025 (morrical2025thebacteriophaget4 pages 9-12)


References

1. (kreuzer1995recombinationdependentdnareplication pages 1-2): K. Kreuzer, M. Saunders, L. J. Weislo, and H. Kreuzer. Recombination-dependent dna replication stimulated by double-strand breaks in bacteriophage t4. Journal of Bacteriology, 177:6844-6853, Dec 1995. URL: https://doi.org/10.1128/jb.177.23.6844-6853.1995, doi:10.1128/jb.177.23.6844-6853.1995. This article has 51 citations and is from a peer-reviewed journal.

2. (albrecht2012disruptionofthe pages 1-2): Dustin W. Albrecht, Timothy J. Herdendorf, and Scott W. Nelson. Disruption of the bacteriophage t4 mre11 dimer interface reveals a two-state mechanism for exonuclease activity. Journal of Biological Chemistry, 287:31371-31381, Sep 2012. URL: https://doi.org/10.1074/jbc.m112.392316, doi:10.1074/jbc.m112.392316. This article has 18 citations and is from a domain leading peer-reviewed journal.

3. (herdendorf2014catalyticmechanismof pages 1-2): Timothy J. Herdendorf and Scott W. Nelson. Catalytic mechanism of bacteriophage t4 rad50 atp hydrolysis. Biochemistry, 53 35:5647-60, Aug 2014. URL: https://doi.org/10.1021/bi500558d, doi:10.1021/bi500558d. This article has 18 citations and is from a peer-reviewed journal.

4. (bleuit2001mediatorproteinsorchestrate pages 2-3): Jill S. Bleuit, Hang Xu, Yujie Ma, Tongsheng Wang, Jie Liu, and Scott W. Morrical. Mediator proteins orchestrate enzyme-ssdna assembly during t4 recombination-dependent dna replication and repair. Proceedings of the National Academy of Sciences of the United States of America, 98:8298-8305, Jul 2001. URL: https://doi.org/10.1073/pnas.131007498, doi:10.1073/pnas.131007498. This article has 103 citations and is from a highest quality peer-reviewed journal.

5. (bleuit2001mediatorproteinsorchestrate media 03c6cc3c): Jill S. Bleuit, Hang Xu, Yujie Ma, Tongsheng Wang, Jie Liu, and Scott W. Morrical. Mediator proteins orchestrate enzyme-ssdna assembly during t4 recombination-dependent dna replication and repair. Proceedings of the National Academy of Sciences of the United States of America, 98:8298-8305, Jul 2001. URL: https://doi.org/10.1073/pnas.131007498, doi:10.1073/pnas.131007498. This article has 103 citations and is from a highest quality peer-reviewed journal.

6. (mosig1998recombinationandrecombinationdependent pages 8-10): Gisela Mosig. Recombination and recombination-dependent dna replication in bacteriophage t4. Annual review of genetics, 32:379-413, Dec 1998. URL: https://doi.org/10.1146/annurev.genet.32.1.379, doi:10.1146/annurev.genet.32.1.379. This article has 234 citations and is from a domain leading peer-reviewed journal.

7. (albrecht2012disruptionofthe pages 2-3): Dustin W. Albrecht, Timothy J. Herdendorf, and Scott W. Nelson. Disruption of the bacteriophage t4 mre11 dimer interface reveals a two-state mechanism for exonuclease activity. Journal of Biological Chemistry, 287:31371-31381, Sep 2012. URL: https://doi.org/10.1074/jbc.m112.392316, doi:10.1074/jbc.m112.392316. This article has 18 citations and is from a domain leading peer-reviewed journal.

8. (albrecht2012disruptionofthe pages 10-11): Dustin W. Albrecht, Timothy J. Herdendorf, and Scott W. Nelson. Disruption of the bacteriophage t4 mre11 dimer interface reveals a two-state mechanism for exonuclease activity. Journal of Biological Chemistry, 287:31371-31381, Sep 2012. URL: https://doi.org/10.1074/jbc.m112.392316, doi:10.1074/jbc.m112.392316. This article has 18 citations and is from a domain leading peer-reviewed journal.

9. (herdendorf2014catalyticmechanismof pages 2-3): Timothy J. Herdendorf and Scott W. Nelson. Catalytic mechanism of bacteriophage t4 rad50 atp hydrolysis. Biochemistry, 53 35:5647-60, Aug 2014. URL: https://doi.org/10.1021/bi500558d, doi:10.1021/bi500558d. This article has 18 citations and is from a peer-reviewed journal.

10. (petrini2024structureguidedfunctional pages 4-7): John Petrini, Marcel Hohl, You Yu, Vitaly Kuryavyi, and Dinshaw Patel. Structure guided functional analysis of the s. cerevisiae mre11 complex. Research Square, Dec 2024. URL: https://doi.org/10.21203/rs.3.rs-5390974/v1, doi:10.21203/rs.3.rs-5390974/v1. This article has 3 citations.

11. (petrini2024structureguidedfunctional pages 7-9): John Petrini, Marcel Hohl, You Yu, Vitaly Kuryavyi, and Dinshaw Patel. Structure guided functional analysis of the s. cerevisiae mre11 complex. Research Square, Dec 2024. URL: https://doi.org/10.21203/rs.3.rs-5390974/v1, doi:10.21203/rs.3.rs-5390974/v1. This article has 3 citations.

12. (morrical2025thebacteriophaget4 pages 9-12): Scott W. Morrical. The bacteriophage t4 homologous recombination system: mechanism, applications, conservation, and environmental significance. EcoSal Plus, Dec 2025. URL: https://doi.org/10.1128/ecosalplus.esp-0003-2025, doi:10.1128/ecosalplus.esp-0003-2025. This article has 0 citations.

13. (bleuit2001mediatorproteinsorchestrate media e27cae80): Jill S. Bleuit, Hang Xu, Yujie Ma, Tongsheng Wang, Jie Liu, and Scott W. Morrical. Mediator proteins orchestrate enzyme-ssdna assembly during t4 recombination-dependent dna replication and repair. Proceedings of the National Academy of Sciences of the United States of America, 98:8298-8305, Jul 2001. URL: https://doi.org/10.1073/pnas.131007498, doi:10.1073/pnas.131007498. This article has 103 citations and is from a highest quality peer-reviewed journal.

14. (bleuit2001mediatorproteinsorchestrate media 665e248d): Jill S. Bleuit, Hang Xu, Yujie Ma, Tongsheng Wang, Jie Liu, and Scott W. Morrical. Mediator proteins orchestrate enzyme-ssdna assembly during t4 recombination-dependent dna replication and repair. Proceedings of the National Academy of Sciences of the United States of America, 98:8298-8305, Jul 2001. URL: https://doi.org/10.1073/pnas.131007498, doi:10.1073/pnas.131007498. This article has 103 citations and is from a highest quality peer-reviewed journal.

15. (bernstein1989bacteriophaget4genetic pages 3-4): H. Bernstein and C. Bernstein. Bacteriophage t4 genetic homologies with bacteria and eucaryotes. Journal of Bacteriology, 171:2265-2270, May 1989. URL: https://doi.org/10.1128/jb.171.5.2265-2270.1989, doi:10.1128/jb.171.5.2265-2270.1989. This article has 51 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](46-deep-research-falcon_artifacts/artifact-00.md)
![## Context ID: pqac-00000012 I have extracted Table 1, Table 2, and Figure 2 from the document, which provide the information on protein interactions and exonuc](46-deep-research-falcon_artifacts/image-1.png)

## Citations

1. mosig1998recombinationandrecombinationdependent pages 8-10
2. bleuit2001mediatorproteinsorchestrate pages 2-3
3. albrecht2012disruptionofthe pages 2-3
4. albrecht2012disruptionofthe pages 1-2
5. kreuzer1995recombinationdependentdnareplication pages 1-2
6. herdendorf2014catalyticmechanismof pages 1-2
7. petrini2024structureguidedfunctional pages 4-7
8. albrecht2012disruptionofthe pages 10-11
9. herdendorf2014catalyticmechanismof pages 2-3
10. petrini2024structureguidedfunctional pages 7-9
11. https://doi.org/10.1021/bi500558d;
12. https://doi.org/10.1074/jbc.M112.392316
13. https://doi.org/10.1073/pnas.131007498;
14. https://doi.org/10.1021/bi500558d
15. https://doi.org/10.1146/annurev.genet.32.1.379;
16. https://doi.org/10.1074/jbc.M112.392316;
17. https://doi.org/10.1128/jb.177.23.6844-6853.1995;
18. https://doi.org/10.1093/genetics/143.4.1507;
19. https://doi.org/10.1146/annurev.genet.32.1.379
20. https://doi.org/10.1128/JVI.40.1.65-77.1981;
21. https://doi.org/10.1186/1743-422X-7-357
22. https://doi.org/10.21203/rs.3.rs-5390974/v1
23. https://doi.org/10.1128/ecosalplus.esp-0003-2025;
24. https://doi.org/10.3389/fcimb.2024.1281827;
25. https://doi.org/10.1007/s13205-024-04055-x
26. https://doi.org/10.1073/pnas.131007498
27. https://doi.org/10.1128/jb.177.23.6844-6853.1995
28. https://doi.org/10.1128/JVI.40.1.65-77.1981
29. https://doi.org/10.1128/jb.171.5.2265-2270.1989
30. https://doi.org/10.3389/fcimb.2024.1281827
31. https://doi.org/10.1128/ecosalplus.esp-0003-2025
32. https://doi.org/10.1128/jb.177.23.6844-6853.1995,
33. https://doi.org/10.1074/jbc.m112.392316,
34. https://doi.org/10.1021/bi500558d,
35. https://doi.org/10.1073/pnas.131007498,
36. https://doi.org/10.1146/annurev.genet.32.1.379,
37. https://doi.org/10.21203/rs.3.rs-5390974/v1,
38. https://doi.org/10.1128/ecosalplus.esp-0003-2025,
39. https://doi.org/10.1128/jb.171.5.2265-2270.1989,