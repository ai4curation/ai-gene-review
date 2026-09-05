# AGT (P01019) — bioinformatics support for the annotation review

Three questions came out of the GOA record for human angiotensinogen that can be
settled from sequence and database evidence rather than from assertion. Each
script fetches live from the UniProt and QuickGO REST APIs (responses cached
under `cache/`, which is disposable) and from the committed PANTHER PAINT slice
`interpro/panther/PTHR11461/PTHR11461-paint.tsv`. Nothing below is hardcoded;
delete `cache/` and re-run to regenerate every number.

```
uv run python resolve_withfrom.py      # -> withfrom_resolved.tsv, supporting_entities.json
uv run python serpin_inhibitory.py     # -> serpin_inhibitory.tsv
uv run python y2h_partners.py          # -> y2h_partners.tsv
```

---

## 1. Is angiotensinogen an inhibitory serpin? (`serpin_inhibitory.py`)

**Question.** GOA asserts `GO:0004867 serine-type endopeptidase inhibitor
activity` for AGT three times — by IBA from PANTHER node `PTN008970140`, by IEA
from InterPro `IPR000215` (Serpin_fam), and by TAS from PMID:3397061. The GO
definition is *"Binds to and stops, prevents or reduces the activity of a
serine-type endopeptidase"*, so the claim is falsifiable.

**Method.** A serpin inhibits by presenting a **reactive bond** (P1–P1') on its
reactive centre loop and then inserting that loop into β-sheet A, which requires
small residues in the **hinge** at P12–P9. Two independent, machine-readable
proxies were therefore measured for every protein in the panel:

- whether UniProt annotates a `SITE` of description *"Reactive bond"*;
- the residues aligned to SERPINA1's hinge, using SERPINA1's own annotated
  reactive bond (P1 = Met382) as the anchor and a global BLASTP-matrix alignment;
- MEROPS classification, read from UniProt cross-references. MEROPS reserves the
  `.9xx` range of family I04 for **non-inhibitor homologues**.

The panel is derived, not hand-picked: the target, plus every seed protein of
the IBD node AGT inherits the term from (read out of the PAINT slice), plus every
reviewed human SERPINA protein (AGT's own clade), plus three reviewed
non-inhibitory serpins from other clades as controls.

**Result** (19 serpins; full table in `serpin_inhibitory.tsv`):

| | MEROPS class | UniProt "Reactive bond" | hinge P17–P9 | small at P12–P9 |
|---|---|---|---|---|
| **P01019 AGT (target)** | **I04.953 — non-inhibitor homologue** | **not annotated** | **ADEREPTES** (res. 425–433) | **2/4** |
| P01009 SERPINA1 (anchor) | I04.001 — inhibitor | Met382 | EKGTEAAGA (res. 366–374) | 4/4 |
| 7 non-inhibitor homologues | I04.9xx | 1/7 annotated | — | mean 2.57/4 |
| 12 inhibitors | I04.0xx / I04.082 / I04.091 | 10/12 annotated | — | mean 3.58/4 |

- **All 7 resolvable seed proteins of IBD node `PTN008970140` are MEROPS
  inhibitors (7/7).** AGT is the only protein in the panel's SERPINA clade that
  is *both* a seed's clade-mate and a MEROPS non-inhibitor homologue. Two of the
  nine seeds (rat `Q5M7T5` Serpinc1, rat `A0ABK0LNG6` Serpina5) were dropped
  because their UniProt entries carry no MEROPS cross-reference; their human
  orthologues SERPINC1 and SERPINA5 are both classed as inhibitors.
- AGT carries **no annotated reactive bond**, unlike 10 of the 12 inhibitors.
- At the hinge position equivalent to SERPINA1 Ala371 (**P12**), AGT has
  **Pro430**. A proline at P12 is incompatible with the hinge opening that loop
  insertion into β-sheet A requires. AGT's hinge also carries Glu427, Arg428 and
  Glu429 where inhibitory serpins hold Thr/Glu/Ala.

**Caveats, stated rather than hidden.** The two proxies are not perfect and the
script shows where they disagree. SERPINH1/HSP47 carries inhibitor-range MEROPS
ids (I04.035/036) yet has a fully degenerate hinge (0/4) — a collagen chaperone
that MEROPS classes optimistically. SERPINA2 is MEROPS I04.952 yet retains an
annotated reactive bond and a 4/4 hinge. So neither measure alone is decisive.
What matters for AGT is that **both** measures put it at the non-inhibitory end
while **all** of the seeds that donated the term sit at the inhibitory end.

**Independent confirmation from the literature.** The crystallographic paper
states it outright: *"angiotensinogen-a non-inhibitory member of the serpin
family of protease inhibitors"* (PMID:20927107), which also reports that AGT
retains the serpin fold at only 22% identity to its closest serpin relatives and
that its reactive centre loop is exposed and mobile rather than engaged. AGT's
physiological protease partner, renin, is an **aspartyl** protease, and AGT is
its **substrate**, not its inhibitor.

**Conclusion.** The `GO:0004867` rows are a family-level inference that does not
survive contact with the target's own sequence. This is a propagation failure at
`PTN008970140`, not a defect in any seed annotation.

## 2. Every WITH/FROM identifier resolved (`resolve_withfrom.py`)

35 of the 114 GOA rows carry a WITH/FROM field; they contain **80 distinct
tokens**, and all 80 resolved (0 unresolved). MOD identifiers were looked up with
`size=5` so that multi-hit ambiguity is visible rather than silently collapsed;
29 tokens returned more than one UniProt entry (canonical Swiss-Prot plus TrEMBL
fragments/isoforms) and the reviewed entry was preferred in each case.

Findings that bear on the review:

- `MGI:MGI:87963` → **P11859, mouse Agt**; `RGD:2069` → **P01015, rat Agt**;
  `UniProtKB:P01019` → the target itself. These three, plus node
  `PTN008518321`, are the entire evidence base of the `GO:0038166` and
  `GO:0042981` IBAs — an angiotensinogen-specific node seeded by
  angiotensinogens, which is exactly what a well-placed IBD looks like.
- The `GO:0005576` IBA node `PTN000156123` is seeded by 51 proteins spanning the
  whole secreted-serpin range, **including non-inhibitory ones** (SERPINF1/PEDF,
  SERPINA6/CBG, SERPINA7/TBG, ovalbumin). Secretion is the property they
  genuinely share, so this node is correctly placed and correctly broad.
- The `GO:0004867` node `PTN008970140` is seeded **only** by inhibitors — see §1.

A useful contrast is visible inside the same family: at node `PTN002606963`,
PAINT curators recorded an **IRD** (`negated=true`) against `GO:0005576` to stop
the extracellular-region inference reaching the ER-resident/intracellular serpin
subclade. The machinery to block a bad propagation exists and is in use in this
very family; it simply has not been applied to angiotensinogen for
`GO:0004867`.

## 3. Compartments of the `protein binding` IPI partners (`y2h_partners.py`)

AGT is `Secreted` with a cleaved signal peptide (UniProt keyword `Signal`).
Sixteen `GO:0005515` / receptor-binding IPI partners were taken straight from the
GOA WITH/FROM fields and their UniProt subcellular locations fetched:

| Reference | partners | share a secreted/extracellular compartment |
|---|---|---|
| PMID:32814053 (large-scale Y2H, neurodegeneration interactome) | 10 | **0** |
| PMID:16237761 (Y2H, HCV F protein bait) | 1 | 0 |
| PMID:20927107 (renin, crystal structure) | 1 | 1 |
| PMID:23082758 (*Drosophila* AnCE, crystal structure) | 1 | 1 |
| PMID:18202720 / PMID:1378723 / PMID:10406457 (angiotensin receptors) | 3 | 0 (cell membrane) |

All ten PMID:32814053 partners are intracellular — mitochondrial intermembrane
space and matrix (NME4), cytosol (EIF2B4), nucleus/cytoplasm (PRMT5, SLFN12), ER
membrane (VKORC1L1), trans-Golgi network (TGOLN2), dendrite/membrane (TMEM185A),
membrane (SNX12) — plus two with no annotated location (NPHP1, PRRG2). A yeast
two-hybrid assay reconstitutes a transcription factor in the yeast nucleus, so a
secreted, disulfide-bonded, four-site N-glycosylated plasma protein is being
tested in a compartment it never occupies. None of the ten has functional
follow-up, and UniProt records `NbExp=3` for each, which is replicate counts
within one study, not three studies.

**The 0/3 for the angiotensin receptors is not a mismatch and should not be read
as one.** AGTR1/AGTR2 are cell-membrane proteins whose ligand-binding face is
extracellular; a secreted ligand meeting a cell-surface receptor is the normal
case. The metric is only diagnostic for the yeast two-hybrid rows.

---

## What this does and does not establish

- It **does** establish that AGT lacks the two sequence features required for
  serpin-mechanism protease inhibition, that MEROPS classes it as a
  non-inhibitor homologue, and that every seed of the IBD node donating
  `GO:0004867` is an inhibitor.
- It **does** establish that the ten-partner Y2H block is a systematic
  compartment mismatch.
- It **does not** test whether AGT inhibits any protease by a non-serpin
  mechanism; no such activity has been reported, but absence of a report is not
  a measurement. The `GO:0004867` verdict rests on the term's own definition
  (serpin-type inhibition of a serine endopeptidase) plus the published
  statement that AGT is non-inhibitory, not on this analysis alone.
- It **does not** test the individual Y2H interactions; it shows only that their
  provenance and compartments make them unsuitable as the basis for a functional
  claim.
