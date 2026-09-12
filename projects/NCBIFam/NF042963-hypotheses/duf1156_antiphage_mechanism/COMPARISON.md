# Blinded comparison: holdout vs OpenScientist (NF042963 / DUF1156)

Compares `HOLDOUT-prediction.md` (recorded before the run, from InterPro/UniProt)
against `openscientist.md` (structure-based, blinded to the mechanism), plus a
family-wide check run afterward to adjudicate the one disagreement.

## Agreement (both, high confidence)

- **Enzyme:** SAM-dependent, site-specific **DNA amino-methyltransferase** —
  intact catalytic machinery: Class I motif I glycine loop (FxGxG, F233–G237) +
  amino-MTase catalytic **DPPY** motif IV (D617–Y620), converging in one
  Rossmann SAM pocket (AlphaFold AF-A0A3B7MFS0-F1, G235–D617 Cα = 8.1 Å).
- **No nuclease** anywhere in the ~1000-aa chain (no PD-(D/E)xK, HNH, GIY-YIG,
  m5C Pro-Cys). So the protein is *exclusively* a methyltransferase.
- **DUF1156 (PF06634, res ~30–90) + C-terminal extension = accessory** (target
  recognition / scaffolding), not catalytic. DUF1156 is a *separate small
  domain*, not the catalytic centre — it just names the family.
- **Defense mechanism:** epigenetic self/non-self discrimination in the
  **BREX / DISARM / restriction–modification** mould — host DNA is self-marked
  by methylation; unmethylated phage DNA is excluded/restricted, with any
  effector step supplied in *trans* (the protein has no nuclease). OpenScientist
  cites BREX/DISARM precedent (PMID:39979294, 29085076, 32338761) — NOT in our
  publications/ cache, so treated as leads, not verbatim-verified.

## Disagreement: target base (m4C vs m6A) — the interesting part

| | Holdout (annotation) | OpenScientist (structure) |
|---|---|---|
| Target base | **N6-adenine (m6A)** | **N4-cytosine (m4C)** |
| Basis | InterPro IPR014455 "DNA methylase, N-6 adenine-specific"; UniProt names "Adenine-specific DNA methylase" | Foldseek top hits M.MjaII/M.MvaI/M.AvaI all m4C (EC 2.1.1.113), prob 1.0 |

**Adjudication (family-wide, 151 members, 2026-07-18):** 19 named "adenine", **0**
named "cytosine"; 2 carry IPR014455 (N6-adenine). Every base-specificity signal in
the family points to **adenine (m6A)**, none to cytosine. Foldseek **cannot**
distinguish m6A from m4C — the two amino-MTase classes share the same β-class fold
and the DPPY motif (OpenScientist's own Limitation #5). So the confident m4C call is
an over-reach from single-representative fold-matching; the family evidence favors
**m6A**, matching the holdout. Net: **base genuinely UNDECIDED, leaning m6A.**

## What the run genuinely ADDED beyond the holdout

- Structural proof the catalytic site is **intact** (not a degraded pseudo-MTase)
  — the decisive point for whether an MF term is warranted at all.
- Localised the actual catalytic module and residues (motif I F233–G237; DPPY
  D617–Y620) and confirmed DUF1156 is a distinct accessory N-terminal domain.
- A concrete, testable model (BREX/DISARM-like) + the decisive experiment: a
  **DPPY catalytic-dead mutant (D617A/Y620A)** should abolish both methylation
  and phage protection; LC-MS/MS of digested host DNA resolves m4C vs m6A.

## GO consequences

- **BP** `GO:0051607 defense response to virus` stands; the proposed-new-term
  request `defense response to bacteriophage` (is_a GO:0051607) still stands.
- **MF (new, beyond NCBI's BP-only go_terms):** the family has a real molecular
  function — **`GO:0009008 DNA-methyltransferase activity`** as the safe parent
  (amino-MTase confirmed, m5C excluded), with the specific child **UNDECIDED**
  between `GO:0009007` site-specific DNA-MTase (adenine-specific, EC 2.1.1.72,
  favored by family annotation) and `GO:0015667` (cytosine-N4-specific, EC
  2.1.1.113, per OpenScientist structure). Do not assert a specific base until
  biochemistry resolves it. This is a proposed enrichment, not part of the
  adopt/refine ncbifam2go seed (which only touches NCBI's own go_terms).
