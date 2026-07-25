# AAMP (angio-associated migratory cell protein) — review notes

PAINT no-IBA project review, using the `affinage` deep-research provider
(`AAMP-deep-research-affinage.md`, gates passed) plus UniProt Q13685, the GOA TSV and the
primary literature.

## The most interesting finding: a self-referential IBA

`GO:0014909 smooth muscle cell migration` is annotated **twice** — once IBA, once IEP. The IBA's
WITH/FROM field is `PANTHER:PTN001068868|UniProtKB:Q13685`, and **`Q13685` is human AAMP
itself** — the very gene being annotated (confirmed by UniProt lookup: `AAMP_HUMAN`).

So the phylogenetic inference is seeded by the target gene's own annotation. It transfers
nothing: the human gene already carries the term directly. This is
`EVIDENCE_CIRCULAR_OR_REDUNDANT` in the propagation taxonomy — "the target already has stronger
direct evidence".

Two things follow:

1. The **term is correct** — this is a real AAMP function — so the action is `ACCEPT`, not
   `REMOVE`. The IBA is redundant, not wrong. Worth recording in `propagation_review` so the
   redundancy is visible.
2. The underlying direct annotation is coded **IEP** (expression pattern), which *understates*
   its own paper. PMID:18634987 is not an expression study: it reports
   [PMID:18634987, "The AAMP overexpression increases, while both treatment with anti-rAAMP-ab
   and transfection with siRNA decreases SMC migration."] plus in-vivo antibody blockade
   reducing neointima formation in apoE−/− mice. That is IMP-grade evidence. Flagged as a
   `suggested_question` for the responsible curator rather than silently re-coded here.

## What AAMP actually does — a Rho-family GTPase regulator

The GOA record describes AAMP through its *phenotypes* (migration, angiogenesis) and one
biochemical property (heparin binding). It has **no molecular function connected to the
mechanism**, which the modern literature has worked out in some detail:

- **RhoA.** AAMP binds RhoA directly and shields it from degradation
  [PMID:34901393, "AAMP stabilized RhoA by binding to it and suppressing its SMURF2-mediated
  ubiquitination and degradation."] — raising the active RhoA pool.
- **CDC42.** [PMID:33279622, "AAMP interacted with cell division cycle 42 (CDC42) and promoted
  its activation, resulting in the formation of cellular protrusions."] Affinage adds that this
  works by impeding the ARHGAP1–CDC42 interaction.
- **Pathway context.** [PMID:26350504, "Furthermore, we identified RhoA/Rho kinase signaling as
  an important factor that contributes to the action of AAMP in regulating endothelial cell
  migration and angiogenesis."] and, in smooth muscle,
  [PMID:18634987, "Knockdown of AAMP decreases RhoA activity in the membrane fraction of SMCs."]

Three independent groups, two GTPases, two cell types, consistent direction. This supports
three `NEW` annotations: `GO:0031267 small GTPase binding` (MF), `GO:0050821 protein
stabilization` and `GO:0051057 positive regulation of small GTPase mediated signal transduction`
(BP). Together they convert AAMP from "protein associated with migration" to a protein with a
stated mechanism.

**Term check worth recording:** `GO:0017048 Rho GTPase binding` would have been the more
specific MF, but a direct id lookup shows it is **obsolete**. `GO:0031267 small GTPase binding`
is the correct live term. (This check was added to the workflow after the AAGAB review, where
the reverse error — assuming a term was absent because a keyword search missed it — cost a
review round.)

## The `protein binding` annotations, again orthogonal to the biology

All four `GO:0005515` IPI annotations report the same partner: **AEN** (Q8WTP8), an
apoptosis-enhancing nuclease, from four large-scale interactome papers. There is no functional
follow-up and no described connection between AAMP and AEN.

Meanwhile **none of the four recovered RHOA, RHOB, CDC42, NOD2 or CD276** — every partner with
actual mechanistic follow-up. This is the third gene in this campaign (after AAGAB and AAMDC)
where the high-throughput binding record and the functionally characterised interactions are
disjoint sets. The pattern is worth naming: proteome-scale screens populate `GO:0005515` for
these genes without touching what is actually known about them.

Marked `MARK_AS_OVER_ANNOTATED` rather than `REMOVE` — four screens is real reproducibility,
and the pair may yet mean something.

## Localisation

Cytosol, cytoplasm, plasma membrane and cell surface are all annotated and all consistent with
UniProt [file:human/AAMP/AAMP-uniprot.txt, "SUBCELLULAR LOCATION: Cell membrane. Cytoplasm."].
The cell-surface/extracellular pool is genuine and functionally relevant — it is where heparin
binding and heparin-sensitive cell adhesion happen, and where the blocking antibody acts.

## Suggestion 5: the obsolescence claim, verified in the open

`GO:0017048 Rho GTPase binding` would have been the more specific MF for the RhoA/CDC42
binding, and the choice of `GO:0031267` rests entirely on it being obsolete. That claim is
load-bearing, so here is the lookup rather than an assertion:

```
$ oaklib sqlite:obo:go
GO:0017048 -> label=GO_0017048  is_obsolete=True   (OLS: is_obsolete: true, is_root: true)
GO:0031267 -> small GTPase binding                 (live)
```

An obsolete term has no label and detaches to the root, which is what `GO_0017048` shows.

## Actions

| Term | Evidence | Action |
|---|---|---|
| `GO:0014909` smooth muscle cell migration | IBA, IEP | ACCEPT (IBA flagged circular) |
| `GO:0010595` positive regulation of endothelial cell migration | ISS | ACCEPT |
| `GO:0008201` heparin binding | IDA | ACCEPT |
| `GO:0001525` angiogenesis | NAS | ACCEPT |
| `GO:0009986` cell surface | IDA | ACCEPT |
| cytosol / cytoplasm / plasma membrane | IEA, IDA, TAS | ACCEPT |
| `GO:0005515` protein binding ×4 (all AEN) | IPI | MARK_AS_OVER_ANNOTATED |
| `GO:0031267` small GTPase binding | IPI (proposed) | NEW |
| `GO:0050821` protein stabilization | IMP (proposed) | NEW |
| `GO:0051057` positive regulation of small GTPase mediated signal transduction | IMP (proposed) | NEW |
| `GO:1903141` negative regulation of establishment of endothelial barrier | IMP (proposed) | NEW |
| `GO:0070432` regulation of NOD2 signaling pathway | IMP (proposed) | NEW |

## Two further arms, added after review

- **Endothelial barrier (PMID:39404373).** siRNA depletion of AAMP *increases* trans-endothelial
  electrical resistance, so AAMP is a **negative** regulator of barrier function. The mechanism
  is the same Rho axis: depletion lowers RhoA and RhoB activity, reducing actomyosin contraction
  in resting endothelium. This paper is also the third independent lab to report AAMP-dependent
  Rho regulation, and it extends it to RhoB.
- **NOD2/NF-κB (PMID:19535145).** I had originally left this unannotated because the mechanism
  is unresolved. That conflated *mechanism* with *evidence*: GO regulation terms do not require a
  resolved mechanism, and the paper has overexpression plus siRNA in HEK293T. Annotated to the
  **unsigned parent** `GO:0070432`, because the paper says "modulates" and never establishes a
  direction — `GO:0070434`/`GO:0070433` would assert more than the data support.

**CD276/B7-H3 dropped from the description.** It came from the affinage narrative citing
PMID:35919070, which is neither cited nor cached here. An unverifiable partner should not sit in
a description.
