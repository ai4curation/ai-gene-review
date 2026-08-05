# PTTG1 review notes

## Research provenance (2026-07-19)

- Refreshed the reviewed UniProt record and all 30 QuickGO rows with
  `just fetch-gene human PTTG1`.
- Cached all nine GOA-linked PMIDs with
  `just fetch-gene-pmids human PTTG1` and read every cached record. The cache
  contains full text for PMID:24781523, PMID:33961781, and PMID:34290405; the
  other six GOA-linked records are abstract-only.
- Ran `just deep-research-openscientist human PTTG1`. The first OpenScientist
  attempt reached the provider's 600-second timeout and produced no report. A
  second OpenScientist attempt was started while the primary-source review
  continued. No content is attributed to OpenScientist unless that retry
  produces a report.
- Cached and inspected three additional primary studies needed to resolve the
  dual inhibitor/activator biology: PMID:10411507, PMID:11371342, and
  PMID:23798554.
- GO identifiers used as authored replacements were checked against the current
  Gene Ontology: GO:0002020 (protease binding), GO:0140608 (cysteine-type
  endopeptidase activator activity), and GO:2000816 (negative regulation of
  mitotic sister chromatid separation).

## Biological synthesis

PTTG1 encodes human securin, a short, largely intrinsically disordered regulator
of the cysteine endopeptidase ESPL1/separase. The direct biochemical and
structural evidence converges on a dual role: PTTG1 binds separase as an
inhibitory pseudosubstrate before anaphase, but it is also required for full
separase activation/stability. APC/C-dependent degradation of securin at the
metaphase-to-anaphase transition releases separase to cleave cohesin.

- The foundational vertebrate study identifies human PTTG1 as securin and
  reports that a stable securin mutant blocks sister-chromatid separation:
  [PMID:10411507 "Human securin is identical to the product of the gene called
  pituitary tumor-transforming gene (PTTG)"] and [PMID:10411507 "expression of
  a stable Xenopus securin mutant protein blocked sister-chromatid separation
  but did not block the embryonic cell cycle"].
- Human loss-of-function evidence shows that securin is also required for
  separase competence and euploidy: [PMID:11371342 "The abnormal mitoses were
  associated with biochemical defects in the activation of separin, the
  sister-separating protease, rendering it unable to cleave the cohesin subunit
  Scc1 efficiently."]
- Direct inhibitor mechanism: [PMID:12194817 "securin inhibits separase by
  blocking the access of substrates to the active site of separase"].
- Structural mechanism: [PMID:34290405 "In both complexes, separase is
  inhibited by pseudosubstrate motifs that block substrate binding at the
  catalytic site and at nearby docking sites."] The same paper resolves a
  human separase-securin complex and identifies multiple securin motifs that
  occupy separase substrate-recognition sites.
- Independent activation and inhibition are supported in human cells:
  [PMID:23798554 "These data demonstrate that while the motif containing H(134)
  has a strong affinity for separase and is involved in inhibiting it, another
  domain(s) is involved in activating separase and has a weaker affinity for
  it."]
- PTTG1 is both nuclear and cytosolic. The original human cloning paper reports
  [PMID:9811450 "although hPTTG is mainly a cytosolic protein, it is partially
  localized in the nucleus"].
- The Reactome record for the direct complex states: [Reactome:R-HSA-2467798
  "PTTG1 sequesters ESPL1 and block its catalytic site, preventing it from
  cleaving centromeric cohesin and causing premature separation of sister
  chromatids"].

## Annotation decisions

- Accept both cysteine-type endopeptidase inhibitor annotations as the core
  molecular function, and accept separase-securin complex membership.
- Replace every generic `protein binding` annotation consistently with
  GO:0002020 `protease binding`. All six GOA rows name ESPL1 as the interacting
  partner; the replacement preserves the physical-interaction claim while
  avoiding an uninformative generic binding term. The inhibitor and activator
  consequences are captured separately by specific regulator terms.
- Replace the generic GO:0140677 `molecular function activator activity` with
  GO:0140608 `cysteine-type endopeptidase activator activity`. PMID:23798554 and
  PMID:11371342 support separase-specific activation. PMID:15929994 primarily
  characterizes intrinsic disorder and does not directly establish activation
  in its accessible abstract, so that citation is flagged as a poor match for
  this GOA claim rather than used as the sole support.
- Replace the broad InterPro2GO `chromosome organization` term with GO:2000816
  `negative regulation of mitotic sister chromatid separation`, which captures
  securin's direct pre-anaphase role.
- Keep the IBA homologous-chromosome-segregation annotation, the meiotic
  cohesion annotation, and spermatogenesis as non-core. These are biologically
  plausible meiotic/testis contexts but are secondary to the mitotic
  separase-control activity. PMID:9915854 provides expression and interaction
  evidence and concludes only that PTTG "may play a role in spermatogenesis".
- Accept nuclear, cytoplasmic, and cytosolic localization rows. These are
  mutually compatible pools, and the direct 1998 fractionation result supports
  both major compartments.
- Accept all seven Reactome cytosol rows. They are redundant but correspond to
  explicit cytosolic APC/C recognition, ubiquitination, degradation, or
  separase-sequestration reactions; none changes the core functional model.

## Remaining uncertainty

The timing and relative contribution of the separase-activating/chaperone role
versus pseudosubstrate inhibition in untransformed human tissues remain less
well defined than the inhibitory structure. Likewise, the GOA spermatogenesis
claim is based on expression and interaction evidence rather than a direct
human genetic perturbation.
