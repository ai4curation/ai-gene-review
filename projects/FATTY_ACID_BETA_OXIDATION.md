---
title: "Mitochondrial Fatty Acid β-Oxidation (cross-species)"
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN]
species: [human, DROME]
genes: [ACADVL, ACAD9, ACADM, ACADS, HADHA, HADHB, ECHS1, HADH, ACAT1, ACAA2]
---

# Mitochondrial Fatty Acid β-Oxidation (cross-species)

## Overview

A cross-species curation of the **mitochondrial fatty acid β-oxidation (FAO)
spiral** — the four-step cycle that degrades saturated fatty acyl-CoA esters two
carbons at a time (acyl-CoA dehydrogenase → enoyl-CoA hydratase →
3-hydroxyacyl-CoA dehydrogenase → 3-ketoacyl-CoA thiolase). The project reviews
the full enzyme complement in **human** and **Drosophila melanogaster**, ties
them together in the cross-species module
[`MODULE:fatty_acid_beta_oxidation`](../modules/fatty_acid_beta_oxidation.html),
and uses the pathway as a testbed for several recurring curation problems:
chain-length substrate specificity, cross-paralog/cross-gene mis-annotation,
moonlighting functions, organelle (mitochondrion vs peroxisome) assignment, and
GO↔RHEA reaction mapping.

**Scope:** 20 grounded gene products (10 human + 10 Drosophila). The module's
derived QC reports 20/20 grounded genes reviewed.

## The gene set

| Step | Reaction | Human | Drosophila |
|------|----------|-------|------------|
| ① dehydrogenase | acyl-CoA → (2E)-enoyl-CoA | ACADVL, ACAD9 (VLC/LC); ACADM (MC); ACADS (SC) | `DROME/Acadvl`, `DROME/Egm`; `DROME/Mcad`; `DROME/Arc42`, `DROME/CG4860` |
| ② hydratase | enoyl-CoA → (3S)-3-hydroxyacyl-CoA | HADHA (LC, MTP); ECHS1 (S/MC) | `DROME/Mtpalpha`; `DROME/Echs1` |
| ③ 3-OH-acyl-CoA DH | → 3-oxoacyl-CoA | HADHA (LC, MTP); HADH (S/MC) | `DROME/Mtpalpha`; (fly S/MC ortholog unresolved) |
| ④ thiolase | → acetyl-CoA + acylₙ₋₂-CoA | HADHB (LC, MTP); ACAA2 (M/LC); ACAT1 (SC/ketone) | `DROME/Mtpbeta`; `DROME/Acaa`; `DROME/Acat1` |

## Curation findings and patterns

### Chain-length substrate specificity
Each step is run by a family of chain-length-specific isozymes. The curation
principle is **use the chain-length-specific molecular-function term where one
exists, and fall back to the general term where it does not** ("not all MF have
them"): VLCAD `GO:0017099`, MCAD `GO:0070991`, SCAD `GO:0016937`, long-chain
3-OH-acyl-CoA DH `GO:0016509`; general fall-backs for the hydratases (`GO:0004300`)
and the straight-chain thiolases (`GO:0003988`). See the flagship
[Enzyme Specificity](ENZYME_SPECIFICITY.html) project for the worked table.

### Cross-paralog and cross-gene mis-annotation
- **ACADVL** ← mouse LCAD (*Acadl*, P50544): 8 IEA/ISS annotations were
  cross-transferred from the paralog, including a self-contradictory "negative
  regulation of fatty acid oxidation" — removed.
- **ACAT1** ← SOAT1/SOAT2 name collision: cholesterol O-acyltransferase +
  ER-localization annotations (from a SARS-CoV-2/CH25H paper about the ER
  acyl-CoA:cholesterol acyltransferase) were mis-attributed to the mitochondrial
  T2 thiolase — removed.
- **HADHA**: thiolase MF removed (that activity is the HADHB subunit's), plus a
  wrong-paper thioesterase term (a Them5/Acot15 paper).

### Moonlighting functions
- **HADH** → GLUD1 (glutamate dehydrogenase) inhibitor / negative regulation of
  insulin secretion (definitive protein-protein interaction evidence,
  PMID:20670938).
- **HADHA** → monolysocardiolipin acyltransferase / cardiolipin remodeling
  (third core function).
- **ACAT1** → tetramer protein-lysine acetyltransferase of PDH components
  (PMID:27867011, verified).

### The mitochondrial trifunctional protein (MTP)
Steps ②–④ for long-chain substrates are carried by the membrane-bound MTP, an
α₂β₂ heterotetramer (α = HADHA / `DROME/Mtpalpha`; β = HADHB / `DROME/Mtpbeta`).
The reviews keep α- and β-subunit activities consistent across species.

### GO↔RHEA reaction-chaining gap
The cross-species module's [reaction-chaining check](../modules/README.md) flags
step ①→② as a break: step ① makes **(2E)-enoyl-CoA**, but the enoyl-CoA hydratase
MF `GO:0004300` maps only to **RHEA:20724** (the (3E) variant), not the canonical
(2E) crotonase **RHEA:16105**. The chemistry is correct; the gap is in the
`GO:0004300 → RHEA` mapping. Recorded as a `MAPPING_GAP` override on the module
connection; see [projects/RHEA](RHEA.html).

## Organelle specificity — mitochondrion vs peroxisome

β-oxidation runs in **both** mitochondria (this gene set) and peroxisomes
(ACOX1, HSD17B4, ACAA1, SCP2…). Several fly annotations carried peroxisome calls
of uncertain standing. Rather than run our own bioinformatics, these were phrased
as neutral function-assignment hypotheses and tested with the **OpenScientist**
workflow (independent AI scientist; our review conclusions held out for
comparison):

| Gene | Peroxisome evidence tested | OpenScientist verdict | vs. our review |
|------|---------------------------|-----------------------|----------------|
| `DROME/Acat1` | ISM (PMID:22758915) | **Refuted / over-annotated → remove.** Acat1 is *not* among the six proteins Faust et al. 2012 experimentally confirmed peroxisomal; its C-terminal **-EKL** is a non-canonical, structurally-embedded catalytic motif (not a PTS1); *Drosophila* is PTS1-only and a cholesterol auxotroph; LOPIT maps it to mitochondria. | Agrees; strengthens `MARK_AS_OVER_ANNOTATED` → REMOVE |
| `DROME/Mtpalpha` | IDA (PMID:22758915) | *run in progress* — note Mtpalpha **is** in Faust et al.'s experimentally-confirmed peroxisomal list, so a genuine dual localization is plausible | expected to confirm `KEEP_AS_NON_CORE` (real minor peroxisomal pool) |

The dissociation is the point: two proteins annotated peroxisomal by the **same**
inventory paper resolve oppositely — Acat1's call is computational-only, Mtpalpha's
is experimentally confirmed.

## Validating datasets

Independent, in-vivo data that reports each enzyme's substrate specificity
(surveyed, not re-run):

- **Acylcarnitine chain-length signatures** (human newborn screening): MCAD
  deficiency → C8; VLCAD → C14:1/C14:2; LCHAD/HADHA → C16-OH — direct in-vivo
  readouts of which chain-length step is blocked.
- **Fly CRISPR-KO acylcarnitine profiling** (Geronazzo et al. 2025, PMID:40519079):
  the same clinical assay in *Drosophila* — Arc42 KO reproduces the ACADS/SCAD C4
  (butyrylcarnitine) signature, CG4860 KO does not, functionally disambiguating
  two paralogs indistinguishable by sequence/EC.
- **MTBLS636** (MetaboLights): mitochondrial cardiolipin molecular-species atlas
  across ~20 human cell lines — the CL space HADHA's MLCL-acyltransferase remodels.
- **Spatial proteomics** for the organelle question: LOPIT-DC U-2 OS
  (PRIDE PXD011254) and Dynamic Organellar Maps (HeLa) resolve mitochondrion vs
  peroxisome per protein; **MitoCoP** (PMID:34800366) is the high-confidence
  human mitochondrial reference.

## FlyBase curation gap (PMID:40519079)

The Geronazzo et al. 2025 CRISPR study is a rich functional resource, but FlyBase
has so far propagated only **one** GO annotation from it to GOA:

```
Arc42  involved_in  GO:0033539 (fatty acid beta-oxidation using acyl-CoA dehydrogenase)  IMP  PMID:40519079  (2026-06-12)
```

Not yet captured (candidate annotations):

| Gene | Candidate annotation | Basis in the paper |
|------|----------------------|--------------------|
| `DROME/Arc42` | `enables GO:0016937` (short-chain acyl-CoA DH activity), IMP | KO elevates C4/butyrylcarnitine, mirroring ACADS deficiency |
| `DROME/CG4860` | the short-chain specificity should **not** propagate here | KO does *not* elevate C4 (the negative paralog result) |
| `DROME/Mcad` | medium-chain acyl-CoA DH phenotype, IMP | KO acylcarnitine profile |
| MTP genes | long-chain FAO phenotypes | KO acylcarnitine profiles |

Our reviews already encode the Arc42-vs-CG4860 disambiguation (Arc42 → core
short-chain MF; CG4860 → MODIFY to general acyl-CoA DH activity), so they are
ahead of FlyBase on this paper's implications.

## Curation-model gap: representing experimentally-supported negatives

The CG4860 result is a clean *negative*: an experiment shows the paralog does
**not** carry the short-chain role that electronic annotation assigns it. The
schema supports proposing a novel **NOT** annotation (`negated: true` +
`action: NEW`) — but only for a GO term **absent** from the gene's GOA. The
`NEW`-exists check is term-level (it ignores the `negated` flag), so a `NOT + NEW`
on `GO:0016937` is rejected because the *positive* `GO:0016937` is already in GOA.

Consequently there is **no first-class way to negate an existing positive
electronic annotation**; the recourse today is `MODIFY` / `MARK_AS_OVER_ANNOTATED`
/ `REMOVE`. A schema/validation enhancement — keying the `NEW`-exists check on
`(term, negated)` so a curator-supported NOT can coexist with a positive
annotation — would let experimentally-supported negatives (like CG4860's) be
represented directly. Flagged here as a candidate improvement.

---

# STATUS

## Completed
- [x] 8 human FAO gene reviews (ACADVL, ACADM, ACADS, HADHA, ECHS1, HADH, ACAT1, ACAA2); ACAD9 + HADHB pre-existing
- [x] 10 Drosophila ortholog reviews
- [x] Cross-species module + reaction-chaining check (QC 20/20)
- [x] OpenScientist organelle hypothesis: `DROME/Acat1` peroxisome (refuted)

## In progress / open
- [ ] OpenScientist organelle hypothesis: `DROME/Mtpalpha` peroxisome (running)
- [ ] Fly medium/short-chain 3-hydroxyacyl-CoA dehydrogenase ortholog (HADH) — unresolved ("?")
- [ ] FlyBase curation-gap candidates from PMID:40519079 (above)
- [ ] Negation-representation gap (NOT+NEW vs existing positive term)

Last updated: 2026-07-01

# NOTES

## 2026-07-01

Created the project to capture the cross-species FAO curation, the validating
datasets (acylcarnitine + fly CRISPR + MTBLS636 + spatial proteomics), the
OpenScientist organelle work, the FlyBase under-curation of PMID:40519079, and
the NOT/NEW negation-representation gap surfaced by the CG4860 negative result.
