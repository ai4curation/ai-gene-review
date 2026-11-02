# BHLHE40 (DEC1 / STRA13 / SHARP2) review notes

No deep-research provider keys were available; this file records a manual literature
survey (Europe PMC searches, papers cached with `ai-gene-review fetch-pmid`).
UniProt: O14503 (human), mouse ortholog O35185.

## Identity and domain architecture

- 412 aa class E bHLH-Orange protein; bHLH domain 52-107 and Orange domain 142-175
  (UniProt FT, PROSITE-ProRule), PANTHER PTHR10985 (HES-related), InterPro HES_HEY.
- Cloned from Bt2cAMP-differentiated human chondrocytes [PMID:9240428 "a novel human
  cDNA for a basic helix-loop-helix (bHLH) protein (named DEC1)"]; mouse Stra13 cloned as
  a retinoic acid-inducible gene [PMID:9284045].
- Unlike HES proteins it lacks the C-terminal WRPW Groucho-binding motif
  [PMID:10737769 "Because Stra13 lacks the conserved WRPW motif for interaction with
  Groucho"].

## Molecular function: E-box DNA-binding repressor

- Binds class B CACGTG E-boxes as a homodimer [PMID:12297495 "Stra13 binds with high
  affinity to CACGTG class B E-box elements as a homodimer"].
- Represses DEC2 promoter via proximal E-box; DNA-binding mutants inactive
  [PMID:12624110 "The repression was observed with wild type DEC1 but not its DNA
  binding-defective mutants"].
- Represses mPer1 via DNA binding, not BMAL1 interaction [PMID:15193144 "providing
  direct evidence that DNA binding, rather than Bmal1 interactions, is responsible for the
  repression on the mPer1 promoter"].
- Arg65 needed for E-box binding, BMAL1 interaction and repression; DEC1-DEC2
  heterodimer by pull-down [PMID:15560782].
- ChIP/EMSA/reporter: binds E but not E' boxes [PMID:18411297].
- Repression mechanisms: HDAC1-dependent (autorepression) and HDAC-independent via TFIIB
  interaction (c-Myc repression) [PMID:10737769 "Stra13 expression is transcriptionally
  repressed and maintained at a low level in cells through a negative autoregulatory
  mechanism that is brought about by its interaction with the corepressor histone
  deacetylase (HDAC1)"].
- Corepressor of RXR and RXR heterodimers through an LXXLL motif [PMID:19786558 "DEC1 and
  DEC2 interacted directly with RXRalpha, and ligand addition enhanced their association";
  "an LXXLL motif in DEC1 and DEC2 is necessary for RXRalpha repression"]; IL-6 enhances
  DEC1-RXRalpha association [PMID:29234281].
- Context-dependent effects through p53: mouse Stra13 binds p53 and stabilizes it
  [PMID:17347673]; human DEC1 binds p53 on the MIC-1 promoter and attenuates p53
  transactivation of MIC-1 [PMID:22723347].

## Circadian clock

- Fifth clock-gene family; represses CLOCK/BMAL1-activated Per1; light-inducible in SCN
  [PMID:12397359].
- DEC autofeedback loop: CLOCK/BMAL activates Dec1 through three CACGTG E-boxes, and DEC1/2,
  PER and CRY repress it [PMID:14672706].
- Dec1-/- mice: slightly longer free-running period and faster re-entrainment
  [PMID:18411297 "Dec1-/- mice showed behavioral rhythms with slightly but significantly
  longer circadian periods under conditions of constant darkness and faster
  reentrainment to a 6-h phase-advanced shift of a light-dark cycle"].
- Clock-output targets: SHP/NR0B2 [PMID:28797635], ATP1B1 and blood pressure
  [PMID:30012868].

## Hypoxia

- HIF-1 target: functional HREs in the DEC1 promoter [PMID:12354771 "Because DEC1 and
  DEC2 are directly inducible by HIF-1, these transcription factors may be crucial for the
  adaptation to hypoxia"]; VHL/hypoxia-regulated and overexpressed in clear-cell renal
  carcinoma [PMID:11278694].
- Effector of hypoxic inhibition of adipogenesis by repressing PPARG2 (mouse)
  [PMID:11879638 "represses PPAR gamma 2 promoter activation and functions as an effector
  of hypoxia-mediated inhibition of adipogenesis"].
- Hypoxia induction is an expression response; I did not add a hypoxia process term.

## Immune functions (mostly mouse)

- Stra13-/- mice: defective CD4 T cell activation, late-onset autoimmunity
  [PMID:11668339].
- T cells: Bhlhe40 promotes GM-CSF and represses IL-10; required for EAE
  [PMID:24699451 "it positively regulates the production of GM-CSF and negatively
  regulates the production of IL-10"]; ChIP-seq peaks at Il3/Csf2 and Il10 loci.
- Mtb infection: essential repressor of Il10; binds +6 kb Il10 element [PMID:29773644].
- Macrophages: required cell-intrinsically for large peritoneal macrophage self-renewal;
  represses Maf/Mafb (ChIP peak at Maf promoter) [PMID:31061528]; with Bhlhe41 regulates
  alveolar macrophage self-renewal and identity [PMID:31414712].
- Efferocytosis-induced macrophage proliferation: Myc induces Bhlhe40, which represses
  c-Maf [PMID:34784501 "Bhlhe40 then represses the cell-cycling-inhibitor c-Maf to drive
  proliferation"]. This is one context of the wider LPM proliferation programme and is not
  treated as the gene's defining function.
- Tissue-resident memory CD8 T cells and TILs: Bhlhe40 sustains mitochondrial fitness
  [PMID:31533057].

## Localization and PTMs

- Mostly nuclear, with some cytoplasmic protein; SUMOylation at K159/K279 stabilizes it
  and enhances repression [PMID:21829689 "DEC1 is predominantly localized in the
  nucleus, but can also be found in the cytoplasm"]; ubiquitin/proteasome turnover
  [PMID:11278694].

## Curation decisions summary

- Core: RNA Pol II-specific DNA-binding transcription repressor activity at CACGTG E-boxes
  (GO:0001227, GO:0070888), negative regulation of Pol II transcription (GO:0000122) and
  circadian regulation of gene expression (GO:0032922); nucleus.
- 82 bare protein-binding rows: MODIFY to informative terms where a small-scale study
  supports one (RXRA → nuclear retinoid X receptor binding; p53 → p53 binding; BMAL1 → bHLH
  transcription factor binding), REMOVE for high-throughput Y2H, viral and UBC9 rows.
- IBA anterior/posterior pattern specification: HES-subfamily (segmentation clock)
  function, with no DEC-specific evidence and normal development in knockout mice →
  MARK_AS_OVER_ANNOTATED.
- NEW (conservative): transcription corepressor activity (RXR, IDA PMID:19786558);
  negative regulation of interleukin-10 production and positive regulation of
  macrophage proliferation (ISS from mouse; direct binding at Il10 and Maf loci shown by
  ChIP-seq).
