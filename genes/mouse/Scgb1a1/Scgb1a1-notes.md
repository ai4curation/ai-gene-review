# Mouse Scgb1a1 (uteroglobin / CC10 / CC16, UniProt Q06318) — curation notes

Prototype secretoglobin (SCGB1A1), curated as a comparator to the cat Fel d 1
secretoglobin allergen (FELCA/CH1, CH2). Uteroglobin is the family archetype.

## Identity
- UniProt Q06318, `UTER_MOUSE`, gene `Scgb1a1` (synonyms Cc10, Ugb, Utg).
- Names: uteroglobin; Clara/club cell 10 kDa secretory protein (CC10/CCSP);
  club cell 17 kDa protein; PCB-binding protein.
- Secreted, disulfide-linked antiparallel homodimer; uteroglobin fold with a
  hydrophobic ligand cavity [UniProt SUBUNIT/SIMILARITY].

## Molecular function (known)
- **Potent phospholipase A2 inhibitor** — the defining biochemical activity and
  the basis of its anti-inflammatory effect [UniProt FUNCTION "potent inhibitor of
  phospholipase A2"]. Added as NEW MF GO:0019834.
- **Phospholipid binding** — binds phosphatidylcholine, phosphatidylinositol
  [UniProt "Binds phosphatidylcholine, phosphatidylinositol"]. Added NEW GO:0005543.
- **PCB binding** (GO:0097160) — binds polychlorinated biphenyls; xenobiotic
  sequestration ("PCB-binding protein"). GOA IEA/ISO → ACCEPT.
- **Progesterone/steroid binding — weak, doubtful physiological relevance.** Mouse
  CC10 binds progesterone 27% less than rat, 48% less than rabbit uteroglobin
  [PMID:8440203 "casts doubt on the importance of such binding as a physiologic"].
  Not added as a core function.

## Biological process / immunomodulation
- Hung et al. 2004 (PMID:15356574, abstract only): CC10 dose-dependently suppresses
  Th2 cytokines IL-4/IL-5/IL-13 (not IFN-gamma), reduces GATA-3, decreases GATA-3
  mRNA stability; in vivo CC10 reconstitution lowers Th2 cytokines + eosinophilia.
  → ACCEPT neg reg IL-4/5/13 production, regulation of mRNA stability, regulation of
  inflammatory response.
- **Caveat on IFN-gamma**: GOA has GO:0032689 "negative regulation of type II
  interferon production" (IDA, PMID:15356574), but the abstract says CC10 does NOT
  suppress IFN-gamma and INDUCES it in naive CD4+ T cells
  [PMID:15356574 "induce IFN-gamma expression in naive CD4(+) T cells"]. Marked
  UNDECIDED (apparent contradiction; full text needed; not removed since curator
  read full text).
- **neg reg transcription by RNA Pol II (GO:0000122, IDA+IMP)**: kept NON_CORE — the
  transcriptional effect is indirect, downstream of GATA-3 reduction/mRNA
  destabilization; CC10 is a secreted protein, not a transcription factor.

## Localization
- Secreted (extracellular region) — ACCEPT (IBA/IEA/ISO).
- Cytoplasm — IBA + IDA (PMID:8813084: CCSP in cytoplasm of columnar airway
  epithelium); biosynthetic compartment → KEEP_AS_NON_CORE.
- Secretory granule — ACCEPT (storage before regulated secretion).
- **Nuclear envelope (IEA + ISO)** — UNDECIDED: biologically unexpected for a
  secreted club cell protein; cannot verify (some reports describe receptor-mediated
  uptake of uteroglobin).

## Expression / regulation
- Club cells (non-ciliated) of airway epithelium [UniProt TISSUE]; induced by
  glucocorticoids [UniProt INDUCTION "By glucocorticoids"] → ACCEPT response to
  glucocorticoid.
- Many GO_REF:0000107 "response to X" (ozone, LPS, SiO2, FGF, cytokine, xenobiotic)
  are electronic phenotype-level associations → KEEP_AS_NON_CORE.

## Core functions recorded
1. Phospholipase A2 inhibitor activity (GO:0019834) → regulation of inflammatory response.
2. Phospholipid / hydrophobic-ligand binding (GO:0005543; + PCB).
3. Secreted immunomodulator suppressing Th2 cytokines (IL-4/5/13) via GATA-3 mRNA
   destabilization.

## Knowledge gaps
- Receptor/transduction by which secreted CC10 reaches T cells to destabilize GATA-3
  mRNA is undefined.
- Physiological relevance of (weak) progesterone binding is doubtful.

## Key references
- PMID:15356574 — Hung 2004, CC10 regulation of Th2 responses (abstract only).
- PMID:8813084 — CCSP cytoplasmic localization in developing mouse lung (abstract).
- PMID:8440203 — species variation in CC10 progesterone binding (abstract).
- file:mouse/Scgb1a1/Scgb1a1-uniprot.txt — curated PLA2 inhibitor / phospholipid /
  PCB binding, secretion, glucocorticoid induction.
