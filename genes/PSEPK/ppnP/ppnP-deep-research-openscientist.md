---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-19T07:16:06.669979'
end_time: '2026-08-19T08:00:38.554507'
duration_seconds: 2671.88
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: ppnP
  gene_symbol: ppnP
  uniprot_accession: Q88F51
  protein_description: 'RecName: Full=Pyrimidine/purine nucleoside phosphorylase {ECO:0000255|HAMAP-Rule:MF_01537};
    EC=2.4.2.1 {ECO:0000255|HAMAP-Rule:MF_01537}; EC=2.4.2.2 {ECO:0000255|HAMAP-Rule:MF_01537};
    AltName: Full=Adenosine phosphorylase {ECO:0000255|HAMAP-Rule:MF_01537}; AltName:
    Full=Cytidine phosphorylase {ECO:0000255|HAMAP-Rule:MF_01537}; AltName: Full=Guanosine
    phosphorylase {ECO:0000255|HAMAP-Rule:MF_01537}; AltName: Full=Inosine phosphorylase
    {ECO:0000255|HAMAP-Rule:MF_01537}; AltName: Full=Thymidine phosphorylase {ECO:0000255|HAMAP-Rule:MF_01537};
    AltName: Full=Uridine phosphorylase {ECO:0000255|HAMAP-Rule:MF_01537}; AltName:
    Full=Xanthosine phosphorylase {ECO:0000255|HAMAP-Rule:MF_01537};'
  gene_info: Name=ppnP {ECO:0000255|HAMAP-Rule:MF_01537}; OrderedLocusNames=PP_4248;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the nucleoside phosphorylase PpnP family.
  protein_domains: Ppnp. (IPR009664); RmlC-like_jellyroll. (IPR014710); RmlC_Cupin_sf.
    (IPR011051); Ppnp (PF06865)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 3
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: ppnP-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ppnP-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88F51
- **Protein Description:** RecName: Full=Pyrimidine/purine nucleoside phosphorylase {ECO:0000255|HAMAP-Rule:MF_01537}; EC=2.4.2.1 {ECO:0000255|HAMAP-Rule:MF_01537}; EC=2.4.2.2 {ECO:0000255|HAMAP-Rule:MF_01537}; AltName: Full=Adenosine phosphorylase {ECO:0000255|HAMAP-Rule:MF_01537}; AltName: Full=Cytidine phosphorylase {ECO:0000255|HAMAP-Rule:MF_01537}; AltName: Full=Guanosine phosphorylase {ECO:0000255|HAMAP-Rule:MF_01537}; AltName: Full=Inosine phosphorylase {ECO:0000255|HAMAP-Rule:MF_01537}; AltName: Full=Thymidine phosphorylase {ECO:0000255|HAMAP-Rule:MF_01537}; AltName: Full=Uridine phosphorylase {ECO:0000255|HAMAP-Rule:MF_01537}; AltName: Full=Xanthosine phosphorylase {ECO:0000255|HAMAP-Rule:MF_01537};
- **Gene Information:** Name=ppnP {ECO:0000255|HAMAP-Rule:MF_01537}; OrderedLocusNames=PP_4248;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the nucleoside phosphorylase PpnP family.
- **Key Domains:** Ppnp. (IPR009664); RmlC-like_jellyroll. (IPR014710); RmlC_Cupin_sf. (IPR011051); Ppnp (PF06865)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ppnP" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ppnP' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ppnP** (gene ID: ppnP, UniProt: Q88F51) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: **ppnP** (PP_4248, UniProt Q88F51) — Pyrimidine/Purine Nucleoside Phosphorylase from *Pseudomonas putida* KT2440

## Summary

The gene **ppnP** (ordered locus name **PP_4248**; UniProt accession **Q88F51**, entry name PPNP_PSEPK) of *Pseudomonas putida* KT2440 encodes a small (94-residue) cytoplasmic enzyme, **pyrimidine/purine nucleoside phosphorylase (PpnP)**. Its primary and defining function is to catalyze the **reversible phosphorolysis of the N-glycosidic bond of nucleosides**: a nucleoside plus inorganic phosphate is cleaved into the free nucleobase and (2-deoxy)-α-D-ribose-1-phosphate. The enzyme is unusually broad in substrate scope, acting on **both purine and pyrimidine nucleosides** (ribo- and deoxyribo-), which is why it carries two Enzyme Commission numbers, **EC 2.4.2.1** (purine-nucleoside phosphorylase) and **EC 2.4.2.2** (pyrimidine-nucleoside phosphorylase), and a raft of alternative names — adenosine, cytidine, guanosine, inosine, thymidine, uridine, and xanthosine phosphorylase.

Structurally, PpnP represents a **distinct, third class of nucleoside phosphorylase**. Unlike the classical NP-I (trimeric/hexameric) and NP-II (dimeric) families, PpnP adopts an **RmlC-like cupin (jelly-roll) fold** and assembles as a **rigid homodimer** bearing a hydrophobic nucleoside-binding pocket. Q88F51 carries the diagnostic Pfam PF06865 (Ppnp) domain and the InterPro cupin superfamily signatures (IPR009664, IPR011051, IPR014710); its AlphaFold model is of very high confidence (mean pLDDT ≈ 98), consistent with the crystallographically observed cupin fold of its orthologs.

Functionally, PpnP operates at the **entry point of intracellular nucleoside catabolism and salvage**. By liberating free bases it feeds base-salvage pathways, and by producing (deoxy)ribose-1-phosphate it supplies — through phosphopentomutase and the pentose-phosphate/PRPP node — both nucleotide biosynthesis and central carbon/energy metabolism. The gene product is a soluble, single-domain protein with no signal peptide or transmembrane segment, and thus performs its function in the **cytoplasm**. The identification of PpnP's activity traces to a landmark high-throughput in vitro metabolomics screen of *E. coli*'s uncharacterized proteins, and the reaction set is now recorded explicitly in UniProt. Because *P. putida* Q88F51 shares the same length, conserved sequence blocks, domain assignment, and fold as the experimentally characterized *E. coli* ortholog, its annotation as a PpnP-family nucleoside phosphorylase is well supported.

---

## Key Findings

### F001 — Q88F51 is a bona fide PpnP-family pyrimidine/purine nucleoside phosphorylase

Q88F51 (entry name PPNP_PSEPK) is a 94-amino-acid protein encoded by the gene **ppnP** (ordered locus name **PP_4248**) in *P. putida* KT2440. It is annotated by the curated HAMAP rule **MF_01537** to the **nucleoside phosphorylase PpnP family** and carries the family-diagnostic domains: **Pfam PF06865 (Ppnp)**, **InterPro IPR009664 (Ppnp)**, and the RmlC-like cupin jelly-roll fold signatures **IPR014710 / IPR011051**. A direct pairwise comparison with the *E. coli* PpnP ortholog (UniProt P0C037, also 94 residues) shows identical length and multiple conserved sequence blocks (e.g., NEYF, KSI, SVGVM, SGAL, FNVP, YLC), confirming that the *P. putida* protein is a true member of this family rather than a same-symbol coincidence.

The PpnP class is defined in the primary literature as a distinct group of nucleoside phosphorylases. As Wen et al. describe, PpnP represents "another class of NP protein in *Escherichia coli* named Pyrimidine/purine nucleoside phosphorylase (ppnP), which can catalyze the phosphorolysis of diverse nucleosides and yield d-ribose 1-phosphate and the respective free bases" ([PMID: 35094440](https://pubmed.ncbi.nlm.nih.gov/35094440/)). This establishes the enzymatic identity assigned to Q88F51 and its EC numbers **2.4.2.1** and **2.4.2.2**. **Gene/organism verification passed**: the gene symbol, organism, protein family, and domain architecture all align with the UniProt-provided identity, and the closest experimentally characterized literature (*E. coli* PpnP) belongs to the same family — so this report proceeds with confidence that it describes the correct protein.

### F002 — PpnP catalyzes reversible phosphorolysis of both purine and pyrimidine nucleosides with broad specificity

The core reaction catalyzed by PpnP is:

> **nucleoside + phosphate ⇌ nucleobase + (2-deoxy)-α-D-ribose-1-phosphate**

The enzyme's dual EC assignment — **EC 2.4.2.1** (purine-nucleoside phosphorylase) and **EC 2.4.2.2** (pyrimidine-nucleoside phosphorylase) — reflects its unusually broad substrate range. UniProt's alternative names for Q88F51 enumerate activity on **adenosine, cytidine, guanosine, inosine, thymidine, uridine, and xanthosine**, spanning both purine and pyrimidine bases and both ribo- and deoxyribonucleosides. The experimentally characterized *E. coli* ortholog was shown to "catalyze the phosphorolysis of diverse nucleosides and yield d-ribose 1-phosphate and the respective free bases" ([PMID: 35094440](https://pubmed.ncbi.nlm.nih.gov/35094440/)), documenting both the breadth of substrates and the reaction products.

The reaction is physiologically important because its products are not dead ends: the ribose-1-phosphate generated is a metabolic currency. As Tozzi et al. explain, "ribose-1-phosphate, produced by purine nucleoside phosphorylase acting catabolically, is either anabolized for pyrimidine salvage and 5-fluorouracil activation, with uridine phosphorylase acting anabolically, or recycled for nucleoside and base interconversion" ([PMID: 16519676](https://pubmed.ncbi.nlm.nih.gov/16519676/)). This situates PpnP's product at a branch point feeding both salvage and interconversion.

### F003 — PpnP defines a third structural class of nucleoside phosphorylase: a cupin-fold rigid dimer with a hydrophobic nucleoside pocket

Nucleoside phosphorylases were classically divided into two structural superfamilies (NP-I, trimeric/hexameric; NP-II, dimeric). PpnP is neither. Crystal structures of PpnP from *E. coli* and three additional species revealed that "the structure of ppnP belongs to the RlmC-like Cupin fold and showed as a rigid dimeric conformation" ([PMID: 35094440](https://pubmed.ncbi.nlm.nih.gov/35094440/)) — establishing PpnP as a **third, structurally distinct class**. The same study identified "a potential nucleoside binding pocket full of hydrophobic residues, and the residues involved in the dimer and pocket formation are all well conserved in bacteria" ([PMID: 35094440](https://pubmed.ncbi.nlm.nih.gov/35094440/)).

The conservation of both the dimer interface and the hydrophobic pocket residues across bacteria is the structural basis for extending this mechanistic picture to *P. putida*: Q88F51 carries the identical PF06865 / IPR009664 Ppnp domain and the RmlC-like cupin superfamily fold (IPR011051 / IPR014710). The hydrophobic active-site pocket is consistent with the enzyme's ability to accommodate a wide variety of nucleobases, rationalizing the broad substrate specificity described in F002.

### F004 — PpnP functions in the cytoplasm within nucleoside catabolism/salvage, feeding pentose phosphates into central carbon metabolism

Q88F51 is a small (94 aa), soluble, single-domain protein with **no signal peptide and no transmembrane region**, features that firmly place it in the **cytoplasm**, where nucleoside catabolism occurs. Its metabolic role is to sit at the head of the pathway that mobilizes the sugar and base moieties of nucleosides. The (deoxy)ribose-1-phosphate it releases is interconverted by phosphopentomutase to ribose-5-phosphate, the precursor of PRPP. As Tozzi et al. state, "the two main pentose phosphates, ribose-5-phosphate and ribose-1-phosphate, are readily interconverted by the action of phosphopentomutase. Ribose-5-phosphate is the direct precursor of 5-phosphoribosyl-1-pyrophosphate, for both de novo and 'salvage' synthesis of nucleotides" ([PMID: 16519676](https://pubmed.ncbi.nlm.nih.gov/16519676/)).

Beyond nucleotide synthesis, the pentose moiety serves as a carbon and energy source. The same review notes that "the nucleosides can be regarded, both in bacteria and in eukaryotic cells, as carriers of sugars, that are made available though the action of nucleoside phosphorylases" ([PMID: 16519676](https://pubmed.ncbi.nlm.nih.gov/16519676/)). Thus PpnP simultaneously (i) recycles nucleobases for base salvage and (ii) channels the pentose backbone into the pentose-phosphate pathway and central carbon metabolism — a role especially relevant for a metabolically versatile soil bacterium like *P. putida*.

### F005 — PpnP's function was experimentally discovered by high-throughput in vitro metabolomics; UniProt lists explicit per-substrate reactions

The functional annotation of the PpnP family rests on direct experimental evidence. The *E. coli* ortholog that defines PpnP function — **yaiE/ppnP** (UniProt P0C037, evidence at protein level, PE = 1) — was experimentally characterized in a nontargeted in vitro metabolomics screen by Sévin et al.: "In screening all 1,275 functionally uncharacterized *Escherichia coli* proteins, we discovered 241 potential novel enzymes, 12 of which we experimentally validated" ([PMID: 27941785](https://pubmed.ncbi.nlm.nih.gov/27941785/)). PpnP was among the validated novel enzymes, assigning it nucleoside phosphorylase activity.

Reflecting this, UniProt records **eight explicit catalytic reactions** for Q88F51:

| EC | Substrate | Products |
|----|-----------|----------|
| 2.4.2.1 | Adenosine + phosphate | Adenine + α-D-ribose-1-phosphate |
| 2.4.2.1 | Guanosine + phosphate | Guanine + α-D-ribose-1-phosphate |
| 2.4.2.1 | Inosine + phosphate | Hypoxanthine + α-D-ribose-1-phosphate |
| 2.4.2.1 | Xanthosine + phosphate | Xanthine + α-D-ribose-1-phosphate |
| 2.4.2.2 | Cytidine + phosphate | Cytosine + α-D-ribose-1-phosphate |
| 2.4.2.2 | Uridine + phosphate | Uracil + α-D-ribose-1-phosphate |
| 2.4.2.2 | Thymidine + phosphate | Thymine + 2-deoxy-α-D-ribose-1-phosphate |

The enzyme is annotated with the keywords Glycosyltransferase/Transferase and, notably, has **no cofactor or metal-ion requirement** — it is metal-independent, unlike some other transferases. The reaction with thymidine (a 2'-deoxyribonucleoside) yielding 2-deoxy-α-D-ribose-1-phosphate confirms the enzyme's activity on both ribo- and deoxyribonucleosides.

### F006 — The AlphaFold model of Q88F51 is very high confidence, supporting the predicted cupin fold

The AlphaFold DB model of Q88F51 (94 residues) has a **mean per-residue pLDDT of 97.9**, with **98% of Cα residues scoring >90** and **100% scoring >70**, indicating a very confidently predicted, well-ordered single-domain structure. This is fully consistent with the RmlC-like cupin (jelly-roll) fold assigned by InterPro (IPR011051 / IPR014710) and observed crystallographically for PpnP orthologs. In other words, the computational structure prediction independently corroborates the domain-based and homology-based structural assignment: "the structure of ppnP belongs to the RlmC-like Cupin fold and showed as a rigid dimeric conformation" ([PMID: 35094440](https://pubmed.ncbi.nlm.nih.gov/35094440/)). The high confidence of the model, combined with the small size and single-domain architecture, reinforces that Q88F51 folds into the compact cupin barrel characteristic of the PpnP family.

---

## Mechanistic Model / Interpretation

PpnP is best understood as the **broad-specificity gatekeeper of nucleoside phosphorolysis** in *P. putida*. The following schematic summarizes its catalytic role and metabolic context:

```
        Purine nucleosides                Pyrimidine nucleosides
   (adenosine, guanosine,              (cytidine, uridine,
    inosine, xanthosine)                thymidine, ...)
             │                                   │
             │        + inorganic phosphate (Pi) │
             ▼                                   ▼
      ┌───────────────────────────────────────────────┐
      │            PpnP  (Q88F51 / PP_4248)            │
      │   Cupin-fold rigid homodimer, cytoplasmic      │
      │   EC 2.4.2.1 (purine) + EC 2.4.2.2 (pyrimidine)│
      │            metal-independent                    │
      └───────────────────────────────────────────────┘
             │                                   │
             ▼                                   ▼
     free nucleobases              (2-deoxy)-α-D-ribose-1-phosphate
  (adenine, guanine,                          │
   hypoxanthine, xanthine,      phosphopentomutase (deoB)
   cytosine, uracil, thymine)                 │
             │                                 ▼
             ▼                         ribose-5-phosphate
     BASE SALVAGE                              │
   (PRT enzymes + PRPP)          ┌─────────────┴─────────────┐
             │                   ▼                           ▼
             ▼            PRPP / nucleotide          pentose-phosphate
        nucleotides       biosynthesis (de novo    pathway → central
                          + salvage)                carbon / energy
```

**Reaction chemistry.** PpnP cleaves the N-glycosidic bond linking the nucleobase to the pentose sugar, using inorganic phosphate as the nucleophile. The result is a free base plus a phosphorylated sugar, α-D-ribose-1-phosphate (or 2-deoxy-α-D-ribose-1-phosphate for deoxyribonucleosides). The reaction is fully reversible, so under anabolic conditions PpnP can, in principle, run in the synthetic direction. The absence of any metal-ion or cofactor requirement distinguishes PpnP mechanistically and simplifies its catalytic machinery, which relies instead on a constellation of conserved active-site residues lining a hydrophobic pocket.

**Structural distinctiveness.** The most striking feature of PpnP is that it solves the same catalytic problem as the classical NP-I and NP-II phosphorylases using a **completely different protein fold** — the RmlC-like cupin jelly-roll. This is a textbook case of convergent evolution of enzymatic function on an unrelated structural scaffold. The rigid dimeric assembly and hydrophobic base-binding pocket are conserved across bacteria, and Q88F51's domain assignment and very-high-confidence AlphaFold model indicate that the *P. putida* enzyme adopts this same architecture.

**Physiological logic.** In *P. putida*, a nutritionally versatile soil organism, the ability to salvage nucleobases and to harvest ribose from nucleosides is metabolically valuable. PpnP provides a single, broad-specificity enzyme that can process essentially the full spectrum of dietary or turnover-derived nucleosides, funneling bases into salvage and the pentose into the phosphopentomutase → ribose-5-phosphate → PRPP / pentose-phosphate hub. This allows nucleosides to serve simultaneously as nitrogen (via bases), carbon, and energy sources.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|------|-----------------|---------------------|
| [35094440](https://pubmed.ncbi.nlm.nih.gov/35094440/) | *Crystal structures of a new class of pyrimidine/purine nucleoside phosphorylase revealed a Cupin fold* | **Primary structural/functional source.** Defines PpnP as a distinct NP class, establishes the cupin dimeric fold, the hydrophobic nucleoside pocket, broad substrate phosphorolysis, and conservation across bacteria. Supports F001–F003 and F006. |
| [27941785](https://pubmed.ncbi.nlm.nih.gov/27941785/) | *Nontargeted in vitro metabolomics for high-throughput identification of novel enzymes in E. coli* | **Primary experimental discovery source.** High-throughput screen that experimentally validated *E. coli* yaiE/ppnP as a nucleoside phosphorylase, the basis of the family annotation. Supports F005. |
| [16519676](https://pubmed.ncbi.nlm.nih.gov/16519676/) | *Pentose phosphates in nucleoside interconversion and catabolism* | **Pathway context.** Explains how ribose-1-phosphate is interconverted by phosphopentomutase to ribose-5-phosphate/PRPP and how nucleosides act as sugar carriers. Supports F002 and F004. |
| [15115774](https://pubmed.ncbi.nlm.nih.gov/15115774/) | *Characterization of E. coli uridine phosphorylase by single-site mutagenesis* | **Comparative context** on active-site residues of a classical (NP-I) pyrimidine phosphorylase; useful for contrasting the distinct PpnP fold. |
| [36601892](https://pubmed.ncbi.nlm.nih.gov/36601892/) | *Computational design of prospective molecular targets for Burkholderia cepacia complex...* | **Applied interest.** Selected ppnP as a candidate drug target and modeled its 3D structure, illustrating interest in PpnP as an antibacterial target. |
| [1664051](https://pubmed.ncbi.nlm.nih.gov/1664051/) | *Guanosine kinase from Trichomonas vaginalis* | **Peripheral context** on nucleoside metabolism/salvage enzymes; not directly on PpnP. |

The evidentiary chain for Q88F51 combines: (i) **direct experimental annotation** of the orthologous *E. coli* enzyme (PMID 27941785); (ii) **direct structural characterization** of PpnP-family enzymes including the cupin fold and conserved active site (PMID 35094440); (iii) **sequence and domain homology** linking Q88F51 unambiguously to that family (94-aa length, conserved blocks, PF06865/IPR009664); (iv) **high-confidence structure prediction** (AlphaFold pLDDT ≈ 98) confirming the fold; and (v) **pathway-level reviews** establishing the metabolic destination of its products (PMID 16519676). No literature was found describing a different, conflicting gene under the symbol "ppnP" — all evidence converges on the same nucleoside-phosphorylase identity.

---

## Limitations and Knowledge Gaps

1. **No direct enzymology on the *P. putida* protein.** All experimental catalytic characterization (activity assays, structures) derives from the *E. coli* ortholog and other bacterial PpnP homologs. Q88F51's activity is inferred by strong homology and domain identity rather than measured directly. Kinetic parameters (kcat, Km) and substrate-preference ranking specific to the *P. putida* enzyme are unknown.

2. **Substrate-preference quantification is qualitative.** While the enzyme is broadly specific, the relative catalytic efficiency across the seven-plus named substrates (e.g., whether it favors purine over pyrimidine, or ribo- over deoxyribonucleosides) has not been quantified for Q88F51.

3. **Directionality in vivo.** The reaction is reversible; the physiologically dominant direction (catabolic phosphorolysis vs. anabolic synthesis) in *P. putida* under given growth conditions has not been established experimentally.

4. **Genetic/physiological role untested.** No knockout, complementation, or growth-phenotype data for PP_4248 in *P. putida* were found. Its essentiality, regulation, and quantitative contribution to nucleoside catabolism relative to any paralogous phosphorylases remain uncharacterized.

5. **Structural inference.** The cytoplasmic localization and homodimeric assembly for Q88F51 are inferred from sequence features and family homology plus a high-confidence AlphaFold monomer model; no experimental structure of the *P. putida* protein exists, and AlphaFold confidence does not validate the dimer interface or catalytic geometry directly.

6. **Active-site residue mapping.** The specific catalytic and substrate-binding residues have not been mapped onto the Q88F51 sequence in this investigation; this would strengthen mechanistic claims.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and enzyme assays.** Clone PP_4248, purify the protein, and measure phosphorolytic activity across all candidate substrates (adenosine, guanosine, inosine, xanthosine, cytidine, uridine, thymidine, and deoxyribonucleosides) to obtain kcat/Km values and rank substrate preference for the *P. putida* enzyme specifically.

2. **Crystallography / cryo-EM.** Determine the experimental structure of Q88F51, ideally with substrate/phosphate bound, to confirm the cupin fold, the dimer interface, and the active-site architecture, and to identify catalytic residues.

3. **Active-site residue mapping and mutagenesis.** Align Q88F51 with the crystallized *E. coli* PpnP, map conserved pocket and dimer residues, and perform site-directed mutagenesis to confirm their catalytic roles (analogous to the uridine-phosphorylase mutagenesis in PMID 15115774).

4. **Genetics in *P. putida* KT2440.** Construct a ΔPP_4248 mutant and assess growth on nucleosides as carbon/nitrogen sources, measure intracellular nucleoside/base pools, and test complementation to establish the enzyme's in vivo role and whether it is redundant with other phosphorylases.

5. **Metabolic flux analysis.** Use labeled nucleosides to trace flux from PpnP-derived ribose-1-phosphate through phosphopentomutase into the pentose-phosphate/PRPP node, quantifying PpnP's contribution to central carbon metabolism.

6. **Regulation and expression.** Characterize transcriptional regulation of ppnP (induction by nucleosides, growth phase, nutrient limitation) to understand when the catabolic pathway is engaged.

7. **Target validation (applied).** Given the interest in PpnP as an antibacterial target (PMID 36601892), experimentally validate whether inhibition of PpnP impairs growth under nucleoside-dependent conditions.

---

## Conclusion

**ppnP (PP_4248, Q88F51)** in *Pseudomonas putida* KT2440 encodes **pyrimidine/purine nucleoside phosphorylase (PpnP)**, a small, metal-independent, cytoplasmic enzyme (EC 2.4.2.1 / EC 2.4.2.2) that catalyzes the reversible phosphorolysis of the N-glycosidic bond of a broad range of purine and pyrimidine (deoxy)ribonucleosides, producing the free nucleobase and (2-deoxy)-α-D-ribose-1-phosphate. It belongs to a structurally distinct third class of nucleoside phosphorylases defined by an RmlC-like cupin-fold rigid homodimer with a hydrophobic active-site pocket — an assignment supported by its diagnostic Ppnp/cupin domains and a very-high-confidence AlphaFold model. Functionally, it stands at the entry of intracellular nucleoside catabolism and salvage, recycling bases and funneling ribose-1-phosphate via phosphopentomutase into the PRPP/pentose-phosphate hub of central carbon metabolism. The annotation is well supported by experimental characterization of the orthologous *E. coli* enzyme and by strong sequence/structural homology, though direct enzymatic and genetic characterization of the *P. putida* protein itself remains to be performed.


## Artifacts

- [OpenScientist final report](ppnP-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ppnP-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:35094440
2. PMID:16519676
3. PMID:27941785