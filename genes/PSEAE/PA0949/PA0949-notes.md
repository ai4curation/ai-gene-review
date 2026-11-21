# PA0949 (Q9I509) review notes

WrbA-family flavodoxin-like NAD(P)H:quinone oxidoreductase of P. aeruginosa PAO1.
No gene name in UniProt; folder and gene_symbol use the locus tag.

## Literature (no deep-research provider available; own reading)

- Green et al. 2014 (abstract only, no PMC): five P. aeruginosa quinone
  reductases, including WrbA, purified and assayed. [PMID:25085734 "In in vitro
  assays, each enzyme was shown to reduce quinone substrates with only minimal
  semiquinone formation."] Over-expression gave no H2O2 protection in wild type
  [PMID:25085734 "However, when each was individually over-expressed in P.
  aeruginosa no overt H2O2-protective phenotype was observed."], only in a katA
  mutant or in P. putida.
- Patridge & Ferry 2006 (full text, PMC1482846): E. coli and A. fulgidus WrbA are
  NQOs; WrbA family = type IV NQO. P. aeruginosa appears only as a solved
  structure [PMID:16672604 "The presence of this fold has recently been confirmed
  in the published crystal structures of the Deinococcus radiodurans and
  Pseudomonas aeruginosa WrbA homologues"]. The PseudoCAP IDA of GO:0016655 to
  PA0949 citing this paper is therefore a wrong-reference row (CONFIRMED).
- Gorman & Shapiro 2005 (full text, PMC2253248): crystal structures of P.
  aeruginosa WrbA with FMN, homotetramer [PMID:16322580 "each WrbA protein forms a
  homotetramer with 222 symmetry, unique among flavodoxin-like proteins, in which
  each protomer binds one flavin mononucleotide cofactor molecule."].
- PubMed MCP search returned API errors on 2026-11-05; PMC id conversion showed no
  full text for PMID:25085734.

## PseudoCAP IBA-seed assessment

Seed support queried live in QuickGO on 2026-11-05 (seed MOD ids mapped to UniProt).

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000777387 | GO:0003955 NAD(P)H dehydrogenase (quinone) activity | 4 | 363 (76 taxa) | GO:0003955, IMP, PMID:25085734 (PseudoCAP) | SOUND | Abstract states the purified PA enzyme reduces quinones in vitro; the term is right, the code would better be IDA. | E. coli WrbA P0A8G6 (IDA/IMP PMID:16672604), yeast PST2 Q12335 (IDA PMID:28499769), Arabidopsis FQR1 Q9LSQ5 (IDA PMID:11842161) | Yes; three independent IDA seeds across bacteria, fungi and plants |

No PSEUDOCAP or GO_CENTRAL defect for the seeding row. Node term suits the WrbA clade.

Other findings on this gene:

- GO:0016655 IDA (PseudoCAP, PMID:16672604): wrong reference, PSEUDOCAP defect
  recorded (CONFIRMED, full text read). This row does not seed an IBD.
- GO:0016020 membrane IBA at the same node: seeded only by fungal Pst/Ycp4/Rfs1
  proteins (PM / membrane raft). Marked over-annotated for PA0949; no defect filed
  (PA0949 is not a seed for it), raised as a question.
- GO:0034599 IMP: over-expression in a katA mutant only; marked over-annotated.
