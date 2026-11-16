# aguB (PA0293, Q9I6J8) review notes

N-carbamoylputrescine amidohydrolase (EC 3.5.1.53), 292 aa, nitrilase /
carbon-nitrogen hydrolase superfamily (Pfam CN_hydrolase; NCBIfam TIGR03381
agmatine_aguB; InterPro IPR017755), with the Glu-Lys-Cys catalytic triad
(UniProt ACT_SITE 44, 117, 154). Second enzyme of the agmatine route from
arginine to putrescine (AguA agmatine deiminase, then AguB). Unreviewed
UniProt entry.

## Literature (no deep-research provider available; own reading)

- Haas et al. 1984 (abstract only): agmatine-utilization (agu) mutants;
  aguA and aguB were mapped by cotransduction [PMID:6423933 "The genes encoding
  agmatine deiminase (aguA) and N-carbamoylputrescine amidinohydrolase (aguB)
  were 98% cotransducible"]. This is the PseudoCAP IMP source. The abstract
  names aguB as the gene for the enzyme; the IMP most likely rests on loss of
  the activity in agu mutants, i.e. a lysate assay, which on its own is weaker
  than direct biochemistry.
- Nakada & Itoh 2003 (abstract only): purified AguB, specific for
  N-carbamoylputrescine [PMID:12634339 "AguB was specific to
  N-carbamoylputrescine and the K(m) and K(cat) values of the enzyme for the
  substrate were 0.5 mM and 3.3 s(-1), respectively."]; AguB is a nitrilase-family
  protein [PMID:12634339 "AguB is a protein of the nitrilase family that performs
  thiol-assisted catalysis."]; AguA and AguB act biosynthetically in the ADC
  route [PMID:12634339 "a double mutant of aguAB and speC was a putrescine
  auxotroph."]. This direct biochemistry confirms the term annotated from the
  1984 paper.
- PubMed MCP search returned API errors on 2026-11-05.

## PseudoCAP IBA-seed assessment

Other seeds' experimental support queried live in QuickGO on 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000557706 | GO:0050126 N-carbamoylputrescine amidase activity | 2 | 74 (57 taxa) | GO:0050126, IMP, PMID:6423933 (PseudoCAP) | SOUND | Abstract names aguB as the N-carbamoylputrescine amidohydrolase gene; the activity is independently confirmed with purified AguB (PMID:12634339). | Arabidopsis CPA/NLP1 AT2G27450 (Q8VYF5, IDA PMID:12435743) | Yes; the plant seed has IDA |
| PTN000557638 | GO:0016811 hydrolase activity, acting on C-N (but not peptide) bonds, in linear amides | 10 | 32 (23 taxa) | GO:0050126, IMP, PMID:6423933 (PseudoCAP) | SOUND | GO:0050126 is_a GO:0016811; broad node term suits a nitrilase-superfamily clade. | human, rat, mouse, worm, fly, Dictyostelium, Arabidopsis (x2), Helicobacter seeds | Yes; nine other seeds |

No PSEUDOCAP or GO_CENTRAL defect. The 1984 IMP is a genetics-led basis,
but the term is correct for the gene and is supported by later purified-enzyme
kinetics, so I do not ask for it to be changed. Adding an IDA from
PMID:12634339 would strengthen the seed; that is a curation suggestion, not a
defect.
