---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T05:58:43.300415'
end_time: '2026-07-17T06:29:15.184268'
duration_seconds: 1831.88
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: pdxB
  gene_symbol: pdxB
  uniprot_accession: Q88L20
  protein_description: 'RecName: Full=Erythronate-4-phosphate dehydrogenase {ECO:0000255|HAMAP-Rule:MF_01825};
    EC=1.1.1.290 {ECO:0000255|HAMAP-Rule:MF_01825};'
  gene_info: Name=pdxB {ECO:0000255|HAMAP-Rule:MF_01825}; OrderedLocusNames=PP_2117;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the D-isomer specific 2-hydroxyacid
  protein_domains: D-isomer_2_OHA_DH_cat_dom. (IPR006139); D-isomer_DH_CS. (IPR029753);
    D-isomer_DH_NAD-bd. (IPR006140); Erythronate-4-P_DHase. (IPR020921); Erythronate-4-P_DHase_dimer.
    (IPR024531)
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: pdxB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pdxB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88L20
- **Protein Description:** RecName: Full=Erythronate-4-phosphate dehydrogenase {ECO:0000255|HAMAP-Rule:MF_01825}; EC=1.1.1.290 {ECO:0000255|HAMAP-Rule:MF_01825};
- **Gene Information:** Name=pdxB {ECO:0000255|HAMAP-Rule:MF_01825}; OrderedLocusNames=PP_2117;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the D-isomer specific 2-hydroxyacid
- **Key Domains:** D-isomer_2_OHA_DH_cat_dom. (IPR006139); D-isomer_DH_CS. (IPR029753); D-isomer_DH_NAD-bd. (IPR006140); Erythronate-4-P_DHase. (IPR020921); Erythronate-4-P_DHase_dimer. (IPR024531)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pdxB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pdxB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pdxB** (gene ID: pdxB, UniProt: Q88L20) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: pdxB (Q88L20 / PP_2117)
### Erythronate-4-phosphate dehydrogenase — *Pseudomonas putida* KT2440 (PSEPK)

## 1. Summary (Answer to the Research Question)

**pdxB** encodes **erythronate-4-phosphate dehydrogenase (PdxB; EC 1.1.1.290)**, a cytoplasmic, NAD⁺-dependent oxidoreductase of the **D-isomer-specific 2-hydroxyacid dehydrogenase superfamily**. Its primary function is to catalyze the **second committed step of the de novo (DXP-dependent, PdxA/PdxJ) pyridoxal 5′-phosphate (vitamin B6) biosynthetic pathway**: the NAD⁺-dependent oxidation of the C2 hydroxyl of **4-phospho-D-erythronate** to yield **(R)-3-hydroxy-2-oxo-4-phosphonooxybutanoate** (2-oxo-3-hydroxy-4-phosphobutanoate). The enzyme acts as a soluble **homodimer in the cytosol** and is essential for vitamin B6 prototrophy; loss of pdxB produces a B6 auxotroph rescuable only by exogenous B6 vitamers via salvage.

Gene-identity verification: the UniProt description (erythronate-4-phosphate dehydrogenase, EC 1.1.1.290, gene *pdxB*, locus PP_2117), the InterPro domain set (IPR006139/IPR006140/IPR020921/IPR024531/IPR029753), and the D-2-hydroxyacid dehydrogenase family assignment all agree with the primary literature on PdxB, including the structurally characterized ortholog from the same genus (*Pseudomonas aeruginosa*). The identity is **confirmed and unambiguous**.

---

## 2. Molecular Function — the Catalyzed Reaction

**Reaction (EC 1.1.1.290):**

> 4-phospho-D-erythronate + NAD⁺ → (R)-3-hydroxy-2-oxo-4-phosphonooxybutanoate + NADH + H⁺

- **Enzyme class:** oxidoreductase acting on the CH-OH group of a donor with NAD⁺ as acceptor.
- **Cofactor:** NAD⁺ (bound in a Rossmann-type nucleotide-binding domain).
- **Substrate specificity / stereochemistry:** the enzyme is a **D-isomer-specific 2-hydroxyacid dehydrogenase**, i.e., it stereospecifically oxidizes the 2-hydroxyacid substrate (4-phospho-D-erythronate) at C2. It is homologous to and mechanistically analogous to **SerA (D-3-phosphoglycerate dehydrogenase)**, the first enzyme of phosphorylated serine biosynthesis; the two share a common ancestor and analogous NAD⁺/substrate/active-site residues [PMID 2681152].
- **Family evidence:** the crystallographically characterized *P. aeruginosa* ortholog is described as "a member of the d-isomer specific 2-hydroxyacid dehydrogenase superfamily" [PMID 17217963], and UniProt/InterPro assign the dedicated *Erythronate-4-P_DHase* signatures to Q88L20.

The reaction converts an alcohol (2-hydroxyacid) into a 2-keto acid, priming the carbon skeleton for the subsequent transamination step of the pathway.

**Residue-level catalytic annotation (UniProt Q88L20, HAMAP-Rule MF_01825; residue identities verified against the sequence in this work).** The catalytic active site comprises **Arg207, Glu236, and His253**, i.e., the **canonical His–Glu–Arg catalytic triad** of the D-isomer-specific 2-hydroxyacid dehydrogenase superfamily, with **His253 as the proton donor** (general acid/base). Mechanistically, His253 shuttles the substrate C2-hydroxyl proton during hydride transfer to NAD⁺, Glu236 orients and tunes the pKa of the histidine, and Arg207 electrostatically stabilizes the substrate carboxylate/oxyanion transition state — the same logic used by SerA and other D-2-hydroxyacid dehydrogenases. **NAD⁺** is coordinated by Asp146, Thr174, Ala205/Ser206/Arg207, Asp231 and Gly256; the **substrate** is anchored by Ser45, Thr66 and Tyr257. The formal pathway assignment is "pyridoxine 5′-phosphate from D-erythrose 4-phosphate: **step 2 of 5**" (UniPathway UPA00244). These positions are consistent with the *P. aeruginosa* structure and the 67% sequence identity established above.

**Cross-database consensus.** KEGG independently assigns PP_2117 to ortholog **K03473, "erythronate-4-phosphate dehydrogenase [EC:1.1.1.290]"**, in pathway **ppu00750 "Vitamin B6 metabolism"** (gene 2415325..2416467; 1143 bp / 380 aa), agreeing with the UniProt/HAMAP and BioCyc annotations.

---

## 3. Biological Process — the Pathway Context

PdxB operates in the **deoxyxylulose-5-phosphate (DXP)-dependent PdxA/PdxJ route of de novo pyridoxal 5′-phosphate (PLP / vitamin B6) biosynthesis**, the pathway characteristic of the γ-subdivision of proteobacteria (E. coli, *Pseudomonas*, *Photorhabdus*) [PMID 17217963]. The pathway assembles PLP from two branches that converge at PdxJ:

**Branch feeding PdxB (the "4-carbon / hydroxythreonine" arm):**
1. Erythrose-4-phosphate → 4-phospho-D-erythronate (erythrose-4-P dehydrogenase, Epd/GapB)
2. **4-phospho-D-erythronate → 2-oxo-3-hydroxy-4-phosphobutanoate  — catalyzed by PdxB (this enzyme)**
3. → 4-phospho-hydroxy-L-threonine (transaminase SerC/PdxF, using L-glutamate)
4. → 3-amino-2-oxopropyl phosphate / (2-oxo-3-hydroxy-4-phosphobutanoate handling) by PdxA
5. **PdxJ** condenses the PdxA product with **1-deoxy-D-xylulose 5-phosphate (DXP)** to form **pyridoxine 5′-phosphate (PNP)**
6. **PdxH** oxidizes PNP → **pyridoxal 5′-phosphate (PLP)**, the active cofactor.

Thus PdxB provides the second enzymatic step of the erythronate-derived arm, generating the 2-keto acid that SerC then transaminates. This positions PdxB as a **committed, upstream enzyme of essential cofactor biosynthesis** rather than a peripheral or pleiotropic factor.

**Essentiality / genetic evidence.** In *Photorhabdus luminescens*, a transposon insertion in *pdxB* produced a strain "required for de novo vitamin B6 biosynthesis"; the mutant showed growth deficiency in nutrient-poor medium that was "restored … by supplementation with pyridoxal 5′-phosphate (PLP)" and by other B6 vitamers (pyridoxal, pyridoxine, pyridoxamine) via salvage [PMID 27060119]. In *E. coli*, "PdxB (erythronate 4-phosphate dehydrogenase) is expected to be required for synthesis of the essential cofactor pyridoxal 5′-phosphate (PLP)" [PMID 31712440]. Because *P. putida* KT2440 encodes *pdxB* (PP_2117), it uses this DXP-dependent pathway rather than the single-step DXP-independent PdxS/PdxT (ribose-5-phosphate + glutamine) route found in *Bacillus* and many other taxa.

**Downstream significance.** PLP is the obligatory cofactor for a large set of transaminases, decarboxylases, racemases, and related enzymes (amino-acid and one-carbon metabolism). PdxB activity therefore underpins broad PLP-dependent metabolism, but its *precise* role is the single oxidation step above — the wider metabolic effects of pdxB loss are secondary consequences of PLP depletion, not additional catalytic activities.

---

## 4. Subcellular Localization

- **Cytoplasmic / cytosolic.** UniProt Q88L20 explicitly annotates **SUBCELLULAR LOCATION: Cytoplasm** (HAMAP-Rule MF_01825), and **SUBUNIT: Homodimer**. PdxB is a soluble enzyme: the *P. aeruginosa* ortholog is a **homodimer of 380-residue subunits**, crystallized as a soluble protein with bound NAD, with no membrane association [PMID 17217963].
- UniProt/InterPro annotate no signal peptide, lipobox, or transmembrane segment for Q88L20, consistent with a location in the bacterial cytoplasm where its substrate (a phosphorylated central-metabolism intermediate) and cofactor (NAD⁺) reside.

---

## 5. Structural Basis (Evidence from the Genus-level Ortholog)

The first PdxB structure was solved for *Pseudomonas aeruginosa* D-erythronate-4-phosphate dehydrogenase in complex with NAD [PMID 17217963]:

- **Quaternary structure:** homodimer; the **C-terminal dimerization domain has a unique fold** largely responsible for dimer formation (matching InterPro IPR024531, "Erythronate-4-P_DHase_dimer", assigned to Q88L20).
- **Domain organization per subunit:** (i) a **lid domain**, (ii) a **nucleotide (NAD)-binding domain** (Rossmann-like; InterPro IPR006140 "D-isomer_DH_NAD-bd"), and (iii) the **C-terminal dimerization domain**.
- **Catalytic domain:** InterPro IPR006139 ("D-isomer_2_OHA_DH_cat_dom") and the conserved signature IPR029753 ("D-isomer_DH_CS") mark the catalytic 2-hydroxyacid dehydrogenase machinery (conserved Arg/Glu/His catalytic residues typical of the superfamily).
- **Conformational dynamics:** the two subunits in the crystal captured different ligand combinations and open vs. more-closed active-site clefts, illustrating the hinge-bending domain closure over the phosphorylated substrate that accompanies catalysis.

Because *P. putida* and *P. aeruginosa* are congeners with highly conserved PdxB sequences, this structure is a strong homology template for the localization, oligomeric state, cofactor usage, and catalytic mechanism of PP_2117.

**Quantitative sequence support (this work).** Global Needleman–Wunsch alignment of UniProt sequences confirms strong orthology: P. putida PdxB (Q88L20, **380 aa**) is **67.3% identical** to the crystallized *P. aeruginosa* PdxB (Q9I3W9, also **380 aa**; the enzyme of PMID 17217963) and **46.5% identical** to *E. coli* PdxB (P05459, 378 aa). Both *Pseudomonas* proteins are exactly the same length. A Rossmann-type nucleotide-binding fingerprint (**GAGEVG**) is present at residues ~123–128 of Q88L20, consistent with the NAD-binding domain. These identities (well above the ~30% "twilight zone") justify confident transfer of the P. aeruginosa structure and catalytic mechanism to PP_2117.

---

## 6. Supported and Refuted Hypotheses

**Supported:**
- PdxB is erythronate-4-phosphate dehydrogenase (EC 1.1.1.290), an NAD⁺-dependent D-2-hydroxyacid dehydrogenase. ✔ (UniProt/InterPro + PMID 17217963, 2681152)
- It performs the second step of the DXP-dependent de novo PLP (vitamin B6) pathway and is essential for B6 prototrophy. ✔ (PMID 27060119, 31712440, 17217963)
- It is a soluble cytoplasmic homodimer with lid / NAD-binding / dimerization domains. ✔ (PMID 17217963; InterPro)

**Refuted / excluded:**
- PdxB is **not** a transporter, structural protein, or signaling molecule; it is a soluble metabolic oxidoreductase.
- *P. putida* does **not** rely solely on the DXP-independent PdxS/PdxT PLP route — the presence of pdxB places it in the DXP-dependent pathway.
- No evidence supports a membrane-bound or secreted localization.

---

## 7. Limitations and Future Directions

- **No PdxB study exists on P. putida KT2440 itself.** Functional/structural evidence is transferred from the same genus (*P. aeruginosa*) and from *E. coli*/*Photorhabdus* orthologs; direct in vitro kinetics (Km, kcat, substrate specificity) for PP_2117 have not been reported.
- **Kinetic promiscuity / underground metabolism.** In *E. coli*, PdxB deletion can be partially bypassed by promiscuous activities of other enzymes; whether *P. putida* has analogous bypasses is unknown (the Kim et al. 2019 study, PMID 31712440, addresses this in *E. coli*).
- Future work: recombinant expression and steady-state kinetics of PP_2117; confirmation of NAD⁺ vs. NADP⁺ preference; genetic essentiality/auxotrophy test in KT2440; an experimental (rather than homology-modeled) structure.

---

## References
- **PMID 17217963** — Ha et al. (2007). *Crystal structure of D-erythronate-4-phosphate dehydrogenase complexed with NAD.* (Structure, family, mechanism, homodimer/domains; *P. aeruginosa* ortholog.)
- **PMID 2681152** — Schoenlein, Roa, Winkler (1989). *Divergent transcription of pdxB and homology between the pdxB and serA gene products in E. coli K-12.* (Gene, SerA homology, NAD⁺/2-hydroxyacid dehydrogenase inference, pdxB-hisT operon.)
- **PMID 27060119** — Sato, Yoshiga, Hasegawa (2016). *Involvement of Vitamin B6 Biosynthesis Pathways in the Insecticidal Activity of Photorhabdus luminescens.* (pdxB required for de novo B6; auxotrophy rescued by PLP/vitamers; salvage.)
- **PMID 31712440** — Kim et al. (2019). *Hidden resources in the E. coli genome…* (PdxB required for PLP synthesis; underground/bypass metabolism.)
- **UniProt Q88L20** (HAMAP-Rule MF_01825) and **InterPro** IPR006139/IPR006140/IPR020921/IPR024531/IPR029753 (domain and family annotation for PP_2117).


## Artifacts

- [OpenScientist final report](pdxB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pdxB-deep-research-openscientist_artifacts/final_report.pdf)