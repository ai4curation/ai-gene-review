# Septal-junction module — genome scan

**Question.** Can the `modules/septal_junction.yaml` module be used to scan another genome
and detect its members?  **Answer: yes.**

This scan is run with the generic `scan-module` tool (no module-specific code), which reads
each component's `family` term and `representative_members` exemplars straight from the
module document:

```bash
ai-gene-review scan-module modules/septal_junction.yaml \
  --targets modules/septal_junction/scan_targets.json --homology \
  --out modules/septal_junction/scan_results
```

Target genomes are in `scan_targets.json` (module-specific config, colocated). Results are
regenerated into `scan_results/*.tsv`. Positive controls = filamentous heterocyst-forming
cyanobacteria (expected to carry the SJ module); negative controls = unicellular
cyanobacteria (expected to lack the SJ-specific components).

## Method A — InterPro family membership (n members per genome)

| component | InterPro | 7120 | *N. punctiforme* | *A. variabilis* | *Synechocystis* | *S. elongatus* |
|-----------|----------|------|------------------|-----------------|-----------------|----------------|
| **FraD**  | IPR020360 (specific) | 1 | 1 | 1 | **0** | **0** |
| **FraC**  | IPR054663 (specific) | 1 | 1 | 1 | **0** | **0** |
| SepN      | (no model) | NA | NA | NA | NA | NA |
| SepJ      | IPR000620 (broad EamA) | 6 | 9 | 6 | 4 | 3 |
| FraE      | IPR032688 (broad ABC-2) | 2 | 3 | 2 | 1 | 1 |
| AmiC      | IPR050695 (broad Amidase_3) | 5 | 4 | 4 | 3 | 3 |

FraD and FraC families are **diagnostic** (present in every heterocyst-former, absent from
every unicellular genome). SepN has no family model. SepJ/FraE/AmiC map to broad domains
present in all cyanobacteria, so family membership alone does not discriminate them.

## Method B — sequence homology (phmmer of the PCC 7120 exemplar), best hit per genome

`Y` = E ≤ 1e-5. Cells: best-hit accession, E-value, % identity.

| component | 7120 (self) | *N. punctiforme* | *A. variabilis* | *Synechocystis* | *S. elongatus* |
|-----------|-------------|------------------|-----------------|-----------------|----------------|
| **FraD** | P46079 (100%) | **B2IXC8** (7e-165, 70%) | **Q3MGQ1** (2e-233, 98%) | none | none |
| **FraC** | P46078 (100%) | **B2IXC9** (4e-64, 60%) | **Q3MGQ2** (1e-109, 96%) | none | none |
| **SepN** | A0ACD7RWW5 (100%) | **B2IXD4** (6e-127, 82%) | **Q3MF16** (5e-151, 97%) | none | none |
| FraE | A0ACD7RSN5 (100%) | **B2IXC7** (6e-119, 75%) | **Q3MGQ0** (3e-152, 97%) | P74719 (2e-78, 50%)¹ | none |
| SepJ | A0ACD7RSI0 (100%) | **B2J1N1** (2e-214, 53%) | **Q3MGV3** (0, 97%) | P72732 (1e-47, 34%)¹ | n (6e-3)¹ |
| AmiC | A0ACD7S2F2 (100%) | B2J2S4 (2e-272, 71%)² | Q3MD47 (0, 96%)² | P73736 (2e-117, 42%)¹ | Q31KM9 (2e-88, 52%)¹ |

¹ Hit is to a paralog in a unicellular genome (generic DMT transporter, ABC-2 permease, or
housekeeping amidase), **not** a true SJ ortholog. ² Best of several amidase-family paralogs;
true AmiC1/AmiC2 assignment needs reciprocal-best-hit, not just top hit.

- **FraD, FraC and SepN**: strong hits in all heterocyst-formers, **no hit** in either
  unicellular genome. **SepN — which has no family model — is detected purely from its
  representative-member sequence**, validating the family-with-exemplars grounding.
- Self column = 100% identity (positive control on the method itself).

## The fraC–fraD–fraE operon is syntenic in the positives

The best hits for FraC/FraD/FraE carry **consecutive accessions** in both positive genomes —
*N. punctiforme* **B2IXC9 / B2IXC8 / B2IXC7**, *A. variabilis* **Q3MGQ2 / Q3MGQ1 / Q3MGQ0** —
so the operon is intact and syntenic. This adds strong genomic-context confidence to the
FraE ortholog call even though its InterPro family is broad.

## Candidate members for curation

High-confidence orthologs detected in the two positive genomes (the "gap-fill" candidates):

| component | *N. punctiforme* (NOSP7, 63737) | *A. variabilis* (TRIV2, 240292) | basis |
|-----------|---------------------------------|---------------------------------|-------|
| FraD | B2IXC8 | Q3MGQ1 | specific family + homology + synteny |
| FraC | B2IXC9 | Q3MGQ2 | specific family + homology + synteny |
| FraE | B2IXC7 | Q3MGQ0 | homology + operon synteny |
| SepN | B2IXD4 | Q3MF16 | exemplar homology (no family) |
| SepJ | B2J1N1 | Q3MGV3 | exemplar homology (broad domain) |
| AmiC | B2J2S4 (best) | Q3MD47 (best) | homology; paralog assignment needs RBH |

## Interpretation for the module

- The module scans a new genome successfully; both positive genomes contain detectable
  members of all components; both negatives lack the SJ-specific ones.
- **FraD, FraC, SepN are the diagnostic core.** FraD/FraC via specific families, SepN via
  exemplar homology.
- Components grounded on **broad domains (SepJ, FraE, AmiC) are not discriminated by family
  membership**; their orthologs are recovered by exemplar homology + synteny, but a top-hit
  can land on a paralog (see the unicellular negatives). Strengthening those groundings
  (specific HMMs / curated ortholog sets / RBH) is the main improvement opportunity.

## Limitations

- phmmer reports the single best hit, not a reciprocal-best-hit; the paralog hits in the
  negatives are the honest signal that a grounding is broad, not a claim of SJ orthology.
- Only reference proteomes are scanned; two POS + two NEG genomes are a validation set, not
  a phylogenetic survey.
