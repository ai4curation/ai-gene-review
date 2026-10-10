# Gamt (rat, UniProt P10868) curation notes

## Re-review 2026-10-04

### What GOA changed

The refreshed `Gamt-goa.tsv` carries 22 rows, matching the 22 rows in the review.
One row was newly seeded as `action: PENDING` - a second ISO row for GO:0006601
creatine biosynthetic process whose donor is human GAMT (UniProtKB:Q14353), split
from the pre-existing ISO row whose donor is mouse Gamt (MGI:MGI:1098221). No rows
were retired.

### PENDING resolved

- **GO:0006601 creatine biosynthetic process (ISO GO_REF:0000121, donor
  UniProtKB:Q14353): ACCEPT.** Human GAMT is the one-to-one ortholog and is the very
  record UniProt cites for the rat FUNCTION line (`ECO:0000250|UniProtKB:Q14353`),
  so the process transfers without reservation. Reviewed as sound but redundant -
  rat Gamt has its own IDA evidence for the same term - and given its own
  `propagation_review` naming the human donor (`NO_FAILURE_CORE`,
  `SUPPORTS_TRANSFER`), rather than copying the sibling row's mouse-donor text.

### Actions changed

None. All 21 previously reviewed rows kept their action after re-audit:

- The three mouse-donor ISO phenotype rows (GO:0007283 spermatogenesis, GO:0009887
  animal organ morphogenesis, GO:0040014 regulation of multicellular organism growth)
  stay `MARK_AS_OVER_ANNOTATED`. These are organismal consequences of creatine
  deficiency, not steps the enzyme performs; the enzyme's contribution to each is
  entirely via the creatine it makes, which GO:0006601 already records.
- GO:0005634 nucleus (IBA) stays `MARK_AS_OVER_ANNOTATED`. The existing review
  already argues this on node placement rather than on donor count - the IBD sits at
  a deep eukaryote node (taxon 2759) seeded by the S. cerevisiae member
  (SGD:S000002873), the same node separately asserts cytoplasm, and the direct rat
  evidence places GAMT in the liver cytosolic fraction. That is the correct way to
  challenge an IBA and it was left intact.
- GO:0008757 S-adenosylmethionine-dependent methyltransferase activity stays
  `ACCEPT` although it is a parent of GO:0030731, which the gene also carries;
  parent-plus-child with different evidence is not a defect.
- GO:0042802 identical protein binding (IPI, PMID:12079381) stays
  `KEEP_AS_NON_CORE`, but the reasoning was made specific rather than generic. The
  dimer is real and resolved, with an inter-subunit contact at the substrate site
  [PMID:12079381 "The truncated enzyme forms a dimer, and each subunit contains one SAH molecule in the active site. Arg220 of the partner subunit forms a pair of hydrogen bonds with Asp134 at the guanidinoacetate-binding site."],
  but it is the N-terminally truncated protein, and UniProt records the physiological
  state as a monomer
  [UniProtKB:P10868 "SUBUNIT: Monomer. May form homodimers upon proteolytic removal of the first 36 amino acid residues."],
  with that cleavage abolishing activity
  [UniProtKB:P10868 "The N-terminal first 36 amino acid residues are susceptible to proteolytic cleavage, leading to loss of activity."].
  So the row is kept, with the caveat stated, rather than read as the enzyme's
  functional quaternary form.

### Support quotes upgraded

Several rows carried only the cited paper's **title** as `supporting_text`, which
asserts nothing about the experiment. Replaced with abstract text that actually bears
on the annotation:

- GO:0006601 (TAS, PMID:12079381) and GO:0008757 / GO:0030731 (IDA, PMID:15533043):
  now quote the enzymatic statement and the structural observations
  [PMID:15533043 "SAH has extensive interactions with GAMT through H-bonds and hydrophobic interactions."],
  [PMID:15533043 "The guanidino groups of GAA and GUN form two pairs of H-bonds with E45 and D134, respectively."],
  [PMID:15533043 "O(D1) of D134 and C(E) of SAM approach N(E) of GAA from the tetrahedral directions."].
- GO:0030731 (NAS, PMID:3277179): now quotes the heterologous-expression result that
  ties this cDNA to the activity
  [PMID:3277179 "This protein represented as much as 5% of the bacterial soluble protein and showed the guanidinoacetate methyltransferase activity."],
  [PMID:3277179 "Also, the enzyme showed kinetic properties indistinguishable from those of the liver enzyme."].
- GO:1990402 embryonic liver development (IEP, PMID:15918910): now quotes the
  expression finding itself
  [PMID:15918910 "AGAT and GAMT are expressed in hepatic primordium as soon as 12.5 days"],
  which is what makes the over-annotation call concrete - the study maps expression
  and never perturbs Gamt or assays a hepatic developmental outcome.
- `core_functions` had a paraphrase of the UniProt FUNCTION and PATHWAY lines spliced
  into one quote; replaced with the two lines quoted separately.

### Other edits

- `description` rewritten as standalone biology. The prior text described what the
  review did ("The review accepts ... keeps ... marks ...") rather than the gene. The
  new text adds the EC number, the reaction and its coproduct, the upstream Gatm/AGAT
  step, tissue distribution, SAH inhibition and methylation-potential sensitivity, the
  N-terminal proteolysis/monomer-dimer point, and the consequences of deficiency.
- `status` moved from IN_PROGRESS to COMPLETE (no PENDING rows remain).

### Open questions

- Is GO:0042802 the right record for what was observed? The dimer belongs to a
  proteolysed form that has lost activity; a reviewer may prefer to drop the row
  entirely rather than keep it with a caveat.
- UniProt's rat FUNCTION line ends "Important in nervous system development", carried
  by similarity from human GAMT. No corresponding process annotation exists on the rat
  gene and none was proposed - the enzyme's contribution to neurodevelopment runs
  through the creatine (and the guanidinoacetate) it makes, which is the substrate/product
  relationship rather than participation in the developmental process.

**Stale UniProt quotes (2026-10-10):** replaced 14 `UniProtKB:P10868` supporting_text quotes that no longer matched the refreshed flat file (the FUNCTION line now wraps at "S-/adenosylmethionine"): 13 with verbatim PATHWAY, CATALYTIC ACTIVITY or FUNCTION text from the current `Gamt-uniprot.txt`, and the cytoplasm IBA row with a verbatim deep-research quote on cytosolic localization (UniProt has no SUBCELLULAR LOCATION line).
