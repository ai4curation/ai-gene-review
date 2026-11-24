---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T15:13:43.188802'
end_time: '2026-10-24T16:31:28.512145'
duration_seconds: 4665.32
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: mouse
  gene_id: Rtl8a
  gene_symbol: Rtl8a
  uniprot_accession: F6VWQ4
  protein_description: 'SubName: Full=Retrotransposon Gag like 8A {ECO:0000313|Ensembl:ENSMUSP00000086158.4};
    SubName: Full=Retrotransposon Gag like 8B {ECO:0000313|Ensembl:ENSMUSP00000086157.4};'
  gene_info: Name=Rtl8a {ECO:0000313|Ensembl:ENSMUSP00000086158.4}; Synonyms=Rtl8b
    {ECO:0000313|Ensembl:ENSMUSP00000086157.4};
  organism_full: Mus musculus (Mouse).
  protein_family: Not specified in UniProt
  protein_domains: RTL1/1-8/LDOC_capsid-like. (IPR032549); RTL1-8_LDOC (PF16297)
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Rtl8a-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Rtl8a-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** F6VWQ4
- **Protein Description:** SubName: Full=Retrotransposon Gag like 8A {ECO:0000313|Ensembl:ENSMUSP00000086158.4}; SubName: Full=Retrotransposon Gag like 8B {ECO:0000313|Ensembl:ENSMUSP00000086157.4};
- **Gene Information:** Name=Rtl8a {ECO:0000313|Ensembl:ENSMUSP00000086158.4}; Synonyms=Rtl8b {ECO:0000313|Ensembl:ENSMUSP00000086157.4};
- **Organism (full):** Mus musculus (Mouse).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** RTL1/1-8/LDOC_capsid-like. (IPR032549); RTL1-8_LDOC (PF16297)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Rtl8a" matches the protein description above**
2. **Verify the organism is correct:** Mus musculus (Mouse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Rtl8a' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Rtl8a** (gene ID: Rtl8a, UniProt: F6VWQ4) in mouse.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *Rtl8a* (Retrotransposon Gag-like 8A), Mouse

**Target:** *Rtl8a* / *Rtl8b* (Mus musculus) — UniProt **F6VWQ4**
**Protein:** Retrotransposon Gag-like 8 (RTL8; Mart/SIRH family of retrotransposon-derived genes; human orthologs are the FAM127/RTL8A–C genes)
**Key domain:** RTL1/1-8/LDOC capsid-like domain (InterPro IPR032549; Pfam PF16297)

---

## 1. Summary (Answer to the Research Question)

*Rtl8a* encodes **RTL8**, a small (~13 kDa) protein belonging to the **Mart/SIRH family of domesticated retrotransposon (Ty3/Gypsy-type) Gag-derived genes**. It is **not an enzyme, transporter, or classical signaling molecule**; rather, it is a **capsid-like protein-interaction adapter**. RTL8 corresponds to a truncated version of its paralog **PEG10**, consisting essentially of the **N-terminal Gag/capsid-like domain** and lacking the capacity to form particles on its own.

Its **primary molecular function** is to act as a **small structural adapter that regulates other retroelement-derived capsid proteins and the proteostasis machinery**, through two interlocking activities:

1. **Nucleolar targeting and control of UBQLN2 trafficking** — RTL8 localizes to **nucleoli** and promotes **nuclear translocation of the ubiquilin UBQLN2** into subnuclear protein-quality-control (PQC) compartments (validated in **mouse brain**).
2. **Antagonism of PEG10 capsid assembly** — RTL8 binds the **PEG10 capsid (Gag) domain**, is co-incorporated into PEG10 particles, and **inhibits PEG10 virus-like-particle (VLP) formation/release**, while also being the **required bridge** that lets UBQLN2 complex with PEG10 and be recruited to **stress granules**.

Thus RTL8 operates at the interface of **endogenous retrovirus-like protein biology and the ubiquitin–proteasome/stress-granule proteostasis network**, functioning in both the **nucleus/nucleolus** and the **cytoplasm (stress granules)**.

---

## 2. Gene/Protein Identity Verification

The provided UniProt record (F6VWQ4; "Retrotransposon Gag like 8A/8B", mouse, *Rtl8a/Rtl8b*, RTL1/1-8/LDOC capsid-like domain) **matches** the published literature on **RTL8** (Mart/SIRH family; human orthologs = FAM127A/B/C, i.e. RTL8C/A/B):

- The literature describes RTL8 as a **Mart-family / retroelement-derived gene** with an **N-terminal Gag-like capsid domain** — exactly the IPR032549 / PF16297 domain annotated for F6VWQ4 [PMID 39775359].
- The UBQLN2–RTL8 interaction was confirmed **in mouse brain tissue**, directly matching the mouse organism of the target [PMID 35247097].
- RTL8 exists as a set of **near-identical paralogs** (in human RTL8A/B/C; in mouse *Rtl8a/Rtl8b/Rtl8c*), consistent with the dual gene naming (Rtl8a / Rtl8b) on this UniProt entry.

**Conclusion:** This is the correct gene. The literature describes the same protein family, domain, and organism. No evidence of a conflicting same-symbol gene was found.

---

## 3. Molecular Identity and Structure

RTL8 is one of the smallest members of the **SIRH/Mart ("Sushi-ichi retrotransposon homolog" / Mammalian retrotransposon-derived) family** of domesticated **LTR-retrotransposon Gag genes**. Key structural facts:

- It is a **~13 kDa** protein [PMID 35247097].
- It **resembles a truncated form of PEG10**, sharing homology specifically with the **N-terminal Gag-like capsid domain** [PMID 39775359]. This is the IPR032549 "RTL1/1-8/LDOC capsid-like" domain annotated on F6VWQ4.
- **Alone, RTL8 cannot form virus-like particles (VLPs)** — unlike PEG10, which self-assembles into Gag-type capsids — but RTL8 **can be incorporated into PEG10-derived particles** [PMID 39775359].

Mechanistically this is important: because RTL8 is essentially a "lone capsid domain," it functions as a **capsid-interaction module** that docks onto, and co-assembles with, the full-length capsid proteins of its paralogs (notably PEG10), as well as onto proteostasis factors (UBQLN2). It has **no known catalytic activity**; its function is **structural/adaptor**, derived from the ancestral viral capsid fold.

*Context:* PEG10, the closest relative, is a Mart-family gene essential for placentation that forms Gag-type VLPs and even **binds and secretes its own mRNA** in extracellular vesicles [PMID 34413232]. RTL8 should be understood as a regulatory "satellite" of this capsid-forming machinery.

### 3.1 Evolutionary origin and domain architecture (bioinformatic evidence)

- The **UniProt record F6VWQ4** (gene *Rtl8a*, MGI:1913408) is a **113-amino-acid (~13 kDa)** protein consisting **almost entirely of a single "RTL1/3-8/LDOC capsid-like" domain (residues 18–113)**; the entry carries **no GO or subcellular-location annotations** (an uncharacterized TrEMBL entry), underscoring that functional knowledge comes from primary literature, not database annotation.
- RTL8 belongs to the family of **>50 cellular genes derived by recurrent "molecular domestication" of Gypsy/Ty3 LTR-retrotransposons** in mammalian genomes; these genes are **conserved across divergent mammals** and show similarity to **Gag**, the structural capsid protein of retroelements. Active Gypsy/Ty3 retrotransposons were themselves eliminated from the mammalian lineage **>180 million years ago** [PMID 19845640].
- Because the protein is a **lone Gag/capsid-like domain** (no reverse transcriptase, protease, or integrase), its biology is necessarily **structural/adaptor**, consistent with its experimentally demonstrated capsid co-assembly (PEG10) and protein-binding (UBQLN2) activities.

### 3.2 Mouse genomic context (Ensembl GRCm39)

The mouse genome contains a **tandem cluster of three near-identical *Rtl8* paralogs on the X chromosome**, all within <70 kb:

| Gene | Ensembl ID | Location (chr X) | Strand |
|---|---|---|---|
| *Rtl8c* | ENSMUSG00000051851 | 52,609,752–52,612,251 | + |
| *Rtl8a* | ENSMUSG00000067925 | 52,644,455–52,645,649 | − |
| *Rtl8b* | ENSMUSG00000067924 | 52,671,141–52,680,104 | − |

Because *Rtl8a/8b/8c* encode **near-identical 113-aa proteins**, the UniProt entry F6VWQ4 is listed under both *Rtl8a* and *Rtl8b*, and most experimental assays detect "RTL8" collectively rather than resolving individual paralogs. The demonstrated RTL8 functions therefore apply to the cluster as a group, of which *Rtl8a* is a representative member. Note that the RTL8 cluster is **X-linked**, distinguishing it from its autosomal, imprinted relative *Peg10*.

---

## 4. Primary Function and Mechanism

Because RTL8 is non-enzymatic, its "primary function" is best described as a **capsid-like adapter/regulator**. Two mechanistic axes are well supported:

### 4.1 Nucleolar protein and regulator of UBQLN2 (protein quality control)

- RTL8 was discovered as an interactor of **UBQLN2**, a ubiquitin-proteasome shuttle/adaptor protein implicated in ALS/FTD and other neurodegenerative diseases [PMID 35247097].
- Under both endogenous and overexpressed conditions, **RTL8 localizes to nucleoli** [PMID 35247097].
- When co-expressed, **RTL8 promotes nuclear translocation of UBQLN2**, including during **heat-shock stress**, delivering UBQLN2 into **ubiquitin-enriched subnuclear structures containing PQC components** [PMID 35247097].
- This activity is **specific to UBQLN2** (not the related UBQLN1 or UBQLN4), and **UBQLN2 reciprocally stabilizes RTL8** protein levels in human cell lines and mouse brain [PMID 35247097].

**Interpretation:** RTL8 is a nucleolar adapter that governs the **nuclear/subnuclear distribution of UBQLN2**, thereby feeding into the **ubiquitin–proteasome protein-quality-control pathway**. This links the gene to clearance of aberrant nuclear proteins and to neurodegeneration-relevant proteostasis.

### 4.2 Antagonist of PEG10 capsid (VLP) assembly

- RTL8 **binds the N-terminal (capsid) domain of PEG10** and is **packaged into PEG10 particles** [PMID 39775359].
- RTL8 co-expression **decreases secreted PEG10 VLP abundance** while **increasing intracellular PEG10**, indicating it **inhibits PEG10 VLP formation or release** [PMID 39775359].
- Modulating RTL8 levels changes PEG10-derived VLP abundance in cells that naturally produce them [PMID 39775359].

**Interpretation:** By co-assembling into PEG10 capsids through the shared Gag fold, RTL8 acts as a **dominant-negative–like structural inhibitor (antagonist)** of PEG10 particle assembly/secretion — a rare example of one domesticated retroelement protein regulating another.

### 4.3 Required bridge for the UBQLN2–PEG10–stress-granule network

- **RTL8 confers on UBQLN2 the ability to complex with and regulate PEG10** [PMID 40680123].
- PEG10, a **core stress-granule component** that forms VLPs within granules, **recruits UBQLN2 to stress granules under stress — but only when RTL8 is present** [PMID 40680123].
- Changing RTL8/PEG10/UBQLN2 levels **remodels stress-granule disassembly kinetics and translation recovery** [PMID 40680123; preprint PMID 39484508].

**Interpretation:** RTL8 is an **obligatory adapter** coupling UBQLN2 proteostasis machinery to PEG10 capsids within **cytoplasmic stress granules**, integrating two endogenous retrovirus-like proteins into the cellular stress response.

---

## 5. Subcellular Localization

RTL8 operates in **multiple compartments**, consistent with its adapter role:

| Compartment | Evidence |
|---|---|
| **Nucleolus** (steady state) | RTL8 localizes to nucleoli endogenously and when overexpressed [PMID 35247097] |
| **Nucleus / subnuclear PQC bodies** | Co-translocates with UBQLN2 into ubiquitin-enriched subnuclear structures [PMID 35247097] |
| **Cytoplasm / stress granules** | Required for UBQLN2 recruitment to PEG10-containing stress granules [PMID 40680123] |
| **PEG10 particles / VLPs** | Incorporated into PEG10-derived capsid particles [PMID 39775359] |

---

## 6. Pathways and Biological Context

- **Ubiquitin–proteasome system / protein quality control:** via control of UBQLN2 localization and stability [PMID 35247097].
- **Stress-granule dynamics and translational recovery:** via the RTL8–PEG10–UBQLN2 axis [PMID 40680123].
- **Endogenous retrovirus-like (Mart/SIRH) protein network:** direct regulation of PEG10 capsid assembly [PMID 39775359].
- **Tissue context:** RTL8 is **broadly expressed in many of the same tissues as PEG10, including brain** [PMID 39775359]; the functional interaction with UBQLN2 was confirmed in **mouse brain** [PMID 35247097], making the brain a particularly relevant site of action.
- **Disease relevance:** UBQLN2 and PEG10 are implicated in **ALS/FTD and other neurodegenerative diseases**; RTL8, as their shared regulator, is positioned within this neurodegeneration-associated proteostasis network [PMID 35247097; PMID 40680123].

---

## 7. Supported and Refuted Hypotheses

**Supported:**
- H1: RTL8 is a domesticated retrotransposon Gag/capsid-like protein (truncated PEG10-like). ✔ [PMID 39775359]
- H2: RTL8 is a nucleolar protein that controls UBQLN2 nuclear trafficking. ✔ [PMID 35247097]
- H3: RTL8 regulates PEG10 capsid/VLP assembly (antagonist). ✔ [PMID 39775359]
- H4: RTL8 bridges UBQLN2–PEG10 interaction in stress granules. ✔ [PMID 40680123]

**Refuted / not supported:**
- The protein is **not** an enzyme or transporter; no catalytic or transport activity is described. Its "retrotransposon Gag-like" name reflects evolutionary origin, not an active transposition function.

---

## 8. Limitations and Future Directions

- Much of the mechanistic detail comes from **human cell lines and overexpression**; the strongest mouse-specific evidence is the **UBQLN2–RTL8 interaction in mouse brain** [PMID 35247097]. Endogenous mouse *Rtl8a*-specific loss-of-function phenotypes are not yet well characterized in the retrieved literature.
- Mouse has **near-identical paralogs (*Rtl8a/8b/8c*)** arranged as a **tandem X-linked cluster** (chr X ~52.61–52.68 Mb, Ensembl GRCm39), complicating isoform-specific functional assignment; most antibodies/assays detect "RTL8" collectively.
- The field is young (key papers 2022–2025); **structural confirmation** (e.g., cryo-EM of RTL8 within PEG10 capsids) and **in vivo developmental/neurological roles** in mouse remain open.
- Future work: conditional *Rtl8a* knockout phenotyping, isoform-resolved expression mapping, and direct tests of whether RTL8-regulated PEG10/UBQLN2 proteostasis modifies neurodegeneration models.

---

## References (PMIDs)

- PMID **19845640** — Volff, J.N. Cellular genes derived from Gypsy/Ty3 retrotransposons in mammalian genomes (2009; evolutionary origin review).
- PMID **35247097** — RTL8 promotes nuclear localization of UBQLN2 to subnuclear PQC compartments (2022; mouse brain validation).
- PMID **39775359** — The gag-like gene RTL8 antagonizes PEG10-mediated virus-like particles (2024).
- PMID **40680123** — Endogenous retrovirus-like proteins recruit UBQLN2 to stress granules and shape their functional biology (2025).
- PMID **39484508** — (preprint of the above) Endogenous retrovirus-like proteins recruit UBQLN2 to stress granules (2024).
- PMID **34413232** — Mammalian retrovirus-like protein PEG10 packages its own mRNA / VLP context (2021).


## Artifacts

- [OpenScientist final report](Rtl8a-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Rtl8a-deep-research-openscientist_artifacts/final_report.pdf)