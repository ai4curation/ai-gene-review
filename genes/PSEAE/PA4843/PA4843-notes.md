# PA4843 / GcbA (AdcA) (Q9HUW7) review notes

Unreviewed UniProt entry with no gene name; folder and gene_symbol use the locus
tag. Literature names: GcbA (Petrova et al. 2014) and AdcA, AmrZ-dependent
cyclase A (Jones et al. 2014). 542 aa: two receiver domains (125-242, 251-367)
and a GGEEF domain (407-539), a PleD-like architecture. UniProt CAUTION: one
receiver lacks conserved residues (PROSITE-ProRule PRU00169). No TRANSMEM feature,
and a Kyte-Doolittle scan (19-residue window, mean above 1.6, run in this session)
finds no hydrophobic window, so it is predicted soluble. The UniProt "Cell inner
membrane" location rests on an ARBA rule only.

## Literature (no deep-research provider available; own reading)

- Jones et al. 2014 (PMID:24603766; full text cached). AmrZ directly represses
  PA4843 (adcA). Expression of PA4843 raises c-di-GMP about 30-fold
  [PMID:24603766 "expression of PA4843 in these strains generated nearly thirty
  fold more c-di-GMP"]; deleting adcA in a amrZ mutant restores wild-type
  c-di-GMP and removes the hyperbiofilm phenotype [PMID:24603766 "Deletion of
  adcA in a ΔamrZ mutant eliminated the accumulation of c-di-GMP and the hyper
  biofilm phenotype"].
- Petrova et al. 2014 (PMID:24891445; full text cached). GcbA overexpression
  gives 228 pmol/mg c-di-GMP versus under 35 for wild type; deletion halves
  planktonic c-di-GMP. GcbA promotes initial attachment, suppresses flagellar
  reversals, and represses swimming and swarming, but does not affect later
  biofilm formation [PMID:24891445 "promotes initial attachment to surfaces, but
  not biofilm formation"].
- Petrova & Sauer 2015 (PMID:25331436; abstract only, no full text from the PMC
  API on 2026-11-05). GcbA DGC activity is needed for BdlA processing and so for
  dispersal in response to many cues [PMID:25331436 "plays an essential role in
  allowing biofilm cells to disperse in response to increasing concentrations of
  a variety of substances, including carbohydrates, heavy metals, and nitric
  oxide"]. Glutamate is not named in the abstract.
- Kulasakara et al. 2006 (PMID:16477007): PA4843 gave no detectable c-di-GMP in
  the PA14 screen (below detection). Not cited by a PA4843 row.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002895344 | GO:0052621 diguanylate cyclase activity | 19 | 205 (28 taxa) | GO:0052621, EXP, PMID:24603766 (PseudoCAP) | SOUND | Expression of PA4843 raises cellular c-di-GMP about 30-fold (LC-MS/MS; full text read). | E. coli DosC, DgcC, DgcJ, DgcM, DgcN, DgcQ, DgcZ and others; B. subtilis DgcK, DgcP; Shewanella Q8EGF8; P. aeruginosa dgcP, wspR, PA1107, PA2870, PA3177, PA3343, PA4332 | Yes. No GO_CENTRAL defect. |
| PTN002895344 | GO:0052621 diguanylate cyclase activity | 19 | 205 (28 taxa) | GO:0052621, IMP, PMID:24603766 (PseudoCAP) | SOUND | Deleting adcA in a amrZ mutant returns c-di-GMP to wild-type levels (full text read). | as above | Yes |
| PTN002895344 | GO:0052621 diguanylate cyclase activity | 19 | 205 (28 taxa) | GO:0052621, IDA, PMID:24891445 (PseudoCAP) | SOUND | Overexpression 228 vs under 35 pmol/mg c-di-GMP; deletion halves planktonic c-di-GMP (full text read). | as above | Yes |

Batch consistency: see wspR-notes.md.

## Other rows

- GO:1902065 response to L-glutamate IMP (PMID:25331436, abstract only): GcbA
  primes BdlA so that biofilms can disperse in response to many cues; the role is
  in dispersal generally, not in sensing glutamate. GO has no biofilm dispersal
  term (checked go-basic.obo). MARK_AS_OVER_ANNOTATED, PSEUDOCAP WRONG_TERM
  defect, PROBABLE (abstract only; glutamate is presumably one of the tested
  dispersal cues in the full text).
- GO:1900233 IMP (PMID:24603766): supported in the amrZ-mutant background;
  Petrova et al. found no effect on biofilm formation in wild type, so
  KEEP_AS_NON_CORE.
- GO:0000160 IEA: KEEP_AS_NON_CORE; the receivers are predicted, no cognate
  kinase or phosphorylation shown.

## Non-seed IBA node PTN002895351

Node-level GO_CENTRAL defects (plasma membrane; GO:0043709) are recorded once, on
wspR. For PA4843: PM IBA and IEA MARK_AS_OVER_ANNOTATED (soluble);
GO:0043709 IBA MODIFY to GO:1900189 (the deletion attaches less, consistent with
SadC); GO:1902201 IBA ACCEPT (deletion swims and swarms slightly more).
