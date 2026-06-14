---
title: "Worked Demonstrator: Kinetic/Mechanism Data for ENZYME_SPECIFICITY Cases"
---

# Worked demonstrator — substrate-specificity data sources applied to real genes

Applies the clients in [`..`](..) (`query_sabiork.py`, `query_mcsa.py`) to a positive control plus
real cases from [`../../ENZYME_SPECIFICITY.md`](../../ENZYME_SPECIFICITY.md). All numbers below were
pulled live from the public APIs on **2026-06-14**; raw outputs are in [`data/`](data/). Values are
reproduced as returned (read and verify before curating; kinetic values vary with assay conditions).

## 1. Positive control — human hexokinase (EC 2.7.1.1)

Confirms the approach recovers a *known* substrate-specificity profile, with PubMed provenance.

`python query_sabiork.py --ec 2.7.1.1 --organism "Homo sapiens" --summary`

| Hexose substrate | Km range (n) | Interpretation |
|---|---|---|
| **D-Glucose** | 9.3×10⁻⁵ – 2.1×10⁻³ M, low ~**4.6×10⁻⁵ M** (n=42) | preferred substrate (tightest Km) |
| **D-Mannose** | 8.0×10⁻⁵ – 2.2×10⁻³ M (n=13) | near-glucose affinity |
| **D-Fructose** | 4.7×10⁻³ – 2.4×10⁻¹ M (n=11) | ~**100–200× weaker** than glucose |

Provenance examples: D-Glucose Km — PMID:16640561, 17080299, 29298880; D-Fructose Km — PMID:7730377,
953036. The phosphate donor is also resolved (ATP n=52 vs weak ITP/CTP/UTP), i.e. **both** half-site
specificities are visible. This is the measured discrimination that the
[`Boltz-2`](../../BOLTZ2_SUBSTRATE_SPECIFICITY.md) affinity module could only (poorly) approximate.

M-CSA (`--uniprot P19367`) returns the catalytic context: entry 696 *hexokinase type I* (EC 2.7.1.1,
3 catalytic residues) and the family neighbour 592 *glucokinase* (EC 2.7.1.2).

## 2. PHYKPL (human, Q8IUZ5) — "wrong reaction mechanism" case

[`ENZYME_SPECIFICITY.md`](../../ENZYME_SPECIFICITY.md) records PHYKPL as annotated transaminase but
actually a **PLP-dependent phospho-lyase** (EC 4.2.3.134). SABIO-RK **corroborates this directly**:

`python query_sabiork.py --ec 4.2.3.134 --summary`

- Record matches the gene exactly: `UniprotID = Q8IUZ5`.
- Substrate: **5-phosphonooxy-L-lysine**, Km ≈ **4.5–16.9 µM**.
- Reaction components in the record: substrate + **H₂O**, **cofactor Pyridoxal phosphate (PLP)**,
  product includes **phosphate** — the signature of a *lyase acting on a C–O–P bond*, **not** a
  transaminase (which would show an amino-donor/amino-acceptor pair, no phosphate release).
- Provenance: **PMID:22241472** — the same paper UniProt cites for `EC=4.2.3.134`.

So an independent kinetic database, queried programmatically, returns evidence consistent with the
MODIFY decision already made (remove transaminase MF; use phospho-lyase). No change to the completed
review is needed; this is confirmatory.

## 3. Coverage reality — where the open caches are silent

An honest, important finding: the open kinetic caches have **sparse coverage for niche and
uncharacterized enzymes**, exactly the hard cases in gene review.

| Gene | Query | Result |
|---|---|---|
| **LPL1** (CANAL, phospholipase B) | SABIO-RK EC 3.1.1.5 | 0 records |
| **yegV** (E. coli, uncharacterized) | SABIO-RK UniProt P0A8A8 | 0 records |
| PHYKPL | SABIO-RK EC 4.2.3.134 | hit (above) |

For LPL1/yegV, fall back to **primary literature** (and M-CSA mechanism where a reference enzyme
exists). The databases help most for *well-studied* enzymes; they do not manufacture data for the
under-characterized ones — which is precisely why curated GO review with full-text reading remains
essential.

## Takeaways

1. The clients work against the live APIs and return **substrate-resolved, PubMed-cited** data
   (hexokinase, PHYKPL).
2. For specificity questions on **studied** enzymes, this is faster and more authoritative than any
   structure/affinity prediction.
3. For **niche/uncharacterized** enzymes the caches are often empty — no shortcut around literature.
4. M-CSA adds the **reaction-class / catalytic-residue** check that kinetics alone cannot give
   (the dimension that distinguishes the PHYKPL phospho-lyase-vs-transaminase error).

## Reproduce

```bash
cd projects/ENZYME_SPECIFICITY_DATA_SOURCES
python query_sabiork.py --ec 2.7.1.1 --organism "Homo sapiens" --summary
python query_sabiork.py --ec 4.2.3.134 --summary
python query_mcsa.py --uniprot P19367
```
