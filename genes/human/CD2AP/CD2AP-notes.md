# CD2AP curation notes

## 2026-06-19

- Deep-research attempt with `just deep-research-falcon human CD2AP --fallback perplexity-lite` timed out after 180 seconds with no generated research artifact, so this manual review uses cached UniProt, GOA, PANTHER family, and publication evidence.
- CD2AP is best treated as an SH3-domain scaffolding/adaptor protein that links membrane and junctional proteins to actin-rich cortical structures. The original CMS/CD2AP paper reports that the protein is cytoplasmic, colocalizes with F-actin and p130(Cas) in membrane ruffles and leading edges, and that ectopic expression changes actin cytoskeleton organization [PMID:10339567 "functions as a scaffolding molecule with a specialized role in regulation of the actin cytoskeleton"].
- Core localization annotations are cytoplasm, actin cytoskeleton/filamentous actin, ruffle, leading edge, plasma membrane/cell periphery, vesicle/endosomal compartments, and junctional structures. UniProt summarizes CD2AP as acting between membrane proteins and actin cytoskeleton, anchoring the podocyte slit diaphragm to actin, and participating in epithelial junction formation.
- Homodimerization and multimeric SH3-mediated complexes are supported. The structural paper states that CD2AP/CMS family endocytic adaptors engage multiple effectors and can couple cargo trafficking to the cytoskeleton [PMID:17020880 "couple cargo trafficking with the cytoskeleton"], and reports that CD2 and Cbl-b peptides mediate multimerization of CMS SH3 domains [PMID:17020880 "can mediate multimerization of N-terminal CMS SH3 domains"].
- The broad `protein binding` annotations should not be accepted as core terms. Several are real interaction observations, but CD2AP's informative molecular role is adaptor/scaffold activity, SH3/proline-rich partner recognition, actin association, or specific complex context rather than generic protein binding.
- Epithelial junction evidence is strong. A full-text JCB paper reports that SH3BP1 formed a complex with JACOP/paracingulin and CD2AP, and that both scaffold proteins were required for normal Cdc42 signaling and junction formation [PMID:22891260 "CD2AP, a scaffolding protein; both were required for normal Cdc42 signaling and junction formation"]. This supports anchoring junction, actin filament organization, and negative regulation of small GTPase signaling annotations.
- CD2AP is also part of the submembrane actin/junction module through CapZ. The same paper states that CD2AP is part of the submembrane actin cytoskeleton and binds/regulates CapZ [PMID:22891260 "CD2AP, a protein that is part of the submembrane actin cytoskeleton and binds and regulates CapZ"].
- Podocyte slit diaphragm localization is biologically central for CD2AP in vivo, even though several slit-diaphragm details in the current GOA set are electronically transferred. I accepted slit diaphragm/anchoring junction context because it is consistent with UniProt and the established renal disease association.
- Neuronal axon/dendrite and synapse annotations are plausible Alzheimer/endosomal context but are not the primary evolved function of CD2AP. The RIN3 Alzheimer paper shows that RIN3 recruited BIN1 and CD2AP to early endosomes and that RIN3/CD2AP expression affected APP cleavage/trafficking in neuronal models [PMID:32552912 "RIN3 recruited BIN1(bridging integrator 1) and CD2AP (CD2 associated protein), two other AD risk factors, to early endosomes"]. I kept axon/dendrite/synapse context non-core rather than making it the defining function.
- The tau secretion annotation from PMID:27044754 is experimental but the cached record is abstract-only and the abstract names FRMD4A rather than CD2AP. Following the project rule not to overrule curators from incomplete evidence, I marked this annotation UNDECIDED rather than removing it [PMID:27044754 "Individual silencing of ten common late-onset Alzheimer's disease risk genes"].
- High-throughput cadhesome, exosome, AD network, and interactome annotations are useful context but not core molecular function evidence. Cadherin binding from E-cadherin proximity proteomics is over-specific for CD2AP because the paper describes a large cadhesome proximity/interactome resource rather than direct CD2AP cadherin binding [PMID:25468996 "isolate and identify 612 proteins in the vicinity of E-cadherin's cytoplasmic tail"].

## 2026-06-20 Second-Pass Review Notes

Second-pass audit confirmed the existing action calls and reference-review
coverage. No YAML changes were needed in this pass.

The single UNDECIDED annotation remains GO:0050714 positive regulation of
protein secretion from PMID:27044754. The cached record is abstract-only and
foregrounds FRMD4A rather than exposing the CD2AP-specific experimental result.
Because the annotation is experimental, it should remain UNDECIDED rather than
be removed without full-text or supplementary-data review.

The core function remains SH3-domain scaffold/adaptor activity linking membrane,
endocytic, junctional, and slit-diaphragm partner complexes to actin-rich
cortical structures. Alzheimer relevance should be represented through
endosomal trafficking modules involving RIN3/BIN1/CD2AP and APP/tau-related
cellular phenotypes, not as generic protein-binding function.
