# Trh (rat, P01150) - manual literature synthesis

No deep-research provider was available for this review; this file was assembled by hand from
the cached publications in `publications/`, PubMed searches, and the UniProt record
`Trh-uniprot.txt`. Every claim carries a provenance tag.

## Identity, precursor structure and processing

- Rat pro-thyrotropin-releasing hormone (pro-TRH), 255 aa precursor; UniProt P01150, RGD:3903,
  GeneID 25569. [UniProtKB:P01150 "Belongs to the TRH family."]
- The cDNA cloned from rat hypothalamus encodes a ~29 kDa protein carrying five copies of the TRH
  progenitor Gln-His-Pro-Gly flanked by paired basic residues; mRNA is concentrated in the
  parvocellular paraventricular nucleus (PVN). [PMID:3079917 "This protein contained five copies of
  the sequence Gln-His-Pro-Gly flanked by paired basic amino acids and could therefore generate five
  TRH molecules."] [PMID:3079917 "These findings indicate that mammalian TRH arises by
  posttranslational processing of a larger precursor protein."]
- Hypothalamic processing is nearly complete, yielding TRH (pGlu-His-Pro-NH2) plus connecting
  peptides prepro-TRH(160-169) and (178-199); the olfactory bulb processes the precursor
  differently, leaving N-terminally TRH-containing extended forms. [PMID:2119297 "In extracts from
  the rat hypothalamus, TRH and two pro-TRH-connecting peptides, prepro-TRH-(160-169) and
  prepro-TRH-(178-199) were detected in molar ratios corresponding to those expected for a nearly
  complete processing of the prohormone molecule."]
- The precursor itself is not the active ligand; the active species is the amidated tripeptide.
  The gene product therefore functions by being processed in the regulated secretory pathway and
  released (UniProt: "Secreted").

## Molecular function: hormone / neuropeptide ligand of TRH receptors

- UniProt function: [UniProtKB:P01150 "Functions as a regulator of the biosynthesis of TSH in the
  anterior pituitary gland and as a neurotransmitter/ neuromodulator in the central and peripheral
  nervous systems."]
- Hypophysiotropic TRH neurons of the PVN control thyrotropin synthesis and release and so the
  hypothalamus-pituitary-thyroid (HPT) axis. [PMID:27515033 "TRH controls the synthesis and release
  of thyrotropin, which activates the synthesis and secretion of thyroid hormones"]
- Mouse Trh knockout: tertiary hypothyroidism with reduced pituitary TSH content, reversed by TRH
  administration. [PMID:10628753 "TRH is essential only for the postnatal maintenance of the normal
  function of pituitary thyrotrophs, including the normal feedback regulation of the TSH gene by
  thyroid hormone"]
- TRH receptor coupling is via Gq/11 (hippocampal interneurons). [PMID:16990402 "Because the effects
  of TRH were mediated via Galphaq/11, but were independent of its known downstream effectors, a
  direct coupling may exist between Galphaq/11 and K+ channels."]

## Extra-hypophysiotropic (neuromodulatory) actions, mostly exogenous-peptide pharmacology

- Feeding: third-ventricle TRH suppresses food intake, partly via hypothalamic neuronal histamine
  (TRH-R2 on tuberomammillary histamine neurons; TRH raises t-MH, HDC activity and HDC mRNA).
  [PMID:17760865 "These results indicate that hypothalamic neuronal histamine mediates the
  TRH-induced suppression of feeding behavior."] [PMID:17760865 "Microinfusion of TRH into the TMN
  increased t-MH content, histidine decarboxylase (HDC) activity and expression of HDC mRNA in the
  TMN."]
- Brainstem TRH instead stimulates food intake through vagal cholinergic ghrelin release; an
  intracisternal TRH antibody reduces natural refeeding, indicating an endogenous role.
  [PMID:16959836 "Natural food intake in overnight fasted rats was significantly reduced by ic TRH
  antibody, ic Y1 antagonist, and peripheral atropine."]
- Hippocampus: TRH increases GABA release by exciting interneurons [PMID:16990402 "TRH increases the
  excitability of interneurons to facilitate GABA release"] and inhibits K+-evoked glutamate and
  aspartate release from slices [PMID:16055093 "all three TRH doses significantly (P < 0.05)
  inhibited peak 50 mM [K(+)]-stimulated glutamate/aspartate release"].
- Pancreas: TRH is co-depleted with insulin by neonatal streptozotocin; perinatal TRH enhanced basal
  insulin secretion of adult nSTZ islets. [PMID:16118471 "Perinatal TRH treatment enhanced basal
  insulin secretion in vitro in nSTZ animals of both sexes"]
- Neurohypophysis: i.v. TRH modulates vasopressin and oxytocin content and release depending on
  hydration. [PMID:12369739 "TRH displays different character of action on vasopressin and oxytocin
  secretion in relation to the actual state of water metabolism."]
- Locomotion: TRH and its analogue TA-0910 are anti-ataxic in the Rolling mouse Nagoya
  (Cacna1a mutant) (PMID:8719807, abstract read via PubMed only); this is the source of the mouse
  IGI "adult walking behavior" row propagated to rat. It is a drug effect on another gene's mutant.

## Regulation of Trh expression / content (IEP rows)

- Hypoxia lowers hypothalamic TRH release [PMID:15726019 "We conclude that acute and chronic hypoxia
  exposure produces an inhibition of hypothalamic TRH secretion from the ME and PVN."]
- Ethanol and glucose drinking change limbic TRH content [PMID:15680480 "Ethanol consumption
  decreased TRH content and PPII activity in frontal cortex of male rats after 3-6 weeks."]
- Corticosterone raises brain TRH and TRH-like peptides [PMID:16293347 "Significant increases,
  ranging from 2- to 12-fold, in TRH or TRH-like peptide levels were observed in almost all brain
  regions studied at 4h after corticosterone injection."]
- These are changes in the gene's expression/peptide content, not processes performed by TRH.

## Localisation

- Secreted; stored in dense-core secretory granules of neurons before regulated release
  (UniProt "Secreted"; PANTHER IBA to secretory granule).
- PMID:3930986 detects TRH immunoreactivity in secretory granules, cytoplasm and nucleus of
  pituitary thyrotropes and lactotropes (target cells), which the authors interpret as internalised
  TRH. [PMID:3930986 "At the subcellular level, the reaction was detected within the cytoplasmic
  matrix, the secretory granules, and the nucleus but only occasionally at the plasma membrane."]

## Annotation-relevant observations from GOA comparators (QuickGO, 2026-10-28)

- Human TRH (P20396) carries GO:0007189 adenylate cyclase-activating GPCR signaling pathway by IDA
  (UniProt, 2025-07-07) from PMID:35940204, a cryo-EM study of the TSH receptor activated by TSH and
  the M22 autoantibody (PubMed abstract read). TRH is not studied in that paper; the rat ISO row
  derives from this human row.
- Analogous hypophysiotropic hormones carry a "positive regulation of <pituitary hormone> secretion"
  BP: human GHRH (P01286) GO:0060124 (IDA, IMP), human CRH (P06850) GO:0051461 (IBA, IDA). TRH has
  no GO:2000614 positive regulation of thyroid-stimulating hormone secretion row in human or rat.
