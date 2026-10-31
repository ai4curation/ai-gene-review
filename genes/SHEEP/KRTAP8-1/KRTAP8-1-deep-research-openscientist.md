---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T17:27:41.970380'
end_time: '2026-10-24T17:45:36.191736'
duration_seconds: 1074.22
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: SHEEP
  gene_id: KRTAP8-1
  gene_symbol: KRTAP8-1
  uniprot_accession: P02448
  protein_description: 'RecName: Full=Keratin-associated protein 8-1; AltName: Full=Component
    0.62; AltName: Full=HGT keratin; AltName: Full=HGT keratin component F; AltName:
    Full=Keratin, high-tyrosine matrix protein;'
  gene_info: Name=KRTAP8-1; Synonyms=HGT;
  organism_full: Ovis aries (Sheep).
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
citation_count: 10
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
- **UniProt Accession:** P02448
- **Protein Description:** RecName: Full=Keratin-associated protein 8-1; AltName: Full=Component 0.62; AltName: Full=HGT keratin; AltName: Full=HGT keratin component F; AltName: Full=Keratin, high-tyrosine matrix protein;
- **Gene Information:** Name=KRTAP8-1; Synonyms=HGT;
- **Organism (full):** Ovis aries (Sheep).
- **Protein Family:** Belongs to the KRTAP type 8 family. .
- **Key Domains:** KRTAP8-1. (IPR039351); KRTAP_type8/19/20/21/22. (IPR021743); KRTAP (PF11759)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "KRTAP8-1" matches the protein description above**
2. **Verify the organism is correct:** Ovis aries (Sheep).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'KRTAP8-1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **KRTAP8-1** (gene ID: KRTAP8-1, UniProt: P02448) in SHEEP.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# KRTAP8-1 (UniProt P02448) in Sheep (*Ovis aries*): A Functional Annotation Report

## Summary

**Sheep KRTAP8-1 (UniProt P02448) is a small, 62-residue structural protein belonging to the high-glycine-tyrosine (HGT) class of keratin-associated proteins (KAPs).** It is not an enzyme, transporter, or signaling molecule. Its primary function is structural: it serves as an interfilament **matrix protein** that packs against and organizes trichocyte keratin intermediate filaments (IFs) within the cortical cells of the wool/hair fibre. Historically it was known as "high-glycine-tyrosine type I-F," "HGT keratin component F," and "Component 0.62," and the modern gene symbol is **KRTAP8-1** (synonym *HGT*). The identity of the target is unambiguous: UniProt annotation, family assignment (KRTAP type 8), domain signatures (IPR039351, IPR021743, PF11759), and the primary literature all converge on a sheep wool HGT-KAP.

The protein carries out its function **intracellularly**, inside the differentiating and keratinizing cortical cells of the wool follicle, and ends up as an insoluble component of the mature, dead fibre cortex. KRTAP8-1 is deposited **preferentially on the orthocortical side** of the fibre and is among the earliest KAPs expressed during follicle differentiation (just after the keratin genes themselves). Experimentally, its human ortholog KAP8.1 has been shown to bind the **head domain of the type II trichocyte keratin K85**, which is helically arranged around the IF axis; this binding helps organize IFs into the helically packed macrofibrils characteristic of the orthocortex. Because the orthocortex and paracortex are segregated bilaterally within fine wool fibres, and because HGT-KAPs like KRTAP8-1 are concentrated in the orthocortex, the protein contributes mechanistically to **wool crimp (curvature) and fibre mechanical properties**.

The protein's amino acid chemistry explains how it works. Direct sequence analysis of P02448 shows a 62-residue chain that is ~40 mol% glycine + tyrosine, ~31 mol% aromatic (Tyr + Phe + Trp), almost completely devoid of charged residues (only two arginines; ~3 mol% charged), and containing four cysteines. A central tandem **glycine-aromatic repeat domain** (Gly-Tyr / Gly-Phe dipeptides) forms a flexible, "glue-like" core, while the four cysteines (at positions 4, 13, 28, 53) provide covalent anchoring points and a short basic C-terminal tail (…GCRRFWPFALY) provides the only charged motif. Because it is cysteine-poor relative to high-sulphur KAPs, KRTAP8-1 is thought to stabilize its contacts with keratins largely through **aromatic ring-stacking and hydrogen bonding** rather than extensive disulfide crosslinking. The gene is polymorphic in sheep, with variants that alter a tyrosine residue (p.Tyr34Asn) and that sit within a chromosomal region linked to wool fibre diameter.

---

## Key Findings

### Finding 1 — KRTAP8-1 is a sheep high-glycine-tyrosine (HGT) keratin-associated protein (historically "HGT type I-F")

The identity and classification of the target protein are firmly established. UniProt P02448 (KRTAP8-1; synonyms "Component 0.62," "HGT keratin component F," "Keratin high-tyrosine matrix protein") belongs to the **KRTAP type 8 family**. The KAP superfamily is conventionally divided into three chemical classes based on amino acid composition: the **high-sulphur (HS)** KAPs, the **ultra-high-sulphur (UHS)** KAPs, and the **high-glycine-tyrosine (HGT)** KAPs. KAP8 is a member of the HGT class ([PMID: 25279319](https://pubmed.ncbi.nlm.nih.gov/25279319/)).

Crucially, the historical nomenclature links the modern gene symbol directly to the UniProt alias. A 1994 linkage study explicitly equated KRTAP8 with "high-glycine-tyrosine type I-F" — the exact historical name corresponding to the UniProt alias "HGT keratin component F" ([PMID: 7518411](https://pubmed.ncbi.nlm.nih.gov/7518411/)). This chain of evidence resolves the mandatory gene-identity verification: the gene symbol matches the protein description, the organism is sheep (*Ovis aries*), and the HGT family/domain assignment aligns with the literature. A related ovine KAP8 member (notional KAP8-2) has been described as a 63-residue protein rich in glycine and tyrosine with low cysteine, reinforcing the family's compositional signature ([PMID: 25279319](https://pubmed.ncbi.nlm.nih.gov/25279319/)).

> *"KAPs can be divided into three groups: the high sulphur (HS) KAPs, the ultra-high sulphur (UHS) KAPs and the high glycine-tyrosine (HGT) KAPs. KAP8 is a HGT-KAP family"* — [PMID: 25279319](https://pubmed.ncbi.nlm.nih.gov/25279319/)

> *"two high-glycine-tyrosine class genes, KRTAP6 (previously high-glycine-tyrosine type II) and KRTAP8 (previously high-glycine-tyrosine type I-F)"* — [PMID: 7518411](https://pubmed.ncbi.nlm.nih.gov/7518411/)

### Finding 2 — KRTAP8-1/KAP8.1 binds the head domain of type II keratin K85 and organizes intermediate filaments in the orthocortex

The most direct mechanistic evidence for KRTAP8-1 function comes from in vitro binding and structural studies of KAP8.1. Using a combination of Western blotting, isothermal titration calorimetry, circular dichroism, and transmission electron microscopy (TEM), researchers demonstrated that **KAP8.1 binds the head domain of the trichocyte keratin K85** — a type II keratin — and that this head domain is helically aligned around the axis of the intermediate filament ([PMID: 23791804](https://pubmed.ncbi.nlm.nih.gov/23791804/)). From these binding data and TEM observations of bundled filament complexes formed in vitro, the authors proposed that the helical arrangement of IFs uniquely found in the orthocortex (distributed on the convex side of the curved fibre) is regulated by KAP8.1.

A key property of HGT-KAPs revealed in the same work is **bidirectional binding**: HGT KAPs can interact in more than one direction (the study also detected interaction with the desmoplakin C-terminus, DPCT-C), and this bidirectional binding capacity contributes to the mechanical robustness of the fibre ([PMID: 23791804](https://pubmed.ncbi.nlm.nih.gov/23791804/)). More generally, KAPs infiltrate the space between intermediate filaments and are recognized as having especially important roles in organizing IFs into macrofibrils, in determining the fibre's hardness, toughness, and pliability, and in cross-linking IFs to one another ([PMID: 29797269](https://pubmed.ncbi.nlm.nih.gov/29797269/)).

> *"KAP8.1 binds to the head domain of K85, which is helically aligned around the axis of the intermediate filament (IF). … we propose that the helical arrangement of IFs found in the orthocortex, which is uniquely distributed on the convex fiber side of the hair, is regulated by KAP8.1"* — [PMID: 23791804](https://pubmed.ncbi.nlm.nih.gov/23791804/)

> *"The KAPs, which infiltrate the space between the IF, are recognized as having especially important roles in the organisation of the IF into macrofibrils, in determining some of the most important physical attributes of the fully-keratinised hair fibre, including its hardness, toughness and pliability, and in linking IF to one another"* — [PMID: 29797269](https://pubmed.ncbi.nlm.nih.gov/29797269/)

### Finding 3 — KRTAP8-1 localizes to the orthocortex of the hair/wool cortex and influences fibre curvature/crimp

The spatial localization of the protein reinforces its structural role. Immunohistochemistry using an anti-KAP8.1 monoclonal antibody showed that **KAP8.1 is predominantly expressed in discrete regions of the keratinizing zone of the hair shaft cortex**, and this protein distribution paralleled the distribution of KAP8.1 mRNA — leading the authors to propose that KAP8.1 plays a role in controlling hair curvature ([PMID: 30125694](https://pubmed.ncbi.nlm.nih.gov/30125694/)).

Proteomic comparisons of straight (crimp-mutant) versus wild-type crimpy wool support this interpretation at the whole-fibre level. In straight-fibre mutants, several HGT-class proteins normally associated with the orthocortex — specifically the **KAP6, KAP7, and KAP8 families** — are reduced in abundance ([PMID: 34859500](https://pubmed.ncbi.nlm.nih.gov/34859500/)). This both places KAP8 in the orthocortex and directly ties its abundance to fibre curvature. Developmentally, the HGT-KAP genes are the **first sub-group of KAP genes expressed in the wool follicle**, coming on just after the keratin genes ([PMID: 22044071](https://pubmed.ncbi.nlm.nih.gov/22044071/)), consistent with a role in laying down the early scaffold of the cortical matrix.

> *"KAP8.1 was predominantly expressed in discrete regions of the keratinizing zone of the hair shaft cortex. The protein expression patterns paralleled the distribution of KAP8.1 mRNA and suggested that KAP8.1 plays a role associated with cells to control hair curvature"* — [PMID: 30125694](https://pubmed.ncbi.nlm.nih.gov/30125694/)

> *"the reduced abundance of some proteins in the high glycine-tyrosine class normally associated with the orthocortex, specifically the KAP6, KAP7, and KAP8 families"* — [PMID: 34859500](https://pubmed.ncbi.nlm.nih.gov/34859500/)

### Finding 4 — KRTAP8-1 is polymorphic in sheep, with variants affecting a tyrosine residue, and relies on non-disulfide interactions

KRTAP8-1 shows genetic variation in sheep populations. PCR-SSCP screening of 250 Romney-cross sheep identified **five KRTAP8-1 sequence variants** in an amplicon spanning the entire coding region, with four SNPs (three in the coding region); one nonsynonymous SNP is predicted to produce the amino-acid change **p.Tyr34Asn** ([PMID: 22044071](https://pubmed.ncbi.nlm.nih.gov/22044071/)). Because tyrosine is central to the aromatic-interaction chemistry of HGT-KAPs, substitution of a tyrosine for a non-aromatic asparagine is plausibly functionally relevant.

The chemistry of the HGT-KAP class is cysteine-poor. A newly characterised ovine HGT-KAP was reported to contain 63.2 mol% glycine + tyrosine and **no cysteine at all**, leading the authors to propose that intra- and inter-strand stabilization in such proteins occurs through **ring-stacking and hydrogen bonding** rather than disulfide bonds ([PMID: 31717789](https://pubmed.ncbi.nlm.nih.gov/31717789/)). KRTAP8-1 itself contains only four cysteines (see Finding 6), so while it can form a limited number of disulfides, non-covalent aromatic and hydrogen-bond interactions dominate its packing against keratins. Classical linkage mapping placed the HGT loci (KRTAP6/KRTAP8) within a chromosomal region linked to **wool fibre diameter**, raising the possibility that genetic variation here affects a commercially important fibre trait ([PMID: 7516629](https://pubmed.ncbi.nlm.nih.gov/7516629/)).

> *"contains a high proportion (63.2 mol%) of glycine and tyrosine, but would not contain any cysteine. This suggests that other forms of intra- and inter-strand interaction may occur with this KAP, such as interactions via ring-stacking and hydrogen-bonding"* — [PMID: 31717789](https://pubmed.ncbi.nlm.nih.gov/31717789/)

> *"High-glycine-tyrosine proteins (KRTAP6, 7 and 8) are known to vary considerably in abundance in wool fibres and it is possible that a gene for major effect on fibre diameter is located within the same chromosomal region as KRTAP6 and KRTAP8"* — [PMID: 7516629](https://pubmed.ncbi.nlm.nih.gov/7516629/)

### Finding 5 — HGT proteins (including KAP8) are deposited preferentially on the orthocortical side of the follicle, underpinning bilateral asymmetry and crimp

The wool cortex contains three cell types: **orthocortex, mesocortex, and paracortex**. In fine Merino fibres, the ortho- and paracortex segregate bilaterally, with the paracortex positioned on the concave side of the crimp wave. In situ hybridization in the developing follicle showed that sulphur-rich (HS/UHS) proteins are initially expressed on the **paracortical** side, whereas **proteins high in glycine and tyrosine (the HGT / KAP8 class) are initially expressed on the orthocortical side** ([PMID: 17697142](https://pubmed.ncbi.nlm.nih.gov/17697142/)). The same study established that the paracortex has a higher cysteine concentration than the orthocortex, defining the chemical asymmetry (HGT-rich orthocortex vs cysteine-rich paracortex) that mechanically produces crimp.

This bilateral deposition pattern complements the proteomic observation that KAP8 is reduced in straight crimp-mutant wool ([PMID: 34859500](https://pubmed.ncbi.nlm.nih.gov/34859500/)): removing or reducing the orthocortical HGT matrix collapses the ortho/para asymmetry and straightens the fibre.

> *"proteins high in glycine and tyrosine tend to be expressed initially on the orthocortical side of the follicle"* — [PMID: 17697142](https://pubmed.ncbi.nlm.nih.gov/17697142/)

> *"the paracortex has a higher concentration of cysteine than the orthocortex"* — [PMID: 17697142](https://pubmed.ncbi.nlm.nih.gov/17697142/)

### Finding 6 — Direct sequence analysis of P02448: a 62-residue, charge-depleted, Gly/Tyr/aromatic-rich peptide with four cysteines

Direct analysis of the canonical UniProt P02448 sequence (62 aa; protein-level evidence, PE=1) quantifies the compositional signature that defines the protein's behaviour:

```
MSYCFSSTVFPGCYWGSYGYPLGYSVGCGYGSTYSPVGYGFGYGYNGSGAFGCRRFWPFALY
```

| Property | Value |
|---|---|
| Length | 62 residues |
| Glycine | 14 residues (22.6 mol%) |
| Tyrosine | 11 residues (17.7 mol%) |
| **Gly + Tyr combined** | **40.3 mol%** |
| Total aromatic (Y + F + W) | 19 residues (30.6 mol%) |
| Serine | ~12.9 mol% |
| Charged residues (R+K+D+E) | 3.2 mol% (2 Arg; no Asp/Glu/Lys) |
| Cysteine | 4 residues (6.5 mol%) at positions 4, 13, 28, 53 |

Position 34 is a tyrosine, exactly matching the experimentally reported **p.Tyr34Asn** polymorphism ([PMID: 22044071](https://pubmed.ncbi.nlm.nih.gov/22044071/)). The near-complete absence of acidic and lysine residues means the protein carries essentially no net charge beyond a small basic contribution from two arginines, so electrostatics play little role in its interactions — consistent with a matrix protein that packs against keratins via hydrophobic/aromatic contacts and hydrogen bonds rather than charge-charge pairing.

### Finding 7 — Modular architecture: a tandem Gly-aromatic repeat core flanked by cysteine anchors and a short basic C-terminus

Motif analysis of P02448 reveals a clear modular design. The sequence contains seven Gly-[Tyr/Phe] dipeptide motifs (six Gly-Tyr, one Gly-Phe) plus four Tyr-Gly motifs, concentrated in a **central tandem glycine-aromatic repeat domain** (e.g., the …PVGYGFGYGY… stretch). The four cysteines are distributed at positions 4 and 13 (an N-terminal pair) and at positions 28 and 53, flanking and punctuating the Gly/Tyr-rich core and providing covalent anchor points. The only charged residues form a short **basic C-terminal tail** (…GCRRFWPFALY).

Consistent with this repetitive, low-complexity architecture, **no experimental 3-D structure exists for P02448, and no AlphaFold DB model is available** (the entry returns a 404). This is in keeping with reviews noting that little is known about KAP three-dimensional structure and that KAPs likely adopt a variety of energetically similar conformations in vivo, with only local structural regularity ([PMID: 29797269](https://pubmed.ncbi.nlm.nih.gov/29797269/)). In other words, KRTAP8-1 is best understood not as a folded globular protein but as a flexible, partly disordered "molecular glue" whose repeating aromatic motifs intercalate between keratin filaments.

> *"Little, however, is known about their three-dimensional structures, though modelling has indicated that some local structural regularity is likely to exist. Current data suggest that the KAPs in vivo may adopt a variety of energetically-similar conformations"* — [PMID: 29797269](https://pubmed.ncbi.nlm.nih.gov/29797269/)

---

## Mechanistic Model / Interpretation

The findings integrate into a coherent, self-consistent mechanistic model of KRTAP8-1 as a **structural matrix protein that builds and shapes the wool orthocortex**.

**Molecular level.** KRTAP8-1 is a small, flexible, charge-free peptide dominated by glycine and aromatic residues. Its central Gly-Tyr/Gly-Phe repeat domain acts as a pliable "glue" that intercalates into the space between keratin intermediate filaments, making extensive **aromatic ring-stacking and hydrogen-bond contacts** with the filaments. The four cysteines provide a limited number of covalent **disulfide anchors**, and the short basic C-terminal tail offers a localized interaction motif. Unlike the high-sulphur KAPs (which are rich in cysteine and crosslink heavily via disulfides, dominating the paracortex), KRTAP8-1 depends mainly on non-covalent interactions.

**Filament level.** KAP8.1 binds the **head domain of the type II keratin K85**, which winds helically around the IF axis. By docking onto this helical track and by exploiting **bidirectional binding**, HGT-KAPs organize adjacent IFs into the helically packed macrofibril arrangement that is the structural hallmark of the orthocortex, contributing to the fibre's mechanical strength, toughness, and pliability.

**Cellular / tissue level.** During follicle differentiation, HGT-KAP genes (including KRTAP8-1) switch on early, immediately after the keratin genes, and the protein is deposited preferentially on the **orthocortical** side of the fibre. Because the sulphur-rich KAPs are laid down on the opposite (paracortical) side, the fibre develops a **bilateral ortho/para chemical and structural asymmetry**. The orthocortex and paracortex have different mechanical/swelling properties, and this side-by-side asymmetry causes the fibre to bend — producing **crimp (curvature)**. Reducing HGT-KAP (KAP8) abundance collapses this asymmetry and straightens the fibre.

```
            WOOL FOLLICLE (differentiating cortical cells)
   +----------------------------------------------------------+
   |  Early:  keratin genes  ->  HGT-KAP genes (KRTAP8-1) ...  |
   +----------------------------------------------------------+
                              | deposition
                              v
     ORTHOCORTEX (convex side)            PARACORTEX (concave side)
   +---------------------------+        +---------------------------+
   | HGT-KAPs: KAP6/7/8         |        | HS / UHS KAPs (Cys-rich)  |
   | KRTAP8-1 (Gly/Tyr, low Cys)|        | heavy disulfide crosslink |
   | aromatic ring-stacking     |        |                           |
   | helically packed IFs       |        | denser packing            |
   +---------------------------+        +---------------------------+
                 \                         /
                  \   bilateral asymmetry /
                   v                      v
                     +------------------+
                     |   FIBRE CRIMP     |
                     |  (curvature)      |
                     +------------------+

   Molecular detail:
   K85 head domain (helical around IF) -- bound by -- KAP8.1
   KRTAP8-1 core:  ...Gly-Tyr-Gly-Phe-Gly-Tyr...  (ring-stacking glue)
   Cys4 - Cys13 - Cys28 - Cys53  (disulfide anchors)
   C-terminus: ...Cys-Arg-Arg-Phe-Trp-Pro-Phe-Ala-Leu-Tyr (basic motif)
```

**Where it acts.** The protein performs its structural role **intracellularly** while cortical cells differentiate and keratinize, and then persists as an insoluble matrix component of the mature, dead fibre. It is not secreted into the extracellular space in the conventional sense; rather, it becomes part of the cytoplasmic keratin–KAP composite that fills the cortical cell.

**What it is NOT.** KRTAP8-1 has no catalytic activity (not an enzyme), no transport function, and no signaling role. Its only "pathway" is the structural assembly pathway of trichocyte keratinization. Broad pleiotropic effects attributed to the locus (e.g., associations with fibre diameter) are secondary consequences of its structural role, not independent functions.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [23791804](https://pubmed.ncbi.nlm.nih.gov/23791804/) | *Bidirectional binding property of HGT KAP contributes to mechanical strength and shape of hair* | **Primary mechanistic evidence**: KAP8.1 binds K85 head domain; organizes helical IFs; bidirectional binding → mechanical robustness |
| [30125694](https://pubmed.ncbi.nlm.nih.gov/30125694/) | *Structural behavior of KAP8.1 in human hair revealed by a monoclonal antibody* | **Localization**: KAP8.1 in keratinizing cortex; role in hair curvature |
| [34859500](https://pubmed.ncbi.nlm.nih.gov/34859500/) | *Wool fiber curvature correlated with abundance of K38 and specific KAPs* | **Functional link**: KAP8 family reduced in straight fibres; orthocortex association |
| [17697142](https://pubmed.ncbi.nlm.nih.gov/17697142/) | *Differential expression of proteins in cortical cells of wool and hair* | **Spatial deposition**: HGT proteins on orthocortical side; para/ortho cysteine asymmetry |
| [22044071](https://pubmed.ncbi.nlm.nih.gov/22044071/) | *Variation in ovine KAP7-1 and KAP8-1 genes (PCR-SSCP)* | **Polymorphism + timing**: 5 KRTAP8-1 variants, p.Tyr34Asn; HGT-KAPs expressed first |
| [31717789](https://pubmed.ncbi.nlm.nih.gov/31717789/) | *Ovine KAP rich in Gly/Tyr but lacking cysteine* | **Interaction chemistry**: ring-stacking and hydrogen-bonding in cysteine-poor HGT-KAPs |
| [25279319](https://pubmed.ncbi.nlm.nih.gov/25279319/) | *The sheep KAP8-2 gene, a new KAP8 family member absent in humans* | **Classification**: KAP8 is HGT-KAP; family compositional signature |
| [7518411](https://pubmed.ncbi.nlm.nih.gov/7518411/) | *Linkage between KRTAP genes and growth hormone in sheep* | **Nomenclature**: KRTAP8 = "high-glycine-tyrosine type I-F" (= UniProt "component F") |
| [7516629](https://pubmed.ncbi.nlm.nih.gov/7516629/) | *Linkage between HGT keratin gene loci and wool fibre diameter* | **Trait linkage**: HGT cluster (KRTAP6/8) linked to fibre diameter |
| [29797269](https://pubmed.ncbi.nlm.nih.gov/29797269/) | *Trichocyte Keratin-Associated Proteins (KAPs)* (review) | **Framework**: general KAP matrix role; limited 3-D structural knowledge; multiple conformations |

**Consistency of the evidence.** Multiple independent lines — in vitro binding/biophysics ([PMID: 23791804](https://pubmed.ncbi.nlm.nih.gov/23791804/)), immunohistochemistry ([PMID: 30125694](https://pubmed.ncbi.nlm.nih.gov/30125694/)), proteomics of crimp mutants ([PMID: 34859500](https://pubmed.ncbi.nlm.nih.gov/34859500/)), developmental in situ hybridization ([PMID: 17697142](https://pubmed.ncbi.nlm.nih.gov/17697142/)), genetics ([PMID: 22044071](https://pubmed.ncbi.nlm.nih.gov/22044071/), [PMID: 7516629](https://pubmed.ncbi.nlm.nih.gov/7516629/)), and direct sequence analysis — all point in the same direction and do not contradict one another. The convergence across experimental modalities gives high confidence in the structural-matrix interpretation.

**A caveat on orthology.** The most detailed binding and antibody studies ([PMID: 23791804](https://pubmed.ncbi.nlm.nih.gov/23791804/), [PMID: 30125694](https://pubmed.ncbi.nlm.nih.gov/30125694/)) were performed on **human hair KAP8.1**, whereas the target is the **sheep** ortholog. The family conservation, shared HGT chemistry, and consistent orthocortical localization make cross-species inference reasonable, but strictly speaking, K85-head-domain binding has not been demonstrated for the sheep protein directly.

---

## Limitations and Knowledge Gaps

1. **No direct 3-D structure.** There is no experimental structure of KRTAP8-1, and no AlphaFold model is available for P02448. The proposed flexible/partly disordered architecture is inferred from sequence composition and from general KAP reviews, not from a solved structure.

2. **Species gap for the binding data.** The pivotal K85-head-domain binding and bidirectional-binding experiments were conducted on **human** KAP8.1. Direct demonstration that sheep KRTAP8-1 binds the ovine K85 (or its ovine homolog) is lacking.

3. **Functional consequence of the p.Tyr34Asn polymorphism is untested.** Although a Tyr→Asn substitution removes an aromatic ring central to the proposed interaction chemistry, no study has measured its effect on binding, fibre structure, or a wool phenotype.

4. **Correlative, not causal, links to crimp.** The association of KAP8 abundance with curvature rests on proteomic correlation in crimp mutants and on localization. No gene-knockout or knockdown of KRTAP8-1 specifically has been performed in sheep to prove causality.

5. **Disulfide bonding pattern unknown.** The four cysteines could form intramolecular disulfides, intermolecular crosslinks to keratins or other KAPs, or remain partly free. The actual bonding topology has not been determined.

6. **Quantitative stoichiometry and in-fibre organization.** The precise copy number of KRTAP8-1 per IF, its distribution relative to other orthocortical KAPs, and whether it has preferred binding partners beyond K85 remain unquantified.

---

## Proposed Follow-up Experiments / Actions

1. **Direct ovine binding assays.** Express recombinant sheep KRTAP8-1 (P02448) and the ovine K85 head domain; measure binding by ITC/SPR and visualize bundled-filament complexes by TEM — replicating the human KAP8.1 study in the native species.

2. **Variant functional assay.** Produce the p.Tyr34Asn variant and compare its keratin-binding affinity and in vitro filament-bundling capacity to wild-type, testing whether loss of an aromatic ring weakens matrix interactions.

3. **Structural characterization.** Apply circular dichroism, NMR, and/or solid-state NMR to recombinant KRTAP8-1 to determine the extent of disorder, any local secondary structure in the Gly-aromatic repeat, and the disulfide bonding pattern.

4. **Spatially resolved proteomics / imaging.** Use anti-KRTAP8-1 antibodies or MS imaging on ortho- vs paracortex microdissections across crimp phases to quantify the protein's bilateral gradient directly in sheep fibre.

5. **Genotype–phenotype association study.** Genotype the five known KRTAP8-1 variants in a large, phenotyped flock and test associations with crimp/curvature, fibre diameter, and mechanical properties, adjusting for neighbouring KRTAPs.

6. **Comparative genomics.** Map the full ovine KAP8 locus and compare across breeds differing in crimp to identify regulatory or copy-number variation affecting KRTAP8-1 expression.

---

## Conclusion

Sheep **KRTAP8-1 (P02448)** is a small structural high-glycine-tyrosine keratin-associated protein, not an enzyme, transporter, or signaling molecule. It functions **intracellularly within keratinizing wool cortical cells**, where it is deposited early and preferentially on the **orthocortical** side, binds trichocyte keratin intermediate filaments (notably the **head domain of type II keratin K85**), and organizes them into helically packed macrofibrils via **aromatic ring-stacking and hydrogen-bond "glue" chemistry** supplemented by a few disulfide anchors. In so doing it contributes to fibre mechanical strength and to the bilateral ortho/paracortex asymmetry that generates **wool crimp and curvature**.


## Artifacts

- [OpenScientist final report](KRTAP8-1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](KRTAP8-1-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:25279319
2. PMID:7518411
3. PMID:23791804
4. PMID:29797269
5. PMID:30125694
6. PMID:34859500
7. PMID:22044071
8. PMID:31717789
9. PMID:7516629
10. PMID:17697142