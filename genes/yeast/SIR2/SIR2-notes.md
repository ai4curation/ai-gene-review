# SIR2 curation notes

## 2026-09-02 Update

Audited existing_annotations for oversights.

- **GO:0006303 (double-strand break repair via nonhomologous end joining), IMP,
  PMID:9501103**: was marked `REMOVE` with the reasoning "SIR2 is not a component
  of the NHEJ repair machinery... conflates recombination suppression with NHEJ
  repair." This is contradicted by the cited paper's own abstract, which reports
  a direct functional assay: "using an in vivo plasmid rejoining assay, we
  demonstrate that SIR2, SIR3 and SIR4, three genes shown previously to function
  in TPE, are essential for Ku-dependent DSB repair" [PMID:9501103 "using an in
  vivo plasmid rejoining assay, we demonstrate that SIR2, SIR3 and SIR4, three
  genes shown previously to function in TPE, are essential for Ku-dependent DSB
  repair"]. SIR2 is not part of the core catalytic NHEJ machinery (Ku70/80,
  Lig4/Dnl4), but the IMP evidence directly demonstrates it is genuinely required
  for efficient Ku-dependent end-joining in vivo. Changed action from
  `REMOVE` to `KEEP_AS_NON_CORE` to reflect this real, experimentally-demonstrated,
  secondary requirement rather than removing a genuine finding.

## 2026-09-04 Update: review follow-up

Addressing review feedback on PR #2942.

### Dropped the speculative mechanism from the NHEJ `reason`

The `reason` had claimed the end-joining requirement was "likely via its
chromatin/telomere maintenance role". The paper does not say this, and none of
the papers bearing on the actual candidate mechanism are cached, so no PMID can
be cited without guessing. The clause is removed and replaced with an explicit
statement that the mechanism is not established by the cached abstract. (For the
record only, not asserted in the YAML: the standard explanation in the field is
that loss of silencing derepresses HML/HMR, producing a pseudo-diploid a1/alpha2
state that represses NHEJ genes such as NEJ1 - i.e. an indirect transcriptional
effect rather than a direct chromatin one. This should be sourced properly before
it enters the review.)

### GO:0016740 `REMOVE` was wrong -- the review's own text conceded it

The prior `reason` argued SIR2 "is not a transferase", while simultaneously
admitting "the reaction formally involves transfer of the acetyl group to
ADP-ribose". The repo's own UniProt record settles it:

- `SIR2-uniprot.txt:7` -- `EC=2.3.1.286` (EC class 2.3 = acyltransferases)
- `SIR2-uniprot.txt:282-287` -- reaction `N(6)-acetyl-L-lysyl-[protein] + NAD(+)
  + H2O = 2''-O-acetyl-ADP-D-ribose + nicotinamide + L-lysyl-[protein]`
- `SIR2-uniprot.txt:442` -- keyword `Transferase`
- `SIR2-goa.tsv:15` -- the IEA cites `UniProtKB-KW:KW-0808`, i.e. that keyword

Sirtuins are not hydrolytic deacetylases; they consume NAD+ and transfer the
acetyl group onto ADP-ribose. So the term is correct but uninformatively generic.
Changed `REMOVE` to `KEEP_AS_NON_CORE`. The entry's existing `supporting_text`
[PMID:10811920 "members of the SIR2 family catalyze an NAD-nicotinamide exchange
reaction that requires the presence of acetylated lysines"] supports the transfer
chemistry, so it was already inconsistent with the `REMOVE`.

### Replaced title-only quotes for PMID:9501103

Three `supported_by` entries quoted the paper's title rather than a result. All
three now quote the abstract body:

- GO:0006974 (DNA damage response, IBA) -- "As is the case for Ku-deficient
  strains, residual repair operating in the absence of the SIR gene products
  ensues through an error-prone DNA repair pathway that results in terminal
  deletions."
- GO:0031509 (subtelomeric heterochromatin formation, IBA and IMP) -- "SIR2, SIR3
  and SIR4, three genes shown previously to function in TPE". Note this is the
  paper reporting SIR2's TPE role as *previously established*, not as its own
  result; the IMP's `reason` now says so explicitly. `full_text_available` is
  false, so per CLAUDE.md the SGD curator's experimental call still stands.

### Stale companion documents -- NOT fixed here, needs a maintainer decision

Four files in this folder still record the retracted `REMOVE` decisions and now
contradict the review:

- `SIR2-ANNOTATION-ACTIONS.tsv:51` -- GO:0006303 `REMOVE`
- `SIR2-CURATION-SUMMARY.md:62,66` -- GO:0016740 and GO:0006303 under
  "mechanistically incorrect"
- `README-CURATION.md:207,209` -- "Remove GO:0016740", "Remove GO:0006303"
- `CURATION-REVIEW-FINAL.md:140-152` -- including "PMID:9501103 discusses
  telomeric silencing and recombination suppression, not NHEJ repair
  participation", which is exactly the claim the cited abstract disproves

These are ad-hoc curation artifacts outside the schema-defined file set
(`*-ai-review.yaml`, `*-notes.md`, ...), and the right fix is arguably to delete
them rather than maintain a parallel record that can drift out of sync with the
review. That is a maintainer call, so they are left untouched and flagged on the
PR instead.

### Scope of these passes

Both passes were targeted (the NHEJ decision, then the review's specific
findings). The remaining annotation actions were not systematically
re-adjudicated, so no blanket claim is made about them.

## 2026-09-08 Update: round-3 review follow-up (PR #2942)

Addressed the two in-scope self-consistency suggestions from the round-2 review:

- GO:0006303 `summary` said the NHEJ requirement is "a secondary consequence of
  its silencing/chromatin role". The `/chromatin` clause pointed back at the
  direct-chromatin mechanism that the `reason` explicitly declines to assert, so
  the two conflicted. Trimmed to "a secondary consequence of its silencing
  function" - true under either candidate mechanism and now consistent with the
  `reason`.
- GO:0016740 `summary` called it a "Generic parent term". Whether GO:0016740 is
  actually an ancestor of the NAD-dependent deacetylase terms is an unverified
  ontology-ancestry claim (GO tends to classify protein deacetylase activity
  under hydrolase). Dropped "parent"; "Generic term" says what is meant without
  depending on the ontology placement.

### Items NOT fixed here - outside this pass's permitted edit set

This pass was permitted to edit only `SIR2-ai-review.yaml` and `SIR2-notes.md`.
The two remaining blocking items both require editing other files and are left
for a maintainer decision:

- `generate_sir2_review.py` still hardcodes the retracted `REMOVE` decisions for
  GO:0016740 (`:179-184`) and GO:0006303 (`:511-516`) and the title-only
  PMID:9501103 quote, and writes `SIR2-ai-review.yaml` wholesale to a hardcoded
  `/Users/cjm/...` path (`:822-823`). It is not wired into CI or any justfile
  target, so there is no live break, but running it (as `README-CURATION.md:124-128`
  advertises) would revert this PR. Recommended fix: delete the one-off scaffold
  and drop the "can be run to regenerate" line, since the review file is now
  hand-curated. Left untouched here per edit scope.
- The four stale companion docs (`SIR2-ANNOTATION-ACTIONS.tsv`,
  `SIR2-CURATION-SUMMARY.md`, `README-CURATION.md`, `CURATION-REVIEW-FINAL.md`)
  remain as recorded above; the GO:0016740 change makes two of them stale on a
  second count. Same maintainer call (delete vs. maintain).

## 2026-09-09 Update: round-4 review follow-up (PR #2942)

### GO:0006281 `DNA repair` -- rationale was falsified by this PR's own NHEJ fix

The round-3 review flagged a contradiction introduced by this PR: GO:0006281 was
`MARK_AS_OVER_ANNOTATED` on the grounds that "SIR2 is not a DNA repair enzyme...
This is recombination suppression, not DNA repair", while the GO:0006303 block
accepts IMP evidence that SIR2 *is* genuinely required for Ku-dependent
end-joining repair.

Checked the ancestry rather than assuming it. QuickGO
(`/ontology/go/terms/GO:0006303/ancestors?relations=is_a,part_of`) returns both
`GO:0006302` and `GO:0006281` among the ancestors of `GO:0006303`, so this is a
true-path-rule problem and not merely a prose inconsistency: accepting the NHEJ
child entails the DNA-repair parent.

Rewrote the GO:0006281 block to argue *altitude* rather than *falsity*, and
changed the action `MARK_AS_OVER_ANNOTATED` -> `KEEP_AS_NON_CORE`, matching how
the other correct-but-generic IEA rows on this gene are handled (GO:0016740
transferase activity, GO:0006974 DNA damage response). Added the PMID:9501103
plasmid-rejoining quote to `supported_by` so the retained term is grounded in the
same experimental row that grounds the child term. The existing PMID:12923057
hyperrecombination quote is kept.

Note the provenance symmetry the review pointed out: GO:0006281 is the same kind
of keyword-derived row (IEA, GO_REF:0000043, UniProtKB-KW:KW-0234) that this
review already accepted for GO:0016740 on the strength of its UniProt keyword
chain, and it now additionally has experimental grounding on the target itself.

### `generate_sir2_review.py` -- stale decisions synced

The script writes `SIR2-ai-review.yaml` wholesale, so running it (as
`README-CURATION.md` advertises) would have reverted this PR. It is not wired
into CI and its output path is still hardcoded to `/Users/cjm/...`, so nothing
was breaking today, but the documented regeneration path silently undid the fix.
Updated the three now-stale dict entries in place so the script's decisions match
the curated YAML:

- GO:0006303 -- `REMOVE` -> `KEEP_AS_NON_CORE`, with the abstract-body quote
  replacing the title-only one
- GO:0016740 -- `REMOVE` -> `KEEP_AS_NON_CORE`, with the EC 2.3.1.286 rationale
- GO:0006281 -- `MARK_AS_OVER_ANNOTATED` -> `KEEP_AS_NON_CORE`, per the change
  above

This is the narrower of the two fixes the review offered (update the dicts vs.
delete the scaffold and drop the README claim). Deleting the script is still the
better long-term answer -- a wholesale generator alongside a hand-curated YAML
will drift again -- but that requires editing `README-CURATION.md`, which is
outside this pass's permitted edit set. Flagged on the PR instead.

### Still NOT fixed -- outside this pass's edit scope

The four stale companion docs are unchanged, for the third round running. This
pass was permitted to edit `*-ai-review.yaml`, `*-notes.md`, and tooling scripts
only; `SIR2-ANNOTATION-ACTIONS.tsv`, `SIR2-CURATION-SUMMARY.md`,
`README-CURATION.md`, and `CURATION-REVIEW-FINAL.md` are none of those. The
maintainer call (delete vs. maintain) is still open.
