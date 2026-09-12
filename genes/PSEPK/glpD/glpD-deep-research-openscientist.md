---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-26T20:22:44.068492'
end_time: '2026-07-26T20:51:06.055884'
duration_seconds: 1701.99
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: glpD
  gene_symbol: glpD
  uniprot_accession: Q88NY0
  protein_description: 'RecName: Full=Glycerol-3-phosphate dehydrogenase {ECO:0000256|RuleBase:RU361217};
    EC=1.1.5.3 {ECO:0000256|RuleBase:RU361217};'
  gene_info: Name=glpD {ECO:0000313|EMBL:AAN66698.1}; OrderedLocusNames=PP_1073 {ECO:0000313|EMBL:AAN66698.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the FAD-dependent glycerol-3-phosphate
  protein_domains: DAO_C. (IPR031656); DAO_C_sf. (IPR038299); FAD-dep_OxRdtase. (IPR006076);
    FAD/NAD-bd_sf. (IPR036188); G3P_DH_FAD-dep. (IPR000447)
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
  path: glpD-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: glpD-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88NY0
- **Protein Description:** RecName: Full=Glycerol-3-phosphate dehydrogenase {ECO:0000256|RuleBase:RU361217}; EC=1.1.5.3 {ECO:0000256|RuleBase:RU361217};
- **Gene Information:** Name=glpD {ECO:0000313|EMBL:AAN66698.1}; OrderedLocusNames=PP_1073 {ECO:0000313|EMBL:AAN66698.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the FAD-dependent glycerol-3-phosphate
- **Key Domains:** DAO_C. (IPR031656); DAO_C_sf. (IPR038299); FAD-dep_OxRdtase. (IPR006076); FAD/NAD-bd_sf. (IPR036188); G3P_DH_FAD-dep. (IPR000447)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "glpD" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'glpD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **glpD** (gene ID: glpD, UniProt: Q88NY0) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *glpD* (PP_1073, UniProt Q88NY0) in *Pseudomonas putida* KT2440

**Target:** Glycerol-3-phosphate dehydrogenase (GlpD)
**Gene:** *glpD* / OrderedLocusName PP_1073
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / NCIMB 11950 / KT2440) — proteome code PSEPK
**EC number:** 1.1.5.3
**Protein family:** FAD-dependent glycerol-3-phosphate dehydrogenase (aerobic subfamily)

---

## Summary

**The gene *glpD* (PP_1073, UniProt Q88NY0) in *Pseudomonas putida* KT2440 encodes the aerobic, FAD-dependent sn-glycerol-3-phosphate dehydrogenase (GlpD, EC 1.1.5.3).** Its primary function is to catalyze the oxidation of *sn*-glycerol-3-phosphate (G3P) to dihydroxyacetone phosphate (DHAP), transferring the abstracted electron pair through a non-covalently bound FAD prosthetic group to a membrane quinone. The net reaction is: **a quinone + sn-glycerol 3-phosphate → dihydroxyacetone phosphate + a quinol.** By donating electrons directly to the membrane ubiquinone pool, GlpD couples the catabolism of glycerol to the aerobic respiratory chain, without producing a soluble reduced cofactor (NADH). It is therefore the committed, respiration-coupled step that converts a glycerol-derived intermediate into a central-metabolism triose phosphate.

**Localization:** GlpD is a monotopic, cytoplasmic-membrane-associated flavoenzyme. It is not an integral polytopic transporter; rather, it associates with the inner (cytoplasmic) face of the membrane where it can hand electrons to the quinone pool while its active site oxidizes the cytoplasmic substrate G3P. This localization and mechanism are established in molecular detail for the closely related *Escherichia coli* ortholog, whose crystal structures (up to 1.75 Å) reveal a hydrophobic membrane-binding "plateau" harboring the likely ubiquinone-binding site. Because Q88NY0 is ~57–60% identical to that reference enzyme and shares its complete domain architecture and FAD-binding fingerprint, this structural and mechanistic annotation transfers with high confidence.

**Pathway context:** In *P. putida* KT2440, *glpD* is the terminal gene of the substrate-inducible **glpFKRD** cluster that constitutes the canonical glycerol-utilization pathway: glycerol enters via the aquaglyceroporin GlpF, is phosphorylated by glycerol kinase GlpK to G3P, and G3P is oxidized by GlpD to DHAP, which then feeds glycolysis (EDEMP cycle) and gluconeogenesis. The cluster is under negative control by the G3P-responsive DeoR-family repressor GlpR. This regulation underlies the well-documented long, bimodal (stochastic) lag phase that KT2440 exhibits when growing on glycerol. A transcriptional Φ(*glpD-gfp*) fusion has been used as a direct proxy of G3P dehydrogenase activity in this organism, tying *glpD* expression to the glycerol growth phenotype.

---

## Key Findings

### Finding 1 — GlpD is a FAD-dependent aerobic G3P dehydrogenase that oxidizes G3P to DHAP (EC 1.1.5.3)

UniProt entry Q88NY0 carries the recommended name *Glycerol-3-phosphate dehydrogenase* with EC 1.1.5.3 and the catalytic activity "a quinone + sn-glycerol 3-phosphate = dihydroxyacetone phosphate + a quinol." The cofactor is FAD, the protein is 514 amino acids long, and it belongs to the FAD-dependent glycerol-3-phosphate dehydrogenase family. Orthology databases reinforce this: KEGG assigns ppu:PP_1073 to ortholog group **K00111** ("glycerol-3-phosphate dehydrogenase, aerobic; EC 1.1.5.3"), eggNOG places it in **COG0578**, and the Pfam/InterPro architecture (PF01266 DAO + PF16901 DAO_C; IPR000447 G3P_DH_FAD-dep, IPR006076) is diagnostic of this enzyme class.

The reaction itself is directly documented for the enzyme family. As stated for the characterized ortholog, "GlpD is a six transmembrane spanning redox enzyme that catalyzes the oxidation of glycerol-3-phosphate to dihydroxyacetone phosphate" ([PMID: 16363804](https://pubmed.ncbi.nlm.nih.gov/16363804/)), and it is "an essential membrane enzyme, functioning at the central junction of respiration, glycolysis, and phospholipid biosynthesis" ([PMID: 18296637](https://pubmed.ncbi.nlm.nih.gov/18296637/)). The substrate specificity is narrow: the physiological substrate is *sn*-glycerol-3-phosphate, and the product is dihydroxyacetone phosphate. Unlike the cytosolic NAD⁺-linked glycerol-3-phosphate dehydrogenase (EC 1.1.1.8), this enzyme is FAD/quinone-linked (EC 1.1.5.3) and does not generate soluble NADH; the electrons instead enter the membrane quinone pool.

### Finding 2 — GlpD is a monotopic, membrane-associated respiratory flavoenzyme that feeds electrons into the quinone pool

The subcellular localization and respiratory role are firmly established for the *E. coli* ortholog, which is defined as "aerobic sn-glycerol 3-phosphate dehydrogenase is a cytoplasmic membrane-associated respiratory enzyme encoded by the glpD gene of Escherichia coli" ([PMID: 8955388](https://pubmed.ncbi.nlm.nih.gov/8955388/)). Crystallographic work on the fully active *E. coli* enzyme, solving "seven previously undescribed structures ... up to 1.75 Å resolution," identified "a hydrophobic plateau that is likely the ubiquinone-binding site" and showed "how GlpD shuttles electrons into the respiratory pathway" ([PMID: 18296637](https://pubmed.ncbi.nlm.nih.gov/18296637/)).

Mechanistically, this defines GlpD as a **monotopic membrane redox flavoenzyme**: it is not a channel or a polytopic integral-membrane transporter but an enzyme that docks onto the cytoplasmic face of the inner membrane. The FAD cofactor accepts the hydride from G3P; the reduced flavin is then re-oxidized by ubiquinone bound at the hydrophobic plateau, generating quinol that diffuses into the respiratory chain. For Q88NY0 the annotated reaction (quinone + G3P → DHAP + quinol) is fully consistent with this mechanism — electrons enter the membrane quinone pool rather than a soluble cofactor, tightly linking glycerol oxidation to aerobic respiration and, ultimately, to proton-motive-force generation and ATP synthesis. Independent early genetic work also showed that "the amino-terminal 30 to 60 amino acids of this hybrid protein (provided by glpD) were sufficient for efficient membrane localization" ([PMID: 3027031](https://pubmed.ncbi.nlm.nih.gov/3027031/)), consistent with an N-terminal membrane-association determinant.

### Finding 3 — *glpD* (PP_1073) resides in the GlpR-controlled *glpFKRD* cluster and governs the glycerol lag-phase phenotype

The KEGG genomic neighborhood of PP_1073 in KT2440 shows an intact glycerol-utilization operon:

| Locus | Gene | Product / KO | Function |
|-------|------|--------------|----------|
| PP_1073 | *glpD* | K00111 | FAD-dependent G3P dehydrogenase (EC 1.1.5.3) |
| PP_1074 | *glpR* | K02444 | DeoR-family G3P-responsive repressor of the *glp* regulon |
| PP_1075 | *glpK* | (EC 2.7.1.30) | Glycerol kinase (glycerol → G3P) |
| PP_1076 | *glpF* | — | Aquaglyceroporin / glycerol uptake facilitator |

This *glpFKRD* arrangement encodes a complete, self-contained glycerol pathway. Functional evidence in *P. putida* KT2440 comes from Nikel et al. (2015), who used a transcriptional Φ(*glpD-gfp*) fusion "(a proxy of the glycerol-3-phosphate [G3P] dehydrogenase activity)" to link "the macroscopic phenotype to the expression of the glp genes" ([PMID: 25827416](https://pubmed.ncbi.nlm.nih.gov/25827416/)). Genetic perturbation confirmed the regulatory logic: "deleting glpR (encoding the G3P-responsive transcriptional repressor that controls the expression of the glpFKRD gene cluster)" — or overexpressing *glpK* — abolished the bimodal *glpD* expression and shortened the characteristic long glycerol lag phase. The physiological effector (inducer/anti-repressor) of GlpR is G3P itself. This places *glpD* both mechanistically (enzyme) and regulatorily (GlpR target) at the heart of glycerol metabolism in KT2440.

### Finding 4 — GlpD provides the canonical entry of glycerol carbon into central metabolism via DHAP

GlpD's product, DHAP, is a triose-phosphate node that feeds directly into glycolysis (the EDEMP cycle in *Pseudomonas*) and gluconeogenesis, and connects to glycerophospholipid metabolism (KEGG ppu00564). The linear catabolic route is therefore: glycerol → (GlpF import) → glycerol → (GlpK phosphorylation) → G3P → (GlpD oxidation) → DHAP → central carbon metabolism. Nikel & de Lorenzo (2018) confirmed that in KT2440 the prolonged glycerol lag "has been shown to be connected with the stochastic expression of the glp genes, which encode the enzymes needed for glycerol processing" ([PMID: 29476475](https://pubmed.ncbi.nlm.nih.gov/29476475/)), underscoring that *glpD* and its operon partners are the enzymes required for glycerol catabolism.

Notably, KT2440 also possesses an **alternative, lanthanide/PQQ-dependent periplasmic route** for glycerol oxidation (Wehrmann et al. 2020, [PMID: 32345644](https://pubmed.ncbi.nlm.nih.gov/32345644/)). This route is distinct from, and runs parallel to, the cytoplasmic GlpD/G3P pathway. Its existence does not alter the assignment of GlpD as the classical G3P-oxidizing enzyme, but it is important context: glycerol metabolism in *P. putida* is not solely dependent on GlpD, which may explain some of the metabolic flexibility and phenotypic variability seen on glycerol.

### Finding 5 — Q88NY0 is a bona fide ortholog of *E. coli* GlpD (~60% identity), justifying annotation transfer

A Needleman-Wunsch global alignment (BLOSUM62, gap = −4) of *P. putida* GlpD (Q88NY0, 514 aa) against the structurally and biochemically characterized *E. coli* aerobic GlpD (P13035, 501 aa) yields **297 identical positions over 501 aligned columns = ~59–60% amino-acid identity.** Both enzymes share the N-terminal FAD-binding dinucleotide (Rossmann) fingerprint — Q88NY0 `GGGINGVGIAADAAGRG` versus *E. coli* `GGGINGAGIAADAAGRG`, both containing the GxGxxG motif — and the identical domain architecture (Pfam PF01266 DAO + PF16901 DAO_C; InterPro IPR000447), ortholog group (COG0578), and KEGG KO (K00111).

The reference enzyme, P13035, is the subject of the high-resolution crystallographic study reporting "seven previously undescribed structures of the fully active E. coli GlpD, up to 1.75 A resolution" ([PMID: 18296637](https://pubmed.ncbi.nlm.nih.gov/18296637/)). At ~60% identity with fully conserved catalytic architecture, transfer of the reaction, cofactor, mechanism, and membrane-association annotation from P13035 to Q88NY0 is well justified by standard homology-based inference thresholds (>40% identity over the full length with conserved active-site motifs).

### Finding 6 — Q88NY0 is the aerobic GlpD, not the anaerobic GlpA

*E. coli* has two FAD-dependent G3P dehydrogenase systems: the aerobic **GlpD** (a single polypeptide feeding ubiquinone) and the anaerobic **GlpABC** (a three-subunit enzyme, GlpA being the flavoprotein, feeding menaquinone). To discriminate which subfamily Q88NY0 belongs to, global pairwise alignments were computed against both:

| Reference | Type | Length | % identity to Q88NY0 |
|-----------|------|--------|----------------------|
| *E. coli* GlpD (P13035) | Aerobic, single-subunit | 501 aa | **57.4%** |
| *E. coli* GlpA (P0A9C0) | Anaerobic, GlpABC complex | 542 aa | 26.7% |

The >2-fold higher identity to GlpD, combined with the operon context — a single *glpD* gene within *glpFKRD*, with **no adjacent glpB/glpC subunit genes** — and the K00111/COG0578 assignment, unambiguously places PP_1073 in the aerobic GlpD subfamily. The reference enzyme's identity as the aerobic, respiration-linked GlpD "functioning at the central junction of respiration, glycolysis, and phospholipid biosynthesis" ([PMID: 18296637](https://pubmed.ncbi.nlm.nih.gov/18296637/)) therefore applies to Q88NY0.

---

## Mechanistic Model / Interpretation

Putting the six findings together yields a coherent picture of GlpD as the respiration-coupled gateway for glycerol carbon in *P. putida* KT2440:

```
   Extracellular glycerol
            │
            │  GlpF (PP_1076)  aquaglyceroporin — facilitated diffusion
            ▼
      Cytoplasmic glycerol
            │
            │  GlpK (PP_1075)  glycerol kinase, ATP → ADP   (EC 2.7.1.30)
            ▼
   sn-glycerol-3-phosphate (G3P) ──► (also effector/anti-repressor of GlpR)
            │
            │  ┌───────────────────────────────────────────────────┐
            │  │  GlpD (PP_1073)  FAD-dependent G3P dehydrogenase     │
            │  │  monotopic, inner-membrane-associated flavoenzyme   │
            │  │  G3P + FAD → DHAP + FADH2                            │
            │  │  FADH2 + quinone(Q) → FAD + quinol(QH2)              │
            │  └───────────────────────────────────────────────────┘
            ▼                                    │
   Dihydroxyacetone phosphate (DHAP)            │ electrons
            │                                    ▼
            │                          Membrane ubiquinone pool
   ┌────────┴─────────┐                          │
   ▼                  ▼                          ▼
 Glycolysis/       Gluconeogenesis        Aerobic respiratory chain
 EDEMP cycle       & phospholipid         → proton-motive force → ATP
 (central carbon)  biosynthesis

   Regulation: GlpR (PP_1074, DeoR family) represses glpFKRD; G3P relieves
   repression → substrate induction. Stochastic (bimodal) glpD expression
   → long, variable glycerol lag phase.
```

**Two functional outputs from one reaction.** The oxidation of G3P to DHAP simultaneously (i) delivers a carbon skeleton (DHAP) to central metabolism and (ii) delivers reducing equivalents to the respiratory chain. This dual coupling is what makes GlpD the "committed" and metabolically pivotal step of glycerol utilization — it is the point at which glycerol-derived carbon and electrons are fully integrated into the cell's energy and biosynthetic economy.

**Why the quinone linkage matters.** Because GlpD reduces quinone rather than NAD⁺, glycerol oxidation via this route is obligately coupled to a functioning membrane electron-transport chain. This is the biochemical basis of the enzyme's classification as "aerobic" G3P dehydrogenase and distinguishes it sharply from the cytosolic NAD⁺-linked isozyme.

**Regulatory logic and phenotype.** The GlpR repressor keeps the operon off until G3P accumulates, at which point the pathway is induced. The stochastic, all-or-none character of this induction in individual cells produces population-level bimodality and the notoriously long glycerol lag phase in KT2440 — a phenotype directly traced to *glp* gene expression via the Φ(*glpD-gfp*) reporter.

---

## Evidence Base

| PMID | Title (abbrev.) | Relevance to Q88NY0 |
|------|-----------------|---------------------|
| [18296637](https://pubmed.ncbi.nlm.nih.gov/18296637/) | *Structure of glycerol-3-phosphate dehydrogenase, an essential monotopic membrane enzyme* | Primary structural reference (P13035, up to 1.75 Å). Defines monotopic membrane association, ubiquinone-binding site, respiratory electron shuttling, and the "central junction" role. Annotation transferred to Q88NY0 (~57–60% identity). |
| [8955388](https://pubmed.ncbi.nlm.nih.gov/8955388/) | *Action at a distance for negative control of glpD* | Establishes GlpD as a cytoplasmic-membrane-associated respiratory enzyme and documents *glpD* regulation. Supports localization (F002). |
| [16363804](https://pubmed.ncbi.nlm.nih.gov/16363804/) | *Peptergents ... membrane protein, glycerol-3-phosphate dehydrogenase* | States directly that GlpD catalyzes oxidation of G3P to DHAP and is a transmembrane redox enzyme. Supports reaction/mechanism (F001). |
| [3027031](https://pubmed.ncbi.nlm.nih.gov/3027031/) | *Cloning and characterization of glpD of E. coli K-12* | Confirms *glpD* is the structural gene for aerobic G3P dehydrogenase (Mr ~55,000) and that its N-terminal ~30–60 residues confer membrane localization. Supports F001/F002/F006. |
| [25827416](https://pubmed.ncbi.nlm.nih.gov/25827416/) | *Glycerol-dependent metabolic persistence of P. putida KT2440 / GlpR* | The key organism-specific paper. Uses Φ(*glpD-gfp*) as a proxy for G3P dehydrogenase activity; establishes *glpFKRD* cluster, GlpR control, and the glycerol lag phenotype. Supports F003. |
| [29476475](https://pubmed.ncbi.nlm.nih.gov/29476475/) | *Assessing Carbon Source-Dependent Phenotypic Variability in P. putida* | Confirms *glp* genes encode the enzymes needed for glycerol processing and links stochastic *glp* expression to the lag phenotype. Supports F004. |
| [32345644](https://pubmed.ncbi.nlm.nih.gov/32345644/) | *Cellular Response to Lanthanum ... Novel Route for Glycerol Metabolism* | Documents an alternative PQQ/lanthanide-dependent glycerol-oxidation route in KT2440, parallel to and distinct from the GlpD/G3P pathway. Context for F004. |

Additional KT2440 systems-biology and metabolic-engineering papers ([PMID: 41260329](https://pubmed.ncbi.nlm.nih.gov/41260329/) on HexR regulation of central carbon metabolism; [PMID: 41856294](https://pubmed.ncbi.nlm.nih.gov/41856294/) and [PMID: 33796510](https://pubmed.ncbi.nlm.nih.gov/33796510/) on glycerol as a co-feedstock) provide broader context on central-carbon regulation and the biotechnological importance of glycerol utilization in this organism, but do not directly characterize GlpD.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of the *P. putida* protein.** The functional assignment of Q88NY0 rests on (i) sequence orthology (~57–60% identity to *E. coli* GlpD), (ii) conserved domain architecture and FAD motif, and (iii) organism-specific genetic/regulatory evidence from KT2440. There is, to our knowledge, no published purified-enzyme kinetic study (Km, kcat, quinone specificity) of the KT2440 GlpD itself. Kinetic parameters and quinone (ubiquinone vs. other) specificity are inferred, not measured, for the *P. putida* enzyme.

2. **Structure is homology-based.** No experimental structure of Q88NY0 exists; the monotopic membrane topology and ubiquinone-binding plateau are inferred from the *E. coli* crystal structures. An AlphaFold model plus the conserved FAD fingerprint make this inference robust, but residue-level details (e.g., the exact quinone pocket) remain predictive.

3. **Regulatory effector confirmation.** GlpR is annotated as G3P-responsive by homology and by phenotype (glpR deletion abolishes bimodality), but a direct in vitro demonstration that G3P binds KT2440 GlpR and relieves repression at the *glpD* promoter was not located in the reviewed literature.

4. **Interplay with the alternative PQQ/lanthanide route.** The relative flux through GlpD versus the lanthanide-dependent periplasmic glycerol-oxidation route under different growth conditions is not quantified here, leaving the precise physiological weighting of GlpD's contribution open.

5. **Phospholipid-biosynthesis link.** The "phospholipid biosynthesis" junction cited for the *E. coli* enzyme reflects G3P being a shared precursor; whether *P. putida* GlpD activity meaningfully competes with G3P acyltransferases for the G3P pool in KT2440 has not been established experimentally.

---

## Proposed Follow-up Experiments / Actions

1. **Direct enzymology.** Heterologously express and purify KT2440 GlpD (PP_1073), reconstitute with FAD, and measure steady-state kinetics with *sn*-G3P and a panel of quinone acceptors (ubiquinone-1/-2 analogs, menaquinone) to obtain Km/kcat and confirm ubiquinone preference — distinguishing it definitively from the anaerobic menaquinone-linked GlpABC class.

2. **Genetic loss-of-function.** Construct a clean ΔPP_1073 mutant and test growth on glycerol as sole carbon source, with and without the lanthanide/PQQ route active (± La³⁺). This would quantify GlpD's contribution to glycerol catabolism and dissect its redundancy with the alternative route.

3. **Localization / topology.** Perform membrane fractionation and protease-protection assays (or a GFP/PhoA-LacZ topology fusion) on KT2440 GlpD to experimentally confirm monotopic cytoplasmic-membrane association predicted from the ortholog.

4. **Regulatory validation.** Purify KT2440 GlpR and perform EMSA / DNase-footprinting at the *glpFKRD* promoter ± G3P to confirm G3P as the physiological anti-repressor and map operator sites; correlate with the previously reported bimodal Φ(*glpD-gfp*) expression.

5. **Structural confirmation.** Solve the KT2440 GlpD structure (cryo-EM of the membrane-associated form or X-ray of a solubilized construct) to validate the predicted FAD and quinone pockets and the membrane-binding surface.

6. **Flux analysis.** Use ¹³C-glycerol metabolic flux analysis in wild-type and ΔglpD strains to quantify carbon flow from G3P/DHAP into the EDEMP cycle versus gluconeogenesis and phospholipid biosynthesis, resolving the "central junction" role in *P. putida* specifically.

---

## Conclusion

*glpD* (PP_1073, UniProt Q88NY0) in *Pseudomonas putida* KT2440 encodes the **aerobic, FAD-dependent sn-glycerol-3-phosphate dehydrogenase (GlpD, EC 1.1.5.3)**, a monotopic cytoplasmic-membrane-associated flavoenzyme that oxidizes *sn*-glycerol-3-phosphate to dihydroxyacetone phosphate and delivers the electrons to the membrane quinone pool (quinone + G3P → DHAP + quinol), thereby coupling glycerol catabolism to aerobic respiration. It operates at the junction of glycerol utilization, central carbon metabolism (DHAP feeding glycolysis/EDEMP and gluconeogenesis) and phospholipid biosynthesis. In KT2440 it is the terminal gene of the substrate-inducible, GlpR-repressed *glpFKRD* cluster, and its stochastic expression underlies the organism's characteristic long glycerol lag phase. The identity is confirmed by ~57–60% amino-acid identity, conserved FAD fingerprint, and shared domain architecture with the structurally characterized *E. coli* GlpD, and it is discriminated as the aerobic GlpD (57%) rather than the anaerobic GlpA (27%).


## Artifacts

- [OpenScientist final report](glpD-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](glpD-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:16363804
2. PMID:18296637
3. PMID:8955388
4. PMID:3027031
5. PMID:25827416
6. PMID:29476475
7. PMID:32345644
8. PMID:41260329
9. PMID:41856294
10. PMID:33796510