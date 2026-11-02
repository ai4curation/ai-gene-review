---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T13:13:33.729141'
end_time: '2026-10-24T13:44:38.551291'
duration_seconds: 1864.82
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: LDOC1
  gene_symbol: LDOC1
  uniprot_accession: O95751
  protein_description: 'RecName: Full=Protein LDOC1; AltName: Full=Leucine zipper
    protein down-regulated in cancer cells;'
  gene_info: Name=LDOC1; Synonyms=BCUR1;
  organism_full: Homo sapiens (Human).
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
citation_count: 11
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: LDOC1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: LDOC1-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** O95751
- **Protein Description:** RecName: Full=Protein LDOC1; AltName: Full=Leucine zipper protein down-regulated in cancer cells;
- **Gene Information:** Name=LDOC1; Synonyms=BCUR1;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the LDOC1 family. .
- **Key Domains:** RTL1/1-8/LDOC_capsid-like. (IPR032549); RTL1-8_LDOC (PF16297)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "LDOC1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'LDOC1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **LDOC1** (gene ID: LDOC1, UniProt: O95751) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# LDOC1 (O95751): A Nuclear Retroelement-Derived Regulatory Adapter and Candidate Tumor Suppressor

**Gene:** LDOC1 (synonym BCUR1) · **Organism:** *Homo sapiens* · **Locus:** Xq27
**Protein:** Leucine zipper protein down-regulated in cancer cells (LDOC1), 146 aa
**Domain/family:** RTL1/1-8/LDOC capsid-like (InterPro IPR032549; Pfam PF16297); "LDOC1 family" — a retrotransposon-Gag-derived (RTL/MART) gene

---

## Summary

**LDOC1 is a small, 146-residue, X-linked (Xq27), predominantly nuclear protein that functions not as an enzyme or transporter but as a regulatory adapter.** Its primary molecular role is to serve as a negative regulator of pro-survival/pro-proliferative signaling and of chromatin state by directing the destabilization or proteasomal degradation of specific partner proteins. LDOC1 was originally identified by RNA differential display as a gene ubiquitously expressed in normal tissues but silenced in cancer cell lines, and it carries two recognizable interaction modules: an N-terminal leucine-zipper/coiled-coil motif and a proline-rich PxxP (SH3-binding) cluster, together with a strongly acidic C-terminal tail ([PMID: 10403563](https://pubmed.ncbi.nlm.nih.gov/10403563/)).

Mechanistically, LDOC1 converges on several growth- and survival-promoting pathways. It inhibits **NF-κB** signaling to promote apoptosis — binding and destabilizing the nucleolar GTPase GNL3L and reversing GNL3L-driven upregulation of the p65 NF-κB subunit, with its pro-apoptotic activity enhanced by the transcription factor MZF-1 ([PMID: 27764577](https://pubmed.ncbi.nlm.nih.gov/27764577/); [PMID: 27076087](https://pubmed.ncbi.nlm.nih.gov/27076087/)). It suppresses **JAK2/STAT3** signaling by routing phospho-JAK2 for degradation through the E3-ligase adapter LNX1 ([PMID: 30634502](https://pubmed.ncbi.nlm.nih.gov/30634502/)), and it suppresses **Wnt5a**-driven metastasis in osteosarcoma ([PMID: 28240050](https://pubmed.ncbi.nlm.nih.gov/28240050/)). Most recently, LDOC1 was shown to be a nuclear **epigenetic regulator** that controls global histone **H2B monoubiquitination (H2Bub1)** by promoting the proteasomal degradation of H2B/H2Bub1 via the proteasome subunit PSMA1, thereby shaping chromatin accessibility and tumor-cell plasticity ([PMID: 41484780](https://pubmed.ncbi.nlm.nih.gov/41484780/)).

Evolutionarily, LDOC1 is a **domesticated retrotransposon-Gag (capsid-like) gene**: UniProt/InterPro assign it the RTL1/1-8/LDOC capsid-like domain (IPR032549; Pfam PF16297), placing it in the same broad family of captured retroelement genes as the PNMA and RTL/SIRH genes ([PMID: 40263616](https://pubmed.ncbi.nlm.nih.gov/40263616/)). AlphaFold modeling confirms a compact, well-folded globular core (the capsid-like domain) plus a flexible, disordered acidic C-terminal tail. Across cancers (cervical, gastric, pancreatic, osteosarcoma, lung), LDOC1 is frequently silenced by promoter hypermethylation, and its loss is associated with increased aggressiveness and worse survival — consistent with a tumor/metastasis-suppressor role, although the direction of its expression and its subcellular pool are context-dependent.

---

## Key Findings

### Finding 1 — A small nuclear protein with defined interaction motifs, derived from a retrotransposon Gag gene

LDOC1 was originally cloned by RNA differential display as a gene down-regulated in cancer cell lines ([PMID: 10403563](https://pubmed.ncbi.nlm.nih.gov/10403563/)). It maps to chromosome Xq27 and encodes a 146-amino-acid protein. The predicted protein sequence showed *"no similarity to known sequences in the database except for a leucine zipper-like motif at the N-terminal region and a proline-rich region that shares marked similarity to an SH3-binding domain"* ([PMID: 10403563](https://pubmed.ncbi.nlm.nih.gov/10403563/)). Critically, an EGFP-LDOC1 fusion protein was *"localized in the nucleus,"* establishing nuclear localization experimentally in the earliest characterization of the gene.

The modern annotation adds an important evolutionary dimension: UniProt O95751 assigns LDOC1 the RTL1/1-8/LDOC capsid-like domain (InterPro IPR032549; Pfam PF16297), indicating that the gene is a member of the retrotransposon-Gag-like (RTL/MART) gene family. This means the "leucine zipper" and overall fold reflect an ancestral viral/retroelement capsid architecture that has been domesticated by the host genome.

### Finding 2 — A tumor-suppressor candidate silenced by promoter methylation across multiple cancers

LDOC1 shows a consistent expression pattern diagnostic of a tumor suppressor: it is ubiquitously expressed in normal human tissues but lost in cancer. Northern blot analysis *"revealed no expression in pancreatic and gastric cancer cell lines but ubiquitous expression in normal human tissues"* ([PMID: 10403563](https://pubmed.ncbi.nlm.nih.gov/10403563/)). The silencing mechanism is epigenetic: in cervical cancer, 4 of 6 cell lines silenced LDOC1, and PCR-based promoter methylation analysis *"revealed a significant association between promoter methylation and the loss of LDOC1 expression, which could be reverted by DNA methyltransferase inhibitors"* ([PMID: 24125169](https://pubmed.ncbi.nlm.nih.gov/24125169/)). Reversibility by DNMT inhibitors is a hallmark of promoter CpG-island hypermethylation-driven gene silencing. In osteosarcoma, loss of LDOC1 correlates with worse patient survival ([PMID: 28240050](https://pubmed.ncbi.nlm.nih.gov/28240050/)).

> **A note on context-dependence:** The tumor-suppressor model is not universal. In prostate cancer, LDOC-1 mRNA was reported *overexpressed* in LNCaP and PC-3 cancer cell lines relative to normal prostate lines, with cytoplasmic (not nuclear) staining ([PMID: 27698860](https://pubmed.ncbi.nlm.nih.gov/27698860/)), and in head-and-neck squamous cell carcinoma patients LDOC1 expression was increased ([PMID: 22825526](https://pubmed.ncbi.nlm.nih.gov/22825526/)). This indicates that LDOC1's role is tissue- and context-dependent, and that its subcellular distribution may track with its function.

| Cancer type | LDOC1 status | Mechanism / correlate | Reference |
|---|---|---|---|
| Pancreatic, gastric | Lost in cell lines | Downregulation vs. normal tissue | [PMID: 10403563](https://pubmed.ncbi.nlm.nih.gov/10403563/) |
| Cervical | Silenced (4/6 lines) | Promoter methylation, DNMT-reversible | [PMID: 24125169](https://pubmed.ncbi.nlm.nih.gov/24125169/) |
| Osteosarcoma | Loss → worse survival | ↓Wnt5a; ↑metastasis suppressors | [PMID: 28240050](https://pubmed.ncbi.nlm.nih.gov/28240050/) |
| Lung (NSCLC) | Loss → aggressiveness | ↑JAK2/STAT3; H2Bub1 dysregulation | [PMID: 30634502](https://pubmed.ncbi.nlm.nih.gov/30634502/); [PMID: 41484780](https://pubmed.ncbi.nlm.nih.gov/41484780/) |
| Prostate | Overexpressed (cytoplasmic) | Context-dependent, pro-apoptotic activity | [PMID: 27698860](https://pubmed.ncbi.nlm.nih.gov/27698860/) |

### Finding 3 — Primary molecular function: inhibitor of NF-κB signaling and pro-apoptotic regulator via protein interactions

LDOC1's best-established molecular function is as a **negative regulator of NF-κB signaling that promotes apoptosis.** The protein *"is a known regulator of nuclear factor mediated pathway to apoptosis through inhibition of nuclear factor kappa B (NF-kappaB)"* ([PMID: 27076087](https://pubmed.ncbi.nlm.nih.gov/27076087/)). This function is modulated by protein partners. The transcription factor myeloid zinc finger gene 1 (MZF-1) *"has been shown to interact with LDOC1 and to enhance LDOC1 activity favoring apoptosis"* ([PMID: 27076087](https://pubmed.ncbi.nlm.nih.gov/27076087/)).

The mechanistic link to NF-κB was defined through the interaction with the nucleolar GTPase GNL3L. LDOC1 directly binds GNL3L, and *"GNL3L upregulates NF-κB dependent transcriptional activity by modulating the expression of NF-κB subunit p65, which is reversed upon co-expression of LDOC1 with GNL3L"* ([PMID: 27764577](https://pubmed.ncbi.nlm.nih.gov/27764577/)). In other words, LDOC1 destabilizes GNL3L, thereby lowering p65 levels and suppressing NF-κB-dependent transcription and proliferation. This establishes a recurring theme: **LDOC1 acts by binding a partner and driving its destabilization.**

### Finding 4 — Suppression of JAK2/STAT3 and Wnt5a signaling to restrain cancer aggressiveness and metastasis

Beyond NF-κB, LDOC1 restrains two further oncogenic pathways. In lung cancer it is described as a *"Novel STAT3 Inhibitor LDOC1 [that] Targets Phospho-JAK2 for Degradation by Interacting with LNX1 and Regulates the Aggressiveness of Lung Cancer"* ([PMID: 30634502](https://pubmed.ncbi.nlm.nih.gov/30634502/)). Here LDOC1 behaves as an adapter that recruits the E3-ligase adapter LNX1 to phosphorylated JAK2, routing active JAK2 for degradation and thereby shutting down STAT3 signaling — again using a degrade-the-partner strategy.

In osteosarcoma, *"LDOC1 expression decreased Wnt5a levels"* and up-regulated metastasis-suppressor genes; LDOC1-expressing cells showed reduced migration and invasion, and *"increased LDOC1 expression is associated with weaker lung metastasis ability"* in xenografts, with higher LDOC1 correlating with better patient survival ([PMID: 28240050](https://pubmed.ncbi.nlm.nih.gov/28240050/)). In cervical cancer, restoring LDOC1 through the HAND2-AS1/miR-330-5p competing-endogenous-RNA axis inhibited proliferation, invasion, and metastasis; HAND2-AS1 sponges miR-330-5p to de-repress LDOC1, which then lowers Ki-67, PCNA, N-cadherin, and MMP-2/9 and reduces lymph-node metastasis ([PMID: 31889905](https://pubmed.ncbi.nlm.nih.gov/31889905/)).

### Finding 5 — A nuclear epigenetic regulator controlling histone H2B monoubiquitination (H2Bub1)

The most mechanistically detailed study to date places LDOC1 at the chromatin level. In non-small-cell lung cancer, *"although it lacks a canonical nuclear localization signal, it predominantly localizes to the nucleus in NSCLC cells,"* and its loss causes broad transcriptomic changes ([PMID: 41484780](https://pubmed.ncbi.nlm.nih.gov/41484780/)). Mechanistically, *"LDOC1 interacts with histone H2B and H2Bub1 as well as with PSMA1 to promote their proteasomal degradation, thereby limiting global H2Bub1 levels"* ([PMID: 41484780](https://pubmed.ncbi.nlm.nih.gov/41484780/)).

Intriguingly, LDOC1 knockdown *increases* total global H2Bub1 but *reduces* chromatin-bound H2Bub1 and enhances chromatin compaction — effects partially mediated by an LDOC1–THAP12 interaction. The study used an integrated suite of methods (ChIP-seq, ATAC-seq, MNase assays, co-immunoprecipitation, and proximity ligation), making this the strongest mechanistic evidence for LDOC1's role as a chromatin/proteasome adapter linking histone ubiquitination to tumor-cell plasticity.

### Finding 6 — A member of the domesticated retrotransposon-derived (Gag/capsid-like) gene family

LDOC1's capsid-like domain (IPR032549; Pfam PF16297) places it among retrotransposon-Gag-derived genes that have been "domesticated" by the host genome. The general principle is that *"mutation of a deteriorating retrotransposon can result in a gene that provides a selective advantage to the host in a process termed 'domestication'"* ([PMID: 40263616](https://pubmed.ncbi.nlm.nih.gov/40263616/)). The same study shows that related retrotransposon-derived capsid genes (PNMA1, PNMA4) retain the ancestral ability to form capsid-like structures and are required to maintain reproductive capacity in mammals — illustrating that this gene family can acquire essential, non-transposon host functions. For LDOC1, the retained capsid-like fold likely provides a stable protein-interaction scaffold now repurposed for host regulatory functions.

### Finding 7 — Domain architecture: leucine-zipper/coiled-coil, PxxP SH3-binding cluster, and acidic C-terminal tail

Analysis of the 146-residue sequence (UniProt O95751) confirms three functional modules:

1. **N-terminal leucine/arginine-rich segment (res ~1–45)** — leucines at positions 5, 7, 8, 9, 13, 26, 31, 32, 39, 40, consistent with a leucine-zipper/coiled-coil dimerization motif. Leucine is the most abundant residue overall (20/146).
2. **Proline-rich cluster (res ~46–54; prolines at 46, 47, 50, 52, 54; sequence RPPSCPVPFP)** — a classic SH3-binding PxxP region.
3. **Strongly acidic C-terminal tail** (…DDDEDDDDEEEEDDY), ~59% Asp/Glu over the last 27 residues; Glu+Asp together account for 32/146 residues.

These features recapitulate the original observation of *"a leucine zipper-like motif at the N-terminal region and a proline-rich region that shares marked similarity to an SH3-binding domain"* ([PMID: 10403563](https://pubmed.ncbi.nlm.nih.gov/10403563/)). Functionally, the leucine zipper enables homo/hetero-dimerization, the PxxP motif recruits SH3-domain partners, and the acidic tail is a common feature of chromatin/transcription adapters (acidic activation/interaction surfaces).

### Finding 8 — An interactome converging on chromatin/transcription machinery and the proteasome

Curated IntAct/UniProt protein–protein interactions for LDOC1 (O95751) are strikingly enriched for nuclear regulators. These include:

- **Chromatin remodelers/corepressors:** AEBP2 (PRC2 cofactor), MBD3 (NuRD), HDAC4, SUDS3 (SIN3), DPF2 and SMARCD1 (SWI/SNF-BAF), MEAF6 (MOZ/HBO1 HAT), THAP7, TLE5/AES (Groucho corepressor), NRIP1.
- **Zinc-finger transcription factors:** ZBTB16, ZBTB24, and many others.
- **Proteasome components:** PSMA1 and PSMF1.
- **Validated functional partners:** GNL3L, and PEG10 — another retrotransposon-derived (SIRH/Mart) gene product.

This interactome strongly supports LDOC1's identity as a **nuclear regulatory adapter** that bridges transcription-factor/chromatin complexes to the proteasome, consistent with the degrade-the-partner mechanism seen for GNL3L, JAK2, and H2B/H2Bub1. These interactions are largely from high-throughput curation and most remain individually unvalidated.

### Finding 9 — AlphaFold predicts a well-folded capsid-like core plus a disordered acidic tail

The AlphaFold model of O95751 (AF-O95751-F1) has a high mean pLDDT of 90.8, with 78.8% of residues at very-high confidence (>90) and none at very-low confidence. Per-residue confidence is high/very-high across residues ~1–120 (window means 89–98), indicating a compact ordered domain, and drops sharply in the C-terminal acidic tail (residues ~130–146, mean pLDDT ≈ 55–60), indicating a flexible/disordered extension. This structural prediction matches the InterPro RTL1/1-8/LDOC capsid-like domain assignment (IPR032549; Pfam PF16297) — a globular capsid-derived fold followed by an intrinsically disordered acidic region that likely mediates transient regulatory interactions.

---

## Mechanistic Model / Interpretation

The picture that emerges is coherent across all nine findings: **LDOC1 is a nuclear, retroelement-derived scaffolding/adapter protein whose principal output is the negative regulation of pro-survival signaling and chromatin state, achieved by promoting the destabilization or degradation of its binding partners.**

```
                      LDOC1 (146 aa, nuclear, X-linked Xq27)
         ┌────────────────────────────────────────────────────────────┐
         │  LeuZip/coiled-coil │  PxxP (SH3-bind) │  acidic C-tail       │
         │   (res ~1–45)       │   (res ~46–54)   │ (DDD...EEE, flexible)│
         └──────────┬──────────┴────────┬─────────┴────────┬────────────┘
                    │ dimerization       │ SH3 partners      │ acidic
                    ▼                     ▼                   ▼ interactions
   ┌─────────────────────────────────────────────────────────────────────┐
   │              NUCLEAR REGULATORY ADAPTER  (degrade-the-partner)         │
   └───────────┬───────────────┬─────────────────┬────────────────────────┘
               │               │                 │
   NF-κB axis  │   JAK2/STAT3  │   Wnt5a axis     │   Chromatin / H2Bub1
   ──────────  │   ──────────  │   ──────────     │   ──────────────────
   binds GNL3L │   binds LNX1  │   lowers Wnt5a   │   binds H2B/H2Bub1 +
   → destabil- │   (E3 adapter)│   → ↑metastasis- │   PSMA1 → proteasomal
   izes GNL3L  │   → degrades  │   suppressor     │   degradation; limits
   → ↓p65      │   pJAK2       │   genes          │   global H2Bub1;
   → ↓NF-κB    │   → ↓STAT3    │                  │   THAP12-dependent
   → APOPTOSIS │   → ↓aggress. │   → ↓metastasis  │   chromatin compaction
   (MZF-1 ↑)   │               │                  │
   ───────────────────────────────────────────────────────────────────────
                      NET EFFECT: tumor/metastasis suppression
                 (context-dependent; silenced by promoter methylation)
```

Three unifying principles tie the data together:

1. **LDOC1 is an adapter, not an enzyme.** It has no catalytic domain; its AlphaFold-predicted fold is a capsid-like scaffold, and its function in every well-characterized case is to bind a partner and change that partner's fate (stability, localization, or degradation). The recurrent involvement of proteasome subunits (PSMA1, PSMF1) and an E3-ligase adapter (LNX1) in its mechanism is the signature of a degradation-targeting adapter.

2. **LDOC1 operates predominantly in the nucleus/chromatin**, despite lacking a canonical NLS — nuclear import is likely piggybacked via its many chromatin/transcription-factor partners. Its interactome (PRC2, NuRD, SIN3, SWI/SNF, HAT complexes, zinc-finger TFs) and its direct control of H2Bub1 firmly locate its primary activity on chromatin. The cytoplasmic staining reported in prostate tissue ([PMID: 27698860](https://pubmed.ncbi.nlm.nih.gov/27698860/)) may reflect a distinct, context-dependent pool.

3. **LDOC1's domesticated-retroelement origin explains its architecture.** The capsid-like Gag domain provides a robust oligomerization/interaction platform; the host has repurposed this scaffold — plus an acquired acidic disordered tail — into a chromatin/signaling regulator, paralleling how related RTL/PNMA/PEG10 genes acquired essential host functions.

---

## Evidence Base

| PMID | Title (abbreviated) | Contribution to the model |
|---|---|---|
| [10403563](https://pubmed.ncbi.nlm.nih.gov/10403563/) | *Identification of a novel gene, LDOC1, down-regulated in cancer cell lines* | Foundational: cloning, Xq27, 146-aa, leucine zipper + SH3-binding motif, **nuclear localization** (EGFP), loss in pancreatic/gastric cancer vs. ubiquitous normal expression. |
| [24125169](https://pubmed.ncbi.nlm.nih.gov/24125169/) | *Loss of LDOC1 expression by promoter methylation in cervical cancer cells* | Establishes epigenetic silencing mechanism; methylation significantly associated with loss, reversible by DNMT inhibitors. |
| [27764577](https://pubmed.ncbi.nlm.nih.gov/27764577/) | *LDOC1 interacts with GNL3L to modulate NF-κB signaling* | Direct mechanism for NF-κB inhibition: LDOC1 destabilizes GNL3L, reversing GNL3L-driven p65 upregulation. |
| [27076087](https://pubmed.ncbi.nlm.nih.gov/27076087/) | *LDOC1 Gene Expression in Men With Klinefelter Syndrome* | States LDOC1's NF-κB-inhibitory, pro-apoptotic function and the MZF-1 interaction enhancing its activity. |
| [30634502](https://pubmed.ncbi.nlm.nih.gov/30634502/) | *Novel STAT3 Inhibitor LDOC1 Targets Phospho-JAK2 for Degradation by Interacting with LNX1...* | Mechanism for JAK2/STAT3 suppression via LNX1-mediated pJAK2 degradation. |
| [28240050](https://pubmed.ncbi.nlm.nih.gov/28240050/) | *LDOC1 regulates Wnt5a expression and osteosarcoma cell metastasis...* | In vivo metastasis-suppressor role; LDOC1 lowers Wnt5a and reduces lung metastasis; loss correlates with worse survival. |
| [31889905](https://pubmed.ncbi.nlm.nih.gov/31889905/) | *HAND2-AS1 inhibits invasion/metastasis via miR-330-5p-mediated LDOC1* | ceRNA axis restoring LDOC1 suppresses proliferation/invasion/metastasis in cervical cancer. |
| [41484780](https://pubmed.ncbi.nlm.nih.gov/41484780/) | *LDOC1 connects histone H2B monoubiquitination to tumor cell plasticity in NSCLC* | Strongest mechanistic study: nuclear localization without NLS; LDOC1 + PSMA1 degrade H2B/H2Bub1; THAP12-dependent chromatin effects. |
| [40263616](https://pubmed.ncbi.nlm.nih.gov/40263616/) | *The retrotransposon-derived capsid genes PNMA1 and PNMA4 maintain reproductive capacity* | Establishes the domesticated-retroelement-capsid gene family and the "domestication" concept for LDOC1's family. |
| [27698860](https://pubmed.ncbi.nlm.nih.gov/27698860/) | *LDOC-1 gene expression in prostate cancer* | Context-dependent counterpoint: LDOC1 overexpressed and cytoplasmic in prostate cancer. |
| [22825526](https://pubmed.ncbi.nlm.nih.gov/22825526/) | *LDOC1 expression in HNSCC and Parkinson's disease* | Context-dependent: increased LDOC1 associated with pro-apoptotic activity in HNSCC. |

**Structural/bioinformatic evidence (database-derived):** UniProt O95751; InterPro IPR032549 and Pfam PF16297 (RTL1/1-8/LDOC capsid-like domain); AlphaFold model AF-O95751-F1 (mean pLDDT 90.8); and curated IntAct/UniProt interaction records underpin Findings 6–9. These are supportive inference rather than direct experimental assays.

---

## Limitations and Knowledge Gaps

1. **No catalytic/biochemical reaction.** LDOC1 is not an enzyme or transporter; there is no substrate-specificity question in the classical sense. Its "substrate" is better understood as its set of protein partners whose stability it modulates. The precise biochemical step by which LDOC1 promotes partner degradation (does it bridge substrates to E3 ligases/the proteasome? does it alter conformation?) remains to be defined structurally.

2. **Mechanism of nuclear import is unresolved.** LDOC1 lacks a canonical NLS yet is predominantly nuclear ([PMID: 41484780](https://pubmed.ncbi.nlm.nih.gov/41484780/)). Whether import depends on partner piggybacking, the leucine zipper, or an unconventional signal is unknown.

3. **Context-dependent / contradictory expression data.** The tumor-suppressor model holds in cervical, gastric, pancreatic, osteosarcoma, and lung contexts, but prostate and HNSCC data show the opposite direction of expression and a cytoplasmic pool ([PMID: 27698860](https://pubmed.ncbi.nlm.nih.gov/27698860/); [PMID: 22825526](https://pubmed.ncbi.nlm.nih.gov/22825526/)). The determinants of LDOC1's cell-type-specific role and localization are not understood.

4. **Interactome is largely high-throughput.** Many of the chromatin-complex interactions (AEBP2, MBD3, SWI/SNF, etc.) derive from curated large-scale datasets and have not been individually validated or functionally dissected. Only GNL3L, LNX1, MZF-1, H2B/H2Bub1, PSMA1, and THAP12 are experimentally supported partners.

5. **Normal physiological function is poorly defined.** Nearly all data come from cancer models. The native role of LDOC1 in normal tissues (where it is ubiquitously expressed) and any developmental/reproductive function analogous to its RTL/PNMA relatives are unexplored.

6. **No experimental 3D structure.** All structural claims rest on AlphaFold prediction and domain homology; no crystal/cryo-EM structure of LDOC1 (alone or in complex) exists, and whether it retains capsid-forming/oligomerization ability is untested.

---

## Proposed Follow-up Experiments / Actions

1. **Define the degradation machinery.** Test directly whether LDOC1 acts as a substrate-recognition adapter for specific E3 ligases or for the 20S/26S proteasome. IP-MS of LDOC1 under proteasome inhibition, plus in vitro reconstitution of GNL3L/H2Bub1 degradation, would establish the biochemical mechanism.

2. **Map the nuclear-import route.** Mutagenize the leucine zipper and acidic tail, and deplete candidate carrier partners, to identify how a no-NLS protein reaches the nucleus.

3. **Validate the chromatin interactome.** Co-IP and proximity-ligation validation of the PRC2/NuRD/SIN3/SWI/SNF/HAT interactions, followed by functional epistasis with H2Bub1 regulation, to determine which are physiologically relevant.

4. **Resolve the context-dependence.** Systematically compare LDOC1 localization (nuclear vs. cytoplasmic) and function across prostate, HNSCC, cervical, and lung models, correlating with partner availability (e.g., GNL3L, LNX1, THAP12) and post-translational modifications.

5. **Test capsid/oligomerization activity.** Use the AlphaFold-predicted capsid-like core and relatedness to PNMA1/PNMA4 ([PMID: 40263616](https://pubmed.ncbi.nlm.nih.gov/40263616/)) to ask, by negative-stain/cryo-EM and SEC-MALS, whether LDOC1 self-assembles — which would reframe its scaffolding mechanism.

6. **Solve an experimental structure**, ideally of LDOC1 bound to a validated partner (GNL3L or H2B/H2Bub1), to reveal the interaction surfaces used by the leucine zipper, PxxP motif, and acidic tail.

7. **Define the normal physiological role** via conditional knockout in mouse, with attention to reproductive/developmental phenotypes given the gene family's evolutionary history.

---

## Conclusion

LDOC1 (O95751) is best described as a **small, X-linked, predominantly nuclear regulatory adapter derived from a domesticated retrotransposon Gag/capsid gene.** It is not an enzyme or transporter; rather, through its leucine-zipper, SH3-binding PxxP motif, acidic tail, and capsid-like scaffold, it binds specific partners and promotes their destabilization/proteasomal degradation. This single biochemical logic underlies its convergent suppression of NF-κB (via GNL3L/p65, with MZF-1), JAK2/STAT3 (via LNX1), and Wnt5a signaling, and its control of histone H2B monoubiquitination (via PSMA1/THAP12). These activities make it a context-dependent tumor- and metastasis-suppressor that is frequently silenced by promoter hypermethylation across cancers.


## Artifacts

- [OpenScientist final report](LDOC1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](LDOC1-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:10403563
2. PMID:27764577
3. PMID:27076087
4. PMID:30634502
5. PMID:28240050
6. PMID:41484780
7. PMID:40263616
8. PMID:24125169
9. PMID:27698860
10. PMID:22825526
11. PMID:31889905