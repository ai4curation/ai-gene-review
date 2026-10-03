---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-26T22:20:47.890078'
end_time: '2026-09-26T22:30:07.537333'
duration_seconds: 559.65
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: ARATH
  gene_id: ZDS
  gene_symbol: ZDS1
  uniprot_accession: Q38893
  protein_description: 'RecName: Full=Zeta-carotene desaturase, chloroplastic/chromoplastic
    {ECO:0000305}; EC=1.3.5.6 {ECO:0000269|PubMed:9914519}; AltName: Full=9,9''-di-cis-zeta-carotene
    desaturase {ECO:0000305}; AltName: Full=Carotene 7,8-desaturase {ECO:0000305};
    AltName: Full=Protein CHLOROPLAST BIOGENESIS 5 {ECO:0000303|PubMed:24907342};
    AltName: Full=Protein PIGMENT DEFECTIVE 181 {ECO:0000305}; AltName: Full=Protein
    SPONTANEOUS CELL DEATH 1 {ECO:0000303|PubMed:17468780}; Flags: Precursor;'
  gene_info: Name=ZDS1 {ECO:0000305}; Synonyms=CLB5 {ECO:0000303|PubMed:24907342},
    PDE181 {ECO:0000305}, SPC1 {ECO:0000303|PubMed:17468780}, ZDS {ECO:0000303|Ref.1};
    OrderedLocusNames=At3g04870 {ECO:0000312|Araport:AT3G04870}; ORFNames=T9J14.18
    {ECO:0000312|EMBL:AAG51402.1};
  organism_full: Arabidopsis thaliana (Mouse-ear cress).
  protein_family: Belongs to the zeta carotene desaturase family.
  protein_domains: Amino_oxidase. (IPR002937); FAD/NAD-bd_sf. (IPR036188); Zeta_caro_desat.
    (IPR014103); Zeta_carotene_desat/Oxidored. (IPR050464); Amino_oxidase (PF01593)
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
  path: ZDS-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q38893
- **Protein Description:** RecName: Full=Zeta-carotene desaturase, chloroplastic/chromoplastic {ECO:0000305}; EC=1.3.5.6 {ECO:0000269|PubMed:9914519}; AltName: Full=9,9'-di-cis-zeta-carotene desaturase {ECO:0000305}; AltName: Full=Carotene 7,8-desaturase {ECO:0000305}; AltName: Full=Protein CHLOROPLAST BIOGENESIS 5 {ECO:0000303|PubMed:24907342}; AltName: Full=Protein PIGMENT DEFECTIVE 181 {ECO:0000305}; AltName: Full=Protein SPONTANEOUS CELL DEATH 1 {ECO:0000303|PubMed:17468780}; Flags: Precursor;
- **Gene Information:** Name=ZDS1 {ECO:0000305}; Synonyms=CLB5 {ECO:0000303|PubMed:24907342}, PDE181 {ECO:0000305}, SPC1 {ECO:0000303|PubMed:17468780}, ZDS {ECO:0000303|Ref.1}; OrderedLocusNames=At3g04870 {ECO:0000312|Araport:AT3G04870}; ORFNames=T9J14.18 {ECO:0000312|EMBL:AAG51402.1};
- **Organism (full):** Arabidopsis thaliana (Mouse-ear cress).
- **Protein Family:** Belongs to the zeta carotene desaturase family.
- **Key Domains:** Amino_oxidase. (IPR002937); FAD/NAD-bd_sf. (IPR036188); Zeta_caro_desat. (IPR014103); Zeta_carotene_desat/Oxidored. (IPR050464); Amino_oxidase (PF01593)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ZDS1" matches the protein description above**
2. **Verify the organism is correct:** Arabidopsis thaliana (Mouse-ear cress).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ZDS1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ZDS1** (gene ID: ZDS, UniProt: Q38893) in ARATH.

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
- **UniProt Accession:** Q38893
- **Protein Description:** RecName: Full=Zeta-carotene desaturase, chloroplastic/chromoplastic {ECO:0000305}; EC=1.3.5.6 {ECO:0000269|PubMed:9914519}; AltName: Full=9,9'-di-cis-zeta-carotene desaturase {ECO:0000305}; AltName: Full=Carotene 7,8-desaturase {ECO:0000305}; AltName: Full=Protein CHLOROPLAST BIOGENESIS 5 {ECO:0000303|PubMed:24907342}; AltName: Full=Protein PIGMENT DEFECTIVE 181 {ECO:0000305}; AltName: Full=Protein SPONTANEOUS CELL DEATH 1 {ECO:0000303|PubMed:17468780}; Flags: Precursor;
- **Gene Information:** Name=ZDS1 {ECO:0000305}; Synonyms=CLB5 {ECO:0000303|PubMed:24907342}, PDE181 {ECO:0000305}, SPC1 {ECO:0000303|PubMed:17468780}, ZDS {ECO:0000303|Ref.1}; OrderedLocusNames=At3g04870 {ECO:0000312|Araport:AT3G04870}; ORFNames=T9J14.18 {ECO:0000312|EMBL:AAG51402.1};
- **Organism (full):** Arabidopsis thaliana (Mouse-ear cress).
- **Protein Family:** Belongs to the zeta carotene desaturase family.
- **Key Domains:** Amino_oxidase. (IPR002937); FAD/NAD-bd_sf. (IPR036188); Zeta_caro_desat. (IPR014103); Zeta_carotene_desat/Oxidored. (IPR050464); Amino_oxidase (PF01593)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ZDS1" matches the protein description above**
2. **Verify the organism is correct:** Arabidopsis thaliana (Mouse-ear cress).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ZDS1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ZDS1** (gene ID: ZDS, UniProt: Q38893) in ARATH.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: Arabidopsis ZDS1/ZDS (At3g04870; UniProt Q38893)

## Executive summary

The requested protein is correctly identified as the *Arabidopsis thaliana* ζ-carotene desaturase encoded by **At3g04870**, corresponding to **UniProt Q38893**. In Arabidopsis literature the same locus is called **ZDS/ZDS1, CLB5, SPC1,** and **PDE181**. Mapping, independent mutant alleles, molecular lesions, transgene complementation, and loss of transcript/protein in strong alleles establish this identity. This report does not use results concerning unrelated genes named “ZDS1” in other organisms as evidence for Q38893. (avendanovazquez2014anuncharacterizedapocarotenoidderived pages 2-3, dong2007thearabidopsisspontaneous pages 1-2, avendanovazquez2014anuncharacterizedapocarotenoidderived pages 1-2)

ZDS is a plastid-targeted, FAD-dependent carotene desaturase that performs the second pair of desaturations in the plant poly-*cis* carotenoid pathway. Its accepted reaction is:

**9,15,9′-tri-*cis*-ζ-carotene → 9,9′-di-*cis*-neurosporene → 7,9,9′-tri-*cis*-lycopene (prolycopene)**,

introducing the 7–8 and 7′–8′ double bonds. The enzyme is assigned **EC 1.3.5.6**. Prolycopene is subsequently isomerized to all-*trans*-lycopene, which feeds carotene cyclization and production of photoprotective carotenes, xanthophylls, ABA precursors, and other apocarotenoids. Arabidopsis desaturases expressed heterologously established that higher-plant carotenoid biosynthesis proceeds through this poly-*cis* route. (rosassaavedra2016biosynthesisofcarotenoids pages 11-14, moreno2021plantapocarotenoidsfrom pages 31-33)

The strongest biological conclusion is that AtZDS is indispensable both for **carotenoid metabolic flux** and for normal **chloroplast differentiation, photoprotection, and plastid-to-nucleus signaling**. Strong loss-of-function alleles are albino and seedling-lethal. Importantly, some unusual developmental effects appear to result not merely from carotenoid deficiency but from accumulation of an unidentified upstream cis-carotene-derived signal, commonly designated **ACS1**. Its chemical identity and biosynthetic mechanism remain unresolved. (escobar‐tovar2021deconvolutingapocarotenoid‐mediatedretrograde pages 5-8, moreno2021plantapocarotenoidsfrom pages 13-15, dong2007thearabidopsisspontaneous pages 1-2)

## Evidence-weighted annotation

| Annotation | Best evidence | Confidence / caveat |
|---|---|---|
| **Identity and aliases** | **Direct Arabidopsis evidence:** *Arabidopsis thaliana* locus **At3g04870**, corresponding to UniProt **Q38893**, encodes ζ-carotene desaturase and is the locus independently characterized as **ZDS/ZDS1, CLB5, SPC1, and PDE181**. Three *clb5* alleles mapped to this locus; a wild-type **35S:ZDS** transgene complemented the phenotype, while strong alleles lacked detectable transcript or protein. The *spc1* allelic series independently associated this locus with ζ-carotene desaturase function. (avendanovazquez2014anuncharacterizedapocarotenoidderived pages 2-3, dong2007thearabidopsisspontaneous pages 1-2, avendanovazquez2014anuncharacterizedapocarotenoidderived pages 1-2) | **High.** Genetic mapping, independent alleles, molecular lesions, complementation, and protein/transcript measurements establish identity. “ZDS1” can denote unrelated genes in other organisms; organism and accession must therefore accompany the symbol. |
| **Catalytic function and pathway step** | **Direct/near-direct Arabidopsis evidence:** ZDS performs the second pair of desaturations in the plastid carotenoid pathway, downstream of phytoene desaturase and Z-ISO, converting poly-*cis* ζ-carotene intermediates toward poly-*cis* lycopene (prolycopene), which is subsequently isomerized before carotenoid cyclization. The accepted sequence is **9,15,9′-tri-*cis*-ζ-carotene → 9,9′-di-*cis*-neurosporene → 7,9,9′-tri-*cis*-lycopene**, introducing double bonds at the 7–8 and 7′–8′ positions; EC **1.3.5.6**. Arabidopsis desaturases expressed heterologously in *E. coli* established a poly-*cis* route to prolycopene. (rosassaavedra2016biosynthesisofcarotenoids pages 11-14, moreno2021plantapocarotenoidsfrom pages 31-33) | **High for pathway role; moderate for exact AtZDS stereochemical sequence from the retrieved evidence.** The precise reaction assignment is supported by the 1999 heterologous biochemical study and conserved plant ZDS chemistry, but the available excerpts do not provide purified AtZDS kinetics or numerical substrate-preference measurements. |
| **Cofactors, electron transfer, and domains** | **Plant-family biochemical inference consistent with Q38893:** Plant ZDS proteins are membrane-associated, **FAD-dependent oxidoreductases**. Electrons removed during desaturation are transferred to plastid quinones and ultimately through **plastid terminal oxidase (PTOX)** to oxygen. This agrees with the stated Q38893 **amino-oxidase/FAD–NAD-binding fold**, **Amino_oxidase (PF01593)**, and **ζ-carotene-desaturase-family** annotations. (rosassaavedra2016biosynthesisofcarotenoids pages 11-14) | **Moderate to high.** Family membership and pathway biochemistry strongly support FAD/quinone coupling, but the retrieved literature does not document direct FAD binding, membrane topology, or electron-acceptor assays using purified At3g04870 protein. |
| **Subcellular localization** | **Direct Arabidopsis evidence:** A fusion containing the first **120 amino acids** of AtZDS linked to GFP produced punctate/needle-like fluorescence inside chloroplasts, resembling plastoglobule-associated localization. Its plastid targeting is also consistent with carotenoid biosynthesis and the annotated N-terminal transit peptide/precursor status. (avendanovazquez2014anuncharacterizedapocarotenoidderived pages 2-3) | **High for chloroplast targeting; moderate for the precise intraplastid compartment.** The transit-peptide fusion establishes import into chloroplasts, but resemblance to plastoglobuli is morphological and does not alone prove stable plastoglobule residence or define thylakoid-envelope partitioning of full-length native ZDS. |
| **Loss-of-function phenotypes** | **Direct Arabidopsis evidence:** Weak **spc1-1** plants show leaf bleaching, mosaic spontaneous cell death, superoxide accumulation, reduced downstream carotenoids, and decreased chlorophyll; strong **spc1-2** and null-like **clb5** alleles arrest shortly after germination, are albino/seedling-lethal, and display severe defects in chloroplast differentiation, photoprotection, leaf polarity, and cell expansion. Photosynthesis-associated nuclear transcripts such as **Lhcb1.1, Lhcb1.4, and RbcS** were absent in *spc1-2*. (avendanovazquez2014anuncharacterizedapocarotenoidderived pages 2-3, dong2007thearabidopsisspontaneous pages 1-2, avendanovazquez2014anuncharacterizedapocarotenoidderived pages 1-2) | **High.** Multiple alleles and complementation connect the phenotypes to AtZDS. These broad effects arise both from loss of downstream photoprotective carotenoids and from signaling caused by accumulated upstream intermediates, so not every phenotype reflects the catalytic block alone. |
| **Apocarotenoid retrograde signaling** | **Direct Arabidopsis evidence:** *clb5* accumulates a still-unidentified signal termed **ACS1**, proposed to derive from phytofluene and/or ζ-carotenoids. Relative to *pds3*, *clb5* had **2,193 differentially expressed genes**—**626 induced** and **1,567 repressed**—and **81%** shifted back toward the *pds3* state in *ccd4 clb5*. About **31 of 57** chloroplast 70S ribosomal-protein genes fell by more than **2 log₂-fold**, linking the signal to inhibited plastid translation and GUN1-dependent leaf-development signaling. (escobar‐tovar2021deconvolutingapocarotenoid‐mediatedretrograde pages 5-8, escobar‐tovar2021deconvolutingapocarotenoid‐mediatedretrograde pages 8-10) | **High for existence of a ZDS-block-dependent retrograde-signaling state; low to moderate for ACS1 identity and biosynthetic mechanism.** Reviews note that CCD4 cannot directly cleave relevant *cis*-ζ-carotene isomers under tested conditions, so rescue by *ccd4* may be indirect. The active molecule remains chemically unidentified. (moreno2021plantapocarotenoidsfrom pages 13-15) |
| **Applications and real-world relevance** | **Direct Arabidopsis use:** AtZDS mutants are research tools for dissecting carotenoid metabolism, chloroplast biogenesis, plastid translation, photoprotection, and plastid-to-nucleus signaling. **Comparative tomato evidence—not direct evidence about Q38893 physiology:** Arabidopsis ZDS overexpression bypassed endogenous tomato ZDS co-suppression, identifying ZDS as an engineering bottleneck in fruit carotenogenesis. Tomato ZDS-RNAi fruit accumulated **21.7–78.9 μg g⁻¹ FW ζ-carotene** versus **0.3 μg g⁻¹** in wild type, while lycopene declined to **1.1–2.0 μg g⁻¹** from **105.7 μg g⁻¹** and ABA fell by at least **75%**. (mcquinn2020manipulationofzds pages 5-6) | **High for experimental utility; moderate for crop-engineering translation.** The tomato results demonstrate potential control of fruit color, carotenoid composition, and ABA-linked development, but they concern a different species and do not establish an approved agricultural implementation. Strong AtZDS suppression is generally deleterious because downstream carotenoids are indispensable. |


*Table: Evidence-weighted annotation of Arabidopsis thaliana At3g04870 (UniProt Q38893), separating direct Arabidopsis findings from plant-family inference and comparative tomato data. Confidence notes identify unresolved issues such as the chemical identity and production mechanism of ACS1.*

## 1. Identity verification and nomenclature

The evidence supports the following identity:

- **Organism:** *Arabidopsis thaliana* (mouse-ear cress)
- **Locus:** **At3g04870**
- **UniProt:** **Q38893**
- **Principal gene designation:** **ZDS**, often rendered **ZDS1** in database annotations
- **Experimentally linked aliases/alleles:** **CLB5** (*CHLOROPLAST BIOGENESIS 5*), **SPC1** (*SPONTANEOUS CELL DEATH 1*), and **PDE181** (*PIGMENT DEFECTIVE 181*)
- **Protein:** chloroplastic/chromoplastic ζ-carotene desaturase precursor

The 2014 CLB5 study characterized three lesions: **clb5-1**, a nonsense allele; **clb5-2**, a 28-bp deletion affecting splicing; and **clb5-3**, a conserved Lys-to-Glu substitution. A wild-type **35S:ZDS** construct rescued the mutant phenotype, while clb5-1 and clb5-2 lacked detectable ZDS transcript and protein. These findings provide stronger locus identification than symbol matching alone. (avendanovazquez2014anuncharacterizedapocarotenoidderived pages 2-3)

The independent *spc1* allelic series reached the same functional assignment. The weak **spc1-1** allele retained partial function, whereas **spc1-2** produced severe early arrest and seedling lethality. Thus, the aliases describe alleles or discovery contexts at the same Arabidopsis ZDS locus, not separate proteins. (dong2007thearabidopsisspontaneous pages 1-2)

## 2. Primary molecular function

### 2.1 Catalyzed chemistry and substrate specificity

ZDS is an oxidoreductase of the central carotenoid-biosynthesis pathway. PDS first introduces two double bonds into phytoene-derived substrates; Z-ISO adjusts cis/trans geometry; ZDS then introduces two additional conjugated double bonds. The accepted two-step sequence is:

1. **9,15,9′-tri-*cis*-ζ-carotene → 9,9′-di-*cis*-neurosporene**
2. **9,9′-di-*cis*-neurosporene → 7,9,9′-tri-*cis*-lycopene (prolycopene)**

Accordingly, the biologically relevant specificity is for poly-*cis*, linear C40 carotene intermediates with the appropriate 15-*trans* configuration rather than for all-*trans*-ζ-carotene generally. The products remain linear carotenoids; ZDS does not cyclize lycopene or cleave carotenoids. (rosassaavedra2016biosynthesisofcarotenoids pages 11-14)

The 1999 biochemical work by Bartley, Scolnik, and Beyer, using Arabidopsis carotene desaturases expressed in *Escherichia coli*, established the poly-*cis* pathway leading to prolycopene. However, the retrieved evidence does not provide purified-Q38893 kinetic constants, turnover numbers, or numerical comparisons among alternative isomers. Therefore, the reaction assignment is strong, while claims about relative catalytic efficiency for individual cis-isomers would exceed the available evidence. (moreno2021plantapocarotenoidsfrom pages 31-33)

### 2.2 Cofactor, electron transfer, and domain interpretation

Plant ZDS enzymes are **FAD-dependent, membrane-associated desaturases**. Electrons removed from carotene substrates enter the plastid quinone pool and are ultimately passed through the plastid terminal oxidase system to oxygen. This chemistry is consistent with Q38893’s amino-oxidase/FAD–NAD-binding fold and ζ-carotene-desaturase-family annotations. (rosassaavedra2016biosynthesisofcarotenoids pages 11-14)

The supplied InterPro/Pfam assignments—**Amino_oxidase (IPR002937/PF01593), FAD/NAD-binding superfamily (IPR036188), Zeta_caro_desat (IPR014103),** and **Zeta-carotene-desaturase/oxidoreductase (IPR050464)**—therefore align with the literature. Nevertheless, direct FAD-binding stoichiometry, membrane topology, and quinone preference have not been demonstrated in the retrieved studies using purified At3g04870 itself. Those features should be described as strongly supported family-level mechanism rather than Q38893-specific structural measurements.

## 3. Cellular localization

ZDS acts inside plastids, the site of plant carotenoid biosynthesis. Direct Arabidopsis localization evidence comes from a construct containing the first **120 amino acids** of ZDS fused to GFP. It produced punctate or needle-like fluorescence inside chloroplasts, demonstrating that the N terminus contains plastid-targeting information. The pattern resembled plastoglobuli. (avendanovazquez2014anuncharacterizedapocarotenoidderived pages 2-3)

The safest annotation is therefore **chloroplast/chromoplast-localized, plastid membrane-associated enzyme**. The experiment establishes plastid import but does not, by itself, prove that full-length endogenous ZDS resides exclusively in plastoglobuli rather than partitioning among plastoglobule, thylakoid, or envelope-associated membrane environments. The “precursor” flag is consistent with synthesis in the cytosol followed by N-terminal transit-peptide-dependent import.

## 4. Pathway placement and physiological role

ZDS lies between Z-ISO/PDS-dependent cis-carotene formation and carotenoid isomerase-dependent production of cyclizable all-*trans*-lycopene. Downstream products include α- and β-carotene, lutein and other xanthophylls, photoprotective pigments, and substrates for ABA and diverse apocarotenoid signals. Blocking ZDS therefore has two simultaneous biochemical consequences:

1. **Accumulation of upstream phytofluene/ζ-carotene-related intermediates**.
2. **Depletion of downstream lycopene-derived carotenes and xanthophylls**.

This dual consequence explains why ZDS mutants combine metabolic deficiency—loss of pigments and photoprotection—with signaling phenotypes that differ from some other albino carotenoid mutants. (rosassaavedra2016biosynthesisofcarotenoids pages 11-14, avendanovazquez2014anuncharacterizedapocarotenoidderived pages 1-2)

## 5. Experimental genetics and phenotype

The 2007 **SPC1** study showed that weak **spc1-1** plants undergo leaf bleaching, superoxide accumulation, mosaic spontaneous cell death, reduced downstream carotenoids, and reduced chlorophyll. Strong **spc1-2** seedlings arrest soon after germination and are lethal. Photosynthesis-associated nuclear genes including **Lhcb1.1, Lhcb1.4,** and **RbcS** were undetectable in spc1-2, linking the plastid metabolic defect to retrograde control of nuclear transcription. (dong2007thearabidopsisspontaneous pages 1-2)

The CLB5 work showed very early arrest during proplastid-to-chloroplast differentiation, severe leaf-polarity and cell-expansion defects, and broad disruption of plastid- and nucleus-encoded gene expression. Genetic or pharmacological reduction of upstream PDS activity suppressed important clb5 phenotypes. This is critical mechanistic evidence: the distinctive developmental syndrome is not explained solely by absence of downstream carotenoids; accumulation of an upstream metabolite or derivative is also required. (avendanovazquez2014anuncharacterizedapocarotenoidderived pages 2-3, avendanovazquez2014anuncharacterizedapocarotenoidderived pages 1-2)

## 6. Apocarotenoid retrograde signaling

### 6.1 Current model

The clb5/ZDS block is proposed to permit formation of an unidentified apocarotenoid signal termed **ACS1**, derived from phytofluene and/or ζ-carotene-related metabolites. ACS1 remodels nuclear expression of chloroplast ribosomal proteins, inhibits plastid translation, and triggers a second, GUN1-dependent developmental pathway that produces the characteristic finger-like or needle-like leaves. Light and an early developmental window are important components of this signaling cascade. (escobar‐tovar2021deconvolutingapocarotenoid‐mediatedretrograde pages 5-8, escobar‐tovar2021deconvolutingapocarotenoid‐mediatedretrograde pages 8-10)

The 2021 transcriptomic analysis found **2,193 differentially expressed genes** in clb5 relative to pds3: **626 induced** and **1,567 repressed**. In the **ccd4 clb5** double mutant, **81%** of these genes shifted back toward the pds3 expression state. Approximately **31 of 57** genes encoding large- or small-subunit chloroplast 70S ribosomal proteins fell by more than **2 log2-fold**; 28 of the affected genes were nuclear-encoded. Plastid proteins including ClpP1 and Rpl2 and photosynthetic proteins RbcL and PetA were strongly reduced, consistent with impaired plastid translation. (escobar‐tovar2021deconvolutingapocarotenoid‐mediatedretrograde pages 5-8, escobar‐tovar2021deconvolutingapocarotenoid‐mediatedretrograde pages 8-10)

### 6.2 Major unresolved issue

The signal’s chemical identity remains unknown. Although genetic rescue by **ccd4** initially suggested that CCD4 generates ACS1, authoritative review analysis notes that CCD4 did not cleave the relevant cis-ζ-carotene configurations in tested in-vivo or in-vitro systems. The ccd4 rescue could consequently reflect an indirect metabolic effect rather than direct production of ACS1 by CCD4. (moreno2021plantapocarotenoidsfrom pages 13-15)

Expert interpretation should therefore distinguish two conclusions:

- **Well supported:** blocking ZDS creates a metabolite-dependent retrograde-signaling state that affects plastid translation and leaf development.
- **Not yet established:** the molecular structure of ACS1, its immediate precursor, and the enzyme that directly generates it.

## 7. Recent developments, 2023–2024

A 2023 Plant Journal study reported that deregulating ZDS in Arabidopsis and tomato exposes carotenoid-derived, partly redundant regulation of floral-meristem identity and function: McQuinn et al., **“Deregulation of ζ-carotene desaturase in Arabidopsis and tomato exposes a unique carotenoid-derived redundant regulation of floral meristem identity and function,”** published March 2023, DOI: https://doi.org/10.1111/tpj.16168. This extends interest in ZDS-associated metabolites beyond seedling chloroplast and leaf development to reproductive meristem regulation. However, the full experimental text was not retrievable in the present evidence set, so specific floral counts, metabolite changes, or mechanistic assignments are not asserted here.

Recent research has increasingly treated cis-carotenes as potential regulatory precursors rather than merely pathway intermediates. A relevant 2024 study by Hou et al., published online in November 2023 and in *Journal of Experimental Botany* volume 75 (2024), investigated how reduced phytoene-synthase activity tunes a cis-carotene-derived signal controlling the PIF3/HY5 module and plastid biogenesis; DOI: https://doi.org/10.1093/jxb/erad443. This supports the broader concept that changing flux upstream of ZDS can alter developmental signaling, but it does not chemically identify clb5 ACS1 or change Q38893’s primary enzymatic annotation.

Thus, 2023–2024 work broadens the developmental scope of cis-carotene signaling, while the central unresolved problem remains chemical identification and direct biosynthetic validation of the signal.

## 8. Applications and real-world relevance

### 8.1 Research applications

Arabidopsis clb5/spc1 alleles are valuable experimental tools for separating three coupled processes:

- carotenoid biosynthetic flux and photoprotection;
- chloroplast differentiation and plastid translation;
- metabolite-mediated plastid-to-nucleus signaling.

Because null alleles are severely pleiotropic and often lethal, inducible, partial-loss, tissue-specific, or flux-tuning approaches are more informative than complete knockout for biotechnology.

### 8.2 Crop metabolic engineering

Comparative work in tomato illustrates ZDS’s engineering potential but must not be mistaken for direct Arabidopsis physiology. Tomato ZDS repression increased ripe-fruit ζ-carotene from **0.3 μg g⁻¹ fresh weight** in wild type to **21.7–78.9 μg g⁻¹**, while lycopene declined from **105.7 μg g⁻¹** to **1.1–2.0 μg g⁻¹**. ABA accumulation in developing repressed fruit was at least **75% lower**. Conversely, expression of Arabidopsis ZDS bypassed endogenous tomato co-suppression, supporting the conclusion that ZDS can become a bottleneck in ripening-associated carotenogenesis. (mcquinn2020manipulationofzds pages 5-6)

Potential applications include modification of fruit color, carotenoid composition, nutritional traits, and apocarotenoid/ABA-related development. However, strong ZDS inhibition compromises photoprotective pigments and development; successful implementation would require organ-, stage-, or tissue-specific control. The retrieved evidence establishes experimental proof of concept, not a currently commercialized ZDS1-based Arabidopsis or crop product.

## 9. Overall confidence assessment

**High-confidence annotations** are the locus identity, ζ-carotene-desaturase activity, plastid targeting, placement in the poly-*cis* carotenoid pathway, and necessity for chloroplast development and photoprotection. Genetic complementation, independent alleles, heterologous biochemistry, localization constructs, pigment phenotypes, and transcriptomic data converge on these conclusions. (avendanovazquez2014anuncharacterizedapocarotenoidderived pages 2-3, dong2007thearabidopsisspontaneous pages 1-2, moreno2021plantapocarotenoidsfrom pages 31-33)

**Moderate-confidence annotations** include the precise native intraplastid membrane compartment and Q38893-specific details of FAD/quinone handling, because these are supported chiefly by family biochemistry and targeting experiments rather than a purified native enzyme structure or membrane-topology study. (rosassaavedra2016biosynthesisofcarotenoids pages 11-14)

**Open questions** are ACS1’s chemical identity, its immediate carotenoid precursor, whether CCD4 acts directly or indirectly, and how cis-carotene-derived signals intersect with floral-meristem and broader developmental regulation. (moreno2021plantapocarotenoidsfrom pages 13-15)

## Key references

1. Bartley GE, Scolnik PA, Beyer P. Arabidopsis carotene desaturases and the poly-*cis* pathway to prolycopene. *European Journal of Biochemistry*. **1999**;259:396–403. Bibliographic evidence summarized in the retrieved review. (moreno2021plantapocarotenoidsfrom pages 31-33)
2. Dong H et al. “The Arabidopsis spontaneous cell death1 gene, encoding a ζ-carotene desaturase essential for carotenoid biosynthesis, is involved in chloroplast development, photoprotection and retrograde signalling.” *Cell Research*. **May 2007**;17:458–470. https://doi.org/10.1038/cr.2007.37 (dong2007thearabidopsisspontaneous pages 1-2)
3. Avendaño-Vázquez AO et al. “An uncharacterized apocarotenoid-derived signal generated in ζ-carotene desaturase mutants regulates leaf development and the expression of chloroplast and nuclear genes in Arabidopsis.” *The Plant Cell*. **June 2014**;26:2524–2537. https://doi.org/10.1105/tpc.114.123349 (avendanovazquez2014anuncharacterizedapocarotenoidderived pages 2-3, avendanovazquez2014anuncharacterizedapocarotenoidderived pages 1-2)
4. Escobar-Tovar L et al. “Deconvoluting apocarotenoid-mediated retrograde signaling networks regulating plastid translation and leaf development.” *The Plant Journal*. **March 2021**;105:1582–1599. https://doi.org/10.1111/tpj.15134 (escobar‐tovar2021deconvolutingapocarotenoid‐mediatedretrograde pages 5-8, escobar‐tovar2021deconvolutingapocarotenoid‐mediatedretrograde pages 8-10)
5. Moreno JC et al. “Plant apocarotenoids: from retrograde signaling to interspecific communication.” *The Plant Journal*. **January 2021**;105:351–375. https://doi.org/10.1111/tpj.15102 (moreno2021plantapocarotenoidsfrom pages 13-15)
6. McQuinn RP et al. “Manipulation of ZDS in tomato exposes carotenoid- and ABA-specific effects on fruit development and ripening.” *Plant Biotechnology Journal*. **April 2020**;18:2210–2224. https://doi.org/10.1111/pbi.13377 (mcquinn2020manipulationofzds pages 5-6)
7. McQuinn RP et al. “Deregulation of ζ-carotene desaturase in Arabidopsis and tomato exposes a unique carotenoid-derived redundant regulation of floral meristem identity and function.” *The Plant Journal*. **March 2023**;114:783–804. https://doi.org/10.1111/tpj.16168

References

1. (avendanovazquez2014anuncharacterizedapocarotenoidderived pages 2-3): Aida-Odette Avendaño-Vázquez, Elizabeth Cordoba, Ernesto Llamas, Carolina San Román, Nazia Nisar, Susana De la Torre, Maricela Ramos-Vega, María de la Luz Gutiérrez-Nava, Christopher Ian Cazzonelli, Barry James Pogson, and Patricia León. An uncharacterized apocarotenoid-derived signal generated in ζ-carotene desaturase mutants regulates leaf development and the expression of chloroplast and nuclear genes in arabidopsis[c][w]. Plant Cell, 26:2524-2537, Jun 2014. URL: https://doi.org/10.1105/tpc.114.123349, doi:10.1105/tpc.114.123349. This article has 151 citations and is from a highest quality peer-reviewed journal.

2. (dong2007thearabidopsisspontaneous pages 1-2): Haili Dong, Yan Deng, Jinye Mu, Qingtao Lu, Yiqin Wang, Yunyuan Xu, Chengcai Chu, Kang Chong, Congming Lu, and Jianru Zuo. The arabidopsis spontaneous cell death1 gene, encoding a ζ-carotene desaturase essential for carotenoid biosynthesis, is involved in chloroplast development, photoprotection and retrograde signalling. Cell Research, 17:458-470, May 2007. URL: https://doi.org/10.1038/cr.2007.37, doi:10.1038/cr.2007.37. This article has 91 citations and is from a domain leading peer-reviewed journal.

3. (avendanovazquez2014anuncharacterizedapocarotenoidderived pages 1-2): Aida-Odette Avendaño-Vázquez, Elizabeth Cordoba, Ernesto Llamas, Carolina San Román, Nazia Nisar, Susana De la Torre, Maricela Ramos-Vega, María de la Luz Gutiérrez-Nava, Christopher Ian Cazzonelli, Barry James Pogson, and Patricia León. An uncharacterized apocarotenoid-derived signal generated in ζ-carotene desaturase mutants regulates leaf development and the expression of chloroplast and nuclear genes in arabidopsis[c][w]. Plant Cell, 26:2524-2537, Jun 2014. URL: https://doi.org/10.1105/tpc.114.123349, doi:10.1105/tpc.114.123349. This article has 151 citations and is from a highest quality peer-reviewed journal.

4. (rosassaavedra2016biosynthesisofcarotenoids pages 11-14): Carolina Rosas-Saavedra and Claudia Stange. Biosynthesis of carotenoids in plants: enzymes and color. Sub-cellular biochemistry, 79:35-69, Jan 2016. URL: https://doi.org/10.1007/978-3-319-39126-7\_2, doi:10.1007/978-3-319-39126-7\_2. This article has 136 citations.

5. (moreno2021plantapocarotenoidsfrom pages 31-33): Juan C. Moreno, Jianing Mi, Yagiz Alagoz, and Salim Al‐Babili. Plant apocarotenoids: from retrograde signaling to interspecific communication. The Plant Journal, 105:351-375, Jan 2021. URL: https://doi.org/10.1111/tpj.15102, doi:10.1111/tpj.15102. This article has 238 citations.

6. (escobar‐tovar2021deconvolutingapocarotenoid‐mediatedretrograde pages 5-8): Lina Escobar‐Tovar, Julio Sierra, Arihel Hernández‐Muñoz, Ryan P. McQuinn, Sandra Mathioni, Elizabeth Cordoba, Catherine Colas des Francs‐Small, Blake C. Meyers, Barry Pogson, and Patricia León. Deconvoluting apocarotenoid‐mediated retrograde signaling networks regulating plastid translation and leaf development. Mar 2021. URL: https://doi.org/10.1111/tpj.15134, doi:10.1111/tpj.15134. This article has 32 citations.

7. (moreno2021plantapocarotenoidsfrom pages 13-15): Juan C. Moreno, Jianing Mi, Yagiz Alagoz, and Salim Al‐Babili. Plant apocarotenoids: from retrograde signaling to interspecific communication. The Plant Journal, 105:351-375, Jan 2021. URL: https://doi.org/10.1111/tpj.15102, doi:10.1111/tpj.15102. This article has 238 citations.

8. (escobar‐tovar2021deconvolutingapocarotenoid‐mediatedretrograde pages 8-10): Lina Escobar‐Tovar, Julio Sierra, Arihel Hernández‐Muñoz, Ryan P. McQuinn, Sandra Mathioni, Elizabeth Cordoba, Catherine Colas des Francs‐Small, Blake C. Meyers, Barry Pogson, and Patricia León. Deconvoluting apocarotenoid‐mediated retrograde signaling networks regulating plastid translation and leaf development. Mar 2021. URL: https://doi.org/10.1111/tpj.15134, doi:10.1111/tpj.15134. This article has 32 citations.

9. (mcquinn2020manipulationofzds pages 5-6): Ryan P. McQuinn, Nigel E. Gapper, Amanda G. Gray, Silin Zhong, Takayuki Tohge, Zhangjun Fei, Alisdair R. Fernie, and James J. Giovannoni. Manipulation of zds in tomato exposes carotenoid‐ and aba‐specific effects on fruit development and ripening. Plant Biotechnology Journal, 18:2210-2224, Apr 2020. URL: https://doi.org/10.1111/pbi.13377, doi:10.1111/pbi.13377. This article has 68 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](ZDS-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. rosassaavedra2016biosynthesisofcarotenoids pages 11-14
2. avendanovazquez2014anuncharacterizedapocarotenoidderived pages 2-3
3. moreno2021plantapocarotenoidsfrom pages 13-15
4. mcquinn2020manipulationofzds pages 5-6
5. dong2007thearabidopsisspontaneous pages 1-2
6. moreno2021plantapocarotenoidsfrom pages 31-33
7. avendanovazquez2014anuncharacterizedapocarotenoidderived pages 1-2
8. c
9. w
10. https://doi.org/10.1111/tpj.16168.
11. https://doi.org/10.1093/jxb/erad443.
12. https://doi.org/10.1038/cr.2007.37
13. https://doi.org/10.1105/tpc.114.123349
14. https://doi.org/10.1111/tpj.15134
15. https://doi.org/10.1111/tpj.15102
16. https://doi.org/10.1111/pbi.13377
17. https://doi.org/10.1111/tpj.16168
18. https://doi.org/10.1105/tpc.114.123349,
19. https://doi.org/10.1038/cr.2007.37,
20. https://doi.org/10.1007/978-3-319-39126-7\_2,
21. https://doi.org/10.1111/tpj.15102,
22. https://doi.org/10.1111/tpj.15134,
23. https://doi.org/10.1111/pbi.13377,