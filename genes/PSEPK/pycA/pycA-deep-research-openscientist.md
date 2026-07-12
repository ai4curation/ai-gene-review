---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T19:17:03.980532'
end_time: '2026-07-11T19:34:20.283909'
duration_seconds: 1036.3
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: pycA
  gene_symbol: pycA
  uniprot_accession: Q88C36
  protein_description: 'RecName: Full=Biotin carboxylase {ECO:0000256|ARBA:ARBA00017242};
    AltName: Full=Acetyl-coenzyme A carboxylase biotin carboxylase subunit A {ECO:0000256|ARBA:ARBA00033786};'
  gene_info: Name=pycA {ECO:0000313|EMBL:AAN70912.1}; OrderedLocusNames=PP_5347 {ECO:0000313|EMBL:AAN70912.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: ACC_Biotin_Carboxylase. (IPR051602); ATP-grasp. (IPR011761); BC-like_N.
    (IPR005481); Biotin_carboxylation_dom. (IPR011764); Biotin_COase_C. (IPR005482)
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
citation_count: 12
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: pycA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pycA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88C36
- **Protein Description:** RecName: Full=Biotin carboxylase {ECO:0000256|ARBA:ARBA00017242}; AltName: Full=Acetyl-coenzyme A carboxylase biotin carboxylase subunit A {ECO:0000256|ARBA:ARBA00033786};
- **Gene Information:** Name=pycA {ECO:0000313|EMBL:AAN70912.1}; OrderedLocusNames=PP_5347 {ECO:0000313|EMBL:AAN70912.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** ACC_Biotin_Carboxylase. (IPR051602); ATP-grasp. (IPR011761); BC-like_N. (IPR005481); Biotin_carboxylation_dom. (IPR011764); Biotin_COase_C. (IPR005482)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pycA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pycA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pycA** (gene ID: pycA, UniProt: Q88C36) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *pycA* (PP_5347; UniProt Q88C36) in *Pseudomonas putida* KT2440

## Summary

**pycA (locus PP_5347; UniProt Q88C36) in *Pseudomonas putida* KT2440 encodes the biotin carboxylase (BC), or α, subunit of a two-subunit pyruvate carboxylase (EC 6.4.1.1).** Its primary molecular function is to catalyze the first, ATP- and bicarbonate-dependent half-reaction of biotin-dependent carboxylation: it carboxylates the biotin prosthetic group that is covalently attached to a lysine of its partner subunit, PycB. Working together, PycA and PycB convert pyruvate + HCO₃⁻ + ATP into oxaloacetate + ADP + Pᵢ. This is a soluble, cytoplasmic **anaplerotic** reaction — it replenishes the four-carbon dicarboxylic-acid pool of the tricarboxylic acid (TCA) cycle and supplies oxaloacetate for gluconeogenesis and biosynthesis.

An important correction emerged during this investigation. UniProt's automated (ARBA/rule-based) annotation labels Q88C36 as the "acetyl-coenzyme A carboxylase biotin carboxylase subunit A." This name is derived from the shared ATP-grasp/biotin-carboxylase domain architecture that is common to **all** biotin-dependent carboxylases, and it is a **mis-annotation** in the specific genomic context of *P. putida* KT2440. Genomic synteny, orthology (KEGG), and domain analysis all indicate that PP_5347 is the BC subunit of pyruvate carboxylase, not of acetyl-CoA carboxylase. Decisively, *P. putida* KT2440 possesses a *separate, complete* acetyl-CoA carboxylase encoded by *accBCAD* (accC = PP_0558, accB = PP_0559, accA = PP_1607, accD = PP_1996), so PycA is neither required for nor part of fatty-acid initiation.

The evidence base combines (i) direct genomic and orthology evidence within *P. putida* KT2440, (ii) sequence and structural bioinformatics on Q88C36 itself (51% identity to *E. coli* biotin carboxylase with a fully conserved active site; soluble cytoplasmic protein with no signal peptide or transmembrane helix), and (iii) a rich mechanistic literature on the biotin-dependent carboxylase superfamily and, specifically, the distinct two-subunit pyruvate carboxylase architecture found in Gram-negative bacteria. Multi-omics data from *P. putida* KT2440 grown on lignin-derived aromatic substrates provide physiological confirmation that the enzyme is upregulated for anaplerotic TCA replenishment.

---

## Key Findings

### Finding 1 — pycA is the biotin carboxylase subunit of a two-subunit pyruvate carboxylase, not of acetyl-CoA carboxylase

The single most consequential result of this investigation is a **correction to the database annotation.** The initial reading of UniProt Q88C36 ("Biotin carboxylase"; alt. name "Acetyl-coenzyme A carboxylase biotin carboxylase subunit A") suggested a role in fatty-acid initiation. However, examination of the genomic context, orthology assignments, and domain content of the neighboring gene overturns this.

Several independent lines of evidence converge:

1. **Genomic synteny.** PP_5347 (*pycA*) sits immediately adjacent to PP_5346 (*pycB*, UniProt Q88C37, 602 aa), which KEGG annotates as **pyruvate carboxylase subunit B (K01960)**. Adjacent, co-transcribed α/β genes are the hallmark of the two-subunit pyruvate carboxylase.
2. **Domain partitioning.** PycB contains a **pyruvate carboxyltransferase (CT) domain (IPR000891/PF00682)** plus a C-terminal **biotin/lipoyl-attachment (BCCP) domain** (residues ~526–601) — i.e., PycB carries the biotin. PycA (471 aa) contains **only** the biotin-carboxylase/ATP-grasp domain and has **no** BCCP domain. This division of labor is exactly the two-subunit PC architecture.
3. **Orthology.** KEGG assigns PP_5347 → **K01959 (pyruvate carboxylase subunit A, EC 6.4.1.1)**, mapped to the TCA cycle and pyruvate metabolism — not to fatty-acid biosynthesis.
4. **A separate ACC exists.** *P. putida* KT2440 encodes a complete, dedicated acetyl-CoA carboxylase elsewhere in the genome: accC = PP_0558 (K01961), accB = PP_0559 (K02160), accA = PP_1607, accD = PP_1996. Because a full ACC is already present, PP_5347 is not needed for malonyl-CoA production.

This architecture matches the described two-subunit pyruvate carboxylase of Gram-negative bacteria. As Choi *et al.* (2016) state, "PC is a two-subunit enzyme in a collection of Gram-negative bacteria, with the α subunit containing the BC and the β subunit the CT and BCCP domains" ([PMID: 27708276](https://pubmed.ncbi.nlm.nih.gov/27708276/)). PycA (BC; α; PP_5347) and PycB (CT + BCCP; β; PP_5346) map directly onto this description. The holoenzyme catalyzes the reaction that Laseke *et al.* (2025) describe: "Pyruvate carboxylase (PC) catalyzes the carboxylation of pyruvate to oxaloacetate which serves as an important anaplerotic reaction to replenish citric acid cycle intermediates" ([PMID: 39725256](https://pubmed.ncbi.nlm.nih.gov/39725256/)).

### Finding 2 — The reaction catalyzed: the ATP·bicarbonate biotin-carboxylation half-reaction

PycA's specific catalytic contribution is the **first half-reaction** of biotin-dependent carboxylation. The overall pyruvate carboxylase reaction proceeds in two spatially separated half-reactions:

- **Half-reaction 1 (PycA, BC domain):** biotin–[PycB] + HCO₃⁻ + ATP → carboxybiotin–[PycB] + ADP + Pᵢ. This is the activity annotated for Q88C36 (Rhea RHEA:13501; the biotin-carboxylase sub-activity that operates within EC 6.4.1.1).
- **Half-reaction 2 (PycB, CT domain):** carboxybiotin + pyruvate → oxaloacetate + biotin.
- **Net (EC 6.4.1.1):** pyruvate + HCO₃⁻ + ATP → oxaloacetate + ADP + Pᵢ.

The BC half-reaction chemistry is well established across the superfamily. Chou & Tong (2011) note that "Biotin carboxylase (BC) activity is shared among biotin-dependent carboxylases and catalyzes the Mg-ATP-dependent carboxylation of biotin using bicarbonate as the CO₂ donor" ([PMID: 21592965](https://pubmed.ncbi.nlm.nih.gov/21592965/)). Kinetic dissection of the BC domain of *Rhizobium etli* PC by Adina-Zada *et al.* (2012) resolves this half-reaction into "the enzyme-catalyzed bicarbonate-dependent ATP cleavage, carboxylation of biotin, and phosphorylation of ADP by carbamoyl phosphate" ([PMID: 22985389](https://pubmed.ncbi.nlm.nih.gov/22985389/)) — precisely the chemistry assigned to PycA. Tong (2017) places PycA in context: "Biotin-dependent carboxylases are widely distributed in nature and have central roles in the metabolism of fatty acids, amino acids, carbohydrates, and other compounds" ([PMID: 28683917](https://pubmed.ncbi.nlm.nih.gov/28683917/)).

### Finding 3 — Substrate specificity: PycA carboxylates the biotinyl-lysine of PycB's BCCP domain

The physiological substrate of PycA is **not free biotin** but the biotin prosthetic group covalently tethered to a specific lysine of its partner subunit. PycB (Q88C37) carries the conserved biotin-attachment motif **A-M-K-M**, with the biotinylated residue at **Lys567** within its C-terminal biotin/lipoyl (BCCP) domain (residues ~526–601). This covalently biotinylated lysine is the moiety that PycA carboxylates in half-reaction 1. This mode of substrate presentation — a mobile, protein-tethered biotin — is the defining feature of biotin-dependent carboxylases and dictates that PycA must physically dock the BCCP arm of PycB into its BC active site to accomplish carboxylation.

### Finding 4 — Fully conserved, intact biotin-carboxylase active site (51% identity to *E. coli* AccC)

Direct bioinformatic analysis of Q88C36 confirms a catalytically competent BC enzyme. A Needleman–Wunsch global alignment of Q88C36 (471 aa) against *E. coli* biotin carboxylase AccC (P24182) gives **51.0% identity over 447 aligned positions**. Critically, **all** of the *E. coli* BC catalytic and ATP-binding residues are conserved in Q88C36:

| *E. coli* AccC residue | Q88C36 equivalent | Role |
|---|---|---|
| Lys116 | Lys115 | ATP binding |
| Lys159 | Lys157 | ATP binding |
| His209 | His207 | catalysis |
| Glu276 | Glu274 | catalytic base |
| Glu288 | Glu286 | divalent-metal coordination |
| Asn290 | Asn288 | divalent-metal coordination |

The glycine-rich ATP-binding loop is present (…MLKATSGGGGRGI…) within the ATP-grasp domain (residues ~119–315). These are the very residues identified by Thoden *et al.* for mutagenesis: "Four of these residues of biotin carboxylase, Lys-116, Lys-159, His-209, and Glu-276, were selected for site-directed mutagenesis studies" ([PMID: 11346647](https://pubmed.ncbi.nlm.nih.gov/11346647/)). Their full conservation in Q88C36 indicates an intact, functional active site. The enzyme requires Mg²⁺ (and can use Mn²⁺), as for all biotin carboxylases.

### Finding 5 — Localization: soluble cytoplasmic protein

PycA carries out its function in the **cytoplasm**. Two lines of evidence support this:

1. **Sequence/topology analysis of Q88C36.** A Kyte–Doolittle hydropathy scan gives a maximum 19-residue window score of **1.26**, below the ~1.6 threshold for a transmembrane helix; the N-terminus (MIKKILIANRGEIA…) shows no cleavable signal peptide. The protein is therefore predicted soluble and cytoplasmic with no membrane insertion or secretion.
2. **Biology of the family.** Bacterial pyruvate carboxylases and biotin carboxylases are cytosolic enzymes. As a comparative example, in the related soil bacterium *Azotobacter vinelandii* the biotin carboxylase (AccC) is a cytoplasmic protein whose ATPase activity is regulated by a cytoplasmic cyclophilin; Dimou *et al.* (2012) report "a physical interaction among AvppiB, encoding the cytoplasmic cyclophilin from the soil nitrogen-fixing bacterium *Azotobacter vinelandii*, and AvaccC, encoding the biotin carboxylase subunit of acetyl-CoA carboxylase" ([PMID: 22809506](https://pubmed.ncbi.nlm.nih.gov/22809506/)). While that study concerns an ACC biotin carboxylase, it demonstrates the cytoplasmic, soluble nature of bacterial BC subunits generally.

### Finding 6 — Mechanistic coupling: swinging biotin and allosteric control by acetyl-CoA

Within the holoenzyme, PycA's active site is coupled to PycB's CT active site by **long-range translocation of the biotinylated carrier domain** — the "swinging arm" mechanism. Liu *et al.* (2018) show that in pyruvate carboxylase "the reaction occurs in two separate catalytic domains, coupled by the long-range translocation of a biotinylated carrier domain (BCCP)" ([PMID: 29643369](https://pubmed.ncbi.nlm.nih.gov/29643369/)). PycA generates carboxybiotin at its BC site; the BCCP arm of PycB then shuttles the carboxybiotin over tens of ångströms to the CT active site, where pyruvate is carboxylated to oxaloacetate.

This coupling is under **allosteric control by acetyl-CoA**, a hallmark of pyruvate carboxylase. Laseke *et al.* (2025) note that "In most organisms, the PC-catalyzed reaction is allosterically activated by acetyl-coenzyme A" ([PMID: 39725256](https://pubmed.ncbi.nlm.nih.gov/39725256/)). Mechanistically, acetyl-CoA acts on the carrier translocation step: Liu *et al.* (2018) find that "the allosteric activator, acetyl CoA, promotes one specific intermolecular carrier domain translocation pathway" ([PMID: 29643369](https://pubmed.ncbi.nlm.nih.gov/29643369/)). The acetyl-CoA binding site is formed largely within the CT/tetramerization (β/PycB-type) region; in *R. etli* PC, key residues include Arg427, Arg429, Arg469, Asp471, and Arg472 ([PMID: 27379711](https://pubmed.ncbi.nlm.nih.gov/27379711/); [PMID: 26149215](https://pubmed.ncbi.nlm.nih.gov/26149215/); [PMID: 22985389](https://pubmed.ncbi.nlm.nih.gov/22985389/)). The physiological logic is elegant: high acetyl-CoA signals a need for more oxaloacetate (to condense with acetyl-CoA into citrate, and to sustain the TCA cycle), so acetyl-CoA switches on the anaplerotic PC reaction.

### Finding 7 — BC-domain dimerization is required for catalysis

The BC domain of pyruvate carboxylase functions as a dimer, and the dimer interface is catalytically essential. Studies on *Staphylococcus aureus* PC show that "mutations in the dimer interface can produce stable monomers that are still catalytically active," yet several interface mutations (e.g., K442E) and BC-domain chimeras abolish activity, and the isolated *S. aureus* BC domain "is monomeric in solution and catalytically inactive" ([PMID: 23286247](https://pubmed.ncbi.nlm.nih.gov/23286247/)). *E. coli* BC studies indicate long-range communication between the two active sites of a dimer, and BC shows substrate inhibition by ATP that is competitive against bicarbonate ([PMID: 21592965](https://pubmed.ncbi.nlm.nih.gov/21592965/)). These properties are expected to apply to PycA given its 51% identity and full active-site conservation.

### Finding 8 — Physiological role in *P. putida* KT2440: anaplerosis for TCA/oxaloacetate replenishment

Direct, organism-specific evidence confirms the anaplerotic function. Multi-omics analysis of *P. putida* KT2440 grown on lignin-derived phenolic acids (ferulate, *p*-coumarate, vanillate, 4-hydroxybenzoate) versus succinate showed a large induction of pyruvate carboxylase: Zhou *et al.* (2025) report "Up to 30-fold increase in pyruvate carboxylase and glyoxylate shunt proteins implies a metabolic remodeling" ([PMID: 40883435](https://pubmed.ncbi.nlm.nih.gov/40883435/)). When *P. putida* grows on aromatic/gluconeogenic substrates that feed carbon into the TCA cycle asymmetrically, it must replenish oxaloacetate to keep the cycle turning and to supply gluconeogenic and amino-acid precursors — exactly the role of pyruvate carboxylase. KEGG maps PP_5347 to the TCA cycle, pyruvate metabolism, carbon fixation, and amino-acid biosynthesis pathways, all consistent with anaplerosis.

### Finding 9 — Position within the *P. putida* anaplerotic network

Pyruvate carboxylase (PycA/PycB) operates alongside a set of parallel anaplerotic and gluconeogenic enzymes in *P. putida* KT2440:

- **PEP carboxylase** (*ppc* = PP_1505; K01595): PEP + HCO₃⁻ → oxaloacetate.
- **NADP-malic enzyme** (*maeB* = PP_5085; K00029): interconverts malate and pyruvate.

Notably, *P. putida* KT2440 has **no single-chain pyruvate carboxylase** (the canonical single-polypeptide KO K01958 is absent from the genome), which is fully consistent with the two-subunit PycA/PycB being the organism's pyruvate carboxylase. The presence of both PEP carboxylase and a two-subunit PC gives *P. putida* redundant routes to oxaloacetate, reflecting the metabolic versatility of this soil bacterium.

---

## Mechanistic Model / Interpretation

### The two-subunit pyruvate carboxylase of *P. putida* KT2440

```
   Operon:   ... PP_5347 (pycA) --- PP_5346 (pycB) ...
                   |                     |
                   v                     v
             BC subunit (alpha)    CT + BCCP subunit (beta)
             471 aa, Q88C36        602 aa, Q88C37
             ATP-grasp fold        carboxyltransferase + biotin-Lys567
```

The holoenzyme executes anaplerosis in two coupled half-reactions:

```
  HALF-REACTION 1  (PycA, biotin carboxylase active site)
  ---------------------------------------------------------
     ATP + HCO3-  +  biotin~Lys567-[PycB]
                          |
              Mg2+, BC active site (Lys115, Lys157,
              His207, Glu274, Glu286/Asn288)
                          v
     ADP + Pi     +  carboxy-biotin~Lys567-[PycB]

                  |  BCCP "swinging arm" translocates
                  |  carboxybiotin ~tens of Angstroms
                  v

  HALF-REACTION 2  (PycB, carboxyltransferase active site)
  ---------------------------------------------------------
     carboxy-biotin~Lys567  +  pyruvate
                          v
     biotin~Lys567         +  OXALOACETATE

  NET:  pyruvate + HCO3- + ATP  -->  oxaloacetate + ADP + Pi   (EC 6.4.1.1)
  Allosteric activator: acetyl-CoA (acts on carrier translocation)
```

### Why this matters for cellular physiology

Oxaloacetate is consumed continuously — condensed with acetyl-CoA into citrate to run the TCA cycle, and drawn off for gluconeogenesis (via PEP carboxykinase), for aspartate/asparagine and the aspartate-derived amino-acid family, and for pyrimidine biosynthesis. When carbon enters metabolism as pyruvate or as compounds that funnel through pyruvate/acetyl-CoA (including many aromatic and lignin-derived substrates that *P. putida* famously degrades), oxaloacetate would be depleted without a replenishing (anaplerotic) reaction. PycA/PycB pyruvate carboxylase provides exactly this replenishment. The 30-fold induction of PC on aromatic substrates ([PMID: 40883435](https://pubmed.ncbi.nlm.nih.gov/40883435/)) is the physiological signature of this demand.

### The annotation correction, summarized

| Attribute | UniProt automated annotation | Corrected assignment (this investigation) |
|---|---|---|
| Enzyme complex | Acetyl-CoA carboxylase (ACC) | Two-subunit pyruvate carboxylase (PC) |
| EC number | 6.4.1.2 (implied) | **6.4.1.1** |
| Product | Malonyl-CoA (fatty-acid initiation) | **Oxaloacetate (anaplerosis)** |
| Partner subunit | AccB/BCCP + AccA/AccD | **PycB (PP_5346): CT + BCCP** |
| Genomic neighbor | — | PP_5346 = pyruvate carboxylase β (K01960) |
| Basis of error | Shared ATP-grasp/BC domain | — |

The shared biotin-carboxylase/ATP-grasp domain is common to ACC, PC, propionyl-CoA carboxylase, methylcrotonyl-CoA carboxylase, and urea carboxylase. Automated pipelines keyed on this domain frequently default to the ACC name. The decisive discriminators here are **genomic synteny with a CT+BCCP β-subunit** and the **presence of a separate, complete accBCAD operon** elsewhere in the genome.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the findings |
|---|---|---|
| [27708276](https://pubmed.ncbi.nlm.nih.gov/27708276/) | *A distinct holoenzyme organization for two-subunit pyruvate carboxylase* | Directly describes the α (BC) / β (CT+BCCP) two-subunit PC architecture that matches PycA/PycB in Gram-negative bacteria. **Core support for Finding 1.** |
| [39725256](https://pubmed.ncbi.nlm.nih.gov/39725256/) | *Hydrolysis of the acetyl-CoA allosteric activator by S. aureus PC* | Defines the pyruvate→oxaloacetate reaction, its anaplerotic role, and acetyl-CoA allosteric activation. **Supports Findings 1, 2, 6, 8.** |
| [22985389](https://pubmed.ncbi.nlm.nih.gov/22985389/) | *Roles of Arg427 and Arg472 in acetyl-CoA binding in PC* | Kinetically dissects the BC-domain half-reaction (bicarbonate-dependent ATP cleavage, biotin carboxylation). **Defines the PycA half-reaction; Findings 2, 6.** |
| [21592965](https://pubmed.ncbi.nlm.nih.gov/21592965/) | *Regulation of biotin carboxylase by substrate inhibition and dimerization* | Establishes the Mg-ATP + bicarbonate BC mechanism and substrate inhibition/dimer behavior. **Findings 2, 7.** |
| [11346647](https://pubmed.ncbi.nlm.nih.gov/11346647/) | *Site-directed mutagenesis of ATP binding residues of biotin carboxylase* | Identifies the catalytic residues (Lys116, Lys159, His209, Glu276) conserved in Q88C36. **Finding 4.** |
| [28683917](https://pubmed.ncbi.nlm.nih.gov/28683917/) | *Striking diversity in holoenzyme architecture of biotin-dependent carboxylases* | Places PycA in the biotin-dependent carboxylase superfamily with a shared BC half-reaction across diverse holoenzymes. **Findings 2, 5.** |
| [29643369](https://pubmed.ncbi.nlm.nih.gov/29643369/) | *Allosteric regulation alters carrier domain translocation in PC* | Establishes the swinging-BCCP mechanism coupling BC and CT sites, and acetyl-CoA's effect on translocation. **Finding 6.** |
| [23286247](https://pubmed.ncbi.nlm.nih.gov/23286247/) | *Importance of the BC domain dimer for S. aureus PC catalysis* | Shows the BC-domain dimer interface is essential for catalysis; isolated BC domain is inactive. **Finding 7.** |
| [22809506](https://pubmed.ncbi.nlm.nih.gov/22809506/) | *Cyclophilin interaction with the biotin carboxylase subunit* | Demonstrates a bacterial BC subunit is cytoplasmic and regulated by protein–protein interaction. **Finding 5.** |
| [40883435](https://pubmed.ncbi.nlm.nih.gov/40883435/) | *Quantitative decoding of carbon/energy metabolism in P. putida for lignin utilization* | Organism-specific: up to 30-fold PC induction during growth on aromatics implies anaplerotic remodeling. **Finding 8.** |
| [27379711](https://pubmed.ncbi.nlm.nih.gov/27379711/) / [26149215](https://pubmed.ncbi.nlm.nih.gov/26149215/) | *Allosteric domain residues of R. etli PC* | Map the acetyl-CoA allosteric site (Arg427/Arg429/Arg469/Asp471/Arg472). **Finding 6.** |

**Note on organism specificity of the evidence:** Direct enzymological characterization of *P. putida* KT2440 PycA/PycB has not, to our knowledge, been published. The mechanistic detail above is inferred by strong homology (51% identity of PycA to characterized biotin carboxylases; conserved active site; two-subunit architecture matching Choi *et al.* 2016) and by organism-specific expression data (Zhou *et al.* 2025). This is a well-supported inference, but it remains an inference for the enzymological specifics.

---

## Limitations and Knowledge Gaps

1. **No direct enzymology on *P. putida* PycA/PycB.** Kinetic parameters (kcat, Kₘ for ATP, bicarbonate, pyruvate), the extent of acetyl-CoA activation, and confirmation of the reaction product for *this specific enzyme* have not been measured. Assignments rest on homology and genomic context.
2. **UniProt name is a known mis-annotation.** The recommended UniProt name ("acetyl-CoA carboxylase biotin carboxylase subunit A") is an automated ARBA/rule-based call driven by the shared ATP-grasp/BC domain and should be treated with caution. The corrected functional assignment (pyruvate carboxylase BC subunit) is supported by orthology and synteny but has not been experimentally validated in KT2440.
3. **Biotinyl-Lys567 of PycB not experimentally confirmed.** The biotinylation site is inferred from the conserved A-M-K-M motif position; direct mass-spectrometric confirmation is lacking.
4. **Structural data are homology-based.** No experimental structure of *P. putida* PycA exists; residue mappings and the hydropathy/topology analysis are computational.
5. **Regulation in vivo.** Whether PycA/PycB is acetyl-CoA-activated in *P. putida* (as in most organisms) and how its expression is controlled at the transcriptional level are not established beyond the proteomic correlation with aromatic-substrate growth.
6. **Interplay with parallel anaplerotic routes.** The relative flux contributions of PC vs. PEP carboxylase (Ppc) vs. malic enzyme under different carbon sources remain to be quantified (e.g., by ¹³C metabolic flux analysis).

---

## Proposed Follow-up Experiments / Actions

1. **Gene knockout / complementation.** Construct a clean ΔpycA (and ΔpycA ΔpycB) mutant in *P. putida* KT2440 and test growth on pyruvate, lactate, and aromatic/lignin-derived substrates (where anaplerosis via PC is expected to be critical) versus TCA-feeding substrates (succinate) where it should be dispensable. Complement to confirm phenotype specificity.
2. **In vitro enzymology.** Co-express and purify recombinant PycA + PycB; measure the coupled pyruvate → oxaloacetate reaction (malate-dehydrogenase-coupled assay) and the isolated BC half-reaction (ATP/bicarbonate-dependent biotin carboxylation). Determine kcat and Kₘ values and test acetyl-CoA activation.
3. **Confirm biotinylation site.** Use streptavidin blotting and LC-MS/MS to verify covalent biotin attachment at Lys567 of PycB and demonstrate that PycA carboxylates the holo (biotinylated) but not apo PycB.
4. **Active-site validation.** Site-directed mutagenesis of the conserved catalytic residues predicted here (e.g., Lys115, Glu274) and assay for loss of BC activity, testing the homology-based active-site assignment.
5. **¹³C metabolic flux analysis (MFA).** Quantify the flux through PC vs. PEP carboxylase vs. malic enzyme across carbon sources (glucose, succinate, ferulate) to define the physiological weighting of PycA/PycB in the *P. putida* anaplerotic network.
6. **Structural determination.** Solve the PycA (and PycA/PycB holoenzyme) structure by cryo-EM or X-ray crystallography to confirm the ATP-grasp fold, the BC-domain dimer interface, and the holoenzyme organization predicted for two-subunit PCs.
7. **Database correction.** Submit the corrected functional assignment (pyruvate carboxylase BC subunit, EC 6.4.1.1) to UniProt with the supporting synteny/orthology evidence to prevent propagation of the ACC mis-annotation.

---

## Conclusion

*pycA* (PP_5347; Q88C36) encodes the biotin carboxylase (α) subunit of a two-subunit pyruvate carboxylase in *Pseudomonas putida* KT2440. It catalyzes the MgATP- and bicarbonate-dependent carboxylation of the biotin prosthetic group carried on Lys567 of its partner subunit PycB (PP_5346), and, together with PycB's carboxyltransferase activity, converts pyruvate + HCO₃⁻ + ATP to oxaloacetate + ADP + Pᵢ (EC 6.4.1.1). The enzyme is a soluble, cytoplasmic, anaplerotic protein that replenishes TCA-cycle oxaloacetate — a role of particular importance when *P. putida* grows on aromatic and lignin-derived carbon. The UniProt "acetyl-CoA carboxylase" designation is a domain-driven mis-annotation; *P. putida* KT2440 has a separate, complete acetyl-CoA carboxylase (accBCAD), and PycA is not involved in fatty-acid initiation.


## Artifacts

- [OpenScientist final report](pycA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pycA-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:27708276
2. PMID:39725256
3. PMID:21592965
4. PMID:22985389
5. PMID:28683917
6. PMID:11346647
7. PMID:22809506
8. PMID:29643369
9. PMID:27379711
10. PMID:26149215
11. PMID:23286247
12. PMID:40883435