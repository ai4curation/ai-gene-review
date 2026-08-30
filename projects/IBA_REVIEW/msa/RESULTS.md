---
title: "IBA Pseudo-Enzyme MSA Checks"
species: [human, ANOGA, SCHPO, yeast, worm, ARATH]
genes: [AGO1, AGO2, AGO3, AGO4, DPYSL2, CRMP1, DPYSL3, DPYSL4, UBAC2, CASP12, LPA, ADGB,
        ADPRHL1, PGRPLC, AKTIP, AZIN1, SEPHS1, CPS1, HSPA13, Epe1, cts2, KDX1, SSZ1,
        wago-4, CRY1]
---

# MSA checks of pseudo-enzyme claims

Reproducible alignment-level verification of catalytic-residue loss for the
pseudo-enzyme examples in the [IBA_REVIEW findings](../../IBA_REVIEW.md) (Pattern 7).
Earlier passes relied on UniProt CAUTION/FUNCTION text; this analysis independently
inspects the actual residues. Sections 1–2 cover the original two claims; section 3
generalizes the method and applies it to six more.

Run: `uv run python catalytic_residue_msa.py` (FAMSA alignment via `pyfamsa`).
Target sequences come from the repo's local `genes/.../*-uniprot.txt`; the reference
active enzyme (DPYS) and the catalytic-residue **positions** are pulled live from the
UniProt REST feature tables (with a documented hardcoded fallback for the AGO2
positions if the API returns none — not triggered in the runs reported here, which
used the live metal-binding-site features).

## 1. Human Argonautes AGO1–4 — RNase-H-like catalytic site (DDH of the DEDH tetrad)

Residues at the positions UniProt annotates on AGO2 as divalent-metal-binding
(the catalytic Asp/Asp/His — i.e. the DDH metal-coordinating subset of the
canonical DEDH slicer tetrad; the catalytic-glutamate "finger" is discussed in
the caveats and is not in the metal-binding feature set):

| AGO2 position | AGO1 | AGO2 | AGO3 | AGO4 |
|---------------|------|------|------|------|
| D597          | D    | **D** | D   | D    |
| D669          | D    | **D** | D   | **G** |
| H807          | R    | **H** | H   | **R** |

- **AGO2** (the only human slicer) has the intact tetrad.
- **AGO4** has **two** substitutions — D669G and H807R — consistent with no
  endonuclease activity. This is direct, alignment-level support for the AGO4 REMOVE
  (`GO:0004521` RNA endonuclease activity).
- Nuance the MSA reveals: **AGO3 retains the full tetrad** (D/D/H), so its weak slicing
  is *not* explained by tetrad loss — a blanket "only AGO2 has the residues" would have
  been wrong. AGO1 loses only the catalytic His (H→R).

## 2. CRMP/DPYSL family vs active dihydropyrimidinase (DPYS, Q14117)

Residues at DPYS's UniProt-annotated Zn(2+)-coordinating / active-site positions:

| DPYS position | DPYS | DPYSL2 | DPYSL3 | DPYSL4 | DPYSL5 | CRMP1 |
|---------------|------|--------|--------|--------|--------|-------|
| H67  (Zn)     | H    | H      | H      | H      | **S**  | **N** |
| H69  (Zn)     | H    | **R**  | H      | **R**  | H      | **Y** |
| K159 (carbamate→Zn) | K | **L** | **M** | **L** | **Q** | **Q** |
| H192 (Zn)     | H    | H      | H      | H      | H      | H     |
| H248 (Zn)     | H    | **K**  | **K**  | **K**  | **N**  | **K** |
| D326 (Zn)     | D    | **A**  | **A**  | **A**  | D      | **G** |

- **All five CRMP/DPYSL paralogs have lost the carbamylated catalytic Lys159** — the
  residue that bridges the binuclear metal centre — plus several Zn-coordinating
  His/Asp. Without K159 there is no metal site and no amidohydrolase activity.
- This is first-hand confirmation of the UniProt CAUTION ("Lacks most of the conserved
  residues … essential for binding the metal cofactor") and supports the `GO:0016812`
  REMOVE across DPYSL2/3/4 (and the same basis for DPYSL5/CRMP1).

## 3. Systematic pass over the pseudo-enzyme backlog (2026-08-26)

`catalytic_residue_check.py` generalizes the method: it takes a **catalytic reference**
whose active-site residues are annotated in UniProt, aligns it with the target plus
explicit catalytic (+) and non-catalytic (−) controls, and reports what each protein
carries at those positions in its own numbering. Positions are always pulled live from
the reference's feature table, never written from memory.

Run: `uv run python catalytic_residue_check.py CASE`, where CASE is one of
`pgrp · rhomboid · caspase · calpain · plasminogen · adprh · e2 · odc · sephs ·
gatase · mapk · hsp70 · argonaute_worm · jmjc · chitinase · photolyase`.

The corpus carries ~53 `PSEUDO_OR_SUBACTIVITY_LOSS` rows across ~35 genes, of which only
the Argonaute and CRMP claims above had ever been checked first-hand. This pass covers
every remaining claim where a catalytic reference with annotated active-site residues
exists — 17 targets.

### Confirmed: the site really is degenerate (13)

| Target | Claim under test | Reference | Residue result |
|---|---|---|---|
| **Epe1** (SCHPO) | pseudo-demethylase | KDM2A/KDM2B — *the actual IBA donors* | Fe ligand H284→**Y370**; D214→E299. Matches UniProt verbatim: *"iron catalytic His in position 370 which is replaced by a Tyr residue"* |
| **cts2** (SCHPO) | no chitinase activity | CHIT1 (Q13231) GH18 Glu | catalytic proton donor E140→**N166**; also Y141→K167, W358→T401. UniProt: *"Lacks the conserved Glu residue in position 166"* — the MSA additionally names the substitute (Asn) |
| **SEPHS1** (human) | not a selenophosphate synthetase | SelD (P16456) | catalytic C17→**T29**, while **every** ATP/Mg ligand (K32, D69, D87, D110, D265) is retained. SEPHS2 has selenocysteine **U60** at the same column |
| **CPS1** (human) | uses ammonia, not glutamine | CarA (P0A6F1) GATase triad | nucleophile C269→**S294**; His377/Glu379 retained — precisely why the glutaminase half-reaction is dead |
| **KDX1** (yeast) | pseudokinase | Fus3/Slt2 | β3 VAIK lysine K42→**R54** lost, HRD aspartate retained. Its active paralog Slt2 keeps K54 — a same-organism paralog contrast |
| **wago-4** (worm) | not a slicer | AGO2 (Q9UKV8) | **all three** metal ligands lost (G676, T756, N913) — more degenerate than human AGO4, which still keeps D589 |
| **CRY1** (ARATH) | not a photolyase | PhrB (P00914) | loses the folate-antenna pair (L114, S115) and the DNA-lesion Gln405→**E422**; patterns exactly with the human CRY1 negative control and against PhrB |
| **PGRPLC** (ANOGA) | no amidase activity | PGLYRP2 (Q96PD5) Zn triad | H→**A310**, C→**S429**; catalytic PGLYRP2/PGRP-LB/PGRP-SC1a keep all three |
| **UBAC2** (human) | rhomboid pseudoprotease | GlpG (P09391) Ser-His | S→**L131**, H→**A183**; GlpG/RHBDL2/PARL keep both |
| **ADGB** (human) | not a calpain protease | CAPN1 (P07384) | **all three** triad residues lost (Y158/P320/K343) |
| **ADPRHL1** (human) | inactive ARH2 | ADPRH (P54922) Mg | 3 of 6 lost (N58, A306, A307) |
| **SSZ1** (yeast) | no ATP hydrolysis | HSPA8 (P11142) | 3 of 8 nucleotide ligands lost including the catalytic **K71→R71**; Ssa1 retains all |
| **AKTIP** (human) | pseudo-E2 | UBE2N (P61088) | no residue aligns to the catalytic Cys column at all; the region is unalignable (see flanking context). The UEV control UBE2V1 substitutes A104. Weaker than a clean substitution but consistent with the UniProt CAUTION |

Two of these deserve emphasis because they close the loop on claims the project had been
carrying on someone else's word. **Epe1** is the project's founding example and had never
been checked against its own IBA donors; it now is, and the substitution lands on residue
370 exactly as UniProt states. **cts2** and **PGRPLC** were both resting on OpenScientist
residue assertions ("E-to-N loss at position 166", "H310A and C429S"); all three positions
reproduce exactly under independent alignment.

### Not supported as stated: the site is intact (4)

These are the valuable ones. In each case the annotation call may still be right, but the
*stated mechanism* — catalytic-residue loss — is wrong, and the review or the project page
should say what actually blocks the activity.

- **LPA.** The alignment reproduces the catalytic triad exactly. This is *not* a
  contradiction of the LPA gene review, which already states apo(a) "retains the
  catalytic His-Asp-Ser triad" and rests its case on a different argument — the
  zymogen **activation junction** is S1819|I1820 rather than plasminogen's cleavable
  R|V. Independent confirmation of a careful review. What it does contradict is the
  row's structured `failure_modes: [PSEUDO_OR_SUBACTIVITY_LOSS]`: nothing was lost
  from the active site, so the mode should describe activation, not site degeneracy.
  UniProt's FUNCTION line moreover still asserts apo(a) "has serine proteinase
  activity and is able of autoproteolysis," which is why the IDA row is correctly
  left UNDECIDED.
- **CASP12.** The full-length Csp12-L variant carries the canonical caspase
  **QACRG** motif (C220) and the conserved His (H172) — verified twice, once by
  alignment against caspase-1 and once by direct motif search. CASP12 is genuinely
  inactive and the REMOVE stands (GOA carries a curated `NOT` by **IKR**, inferred
  from key residues), but the mechanism is a **nonsense polymorphism at codon 125**
  truncating the protein before the catalytic domain in the reference allele — not a
  degenerate active site. Note also that UniProt only says CASP12 "**May** lack
  protease activity (Probable)," a hedged non-experimental statement. The Pattern 7
  *Lesson* line in [IBA_REVIEW.md](../../IBA_REVIEW.md), which groups CASP12 with
  AGO4/CRMP under "degenerate/absent active site," should say truncation instead;
  the Pattern 7 bullet itself already says "truncated" and is correct.
- **AZIN1.** Antizyme inhibitor 1 **retains** ODC1's catalytic proton donor (C360→C358)
  and both PLP-binding residues (S200, G237). What it loses is *substrate* binding —
  the ornithine contacts Y331→**S329** and Y389→**D387**. So AZIN1 is not a
  catalytic-machinery pseudo-enzyme; it is an enzyme that can no longer bind its
  substrate, which fits its actual biology (it binds antizyme, not ornithine). The
  paralog contrast sharpens it: **AZIN2 loses the catalytic Cys (V361) while AZIN1
  keeps it**, so a blanket "the antizyme inhibitors lost the catalytic residue" would
  have been wrong in both directions.
- **HSPA13.** All eight HSPA8 nucleotide-binding residues are retained (the only change,
  S275→T300, is conservative). The `GO:0044183` REMOVE is a claim about the
  **substrate-binding domain**, not the nucleotide site, so this check neither supports
  nor refutes it — it only rules out the ATPase-site argument. Contrast SSZ1, which does
  lose the catalytic lysine.

**Why this pass mattered.** Three of the confirmations closed *named open items*.
HISTORY.md had excluded PGRPLC for want of exactly this check; Pattern 7 carried an
explicit caveat that UBAC2's residue loss was "inferred from the inactive-rhomboid
classification … not from an explicit UniProt CAUTION"; and Epe1, the project's founding
example, had never been aligned against its own IBA donors. All three are now first-hand.

Equally important is the hit rate on the other side: **4 of 17 targets (24%) had an
intact catalytic site** despite the review or project page describing residue loss. In
none of those four is the *conclusion* clearly wrong — CASP12 is truncated, LPA cannot be
activated, AZIN1 cannot bind ornithine, HSPA13's issue is its substrate-binding domain —
but in all four the *reason given* was wrong. A claim of the form "lacks the catalytic
residues" is cheap to write, easy to believe, and, on this sample, wrong about a quarter
of the time.

## Caveats

- FAMSA with a UPGMA guide tree; results are robust because the inspected columns are
  deep, conserved active-site positions (unambiguous to align).
- Residue retention is **not** proof of activity, and residue loss is **not** the only
  route to inactivity. Four worked counterexamples above: truncation (CASP12), a blocked
  zymogen activation junction (LPA), loss of *substrate* rather than catalytic residues
  (AZIN1), and a defect in a different domain entirely (HSPA13). Read a retained site as
  "this particular argument for inactivity fails," not as "the protein is active."
- The method needs a **catalytic reference with annotated active/binding-site features**.
  Several backlog claims cannot be checked this way at all — CAPG (severing vs capping),
  CRYAA (holdase vs foldase), MEFV and RAD51C (whole domains absent rather than residues
  substituted) — because they are not point-residue questions.
- Always include a genuine catalytic **positive** control and verify its identity first.
  The first PGRP run used Q9VXN9 as "PGRP-LB"; it is actually PGRP-**LE**, itself a
  non-catalytic receptor, which made the controls appear to have lost the site too.
- Gaps are weaker evidence than substitutions. AKTIP's catalytic-Cys column is a gap, so
  the tool prints flanking alignment context rather than reporting a residue.
- UniProt annotated 3 metal-binding residues on AGO2 (the two Asp and the His that
  coordinate the cations); the "E" of the DEDH shorthand is the catalytic glutamate
  finger and is not in the metal-binding feature set, so it is not shown here.
- This verifies *catalytic-residue loss*, which is necessary (not by itself sufficient)
  evidence; it is corroborated by the experimental/curated statements cited in the
  findings.
