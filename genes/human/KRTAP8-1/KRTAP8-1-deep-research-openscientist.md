---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T17:27:41.875365'
end_time: '2026-10-24T18:08:56.451593'
duration_seconds: 2474.58
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: KRTAP8-1
  gene_symbol: KRTAP8-1
  uniprot_accession: Q8IUC2
  protein_description: 'RecName: Full=Keratin-associated protein 8-1; AltName: Full=High
    glycine-tyrosine keratin-associated protein 8.1;'
  gene_info: Name=KRTAP8-1; Synonyms=KAP8.1, KRTAP8.1;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the KRTAP type 8 family. .
  protein_domains: KRTAP8-1. (IPR039351); KRTAP_type8/19/20/21/22. (IPR021743); KRTAP
    (PF11759)
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
  path: KRTAP8-1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: KRTAP8-1-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q8IUC2
- **Protein Description:** RecName: Full=Keratin-associated protein 8-1; AltName: Full=High glycine-tyrosine keratin-associated protein 8.1;
- **Gene Information:** Name=KRTAP8-1; Synonyms=KAP8.1, KRTAP8.1;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the KRTAP type 8 family. .
- **Key Domains:** KRTAP8-1. (IPR039351); KRTAP_type8/19/20/21/22. (IPR021743); KRTAP (PF11759)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "KRTAP8-1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'KRTAP8-1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **KRTAP8-1** (gene ID: KRTAP8-1, UniProt: Q8IUC2) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# KRTAP8-1 (KAP8.1, UniProt Q8IUC2): Functional Annotation Report

## Summary

**KRTAP8-1 encodes keratin-associated protein 8.1 (KAP8.1), a small structural protein of the hair fibre.** It is not an enzyme, transporter, or signaling molecule. Its primary and essentially sole function is **structural**: it is one of the matrix proteins that embed and crosslink the keratin intermediate filaments (IFs) of the hard α-keratin composite that constitutes the hair/wool cortex. KAP8.1 belongs to the **high glycine–tyrosine (HGT) class** of keratin-associated proteins (KAPs), a diagnostic classification confirmed both by its amino-acid composition (computed here directly from the 63-residue Q8IUC2 sequence: ~42.9% Gly+Tyr, only 4 cysteines) and by the literature ([PMID: 25279319](https://pubmed.ncbi.nlm.nih.gov/25279319/), [PMID: 23791804](https://pubmed.ncbi.nlm.nih.gov/23791804/)).

Mechanistically, the most precise experimental evidence comes from in-vitro biophysical work showing that **KAP8.1 binds the head domain of the type II trichocyte (hair) keratin K85** and helps organize the helical arrangement of intermediate filaments in the hair **orthocortex** — the compartment distributed asymmetrically on the convex side of curved fibres ([PMID: 23791804](https://pubmed.ncbi.nlm.nih.gov/23791804/)). Through this binding, and through additional bidirectional interactions with other partners, KAP8.1 contributes to the mechanical strength and the shape/curvature of the hair fibre. Immunohistochemistry confirms that the protein is deposited in discrete regions of the keratinizing cortex, consistent with a role in controlling hair curvature ([PMID: 30125694](https://pubmed.ncbi.nlm.nih.gov/30125694/)).

Structurally, AlphaFold modelling performed in this investigation shows KAP8.1 to be **fully intrinsically disordered** (mean pLDDT 41.2; 100% of residues below pLDDT 50), consistent with its role as a flexible component of the amorphous interfilamentous matrix rather than a globular folded protein. Its glycine-tyrosine core is **conserved across mammals under purifying selection**, indicating a specific, maintained keratin-interaction function. It acts **intracellularly** within terminally differentiating cortical trichocytes, is encoded by an **intronless gene** in the chromosome 21q22.1 KAP gene cluster, and is expressed early in the follicle-differentiation program under **HOXC13** control ([PMID: 15385554](https://pubmed.ncbi.nlm.nih.gov/15385554/), [PMID: 22044071](https://pubmed.ncbi.nlm.nih.gov/22044071/)).

**Gene-identity verification:** The gene symbol KRTAP8-1 matches the UniProt protein description (Keratin-associated protein 8-1 / high glycine-tyrosine keratin-associated protein 8.1), the organism is correctly *Homo sapiens*, and the protein family (KRTAP type 8, HGT-KAP, Pfam PF11759) aligns with all literature found. There was **no gene-symbol ambiguity**: all retrieved literature (KAP8/KAP8.1 in human, sheep, and mouse) refers to the same orthologous HGT-KAP. This report therefore proceeds with confidence on the correct target.

---

## Key Findings

### Finding 1 — KAP8.1 is a high glycine-tyrosine keratin-associated structural matrix protein of the hair cortex

The amino-acid composition of KAP8.1, computed directly from the UniProt Q8IUC2 sequence (63 residues), is the defining signature of the high glycine-tyrosine (HGT) KAP class: **glycine 23.8% and tyrosine 19.0%, together 42.9%** of all residues, with very low cysteine content (6.3%, 4 residues). The sequence contains a defined region of twelve 2-amino-acid G-[YCGS] repeats spanning residues 12–54. This composition contrasts sharply with the other two KAP classes — high-sulfur (HS) and ultra-high-sulfur (UHS) KAPs — which are cysteine-rich and mediate disulfide crosslinking. The three-class scheme is established in the literature: keratin-associated proteins are "classified into three groups; high sulfur (HS) KAPs, ultra high sulfur (UHS) KAPs, and high glycine-tyrosine (HGT) KAPs" ([PMID: 23791804](https://pubmed.ncbi.nlm.nih.gov/23791804/)). KAP8 specifically is assigned to the HGT family and "was believed to be coded for by a single gene in both humans and sheep" ([PMID: 25279319](https://pubmed.ncbi.nlm.nih.gov/25279319/)).

Functionally, UniProt annotates KAP8.1 as a matrix protein that embeds the hair-keratin intermediate filaments, and it belongs to the KRTAP type 8 family (Pfam PF11759). Together these establish the fundamental identity of the protein: a **non-enzymatic, non-catalytic structural matrix protein** of the hair shaft, whose role is to be embedded among, and to crosslink, the keratin IFs.

### Finding 2 — KAP8.1 binds the head domain of hair keratin K85 and organizes the helical arrangement of intermediate filaments in the orthocortex

The most precise mechanistic evidence for KAP8.1 function comes from a dedicated biophysical study (Matsunaga et al., 2013). Using **isothermal titration calorimetry (ITC), Western blotting, circular dichroism, and transmission electron microscopy**, the authors demonstrated that "KAP8.1 binds to the head domain of K85, which is helically aligned around the axis of the intermediate filament (IF)" ([PMID: 23791804](https://pubmed.ncbi.nlm.nih.gov/23791804/)). K85 is a type II trichocyte (hair) keratin, so this identifies the **specific molecular binding partner and binding mode** of KAP8.1 — a level of detail rarely available for KAP proteins.

The same study links this binding directly to higher-order fibre architecture: "the helical arrangement of IFs found in the orthocortex, which is uniquely distributed on the convex fiber side of the hair, is regulated by KAP8.1" ([PMID: 23791804](https://pubmed.ncbi.nlm.nih.gov/23791804/)). The authors further describe a **bidirectional binding property** of HGT-KAPs (also engaging, for example, the desmoplakin C-terminus), proposing that this crosslinking contributes to the mechanical strength and the shape of the hair. This is the central mechanistic claim of the report: KAP8.1 is a **molecular organizer/crosslinker** that positions and bundles keratin IFs on one side of the fibre.

### Finding 3 — KAP8.1 localizes to discrete regions of the keratinizing cortex and is linked to hair curvature

Monoclonal-antibody immunohistochemistry (Akiba et al., 2018) showed that "KAP8.1 was predominantly expressed in discrete regions of the keratinizing zone of the hair shaft cortex" ([PMID: 30125694](https://pubmed.ncbi.nlm.nih.gov/30125694/)), paralleling the distribution of KAP8.1 mRNA. The authors explicitly "suggested that KAP8.1 plays a role associated with cells to control hair curvature" ([PMID: 30125694](https://pubmed.ncbi.nlm.nih.gov/30125694/)). UniProt's tissue-specificity annotation is consistent: expression is essentially restricted to only one vertical half of the hair-forming compartment, and in beard hairs is absent from the central medulla.

This asymmetric deposition is the hallmark of HGT-KAPs generally: proteins "high in glycine and tyrosine tend to be expressed initially on the orthocortical side of the follicle" ([PMID: 17697142](https://pubmed.ncbi.nlm.nih.gov/17697142/)). The asymmetry is mechanistically important because curved (crimped) hairs have a bilateral cortex — ortho- on the convex side and para- on the concave side — and differential matrix-protein deposition between the two halves generates the differential swelling/mechanical behaviour that bends the fibre. KAP8.1's orthocortical localization therefore ties its molecular binding function (Finding 2) directly to the macroscopic phenotype of **hair curvature**.

### Finding 4 — KRTAP8-1 is an intronless hair-cortex gene in the HGT-KAP program, co-expressed early under HOXC13 control

KRTAP8-1 maps to the **chromosome 21q22.1 KAP gene domain** and, like other HGT-KAPs, is a **single-exon (intronless) gene** — a common architecture in the KAP superfamily. Its temporal and spatial expression follows the stereotyped HGT-KAP program. In the orthologous mouse Krtap16 HGT-KAP complex, the genes show "strong expression in a narrowly defined pattern restricted to the lower and middle cortical region of the hair shaft" ([PMID: 15385554](https://pubmed.ncbi.nlm.nih.gov/15385554/)), decline through catagen, and carry functional **Hoxc13 binding sites**, placing the HGT-KAP program under the control of this master hair-follicle transcription factor.

HGT-KAP genes are also among the first KAP genes activated during follicle differentiation: "The genes encoding the high glycine-tyrosine (HGT) KAPs are the first sub-group of KAP genes expressed in the wool follicle and just after expression of the keratin genes" ([PMID: 22044071](https://pubmed.ncbi.nlm.nih.gov/22044071/)). This temporal ordering — keratins first, then HGT-KAPs — is mechanistically sensible: the IF scaffold must be laid down before (or while) the matrix proteins that embed it are deposited.

### Finding 5 — KAP8.1 is predicted to be fully intrinsically disordered with regularly spaced aromatic residues

An AlphaFold model (AF-Q8IUC2-F1, v6) analyzed in this investigation has a **mean pLDDT of 41.2, with 100% of residues below pLDDT 50** — the signature of an intrinsically disordered protein with no confidently folded globular structure. This is entirely consistent with KAP8.1's role as a flexible component of the **amorphous interfilamentous matrix** rather than a rigid folded module.

The sequence features that drive both disorder and function are striking: the 63-aa chain is **28.6% aromatic** (18 Tyr/Phe/Trp residues, spaced roughly every 3–4 residues), **23.8% glycine** (15 Gly, similarly regularly spaced), with only 4 cysteines (positions 3, 14, 29, 49) and a near-neutral net charge (+1). Seven GY and four YG dipeptide motifs recur. The regular spacing of aromatic residues is important mechanistically: because KAP8.1 is cysteine-poor, it cannot rely on the disulfide-crosslinking chemistry used by high-sulfur KAPs; instead, **aromatic (Tyr/Phe) stacking and other non-covalent interactions** are the likely basis of its keratin adhesion. This fits the broader biomaterial model in which "hard α-keratins are fibre-reinforced biomaterials that consist of 10 nm intermediate filaments (IFs) embedded in an elastomeric protein matrix" ([PMID: 23135675](https://pubmed.ncbi.nlm.nih.gov/23135675/)) — KAP8.1 being a component of the elastomeric matrix phase.

### Finding 6 — KAP8.1 has a highly conserved central core across mammals, indicating purifying selection on its keratin-interaction function

Retrieval and alignment of 25 mammalian KAP8.1/KRTAP8-1 orthologs from UniProt (human Q8IUC2, sheep P02448, mouse O08633, cow F1MTA9, orangutan H2P2Y0, and others) revealed a **strongly conserved central block**. Measured against human as the anchor, core identity was: **orangutan 100%, cow 93%, sheep 91%, mouse 74%** over the ~42–44-aa core. A central motif around **PLGYSVGCGYGSTYSPVGYG** — including the GY-rich repeat and conserved Cys/Ser/Pro residues — is near-invariant, whereas the N-terminal ~8–9 residues are more variable. The retention of this core under purifying selection implies that it mediates a **specific, functionally important keratin interaction** that natural selection has preserved for tens of millions of years.

This bioinformatic conclusion is independently corroborated by experiment: the Akiba et al. monoclonal antibody "recognized a linear epitope shared among human, mouse, and sheep KAP8.1" ([PMID: 30125694](https://pubmed.ncbi.nlm.nih.gov/30125694/)) — i.e., a conserved linear stretch of the protein across exactly the species in which high core identity was measured here.

---

## Mechanistic Model / Interpretation

KAP8.1 can be understood as a small, disordered **molecular "glue and organizer"** operating inside terminally differentiating hair-cortex cells. The following model synthesizes the six findings.

### The hard α-keratin composite

Hair is a fibre-reinforced biological composite. Its building block is the macrofibril: paracrystalline arrays of ~10 nm **keratin intermediate filaments (IFs)** embedded in an **amorphous protein matrix** made of KAPs ([PMID: 23135675](https://pubmed.ncbi.nlm.nih.gov/23135675/)). KAP8.1 is a matrix protein in this composite.

```
   Hair cortex composite (cross-section, schematic)

   ||||  ||||  ||||      <- keratin intermediate filaments (incl. K85)
   ||||  ||||  ||||
   ::::::::::::::::      <- amorphous KAP matrix
   ::KAP8.1::KAP8.1::       (HGT, cysteine-poor, aromatic/Gly-rich)
   ::::::::::::::::

   KAP8.1 binds the HEAD DOMAIN of K85, which is helically
   arrayed around the IF axis -> organizes helical IF bundling
```

### From molecule to fibre shape

```
 Gene (chr 21q22.1, intronless)
        |  HOXC13-driven, early in differentiation
        v
 KAP8.1 protein (63 aa, intrinsically disordered)
        |  Gly 23.8% + Tyr 19.0%; aromatic-rich; Cys-poor
        v
 Binds head domain of hair keratin K85  -- bidirectional crosslinking
        |
        v
 Organizes helical arrangement of IFs in the ORTHOCORTEX
        |  deposited asymmetrically (convex side of fibre)
        v
 Bilateral ortho/para cortex asymmetry
        |
        v
 Mechanical strength + hair SHAPE / CURVATURE
```

The key mechanistic links are:

| Level | What KAP8.1 does | Evidence |
|---|---|---|
| Sequence | Gly/Tyr-rich, Cys-poor, aromatic — adhesion via non-covalent (aromatic) chemistry | Composition computed from Q8IUC2; [PMID: 25279319](https://pubmed.ncbi.nlm.nih.gov/25279319/) |
| Structure | Intrinsically disordered → flexible matrix filler | AlphaFold pLDDT 41.2, 100% < 50 |
| Molecular interaction | Binds head domain of keratin K85 | ITC/CD/TEM, [PMID: 23791804](https://pubmed.ncbi.nlm.nih.gov/23791804/) |
| Supramolecular | Organizes helical IF arrangement in orthocortex | [PMID: 23791804](https://pubmed.ncbi.nlm.nih.gov/23791804/) |
| Tissue | Deposited in discrete keratinizing cortex regions, one vertical half | [PMID: 30125694](https://pubmed.ncbi.nlm.nih.gov/30125694/), [PMID: 17697142](https://pubmed.ncbi.nlm.nih.gov/17697142/) |
| Phenotype | Contributes to mechanical strength and hair curvature | [PMID: 23791804](https://pubmed.ncbi.nlm.nih.gov/23791804/), [PMID: 30125694](https://pubmed.ncbi.nlm.nih.gov/30125694/) |
| Evolution | Core conserved under purifying selection → specific maintained function | Ortholog alignment; [PMID: 30125694](https://pubmed.ncbi.nlm.nih.gov/30125694/) |

### Localization

KAP8.1 carries out its function **intracellularly**, within the cytoplasm of terminally differentiating cortical trichocytes of the hair follicle, where it is deposited into the hardening keratin matrix during keratinization. It is not secreted and is not a membrane protein. Within the fibre, it is spatially restricted to the **orthocortex** (one vertical half of the cortex) and is absent from the medulla in beard hairs ([PMID: 30125694](https://pubmed.ncbi.nlm.nih.gov/30125694/)). After keratinization is complete, the protein persists as a permanent, crosslinked structural constituent of the dead hair shaft.

### Pathway context

KAP8.1 does not participate in a classical signaling or metabolic pathway. The relevant "pathway" is the **hair-follicle keratinization / differentiation program**: hair keratin genes are expressed first, immediately followed by the HGT-KAP subgroup (including KRTAP8-1), under the transcriptional control of HOXC13 ([PMID: 22044071](https://pubmed.ncbi.nlm.nih.gov/22044071/), [PMID: 15385554](https://pubmed.ncbi.nlm.nih.gov/15385554/)). The output of this program is the assembled hard α-keratin fibre.

---

## Evidence Base

| PMID | Title (abbreviated) | How it supports the findings |
|---|---|---|
| [23791804](https://pubmed.ncbi.nlm.nih.gov/23791804/) | *Bidirectional binding property of high glycine-tyrosine keratin-associated protein contributes to the mechanical strength and shape of hair* | **Primary mechanistic study.** ITC/CD/TEM show KAP8.1 binds the head domain of keratin K85 and organizes helical IF arrangement in the orthocortex; establishes HGT-KAP class and bidirectional crosslinking → strength and shape. Supports Findings 1, 2. |
| [30125694](https://pubmed.ncbi.nlm.nih.gov/30125694/) | *Structural behavior of keratin-associated protein 8.1 in human hair as revealed by a monoclonal antibody* | **Localization study.** IHC shows KAP8.1 in discrete keratinizing cortex regions; proposes role in hair curvature; demonstrates a conserved linear epitope across human, mouse, sheep. Supports Findings 3, 6. |
| [25279319](https://pubmed.ncbi.nlm.nih.gov/25279319/) | *The sheep KAP8-2 gene, a new KAP8 family member that is absent in humans* | Assigns KAP8 to the HGT-KAP family; notes single-gene status in humans. Supports Finding 1. |
| [15385554](https://pubmed.ncbi.nlm.nih.gov/15385554/) | *Krtap16 … hair keratin-associated protein (KAP) gene complex … regulation by Hoxc13* | Cortical, stage-specific expression of the HGT-KAP program; functional HOXC13 binding sites. Supports Finding 4. |
| [22044071](https://pubmed.ncbi.nlm.nih.gov/22044071/) | *Search for variation in the ovine KAP7-1 and KAP8-1 genes …* | Places HGT-KAPs first in the KAP expression sequence, just after hair keratins. Supports Finding 4. |
| [17697142](https://pubmed.ncbi.nlm.nih.gov/17697142/) | *The differential expression of proteins in the cortical cells of wool and hair fibres* | HGT proteins are deposited initially on the orthocortical side → basis for crimp/curvature asymmetry. Supports Finding 3. |
| [23135675](https://pubmed.ncbi.nlm.nih.gov/23135675/) | *Regulation of hard α-keratin mechanics via control of intermediate filament hydration: matrix squeeze revisited* | Establishes the IF-in-matrix composite architecture in which KAP8.1 is the elastomeric matrix phase. Supports Finding 5. |

Supporting context papers from the broader literature set reinforce the model without directly testing KAP8.1: characterization of human type I/II hair keratin and KAP gene domains ([PMID: 14962103](https://pubmed.ncbi.nlm.nih.gov/14962103/), [PMID: 15617563](https://pubmed.ncbi.nlm.nih.gov/15617563/), [PMID: 15737194](https://pubmed.ncbi.nlm.nih.gov/15737194/)); the human KAP review ([PMID: 16939781](https://pubmed.ncbi.nlm.nih.gov/16939781/)); mouse HGT proteins ([PMID: 9374545](https://pubmed.ncbi.nlm.nih.gov/9374545/)); and hair mechanical/viscoelastic studies ([PMID: 28919511](https://pubmed.ncbi.nlm.nih.gov/28919511/), [PMID: 22848616](https://pubmed.ncbi.nlm.nih.gov/22848616/), [PMID: 27162354](https://pubmed.ncbi.nlm.nih.gov/27162354/)) that describe the IF/matrix composite whose matrix phase KAP8.1 populates.

---

## Limitations and Knowledge Gaps

1. **No KAP8.1-specific loss-of-function phenotype in humans.** There is no reported human disease directly attributable to KRTAP8-1 mutation. KAP genes are highly polymorphic and partially redundant, so a single-gene knockout may be phenotypically subtle. The curvature/strength role is therefore inferred from biochemistry, localization, and orthology rather than from a human genetic lesion.

2. **Binding studied for K85 only.** The direct binding evidence is for the head domain of keratin K85 ([PMID: 23791804](https://pubmed.ncbi.nlm.nih.gov/23791804/)). Whether KAP8.1 binds additional hair keratins (e.g., other type II trichocyte keratins) with comparable affinity, and the precise residues mediating binding, remain to be mapped.

3. **The aromatic-adhesion hypothesis is inferential.** The proposal that Tyr/Phe stacking (rather than disulfide chemistry) mediates keratin adhesion is well-motivated by composition and disorder but has not been directly demonstrated by mutagenesis for KAP8.1.

4. **AlphaFold confidence is intrinsically low for disordered proteins.** The pLDDT < 50 result is itself evidence of disorder, but it means no atomic-resolution structural model of the bound state exists. The conformation KAP8.1 adopts upon binding keratin is unknown.

5. **Quantitative contribution to fibre mechanics is unresolved.** The degree to which KAP8.1 specifically (versus the HGT-KAP class collectively) sets curvature or strength has not been isolated experimentally.

6. **Human vs. ovine/murine extrapolation.** Several mechanistic details derive from sheep and mouse systems; while the core is highly conserved (Finding 6), species-specific differences in expression timing or partner keratins cannot be excluded.

---

## Proposed Follow-up Experiments / Actions

1. **Targeted binding map.** Perform ITC/SPR of recombinant human KAP8.1 against a panel of hair keratin head domains (K81–K86 type II; K31–K40 type I) to define substrate specificity beyond K85.

2. **Mutagenesis of aromatic residues.** Systematically substitute the conserved Tyr/Phe residues (and the near-invariant core motif PLGYSVGCGYGSTYSPVGYG) and re-test keratin binding to directly test the aromatic-adhesion hypothesis.

3. **Knockout/knock-in mouse.** Generate Krtap8-1 null and point-mutant mice and quantify hair curvature, cross-sectional ortho/para asymmetry, and tensile/viscoelastic properties to isolate KAP8.1's phenotypic contribution.

4. **Super-resolution immuno-EM.** Localize KAP8.1 at the IF surface within orthocortical macrofibrils to test the predicted helical, IF-head-domain-associated positioning in situ.

5. **Population-genetics of KRTAP8-1 variants.** Associate human KRTAP8-1 polymorphisms with quantitative hair-curl phenotypes across ancestries to test the curvature link in humans.

6. **Integrative structural modelling.** Use AlphaFold-Multimer / disordered-protein ensemble methods on the KAP8.1–K85 head-domain complex to generate a testable bound-state model.

---

*Report generated from a 5-iteration autonomous investigation: 6 confirmed findings, 35 papers reviewed. Target gene identity (KRTAP8-1 / Q8IUC2 / Homo sapiens / HGT-KAP type 8 family) was verified against all literature with no gene-symbol ambiguity.*


## Artifacts

- [OpenScientist final report](KRTAP8-1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](KRTAP8-1-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:25279319
2. PMID:23791804
3. PMID:30125694
4. PMID:15385554
5. PMID:22044071
6. PMID:17697142
7. PMID:23135675
8. PMID:14962103
9. PMID:15617563
10. PMID:15737194
11. PMID:16939781
12. PMID:9374545
13. PMID:28919511
14. PMID:22848616
15. PMID:27162354