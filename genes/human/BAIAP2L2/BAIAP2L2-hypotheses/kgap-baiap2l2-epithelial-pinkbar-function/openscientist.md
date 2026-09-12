# Native epithelial function of human BAIAP2L2/Pinkbar: an evidence audit

**Iteration 1 — literature synthesis (no primary data provided).**
Scope: distinguish *direct* BAIAP2L2 evidence from I-BAR-family/paralog inference; evaluate the
unresolved native intestinal/renal epithelial function; recommend GO curation stance.

---

## 1. Summary (answer to the research question)

The **native epithelial function of BAIAP2L2/Pinkbar in human intestine and kidney remains unresolved.**
There is solid *direct* biochemical and cell-biological evidence that BAIAP2L2 is an epithelial-expressed
I-BAR protein that binds membranes, generates **planar** (not tubular) membrane sheets, and localizes to
**Rab13-positive vesicles and intercellular junctions** — i.e., a demonstrable membrane-flattening/scaffold
*molecular function*. However, the corresponding **in-vivo physiological output is not established**:
`Baiap2l2`-knockout mice have normal kidney/colon morphology and normal electrolyte homeostasis **under basal
conditions only**, and no challenge, aging, or paralog-compound-knockout experiments have been reported.
The single well-established organ-level loss-of-function phenotype is **cochlear** (stereocilia maintenance /
deafness), which is mechanistically distinct from the epithelial junctional role.

---

## 2. Direct BAIAP2L2 evidence vs. paralog/I-BAR inference

### 2a. DIRECT epithelial evidence (BAIAP2L2 itself)
All direct native-epithelial evidence traces to **one** foundational paper:

- **Pykäläinen et al., 2011, *Nat Struct Mol Biol* — PMID 21743456; DOI 10.1038/nsmb.2079** (cached/validated abstract).
  - Specifically expressed in **intestinal epithelial cells**.
  - Localizes to **Rab13-positive vesicles** and to the **plasma membrane at intercellular junctions**.
  - I-BAR/IMD domain **does not tubulate** membranes but **promotes planar membrane sheets**.
  - Structure: **relatively flat lipid-binding interface**; assembles into **sheet-like oligomers** (crystals + solution)
    → mechanistic basis for planar deformation.
  - *Note:* phosphoinositide dependence is the expected I-BAR mechanism and is consistent with the flat basic
    lipid interface described here, but the abstract states "lipid-binding interface" rather than naming a specific
    PIP species; a strict phosphoinositide-specificity claim for BAIAP2L2 should be flagged **partially inferred**.

### 2b. PARALOG / I-BAR-FAMILY inference (NOT direct native-tissue proof)
- **Sudhaharan et al., 2016, *J Cell Sci* — PMID 27278019** (cached). Rif (Rho-family GTPase) signals through
  I-BAR proteins; explicitly groups **IRSp53 (BAIAP2), IRTKS (BAIAP2L1) and Pinkbar (BAIAP2L2)** as a morphology
  module. BAIAP2L2-specific downstream biology here is inferred from the family.
- **Tholen et al., 2023 — PMID 36520027**: BAIAP2L2 **binds BAIAP2 and BAIAP2L1** (mass spec) → heteromeric
  I-BAR assemblies plausible; supports **redundancy**.
- General I-BAR mechanism (negative-curvature/PIP2 binding of IRSp53) is a family property; applying it to
  BAIAP2L2 is inference **except** where Pinkbar's *divergent* flat-interface/planar behavior is directly shown (2a).

---

## 3. Why knockout mice look normal — and what has NOT been tested

**Tholen et al., 2023 (PMID 36520027)** (title: "HNF1β-associated cyst development and electrolyte disturbances
are not explained by BAIAP2L2"; journal *Pflügers Archiv / Eur J Physiol* — **DOI uncertain, flag for verification**):

- BAIAP2L2 is a **direct transcriptional target of HNF1β** (luciferase reporter validated).
- `Baiap2l2`-KO kidney epithelial cells: **normal F-actin at cell–cell contacts**; **normal polarized 3D spheroids** with lumen.
- `Baiap2l2`-KO mice: **normal kidney and colon morphology**; **normal serum and urine electrolytes** — but explicitly
  **"under physiological conditions."**

**Interpretation of the null phenotype (unresolved, not disproven):**
1. **Paralog redundancy** — BAIAP2L2 physically binds BAIAP2 and BAIAP2L1; single KO may be buffered.
   *Untested:* compound/double/triple I-BAR knockouts.
2. **Challenge-dependence** — only basal conditions assayed. *Untested:* low-Mg²⁺/high-salt diets, ischemia-reperfusion
   or nephrotoxic injury, colitis/DSS challenge, infection, or aged cohorts (note the cochlear phenotype is
   *progressive*, becoming overt by 8 months — an epithelial phenotype could likewise be age- or stress-gated).
3. **Sub-morphological/functional readouts not probed** — junction dynamics, barrier resealing after wounding,
   TER/paracellular permeability, Rab13-cargo trafficking kinetics.

---

## 4. Candidate epithelial partners, cargo, and structures

| Candidate | Evidence class | Source |
|---|---|---|
| **Rab13** (junction assembly, polarized transport) — leading candidate pathway | Direct co-localization (Pinkbar); independent Rab13 junction role | PMID 21743456; PMID 21795389, 24377937 |
| **BAIAP2 / BAIAP2L1** heteromers | Direct interaction (mass spec) | PMID 36520027 |
| **HNF1β** (upstream transcriptional driver) | Direct (ChIP/RNA-seq + reporter) | PMID 36520027 |
| Rho-GTPase **Rif** module | Family/paralog inference | PMID 27278019 |
| EGFR/c-Src/pAKT/MMP2/MMP9 axis | Non-native cancer cells, correlative | PMID 34695828 |
| EPS8/EPS8L2/TWF2/CAPZB2/CIB2/MYO15A | **Stereocilia-specific — NOT epithelial** | PMID 33151556, 34346063, 35044843 |

**No direct epithelial cargo or a specific junctional structure built by BAIAP2L2 has been identified.**
The strongest mechanistic hypothesis: a **Rab13-coupled, lipid-binding planar scaffold that flattens/stabilizes
membrane at nascent intercellular junctions**, potentially in heteromeric I-BAR assemblies.

---

## 5. The established (contrasting) cochlear function — keep separate
- **Carlton et al., 2021 — PMID 33151556**: KO mice lose stereocilia rows 2/3, lose MET current, deaf by 8 months;
  tip localization requires MYO15A + EPS8. (eLife/PLoS-class; **DOI flag for verification**.)
- **Yan et al., 2022 — PMID 34346063**: BAIAP2L2 is a "row 2 complex" component (binds EPS8L2, TWF2, CAPZB2, CIB2);
  tip localization requires CIB2.
- **Halford et al., 2022 — PMID 35044843**: BAIAP2L2–EPS8–MYO15A tripartite complex; row-2 tip retention depends on
  Ca²⁺ influx through transduction channels.
- **Ikäheimo et al., 2024 — PMID 39037943**: in stereocilia-fusion pathology BAIAP2L2 mislocalizes from tips.

These describe a **protrusion-tip actin-scaffold** function (negative-curvature geometry), mechanistically distinct
from the **planar-junction** epithelial activity. BAIAP2L2 thus operates in two different membrane geometries.

---

## 6. Supported vs. refuted hypotheses

**Supported (direct evidence):**
- BAIAP2L2 binds membranes and generates **planar sheets** via a flat lipid interface + sheet oligomers (PMID 21743456).
- BAIAP2L2 localizes to **Rab13 vesicles and epithelial junctions** (PMID 21743456).
- BAIAP2L2 is an **HNF1β target** and binds I-BAR paralogs (PMID 36520027).
- BAIAP2L2 maintains **cochlear stereocilia** (PMID 33151556, 34346063, 35044843).

**Refuted / not supported (basal conditions):**
- BAIAP2L2 is **required for basal renal/colonic morphology or electrolyte homeostasis** — **refuted** (PMID 36520027).
- BAIAP2L2 explains **HNF1β cyst/electrolyte phenotype** — **refuted** (PMID 36520027).

**Unresolved (open):**
- A specific native epithelial *biological process* / cargo / junctional structure.
- Challenge- or age-dependent epithelial phenotypes.
- Strict phosphoinositide-species specificity of BAIAP2L2 membrane binding.

---

## 7. GO-style curation recommendation

1. **Support a membrane-bending/scaffold molecular function.** Direct structural + in-vitro data justify MF terms such as
   *phosphatidylinositol/phospholipid binding* (with the caveat that a specific PIP species is inferred) and a
   *membrane deformation / planar membrane-sheet scaffolding* activity. This is the best-evidenced, BAIAP2L2-specific claim.
2. **Keep epithelial biological-process terms as inferred / non-core.** Localization to junctions/Rab13 vesicles is
   direct, but the *process* (junction assembly, epithelial morphogenesis, barrier function) has **no in-vivo support** and
   a KO shows no basal phenotype → annotate as **inferred/IEA-or-IMP-pending / non-core**, not established.
3. **Native epithelial function = "unresolved."** Do not assert a core epithelial physiological role; the honest curation
   status is *candidate/unresolved pending challenge and compound-KO data.*
4. **Do not transfer stereocilia partners (EPS8/CIB2/MYO15A etc.) to epithelium** — these are tissue-specific and would
   be an over-annotation.

---

## 8. Limitations & future directions
- **Limitation:** the entire direct epithelial case rests on a single 2011 paper; independent replication of planar-sheet
  activity and junction localization in human intestinal/renal tissue is lacking.
- **DOI caveat:** PMIDs are validated against cached PubMed abstracts. DOIs are provided where confidently known
  (Pykäläinen 2011 = 10.1038/nsmb.2079); other DOIs are **flagged uncertain** and should be verified before publication.
- **Priority experiments:** (i) compound BAIAP2/BAIAP2L1/BAIAP2L2 knockouts in gut/kidney; (ii) epithelial challenge
  models (injury, colitis, low-Mg/high-salt, aging); (iii) barrier/junction-dynamics and Rab13-cargo trafficking assays;
  (iv) defined phosphoinositide-binding specificity for the BAIAP2L2 I-BAR domain; (v) human intestinal/renal organoid
  localization and knockout phenotyping.

---

### Key citations (PMID / DOI / cache status)
- PMID **21743456** — Pykäläinen 2011, *Nat Struct Mol Biol* — DOI **10.1038/nsmb.2079** — cached ✔ (core direct evidence)
- PMID **36520027** — Tholen 2023 — DOI **uncertain (flag)** — cached ✔ (KO phenotype, HNF1β, paralog binding)
- PMID **27278019** — Sudhaharan 2016, *J Cell Sci* — DOI uncertain (flag) — cached ✔ (I-BAR/Rif family inference)
- PMID **33151556** — Carlton 2021 — DOI uncertain (flag) — cached ✔ (cochlear KO)
- PMID **34346063** — Yan 2022 — DOI uncertain (flag) — cached ✔ (row-2 complex)
- PMID **35044843** — Halford 2022 — DOI uncertain (flag) — cached ✔ (tripartite complex, Ca²⁺-dependent tip retention)
- PMID **39037943** — Ikäheimo 2024 — DOI uncertain (flag) — cached ✔ (stereocilia fusion mislocalization)
- PMID **34695828** — Shakery 2023 — DOI uncertain (flag) — cached ✔ (non-native cancer-cell, correlative)
- PMID **21795389** — Abou-Zeid 2011 / PMID **24377937** — Zahraoui 2014 — cached ✔ (Rab13 junction biology, context)
