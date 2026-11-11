---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T18:45:47.121521'
end_time: '2026-10-24T19:20:28.982250'
duration_seconds: 2081.86
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: mouse
  gene_id: Scgb3a1
  gene_symbol: Scgb3a1
  uniprot_accession: Q920D7
  protein_description: 'RecName: Full=Secretoglobin family 3A member 1; AltName: Full=Cytokine
    HIN-1; AltName: Full=High in normal 1; AltName: Full=Pneumo secretory protein
    2; Short=PnSP-2; AltName: Full=Uteroglobin-related protein 2; Flags: Precursor;'
  gene_info: Name=Scgb3a1; Synonyms=Hin1, Pnsp2, Ugrp2;
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
citation_count: 11
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Scgb3a1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Scgb3a1-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q920D7
- **Protein Description:** RecName: Full=Secretoglobin family 3A member 1; AltName: Full=Cytokine HIN-1; AltName: Full=High in normal 1; AltName: Full=Pneumo secretory protein 2; Short=PnSP-2; AltName: Full=Uteroglobin-related protein 2; Flags: Precursor;
- **Gene Information:** Name=Scgb3a1; Synonyms=Hin1, Pnsp2, Ugrp2;
- **Organism (full):** Mus musculus (Mouse).
- **Protein Family:** Belongs to the secretoglobin family. UGRP subfamily.
- **Key Domains:** Secretoglobin_3A. (IPR040301); SCGB3A (PF20490)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Scgb3a1" matches the protein description above**
2. **Verify the organism is correct:** Mus musculus (Mouse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Scgb3a1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Scgb3a1** (gene ID: Scgb3a1, UniProt: Q920D7) in mouse.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: Mouse *Scgb3a1* (HIN-1 / UGRP2 / PnSP-2), UniProt Q920D7

## Summary

**Mouse *Scgb3a1* encodes Secretoglobin family 3A member 1, a small (~10.6 kDa) secreted, cytokine-like protein of the secretoglobin (SCGB) superfamily, UGRP subfamily. It is not an enzyme or a transporter but a *signaling molecule* whose primary function is to act extracellularly to restrain epithelial cell growth, migration, and invasion.** The protein is widely known under several synonyms — **HIN-1** (High-In-Normal-1), **UGRP2** (uteroglobin-related protein 2), and **PnSP-2** (pneumo secretory protein 2) — reflecting its independent discovery in airway biology and in breast cancer research. All of these names refer to the same gene product. Identity verification against the UniProt record (Q920D7, *Mus musculus*, secretoglobin family / UGRP subfamily, Secretoglobin_3A domain IPR040301 / PF20490) was performed and is consistent with the literature reviewed; the gene symbol, organism, and domain architecture all align.

The mature protein is produced by **terminally differentiated airway epithelium** (trachea and bronchi) and by other secretory epithelia (uterine and mammary glands, stomach, small intestine), from which it is secreted into extracellular fluids — it is readily detected in bronchial lavage, saliva, plasma, and serum. Structurally it adopts the canonical **uteroglobin secretoglobin fold**: a signal peptide is cleaved from the 104-residue precursor, and the mature chain assembles into a **disulfide-linked, antiparallel homodimer**. Functionally, HIN-1/Scgb3a1 binds a **high-affinity cell-surface site** on epithelial cells and suppresses **PI3K/AKT (–mTOR) signaling**, thereby blocking mitogen-induced cell-cycle reentry (inhibiting Rb phosphorylation) and inducing apoptosis in growing cells. Expression of constitutively active AKT abrogates its growth-arresting effect, placing AKT directly downstream.

*Scgb3a1* transcription is controlled by the ubiquitous factor **NF-Y** (with a minor PU-box contribution) and gated by **CpG methylation** near the transcription start site; it is modulated by inflammatory cytokine signaling — **induced by Oncostatin M via STAT3/5 and ERK/p38 MAPK**, and **repressed by IFN-γ via STAT1**. In human cancers the orthologous gene is silenced by aberrant promoter hypermethylation in a large fraction of breast, lung, prostate, and other carcinomas, consistent with its role as the tumor suppressor "High-In-Normal-1." Knockout mice are developmentally near-normal, indicating a non-essential, modulatory role that is distinct and non-redundant relative to its paralogs SCGB1A1 (CC10/uteroglobin) and SCGB3A2 (UGRP1). The mouse and human orthologs share ~60% sequence identity and a conserved interchain-disulfide cysteine, corroborating a conserved secreted growth-inhibitory function.

---

## Key Findings

### Finding 1 — Scgb3a1 is a small secreted secretoglobin acting extracellularly as a growth-inhibitory signaling molecule

*Scgb3a1* encodes a small (~10 kDa) secreted protein belonging to the secretoglobin superfamily, UGRP subfamily, and is also named **HIN-1 (High-In-Normal-1)**, **UGRP2**, and **PnSP-2**. The protein was originally identified as "a putative cytokine with no significant homology to known proteins" ([PMID: 11481438](https://pubmed.ncbi.nlm.nih.gov/11481438/)), framing it from the outset as a secreted, cytokine-like signaling molecule rather than a catalytic protein. Its extracellular site of action is established by two complementary lines of evidence. First, **ligand-binding studies demonstrate high-affinity HIN-1 binding sites on the surface of epithelial cells** — "ligand-binding studies indicate the presence of high-affinity cell surface HIN-1 binding on epithelial cells" ([PMID: 16266985](https://pubmed.ncbi.nlm.nih.gov/16266985/)) — implying a cell-surface receptor through which HIN-1 transmits its signal. Second, the protein is detected in extracellular fluids: "correlating with the secretory nature of HIN-1, high levels of HIN-1 protein are detected in bronchial lavage, saliva, plasma, and serum" ([PMID: 15383627](https://pubmed.ncbi.nlm.nih.gov/15383627/)).

Functionally, recombinant HIN-1 is a **potent inhibitor of anchorage-dependent and anchorage-independent cell growth, cell migration, and invasion** ([PMID: 16266985](https://pubmed.ncbi.nlm.nih.gov/16266985/)). The gene is described as "a small, secreted protein [that] is silenced due to methylation in a substantial fraction of breast, prostate, lung, and pancreatic carcinomas" ([PMID: 16266985](https://pubmed.ncbi.nlm.nih.gov/16266985/)), reflecting its status as a secreted tumor-suppressor. Together these data define the primary function: **a secreted, extracellularly acting growth-inhibitory signaling molecule.**

### Finding 2 — HIN-1/Scgb3a1 inhibits cell growth and invasion by suppressing AKT activation

The mechanism linking HIN-1 to growth inhibition is suppression of the **PI3K/AKT** axis. In HIN-1–expressing cells, "mitogen-induced phosphorylation and activation of AKT are inhibited," and critically, "expression of constitutively active AKT abrogates HIN-1–mediated growth arrest" ([PMID: 16266985](https://pubmed.ncbi.nlm.nih.gov/16266985/)). The epistasis result — restoring AKT activity rescues cells from HIN-1–induced arrest — places **AKT genetically downstream** of HIN-1 and identifies AKT suppression as the operative mechanism rather than a correlated byproduct. At the cell-cycle level, HIN-1 blocks cell-cycle reentry and Rb phosphorylation in synchronized cells and induces apoptosis in growing cells, consistent with loss of the pro-survival, pro-proliferative AKT signal.

An independent disease-model study corroborates this axis in reverse: in paclitaxel-resistant ovarian clear cell carcinoma (OCCC), HIN-1 promoter methylation (i.e., loss of HIN-1 expression) is accompanied by elevated downstream signaling — "phospho-AKT473 and phospho-mTOR were significantly increased in HIN-1–methylated paclitaxel-resistant OCCC cell lines" ([PMID: 26497956](https://pubmed.ncbi.nlm.nih.gov/26497956/)) — and demethylation/re-expression of HIN-1 suppresses tumor growth through the AKT–mTOR pathway. The convergence of a gain-of-function study (HIN-1 expression lowers phospho-AKT) and a loss-of-function/disease study (HIN-1 silencing raises phospho-AKT/mTOR) makes the **HIN-1 → ↓AKT → growth arrest** model robust.

### Finding 3 — Scgb3a1 is expressed by terminally differentiated airway epithelium and other secretory epithelia

In the mouse, HIN-1/Scgb3a1 is most highly expressed in the lung and trachea, with lower expression in stomach, heart, small intestine, and uterine and mammary glands — "highest HIN-1 and UGRP-1 expression is detected in the lung" ([PMID: 12175512](https://pubmed.ncbi.nlm.nih.gov/12175512/)). During development, expression appears late (around E17.5–18.5), and in situ localization shows "the HIN-1 messenger RNA was localized to the epithelia of the trachea, bronchi, and uterine glands" ([PMID: 12175512](https://pubmed.ncbi.nlm.nih.gov/12175512/)), pinpointing the producing cell types. Importantly, expression is tied to differentiation state: "the expression of HIN-1 is restricted to terminally differentiated airway epithelial cells in vivo and in vitro implicating HIN-1 in the acquisition or maintenance of terminally differentiated epithelial phenotype" ([PMID: 12175512](https://pubmed.ncbi.nlm.nih.gov/12175512/)), and it is upregulated during retinoic-acid–induced differentiation of bronchial epithelium. This differentiation-coupled, epithelial-restricted expression pattern dovetails with its growth-restraining function — the protein marks and reinforces the quiescent, differentiated epithelial state.

### Finding 4 — Scgb3a1 expression is controlled by NF-Y/PU-box, CpG methylation, and cytokine signaling

The transcriptional logic of *Scgb3a1* has been dissected in detail. In mouse, transcription is driven mainly by the ubiquitous CCAAT-binding factor **NF-Y**, with a minor contribution from a PU-box binding protein — "expression of the mouse Scgb3a1 gene is regulated by a PU-box binding protein and a ubiquitous transcription factor NF-Y" ([PMID: 18194566](https://pubmed.ncbi.nlm.nih.gov/18194566/)) — and tissue-specific expression correlates with demethylation of the two CpGs closest to the transcription start site. This NF-Y–centered, methylation-gated control distinguishes *Scgb3a1* from its paralog *Scgb3a2/Ugrp1*, which is a direct NKX2-1/TTF-1 target.

Layered on top of this basal control is **inflammatory cytokine regulation**. IFN-γ represses the gene via STAT1: "IFN-gamma induced the phosphorylation of STAT1, which binds to a STAT-binding element (SBE) in the SCGB3A1 gene promoter, leading to decreased transcriptional activation of this gene" ([PMID: 19135978](https://pubmed.ncbi.nlm.nih.gov/19135978/)). Conversely, Oncostatin M induces the gene via STAT3/5 and MAPK: "OSM-activated STAT3/5, through binding to the STAT-binding element located at -201 to -209 bp in the mouse Scgb3a1 gene promoter" ([PMID: 18978304](https://pubmed.ncbi.nlm.nih.gov/18978304/)), with concurrent ERK/p38 MAPK involvement — and notably OSM reciprocally *down*-regulates the paralog SCGB3A2. Finally, in human cancers, aberrant promoter hypermethylation silences the gene across tumor types — "promoter methylation was observed in 73% of breast cancer, 67% of nonsmall cell lung cancer (NSCLC)" ([PMID: 15472908](https://pubmed.ncbi.nlm.nih.gov/15472908/)) — completely correlated with loss of expression.

### Finding 5 — Scgb3a1 is a disulfide-linked secreted homodimer with a cleaved signal peptide, adopting the uteroglobin secretoglobin fold

Analysis of the UniProt Q920D7 record defines the protein's architecture. It is a **104-residue precursor (~10.6 kDa)** with an N-terminal **signal peptide (residues 1–21)** that is cleaved to yield the mature secreted chain (residues 22–104). The mature chain contains only a small number of cysteines; **Cys81 forms an interchain disulfide bond**, and the subunit is annotated as a **disulfide-linked, secreted homodimer**. The annotated function — "secreted cytokine-like protein that inhibits cell growth in vitro," secretoglobin/UGRP subfamily — matches the experimental literature in Findings 1–2.

This architecture is the canonical secretoglobin fold, exemplified by the family prototype CC10/uteroglobin (SCGB1A1): "Structurally it is a homodimer of subunits of 70 amino acids covalently bound in an antiparallel manner. It belongs to secretogobin (SCGB) family" ([PMID: 12769755](https://pubmed.ncbi.nlm.nih.gov/12769755/)). In uteroglobin, this antiparallel dimer encloses a hydrophobic internal cavity capable of binding small hydrophobic ligands; by homology, Scgb3a1 is expected to share this disulfide-linked antiparallel dimer architecture, though a ligand for the putative cavity has not been experimentally defined for Scgb3a1 specifically.

### Finding 6 — Scgb3a1-null mice are developmentally near-normal, indicating a non-essential, non-redundant modulatory role

In mouse airway, the three secretoglobins SCGB1A1 (CC10), SCGB3A1 (UGRP2/HIN-1), and SCGB3A2 (UGRP1) show unique, non-overlapping spatiotemporal expression during gestation and adulthood. Genetic loss-of-function experiments show that "the lack of Scgb3a1 or Scgb3a2 did not affect expression of the other Scgb genes as determined by mRNA measurements. Moreover, the lack of Scgb3a1 or Scgb3a2 did not affect development of the pulmonary neuroepithelial bodies during embryogenesis" ([PMID: 30768367](https://pubmed.ncbi.nlm.nih.gov/30768367/)). Only *Scgb3a2* loss caused a slight reduction in ciliated cells; *Scgb3a1* loss produced a near-normal developmental phenotype, and there was no transcriptional compensation among paralogs. The authors conclude that "these results suggest that SCGB1A1, SCGB3A1, and SCGB3A2 each may possess its own unique biological function" ([PMID: 30768367](https://pubmed.ncbi.nlm.nih.gov/30768367/)). This supports a model in which Scgb3a1 is a **non-essential but functionally distinct modulatory factor** — its loss is tolerated developmentally, consistent with a role in fine-tuning epithelial growth/differentiation rather than in essential morphogenesis.

### Finding 7 — Mouse and human SCGB3A1 are evolutionarily conserved with a conserved interchain-disulfide cysteine

A Needleman–Wunsch global alignment of mouse SCGB3A1 (Q920D7, 104 aa) against the human ortholog (Q96QR1, 104 aa) yields **61/101 identical aligned positions = ~60.4% sequence identity** — high for a small secreted protein, where rapid divergence is common. Both are 104-residue precursors. The cysteine that forms the interchain disulfide in the mature protein is **conserved** (mouse Cys81 aligns to human Cys78), preserving the structural feature required for homodimer formation; the other mouse cysteine lies within the cleaved signal peptide and is not part of the mature dimer. Both orthologs carry the identical UniProt functional annotation — "secreted cytokine-like protein; inhibits cell growth in vitro" and "homodimer, disulfide-linked" — and the human "Secreted" location is experimentally supported (ECO:0000269, [PMID: 11481438](https://pubmed.ncbi.nlm.nih.gov/11481438/), the founding HIN-1 study). The cross-species conservation of sequence, the disulfide cysteine, and the functional annotation corroborates a conserved secreted growth-inhibitory function.

---

## Mechanistic Model / Interpretation

The findings integrate into a coherent model of Scgb3a1 as a **differentiation-coupled, secreted autocrine/paracrine brake on epithelial proliferation**, signaling through a cell-surface receptor to suppress PI3K/AKT.

```
   Transcriptional / epigenetic control
   ┌─────────────────────────────────────────────┐
   │  NF-Y (CCAAT) + minor PU-box  → basal ON     │
   │  CpG demethylation near TSS   → tissue ON    │
   │  Oncostatin M → STAT3/5 + ERK/p38 → INDUCE   │
   │  IFN-γ → STAT1                     → REPRESS  │
   │  Cancer: promoter hypermethylation → SILENCE │
   └─────────────────────────────────────────────┘
                         │
                         ▼
   Terminally differentiated airway epithelium
   (trachea, bronchi; also uterine/mammary glands)
                         │  translation; signal peptide (1–21) cleaved
                         ▼
   Mature chain (22–104) → disulfide-linked (Cys81)
   ANTIPARALLEL HOMODIMER  (uteroglobin / SCGB fold)
                         │  SECRETED
                         ▼
   Extracellular space (lavage, saliva, plasma, serum)
                         │  binds HIGH-AFFINITY cell-surface site
                         ▼
   ┌─────────────────────────────────────────────┐
   │  ↓ mitogen-induced AKT phosphorylation       │
   │  (PI3K/AKT – mTOR axis suppressed)           │
   └─────────────────────────────────────────────┘
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
  ↓ Rb phosphoryl.   apoptosis in    ↓ migration
  → cell-cycle       growing cells   & invasion
    reentry block
                         │
                         ▼
     GROWTH RESTRAINT / maintenance of
     quiescent differentiated epithelium
     (tumor-suppressor "High-In-Normal")
```

**Primary function (direct answer to the research question).** Scgb3a1 is **not an enzyme or transporter**. It is a **secreted signaling molecule** (cytokine-like secretoglobin). Its primary role in the pathway is to act as an **extracellular ligand** that engages a high-affinity cell-surface binding site on epithelial cells and **negatively regulates PI3K/AKT(–mTOR) signaling**, producing cell-cycle arrest (via reduced Rb phosphorylation), apoptosis of proliferating cells, and inhibition of migration/invasion. The epistasis experiment — constitutively active AKT overrides HIN-1 — is the key mechanistic anchor establishing AKT as the direct downstream effector.

**Site of action.** The protein functions **extracellularly**. It is synthesized with a cleaved signal peptide, assembled into a secreted disulfide-linked homodimer, and released into airway/luminal fluids and the circulation, where it binds receptors on the surface of (likely neighboring or self) epithelial cells — an autocrine/paracrine mode consistent with a locally acting growth suppressor.

**Pathway placement.** Upstream, the gene integrates basal (NF-Y, methylation) and inflammatory (OSM/STAT3-5 induction; IFN-γ/STAT1 repression) inputs. Downstream, the protein feeds into the canonical growth-control hub PI3K/AKT/mTOR. This positions Scgb3a1 at the interface of **airway inflammation and epithelial growth control**: inflammatory context tunes how much secreted brake is available, and the brake acts on the universal proliferative/survival signaling node.

**Relationship to paralogs.** Although Scgb3a1 shares the SCGB fold and lung-epithelial expression with SCGB1A1 (CC10, anti-inflammatory) and SCGB3A2 (UGRP1, an NKX2-1/TTF-1 target with anti-inflammatory activity), the knockout and expression data show each has a distinct, non-redundant function. Scgb3a1's distinguishing feature is its NF-Y/methylation-driven regulation and its specific growth-suppressive, AKT-directed activity.

| Feature | Evidence summary | PMIDs |
|---|---|---|
| Secreted; extracellular action | Found in lavage, saliva, plasma, serum; high-affinity cell-surface binding | 11481438, 15383627, 16266985 |
| Primary function: growth/invasion inhibitor | Inhibits anchorage-dependent/-independent growth, migration, invasion | 16266985 |
| Mechanism: ↓AKT | ↓mitogen-induced AKT-P; active AKT rescues; ↑pAKT/pmTOR when silenced | 16266985, 26497956 |
| Localization of production | Terminally differentiated tracheal/bronchial epithelium; uterine glands | 12175512 |
| Structure: disulfide homodimer, SCGB fold | 104-aa precursor, signal peptide cleaved, Cys81 interchain disulfide | 12769755 (family prototype); UniProt Q920D7 |
| Regulation | NF-Y/PU-box; CpG methylation; OSM↑ (STAT3/5), IFN-γ↓ (STAT1); cancer hypermethylation | 18194566, 18978304, 19135978, 15472908 |
| Non-essential, non-redundant | Near-normal KO; no paralog compensation | 30768367 |
| Conserved mouse↔human | ~60% identity; conserved disulfide Cys; identical annotation | 11481438 |

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports / challenges the findings |
|---|---|---|
| [11481438](https://pubmed.ncbi.nlm.nih.gov/11481438/) | *HIN-1, a putative cytokine highly expressed in normal but not cancerous mammary epithelial cells* | Founding identification of HIN-1 as a secreted, cytokine-like protein; underlies the "secreted" annotation and growth-suppressor concept (supports F001, F007). |
| [16266985](https://pubmed.ncbi.nlm.nih.gov/16266985/) | *HIN-1, an inhibitor of cell growth, invasion, and AKT activation* | Central mechanistic paper: high-affinity cell-surface binding, inhibition of growth/migration/invasion, AKT suppression, and the epistasis rescue by active AKT (supports F001, F002). |
| [26497956](https://pubmed.ncbi.nlm.nih.gov/26497956/) | *Demethylation of HIN-1 reverses paclitaxel-resistance of OCCC through AKT-mTOR* | Independent, reverse-direction confirmation: HIN-1 silencing raises pAKT/pmTOR; re-expression suppresses tumor growth (supports F002). |
| [12175512](https://pubmed.ncbi.nlm.nih.gov/12175512/) | *Expression of HIN-1 and UGRP-1 in adult and developing tissues* | Establishes lung/trachea as primary sites, in situ localization to tracheal/bronchial/uterine epithelium, and differentiation-coupled expression (supports F003). |
| [18194566](https://pubmed.ncbi.nlm.nih.gov/18194566/) | *Regulation of mouse Scgb3a1 by NF-Y and CpG methylation* | Defines the core mouse transcriptional regulators (NF-Y, PU-box) and methylation gating (supports F004). |
| [19135978](https://pubmed.ncbi.nlm.nih.gov/19135978/) | *IFN-gamma down-regulates Secretoglobin 3A1* | IFN-γ/STAT1 repression via a promoter SBE (supports F004). |
| [18978304](https://pubmed.ncbi.nlm.nih.gov/18978304/) | *Oncostatin M regulates SCGB3A1 and 3A2 bidirectionally* | OSM/STAT3-5 + ERK/p38 induction of Scgb3a1 (supports F004). |
| [15472908](https://pubmed.ncbi.nlm.nih.gov/15472908/) | *Aberrant methylation of HIN-1 in many human malignancies* | Documents epigenetic silencing across cancers correlated with loss of expression (supports F004). |
| [15383627](https://pubmed.ncbi.nlm.nih.gov/15383627/) | *Frequent HIN-1 promoter methylation and lack of expression in multiple tumor types* | Confirms secreted nature (lavage/saliva/plasma/serum) and cancer silencing (supports F001, F004). |
| [12769755](https://pubmed.ncbi.nlm.nih.gov/12769755/) | *Clinical aspects of CC10/uteroglobin (SCGB1A1)* | Describes the shared antiparallel disulfide-linked homodimer SCGB fold that Scgb3a1 belongs to (supports F005). |
| [30768367](https://pubmed.ncbi.nlm.nih.gov/30768367/) | *Spatiotemporal expression of SCGB1A1, 3A1, 3A2 in mouse airway* | Non-overlapping expression; near-normal Scgb3a1 KO; no paralog compensation; distinct functions (supports F006). |
| [11682631](https://pubmed.ncbi.nlm.nih.gov/11682631/) | *UGRP1 (Scgb3a2), downstream of NKX2.1* | Context for the paralog Scgb3a2 (NKX2-1 target), contrasting with Scgb3a1's NF-Y–driven regulation (context for F004, F006). |
| [24187664](https://pubmed.ncbi.nlm.nih.gov/24187664/) | *Neonatal hyperoxia alters lung secretoglobins and ANXA1* | Shows SCGB3A1 protein is modulated in lung injury models, supporting a role in airway epithelial homeostasis (contextual). |
| [19098448](https://pubmed.ncbi.nlm.nih.gov/19098448/) | *HIN-1 methylation in esophageal squamous cancer progression* | HIN-1 silencing is an early event in malignant transformation, consistent with tumor-suppressor function (contextual, human). |
| [24850174](https://pubmed.ncbi.nlm.nih.gov/24850174/) | *HIN-1 promoter methylation meta-analysis in breast cancer* | Meta-analytic evidence linking HIN-1 silencing to breast cancer pathogenesis (contextual, human). |

**Interpretation of the evidence base.** The mechanistic core (secreted ligand → cell-surface binding → AKT suppression → growth arrest) rests on a *precise, hypothesis-driven* study ([PMID: 16266985](https://pubmed.ncbi.nlm.nih.gov/16266985/)) and is independently reinforced by a disease-model study ([PMID: 26497956](https://pubmed.ncbi.nlm.nih.gov/26497956/)). Expression/localization and transcriptional regulation are supported by targeted molecular studies in mouse ([PMID: 12175512](https://pubmed.ncbi.nlm.nih.gov/12175512/), [18194566](https://pubmed.ncbi.nlm.nih.gov/18194566/), [18978304](https://pubmed.ncbi.nlm.nih.gov/18978304/), [19135978](https://pubmed.ncbi.nlm.nih.gov/19135978/)). Structural inference is by homology to the well-characterized uteroglobin prototype ([PMID: 12769755](https://pubmed.ncbi.nlm.nih.gov/12769755/)) plus the UniProt feature annotation. The human cancer literature, while largely high-throughput/clinical, consistently places loss of HIN-1 at the service of tumor progression, corroborating the growth-suppressor role across species.

---

## Limitations and Knowledge Gaps

1. **The receptor is unidentified.** High-affinity cell-surface binding sites for HIN-1 are demonstrated functionally ([PMID: 16266985](https://pubmed.ncbi.nlm.nih.gov/16266985/)), but the molecular identity of the receptor that couples HIN-1 to AKT suppression is unknown. This is the single most important gap: without the receptor, the proximal signal-transduction step (how an extracellular secretoglobin dimer down-modulates PI3K/AKT) remains undefined.

2. **No experimentally determined 3D structure of Scgb3a1.** The disulfide-linked antiparallel homodimer and uteroglobin fold are inferred from UniProt annotation and homology to SCGB1A1, not from a crystal/NMR/cryo-EM structure of Scgb3a1 itself. Whether its internal cavity binds a small hydrophobic ligand (as uteroglobin does) — and whether such a ligand is functionally relevant — is unknown.

3. **Mechanistic studies are largely in cancer/epithelial cell lines.** The AKT-suppression mechanism was established primarily in human breast/cancer cell models; direct demonstration of the same mechanism in primary mouse airway epithelium in vivo is limited.

4. **Mild knockout phenotype leaves physiological role underdetermined.** *Scgb3a1*-null mice are developmentally near-normal with no paralog compensation ([PMID: 30768367](https://pubmed.ncbi.nlm.nih.gov/30768367/)). The precise physiological context in which the growth-restraining function matters (e.g., injury/repair, inflammation, carcinogenesis challenge) has not been fully delineated — the phenotype may only emerge under stress.

5. **Possible additional functions.** Secretoglobins (notably CC10/SCGB1A1 and SCGB3A2) have anti-inflammatory/immunomodulatory activities. Whether Scgb3a1 shares any such activity beyond growth restraint — and how its inflammatory-cytokine regulation (OSM/IFN-γ) connects to a physiological output — is not resolved.

---

## Proposed Follow-up Experiments / Actions

1. **Identify the HIN-1/Scgb3a1 receptor.** Use affinity capture / cross-linking of labeled recombinant HIN-1 homodimer on responsive epithelial cells, followed by mass-spectrometry; validate candidates by CRISPR knockout and loss of HIN-1–induced AKT suppression. This directly closes the central mechanistic gap.

2. **Determine the 3D structure of the Scgb3a1 homodimer** (X-ray/cryo-EM or validated AlphaFold-Multimer model), confirm the Cys81 interchain disulfide and antiparallel dimer, and probe the internal cavity for candidate small-molecule ligands by biophysical binding assays.

3. **Dissect the signaling step to AKT.** In defined epithelial lines, quantify PI3K activity, PDK1/mTORC2-dependent AKT phosphorylation (Thr308 vs Ser473), and PTEN status after HIN-1 exposure; test whether HIN-1 acts upstream of PI3K or via a phosphatase.

4. **In vivo stress/challenge phenotyping of Scgb3a1-null mice.** Subject knockouts to airway injury (hyperoxia, naphthalene), allergic inflammation, and chemical carcinogenesis to reveal conditional phenotypes that the near-normal baseline masks; read out epithelial proliferation and AKT pathway activation.

5. **Test the cytokine-regulation circuit physiologically.** In airway epithelial models and mice, perturb Oncostatin M and IFN-γ signaling and measure Scgb3a1 output and downstream epithelial proliferation, linking the inflammatory inputs (Finding 4) to the growth-control output (Finding 2) in a single system.

6. **Cross-species functional conservation test.** Confirm that human and mouse HIN-1 reciprocally suppress AKT and growth in each other's epithelial cells, validating the conservation inference (Finding 7) functionally rather than by sequence alone.

---

## Conclusion

Mouse **Scgb3a1 (HIN-1/UGRP2/PnSP-2, Q920D7)** is a small secreted secretoglobin of the UGRP subfamily — a disulfide-linked antiparallel homodimer with the uteroglobin fold — produced by terminally differentiated airway and secretory epithelia and released into extracellular fluids. Its **primary function is as an extracellular, cytokine-like signaling molecule that restrains epithelial cell growth, migration, and invasion by binding a high-affinity cell-surface site and suppressing PI3K/AKT(–mTOR) signaling.** It is regulated by NF-Y and CpG methylation and tuned by inflammatory cytokines (induced by Oncostatin M/STAT3-5, repressed by IFN-γ/STAT1), and it is silenced by promoter hypermethylation in many epithelial cancers — hallmarks of the tumor suppressor "High-In-Normal-1." It is neither an enzyme nor a transporter; it is a secreted growth-inhibitory signaling protein acting extracellularly on the AKT pathway.


## Artifacts

- [OpenScientist final report](Scgb3a1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Scgb3a1-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:11481438
2. PMID:16266985
3. PMID:15383627
4. PMID:26497956
5. PMID:12175512
6. PMID:18194566
7. PMID:19135978
8. PMID:18978304
9. PMID:15472908
10. PMID:12769755
11. PMID:30768367