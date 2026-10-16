# CFAP70 notes

## Deep research status

Automated deep research was attempted and failed, so no `CFAP70-deep-research-*.md`
file exists for this gene:

- `just deep-research human CFAP70 --provider falcon` failed with
  `Exception: Failed to authenticate` (Edison/Falcon JWT authentication error).
- `just deep-research human CFAP70 --provider perplexity` failed with
  `Provider 'perplexity' not available. Available: falcon, asta, openscientist`.

The notes below come from a manual PubMed search (`CFAP70[Title/Abstract]`, 18 hits,
2016-2026) and the cached publications under `publications/`. Each cited PMID was
cached with `just fetch-pmid`.

## Identity

- UniProt Q5T0N1 (CFA70_HUMAN); 1,121 aa; TPR-repeat protein (7 TPR repeats in the
  C-terminal half), PANTHER PTHR44314. Ortholog of Chlamydomonas FAP70.
- Disease: spermatogenic failure 41 (SPGF41, MIM:618670), autosomal recessive.

## Localization: from "base of the outer dynein arm" to the C2a projection

- The first characterisation (mouse/swine/Chlamydomonas) placed it on the doublets:
  [PMID:30158508 "A stepwise extraction of proteins from swine tracheal cilia showed that
  CFAP70 bound tightly to the ciliary axoneme"] and [PMID:30158508 "Cryo-electron
  tomography revealed that the N-terminus of FAP70 resided stably at the base of the
  ODA."]
- This was revised by the Witman group using the same tagged strain:
  [PMID:33988244 "we determined by super-resolution structured illumination microscopy
  that FAP70 is located exclusively in the CA, and show by cryo-electron microscopy that
  its N-terminus is located at the base of the C2a projection of the CA."] They explain
  the earlier result: [PMID:33988244 "streptavidin signal was present at the base of the
  outer dynein arm, as well as associated with the nexin-dynein regulatory complex"] and
  argue from CA-less mutants that FAP70 cannot be on the doublets.
- Mouse sperm in situ cryo-ET confirms C2a placement in mammals:
  [PMID:40473901 "We identified two major components of the C2a projections: CFAP65 and
  CFAP70; the latter forms a homodimer involved in CA"].
- Mouse KO: [PMID:42417609 "The ciliary incorporation of CCDC108, MYCBPAP, and CFAP70 is
  essential for one another's stability, with the loss of any single component
  triggering C2a collapse"]. CFAP65 binds CFAP70 at the C2a base
  [PMID:39853433 "CFAP65 was found to anchor at the base of the C2a projection of the
  axoneme, interacting with proteins such as CFAP70 and MYCBPAP."]
- Human sperm: [PMID:37934199 "In control sperm, TTC29 and CFAP70 immunostaining
  decorated the full length of the flagellum"]; CFAP70 is lost from sperm of a ZMYND12
  patient.

Conclusion: CFAP70 is a C2a-projection component of the axonemal central apparatus,
not an outer dynein arm subunit. The GOA `part_of outer dynein arm` (IDA, PMID:31621862)
reflects the 2018 model.

## Function

- Motility: [PMID:30158508 "When CFAP70 was knocked down in cultured mouse ependyma,
  reductions in cilia beating frequency were observed."] Chlamydomonas fap70 cells swim
  slowly. Mouse Cfap70 KO shows PCD-like phenotypes [PMID:42417609 "all three knockout
  strains exhibit distinct phenotypes related to primary ciliary dyskinesia (PCD),
  including hydrocephalus and sinusitis."]
- Sperm flagellum biogenesis (mouse): [PMID:37352829 "CFAP70 is required for the
  biogenesis of spermatid flagella partially by regulating the expression of
  OAT-associated proteins (e.g., QRICH2), assisting the cytoplasmic preassembly of the
  calmodulin- and radial spoke-associated complex (CSC), and controlling the manchette
  localization of axoneme-related proteins."] and [PMID:37458246 "the lack of CFAP70
  impairs sperm flagellum biogenesis and head shaping during spermiogenesis."]
  (37458246 is abstract only.)
- Human genetics: [PMID:31621862 "this work provides the first evidence that loss of
  CFAP70 function causes MMAF"] (abstract only); a nonsense p.R988X proband and
  truncation mouse model in PMID:37352829.

## Annotation decisions (summary)

- `outer dynein arm` (IDA) -> MODIFY to `axonemal central pair projection`
  (GO:1990718), a lateral location correction supported by PMID:33988244 and
  PMID:40473901. Comparator check: CFAP65 and MYCBPAP (C2a partners) carry
  GO:1990716 axonemal central apparatus in GOA; HYDIN carries GO:1990718.
- `axoneme` (IEA, ISS) -> MODIFY to the more specific GO:1990718.
- `cilium assembly` (IBA, ISS) -> MODIFY to `sperm flagellum assembly`: in mouse
  respiratory/ependymal cilia the KO alters beating rather than abolishing assembly,
  whereas sperm flagellum biogenesis fails.
- `ciliary basal body` (IDA, abstract-only PMID:31621862) -> UNDECIDED.
- `extracellular exosome` (HDA urine proteomics) -> MARK_AS_OVER_ANNOTATED.

## Review round 2 (PR 5062 automated review)

### Why no molecular function is asserted

CFAP43 and CFAP47 receive NEW `GO:0005200 structural constituent of cytoskeleton` in this
repository because their structures resolve the protein's own contacts within the
axoneme (CFAP47: domain-by-domain contacts with C1, HYDIN and C2 in PMID:40473901).
CFAP70 has no equivalent contact map: the mouse in situ model places a homodimer in C2a
[PMID:40473901 "We identified two major components of the C2a projections: CFAP65 and
CFAP70; the latter forms a homodimer involved in CA"], the dimer was built with
AlphaFold-assisted modelling, and in Chlamydomonas only the N-terminus has been placed
[PMID:33988244 "Additional experiments, such as localization of the C-terminus of FAP70 or
higher resolution single-particle cryo-electron microscopy, will be necessary to delimit
FAP70 within the C2 microtubule."]. The knockout data (C2a collapse) are interdependent
across CFAP70, CFAP65, MYCBPAP and CCDC108 and so show necessity rather than which
subunit supplies structure. GO:0005200 is therefore plausible but not asserted; this is
recorded in the first core function description.

### Cilium row made consistent with axoneme rows

`cilium` (IEA) changed from TOO_GENERAL to MODIFY -> GO:1990718 axonemal central pair
projection, matching the axoneme rows, since the same specific term entails both.

### Comparator checks (QuickGO annotation search, exact term, run 2026-10-16)

Query: `https://www.ebi.ac.uk/QuickGO/services/annotation/search?geneProductId=UniProtKB:<acc>&goId=<term>&goUsage=exact`.

- GO:1990716: CFAP65 (Q6ZU64) ISS + IEA; MYCBPAP (Q8TBZ2) ISS; HYDIN (Q4G0P3) ISS + IEA.
- GO:1990718: HYDIN (Q4G0P3) IEA only (GO_REF:0000107, Ensembl); CFAP65, MYCBPAP, SPAG16,
  SPAG17 have none. CFAP70 (Q5T0N1) has neither term. The review's claims hold; the
  HYDIN GO:1990718 support is electronic only, which the reason now states.
