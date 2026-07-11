---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-05T13:40:38.425841'
end_time: '2026-07-05T13:56:06.093810'
duration_seconds: 927.67
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: NAGS
  gene_symbol: NAGS
  uniprot_accession: Q8N159
  protein_description: 'RecName: Full=N-acetylglutamate synthase, mitochondrial; EC=2.3.1.1
    {ECO:0000269|PubMed:12459178, ECO:0000269|PubMed:23894642, ECO:0000269|PubMed:7126172};
    AltName: Full=Amino-acid acetyltransferase; Contains: RecName: Full=N-acetylglutamate
    synthase long form; Contains: RecName: Full=N-acetylglutamate synthase short form;
    Contains: RecName: Full=N-acetylglutamate synthase conserved domain form; Flags:
    Precursor;'
  gene_info: Name=NAGS;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the acetyltransferase family. .
  protein_domains: AceGlu_kinase-like_sf. (IPR036393); Acyl_CoA_acyltransferase. (IPR016181);
    Asp/Glu/Uridylate_kinase. (IPR001048); GlcNAc_Synth_met. (IPR011243); GNAT_dom.
    (IPR000182)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 45
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: NAGS-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q8N159
- **Protein Description:** RecName: Full=N-acetylglutamate synthase, mitochondrial; EC=2.3.1.1 {ECO:0000269|PubMed:12459178, ECO:0000269|PubMed:23894642, ECO:0000269|PubMed:7126172}; AltName: Full=Amino-acid acetyltransferase; Contains: RecName: Full=N-acetylglutamate synthase long form; Contains: RecName: Full=N-acetylglutamate synthase short form; Contains: RecName: Full=N-acetylglutamate synthase conserved domain form; Flags: Precursor;
- **Gene Information:** Name=NAGS;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the acetyltransferase family. .
- **Key Domains:** AceGlu_kinase-like_sf. (IPR036393); Acyl_CoA_acyltransferase. (IPR016181); Asp/Glu/Uridylate_kinase. (IPR001048); GlcNAc_Synth_met. (IPR011243); GNAT_dom. (IPR000182)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "NAGS" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'NAGS' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **NAGS** (gene ID: NAGS, UniProt: Q8N159) in human.

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
- **UniProt Accession:** Q8N159
- **Protein Description:** RecName: Full=N-acetylglutamate synthase, mitochondrial; EC=2.3.1.1 {ECO:0000269|PubMed:12459178, ECO:0000269|PubMed:23894642, ECO:0000269|PubMed:7126172}; AltName: Full=Amino-acid acetyltransferase; Contains: RecName: Full=N-acetylglutamate synthase long form; Contains: RecName: Full=N-acetylglutamate synthase short form; Contains: RecName: Full=N-acetylglutamate synthase conserved domain form; Flags: Precursor;
- **Gene Information:** Name=NAGS;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the acetyltransferase family. .
- **Key Domains:** AceGlu_kinase-like_sf. (IPR036393); Acyl_CoA_acyltransferase. (IPR016181); Asp/Glu/Uridylate_kinase. (IPR001048); GlcNAc_Synth_met. (IPR011243); GNAT_dom. (IPR000182)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "NAGS" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'NAGS' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **NAGS** (gene ID: NAGS, UniProt: Q8N159) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: Human NAGS (N-Acetylglutamate Synthase)

## Gene/Protein Identity Verification

The gene symbol **NAGS** unambiguously corresponds to human **N-acetylglutamate synthase, mitochondrial** (UniProt: Q8N159; EC 2.3.1.1; Ensembl: ENSG00000161653). The protein belongs to the acetyltransferase family and contains the expected amino acid kinase-like (AAK) and GNAT acetyltransferase (NAT) domains, consistent with the UniProt annotation. The literature is concordant with this identity.

The following table summarizes key properties of human NAGS:

| Property | Human NAGS summary |
|---|---|
| Gene symbol | **NAGS** (N-acetylglutamate synthase) (morizono2004mammaliannacetylglutamatesynthase. pages 1-2, caldovic2010nacetylglutamatesynthasestructure pages 1-2) |
| UniProt accession | **Q8N159** |
| EC number | **EC 2.3.1.1** (morizono2004mammaliannacetylglutamatesynthase. pages 1-2, caldovic2024dataminingapproachesfor pages 2-4) |
| Enzyme classification | **Acetyltransferase**; specifically an N-acetylglutamate synthase in the acetyltransferase family (shi2015thenacetylglutamatesynthase pages 1-3, caldovic2010nacetylglutamatesynthasestructure pages 1-2) |
| Reaction catalyzed | **L-glutamate + acetyl-CoA → N-acetylglutamate (NAG) + CoA** (morizono2004mammaliannacetylglutamatesynthase. pages 1-2, caldovic2010nacetylglutamatesynthasestructure pages 4-5, shi2015thenacetylglutamatesynthase pages 1-3) |
| Substrates | **L-glutamate** and **acetyl-CoA**; human enzyme shows high specificity for these substrates (shi2015thenacetylglutamatesynthase pages 3-6, shi2015thenacetylglutamatesynthase pages 1-3) |
| Product | **N-acetylglutamate (NAG)**, the essential allosteric activator of CPS1 (morizono2004mammaliannacetylglutamatesynthase. pages 1-2, caldovic2003nacetylglutamateandits pages 7-8) |
| Allosteric activator | **L-arginine**; activates mammalian NAGS about **2–5-fold**, with **Ka ~30–50 µM** (caldovic2003nacetylglutamateandits pages 7-8, shi2015thenacetylglutamatesynthase pages 3-6) |
| Km for glutamate | Reported range **~1–8.1 mM** depending on preparation/assay system (shi2015thenacetylglutamatesynthase pages 3-6) |
| Km for acetyl-CoA | Reported range **~0.7–4.4 mM** depending on preparation/assay system (shi2015thenacetylglutamatesynthase pages 3-6) |
| Subcellular localization | **Mitochondrial matrix** (morizono2004mammaliannacetylglutamatesynthase. pages 1-2, shi2015thenacetylglutamatesynthase pages 3-6) |
| Tissue expression | Highest in **liver** and **small intestine**; lower expression reported in **kidney, testis, spleen** (morizono2004mammaliannacetylglutamatesynthase. pages 1-2) |
| Protein length | **534 aa preprotein** with N-terminal mitochondrial targeting sequence (morizono2004mammaliannacetylglutamatesynthase. pages 1-2) |
| Domain architecture | N-terminal **AAK (amino acid kinase-like) domain** plus C-terminal **NAT/GNAT acetyltransferase domain**; also contains an N-terminal variable segment (shi2015thenacetylglutamatesynthase pages 6-8, shi2015thenacetylglutamatesynthase pages 11-15, caldovic2010nacetylglutamatesynthasestructure pages 1-2) |
| Oligomeric state | Reported as **trimeric** in some studies, with evidence for arginine-dependent oligomerization behavior; vertebrate-like NAGS family members also discussed in relation to **tetrameric** organization/models (shi2015thenacetylglutamatesynthase pages 3-6, shi2015thenacetylglutamatesynthase pages 1-3) |
| Disease association | **NAGS deficiency (NAGSD)** causing **hyperammonemia** / urea cycle dysfunction; strong disease-target association in Open Targets (morizono2004mammaliannacetylglutamatesynthase. pages 4-5, mew2011nacetylglutamatesynthasedeficiency pages 1-2, OpenTargets Search: -NAGS) |
| Drug / functional replacement therapy | **N-carbamylglutamate (carglumic acid / carbamylglutamate)**, a stable NAG analog that activates CPS1 and can normalize ammonia in NAGSD (caldovic2010nacetylglutamatesynthasestructure pages 5-7, singh2024theefficacyof pages 1-2, mew2011nacetylglutamatesynthasedeficiency pages 5-6) |


*Table: This table summarizes core biochemical, cellular, and clinical properties of human NAGS, including its catalytic reaction, regulation, localization, and disease relevance. It is useful as a compact reference for the functional annotation of UniProt Q8N159.*

## 1. Enzymatic Function and Catalytic Reaction

Human N-acetylglutamate synthase (NAGS; EC 2.3.1.1) catalyzes the formation of N-acetylglutamate (NAG) from two substrates, L-glutamate and acetyl-coenzyme A (acetyl-CoA), releasing free CoA as a by-product (morizono2004mammaliannacetylglutamatesynthase. pages 1-2, shi2015thenacetylglutamatesynthase pages 1-3). This acetylation reaction is the committed step in the production of NAG in mammalian hepatocytes. The catalytic mechanism involves a direct nucleophilic attack by the α-amino nitrogen of L-glutamate on the acetyl group of acetyl-CoA, rather than proceeding through a ping-pong mechanism (caldovic2010nacetylglutamatesynthasestructure pages 4-5).

### Substrate Specificity and Kinetic Parameters

Human NAGS exhibits high substrate specificity. Studies on human liver NAGS reported apparent Km values of 4.4 mM for acetyl-CoA and 8.1 mM for L-glutamate, whereas studies using recombinant rat NAGS yielded lower Km values of 0.7 mM for acetyl-CoA and 1 mM for L-glutamate, which are considered more representative of the purified enzyme (shi2015thenacetylglutamatesynthase pages 3-6). The enzyme displays very low activity with alternative amino acid substrates: only 5.0% activity with glutamine and 2.9% with glycine relative to glutamate. Similarly, acetyl-CoA is highly specific as the acyl donor, with only 4.3% activity toward propionyl-CoA and no measurable activity with other acyl-CoA derivatives (shi2015thenacetylglutamatesynthase pages 3-6).

## 2. Domain Structure and Protein Architecture

Human NAGS is synthesized as a 534-amino acid preprotein (morizono2004mammaliannacetylglutamatesynthase. pages 1-2). The protein contains three structurally distinct regions:

- **Mitochondrial targeting signal (MTS):** Residues 1–49 at the N-terminus, which direct the protein to the mitochondrial matrix and are cleaved upon import (morizono2004mammaliannacetylglutamatesynthase. pages 1-2, morizono2004mammaliannacetylglutamatesynthase. pages 2-4).
- **Variable domain:** A ~40–50 amino acid segment rich in charged residues and prolines that lacks defined secondary structure. This domain is unique to mammalian NAGS and may facilitate protein–protein interactions with other mitochondrial partners (shi2015thenacetylglutamatesynthase pages 6-8, shi2015thenacetylglutamatesynthase pages 15-17).
- **Conserved segment:** Contains two independently folded functional domains connected by a short 1–3 amino acid linker:
  - An N-terminal **amino acid kinase-like (AAK) domain** (approximately residues 137–373), featuring an eight-stranded β-sheet core flanked by α-helices. This domain binds L-arginine and provides the structural framework for allosteric regulation (shi2015thenacetylglutamatesynthase pages 6-8, shi2015thenacetylglutamatesynthase pages 11-15, caldovic2010nacetylglutamatesynthasestructure pages 1-2).
  - A C-terminal **N-acetyltransferase (NAT/GNAT) domain** (approximately residues 377–472), adopting a seven-stranded β-sheet αβα sandwich fold characteristic of GCN5-related acetyltransferases. This domain harbors the catalytic site where both acetyl-CoA and L-glutamate bind (shi2015thenacetylglutamatesynthase pages 6-8, shi2015thenacetylglutamatesynthase pages 1-3, shi2015thenacetylglutamatesynthase pages 11-15).

While only the NAT domain has significant NAGS catalytic activity, the AAK domain is essential for enhancing enzymatic activity and mediating arginine-dependent allosteric regulation (shi2015thenacetylglutamatesynthase pages 11-15, shi2015thenacetylglutamatesynthase pages 15-17). Vertebrate-like NAGS proteins have a tetrameric quaternary structure, distinguishing them from classical bacterial NAGS enzymes, which form hexamers (shi2015thenacetylglutamatesynthase pages 1-3). Mammalian NAGS exists as a trimer whose oligomerization state depends on L-arginine concentration (shi2015thenacetylglutamatesynthase pages 3-6).

## 3. Subcellular Localization and Tissue Expression

Human NAGS is targeted to the **mitochondrial matrix** where it carries out its catalytic function (morizono2004mammaliannacetylglutamatesynthase. pages 1-2, shi2015thenacetylglutamatesynthase pages 3-6). The N-terminal mitochondrial targeting signal is cleaved upon import into the mitochondria. Two possible signal peptide cleavage sites have been predicted after amino acid positions 31 and 49, generating long and short mature forms (morizono2004mammaliannacetylglutamatesynthase. pages 1-2).

### Post-translational Processing and Multiple Forms

Studies on mouse NAGS have revealed a bipartite mitochondrial import mechanism similar to ornithine transcarbamylase. Two cleavage events occur after mitochondrial import: (1) cleavage of the canonical mitochondrial leader peptide after amino acid 50, and (2) a second cleavage at the end of the variable domain after amino acid 91 (morizono2004mammaliannacetylglutamatesynthase. pages 4-5). This processing generates two mature forms:

- **NAGS-M (mature NAGS):** Retains the variable domain after MTS removal.
- **NAGS-C (conserved domain NAGS):** Lacks both the MTS and the variable segment.

Both forms are catalytically active with similar substrate affinities; however, NAGS-C exhibits approximately two-fold higher maximal velocity compared to NAGS-M (caldovic2010nacetylglutamatesynthasestructure pages 1-2).

### Tissue Distribution

NAGS is primarily expressed in **liver** and **small intestine**, the tissues where carbamoyl phosphate synthetase 1 (CPS1) is exclusively expressed (morizono2004mammaliannacetylglutamatesynthase. pages 1-2). Lower expression levels are also detectable in kidney, testis, and spleen, suggesting potential additional roles beyond the urea cycle (morizono2004mammaliannacetylglutamatesynthase. pages 1-2). Notably, one study reported that NAGS immunoreactivity was not detected in kidney or spleen tissue, indicating that the primary physiological expression is hepatic and intestinal (shi2015thenacetylglutamatesynthase pages 3-6).

## 4. Role in the Urea Cycle and Biochemical Pathway

The primary physiological role of human NAGS is to produce N-acetylglutamate (NAG), which serves as an **essential and obligatory allosteric activator** of carbamoyl phosphate synthetase 1 (CPS1), the first and rate-limiting enzyme of the urea cycle (morizono2004mammaliannacetylglutamatesynthase. pages 1-2, caldovic2003nacetylglutamateandits pages 7-8, haskins2016effectofarginine pages 1-2). Without NAG, CPS1 is catalytically inactive, and the entire urea cycle—which converts toxic ammonia into non-toxic urea—is effectively shut down.

### Regulatory Function in Ureagenesis

NAG concentrations in liver mitochondria are similar to the activation constant (Ka) of CPS1 for NAG, positioning NAG as a key flux regulator of the urea cycle (caldovic2003nacetylglutamateandits pages 7-8, caldovic2003nacetylglutamateandits pages 6-7). The regulation operates through a **double positive feedback loop**: L-arginine (the end-product of the urea cycle) allosterically activates NAGS to produce NAG, which in turn activates CPS1 (caldovic2010nacetylglutamatesynthasestructure pages 2-4, haskins2008inversionofallosteric pages 9-10). This arrangement creates a rapid and robust ammonia detoxification system that protects the central nervous system from hyperammonemia (caldovic2010nacetylglutamatesynthasestructure pages 2-4).

Increased dietary protein and ammonia intake are associated with elevated NAGS activity and hepatic NAG content, allowing modulation of urea cycle flux at relatively constant ammonium concentrations (caldovic2003nacetylglutamateandits pages 7-8).

## 5. Allosteric Regulation by L-Arginine

L-arginine is the primary allosteric activator of mammalian NAGS, increasing enzymatic activity 2–5-fold at saturating substrate concentrations, with an activation constant (Ka) of 30–50 µM (caldovic2003nacetylglutamateandits pages 7-8, shi2015thenacetylglutamatesynthase pages 3-6). This Ka corresponds well to physiological liver arginine concentrations, ensuring physiological relevance of the activation mechanism. The activation is highly specific to L-arginine; among structural analogues, only L-argininic acid produces similar activation, and both bind to the same site (shi2015thenacetylglutamatesynthase pages 3-6). Arginine increases enzyme velocity without significantly affecting substrate affinity (caldovic2003nacetylglutamateandits pages 6-7, shi2015thenacetylglutamatesynthase pages 3-6).

The arginine-binding site is located at the C-terminus of the AAK domain near the AAK-NAT domain interface and is defined by a conserved motif (E-(L/I)-(F/M)-(T/S)-X-X-G-X-G-T) (shi2015thenacetylglutamatesynthase pages 8-11). In mammalian NAGS, arginine binding induces a conformational change causing the NAT domain to undergo marked reorientation relative to the AAK domain, enabling their productive interaction (caldovic2010nacetylglutamatesynthasestructure pages 2-4). Arginine binding also affects NAGS oligomerization state: in mouse NAGS, the partition coefficient increases in the presence of L-arginine, suggesting a smaller hydrodynamic radius due to a conformational or oligomerization change (haskins2016effectofarginine pages 1-2).

The physiological importance of arginine activation was demonstrated in vivo using NAGS knockout mice treated with AAV vectors encoding either wild-type NAGS or the arginine-insensitive E354A mutant. Mice expressing E354A mutant NAGS were viable but maintained chronically elevated plasma ammonia despite equivalent protein expression levels, demonstrating that arginine activation is essential for normal ureagenesis (sonaimuthu2021genedeliverycorrects pages 1-2, sonaimuthu2021genedeliverycorrects pages 8-11).

## 6. Evolutionary Perspective

NAGS has undergone a remarkable evolutionary transformation in its allosteric regulation. In microorganisms and plants, NAGS catalyzes the first committed step of arginine biosynthesis and is **inhibited** by arginine as part of end-product feedback regulation (haskins2008inversionofallosteric pages 8-9, caldovic2010nacetylglutamatesynthasestructure pages 1-2). During the evolution of vertebrates from aquatic to terrestrial habitats, the allosteric effect of arginine on NAGS inverted from inhibition to activation (haskins2008inversionofallosteric pages 8-9, haskins2008inversionofallosteric pages 9-10).

This transition was gradual across vertebrate phylogeny: bacterial NAGS shows complete inhibition by arginine, fish NAGS (zebrafish, pufferfish) shows partial inhibition, and amphibian and mammalian NAGS shows full activation (haskins2008inversionofallosteric pages 9-10, haskins2008inversionofallosteric pages 1-2). The four invariant amino acids responsible for arginine binding are conserved from bacteria to mammals, indicating that the same binding site produces different conformational outcomes depending on species-specific structural context (haskins2008inversionofallosteric pages 8-9, haskins2008inversionofallosteric pages 4-5). This allosteric inversion coincided with the transition from CPS III (in fish) to CPS I (in tetrapods) and is considered a molecular marker for tetrapod evolution (haskins2008inversionofallosteric pages 8-9, haskins2008inversionofallosteric pages 9-10).

Phylogenetically, mammalian NAGS evolved from a bifunctional N-acetylglutamate synthase-kinase (NAGS-K) ancestor, retaining the acetyltransferase activity while losing the kinase activity that is no longer needed in animals (qu2007anovelbifunctional pages 11-12, shi2015thenacetylglutamatesynthase pages 11-15). The mammalian NAGS gene was not identified until 2002 due to very low sequence similarity (~20–30%) with classical bacterial NAGS (shi2015thenacetylglutamatesynthase pages 1-3, caldovic2010nacetylglutamatesynthasestructure pages 2-4).

## 7. Clinical Significance: NAGS Deficiency

### Disease Overview

NAGS deficiency (NAGSD; OMIM #237310) is an autosomal recessive urea cycle disorder and the **rarest** of all urea cycle defects, with an estimated incidence of less than 1 in 2,000,000 live births (singh2024theefficacyof pages 1-2). As of 2024, only approximately 105 cases from 79 families have been reported worldwide (caldovic2024dataminingapproachesfor pages 2-4). The condition is uniquely treatable among urea cycle disorders because a pharmacological substitute for NAG is available (mew2011nacetylglutamatesynthasedeficiency pages 5-6). OpenTargets analysis confirms strong disease-target associations for NAGS with hyperammonemia due to NAGS deficiency (association score 0.84) and hereditary disease (score 0.87) (OpenTargets Search: -NAGS).

### Clinical Presentation

NAGS deficiency presents with hyperammonemia that can range from severe neonatal onset to mild late-onset forms. Neonatal presentations typically include poor feeding, vomiting, lethargy, hypertonia or hypotonia, seizures, and tachypnea (kenneson2020presentationandmanagement pages 6-7, singh2024theefficacyof pages 1-2). Late-onset cases may present with cyclic vomiting, behavioral changes, headaches, ataxia, and decreased consciousness, sometimes not diagnosed until adulthood (kenneson2020presentationandmanagement pages 6-7, logt2016hyperammonemiadueto pages 2-4). Biochemically, affected individuals show elevated plasma ammonia and glutamine, with low-to-normal citrulline and normal urinary orotic acid, a profile indistinguishable from CPS1 deficiency (mew2011nacetylglutamatesynthasedeficiency pages 1-2, caldovic2010nacetylglutamatesynthasestructure pages 5-7).

### Genotype-Phenotype Correlations

Missense mutations in the C-terminal NAT domain typically cause severe neonatal-onset disease with less than 5% residual enzyme activity, often involving frameshift or nonsense mutations (kenneson2020presentationandmanagement pages 6-7, caldovic2010nacetylglutamatesynthasestructure pages 5-7). Mutations in the AAK domain tend to cause later-onset phenotypes and may affect arginine regulation rather than catalysis directly (kenneson2020presentationandmanagement pages 6-7). Residual NAGS activity as low as 5% can result in milder, late-onset disease (caldovic2024dataminingapproachesfor pages 4-6).

### Treatment

NAGS deficiency is uniquely treatable with **N-carbamylglutamate (NCG; carglumic acid, Carbaglu®)**, a stable structural analog of NAG that directly activates CPS1 and is resistant to enzymatic degradation by acylase (caldovic2010nacetylglutamatesynthasestructure pages 5-7, mew2011nacetylglutamatesynthasedeficiency pages 5-6). NCG normalizes plasma ammonia levels within 8 hours during acute hyperammonemic crises and is effective as long-term maintenance therapy at doses of 15–200 mg/kg/day (caldovic2010nacetylglutamatesynthasestructure pages 5-7, mew2011nacetylglutamatesynthasedeficiency pages 5-6). All patients studied have responded well to carbamylglutamate therapy, with normalization of plasma ammonia, citrulline, and urine orotic acid (singh2024theefficacyof pages 1-2). A 3-day NCG trial at 2.2 g/m²/day can serve both diagnostic and therapeutic purposes (caldovic2010nacetylglutamatesynthasestructure pages 5-7).

## 8. Recent Developments (2024)

### Recombinant Human NAGS for Variant Assessment

Gougeard et al. (2024) developed a stabilized chimeric form of human NAGS (the conserved domain fused with maltose binding protein, MBP-cHuNAGS) for assessing the pathogenicity of missense variants found in NAGSD patients. They characterized 23 nonsynonymous single-base changes and found that for all but one variant (A279T), disease causation was explained by the enzymatic alterations identified, including loss of arginine activation, increased Km for glutamate, active site inactivation, decreased thermal stability, and protein misfolding (gougeard2024useofpure pages 14-16). Importantly, 17 of the 23 variants showed increased tendency to misfold, suggesting that NAGSD may fundamentally function as a **protein misfolding disease**. The study also revealed that wild-type human NAGS loses 25% of activity at fever temperature (40°C), suggesting thermal instability as a clinically relevant disease mechanism. The authors suggest that pharmacochaperones could represent a novel therapeutic strategy (gougeard2024useofpure pages 14-16).

### Transcriptional Regulation and Prevalence Studies

Caldovic et al. (2024) used datamining approaches to investigate the low prevalence of NAGSD and identify novel regulatory elements in the NAGS gene and other urea cycle genes. They discovered a **novel regulatory element in the first intron** of the NAGS gene through ENCODE database analysis and identified eight deleterious sequence variants in NAGS splicing regions and cis-acting regulatory elements (caldovic2024dataminingapproachesfor pages 2-4, caldovic2024dataminingapproachesfor pages 1-2). Their analysis suggests that the rarity of NAGSD may be due to several factors: (1) the NAGS protein fold tolerates amino acid substitutions unusually well, with NAGS monomers from different organisms sharing only ~20% sequence identity while maintaining similar three-dimensional structures; (2) the NAGS catalytic domain has a small genomic footprint (comprising only 29.5% of the protein); and (3) alternative metabolic sources of NAG or NCG may exist in the body (caldovic2024dataminingapproachesfor pages 4-6).

### Nutritional Management

Singh et al. (2024) reported on the efficacy of carbamylglutamate in seven NAGS deficiency cases, demonstrating that protein restriction is generally not necessary when patients are maintained on adequate carbamylglutamate therapy, though disruption of access to the drug can have severe consequences including hyperammonemic episodes with poor long-term outcomes (singh2024theefficacyof pages 1-2).

### Gene Therapy

Sonaimuthu et al. (2021) demonstrated successful AAV2/8-based gene therapy for NAGS deficiency in knockout mice. Doses of 10¹⁰ and 10¹¹ viral particles completely rescued Nags−/− mice from hyperammonemia, with NAGS protein expression matching or exceeding wild-type levels (sonaimuthu2021genedeliverycorrects pages 5-6, sonaimuthu2021genedeliverycorrects pages 6-8). The study also demonstrated that arginine-insensitive NAGS (E354A mutant) failed to fully correct hyperammonemia despite equivalent protein expression, confirming the physiological essentiality of arginine-mediated NAGS activation (sonaimuthu2021genedeliverycorrects pages 1-2, sonaimuthu2021genedeliverycorrects pages 8-11).

## 9. Summary

Human NAGS (Q8N159) is a mitochondrial matrix acetyltransferase that catalyzes the synthesis of N-acetylglutamate from L-glutamate and acetyl-CoA. Its primary biological role is to produce NAG, the obligatory allosteric activator of CPS1, the first and rate-limiting enzyme of the urea cycle. NAGS is allosterically activated by L-arginine, creating a double positive feedback loop that enables rapid and robust ammonia detoxification. The enzyme is predominantly expressed in liver and small intestine, consistent with its role in hepatic ureagenesis. NAGS deficiency is the rarest urea cycle disorder but is uniquely treatable with the NAG analog N-carbamylglutamate (carglumic acid). Recent research (2024) has revealed that many NAGSD-causing mutations lead to protein misfolding, opening potential therapeutic avenues with pharmacochaperones, while novel cis-regulatory elements in the NAGS gene continue to be discovered through genomic datamining approaches.

References

1. (morizono2004mammaliannacetylglutamatesynthase. pages 1-2): Hiroki Morizono, Ljubica Caldovic, Dashuang Shi, and Mendel Tuchman. Mammalian n-acetylglutamate synthase. Molecular genetics and metabolism, 81 Suppl 1:S4-11, Apr 2004. URL: https://doi.org/10.1016/j.ymgme.2003.10.017, doi:10.1016/j.ymgme.2003.10.017. This article has 76 citations and is from a peer-reviewed journal.

2. (caldovic2010nacetylglutamatesynthasestructure pages 1-2): Ljubica Caldovic, Nicholas Ah Mew, Dashuang Shi, Hiroki Morizono, Marc Yudkoff, and Mendel Tuchman. N-acetylglutamate synthase: structure, function and defects. Molecular genetics and metabolism, 100 Suppl 1:S13-9, Jan 2010. URL: https://doi.org/10.1016/j.ymgme.2010.02.018, doi:10.1016/j.ymgme.2010.02.018. This article has 95 citations and is from a peer-reviewed journal.

3. (caldovic2024dataminingapproachesfor pages 2-4): Ljubica Caldovic, Julie J. Ahn, Jacklyn Andricovic, Veronica M. Balick, Mallory Brayer, Pamela A. Chansky, Tyson Dawson, Alex C. Edwards, Sara E. Felsen, Karim Ismat, Sveta V. Jagannathan, Brendan T. Mann, Jacob A. Medina, Toshio Morizono, Michio Morizono, Shatha Salameh, Neerja Vashist, Emily C. Williams, Zhe Zhou, and Hiroki Morizono. Datamining approaches for examining the low prevalence of n‐acetylglutamate synthase deficiency and understanding transcriptional regulation of urea cycle genes. Journal of Inherited Metabolic Disease, 47:1175-1193, Nov 2024. URL: https://doi.org/10.1002/jimd.12687, doi:10.1002/jimd.12687. This article has 2 citations and is from a peer-reviewed journal.

4. (shi2015thenacetylglutamatesynthase pages 1-3): Dashuang Shi, Norma Allewell, and Mendel Tuchman. The n-acetylglutamate synthase family: structures, function and mechanisms. International Journal of Molecular Sciences, 16:13004-13022, Jun 2015. URL: https://doi.org/10.3390/ijms160613004, doi:10.3390/ijms160613004. This article has 46 citations.

5. (caldovic2010nacetylglutamatesynthasestructure pages 4-5): Ljubica Caldovic, Nicholas Ah Mew, Dashuang Shi, Hiroki Morizono, Marc Yudkoff, and Mendel Tuchman. N-acetylglutamate synthase: structure, function and defects. Molecular genetics and metabolism, 100 Suppl 1:S13-9, Jan 2010. URL: https://doi.org/10.1016/j.ymgme.2010.02.018, doi:10.1016/j.ymgme.2010.02.018. This article has 95 citations and is from a peer-reviewed journal.

6. (shi2015thenacetylglutamatesynthase pages 3-6): Dashuang Shi, Norma Allewell, and Mendel Tuchman. The n-acetylglutamate synthase family: structures, function and mechanisms. International Journal of Molecular Sciences, 16:13004-13022, Jun 2015. URL: https://doi.org/10.3390/ijms160613004, doi:10.3390/ijms160613004. This article has 46 citations.

7. (caldovic2003nacetylglutamateandits pages 7-8): Ljubica CALDOVIC and Mendel TUCHMAN. N-acetylglutamate and its changing role through evolution. The Biochemical journal, 372 Pt 2:279-90, Jun 2003. URL: https://doi.org/10.1042/bj20030002, doi:10.1042/bj20030002. This article has 194 citations.

8. (shi2015thenacetylglutamatesynthase pages 6-8): Dashuang Shi, Norma Allewell, and Mendel Tuchman. The n-acetylglutamate synthase family: structures, function and mechanisms. International Journal of Molecular Sciences, 16:13004-13022, Jun 2015. URL: https://doi.org/10.3390/ijms160613004, doi:10.3390/ijms160613004. This article has 46 citations.

9. (shi2015thenacetylglutamatesynthase pages 11-15): Dashuang Shi, Norma Allewell, and Mendel Tuchman. The n-acetylglutamate synthase family: structures, function and mechanisms. International Journal of Molecular Sciences, 16:13004-13022, Jun 2015. URL: https://doi.org/10.3390/ijms160613004, doi:10.3390/ijms160613004. This article has 46 citations.

10. (morizono2004mammaliannacetylglutamatesynthase. pages 4-5): Hiroki Morizono, Ljubica Caldovic, Dashuang Shi, and Mendel Tuchman. Mammalian n-acetylglutamate synthase. Molecular genetics and metabolism, 81 Suppl 1:S4-11, Apr 2004. URL: https://doi.org/10.1016/j.ymgme.2003.10.017, doi:10.1016/j.ymgme.2003.10.017. This article has 76 citations and is from a peer-reviewed journal.

11. (mew2011nacetylglutamatesynthasedeficiency pages 1-2): Nicholas Ah Mew and Nicholas Ah Mew. N-acetylglutamate synthase deficiency: an insight into the genetics, epidemiology, pathophysiology, and treatment. The Application of Clinical Genetics, pages 127, Aug 2011. URL: https://doi.org/10.2147/tacg.s12702, doi:10.2147/tacg.s12702. This article has 53 citations.

12. (OpenTargets Search: -NAGS): Open Targets Query (-NAGS, 9 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

13. (caldovic2010nacetylglutamatesynthasestructure pages 5-7): Ljubica Caldovic, Nicholas Ah Mew, Dashuang Shi, Hiroki Morizono, Marc Yudkoff, and Mendel Tuchman. N-acetylglutamate synthase: structure, function and defects. Molecular genetics and metabolism, 100 Suppl 1:S13-9, Jan 2010. URL: https://doi.org/10.1016/j.ymgme.2010.02.018, doi:10.1016/j.ymgme.2010.02.018. This article has 95 citations and is from a peer-reviewed journal.

14. (singh2024theefficacyof pages 1-2): Rani H. Singh, Marie-Hélène Bourdages, Angela Kurtz, Erin MacLoed, Chelsea Norman, Suzanne Ratko, Sandra C. van Calcar, and Aileen Kenneson. The efficacy of carbamylglutamate impacts the nutritional management of patients with n-acetylglutamate synthase deficiency. Orphanet Journal of Rare Diseases, Apr 2024. URL: https://doi.org/10.1186/s13023-024-03167-0, doi:10.1186/s13023-024-03167-0. This article has 10 citations and is from a peer-reviewed journal.

15. (mew2011nacetylglutamatesynthasedeficiency pages 5-6): Nicholas Ah Mew and Nicholas Ah Mew. N-acetylglutamate synthase deficiency: an insight into the genetics, epidemiology, pathophysiology, and treatment. The Application of Clinical Genetics, pages 127, Aug 2011. URL: https://doi.org/10.2147/tacg.s12702, doi:10.2147/tacg.s12702. This article has 53 citations.

16. (morizono2004mammaliannacetylglutamatesynthase. pages 2-4): Hiroki Morizono, Ljubica Caldovic, Dashuang Shi, and Mendel Tuchman. Mammalian n-acetylglutamate synthase. Molecular genetics and metabolism, 81 Suppl 1:S4-11, Apr 2004. URL: https://doi.org/10.1016/j.ymgme.2003.10.017, doi:10.1016/j.ymgme.2003.10.017. This article has 76 citations and is from a peer-reviewed journal.

17. (shi2015thenacetylglutamatesynthase pages 15-17): Dashuang Shi, Norma Allewell, and Mendel Tuchman. The n-acetylglutamate synthase family: structures, function and mechanisms. International Journal of Molecular Sciences, 16:13004-13022, Jun 2015. URL: https://doi.org/10.3390/ijms160613004, doi:10.3390/ijms160613004. This article has 46 citations.

18. (haskins2016effectofarginine pages 1-2): N. Haskins, Amy Mumo, P. H. Brown, M. Tuchman, H. Morizono, and L. Caldovic. Effect of arginine on oligomerization and stability of n-acetylglutamate synthase. Scientific Reports, Dec 2016. URL: https://doi.org/10.1038/srep38711, doi:10.1038/srep38711. This article has 9 citations and is from a peer-reviewed journal.

19. (caldovic2003nacetylglutamateandits pages 6-7): Ljubica CALDOVIC and Mendel TUCHMAN. N-acetylglutamate and its changing role through evolution. The Biochemical journal, 372 Pt 2:279-90, Jun 2003. URL: https://doi.org/10.1042/bj20030002, doi:10.1042/bj20030002. This article has 194 citations.

20. (caldovic2010nacetylglutamatesynthasestructure pages 2-4): Ljubica Caldovic, Nicholas Ah Mew, Dashuang Shi, Hiroki Morizono, Marc Yudkoff, and Mendel Tuchman. N-acetylglutamate synthase: structure, function and defects. Molecular genetics and metabolism, 100 Suppl 1:S13-9, Jan 2010. URL: https://doi.org/10.1016/j.ymgme.2010.02.018, doi:10.1016/j.ymgme.2010.02.018. This article has 95 citations and is from a peer-reviewed journal.

21. (haskins2008inversionofallosteric pages 9-10): Nantaporn Haskins, Maria Panglao, Qiuhao Qu, Himani Majumdar, Juan Cabrera-Luque, Hiroki Morizono, Mendel Tuchman, and Ljubica Caldovic. Inversion of allosteric effect of arginine on n-acetylglutamate synthase, a molecular marker for evolution of tetrapods. BMC Biochemistry, 9:24-24, Sep 2008. URL: https://doi.org/10.1186/1471-2091-9-24, doi:10.1186/1471-2091-9-24. This article has 38 citations and is from a peer-reviewed journal.

22. (shi2015thenacetylglutamatesynthase pages 8-11): Dashuang Shi, Norma Allewell, and Mendel Tuchman. The n-acetylglutamate synthase family: structures, function and mechanisms. International Journal of Molecular Sciences, 16:13004-13022, Jun 2015. URL: https://doi.org/10.3390/ijms160613004, doi:10.3390/ijms160613004. This article has 46 citations.

23. (sonaimuthu2021genedeliverycorrects pages 1-2): P. Sonaimuthu, E. Senkevitch, N. Haskins, P. Uapinyoying, M. McNutt, H. Morizono, M. Tuchman, and L. Caldovic. Gene delivery corrects n-acetylglutamate synthase deficiency and enables insights in the physiological impact of l-arginine activation of n-acetylglutamate synthase. Scientific Reports, Feb 2021. URL: https://doi.org/10.1038/s41598-021-82994-8, doi:10.1038/s41598-021-82994-8. This article has 16 citations and is from a peer-reviewed journal.

24. (sonaimuthu2021genedeliverycorrects pages 8-11): P. Sonaimuthu, E. Senkevitch, N. Haskins, P. Uapinyoying, M. McNutt, H. Morizono, M. Tuchman, and L. Caldovic. Gene delivery corrects n-acetylglutamate synthase deficiency and enables insights in the physiological impact of l-arginine activation of n-acetylglutamate synthase. Scientific Reports, Feb 2021. URL: https://doi.org/10.1038/s41598-021-82994-8, doi:10.1038/s41598-021-82994-8. This article has 16 citations and is from a peer-reviewed journal.

25. (haskins2008inversionofallosteric pages 8-9): Nantaporn Haskins, Maria Panglao, Qiuhao Qu, Himani Majumdar, Juan Cabrera-Luque, Hiroki Morizono, Mendel Tuchman, and Ljubica Caldovic. Inversion of allosteric effect of arginine on n-acetylglutamate synthase, a molecular marker for evolution of tetrapods. BMC Biochemistry, 9:24-24, Sep 2008. URL: https://doi.org/10.1186/1471-2091-9-24, doi:10.1186/1471-2091-9-24. This article has 38 citations and is from a peer-reviewed journal.

26. (haskins2008inversionofallosteric pages 1-2): Nantaporn Haskins, Maria Panglao, Qiuhao Qu, Himani Majumdar, Juan Cabrera-Luque, Hiroki Morizono, Mendel Tuchman, and Ljubica Caldovic. Inversion of allosteric effect of arginine on n-acetylglutamate synthase, a molecular marker for evolution of tetrapods. BMC Biochemistry, 9:24-24, Sep 2008. URL: https://doi.org/10.1186/1471-2091-9-24, doi:10.1186/1471-2091-9-24. This article has 38 citations and is from a peer-reviewed journal.

27. (haskins2008inversionofallosteric pages 4-5): Nantaporn Haskins, Maria Panglao, Qiuhao Qu, Himani Majumdar, Juan Cabrera-Luque, Hiroki Morizono, Mendel Tuchman, and Ljubica Caldovic. Inversion of allosteric effect of arginine on n-acetylglutamate synthase, a molecular marker for evolution of tetrapods. BMC Biochemistry, 9:24-24, Sep 2008. URL: https://doi.org/10.1186/1471-2091-9-24, doi:10.1186/1471-2091-9-24. This article has 38 citations and is from a peer-reviewed journal.

28. (qu2007anovelbifunctional pages 11-12): Qiuhao Qu, Hiroki Morizono, Dashuang Shi, Mendel Tuchman, and Ljubica Caldovic. A novel bifunctional n-acetylglutamate synthase-kinase from xanthomonas campestris that is closely related to mammalian n-acetylglutamate synthase. BMC Biochemistry, 8:4-4, Apr 2007. URL: https://doi.org/10.1186/1471-2091-8-4, doi:10.1186/1471-2091-8-4. This article has 34 citations and is from a peer-reviewed journal.

29. (kenneson2020presentationandmanagement pages 6-7): Aileen Kenneson and Rani H. Singh. Presentation and management of n-acetylglutamate synthase deficiency: a review of the literature. Orphanet Journal of Rare Diseases, Oct 2020. URL: https://doi.org/10.1186/s13023-020-01560-z, doi:10.1186/s13023-020-01560-z. This article has 26 citations and is from a peer-reviewed journal.

30. (logt2016hyperammonemiadueto pages 2-4): Anne-Els van de Logt, Leo A. J. Kluijtmans, Marleen C. D. G. Huigen, and Mirian C. H. Janssen. Hyperammonemia due to adult-onset n-acetylglutamate synthase deficiency. JIMD reports, 31:95-99, May 2016. URL: https://doi.org/10.1007/8904\_2016\_565, doi:10.1007/8904\_2016\_565. This article has 16 citations and is from a peer-reviewed journal.

31. (caldovic2024dataminingapproachesfor pages 4-6): Ljubica Caldovic, Julie J. Ahn, Jacklyn Andricovic, Veronica M. Balick, Mallory Brayer, Pamela A. Chansky, Tyson Dawson, Alex C. Edwards, Sara E. Felsen, Karim Ismat, Sveta V. Jagannathan, Brendan T. Mann, Jacob A. Medina, Toshio Morizono, Michio Morizono, Shatha Salameh, Neerja Vashist, Emily C. Williams, Zhe Zhou, and Hiroki Morizono. Datamining approaches for examining the low prevalence of n‐acetylglutamate synthase deficiency and understanding transcriptional regulation of urea cycle genes. Journal of Inherited Metabolic Disease, 47:1175-1193, Nov 2024. URL: https://doi.org/10.1002/jimd.12687, doi:10.1002/jimd.12687. This article has 2 citations and is from a peer-reviewed journal.

32. (gougeard2024useofpure pages 14-16): Nadine Gougeard, Enea Sancho‐Vaello, M. Leonor Fernández‐Murga, Borja Martínez‐Sinisterra, Badr Loukili‐Hassani, Johannes Häberle, Clara Marco‐Marín, and Vicente Rubio. Use of pure recombinant human enzymes to assess the disease‐causing potential of missense mutations in urea cycle disorders, applied to n‐acetylglutamate synthase deficiency. Journal of Inherited Metabolic Disease, 47:1194-1212, May 2024. URL: https://doi.org/10.1002/jimd.12747, doi:10.1002/jimd.12747. This article has 2 citations and is from a peer-reviewed journal.

33. (caldovic2024dataminingapproachesfor pages 1-2): Ljubica Caldovic, Julie J. Ahn, Jacklyn Andricovic, Veronica M. Balick, Mallory Brayer, Pamela A. Chansky, Tyson Dawson, Alex C. Edwards, Sara E. Felsen, Karim Ismat, Sveta V. Jagannathan, Brendan T. Mann, Jacob A. Medina, Toshio Morizono, Michio Morizono, Shatha Salameh, Neerja Vashist, Emily C. Williams, Zhe Zhou, and Hiroki Morizono. Datamining approaches for examining the low prevalence of n‐acetylglutamate synthase deficiency and understanding transcriptional regulation of urea cycle genes. Journal of Inherited Metabolic Disease, 47:1175-1193, Nov 2024. URL: https://doi.org/10.1002/jimd.12687, doi:10.1002/jimd.12687. This article has 2 citations and is from a peer-reviewed journal.

34. (sonaimuthu2021genedeliverycorrects pages 5-6): P. Sonaimuthu, E. Senkevitch, N. Haskins, P. Uapinyoying, M. McNutt, H. Morizono, M. Tuchman, and L. Caldovic. Gene delivery corrects n-acetylglutamate synthase deficiency and enables insights in the physiological impact of l-arginine activation of n-acetylglutamate synthase. Scientific Reports, Feb 2021. URL: https://doi.org/10.1038/s41598-021-82994-8, doi:10.1038/s41598-021-82994-8. This article has 16 citations and is from a peer-reviewed journal.

35. (sonaimuthu2021genedeliverycorrects pages 6-8): P. Sonaimuthu, E. Senkevitch, N. Haskins, P. Uapinyoying, M. McNutt, H. Morizono, M. Tuchman, and L. Caldovic. Gene delivery corrects n-acetylglutamate synthase deficiency and enables insights in the physiological impact of l-arginine activation of n-acetylglutamate synthase. Scientific Reports, Feb 2021. URL: https://doi.org/10.1038/s41598-021-82994-8, doi:10.1038/s41598-021-82994-8. This article has 16 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](NAGS-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. shi2015thenacetylglutamatesynthase pages 3-6
2. caldovic2010nacetylglutamatesynthasestructure pages 4-5
3. shi2015thenacetylglutamatesynthase pages 1-3
4. caldovic2010nacetylglutamatesynthasestructure pages 1-2
5. caldovic2010nacetylglutamatesynthasestructure pages 2-4
6. caldovic2003nacetylglutamateandits pages 7-8
7. shi2015thenacetylglutamatesynthase pages 8-11
8. haskins2016effectofarginine pages 1-2
9. singh2024theefficacyof pages 1-2
10. caldovic2024dataminingapproachesfor pages 2-4
11. mew2011nacetylglutamatesynthasedeficiency pages 5-6
12. kenneson2020presentationandmanagement pages 6-7
13. caldovic2024dataminingapproachesfor pages 4-6
14. caldovic2010nacetylglutamatesynthasestructure pages 5-7
15. gougeard2024useofpure pages 14-16
16. shi2015thenacetylglutamatesynthase pages 6-8
17. shi2015thenacetylglutamatesynthase pages 11-15
18. mew2011nacetylglutamatesynthasedeficiency pages 1-2
19. shi2015thenacetylglutamatesynthase pages 15-17
20. caldovic2003nacetylglutamateandits pages 6-7
21. haskins2008inversionofallosteric pages 9-10
22. sonaimuthu2021genedeliverycorrects pages 1-2
23. sonaimuthu2021genedeliverycorrects pages 8-11
24. haskins2008inversionofallosteric pages 8-9
25. haskins2008inversionofallosteric pages 1-2
26. haskins2008inversionofallosteric pages 4-5
27. qu2007anovelbifunctional pages 11-12
28. logt2016hyperammonemiadueto pages 2-4
29. caldovic2024dataminingapproachesfor pages 1-2
30. sonaimuthu2021genedeliverycorrects pages 5-6
31. sonaimuthu2021genedeliverycorrects pages 6-8
32. https://doi.org/10.1016/j.ymgme.2003.10.017,
33. https://doi.org/10.1016/j.ymgme.2010.02.018,
34. https://doi.org/10.1002/jimd.12687,
35. https://doi.org/10.3390/ijms160613004,
36. https://doi.org/10.1042/bj20030002,
37. https://doi.org/10.2147/tacg.s12702,
38. https://doi.org/10.1186/s13023-024-03167-0,
39. https://doi.org/10.1038/srep38711,
40. https://doi.org/10.1186/1471-2091-9-24,
41. https://doi.org/10.1038/s41598-021-82994-8,
42. https://doi.org/10.1186/1471-2091-8-4,
43. https://doi.org/10.1186/s13023-020-01560-z,
44. https://doi.org/10.1007/8904\_2016\_565,
45. https://doi.org/10.1002/jimd.12747,