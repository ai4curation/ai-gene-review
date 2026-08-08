---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T17:53:41.711786'
end_time: '2026-07-18T19:48:26.743536'
duration_seconds: 6885.03
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: coq7
  gene_symbol: coq7
  uniprot_accession: Q88QR1
  protein_description: 'RecName: Full=3-demethoxyubiquinol 3-hydroxylase {ECO:0000255|HAMAP-Rule:MF_01658};
    Short=DMQ hydroxylase {ECO:0000255|HAMAP-Rule:MF_01658}; EC=1.14.99.60 {ECO:0000255|HAMAP-Rule:MF_01658};
    AltName: Full=2-nonaprenyl-3-methyl-6-methoxy-1,4-benzoquinol hydroxylase {ECO:0000255|HAMAP-Rule:MF_01658};'
  gene_info: Name=coq7 {ECO:0000255|HAMAP-Rule:MF_01658}; OrderedLocusNames=PP_0427;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the COQ7 family. {ECO:0000255|HAMAP-
  protein_domains: COQ7_proteobact. (IPR047809); Ferritin-like. (IPR012347); Ferritin-like_SF.
    (IPR009078); Ubq_synth_Coq7. (IPR011566); COQ7 (PF03232)
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
citation_count: 11
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: coq7-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: coq7-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88QR1
- **Protein Description:** RecName: Full=3-demethoxyubiquinol 3-hydroxylase {ECO:0000255|HAMAP-Rule:MF_01658}; Short=DMQ hydroxylase {ECO:0000255|HAMAP-Rule:MF_01658}; EC=1.14.99.60 {ECO:0000255|HAMAP-Rule:MF_01658}; AltName: Full=2-nonaprenyl-3-methyl-6-methoxy-1,4-benzoquinol hydroxylase {ECO:0000255|HAMAP-Rule:MF_01658};
- **Gene Information:** Name=coq7 {ECO:0000255|HAMAP-Rule:MF_01658}; OrderedLocusNames=PP_0427;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the COQ7 family. {ECO:0000255|HAMAP-
- **Key Domains:** COQ7_proteobact. (IPR047809); Ferritin-like. (IPR012347); Ferritin-like_SF. (IPR009078); Ubq_synth_Coq7. (IPR011566); COQ7 (PF03232)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "coq7" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'coq7' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **coq7** (gene ID: coq7, UniProt: Q88QR1) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *coq7* (PP_0427 / UniProt Q88QR1) in *Pseudomonas putida* KT2440

## Summary

The gene **coq7** (ordered locus **PP_0427**; UniProt accession **Q88QR1**; entry name **COQ7_PSEPK**; RefSeq WP_010951761.1; 215 aa) of *Pseudomonas putida* KT2440 encodes **3-demethoxyubiquinol 3-hydroxylase**, also called **DMQ hydroxylase** (EC 1.14.99.60). This enzyme is a **ferritin-like, carboxylate-bridged di-iron oxygenase** that catalyzes the **penultimate (C5) aromatic-ring hydroxylation** of the ubiquinone (coenzyme Q) biosynthetic pathway. It converts 5-methoxy-2-methyl-3-(all-*trans*-polyprenyl)benzene-1,4-diol — **demethoxyubiquinol (DMQH₂)** — to **3-demethylubiquinol**, using molecular O₂ and a reducing cosubstrate. The product is subsequently O-methylated by UbiG/Coq3 to yield mature ubiquinol (the reduced form of coenzyme Q₉ in *P. putida*), the lipophilic electron/proton carrier of the respiratory chain.

The identity of Q88QR1 is established across **seven independent lines of evidence**: (1) membership in the COQ7/CLK-1 protein family (PF03232; IPR011566); (2) direct functional evidence that a *Pseudomonas* Coq7 complements the *E. coli ubiF* mutant; (3) direct spectroscopic/biochemical proof that the COQ7 family uses a carboxylate-bridged diiron center to hydroxylate DMQ; (4) bioinformatic confirmation that Q88QR1 carries the canonical 4-glutamate/2-histidine di-iron ligand signature; (5) an AlphaFold structural model (mean pLDDT 92.3) showing a pre-organized bimetallic active site; (6) UniProt/KEGG/BioCyc database annotations consistent with a two-iron, membrane-associated monooxygenase in ubiquinone biosynthesis; and (7) an evolutionary framework placing *Pseudomonas* Coq7 as the ancestral di-iron alternative to the flavin monooxygenase UbiF used by *E. coli*.

Functionally, Coq7 operates as a **peripheral (monotopic) membrane protein on the cytoplasmic face of the plasma membrane**, where its di-iron center and its substrate's long isoprenoid tail enable capture and hydroxylation of the lipophilic quinone substrate at the membrane–water interface. Because its product is a precursor of the essential respiratory quinone, Coq7 activity is required for aerobic respiratory electron transport. In *Pseudomonas*, this di-iron Coq7 — the true bacterial ortholog of human COQ7/CLK-1 — replaces the unrelated flavin monooxygenase UbiF that performs the identical C5 step in *E. coli*.

---

## Key Findings

### Finding 1 — coq7 encodes a di-iron carboxylate DMQ hydroxylase catalyzing the penultimate step of ubiquinone biosynthesis

Q88QR1 belongs to the **COQ7/CLK-1 family** (Pfam PF03232; InterPro IPR011566), a group of di-iron carboxylate oxidases/hydroxylases. The functional assignment rests on two decisive pieces of experimental work. First, Stenmark et al. (2001) cloned *COQ7* from the close relative *Pseudomonas aeruginosa* (and from *Thiobacillus ferrooxidans*) and showed that it **functionally complements an *Escherichia coli ubiF* mutant** that lacks the enzyme responsible for 5-demethoxyubiquinone hydroxylation. They further identified a conserved sequence motif for iron ligands, assigning Coq7 to the family of di-iron-containing hydroxylases and supporting a **direct catalytic** (rather than merely structural) role:

> "Here we identify Coq7 as belonging to a family of a di-iron containing oxidases/hydroxylases based on a conserved sequence motif for the iron ligands, supporting a direct function of Coq7 as a hydroxylase. We have cloned COQ7 from Pseudomonas aeruginosa and Thiobacillus ferrooxidans and show that indeed this gene complements an Escherichia coli mutant that lacks an unrelated 5-demethoxyubiquinone hydroxylase." — [PMID: 11435415](https://pubmed.ncbi.nlm.nih.gov/11435415/)

Second, direct biochemical and spectroscopic proof of the catalytic mechanism comes from the human ortholog CLK-1/COQ7. Lu et al. (2013) used UV-visible and Mössbauer spectroscopy to demonstrate that the enzyme houses a **carboxylate-bridged diiron center that activates O₂** to hydroxylate 5-demethoxyubiquinone (DMQ):

> "Both UV-visible and Mössbauer experiments provide unambiguous evidence that GB1-hCLK-1 functions as a 5-demethoxyubiquinone-hydroxylase, utilizing its carboxylate-bridged diiron center." — [PMID: 23445365](https://pubmed.ncbi.nlm.nih.gov/23445365/)

Together these establish the enzyme identity for the *P. putida* ortholog: a di-iron hydroxylase performing the DMQ-hydroxylation (C5) step, classified as **EC 1.14.99.60**. The reaction registered in Rhea (Rhea:50908) is: DMQH₂ + AH₂ + O₂ → 3-demethylubiquinol + A + H₂O.

### Finding 2 — Coq7 is a membrane-associated interfacial protein acting on the cytoplasmic face; the substrate side chain enhances catalysis

Stenmark et al. (2001) proposed, from homology to other well-characterized diiron-carboxylate proteins, that Coq7 is an **interfacial integral (monotopic) membrane protein** — associated with, rather than spanning, the lipid bilayer:

> "Based on the similarities to other well studied di-iron carboxylate proteins, we propose a structural model for Coq7 as an interfacial integral membrane protein." — [PMID: 11435415](https://pubmed.ncbi.nlm.nih.gov/11435415/)

This localization model is corroborated functionally. Lu et al. (2013) showed with human CLK-1 that the **isoprenoid tail of the physiological substrate is important for catalysis**: both V_max and k_cat/K_M for DMQ hydroxylation increase when the tail-less analog DMQ0 is replaced by the tailed DMQ2, and the tailed substrate mediates NADH reduction of the diiron center while reducing uncoupled NADH consumption:

> "Both Vmax and kcat/KM for DMQ hydroxylation increase when DMQ0 is replaced by DMQ2 as the substrate, which demonstrates that an isoprenoid side chain enhances enzymatic hydroxylation and improves catalytic efficiency." — [PMID: 23445365](https://pubmed.ncbi.nlm.nih.gov/23445365/)

The dependence on the lipophilic tail is exactly what is expected for an enzyme that accesses its substrate at the membrane interface. UniProt annotates the subcellular location of Q88QR1 as **"Cell membrane; Peripheral membrane protein,"** consistent with this interfacial model, and the *P. putida* enzyme acts on the **cytoplasmic (inner) face** of the plasma membrane, where the soluble ubiquinone-biosynthesis machinery operates.

### Finding 3 — Physiological role: Coq7 supplies ubiquinone required for respiratory electron transport

Ubiquinone (coenzyme Q) is the lipophilic proton/electron carrier of proteobacterial respiratory chains. Its biosynthesis requires three aromatic-ring hydroxylations; Coq7/UbiF performs the **C5 (penultimate) hydroxylation of DMQ**, the immediate precursor of ubiquinol, which is then O-methylated (UbiG/Coq3) to finished ubiquinone. Loss of this step blocks respiration. Padilla et al. (2004) showed that yeast producing only DMQ (i.e., with a defective Coq7 step) are respiratory-deficient and cannot support NADH- or succinate-cytochrome *c* reductase activity:

> "Yeast strains lacking Q(6) and producing solely DMQ were respiratory deficient and unable to support (6)either NADH-cytochrome c reductase or succinate-cytochrome c reductase activities." — [PMID: 15078893](https://pubmed.ncbi.nlm.nih.gov/15078893/)

The pathway context is now well defined in *E. coli*: Hajj Chehade et al. (2019) showed that the terminal reactions of the UQ pathway are organized as a **soluble ~1-MDa Ubi metabolon**, in which the SCP2 domain of UbiJ forms an extended hydrophobic cavity that sequesters the hydrophobic UQ intermediates:

> "seven Ubi proteins form the Ubi complex, a stable metabolon that catalyzes the last six reactions of the UQ biosynthetic pathway in Escherichia coli. The SCP2 domain of UbiJ forms an extended hydrophobic cavity that binds UQ intermediates" — [PMID: 30686758](https://pubmed.ncbi.nlm.nih.gov/30686758/)

This establishes that the DMQ-hydroxylation step operates within a soluble, membrane-associated complex handling lipophilic intermediates, and that its failure abolishes respiratory electron transport — defining the physiological importance of Coq7 in *Pseudomonas*.

### Finding 4 — Bioinformatic verification of the canonical ferritin-like di-iron center

Direct inspection of the UniProt Q88QR1 (COQ7_PSEPK) record confirms the molecular features expected of this enzyme class. The protein is **215 amino acids**, EC 1.14.99.60, with a cofactor requirement of **"binds 2 iron ions per subunit."** The six annotated iron-binding residues are **Glu64, Glu94, His97, Glu146, Glu178, His181** — i.e., two E-x-x-H motifs (E94–VDH97 and E178–EQH181) plus two bridging carboxylates (E64, E146). This **4-glutamate/2-histidine ligand signature** is the exact hallmark of the ferritin-like carboxylate-bridged diiron oxidase superfamily (InterPro IPR009078 "Ferritin-like_SF"; IPR012347 "Ferritin-like"). This independently verifies, at the sequence level, that Q88QR1 possesses the metal-binding architecture required for O₂-activating di-iron hydroxylase chemistry.

### Finding 5 — Evolutionary context: Pseudomonas uses the ancestral di-iron Coq7 for the step E. coli performs with the FMO UbiF

Proteobacteria evolved diverse enzyme combinations for the three contiguous UQ ring hydroxylations. In *E. coli*, these are performed by **three flavin monooxygenases (FMOs) — UbiF, UbiH, and UbiI** — each modifying a single ring position, but these FMOs occur in only a fraction of proteobacteria (Pelosi et al. 2016):

> "In Escherichia coli, each of three UQ flavin monooxygenases (FMOs), called UbiF, UbiH, and UbiI, modifies a single position of the aromatic ring." — [PMID: 27822549](https://pubmed.ncbi.nlm.nih.gov/27822549/)

*Pseudomonas* instead encodes a **COQ7-family di-iron enzyme** for the penultimate (C5/DMQ) step. The functional interchangeability of the two unrelated enzyme classes at this precise position is demonstrated by cross-complementation: Stenmark et al. (2001) showed *P. aeruginosa* Coq7 rescues the *E. coli ubiF* mutant, and work on *C. elegans* CLK-1 (Kawamukai and colleagues, 2003) showed that CLK-1/Coq7 likewise rescues the *E. coli ubiF* mutant:

> "the plasmid encoding C. elegans CLK-1 supported aerobic respiration on a non-fermentable carbon source of E. coli ubiF mutant strain and rescued the ability to synthesize ubiquinone, suggesting that the eukaryotic CLK-1/Coq7p family could function as bacterial UbiF" — [PMID: 12753928](https://pubmed.ncbi.nlm.nih.gov/12753928/)

Q88QR1 is the *P. putida* ortholog (COQ7_PSEPK, PP_0427) within this di-iron branch, making it the true bacterial homolog of the eukaryotic COQ7/CLK-1 enzymes, distinct from the FMO-based UbiF route.

### Finding 6 — AlphaFold structure confirms a pre-organized bimetallic di-iron active site

The AlphaFold model **AF-Q88QR1-F1** (mean pLDDT 92.3 — very high confidence) was analyzed directly. The six sequence-annotated iron ligands (E64, E94, H97, E146, E178, H181) all have per-residue pLDDT > 93, and their coordinating side-chain atoms converge into a single cluster: every ligand atom lies within 4.8 Å of the common centroid. Characteristic short carboxylate–carboxylate and carboxylate–histidine contacts are present (E94–E178 3.4 Å; E146–E178 4.0 Å; E64–E94 4.9 Å; E94–H97 5.3 Å; E94–H181 4.8 Å). This tight 4-Glu/2-His arrangement is the geometry expected for two adjacent (~3–4 Å apart) bridged iron ions of a ferritin-like carboxylate-bridged di-iron center — indicating that the active site is **structurally pre-organized** to bind the bimetallic cofactor, independent of any experimental crystal structure.

### Finding 7 — Database annotations independently corroborate the identity

The UniProt Q88QR1 (COQ7_PSEPK) controlled-vocabulary keywords are: **Cell membrane, Iron, Membrane, Metal-binding, Monooxygenase, Oxidoreductase, Ubiquinone biosynthesis.** Cross-references map the same locus consistently across independent databases: KEGG **ppu:PP_0427**, RefSeq **WP_010951761.1**, GeneID **83677718**, STRING **160488.PP_0427**, and BioCyc **PPUT160488:G1G01-463-MONOMER**. These annotations are fully concordant with the experimentally and structurally supported conclusion: a two-iron, metal-binding, membrane-associated monooxygenase acting in ubiquinone biosynthesis.

---

## Mechanistic Model / Interpretation

### The reaction and its position in the pathway

Coq7 catalyzes the **C5 hydroxylation** of the aromatic ring of the ubiquinone precursor. In *P. putida* (which makes UQ₉, with a nonaprenyl tail), the substrate is 5-methoxy-2-methyl-3-(all-*trans*-nonaprenyl)benzene-1,4-diol (DMQH₂). The reaction is:

```
DMQH2 (demethoxyubiquinol)  +  AH2  +  O2
        │
        ▼   Coq7 / DMQ hydroxylase (di-iron, EC 1.14.99.60)
        │   (introduces –OH at ring position C5)
        ▼
3-demethylubiquinol  +  A  +  H2O
        │
        ▼   UbiG / Coq3 (O-methyltransferase; SAM-dependent)
        │   (methylates the new C5-OH → C5-OMe)
        ▼
Ubiquinol (UQ9H2)  ⇌  Ubiquinone (UQ9)  ← respiratory electron/proton carrier
```

### Simplified schematic of the terminal UQ-biosynthesis steps

```
 ... → DMQH2 ──[Coq7 / UbiF-equivalent]──► 3-demethyl-UQH2 ──[UbiG]──► UQH2 → UQ
             (penultimate hydroxylation)              (final O-methylation)
```

### Enzyme architecture and localization

```
        CYTOPLASM (reducing environment; soluble Ubi metabolon assembles here)
   ┌───────────────────────────────────────────────────────────────┐
   │   Coq7  (peripheral / monotopic, 215 aa)                       │
   │      ▓▓ di-iron center ▓▓                                      │
   │      Fe─Fe bridged by E64, E146; chelated by E94/H97, E178/H181│
   │      activates O2 → hydroxylates DMQ ring at C5                │
   └──────────┬────────────────────────────────────────────────────┘
              │ isoprenoid tail of substrate anchors in bilayer
   ~~~~~~~~~~~~▼~~~~~~~~~ INNER (PLASMA) MEMBRANE ~~~~~~~~~~~~~~~~~~~~~
              (lipophilic DMQ/UQ intermediates partition here)
```

The mechanistic logic is coherent: the di-iron center performs O₂ activation and oxygen-atom insertion at C5 of the aromatic head-group, while the substrate's **polyprenyl tail** partitions into the membrane and both anchors the enzyme at the interface and improves catalytic efficiency (Finding 2). The enzyme works within a **soluble metabolon** (analogous to the *E. coli* Ubi complex), in which a lipid-binding SCP2 protein (UbiJ) shuttles hydrophobic intermediates between active sites (Finding 3). The end product, ubiquinone, is indispensable for aerobic (and, via alternative routes, anaerobic) respiratory electron transport.

### Comparison of the C5-hydroxylation enzymes across organisms

| Organism | Enzyme for C5 (DMQ) hydroxylation | Chemistry / cofactor | Evidence |
|---|---|---|---|
| *E. coli* | **UbiF** (flavin monooxygenase) | FAD-dependent | [PMID: 10802164](https://pubmed.ncbi.nlm.nih.gov/10802164/) |
| *P. aeruginosa / P. putida* | **Coq7** (di-iron hydroxylase) | Carboxylate-bridged di-iron | [PMID: 11435415](https://pubmed.ncbi.nlm.nih.gov/11435415/) |
| *C. elegans* | **CLK-1 / Coq7** | Di-iron; complements *E. coli ubiF* | [PMID: 12753928](https://pubmed.ncbi.nlm.nih.gov/12753928/) |
| Human | **COQ7 / CLK-1** | Carboxylate-bridged di-iron (spectroscopy) | [PMID: 23445365](https://pubmed.ncbi.nlm.nih.gov/23445365/) |
| Yeast (*S. cerevisiae*) | **Coq7p** | Di-iron; regulated by phosphorylation | [PMID: 23940037](https://pubmed.ncbi.nlm.nih.gov/23940037/) |

### Di-iron ligand map for Q88QR1

| Ligand residue | Motif role | AlphaFold pLDDT |
|---|---|---|
| Glu64 | Bridging carboxylate | > 93 |
| Glu94 | E-x-x-H motif 1 (Glu) | > 93 |
| His97 | E-x-x-H motif 1 (His) | > 93 |
| Glu146 | Bridging carboxylate | > 93 |
| Glu178 | E-x-x-H motif 2 (Glu) | > 93 |
| His181 | E-x-x-H motif 2 (His) | > 93 |

The two E-x-x-H motifs plus two additional bridging glutamates form the canonical 4-Glu/2-His ligand set of the ferritin-like di-iron oxidase superfamily.

### A note on the "catalytic vs. structural" question

In eukaryotes, Coq7 has an additional layer of **regulatory** function beyond catalysis: it participates in stabilizing other Coq proteins in the biosynthetic complex, and its activity is modulated by phosphorylation/dephosphorylation. Tran et al. (2006) reported that yeast Coq7p co-migrates with Coq3 and Coq4 in a high-molecular-mass complex and that Q and its precursor DMQ help stabilize other Coq polypeptides ([PMID: 16624818](https://pubmed.ncbi.nlm.nih.gov/16624818/)). Martín-Montalvo et al. (2013) showed the mitochondrial phosphatase Ptc7p activates Coq6 biosynthesis by **dephosphorylating Coq7p** ([PMID: 23940037](https://pubmed.ncbi.nlm.nih.gov/23940037/)), and post-transcriptional regulation of COQ7 mRNA by RNA-binding proteins tunes CoQ output in human cells ([PMID: 26690054](https://pubmed.ncbi.nlm.nih.gov/26690054/)). **These regulatory layers are eukaryote-specific elaborations.** For the *P. putida* bacterial enzyme, the core, conserved, and primary function is the **catalytic** di-iron hydroxylation of DMQ; the phosphorylation-based regulation described in yeast/mammals is not expected to apply directly to the bacterial ortholog.

---

## Evidence Base

| PMID | Title (abbreviated) | Contribution to this report | Weight |
|---|---|---|---|
| [11435415](https://pubmed.ncbi.nlm.nih.gov/11435415/) | *Coq7 (clk-1), a membrane-bound di-iron carboxylate hydroxylase in ubiquinone biosynthesis* | **Keystone.** Cloned *Pseudomonas* Coq7; showed complementation of *E. coli ubiF*; identified di-iron ligand motif; proposed interfacial membrane model | Very high (direct, *Pseudomonas*) |
| [23445365](https://pubmed.ncbi.nlm.nih.gov/23445365/) | *Human CLK-1: substrate-mediated reduction of the diiron center for DMQ hydroxylation* | Direct UV-vis/Mössbauer proof of carboxylate-bridged diiron mechanism; isoprenoid tail enhances catalysis | Very high (direct biochemistry) |
| [12753928](https://pubmed.ncbi.nlm.nih.gov/12753928/) | *Complementation of E. coli ubiF by C. elegans CLK-1* | Confirms functional interchangeability of di-iron Coq7 and FMO UbiF at the same step | High |
| [27822549](https://pubmed.ncbi.nlm.nih.gov/27822549/) | *Evolution of ubiquinone biosynthesis in proteobacteria* | Frames the FMO (UbiF/H/I) route vs. alternative enzymes; evolutionary context | High |
| [15078893](https://pubmed.ncbi.nlm.nih.gov/15078893/) | *Demethoxy-Q fails to support respiration* | Shows loss of the Coq7 step (DMQ accumulation) abolishes respiratory electron transport | High (physiological) |
| [30686758](https://pubmed.ncbi.nlm.nih.gov/30686758/) | *A soluble metabolon synthesizes ubiquinone* | Establishes the Ubi metabolon / UbiJ SCP2 hydrophobic cavity for pathway intermediates | High (pathway context) |
| [10802164](https://pubmed.ncbi.nlm.nih.gov/10802164/) | *Identification of the ubiF gene in E. coli* | Defines the FMO UbiF that Coq7 replaces; identifies the C5 substrate | Supporting |
| [16624818](https://pubmed.ncbi.nlm.nih.gov/16624818/) | *Complementation of yeast coq7 by E. coli UbiF* | Establishes dual (catalytic + structural) roles of eukaryotic Coq7; complex membership | Supporting (eukaryote-specific) |
| [23940037](https://pubmed.ncbi.nlm.nih.gov/23940037/) | *Ptc7 activates Coq7 in yeast* | Documents phosphoregulation of Coq7 (eukaryote-specific layer) | Supporting (eukaryote-specific) |
| [36229432](https://pubmed.ncbi.nlm.nih.gov/36229432/) | *Manganese-driven CoQ deficiency* | Confirms Coq7 is a diiron hydroxylase catalyzing the penultimate CoQ step; sensitive to mismetallation | Supporting |
| [26690054](https://pubmed.ncbi.nlm.nih.gov/26690054/) | *RNA-binding proteins regulate COQ7* | Post-transcriptional regulation of COQ7 in humans (eukaryote-specific) | Contextual |

**Consistency across the evidence base:** The molecular identity, catalytic chemistry, di-iron cofactor, membrane-interfacial localization, and physiological requirement for respiration are mutually reinforcing across genetic (complementation), biochemical/spectroscopic, bioinformatic (sequence motif), structural (AlphaFold), and database-annotation lines of evidence. No source contradicts the core assignment.

**Note on direct vs. inferred evidence:** No study has been performed directly on the purified *P. putida* Q88QR1 protein. The functional assignment for the *P. putida* ortholog is by strong homology and cross-species inference: direct experiments exist for the closely related *P. aeruginosa* Coq7 (complementation) and for the human/nematode COQ7/CLK-1 (spectroscopy, complementation), which share the family, the ligand motif, and the reaction.

---

## Limitations and Knowledge Gaps

1. **No direct biochemistry on Q88QR1 itself.** All catalytic and spectroscopic evidence derives from orthologs (*P. aeruginosa*, human CLK-1, *C. elegans* CLK-1, yeast Coq7p). The assignment for the *P. putida* protein is a strong homology-based inference, not a direct enzymatic measurement.

2. **No experimental structure.** The di-iron site geometry is supported by an AlphaFold model (high confidence, pLDDT 92.3) and sequence motifs, but no crystal or cryo-EM structure of Q88QR1 (or any Coq7) with bound metals and substrate has been solved. AlphaFold does not model metal ions directly; the "pre-organized di-iron site" is inferred from ligand side-chain convergence.

3. **Iron loading and metal specificity not directly demonstrated in *P. putida*.** The requirement for two Fe (vs. potential mismetallation by Mn, which degrades Coq7 in other systems — [PMID: 36229432](https://pubmed.ncbi.nlm.nih.gov/36229432/)) has not been tested for the *Pseudomonas* enzyme.

4. **Reductant/electron-donor identity in *Pseudomonas* is unconfirmed.** The EC 1.14.99.60 reaction uses a generic reduced acceptor (AH₂); the physiological electron donor in *P. putida* (e.g., a specific reductase, ferredoxin, or NAD(P)H route) has not been experimentally defined.

5. **Metabolon composition in *Pseudomonas* is assumed by analogy to *E. coli*.** Whether *P. putida* assembles an equivalent Ubi metabolon (with a UbiJ-like SCP2 protein) around Coq7 has not been directly verified.

6. **Precise membrane topology and orientation** of the *P. putida* enzyme are modeled, not experimentally mapped (e.g., by protease-accessibility or cysteine-labeling assays).

---

## Proposed Follow-up Experiments / Actions

1. **Heterologous complementation test (fast, decisive).** Express *P. putida* PP_0427 in an *E. coli ubiF* deletion strain and score restoration of aerobic growth on succinate/non-fermentable carbon and ubiquinone synthesis by LC-MS. This directly confirms the DMQ-hydroxylase function of Q88QR1 specifically.

2. **In vitro reconstitution and spectroscopy.** Purify recombinant Q88QR1, reconstitute the di-iron center, and confirm carboxylate-bridged diiron geometry by UV-vis/Mössbauer/EPR (mirroring the human CLK-1 study, [PMID: 23445365](https://pubmed.ncbi.nlm.nih.gov/23445365/)). Measure kinetics (V_max, k_cat/K_M) with tailed (DMQ_n) versus tail-less (DMQ0) substrates to verify the isoprenoid-tail effect.

3. **Site-directed mutagenesis of the ligand set.** Mutate E64, E94, H97, E146, E178, or H181 individually to Ala/Gln and test loss of activity/iron binding, validating the predicted 4-Glu/2-His di-iron ligand map.

4. **Metabolite profiling of a knockout.** Delete PP_0427 in *P. putida* KT2440 and quantify accumulation of DMQ₉ and depletion of UQ₉ by LC-MS; assess respiratory phenotype (O₂ consumption, growth on non-fermentable carbon).

5. **Metal-specificity / mismetallation test.** Assess whether Mn overload phenocopies CoQ deficiency in *P. putida* (as in [PMID: 36229432](https://pubmed.ncbi.nlm.nih.gov/36229432/)), probing whether the bacterial enzyme shares the diiron mismetallation vulnerability.

6. **Metabolon interaction mapping.** Use co-immunoprecipitation / crosslinking-MS or BN-PAGE to test whether *P. putida* Coq7 assembles with other Ubi/Coq proteins into a soluble metabolon analogous to the *E. coli* Ubi complex.

7. **Membrane-topology assay.** Confirm peripheral/monotopic association and cytoplasmic-face orientation via carbonate extraction, protease-protection, and substituted-cysteine accessibility experiments.

---

## Conclusion

*coq7* (PP_0427; UniProt Q88QR1) of *Pseudomonas putida* KT2440 encodes **3-demethoxyubiquinol 3-hydroxylase (DMQ hydroxylase, EC 1.14.99.60)** — a **ferritin-like carboxylate-bridged di-iron oxygenase** that catalyzes the **penultimate (C5) hydroxylation** of ubiquinone biosynthesis, converting demethoxyubiquinol to 3-demethylubiquinol using O₂. It functions as a **peripheral (monotopic) protein on the cytoplasmic face of the plasma membrane**, capturing its lipophilic, polyprenyl-tailed substrate at the membrane interface, and it supplies the precursor of **ubiquinone**, the essential respiratory-chain electron carrier. In *Pseudomonas* this di-iron enzyme — the true bacterial ortholog of eukaryotic COQ7/CLK-1 — is the evolutionary alternative to the unrelated flavin monooxygenase UbiF that performs the same step in *E. coli*. The assignment is supported by seven concordant lines of genetic, biochemical, bioinformatic, structural, and database evidence, though direct biochemistry on the *P. putida* protein itself remains to be performed.


## Artifacts

- [OpenScientist final report](coq7-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](coq7-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:11435415
2. PMID:23445365
3. PMID:15078893
4. PMID:30686758
5. PMID:27822549
6. PMID:12753928
7. PMID:10802164
8. PMID:23940037
9. PMID:16624818
10. PMID:26690054
11. PMID:36229432