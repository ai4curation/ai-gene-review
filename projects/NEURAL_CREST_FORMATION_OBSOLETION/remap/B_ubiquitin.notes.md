# Group B: CUL3 ubiquitin / ribosome-biogenesis group: remap notes

Input: `B_ubiquitin.input.tsv` (7 rows, all UniProt IMP, `involved_in` GO:0014029).
Output: `B_ubiquitin.tsv`. Checker: 7 rows, 0 errors (2026-10-09).

| Gene | Paper | Source | Decision |
|---|---|---|---|
| KBTBD8 (human) | PMID:26399832 | FULL_TEXT | REPLACE → GO:0014036 |
| kbtbd8 (X. tropicalis) | PMID:26399832 | FULL_TEXT | REPLACE → GO:0014036 |
| TCOF1 (human) | PMID:26399832 | FULL_TEXT | REPLACE → GO:0014036 |
| NOLC1 (human) | PMID:26399832 | FULL_TEXT | REPLACE → GO:0014036 |
| KLHL12 (human) | PMID:27716508 | ABSTRACT | UNDECIDED (candidate GO:0014036) |
| PEF1 (human) | PMID:27716508 | ABSTRACT | UNDECIDED (candidate GO:0014036) |
| PDCD6 / ALG2 (human) | PMID:27716508 | ABSTRACT | UNDECIDED (candidate GO:0014036) |

## PMID:26399832 (Werner et al. 2015, Nature): full text cached (PMC4602398)

**Systems.** The work is in human ESCs (H1/H9) taken through embryoid-body
differentiation and dual-SMAD "neural conversion", plus *Xenopus tropicalis*
embryos. In the frogs, a morpholino or dominant-negative CUL3 was injected into
one blastomere at the 2-cell stage, and SOX10 in situ hybridisation was read at
stage 16–18. Only KBTBD8 and CUL3 were manipulated in Xenopus. TCOF1 and NOLC1
were tested only in hESCs.

**Phenotype.** Cells lose neural crest (SOX10, SNAIL2, AP2, p75, HNK1) and gain
CNS precursors (PAX6). Pluripotency, cell cycle and survival are unaffected. The
defect appears when crest markers first appear: "KBTBD8 was required for early
neural crest specification, with CNS precursor markers accumulating in
KBTBD8-depleted cells when neural crest markers were first detected in control
experiments". This is a fate choice between crest and CNS. It is not
border-territory formation and not EMT, delamination or migration, so
GO:0014036 *neural crest cell fate specification* is the right level. The
progenitor-maintenance NTR does not fit, because the cells do not stay
undifferentiated: they switch to CNS fate.

**KBTBD8 (human, Q8NFY9; X. tropicalis, A0A1B8YAB1).** KBTBD8 is the CUL3
substrate adaptor. Knockdown is rescued by shRNA-resistant KBTBD8. The
CUL3-binding mutant (Y74A) and the substrate-binding mutant (W579A) fail to
support specification, so the adaptor's catalytic role is required. In Xenopus:
"Also in Xenopus tropicalis, downregulation or inhibition of CUL3KBTBD8
prevented neural crest formation and caused an expansion of the CNS precursor
territory". The adaptor carries out the ubiquitylation step that drives the
fate choice, so it does part of the work.

Alternative considered: GO:1905297 *positive regulation of neural crest cell
fate specification*. I rejected it. KBTBD8 does not tune a specification process
that other factors carry out. Its translational control is the mechanism by
which the CNS-versus-crest choice is enforced: it suppresses translation of CNS
precursor proteins such as ATRX and PCM1 "until neural crest specification had
occurred". A GO editor could reasonably prefer the regulation term, and I flag
this as the main judgement call.

**TCOF1 (Q13428) and NOLC1 (Q14978).** These are the ubiquitylation substrates.
Under the CLAUDE.md participation test they fall in the *scaffold* case, not the
angiotensinogen case. Monoubiquitylated TCOF1 recruits NOLC1, and together they
form a platform that "connect[s] RNA polymerase I with" the H/ACA
pseudouridylation enzymes and the SSU processome. That platform is the effector
that remodels translation. Depleting either protein phenocopies loss of KBTBD8,
and co-depletion is epistatic ("act in a common pathway"). At the time of
specification, TCOF1 loss does not affect rRNA synthesis, p53 or survival, so
the phenotype is not a nonspecific ribosome-biogenesis or cell-death effect
(that effect appears only later). The substrates therefore contribute
structurally to the step, and GO:0014036 applies to them too. Both rows are
human hESC IMP only.

## PMID:27716508 (McGourty et al. 2016, Cell): abstract only

There is no PMC record (checked with PubMed ID conversion), and the publisher
page returned 403. The abstract says CUL3 "is an essential regulator of neural
crest specification", and that KLHL12 with the PEF1–ALG2 (PDCD6) calcium
co-adaptor monoubiquitylates SEC31, which drives large COPII coats and collagen
secretion. It does not describe the neural crest experiments, which are
presumably hESC neural conversion as in the companion paper.

UniProt's full-text curation of PEF1 (Q9UBV8) and PDCD6 (O75340) states that
SEC31 monoubiquitination and collagen export are "required for neural crest
specification". KLHL12 (Q53G59) says that "BCR(KLHL12) complex is also involved
in neural crest specification". So the curator's intent maps to GO:0014036.

I marked these rows UNDECIDED rather than REPLACE for two reasons:

1. I cannot see the experiments: the species/system, the readout, or whether
   rescue or epistasis was shown.
2. The participation test is genuinely open. The molecular activity is
   collagen/COPII secretion. Whether that does part of the work of crest fate
   specification, or is an upstream requirement (which would argue for
   GO:1905297, or for no crest term at all with the secretion process kept
   instead), depends on the full-text data.

Per CLAUDE.md, an experimental row is not removed without the full text.
Candidate replacement: GO:0014036, with GO:1905297 as the alternative. The
candidate ids are given only in the rationale column, not in `replacement_ids`.

## Verification

- GO term labels were checked live on QuickGO by `check_remap.py` (GO:0014036
  "neural crest cell fate specification").
- All quotes are verbatim from `publications/PMID_26399832.md` (full text) or
  `publications/PMID_27716508.md` (abstract; fetched this session with
  `just fetch-pmid 27716508`).
