# proB notes

## Evidence synthesis

- `file:ECOLI/proB/proB-uniprot.txt` identifies `P0A7B5` as E. coli K-12
  glutamate 5-kinase, EC 2.7.2.11, with RHEA:14877 for `L-glutamate + ATP =
  L-glutamyl 5-phosphate + ADP`.

- PMID:6319365 purified E. coli gamma-glutamyl kinase/ProB and assayed
  ATP-dependent kinase activity with glutamate, directly supporting
  `GO:0004349 glutamate 5-kinase activity` and ProB participation in
  L-proline biosynthesis.

- PMID:16337196 showed that wild-type E. coli G5K requires free Mg for
  activity, is tetrameric, and is regulated by proline. Deleting the C-terminal
  PUA fold left the enzyme active but changed Mg dependence, proline
  inhibition, and proline-triggered aggregation, supporting Mg and proline
  binding while arguing against a generic PUA-to-RNA-binding transfer for ProB.

- PMID:17069808 mapped E. coli G5K active-center residues required for
  catalysis, ATP binding, glutamate binding, and proline binding; the abstract
  is sufficient for those facets but not for the full EcoCyc Mg curation, which
  is still supported by PMID:16337196 and PMID:17321544.

- PMID:17321544 resolved E. coli G5K structures and described a tetrameric
  dimer-of-dimers architecture in which the AAK and PUA domains contact each
  other across the dimer and a negatively charged cavity hosts Mg ions.

- PMID:17321544 also noted that the G5K tetramer could position bacterial
  glutamate-5-phosphate reductase active centers close to the kinase active
  centers, supporting a substrate-channeling model for the unstable G5P
  intermediate. UniProt records possible ProA/ProB complex formation, but the
  direct physiological complex and channeling mechanism remain open.

- PMID:20970428 localized the proline feedback-inhibitor binding site and
  described the E. coli enzyme's dimeric functional unit. The older
  PMID:6319365 native-mass estimate implied self-association but not the final
  oligomeric stoichiometry.

- PMID:4598010 is abstract-only locally but explicitly describes E. coli proB
  blocks as early proline-biosynthesis lesions bypassed by arginine-pathway
  mutations, so the `GO:0055129 L-proline biosynthetic process` IMP row should
  be accepted rather than second-guessed.

- PMID:18304323 profiled the E. coli cytosolic fraction by LC-MS/MS and is the
  source of the EcoCyc cytosol IDA row for ProB. The abstract documents the
  cytosolic-fraction proteomics design; the ProB-specific assignment is in GOA.

## Annotation decisions

- Accepted all `GO:0004349 glutamate 5-kinase activity`,
  `GO:0055129 L-proline biosynthetic process`, cytoplasm/cytosol, Mg binding,
  and proline binding rows. Kept self-association rows as non-core.

- Kept `GO:0005524 ATP binding` as a non-core substrate-binding facet and
  modified `GO:0016301 kinase activity` to `GO:0004349 glutamate 5-kinase
  activity`, because both are true but generic facets of the specific
  ATP-dependent glutamate 5-kinase activity.

- Removed the InterPro-derived `GO:0003723 RNA binding` row: E. coli ProB's PUA
  fold modulates the kinase domain and oligomerization, and no cached
  ProB-specific evidence supports RNA binding.

## Deep research

No automated deep-research file was generated during this pass; curation used
the cached UniProt, GOA, PANTHER, and publication records.


## 2026-11-07 evidence re-audit

All original annotation payloads and row order are preserved. No NEW annotation was added. The catalytic reaction and proline-biosynthetic participation remain supported. Direct E. coli primary studies and newer experiments are distinguished from inferred KT2440 function.

The normal Falcon research attempt failed with HTTP 403 authentication/access error; no provider report was fabricated. Manual source review used the protected existing caches and normally fetched new publications.

PMID:39514317 (full text) challenges required ProA–ProB channeling: heterologous kinase replacements and overexpressed alternative reductases support E. coli growth; failed crosslinking alone is not universal proof of no interaction. ProA is reduced glutamyl-phosphate chemistry; spontaneous GSA cyclization supplies P5C. The computed GP half-life and diffusion times are calculations, not intracellular measurements. Native-locus monomeric-GFP fusions show dispersed cytoplasmic localization. Expression/purification used engineered BL21 derivatives, while growth experiments used K-12 BW25113 derivatives. No matched-protein complex requirement is imposed.

PMID:37511294 (full text) overturns the previous claim that no ProB binds RNA. K-12 ASKA-derived proB was recloned into pET21a with C-terminal His tag, expressed in BL21-Gold(DE3), and tested by SELEX/competition EMSA. Estimated KD >>10 micromolar, no mapped binding site, no established native target or RNA-regulatory function. The original RNA-binding row is retained as non-core intrinsic in-vitro capability.

PAINT loss checks reported no IRD/IKR on the target lineage. Existing abstract-only primary caches were not refreshed. Curated experimental annotations remain supported where independent evidence agrees; no target-table detail was invented. Complete validation, ontology snapshots and preservation proof are in the member-review audit and ignored existing-review logs.
