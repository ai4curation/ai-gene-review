---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-25T15:33:50.454454'
end_time: '2026-09-25T15:42:56.594117'
duration_seconds: 546.14
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: AASS
  gene_symbol: AASS
  uniprot_accession: Q9UDR5
  protein_description: 'RecName: Full=Alpha-aminoadipic semialdehyde synthase, mitochondrial
    {ECO:0000305|PubMed:10775527, ECO:0000305|PubMed:463877}; AltName: Full=LKR/SDH
    {ECO:0000305|PubMed:10775527}; Includes: RecName: Full=Lysine ketoglutarate reductase
    {ECO:0000305|PubMed:10775527}; Short=LKR {ECO:0000303|PubMed:10775527}; Short=LOR;
    EC=1.5.1.8 {ECO:0000269|PubMed:10775527, ECO:0000269|PubMed:463877}; Includes:
    RecName: Full=Saccharopine dehydrogenase {ECO:0000305|PubMed:10775527}; Short=SDH
    {ECO:0000303|PubMed:10775527}; EC=1.5.1.9 {ECO:0000269|PubMed:10775527, ECO:0000269|PubMed:463877};
    Flags: Precursor;'
  gene_info: Name=AASS {ECO:0000312|HGNC:HGNC:17366};
  organism_full: Homo sapiens (Human).
  protein_family: In the C-terminal section; belongs to the saccharopine
  protein_domains: AASS. (IPR051168); AlaDH/PNT_N. (IPR007886); AlaDH/PNT_NAD(H)-bd.
    (IPR007698); NAD(P)-bd_dom_sf. (IPR036291); Sacchrp_dh-like_C. (IPR032095)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 31
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: AASS-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q9UDR5
- **Protein Description:** RecName: Full=Alpha-aminoadipic semialdehyde synthase, mitochondrial {ECO:0000305|PubMed:10775527, ECO:0000305|PubMed:463877}; AltName: Full=LKR/SDH {ECO:0000305|PubMed:10775527}; Includes: RecName: Full=Lysine ketoglutarate reductase {ECO:0000305|PubMed:10775527}; Short=LKR {ECO:0000303|PubMed:10775527}; Short=LOR; EC=1.5.1.8 {ECO:0000269|PubMed:10775527, ECO:0000269|PubMed:463877}; Includes: RecName: Full=Saccharopine dehydrogenase {ECO:0000305|PubMed:10775527}; Short=SDH {ECO:0000303|PubMed:10775527}; EC=1.5.1.9 {ECO:0000269|PubMed:10775527, ECO:0000269|PubMed:463877}; Flags: Precursor;
- **Gene Information:** Name=AASS {ECO:0000312|HGNC:HGNC:17366};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** In the C-terminal section; belongs to the saccharopine
- **Key Domains:** AASS. (IPR051168); AlaDH/PNT_N. (IPR007886); AlaDH/PNT_NAD(H)-bd. (IPR007698); NAD(P)-bd_dom_sf. (IPR036291); Sacchrp_dh-like_C. (IPR032095)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "AASS" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'AASS' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **AASS** (gene ID: AASS, UniProt: Q9UDR5) in human.

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
- **UniProt Accession:** Q9UDR5
- **Protein Description:** RecName: Full=Alpha-aminoadipic semialdehyde synthase, mitochondrial {ECO:0000305|PubMed:10775527, ECO:0000305|PubMed:463877}; AltName: Full=LKR/SDH {ECO:0000305|PubMed:10775527}; Includes: RecName: Full=Lysine ketoglutarate reductase {ECO:0000305|PubMed:10775527}; Short=LKR {ECO:0000303|PubMed:10775527}; Short=LOR; EC=1.5.1.8 {ECO:0000269|PubMed:10775527, ECO:0000269|PubMed:463877}; Includes: RecName: Full=Saccharopine dehydrogenase {ECO:0000305|PubMed:10775527}; Short=SDH {ECO:0000303|PubMed:10775527}; EC=1.5.1.9 {ECO:0000269|PubMed:10775527, ECO:0000269|PubMed:463877}; Flags: Precursor;
- **Gene Information:** Name=AASS {ECO:0000312|HGNC:HGNC:17366};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** In the C-terminal section; belongs to the saccharopine
- **Key Domains:** AASS. (IPR051168); AlaDH/PNT_N. (IPR007886); AlaDH/PNT_NAD(H)-bd. (IPR007698); NAD(P)-bd_dom_sf. (IPR036291); Sacchrp_dh-like_C. (IPR032095)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "AASS" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'AASS' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **AASS** (gene ID: AASS, UniProt: Q9UDR5) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Human AASS (UniProt Q9UDR5): Functional-Annotation Research Report

## Executive summary

Human **AASS** encodes mitochondrial **α-aminoadipic semialdehyde synthase**, a bifunctional enzyme that performs the first two committed reactions of the saccharopine pathway of L-lysine degradation. Its N-terminal lysine-2-oxoglutarate reductase domain—also called lysine-ketoglutarate reductase or LOR/LKR—uses NADPH to condense L-lysine with 2-oxoglutarate, producing saccharopine. Its C-terminal saccharopine dehydrogenase domain uses NAD⁺ to oxidize saccharopine to L-2-aminoadipate-6-semialdehyde and glutamate. Thus, AASS controls entry of lysine carbon and nitrogen into a pathway that ultimately produces glutaryl-CoA, acetoacetyl-CoA, and acetyl-CoA. (leandro2022characterizationandstructure pages 1-2, matthews2020reviewoflysine pages 2-4)

The supplied identity is correct and unambiguous: **AASS, Homo sapiens, UniProt Q9UDR5**, is the LKR/SDH bifunctional mitochondrial protein, not AADAT, ALDH7A1, or another similarly named lysine-pathway enzyme. Loss of LKR or of the whole enzyme causes hyperlysinemia type I, generally a benign biochemical phenotype. Selective SDH impairment permits continued saccharopine formation but prevents its clearance, producing hyperlysinemia type II/saccharopinuria; animal evidence indicates that saccharopine—not lysine alone—is toxic to mitochondria and developing neurons. (kopec2017humanalphaaminoadipicsemialdehyde pages 1-4, houten2013geneticbasisof pages 1-2, guo2022themetabolitesaccharopine pages 1-3)

## 1. Mandatory identity verification

The original human gene-cloning study identified a single 2,781-bp open reading frame encoding a predicted 927-residue bifunctional protein, with an N-terminal region homologous to yeast LYS1 and a C-terminal region homologous to yeast LYS9. The gene comprised 24 exons over approximately 68 kb at chromosome 7q31.3. Current reviewed annotations describe a 926-residue precursor of approximately 102.1 kDa, reflecting subsequent sequence annotation rather than a different protein. (sacksteder2000identificationofthe pages 1-2, sacksteder2000identificationofthe pages 5-7, matthews2020reviewoflysine pages 2-4)

The UniProt cross-reference is explicitly **Q9UDR5**, gene **AASS**, human Gene ID 10157. The enzyme carries EC activities **1.5.1.8** and **1.5.1.9**, corresponding to LKR/LOR and SDH, respectively. No evidence encountered indicated symbol ambiguity for the human target. (kopec2017humanalphaaminoadipicsemialdehyde pages 1-4)

The literature-defined architecture also agrees with the supplied InterPro assignments. The N-terminal LOR region contains the NADPH-binding/reductase machinery, whereas the C-terminal region belongs to the saccharopine-dehydrogenase family and includes an NAD(H)-binding fold. Functional domain boundaries have been assigned approximately to residues 33–455 and 455–926; recombinant studies used residues 23–452 for LKR, 455–926 for SDH, and 23–926 for near-full-length AASS. (kopec2017humanalphaaminoadipicsemialdehyde pages 1-4, matthews2020reviewoflysine pages 2-4)

| Feature | Evidence-based annotation | Key quantitative or experimental support | Interpretation/strength |
|---|---|---|---|
| Identity/domain architecture | Human **AASS**, UniProt **Q9UDR5**, is a bifunctional lysine-catabolic enzyme with an N-terminal lysine-2-oxoglutarate reductase region and a C-terminal saccharopine dehydrogenase region. | The precursor has 926 amino acids and an approximately 102.1-kDa monomeric mass. Functional regions are assigned approximately to residues 33–455 and 455–926. The human LOR structure is PDB 8E8U. (kopec2017humanalphaaminoadipicsemialdehyde pages 1-4, leandro2022characterizationandstructure pages 5-6, leandro2022characterizationandstructure pages 1-2, matthews2020reviewoflysine pages 2-4) | **High:** concordant gene-cloning, biochemical, database-linked review, and structural evidence. |
| LOR reaction and cofactor | LOR catalyzes L-lysine + 2-oxoglutarate + NADPH to form saccharopine + NADP⁺ + H₂O, EC 1.5.1.8. | Human LOR preferentially uses NADPH; Ser266 and Arg267 accommodate its 2′-phosphate. The active structural construct formed a tetramer, and activity was measured by NADPH oxidation. (leandro2022characterizationandstructure pages 5-6, leandro2022characterizationandstructure pages 1-2, houten2013geneticbasisof pages 4-5) | **High for reaction and cofactor; moderate for rate control:** supported by direct enzymology and structure, although physiological rate limitation is context-dependent. |
| SDH reaction, cofactor, and kinetics | SDH oxidizes saccharopine with NAD⁺ to L-2-aminoadipate-6-semialdehyde, glutamate, NADH, and H⁺, EC 1.5.1.9. | Recombinant human SDH had apparent Kₘ values of **0.1 mM for NAD⁺** and **1.3 mM for saccharopine** and preferred NAD⁺ over NADP⁺. Apo and NAD⁺-bound structures were solved at 1.9 and 2.7 Å. (kopec2017humanalphaaminoadipicsemialdehyde pages 1-4) | **High:** direct recombinant-enzyme kinetics and structural evidence; kinetic values remain assay-dependent. |
| Localization and tissue distribution | AASS performs the first two reactions of the mitochondrial saccharopine pathway. Human expression is broad but highest in liver, with relatively high expression in heart and kidney. | Mitochondrially targeted human AASS or SDH rescued mitochondrial abnormalities in *C. elegans* mutants. Human Northern blots detected transcripts in all tissues examined, with the highest level in liver. (zhou2019thelysinecatabolite pages 9-11, zhou2019thelysinecatabolite pages 6-8, sacksteder2000identificationofthe pages 5-7, matthews2020reviewoflysine pages 2-4) | **High for mitochondrial pathway assignment and liver enrichment; moderate for detailed cell-type distribution.** |
| Hyperlysinemia type I | Biallelic loss affecting LOR alone or both activities causes autosomal-recessive hyperlysinemia type I, usually a benign or minimally symptomatic biochemical phenotype dominated by elevated lysine. | Plasma lysine commonly exceeds **600 μmol/L** and can reach **2,000 μmol/L**, versus an adult reference range of 111–248 μmol/L. An eight-patient series identified four missense variants, two deletions, and one duplication. A 2023 newborn-screened child with p.R146W and p.T371I was developing normally at 11 months without treatment. Estimated frequency is **1 in 300,000–500,000 newborns**. (houten2013geneticbasisof pages 1-2, yeganeh2023acaseof pages 1-2) | **Moderate to high:** human genetic and relatively unbiased screening evidence supports benignity, but cohorts and longitudinal data are limited. |
| Hyperlysinemia type II and saccharopinuria | Selective SDH impairment with retained LOR flux causes lysine and saccharopine accumulation. Models implicate saccharopine, rather than lysine alone, in mitochondrial and neuronal toxicity. | SDH-mutant mice accumulated cerebral lysine and saccharopine and developed smaller brains and thinner cortices; LOR-R65Q mice had elevated lysine but normal brain development. Saccharopine disrupted mitochondrial dynamics and inhibited the neurotrophic function of glucose-6-phosphate isomerase. (zhou2019thelysinecatabolite pages 6-8, guo2022themetabolitesaccharopine pages 1-3) | **Strong mechanistic animal evidence but limited human certainty:** type II cases are exceptionally rare, precluding precise genotype–phenotype estimates. |
| Therapeutic targeting | Selective LOR inhibition is under preclinical investigation as substrate-reduction therapy for PDE-ALDH7A1 and glutaric aciduria type 1. SDH inhibition is undesirable because it could increase saccharopine. | Structural and assay platforms exist for human LOR and SDH. The generally benign type I phenotype provides partial human safety validation for lowering LOR activity. No relevant AASS-targeted clinical trial was identified. (kopec2017humanalphaaminoadipicsemialdehyde pages 1-4, leandro2022characterizationandstructure pages 1-2, yeganeh2023acaseof pages 1-2) | **Preclinical and emerging:** biologically compelling and structurally tractable, but domain selectivity and long-term safety remain unresolved. |


*Table: Compact functional and translational evidence map for human AASS/Q9UDR5, integrating enzymology, localization, genetics, disease mechanisms, and therapeutic status.*

## 2. Primary biochemical function and substrate specificity

### 2.1 LKR/LOR reaction

The first domain catalyzes the reductive condensation:

**L-lysine + 2-oxoglutarate + NADPH + H⁺ → L-saccharopine + NADP⁺ + H₂O**.

This is EC 1.5.1.8 and is the first committed step of the saccharopine pathway. The physiological amino-acid substrate is L-lysine, the carbonyl cosubstrate is 2-oxoglutarate/α-ketoglutarate, and the preferred reducing cofactor is NADPH. Human LOR’s NADPH preference differs from the NADH-dependent homolog in yeast; structural analysis places Ser266 and Arg267 where they can accommodate and electrostatically stabilize the additional 2′-phosphate of NADPH. (leandro2022characterizationandstructure pages 5-6, leandro2022characterizationandstructure pages 1-2)

The 2022 human LOR study solved an active long-domain structure, PDB **8E8U**, and found a tetrameric assembly. Gel filtration gave an apparent mass of approximately 150–200 kDa for isolated constructs, while structural-interface analysis supported higher-order association; earlier purification of full-length mammalian AASS gave an approximately 115-kDa subunit and approximately 467-kDa native tetramer. These data support oligomerization as functionally relevant, although isolated-domain and full-length quaternary states should not be assumed identical under every condition. (leandro2022characterizationandstructure pages 5-6, matthews2020reviewoflysine pages 2-4)

### 2.2 SDH reaction

The second domain catalyzes:

**L-saccharopine + NAD⁺ + H₂O → L-2-aminoadipate-6-semialdehyde + L-glutamate + NADH + H⁺**.

This is EC 1.5.1.9. Human SDH strongly favors NAD⁺ over NADP⁺; Asp512 and Met513 were implicated in excluding the 2′-phosphate of NADP⁺. Recombinant human SDH showed apparent **Kₘ values of 0.1 mM for NAD⁺ and 1.3 mM for saccharopine**. Apo and NAD⁺-bound structures were determined at **1.9 Å and 2.7 Å**, respectively. These values establish cofactor and substrate recognition directly, while remaining assay-condition-dependent rather than universal cellular constants. (kopec2017humanalphaaminoadipicsemialdehyde pages 1-4)

The fusion of both catalytic activities may facilitate coordinated expression and potentially substrate channeling, but direct proof that AASA is obligatorily channeled between active sites remains limited. The strongest conclusion is that one polypeptide sequentially carries out both reactions. (sacksteder2000identificationofthe pages 1-2, sacksteder2000identificationofthe pages 5-7)

## 3. Cellular localization and physiological distribution

AASS is a **mitochondrial** enzyme, and the first two saccharopine-pathway reactions occur in mitochondria. Functional evidence is particularly strong: mitochondrially targeted human full-length AASS or human SDH rescued mitochondrial abnormalities in *C. elegans* SDH-domain mutants, whereas the LKR domain alone did not rescue the saccharopine-clearance defect. (zhou2019thelysinecatabolite pages 9-11, zhou2019thelysinecatabolite pages 6-8)

Expression is broad but enriched in organs responsible for amino-acid oxidation. Northern blotting detected AASS transcripts in every human tissue examined, with highest expression in liver, relatively high expression in heart and kidney, and lower detectable expression elsewhere. The liver is regarded as the principal organ of mammalian lysine catabolism. (sacksteder2000identificationofthe pages 5-7, matthews2020reviewoflysine pages 2-4)

Brain pathway usage is more nuanced. Older work assigned greater importance to the pipecolate route in adult brain, but newer tracing and genetic studies support substantial saccharopine-pathway activity in mammalian brain, particularly during development and under metabolic challenge. AASS protein is present in neuronal and glial preparations in mice, although expression and pathway balance vary with developmental stage and species. Therefore, “mitochondrial lysine degradation enzyme with liver enrichment and biologically meaningful brain activity” is more accurate than describing AASS as liver-exclusive or universally dominant in every adult brain cell. (valderrama2025lysineαketoglutaratereductase pages 2-3, guo2022themetabolitesaccharopine pages 1-3)

## 4. Pathway context

After AASS produces AASA, **ALDH7A1/antiquitin** oxidizes it to 2-aminoadipate. AADAT then forms 2-oxoadipate, DHTKD1-dependent oxidative decarboxylation generates glutaryl-CoA, and GCDH continues the pathway toward crotonyl-CoA, acetoacetyl-CoA, and acetyl-CoA. AASS therefore lies upstream of several clinically important lysine-catabolism disorders, including pyridoxine-dependent epilepsy due to ALDH7A1 deficiency and glutaric aciduria type I due to GCDH deficiency. (houten2013geneticbasisof pages 1-2, matthews2020reviewoflysine pages 2-4)

AASA equilibrates with the cyclic compound Δ¹-piperideine-6-carboxylate, or P6C. In ALDH7A1 deficiency, AASA/P6C accumulates; P6C reacts with pyridoxal-5′-phosphate, helping explain pyridoxine-responsive seizures. AASS does not itself act as a signaling protein, but its control of upstream metabolic flux changes concentrations of lysine, saccharopine, AASA/P6C, glutamate, and downstream organic acids, thereby indirectly affecting mitochondrial physiology and neuronal function. (valderrama2025lysineαketoglutaratereductase pages 3-5, kopec2017humanalphaaminoadipicsemialdehyde pages 1-4)

## 5. Human genetic and clinical evidence

### Hyperlysinemia type I

Biallelic AASS variants affecting LKR alone or destabilizing the full enzyme cause autosomal-recessive hyperlysinemia type I. Plasma lysine generally exceeds **600 μmol/L** and may reach **2,000 μmol/L**, compared with an adult reference interval of **111–248 μmol/L**. Alternative lysine products, including homoarginine, acetyl-lysines, and pipecolate, may also increase. (houten2013geneticbasisof pages 1-2)

The founding patient carried a homozygous frameshifting 9-bp deletion producing a stop at residue 534. Fibroblasts retained only approximately **10% of normal LKR** and **3.5% of normal SDH** activity, with markedly reduced AASS RNA. (sacksteder2000identificationofthe pages 5-7)

A 2013 cohort of eight patients identified four missense variants, two deletions, and one duplication. Importantly, severe neurological findings in two patients were associated with a contiguous deletion involving both **AASS and PTPRZ1**, supporting the expert interpretation that isolated hyperlysinemia should not automatically be assigned causality for neurological disease. (houten2013geneticbasisof pages 1-2)

The most informative recent clinical report was published in October 2023. A newborn-screened child carried two novel LOR-domain variants, p.R146W and p.T371I, predicted to disrupt domain folding. At 11 months, growth, development, and examination were normal without therapy. Newborn-screening data place hyperlysinemia’s estimated frequency at approximately **1 in 300,000–500,000 births**. This relatively unbiased observation strengthens the view that type I is usually a benign biochemical phenotype, although available cohorts remain too small to exclude uncommon complications. [Yeganeh et al., 2023, DOI URL: https://doi.org/10.1002/jmd2.12399] (yeganeh2023acaseof pages 1-2)

### Hyperlysinemia type II/saccharopinuria

If SDH is selectively impaired while LKR continues to operate, both lysine and saccharopine accumulate. This is termed hyperlysinemia type II or saccharopinuria. Human cases are exceptionally rare, so the exact penetrance and phenotypic spectrum remain uncertain. (houten2013geneticbasisof pages 1-2, yeganeh2023acaseof pages 1-2)

Mechanistic evidence nevertheless distinguishes type II sharply from type I. Mice carrying the LKR-domain R65Q substitution accumulated cerebral lysine but developed normally. SDH-domain G489E mice accumulated both lysine and saccharopine and had smaller brains, reduced cortical thickness, and defective neuronal development. Saccharopine inhibited the neurotrophic function of glucose-6-phosphate isomerase, and extracellular GPI supplementation rescued neuronal defects in experimental systems. [Guo et al., published 30 March 2022, DOI URL: https://doi.org/10.1523/JNEUROSCI.1459-21.2022] (guo2022themetabolitesaccharopine pages 1-3)

Earlier *C. elegans* and mouse work also showed that SDH failure causes mitochondrial enlargement, disrupted fission/tubulation, ATP loss, liver injury, growth retardation, and premature death. Blocking LKR upstream prevented saccharopine formation and rescued mitochondrial morphology and bioenergetics. This supports classification of saccharopinuria as a mitochondrial-metabolite toxicity disorder, while the degree to which model severity predicts individual human outcomes remains unresolved. [Zhou et al., online 20 December 2018/volume year 2019, DOI URL: https://doi.org/10.1083/jcb.201807204] (zhou2019thelysinecatabolite pages 1-2, zhou2019thelysinecatabolite pages 6-8)

## 6. Current applications and translational development

### Diagnostic use

AASS deficiency is diagnosed by plasma/urine amino-acid analysis followed by molecular testing. Marked lysine elevation suggests type I; saccharopine measurement is crucial for recognizing an SDH-selective/type II defect. The 2023 case illustrates that high urinary lysine may initially resemble a cystinuria-like aminoaciduria profile. Because moderate lysine elevation below 600 μmol/L can occur secondarily in other metabolic disorders, biochemical results require pathway-aware interpretation rather than automatic assignment to AASS deficiency. (houten2013geneticbasisof pages 1-2, yeganeh2023acaseof pages 1-2)

### AASS as a substrate-reduction target

AASS inhibition is being developed conceptually as **substrate-reduction therapy** for diseases downstream of AASS:

* In **PDE-ALDH7A1**, reducing LKR flux should lower production of AASA and P6C, complementing pyridoxine and dietary lysine reduction.
* In **glutaric aciduria type I**, reducing entry of lysine into the saccharopine pathway should lower glutaryl-CoA, glutarate, and 3-hydroxyglutarate formation.

The therapeutic logic is strengthened by human type I hyperlysinemia, in which profound reduction of AASS/LKR activity is generally tolerated. Structural determination of the human LOR domain and development of recombinant assays provide practical platforms for inhibitor discovery. [Leandro et al., received 7 June and accepted 30 August 2022, DOI URL: https://doi.org/10.1098/rsob.220179] (leandro2022characterizationandstructure pages 1-2, yeganeh2023acaseof pages 1-2)

Domain selectivity is essential. **LKR inhibition** prevents formation of saccharopine and downstream toxic metabolites; **SDH inhibition** would instead increase saccharopine and may damage mitochondria. AASS-directed therapy is therefore not equivalent to nonspecific inhibition of the whole protein’s two activities. (zhou2019thelysinecatabolite pages 9-11, valderrama2025lysineαketoglutaratereductase pages 5-6)

No relevant registered human trial of an AASS inhibitor was identified in the searches conducted for this report. Accordingly, AASS-directed pharmacology should be described as preclinical rather than a current clinical implementation. Existing real-world management remains disease-specific—for example, pyridoxine with lysine reduction for PDE-ALDH7A1, and lysine-restricted/arginine-enriched diet, carnitine, and emergency protocols for GA1—not direct AASS inhibition. (valderrama2025lysineαketoglutaratereductase pages 5-6, latzer2024inheritedmetabolicepilepsiesestablished pages 9-10)

## 7. Recent developments, 2023–2024

Direct AASS-focused literature in 2023–2024 was limited. The principal 2023 advance was the newborn-screened p.R146W/p.T371I case, which provided relatively unbiased human evidence that LOR-domain deficiency can be clinically silent and helped de-risk selective LOR inhibition. (yeganeh2023acaseof pages 1-2)

A 2023 review of mitochondrial NAD kinase biology also reinforced the biochemical dependence of LKR on mitochondrial NADPH, placing AASS within broader mitochondrial redox metabolism. However, this does not supersede direct AASS enzymology and should be considered contextual rather than primary functional evidence.

The 2024 inherited-metabolic-epilepsy literature continued to support lysine restriction and pyridoxal/pyridoxine-directed management in ALDH7A1 disease, while substrate reduction remained an emerging strategy. No 2024 study retrieved in this search established an approved AASS drug, a validated clinical biomarker beyond conventional metabolite/genetic testing, or a human interventional efficacy signal. Thus, recent progress has principally involved clinical natural-history clarification and therapeutic rationale, not clinical translation. (latzer2024inheritedmetabolicepilepsiesestablished pages 9-10, yeganeh2023acaseof pages 1-2)

## 8. Expert interpretation and evidence limitations

The most defensible functional annotation is that AASS is the mitochondrial, bifunctional gatekeeper of saccharopine-mediated lysine degradation. Evidence for reaction identity, domain organization, cofactor preference, and liver enrichment is strong and includes purified human enzyme, crystallography, patient fibroblasts, molecular genetics, and functional rescue experiments. (kopec2017humanalphaaminoadipicsemialdehyde pages 1-4, leandro2022characterizationandstructure pages 5-6, sacksteder2000identificationofthe pages 1-2)

Three cautions are important:

1. **Type I and type II should not be conflated.** Lysine accumulation alone is generally tolerated, whereas saccharopine accumulation is mechanistically toxic in models.
2. **Neurological findings in a hyperlysinemic patient are not automatically caused by AASS.** Contiguous deletions, prenatal exposures, or independent diagnoses must be considered.
3. **Therapeutic inhibition must target LKR safely and selectively.** Long-term human data are sparse, especially for infancy, pregnancy, brain development, and partial pharmacological inhibition across tissues.

OpenTargets associates AASS most strongly with hyperlysinemia among the retrieved disease links, with additional evidence for saccharopinuria; broader neurodegenerative associations are substantially less specific and should not be interpreted as proof that AASS causes common neurodegenerative disease. (OpenTargets Search: -AASS)

## Conclusion

AASS/Q9UDR5 is conclusively the human mitochondrial α-aminoadipic semialdehyde synthase specified in the query. It is a two-domain enzyme whose NADPH-dependent LKR activity converts L-lysine and 2-oxoglutarate to saccharopine and whose NAD⁺-dependent SDH activity converts saccharopine to AASA and glutamate. Its principal physiological role is control of mitochondrial lysine-catabolic flux, especially in liver but also in kidney, heart, and brain. Human genetics indicates that loss of pathway entry is usually well tolerated, while model studies show that failure to clear saccharopine is harmful. This asymmetry makes the LKR domain a compelling but still preclinical substrate-reduction target for PDE-ALDH7A1 and GA1.

References

1. (leandro2022characterizationandstructure pages 1-2): João Leandro, Susmita Khamrui, Chalada Suebsuwong, Peng-Jen Chen, Cody Secor, Tetyana Dodatko, Chunli Yu, Roberto Sanchez, Robert J. DeVita, Sander M. Houten, and Michael B. Lazarus. Characterization and structure of the human lysine-2-oxoglutarate reductase domain, a novel therapeutic target for treatment of glutaric aciduria type 1. Open Biology, May 2022. URL: https://doi.org/10.1098/rsob.220179, doi:10.1098/rsob.220179. This article has 15 citations and is from a peer-reviewed journal.

2. (matthews2020reviewoflysine pages 2-4): Dwight E Matthews. Review of lysine metabolism with a focus on humans. The Journal of nutrition, 150 Supplement_1:2548S-2555S, Oct 2020. URL: https://doi.org/10.1093/jn/nxaa224, doi:10.1093/jn/nxaa224. This article has 222 citations.

3. (kopec2017humanalphaaminoadipicsemialdehyde pages 1-4): J Kopec, E Rembeza, and M McLaughlin. Human alpha-aminoadipic semialdehyde synthase (aass). Unknown journal, 2017.

4. (houten2013geneticbasisof pages 1-2): Sander M Houten, Heleen te Brinke, Simone Denis, Jos PN Ruiter, Alida C Knegt, Johannis BC de Klerk, Persephone Augoustides-Savvopoulou, Johannes Häberle, Matthias R Baumgartner, Turgay Coşkun, Johannes Zschocke, Jörn Oliver Sass, Bwee Tien Poll-The, Ronald JA Wanders, and Marinus Duran. Genetic basis of hyperlysinemia. Orphanet Journal of Rare Diseases, 8:57-57, Apr 2013. URL: https://doi.org/10.1186/1750-1172-8-57, doi:10.1186/1750-1172-8-57. This article has 70 citations and is from a peer-reviewed journal.

5. (guo2022themetabolitesaccharopine pages 1-3): Ye Guo, Junjie Wu, Min Wang, Xin Wang, Youli Jian, Chonglin Yang, and Weixiang Guo. The metabolite saccharopine impairs neuronal development by inhibiting the neurotrophic function of glucose-6-phosphate isomerase. The Journal of Neuroscience, 42:2631-2646, Feb 2022. URL: https://doi.org/10.1523/jneurosci.1459-21.2022, doi:10.1523/jneurosci.1459-21.2022. This article has 35 citations.

6. (sacksteder2000identificationofthe pages 1-2): Katherine A. Sacksteder, Barbara J. Biery, James C. Morrell, Barbara K. Goodman, Brian V. Geisbrecht, Rody P. Cox, Stephen J. Gould, and Michael T. Geraghty. Identification of the alpha-aminoadipic semialdehyde synthase gene, which is defective in familial hyperlysinemia. American journal of human genetics, 66 6:1736-43, Jun 2000. URL: https://doi.org/10.1086/302919, doi:10.1086/302919. This article has 143 citations and is from a highest quality peer-reviewed journal.

7. (sacksteder2000identificationofthe pages 5-7): Katherine A. Sacksteder, Barbara J. Biery, James C. Morrell, Barbara K. Goodman, Brian V. Geisbrecht, Rody P. Cox, Stephen J. Gould, and Michael T. Geraghty. Identification of the alpha-aminoadipic semialdehyde synthase gene, which is defective in familial hyperlysinemia. American journal of human genetics, 66 6:1736-43, Jun 2000. URL: https://doi.org/10.1086/302919, doi:10.1086/302919. This article has 143 citations and is from a highest quality peer-reviewed journal.

8. (leandro2022characterizationandstructure pages 5-6): João Leandro, Susmita Khamrui, Chalada Suebsuwong, Peng-Jen Chen, Cody Secor, Tetyana Dodatko, Chunli Yu, Roberto Sanchez, Robert J. DeVita, Sander M. Houten, and Michael B. Lazarus. Characterization and structure of the human lysine-2-oxoglutarate reductase domain, a novel therapeutic target for treatment of glutaric aciduria type 1. Open Biology, May 2022. URL: https://doi.org/10.1098/rsob.220179, doi:10.1098/rsob.220179. This article has 15 citations and is from a peer-reviewed journal.

9. (houten2013geneticbasisof pages 4-5): Sander M Houten, Heleen te Brinke, Simone Denis, Jos PN Ruiter, Alida C Knegt, Johannis BC de Klerk, Persephone Augoustides-Savvopoulou, Johannes Häberle, Matthias R Baumgartner, Turgay Coşkun, Johannes Zschocke, Jörn Oliver Sass, Bwee Tien Poll-The, Ronald JA Wanders, and Marinus Duran. Genetic basis of hyperlysinemia. Orphanet Journal of Rare Diseases, 8:57-57, Apr 2013. URL: https://doi.org/10.1186/1750-1172-8-57, doi:10.1186/1750-1172-8-57. This article has 70 citations and is from a peer-reviewed journal.

10. (zhou2019thelysinecatabolite pages 9-11): Junxiang Zhou, Xin Wang, Min Wang, Yuwei Chang, Fengxia Zhang, Zhaonan Ban, Ruofeng Tang, Qiwen Gan, Shaohuan Wu, Ye Guo, Qian Zhang, Fengyang Wang, Liyuan Zhao, Yudong Jing, Wenfeng Qian, Guodong Wang, Weixiang Guo, and Chonglin Yang. The lysine catabolite saccharopine impairs development by disrupting mitochondrial homeostasis. The Journal of Cell Biology, 218:580-597, Dec 2019. URL: https://doi.org/10.1083/jcb.201807204, doi:10.1083/jcb.201807204. This article has 94 citations.

11. (zhou2019thelysinecatabolite pages 6-8): Junxiang Zhou, Xin Wang, Min Wang, Yuwei Chang, Fengxia Zhang, Zhaonan Ban, Ruofeng Tang, Qiwen Gan, Shaohuan Wu, Ye Guo, Qian Zhang, Fengyang Wang, Liyuan Zhao, Yudong Jing, Wenfeng Qian, Guodong Wang, Weixiang Guo, and Chonglin Yang. The lysine catabolite saccharopine impairs development by disrupting mitochondrial homeostasis. The Journal of Cell Biology, 218:580-597, Dec 2019. URL: https://doi.org/10.1083/jcb.201807204, doi:10.1083/jcb.201807204. This article has 94 citations.

12. (yeganeh2023acaseof pages 1-2): Mehdi Yeganeh, Christiane Auray‐Blais, Bruno Maranda, Amanda Sabovic, Robert J. DeVita, Michael B. Lazarus, and Sander M. Houten. A case of hyperlysinemia identified by urine newborn screening. JIMD Reports, 64:440-445, Oct 2023. URL: https://doi.org/10.1002/jmd2.12399, doi:10.1002/jmd2.12399. This article has 8 citations and is from a peer-reviewed journal.

13. (valderrama2025lysineαketoglutaratereductase pages 2-3): Gabriel Vieira Valderrama, Gabriela Alves Moreira, and Paulo Arruda. Lysine α-ketoglutarate reductase as a therapeutic target for saccharopine pathway related diseases. Frontiers in Molecular Neuroscience, Oct 2025. URL: https://doi.org/10.3389/fnmol.2025.1695490, doi:10.3389/fnmol.2025.1695490. This article has 1 citations.

14. (valderrama2025lysineαketoglutaratereductase pages 3-5): Gabriel Vieira Valderrama, Gabriela Alves Moreira, and Paulo Arruda. Lysine α-ketoglutarate reductase as a therapeutic target for saccharopine pathway related diseases. Frontiers in Molecular Neuroscience, Oct 2025. URL: https://doi.org/10.3389/fnmol.2025.1695490, doi:10.3389/fnmol.2025.1695490. This article has 1 citations.

15. (zhou2019thelysinecatabolite pages 1-2): Junxiang Zhou, Xin Wang, Min Wang, Yuwei Chang, Fengxia Zhang, Zhaonan Ban, Ruofeng Tang, Qiwen Gan, Shaohuan Wu, Ye Guo, Qian Zhang, Fengyang Wang, Liyuan Zhao, Yudong Jing, Wenfeng Qian, Guodong Wang, Weixiang Guo, and Chonglin Yang. The lysine catabolite saccharopine impairs development by disrupting mitochondrial homeostasis. The Journal of Cell Biology, 218:580-597, Dec 2019. URL: https://doi.org/10.1083/jcb.201807204, doi:10.1083/jcb.201807204. This article has 94 citations.

16. (valderrama2025lysineαketoglutaratereductase pages 5-6): Gabriel Vieira Valderrama, Gabriela Alves Moreira, and Paulo Arruda. Lysine α-ketoglutarate reductase as a therapeutic target for saccharopine pathway related diseases. Frontiers in Molecular Neuroscience, Oct 2025. URL: https://doi.org/10.3389/fnmol.2025.1695490, doi:10.3389/fnmol.2025.1695490. This article has 1 citations.

17. (latzer2024inheritedmetabolicepilepsiesestablished pages 9-10): Itay Tokatly Latzer and Phillip L. Pearl. Inherited metabolic epilepsies-established diseases, new approaches. Epilepsia open, Dec 2024. URL: https://doi.org/10.1002/epi4.13121, doi:10.1002/epi4.13121. This article has 4 citations and is from a peer-reviewed journal.

18. (OpenTargets Search: -AASS): Open Targets Query (-AASS, 5 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

## Artifacts

- [Edison artifact artifact-00](AASS-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. kopec2017humanalphaaminoadipicsemialdehyde pages 1-4
2. houten2013geneticbasisof pages 1-2
3. sacksteder2000identificationofthe pages 5-7
4. yeganeh2023acaseof pages 1-2
5. guo2022themetabolitesaccharopine pages 1-3
6. leandro2022characterizationandstructure pages 1-2
7. matthews2020reviewoflysine pages 2-4
8. sacksteder2000identificationofthe pages 1-2
9. leandro2022characterizationandstructure pages 5-6
10. houten2013geneticbasisof pages 4-5
11. zhou2019thelysinecatabolite pages 9-11
12. zhou2019thelysinecatabolite pages 6-8
13. zhou2019thelysinecatabolite pages 1-2
14. latzer2024inheritedmetabolicepilepsiesestablished pages 9-10
15. Yeganeh et al., 2023, DOI URL: https://doi.org/10.1002/jmd2.12399
16. Guo et al., published 30 March 2022, DOI URL: https://doi.org/10.1523/JNEUROSCI.1459-21.2022
17. Zhou et al., online 20 December 2018/volume year 2019, DOI URL: https://doi.org/10.1083/jcb.201807204
18. Leandro et al., received 7 June and accepted 30 August 2022, DOI URL: https://doi.org/10.1098/rsob.220179
19. https://doi.org/10.1002/jmd2.12399]
20. https://doi.org/10.1523/JNEUROSCI.1459-21.2022]
21. https://doi.org/10.1083/jcb.201807204]
22. https://doi.org/10.1098/rsob.220179]
23. https://doi.org/10.1098/rsob.220179,
24. https://doi.org/10.1093/jn/nxaa224,
25. https://doi.org/10.1186/1750-1172-8-57,
26. https://doi.org/10.1523/jneurosci.1459-21.2022,
27. https://doi.org/10.1086/302919,
28. https://doi.org/10.1083/jcb.201807204,
29. https://doi.org/10.1002/jmd2.12399,
30. https://doi.org/10.3389/fnmol.2025.1695490,
31. https://doi.org/10.1002/epi4.13121,