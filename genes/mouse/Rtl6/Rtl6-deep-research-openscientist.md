---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T14:53:48.860087'
end_time: '2026-10-24T15:11:05.928365'
duration_seconds: 1037.07
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: mouse
  gene_id: Rtl6
  gene_symbol: Rtl6
  uniprot_accession: Q505G4
  protein_description: 'RecName: Full=Retrotransposon Gag-like protein 6 {ECO:0000250|UniProtKB:Q6ICC9};
    AltName: Full=Mammalian retrotransposon-derived protein 6 {ECO:0000303|PubMed:15716091};
    AltName: Full=Protein LDOC1L {ECO:0000305}; AltName: Full=Protein Sushi-15E3;'
  gene_info: Name=Rtl6 {ECO:0000250|UniProtKB:Q6ICC9}; Synonyms=Ldoc1l {ECO:0000305},
    Mar6, Mart6 {ECO:0000303|PubMed:15716091}, Sushi-15E3;
  organism_full: Mus musculus (Mouse).
  protein_family: Belongs to the LDOC1 family. .
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
citation_count: 4
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Rtl6-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Rtl6-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q505G4
- **Protein Description:** RecName: Full=Retrotransposon Gag-like protein 6 {ECO:0000250|UniProtKB:Q6ICC9}; AltName: Full=Mammalian retrotransposon-derived protein 6 {ECO:0000303|PubMed:15716091}; AltName: Full=Protein LDOC1L {ECO:0000305}; AltName: Full=Protein Sushi-15E3;
- **Gene Information:** Name=Rtl6 {ECO:0000250|UniProtKB:Q6ICC9}; Synonyms=Ldoc1l {ECO:0000305}, Mar6, Mart6 {ECO:0000303|PubMed:15716091}, Sushi-15E3;
- **Organism (full):** Mus musculus (Mouse).
- **Protein Family:** Belongs to the LDOC1 family. .
- **Key Domains:** RTL1/1-8/LDOC_capsid-like. (IPR032549); RTL1-8_LDOC (PF16297)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Rtl6" matches the protein description above**
2. **Verify the organism is correct:** Mus musculus (Mouse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Rtl6' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Rtl6** (gene ID: Rtl6, UniProt: Q505G4) in mouse.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: Mouse *Rtl6* (SIRH3 / Ldoc1l / Mart6 / Sushi-15E3)

**UniProt:** [Q505G4](https://www.uniprot.org/uniprotkb/Q505G4/entry) · **Gene:** *Rtl6* · **Organism:** *Mus musculus* (Mouse) · **Family:** LDOC1 / Retrotransposon Gag-like (RTL)/SIRH · **Domain:** RTL1/1-8/LDOC_capsid-like (IPR032549); RTL1-8_LDOC (PF16297)

---

## Summary

Mouse **Rtl6** encodes a small (243-amino-acid, ~27 kDa), **extremely basic** (predicted pI ≈ 11.15; net charge ≈ +13) protein derived from the *gag* (capsid) gene of an ancient **domesticated retrovirus** (a metavirus/sushi-ichi-type element). Its primary, experimentally demonstrated function is **innate-immune defense of the eutherian brain**: RTL6 is expressed selectively by **microglia** (the brain's resident macrophages), peaks in expression **perinatally**, and acts **extracellularly** as a **cationic scavenger that directly binds and clears bacterial lipopolysaccharide (LPS)**. This is not a signaling, enzymatic, or transport function in the classical sense — RTL6 is best described as a **pathogen-associated-molecular-pattern (PAMP) sequestration effector** that physically traps an anionic microbial ligand and promotes its removal.

The mechanism is electrostatic and structural. AlphaFold2/ColabFold modeling predicts two long α-helices: an **N-terminal leucine-zipper/coiled-coil** (confirmed independently by UniProt's coiled-coil annotation at residues 29–69) that mediates **self-oligomerization** into a "bouquet"-like granule, and an **extremely basic C-terminal helix** that presents a positively charged surface to capture the highly acidic LPS molecule. In vivo brain-injection experiments show RTL6 accumulates at LPS-injected sites within minutes, in proportion to the LPS dose, forming a complex with RTL6 at the core and LPS on the surface. The function is **specific and non-redundant**: *Rtl6*-knockout mice fail to clear injected LPS (which persists in the extracellular space for >2 h), while clearance of double-stranded RNA (dsRNA) — handled by the paralog RTL5 — is unaffected, and vice versa, yielding a clean double dissociation.

RTL6 belongs to a **microglial RTL defense triad**: RTL5/SIRH8 removes viral dsRNA, **RTL6/SIRH3 removes bacterial LPS**, and RTL9/SIRH10 removes fungal zymosan — each targeting a different class of PAMP. RTL6 is the **most conserved** of the eleven eutherian RTL/SIRH genes, under exceptionally strong purifying selection (dN/dS mostly < 0.05), underscoring an essential, non-redundant role acquired during mammalian evolution. It most likely functions **independently of the Toll-like-receptor (TLR4) signaling system**, instead acting as a direct physical "trap." Notably, the formal UniProt entry for Q505G4 remains sparse (no Function comment, no subcellular-location annotation, no GO terms), so this report synthesizes the primary literature that now defines the gene's role.

---

## Gene/Protein Identity Verification

Before presenting findings, the mandatory identity checks were completed and **passed**:

| Check | Result |
|-------|--------|
| Gene symbol "Rtl6" matches UniProt protein description | ✅ Yes — "Retrotransposon Gag-like protein 6," synonyms Ldoc1l/Mar6/Mart6/Sushi-15E3 |
| Organism | ✅ *Mus musculus* (mouse) |
| Protein family/domains align with literature | ✅ Yes — LDOC1 family; RTL1-8/LDOC capsid-like (GAG-like) domain; literature on "RTL6/SIRH3" matches exactly |
| Risk of same-symbol confusion with a different gene | ⚠️ Low — the primary literature (Irie et al. 2022; Ishino/Kaneko-Ishino reviews) explicitly uses "RTL6/SIRH3" for this mouse microglial gene. No conflicting-organism literature was found that would redirect the research. |

The gene is **not ambiguous** in the current literature, and a dedicated, recent primary paper (Irie et al. 2022, *Development*) directly characterizes mouse RTL6 function. Research therefore proceeded on the correct target.

---

## Key Findings

### Finding 1 — RTL6/SIRH3 is a microglial innate-immune effector against bacterial LPS in the eutherian brain

The defining functional study, **Irie et al. 2022** (*Retrovirus-derived RTL5 and RTL6 genes are novel constituents of the innate immune system in the eutherian brain*, [PMID: 36162816](https://pubmed.ncbi.nlm.nih.gov/36162816/)), generated **RTL6-Venus knock-in reporter mice** and demonstrated that RTL6 is expressed **specifically in microglia**. Loss-of-function **Rtl6-knockout mice** showed an impaired brain response to lipopolysaccharide, providing direct genetic evidence that RTL6 acts as a factor against LPS. In the authors' words:

> "Experiments using Rtl6 or Rtl5 knockout mice provided additional evidence that RTL6 and RTL5 act as factors against LPS and dsRNA, respectively, in the brain, providing the first demonstration that retrovirus-derived genes play a role in the eutherian innate immune system." — [PMID: 36162816](https://pubmed.ncbi.nlm.nih.gov/36162816/)

This was independently reaffirmed in the review by **Ishino/Kaneko-Ishino 2023** ([PMID: 37834332](https://pubmed.ncbi.nlm.nih.gov/37834332/)):

> "RTL5 and RTL6 (also known as sushi-ichi retrotransposon homolog 8 (SIRH8) and SIRH3) are microglial genes that play important roles in the brain's innate immunity against viruses and bacteria through their removal of double-stranded RNA and lipopolysaccharide, respectively." — [PMID: 37834332](https://pubmed.ncbi.nlm.nih.gov/37834332/)

**Interpretation:** RTL6's primary biological process is **innate immune defense (bacterial/LPS clearance)**, carried out by microglia in the CNS. This is the central, experimentally anchored conclusion of the report.

### Finding 2 — RTL6 is a cationic (extremely basic) protein secreted extracellularly as dots/granules in the CNS

Irie et al. 2022 report that RTL5 and RTL6 "respectively, encode a strongly acidic and extremely basic protein," and that the RTL6-Venus fusion, when expressed in microglia, "**appeared as extracellular dots and granules in the central nervous system**" and showed "a rapid response to pathogens such as lipopolysaccharide (LPS)."

> "They, respectively, encode a strongly acidic and extremely basic protein, and are well conserved among the eutherians." — [PMID: 36162816](https://pubmed.ncbi.nlm.nih.gov/36162816/)

> "Venus and mCherry knock-in mice exhibited expression of RTL5-mCherry and RTL6-Venus fusion proteins in microglia and appeared as extracellular dots and granules in the central nervous system." — [PMID: 36162816](https://pubmed.ncbi.nlm.nih.gov/36162816/)

**Interpretation:** This establishes both the **biochemical basis** of function (an extremely basic/cationic protein can bind anionic LPS) and the **subcellular localization** (the protein acts **extracellularly**, deposited as dots/granules in the CNS, rather than as an intracellular enzyme). The "extremely basic" character is the mechanistic key: LPS is a strongly anionic amphipathic molecule, and electrostatic complementarity underlies the trapping.

### Finding 3 — RTL6 is a eutherian-specific, retrovirus (metavirus)-derived domesticated Gag-like gene of the LDOC1/SIRH family

RTL6/SIRH3 is one of **eleven sushi-ichi retrotransposon homolog (SIRH)/Retrotransposon Gag-like (RTL) genes** derived from an ancient metavirus/retrovirus and conserved specifically among eutherian (placental) mammals (Kaneko-Ishino & Ishino 2023, [PMID: 37892118](https://pubmed.ncbi.nlm.nih.gov/37892118/); Irie et al. 2026, [PMID: 42511665](https://pubmed.ncbi.nlm.nih.gov/42511665/)). It is a member of the **LDOC1 protein family** (UniProt Q505G4; synonyms Ldoc1l/Mart6/Sushi-15E3) and retains an **RTL1/LDOC capsid-like (GAG-like) domain** (InterPro IPR032549; Pfam PF16297).

> "Eutherian mammals possess 11 metavirus-derived genes, collectively known as the sushi-ichi retrotransposon homologue (SIRH)/Retrotransposon Gag-like (RTL) genes." — [PMID: 42511665](https://pubmed.ncbi.nlm.nih.gov/42511665/)

> "SIRH3/RTL6, SIRH8/RTL5, and SIRH10/RTL9 mediate innate immune responses against bacterial-, viral-, and fungal-derived pathogen-associated molecular patterns, respectively." — [PMID: 42511665](https://pubmed.ncbi.nlm.nih.gov/42511665/)

**Interpretation:** The protein's architecture is that of a **retroviral capsid (Gag) protein that has been "domesticated"** by the host genome. In retroviruses, Gag self-assembles into the viral capsid shell; RTL6 appears to repurpose this inherent **self-oligomerization/capsid-assembly property** to build a PAMP-trapping scaffold. For the related RTL9, the C-terminal retroviral GAG-like region is required for pathogen-degrading activity, implicating the conserved Gag/capsid-like domain generally in RTL immune-effector function.

### Finding 4 — RTL6 directly traps LPS via a cationic C-terminal helix and leucine-zipper oligomerization; Rtl6 loss specifically impairs LPS clearance

This is the **mechanistic core** of the report, drawn from the in vivo assays in Irie et al. 2022 (PMC9641642).

- **Rapid, dose-proportional recruitment:** Minutes after injection of fluorescently labeled LPS into the brain, RTL6 accumulated at LPS-injected regions **in proportion to the amount of LPS**.
- **Complex architecture:** In RTL5/RTL6 double-knock-in brains, a large "RTL5/RTL6/LPS complex" formed in which **RTL6 was at the complex core and LPS on its surface**, "suggesting that the RTL6 complex has the capacity to trap LPS."
- **Specificity (double dissociation):** In *Rtl6*-KO brain (n = 4), "much of the injected LPS remained in the extracellular space even after 2 h… indicating that LPS removal was significantly reduced in the Rtl6 KO mice," whereas in *Rtl5*-KO mice "the LPS removal activity was essentially unaffected." Conversely, **dsRNA removal was impaired in Rtl5-KO but not Rtl6-KO** — a clean, reciprocal double dissociation establishing ligand specificity.
- **Structural model:** ColabFold/AlphaFold2 predicts RTL6 has **two long helices** — an **extremely basic C-terminal helix** and an **N-terminal leucine-zipper motif**. RTL6 **oligomerizes via the leucine zipper** into a "bouquet-like" structure that **electrostatically traps the highly acidic LPS** on the surface of its basic helix.

> "These proteins display a rapid response to pathogens such as lipopolysaccharide (LPS), double-stranded (ds) RNA analog and non-methylated CpG DNA, acting both cooperatively and/or independently." — [PMID: 36162816](https://pubmed.ncbi.nlm.nih.gov/36162816/)

**Interpretation:** RTL6 is a **direct physical trap** — a cationic, self-assembling capsid-like scaffold that sequesters anionic LPS. The reciprocal KO experiments rule out redundancy and demonstrate **ligand-specific, non-overlapping roles** for RTL5 (dsRNA) and RTL6 (LPS).

### Finding 5 — RTL6 (243 aa, pI ≈ 11.15) is the most conserved RTL gene, under very strong purifying selection; CNS-predominant, perinatal-peak expression; likely TLR-independent

**Molecular properties (Irie et al. 2022, PMC9641642):** Mouse RTL6 is a small **243-aa protein** with an extreme isoelectric point **pI = 11.15** (contrast RTL5: 599 aa, pI = 4.39); it shares ~25.6–27.7% identity / ~44% similarity with the sushi-ichi retrotransposon Gag protein; endogenous RTL6 runs at ~27 kDa (RTL6-Venus at 54 kDa).

**Evolution:** RTL6 shows an **extremely low dN/dS ratio** (mostly < 0.05 across ten eutherian species) — "RTL6 has been subjected to very strong purifying selection" and is "**the most conserved of the RTL genes in eutherians**," with dN/dS lying between housekeeping genes (~0.093) and histone H3 (< 0.01). It is **eutherian-specific** with no orthologues in birds, monotremes, or marsupials (locus mapped between SHISAL1 and PRR5).

**Expression:** *Rtl6* is **predominantly expressed in the CNS**, rising from embryonic day E13.5 and **peaking perinatally (P0–P3)**; **more than 40% of P1 microglia** express RTL6. Lower-level mRNA is also seen in muscle, kidney, and testis.

**Pathway relationship:** Microglia express TLR3/4/9 (for dsRNA/LPS/CpG), but the authors note that RTL6/RTL5 act as intra/extracellular granules and "**it is possible that they function independently of the TLR systems.**"

> "They, respectively, encode a strongly acidic and extremely basic protein, and are well conserved among the eutherians." — [PMID: 36162816](https://pubmed.ncbi.nlm.nih.gov/36162816/)

**Interpretation:** The exceptional conservation (dN/dS < 0.05) is strong evolutionary evidence that RTL6's LPS-trapping function is **essential and non-redundant**. The perinatal expression peak suggests the protein is especially important during the **vulnerable neonatal window**, when the blood-brain barrier is immature and the CNS is at heightened risk of bacterial/endotoxin exposure. The likely TLR-independence positions RTL6 as a **direct scavenger** rather than a receptor/signal transducer.

### Finding 6 — UniProt sequence features independently corroborate the oligomerization/charge mechanism, but functional annotation is sparse/outdated

The reviewed Swiss-Prot entry **UniProt Q505G4** (protein existence level 2: evidence at transcript level) describes a **243-aa chain** with **net charge ≈ +13** (36 basic residues K/R/H vs 20 acidic D/E), confirming the strongly cationic character (reported pI 11.15). Critically, UniProt annotates a **coiled-coil feature at residues 29–69** — matching the **N-terminal leucine-zipper/oligomerization element** described from AlphaFold2 modeling by Irie et al. 2022. **Disordered regions** flank the termini (1–22, 84–105, 218–243).

However, the UniProt entry has **NO Function comment, NO subcellular-location annotation, and NO GO terms**, and lists tissue specificity only as "Widely expressed" (keyword set limited to "Coiled coil").

**Interpretation:** Two **independent lines of evidence** — the experimental/structural study and the database sequence features — converge on the same mechanism (a cationic, coiled-coil-oligomerizing protein). This cross-validation strengthens confidence in the oligomerize-and-trap model. At the same time, the gap between the rich functional literature and the barren formal annotation highlights that **database annotations lag the primary literature** for this gene; the UniProt "Widely expressed" tissue note, in particular, is contradicted by the CNS/microglia-predominant expression shown experimentally.

---

## Mechanistic Model / Interpretation

RTL6 is best understood as a **domesticated viral capsid protein repurposed as a cationic endotoxin trap**. The proposed sequence of events:

```
            BACTERIAL ENDOTOXIN IN THE PERINATAL CNS
                              │
                              ▼
 Microglia (resident brain macrophages) constitutively express RTL6
       (perinatal peak; >40% of P1 microglia; secreted extracellularly)
                              │
                              ▼
   RTL6 self-oligomerizes via N-terminal leucine-zipper / coiled-coil
              (residues 29–69) → "bouquet"-like granule
                              │
                              ▼
  Extremely basic C-terminal helix (pI 11.15, net +13) presents a
          positively charged surface to the extracellular space
                              │
              LPS (highly anionic lipoglycan) appears
                              │
                              ▼
   Electrostatic capture: RTL6 at complex CORE, LPS on the SURFACE
          (recruitment within minutes, proportional to LPS dose)
                              │
                              ▼
         LPS SEQUESTERED and REMOVED from extracellular space
       (fails to clear within >2 h in Rtl6-KO → function confirmed)
                              │
                              ▼
   Likely TLR4-independent: acts as a direct physical scavenger,
         not a receptor/signal transducer
```

RTL6 is the **antibacterial member of a microglial RTL defense triad** in which each paralog neutralizes a distinct class of PAMP by direct binding/removal:

| RTL gene | Alias | PAMP target | Pathogen class | Biochemical property |
|----------|-------|-------------|----------------|----------------------|
| **RTL6** | **SIRH3** | **Lipopolysaccharide (LPS)** | **Bacteria** | **Extremely basic (cationic), pI ≈ 11.15, net +13** |
| RTL5 | SIRH8 | Double-stranded RNA | Viruses | Strongly acidic, pI ≈ 4.39 |
| RTL9 | SIRH10 | Zymosan / β-glucan | Fungi | Gag-like C-terminus required for activity |

The electrostatic logic is elegant and self-consistent: an **extremely basic** RTL6 captures **anionic** LPS, whereas the **acidic** RTL5 captures a different (nucleic-acid) ligand. The reciprocal knockout double dissociation (Rtl6-KO loses LPS clearance but keeps dsRNA clearance; Rtl5-KO the reverse) demonstrates that these are **dedicated, non-redundant effectors**, not generic sticky proteins.

**Functional classification:** RTL6 is **not an enzyme** (no catalyzed reaction, no substrate turnover), **not a transporter**, and **not a classical signaling molecule**. It is a **scavenger/sequestration protein (PAMP-binding innate-immune effector)** that acts through stoichiometric physical binding and oligomeric assembly. Its "substrate specificity," in the loose sense, is **anionic bacterial LPS**, recognized via charge complementarity rather than a defined catalytic/enzymatic pocket.

**Localization:** The protein performs its function **extracellularly**, deposited as dots/granules in the CNS parenchyma after secretion from microglia — a localization appropriate for intercepting extracellular endotoxin.

---

## Evidence Base

| Paper | PMID | Type | Role in this report |
|-------|------|------|---------------------|
| *Retrovirus-derived RTL5 and RTL6 genes are novel constituents of the innate immune system in the eutherian brain* (Irie et al. 2022, *Development*) | [36162816](https://pubmed.ncbi.nlm.nih.gov/36162816/) | **Primary** | **Defining functional study.** Knock-in reporters + KO mice; LPS brain-injection trapping assays; AlphaFold2 structural model; dN/dS conservation; expression profiling. Supports Findings 1, 2, 4, 5. |
| *Retrovirus-Derived RTL/SIRH: Their Diverse Roles in the Current Eutherian Developmental System…* (Kaneko-Ishino & Ishino 2023) | [37892118](https://pubmed.ncbi.nlm.nih.gov/37892118/) | Review | Places RTL6 in the 11-member eutherian RTL/SIRH family; retrovirus-derived origin. Supports Finding 3. |
| *Retrovirus-Derived…* (Ishino/Kaneko-Ishino 2023) | [37834332](https://pubmed.ncbi.nlm.nih.gov/37834332/) | Review | Independently restates RTL6 (SIRH3) as a microglial gene that removes LPS. Supports Finding 1. |
| *Virus-Derived Domesticated Genes in Microglia and Resident Macrophages…* (Irie et al. 2026) | [42511665](https://pubmed.ncbi.nlm.nih.gov/42511665/) | Review | Frames the RTL5/RTL6/RTL9 triad (viral/bacterial/fungal PAMPs); 11 metavirus-derived genes. Supports Finding 3 and the mechanistic model. |
| UniProt Q505G4 (reviewed/Swiss-Prot) | — | Database | Sequence features: 243 aa, net +13, coiled-coil 29–69, disordered termini. Independently corroborates mechanism (Finding 6). Also documents annotation gaps. |

**Consistency of the evidence base:** All four papers and the database entry are **mutually reinforcing** — there are no contradictory findings. The strongest evidence is the **loss-of-function genetics** (Rtl6-KO fails to clear LPS) combined with the **reciprocal specificity control** (Rtl5-KO does not), which together constitute near-definitive proof of a dedicated LPS-clearing role. The structural/charge evidence (AlphaFold2 + UniProt coiled-coil + pI 11.15/net +13) provides a coherent mechanistic explanation, and the evolutionary evidence (dN/dS < 0.05) argues the function is essential.

---

## Limitations and Knowledge Gaps

1. **Protein existence level is only "transcript" (PE2) in UniProt**, and the formal entry lacks Function/localization/GO annotations. The functional knowledge comes almost entirely from **one primary research group** (Irie, Kaneko-Ishino, Ishino and colleagues). Independent replication by other laboratories would strengthen confidence.

2. **Molecular/biophysical detail is inferred, not fully resolved.** The leucine-zipper oligomerization and basic-helix LPS binding derive from **AlphaFold2 modeling** plus in vivo imaging, not from an experimental crystal/cryo-EM structure of an RTL6–LPS complex. The exact binding stoichiometry, affinity (Kd), and the specific LPS moiety contacted (lipid A phosphates vs. core/O-antigen) remain undetermined.

3. **Fate of trapped LPS is unclear.** It is not established whether RTL6-bound LPS is subsequently phagocytosed/degraded by microglia, drained, or otherwise neutralized. "Removal/clearance" describes the phenotype, not the downstream disposal pathway.

4. **TLR-independence is stated as a possibility, not proven.** Whether RTL6 function requires, cooperates with, or is fully independent of TLR4/MD-2/CD14 signaling has not been directly tested (e.g., in TLR4-null backgrounds).

5. **Physiological/disease relevance beyond acute injection is untested.** Whether Rtl6-KO mice show increased susceptibility to real bacterial CNS infection (e.g., meningitis), neonatal sepsis-associated brain injury, or endotoxin-driven neuroinflammation is not established. The reported assays are acute, injected-ligand models.

6. **Minor extraneural expression** (muscle, kidney, testis) is noted but functionally uncharacterized; a non-CNS role cannot be excluded.

---

## Proposed Follow-up Experiments / Actions

1. **Direct binding biochemistry.** Purify recombinant RTL6 and measure LPS binding by SPR/ITC/microscale thermophoresis to obtain a **Kd** and determine which part of LPS (lipid A phosphates, inner-core KDO, O-antigen) is recognized. Test specificity against other anionic ligands (lipoteichoic acid, nucleic acids, polyglutamate).

2. **Experimental structure.** Solve a cryo-EM or crystal structure of the RTL6 oligomer and, ideally, an RTL6–lipid A complex to validate the "bouquet"/capsid-like assembly and the basic-helix binding surface predicted by AlphaFold2.

3. **Structure-guided mutagenesis.** Neutralize the C-terminal basic residues (K/R→A) to test loss of LPS binding, and disrupt the leucine zipper (residues 29–69) to test whether oligomerization is required for trapping — in vitro and via knock-in mice.

4. **Downstream fate of trapped LPS.** Use live imaging and pulse-chase to determine whether RTL6–LPS complexes are phagocytosed/degraded by microglia, and whether RTL6 lowers downstream NF-κB/cytokine (TNF-α, IL-6) induction.

5. **TLR4-dependence test.** Cross Rtl6-KO with Tlr4-KO (or Cd14/Ly96-null) mice to formally dissect whether RTL6 scavenging is independent of, parallel to, or upstream of TLR4 signaling.

6. **Infection and neonatal challenge models.** Test Rtl6-KO susceptibility to live Gram-negative bacterial CNS infection and to systemic LPS/neonatal endotoxemia, assaying brain bacterial load, neuroinflammation, blood-brain-barrier integrity, and neurodevelopmental outcomes.

7. **Database annotation update.** Submit the now-established function, microglial expression, extracellular localization, and LPS-binding activity to UniProt/GO so the formal annotation reflects the primary literature.

---

## Conclusion

Mouse **Rtl6 (SIRH3/Ldoc1l/Mart6; UniProt Q505G4)** is a **retrovirus-derived, domesticated Gag/capsid-like protein** whose primary function is **innate-immune defense of the brain against bacterial endotoxin**. Expressed selectively by **microglia** (peaking perinatally) and acting **extracellularly**, RTL6 is an **extremely cationic scavenger** (pI ≈ 11.15, net ≈ +13) that **oligomerizes via an N-terminal leucine-zipper/coiled-coil (residues 29–69)** and uses its **basic C-terminal helix** to **directly trap and clear anionic lipopolysaccharide (LPS)**. Its role is **specific and non-redundant** — *Rtl6*-knockout mice fail to clear injected LPS while clearing dsRNA normally — and it is the **antibacterial member of a microglial RTL defense triad** (RTL5→viral dsRNA, RTL6→bacterial LPS, RTL9→fungal zymosan). RTL6 is thus a **PAMP-sequestration effector**, likely independent of TLR4 signaling, and is **not** an enzyme or transporter. Its status as the **most conserved RTL gene** (dN/dS < 0.05) underscores that this endotoxin-trapping function is essential to eutherian brain immunity.


## Artifacts

- [OpenScientist final report](Rtl6-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Rtl6-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:36162816
2. PMID:37834332
3. PMID:37892118
4. PMID:42511665