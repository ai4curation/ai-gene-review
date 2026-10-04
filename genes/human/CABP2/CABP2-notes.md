# CABP2 evidence and review notes

## Scope and identity

Human CABP2 is UniProt Q9NPB3, HGNC:1385 and NCBI Gene 51475. All 49 normal source assertions, their qualifiers and partner identifiers, and both reviewed product records are preserved. The products are L-CaBP2/Q9NPB3-1 and S-CaBP2/Q9NPB3-2. The normal short-product deletion at residues 15–71 is distinct from pathogenic truncations. The 61-residue alternative region described for mouse CaBP2 in the discovery paper is not substituted for the current human product records. Computationally mapped sequences are not additional reviewed products.

The review assigns 9 ACCEPT, 39 KEEP_AS_NON_CORE and 1 UNDECIDED decisions. No NEW annotation is proposed. One calcium-channel regulator core integrates calcium sensing, membrane association and hearing; these features are not split into redundant cores.

## Calcium binding and channel regulation

[PMID:10625670](https://pubmed.ncbi.nlm.nih.gov/10625670/) reports human, mouse and bovine cloning and recombinant biochemical experiments. CaBP2 exhibits calcium-sensitive purification behavior, stimulates CaMKII and inhibits GRK5 in vitro, while the authors explicitly leave physiological effector colocalization unresolved. These assays do not assign kinase activity to CaBP2. Bacterial N-myristoyltransferase modifies CaBP2; myristoylation is not CaBP2's own catalytic function. The CHO GFP experiments concern CaBP1 splice forms and are not used as CaBP2 localization evidence.

[PMID:22981119](https://pubmed.ncbi.nlm.nih.gov/22981119/) connects human CABP2 variants with hearing impairment and tests human CaBP2 with rat CaV1.3 alpha1 in HEK293T cells. The engineered p.Phe164* construct is a surrogate for the predicted splice-associated p.Phe164Serfs*4 product, not its exact sequence. At matched protein levels the surrogate retains partial suppression of calcium-dependent inactivation, rather than being completely inactive. Purified bacterial WT and truncated proteins have different calcium-binding thermodynamics by ITC. COS7 exon trapping tests human variant splicing, not protein abundance in a patient's inner ear.

The 2012 assay also found lower peak current density with WT CaBP2. The refined HEK293/hSK3-1 experiment in [PMID:28183797](https://pubmed.ncbi.nlm.nih.gov/28183797/), using a corrected channel clone and a viability-supporting potassium channel, did not reproduce that decrease. The authors raise cell viability and selection as a possible explanation. The review therefore does not make reduced or increased peak current amplitude a universal CaBP2 mechanism.

In native mouse inner hair cells, loss of Cabp2 increases calcium-channel inactivation while leaving current density, activation range and gross synapse numbers unchanged under the tested conditions. The room-temperature analysis resolves increased voltage-dependent inactivation; its calcium-dependent component showed only a nonsignificant trend. The broad [GO:0005246 calcium channel regulator activity](https://amigo.geneontology.org/amigo/term/GO:0005246) is appropriate, without asserting a proven native CDI-specific defect or a uniform activation shift. Calcium binding is independently demonstrated by target ITC experiments and belongs within this regulatory unit.

The mouse study also reports reduced spontaneous and sound-evoked spiral ganglion neuron firing. Maintaining synaptic channel availability is the proposed link between channel regulation and sound encoding. Capacitance measurements did not directly show reduced exocytosis and actually increased with long depolarizations; a possible extrasynaptic contribution remains interpretive. The c.466G>T human allele's nonsense-mediated decay was inferred, not measured. Human genetics, heterologous constructs and native mouse physiology are kept distinct.

## Localization and retinal specificity

The title of [PMID:19338761](https://pubmed.ncbi.nlm.nih.gov/19338761/) foregrounds CaBP7/8, but its Methods and Results explicitly include tagged human CaBP2 in differentiated Neuro2A cells. CaBP2 associates with the plasma membrane and a perinuclear region resembling the Golgi. The more specific syntaxin-6/VSVG TGN colocalization and transmembrane-domain perturbations concern CaBP7/8. They are not transferred to CaBP2. Golgi and perinuclear annotations are retained with these model and morphology limits. Membrane association is coherent with the channel-regulatory role.

The 2017 LacZ reporter and RT-PCR establish mouse hair-cell expression; unsuccessful antibody localization attempts do not provide an image of endogenous CaBP2 protein at a particular membrane compartment. No figure images or supplementary tables were inspected in these papers.

The complete indexed official abstract for [PMID:27822497](https://pubmed.ncbi.nlm.nih.gov/27822497/) reports altered ganglion-cell light responses in mouse Cabp2 knockouts despite preserved gross retinal and synapse morphology. Full text and images were not recovered; no normal cache is present, and this paper is not added as a YAML citation or quotation. It supplies explicitly external context for the retained broad visual-perception annotations alongside curated ortholog evidence. Apparently intact scotopic electroretinograms in the 2017 paper are a different readout and do not negate the reported ganglion-response phenotype.

[GO:0007602 phototransduction](https://amigo.geneontology.org/amigo/term/GO:0007602) concerns intracellular conversion of absorbed photons into a molecular signal, under signal transduction and detection of light stimulus. The inspected CaBP2 evidence does not independently resolve its own photon-conversion step or settle the PAINT node placement, so this assertion remains UNDECIDED. The original node and Cabp4 descendant evidence are preserved. Neither a paralog donor, a short donor list nor the lack of a human experiment is treated as evidence that the inference is false. The plasma-membrane IBA's target self-source is legitimate descendant evidence, not circularity.

## Protein interactions and policy

All 33 HuRI-derived IPI assertions from [PMID:32296183](https://pubmed.ncbi.nlm.nih.gov/32296183/) are retained as non-core. Each exact GOA partner, including isoform suffixes, matches the UniProt IntAct edge list. The complete abstract and selected binary-screening/retesting framework were read in the independent consultation. Individual target supplementary cells were not inspected. Dataset-level MAPPIT/GPCA benchmarking and NbExp counts are not presented as partner-specific orthogonal or native-tissue validation.

This follows the user's standing instruction to retain supported generic binding as non-core, recorded in the [published project policy](https://github.com/ai4curation/ai-gene-review/blob/3eb5f8979787f246e82ecaadcb5fc6e49507ff4c/projects/CLINGEN_MENDELIAN.md). The interactions alone do not establish CABP2 regulation of each partner or transfer a partner's catalytic activity. No finer unsupported adapter or enzyme function is invented.

## Source access and research provenance

The cached sources for PMID:10625670, PMID:19338761, PMID:22981119 and PMID:28183797 provide full text. The existing PMID:32296183 cache is preserved. Full-text flags describe availability, not a claim that every paragraph or image was independently inspected.

The complete abstracts and selected unique Methods/Results/Discussion supporting the decisions were read, including the full load-bearing channel experiments and relevant Methods in both modern mechanism papers. Ten short YAML quotation entries match the normal caches, with repeated uses counted: 11 words from PMID:10625670, 17 from PMID:19338761, 4 from PMID:32296183, 14 from PMID:22981119 and 20 from PMID:28183797.

One installed normal Falcon attempt with its configured perplexity-lite fallback failed with DNS errors and produced no provider research output. These manual notes are not represented as provider-generated research. All 49 source assertions have been manually assessed, including the explicit unresolved phototransduction inference. The review remains DRAFT while retaining that uncertainty and the standing-policy binding advisories.

Normal validation, including references, GOA consistency and authored GO terms, passed with 33 expected generic-binding policy warnings and no errors. The unresolved IBA has explicit UNRESOLVED propagation metadata; this does not claim that its PAINT node placement was independently reconstructed.

## 2026-10-03: reviewed record

The independently approved review passed full normal canonical validation and status reporting, retaining DRAFT and 33 standing-policy binding advisories. All 49 source assertions, both named products and source-cache bytes are preserved. The standard [CREATE history record](../../../history/genes/human/CABP2/2026-10-03T201721Z-codex-22ff89.yaml) passed history validation.

## 2026-10-03: retinal evidence follow-up

The source-access statements in the initial review above describe the earlier checkpoint. A subsequently recovered normal full-text cache for [PMID:27822497](https://pubmed.ncbi.nlm.nih.gov/27822497/) now supersedes the earlier abstract-only, external-access limitation for that paper. Its exact bibliographic identity and complete abstract were checked, and selected unique Methods, Results and Discussion were read. Figure images and supplements were not inspected.

The experiments used mouse retinal whole mounts and cone-dominated light stimulation. Cabp2 loss reduced excitatory light-response amplitude and modestly slowed ON-alpha ganglion-cell responses; tested OFF-transient responses were not significantly altered. The study also reports preserved gross retinal/ribbon morphology. Its antibody cross-reactivity was investigated using Cabp1/Cabp2 knockout controls; that boundary matters when interpreting localization. These data support the existing broad visual-perception annotations through mouse ortholog evidence and curator judgment. They do not establish human retinal physiology or identify a particular native retinal channel target for CaBP2.

Both visual-perception rows now cite PMID:27822497 as positive evidence. PMID:28183797 is removed from their positive support, while its apparently intact scotopic ERG remains a contextual caveat in the reasons. PMID:27822497 itself reports unchanged ERG b-waves in Discussion as data not shown. Ganglion-cell synaptic currents and ERG provide different circuit readouts, so the preserved ERG does not erase the observed ganglion phenotype. The description now explicitly attributes the retinal evidence to mouse ortholog studies. The exact phototransduction step and PAINT node placement remain unresolved.

All 49 machine-sourced assertions, their actions, both named products, the auditory channel-regulator core and the 10 prior reference entries are preserved. One additional reference and one 14-word Results quotation are added; all 10 earlier quotation entries are unchanged. Calcium sensing remains within the integrated regulatory core. No additional annotation or change to the unresolved phototransduction decision is introduced.

### Retinal follow-up application

The independently approved candidate passed full normal canonical validation, status reporting, targeted rendering and standard EDIT history validation. DRAFT retains 33 expected standing-policy binding advisories. All 49 source assertions and actions, both products, the core, earlier sources and history are preserved. See the [retinal follow-up history](https://github.com/ai4curation/ai-gene-review/blob/main/history/genes/human/CABP2/2026-10-03T232702Z-codex-1f111a.yaml).
