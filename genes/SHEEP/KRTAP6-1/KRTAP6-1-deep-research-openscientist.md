---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T17:27:41.880336'
end_time: '2026-10-24T17:52:12.358667'
duration_seconds: 1470.48
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: SHEEP
  gene_id: KRTAP6-1
  gene_symbol: KRTAP6-1
  uniprot_accession: Q02958
  protein_description: 'RecName: Full=Keratin-associated protein 6-1; AltName: Full=Keratin,
    glycine/tyrosine-rich of hair;'
  gene_info: Name=KRTAP6-1; Synonyms=KAP6-1;
  organism_full: Ovis aries (Sheep).
  protein_family: Belongs to the KRTAP type 6 family. .
  protein_domains: KAP6. (IPR040313)
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
  path: KRTAP6-1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: KRTAP6-1-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q02958
- **Protein Description:** RecName: Full=Keratin-associated protein 6-1; AltName: Full=Keratin, glycine/tyrosine-rich of hair;
- **Gene Information:** Name=KRTAP6-1; Synonyms=KAP6-1;
- **Organism (full):** Ovis aries (Sheep).
- **Protein Family:** Belongs to the KRTAP type 6 family. .
- **Key Domains:** KAP6. (IPR040313)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "KRTAP6-1" matches the protein description above**
2. **Verify the organism is correct:** Ovis aries (Sheep).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'KRTAP6-1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **KRTAP6-1** (gene ID: KRTAP6-1, UniProt: Q02958) in SHEEP.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# KRTAP6-1 (Q02958) in Sheep — Functional Annotation Report

**Gene:** KRTAP6-1 (synonym KAP6-1)
**Protein:** Keratin-associated protein 6-1 (Keratin, glycine/tyrosine-rich of hair)
**UniProt:** Q02958
**Organism:** *Ovis aries* (sheep)
**Family:** KRTAP type 6 family; high glycine–tyrosine keratin-associated protein (HGT-KAP); InterPro IPR040313 (KAP6)
**Report date:** 2026-10-24

---

## Summary

Sheep **KRTAP6-1** encodes a small (83 amino acid), strongly basic, glycine/tyrosine-rich **high glycine–tyrosine keratin-associated protein (HGT-KAP)**. It is **not an enzyme, transporter, or signalling molecule**. Its primary function is **architectural/structural**: it is a component of the **interfilament matrix** of the wool/hair fibre, the amorphous protein phase that embeds, surrounds, and cross-links the hair keratin **intermediate filaments (IFs)**. In doing so, KRTAP6-1 helps convert bundles of keratin IFs into a rigid, mechanically robust **filament–matrix composite**. This research target was verified against the UniProt identity: the gene symbol, organism (sheep), protein family (KAP type 6), and glycine/tyrosine-rich composition are all internally consistent with the literature, and the findings below pertain specifically to the correct ovine protein.

Direct analysis of the Q02958 protein sequence confirms its HGT-KAP identity: glycine 37.3% and tyrosine 21.7% give a **combined Gly+Tyr content of 59%**, closely matching the ~60% reported for the closely related goat KAP6-1 homologues. The protein has essentially **no acidic residues** (Asp+Glu = 0) and four arginines, producing a **strongly basic, high-isoelectric-point protein**, and it retains **nine cysteines** that enable **disulfide cross-linking** to the cysteine-rich hair keratins. Structural prediction reinforces this picture: the AlphaFold model of Q02958 is **fully intrinsically disordered** (mean pLDDT 37.4; 100% of residues below the low-confidence threshold of 50), consistent with a pliable matrix "glue" rather than a folded catalytic domain, and with the experimental observation that recombinant KAP6.1 is insoluble and aggregation-prone in isolation.

Functionally and anatomically, KRTAP6-1 is synthesised in the **cytoplasm of differentiating cortical trichocytes** late in wool-follicle keratinisation and is deposited predominantly in the **orthocortex** of the wool fibre. Its abundance and sequence variation have measurable consequences for fibre properties: a 57-bp (19-amino-acid) deletion allele is associated with **coarser, more variable wool**, and the abundance of KAP6-family HGT-KAPs in the orthocortex is correlated with **wool fibre curvature (crimp)**. The protein therefore acts as a structural "tuning" element of the cortical matrix that helps set the final physical phenotype of the wool fibre.

---

## Key Findings

### Finding 1 — KRTAP6-1 encodes a high glycine–tyrosine keratin-associated protein (HGT-KAP) of the wool/hair fibre matrix

UniProt Q02958 annotates KRTAP6-1 (KAP6-1) as "Keratin-associated protein 6-1 / Keratin, glycine/tyrosine-rich of hair," placing it in the KAP type 6 family (InterPro IPR040313). This family classification is the backbone of the protein's functional identity. Keratin-associated proteins are divided into three biochemical classes — the **high-sulphur (HS)**, **ultra-high-sulphur (UHS)**, and **high glycine–tyrosine (HGT)** KAPs — and KAP6 belongs to the HGT class ([PMID: 25279319](https://pubmed.ncbi.nlm.nih.gov/25279319/)).

The HGT identity is grounded in composition and localization. Ovine HGT-KAPs, including KAP6-1, are predominantly present in the **orthocortex** of wool fibres ([PMID: 25782086](https://pubmed.ncbi.nlm.nih.gov/25782086/), *"High glycine-tyrosine keratin-associated proteins (HGT-KAPs) are predominantly present in the orthocortex of wool fibres"*). Independent sequence evidence from the closely related goat KAP6-1 homologues — six basic proteins of 71–84 amino acids with a **combined glycine and tyrosine content of about 60%** ([PMID: 15478612](https://pubmed.ncbi.nlm.nih.gov/15478612/)) — establishes the small, basic, glycine/tyrosine-rich composition that is the hallmark of this family. Together these data firmly identify KRTAP6-1 as an HGT-KAP whose site of action is the wool-fibre cortex.

### Finding 2 — KAP6-1 functions as an interfilament matrix protein that cross-links hair keratin intermediate filaments

The mechanistic role of KRTAPs is to form the **interfilamentous matrix** between keratin IF bundles through **extensive disulfide bond cross-linking** with the numerous cysteine residues in hair keratins ([PMID: 29797267](https://pubmed.ncbi.nlm.nih.gov/29797267/), *"KRTAPs form the interfilamentous matrix between intermediate filament bundles through extensive disulfide bond cross-linking with the numerous cysteine residues in hair keratins"*). This is the defining structural function of the family and applies to KAP6.

Biochemical work confirms that KAPs are the **major constituent of the matrix** between hair keratin IFs and that they **stabilise hair structure by extensive disulfide bonding**; crucially, **KAP6.1 specifically** was expressed and purified as a cysteine-containing, aggregation-prone protein in this study ([PMID: 29391282](https://pubmed.ncbi.nlm.nih.gov/29391282/), *"KAPs are the major constituent of the matrix between the hair keratin intermediate filaments (IFs), and stabilise hair structure by extensive disulfide bonding"*). At the structural level, trichocyte keratin is understood as a **filament–matrix composite** ([PMID: 29797268](https://pubmed.ncbi.nlm.nih.gov/29797268/)), in which keratin IFs provide the filamentous phase and KAPs such as KAP6-1 provide the embedding, cross-linking matrix phase. The precise role of KRTAP6-1 is therefore that of a **structural adapter/cross-linker** — it has no catalytic activity; its "substrate" is the keratin IF, which it binds and cross-links via disulfide bonds.

### Finding 3 — KRTAP6-1 is expressed in cortical cells late in follicle differentiation, and its variation affects wool fibre diameter

In situ hybridisation localizes KRTAP6-1 expression to the **upper follicle keratogenous zone**, temporally **later** than keratins and trichohyalin, and specifically to **cortical cells forming the brush-end anchoring structure** of the fibre ([PMID: 19272529](https://pubmed.ncbi.nlm.nih.gov/19272529/), *"Some genes (KRT27, KRT31, KRT85 and KRTAP6-1), but not others, were expressed in cortical cells forming the brush-end"*). This expression pattern — late, cortical, and cytoplasmic — is exactly what is expected of a matrix protein deposited after the keratin IF scaffold is laid down.

The functional consequence of this structural role is visible at the whole-fibre level. A **57-bp deletion (loss of 19 amino acids), variant C**, of ovine KRTAP6-1 is associated with **increased mean fibre diameter, fibre diameter standard deviation, coefficient of variation of fibre diameter, and prickle factor** ([PMID: 25782086](https://pubmed.ncbi.nlm.nih.gov/25782086/), *"The results suggest that variation in ovine KRTAP6-1 affects wool fibre diameter-associated traits and that the 57-bp deletion in this gene would lead to coarser wool"*). This genotype–phenotype link is corroborated at the locus level: the KRTAP6/KRTAP8 gene cluster showed **linkage to wool fibre diameter** in a Merino half-sib family ([PMID: 7516629](https://pubmed.ncbi.nlm.nih.gov/7516629/)). Reducing the matrix protein's length changes the properties of the matrix it builds, and this propagates to the measurable coarseness and uniformity of the wool.

### Finding 4 — The Q02958 sequence confirms HGT-KAP identity: 59% Gly+Tyr, strongly basic, nine cysteines for cross-linking

Direct computational analysis of the 83-amino-acid UniProt Q02958 sequence provides quantitative confirmation of the protein's class and functional features:

| Property | Value (Q02958) | Interpretation |
|---|---|---|
| Length | 83 aa | Small matrix protein |
| Glycine | 37.3% (31 residues) | Flexibility / low-complexity |
| Tyrosine | 21.7% (18 residues) | HGT-KAP hallmark |
| **Gly + Tyr combined** | **59.0%** | Matches ~60% HGT-KAP definition |
| Serine | 14.5% | Low-complexity repeats |
| Cysteine | 10.8% (9 residues) | Disulfide cross-linking |
| Acidic (Asp+Glu) | 0 | Strongly basic, high pI |
| Arginine | 4 | Contributes to high pI |
| Repetitive motifs | GYG (×8), GCGY (×3), CGSGYG (×3) | Low-complexity, repetitive |

The measured **59% Gly+Tyr** content matches the ~60% reported for the goat KAP6-1 homologues ([PMID: 15478612](https://pubmed.ncbi.nlm.nih.gov/15478612/), *"with a combined glycine and tyrosine content of about 60%"*), while the complete absence of acidic residues and the presence of four arginines explain the **strongly basic, high isoelectric point** character typical of HGT-KAPs ([PMID: 29391282](https://pubmed.ncbi.nlm.nih.gov/29391282/), *"with high isoelectric points"*). The nine cysteines, despite the protein being dominated by glycine and tyrosine, provide the chemical handles for the disulfide cross-linking to hair keratins described in Finding 2. The low-complexity, repetitive sequence (GYG, GCGY, CGSGYG motifs) is characteristic of a flexible, non-globular protein.

### Finding 5 — KAP6-family abundance in the orthocortex is associated with wool fibre curvature (crimp)

Proteomic and structural comparison of straight (crimp-mutant) versus wild-type crimpy wool, using **matched twin pairs** to control for fibre-diameter variability, revealed that straight fibres had a **fragmented/annular orthocortex** and a **reduced abundance of HGT-class KAP6, KAP7, and KAP8 proteins** normally associated with the orthocortex, along with lower type I keratin K38, while KAP16/KAP19 increased ([PMID: 34859500](https://pubmed.ncbi.nlm.nih.gov/34859500/), *"Crimp mutant fibers were noted for the reduced abundance of some proteins in the high glycine-tyrosine class normally associated with the orthocortex, specifically the KAP6, KAP7, and KAP8 families"*).

Because HGT-KAPs including KAP6-1 are **predominantly present in the orthocortex** ([PMID: 25782086](https://pubmed.ncbi.nlm.nih.gov/25782086/)), this result directly ties the amount of KAP6-family matrix protein in the orthocortex to the **macroscopic curvature (crimp)** of the wool fibre. The orthocortex–paracortex bilateral asymmetry is the classical structural basis of crimp, and the finding indicates that KAP6 matrix abundance is part of the molecular machinery that generates the differential properties producing curvature. This elevates KRTAP6-1 from a generic "filler" to a quantitative determinant of a specific, economically important fibre trait.

### Finding 6 — AlphaFold predicts Q02958 is fully intrinsically disordered, consistent with a flexible matrix protein

The AlphaFold DB model AF-Q02958-F1 (v6, 83 residues) has a **mean per-residue confidence pLDDT of 37.4** (range 30.2–49.0). **100% of residues fall below pLDDT 50**, and none exceed 70 — i.e., no secondary-structure-rich, high-confidence folded core is predicted anywhere in the protein. This is the signature of an **intrinsically disordered protein (IDP)**, not a folded enzyme or structured binding domain.

This prediction is fully consistent with the experimental behaviour of the protein: KAPs, including recombinant **KAP6.1**, are **insoluble in isolation and prone to forming aggregates in solution** ([PMID: 29391282](https://pubmed.ncbi.nlm.nih.gov/29391282/), *"they tend to be insoluble in isolation and are prone to forming aggregates in solution"*). An intrinsically disordered, glycine-rich chain is ideally suited to act as a conformable "glue" that fills the irregular spaces between keratin IFs and adopts its functional conformation only upon cross-linking and incorporation into the matrix, rather than existing as a stable, soluble, folded protein. The lack of a stable fold also explains why detailed atomic-resolution structural information on KAP–IF interactions remains lacking.

---

## Mechanistic Model / Interpretation

KRTAP6-1 is best understood as one structural building block in the hierarchical assembly of the wool fibre. The following model integrates the six findings:

```
   WOOL FOLLICLE (cortical trichocyte, late differentiation)
   ──────────────────────────────────────────────────────────
   1. Hair keratin IF proteins assemble first  ──►  keratin
      (type I + type II heterodimers)                intermediate
                                                      filaments (IFs)
                                                          │
   2. KRTAP6-1 synthesised LATE in cytoplasm             │
      (upper keratogenous zone; cortical cells)          ▼
      - 83 aa, 59% Gly+Tyr, 0 acidic, basic        ┌──────────────┐
      - intrinsically disordered (pLDDT 37)        │ IF  IF  IF   │
      - 9 cysteines                                │  ░░░░░░░░░░   │ ← KAP6-1 fills
                                                    │ IF  IF  IF   │   interfilament
   3. Disulfide cross-linking (−S−S−) between      │  ░░░░░░░░░░   │   MATRIX
      KAP6-1 cysteines and keratin cysteines       │ IF  IF  IF   │
                                                    └──────────────┘
                                                     FILAMENT–MATRIX
                                                       COMPOSITE
                                                          │
   4. Deposited predominantly in ORTHOCORTEX  ──►  bilateral ortho/para
                                                    asymmetry → CRIMP
                                                          │
   5. Final fibre physical properties:           ──►  diameter, variability,
      abundance/variants tune the matrix               curvature (crimp),
                                                        prickle factor
```

**Primary function (direct answer to the research question).** KRTAP6-1 is a **structural matrix protein**, not an enzyme, transporter, or signalling molecule. It catalyses no reaction and transports no substrate. Its "action" is to bind and **disulfide-cross-link hair keratin intermediate filaments** via its nine cysteines, forming the amorphous interfilament matrix of the fibre cortex (Findings 2, 4). Although KAP6 is dominated by glycine and tyrosine rather than cysteine, these retained cysteines are the functional cross-linking residues; the glycine/tyrosine-rich, intrinsically disordered backbone provides a flexible, space-filling scaffold (Findings 4, 6).

**Subcellular/anatomical localization.** The protein functions **intracellularly** within terminally differentiating cortical trichocytes, where it is deposited into the cytoplasmic matrix surrounding keratin IFs. At the tissue scale it is concentrated in the **orthocortex** of the wool-fibre cortex (Findings 1, 3, 5). In the mature, dead, cornified fibre it is an integral, cross-linked component of the cortical matrix rather than a free protein.

**Pathway context.** KRTAP6-1 does not participate in a signalling or metabolic pathway in the enzymatic sense. Its "pathway" is the **trichocyte keratinisation / hair-fibre assembly program**: it acts downstream of keratin IF assembly and trichohyalin, being expressed late in the keratogenous zone, and its incorporation into the disulfide-bonded matrix is the terminal structural step that fixes the fibre's mechanical architecture (Findings 2, 3).

**Phenotypic output.** By setting the quantity and quality of cortical matrix, KRTAP6-1 helps determine macroscopic fibre traits. A 19-amino-acid deletion allele produces **coarser, more variable wool**, and KAP6-family orthocortex abundance correlates with **crimp** (Findings 3, 5). These are precise, mechanistically interpretable phenotypes — not vague pleiotropy — because they flow directly from the protein's role as a matrix cross-linker that is asymmetrically distributed across the cortex.

---

## Evidence Base

| PMID | Paper (abbreviated) | How it supports the findings |
|---|---|---|
| [25782086](https://pubmed.ncbi.nlm.nih.gov/25782086/) | *A 57-bp deletion in the ovine KAP6-1 gene affects wool fibre diameter* | Primary ovine KRTAP6-1 study: establishes orthocortex localization of HGT-KAPs and links a 57-bp/19-aa deletion to coarser, more variable wool (Findings 1, 3, 5). |
| [29391282](https://pubmed.ncbi.nlm.nih.gov/29391282/) | *Expression and purification of HS and HGT KAPs...* | Biochemical study that specifically worked with KAP6.1; documents matrix cross-linking role, high pI, and insolubility/aggregation of recombinant protein (Findings 2, 4, 6). |
| [29797267](https://pubmed.ncbi.nlm.nih.gov/29797267/) | *Evolution of Trichocyte Keratin Associated Proteins* | States the defining mechanism: KRTAPs form the interfilament matrix via disulfide cross-linking to keratin cysteines (Finding 2). |
| [29797268](https://pubmed.ncbi.nlm.nih.gov/29797268/) | *Structural Hierarchy of Trichocyte Keratin Intermediate Filaments* | Frames trichocyte keratin as a filament–matrix composite, the structural context for KAP6-1's role (Finding 2). |
| [19272529](https://pubmed.ncbi.nlm.nih.gov/19272529/) | *Expression patterns of keratin IF and KAP genes in wool follicles* | In situ localization of KRTAP6-1 to cortical cells / brush-end, late in differentiation (Finding 3). |
| [15478612](https://pubmed.ncbi.nlm.nih.gov/15478612/) | *Cloning... six full-length cDNA similar to sheep KAP6-1 from cashmere goat* | Independent sequence data showing ~60% Gly+Tyr, small basic proteins — confirms composition of Q02958 (Findings 1, 4). |
| [34859500](https://pubmed.ncbi.nlm.nih.gov/34859500/) | *Wool fiber curvature correlated with abundance of K38 and specific KAPs* | Twin-controlled proteomics tying orthocortex KAP6 abundance to crimp (Finding 5). |
| [7516629](https://pubmed.ncbi.nlm.nih.gov/7516629/) | *Evidence of linkage between HGT keratin gene loci and wool fibre diameter* | Genetic linkage of the KRTAP6/8 cluster to fibre diameter (Finding 3). |
| [25279319](https://pubmed.ncbi.nlm.nih.gov/25279319/) | *The sheep KAP8-2 gene...* | Classifies KAPs into HS/UHS/HGT groups and maps the KRTAP6 cluster on sheep chromosome 1 (Finding 1, genomic context). |

**AlphaFold DB** model AF-Q02958-F1 (v6) provided the structural-disorder evidence for Finding 6 (mean pLDDT 37.4; 100% of residues < 50).

All attributions above are based on the verified citation snippets and abstracts in the knowledge outline; claims are not inferred from paper titles alone.

---

## Limitations and Knowledge Gaps

1. **No high-resolution structure of KAP6-1 in situ.** The functional model rests on the general KAP matrix paradigm plus an AlphaFold disorder prediction. There is no experimental atomic structure of KAP6-1 bound to keratin IFs, and detailed KAP–IF interaction geometry remains unknown. The intrinsic disorder of the protein makes conventional crystallography/NMR intractable.

2. **Cross-linking inferred, not directly mapped for KAP6-1.** The disulfide cross-linking role is established for the KAP class and the presence of nine cysteines is confirmed from the Q02958 sequence, but the specific keratin partners and disulfide topology of KAP6-1 have not been directly mapped in the fibre.

3. **Genotype–phenotype associations are correlational.** The 57-bp deletion association with coarser wool ([PMID: 25782086](https://pubmed.ncbi.nlm.nih.gov/25782086/)) and the crimp correlation ([PMID: 34859500](https://pubmed.ncbi.nlm.nih.gov/34859500/)) are statistical associations from candidate-gene and proteomic studies, not causal gene-knockout experiments. KRTAP genes are clustered, so linkage to neighbouring KRTAPs is a potential confounder (though some studies statistically adjusted for nearby loci).

4. **Reliance on homologues for some composition data.** Part of the compositional evidence derives from goat KAP6-1 homologues ([PMID: 15478612](https://pubmed.ncbi.nlm.nih.gov/15478612/)); while the direct Q02958 sequence analysis (59% Gly+Tyr) corroborates this, species-specific differences in exact partners cannot be excluded.

5. **Quantitative contribution unresolved.** KAP6-1 is one of many KAPs in a large chromosome-1 cluster. Its individual, isolated contribution to fibre mechanics relative to other KAP6 members and other HGT-KAP families (KAP7, KAP8, KAP20) is not precisely partitioned.

---

## Proposed Follow-up Experiments / Actions

1. **Targeted gene editing in sheep or a model system.** CRISPR knockout or allele-swap (wild-type vs 57-bp deletion) of KRTAP6-1 to establish causality for the coarse-wool and crimp phenotypes, decoupling it from linked KRTAPs.

2. **Crosslink mass spectrometry of the fibre cortex.** Use disulfide-mapping / XL-MS on isolated wool cortex to identify the specific keratin cysteine partners of KAP6-1 and quantify its cross-link density in ortho- vs paracortex.

3. **Quantitative spatial proteomics of ortho- vs paracortex.** Laser-capture or microdissection coupled to MS to measure absolute KAP6-1 abundance across the bilateral cortex and correlate with local curvature, extending [PMID: 34859500](https://pubmed.ncbi.nlm.nih.gov/34859500/).

4. **Biophysical reconstitution.** In vitro co-assembly of recombinant KAP6.1 (building on [PMID: 29391282](https://pubmed.ncbi.nlm.nih.gov/29391282/)) with hair keratins under oxidising conditions to test matrix formation, measure mechanical contribution, and probe disorder-to-order transitions by circular dichroism / SAXS.

5. **Population-scale association and selection studies.** Genotype KRTAP6-1 variants across diverse sheep breeds to refine effect sizes on diameter, CV, prickle factor, and crimp, and assess value for marker-assisted selection in wool breeding programs.

6. **Comparative evolutionary analysis.** Characterise KAP6-1 orthologues across wool/hair-producing species to relate conservation of the Gly/Tyr/Cys pattern to fibre properties, strengthening structure–function inference.

---

*Report compiled from six confirmed findings and 24 reviewed papers over five discovery iterations. Target identity (UniProt Q02958, KRTAP6-1, Ovis aries, KAP type 6 / HGT-KAP family) was verified as consistent across gene symbol, organism, protein family, domain annotation, and literature before and throughout the investigation.*


## Artifacts

- [OpenScientist final report](KRTAP6-1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](KRTAP6-1-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:25279319
2. PMID:25782086
3. PMID:15478612
4. PMID:29797267
5. PMID:29391282
6. PMID:29797268
7. PMID:19272529
8. PMID:7516629
9. PMID:34859500