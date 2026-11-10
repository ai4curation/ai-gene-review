# UR000100608 / HAMAP MF_01093 (MtrA): which proteins does it annotate?

Script: `classify_rule_matches.py`
(`python3 rules/unirule/UR000100608/classify_rule_matches.py > rules/unirule/UR000100608/rule_matches.tsv 2> rules/unirule/UR000100608/summary.txt`,
standard library plus `requests`). It fetches entries live from the UniProt REST API, so
counts can change between releases. Output from the 2026-11-10 run: `rule_matches.tsv`
(one row per entry) and `summary.txt`.

## Queries

- `source:MF_01093` returns the entries whose annotations cite the rule as evidence
  (`ECO:0000255|HAMAP-Rule:MF_01093`): 219 entries.
- `xref:hamap-MF_01093` returns the entries matching the HAMAP family signature: 221.
  The two signature matches without rule annotation, A0A1G9CIW5 and A0ABT4INZ3, are
  both flagged as fragments, which the rule's negative fragment condition excludes.

## Classification

Each rule-annotated entry was classified from its own sequence:

- ANCHORED: length >= 215 and a C-terminal hydrophobic segment (maximum Kyte-Doolittle
  mean over a 19-residue window >= 1.6 within the last 60 residues).
- SOLUBLE: length < 215 and no such segment. The 215-residue cutoff is the one
  Wagner et al. used to separate the cytoplasmic MtrA homologues (PMID:27324530).
- AMBIGUOUS: the two criteria disagree.

| Class | Entries | Reviewed | Length range | C-terminal max KD | Taxonomic classes |
|---|---|---|---|---|---|
| ANCHORED | 197 | 17 | 237-264 | 1.93 or more | Methanomicrobia 136, Methanobacteria 36, Methanococci 24, Methanopyri 1 |
| SOLUBLE | 22 | 3 | 167-204 | 0.72 or less | Methanobacteria 22 |
| AMBIGUOUS | 0 | | | | |

The two classes do not overlap on either criterion: no rule-annotated entry is between
205 and 236 residues long, and no C-terminal score falls between 0.72 and 1.93. Length
histogram (10-aa bins): 160:1, 180:16, 190:4, 200:1, 230:26, 240:153, 250:15, 260:3.

Every one of the 22 soluble entries comes from an organism that also has an anchored
entry annotated by this rule, so each is an extra copy beside the operon subunit.

## Which rule statements the soluble homologues receive

| Statement | ANCHORED (n=197) | SOLUBLE (n=22) |
|---|---|---|
| SUBCELLULAR LOCATION Cell membrane | 197 | 22 |
| EC 7.2.1.4 | 197 | 22 |
| SUBUNIT "composed of 8 subunits" | 197 | 22 |
| FUNCTION "sodium-ion translocating" | 197 | 22 |
| PATHWAY methanogenesis | 197 | 22 |
| COFACTOR cobamide | 197 | 22 |
| BINDING site cobamide | 197 | 22 |
| keyword Cell membrane | 197 | 22 |
| keyword Transmembrane | 197 | 22 |
| keyword Translocase | 197 | 22 |
| keyword Methanogenesis | 197 | 22 |
| GO:0005886 plasma membrane | 197 | 22 |
| GO:0030269 tetrahydromethanopterin S-methyltransferase activity | 197 | 22 |
| GO:0006730 one-carbon metabolic process | 197 | 22 |
| GO:0019386 methanogenesis, from carbon dioxide | 197 | 22 |
| any TRANSMEM feature | 197 | 3 |
| TRANSMEM outside the last 60 residues | 0 | 3 |

All 22 soluble homologues carry the cell membrane location, EC 7.2.1.4, the
eight-subunit complex statement and the four GO terms. The GO columns record the
presence of the term in the entry and not its source; in the reviewed paralog O27134
these rows come from the rule's subcellular location, EC/Rhea, pathway and keyword
consequents (`genes/METTH/mtrA2/mtrA2-goa.tsv`).

In the anchored entries every TRANSMEM lies at the C-terminus (for example 219-237 in
O27227, 221-241 in Q58261). The three soluble entries with a TRANSMEM are the three
reviewed ones, and in each the helix the rule's TM trigger placed is inside the
soluble cobamide domain: O27134 102-118, D9PXT1 22-38, D3E0P6 39-58. The 19 unreviewed
soluble entries have no TRANSMEM but still carry "Cell membrane".

## The three reviewed soluble homologues are the rule's Duplicate species

The rule's `Duplicate: in METRM, METTH, METTM` clause covers exactly the three species
whose reviewed entries come in pairs:

| Species | Anchored (operon) | Soluble homologue |
|---|---|---|
| METTH, M. thermautotrophicus Delta H | O27227 (238 aa) | O27134 (183 aa) |
| METTM, M. marburgensis Marburg | P80184 (238 aa) | D9PXT1 (185 aa) |
| METRM, M. ruminantium M1 | D3E045 (245 aa) | D3E0P6 (193 aa) |

So the Duplicate clause and the lower Size bound of 183 were set to admit the soluble
paralogs, but the rule body has no case that withholds the membrane, complex and
catalytic statements from them.

## Proposed fix

HAMAP already supports length-conditional cases (MF_04119 uses `case <Length>370>`).
Wrap the membrane, topology and Mtr-complex statements of MF_01093 in a length case,
for example `case <Length>215>` (any cutoff from 205 to 236 gives the same split today):
SUBCELLULAR LOCATION, SUBUNIT, FUNCTION, CATALYTIC ACTIVITY and the EC number in DE,
PATHWAY, the `General; Transmembrane` and `ADD_TOPO_DOMAIN` triggers, the keywords Cell
membrane, Membrane, Transmembrane, Transmembrane helix and Translocase, and the GO lines
GO:0030269, GO:0019386 and GO:0005886. In the else branch keep only what the soluble
cobamide domain supports: a family name (for example "MtrA-like cytoplasmic corrinoid
protein"), SIMILARITY, the cobamide COFACTOR and the His BINDING site. A separate HAMAP
family for the cytoplasmic homologues would do the same job.

## Caveats

- Hydropathy is a screen, not a topology predictor; the classification rests on
  hydropathy and length agreeing, which they do for every entry.
- The 22 soluble entries are all Methanobacteria. Wagner et al. also mention extra
  copies in Methanosarcina barkeri; none of these is annotated by this rule as a
  short entry in this release.
