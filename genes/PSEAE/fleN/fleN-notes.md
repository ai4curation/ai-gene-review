# fleN (PA1454, UniProt G3XD64) notes

No deep-research provider was available; the literature research below was done manually
(PubMed search "FleN Pseudomonas aeruginosa", 28 hits; key papers cached via `just fetch-pmid`).

## Biology summary

- Identification: fleN ORF between flhF and fliA encodes a 280-aa protein "with an ATP-binding
  motif at its N terminus"; insertion mutants are multiflagellate and FleQ-dependent flagellar
  promoters are up-regulated [PMID:10629180 "the mutants were multiflagellate, with three to six polar
  flagella per bacterium as rather than one as in the wild type"]. Full text of this paper is not
  available to us (abstract only; PMC publisher-restricted).
- FleN-FleQ interaction (yeast two-hybrid), Walker A K24Q abolishes it; ATP binding still described as
  putative [PMID:11673434 "Flagellar number in Pseudomonas aeruginosa is controlled by FleN, a putative
  ATP/GTP binding protein"].
- FleN with FleQ at the pel promoter: FleN binds DNA-bound FleQ and bends DNA; requires ATP but not
  hydrolysis [PMID:22581773 "FleN is a putative ATPase with a deviant Walker A motif"].
- Crystal structures (apo and AMP-PNP): ATP binding remodels FleN into a dimer; nucleotide binding,
  not hydrolysis, is needed to antagonize FleQ [PMID:28065505 "it is nucleotide binding and not hydrolysis
  by FleN that is necessary to exert an antagonistic effect against FleQ"].
- FleQ AAA+ / FleN complex: FleN allosterically blocks ATP binding to FleQ [PMID:34669473 "FleN WT
  completely abolishes the ATPase activity of FleQFL"]; FleN has its own weak ATPase activity
  [PMID:34669473 "residual activity is similar to the ATPase activity of FleN"].
- Cryo-EM FleQ-FleN (+/- c-di-GMP): K19A "no longer dimerize or hydrolyze ATP efficiently (at about 16%
  relative to wild-type FleN)"; D48A is "ATP-binding but hydrolysis-incompetent" [PMID:38051770].
- Localization: FleN fluorescent fusions diffuse [PMID:36622167 "FleN was equally distributed in the
  cells independent of the terminus to which fluorescent protein was attached"]. No evidence of the
  MinD-like membrane association.

## Decisions

- ATP binding IDA (PseudoCAP): term true, evidence code likely wrong (sequence motif). ACCEPT + PSEUDOCAP
  source defect (WRONG_EVIDENCE_CODE, PROBABLE, CHECK).
- ATP binding IBA: ACCEPT; GO_CENTRAL source defect asking to re-seed PTN000344128.
- ATP hydrolysis activity IBA: ACCEPT (weak intrinsic ATPase shown, PMID:38051770, PMID:34669473).
- cytosol IBA: ACCEPT. cytoplasmic side of plasma membrane IBA: MARK_AS_OVER_ANNOTATED (MinD-specific).
- NEW: GO:0042030 ATPase inhibitor activity (IDA, PMID:34669473) for anti-activation of FleQ;
  GO:1902209 negative regulation of bacterial-type flagellum assembly (IMP, PMID:10629180). FleN performs
  the regulatory step itself (binds/inhibits FleQ), so the participation test is met.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN000344128 | GO:0005524 ATP binding | 1 (sole seed) | 149 (75 taxa) | GO:0005524 ATP binding, IDA, PMID:10629180 | WRONG (evidence code; term itself correct) | PMID:10629180 only reports an ATP-binding sequence motif; the same authors called FleN "putative ATP/GTP binding" in 2001 (PMID:11673434). Not direct evidence, so the row should be ISM/ISS or re-keyed to PMID:28065505 (FleN-AMP-PNP structure). The IBD conclusion (MinD/ParA/FlhG clade binds ATP) is biologically sound and the leaf IBAs are not wrong, but the node needs a genuine experimental seed (FleN PMID:28065505 or E. coli MinD) before the PseudoCAP row is corrected. |

Caveat: full text of PMID:10629180 was not accessible; the evidence-code verdict rests on the abstract
plus the authors' 2001 wording, hence confidence PROBABLE.
