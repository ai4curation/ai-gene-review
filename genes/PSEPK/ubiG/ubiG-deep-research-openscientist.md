---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T17:53:42.953601'
end_time: '2026-07-18T19:27:41.905162'
duration_seconds: 5638.95
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: ubiG
  gene_symbol: ubiG
  uniprot_accession: Q88M10
  protein_description: 'RecName: Full=Ubiquinone biosynthesis O-methyltransferase
    {ECO:0000255|HAMAP-Rule:MF_00472}; AltName: Full=2-polyprenyl-6-hydroxyphenol
    methylase {ECO:0000255|HAMAP-Rule:MF_00472}; EC=2.1.1.222 {ECO:0000255|HAMAP-Rule:MF_00472};
    AltName: Full=3-demethylubiquinone 3-O-methyltransferase {ECO:0000255|HAMAP-Rule:MF_00472};
    EC=2.1.1.64 {ECO:0000255|HAMAP-Rule:MF_00472};'
  gene_info: Name=ubiG {ECO:0000255|HAMAP-Rule:MF_00472}; OrderedLocusNames=PP_1765;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the methyltransferase superfamily. UbiG/COQ3
  protein_domains: SAM-dependent_MTases_sf. (IPR029063); UbiG_MeTrfase. (IPR010233);
    Methyltransf_23 (PF13489)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 13
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: ubiG-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ubiG-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88M10
- **Protein Description:** RecName: Full=Ubiquinone biosynthesis O-methyltransferase {ECO:0000255|HAMAP-Rule:MF_00472}; AltName: Full=2-polyprenyl-6-hydroxyphenol methylase {ECO:0000255|HAMAP-Rule:MF_00472}; EC=2.1.1.222 {ECO:0000255|HAMAP-Rule:MF_00472}; AltName: Full=3-demethylubiquinone 3-O-methyltransferase {ECO:0000255|HAMAP-Rule:MF_00472}; EC=2.1.1.64 {ECO:0000255|HAMAP-Rule:MF_00472};
- **Gene Information:** Name=ubiG {ECO:0000255|HAMAP-Rule:MF_00472}; OrderedLocusNames=PP_1765;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the methyltransferase superfamily. UbiG/COQ3
- **Key Domains:** SAM-dependent_MTases_sf. (IPR029063); UbiG_MeTrfase. (IPR010233); Methyltransf_23 (PF13489)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ubiG" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ubiG' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ubiG** (gene ID: ubiG, UniProt: Q88M10) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *ubiG* (Q88M10, PP_1765) — Ubiquinone Biosynthesis O-Methyltransferase in *Pseudomonas putida* KT2440

## Summary

The gene **ubiG** (UniProt **Q88M10**; ordered locus **PP_1765**) of *Pseudomonas putida* strain KT2440 encodes **ubiquinone biosynthesis O-methyltransferase**, a **S-adenosyl-L-methionine (SAM)-dependent methyltransferase** of the **UbiG/COQ3 family** within the Class I methyltransferase superfamily. Its defining and best-supported function is **bifunctional O-methylation** in the biosynthesis of **coenzyme Q (ubiquinone, UQ)**: a single UbiG polypeptide catalyzes **both** of the two O-methylation steps of the pathway. The first (EC 2.1.1.222) methylates the C6-hydroxyl of 2-polyprenyl-6-hydroxyphenol to give 2-polyprenyl-6-methoxyphenol; the second and terminal step (EC 2.1.1.64) methylates 3-demethylubiquinone to yield mature ubiquinone. In both reactions, SAM is the methyl donor and S-adenosyl-L-homocysteine (SAH) is the byproduct.

UbiG operates in the **cytoplasm**, acting as a **soluble/peripheral membrane protein at the inner (cytoplasmic) face of the plasma membrane**, where its lipophilic polyprenyl-quinone substrates reside. It is not a firmly integral membrane protein; rather, a unique structural insertion mediates transient membrane-lipid interaction that also gates access to the SAM-binding pocket. Functionally, UbiG works within a large **soluble multiprotein "Ubi metabolon"** that sequesters the hydrophobic pathway intermediates and channels them through the last six reactions of UQ biosynthesis. Its two methylation reactions are **oxygen-independent** and are therefore shared by both the aerobic (O₂-dependent) and anaerobic (O₂-independent) branches of the ubiquinone pathway found in proteobacteria.

The product of the pathway, **ubiquinone**, is the central **lipid-soluble electron carrier of the aerobic respiratory electron transport chain**, making UbiG essential for respiratory energy metabolism. This annotation is assigned with **high confidence by strong orthology** to the experimentally characterized *Escherichia coli* UbiG and its eukaryotic counterpart Coq3, and is codified in the HAMAP rule MF_00472. No *P. putida*-specific biochemical study of PP_1765 currently exists; the functional narrative below is built on the extensive *E. coli*/yeast literature for direct orthologs, together with structural, genetic, and physiological evidence.

---

## Gene/Protein Identity Verification

Before presenting the functional narrative, the mandatory identity check was completed and **passed**. There is no wrong-gene concern: the gene symbol, protein description, EC numbers, family, and domains all coherently describe the ubiquinone biosynthesis O-methyltransferase.

| Criterion | UniProt reference (Q88M10) | Literature consensus | Match? |
|---|---|---|---|
| Gene symbol | *ubiG* | *ubiG* is the canonical name for the UQ biosynthesis O-methyltransferase | ✔ |
| Protein description | Ubiquinone biosynthesis O-methyltransferase; 2-polyprenyl-6-hydroxyphenol methylase; 3-demethylubiquinone 3-O-methyltransferase | Matches the bifunctional O-methyltransferase characterized in *E. coli* | ✔ |
| EC numbers | EC 2.1.1.222 and EC 2.1.1.64 | The two O-methylation steps of UQ biosynthesis | ✔ |
| Organism | *P. putida* KT2440 (a Gammaproteobacterium) | UQ pathway is conserved across Gammaproteobacteria including *Pseudomonas* | ✔ |
| Protein family | Methyltransferase superfamily, UbiG/COQ3 | UbiG/Coq3 O-methyltransferase family | ✔ |
| Key domains | SAM-dependent MTase (IPR029063); UbiG MeTrfase (IPR010233); PF13489 | Class I SAM-dependent MTase fold confirmed by crystallography | ✔ |

The one caveat is that all **direct experimental characterization derives from orthologs** (chiefly *E. coli* UbiG and yeast/rat Coq3), not from the *P. putida* protein itself. Because HAMAP rule MF_00472 governs this assignment and the pathway is deeply conserved in Gammaproteobacteria, the orthology-based annotation is robust. UbiG is ~40% identical to yeast Coq3 and is functionally interchangeable with it ([PMID: 8703953](https://pubmed.ncbi.nlm.nih.gov/8703953/)).

---

## Key Findings

### Finding 1 — UbiG is a bifunctional SAM-dependent O-methyltransferase catalyzing both O-methylation steps of ubiquinone biosynthesis

The core function of UbiG is unambiguously established by direct biochemistry in the *E. coli* ortholog. Purified *E. coli* UbiG was shown to catalyze **both** O-methylation steps of coenzyme Q biosynthesis in vitro — a single polypeptide performs two chemically distinct methyl transfers on different substrates. As Poon et al. state, "In addition, E. coli UbiGp was purified and found to catalyze both O-methylation steps" ([PMID: 10419476](https://pubmed.ncbi.nlm.nih.gov/10419476/)). This bifunctionality is not merely inferred from sequence: it was demonstrated enzymatically with the purified protein.

Cross-species complementation reinforces this. When the *E. coli* UbiG polypeptide is targeted to the mitochondria of a yeast *coq3* mutant, it restores respiratory competence. Hsu et al. established both the identity and the role of the enzyme: "The second O-methylation step in E. coli, the conversion of demethylubiquinone to ubiquinone, is carried out by the UbiG methyltransferase, which is 40% identical in amino acid sequence with the yeast Coq3 methyltransferase" ([PMID: 8703953](https://pubmed.ncbi.nlm.nih.gov/8703953/)).

The methyl donor is **S-adenosyl-L-methionine**. Early enzymology on the membrane-associated methyltransferase demonstrated that "S-Adenosyl-L-methionine was active as the methyl donor for the reaction" ([PMID: 769831](https://pubmed.ncbi.nlm.nih.gov/769831/)), consistent with the Class I SAM-dependent methyltransferase fold.

Per HAMAP rule MF_00472, the two reactions catalyzed by UbiG are:

- **EC 2.1.1.222** — the earlier step: methylation of the C6-hydroxyl of **2-polyprenyl-6-hydroxyphenol** → **2-polyprenyl-6-methoxyphenol**.
- **EC 2.1.1.64** — the terminal step: methylation of **3-demethylubiquinone** → **ubiquinone (coenzyme Q)**.

The two acceptors are chemically similar aromatic hydroxyls positioned at early and late points of the pathway, which explains how a single active site can handle both. Note that UbiG performs the two **O**-methylations only; the intervening **C**-methylation of the pathway is carried out by a separate enzyme, UbiE. *P. putida* Q88M10 (PP_1765) is a HAMAP-ruled ortholog in the UbiG/COQ3 family (SAM-dependent MTase superfamily, InterPro IPR010233), so these activities are assigned to the *P. putida* protein by direct orthology.

### Finding 2 — UbiG is a peripheral membrane protein acting at the cytoplasmic face, with a membrane-binding insertion that gates methyl-donor access

The subcellular location of UbiG activity is well defined. Classic enzymology showed the methyltransferase is **not firmly membrane-bound** but has affinity for the cell membrane, and concluded that "in vivo, the methyltransferase reaction probably occurs at the internal surface of the cytoplasmic membrane" — i.e., the **cytoplasmic (inner) face** of the *E. coli* plasma membrane ([PMID: 769831](https://pubmed.ncbi.nlm.nih.gov/769831/)). This makes biological sense: the polyprenyl-quinone substrates are lipophilic and partition into the membrane, while the catalytic machinery must reach them from the cytoplasmic side.

The eukaryotic ortholog behaves analogously. Using antibodies to yeast Coq3p, "the Coq3 polypeptide is peripherally associated with the matrix-side of the inner membrane of yeast mitochondria" ([PMID: 10419476](https://pubmed.ncbi.nlm.nih.gov/10419476/)) — the topological equivalent of the bacterial cytoplasmic face.

Structural biology provides the mechanistic explanation. UbiG adopts a **classic Class I SAM-dependent methyltransferase fold**, established when the *E. coli* enzyme was crystallized and shown to diffract to 2.0 Å ([PMID: 21636923](https://pubmed.ncbi.nlm.nih.gov/21636923/)). A subsequent structural study revealed that "UbiG possesses a unique sequence insertion between β4 and α10, which is used for membrane lipid interaction. Interestingly, this sequence insertion also covers the methyl donor binding pocket" ([PMID: 26975567](https://pubmed.ncbi.nlm.nih.gov/26975567/)). This couples membrane binding to catalysis: association with the lipid bilayer reorganizes the insertion so that the SAM/SAH-binding pocket becomes accessible, effectively **gating methyl-donor entry** upon membrane docking. Truncating or loosening this region increases SAH binding affinity, confirming the coupling. In this way a largely water-soluble enzyme is able to methylate lipophilic, membrane-proximal substrates.

### Finding 3 — UbiG functions within a multiprotein Ubi complex (soluble metabolon) and depends on upstream UbiX/UbiD

UbiG does not act as an isolated enzyme. In *E. coli*, "seven Ubi proteins form the Ubi complex, a stable metabolon that catalyzes the last six reactions of the UQ biosynthetic pathway in Escherichia coli" ([PMID: 30686758](https://pubmed.ncbi.nlm.nih.gov/30686758/)). This ~1-MDa cytoplasmic assembly uses the SCP2 lipid-binding domain of UbiJ to sequester the hydrophobic UQ intermediates, allowing the otherwise membrane-partitioning substrates to be processed in the **soluble/cytoplasmic fraction** rather than in the membrane itself. This metabolon architecture explains how a "membrane-associated" pathway can nonetheless proceed largely in the cytoplasm, and it provides a physical scaffold that positions UbiG next to the other tailoring enzymes. The role of the UbiJ–UbiK subcomplex within this metabolon has been further characterized structurally ([PMID: 36142227](https://pubmed.ncbi.nlm.nih.gov/36142227/); [PMID: 38710096](https://pubmed.ncbi.nlm.nih.gov/38710096/)).

UbiG's activity is also functionally dependent on upstream flavin-handling enzymes. Genetic work showed that a *ubiG* mutant strain (IS16) has a Q-deficient phenotype: "Complementation of IS16 with either ubiG or ubiX(K-12) reverses this phenotype, suggesting that UbiX may interact with UbiG" ([PMID: 16923914](https://pubmed.ncbi.nlm.nih.gov/16923914/)). Biochemically, a *ubiX* deletion strain "accumulates 4-hydroxy-3-octaprenyl-benzoate, and has reduced UbiG O-methyltransferase activity" ([PMID: 17889824](https://pubmed.ncbi.nlm.nih.gov/17889824/)). Because UbiX (with UbiD) performs the decarboxylation that generates the substrate feeding into the O-methylation/hydroxylation cycle, loss of UbiX starves UbiG of its correct substrate and depresses its measured activity — evidence that UbiG operates downstream in an ordered, interdependent pathway.

### Finding 4 — UbiG's product, ubiquinone, is the central lipid electron carrier of aerobic respiration; loss of UbiG causes Q deficiency and respiratory defects

The physiological purpose of UbiG is to make ubiquinone, without which respiration is compromised. The authoritative review of bacterial coenzyme Q biology states that ubiquinone "functions in the respiratory electron transport chain and plays a pivotal role in energy generating processes" ([PMID: 24480387](https://pubmed.ncbi.nlm.nih.gov/24480387/)). The *ubi* genes — including *ubiG* — are required for Q production in *E. coli*, and *ubi* mutants show respiratory/growth phenotypes on non-fermentable carbon sources.

Because UbiG performs two of the essential steps, loss of UbiG blocks completion of ubiquinone: without it, the two O-methylation steps cannot proceed and Q biosynthesis fails ([PMID: 10419476](https://pubmed.ncbi.nlm.nih.gov/10419476/)). Evolutionarily, ubiquinone is a **high-redox-potential quinone** whose emergence "is believed to be an adaptive response to this environmental transition" — the shift to an aerobic lifestyle in Gammaproteobacteria, the clade that includes *Pseudomonas* ([PMID: 31767748](https://pubmed.ncbi.nlm.nih.gov/31767748/)). For an obligately aerobic organism such as *P. putida* KT2440, UbiG-dependent ubiquinone production is therefore central to bioenergetics, and reduced ubiquinol additionally serves as a lipid-soluble antioxidant.

### Finding 5 — UbiG's O-methylation steps are shared across the aerobic and anaerobic ubiquinone biosynthesis routes

Proteobacteria maintain ubiquinone synthesis across the entire oxygen range. Ubiquinone is the molecule by which, in respiratory metabolism, "electrons are shuttled from reduced substrates to terminal electron acceptors" ([PMID: 31289180](https://pubmed.ncbi.nlm.nih.gov/31289180/)). Under oxic conditions, an O₂-dependent set of hydroxylases (UbiI/UbiH/UbiF) installs the ring hydroxyls; under anoxia, these are replaced by an O₂-independent set (UbiT/UbiU/UbiV) ([PMID: 31289180](https://pubmed.ncbi.nlm.nih.gov/31289180/); [PMID: 32409583](https://pubmed.ncbi.nlm.nih.gov/32409583/)). Crucially, the **methyltransferase steps — including both UbiG O-methylations and the UbiE C-methylation — are common to both routes**, because their chemistry (SAM-dependent methyl transfer) does not require molecular oxygen ([PMID: 24480387](https://pubmed.ncbi.nlm.nih.gov/24480387/)).

Thus UbiG is a **constitutive, branch-independent core enzyme** of the pathway — a single methyltransferase serving both the aerobic and anaerobic modes of Q biosynthesis. For a metabolically versatile bacterium like *P. putida*, this positions UbiG at both an early (first O-methylation) and the terminal (final O-methylation) tailoring step of the common pathway core, independent of oxygen availability.

---

## Mechanistic Model / Interpretation

Putting the findings together, UbiG (PP_1765) is the shared O-methylating enzyme of the ubiquinone biosynthesis pathway. Coenzyme Q biosynthesis in Gammaproteobacteria proceeds by decorating a polyprenylated aromatic ring through an alternating series of decarboxylation, hydroxylation, and methylation reactions. UbiG contributes the two O-methyl groups; UbiE contributes the intervening C-methyl group.

### Position of UbiG's two reactions in the pathway

```
                         4-hydroxy-3-polyprenyl-benzoate (from chorismate / 4-hydroxybenzoate)
                                        │  UbiX/UbiD (decarboxylation)
                                        ▼
                         2-polyprenylphenol
                                        │  UbiI/UbiH/UbiF (O2 route)  OR  UbiT/UbiU/UbiV (anoxic route)
                                        ▼
                         2-polyprenyl-6-hydroxyphenol
                                        │  ◄── UbiG  (EC 2.1.1.222, FIRST O-methylation)   [SAM → SAH]
                                        ▼
                         2-polyprenyl-6-methoxyphenol
                                        │  further hydroxylation + C-methylation (UbiE) + hydroxylation
                                        ▼
                         3-demethylubiquinone
                                        │  ◄── UbiG  (EC 2.1.1.64, SECOND / TERMINAL O-methylation)   [SAM → SAH]
                                        ▼
                            ★  UBIQUINONE (Coenzyme Q)  ★
                                        │
                                        ▼
                     Respiratory electron transport chain (mobile lipid electron carrier)
```

### The two reactions catalyzed by the one enzyme

| Feature | First O-methylation | Second (terminal) O-methylation |
|---|---|---|
| EC number | 2.1.1.222 | 2.1.1.64 |
| Substrate | 2-polyprenyl-6-hydroxyphenol | 3-demethylubiquinone |
| Product | 2-polyprenyl-6-methoxyphenol | Ubiquinone |
| Methyl donor / byproduct | SAM / SAH | SAM / SAH |
| Position in pathway | Early | Final |

### Spatial and organizational model

```
        CYTOPLASM  (site of catalysis)
   ┌───────────────────────────────────────────────┐
   │   ~1-MDa soluble Ubi metabolon                 │
   │   ┌──────────────────────────────────────┐     │
   │   │ UbiJ (SCP2) binds hydrophobic         │     │
   │   │ polyprenyl-quinone intermediates ─────┼──►  UbiG methylates (x2)
   │   │ + UbiE, UbiH/I/F (or U/V/T), UbiG ... │     │      using SAM
   │   └──────────────────────────────────────┘     │
   │        ▲ peripheral docking of UbiG            │
   │        │ (β4–α10 insertion binds lipid,        │
   │========│=gates SAM pocket)=====================│  INNER (cytoplasmic) leaflet
   │////////▼///////////////////////////////////////│  PLASMA MEMBRANE
   └───────────────────────────────────────────────┘
                 PERIPLASM / OUTSIDE
```

UbiG is a **peripheral, cytoplasm-facing** enzyme. It docks transiently to the membrane through a β4–α10 sequence insertion; this docking simultaneously exposes the SAM-binding pocket, so methyl-donor access is coupled to membrane engagement. In vivo, however, most of the pathway operates as a **soluble metabolon** in which UbiJ's SCP2 domain solubilizes the lipophilic substrates, enabling processing in the cytoplasmic compartment. UbiG's two reactions are oxygen-independent and therefore identical in the aerobic and anaerobic branches; only the hydroxylation steps differ between routes. The end product, ubiquinone, is delivered to the membrane where it serves as the mobile electron carrier of the respiratory chain — the physiological reason UbiG is essential.

For *P. putida* KT2440 specifically, all of this is inferred from orthology (HAMAP MF_00472) to *E. coli* UbiG and yeast/rat Coq3. The 40% sequence identity between UbiG and Coq3, the conserved Class I MTase fold, the conserved domain architecture (IPR010233), and the deep conservation of the *ubi* operon across Gammaproteobacteria make this a high-confidence assignment.

---

## Evidence Base

| PMID | Study (abbrev.) | Contribution to annotation | Evidence type |
|---|---|---|---|
| [10419476](https://pubmed.ncbi.nlm.nih.gov/10419476/) | Poon et al. 1999 — Coq3/UbiG catalyze both O-methylation steps | Purified UbiG catalyzes **both** O-methylations in vitro; Coq3 peripheral to matrix side of inner membrane | Direct biochemistry; immunolocalization |
| [8703953](https://pubmed.ncbi.nlm.nih.gov/8703953/) | Hsu et al. 1996 — complementation of yeast *coq3* by *E. coli* UbiG | UbiG restores respiration; ~40% identity to Coq3; carries out demethyl-UQ → UQ | In vivo cross-species complementation |
| [769831](https://pubmed.ncbi.nlm.nih.gov/769831/) | Leppik et al. 1976 — membrane-associated methyltransferase | SAM is the methyl donor; reaction at internal (cytoplasmic) surface of membrane | Classic enzymology |
| [21636923](https://pubmed.ncbi.nlm.nih.gov/21636923/) | Xing et al. 2011 — crystallization of *E. coli* UbiG | UbiG catalyzes two O-methyl transfers; 2.0 Å crystals; Class I MTase fold | Structural (crystallography) |
| [26975567](https://pubmed.ncbi.nlm.nih.gov/26975567/) | Zhu et al. 2016 — methyl-donor recognition | β4–α10 insertion binds lipid and covers SAM pocket; membrane binding gates methyl-donor access | Structural / mechanistic |
| [30686758](https://pubmed.ncbi.nlm.nih.gov/30686758/) | Hajj Chehade et al. 2019 — soluble metabolon | Seven Ubi proteins form a stable ~1-MDa cytoplasmic metabolon (last six reactions) | Biochemistry / complex isolation |
| [16923914](https://pubmed.ncbi.nlm.nih.gov/16923914/) | Gulmezian et al. 2006 — UbiG–UbiX genetic interaction | *ubiG*/*ubiX* both complement a Q-deficient mutant → functional interaction | Genetics |
| [17889824](https://pubmed.ncbi.nlm.nih.gov/17889824/) | Gulmezian et al. 2007 — role of UbiX | *ubiX* deletion reduces UbiG O-methyltransferase activity; substrate accumulation | Genetics / biochemistry |
| [24480387](https://pubmed.ncbi.nlm.nih.gov/24480387/) | Aussel et al. 2014 — review of bacterial coenzyme Q | Ubiquinone is the respiratory electron carrier; *ubi* genes required; methyltransferases O₂-independent | Authoritative review |
| [31289180](https://pubmed.ncbi.nlm.nih.gov/31289180/) | Pelosi et al. 2019 — UQ biosynthesis over the O₂ range | O₂-dependent vs O₂-independent hydroxylase sets; methylation steps shared | Biochemistry / genetics |
| [32409583](https://pubmed.ncbi.nlm.nih.gov/32409583/) | Vo et al. 2020 — O₂-independent UQ pathway (UbiT/U/V) | Anaerobic hydroxylase branch; methyltransferases common to both | Genetics |
| [31767748](https://pubmed.ncbi.nlm.nih.gov/31767748/) | Anand et al. 2019 — high-redox-potential quinones | Ubiquinone as an aerobic adaptation in Gammaproteobacteria | Evolutionary / adaptive |
| [36142227](https://pubmed.ncbi.nlm.nih.gov/36142227/) | Functional role of UbiJ–UbiK | Metabolon subcomplex architecture supporting cytosolic UQ synthesis | Structural |
| [38710096](https://pubmed.ncbi.nlm.nih.gov/38710096/) | Structural reconstruction of the Ubi complex | Further structural detail of the soluble metabolon | Structural |

**How the evidence converges:** The direct-biochemistry papers ([PMID: 10419476](https://pubmed.ncbi.nlm.nih.gov/10419476/), [PMID: 769831](https://pubmed.ncbi.nlm.nih.gov/769831/)) and the complementation study ([PMID: 8703953](https://pubmed.ncbi.nlm.nih.gov/8703953/)) establish the enzymatic function beyond doubt for the ortholog. The structural work ([PMID: 21636923](https://pubmed.ncbi.nlm.nih.gov/21636923/), [PMID: 26975567](https://pubmed.ncbi.nlm.nih.gov/26975567/)) explains the fold, the SAM dependence, and the membrane coupling. The metabolon and genetics papers place UbiG within its pathway context and physical assembly. The reviews and O₂-range studies define the physiological and evolutionary significance. None of the evidence is contradictory; the only limitation is that all of it concerns orthologs rather than PP_1765 directly.

---

## Supported and Refuted Hypotheses

**Supported:**

- **H1** — *ubiG* encodes a SAM-dependent O-methyltransferase of ubiquinone biosynthesis. **Supported** by multiple lines of direct biochemistry and orthology.
- **H2** — UbiG is bifunctional, catalyzing both O-methylation steps. **Supported** ([PMID: 10419476](https://pubmed.ncbi.nlm.nih.gov/10419476/); [PMID: 8703953](https://pubmed.ncbi.nlm.nih.gov/8703953/)).
- **H3** — UbiG acts as a peripheral protein at the cytoplasmic membrane face and within a soluble metabolon. **Supported** ([PMID: 769831](https://pubmed.ncbi.nlm.nih.gov/769831/); [PMID: 30686758](https://pubmed.ncbi.nlm.nih.gov/30686758/); [PMID: 26975567](https://pubmed.ncbi.nlm.nih.gov/26975567/)).

**Refuted / revised:**

- The classic view that Q biosynthesis is strictly a membrane-embedded process was **revised** by the demonstration of a soluble cytoplasmic Ubi metabolon ([PMID: 30686758](https://pubmed.ncbi.nlm.nih.gov/30686758/)). UbiG is best described as membrane-**associated/peripheral** rather than integral.

No wrong-gene concern was found: the *ubiG* symbol, family, domains, and reactions are internally consistent and match a large, unambiguous literature.

---

## Limitations and Knowledge Gaps

1. **No *P. putida*-specific characterization.** There is no published biochemical, structural, or genetic study of PP_1765 (Q88M10) itself. Every functional claim rests on orthology to *E. coli* UbiG and yeast/rat Coq3, codified by HAMAP MF_00472. While this is a high-confidence inference (conserved family, domains, and operon context), a formal knock-out or in vitro assay in *P. putida* KT2440 has not been reported.

2. **Substrate isoprenoid tail length not verified in *P. putida*.** *E. coli* makes UQ-8 (octaprenyl tail); *Pseudomonas* species predominantly make UQ-9 (nonaprenyl tail). The polyprenyl chain length of UbiG's physiological substrates in *P. putida* is therefore inferred, not measured — though the O-methylation chemistry on the aromatic ring is independent of tail length, so UbiG substrate recognition is expected to be unchanged.

3. **Metabolon composition in *P. putida* is assumed.** The seven-protein Ubi metabolon and the UbiJ SCP2 solubilization mechanism were characterized in *E. coli*. Whether *P. putida* assembles an identical complex (and the identity of its UbiJ/UbiK counterparts) has not been experimentally confirmed.

4. **Kinetic parameters and regulation unknown.** No K_m, k_cat, or substrate-specificity constants are available for the *P. putida* enzyme, and any strain-specific regulation of *ubiG* expression is uncharacterized.

5. **Aerobic vs anaerobic branch usage in *P. putida*.** *P. putida* KT2440 is an aerobe; the extent to which it deploys the O₂-independent (UbiT/U/V) branch, and thus the conditions under which UbiG operates in each mode, is not directly established for this strain.

---

## Proposed Follow-up Experiments / Actions

1. **Targeted gene knockout / complementation in *P. putida* KT2440.** Delete PP_1765 and assay for ubiquinone deficiency (LC-MS quantification of UQ-9) and respiratory/growth defects on non-fermentable carbon sources; complement with PP_1765 and, as a cross-species control, with *E. coli ubiG* to confirm conserved function.

2. **In vitro enzymology of recombinant PP_1765.** Express and purify the *P. putida* protein and demonstrate both O-methylation activities (EC 2.1.1.222 and EC 2.1.1.64) with SAM as donor, measuring SAH production and determining kinetic parameters for both substrates.

3. **Quinone profiling.** Confirm the isoprenoid chain length of the physiological substrate/product (UQ-9 expected) by mass spectrometry, and monitor accumulation of the demethylated intermediate (3-demethylubiquinone) in a *ubiG* mutant.

4. **Structural / membrane-association validation.** Solve or model the *P. putida* UbiG structure (AlphaFold + experimental validation) to verify the Class I MTase fold and the β4–α10 membrane-binding insertion; test membrane/lipid binding and its effect on SAM/SAH affinity.

5. **Metabolon reconstitution.** Determine whether PP_1765 co-purifies with the *P. putida* orthologs of UbiJ/UbiK/UbiE/UbiH etc., to test whether the soluble Ubi metabolon is conserved in this organism.

6. **Oxygen-regime physiology.** Test *ubiG* essentiality and UQ synthesis under oxic vs microaerobic/anoxic conditions to confirm that the O-methylation steps are shared across both hydroxylase branches in *P. putida*.

---

## Conclusion

*ubiG* (Q88M10, PP_1765) of *Pseudomonas putida* KT2440 encodes the **bifunctional, SAM-dependent O-methyltransferase of coenzyme Q (ubiquinone) biosynthesis**. A single UbiG polypeptide catalyzes both O-methylation steps — the early conversion of 2-polyprenyl-6-hydroxyphenol to its 6-methoxy product (EC 2.1.1.222) and the terminal conversion of 3-demethylubiquinone to ubiquinone (EC 2.1.1.64) — using S-adenosyl-L-methionine as the methyl donor. It functions in the cytoplasm as a peripheral, membrane-docking enzyme at the inner face of the plasma membrane and operates within a soluble multiprotein Ubi metabolon, with its oxygen-independent chemistry shared by both the aerobic and anaerobic ubiquinone routes. Its product, ubiquinone, is the central lipid electron carrier of the respiratory chain, making UbiG essential for aerobic respiratory energy metabolism. The annotation is assigned with high confidence by orthology (HAMAP MF_00472) to the experimentally characterized *E. coli* UbiG and eukaryotic Coq3, as no *P. putida*-specific study yet exists.


## Artifacts

- [OpenScientist final report](ubiG-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ubiG-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:8703953
2. PMID:10419476
3. PMID:21636923
4. PMID:26975567
5. PMID:30686758
6. PMID:36142227
7. PMID:38710096
8. PMID:16923914
9. PMID:17889824
10. PMID:24480387
11. PMID:31767748
12. PMID:31289180
13. PMID:32409583