---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T16:46:23.661295'
end_time: '2026-07-17T17:05:43.844245'
duration_seconds: 1160.18
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: aruC
  gene_symbol: aruC
  uniprot_accession: Q88QW2
  protein_description: 'SubName: Full=Acetylornithine aminotransferase 2 {ECO:0000313|EMBL:AAN66003.1};
    EC=2.6.1.11 {ECO:0000313|EMBL:AAN66003.1}; EC=2.6.1.13 {ECO:0000313|EMBL:AAN66003.1};'
  gene_info: Name=aruC {ECO:0000313|EMBL:AAN66003.1}; OrderedLocusNames=PP_0372 {ECO:0000313|EMBL:AAN66003.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the class-III pyridoxal-phosphate-dependent
  protein_domains: Aminotrans_3. (IPR005814); Aminotrans_3_PPA_site. (IPR049704);
    Class-III_PLP-dep_AT. (IPR050103); PyrdxlP-dep_Trfase. (IPR015424); PyrdxlP-dep_Trfase_major.
    (IPR015421)
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
citation_count: 6
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: aruC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: aruC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88QW2
- **Protein Description:** SubName: Full=Acetylornithine aminotransferase 2 {ECO:0000313|EMBL:AAN66003.1}; EC=2.6.1.11 {ECO:0000313|EMBL:AAN66003.1}; EC=2.6.1.13 {ECO:0000313|EMBL:AAN66003.1};
- **Gene Information:** Name=aruC {ECO:0000313|EMBL:AAN66003.1}; OrderedLocusNames=PP_0372 {ECO:0000313|EMBL:AAN66003.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the class-III pyridoxal-phosphate-dependent
- **Key Domains:** Aminotrans_3. (IPR005814); Aminotrans_3_PPA_site. (IPR049704); Class-III_PLP-dep_AT. (IPR050103); PyrdxlP-dep_Trfase. (IPR015424); PyrdxlP-dep_Trfase_major. (IPR015421)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "aruC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'aruC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **aruC** (gene ID: aruC, UniProt: Q88QW2) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *aruC* / PP_0372 (UniProt Q88QW2) in *Pseudomonas putida* KT2440

## Summary

**PP_0372 (UniProt Q88QW2), labelled "aruC," encodes a cytoplasmic, pyridoxal-5′-phosphate (PLP)-dependent class-III aminotransferase whose primary annotated function is acetylornithine aminotransferase (EC 2.6.1.11), the ArgD step of L-arginine biosynthesis.** In this reaction the enzyme catalyses the reversible transamination *N*-acetyl-L-glutamate-5-semialdehyde + L-glutamate ⇌ *N*²-acetyl-L-ornithine + 2-oxoglutarate (KEGG reaction R02283), converting a glutamate-derived carbon skeleton into the acetylated ornithine precursor of arginine. The protein carries the diagnostic Aminotrans_3 fold and an intact class-III active site, and it belongs to a family whose members characteristically prefer *N*-acylated ornithine substrates over free ornithine.

**A central conclusion of this investigation is that the "aruC" gene symbol is an annotation artifact and does NOT denote the catabolic arginine-succinyltransferase (AST) pathway enzyme.** The genuine *aruC* of the AST catabolic pathway — N²-succinylornithine 5-aminotransferase (EC 2.6.1.81) — was originally defined in *Pseudomonas aeruginosa* (gene PA0895) and, in *P. putida* KT2440, is encoded by a separate gene, **PP_4481**, sitting within a complete, dedicated catabolic AST gene cluster (PP_4475–PP_4481). PP_0372 instead maps by KEGG orthology to K00821 (anabolic acetylornithine/*N*-succinyl-DAP aminotransferase), lies in an unrelated genomic neighborhood, and is only ~40–42 % identical to the characterized catabolic AruC/AstC/ArgD clade while being 61 % identical to its true anabolic ortholog PA0530.

**The family to which PP_0372 belongs is experimentally bifunctional.** The archetypal enzyme, *E. coli* ArgD, exhibits both *N*-acetylornithine aminotransferase activity (arginine biosynthesis, EC 2.6.1.11) and *N*-succinyl-L,L-diaminopimelate aminotransferase activity (DapC, lysine biosynthesis, EC 2.6.1.17), with comparable specificity constants for both substrates. Accordingly, KEGG assigns PP_0372 to modules for both arginine biosynthesis (ppu00220) and succinyl-DAP lysine biosynthesis (M00016), and UniProt lists EC 2.6.1.11 and 2.6.1.13. **The key caveat is that all substrate and localization assignments for PP_0372 derive from orthology, genomic context, and conserved active-site residues — no direct enzymology has been performed on PP_0372 or its close ortholog PA0530 themselves.**

---

## Key Findings

### F1 — The catabolic AruC function: N²-succinylornithine 5-aminotransferase in the AST pathway

The gene symbol *aruC* was coined in *Pseudomonas aeruginosa* PAO1, where cloning and sequencing of the 26-kb *aru* cluster established that the *aruCFGDB* operon, under the control of the ArgR regulator, encodes the enzymes of the catabolic **arginine succinyltransferase (AST) pathway**. In that landmark study, AruC was assigned the function of **N²-succinylornithine 5-aminotransferase**, one step in the five-enzyme route that dissimilates arginine via succinylated intermediates ([PMID: 9393691](https://pubmed.ncbi.nlm.nih.gov/9393691/)). The verified quotation is unambiguous: *"The aruR, aruC, aruD, aruB, and aruE genes specify the ArgR regulatory protein, N2-succinylornithine 5-aminotransferase, N-succinylglutamate 5-semialdehyde dehydrogenase, N2-succinylarginine dihydrolase, and N-succinylglutamate desuccinylase, respectively."*

This finding matters because it defines what "*aruC*" *originally* means — a catabolic enzyme (EC 2.6.1.81) — and thereby frames the central identification problem: the *P. putida* protein Q88QW2, though bearing the same label, is not this catabolic enzyme (see F4).

### F2 — Class-III PLP fold with specificity for N-acylated ornithine

The acyl-ornithine aminotransferase family is defined structurally and mechanistically by work on the *E. coli* catabolic homolog **AstC**. X-ray structures of AstC in apo, holo (PLP-bound), and succinylornithine-bound states, complemented by docking, showed that AstC (catabolic) and ArgD (anabolic) are only **58 % identical yet functionally interchangeable** ([PMID: 23484010](https://pubmed.ncbi.nlm.nih.gov/23484010/)): *"Escherichia coli possesses two acyl ornithine aminotransferases, one catabolic (AstC) and the other anabolic (ArgD), that participate in L-arginine metabolism. Although only 58% identical, the enzymes have been shown to be functionally interchangeable."*

Critically, the same study established the substrate-specificity logic of the entire family: *"The docking studies support our observations that AstC has a strong preference for acylated ornithine species over ornithine itself, and suggest that the increase in specificity associated with acylation is caused by steric and desolvation effects rather than specific interactions between the substrate and enzyme."* This means the enzymes discriminate the acyl group (succinyl- or acetyl-) primarily through steric and desolvation effects rather than dedicated binding contacts — explaining why members of this family can accommodate more than one acyl-ornithine substrate and why the family gives rise to the multiple EC numbers (2.6.1.11 / 2.6.1.13 / 2.6.1.17 / 2.6.1.81) seen across paralogs. Q88QW2 belongs to this Aminotrans_3 (IPR005814) / class-III (IPR050103) family.

### F3 — The AST pathway dissimilates the arginine/ornithine carbon skeleton in *P. putida*

In *Pseudomonas*, including *P. putida*, the AST pathway is inducible by arginine and is responsible for catabolizing the carbon backbone of arginine. Direct in vivo evidence comes from inhibitor studies: blocking succinylornithine transaminase (the AruC step) with aminooxyacetic acid caused **accumulation of succinylornithine**, demonstrating that this pathway dissimilates the arginine carbon skeleton ([PMID: 3129535](https://pubmed.ncbi.nlm.nih.gov/3129535/)): *"The accumulation of succinylornithine following in vivo inhibition of succinylornithine transaminase activity by aminooxyacetic acid showed that this pathway is responsible for the dissimilation of the carbon skeleton of arginine."* Genetic dissection of *P. putida* mutants further mapped arginine utilization to both the AST pathway and the arginine oxidase route, with arginine channelled mainly through the oxidase route ([PMID: 1791443](https://pubmed.ncbi.nlm.nih.gov/1791443/)). This establishes the physiological context of the catabolic AruC — but again, this is the PP_4481 enzyme, not PP_0372.

### F4 — PP_0372 is the ANABOLIC acetylornithine aminotransferase, not the catabolic AST enzyme

This is the pivotal correction of the database label. Multiple orthogonal lines of bioinformatic evidence converge:

| Line of evidence | Observation |
|---|---|
| **KEGG orthology** | PP_0372 → **K00821** (acetylornithine / *N*-succinyl-DAP aminotransferase, EC 2.6.1.11 / 2.6.1.17), pathway **ppu00220 Arginine biosynthesis** + module **M00016** (succinyl-DAP lysine biosynthesis) |
| ***P. aeruginosa* ortholog** | PA0530 — also K00821, class-III PLP AT, arginine biosynthesis (the true anabolic ortholog) |
| **Genuine catabolic *aruC***| *P. aeruginosa* PA0895 — **K00840**, succinylornithine aminotransferase, EC 2.6.1.81 (matches [PMID: 9393691](https://pubmed.ncbi.nlm.nih.gov/9393691/)) |
| **KT2440 catabolic cluster** | Separate, complete AST cluster **PP_4475–PP_4481** (module M00879, arginine→glutamate); its dedicated succinylornithine aminotransferase is **PP_4481** (K00840) |
| **Genomic neighborhood** | PP_0372 is flanked by an acyl-CoA dehydrogenase (PP_0370), a LysR-family regulator (PP_0371), and a membrane protein (PP_0373) — **no *aru*/*ast* genes nearby** |

Thus PP_0372 and the catabolic AST enzyme are distinct gene products with distinct KEGG orthology (K00821 vs K00840), distinct EC numbers (2.6.1.11 vs 2.6.1.81), distinct pathways (biosynthesis vs catabolism), and distinct genomic locations. The "aruC" symbol applied to PP_0372 is an annotation artifact propagated from the ambiguous acyl-ornithine aminotransferase family.

### F5 — The ArgD family is experimentally bifunctional (arginine + lysine biosynthesis)

The anabolic identity of PP_0372 is reinforced by direct enzymology on its family archetype. Purified *E. coli* *argD*-encoded *N*-acetylornithine aminotransferase was shown to possess **both** activities: *N*-acetylornithine aminotransferase (EC 2.6.1.11, arginine biosynthesis) **and** *N*-succinyl-L,L-diaminopimelate aminotransferase (DapC, EC 2.6.1.17, lysine biosynthesis), with similar specificity constants for the two substrates ([PMID: 10074354](https://pubmed.ncbi.nlm.nih.gov/10074354/)): *"This enzyme exhibits both NAcOATase and DapATase activity, with similar specificity constants for N-acetylornithine and N-succinyl-L,L-DAP, suggesting that it can function in both lysine and arginine biosynthesis."* Because PP_0372 is orthologous to this ArgD (KEGG K00821, member of both arginine-biosynthesis and succinyl-DAP-lysine-biosynthesis modules), the same dual biosynthetic capability is the most parsimonious prediction for PP_0372.

### F6 — PP_0372 belongs to a divergent *Pseudomonas* acetylornithine-AT subfamily

Global pairwise alignments quantify the phylogenetic placement of PP_0372 and confirm it is anabolic:

| Comparison | % identity to PP_0372 | Clade |
|---|---|---|
| **PA0530** (*P. aeruginosa*, K00821, arginine biosynthesis) | **61.2 %** | anabolic (true ortholog) |
| *P. aeruginosa* AruC / PA0895 (catabolic, K00840) | 42.0 % | catabolic |
| KT2440 catabolic PP_4481 (K00840) | 42.1 % | catabolic |
| *E. coli* ArgD | 40.7 % | anabolic *E. coli* |
| *E. coli* AstC | 40.3 % | catabolic *E. coli* |

The characterized catabolic clade is internally 60–80 % identical (PP_4481–PA0895 = 79.9 %; *E. coli* ArgD–AstC = 60 %), whereas PP_0372 sits well outside it (~40–42 %) and instead pairs tightly with PA0530 (61 %). KT2440 in fact encodes **three related class-III paralogs** with divided labor:

- **PP_0372** (K00821) — acetylornithine AT, arginine biosynthesis (this protein)
- **PP_1588** (K14267) — dedicated DapC / *N*-succinyl-DAP AT, lysine biosynthesis
- **PP_4481** (K00840) — catabolic succinylornithine AT, AST pathway

Because *P. putida* maintains a separate dedicated DapC (PP_1588), the DapC "moonlighting" activity may be less physiologically important for PP_0372 than for *E. coli* ArgD, though it remains chemically plausible. No direct enzymology exists for PP_0372 or PA0530 themselves.

### F7 — Cytoplasmic localization and an intact class-III active site

Sequence analysis of the 426-residue protein supports a soluble cytoplasmic enzyme with a functional PLP active site. The sequence contains the diagnostic class-III catalytic motif **`...IITLGKGLGGG...`** (residues ~285–295); the lysine in this G-x-K-x-G/GGG context is the conserved **PLP Schiff-base (internal aldimine) residue**, and the adjacent glycine-rich stretch forms the phosphate-binding loop. Kyte–Doolittle hydropathy analysis found **no N-terminal signal peptide and no transmembrane segment** (maximum 19-residue window hydrophobicity 1.57, occurring internally at position 304, below the ~1.6 TM threshold), and the N-terminus (MNLFNLRRSAP…) lacks a cleavable signal architecture. UniProt confirms PLP as cofactor and family assignment to class-III PLP-dependent aminotransferases. Together these indicate a cytoplasmic enzyme — the expected localization for an amino-acid-biosynthetic aminotransferase.

### F8 — The exact catalyzed reaction (KEGG R02283, EC 2.6.1.11)

The precise reaction assigned to PP_0372 via KEGG KO K00821 is **R02283**, *N*²-acetyl-L-ornithine:2-oxoglutarate aminotransferase:

```
N-Acetyl-L-ornithine + 2-Oxoglutarate  ⇌  N-Acetyl-L-glutamate 5-semialdehyde + L-Glutamate
   (C00437)          (C00026)               (C01250)                        (C00025)
                          EC 2.6.1.11 — Arginine biosynthesis (map00220)
```

The same KO also carries EC 2.6.1.17 (*N*-succinyl-DAP aminotransferase, module M00016), formalizing the dual biosynthetic assignment.

---

## Mechanistic Model / Interpretation

### Where PP_0372 sits in metabolism

PP_0372 catalyzes the fourth step of the acetylated branch of L-arginine biosynthesis, the transamination that installs the future α-amino group of ornithine while the α-amino group remains masked as an acetyl group:

```
 Glutamate
    │  N-acetylglutamate synthase (ArgA)
    ▼
 N-acetylglutamate
    │  N-acetylglutamate kinase (ArgB)
    ▼
 N-acetylglutamyl-phosphate
    │  N-acetyl-γ-glutamyl-phosphate reductase (ArgC)
    ▼
 N-acetylglutamate-5-semialdehyde
    │  ◄────  PP_0372  (acetylornithine aminotransferase, ArgD; EC 2.6.1.11; R02283)
    │         + L-glutamate  →  + 2-oxoglutarate
    ▼
 N2-acetyl-L-ornithine
    │  (deacetylation / acetyl transfer)
    ▼
 L-ornithine ──► citrulline ──► argininosuccinate ──► L-arginine
```

In parallel, the same enzyme family can act on *N*-succinyl-L,L-diaminopimelate in the lysine/*meso*-DAP pathway (DapC, EC 2.6.1.17), converting the 2-oxo intermediate to *N*-succinyl-L,L-DAP en route to *meso*-DAP and L-lysine (KEGG module M00016).

### Why the "aruC" label is misleading — a tale of two clades

The acyl-ornithine aminotransferases form two functionally distinct but sequence-related clades that a naive symbol transfer conflates:

```
        CLASS-III PLP AMINOTRANSFERASES (Aminotrans_3, IPR005814)
        │
  ┌─────┴───────────────────────────────┐
  │                                       │
 ANABOLIC clade (K00821)          CATABOLIC AST clade (K00840)
 acetylornithine AT / ArgD        succinylornithine AT / AruC(true)
 EC 2.6.1.11 (+2.6.1.17)          EC 2.6.1.81
 arginine (+lysine) BIOSYNTHESIS  arginine CATABOLISM (AST pathway)
  │                                       │
  ├─ E. coli ArgD                         ├─ E. coli AstC
  ├─ P. aeruginosa PA0530                 ├─ P. aeruginosa PA0895 (real aruC)
  └─ P. putida PP_0372  ◄── THIS PROTEIN  └─ P. putida PP_4481 (real catabolic AruC)
```

PP_0372 clearly belongs to the left (anabolic) clade: 61 % identity to PA0530, only ~40–42 % to any catabolic-clade member, K00821 orthology, biosynthesis-pathway membership, and a genomic location divorced from the *aru*/*ast* operons. The catabolic AST role in KT2440 is fully accounted for by the separate PP_4475–PP_4481 cluster with PP_4481 as its succinylornithine aminotransferase. Hence the "aruC" symbol on PP_0372 is a mis-transferred label; its EC 2.6.1.13 annotation (ornithine aminotransferase-like) likewise reflects family-level ambiguity rather than a measured activity.

### Localization and cofactor

As a class-III PLP aminotransferase with no signal peptide or transmembrane helix, PP_0372 functions in the **cytoplasm**, where amino-acid biosynthesis occurs. It uses **pyridoxal-5′-phosphate** covalently tethered via a Schiff base to the active-site lysine identified in the `IITLGKGLGGG` motif, cycling between the pyridoxal (PLP) and pyridoxamine (PMP) forms during the ping-pong transamination mechanism.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [9393691](https://pubmed.ncbi.nlm.nih.gov/9393691/) | *Cloning and characterization of the aru genes … AST pathway in P. aeruginosa* | Defines the **true catabolic AruC** as N²-succinylornithine 5-aminotransferase (F1); anchors the identity contrast in F4 |
| [23484010](https://pubmed.ncbi.nlm.nih.gov/23484010/) | *Structure of the catabolic N-succinylornithine transaminase (AstC) from E. coli* | Establishes the **acyl-ornithine AT family**, catabolic/anabolic interchangeability, and **acylated-ornithine substrate preference** (F2) |
| [3129535](https://pubmed.ncbi.nlm.nih.gov/3129535/) | *Catabolism of arginine, citrulline and ornithine by Pseudomonas* | In vivo inhibitor evidence that the AST/succinylornithine transaminase step **dissimilates the arginine carbon skeleton** (F3) |
| [1791443](https://pubmed.ncbi.nlm.nih.gov/1791443/) | *P. putida mutants affected in arginine/ornithine/citrulline catabolism* | Genetic mapping of *P. putida* arginine catabolism to the **AST and oxidase routes** (F3 context) |
| [10074354](https://pubmed.ncbi.nlm.nih.gov/10074354/) | *Dual biosynthetic capability of N-acetylornithine aminotransferase* | Direct enzymology showing the **ArgD family is bifunctional** (EC 2.6.1.11 + DapC 2.6.1.17) — the anabolic-function basis for PP_0372 (F5) |
| [26913973](https://pubmed.ncbi.nlm.nih.gov/26913973/) | *Revisited genome of P. putida KT2440* | Supports careful re-annotation of KT2440 gene functions; context for treating legacy labels critically (F4) |
| [6423769](https://pubmed.ncbi.nlm.nih.gov/6423769/) | *L-arginine utilization by Pseudomonas species* | Background on the multiplicity of arginine catabolic pathways in *P. putida* (F3 context) |

Supporting database evidence (KEGG KO K00821/K00840, EC numbers, module membership, InterPro domains IPR005814/IPR050103/IPR049704/IPR015421/IPR015424, and UniProt cofactor/family annotation) was used to place PP_0372 in the anabolic clade and to identify PP_4481 as the true catabolic enzyme.

**How the evidence fits together:** The primary literature ([9393691](https://pubmed.ncbi.nlm.nih.gov/9393691/), [23484010](https://pubmed.ncbi.nlm.nih.gov/23484010/), [10074354](https://pubmed.ncbi.nlm.nih.gov/10074354/)) is direct and experimental but was performed on *homologs* (*P. aeruginosa* AruC, *E. coli* AstC and ArgD), not on PP_0372. The bioinformatic evidence (orthology, alignments, genomic context, active-site motif, hydropathy) transfers those findings to PP_0372 with a clear, testable logic. No paper reports direct biochemistry on PP_0372 or PA0530.

---

## Limitations and Knowledge Gaps

1. **No direct enzymology on PP_0372 or PA0530.** Every functional assignment — substrate (acetylornithine), reaction (R02283), kinetics, and the possible DapC side-activity — is inferred from orthology and characterized homologs, not measured on the *P. putida* protein. Kinetic constants (k_cat, K_M) for PP_0372 are unknown.

2. **Residual EC ambiguity.** UniProt lists EC 2.6.1.11 **and** 2.6.1.13 (ornithine aminotransferase), and KEGG adds 2.6.1.17. These reflect family-level promiscuity rather than experimentally resolved specificity for PP_0372. Which reaction(s) it catalyzes physiologically in *P. putida* has not been demonstrated.

3. **DapC role uncertain in *P. putida*.** Because KT2440 encodes a dedicated DapC (PP_1588, K14267), the lysine-biosynthetic side activity that is important for *E. coli* ArgD may be dispensable for PP_0372. The division of labor among the three KT2440 paralogs (PP_0372, PP_1588, PP_4481) has not been tested genetically.

4. **Localization inferred, not observed.** Cytoplasmic localization rests on the absence of signal/TM features and family expectation; no proteomic or fluorescence-based localization data specific to PP_0372 were found.

5. **No phenotype/fitness data specific to PP_0372.** Although RB-TnSeq fitness datasets exist for *Pseudomonas* ([PMID: 38323821](https://pubmed.ncbi.nlm.nih.gov/38323821/)), no PP_0372-specific arginine-auxotrophy phenotype was retrieved to confirm the biosynthetic role in vivo.

---

## Proposed Follow-up Experiments / Actions

1. **Direct enzyme assay.** Heterologously express and purify PP_0372, reconstitute with PLP, and assay transaminase activity against *N*-acetyl-L-ornithine + 2-oxoglutarate (forward/reverse), reporting k_cat and K_M. Include *N*-succinyl-L,L-DAP, *N*-succinylornithine, and free ornithine to map substrate specificity and test the predicted acylated-ornithine preference (F2, F8).

2. **Genetic complementation / auxotrophy test.** Delete PP_0372 in KT2440 and test for arginine auxotrophy on minimal medium; complement an *E. coli argD* mutant with PP_0372 to confirm the biosynthetic role. Cross with ΔPP_1588 (DapC) to probe whether PP_0372 contributes to lysine biosynthesis.

3. **Confirm the catabolic assignment of PP_4481.** Delete the PP_4475–PP_4481 cluster and test loss of growth on arginine as sole carbon/nitrogen source; assay PP_4481 for succinylornithine aminotransferase activity to formally separate the catabolic function from PP_0372.

4. **Structural validation.** Solve or model (AlphaFold + docking) the PP_0372 structure and verify the class-III fold, the Schiff-base lysine in the `IITLGKGLGGG` motif, and the acyl-binding pocket geometry that governs steric/desolvation-based specificity.

5. **Curate the annotation.** Recommend updating the "aruC / acetylornithine aminotransferase 2 / EC 2.6.1.13" label for Q88QW2 to the anabolic **acetylornithine aminotransferase (ArgD; EC 2.6.1.11, +DapC 2.6.1.17)** assignment, and reserve the catabolic *aruC* / succinylornithine aminotransferase designation for PP_4481.

---

## Conclusion

PP_0372 (Q88QW2) is best described as the **cytoplasmic, PLP-dependent acetylornithine aminotransferase (ArgD) of L-arginine biosynthesis** in *P. putida* KT2440, catalysing the reversible EC 2.6.1.11 transamination (KEGG R02283) with the broad *N*-acyl-ornithine specificity of its class-III family and a plausible secondary DapC role in lysine biosynthesis. Its "aruC" symbol is an annotation artifact: the catabolic AST-pathway succinylornithine aminotransferase is a separate gene, PP_4481. All assignments rest on orthology, genomic context, and conserved active-site residues rather than on direct characterization of PP_0372 itself, which remains the principal knowledge gap.


## Artifacts

- [OpenScientist final report](aruC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](aruC-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:9393691
2. PMID:23484010
3. PMID:3129535
4. PMID:1791443
5. PMID:10074354
6. PMID:38323821