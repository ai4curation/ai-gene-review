# ASS1 review notes

# ASS1 evidence audit, 2026-09-28

This initial audit examined all 79 original annotation reasons and the existing core function before revising the review. The existing draft has 29 ACCEPT, 41 KEEP_AS_NON_CORE, seven REMOVE, one MARK_AS_OVER_ANNOTATED and one MODIFY decision; these are provisional prior decisions, not endorsed results.

## Cached primary abstracts read

All 16 complete cached abstracts were read: PMID:12620389, 16189514, 17496144, 18473344, 19056867, 21106532, 21988832, 22658674, 23533145, 25416956, 27287393, 28587924, 28985504, 6194510, 7977368 and 8792870. Only 21988832, 23533145 and 25416956 report full text available in these caches; their target-level full-text records were not yet read at this stage. Reading an abstract is not verification of the individual assay underlying an annotation.

- PMID:8792870 describes recombinant wild-type human ASS1 and 12 mutant forms expressed in bacteria. Purified wild type resembles native human liver enzyme; tetramerization and catalysis have independent support beyond the self-interaction screens. PMID:18473344 examines recombinant human variants including substrate-affinity defects; PMID:27287393 examines 21 variants and in-vitro residual activity/substrate response. These are enzyme-function sources, not a basis for clinical advice. Independent official identity checks were planned.
- PMID:7977368 concerns mutations in ten Japanese patients and supports the established metabolic deficiency. PMID:6194510 provides the human cDNA sequence; its abstract does not by itself demonstrate cytosolic localization.
- PMID:12620389 identifies ARAF/CRAF partners in a screen; the complete abstract does not identify the ASS1-specific assay. PMID:17496144 principally concerns the NMRAL1/HSCARG NADP(H) sensor structure and mentions ASS regulation; exact interaction experiments remain to inspect. PMID:28587924 explicitly describes ASS1-PRMT7 yeast two-hybrid, pull-down and mutagenesis, but construct and species Methods had not yet been read. PMID:28985504 explicitly reports CLOCK-dependent ASS1 K165/K176 acetylation and circadian activity in human cells and mouse liver; full Methods remain unread.
- PMID:16189514, 21988832 and 25416956 are human interaction maps. Their overall validation rates do not establish the specific ASS1 self-pair assay. UniProt independently records homotetramerization and self-interaction.
- PMID:22658674 describes two complementary UV-crosslink approaches for the HeLa mRNA-bound proteome. Its screen scale does not establish poor methodological quality. The ASS1-specific record remains unread; the old LOW_QUALITY reference judgment and RNA-binding over-annotation rationale require reassessment.
- PMID:19056867 and 23533145 are urinary/extracellular-vesicle proteomics studies. ASS1 peptide-level records had not yet been read; do not describe their individual detection as independently verified.

## Additional official primary records

[PMID:18323623](https://pubmed.ncbi.nlm.nih.gov/18323623/), *Structure of human argininosuccinate synthetase*, DOI 10.1107/S0907444907067455: PubMed identity and complete abstract read. Reports human ASS1 crystal structure with citrulline and aspartate. The IUCr full-text link returned 403; no full Methods or figure inspection claimed. UniProt independently assigns its homotetramer evidence to this paper. New cache still needed if cited in YAML.

[PMID:7845368](https://pubmed.ncbi.nlm.nih.gov/7845368/), *Demonstration of argininosuccinate synthetase activity associated with mitochondrial membrane: characterization and hormonal regulation*, DOI 10.1007/BF00926075: complete official abstract and rat MeSH read. Rat liver outer-membrane-associated activity has cytoplasmic-enzyme-like kinetics. Development and hormones alter its subcellular distribution; this does not establish human mitochondrial-matrix import. Full Methods were not accessed.

[PMID:8867809](https://pubmed.ncbi.nlm.nih.gov/8867809/), *Argininosuccinate synthetase and argininosuccinate lyase are localized around mitochondria: an immunocytochemical study*, DOI 10.1002/(SICI)1097-4644(19960301)60:3<334::AID-JCB5>3.0.CO;2-X: official search record provided complete abstract, identity and rat MeSH (a subsequent ordinary page open returned reCAPTCHA). Immunoelectron microscopy places rat enzymes near the cytoplasmic face of the mitochondrial outer membrane; soluble cytoplasmic localization is compatible with this. No human assay, full Methods or image inspection claimed. Together these papers defeat the draft's blanket rejection of mitochondrial association solely because ASS1 is cytosolic; actual electronic donor scope still needs assessment.

## Endothelial functional experiments

[PMID:21106532 / PMC3024748](https://pmc.ncbi.nlm.nih.gov/articles/PMC3024748/): official identity, complete abstract, Methods and Results through Fig. 3's initial description were read (web lines 102–183). Later Results access returned reCAPTCHA; figure pixels and supplements were not examined. Human ASS1 was expressed in HUVECs; the comparator NOS3 overexpression construct was bovine. HAEC experiments used human ASS1/NOS3 siRNAs, scrambled controls and laminar shear stress at 12 dyn/cm2 for 24 h. Methods measured accumulated nitrite/nitrate and fluorescent THP-1 adhesion after TNF stimulation. Results support ASS1-dependent NO output and reduced monocyte adhesion, including NOS3 dependence; no claim of ASS1 directly synthesizing NO or sensing shear stress. These original IMP annotations can be retained as context-dependent consequences of the metabolic activity without turning adhesion into a separate core function.

## Curated resources and functional boundaries

Current local UniProt P00966 describes the ATP-dependent citrulline/aspartate ligation, cytosolic location, homotetramer and CLOCK regulation. Positive IntAct aggregate counts are ARAF 4, ASS1 self 3, NMRAL1 3 and PRMT7 9; these are aggregate counts, not proof of the original paper's exact experiments. The three disease/kinetic sources underlie the established enzyme function.

[Human Protein Atlas](https://www.proteinatlas.org/ENSG00000130707-ASS1/subcellular) explicitly reports supported cytosol and uncertain additional nucleoplasm, antibody HPA020934. Text read; image pixels and per-cell-line details not yet inspected. No new nuclear annotation proposed from uncertain staining.

[Reactome R-HSA-70635](https://reactome.org/content/detail/R-HSA-70635) lists the ASS1 ligation step within the human urea cycle. [R-HSA-70577](https://reactome.org/content/detail/R-HSA-70577) is explicitly cytosolic and models ASS1 tetramer:NMRAL1 dimer:NADPH catalysis. Its summary cites the human crystal study, NMRAL1 papers 17496144/18263583, and human liver purification. This is corroborating curated context; a separate primary NMRAL1 assay review was planned. Local Reactome caches must be obtained normally before YAML citations to them.

No matching P00966, ASS1 or Ass1 entry was found in the current local gocams/index.tsv search. This is a bounded local index observation, not evidence that no model exists elsewhere.

Preserve all original source objects/identifiers, qualifiers and evidence. Do not remove experimentally supported generic interactions for lack of specificity. Do not label uninspected interaction or RNA data erroneous. Distinguish direct catalytic participation in the urea/arginine pathway from pleiotropic development/response annotations, and distinguish genuine cytosolic enzyme association with the mitochondrial surface from matrix localization.


# ASS1 source-reading addendum, 2026-09-28

This addendum updates the earlier read boundaries without changing the original working notes or normal source files.

The complete cached PMID:23533145 paper has now been read. It describes pooled expressed-prostatic-secretion/urine exosome isolation, ultracentrifugation, DTT/sucrose washing and duplicate mass-spectrometric analyses. The cached main body does not identify ASS1/P00966. The supplemental target protein/peptide table remains uninspected, so the corresponding annotation remains UNDECIDED. Lack of a demonstrated vesicular function is not evidence of contamination.

The other exosome source, PMID:19056867, has a positive target-level closure. Two reviewers independently inspected the [original NIH/NHLBI laboratory database](https://esbl.nhlbi.nih.gov/UrinaryExosomes/), including its header, publication/instrument mapping and ASS1 row. It identifies argininosuccinate synthetase 1, gene ASS1, RefSeq NP_000041, and references 1 and 2; reference 2 is Gonzales et al., PMID:19056867. The header identifies healthy human urinary-exosome preparations. The displayed peptide count 20 is a database field shared across the listed references; no claim assigns all 20 to one experiment. Raw spectra, individual peptide sequences, intravesicular topology and exosomal enzyme activity were not independently checked. Retain the existing HDA annotation as contextual detection, KEEP_AS_NON_CORE. This source does not close PMID:23533145.

Current official AmiGO definitions and parent relationships were read for [identical protein binding, GO:0042802](https://amigo.geneontology.org/amigo/term/GO:0042802), [enzyme binding, GO:0019899](https://amigo.geneontology.org/amigo/term/GO:0019899), and [L-aspartate catabolic process, GO:0006533](https://amigo.geneontology.org/amigo/term/GO:0006533). The three original self-interaction rows already use identical protein binding; no replacement is needed. Their original interactome target experiments remain uninspected, while independent human purified-enzyme and structural studies support homotetramerization. PRMT7 and CLOCK are demonstrated catalytic partners, allowing enzyme-binding refinements without assigning their catalytic activities to ASS1. NMRAL1/HSCARG is described as a sensor lacking a complete catalytic site; enzyme-binding refinement for that partner is not established.

The existing aspartate/citrulline catabolic terms are retained in their actual ASS1–ASL pathway context. Aspartate carbon proceeds through argininosuccinate to fumarate; its nitrogen enters the urea-cycle route, and citrulline proceeds through argininosuccinate into arginine. This is not a rule that every enzyme consuming a substrate is involved in its catabolism. No new process term is proposed. The detailed human patient-genetics source PMID:7977368 is not misrepresented as the independent crystal/kinetic experiments.

The nuclear finding is supported by the 2024 primary [PMID:38858597](https://pubmed.ncbi.nlm.nih.gov/38858597/) and its [original full text](https://www.nature.com/articles/s42255-024-01060-5), independently assessed in the nuclear consultation. Human HCT116 microscopy and fractionation support context-dependent nuclear localization. The proposed single NEW is GO:0005634 nucleus, not a nuclear catalytic core or a DNA-repair/transcription/cell-cycle process assertion. The paper's correction, DOI 10.1038/s42255-024-01090-z, concerns author order. The isotope-tracing caveat about dehydrated malate potentially contributing to a fumarate signal is preserved and not generalized to negate separate localization observations. The uncertain HPA nucleoplasm staining is not the basis of this NEW.

The complete donor/interaction consultation records which historical MGI donor abstracts were actually read and which target experiments remain uninspected. No screen is judged low quality merely because it is high throughput. The prospective plan covered 79 unchanged source objects plus one nuclear-localization NEW, with 28 ACCEPT, 30 UNDECIDED, 18 KEEP_AS_NON_CORE, 3 MODIFY and 1 NEW decisions. Publication-cache recovery and final independent consultation remained prerequisites for authoring at that stage.


# ASS1 recovered source reading

The recovered normal publication records were inspected before import. The five abstract-only records and both complete Reactome summaries were read in full. PMID:38858597 has full XML; the reading covered its complete abstract, nuclear-localization Results/Figure 2 legend and targeted fractionation, western blot and immunofluorescence Methods. An initial broad extraction was truncated, so whole-paper reading is not claimed. Figure pixels, uncropped blots and supplements remain uninspected.

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


## 2026-09-29 — review follow-up

Reader-facing spacing and PMID formatting were corrected, and temporary agent-handoff details were removed from these notes while preserving the dated scientific reading limits. These editorial edits do not change annotation actions, original source fields, literal quotations or the core function. The quantitative inhibitor-binding evidence, mitochondrial localization wording and response-annotation decisions are undergoing separate reassessment.


### Quantitative binding and mitochondrial localization follow-up

The complete normal abstracts for PMID:11083085, PMID:7845368 and PMID:8867809 were read again, alongside the official PubMed/publisher abstracts for the first two. The toxic-substance row now records the millimolar inhibition constants and separates rat affinity capture from human enzyme inhibition; Ki-prime is not a measured equilibrium dissociation constant. Cellular toxicity remains unestablished. The outer-membrane row now explicitly distinguishes proximity imaging from the separate membrane-associated activity observation. Full separation controls and direct human localization were not inspected. Both existing annotations remain non-core with these limitations; solubility alone does not exclude peripheral membrane association.


### RNA-binding target evidence

The [original article and supplement](https://rnajc.ucsf.edu/sites/rnajc.ucsf.edu/files/CastelloArticlePlusSupplementalJune2012.pdf) for PMID:22658674 explicitly places ASS1 in the mRNA-interactome class of Table 1 (printed p. 1404; PDF page 12). The parsed table, capture/enrichment Results, Figure 1 legend and isolation Methods were inspected. Parsed table text was inspected; table images were not examined. This closes the previously uninspected target boundary. Row 75 is now KEEP_AS_NON_CORE; RNA-target specificity remains unestablished. Cache availability is kept distinct from this external full-text reading.


### Source-specific response and neuronal-location reassessment

The rat ortholog transfers were reconsidered individually using their mapped donor studies. Five additional annotations are retained as non-core: neuronal cell body, peptide-hormone response, steroid-hormone response, growth-hormone response and cellular amine response. The original human IEA source objects remain unchanged. Response terms retained here have target-specific observations in a functional metabolic context; expression changes with unresolved interpretation remain undecided rather than being rejected as false. Neither an ASS-specific knockout nor direct human replication is treated as a universal requirement.

The LPS parent and cellular child use different experiments (PMID:12589771 versus PMID:9879717); likewise, glucocorticoid activity in astrocytes (PMID:8923475) differs from dexamethasone-induced transcription in fetal hepatocytes (PMID:9395312). The cellular child studies do have cellular resolution. Their remaining uncertainty concerns functional interpretation, not the cell type or the mere absence of a knockout.

The following reading scope applies to this reassessment. Most donor papers were available as abstracts; limited publisher passages or parsed tables are identified explicitly. No uncached quotation was added to YAML supporting text.

- [PMID:10473900](https://pubmed.ncbi.nlm.nih.gov/10473900/): Previously read complete developmental Northern/run-on abstract; no full functional developmental paper claimed.
- [PMID:15698416](https://pubmed.ncbi.nlm.nih.gov/15698416/): Complete official indexed abstract. Rat LPS dose comparison; CUNS and ASS mRNA measured. Full Methods/figures unread.
- [PMID:9544996](https://pubmed.ncbi.nlm.nih.gov/9544996/): Complete official abstract. Perinatal rat intestine Northern/in-situ and ASS immunohistochemistry described; full Methods/images unread.
- [PMID:15257170](https://pubmed.ncbi.nlm.nih.gov/15257170/): Complete official abstract. Rat Dahl salt-sensitive/resistant liver mRNA study; no full Methods/images read.
- [PMID:9252090](https://pubmed.ncbi.nlm.nih.gov/9252090/): Complete official abstract. Rat liver intoxication slot-blot time courses after allyl alcohol/acetaminophen; full paper unread.
- [PMID:20452409](https://pubmed.ncbi.nlm.nih.gov/20452409/): Complete official abstract. Rat 28-day PFOA hepatic mRNA/protein study; full paper unread.
- [PMID:11686784](https://pubmed.ncbi.nlm.nih.gov/11686784/): Previously read complete official abstract; dietary rat zinc and cytosolic ASS activity. No complete Methods claim.
- [PMID:11083085](https://pubmed.ncbi.nlm.nih.gov/11083085/): Previously read complete official/cached abstract. Rat affinity capture versus recombinant human inhibition distinguished. The binding annotation was reassessed separately.
- [PMID:16168957](https://pubmed.ncbi.nlm.nih.gov/16168957/): Complete official abstract. Suckling-rat dietary spermine, ASS gene/protein changes; full paper unread.
- [PMID:16339744](https://www.ebm-journal.org/journals/experimental-biology-and-medicine/articles/10.1177/153537020523001104/pdf): Primary PDF parsed text: complete abstract, rat ovariectomy/estradiol animal/tissue Methods, Table 1 ASS spots, adjacent Results/Discussion. No table image or raw spectra inspected. Two ASS spots have reported fold changes 2.23 and 1.68.
- [PMID:12589771](https://pubmed.ncbi.nlm.nih.gov/12589771/): Previously read complete official abstract of rat RPE-J combined inflammatory treatment and arginine/NO context; not complete Methods or single-stimulus controls.
- [PMID:12445581](https://www.sciencedirect.com/science/article/pii/S0014299902025840): Complete official abstract plus indexed publisher Introduction, tissue-preparation passages, start of Results and target Discussion paragraph. Native rat gastric ASS/ASL/nNOS localization described in myenteric neurons and muscle-layer nerve fibers. Full antibody-control Methods, all Results and image pixels not read.
- [PMID:17938381](https://pubmed.ncbi.nlm.nih.gov/17938381/): Complete official abstract. Female rat SHR offspring, strain comparison and maternal citrulline intervention. No full Methods or ASS-specific perturbation read.
- [PMID:17900569](https://pubmed.ncbi.nlm.nih.gov/17900569/): Official indexed abstract beginning plus author-repository complete abstract: Activated microglia cells express argininosuccinate synthetase and argininosuccinate lyase in the rat brain after transient ischemia. Rat MCAO immunohistochemistry at 24/72/144 hours; full repository PDF closed and images not seen.
- [PMID:9688877](https://journals.physiology.org/doi/10.1152/ajpendo.1998.275.1.E79): Complete abstract and search-indexed original publisher Methods/Results/Discussion passages, including pASr11 ASS probe, female Wistar treatment groups, target ASS transcript results and functional CUNS. Direct page open returned 403; figure pixels not seen. Prednisolone increases ASS mRNA (68% versus pair-fed); GH reduces it; coordinated ureagenesis changes measured in identically treated groups. No isolated ASS intervention or human experiment.
- [PMID:8923475](https://pubmed.ncbi.nlm.nih.gov/8923475/): Previously read complete official/cached abstract of rat astrocytes, ASS enzyme activity after dexamethasone and variable cAMP response. Full condition-specific target results unread.
- [PMID:9618389](https://pubmed.ncbi.nlm.nih.gov/9618389/): Complete official abstract. Perinatal rat diaphragm ASS/ASL expression and NOS-directed force experiments. No full paper/images read.
- [PMID:19651254](https://pubmed.ncbi.nlm.nih.gov/19651254/): Complete official abstract. Maternal dietary UFA and three-day rat pup liver proteomics; full target table/Methods unread.
- [PMID:9879717](https://pubmed.ncbi.nlm.nih.gov/9879717/): Complete official abstract, independently rechecked. Rat alveolar macrophage LPS experiment measures ASS mRNA/protein and labeled-citrulline recycling. No full Methods claim.
- [PMID:9893939](https://pubmed.ncbi.nlm.nih.gov/9893939/): Complete official abstract; identified as a review discussing rat-hepatocyte glutamine regulation/cell swelling. Underlying primary target assay not read.
- [PMID:10353334](https://pubmed.ncbi.nlm.nih.gov/10353334/): Complete official abstract. Fetal rat brain aggregates, ammonium, RNase protection/in-situ ASS/ASL expression; no flux measurement or full Methods claimed.
- [PMID:9395312](https://pubmed.ncbi.nlm.nih.gov/9395312/): Complete official abstract, independently rechecked. Fetal rat hepatocyte dose/time transcription experiment, actinomycin/puromycin and nuclear run-on; glucagon enhances the dexamethasone response. No complete Methods claim.
- [PMID:8985169](https://pubmed.ncbi.nlm.nih.gov/8985169/): Complete official abstract. Cultured rat hepatocyte oleate/dexamethasone/carnitine conditions and ASS mRNA; full paper unread.
- [PMID:18457831](https://pubmed.ncbi.nlm.nih.gov/18457831/): Complete official indexed abstract: polyaspartoyl-L-arginine, rat aortic endothelial cells, ASS protein induction and functional NO/arginine-cycle endpoints; NOS/ASL inhibitors, not an ASS-specific intervention. Later direct PubMed reopen returned a stub; no complete Methods or image inspection claimed.
- [PMID:22658674](https://rnajc.ucsf.edu/sites/rnajc.ucsf.edu/files/CastelloArticlePlusSupplementalJune2012.pdf): UCSF-hosted primary article plus supplement, parsed PDF text. Main Table 1, printed p. 1404 / PDF page 12 (zero-based page 11), explicitly classifies ASS1 as mRNA interactome. Read Results pp. 1394–1396, main Methods In Vivo Isolation of HeLa RBPs (p. 1403), and Extended Experimental Procedures S1–S2 (PDF pages 15–16): capture, protein identification and enrichment analysis. Human HeLa, UV crosslinking, stringent oligo(dT) capture and RNase release. No ASS1-specific binding-site/CLIP validation or raw-spectra reanalysis. EMBL direct PDF open limited; UCSF supplied actual parsed text.
