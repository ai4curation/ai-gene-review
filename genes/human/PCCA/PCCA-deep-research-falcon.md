---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-07T00:28:55.688277'
end_time: '2026-07-07T00:48:23.487410'
duration_seconds: 1167.8
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: P05165
  gene_symbol: PCCA
  uniprot_accession: P05165
  protein_description: 'RecName: Full=Propionyl-CoA carboxylase alpha chain, mitochondrial
    {ECO:0000305|PubMed:2740237}; Short=PCCase subunit alpha; EC=6.4.1.3 {ECO:0000269|PubMed:6765947,
    ECO:0000269|PubMed:8434582}; AltName: Full=Propanoyl-CoA:carbon dioxide ligase
    subunit alpha; Flags: Precursor;'
  gene_info: Name=PCCA {ECO:0000312|HGNC:HGNC:8653};
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: ATP-grasp. (IPR011761); ATP_grasp_subdomain_1. (IPR013815); BC-like_N.
    (IPR005481); Biotin_BS. (IPR001882); Biotin_carboxylase_complex. (IPR050856)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 33
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PCCA-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PCCA-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P05165
- **Protein Description:** RecName: Full=Propionyl-CoA carboxylase alpha chain, mitochondrial {ECO:0000305|PubMed:2740237}; Short=PCCase subunit alpha; EC=6.4.1.3 {ECO:0000269|PubMed:6765947, ECO:0000269|PubMed:8434582}; AltName: Full=Propanoyl-CoA:carbon dioxide ligase subunit alpha; Flags: Precursor;
- **Gene Information:** Name=PCCA {ECO:0000312|HGNC:HGNC:8653};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** ATP-grasp. (IPR011761); ATP_grasp_subdomain_1. (IPR013815); BC-like_N. (IPR005481); Biotin_BS. (IPR001882); Biotin_carboxylase_complex. (IPR050856)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PCCA" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PCCA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PCCA** (gene ID: P05165, UniProt: P05165) in human.

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
- **UniProt Accession:** P05165
- **Protein Description:** RecName: Full=Propionyl-CoA carboxylase alpha chain, mitochondrial {ECO:0000305|PubMed:2740237}; Short=PCCase subunit alpha; EC=6.4.1.3 {ECO:0000269|PubMed:6765947, ECO:0000269|PubMed:8434582}; AltName: Full=Propanoyl-CoA:carbon dioxide ligase subunit alpha; Flags: Precursor;
- **Gene Information:** Name=PCCA {ECO:0000312|HGNC:HGNC:8653};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** ATP-grasp. (IPR011761); ATP_grasp_subdomain_1. (IPR013815); BC-like_N. (IPR005481); Biotin_BS. (IPR001882); Biotin_carboxylase_complex. (IPR050856)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PCCA" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PCCA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PCCA** (gene ID: P05165, UniProt: P05165) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: PCCA (Propionyl-CoA Carboxylase Alpha Chain, Mitochondrial)

**Gene:** PCCA | **UniProt:** P05165 | **EC:** 6.4.1.3 | **Organism:** Homo sapiens

## 1. Gene and Protein Overview

The *PCCA* gene (HGNC:8653) is located on human chromosome 13 and encodes the alpha (α) subunit of propionyl-CoA carboxylase (PCC), a biotin-dependent mitochondrial enzyme (kelson1996chaperoninmediatedassemblyof pages 1-2). The α subunit has a molecular mass of approximately 70 kDa and is synthesized as a precursor protein containing an N-terminal mitochondrial targeting presequence of approximately 25 amino acids, which is proteolytically cleaved upon import into the mitochondrial matrix, yielding a mature protein beginning at residue 26 (kelson1996chaperoninmediatedassemblyof pages 2-3, kelson1996chaperoninmediatedassemblyof pages 1-2). The gene product functions together with the β subunit (encoded by *PCCB*) to form the active holoenzyme.

The following table summarizes the key properties of PCCA:

| Property | Summary |
|---|---|
| Gene name | **PCCA**; encodes the mitochondrial **propionyl-CoA carboxylase alpha chain** in human, matching UniProt accession **P05165** (kelson1996chaperoninmediatedassemblyof pages 1-2) |
| UniProt accession | **P05165** (user-provided target context) |
| Chromosomal location | **Chromosome 13** in human (kelson1996chaperoninmediatedassemblyof pages 1-2) |
| Protein size | **~70 kDa** alpha subunit of PCC (kelson1996chaperoninmediatedassemblyof pages 1-2) |
| Enzyme classification | **EC 6.4.1.3**, propionyl-CoA carboxylase (erdal2025aminoacidmetabolism pages 9-10, kelson1996chaperoninmediatedassemblyof pages 1-2) |
| Cofactor | **Biotin**; PCC is a **biotin-dependent carboxylase** (erdal2025aminoacidmetabolism pages 9-10, jitrapakdee2003thebiotinenzyme pages 4-6) |
| Reaction catalyzed | **Propionyl-CoA + HCO3− + ATP → D-methylmalonyl-CoA + ADP + Pi**; ATP-dependent biotin-mediated carboxylation (erdal2025aminoacidmetabolism pages 9-10, kelson1996chaperoninmediatedassemblyof pages 1-2, zhou2024structuralinsightsinto pages 4-6) |
| Subcellular localization | **Mitochondrial matrix** (kelson1996chaperoninmediatedassemblyof pages 1-2) |
| Mitochondrial targeting | Synthesized as a precursor with an **N-terminal mitochondrial leader/presequence**; mature alpha subunit begins at about **residue 26**, implying a ~25 aa targeting peptide (kelson1996chaperoninmediatedassemblyof pages 2-3, kelson1996chaperoninmediatedassemblyof pages 1-2) |
| Holoenzyme assembly | **α6β6 dodecamer**; four-layer architecture with six β subunits forming the core and α subunits arranged on top and bottom (kelson1996chaperoninmediatedassemblyof pages 1-2, zhou2024structuralinsightsinto pages 4-6, zhou2024structuralinsightsinto pages 1-4) |
| Key domains | **Alpha/PCCA:** **BC** (biotin carboxylase), **BT** linker/hub domain, **BCCP** (biotin carboxyl carrier protein); **Beta/PCCB:** **CT** (carboxyltransferase) domain with CT-N and CT-C subdomains (zhou2024structuralinsightsinto pages 4-6, zhou2024structuralinsightsinto pages 1-4, jitrapakdee2003thebiotinenzyme pages 4-6) |
| Primary metabolic pathway | **Propionate metabolism**: propionyl-CoA → D-methylmalonyl-CoA → L-methylmalonyl-CoA → **succinyl-CoA**, which enters the **TCA cycle** and supports gluconeogenesis (erdal2025aminoacidmetabolism pages 9-10, erdal2025aminoacidmetabolism pages 6-9) |
| Metabolic inputs to pathway | Propionyl-CoA arises from catabolism of **isoleucine, valine, threonine, methionine**, **odd-chain fatty acids**, and **cholesterol side chains** (kelson1996chaperoninmediatedassemblyof pages 1-2, erdal2025aminoacidmetabolism pages 9-10, erdal2025aminoacidmetabolism pages 6-9) |
| Disease association | Biallelic loss-of-function variants in **PCCA** cause **propionic acidemia**, a severe autosomal recessive organic acidemia with metabolic decompensation, neurologic disease, and cardiomyopathy risk (maines2023understandingthepathogenesis pages 1-2, riverabarahona2018identificationof34 pages 1-5) |
| Substrate specificity | **Primary substrate:** propionyl-CoA. Human PCC can also carboxylate **acetyl-CoA** at a much lower rate, about **1.5%** of the propionyl-CoA rate; recent structural work found acetyl-CoA and propionyl-CoA bind in highly similar modes (zhou2024structuralinsightsinto pages 6-7, jitrapakdee2003thebiotinenzyme pages 10-11) |
| Representative recent structural data | High-resolution human PCC cryo-EM structures reported in 2024: **apo 3.02 Å**, **propionyl-CoA-bound 2.80 Å**, with overall structures reported in the **2.29–3.38 Å** range; PDB entries include **8XL3, 8XL4, 8XL5** (zhou2024structuralinsightsinto pages 4-6, zhou2024structuralinsightsinto pages 11-14, zhou2024structuralinsightsinto pages 9-11) |


*Table: This table summarizes the core molecular, biochemical, structural, and disease-related properties of human PCCA/propionyl-CoA carboxylase alpha chain. It is useful as a compact reference for functional annotation and for linking enzyme function to propionic acidemia.*

## 2. Enzymatic Function and Reaction Mechanism

PCC catalyzes the ATP-dependent, biotin-mediated carboxylation of propionyl-CoA to produce D-methylmalonyl-CoA, using bicarbonate (HCO₃⁻) as the CO₂ donor (erdal2025aminoacidmetabolism pages 9-10, kelson1996chaperoninmediatedassemblyof pages 1-2). This reaction (EC 6.4.1.3) proceeds via a two-step mechanism characteristic of all biotin-dependent carboxylases:

**Step 1 — Biotin carboxylation (in the BC domain of the α subunit):** ATP activates bicarbonate to form a carboxyphosphate intermediate, which then transfers its carboxyl group to the N1′ atom of the covalently attached biotin prosthetic group (zhou2024structuralinsightsinto pages 4-6).

**Step 2 — Carboxyl transfer (in the CT domain of the β subunit):** The carboxylated biotin swings from the BC domain to the CT domain, where the carboxyl group is transferred to the C-α of propionyl-CoA, generating D-methylmalonyl-CoA. This process involves decarboxylation of carboxybiotin to produce free CO₂ and activated biotin, followed by deprotonation of the acyl moiety to attack the CO₂ (zhou2024structuralinsightsinto pages 4-6).

### Substrate Specificity

PCC exhibits strong selectivity for propionyl-CoA as its primary substrate. However, recent cryo-EM structural analyses have demonstrated that PCC can also carboxylate acetyl-CoA, albeit at a dramatically reduced rate—approximately 1.5% of the propionyl-CoA carboxylation rate (zhou2024structuralinsightsinto pages 6-7). Structural studies revealed that propionyl-CoA and acetyl-CoA bind to PCC with nearly identical binding modes, indicating that the acyl-CoA specificity is largely attributable to subtle differences in interactions mediated by the acyl groups, although these differences were not fully resolved in the available cryo-EM densities (zhou2024structuralinsightsinto pages 6-7, zhou2024structuralinsightsinto pages 4-6). The carboxyltransferase domains of PCC, acetyl-CoA carboxylase, and 3-methylcrotonyl-CoA carboxylase show no sequence identity, underscoring the uniqueness of each enzyme's substrate binding site (jitrapakdee2003thebiotinenzyme pages 10-11).

## 3. Protein Structure and Domain Architecture

### Domain Organization

The PCCA-encoded α subunit contains three functional domains arranged from N- to C-terminus (zhou2024structuralinsightsinto pages 4-6, zhou2024structuralinsightsinto pages 1-4, jitrapakdee2003thebiotinenzyme pages 4-6):

- **Biotin carboxylase (BC) domain:** Located at the N-terminus, this domain contains the ATP-grasp fold and catalyzes the first half-reaction—the ATP-dependent carboxylation of the covalently attached biotin cofactor using bicarbonate as the CO₂ source.

- **BT (BC-CT interaction) domain:** An intermediate hub domain that mediates interactions between the BC and CT functional regions.

- **Biotin carboxyl carrier protein (BCCP) domain:** Located at the C-terminus, this domain contains the conserved lysine residue to which biotin is covalently attached via an amide bond. The BCCP domain positions the biotinyl group adjacent to the acyl-CoA binding pocket in the CT domain.

The β subunit (encoded by *PCCB*) consists solely of the carboxyltransferase (CT) domain, which is divided into CT-N and CT-C subdomains. The CT domain catalyzes the second half-reaction—transfer of the carboxyl group from carboxybiotin to propionyl-CoA (zhou2024structuralinsightsinto pages 4-6).

### Holoenzyme Assembly

The PCC holoenzyme assembles as an α₆β₆ dodecamer with a distinctive four-layer architecture: six β subunits form the core in two layers, with six α subunits positioned at the top and bottom in two additional layers. Each α subunit binds to one β subunit (kelson1996chaperoninmediatedassemblyof pages 1-2, zhou2024structuralinsightsinto pages 4-6, zhou2024structuralinsightsinto pages 1-4). The assembly of the holoenzyme requires molecular chaperones; studies in *E. coli* expression systems demonstrated that chaperonin (GroEL/GroES) facilitates proper folding and assembly of both wild-type and mutant PCC subunits (kelson1996chaperoninmediatedassemblyof pages 1-2).

### High-Resolution Structures

A major structural advance came in 2024, when Zhou et al. reported the first high-resolution cryo-EM structures of human PCC holoenzyme in multiple states: the apo form at 3.02 Å resolution, the propionyl-CoA-bound form (PCC-PCO) at 2.80 Å resolution, and the acetyl-CoA-bound form (PCC-ACO) at 3.38 Å resolution. These structures have been deposited in the Protein Data Bank (PDB entries 8XL3, 8XL4, 8XL5) (zhou2024structuralinsightsinto pages 4-6, zhou2024structuralinsightsinto pages 11-14, zhou2024structuralinsightsinto pages 9-11). Notably, in all PCC structures analyzed, the covalently linked biotin binds to an exo-site distant (>7 Å) from the catalytic residues G437 and A438 in the CT domain, suggesting the enzyme was captured in a catalytically incompetent conformation (zhou2024structuralinsightsinto pages 6-7).

## 4. Subcellular Localization

PCC functions exclusively in the **mitochondrial matrix**, where it processes propionyl-CoA generated from multiple catabolic pathways (kelson1996chaperoninmediatedassemblyof pages 1-2). Both the α and β subunit precursors contain N-terminal mitochondrial matrix targeting presequences. The α subunit precursor undergoes proteolytic cleavage at a conserved motif for mitochondrial-targeted protein processing, with the mature α subunit beginning at approximately residue 26 (kelson1996chaperoninmediatedassemblyof pages 2-3). When expressed with its full-length sequence including the mitochondrial leader in mammalian cells, the β subunit precursor is correctly transported to mitochondria, confirming the functionality of the targeting sequence (kelson1996chaperoninmediatedassemblyof pages 1-2).

## 5. Metabolic Pathways and Biochemical Context

### The Propionate Metabolism Pathway

PCC occupies a critical position in the propionate catabolism pathway, catalyzing the first committed step in the conversion of propionyl-CoA to succinyl-CoA, a TCA cycle intermediate (erdal2025aminoacidmetabolism pages 9-10). The complete pathway proceeds as follows:

1. **Propionyl-CoA → D-methylmalonyl-CoA** (catalyzed by PCC; biotin- and ATP-dependent)
2. **D-methylmalonyl-CoA → L-methylmalonyl-CoA** (catalyzed by methylmalonyl-CoA epimerase)
3. **L-methylmalonyl-CoA → Succinyl-CoA** (catalyzed by methylmalonyl-CoA mutase, requiring vitamin B₁₂)

Succinyl-CoA then enters the TCA cycle and can support gluconeogenesis (erdal2025aminoacidmetabolism pages 9-10, erdal2025aminoacidmetabolism pages 6-9).

### Sources of Propionyl-CoA

Propionyl-CoA is generated from multiple metabolic sources (kelson1996chaperoninmediatedassemblyof pages 1-2, erdal2025aminoacidmetabolism pages 9-10, erdal2025aminoacidmetabolism pages 6-9):

- **Branched-chain amino acid catabolism:** Isoleucine and valine degradation pathways converge to generate propionyl-CoA
- **Other amino acids:** Threonine and methionine catabolism also produce propionyl-CoA
- **Odd-chain fatty acid β-oxidation:** The final three-carbon unit from odd-chain fatty acids yields propionyl-CoA
- **Cholesterol side chain oxidation:** Cholesterol metabolism generates propionyl-CoA
- **Gut microbiome-derived propionate:** The liver is the primary organ for clearing propionate produced by intestinal bacteria (erdal2025aminoacidmetabolism pages 9-10)

The liver is the dominant organ for propionyl-CoA metabolism, with kidney and pancreas also possessing significant metabolic capacity (lu2026lossofpropionylcoa pages 1-5). In healthy individuals, efficient hepatic propionate metabolism maintains low circulating propionate levels (0.4–5 µM) (chen2025elevatedpropionateand pages 2-3).

### Metabolic Consequences of PCCA Deficiency

Studies using CRISPR-edited PCCA-null HepG2 cells have revealed that PCCA deficiency causes widespread metabolic reprogramming beyond simple propionyl-CoA accumulation (lu2026lossofpropionylcoa pages 5-8, lu2026lossofpropionylcoa pages 1-5, lu2026lossofpropionylcoa pages 8-11):

- **Reduced mitochondrial fatty acid oxidation**, with decreased incorporation of fatty acid-derived acetyl-CoA into the TCA cycle
- **Impaired pyruvate anaplerosis** via pyruvate carboxylase, reducing gluconeogenic and lipogenic capacity
- **Reduced branched-chain amino acid catabolism**, evidenced by decreased downstream metabolites
- **CoA and carnitine depletion**, as excess propionyl-CoA sequesters these cofactors
- **Accumulation of toxic metabolites** including methylcitrate, propionylcarnitine, and propionylglutamate, which impair ammonia detoxification and disrupt the TCA cycle (lu2026lossofpropionylcoa pages 1-5)

## 6. Disease Association: Propionic Acidemia

### Clinical Features

Propionic acidemia (PA; OMIM #606054) is an autosomal recessive inborn error of metabolism caused by biallelic mutations in either *PCCA* or *PCCB*, resulting in deficient PCC enzyme activity (maines2023understandingthepathogenesis pages 1-2, riverabarahona2018identificationof34 pages 1-5). The clinical presentation includes:

- **Neonatal/early-onset form:** Ketoacidosis, feeding refusal, lethargy, failure to thrive, seizures, and encephalopathy (riverabarahona2018identificationof34 pages 1-5)
- **Late-onset form:** Milder presentation with developmental delay
- **Neurological complications:** Psychomotor retardation, dystonia, developmental and speech delays, seizures, stroke-like episodes, optic neuropathy, and intellectual disability (chen2025elevatedpropionateand pages 3-4)
- **Cardiac complications:** Hypertrophic or dilated cardiomyopathy and acquired long QT syndrome (aLQTS), which are major causes of morbidity and mortality (maines2023understandingthepathogenesis pages 1-2)
- **Other complications:** Pancreatitis, hyperammonemia, and hematologic abnormalities (riverabarahona2018identificationof34 pages 1-5)

### Pathophysiological Mechanisms

The pathophysiology of PA extends beyond simple metabolite toxicity and involves multiple cellular pathways (maines2023understandingthepathogenesis pages 1-2, maines2023understandingthepathogenesis pages 4-5, chen2025elevatedpropionateand pages 3-4):

- **TCA cycle dysfunction:** Decreased succinyl-CoA availability and inhibition of TCA enzymes (pyruvate dehydrogenase, oxoglutarate dehydrogenase, succinyl-CoA ligase) by propionate and methylcitrate
- **Mitochondrial electron transport chain dysfunction:** Documented deficiencies in complexes I, III, and IV; propionyl-CoA acts as a mitochondrial toxin impairing oxidative phosphorylation
- **Oxidative stress:** Increased reactive oxygen species production; mtDNA depletion and ultrastructural mitochondrial abnormalities
- **Neurological damage:** The basal ganglia are particularly vulnerable due to high energy demands; propionate accumulates in GABAergic neurons where it inhibits GABA transaminase, leading to GABA accumulation and lethargy (chen2025elevatedpropionateand pages 7-7)
- **CoQ10 deficiency, carnitine depletion, and epigenetic/miRNA dysregulation** also contribute to disease pathology (maines2023understandingthepathogenesis pages 11-13)

## 7. Current and Emerging Therapeutic Approaches

The following table summarizes current and emerging therapeutic strategies for propionic acidemia:

| Therapy type | Mechanism | Development stage | Key findings |
|---|---|---|---|
| Conventional management: dietary protein restriction, carnitine supplementation, metronidazole/other antibiotics | Reduces propiogenic substrate load from isoleucine, valine, methionine, threonine and lowers gut microbiota-derived propionate; carnitine promotes formation/excretion of propionylcarnitine and helps maintain carnitine pools | Standard of care / established clinical management | Current treatment is mainly supportive rather than curative. Dietary restriction, carnitine, and metronidazole/antibiotics are widely used and have improved survival, but many patients still develop chronic complications including neurologic and cardiac disease despite metabolic management (riverabarahona2018identificationof34 pages 1-5, erdal2025aminoacidmetabolism pages 9-10) |
| Liver transplantation | Provides a major new source of functional hepatic PCC activity, increasing systemic propionyl-CoA clearance and reducing recurrent metabolic instability | Established option for selected severe patients | Considered for severe disease; can stabilize metabolic control and may improve or reverse cardiomyopathy in some patients, but does not fully cure extrahepatic disease and is limited by transplant eligibility and risks (maines2023understandingthepathogenesis pages 1-2, maines2023understandingthepathogenesis pages 13-14) |
| mRNA-3927 dual mRNA-LNP therapy (encodes PCCA and PCCB) | Intravenous lipid nanoparticle delivery of therapeutic mRNAs to liver cells, enabling translation of both PCC subunits and reconstitution of active PCC enzyme | Clinical; first-in-human Phase 1/2 with interim results published in *Nature* (2024) | In 16 participants across 5 dose cohorts, 346 IV doses were administered over 15.69 person-years with no dose-limiting toxicities. Among 8 participants with pretreatment metabolic decompensation events, treatment was associated with a 70% reduction in risk; biomarkers including 3-HP, 2-MC, propionylcarnitine, and n-propionylglycine generally decreased after treatment (koeberl2024interimanalysesof pages 1-2, koeberl2024interimanalysesof pages 2-3, koeberl2024interimanalysesof pages 5-6) |
| Antisense oligonucleotide therapy targeting PCCA pseudoexon | Splice-switching ASOs suppress aberrant pseudoexon inclusion in mutant PCCA pre-mRNA to restore normal splicing and rescue enzyme expression/activity | Preclinical / experimental personalized RNA therapy | Recent work demonstrated modulation of PCCA pseudoexon splicing as a plausible mutation-specific rescue strategy, highlighting pseudoexon activation as a therapeutically actionable mechanism in propionic acidemia (chen2025elevatedpropionateand pages 7-7) |
| Metabolic rerouting approaches | Diverts upstream propiogenic flux away from propionyl-CoA production, for example by genetically or pharmacologically reducing valine/isoleucine catabolic steps that feed propionate metabolism | Preclinical proof-of-concept | In zebrafish models of disorders of propionyl-CoA metabolism, proximal interruption of valine/isoleucine oxidation improved survival and reduced propionate-derived toxic metabolites, supporting metabolic rerouting as a candidate strategy for PA (chen2025elevatedpropionateand pages 7-7) |


*Table: This table summarizes current and emerging therapeutic approaches for propionic acidemia associated with PCCA deficiency, spanning standard management, transplantation, RNA therapeutics, and experimental metabolic strategies. It is useful for comparing mechanism, maturity, and evidence across interventions.*

### mRNA-3927: A Landmark Clinical Advance

The most significant recent therapeutic development for PA is the first-in-human phase 1/2 clinical trial of mRNA-3927, a dual mRNA therapy encapsulated in lipid nanoparticles (LNPs) that encodes both human PCCA and PCCB subunits. As reported in *Nature* in April 2024, the interim analysis enrolled 16 participants across 5 dose cohorts (0.30–0.90 mg/kg administered intravenously every 2–3 weeks) (koeberl2024interimanalysesof pages 1-2, koeberl2024interimanalysesof pages 2-3). Key findings include:

- A total of 346 intravenous doses were administered over 15.69 person-years of treatment
- No dose-limiting toxicities were observed
- A **70% reduction in the risk of metabolic decompensation events** among the 8 participants who reported them in the 12-month pretreatment period (koeberl2024interimanalysesof pages 1-2)
- Most patients showed reductions in disease biomarkers (3-hydroxypropionate, 2-methylcitrate, propionylcarnitine, and n-propionylglycine) after treatment (koeberl2024interimanalysesof pages 2-3)
- The most common adverse events were pyrexia (68.8%), diarrhea (50%), and vomiting (50%); infusion-related reactions occurred in 31.3% of participants but were generally grade 1–2 (koeberl2024interimanalysesof pages 2-3)
- The mRNA was successfully transported into liver cells, enabling protein translation and post-translational modification into the active PCC enzyme (koeberl2024interimanalysesof pages 5-6)

### Antisense Oligonucleotide Approaches

An innovative personalized therapeutic strategy involves splice-modulating antisense oligonucleotides (ASOs) targeting a PCCA pseudoexon. The c.1285-1416A>G variant in intron 14 of the *PCCA* gene activates a pseudoexon, and ASOs designed to suppress this aberrant splicing event have been shown to rescue normal PCCA mRNA expression and enzyme activity in cellular models (chen2025elevatedpropionateand pages 7-7).

## 8. Evolutionary Context

PCC belongs to the ancient family of biotin-dependent carboxylases, which are widespread across all three domains of life. Phylogenomic analyses suggest that CoA-bearing-substrate carboxylases, including PCC, arose from an ancestral enzyme present in the last common ancestor of Bacteria that could carry out non-specific carboxylation of several CoA-bearing substrates. Eukaryotes most likely acquired their biotin-dependent carboxylases through the mitochondrial endosymbiosis, consistent with the exclusive mitochondrial localization of PCC in eukaryotic cells (jitrapakdee2003thebiotinenzyme pages 4-6). The conserved domain architecture—BC, BCCP, and CT domains—is shared across PCC, acetyl-CoA carboxylase, 3-methylcrotonyl-CoA carboxylase, and pyruvate carboxylase, reflecting their common evolutionary origin, though the CT domains diverge to accommodate different substrate specificities (jitrapakdee2003thebiotinenzyme pages 4-6, jitrapakdee2003thebiotinenzyme pages 10-11).

## 9. Summary

PCCA encodes the α subunit of propionyl-CoA carboxylase, a biotin-dependent mitochondrial matrix enzyme that catalyzes the ATP-dependent carboxylation of propionyl-CoA to D-methylmalonyl-CoA (EC 6.4.1.3). This reaction is the first committed step in the conversion of propionyl-CoA to succinyl-CoA for entry into the TCA cycle. The enzyme functions as an α₆β₆ dodecamer, with the α subunit housing the biotin carboxylase and biotin carboxyl carrier protein domains, and the β subunit providing the carboxyltransferase domain. PCC is essential for the catabolism of branched-chain amino acids (isoleucine, valine), threonine, methionine, odd-chain fatty acids, and cholesterol side chains, as well as for clearance of gut-derived propionate. Loss-of-function mutations in *PCCA* cause propionic acidemia, a severe inborn error of metabolism with multisystem complications including neurological damage, cardiomyopathy, and recurrent metabolic crises. Recent high-resolution cryo-EM structures (2024) have provided unprecedented structural insights, and the landmark mRNA-3927 clinical trial has demonstrated the feasibility of dual mRNA replacement therapy for this devastating disorder.

References

1. (kelson1996chaperoninmediatedassemblyof pages 1-2): T. L. Kelson, T. Ohura, and J. Kraus. Chaperonin-mediated assembly of wild-type and mutant subunits of human propionyl-coa carboxylase expressed in escherichia coli. Human molecular genetics, 5 3:331-7, Mar 1996. URL: https://doi.org/10.1093/hmg/5.3.331, doi:10.1093/hmg/5.3.331. This article has 37 citations and is from a domain leading peer-reviewed journal.

2. (kelson1996chaperoninmediatedassemblyof pages 2-3): T. L. Kelson, T. Ohura, and J. Kraus. Chaperonin-mediated assembly of wild-type and mutant subunits of human propionyl-coa carboxylase expressed in escherichia coli. Human molecular genetics, 5 3:331-7, Mar 1996. URL: https://doi.org/10.1093/hmg/5.3.331, doi:10.1093/hmg/5.3.331. This article has 37 citations and is from a domain leading peer-reviewed journal.

3. (erdal2025aminoacidmetabolism pages 9-10): Ranya Erdal, Kıvanç Birsoy, and Gokhan Unlu. Amino acid metabolism in liver mitochondria: from homeostasis to disease. Metabolites, 15:446, Jul 2025. URL: https://doi.org/10.3390/metabo15070446, doi:10.3390/metabo15070446. This article has 7 citations.

4. (jitrapakdee2003thebiotinenzyme pages 4-6): Sarawut Jitrapakdee and John Wallace. The biotin enzyme family: conserved structural motifs and domain rearrangements. Jun 2003. URL: https://doi.org/10.2174/1389203033487199, doi:10.2174/1389203033487199. This article has 142 citations and is from a peer-reviewed journal.

5. (zhou2024structuralinsightsinto pages 4-6): Fayang Zhou, Yuanyuan Zhang, Yuyao Zhu, Qiang Zhou, Yigong Shi, and Qiuyu Hu. Structural insights into human propionyl-coa carboxylase (pcc) and 3-methylcrotonyl-coa carboxylase (mcc). bioRxiv, Aug 2024. URL: https://doi.org/10.1101/2024.04.30.591959, doi:10.1101/2024.04.30.591959. This article has 10 citations.

6. (zhou2024structuralinsightsinto pages 1-4): Fayang Zhou, Yuanyuan Zhang, Yuyao Zhu, Qiang Zhou, Yigong Shi, and Qiuyu Hu. Structural insights into human propionyl-coa carboxylase (pcc) and 3-methylcrotonyl-coa carboxylase (mcc). bioRxiv, Aug 2024. URL: https://doi.org/10.1101/2024.04.30.591959, doi:10.1101/2024.04.30.591959. This article has 10 citations.

7. (erdal2025aminoacidmetabolism pages 6-9): Ranya Erdal, Kıvanç Birsoy, and Gokhan Unlu. Amino acid metabolism in liver mitochondria: from homeostasis to disease. Metabolites, 15:446, Jul 2025. URL: https://doi.org/10.3390/metabo15070446, doi:10.3390/metabo15070446. This article has 7 citations.

8. (maines2023understandingthepathogenesis pages 1-2): Evelina Maines, Michele Moretti, Nicola Vitturi, Giorgia Gugelmo, Ilaria Fasan, Livia Lenzini, Giovanni Piccoli, Vincenza Gragnaniello, Arianna Maiorana, Massimo Soffiati, Alberto Burlina, and Roberto Franceschi. Understanding the pathogenesis of cardiac complications in patients with propionic acidemia and exploring therapeutic alternatives for those who are not eligible or are waiting for liver transplantation. Metabolites, 13(4):563, Apr 2023. URL: https://doi.org/10.3390/metabo13040563, doi:10.3390/metabo13040563. This article has 7 citations.

9. (riverabarahona2018identificationof34 pages 1-5): Ana Rivera-Barahona, Rosa Navarrete, Raquel García-Rodríguez, Eva Richard, Magdalena Ugarte, Celia Pérez-Cerda, Belén Pérez, Alejandra Gámez, and Lourdes R. Desviat. Identification of 34 novel mutations in propionic acidemia: functional characterization of missense variants and phenotype associations. Molecular genetics and metabolism, 125 3:266-275, Nov 2018. URL: https://doi.org/10.1016/j.ymgme.2018.09.008, doi:10.1016/j.ymgme.2018.09.008. This article has 29 citations and is from a peer-reviewed journal.

10. (zhou2024structuralinsightsinto pages 6-7): Fayang Zhou, Yuanyuan Zhang, Yuyao Zhu, Qiang Zhou, Yigong Shi, and Qiuyu Hu. Structural insights into human propionyl-coa carboxylase (pcc) and 3-methylcrotonyl-coa carboxylase (mcc). bioRxiv, Aug 2024. URL: https://doi.org/10.1101/2024.04.30.591959, doi:10.1101/2024.04.30.591959. This article has 10 citations.

11. (jitrapakdee2003thebiotinenzyme pages 10-11): Sarawut Jitrapakdee and John Wallace. The biotin enzyme family: conserved structural motifs and domain rearrangements. Jun 2003. URL: https://doi.org/10.2174/1389203033487199, doi:10.2174/1389203033487199. This article has 142 citations and is from a peer-reviewed journal.

12. (zhou2024structuralinsightsinto pages 11-14): Fayang Zhou, Yuanyuan Zhang, Yuyao Zhu, Qiang Zhou, Yigong Shi, and Qiuyu Hu. Structural insights into human propionyl-coa carboxylase (pcc) and 3-methylcrotonyl-coa carboxylase (mcc). bioRxiv, Aug 2024. URL: https://doi.org/10.1101/2024.04.30.591959, doi:10.1101/2024.04.30.591959. This article has 10 citations.

13. (zhou2024structuralinsightsinto pages 9-11): Fayang Zhou, Yuanyuan Zhang, Yuyao Zhu, Qiang Zhou, Yigong Shi, and Qiuyu Hu. Structural insights into human propionyl-coa carboxylase (pcc) and 3-methylcrotonyl-coa carboxylase (mcc). bioRxiv, Aug 2024. URL: https://doi.org/10.1101/2024.04.30.591959, doi:10.1101/2024.04.30.591959. This article has 10 citations.

14. (lu2026lossofpropionylcoa pages 1-5): Fang Lu, Chorlada Paiboonrungruang, Wentao He, Zhaohui Xiong, Pingchuan Tang, Takhar Kasumov, Xiaoxin Chen, and Guo-Fang Zhang. Loss of propionyl-coa carboxylase reprograms hepatic metabolism by suppressing mitochondrial pyruvate carboxylation and fatty acid oxidation. bioRxiv, Apr 2026. URL: https://doi.org/10.64898/2026.04.13.718201, doi:10.64898/2026.04.13.718201. This article has 0 citations.

15. (chen2025elevatedpropionateand pages 2-3): Xiaoxin Chen, Qing Cheng, and Guo-Fang Zhang. Elevated propionate and its association with neurological dysfunctions in propionic acidemia. Frontiers in Molecular Neuroscience, Mar 2025. URL: https://doi.org/10.3389/fnmol.2025.1499376, doi:10.3389/fnmol.2025.1499376. This article has 11 citations.

16. (lu2026lossofpropionylcoa pages 5-8): Fang Lu, Chorlada Paiboonrungruang, Wentao He, Zhaohui Xiong, Pingchuan Tang, Takhar Kasumov, Xiaoxin Chen, and Guo-Fang Zhang. Loss of propionyl-coa carboxylase reprograms hepatic metabolism by suppressing mitochondrial pyruvate carboxylation and fatty acid oxidation. bioRxiv, Apr 2026. URL: https://doi.org/10.64898/2026.04.13.718201, doi:10.64898/2026.04.13.718201. This article has 0 citations.

17. (lu2026lossofpropionylcoa pages 8-11): Fang Lu, Chorlada Paiboonrungruang, Wentao He, Zhaohui Xiong, Pingchuan Tang, Takhar Kasumov, Xiaoxin Chen, and Guo-Fang Zhang. Loss of propionyl-coa carboxylase reprograms hepatic metabolism by suppressing mitochondrial pyruvate carboxylation and fatty acid oxidation. bioRxiv, Apr 2026. URL: https://doi.org/10.64898/2026.04.13.718201, doi:10.64898/2026.04.13.718201. This article has 0 citations.

18. (chen2025elevatedpropionateand pages 3-4): Xiaoxin Chen, Qing Cheng, and Guo-Fang Zhang. Elevated propionate and its association with neurological dysfunctions in propionic acidemia. Frontiers in Molecular Neuroscience, Mar 2025. URL: https://doi.org/10.3389/fnmol.2025.1499376, doi:10.3389/fnmol.2025.1499376. This article has 11 citations.

19. (maines2023understandingthepathogenesis pages 4-5): Evelina Maines, Michele Moretti, Nicola Vitturi, Giorgia Gugelmo, Ilaria Fasan, Livia Lenzini, Giovanni Piccoli, Vincenza Gragnaniello, Arianna Maiorana, Massimo Soffiati, Alberto Burlina, and Roberto Franceschi. Understanding the pathogenesis of cardiac complications in patients with propionic acidemia and exploring therapeutic alternatives for those who are not eligible or are waiting for liver transplantation. Metabolites, 13(4):563, Apr 2023. URL: https://doi.org/10.3390/metabo13040563, doi:10.3390/metabo13040563. This article has 7 citations.

20. (chen2025elevatedpropionateand pages 7-7): Xiaoxin Chen, Qing Cheng, and Guo-Fang Zhang. Elevated propionate and its association with neurological dysfunctions in propionic acidemia. Frontiers in Molecular Neuroscience, Mar 2025. URL: https://doi.org/10.3389/fnmol.2025.1499376, doi:10.3389/fnmol.2025.1499376. This article has 11 citations.

21. (maines2023understandingthepathogenesis pages 11-13): Evelina Maines, Michele Moretti, Nicola Vitturi, Giorgia Gugelmo, Ilaria Fasan, Livia Lenzini, Giovanni Piccoli, Vincenza Gragnaniello, Arianna Maiorana, Massimo Soffiati, Alberto Burlina, and Roberto Franceschi. Understanding the pathogenesis of cardiac complications in patients with propionic acidemia and exploring therapeutic alternatives for those who are not eligible or are waiting for liver transplantation. Metabolites, 13(4):563, Apr 2023. URL: https://doi.org/10.3390/metabo13040563, doi:10.3390/metabo13040563. This article has 7 citations.

22. (maines2023understandingthepathogenesis pages 13-14): Evelina Maines, Michele Moretti, Nicola Vitturi, Giorgia Gugelmo, Ilaria Fasan, Livia Lenzini, Giovanni Piccoli, Vincenza Gragnaniello, Arianna Maiorana, Massimo Soffiati, Alberto Burlina, and Roberto Franceschi. Understanding the pathogenesis of cardiac complications in patients with propionic acidemia and exploring therapeutic alternatives for those who are not eligible or are waiting for liver transplantation. Metabolites, 13(4):563, Apr 2023. URL: https://doi.org/10.3390/metabo13040563, doi:10.3390/metabo13040563. This article has 7 citations.

23. (koeberl2024interimanalysesof pages 1-2): Dwight Koeberl, Andreas Schulze, Neal Sondheimer, Gerald S. Lipshutz, Tarekegn Geberhiwot, Lerong Li, Rajnish Saini, Junxiang Luo, Vanja Sikirica, Ling Jin, Min Liang, Mary Leuchars, and Stephanie Grunewald. Interim analyses of a first-in-human phase 1/2 mrna trial for propionic acidaemia. Nature, 628:872-877, Apr 2024. URL: https://doi.org/10.1038/s41586-024-07266-7, doi:10.1038/s41586-024-07266-7. This article has 136 citations and is from a highest quality peer-reviewed journal.

24. (koeberl2024interimanalysesof pages 2-3): Dwight Koeberl, Andreas Schulze, Neal Sondheimer, Gerald S. Lipshutz, Tarekegn Geberhiwot, Lerong Li, Rajnish Saini, Junxiang Luo, Vanja Sikirica, Ling Jin, Min Liang, Mary Leuchars, and Stephanie Grunewald. Interim analyses of a first-in-human phase 1/2 mrna trial for propionic acidaemia. Nature, 628:872-877, Apr 2024. URL: https://doi.org/10.1038/s41586-024-07266-7, doi:10.1038/s41586-024-07266-7. This article has 136 citations and is from a highest quality peer-reviewed journal.

25. (koeberl2024interimanalysesof pages 5-6): Dwight Koeberl, Andreas Schulze, Neal Sondheimer, Gerald S. Lipshutz, Tarekegn Geberhiwot, Lerong Li, Rajnish Saini, Junxiang Luo, Vanja Sikirica, Ling Jin, Min Liang, Mary Leuchars, and Stephanie Grunewald. Interim analyses of a first-in-human phase 1/2 mrna trial for propionic acidaemia. Nature, 628:872-877, Apr 2024. URL: https://doi.org/10.1038/s41586-024-07266-7, doi:10.1038/s41586-024-07266-7. This article has 136 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PCCA-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PCCA-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. kelson1996chaperoninmediatedassemblyof pages 1-2
2. zhou2024structuralinsightsinto pages 4-6
3. zhou2024structuralinsightsinto pages 6-7
4. jitrapakdee2003thebiotinenzyme pages 10-11
5. kelson1996chaperoninmediatedassemblyof pages 2-3
6. erdal2025aminoacidmetabolism pages 9-10
7. lu2026lossofpropionylcoa pages 1-5
8. chen2025elevatedpropionateand pages 2-3
9. chen2025elevatedpropionateand pages 3-4
10. maines2023understandingthepathogenesis pages 1-2
11. chen2025elevatedpropionateand pages 7-7
12. maines2023understandingthepathogenesis pages 11-13
13. koeberl2024interimanalysesof pages 1-2
14. koeberl2024interimanalysesof pages 2-3
15. koeberl2024interimanalysesof pages 5-6
16. jitrapakdee2003thebiotinenzyme pages 4-6
17. zhou2024structuralinsightsinto pages 1-4
18. erdal2025aminoacidmetabolism pages 6-9
19. zhou2024structuralinsightsinto pages 11-14
20. zhou2024structuralinsightsinto pages 9-11
21. lu2026lossofpropionylcoa pages 5-8
22. lu2026lossofpropionylcoa pages 8-11
23. maines2023understandingthepathogenesis pages 4-5
24. maines2023understandingthepathogenesis pages 13-14
25. https://doi.org/10.1093/hmg/5.3.331,
26. https://doi.org/10.3390/metabo15070446,
27. https://doi.org/10.2174/1389203033487199,
28. https://doi.org/10.1101/2024.04.30.591959,
29. https://doi.org/10.3390/metabo13040563,
30. https://doi.org/10.1016/j.ymgme.2018.09.008,
31. https://doi.org/10.64898/2026.04.13.718201,
32. https://doi.org/10.3389/fnmol.2025.1499376,
33. https://doi.org/10.1038/s41586-024-07266-7,