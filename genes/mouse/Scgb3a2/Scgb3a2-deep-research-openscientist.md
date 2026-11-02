---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T18:45:47.054298'
end_time: '2026-10-24T19:24:34.593924'
duration_seconds: 2327.54
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: mouse
  gene_id: Scgb3a2
  gene_symbol: Scgb3a2
  uniprot_accession: Q920H1
  protein_description: 'RecName: Full=Secretoglobin family 3A member 2; AltName: Full=Pneumo
    secretory protein 1; Short=PnSP-1; AltName: Full=Uteroglobin-related protein 1;
    Flags: Precursor;'
  gene_info: Name=Scgb3a2; Synonyms=Pnsp1, Ugrp1;
  organism_full: Mus musculus (Mouse).
  protein_family: Belongs to the secretoglobin family. UGRP subfamily.
  protein_domains: Secretoglobin_3A. (IPR040301); SCGB3A (PF20490)
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
citation_count: 21
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Scgb3a2-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Scgb3a2-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q920H1
- **Protein Description:** RecName: Full=Secretoglobin family 3A member 2; AltName: Full=Pneumo secretory protein 1; Short=PnSP-1; AltName: Full=Uteroglobin-related protein 1; Flags: Precursor;
- **Gene Information:** Name=Scgb3a2; Synonyms=Pnsp1, Ugrp1;
- **Organism (full):** Mus musculus (Mouse).
- **Protein Family:** Belongs to the secretoglobin family. UGRP subfamily.
- **Key Domains:** Secretoglobin_3A. (IPR040301); SCGB3A (PF20490)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Scgb3a2" matches the protein description above**
2. **Verify the organism is correct:** Mus musculus (Mouse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Scgb3a2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Scgb3a2** (gene ID: Scgb3a2, UniProt: Q920H1) in mouse.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of Mouse *Scgb3a2* (Secretoglobin family 3A member 2 / UGRP1 / PnSP-1; UniProt Q920H1)

## Summary

Mouse **Scgb3a2** encodes **Secretoglobin family 3A member 2 (SCGB3A2)**, also known historically as **Uteroglobin-Related Protein 1 (UGRP1)** and **Pneumo Secretory Protein 1 (PnSP-1)**. It is a small (~10 kDa) **secreted protein** that assembles into a disulfide-linked **homodimer** (and higher-order tetramer) and belongs to the **secretoglobin superfamily, UGRP subfamily** — the same structural family as uteroglobin/Clara cell secretory protein. Gene identity, organism (*Mus musculus*), and protein family all match the UniProt record precisely; the literature reviewed is unambiguously about this gene, so no identity conflict exists. SCGB3A2 is **not an enzyme, transporter, or structural/cytoskeletal protein**. Instead, it functions extracellularly as a **cytokine-/growth-factor-like immunomodulator and a secreted lipid/ligand-binding chaperone**.

The protein is produced almost exclusively by **airway epithelial Club (Clara) cells** of the lung and trachea, under the direct transcriptional control of the homeodomain transcription factor **NKX2-1 (T/EBP/TITF1)**. From its site of secretion into the airway lumen and alveolar space, SCGB3A2 carries out four interlocking, well-documented activities: (1) an **anti-inflammatory** activity that suppresses Th2-driven allergic airway inflammation by **inhibiting the NF-κB pathway**; (2) a **growth-factor** activity that promotes **fetal lung development and maturation**; (3) a **tissue-protective/anti-fibrotic and anti-emphysema** activity mediated by **STAT1/STAT3 signaling that transcriptionally upregulates α1-antitrypsin (Serpina1a)**; and (4) an **innate-immune and anti-cancer** activity in which SCGB3A2 acts as an **LPS chaperone**, binding bacterial lipopolysaccharide and delivering it into the cytosol via the cell-surface receptor **syndecan-1** to trigger **caspase-11–driven pyroptosis**. It also binds the alveolar-macrophage scavenger receptor **MARCO** and recognizes microbial surfaces, linking it to pathogen clearance.

The coherent picture that emerges is of a Club-cell secretoglobin that operates at the air–epithelium interface as a multifunctional signaling and chaperone molecule, using **two identified receptors (MARCO and syndecan-1)** and converging on **two principal signaling outputs (NF-κB inhibition and STAT3 activation)** to defend and remodel the lung. This report lays out the evidence for each of these functions, synthesizes them into a mechanistic model, evaluates the literature, and identifies the remaining knowledge gaps.

---

## Key Findings

### Finding 1 — Identity: SCGB3A2/UGRP1 is a secreted, NKX2-1–controlled homodimeric secretoglobin of airway Club cells

SCGB3A2 (gene *Scgb3a2*; synonyms *Ugrp1*, *Pnsp1*) was originally discovered as a novel gene **down-regulated in the lungs of T/ebp/Nkx2.1-null mouse embryos**, identifying it from the outset as a downstream target of the master lung/thyroid transcription factor NKX2-1. The gene has a compact structure of **3 exons and 2 introns** and maps to mouse **chromosome 18C-D**, a region homologous to **human 5q31-34** — a locus repeatedly linked to asthma and atopic phenotypes. The gene product is a **~10 kDa secreted protein** that forms a **homodimer** (and tetramer) and shows amino-acid sequence similarity to the **uteroglobin/Clara cell secretory protein family** of secretoglobins ([PMID: 11682631](https://pubmed.ncbi.nlm.nih.gov/11682631/)).

Expression is **predominantly in the lung** (airway epithelial Club/Clara-like cells) and trachea, with only low levels in thyroid. Developmentally, expression is detectable from early organogenesis and rises markedly by E16.5. Crucially, **cotransfection/reporter assays confirmed that T/EBP/NKX2.1 directly regulates the *Ugrp1* promoter** at the transcriptional level ([PMID: 11682631](https://pubmed.ncbi.nlm.nih.gov/11682631/)). This establishes the cell of origin, the secreted and dimeric nature of the protein, its family membership, and its upstream transcriptional regulator — the foundational facts on which all functional interpretations rest.

> *"The gene product is a secreted protein, forms a homodimer, and exhibits an amino acid sequence similar to that seen in the uteroglobin/Clara cell secretory protein family of proteins"* — [PMID: 11682631](https://pubmed.ncbi.nlm.nih.gov/11682631/)

### Finding 2 — Anti-inflammatory activity: suppression of allergic airway inflammation via NF-κB inhibition

SCGB3A2 is a bona fide **anti-inflammatory factor** in the airway. When adenovirus-delivered UGRP1 was expressed in the airway epithelium of ovalbumin (OVA)-sensitized and -challenged mice, it **markedly reduced the number of infiltrating inflammatory cells, particularly eosinophils**, in lung tissue and lowered the Th2 cytokines **IL-4, IL-5, and IL-13** in bronchoalveolar lavage (BAL) fluid ([PMID: 16456148](https://pubmed.ncbi.nlm.nih.gov/16456148/)). Mechanistically, more recent work shows that SCGB3A2 overexpression **mitigates toluene-diisocyanate (TDI)-induced inflammation and airway remodeling by inhibiting the NF-κB pathway and enhancing autophagy**; critically, re-activating NF-κB abrogated the protective effect, demonstrating that NF-κB inhibition is causal, not incidental ([PMID: 40865253](https://pubmed.ncbi.nlm.nih.gov/40865253/)).

SCGB3A2 sits within an **anti-inflammatory regulatory loop**: its own expression is suppressed during active inflammation and induced by resolving signals. *Ugrp1* mRNA is strongly inversely correlated with IL-5 (r = 0.948, P < 0.0001) and with IL-9 (r = 0.616, P = 0.023) in BAL, and intranasal IL-5 or IL-9 reduces lung *Ugrp1* ([PMID: 15626484](https://pubmed.ncbi.nlm.nih.gov/15626484/); [PMID: 15531759](https://pubmed.ncbi.nlm.nih.gov/15531759/)). Conversely, the anti-inflammatory cytokine **IL-10 induces *UGRP1* transcription through two NKX2-1 (T/EBP) binding sites** in the promoter ([PMID: 15485815](https://pubmed.ncbi.nlm.nih.gov/15485815/)). Thus SCGB3A2 is both an effector and a readout of the anti-inflammatory state of the airway.

> *"markedly reduced the number of infiltrating inflammatory cells, particularly eosinophils, in lung tissue as well as the level of proinflammatory cytokines such as interleukin (IL)-4, IL-5, and IL-13 in bronchoalveolar lavage fluids"* — [PMID: 16456148](https://pubmed.ncbi.nlm.nih.gov/16456148/)

### Finding 3 — Growth-factor activity: promotion of fetal lung development and maturation

SCGB3A2 behaves as a **growth factor for the developing lung**. Its expression rises sharply around **E16.5**, precisely when the lung undergoes dramatic morphogenetic changes. In *ex vivo* organ culture, SCGB3A2 **promoted early lung development of both wild-type and Nkx2-1-null fetal lungs**. Administered intravenously to Nkx2-1-heterozygous pregnant dams, it **rescued/advanced organogenesis in null fetuses**, and given to pregnant wild-type mice during mid-to-late organogenesis it **significantly promoted late lung maturation**, as judged by fetal breathing motion, gross/histological lung morphology, gestational-stage-specific gene expression, and surfactant phospholipid profiles ([PMID: 18535256](https://pubmed.ncbi.nlm.nih.gov/18535256/)).

> *"SCGB3A2 significantly promoted both early and late stages of lung dev"* — [PMID: 18535256](https://pubmed.ncbi.nlm.nih.gov/18535256/)

This activity is distinct from simple anti-inflammation: it is a direct, dose-responsive developmental/maturational effect, consistent with the protein's sharply timed developmental expression.

### Finding 4 — Anti-fibrotic activity and MARCO binding (innate defense)

Endogenous SCGB3A2 **protects against pulmonary fibrosis**. In a loss-of-function model, **Scgb3a2-null mice given bleomycin developed more severe fibrosis than wild-type**, with greater weight loss, higher Ashcroft fibrosis scores, elevated hydroxyproline and collagen mRNAs, more BAL inflammatory cells, and higher IL-4 and TGFβ mRNAs ([PMID: 26559674](https://pubmed.ncbi.nlm.nih.gov/26559674/)). This genetic evidence establishes that the protein normally restrains TGFβ-driven fibrotic remodeling.

Separately, a key mechanistic study identified a receptor and a microbial-recognition role. Secreted recombinant UGRP1 co-purified with apolipoprotein A-I, and expression cloning identified the **macrophage scavenger receptor with collagenous structure (MARCO)** — expressed by alveolar macrophages — as a **UGRP1 receptor**. UGRP1 also **bound bacteria and yeast**, and **LPS competed with UGRP1 for binding to MARCO and to bacteria** ([PMID: 12847263](https://pubmed.ncbi.nlm.nih.gov/12847263/)). This defines a lung-specific ligand–receptor pair and places SCGB3A2 squarely within innate immune surveillance and pathogen clearance.

> *"BLM-treated Scgb3a2-null mouse lungs had more severe fibrosis than those of wild-type mouse lungs"* — [PMID: 26559674](https://pubmed.ncbi.nlm.nih.gov/26559674/)
>
> *"we identified macrophage scavenger receptor with collagenous structure (MARCO) as a receptor for UGRP1"* — [PMID: 12847263](https://pubmed.ncbi.nlm.nih.gov/12847263/)

### Finding 5 — LPS chaperone: delivery of LPS via syndecan-1 to trigger caspase-11 pyroptosis

The most mechanistically precise function assigned to SCGB3A2 is that of an **LPS-delivery chaperone**. Secreted SCGB3A2 **binds lipopolysaccharide (LPS) and chaperones it into the cytosol through the cell-surface receptor syndecan-1**, thereby activating the **non-canonical inflammasome and caspase-11–driven pyroptosis** ([PMID: 30526845](https://pubmed.ncbi.nlm.nih.gov/30526845/)). SCGB3A2 + LPS co-treatment significantly induced pyroptosis of RAW264.7 macrophages and decreased cancer-cell proliferation *in vitro*, and SCGB3A2 treatment **reduced progression of xenograft tumors in mice**. The authors conclude that SCGB3A2 is a **critical LPS-delivery vehicle** that unifies its innate-immune and anti-cancer activities.

> *"secretoglobin(SCGB)3A2, a small protein predominantly secreted in airways, chaperones LPS to the cytosol through the cell surface receptor syndecan-1; this leads to pyroptotic cell death driven by caspase-11"* — [PMID: 30526845](https://pubmed.ncbi.nlm.nih.gov/30526845/)

This finding is especially important because it provides a concrete **molecular mechanism** — ligand (LPS), receptor (syndecan-1), route (cytosolic delivery), and effector (caspase-11/pyroptosis) — for a secretoglobin whose family is best known for ligand-binding hydrophobic cavities.

### Finding 6 — STAT3 → α1-antitrypsin axis protects the lung from emphysema

SCGB3A2 protects alveolar structure through a defined transcriptional cascade. In a 6-month cigarette-smoke COPD model, **Scgb3a2-knockout mice lost lung structure even under control conditions** and developed more airspace expansion and alveolar-wall destruction than wild-type after smoke exposure, whereas **Scgb3a2-overexpressing (transgenic) lungs were protected** ([PMID: 36796505](https://pubmed.ncbi.nlm.nih.gov/36796505/)). Mechanistically, SCGB3A2 **increased the expression and phosphorylation of STAT1 and STAT3 and increased α1-antitrypsin (A1AT) expression** in mouse lung fibroblast (MLg) and epithelial (MLE-15) cells. A1AT levels fell with *Stat3* knockdown and rose with *Stat3* overexpression; SCGB3A2 stimulation induced **STAT3 homodimer formation**; and **ChIP and reporter assays showed STAT3 binds specific sites on *Serpina1a* (encoding A1AT) and upregulates its transcription**, with nuclear localization of phosphorylated STAT3.

> *"SCGB3A2 increased the expression and phosphorylation of signal transducers and activators of transcription (STAT)1 and STAT3, and the expression of α1-antitrypsin (A1AT) in mouse lung fibroblast-derived MLg cells and mouse lung epithelial-derived MLE-15 cells"* — [PMID: 36796505](https://pubmed.ncbi.nlm.nih.gov/36796505/)
>
> *"STAT3 binds to specific binding sites on the Serpina1a gene encoding A1AT and upregulates its transcription in lung tissues of mice"* — [PMID: 36796505](https://pubmed.ncbi.nlm.nih.gov/36796505/)

Because α1-antitrypsin is the principal inhibitor of neutrophil elastase and its deficiency is a classic cause of emphysema, this axis provides a mechanistic explanation for the protein's anti-emphysema and tissue-protective activities.

### Finding 7 — Integrated model: a secreted secretoglobin with two receptors and two signaling outputs, not an enzyme

The authoritative review by Kimura et al. (2022) consolidates these threads: SCGB3A2 is *"a small secretory protein of ~10 kDa that forms a dimer and a tetramer... predominantly expressed in airway epithelial Club cells, and has anti-inflammatory, growth factor, anti-fibrotic, and anti-cancer activities that influence various lung diseases"* ([PMID: 35016921](https://pubmed.ncbi.nlm.nih.gov/35016921/)). Across the primary literature these resolve into anti-inflammatory activity via NF-κB inhibition, growth-factor/tissue-protective activity via STAT1/STAT3 → Serpina1a, and innate-immune/anti-cancer activity via LPS chaperoning through syndecan-1 and MARCO binding. **No catalytic/enzymatic or transporter activity has been reported.**

> *"SCGB3A2 is a small secretory protein of ~10 kDa that forms a dimer and a tetramer. SCGB3A2 is predominantly expressed in airway epithelial Club cells, and has anti-inflammatory, growth factor, anti-fibrotic, and anti-cancer activities that influence various lung diseases"* — [PMID: 35016921](https://pubmed.ncbi.nlm.nih.gov/35016921/)

---

## Mechanistic Model / Interpretation

SCGB3A2 is best understood as a **Club-cell secretoglobin that functions at the air–epithelium interface as a multifunctional signaling and chaperone protein**. The following schematic integrates the findings:

```
                    NKX2-1 (T/EBP)  ◄── IL-10 (induces)
                        │               IL-5 / IL-9 (repress)
                        ▼
              ┌─────────────────────┐
              │  Airway Club cell   │
              │   Scgb3a2 gene      │
              └─────────┬───────────┘
                        │ secretion
                        ▼
        ~10 kDa secreted homodimer/tetramer (SCGB3A2)
        acts EXTRACELLULARLY in airway lumen / alveolar space
                        │
     ┌──────────────────┼───────────────────┬────────────────────┐
     ▼                  ▼                   ▼                    ▼
 Binds LPS +       STAT1/STAT3          NF-κB inhibition      MARCO receptor
 syndecan-1        activation           + autophagy           (alveolar
     │             │                    │                      macrophages)
     ▼             ▼                    ▼                     + binds
 Cytosolic     STAT3 homodimer     ↓ eosinophils,            bacteria/yeast
 LPS delivery  → binds Serpina1a   ↓ IL-4/IL-5/IL-13         (LPS competes)
     │         → ↑ α1-antitrypsin  ↓ airway remodeling           │
     ▼             │                    │                         ▼
 caspase-11     ↓ elastase damage   suppresses allergic      innate microbial
 PYROPTOSIS    → anti-emphysema     airway inflammation      recognition /
     │          protects alveoli                             clearance
     ▼
 anti-cancer
 (↓ tumor growth)

 Separately: endogenous SCGB3A2 restrains TGFβ-driven fibrosis
 (Scgb3a2-null → worse bleomycin fibrosis)
 and promotes fetal lung development/maturation (growth-factor activity)
```

**Two receptors, two outputs.** The protein engages at least two cell-surface receptors: **MARCO** on alveolar macrophages (microbial recognition) and **syndecan-1** (cytosolic LPS delivery). Its intracellular signaling converges on two principal transcriptional outputs: **inhibition of NF-κB** (anti-inflammatory arm) and **activation of STAT1/STAT3** (tissue-protective/growth-factor arm, with *Serpina1a*/A1AT as the defined target gene).

**A unifying biochemical theme — ligand binding, not catalysis.** The secretoglobin fold is characterized by a hydrophobic internal cavity (classically demonstrated for uteroglobin's progesterone binding; [PMID: 7770456](https://pubmed.ncbi.nlm.nih.gov/7770456/), and for the uteroglobin-like cat allergen Fel d 1; [PMID: 17543334](https://pubmed.ncbi.nlm.nih.gov/17543334/)). SCGB3A2 exploits this ligand-binding capacity to **bind and chaperone LPS** (and to bind bacterial/fungal surfaces), rather than to catalyze any reaction. This reframes several of its "activities" as downstream consequences of a core **ligand-binding/chaperone** biochemical function combined with receptor-mediated signaling.

| Activity | Trigger / Receptor | Signaling output | Functional outcome | Key evidence |
|---|---|---|---|---|
| Anti-inflammatory | (airway epithelium) | NF-κB inhibition, ↑autophagy | ↓ eosinophils, ↓ Th2 cytokines, ↓ remodeling | [16456148](https://pubmed.ncbi.nlm.nih.gov/16456148/), [40865253](https://pubmed.ncbi.nlm.nih.gov/40865253/) |
| Growth factor | (fetal lung) | — (promotes maturation) | ↑ lung development, surfactant | [18535256](https://pubmed.ncbi.nlm.nih.gov/18535256/) |
| Anti-emphysema / tissue-protective | fibroblasts, epithelium | STAT1/STAT3 → *Serpina1a* | ↑ α1-antitrypsin, ↓ alveolar destruction | [36796505](https://pubmed.ncbi.nlm.nih.gov/36796505/) |
| Anti-fibrotic | (endogenous) | ↓ TGFβ, ↓ IL-4 | ↓ bleomycin fibrosis | [26559674](https://pubmed.ncbi.nlm.nih.gov/26559674/) |
| Innate immune / anti-cancer | LPS + syndecan-1; MARCO | caspase-11 | pyroptosis, ↓ tumor growth, microbial binding | [30526845](https://pubmed.ncbi.nlm.nih.gov/30526845/), [12847263](https://pubmed.ncbi.nlm.nih.gov/12847263/) |

**Localization.** All evidence indicates that SCGB3A2 is **secreted and acts extracellularly** — in the airway lumen and alveolar space (where it contacts macrophages via MARCO), and at the cell surface of target cells (via syndecan-1), from which it is routed to the **cytosol** specifically for the LPS-pyroptosis function. It is synthesized as a precursor (signal peptide) consistent with the classical secretory pathway.

---

## Evidence Base

| PMID | Study | Contribution | Strength |
|---|---|---|---|
| [11682631](https://pubmed.ncbi.nlm.nih.gov/11682631/) | UGRP1 as NKX2-1 target gene | Gene discovery, secreted homodimer, secretoglobin family, NKX2-1 regulation | Primary; foundational identity |
| [16456148](https://pubmed.ncbi.nlm.nih.gov/16456148/) | UGRP1 suppresses allergic airway inflammation | Gain-of-function: ↓ eosinophils, ↓ Th2 cytokines | Primary; in vivo mouse |
| [40865253](https://pubmed.ncbi.nlm.nih.gov/40865253/) | Curcumin/SCGB3A2 autophagy & NF-κB | Mechanism: NF-κB inhibition is causal | Primary; mechanistic |
| [15485815](https://pubmed.ncbi.nlm.nih.gov/15485815/) | IL-10 induces UGRP1 via T/EBP sites | Places SCGB3A2 in anti-inflammatory loop | Primary; promoter dissection |
| [15626484](https://pubmed.ncbi.nlm.nih.gov/15626484/) | IL-5 reduces UGRP1 | Inverse regulation by Th2 cytokine (r=0.948) | Primary; correlation + intervention |
| [15531759](https://pubmed.ncbi.nlm.nih.gov/15531759/) | IL-9 reduces UGRP1 | Inverse regulation (r=0.616) + localization | Primary |
| [18535256](https://pubmed.ncbi.nlm.nih.gov/18535256/) | SCGB3A2 in lung development | Growth-factor activity in vivo/ex vivo | Primary; developmental |
| [26559674](https://pubmed.ncbi.nlm.nih.gov/26559674/) | SCGB3A2 anti-fibrotic | Loss-of-function: worse bleomycin fibrosis | Primary; knockout |
| [12847263](https://pubmed.ncbi.nlm.nih.gov/12847263/) | UGRP1–MARCO ligand–receptor pair | Receptor identification, microbial binding | Primary; biochemical |
| [30526845](https://pubmed.ncbi.nlm.nih.gov/30526845/) | LPS uptake via syndecan-1 → pyroptosis | LPS chaperone mechanism + anti-cancer | Primary; mechanistic |
| [36796505](https://pubmed.ncbi.nlm.nih.gov/36796505/) | SCGB3A2 protects from emphysema | STAT3 → Serpina1a/A1AT axis; ChIP | Primary; knockout + transgenic + mechanism |
| [35016921](https://pubmed.ncbi.nlm.nih.gov/35016921/) | Kimura et al. review (2022) | Authoritative synthesis of all activities | Review |

**Supporting structural context.** Studies of related secretoglobins — uteroglobin's progesterone-binding hydrophobic cavity ([PMID: 7770456](https://pubmed.ncbi.nlm.nih.gov/7770456/)) and the calcium-binding, ligand-cavity-bearing uteroglobin-like fold of Fel d 1 ([PMID: 17543334](https://pubmed.ncbi.nlm.nih.gov/17543334/)) — support the inference that SCGB3A2's shared fold provides a ligand-binding cavity consistent with its LPS-chaperone role.

**Human genetics / translational context.** Human *UGRP1* lies at the asthma-linked 5q31 locus; a functional −112G/A promoter polymorphism that reduces transcription was associated with asthma in a Japanese population ([PMID: 11813133](https://pubmed.ncbi.nlm.nih.gov/11813133/)) and with allergic rhinitis in Singapore Chinese ([PMID: 21410962](https://pubmed.ncbi.nlm.nih.gov/21410962/)), though several other populations (Indian, Sicilian, German) found no association ([PMID: 15591807](https://pubmed.ncbi.nlm.nih.gov/15591807/), [PMID: 18201431](https://pubmed.ncbi.nlm.nih.gov/18201431/), [PMID: 12915772](https://pubmed.ncbi.nlm.nih.gov/12915772/)). These genetic data are consistent with — but do not by themselves establish — the anti-inflammatory function; their mixed results reflect population heterogeneity rather than contradicting the mechanistic mouse data. SCGB3A2 is also a candidate biomarker in lung adenocarcinoma ([PMID: 21937081](https://pubmed.ncbi.nlm.nih.gov/21937081/), [PMID: 29363881](https://pubmed.ncbi.nlm.nih.gov/29363881/)).

---

## Limitations and Knowledge Gaps

1. **No atomic structure of SCGB3A2 itself.** The ligand-binding cavity and the physical basis of LPS binding are inferred from homology to uteroglobin and Fel d 1, not from an experimental SCGB3A2 structure. A crystal or cryo-EM structure (apo and LPS-bound) would confirm the chaperone mechanism.

2. **Receptor usage is incompletely mapped.** MARCO and syndecan-1 are identified, but whether a dedicated signaling receptor mediates the STAT1/STAT3 and NF-κB effects — and how receptor choice is partitioned between the anti-inflammatory and pyroptotic outcomes — is unresolved. The signal that triggers STAT3 phosphorylation downstream of SCGB3A2 has not been traced to a specific receptor.

3. **Apparently opposing immune outputs.** SCGB3A2 is anti-inflammatory (NF-κB inhibition, ↓ eosinophils) yet pro-pyroptotic (caspase-11 activation with LPS). The context (LPS availability, cell type, receptor engaged) that dictates which program dominates is not fully defined.

4. **Molecular-weight / oligomerization details.** Reports cite ~10 kDa (monomer) and ~17 kDa (homodimeric secretory protein in early human work); clarifying the physiological oligomeric state in vivo and whether tetramers are functionally distinct from dimers remains open.

5. **Human vs. mouse translation.** Most mechanistic data are from mouse; human genetic associations are inconsistent across populations. The degree to which the mouse mechanisms (especially the STAT3→*SERPINA1*/A1AT axis and syndecan-1 LPS delivery) operate in human airways needs direct confirmation.

6. **Endogenous ligand spectrum.** Beyond LPS and microbial surfaces, the full repertoire of hydrophobic/lipid ligands that the secretoglobin cavity binds (e.g., phospholipids, steroids) has not been systematically characterized for SCGB3A2.

---

## Proposed Follow-up Experiments / Actions

1. **Determine the SCGB3A2 structure, apo and LPS-bound**, by X-ray crystallography or cryo-EM, and map LPS contacts by mutagenesis to test whether the secretoglobin cavity is the LPS-binding site.

2. **Define the signaling receptor(s) for the STAT3 arm.** Use proximity labeling (BioID/APEX) or affinity capture on lung fibroblasts/epithelial cells to identify the receptor upstream of SCGB3A2-induced STAT1/STAT3 phosphorylation, then validate with receptor knockdown/knockout and loss of A1AT induction.

3. **Dissect the anti-inflammatory vs. pyroptotic switch.** Titrate LPS and compare syndecan-1⁺ vs. syndecan-1⁻ and MARCO⁺ vs. MARCO⁻ cells to establish which receptor/context routes SCGB3A2 toward NF-κB inhibition versus caspase-11 pyroptosis.

4. **Test the STAT3→*Serpina1a* axis genetically in vivo.** Cross *Scgb3a2*-transgenic mice with *Stat3* or *Serpina1a* conditional alleles to confirm that A1AT induction is required for the anti-emphysema phenotype under cigarette-smoke exposure.

5. **Validate human translatability.** Measure SCGB3A2-dependent A1AT induction and syndecan-1–mediated LPS uptake in primary human airway epithelial cells and macrophages; correlate with human airway-disease outcomes.

6. **Characterize the ligand repertoire** of recombinant SCGB3A2 by lipidomic co-purification and biophysical binding assays to define substrate specificity of the chaperone cavity beyond LPS.

7. **Evaluate therapeutic potential** of recombinant SCGB3A2 (or stabilized dimer/tetramer) in preclinical models of asthma, COPD/emphysema, pulmonary fibrosis, and lung cancer, leveraging its convergent anti-inflammatory, tissue-protective, and anti-tumor activities.

---

## Conclusion

Mouse SCGB3A2/UGRP1 (Q920H1) is a small, secreted, NKX2-1–driven **secretoglobin of airway Club cells** whose primary molecular function is **ligand binding/chaperoning and receptor-mediated immunomodulation — not enzymatic catalysis or transport**. Acting extracellularly in the airway and alveolar space, it suppresses allergic inflammation by inhibiting NF-κB, promotes fetal lung development, protects alveolar structure from emphysema through a STAT1/STAT3 → α1-antitrypsin (*Serpina1a*) transcriptional axis, restrains fibrosis, and serves innate host-defense and anti-cancer functions by binding microbial surfaces (via MARCO) and chaperoning LPS into the cytosol (via syndecan-1) to trigger caspase-11 pyroptosis. These activities are well supported by convergent gain-of-function, loss-of-function (knockout), and mechanistic (ChIP, reporter, receptor-identification) evidence in mouse models, synthesized in a 2022 authoritative review.


## Artifacts

- [OpenScientist final report](Scgb3a2-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Scgb3a2-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:11682631
2. PMID:16456148
3. PMID:40865253
4. PMID:15626484
5. PMID:15531759
6. PMID:15485815
7. PMID:18535256
8. PMID:26559674
9. PMID:12847263
10. PMID:30526845
11. PMID:36796505
12. PMID:35016921
13. PMID:7770456
14. PMID:17543334
15. PMID:11813133
16. PMID:21410962
17. PMID:15591807
18. PMID:18201431
19. PMID:12915772
20. PMID:21937081
21. PMID:29363881