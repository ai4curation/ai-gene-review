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

## Extending to further genomes

**Cylindrospermum stagnale PCC 7417 (taxon 56107, a more divergent Nostocaceae).** All
components are reciprocal orthologs at 52–72% identity (more divergent than *A. variabilis*),
and the fraC–fraD–fraE operon is syntenic (Cylst_1330 / Cylst_1329 / Cylst_1328): FraD
**K9WUY7**, FraC **K9WTD1**, FraE **K9WTV4**, SepN **K9WXR0**, SepJ **K9WRN1**, AmiC2
**K9X2S2**. Notably this genome has **no tandem AmiC1** — the AmiC2 ortholog (K9X2S2) is
standalone and both 7120 AmiC exemplars reciprocate to it, so the AmiC1/AmiC2 duplication
appears to be a *Nostoc/Anabaena*-specific event rather than ancestral to the module.

**Chlorogloeopsis fritschii PCC 6912 (taxon 246409, Stigonematales / true-branching) — a
genuine absence.** Despite being a heterocyst-former, this genome yields **no detectable
FraD, FraC, FraE, SepN or AmiC** (family membership = 0 for IPR020360/IPR054663; homology =
no hit), and only a weak, non-reciprocal SepJ-domain hit. The full 16,971-protein proteome
was searched, so this is a real negative, not a data artifact: the FraD/SepN septal-junction
module is **not universal across heterocyst-forming cyanobacteria** — the deepest-branching
Stigonematales lineage sampled here either uses a divergent SJ system or lacks these
components. A worthwhile follow-up question for the module.

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

## Reciprocal-best-hit ortholog assignment (`--rbh`)

Because several components are grounded on broad domains, a forward best-hit can land on a
paralog. Running RBH against the exemplars' source genome (Nostoc PCC 7120, taxon 103690)
confirms 1:1 orthology and, critically, **disambiguates the tandem amidase paralogs**:

```
ai-gene-review scan-module modules/septal_junction.yaml \
  --taxa 63737 --source-taxon 103690 --rbh
```

| 7120 exemplar | → NOSP7 fwd hit | → 7120 rev hit | reciprocal |
|---------------|-----------------|----------------|:----------:|
| FraD P46079 | B2IXC8 | P46079 | ✓ |
| FraC P46078 | B2IXC9 | P46078 | ✓ |
| FraE A0ACD7RSN5 | B2IXC7 | A0ACD7RSN5 | ✓ |
| SepN A0ACD7RWW5 | B2IXD4 | A0ACD7RWW5 | ✓ |
| SepJ A0ACD7RSI0 | B2J1N1 | A0ACD7RSI0 | ✓ |
| **AmiC2** A0ACD7S2F2 | **B2J2S4** | A0ACD7S2F2 | ✓ |
| **AmiC1** A0ACD7S1M0 | **B2J2S3** | A0ACD7S1M0 | ✓ |

Every component is a reciprocal best hit — independently confirming the FraD/FraC/FraE/SepN/
SepJ ortholog calls — and the two NOSP7 amidases resolve cleanly: **B2J2S4 = AmiC2 ortholog,
B2J2S3 = AmiC1 ortholog** (a tandem pair, mirroring the 7120 alr0093/alr0092 arrangement).

The same RBH run assigns the *Anabaena variabilis* (TRIV2, taxon 240292) orthologs, all
reciprocal: FraD **Q3MGQ1**, FraC **Q3MGQ2**, FraE **Q3MGQ0** (syntenic operon), SepN
**Q3MF16**, SepJ **Q3MGV3**, and the tandem amidases **AmiC2 Q3MD47 / AmiC1 Q3MD48**.

### Reciprocity gate on the homology call (`--homology --source-taxon`)

With a source taxon, the homology table adds `reciprocal` / `ortholog` columns: a hit is an
**ortholog (`O`)** only if it is significant *and* a reciprocal best hit; otherwise it is a
**homolog-only (`h`)** hit. This auto-flags broad-domain false positives — e.g. the amidase
hits in the unicellular negatives (*Synechocystis* P73736, *Synechococcus* Q31KM9) drop from
`Y` to `h`, correctly marking them as housekeeping-amidase paralogs, not SJ orthologs.

Caveat (honest limitation): RBH is necessary but not sufficient for the broadest families.
SepJ and FraE still score `O` in *Synechocystis* because their transporter families
(DMT/EamA, ABC-2) are ancient and the unicellular genome's single family member is genuinely
the mutual best match. For those, the SJ-specific signal is the **operon/synteny context**
(absent in unicellular genomes), not sequence reciprocity alone.

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
