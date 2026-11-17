

## 2026-11-06 Bacillus comparative chemotaxis review

Identity: P24073, primary gene fliY, UniProt BACSU, strain 168, taxon 224308. Current primary names were checked explicitly because historical cheA/cheC/cheD aliases can refer to fliZ/fliP/fliY.

The reviewed accession is the strain 168 reference. The receptor and CheD mechanistic studies explicitly use OI1085-derived chemotactic laboratory strains; these are not relabeled as literal strain 168 assays. Conserved gene identity and curated strain 168 records support the functional synthesis, with no claim of a sequence-verified identical assay construct. PMID25313396 instead uses predominantly strain 3610; these experiments are identified as such.

FliY is a structural component of the Bacillus subtilis flagellar switch and a CheY-P phosphatase. Its N-terminal region binds CheY-P, its CheC-like catalytic region accelerates CheY-P hydrolysis, and its FliN-like C-terminal region contributes to the flagellar C-ring. FliY resets the chemotactic signal near the motor, while CheC provides a second native phosphatase and CheD-dependent adaptation feedback. Its contribution to flagellar assembly is distinct from the ion-driven torque-generating activity of the motor.

- [PMID:12920116 Bacillus subtilis hydrolyzes CheY-P at the location of its action, the flagellar switch.] Abstract-only cache; detailed claims limited to available evidence unless publisher full access is explicitly recorded.
- [PMID:14749334 Bacillus subtilis CheC and FliY are members of a novel class of CheY-P-hydrolyzing proteins in the chemotactic signal transduction cascade.] Abstract-only cache; detailed claims limited to available evidence unless publisher full access is explicitly recorded.
- [PMID:25313396 FlgM is secreted by the flagellar export apparatus in Bacillus subtilis.] Abstract-only cache; detailed claims limited to available evidence unless publisher full access is explicitly recorded.
- [PMID:33684668 Diversity of bacterial chemosensory systems.] Full cached text available.

The pristine review text, complete original non-review annotation payloads, inherited proposals and raw SHA-256 hashes are recorded in `.cache/module-audit-logs/chemotaxis-20261106/bacillus-baseline.json`. Every machine annotation is preserved. No raw UniProt or GOA file was edited. This was an existing review; inherited provider outputs were not regenerated. The inherited GO:0005515 NEW row at zero-based index 19 was retired because it is an uninformative authored proposal absent from frozen GOA; its full payload is preserved in the baseline and bacillus-retired-proposals.json. The other inherited NEW rows (GO:0009433 and GO:0070298) remain. The false native CheX assertion and assembly/secretion conflation were corrected.

No NEW biological-process annotation was inferred from necessity alone. New proposals, if any, identify missing experimentally grounded molecular activities. PAINT loss checks were run for all genes carrying IBA and found no lineage loss; donor count and target self-inclusion were not used as weaknesses.

Extension evidence [PMID:1447979 Identification and characterization of FliY, a novel component of the Bacillus subtilis flagellar switch complex.] supports a separate structural molecule activity proposal (GO:0005198), through physical switch-component identity and complementation as well as the null phenotype. This is an independent specific role, not reinstatement of the retired GO:0005515 proposal. The historical cheD complementation group in this paper refers to FliY, not modern CheD receptor deamidase.


## 2026-11-06 PR6100 round1 scientific follow-up

All pre-edit rows, original actions and source hashes are frozen in `.cache/module-audit-logs/chemotaxis-20261106/round1-bacillus-baseline.json`. No machine annotation payload or inherited authored proposal payload was changed. Every summary in this gene is now claim-specific.

Removed CheC-specific phosphatase-stimulation quotes and copied CheC reasons from FliY. PMID12920116 directly reports FliY CheY-P hydrolysis; PMID14749334 distinguishes constitutive FliY turnover from CheC adaptation. PMID30455280 supplies physical switch-assembly evidence for the structural/location claims, with strain3610/PY79 versus reference168 scope explicit.


## 2026-11-06 SFT prediction follow-up for PR6100 CI

All nine BioReason-Pro SFT predictions were independently assessed against primary findings. The GO:0044780 flagellum-assembly verdict changes from NPI to CNN: FliY supplies physical C-ring/switch assemblies, while motor-assembly complementation and the assembly-mutant evidence support participation beyond necessity alone. GO:0071978 swarming changes from LSP to CNN: swarming is a supported contextual behavior, not a less-specific version of general regulation of motility. Both claims are already annotated, so they are not novel predictions. The reference sequence is strain 168; the 2015/2019 native structural and swarming experiments used 3610-derived constructs/backgrounds. Conserved protein-role inference is retained without claiming a literal 168 swarming experiment or identical assay sequence.

Publisher full text of Calvo and Kearns, PMID:25313396, DOI:10.1128/JB.02324-14, was read at https://journals.asm.org/doi/10.1128/jb.02324-14 on 2026-11-06. The normal publication cache is abstract-only and was not changed. Two short verbatim excerpts from the publisher article:

- Methods, strain construction: “All strains are in the 3610 background unless otherwise noted.”
- Figure 4 caption: “Mutations in the fla-che operon abolish swarming motility.”

Figure 4 identifies DS5384 as the fliY mutant. The Results infer FliY among proteins needed for hook-basal-body completion. That conclusion is distinct from the smaller set sufficient for FlgM secretion. PMID:30455280 provides complementary physical interaction/cross-link evidence and rescue of E.coli motor assembly by the FliY C-terminal region; its intact switch architecture remains an experimentally constrained model. Neither paper is relabeled as an experiment on the strain 168 reference accession.

The other seven categories remain unchanged. Phosphatase and dephosphorylation are supported directly by PMID:12920116; basal-body LSP is justified by the more-specific C-ring refinement proposed in this review and verified ontology ancestry. Cytoplasm remains CNN: UniProt already specifies the cytoplasmic side by curated similarity, and PMID:30455280 measures soluble as well as flagellar membrane-associated FliY. C-ring is not a GO is_a/part_of descendant of cytoplasm in the retrieved QuickGO ancestry, so that is not used as an LSP argument. The cell-septum NPI retains the positive flagellar structural/localization evidence; speculative model-error explanations involving SpoA/FtsZ and claims about training membership were removed. The report's network/domain checks are supportive analyses, not independent microscopy or exhaustive exclusion of all secondary localization. Frozen GO:0071977 COR and GO:0009374 NPI ontology-pair judgments, including the raw mismatched labels, remain fixed.

No raw prediction ID, label, aspect, method, version or source-reference metadata changed. The main gene review, raw sources, provider artifacts and module science remain byte-identical. Detailed pre-edit hashes, per-row payload comparisons, validation logs and manifest are under `.cache/module-audit-logs/chemotaxis-20261106/fliy-prediction-ci/`.

## 2026-11-06 PR #6100 cell-septum prediction evidence correction

Removed the unsupported PATHWAY_CONTEXT_IGNORED error type: B. subtilis has a division septum, and the prediction-error mechanism is unknown. Restored the explicit flagellar-switch statement from PMID:23532838 alongside the Bacillus switch-assembly experiments in PMID:30455280. The former is comparative context, with Thermotoga structural work, not an extra Bacillus localization assay. Removed a methods-only OpenScientist quotation; the analysis method remains described in the summary. The NPI verdict and all nine raw prediction payloads remain unchanged. Clarified that the C-ring term is a proposed refinement in this gene review, rather than an exact pre-existing GOA term.
