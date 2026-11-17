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

## 2026-11-17: direct enzymology found; generic MF term refined

Found by a cross-member audit of PseudoCAP shared claims, not by re-reading this
gene: `wbpX` and `wbpY` share the `GO:0016757` claim from PMID:9680202, and the
two reviews had settled it differently. `wbpY` used `MODIFY` to `GO:0016758`
hexosyltransferase activity, citing [PMID:35166992] for **both** enzymes, while
`wbpX` used `ACCEPT` on the reasoning that "the linkage and donor have not been
shown biochemically". `wbpX` did not cite PMID:35166992 at all, so one of the two
had to be wrong.

The paper settles it against the `wbpX` reading. It is titled "Biosynthesis of the
Pseudomonas aeruginosa common polysaccharide antigen by D-Rhamnosyltransferases
WbpX and WbpY", its full text is cached, and it reports
[PMID:35166992 "We demonstrated that these GTs are indeed D-RhaTs and catalyze the
transfer of D-Rha from GDP-D-Rha to the reaction product of WbpZ."]. Both enzymes
were expressed and assayed; each alone adds one D-Rha residue and together they
build a polymer of at least eight
[PMID:35166992 "While WbpX and WbpY transferred one D-Rha residue to the WbpZ
product, the combination of WbpX and WbpY resulted in the synthesis of a D-Rhamnan
polymer of at least 8 D-Rha residues."], with WbpX additionally extending the WbpY
product [PMID:35166992 "Additionally, WbpX was observed to transfer several D-Rha
residues to the WbpY product, as well as to a less natural acceptor substrate."].

What the earlier review echoed was the paper's own description of the *prior* state
of the field, from its introduction
[PMID:35166992 "WbpX and WbpY have not been biochemically characterized and the
mechanisms by which D-Rha polymers are synthesized have yet to be understood."] —
true in 2021, not after this work.

Consequences recorded in the review:

- All three `GO:0016757` rows (IBA, IEA, IMP) are now `MODIFY` to `GO:0016758`
  hexosyltransferase activity, matching `wbpY`. D-rhamnose is 6-deoxy-D-mannose, a
  hexose, and `GO:0016758` is an `is_a` child of `GO:0016757` (checked in OLS).
  GO still has no D-rhamnosyltransferase term, which is why the refinement stops
  at hexosyltransferase rather than naming the sugar.
- `core_functions.molecular_function` moved to `GO:0016758`, and the description no
  longer calls the transfer "proposed". The *linkage* assignment (alpha1-2 to WbpX)
  is still an inference from repeat-unit structure, and the description says so.
- The IBA row carries a `propagation_review` identical in substance to `wbpY`'s:
  the node conclusion is sound and apt for the GT4 node's breadth, the two seeds
  are weak only in provenance (a 1998 mutant phenotype, not an assay), and the node
  would be better re-seeded with the PMID:35166992 assays. The gene appearing in
  its own `WITH/FROM` is expected, not circular.

Not changed: the IBA-seed assessment table above still reads SOUND, and no
GO_CENTRAL or PseudoCAP defect is recorded. The node term was never wrong; what
changed is that the target now has direct evidence for a more specific term.
