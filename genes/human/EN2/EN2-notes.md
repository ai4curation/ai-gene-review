# EN2 review notes

## Review scope and evidence limitations

- Manual review started 2026-07-14 from the seeded human GOA, UniProtKB
  `P19622`, cached publications, and official UniProt/QuickGO records.
- Automated deep-research providers are globally quota-blocked. No provider was
  retried and no provider-labelled report was created. These notes are the
  manual research record.
- Most developmental evidence for EN2 comes from mouse or other vertebrate
  orthologs. The review therefore distinguishes the conserved molecular
  activity of human EN2 from organism-level developmental phenotypes inferred
  from orthology.

## Product identity and intrinsic activity

- Human EN2 is a 333-aa, reviewed Engrailed-family homeobox protein. UniProt
  records a homeobox DNA-binding region at residues 244-303 and nuclear
  localization [UniProtKB:P19622, "Homeobox protein engrailed-2"; "SUBCELLULAR
  LOCATION: Nucleus"].
- The homeodomain and additional Engrailed conserved regions support a nuclear,
  sequence-specific transcription-factor role. In the MAP1B study, chick EN2
  was the source Engrailed protein used for biochemical transfer annotations;
  the paper reports that the MAP1B promoter has conserved homeoprotein/Foxa2
  sites and that the relevant promoter region is recognized by Engrailed- and
  Foxa2-containing nuclear extracts [PMID:12642491, "The MAP1B (Mtap1b)
  promoter presents two evolutionary conserved overlapping homeoproteins and
  Hepatocyte nuclear factor 3beta (HNF3beta/Foxa2) cognate binding sites";
  "the promoter domain containing HF1 and HF2 is recognized by cerebellum
  nuclear extracts containing Engrailed and Foxa2 and has regulatory functions
  in primary cultures of embryonic mesmetencephalic nerve cells"].
- EN2 can interact directly with FOXA2. The interaction maps to the Engrailed
  homeodomain and a region containing the PBX-binding domain
  [PMID:12642491, "Direct interaction was confirmed by pull-down experiments,
  and the regions participating in this interaction were identified."; "In
  Engrailed, two independent interacting domains exist: the homeodomain and a
  region that includes the Pbx-binding domain."]. The same study reports
  reciprocal, dose-dependent antagonism at the MAP1B promoter
  [PMID:12642491, "Foxa2 antagonizes the Engrailed-driven regulation of the
  MAP1B promoter, and vice versa."].
- An earlier study demonstrated direct Engrailed regulation of the MAP1B
  promoter, including conserved ATTA homeoprotein sites, by binding assays,
  cell transfection, and chick neural-tube electroporation
  [PMID:11331364, "These experiments demonstrate that MAP1B promoter is
  regulated by Engrailed in vivo. Moreover, they show that one promoter domain
  that contains all ATTA homeoprotein cognate binding sites common to the rat
  and human genes is an essential element of this regulation."]. The accessible
  full-text record shows context-dependent activation in cultured cells and
  repression in the chick neural tube; this supports retaining both positive
  and negative transcription-regulation transfers while not claiming either
  polarity as EN2's sole core activity.
- Human TF methylation-sensitive SELEX supplies direct human EN2 DNA-binding
  evidence in the GOA source dataset. The cached article explains the scale and
  assay class [PMID:28473536, "By analysis of 542 human TFs with
  methylation-sensitive SELEX (systematic evolution of ligands by exponential
  enrichment), we found that there are also many TFs that prefer CpG-methylated
  sequences."]. The article further identifies homeodomains as a major class
  whose DNA specificity can be affected by methylcytosine [PMID:28473536,
  "Most of these are in the extended homeodomain family."]. The cached prose
  does not reproduce the EN2 supplemental row, so no EN2-specific methylation
  preference is asserted here.

## Conserved developmental roles (non-core biological contexts)

- The mouse En1/En2 coding-sequence replacement experiment shows that En2 can
  supply En1 biochemical activity in the embryonic mid-hindbrain and that the
  differing mutant phenotypes primarily reflect expression pattern
  [PMID:7624797, "En-1 coding sequences were replaced with En-2 sequences by
  gene targeting. This rescued all En-1 mutant defects, demonstrating that the
  difference between En-1 and En-2 stems from their divergent expression
  patterns."]. This supports conservation of Engrailed activity, but it is not
  direct human developmental evidence.
- In mouse, En1 and En2 are jointly required for survival of mesencephalic
  dopaminergic neurons. The double-mutant/RNAi study attributes cell loss to
  apoptosis and a cell-autonomous requirement [PMID:15175251, "This
  disappearance is caused by apoptosis revealed by the presence of activated
  caspase 3 in the dying tyrosine hydroxylase-positive mutant cells."; "the
  demise of mDA neurons in the mutant mice is due to a cell-autonomously
  requirement of the engrailed genes"]. This supports the Ensembl orthology
  transfer for negative regulation of neuronal apoptosis as a non-core
  developmental/survival context.
- Mouse conditional genetics establishes a late role for En1/En2 in regional
  cerebellar foliation, after isthmic organizer activity and major output-cell
  specification. Both genes are required for vermis- and hemisphere-specific
  folia in the correct mediolateral position [PMID:20081196, "both En genes are
  required to ensure that folia exclusive to the vermis or hemispheres form in
  the appropriate mediolateral position"]. Mutants show altered granule-cell
  precursor layer thickness and fissure timing/position [PMID:20081196,
  "foliation is altered from the onset and is accompanied by changes in the
  thickness of the layer of proliferating granule cell precursors. In addition,
  the positioning and timing of fissure formation are altered."]. This is the
  strongest evidence for placing EN2 in the top-down cerebellum-development
  decomposition, but it remains a downstream developmental phenotype rather
  than the protein's core molecular activity.
- Expression analysis places mouse En2 broadly across the E17.5 cerebellar
  cortex, including Purkinje cells, granule-cell precursors, GABAergic
  interneuron precursors, and unipolar brush cell precursors
  [PMID:21431469, "En2 is broadly expressed throughout the cerebellar cortex at
  E17.5 and is present in all of the main neuronal cell types (excluding DCN
  neurons), including Purkinje cells (identified by LHX1/5 and/or RORα
  immunoreactivity), GCPs (identified by PAX6), GABAergic interneurons (PAX2-
  positive, which include Golgi, basket and stellate cell precursors), and
  unipolar brush cell precursors (TBR2 double labeling)."]. Expression alone
  does not establish a direct role in each cell type.

## Ontology and annotation decisions

- Official QuickGO definitions were checked on 2026-07-14 for the authored
  terms used below. `GO:0000981` is "DNA-binding transcription factor activity,
  RNA polymerase II-specific" and `GO:0000978` is "RNA polymerase II
  cis-regulatory region sequence-specific DNA binding". `GO:0021587` is
  "cerebellum morphogenesis".
- Broad `DNA binding` (`GO:0003677`) is modified to the sequence-specific Pol II
  cis-regulatory binding term already supported by IBA/ISS evidence.
- Broad `regulation of DNA-templated transcription` (`GO:0006355`) is modified
  to `regulation of transcription by RNA polymerase II` (`GO:0006357`), matching
  the more specific IBA annotation.
- HPA fibrillar-center and nucleolar localizations are retained as non-core
  observed localizations. Nucleoplasm, nucleus, and chromatin are consistent
  with the transcription-factor activity.
- Direction-specific activation, repression, and FOXA2 interaction annotations
  are retained because the source chicken EN2 experiments establish these
  context-dependent activities and the human Engrailed homeodomain is highly
  conserved. They are not split into separate core functions because the
  polarity depends on target and partner context.
- A new ISS proposal to `GO:0021587` is included to connect the human EN2 review
  to the top-down cerebellar foliation module. Its support is the mouse En2
  ortholog and PMID:20081196, and it is explicitly classified as non-core.

## Synthesis boundary

The core function is EN2's nuclear/chromatin-associated, sequence-specific
DNA-binding transcription-factor activity regulating RNA polymerase II
transcription. Neuron differentiation, neuronal survival, embryonic brain
development, and cerebellar regional foliation are biological outcomes of that
activity in particular developmental contexts, not additional intrinsic
molecular activities.

