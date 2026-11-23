---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-30T05:59:34.854396'
end_time: '2026-09-30T06:11:10.072395'
duration_seconds: 695.22
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: ARATH
  gene_id: IIL1
  gene_symbol: IIL1
  uniprot_accession: Q94AR8
  protein_description: 'RecName: Full=3-isopropylmalate dehydratase large subunit,
    chloroplastic {ECO:0000305}; EC=4.2.1.33 {ECO:0000269|PubMed:19597944}; AltName:
    Full=2-(omega-methylthio)alkylmalate dehydratase large subunit {ECO:0000305};
    EC=4.2.1.170 {ECO:0000269|PubMed:19597944}; AltName: Full=AtLEUC {ECO:0000303|PubMed:20663849};
    AltName: Full=Isopropylmalate isomerase large subunit 1 {ECO:0000303|PubMed:19150812,
    ECO:0000303|PubMed:19597944}; Short=AtIIL1 {ECO:0000303|PubMed:19150812}; Short=IPMI
    LSU1 {ECO:0000303|PubMed:19597944}; AltName: Full=Methylthioalkylmalate isomerase
    large subunit {ECO:0000305}; Short=MAM-IL {ECO:0000305}; Flags: Precursor;'
  gene_info: Name=IIL1 {ECO:0000303|PubMed:19150812}; OrderedLocusNames=At4g13430
    {ECO:0000312|Araport:AT4G13430}; ORFNames=T9E8.170 {ECO:0000312|EMBL:CAB40778.1};
  organism_full: Arabidopsis thaliana (Mouse-ear cress).
  protein_family: Belongs to the aconitase/IPM isomerase family.
  protein_domains: Acnase/IPM_dHydase_lsu_aba_1/3. (IPR015931); Acoase/IPM_deHydtase_lsu_aba.
    (IPR001030); Aconitase_4Fe-4S_dom. (IPR036008); Homoacnase/IPMdehydase_lsu. (IPR006251);
    IPM_dehydratase_rel_enz. (IPR050067)
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
  path: IIL1-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q94AR8
- **Protein Description:** RecName: Full=3-isopropylmalate dehydratase large subunit, chloroplastic {ECO:0000305}; EC=4.2.1.33 {ECO:0000269|PubMed:19597944}; AltName: Full=2-(omega-methylthio)alkylmalate dehydratase large subunit {ECO:0000305}; EC=4.2.1.170 {ECO:0000269|PubMed:19597944}; AltName: Full=AtLEUC {ECO:0000303|PubMed:20663849}; AltName: Full=Isopropylmalate isomerase large subunit 1 {ECO:0000303|PubMed:19150812, ECO:0000303|PubMed:19597944}; Short=AtIIL1 {ECO:0000303|PubMed:19150812}; Short=IPMI LSU1 {ECO:0000303|PubMed:19597944}; AltName: Full=Methylthioalkylmalate isomerase large subunit {ECO:0000305}; Short=MAM-IL {ECO:0000305}; Flags: Precursor;
- **Gene Information:** Name=IIL1 {ECO:0000303|PubMed:19150812}; OrderedLocusNames=At4g13430 {ECO:0000312|Araport:AT4G13430}; ORFNames=T9E8.170 {ECO:0000312|EMBL:CAB40778.1};
- **Organism (full):** Arabidopsis thaliana (Mouse-ear cress).
- **Protein Family:** Belongs to the aconitase/IPM isomerase family.
- **Key Domains:** Acnase/IPM_dHydase_lsu_aba_1/3. (IPR015931); Acoase/IPM_deHydtase_lsu_aba. (IPR001030); Aconitase_4Fe-4S_dom. (IPR036008); Homoacnase/IPMdehydase_lsu. (IPR006251); IPM_dehydratase_rel_enz. (IPR050067)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "IIL1" matches the protein description above**
2. **Verify the organism is correct:** Arabidopsis thaliana (Mouse-ear cress).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'IIL1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **IIL1** (gene ID: IIL1, UniProt: Q94AR8) in ARATH.

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
- **UniProt Accession:** Q94AR8
- **Protein Description:** RecName: Full=3-isopropylmalate dehydratase large subunit, chloroplastic {ECO:0000305}; EC=4.2.1.33 {ECO:0000269|PubMed:19597944}; AltName: Full=2-(omega-methylthio)alkylmalate dehydratase large subunit {ECO:0000305}; EC=4.2.1.170 {ECO:0000269|PubMed:19597944}; AltName: Full=AtLEUC {ECO:0000303|PubMed:20663849}; AltName: Full=Isopropylmalate isomerase large subunit 1 {ECO:0000303|PubMed:19150812, ECO:0000303|PubMed:19597944}; Short=AtIIL1 {ECO:0000303|PubMed:19150812}; Short=IPMI LSU1 {ECO:0000303|PubMed:19597944}; AltName: Full=Methylthioalkylmalate isomerase large subunit {ECO:0000305}; Short=MAM-IL {ECO:0000305}; Flags: Precursor;
- **Gene Information:** Name=IIL1 {ECO:0000303|PubMed:19150812}; OrderedLocusNames=At4g13430 {ECO:0000312|Araport:AT4G13430}; ORFNames=T9E8.170 {ECO:0000312|EMBL:CAB40778.1};
- **Organism (full):** Arabidopsis thaliana (Mouse-ear cress).
- **Protein Family:** Belongs to the aconitase/IPM isomerase family.
- **Key Domains:** Acnase/IPM_dHydase_lsu_aba_1/3. (IPR015931); Acoase/IPM_deHydtase_lsu_aba. (IPR001030); Aconitase_4Fe-4S_dom. (IPR036008); Homoacnase/IPMdehydase_lsu. (IPR006251); IPM_dehydratase_rel_enz. (IPR050067)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "IIL1" matches the protein description above**
2. **Verify the organism is correct:** Arabidopsis thaliana (Mouse-ear cress).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'IIL1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **IIL1** (gene ID: IIL1, UniProt: Q94AR8) in ARATH.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: IIL1 (IPMI LSU1) in Arabidopsis thaliana

## Gene Identity and Nomenclature

The gene IIL1 (Isopropylmalate Isomerase Large subunit 1) corresponds to the Arabidopsis thaliana locus **At4g13430** (UniProt Q94AR8) and encodes the large catalytic subunit of the plastidial isopropylmalate isomerase (IPMI), also known as isopropylmalate dehydratase (knill2009arabidopsisthalianaencodes pages 2-4, sawada2009omicsbasedapproachesto pages 1-2). This protein is alternatively designated as **IPMI LSU1**, **AtLeuC1**, **LEUC**, or **MAM-IL1** (methylthioalkylmalate isomerase large subunit 1) in the literature (sawada2009omicsbasedapproachesto pages 1-2, sawada2009omicsbasedapproachesto pages 2-4). The gene identity has been verified to match the UniProt description of a 3-isopropylmalate dehydratase large subunit, chloroplastic precursor with dual enzymatic activities (EC 4.2.1.33 and EC 4.2.1.170).

## Enzymatic Function and Catalyzed Reactions

### Primary Enzymatic Activity

IIL1 encodes the large subunit of a bacterial-type heterodimeric isopropylmalate isomerase/dehydratase (EC 4.2.1.33) that belongs to the aconitase/IPM-isomerase family (binder2010branchedchainaminoacid pages 6-7). The enzyme catalyzes a reversible isomerization reaction involving the rearrangement of 2-substituted malate derivatives to their corresponding 3-substituted isomers (binder2010branchedchainaminoacid pages 6-7, knill2009arabidopsisthalianaencodes pages 1-2).

In **leucine biosynthesis**, the enzyme catalyzes the reversible conversion of **2-isopropylmalate (2-IPM) to 3-isopropylmalate (3-IPM)**, representing the second step of the leucine-specific biosynthetic pathway (knill2009arabidopsisthalianaencodes pages 8-10, binder2010branchedchainaminoacid pages 6-7, knill2009arabidopsisthalianaencodes pages 1-2). This reaction follows the condensation of acetyl-CoA with 3-methyl-2-oxobutanoate by isopropylmalate synthase and precedes oxidative decarboxylation by isopropylmalate dehydrogenase (knill2009arabidopsisthalianaencodes pages 1-2).

### Secondary Enzymatic Activity in Specialized Metabolism

The same large subunit also catalyzes structurally analogous reactions in **methionine side-chain elongation** for aliphatic glucosinolate biosynthesis (knill2009arabidopsisthalianaencodes pages 1-2, sawada2009omicsbasedapproachesto pages 1-2). In this pathway, the enzyme converts **2-(ω-methylthio)alkylmalates to 3-(ω-methylthio)alkylmalates** (EC 4.2.1.170), with documented substrates including 2-(3-methylthiopropyl)malate associated with the second elongation cycle (knill2009arabidopsisthalianaencodes pages 7-8, knill2009arabidopsisthalianaencodes pages 2-4). This dual functionality reflects an evolutionary recruitment from primary amino acid metabolism to specialized defense compound biosynthesis (knill2009arabidopsisthalianaencodes pages 1-2).

## Substrate Specificity and Determinants

IIL1 exhibits **broad substrate specificity** encompassing both leucine pathway intermediates and sulfur-containing methylthioalkylmalate derivatives (knill2009arabidopsisthalianaencodes pages 7-8, knill2009arabidopsisthalianaencodes pages 2-4, knill2009arabidopsisthalianaencodes pages 8-10). The protein does not determine substrate specificity independently; rather, it functions as the shared large-subunit component of heterodimeric complexes whose substrate preference is primarily conferred by the associated small subunit (lachler2020inarabidopsisthaliana pages 1-2, imhof2014thesmallsubunit pages 9-10).

Arabidopsis encodes three IPMI small subunits that define functional specialization: **IPMI SSU1** preferentially supports leucine biosynthesis and the first cycle of methionine chain elongation, while **IPMI SSU2 and SSU3** are specialized for later rounds of methionine-chain elongation in glucosinolate biosynthesis, though some functional overlap exists (lachler2020inarabidopsisthaliana pages 1-2, imhof2014thesmallsubunit pages 9-10, imhof2014thesmallsubunit pages 7-8). The large subunit IIL1/IPMI LSU1 is encoded by a single gene and is shared across all these heterodimeric combinations (knill2009arabidopsisthalianaencodes pages 2-4, knill2009arabidopsisthalianaencodes pages 1-2).

## Subcellular Localization

IIL1/IPMI LSU1 functions in **plastids**, including both chloroplasts and specialized non-photosynthetic plastids depending on tissue type and developmental stage (knill2009arabidopsisthalianaencodes pages 2-4, knill2009arabidopsisthalianaencodes pages 1-2, knill2009arabidopsisthalianaencodes pages 7-8). Sequence analysis reveals N-terminal extensions predicted to serve as plastid-targeting signals for both the large and small IPMI subunits (knill2009arabidopsisthalianaencodes pages 2-4). Experimental GFP-tagging studies have confirmed chloroplast import for IPMI small subunits, with SSU2 specifically localized to chloroplasts and SSU1 found in smaller, non-green plastids in epidermal cells and root tissues (knill2009arabidopsisthalianaencodes pages 7-8, lachler2020inarabidopsisthaliana pages 6-8, lachler2020inarabidopsisthaliana pages 1-2).

The plastidial localization is functionally appropriate, as both leucine biosynthesis and the methionine chain-elongation pathway for glucosinolate formation occur in these organelles (knill2009arabidopsisthalianaencodes pages 1-2, knill2009arabidopsisthalianaencodes pages 7-8). Tissue-specific expression patterns show that SSU1-containing complexes are prevalent in small plastids of epidermis and root parenchyma, while SSU2/SSU3-containing complexes localize to chloroplasts in photosynthetic parenchyma surrounding vasculature (lachler2020inarabidopsisthaliana pages 6-8, lachler2020inarabidopsisthaliana pages 1-2).

## Biochemical Pathways

### Leucine Biosynthesis Pathway

IIL1 plays an essential role in the **plastidial leucine biosynthesis pathway**, functioning as the second enzyme in the leucine-specific branch that diverges from valine biosynthesis (binder2010branchedchainaminoacid pages 6-7, knill2009arabidopsisthalianaencodes pages 8-10). The pathway proceeds through the following sequence:

1. Isopropylmalate synthase (IPMS) condenses 3-methyl-2-oxobutanoate with acetyl-CoA to form 2-isopropylmalate
2. **Isopropylmalate isomerase (IPMI; IIL1 + small subunit)** converts 2-isopropylmalate to 3-isopropylmalate
3. Isopropylmalate dehydrogenase (IPMDH) performs oxidative decarboxylation to yield 4-methyl-2-oxopentanoate
4. Branched-chain aminotransferase (BCAT) transamination produces leucine

Genetic evidence from ipmi lsu1 mutants demonstrates accumulation of 2-isopropylmalate and elevated valine levels, confirming IIL1's role in channeling metabolites from the shared branched-chain amino acid pathway specifically into leucine biosynthesis (binder2010branchedchainaminoacid pages 6-7, knill2009arabidopsisthalianaencodes pages 8-10, knill2009arabidopsisthalianaencodes pages 4-6).

### Methionine Chain Elongation and Glucosinolate Biosynthesis

IIL1 functions in the **methionine side-chain elongation pathway**, which generates elongated methionine derivatives that serve as precursors for aliphatic glucosinolate biosynthesis—a characteristic defense system of Brassicaceae plants (knill2009arabidopsisthalianaencodes pages 10-12, knill2009arabidopsisthalianaencodes pages 1-2). This pathway involves iterative cycles of chain elongation, each comprising:

1. Transamination of methionine (or elongated homologs) to the corresponding 2-oxo acid
2. Condensation with acetyl-CoA by methylthioalkylmalate synthase (MAM)
3. **Isomerization by methylthioalkylmalate isomerase (MAM-IL; IIL1 + SSU2/SSU3)** converting 2-methylthioalkylmalate to 3-methylthioalkylmalate
4. Oxidative decarboxylation by methylthioalkylmalate dehydrogenase
5. Transamination to produce chain-elongated methionine derivatives

The products of these cycles undergo further modifications including S-oxygenation, core structure formation, and secondary modifications to yield the diverse array of aliphatic glucosinolates (knill2009arabidopsisthalianaencodes pages 10-12, knill2009arabidopsisthalianaencodes pages 1-2). IIL1 mutants show characteristic shifts toward shorter-chain glucosinolates, with reductions in C7-C8 species and increases in C3 glucosinolates, demonstrating impaired capacity for multiple rounds of chain elongation (knill2009arabidopsisthalianaencodes pages 7-8, knill2009arabidopsisthalianaencodes pages 10-12, sawada2009omicsbasedapproachesto pages 2-4).

### Pathway Integration and Regulation

The dual functionality of IIL1 represents a biochemical bridge between primary branched-chain amino acid metabolism and specialized defense metabolism (knill2009arabidopsisthalianaencodes pages 10-12, knill2009arabidopsisthalianaencodes pages 1-2). Transcriptional evidence indicates that IIL1/AtLeuC1 is co-expressed with established methionine-derived glucosinolate biosynthetic genes and is coordinately regulated by the R2R3-MYB transcription factor MYB28/HAG1, the master regulator of aliphatic glucosinolate biosynthesis (sawada2009omicsbasedapproachesto pages 2-4). This regulatory integration confirms IIL1's assignment to the glucosinolate chain-elongation module while maintaining its essential housekeeping function in leucine biosynthesis.

## Protein Structure and Cofactor Requirements

### Quaternary Structure

IIL1/IPMI LSU1 forms **bacterial-type heterodimeric complexes** comprising the large subunit paired with one of three small subunits (SSU1, SSU2, or SSU3) (knill2009arabidopsisthalianaencodes pages 2-4, lachler2020inarabidopsisthaliana pages 1-2, knill2009arabidopsisthalianaencodes pages 1-2). This heterodimeric organization distinguishes Arabidopsis IPMI from the monomeric fungal and some prokaryotic enzymes. The large subunit should therefore be understood as an essential component of the active enzyme complex rather than an independently functional protein.

### Protein Family and Domains

IIL1 belongs to the **aconitase/isopropylmalate isomerase family** and contains conserved aconitase-like iron-sulfur domain architecture (binder2010branchedchainaminoacid pages 6-7). This family assignment aligns with the UniProt-annotated InterPro domains including aconitase/IPM dehydratase large subunit (IPR001030), aconitase 4Fe-4S domain (IPR036008), and homoaconitase/IPM dehydratase large subunit (IPR006251).

### Iron-Sulfur Cluster Requirements

As a member of the aconitase family, IPMI large subunits are predicted to contain **[4Fe-4S] clusters** essential for catalytic activity (binder2010branchedchainaminoacid pages 6-7). The Fe-S-bearing component in IPMI heterodimers is attributed to the large subunit based on homology with bacterial and mitochondrial orthologs (roland2020theplastidialarabidopsis pages 4-6, roland2020theplastidialarabidopsis pages 6-7). However, direct experimental demonstration of Fe-S cluster binding, spectroscopic characterization, or reconstitution studies for Arabidopsis IIL1/IPMI LSU1 remain limited in the current literature. Studies investigating the plastidial NFU1 protein as a potential [4Fe-4S] cluster delivery factor identified IPMI as a candidate interaction partner, but this interaction could not be conclusively established due to technical limitations including auto-activation in yeast assays (roland2020theplastidialarabidopsis pages 6-7, roland2020theplastidialarabidopsis pages 8-9, roland2020theplastidialarabidopsis pages 20-22). Therefore, while Fe-S cofactor requirements are strongly predicted from structural homology, direct biochemical validation for the Arabidopsis protein awaits further investigation.

## Experimental Evidence

### Genetic Evidence from Mutant Studies

Multiple independent T-DNA insertion alleles of IIL1/IPMI LSU1 have been characterized, providing robust genetic evidence for its dual pathway functions (knill2009arabidopsisthalianaencodes pages 10-12, knill2009arabidopsisthalianaencodes pages 8-10, knill2009arabidopsisthalianaencodes pages 4-6). Three principal alleles (ipmi lsu1-1, ipmi lsu1-2, and ipmi lsu1-3) carry insertions in the 5' untranslated region and produce varying degrees of transcript reduction in an allele- and tissue-dependent manner (knill2009arabidopsisthalianaencodes pages 4-6). These represent hypomorphic rather than complete null mutations.

### Metabolic Phenotypes

**Leucine pathway intermediates:** Mutant plants accumulate 2-isopropylmalate, with quantitative measurements showing approximately 0.42 mg/g dry weight in the strongest ipmi lsu1-3 allele, 0.02 mg/g in ipmi lsu1-1, and undetectable levels in ipmi lsu1-2 and wild-type plants (knill2009arabidopsisthalianaencodes pages 4-6, knill2009arabidopsisthalianaencodes pages 6-7). This accumulation directly demonstrates impaired IPMI activity in vivo.

**Amino acid levels:** Stronger alleles show approximately **2-fold elevation in methionine** and accumulation of S-methylmethionine (SMM), particularly pronounced in ipmi lsu1-1 and ipmi lsu1-3 rosette leaves and seeds (knill2009arabidopsisthalianaencodes pages 4-6). Valine levels increase in ipmi lsu1-3 mutants, consistent with reduced flux from the shared pathway into leucine synthesis, while leucine and isoleucine levels remain comparable to wild-type, indicating metabolic buffering (knill2009arabidopsisthalianaencodes pages 4-6, knill2009arabidopsisthalianaencodes pages 6-7).

**Glucosinolate alterations:** All mutant alleles display substantial changes in aliphatic glucosinolate composition in both leaves and seeds (knill2009arabidopsisthalianaencodes pages 10-12, knill2009arabidopsisthalianaencodes pages 6-7). Stronger atleuc1/iil1 knockouts show significant reductions in long-chain C7-C8 methionine-derived glucosinolates, decreases in C4-C6 species, and increases in C3 glucosinolates, consistent with impaired repeated side-chain elongation (sawada2009omicsbasedapproachesto pages 2-4). Notably, tryptophan-derived indolic glucosinolates are comparatively unaffected, demonstrating pathway specificity (sawada2009omicsbasedapproachesto pages 2-4).

**Chain elongation intermediates:** Mutants accumulate 2-(3'-methylsulfinyl)propylmalate, an oxidized intermediate of the second methionine chain-elongation cycle that is absent from wild-type plants, providing direct evidence that the IPMI isomerization step is blocked in the glucosinolate pathway (knill2009arabidopsisthalianaencodes pages 10-12, knill2009arabidopsisthalianaencodes pages 8-10, knill2009arabidopsisthalianaencodes pages 6-7).

### Developmental Phenotypes

The developmental consequences of IIL1 reduction vary by allele strength. The strongest allele, ipmi lsu1-3, exhibits **severe developmental delay**, while milder alleles (ipmi lsu1-1 and ipmi lsu1-2) show primarily biochemical rather than gross morphological defects (knill2009arabidopsisthalianaencodes pages 4-6). Importantly, simple leucine deficiency does not fully explain the developmental abnormalities, as amino acid supplementation improves growth but does not restore normal morphology in severe knockdown lines (imhof2014thesmallsubunit pages 4-5).

A recent 2023 preprint reported a temperature-sensitive leaf developmental defect (the "iil phenotype") in the Arabidopsis Bur-0 accession linked to expanded intronic TTC trinucleotide repeats in IIL1 (li2023intronictnrretainedisopropylmalate pages 12-15). This phenotype results from co-suppression reducing total IIL1 transcripts combined with increased abundance of intron-3-retained transcripts (approximately 25-39% in affected tissues versus below 1-6% in controls), suggesting that aberrant IIL1 transcripts may produce non-functional proteins that interfere with normal metabolism (li2023intronictnrretainedisopropylmalate pages 12-15). This finding emphasizes that IIL1 function depends not only on expression levels but also on transcript quality.

### Complementation and Functional Studies

Arabidopsis IPMI small subunits (SSU1, SSU2, SSU3) can functionally replace the bacterial leuD small subunit in E. coli leucine auxotrophs, demonstrating evolutionary conservation of the heterodimeric IPMI structure and function (imhof2014thesmallsubunit pages 9-10, imhof2014thesmallsubunit pages 8-9). However, Arabidopsis IPMI LSU1 did not complement E. coli leuC deletions, indicating that proper function in planta requires appropriate plant-specific small-subunit partners (imhof2014thesmallsubunit pages 9-10).

### Localization Studies

GFP-tagging experiments confirmed chloroplast import for IPMI SSU2 in both tobacco and Arabidopsis protoplasts (knill2009arabidopsisthalianaencodes pages 7-8). Detailed tissue-specific localization showed SSU1 in small plastids of epidermal cells and root tissues, while SSU2 and SSU3 localize to larger chloroplasts in photosynthetic parenchyma (lachler2020inarabidopsisthaliana pages 6-8, lachler2020inarabidopsisthaliana pages 1-2, lachler2020inarabidopsisthaliana pages 8-10). These patterns support the model that IIL1/IPMI LSU1 functions in multiple plastid types depending on its small-subunit partner and tissue context.

### Transcriptional and Co-expression Evidence

Gene expression profiling and regulatory studies demonstrate that IIL1/AtLeuC1 is co-expressed with established methionine-derived glucosinolate biosynthetic genes and is transcriptionally activated by the MYB28/HAG1 transcription factor, the master positive regulator of aliphatic glucosinolate biosynthesis (sawada2009omicsbasedapproachesto pages 2-4). This regulatory coordination provides independent support for IIL1's role in specialized metabolism beyond its primary function in leucine biosynthesis.

## Evolutionary and Bioinformatic Context

The dual functionality of IIL1 reflects the **evolutionary recruitment of primary metabolic enzymes into specialized metabolic pathways** (knill2009arabidopsisthalianaencodes pages 1-2). The methionine chain-elongation pathway for glucosinolate biosynthesis shares all four reaction types with leucine biosynthesis: condensation, isomerization, oxidative decarboxylation, and transamination (knill2009arabidopsisthalianaencodes pages 1-2). This close evolutionary relationship suggests that the glucosinolate pathway arose through duplication and divergence of leucine biosynthetic genes, with IIL1/IPMI LSU1 representing a shared component that retained its original function while acquiring a new role in specialized metabolism.

Phylogenetic analyses indicate that methylthioalkylmalate synthase (MAM) evolved from isopropylmalate synthase (IPMS) through loss of a regulatory domain and a few active-site amino acid changes. Similarly, the IPMI system adapted to recognize structurally analogous sulfur-containing substrates through evolution of specialized small subunits (SSU2 and SSU3) while retaining the ancestral large subunit and leucine-pathway small subunit (SSU1) (lachler2020inarabidopsisthaliana pages 1-2, imhof2014thesmallsubunit pages 9-10).

## Summary and Current Understanding

IIL1 (At4g13430, UniProt Q94AR8) encodes the plastidial isopropylmalate isomerase large subunit, a dual-function enzyme at the intersection of primary and specialized metabolism in Arabidopsis thaliana. The protein functions as the essential large-subunit component of heterodimeric IPMI complexes that catalyze the reversible isomerization of 2-substituted malates to 3-substituted malates in both leucine biosynthesis (2-isopropylmalate ⇌ 3-isopropylmalate) and methionine chain elongation for aliphatic glucosinolate biosynthesis (2-methylthioalkylmalates ⇌ 3-methylthioalkylmalates). 

The enzyme operates in plastids, where it partners with different small subunits to achieve functional specialization: SSU1 for leucine biosynthesis and early glucosinolate chain elongation, and SSU2/SSU3 for later glucosinolate elongation cycles. Genetic evidence from multiple independent mutant alleles demonstrates that IIL1 is essential for normal flux through both pathways, with mutations causing accumulation of pathway intermediates, altered glucosinolate chain-length distributions, and developmental defects in stronger alleles.

As a member of the aconitase/IPM-isomerase family, IIL1 is predicted to contain [4Fe-4S] clusters essential for catalysis, though direct biochemical characterization of the Arabidopsis protein's cofactor requirements remains incomplete. The dual functionality of IIL1 exemplifies the evolutionary plasticity of plant metabolism, wherein enzymes of primary metabolism can be recruited and adapted for specialized defensive functions while maintaining their original housekeeping roles.

| Feature/Aspect | Description | Key Evidence/References |
|---|---|---|
| Identity | **IIL1** is *Arabidopsis thaliana* locus **At4g13430**, encoding the single large subunit of the bacterial-type heterodimeric isopropylmalate isomerase/dehydratase, commonly termed **IPMI LSU1**, **AtLeuC1**, or **MAM-IL1**. This identity matches UniProt Q94AR8 and should not be confused with similarly named genes in other organisms. | Independent genetic studies identify At4g13430 as the IPMI large-subunit gene (knill2009arabidopsisthalianaencodes pages 2-4, sawada2009omicsbasedapproachesto pages 1-2, sawada2009omicsbasedapproachesto pages 2-4). |
| Enzyme class and primary function | IIL1 is the shared large-subunit component of **isopropylmalate isomerase/dehydratase** (EC 4.2.1.33). The functional enzyme catalyzes a reversible rearrangement of a 2-substituted malate into the corresponding 3-substituted malate. | The reaction and enzyme assignment are supported by pathway studies and a branched-chain amino-acid metabolism review (binder2010branchedchainaminoacid pages 6-7, knill2009arabidopsisthalianaencodes pages 1-2). |
| Leucine-pathway reaction | In leucine biosynthesis, the IPMI complex converts **2-isopropylmalate ⇌ 3-isopropylmalate**. This is the second reaction of the leucine-specific extension sequence, between isopropylmalate synthase and isopropylmalate dehydrogenase. | Reduced IIL1 activity causes accumulation of 2-isopropylmalate, directly linking the gene product to this reaction in vivo (knill2009arabidopsisthalianaencodes pages 8-10, knill2009arabidopsisthalianaencodes pages 1-2). |
| Glucosinolate-pathway reaction | In methionine side-chain elongation, the same type of reaction converts **2-(ω-methylthio)alkylmalates into the corresponding 3-(ω-methylthio)alkylmalates** before oxidative decarboxylation. UniProt therefore also assigns EC 4.2.1.170 to the protein. | Mutant metabolite profiles and pathway analysis establish IIL1/MAM-IL1 as the large subunit of methylthioalkylmalate isomerase (knill2009arabidopsisthalianaencodes pages 1-2, sawada2009omicsbasedapproachesto pages 1-2, sawada2009omicsbasedapproachesto pages 2-4). |
| Substrate specificity | IIL1 is not restricted to one substrate class. Its complexes process **2-isopropylmalate** in primary leucine metabolism and structurally analogous sulfur-containing malates in specialized metabolism. A documented example is **2-(3-methylthiopropyl)malate**, associated with methionine-chain elongation. | Genetic and metabolomic evidence supports utilization of both isopropylmalate and methylthioalkylmalate substrates (knill2009arabidopsisthalianaencodes pages 7-8, knill2009arabidopsisthalianaencodes pages 2-4, knill2009arabidopsisthalianaencodes pages 8-10). |
| Determinant of specificity | The large subunit is shared, whereas much of substrate and pathway preference is conferred by the associated small subunit. **SSU1** principally supports leucine synthesis; **SSU2 and SSU3** preferentially support methionine-chain elongation, although overlap occurs. | Small-subunit genetics and substrate-recognition analysis support this division of labor (lachler2020inarabidopsisthaliana pages 1-2, imhof2014thesmallsubunit pages 9-10, imhof2014thesmallsubunit pages 7-8). |
| Quaternary organization | Arabidopsis IPMI is a **bacterial-type heterodimer**, comprising IIL1/IPMI LSU1 and one of three alternative small subunits. IIL1 should therefore be annotated as an essential subunit of the active complex rather than assumed to act independently. | The single-large/three-small-subunit organization is consistently reported across foundational and later studies (knill2009arabidopsisthalianaencodes pages 2-4, lachler2020inarabidopsisthaliana pages 1-2, knill2009arabidopsisthalianaencodes pages 1-2). |
| Protein family and domains | IIL1 belongs to the **aconitase/IPM-isomerase family** and contains the conserved aconitase-like iron–sulfur domain architecture expected for IPMI large subunits. This aligns with the UniProt/InterPro domain assignments supplied for Q94AR8. | Comparative classification places IPMI in the aconitase family and associates its chemistry with an iron–sulfur-containing scaffold (binder2010branchedchainaminoacid pages 6-7). |
| Cofactor status | Aconitase-family chemistry predicts an iron–sulfur requirement, and the IPMI large subunit has been described as the Fe–S-bearing component. However, direct spectroscopic demonstration or cluster-transfer reconstitution for Arabidopsis IIL1 remains limited; its proposed interaction with plastidial NFU1 was not conclusively established. | Fe–S attribution is supported by homology and interaction-screen context, but the specific NFU1–IIL1 relationship remains tentative (roland2020theplastidialarabidopsis pages 4-6, roland2020theplastidialarabidopsis pages 6-7, roland2020theplastidialarabidopsis pages 20-22). |
| Primary biochemical pathway | IIL1 participates in **plastidial leucine biosynthesis**, connecting the valine-derived precursor 3-methyl-2-oxobutanoate to leucine through the IPMS–IPMI–IPMDH reaction sequence. | Mutants accumulate 2-isopropylmalate and may show increased valine even when bulk leucine remains buffered (binder2010branchedchainaminoacid pages 6-7, knill2009arabidopsisthalianaencodes pages 8-10, knill2009arabidopsisthalianaencodes pages 4-6). |
| Specialized biochemical pathway | IIL1 also functions in the repeated **methionine side-chain elongation cycles** that generate precursors for aliphatic glucosinolates. It is therefore a biochemical bridge between primary branched-chain amino-acid metabolism and Brassicales specialized defense metabolism. | Large-subunit mutants accumulate pathway intermediates and display altered aliphatic-glucosinolate chain-length distributions (knill2009arabidopsisthalianaencodes pages 10-12, knill2009arabidopsisthalianaencodes pages 1-2). |
| Subcellular localization | The functional site is **plastidial**, including chloroplasts and likely specialized non-green plastids depending on the small-subunit partner and tissue. IIL1 possesses an inferred N-terminal plastid-targeting extension, but the strongest direct imaging evidence concerns its small-subunit partners rather than an LSU1–GFP fusion. | Transit-peptide analysis supports plastid targeting; GFP studies place SSU2 in chloroplasts and other SSUs in distinct plastid classes (knill2009arabidopsisthalianaencodes pages 2-4, knill2009arabidopsisthalianaencodes pages 7-8, lachler2020inarabidopsisthaliana pages 6-8, lachler2020inarabidopsisthaliana pages 1-2). |
| Genetic evidence | Independent hypomorphic or knockout alleles show reduced IIL1 expression, accumulation of leucine- and methionine-chain-elongation intermediates, and altered glucosinolate profiles. The strongest alleles can delay development. | Multiple alleles produced allele-dependent metabolic and developmental phenotypes (knill2009arabidopsisthalianaencodes pages 10-12, knill2009arabidopsisthalianaencodes pages 8-10, knill2009arabidopsisthalianaencodes pages 4-6). |
| Quantitative mutant metabolite evidence | In reported LSU1 mutants, methionine was approximately **twofold higher** in stronger lines; one strong allele accumulated about **0.42 mg 2-isopropylmalate per g dry weight**, compared with approximately **0.02 mg/g** in another allele and no detectable amount in a weaker line. | These measurements demonstrate allele-dependent impairment of pathway flux (knill2009arabidopsisthalianaencodes pages 4-6, knill2009arabidopsisthalianaencodes pages 6-7). |
| Glucosinolate-chain-length evidence | Stronger atleuc1/iil1 alleles reduce long-chain **C7–C8** methionine-derived glucosinolates, decrease several C4–C6 products, and increase C3 species, consistent with inefficient repeated side-chain elongation. Tryptophan-derived glucosinolates are comparatively unaffected. | Targeted glucosinolate profiling in independent knockout lines supports specificity for methionine-derived products (knill2009arabidopsisthalianaencodes pages 7-8, knill2009arabidopsisthalianaencodes pages 10-12, sawada2009omicsbasedapproachesto pages 2-4). |
| Regulatory evidence | AtLeuC1/IIL1 is coexpressed with methionine-derived glucosinolate biosynthetic genes and is coordinately regulated by the aliphatic-glucosinolate regulator **MYB28/HAG1**, reinforcing its assignment to the chain-elongation module. | Coexpression and regulatory evidence complements mutant metabolomics (sawada2009omicsbasedapproachesto pages 2-4). |
| Recent developmental finding | A 2023 preprint linked temperature-sensitive leaf defects in the Bur-0 accession to expanded intronic TTC repeats, IIL1 silencing, and enrichment of intron-retained transcripts. Affected leaves contained about **25–39.1%** retained transcripts, versus below **1–6%** in controls. Because this evidence was reported as a preprint, it should be interpreted cautiously. | The phenotype depended on transcript imbalance rather than simple IIL1 reduction alone and was suppressed by increasing normal IIL1 transcript abundance (li2023intronictnrretainedisopropylmalate pages 12-15). |
| Overall annotation confidence | The dual role of IIL1 in leucine synthesis and methionine-derived glucosinolate precursor formation is supported strongly by independent genetics, metabolomics, coexpression, pathway conservation, and plastid-localization evidence. Remaining uncertainties concern direct purified-holoenzyme kinetics, LSU1-specific imaging, and direct characterization of its Fe–S cofactor. | Convergent evidence supports the core annotation while distinguishing experimentally established findings from family-based inference (knill2009arabidopsisthalianaencodes pages 8-10, knill2009arabidopsisthalianaencodes pages 10-12, sawada2009omicsbasedapproachesto pages 2-4, roland2020theplastidialarabidopsis pages 6-7). |


*Table: This table integrates the identity, reactions, substrate range, pathway roles, localization, structural features, and experimental evidence for Arabidopsis IIL1/IPMI LSU1. It also flags where conclusions rely on direct experiments versus family-based inference.*

References

1. (knill2009arabidopsisthalianaencodes pages 2-4): Tanja Knill, Michael Reichelt, Christian Paetz, Jonathan Gershenzon, and Stefan Binder. Arabidopsis thaliana encodes a bacterial-type heterodimeric isopropylmalate isomerase involved in both leu biosynthesis and the met chain elongation pathway of glucosinolate formation. Plant Molecular Biology, 71:227-239, Jul 2009. URL: https://doi.org/10.1007/s11103-009-9519-5, doi:10.1007/s11103-009-9519-5. This article has 103 citations and is from a peer-reviewed journal.

2. (sawada2009omicsbasedapproachesto pages 1-2): Yuji Sawada, Ayuko Kuwahara, Mutsumi Nagano, Tomoko Narisawa, Akane Sakata, Kazuki Saito, and Masami Yokota Hirai. Omics-based approaches to methionine side chain elongation in arabidopsis: characterization of the genes encoding methylthioalkylmalate isomerase and methylthioalkylmalate dehydrogenase. Plant & cell physiology, 50 7:1181-90, Jul 2009. URL: https://doi.org/10.1093/pcp/pcp079, doi:10.1093/pcp/pcp079. This article has 128 citations and is from a domain leading peer-reviewed journal.

3. (sawada2009omicsbasedapproachesto pages 2-4): Yuji Sawada, Ayuko Kuwahara, Mutsumi Nagano, Tomoko Narisawa, Akane Sakata, Kazuki Saito, and Masami Yokota Hirai. Omics-based approaches to methionine side chain elongation in arabidopsis: characterization of the genes encoding methylthioalkylmalate isomerase and methylthioalkylmalate dehydrogenase. Plant & cell physiology, 50 7:1181-90, Jul 2009. URL: https://doi.org/10.1093/pcp/pcp079, doi:10.1093/pcp/pcp079. This article has 128 citations and is from a domain leading peer-reviewed journal.

4. (binder2010branchedchainaminoacid pages 6-7): Stefan Binder. Branched-chain amino acid metabolism in arabidopsis thaliana. The Arabidopsis Book, 2010:e0137, Jan 2010. URL: https://doi.org/10.1199/tab.0137, doi:10.1199/tab.0137. This article has 313 citations and is from a peer-reviewed journal.

5. (knill2009arabidopsisthalianaencodes pages 1-2): Tanja Knill, Michael Reichelt, Christian Paetz, Jonathan Gershenzon, and Stefan Binder. Arabidopsis thaliana encodes a bacterial-type heterodimeric isopropylmalate isomerase involved in both leu biosynthesis and the met chain elongation pathway of glucosinolate formation. Plant Molecular Biology, 71:227-239, Jul 2009. URL: https://doi.org/10.1007/s11103-009-9519-5, doi:10.1007/s11103-009-9519-5. This article has 103 citations and is from a peer-reviewed journal.

6. (knill2009arabidopsisthalianaencodes pages 8-10): Tanja Knill, Michael Reichelt, Christian Paetz, Jonathan Gershenzon, and Stefan Binder. Arabidopsis thaliana encodes a bacterial-type heterodimeric isopropylmalate isomerase involved in both leu biosynthesis and the met chain elongation pathway of glucosinolate formation. Plant Molecular Biology, 71:227-239, Jul 2009. URL: https://doi.org/10.1007/s11103-009-9519-5, doi:10.1007/s11103-009-9519-5. This article has 103 citations and is from a peer-reviewed journal.

7. (knill2009arabidopsisthalianaencodes pages 7-8): Tanja Knill, Michael Reichelt, Christian Paetz, Jonathan Gershenzon, and Stefan Binder. Arabidopsis thaliana encodes a bacterial-type heterodimeric isopropylmalate isomerase involved in both leu biosynthesis and the met chain elongation pathway of glucosinolate formation. Plant Molecular Biology, 71:227-239, Jul 2009. URL: https://doi.org/10.1007/s11103-009-9519-5, doi:10.1007/s11103-009-9519-5. This article has 103 citations and is from a peer-reviewed journal.

8. (lachler2020inarabidopsisthaliana pages 1-2): Kurt Lächler, Karen Clauss, Janet Imhof, Christoph Crocoll, Alexander Schulz, Barbara Ann Halkier, and Stefan Binder. In arabidopsis thaliana substrate recognition and tissue- as well as plastid type-specific expression define the roles of distinct small subunits of isopropylmalate isomerase. Frontiers in Plant Science, Jun 2020. URL: https://doi.org/10.3389/fpls.2020.00808, doi:10.3389/fpls.2020.00808. This article has 7 citations.

9. (imhof2014thesmallsubunit pages 9-10): Janet Imhof, Florian Huber, Michael Reichelt, Jonathan Gershenzon, Christoph Wiegreffe, Kurt Lächler, and Stefan Binder. The small subunit 1 of the arabidopsis isopropylmalate isomerase is required for normal growth and development and the early stages of glucosinolate formation. PLoS ONE, 9:e91071, Mar 2014. URL: https://doi.org/10.1371/journal.pone.0091071, doi:10.1371/journal.pone.0091071. This article has 27 citations and is from a peer-reviewed journal.

10. (imhof2014thesmallsubunit pages 7-8): Janet Imhof, Florian Huber, Michael Reichelt, Jonathan Gershenzon, Christoph Wiegreffe, Kurt Lächler, and Stefan Binder. The small subunit 1 of the arabidopsis isopropylmalate isomerase is required for normal growth and development and the early stages of glucosinolate formation. PLoS ONE, 9:e91071, Mar 2014. URL: https://doi.org/10.1371/journal.pone.0091071, doi:10.1371/journal.pone.0091071. This article has 27 citations and is from a peer-reviewed journal.

11. (lachler2020inarabidopsisthaliana pages 6-8): Kurt Lächler, Karen Clauss, Janet Imhof, Christoph Crocoll, Alexander Schulz, Barbara Ann Halkier, and Stefan Binder. In arabidopsis thaliana substrate recognition and tissue- as well as plastid type-specific expression define the roles of distinct small subunits of isopropylmalate isomerase. Frontiers in Plant Science, Jun 2020. URL: https://doi.org/10.3389/fpls.2020.00808, doi:10.3389/fpls.2020.00808. This article has 7 citations.

12. (knill2009arabidopsisthalianaencodes pages 4-6): Tanja Knill, Michael Reichelt, Christian Paetz, Jonathan Gershenzon, and Stefan Binder. Arabidopsis thaliana encodes a bacterial-type heterodimeric isopropylmalate isomerase involved in both leu biosynthesis and the met chain elongation pathway of glucosinolate formation. Plant Molecular Biology, 71:227-239, Jul 2009. URL: https://doi.org/10.1007/s11103-009-9519-5, doi:10.1007/s11103-009-9519-5. This article has 103 citations and is from a peer-reviewed journal.

13. (knill2009arabidopsisthalianaencodes pages 10-12): Tanja Knill, Michael Reichelt, Christian Paetz, Jonathan Gershenzon, and Stefan Binder. Arabidopsis thaliana encodes a bacterial-type heterodimeric isopropylmalate isomerase involved in both leu biosynthesis and the met chain elongation pathway of glucosinolate formation. Plant Molecular Biology, 71:227-239, Jul 2009. URL: https://doi.org/10.1007/s11103-009-9519-5, doi:10.1007/s11103-009-9519-5. This article has 103 citations and is from a peer-reviewed journal.

14. (roland2020theplastidialarabidopsis pages 4-6): Mélanie Roland, Jonathan Przybyla-Toscano, Florence Vignols, Nathalie Berger, Tamanna Azam, Loick Christ, Véronique Santoni, Hui-Chen Wu, Tiphaine Dhalleine, Michael K. Johnson, Christian Dubos, Jérémy Couturier, and Nicolas Rouhier. The plastidial arabidopsis thaliana nfu1 protein binds and delivers [4fe-4s] clusters to specific client proteins. Journal of Biological Chemistry, 295(6):1727-1742, Feb 2020. URL: https://doi.org/10.1074/jbc.ra119.011034, doi:10.1074/jbc.ra119.011034. This article has 33 citations and is from a domain leading peer-reviewed journal.

15. (roland2020theplastidialarabidopsis pages 6-7): Mélanie Roland, Jonathan Przybyla-Toscano, Florence Vignols, Nathalie Berger, Tamanna Azam, Loick Christ, Véronique Santoni, Hui-Chen Wu, Tiphaine Dhalleine, Michael K. Johnson, Christian Dubos, Jérémy Couturier, and Nicolas Rouhier. The plastidial arabidopsis thaliana nfu1 protein binds and delivers [4fe-4s] clusters to specific client proteins. Journal of Biological Chemistry, 295(6):1727-1742, Feb 2020. URL: https://doi.org/10.1074/jbc.ra119.011034, doi:10.1074/jbc.ra119.011034. This article has 33 citations and is from a domain leading peer-reviewed journal.

16. (roland2020theplastidialarabidopsis pages 8-9): Mélanie Roland, Jonathan Przybyla-Toscano, Florence Vignols, Nathalie Berger, Tamanna Azam, Loick Christ, Véronique Santoni, Hui-Chen Wu, Tiphaine Dhalleine, Michael K. Johnson, Christian Dubos, Jérémy Couturier, and Nicolas Rouhier. The plastidial arabidopsis thaliana nfu1 protein binds and delivers [4fe-4s] clusters to specific client proteins. Journal of Biological Chemistry, 295(6):1727-1742, Feb 2020. URL: https://doi.org/10.1074/jbc.ra119.011034, doi:10.1074/jbc.ra119.011034. This article has 33 citations and is from a domain leading peer-reviewed journal.

17. (roland2020theplastidialarabidopsis pages 20-22): Mélanie Roland, Jonathan Przybyla-Toscano, Florence Vignols, Nathalie Berger, Tamanna Azam, Loick Christ, Véronique Santoni, Hui-Chen Wu, Tiphaine Dhalleine, Michael K. Johnson, Christian Dubos, Jérémy Couturier, and Nicolas Rouhier. The plastidial arabidopsis thaliana nfu1 protein binds and delivers [4fe-4s] clusters to specific client proteins. Journal of Biological Chemistry, 295(6):1727-1742, Feb 2020. URL: https://doi.org/10.1074/jbc.ra119.011034, doi:10.1074/jbc.ra119.011034. This article has 33 citations and is from a domain leading peer-reviewed journal.

18. (knill2009arabidopsisthalianaencodes pages 6-7): Tanja Knill, Michael Reichelt, Christian Paetz, Jonathan Gershenzon, and Stefan Binder. Arabidopsis thaliana encodes a bacterial-type heterodimeric isopropylmalate isomerase involved in both leu biosynthesis and the met chain elongation pathway of glucosinolate formation. Plant Molecular Biology, 71:227-239, Jul 2009. URL: https://doi.org/10.1007/s11103-009-9519-5, doi:10.1007/s11103-009-9519-5. This article has 103 citations and is from a peer-reviewed journal.

19. (imhof2014thesmallsubunit pages 4-5): Janet Imhof, Florian Huber, Michael Reichelt, Jonathan Gershenzon, Christoph Wiegreffe, Kurt Lächler, and Stefan Binder. The small subunit 1 of the arabidopsis isopropylmalate isomerase is required for normal growth and development and the early stages of glucosinolate formation. PLoS ONE, 9:e91071, Mar 2014. URL: https://doi.org/10.1371/journal.pone.0091071, doi:10.1371/journal.pone.0091071. This article has 27 citations and is from a peer-reviewed journal.

20. (li2023intronictnrretainedisopropylmalate pages 12-15): Yimeng Li, Rui Li, Kensuke Kawade, Muneo Sato, Ayuko Kuwahara, Ryosuke Sasaki, Akira Oikawa, Hirokazu Tsukaya, and Masami Yokota Hirai. Intronic tnr-retained isopropylmalate isomerase large subunit1 transcripts impair leaf development in arabidopsis. bioRxiv, Mar 2023. URL: https://doi.org/10.1101/2023.03.24.534132, doi:10.1101/2023.03.24.534132. This article has 0 citations.

21. (imhof2014thesmallsubunit pages 8-9): Janet Imhof, Florian Huber, Michael Reichelt, Jonathan Gershenzon, Christoph Wiegreffe, Kurt Lächler, and Stefan Binder. The small subunit 1 of the arabidopsis isopropylmalate isomerase is required for normal growth and development and the early stages of glucosinolate formation. PLoS ONE, 9:e91071, Mar 2014. URL: https://doi.org/10.1371/journal.pone.0091071, doi:10.1371/journal.pone.0091071. This article has 27 citations and is from a peer-reviewed journal.

22. (lachler2020inarabidopsisthaliana pages 8-10): Kurt Lächler, Karen Clauss, Janet Imhof, Christoph Crocoll, Alexander Schulz, Barbara Ann Halkier, and Stefan Binder. In arabidopsis thaliana substrate recognition and tissue- as well as plastid type-specific expression define the roles of distinct small subunits of isopropylmalate isomerase. Frontiers in Plant Science, Jun 2020. URL: https://doi.org/10.3389/fpls.2020.00808, doi:10.3389/fpls.2020.00808. This article has 7 citations.

## Artifacts

- [Edison artifact artifact-00](IIL1-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. binder2010branchedchainaminoacid pages 6-7
2. knill2009arabidopsisthalianaencodes pages 1-2
3. knill2009arabidopsisthalianaencodes pages 2-4
4. sawada2009omicsbasedapproachesto pages 2-4
5. knill2009arabidopsisthalianaencodes pages 4-6
6. imhof2014thesmallsubunit pages 4-5
7. li2023intronictnrretainedisopropylmalate pages 12-15
8. imhof2014thesmallsubunit pages 9-10
9. knill2009arabidopsisthalianaencodes pages 7-8
10. sawada2009omicsbasedapproachesto pages 1-2
11. knill2009arabidopsisthalianaencodes pages 8-10
12. lachler2020inarabidopsisthaliana pages 1-2
13. imhof2014thesmallsubunit pages 7-8
14. lachler2020inarabidopsisthaliana pages 6-8
15. knill2009arabidopsisthalianaencodes pages 10-12
16. roland2020theplastidialarabidopsis pages 4-6
17. roland2020theplastidialarabidopsis pages 6-7
18. roland2020theplastidialarabidopsis pages 8-9
19. roland2020theplastidialarabidopsis pages 20-22
20. knill2009arabidopsisthalianaencodes pages 6-7
21. imhof2014thesmallsubunit pages 8-9
22. lachler2020inarabidopsisthaliana pages 8-10
23. 4Fe-4S
24. 4fe-4s
25. https://doi.org/10.1007/s11103-009-9519-5,
26. https://doi.org/10.1093/pcp/pcp079,
27. https://doi.org/10.1199/tab.0137,
28. https://doi.org/10.3389/fpls.2020.00808,
29. https://doi.org/10.1371/journal.pone.0091071,
30. https://doi.org/10.1074/jbc.ra119.011034,
31. https://doi.org/10.1101/2023.03.24.534132,