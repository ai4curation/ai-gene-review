---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-02T06:42:11.676979'
end_time: '2026-10-02T06:54:27.634181'
duration_seconds: 735.96
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: ARATH
  gene_id: CYP71A13
  gene_symbol: CYP71A13
  uniprot_accession: O49342
  protein_description: 'RecName: Full=Indoleacetaldoxime dehydratase; EC=4.8.1.3 {ECO:0000269|PubMed:17573535};
    AltName: Full=Cytochrome P450 71A13;'
  gene_info: Name=CYP71A13; OrderedLocusNames=At2g30770; ORFNames=T11J7.16;
  organism_full: Arabidopsis thaliana (Mouse-ear cress).
  protein_family: Belongs to the cytochrome P450 family. .
  protein_domains: Cyt_P450. (IPR001128); Cyt_P450_CS. (IPR017972); Cyt_P450_E_grp-I.
    (IPR002401); Cyt_P450_sf. (IPR036396); p450 (PF00067)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 17
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: CYP71A13-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: CYP71A13-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** O49342
- **Protein Description:** RecName: Full=Indoleacetaldoxime dehydratase; EC=4.8.1.3 {ECO:0000269|PubMed:17573535}; AltName: Full=Cytochrome P450 71A13;
- **Gene Information:** Name=CYP71A13; OrderedLocusNames=At2g30770; ORFNames=T11J7.16;
- **Organism (full):** Arabidopsis thaliana (Mouse-ear cress).
- **Protein Family:** Belongs to the cytochrome P450 family. .
- **Key Domains:** Cyt_P450. (IPR001128); Cyt_P450_CS. (IPR017972); Cyt_P450_E_grp-I. (IPR002401); Cyt_P450_sf. (IPR036396); p450 (PF00067)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CYP71A13" matches the protein description above**
2. **Verify the organism is correct:** Arabidopsis thaliana (Mouse-ear cress).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CYP71A13' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CYP71A13** (gene ID: CYP71A13, UniProt: O49342) in ARATH.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# CYP71A13 (At2g30770, UniProt O49342): The Endoplasmic Reticulum Cytochrome P450 Committing Tryptophan-Derived Aldoxime to Camalexin Biosynthesis in *Arabidopsis thaliana*

**Gene:** CYP71A13 | **Locus:** At2g30770 (ORF T11J7.16) | **UniProt:** O49342
**Organism:** *Arabidopsis thaliana* (mouse-ear cress)
**Protein family:** Cytochrome P450, CYP71 clan (Cyt_P450 / PF00067; IPR001128, IPR017972, IPR002401, IPR036396)
**Enzyme designation:** Indoleacetaldoxime dehydratase, EC 4.8.1.3

---

## Summary

**CYP71A13** (gene name *CYP71A13*; ordered locus **At2g30770**; UniProt **O49342**) is a membrane-anchored cytochrome P450 monooxygenase of *Arabidopsis thaliana* that performs a committed, branch-point reaction in the biosynthesis of **camalexin**, the major indolic phytoalexin of the Brassicaceae. The enzyme catalyzes the conversion of the tryptophan-derived intermediate **indole-3-acetaldoxime (IAOx)** into **indole-3-acetonitrile (IAN)**. Although it belongs to the cytochrome P450 family (and was named Cytochrome P450 71A13), the net physiological transformation it carries out is a **dehydration of an aldoxime to a nitrile**, which is why it carries the enzyme designation **indoleacetaldoxime dehydratase, EC 4.8.1.3** ([PMID: 17573535](https://pubmed.ncbi.nlm.nih.gov/17573535/)). This target identity is fully consistent with the UniProt record: the protein is the CYP71A13 product of *Arabidopsis thaliana*, a cytochrome P450 (Cyt_P450 / PF00067 domains), and all literature retrieved corresponds precisely to this gene, organism, and family. There is **no gene-symbol ambiguity**; the primary biochemical, genetic, and biophysical literature all converge on the same molecule.

Functionally, CYP71A13 sits at a **metabolic branch point** downstream of CYP79B2/CYP79B3, which produce IAOx from tryptophan. IAOx is a shared precursor that can be routed toward indolic glucosinolates (via CYP83B1), toward the auxin indole-3-acetic acid (IAA), or toward camalexin. CYP71A13 is the enzyme that **channels IAOx specifically into the camalexin branch**, producing IAN, which is then elaborated by GSTF6, downstream peptidase/transferase steps, and the multifunctional P450 CYP71B15 (PAD3) to yield camalexin. Loss of CYP71A13 strongly reduces pathogen-induced camalexin and compromises resistance to necrotrophic fungi; exogenous IAN restores camalexin in the mutant, placing the enzyme firmly upstream of IAN.

Spatially, CYP71A13 is a **class-II (microsomal) heme-thiolate cytochrome P450 anchored to the cytosolic face of the endoplasmic reticulum (ER)**, where it draws electrons from the ER-resident NADPH–cytochrome P450 reductase. It does not act in isolation: biophysical studies show it physically assembles with the other camalexin-pathway enzymes into an **ER-localized metabolon** that channels the reactive IAOx intermediate directly into camalexin without leakage into competing branches. Transcriptionally, *CYP71A13* is a **pathogen-inducible gene** co-regulated with the downstream camalexin gene *PAD3* and governed by the master immune transcription factor **WRKY33**, distinct from the MYB-controlled module that supplies IAOx. The enzyme acts redundantly with its tandem paralog **CYP71A12**: single mutants retain partial camalexin, whereas the double knockout is essentially camalexin-free.

---

## Key Findings

### Finding 1 — CYP71A13 catalyzes the dehydration of IAOx to IAN (the defining biochemical activity)

The primary biochemical function of CYP71A13 was established by Nafisi et al. (2007) through direct heterologous enzyme assays. **Recombinant CYP71A13 expressed in *Escherichia coli* converted IAOx to indole-3-acetonitrile (IAN)** ([PMID: 17573535](https://pubmed.ncbi.nlm.nih.gov/17573535/)). The activity was reconstituted *in planta*: **co-expression of CYP79B2 and CYP71A13 in *Nicotiana benthamiana* resulted in the conversion of tryptophan to IAN** ([PMID: 17573535](https://pubmed.ncbi.nlm.nih.gov/17573535/)), since CYP79B2 supplies IAOx from Trp and CYP71A13 converts that IAOx to IAN.

The net transformation — removal of water from the aldoxime to generate a nitrile — is described in the literature as a dehydration: tryptophan "is converted to indole-3-acetaldoxime and subsequently dehydrated to indole-3-acetonitrile" ([PMID: 19523656](https://pubmed.ncbi.nlm.nih.gov/19523656/)). This explains the apparent paradox between the protein's family identity (a cytochrome P450 monooxygenase by sequence) and its enzyme classification as an **indoleacetaldoxime dehydratase (EC 4.8.1.3)**. CYP71A13 is thus a P450 that performs a non-canonical, dehydratase-type net reaction on its physiological aldoxime substrate. Later biophysical work (see Finding 8) refined the chemistry, reporting that CYP71A13 synthesizes the **intermediary indole-3-cyanohydrin** (a nitrile-equivalent that is subsequently glutathionylated), consistent with the IAOx→nitrile transformation.

**Substrate specificity:** the physiological substrate is the tryptophan-derived oxime IAOx, and the product is IAN. This is the committed, pathway-defining step of camalexin biosynthesis.

### Finding 2 — CYP71A13 is required for pathogen-induced camalexin and resistance to necrotrophic fungi

Genetic loss-of-function analysis demonstrated the biological importance of the enzyme. **Plants carrying *cyp71A13* mutations produce greatly reduced amounts of camalexin after infection by *Pseudomonas syringae* or *Alternaria brassicicola* and are susceptible to *A. brassicicola*, as are *pad3* and *cyp79B2 cyp79B3* mutants** ([PMID: 17573535](https://pubmed.ncbi.nlm.nih.gov/17573535/)). This places CYP71A13 alongside the other core camalexin biosynthetic genes as essential for the phytoalexin-based defense response.

Crucially, the metabolic position of the enzyme was confirmed by chemical complementation: **exogenously supplied IAN restored camalexin production in *cyp71A13* mutant plants** ([PMID: 17573535](https://pubmed.ncbi.nlm.nih.gov/17573535/)). Because feeding the product (IAN) bypasses the enzymatic lesion, CYP71A13 must act **upstream of IAN** and downstream of IAOx — exactly the IAOx→IAN step. Independent induced-resistance studies corroborate the requirement for CYP71A13-dependent camalexin in multiple biotic contexts ([PMID: 23073694](https://pubmed.ncbi.nlm.nih.gov/23073694/)).

### Finding 3 — CYP71A13 acts at a metabolic branch point, diverting IAOx from glucosinolates/auxin into camalexin

IAOx, generated from tryptophan by CYP79B2/CYP79B3, is a shared intermediate that feeds three distinct outputs. As stated in the literature, **"IAOx serves as an intermediate in the biosynthesis of indole glucosinolates (I-GLSs), camalexin and the plant hormone indole-3-acetic acid (IAA)"** ([PMID: 19263076](https://pubmed.ncbi.nlm.nih.gov/19263076/)). The partitioning of this pool is enzyme-controlled: **"CYP83B1 channels IAOx into I-GLS biosynthesis, CYP71A13 channels IAOx into camalexin biosynthesis, whereas the IAOx-metabolizing enzyme in IAA biosynthesis is not known"** ([PMID: 19263076](https://pubmed.ncbi.nlm.nih.gov/19263076/)).

CYP71A13 is therefore the **commitment/entry enzyme** that dedicates the oxime pool specifically to camalexin. This branch-point role is reinforced by regulation: transcription of *CYP71A13* and *PAD3* is co-regulated and pathogen-induced, while the shared upstream step is controlled by R2R3-MYB factors (MYB34/MYB51/MYB122) — see Finding 6.

### Finding 4 — CYP71A13 acts redundantly with its tandem paralog CYP71A12

CYP71A13 is not the only IAOx dehydratase in *Arabidopsis*. **"The *CYP71A13* gene is located in tandem with its close homolog *CYP71A12*, also encoding an IAOx dehydratase"** ([PMID: 25953104](https://pubmed.ncbi.nlm.nih.gov/25953104/)). The two paralogs are partially redundant: **"in contrast to *cyp71a13* plants, in which camalexin accumulation is partially reduced, double mutants synthesized only traces of camalexin"** ([PMID: 25953104](https://pubmed.ncbi.nlm.nih.gov/25953104/)). This gene-dosage pattern — partial loss in the single mutant, near-complete loss in the double knockout — demonstrates that CYP71A12 also contributes to the committed step.

The paralogs have partially diverged. CYP71A12 is more root-associated and preferentially yields indole-3-carbaldehyde/indole-3-carboxylic acid derivatives, and it is specifically implicated in root/exudate camalexin responses ([PMID: 20348432](https://pubmed.ncbi.nlm.nih.gov/20348432/); [PMID: 35191984](https://pubmed.ncbi.nlm.nih.gov/35191984/)), while CYP71A13 carries much of the leaf camalexin flux. This tandem-duplication redundancy buffers phytoalexin production across tissues.

### Finding 5 — CYP71A13 is an ER-membrane-anchored P450 that assembles into a camalexin metabolon

As a CYP71-family cytochrome P450 (UniProt O49342; domains Cyt_P450 / PF00067), CYP71A13 carries an N-terminal membrane anchor and localizes to the **cytosolic face of the endoplasmic reticulum**, where it is reduced by the ER-resident NADPH–cytochrome P450 reductase. Mucha et al. (2019) demonstrated that the camalexin pathway enzymes — CYP79B2/B3, CYP71A12/A13, CYP71B15/PAD3, and GSTF6 — physically associate into an **ER-localized metabolon** that channels the unstable intermediate IAOx (*The Formation of a Camalexin Biosynthetic Metabolon*, [PMID: 31511315](https://pubmed.ncbi.nlm.nih.gov/31511315/)).

The site of action is therefore the **ER membrane**. Metabolon assembly provides a mechanistic rationale for efficient channeling: by co-localizing CYP71A13 with its upstream (CYP79B2/B3) and downstream (PAD3, GSTF6) partners, the reactive/toxic IAOx intermediate can be passed directly into the camalexin branch without escaping into the competing glucosinolate or auxin routes.

### Finding 6 — CYP71A13 is a pathogen-inducible gene in the WRKY33-controlled camalexin regulon

*CYP71A13* expression is induced by bacterial and fungal pathogens and is tightly co-regulated with the downstream camalexin gene *CYP71B15/PAD3*: **"Expression levels of CYP71A13 and PAD3 are coregulated"** ([PMID: 17573535](https://pubmed.ncbi.nlm.nih.gov/17573535/)). This dedicated camalexin branch is driven by the master immune transcription factor WRKY33, consistent with **"camalexin accumulation via WRKY33-targeted transcription of PAD3"** ([PMID: 36319610](https://pubmed.ncbi.nlm.nih.gov/36319610/)).

Importantly, this regulatory module is **distinct** from the one controlling IAOx supply. The R2R3-MYB factors MYB34/MYB51/MYB122 control the shared upstream step (CYP79B2/B3), but the camalexin-specific genes are not dependent on them: **"Consistently expression of the camalexin biosynthesis genes CYP71B15/PAD3 and CYP71A13 was not negatively affected in the triple myb mutant"** ([PMID: 26379682](https://pubmed.ncbi.nlm.nih.gov/26379682/)). CYP71A13 thus belongs to the inducible, WRKY33-governed camalexin regulon rather than the MYB-governed indole-supply module. Additional regulatory layers converge on this branch, including WRKY33-dependent CCCH-protein C3H14 ([PMID: 32279333](https://pubmed.ncbi.nlm.nih.gov/32279333/)), hierarchical WRKY/MYB networks ([PMID: 32082343](https://pubmed.ncbi.nlm.nih.gov/32082343/)), ROS-triggered WRKY33 induction ([PMID: 31749193](https://pubmed.ncbi.nlm.nih.gov/31749193/)), and an enhancer–promoter–WRKY15 module that constrains PAD3/GSTU4 to maintain immune homeostasis ([PMID: 39628054](https://pubmed.ncbi.nlm.nih.gov/39628054/)). *CYP71A13* is also induced during beneficial microbial interactions, where IAOx-derived compounds restrict root colonization ([PMID: 22852809](https://pubmed.ncbi.nlm.nih.gov/22852809/)).

### Finding 7 — Sequence analysis confirms CYP71A13 is a microsomal (ER) heme-thiolate cytochrome P450

Bioinformatic analysis of the 497-amino-acid CYP71A13 protein (UniProt O49342) independently corroborates its localization and catalytic chemistry. The protein begins with a **hydrophobic N-terminal segment** (residues ~7–21, "SLCLTTLITLLLLRR"; mean Kyte–Doolittle hydropathy of residues 2–25 ≈ +1.45) that constitutes the type-I N-terminal signal-anchor tethering the enzyme to the ER membrane. It contains the absolutely conserved P450 **heme-binding signature FxxGxRxCxG** ("FGSGRRICPG" at residues 432–441), whose invariant Cys439 is the proximal thiolate ligand to the heme iron, together with the **K-helix ExxR motif**. These are the hallmarks of a catalytically competent class-II (microsomal) cytochrome P450. The structural features thus independently confirm ER-membrane localization and a heme-thiolate oxygen-activating active site, consistent with CYP71 monooxygenase ancestry even though the net physiological reaction on IAOx is a dehydration.

### Finding 8 — CYP71A13 physically interacts with pathway P450s and P450-reductase and allosterically enhances CYP79B2

Direct biophysical evidence places CYP71A13 inside a functional multi-enzyme complex. Using untargeted co-immunoprecipitation with CYP71A13 and CYP71B15 as baits, Mucha et al. showed that **"the camalexin biosynthetic P450 enzymes copurified with these enzymes"** ([PMID: 31511315](https://pubmed.ncbi.nlm.nih.gov/31511315/)), with interactions confirmed by targeted co-IP and FRET-FLIM (Förster resonance energy transfer by fluorescence-lifetime microscopy). CYP71A13 is electronically coupled to its redox partner — **"the interaction of CYP71A13 and Arabidopsis P450 Reductase1 was observed"** ([PMID: 31511315](https://pubmed.ncbi.nlm.nih.gov/31511315/)) — consistent with microsomal P450 function.

Beyond assembly, CYP71A13 **allosterically tunes upstream flux**: **"We detected increased substrate affinity of CYP79B2 in the presence of CYP71A13, indicating an allosteric interaction"** ([PMID: 31511315](https://pubmed.ncbi.nlm.nih.gov/31511315/)). The glutathione transferase GSTU4 is also physically recruited to the complex, and the overall rationale is metabolic channeling: **"the biosynthetic pathway of this compound is channeled by the formation of an enzyme complex"** ([PMID: 31511315](https://pubmed.ncbi.nlm.nih.gov/31511315/)). Channeling prevents leakage of the reactive IAOx/nitrile intermediates and explains the pathway's efficiency and specificity toward camalexin.

---

## Mechanistic Model and Interpretation

### The camalexin branch of tryptophan metabolism

CYP71A13 operates within a branched pathway that converts tryptophan into several classes of indolic defense metabolites. The committed branch to camalexin begins with the dehydration of IAOx to IAN carried out by CYP71A13 (and its paralog CYP71A12).

```
                        Tryptophan (Trp)
                             |
                   CYP79B2 / CYP79B3   (MYB34/51/122-controlled; ER-anchored P450s)
                             |
                             v
              Indole-3-acetaldoxime (IAOx)   <-- shared branch-point intermediate
                   /         |          \
          CYP83B1       CYP71A13 /      (unknown)
             |          CYP71A12            |
             v             |               v
   Indolic glucosinolates  |            Auxin (IAA)
     (I-GLS)               v
                 Indole-3-acetonitrile (IAN)   <-- committed to camalexin
                           |
                        GSTF6 (GSH conjugation) --> GSH(IAN)
                           |
                   GGTs / PCS / peptidase steps
                           |
                           v
                     Cys(IAN)
                           |
                 CYP71B15 / PAD3 (multifunctional P450:
                 thiazoline ring closure, DHCA formation, cyanide release)
                           |
                           v
                      CAMALEXIN  (antimicrobial phytoalexin)
```

The downstream steps are well characterized: GSTF6 conjugates IAN to glutathione, GGTs and PCS process the conjugate toward Cys(IAN) ([PMID: 21239642](https://pubmed.ncbi.nlm.nih.gov/21239642/)), and the multifunctional CYP71B15/PAD3 performs thiazoline ring closure, dihydrocamalexic-acid formation, and cyanide release to yield camalexin ([PMID: 19567706](https://pubmed.ncbi.nlm.nih.gov/19567706/)).

CYP71A13's strategic importance lies in its position at the **first committed step** of the camalexin branch. IAOx is a reactive, potentially toxic intermediate shared by three competing routes; the enzyme that consumes it determines flux direction. By converting IAOx to IAN, CYP71A13 dedicates this carbon specifically to camalexin and away from indolic glucosinolates (CYP83B1) and auxin.

### Spatial organization: an ER metabolon with channeling and allostery

The enzyme does not function as a free-floating catalyst. The experimental and bioinformatic evidence converge on the following spatial/functional model:

| Property | Evidence | Source |
|---|---|---|
| ER-membrane localization | N-terminal hydrophobic signal-anchor (Kyte–Doolittle ≈ +1.45); microsomal P450 class II | Finding 7; [PMID: 31511315](https://pubmed.ncbi.nlm.nih.gov/31511315/) |
| Heme-thiolate active site | Conserved FxxGxRxCxG with Cys439 proximal ligand; ExxR motif | Finding 7 |
| Redox coupling | Physical interaction with Arabidopsis P450 Reductase1 | [PMID: 31511315](https://pubmed.ncbi.nlm.nih.gov/31511315/) |
| Metabolon assembly | Co-IP + FRET-FLIM with CYP79B2/B3, CYP71A12, PAD3, GSTF6/GSTU4 | [PMID: 31511315](https://pubmed.ncbi.nlm.nih.gov/31511315/) |
| Allosteric upstream control | Increases CYP79B2 substrate affinity | [PMID: 31511315](https://pubmed.ncbi.nlm.nih.gov/31511315/) |
| Metabolic channeling | Pathway proceeds without release of reactive IAOx | [PMID: 31511315](https://pubmed.ncbi.nlm.nih.gov/31511315/) |

This arrangement elegantly solves two problems simultaneously: (1) it prevents the reactive IAOx intermediate from escaping into competing branches or causing cellular damage, and (2) by boosting CYP79B2 affinity, CYP71A13 helps match upstream IAOx supply to downstream consumption — a feed-forward optimization of the committed pathway.

### Regulatory logic: a WRKY33-controlled, pathogen-inducible defense module

CYP71A13 is embedded in the inducible plant immune response. Its transcription is co-regulated with *PAD3* and controlled by WRKY33, the master regulator of camalexin biosynthesis, and is independent of the MYB34/51/122 factors that govern the shared upstream IAOx-supplying step. This regulatory separation means the plant can modulate how much of its indolic precursor pool is dedicated to camalexin (via the WRKY33 branch) semi-independently of how much total IAOx is made (via the MYB branch). The result is a system in which pathogen perception rapidly and specifically ramps up camalexin-committed enzymes, including CYP71A13.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the findings |
|---|---|---|
| [17573535](https://pubmed.ncbi.nlm.nih.gov/17573535/) | *CYP71A13 catalyzes the conversion of IAOx in camalexin synthesis* | **Foundational paper.** Direct enzyme assay (E. coli) showing IAOx→IAN; N. benthamiana reconstitution (Trp→IAN with CYP79B2); loss-of-function mutant phenotype (reduced camalexin, A. brassicicola susceptibility); IAN chemical complementation; CYP71A13/PAD3 co-regulation. Supports Findings 1, 2, 6. |
| [19263076](https://pubmed.ncbi.nlm.nih.gov/19263076/) | *Controlled IAOx production via ethanol-induced CYP79B2* | Establishes IAOx as the three-way branch-point intermediate (I-GLS, camalexin, IAA) and names CYP71A13 as the enzyme channeling IAOx into camalexin. Supports Finding 3. |
| [25953104](https://pubmed.ncbi.nlm.nih.gov/25953104/) | *cyp71a12 cyp71a13 double knockout (TALEN) metabolic analysis* | Documents tandem paralog CYP71A12 as a second IAOx dehydratase; single vs. double mutant camalexin levels establish redundancy. Supports Finding 4. |
| [31511315](https://pubmed.ncbi.nlm.nih.gov/31511315/) | *The Formation of a Camalexin Biosynthetic Metabolon* | Co-IP + FRET-FLIM evidence for ER metabolon; CYP71A13–P450 Reductase1 interaction; allosteric enhancement of CYP79B2; metabolic channeling; GSTU4 recruitment. Supports Findings 5, 8. |
| [26379682](https://pubmed.ncbi.nlm.nih.gov/26379682/) | *MYB34/51/122 in camalexin regulation* | Shows CYP71A13 and PAD3 expression is not reduced in the myb triple mutant, separating camalexin-branch regulation from MYB-controlled IAOx supply. Supports Finding 6. |
| [36319610](https://pubmed.ncbi.nlm.nih.gov/36319610/) | *OXI1 coordinates NHP, SA, camalexin* | Links camalexin accumulation to WRKY33-targeted PAD3 transcription. Supports Finding 6. |
| [19523656](https://pubmed.ncbi.nlm.nih.gov/19523656/) | *Evolution of camalexin and related indolic compounds* | Describes the net reaction as dehydration of IAOx to IAN. Supports Finding 1. |
| [21239642](https://pubmed.ncbi.nlm.nih.gov/21239642/) | *Glutathione-IAN is required for camalexin biosynthesis* | Defines the downstream route: GSTF6 conjugates IAN to GSH; GGTs/PCS process GSH(IAN) toward Cys(IAN). Contextualizes CYP71A13's product (IAN). |
| [19567706](https://pubmed.ncbi.nlm.nih.gov/19567706/) | *CYP71B15 (PAD3) converts Cys(IAN) to camalexin* | Establishes the terminal step; confirms IAN as the pathway's committed intermediate downstream of CYP71A13. |
| [20348432](https://pubmed.ncbi.nlm.nih.gov/20348432/) | *MAMP-activated root immune responses* | CYP71A12-dependent camalexin exudation in roots; illustrates paralog tissue divergence. Supports Finding 4. |
| [35191984](https://pubmed.ncbi.nlm.nih.gov/35191984/) | *Priming of camalexin in ISR by beneficial bacteria* | CYP71A12/PAD3 contribution to camalexin in ISR; paralog context. Supports Finding 4. |
| [23073694](https://pubmed.ncbi.nlm.nih.gov/23073694/) | *Pf.SS101-induced resistance* | cyp71A13/cyp71A12 among mutants showing camalexin/glucosinolate requirement for induced resistance. Supports Findings 2, 3. |
| [22852809](https://pubmed.ncbi.nlm.nih.gov/22852809/) | *IAOx-derived compounds restrict P. indica root colonization* | CYP71A13 induced during beneficial interactions; IAOx-derived metabolites regulate symbiosis. Supports Finding 6 context. |
| [35257500](https://pubmed.ncbi.nlm.nih.gov/35257500/) | *WRKY33-mediated IGS pathway and camalexin loss in Brassica* | Evolutionary/regulatory context for the WRKY33-governed Trp-metabolite network. Supports Finding 6. |
| [32279333](https://pubmed.ncbi.nlm.nih.gov/32279333/); [32082343](https://pubmed.ncbi.nlm.nih.gov/32082343/); [39628054](https://pubmed.ncbi.nlm.nih.gov/39628054/); [31749193](https://pubmed.ncbi.nlm.nih.gov/31749193/) | *WRKY33/MYB regulatory network papers* | Collectively define the WRKY33-centered transcriptional network controlling the camalexin branch in which CYP71A13 resides. Supports Finding 6. |

**Convergence:** Every line of evidence — biochemical (heterologous assay), genetic (loss-of-function + chemical complementation), biophysical (co-IP/FRET-FLIM), and bioinformatic (sequence motifs) — points to the same conclusion. No retrieved paper challenges the core function; disagreement in the literature concerns only the fine chemistry of the product (nitrile vs. indole-3-cyanohydrin) and the relative tissue contributions of the two paralogs.

---

## Limitations and Knowledge Gaps

1. **Precise reaction mechanism.** CYP71A13 is a P450 by sequence yet produces a nitrile from an aldoxime (net dehydration, EC 4.8.1.3). Later work reports an **indole-3-cyanohydrin** product that is subsequently glutathionylated ([PMID: 31511315](https://pubmed.ncbi.nlm.nih.gov/31511315/)). The exact catalytic chemistry — whether a classical dehydration or an oxidative route through a cyanohydrin — and the oxygen/electron requirements have not been fully resolved at atomic resolution.

2. **No experimental 3D structure.** All structural inferences (ER anchor, heme-thiolate ligation, ExxR motif) are from sequence analysis and homology to the P450 fold. No crystal or cryo-EM structure of CYP71A13 exists, so the active-site architecture and substrate-binding determinants are modeled, not observed.

3. **Substrate-specificity breadth untested.** The physiological substrate (IAOx) is clear, but systematic screening against related aldoximes or the degree of overlap with CYP71A12's substrate/product preferences has not been exhaustively characterized in vitro.

4. **Metabolon stoichiometry and dynamics.** The metabolon was demonstrated qualitatively (interactions, channeling, allostery). The composition, stoichiometry, assembly/disassembly kinetics, and whether the complex is constitutive or pathogen-induced remain open.

5. **Paralog division of labor.** CYP71A12 vs. CYP71A13 tissue- and product-specialization is described but not fully quantified; the extent to which each dominates in roots vs. leaves and under different elicitors needs finer dissection.

6. **Regulation beyond transcription.** Post-translational control (phosphorylation, turnover, metabolon-dependent stabilization) of CYP71A13 during immune activation is essentially unexplored.

---

## Proposed Follow-up Experiments / Actions

1. **Structural determination.** Obtain a cryo-EM or crystal structure of CYP71A13 (and/or an AlphaFold model refined with experimental restraints) to define the active site, the heme pocket, and substrate-binding residues; pair with docking of IAOx to clarify the dehydration mechanism.

2. **Mechanistic enzymology.** Use purified, reconstituted CYP71A13 with defined reductase and NADPH to measure O₂ consumption, detect reaction intermediates (e.g., indole-3-cyanohydrin), and distinguish a true dehydration from an oxidative route via isotope labeling (¹⁸O₂/H₂¹⁸O) and stopped-flow kinetics.

3. **Substrate-specificity panel.** Assay CYP71A13 and CYP71A12 side-by-side against a panel of aryl-aldoximes to quantify specificity constants and define the structural basis of their partially divergent product profiles.

4. **Quantitative metabolon biology.** Use split-fluorophore/BiFC, proximity labeling (TurboID), and quantitative FRET to map metabolon composition and stoichiometry, and test whether assembly is induced by pathogen elicitation and required for channeling in vivo.

5. **Flux analysis at the branch point.** Apply ¹³C/¹⁵N-labeled tryptophan flux tracing in wild-type, cyp71a13, cyp71a12, and double mutants (± CYP83B1 perturbation) to quantitatively partition IAOx between camalexin, glucosinolates, and auxin, and to test the allosteric CYP79B2 enhancement in vivo.

6. **Regulatory dissection.** ChIP and reporter assays to directly map WRKY33 (and WRKY15/C3H14) binding at the *CYP71A13* promoter, and test post-translational modifications of the protein during the immune response.

---

## Conclusion

CYP71A13 (At2g30770; UniProt O49342) is unambiguously identified as the *Arabidopsis thaliana* cytochrome P450 that commits tryptophan-derived indole-3-acetaldoxime to camalexin. It is an ER-membrane-anchored, heme-thiolate class-II P450 that catalyzes the dehydration of IAOx to indole-3-acetonitrile (EC 4.8.1.3) — the first committed step of the camalexin branch — operating within a channeling ER metabolon, coupled to NADPH–cytochrome P450 reductase, allosterically enhancing upstream CYP79B2, acting redundantly with its tandem paralog CYP71A12, and transcriptionally governed by the WRKY33 immune regulon. Its loss reduces pathogen-induced camalexin and compromises resistance to necrotrophic fungi. All retrieved evidence — biochemical, genetic, biophysical, and bioinformatic — converges on this function, with no gene-symbol ambiguity.


## Artifacts

- [OpenScientist final report](CYP71A13-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](CYP71A13-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:17573535
2. PMID:19523656
3. PMID:23073694
4. PMID:19263076
5. PMID:25953104
6. PMID:20348432
7. PMID:35191984
8. PMID:31511315
9. PMID:36319610
10. PMID:26379682
11. PMID:32279333
12. PMID:32082343
13. PMID:31749193
14. PMID:39628054
15. PMID:22852809
16. PMID:21239642
17. PMID:19567706