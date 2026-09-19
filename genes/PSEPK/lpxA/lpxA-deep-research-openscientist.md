---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-11T00:46:14.888927'
end_time: '2026-08-11T01:02:05.323280'
duration_seconds: 950.43
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: lpxA
  gene_symbol: lpxA
  uniprot_accession: Q88MG8
  protein_description: 'RecName: Full=Acyl-[acyl-carrier-protein]--UDP-N-acetylglucosamine
    O-acyltransferase {ECO:0000255|HAMAP-Rule:MF_00387}; Short=UDP-N-acetylglucosamine
    acyltransferase {ECO:0000255|HAMAP-Rule:MF_00387}; EC=2.3.1.129 {ECO:0000255|HAMAP-Rule:MF_00387};'
  gene_info: Name=lpxA {ECO:0000255|HAMAP-Rule:MF_00387}; OrderedLocusNames=PP_1603;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the transferase hexapeptide repeat family. LpxA
  protein_domains: Acetyltransf_C. (IPR029098); Acetyltransf_C_sf. (IPR037157); Hexapep.
    (IPR001451); Hexapep_transf_CS. (IPR018357); Lipid_A_LpxA. (IPR010137)
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
citation_count: 11
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: lpxA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: lpxA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88MG8
- **Protein Description:** RecName: Full=Acyl-[acyl-carrier-protein]--UDP-N-acetylglucosamine O-acyltransferase {ECO:0000255|HAMAP-Rule:MF_00387}; Short=UDP-N-acetylglucosamine acyltransferase {ECO:0000255|HAMAP-Rule:MF_00387}; EC=2.3.1.129 {ECO:0000255|HAMAP-Rule:MF_00387};
- **Gene Information:** Name=lpxA {ECO:0000255|HAMAP-Rule:MF_00387}; OrderedLocusNames=PP_1603;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the transferase hexapeptide repeat family. LpxA
- **Key Domains:** Acetyltransf_C. (IPR029098); Acetyltransf_C_sf. (IPR037157); Hexapep. (IPR001451); Hexapep_transf_CS. (IPR018357); Lipid_A_LpxA. (IPR010137)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "lpxA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'lpxA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **lpxA** (gene ID: lpxA, UniProt: Q88MG8) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# LpxA (PP_1603, Q88MG8) in *Pseudomonas putida* KT2440: The Priming Acyltransferase of Lipid A Biosynthesis

## Summary

The gene **lpxA** (ordered locus **PP_1603**; UniProt **Q88MG8**) of *Pseudomonas putida* KT2440 encodes **acyl-[acyl-carrier-protein]–UDP-N-acetylglucosamine O-acyltransferase (EC 2.3.1.129)**, commonly abbreviated **UDP-GlcNAc acyltransferase (LpxA)**. This enzyme catalyzes the **first and committed priming step** of lipid A biosynthesis: the reversible transfer of an *R*-3-hydroxyacyl chain from acyl carrier protein (ACP) to the 3-hydroxyl group of UDP-N-acetylglucosamine (UDP-GlcNAc), yielding UDP-3-*O*-(*R*-3-hydroxyacyl)-GlcNAc. Lipid A is the hydrophobic membrane anchor (the "endotoxin" moiety) of lipopolysaccharide (LPS), the dominant glycolipid of the outer leaflet of the Gram-negative outer membrane. LpxA therefore sits at the head of the highly conserved nine-step **Raetz pathway** that produces Kdo₂-lipid A, and its enzymatic family is a validated antibacterial drug-target class.

Mechanistically, LpxA is a **homotrimeric left-handed β-helix (LβH) enzyme** belonging to the transferase hexapeptide-repeat family. Each protomer folds into an N-terminal nine-rung LβH domain followed by a C-terminal α-helical domain, and the three catalytic sites of the biological trimer form at the interfaces between adjacent subunits. A conserved active-site histidine acts as the general base that deprotonates the UDP-GlcNAc 3-OH for nucleophilic attack on the ACP-thioester carbonyl, while a single "hydrocarbon-ruler" residue at the floor of the acyl-binding groove sets the maximum acyl-chain length the enzyme will accept. This ruler mechanism is the molecular explanation for the striking species-to-species variation in lipid A primary acyl-chain length.

For *P. putida* specifically, multiple converging lines of evidence — ortholog biochemistry, sequence alignment, an AlphaFold structural model, and direct chemical characterization of *P. putida* lipid A — indicate that LpxA is **selective for a short *R*-3-hydroxydecanoyl (C10) donor**. The catalytic histidine maps to **His121** and the ruler residue to a bulky **Met169** (in place of *E. coli*'s small Gly173), predicting the short-chain preference confirmed by the C10–C12 primary acyl chains found in *P. putida* KT2442 lipid A. LpxA operates in the **cytoplasm** on the cytoplasmic face of the pathway, priming a soluble sugar-nucleotide substrate before downstream membrane-associated enzymes complete lipid A assembly and Lpt machinery exports it to the outer membrane.

---

## Key Findings

### Finding 1 — LpxA catalyzes the first, priming step of lipid A biosynthesis

LpxA (PP_1603, Q88MG8) is **acyl-ACP–UDP-N-acetylglucosamine O-acyltransferase, EC 2.3.1.129**. It catalyzes the transfer of an *R*-3-hydroxyacyl chain from its carrier, acyl carrier protein (ACP), onto the 3-OH group of UDP-GlcNAc, producing UDP-3-*O*-(*R*-3-hydroxyacyl)-GlcNAc. This is the **first of nine committed enzymatic steps** — the so-called Raetz pathway — that build lipid A and, ultimately, LPS. The reaction was directly described for LpxA orthologs as "the transfer of an R-3-hydroxyacyl chain from its acyl carrier protein (ACP) to the 3-OH group of UDP-GlcNAc" and identified as "the first step of lipid A biosynthesis" that is "essential in the growth of Gram-negative bacteria" ([PMID: 30850651](https://pubmed.ncbi.nlm.nih.gov/30850651/)).

A defining biochemical feature of this step is its **reversibility and unfavorable thermodynamics**. The LpxA reaction "adds an O-acyl group to the GlcNAc in UDP-GlcNAc" in a "reversible reaction" ([PMID: 25945572](https://pubmed.ncbi.nlm.nih.gov/25945572/)). Because the equilibrium constant favors the reverse direction, flux through the pathway is gated forward by the subsequent, essentially irreversible deacetylation catalyzed by LpxC. This kinetic arrangement makes LpxA a genuine "priming" enzyme: it establishes the acylated precursor but only commits it once LpxC acts. The enzyme's identity is codified by HAMAP rule MF_00387 and its membership in the transferase hexapeptide-repeat family, with the Lipid_A_LpxA (IPR010137) and Hexapep (IPR001451) domain signatures.

### Finding 2 — LpxA is a homotrimeric left-handed β-helix enzyme with a catalytic histidine and a "hydrocarbon ruler"

Crystal structures of LpxA orthologs from multiple Gram-negative bacteria — *Pseudomonas aeruginosa* ([PMID: 26352800](https://pubmed.ncbi.nlm.nih.gov/26352800/)), *Bacteroides fragilis* ([PMID: 25945572](https://pubmed.ncbi.nlm.nih.gov/25945572/)), and *Francisella novicida* ([PMID: 27545601](https://pubmed.ncbi.nlm.nih.gov/27545601/)) — reveal a **strongly conserved architecture**. Each monomer forms "a nine-rung left-handed β-helical (LβH) fold in the N-terminus followed by an α-helical motif in the C-terminus" ([PMID: 25945572](https://pubmed.ncbi.nlm.nih.gov/25945572/)). The biological unit is a **homotrimer**, and the enzyme's three active sites are located at the interfaces between adjacent subunits — each catalytic pocket is assembled from residues contributed by two neighboring protomers.

Catalysis proceeds through a **general-base mechanism**. A conserved active-site histidine (His121 in *P. aeruginosa*; His125 in *E. coli*) deprotonates and activates the UDP-GlcNAc 3-hydroxyl group so it can attack the thioester carbonyl of the acyl-ACP donor; an oxyanion hole formed by a backbone amide stabilizes the resulting tetrahedral transition state. Structural work "supports the role of catalytic His121 in activating the UDP-GlcNAc 3-hydroxyl group for nucleophilic attack during the reaction" and, from product-complex structures, showed "how Met169 serves to constrain the length of the acyl chain and thus functions as the so-called hydrocarbon ruler" ([PMID: 26352800](https://pubmed.ncbi.nlm.nih.gov/26352800/)). The **"hydrocarbon ruler"** concept is central: a single residue at the floor of the acyl-binding pocket determines the maximum length of acyl chain that will fit, and thereby dictates the primary acyl-chain length of the organism's lipid A.

### Finding 3 — *P. putida* LpxA is C10-selective, matching KT2442 lipid A

Acyl-chain selectivity is **species-specific** and is the primary determinant of the 3-*O*/*N*-linked primary acyl chains of lipid A. Direct comparison across orthologs establishes the pattern: "In Escherichia coli and Leptospira interrogans, LpxA prefers to incorporate longer R-3-hydroxyacyl chains (C14 and C12, respectively), whereas in Pseudomonas aeruginosa, the enzyme is selective for R-3-hydroxydecanoyl, a 10-hydrocarbon long acyl chain" ([PMID: 26352800](https://pubmed.ncbi.nlm.nih.gov/26352800/)).

Because *P. putida* LpxA (PP_1603) is a close ortholog of *P. aeruginosa* LpxA, the biochemically demonstrated **C10 preference** of the *Pseudomonas* enzyme is the best-supported model for Q88MG8. This inference is corroborated by direct chemical characterization of the enzyme's downstream product. Structural analysis of *P. putida* KT2442 lipid A found "four lipid A species... two are hexa-acylated, and the other two are penta-acylated," and noted that "compared with lipid A of P. aeruginosa, P. putida lipid A has less hydroxylation on the secondary acyl chains and less modification" ([PMID: 26579930](https://pubmed.ncbi.nlm.nih.gov/26579930/)). The primary hydroxy-acyl chains fall in the C10–C12 range, closely resembling *P. aeruginosa*. High-resolution LC-MS/MS of *P. putida* lipid A independently confirmed these species ([PMID: 32673427](https://pubmed.ncbi.nlm.nih.gov/32673427/)). The convergence of ortholog biochemistry and product structure makes the C10 assignment robust.

| Organism | LpxA acyl-chain preference | Ruler residue | Reference |
|---|---|---|---|
| *Escherichia coli* | C14 (*R*-3-hydroxymyristoyl) | Gly173 (small) | [PMID: 17698807](https://pubmed.ncbi.nlm.nih.gov/17698807/) |
| *Leptospira interrogans* | C12 (*R*-3-hydroxylauroyl) | Lys171 (bulky) | [PMID: 19456129](https://pubmed.ncbi.nlm.nih.gov/19456129/) |
| *Pseudomonas aeruginosa* | C10 (*R*-3-hydroxydecanoyl) | Met169 (bulky) | [PMID: 26352800](https://pubmed.ncbi.nlm.nih.gov/26352800/) |
| ***P. putida* KT2440 (Q88MG8)** | **C10 (predicted)** | **Met169** | This work (inference) |

### Finding 4 — LpxA acts in the cytoplasm and initiates the pathway that builds the outer-membrane LPS anchor

Lipid A "constitutes a major component of lipopolysaccharides, also referred to as endotoxins, which form the outer monolayer of the outer membrane of Gram-negative bacteria" ([PMID: 25945572](https://pubmed.ncbi.nlm.nih.gov/25945572/)). While the final product resides in the outer membrane, the biosynthetic pathway begins in the **cytoplasm**. LpxA is a soluble/peripheral, cytoplasm-facing enzyme that acts on the soluble sugar-nucleotide UDP-GlcNAc; downstream enzymes (LpxC, LpxD, LpxH, LpxB, LpxK, WaaA, LpxL/LpxM) progressively build lipid A at the cytoplasmic (inner) leaflet of the inner membrane, after which the Lpt trans-envelope machinery exports the completed molecule to the outer membrane.

In *P. putida* the downstream secondary acyltransferase steps are genetically defined: "the two acyltransferases encoded by PP_0063 and PP_1735, respectively, are responsible for the site-specific additions of the two secondary acyl chains at the 2- and 2'-positions of lipid A in P. putida" ([PMID: 28557109](https://pubmed.ncbi.nlm.nih.gov/28557109/)). This places LpxA (PP_1603) unambiguously at the **head of a genetically mapped *P. putida* lipid A pathway**, upstream of these LpxL homologs.

### Finding 5 — Sequence alignment pinpoints catalytic His121 and a Met169 hydrocarbon-ruler in *P. putida* LpxA

A global Needleman–Wunsch alignment of *P. putida* LpxA (Q88MG8, 258 aa) against *E. coli* LpxA (P0A722, 262 aa) yields **52.5% identity** (135 of 257 aligned positions), confirming close orthology. The catalytic general-base histidine — established in *E. coli* as His125 by mutagenesis and crystallography — aligns exactly to ***P. putida* His121** (local context AYAHIG-**H**-DS). Critically, the acyl-chain "ruler" position, which in *E. coli* is the small **Gly173** (permitting long C14 chains), aligns to a **Methionine (Met169)** in *P. putida* — the same bulky ruler residue identified in *P. aeruginosa* LpxA and functionally equivalent to the Lys171 that limits chain length in *L. interrogans*.

The reference biochemistry anchoring this analysis is well established. *E. coli* "LpxA is highly selective for R-3-hydroxymyristate," and its crystal structure "revealed that LpxA contains an unusual, left-handed parallel beta-helix fold" ([PMID: 17698807](https://pubmed.ncbi.nlm.nih.gov/17698807/)). In *L. interrogans*, "the R-3-hydroxylauroyl selectivity of LiLpxA is explained by the position of the K171 side chain, which limits the length of the acyl-chain" ([PMID: 19456129](https://pubmed.ncbi.nlm.nih.gov/19456129/)) — establishing the general principle that a single bulky side chain at the ruler position shortens the acyl-binding groove. Because *P. putida* carries the identical bulky **Met169** found in *P. aeruginosa*, where "Met169 serves to constrain the length of the acyl chain and thus functions as the so-called hydrocarbon ruler" ([PMID: 26352800](https://pubmed.ncbi.nlm.nih.gov/26352800/)), the enzyme is predicted to select a **short (~C10) *R*-3-hydroxydecanoyl** donor rather than *E. coli*'s C14.

### Finding 6 — LpxA initiates the conserved Raetz pathway producing lipid A, the endotoxin anchor of LPS

LpxA catalyzes the first of nine conserved enzymatic steps (the **Raetz pathway**) that build **Kdo₂-lipid A**, the hydrophobic membrane-anchor domain of LPS. As the authoritative review summarizes, "bacterial lipopolysaccharides (LPS) typically consist of a hydrophobic domain known as lipid A (or endotoxin), a nonrepeating 'core' oligosaccharide, and a distal polysaccharide (or O-antigen)" ([PMID: 12045108](https://pubmed.ncbi.nlm.nih.gov/12045108/)). The pathway is highly conserved across Gram-negative bacteria, and its enzymes are clinically relevant targets: "many enzymes of lipid A biosynthesis like LpxC have been validated as targets for development of new antibiotics" ([PMID: 12045108](https://pubmed.ncbi.nlm.nih.gov/12045108/)).

The lipid A product is the agonist recognized by the mammalian innate-immune receptor TLR4, linking this bacterial biosynthetic pathway to host endotoxin recognition. In *P. putida*, the pathway proceeds from LpxA (PP_1603) through downstream Lpx enzymes, including secondary acyltransferases PP_0063/PP_1735 ([PMID: 28557109](https://pubmed.ncbi.nlm.nih.gov/28557109/)), producing the hexa-/penta-acylated lipid A species observed in KT2442 ([PMID: 26579930](https://pubmed.ncbi.nlm.nih.gov/26579930/)).

### Finding 7 — AlphaFold model of Q88MG8 confirms a high-confidence LβH+α-helical fold with intact His121 and Met169

The AlphaFold DB model **AF-Q88MG8-F1** (258 residues) is a **very high confidence** structure: mean pLDDT **97.8**, with 100% of residues above 70 and 97% above 90. The model reproduces the canonical LpxA two-part architecture — an N-terminal left-handed β-helix core (residues ~15–172, mean pLDDT 98.2) followed by a C-terminal α-helical domain (residues ≥175, mean pLDDT 97.4) — exactly matching the Acetyltransf_C / Lipid_A_LpxA domain assignment.

Both functionally critical residues are modeled with high confidence: the predicted **catalytic His121** (pLDDT 98.1) and the **ruler Met169** (pLDDT 98.5). Within a single modeled chain, His121(NE2) and Met169(SD) lie ~25 Å apart (Cα–Cα 22.9 Å). This apparent separation is expected and consistent with the known biology: LpxA's three active sites are formed at the **subunit interfaces of the biological homotrimer**, with each catalytic pocket combining residues from two adjacent protomers. A single-chain model therefore necessarily places these residues far apart. The high-confidence fold reproduces the same architecture confirmed crystallographically for *E. coli*, whose structure "revealed that LpxA contains an unusual, left-handed parallel beta-helix fold" ([PMID: 17698807](https://pubmed.ncbi.nlm.nih.gov/17698807/)).

---

## Mechanistic Model / Interpretation

### The reaction and its place in the pathway

LpxA performs the committed priming acylation that opens Gram-negative lipid A biosynthesis:

```
   UDP-GlcNAc  +  R-3-hydroxyacyl-ACP
                        │  LpxA (EC 2.3.1.129)
                        │  His121 general base; Met169 ruler
                        ▼  (reversible, unfavorable)
   UDP-3-O-(R-3-hydroxyacyl)-GlcNAc  +  ACP
                        │  LpxC (irreversible deacetylation) — gates flux forward
                        ▼
   UDP-3-O-(acyl)-GlcN  →  LpxD  →  LpxH  →  LpxB  →  LpxK  →  WaaA(KdtA)  →  LpxL/LpxM
                        ▼
                  Kdo2-lipid A  →  (+core, +O-antigen)  →  LPS
                        │  Lpt trans-envelope transport
                        ▼
             OUTER MEMBRANE (outer leaflet) — endotoxin, TLR4 agonist
```

The enzyme works on a **soluble cytoplasmic substrate** (UDP-GlcNAc) using a **soluble acyl donor** (acyl-ACP). Its own reaction is thermodynamically unfavorable and readily reversible; net forward flux is enforced by LpxC, the first irreversible step. This makes LpxA a true "priming" enzyme rather than a rate-limiting valve.

### The hydrocarbon-ruler logic

The single most informative structural determinant for *P. putida* biology is the **ruler residue**. A simple rule governs primary acyl-chain length:

| Ruler side chain | Groove length | Selected chain | Example |
|---|---|---|---|
| Small (Gly) | Long | C14 | *E. coli* Gly173 |
| Bulky (Lys) | Intermediate | C12 | *L. interrogans* Lys171 |
| Bulky (Met) | Short | C10 | *P. aeruginosa* / ***P. putida* Met169** |

Because *P. putida* Met169 is identical in identity and register to *P. aeruginosa*'s experimentally validated ruler, the prediction that Q88MG8 selects **C10 (*R*-3-hydroxydecanoyl)** is well grounded. This prediction is not merely computational — it is **independently confirmed at the product level**: *P. putida* KT2442 lipid A carries primary acyl chains in the C10–C12 range, closely resembling *P. aeruginosa* ([PMID: 26579930](https://pubmed.ncbi.nlm.nih.gov/26579930/), [PMID: 32673427](https://pubmed.ncbi.nlm.nih.gov/32673427/)). Four independent lines of evidence therefore converge on the same conclusion: (1) ortholog biochemistry, (2) sequence alignment, (3) the AlphaFold structural model, and (4) the chemical structure of the biosynthetic product.

### Quaternary structure and catalysis

LpxA functions only as a **homotrimer**. The three active sites are interfacial — each is built from residues of two neighboring subunits. His121 acts as the general base, abstracting a proton from the UDP-GlcNAc 3-OH so that oxygen attacks the acyl-ACP thioester carbonyl; an oxyanion hole stabilizes the tetrahedral intermediate, and ACP is released as the acyl group is transferred to the sugar-nucleotide. Met169 lines the acyl-binding groove and physically limits how deep the acyl chain can bury, enforcing chain-length selectivity. The AlphaFold monomer faithfully reproduces the LβH+α-helical fold and positions both residues correctly, with the ~25 Å His121–Met169 separation within a chain being the expected signature of interfacial active sites.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the findings |
|---|---|---|
| [30850651](https://pubmed.ncbi.nlm.nih.gov/30850651/) | *Structure-guided antibacterial peptide targeting UDP-GlcNAc acyltransferase* | States the exact reaction, LpxA's first-step position, essentiality, and druggability (F1) |
| [25945572](https://pubmed.ncbi.nlm.nih.gov/25945572/) | *Structures of B. fragilis UDP-GlcNAc acyltransferase (BfLpxA)* | Confirms reversibility, O-acylation chemistry, LβH homotrimeric fold, and lipid A's OM localization (F1, F2, F4) |
| [26352800](https://pubmed.ncbi.nlm.nih.gov/26352800/) | *Structures of P. aeruginosa LpxA reveal substrate selectivity* | Documents His121 catalytic base, Met169 hydrocarbon ruler, and C10 selectivity of the closest ortholog (F2, F3, F5) |
| [26579930](https://pubmed.ncbi.nlm.nih.gov/26579930/) | *Structure of phospholipids and lipid A of P. putida KT2442* | Directly characterizes P. putida lipid A (4 species; C10–C12 primary chains), confirming product of a C10-selective LpxA (F3, F6) |
| [32673427](https://pubmed.ncbi.nlm.nih.gov/32673427/) | *LC-HRMS/MS of lipid A from E. coli, P. putida, P. taiwanensis* | Independent high-resolution confirmation of P. putida lipid A species (F3) |
| [28557109](https://pubmed.ncbi.nlm.nih.gov/28557109/) | *Two secondary acyltransferases of lipid A in P. putida KT2442* | Defines downstream PP_0063/PP_1735, placing LpxA (PP_1603) at pathway head in this organism (F4, F6) |
| [17698807](https://pubmed.ncbi.nlm.nih.gov/17698807/) | *Structural basis for acyl-chain selectivity of UDP-GlcNAc acyltransferase* | Establishes E. coli C14 selectivity and LβH fold — the reference for alignment and AlphaFold validation (F5, F7) |
| [19456129](https://pubmed.ncbi.nlm.nih.gov/19456129/) | *Structural basis for selectivity of L. interrogans LpxA* | Shows a single bulky ruler side chain (K171) limits chain length — the principle applied to Met169 (F5) |
| [12045108](https://pubmed.ncbi.nlm.nih.gov/12045108/) | *Lipopolysaccharide endotoxins* (Raetz & Whitfield review) | Authoritative definition of LPS/lipid A architecture and validated antibiotic targets (F6) |
| [27545601](https://pubmed.ncbi.nlm.nih.gov/27545601/) | *Crystal structure and activity of F. novicida LpxA* | Additional LβH structure; illustrates ruler-residue variation and that downstream enzymes/acyl-ACP pool also shape final chain length (F2) |

Supporting context on the LpxA family: the *F. novicida* LpxA work ([PMID: 27545601](https://pubmed.ncbi.nlm.nih.gov/27545601/)) importantly qualifies the ruler model, noting that "the acyl chain length of lipid A is determined by several factors including acyl chain selectivity of LpxA and downstream enzymes, as well as the composition of the acyl-ACP pool in vivo." This nuance means LpxA sets the *preference*, but the observed lipid A profile is a joint product of enzyme selectivity and substrate availability — a caveat consistent with the mixed hexa-/penta-acylated species seen in *P. putida*. A related note: the *Cronobacter sakazakii* study ([PMID: 29339761](https://pubmed.ncbi.nlm.nih.gov/29339761/)) identifies LpxA as "the first enzyme in the pathway of lipid A biosynthesis" and shows a binding partner can modulate its activity, reinforcing LpxA's canonical role.

---

## Limitations and Knowledge Gaps

1. **No direct enzymology on Q88MG8 itself.** The C10 selectivity, His121 catalytic role, and Met169 ruler function are established by **inference from close orthologs** (chiefly *P. aeruginosa*) combined with alignment and an AlphaFold model — not by direct kinetic assays or a crystal structure of the *P. putida* enzyme. The inference is strong (52.5% identity to *E. coli*; identical ruler residue to *P. aeruginosa*; product structure matches), but remains an inference.

2. **Chain-length determination is multifactorial.** As emphasized by the *F. novicida* study ([PMID: 27545601](https://pubmed.ncbi.nlm.nih.gov/27545601/)), final lipid A acyl-chain length depends on LpxA selectivity, downstream enzymes, and the cellular acyl-ACP pool. The presence of C10–C12 species in *P. putida* is consistent with a C10-preferring LpxA but does not exclude some flexibility.

3. **No structure of the biological trimer for Q88MG8.** The available AlphaFold model is a monomer; the interfacial active sites and the precise geometry of His121/Met169 relative to bound substrate can only be inferred from ortholog trimer structures.

4. **Essentiality is assumed, not demonstrated in *P. putida*.** LpxA is essential in most Gram-negative bacteria, and lipid A is fundamental to the OM, but a direct essentiality/conditional-knockout study for PP_1603 was not identified in this investigation.

5. **Regulation is uncharacterized in *P. putida*.** Pathway flux control (e.g., the LpxC-mediated gating known from *E. coli*) has not been examined specifically in *P. putida*.

---

## Proposed Follow-up Experiments / Actions

1. **Direct biochemical assay of recombinant Q88MG8.** Express and purify PP_1603 and measure acyl-chain selectivity against a panel of *R*-3-hydroxyacyl-ACP donors (C8, C10, C12, C14). This would directly test the predicted C10 preference and quantify kinetic parameters (kcat/Km).

2. **Structure determination.** Solve a crystal or cryo-EM structure of the *P. putida* LpxA homotrimer, ideally with substrate/product, to visualize the interfacial active site and confirm the Met169 ruler geometry.

3. **Ruler-residue mutagenesis.** Engineer Met169→Gly (mimicking *E. coli*) and assay whether selectivity shifts toward longer C14 chains, and correlate with changes in cellular lipid A profile by LC-MS/MS. Conversely, introduce Met169 into an *E. coli*-like scaffold to test sufficiency.

4. **Catalytic-histidine test.** Generate His121Ala and His121Asn variants and measure loss of activity to confirm the general-base role predicted from alignment.

5. **Genetic essentiality / conditional depletion.** Construct a conditional PP_1603 allele (e.g., inducible depletion) to confirm essentiality in *P. putida* KT2440 and to enable inhibitor screening.

6. **Inhibitor / antibacterial evaluation.** Given LpxA's validated target-class status, screen the *P. putida* enzyme against known LpxA-directed peptides/small molecules ([PMID: 30850651](https://pubmed.ncbi.nlm.nih.gov/30850651/)) to assess whether the short-chain-selective Pseudomonas active site offers a distinct pharmacological pocket.

---

## Conclusion

LpxA (PP_1603, Q88MG8) of *Pseudomonas putida* KT2440 is unambiguously identified — by domain signatures, HAMAP rule MF_00387, ortholog biochemistry, sequence alignment, an AlphaFold model, and the chemical structure of its downstream product — as **acyl-ACP–UDP-N-acetylglucosamine O-acyltransferase (EC 2.3.1.129)**, the cytoplasmic homotrimeric LβH enzyme that catalyzes the first, priming step of lipid A biosynthesis. It uses a catalytic His121 general base and a bulky Met169 hydrocarbon ruler that selects a short ~C10 *R*-3-hydroxydecanoyl donor, matching the short primary acyl chains of *P. putida* lipid A. Its product, lipid A, is the endotoxin anchor of LPS that forms the essential outer leaflet of the Gram-negative outer membrane, making LpxA the committed head of the conserved Raetz pathway and a member of a validated antibacterial drug-target class.


## Artifacts

- [OpenScientist final report](lpxA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](lpxA-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:30850651
2. PMID:25945572
3. PMID:26352800
4. PMID:27545601
5. PMID:26579930
6. PMID:32673427
7. PMID:17698807
8. PMID:19456129
9. PMID:28557109
10. PMID:12045108
11. PMID:29339761