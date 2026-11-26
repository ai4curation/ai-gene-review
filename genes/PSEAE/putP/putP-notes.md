# putP (PA0783, Q9I5F5) review notes

Sodium/proline symporter, solute:sodium symporter family (TC 2.A.21.2.3;
NCBIfam TIGR02121 Na_Pro_sym; PANTHER PTHR48086). Unreviewed UniProt entry.
Multi-pass inner-membrane protein. Operon putA-putP, induced by proline via
the AraC/XylS activator PruR.

## Literature (no deep-research provider available; own reading)

- Nakada et al. 2002 (full text read). putA and putP form an operon; PruR
  activates it in response to proline. A putP::ΩSp/Sm knockout grows poorly on
  proline [PMID:12270821 "In contrast, the growth of strain PAO4503 ( putP
  ::ΩSp/Sm) on proline was significantly handicapped (Fig. 4 )."], and the
  authors conclude PutP is the major proline transporter [PMID:12270821 "PutP
  PAO is the major proline transporter for proline utilization in strain
  PAO1, as it is in enteric bacteria"]. PutP is 77% identical to E. coli PutP
  [PMID:12270821 "PutP PAO is highly homologous to the PutP proteins of P.
  fluorescens (84% identity), P. putida (80% identity), and E. coli (77%
  identity)."]. No direct uptake assay is reported in this paper.
- No other PAO1 PutP functional papers found. The function rests on this
  genetics plus close homology to E. coli PutP, a well-studied Na+/proline
  symporter (QuickGO: P07117 IDA/EXP GO:0005298).

## PseudoCAP IBA-seed assessment

Other seeds' experimental support queried live in QuickGO on 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN005155964 | GO:0022857 transmembrane transporter activity | 7 | 29 (21 taxa) | GO:0015193, IMP, PMID:12270821 (PseudoCAP) | SOUND | Knockout grows poorly on proline; authors conclude PutP is the main proline transporter; 77% identity to E. coli PutP. Descendant term supports the generic node term, which suits the SSS-family clade. | E. coli PutP P07117 (IDA GO:0005298), PanF P16256 (IDA GO:0015233), ActP P32705 (IDA GO:0015123), Salmonella PutP P10502 (EXP), B. subtilis PutP P94392 (CACAO IMP), C. albicans CGD:CAL0000179770 | Yes; several IDA seeds |
| PTN001371338 | GO:0015193 L-proline transmembrane transporter activity | 2 | 20 (16 taxa) | same row | SOUND | as above; node is the PutP subfamily | B. subtilis PutP P94392 (CACAO IMP GO:0015193). The sibling IBD GO:0005298 on the same node rests on E. coli and Salmonella PutP (IDA/EXP). | Yes, on P94392; and the node's PutP members (P07117, P10502) are experimentally proline transporters |

Note: in the current GO, GO:0005298 proline:sodium symporter activity is not
an is_a descendant of GO:0015193 L-proline transmembrane transporter activity,
so the E. coli/Salmonella IDA rows do not by themselves entail the GO:0015193
IBD; P94392 does. Not a defect.

No PSEUDOCAP defect and no GO_CENTRAL defect.
