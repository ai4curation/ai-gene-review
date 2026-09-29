# ASS1 review notes

# ASS1 evidence audit, 2026-09-28

These are working notes, not a completed review. Canonical gene/provider files and publication caches remain unchanged. Readiness snapshots are in this directory. All 79 original annotation reasons and the current core were read. The existing draft has 29 ACCEPT, 41 KEEP_AS_NON_CORE, seven REMOVE, one MARK_AS_OVER_ANNOTATED and one MODIFY decision; these are provisional prior decisions, not endorsed results.

## Cached primary abstracts read

All 16 complete cached abstracts were read: PMID:12620389, 16189514, 17496144, 18473344, 19056867, 21106532, 21988832, 22658674, 23533145, 25416956, 27287393, 28587924, 28985504, 6194510, 7977368 and 8792870. Only 21988832, 23533145 and 25416956 report full text available in these caches; their target-level full-text records were not yet read by root. Reading an abstract is not verification of the individual assay underlying an annotation.

- PMID:8792870 describes recombinant wild-type human ASS1 and 12 mutant forms expressed in bacteria. Purified wild type resembles native human liver enzyme; tetramerization and catalysis have independent support beyond the self-interaction screens. PMID:18473344 examines recombinant human variants including substrate-affinity defects; PMID:27287393 examines 21 variants and in-vitro residual activity/substrate response. These are enzyme-function sources, not a basis for clinical advice. Independent official identity checks were assigned to amer1.
- PMID:7977368 concerns mutations in ten Japanese patients and supports the established metabolic deficiency. PMID:6194510 provides the human cDNA sequence; its abstract does not by itself demonstrate cytosolic localization.
- PMID:12620389 identifies ARAF/CRAF partners in a screen; the complete abstract does not identify the ASS1-specific assay. PMID:17496144 principally concerns the NMRAL1/HSCARG NADP(H) sensor structure and mentions ASS regulation; exact interaction experiments remain to inspect. PMID:28587924 explicitly describes ASS1-PRMT7 yeast two-hybrid, pull-down and mutagenesis, but root has not read construct/species Methods. PMID:28985504 explicitly reports CLOCK-dependent ASS1 K165/K176 acetylation and circadian activity in human cells and mouse liver; full Methods remain unread.
- PMID:16189514, 21988832 and 25416956 are human interaction maps. Their overall validation rates do not establish the specific ASS1 self-pair assay. UniProt independently records homotetramerization and self-interaction.
- PMID:22658674 describes two complementary UV-crosslink approaches for the HeLa mRNA-bound proteome. Its screen scale does not establish poor methodological quality. The ASS1-specific record remains unread; the old LOW_QUALITY reference judgment and RNA-binding over-annotation rationale require reassessment.
- PMID:19056867 and 23533145 are urinary/extracellular-vesicle proteomics studies. Root has not read ASS1 peptide-level records; do not describe their individual detection as independently verified.

## Additional official primary records

[PMID:18323623](https://pubmed.ncbi.nlm.nih.gov/18323623/), *Structure of human argininosuccinate synthetase*, DOI 10.1107/S0907444907067455: PubMed identity and complete abstract read. Reports human ASS1 crystal structure with citrulline and aspartate. The IUCr full-text link returned 403; no full Methods or figure inspection claimed. UniProt independently assigns its homotetramer evidence to this paper. New cache still needed if cited in YAML.

[PMID:7845368](https://pubmed.ncbi.nlm.nih.gov/7845368/), *Demonstration of argininosuccinate synthetase activity associated with mitochondrial membrane: characterization and hormonal regulation*, DOI 10.1007/BF00926075: complete official abstract and rat MeSH read. Rat liver outer-membrane-associated activity has cytoplasmic-enzyme-like kinetics. Development and hormones alter its subcellular distribution; this does not establish human mitochondrial-matrix import. Full Methods were not accessed.

[PMID:8867809](https://pubmed.ncbi.nlm.nih.gov/8867809/), *Argininosuccinate synthetase and argininosuccinate lyase are localized around mitochondria: an immunocytochemical study*, DOI 10.1002/(SICI)1097-4644(19960301)60:3<334::AID-JCB5>3.0.CO;2-X: official search record provided complete abstract, identity and rat MeSH (a subsequent ordinary page open returned reCAPTCHA). Immunoelectron microscopy places rat enzymes near the cytoplasmic face of the mitochondrial outer membrane; soluble cytoplasmic localization is compatible with this. No human assay, full Methods or image inspection claimed. Together these papers defeat the draft's blanket rejection of mitochondrial association solely because ASS1 is cytosolic; actual electronic donor scope still needs assessment.

## Endothelial functional experiments

[PMID:21106532 / PMC3024748](https://pmc.ncbi.nlm.nih.gov/articles/PMC3024748/): official identity, complete abstract, Methods and Results through Fig. 3's initial description were read (web lines 102–183). Later Results access returned reCAPTCHA; figure pixels and supplements were not examined. Human ASS1 was expressed in HUVECs; the comparator NOS3 overexpression construct was bovine. HAEC experiments used human ASS1/NOS3 siRNAs, scrambled controls and laminar shear stress at 12 dyn/cm2 for 24 h. Methods measured accumulated nitrite/nitrate and fluorescent THP-1 adhesion after TNF stimulation. Results support ASS1-dependent NO output and reduced monocyte adhesion, including NOS3 dependence; no claim of ASS1 directly synthesizing NO or sensing shear stress. These original IMP annotations can be retained as context-dependent consequences of the metabolic activity without turning adhesion into a separate core function.

## Curated resources and functional boundaries

Current local UniProt P00966 describes the ATP-dependent citrulline/aspartate ligation, cytosolic location, homotetramer and CLOCK regulation. Positive IntAct aggregate counts are ARAF 4, ASS1 self 3, NMRAL1 3 and PRMT7 9; these are aggregate counts, not proof of the original paper's exact experiments. The three disease/kinetic sources underlie the established enzyme function.

[Human Protein Atlas](https://www.proteinatlas.org/ENSG00000130707-ASS1/subcellular) explicitly reports supported cytosol and uncertain additional nucleoplasm, antibody HPA020934. Text read; image pixels and per-cell-line details not yet inspected. No new nuclear annotation proposed from uncertain staining.

[Reactome R-HSA-70635](https://reactome.org/content/detail/R-HSA-70635) lists the ASS1 ligation step within the human urea cycle. [R-HSA-70577](https://reactome.org/content/detail/R-HSA-70577) is explicitly cytosolic and models ASS1 tetramer:NMRAL1 dimer:NADPH catalysis. Its summary cites the human crystal study, NMRAL1 papers 17496144/18263583, and human liver purification. This is corroborating curated context; primary NMRAL1 assay review is assigned to alx3. Local Reactome caches must be obtained normally before YAML citations to them.

No matching P00966, ASS1 or Ass1 entry was found in the current local gocams/index.tsv search. This is a bounded local index observation, not evidence that no model exists elsewhere.

Preserve all original source objects/identifiers, qualifiers and evidence. Do not remove experimentally supported generic interactions for lack of specificity. Do not label uninspected interaction or RNA data erroneous. Distinguish direct catalytic participation in the urea/arginine pathway from pleiotropic development/response annotations, and distinguish genuine cytosolic enzyme association with the mitochondrial surface from matrix localization.


# ASS1 source-reading addendum, 2026-09-28

This addendum updates the earlier read boundaries without changing the original working notes or normal source files.

The complete cached PMID23533145 paper has now been read by root. It describes pooled expressed-prostatic-secretion/urine exosome isolation, ultracentrifugation, DTT/sucrose washing and duplicate mass-spectrometric analyses. The cached main body does not identify ASS1/P00966. The supplemental target protein/peptide table remains uninspected, so the corresponding annotation remains UNDECIDED. Lack of a demonstrated vesicular function is not evidence of contamination.

The other exosome source, PMID19056867, has a positive target-level closure. Root and alx3 independently inspected the [original NIH/NHLBI laboratory database](https://esbl.nhlbi.nih.gov/UrinaryExosomes/), including its header, publication/instrument mapping and ASS1 row. It identifies argininosuccinate synthetase1, gene ASS1, RefSeq NP_000041, and references1,2; reference2 is Gonzales et al., PMID19056867. The header identifies healthy human urinary-exosome preparations. The displayed peptide count20 is a database field shared across the listed references; no claim assigns all20 to one experiment. Raw spectra, individual peptide sequences, intravesicular topology and exosomal enzyme activity were not independently checked. Retain the existing HDA annotation as contextual detection, KEEP_AS_NON_CORE. This source does not close PMID23533145.

Current official AmiGO definitions and parent relationships were read for [identical protein binding, GO:0042802](https://amigo.geneontology.org/amigo/term/GO:0042802), [enzyme binding, GO:0019899](https://amigo.geneontology.org/amigo/term/GO:0019899), and [L-aspartate catabolic process, GO:0006533](https://amigo.geneontology.org/amigo/term/GO:0006533). The three original self-interaction rows already use identical protein binding; no replacement is needed. Their original interactome target experiments remain uninspected, while independent human purified-enzyme and structural studies support homotetramerization. PRMT7 and CLOCK are demonstrated catalytic partners, allowing enzyme-binding refinements without assigning their catalytic activities to ASS1. NMRAL1/HSCARG is described as a sensor lacking a complete catalytic site; enzyme-binding refinement for that partner is not established.

The existing aspartate/citrulline catabolic terms are retained in their actual ASS1–ASL pathway context. Aspartate carbon proceeds through argininosuccinate to fumarate; its nitrogen enters the urea-cycle route, and citrulline proceeds through argininosuccinate into arginine. This is not a rule that every enzyme consuming a substrate is involved in its catabolism. No new process term is proposed. The detailed human patient-genetics source PMID7977368 is not misrepresented as the independent crystal/kinetic experiments.

The nuclear finding is supported by the 2024 primary [PMID38858597](https://pubmed.ncbi.nlm.nih.gov/38858597/) and its [original full text](https://www.nature.com/articles/s42255-024-01060-5), independently assessed in the nuclear consultation. Human HCT116 microscopy and fractionation support context-dependent nuclear localization. The proposed single NEW is GO:0005634 nucleus, not a nuclear catalytic core or a DNA-repair/transcription/cell-cycle process assertion. The paper's correction, DOI10.1038/s42255-024-01090-z, concerns author order. The isotope-tracing caveat about dehydrated malate potentially contributing to a fumarate signal is preserved and not generalized to negate separate localization observations. The uncertain HPA nucleoplasm staining is not the basis of this NEW.

The complete donor/interaction consultation records which historical MGI donor abstracts were actually read and which target experiments remain uninspected. No screen is judged low quality merely because it is high throughput. The prospective v3 plan covers79 unchanged source objects plus one nuclear-localization NEW, with28 ACCEPT,30 UNDECIDED,18 KEEP_AS_NON_CORE,3 MODIFY and1 NEW decisions. Source59's exact normal cache import and final independent consultation remain prerequisites for canonical authoring.


# ASS1 recovered source reading

Read from the verified Source59 archive (SHA256 `1ebb96dd20858c012aff9ac6b98552855a1cfdccd28f4b514de44dcbb92d8bec`), before canonical import. The five abstract-only records and both complete Reactome summaries were read in full. PMID:38858597 has full XML; root read its complete abstract, nuclear-localization Results/Figure 2 legend and targeted fractionation, western blot and immunofluorescence Methods. An initial broad extraction was truncated, so whole-paper reading is not claimed. Figure pixels, uncropped blots and supplements remain uninspected.

- PMID:7845368 explicitly studies rat liver; membrane-associated activity varies with development and hormonal conditions. It does not establish a constitutive human mitochondrial-matrix enzyme.
- PMID:8867809 localizes soluble enzymes adjacent to the cytoplasmic surface of the outer mitochondrial membrane; the abstract alone does not establish organism. Previously checked official organism provenance remains separate.
- PMID:11083085 distinguishes rat affinity capture from recombinant human inhibition. Human inhibition is measured at millimolar concentrations; the abstract explicitly leaves cellular toxicity significance unresolved.
- PMID:18263583 supports an HSCARG/NMRAL1 association and inhibition of ASS1, not a new catalytic activity on ASS1. HSCARG RNAi apoptosis is not automatically an ASS1 apoptosis annotation.
- PMID:18323623 is a human substrate-bound structure. The abstract establishes citrulline/aspartate binding and comparison to bacterial enzymes; complete structural Methods remain unread.
- Reactome R-HSA-70577 describes cytosolic ASS1 tetramer catalysis with NMRAL1 regulation. R-HSA-9956517 distinguishes candidate/member variant alleles and residual activities; its short event title does not justify universal complete loss of activity for every variant.

PMID:38858597 directly supports the proposed human nuclear-location annotation. Endogenous HCT116 staining is supported by cytosol/nucleus fractionation; lamin/H3 and MEK/GAPDH/tubulin markers are reported, with mitochondrial contamination controls in the p53 comparison. Figure 2 separates three human imaging experiments, four fractionation experiments and five p53-comparison samples. Normal mouse hepatocyte localization is additional evidence, not relabelled as human. The Methods specify ASS1 antibody ab124465 and nuclear enrichment with repeated washes; immunofluorescence uses DAPI and confocal imaging. Basal human nuclear signal increases after doxorubicin. IPO7 association and perturbation are compatible with import but do not establish ASS1 as an import receptor. Nuclear fumarate production involves ASS1 together with ASL; no direct ASS1 lyase or chromatin-enzyme activity is inferred.

The previously checked publisher correction remains limited to its actual scope. No new process annotation is proposed from this paper.


## Final source closure and synthesis

The eight additional normal source caches were recovered and independently checked before final authoring. Each reference records its actual cache availability and the separately bounded scientific reading. The original 79 source assertions, order and qualifiers are preserved; one human nuclear-localization assertion is appended. No new process or second catalytic core is proposed. Decisions: 28 ACCEPT, 30 UNDECIDED, 18 KEEP_AS_NON_CORE, 3 MODIFY and 1 NEW. The original deep-research report and artifacts remain unchanged.
