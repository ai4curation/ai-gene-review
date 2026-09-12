---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T06:05:25.311690'
end_time: '2026-07-17T06:17:34.296909'
duration_seconds: 728.99
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: serC
  gene_symbol: serC
  uniprot_accession: Q88M07
  protein_description: 'RecName: Full=Phosphoserine aminotransferase {ECO:0000255|HAMAP-Rule:MF_00160};
    EC=2.6.1.52 {ECO:0000255|HAMAP-Rule:MF_00160}; AltName: Full=Phosphohydroxythreonine
    aminotransferase {ECO:0000255|HAMAP-Rule:MF_00160}; Short=PSAT {ECO:0000255|HAMAP-Rule:MF_00160};'
  gene_info: Name=serC {ECO:0000255|HAMAP-Rule:MF_00160}; OrderedLocusNames=PP_1768;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the class-V pyridoxal-phosphate-dependent
  protein_domains: Aminotrans_V_dom. (IPR000192); Pser_aminoTfrase. (IPR022278); PyrdxlP-dep_Trfase.
    (IPR015424); PyrdxlP-dep_Trfase_major. (IPR015421); PyrdxlP-dep_Trfase_small.
    (IPR015422)
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
citation_count: 5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: serC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: serC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88M07
- **Protein Description:** RecName: Full=Phosphoserine aminotransferase {ECO:0000255|HAMAP-Rule:MF_00160}; EC=2.6.1.52 {ECO:0000255|HAMAP-Rule:MF_00160}; AltName: Full=Phosphohydroxythreonine aminotransferase {ECO:0000255|HAMAP-Rule:MF_00160}; Short=PSAT {ECO:0000255|HAMAP-Rule:MF_00160};
- **Gene Information:** Name=serC {ECO:0000255|HAMAP-Rule:MF_00160}; OrderedLocusNames=PP_1768;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the class-V pyridoxal-phosphate-dependent
- **Key Domains:** Aminotrans_V_dom. (IPR000192); Pser_aminoTfrase. (IPR022278); PyrdxlP-dep_Trfase. (IPR015424); PyrdxlP-dep_Trfase_major. (IPR015421); PyrdxlP-dep_Trfase_small. (IPR015422)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "serC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'serC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **serC** (gene ID: serC, UniProt: Q88M07) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *serC* (Q88M07 / PP_1768) in *Pseudomonas putida* KT2440

## Gene / Protein Identity — Verified

| Field | Value |
|---|---|
| UniProt | Q88M07 (SERC_PSEPK) |
| Gene | *serC* (alias *pdxF*); OrderedLocusName PP_1768 |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) |
| Enzyme | Phosphoserine aminotransferase (PSAT); also phosphohydroxythreonine aminotransferase |
| EC | 2.6.1.52 |
| Family | Class-V (fold-type IV) pyridoxal-5′-phosphate (PLP)–dependent aminotransferase |
| Domains | Aminotrans_V (IPR000192); Pser_aminoTfrase (IPR022278); PLP-dep transferase major+small (IPR015421/IPR015422) |
| Length | 361 aa |

**Identity confirmed — no ambiguity.** The gene symbol *serC*, the EC number, the class-V/fold-type IV PLP domain architecture, and the organism all agree between the UniProt record and the primary literature retrieved. Functional-genomic work in the genus *Pseudomonas* explicitly assigns *serC* the "3-phosphoserine aminotransferase" activity by homology, direct enzyme assay, and functional complementation ([PMID: 10368439](https://pubmed.ncbi.nlm.nih.gov/10368439/)). This is the serine/vitamin-B6 biosynthetic aminotransferase, not an unrelated same-symbol gene.

---

## Summary

**serC (Q88M07 / PP_1768) in *Pseudomonas putida* KT2440 encodes phosphoserine aminotransferase (PSAT; EC 2.6.1.52), a soluble cytoplasmic, PLP-dependent, homodimeric class-V (fold-type IV) aminotransferase.** Its primary function is to catalyze the **reversible, L-glutamate-linked transamination of 3-phosphohydroxypyruvate (3-PHP) to O-phospho-L-serine**, generating α-ketoglutarate (2-oxoglutarate) as co-product. This is the **second of three committed steps** of the phosphorylated pathway of L-serine biosynthesis: **SerA → SerC → SerB**.

The enzyme is **bifunctional** (hence the alias *pdxF*). In addition to serine biosynthesis, it transaminates the erythronate-derived keto-acid intermediate ("2-ketoerythroic acid 4-phosphate") to **4-phospho-hydroxy-L-threonine** in the de novo biosynthesis of **pyridoxal-5′-phosphate (vitamin B6)**. Because *P. putida* KT2440 uses the deoxyxylulose-5-phosphate (DXP)-dependent, *E. coli*-type B6 route (encoding *pdxA/B/J/H* but lacking the alternative *pdxS/pdxT* system), this second catalytic activity is biologically operative. In *Pseudomonas* specifically, SerC/PdxF additionally supplies side-chain amino groups feeding aromatic amino acid biosynthesis (Trp, Phe, Tyr).

Structurally, the protein is a **homodimer of ~361-residue subunits** with two shared active sites at the subunit interface and PLP bound as an internal aldimine to a conserved active-site lysine (E. coli Lys198 → *P. putida* **Lys197**). Q88M07 shares **58.2% sequence identity** with the crystallographically characterized *E. coli* enzyme, with the full catalytic machinery conserved, and carries no signal peptide or transmembrane segment — establishing it as a **soluble cytoplasmic enzyme** that operates in the cytosol where its substrates are generated. This report consolidates six confirmed findings supported by five core publications plus bioinformatic analysis.

---

## Key Findings

### F001 — serC is a PLP-dependent phosphoserine aminotransferase catalyzing the second step of phosphorylated L-serine biosynthesis

The core, primary function of *serC*/PP_1768 is **phosphoserine aminotransferase (PSAT, EC 2.6.1.52)**. The catalyzed reaction is:

> **3-phosphohydroxypyruvate + L-glutamate ⇌ O-phospho-L-serine + 2-oxoglutarate**

The reaction is reversible, **PLP-dependent**, and proceeds through a **bimolecular ping-pong (Bi-Bi)** mechanism in which the PLP cofactor cycles between the pyridoxal (PLP) and pyridoxamine (PMP) forms — the amino group is first transferred from L-glutamate to enzyme-bound PLP (releasing α-ketoglutarate), then from PMP to 3-PHP (yielding O-phospho-L-serine). It is the **second of three steps** in the phosphorylated pathway of L-serine biosynthesis:

```
   3-phosphoglycerate
        │  SerA (3-PGA dehydrogenase; NAD+-dependent oxidation)
        ▼
   3-phosphohydroxypyruvate (3-PHP)
        │  SerC (PSAT; PLP-dependent, L-Glu → α-KG transamination)   ← THIS ENZYME
        ▼
   O-phospho-L-serine
        │  SerB (phosphoserine phosphatase; hydrolysis)
        ▼
   L-serine
```

The plant PSAT study defines the reaction and mechanism for the family: PSAT "*catalyzes the conversion of 3-phosphohydroxypyruvate (3-PHP) to 3-phosphoserine (PSer) in an L-glutamate (Glu)-linked reversible transamination reaction... through a bimolecular ping-pong mechanism*" ([PMID: 30034403](https://pubmed.ncbi.nlm.nih.gov/30034403/)). The EC number and reaction are confirmed for the bacterial orthologue: PSAT "*catalyses the conversion of 3-phosphohydroxypyruvate to l-phosphoserine*" ([PMID: 10024454](https://pubmed.ncbi.nlm.nih.gov/10024454/)). Direct evidence in the genus *Pseudomonas* establishes that *serC* "*encodes 3-phosphoserine aminotransferase*" ([PMID: 10368439](https://pubmed.ncbi.nlm.nih.gov/10368439/)).

**Substrate specificity:** the amino-group donor is L-glutamate; the acceptor is the phosphorylated keto acid 3-phosphohydroxypyruvate — the phosphate group is a specificity determinant recognized by conserved active-site arginines and histidines.

### F002 — serC/PdxF is bifunctional, also acting in vitamin B6 (PLP) biosynthesis and providing amino groups for aromatic amino acids

*serC* is the same protein as **PdxF**. In enteric bacteria the locus is described as "*corresponds to serC, the bifunctional gene for phosphoserine-oxoglutarate aminotransferase (SerC) and 2-ketoerythroic acid 4-phosphate transaminase (PdxF)*" ([PMID: 11016848](https://pubmed.ncbi.nlm.nih.gov/11016848/)). In this second role the enzyme transaminates (with glutamate) the erythronate-derived keto acid to **4-phospho-hydroxy-L-threonine**, a dedicated precursor of PLP in the DXP-dependent route.

In *Pseudomonas*, the gene sits within a **mixed-function supraoperon**, and the enzyme's role extends further: although "*SerC(PdxF) and HisHb exercise their primary functions in serine, pyridoxine, and histidine biosynthesis, they also have critical catalytic roles in provision of the sidechain amino groups of tryptophan, phenylalanine, and tyrosine*" ([PMID: 10368439](https://pubmed.ncbi.nlm.nih.gov/10368439/)). Thus in *P. putida*, a single enzyme feeds three biosynthetic outputs: (1) O-phospho-L-serine → L-serine; (2) 4-phospho-hydroxy-L-threonine → PLP/vitamin B6; and (3) amino-group provision for aromatic amino acid biosynthesis.

### F003 — serC is a cytoplasmic homodimeric class-V PLP fold-type IV aminotransferase with PLP bound to an active-site lysine

Crystallography of the *E. coli* orthologue defines the architecture. PSAT is a **homodimer** of ~361-residue subunits: "*Each subunit (361 residues) of the PSAT homodimer is composed of a large pyridoxal-5′-phosphate binding domain*" ([PMID: 10024454](https://pubmed.ncbi.nlm.nih.gov/10024454/)) — a seven-stranded, mostly parallel β-sheet — plus a smaller C-terminal domain. The PLP cofactor is held as an **internal aldimine (Schiff base)** to the active-site lysine: "*The cofactor is bound through an aldimine linkage to Lys198 in the active site*" ([PMID: 10024454](https://pubmed.ncbi.nlm.nih.gov/10024454/)). Substrate carboxylate/phosphate groups are coordinated by Ser9, Arg335, His41, Arg42, His328 and Arg77. This matches the UniProt/InterPro assignment of Q88M07 as a **class-V (subgroup IV) PLP-dependent aminotransferase**. The enzyme functions as an obligate homodimer with two shared active sites at the subunit interface, consistent with the plant PSAT structure ([PMID: 30034403](https://pubmed.ncbi.nlm.nih.gov/30034403/)).

### F004 — Q88M07 shares 58% identity with E. coli PSAT with catalytic and substrate-binding residues conserved

A global pairwise alignment of *P. putida* serC (Q88M07, 361 aa) against the experimentally characterized *E. coli* PSAT (P23721 / SERC_ECOLI, 362 aa) gives **58.2% sequence identity** (209 of 359 aligned columns). Critically, the **catalytic active-site lysine** that forms the PLP internal aldimine is conserved (E. coli Lys198 → *P. putida* **Lys197**, in the conserved **AGAQ-K197-NIGP** motif), as are the substrate/cofactor-coordinating residues:

| Residue role | *E. coli* PSAT | *P. putida* Q88M07 |
|---|---|---|
| Catalytic lysine (PLP aldimine) | Lys198 | **Lys197** |
| Substrate coordination | His41 | His42 |
| Substrate coordination | Arg42 | Arg43 |
| Substrate coordination | His328 | His327 |
| Carboxylate binding | Arg335 | Arg334 |
| Overall identity | — | **58.2%** |

This level of identity, precise conservation of the catalytic machinery, matching subunit length, and identical InterPro domain architecture (Aminotrans_V IPR000192; Pser_aminoTfrase IPR022278; fold-type IV major + small PLP domains) provide strong structure/evolution-based evidence for transferring the experimentally established EC 2.6.1.52 function to Q88M07. The anchoring fact: the E. coli catalytic lysine "*is bound through an aldimine linkage to Lys198 in the active site*" ([PMID: 10024454](https://pubmed.ncbi.nlm.nih.gov/10024454/)), conserved as Lys197 in *P. putida*.

### F005 — P. putida KT2440 uses the DXP-dependent (E. coli-type) vitamin B6 pathway, making serC's PdxF role operative

A genome/KEGG survey of *P. putida* KT2440 shows it encodes the **complete DXP-dependent** vitamin B6 biosynthesis pathway and lacks the alternative DXP-independent *pdxS/pdxT* (Pdx1/Pdx2) genes:

| Gene | Locus | Enzyme |
|---|---|---|
| *pdxB* | PP_2117 | erythronate-4-phosphate dehydrogenase |
| ***serC*** | **PP_1768** | **phosphoserine / PdxF aminotransferase (this gene)** |
| *pdxA* | PP_0402 | 4-hydroxythreonine-4-phosphate dehydrogenase |
| *pdxJ* | PP_1436 | pyridoxine-5′-phosphate synthase |
| *pdxH* | PP_1129 | PNP/PMP oxidase |

Because the DXP-dependent route proceeds through **4-phosphohydroxy-L-threonine**, whose formation requires the SerC transamination step, *serC*/PP_1768 supplies **both** O-phospho-L-serine (serine pathway) and 4-phospho-hydroxy-L-threonine (PLP pathway) in this organism. The B6 review defines the route: the vitamin "*is synthesized from the condensation of deoxyxylulose 5-phosphate and 4-phosphohydroxy-L-threonine catalysed by the concerted action of PdxA and PdxJ*" ([PMID: 17822383](https://pubmed.ncbi.nlm.nih.gov/17822383/)), whereas the alternative route "*is characterized by the presence of two genes, Pdx1 and Pdx2*" ([PMID: 17822383](https://pubmed.ncbi.nlm.nih.gov/17822383/)) and bypasses the SerC-dependent intermediate. The presence of *pdxA/pdxJ* and absence of *pdxS/pdxT* is precisely what makes serC's B6 role operative in *P. putida*. Notably, the three serine-pathway genes are **dispersed** in KT2440 (serA PP_5155, serC PP_1768, serB PP_4909) rather than co-operonic.

### F006 — Q88M07 is a soluble cytoplasmic enzyme with no signal peptide or transmembrane segment

Sequence-based localization analysis of Q88M07 (361 aa) confirms a **cytoplasmic** location. There is **no hydrophobic transmembrane helix** (maximum Kyte-Doolittle hydropathy over a 19-residue window = 1.15, well below the ~1.6 threshold for a TM segment) and **no N-terminal secretory signal peptide** (the N-terminus MSKRAFNFC… begins with charged/polar residues K3/R4 and lacks a hydrophobic h-region). These features, together with the crystallographically established soluble homodimeric fold of orthologues, indicate serC operates as a soluble **cytosolic** enzyme in *P. putida*, where all of its substrates (3-PHP, L-glutamate, and the B6-pathway keto acid) are generated by other cytoplasmic enzymes. In compartmentalized eukaryotes the homolog is a soluble organellar enzyme — PSAT "*in plants takes place in plastids*" ([PMID: 30034403](https://pubmed.ncbi.nlm.nih.gov/30034403/)) — consistent with a soluble, non-membrane-bound enzyme localizing to the bacterial cytoplasm.

---

## Mechanistic Model / Interpretation

The findings converge into a coherent picture of a **single bifunctional PLP enzyme serving as a metabolic hub** for three biosynthetic outputs in *P. putida* KT2440.

### Catalytic mechanism (ping-pong Bi-Bi)

```
Half-reaction 1 (amino donor):
   L-glutamate + E-PLP  ⇌  α-ketoglutarate + E-PMP

Half-reaction 2 (amino acceptor, serine pathway):
   3-phosphohydroxypyruvate + E-PMP  ⇌  O-phospho-L-serine + E-PLP

Half-reaction 2′ (amino acceptor, B6 pathway):
   2-oxo-3-hydroxy-4-phosphobutanoate + E-PMP  ⇌  4-phospho-hydroxy-L-threonine + E-PLP
```

The enzyme cycles between the PLP (aldimine) and PMP (amine) forms of its cofactor, covalently tethered to Lys197. The dual amino-acceptor specificity (half-reactions 2 and 2′) is the structural basis for its bifunctionality: the active site accommodates two structurally related phosphorylated keto-acid substrates.

### Metabolic integration

```
                         L-glutamate
                              │  (amino donor)
                              ▼
    3-PGA ──SerA──► 3-PHP ──[SerC/PSAT]──► O-phospho-L-serine ──SerB──► L-SERINE
                                 │  (α-KG released)                         │
                                 │                          ┌──────────────┴──────────────┐
                                 │                        glycine + 1C/folate, cysteine,
                                 │                        phospholipid head groups
    erythronate-4-P ──PdxB──► keto-acid ──[SerC/PdxF]──► 4-P-OH-L-Thr ──PdxA/PdxJ/PdxH──► PLP (VITAMIN B6)
                                 │
                                 └──► amino-group provision ──► Trp / Phe / Tyr (aromatic AAs)
```

serC is a node whose loss would simultaneously impair serine, vitamin B6, and aromatic amino acid biosynthesis — an unusually pleiotropic yet mechanistically precise role. Its serine product is the precursor of **glycine and one-carbon (folate) units** (via serine hydroxymethyltransferase), **cysteine**, and phospholipid head groups, and L-serine is itself an amino donor and osmolyte. The dispersed genomic organization of the serine genes (serA/serC/serB not co-operonic) contrasts with the *Pseudomonas* "mixed-function supraoperon" context reported for serC/pdxF, reflecting regulatory integration of these amphibolic functions.

### Localization

All substrates and downstream pathway enzymes are cytoplasmic, and the protein carries no export or membrane-anchoring signals. The enzyme therefore performs its catalysis in the **cytosol**, forming a soluble homodimer with two interface-shared active sites.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [10024454](https://pubmed.ncbi.nlm.nih.gov/10024454/) | *Crystal structure of phosphoserine aminotransferase from E. coli at 2.3 Å* | Defines EC 2.6.1.52, reaction, homodimeric fold, and PLP–Lys198 aldimine; the primary structural anchor for functional transfer |
| [10368439](https://pubmed.ncbi.nlm.nih.gov/10368439/) | *A probable mixed-function supraoperon in Pseudomonas…* | Direct genus-level evidence that serC encodes 3-phosphoserine aminotransferase (homology + assay + complementation); documents bifunctional/aromatic-AA roles |
| [30034403](https://pubmed.ncbi.nlm.nih.gov/30034403/) | *Structural Analysis of Phosphoserine Aminotransferase (Isoform 1)…* | Defines substrates, PLP dependence, ping-pong mechanism, and soluble/organellar localization of the PSAT family |
| [11016848](https://pubmed.ncbi.nlm.nih.gov/11016848/) | *Regulation of septation: a novel role for SerC/PdxF in Salmonella?* | States serC is the bifunctional SerC/PdxF gene serving both serine and pyridoxine (B6) biosynthesis |
| [17822383](https://pubmed.ncbi.nlm.nih.gov/17822383/) | *Two independent routes of de novo vitamin B6 biosynthesis* | Distinguishes DXP-dependent (SerC-using) vs Pdx1/Pdx2 routes; underpins the inference that KT2440's B6 role for serC is operative |

Three additional papers surfaced during literature search (PMID 40076802, 38806671, 29483190) concern *serC*/serine metabolism in *Mycobacterium* and *Staphylococcus* and are peripheral to *P. putida* function; they were not used to support the core findings.

**How the evidence supports the conclusion:** The annotation rests on triangulation of (1) direct enzymological/genetic evidence within the genus *Pseudomonas* [PMID: 10368439], (2) high-resolution structural/mechanistic characterization of well-studied orthologues (E. coli, plant) [PMID: 10024454; 30034403], (3) explicit bifunctionality evidence in enteric bacteria [PMID: 11016848], (4) genome-context confirmation that the B6 route requiring SerC is present in KT2440 [PMID: 17822383], and (5) bioinformatic conservation analysis (58% identity, conserved catalytic Lys197 and substrate-binding residues, no membrane/signal features). No evidence challenges the annotation.

---

## Supported and Refuted Hypotheses

**Supported**
- serC = phosphoserine aminotransferase (EC 2.6.1.52), catalyzing 3-PHP + L-glutamate ⇌ O-phospho-L-serine + 2-oxoglutarate (structural, enzymatic, genus-level, and bioinformatic evidence).
- serC is bifunctional (serC/pdxF) and, given KT2440's DXP-dependent B6 pathway and absence of pdxS/pdxT, also acts in vitamin B6 biosynthesis.
- serC is a soluble, cytoplasmic, homodimeric PLP enzyme; catalytic Lys197 conserved.

**Refuted / excluded**
- Not a membrane transporter, not secreted/periplasmic (no TM segment, no signal peptide).
- Not dependent on the pdxS/pdxT B6 route (those genes are absent), so its B6 contribution is not bypassed as it would be in many other bacteria.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of Q88M07 itself.** The assignment for KT2440 PP_1768 is inferred from orthologues and genus-level (not strain-level) evidence; no purified-enzyme kinetics (Km, kcat, directional preference) or crystal structure exists for the KT2440 protein specifically.
2. **Residue numbering derives from bioinformatic alignment**, not an experimental *P. putida* structure; while conservation is strong, the exact active-site geometry of Q88M07 has not been solved.
3. **Quantitative flux partitioning is unknown** — how SerC apportions capacity among serine, B6, and aromatic amino acid biosynthesis under different growth conditions has not been measured.
4. **Regulation is uncharacterized in KT2440** (e.g., response to serine stress or B6 limitation).
5. **The PdxF (keto-acid transaminase) activity** is annotated by orthology; direct demonstration for the KT2440 enzyme is absent.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and enzyme kinetics.** Purify Q88M07 and assay both PSAT (3-PHP → O-phospho-L-serine) and PdxF (keto-acid → 4-phospho-hydroxy-L-threonine) activities; determine Km, kcat, and PLP dependence to confirm bifunctionality directly.
2. **Gene knockout and complementation.** Delete PP_1768 in KT2440 and test for serine (and possibly pyridoxine) auxotrophy on minimal media; complement with cloned KT2440 serC and E. coli serC to confirm functional equivalence.
3. **Structural determination.** Solve the crystal or cryo-EM structure (with/without α-methyl-L-glutamate or substrate analogs) to verify the predicted active-site geometry and Lys197 aldimine.
4. **Subcellular localization confirmation.** Use fluorescent-protein fusion or cell fractionation to experimentally verify predicted cytoplasmic localization.
5. **Metabolic flux analysis.** Use ¹³C-labeling to quantify partitioning of serC-mediated transamination among serine, B6, and aromatic pathways.
6. **Regulatory investigation.** Examine transcriptional regulation of serC under serine stress and B6 limitation.

---

## References (PMIDs)

- Hester G. et al. (1999) *Crystal structure of phosphoserine aminotransferase from E. coli at 2.3 Å.* [PMID: 10024454](https://pubmed.ncbi.nlm.nih.gov/10024454/)
- Sekula B. et al. (2018) *Structural analysis of phosphoserine aminotransferase isoform 1.* [PMID: 30034403](https://pubmed.ncbi.nlm.nih.gov/30034403/)
- Xie G. et al. (1999) *A probable mixed-function supraoperon in Pseudomonas (serC/pdxF).* [PMID: 10368439](https://pubmed.ncbi.nlm.nih.gov/10368439/)
- Mouslim C. et al. (2000) *Regulation of septation: a novel role for SerC/PdxF in Salmonella?* [PMID: 11016848](https://pubmed.ncbi.nlm.nih.gov/11016848/)
- Fitzpatrick T.B. et al. (2007) *Two independent routes of de novo vitamin B6 biosynthesis.* [PMID: 17822383](https://pubmed.ncbi.nlm.nih.gov/17822383/)

---

*Report generated from 5 completed research iterations, 6 confirmed findings, and 8 reviewed publications. All functional claims are supported by cited primary literature and bioinformatic analysis of the target sequence Q88M07.*


## Artifacts

- [OpenScientist final report](serC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](serC-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:10368439
2. PMID:30034403
3. PMID:10024454
4. PMID:11016848
5. PMID:17822383