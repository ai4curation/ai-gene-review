# SERINC1 curation notes

Date: 2026-07-18

## Research log

- `just fetch-gene human SERINC1` fetched 16 GOA rows and seeded 12 grouped
  annotation entries.
- `just fetch-gene-pmids human SERINC1` confirmed both GOA PMIDs were cached.
- Falcon deep research failed with HTTP 402; Perplexity-lite fallback failed
  with HTTP 401 insufficient quota. The failures are documented here and in
  `SERINC1-deep-research-manual.md`; no failed provider-named output was kept.
- Reviewed Q9NRX5 UniProt, every raw GOA row/group, PMID:20195357,
  PMID:32296183, PMID:16120614, and PMID:28006656.

## Annotation decisions

- GO:0016020 membrane (IBA and IEA): **MODIFY** to GO:0005789 endoplasmic
  reticulum membrane. Generic membrane is true but less informative than the
  experimentally established mammalian ER site.
- GO:0005789 endoplasmic reticulum membrane (IEA and ISS group): **ACCEPT**.
  Rat Serinc1 co-localizes with lipid-biosynthetic enzymes in ER membranes
  [PMID:16120614, "rat Serinc1 protein co-localizes with lipid biosynthetic
  enzymes in endoplasmic reticulum membranes"].
- GO:0005886 plasma membrane (ISS): **UNDECIDED**. The source rat record has an
  experimental annotation, but the cached paper is abstract-only and emphasizes
  ER localization; do not overrule the curator without the assayed full-text
  context.
- GO:0005515 protein binding (IPI; two grouped entries representing PAX8 and
  four HuRI partners): **MARK_AS_OVER_ANNOTATED**. Both are systematic screens
  without a demonstrated functional consequence for SERINC1.
- GO:0010698 acetyltransferase activator activity (ISS): **MODIFY** to
  GO:0008047 enzyme activator activity. SERINC1 stimulates phosphatidylserine
  synthase and serine C-palmitoyltransferase, but neither result establishes
  activation of an acetyltransferase.
- GO:0030674 protein-macromolecule adaptor activity (ISS): **ACCEPT**. The
  mammalian/yeast study supports a scaffold that links serine-synthetic and
  lipid-biosynthetic machinery [PMID:16120614, "forms an intracellular complex
  with key enzymes"].
- GO:0044091 membrane biogenesis, GO:0006658 phosphatidylserine metabolic
  process, and GO:0006665 sphingolipid metabolic process (ISS): **ACCEPT** as
  the processes captured by the direct rat and family-level experiments.

## Important negative boundary

Do not add L-serine transmembrane transporter activity. The open-access full
text of PMID:16120614 reports unchanged free-serine uptake in Serinc1-expressing
cells and explicitly distinguishes incorporation into nascent membrane lipids
from transport across the bilayer.

## Synthesis and priorities

The core assignment is orthology-supported ER membrane adaptor/enzyme activator
activity promoting phosphatidylserine and sphingolipid synthesis. The strongest
next test is endogenous human SERINC1 knockout/rescue, both alone and combined
with other SERINC paralogs, with isotope-resolved lipid synthesis and direct
enzyme/complex measurements. ER-versus-plasma-membrane localization should be
resolved independently at endogenous abundance.
