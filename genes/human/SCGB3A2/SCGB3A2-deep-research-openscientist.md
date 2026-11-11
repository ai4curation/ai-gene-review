---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T18:45:47.231621'
end_time: '2026-10-24T18:59:34.419899'
duration_seconds: 827.19
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: SCGB3A2
  gene_symbol: SCGB3A2
  uniprot_accession: Q96PL1
  protein_description: 'RecName: Full=Secretoglobin family 3A member 2; AltName: Full=Pneumo
    secretory protein 1; Short=PnSP-1; AltName: Full=Uteroglobin-related protein 1;
    Flags: Precursor;'
  gene_info: Name=SCGB3A2; Synonyms=PNSP1, UGRP1; ORFNames=UNQ566/PRO1128;
  organism_full: Homo sapiens (Human).
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
citation_count: 24
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: SCGB3A2-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: SCGB3A2-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q96PL1
- **Protein Description:** RecName: Full=Secretoglobin family 3A member 2; AltName: Full=Pneumo secretory protein 1; Short=PnSP-1; AltName: Full=Uteroglobin-related protein 1; Flags: Precursor;
- **Gene Information:** Name=SCGB3A2; Synonyms=PNSP1, UGRP1; ORFNames=UNQ566/PRO1128;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the secretoglobin family. UGRP subfamily.
- **Key Domains:** Secretoglobin_3A. (IPR040301); SCGB3A (PF20490)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SCGB3A2" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SCGB3A2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SCGB3A2** (gene ID: SCGB3A2, UniProt: Q96PL1) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# SCGB3A2 (Secretoglobin family 3A member 2 / UGRP1 / PnSP-1): A Functional Annotation Report

**Gene:** SCGB3A2 (synonyms: *PNSP1*, *UGRP1*; ORF names *UNQ566/PRO1128*)
**UniProt:** Q96PL1 · **Organism:** *Homo sapiens* (Human)
**Protein family:** Secretoglobin family, UGRP subfamily · **Domain:** Secretoglobin_3A (IPR040301); SCGB3A (PF20490)

---

## Identity Verification

The research target was verified against the UniProt record before and throughout the investigation. The gene symbol **SCGB3A2** corresponds unambiguously to the human **Secretoglobin family 3A member 2**, also widely known in the literature as **uteroglobin-related protein 1 (UGRP1)** and **pneumo secretory protein 1 (PnSP-1)**. All literature retrieved — spanning lung development, airway inflammation, pulmonary fibrosis, emphysema, and innate immunity — is consistently about this protein (human and its mouse ortholog *Scgb3a2*), and the described biochemistry (small secreted secretoglobin, ~10 kDa disulfide-linked homodimer, phospholipase A2 inhibition) matches the UniProt family/domain annotation (secretoglobin family, UGRP subfamily). No conflicting "same-symbol, different-gene" literature was encountered. **The identification is confirmed; research proceeded on the correct gene.** Much causal mechanism derives from the mouse ortholog, which is appropriate given high conservation and the fact that human recombinant protein reproduces the key activities.

---

## Summary

**SCGB3A2 is a small (~10 kDa), secreted, disulfide-linked homodimeric secretoglobin produced almost exclusively by airway epithelial Club (Clara) cells and submucosal-gland serous cells, and released into the airway surface liquid where it carries out its function extracellularly. It is not an enzyme or a transporter.** Its defining, quantitatively measured biochemical activity is **inhibition of phospholipase A2 (PLA2, including the secretory group IB enzyme PLA2G1B)** — an activity it shares with the prototype secretoglobin uteroglobin/SCGB1A1 and which provides a direct mechanistic basis for its anti-inflammatory and anti-fibrotic effects by limiting liberation of arachidonic acid and downstream eicosanoid/lipid mediators ([PMID: 24213919](https://pubmed.ncbi.nlm.nih.gov/24213919/)).

Beyond its PLA2-inhibitory biochemistry, SCGB3A2 behaves as a multifunctional extracellular signaling/ligand molecule. It engages at least two defined cell-surface receptors: the alveolar-macrophage scavenger receptor **MARCO** (macrophage receptor with collagenous structure), identified by expression cloning as a bona fide SCGB3A2/UGRP1 receptor ([PMID: 12847263](https://pubmed.ncbi.nlm.nih.gov/12847263/)), and **podoplanin (PDPN)**, through which it can drive an NF-κB inflammatory program during *Streptococcus pneumoniae* infection ([PMID: 35652821](https://pubmed.ncbi.nlm.nih.gov/35652821/)). Downstream, it activates **STAT1/STAT3** signaling, where STAT3 homodimers induce the cytoprotective anti-protease **α1-antitrypsin (A1AT/SERPINA1)** ([PMID: 36796505](https://pubmed.ncbi.nlm.nih.gov/36796505/)). It also functions as a **developmental growth/differentiation factor** acting downstream of the master lung transcription factor **NKX2-1 (TTF-1)** to promote bronchial branching and fetal lung maturation ([PMID: 18535256](https://pubmed.ncbi.nlm.nih.gov/18535256/)).

In vivo loss- and gain-of-function mouse studies converge on a tissue-protective role: *Scgb3a2*-null mice develop worse bleomycin-induced fibrosis, more severe cigarette-smoke emphysema, and aging-related emphysematous/lymphoma-like lesions, whereas transgenic or recombinant SCGB3A2 protects the lung and accelerates fibrosis resolution. Its biological activity has been mapped to the **C-terminal region** of the mature protein. Collectively, SCGB3A2 is best described as a **secreted airway-protective secretoglobin whose core biochemistry is PLA2 inhibition / lipid sequestration, coupled to receptor-mediated (MARCO, PDPN) and STAT-dependent signaling and to NKX2-1-driven lung-maturation activity.**

---

## Key Findings

### Finding 1 — A small secreted anti-inflammatory secretoglobin produced by airway Club cells

SCGB3A2 is a ~10 kDa secreted protein that forms dimers and higher-order tetramers and is predominantly expressed by airway epithelial **Club (Clara) cells**, from which it is secreted into the airway lumen. Structurally and genetically it is closely related to SCGB1A1 (CC10/uteroglobin), the founding member of the secretoglobin superfamily. A comprehensive review states that *"SCGB3A2 is a small secretory protein of ~10 kDa that forms a dimer and a tetramer. SCGB3A2 is predominantly expressed in airway epithelial Club cells, and has anti-inflammatory, growth factor, anti-fibrotic, and anti-cancer activities that influence various lung diseases"* ([PMID: 35016921](https://pubmed.ncbi.nlm.nih.gov/35016921/)).

Its anti-inflammatory activity is directly demonstrated in vivo. In an ovalbumin (OVA)-induced allergic airway inflammation model, *"intranasal administration of adeno-UGRP1 successfully delivered UGRP1 to the epithelial cells of airways and markedly reduced the number of infiltrating inflammatory cells, particularly eosinophils, in lung tissue as well as the level of proinflammatory cytokines such as interleukin (IL)-4, IL-5, and IL-13 in bronchoalveolar lavage fluids"* ([PMID: 16456148](https://pubmed.ncbi.nlm.nih.gov/16456148/)). This establishes a causal, protein-level anti-inflammatory function in Th2-skewed airway disease, with suppression of the eosinophil-driving cytokine axis (IL-4/IL-5/IL-13). Consistent with its secretory, airway-restricted biology, UGRP1 is detectable at high concentrations in sputum, bronchoalveolar lavage fluid, and amniotic fluid, and at much lower levels in serum/urine, paralleling the Clara cell protein and supporting its use as a **biomarker of respiratory epithelial integrity** ([PMID: 20843168](https://pubmed.ncbi.nlm.nih.gov/20843168/)).

### Finding 2 — An NKX2-1 target that acts as a growth/differentiation factor promoting fetal lung maturation

SCGB3A2 was originally discovered as a downstream transcriptional target of the homeodomain transcription factor **NKX2-1 (TTF-1)** in the lung: *"Secretoglobin 3A2 (SCGB3A2) was originally identified as a downstream target in lung for the homeodomain transcription factor NKX2-1, whose null mutation resulted in severely hypoplastic lungs"* ([PMID: 18535256](https://pubmed.ncbi.nlm.nih.gov/18535256/)). Its expression is developmentally regulated — very low in early gestation (E11.5), rising sharply by mid-to-late gestation (E16.5) during mouse lung morphogenesis.

Critically, SCGB3A2 is not merely a marker but an **active growth factor**: *"SCGB3A2 significantly promoted both early and late stages of lung dev[elopment]"* ex vivo and in vivo, including bronchial branching morphogenesis and functional maturation reflected in surfactant/phospholipid profiles ([PMID: 18535256](https://pubmed.ncbi.nlm.nih.gov/18535256/)). This places SCGB3A2 within the NKX2-1 regulatory module that also controls surfactant proteins — a module so conserved that ectopic NKX2-1 expression reactivates SCGB3A2/surfactant genes in gastric adenocarcinoma of fundic-gland type ([PMID: 36094595](https://pubmed.ncbi.nlm.nih.gov/36094595/)).

### Finding 3 — Signals through STAT3 to drive cytoprotective transcription and engages MARCO on macrophages

Mechanistically, SCGB3A2 is an upstream activator of the JAK/STAT pathway in lung stromal and epithelial cells. In mouse lung fibroblast-derived MLg cells and epithelial MLE-15 cells, *"SCGB3A2 increased the expression and phosphorylation of signal transducers and activators of transcription (STAT)1 and STAT3, and the expression of α1-antitrypsin (A1AT)"* ([PMID: 36796505](https://pubmed.ncbi.nlm.nih.gov/36796505/)). The signaling is specific at the level of STAT3 dimer biology: *"STAT3 formed a homodimer when cells were stimulated with SCGB3A2"*, and this homodimer binds the *Serpina1a* (A1AT) gene to transactivate it; A1AT induction is STAT3-dependent — abolished by *Stat3* knockdown and enhanced by STAT3 overexpression ([PMID: 36796505](https://pubmed.ncbi.nlm.nih.gov/36796505/)). Because A1AT is a major anti-protease that protects alveolar matrix from neutrophil elastase, this axis directly links SCGB3A2 signaling to protection against protease-driven tissue destruction (emphysema).

At the cellular-niche level, single-cell/omics analyses of chronic obstructive pulmonary disease (COPD) show coordinated upregulation of SCGB3A2 and its macrophage receptor MARCO: *"enhanced expression of secretoglobin 3A2 (SCGB3A2) and macrophage receptor with collagenous structure (MARCO) across epithelial secretory cells and interstitial macrophages"*, with MARCO activation associated with anti-inflammatory interstitial macrophage phenotypes ([PMID: 41071173](https://pubmed.ncbi.nlm.nih.gov/41071173/)). This positions SCGB3A2 as the secreted epithelial ligand of an epithelial→macrophage anti-inflammatory signaling axis.

### Finding 4 — Anti-fibrotic and tissue-protective in vivo; activity maps to the C-terminal region

In vivo genetic and pharmacological experiments establish SCGB3A2 as tissue-protective. *Scgb3a2*-null mice develop **more severe bleomycin-induced pulmonary fibrosis**: investigators *"demonstrated that BLM-treated Scgb3a2-null mouse lungs had more severe fibrosis than those of wild-type mouse lungs"* (higher Ashcroft scores, hydroxyproline, collagen mRNAs, TGF-β and Th2 cytokines) ([PMID: 26559674](https://pubmed.ncbi.nlm.nih.gov/26559674/)). Conversely, transgenic SCGB3A2 overexpression accelerates resolution of bleomycin fibrosis ([PMID: 26178733](https://pubmed.ncbi.nlm.nih.gov/26178733/)).

In the cigarette-smoke emphysema model, *"The KO mice showed loss of lung structure under control condition, and CS exposure resulted in more expansion of airspace and destruction of alveolar wall than WT mouse lungs. In contrast, TG mouse lungs showed no significant changes after CS exposure"* ([PMID: 36796505](https://pubmed.ncbi.nlm.nih.gov/36796505/)). *Scgb3a2*-KO mice also develop aggravated **aging-related emphysematous and lymphoma-like lesions**, with declining surfactant-protein expression and altered immune-gene programs ([PMID: 35651829](https://pubmed.ncbi.nlm.nih.gov/35651829/)).

Structure–activity mapping localizes the bioactivity to the C-terminus: *"those corresponding to the C-terminal region of the SCGB3A2 sequence exhibited its unique biological activities of promoting cell proliferation and bronchial branching, and/or inhibiting apoptosis"* ([PMID: 39515417](https://pubmed.ncbi.nlm.nih.gov/39515417/)). This identifies a defined, druggable peptide epitope responsible for the growth-factor/anti-apoptotic/anti-inflammatory activities.

### Finding 5 — MARCO is the experimentally identified receptor; roles in innate immunity and pathogen clearance

Using a retroviral vector-mediated expression-cloning approach, *"we identified macrophage scavenger receptor with collagenous structure (MARCO) as a receptor for UGRP1"* ([PMID: 12847263](https://pubmed.ncbi.nlm.nih.gov/12847263/)). MARCO is expressed on alveolar macrophages while UGRP1/SCGB3A2 is secreted by bronchial Clara-like cells — defining a **lung-specific ligand–receptor pair**.

Functionally, SCGB3A2 behaves as an innate-immune pattern-recognition/opsonin molecule: *"UGRP1 also bound to bacteria and yeast. LPS, a previously identified MARCO ligand, competed with UGRP1 for binding to MARCO and bacteria"* ([PMID: 12847263](https://pubmed.ncbi.nlm.nih.gov/12847263/)). Because LPS and UGRP1 compete for the same MARCO binding site, SCGB3A2 can act both as a microbe-binding molecule and as a modulator of macrophage scavenger-receptor signaling. Its lipid-handling character is further evidenced by the fact that *"in a mammalian expression system, secreted recombinant UGRP1 was copurified with apolipoprotein A-I"* ([PMID: 12847263](https://pubmed.ncbi.nlm.nih.gov/12847263/)), consistent with the secretoglobin lipophilic internal cavity.

A second, distinct receptor interaction has also been reported: UGRP1 binds **podoplanin (PDPN)** on macrophages and, via a PDPN→RhoA→NF-κB axis, can *promote* pro-inflammatory cytokine production (IL-6, IL-1β, TNFα) and upregulate TLR2/MyD88/NOD2/NLRP3 during *S. pneumoniae* infection ([PMID: 35652821](https://pubmed.ncbi.nlm.nih.gov/35652821/)). This indicates SCGB3A2's net effect is **context- and receptor-dependent** — predominantly anti-inflammatory through MARCO/STAT3/PLA2-inhibition in sterile or allergic injury, but able to amplify protective inflammation through PDPN during bacterial infection.

### Finding 6 — A disulfide-linked homodimer whose defining biochemical activity is PLA2 inhibition

The core biochemistry was pinned down quantitatively. Human SCGB3A2 is a **93-residue precursor** (signal peptide residues 1–21; mature chain 22–93; ~10.2 kDa) that forms a **disulfide-linked homodimer** via an interchain bond at **Cys70** (UniProt Q96PL1). Recombinant human SCGB3A2 *"readily formed a dimer in solution and exhibited novel phospholipase A2 inhibitory activity. This is the first demonstration of any quantitative biochemical measurement for the evaluation of SCGB3A2 protein"* ([PMID: 24213919](https://pubmed.ncbi.nlm.nih.gov/24213919/)). UniProt further annotates strong inhibition of **PLA2G1B** specifically.

The same recombinant human protein reproduced the physiological activities: *"human SCGB3A2 exhibited growth factor activity by promoting embryonic lung development in both ex vivo and in vivo systems and antifibrotic activity in the bleomycin-induced lung fibrosis model"* ([PMID: 24213919](https://pubmed.ncbi.nlm.nih.gov/24213919/)). Pharmacokinetic profiling showed rapid, broad biodistribution including **placental transfer**: *"the protein was detected in the dam's serum and lung, as well as the placenta, amniotic fluids, and embryonic lungs at 10 min postadministration, suggesting that SCGB3A2 readily crosses the placenta"* ([PMID: 24213919](https://pubmed.ncbi.nlm.nih.gov/24213919/)). PLA2 inhibition is the single biochemical activity that mechanistically unifies the anti-inflammatory and anti-fibrotic phenotypes, since PLA2 is the rate-limiting enzyme releasing arachidonic acid for pro-inflammatory eicosanoid synthesis.

### Finding 7 — Structural/evolutionary inference: a single-cysteine hydrophobic fold suited to lipid binding and PLA2 inhibition

The mature SCGB3A2 chain (72 aa) contains a **single cysteine (Cys70)**, which necessarily forms the interchain disulfide creating the homodimer — the same minimal **single-Cys, disulfide-linked antiparallel homodimer architecture** as the prototype secretoglobin uteroglobin/SCGB1A1. Compositional analysis performed during this investigation showed SCGB3A2 is unusually **hydrophobic for a secreted protein** (Kyte–Doolittle GRAVY ≈ +0.46) and strikingly **leucine-rich** (~25% Leu vs ~11% in uteroglobin), consistent with amphipathic α-helices that enclose a hydrophobic internal cavity suited to binding lipophilic ligands/phospholipids.

Because uteroglobin is a well-established PLA2 inhibitor and lipid-binding protein, and SCGB3A2 experimentally shares PLA2-inhibitory activity and dimerization ([PMID: 24213919](https://pubmed.ncbi.nlm.nih.gov/24213919/)), the shared fold provides a strong **evolutionary and structural rationale** for a conserved PLA2-inhibitory, lipid-sequestering function. The hydrophobic-cavity model also explains the observed co-purification with apolipoprotein A-I ([PMID: 12847263](https://pubmed.ncbi.nlm.nih.gov/12847263/)) and the binding of microbial surfaces/LPS.

---

## Mechanistic Model / Interpretation

SCGB3A2 can be understood as a **secreted airway-protective module** with one core biochemical activity (PLA2 inhibition / lipid sequestration) that is coupled to receptor-mediated signaling and developmental growth-factor activity.

```
                          NKX2-1 (TTF-1)
                              │  (transcriptional induction)
                              ▼
   Airway Club cell  ───►  SCGB3A2 gene  ──► ~10 kDa precursor (93 aa)
   (+ submucosal serous)                       │ signal peptide cleaved (1–21)
                                               ▼
                               Mature chain (22–93), single Cys70
                                               │  interchain S–S bond at Cys70
                                               ▼
                         SECRETED DISULFIDE-LINKED HOMODIMER (→ tetramer)
                                  (hydrophobic, Leu-rich cavity)
                                               │
         ┌───────────────────────────┬────────┴───────────────┬────────────────────────┐
         ▼                           ▼                         ▼                        ▼
  PLA2 INHIBITION            MARCO (alveolar Mφ)        PDPN (macrophage)        GROWTH-FACTOR
  (PLA2G1B)                  • anti-inflammatory         • RhoA → NF-κB            ACTIVITY
  ↓ arachidonic acid         • binds bacteria/yeast      • ↑IL-6/IL-1β/TNFα        (C-terminal peptide)
  ↓ eicosanoids / lipid      • competes with LPS         • protective              • bronchial branching
     mediators               • assoc. ApoA-I               inflammation in        • fetal lung maturation
         │                           │                       S. pneumoniae        • anti-apoptotic
         └──────────┬────────────────┘                         │
                    ▼                                     (context-dependent)
            STAT1 / STAT3 activation
            STAT3 homodimer → Serpina1a
                    ▼
            ↑ α1-antitrypsin (A1AT)
                    ▼
     Anti-protease, anti-fibrotic, cytoprotective → protects against
     fibrosis, emphysema, allergic (Th2) inflammation
```

**Where it acts:** SCGB3A2 is an **extracellular** effector. It is synthesized in airway epithelial Club cells (and submucosal gland serous cells), secreted into the **airway surface liquid / lumen**, and exerts its functions there and on neighboring cells — inhibiting secreted PLA2 in the lining fluid, binding inhaled microbes, and engaging receptors (MARCO, PDPN) on alveolar/interstitial macrophages. It is not intracellular or membrane-integral, and it is not an enzyme itself.

**Primary function (per the research question):** SCGB3A2 is **not an enzyme or transporter**; it is best classified as a **secreted inhibitor/ligand (signaling molecule)**. Its primary biochemical function is **inhibition of phospholipase A2 (PLA2G1B and related PLA2 activity)**, likely mediated by its hydrophobic secretoglobin cavity sequestering phospholipid substrate and/or binding the enzyme. This single activity rationalizes its anti-inflammatory and anti-fibrotic physiology by reducing arachidonic-acid liberation and downstream eicosanoid signaling. Layered on top are two receptor-coupled signaling roles (MARCO-linked anti-inflammatory macrophage modulation and innate-immune microbe binding; PDPN-linked NF-κB inflammation) and an NKX2-1-dependent developmental growth-factor role.

**Pathways in which it functions:**

| Pathway / axis | SCGB3A2 role | Net effect | Evidence |
|---|---|---|---|
| PLA2 / arachidonic-acid / eicosanoid | Inhibitor of PLA2G1B | ↓ lipid inflammatory mediators | [PMID: 24213919](https://pubmed.ncbi.nlm.nih.gov/24213919/) |
| JAK–STAT (STAT1/STAT3) | Upstream activator; STAT3 homodimer → A1AT | Anti-protease, cytoprotective | [PMID: 36796505](https://pubmed.ncbi.nlm.nih.gov/36796505/) |
| MARCO scavenger-receptor (innate immunity) | Ligand; microbe/LPS binding | Anti-inflammatory Mφ; pathogen clearance | [PMID: 12847263](https://pubmed.ncbi.nlm.nih.gov/12847263/), [PMID: 41071173](https://pubmed.ncbi.nlm.nih.gov/41071173/) |
| PDPN → RhoA → NF-κB | Ligand | Pro-inflammatory (antibacterial) | [PMID: 35652821](https://pubmed.ncbi.nlm.nih.gov/35652821/) |
| NKX2-1 developmental program | Downstream target + growth factor | Lung branching/maturation | [PMID: 18535256](https://pubmed.ncbi.nlm.nih.gov/18535256/) |

**Reconciling anti- vs pro-inflammatory data:** The apparent paradox (anti-inflammatory via MARCO/STAT3/PLA2-inhibition; pro-inflammatory via PDPN/NF-κB) is resolved by **receptor context**. In sterile or allergic injury, PLA2 inhibition and MARCO/STAT3 signaling dominate, producing net protection. During acute bacterial challenge, PDPN engagement can amplify a protective host response. This duality is characteristic of innate airway-defense molecules that must both dampen chronic inflammation and mount acute antimicrobial responses.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the findings |
|---|---|---|
| [24213919](https://pubmed.ncbi.nlm.nih.gov/24213919/) | *Preclinical evaluation of human SCGB3A2 in lung development and fibrosis* | **Core biochemistry:** first quantitative demonstration that human SCGB3A2 forms a dimer and inhibits PLA2; reproduces growth-factor and anti-fibrotic activity; shows placental transfer. |
| [12847263](https://pubmed.ncbi.nlm.nih.gov/12847263/) | *UGRP1 and MARCO as a lung-specific ligand–receptor pair* | Identifies **MARCO as the receptor**; demonstrates bacteria/yeast binding, LPS competition, and ApoA-I association (innate-immune/opsonin + lipid-binding role). |
| [36796505](https://pubmed.ncbi.nlm.nih.gov/36796505/) | *SCGB3A2 protects lung from cigarette smoke-induced emphysema* | Establishes the **STAT1/STAT3 → A1AT** signaling mechanism and emphysema protection via KO/TG mice. |
| [18535256](https://pubmed.ncbi.nlm.nih.gov/18535256/) | *Role of SCGB3A2 in lung development* | **NKX2-1 target** and **growth-factor activity** promoting fetal lung development/branching. |
| [16456148](https://pubmed.ncbi.nlm.nih.gov/16456148/) | *UGRP1 suppresses allergic airway inflammation* | Direct in vivo **anti-inflammatory** evidence: reduced eosinophils and IL-4/IL-5/IL-13. |
| [26559674](https://pubmed.ncbi.nlm.nih.gov/26559674/) | *SCGB3A2 anti-fibrotic activity in bleomycin model* | Loss-of-function: KO lungs show **worse fibrosis**. |
| [26178733](https://pubmed.ncbi.nlm.nih.gov/26178733/) | *Transgenic SCGB3A2 accelerates fibrosis resolution* | Gain-of-function: TG lungs **resolve fibrosis faster**. |
| [35651829](https://pubmed.ncbi.nlm.nih.gov/35651829/) | *Aging emphysema/lymphoma-like lesions enhanced by SCGB3A2 loss* | KO mice develop age-related emphysema and immune lesions → homeostatic/immune role. |
| [39515417](https://pubmed.ncbi.nlm.nih.gov/39515417/) | *SCGB3A2 peptides for allergic airway inflammation* | Maps bioactivity to the **C-terminal region** (therapeutic peptides). |
| [41071173](https://pubmed.ncbi.nlm.nih.gov/41071173/) | *Anti-inflammatory macrophage niche in COPD* | Links SCGB3A2 with **MARCO** in an anti-inflammatory epithelial→macrophage niche. |
| [35652821](https://pubmed.ncbi.nlm.nih.gov/35652821/) | *UGRP1 binds PDPN to promote inflammation in S. pneumoniae* | Defines a second receptor (**PDPN → RhoA → NF-κB**) and a context-dependent pro-inflammatory role. |
| [35016921](https://pubmed.ncbi.nlm.nih.gov/35016921/) | *Emerging role of SCGB3A2 in human diseases (review)* | Authoritative summary of size, oligomerization, Club-cell localization, and functional repertoire. |
| [20843168](https://pubmed.ncbi.nlm.nih.gov/20843168/) | *ELISA for UGRP1 as a biomarker* | Secretion/biodistribution: high in BALF/sputum/amniotic fluid; biomarker of epithelial integrity. |
| [36094595](https://pubmed.ncbi.nlm.nih.gov/36094595/) | *NKX2-1 in fundic-gland gastric adenocarcinoma* | Independent confirmation that SCGB3A2 is part of the NKX2-1 transcriptional module. |

**Supporting but lower-weight / genetic-association literature:** Multiple human genetic studies examine the *SCGB3A2* promoter **−112G/A (rs1368408)** polymorphism in asthma, allergic rhinitis, and Graves' disease, with the low-expressing A allele linked to lower plasma UGRP1 and, in some cohorts, disease susceptibility ([PMID: 18089940](https://pubmed.ncbi.nlm.nih.gov/18089940/), [PMID: 21170691](https://pubmed.ncbi.nlm.nih.gov/21170691/), [PMID: 19126779](https://pubmed.ncbi.nlm.nih.gov/19126779/), [PMID: 21410962](https://pubmed.ncbi.nlm.nih.gov/21410962/)). These associations are inconsistent across populations (e.g., no association in Sicilian asthma, [PMID: 18201431](https://pubmed.ncbi.nlm.nih.gov/18201431/); no major role in severe RSV, [PMID: 21503925](https://pubmed.ncbi.nlm.nih.gov/21503925/)) and are therefore supportive context rather than definitive mechanistic evidence. Expression studies show SCGB3A2 is downregulated by Th2 cytokines (IL-5, [PMID: 15626484](https://pubmed.ncbi.nlm.nih.gov/15626484/)) and in chronic rhinosinusitis ([PMID: 21385388](https://pubmed.ncbi.nlm.nih.gov/21385388/)), consistent with a protein depleted where inflammation is uncontrolled. SCGB3A2 is the paralog of the putative breast tumor suppressor SCGB3A1/HIN-1, and the two are reciprocally regulated by oncostatin M ([PMID: 18978304](https://pubmed.ncbi.nlm.nih.gov/18978304/), [PMID: 12175512](https://pubmed.ncbi.nlm.nih.gov/12175512/)).

---

## Supported and Refuted Hypotheses

| Hypothesis | Status | Key evidence |
|---|---|---|
| SCGB3A2 is a secreted anti-inflammatory secretoglobin from Club cells | **Supported** | [PMID: 35016921](https://pubmed.ncbi.nlm.nih.gov/35016921/), [16456148](https://pubmed.ncbi.nlm.nih.gov/16456148/) |
| SCGB3A2 is a growth/differentiation factor for lung development, downstream of NKX2-1 | **Supported** | [PMID: 18535256](https://pubmed.ncbi.nlm.nih.gov/18535256/) |
| SCGB3A2 signals via STAT3 (homodimer) to induce protective genes (A1AT) | **Supported** | [PMID: 36796505](https://pubmed.ncbi.nlm.nih.gov/36796505/) |
| SCGB3A2 is anti-fibrotic and protects against emphysema in vivo | **Supported** | [PMID: 26559674](https://pubmed.ncbi.nlm.nih.gov/26559674/), [26178733](https://pubmed.ncbi.nlm.nih.gov/26178733/), [36796505](https://pubmed.ncbi.nlm.nih.gov/36796505/) |
| MARCO is the receptor for SCGB3A2/UGRP1 | **Supported (direct, expression cloning)** | [PMID: 12847263](https://pubmed.ncbi.nlm.nih.gov/12847263/); corroborated [41071173](https://pubmed.ncbi.nlm.nih.gov/41071173/) |
| SCGB3A2 binds microbes/lipid (ApoA-I) as an innate-immune opsonin | **Supported** | [PMID: 12847263](https://pubmed.ncbi.nlm.nih.gov/12847263/) |
| SCGB3A2's precise biochemical activity is phospholipase A2 inhibition | **Supported (direct biochemistry)** | [PMID: 24213919](https://pubmed.ncbi.nlm.nih.gov/24213919/); UniProt Q96PL1 |
| SCGB3A2 is itself an enzyme or transporter | **Refuted** | No catalytic/transport activity; it is a secreted PLA2-inhibitor/ligand ([PMID: 24213919](https://pubmed.ncbi.nlm.nih.gov/24213919/), [35016921](https://pubmed.ncbi.nlm.nih.gov/35016921/)) |

---

## Limitations and Knowledge Gaps

1. **No experimental 3-D structure of human SCGB3A2.** The homodimer architecture, hydrophobic cavity, and PLA2-inhibition mechanism are inferred from the single-cysteine sequence, homology to uteroglobin/SCGB1A1, and compositional/bioinformatic analysis. A crystal or cryo-EM structure (ideally with bound phospholipid or in complex with PLA2) is lacking.

2. **Mechanism of PLA2 inhibition is not resolved.** It is unknown whether SCGB3A2 inhibits PLA2 by sequestering phospholipid substrate in its cavity, by direct enzyme binding, or both. The full set of inhibited PLA2 isoforms beyond PLA2G1B and the inhibition kinetics (Ki, competitive vs non-competitive) remain uncharacterized.

3. **Receptor duality is incompletely mapped.** MARCO and PDPN both bind SCGB3A2 but drive opposite inflammatory outcomes, and neither has been firmly shown to mediate the epithelial/fibroblast STAT3 activation. Structural basis of binding, receptor stoichiometry, and context-selectivity are open questions.

4. **Much mechanistic data is from mouse.** While human recombinant SCGB3A2 reproduces key activities ([PMID: 24213919](https://pubmed.ncbi.nlm.nih.gov/24213919/)), the STAT3→A1AT axis, emphysema/fibrosis phenotypes, and MARCO signaling are largely demonstrated in mouse models; direct human in vivo validation is limited.

5. **Human genetic associations are inconsistent.** The −112G/A promoter SNP shows population-dependent and often weak/absent associations, so it does not firmly establish causal human disease relevance.

6. **The physiological lipophilic ligand** bound in the secretoglobin cavity is not established; "anti-cancer" and non-pulmonary roles remain preliminary and outside the protein's core airway function.

---

## Proposed Follow-up Experiments / Actions

1. **Solve the structure.** Determine the crystal/cryo-EM structure of the human SCGB3A2 homodimer, ideally in complex with a phospholipid ligand and/or with PLA2G1B, to define the hydrophobic cavity and the inhibition mechanism directly.

2. **Define PLA2-inhibition biochemistry.** Perform enzyme kinetics against a panel of secreted PLA2 isoforms (groups IB, IIA, V, X) to establish substrate/enzyme specificity, Ki values, and inhibition mode; test whether the C-terminal active peptide ([PMID: 39515417](https://pubmed.ncbi.nlm.nih.gov/39515417/)) retains PLA2 inhibition.

3. **Map receptor-binding determinants.** Use mutagenesis/peptide arrays to identify the SCGB3A2 residues that bind MARCO vs PDPN, and test whether receptor-selective variants can separate anti-inflammatory (MARCO/STAT3) from pro-inflammatory (PDPN/NF-κB) signaling.

4. **Dissect the STAT3→A1AT axis in human cells.** Confirm the SCGB3A2 → STAT3 homodimer → *SERPINA1* induction in primary human lung fibroblasts/epithelium and determine whether it requires a specific receptor (e.g., MARCO).

5. **Test therapeutic potential.** Evaluate recombinant human SCGB3A2 or its C-terminal peptide in human-relevant models (organoids, precision-cut lung slices, humanized mice) for fibrosis (IPF), emphysema (COPD/α1-antitrypsin deficiency), and allergic asthma, leveraging its rapid biodistribution and placental-transfer profile.

6. **Clarify the infection context.** Determine in vivo whether the PDPN-dependent pro-inflammatory activity is net-protective or net-harmful across different airway pathogens, to guide whether SCGB3A2 agonism or antagonism is desirable in infection.

---

### Bottom line

SCGB3A2/UGRP1 is a secreted, homodimeric airway secretoglobin — not an enzyme or transporter — whose defining biochemistry is **phospholipase A2 inhibition**, executed **extracellularly in the airway lining fluid**, and coupled to receptor-mediated signaling (MARCO, PDPN; STAT1/STAT3→α1-antitrypsin) and NKX2-1-driven lung-maturation growth-factor activity, together producing robust anti-inflammatory, anti-fibrotic, and tissue-protective effects in the lung.


## Artifacts

- [OpenScientist final report](SCGB3A2-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](SCGB3A2-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:24213919
2. PMID:12847263
3. PMID:35652821
4. PMID:36796505
5. PMID:18535256
6. PMID:35016921
7. PMID:16456148
8. PMID:20843168
9. PMID:36094595
10. PMID:41071173
11. PMID:26559674
12. PMID:26178733
13. PMID:35651829
14. PMID:39515417
15. PMID:18089940
16. PMID:21170691
17. PMID:19126779
18. PMID:21410962
19. PMID:18201431
20. PMID:21503925
21. PMID:15626484
22. PMID:21385388
23. PMID:18978304
24. PMID:12175512