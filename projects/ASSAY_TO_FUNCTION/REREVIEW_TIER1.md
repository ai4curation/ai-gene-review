# Tier-1 re-review (MF-from-hub-readout candidates)

Re-review of the 7 Tier-1 candidates produced by `flag_candidates.py`, checked
against each annotation's actual evidence in its review file. Conclusion up
front: **none is a clean readout-driven over-annotation**; the flag over-fired,
and the reasons are an informative calibration of the rubric.

## Verdicts

| gene | term | flagged because | evidence in file | verdict |
|---|---|---|---|---|
| Calm2 (mouse) | calcium-dependent protein binding (GO:0048306) | Ca²⁺-imaging paper | IPI PMID:33199372 + IEA + ISO | **KEEP** — this *is* calmodulin's core molecular activity, shown by direct interaction, not by the imaging readout |
| HRC (human) | calcium ion binding (GO:0005509) | Ca²⁺-imaging paper | IEA consistent w/ IDA; KD ~1.9 mM cited | **KEEP** — defining direct binding activity |
| Ctnnb1 (mouse) | transcription coactivator activity (GO:0003713) | luciferase reporter | biochem/structural PMID:21075118 (β-catenin–Lef-1) | **KEEP** — β-catenin is the canonical Wnt coactivator (machinery) |
| NOTCH1 (human) | transcription coactivator activity (GO:0003713) | reporter | NICD–RBPJ/CSL coactivation | **KEEP** — NICD is a bona fide coactivator |
| Notch1 (mouse) | transcription coactivator activity (GO:0003713) | reporter | as above | **KEEP** |
| HMGB1 (human) | transcription coactivator activity (GO:0003713) | reporter | IDA PMID:19223331 (enhances TF binding) | **KEEP (borderline)** — IDA-supported; a more proximal "DNA bending/HMG-box" MF would be more informative but the term is defensible |
| SIRT1 (human) | transcription corepressor activity (GO:0003714) | reporter PMID:20955178 | IBA + IDA PMID:12535671 | **KEEP_AS_NON_CORE (soft)** — corepression is downstream of SIRT1's core NAD⁺-dependent deacetylase activity; not wrong, but not the core MF |

No edits were made to the gene review files: six verdicts are KEEP, and the
SIRT1 case is a soft, debatable non-core suggestion that does not meet the bar
for unilaterally overriding an existing curated `ACCEPT`.

## Why the flag over-fired — calibration findings

1. **Binding MF is a direct activity, not a readout consequence.** "calcium ion
   binding", "calcium-dependent protein binding" (and protein/ligand binding
   generally) describe the molecular activity itself and are established by
   binding/IPI/IDA assays. The "a state readout cannot license MF" premise does
   not apply. → **Flagger change applied:** Tier 1 now skips any MF term whose
   label contains "binding" (removed Calm2, HRC).

2. **Coregulator MF is legitimate for genuine coregulators.** β-catenin and NICD
   are textbook transcriptional coactivators; SIRT1/HMGB1 act on chromatin. The
   discriminator separating these from a true over-annotation is **machinery
   membership**, not the MF aspect. The corpus's clean over-annotation —
   `AIP → transcription coactivator activity` (AIP is an AhR chaperone, not a
   coregulator) — is exactly the machinery-non-member case.

3. **The standing-only filter already does its job.** The genuine over-annotation
   (AIP) was already `MARK_AS_OVER_ANNOTATED` by a curator, so it was correctly
   *not* re-flagged. Among annotations still standing as `ACCEPT`, the
   MF-from-hub set is dominated by legitimate calls. **Implication:** the
   flagger's marginal value is higher on *unreviewed* annotations and on the
   Tier-2 triage queue than on re-litigating accepted MF calls.

## Net effect on the flagger / rubric

- `flag_candidates.py`: Tier 1 excludes `*binding` MF; the Tier-1 reason text
  now says "verify direct (e.g. DNA-binding) evidence" rather than asserting the
  MF is unlicensed. Tier 1: 7 → 5.
- `rubric.yaml` / `RUBRIC.md`: the MF prohibition is refined — it targets
  *regulatory/process-like* MF (coactivator/corepressor/TF activity) inferred
  for genes outside the relevant machinery, **not** direct binding or catalytic
  MF, which carry their own assays.
- Recommended next application: run the flagger over *unreviewed* hub-aligned MF
  annotations (where curators have not yet adjudicated) rather than ACCEPTed ones.
