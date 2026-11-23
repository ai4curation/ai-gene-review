# cyaB (PA3217, Q9HZ23) review notes

Class IIIb adenylyl cyclase with an N-terminal MASE2 membrane sensor domain (six
predicted TM helices, Phobius) and a C-terminal Guanylate_cyc (CHD) catalytic domain.

## Literature (no deep-research provider available; own reading)

- Wolfgang et al. 2003 (abstract only; no PMC full text): microarray work on the
  TTSS regulon identified a membrane-associated adenylate cyclase signalling
  pathway [PMID:12586068 "led to the identification of a signaling pathway that
  originates from a membrane-associated adenylate cyclase and controls TTSS gene
  expression"]; mutants unable to make cAMP were profiled [PMID:12586068
  "Transcriptome analysis of mutants lacking the ability to synthesize cAMP or
  the cAMP binding protein Vfr"]. This is the PseudoCAP source for the IMP MF and
  BP rows.
- Topal et al. 2012 (full text, PMC3269522): biochemical and structural
  characterisation of CyaB. Purified catalytic domain is active and stimulated by
  CO2/HCO3- [PMID:22226839 "CO2/HCO3− stimulated CyaB217–463 activity in the
  presence of either divalent, with optimal stimulation occurring at pH 7."];
  CyaB makes most cellular cAMP [PMID:22226839 "CyaB activity indeed accounts for
  the majority of intracellular cAMP"]; the MASE2 domain anchors it in the inner
  membrane [PMID:22226839 "Full-length CyaB and CyaBΔ1–17 were detected
  exclusively in the total membrane and inner membrane fractions"]. This gives
  direct evidence for GO:0004016 and a new plasma membrane location row.
- GO:0019933 cAMP-mediated signaling is obsolete, so the IEA intracellular signal
  transduction row is kept as is (non-core).
- PubMed MCP search returned API errors on 2026-11-05.

## PseudoCAP IBA-seed assessment

Seed support queried live in QuickGO on 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002454020 | GO:0004016 adenylate cyclase activity | 12 | 158 (20 taxa) | GO:0004016, IMP, PMID:12586068 (PseudoCAP) | SOUND | Abstract describes cAMP-null mutants and a membrane adenylate cyclase; the activity is confirmed with purified CyaB in PMID:22226839 (full text). MF by IMP is weaker than IDA but correct. | M. tuberculosis Rv1264, Rv1318c, Rv1319c, Rv1647 (IDA), T. brucei receptor ACs (6, IDA PMID:11166383), Dictyostelium AcrA (IDA) | Yes; eleven IDA seeds |
| PTN002454020 | GO:0006171 cAMP biosynthetic process | 4 | 158 (20 taxa) | GO:0006171, IMP, PMID:12586068 (PseudoCAP) | SOUND | Loss of cAMP synthesis in the mutant; CyaB makes most cellular cAMP (PMID:22226839). | Rv1318c, Rv1319c, Rv1647 (IDA) | Yes; three IDA seeds |

No PSEUDOCAP or GO_CENTRAL defect. The node is a class III AC clade; both terms suit it.
