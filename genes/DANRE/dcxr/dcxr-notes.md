# dcxr (Q567K5): evidence and exact-input prediction review

The generic oxidoreductase prediction is correct but less precise than the established DCXR-like assignment. The function paragraph instead transfers a bacterial FabG fatty-acid-synthesis reaction across the SDR family, assigning a different substrate class and carrier-protein context.

## Input identity and functional boundary

Q567K5 is a 244-residue zebrafish dcxr product. It aligns without gaps to the 244-residue human DCXR Q7Z4W1, with 169 identical residues. All three reference catalytic positions 136, 149 and 153 are conserved, as are most annotated NADP-contact residues. The selected PANTHER assignment is PTHR44252:SF3, while human DCXR is SF2; the official SF3 label is D-ERYTHRULOSE REDUCTASE-RELATED. That label alone cannot overturn the conserved sequence and PAINT inference or establish an alternative substrate. The emitted donor Q9X248 is Thermotoga FabG.

## Biological evidence

- [PMID:11882650 — Molecular characterization of mammalian dicarbonyl/L-xylulose reductase and its localization in kidney.](https://pubmed.ncbi.nlm.nih.gov/11882650/): Purified mammalian DCXR proteins reduce alpha-dicarbonyls and interconvert xylitol and L-xylulose; this supports ortholog-based chemistry rather than a zebrafish assay.

> homotetramers with NADPH-linked reductase activity for alpha-dicarbonyl
> compounds, catalyzed the oxidoreduction between xylitol and l-xylulose


> which is involved in the uronate cycle
> of glucose metabolism

## Exact non-GO claims

The complete emitted record is preserved in [dcxr-protnlm-source.json](dcxr-protnlm-source.json). Assessments below address the selected protein product; evidence on longer products is identified explicitly.

### Protein name

> Uncharacterized protein

UNSCORED: “Uncharacterized protein” has no ProtNLM evidence tag in the returned name field and provides no specific functional hypothesis. It is retained in the raw source rather than treated as a model-origin claim.

### Function

> Catalyzes the NADPH-dependent reduction of beta-ketoacyl-ACP substrates to beta-hydroxyacyl-ACP products, the first reductive step in the elongation cycle of fatty acid biosynthesis

PLI (CS 0; PARALOG_OVERANNOTATION). The donor is a bacterial FabG beta-ketoacyl-ACP reductase. Q567K5 instead has the full-length DCXR-like sequence and conserved catalytic architecture supporting soluble L-xylulose/carbonyl reduction. Related NADPH-dependent SDR chemistry does not establish ACP recognition or membership in fatty-acid-chain elongation. This is not a claim that animals lack all ACP-dependent fatty-acid synthesis; it is a distinction between the two enzyme branches. [PMID:11882650](https://pubmed.ncbi.nlm.nih.gov/11882650/); [sequence comparison](dcxr-bioinformatics/RESULTS.md); [donor](dcxr-fabg-prediction-donor.json).

## Emitted GO claims

All 1 emitted GO claims are individually assessed in [dcxr-protnlm-predictions-review.yaml](dcxr-protnlm-predictions-review.yaml).

## Family integration

PTHR44252 includes related small-carbonyl reductases whose substrate boundaries need primary enzymology. Human and fish occupy different PANTHER subfamilies despite a gap-free alignment and conserved catalytic residues. The biological inference rests on the sequence plus experimentally characterized DCXR chemistry and the existing phylogenetic judgment, not on renaming the official family or assuming every SDR is FabG.

## Evidence limits

No purified Q567K5 assay or target-specific compartment study was found. The 2002 mammalian biochemical report is abstract-only in the cache but explicitly states the assayed substrates. The genuine Falcon synthesis is useful for ortholog enzymology, with cofactor preference, tetramerization and tissue distribution kept distinct from direct zebrafish measurements. No kinetic constants or exclusive physiological substrate are assigned.

Exact sequence mapping: [dcxr-bioinformatics/RESULTS.md](dcxr-bioinformatics/RESULTS.md). Global alignments can place nonhomologous alternative tails opposite gaps or distant residues; only conserved segments and explicitly retained feature intervals support functional transfer.
