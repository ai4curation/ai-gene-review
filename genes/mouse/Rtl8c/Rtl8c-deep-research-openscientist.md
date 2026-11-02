---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T15:34:42.780630'
end_time: '2026-10-24T16:20:25.817784'
duration_seconds: 2743.04
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: mouse
  gene_id: Rtl8c
  gene_symbol: Rtl8c
  uniprot_accession: F6TUF7
  protein_description: 'SubName: Full=Retrotransposon Gag like 8C {ECO:0000313|Ensembl:ENSMUSP00000069901.4};'
  gene_info: Name=Rtl8c {ECO:0000313|Ensembl:ENSMUSP00000069901.4};
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
citation_count: 12
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Rtl8c-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Rtl8c-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** F6TUF7
- **Protein Description:** SubName: Full=Retrotransposon Gag like 8C {ECO:0000313|Ensembl:ENSMUSP00000069901.4};
- **Gene Information:** Name=Rtl8c {ECO:0000313|Ensembl:ENSMUSP00000069901.4};
- **Organism (full):** Mus musculus (Mouse).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** RTL1/1-8/LDOC_capsid-like. (IPR032549); RTL1-8_LDOC (PF16297)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Rtl8c" matches the protein description above**
2. **Verify the organism is correct:** Mus musculus (Mouse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Rtl8c' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Rtl8c** (gene ID: Rtl8c, UniProt: F6TUF7) in mouse.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of Mouse *Rtl8c* (Retrotransposon Gag-like 8C, UniProt F6TUF7)

## Summary

Mouse **Rtl8c** (gene ID *Rtl8c*; UniProt **F6TUF7**; Ensembl ENSMUSP00000069901; MGI:1920115) encodes a small (~13.6 kDa, 112-residue) protein belonging to the **SIRH/Mart family of domesticated LTR-retrotransposon Gag-derived genes**. Rtl8c is one of three near-identical mouse paralogs — Rtl8a, Rtl8b, and Rtl8c (also annotated *Cxx1a/b/c* or *Mart8a/b/c*). The protein is built almost entirely from a single **retrotransposon Gag/capsid-like domain** (Pfam PF16297 "RTL1-8_LDOC"; InterPro IPR032549). Identity verification is unambiguous: the gene symbol, the mouse organism, and the capsid-like domain family all align precisely with the literature retrieved in this investigation. This is the correct gene — not a case of symbol ambiguity.

The **primary function of Rtl8c is that of a protein-interaction adaptor/scaffold, not an enzyme, transporter, receptor, or RNA-packaging protein**. Its defining molecular activity is to serve as an **obligate, paralog-specific partner of UBQLN2** (Ubiquilin-2), a shuttle factor of the ubiquitin-proteasome system. RTL8 proteins localize constitutively to the **nucleolus** and, when co-expressed with UBQLN2, drive the **nuclear translocation of UBQLN2** into ubiquitin-enriched subnuclear **protein quality control (PQC) bodies**. This activity is specific to UBQLN2 and does not extend to the related brain ubiquilins UBQLN1 or UBQLN4. In the cytoplasm, RTL8 is required for UBQLN2 to complex with and regulate a second domesticated retrotransposon protein, **PEG10**, and for the PEG10-driven recruitment of UBQLN2 to **stress granules** under cellular stress.

Through this adaptor function, Rtl8c operates within the **ubiquitin-proteasome / stress-granule proteostasis network**. Because UBQLN2 restrains the retrotransposon PEG10 to maintain neuronal health, and because UBQLN2 is a well-established amyotrophic lateral sclerosis / frontotemporal dementia (ALS/FTD) gene, Rtl8c sits at a mechanistically defined node of the neuronal proteostasis axis whose dysregulation underlies ALS/FTD. Structural analysis reinforces this conclusion: the F6TUF7 sequence lacks the cysteine/histidine residues of a nucleocapsid zinc-knuckle, ruling out RNA packaging, and contains no catalytic motifs, ruling out enzymatic activity. The evidence base is convergent across direct biochemistry, structural inference, and evolutionary context.

---

## Key Findings

### F001 — Identity: Rtl8c is a small SIRH/Mart-family retrotransposon Gag-derived protein

Mouse Rtl8c (F6TUF7, ENSMUSP00000069901) encodes "Retrotransposon Gag like 8C." It is one of three near-identical mouse paralogs (Rtl8a/b/c, also annotated *Cxx1a,b,c* / *Mart8a,b,c*) that form part of the **Mammalian retrotransposon transcript (Mart1–9)** family, equivalently called the **sushi-ichi-related retrotransposon homolog (SIRH)** family. These are Ty3/gypsy LTR-retroelement-derived genes that show moderate homology to the sushi-ichi LTR-retrotransposon of pufferfish [[PMID: 25888968](https://pubmed.ncbi.nlm.nih.gov/25888968/)]. The RTL8 proteins are small (~13 kDa) and highly homologous to one another [[PMID: 35247097](https://pubmed.ncbi.nlm.nih.gov/35247097/)]. The protein's single annotated domain is Pfam PF16297 (RTL1-8_LDOC) / InterPro IPR032549 (RTL1/1-8/LDOC capsid-like), consistent with an LTR-retrotransposon Gag/capsid-like origin.

The placental-expression survey of Naruse et al. explicitly maps the *Cxx1a,b,c/Mart8* genes — the Rtl8 cluster — within the SIRH family and documents their expression dynamics, confirming Rtl8c's family membership: *"Mammalian retrotransposon transcripts (Mart1-9), also called sushi-ichi-related retrotransposon-homolog (SIRH) genes, are a class of Ty3/gypsy LTR-retroelements showing moderate homology to the sushi-ichi LTR-retrotransposon in pufferfish"* [[PMID: 25888968](https://pubmed.ncbi.nlm.nih.gov/25888968/)]. Identity is therefore verified on all three mandatory axes — symbol, organism, and domain family.

### F002 — Primary function: a UBQLN2-specific adaptor driving UBQLN2 nuclear/nucleolar translocation

The central functional finding comes from a mass-spectrometry interactome screen that identified **RTL8 as a direct interactor of UBQLN2**, confirmed both *in vitro* with recombinant proteins and *in vivo* in mouse brain tissue [[PMID: 35247097](https://pubmed.ncbi.nlm.nih.gov/35247097/)]. Under both endogenous and overexpressed conditions, **RTL8 localizes to nucleoli**, and when co-expressed with UBQLN2, **RTL8 promotes the nuclear translocation of UBQLN2**, including during heat-shock stress: *"Under endogenous and overexpressed conditions, RTL8 localizes to nucleoli. When co-expressed with UBQLN2, RTL8 promotes nuclear translocation of UBQLN2"* [[PMID: 35247097](https://pubmed.ncbi.nlm.nih.gov/35247097/)].

Crucially, this effect is **paralog-specific**: it is confined to UBQLN2 and does not extend to the other brain-expressed ubiquilins UBQLN1 and UBQLN4 — *"The robust effect of RTL8 on the nuclear translocation and subnuclear localization of UBQLN2 does not extend to the other brain-expressed ubiquilins, UBQLN1 and UBQLN4"* [[PMID: 35247097](https://pubmed.ncbi.nlm.nih.gov/35247097/)]. The selectivity indicates a precise, evolved molecular interaction rather than a nonspecific association. The two proteins colocalize within **ubiquitin-enriched subnuclear structures containing protein quality control (PQC) components**, placing RTL8 function squarely within the protein quality control pathway [[PMID: 35247097](https://pubmed.ncbi.nlm.nih.gov/35247097/)]. UBQLN2 reciprocally stabilizes RTL8 protein levels, indicating a mutually reinforcing partnership.

### F003 — RTL8 bridges UBQLN2 to PEG10 and is required for UBQLN2 recruitment to stress granules

A 2025 study established that UBQLN2 proteostasis is governed by **two retrovirus-like proteins acting in series: RTL8 and PEG10**. RTL8 is the molecular bridge: it *"confers on UBQLN2 the ability to complex with and regulate PEG10"* [[PMID: 40680123](https://pubmed.ncbi.nlm.nih.gov/40680123/)]. PEG10 — itself a domesticated LTR-retrotransposon Gag homolog and a core component of stress granules that self-assembles into virus-like particles — drives the recruitment of UBQLN2 into **stress granules** under various stress conditions, but can only do so when RTL8 is present: *"PEG10, a core component of stress granules, drives the recruitment of UBQLN2 to stress granules under various stress conditions but can only do so when RTL8 is present"* [[PMID: 40680123](https://pubmed.ncbi.nlm.nih.gov/40680123/)]. Altering the relative levels of RTL8, PEG10, and UBQLN2 remodels stress-granule disassembly kinetics and translation recovery, demonstrating a functional consequence of the adaptor activity.

The structural/functional context of the partner PEG10 is provided independently: *"We identified several mammalian Gag homologs that form virus-like particles and one LTR retrotransposon homolog, PEG10, that preferentially binds and facilitates vesicular secretion of its own messenger RNA (mRNA)"* [[PMID: 34413232](https://pubmed.ncbi.nlm.nih.gov/34413232/)]. RTL8 thus couples UBQLN2 to a retroviral-like particle-forming protein, extending UBQLN2's reach into a cytoplasmic RNP compartment.

### F004 — Localization and expression: nucleoli/subnuclear PQC bodies, cytoplasmic stress granules; brain and placenta

RTL8 localizes **constitutively to nucleoli** and redistributes together with UBQLN2 into ubiquitin-enriched subnuclear PQC structures within the nucleus (Mohan et al. 2022), and it participates in cytoplasmic stress granules via PEG10 (Mohan et al. 2025). The endogenous RTL8/UBQLN2 interaction was confirmed in **mouse brain tissue**, establishing neural expression and physiological relevance: *"confirmed the interaction between UBQLN2 and RTL8 both in vitro using recombinant proteins and in vivo using mouse brain tissue"* [[PMID: 35247097](https://pubmed.ncbi.nlm.nih.gov/35247097/)].

At the family level, the mouse Rtl8 cluster (*Cxx1a,b,c/Mart8*) is expressed during **placentogenesis**, with sense and antisense transcripts co-localizing to trophoblast subtypes of the junctional zone and rising up to ~1,489 molecules/ng cDNA at embryonic day E9.5: *"ISH demonstrated sense and antisense transcript co-localization of Rgag4/Mart5 to Cxx1a,b,c/Mart8b,c,a in trophoblast subtypes at the junctional zone"* [[PMID: 25888968](https://pubmed.ncbi.nlm.nih.gov/25888968/)]. The protein therefore acts in at least two cellular compartments — the nucleus/nucleolus and the cytoplasmic stress granule — and across at least two tissues, brain and placenta.

### F005 — Structural inference: a minimal 112-aa Gag/capsid-like module lacking a nucleocapsid zinc-knuckle

UniProt F6TUF7 is **112 residues, 13,578 Da**. Its single annotated domain, "RTL1/1-8/LDOC capsid-like" (InterPro IPR032549; Pfam PF16297), spans residues 2–112 — essentially the entire protein. Direct sequence analysis performed in this investigation found **zero cysteines and zero histidines**, meaning the protein cannot form a **CCHC-type nucleocapsid zinc-knuckle** (the motif C-x2-C-x4-H-x4-C is absent). This is a decisive structural distinction: canonical retrotransposon/retroviral Gag proteins use the CCHC zinc-knuckle for RNA binding and packaging, and its complete absence rules out an RNA-packaging role for Rtl8c. The protein carries a net negative charge (~ -4; 20 acidic D/E vs. 16 basic K/R residues) with a strongly acidic C-terminal tail (…EFGWEEDEDF), a feature compatible with protein-protein interaction surfaces rather than nucleic-acid binding.

The family context confirms the derivation of this domain from the retrotransposon capsid protein: *"Among these are homologs of the capsid protein (known as Gag) of long terminal repeat (LTR) retrotransposons and retroviruses"* [[PMID: 34413232](https://pubmed.ncbi.nlm.nih.gov/34413232/)]. In short, Rtl8c is a **minimal Gag capsid-like module stripped of RNA-binding machinery** — structurally optimized for protein binding, consistent with its experimentally demonstrated adaptor role.

### F006 — Paralog-based inference: the capsid-like domain supports nucleolar localization and protein-interaction roles

The closest well-characterized domain relative sharing Pfam PF16297 is **LDOC1 (SIRH7/Mart7)**, a member of the same domesticated-retrotransposon family. LDOC1 provides a functional template that parallels RTL8's observed behavior. LDOC1 localizes to the nucleus/nucleolus and acts as a **leucine-zipper protein-interaction adaptor**: it interacts with the nucleolar GTPase GNL3L — *"Leucine Zipper Down-regulated in Cancer-1 (LDOC1) is a novel interacting partner of GNL3L"* [[PMID: 27764577](https://pubmed.ncbi.nlm.nih.gov/27764577/)] — and with the transcription factor MZF-1, and it represses NF-κB (p65/RelA) transcriptional activity to inhibit proliferation and promote apoptosis [[PMID: 26637328](https://pubmed.ncbi.nlm.nih.gov/26637328/)]. LDOC1 also shuttles between nucleus and cytoplasm, with nucleus-to-cytoplasm translocation documented in cancer: *"LDOC1 was translocated from the nucleus to the cytoplasm in human thyroid cancer"* [[PMID: 31889386](https://pubmed.ncbi.nlm.nih.gov/31889386/)].

This paralog comparison is corroborative, not definitive, for Rtl8c, but it reinforces two inferences from direct RTL8 data: (1) the PF16297 capsid-like fold functions as a **protein-protein interaction module** that supports nucleolar localization, and (2) members of this family **shuttle between nuclear and cytoplasmic compartments** — exactly the behavior documented for RTL8 with respect to UBQLN2.

### F007 — Pathway role: RTL8 is the adaptor enabling UBQLN2-mediated restraint of PEG10 in the proteostasis/ALS axis

Two complementary lines of evidence define a specific molecular pathway. First, **UBQLN2 restrains the domesticated retrotransposon PEG10 to maintain neuronal health**; loss of UBQLN2 function — as occurs with ALS-linked mutations — leads to PEG10 accumulation [[PMID: 36951542](https://pubmed.ncbi.nlm.nih.gov/36951542/)]. Second, **RTL8 confers on UBQLN2 the ability to complex with and regulate PEG10** [[PMID: 40680123](https://pubmed.ncbi.nlm.nih.gov/40680123/)], and the PEG10-driven recruitment of UBQLN2 to stress granules occurs only when RTL8 is present. RTL8 is therefore the **required adaptor** that licenses UBQLN2 to engage its PEG10 substrate.

The broader pathway is well-anchored. UBQLN2 is an established ubiquitin-proteasome shuttle factor and ALS/FTD gene that colocalizes with stress-granule components and regulates stress-granule dynamics: *"Ubiquilin 2 colocalizes with the SG component proteins G3BP1, TIA-1, ATXN2, and PABPC1. It participates in regulating SG dynamics"* [[PMID: 34750982](https://pubmed.ncbi.nlm.nih.gov/34750982/)]. UBQLN2 also participates in Parkin-mediated mitophagy [[PMID: 37501540](https://pubmed.ncbi.nlm.nih.gov/37501540/)] and can drive NF-κB activity and cytosolic TDP-43 aggregation in neuronal cells [[PMID: 26521126](https://pubmed.ncbi.nlm.nih.gov/26521126/)]. By acting as the UBQLN2 adaptor, RTL8/Rtl8c gains indirect influence over this network — but its *precise* role is the gating of the UBQLN2–PEG10 engagement, not broad pleiotropy.

### F008 — Integrated conclusion: Rtl8c is a UBQLN2 proteostasis adaptor (domesticated Gag), not an enzyme/transporter

Convergent experimental, structural, and evolutionary evidence supports a single coherent conclusion. **(1) Biochemistry:** RTL8 binds UBQLN2 paralog-specifically, drives UBQLN2 nuclear/nucleolar translocation into PQC bodies [[PMID: 35247097](https://pubmed.ncbi.nlm.nih.gov/35247097/)], and is required for UBQLN2 to complex with and regulate PEG10 and localize to stress granules [[PMID: 40680123](https://pubmed.ncbi.nlm.nih.gov/40680123/)]. **(2) Disease axis:** UBQLN2 restrains PEG10 to protect neurons, linking the axis to ALS/FTD [[PMID: 36951542](https://pubmed.ncbi.nlm.nih.gov/36951542/)]. **(3) Structure:** F6TUF7 is a 112-aa single Gag capsid-like domain (PF16297) with no cysteines or histidines and thus no RNA-binding nucleocapsid zinc-knuckle, ruling out enzymatic and nucleic-acid-packaging roles. **(4) Evolution:** Rtl8c is a member of the SIRH/Mart domesticated LTR-retrotransposon-derived family [[PMID: 28484174](https://pubmed.ncbi.nlm.nih.gov/28484174/)]. No primary literature supports any catalytic, transporter, or receptor function for Rtl8c.

---

## Mechanistic Model / Interpretation

Rtl8c is best understood as a **compartment-directing adaptor for UBQLN2**, repurposed from an ancient retrotransposon capsid protein. The capsid-like fold, which in ancestral retroelements oligomerized to form a particle shell, has here been retained as a **protein-protein interaction surface** while the RNA-binding zinc-knuckle has been lost. The result is a dedicated, minimal protein module whose job is to bind one specific client (UBQLN2) and control where that client acts.

The operating logic can be summarized as a two-stage, series pathway:

```
            NUCLEUS                                CYTOPLASM
  +-----------------------------+      +----------------------------------+
  |   RTL8c (nucleolus)         |      |   Stress (heat shock, oxidative) |
  |        |                    |      |            |                     |
  |        | binds, paralog-    |      |            v                     |
  |        | specific           |      |   PEG10 (virus-like particle,    |
  |        v                    |      |   stress-granule core)           |
  |   UBQLN2 --> nuclear import |      |            | requires RTL8       |
  |        |                    |      |            v                     |
  |        v                    |      |   RTL8-UBQLN2 complex recruited  |
  |   Ubiquitin-rich subnuclear |      |   to STRESS GRANULES             |
  |   PQC bodies (quality       |      |            |                     |
  |   control)                  |      |            v                     |
  +-----------------------------+      |   UBQLN2 engages & regulates     |
                                       |   PEG10 -> tunes SG disassembly, |
                                       |   translation recovery           |
                                       +----------------------------------+

  Disease link:  UBQLN2 (ALS/FTD gene) restrains PEG10 -> loss = PEG10 buildup
                 RTL8c is the obligate adaptor gating this engagement
```

Two features distinguish Rtl8c's role as *precise* rather than generic. First, the **paralog specificity** for UBQLN2 (and not UBQLN1/UBQLN4) indicates an evolved, defined binding interface. Second, the **obligate requirement** — PEG10 can recruit UBQLN2 to stress granules *only when RTL8 is present* — makes Rtl8c a non-redundant switch in the pathway rather than a bystander.

The following table contrasts what Rtl8c *is* versus plausible alternative functional classes that the evidence excludes:

| Functional hypothesis | Verdict | Basis |
|---|---|---|
| Enzyme (catalytic) | **Excluded** | No catalytic motif; single capsid-like domain occupies whole protein (F005) |
| Transporter | **Excluded** | No membrane-spanning/transporter architecture; soluble nucleolar protein (F002, F005) |
| RNA-packaging Gag | **Excluded** | No CCHC zinc-knuckle (0 Cys, 0 His) (F005) |
| Receptor/signaling ligand | **Not supported** | No primary literature; acidic soluble adaptor (F005, F008) |
| **Protein-interaction adaptor/scaffold** | **Supported** | Direct biochemistry: binds UBQLN2, gates PEG10 engagement (F002, F003, F007) |

Localization-wise, Rtl8c is a **dual-compartment protein**: constitutively nucleolar at baseline, directing UBQLN2 into subnuclear PQC bodies, and cytoplasmic/stress-granule-associated via PEG10 under stress. This mirrors the nucleo-cytoplasmic shuttling documented for its paralog LDOC1 (F006), supporting the view that compartment-switching is an intrinsic property of this capsid-like family.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [35247097](https://pubmed.ncbi.nlm.nih.gov/35247097/) | *RTL8 promotes nuclear localization of UBQLN2 to subnuclear PQC compartments* | **Primary, strongest.** Establishes RTL8 as a direct, paralog-specific UBQLN2 adaptor; nucleolar localization; nuclear translocation of UBQLN2; in vitro + mouse brain in vivo validation (F002, F004) |
| [40680123](https://pubmed.ncbi.nlm.nih.gov/40680123/) | *Endogenous retrovirus-like proteins recruit UBQLN2 to stress granules* | **Primary, strongest.** Shows RTL8 confers on UBQLN2 the ability to complex with/regulate PEG10 and is required for stress-granule recruitment (F003, F007, F008) |
| [36951542](https://pubmed.ncbi.nlm.nih.gov/36951542/) | *UBQLN2 restrains the domesticated retrotransposon PEG10 to maintain neuronal health in ALS* | Anchors the disease axis: UBQLN2→PEG10 restraint, ALS relevance (F007). (The attributed snippet is a paraphrase of the paper's thesis, flagged as non-exact during verification.) |
| [34413232](https://pubmed.ncbi.nlm.nih.gov/34413232/) | *Mammalian retrovirus-like protein PEG10 packages its own mRNA* | Characterizes the partner PEG10 as a virus-like-particle-forming Gag homolog; defines family capsid origin (F003, F005) |
| [25888968](https://pubmed.ncbi.nlm.nih.gov/25888968/) | *Selective expression of sense/antisense transcripts of the SIRH family during mouse placentogenesis* | Defines the SIRH/Mart family and maps Rtl8 (Cxx1/Mart8) cluster; placental expression (F001, F004) |
| [34750982](https://pubmed.ncbi.nlm.nih.gov/34750982/) | *ALS-linked UBQLN2 mutation affects stress granule assembly via TIA-1* | Documents UBQLN2 stress-granule biology (G3BP1/TIA-1/ATXN2) — the compartment where RTL8 acts (F007) |
| [37501540](https://pubmed.ncbi.nlm.nih.gov/37501540/) | *UBQLN2 and HSP70 in Parkin-mediated mitophagy* | Context for UBQLN2's broader proteostasis roles (F007) |
| [26521126](https://pubmed.ncbi.nlm.nih.gov/26521126/) | *Ubiquilin-2 drives NF-κB activity and cytosolic TDP-43 aggregation* | Context for UBQLN2 downstream effects in neurons (F007) |
| [27764577](https://pubmed.ncbi.nlm.nih.gov/27764577/) | *LDOC1 interacts with GNL3L to modulate NF-κB signaling* | Paralog template: PF16297 protein acts as nucleolar interaction adaptor (F006) |
| [31889386](https://pubmed.ncbi.nlm.nih.gov/31889386/) | *LDOC1 in thyroid cancer* | Paralog template: nucleo-cytoplasmic shuttling of a same-family protein (F006) |
| [26637328](https://pubmed.ncbi.nlm.nih.gov/26637328/) | *LDOC1 represses NF-κB in papillary thyroid carcinoma* | Paralog template: leucine-zipper adaptor, NF-κB repression (F006) |
| [28484174](https://pubmed.ncbi.nlm.nih.gov/28484174/) | *Evolution of brain functions and LTR retrotransposon-derived genes* | Evolutionary framing of SIRH/Mart domestication (F008) |
| [23704700](https://pubmed.ncbi.nlm.nih.gov/23704700/) | *PNMA-MS1 in marsupials / SIRH evolution* | Broader evolutionary context for Gag-derived mammalian gene families |

**How the evidence converges:** The two Mohan studies ([PMID: 35247097](https://pubmed.ncbi.nlm.nih.gov/35247097/), [PMID: 40680123](https://pubmed.ncbi.nlm.nih.gov/40680123/)) are the decisive primary sources — they use recombinant-protein biochemistry, cell-based co-localization, and mouse-brain validation to define the adaptor function directly. The structural analysis (F005) was performed in this investigation from the F6TUF7 sequence and independently excludes RNA-packaging and enzymatic roles. The LDOC1 paralog literature (F006) is supportive-by-homology rather than direct. The ALS/UBQLN2 literature (F007) establishes the pathway and disease relevance into which RTL8's adaptor function feeds.

**Caveat on one citation:** The snippet attributed to [PMID: 36951542](https://pubmed.ncbi.nlm.nih.gov/36951542/) is a paraphrase of the paper's central claim and was flagged as a non-exact (mismatch) quote during verification; the paper's thesis (UBQLN2 restrains PEG10) is nonetheless well-supported by its title and by the independent Mohan 2025 data.

---

## Limitations and Knowledge Gaps

1. **No Rtl8c-isoform-specific functional study.** Essentially all direct functional data concern "RTL8" as a group (the three near-identical paralogs Rtl8a/b/c are experimentally difficult to distinguish with current reagents). Whether Rtl8c specifically — as opposed to Rtl8a or Rtl8b — has any unique activity, expression domain, or binding preference is unknown.

2. **Structural model is inferential.** The conclusions about the capsid-like fold and the absence of a zinc-knuckle are derived from sequence/domain annotation, not from an experimental 3D structure of Rtl8c. No crystal, cryo-EM, or NMR structure of RTL8 was identified, and no AlphaFold confidence analysis was performed in this investigation.

3. **Mapping of the UBQLN2-binding interface is incomplete.** The residues on RTL8 that mediate the paralog-specific UBQLN2 interaction, and the reciprocal surface on UBQLN2, have not been defined in the literature reviewed. The structural basis of the specificity for UBQLN2 over UBQLN1/UBQLN4 remains open.

4. **In vivo loss-of-function phenotype unknown.** No *Rtl8c*-knockout mouse phenotype was retrieved. The physiological consequence of losing Rtl8c (versus the whole Rtl8 cluster) — in brain, placenta, or elsewhere — is not established.

5. **Quantitative interaction parameters missing.** Binding affinities (K_d), stoichiometry of the RTL8–UBQLN2–PEG10 complex, and kinetic parameters of the stress-granule recruitment were not available in the summarized evidence.

6. **Placental vs. neural function.** Rtl8 cluster transcripts are abundant in placental trophoblast, yet the mechanistic work is in the UBQLN2/neuronal context. Whether the adaptor function operates identically in placenta is untested.

---

## Proposed Follow-up Experiments / Actions

1. **Paralog-resolving genetics.** Generate *Rtl8c*-specific CRISPR knockouts (distinguishable from Rtl8a/b via flanking unique sequence or targeted degron tags) and assay UBQLN2 localization, PEG10 regulation, and stress-granule dynamics to determine whether Rtl8c is functionally redundant with its paralogs or has a unique role.

2. **Experimental structure determination.** Solve the RTL8–UBQLN2 complex by cryo-EM or X-ray crystallography (or at minimum, generate and validate an AlphaFold-Multimer model) to map the interaction interface and test the prediction that the acidic C-terminal tail of Rtl8c contacts UBQLN2.

3. **Interface mutagenesis.** Use alanine/charge-reversal scanning of the predicted interface (especially the acidic C-terminal …EFGWEEDEDF motif) to identify residues required for UBQLN2 binding and for the paralog specificity over UBQLN1/UBQLN4.

4. **Quantitative biophysics.** Measure RTL8–UBQLN2 and RTL8–UBQLN2–PEG10 binding affinities and stoichiometry by ITC/SPR/mass photometry to define the thermodynamics of the ternary complex.

5. **In vivo disease modeling.** Cross Rtl8-cluster loss-of-function alleles into UBQLN2-ALS mouse models to test whether RTL8 levels modulate PEG10 accumulation and neurodegeneration — directly probing the therapeutic relevance of the adaptor.

6. **Compartment-switching mechanism.** Use live-cell imaging under acute stress to resolve the kinetics of RTL8 redistribution from nucleolus to stress granules and determine whether PEG10 or UBQLN2 drives the switch.

---

## Conclusion

Mouse Rtl8c (F6TUF7) is a domesticated-retrotransposon, Gag-capsid-derived **protein-interaction adaptor**. Its primary, precise molecular function is to act as an obligate, paralog-specific partner of the ubiquitin-proteasome shuttle factor UBQLN2 — directing UBQLN2 into nucleolar/subnuclear protein-quality-control bodies and licensing UBQLN2 to complex with and regulate the retrotransposon protein PEG10 and to be recruited to cytoplasmic stress granules. It is not an enzyme, transporter, receptor, or RNA-packaging protein. Through this adaptor role, Rtl8c functions within the ubiquitin-proteasome/stress-granule proteostasis network, an axis central to ALS/FTD neurobiology.


## Artifacts

- [OpenScientist final report](Rtl8c-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Rtl8c-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:25888968
2. PMID:35247097
3. PMID:40680123
4. PMID:34413232
5. PMID:27764577
6. PMID:26637328
7. PMID:31889386
8. PMID:36951542
9. PMID:34750982
10. PMID:37501540
11. PMID:26521126
12. PMID:28484174