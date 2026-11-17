# speC (PA4519, Q9HVQ3) review notes

Ornithine decarboxylase (ODC, EC 4.1.1.17) of the fold-type III (Orn/Lys/Arg
decarboxylase class-II, Pfam Orn_Arg_deC_N, PROSITE ODR_DC_2) family, 387 aa. This is
the eukaryote-like ODC fold, not the large fold-type I SpeC of E. coli.

## Literature (no deep-research provider available; own reading)

- Nakada & Itoh 2003 (abstract only; no PMC full text): identified speA (ADC) and
  speC (ODC) in PAO1 [PMID:12634339 "The authors identified the speA and speC
  genes in Pseudomonas aeruginosa PAO1."]; the two decarboxylase activities were
  similar and each sufficed for growth [PMID:12634339 "The activities of the two
  decarboxylases were similar and each enzyme alone appeared to direct
  sufficient formation of the polyamine for normal growth."]; the speA speC
  double mutant was a putrescine auxotroph [PMID:12634339 "A mutant defective in
  both speA and speC was a putrescine auxotroph."]. The PseudoCAP IMP for ODC
  activity most likely reflects loss of ODC activity in the speC mutant; with the
  fold-type III ODC signatures this is sound.
- PubMed MCP search returned API errors on 2026-11-05.

## PseudoCAP IBA-seed assessment

Seed support queried live in QuickGO on 2026-11-05 (MOD ids mapped to UniProt;
the WB and MGI ids did not map automatically but are C. elegans odc-1 and mouse
Odc1).

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000159726 | GO:0004586 ornithine decarboxylase activity | 8 | 234 (101 taxa) | GO:0004586, IMP, PMID:12634339 (PseudoCAP) | SOUND | Abstract states speC encodes ODC, ODC activity comparable to ADC, and putrescine auxotrophy with speA; fold-type III ODC signatures agree. | human ODC1 P11926 (EXP/IDA), yeast SPE1 P08432 (EXP/IDA), Candida SPE1 P78599 (IGI), P. falciparum Q8IJ77 (IDA), rat Odc1 P09057 (IDA), mouse Odc1, C. elegans odc-1 | Yes; several IDA/EXP seeds |

No PSEUDOCAP defect. The IBD stands without the speC seed.

### Node-level problem: antizyme inhibitor 1 inherits ODC activity

The node includes the antizyme inhibitors (AZIN1, AZIN2), which are catalytically
inactive ODC paralogs. The AZIN2 branch carries a NOT at PTN000159772, but the AZIN1
branch does not. Live QuickGO query (2026-11-05) for human AZIN1 O14977 and GO:0004586
returned: "UniProtKB:O14977 AZIN1 enables GO:0004586 IBA GO_REF:0000033" with
WITH/FROM PTN000159726, while AZIN2 Q96A70 has "NOT|enables GO:0004586 IBA". The
PANTHER leaf file (.cache/paint/leaf.gaf.gz) likewise propagates GO:0004586 to
chicken AZIN1 A0A1D5PIE4 from PTN000159726. UniProt's curated function text for
O14977 reads: "AZI is an enzymatically inactive ODC homolog that counteracts the
negative effect of ODC antizymes". A GO_CENTRAL defect (MISSING_NEGATION on the AZIN1
subclade) is recorded on the speC ODC IBA row. It does not affect speC itself, whose
IBA is correct.

## 2026-11-13 merge of the bacterial_putrescine_biosynthesis review (PR #6233)

Deep research: no provider run (no API keys in this session); the review was built
from the UniProt record and the cached publication.

- speC encodes the ODC of the direct ornithine route; ODC and ADC activities are
  similar and either suffices for growth; the double mutant is a putrescine auxotroph.
  [PMID:12634339 "A mutant defective in both speA and speC was a putrescine auxotroph."]
- The UniProt entry is unreviewed (PE 3); its name is submitter-imported and its
  pathway/similarity lines are ARBA, so only family signatures (InterPro IPR002433,
  PRINTS ORNDCRBXLASE, CDD PLPDE_III_ODC, PTHR11482:SF6) are cited.
- Q9HVQ3 is itself a PAINT seed for PTN000159726 (ODC activity), from the IMP row.
- Reconciled with the PseudoCAP review above: every row verdict agreed; that review's
  description, AZIN1 source defect and reference adjudication were kept, and the
  family-signature quotes from this review were added as support on the rows that
  had none.
