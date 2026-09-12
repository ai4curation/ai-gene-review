---
title: "Pseudoenzymes: Catalytically Dead, Functionally Alive"
marp: true
theme: default
paginate: true
backgroundColor: #fff
style: |
  section { font-size: 24px; }
  h1 { color: #2c3e50; }
  h2 { color: #34495e; }
  table { font-size: 18px; }
  section.lead h1 { font-size: 48px; }
---

<!-- _class: lead -->

# Pseudoenzymes

### Catalytically dead enzyme homologs — ~10% of eukaryotic enzyme families

Chris Mungall | AI-Assisted Gene Review

2026-06-22

---

## Why this matters

- Automated annotation pipelines (InterPro2GO, EC2GO, UniRule, ARBA, Pfam) propagate **enzyme activity from family membership** — without checking catalytic-residue conservation.
- For pseudoenzymes this produces a **systematic class of over-annotation**:
  - Molecular function: e.g. GO:0004784 (SOD activity), GO:0032452 (histone demethylase activity)
  - Downstream BP: e.g. GO:0019430 (removal of superoxide radicals), GO:0070076 (histone lysine demethylation)
  - Cofactor/binding: e.g. GO:0005506 (iron ion binding), GO:0020037 (heme binding)
- Catalytic loss does **not** mean loss of function — many pseudoenzymes neofunctionalize.

---

## What is a pseudoenzyme?

- A protein that retains the **fold** (and often substrate/metal-binding capacity) of an enzyme family but has **lost canonical catalysis**.
- **NOT a pseudogene** — expressed, stably folded, often under selection.
- Estimated **~10% of eukaryotic enzyme families** contain ≥1 pseudoenzyme; higher in kinases and proteases.
- Manning et al. 2002 first identified **~10% of the human kinome** as pseudokinases.
- Typical fates: new molecular function, residual/weak activity, regulator of the parental family, unknown function, or neutral decay.

---

## How pseudoenzymes arise — functional types

(Murphy et al. 2017; Ribeiro et al. 2019)

| Type | Role | Examples |
|------|------|----------|
| 1 | Allosteric activator of active paralog | HER3/ErbB3, STRAD, KSR1 |
| 2 | Scaffold / signaling hub | TRIB1/2/3, ILK |
| 3 | Regulator / decoy / competitor | iRhom1/2, CCS |
| 4 | Substrate binding / sequestration | PSMA, pseudo-phosphatases |
| 5 | Reader / recognition without modifying | Epe1, MLL3/KMT2C |
| 6 | Unknown / novel function | many pseudokinases |
| 7 | Degraded / neutral decay | hard to tell from Type 6 |

---

## The approach: AI gene review framework

Detect, then re-annotate. The curation decision tree:

1. **Confirm the family** (Pfam/InterPro) — a "broken" Cu/Zn SOD may be a normal Mn-SOD.
2. **Check catalytic residues** (M-CSA / literature).
3. **Check motif patterns** (PROSITE/PRINTS) — flanking context, not just residues.
4. **Check literature** for biochemical assay data.
5. **Propose a NEW annotation** for the actual non-catalytic function.

Outcome: over-annotated catalytic terms → MARK_AS_OVER_ANNOTATED / REMOVE; real role → NEW.

---

## Detection methodology

- **Direct catalytic-residue conservation** — align to a canonical member; simple but misses context defects.
- **PROSITE motif matching** — requires catalytic *and* flanking residues (structural geometry). e.g. Cu/Zn SOD PS00087 (Cu signature), PS00332 (disulfide signature).
- **M-CSA-based scoring** — PseudoHunter (Byrne et al. 2020); Ribeiro et al. 2019.
- **HMM-based scoring** — check conservation at catalytic columns (e.g. Epe1 JmjC).
- **Structural analysis** — metal geometry, active-site accessibility, rescue mutagenesis.
- **Family resources** — Pseudokinase DB/KLIFS, MEROPS "non-peptidase homologs", CAZy.

---

## Finding 1: Cu/Zn SOD family in a tardigrade

*Ramazzottius varieornatus* — expanded SOD family (~10 paralogs), substantial pseudoenzyme content.

| Gene (UniProt) | Status | Evidence |
|----------------|--------|----------|
| **RvSOD15** (A0A1D1VU85) | **Confirmed pseudoenzyme** | V87 replaces catalytic His; V87H rescue failed (loop dynamics) — PMID:37358501 |
| RvY_00650 / 03757 / 17310 | Probable pseudoenzyme | Cu His preserved but PROSITE PS00087 fails |
| RvY_15948 (A0A1D1VWP9) | **Not a SOD** — CCS-like chaperone | H46→A, H48→C; no PROSITE match |

**Insight:** ~half the expanded repertoire is non-catalytic or chaperone — "more copies = more antioxidant capacity" is only partly true.

---

## Finding 2: Epe1 — paradigmatic Type 5 "reader"

*S. pombe* Epe1 (UniProt O94603) — confirmed JmjC pseudo-demethylase.

- **Defect:** degenerate Fe(II) motif (HVD instead of HxD); missing catalytic residues.
- **Biochemistry:** no detectable H3K9me removal; H297A "catalytic" mutant still works.
- **Actual function:** anti-silencing factor — recruits SAGA / Bdf2 to heterochromatin boundaries; reads H3K9me, does not erase it.
- **Removed:** GO:0032452 (demethylase), GO:0051213 (dioxygenase), GO:0005506 (iron binding), GO:0070076 (demethylation).
- **Added:** GO:0042393 (histone binding), GO:0140030 (modification-dependent protein binding).

(Raiymbek et al. 2020; Bao et al. 2019)

---

## Finding 3: EryCII — a P450 that activates a glycosyltransferase

*S. erythraea* EryCII (DesVIII/EryCII family) — Type 1 with a twist.

- **Defect:** lacks the heme-ligating Cys and the heme group; PDB **2YJN is apo**. Structure-based alignment vs CYP125 → "not active P450 enzymes" (PMID:22056329); UniProt CAUTION "lacks the heme-binding sites".
- **Actual function:** allosteric activator + stabilizer of glycosyltransferase **EryCIII** (α2β2 heterotetramer); EryCIII is inactive without it. Activates a **non-homologous** partner.
- **Removed:** GO:0004497, GO:0016705, GO:0005506, GO:0020037.
- **Added:** GO:0008047 (enzyme activator), GO:0050821 (protein stabilization), GO:0032991 (complex), GO:1901115 (erythromycin biosynthesis).

---

## Finding 4: "Pseudo-ketosynthases" — structural subunits

Condensing-enzyme folds that lost the catalytic Cys and became required, non-catalytic subunits:

- **PqsB** (*P. aeruginosa*): FabH/KAS-III-fold partner of catalytic PqsC; active-site Cys-129/His-269 live in PqsC. IEA acyltransferase → MARK_AS_OVER_ANNOTATED (contributes_to). (PMID:24239007, PMID:26811339)
- **ActI-ORF2 / KSβ-CLF** (*S. coelicolor*): actinorhodin type II PKS **chain-length factor** — a ketosynthase descendant that "does not have an active site" yet sets chain length (PMID:15286722). Proposed new MF: "polyketide chain length factor activity".

---

## Not every "inactive" protein is a pseudoenzyme

Important clarifications from the review set:

- **AlgG** (*P. putida*): supports polymer formation even when catalytically inactive — but is normally a functional C5-epimerase. **Dual-function**, not a pseudoenzyme.
- **CipA** (*A. thermocellum*): a *bona fide* non-enzymatic scaffoldin (cohesin domains) — never derived from a catalytic ancestor.

And beware cross-family misassignment: **RvY_01767** looked like a degraded Cu/Zn SOD but is a canonical **Mn-SOD** (IPR001189) — always confirm the family first.

---

## Challenges

- **Dead vs active is subtle.** All catalytic residues can be intact yet the enzyme is dead — RvSOD15 V87H rescue failed because a nearby flexible loop destabilized coordination. Sequence-only checks miss this.
- **IBA/IEA propagation pitfalls.** Pfam membership ≠ catalytic activity; downstream BP and pathway terms get co-propagated and must be removed *together*.
- **Decay-in-progress vs stable pseudoenzyme** needs dN/dS, expression, and functional data to distinguish.
- **Verify the family** before declaring a pseudoenzyme — a "broken" enzyme may belong to a different family.

---

## Conclusions & future directions

- Pseudoenzymes are a common, systematic source of homology-driven **over-annotation** — and an opportunity to capture **real neofunctionalized roles** (scaffold, activator, reader, chaperone).
- The **three-check rule** — catalytic residues + flanking context + biochemistry — reliably flags candidates; reusable Cu/Zn SOD and JmjC pipelines exist.
- **Future work:** generic `pseudoenzyme-screen.py` (Pfam ID + canonical member → screen paralogs); programmatic M-CSA access; a curated pseudoenzyme TSV; add mammalian pseudokinases; quantify the PANTHER/IBA over-annotation rate.

Status: **MATURE** — flagship pipeline project.
