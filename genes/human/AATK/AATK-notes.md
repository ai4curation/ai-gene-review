# AATK / PTHR24417 notes

## Family context

- AATK is the only reviewed human member of `PTHR24417:SF0`. LMTK2
  (`PTHR24417:SF8`) and LMTK3 (`PTHR24417:SF2`) already have complete human
  reviews.
- The shared `PTN004704357` PAINT row asserts `GO:0004672` protein kinase
  activity across the LMTK family. Existing LMTK2 and LMTK3 reviews both treat
  that row as sound but too broad because direct human assays resolve those
  paralogs as serine/threonine protein kinases.
- The LMTK1-specific PAINT node `PTN002815112` carries mouse-Aatk-seeded
  assertions for `GO:0004713`, `GO:0007420`, and `GO:0051402`.

## Row calls

- The two generic `GO:0004672` protein kinase rows were modified to
  `GO:0004674` protein serine/threonine kinase activity. AATK's reviewed
  UniProt record names the product `Serine/threonine-protein kinase LMTK1` and
  carries EC 2.7.11.1 protein-serine and protein-threonine catalytic reactions.
- Both `GO:0004713` protein tyrosine kinase rows were left `UNDECIDED`.
  PMID:11314040 reported tyrosine autophosphorylation by mouse Aatk, but the
  current human UniProt entry assigns AATK only to EC 2.7.11.1 and the two
  better-characterized human LMTK paralogs are serine/threonine kinases. That is
  enough conflict to avoid accepting the human rows as core, but not enough to
  accuse the LMTK1-specific PAINT and InterPro rows of being wrong.
- The `GO:0007420` brain development IBA was accepted. Mouse genetic work ties
  Aatk/LMTK1 to axonal outgrowth, and the human SH-SY5Y paper directly shows
  increased neuronal differentiation and neurite length after human AATK
  overexpression.
- The `GO:0051402` neuron apoptotic process IBA was kept as non-core. It is
  supported by the mouse Aatk seed, but human AATK has direct differentiation
  evidence rather than direct neuron-apoptosis evidence in the cached papers.
- The seven `GO:0005515` rows were removed under the bare-protein-binding policy
  and preserved one per GOA input row. The rows report PPP1CA, PPP1CC, or TEPSIN
  as WITH/FROM partners from IntAct screens, but a root protein-binding term is
  not an informative AATK molecular function.

## Modules and GO-CAMs

- `rg 'Q6ZMQ8|AATK' gocams/index.tsv` found no production GO-CAM covering AATK.
- The reviewed human LMTK paralogs are single-chain kinases with different
  substrates and trafficking contexts rather than a stable multi-subunit
  biological module, so this PR adds no `modules/` review.
