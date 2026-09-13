# APOC4 bioinformatics — results

Two questions came up while reviewing the human APOC4 (UniProt P55056) GO
annotations that could be settled by computation rather than asserted from
memory. Both scripts fetch their inputs live and print the numbers they derive;
nothing below is hardcoded.

Reproduce with:

```bash
uv run python family_taxonomy.py
uv run python amphipathic_helix.py
uv run python huri_partner_topology.py
```

Run date: 2026-09-12. Outputs are also written to `family_taxonomy_result.json`,
`family_members.tsv`, `amphipathic_helix_result.json`, `huri_partners.tsv` and
`huri_partner_topology_result.json`.

---

## 1. Is PANTHER family PTHR32288 confined to Eutheria?

**Why it matters.** All four IBA rows on human APOC4 descend from the single PAINT
IBD node `PANTHER:PTN000792756`, which PAINT places at `taxon:9347` (Eutheria).
Reviewing an IBA means arguing with the node placement, so the first thing to
establish is whether the target sits inside the clade the node covers, and
whether the node is over-reaching the family's real taxonomic span.

**Method.** `family_taxonomy.py` pulls every UniProt protein InterPro assigns to
PTHR32288 (paginated, `api/protein/UniProt/entry/panther/PTHR32288`), collects the
distinct source organisms, resolves each organism's full NCBI lineage from the
UniProt taxonomy REST service, and tests each for the presence of taxon 9347.

**Result.**

| quantity | value |
|---|---|
| UniProt members in PTHR32288 | 189 |
| distinct source organisms | 149 |
| organisms inside Eutheria | 146 |
| organisms outside Eutheria | 3 |
| members whose organism is inside Eutheria | 185 / 189 |
| member length (min / median / max) | 39 / 127 / 260 |

The four members outside Eutheria are:

| accession | length | organism | InterPro name |
|---|---|---|---|
| A0A4X2JTF9 | 144 | *Vombatus ursinus* (common wombat) | Apolipoprotein C-IV |
| A0A6P5LMY2 | 142 | *Phascolarctos cinereus* (koala) | Apolipoprotein C-IV |
| A0A6P5LUG1 | 146 | *Phascolarctos cinereus* (koala) | Apolipoprotein C-IV |
| A0ACF7XIT4 | 177 | *Tetrahymena utriculariae* | Uncharacterized protein |

**Interpretation.** 98% of the family is eutherian. The only credible extension
beyond Eutheria is three marsupial (Metatheria) sequences, so the family spans at
most Theria; the single ciliate hit is an uncharacterised protein and is almost
certainly a spurious HMM match rather than a genuine apolipoprotein C-IV. The
PAINT node at Eutheria is therefore placed at or just inside the family's own
origin — a conservative placement, not an over-reach — and every mammalian APOC4,
human included, is inside the clade that inherits the node's assertions. This is
an independent, data-derived corroboration of the published phylogenetic claim
that "ApoC-IV first arose in Eutheria" (PMID:31722659).

It also frames the one direction in which the node is *under*-reaching: if the
marsupial sequences are real orthologues, the IBD could arguably sit one node
deeper, at Theria. Nothing in the GO annotations depends on that.

## 2. Does human apoC-IV carry apolipoprotein-like amphipathic helices?

**Why it matters.** The sole molecular-function row on APOC4 (GO:0005319 lipid
carrier activity, TAS) traces to PMID:8530039, which inferred it from "two
potential amphipathic alpha-helical domains" in the *predicted* sequence. The only
direct biophysical demonstration anywhere in the family is on the rabbit
orthologue, which "forms discoidal micelles with phosphatidylcholine"
(PMID:8576182). The sequence-level half of that inference is testable.

**Method.** `amphipathic_helix.py` fetches each protein from UniProt, asserts the
accession resolves to the expected entry (a demerged accession is rejected rather
than silently scored), trims to the longest annotated `CHAIN` feature so signal
peptides are excluded, and scans the Eisenberg normalised-consensus hydrophobic
moment over 18-residue windows at 100° per residue. Two summary statistics are
reported: the single strongest window (`maxMuH`), and the number of
*non-overlapping* windows reaching Eisenberg's surface-seeking cutoff μH ≥ 0.35,
normalised by mature-chain length (`seg/res`).

**Result.**

| protein | chain | mature len | max μH | mean H (chain) | n segments μH≥0.35 | segments/residue | role |
|---|---|---|---|---|---|---|---|
| APOC4_HUMAN | 28–127 | 100 | 0.515 | −0.145 | 3 | 0.0300 | target |
| APOC4_RABIT | 28–124 | 97 | 0.399 | −0.097 | 3 | 0.0309 | orthologue with direct lipid-binding data |
| APOC4_MOUSE | 28–124 | 97 | 0.498 | −0.144 | 2 | 0.0206 | orthologue, IBA donor |
| APOC1_HUMAN | 27–83 | 57 | 0.572 | −0.239 | 2 | 0.0351 | exchangeable apoC control |
| APOC2_HUMAN | 23–101 | 79 | 0.399 | −0.051 | 2 | 0.0253 | exchangeable apoC control |
| APOC3_HUMAN | 21–99 | 79 | 0.514 | −0.029 | 2 | 0.0253 | exchangeable apoC control |
| APOA1_HUMAN | 19–267 | 249 | 0.535 | −0.196 | 8 | 0.0321 | class-A amphipathic-helix positive control |
| B2MG_HUMAN | 21–119 | 99 | 0.459 | −0.114 | 1 | 0.0101 | secreted all-β negative control |
| THIO_HUMAN | 2–105 | 104 | 0.483 | 0.056 | 1 | 0.0096 | cytosolic globular negative control |

Human apoC-IV's three high-moment segments begin at mature residues 26, 56 and
81; the strongest window is `RMKELLETVVNRTRDGWQ` (mature residue 26).

**Interpretation.** The single strongest window does *not* discriminate: both
negative controls reach μH ≈ 0.46–0.48 somewhere in their sequence, because any
100-residue protein contains some window with a lopsided hydrophobic face. What
separates the two classes cleanly is how much of the chain is built that way. The
seven exchangeable apolipoproteins fall in 0.0206–0.0351 high-moment segments per
residue; the two globular controls fall at 0.0096–0.0101. The groups do not
overlap, and the script derives the separation rather than asserting it: 2.04× at
the narrowest (mouse apoC-IV against β2-microglobulin) and 3.66× at the widest
(APOC1 against thioredoxin). Human apoC-IV sits at 0.0300 — inside the
apolipoprotein band, between APOC2/C3 (0.0253) and APOC1 (0.0351), about three
times the controls (2.97–3.12×), and differing by 0.0009 from rabbit apoC-IV
(0.0309), the orthologue for which discoidal-micelle formation with
phosphatidylcholine was actually measured, and by 0.0021 from APOA1 (0.0321). No
significance test is offered here: with nine proteins and one statistic each, the
claim is the group separation, not a p-value on any individual pair.

This supports, at the sequence level, that human apoC-IV is built like an
exchangeable, lipid-surface-seeking apolipoprotein, and so supports retaining
GO:0005319 and proposing phospholipid binding by similarity to the rabbit
orthologue. It does **not** by itself demonstrate lipid binding by the human
protein — a hydrophobic-moment scan is a sequence statistic, not an assay, and
the direct measurement remains rabbit-only.

One small refinement of the 1995 prediction: the scan finds three non-overlapping
high-moment segments in the human mature chain rather than two. The window
definition differs from whatever the original authors used, so this is a
difference in method rather than a contradiction, and nothing in the review rests
on the count being two or three.

## 3. Can APOC4 reach the compartment its 23 two-hybrid partners occupy?

**Why it matters.** All 23 GO:0005515 rows on APOC4 come from one reference,
PMID:32296183 (HuRI), a systematic yeast two-hybrid screen. The review marks every
one `MARK_AS_OVER_ANNOTATED`, and that judgement rests on where the partners live.
Those counts are load-bearing for 23 annotation decisions, so they should be
re-runnable rather than asserted.

**Method.** `huri_partner_topology.py` takes the 23 `WITH/FROM` entities exactly as
GOA records them, fetches each from UniProt (rejecting any inactive entry rather
than scoring it), and records the verbatim `SUBCELLULAR LOCATION` values plus
whether the protein has a transmembrane segment or a cleaved signal peptide. It
asserts first that the target itself resolves to APOC4_HUMAN, is curated Secreted,
and carries a signal peptide.

**Result.**

| quantity | value |
|---|---|
| partners resolved | 23 / 23 |
| with a curated Secreted or Extracellular location | **0** |
| with a curated mitochondrial location | 10 |
| with a transmembrane segment | 10 |
| with a cleaved signal peptide | 1 (THBD) |
| with no curated subcellular location at all | 1 (SYT16) |

Per-partner rows are in `huri_partners.tsv`.

**Interpretation.** The useful distinction is not "intracellular" — APOC4's mature
chain *does* pass through the ER and Golgi, so sharing a compartment name with a
secretory-pathway protein proves nothing on its own. It is **which face** of that
compartment. APOC4 is lumenal throughout its transit and extracellular thereafter;
it never faces the cytosol, the mitochondrial matrix or the nucleus. Twenty-one of
the 23 partners do their work on the cytosolic side or inside an organelle APOC4
never enters; the two that are not in that class are handled below. And whatever
their native compartment, all 23 pairs were scored by a Gal4 two-hybrid in the
yeast nucleus — a compartment the target cannot occupy at all — so the assay could
not have observed any of them where it matters.

Five partners (MICOS10, MICOS13, MAIP1, BCL2L2, TIMMDC1) are curated *exclusively*
to the mitochondrion, which has no connection to the secretory pathway at all;
those rows get the sharpest version of the argument. THBD is the one partial
exception and is flagged as such in its own row: as a single-pass type I membrane
protein it genuinely presents an extracellular domain to flowing blood, so an
encounter with a plasma apolipoprotein is not topologically absurd — but that is
exactly the topology a nuclear two-hybrid cannot test, and no follow-up experiment
exists. SYT16 has no curated location, so its pair cannot be assessed for
compartment compatibility either way.

This analysis does **not** show the interactions are false. It shows the assay could
not have observed them in a physiological compartment, and that no orthogonal
experiment has since done so — which is the basis for over-annotation rather than
removal.

## Caveats

- Both analyses are sequence/database analyses. Neither is an experiment, and
  neither can establish a function the literature has not measured.
- The hydrophobic-moment threshold (μH ≥ 0.35) and window length (18) are
  conventional choices, not fitted; the separation between the apolipoprotein and
  globular groups is robust to them only within the range tested here.
- The InterPro member list reflects PANTHER HMM assignment, which is why an
  uncharacterised ciliate protein appears in the family; family membership is not
  a curated orthology assertion.
