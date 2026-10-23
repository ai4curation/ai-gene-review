# GNAO1 (human, P09471) review notes

## Session 2026-10-23

### Deep research status
- `just deep-research-falcon human GNAO1 --fallback perplexity-lite` was run twice and **failed**:
  falcon raised `Exception: Failed to authenticate`, and the fallback failed with
  `Provider 'perplexity' not available. Available: openai, falcon, openscientist`.
  No `-deep-research-*.md` file exists for this gene. The review below is based on the
  UniProt record, the cached publications for the GOA references, the cached GO-CAM index,
  and general background knowledge of heterotrimeric G-protein biology (statements from
  background knowledge are flagged as such and are not used as supporting_text).

### Identity
- GNAO1 encodes Galpha-o (Go alpha), a member of the Gi/o/t/z subfamily of heterotrimeric
  G-protein alpha subunits [file:human/GNAO1/GNAO1-uniprot.txt "Belongs to the G-alpha family. G(i/o/t/z) subfamily."].
- Two splice isoforms, Alpha-1 (GoA, P09471-1) and Alpha-2 (GoB, P09471-2) arise from
  alternative splicing of a single gene on chromosome 16
  [PMID:1899283 "Different forms of Go alpha mRNA arise by alternative splicing of transcripts from a single gene on human chromosome 16."].
- Most abundant G protein in brain [PMID:29925951 "GO is the most abundant G protein in the brain"];
  also present in heart [PMID:9050846 "The G alpha(o) protein is the most abundant G alpha subtype in the nervous system, but it is also found in the heart."].

### Molecular function: G protein (GTPase switch)
- UniProt: alternates between active GTP-bound and inactive GDP-bound states; activated GPCR
  promotes GDP release and GTP binding [file:human/GNAO1/GNAO1-uniprot.txt "Signaling by an activated
  GPCR promotes GDP release and GTP binding"]. Catalytic activity GTP + H2O = GDP + phosphate (Rhea:19669),
  evidence PMID:39103320.
- Knight et al. 2024 [PMID:39103320]: purified Galpha-o binds and hydrolyses BODIPY-GTP;
  "Many neurotransmitter receptors activate G proteins through exchange of GDP for GTP."
  The disease variant K46E "binds poorly to guanine nucleotides yet retains wild-type affinity
  for G protein βγ subunits" and "forms a stable complex with receptors and Gβγ, impeding
  effector activation". Cryo-EM of dopamine-bound D2R with GoA K46E.
- Receptor coupling: "the dopamine D2 receptor (D2R, couples to GαoA and GαoB)" and the
  mu-opioid receptor "couples to Gαi1, Gαi2, Gαi3, Gαz, GαoA, and GαoB" [PMID:39103320].
- Structures: 5-HT1B receptor–Go [PMID:29925951 "5-HT1BR couples to Gi/o"]; ADGRG3/GPR97–Go
  bound to glucocorticoids [PMID:33408414 "Palmitoylation at the cytosolic tail of the Go protein was found to be essential for efficient engagement with GPR97"].
- Gbeta-gamma binding is part of the cycle (heterotrimer formation in GDP state); retained by
  K46E [PMID:39103320].
- Regulators: RGS proteins (GAPs: RGS14, RGS16, RGS19 by similarity / PMID:34685729) and
  RIC8A (non-receptor GEF/chaperone, IntAct). These are partners of the switch, not separate
  functions of GNAO1.

### Biological process
- Effector output: inhibition of adenylyl cyclase (UniProt "GNAO1 acts by inhibiting the activity of adenylate
  cyclases, leading to decreased intracellular cAMP levels (By similarity)") and, via released
  Gbeta-gamma, modulation of GIRK K+ channels and voltage-gated Ca2+ channels (PMID:39103320 uses GIRK
  readouts: "Upon binding to free Gβγ, GIRK channel opening leads to potassium flux.").
- Heart: Gnao1-null mice lack muscarinic inhibition of L-type Ca channels
  [PMID:9050846 "muscarinic inhibition of L-type Ca2+ channels requires coupling of the muscarinic receptor to G alpha(o)"].
  Knockout mice have "tremors and occasional seizures" with grossly intact nervous system.
- GO-CAM models (gocams/index.tsv) for human GNAO1 consistently use G protein activity
  (GO:0003925) in adenylate cyclase-inhibiting GPCR signaling (GO:0007193) or the serotonin
  variant (GO:0007198), located on the cytoplasmic side of plasma membrane (GO:0009898):
  HTR1B, ADGRG3, CHRM2, ADRA2B, GPR158/RGS7 models.
- Mouse GO-CAM 62f58d8800006739 places Gnao1 (isoform Alpha-2) in negative regulation of
  insulin secretion (source of the human IEA for GO:0046676).

### Localization
- Peripheral membrane protein on the cytoplasmic side of the plasma membrane, lipid anchored
  (N-myristoylation of Gly2 / palmitoylation at Cys3 [background], and palmitoylation at Cys351 per UniProt/PMID:33408414).
- Solis et al. 2021 [PMID:34685729]: "of the two intracellular sites of Gαo localization, plasma
  membrane and Golgi, the former is strongly reduced for the mutant proteins".
- Neuronal compartments (dendrite, cell body, pre/postsynaptic membrane, synapses) are IEA
  transfers from mouse (SynGO etc.); biologically plausible given abundance in neurons and
  growth cones (PMID:9050846: "G alpha(o) makes up 0.2-0.5% of brain particulate protein and 10% of the growth cone membrane").

### Disease: GNAO1 encephalopathy
- Two OMIM entities (UniProt): DEE17 (developmental and epileptic encephalopathy 17, MIM:615473)
  and NEDIM (neurodevelopmental disorder with involuntary movements, MIM:617493). De novo,
  dominant, mostly missense variants clustering in the nucleotide-binding / switch regions
  (G40, Q52, K46, G203, R209, E246, etc. [background knowledge]).
- Mechanisms: Q52P/Q52R are "deficient in binding and hydrolyzing GTP" with reduced PM
  localization and partner interactions [PMID:34685729]; K46E is nucleotide-binding deficient and
  acts dominant-negatively by sequestering receptor and Gbeta-gamma in a nucleotide-free complex
  [PMID:39103320 "GαoK46E suppressed the release of Gβγ, and did so both in the absence and presence of wild-type Gαo"].
  R209C instead "binds to nucleotides but fails to release Gβγ" [PMID:39103320].
- Overall: the disease is best explained as perturbation of the Galpha-o GTPase cycle, with
  dominant-negative and gain/loss-of-function classes [background: Feng et al. 2017 eLife,
  not cached].

### Background paper (not cited in review)
- PMID:42870023 (Deutsch et al. 2026, smFRET of Galpha-i alpha-helical domain dynamics in
  mu-opioid receptor–Gi complexes) concerns Gi, not Go; not directly relevant to GNAO1 and
  not cited in the review.

### Interaction (protein binding) annotations
- HTT (PMID:17500595, Y2H huntingtin interactome); calreticulin, ABCD3, CBX5, DLST, HTT,
  NEK7, RPS6KA3, TGFBR2, VCP (PMID:32814053 neurodegeneration Y2H map); RIC8A (PMID:33961781 HuRI-like
  network); SYNGAP1 (PMID:37207277); VCP (PMID:37776851); RGS19 (PMID:34685729). Only RIC8A and
  RGS19 are mechanistically meaningful (GEF and GAP of the switch); all generic protein binding
  rows are removed as uninformative.

### Decisions summary
- Core: G protein activity (GO:0003925) in heterotrimeric G-protein complex, cytoplasmic side
  of plasma membrane; adenylate cyclase-inhibiting GPCR signaling (GO:0007193), dopamine and serotonin receptor signaling.
- GTPase activity (parent of G protein activity), signal transduction, adenylate
  cyclase-modulating GPCR signaling, guanyl nucleotide binding, response to monoamine: TOO_GENERAL.
- Muscle contraction (TAS, PMID:9050846): MODIFY to G protein-coupled acetylcholine receptor signaling pathway (GO:0007213).
- cytoplasm (IBA): MODIFY to cytoplasmic side of plasma membrane.
- CRHR1 binding (IBA): MARK_AS_OVER_ANNOTATED (no GNAO1-specific evidence; CRHR1 is primarily Gs-coupled).
