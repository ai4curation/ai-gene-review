# actC (Q93P57): is the act operon's two-taxon-id annotation a cross-isolate transfer?

Script: `check_act_entries.py` (standard library only; uses `curl` so the
container's HTTPS proxy applies). Run on 2026-11-01:
`python3 -I check_act_entries.py`. Raw output in `run.log`.

## Why this was checked

The CACAO annotations citing PMID:11359579 are spread over two NCBI taxon ids,
`NCBITaxon:34` (*Myxococcus xanthus*) and `NCBITaxon:246197` (*M. xanthus*
strain DK1622). A screen of the CACAO corpus flagged that pattern as a possible
cross-isolate experimental transfer. The competing explanation is that the two
ids denote one organism, because DK1622 is both the standard laboratory strain
and the reference genome. This check distinguishes the two by comparing the
sequences themselves.

## Result 1: one organism, one set of loci — not two isolates

Every act gene is represented twice in UniProtKB: once from GenBank AF350253,
the authors' own submission with PMID:11359579, filed at the species-level
taxon 34; and once from the DK1622 genome (CP000113) at taxon 246197.

| gene | taxon 34 | DK1622 | len 34 | len DK | identical | aa diffs | shared RefSeq |
|---|---|---|---|---|---|---|---|
| actA | Q93P59 | Q1D7F9 | 342 | 342 | no | 2 | no |
| actB | Q93P58 | Q1D7F8 | 553 | 553 | **yes** | 0 | yes |
| actC | Q93P57 | Q1D7F7 | 437 | 437 | **yes** | 0 | yes |
| actD | Q93P56 | not in UniProtKB | — | — | — | — | — |
| actE | Q93P55 | not in UniProtKB | — | — | — | — | — |

actB and actC are byte-identical between the two taxon ids and share a RefSeq
protein accession. actA differs at two residues out of 342 (D90A, T109S) — the
scale of discrepancy expected between a 2001 PCR-derived submission and a 2006
whole-genome assembly of the same strain, not between two isolates. The DK1622
entries for actD and actE were sought by the ordered locus names the literature
gives (MXAN3216 for actD, per PMID:17189369) and are not in UniProtKB; that is a
gap in this check, not evidence either way.

**Conclusion: the two taxon ids are two UniProtKB representations of the same
DK1622 loci. No cross-isolate transfer is possible here.**

## Result 2: the experimental annotations sit on the non-proteome entry

The actC pair as served on 2026-11-01:

| | Q93P57 (taxon 34) | Q1D7F7 (taxon 246197) |
|---|---|---|
| gene names | `actC` | `MXAN_3215` only — no `GN Name` |
| length / sequence md5 | 437 / `35f6afd6eb648ed125515102dc4ef8c1` | 437 / `35f6afd6eb648ed125515102dc4ef8c1` |
| RefSeq | `WP_011553262.1` | `WP_011553262.1` |
| reference proteome | none | `UP000002402` |
| `DR GO` lines | 6 | 3 |

Q93P57 carries all three CACAO experimental rows (`GO:0031155`, `GO:0009966`,
`GO:0043937`, each IMP) plus three IEA rows. Q1D7F7 — the ActC that is in the
DK1622 reference proteome, and so the one reached through STRING, KEGG and
EnsemblBacteria — carries only the three IEA rows (`GO:0005737`, `GO:0016747`,
`GO:0004029`) and none of the experimental ones.

The split runs through the operon: the actA and actC rows are on the taxon-34
entries, the actB rows on the DK1622 entry. The gene-name column explains it
without any appeal to curator error — `actB` is a `GN Name` only on the DK1622
side, `actC` only on the taxon-34 side — so a curator searching by gene symbol
is routed to a different entry for each gene of one operon.

## Result 3: GO:0004029 is propagated from one PANTHER node to ~1,300 proteins

QuickGO served `numberOfHits: 2648` for `withFrom=PANTHER:PTN005180820`, the
ancestral node behind Q93P57's TreeGrafter rows. Every annotation in the first
page of 200 was either `GO:0004029` (100) or `GO:0005737` (100), i.e. the node
emits exactly that pair, so ~1,324 proteins receive the aldehyde
dehydrogenase (NAD+) assertion from it.

This is context for the `GO:0004029` row, not proof it is wrong; the argument
against it is the fold. NAD+-dependent aldehyde dehydrogenases (EC 1.2.1.3) are
the ALDH superfamily (Pfam PF00171, SUPFAM SSF53720), and Q93P57 matches none of
those signatures — its NAD(P)-binding domain is the Rossmann-like
Gene3D 3.40.50.720 / SUPFAM SSF51735 fold, and its only other domain is GNAT.

## Limitations

- Everything here is database comparison. No activity was predicted or measured,
  and nothing in this analysis bears on whether ActC has any catalytic function.
- Sequence identity establishes that two records describe the same protein; it
  does not by itself establish a shared genomic locus. The shared RefSeq protein
  accession and the locus names in PMID:17189369 are what tie these to one locus.
- API results are live and dated above; re-running on another day may give
  different annotation counts.
