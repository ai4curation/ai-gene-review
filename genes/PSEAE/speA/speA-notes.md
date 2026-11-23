# speA (PA4839, Q9HUX1) review notes

Biosynthetic arginine decarboxylase (ADC, EC 4.1.1.19), 636 aa, PLP- and
Mg2+-dependent, Orn/Lys/Arg decarboxylase class-II family, SpeA subfamily
(HAMAP MF_01417; NCBIfam TIGR01273; PANTHER PTHR43295). Converts L-arginine to
agmatine; agmatine is then converted to putrescine by AguA (agmatine deiminase)
and AguB (N-carbamoylputrescine amidohydrolase).

## Literature (no deep-research provider available; own reading)

- Nakada & Itoh 2003 (abstract only; no PMC full text): identified speA and
  speC in PAO1 [PMID:12634339 "The authors identified the speA and speC genes in
  Pseudomonas aeruginosa PAO1."]; ADC and ODC activities were similar and each
  sufficed for growth [PMID:12634339 "The activities of the two decarboxylases
  were similar and each enzyme alone appeared to direct sufficient formation of
  the polyamine for normal growth."]; the speA speC double mutant was a
  putrescine auxotroph [PMID:12634339 "A mutant defective in both speA and speC
  was a putrescine auxotroph."]. The IMP for ADC activity most likely reflects
  loss of ADC activity in the speA mutant; with the HAMAP SpeA assignment this
  is sound.
- Haas et al. 1984 showed that arginine is degraded by an arginine
  decarboxylase (agmatine) pathway in P. aeruginosa (aguA, aguB mutants)
  [PMID:6423933], but I could not establish from the abstracts whether the
  catabolic route uses SpeA itself. The InterPro2GO L-arginine catabolic process
  row is therefore left UNDECIDED.
- PubMed MCP search returned API errors on 2026-11-05.

## PseudoCAP IBA-seed assessment

Other seeds' experimental support queried live in QuickGO on 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN008680444 | GO:0008792 arginine decarboxylase activity | 4 | 103 (55 taxa) | GO:0008792, IMP, PMID:12634339 (PseudoCAP and CACAO) | SOUND | Abstract states speA encodes ADC, with activity comparable to ODC and putrescine auxotrophy of the speA speC mutant; HAMAP SpeA subfamily agrees. | E. coli SpeA P21170 (EXP/IDA, e.g. PMID:2198270, PMID:8088419), Arabidopsis ADC1 AT2G16500 and ADC2 AT4G34710 | Yes; E. coli SpeA alone has several IDA/EXP rows |

No PSEUDOCAP or GO_CENTRAL defect. The node lies in PTHR43295 (arginine
decarboxylase), not in the ODC family node PTN000159726; the AZIN1
MISSING_NEGATION defect recorded in genes/PSEAE/speC does not concern this node.
