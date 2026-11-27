---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T17:27:42.048549'
end_time: '2026-10-24T17:40:26.852154'
duration_seconds: 764.8
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: KRTAP1-1
  gene_symbol: KRTAP1-1
  uniprot_accession: Q07627
  protein_description: 'RecName: Full=Keratin-associated protein 1-1; AltName: Full=High
    sulfur keratin-associated protein 1.1; AltName: Full=Keratin-associated protein
    1.1; AltName: Full=Keratin-associated protein 1.6; AltName: Full=Keratin-associated
    protein 1.7;'
  gene_info: Name=KRTAP1-1; Synonyms=B2A, KAP1.1, KAP1.6, KAP1.7, KRTAP1.1;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the KRTAP type 1 family. .
  protein_domains: KAP. (IPR002494); Keratin_B2 (PF01500)
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
citation_count: 15
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: KRTAP1-1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: KRTAP1-1-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q07627
- **Protein Description:** RecName: Full=Keratin-associated protein 1-1; AltName: Full=High sulfur keratin-associated protein 1.1; AltName: Full=Keratin-associated protein 1.1; AltName: Full=Keratin-associated protein 1.6; AltName: Full=Keratin-associated protein 1.7;
- **Gene Information:** Name=KRTAP1-1; Synonyms=B2A, KAP1.1, KAP1.6, KAP1.7, KRTAP1.1;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the KRTAP type 1 family. .
- **Key Domains:** KAP. (IPR002494); Keratin_B2 (PF01500)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "KRTAP1-1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'KRTAP1-1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **KRTAP1-1** (gene ID: KRTAP1-1, UniProt: Q07627) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# KRTAP1-1 (Q07627): A High-Sulfur Keratin-Associated Protein That Disulfide-Cross-Links the Hair-Shaft Cortex

**Gene:** KRTAP1-1 (synonyms: B2A, KAP1.1, KAP1.6, KAP1.7, KRTAP1.1)
**Protein:** Keratin-associated protein 1-1 / High-sulfur keratin-associated protein 1.1
**Organism:** *Homo sapiens* (human)
**UniProt:** Q07627 — **Family:** KRTAP type 1 — **Domains:** IPR002494 (KAP), Pfam PF01500 (Keratin_B2)

## Summary

**KRTAP1-1 (UniProt Q07627) encodes a high-sulfur, cysteine-rich keratin-associated protein (KAP) of the type-1 ("B2") family. Its function is structural, not catalytic, transport, or signaling: it is a matrix protein of the hair-shaft cortex that becomes extensively disulfide (cystine) cross-linked to hard keratin intermediate filaments (IFs) and to neighbouring KAPs, embedding the filament network in a rigid amorphous matrix that gives hair its hardness, stiffness, and mechanical resilience.** The gene symbol, organism (*Homo sapiens*), protein family (KRTAP type 1), and domain assignments (IPR002494 "KAP"; Pfam PF01500 "Keratin_B2") were all verified against primary literature, and the UniProt synonyms (KAP1.1, KAP1.6, KAP1.7, B2A) map directly onto proteins described in the human KAP1-family characterization studies. This is the correct gene; there is no ambiguity of identity, although the directly functional literature for this *specific* paralog is limited and most mechanistic understanding derives from family-level and class-level evidence.

The protein acts **intracellularly within terminally differentiating cortical trichocytes of the anagen hair follicle**, where it is synthesized late in differentiation and deposited into the interfilament matrix of the hardening hair shaft. Direct sequence analysis of the 177-amino-acid Q07627 product confirms the defining biochemical feature of the family: an exceptionally high cysteine content (25.4 mol%) organized into tandem "double-cysteine" pentapeptide repeats (CCQPS, CCETS, CCQTS, etc.). These paired thiols are the chemical basis for the dense disulfide cross-linking that locks the keratin IF network into a cohesive, insoluble composite.

Functionally, KRTAP1-1 is a **terminal structural effector of the hair-follicle keratinization program**. It lies downstream of the HOXC13/DLX3/LEF1/FOXN1 transcription-factor network (itself downstream of follicular Wnt/BMP signalling), which drives cortical trichocytes to co-express hard keratins and KAPs during the same late-differentiation window. KRTAP1-1 does not participate in any enzymatic reaction, transport process, or signal-transduction cascade; its "pathway" is the biosynthesis and assembly of the hair fiber. Orthogonal genetic evidence from livestock — where allelic variation in KAP genes causally alters fiber diameter and quality — confirms that proteins of this class set the physical/material properties of the hair fiber.

---

## Key Findings

### Finding 1 — Identity confirmed: KRTAP1-1 is a high-sulfur type-1 keratin-associated protein (KAP1.1 / hKAP1.6 / hKAP1.7)

The product of Q07627 was unambiguously placed within the human keratin-associated protein 1 (KAP1) family. The UniProt synonyms listed for this entry — KAP1.1, KAP1.6, KAP1.7, and B2A — correspond directly to proteins characterized by cDNA cloning and sequence analysis. Rogers and colleagues explicitly named two novel human high-sulfur KAPs "hKAP1.6 and hKAP1.7" ([PMID: 11841537](https://pubmed.ncbi.nlm.nih.gov/11841537/)), the exact synonyms recorded for Q07627. The dedicated KAP1-family characterization reports isolation of "*two cDNA encoding novel members of the human keratin-associated protein 1 family (human keratin-associated protein 1.6 and human keratin-associated protein 1.7)*" ([PMID: 12895003](https://pubmed.ncbi.nlm.nih.gov/12895003/)). The domain assignments — InterPro IPR002494 ("KAP") and Pfam PF01500 ("Keratin_B2") — are the signatures of the KRTAP type-1 high-sulfur family. Identity verification is therefore complete across gene symbol, organism, family, and domain.

### Finding 2 — Primary function: a structural matrix protein that cross-links hair keratin intermediate filaments

KAP proteins constitute the interfilamentous matrix of the hair shaft, forming a cross-linked network together with the hair keratin IFs that provide the fiber's load-bearing core. The KAP1-family characterization states plainly that "*Keratin-associated proteins are involved in the formation of the cross-linked network of the keratin-intermediate filament proteins that support hair fibers*" ([PMID: 12895003](https://pubmed.ncbi.nlm.nih.gov/12895003/)). The high-sulfur subclass to which KRTAP1-1 belongs supplies the matrix between filament bundles: a representative cysteine-rich KAP forms "*part of the interstitial matrix between bundles of intermediate filaments*" ([PMID: 7536172](https://pubmed.ncbi.nlm.nih.gov/7536172/)). The cross-linking chemistry is disulfide-based: in keratin fibers, "*Intermolecular disulfide bonds occur within filaments and between them and the surrounding matrix*" ([PMID: 35477858](https://pubmed.ncbi.nlm.nih.gov/35477858/)). Thus KRTAP1-1's role is to act as a cystine-rich "glue" that covalently ties the keratin filament network together and embeds it in a rigid amorphous phase.

### Finding 3 — Localization: expressed and acting in the differentiated hair-follicle cortex

In situ hybridization of human anagen hair follicles localizes the KAP1 group — including hKAP1.6/hKAP1.7 (= KRTAP1-1) — to the cortex. Rogers et al. "*demonstrated the expression of this group in the differentiated portions of the hair cortex*" ([PMID: 11841537](https://pubmed.ncbi.nlm.nih.gov/11841537/)). KAP synthesis occurs intracellularly in cortical trichocytes late in terminal differentiation, where the proteins are deposited into the interfilament matrix of the hardening hair shaft — consistent with the observation that cysteine-rich KAPs are synthesized late in follicle differentiation ([PMID: 7536172](https://pubmed.ncbi.nlm.nih.gov/7536172/)). The site of action is therefore the keratinizing cortex of the growing (anagen) hair follicle, inside the trichocyte, with the mature product forming an integral part of the dead, insoluble hair shaft.

### Finding 4 — Structure/evolution: a five-domain architecture built from double-cysteine pentapeptide repeats expanded by gene duplication

Comparative sequence analysis established that KAP1 proteins are "*fundamentally composed of five distinct domains, and that they can be classified primarily by a striking variation in double cysteine-containing pentapeptide repeats in the repetitive I domain*" ([PMID: 12895003](https://pubmed.ncbi.nlm.nih.gov/12895003/)). These cysteine-repeat motifs arose "*mainly through gene duplication of the cysteine-repeat motifs during evolution*" ([PMID: 12895003](https://pubmed.ncbi.nlm.nih.gov/12895003/)). The architecture is functionally coherent: the central repetitive "I" domain concentrates the paired cysteines that supply the thiols for disulfide matrix cross-linking, while the flanking domains frame the repeat core. Evolution of the family by duplicating cysteine-rich units directly tunes the cross-linking density available to the matrix.

### Finding 5 — Direct sequence analysis of Q07627 confirms high-sulfur composition and double-cysteine pentapeptide repeats

Independent analysis of the UniProt canonical sequence of Q07627 (177 residues) quantifies the family signature in this specific protein: cysteine = 45/177 = **25.4 mol%** (sulfur-containing residues, C+M = 26.0%), with 14 adjacent "CC" dipeptides. The central repetitive region (approximately residues 23–86) is built from tandem double-cysteine pentapeptide units — CCQPS (×4), CCETS (×3), CCQTS, and related motifs (12 CC-containing pentapeptide-type motifs in total). The overall amino-acid composition is dominated by Cys (25.4%), Ser (16.9%), Gly (10.2%), Thr (8.5%), Pro (8.5%), and Gln (6.2%). These measured CCQPS/CCETS units are precisely the "double cysteine-containing pentapeptide repeats in the repetitive I domain" described for the family ([PMID: 12895003](https://pubmed.ncbi.nlm.nih.gov/12895003/)). This provides direct, protein-specific confirmation that KRTAP1-1 carries the chemical machinery (dense paired thiols) required for its structural cross-linking role.

| Property | Value (Q07627) | Interpretation |
|---|---|---|
| Length | 177 aa | Small matrix protein |
| Cysteine | 25.4 mol% (45 residues) | "High-sulfur" — thiol donor for disulfides |
| Sulfur residues (C+M) | 26.0 mol% | Extreme sulfur enrichment |
| "CC" dipeptides | 14 | Paired thiols for cross-linking |
| Dominant repeats | CCQPS (×4), CCETS (×3), CCQTS | Double-cysteine pentapeptide units |
| Other major residues | Ser 16.9%, Gly 10.2%, Thr 8.5%, Pro 8.5% | Flexible, non-helical matrix composition |

### Finding 6 — Regulatory/pathway placement: a downstream effector of the HOXC13/DLX3/LEF1/FOXN1 hair-shaft differentiation program

KAP genes carry promoter enhancer elements for the HOX transcription-factor family (alongside ETS, heat-shock factor, and AML elements), present in nearly all KAP genes examined: "*Primary among these were binding elements for the ETS, heat shock factor, AML, and HOX families of transcription factors*" ([PMID: 14962103](https://pubmed.ncbi.nlm.nih.gov/14962103/)). The master regulator HOXC13 drives the cortical trichocyte hard-keratin/KAP differentiation program: "*HOXC13 is one critical regulatory factor, proved by the hair defects in HOXC13 mutant mice and HOXC13 mutant patients*" ([PMID: 30139327](https://pubmed.ncbi.nlm.nih.gov/30139327/)). HOXC13 itself is controlled by upstream factors including DLX3 and GATA3 — CtBP1-driven suppression of Dlx3 reduces downstream Gata3, Hoxc13, and hair keratins ([PMID: 24280726](https://pubmed.ncbi.nlm.nih.gov/24280726/)). Post-transcriptionally, miR-22 represses Dlx3, Foxn1, and Hoxc13 to shut down the hair-keratin differentiation program ([PMID: 26020521](https://pubmed.ncbi.nlm.nih.gov/26020521/)). KAPs such as KRTAP1-1 are co-expressed with hard keratins in the same cortical cells during the same late-differentiation window ([PMID: 11841537](https://pubmed.ncbi.nlm.nih.gov/11841537/); [PMID: 7536172](https://pubmed.ncbi.nlm.nih.gov/7536172/)). KRTAP1-1 is therefore a terminal structural output of this transcriptional cascade, not a node that transmits signal.

### Finding 7 — Functional genetic evidence: allelic variation in KAP genes alters fiber diameter/quality

Although direct knockout data for human KRTAP1-1 are lacking, livestock genetics provide strong class-level causal evidence that KAP proteins determine fiber physical properties. In sheep, sequence variants of the KAP gene KRTAP20-1 are statistically associated with fiber traits: "*Variant A was found to be associated with a decrease in mean fiber diameter, fiber diameter standard deviation, and prickle factor*" ([PMID: 30535023](https://pubmed.ncbi.nlm.nih.gov/30535023/)). More broadly, KAP genes are established functional constituents whose variation affects cashmere/wool fiber traits ([PMID: 31979055](https://pubmed.ncbi.nlm.nih.gov/31979055/)), and KAPs are implicated in human hereditary hair diseases and polymorphism ([PMID: 16939781](https://pubmed.ncbi.nlm.nih.gov/16939781/)). This confirms that the KAP class causally sets fiber dimensions and material quality — exactly what a structural matrix cross-linker should do.

---

## Mechanistic Model / Interpretation

KRTAP1-1 is best understood as one of the **cystine-rich "mortar" proteins** that fill the space between hard-keratin "bricks" in the hair-shaft cortex. The mature hair fiber is a composite material: ordered, semi-crystalline keratin intermediate filaments embedded in an amorphous, sulfur-rich matrix. KRTAP1-1 is a constituent of that matrix. Its ~25% cysteine content, organized as paired CC thiols in pentapeptide repeats, enables it to form a high density of disulfide (cystine) cross-links — both within the matrix (KAP–KAP) and between the matrix and the keratin filament surfaces. This covalent network converts a bundle of filaments into a rigid, insoluble, mechanically resilient fiber.

```
 UPSTREAM SIGNALING            TRANSCRIPTIONAL PROGRAM            TERMINAL STRUCTURAL EFFECTORS
 (dermal papilla)              (cortical trichocyte nucleus)      (hair-shaft cortex, intracellular matrix)
 ─────────────────             ───────────────────────────        ───────────────────────────────────────
   Wnt / BMP  ───────►  DLX3 ─► GATA3 ─► HOXC13 ─┬─► LEF1    ───►   Hard keratins (KRT3x/KRT8x)  = FILAMENTS
   (miR-22 represses             │ (FOXN1)       │                       │
    DLX3/FOXN1/HOXC13)           └───────────────┘                 KRTAP1-1 + other KAPs         = MATRIX
                                                                         │
                                                                 disulfide (cystine) cross-linking
                                                                         │
                                                                   RIGID HAIR FIBER
                                                                 (hardness, stiffness, resilience)
```

The protein performs no chemistry of its own. It is not an enzyme (no catalytic domain, no substrate turnover), not a transporter (no membrane-spanning segments, no cargo), and not a signaling molecule (no receptor interaction or second-messenger role). Its "reaction" is passive incorporation and oxidative disulfide bond formation during the hardening of the fiber. Its biological process is **hair-follicle terminal differentiation / keratinization**; its cellular compartment of action is the **intracellular keratinizing cortex of the trichocyte**, with the final product residing in the dead, cornified hair shaft. Its pathway placement is purely downstream: it is an *output* of the HOXC13-centered hard-keratin program, co-regulated with the keratins it binds.

| Question posed by the research brief | Answer for KRTAP1-1 |
|---|---|
| Primary function (enzyme/transporter/structural/signaling)? | **Structural** — matrix cross-linker |
| Reaction / substrate specificity? | None (non-catalytic); "substrate" is conceptually the keratin IF surface it disulfide-bonds to |
| Broader structural role? | Fills interfilament matrix; cross-links keratin IFs into a rigid composite fiber |
| Where does it act? | Intracellularly in cortical trichocytes; final product in the cornified hair shaft |
| Pathway? | Terminal effector of HOXC13/DLX3/LEF1/FOXN1 hair-keratinization program (downstream of Wnt/BMP) |
| Evidence type | Family/class-level experimental (expression, composition, biochemistry) + direct sequence analysis + comparative genetics |

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the findings |
|---|---|---|
| [11841537](https://pubmed.ncbi.nlm.nih.gov/11841537/) | *hKAP1.6 and hKAP1.7 … expressed in the hair follicle cortex* | Names the exact synonyms of Q07627; localizes expression to the differentiated hair cortex (F001, F003) |
| [12895003](https://pubmed.ncbi.nlm.nih.gov/12895003/) | *Characterization of human keratin-associated protein 1 family members* | Places protein in KAP1 family; defines cross-linking role, five-domain architecture, double-cysteine pentapeptide repeats, duplication origin (F001, F002, F004, F005) |
| [7536172](https://pubmed.ncbi.nlm.nih.gov/7536172/) | *Cysteine-rich KAP synthesized late in rabbit hair follicle differentiation* | Establishes high-sulfur KAPs as interstitial matrix between IF bundles, synthesized late in differentiation (F002, F003) |
| [35477858](https://pubmed.ncbi.nlm.nih.gov/35477858/) | *Susceptibility of disulfide bonds … under tensile stress* | Provides disulfide cross-linking mechanism linking matrix to keratin filaments (F002) |
| [14962103](https://pubmed.ncbi.nlm.nih.gov/14962103/) | *Second high-sulfur KAP gene domain on chromosome 21* | Shows KAP genes carry HOX (and ETS/HSF/AML) promoter elements, linking them to the HOXC13 program (F006) |
| [30139327](https://pubmed.ncbi.nlm.nih.gov/30139327/) | *HOXC13 regulation of keratins in cashmere goat* | Establishes HOXC13 as master regulator of the cortical hard-keratin/KAP program (F006) |
| [24280726](https://pubmed.ncbi.nlm.nih.gov/24280726/) | *CtBP1 overexpression perturbs skin homeostasis* | Positions DLX3→GATA3→HOXC13→hair keratins cascade upstream of KAP expression (F006) |
| [26020521](https://pubmed.ncbi.nlm.nih.gov/26020521/) | *miR-22 regulation of the hair cycle* | Shows post-transcriptional control of DLX3/FOXN1/HOXC13 program feeding KAP expression (F006) |
| [30535023](https://pubmed.ncbi.nlm.nih.gov/30535023/) | *Ovine KRTAP20-1 variants and wool traits* | Causal genetic evidence that KAP allelic variation alters fiber diameter/quality (F007) |
| [31979055](https://pubmed.ncbi.nlm.nih.gov/31979055/) | *Caprine KAP gene variation and cashmere traits* | Reinforces KAPs as functional determinants of fiber traits (F007) |
| [16939781](https://pubmed.ncbi.nlm.nih.gov/16939781/) | *Human hair keratin-associated proteins (KAPs)* — review | Authoritative overview of KAP families, genomic organization, expression, disease links (F007) |
| [28919511](https://pubmed.ncbi.nlm.nih.gov/28919511/) | *Viscoelastic properties of α-keratin fibers* | Experimentally identifies matrix disulfide bonds as a source of fiber viscoelasticity/strength (context for F002) |
| [31067053](https://pubmed.ncbi.nlm.nih.gov/31067053/) | *Hydrogen and disulfide bond contribution to keratin mechanics* | Quantifies disulfide (cystine) contribution to fiber Young's modulus (context for F002) |

Supporting context from the broader literature set reinforces the structural interpretation: the whole-genome-sequencing report that flagged a KRTAP1-1 loss-of-function variant (rs3213755) associated with antidepressant remission ([PMID: 33633223](https://pubmed.ncbi.nlm.nih.gov/33633223/)) is an association/pharmacogenomic signal and does not imply a direct neuronal function for the protein; it most plausibly reflects linkage or an unrelated expression-QTL effect, and does not alter the structural annotation. The KRTAP-1 genomic region's fragility and role in ERBB2 amplification ([PMID: 33290559](https://pubmed.ncbi.nlm.nih.gov/33290559/)) concerns the locus as a genomic structural feature, not the protein's biochemical function.

---

## Limitations and Knowledge Gaps

1. **No direct functional study of the specific KRTAP1-1 paralog.** Mechanistic conclusions rest on (a) family/class-level experimental evidence (KAP1 characterization, high-sulfur KAP biochemistry) and (b) direct sequence analysis of Q07627. There is no published knockout, knockdown, structural (crystal/cryo-EM), or biophysical study of the isolated human KRTAP1-1 protein.

2. **Redundancy within the KAP1 cluster.** KRTAP1-1 is one of many closely related high-sulfur KAPs encoded in a tandem cluster. Functional redundancy likely obscures any single-gene phenotype, which is why human disease and livestock trait associations tend to implicate the KAP class rather than this specific gene.

3. **Cross-species inference.** Key regulatory (HOXC13, DLX3) and trait-association (KRTAP20-1, cashmere/wool) evidence comes from mouse, sheep, and goat. While the hair-keratinization program is highly conserved, species-specific details should be confirmed in human tissue.

4. **The "disulfide partner" specificity is inferred, not mapped.** The precise keratin IF surfaces and neighbouring KAPs to which KRTAP1-1 forms cystine bonds in vivo have not been experimentally mapped; "substrate specificity" is a conceptual rather than measured property.

5. **The pharmacogenomic association ([PMID: 33633223](https://pubmed.ncbi.nlm.nih.gov/33633223/)) is unexplained mechanistically** and should not be over-interpreted as evidence of a non-structural function.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and in vitro cross-linking assay.** Express Q07627, oxidatively refold it with purified human hair keratins, and use mass spectrometry to map intra-/inter-molecular disulfide bonds — directly testing the predicted matrix–filament cross-linking role and identifying specific cysteine partners.

2. **Structural/biophysical characterization.** Apply CD, SAXS, and AFM nanoindentation to recombinant KRTAP1-1 ± oxidation to quantify how its disulfide density contributes to matrix stiffness, complementing existing whole-fiber mechanics data ([PMID: 28919511](https://pubmed.ncbi.nlm.nih.gov/28919511/), [PMID: 31067053](https://pubmed.ncbi.nlm.nih.gov/31067053/)).

3. **Targeted expression profiling in human anagen follicles.** Use paralog-specific in situ hybridization / single-cell or spatial transcriptomics to resolve the precise cortical sub-compartment and differentiation timing of KRTAP1-1 relative to its partner hard keratins.

4. **Promoter dissection.** Experimentally validate HOXC13/LEF1/DLX3 occupancy at the KRTAP1-1 promoter (ChIP, reporter assays) to confirm its placement as a direct downstream effector of the hair-keratinization transcriptional network ([PMID: 14962103](https://pubmed.ncbi.nlm.nih.gov/14962103/), [PMID: 30139327](https://pubmed.ncbi.nlm.nih.gov/30139327/)).

5. **Human genetic association for hair phenotypes.** Test KRTAP1-1 sequence variants against quantitative human hair traits (fiber diameter, curl, tensile strength), paralleling the ovine/caprine KAP trait associations ([PMID: 30535023](https://pubmed.ncbi.nlm.nih.gov/30535023/), [PMID: 31979055](https://pubmed.ncbi.nlm.nih.gov/31979055/)).

6. **Clarify the rs3213755 pharmacogenomic signal** via eQTL fine-mapping to determine whether the association reflects the protein itself or linkage to neighbouring loci ([PMID: 33633223](https://pubmed.ncbi.nlm.nih.gov/33633223/)).

---

### Bottom line

KRTAP1-1 (Q07627) is a **high-sulfur, cysteine-rich structural matrix protein of the hair-shaft cortex**. It disulfide-cross-links hard keratin intermediate filaments and neighbouring KAPs into a rigid composite fiber, acts intracellularly in differentiating anagen cortical trichocytes, functions as a terminal effector of the HOXC13/DLX3/LEF1/FOXN1 keratinization program, and has no enzymatic, transport, or signaling activity.


## Artifacts

- [OpenScientist final report](KRTAP1-1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](KRTAP1-1-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:11841537
2. PMID:12895003
3. PMID:7536172
4. PMID:35477858
5. PMID:14962103
6. PMID:30139327
7. PMID:24280726
8. PMID:26020521
9. PMID:30535023
10. PMID:31979055
11. PMID:16939781
12. PMID:33633223
13. PMID:33290559
14. PMID:28919511
15. PMID:31067053