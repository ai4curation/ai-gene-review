---
title: "HAMAP Rule Review"
collections: [FUNCTION_PREDICTION]
maturity: IN_PROGRESS
tags: [PIPELINE, EVALUATION]
species: [METTH, METJA]
genes: [mtrA2, mtrA1, mtrH, mtrA]
---

# HAMAP Rule Review

**Bottom line:** HAMAP is UniProt's curated rule system for microbial protein
families, and its output is what most unreviewed bacterial and archaeal
proteins carry as their name, EC number, location and GO terms. This project
reviews HAMAP rules the way [ARBA_REVIEW](ARBA_REVIEW.md) reviews ARBA rules,
starting from rules that gene reviews have already caught misfiring. The first
case comes from the [ARCHAEA](ARCHAEA.md) project: rule MF_01093 (MtrA) is
written for the membrane-anchored subunit of the methyltransferase complex but
is allowed to annotate a soluble paralog too, which then receives a membrane
location, a transmembrane segment inside its soluble domain and the whole
complex's reaction. The rule review counts 22 such
soluble homologues among the 219 proteins the rule annotates, every one given
the membrane, complex and reaction statements; a length condition separates
them cleanly. A scan of every HAMAP rule finds that this shape is rare: of 18
rules built the same way, only MF_01093 gives proteins a transmembrane segment
with no hydrophobic stretch behind it.

## Why HAMAP

- HAMAP rules are manually curated per family, so a misfire is a fixable
  rule-design choice rather than a statistical artefact, unlike ARBA.
- Their consequents are copied into UniProtKB as names, EC numbers, comments,
  features and keywords, and into GO through UniRule (GO_REF:0000104) and the
  combined pipeline (GO_REF:0000120). An error in one rule therefore reaches
  every member in every proteome.
- `rules/unirule/` already caches 4,535 UniRule records synced with
  `just unirule-sync`, 2,281 of them HAMAP rules (MF_ accessions). Until now
  none had a review.

## The MF_01093 failure

MF_01093 annotates MtrA, the cobamide-carrying subunit of the
Na+-translocating methyl-H4MPT:coenzyme M methyltransferase. Three features of
the rule combine:

| Feature | In MF_01093 | Effect on a soluble paralog |
|---|---|---|
| Duplicate clause | `Duplicate: in METRM, METTH, METTM` | the rule may annotate a second, MtrA-like protein in the same proteome |
| Unconditional location | `SUBCELLULAR LOCATION: Cell membrane; Single-pass membrane protein`, outside any `case` | every member is placed in the membrane |
| Transmembrane trigger | `DR General; Transmembrane; ...; trigger=yes` | a transmembrane segment is predicted on every member and written as a feature |

The gene review of METTH/mtrA2 (O27134) shows the result: a 183-residue protein
aligned only to the soluble cobamide domain of the operon subunit, with no
counterpart to its C-terminal anchor, is given a transmembrane segment at
residues 102-118 (mean Kyte-Doolittle hydropathy 0.49, with charged residues),
the Na+-coupled reaction and complex membership
(genes/METTH/mtrA2/mtrA2-bioinformatics/RESULTS.md). This is pattern 24 in the
[ARCHAEA error catalogue](ARCHAEA/annotation-patterns.md).

## Scan of all HAMAP rules

[`HAMAP/scan_hamap_rules.py`](HAMAP/scan_hamap_rules.py) parses the HAMAP rule
flat file (Release 2026_04, 2,431 family rules) and records, for each rule, its
duplicate clause, unconditional locations, transmembrane trigger, size range
and subunit statement ([output](HAMAP/hamap_rule_scan.yaml)).

| Rules | Count |
|---|---|
| All family rules | 2,431 |
| With a duplicate clause (paralogs allowed) | 716 |
| With an unconditional membrane location | 231 |
| With a transmembrane trigger | 254 |
| **All three (the MF_01093 shape)** | **18** |
| Duplicate clause and unconditional membrane location, no trigger | 16 |

The shape alone does not make a rule wrong: most of the 18 are multi-pass
transporters and membrane enzymes whose paralogs are membrane proteins too.
[`HAMAP/check_rule_tm_segments.py`](HAMAP/check_rule_tm_segments.py) tests
each member directly. It fetches every UniProtKB entry carrying each of the 18
rules (141,582 rule-assigned transmembrane segments) and computes the mean
hydropathy of each segment whose evidence names the rule. Weak helices in
multi-pass proteins often fall below a 1.0 threshold, so the test that matters
is an entry with **no** rule-assigned segment above it
([summary](HAMAP/rule_tm_summary.yaml); the per-segment table is regenerated
by the script and not committed).

| Rule | Entries | Entries with no hydrophobic segment | Notes |
|---|---|---|---|
| MF_01093 MtrA | 159 | 4 | O27134, D9PXT1 and D3E0P6, three of the soluble homologues (the rule review confirms all three); A6UWH7 (*Methanococcus aeolicus*, 240 residues) is an anchored subunit whose rule-placed segment is slightly off its C-terminal helix |
| MF_01944 LpxM | 4 | 2 | *E. coli* and *Shigella* LpxM (segment 23-43, 0.85). Not an error: the inner-membrane location has experimental support (PMID:9099672), so this is a weakly hydrophobic real anchor and a false positive of the test |
| the other 16 | 24,320 | 0 | |

So among HAMAP rules that allow paralogs and put a transmembrane segment on
every member, MF_01093 is the one whose soluble paralogs receive a membrane
span that is not there. The test sees only proteins that carry a TRANSMEM
feature, so it undercounts: the MF_01093 review finds 22 soluble homologues,
of which only the 3 reviewed ones carry a rule-made segment; the 19
unreviewed ones have no TRANSMEM feature but still receive the cell membrane
location. Plan item 2 extends the check to location-only cases.

## Rule reviews

| Rule | UniRule | Review | Verdict |
|---|---|---|---|
| MF_01093 MtrA | UR000100608 | [rules/unirule/UR000100608](../rules/unirule/UR000100608/UR000100608-review.yaml) | MODIFY: 22 of 219 annotated proteins are soluble homologues that receive the anchored subunit's statements; wrap those in `case <Length>215>` |
| MF_01501 MtrH | UR000038407 | [rules/unirule/UR000038407](../rules/unirule/UR000038407/UR000038407-review.yaml) | MODIFY: conditions sound, activity consequents describe the complex |

MF_01501 is the complex-activity case (pattern 16 in the ARCHAEA catalogue).
Its conditions are sound: all 52 matching UniProtKB entries are MtrH proteins
of methanogens, none with a transmembrane segment, and the rule states no
membrane location. Its activity consequents are the complex's: MtrH catalyses
only the first half-reaction (methyl transfer from methyl-H4MPT to the MtrA
cobamide, PMID:10338124), yet the rule gives it the whole Na+-translocating
reaction (RHEA:53492) and exports GO:0030269, which is_a sodium ion
transmembrane transporter activity, so GO's logical inference adds sodium
transmembrane transport to a soluble subunit. The review proposes exporting
the parent GO:0042086 instead (or GO:0030269 as contributes_to) and asking
Rhea for the half-reaction.

Copying the complex reaction onto every subunit rule is HAMAP's usual
convention for ion-translocating complexes, not a one-off
(`rules/unirule/UR000038407/summary.txt`): all 8 Mtr subunit rules carry
EC 7.2.1.4 and RHEA:53492, as do all 11 NDH-1 subunit rules (EC 7.1.1.-) and
all 6 Na+-NQR subunit rules (EC 7.2.1.1). The bacterial F-type ATP synthase
rules are the exception: only the catalytic alpha and beta rules carry EC
7.1.2.2 and its reaction. That shows the convention can be confined to the
catalytic subunits, and it is the model the MtrH fix follows.

## Plan

1. Rule reviews of MF_01093 and MF_01501: done (both MODIFY).
2. Extend the check to location-only cases: members of the 18 candidate rules
   that carry the rule's membrane location without any TRANSMEM feature (the
   19 unreviewed MtrA homologues), and the 16 weaker candidates (duplicate
   clause and unconditional membrane location without a transmembrane
   trigger). These need an independent transmembrane prediction run on the
   sequences, since there is no rule-made segment to score.
3. Measure the complex-activity convention across all subunit rules: which
   complexes copy the complex EC and reaction onto every subunit (Mtr, NDH-1,
   Na+-NQR) and which confine it (F-type ATP synthase), and what GO terms each
   subunit rule exports as a result.
4. Review HAMAP rules behind annotations the gene reviews reject, starting
   with the UniRule (GO_REF:0000104) rows in `genes/`.

## Reproducing

```bash
curl -O https://ftp.expasy.org/databases/hamap/hamap_rules.dat
uv run python projects/HAMAP/scan_hamap_rules.py hamap_rules.dat > projects/HAMAP/hamap_rule_scan.yaml
uv run python projects/HAMAP/check_rule_tm_segments.py --from-scan projects/HAMAP/hamap_rule_scan.yaml > rule_tm_segments.tsv
uv run python projects/HAMAP/check_rule_tm_segments.py --summarise rule_tm_segments.tsv > projects/HAMAP/rule_tm_summary.yaml
```
