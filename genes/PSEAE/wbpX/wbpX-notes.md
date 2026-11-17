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

- The specific activity is asserted as a **`NEW` row**: `GO:0016758`
  hexosyltransferase activity, IDA, on PMID:35166992. D-rhamnose is
  6-deoxy-D-mannose, a hexose, and `GO:0016758` is an `is_a` child of `GO:0016757`
  (checked in OLS). GO still has no D-rhamnosyltransferase term, which is why it
  stops at hexosyltransferase rather than naming the sugar.
- The three existing `GO:0016757` rows (IBA, IEA, IMP) stay **`ACCEPT`**. An earlier
  version of this change made all three `MODIFY` to `GO:0016758`, copying `wbpY`.
  The 2026-11-14 ruling in CLAUDE.md disallows that: a `MODIFY` needs *this row's own*
  evidence for the deeper term, and none of the three has it — the IBA inherits a node
  typed at `GO:0016757`, the IEA rests on the generic GT1 fold signature `IPR001296`,
  and the 1998 IMP is a mutant phenotype whose "rhamnosyltransferase" naming is the
  authors' own hedged inference. The assay belongs on the row that holds it. `wbpY` was
  changed the same way in the same PR, so the pair still agrees.
- `core_functions.molecular_function` is `GO:0016758`, and neither the core-function
  description nor the top-level `description` calls the transfer "proposed" any more.

Three statements in this file contradicted the paper and were corrected with it:

- The top-level `description` said the donor and linkage "have not been shown by
  enzyme assay" and that WbpX acts **processively**. The paper shows transfer from
  GDP-D-Rha directly, and reports the opposite mechanism: the WbpX/WbpY mixture
  synthesises D-Rha oligomers *non-processively*.
- The core-function description said the alpha1-2 assignment "remains inferred …
  rather than shown". It was shown: [PMID:35166992 "NMR analysis revealed that WbpX
  synthesizes both α1-2 and α1-3 D-Rha linkages while WbpY synthesizes a single
  D-Rhaα1-3 linkage."]. The open question is which linkage WbpX makes at each
  position of the native repeat, not whether any was demonstrated.
- `suggested_questions` and `suggested_experiments` asked for the donor, linkage and
  processivity work this paper had already done. Both now ask what is actually open:
  how a single-domain enzyme switches between the two linkages.
- The IBA row carries a `propagation_review` identical in substance to `wbpY`'s:
  the node conclusion is sound and apt for the GT4 node's breadth, the two seeds
  are weak only in provenance (a 1998 mutant phenotype, not an assay), and the node
  would be better re-seeded with the PMID:35166992 assays. The gene appearing in
  its own `WITH/FROM` is expected, not circular.

Not changed: the IBA-seed assessment table above still reads SOUND, and no
GO_CENTRAL or PseudoCAP defect is recorded. The node term was never wrong; what
changed is that the target now has direct evidence for a more specific term.

**A second shared claim, caught in review.** `wbpX` and `wbpY` also share
`GO:0009103` lipopolysaccharide biosynthetic process from the same 1998 paper,
and had it as `TOO_GENERAL` here against `MODIFY` to `GO:0009243` there, with
nothing in either row arguing the difference. Both now read `TOO_GENERAL`: that
is what `action_consistency.yaml` calls the intended use, a broad term subsumed
by a more specific accepted term, and the specific term is the `GO:0009243` IDA
row both genes already carry, so a `MODIFY` proposing it as a replacement would
add nothing.

Both rows now also say why that term is `TOO_GENERAL` while the three
`GO:0016757` rows are `ACCEPT`, since both are ancestors of a term asserted
elsewhere in the review. LPS biosynthesis is imprecise in its own right once
O-antigen synthesis is asserted — LPS is lipid A plus core plus O antigen, and
the row does not say which part this gene builds. Glycosyltransferase activity
is not imprecise in that way: it is a definite claim about what the protein does
to a substrate, and it is as precise as those rows' own evidence reaches.

The audit script could not see this one: it reads the molecular-function
worklist, so process claims are out of its scope. That limit is now stated in the
script and on the project page.

**Two corrections to the entry above, from later review rounds.** The entry is
left as written and corrected here, because it is a record of what was believed
when, not a statement of current fact.

*Processivity was overstated.* The paragraph above says the paper "reports the
opposite mechanism: the WbpX/WbpY mixture synthesises D-Rha oligomers
*non-processively*". The paper does report that, but hedges it in the same
breath: [PMID:35166992 "WbpX and WbpY lack the QxxRW sequence found in processive
enzymes [47] and therefore may act in a non-processive or partially processive
mechanism."]. The review rows now carry the hedge; this note is where it was
missing longest, because round 4 corrected the YAML and not the prose beside it.

*The linkage NMR was not run on the lipid-analogue acceptor.* The entry above
cites the α1-2/α1-3 result without saying which acceptor produced it. The
transfer assays used the phenylundecyl-diphosphate analogue, but NMR of those
products failed — [PMID:35166992 "However, the 2D NMR analysis showed that a
complex mixture of compounds was present and the structures could not be
resolved (data not shown)."] — and the linkage assignments come from a
large-scale synthesis on a benzyl D-rhamnoside acceptor, which the authors note
[PMID:35166992 "It is interesting that the polymerization by WbpX was clearly
facilitated by replacing the D-GlcNAcα-PP-Und moiety of the acceptor with a
benzyl group that appeared to enhance the acceptor affinity."] and which may
[PMID:35166992 "This sequence of WbpZ → WbpY → WbpX action may not be required
when using a non-natural synthetic D-Rhaα-Bn acceptor."] bypass the native order
of action. The `GO:0016758` term is unaffected either way, since it asserts
hexosyl transfer and not a linkage.

Both corrections are the same failure repeated: fixing a claim in one file and
leaving the identical claim in the file next to it. The lesson applied from
round 3 onwards is to sweep every instance rather than patch the one that was
named.
