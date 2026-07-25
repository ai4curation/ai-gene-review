---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T16:52:16.946247'
end_time: '2026-07-20T18:18:12.170753'
duration_seconds: 5155.22
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_3298
  gene_symbol: PP_3298
  uniprot_accession: Q88HQ5
  protein_description: 'SubName: Full=CinA domain protein {ECO:0000313|EMBL:AAN68905.1};'
  gene_info: OrderedLocusNames=PP_3298 {ECO:0000313|EMBL:AAN68905.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: CinA-like_C. (IPR036653); CinA_C. (IPR008136); CinA (PF02464)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 2
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PP_3298-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_3298-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88HQ5
- **Protein Description:** SubName: Full=CinA domain protein {ECO:0000313|EMBL:AAN68905.1};
- **Gene Information:** OrderedLocusNames=PP_3298 {ECO:0000313|EMBL:AAN68905.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** CinA-like_C. (IPR036653); CinA_C. (IPR008136); CinA (PF02464)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_3298" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_3298' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_3298** (gene ID: PP_3298, UniProt: Q88HQ5) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of PP_3298 (Q88HQ5): A Standalone CinA C-terminal / PncC-Family NMN Deamidase in *Pseudomonas putida* KT2440

## Summary

**PP_3298** (UniProt **Q88HQ5**) of *Pseudomonas putida* KT2440 encodes a 167-amino-acid protein whose sole structural module is a **CinA C-terminal domain** (Pfam **PF02464**; InterPro **IPR008136** CinA_C / **IPR036653** CinA-like_C; COG1546). Based on convergent evidence from sequence homology, domain architecture, active-site conservation, and genomic context, PP_3298 is best annotated as a **cytoplasmic nicotinamide mononucleotide (NMN) deamidase of the PncC family (EC 3.5.1.42)**. Its predicted primary function is to hydrolytically deamidate NMN to nicotinic acid mononucleotide (NaMN) plus ammonia, a committed recycling reaction of the bacterial **pyridine nucleotide cycle (PNC)** that feeds salvaged pyridine into the Preiss–Handler pathway (NadD → NadE) to regenerate NAD⁺.

Critically, PP_3298 is **not** a full-length bifunctional CinA (competence/damage-inducible protein A). Full CinA proteins (~420 aa) carry an N-terminal COG1058/MoaC-like (molybdopterin biosynthesis / ADP-ribose pyrophosphatase-like) domain fused to the C-terminal CinA domain. PP_3298 consists of the **isolated C-terminal catalytic module only**, and its length (167 aa) matches standalone PncC enzymes such as *E. coli* PncC/YgaD (165 aa) rather than full CinA. This distinction matters because the CinA name historically implies a role in natural competence and DNA recombination; PP_3298 does not carry that connotation. Importantly, the CinA C-terminal domain is precisely the module experimentally shown to harbor the NMN deamidase activity ([PMID: 25313401](https://pubmed.ncbi.nlm.nih.gov/25313401/)).

Three lines of evidence support this annotation: (1) the protein is architecturally a **standalone CinA_C / PncC domain**, lacking the N-terminal domain of full CinA; (2) it shares **38% sequence identity** with the experimentally confirmed *E. coli* NMN deamidase PncC (P0A6G3) and strictly conserves the **AESCT active-site signature motif**; and (3) its **genomic neighborhood** in KT2440 contains no *recA*, *recX*, or other competence/recombination genes, arguing against a competence-operon (cinA-like) role and in favor of a standalone housekeeping metabolic function. The consensus annotation is therefore a **metabolic NMN deamidase acting in NAD⁺ salvage/recycling**, not a competence factor.

---

## Verified Protein Identity

| Attribute | Value |
|---|---|
| UniProt accession | Q88HQ5 |
| Locus | PP_3298 (EMBL AAN68905.1) |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125) |
| Length | 167 aa |
| Domain | CinA C-terminal (≈ residues 9–156) |
| Pfam / InterPro | PF02464 (CinA); IPR008136 (CinA_C); IPR036653 (CinA-like_C) |
| Fold / superfamily | Gene3D 3.90.950.20; SUPFAM SSF142433 (CinA-like) |
| Orthologous group | eggNOG **COG1546** (CinA/PncC family) |

The domain content (a single CinA C-terminal domain, PF02464), the orthology assignment (COG1546), and the short single-domain length (167 aa) are all consistent with the UniProt description "CinA domain protein." The organism and locus match the research target exactly. **There is no gene-symbol ambiguity — this is the correct protein**, and the analysis below builds a functional annotation from its domain, homology, and genomic evidence rather than from a same-symbol gene in a different organism.

---

## Key Findings

### Finding 1 — PP_3298 is a standalone CinA C-terminal / PncC-family protein, not a full bifunctional CinA

UniProt Q88HQ5 is a **167-amino-acid** protein consisting of a **single CinA C-terminal domain** spanning approximately residues 9–156. This module is annotated consistently across multiple databases: Pfam **PF02464** (CinA), InterPro **IPR008136** (CinA_C) and **IPR036653** (CinA-like_C), Gene3D **3.90.950.20**, SUPFAM **SSF142433**, and eggNOG **COG1546**. Importantly, the protein **lacks the N-terminal COG1058/MoaC-like domain** (a molybdopterin-biosynthesis / ADP-ribose pyrophosphatase-like module) that is fused to the C-terminal CinA domain in full-length bifunctional CinA proteins.

The length and architecture are diagnostic. Full bifunctional CinA proteins are roughly **420 amino acids** (e.g., the *Thermus thermophilus* CinA characterized structurally in [PMID: 25313401](https://pubmed.ncbi.nlm.nih.gov/25313401/)). Standalone PncC-type NMN deamidases are roughly half that length — *E. coli* PncC/YgaD is **165 aa**. PP_3298, at 167 aa, matches the standalone PncC architecture almost exactly. This establishes the protein as the **isolated catalytic C-terminal module**, which is the portion of CinA experimentally demonstrated to carry NMN deamidase activity. A practical consequence is that PP_3298 is **not expected to possess ADP-ribose pyrophosphatase activity**, because that activity resides in the N-terminal domain that PP_3298 lacks.

| Feature | PP_3298 (Q88HQ5) | *E. coli* PncC (P0A6G3) | Full CinA (*T. thermophilus*) |
|---|---|---|---|
| Length (aa) | 167 | 165 | ~420 |
| N-terminal COG1058/MoaC domain | Absent | Absent | Present |
| CinA C-terminal domain (PF02464) | Present (≈9–156) | Present | Present |
| Architecture | Standalone | Standalone | Bifunctional |
| Annotated function | NMN deamidase (predicted) | NMN deamidase (confirmed) | Bifunctional CinA / NMN deamidase |

### Finding 2 — PP_3298 is predicted to be an NMN deamidase (PncC, EC 3.5.1.42) of the pyridine nucleotide cycle

A global Needleman–Wunsch alignment of Q88HQ5 against the experimentally validated *E. coli* NMN deamidase **PncC (P0A6G3)** yields **38.1% identity (61/160 aligned positions)** over the full length of the alignment. This level of identity is comfortably within the range where enzymatic function can be transferred with confidence for a single-domain enzyme family, particularly when combined with active-site conservation.

Crucially, the **PncC-family active-site signature motif is strictly conserved**. Q88HQ5 residues 23–30, **`AESCTAGC`**, align exactly with the *E. coli* PncC motif **`AESCTGGW`**, preserving the invariant **A-E-S-C-T** catalytic core. In this enzyme family the conserved cysteine together with the surrounding acidic/serine residues form the machinery for the amidohydrolase chemistry, so their conservation is strong evidence that PP_3298 retains catalytic competence rather than being a degenerate pseudo-enzyme. This is an especially important control because the reference literature explicitly showed that **not every family homolog is active**.

The reference biochemistry underpinning this assignment is well established. Galeazzi et al. 2011 ([PMID: 21953451](https://pubmed.ncbi.nlm.nih.gov/21953451/)) identified *pncC*/*ygaD* as the long-sought *E. coli*/*Shewanella* NMN deamidase (EC 3.5.1.42), defining a **novel, broadly conserved amidohydrolase family**: *"Nicotinamide mononucleotide (NMN) deamidase (EC 3.5.1.42), one of the key enzymes of the bacterial pyridine nucleotide cycle, was originally described in Enterobacteria, but the corresponding gene eluded identification for over 30 years."* That study also cautioned that only a subset of family homologs are active — *"Of the three PncC homologs present in Escherichia coli, NMN deamidase activity was confirmed only for the recombinant purified product of the ygaD gene"* — which is precisely why the strict conservation of the AESCT motif in PP_3298 is central to a confident functional call.

Karuppiah et al. 2014 ([PMID: 25313401](https://pubmed.ncbi.nlm.nih.gov/25313401/)) resolved the structure and mechanism of the bifunctional *T. thermophilus* CinA and showed that **the C-terminal domain — the sole domain present in PP_3298 — harbors the NMN deamidase activity**: *"the C-terminal domain harbors the nicotinamide mononucleotide deamidase activity."* Sánchez-Carrón et al. 2013 ([PMID: 24340054](https://pubmed.ncbi.nlm.nih.gov/24340054/)) provided a comprehensive phylogenetic and structural classification of NMN deamidases, placing CinA-domain proteins firmly within the NMN-deamidase family and cataloguing the conserved catalytic blocks that PP_3298 satisfies; they also reported that a characterized family enzyme (OiPncC) is a strict Michaelian enzyme toward its only substrate NMN (Km ≈ 0.18 mM).

The reaction assigned to PP_3298 is therefore:

```
   Nicotinamide mononucleotide (NMN) + H2O
                    │
                    ▼   NMN deamidase (PncC, EC 3.5.1.42)
                    │
   Nicotinic acid mononucleotide (NaMN) + NH3
```

### Finding 3 — Genomic context supports a standalone metabolic role, not a competence operon

The KEGG genome neighborhood of PP_3298 in *P. putida* KT2440 places the gene (coordinates 3,731,103–3,731,606; 504 nt / 167 aa) among neighbors that are **not** associated with DNA recombination, competence, or the SOS response:

| Locus | Context | Annotation |
|---|---|---|
| PP_3296 | upstream | Putative transporter (KEGG K07112) |
| PP_3297 | upstream | Conserved protein of unknown function |
| **PP_3298** | **target** | **CinA domain protein (predicted NMN deamidase)** |
| PP_3299 | complementary strand | Outer membrane lipoprotein |
| PP_3300 | downstream | TetR-family transcriptional regulator |

None of these flanking genes is *recA*, *recX*, or another competence/DNA-recombination gene. This is a meaningful negative result. In naturally transformable bacteria, *cinA* is the **first gene of a competence-inducible (cin) operon** immediately preceding *recA*. The classic characterization in *Streptococcus pneumoniae* showed that *"recA is part of a competence-inducible (cin) operon"* and that the *cinA* gene heads this operon and is co-transcribed with *recA* under competence induction ([PMID: 7538190](https://pubmed.ncbi.nlm.nih.gov/7538190/)). Similarly, in *Deinococcus radiodurans* the *recA* locus forms a polycistronic operon with an upstream *cinA*-like cistron, with the predicted product showing *"substantial similarity to the competence-damage inducible protein (cinA gene product) from Streptococcus pneumoniae"* ([PMID: 10606814](https://pubmed.ncbi.nlm.nih.gov/10606814/)). The **absence** of any such linkage for PP_3298 indicates it is **not embedded in a cinA–recA competence operon**, and is instead a stand-alone gene consistent with a housekeeping metabolic function. KEGG annotates PP_3298 only as a "CinA domain protein" with no KO/pathway ortholog assigned, reflecting the current under-annotation of this specific ortholog and consistent with the homology-based inference presented here.

---

## Mechanistic Model / Interpretation

The synthesis of the three findings yields a coherent functional model: **PP_3298 is a cytoplasmic recycling enzyme of NAD⁺ metabolism**, specifically the NMN deamidase step of the bacterial pyridine nucleotide cycle.

NAD⁺ is continuously consumed not only as a redox cofactor but non-redoxively by enzymes such as NAD⁺-dependent DNA ligases, ADP-ribosyltransferases, and sirtuins, which cleave the glycosidic bond and release **nicotinamide** and other pyridine intermediates. The **pyridine nucleotide cycle (PNC)** salvages these degradation products back into NAD⁺ rather than paying the higher cost of de novo synthesis from aspartate. Within this cycle, NMN deamidase performs a key committed step: it **removes the amide nitrogen from NMN**, converting the amidated intermediate (NMN) into the deamidated intermediate (NaMN). NaMN then re-enters the universal **Preiss–Handler / de novo convergence point**, where NadD (NaMN adenylyltransferase) converts NaMN to NaAD, and NadE (NAD synthetase) amidates NaAD to regenerate NAD⁺.

```
        NAD+  ──(consumption / turnover)──►  Nicotinamide + ...
          ▲                                        │
          │ NadE (NAD synthetase)                  │  (salvage → NMN)
        NaAD                                        ▼
          ▲                                        NMN
          │ NadD (NaMN adenylyltransferase)         │
        NaMN  ◄────────────────────────────────────┘
                  PP_3298: NMN deamidase (EC 3.5.1.42)
                  NMN + H2O → NaMN + NH3
```

Localization is inferred to be **cytoplasmic**: PP_3298 has no signal peptide or predicted transmembrane segment, its substrate (NMN) and products (NaMN, NH₃) are soluble cytoplasmic metabolites, and its homolog PncC is a soluble cytoplasmic enzyme purified in native/recombinant soluble form. Its downstream partners (NadD, NadE) are likewise cytoplasmic. The reaction therefore occurs in the cytosol as part of central cofactor metabolism.

The mechanistic chemistry is an **amidohydrolase** reaction — hydrolysis of the carboxamide of the nicotinamide moiety to a carboxylate, releasing ammonia. The conserved AESCT motif, including the invariant cysteine, provides the catalytic machinery, consistent with the "novel broadly conserved amidohydrolase family" described by Galeazzi et al. The key interpretive caution — that some CinA_C/PncC homologs are catalytically inactive — is addressed here by the strict conservation of the full active-site signature, which supports (though does not prove) that PP_3298 is an active enzyme.

An important interpretive point concerns the **"CinA" name**. The domain family is named after the *S. pneumoniae* competence-damage-inducible protein A, creating a strong potential for mis-annotation as a competence/DNA-repair factor. Structural and biochemical work (Karuppiah et al. 2014) clarified that even in full bifunctional CinA the C-terminal domain is an NMN deamidase, and phylogenetic work (Sánchez-Carrón et al. 2013) folds CinA-domain proteins into the NMN-deamidase classification. Combined with the genomic-context evidence that PP_3298 is not in a *recA* operon, the weight of evidence points **away from a competence role and toward a metabolic NMN deamidase identity**.

---

## Evidence Base

| PMID | Title / focus | How it supports the annotation |
|---|---|---|
| [21953451](https://pubmed.ncbi.nlm.nih.gov/21953451/) | *Identification of NMN deamidase of the bacterial pyridine nucleotide cycle; a novel broadly conserved amidohydrolase family* (Galeazzi et al. 2011) | Defines EC 3.5.1.42 activity of the PncC family (to which Q88HQ5 belongs by 38% identity) and warns that only some homologs (ygaD) are active — motivating active-site checking. |
| [25313401](https://pubmed.ncbi.nlm.nih.gov/25313401/) | *Structure and mechanism of the bifunctional CinA enzyme from Thermus thermophilus* (Karuppiah et al. 2014) | Shows the CinA **C-terminal domain** — the sole domain in PP_3298 — harbors NMN deamidase activity; establishes the mechanism. |
| [24340054](https://pubmed.ncbi.nlm.nih.gov/24340054/) | *New insights into the phylogeny and molecular classification of NMN deamidases* (Sánchez-Carrón et al. 2013) | Places CinA-domain proteins in the NMN-deamidase family; catalogs conserved catalytic blocks consistent with PP_3298; reports Km ≈ 0.18 mM for a family enzyme. |
| [7538190](https://pubmed.ncbi.nlm.nih.gov/7538190/) | *The recA gene of S. pneumoniae is part of a competence-induced operon* (Martin et al. 1995) | Establishes the classic *cinA*–*recA* competence-operon architecture that PP_3298 does **not** exhibit. |
| [10606814](https://pubmed.ncbi.nlm.nih.gov/10606814/) | *Molecular analysis of the D. radiodurans recA locus* (1999) | Second example of *cinA*-like linkage to *recA*, reinforcing the diagnostic value of the missing linkage in PP_3298. |
| [31874073](https://pubmed.ncbi.nlm.nih.gov/31874073/) | Multidrug resistance analysis (no abstract available) | Peripheral; not directly informative for this annotation. |

**Direct verbatim support:**

- On family/EC assignment — *"Nicotinamide mononucleotide (NMN) deamidase (EC 3.5.1.42), one of the key enzymes of the bacterial pyridine nucleotide cycle, was originally described in Enterobacteria, but the corresponding gene eluded identification for over 30 years."* ([PMID: 21953451](https://pubmed.ncbi.nlm.nih.gov/21953451/))
- On selectivity of activity within the family — *"Of the three PncC homologs present in Escherichia coli, NMN deamidase activity was confirmed only for the recombinant purified product of the ygaD gene."* ([PMID: 21953451](https://pubmed.ncbi.nlm.nih.gov/21953451/))
- On the catalytic module — *"the C-terminal domain harbors the nicotinamide mononucleotide deamidase activity."* ([PMID: 25313401](https://pubmed.ncbi.nlm.nih.gov/25313401/))
- On the competence-operon architecture that PP_3298 lacks — the *S. pneumoniae* study establishes that *recA* is part of a competence-inducible operon with *cinA* as its first gene ([PMID: 7538190](https://pubmed.ncbi.nlm.nih.gov/7538190/)).

---

## Supported and Refuted Hypotheses

| Hypothesis | Status | Basis |
|---|---|---|
| PP_3298 is a standalone CinA C-terminal (PncC-family) protein | **Supported** | 167 aa, single PF02464 domain, COG1546, no COG1058 domain |
| PP_3298 is an NMN deamidase (EC 3.5.1.42) | **Supported (strong inference)** | 38.1% identity to confirmed *E. coli* PncC; conserved AESCT catalytic motif; family biochemistry ([PMID: 21953451](https://pubmed.ncbi.nlm.nih.gov/21953451/), [PMID: 25313401](https://pubmed.ncbi.nlm.nih.gov/25313401/)) |
| PP_3298 acts in the cytoplasm in the NAD pyridine nucleotide cycle | **Supported** | Soluble single-domain enzyme; substrate/pathway context |
| PP_3298 is a full bifunctional competence CinA with ADP-ribose pyrophosphatase activity | **Refuted** | Lacks the N-terminal COG1058 domain that carries that activity ([PMID: 25313401](https://pubmed.ncbi.nlm.nih.gov/25313401/)) |
| PP_3298 directly mediates natural transformation/competence | **Not supported** | Competence link is for the full-length CinA operon ([PMID: 7538190](https://pubmed.ncbi.nlm.nih.gov/7538190/)); genomic context shows no *recA*/competence linkage |

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of PP_3298.** The functional assignment is entirely **inferential**, based on homology (38% identity to *E. coli* PncC), active-site conservation, domain architecture, and genomic context. No enzyme kinetics, structure, or knockout phenotype has been reported for this specific *P. putida* protein.

2. **Homology is moderate, not high.** 38% identity is sufficient for confident family assignment but leaves room for shifted substrate specificity or altered kinetics. The reference literature explicitly notes that some PncC-family homologs are catalytically inactive, so the strict AESCT-motif conservation is necessary but not, by itself, definitive proof of activity.

3. **Active-site motif divergence at non-core positions.** PP_3298's motif `AESCTAGC` differs from *E. coli*'s `AESCTGGW` at the last three positions (AGC vs GGW). The invariant A-E-S-C-T core is preserved, but the functional consequence of the flanking differences (e.g., on substrate binding or turnover) is unknown.

4. **Localization is predicted, not demonstrated.** Cytoplasmic localization is inferred from the absence of targeting signals and the soluble nature of substrate/products, not from experimental fractionation or imaging.

5. **Pathway context in *P. putida* is untested.** Whether PP_3298 is the physiologically dominant NMN deamidase in *P. putida*, whether it is redundant with other salvage enzymes, and its regulation (e.g., by the nearby TetR-family regulator PP_3300) remain unknown.

6. **CinA-name ambiguity.** Databases may propagate a "competence/DNA-repair" connotation from the CinA name. The evidence here argues against that role for PP_3298, but the ambiguity should be flagged explicitly to prevent mis-annotation.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and enzyme assay.** Clone, express, and purify PP_3298 and directly measure NMN deamidase activity (NMN → NaMN + NH₃), determining kcat, Km, and pH/temperature optima — analogous to the OiPncC characterization in [PMID: 24340054](https://pubmed.ncbi.nlm.nih.gov/24340054/) (Km ≈ 0.18 mM for NMN). This would convert the prediction into a confirmed function.

2. **Substrate-specificity panel.** Test related nucleotides (NMN, NaMN, NAD⁺, NADH, nicotinamide riboside) to confirm NMN specificity and rule out promiscuous amidohydrolase activity.

3. **Active-site mutagenesis.** Mutate the conserved catalytic residues (particularly the Cys and Ser/Glu of the AESCT motif) to confirm they are required for activity, validating the mechanistic model.

4. **Genetic knockout and metabolomics.** Delete PP_3298 in *P. putida* KT2440 and measure intracellular NMN/NaMN/NAD⁺ pools; a buildup of NMN and/or a growth phenotype under NAD⁺-recycling stress would confirm the physiological role. Test for redundancy with any other candidate NMN deamidases in the genome.

5. **Structural determination or AlphaFold + docking.** Solve or model the structure and dock NMN to verify the active-site geometry and compare to the *T. thermophilus* CinA C-terminal domain ([PMID: 25313401](https://pubmed.ncbi.nlm.nih.gov/25313401/)).

6. **Regulatory analysis.** Investigate whether the adjacent TetR-family regulator (PP_3300) controls PP_3298 expression, and whether expression responds to NAD⁺ availability rather than DNA-damage/competence stimuli — a direct test of the metabolic-vs-competence hypothesis.

7. **Comparative genomics across *Pseudomonas*.** Confirm the conservation of the standalone architecture and non-*recA* genomic context across *Pseudomonas* species to strengthen the housekeeping-metabolism interpretation.

---

## Conclusion

PP_3298 (Q88HQ5) is a **167-aa standalone CinA C-terminal / PncC-family protein**, predicted with good confidence to be a **cytoplasmic NMN deamidase (EC 3.5.1.42)** that hydrolyzes NMN to NaMN + NH₃ as a committed recycling step of the bacterial pyridine nucleotide cycle, feeding NaMN into the Preiss–Handler pathway (NadD → NadE) to regenerate NAD⁺. It is the isolated catalytic module (lacking the N-terminal COG1058 domain of full bifunctional CinA) and, based on its genomic context, is a **metabolic housekeeping enzyme rather than a competence/DNA-repair factor**. The assignment rests on 38% identity to experimentally confirmed *E. coli* PncC, strict conservation of the AESCT active-site motif, and diagnostic genomic context — but awaits direct experimental validation.


## Artifacts

- [OpenScientist final report](PP_3298-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_3298-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:25313401
2. PMID:21953451
3. PMID:24340054
4. PMID:7538190
5. PMID:10606814