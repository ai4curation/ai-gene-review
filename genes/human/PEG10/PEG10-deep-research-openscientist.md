---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T13:13:33.675626'
end_time: '2026-10-24T13:35:26.894019'
duration_seconds: 1313.22
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: PEG10
  gene_symbol: PEG10
  uniprot_accession: Q86TG7
  protein_description: 'RecName: Full=Retrotransposon-derived protein PEG10 {ECO:0000305};
    AltName: Full=Embryonal carcinoma differentiation-regulated protein {ECO:0000250|UniProtKB:Q7TN75};
    AltName: Full=Mammalian retrotransposon-derived protein 2 {ECO:0000250|UniProtKB:Q7TN75};
    AltName: Full=Myelin expression factor 3-like protein 1 {ECO:0000303|Ref.2}; Short=MEF3-like
    protein 1 {ECO:0000303|Ref.2}; AltName: Full=Paternally expressed gene 10 protein
    {ECO:0000303|PubMed:11318613}; AltName: Full=Retrotransposon gag domain-containing
    protein 3; AltName: Full=Retrotransposon-derived gag-like polyprotein {ECO:0000303|PubMed:15611116};
    AltName: Full=Ty3/Gypsy-like protein {ECO:0000250|UniProtKB:Q7TN75};'
  gene_info: Name=PEG10 {ECO:0000303|PubMed:11318613, ECO:0000312|HGNC:HGNC:14005};
    Synonyms=EDR {ECO:0000250|UniProtKB:Q7TN75}, KIAA1051e {ECO:0000303|PubMed:10231032},
    MAR2, MART2 {ECO:0000250|UniProtKB:Q7TN75}, MEF3L1 {ECO:0000303|Ref.2}, RGAG3;
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: DNA/RNA_pol_sf. (IPR043502); PEG10-RTL1_C-capsid. (IPR063300);
    Peptidase_aspartic_dom_sf. (IPR021109); PRO_PEG10-RTL1. (IPR063610); Rev_trsase/Diguanyl_cyclase.
    (IPR043128)
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
citation_count: 20
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PEG10-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PEG10-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q86TG7
- **Protein Description:** RecName: Full=Retrotransposon-derived protein PEG10 {ECO:0000305}; AltName: Full=Embryonal carcinoma differentiation-regulated protein {ECO:0000250|UniProtKB:Q7TN75}; AltName: Full=Mammalian retrotransposon-derived protein 2 {ECO:0000250|UniProtKB:Q7TN75}; AltName: Full=Myelin expression factor 3-like protein 1 {ECO:0000303|Ref.2}; Short=MEF3-like protein 1 {ECO:0000303|Ref.2}; AltName: Full=Paternally expressed gene 10 protein {ECO:0000303|PubMed:11318613}; AltName: Full=Retrotransposon gag domain-containing protein 3; AltName: Full=Retrotransposon-derived gag-like polyprotein {ECO:0000303|PubMed:15611116}; AltName: Full=Ty3/Gypsy-like protein {ECO:0000250|UniProtKB:Q7TN75};
- **Gene Information:** Name=PEG10 {ECO:0000303|PubMed:11318613, ECO:0000312|HGNC:HGNC:14005}; Synonyms=EDR {ECO:0000250|UniProtKB:Q7TN75}, KIAA1051e {ECO:0000303|PubMed:10231032}, MAR2, MART2 {ECO:0000250|UniProtKB:Q7TN75}, MEF3L1 {ECO:0000303|Ref.2}, RGAG3;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** DNA/RNA_pol_sf. (IPR043502); PEG10-RTL1_C-capsid. (IPR063300); Peptidase_aspartic_dom_sf. (IPR021109); PRO_PEG10-RTL1. (IPR063610); Rev_trsase/Diguanyl_cyclase. (IPR043128)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PEG10" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PEG10' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PEG10** (gene ID: PEG10, UniProt: Q86TG7) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# PEG10 (Q86TG7): A Domesticated Retroviral Gag/Protease That Packages RNA, Signals Between Cells, and Builds the Placenta

## Summary

**PEG10** (Paternally Expressed Gene 10; UniProt **Q86TG7**; human chromosome **7q21**) is a protein-coding gene that originated by **domestication of a Ty3/gypsy LTR retrotransposon**. Its primary molecular function is that of a **retroviral Gag-like capsid protein**: it self-assembles into capsid-like **virus-like particles (VLPs)** that selectively bind and package RNA — preferentially its own mRNA and U/G-rich transcripts — and can bud from membranes into secreted particles that transfer mRNA cargo between cells. Through a **programmed −1 ribosomal frameshift** at a conserved slippery site/pseudoknot, PEG10 produces both a short **GAG (RF1)** product and a longer **GAG-POL (RF1/2)** fusion that carries a functional **viral aspartic protease** (DSG/DTG motif). This architecture — Gag capsid + Pol-like protease, generated by frameshifting — directly mirrors that of retroviruses and retrotransposons and has been confirmed at the structural level by X-ray crystallography.

Beyond its structural/RNA-packaging role, PEG10 acts as a **signaling adaptor and anti-apoptotic factor**. The GAG-like product PEG10-RF1 directly **binds and inhibits TGF-β-superfamily type I/II receptors** (ALK1/ACVRL1 and ALK5), and PEG10 physically associates with and antagonizes the **pro-apoptotic ubiquitin ligase SIAH1**, thereby suppressing cell death and promoting proliferation. It functions mainly in the **cytoplasm** (budding at membranes) and **extracellularly** (via secreted VLPs).

Physiologically, PEG10 is **essential and non-redundant for placentation**: knockout mice die at ~E10.5 from placental failure, and its viral protease activity is specifically required to maintain fetal placental capillary structure. Its oncofetal reactivation drives multiple cancers — most notably **hepatocellular carcinoma (HCC)**, where it stabilizes **GLUT1** and **HK2** mRNAs by blocking the Staufen1-mediated decay pathway to fuel aerobic glycolysis — and its escape from **UBQLN2** proteostatic control in neurons perturbs mRNA splicing in a **TDP-43-like** manner, implicating it in ALS and related neurodegeneration. This report synthesizes 11 confirmed findings from 35 reviewed papers into a coherent mechanistic model of PEG10 as a domesticated Gag/protease RNA-packaging and intercellular-signaling protein.

**Gene identity confirmation:** The symbol PEG10 (HGNC:14005; synonyms EDR, MART2/MAR2, MEF3L1, RGAG3, KIAA1051e, SIRH1), the organism *Homo sapiens*, and the InterPro capsid/protease/reverse-transcriptase domains (IPR063300 PEG10-RTL1_C-capsid; IPR021109 Peptidase_aspartic_dom_sf; IPR063610 PRO_PEG10-RTL1) all align precisely with the literature synthesized here. There is no gene-symbol ambiguity.

---

## Key Findings

### Finding 1 — PEG10 is a Ty3/gypsy retrotransposon-derived, paternally imprinted gene essential for placentation

PEG10 is a paternally expressed (monoallelic) imprinted gene located within the **PEG10/SGCE imprinted cluster** at human chromosome 7q21, regulated by a germline differentially methylated region (gDMR). It is **conserved across therian mammals** (both eutherians and marsupials) and derives from a **Ty3/gypsy LTR retrotransposon**, retaining GAG- and POL-like domains. Its essential developmental role is established by direct genetic evidence: *Peg10* knockout mice show **early embryonic lethality at ~E10.5 owing to severe placental defects** ([PMID: 16341224](https://pubmed.ncbi.nlm.nih.gov/16341224/)), a result independently corroborated in later work ([PMID: 34559199](https://pubmed.ncbi.nlm.nih.gov/34559199/)). The same foundational study characterized PEG10 as one of the "actively transcribed Ty3/gypsy retrotransposon-derived genes with highly conserved DNA sequences and insertion sites," firmly establishing both its evolutionary origin and the deep conservation that signals functional domestication.

This finding anchors the entire investigation: PEG10 is not a parasitic mobile element but a **co-opted single-copy cellular gene** whose retroviral ancestry is the key to its biochemistry.

### Finding 2 — PEG10 is a Gag-like RNA-binding protein that self-assembles into virus-like particles and packages its own mRNA

PEG10's N-terminal **GAG/capsid domain** promotes vesicle budding in a manner analogous to the HIV p24 Gag protein: "the Gag domain of PEG10 can promote vesicle budding similar to the HIV p24 Gag protein" ([PMID: 30951545](https://pubmed.ncbi.nlm.nih.gov/30951545/)). Functionally, PEG10 **preferentially binds and facilitates vesicular secretion of its own mRNA** ([PMID: 34413232](https://pubmed.ncbi.nlm.nih.gov/34413232/)) and assembles into **virus-like particles (VLPs) that can be purified by iodixanol ultracentrifugation** ([PMID: 39775359](https://pubmed.ncbi.nlm.nih.gov/39775359/)). Its RNA binding is sequence-selective: PEG10 "has selectivity for binding **U/G-rich RNAs**" ([PMID: 42239172](https://pubmed.ncbi.nlm.nih.gov/42239172/)). In trophoblast stem cells, PEG10 also binds cellular transcripts (including *Hbegf*) and stabilizes mRNAs required for differentiation.

Together these data define the **primary molecular function**: PEG10 is a self-assembling, RNA-packaging **structural (capsid) protein** with sequence-selective RNA-binding activity.

### Finding 3 — PEG10's POL-like viral aspartic protease is required for placental vascular maintenance and self-processing

PEG10 is translated as **GAG and GAG-POL** forms via a −1 ribosomal frameshift, and the POL-like region contains a conserved **viral aspartic protease (DSG/DTG) motif**. Knock-in mice carrying a point mutation in this motif survive early placentation but show **perinatal lethality with fetal/placental growth retardation and severe fetal capillary (endothelial) defects**; PEG10 is expressed in the "three trophoblast cell layers that surround fetal capillary endothelial cells" ([PMID: 34559199](https://pubmed.ncbi.nlm.nih.gov/34559199/)). The protease is also central to PEG10's own biology: PEG10 "undergoes a complex self-processing pathway that results in gene expression changes when the protein accumulates in cells" ([PMID: 36951542](https://pubmed.ncbi.nlm.nih.gov/36951542/)).

This finding dissociates two developmental requirements — the **Gag/capsid** function (needed for early placentation) and the **protease** function (needed later for fetal vasculature) — demonstrating that both retroviral-derived modules are physiologically active.

### Finding 4 — PEG10 is an oncoprotein, notably in HCC, acting by stabilizing target mRNAs

PEG10 is overexpressed in HCC and associated with poor prognosis; liver-specific *Peg10* deletion impedes hepatocarcinogenesis in mice. Mechanistically, "as an RNA-binding protein (RBP), PEG10 inhibited the **Staufen1-mediated mRNA decay (SMD) pathway, stabilizing GLUT1 and HK2 mRNA** to enhance glucose uptake and aerobic glycolysis" ([PMID: 42826094](https://pubmed.ncbi.nlm.nih.gov/42826094/)). This directly links PEG10's RNA-binding capsid function to a metabolic (Warburg-effect) oncogenic program. PEG10 protein abundance is tightly controlled: the E3 ligases SIAH1/SIAH2 "bound to the PAIR domain of PEG10 and promoted its polyubiquitination via K48/63-linked chains" ([PMID: 42168988](https://pubmed.ncbi.nlm.nih.gov/42168988/)), while USP9X deubiquitinates and stabilizes PEG10 ([PMID: 30951545](https://pubmed.ncbi.nlm.nih.gov/30951545/)). Transcriptionally, "CTR9 promoted the oncogene paternally expressed gene 10 (PEG10) transcription via its promoter region" ([PMID: 34876700](https://pubmed.ncbi.nlm.nih.gov/34876700/)).

### Finding 5 — In neurons, PEG10 is restrained by UBQLN2 and drives TDP-43-like splicing dysregulation

The proteasome shuttle factor **UBQLN2** restrains PEG10 to maintain neuronal health; ALS-linked UBQLN2 mutations permit PEG10 accumulation ([PMID: 36951542](https://pubmed.ncbi.nlm.nih.gov/36951542/)). Excess PEG10 is functionally pathogenic: "PEG10 overexpression mimics the **loss of TDP-43** in broad changes to gene expression, including **dysregulation of mRNA splicing pathways**," with PEG10 binding U/G-rich RNAs ([PMID: 42239172](https://pubmed.ncbi.nlm.nih.gov/42239172/)). PEG10 "has been implicated in neurological disease" ([PMID: 39775359](https://pubmed.ncbi.nlm.nih.gov/39775359/)), and the related Gag-like gene **RTL8 antagonizes PEG10 VLP formation**, suggesting a built-in counter-regulatory mechanism.

### Finding 6 — PEG10 (SIRH1) has a GAG-then-GAG-POL architecture generated by programmed −1 ribosomal frameshifting

PEG10 is the founding member (**SIRH1**) of the **sushi-ichi-related retrotransposon homolog (SIRH)** family of LTR-retrotransposon-domesticated genes that emerged with viviparous mammals. These genes "encode proteins that are homologous to a retrotransposon Gag capsid protein and sometimes also have a Pol-like region," and "PEG10 is conserved in both the marsupials and the eutherians" ([PMID: 22866050](https://pubmed.ncbi.nlm.nih.gov/22866050/)). Like retroviruses, PEG10 produces a short ORF1 (GAG) and, via a conserved **GGGAAAC slippery site plus downstream RNA pseudoknot**, a **programmed −1 ribosomal frameshift (−1 PRF)** yielding the GAG-POL fusion containing the aspartic protease. This −1 PRF element is a defined, conserved translational-recoding mechanism "through RNA structural elements, most notably stimulatory pseudoknots" and can be selectively modulated by structure-guided antisense oligonucleotides ([PMID: 42818233](https://pubmed.ncbi.nlm.nih.gov/42818233/)).

### Finding 7 — PEG10 functions extracellularly via secreted VLPs that transfer mRNA; dysregulation disrupts TGF-β signaling in preeclampsia

PEG10 acts not only intracellularly but **extracellularly**. In the placenta, "PEG10 forms virus-like particles, which are **transferred from the trophoblast to the closely proximate endothelial cells**," and "excessive PEG10 disrupts maternal vascular development by **inhibiting TGF-β signaling**" in preeclampsia ([PMID: 38715110](https://pubmed.ncbi.nlm.nih.gov/38715110/)). The programmable nature of the cargo — "the mRNA cargo of PEG10 can be reprogrammed by flanking genes of interest with [PEG10 UTRs]" ([PMID: 34413232](https://pubmed.ncbi.nlm.nih.gov/34413232/)) — underpins the engineered **SEND** mRNA-delivery platform, and PEG10 eVLPs have been engineered to package neoantigen mRNA/peptides for cancer vaccines ([PMID: 39269893](https://pubmed.ncbi.nlm.nih.gov/39269893/)).

This finding establishes PEG10 as a genuine **intercellular communication device** whose physiological output converges on the TGF-β pathway.

### Finding 8 — PEG10 is an anti-apoptotic, proliferation-promoting protein that antagonizes SIAH1

The first functional characterization identified PEG10 as highly expressed in the majority of HCCs but absent in normal liver; "PEG10 protein associated with **SIAH1, a mediator of apoptosis**, and overexpression of PEG10 decreased the cell death mediated by SIAH1," while "exogenous expression of PEG10 conferred oncogenic activity and transfection of hepatoma cells with antisense S-oligonucleotides suppressing PEG10 resulted in their growth inhibition" ([PMID: 12810624](https://pubmed.ncbi.nlm.nih.gov/12810624/)). Reciprocally, "SIAH1 also reduces the amount of PEG10 protein, which is known to be frequently overexpressed in HCC and to promote cell proliferation" ([PMID: 17273732](https://pubmed.ncbi.nlm.nih.gov/17273732/)). PEG10-RF1 is thus an **inhibitor of apoptosis that mediates cell proliferation** ([PMID: 20084274](https://pubmed.ncbi.nlm.nih.gov/20084274/)).

### Finding 9 — Gene organization, two frameshift isoforms, cytoplasmic localization, and broad oncofetal overexpression

PEG10 maps to the **7q21 imprinted locus** (adjacent to *SGCE*) and encodes at least two proteins: **PEG10-RF1 (GAG-like)** and **PEG10-RF1/2 (GAG-POL)**, produced "by −1 frameshift translation," with "translation initiated at a **non-AUG start codon** upstream of the previously predicted AUG codon as well as at the AUG codon" ([PMID: 20084274](https://pubmed.ncbi.nlm.nih.gov/20084274/)). PEG10 is a **cytoplasmic** protein that buds from membranes to form secreted VLPs ([PMID: 30951545](https://pubmed.ncbi.nlm.nih.gov/30951545/)). Its oncofetal reactivation extends beyond HCC: in high-risk B-cell chronic lymphocytic leukemia, "expression levels in CD19+ B-CLL cells were **100-fold higher** than in B-cells from healthy donors," where it is prognostic and long-term knockdown induces apoptosis ([PMID: 17621626](https://pubmed.ncbi.nlm.nih.gov/17621626/)).

### Finding 10 — X-ray crystallography confirms PEG10 adopts a retroviral capsid (CA) fold

Direct structural evidence validates the Gag classification: "X-ray crystal structures of stably folded domains of MOAP1 ... and PEG10 ... are **highly similar to the C-terminal capsid (CA) domains of cognate Gag proteins**," and these structures "suggest that these proteins may have **preserved some of the key interactions that facilitated assembly of their ancestral Gags into capsids**" ([PMID: 34357660](https://pubmed.ncbi.nlm.nih.gov/34357660/)). This provides structural (not merely sequence-based) support for the InterPro **PEG10-RTL1_C-capsid** domain (IPR063300) listed in the UniProt annotation.

### Finding 11 — PEG10-RF1 directly binds and inhibits TGF-β superfamily type I/II receptors (ALK1, ALK5)

In a yeast two-hybrid screen for binding partners of **ALK1** (a TGF-β type I receptor; ACVRL1), **PEG10-RF1 was identified as an ALK1-binding protein**. "PEG10-RF1 also interacts with different members of TGF-β superfamily type I and II receptors. PEG10-RF1 binding to ALK1 is mediated by a **200-amino-acid domain with no recognized motif**. PEG10-RF1 **inhibits ALK1 as well as ALK5 signaling**" ([PMID: 15611116](https://pubmed.ncbi.nlm.nih.gov/15611116/)). PEG10 was identified as "an ALK1-binding protein encoded by an ancient retroviral/retrotransposon element integrated as a single copy gene known as PEG10 on human chromosome 7q21," with broad expression "in ... human placenta, brain, kidney, endothelial cells, lymphoblasts." This provides the **molecular mechanism** connecting PEG10 to the TGF-β pathway modulation observed physiologically in preeclampsia (Finding 7).

---

## Mechanistic Model / Interpretation

PEG10 is best understood as a **domesticated retrovirus-in-miniature** whose ancestral Gag/Pol biochemistry has been repurposed for mammalian physiology. The findings cohere into the following integrated model:

```
                 PEG10 mRNA (7q21, paternally expressed, imprinted)
                          │
        non-AUG / AUG start ──────────────────┐
                          │ translation         │
                 ┌────────┴─────────┐           │
                 │  GGGAAAC slippery │           │
                 │  site + pseudoknot│  −1 PRF   │
                 ▼                   ▼           ▼
            GAG (RF1)          GAG-POL (RF1/2)
          capsid protein     capsid + ASPARTIC PROTEASE (DSG/DTG)
                 │                   │
                 │                   └─► self-processing / autoproteolysis
                 │                        └─► maintains fetal capillary structure
                 ▼
     ┌───────────────────────────────────────────────┐
     │  CAPSID SELF-ASSEMBLY (retroviral CA fold)      │  ◄── X-ray confirmed
     │  + sequence-selective RNA binding (U/G-rich,    │
     │    own mRNA)                                     │
     └───────────────┬─────────────────────┬───────────┘
                     │                     │
        buds at membrane →           intracellular RBP activity
        SECRETED VLPs                      │
          │                                ├─► blocks Staufen1-mediated decay
          │ transfer mRNA                  │    → stabilizes GLUT1 / HK2 mRNA
          ▼ between cells                  │    → aerobic glycolysis (HCC)
   trophoblast → endothelium              └─► regulates mRNA splicing
          │                                    (TDP-43-like when in excess → ALS)
          ▼
   PROTEIN-PROTEIN SIGNALING:
     • binds + inhibits ALK1/ALK5 (TGF-β receptors) → TGF-β pathway control
     • binds + antagonizes SIAH1 → anti-apoptotic, pro-proliferative

   REGULATION of PEG10 abundance:
     • SIAH1/SIAH2 → K48/K63 polyubiquitination (PAIR domain) → degradation
     • USP9X → deubiquitination → stabilization
     • UBQLN2 → proteasomal restraint (neurons)
     • RTL8 → antagonizes VLP assembly
     • CTR9 → transcriptional activation
```

**Three functional modules operate in parallel:**

1. **Structural / RNA-packaging module (primary molecular function).** The Gag-derived capsid domain adopts a bona fide retroviral CA fold (Finding 10), self-assembles into VLPs (Findings 2, 9), and binds RNA with U/G-rich selectivity, preferentially its own mRNA (Finding 2). This makes PEG10 a **cytoplasmic/membrane-associated RNA-binding structural protein** that can bud into **secreted, mRNA-carrying particles** (Finding 7).

2. **Enzymatic module.** The −1 frameshift produces a GAG-POL fusion carrying a functional **aspartic protease** (Findings 3, 6) that mediates self-processing and is specifically required for fetal placental vasculature (Finding 3).

3. **Signaling/adaptor module.** PEG10-RF1 directly binds and inhibits **TGF-β receptors ALK1/ALK5** (Finding 11) and antagonizes the pro-apoptotic ligase **SIAH1** (Finding 8). These protein–protein interactions explain both its physiological role in vascular remodeling (TGF-β) and its anti-apoptotic/oncogenic activity.

**Localization.** PEG10 carries out its functions principally in the **cytoplasm** (RNA binding, budding at membranes, SIAH1/receptor interactions) and **extracellularly**, via secreted VLPs that deliver mRNA to neighboring cells (Findings 7, 9).

**Physiology vs. pathology.** The same machinery that builds the placenta (intercellular mRNA transfer + TGF-β tuning + anti-apoptosis) becomes pathogenic when dysregulated: **too much PEG10** disrupts maternal spiral-artery remodeling (preeclampsia), drives oncofetal cancers (HCC glycolysis via GLUT1/HK2 stabilization; B-CLL), and — when it escapes UBQLN2 control in neurons — produces TDP-43-like splicing collapse (ALS). This explains why PEG10 abundance is policed by a dedicated network (SIAH1/2, USP9X, UBQLN2, RTL8).

### Summary table of PEG10 functional modules

| Module | Domain / isoform | Molecular activity | Evidence type | Key PMIDs |
|---|---|---|---|---|
| Capsid / RNA packaging | GAG (RF1) | Self-assembly into VLPs; U/G-rich & self-mRNA binding; membrane budding | Experimental + X-ray structure | 30951545, 34413232, 39775359, 42239172, 34357660 |
| Protease | GAG-POL (RF1/2), DSG/DTG | Aspartic protease; self-processing; fetal capillary maintenance | Knock-in mouse; biochemistry | 34559199, 36951542, 22866050 |
| TGF-β signaling adaptor | RF1, ~200-aa domain | Binds/inhibits ALK1 & ALK5; disrupts vascular remodeling | Y2H + functional assays; in vivo | 15611116, 38715110 |
| Anti-apoptotic adaptor | RF1 (PAIR domain) | Binds/antagonizes SIAH1; promotes proliferation | Co-IP; overexpression/knockdown | 12810624, 17273732, 20084274 |
| Translational control | mRNA (slippery site + pseudoknot) | Programmed −1 frameshift; non-AUG + AUG initiation | Reporter/structure studies | 22866050, 20084274, 42818233 |

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [16341224](https://pubmed.ncbi.nlm.nih.gov/16341224/) | *Deletion of Peg10 causes early embryonic lethality* | Genetic proof PEG10 is essential for placenta; Ty3/gypsy origin |
| [34559199](https://pubmed.ncbi.nlm.nih.gov/34559199/) | *PEG10 viral aspartic protease domain essential for fetal capillary structure* | Protease motif required for placental vasculature; trophoblast localization |
| [30951545](https://pubmed.ncbi.nlm.nih.gov/30951545/) | *Gag protein PEG10 binds RNA and regulates trophoblast stem cells* | Gag-domain budding like HIV p24; RNA binding; USP9X stabilization |
| [34413232](https://pubmed.ncbi.nlm.nih.gov/34413232/) | *PEG10 packages its own mRNA; pseudotyped for delivery* | Selective self-mRNA packaging; programmable cargo (SEND) |
| [39775359](https://pubmed.ncbi.nlm.nih.gov/39775359/) | *RTL8 antagonizes PEG10 VLPs* | VLP purification; neurological disease link; RTL8 counter-regulation |
| [42239172](https://pubmed.ncbi.nlm.nih.gov/42239172/) | *PEG10 is a regulator of mRNA splicing in neurons* | U/G-rich RNA selectivity; TDP-43-like splicing dysregulation |
| [22866050](https://pubmed.ncbi.nlm.nih.gov/22866050/) | *Genes domesticated from LTR retrotransposons (review)* | SIRH1/family architecture; GAG+POL; therian conservation |
| [42818233](https://pubmed.ncbi.nlm.nih.gov/42818233/) | *Structure-guided ASOs modulate frameshifting* | −1 PRF/pseudoknot mechanism; therapeutic modulation |
| [38715110](https://pubmed.ncbi.nlm.nih.gov/38715110/) | *Disruption of maternal vascular remodeling in preeclampsia (Nature)* | VLP transfer trophoblast→endothelium; TGF-β inhibition in vivo |
| [15611116](https://pubmed.ncbi.nlm.nih.gov/15611116/) | *Gag/Gag-Pol-like proteins interact with ALK1* | Direct binding/inhibition of ALK1 & ALK5 (TGF-β receptors) |
| [12810624](https://pubmed.ncbi.nlm.nih.gov/12810624/) | *PEG10 in HCC through interaction with SIAH1* | First functional study; anti-apoptotic, oncogenic; SIAH1 binding |
| [17273732](https://pubmed.ncbi.nlm.nih.gov/17273732/) | *SIAH1 causes growth arrest/apoptosis in hepatoma* | PEG10 is a SIAH1 degradation target; pro-proliferative |
| [20084274](https://pubmed.ncbi.nlm.nih.gov/20084274/) | *Genetic/molecular analyses of PEG10* | Two frameshift isoforms; non-AUG initiation; 7q21 locus |
| [17621626](https://pubmed.ncbi.nlm.nih.gov/17621626/) | *PEG10 overexpression in high-risk B-CLL* | ~100-fold reactivation beyond HCC; prognostic; apoptosis on knockdown |
| [34357660](https://pubmed.ncbi.nlm.nih.gov/34357660/) | *Structural evidence MOAP1/PEG10 derived from Gag* | X-ray CA fold; preserved capsid-assembly surfaces |
| [42826094](https://pubmed.ncbi.nlm.nih.gov/42826094/) | *PEG10 inhibits mRNA decay to promote glucose metabolism in HCC* | Staufen1-mediated decay block; GLUT1/HK2 stabilization |
| [42168988](https://pubmed.ncbi.nlm.nih.gov/42168988/) | *Polyubiquitination of PEG10 by SIAH1/2 in HCC* | PAIR-domain K48/K63 ubiquitination controls PEG10 abundance |
| [34876700](https://pubmed.ncbi.nlm.nih.gov/34876700/) | *CTR9 promotes HCC via PEG10 transcription* | Transcriptional driver of PEG10 oncogenesis |
| [36951542](https://pubmed.ncbi.nlm.nih.gov/36951542/) | *UBQLN2 restrains PEG10 in ALS* | Proteostatic control; self-processing; neurodegeneration link |
| [39269893](https://pubmed.ncbi.nlm.nih.gov/39269893/) | *Engineering PEG10 eVLPs for cancer vaccination* | Applied proof of self-assembly/cargo-loading |

**Convergence of evidence types.** The PEG10 model rests on an unusually strong, multi-modal evidence base: **genetics** (knockout and protease knock-in mice; Findings 1, 3), **structural biology** (X-ray capsid fold; Finding 10), **biochemistry** (RNA-binding selectivity, VLP purification, frameshifting assays; Findings 2, 6), **interaction studies** (Y2H and co-IP for ALK1/ALK5 and SIAH1; Findings 8, 11), and **in vivo physiology/pathology** (preeclampsia, HCC, ALS; Findings 4, 5, 7). These independent lines agree, giving high confidence in the core mechanistic model.

---

## Limitations and Knowledge Gaps

- **Precise in vivo RNA cargo spectrum is incomplete.** While self-mRNA preference and U/G-rich selectivity are established ([PMID: 34413232](https://pubmed.ncbi.nlm.nih.gov/34413232/), [PMID: 42239172](https://pubmed.ncbi.nlm.nih.gov/42239172/)), the full endogenous set of transcripts packaged and transferred by physiological PEG10 VLPs — and how this changes between placenta, neurons, and tumors — is not fully mapped.
- **Protease substrate specificity is largely undefined.** The aspartic protease is required for placental vasculature and self-processing ([PMID: 34559199](https://pubmed.ncbi.nlm.nih.gov/34559199/), [PMID: 36951542](https://pubmed.ncbi.nlm.nih.gov/36951542/)), but the exact cleavage sites, kinetic parameters, and whether it has *trans* (non-self) cellular substrates remain open.
- **Mechanism of TGF-β receptor inhibition.** PEG10-RF1 binds/inhibits ALK1 and ALK5 via a ~200-aa domain with "no recognized motif" ([PMID: 15611116](https://pubmed.ncbi.nlm.nih.gov/15611116/)); the structural basis and whether inhibition is competitive, allosteric, or trafficking-based is unknown.
- **Isoform-specific functions.** The division of labor between PEG10-RF1 (GAG) and RF1/2 (GAG-POL), and the regulation of the −1 frameshift ratio in different tissues, is not quantitatively resolved in vivo.
- **Human-specific vs. mouse data.** Several mechanistic experiments (protease knock-in, UBQLN2 restraint) rely on mouse models; human-specific validation is partial.
- **Causality in neurodegeneration.** The TDP-43-like effect is compelling ([PMID: 42239172](https://pubmed.ncbi.nlm.nih.gov/42239172/)), but a direct causal demonstration that PEG10 accumulation initiates (rather than accompanies) human ALS pathology is still developing.
- **No new primary data generated here.** This report is a literature/annotation synthesis; findings reflect the cited studies' own designs, sample sizes, and caveats.

---

## Proposed Follow-up Experiments / Actions

1. **Comprehensive VLP cargo mapping.** Perform CLIP-seq and VLP-RNA-seq on PEG10 particles purified from trophoblast, neuronal, and HCC cells to define the physiological, context-specific RNA cargo and test the U/G-rich/self-mRNA selectivity quantitatively.
2. **Protease substrate profiling.** Use N-terminomics/mass spectrometry with protease-dead (DSG/DTG mutant) controls to identify PEG10 autoproteolytic and potential *trans* substrates; determine cleavage consensus and kinetics.
3. **Structural characterization of the TGF-β interaction.** Solve a cryo-EM/X-ray structure of PEG10-RF1 bound to ALK1/ALK5 ectodomains or kinase domains to define the inhibitory interface and enable mechanism-based inhibitors.
4. **Quantify frameshift ratios in vivo.** Use targeted proteomics or frameshift reporters knocked into the endogenous locus to measure the GAG:GAG-POL ratio across placenta, brain, and tumor, and test whether structure-guided ASOs ([PMID: 42818233](https://pubmed.ncbi.nlm.nih.gov/42818233/)) can therapeutically tune it.
5. **Targeting PEG10 in HCC.** Validate the Staufen1–GLUT1/HK2 axis ([PMID: 42826094](https://pubmed.ncbi.nlm.nih.gov/42826094/)) as a metabolic vulnerability; test whether blocking PEG10 VLP assembly (e.g., via RTL8 mimetics; [PMID: 39775359](https://pubmed.ncbi.nlm.nih.gov/39775359/)) suppresses glycolysis and tumor growth.
6. **Proteostatic rescue in neurons.** Test whether enhancing UBQLN2 function or SIAH-mediated degradation lowers neuronal PEG10 and reverses TDP-43-like splicing defects in patient-derived models ([PMID: 36951542](https://pubmed.ncbi.nlm.nih.gov/36951542/), [PMID: 42239172](https://pubmed.ncbi.nlm.nih.gov/42239172/)).
7. **Preeclampsia biomarker/therapeutic.** Evaluate circulating PEG10 VLPs as a preeclampsia biomarker and test whether restoring TGF-β signaling counteracts PEG10-driven vascular defects ([PMID: 38715110](https://pubmed.ncbi.nlm.nih.gov/38715110/)).

---

## Conclusion

PEG10 (Q86TG7) is a **domesticated Ty3/gypsy retrotransposon-derived gene** whose primary molecular function is to act as a **retroviral Gag-like capsid protein that self-assembles into RNA-packaging virus-like particles** and, through programmed −1 frameshifting, additionally produces a **Gag-Pol form bearing a functional aspartic protease**. Operating in the **cytoplasm and extracellularly**, it transfers mRNA between cells, directly **inhibits TGF-β receptors ALK1/ALK5**, and **antagonizes the pro-apoptotic ligase SIAH1**. These activities make it essential and non-redundant for **placentation and placental-vascular maintenance**, while its dysregulation drives **oncofetal cancers** (notably HCC, via GLUT1/HK2 mRNA stabilization) and **neurodegeneration** (ALS/TDP-43-like splicing collapse when it escapes UBQLN2 control). The gene identity — symbol PEG10, human organism, and InterPro capsid/protease/reverse-transcriptase domains — is unambiguously confirmed by the literature synthesized here.


## Artifacts

- [OpenScientist final report](PEG10-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PEG10-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:16341224
2. PMID:34559199
3. PMID:30951545
4. PMID:34413232
5. PMID:39775359
6. PMID:42239172
7. PMID:36951542
8. PMID:42826094
9. PMID:42168988
10. PMID:34876700
11. PMID:22866050
12. PMID:42818233
13. PMID:38715110
14. PMID:39269893
15. PMID:12810624
16. PMID:17273732
17. PMID:20084274
18. PMID:17621626
19. PMID:34357660
20. PMID:15611116