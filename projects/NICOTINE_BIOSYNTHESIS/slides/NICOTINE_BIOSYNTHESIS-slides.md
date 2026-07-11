---
title: "Nicotine Biosynthesis Project"
marp: true
theme: default
paginate: true
backgroundColor: #fff
style: |
  section { font-size: 24px; }
  h1 { color: #2c3e50; }
  h2 { color: #34495e; }
  table { font-size: 18px; }
  section.lead h1 { font-size: 48px; }
---

<!-- _class: lead -->

# Nicotine Biosynthesis Project

### Completing the nicotine biosynthesis pathway in *Nicotiana attenuata*

Chris Mungall | AI-Assisted Gene Review

2026-06-22

---

## Why now: the pathway is finally complete

- A **2026 *Cell* paper** ("Complete biosynthesis of nicotine", Chang et al.) closes the last gaps in the *N. attenuata* pathway.
- A parallel 2025 **bioRxiv** preprint (Schwabe et al.) shows nicotine biosynthesis is finished by a **cryptic activating glucosylation**.
- New steps upgraded from side chemistry to **pathway core**: a **glycosylation** step and a **deglycosylation** step.
- Provides a **minimal heterologous reconstruction** path (yeast / *N. benthamiana*).
- Makes a transporter, **NaMATE1**, a core metabolon component rather than a peripheral annotation.

---

## Why *Nicotiana attenuata*

- The new *Cell* mechanistic closure is **in *N. attenuata*** itself — no cross-species translation noise at project start.
- Strong prior pathway/evolution work already centered on *N. attenuata* (not just cultivated *N. tabacum*).
- Rich **root-expression and ecology** literature helps separate true biosynthetic genes from housekeeping paralogs and regulators.
- Deliberately **not** seeded in *N. tabacum*: forcing tobacco→attenuata orthology up front would add avoidable paralog noise.

Species code: `NICAT`.

---

## The pathway: two branches that couple

- **Pyridine branch** (from aspartate): supplies nicotinic acid.
  - `NaAO2` (aspartate oxidase) → `NaQPT2` (quinolinate phosphoribosyltransferase) → `NaNAMNH` (NAMN hydrolase → nicotinic acid).
- **Pyrrolidine branch** (from polyamines): supplies the N-methyl-Δ1-pyrrolinium cation.
  - `NaODC1`/`NaODC2` → `NaPMT1.1`/`NaPMT1.2` (N-methylputrescine) → `NaMPO1` (oxidation).
- **Coupling + late steps**: the two branches join and are finished by the glycosylation/condensation/deglycosylation module.

---

## The late module: glycosylate → couple → deglycosylate

From the bioRxiv mechanistic reconstitution (tobacco enzymes; *N. benthamiana* in planta):

| Enzyme | Assigned role |
|---|---|
| `UGT1` (NaGT) | nicotinic acid N-glucosyltransferase |
| `A622` (NaGR) | nicotinic acid N-glucoside reductase |
| `BBLa` (NicGS) | (S)-nicotine glucoside synthase (sets stereoselectivity) |
| `beta-GD1` (NicGH) | nicotine glucoside hydrolase → (S)-nicotine |

A **four-enzyme cascade** (UGT1 + A622 + BBLa + beta-GD1) reconstitutes **(S)-nicotine** in vitro.

---

## The approach: AI gene review framework

- Review each core gene's existing GO annotations against literature + bioinformatics evidence, then synthesize core functions.
- Project owns three things:
  1. The canonical single-species nicotine pathway **gene list**.
  2. The **review-job table** that fetches/creates review stubs.
  3. The **accession-resolution backlog** for *Cell*-era names not yet normalized in public resources.
- Two-layer naming: a **canonical symbol layer** (biology) and a **launch-job layer** (current fetchable accessions).

---

## The seed gene set (1/2): upstream supply

| Gene | Role | State |
|---|---|---|
| `NaAO2` | Pyridine branch entry from aspartate | Provisional accession |
| `NaNAMNH` | NAMN hydrolase → nicotinic acid (new *Cell* step) | Pending accession |
| `NaQPT2` | Quinolinate phosphoribosyltransferase | Provisional accession |
| `NaODC1`, `NaODC2` | Pyrrolidine precursor supply | Provisional accession |
| `NaPMT1.1`, `NaPMT1.2` | N-methylputrescine formation | Launch-ready |
| `NaMPO1` | Oxidation to pyrrolinium intermediate | Candidate mapping |

---

## The seed gene set (2/2): coupling, late steps, transport

| Gene | Role | State |
|---|---|---|
| `NaUGT1` | Glycosylation step producing NG (new *Cell* step) | Candidate mapping |
| `NaA622` | Ring-condensation branch point | Launch-ready |
| `NaBBL1`, `NaBBL2` | Late oxidation after condensation | Provisional accession |
| `NaBGL1`, `NaBGL2` | Deglycosylation NG → nicotine (new *Cell* step) | BGLU18 candidates ready |
| `NaMATE1` | Vacuolar metabolon transporter / export | Candidate mapping |

Minimal heterologous set (*Cell*): `NaODC`, `NaPMT1`, `NaMPO`, `NaUGT1`, `NaA622`, `NaBBL2`, `NaBGL1`, `NaMATE1`.

---

## Accession mapping dive (2026-04-05)

Sequence-backed cross-release candidates (tobacco loci → NIATv7 → UniProt `NICAT`):

| Canonical | Candidate accession |
|---|---|
| `NaMPO1` | `AMO_3` / A0A314KPU1 |
| `NaMATE1` | `DTX40_3` / A0A314KVN4 |
| `NaUGT1` | `UGT85A2_0` / A0A2H4GSI3 |
| `NaBGL1` | `BGLU18_6` / A0A1J6KFZ7 |
| `NaBGL2` | `BGLU18_1` / A0A314KWB2 |

`BGLU18` candidates now anchor the **beta-GD** deglycosylases; `BGLU42` demoted to a historical comparator.

---

## Challenges

- **Non-model plant**: public annotation still trails the *Cell* paper's `Na...` nomenclature for several genes.
- **Paralogs everywhere**: ODC, PMT, BBL, BGL families each expose duplicated copies — pick the real pathway member, not a housekeeping paralog.
- **Cross-species evidence**: mechanistic/structural work is on **tobacco** enzymes + *N. benthamiana* reconstitution, strong for **role assignment** but weak for exact NICAT accession resolution.
- **Transport / compartmentation**: `NaMATE1` (and follow-up `NaNUP`) tie biosynthesis to vacuolar export.
- **Open gap**: `NaNAMNH` has a clear function but no stable public NICAT accession yet.

---

## Status and what's left

Project maturity: **MATURE**.

- All 22 current `launch_ready` aliases fetched into `genes/NICAT/` and advanced to **DRAFT** review state.
- `NaUGT1`, `NaMPO1`, `NaBGL2`, `NaMATE1` converted from backlog into sequence-backed candidate jobs.
- PMT paralog pair curated beyond seeded stubs.

Remaining worklist:
- [ ] Resolve a stable public accession for `NaNAMNH`.
- [ ] Revisit whether `NaNUP` belongs in the core transport batch after the minimal metabolon is reviewed.

---

## Excluded from seed (tracked as follow-up)

- `NaNUP` — transport-associated, but not part of the minimal *Cell* metabolon.
- `NaERF1-like`, `NaMYC2` — important regulators; settle the enzyme/transport core first.
- `NaAO1`, `NaQPT1`, `NaQS` — housekeeping / parallel-pathway comparators.

Rationale: keep the seed conservative — enzymes and transport first, control logic later.

---

## Key sources

1. Chang L, *et al.* 2026. **Complete biosynthesis of nicotine**. *Cell*.
2. Schwabe BTW, *et al.* 2025. **Nicotine biosynthesis completed by cryptic activating glucosylation**. *bioRxiv* (DOI 10.64898/2025.12.04.692101).
3. Xu S, *et al.* 2017. **Wild tobacco genomes reveal the evolution of nicotine biosynthesis**. *PNAS* (PMC5468653).
4. Zhang *et al.* 2025. DNA methylation valleys in root-specific nicotine genes in *N. attenuata*. *Front. Plant Sci.* (PMC12361153).

Proteome/accession resources: Sol Genomics Network (Nitab v4.5, NIATv7) + UniProtKB `NICAT` stream.
