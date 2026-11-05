# NTSR1 (human) — curation notes

UniProt: P30989. HGNC symbol NTSR1 (neurotensin receptor 1, "NTS1", historically "NT-1R"/"NTRH").
418 aa, 7TM class A (rhodopsin-like) GPCR; UniProt family assignment: "Belongs to the G
protein-coupled receptor 1 family. Neurotensin receptor subfamily. NTSR1 sub-subfamily."
PANTHER: PTHR24243:SF9 (NEUROTENSIN RECEPTOR TYPE 1).

Deep research: `just deep-research-falcon human NTSR1 --fallback perplexity-lite` was run twice and
failed both times — the falcon provider returned "Edison API request failed: Failed to authenticate"
and the configured fallback ("perplexity-lite") is not available in this environment ("Available:
openai, falcon, openscientist"). No `-deep-research-*.md` file was written (per repo policy I did not
author one myself). These notes were assembled from the cached publications, UniProt, Reactome and
PubMed/QuickGO/OLS lookups instead.

## Molecular identity and ligand

- Cloned from the human colonic adenocarcinoma line HT29; "encodes a putative peptide of 418 amino
  acids with 7 transmembrane domains" [PMID:8381365, "amino acids with 7 transmembrane domains"], with
  transcript "indicated a single transcript of 4 kb in the brain" [PMID:8381365, "indicated a single
  transcript of 4 kb in the brain"] plus small intestine and blood mononuclear cells.
- UniProt FUNCTION: "G protein-coupled receptor for the tridecapeptide neurotensin" — signaling
  "effected via G proteins that activate a phosphatidylinositol-calcium second messenger system",
  leading to MAP kinase activation and protection from apoptosis
  [file:human/NTSR1/NTSR1-uniprot.txt, "G protein-coupled receptor for the tridecapeptide neurotensin"].
- Reactome places NTSR1 at the plasma membrane as a Gq/11-coupled GEF: "Neurotensin receptors can bind
  neurotensins" [Reactome:R-HSA-388900] and "Liganded Gq/11-activating GPCRs act as GEFs for Gq/11"
  [Reactome:R-HSA-379048], with Gq binding and complex dissociation steps (R-HSA-749448, R-HSA-749452).

## G protein coupling — Gq/11 canonical, promiscuous in practice

- Purified NTS1 activates Gq directly: "NTS1 monomers activate G alpha q beta(1)gamma(2), whereas
  receptor dimers" catalyse nucleotide exchange with lower affinity [PMID:17620610]. The same study
  shows concentration-dependent homodimerization ("NTS1, a class A GPCR, dimerizes in detergent
  solution in a" concentration-dependent manner) and positive cooperativity of agonist binding
  ("binds the agonist neurotensin with a" Hill slope ~1 at low, ~2 at high receptor concentration),
  while concluding "NTS1 dimerization per se is not a prerequisite for G protein activation".
  So homodimerization is real but modulatory, not required for the core activity.
- NTSR1 "engages multiple subtypes of G protein" [PMID:31243364]; the Kato et al. cryo-EM study
  "present structures of human NTSR1 in complex with the agonist JMV449 and the" heterotrimeric Gi1
  protein, resolving canonical and non-canonical (≈45° rotated) receptor–G protein states.
- Deutsch et al. 2026 used **human** NTSR1 ("Full-length human NTSR1 was expressed and purified as
  previously described", Sf9/baculovirus, N-terminal Flag–8xHis, NTS8–13 agonist) — not the rat
  ortholog [PMID:42870023]. smFRET of the Gαi α-helical domain in "NTSR1–Gi ternary complexes
  (Methods), which couple promiscuously in vitro" gave a correlation between agonist-induced low-FRET
  (AHD-open) occupancy and GTP turnover (R² = 0.89), and the allosteric modulator SBI-553 "further
  shifted the AHD toward the open state proportionally to its positive modulation of GTP turnover
  in vitro". The headline conclusion is explicitly generalized: "a pattern that also applied to Gi
  bound to neurotensin type 1 receptor (NTSR1)". This is direct human-protein evidence that NTSR1
  acts as a GEF on heterotrimeric Gi and that it binds the intact heterotrimer.
- NTSR1 is used in the field as the benchmark promiscuous GPCR: in the CaSR study, "Activation levels
  by CaSR were compared against G-protein subtype activation by NTSR1, a promiscuous GPCR that
  activates most G-proteins" [PMID:38326620].

## Arrestin arm and biased signaling

- Cryo-EM of full-length human NTSR1 with β-arrestin 1: "phosphorylation of NTSR1 is critical for the"
  formation of a stable complex, with a PIP2 bridge between TM1/TM4 and the arrestin C-lobe
  [PMID:31945771]. Arrestin binding is the canonical desensitization/internalization arm
  ("triggering receptor" internalization).
- SBI-553 is a β-arrestin-biased allosteric modulator that "extends profound β-arrestin bias to the"
  endogenous ligand by "selectively antagonizing G protein signaling", and attenuates psychostimulant
  self-administration without the side effects of balanced NTSR1 agonism [PMID:32470395]. Follow-up
  work shows the same intracellular pocket can be used to re-tune G protein subtype selectivity
  [PMID:39711540]. Interpretation: G protein and β-arrestin outputs of NTSR1 are separable, which
  matters when judging which downstream processes to attribute to the receptor.

## Post-translational modification, membrane microdomains, trafficking

- Dual palmitoylation: "dual-palmitoylation at Cys381 and Cys383 of endogenously-expressed NTSR-1 in"
  MDA-MB-231 cells and in transfected HEK293T [PMID:21725197]. The palmitoylation-deficient
  C381,383S mutant "failed to interact with Gα q/11 following 15 min stimulation with 1 µM NTS", and
  "palmitoylation-deficient NTSR-1 localization within caveolinenriched SMDs is diminished upon NTS
  stimulation". WT receptor signals to ERK ("only WT-NTSR-1 efficiently stimulated ERK
  phosphorylation") and is cytoprotective: "HEK293T cells transfected with WT-NTSR-1 and treated with
  200 nM NTS showed less apoptosis relative to untreated cells", whereas the mutant shows "reduced
  ability to protect HEK293T cells against apoptosis induced by serum" starvation. UniProt records the
  same: "Palmitoylated; this is required for normal localization at" membrane rafts, and subcellular
  location "Membrane raft".
- Rat substantia nigra EM/radioautography: label is predominantly somatodendritic — "labels with
  somata and dendrites of presumptive dopaminergic neurons", with "modest localization in myelinated
  and unmyelinated axons and astrocytic" leaflets; plasma-membrane receptors are "predominantly
  extrasynaptic"; intracellular receptors occupy "membranes of smooth endoplasmic reticulum and Golgi
  apparatus" (biosynthetic pool) and "A fraction of these immunoreactive" receptors sit in endosomes
  after ligand-induced internalization [PMID:9763490]. This supports neuronal somatodendritic/axonal
  localization and ER/Golgi as biosynthetic (not active) locations, and argues against a synaptic
  (as opposed to extrasynaptic, modulatory) site of action.

## Downstream signaling and gene expression (tumour/epithelial context)

- In human colonocytes, NTSR1 activation drives a miRNA program: "Here, we used microRNA microarray
  expression analysis to detect the miRNA signature of NTR1 activation in human colonic NCM460
  epithelial cells overexpressing NTR1."; "NT altered the expression levels of 38 miRNAs (8
  up-regulated and 30 down-regulated)"; conclusion: "NTR1 activation stimulates expression of miR-21
  and miR-155 in" colonocytes via Akt and NF-κB, down-regulating PTEN and SOCS1 and promoting tumour
  growth [PMID:21806946]. The GOA IGI rows with NTS (P30990) for neuropeptide signaling and
  positive regulation of gene expression come from this work.

## Organismal physiology (mostly rodent; basis of the Ensembl-Compara IEA block)

- NTSR1 knockout mice: "hyperthermic; their body temperature was not affected by intracerebroventricular"
  NT; increased body weight and food intake; loss of NT-induced hypolocomotion ("but did not respond
  to i.c.v. NT-induced" hypolocomotion); feeding suppression by i.c.v. NT lost ("I.c.v. injection of NT
  inhibited feeding in fasted wild-type" mice but not in knockouts). Conclusion: the receptor is
  "clearly implicated in thermal and feeding regulation, weight control, and" NT-induced
  hypolocomotion, but "the NT-1R does not play a role in NT-induced analgesia" [PMID:12384239].
- Nociception is the paralog's job: in Ntsr1 vs Ntsr2 knockouts, jump latency changed only in
  Ntsr2-deficient mice; "Ntsr1-deficient or wild-type control mice. Latencies of tail flick and hind
  paw" licking were unaffected, and "results suggest that Ntsr2 has an important role in thermal
  nociception compared" to Ntsr1 [PMID:14725975]. This directly contradicts the GOA IEA row
  GO:0050965 (detection of temperature stimulus involved in sensory perception of pain) for NTSR1.
- NT acting through NTSR1 is hypotensive and modulates glutamate/GABA release and inhibitory synaptic
  transmission in limbic circuits; a 2026 study reports biased NTSR1 signaling differentially
  regulating inhibitory synaptic transmission in the extended amygdala and suppressing motivated
  feeding [PMID:42146540] (abstract-level, not used as supporting_text).

## Interactome rows

- IntAct/UniProt list NTS (P30990 and its PRO_0000019524 mature peptide), NTSR1 itself (homodimer),
  RAMP1 (O60894) and RAMP3 (O60896). The RAMP rows derive from large-scale screens: BioPlex 3.0
  affinity-purification MS [PMID:33961781] and a multiplexed GPCR–RAMP suspension-bead-array screen
  that "identified 122 GPCRs that showed strong evidence for interaction with at least one RAMP"
  [PMID:39083597]. NTSR1-specific values live in those papers' supplementary tables, which are not in
  the cached text; the interactions are plausible but the bare `protein binding` term carries no
  functional information, so those rows are removed per repo policy rather than being treated as false.
- PMID:23597562 (SSR128129E, an allosteric multi-FGFR blocker) is the `original_reference_id` for one
  `protein binding` row with the NTS mature peptide. The cached record is abstract-only and the
  abstract is entirely about FGFR; I did not use this as evidence either way, and treated the row
  under the generic-protein-binding policy only.

## Curation reasoning summary

- Core: `GO:0016492 G protein-coupled neurotensin receptor activity` at the plasma membrane (and in
  palmitoylation-dependent membrane rafts), driving `GO:0007218 neuropeptide signaling pathway`.
- Missing from GOA and proposed NEW: `GO:0007200 phospholipase C-activating G protein-coupled receptor
  signaling pathway`. Participation test: NTSR1 itself does the work of the first step (it is the GEF
  that loads Gq with GTP, which then activates PLC) — direct evidence in PMID:17620610 and the
  Gαq/11 co-IP in PMID:21725197, plus UniProt's "phosphatidylinositol-calcium second messenger system".
  Comparator check (QuickGO, 2026-10): AGTR1 has 13 annotations to GO:0007200, TACR1 has 5, HTR2A has
  4 — all peptide/amine Gq-coupled GPCRs in exactly the same role — while NTSR1 and NTSR2 have none.
  So the absence is a gap, not a convention.
- Downstream inositol-phosphate and calcium rows (GO:0032960, GO:0060732, GO:0051281) are kept; the
  opposite-sign or catabolic rows (GO:0051280, GO:0071545) and the transport rows (GO:0070779,
  GO:0098712) are not claims that the receptor performs the step.
- Organismal/behavioural IEA rows transferred from rat Ntsr1 (P20789) are retained as non-core where
  the rodent literature supports them (temperature homeostasis, feeding, blood pressure, locomotion,
  transmitter release, reward/fear), and only GO:0050965 is removed, because mouse knockouts of both
  paralogs assign thermal nociception to Ntsr2 rather than Ntsr1.
