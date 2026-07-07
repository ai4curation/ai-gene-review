# FGFRL1: A Kinase-Dead FGF Receptor-like Protein — Mechanism of Signaling, Adhesion, and Fusion

**Research question.** How does human FGFRL1, an atypical kinase-dead fibroblast growth
factor receptor-like protein, modulate FGF/FGFR signaling and cell adhesion/fusion in vivo?
Which mechanistic model(s) — ligand/heparin-binding decoy, inhibitory FGFR-complex component,
cytoplasmic Sprouty/Spred scaffold, or adhesion/fusion molecule — are supported, and should
FGFRL1 receive the canonical Gene Ontology term *fibroblast growth factor receptor activity*?

> **Evidence provenance.** Findings below are drawn from **direct FGFRL1-specific experiments**
> (mostly the Trueb laboratory, Bern). Where I extend from canonical FGFR-family biology I flag it
> as **[FGFR-family inference]**. PMIDs are given for every claim; DOIs that I could not verify
> from the cached abstract metadata are flagged **[DOI uncached — verify]**.

---

## 1. Summary (answer)

FGFRL1 is best described as a **multifunctional, kinase-dead ectodomain receptor** whose in vivo
activity is carried almost entirely by its **extracellular Ig domains, not by intracellular
signal transduction**. Direct evidence supports three overlapping ectodomain-based roles — a
**ligand/heparin-binding decoy (ligand sink)**, a **constitutively dimeric, HSPG-dependent
adhesion molecule**, and an **active cell–cell fusogen** — while the **cytoplasmic Sprouty/Spred
scaffold is real biochemically but genetically dispensable in vivo**. Because FGFRL1 lacks the
tyrosine kinase domain and does not transduce FGF signals by transphosphorylation, assigning it
the canonical GO term *fibroblast growth factor receptor activity* (which denotes kinase-dependent
signal transduction) **overstates its function**; *FGF binding* + *heparin binding* + *cell
adhesion / cell–cell fusion / negative regulation of FGFR signaling* is the accurate annotation.

---

## 2. Key findings with statistical / experimental evidence

### 2.1 Ligand-sink / decoy model — **strongly supported (direct evidence)**
- The recombinant ectodomain **and** the membrane-bound receptor bind **FGF2, FGF3, FGF4, FGF8,
  FGF10, FGF22** with high affinity (ligand dot-blot, cell-based binding, surface plasmon
  resonance). The ectodomain is **proteolytically shed** near the membrane, releasing a soluble
  ligand-binding fragment, and **ectopic FGFRL1 antagonizes FGFR signaling in Xenopus embryos**
  (PMID **19920134**; Steinberg et al., 2010, *J Biol Chem* — [DOI uncached — verify]).
- Original characterization: FGFRL1 binds **heparin and FGF2** specifically and exerts a
  **negative effect on proliferation** in MG-63 cells (PMID **12813049**; Trueb et al., 2003,
  *J Biol Chem* — [DOI uncached — verify]).
- **FGF8 binds via the Ig2 domain** with very high affinity (rapid on-rate, slow off-rate;
  ELISA + Biacore); constructs lacking Ig2 bind poorly (PMID **33019532**; Zhuang et al., 2020,
  *Int J Mol Sci* — [DOI uncached — verify]).

### 2.2 Constitutive dimerization + HSPG-dependent adhesion — **strongly supported (direct)**
- FRET and co-precipitation of differentially tagged polypeptides show **constitutive homodimers**
  at the cell surface, enriched at **cell–cell contacts**. The ectodomain promotes **adhesion but
  not spreading**; adhesion is mediated by **cell-surface heparan sulfate**, is **specifically
  blocked by soluble heparin** (not other GAGs), is reduced by **heparin-binding-site mutagenesis**,
  and is neutralized by a **synthetic heparin-binding-site peptide**. The authors note FGFRL1
  "**resembles the nectins**" (PMID **18061161**; Rieckmann et al., 2008, *J Biol Chem* —
  [DOI uncached — verify]).
- Mechanistic significance: unlike canonical FGFRs, which **dimerize upon ligand + heparan
  sulfate engagement to trigger kinase activation** **[FGFR-family inference]**, FGFRL1 is
  **pre-dimerized** and uses HSPGs for adhesion in trans — decoupling dimerization from any
  kinase output.

### 2.3 Active cell–cell fusion via Ig3 + transmembrane domain — **supported (direct)**
- FGFRL1 is the **first mammalian protein shown to actively fuse cells** into large syncytia;
  cytoplasmic-mixing reporters map fusion to **Ig3 + transmembrane domain (necessary and
  sufficient)**, and FGFRL1-transfected HEK293/HeLa fuse with **untransfected CHO cells** —
  implying a **partner on the opposing membrane** (PMID **20851884**; Steinberg et al., 2010,
  *J Cell Sci* — [DOI uncached — verify]).
- Fusing contact sites form a **net-like structure with ~1 µm pores**, proposed fusion-pore
  precursors (PMID **21980560**; Trueb & Steinberg, 2011 — [DOI uncached — verify]).
- In vivo correlate: FgfrL1 is upregulated during myoblast→myotube fusion; **FgfrL1-null mice die
  at birth from a malformed diaphragm** and **specifically lack slow muscle fibers** (PMID
  **25172430**; Amann et al., 2014, *Dev Biol* — [DOI uncached — verify]).
- **Open question:** the identity of the **Ig3 trans-fusion partner is unknown**.

### 2.4 Cytoplasmic Sprouty/Spred scaffold — **real biochemically but genetically dispensable**
- The **C-terminal histidine-rich domain binds Spred1** and other Sprouty/Spred proteins (via
  their shared SPR domain; yeast two-hybrid + co-precipitation + membrane co-distribution), and
  Spred1 increases FGFRL1 plasma-membrane retention (PMID **21616146**; Zhuang et al., 2011 —
  [DOI uncached — verify]).
- **But** knock-in mice lacking the three conserved intracellular motifs (**FgfrL1ΔC-GFP**) are
  **viable, fertile, and phenotypically normal** (normal diaphragm and kidney) (PMID **25126760**;
  Bluteau et al., 2014 — [DOI uncached — verify]).
- Systematic domain-deletion mice: **intracellular-domain deletion → normal**; **Ig3 deletion →
  complete absence of metanephric kidneys**; **Ig2 deletion → hypoplastic kidneys**. The
  principal function is attributed to **Ig3** (with Ig2 contributing to ligand binding) (PMID
  **31923383**; Gerber et al., 2020, *Dev Biol* — [DOI uncached — verify]).

### 2.5 GO annotation verdict — canonical *FGF receptor activity* overstates FGFRL1
- Every primary source states FGFRL1 **lacks the tyrosine kinase domain required for FGF-mediated
  signal transduction by transphosphorylation** (PMID **12813049**, **19920134**, **40699684**).
- GO:0005007 *fibroblast growth factor receptor activity* denotes **combining with FGF and
  transmitting the signal across the membrane** — a kinase-dependent transduction activity FGFRL1
  does not perform. **Recommended annotations:** *fibroblast growth factor binding* (GO:0017134),
  *heparin binding* (GO:0008201), *cell-cell adhesion*, *cell-cell fusion / myoblast fusion*,
  and *negative regulation of fibroblast growth factor receptor signaling pathway*.

---

## 3. Supported vs. refuted hypotheses

| Model | Verdict | Basis |
|-------|---------|-------|
| Ligand/heparin-binding **decoy (ligand sink)** | **Supported** | Multi-FGF binding, ectodomain shedding, Xenopus antagonism (19920134); heparin/FGF2 binding (12813049); Ig2→FGF8 (33019532) |
| **HSPG-dependent adhesion** molecule (nectin-like) | **Supported** | Constitutive dimers + heparin-specific adhesion + mutagenesis (18061161) |
| **Active cell–cell fusogen** with unknown Ig3 partner | **Supported** | Ig3+TM necessary/sufficient, fuses untransfected cells (20851884, 21980560); slow-fiber/diaphragm phenotype (25172430) |
| **Inhibitory FGFR-complex** component (heterodimer with FGFR1–4) | **Plausible but not directly demonstrated** | Antagonism of FGFR signaling is shown (19920134), but a physical FGFRL1·FGFR complex is inferred, not proven in the cached literature **[FGFR-family inference]** |
| **Cytoplasmic Sprouty/Spred scaffold** as the essential mechanism | **Refuted (for in vivo essential function)** | ΔC mice normal (25126760); intracellular-deletion mice normal (31923383) — though Spred1 binding is real (21616146) |
| Canonical GO *FGF receptor activity* (kinase signal transduction) | **Refuted / overstated** | No kinase domain; no transphosphorylation (12813049, 19920134, 40699684) |

**Integrating view.** The decoy, adhesion, and fusion activities are **not mutually exclusive**;
they are three read-outs of the **same ligand/HSPG/partner-binding ectodomain**. Notably the
**Ig3 domain** is required for both **kidney development** and **fusion**, and **Ig2** carries
**FGF8 binding** — suggesting a domain-partitioned mechanism: Ig2 = ligand sink, Ig3 = trans
adhesion/fusion partner engagement.

---

## 4. Experiments that would distinguish the four models

1. **Ligand-sink vs. receptor-complex (separation of function).**
   Compare an **Ig2-only "ligand-trap" knock-in** (binds FGF8, cannot fuse) against an
   **Ig3-only knock-in** (fuses, weak ligand binding) in mice; if kidney rescue tracks with Ig3
   not with FGF sequestration, the essential role is adhesion/fusion, not ligand sink.
   Complement with **quantitative FGF8 gradient imaging** (reporter) in wild-type vs. FGFRL1-null
   metanephros to test whether FGFRL1 sharpens/limits the FGF8 field (ligand-sink prediction).

2. **Physical FGFRL1·FGFR complex.**
   **Co-IP / proximity-ligation / BioID or split-nanoluc** between endogenous FGFRL1 and FGFR1–4
   in nephrogenic cells ± FGF8/heparin; **cross-linking mass spec** on purified ectodomains.
   Functionally, test whether FGFRL1 **cis-inhibits FGFR autophosphorylation** in a defined
   co-expression system (pERK / pFRS2 dose–response) — distinguishes a true inhibitory-complex
   component from a purely extracellular ligand sink.

3. **Adhesion vs. fusion (is adhesion a fusion intermediate?).**
   Use **heparin-binding-site mutants** and **HSPG-deficient (e.g., Ext1/2-null or heparinase-
   treated) target cells** in the CHO trans-fusion assay: if HSPG loss abolishes adhesion but
   fusion persists, adhesion and fusion are separable; if both fail, HSPG bridging is the fusion
   trigger. Live-imaging of the ~1 µm net-like pores with membrane/cytoplasmic dyes to order
   adhesion → pore → mixing.

4. **Identify the Ig3 fusion partner (the central unknown).**
   **Recombinant FGFRL1-Ig3 ectodomain pulldown + mass spectrometry** from myoblast/diaphragm
   membranes; **CRISPR loss-of-function screen** in the CHO trans-fusion reporter (FGFRL1+ cells
   fuse with a genome-wide-KO CHO library — dropout identifies the required partner);
   **cell-surface expression cloning** for a factor conferring fusion competence on non-fusing
   cells. Validate candidate by conditional KO → expect diaphragm slow-fiber / syncytium defects
   phenocopying FgfrL1-null.

5. **Cytoplasmic contribution (already largely answered).**
   The ΔC and intracellular-deletion mice (25126760, 31923383) already show the tail is
   dispensable in vivo; a targeted test would be a **Spred1;FgfrL1 double-mutant** to ask whether
   Spred recruitment fine-tunes ERK output in a sensitized background without being essential.

---

## 5. Limitations and future directions

- Much of the mechanistic work is from **one laboratory** and relies on **overexpression and
  heterologous (CHO/HEK/Xenopus) systems**; endogenous-level, human, in-vivo confirmation is
  limited.
- A **physical FGFRL1·FGFR heterocomplex** is inferred but not directly demonstrated in the
  cached literature — the "inhibitory receptor-complex" model remains open.
- The **Ig3 fusion partner is unidentified**, leaving the fusion mechanism molecularly incomplete.
- **Cancer studies** (SCLC/ENO1–PI3K/Akt PMID 31957179; rectal/ovarian/ESCC MAPK PMID 32098557,
  29675438, 29963148; miR-210-3p PMID 37062273) report FGFRL1-linked signaling changes but are
  **correlative/knockdown** and may reflect context-specific or indirect effects rather than a
  cell-autonomous kinase activity.
- **DOIs were not machine-verifiable** from the available metadata and are flagged accordingly;
  PMIDs are authoritative.

---

## 6. Cited literature (PMIDs)

- **12813049** Trueb et al. 2003 — first characterization; heparin/FGF2 binding; decoy hypothesis.
- **18061161** Rieckmann et al. 2008 — constitutive dimers; HSPG-dependent adhesion; nectin-like.
- **19920134** Steinberg et al. 2010 — ectodomain shedding; binds FGF2/3/4/8/10/22; Xenopus antagonism.
- **20851884** Steinberg et al. 2010 — active cell fusion; Ig3+TM necessary/sufficient.
- **21080029** Trueb 2011 — review; high-affinity FGF/heparin binding; human craniosynostosis frameshift.
- **21616146** Zhuang et al. 2011 — Spred1/Sprouty binding via His-rich C-terminus.
- **21980560** Trueb & Steinberg 2011 — net-like pore structure during fusion.
- **23112089** Trueb et al. 2013 — kidney development; FGFRL1 interacts mainly with Fgf8.
- **25126760** Bluteau et al. 2014 — ΔC-GFP mice viable/normal (tail dispensable).
- **25172430** Amann et al. 2014 — required for slow muscle fibers.
- **31923383** Gerber et al. 2020 — domain-deletion mice; Ig3 essential for metanephric kidney.
- **33019532** Zhuang et al. 2020 — FGF8 binds via Ig2 (SPR/Biacore).
- **40699684** Guan et al. 2025 — recent review; kinase-dead, multifunctional.
- Cancer/context: 31957179, 32098557, 29675438, 29963148, 37062273 (correlative).
