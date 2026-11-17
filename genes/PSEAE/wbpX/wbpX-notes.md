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

**Substrate specificity, added in a later round.** The two enzymes differ in a
way neither review recorded at first. WbpX is strictly specific for its sugar
[PMID:35166992 "WbpX showed no transferase activity using any of the nucleotide
sugars other than GDP-D-[3H]Rha, indicating that it is exclusively a D-RhaT."],
while WbpY also transfers D-mannose [PMID:35166992 "In contrast, His6-WbpY had
also significant D-ManT activity using GDP-[3H]Man which was 70% of the D-RhaT
activity (Table 1)."] and is therefore [PMID:35166992 "WbpY is therefore a dual
D-RhaT and D-ManT, similar to WbpZ."].

So WbpX is bifunctional in *linkage* (α1-2 and α1-3) but monospecific in
*sugar*, and WbpY is the reverse: one linkage, two sugars. That bears on the
request for a GO D-rhamnosyltransferase term, which is recorded once for the
pair on the wbpY review — such a term would describe WbpX exactly and WbpY only
partly. It also means `GO:0016758` hexosyltransferase activity is the apter stop
for WbpY than it first appeared, since D-rhamnose is 6-deoxy-D-mannose and the
term covers both sugars the enzyme uses.

Neither activity is separately annotated: GOA carries no mannosyltransferase row
for either gene, and at 70% of the D-rhamnose rate the D-mannose activity is a
genuine secondary activity rather than noise, but no D-mannose appears in the CPA
repeat, so what it does in vivo is unknown. That is a question for the bench, and
it is recorded as one on wbpY.

**Correction to the acceptor note above.** The paragraph added earlier to
separate the transfer assay from the linkage NMR did the separation for WbpX and
then swept WbpY's result into the same clause, saying that "on that acceptor"
WbpX forms both linkages "whereas WbpY forms only alpha1-3". WbpY's linkage NMR
was not run on the benzyl acceptor at all: it used the lipid analogue
[PMID:35166992 "To analyze the linkage(s) synthesized by WbpY, purified GST-WbpY
elution fractions were pooled and used in 1000 × standard assays, using
D-Rhaα1-3-D-GlcNAcα-PP-PhU acceptor substrate"], giving [PMID:35166992 "Thus
WbpY is a monofunctional α1,3-D-RhaT."]. The benzyl acceptor appears only in the
WbpX experiment. So the sentence written to stop two experiments being read as
one did exactly that for a third.

The same clause also left "it adds several residues in sequence" dangling off
WbpY, which adds one [PMID:35166992 "The spectra indicated that WbpY transferred
a single D-Rha residue in α1-3 linkage"]; the multi-residue result is WbpX's
[PMID:35166992 "indicating that WbpX added multiple residues to D-Rhaα-Bn
acceptor substrate"]. As written it asserted the opposite of this review's own
finding a few lines above.

Both are corrected in the description, which now states each enzyme's result
with the acceptor that produced it.

**Correction to the D-mannose reasoning above.** The paragraph on substrate
specificity says "no D-mannose appears in the CPA repeat, so what it does in vivo
is unknown". The *repeat* is pure D-rhamnan, so that sentence is literally
accurate, but it was written on the broader premise that CPA contains no
D-mannose at all, and the paper says otherwise: [PMID:35166992 "CPA from various
PA strains is essentially a D-rhamnan but has been shown to contain a small
amount of D-Man as well as other monosaccharides including xylose and ribose"].

The paper also goes some way to answering the question that premise generated.
WbpY is judged [PMID:35166992 "WbpY could transfer a single D-Man but due its
restricted acceptor specificity it is not likely to build a D-Man polymer."], and
the purity of the polymer is attributed to WbpX alone: [PMID:35166992 "The
relatively high purity of CPA is clearly due to the polymerizing activity of WbpX
that exclusively utilizes GDP-D-Rha as donor."]. So the minor D-mannose in CPA
would be single residues rather than stretches, which fits WbpY as a possible
source without showing it is one. The wbpY question is sharpened accordingly, and
WbpX's exclusivity is now recorded as the reason the polymer is as pure as it is
rather than as a bare specificity fact.
