# SORL1 notes

## Review status

- First-pass review completed on 2026-06-19.
- `just fetch-gene-pmids human SORL1` completed successfully; all 34 PMID-backed publication caches were present after refresh.
- Falcon deep research was attempted with `timeout 180 just deep-research-falcon human SORL1 --fallback perplexity-lite`, but the process timed out and no provider deep-research artifact was written. These notes rely on cached UniProt, GOA, and publication files.
- `just validate human SORL1` passes cleanly.

## Functional synthesis

SORL1 encodes SORLA/LR11, a VPS10P/LDLR-family type I membrane sorting receptor. Its core biology is cargo binding and adaptor-dependent trafficking through trans-Golgi, endosomal, recycling-endosomal, lysosomal, and plasma-membrane routes.

For Alzheimer biology, the strongest functional axis is APP and amyloid-beta handling. The foundational APP paper supports interaction, Golgi/endosomal colocalization, and reduced amyloidogenic processing: [PMID:16174740 "sorLA acts as a sorting receptor that protects APP from processing into Abeta and thereby reduces the burden of amyloidogenic peptide formation"] A follow-up mechanistic paper supports the BACE/APP trafficking model rather than direct enzyme inhibition: [PMID:16407538 "sorLA acts as a trafficking receptor that prevents BACE-APP interactions and hence BACE cleavage of APP"] Adaptor-dependent retention/retrieval is supported by the GGA/PACS-1 study: [PMID:17855360 "sorLA acts as a retention factor for APP in trans-Golgi compartments/trans-Golgi network, preventing release of the precursor into regular processing pathways"]

SORL1 also binds and sorts amyloid-beta peptides directly. The lysosomal-sorting study supports a distinct amyloid-beta cargo function: [PMID:24523320 "Aβ binds to the amino-terminal VPS10P domain of SORLA"] and links it to lysosomal targeting: [PMID:24523320 "this receptor to direct lysosomal targeting of nascent Aβ peptides"] Endocytic recycling evidence supports an additional route by which LR11/SORLA alters amyloid output: [PMID:22621900 "LR11 modulates Aβ levels by promoting APP traffic to the endocytic recycling compartment"]

Many other SORL1 annotations are real cargo-specific biology but are not the core Alzheimer review focus. Examples include lipoprotein lipase trafficking [PMID:21385844 "LPL binds to SorLA in the biosynthetic pathway and is subsequently transported to endosomes"], GDNF/GFRA1/RET sorting [PMID:23333276 "SorLA acts as sorting receptor for the GDNF/GFRα1 complex, directing it from the cell surface to endosomes"], insulin receptor recycling [PMID:27322061 "SORLA acts as a sorting factor for the insulin receptor"], and HER2 recycling in cancer cells [PMID:31138794 "SORLA co-localizes with HER2 on the plasma membrane and in intracellular vesicles"].

## Annotation decisions

- Accepted cargo receptor activity, protein transporter activity, APP/amyloid-beta binding and processing terms, protein targeting/sorting/recycling terms, receptor-mediated endocytosis, and core Golgi/endosomal/plasma-membrane locations.
- Modified `aspartic-type endopeptidase inhibitor activity`: the evidence supports reduced BACE-dependent APP cleavage by trafficking, not direct BACE catalytic inhibition. Replacement terms are `negative regulation of amyloid precursor protein catabolic process` and `negative regulation of amyloid-beta formation`.
- Marked generic `protein binding` annotations as over-annotated because the useful biology is specific cargo receptor activity, amyloid-beta binding, lipoprotein binding, or cargo-specific sorting.
- Kept adipose/insulin, GDNF, cytokine, HER2/cancer, smooth-muscle, neuropeptide, and broad extracellular/exosomal/localization annotations as non-core.
- Marked cytosol, perinucleolar compartment, and neurofibrillary-tangle regulation as over-annotated; the nuclear-envelope lumen annotations were left `UNDECIDED` because the cached evidence does not allow full-text verification.

Final action distribution: 92 ACCEPT, 44 KEEP_AS_NON_CORE, 25 MARK_AS_OVER_ANNOTATED, 4 MODIFY, 3 UNDECIDED.

## Knowledge gaps and experiments

- The GO representation is still coarse: `cargo receptor activity` captures the receptor class, but does not distinguish APP/amyloid-beta cargo sorting from other SORL1 cargo programs.
- The largest mechanistic gap is whether Alzheimer-associated SORL1 variants selectively impair APP binding, amyloid-beta binding, adaptor recruitment, endosome-to-Golgi retrieval, or lysosomal delivery.
- Useful experiments would use endogenous SORL1 variant knock-ins in human neurons, with compartment-resolved live imaging and biochemical readouts for APP, BACE1, nascent amyloid-beta, and cargo-specific adaptor recruitment.

## 2026-06-20 Second-Pass Review Notes

Second-pass audit confirmed the existing action calls. No annotation actions were
changed. The YAML now records `reference_review` metadata for the main APP and
amyloid-beta trafficking anchors: PMID:16174740, PMID:16407538, PMID:17855360,
PMID:22621900, and PMID:24523320.

The remaining UNDECIDED calls are nuclear-envelope style localization
annotations whose cached evidence does not allow direct full-text verification.
They should remain UNDECIDED rather than being removed from incomplete evidence.

The core function remains SORL1 cargo receptor activity: APP/BACE1 trafficking,
APP retention/retrieval in TGN/endosomal routes, amyloid-beta binding through the
VPS10P domain, and lysosomal routing of amyloid-beta peptides. Other cargoes
remain important but are best treated as non-core cargo-specific extensions of
the same sorting-receptor biology unless the review question is about that tissue
or pathway.
