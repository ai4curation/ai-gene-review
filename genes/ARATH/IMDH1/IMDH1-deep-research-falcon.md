---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-30T05:59:35.685003'
end_time: '2026-09-30T06:13:25.097427'
duration_seconds: 829.41
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: ARATH
  gene_id: IMDH1
  gene_symbol: IMDH1
  uniprot_accession: Q9FMT1
  protein_description: 'RecName: Full=3-isopropylmalate dehydrogenase 1, chloroplastic
    {ECO:0000303|PubMed:15849421}; Short=3-IPM-DH 1 {ECO:0000303|PubMed:15849421};
    Short=AtIMDH1 {ECO:0000303|PubMed:15849421, ECO:0000303|PubMed:19674406}; Short=IMDH
    1 {ECO:0000303|PubMed:15849421}; EC=1.1.1.85 {ECO:0000269|PubMed:15849421, ECO:0000269|PubMed:19674406,
    ECO:0000269|PubMed:20840499}; AltName: Full=Beta-IPM dehydrogenase 1 {ECO:0000303|PubMed:15849421};
    AltName: Full=Isopropylmalate dehydrogenase 1 {ECO:0000303|PubMed:19493961}; Short=AtIMD1
    {ECO:0000303|PubMed:19493961}; AltName: Full=Methylthioalkylmalate dehydrogenase
    1 {ECO:0000303|PubMed:19493961}; Flags: Precursor;'
  gene_info: Name=IMDH1 {ECO:0000303|PubMed:15849421}; Synonyms=IMD1 {ECO:0000303|PubMed:19493961},
    IPMDH1 {ECO:0000303|PubMed:20840499}, MAM-D1 {ECO:0000303|PubMed:19493961}; OrderedLocusNames=At5g14200
    {ECO:0000312|Araport:AT5G14200}; ORFNames=MUA22.20 {ECO:0000312|EMBL:BAB08299.1};
  organism_full: Arabidopsis thaliana (Mouse-ear cress).
  protein_family: Belongs to the isocitrate and isopropylmalate
  protein_domains: IsoCit/isopropylmalate_DH_CS. (IPR019818); IsoPropMal-DH-like_dom.
    (IPR024084); Isopropylmalate_DH. (IPR004429); Iso_dh (PF00180)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 27
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: IMDH1-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q9FMT1
- **Protein Description:** RecName: Full=3-isopropylmalate dehydrogenase 1, chloroplastic {ECO:0000303|PubMed:15849421}; Short=3-IPM-DH 1 {ECO:0000303|PubMed:15849421}; Short=AtIMDH1 {ECO:0000303|PubMed:15849421, ECO:0000303|PubMed:19674406}; Short=IMDH 1 {ECO:0000303|PubMed:15849421}; EC=1.1.1.85 {ECO:0000269|PubMed:15849421, ECO:0000269|PubMed:19674406, ECO:0000269|PubMed:20840499}; AltName: Full=Beta-IPM dehydrogenase 1 {ECO:0000303|PubMed:15849421}; AltName: Full=Isopropylmalate dehydrogenase 1 {ECO:0000303|PubMed:19493961}; Short=AtIMD1 {ECO:0000303|PubMed:19493961}; AltName: Full=Methylthioalkylmalate dehydrogenase 1 {ECO:0000303|PubMed:19493961}; Flags: Precursor;
- **Gene Information:** Name=IMDH1 {ECO:0000303|PubMed:15849421}; Synonyms=IMD1 {ECO:0000303|PubMed:19493961}, IPMDH1 {ECO:0000303|PubMed:20840499}, MAM-D1 {ECO:0000303|PubMed:19493961}; OrderedLocusNames=At5g14200 {ECO:0000312|Araport:AT5G14200}; ORFNames=MUA22.20 {ECO:0000312|EMBL:BAB08299.1};
- **Organism (full):** Arabidopsis thaliana (Mouse-ear cress).
- **Protein Family:** Belongs to the isocitrate and isopropylmalate
- **Key Domains:** IsoCit/isopropylmalate_DH_CS. (IPR019818); IsoPropMal-DH-like_dom. (IPR024084); Isopropylmalate_DH. (IPR004429); Iso_dh (PF00180)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "IMDH1" matches the protein description above**
2. **Verify the organism is correct:** Arabidopsis thaliana (Mouse-ear cress).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'IMDH1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **IMDH1** (gene ID: IMDH1, UniProt: Q9FMT1) in ARATH.

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
- **UniProt Accession:** Q9FMT1
- **Protein Description:** RecName: Full=3-isopropylmalate dehydrogenase 1, chloroplastic {ECO:0000303|PubMed:15849421}; Short=3-IPM-DH 1 {ECO:0000303|PubMed:15849421}; Short=AtIMDH1 {ECO:0000303|PubMed:15849421, ECO:0000303|PubMed:19674406}; Short=IMDH 1 {ECO:0000303|PubMed:15849421}; EC=1.1.1.85 {ECO:0000269|PubMed:15849421, ECO:0000269|PubMed:19674406, ECO:0000269|PubMed:20840499}; AltName: Full=Beta-IPM dehydrogenase 1 {ECO:0000303|PubMed:15849421}; AltName: Full=Isopropylmalate dehydrogenase 1 {ECO:0000303|PubMed:19493961}; Short=AtIMD1 {ECO:0000303|PubMed:19493961}; AltName: Full=Methylthioalkylmalate dehydrogenase 1 {ECO:0000303|PubMed:19493961}; Flags: Precursor;
- **Gene Information:** Name=IMDH1 {ECO:0000303|PubMed:15849421}; Synonyms=IMD1 {ECO:0000303|PubMed:19493961}, IPMDH1 {ECO:0000303|PubMed:20840499}, MAM-D1 {ECO:0000303|PubMed:19493961}; OrderedLocusNames=At5g14200 {ECO:0000312|Araport:AT5G14200}; ORFNames=MUA22.20 {ECO:0000312|EMBL:BAB08299.1};
- **Organism (full):** Arabidopsis thaliana (Mouse-ear cress).
- **Protein Family:** Belongs to the isocitrate and isopropylmalate
- **Key Domains:** IsoCit/isopropylmalate_DH_CS. (IPR019818); IsoPropMal-DH-like_dom. (IPR024084); Isopropylmalate_DH. (IPR004429); Iso_dh (PF00180)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "IMDH1" matches the protein description above**
2. **Verify the organism is correct:** Arabidopsis thaliana (Mouse-ear cress).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'IMDH1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **IMDH1** (gene ID: IMDH1, UniProt: Q9FMT1) in ARATH.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: IMDH1 (3-Isopropylmalate Dehydrogenase 1) in Arabidopsis thaliana

## Gene Identity and Nomenclature

IMDH1 (gene locus At5g14200, UniProt accession Q9FMT1) encodes 3-isopropylmalate dehydrogenase 1, a chloroplast-localized enzyme in *Arabidopsis thaliana* (binder2010branchedchainaminoacid pages 7-8). The gene is also designated AtIMD1, AtIPMDH1, MAM-D1, or IPMDH1 in the literature, reflecting its dual roles in primary and specialized metabolism (binder2010branchedchainaminoacid pages 7-8, sawada2009omicsbasedapproachesto pages 2-4, sawada2009omicsbasedapproachesto pages 1-2). This nomenclature can be confusing, but all these designations refer to the same protein encoded by At5g14200, as confirmed by multiple independent studies (binder2010branchedchainaminoacid pages 7-8, sawada2009omicsbasedapproachesto pages 2-4).

## Primary Enzymatic Function and Substrate Specificity

### Catalyzed Reaction

IMDH1 is classified as EC 1.1.1.85 and catalyzes an NAD⁺-dependent oxidative decarboxylation reaction (binder2010branchedchainaminoacid pages 7-8). The enzyme acts on 3-malate derivatives, converting them to the corresponding chain-elongated 2-oxo acids with concomitant release of CO₂ and production of NADH (binder2010branchedchainaminoacid pages 7-8, lachler2020inarabidopsisthaliana pages 1-2).

### Dual Substrate Specificity

IMDH1 exhibits dual substrate specificity, reflecting its functions in both primary and specialized metabolism:

**Leucine Biosynthesis Substrate:** In the leucine biosynthetic pathway, IMDH1 catalyzes the oxidative decarboxylation of 3-isopropylmalate (3-IPM) to produce 4-methyl-2-oxopentanoate (4MOP, also known as α-ketoisocaproate), the penultimate step before leucine formation (binder2010branchedchainaminoacid pages 7-8). Recombinant IMDH1 demonstrates high catalytic activity with 3-IPM as substrate (binder2010branchedchainaminoacid pages 7-8).

**Glucosinolate Biosynthesis Substrate:** IMDH1 also accepts methylthioalkylmalate intermediates, particularly 3-(2'-methylthio)ethylmalate, as substrates in the methionine side-chain elongation pathway (leong2017promiscuityimpersonationand pages 2-3, leong2017promiscuityimpersonationand pages 1-2). The enzyme performs the same oxidative decarboxylation chemistry on these structurally related compounds, producing one-carbon-elongated 2-oxo acids used in iterative methionine chain elongation (leong2017promiscuityimpersonationand pages 1-2, lachler2020inarabidopsisthaliana pages 1-2).

### Structural Determinants of Substrate Preference

The substrate preference of IMDH1 is primarily determined by a critical amino acid substitution at position 137. IMDH1 contains a phenylalanine at this position (L137F mutation relative to ancestral leucine-biosynthetic enzymes), which reshapes the hydrophobic portion of the active-site pocket to better accommodate the longer methylthioethyl side chain of glucosinolate precursors (leong2017promiscuityimpersonationand pages 2-3). Both 3-IPM and methylthioalkylmalates share the same carboxyl and hydroxyl group configuration, allowing recognition by conserved polar-binding residues, while the L137F substitution alters discrimination between the different aliphatic side chains (leong2017promiscuityimpersonationand pages 2-3, leong2017promiscuityimpersonationand pages 1-2). Reciprocal substitution experiments demonstrated that this single amino acid change can shift catalytic efficiency between native and alternative substrates (leong2017promiscuityimpersonationand pages 2-3).

While IMDH1 retains measurable 3-IPM activity and can support leucine synthesis, its principal specialization in *Arabidopsis* is toward methylthioalkylmalates and the formation of C4–C8 methionine-derived glucosinolates (binder2010branchedchainaminoacid pages 7-8, kitainda2021structuralstudiesof pages 6-8). The related paralogs IMDH2 and IMDH3 are more exclusively dedicated to leucine biosynthesis (binder2010branchedchainaminoacid pages 7-8).

## Biochemical Pathways

### Primary Metabolism: Leucine Biosynthesis

IMDH1 participates in branched-chain amino acid (BCAA) metabolism, specifically in the leucine biosynthetic pathway (binder2010branchedchainaminoacid pages 7-8, binder2010branchedchainaminoacid pages 1-3). Leucine biosynthesis branches from the valine pathway and requires a series of enzymatic transformations. IMDH1 catalyzes the penultimate step, converting 3-isopropylmalate to 4-methyl-2-oxopentanoate, which is subsequently transaminated to produce leucine (binder2010branchedchainaminoacid pages 7-8).

Evidence for this function includes: (1) high recombinant enzyme activity with 3-IPM substrate (binder2010branchedchainaminoacid pages 7-8), (2) decreased free leucine levels in *imdh1* loss-of-function mutants (binder2010branchedchainaminoacid pages 7-8), and (3) ability of IMDH1 to complement leucine-auxotrophic bacteria and yeast (kitainda2021structuralstudiesof pages 6-8).

### Specialized Metabolism: Aliphatic Glucosinolate Biosynthesis

IMDH1 plays a particularly important role in the methionine side-chain elongation cycle, which supplies precursors for methionine-derived aliphatic glucosinolate biosynthesis (binder2010branchedchainaminoacid pages 7-8, sawada2009omicsbasedapproachesto pages 1-2, sawada2009omicsbasedapproachesto pages 2-4). Glucosinolates are sulfur-containing specialized metabolites characteristic of Brassicales plants, serving as defense compounds against herbivores and pathogens.

The methionine chain-elongation cycle operates iteratively and consists of four enzymatic steps: (1) condensation of a methionine-derived 2-oxo acid with acetyl-CoA by methylthioalkylmalate synthase (MAM), (2) isomerization by isopropylmalate isomerase (IPMI), (3) oxidative decarboxylation by IMDH1, and (4) transamination to regenerate an elongated methionine derivative (sawada2009omicsbasedapproachesto pages 1-2, lachler2020inarabidopsisthaliana pages 1-2). This cycle can iterate multiple times, producing chain-elongated methionine derivatives with 3 to 8 carbons in the side chain, which determine the structural diversity of aliphatic glucosinolates (sawada2009omicsbasedapproachesto pages 2-4, binder2010branchedchainaminoacid pages 8-9).

The methionine chain-elongation pathway is mechanistically analogous to leucine biosynthesis, and IMDH1 represents a specialized enzyme recruited from the leucine pathway to support glucosinolate biosynthesis through gene duplication and functional divergence (sawada2009omicsbasedapproachesto pages 1-2, binder2010branchedchainaminoacid pages 9-10, leong2017promiscuityimpersonationand pages 1-2).

## Subcellular Localization

IMDH1 is localized to chloroplasts and other plastid types (takac2018shotgunproteomicanalysis pages 9-11, lachler2020inarabidopsisthaliana pages 1-2). This localization is consistent with the plastidial compartmentalization of both leucine biosynthesis and the methionine chain-elongation machinery (lachler2020inarabidopsisthaliana pages 1-2, mikkelsen2010productionofthe pages 3-4). 

Plastid localization is functionally significant for several reasons. First, both branched-chain amino acid biosynthesis and methionine chain elongation occur within plastids, where the relevant substrates and cofactors are available (mikkelsen2010productionofthe pages 3-4, lachler2020inarabidopsisthaliana pages 1-2). Second, compartmentalization in plastids improves metabolic flux by colocalizing all enzymes of the chain-elongation cycle, avoiding the need for transport of intermediates between compartments (mikkelsen2010productionofthe pages 3-4). Third, after chain elongation is complete in plastids, the elongated methionine derivatives are exported to the cytosol where the core glucosinolate structure is synthesized by a different set of enzymes (lachler2020inarabidopsisthaliana pages 15-16, lachler2020inarabidopsisthaliana pages 1-2).

Proteomic studies of *Arabidopsis* root plastids have identified IMDH1 (referred to as IMD1) among plastid-localized proteins involved in amino acid biosynthesis (takac2018shotgunproteomicanalysis pages 9-11). The tissue- and plastid-type-specific expression patterns of related pathway components suggest that different plastid populations may support either primary leucine biosynthesis or specialized glucosinolate precursor formation (lachler2020inarabidopsisthaliana pages 15-16, lachler2020inarabidopsisthaliana pages 12-14).

## Experimental Evidence

### Genetic and Mutant Studies

Loss-of-function studies provide strong functional evidence for IMDH1's dual roles. T-DNA insertion mutants of IMDH1 (*atimd1*) show:

**Leucine phenotype:** Reduced free leucine levels, confirming contribution to leucine biosynthesis, though leucine production is not completely abolished due to functional redundancy with IMDH2 and IMDH3 (binder2010branchedchainaminoacid pages 7-8, harun2021potentialarabidopsisthaliana pages 14-16).

**Glucosinolate phenotype:** Strong *atimd1* knockout mutants exhibit pronounced depletion of long-chain (C7–C8) methionine-derived glucosinolates, moderate reduction in C4–C6 glucosinolates, and elevated C3 glucosinolates (sawada2009omicsbasedapproachesto pages 2-4). This pattern indicates impaired iterative methionine chain elongation—IMDH1 is essential for multiple rounds of elongation required to generate longer-chain glucosinolate precursors (sawada2009omicsbasedapproachesto pages 2-4). Importantly, tryptophan-derived indolic glucosinolates remain largely unaffected, demonstrating pathway specificity (sawada2009omicsbasedapproachesto pages 2-4).

Weaker mutant alleles show similar but attenuated phenotypes, providing allelic evidence supporting these functional assignments (sawada2009omicsbasedapproachesto pages 2-4).

### Biochemical and Enzymatic Studies

Recombinant IMDH1 protein has been purified and characterized, demonstrating high catalytic activity with 3-isopropylmalate as substrate (binder2010branchedchainaminoacid pages 7-8). While detailed kinetic parameters are not extensively reported in the available literature, the enzyme's ability to complement leucine-auxotrophic microorganisms confirms its functional competence in leucine biosynthesis (kitainda2021structuralstudiesof pages 6-8).

### Structural and Molecular Studies

Structural analysis and site-directed mutagenesis have identified the L137F substitution as the key determinant of IMDH1's altered substrate preference (leong2017promiscuityimpersonationand pages 2-3). This residue is located in the hydrophobic portion of the active-site pocket, where it modulates accommodation of substrates with different side-chain lengths and compositions (leong2017promiscuityimpersonationand pages 2-3). The conserved polar-group binding interactions remain unchanged between IMDH1 and leucine-biosynthetic IPMDHs, explaining why both enzyme types can recognize the shared malate core structure (leong2017promiscuityimpersonationand pages 2-3).

### Bioinformatic and Co-expression Studies

IMDH1 was initially identified as a candidate methylthioalkylmalate dehydrogenase through transcriptome co-expression analysis (sawada2009omicsbasedapproachesto pages 2-4, sawada2009omicsbasedapproachesto pages 1-2). IMDH1 shows strong co-expression with established methionine-derived glucosinolate biosynthetic genes across multiple *Arabidopsis* datasets and environmental conditions (sawada2009omicsbasedapproachesto pages 2-4). This "perfect co-expression" with key methionine chain-elongation genes supports its functional integration into the glucosinolate biosynthetic network (binder2010branchedchainaminoacid pages 7-8).

### Evolutionary Evidence

Phylogenetic analysis reveals that IMDH1 shares 84–93% amino acid identity with the other *Arabidopsis* isopropylmalate dehydrogenases (IMDH2 and IMDH3) involved in leucine biosynthesis (leong2017promiscuityimpersonationand pages 1-2, binder2010branchedchainaminoacid pages 9-10). This high sequence similarity indicates that IMDH1 arose through gene duplication from an ancestral leucine-biosynthetic enzyme, followed by neofunctionalization for glucosinolate metabolism (leong2017promiscuityimpersonationand pages 1-2, sawada2009omicsbasedapproachesto pages 2-4). The enzyme represents a classic example of how specialized metabolic pathways evolve through recruitment and modification of primary metabolic enzymes (leong2017promiscuityimpersonationand pages 1-2).

## Transcriptional Regulation

IMDH1 expression is coordinately regulated with other methionine-derived glucosinolate biosynthetic genes (sawada2009omicsbasedapproachesto pages 2-4, binder2010branchedchainaminoacid pages 7-8). The gene is associated with the MYB28/PMG1/HAG1 positive-regulatory program, which serves as a master regulator of aliphatic glucosinolate biosynthesis (sawada2009omicsbasedapproachesto pages 2-4, sawada2009omicsbasedapproachesto pages 1-2). However, the available evidence derives primarily from co-expression and correlation analyses rather than direct demonstration of MYB28 binding to the IMDH1 promoter (sawada2009omicsbasedapproachesto pages 2-4, sawada2009omicsbasedapproachesto pages 1-2). This coordinated regulation allows plants to modulate glucosinolate biosynthetic capacity in response to environmental stimuli and developmental cues (sawada2009omicsbasedapproachesto pages 1-2).

## Summary and Functional Integration

IMDH1 represents a functionally bifurcated enzyme that bridges primary and specialized metabolism in *Arabidopsis thaliana*. The enzyme catalyzes NAD⁺-dependent oxidative decarboxylation of both 3-isopropylmalate (in leucine biosynthesis) and methylthioalkylmalate intermediates (in glucosinolate biosynthesis). Its chloroplast localization places it within the compartment where both pathways operate, facilitating efficient metabolic flux.

While IMDH1 retains ancestral leucine-biosynthetic activity and contributes to leucine production, its primary specialization in *Arabidopsis* appears to be toward methionine-derived glucosinolate biosynthesis. This specialization is evident from: (1) the L137F active-site substitution favoring methylthioalkylmalate substrates, (2) the particularly severe reduction in long-chain glucosinolates in *imdh1* mutants, (3) co-expression with glucosinolate genes, and (4) association with MYB28-mediated transcriptional regulation.

The existence of IMDH2 and IMDH3 as more dedicated leucine biosynthetic enzymes suggests evolutionary division of labor within the IPMDH gene family, allowing IMDH1 to acquire specialized glucosinolate-related functions while maintaining partial redundancy for the essential leucine biosynthetic function. This represents an elegant evolutionary solution that permits metabolic innovation while preserving primary metabolic capacity.

| Characteristic | IMDH1 annotation / evidence | Key sources |
|---|---|---|
| Identity | **IMDH1**; synonyms **AtIMD1, AtIPMDH1, MAM-D1**; ordered locus **At5g14200**; UniProt **Q9FMT1**; organism: *Arabidopsis thaliana*. The matching locus and aliases verify that the literature concerns the requested protein rather than a similarly named protein from another organism. | (binder2010branchedchainaminoacid pages 7-8, sawada2009omicsbasedapproachesto pages 2-4) |
| Enzyme classification | Chloroplast-targeted **3-isopropylmalate dehydrogenase 1** / methylthioalkylmalate dehydrogenase; **EC 1.1.1.85**; member of the isocitrate/isopropylmalate-dehydrogenase family. | (binder2010branchedchainaminoacid pages 7-8) |
| Reaction type | Catalyzes an **NAD⁺-dependent oxidative decarboxylation** of a 3-malate derivative, yielding the corresponding chain-elongated **2-oxo acid**, CO₂, and NADH. | (binder2010branchedchainaminoacid pages 7-8, lachler2020inarabidopsisthaliana pages 1-2, kitainda2021structuralstudiesof pages 6-8) |
| Leucine-pathway substrate and product | Converts **3-isopropylmalate (3-IPM)** to **4-methyl-2-oxopentanoate (4MOP; α-ketoisocaproate)**, the penultimate reaction of leucine biosynthesis; 4MOP is subsequently transaminated to leucine. | (binder2010branchedchainaminoacid pages 7-8) |
| Glucosinolate-pathway substrate and product | Accepts methylthioalkylmalate intermediates, notably **3-(2′-methylthio)ethylmalate**, and oxidatively decarboxylates them to the corresponding one-carbon-elongated **2-oxo acid** used in iterative methionine side-chain elongation. | (leong2017promiscuityimpersonationand pages 2-3, leong2017promiscuityimpersonationand pages 1-2, lachler2020inarabidopsisthaliana pages 1-2) |
| Substrate specificity | IMDH1 retains measurable 3-IPM activity and can support leucine synthesis, but its principal *Arabidopsis* specialization is toward methylthioalkylmalates and formation of **C4–C8 methionine-derived glucosinolates**; IMDH2 and IMDH3 are more dedicated to leucine biosynthesis. | (binder2010branchedchainaminoacid pages 7-8, kitainda2021structuralstudiesof pages 6-8) |
| Structural determinant | A key **Phe at position 137**—corresponding to an ancestral **Leu-to-Phe change (L137F)**—reshapes the hydrophobic substrate pocket and favors the longer methylthioethyl side chain. Reciprocal substitutions shift catalytic efficiency between 3-IPM and methylthioalkylmalate substrates. | (leong2017promiscuityimpersonationand pages 2-3) |
| Subcellular localization | **Chloroplast/plastid**. This localization places IMDH1 with the plastidial leucine-biosynthetic and methionine-chain-elongation machinery; glucosinolate precursors subsequently leave the plastid for downstream core-structure synthesis. | (takac2018shotgunproteomicanalysis pages 9-11, lachler2020inarabidopsisthaliana pages 1-2, mikkelsen2010productionofthe pages 3-4) |
| Primary-metabolism pathway | Participates in **branched-chain amino-acid metabolism**, specifically the penultimate step of **leucine biosynthesis**. Recombinant activity with 3-IPM and decreased free leucine in loss-of-function material support this assignment. | (binder2010branchedchainaminoacid pages 7-8) |
| Specialized-metabolism pathway | Functions in the **methionine side-chain elongation cycle**, upstream of methionine-derived **aliphatic glucosinolate** core synthesis. The cycle comprises condensation, isomerization, IMDH1-mediated oxidative decarboxylation, and transamination or another elongation round. | (sawada2009omicsbasedapproachesto pages 1-2, sawada2009omicsbasedapproachesto pages 2-4, lachler2020inarabidopsisthaliana pages 1-2) |
| Transcriptional regulation | IMDH1 is co-expressed with methionine-derived glucosinolate genes and is coordinately associated with the **MYB28/PMG1/HAG1** positive-regulatory program. Available evidence supports pathway-level regulation but does **not** by itself establish direct MYB28 binding to the IMDH1 promoter. | (sawada2009omicsbasedapproachesto pages 2-4, binder2010branchedchainaminoacid pages 7-8) |
| Evolutionary relationship | One of three closely related Arabidopsis IPMDHs, sharing approximately **84–93% amino-acid identity** with the family. Gene duplication and active-site divergence recruited IMDH1 from ancestral leucine metabolism into glucosinolate biosynthesis while retaining leucine-pathway activity. | (leong2017promiscuityimpersonationand pages 1-2, binder2010branchedchainaminoacid pages 9-10, sawada2009omicsbasedapproachesto pages 2-4) |
| Loss-of-function phenotype: leucine | Disruption of IMDH1 lowers **free leucine**, consistent with a non-exclusive contribution to leucine synthesis alongside IMDH2 and IMDH3. | (binder2010branchedchainaminoacid pages 7-8, harun2021potentialarabidopsisthaliana pages 14-16) |
| Loss-of-function phenotype: glucosinolates | Strong *atimd1* mutants show **pronounced depletion of C7–C8 methionine-derived glucosinolates**, smaller decreases in **C4–C6** compounds, and accumulation of **C3** glucosinolates; tryptophan-derived glucosinolates are largely unaffected. This pattern indicates impaired iterative methionine chain elongation rather than a general block in glucosinolate synthesis. | (sawada2009omicsbasedapproachesto pages 2-4) |
| Overall functional interpretation | IMDH1 is a **dual-function but specialized plastidial oxidative decarboxylase**: it contributes to primary leucine production while serving a particularly important role in generating elongated methionine-derived precursors that determine aliphatic-glucosinolate chain-length composition. | (binder2010branchedchainaminoacid pages 7-8, leong2017promiscuityimpersonationand pages 2-3, kitainda2021structuralstudiesof pages 6-8) |


*Table: This table consolidates identity, catalytic chemistry, substrate specificity, localization, pathway roles, regulation, evolutionary specialization, and mutant evidence for Arabidopsis IMDH1 (Q9FMT1). It also distinguishes direct evidence from pathway-level inference.*

## Key Research Papers and URLs

- **Binder (2010):** Comprehensive review of branched-chain amino acid metabolism in *Arabidopsis*. The Arabidopsis Book, DOI: 10.1199/tab.0137
  https://doi.org/10.1199/tab.0137

- **Sawada et al. (2009):** Omics-based characterization of methylthioalkylmalate isomerase and dehydrogenase. Plant and Cell Physiology, 50:1181-1190, DOI: 10.1093/pcp/pcp079
  https://doi.org/10.1093/pcp/pcp079

- **Leong and Last (2017):** Evolution of plant specialized metabolism through promiscuity and accommodation. Current Opinion in Structural Biology, 47:105-112, DOI: 10.1016/j.sbi.2017.07.005
  https://doi.org/10.1016/j.sbi.2017.07.005

- **Lächler et al. (2020):** Substrate recognition and tissue-specific expression of isopropylmalate isomerase small subunits. Frontiers in Plant Science, DOI: 10.3389/fpls.2020.00808
  https://doi.org/10.3389/fpls.2020.00808

- **Kitainda and Jez (2021):** Structural studies of aliphatic glucosinolate chain-elongation enzymes. Antioxidants, 10:1500, DOI: 10.3390/antiox10091500
  https://doi.org/10.3390/antiox10091500

This comprehensive analysis confirms that IMDH1 (At5g14200, UniProt Q9FMT1) is a well-characterized, dual-function enzyme with established roles in both primary leucine biosynthesis and specialized aliphatic glucosinolate metabolism in *Arabidopsis thaliana*.

References

1. (binder2010branchedchainaminoacid pages 7-8): Stefan Binder. Branched-chain amino acid metabolism in arabidopsis thaliana. The Arabidopsis Book, 2010:e0137, Jan 2010. URL: https://doi.org/10.1199/tab.0137, doi:10.1199/tab.0137. This article has 313 citations and is from a peer-reviewed journal.

2. (sawada2009omicsbasedapproachesto pages 2-4): Yuji Sawada, Ayuko Kuwahara, Mutsumi Nagano, Tomoko Narisawa, Akane Sakata, Kazuki Saito, and Masami Yokota Hirai. Omics-based approaches to methionine side chain elongation in arabidopsis: characterization of the genes encoding methylthioalkylmalate isomerase and methylthioalkylmalate dehydrogenase. Plant and Cell Physiology, 50:1181-1190, Jun 2009. URL: https://doi.org/10.1093/pcp/pcp079, doi:10.1093/pcp/pcp079. This article has 128 citations and is from a domain leading peer-reviewed journal.

3. (sawada2009omicsbasedapproachesto pages 1-2): Yuji Sawada, Ayuko Kuwahara, Mutsumi Nagano, Tomoko Narisawa, Akane Sakata, Kazuki Saito, and Masami Yokota Hirai. Omics-based approaches to methionine side chain elongation in arabidopsis: characterization of the genes encoding methylthioalkylmalate isomerase and methylthioalkylmalate dehydrogenase. Plant and Cell Physiology, 50:1181-1190, Jun 2009. URL: https://doi.org/10.1093/pcp/pcp079, doi:10.1093/pcp/pcp079. This article has 128 citations and is from a domain leading peer-reviewed journal.

4. (lachler2020inarabidopsisthaliana pages 1-2): Kurt Lächler, Karen Clauss, Janet Imhof, Christoph Crocoll, Alexander Schulz, Barbara Ann Halkier, and Stefan Binder. In arabidopsis thaliana substrate recognition and tissue- as well as plastid type-specific expression define the roles of distinct small subunits of isopropylmalate isomerase. Frontiers in Plant Science, Jun 2020. URL: https://doi.org/10.3389/fpls.2020.00808, doi:10.3389/fpls.2020.00808. This article has 7 citations.

5. (leong2017promiscuityimpersonationand pages 2-3): Bryan J Leong and Robert L Last. Promiscuity, impersonation and accommodation: evolution of plant specialized metabolism. Current opinion in structural biology, 47:105-112, Dec 2017. URL: https://doi.org/10.1016/j.sbi.2017.07.005, doi:10.1016/j.sbi.2017.07.005. This article has 72 citations and is from a peer-reviewed journal.

6. (leong2017promiscuityimpersonationand pages 1-2): Bryan J Leong and Robert L Last. Promiscuity, impersonation and accommodation: evolution of plant specialized metabolism. Current opinion in structural biology, 47:105-112, Dec 2017. URL: https://doi.org/10.1016/j.sbi.2017.07.005, doi:10.1016/j.sbi.2017.07.005. This article has 72 citations and is from a peer-reviewed journal.

7. (kitainda2021structuralstudiesof pages 6-8): Vivian Kitainda and Joseph M. Jez. Structural studies of aliphatic glucosinolate chain-elongation enzymes. Antioxidants, 10:1500, Sep 2021. URL: https://doi.org/10.3390/antiox10091500, doi:10.3390/antiox10091500. This article has 34 citations.

8. (binder2010branchedchainaminoacid pages 1-3): Stefan Binder. Branched-chain amino acid metabolism in arabidopsis thaliana. The Arabidopsis Book, 2010:e0137, Jan 2010. URL: https://doi.org/10.1199/tab.0137, doi:10.1199/tab.0137. This article has 313 citations and is from a peer-reviewed journal.

9. (binder2010branchedchainaminoacid pages 8-9): Stefan Binder. Branched-chain amino acid metabolism in arabidopsis thaliana. The Arabidopsis Book, 2010:e0137, Jan 2010. URL: https://doi.org/10.1199/tab.0137, doi:10.1199/tab.0137. This article has 313 citations and is from a peer-reviewed journal.

10. (binder2010branchedchainaminoacid pages 9-10): Stefan Binder. Branched-chain amino acid metabolism in arabidopsis thaliana. The Arabidopsis Book, 2010:e0137, Jan 2010. URL: https://doi.org/10.1199/tab.0137, doi:10.1199/tab.0137. This article has 313 citations and is from a peer-reviewed journal.

11. (takac2018shotgunproteomicanalysis pages 9-11): Shot-Gun Proteomic Analysis on Roots of Arabidopsis pldα1 Mutants Suggesting New Roles of PLDα1 in Mitochondrial Protein Import, Vesicular Trafficking and Glucosinolate Biosynthesis

12. (mikkelsen2010productionofthe pages 3-4): Michael Dalgaard Mikkelsen, Carl Erik Olsen, and Barbara Ann Halkier. Production of the cancer-preventive glucoraphanin in tobacco. Molecular plant, 3 4:751-9, Jul 2010. URL: https://doi.org/10.1093/mp/ssq020, doi:10.1093/mp/ssq020. This article has 95 citations and is from a highest quality peer-reviewed journal.

13. (lachler2020inarabidopsisthaliana pages 15-16): Kurt Lächler, Karen Clauss, Janet Imhof, Christoph Crocoll, Alexander Schulz, Barbara Ann Halkier, and Stefan Binder. In arabidopsis thaliana substrate recognition and tissue- as well as plastid type-specific expression define the roles of distinct small subunits of isopropylmalate isomerase. Frontiers in Plant Science, Jun 2020. URL: https://doi.org/10.3389/fpls.2020.00808, doi:10.3389/fpls.2020.00808. This article has 7 citations.

14. (lachler2020inarabidopsisthaliana pages 12-14): Kurt Lächler, Karen Clauss, Janet Imhof, Christoph Crocoll, Alexander Schulz, Barbara Ann Halkier, and Stefan Binder. In arabidopsis thaliana substrate recognition and tissue- as well as plastid type-specific expression define the roles of distinct small subunits of isopropylmalate isomerase. Frontiers in Plant Science, Jun 2020. URL: https://doi.org/10.3389/fpls.2020.00808, doi:10.3389/fpls.2020.00808. This article has 7 citations.

15. (harun2021potentialarabidopsisthaliana pages 14-16): Sarahani Harun, Nor Afiqah-Aleng, Mohammad Bozlul Karim, Md Altaf Ul Amin, Shigehiko Kanaya, and Zeti-Azura Mohamed-Hussein. Potential arabidopsis thaliana glucosinolate genes identified from the co-expression modules using graph clustering approach. PeerJ, 9:e11876, Aug 2021. URL: https://doi.org/10.7717/peerj.11876, doi:10.7717/peerj.11876. This article has 14 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](IMDH1-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. binder2010branchedchainaminoacid pages 7-8
2. leong2017promiscuityimpersonationand pages 2-3
3. kitainda2021structuralstudiesof pages 6-8
4. mikkelsen2010productionofthe pages 3-4
5. takac2018shotgunproteomicanalysis pages 9-11
6. sawada2009omicsbasedapproachesto pages 2-4
7. leong2017promiscuityimpersonationand pages 1-2
8. sawada2009omicsbasedapproachesto pages 1-2
9. lachler2020inarabidopsisthaliana pages 1-2
10. binder2010branchedchainaminoacid pages 1-3
11. binder2010branchedchainaminoacid pages 8-9
12. binder2010branchedchainaminoacid pages 9-10
13. lachler2020inarabidopsisthaliana pages 15-16
14. lachler2020inarabidopsisthaliana pages 12-14
15. harun2021potentialarabidopsisthaliana pages 14-16
16. https://doi.org/10.1199/tab.0137
17. https://doi.org/10.1093/pcp/pcp079
18. https://doi.org/10.1016/j.sbi.2017.07.005
19. https://doi.org/10.3389/fpls.2020.00808
20. https://doi.org/10.3390/antiox10091500
21. https://doi.org/10.1199/tab.0137,
22. https://doi.org/10.1093/pcp/pcp079,
23. https://doi.org/10.3389/fpls.2020.00808,
24. https://doi.org/10.1016/j.sbi.2017.07.005,
25. https://doi.org/10.3390/antiox10091500,
26. https://doi.org/10.1093/mp/ssq020,
27. https://doi.org/10.7717/peerj.11876,