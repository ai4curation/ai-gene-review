---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T11:39:03.509703'
end_time: '2026-08-31T11:58:09.775311'
duration_seconds: 1146.27
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: rbsK
  gene_symbol: rbsK
  uniprot_accession: Q88K34
  protein_description: 'RecName: Full=Ribokinase {ECO:0000256|ARBA:ARBA00016943, ECO:0000256|HAMAP-Rule:MF_01987};
    Short=RK {ECO:0000256|HAMAP-Rule:MF_01987}; EC=2.7.1.15 {ECO:0000256|ARBA:ARBA00012035,
    ECO:0000256|HAMAP-Rule:MF_01987};'
  gene_info: Name=rbsK {ECO:0000256|HAMAP-Rule:MF_01987, ECO:0000313|EMBL:AAN68070.1};
    OrderedLocusNames=PP_2458 {ECO:0000313|EMBL:AAN68070.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the carbohydrate kinase pfkB family.
  protein_domains: Carboh/pur_kinase_PfkB_CS. (IPR002173); PfkB_dom. (IPR011611);
    Ribo/fructo_kinase. (IPR002139); Ribokinase. (IPR011877); Ribokinase-like. (IPR029056)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 13
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: rbsK-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: rbsK-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88K34
- **Protein Description:** RecName: Full=Ribokinase {ECO:0000256|ARBA:ARBA00016943, ECO:0000256|HAMAP-Rule:MF_01987}; Short=RK {ECO:0000256|HAMAP-Rule:MF_01987}; EC=2.7.1.15 {ECO:0000256|ARBA:ARBA00012035, ECO:0000256|HAMAP-Rule:MF_01987};
- **Gene Information:** Name=rbsK {ECO:0000256|HAMAP-Rule:MF_01987, ECO:0000313|EMBL:AAN68070.1}; OrderedLocusNames=PP_2458 {ECO:0000313|EMBL:AAN68070.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the carbohydrate kinase pfkB family.
- **Key Domains:** Carboh/pur_kinase_PfkB_CS. (IPR002173); PfkB_dom. (IPR011611); Ribo/fructo_kinase. (IPR002139); Ribokinase. (IPR011877); Ribokinase-like. (IPR029056)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "rbsK" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'rbsK' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **rbsK** (gene ID: rbsK, UniProt: Q88K34) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *rbsK* (Ribokinase, PP_2458 / UniProt Q88K34) in *Pseudomonas putida* KT2440

## Summary

The gene **rbsK** (ordered locus **PP_2458**; UniProt **Q88K34**) of *Pseudomonas putida* KT2440 encodes **ribokinase (RK; EC 2.7.1.15)**, a cytoplasmic sugar kinase of the **PfkB carbohydrate-kinase superfamily**. Its primary and defining biochemical function is the **ATP-dependent phosphorylation of D-ribose to D-ribose-5-phosphate**, releasing ADP. This is the committed, essentially irreversible first intracellular step of D-ribose catabolism: it traps free ribose entering the cell in a charged, membrane-impermeant phosphorylated form and channels it into central carbon and nucleotide metabolism. The enzyme requires **Mg²⁺** (to coordinate the ATP phosphates, forming the true Mg·ATP donor) and is **activated by a monovalent cation, most effectively K⁺** — a mechanistic hallmark of the ribokinase branch of the PfkB family.

The product, **D-ribose-5-phosphate (R5P)**, is a hub metabolite. It enters the **non-oxidative pentose phosphate pathway** and, via phosphoribosyl pyrophosphate synthetase (PRPS), becomes **5-phospho-α-D-ribose-1-diphosphate (PRPP)** — the universal precursor for de novo and salvage synthesis of purine and pyrimidine nucleotides, and for the biosynthesis of histidine and tryptophan. RbsK therefore sits at the junction between carbohydrate uptake and the building blocks of nucleic acids.

In *P. putida* KT2440 specifically, PP_2458 is embedded in a complete, contiguous **ribose-utilization operon** (PP_2454–PP_2460: *rbsB-rbsA-rbsC-rbsR-rbsK-rbsD* plus an adjacent ribonucleoside hydrolase). This genomic context places RbsK immediately downstream of the **RbsBAC high-affinity ABC ribose importer** and the **RbsD ribose pyranase/anomerase**, defining a coherent import-and-activate module in the cytoplasm. Direct enzymatic assay of the *P. putida* protein has not been published (UniProt evidence level PE=3, "inferred from homology"); however, the annotation is strongly supported by (i) ortholog biochemistry and crystallography from *E. coli*, *Vibrio cholerae* and *Arabidopsis thaliana*, and (ii) sequence analysis performed during this investigation showing **41.4% identity to biochemically characterized *E. coli* ribokinase** with **full conservation of every catalytic and cofactor-binding motif**, including the general-base aspartate (Asp254).

### Gene-identity verification (mandatory check)

All required verification steps pass. (1) The gene symbol **"rbsK"** is the canonical bacterial ribokinase gene name (as in the *E. coli rbsDACBK* operon) and matches the UniProt ribokinase description. (2) The organism is confirmed as *Pseudomonas putida* KT2440 (PP_2458); orthologs used for functional inference are clearly labeled as such. (3) The PfkB/ribokinase-family literature aligns with the InterPro domains listed for Q88K34 (IPR011877 Ribokinase; IPR002139 Ribo/fructokinase; IPR011611 PfkB domain; IPR029056 Ribokinase-like fold; IPR002173 PfkB conserved site). (4) No conflicting literature for a different "rbsK" was found. This report describes the correct protein.

---

## Key Findings

### Finding 1 — RbsK is a ribokinase catalyzing D-ribose + ATP → D-ribose-5-phosphate + ADP (EC 2.7.1.15)

The core function of the gene product is unambiguous at the level of enzyme class. UniProt Q88K34 annotates PP_2458 as ribokinase (EC 2.7.1.15) under HAMAP curation rule MF_01987, and this reaction is one of the best-characterized in carbohydrate metabolism across orthologs. The enzyme transfers the γ-phosphate of ATP to the 5-hydroxyl of D-ribose, producing D-ribose-5-phosphate and ADP.

The reaction stoichiometry is stated directly in the structural literature: *"Ribokinase (RK) is one of the principal enzymes in carbohydrate metabolism, catalyzing the reaction of D-ribose and adenosine triphosphate to produce ribose-5-phosphate and adenosine diphosphate (ADP)"* ([PMID: 25084391](https://pubmed.ncbi.nlm.nih.gov/25084391/)). The classic *E. coli* enzyme study similarly confirms substrate, product, and cofactor requirements: *"Ribokinase phosphorylates ribose to form ribose-5-phosphate in the presence of ATP and magnesium"* ([PMID: 9385653](https://pubmed.ncbi.nlm.nih.gov/9385653/)).

The reaction is catalytically efficient in characterized orthologs — recombinant *E. coli* ribokinase reached a specific activity of roughly **75 µmol/min/mg** ([PMID: 16784868](https://pubmed.ncbi.nlm.nih.gov/16784868/)). Crystallographic ternary complexes captured with ribose plus ATP (or ATP analogs) and with product/ADP have defined the transferred phosphoryl group and the catalytic geometry ([PMID: 25084391](https://pubmed.ncbi.nlm.nih.gov/25084391/); [PMID: 30822455](https://pubmed.ncbi.nlm.nih.gov/30822455/); [PMID: 9385653](https://pubmed.ncbi.nlm.nih.gov/9385653/)). This is the **primary and defining activity** of the gene product.

### Finding 2 — Cofactor requirements and substrate specificity: Mg²⁺, K⁺ activation, and strict D-stereospecificity

Ribokinase catalysis has two well-defined ionic requirements that are diagnostic of the enzyme. First, a **divalent metal (Mg²⁺, or Mn²⁺)** is required to coordinate the ATP phosphates and stabilize the transition state — the true phosphoryl donor is Mg·ATP. Second, and characteristically for this enzyme, a **monovalent cation** is essential for maximal activity, with a strong preference for **potassium**. The definitive substrate-specificity study reports: *"Catalytic activity of RK: (i) is strongly dependent on the presence of monovalent cations (potassium >>> ammonium > cesium), and (ii) is cooperatively enhanced by divalent magnesium and manganese ions"* ([PMID: 16784868](https://pubmed.ncbi.nlm.nih.gov/16784868/)). The K⁺ ion binds near the active site and orders a loop that positions the catalytic ("anion hole") machinery — a structural feature shared across the ribokinase subfamily of PfkB kinases.

Regarding substrate scope, D-ribose is the preferred and physiological substrate, but the enzyme phosphorylates several other D-sugars *in vitro* (2-deoxy-D-ribose, and less efficiently D-arabinose, D-xylose, and D-fructose) when supplied with ATP, K⁺ and Mg²⁺. Crucially, the enzyme is **strictly D-stereospecific**: *"L-ribose and L-arabinose are not substrates for the recombinant enzyme"* ([PMID: 16784868](https://pubmed.ncbi.nlm.nih.gov/16784868/)). This D-specificity reflects the geometry of the sugar-binding pocket and confirms that the physiological role is catabolism of naturally occurring D-pentoses.

### Finding 3 — PfkB superfamily membership, homodimeric quaternary structure, and cytoplasmic localization

RbsK belongs to the **PfkB family of carbohydrate kinases**, a group united by a conserved α/β "ribokinase-like" fold and characteristic sequence motifs. InterPro assigns Q88K34 to this family through multiple signatures: IPR002139 (ribokinase/fructokinase), IPR011877 (ribokinase), IPR011611 (PfkB domain), IPR029056 (ribokinase-like fold), and IPR002173 (PfkB conserved site). The family assignment is established in the foundational structural paper: *"Ribokinase belongs to the PfkB family of carbohydrate kinases, for which no three-dimensional structure is currently known"* — a statement from the 1997 study that first crystallized the *E. coli* enzyme ([PMID: 9385653](https://pubmed.ncbi.nlm.nih.gov/9385653/)).

The enzyme functions as a **homodimer**. Solution biophysical measurements on *E. coli* ribokinase directly demonstrate this: the authors *"give evidence from light-scattering and gel filtration studies that the protein forms a dimer in solution"* ([PMID: 9385653](https://pubmed.ncbi.nlm.nih.gov/9385653/)). Each protomer carries the canonical ribokinase fold with a small β-sheet "lid" that closes over the sugar-binding site upon substrate binding (induced fit). Structures of orthologs from *Arabidopsis thaliana* ([PMID: 30822455](https://pubmed.ncbi.nlm.nih.gov/30822455/)) and *Vibrio cholerae* ([PMID: 25084391](https://pubmed.ncbi.nlm.nih.gov/25084391/)) have been captured in multiple ligation states (apo, ATP-binary, and ribose+ATP-ternary), confirming the conserved architecture and lid closure.

As a soluble metabolic enzyme with no signal peptide, transmembrane segment, or lipidation signal, RbsK carries out its function in the **cytoplasm**, consistent with its role acting on ribose that has already been imported across the inner membrane by the RbsBAC ABC transporter. HAMAP rule MF_01987 assigns cytoplasmic subcellular localization.

### Finding 4 — RbsK performs the committed step of D-ribose catabolism, feeding R5P into the pentose phosphate pathway and PRPP-dependent biosynthesis

The biological purpose of RbsK is to commit imported D-ribose to metabolism. In the canonical *E. coli* system, ribose transport and initial metabolism are encoded together: *"The genes for the transport and initial-step metabolism of D-ribose form a single rbsDACBK operon. RbsABC forms the ABC-type high-affinity D-ribose transporter, while RbsD and RbsK are involved in the conversion of D-ribose into D-ribose 5-phosphate"* ([PMID: 23651393](https://pubmed.ncbi.nlm.nih.gov/23651393/)). RbsD interconverts the pyranose and furanose anomers of ribose, presenting the correct form to RbsK for phosphorylation.

The product R5P is a central metabolic node. Its fate is described directly: *"The phosphorylated sugar can enter the pentose phosphate pathway or be used for the synthesis of nucleotides, histidine, and tryptophan"* ([PMID: 9385653](https://pubmed.ncbi.nlm.nih.gov/9385653/)). More specifically, R5P is the direct precursor of **5-phosphoribosyl-1-pyrophosphate (PRPP)**, which is used for both de novo and salvage synthesis of nucleotides — a role emphasized across the pentose-phosphate biochemistry literature: R5P *"is the direct precursor of 5-phosphoribosyl-1-pyrophosphate, for both de novo and 'salvage' synthesis of nucleotides"* ([PMID: 16519676](https://pubmed.ncbi.nlm.nih.gov/16519676/); see also [PMID: 16893570](https://pubmed.ncbi.nlm.nih.gov/16893570/)). By phosphorylating ribose, RbsK both prevents efflux of the free sugar and supplies this biosynthetic precursor pool. In *P. putida* — a bacterium that preferentially catabolizes organic acids and aromatics — this route enables the use of ribose (including ribose liberated by nucleoside catabolism) as a carbon/energy source and as a biosynthetic building block.

### Finding 5 — Sequence-level confirmation: 41.4% identity to *E. coli* RbsK with full conservation of all catalytic motifs

Because no direct enzymatic assay of the *P. putida* protein exists (UniProt PE=3), this investigation performed a rigorous sequence analysis to confirm functional identity. A global Needleman–Wunsch alignment of Q88K34 (302 aa) against the biochemically characterized *E. coli* ribokinase (P0A9J6/RbsK, 309 aa) gives **41.4% identity over 301 aligned positions** — well within the range that reliably indicates conserved enzymatic function for this family.

Critically, **every diagnostic ribokinase/PfkB motif is conserved** in Q88K34:

| Motif | Function | Q88K34 residues | *E. coli* equivalent |
|-------|----------|-----------------|----------------------|
| **GGKGANQAV** | Glycine-rich PfkB nucleotide/sugar-binding fingerprint | 39–47 | GGKGANQAV (identical) |
| **NPAPAT** | Anion-hole / phosphate-binding motif | 164–169 | NPAPA (conserved) |
| **TPNESEAE** | Catalytic loop | 184–191 | TPNETEAE (conserved) |
| **AAGDTFIGGF** | GAGDTF signature carrying catalytic base + di-Gly anion hole | 251–260 | catalytic Asp255 (conserved) |

Within the GAGDTF signature, the **general-base aspartate (Asp254)** — which deprotonates the ribose 5-OH for in-line phosphoryl transfer and aligns to *E. coli* Asp255 — is present, immediately followed by the **di-glycine anion-hole element (Gly258/Gly259)**. The conservation of the catalytic base plus the full complement of substrate- and cofactor-binding motifs makes the ribokinase assignment for Q88K34 essentially certain by sequence, even in the absence of a direct assay. Ortholog structural/mutational work supports the same catalytic-residue mechanism: *"ATP-dependent ribokinase (RBSK) phosphorylates ribose to ribose-5'-phosphate"* ([PMID: 30822455](https://pubmed.ncbi.nlm.nih.gov/30822455/)). This is the strongest protein-specific evidence available for the *P. putida* enzyme.

### Finding 6 — In *P. putida* KT2440, PP_2458 lies within a complete, contiguous ribose-utilization operon

Genomic context in the target organism reinforces the pathway role — directly in *P. putida* KT2440, not merely by orthology. KEGG places PP_2458 (rbsK, ortholog **K00852**, EC 2.7.1.15; genome coordinates ~2,805,226–2,806,134) in the pentose phosphate pathway map (ppu00030). Its immediate neighbors, all on the same strand, form a coherent ribose regulon:

| Locus | Gene | Product | Approx. coordinates |
|-------|------|---------|---------------------|
| PP_2454 | *rbsB* | Periplasmic ribose-binding protein | 2,800,658–2,801,617 |
| PP_2455 | *rbsA* | ABC transporter ATP-binding subunit | 2,801,617–2,803,191 |
| PP_2456 | *rbsC* | ABC transporter permease | 2,803,188–2,804,183 |
| PP_2457 | *rbsR* | LacI-type transcriptional repressor | 2,804,188–2,805,210 |
| **PP_2458** | ***rbsK*** | **Ribokinase (EC 2.7.1.15) — this protein** | **2,805,226–2,806,134** |
| PP_2459 | *rbsD* | Ribose pyranase / anomerase | 2,806,131–2,806,529 (overlaps *rbsK*) |
| PP_2460 | *nuh* | Ribonucleoside hydrolase | 2,806,627–2,807,595 |

The overlap between the *rbsK* stop and *rbsD* start codons and the contiguous arrangement are consistent with operonic co-transcription. This mirrors the canonical *E. coli rbsDACBK* organization ([PMID: 23651393](https://pubmed.ncbi.nlm.nih.gov/23651393/)) and assembles a self-contained ribose-scavenging module: **RbsBAC** imports extracellular D-ribose, **RbsD** interconverts the ribopyranose/ribofuranose anomers, **RbsK** phosphorylates D-ribose to R5P (the committed step), the adjacent **ribonucleoside hydrolase (Nuh)** supplies intracellular ribose from nucleoside breakdown ([PMID: 16519676](https://pubmed.ncbi.nlm.nih.gov/16519676/); [PMID: 16893570](https://pubmed.ncbi.nlm.nih.gov/16893570/)), and **RbsR** (LacI-type) provides ribose-inducible transcriptional control. This places rbsK's activity firmly in the cytoplasm, immediately downstream of the RbsBAC importer.

---

## Mechanistic Model / Interpretation

The findings converge on a clear, coherent model of RbsK as the metabolic gatekeeper for ribose in *P. putida* KT2440.

```
   EXTRACELLULAR / PERIPLASM              INNER MEMBRANE                 CYTOPLASM
   ─────────────────────────    ───────────────────────────   ───────────────────────────────

     D-ribose (free sugar)
          │
          │ captured by
          ▼
     RbsB (PP_2454)  ────────►  RbsC permease (PP_2456)
   periplasmic binding prot.    RbsA ATPase  (PP_2455)  ──►   D-ribose (cytoplasmic pool)
                                 [ABC importer, ATP-driven]            │
                                                                       │  RbsD (PP_2459)
                                                                       │  pyranase/anomerase
                                                                       ▼  (pyranose → furanose)
                                                              ┌───────────────────────────┐
   Nucleosides ──► free ribose ────────────────────────────► │  RbsK  (PP_2458)          │
   (via Nuh, PP_2460, ribonucleoside hydrolase)              │  RIBOKINASE, EC 2.7.1.15  │
                                                              │  D-ribose + ATP           │
                                                              │     │ Mg²⁺, K⁺            │
                                                              │     ▼                     │
                                                              │  D-ribose-5-P + ADP       │
                                                              └───────────┬───────────────┘
                                                                          │
                        ┌─────────────────────────────────────────────────┼───────────────────────┐
                        ▼                                                   ▼                       ▼
             Non-oxidative Pentose                              PRPP (via PRPS)          Central carbon
             Phosphate Pathway  ──► F6P, GAP                    │                        (energy/biomass)
             (glycolytic entry)                     ┌───────────┼──────────────┐
                                                     ▼           ▼              ▼
                                              Purine/pyrimidine  Histidine   Tryptophan
                                              nucleotides        biosynthesis biosynthesis
                                              (de novo + salvage)
```

**Catalytic chemistry.** Asp254 acts as a general base, deprotonating the ribose 5′-hydroxyl, which then performs an in-line nucleophilic attack on the γ-phosphate of Mg·ATP held in the anion hole. The monovalent cation (K⁺) orders the catalytic loop; the di-glycine element and NPAPA motif stabilize the developing negative charge in the transition state. This mechanism is conserved across the ribokinase family and inferred for Q88K34 from full active-site conservation.

**Why phosphorylation is the committed step.** Free ribose is membrane-permeant and can be lost from the cell; ribose-5-phosphate, being charged, is trapped intracellularly. By consuming ATP, RbsK makes the reaction thermodynamically favorable and effectively irreversible, committing the carbon skeleton to metabolism — the classic "kinase trap" logic shared with hexokinase and other sugar kinases.

**Regulatory layer.** The LacI-family repressor **RbsR (PP_2457)** encoded within the same cluster couples expression of the whole module to ribose availability, ensuring the transporter and kinase are made only when ribose is present — an economical arrangement typical of inducible sugar catabolic operons.

**Metabolic significance.** R5P is not merely a catabolic intermediate — it is the entry point to PRPP and hence to all nucleotide biosynthesis. RbsK therefore serves a dual purpose: it allows ribose (and ribose liberated from nucleosides by Nuh) to be used as a carbon and energy source, and it replenishes the R5P/PRPP pool required for growth. The centrality of R5P/PRPP for nucleotide supply is echoed even in eukaryotic systems, where R5P availability governs PRPP synthesis and proliferation ([PMID: 31253668](https://pubmed.ncbi.nlm.nih.gov/31253668/); [PMID: 2432883](https://pubmed.ncbi.nlm.nih.gov/2432883/)).

---

## Evidence Base

| PMID | Paper (abbrev.) | Organism / system | How it supports the annotation |
|------|-----------------|-------------------|--------------------------------|
| [9385653](https://pubmed.ncbi.nlm.nih.gov/9385653/) | *Purification, characterization, and crystallization of E. coli ribokinase* (Sigrell et al., 1997) | *E. coli* | Defines reaction (ribose + ATP + Mg → R5P), PfkB family membership, homodimer, and downstream fate of R5P (PPP, nucleotides, His, Trp). Foundational reference. |
| [16784868](https://pubmed.ncbi.nlm.nih.gov/16784868/) | *Ribokinase from E. coli: expression, purification, and substrate specificity* (Chuvikovsky et al., 2006) | *E. coli* | Establishes K⁺ monovalent-cation dependence, Mg²⁺/Mn²⁺ enhancement, high specific activity, D-sugar substrate scope, and strict D-stereospecificity (L-sugars not substrates). |
| [25084391](https://pubmed.ncbi.nlm.nih.gov/25084391/) | *Crystallization and preliminary X-ray analysis of ribokinase from V. cholerae* (Paul et al., 2014) | *V. cholerae* | States exact reaction stoichiometry; ternary-complex crystallography confirming catalytic geometry. |
| [30822455](https://pubmed.ncbi.nlm.nih.gov/30822455/) | *Crystal structure and mutational analyses of ribokinase from A. thaliana* (Kang et al., 2019) | *A. thaliana* | Structural + mutational validation of the conserved catalytic mechanism inferred for Q88K34; confirms ribose → R5P activity. |
| [23651393](https://pubmed.ncbi.nlm.nih.gov/23651393/) | *Involvement of RbsR in regulation of purine nucleotide synthesis* (Shimada et al., 2013) | *E. coli* | Defines *rbsDACBK* operon organization (transporter + RbsD + RbsK) mirrored by PP_2454–2460; ties RbsK to R5P production and RbsR regulation. |
| [16519676](https://pubmed.ncbi.nlm.nih.gov/16519676/) | *Pentose phosphates in nucleoside interconversion and catabolism* (Tozzi et al., 2006) | Review | Establishes R5P as the direct precursor of PRPP for de novo and salvage nucleotide synthesis; context for the Nuh–RbsK link. |
| [16893570](https://pubmed.ncbi.nlm.nih.gov/16893570/) | *Methods for determination of intracellular ribose phosphates* (Camici et al., 2006) | Review | Reinforces R5P → PRPP biosynthetic role and nucleoside phosphorolysis as an alternative ribose-phosphate source. |
| [31253668](https://pubmed.ncbi.nlm.nih.gov/31253668/) | *Cell-cycle phosphorylation of PRPS1* (2019) | Human | Illustrates broad importance of R5P → PRPP for nucleotide supply (analogy, not direct evidence for RbsK). |
| [2432883](https://pubmed.ncbi.nlm.nih.gov/2432883/) | *PRPP and PRPP synthetase in rat mammary gland* (1986) | Rat | Shows R5P availability controls PRPP synthesis (analogy for downstream significance). |

**Note on non-relevant hits.** Several PubMed results retrieved during the investigation concern *P. putida* KT2440 in the context of xenobiotic/aromatic degradation, bioremediation, or high-throughput fitness/annotation studies (e.g., [PMID: 32443190](https://pubmed.ncbi.nlm.nih.gov/32443190/), [PMID: 36528203](https://pubmed.ncbi.nlm.nih.gov/36528203/), [PMID: 31924622](https://pubmed.ncbi.nlm.nih.gov/31924622/), [PMID: 38323821](https://pubmed.ncbi.nlm.nih.gov/38323821/)). These mention KT2440 but do not address rbsK/ribokinase directly and were not used to support functional claims.

---

## Supported and Refuted Hypotheses

| Hypothesis | Status | Basis |
|------------|--------|-------|
| rbsK is an ATP-dependent ribokinase (EC 2.7.1.15) producing R5P | **Supported** | UniProt/HAMAP + ortholog biochemistry ([PMID: 25084391](https://pubmed.ncbi.nlm.nih.gov/25084391/), [9385653](https://pubmed.ncbi.nlm.nih.gov/9385653/), [16784868](https://pubmed.ncbi.nlm.nih.gov/16784868/)) |
| Enzyme requires monovalent (K⁺) and divalent (Mg²⁺) cations | **Supported** | [PMID: 16784868](https://pubmed.ncbi.nlm.nih.gov/16784868/) |
| Strict D-sugar stereospecificity; L-sugars not substrates | **Supported** | [PMID: 16784868](https://pubmed.ncbi.nlm.nih.gov/16784868/) |
| Member of pfkB superfamily; homodimer | **Supported** | [PMID: 9385653](https://pubmed.ncbi.nlm.nih.gov/9385653/); InterPro domains |
| Q88K34 conserves ribokinase active-site residues (Asp254 base, GG anion hole, GGKGANQAV, NPAPA) | **Supported** | 41.4% identity to *E. coli* RbsK; motif analysis (this work) |
| Acts in cytoplasm downstream of ribose ABC import; feeds PPP/nucleotide synthesis | **Supported** | [PMID: 23651393](https://pubmed.ncbi.nlm.nih.gov/23651393/), [9385653](https://pubmed.ncbi.nlm.nih.gov/9385653/) |
| rbsK is in a genuine ribose operon in *P. putida* KT2440 (rbsB-A-C-R-K-D + nuh) | **Supported** | KEGG ppu genome context, PP_2454–2460 (this work); [PMID: 23651393](https://pubmed.ncbi.nlm.nih.gov/23651393/) |
| rbsK has a non-metabolic / signaling role | **Refuted / no evidence** | No literature support; all evidence points to a housekeeping metabolic kinase |

---

## Limitations and Knowledge Gaps

1. **No direct assay of the *P. putida* protein.** UniProt lists Q88K34 as evidence level PE=3 ("inferred from homology"). No purified-enzyme kinetics (kcat, Km for ribose and ATP), pH/temperature optima, or oligomeric-state measurement have been published for the KT2440 protein itself. All quantitative kinetic and cofactor data come from orthologs, chiefly *E. coli*.

2. **Operon structure is inferred, not experimentally mapped.** The operonic organization of PP_2454–2460 is deduced from gene contiguity, shared strand, and overlapping stop/start codons plus homology to the *E. coli rbs* operon. Transcript mapping (RNA-seq operon boundaries, promoter/terminator identification) and confirmation of RbsR-dependent, ribose-inducible regulation in *P. putida* have not been directly demonstrated here.

3. **Substrate specificity of the *P. putida* enzyme is assumed.** The broad D-sugar promiscuity and strict D-stereospecificity are established for the *E. coli* enzyme; whether the KT2440 ortholog shares the identical specificity profile (e.g., relative activity on 2-deoxyribose, arabinose, xylose, fructose) is untested.

4. **Physiological ribose metabolism in *P. putida* is not directly characterized here.** *P. putida* KT2440 preferentially uses organic acids and aromatics; the extent to which ribose serves as a growth substrate, and the flux through RbsK under different conditions, has not been measured in this study.

5. **No experimental structure of Q88K34.** Structural inference rests on orthologs. An AlphaFold model or experimental structure would allow direct confirmation of active-site residue positioning.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant enzymology.** Clone PP_2458, express and purify the protein, and measure steady-state kinetics: kcat and Km for D-ribose and ATP, K⁺/Mg²⁺ dependence, pH/temperature optima, and the substrate-specificity panel (D-ribose, 2-deoxy-D-ribose, D-arabinose, D-xylose, D-fructose; L-sugar controls). This would upgrade the annotation from PE=3 to direct experimental evidence.

2. **Active-site mutagenesis.** Mutate the predicted general base **Asp254** (and the di-glycine anion hole) to confirm catalytic essentiality, paralleling the *Arabidopsis* mutational study ([PMID: 30822455](https://pubmed.ncbi.nlm.nih.gov/30822455/)).

3. **Transcriptional/operon mapping.** Use RNA-seq or RT-PCR across the PP_2454–2460 region to confirm co-transcription, and test RbsR (PP_2457) as a ribose-responsive repressor via reporter assays and EMSA.

4. **Genetic phenotyping.** Construct a ΔrbsK (PP_2458) deletion and test growth on D-ribose (and on nucleosides, given the adjacent Nuh) as sole carbon source; complement to confirm causality. Cross-reference existing RB-TnSeq fitness datasets for KT2440 ([PMID: 38323821](https://pubmed.ncbi.nlm.nih.gov/38323821/)) for ribose-condition fitness signatures.

5. **Structure determination.** Solve the crystal structure (or refine an AlphaFold model against experimental data) in apo, ATP-bound, and ribose+ATP ternary states to confirm the ribokinase fold, lid closure, and K⁺ site.

6. **Metabolic-flux confirmation.** Use ¹³C-labeled ribose tracing to verify that carbon flows through RbsK into R5P, the pentose phosphate pathway, and the PRPP/nucleotide pool in *P. putida*.

---

## Conclusion

*rbsK* (PP_2458, UniProt Q88K34) of *Pseudomonas putida* KT2440 encodes a **cytoplasmic PfkB-family ribokinase (EC 2.7.1.15)** that catalyzes the **Mg-ATP-dependent, K⁺-activated phosphorylation of D-ribose to D-ribose-5-phosphate**, the committed first step of ribose catabolism. The product feeds the pentose phosphate pathway and PRPP-dependent nucleotide, histidine and tryptophan biosynthesis. The enzyme is a homodimer, is strictly D-stereospecific, and in *P. putida* is encoded within a contiguous ribose-utilization operon (*rbsB-A-C-R-K-D* + nucleoside hydrolase) immediately downstream of the RbsBAC ABC importer and the RbsD anomerase. While direct assay of the *P. putida* protein is lacking (PE=3), the assignment is robustly supported by ortholog biochemistry and structure and by 41.4% sequence identity to *E. coli* ribokinase with complete conservation of all catalytic and cofactor-binding motifs, including the general-base aspartate (Asp254).


## Artifacts

- [OpenScientist final report](rbsK-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](rbsK-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:25084391
2. PMID:9385653
3. PMID:16784868
4. PMID:30822455
5. PMID:23651393
6. PMID:16519676
7. PMID:16893570
8. PMID:31253668
9. PMID:2432883
10. PMID:32443190
11. PMID:36528203
12. PMID:31924622
13. PMID:38323821