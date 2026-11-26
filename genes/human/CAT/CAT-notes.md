# CAT notes

## 2026-11-26 review

Human CAT is the single Swiss-Prot human member of PTHR11465. The SF9 branch also contains animal
catalases and fungal catalase A proteins, while S. cerevisiae cytosolic CTT1 is in SF62. A full
literature-provider deep-research file was not available in this checkout, so this review used the
cached UniProt record, the current GOA rows, the existing PTHR11465 PAINT/family review, and the
publication and Reactome records fetched by `just fetch-gene human CAT`.

Core calls:

- `GO:0004096` catalase activity, `GO:0042744` hydrogen peroxide catabolic process and
  `GO:0061692` cellular detoxification of hydrogen peroxide are the core CAT activity/process
  claims. UniProt records the RHEA:20309 reaction and PMID:10656833 establishes that human catalase
  is a heme-containing peroxisomal enzyme that decomposes hydrogen peroxide to water and oxygen.
- Human CAT is a homotetrameric heme/NADP-binding catalase complex. The cofactor-binding rows are
  real but secondary to the catalytic function.
- The mature enzyme is in the peroxisomal matrix. PMID:8769411 identifies the C-terminal KANL signal
  and shows PTS1-pathway targeting; PMID:21976670 places monomeric catalase in the PEX5 cargo cycle.
- PMID:7882369 supports UniProt's curated growth-factor statement by identifying a human
  erythrocyte-derived growth-promoting factor as catalase and tying that activity to hydrogen
  peroxide decomposition. A separate proliferation or growth GO term would describe a downstream
  consequence rather than work performed by CAT, so no new proliferation annotation was added.
- UniProt's ACATLAS disease block was checked; acatalasemia is caused by CAT variants through loss
  of catalase activity and did not identify an additional GO molecular function, process or location.

Non-core but supported:

- `GO:0005829` cytosol is a transient pre-import state while PEX5 binds CAT cargo; it is not the
  mature resident location. Reactome FOXO3/FOXO6 CAT-expression events do not themselves localize
  catalase protein.
- Reactome neutrophil degranulation rows and the EPS-urine exosome HDA row are peripheral exported
  pools and were kept as non-core.
- UV protection and negative regulation of apoptosis are overexpression-backed keratinocyte
  phenotypes of catalase-mediated peroxide removal, not the main peroxisomal pathway.

Rows pruned or down-scored:

- The Ensembl Compara aminoacylase row is incompatible with catalase biochemistry and was removed.
- Peroxisomal membrane rows were removed because human CAT is a soluble peroxisomal matrix PTS1
  cargo, not an integral or lumen-facing membrane protein.
- The UniProt PMID:10514471 `GO:0016209` antioxidant-activity row is attached to CAT even though the
  abstract characterizes human/mouse PMP20; it was left as a true but too-general antioxidant claim
  with a source-defect query to UniProt.
- Osteoblast differentiation, focal adhesion, generic membrane, hormone, xenobiotic and most
  stimulus-response rows were marked over-annotated because the cached evidence is proteomic
  detection or rodent stress/phenotype propagation, not direct execution of those specific
  processes by the human enzyme.

The existing PTHR11465 review was extended only to add human CAT as an SF9 representative and to
record that the shared PAINT catalase, heme, response-to-H2O2, cytoplasm, peroxisome and
hydrogen-peroxide-catabolism calls now also agree with the human CAT review.
