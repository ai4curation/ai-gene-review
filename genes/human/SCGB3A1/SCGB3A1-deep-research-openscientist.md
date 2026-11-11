---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T18:45:47.647846'
end_time: '2026-10-24T19:08:16.811286'
duration_seconds: 1349.16
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: SCGB3A1
  gene_symbol: SCGB3A1
  uniprot_accession: Q96QR1
  protein_description: 'RecName: Full=Secretoglobin family 3A member 1; AltName: Full=Cytokine
    HIN-1; AltName: Full=High in normal 1; AltName: Full=Pneumo secretory protein
    2; Short=PnSP-2; AltName: Full=Uteroglobin-related protein 2; Flags: Precursor;'
  gene_info: Name=SCGB3A1; Synonyms=HIN1, PNSP2, UGRP2; ORFNames=UNQ629/PRO1245;
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
citation_count: 9
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: SCGB3A1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: SCGB3A1-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q96QR1
- **Protein Description:** RecName: Full=Secretoglobin family 3A member 1; AltName: Full=Cytokine HIN-1; AltName: Full=High in normal 1; AltName: Full=Pneumo secretory protein 2; Short=PnSP-2; AltName: Full=Uteroglobin-related protein 2; Flags: Precursor;
- **Gene Information:** Name=SCGB3A1; Synonyms=HIN1, PNSP2, UGRP2; ORFNames=UNQ629/PRO1245;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the secretoglobin family. UGRP subfamily.
- **Key Domains:** Secretoglobin_3A. (IPR040301); SCGB3A (PF20490)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SCGB3A1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SCGB3A1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SCGB3A1** (gene ID: SCGB3A1, UniProt: Q96QR1) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# SCGB3A1 (HIN-1 / UGRP2): Functional Annotation Report

**Gene:** SCGB3A1 (synonyms: HIN1, PNSP2, UGRP2; ORF names UNQ629/PRO1245)
**Protein:** Secretoglobin family 3A member 1 (Cytokine HIN-1 / High in Normal 1 / Pneumo secretory protein 2 / Uteroglobin-related protein 2)
**UniProt:** Q96QR1 · **NCBI Gene ID:** 92304 · **Ensembl:** ENSG00000161055
**Organism:** *Homo sapiens* (Human)
**Family:** Secretoglobin superfamily, UGRP (SCGB3A) subfamily
**Domains:** Secretoglobin_3A (IPR040301); SCGB3A (PF20490)

---

## Summary

**SCGB3A1 encodes a small, secreted, disulfide-linked homodimeric secretoglobin that acts not as an enzyme or transporter, but as an extracellular, cytokine-like growth-inhibitory ligand.** The gene symbol and the UniProt identity (Q96QR1) are concordant: all authoritative literature for "HIN-1," "SCGB3A1," and "UGRP2" describes the same human secretoglobin-superfamily protein originally discovered as a breast-epithelial tumor-suppressor cytokine. There is no evidence of gene-symbol ambiguity across organisms; the protein is well-characterized in human and mouse airway and glandular epithelium.

The protein is produced by terminally differentiated luminal and airway secretory epithelial cells — mammary luminal epithelium, large-airway bronchial epithelium, and submucosal gland cells — and is secreted apically into the lumen and body fluids, where it is recoverable in bronchial lavage, saliva, plasma, and serum. Its site of action is therefore **extracellular**. Functionally, HIN-1 binds a high-affinity, still-unidentified receptor on the surface of epithelial cells and suppresses mitogen-induced **PI3K/AKT** signaling. Through AKT inhibition it blocks anchorage-dependent and anchorage-independent growth, migration, and invasion; it inhibits Rb phosphorylation and cell-cycle re-entry; and it induces apoptosis in proliferating cells. Constitutively active AKT abolishes these effects, placing AKT downstream of HIN-1 as the critical mechanistic node.

Consistent with a tumor-suppressor role, SCGB3A1 expression is lost early in the development of breast, lung, prostate, esophageal, and multiple other epithelial cancers, predominantly through CpG-island **promoter hypermethylation** rather than mutation. Methylation is essentially absent in normal tissue, tightly correlated with loss of expression, and reversible by demethylating agents. At the structural level, SCGB3A1 shares the secreted, dimeric uteroglobin fold with a central hydrophobic cavity, which in family prototypes binds and sequesters hydrophobic ligands and confers anti-inflammatory activity — a capacity that is structurally plausible for SCGB3A1 but has not been directly demonstrated.

---

## Gene/Protein Identity Verification

Before reporting function, the mandatory identity check was completed and **passed**:

| Verification step | Result |
|---|---|
| Gene symbol "SCGB3A1" matches UniProt description? | **Yes** — "HIN-1," "UGRP2," and "SCGB3A1" are used interchangeably in the literature for the same protein (Q96QR1). |
| Organism correct (*Homo sapiens*)? | **Yes** — human studies dominate; mouse ortholog (Scgb3a1) confirms conservation. |
| Protein family/domains align with literature? | **Yes** — repeatedly described as a secretoglobin/uteroglobin-family member, UGRP (SCGB3A) subfamily. |
| Conflicting literature for a different same-symbol gene? | **No** — no ambiguity detected; all retrieved literature concerns this secretoglobin. |

The symbol is **not** ambiguous. Research proceeded on the correct target.

---

## Key Findings

### Finding 1 — SCGB3A1/HIN-1 is a small secreted secretoglobin acting as an epithelial tumor-suppressor cytokine

HIN-1 ("High in Normal 1") was originally identified by serial analysis of gene expression (SAGE) comparing normal versus ductal carcinoma *in situ* (DCIS) mammary epithelium. It emerged as one of the most strongly down-regulated transcripts in cancer: its expression is lost in approximately **94% of breast carcinomas** and **95% of pre-invasive lesions** (DCIS and LCIS). Re-introduction of HIN-1 into breast cancer cells inhibits their growth, establishing the first functional evidence of a tumor-suppressor role. The original report explicitly described HIN-1 as "a putative cytokine with no significant homology to known proteins" whose reintroduction "inhibits cell growth" ([PMID: 11481438](https://pubmed.ncbi.nlm.nih.gov/11481438/)).

HIN-1 belongs to the **secretoglobin/uteroglobin superfamily**, whose members are "small, secretory, rarely glycosylated dimeric proteins with unclear physiological functions and are mainly expressed in mucosal tissues" ([PMID: 11193762](https://pubmed.ncbi.nlm.nih.gov/11193762/)). This family assignment is the single most important structural clue to its function: it predicts a secreted, dimeric protein with a hydrophobic internal cavity rather than an enzyme or transporter.

### Finding 2 — HIN-1/SCGB3A1 inhibits AKT activation to suppress growth, migration, and invasion

The definitive mechanistic study (Krop et al., *Cancer Res* 2005) established HIN-1 as "a potent inhibitor of anchorage-dependent and anchorage-independent cell growth, cell migration, and invasion" ([PMID: 16266985](https://pubmed.ncbi.nlm.nih.gov/16266985/)). The mechanism operates through the **PI3K/AKT pathway**: "mitogen-induced phosphorylation and activation of AKT are inhibited in HIN-1-expressing cells. In addition, expression of constitutively activate AKT abrogates HIN-1-mediated growth arrest" ([PMID: 16266985](https://pubmed.ncbi.nlm.nih.gov/16266985/)). This epistasis experiment is decisive — it places AKT **downstream** of HIN-1 and identifies AKT suppression as the proximate cause of growth arrest.

Downstream consequences include inhibition of retinoblastoma protein (Rb) phosphorylation and blockade of cell-cycle re-entry in synchronized cells, together with induction of apoptosis in exponentially growing cells. Critically, ligand-binding studies "indicate the presence of high-affinity cell surface HIN-1 binding on epithelial cells" ([PMID: 16266985](https://pubmed.ncbi.nlm.nih.gov/16266985/)), demonstrating that HIN-1 acts as a **secreted ligand engaging a cell-surface receptor** — consistent with its cytokine-like classification. The receptor itself remains unidentified.

```
Mitogen  ──►  [Receptor/RTK]  ──►  PI3K  ──►  AKT-P  ──►  proliferation, survival, migration, invasion
                                              ▲
                                              │  (–) INHIBITION
   SCGB3A1/HIN-1 (secreted dimer) ──► [unidentified high-affinity epithelial receptor]
                                              │
                                              ▼
                        ↓ AKT-P → ↓ Rb-P → G1 arrest, ↓ invasion, ↑ apoptosis
```

### Finding 3 — SCGB3A1 is secreted by airway/glandular epithelium and detectable in body fluids; silenced by promoter hypermethylation in cancer

HIN-1 protein is highly expressed in mammary gland, trachea, lung (bronchial epithelial cells), prostate, pancreas, and salivary gland, with secreted protein detectable in **bronchial lavage, saliva, plasma, and serum** — "high levels of HIN-1 protein are detected in bronchial lavage, saliva, plasma, and serum" ([PMID: 15383627](https://pubmed.ncbi.nlm.nih.gov/15383627/)). In the lung its expression is restricted to terminally differentiated airway epithelial cells and is up-regulated during retinoic-acid-induced bronchial epithelial differentiation: "The expression of HIN-1 is restricted to terminally differentiated airway epithelial cells in vivo and in vitro implicating HIN-1 in the acquisition or maintenance of terminally differentiated epithelial phenotype" ([PMID: 12175512](https://pubmed.ncbi.nlm.nih.gov/12175512/)).

Across more than 800 tumors of 17 types, promoter methylation (≈73% breast, ≈67% NSCLC, high in prostate, retinoblastoma, and Wilms tumor) correlated completely with loss of expression and was reversed by the demethylating agent 5-aza-2'-deoxycytidine: "methylation was completely correlated with loss of expression. Expression negative cell lines restored HIN-1 expression after treatment with 5-aza-2'-deoxycytidine" ([PMID: 15472908](https://pubmed.ncbi.nlm.nih.gov/15472908/)). Methylation is rare (~5%) in non-malignant tissue, underscoring that **epigenetic silencing — not mutation — is the principal inactivation mechanism** and that it is an early event in malignant transformation.

### Finding 4 — SCGB3A1 is a 104-aa secreted precursor forming a disulfide-linked homodimer with a secretoglobin fold

UniProt Q96QR1 describes a **104-residue precursor** with an N-terminal signal peptide (residues 1–20) cleaved to release the mature secreted chain (residues 21–104). The mature protein contains a single cysteine (position 78) that forms an **interchain disulfide bond**, assembling a disulfide-linked **homodimer**. Subcellular location is annotated as Secreted (extracellular region, inferred from direct assay; extracellular exosome, high-throughput). Curated GO terms include cytokine activity (molecular function) and negative regulation of cell growth (biological process).

This architecture is the hallmark of the secretoglobin fold. Family members "form antiparallel homodimers via two intermolecular disulfide bonds" ([PMID: 11193762](https://pubmed.ncbi.nlm.nih.gov/11193762/)), and the fold contains a conserved central feature: "In the known uteroglobin structures, this lysine forms an exposed salt bridge with an aspartate side chain, which is conserved in almost all sequences" ([PMID: 11193762](https://pubmed.ncbi.nlm.nih.gov/11193762/)). The dimeric, boomerang-shaped uteroglobin fold encloses a central hydrophobic cavity — the structural basis for the family's ligand-binding behavior.

### Finding 5 — SCGB3A1 is produced by luminal/airway secretory epithelium and secreted into lumen and body fluids (extracellular site of action)

Curated tissue specificity (from PubMed 11481438 and 12406855) indicates SCGB3A1 is highly expressed in lung and prostate, and also in mammary gland, spleen, pancreas, testis, and liver. In the lung it is detected throughout the airway epithelium with highest expression in large airways and in submucosal gland acinar and ductile cells, but **not** in respiratory bronchioles, alveolar ducts, or alveolar epithelium. In the mammary gland it localizes specifically to **luminal epithelial cells**. The secreted protein is recoverable in bronchial lavage, saliva, plasma, and serum — "high levels of HIN-1 protein are detected in bronchial lavage, saliva, plasma, and serum" ([PMID: 15383627](https://pubmed.ncbi.nlm.nih.gov/15383627/)) — confirming apical secretion into the lumen and the circulation. This defines the **extracellular compartment** as the location where SCGB3A1 carries out its function.

### Finding 6 — SCGB3A1 maps to chromosome 5q35.3 in the SCGB3A subfamily, separate from the 11q12.2 secretoglobin cluster

NCBI/Ensembl annotation (Gene ID 92304, ENSG00000161055) places SCGB3A1 as a small protein-coding gene (~1.6 kb, minus strand) at **chromosome 5q35.3**. It belongs to the secretoglobin 3A (UGRP) subfamily together with its paralog **SCGB3A2 (UGRP1 / HIN-2)**. This is distinct from the classical uteroglobin-family members (CC10/SCGB1A1, mammaglobin, lipophilins, lacryglobin), which "are localized on chromosome 11q12.2 in a dense cluster" ([PMID: 11193762](https://pubmed.ncbi.nlm.nih.gov/11193762/)). SCGB3A1's separate chromosomal location establishes it as a distinct subfamily member rather than part of the ancestral 11q12.2 cluster.

Consolidated GO annotations assign molecular functions of cytokine activity (non-traceable author statement) and protein binding (inferred from physical interaction); cellular components of extracellular region and extracellular exosome; and biological processes of negative regulation of cell growth, regulation of cell population proliferation, and signal transduction. A "positive regulation of myoblast fusion" term is only an electronic/phylogenetic inference (IBA) with no direct experimental support and should be treated cautiously.

### Finding 7 — Family-level inference: secretoglobins can sequester hydrophobic ligands and are anti-inflammatory

The founding secretoglobin, **uteroglobin** (SCGB1A1 prototype), is a secreted anti-inflammatory/immunomodulatory protein. It "inhibits soluble phospholipase A(2) activity and binds and perhaps sequesters hydrophobic ligands such as progesterone, retinols, polychlorinated biphenyls, phospholipids, and prostaglandins" ([PMID: 17916741](https://pubmed.ncbi.nlm.nih.gov/17916741/)). It also displays antichemotactic, antiallergic, and antitumorigenic activities, and secretoglobins are broadly expressed by mucosal epithelia and present in blood, urine, and other body fluids.

Because SCGB3A1 shares the secreted, dimeric uteroglobin fold with its central hydrophobic cavity, an **analogous small-molecule/lipid-binding and immunomodulatory capacity is structurally plausible**. This remains a structure-/evolution-based inference and has **not** been directly demonstrated for SCGB3A1. It is nonetheless a valuable hypothesis: a sequestration or lipid-mediator-buffering activity could reconcile the "cytokine-like" ligand behavior with the absence of an identified classical receptor.

---

## Mechanistic Model / Interpretation

The convergent evidence supports a coherent model of SCGB3A1 as a **secreted epithelial growth-suppressor cytokine** acting in an autocrine/paracrine loop at the luminal surface:

```
 ┌─────────────────────────────────────────────────────────────────────┐
 │  Terminally differentiated luminal / airway / glandular epithelium   │
 │                                                                       │
 │   SCGB3A1 gene (5q35.3)                                                │
 │        │ transcription (retinoic-acid / differentiation induced)      │
 │        ▼                                                               │
 │   104-aa precursor ─► signal-peptide cleavage ─► mature chain (21-104)│
 │        │                                                              │
 │        ▼  interchain disulfide (Cys78)                                │
 │   Disulfide-linked HOMODIMER  ──────────► APICAL SECRETION            │
 └───────────────────────────────────────────────┬─────────────────────┘
                                                  ▼
                 LUMEN / BODY FLUIDS (lavage, saliva, plasma, serum)
                                                  │
                                                  ▼
                 High-affinity binding to UNIDENTIFIED epithelial receptor
                                                  │
                                                  ▼
                        ▼ Mitogen-induced AKT phosphorylation
                        ▼ Rb phosphorylation → G1 cell-cycle arrest
                        ▼ Migration & invasion
                        ▲ Apoptosis in proliferating cells
                                                  │
                                                  ▼
                            TUMOR-SUPPRESSOR OUTPUT
```

**Primary function (answer to the core question).** SCGB3A1 is **not an enzyme or transporter**. It is a **signaling molecule** — a secreted, cytokine-like ligand. Its primary role in the pathway is to **antagonize mitogen-driven PI3K/AKT signaling** by engaging a high-affinity cell-surface receptor on epithelial cells, thereby restraining proliferation, motility, and survival. The AKT epistasis experiment ([PMID: 16266985](https://pubmed.ncbi.nlm.nih.gov/16266985/)) is the strongest direct mechanistic evidence and defines AKT as the critical downstream node.

**Site of action.** Extracellular. SCGB3A1 is synthesized in the secretory pathway (signal peptide), dimerizes via an interchain disulfide, and is secreted apically into the airway/glandular lumen and into the circulation. It exerts its effect from outside the cell by receptor engagement, not intracellularly.

**Pathway context.** The defined pathway is PI3K→AKT→(Rb/cell-cycle, survival, invasion). An additional, structurally-inferred but unproven layer is the family's capacity to sequester hydrophobic ligands (lipids, steroids, retinoids) and to be anti-inflammatory ([PMID: 17916741](https://pubmed.ncbi.nlm.nih.gov/17916741/)); if operative for SCGB3A1, this could provide the molecular basis for receptor-independent or lipid-mediator-buffering effects.

**Paralog contrast.** SCGB3A1's closest paralog SCGB3A2/UGRP1 has an identified receptor (MARCO) and a role in innate pulmonary immunity/pathogen clearance ([PMID: 12847263](https://pubmed.ncbi.nlm.nih.gov/12847263/)). This illustrates that UGRP-subfamily secretoglobins engage cell-surface receptors — supporting the plausibility of a dedicated SCGB3A1 receptor — while also showing that each paralog has a distinct biology, cautioning against assuming SCGB3A1 shares MARCO or an immune-clearance role.

| Feature | SCGB3A1 (HIN-1/UGRP2) | SCGB3A2 (UGRP1/HIN-2) |
|---|---|---|
| Chromosome | 5q35.3 | 5q32 (UGRP subfamily) |
| Receptor | Unidentified (high-affinity, epithelial) | MARCO (identified) |
| Principal annotated role | Growth suppression via AKT inhibition; tumor suppressor | Innate immunity / pathogen clearance; anti-inflammatory |
| Expression | Large-airway epithelium, submucosal glands, mammary luminal cells | Lung Clara-like cells |
| Cancer link | Silenced by promoter hypermethylation across epithelial cancers | Less consistently a tumor suppressor |

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution | Strength |
|---|---|---|---|
| [11481438](https://pubmed.ncbi.nlm.nih.gov/11481438/) | *HIN-1, a putative cytokine highly expressed in normal but not cancerous mammary epithelial cells* | Original discovery; secreted cytokine-like growth inhibitor down-regulated in breast cancer | Primary, functional |
| [16266985](https://pubmed.ncbi.nlm.nih.gov/16266985/) | *HIN-1, an inhibitor of cell growth, invasion, and AKT activation* | Core mechanism: AKT suppression; cell-surface binding; growth/invasion arrest; AKT epistasis | Primary, mechanistic (strongest) |
| [15383627](https://pubmed.ncbi.nlm.nih.gov/15383627/) | *Frequent HIN-1 promoter methylation and lack of expression in multiple human tumor types* | Secretion into body fluids; broad tissue expression; methylation across tumor types | Primary, localization + epigenetics |
| [12175512](https://pubmed.ncbi.nlm.nih.gov/12175512/) | *Expression of HIN-1 and UGRP-1 in adult and developing tissues* | Restriction to terminally differentiated airway epithelium; link to differentiation | Primary, expression |
| [15472908](https://pubmed.ncbi.nlm.nih.gov/15472908/) | *Aberrant methylation of HIN-1 is a frequent event in many human malignancies* | Methylation completely correlates with loss of expression; reversible by 5-aza-dC | Primary, epigenetics (>800 tumors) |
| [11193762](https://pubmed.ncbi.nlm.nih.gov/11193762/) | *All human genes of the uteroglobin family are localized on chromosome 11q12.2…* | Family structure: dimeric, disulfide-linked fold; conserved lysine salt bridge; 11q12.2 cluster distinct from SCGB3A1 | Review/structural |
| [17916741](https://pubmed.ncbi.nlm.nih.gov/17916741/) | *Uteroglobin: a steroid-inducible immunomodulatory protein that founded the Secretoglobin superfamily* | Family prototype: hydrophobic-ligand sequestration; anti-PLA2; anti-inflammatory — basis for structural inference | Authoritative review |
| [12847263](https://pubmed.ncbi.nlm.nih.gov/12847263/) | *UGRP1 and MARCO as a lung-specific ligand-receptor pair* | Paralog SCGB3A2 engages MARCO; UGRP subfamily uses cell-surface receptors | Primary (paralog context) |
| [19098448](https://pubmed.ncbi.nlm.nih.gov/19098448/) | *Promoter methylation of HIN-1 in the progression to esophageal squamous cancer* | Methylation increases with dysplasia grade (0% normal → 50% cancer); early event | Primary, clinical epigenetics |
| [14601057](https://pubmed.ncbi.nlm.nih.gov/14601057/) | *DNA methylation of RASSF1A, HIN-1… in lobular breast carcinoma* | HIN-1 silenced in ductal and lobular carcinomas; unmethylated in normal tissue | Primary, clinical |
| [22695491](https://pubmed.ncbi.nlm.nih.gov/22695491/) | *Methylation of HIN-1, RASSF1A, RIL, CDH13 in breast cancer…* | HIN-1 methylation associates with ER/PR status; clinical correlations | Primary, clinical |
| [30768367](https://pubmed.ncbi.nlm.nih.gov/30768367/) | *Spatiotemporal expression of SCGB1A1, SCGB3A1, SCGB3A2 in mouse airway* | Conserved airway expression; knockouts suggest each SCGB has a unique function | Primary (mouse) |

**How the evidence fits together.** The discovery paper (11481438) and the mechanistic paper (16266985) provide the direct, hypothesis-driven, low-throughput evidence that this report prioritizes. The methylation studies (15472908, 15383627, 19098448, 14601057, 22695491) provide convergent, large-cohort support that loss of SCGB3A1 is an early, recurrent, epigenetically-driven event in epithelial carcinogenesis — consistent with but not proof of a causal tumor-suppressor role. The family/structural literature (11193762, 17916741) and the paralog ligand-receptor paper (12847263) provide the structure- and evolution-based inferences requested, anchoring the secreted-dimer architecture and the plausibility of a dedicated receptor.

---

## Limitations and Knowledge Gaps

1. **The receptor is unidentified.** High-affinity cell-surface binding is demonstrated ([PMID: 16266985](https://pubmed.ncbi.nlm.nih.gov/16266985/)), but the receptor that transduces AKT suppression is unknown. This is the single largest gap in the mechanistic model. Unlike its paralog SCGB3A2 (receptor = MARCO), SCGB3A1 has no validated partner.

2. **Direct ligand-binding/sequestration is inferred, not shown.** The hydrophobic-cavity ligand-binding and anti-inflammatory activities are documented for the family prototype uteroglobin ([PMID: 17916741](https://pubmed.ncbi.nlm.nih.gov/17916741/)) but have **not** been experimentally confirmed for SCGB3A1. Whether SCGB3A1 binds steroids, retinoids, phospholipids, or prostaglandins is open.

3. **No experimental 3D structure for human SCGB3A1.** The dimeric secretoglobin fold and interchain disulfide are inferred from sequence/family homology and UniProt annotation, not from a crystal or cryo-EM structure of SCGB3A1 itself.

4. **Causality vs. correlation in cancer.** Promoter hypermethylation correlates tightly with loss of expression across many tumor types, but methylation studies are associative; the growth-suppressive causality rests primarily on the re-expression experiments in cell lines, not on in vivo genetic models.

5. **Physiological (non-cancer) function underexplored.** The normal role in differentiated epithelium — possibly in surfactant/mucosal homeostasis, epithelial differentiation, or local immunomodulation — is not defined. Mouse knockouts show no gross airway developmental defect and do not alter other Scgb genes ([PMID: 30768367](https://pubmed.ncbi.nlm.nih.gov/30768367/)), leaving the endogenous function unresolved.

6. **Some database annotations are weakly supported.** The GO term "positive regulation of myoblast fusion" is only a phylogenetic/electronic inference (IBA) with no direct experimental backing and should not be treated as an established function.

---

## Proposed Follow-up Experiments / Actions

1. **Receptor identification (highest priority).** Use recombinant tagged HIN-1 dimer for affinity-capture/cross-linking proteomics or an expression-cloning screen (as was successfully used for the SCGB3A2–MARCO pair) on HIN-1-responsive epithelial cells. Validate candidates by loss-of-function (CRISPR) rescue of AKT suppression.

2. **Direct ligand-binding assays.** Test whether purified SCGB3A1 dimer binds hydrophobic ligands (progesterone, retinoic acid, phospholipids, prostaglandins) by isothermal titration calorimetry, fluorescence displacement, or native mass spectrometry — directly testing the family-based inference in Finding 7.

3. **Structural determination.** Solve the SCGB3A1 homodimer structure (X-ray/cryo-EM) and map the hydrophobic cavity; complement with AlphaFold-Multimer prediction and PAE/pLDDT confidence analysis of the dimer interface and disulfide geometry.

4. **Pathway dissection.** Define how receptor engagement reaches PI3K/AKT (receptor tyrosine kinase inhibition? phosphatase activation, e.g., PTEN/PP2A?). Use phospho-proteomics after acute HIN-1 exposure to map the signaling cascade upstream of AKT.

5. **In vivo tumor-suppressor test.** Generate conditional Scgb3a1 knockout mice and challenge with mammary/airway carcinogenesis models to establish whether loss accelerates tumorigenesis — moving from correlative methylation data to causal genetics.

6. **Biomarker development.** Given secretion into saliva, plasma, serum, and lavage, evaluate circulating/secreted HIN-1 protein and promoter-methylation assays as early-detection or risk-stratification biomarkers for breast, lung, and esophageal cancer.

---

## Conclusion

SCGB3A1 (HIN-1/UGRP2, Q96QR1) is a small, secreted, disulfide-linked homodimeric secretoglobin of the UGRP (SCGB3A) subfamily, produced by terminally differentiated luminal, airway, and glandular epithelial cells and secreted into the lumen and body fluids. It functions **extracellularly** as a **cytokine-like growth-inhibitory ligand**, not as an enzyme or transporter: by binding a high-affinity (still-unidentified) epithelial cell-surface receptor it **suppresses mitogen-induced PI3K/AKT signaling**, thereby inhibiting proliferation, migration, and invasion and promoting apoptosis. Its silencing by CpG-island promoter hypermethylation early in breast, lung, prostate, esophageal, and other epithelial cancers is consistent with a tumor-suppressor role. A family-based structural inference — that its uteroglobin fold could bind/sequester hydrophobic ligands and exert anti-inflammatory effects — remains an attractive but untested hypothesis.


## Artifacts

- [OpenScientist final report](SCGB3A1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](SCGB3A1-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:11481438
2. PMID:11193762
3. PMID:16266985
4. PMID:15383627
5. PMID:12175512
6. PMID:15472908
7. PMID:17916741
8. PMID:12847263
9. PMID:30768367