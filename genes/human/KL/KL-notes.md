# KL (alpha-Klotho, Q9UEF7) curation notes

## 2026-09-30 Initial review (Claude Code)

### Identity and architecture
- Type I single-pass membrane protein: signal peptide 1-33, extracellular 34-981, TM 982-1002,
  10-residue cytoplasmic tail [file:human/KL/KL-uniprot.txt "TOPO_DOM        1003..1012"].
- Two tandem GH1-like domains (KL1, KL2). UniProt: "the first region lacks the essential Glu active
  site residue at position 239, and the second one lacks the essential Glu active site residue at
  position 872" [file:human/KL/KL-uniprot.txt].
- Two transcripts: membrane form and a putative secreted KL1-only splice form
  [PMID:9464267 "We have further identified two transcripts that encode a membrane or secreted protein."].
- Shed ectodomain circulates: [PMID:15135068 "Newly established antibodies against Klotho allowed the
  detection of secreted Klotho, a candidate for the putative humoral factor, in sera and cerebrospinal
  fluid."]. The circulating species is 130 kDa (i.e. the shed full ectodomain), not the 70 kDa splice form
  [PMID:15135068 "Surprisingly the secreted Klotho was 130 kDa, in contrast to the 70 kDa predicted form"].

### Core function: FGF23 co-receptor
- [PMID:17086194 "Klotho binds to FGF23"; "the concerted action of Klotho and FGFR1(IIIc) reconstitutes
  the FGF23 receptor"]; Klotho itself cannot signal ["Klotho alone seemed to be incapable of intracellular
  signalling"]. Abstract only.
- [PMID:16436388 "Klotho binds to multiple FGFRs and functions as a cofactor necessary for FGF signaling
  activation by FGF23"; "FGF23 was pulled down with FGFR1c, -3c, and -4 only in the presence of Klotho"].
- Crystal structure of human FGF23-FGFR1c-alphaKlotho ectodomain ternary complex
  [PMID:29342138 "The structure reveals that αKlotho serves as a non-enzymatic scaffold that simultaneously
  tethers FGFR1c and FGF23 to implement FGF23-FGFR1c proximity and hence stability."]. Soluble ectodomain is
  also a co-receptor ["demonstrating that αKlothoecto can serve as a bona fide co-receptor to support FGF23
  signaling in renal proximal tubules"].
- FGF19 also binds alphaKlotho in vitro [PMID:18829467 "We previously showed that FGF19 can bind to both
  alpha and betaKlotho"]; FGF23 specificity lies in the FGF C-terminal tail.
- Human genetics: homozygous H193R causes hyperphosphatemic tumoral calcinosis [PMID:17710231
  "loss-of-function mutations in human KL impair FGF23 bioactivity, underscoring the essential role of KL
  in FGF23-mediated phosphate and vitamin D homeostasis in humans"].

### Enzymatic activity - weighed and rejected as core
- Tohyama 2004 (mouse KLFc fusion) reported weak beta-glucuronidase activity with 4-MU glucuronide and
  steroid glucuronides [PMID:14701853 "An enzymatic activity of Klotho was observed only with
  4-methylumbelliferyl beta-D-glucuronide"]. Abstract-only in cache.
- Chen 2018 (human ectodomain, full text) could not reproduce: [PMID:29342138 "Indeed, αKlothoecto failed
  to hydrolyze substrates for both sialidase and β-glucuronidase in vitro"]; both KL domains lack a
  catalytic Glu ["Moreover, both KL domains lack one of the key catalytic glutamates deep within the
  putative catalytic pocket."]; loop conformations "incompatible with an intrinsic glycosidase activity".
- Deep research (falcon) cites a 2020 structure-function study in which restoring the catalytic glutamates
  increased glucuronidase activity while reducing co-receptor activity; not independently verified here
  (no PMID cached), so not used as evidence.
- Decision: glucuronidase / O-glycosyl hydrolase MF terms MARK_AS_OVER_ANNOTATED (reported, contested,
  no physiological substrate); beta-glucosidase (TAS from 1997 homology statement) REMOVE; carbohydrate
  metabolic process REMOVE.

### Rat-derived IEA process terms
- Rat Kl (Q9Z2Y9) source annotations: BP / norepinephrine from intracerebroventricular shRNA study
  [PMID:20086041 "silencing of brain klotho increased ET1 production and the sympathetic nervous
  activity"] - indirect, systemic. "response to X" terms come from rat IEP (expression) papers
  (PMID:22891896, PMID:20631679, PMID:17992255, PMID:11967236; not cached, identified via QuickGO).
- Decision: norepinephrine biosynthesis REMOVE (KL performs no step); BP MARK_AS_OVER_ANNOTATED;
  response to activity/angiotensin/vitamin D MARK_AS_OVER_ANNOTATED (expression responses);
  response to FGF KEEP_AS_NON_CORE (true by ancestry via FGFR signaling pathway).

### Bone mineralization IMP (PMID:12110410)
- Association of a non-coding CA-repeat microsatellite with bone density in Japanese postmenopausal women
  [PMID:12110410 "None of the genotypes was associated with bone density in the overall population"].
  Not a mutant phenotype; KL loss in humans causes ectopic calcification. MARK_AS_OVER_ANNOTATED.

### NEW proposals and comparator checks
- GO:0015026 coreceptor activity: matches KLB review core MF; KL binds FGF23 and FGFR1c and cannot
  signal alone. Coreceptor is the best available MF; alternative would be FGF binding + FGFR binding only.
- GO:0055062 phosphate ion homeostasis: comparator check (QuickGO 2026-09-30): FGF23 (Q9GZV9) carries it
  (IMP PMID:11062477), FGFR1 and KLB do not. KL is the tissue-selective receptor component doing work in the
  FGF23 signal; human loss-of-function causes hyperphosphatemia. Proposed as NEW with IMP from
  PMID:17710231 but flagged in suggested_questions since FGFR1 lacks it.

### Module relevance (fgfr_signaling)
- Coreceptor activity is a good fit for KL: it binds FGF23 with high affinity, binds FGFR1c, is required
  for receptor activation, lacks signaling capacity. Structural data call it a "scaffold"; the soluble
  ectodomain works in trans as well, so the module location (plasma membrane) captures the membrane form
  but the shed form is extracellular.
