# Casp9 notes

## 2026-10-01

Falcon deep research could not run because the local environment had no available
research provider credentials (`OPENAI_API_KEY`, `EDISON_API_KEY`, `ASTA_API_KEY`,
or `PERPLEXITY_API_KEY`). I therefore reviewed the GOA seed manually against the
cached publications, UniProt, the mouse Reactome apoptosome event, the existing
human CASP9 review, and the project apoptosis-module decisions.

### Manual evidence trail

- `PMID:9708735` and `PMID:9708736` provide the canonical mouse knockout
  evidence for Casp9 as the intrinsic-pathway initiator downstream of
  mitochondrial cytochrome c: Casp9 deletion prevents Casp3 activation and
  places Casp9 downstream of cytochrome c.
- `PMID:12097332` supports mouse Casp9 as an ER-stress initiator that activates
  downstream procaspase-3 in a cytochrome-c-independent, caspase-12-linked
  branch.
- `PMID:15271982` supports recruitment of pro-caspase-9 with Apaf-1 in
  stress-induced apoptosis: the cached abstract reports that Nucling enters an
  Apaf-1/pro-caspase-9 complex after UV irradiation.
- `PMID:11092819` supports the mouse neural-precursor DNA-damage phenotype:
  caspase-9, with p53, is required for neural precursor apoptosis in vitro and
  in vivo after DNA damage.
- `PMID:11150333` supports developmental nervous-system genetic context for the
  Bcl-x / caspase-9 branch rather than a distinct Casp9 molecular activity.
- `PMID:16183742` was used cautiously: TNF treatment can activate Casp9 in wild
  type MEFs as a control, but the PIDD experiment itself reports no detectable
  processing of procaspase-8 or procaspase-9 in PIDD-expressing MEFs.

### Curation notes

- The exact `GO:0006915 apoptotic process` rows were not all treated the same.
  PAINT/IEA/orthology rows were narrowed to `GO:0097193 intrinsic apoptotic
  signaling pathway`, while the `PMID:17901126` and `PMID:16469926` direct rows
  were left `UNDECIDED` because the cached abstracts do not expose a Casp9 assay.
- DNA-damage intrinsic-apoptosis rows were retained as non-core stimulus
  branches into the Apaf-1 apoptosome / executioner-caspase activation axis.
  DNA-damage, UV, hypoxia, ischemia, cobalt, ethanol, lipopolysaccharide,
  indole-3-methanol, anesthetic, kidney-development, leukocyte, and glial parent
  process rows were otherwise treated as non-core or over-annotated contexts
  unless the row directly captured the core axis.
- Nucling and ER-stress papers support specialized Casp9-containing complexes
  or stimulus branches, but the synthesized core function remains cytosolic
  Apaf-1 apoptosome recruitment and downstream procaspase maturation.
