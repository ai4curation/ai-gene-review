# RASA1/p120RasGAP: GAP-Independent Scaffolding Mechanism

**Research question:** What is the evidence for RASA1 functions independent of its catalytic Ras-GAP activity — especially p190RhoGAP recruitment, directed cell movement, and vascular development — and how should GO curation express a non-catalytic molecular function?

*Iteration 1. Literature-based synthesis. Citations are PubMed-cached abstracts (PMIDs verified); DOIs are provided where confidently known and **flagged as uncertain/uncached** otherwise.*

---

## 1. Summary (answer)

RASA1 has a genuine, mechanistically defined **GAP-independent scaffolding function**: through its tandem SH2 domains it directly, phosphotyrosine-dependently recruits p190RhoGAP (and assembles a FAK–RASA1–p190RhoGAP complex) to control RhoA-dependent cytoskeletal reorientation and **directed cell migration**, a role explicitly shown to be **separable from — and not requiring — Ras-GAP catalysis**. Recruitment is direct and high-affinity (Kd ≈ 0.3 µM), and partner binding leaves catalytic activity unchanged, so the two functions are cleanly separable at the molecular level. However, the recruitment/scaffold role is **not sufficient to explain the CM-AVM vascular phenotype**: developmental blood/lymphatic vascular disease from RASA1 loss is driven by the **catalytic (Ras-MAPK) arm** via collagen IV export, and the EPHB4–RASA1 physical interaction is dispensable for angiogenesis. For GO curation, the non-catalytic role should be expressed as a **specific, evidence-backed binding/scaffold molecular function**, scoped to migration/polarity — not recorded merely as a residual mechanism gap.

---

## 2. Catalytic Ras-GAP evidence (kept separate)

- **Vascular development / CM-AVM is Ras-dependent.** In endothelial cells (EC), RASA1 loss dysregulates Ras-MAPK, impairing collagen IV folding/export from the ER → EC apoptosis and defective angiogenesis. *Chen et al. 2019, PMID **31185000** (JCI Insight; DOI 10.1172/jci.insight.125940 — likely, uncertain).*
- **EPHB4–RASA1 act in the same catalytic pathway; physical interaction dispensable.** EPHB4-mutant mice expressing EPHB4 that cannot engage RASA1 (but retains kinase activity) had **normal angiogenesis**; RASA1/EPHB4 protect against CM-AVM "independent of physical interaction." *Chen et al. 2022, PMID **35015735** (JCI; DOI uncertain/uncached).*
- **Review of EPHB4–RASA1 negative regulation of Ras-MAPK.** *Chen et al. 2023, PMID **37259315** (ATVB; DOI uncertain).*
- **Second-hit somatic RASA1 inactivation in CM-AVM EC** confirms loss-of-function (catalytic) genetics. *Lapinski et al. 2018, PMID **29024832**.*

> These establish the **Ras-dependent (catalytic)** disease mechanism and are deliberately partitioned from the scaffold evidence below.

---

## 3. GAP-independent scaffold evidence

### 3.1 Direct, phosphotyrosine-dependent p190RhoGAP recruitment
- N-SH2 of RASA1 binds p190RhoGAP **pTyr-1105** via canonical FLVR arginine R207; **Kd = 0.3 ± 0.1 µM** (ITC). *Jaber Chehayeb et al. 2019, PMID **31891593** (J Struct Biol).*
- The **SH2-SH3-SH2 module simultaneously engages two proximal p190RhoGAP phosphotyrosines** with synergistic (avidity) binding and induced compaction — a selectivity mechanism. *Stiegler, Vish & Boggon 2022, PMID **36417908** (J Biol Chem).*
- RASA1 makes **distinct** SH2 interactions with doubly-phosphorylated partners p190RhoGAP, Dok1, EphB4; **these interactions do not impact catalytic activity.** *Vish, Stiegler & Boggon 2023, PMID **37507023** (J Biol Chem).* → **clean biochemical separation of scaffolding from catalysis.**
- FLVR-unique C-SH2 / methods: PMIDs **32540970**, **37668970**.

### 3.2 Directed cell movement requires the scaffold, not catalysis
- **Cornerstone separation-of-function:** In RasGAP-deficient cells, growth factor rescues spreading/Golgi/transport **Ras-dependently**, but stress-fiber/focal-adhesion turnover producing the elongate migratory morphology depends on the **constitutive RasGAP–p190 association, independent of Ras regulation**; disrupting the pTyr-mediated complex with p190 peptides suppresses migration. *Kulkarni et al. 2000, PMID **10769036** (J Cell Biol; DOI 10.1083/jcb.149.2.457 — likely, uncertain).*
- **FAK–RASA1–p190RhoGAP polarity complex:** FAK (pY397) drives SH2-mediated RASA1 recruitment and p190A phosphorylation, targeting the complex to leading-edge focal adhesions to transiently inhibit RhoA; loss abolishes polarity in fibroblasts, **endothelial** and carcinoma cells. *Tomar et al. 2009, PMID **19435801** (Nat Cell Biol; DOI uncertain).*
- Corroborating pathway/cross-talk context: β3-integrin/EGFR→Src→p190/p120 complex (**21937717**); Brk phosphorylation of p190 Y1105 promoting p190/p120 complex, migration, invasion (**18829532**); E-cadherin→membrane p190RhoGAP/p120RasGAP complex lowering RhoA (**20228844**).

### 3.3 Other non-catalytic RASA1 activities (context)
- Caspase-3 cleavage generates an N-terminal "fragment N" that drives an **Akt-dependent anti-apoptotic** response (independent of GAP catalysis). *Peltzer et al. 2013, PMID **23826368**.*

---

## 4. Supported vs. refuted hypotheses

| Hypothesis | Verdict | Key evidence |
|---|---|---|
| RASA1 has a Ras-GAP-catalysis-independent role in directed migration | **Supported** | Kulkarni 2000 (10769036); Tomar 2009 (19435801) |
| p190RhoGAP recruitment is direct & phosphotyrosine/SH2-dependent | **Supported** | 31891593; 36417908 |
| Scaffold binding is molecularly separable from catalysis | **Supported** | 37507023 |
| The p190 scaffold role is *sufficient* to explain CM-AVM vascular phenotype | **Refuted / not supported** | 35015735 (physical interaction dispensable); 31185000 (catalytic collagen IV arm) |
| GO should record the non-catalytic role only as a residual gap | **Refuted** | Discrete mechanism + BP link warrant a specific binding/scaffold MF annotation |

---

## 5. GO-curation guidance

- **Express a specific molecular function**, distinct from GAP catalysis (GO:0005096 Ras GTPase activator):
  - phosphotyrosine residue binding (GO:0001784) / SH2 adaptor-scaffold activity, evidence PMIDs 31891593, 36417908, 37507023 (IPI/IDA + structural).
  - Biological process: *regulation of cell migration / establishment of cell polarity* via RasGAP–p190RhoGAP, evidence 10769036, 19435801.
- **Retain as non-core binding/scaffold evidence**, and **scope BP annotations to migration/polarity** — do **not** annotate the scaffold to CM-AVM/angiogenesis pathogenesis, which the genetic separation-of-function assigns to the catalytic Ras-MAPK arm (35015735, 31185000).
- **Residual mechanism gap** remains for whether p190 recruitment is *sufficient in vivo* for vascular/migration phenotypes (existing in-vivo data point to catalysis for vasculature); flag this as an open annotation caveat.

---

## 6. Coordination / separation of Ras-dependent vs Ras-independent roles

Evidence supports **context-partitioned** roles rather than a single integrated switch: (i) **catalytic Ras suppression** governs EC survival and collagen IV homeostasis in developmental vasculature (CM-AVM); (ii) **non-catalytic SH2 scaffolding** of p190RhoGAP governs RhoA-dependent cytoskeletal reorientation for directed motility/polarity. Upstream tyrosine kinases (FAK/Src, EphB4, Brk, EGFR) generate the phosphotyrosines that toggle RASA1 between reading partners and localizing signaling — a spatial-temporal, not purely catalytic, layer of control (37507023).

---

## 7. Limitations & future directions

- Synthesis is abstract-level; **DOIs are flagged as uncertain/uncached** and several journal/DOI attributions were inferred, not verified.
- No direct in-vivo "SH2-scaffold-dead but GAP-intact" RASA1 knock-in exists in the retrieved literature to prove sufficiency of p190 recruitment for vascular/migration phenotypes — the key missing separation-of-function reagent.
- Most migration evidence is in fibroblast/carcinoma/EC culture; in-vivo relevance of the scaffold to human vascular disease remains unresolved (residual mechanism gap).
- Future: knock-in RASA1 SH2-binding mutants (R207/R231) vs GAP-dead (R789-type) alleles in EC-specific models to formally dissociate scaffold vs catalytic contributions to angiogenesis and migration.
