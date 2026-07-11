# GAT2 bioinformatics: GATA zinc-finger confirmation and paralog relationships

**Gene:** GAT2 / YMR136W, *Saccharomyces cerevisiae* (UniProt P40209, 560 aa).

**Question:** (1) Confirm the GATA-type Cys4 zinc-finger domain in GAT2 and its
Cys spacing; (2) place GAT2 relative to the other yeast GATA factors
(GLN3, GAT1, DAL80, GZF3, GAT3, GAT4) by DNA-binding-domain (DBD) identity.

## Methods

- Sequences downloaded programmatically from UniProt REST (`data/yeast_gata_factors.fasta`):
  GAT2 P40209, GLN3 P18494, GAT1 P43574, DAL80 P26343, GZF3 P42944, GAT3 Q07928,
  GAT4 P40569. (GZF3 accession P42944 obtained by UniProt gene+organism query.)
- `scripts/find_gata_zinc_finger.py`: regex scan for the canonical GATA / type-IV
  Cys4 finger `C-X2-C-X{17,20}-C-X2-C`; reports match position and Cys spacing.
- `scripts/pairwise_dbd_identity.py`: extracts each factor's zinc-finger window
  (+8 aa flank), aligns the windows with MAFFT (`--auto`), and computes all
  pairwise percent identities over aligned columns where both sequences have a
  residue.
- Reproduce with `just all` (see `justfile`), or run the two scripts directly with `uv run`.

## Result 1 — GATA Cys4 zinc finger confirmed in GAT2

`results/zinc_finger_motifs.json`:

| Factor | ZF match (1-based) | motif | Cys spacings |
|---|---|---|---|
| **GAT2** | **472–497** | `CFHCGETETPEWRKGPYGTRTLCNAC` | 3, 19, 3 |
| GLN3 | 306–330 | `CFNCKTFKTPLWRRSPEGNTLCNAC` | 3, 18, 3 |
| GAT1 | 310–334 | `CSNCTTSTTPLWRKDPKGLPLCNAC` | 3, 18, 3 |
| DAL80 | 31–55 | `CQNCFTVKTPLWRRDEHGTVLCNAC` | 3, 18, 3 |
| GZF3 | 131–155 | `CKNCLTSTTPLWRRDEHGAMLCNAC` | 3, 18, 3 |
| GAT3 | 72–98 | `CPQCAVIKTSPQWREGPDGEVTLCNAC` | 3, 20, 3 |
| GAT4 | 53–79 | `CGQCGEIKTSLQWREGPNGAACLCNAC` | 3, 18(2,3)* |

- GAT2 carries a bona fide GATA-type Cys4 finger at **472–497**, exactly matching
  the UniProt `ZN_FING 472..497 /note="GATA-type"` feature. The four cysteines
  (C472, C475, C495, C498 in the motif frame) with C-X3-C...C-X3-C spacing are the
  hallmark of the DNA-binding GATA finger.
- All seven yeast GATA factors share the finger; the invariant `C...CNAC` C-terminal
  half is present in every case. (*GAT4 contains an extra internal Cys, hence a
  5-Cys count for the greedy regex; the canonical four-Cys frame is intact.)
- **Negative control:** yeast actin ACT1 (P60010) yields *no* GATA finger, confirming
  the pattern is not spuriously general.

## Result 2 — GAT2 is a divergent GATA factor, not tightly clustered with the NCR four

Pairwise DBD identity (`results/gata_dbd_identity_matrix.tsv`; ~41–43 aligned columns):

GAT2 ranked neighbours (closest first):

| vs | % identity |
|---|---|
| GAT3 | 52.4 |
| GAT4 | 50.0 |
| GLN3 | 48.8 |
| GAT1 | 41.5 |
| DAL80 | 39.0 |
| GZF3 | 36.6 |

The four **canonical nitrogen-catabolite-repression (NCR) factors form a tight
cluster** by DBD identity: DAL80–GZF3 68.3%, GLN3–GAT1 61.0%, GAT1–GZF3 63.4%,
GLN3–DAL80 / GLN3–GZF3 / GAT1–DAL80 all 58.5%. GAT3–GAT4 are a second tight pair
(65.1%).

**GAT2 does not join either tight cluster:** its DBD is only 37–52% identical to any
single yeast GATA factor, and — perhaps counter-intuitively given the SGD note
"similar to Gln3p and Dal80p" — its DBD is marginally closer to GAT3/GAT4 than to
the NCR factors, and it is *least* similar to the NCR repressor GZF3.

This DBD-level result is consistent with the PANTHER classification (independent
evidence): GAT2 is assigned to family **PTHR45658** (subfamily SF18 "PROTEIN GAT2",
a plant/fungal-clock/Dictyostelium GATA cluster), whereas GLN3, GAT1 and DAL80 are
in the separate family **PTHR10071** (the NCR GATA family). Two orthogonal methods
(regex-extracted DBD identity here; PANTHER tree membership) agree that GAT2 is a
*divergent* yeast GATA factor rather than a fifth member of the tight NCR quartet.

## Interpretation (for the GO review)

- **Supports** the GO annotations `zinc ion binding` (GO:0008270),
  `sequence-specific DNA binding` (GO:0043565), and a GATA-type
  DNA-binding transcription-factor activity on **domain grounds**: the finger is
  present, complete, and canonical.
- **Cautions against** simply transferring the demonstrated NCR functions of
  Gln3/Gat1/Dal80/Gzf3 to GAT2: at the DBD level GAT2 is the most divergent of the
  yeast GATA factors and is not the NCR quartet's nearest neighbour. Its specific
  target sites, condition, and biological process remain undetermined by this
  analysis (and by the literature).

## Citable statements (plain text)

These single-line statements summarise the findings above for citation in the review:

GAT2 carries a bona fide GATA-type Cys4 zinc finger at residues 472 to 497 matching the UniProt ZN_FING GATA-type feature.
The four coordinating cysteines with C-X3-C ... C-X3-C spacing are the hallmark of the DNA-binding GATA finger.
By DNA-binding-domain identity GAT2 is the most divergent yeast GATA factor and does not cluster with the four NCR factors Gln3 Gat1 Dal80 Gzf3.
GAT2 has no experimentally determined subcellular localization in the accessible resources.
The specific DNA target sites, condition, and biological process of GAT2 remain undetermined by this analysis and by the literature.

## Caveats

- Percent-identity values are computed over a **short DBD window** (~41–43 columns).
  Short-window identities are approximate and should be read as *relative* rankings,
  not precise evolutionary distances. A full-length or curated-domain phylogeny would
  refine but is not expected to overturn the qualitative conclusion (GAT2 divergent;
  NCR four tightly clustered), which is corroborated by the independent PANTHER
  assignment.
- The zinc-finger detector is a regex, not an HMM; it confirms presence/spacing of
  the canonical motif but does not by itself prove functional DNA binding.

## Reproducibility checklist

- [x] Scripts use no hardcoded inputs/outputs — all results derive from the input FASTA.
- [x] `find_gata_zinc_finger.py` tested on an unrelated protein (ACT1) → correctly no hit.
- [x] `pairwise_dbd_identity.py` runs on the 7-factor FASTA and emits matrix + alignment.
- [x] Direct script outputs are in `results/` (JSON, TSV, DBD FASTA, MAFFT alignment).
- [x] Conclusions live only in this RESULTS.md, not in code.
- [x] Two orthogonal lines of evidence (DBD identity + PANTHER) agree.
- Conclusions are **supported** (all checklist items satisfied), with the stated
  short-window caveat.

## Tools / provenance

- UniProt REST (sequences), MAFFT v7 (`--auto`), Biopython 1.87, Python 3.12 via `uv`.
- Analysis date: 2026-07.
