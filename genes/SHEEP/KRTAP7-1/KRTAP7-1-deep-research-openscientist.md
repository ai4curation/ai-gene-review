---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T17:27:41.905154'
end_time: '2026-10-24T18:18:37.589796'
duration_seconds: 3055.68
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: SHEEP
  gene_id: KRTAP7-1
  gene_symbol: KRTAP7-1
  uniprot_accession: Q28580
  protein_description: 'RecName: Full=Keratin-associated protein 7-1; AltName: Full=HGT
    keratin; AltName: Full=HGT-C2; AltName: Full=High glycine-tyrosine keratin-associated
    protein 7.1;'
  gene_info: Name=KRTAP7-1; Synonyms=HGTC2;
  organism_full: Ovis aries (Sheep).
  protein_family: Belongs to the KRTAP type 7 family. .
  protein_domains: KRTAP7. (IPR020184); KRTAP7 (PF15034)
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
citation_count: 9
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: KRTAP7-1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: KRTAP7-1-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q28580
- **Protein Description:** RecName: Full=Keratin-associated protein 7-1; AltName: Full=HGT keratin; AltName: Full=HGT-C2; AltName: Full=High glycine-tyrosine keratin-associated protein 7.1;
- **Gene Information:** Name=KRTAP7-1; Synonyms=HGTC2;
- **Organism (full):** Ovis aries (Sheep).
- **Protein Family:** Belongs to the KRTAP type 7 family. .
- **Key Domains:** KRTAP7. (IPR020184); KRTAP7 (PF15034)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "KRTAP7-1" matches the protein description above**
2. **Verify the organism is correct:** Ovis aries (Sheep).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'KRTAP7-1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **KRTAP7-1** (gene ID: KRTAP7-1, UniProt: Q28580) in SHEEP.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# KRTAP7-1 (Q28580) in Sheep: A Flexible High Glycine-Tyrosine Structural Matrix Protein of the Wool Orthocortex

## Summary

Sheep **KRTAP7-1** (UniProt **Q28580**; gene synonym *HGTC2*; also historically called "HGT keratin" and "HGT-C2") encodes a small 85-amino-acid protein belonging to the **high glycine-tyrosine (HGT) keratin-associated protein** class of the KRTAP type 7 family (InterPro IPR020184; Pfam PF15034). Its identity as a bona fide HGT-KAP of *Ovis aries* wool is firmly established: the protein is unambiguously assigned to the ovine KRTAP7-1 gene by the standardized KAP nomenclature, and its amino acid composition — rich in glycine (≈22%), tyrosine (≈12%), serine (≈14%) and phenylalanine (≈11%), with only five cysteine residues (≈6%) — is the diagnostic chemical signature of the HGT-KAP group. This report therefore addresses the correct target gene, and the retrieved literature maps cleanly onto the correct ovine protein rather than onto a same-symbol gene in a different organism.

The **primary function** of KRTAP7-1 is **structural, not catalytic**. It is not an enzyme, transporter, or signalling molecule. Instead, it is a component of the **interfilamentous matrix** of the wool cortex, where trichocyte (hair/wool) keratin intermediate filaments (IFs) are embedded in and cross-linked by keratin-associated proteins. KRTAP7-1 contributes a **flexible, glycine/tyrosine-rich, low-cysteine matrix element** that co-assembles with the keratin IF network. Because it carries only five cysteines, it participates minimally in the dense disulfide cross-linking that characterizes the high-sulfur KAPs, and instead is thought to confer flexibility and fill interfilament space via glycine/aromatic-rich low-complexity segments.

**Spatially and developmentally**, KRTAP7-1 acts **intracellularly within the terminally keratinized cortical cells of the wool shaft**, with a strong **bias toward the orthocortex** — the component of the bilateral wool fibre associated with crimp and curvature. HGT-KAPs including the KAP7 family are expressed relatively **late in follicle keratinization**, deposited on the orthocortical side of the differentiating fibre. The gene lies within a KAP cluster on **sheep chromosome 1**, and allelic variation in KRTAP7-1 is associated with **wool yield and mean staple length**, consistent with a genuine structural contribution to fibre formation and bulk properties.

---

## Key Findings

### Finding 1 — KRTAP7-1 is a bona fide high glycine-tyrosine keratin-associated protein of sheep wool

Direct composition analysis of the UniProt Q28580 sequence (85 residues) confirms the protein's membership in the HGT-KAP class. The sequence is 22.4% glycine, 14.1% serine, 11.8% tyrosine, and 10.6% phenylalanine, with only 5 cysteine residues (5.9%). The combined glycine + tyrosine content of 34.1% is the defining chemical signature of the high glycine-tyrosine KAP class, and the low cysteine content distinguishes it sharply from the high-sulfur and ultra-high-sulfur KAP groups. UniProt further annotates a tandem region spanning residues 37–82 consisting of "12 × 2 AA repeats of G-[YCGS]" — a glycine-dipeptide low-complexity architecture typical of HGT matrix proteins.

The gene **KRTAP7-1** carries the synonym *HGTC2* and the aliases "HGT keratin" / "HGT-C2," is classified in the **KRTAP type 7 family**, and bears the KRTAP7 domain (InterPro **IPR020184**, Pfam **PF15034**). Every identity check mandated by the research brief is satisfied: the gene symbol matches the protein description, the organism is sheep, and the domain/family assignment aligns with the HGT-KAP literature.

### Finding 2 — Primary function: a structural matrix protein embedding keratin intermediate filaments

The curated UniProt FUNCTION annotation for Q28580 states: *"In the wool cortex, wool keratin intermediate filaments are embedded in an interfilamentous matrix, consisting of hair keratin-associated proteins (KRTAP), which are essential for the form[ation]..."* The SUBUNIT annotation states the protein *"Interacts with wool keratins,"* and the TISSUE SPECIFICITY is simply *"Wool."*

Mechanistically, the KAP family to which KRTAP7-1 belongs forms the matrix that binds keratin IF bundles together. As stated for the family generally, *"KRTAPs form the interfilamentous matrix between intermediate filament bundles through extensive disulfide bond cross-linking with the numerous cysteine residues in hair keratins"* ([PMID: 29797267](https://pubmed.ncbi.nlm.nih.gov/29797267/)). Importantly, while high-sulfur KAPs drive this disulfide cross-linking directly, KRTAP7-1's low cysteine content (5 residues) means it contributes primarily as a **space-filling, flexible glycine/tyrosine-rich component** of this matrix rather than as a heavily disulfide-bonded cross-linker. Its tyrosine and phenylalanine residues may additionally engage in aromatic interactions and, potentially, tyrosine-based cross-links (e.g., isodityrosine) with neighbouring matrix and keratin chains, while its five dispersed cysteines permit limited disulfide tethering to cysteine-rich keratins and high-sulfur KAPs.

### Finding 3 — Localization: HGT-KAPs including KAP7 concentrate in the orthocortex

KRTAP7-1 carries out its function **intracellularly**, within the dead, fully keratinized cortical cells of the mature wool fibre, as part of the cytoplasmic keratin filament–matrix composite. The wool cortical cell population is bilaterally organized into **orthocortex** and **paracortex**, and the HGT-KAP class is spatially restricted. HGT-KAPs are *"predominantly present in the orthocortex of wool fibres"* ([PMID: 25782086](https://pubmed.ncbi.nlm.nih.gov/25782086/)). A proteomic comparison of crimp-mutant versus wild-type sheep wool specifically implicated the KAP7 family: straight (crimp-reduced) fibres showed *"the reduced abundance of some proteins in the high glycine-tyrosine class normally associated with the orthocortex, specifically the KAP6, KAP7, and KAP8 families"* ([PMID: 34859500](https://pubmed.ncbi.nlm.nih.gov/34859500/)).

This finding localizes KRTAP7-1 to a specific anatomical compartment of the fibre and ties its abundance to **fibre curvature/crimp** — a key functional trait. The orthocortex bias means KRTAP7-1 operates within the fibre domain that bends to the outside of the wool crimp, where a more flexible, less densely cross-linked matrix is physically appropriate.

### Finding 4 — Genomic context and phenotypic association

KRTAP7-1 resides in an ordered KAP gene cluster on **sheep chromosome 1**. The cluster order from the centromere is: *"KRTAP11-1, KRTAP7-1, KRTAP8-1, KRTAP6-2, KRTAP6-1, KRTAP13-3 and KRTAP24-1"* ([PMID: 25279319](https://pubmed.ncbi.nlm.nih.gov/25279319/)). This clustering of HGT and other KAP genes is a hallmark of the family's concerted evolution and coordinated expression.

Functionally, allelic variation in the gene has measurable phenotypic consequences. In a study of 222 Pakistani sheep, two coding-sequence variants (A and B) of KRTAP7-1 were found, and *"Variation in KRTAP7-1 was found to be associated with yield (P = 0.017)"* ([PMID: 31863114](https://pubmed.ncbi.nlm.nih.gov/31863114/)). The study reported wool yield of 79.9% for AA versus 81.9% for AB genotypes (P = 0.017), and mean staple length of 47.3 mm (AA) versus 50.9 mm (AB) (P = 0.024). These associations provide experimental genetic evidence that KRTAP7-1 sequence variation affects bulk wool traits, consistent with its structural role in fibre formation — with the caveat that linkage to neighbouring clustered KAPs cannot be entirely excluded.

| Trait | AA genotype | AB genotype | P value |
|-------|-------------|-------------|---------|
| Wool yield | 79.9% | 81.9% | 0.017 |
| Mean staple length | 47.3 mm | 50.9 mm | 0.024 |

### Finding 5 — Developmental expression: late, orthocortical-side deposition

HGT-KAPs are expressed with a distinct spatial and temporal pattern during follicle keratinization. In situ hybridization shows that *"proteins high in glycine and tyrosine tend to be expressed initially on the orthocortical side of the follicle"* ([PMID: 17697142](https://pubmed.ncbi.nlm.nih.gov/17697142/)), in contrast to the sulphur-rich proteins, which are first expressed on the paracortical side. This establishes the orthocortical, developmentally patterned expression of the glycine/tyrosine-rich KAP class that includes KRTAP7-1.

Timing is also informative. For the related glycine/tyrosine-rich KAP6 family, *"KAP6 expression starts relatively late in hair follicle differentiation"* ([PMID: 7680040](https://pubmed.ncbi.nlm.nih.gov/7680040/)), with transcripts localizing to the cells of the hair shaft cortex. By analogy and family membership, KRTAP7-1 is likewise deposited late in terminal cortical keratinization, after the keratin IF scaffold has begun to assemble — consistent with its role as a matrix "infill" around pre-formed filaments. KRTAP7-1 thereby participates in the biological process of **hair/wool fibre morphogenesis (keratinization)**, not a metabolic or signalling pathway.

### Finding 6 — Evolutionary and structural context

Glycine/tyrosine-rich KAP genes are under strong purifying selection, implying functional importance. Sheep and rabbit KAP6 genes share 89% nucleotide identity, *"suggesting that they are equivalent genes and indicating strong selection pressure during evolution"* ([PMID: 7680040](https://pubmed.ncbi.nlm.nih.gov/7680040/)). More broadly, the KRTAP gene family *"members present a typical pattern of concerted evolution, and its evolutionary features are consistent with the evolution of mammalian hair"* ([PMID: 29797267](https://pubmed.ncbi.nlm.nih.gov/29797267/)).

The structural biology of the filament–matrix composite in which KRTAP7-1 acts is well characterized. Trichocyte keratin IFs assemble in the reducing environment at the base of the follicle and are subsequently oxidized and cross-linked in the mature fibre: *"hair keratin can adopt not one but two structurally-distinct conformations, one formed in the living cells at the base of the hair follicle in a reducing environment and the second in the fully differentiated hair in dead cells in an oxidized state"* ([PMID: 29797268](https://pubmed.ncbi.nlm.nih.gov/29797268/)). KRTAP7-1 is deposited and incorporated within this maturing composite. Because it carries only 5 cysteines (5.9%), it contributes mainly a flexible glycine-rich, tyrosine-bearing matrix component rather than a heavily disulfide-crosslinked one.

### Finding 7 — Molecular architecture and formal classification

The full UniProt FUNCTION annotation places the protein within the chemically defined matrix: *"In the wool cortex, wool keratin intermediate filaments are embedded in an interfilamentous matrix, consisting of hair keratin-associated proteins (KRTAP)...The matrix proteins include the high-sulfur and high-glycine-tyrosine keratins."* Direct sequence analysis of the 85-aa protein reveals tyrosines at 10 positions (10, 14, 17, 42, 47, 52, 66, 71, 82, 85), 9 phenylalanines, and only 5 cysteines (positions 6, 7, 32, 44, 64); the region spanning residues 37–82 is a glycine/aromatic-rich low-complexity stretch with repeated GY/YG/GG/GF dipeptides (6 GY + 4 YG motifs).

The KAP family is formally divided into three structural classes: *"KAPs can be divided into three groups: the high sulphur (HS) KAPs, the ultra-high sulphur (UHS) KAPs and the high glycine-tyrosine (HGT) KAPs"* ([PMID: 25279319](https://pubmed.ncbi.nlm.nih.gov/25279319/)), with KAP7 placed in the HGT group. The standardized nomenclature confirms the gene's identity: *"GenBank sequence JN091630 would historically have been named KRTAP7-1 for the gene"* ([PMID: 22298953](https://pubmed.ncbi.nlm.nih.gov/22298953/)).

---

## Mechanistic Model / Interpretation

KRTAP7-1 is best understood as one of the molecular "mortar" components in the brick-and-mortar architecture of the wool cortical cell, where keratin intermediate filaments are the "bricks" and the keratin-associated protein matrix is the "mortar."

```
WOOL FIBRE  →  CORTEX  →  (bilateral: ORTHOCORTEX | PARACORTEX)
                                  │
                                  ▼
          Orthocortical cortical cell (terminally keratinized, dead)
                                  │
   ┌──────────────────────────────────────────────────────────┐
   │   Trichocyte keratin INTERMEDIATE FILAMENTS (type I/II)    │
   │   ████████  ████████  ████████  ████████  (the "bricks")   │
   │      ▲          ▲          ▲          ▲                     │
   │      │          │          │          │                     │
   │   INTERFILAMENTOUS MATRIX  (the "mortar")                   │
   │   - High-sulfur KAPs  → dense disulfide cross-linking       │
   │   - HGT-KAPs (KRTAP7-1) → flexible Gly/Tyr-rich infill ◄────┤
   │       • 85 aa, Gly 22%, Tyr 12%, Cys only 6%               │
   │       • low-complexity GY/YG repeats (res 37–82)           │
   │       • minimal disulfide bonding → flexibility            │
   └──────────────────────────────────────────────────────────┘
```

**Why the orthocortex?** The orthocortex forms the convex (outer) side of the crimp wave in fine wool. A matrix enriched in flexible, low-cysteine HGT-KAPs such as KRTAP7-1 is mechanically consistent with this domain, whereas the paracortex is enriched in rigid, heavily cross-linked high-sulfur KAPs. The observation that KAP7 abundance falls in crimp-reduced (straight) fibres ([PMID: 34859500](https://pubmed.ncbi.nlm.nih.gov/34859500/)) directly links KRTAP7-1 content to the orthocortex/paracortex balance that generates curvature.

**Temporal logic.** The keratin IF scaffold assembles first in the reducing follicular environment; HGT-KAPs are deposited later, on the orthocortical side, as the cell terminally keratinizes ([PMID: 17697142](https://pubmed.ncbi.nlm.nih.gov/17697142/); [PMID: 7680040](https://pubmed.ncbi.nlm.nih.gov/7680040/)). The matrix is then locked into an oxidized, cross-linked state in the mature, dead fibre ([PMID: 29797268](https://pubmed.ncbi.nlm.nih.gov/29797268/)). KRTAP7-1 thus performs its structural function **after** synthesis, as a permanent architectural element of the dead fibre rather than as an active participant in a signalling or metabolic pathway.

**Pathway context.** KRTAP7-1 does not operate in a biochemical signalling cascade. Its "pathway" is the **hair/wool keratinization and fibre-assembly program**: coordinated expression of trichocyte keratins and KAPs within the differentiating cortical cell, culminating in the IF–matrix composite. Its contribution is physical/structural, and its measurable phenotypic footprint (wool yield, staple length, crimp) arises from this structural role.

| Property | KRTAP7-1 (HGT-KAP) | High-sulfur KAPs (contrast) |
|----------|--------------------|-----------------------------|
| Class | High glycine-tyrosine (HGT) | High-/ultra-high-sulfur (HS/UHS) |
| Cysteine content | Low (~6%, 5 residues) | High to very high |
| Dominant role | Flexible matrix infill | Dense disulfide cross-linking |
| Cortical bias | Orthocortex | Paracortex (relative) |
| Mechanical contribution | Flexibility / crimp | Rigidity / hardness |

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the findings |
|------|-----------------|------------------------------|
| [22298953](https://pubmed.ncbi.nlm.nih.gov/22298953/) | *An updated nomenclature for KAPs* | Formally assigns the KRTAP7-1 name to the ovine gene (GenBank JN091630), confirming target identity |
| [25279319](https://pubmed.ncbi.nlm.nih.gov/25279319/) | *The sheep KAP8-2 gene...* | Defines the three KAP classes (HS/UHS/HGT), places KAP7 in HGT, and gives the chromosome-1 cluster order including KRTAP7-1 |
| [29797267](https://pubmed.ncbi.nlm.nih.gov/29797267/) | *Evolution of Trichocyte KAPs* | States the family mechanistic role (interfilamentous matrix via cross-linking) and concerted evolution |
| [29797268](https://pubmed.ncbi.nlm.nih.gov/29797268/) | *Structural Hierarchy of Trichocyte Keratin IFs* | Provides the reducing-follicle vs oxidized-fibre structural context for matrix deposition |
| [25782086](https://pubmed.ncbi.nlm.nih.gov/25782086/) | *A 57-bp deletion in ovine KAP6-1...* | Localizes HGT-KAPs predominantly to the orthocortex |
| [34859500](https://pubmed.ncbi.nlm.nih.gov/34859500/) | *Wool fibre curvature... keratin-associated proteins* | Names the KAP7 family specifically as orthocortex-associated and curvature-linked |
| [31863114](https://pubmed.ncbi.nlm.nih.gov/31863114/) | *Polymorphism in ovine KRTAP7-1...* | Direct genetic association of KRTAP7-1 variation with wool yield and staple length |
| [17697142](https://pubmed.ncbi.nlm.nih.gov/17697142/) | *Differential expression of proteins in cortical cells* | Establishes orthocortical-side expression of Gly/Tyr-rich KAPs |
| [7680040](https://pubmed.ncbi.nlm.nih.gov/7680040/) | *Sequence, expression, evolution of a Gly/Tyr-rich KAP* | Late cortical expression and strong evolutionary conservation of HGT-KAPs |

The evidence is internally consistent and mutually reinforcing. Composition analysis of the Q28580 sequence (Findings 1 and 7) anchors the chemical identity; the nomenclature paper ([PMID: 22298953](https://pubmed.ncbi.nlm.nih.gov/22298953/)) anchors the genetic identity; functional and localization claims (Findings 2–3, 5) are supported by family-level and class-level studies; and the genetic association study ([PMID: 31863114](https://pubmed.ncbi.nlm.nih.gov/31863114/)) provides gene-specific phenotypic evidence. No retrieved paper contradicts the structural-matrix interpretation.

---

## Supported and Refuted Hypotheses

**Supported:**
- KRTAP7-1 is a high glycine-tyrosine keratin-associated protein (confirmed by composition: 34.1% Gly+Tyr, 5.9% Cys).
- Its primary role is a structural interfilamentous matrix protein that binds/crosslinks keratin IFs (UniProt; [PMID: 29797267](https://pubmed.ncbi.nlm.nih.gov/29797267/)).
- It localizes intracellularly in cortical cells, biased to the orthocortex ([PMID: 25782086](https://pubmed.ncbi.nlm.nih.gov/25782086/); [PMID: 34859500](https://pubmed.ncbi.nlm.nih.gov/34859500/)).
- It is deposited late in cortical keratinization with an orthocortical expression bias ([PMID: 17697142](https://pubmed.ncbi.nlm.nih.gov/17697142/); [PMID: 7680040](https://pubmed.ncbi.nlm.nih.gov/7680040/)).
- Allelic variation affects wool production traits ([PMID: 31863114](https://pubmed.ncbi.nlm.nih.gov/31863114/)).

**Refuted / ruled out:**
- KRTAP7-1 is **not** an enzyme, transporter, or signalling protein — no catalytic, transport, or signalling domains; family/structure are purely structural.
- It is **not** a rigid high-sulfur crosslinker — its low cysteine content precludes the dense disulfide network characteristic of HS/UHS KAPs.

---

## Limitations and Knowledge Gaps

1. **No KRTAP7-1-specific functional assay.** The mechanistic role (matrix infill, keratin binding) is inferred from UniProt annotation and from family/class-level studies (KAP6, KAP7, KAP8, general KRTAP biology), not from a biochemical or knockout experiment on KRTAP7-1 itself. There is no direct structural determination (X-ray/NMR/cryo-EM) of KRTAP7-1 within the matrix.

2. **Localization is at the class level.** The orthocortex bias is demonstrated for the HGT-KAP class and the KAP7 *family* ([PMID: 34859500](https://pubmed.ncbi.nlm.nih.gov/34859500/)), not by immunolocalization of the KRTAP7-1 protein specifically.

3. **Developmental timing is inferred by analogy.** The "late, orthocortical-side" expression pattern is best documented for KAP6 and the HGT class generally ([PMID: 7680040](https://pubmed.ncbi.nlm.nih.gov/7680040/); [PMID: 17697142](https://pubmed.ncbi.nlm.nih.gov/17697142/)); a KRTAP7-1-specific in situ hybridization timeline was not located.

4. **Phenotypic association is from a single modest cohort.** The yield/staple-length associations come from 222 Pakistani sheep ([PMID: 31863114](https://pubmed.ncbi.nlm.nih.gov/31863114/)) with nominal (unadjusted-for-multiple-testing) P values near 0.02; replication in independent breeds is needed, and linkage to neighbouring clustered KRTAPs cannot be fully excluded.

5. **Cross-linking chemistry of HGT-KAPs is incompletely defined.** Whether KRTAP7-1's tyrosines participate in specific isodityrosine or di-tyrosine cross-links, or purely in non-covalent aromatic/hydrophobic packing, remains unresolved.

---

## Proposed Follow-up Experiments / Actions

1. **KRTAP7-1-specific immunolocalization.** Raise an antibody to a KRTAP7-1-unique epitope and perform immunohistochemistry across the ortho-/paracortex boundary to confirm the predicted orthocortical bias at the protein level.

2. **Quantitative proteomics by genotype.** Correlate KRTAP7-1 protein abundance (targeted MS/MRM) with the A/B genotypes and with crimp/curvature and staple-length measurements in a larger, multi-breed cohort to test whether the genetic association ([PMID: 31863114](https://pubmed.ncbi.nlm.nih.gov/31863114/)) is mediated by protein dosage.

3. **In situ hybridization time-course.** Map KRTAP7-1 transcript appearance relative to trichocyte keratins and high-sulfur KAPs within the follicle to confirm late, orthocortical-side deposition specifically for this gene.

4. **Structural/biophysical characterization.** Use AlphaFold/structure prediction plus solid-state NMR or synchrotron diffraction on reconstituted keratin–KAP composites to test the "flexible infill" model and probe tyrosine-mediated interactions and isodityrosine cross-links.

5. **Cross-species comparative analysis.** Extend the evolutionary analysis of KRTAP7-1 orthologues across wool/hair species to quantify selection on the glycine/tyrosine low-complexity region and test for coevolution with keratin IF partners.

6. **Breeding/marker validation.** Evaluate KRTAP7-1 variants as candidate markers for marker-assisted selection on wool yield and staple length, independently of the neighbouring clustered KRTAPs.

---

## Conclusion

Sheep KRTAP7-1 is a conserved, orthocortex-biased, high glycine-tyrosine keratin-associated protein that functions as a flexible structural component of the interfilamentous matrix of the wool cortex, embedding and crosslinking trichocyte keratin intermediate filaments during fibre keratinization, with allelic variation influencing wool yield and staple length.

---

*Report prepared from 7 confirmed findings and 26 reviewed papers. All functional claims are attributed to the cited literature or to direct composition analysis of UniProt sequence Q28580. Identity verification per the research brief is complete: the target is confirmed to be ovine KRTAP7-1 (HGTC2), a high glycine-tyrosine keratin-associated protein, not a same-symbol gene in another organism.*


## Artifacts

- [OpenScientist final report](KRTAP7-1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](KRTAP7-1-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:29797267
2. PMID:25782086
3. PMID:34859500
4. PMID:25279319
5. PMID:31863114
6. PMID:17697142
7. PMID:7680040
8. PMID:29797268
9. PMID:22298953