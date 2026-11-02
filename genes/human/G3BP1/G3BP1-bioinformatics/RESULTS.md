# Does human G3BP1 have the sequence features of an ATP-dependent helicase?

## Question

UniProt Q13283 carries `EC=3.6.4.12` and `EC=3.6.4.13` and the alternate name
"ATP-dependent DNA helicase VIII", all on the evidence of a single 1999 report
(PMID:9889278) that purified a helicase activity from HeLa nuclear extract and
identified the band by microsequencing as G3BP. GOA propagates that report into
four molecular-function rows: `GO:0003678` DNA helicase activity, `GO:0003724`
RNA helicase activity, `GO:0033677` DNA/RNA helicase activity and `GO:0016887`
ATP hydrolysis activity.

Every characterised ATP-dependent helicase, in all six superfamilies, is built
on a RecA-like nucleotide-binding core whose Walker A (P-loop, `GxxxxGK[ST]`)
and Walker B motifs are required for ATP binding and hydrolysis; in superfamily 2
the Walker B motif is the DExD/H box. This analysis asks whether G3BP1 has such a
core, using positive and negative controls to show that the test discriminates.

## Method

`reproduce.py` fetches UniProtKB records live from the REST API (no key needed,
cached under `cache/`) and, for each protein, computes from the downloaded record:

- regular-expression hits for six canonical motifs — Walker A/P-loop, Walker B,
  DExD/H box, SF2 motif VI (`QxxGRxGR`) arginine finger, SF2 motif III (SAT) and
  the SF1/SF2 Q motif;
- whether any InterPro, Pfam, PROSITE, CDD, SMART, SUPFAM or Gene3D signature on
  the entry names a helicase or RecA/AAA/P-loop ATPase core;
- the entry's annotated domains and any nucleotide-binding or binding-site features.

Controls:

- **Positive** (known ATP-dependent helicases): DDX3X and EIF4A3 (DEAD-box, SF2),
  BLM (RecQ, SF2), UPF1 (SF1).
- **Negative, fold-matched to G3BP1**: NUTF2 (an NTF2-domain protein, matching
  G3BP1's residues 11–133) and HNRNPA1 (an RRM + RGG protein, matching G3BP1's
  residues 340–466). These are the two folds G3BP1 is actually made of, so they
  test whether G3BP1's architecture could score positive by accident.

## Results

| Protein | Length | Helicase/ATPase signature | Core nt motifs (of 3) | Annotated domains |
|---|---|---|---|---|
| **G3BP1** (Q13283) | 466 | **no** | **0** | NTF2, RRM |
| DDX3X (O00571) | 662 | yes (15 signatures) | 1 | Helicase ATP-binding, Helicase C-terminal |
| EIF4A3 (P60842) | 406 | yes (16) | 2 | Helicase ATP-binding, Helicase C-terminal |
| BLM (P54132) | 1417 | yes (17) | 1 | HRDC, Helicase ATP-binding, Helicase C-terminal |
| UPF1 (Q92900) | 1129 | yes (8) | 1 | UPF1-type SF1B helicase ATP-binding / C-terminal |
| NUTF2 (P61970) | 127 | no | 0 | NTF2 |
| HNRNPA1 (P09651) | 372 | no | 0 | RRM 1, RRM 2 |

`controls_behave_as_expected: true` — all four positive controls are flagged, and
neither fold-matched negative control is.

For G3BP1 specifically (sequence version 1, 466 aa):

- **All six motif searches return zero hits.** No Walker A/P-loop, no Walker B, no
  DExD/H box, no motif VI arginine finger, no motif III, no Q motif.
- **None of the entry's 19 domain/family signatures** names a helicase or a
  RecA/AAA/P-loop ATPase; they describe the NTF2-like fold, the G3BP1-specific RRM
  (`IPR034374`) and the nucleotide-binding α/β-plait superfamily fold of the RRM.
- **No nucleotide-binding or ATP binding-site feature** is annotated on the entry.
- The annotated architecture (NTF2 11–133, acidic disordered region 142–225,
  further disordered segments to 329, RRM 340–415, RG-rich 410–466) accounts for
  the whole protein, leaving no unassigned region that could host the two
  RecA-like lobes an ATP-dependent helicase requires (each is ~200 residues).

## Interpretation

G3BP1 has none of the sequence features that ATP-dependent helicase activity
requires, and the test that finds them in four bona fide helicases finds nothing in
G3BP1 or in either of the two folds G3BP1 is composed of. The 23 PDB structures of
the Q13283 NTF2 domain show a dimerisation module, not a nucleotide-binding lobe.

The 1999 observation is therefore best explained by a co-purifying activity in the
HeLa nuclear extract rather than by G3BP1 itself: microsequencing identifies which
protein is in the band, not which protein carries the activity, and the result has
not been independently reproduced in the 27 years since. The InterPro note that the
RRM belongs to the "nucleotide-binding α/β-plait" structural superfamily refers to
fold ancestry and to single-stranded nucleic-acid binding, not to ATP hydrolysis.

## Part 2: where in the PANTHER family do the helicase annotations sit?

The three helicase IBA rows on Q13283 descend from PANTHER node `PTN002581351`. An
IBA asserts that a function was present at a node and inherited by its descendants,
so the question that bears on it is what descendant evidence the node rests on.
`reproduce.py` therefore also queries QuickGO for every one of the 11 reviewed
members of `PTHR10693` and records which helicase terms each carries, under which
evidence codes.

| Accession | Gene | Subfamily | Organism | Helicase rows | With experimental evidence |
|---|---|---|---|---|---|
| Q13283 | G3BP1 | SF21 | human | 12 | **GO:0003678, GO:0003724, GO:0033677, GO:0016887** |
| P97855 | G3bp1 | SF21 | mouse | 12 | none |
| Q32LC7 | G3BP1 | SF21 | cattle | 7 | none |
| Q5RB87 | G3BP1 | SF21 | orangutan | 5 | none |
| Q9UN86 | G3BP2 | SF10 | human | 0 | none |
| P97379 | G3bp2 | SF10 | mouse | 0 | none |
| Q5R9L3 | G3BP2 | SF10 | orangutan | 0 | none |
| O94260 | nxt3 | SF20 | *S. pombe* | 0 | none |
| P53741 | BRE5 | SF20 | *S. cerevisiae* | 0 | none |
| Q21351 | gtbp-1 | SF20 | *C. elegans* | 0 | none |
| Q9FME2 | NTF2 | SF75 | *A. thaliana* | 0 | none |

Two results, both computed rather than asserted
(`subfamilies_with_any_helicase_row`, `members_with_experimental_helicase_evidence`
in `results.json`):

- **Helicase rows occur in exactly one subfamily, SF21** — the G3BP1 orthologs. The
  paralogous SF10 subfamily (G3BP2, in all three species that have a reviewed entry)
  has none, as do the fungal, nematode and plant members.
- **Q13283 is the only member of the family, in any species, with experimental
  evidence for any helicase term.** Every helicase row on mouse, cattle and
  orangutan G3BP1 carries ISO, ISS, IBA, IEA or RCA — i.e. they are all propagated,
  and the human 1999 result is the sole experimental seed for the entire family.

Experimental codes counted here are IDA, IMP, IGI, IPI, EXP and HDA
(`ECO:0000314`, `ECO:0000315`, `ECO:0000316`, `ECO:0000353`, `ECO:0000269`,
`ECO:0006056`).

This is what makes the IBA assessable rather than merely doubtful. The node's only
descendant grounding is the target's own annotation — which is legitimate in general,
and is *not* circularity — but it means the inheritance claim carries no independent
support beyond the paper Part 1 argues against. That the closest paralog never
acquired the annotation, in any species, is a further sign that the claim entered the
family through one report rather than through comparative biology.

## Scope and limits

- This is a sequence- and annotation-level argument. It cannot exclude a
  non-canonical ATPase site of a kind never described, and it is not a substitute
  for a direct enzymatic assay on recombinant G3BP1.
- Motif regular expressions are necessarily approximate; the controls are included
  precisely so that the test's discriminating power is visible rather than assumed.
  Note that the positive controls score 1–2 of 3 core motifs, not 3 of 3 — the
  signature-level evidence is the stronger half of the test.
- All numbers above are computed by `reproduce.py` from the fetched records and
  written to `results.json`; none are hardcoded.

## Reproduce

```bash
cd genes/human/G3BP1/G3BP1-bioinformatics
python3 reproduce.py        # writes results.json
```
