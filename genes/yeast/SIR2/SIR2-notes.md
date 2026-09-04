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
