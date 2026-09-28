# ASH1L evidence notes

## Initial manual review, 2026-09-28

Human ASH1L (UniProt Q9NR48) is a chromatin-associated SET-domain lysine methyltransferase. The normal seed has 29 GO annotations and two alternative products. The review preserves all source objects, qualifiers and product metadata. The two product records do not establish isoform-specific functions.

The normal gene fetch and publication fetches are recorded separately from the biological assessment. The ordinary deep-research command with its configured fallback returned no generated research file. The literature synthesis here is manual; it is not a provider-generated deep-research report. Existing publication and Reactome caches remain immutable. Four additional primary records were recovered through the normal fetcher: PMID:17923682, PMID:22939622 and PMID:24012418 are abstract-only; PMID:40044670 has XML full text. The actual records and their stated availability were inspected.

### Catalytic specificity and construct dependence

[PMID:26002201, Kinetic characterization of human histone H3 lysine 36 methyltransferases, ASH1L and SETD2](https://pubmed.ncbi.nlm.nih.gov/26002201/) provides direct human enzyme evidence in its structured abstract. Recombinant nucleosomes support ASH1L catalysis, whereas H3K36A nucleosomes do not. The authors report ASH1L mono- and dimethylation of H3K36, no H3K4 activity under their conditions, and trimethylation by SETD2 alone. The normal cache is abstract-only. Full Methods, quantitative kinetic tables and figure pixels were not accessed, so construct and assay details beyond the abstract are not invented.

[PMID:21239497, Crystal structure of the human histone methyltransferase ASH1L catalytic domain and its implications for the regulatory mechanism](https://pubmed.ncbi.nlm.nih.gov/21239497/) identifies a post-SET loop that limits access to the substrate pocket. The normal abstract reports stimulation by loop mutations and H3K36 specificity. The actual Figure 3 caption, additionally read on PubMed, separates wild-type, F2260A and hyperactive Q2265A: “The hyperactive mutant (Q2265A) is able to also produce H3K36 trimethylation.” It also reports activity on H3K4A but not H3K36A substrates. This is a real mutant result, not a false experiment. It does not establish routine trimethyltransferase activity for ordinary human ASH1L. An independent reader subsequently checked the indexed human catalytic-domain purification, HMT Methods and complete targeted K36 Results: recombinant human enzyme was tested with recombinant Xenopus or HeLa histone substrates. Complete article/supplement and figure-pixel review is not claimed.

Accordingly, the two existing H3K36 trimethyltransferase annotations are proposed for MODIFY to the dimethyltransferase activity, retaining their original EXP or IEA provenance. Generic histone methyltransferase, histone H3 methyltransferase and K36-specific activity rows receive the same refinement. This narrows existing assertions rather than appending redundant NEW rows. Mono- and dimethylation are described in prose as one catalytic function.

### H3K4 and H3K9 uncertainties

[PMID:17923682](https://pubmed.ncbi.nlm.nih.gov/17923682/) is a genuine historical human ASH1L H3K4 activity report. The PubMed abstract and figure captions were read, including chromatin occupancy, catalytic-domain assays and target-gene effects; the complete article body and original figure pixels were not read at this stage. Human HeLa/K562 observations must be distinguished from the mouse systems also used in the paper. These positive claims cannot be erased simply because the 2015 human assays support K36 specificity.

[PMID:24012418](https://pubmed.ncbi.nlm.nih.gov/24012418/) reports mouse macrophage Ash1l-dependent H3K4 methylation and A20 regulation. Its abstract was read. Full assay methods and figures remain unread. The two H3K4 annotations therefore remain UNDECIDED while the differing constructs, systems and substrate readouts are reconciled. The IBA is an ancestral-node assertion; donor counts are not an evidence-quality score, and its topology was not reconstructed here.

The H3K9 activity and monomethylation annotations are transferred or mapped from mouse Q99MY8. [PMID:22939622](https://pubmed.ncbi.nlm.nih.gov/22939622/) is an H3K9 monomethylation study, but its actual Ash1l-specific experiment or supplemental entry has not been read. Its abstract foregrounds Prdm3/Prdm16 in mouse fibroblasts; that is insufficient to claim a wrong-gene attribution. All four K9 rows remain UNDECIDED. Human K36 assays under one set of conditions do not refute every possible K9 substrate/cofactor context.

### DNA and chromatin engagement

[PMID:40044670](https://www.nature.com/articles/s41467-025-57556-5) separates reader functions from catalytic specificity. Its normal XML full text was subsequently read for the abstract, target Results and Figure 3–6 captions, human construct purification, binding/EMSA and KMT/HMT Methods. Mouse ES culture and human MV4-11 ChIP analysis methods were also checked. The human PHD recognizes H3K4me2/3; neighboring bromodomain/BAH regions bind DNA. Recognition of a pre-existing H3K4 modification is not evidence that the protein writes it. Human biochemical constructs and MV4-11 chromatin observations are distinct from mouse embryonic stem-cell differentiation experiments. Complete supplements and figure pixels remain unread.

This supports the existing DNA-binding and chromatin-binding annotations as mechanisms that position the writer. It does not establish sequence-specific DNA-binding transcription-factor activity. One catalytic core is proposed, with transcriptional regulation and chromatin remodeling as existing supported processes. No extra core is created merely for each reader domain.

### Localization and original-source limits

[PMID:10860993](https://pubmed.ncbi.nlm.nih.gov/10860993/) directly reports human intranuclear speckles and tight-junction localization using multiple antibodies and double immunofluorescence. Its normal abstract was read. The nuclear pool is part of the chromatin core. Tight-junction localization is retained as non-core; the authors' suggested adhesion-signaling role remains a hypothesis, not a process assertion.

The actual [ASH1L Human Protein Atlas target record](https://www.proteinatlas.org/ENSG00000116539-ASH1L/subcellular) lists supported nucleoplasm and nuclear bodies; the Golgi signal is uncertain. Only target text was read, not the microscopy pixels. The existing nucleoplasm row is accepted; nuclear body localization is kept as non-core. No new Golgi assertion is added.

The abstract-only cache of PMID:25593309 foregrounds ZMYND8, but the source is a screen. This does not show that ASH1L was untested. Nuclear localization is accepted on independent human evidence with the original source-specific assay deferred to its curator.

The short normal cache for Reactome R-HSA-4827383 names other methyltransferases and does not itself identify ASH1L. It is not treated as independent target-level experimental evidence. R-HSA-5638157 does name ASH1L and a dimethylation reaction. Neither short cached summary independently establishes all localization details. Existing nucleoplasm annotations are supported by the human localization evidence, with their original sources retained.

### Ontology and model checks

The official [GO:0046975 page](https://amigo.geneontology.org/amigo/term/GO:0046975) was read: it defines H3K36 methylation and explicitly lists GO:0140954, histone H3K36 dimethyltransferase activity, as an `is_a` child in molecular function. The direct AmiGO child request timed out, but the exact child definition was subsequently read in the official [ZFIN](https://zfin.org/GO:0140954) and [FlyBase](https://flybase.org/cgi-bin/cvreport.pl?id=GO%3A0140954) ontology records. It describes two successive methyl transfers to H3K36 and includes mono-/dimethyltransferase as a synonym. The [GO:0006338 page](https://amigo.geneontology.org/amigo/term/GO:0006338) includes histone-modifying activity through `part_of`. Retaining chromatin remodeling consequently does not imply ATP-dependent nucleosome movement.

No ASH1L/Q9NR48 entry was found in the local GO-CAM index. No pathway-completeness argument or NEW process term is proposed. Two incidental PANTHER exports from seeding carry unreviewed metadata and remain quarantined. No family identifier or official label is authored from their descriptive text.

### Open questions and useful experiments

- Reconcile the historical H3K4 reports with later K36-specific assays using matched human constructs, defined nucleosomes, catalytic-dead controls and product-resolved mass spectrometry.
- Inspect the exact mouse Ash1l H3K9 experiment before deciding whether its human transfer is justified.
- Compare ordinary human ASH1L and Q2265A using matched substrates and a product time course; distinguish mutant gain of trimethylation from ordinary mono-/dimethylation.
- Establish whether the junctional pool has a reproducible function beyond its reported localization.

All 29 annotations are adjudicated: 13 ACCEPT, 3 KEEP_AS_NON_CORE, 7 MODIFY and 6 UNDECIDED. There are no NEW rows. Both alternative products and every original source object are preserved. One H3K36 dimethyltransferase core is supported. Independent prospective consultation covered every row and the core; the final record receives a separate check after normal-source import.

### Full-text follow-up: chromatin binding and catalysis

The actual PMID:40044670 Results distinguish PHD recognition of pre-existing H3K4me2/3 from catalytic writing. Human bromodomain charge mutants lose or weaken binding to 147-bp 601 DNA in EMSAs. PHD–BAH binds nucleosomes and prefers extra linker DNA; the PHD and BAH form an integrated structural module. Recombinant human SET-containing constructs produce H3K36 mono-/dimethylation, and prior H3K4me3 reduces this activity under the tested conditions. Disrupting the PHD–H3K4me3 interaction increases catalytic activity in that assay. These observations substantiate the single writer core and its recruitment mechanism. They do not establish a separate sequence-specific transcription-factor function or resolve the unread mouse K9 assay.

The 2025 study uses J1 mouse ES cells for differentiation experiments and reanalyzes previously reported human MV4-11 ChIP-seq datasets; these are not one human differentiation experiment. Target Results and Methods were read, with figure captions but without independent figure-pixel or supplementary-file assessment. No new differentiation, proliferation or cancer process term is added. The author-repository record for PMID:22939622 yielded bibliographic metadata and abstract only; it supplied no Ash1l-specific assay details.

### 2026-09-28: first external review follow-up

The automatic mouse-to-human H3K4 writer transfer is now MARK_AS_OVER_ANNOTATED. Direct human substrate-specificity results in [PMID:26002201](https://pubmed.ncbi.nlm.nih.gov/26002201/) support this narrower decision. The conflicting historical human and mouse H3K4 claims remain visible; neither assay error nor an MLL1-based explanation is established. The H3K4 IBA remains UNDECIDED pending reconciliation with its actual ancestral placement.

The reviewer suggested GO:0140952 for H3K36 monomethylation, but the current [official record](https://amigo.geneontology.org/amigo/term/GO:0140952) names H3K27 dimethyltransferase activity. It is not appropriate here. [GO:0140954](https://amigo.geneontology.org/amigo/term/GO:0140954) defines successive methyl transfers from unmethylated H3K36 to the dimethylated product and includes a mono/dimethylase synonym. The existing term and single catalytic core already represent the supported chemistry; the affected reasons now make this explicit. No additional annotation or duplicate core is introduced.

The description now identifies the Trithorax family and MRG15 stimulation. These background mechanisms are stated in the Introduction of PMID:40044670; the cited earlier MRG15 structural papers were not independently reassessed. This is not a new MRG15-binding annotation. The paper also describes context-dependent repression, so the description does not generalize ASH1L as a universal antagonist of Polycomb.

Repeated workflow commentary has been shortened in the annotation reasons. Earlier notes and reference reviews retain the actual reading boundaries: no complete PMID:26002201 Methods, PMID:22939622 Ash1l-specific assay, PAINT tree reconstruction, supplementary-file or figure-pixel assessment is newly claimed. The Q2265A mutant result remains distinct from ordinary ASH1L.

Current decisions: 13 ACCEPT, 3 KEEP_AS_NON_CORE, 7 MODIFY, 5 UNDECIDED and 1 MARK_AS_OVER_ANNOTATED; 29 original source rows, two alternative products, one core and no NEW rows.
