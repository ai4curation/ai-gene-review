# wbpX (PA5449, G3XCU3) review notes

No deep-research provider was available. Sources: UniProt record (TrEMBL), cached
PMID:9680202 (abstract only, no PMC full text). PubMed and Europe PMC searches failed
on 2026-11-05 (server errors), so no later literature could be retrieved.

## Function

- WbpX is one of three alpha-D-rhamnosyltransferases that assemble the A-band (common
  polysaccharide antigen) D-rhamnan O-polysaccharide
  [PMID:9680202 "The A-band polysaccharide is assembled by the alpha-D-rhamnosyltransferases, WbpX, WbpY and WbpZ."].
- Proposed role: alpha1-2 rhamnosyl transfer, processive and alternating with WbpY
  [PMID:9680202 "WbpY and WbpX subsequently transfer two alpha1-->3 linked Rha residues and one alpha1-->2 linked Rha respectively"];
  [PMID:9680202 "The last two transferases are predicted to be processive"].
- Mutant phenotype: no A-band LPS, B-band unaffected
  [PMID:9680202 "these mutants are unable to synthesize A-band LPS, while B-band synthesis is unaffected"].
- Domain: glycosyltransferase family 1 (Pfam PF00534, InterPro IPR001296), CDD GT4_MtfB-like.

The linkage assignments in the paper are inferences from repeat-unit structure and gene
order; the abstract reports genetics (mutants, Western blot) rather than enzyme assays.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN005302544 | GO:0016757 glycosyltransferase activity | 2 | 60 (22 taxa) | GO:0016757 glycosyltransferase activity, IMP, PMID:9680202 (PseudoCAP) | SOUND | Generic GT activity for a GT1-domain protein whose mutant cannot make the A-band rhamnan. The specific linkage is inferred, but the node term is the generic one, which the domain plus mutant data support. | WbpY Q9HTB9 (same paper, same kind of evidence) | Yes in substance; WbpY's seed rests on the same paper and the same genetic logic, and the GT1 domain supports the generic term for the whole clade. No GO_CENTRAL defect. |

Defects recorded: PSEUDOCAP 0; GO_CENTRAL 0.
