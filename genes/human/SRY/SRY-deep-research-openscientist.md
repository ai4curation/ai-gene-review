---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T04:14:57.461324'
end_time: '2026-10-24T04:32:20.549992'
duration_seconds: 1043.09
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: SRY
  gene_symbol: SRY
  uniprot_accession: Q05066
  protein_description: 'RecName: Full=Sex-determining region Y protein {ECO:0000303|PubMed:1695712};
    AltName: Full=Testis-determining factor {ECO:0000303|PubMed:12970737, ECO:0000303|PubMed:1695712,
    ECO:0000303|PubMed:2247149};'
  gene_info: Name=SRY {ECO:0000303|PubMed:1695712, ECO:0000312|HGNC:HGNC:11311}; Synonyms=TDF
    {ECO:0000303|PubMed:12970737, ECO:0000303|PubMed:1695712, ECO:0000303|PubMed:2247149};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the SRY family. .
  protein_domains: HMG_box_dom. (IPR009071); HMG_box_dom_sf. (IPR036910); SRY. (IPR017253);
    SRY-related_HMG-box_TF-like. (IPR050140); HMG_box (PF00505)
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
citation_count: 29
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: SRY-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: SRY-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q05066
- **Protein Description:** RecName: Full=Sex-determining region Y protein {ECO:0000303|PubMed:1695712}; AltName: Full=Testis-determining factor {ECO:0000303|PubMed:12970737, ECO:0000303|PubMed:1695712, ECO:0000303|PubMed:2247149};
- **Gene Information:** Name=SRY {ECO:0000303|PubMed:1695712, ECO:0000312|HGNC:HGNC:11311}; Synonyms=TDF {ECO:0000303|PubMed:12970737, ECO:0000303|PubMed:1695712, ECO:0000303|PubMed:2247149};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the SRY family. .
- **Key Domains:** HMG_box_dom. (IPR009071); HMG_box_dom_sf. (IPR036910); SRY. (IPR017253); SRY-related_HMG-box_TF-like. (IPR050140); HMG_box (PF00505)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SRY" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SRY' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SRY** (gene ID: SRY, UniProt: Q05066) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# SRY (Q05066): The Y-Encoded DNA-Bending Master Switch of Testis Determination

*Comprehensive functional annotation report — Homo sapiens Sex-determining region Y protein / Testis-determining factor (TDF)*

## Gene/Protein Identity Verification

- **UniProt:** Q05066 — Sex-determining region Y protein (Testis-determining factor, TDF)
- **Gene:** SRY (synonym TDF); **Organism:** *Homo sapiens* (Human)
- **Family / domains:** SRY family; single HMG box (PF00505; IPR009071, IPR036910, IPR017253, IPR050140)
- **Verification outcome:** The gene symbol, organism, protein family, and HMG-box domain architecture all align precisely with the testis-determining function documented in the literature. **There is no gene-symbol ambiguity** — this is the canonical human sex-determining gene, and the literature below pertains unambiguously to this protein.

---

## Summary

**SRY (Q05066) is the master testis-determining factor of therian mammals — a Y-chromosome–encoded, single-domain architectural transcription factor whose primary biochemical activity is sequence-specific DNA binding in the minor groove and sharp DNA bending.** Through its single high-mobility-group (HMG) box, SRY binds target DNA, bends it by roughly 54° (quantified at atomic resolution by NMR), and thereby reorganizes chromatin/enhancer architecture rather than acting as a classical acidic trans-activator. Acting transiently in the nucleus of pre-Sertoli cells within the bipotential (indifferent) gonad, SRY flips the genetic switch that commits the gonad to testicular rather than ovarian fate. It is both **necessary** — loss-of-function HMG-box mutations cause 46,XY complete gonadal dysgenesis (Swyer syndrome) — and **sufficient** — the *Sry* gene alone induces testis formation in chromosomally XX mice and humans.

Mechanistically, SRY operates as a **dual-action switch**. Together with the nuclear receptor NR5A1/SF1, it directly binds and activates the testis-specific enhancer (Enh13/TESCO) of the autosomal gene **SOX9**, and it independently binds and activates the **FGF9** promoter. SOX9 and FGF9 then form a self-reinforcing feed-forward loop that establishes and maintains the testis program long after SRY itself has switched off. Simultaneously, SRY functions as a sequence-specific **repressor** of the ovarian program by recruiting the KRAB-O adaptor and the KAP1 (TRIM28) silencing machinery to target promoters such as the ovarian determinant RSPO1. This bistable, ON-testis/OFF-ovary logic antagonizes the opposing WNT4/RSPO1/β-catenin/FOXL2 ovarian pathway.

SRY's function is tightly gated at the level of **subcellular localization and dosage**. Its HMG box is flanked by two nuclear localization signals (a β-NLS imported by importin-β1 and a calmodulin-dependent CaM-NLS), and SRY additionally undergoes regulated nucleocytoplasmic shuttling (via Exportin-4 and CRM1). These controls define a narrow ~2-fold transcriptional threshold: human testis determination is a "tenuous" switch in which modest reductions in SRY nuclear accumulation, DNA bend angle, or expression dosage tip development toward the female phenotype. SRY thus exemplifies how a single architectural protein, acting at the right place, time, and level, can direct an entire organ-fate decision.

---

## Key Findings

### Finding 1 — SRY is the master testis-determining factor

SRY is the primary genetic switch that initiates male sex determination in mammals. Within the pre-Sertoli cells of the bipotential gonad, SRY commits the organ to the testicular fate rather than the default ovarian fate. The genetic evidence is classical and unambiguous: individuals with 46,XY karyotypes who carry inactivating SRY mutations develop as phenotypic females (Swyer syndrome / 46,XY complete gonadal dysgenesis), whereas the presence or translocation of SRY drives testis formation. As stated directly in the literature, "During gonadal development, Sry in pre-Sertoli cells activates Sox9 gene transcription, committing the fate of the bipotential gonad to become a testis rather than an ovary" ([PMID: 21558314](https://pubmed.ncbi.nlm.nih.gov/21558314/)), and "Human testis determination is initiated by SRY, a Y-encoded architectural transcription factor" ([PMID: 25258310](https://pubmed.ncbi.nlm.nih.gov/25258310/)).

This finding establishes the identity verification required by the research brief: the gene symbol SRY, the organism (*Homo sapiens*), the HMG-box/SRY family domain architecture, and the testis-determining function all align precisely.

### Finding 2 — SRY is an HMG-box architectural transcription factor that binds the DNA minor groove and bends DNA

The **primary molecular function** of SRY is sequence-specific DNA binding and bending through its single high-mobility-group (HMG) box. Rather than activating transcription through an acidic activation domain, SRY acts as an **architectural ("bending") transcription factor**: it inserts into the DNA minor groove and introduces a sharp bend, remodeling local DNA/chromatin geometry to enable assembly of transcriptional complexes. The HMG box "mediates sequence-specific DNA binding with sharp DNA bending" ([PMID: 36568077](https://pubmed.ncbi.nlm.nih.gov/36568077/)).

The clinical genetics corroborates the centrality of this activity: sex-reversal mutations "cluster in the SRY high mobility group (HMG) box, a conserved motif of specific DNA binding and bending" ([PMID: 25258310](https://pubmed.ncbi.nlm.nih.gov/25258310/)). Electrophoretic mobility shift assays (EMSAs) of patient-derived mutations (e.g., W70L, M64I, K92M, A118P) demonstrate reduced or abolished DNA binding, with K92M showing reduced binding and A118P showing greatly reduced binding ([PMID: 18304538](https://pubmed.ncbi.nlm.nih.gov/18304538/)). A conserved aromatic "buttress" of residues underlies the DNA-bending surface of the box ([PMID: 25258310](https://pubmed.ncbi.nlm.nih.gov/25258310/)).

### Finding 3 — SRY activates SOX9 via a testis-specific enhancer, cooperating with NR5A1/SF1

The key downstream target of SRY is the autosomal gene **SOX9**. SRY, acting together with the nuclear receptor **NR5A1 (SF1)**, binds a testis-specific enhancer upstream of SOX9 — the TES/TESCO element, whose core is the highly conserved **Enh13** — in XY pre-Sertoli cells, upregulating SOX9 transcription and inducing testicular differentiation. "SRY and NR5A1 ... proteins regulate transcription of the autosomal SOX9/Sox9 ... gene in XY embryonic gonads, inducing testicular differentiation" ([PMID: 40467489](https://pubmed.ncbi.nlm.nih.gov/40467489/)), and "the binding of SRY to the highly conserved enhancer Enh13 is thought to be a common mechanism underlying testis differentiation and sex determination in mammals" ([PMID: 38246151](https://pubmed.ncbi.nlm.nih.gov/38246151/)).

Functional perturbation confirms direction and necessity: CRISPR-mediated SRY mutation in pre-implantation embryos "increased the expression of female lineage-specific gene Wnt4 whereas decreased the expression of male specific gene SOX9 in blastocysts" ([PMID: 39498956](https://pubmed.ncbi.nlm.nih.gov/39498956/)). Once induced, SOX9 maintains its own expression through a feed-forward loop and drives Sertoli-cell differentiation.

### Finding 4 — SRY functions in the nucleus; dual nuclear import uses importin-β and calmodulin

SRY carries out its function in the **nucleus** of pre-Sertoli cells, where it accesses target DNA. Its HMG box is flanked by **two nuclear localization signals (NLSs)**: a C-terminal **β-NLS**, imported by importin-β1 (Impβ1) in a Ran-dependent manner, and an N-terminal **CaM-NLS**, mediated by the calcium-binding protein calmodulin (CaM) in a Ran-independent manner. "The sex-determining region on the Y chromosome (SRY) has 2 nuclear localization signals (NLSs) that flank the DNA binding high mobility group (HMG) domain; the β-NLS and the CaM-NLS, which mediate nuclear transport through importin β1 (Impβ1) and the calcium-binding protein calmodulin (CaM), respectively" ([PMID: 21051653](https://pubmed.ncbi.nlm.nih.gov/21051653/)). Intracellular Ca²⁺ acts as a switch between these two mutually exclusive import pathways.

That nuclear import is **physiologically required** — not merely incidental — is shown pharmacologically: a CaM antagonist applied to cultured XY mouse fetal gonads "led to reduced expression of the Sry target gene Sox9, defects in testicular cord formation, and ectopic expression of the ovarian markers Rspondin1 and forkhead box L2" ([PMID: 21558314](https://pubmed.ncbi.nlm.nih.gov/21558314/)). Sex-reversal mutations in either NLS reduce nuclear import and can cause XY sex reversal even when DNA binding is intact ([PMID: 20528776](https://pubmed.ncbi.nlm.nih.gov/20528776/), [PMID: 15746192](https://pubmed.ncbi.nlm.nih.gov/15746192/)).

### Finding 5 — SRY evolved from SOX3 and sits in a regulated cascade (KDM6B upstream, SOX9 downstream)

SRY is a member of the SOX / SRY-related HMG-box family and **arose evolutionarily from the X/autosomal gene SOX3**. It is the top-level regulator of the testis-development cascade: "we investigated the eutherian Sry gene, a top-level regulator of testis development that originated from Sox3" ([PMID: 41138755](https://pubmed.ncbi.nlm.nih.gov/41138755/)). Notably, its HMG box evolves under unusually relaxed purifying selection among eutherians — a "tolerated functional decline" — compared with typical genes.

SRY is itself a **regulated node**. Its timely activation requires chromatin de-repression by the H3K27me3 demethylase **KDM6B**: "loss of Kdm6b leads to a delay in Sry activation and the development of an ovotestis. These results implicate KDM6B as a conserved regulator at the top of the sex determination cascade" ([PMID: 40406982](https://pubmed.ncbi.nlm.nih.gov/40406982/)). Thus SRY is both the recipient of upstream chromatin-level regulation and the trigger of the downstream SRY→SOX9→FGF9/AMH program.

### Finding 6 — NMR structure quantifies minor-groove binding and a ~54° DNA bend

High-resolution NMR of the human SRY HMG box (residues 57–140) bound to a 14-mer DNA directly visualizes the mechanism: the box "binds DNA sequence-specifically in the minor groove, resulting in substantial DNA bending" ([PMID: 11563911](https://pubmed.ncbi.nlm.nih.gov/11563911/)). The average bend angle, derived from an ensemble of 400 simulated-annealing structures, is **54 ± 2°**, achieved by partial intercalation of hydrophobic side chains (e.g., Ile13 of the box) with additional steric and hydrogen-bond contacts (Met9/Arg17).

Crucially, the structure links **bend geometry to clinical phenotype**. For the sex-reversal mutation M64I (M9I in the box numbering), the average bend angle "is reduced by approximately 13 degrees from 54(+/-2) degrees in the wild-type complex to 41(+/-2) degrees in the M9I complex" ([PMID: 11563911](https://pubmed.ncbi.nlm.nih.gov/11563911/)), by altering roll/tilt at an ApA step. (Note: a later study argued that in the full-length protein the basic tail restores sharp bending and that M64I sex reversal is actually driven by a flanking non-classical NLS defect — [PMID: 16762365](https://pubmed.ncbi.nlm.nih.gov/16762365/) — underscoring that both bend geometry and nuclear localization are functionally coupled.)

### Finding 7 — SRY activity requires nucleocytoplasmic shuttling and a C-terminal PDZ partner; a 2-fold transcriptional threshold

Beyond import, SRY undergoes **regulated nucleocytoplasmic shuttling**, and this fine control defines a sharp dosage threshold. Inherited HMG-box variants V60L and I90M selectively impair nuclear import (via Exportin-4) or export (via CRM1), respectively, without altering DNA binding/bending. "Decreased shuttling limits nuclear accumulation of phosphorylated (activated) SRY, in turn reducing occupancy of DNA sites regulating Sertoli-cell differentiation [the testis-specific SRY-box 9 (Sox9) enhancer]" ([PMID: 24003159](https://pubmed.ncbi.nlm.nih.gov/24003159/)). Both variants attenuate SOX9 by roughly 2-fold, defining a male transcriptional threshold: "This shared twofold threshold is reminiscent of autosomal syndromes of transcription-factor haploinsufficiency" ([PMID: 24003159](https://pubmed.ncbi.nlm.nih.gov/24003159/)).

Because SRY lacks a classical activation domain, it may recruit trans-activation capacity through protein partners. Its C-terminus engages a PDZ-domain nuclear factor (SIP-1): "Interacting domains were mapped to the C-terminal seven amino acids of SRY and to the PDZ domains of SIP-1" ([PMID: 9054412](https://pubmed.ncbi.nlm.nih.gov/9054412/)). Additional co-regulators, such as the nucleocytoplasmic protein NHERF2, have also been reported to act as SRY co-regulators in the nucleus ([PMID: 39813852](https://pubmed.ncbi.nlm.nih.gov/39813852/)).

### Finding 8 — SRY is *sufficient* to initiate testis determination (transgenic gain-of-function)

Loss-of-function evidence (HMG-box mutations → gonadal dysgenesis) establishes necessity; gain-of-function evidence establishes **sufficiency**. "The sex-determining region of Chr Y (Sry) gene is sufficient to induce testis formation and the subsequent male development of internal and external genitalia in chromosomally female mice and humans" ([PMID: 17185318](https://pubmed.ncbi.nlm.nih.gov/17185318/)). XX mice carrying an *Sry* transgene (and XX human males carrying translocated SRY) develop as males.

SRY must act within a **brief developmental window** in the bipotential genital ridge and must reach a **critical expression threshold**. It is a dosage-sensitive downstream target of a CITED2/WT1/SF1 module: "Cited2 acts in the gonad with Wt1 and Sf1 to increase the expression of Sry levels to attain a critical threshold to efficiently initiate testis development" ([PMID: 19457926](https://pubmed.ncbi.nlm.nih.gov/19457926/)). Reduced dosage produces partial XY sex reversal, consistent with the 2-fold threshold of Finding 7.

### Finding 9 — SRY directly activates FGF9 in addition to SOX9, seeding the FGF9–SOX9 feed-forward loop

SRY has (at least) **two direct transcriptional targets**. Beyond SOX9, ChIP/promoter-mapping shows SRY binds and activates the **FGF9** promoter: "human and mouse SRY bind to -833 to -821 of human FGF9 and -1010 to -998 of mouse Fgf9, respectively, and control FGF9/Fgf9 mRNA expression" ([PMID: 32886743](https://pubmed.ncbi.nlm.nih.gov/32886743/)). Interestingly, mouse SRY cooperates with SF1 at Fgf9 whereas human SRY activates FGF9 independently of SF1. FGF9 expression alone is sufficient to switch XX fetal gonads toward male fate ex vivo.

Once initiated, FGF9 and SOX9 establish a mutually reinforcing loop: "expression of the Y-linked gene Sry shifts the bipotential gonad toward a testicular fate by upregulating a feed-forward loop between FGF9 and SOX9 to establish SOX9 expression in somatic cells" ([PMID: 18617533](https://pubmed.ncbi.nlm.nih.gov/18617533/)). This loop is what allows the testis program to persist after SRY itself switches off. The opposing WNT4/RSPO1/β-catenin signal promotes ovarian fate, and "activation of beta-catenin in otherwise normal XY mice effectively disrupts the male program and results in male-to-female sex-reversal" ([PMID: 18617533](https://pubmed.ncbi.nlm.nih.gov/18617533/)).

### Finding 10 — SRY is a dual activator/repressor: it recruits the KRAB-O–KAP1 silencing machinery to repress ovarian genes

SRY does not only switch testis genes ON — it also switches ovary genes OFF. It functions as a **sequence-specific transcriptional repressor** by recruiting the KRAB-only adaptor protein **KRAB-O**, which bridges to the **KAP1 (TRIM28) co-repressor machinery** (KAP1–NuRD–SETDB1–HP1). "Transcriptional repression by SRY requires binding to KRAB-O, thus bridging to the KAP1 repression machinery. This repression machinery is recruited to SRY target promoters in chromatin templates via SRY" ([PMID: 19850934](https://pubmed.ncbi.nlm.nih.gov/19850934/)). A proposed repressed target is the ovarian determinant RSPO1: SRY "may function by repressing the ovarian determinant gene, RSPO1, action in the ovarian developmental pathway and activates genes, such as SOX9, important for testis differentiation" ([PMID: 19850934](https://pubmed.ncbi.nlm.nih.gov/19850934/)).

Genetic evidence supports a "general repressor model." In the *Odsex* mouse, a deletion ~1 Mb upstream of *Sox9* causes dominant XX sex reversal, consistent with SRY normally antagonizing a repressor of *Sox9*: these data are "consistent with Sox9 being a direct downstream target of Sry and provide genetic evidence to support a general repressor model of sex determination in mammals" ([PMID: 11101852](https://pubmed.ncbi.nlm.nih.gov/11101852/)). SRY also acts antagonistically to the anti-testis gene DAX1/NR0B1 ([PMID: 11301600](https://pubmed.ncbi.nlm.nih.gov/11301600/)).

---

## Mechanistic Model / Interpretation

SRY is best understood as a **time-limited, dosage-gated architectural switch** that converts a transient Y-chromosome signal into a self-sustaining, bistable organ-fate decision. The logic can be summarized as follows:

```
          UPSTREAM (chromatin de-repression / dosage)
          ─────────────────────────────────────────────
             KDM6B (H3K27me3 demethylase)
             CITED2 + WT1 + SF1  ──► raise SRY to threshold
                               │
                               ▼
   ┌───────────────────────────────────────────────────────┐
   │   SRY protein  (pre-Sertoli cell nucleus, E~10.5–11.5) │
   │                                                        │
   │   Import:  β-NLS ──importin-β1──┐                       │
   │            CaM-NLS ──calmodulin─┤  (Ca²⁺ switches)      │
   │   Shuttle: Exportin-4 (in) / CRM1 (out) → phospho-SRY  │
   │                                                        │
   │   Core activity: HMG box binds MINOR GROOVE,           │
   │                  BENDS DNA ~54°                         │
   └───────────────────────────────────────────────────────┘
             │                                   │
      ACTIVATE (with SF1)                    REPRESS (via KRAB-O/KAP1)
             ▼                                   ▼
   ┌──────────────────────┐             ┌──────────────────────┐
   │  SOX9 (Enh13/TESCO)  │             │  RSPO1 / ovarian      │
   │  FGF9 (promoter)     │             │  program; antagonize  │
   └──────────────────────┘             │  DAX1                 │
             │                           └──────────────────────┘
             ▼
   ┌──────────────────────────────┐
   │  FGF9 ⇄ SOX9 feed-forward loop│  ← self-sustaining; persists
   │  → Sertoli differentiation   │     after SRY switches OFF
   │  → AMH, testis cords          │
   └──────────────────────────────┘

   ANTAGONIST (female pathway): WNT4 / RSPO1 / β-catenin / FOXL2
   (β-catenin stabilization in XY → male-to-female reversal)
```

**Why "architectural"?** SRY's single HMG box does not supply an acidic activation surface; its job is to *reshape DNA*. By bending the SOX9 enhancer (Enh13/TESCO) and the FGF9 promoter, SRY — in cooperation with SF1 — juxtaposes regulatory elements and nucleates transcriptional assembly. The NMR-measured 54° bend and the ~13° bend loss in the M64I mutant directly tie this geometry to function. Any insult that reduces the effective bend, the amount of nuclear SRY, or its DNA occupancy pushes the system below the ~2-fold threshold and toward the female default.

**Why bistable?** SRY acts only briefly, but its outputs are self-locking. SOX9 maintains itself through its own enhancer and through the FGF9↔SOX9 feed-forward loop, so the testis program becomes independent of SRY. Simultaneously, SRY's KRAB-O/KAP1-mediated repression and its antagonism of DAX1 and the WNT4/RSPO1/β-catenin pathway remove the opposing ovarian attractor. The combination of positive feed-forward activation and active repression of the alternative fate is what produces a sharp, committed, irreversible switch.

### Functional annotation at a glance

| Attribute | Annotation | Key evidence |
|---|---|---|
| **Primary molecular function** | Sequence-specific DNA binding + DNA bending (architectural TF) | [PMID: 36568077](https://pubmed.ncbi.nlm.nih.gov/36568077/), [PMID: 11563911](https://pubmed.ncbi.nlm.nih.gov/11563911/) |
| **DNA-binding mode** | Single HMG box, minor groove, ~54° bend | [PMID: 11563911](https://pubmed.ncbi.nlm.nih.gov/11563911/) |
| **Subcellular localization** | Nucleus (pre-Sertoli cells); dual NLS + shuttling | [PMID: 21051653](https://pubmed.ncbi.nlm.nih.gov/21051653/), [PMID: 24003159](https://pubmed.ncbi.nlm.nih.gov/24003159/) |
| **Direct activation targets** | SOX9 (Enh13/TESCO, with SF1); FGF9 promoter | [PMID: 40467489](https://pubmed.ncbi.nlm.nih.gov/40467489/), [PMID: 38246151](https://pubmed.ncbi.nlm.nih.gov/38246151/), [PMID: 32886743](https://pubmed.ncbi.nlm.nih.gov/32886743/) |
| **Repression targets** | RSPO1 / ovarian program (via KRAB-O/KAP1); antagonizes DAX1 | [PMID: 19850934](https://pubmed.ncbi.nlm.nih.gov/19850934/), [PMID: 11301600](https://pubmed.ncbi.nlm.nih.gov/11301600/) |
| **Pathway position** | Top of cascade: (KDM6B/CITED2/WT1/SF1) → SRY → SOX9/FGF9 ⊣ WNT4/β-catenin | [PMID: 41138755](https://pubmed.ncbi.nlm.nih.gov/41138755/), [PMID: 18617533](https://pubmed.ncbi.nlm.nih.gov/18617533/) |
| **Necessity** | HMG-box mutations → 46,XY gonadal dysgenesis (Swyer) | [PMID: 25258310](https://pubmed.ncbi.nlm.nih.gov/25258310/), [PMID: 18304538](https://pubmed.ncbi.nlm.nih.gov/18304538/) |
| **Sufficiency** | *Sry* transgene → testis in XX mice/humans | [PMID: 17185318](https://pubmed.ncbi.nlm.nih.gov/17185318/) |
| **Dosage** | ~2-fold transcriptional threshold; dosage-sensitive | [PMID: 24003159](https://pubmed.ncbi.nlm.nih.gov/24003159/), [PMID: 19457926](https://pubmed.ncbi.nlm.nih.gov/19457926/) |
| **Evolutionary origin** | Derived from SOX3; relaxed selection on HMG box | [PMID: 41138755](https://pubmed.ncbi.nlm.nih.gov/41138755/) |

---

## Evidence Base

The findings rest on a convergent, multi-method evidence base: **structural biology** (NMR of the SRY HMG box–DNA complex), **clinical genetics** (sex-reversal mutations), **mouse/model genetics** (transgenics, CRISPR, gonad culture), and **biochemistry** (EMSA, ChIP, co-IP, yeast two-hybrid).

| Paper (PMID) | Type of evidence | How it supports the findings |
|---|---|---|
| [PMID: 11563911](https://pubmed.ncbi.nlm.nih.gov/11563911/) | NMR structure | Quantifies minor-groove binding and 54±2° bend; M64I reduces bend to 41±2° — ties geometry to function (F2, F6) |
| [PMID: 36568077](https://pubmed.ncbi.nlm.nih.gov/36568077/) | Biophysics/review | Defines HMG-box mechanism: sequence-specific binding with sharp bending (F2) |
| [PMID: 25258310](https://pubmed.ncbi.nlm.nih.gov/25258310/) | Structure-function | SRY as Y-encoded architectural TF; mutations cluster in HMG box; aromatic buttress (F1, F2) |
| [PMID: 18304538](https://pubmed.ncbi.nlm.nih.gov/18304538/) | Clinical + EMSA | Patient HMG-box mutations (K92M, A118P) reduce DNA binding (F2) |
| [PMID: 16762365](https://pubmed.ncbi.nlm.nih.gov/16762365/) | Structure-function | Argues M64I sex reversal is due to NLS defect, not bend loss — couples bending and localization (F6) |
| [PMID: 40467489](https://pubmed.ncbi.nlm.nih.gov/40467489/) | Model genetics | SRY + NR5A1 regulate SOX9 transcription (F3) |
| [PMID: 38246151](https://pubmed.ncbi.nlm.nih.gov/38246151/) | Comparative genomics | SRY binding to conserved Enh13 is a common testis mechanism (F3) |
| [PMID: 39498956](https://pubmed.ncbi.nlm.nih.gov/39498956/) | CRISPR | SRY mutation ↓SOX9, ↑WNT4 in embryos (F3) |
| [PMID: 21558314](https://pubmed.ncbi.nlm.nih.gov/21558314/) | Gonad culture | CaM antagonist ↓Sox9, disrupts cords, induces ovarian markers (F1, F4) |
| [PMID: 21051653](https://pubmed.ncbi.nlm.nih.gov/21051653/) | Cell biology | Dual β-NLS/CaM-NLS; Ca²⁺ as import switch (F4) |
| [PMID: 20528776](https://pubmed.ncbi.nlm.nih.gov/20528776/) | Cell biology | CaM-NLS mutations reduce nuclear import; shared across SOX/HMG proteins (F4) |
| [PMID: 15746192](https://pubmed.ncbi.nlm.nih.gov/15746192/) | Cell biology | CaM-dependent import; NLS mutations underlie sex reversal (F4) |
| [PMID: 24003159](https://pubmed.ncbi.nlm.nih.gov/24003159/) | Cell biology/genetics | Shuttling (Exportin-4/CRM1), phospho-SRY, ~2-fold threshold (F7) |
| [PMID: 9054412](https://pubmed.ncbi.nlm.nih.gov/9054412/) | Y2H/co-IP | C-terminal 7 aa of SRY bind PDZ domains of SIP-1 (F7) |
| [PMID: 17185318](https://pubmed.ncbi.nlm.nih.gov/17185318/) | Transgenics | *Sry* sufficient to induce testis in XX mice/humans (F8) |
| [PMID: 19457926](https://pubmed.ncbi.nlm.nih.gov/19457926/) | Model genetics | CITED2/WT1/SF1 raise SRY to critical threshold (F8) |
| [PMID: 32886743](https://pubmed.ncbi.nlm.nih.gov/32886743/) | ChIP/ex vivo | SRY binds FGF9 promoter; FGF9 sufficient for male fate (F9) |
| [PMID: 18617533](https://pubmed.ncbi.nlm.nih.gov/18617533/) | Model genetics | FGF9↔SOX9 loop; β-catenin stabilization → XY reversal (F9) |
| [PMID: 19850934](https://pubmed.ncbi.nlm.nih.gov/19850934/) | Biochemistry | SRY recruits KRAB-O/KAP1 to repress targets (RSPO1) (F10) |
| [PMID: 11101852](https://pubmed.ncbi.nlm.nih.gov/11101852/) | Mouse genetics | *Odsex*: general repressor model; Sox9 a direct Sry target (F10) |
| [PMID: 41138755](https://pubmed.ncbi.nlm.nih.gov/41138755/) | Molecular evolution | SRY originated from SOX3; relaxed constraint (F5) |
| [PMID: 40406982](https://pubmed.ncbi.nlm.nih.gov/40406982/) | Mouse genetics | KDM6B de-repression required upstream of Sry (F5) |
| [PMID: 11301600](https://pubmed.ncbi.nlm.nih.gov/11301600/) | Review | DAX-1 as antagonistic "antitestis" gene to SRY (F10) |

**Complementary / contextual evidence.** The MAP3K1 literature ([PMID: 24135036](https://pubmed.ncbi.nlm.nih.gov/24135036/), [PMID: 31446095](https://pubmed.ncbi.nlm.nih.gov/31446095/)) shows mutations that "tilt the balance from SOX9/FGF9 to WNT/β-catenin signaling," reinforcing SRY's position upstream of a tunable SOX9/FGF9-vs-WNT antagonism. The DSS/DAX-1 duplication literature ([PMID: 8840552](https://pubmed.ncbi.nlm.nih.gov/8840552/)) and CBX2 ([PMID: 31116734](https://pubmed.ncbi.nlm.nih.gov/31116734/)) further illustrate the repressive/antagonistic logic surrounding SRY. Dmrt1 overexpression driving XX male development ([PMID: 25725066](https://pubmed.ncbi.nlm.nih.gov/25725066/)) places SRY within a broader metazoan context in which SRY is the newly evolved mammalian trigger.

---

## Limitations and Knowledge Gaps

1. **Model-organism extrapolation.** Much mechanistic detail (Enh13 activation, feed-forward loops, KDM6B upstream control, shuttling) derives from mouse or ex vivo gonad cultures. Human-specific features exist — e.g., human SRY activates FGF9 independently of SF1 whereas mouse SRY cooperates with SF1 ([PMID: 32886743](https://pubmed.ncbi.nlm.nih.gov/32886743/)) — so species differences must be handled carefully.

2. **The activation vs. repression balance is not fully resolved at the locus level.** SRY clearly both activates (SOX9, FGF9) and represses (via KRAB-O/KAP1). Which targets are directly repressed in vivo (RSPO1 is "proposed"), and how SRY toggles between co-activator (SF1) and co-repressor (KRAB-O/KAP1) complexes at specific promoters, remains incompletely defined.

3. **Bend-angle vs. localization causality.** The M64I debate ([PMID: 11563911](https://pubmed.ncbi.nlm.nih.gov/11563911/) vs. [PMID: 16762365](https://pubmed.ncbi.nlm.nih.gov/16762365/)) shows that disentangling DNA-bend defects from nuclear-import defects for individual mutations is non-trivial, because the HMG box carries both functions. This complicates genotype–phenotype interpretation in patients.

4. **Direct human-embryo evidence is limited.** For ethical and practical reasons, the human in vivo chain (SRY → SOX9/FGF9 in human pre-Sertoli cells at the precise developmental window) is largely inferred from clinical genetics plus animal models rather than observed directly.

5. **Trans-activation partners under-characterized.** SRY lacks a classical activation domain; partners such as SIP-1 ([PMID: 9054412](https://pubmed.ncbi.nlm.nih.gov/9054412/)) and NHERF2 ([PMID: 39813852](https://pubmed.ncbi.nlm.nih.gov/39813852/)) are reported, but their quantitative contribution to SOX9/FGF9 induction in vivo is unclear.

6. **Post-translational regulation.** Phosphorylation gates nuclear accumulation of "activated" SRY ([PMID: 24003159](https://pubmed.ncbi.nlm.nih.gov/24003159/)), but the responsible kinases/phosphatases and the full PTM code of SRY are not fully mapped.

---

## Proposed Follow-up Experiments / Actions

1. **Genome-wide direct target mapping in human pre-Sertoli-like cells.** Perform CUT&RUN/ChIP-seq for SRY in a human XY gonadal/iPSC-derived pre-Sertoli model to define the complete, directly bound activation and repression cisregulome (confirm SOX9-Enh13 and FGF9; test RSPO1 and other ovarian genes as direct repression targets).

2. **Dissect the activator/repressor switch.** Use proximity labeling (BioID/TurboID) on SRY in male gonadal cells to catalog promoter-context-dependent partners (SF1 vs. KRAB-O/KAP1 vs. SIP-1/NHERF2) and determine what dictates co-activator vs. co-repressor recruitment.

3. **Quantitative threshold mapping.** Build an allelic series of SRY (graded expression/dose) in gonad culture and measure SOX9/FGF9 output to precisely define the human ~2-fold threshold and its sensitivity to NLS/shuttling/bend-angle variants.

4. **Decouple bending from localization.** Engineer SRY variants that selectively alter DNA-bend angle while preserving nuclear import (and vice versa), then assay SOX9/FGF9 activation — resolving the M64I-type causality debate.

5. **Chromatin-level upstream control.** Test whether KDM6B and PRC1/CBX2 activity gate human SRY activation timing, and whether modulating H3K27me3 can rescue or phenocopy threshold-level SRY deficits.

6. **Structural biology of the ternary complexes.** Pursue cryo-EM/NMR of SRY–DNA–SF1 on the Enh13 element and SRY–KRAB-O–KAP1 to visualize how architectural bending nucleates each functional complex.

---

## Conclusion

SRY (Q05066) is the **Y-encoded master testis-determining factor** — an architectural HMG-box transcription factor whose primary biochemical function is sequence-specific minor-groove DNA binding and ~54° DNA bending. It operates transiently in the nucleus of pre-Sertoli cells (entering via dual importin-β/calmodulin NLSs and regulated Exportin-4/CRM1 shuttling) and is both necessary and sufficient to commit the bipotential gonad to testis fate. With SF1 it directly activates SOX9 (Enh13/TESCO) and FGF9, igniting a self-sustaining FGF9↔SOX9 feed-forward loop, while recruiting the KRAB-O/KAP1 machinery to repress the ovarian program (e.g., RSPO1) and antagonize the WNT4/RSPO1/β-catenin/FOXL2 pathway. Its action is dosage-gated to a ~2-fold threshold, and HMG-box or trafficking defects that breach this threshold cause 46,XY gonadal dysgenesis (Swyer syndrome).


## Artifacts

- [OpenScientist final report](SRY-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](SRY-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:21558314
2. PMID:25258310
3. PMID:36568077
4. PMID:18304538
5. PMID:40467489
6. PMID:38246151
7. PMID:39498956
8. PMID:21051653
9. PMID:20528776
10. PMID:15746192
11. PMID:41138755
12. PMID:40406982
13. PMID:11563911
14. PMID:16762365
15. PMID:24003159
16. PMID:9054412
17. PMID:39813852
18. PMID:17185318
19. PMID:19457926
20. PMID:32886743
21. PMID:18617533
22. PMID:19850934
23. PMID:11101852
24. PMID:11301600
25. PMID:24135036
26. PMID:31446095
27. PMID:8840552
28. PMID:31116734
29. PMID:25725066