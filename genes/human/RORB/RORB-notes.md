# RORB notes

**Provenance note:** Provider deep research for RORB failed (Falcon returned HTTP 402
Payment Required; Perplexity is not configured). No `RORB-deep-research-*.md` file exists.
This manual synthesis replaces it. It is built from the UniProt record (Q92753), the cached
publications in `publications/`, and PubMed E-utilities searches used to locate key primary
papers, which were then cached with `just fetch-pmid`.

## Identity and structure

- RORB (RAR-related orphan receptor B; NR1F2; historic name RZR-beta) is a nuclear
  receptor of the NR1 subfamily, with a C4-type zinc-finger DNA-binding domain (Pfam
  PF00105; InterPro IPR001628, IPR044101 NR_DBD_ROR) and a ligand-binding domain (PF00104).
  PANTHER PTHR45805:SF6 "NUCLEAR RECEPTOR ROR-BETA".
- Two isoforms come from alternative promoters: isoform 1 (RORbeta1, Q92753-1) and
  isoform 2 (RORbeta2, Q92753-2, the displayed sequence). They differ only at the N-terminus.
  [file:human/RORB/RORB-uniprot.txt "Event=Alternative promoter usage; Named isoforms=2;"]

## Molecular function: monomeric DNA-binding transcription factor

- Binds RORE half-sites as a monomer: [PMID:7935491 "We show here that the RZRs bind as
  monomers to natural retinoid response elements formed by (A/G)GGTCA half-sites."] and an
  A/T 5' extension improves binding [PMID:7935491 "a T-residue in the -1 position of this
  motif greatly enhances the DNA binding affinity of RZRs"].
- Constitutive transactivation: [PMID:7935491 "On monomeric as well as dimeric binding
  sites, RZRs show constitutive transactivational activity"].
- LBD structure: [PMID:11689423 "We present the crystal structure of the ligand-binding
  domain (LBD) of RORbeta containing a bound stearate ligand and complexed with a coactivator
  peptide."]; [PMID:11689423 "In the crystal, the monomeric LBD adopts the canonical
  agonist-bound form."]
- Retinoids as inverse agonists: [PMID:12958591 "ATRA and related retinoids inhibit ROR beta
  but not ROR alpha transcriptional activity"]; [PMID:12958591 "Our results identify ROR beta
  as a retinoid-regulated nuclear receptor, providing a novel pathway for retinoid action."]
- Human RORB was included in a genome-scale HT-SELEX study of TF DNA-binding specificity
  (PMID:28473536); RORB is not named in the main text, so the IDA is accepted on the
  curator's reading of the supplementary data.
- Target gene: Opn1sw (S opsin), with CRX synergy [PMID:16574740 "RORbeta (retinoid-related
  orphan receptor beta) activates the S opsin gene (Opn1sw) through binding sites upstream of
  the gene."]; [PMID:16574740 "activates the Opn1sw promoter modestly alone but strongly in
  synergy with the retinal cone-rod homeobox factor (CRX)"].
- Nuclear localization: [PMID:27352968 "The wild-type protein was detected in the nucleus as
  expected; in contrast, no mutant protein was detected in the nucleoplasm"].

### Melatonin

The RZR/ROR family was once proposed to bind melatonin. That proposal was later withdrawn
and is not part of the current view. In RORbeta-knockout mice, pineal melatonin rhythms and
melatonin-induced phase shifts are normal: [PMID:17303680 "We conclude that the RORbeta
nuclear receptor is not involved in either the rhythmic production of pineal melatonin or in
mediating phase shifts of circadian rhythms by melatonin"]. RORB has no seven-transmembrane
domain, so GO:0008502 melatonin receptor activity (a GPCR-type receptor activity in practice)
and the GPCR signaling inference built on it are not supported.

## Biological roles (mostly mouse genetics)

- **Retina, rods:** [PMID:19805139 "Rorb(-/-) mice lacking retinoid-related orphan nuclear
  receptor beta lose rods but overproduce primitive S cones that lack outer segments."];
  [PMID:19805139 "Rorb directs rod development and does so at least in part by inducing the
  Nrl-mediated pathway of rod differentiation."]
- **Retina, cones:** [PMID:16574740 "RORbeta-deficient mice fail to induce S opsin
  appropriately during postnatal cone development."]
- **Retina, interneurons (isoform RORbeta1):** [PMID:23652001 "a distinct retinoid-related
  orphan nuclear receptor β1 (RORβ1) isoform encoded by the retinoid-related orphan nuclear
  receptor β gene (Rorb) is critical for both amacrine and horizontal cell differentiation in
  mice."]; [PMID:23652001 "RORβ1 and Foxn4 synergistically induce Ptf1a expression"].
- **Knockout phenotype overall:** [PMID:9670004 "RORbeta-/- mice display a duck-like gait,
  transient male incapability to sexually reproduce, and a severely disorganized retina that
  suffers from postnatal degeneration."]
- **Circadian period:** [PMID:9670004 "under conditions of constant darkness, RORbeta-/-
  mice display an extended period of free-running rhythmicity."]; confirmed in another
  background [PMID:17303680 "RORbeta(C3H)(-/-) mice showing a significant increase in
  circadian period (tau)"]. This is a downstream phenotype. It is unclear whether RORB acts
  in the core clock or through retinal/SCN development.
- **Neocortex layer IV / barrels:** [PMID:21799210 "in vivo overexpression of RORβ is
  sufficient to induce periodic barrel-like clustering of cortical neurons."]; [PMID:21799210
  "RORβ expression levels control cytoarchitectural patterning of neocortical neurons during
  development"].
- **Bone:** [PMID:22189870 "Rorβ inhibited Runx2-dependent activation of a Runx2-reporter
  construct."]; overexpression in MC3T3-E1 cells [PMID:22189870 "These cells displayed
  markedly suppressed bone nodule formation as well as reduced osteocalcin and osterix gene
  expression."]. This is a cell-line overexpression result; I treat it as non-core.
- **Human disease:** heterozygous loss-of-function variants and deletions cause generalized
  epilepsy, often with absences, sometimes with intellectual disability [PMID:27352968 "Our
  data support the role of RORB gene variants/CNVs in neurodevelopmental disorders including
  epilepsy, and especially in generalized epilepsies with predominant absence seizures."].

## Interaction annotation

The GO:0005515 IPI (PMID:23555304) comes from a circadian yeast two-hybrid screen
[PMID:23555304 "we detected interactions between DEC1/2 and CRY1/2, between CLOCK and
RORβ/γ"]. The partner is mouse CLOCK (O08785), and RORB was a strong auto-activator as bait
[PMID:23555304 "RORB (C3) and PPP2CA (G1) showed strong auto-activation of all reporters"].
No functional consequence is shown, so the protein binding term is removed as uninformative.
The interaction itself is not disputed.

## Alzheimer disease context (selective vulnerability)

Leng et al. 2021 (PMID:33432193) used snRNA-seq of caudal entorhinal cortex and identified
RORB as a **marker** of excitatory neurons that are depleted early in AD
[PMID:33432193 "We identified RORB as a marker of selectively vulnerable excitatory neurons in
the entorhinal cortex"]. The link to RORB's own function is explicitly a hypothesis:
[PMID:33432193 "we hypothesize that the vulnerability of RORB-expressing excitatory neuron
subpopulations in different brain regions may be caused by gene expression programs driven by
RORB and potentially other subtype-determining transcription factors."]

**Assessment:** In the material reviewed here, nothing ties RORB *activity* (DNA binding,
target-gene regulation, retinoid modulation) causally to tau vulnerability. There is no
RORB knockdown/overexpression in a tauopathy model, no RORB target-gene set tested for
vulnerability, and no human genetic association of RORB with AD in the sources read. RORB
currently labels the vulnerable population (layer II/III-like entorhinal excitatory neurons).
It does not explain why those neurons are vulnerable. GO annotation for RORB should therefore
carry nothing AD-related. This is recorded as a suggested question/experiment in the review.

## Curation summary

- Core MF: nuclear receptor activity (GO:0004879), with sequence-specific RORE binding.
- Core BP: positive regulation of transcription by RNA pol II; retinal rod and cone
  development; amacrine cell differentiation (isoform 1).
- Removed: melatonin receptor activity (IBA), GPCR signaling pathway (IEA inferred from it),
  protein binding (IPI).
