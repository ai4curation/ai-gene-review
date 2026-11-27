# CSTA notes

## GOA and family

- `CSTA-goa.tsv` has 35 annotation rows, so the QuickGO fetch did not produce a header-only file.
- Human `CSTA` and `CSTB` are the only reviewed human members of `PTHR11414`. `CSTB` already has a complete review on `origin/main`; `CSTA` was unreviewed.
- PAINT has two current `PTHR11414` IBD rows, both at `PANTHER:PTN000151700`: `GO:0004869` and `GO:0005829`. The existing CSTB review verified this same node as the stefin clade and accepted both propagated rows.

## Row calls

- Core MF: `GO:0004869`, `GO:0002020`, and `GO:0045861` are sound. PMID:11152132 directly supports rapid papain binding by labeled CSTA; PMID:20860624 directly supports a wild-type human stefin A/cathepsin B complex; PMID:3488317 directly identifies CSTA among human urinary cysteine-proteinase inhibitors and reports kinetic constants for papain and human cathepsin B.
- `PMID:6203523` is abstract-only and centered on cystatin C. It only names "mammalian cystatins A and B" in the cache, so CSTA rows from that PMID were kept because they are manually curated and independently biologically correct, not because the abstract alone reconstitutes the CSTA experiment.
- Bare `GO:0005515` rows were removed under the protein-binding policy. The papain and CTSB interactions are true, but they are represented by `GO:0002020`, `GO:0004869`, and the CTSB peptidase-inhibitor complex row.
- `GO:0001533` is kept as non-core cornified-envelope context. The cached PMID:10908733 abstract supports direct cell-envelope proteomics but does not name CSTA; Reactome explicitly records cystatin A as about 5% of the cornified envelope in `R-HSA-6811539`.
- `GO:0018149` is marked over-annotated. CSTA is a minor cornified-envelope component and may be a substrate incorporated into the envelope, but the cited evidence does not show that CSTA catalyzes or structurally drives peptide cross-linking.
- `GO:0030216` is marked over-annotated. CSTA is expressed and incorporated during terminal keratinocyte differentiation, but the 2000 envelope-composition paper does not show CSTA as a driver of the differentiation program.
- The `GO:0098609` IMP row from PMID:21944047 is kept as a real but epidermal-context role: CSTA knockdown weakens keratinocyte monolayers and organotypic models under mechanical stress.

No production GO-CAM in `gocams/index.tsv` references `UniProtKB:P01040`, and the two human stefins are monomeric inhibitors rather than a reusable multi-part module, so this family did not need a module or GO-CAM review.
