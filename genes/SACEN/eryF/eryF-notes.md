# eryF (Q00441, P450eryF / CYP107A1) — review notes

Part of the **BGC exemplar curation project** (`projects/BGC.md`) and the erythromycin
pathway concept (`terms/erythromycin_biosynthesis/`). MIBiG BGC0000055; GenBank CAM00071.1
→ UniProt **Q00441** (CP107_SACEN), gene *eryF*.

## Function — a genuine catalytic P450 (contrast with EryCII)

EryF is the cytochrome **P450eryF (CYP107A1)** that catalyzes the **C-6 hydroxylation of
6-deoxyerythronolide B (6-dEB) → erythronolide B (EB)**, an early post-PKS tailoring step of
erythromycin biosynthesis (EC **1.14.15.35**).

- "a cytochrome P-450 monooxygenase system is responsible for hydroxylation of
  6-deoxyerythronolide B to erythronolide B as part of erythromycin biosynthesis"
  [PMID:1732208 — Andersen & Hutchinson 1992].
- "Cytochrome P450eryF (CYP107A) from Saccharopolyspora erythraea catalyzes the hydroxylation
  of 6-deoxyerythronolide B" — crystal structures of the ferrous–dioxygen complex
  [PMID:15824115 — Nagano, Cupp-Vickery, Poulos 2005]. P450eryF is a classic structurally
  characterized bacterial P450 (it uniquely uses a substrate hydroxyl, not the canonical
  acid-alcohol pair, for proton delivery).

**Key contrast:** EryF carries the *same* GO P450 terms (monooxygenase, heme binding, iron ion
binding) as the pseudoenzyme **EryCII** — but for EryF they are **experimentally supported
(IDA)** and correct (intact heme-thiolate active site, solved structure), whereas EryCII lacks
the heme-ligating Cys and the heme. Same annotation set, opposite verdict (see
`genes/SACEN/eryCII/`, `projects/PSEUDOENZYMES.md`).

## Annotation review

All GOA terms are accurate and experimentally supported → **ACCEPT** (monooxygenase activity,
iron ion binding, heme binding — IEA + IDA; cytoplasm IEA — soluble bacterial P450;
oxidoreductase activity acting on paired donors with O2 — general parent; erythromycin
biosynthetic process IDA). No GO MF term exists for EC 1.14.15.35 → propose
"6-deoxyerythronolide B 6-hydroxylase activity".

## References
- PMID:1732208 — Andersen & Hutchinson 1992, *J Bacteriol*: eryF = 6-dEB hydroxylase. VERIFIED.
- PMID:15824115 — Nagano et al. 2005, *JBC*: P450eryF crystal structures / catalysis. VERIFIED.
