---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-10T14:33:13.498518'
end_time: '2026-09-10T14:40:50.196818'
duration_seconds: 456.7
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: NTPase
  gene_symbol: NTPase
  uniprot_accession: O76268
  protein_description: 'RecName: Full=nucleoside diphosphate phosphatase {ECO:0000256|ARBA:ARBA00038863};
    EC=3.6.1.6 {ECO:0000256|ARBA:ARBA00038863};'
  gene_info: Name=NTPase {ECO:0000313|EMBL:AAF51182.1, ECO:0000313|FlyBase:FBgn0024947};
    Synonyms=Dmel\CG3059 {ECO:0000313|EMBL:AAF51182.1}, dmNTPase {ECO:0000313|EMBL:AAF51182.1},
    NTPDase6 {ECO:0000313|EMBL:AAF51182.1}; ORFNames=CG3059 {ECO:0000313|EMBL:AAF51182.1,
    ECO:0000313|FlyBase:FBgn0024947}, Dmel_CG3059 {ECO:0000313|EMBL:AAF51182.1};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Belongs to the GDA1/CD39 NTPase family.
  protein_domains: GDA1_CD39_NTPase. (IPR000407); GDA1_CD39 (PF01150)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 15
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: NTPase-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** O76268
- **Protein Description:** RecName: Full=nucleoside diphosphate phosphatase {ECO:0000256|ARBA:ARBA00038863}; EC=3.6.1.6 {ECO:0000256|ARBA:ARBA00038863};
- **Gene Information:** Name=NTPase {ECO:0000313|EMBL:AAF51182.1, ECO:0000313|FlyBase:FBgn0024947}; Synonyms=Dmel\CG3059 {ECO:0000313|EMBL:AAF51182.1}, dmNTPase {ECO:0000313|EMBL:AAF51182.1}, NTPDase6 {ECO:0000313|EMBL:AAF51182.1}; ORFNames=CG3059 {ECO:0000313|EMBL:AAF51182.1, ECO:0000313|FlyBase:FBgn0024947}, Dmel_CG3059 {ECO:0000313|EMBL:AAF51182.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the GDA1/CD39 NTPase family.
- **Key Domains:** GDA1_CD39_NTPase. (IPR000407); GDA1_CD39 (PF01150)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "NTPase" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'NTPase' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **NTPase** (gene ID: NTPase, UniProt: O76268) in DROME.

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
- **UniProt Accession:** O76268
- **Protein Description:** RecName: Full=nucleoside diphosphate phosphatase {ECO:0000256|ARBA:ARBA00038863}; EC=3.6.1.6 {ECO:0000256|ARBA:ARBA00038863};
- **Gene Information:** Name=NTPase {ECO:0000313|EMBL:AAF51182.1, ECO:0000313|FlyBase:FBgn0024947}; Synonyms=Dmel\CG3059 {ECO:0000313|EMBL:AAF51182.1}, dmNTPase {ECO:0000313|EMBL:AAF51182.1}, NTPDase6 {ECO:0000313|EMBL:AAF51182.1}; ORFNames=CG3059 {ECO:0000313|EMBL:AAF51182.1, ECO:0000313|FlyBase:FBgn0024947}, Dmel_CG3059 {ECO:0000313|EMBL:AAF51182.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the GDA1/CD39 NTPase family.
- **Key Domains:** GDA1_CD39_NTPase. (IPR000407); GDA1_CD39 (PF01150)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "NTPase" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'NTPase' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **NTPase** (gene ID: NTPase, UniProt: O76268) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Drosophila melanogaster* NTPase/CG3059 (UniProt O76268)

## Executive conclusion

The target is the *D. melanogaster* protein represented by UniProt O76268, not a generic nucleotide-binding “NTPase.” The supplied identifiers—**NTPase**, **dmNTPase**, **CG3059**, and **NTPDase6**—are consistent with the fly’s single reported CD39-like nucleoside triphosphate diphosphohydrolase gene. It produces four annotated transcripts, NTDPase-RA through -RD. The experimentally studied RA product is an **intracellular endoplasmic-reticulum (ER) nucleoside diphosphatase** with maximal activity toward **GDP, IDP, and UDP**, rather than a plasma-membrane ATP-selective ectonucleotidase. (volonte2022delineatingpurinergicsignaling pages 5-7)

The most defensible primary reaction is therefore:

**nucleoside diphosphate + H₂O → nucleoside monophosphate + inorganic phosphate**, 

with GDP, IDP, and UDP among the preferred substrates. The available evidence does not establish exact kinetic constants, a complete substrate ranking, physiological nucleotide concentrations, or the relative activity toward every NTP and NDP.

## 1. Identity verification and ambiguity control

“NTPase” is an intrinsically ambiguous symbol because it can denote many unrelated nucleotide-hydrolyzing proteins. Here, identity is constrained by the accession, organism, aliases, and domain assignment supplied in the query: **UniProt O76268; *Drosophila melanogaster*; CG3059/dmNTPase/NTPDase6; GDA1/CD39 family; PF01150/IPR000407**. Literature searches were therefore restricted to this fly CD39-like enzyme and did not transfer findings from unrelated NTPases or from mammalian CD39/ENTPD1.

The independent literature alignment is strong: a 2022 review reports only **one CD39-like NTPDase gene** in the fly genome and four transcripts—RA, RB, RC, and RD—and describes the RA protein as homologous to mammalian NTPDase6. (volonte2022delineatingpurinergicsignaling pages 5-7) Earlier comparative work identified a predicted *Drosophila* CD39-family sequence sharing **44% amino-acid identity** with a characterized rat ER Ca²⁺-dependent nucleoside diphosphatase. At that earlier stage, however, the authors explicitly regarded the fly protein’s function and localization as undetermined. (failer2002cloningexpressionand pages 7-8)

Thus, the family/domain and organism match the requested protein. A residual nomenclature limitation is that some papers say only “Drosophila NTDPase/CD39-like gene” rather than explicitly printing CG3059 or O76268.

## 2. Molecular function and substrate specificity

### Direct target-specific evidence

Functional expression of NTDPase-RA in *Drosophila* Schneider 2 cells showed maximal activity with **GDP, IDP, and UDP**. This supports the UniProt description “nucleoside diphosphate phosphatase” and EC 3.6.1.6, and distinguishes the enzyme from classical cell-surface NTPDases whose central role is often ATP/ADP degradation. (volonte2022delineatingpurinergicsignaling pages 5-7)

The evidence available here does **not** justify a numerical *K*m, *V*max, catalytic efficiency, strict ordering among GDP/IDP/UDP, or a statement that other nucleotides are completely inactive. It establishes a preferred substrate class and three high-activity substrates, not absolute specificity.

### Family-supported catalytic mechanism

GDA1/CD39-family proteins generally hydrolyze the terminal phosphoanhydride bond of nucleoside 5′-tri- and/or diphosphates. They contain five apyrase conserved regions, ACR1–ACR5, involved in phosphate recognition and catalysis; conserved motifs include actin/HSP70/sugar-kinase-like phosphate-binding features and a conserved DXG element. Their activity commonly requires Ca²⁺ or Mg²⁺, but cation preference varies substantially among paralogs. (zimmermann2000extracellularmetabolismof pages 2-4, robson2006theentpdasefamily pages 4-6)

These structural principles support O76268’s enzymatic annotation because it carries the corresponding GDA1_CD39 domain. Nevertheless, divalent-cation dependence and the catalytic contribution of individual residues have not been demonstrated directly for CG3059 in the evidence retrieved.

## 3. Cellular localization and topology

NTDPase-RA was primarily intracellular and localized to the **ER** when expressed in S2 cells; it was not detected as a cell-surface enzyme. (volonte2022delineatingpurinergicsignaling pages 5-7) This is the clearest localization evidence and directly argues against annotating O76268 as the fly equivalent of plasma-membrane CD39/ENTPD1.

Intracellular NTPDases characteristically expose their catalytic domains to an organelle lumen, whereas cell-surface NTPDases expose them extracellularly. Accordingly, a **lumen-facing ER catalytic domain** is a strong topology hypothesis for O76268, but it remains an inference unless directly established by protease protection, selective permeabilization, or equivalent topology experiments. (failer2002cloningexpressionand pages 1-1, robson2006theentpdasefamily pages 2-4)

Older sequence analysis noted that the *Drosophila* protein was unusually long among compared homologues, contained three possible in-frame start codons, and that invertebrate members had one amino-terminal hydrophobic region rather than the two described for vertebrate sequences. (failer2002cloningexpressionand pages 3-4) These observations may relate to isoform selection or membrane targeting, but they are not sufficient to resolve endogenous topology by themselves.

## 4. Biological process and pathway interpretation

The best mechanistic model is that O76268 regulates **ER-luminal nucleoside-diphosphate pools**, especially UDP-, GDP-, and IDP-related pools. Hydrolysis of NDPs to NMPs could facilitate nucleotide-sugar metabolism by removing luminal NDP products and supporting antiport or recycling processes associated with glycosylation. A characterized mammalian ER nucleoside diphosphatase has been proposed to support glycosylation-related quality control, providing a biologically plausible analogy. (failer2002cloningexpressionand pages 7-8, failer2002cloningexpressionand pages 1-1)

This pathway assignment must remain qualified. No retrieved experiment showed that CG3059 knockout or knockdown changes protein glycosylation, ER stress, nucleotide-sugar transport, development, or organismal physiology. The direct annotation is therefore **ER NDP hydrolysis**; “glycosylation/protein-quality-control support” is a family- and compartment-based hypothesis.

A canonical extracellular ATP/ADP–P2 receptor pathway is comparatively unlikely. The studied protein is not cell-surface localized, and *Drosophila* lacks identified P2X-like genes; the 2022 review also noted that extracellular ATP/ADP transport and accumulation had not been quantified in flies. (volonte2022delineatingpurinergicsignaling pages 5-7) This does not exclude all extracellular nucleotide biology, but it means mammalian CD39-mediated vascular, immune, or platelet functions should not be assigned to O76268.

## 5. Expression, isoforms, and organismal function

The strongest quantitative genomic observation is **one CD39-like gene producing four transcripts**. Only the RA product is clearly covered by the retrieved biochemical and localization evidence. (volonte2022delineatingpurinergicsignaling pages 5-7) Isoform-specific abundance, tissue distribution, developmental regulation, and whether RB–RD encode catalytically or topologically distinct proteins remain unresolved.

No precise in-vivo phenotype was found for CG3059/O76268. Consequently, broad claims about development, nervous-system function, immunity, fertility, stress responses, or viability would be speculative. High-throughput expression or interaction records, if present in databases, should be treated as hypothesis-generating until connected to enzyme activity through targeted genetics and metabolite analysis.

## 6. Recent developments and state of the literature

No 2023–2024 publication located in this search added direct biochemical, structural, genetic, or localization evidence for O76268. The most recent authoritative target-relevant synthesis found was **Volonté et al., published December 2022**, which summarized the four transcripts, S2-cell expression, GDP/IDP/UDP preference, ER localization, and absence from the cell surface. (volonte2022delineatingpurinergicsignaling pages 5-7)

The underlying *Drosophila* functional study cited by that review is Fenckova et al., **“Functional characterization of ecto-5′-nucleotidases and apyrases in Drosophila melanogaster,” published in 2011** (DOI URL listed in the review’s references: journal citation *Insect Biochemistry and Molecular Biology* 41:956–967). (volonte2022delineatingpurinergicsignaling pages 9-11) The foundational comparative study is Failer, Braun, and Zimmermann, **October 2002**, DOI: https://doi.org/10.1074/jbc.M201656200. (failer2002cloningexpressionand pages 7-8) Authoritative family context is provided by Robson, Sévigny, and Zimmermann, **May 2006**, DOI: https://doi.org/10.1007/s11302-006-9003-5. (robson2006theentpdasefamily pages 4-6)

The absence of recent target-specific work is itself significant: O76268 remains a sparsely characterized enzyme for which the principal advances are still heterologous biochemical characterization and compartment assignment, not modern in-vivo functional genomics or structural biology.

## 7. Applications and expert assessment

There is no validated therapeutic, diagnostic, industrial, agricultural, or other real-world implementation specific to CG3059/O76268. Its current application is primarily as a research target for understanding intracellular nucleotide metabolism and the evolutionary diversification of CD39-family enzymes.

From an annotation perspective, the expert interpretation should be conservative:

1. **High confidence:** O76268 is the *D. melanogaster* CG3059/dmNTPase CD39-family protein; RA is an ER-localized intracellular enzyme.
2. **Moderate-to-high confidence:** its primary biochemical role is NDP hydrolysis, with GDP, IDP, and UDP as preferred experimental substrates.
3. **Moderate confidence:** catalysis occurs on the ER-luminal side and follows the conserved five-ACR GDA1/CD39 mechanism.
4. **Low-to-moderate confidence:** the physiological purpose is nucleotide-sugar/glycosylation homeostasis or ER quality control.
5. **Unsupported at present:** a specific in-vivo phenotype, extracellular purinergic-signaling role, quantitative kinetics, or practical application.

The evidence hierarchy is summarized below.

| Annotation dimension | Best-supported conclusion | Evidence type | Confidence | Key limitation |
|---|---|---|---|---|
| Identity and aliases | *Drosophila melanogaster* NTPase/CG3059 (dmNTPase; NTPDase6-like), UniProt O76268; the generic symbol “NTPase” must not be confused with unrelated NTPases. | Database-provided identity | High | Literature often uses NTDPase/CD39-like terminology without explicitly stating CG3059 or O76268. |
| Gene and transcripts | The fly genome contains one CD39-like NTPDase gene reported to produce four transcripts: NTDPase-RA, -RB, -RC, and -RD. (volonte2022delineatingpurinergicsignaling pages 5-7) | Direct genomic/transcript annotation | High | Isoform-specific protein expression and functions beyond RA are not established. |
| Primary substrate specificity | RA expressed in Schneider 2 cells showed maximal activity with GDP, IDP, and UDP, supporting classification as a nucleoside diphosphatase rather than an ATP-selective ecto-apyrase. (volonte2022delineatingpurinergicsignaling pages 5-7) | Direct experiment | Moderate–high | Quantitative kinetics and a complete substrate ranking were not available in the reviewed evidence. |
| Catalytic reaction | Best-supported reaction: NDP + H₂O → NMP + inorganic phosphate; likely preferred substrates include GDP, IDP, and UDP. GDA1/CD39-family enzymes can also hydrolyze NTPs, but the extent for O76268 is unresolved. (zimmermann2000extracellularmetabolismof pages 2-4, failer2002cloningexpressionand pages 1-1, volonte2022delineatingpurinergicsignaling pages 5-7) | Direct experiment plus family inference | Moderate–high | Exact stoichiometry, catalytic constants, cation dependence, and physiological substrate concentrations remain unreported for the fly enzyme. |
| Localization | NTDPase-RA is primarily intracellular and localized to the endoplasmic reticulum, not the cell surface, in transfected Drosophila S2 cells. (volonte2022delineatingpurinergicsignaling pages 5-7) | Direct experiment | High for RA in S2 cells | Endogenous localization across fly tissues, developmental stages, and other isoforms has not been established. |
| Family and catalytic architecture | O76268 belongs to the GDA1/CD39 NTPase family; this family is defined by five apyrase conserved regions (ACR1–ACR5) involved in phosphate binding and catalysis. (zimmermann2000extracellularmetabolismof pages 2-4, robson2006theentpdasefamily pages 4-6) | Database-provided identity plus family inference | High for family membership; moderate for residue-level function | The five ACRs and essential residues have not been functionally mutated in CG3059 itself. |
| Catalytic orientation | Because RA is an ER membrane protein related to intracellular NTPDases, its catalytic domain is likely oriented toward the ER lumen. (failer2002cloningexpressionand pages 1-1, robson2006theentpdasefamily pages 2-4) | Family/topology inference | Moderate | Luminal orientation has not been directly demonstrated for O76268. |
| Biological pathway | A plausible role is hydrolysis of luminal UDP/GDP/IDP to support ER nucleotide and nucleotide-sugar homeostasis, potentially coupling to glycosylation or protein-quality-control processes. (failer2002cloningexpressionand pages 1-1, volonte2022delineatingpurinergicsignaling pages 5-7) | Family/ortholog inference | Low–moderate | No direct evidence links CG3059 loss or activity to glycosylation, nucleotide-sugar transport, or ER quality control in vivo. |
| Evolutionary support | The predicted fly sequence was reported to share 44% identity with a characterized rat ER Ca²⁺-dependent nucleoside diphosphatase, while insect sequences form a distinct group. (failer2002cloningexpressionand pages 7-8) | Comparative sequence inference | Moderate | Homology does not establish identical cation dependence, specificity, targeting signals, or physiology. |
| Purinergic signaling | Current evidence argues against assigning O76268 a canonical cell-surface ATP/ADP-signaling role: RA is ER-localized, and Drosophila lacks identified P2X-like genes. (robson2006theentpdasefamily pages 1-2, volonte2022delineatingpurinergicsignaling pages 5-7) | Direct localization plus comparative-genomic inference | Moderate–high | Absence of a known P2X system does not exclude all extracellular nucleotide biology or unidentified receptors. |
| Organismal phenotype and application | No validated organismal phenotype, disease role, therapeutic use, biotechnology implementation, or other real-world application is established specifically for CG3059/O76268. | Evidence-gap assessment | High | Target-specific genetic and physiological studies are sparse; absence of evidence is not evidence of dispensability. |


*Table: Evidence-confidence summary for functional annotation of Drosophila NTPase/CG3059 (UniProt O76268), separating direct findings from database identity and family-level inference. It highlights the strong ER-localization and NDP-substrate evidence while making unresolved pathway and physiological claims explicit.*

## 8. Priority experiments

The most informative next studies would be endogenous epitope tagging to verify tissue and ER localization; topology mapping to test luminal orientation; purified-enzyme kinetics across NDPs and NTPs with Ca²⁺ versus Mg²⁺; isoform-specific expression analysis; and CG3059 loss-of-function combined with ER nucleotide/nucleotide-sugar metabolomics and glycoproteomics. These experiments would convert the current compartment- and homology-based pathway model into a physiological annotation.

References

1. (volonte2022delineatingpurinergicsignaling pages 5-7): Cinzia Volonté, Francesca Alberti, Giuseppe Vitale, and Francesco Liguori. Delineating purinergic signaling in drosophila. Dec 2022. URL: https://doi.org/10.3390/ijms232315196, doi:10.3390/ijms232315196. This article has 4 citations.

2. (failer2002cloningexpressionand pages 7-8): Bernd U. Failer, Norbert Braun, and Herbert Zimmermann. Cloning, expression, and functional characterization of a ca2+-dependent endoplasmic reticulum nucleoside diphosphatase*. The Journal of Biological Chemistry, 277:36978-36986, Oct 2002. URL: https://doi.org/10.1074/jbc.m201656200, doi:10.1074/jbc.m201656200. This article has 69 citations.

3. (zimmermann2000extracellularmetabolismof pages 2-4): Herbert Zimmermann. Extracellular metabolism of atp and other nucleotides. Naunyn-Schmiedeberg's Archives of Pharmacology, 362:299-309, Aug 2000. URL: https://doi.org/10.1007/s002100000309, doi:10.1007/s002100000309. This article has 1400 citations.

4. (robson2006theentpdasefamily pages 4-6): Simon C. Robson, Jean Sévigny, and Herbert Zimmermann. The e-ntpdase family of ectonucleotidases: structure function relationships and pathophysiological significance. Purinergic Signalling, 2:409-430, May 2006. URL: https://doi.org/10.1007/s11302-006-9003-5, doi:10.1007/s11302-006-9003-5. This article has 1230 citations and is from a peer-reviewed journal.

5. (failer2002cloningexpressionand pages 1-1): Bernd U. Failer, Norbert Braun, and Herbert Zimmermann. Cloning, expression, and functional characterization of a ca2+-dependent endoplasmic reticulum nucleoside diphosphatase*. The Journal of Biological Chemistry, 277:36978-36986, Oct 2002. URL: https://doi.org/10.1074/jbc.m201656200, doi:10.1074/jbc.m201656200. This article has 69 citations.

6. (robson2006theentpdasefamily pages 2-4): Simon C. Robson, Jean Sévigny, and Herbert Zimmermann. The e-ntpdase family of ectonucleotidases: structure function relationships and pathophysiological significance. Purinergic Signalling, 2:409-430, May 2006. URL: https://doi.org/10.1007/s11302-006-9003-5, doi:10.1007/s11302-006-9003-5. This article has 1230 citations and is from a peer-reviewed journal.

7. (failer2002cloningexpressionand pages 3-4): Bernd U. Failer, Norbert Braun, and Herbert Zimmermann. Cloning, expression, and functional characterization of a ca2+-dependent endoplasmic reticulum nucleoside diphosphatase*. The Journal of Biological Chemistry, 277:36978-36986, Oct 2002. URL: https://doi.org/10.1074/jbc.m201656200, doi:10.1074/jbc.m201656200. This article has 69 citations.

8. (volonte2022delineatingpurinergicsignaling pages 9-11): Cinzia Volonté, Francesca Alberti, Giuseppe Vitale, and Francesco Liguori. Delineating purinergic signaling in drosophila. Dec 2022. URL: https://doi.org/10.3390/ijms232315196, doi:10.3390/ijms232315196. This article has 4 citations.

9. (robson2006theentpdasefamily pages 1-2): Simon C. Robson, Jean Sévigny, and Herbert Zimmermann. The e-ntpdase family of ectonucleotidases: structure function relationships and pathophysiological significance. Purinergic Signalling, 2:409-430, May 2006. URL: https://doi.org/10.1007/s11302-006-9003-5, doi:10.1007/s11302-006-9003-5. This article has 1230 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](NTPase-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. volonte2022delineatingpurinergicsignaling pages 5-7
2. failer2002cloningexpressionand pages 7-8
3. failer2002cloningexpressionand pages 3-4
4. volonte2022delineatingpurinergicsignaling pages 9-11
5. robson2006theentpdasefamily pages 4-6
6. zimmermann2000extracellularmetabolismof pages 2-4
7. failer2002cloningexpressionand pages 1-1
8. robson2006theentpdasefamily pages 2-4
9. robson2006theentpdasefamily pages 1-2
10. https://doi.org/10.1074/jbc.M201656200.
11. https://doi.org/10.1007/s11302-006-9003-5.
12. https://doi.org/10.3390/ijms232315196,
13. https://doi.org/10.1074/jbc.m201656200,
14. https://doi.org/10.1007/s002100000309,
15. https://doi.org/10.1007/s11302-006-9003-5,