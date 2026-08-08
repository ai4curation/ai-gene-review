---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T08:53:14.450439'
end_time: '2026-07-23T08:57:54.539006'
duration_seconds: 280.09
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: murA
  gene_symbol: murA
  uniprot_accession: Q88P88
  protein_description: 'RecName: Full=UDP-N-acetylglucosamine 1-carboxyvinyltransferase
    {ECO:0000255|HAMAP-Rule:MF_00111}; EC=2.5.1.7 {ECO:0000255|HAMAP-Rule:MF_00111};
    AltName: Full=Enoylpyruvate transferase {ECO:0000255|HAMAP-Rule:MF_00111}; AltName:
    Full=UDP-N-acetylglucosamine enolpyruvyl transferase {ECO:0000255|HAMAP-Rule:MF_00111};
    Short=EPT {ECO:0000255|HAMAP-Rule:MF_00111};'
  gene_info: Name=murA {ECO:0000255|HAMAP-Rule:MF_00111}; OrderedLocusNames=PP_0964;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the EPSP synthase family. MurA subfamily.
  protein_domains: Enolpyruvate_Tfrase_dom. (IPR001986); Enolpyruvate_Tfrase_sf. (IPR036968);
    RNA3'P_cycl/enolpyr_Trfase_a/b. (IPR013792); UDP_GlcNAc_COvinyl_MurA. (IPR005750);
    EPSP_synthase (PF00275)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 9
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: murA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: murA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88P88
- **Protein Description:** RecName: Full=UDP-N-acetylglucosamine 1-carboxyvinyltransferase {ECO:0000255|HAMAP-Rule:MF_00111}; EC=2.5.1.7 {ECO:0000255|HAMAP-Rule:MF_00111}; AltName: Full=Enoylpyruvate transferase {ECO:0000255|HAMAP-Rule:MF_00111}; AltName: Full=UDP-N-acetylglucosamine enolpyruvyl transferase {ECO:0000255|HAMAP-Rule:MF_00111}; Short=EPT {ECO:0000255|HAMAP-Rule:MF_00111};
- **Gene Information:** Name=murA {ECO:0000255|HAMAP-Rule:MF_00111}; OrderedLocusNames=PP_0964;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the EPSP synthase family. MurA subfamily.
- **Key Domains:** Enolpyruvate_Tfrase_dom. (IPR001986); Enolpyruvate_Tfrase_sf. (IPR036968); RNA3'P_cycl/enolpyr_Trfase_a/b. (IPR013792); UDP_GlcNAc_COvinyl_MurA. (IPR005750); EPSP_synthase (PF00275)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "murA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'murA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **murA** (gene ID: murA, UniProt: Q88P88) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: MurA (Q88P88 / PP_0964) in *Pseudomonas putida* KT2440

## Gene/Protein Identity Verification

- **UniProt accession:** Q88P88
- **Gene:** *murA* (ordered locus **PP_0964**)
- **Organism:** *Pseudomonas putida* strain ATCC 47054 / DSM 6125 / KT2440 (PSEPK), a non-pathogenic soil/rhizosphere Gram-negative bacterium widely used as an industrial-biotechnology metabolic chassis (PMID: 26913973).
- **Protein:** UDP-N-acetylglucosamine 1-carboxyvinyltransferase; EC **2.5.1.7**; synonyms **enoylpyruvate transferase / UDP-N-acetylglucosamine enolpyruvyl transferase (EPT)**.
- **Family / domains:** EPSP synthase family, **MurA subfamily** (HAMAP-Rule MF_00111); Pfam **PF00275 (EPSP_synthase)**; InterPro IPR005750 (UDP_GlcNAc_COvinyl_MurA), IPR001986/IPR036968 (Enolpyruvate transferase domain/superfamily), IPR013792.

**Verification outcome:** The gene symbol *murA*, the EC 2.5.1.7 assignment, the EPSP-synthase/MurA-subfamily classification, and the conserved enolpyruvyl-transferase domains are all mutually consistent and match a single, deeply conserved enzyme found across virtually all bacteria. This is **not** an ambiguous symbol: MurA is unambiguously the UDP-GlcNAc enolpyruvyl transferase of peptidoglycan biosynthesis. Because the enzyme is essential and universally conserved (HAMAP rule), the extensive mechanistic literature from *E. coli*, *Enterobacter cloacae*, and other bacteria applies directly to the *P. putida* KT2440 ortholog. Note: strain-specific biochemical papers on the KT2440 MurA are not available, so functional claims below are grounded in (i) the UniProt/HAMAP annotation of Q88P88 and (ii) primary mechanistic/structural studies of orthologous MurA enzymes.

---

## 1. Summary (Answer to the Research Question)

MurA (Q88P88, PP_0964) is a soluble **cytoplasmic enzyme** that catalyzes the **first committed step of peptidoglycan (murein) biosynthesis**: the transfer of the intact **enolpyruvyl group from phosphoenolpyruvate (PEP) to the 3′-hydroxyl of UDP-N-acetylglucosamine (UDP-GlcNAc)**, yielding **enolpyruvyl-UDP-GlcNAc and inorganic phosphate** (EC 2.5.1.7) (PMID: 40127436; 38532715). It is one of only two enzymes in nature (with EPSP synthase, AroA) known to perform enolpyruvyl transfer from PEP (PMID: 40127436). The reaction proceeds by an **addition–elimination mechanism through a tetrahedral ketal intermediate**, mediated by an active-site cysteine and a large substrate-induced open→closed conformational change (PMID: 9485407; 10694381; 9654090). MurA is **essential for bacterial viability**, is **feedback-inhibited** by the downstream product UDP-N-acetylmuramate, and is the molecular **target of the antibiotic fosfomycin** (PMID: 12562791; 38532715; 40127436).

---

## 2. Primary Function: Reaction Catalyzed and Substrate Specificity

**Reaction (EC 2.5.1.7):**

> phosphoenolpyruvate + UDP-N-acetyl-α-D-glucosamine → phosphate + UDP-N-acetyl-3-O-(1-carboxyvinyl)-α-D-glucosamine (enolpyruvyl-UDP-GlcNAc)

MurA transfers the **entire enolpyruvyl moiety (C3 unit) of PEP** — not merely a phosphate — onto the **3′-OH of the GlcNAc sugar** of UDP-GlcNAc, releasing inorganic phosphate (PMID: 38532715; 9485407). This is chemically unusual: PEP is normally used as a phosphoryl donor, but MurA (and EPSP synthase) instead cleave the C–O bond to transfer the enolpyruvyl group. "MurA and its related enolpyruvyl transferase, 5-enolpyruvyl-shikimate-3-phosphate (EPSP) synthase (AroA), are the only known enzymes to catalyze the unusual enolpyruvyl transfer from PEP" (PMID: 40127436).

**Substrate specificity:** The two substrates are highly specific — **PEP** (the enolpyruvyl donor) and **UDP-GlcNAc** (the acceptor sugar nucleotide). The product enolpyruvyl-UDP-GlcNAc is the dedicated substrate of the next enzyme, MurB, which reduces it to UDP-N-acetylmuramate (UDP-MurNAc), the founding building block of the peptidoglycan stem peptide.

**Catalytic mechanism (evidence from structure and stereochemistry):**
- The reaction is an **addition–elimination** proceeding through a **tetrahedral ketal intermediate**: the UDP-GlcNAc 3′-OH adds across the PEP double bond, then phosphate is eliminated (PMID: 9485407).
- Crystallography of the *E. coli* **C115A mutant** trapped with a fluorinated tetrahedral-intermediate analogue defined the absolute configuration (2R) and showed addition occurs **to the 2-si face of PEP**, establishing the stereochemical course (PMID: 9485407).
- An **active-site cysteine (Cys115** in *E. coli*/*Enterobacter* numbering) interacts directly with PEP and is central to catalysis and to protonation chemistry (PMID: 10694381).

**Induced-fit conformational cycle:**
- MurA is a two-domain protein that undergoes a large **open→closed transition upon substrate binding**. Small-angle X-ray scattering and fluorescence showed that "binding of UDP-GlcNAc to free enzyme results in substantial conformational changes, which can be interpreted as the transition from an open to a closed form" (PMID: 9654090).
- A mobile **loop (residues 112–121) bearing the catalytic Cys** closes over the active site; kinetic and X-ray studies of the Cys115Ser mutant established the role of this loop in the induced-fit mechanism (PMID: 10694381).

---

## 3. Subcellular Localization

MurA is a **soluble, cytoplasmic enzyme**. Peptidoglycan biosynthesis begins in the cytoplasm with a series of soluble Mur enzymes (MurA–MurF) that build the UDP-MurNAc-pentapeptide precursor before it is handed to membrane-associated steps (MraY, MurG) and finally polymerized in the periplasm. MurA specifically catalyzes the **cytoplasmic** enolpyruvyl-transfer step (PMID: 38532715 describes it as "the peptidoglycan pathway cytoplasmic step"; PMID: 35819545 calls MurA "an essential cytosolic enzyme in the biosynthesis of peptidoglycan"). Consistent with this, MurA carries no signal peptide or transmembrane segment and acts on soluble nucleotide-sugar substrates.

---

## 4. Pathway Context and Biological Process

**Pathway:** UDP-N-acetylmuramate (peptidoglycan precursor) biosynthesis; more broadly, **bacterial cell-wall / murein biogenesis**.

- MurA performs **step 1** of the committed pathway, consuming **UDP-GlcNAc** (itself made from fructose-6-P via GlmS/GlmM/GlmU).
- Its product, **enolpyruvyl-UDP-GlcNAc**, is reduced by **MurB** (an FAD-dependent reductase) to **UDP-MurNAc**.
- MurC–MurF then sequentially add the pentapeptide (L-Ala, D-Glu, meso-DAP [in Gram-negatives such as *P. putida*], D-Ala-D-Ala) to form UDP-MurNAc-pentapeptide (Park's nucleotide).
- Downstream, MraY and MurG assemble lipid I/lipid II, which is flipped across the membrane and polymerized by penicillin-binding proteins into the peptidoglycan sacculus.

Thus MurA gates the flux of UDP-GlcNAc into cell-wall synthesis, sitting at the branch point between amino-sugar metabolism and peptidoglycan production. In *P. putida* KT2440, a Gram-negative bacterium with a thin peptidoglycan layer between inner and outer membranes, this pathway is required for cell-envelope integrity, cell division, and osmotic protection.

---

## 5. Regulation

**Feedback inhibition by the pathway product:** UDP-N-acetylmuramate (UDP-MurNAc / UNAM) — produced two steps downstream by MurB — "binds tightly to MurA forming a dormant UNAM-PEP-MurA complex and acting as a MurA feedback inhibitor" (PMID: 38532715). Molecular-dynamics analysis indicates UNAM stabilizes the **closed conformation** via hydrogen bonds to conserved arginines (Arg120, Arg91) and has a longer residence time than the forward substrate UDP-GlcNAc, providing product-level control that prevents over-commitment of UDP-GlcNAc to peptidoglycan (PMID: 38532715). This couples the flux through MurA to the demand for cell-wall precursors.

---

## 6. Essentiality, Drug-Target Status, and Fosfomycin

- **Essentiality:** A lethal ΔmurA deletion in *E. coli* is viable only when complemented by a functional *murA* gene, demonstrating that MurA is essential for bacterial growth (PMID: 12562791).
- **Fosfomycin target:** Fosfomycin (a PEP-mimetic epoxide phosphonate) is "an irreversible covalent inhibitor of UDP-GlcNAc enolpyruvyl transferase (MurA)" that "binds to the active site of MurA in competition with substrate phosphoenolpyruvate (PEP) and undergoes the ring-opening nucleophilic attack of an active-site cysteine" (PMID: 40127436). This covalent adduct on the catalytic Cys inactivates the enzyme, blocking cell-wall synthesis.
- **Resistance determinant:** Mutation of the active-site cysteine (e.g., **Cys→Asp**) confers intrinsic fosfomycin resistance; *Chlamydia* MurA naturally carries this substitution and is fosfomycin-resistant, imparting resistance when expressed in *E. coli* (PMID: 12562791).
- **Drug-discovery relevance:** MurA has no mammalian homolog and is a "validated target enzyme for antibacterial drug discovery," motivating ongoing development of covalent (e.g., chloroacetamide-warhead) and natural-product inhibitors (PMID: 36126388; 35819545). This is contextual to the enzyme family and not specific to *P. putida* susceptibility.

---

## 7. Evidence Basis and Confidence

| Claim | Type of evidence | Strength |
|---|---|---|
| Reaction/substrates/products (EC 2.5.1.7) | Biochemical + structural (orthologs) + UniProt/HAMAP annotation of Q88P88 | High |
| Cytoplasmic localization | Pathway biochemistry; absence of signal/TM segments; family annotation | High |
| Addition–elimination via tetrahedral ketal; stereochemistry | X-ray of trapped intermediate analogue (E. coli C115A) (PMID 9485407) | High (ortholog) |
| Active-site Cys, induced-fit loop closure | Kinetics, X-ray, SAXS (Enterobacter/E. coli) (PMID 10694381, 9654090) | High (ortholog) |
| Product feedback inhibition (UDP-MurNAc) | MD + prior biochemistry (PMID 38532715) | Moderate–High |
| Essentiality | Genetic complementation (PMID 12562791) | High (ortholog); MurA universally essential |
| Fosfomycin inhibition/resistance | Structural/pharmacological (PMID 40127436, 12562791) | High (family-level) |

**Inference for Q88P88 specifically:** Because MurA is governed by HAMAP rule MF_00111 and the *P. putida* KT2440 sequence is a bona fide MurA-subfamily member with the conserved catalytic Cys and Arg residues, the mechanistic, localization, and regulatory conclusions transfer with high confidence to PP_0964. Direct enzymology on the KT2440 protein itself has not been reported.

---

## 8. Supported and Refuted Hypotheses

**Supported:**
- H1: Q88P88 is a UDP-GlcNAc enolpyruvyl transferase catalyzing PEP + UDP-GlcNAc → enolpyruvyl-UDP-GlcNAc + Pi. ✔
- H2: The enzyme is cytoplasmic and functions in the first committed step of peptidoglycan biosynthesis. ✔
- H3: Catalysis uses an active-site cysteine and an induced-fit tetrahedral-intermediate mechanism. ✔
- H4: MurA is essential and is the fosfomycin target; the catalytic Cys governs drug sensitivity. ✔
- H5: MurA is feedback-inhibited by the downstream product UDP-MurNAc. ✔ (computational/biochemical)

**Refuted / excluded:**
- The gene symbol is **not** ambiguous; there is no competing well-supported alternative function for this locus. MurA is not a transporter, structural protein, or signaling molecule — it is a biosynthetic transferase.

---

## 9. Limitations and Future Directions

- No *P. putida* KT2440-specific enzymological, structural, or knockout study of MurA was found; conclusions rest on orthologs and family-level annotation.
- The precise residue numbering (catalytic Cys, regulatory Arg) in Q88P88 should be confirmed by sequence alignment to the *E. coli*/*Enterobacter* references before residue-level claims are made for KT2440.
- Whether *P. putida* KT2440 has a second MurA paralog or additional envelope-stress regulation of *murA* expression is not established here.
- Future work: recombinant KT2440 MurA kinetics with PEP/UDP-GlcNAc; fosfomycin MIC and Cys-residue identity; structural confirmation of the closed complex.

---

### Key References
- PMID 40127436 — Kim & Lees (2025), molecular pharmacology of fosfomycin/MurA.
- PMID 9485407 — Skarzynski et al. (1998), tetrahedral-intermediate structure & stereochemistry.
- PMID 10694381 — Schönbrunn et al. (2000), Cys115 loop / induced fit.
- PMID 9654090 — Schönbrunn et al. (1998), open→closed conformational change (SAXS).
- PMID 38532715 — de Oliveira et al. (2024), UDP-MurNAc feedback inhibition (MD).
- PMID 12562791 — McCoy et al. (2003), essentiality & fosfomycin resistance determinant.
- PMID 35819545 / 36126388 — MurA as an essential cytosolic drug target.
- PMID 26913973 — Belda et al. (2016), *P. putida* KT2440 genome/chassis.


## Artifacts

- [OpenScientist final report](murA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](murA-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:26913973
2. PMID:40127436
3. PMID:9485407
4. PMID:12562791
5. PMID:38532715
6. PMID:10694381
7. PMID:9654090
8. PMID:35819545
9. PMID:36126388