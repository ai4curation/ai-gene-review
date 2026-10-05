---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-08T20:02:15.678984'
end_time: '2026-09-08T20:11:46.912910'
duration_seconds: 571.23
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: NEUCR
  gene_id: NCU06005
  gene_symbol: NCU06005
  uniprot_accession: Q7S2F2
  protein_description: 'RecName: Full=glycerol kinase {ECO:0000256|ARBA:ARBA00012099};
    EC=2.7.1.30 {ECO:0000256|ARBA:ARBA00012099}; AltName: Full=ATP:glycerol 3-phosphotransferase
    {ECO:0000256|ARBA:ARBA00043149};'
  gene_info: ORFNames=NCU06005 {ECO:0000313|EMBL:EAA29577.3};
  organism_full: Neurospora crassa (strain ATCC 24698 / 74-OR23-1A / CBS 708.71 /
    DSM 1257 / FGSC 987).
  protein_family: Belongs to the FGGY kinase family.
  protein_domains: ATPase_NBD. (IPR043129); Carb_kinase_FGGY. (IPR000577); Carb_kinase_FGGY_CS.
    (IPR018483); FGGY_C. (IPR018485); FGGY_N. (IPR018484)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 12
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: NCU06005-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q7S2F2
- **Protein Description:** RecName: Full=glycerol kinase {ECO:0000256|ARBA:ARBA00012099}; EC=2.7.1.30 {ECO:0000256|ARBA:ARBA00012099}; AltName: Full=ATP:glycerol 3-phosphotransferase {ECO:0000256|ARBA:ARBA00043149};
- **Gene Information:** ORFNames=NCU06005 {ECO:0000313|EMBL:EAA29577.3};
- **Organism (full):** Neurospora crassa (strain ATCC 24698 / 74-OR23-1A / CBS 708.71 / DSM 1257 / FGSC 987).
- **Protein Family:** Belongs to the FGGY kinase family.
- **Key Domains:** ATPase_NBD. (IPR043129); Carb_kinase_FGGY. (IPR000577); Carb_kinase_FGGY_CS. (IPR018483); FGGY_C. (IPR018485); FGGY_N. (IPR018484)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "NCU06005" matches the protein description above**
2. **Verify the organism is correct:** Neurospora crassa (strain ATCC 24698 / 74-OR23-1A / CBS 708.71 / DSM 1257 / FGSC 987).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'NCU06005' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **NCU06005** (gene ID: NCU06005, UniProt: Q7S2F2) in NEUCR.

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
- **UniProt Accession:** Q7S2F2
- **Protein Description:** RecName: Full=glycerol kinase {ECO:0000256|ARBA:ARBA00012099}; EC=2.7.1.30 {ECO:0000256|ARBA:ARBA00012099}; AltName: Full=ATP:glycerol 3-phosphotransferase {ECO:0000256|ARBA:ARBA00043149};
- **Gene Information:** ORFNames=NCU06005 {ECO:0000313|EMBL:EAA29577.3};
- **Organism (full):** Neurospora crassa (strain ATCC 24698 / 74-OR23-1A / CBS 708.71 / DSM 1257 / FGSC 987).
- **Protein Family:** Belongs to the FGGY kinase family.
- **Key Domains:** ATPase_NBD. (IPR043129); Carb_kinase_FGGY. (IPR000577); Carb_kinase_FGGY_CS. (IPR018483); FGGY_C. (IPR018485); FGGY_N. (IPR018484)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "NCU06005" matches the protein description above**
2. **Verify the organism is correct:** Neurospora crassa (strain ATCC 24698 / 74-OR23-1A / CBS 708.71 / DSM 1257 / FGSC 987).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'NCU06005' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **NCU06005** (gene ID: NCU06005, UniProt: Q7S2F2) in NEUCR.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Neurospora crassa* NCU06005 / UniProt Q7S2F2

## Executive conclusion

The exact target is **NCU06005 (UniProt Q7S2F2)** from *Neurospora crassa* strain ATCC 24698/74-OR23-1A/CBS 708.71/DSM 1257/FGSC 987, commonly represented by the OR74A reference genome. The supplied UniProt record annotates the product as an **FGGY-family glycerol kinase** (EC 2.7.1.30; ATP:glycerol 3-phosphotransferase) with FGGY_N, FGGY_C, carbohydrate-kinase, and ATPase nucleotide-binding signatures. No conflicting use of “NCU06005” for another organism or protein was found.

However, **the literature retrieved contains no direct experimental characterization of NCU06005/Q7S2F2**. No study was found reporting purified-enzyme activity, substrate kinetics, deletion/complementation, isotope tracing, structure, or localization for this exact locus. Accordingly, “glycerol kinase” should be treated as a **credible but computationally inferred annotation**, not an experimentally established function. This caution is important because glycerol-kinase-like homologs can diverge or lack detectable glycerol-kinase activity, and distant homologs can have different cellular targeting (agosto2006conservedfamilyof pages 7-8).

| Claim | Conclusion | Evidence type | Confidence | Key limitation |
|---|---|---|---|---|
| Identity and organism | Q7S2F2 corresponds to ORF **NCU06005** in *Neurospora crassa* strain 74-OR23-1A/OR74A and is annotated as glycerol kinase. | Supplied UniProt record; database annotation | High for record identity; moderate for function | The accession–ORF mapping was not independently validated by a gene-specific publication found in the literature search. |
| Predicted FGGY domains | The protein is predicted to contain the complementary **FGGY_N** and **FGGY_C** regions, an ATPase nucleotide-binding domain, and FGGY carbohydrate-kinase signatures, consistent with an FGGY-family kinase. | Supplied UniProt/InterPro computational annotation | High for predicted architecture; moderate for functional interpretation | No NCU06005 structure, mutagenesis, ligand-binding assay, or purified-enzyme study was found. Domains establish family membership more securely than exact substrate. |
| Proposed glycerol-kinase reaction | The annotation proposes **ATP + glycerol → ADP + sn-glycerol-3-phosphate** (EC 2.7.1.30), ordinarily Mg²⁺ dependent. This is the canonical glycerol-kinase reaction described in comparative literature. (agosto2006conservedfamilyof pages 1-2) | Supplied UniProt annotation plus general glycerol-kinase literature | Moderate | The reaction has not been demonstrated directly with purified Q7S2F2 or an NCU06005-dependent cellular assay. |
| Substrate specificity | **Glycerol is the leading predicted acceptor substrate and ATP the predicted phosphate donor**, but specificity is unverified; FGGY-family membership alone cannot exclude another carbohydrate or polyol substrate. | Annotation and cautious family-based inference | Low–moderate | No kinetic constants, substrate panel, metabolite rescue, isotope tracing, or catalytic-mutant data exist for NCU06005; GK-like homologs can diverge or even lack GK activity. (agosto2006conservedfamilyof pages 7-8) |
| Pathway role | If the annotation is correct, NCU06005 initiates glycerol assimilation by producing glycerol-3-phosphate, connecting glycerol utilization with central carbon metabolism and glycerolipid/phosphoglyceride synthesis. (agosto2006conservedfamilyof pages 1-2) | General biochemical pathway knowledge transferred from glycerol kinases | Moderate for the biochemical consequence; low–moderate for this locus | The downstream fate of glycerol-3-phosphate and pathway flux have not been measured in an NCU06005 mutant. |
| Cellular localization | A **soluble intracellular, probably cytosolic** location is the most conservative hypothesis for an ATP-dependent glycerol-assimilation enzyme; mitochondrial or other compartmental localization is not established. | Bioinformatic/biochemical inference; comparison with distant homologs | Low | No NCU06005 fluorescent fusion, fractionation, organellar proteomics, signal-peptide analysis, or targeting-sequence experiment was identified. Distant GK homologs show variable localization, so mitochondrial assignments cannot be transferred safely. (agosto2006conservedfamilyof pages 4-5, agosto2006conservedfamilyof pages 7-8) |
| *Neurospora* cold induction | Older literature summarized in a comparative study reports cold-induced glycerol-kinase activity in *N. crassa*. (agosto2006conservedfamilyof pages 5-7, agosto2006conservedfamilyof pages 11-12) | Species-level physiological evidence reported secondarily | Low for attribution to NCU06005 | The observation predates assignment to this ORF and does not show that NCU06005 encodes the induced activity; no locus-specific expression or knockout evidence was provided. |
| Gene-specific experimental evidence | No publication located in the searches explicitly tested **NCU06005/Q7S2F2** by deletion, complementation, biochemistry, structural analysis, localization, or targeted expression measurement. | Systematic literature-search result/evidence gap | High confidence that the retrieved literature lacks direct evidence | Absence from retrieved literature is not proof that no unpublished, unindexed, or database-linked dataset exists. |
| 2023–2024 evidence | Recent *N. crassa* studies retrieved used transcriptomics and other genome-scale methods, but none supplied direct functional evidence for NCU06005. Contemporary work illustrates that hundreds of genes can change expression—424 in one 2023 NO-scavenging study—without validating a particular enzyme annotation. | Recent high-throughput literature; negative gene-specific finding | High for lack of direct evidence in retrieved 2023–2024 sources | Genome-wide differential expression is indirect and cannot establish reaction, substrate, or localization. Earlier systems analysis also warned that over one-third of overlapping annotations in a reconstructed *N. crassa* network were incorrect or outdated. (samal2017networkreconstructionand pages 14-15) |


*Table: Evidence hierarchy separating the supplied database annotation from direct literature and homolog-based inference. It highlights that identity and domain architecture are comparatively secure, whereas catalytic specificity, pathway assignment, and localization remain experimentally unvalidated.*

## 1. Identity verification

### Accession, gene, and organism

The supplied identity is internally consistent:

- **UniProt:** Q7S2F2
- **ORF:** NCU06005
- **Organism:** *Neurospora crassa*, reference strain 74-OR23-1A/OR74A and equivalent culture-collection designations listed above
- **Proposed product:** glycerol kinase
- **Proposed EC number:** EC 2.7.1.30
- **Family:** FGGY carbohydrate-kinase family

The exact-accession and exact-symbol searches produced no gene-specific papers and no evidence that the symbol had been confused with another protein. Human **FGGY carbohydrate kinase domain-containing protein**, bacterial LsrK, and glycerol kinases from animals or plants are different proteins and were not treated as evidence about NCU06005 itself.

### Domain-family agreement

The supplied InterPro assignments—ATPase_NBD (IPR043129), Carb_kinase_FGGY (IPR000577), its conserved signature (IPR018483), FGGY_C (IPR018485), and FGGY_N (IPR018484)—are mutually consistent with an FGGY-family ATP-dependent carbohydrate/polyol kinase. This architecture supports **kinase-family membership more strongly than it supports glycerol as the exact substrate**. Comparative studies also show that conserved ATP-, ADP-, and glycerol-binding residues can strengthen a glycerol-kinase assignment, but such residue-level validation was not available for Q7S2F2 in the retrieved evidence (agosto2006conservedfamilyof pages 4-5).

## 2. Proposed primary biochemical function

### Reaction

If the UniProt annotation is correct, Q7S2F2 catalyzes:

**glycerol + ATP → sn-glycerol-3-phosphate + ADP**

The canonical glycerol-kinase reaction is generally Mg²⁺ dependent. Comparative biochemical literature describes this phosphorylation as the obligatory entry step for glycerol utilization and as a connection between carbohydrate and lipid metabolism (agosto2006conservedfamilyof pages 1-2).

**Evidence grade: moderate.** The chemistry is well established for bona fide glycerol kinases, and the domain annotation is compatible with ATP-dependent phosphorylation. It has not been demonstrated using purified Q7S2F2 or an NCU06005-dependent assay.

### Substrate specificity

The leading hypothesis is that the acceptor is **glycerol** and the phosphate donor is **ATP**. Nevertheless, substrate specificity remains the largest uncertainty in the annotation. FGGY-family architecture by itself identifies a carbohydrate/polyol kinase fold but does not uniquely identify the phosphorylated metabolite. Even among proteins described as glycerol-kinase-like, catalytic function may diverge (agosto2006conservedfamilyof pages 7-8).

Therefore, there is currently no defensible NCU06005-specific value for **Kₘ**, **kcat**, catalytic efficiency, nucleotide-donor preference, metal dependence, or activity toward alternative polyols. Claims that Q7S2F2 is strictly glycerol-specific would exceed the available evidence.

## 3. Biological process and pathway context

If Q7S2F2 is a glycerol kinase, its immediate biological role is **glycerol assimilation**. Formation of glycerol-3-phosphate traps imported glycerol intracellularly and generates a metabolite that can be routed toward:

1. **Central carbon and energy metabolism**, after oxidation and conversion into glycolytic intermediates; or
2. **Glycerolipid and phosphoglyceride synthesis**, where glycerol-3-phosphate supplies the glycerol backbone.

General glycerol-kinase literature describes glycerol-3-phosphate as entering glycolysis and being incorporated into diacylglycerols and phosphoglycerides (agosto2006conservedfamilyof pages 1-2). These are pathway-level consequences of the proposed reaction, not demonstrated NCU06005-specific fluxes.

A broader stress-signaling role should not be asserted. *N. crassa* accumulates glycerol during osmotic-stress responses, but glycerol **biosynthesis** and glycerol **assimilation by phosphorylation** are directionally different processes. Consequently, evidence for HOG/p38-dependent glycerol accumulation does not establish that NCU06005 produces the osmolyte or functions directly in that signaling pathway.

Older literature summarized in a comparative glycerol-kinase study reports that *N. crassa* glycerol-kinase activity is induced by cold (agosto2006conservedfamilyof pages 5-7, agosto2006conservedfamilyof pages 11-12). This provides species-level plausibility for a role in temperature-dependent glycerol metabolism, but the historical activity was not mapped to NCU06005. It cannot be used as locus-specific proof.

## 4. Cellular localization

No direct localization evidence was found for Q7S2F2. There is no retrieved report of an NCU06005–GFP fusion, organellar fractionation, immunolocalization, proximity labeling, or compartment-resolved proteomics.

The most conservative working model is a **soluble intracellular enzyme, probably cytosolic**, because it is proposed to use ATP to phosphorylate intracellular glycerol and is not described as a transporter or secreted enzyme. Confidence is low, however. Glycerol-kinase homologs in other lineages can possess mitochondrial-targeting or transmembrane features, and comparative evidence explicitly shows that these features vary between paralogs (agosto2006conservedfamilyof pages 4-5, agosto2006conservedfamilyof pages 7-8). Thus, mitochondrial, peroxisomal, or other compartmental assignments should not be transferred to NCU06005 without sequence-specific targeting analysis and experimental validation.

## 5. Experimental evidence versus inference

### Direct evidence for NCU06005

No retrieved publication explicitly reported any of the following:

- NCU06005 deletion phenotype on glycerol;
- rescue by reintroducing NCU06005;
- loss or restoration of glycerol-kinase activity;
- purified Q7S2F2 kinetics;
- a substrate-screening panel;
- catalytic-residue mutagenesis;
- glycerol-to-glycerol-3-phosphate isotope tracing;
- Q7S2F2 structure or ligand-bound model validated experimentally; or
- cellular localization.

This makes NCU06005 a case where **identity and family architecture are comparatively secure, but precise biochemical function and localization remain provisional**.

### Why expert caution is warranted

A systems reconstruction of *N. crassa* metabolism emphasized the value of combining genomics, transcriptomics, proteomics, genetics, and biochemical characterization. In that analysis, functional-genomics support covered 145 of 168 network genes, transcriptomic support 106 of 168, and proteomic support 68 of 168; none of these results was reported specifically for NCU06005 (samal2017networkreconstructionand pages 4-6). The same work found that more than one-third of genes shared with an earlier metabolic model had incorrect or outdated annotations, demonstrating that database assignments in *N. crassa* should not automatically be regarded as experimentally validated (samal2017networkreconstructionand pages 14-15). Published September 2017: https://doi.org/10.1186/s13068-017-0901-2.

## 6. Recent research, 2023–2024

No 2023–2024 source retrieved directly characterized NCU06005/Q7S2F2. Recent *N. crassa* research increasingly uses RNA-seq and metabolomics to connect genes with metabolism, but these approaches remain indirect unless paired with locus-specific genetics and biochemical assays.

For example, a 2023 RNA-seq study of nitric-oxide scavenging reported **424 differentially transcribed genes**, many associated with carbohydrate and amino-acid metabolism, but did not establish NCU06005's reaction, substrate, or localization. Published October 2023: https://doi.org/10.3390/jof9100985. Likewise, a 2024 RNA-seq/metabolomics analysis of RIC8 and G-protein mutants reported 159 misregulated genes in one mutant and more than 1,000 in two others, illustrating the scope of modern *Neurospora* systems biology rather than furnishing NCU06005-specific evidence. Published December 2024: https://doi.org/10.1128/mbio.03133-24.

The current research gap is therefore not merely a lack of recent review coverage; it is the absence of direct functional experiments on this locus.

## 7. Applications and real-world implementation

No industrial, agricultural, clinical, or synthetic-biology implementation specifically involving NCU06005 was found. Its **potential** relevance is as a target for engineering glycerol assimilation, carbon partitioning, or glycerolipid precursor supply in filamentous fungi, but that remains hypothetical.

Before engineering applications are justified, the annotation should be validated. A rigorous experimental program would include:

1. Growth comparisons of wild type, ΔNCU06005, and complemented strains on glycerol versus glucose and other polyols;
2. Intracellular measurement of glycerol and sn-glycerol-3-phosphate;
3. Purification of Q7S2F2 and determination of ATP-dependent activity across glycerol, erythritol, ribitol, xylitol, and related carbohydrates;
4. Kinetic measurement of Kₘ, kcat, metal dependence, and nucleotide preference;
5. Catalytic-site mutagenesis guided by FGGY-family alignments;
6. Stable-isotope tracing from labeled glycerol into central metabolites and glycerolipids; and
7. Endogenous fluorescent tagging plus biochemical fractionation to establish localization.

A decisive annotation would require concordance between the knockout phenotype, complementation, metabolite changes, and purified-enzyme specificity.

## Final assessment

**Recommended functional annotation:** “Putative FGGY-family glycerol kinase; predicted to catalyze ATP-dependent phosphorylation of glycerol to sn-glycerol-3-phosphate.”

**Recommended biological-process annotation:** “Putative glycerol assimilation and glycerol-3-phosphate metabolism, potentially linking central carbon metabolism with glycerolipid biosynthesis.”

**Recommended localization annotation:** “Intracellular; cytosolic localization predicted only tentatively.”

**Overall confidence:** high for accession–ORF–organism identity and predicted FGGY architecture; moderate for ATP-dependent carbohydrate/polyol kinase activity; low-to-moderate for glycerol as the physiological substrate; low for cellular localization and pathway regulation.

The gene symbol is not demonstrably ambiguous, but **literature is limited for this specific protein**. Accordingly, the precise function should be inferred only from the supplied UniProt/domain annotation and general glycerol-kinase biochemistry, with no claim of direct experimental validation.

References

1. (agosto2006conservedfamilyof pages 7-8): Julian A. Martinez Agosto and Edward R.B. McCabe. Conserved family of glycerol kinase loci in drosophila melanogaster. Molecular genetics and metabolism, 88 4:334-45, Aug 2006. URL: https://doi.org/10.1016/j.ymgme.2006.01.002, doi:10.1016/j.ymgme.2006.01.002. This article has 37 citations and is from a peer-reviewed journal.

2. (agosto2006conservedfamilyof pages 1-2): Julian A. Martinez Agosto and Edward R.B. McCabe. Conserved family of glycerol kinase loci in drosophila melanogaster. Molecular genetics and metabolism, 88 4:334-45, Aug 2006. URL: https://doi.org/10.1016/j.ymgme.2006.01.002, doi:10.1016/j.ymgme.2006.01.002. This article has 37 citations and is from a peer-reviewed journal.

3. (agosto2006conservedfamilyof pages 4-5): Julian A. Martinez Agosto and Edward R.B. McCabe. Conserved family of glycerol kinase loci in drosophila melanogaster. Molecular genetics and metabolism, 88 4:334-45, Aug 2006. URL: https://doi.org/10.1016/j.ymgme.2006.01.002, doi:10.1016/j.ymgme.2006.01.002. This article has 37 citations and is from a peer-reviewed journal.

4. (agosto2006conservedfamilyof pages 5-7): Julian A. Martinez Agosto and Edward R.B. McCabe. Conserved family of glycerol kinase loci in drosophila melanogaster. Molecular genetics and metabolism, 88 4:334-45, Aug 2006. URL: https://doi.org/10.1016/j.ymgme.2006.01.002, doi:10.1016/j.ymgme.2006.01.002. This article has 37 citations and is from a peer-reviewed journal.

5. (agosto2006conservedfamilyof pages 11-12): Julian A. Martinez Agosto and Edward R.B. McCabe. Conserved family of glycerol kinase loci in drosophila melanogaster. Molecular genetics and metabolism, 88 4:334-45, Aug 2006. URL: https://doi.org/10.1016/j.ymgme.2006.01.002, doi:10.1016/j.ymgme.2006.01.002. This article has 37 citations and is from a peer-reviewed journal.

6. (samal2017networkreconstructionand pages 14-15): Areejit Samal, James P. Craig, Samuel T. Coradetti, J. Philipp Benz, James A. Eddy, Nathan D. Price, and N. Louise Glass. Network reconstruction and systems analysis of plant cell wall deconstruction by neurospora crassa. Sep 2017. URL: https://doi.org/10.1186/s13068-017-0901-2, doi:10.1186/s13068-017-0901-2. This article has 53 citations.

7. (samal2017networkreconstructionand pages 4-6): Areejit Samal, James P. Craig, Samuel T. Coradetti, J. Philipp Benz, James A. Eddy, Nathan D. Price, and N. Louise Glass. Network reconstruction and systems analysis of plant cell wall deconstruction by neurospora crassa. Sep 2017. URL: https://doi.org/10.1186/s13068-017-0901-2, doi:10.1186/s13068-017-0901-2. This article has 53 citations.

## Artifacts

- [Edison artifact artifact-00](NCU06005-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. agosto2006conservedfamilyof pages 7-8
2. agosto2006conservedfamilyof pages 1-2
3. samal2017networkreconstructionand pages 14-15
4. agosto2006conservedfamilyof pages 4-5
5. samal2017networkreconstructionand pages 4-6
6. agosto2006conservedfamilyof pages 5-7
7. agosto2006conservedfamilyof pages 11-12
8. https://doi.org/10.1186/s13068-017-0901-2.
9. https://doi.org/10.3390/jof9100985.
10. https://doi.org/10.1128/mbio.03133-24.
11. https://doi.org/10.1016/j.ymgme.2006.01.002,
12. https://doi.org/10.1186/s13068-017-0901-2,