# Septal-junction module — genome scan results

**Question.** Can the `modules/septal_junction.yaml` module be used to scan another
genome and detect its members?

**Answer.** Yes. Using each component's grounding (InterPro family term and/or the
Nostoc PCC 7120 representative-member sequence), all seven components are detected in
two independent filamentous heterocyst-forming cyanobacteria, and the *specific* SJ
components (FraD, FraC, SepN) are cleanly absent from unicellular cyanobacteria.

Reproduce with `uv run python scan.py` (see README.md). Nothing here is hard-coded;
tables are regenerated into `results/*.tsv`.

## Targets

| class | organism | taxon | ref. proteome | #proteins |
|-------|----------|-------|---------------|-----------|
| SELF | *Nostoc* sp. PCC 7120 | 103690 | UP000002483 | 6070 |
| POS  | *Nostoc punctiforme* PCC 73102 | 63737 | UP000001191 | 6573 |
| POS  | *Anabaena variabilis* ATCC 29413 | 240292 | UP000002533 | 5634 |
| NEG  | *Synechocystis* sp. PCC 6803 | 1111708 | UP000001425 | 3508 |
| NEG  | *Synechococcus elongatus* PCC 7942 | 1140 | UP000889800 | 2657 |

POS = filamentous, heterocyst-forming (expected to carry the SJ module).
NEG = unicellular (expected to lack the SJ-specific components).

## Method A — InterPro family membership (n members per genome)

| component | InterPro | specificity | 7120 | *N. punctiforme* | *A. variabilis* | *Synechocystis* | *S. elongatus* |
|-----------|----------|-------------|------|------------------|-----------------|-----------------|----------------|
| **FraD**  | IPR020360 | **specific** | 1 | 1 | 1 | **0** | **0** |
| **FraC**  | IPR054663 | **specific** | 1 | 1 | 1 | **0** | **0** |
| SepN      | (none)    | no model     | NA | NA | NA | NA | NA |
| SepJ      | IPR000620 (EamA) | broad | 6 | 9 | 6 | 4 | 3 |
| FraE      | IPR032688 (ABC-2/NosY) | broad | 2 | 3 | 2 | 1 | 1 |
| AmiC1/2   | IPR050695 (Amidase_3) | broad | 5 | 4 | 4 | 3 | 3 |

- **FraD and FraC families are diagnostic**: exactly one member in every heterocyst-former,
  **zero** in every unicellular genome. These two families alone flag the SJ-bearing lineage.
- **SepN has no family term**, so family membership cannot be used — it needs homology (Method B).
- **SepJ / FraE / AmiC map to broad domains** (EamA/DMT, ABC-2 permease, Amidase_3) that are
  present in all cyanobacteria, including the negatives. Family membership therefore does
  **not** discriminate the SJ-specific protein from unrelated paralogs for these three.

## Method B — sequence homology (phmmer of the PCC 7120 exemplar vs each proteome)

Best hit per exemplar; `Y` = E ≤ 1e-5. Cells show (E-value, % identity over the aligned region).

| component | 7120 (self) | *N. punctiforme* | *A. variabilis* | *Synechocystis* | *S. elongatus* |
|-----------|-------------|------------------|-----------------|-----------------|----------------|
| **FraD** | Y (3e-236, 100%) | Y (7e-165, 70%) | Y (2e-233, 98%) | **none** | **none** |
| **FraC** | Y (3e-113, 100%) | Y (4e-64, 60%) | Y (1e-109, 96%) | **none** | **none** |
| **SepN** | Y (5e-156, 100%) | Y (6e-127, 82%) | Y (5e-151, 97%) | **none** | **none** |
| SepJ | Y (0, 100%) | Y (2e-214, 53%) | Y (0, 97%) | y (1e-47, 34%)¹ | n (6e-3, 32%)¹ |
| FraE | Y (8e-164, 100%) | Y (6e-119, 75%) | Y (3e-152, 97%) | y (2e-78, 50%)¹ | none |
| AmiC1 | Y (0, 100%) | Y (3e-246, 63%) | Y (0, 94%) | y (2e-126, 40%)¹ | y (2e-99, 53%)¹ |
| AmiC2 | Y (0, 100%) | Y (2e-272, 71%) | Y (0, 96%) | y (2e-117, 42%)¹ | y (2e-88, 52%)¹ |

¹ Hit is to a **paralog** in a unicellular genome (a generic DMT transporter, ABC-2 permease, or
housekeeping cell-wall amidase), **not** a true SJ ortholog — see interpretation.

- **Self column = 100% identity, lowest E-value** — the pipeline correctly recovers each exemplar
  (positive control on the method itself).
- **FraD, FraC and SepN**: strong hits (E ≤ 1e-64, 60–98% id) in all three heterocyst-formers and
  **no hit at all** in either unicellular genome. **SepN — which has no Pfam/InterPro/PANTHER
  model — is detected purely from its representative-member sequence.** This validates the
  family-descriptor-with-`representative_members` design: the exemplar sequence *is* the detection
  tool when no family model exists.
- **SepJ, FraE, AmiC** hit paralogs in the unicellular negatives too (moderate identity, driven by
  their broad shared domains). Homology to the exemplar alone therefore over-calls these; a true
  ortholog call needs reciprocal-best-hit and/or genomic (operon) context.

## Bonus: operon synteny is conserved

In both positive genomes the FraD and FraC family members carry **adjacent UniProt accessions**
— *N. punctiforme* B2IXC8 (FraD) / B2IXC9 (FraC); *A. variabilis* Q3MGQ1 / Q3MGQ2 — consistent
with the *fraC-fraD(-fraE)* operon being conserved across heterocyst-forming cyanobacteria.

## Conclusions

1. **The module scans a new genome successfully.** Both filamentous heterocyst-formers contain
   detectable members of all seven components; both unicellular controls lack the SJ-specific ones.
2. **FraD, FraC and SepN are the diagnostic core.** FraD/FraC via their specific InterPro families,
   SepN via exemplar homology — all three present in POS, absent in NEG.
3. **Family model vs exemplar matters.** Components with a specific family (FraD, FraC) are found by
   Method A; SepN (no model) is found only by Method B; and broad-domain components (SepJ, FraE,
   AmiC) are *not* discriminated by either method alone and would need RBH + synteny.
4. This is exactly the kind of gap a curator should see: the module could be strengthened by adding
   **specific** family/HMM groundings (or a curated ortholog set) for SepN, SepJ, FraE and AmiC so
   they become diagnostic rather than relying on broad domains.

## Limitations

- phmmer reports the single best hit, **not** a reciprocal-best-hit; the paralog hits in the
  negatives (footnote 1) are expected and are the honest signal that those groundings are broad,
  not a claim that those genomes have SJ orthologs.
- Only reference proteomes are scanned; a member absent from the reference proteome would be missed.
- Two POS and two NEG genomes are a validation set, not a phylogenetic survey.
