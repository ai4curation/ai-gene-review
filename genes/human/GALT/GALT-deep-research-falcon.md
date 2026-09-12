---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-05T18:48:43.425068'
end_time: '2026-07-05T19:02:52.706140'
duration_seconds: 849.28
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: GALT
  gene_symbol: GALT
  uniprot_accession: P07902
  protein_description: 'RecName: Full=Galactose-1-phosphate uridylyltransferase; Short=Gal-1-P
    uridylyltransferase; EC=2.7.7.12 {ECO:0000269|PubMed:22461411, ECO:0000269|PubMed:27005423};
    AltName: Full=UDP-glucose--hexose-1-phosphate uridylyltransferase;'
  gene_info: Name=GALT;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the galactose-1-phosphate uridylyltransferase
  protein_domains: GalP_UDPtransf1. (IPR001937); GalP_UDPtransf1_His-AS. (IPR019779);
    GalP_Utransf_C. (IPR005850); GalP_Utransf_N. (IPR005849); HIT-like_sf. (IPR036265)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 36
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: GALT-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: GALT-deep-research-falcon_artifacts/artifact-01.md
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
- **UniProt Accession:** P07902
- **Protein Description:** RecName: Full=Galactose-1-phosphate uridylyltransferase; Short=Gal-1-P uridylyltransferase; EC=2.7.7.12 {ECO:0000269|PubMed:22461411, ECO:0000269|PubMed:27005423}; AltName: Full=UDP-glucose--hexose-1-phosphate uridylyltransferase;
- **Gene Information:** Name=GALT;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the galactose-1-phosphate uridylyltransferase
- **Key Domains:** GalP_UDPtransf1. (IPR001937); GalP_UDPtransf1_His-AS. (IPR019779); GalP_Utransf_C. (IPR005850); GalP_Utransf_N. (IPR005849); HIT-like_sf. (IPR036265)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "GALT" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'GALT' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **GALT** (gene ID: GALT, UniProt: P07902) in human.

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
- **UniProt Accession:** P07902
- **Protein Description:** RecName: Full=Galactose-1-phosphate uridylyltransferase; Short=Gal-1-P uridylyltransferase; EC=2.7.7.12 {ECO:0000269|PubMed:22461411, ECO:0000269|PubMed:27005423}; AltName: Full=UDP-glucose--hexose-1-phosphate uridylyltransferase;
- **Gene Information:** Name=GALT;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the galactose-1-phosphate uridylyltransferase
- **Key Domains:** GalP_UDPtransf1. (IPR001937); GalP_UDPtransf1_His-AS. (IPR019779); GalP_Utransf_C. (IPR005850); GalP_Utransf_N. (IPR005849); HIT-like_sf. (IPR036265)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "GALT" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'GALT' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **GALT** (gene ID: GALT, UniProt: P07902) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: Human GALT (Galactose-1-Phosphate Uridylyltransferase)

**Gene:** GALT | **UniProt:** P07902 | **EC:** 2.7.7.12 | **Organism:** Homo sapiens

## 1. Gene and Protein Overview

The human *GALT* gene encodes galactose-1-phosphate uridylyltransferase (also known as UDP-glucose–hexose-1-phosphate uridylyltransferase), a central enzyme in galactose metabolism. The gene is located on chromosome 9p13.3, spans approximately 4.3 kb of genomic DNA, and is organized into 11 exons encoding a cDNA of 1,295 bases that translates to a polypeptide of 379 amino acids (tyfield1999classicalgalactosemiaand pages 1-2, succoio2022galactosemiabiochemistrymolecular pages 2-4). The active enzyme functions as a homodimer with an estimated molecular mass of approximately 88 kDa (tyfield1999classicalgalactosemiaand pages 1-2, tyfield1999classicalgalactosemiaand pages 2-6).

The following table summarizes the key molecular, structural, and functional properties of human GALT:

| Property | Human GALT summary |
|---|---|
| Gene symbol | **GALT** (galactose-1-phosphate uridylyltransferase), matching UniProt P07902 protein description (succoio2022galactosemiabiochemistrymolecular pages 1-2, tyfield1999classicalgalactosemiaand pages 1-2) |
| UniProt ID | **P07902** (user-specified target; protein identity consistent with cited GALT literature) |
| EC number | **EC 2.7.7.12** galactose-1-phosphate uridylyltransferase (succoio2022galactosemiabiochemistrymolecular pages 1-2, delnoy2021currentandfuture pages 1-6) |
| Chromosomal location | **9p13.3** / 9p13 region in human genome (tyfield1999classicalgalactosemiaand pages 1-2, succoio2022galactosemiabiochemistrymolecular pages 2-4) |
| Gene size and exons | ~**4.3 kb**, **11 exons** (tyfield1999classicalgalactosemiaand pages 1-2, succoio2022galactosemiabiochemistrymolecular pages 2-4) |
| Protein length | **379 amino acids** per monomer (succoio2022galactosemiabiochemistrymolecular pages 1-2, tyfield1999classicalgalactosemiaand pages 1-2) |
| Active form | **Homodimer** with **two active sites** contributed by both subunits (succoio2022galactosemiabiochemistrymolecular pages 1-2, forte2023classicgalactosemiaclinical pages 5-7, tyfield1999classicalgalactosemiaand pages 1-2) |
| Molecular mass | Active dimer ~**88 kDa**; GALT monomer detected at ~**43 kDa** in cell studies (tyfield1999classicalgalactosemiaand pages 1-2, wiertelak2025cytosolicudpgalbiosynthetic pages 3-4) |
| Protein family / superfamily | Member of the **galactose-1-phosphate uridylyltransferase family** and **HIT (histidine triad) superfamily** (brenner2002hintfhitand pages 10-11, brenner2002hintfhitand pages 8-9) |
| Key active-site residues | Conserved **His-Pro-His / histidine-triad** catalytic motif; catalytic nucleophile **His166** forms covalent UMP intermediate; active-site contribution from **H186** residues of both subunits; zinc-binding residues **E202, H301, H319, H321** stabilize structure/activity (succoio2022galactosemiabiochemistrymolecular pages 1-2, brenner2002hintfhitand pages 8-9, forte2023classicgalactosemiaclinical pages 5-7) |
| Catalytic mechanism | **Ping-pong double-displacement** mechanism with a covalent uridylylated enzyme intermediate and overall retention of configuration via two inversions (succoio2022galactosemiabiochemistrymolecular pages 1-2, brenner2002hintfhitand pages 8-9) |
| Substrates | **Galactose-1-phosphate (Gal-1-P)** and **UDP-glucose (UDP-Glc)** (succoio2022galactosemiabiochemistrymolecular pages 1-2, durrant2020defectsingalactose pages 1-3) |
| Products | **Glucose-1-phosphate (Glc-1-P)** and **UDP-galactose (UDP-Gal)** (succoio2022galactosemiabiochemistrymolecular pages 1-2, durrant2020defectsingalactose pages 1-3) |
| Subcellular localization | **Cytosol / cytosolic UDP-Gal biosynthetic machinery** (directly supported by recent cell studies) (wiertelak2025cytosolicudpgalbiosynthetic pages 6-8, wiertelak2025cytosolicudpgalbiosynthetic pages 3-4) |
| Pathway | Central enzyme of the **Leloir pathway**: GALM → GALK1 → **GALT** → GALE, linking galactose catabolism to UDP-sugar metabolism (succoio2022galactosemiabiochemistrymolecular pages 1-2, delnoy2021currentandfuture pages 1-6, delnoy2021currentandfuture pages 6-9) |
| Disease association | Deficiency causes **classic galactosemia (Type I)**, the most severe common galactosemia; acute neonatal disease and long-term neurologic/reproductive complications are characteristic (succoio2022galactosemiabiochemistrymolecular pages 2-4, forte2023classicgalactosemiaclinical pages 1-2, tisa2022theimportanceof pages 5-6) |


*Table: This table summarizes the core molecular, biochemical, structural, and disease-related properties of human GALT relevant for functional annotation. It provides a compact reference linking canonical gene/protein features to pathway role and clinical significance.*

## 2. Enzymatic Function and Catalytic Mechanism

### 2.1. Reaction Catalyzed

GALT catalyzes the reversible transfer of a uridylyl (UMP) group from UDP-glucose (UDP-Glc) to galactose-1-phosphate (Gal-1-P), yielding glucose-1-phosphate (Glc-1-P) and UDP-galactose (UDP-Gal) (succoio2022galactosemiabiochemistrymolecular pages 1-2, durrant2020defectsingalactose pages 1-3). This reaction is essential for channeling dietary galactose into central glucose metabolism and for generating UDP-galactose, a nucleotide sugar donor required for glycoprotein and glycolipid biosynthesis (delnoy2021currentandfuture pages 9-13).

The overall reaction is:

**Gal-1-P + UDP-Glc ⇌ Glc-1-P + UDP-Gal**

### 2.2. Ping-Pong Double-Displacement Mechanism

GALT operates via a ping-pong (double-displacement) catalytic mechanism involving formation of a covalent uridylylated enzyme intermediate (succoio2022galactosemiabiochemistrymolecular pages 1-2, brenner2002hintfhitand pages 8-9). In the first half-reaction, the active-site nucleophile His166 attacks UDP-glucose, releasing glucose-1-phosphate and forming a covalent UMP-His166 intermediate. In the second half-reaction, galactose-1-phosphate attacks the enzyme-bound UMP to produce UDP-galactose and regenerate the free enzyme (brenner2002hintfhitand pages 8-9). Each half-reaction proceeds with inversion of configuration at the α-phosphorus center, such that the overall reaction results in retention of configuration, which is a hallmark of ping-pong double-displacement transferases (brenner2002hintfhitand pages 8-9).

### 2.3. Active Site and Structural Features

GALT belongs to Branch III of the histidine triad (HIT) superfamily of nucleotide-binding proteins. The HIT superfamily is characterized by the HxHxQ motif (where x denotes hydrophobic residues), which in GALT differs from the HxHxH motif found in hydrolase branches of the superfamily (brenner2002hintfhitand pages 10-11). The conserved glutamine residue at position 188 in human GALT (Q188) plays a critical functional role; its mutation to arginine (Q188R) reduces catalytic rates by approximately one million-fold (brenner2002hintfhitand pages 10-11).

The enzyme's two active sites are located at the interface between the two subunits of the homodimer, with contributions from residues of both monomers. The catalytic center includes His186 residues from both subunits, forming the His-Pro-His functional motif (succoio2022galactosemiabiochemistrymolecular pages 1-2, forte2023classicgalactosemiaclinical pages 5-7). Each monomer also contains a structural zinc-binding site coordinated by residues E202, H301, H319, and H321, which stabilizes the overall protein structure and supports dimerization and catalytic activity (forte2023classicgalactosemiaclinical pages 5-7). The glucose-1-phosphate binding site involves residues N97, K334, F335, V337, Y339, E340, and Q346 from one chain and N173 and Q188 from the adjacent chain, with N97 also participating in UMP binding (forte2023classicgalactosemiaclinical pages 5-7).

## 3. Subcellular Localization

GALT functions as a component of the cytosolic UDP-galactose biosynthetic machinery. In human cells, UDP-Gal is synthesized in the cytosol via the Leloir pathway, of which GALT is a key enzyme (wiertelak2025cytosolicudpgalbiosynthetic pages 6-8, wiertelak2025cytosolicudpgalbiosynthetic pages 3-4). Recent CRISPR/Cas9-based studies in HEK293T cells confirmed that GALT (detected at ~43 kDa by western blot) operates within the cytosol, where it converts Gal-1-P into UDP-Gal using UDP-Glc as the uridylyl donor (wiertelak2025cytosolicudpgalbiosynthetic pages 3-4). The resulting UDP-Gal is then transported into the Golgi apparatus by the nucleotide sugar transporter SLC35A2 for use as a donor substrate by Golgi-resident glycosyltransferases (wiertelak2025cytosolicudpgalbiosynthetic pages 6-8).

## 4. The Leloir Pathway: Biochemical Pathway Context

GALT occupies a central position in the Leloir pathway, the primary metabolic route for the conversion of galactose to glucose-1-phosphate. This pathway, discovered by Argentine biochemist Luis Leloir (Nobel Prize, 1970), consists of four sequential enzymatic steps (succoio2022galactosemiabiochemistrymolecular pages 1-2, delnoy2021currentandfuture pages 6-9):

1. **GALM (galactose mutarotase):** Converts β-D-galactose to α-D-galactose, ensuring appropriate anomeric substrate availability.
2. **GALK1 (galactokinase):** Phosphorylates α-D-galactose to galactose-1-phosphate using ATP.
3. **GALT (galactose-1-phosphate uridylyltransferase):** Transfers the uridylyl group from UDP-glucose to galactose-1-phosphate, generating glucose-1-phosphate and UDP-galactose.
4. **GALE (UDP-galactose 4'-epimerase):** Reversibly interconverts UDP-galactose and UDP-glucose using NAD⁺ as a cofactor, thereby recycling the UDP-glucose consumed by GALT (succoio2022galactosemiabiochemistrymolecular pages 1-2, delnoy2021currentandfuture pages 6-9, delnoy2021currentandfuture pages 9-13).

The glucose-1-phosphate produced by GALT can enter glycolysis (via conversion to glucose-6-phosphate) for energy production, while the UDP-galactose product serves as a critical sugar donor for glycosylation reactions in the Golgi (succoio2022galactosemiabiochemistrymolecular pages 1-2, delnoy2021currentandfuture pages 9-13).

### 4.1. Role in UDP-Sugar Pools and Glycosylation

GALT contributes to intracellular UDP-galactose levels, although recent studies demonstrate that GALE is the dominant enzyme maintaining UDP-Gal pools under standard conditions. CRISPR-mediated knockout of GALT in HEK293T cells did not substantially reduce intracellular UDP-Gal concentrations or significantly alter N-glycan profiles, indicating that GALT's primary metabolic role is the disposal of exogenous galactose rather than de novo UDP-Gal biosynthesis (wiertelak2025cytosolicudpgalbiosynthetic pages 6-8, wiertelak2025cytosolicudpgalbiosynthetic pages 4-6). In contrast, GALE knockout caused near-complete suppression of UDP-Gal synthesis and dramatic galactosylation defects (wiertelak2025cytosolicudpgalbiosynthetic pages 4-6). Nevertheless, in the context of GALT deficiency, accumulation of galactose-1-phosphate and perturbation of the UDP-glucose/UDP-galactose ratio have pathological consequences for glycosylation, particularly affecting myelin (rich in galactocerebrosides) and other galactose-containing glycoconjugates (panis2024brainfunctionin pages 4-5).

When GALT is non-functional, Gal-1-P accumulates dramatically—for example, a galT-null *S. cerevisiae* mutant showed a 1,000-fold increase in Gal-1-P—and the associated perturbation in UDP-sugar metabolism impairs glycoprotein and glycolipid biosynthesis (boulanger2021sugarphosphatetoxicities pages 12-14).

## 5. Disease Association: Classic Galactosemia (Type I)

### 5.1. Clinical Manifestations

Deficiency of GALT causes classic galactosemia (Type I; OMIM #230400), the most common and most severe form of galactosemia, with an estimated incidence of approximately 1:30,000 live births (delnoy2021currentandfuture pages 1-6). Acute neonatal manifestations include jaundice, hepatomegaly, poor feeding, failure to thrive, hypoglycemia, *Escherichia coli* sepsis, and cataracts (forte2023classicgalactosemiaclinical pages 1-2). Despite early institution of galactose-restricted diet, approximately 85% of patients develop long-term complications including cognitive impairment, ataxia, speech difficulties, decreased bone mineral density, and premature ovarian insufficiency affecting 80–90% of affected women (forte2023classicgalactosemiaclinical pages 1-2, tisa2022theimportanceof pages 5-6).

### 5.2. Pathogenic Mechanisms

The pathophysiology involves accumulation of toxic metabolites, particularly galactose-1-phosphate and galactitol. Galactitol is formed through the alternative polyol pathway via aldose reductase and induces hyperosmotic and oxidative stress, which is responsible for cataract formation in GALT-deficient patients (succoio2022galactosemiabiochemistrymolecular pages 2-4). Additionally, GALT deficiency disturbs the UDP-galactose/UDP-glucose ratio, leading to aberrant glycosylation of proteins and lipids. Gal-1-P may also competitively interfere with other nucleotide sugar reactions, while disrupted pyrimidine biosynthesis gene expression due to altered UTP and CTP levels has been reported (boulanger2021sugarphosphatetoxicities pages 12-14, panis2024brainfunctionin pages 4-5).

### 5.3. Genotype-Phenotype Correlations

Approximately 300 unique mutations at the GALT gene have been identified, contributing to phenotypic variability through allelic heterogeneity (tyfield1999classicalgalactosemiaand pages 8-10). The key pathogenic variants and their characteristics are summarized below:

| Variant name/designation | Nucleotide change | Amino acid change | Frequency / population | Effect on enzyme activity | Clinical phenotype / severity |
|---|---|---|---|---|---|
| Q188R | c.563A>G | p.Gln188Arg (Q188R) | Most common pathogenic GALT variant in Caucasian/European populations; ~60–70% of mutant alleles/cases in cited reports (succoio2022galactosemiabiochemistrymolecular pages 2-4, tyfield1999classicalgalactosemiaand pages 1-2, tyfield1999classicalgalactosemiaand pages 8-10) | Near-complete to undetectable GALT activity when homozygous; severe catalytic defect, with major loss of function (succoio2022galactosemiabiochemistrymolecular pages 2-4, tyfield1999classicalgalactosemiaand pages 1-2, tyfield1999classicalgalactosemiaand pages 8-10) | Classic galactosemia; usually severe neonatal disease and poor prognosis when untreated (tyfield1999classicalgalactosemiaand pages 1-2, forte2023classicgalactosemiaclinical pages 1-2) |
| K285N | c.855G>T | p.Lys285Asn (K285N) | Second most common pathogenic variant in Europeans; ~26–34% of galactosemia alleles in cited review (forte2023classicgalactosemiaclinical pages 5-7) | Causes major loss of function; ~50% activity loss in heterozygotes and complete loss in homozygotes (forte2023classicgalactosemiaclinical pages 5-7) | Severe/classic galactosemia phenotype; consistently associated with severe disease (tyfield1999classicalgalactosemiaand pages 1-2, forte2023classicgalactosemiaclinical pages 1-2, forte2023classicgalactosemiaclinical pages 5-7) |
| Duarte D2 | often defined by c.940A>G in cis with promoter deletion c.-119_-116delGTCA and additional linked changes | p.Asn314Asp (N314D) | Common biochemical variant; Duarte allele prevalence ~5–6% in North American non-galactosemic populations and ~2% in Japan; enzyme activity often ~50% in RBCs (tisa2022theimportanceof pages 5-6, wang2024acasereport pages 5-8, tyfield1999classicalgalactosemiaand pages 8-10) | Reduced but residual activity; decreased RBC GALT activity attributed to reduced abundance/instability rather than N314D alone (tisa2022theimportanceof pages 5-6, tyfield1999classicalgalactosemiaand pages 8-10) | Generally clinically benign/asymptomatic as a standalone Duarte variant; Duarte galactosemia occurs when paired with a classic pathogenic allele (succoio2022galactosemiabiochemistrymolecular pages 2-4, tisa2022theimportanceof pages 5-6, wang2024acasereport pages 5-8) |
| D1 / Los Angeles | c.940A>G in cis with c.652C>T (linked synonymous change in cited review) | p.Asn314Asp (N314D) | Described biochemical variant found globally; less emphasized than D2 but recognized in classic mutation reviews (tyfield1999classicalgalactosemiaand pages 1-2, forte2023classicgalactosemiaclinical pages 5-7) | Associated with normal or increased erythrocyte GALT activity, likely via increased protein abundance/overexpression rather than intrinsic catalytic enhancement (tyfield1999classicalgalactosemiaand pages 1-2, forte2023classicgalactosemiaclinical pages 1-2, forte2023classicgalactosemiaclinical pages 5-7) | Not pathogenic by itself; considered a benign/high-activity biochemical variant (tyfield1999classicalgalactosemiaand pages 1-2, forte2023classicgalactosemiaclinical pages 1-2) |
| S135L | not specified in gathered evidence | p.Ser135Leu (S135L) | Reported variant in classic mutation review; population frequency not specified in gathered evidence (tyfield1999classicalgalactosemiaand pages 1-2) | Tissue-specific residual activity reported; individuals carrying S135L appear to retain GALT activity in some tissues (tyfield1999classicalgalactosemiaand pages 1-2) | Often associated with galactosemia but may show atypical or somewhat milder biochemical behavior because of tissue-specific residual activity (tyfield1999classicalgalactosemiaand pages 1-2) |


*Table: This table summarizes major disease-causing and biochemical GALT variants relevant to classic galactosemia, including their frequencies, effects on enzyme activity, and associated clinical severity. It is useful for linking genotype to functional impact during annotation and interpretation.*

The most prevalent pathogenic variant, Q188R (c.563A>G), accounts for approximately 60–70% of mutant chromosomes in European populations and results in near-complete loss of enzyme activity when homozygous. This variant occurs in a highly conserved domain near the catalytic site and may function as a partial dominant negative when combined with other GALT alleles (succoio2022galactosemiabiochemistrymolecular pages 2-4, tyfield1999classicalgalactosemiaand pages 1-2, tyfield1999classicalgalactosemiaand pages 8-10). K285N (c.855G>T) is the second most common pathogenic variant in Europeans (26–34% of alleles), causing approximately 50% activity loss in heterozygotes and complete loss in homozygotes (forte2023classicgalactosemiaclinical pages 5-7). Importantly, most pathogenic GALT variants are missense mutations that cause protein instability and folding defects rather than direct disruption of catalytic residues (forte2023classicgalactosemiaclinical pages 5-7).

The Duarte variant (D2) is defined by the N314D substitution in cis with a promoter deletion (c.-119_-116delGTCA) and results in reduced GALT activity to approximately 50% of normal in erythrocytes, though it is clinically benign as an isolated variant (tisa2022theimportanceof pages 5-6, wang2024acasereport pages 5-8, tyfield1999classicalgalactosemiaand pages 8-10). The reduced activity is attributed to decreased protein abundance and thermal instability rather than impaired catalytic function per se (tyfield1999classicalgalactosemiaand pages 8-10). The D1/Los Angeles variant carries the same N314D substitution but in a different haplotype context, resulting in normal or increased enzyme activity (tyfield1999classicalgalactosemiaand pages 1-2, forte2023classicgalactosemiaclinical pages 1-2).

## 6. Emerging Therapeutic Approaches

While galactose-restricted diet remains the standard of care, it is inadequate for preventing long-term complications. Several novel therapeutic strategies are under preclinical and early clinical investigation (succoio2022galactosemiabiochemistrymolecular pages 12-13, succoio2022galactosemiabiochemistrymolecular pages 8-9):

- **Gene therapy:** AAV9-mediated GALT gene replacement has shown efficacy in neonatal rat models, increasing GALT levels in liver (64–595% of normal) and brain (3–42%), with reduced toxic metabolite accumulation and improved cataracts (succoio2022galactosemiabiochemistrymolecular pages 8-9, tisa2022theimportanceof pages 11-12).
- **mRNA therapy:** Lipid nanoparticle-delivered GALT mRNA has demonstrated dose-dependent increases in GALT expression and activity, decreasing Gal-1-P levels in liver, blood cells, and tissues in mouse and zebrafish models, and improving motor-related phenotypes (succoio2022galactosemiabiochemistrymolecular pages 8-9, bellagamba2025experimentalgalactose1phosphateuridylyltransferase pages 16-17). It has been estimated that restoring GALT activity to 10–15% of normal may be sufficient to prevent clinical disease (succoio2022galactosemiabiochemistrymolecular pages 8-9).
- **Pharmacological chaperones:** Small molecules that stabilize and facilitate proper folding of mutant GALT protein offer the advantage of oral bioavailability and potential blood-brain barrier penetration, though they are effective only for missense variants and cannot address deletions, splice-site, or active-site mutations (succoio2022galactosemiabiochemistrymolecular pages 8-9).
- **Galactokinase inhibitors (e.g., AT-007):** These aim to reduce galactose-1-phosphate accumulation by inhibiting the upstream phosphorylation step, and are in Phase 1/2 and 2/3 clinical trials (succoio2022galactosemiabiochemistrymolecular pages 6-8).

## 7. Summary

Human GALT (UniProt P07902) is a cytosolic homodimeric metalloenzyme of the HIT superfamily that catalyzes the central step of the Leloir pathway: the transfer of a UMP group from UDP-glucose to galactose-1-phosphate via a ping-pong double-displacement mechanism involving a covalent His166-UMP intermediate. This reaction produces glucose-1-phosphate (for glycolysis) and UDP-galactose (for glycosylation reactions). GALT is expressed broadly, with activity measured in liver, erythrocytes, and brain. Its deficiency causes classic galactosemia (Type I), the most severe inherited disorder of galactose metabolism, characterized by toxic accumulation of galactose-1-phosphate and galactitol, aberrant glycosylation, and severe multi-organ complications including neurological impairment and ovarian failure. The Q188R mutation is the most prevalent pathogenic variant in Caucasian populations, causing near-complete loss of catalytic function. Emerging gene therapy, mRNA therapy, pharmacological chaperone, and galactokinase inhibitor strategies are under active development to complement or replace dietary management.

References

1. (tyfield1999classicalgalactosemiaand pages 1-2): Linda Tyfield, Juergen Reichardt, Judy Fridovich-Keil, David T. Croke, Louis J. Elsas, Wolfgang Strobl, Libor Kozak, Turgay Coskun, Giuseppe Novelli, Yoshiyuki Okano, Cezary Zekanowski, Yoon Shin, and Ma Dolores Boleda. Classical galactosemia and mutations at the galactose‐1‐phosphate uridyl transferase (galt) gene. Human Mutation, 13:417-430, Jan 1999. URL: https://doi.org/10.1002/(sici)1098-1004(1999)13:6<417::aid-humu1>3.0.co;2-0, doi:10.1002/(sici)1098-1004(1999)13:6<417::aid-humu1>3.0.co;2-0. This article has 203 citations and is from a domain leading peer-reviewed journal.

2. (succoio2022galactosemiabiochemistrymolecular pages 2-4): Mariangela Succoio, Rosa Sacchettini, Alessandro Rossi, Giancarlo Parenti, and Margherita Ruoppolo. Galactosemia: biochemistry, molecular genetics, newborn screening, and treatment. Biomolecules, 12:968, Jul 2022. URL: https://doi.org/10.3390/biom12070968, doi:10.3390/biom12070968. This article has 90 citations.

3. (tyfield1999classicalgalactosemiaand pages 2-6): Linda Tyfield, Juergen Reichardt, Judy Fridovich-Keil, David T. Croke, Louis J. Elsas, Wolfgang Strobl, Libor Kozak, Turgay Coskun, Giuseppe Novelli, Yoshiyuki Okano, Cezary Zekanowski, Yoon Shin, and Ma Dolores Boleda. Classical galactosemia and mutations at the galactose‐1‐phosphate uridyl transferase (galt) gene. Human Mutation, 13:417-430, Jan 1999. URL: https://doi.org/10.1002/(sici)1098-1004(1999)13:6<417::aid-humu1>3.0.co;2-0, doi:10.1002/(sici)1098-1004(1999)13:6<417::aid-humu1>3.0.co;2-0. This article has 203 citations and is from a domain leading peer-reviewed journal.

4. (succoio2022galactosemiabiochemistrymolecular pages 1-2): Mariangela Succoio, Rosa Sacchettini, Alessandro Rossi, Giancarlo Parenti, and Margherita Ruoppolo. Galactosemia: biochemistry, molecular genetics, newborn screening, and treatment. Biomolecules, 12:968, Jul 2022. URL: https://doi.org/10.3390/biom12070968, doi:10.3390/biom12070968. This article has 90 citations.

5. (delnoy2021currentandfuture pages 1-6): Britt Delnoy, Ana I. Coelho, and Maria Estela Rubio-Gozalbo. Current and future treatments for classic galactosemia. Journal of Personalized Medicine, 11:75, Jan 2021. URL: https://doi.org/10.3390/jpm11020075, doi:10.3390/jpm11020075. This article has 55 citations.

6. (forte2023classicgalactosemiaclinical pages 5-7): Giovanna Forte, Antonia Lucia Buonadonna, Antonino Pantaleo, Candida Fasano, Donatella Capodiferro, Valentina Grossi, Paola Sanese, Filomena Cariola, Katia De Marco, Martina Lepore Signorile, Andrea Manghisi, Anna Filomena Guglielmi, Simonetta Simonetti, Nicola Laforgia, Vittoria Disciglio, and Cristiano Simone. Classic galactosemia: clinical and computational characterization of a novel galt missense variant (p.a303d) and a literature review. International Journal of Molecular Sciences, 24:17388, Dec 2023. URL: https://doi.org/10.3390/ijms242417388, doi:10.3390/ijms242417388. This article has 2 citations.

7. (wiertelak2025cytosolicudpgalbiosynthetic pages 3-4): Wojciech Wiertelak, Artem Pavlovskyi, Mariusz Olczak, and Dorota Maszczak-Seneczko. Cytosolic udp-gal biosynthetic machinery is required for dimerization of slc35a2 in the golgi membrane and its interaction with b4galt1. Frontiers in Molecular Biosciences, Mar 2025. URL: https://doi.org/10.3389/fmolb.2025.1563384, doi:10.3389/fmolb.2025.1563384. This article has 4 citations.

8. (brenner2002hintfhitand pages 10-11): Charles Brenner. Hint, fhit, and galt: function, structure, evolution, and mechanism of three branches of the histidine triad superfamily of nucleotide hydrolases and transferases. Biochemistry, 41 29:9003-14, Jul 2002. URL: https://doi.org/10.1021/bi025942q, doi:10.1021/bi025942q. This article has 363 citations and is from a peer-reviewed journal.

9. (brenner2002hintfhitand pages 8-9): Charles Brenner. Hint, fhit, and galt: function, structure, evolution, and mechanism of three branches of the histidine triad superfamily of nucleotide hydrolases and transferases. Biochemistry, 41 29:9003-14, Jul 2002. URL: https://doi.org/10.1021/bi025942q, doi:10.1021/bi025942q. This article has 363 citations and is from a peer-reviewed journal.

10. (durrant2020defectsingalactose pages 1-3): Christelle Durrant, Jana I. Fuehring, Alexandra Willemetz, Dominique Chrétien, Giusy Sala, Riccardo Ghidoni, Abram Katz, Agnès Rötig, Monica Thelestam, Myriam Ermonval, and Stuart E. H. Moore. Defects in galactose metabolism and glycoconjugate biosynthesis in a udp-glucose pyrophosphorylase-deficient cell line are reversed by adding galactose to the growth medium. International Journal of Molecular Sciences, 21:2028, Mar 2020. URL: https://doi.org/10.3390/ijms21062028, doi:10.3390/ijms21062028. This article has 15 citations.

11. (wiertelak2025cytosolicudpgalbiosynthetic pages 6-8): Wojciech Wiertelak, Artem Pavlovskyi, Mariusz Olczak, and Dorota Maszczak-Seneczko. Cytosolic udp-gal biosynthetic machinery is required for dimerization of slc35a2 in the golgi membrane and its interaction with b4galt1. Frontiers in Molecular Biosciences, Mar 2025. URL: https://doi.org/10.3389/fmolb.2025.1563384, doi:10.3389/fmolb.2025.1563384. This article has 4 citations.

12. (delnoy2021currentandfuture pages 6-9): Britt Delnoy, Ana I. Coelho, and Maria Estela Rubio-Gozalbo. Current and future treatments for classic galactosemia. Journal of Personalized Medicine, 11:75, Jan 2021. URL: https://doi.org/10.3390/jpm11020075, doi:10.3390/jpm11020075. This article has 55 citations.

13. (forte2023classicgalactosemiaclinical pages 1-2): Giovanna Forte, Antonia Lucia Buonadonna, Antonino Pantaleo, Candida Fasano, Donatella Capodiferro, Valentina Grossi, Paola Sanese, Filomena Cariola, Katia De Marco, Martina Lepore Signorile, Andrea Manghisi, Anna Filomena Guglielmi, Simonetta Simonetti, Nicola Laforgia, Vittoria Disciglio, and Cristiano Simone. Classic galactosemia: clinical and computational characterization of a novel galt missense variant (p.a303d) and a literature review. International Journal of Molecular Sciences, 24:17388, Dec 2023. URL: https://doi.org/10.3390/ijms242417388, doi:10.3390/ijms242417388. This article has 2 citations.

14. (tisa2022theimportanceof pages 5-6): Ioana Badiu Tișa, Anca Cristina Achim, and Anamaria Cozma-Petruț. The importance of neonatal screening for galactosemia. Nutrients, 15:10, Dec 2022. URL: https://doi.org/10.3390/nu15010010, doi:10.3390/nu15010010. This article has 50 citations.

15. (delnoy2021currentandfuture pages 9-13): Britt Delnoy, Ana I. Coelho, and Maria Estela Rubio-Gozalbo. Current and future treatments for classic galactosemia. Journal of Personalized Medicine, 11:75, Jan 2021. URL: https://doi.org/10.3390/jpm11020075, doi:10.3390/jpm11020075. This article has 55 citations.

16. (wiertelak2025cytosolicudpgalbiosynthetic pages 4-6): Wojciech Wiertelak, Artem Pavlovskyi, Mariusz Olczak, and Dorota Maszczak-Seneczko. Cytosolic udp-gal biosynthetic machinery is required for dimerization of slc35a2 in the golgi membrane and its interaction with b4galt1. Frontiers in Molecular Biosciences, Mar 2025. URL: https://doi.org/10.3389/fmolb.2025.1563384, doi:10.3389/fmolb.2025.1563384. This article has 4 citations.

17. (panis2024brainfunctionin pages 4-5): Bianca Panis, E. Vos, Ivo Bari ć, A. Bosch, M. Brouwers, A. Burlina, D. Cassiman, David J Coman, María-Luz Couce, Anibh M. Das, D. Demirbas, A. Empain, Matthias Gautschi, Olga Grafakou, Stephanie Grűnewald, S. D. Kingma, I. Knerr, Elisa Leão-Teles, D. Möslinger, Elaine Murphy, K. Õunap, Adriana Pané, Sabrina Paci, Rossella Parini, Isabel Rivera, S. Scholl-Bürgi, I. V. D. Schwartz, Triantafyllia Sdogou, L. Shakerdi, A. Skouma, Karolina M. Stepien, Eileen P. Treacy, Susan E. Waisbren, Gerard T. Berry, M. Rubio-Gozalbo, P. Tanpaiboon, A. Gropman, Bosch Brouwers Burlina Cassiman Coman Couce Das Demirbas Bari ć, Rubio-Gozalbo. This, and Cyprus Nicosia. Brain function in classic galactosemia, a galactosemia network (galnet) members review. Frontiers in Genetics, Feb 2024. URL: https://doi.org/10.3389/fgene.2024.1355962, doi:10.3389/fgene.2024.1355962. This article has 14 citations and is from a peer-reviewed journal.

18. (boulanger2021sugarphosphatetoxicities pages 12-14): Erin F. Boulanger, Anice Sabag-Daigle, Pankajavalli Thirugnanasambantham, Venkat Gopalan, and Brian M. M. Ahmer. Sugar-phosphate toxicities. Dec 2021. URL: https://doi.org/10.1128/mmbr.00123-21, doi:10.1128/mmbr.00123-21. This article has 66 citations and is from a domain leading peer-reviewed journal.

19. (tyfield1999classicalgalactosemiaand pages 8-10): Linda Tyfield, Juergen Reichardt, Judy Fridovich-Keil, David T. Croke, Louis J. Elsas, Wolfgang Strobl, Libor Kozak, Turgay Coskun, Giuseppe Novelli, Yoshiyuki Okano, Cezary Zekanowski, Yoon Shin, and Ma Dolores Boleda. Classical galactosemia and mutations at the galactose‐1‐phosphate uridyl transferase (galt) gene. Human Mutation, 13:417-430, Jan 1999. URL: https://doi.org/10.1002/(sici)1098-1004(1999)13:6<417::aid-humu1>3.0.co;2-0, doi:10.1002/(sici)1098-1004(1999)13:6<417::aid-humu1>3.0.co;2-0. This article has 203 citations and is from a domain leading peer-reviewed journal.

20. (wang2024acasereport pages 5-8): Yong-cai Wang, Lian-cheng Lan, Xia Yang, Juan Xiao, Hai-xin Liu, and Qing-wen Shan. A case report of classic galactosemia with a galt gene variant and a literature review. BMC Pediatrics, May 2024. URL: https://doi.org/10.1186/s12887-024-04769-0, doi:10.1186/s12887-024-04769-0. This article has 6 citations and is from a peer-reviewed journal.

21. (succoio2022galactosemiabiochemistrymolecular pages 12-13): Mariangela Succoio, Rosa Sacchettini, Alessandro Rossi, Giancarlo Parenti, and Margherita Ruoppolo. Galactosemia: biochemistry, molecular genetics, newborn screening, and treatment. Biomolecules, 12:968, Jul 2022. URL: https://doi.org/10.3390/biom12070968, doi:10.3390/biom12070968. This article has 90 citations.

22. (succoio2022galactosemiabiochemistrymolecular pages 8-9): Mariangela Succoio, Rosa Sacchettini, Alessandro Rossi, Giancarlo Parenti, and Margherita Ruoppolo. Galactosemia: biochemistry, molecular genetics, newborn screening, and treatment. Biomolecules, 12:968, Jul 2022. URL: https://doi.org/10.3390/biom12070968, doi:10.3390/biom12070968. This article has 90 citations.

23. (tisa2022theimportanceof pages 11-12): Ioana Badiu Tișa, Anca Cristina Achim, and Anamaria Cozma-Petruț. The importance of neonatal screening for galactosemia. Nutrients, 15:10, Dec 2022. URL: https://doi.org/10.3390/nu15010010, doi:10.3390/nu15010010. This article has 50 citations.

24. (bellagamba2025experimentalgalactose1phosphateuridylyltransferase pages 16-17): O. Bellagamba, A. Guo, Xinhua Yan, Joe Sarkis, B. Balakrishnan, and Kent Lai. Experimental galactose-1-phosphate uridylyltransferase (galt) mrna therapy improves motor-related phenotypes in a mouse model of classic galactosemia—a pilot study. Biomedicines, Apr 2025. URL: https://doi.org/10.3390/biomedicines13122848, doi:10.3390/biomedicines13122848. This article has 0 citations.

25. (succoio2022galactosemiabiochemistrymolecular pages 6-8): Mariangela Succoio, Rosa Sacchettini, Alessandro Rossi, Giancarlo Parenti, and Margherita Ruoppolo. Galactosemia: biochemistry, molecular genetics, newborn screening, and treatment. Biomolecules, 12:968, Jul 2022. URL: https://doi.org/10.3390/biom12070968, doi:10.3390/biom12070968. This article has 90 citations.

## Artifacts

- [Edison artifact artifact-00](GALT-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](GALT-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. delnoy2021currentandfuture pages 9-13
2. brenner2002hintfhitand pages 8-9
3. brenner2002hintfhitand pages 10-11
4. forte2023classicgalactosemiaclinical pages 5-7
5. wiertelak2025cytosolicudpgalbiosynthetic pages 3-4
6. wiertelak2025cytosolicudpgalbiosynthetic pages 6-8
7. wiertelak2025cytosolicudpgalbiosynthetic pages 4-6
8. panis2024brainfunctionin pages 4-5
9. boulanger2021sugarphosphatetoxicities pages 12-14
10. delnoy2021currentandfuture pages 1-6
11. forte2023classicgalactosemiaclinical pages 1-2
12. succoio2022galactosemiabiochemistrymolecular pages 2-4
13. tyfield1999classicalgalactosemiaand pages 8-10
14. tyfield1999classicalgalactosemiaand pages 1-2
15. succoio2022galactosemiabiochemistrymolecular pages 8-9
16. succoio2022galactosemiabiochemistrymolecular pages 6-8
17. tyfield1999classicalgalactosemiaand pages 2-6
18. succoio2022galactosemiabiochemistrymolecular pages 1-2
19. durrant2020defectsingalactose pages 1-3
20. delnoy2021currentandfuture pages 6-9
21. tisa2022theimportanceof pages 5-6
22. wang2024acasereport pages 5-8
23. succoio2022galactosemiabiochemistrymolecular pages 12-13
24. tisa2022theimportanceof pages 11-12
25. https://doi.org/10.1002/(sici
26. https://doi.org/10.3390/biom12070968,
27. https://doi.org/10.3390/jpm11020075,
28. https://doi.org/10.3390/ijms242417388,
29. https://doi.org/10.3389/fmolb.2025.1563384,
30. https://doi.org/10.1021/bi025942q,
31. https://doi.org/10.3390/ijms21062028,
32. https://doi.org/10.3390/nu15010010,
33. https://doi.org/10.3389/fgene.2024.1355962,
34. https://doi.org/10.1128/mmbr.00123-21,
35. https://doi.org/10.1186/s12887-024-04769-0,
36. https://doi.org/10.3390/biomedicines13122848,