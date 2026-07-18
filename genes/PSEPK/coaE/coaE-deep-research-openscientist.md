---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T13:07:59.405273'
end_time: '2026-07-18T13:35:31.222792'
duration_seconds: 1651.82
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: coaE
  gene_symbol: coaE
  uniprot_accession: Q88Q65
  protein_description: 'RecName: Full=Dephospho-CoA kinase {ECO:0000255|HAMAP-Rule:MF_00376};
    EC=2.7.1.24 {ECO:0000255|HAMAP-Rule:MF_00376}; AltName: Full=Dephosphocoenzyme
    A kinase {ECO:0000255|HAMAP-Rule:MF_00376};'
  gene_info: Name=coaE {ECO:0000255|HAMAP-Rule:MF_00376}; OrderedLocusNames=PP_0631;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the CoaE family. {ECO:0000255|HAMAP-
  protein_domains: Depp_CoAkinase. (IPR001977); P-loop_NTPase. (IPR027417); CoaE (PF01121)
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
  path: coaE-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: coaE-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88Q65
- **Protein Description:** RecName: Full=Dephospho-CoA kinase {ECO:0000255|HAMAP-Rule:MF_00376}; EC=2.7.1.24 {ECO:0000255|HAMAP-Rule:MF_00376}; AltName: Full=Dephosphocoenzyme A kinase {ECO:0000255|HAMAP-Rule:MF_00376};
- **Gene Information:** Name=coaE {ECO:0000255|HAMAP-Rule:MF_00376}; OrderedLocusNames=PP_0631;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the CoaE family. {ECO:0000255|HAMAP-
- **Key Domains:** Depp_CoAkinase. (IPR001977); P-loop_NTPase. (IPR027417); CoaE (PF01121)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "coaE" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'coaE' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **coaE** (gene ID: coaE, UniProt: Q88Q65) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *coaE* (Dephospho-CoA Kinase, PP_0631, UniProt Q88Q65) in *Pseudomonas putida* KT2440

**Gene:** *coaE* (OrderedLocusName **PP_0631**) · **Protein:** Dephospho-CoA kinase (DPCK/DCK), EC 2.7.1.24 · **UniProt:** Q88Q65 (COAE_PSEPK) · **Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440) · **Family/domains:** CoaE family; P-loop NTPase (IPR027417); Dephospho-CoA kinase (IPR001977); Pfam PF01121; HAMAP-Rule MF_00376

---

## Summary

**CoaE (PP_0631; UniProt Q88Q65) of *Pseudomonas putida* KT2440 is dephospho-CoA kinase (EC 2.7.1.24), the enzyme that catalyzes the fifth and final step of the universal coenzyme A (CoA) biosynthetic pathway.** It uses ATP to phosphorylate the 3′-hydroxyl group of the ribose moiety of 3′-dephospho-CoA, producing CoA and ADP. The reaction completes the conversion of the vitamin precursor pantothenate (vitamin B5) into the mature, universally essential acyl-carrier cofactor CoA. No direct experimental study of the *P. putida* protein exists; the assignment is a **high-confidence functional transfer** built from a convergent body of evidence — curated protein-family annotation (CoaE family, HAMAP-Rule MF_00376), the diagnostic Walker-A/P-loop motif present in the target's own sequence, 46.7% amino-acid identity to the biochemically proven *E. coli* enzyme, residue-level conservation of experimentally validated catalytic residues, and consistent KEGG pathway and genomic-context placement.

Mechanistically, CoaE is a small (~22 kDa, 207-residue) soluble, monomeric member of the **P-loop NTPase (nucleotide-kinase) superfamily**. Crystal structures of bacterial orthologs reveal a conserved three-domain architecture — a canonical nucleotide (ATP)-binding core with a five-stranded parallel β-sheet and Walker-A/P-loop motif, a substrate (CoA)-binding α-helical domain, and a lid domain — and show that ATP binding drives large domain motions that close the active site over the dephospho-CoA substrate during phosphoryl transfer. The enzyme is highly specific for dephospho-CoA over related adenosine-containing molecules, functions in the cytoplasm, and is essential in every bacterium in which it has been tested, consistent with the strict indispensability of CoA supply for central metabolism.

Biologically, CoaE operates in the cytosol as the terminal enzyme of the pantothenate-to-CoA pathway (KEGG module M00120), feeding the essential cofactor CoA into fatty-acid and phospholipid metabolism, central carbon metabolism (via acetyl-CoA and other acyl-CoAs), and phosphopantetheine transfer to acyl/peptidyl carrier proteins. In *P. putida* KT2440 the gene is monocistronic and sits next to a conserved *yacG* neighbor (PP_0630), mirroring the *E. coli* gene neighborhood, but is not co-transcribed with the other, dispersed CoA-pathway genes. This report synthesizes seven confirmed findings and 17 reviewed papers into a complete functional narrative. **No ambiguity was found in the gene identity: the *coaE* / dephospho-CoA kinase literature applies directly to this protein by orthology.**

---

## Key Findings

### CoaE catalyzes the final step of CoA biosynthesis (F001)

The primary function of PP_0631/*coaE* is that of **dephospho-CoA kinase (EC 2.7.1.24)**. UniProt entry Q88Q65 annotates the protein as Dephospho-CoA kinase and assigns it to the CoaE family under HAMAP-Rule MF_00376. The enzyme catalyzes the ATP-dependent phosphorylation of the 3′-hydroxyl of the ribose in 3′-dephospho-CoA, yielding CoA + ADP — the **fifth and final step** of the conserved five-enzyme CoA biosynthetic pathway that begins with the phosphorylation of pantothenate.

The reaction chemistry has been directly established for orthologs. In *E. coli*, the *yacE/coaE* gene product was identified as dephospho-CoA kinase by NMR analysis of the reaction product ([PMID: 11292795](https://pubmed.ncbi.nlm.nih.gov/11292795/)): *"Dephosphocoenzyme A (dephospho-CoA) kinase catalyzes the final step in coenzyme A biosynthesis, the phosphorylation of the 3'-hydroxy group of the ribose sugar moiety."* The placement of dephospho-CoA kinase as the terminal enzyme of a universal five-step pathway is confirmed in the authoritative review by Leonardi & Jackowski ([PMID: 26443589](https://pubmed.ncbi.nlm.nih.gov/26443589/)): *"CoA is assembled in five enzymatic steps, starting from the phosphorylation of pantothenate to phosphopantothenate."*

The five steps of the pathway are:

| Step | Enzyme | Gene | EC | Reaction |
|------|--------|------|-----|----------|
| 1 | Pantothenate kinase | *coaA*/PanK | 2.7.1.33 | Pantothenate → 4′-phosphopantothenate |
| 2 | Phosphopantothenoylcysteine synthetase | *coaB* | 6.3.2.5 | + L-Cys → 4′-phosphopantothenoylcysteine |
| 3 | Phosphopantothenoylcysteine decarboxylase | *coaC* | 4.1.1.36 | → 4′-phosphopantetheine |
| 4 | Phosphopantetheine adenylyltransferase | *coaD* | 2.7.7.3 | + ATP → 3′-dephospho-CoA |
| **5** | **Dephospho-CoA kinase** | ***coaE* (PP_0631)** | **2.7.1.24** | **Dephospho-CoA + ATP → CoA + ADP** |

CoaE thus performs the committed final maturation of the cofactor, installing the 3′-phosphate that distinguishes mature CoA from its dephospho precursor.

### CoaE is a P-loop NTPase with a three-domain fold and large catalytic domain motions (F002)

Crystal structures of bacterial CoaE orthologs establish the fold and mechanism that Q88Q65 inherits by homology. The *Haemophilus influenzae* structure ([PMID: 11886213](https://pubmed.ncbi.nlm.nih.gov/11886213/)) describes the three-domain organization: *"The protein molecule consists of three domains: the canonical nucleotide-binding domain with a five-stranded parallel beta-sheet, the substrate-binding alpha-helical domain, and the lid domain formed by a pair of alpha-helices. The overall topology of the protein resembles the structures of nucleotide kinases."* The *E. coli* structure ([PMID: 12538896](https://pubmed.ncbi.nlm.nih.gov/12538896/)) confirms superfamily membership: *"Dephospho-CoA kinase is structurally similar to many nucleoside kinases and other P-loop-containing nucleotide triphosphate hydrolases, despite having negligible sequence similarity to these enzymes."*

The CoA-binding site sits at the interface of all three domains, and catalysis requires substantial conformational change. The *Thermus thermophilus* structure ([PMID: 15526298](https://pubmed.ncbi.nlm.nih.gov/15526298/)), solved in both liganded and unliganded states, revealed that ATP binding induces large domain movements, with proline residues (notably Pro91) conferring flexibility at the domain linkages so the CoA-binding domain can close over the substrate.

Functional residues have been pinpointed by site-directed mutagenesis in the *M. tuberculosis* enzyme ([PMID: 21264299](https://pubmed.ncbi.nlm.nih.gov/21264299/)), which *"identified Lys14 and Arg140 in ATP binding and the stabilization of the phosphoryl intermediate during the phosphotransfer reaction. Mutagenesis of Asp32 and Arg140 showed catalytic efficiencies less than 5-10% of the wild type."* These structural and mutational data map directly onto the InterPro/Pfam domains assigned to Q88Q65: IPR027417 (P-loop_NTPase), IPR001977 (Depp_CoAkinase), and PF01121 (CoaE).

### The target's own sequence carries the CoaE-family Walker-A/P-loop motif (F004)

Direct inspection of the 207-residue Q88Q65 sequence (entry name COAE_PSEPK) confirms the family assignment at the sequence level. The protein contains a canonical **Walker-A/P-loop motif, GGIGSGKS, at residues 15–22**, matching the consensus [AG]xxxxGK[S/T]. This motif is the ATP-binding signature of the P-loop NTPase superfamily and the diagnostic fingerprint of the dephospho-CoA kinase (CoaE) family. The predicted size of ~22 kDa matches biochemically characterized monomeric orthologs (the *E. coli* enzyme is 22.6 kDa). This grounds the annotation in the actual amino-acid sequence of the target rather than in database inheritance alone.

### 46.7% identity to the biochemically confirmed *E. coli* CoaE (F005)

A Needleman–Wunsch global alignment of *P. putida* Q88Q65 (207 aa) against *E. coli* CoaE/YacE (UniProt P0A6I9, 206 aa) yields **99/212 = 46.7% identity over the full length**. The *E. coli* protein is the reference case in which dephospho-CoA kinase activity was experimentally proven by product NMR ([PMID: 11292795](https://pubmed.ncbi.nlm.nih.gov/11292795/)): *"Amplification of the gene and overexpression yielded recombinant dephospho-CoA kinase as a 22.6-kDa monomer. Enzyme assay and nuclear magnetic resonance analyses of the product demonstrated that the recombinant enzyme is indeed dephospho-CoA kinase."*

The Walker-A/P-loop regions are essentially identical between the two proteins (*P. putida* `TGGIGSGKS` vs *E. coli* `TGGIGSGKS`). Identity of 46.7% over the entire protein is well above the ~25–30% "twilight-zone" threshold below which fold and function become uncertain; at this level across the full length, conservation of both three-dimensional fold and enzymatic function is highly reliable. This is the single strongest quantitative pillar supporting the functional transfer to the *P. putida* protein.

### Validated catalytic residues are conserved in the target (F006)

Beyond global identity, the residues known to be functionally critical are conserved. The alignment to *E. coli* CoaE maps the invariant Walker-A/P-loop lysine (*E. coli* Lys15, within GKST) onto ***P. putida* Lys21** (within the GGIGSGKS motif at residues 15–22). This lysine is equivalent to *M. tuberculosis* CoaE Lys14, shown by mutagenesis to be essential for ATP binding and stabilization of the phosphoryl-transfer intermediate ([PMID: 21264299](https://pubmed.ncbi.nlm.nih.gov/21264299/)). Conserved acidic residues immediately C-terminal to the P-loop (*P. putida* Asp37 and Asp39) are strong candidates for the Mg²⁺-coordinating/catalytic aspartate role, occupying the equivalent context to *M. tuberculosis* Asp32. Numerous additional charged residues are shared (e.g., Lys21, Asp37/39, Arg43, Glu101, Asp177), consistent with a fully conserved ATP- and dephospho-CoA-binding active site. This upgrades the confidence from "same family" to "same active-site machinery."

### High substrate specificity, cytoplasmic localization, and essentiality (F003)

**Substrate specificity.** Recombinant *E. coli* dephospho-CoA kinase displayed a strong preference for dephospho-CoA: activity with adenosine, AMP, and adenosine phosphosulfate was only 4–8% of the activity with dephospho-CoA ([PMID: 11292795](https://pubmed.ncbi.nlm.nih.gov/11292795/)): *"The activities with adenosine, AMP, and adenosine phosphosulfate were 4 to 8% of the activity with dephospho-CoA."* The enzyme selectively recognizes the full dephospho-CoA acceptor rather than merely its adenosine/adenine-phosphate portion.

**Essentiality.** CoA biosynthesis is essential across bacteria, and *coaE* specifically is indispensable. It was identified as a novel essential gene in *Streptococcus mutans* by antisense knockdown ([PMID: 15908386](https://pubmed.ncbi.nlm.nih.gov/15908386/)): *"a novel essential gene, the coaE gene, encoding dephospho-coenzyme A kinase, which is involved in the final step of coenzyme A."* It is likewise essential for the survival of *M. tuberculosis* ([PMID: 22954585](https://pubmed.ncbi.nlm.nih.gov/22954585/)): *"we found that CoaE was also essential for the survival of M. tuberculosis."*

**Localization.** The enzyme is a soluble cytoplasmic protein — no signal peptide, no transmembrane domain, and the UniProt subcellular location is cytoplasm. Its substrate (dephospho-CoA) and product (CoA) are cytosolic metabolites, placing its function firmly in the bacterial cytoplasm.

### KEGG pathway placement and conserved genomic context (F007)

KEGG assigns PP_0631/*coaE* to orthology **K00859** (dephospho-CoA kinase, EC 2.7.1.24), pathways ppu00770 (Pantothenate and CoA biosynthesis) and ppu01240 (Biosynthesis of cofactors), and module **ppu_M00120** (Coenzyme A biosynthesis, pantothenate ⇒ CoA). The gene lies at `complement(737926..738549)`. Its immediate neighbors are functionally unrelated to CoA metabolism: PP_0630 = **YacG** (a DNA gyrase inhibitor), PP_0632 = a prepilin leader peptidase/N-methyltransferase, and PP_0633 = PilC. The gene is effectively **monocistronic** and not co-transcribed with the other CoA-pathway genes, which are dispersed across the genome (typical for bacterial CoA biosynthesis). Notably, the *coaE*(*yacE*)-adjacent-to-*yacG* arrangement mirrors the conserved *E. coli* gene neighborhood, indicating evolutionarily preserved local synteny. In the genome-wide mini-Tn5 conditional-essentiality screen of KT2440 ([PMID: 20158506](https://pubmed.ncbi.nlm.nih.gov/20158506/)) — *"a genome-wide collection of single-gene P. putida KT2440 knockouts was generated by mini-Tn5 transposon mutagenesis and used to identify genes essential for growth in minimal medium"* — no viable *coaE* disruption was recovered, consistent with *coaE* being strictly (not merely conditionally) essential.

---

## Mechanistic Model / Interpretation

The findings converge on a single coherent model of CoaE function.

### The reaction and its place in metabolism

```
Pantothenate (vitamin B5)
      │  CoaA / PanK  (2.7.1.33)
      ▼
4'-Phosphopantothenate
      │  CoaB  (6.3.2.5)  + L-Cys
      ▼
4'-Phosphopantothenoyl-cysteine
      │  CoaC  (4.1.1.36)  - CO2
      ▼
4'-Phosphopantetheine
      │  CoaD  (2.7.7.3)  + ATP
      ▼
3'-Dephospho-CoA
      │  ►►► CoaE / PP_0631  (2.7.1.24)   + ATP → + ADP   ◄◄◄  FINAL STEP
      ▼
Coenzyme A (CoA)
      │
      ├──► Acetyl-CoA / acyl-CoAs → central carbon metabolism (TCA, β-oxidation)
      ├──► Malonyl-CoA → fatty-acid & phospholipid biosynthesis
      └──► 4'-Phosphopantetheine transfer → acyl/peptidyl carrier proteins (ACP, PCP)
```

CoaE catalyzes the terminal, committed maturation step: it transfers the γ-phosphate of ATP onto the 3′-hydroxyl of the ribose of dephospho-CoA. The product, CoA, is the universal thioester-forming acyl carrier at the heart of bacterial metabolism. Because every downstream acyl-CoA and every phosphopantetheinylated carrier protein depends on this final phosphorylation, loss of CoaE activity collapses CoA supply — explaining the observed essentiality across taxa.

### The catalytic machine

```
        ┌───────────────────────────────────────────────┐
        │              Dephospho-CoA kinase              │
        │    (P-loop NTPase / nucleotide-kinase fold)    │
        │                                                │
        │  [1] Nucleotide-binding core                   │
        │      5-stranded parallel β-sheet               │
        │      Walker-A / P-loop: GGIGSGKS  (res 15–22)  │
        │      catalytic Lys21 ── binds ATP β/γ-PO4      │
        │                                                │
        │  [2] CoA-binding α-helical domain ─┐            │
        │      (moves on ATP binding)        ├─ active    │
        │  [3] Lid domain (α-helix pair) ────┘   site     │
        │                                                │
        │  ATP binding → large domain closure            │
        │  (proline hinges) → in-line phosphoryl transfer│
        └───────────────────────────────────────────────┘
```

The enzyme is a small monomer with classic nucleotide-kinase topology. The Walker-A/P-loop motif — present verbatim in the Q88Q65 sequence at residues 15–22 (GGIGSGKS) — cradles the ATP phosphates, with the invariant lysine (Lys21 in *P. putida*, equivalent to the mutationally validated Lys14 of *M. tuberculosis*) stabilizing the transition state. ATP binding triggers proline-hinged domain closure that brings the CoA-binding domain and lid over the dephospho-CoA acceptor, aligning the 3′-OH for in-line phosphoryl transfer. High acceptor specificity (dephospho-CoA ≫ adenosine/AMP/APS) reflects extensive recognition of the pantetheine and pyrophosphate portions of the substrate at the multi-domain interface. Kinetic studies of the mycobacterial ortholog indicate an **ordered mechanism** with dephospho-CoA as the leading substrate and ATP binding second ([PMID: 19876400](https://pubmed.ncbi.nlm.nih.gov/19876400/)).

### Regulatory note (from orthologs, not confirmed in *P. putida*)

Studies of the mycobacterial enzyme reveal a regulatory layer in which CTP acts as an intrinsic inhibitor binding at a site overlapping the dephospho-CoA site, and in which a monomer/trimer equilibrium modulates active-enzyme concentration ([PMID: 21731728](https://pubmed.ncbi.nlm.nih.gov/21731728/), [PMID: 19876400](https://pubmed.ncbi.nlm.nih.gov/19876400/)). Whether *P. putida* CoaE shares these features is unknown; these are ortholog-derived hypotheses, not established properties of Q88Q65.

### Confidence assessment

| Evidence pillar | Finding | Strength |
|-----------------|---------|----------|
| Curated family annotation (HAMAP MF_00376, CoaE family, EC 2.7.1.24) | F001 | High |
| Diagnostic Walker-A/P-loop motif present in target sequence | F004 | High |
| 46.7% identity to biochemically proven *E. coli* CoaE | F005 | Very high |
| Residue-level conservation of validated catalytic Lys/Asp | F006 | High |
| KEGG pathway + module M00120 + conserved *yacG* synteny | F007 | High |
| Structural/mechanistic homology to solved ortholog structures | F002 | High |
| Substrate specificity, essentiality, cytoplasmic localization (orthologs) | F003 | Moderate–High (transferred) |

No single line of evidence comes from a direct experimental study of the *P. putida* KT2440 protein, but the **convergence of six independent evidence types** — sequence, structure, family, catalytic residues, pathway/context, and orthologous biochemistry — makes the annotation of Q88Q65 as dephospho-CoA kinase a high-confidence conclusion.

---

## Evidence Base

| PMID | Title (abbreviated) | Contribution |
|------|--------------------|--------------|
| [11292795](https://pubmed.ncbi.nlm.nih.gov/11292795/) | *Identification of yacE (coaE) as the structural gene for dephospho-CoA kinase in E. coli K-12* | **Foundational.** Proves (product NMR) CoaE is dephospho-CoA kinase; establishes reaction, 22.6-kDa monomer, and high substrate specificity. The 46.7%-identity reference ortholog. Supports F001, F003, F005. |
| [26443589](https://pubmed.ncbi.nlm.nih.gov/26443589/) | *Biosynthesis of Pantothenic Acid and Coenzyme A* (Leonardi & Jackowski review) | Authoritative review placing dephospho-CoA kinase as the terminal enzyme of the five-step pathway. Supports F001. |
| [11886213](https://pubmed.ncbi.nlm.nih.gov/11886213/) | *Crystal structure of dephospho-CoA kinase from H. influenzae* | Defines the conserved three-domain P-loop kinase architecture. Supports F002. |
| [12538896](https://pubmed.ncbi.nlm.nih.gov/12538896/) | *Crystal structure of a trimeric form of dephospho-CoA kinase from E. coli* | Confirms P-loop NTPase / nucleoside-kinase superfamily membership matching InterPro/Pfam of Q88Q65. Supports F002. |
| [15526298](https://pubmed.ncbi.nlm.nih.gov/15526298/) | *ATP-induced structural change of dephospho-CoA kinase from T. thermophilus* | Shows ATP-driven domain movements (Pro91 hinge) essential for catalysis. Supports F002. |
| [21264299](https://pubmed.ncbi.nlm.nih.gov/21264299/) | *Identification of critical residues of the mycobacterial dephospho-CoA kinase by mutagenesis* | Identifies Lys14, Arg140, Asp32 as catalytic/ATP-binding; maps to conserved *P. putida* residues. Supports F002, F006. |
| [15908386](https://pubmed.ncbi.nlm.nih.gov/15908386/) | *Inducible antisense RNA expression in S. mutans* | Establishes *coaE* as a novel essential gene. Supports F003. |
| [22954585](https://pubmed.ncbi.nlm.nih.gov/22954585/) | *Evaluation of CoA biosynthesis proteins of M. tuberculosis as drug targets* | Confirms CoaE essentiality for survival. Supports F003. |
| [20158506](https://pubmed.ncbi.nlm.nih.gov/20158506/) | *Conditionally essential genes for growth of P. putida KT2440* | KT2440 mini-Tn5 library; *coaE* not recovered as a viable knockout, consistent with strict essentiality. Supports F007. |
| [21731728](https://pubmed.ncbi.nlm.nih.gov/21731728/) | *Regulatory characteristics of mycobacterial dephospho-CoA kinase* | Ortholog CTP inhibition and monomer/trimer regulation (context; not confirmed in *P. putida*). |
| [19876400](https://pubmed.ncbi.nlm.nih.gov/19876400/) | *Role of UPF0157 in folding of M. tuberculosis CoaE and CTP regulation* | Ordered substrate addition (DCoA then ATP); CTP inhibition (context). |
| [25022520](https://pubmed.ncbi.nlm.nih.gov/25022520/) | *Characterization of dephospho-CoA kinase from Streptomyces peucetius* | Additional biochemical confirmation of CoaE phosphorylating activity; CoaE overexpression boosts CoA-dependent product (doxorubicin). |

**How the evidence coheres:** The *E. coli* study (PMID 11292795) anchors the reaction chemistry and specificity; the crystallographic studies (PMIDs 11886213, 12538896, 15526298) define the fold and dynamics; the mutagenesis study (PMID 21264299) pins down catalytic residues; and sequence analysis of Q88Q65 itself (F004–F006) demonstrates that these features are conserved in the *P. putida* protein at 46.7% identity, with an intact P-loop and catalytic lysine. Essentiality data (PMIDs 15908386, 22954585, 20158506) and KEGG/context data (F007) situate the enzyme's biological importance and cellular pathway.

---

## Limitations and Knowledge Gaps

1. **No direct experimental study of the *P. putida* KT2440 protein.** The entire annotation rests on homology-based transfer. Although 46.7% identity to a proven enzyme, conserved catalytic residues, and consistent pathway context make this robust, the Q88Q65 protein has not itself been purified, assayed kinetically, or crystallized.
2. **Kinetic parameters unknown for *P. putida* CoaE.** Km and kcat for dephospho-CoA and ATP are not measured for this ortholog. Orthologous values vary (e.g., mycobacterial CoaE is reported ~21× more catalytically proficient than some prokaryotic counterparts), so quantitative behavior cannot be assumed.
3. **Regulation is inferred only from distant orthologs.** CTP inhibition and monomer/trimer oligomeric regulation are documented for *M. tuberculosis* CoaE (PMIDs 21731728, 19876400) but have not been tested for the *P. putida* enzyme.
4. **Localization is predicted, not demonstrated.** Cytoplasmic localization is inferred from the absence of signal/transmembrane sequences and from general knowledge of CoA biosynthesis; no experimental fractionation or imaging exists for PP_0631.
5. **Essentiality in *P. putida* is inferred, not directly proven.** The absence of a recoverable *coaE* knockout in the KT2440 transposon library (PMID 20158506) is consistent with strict essentiality but is indirect; a targeted conditional-knockout study would be definitive.
6. **Oligomeric state in solution is unconfirmed for the target.** Orthologs range from monomer (*E. coli*, *H. influenzae*) to trimer (crystallographic and mycobacterial regulatory forms); the physiologically relevant state for *P. putida* CoaE is not established.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and enzyme assay.** Clone PP_0631, express the His-tagged protein, and confirm dephospho-CoA kinase activity via a coupled spectrophotometric assay (ADP production coupled to pyruvate kinase/lactate dehydrogenase, monitoring NADH oxidation) — the strategy used for the *Streptomyces* ortholog (PMID 25022520). Report Km/kcat for dephospho-CoA and ATP.
2. **Substrate-specificity panel.** Test activity against adenosine, AMP, and adenosine phosphosulfate versus dephospho-CoA to verify the strong acceptor preference seen in *E. coli* (PMID 11292795).
3. **Active-site mutagenesis.** Generate K21A (P-loop lysine) and D37A/D39A variants and measure loss of catalytic efficiency, testing the residue-level predictions from F006 and the mycobacterial mutagenesis study (PMID 21264299).
4. **Structural determination.** Solve the crystal or cryo-EM structure of *P. putida* CoaE, ideally with ATP/ADP and dephospho-CoA/CoA bound, to confirm the three-domain fold and closed catalytic conformation predicted from orthologs (PMIDs 11886213, 15526298). An AlphaFold model plus experimental validation is a fast first step.
5. **Conditional essentiality test.** Construct an inducible/depletion strain (e.g., CRISPRi or a regulated promoter) to directly demonstrate that *coaE* is essential in *P. putida* KT2440, complementing the indirect transposon-library inference (PMID 20158506).
6. **Regulatory probing.** Test whether CTP inhibits *P. putida* CoaE and whether the enzyme exhibits oligomer-dependent activity, to determine if the mycobacterial regulatory logic (PMIDs 21731728, 19876400) generalizes to *Pseudomonas*.
7. **Localization confirmation.** Use subcellular fractionation or a fluorescent fusion to confirm cytoplasmic localization.

---

## Conclusion

CoaE (PP_0631, UniProt Q88Q65) of *Pseudomonas putida* KT2440 is dephospho-CoA kinase (EC 2.7.1.24), the cytoplasmic, ATP-dependent enzyme that catalyzes the fifth and final step of coenzyme A biosynthesis — phosphorylating the 3′-hydroxyl of the ribose of dephospho-CoA to yield CoA + ADP — with high specificity for dephospho-CoA. It is a small (~22 kDa) monomeric member of the P-loop NTPase / nucleotide-kinase superfamily with a three-domain fold and a Walker-A/P-loop ATP-binding motif (GGIGSGKS, catalytic Lys21). This high-confidence functional assignment, absent a direct *P. putida* experimental study, is supported by curated family annotation, the diagnostic sequence motif in the target itself, 46.7% identity to the biochemically confirmed *E. coli* enzyme, residue-level conservation of validated catalytic residues, structural homology to solved ortholog structures, and consistent KEGG pathway and genomic-context placement (module M00120). The enzyme acts in the cytosol to supply the essential universal cofactor CoA to central carbon, fatty-acid/phospholipid, and phosphopantetheine-transfer metabolism.


## Artifacts

- [OpenScientist final report](coaE-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](coaE-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:11292795
2. PMID:26443589
3. PMID:11886213
4. PMID:12538896
5. PMID:15526298
6. PMID:21264299
7. PMID:15908386
8. PMID:22954585
9. PMID:20158506
10. PMID:19876400
11. PMID:21731728