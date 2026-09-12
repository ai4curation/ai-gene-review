# AP3D1 (O14617) — bioinformatics support for the annotation review

Two questions from the GOA record for human AP-3 delta can be settled from
sequence and from the records the pipeline already commits, rather than from
assertion. Both scripts fetch live (UniProt REST, cached under the disposable
`cache/`) and read the committed PANTHER slice
`interpro/panther/PTHR22781/PTHR22781-entries.csv`. Nothing below is hardcoded;
delete `cache/` and re-run to regenerate every number.

```
uv run python delta_interfaces.py      # -> delta_interfaces.tsv   (needs mafft on PATH)
uv run python goa_reconcile.py         # -> pass/fail, counts
```

---

## 1. Are the delta ARF1 and VAMP7 interfaces family features? (`delta_interfaces.py`)

**Question.** Three interfaces on AP-3 delta have been mapped at residue
resolution, and all three were mapped **on human AP3D1 itself**, so their
positions need no cross-species inference:

| site | residues | source |
|---|---|---|
| ARF1 site 1 | F77, M110, L111 | PMID:42139345 (mutants `δF77S, δM110S, δL111S`) |
| ARF1 site 2 | H157, K159, R163, R187 | PMID:42139345 (mutants `δH157D, δK159D, δR187D, δR163D`) |
| VAMP7 hinge | I702, V704, L709, L713 | PMID:22521722 (`mut1` I702S/V704S, `mut2` L709S/L713S); PDB 4AFI = O14617 680–729 |

PMID:39705307 independently localises the primary ARF1 site to delta by
hemicomplex pulldown, and its cryo-EM depositions 9C58/9C59/9C5B/9C5C map to
O14617 1–617. The review needs to know two things these papers do not state:
whether human really carries those residues, and whether the interfaces are
delta-family features or generic adaptin features.

**Method.** One MAFFT `--auto` alignment over a panel that is derived, not
hand-picked: every reviewed member of `PTHR22781` in the committed InterPro
slice (9 proteins, all `PTHR22781:SF12`, human through *Arabidopsis*), plus the
four human large subunits of the *other* adaptor complexes as out-of-family
controls — AP3B1 (`PTHR11134`), AP1G1, AP2A1 and AP4E1 (all `PTHR22780`). The
column each human position occupies is read off, and each panel member's own
native position is reported alongside its residue.

The script asserts `len(O14617) == 1153` and asserts each of the eleven claimed
residues **before** aligning, so a changed sequence or a mistyped position fails
loudly instead of producing a plausible table.

**Results** (`delta_interfaces.tsv`; identity to human at the site positions):

| site | positions | PTHR22781 members (excl. human) | out-of-family controls |
|---|---|---|---|
| ARF1 site 1 | 3 | mouse 3/3, bovine 3/3, fly 3/3, *S. cerevisiae* 3/3, *Eremothecium* 3/3, *S. pombe* 3/3, *Dictyostelium* 2/3, *Arabidopsis* 2/3 | AP3B1 1/3, AP1G1 1/3, AP2A1 1/3, AP4E1 1/3 |
| ARF1 site 2 | 4 | mouse 4/4, bovine 4/4, fly 2/4, *Eremothecium* 2/4, *S. pombe* 2/4, *Arabidopsis* 2/4, yeast 1/4, *Dictyostelium* 1/4 | AP3B1 1/4, AP1G1 1/4, AP2A1 1/4, AP4E1 3/4 |
| VAMP7 hinge | 4 | mouse 4/4, bovine 4/4, fly 3/4, *Dictyostelium* 3/4, yeast 1/4, *S. pombe* 1/4, *Arabidopsis* 1/4, *Eremothecium* 0/4 | AP3B1 0/4, AP1G1 1/4, AP2A1 0/4, AP4E1 0/4 |

**Verified, first.** All eleven residues are present in O14617 at exactly the
published positions (the pre-alignment assertions pass). The papers' numbering
is human numbering.

**ARF1 site 1 is an ancient delta feature.** 3/3 from budding yeast to human
inside the family; 1/3 in every out-of-family control. Consistent with
PMID:39705307's finding that the delta site is structurally the analogue of the
AP-1 gamma / COPI site while the *primary* site differs between complexes.

**ARF1 site 2 is a basic patch, mammal-tight and deeper-taxon-loose.** 4/4 in
mouse and bovine, 1–2/4 outside vertebrates. This is weaker than "universally
conserved" and matches the paper's own hedged wording ("highly conserved among
multicellular eukaryotes"). AP4E1 scoring 3/4 is the expected result rather than
a contradiction: the basic ARF1-contact patch is a general adaptin large-subunit
feature, not delta-private — what is delta-private, per PMID:39705307, is that
this is AP-3's *primary* rather than secondary site.

**The VAMP7 hinge is metazoan-enriched and delta-private.** 0/4 or 1/4 in all
four out-of-family human controls; 1/4 or less in the three fungi; 3–4/4 across
metazoa and *Dictyostelium*. Two independent signals agree, because the hinge
sits inside InterPro `IPR010474`, whose name is literally "AP-3 complex subunit
delta domain, metazoa".

**Caveat.** The hinge lies between UniProt's two MobiDB-lite disordered regions
(629–696 and 726–920), so column assignment there is less reliable than in the
HEAT trunk, and the fungal/plant scores should be read as "not recoverable from
this alignment" rather than as demonstrated loss. The mouse and bovine results
do not depend on the alignment being right in a hard region: both proteins come
out with **native positions identical to human's for all eleven residues**
(`native_position` column), which is what the review's `residue_claims` use as
anchor coordinates.

**Use in the review.** The Bilateria IBD node `PTN000513028` is seeded by mouse
Ap3d1 (plus rat, for `GO:0016182`). Recording that human retains every mouse
residue at these interfaces is the checkable form of "there is no
target-specific evidence of divergence that would undercut the transfer" —
encoded as `RETAINED` `residue_claims` with anchor `UniProtKB:O54774`, target
`UniProtKB:O14617`, method `MSA`.

---

## 2. Does the review YAML still match the GOA file? (`goa_reconcile.py`)

**Question.** `existing_annotations` is seeded deterministically from
`AP3D1-goa.tsv` and then hand-edited. Nothing in `just validate` proves the
edited file still corresponds 1:1 to the GOA rows, or that a
`propagation_review.source_entities` entry names a source the row actually
carries.

**Method.** Both sides are reduced to a multiset keyed on
`(GO id, evidence code, reference, normalized WITH/FROM set)` and compared. The
script additionally checks that every IBA row, and every ISS/ISO/IEA/IC row with
`supporting_entities`, has a `propagation_review`; that every
`source_entities[].source_id` appears in that row's own `supporting_entities`
(the defect that drift produces when these lists are hand-typed); and that every
reference cited anywhere is declared in `references:`.

**Result.** 59 GOA rows ↔ 59 GOA-derived YAML entries, no key unmatched in
either direction. Evidence codes: IEA 29, IBA 10, NAS 8, IMP 3, HDA 2, TAS 2,
ISS 2, IPI 1, IDA 1, IC 1. 42 rows require a `propagation_review` (10 IBA plus
32 IEA/ISS/IC rows carrying `supporting_entities`). Every count quoted in
`AP3D1-notes.md`, in the review YAML and in the PR body comes from this script's
output rather than from a hand tally.
