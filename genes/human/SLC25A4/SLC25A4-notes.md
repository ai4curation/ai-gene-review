# SLC25A4 (ANT1 / AAC1) — review notes

UniProt: P12235 (ADT1_HUMAN). HGNC:10990. Gene: SLC25A4; synonyms AAC1, ANT1.
Heart/skeletal-muscle isoform of the mitochondrial ADP/ATP carrier. 298 aa,
6-TM mitochondrial-carrier (SLC25) fold, TC 2.A.29.1.2.

## Core function: ADP/ATP antiporter (GO:0005471)

- ADP:ATP antiport is the defining, experimentally established activity.
  UniProt CATALYTIC ACTIVITY: `ADP(in) + ATP(out) = ADP(out) + ATP(in)`
  (Rhea:34999) with ECO:0000269 from PMID:21586654 and PMID:23173940
  [file:human/SLC25A4/SLC25A4-uniprot.txt].
- "The mitochondrial ADP/ATP carrier (SLC25A4), also called the adenine
  nucleotide translocase, imports ADP into the mitochondrial matrix and exports
  ATP, which are key steps in oxidative phosphorylation." [PMID:37278158].
- Narrow substrate specificity — only ADP and ATP: "A large number of
  nucleotides were tested, but only ADP and ATP are suitable substrates for
  human AAC1, demonstrating a very narrow specificity." [PMID:23173940]. This is
  the key evidence against the legacy "adenine (base) transport" annotations.
- Operates as a MONOMER with a single central substrate binding site,
  alternately exposed to c-state/m-state, via a ping-pong (double-displacement)
  kinetic mechanism [PMID:37278158].
- Km = 23.7 uM for ATP; Vmax 14.6 nmol/min/mg [PMID:23173940, via UniProt
  BIOPHYSICOCHEMICAL PROPERTIES].
- Direct disease-mutant functional data: adPEO mutants show "decreased ADP-ATP
  exchange function and abnormal translocator reversal potential" [PMID:21586654];
  p.Lys33Gln shows "significantly impaired ADP/ATP transport in Lactococcus
  lactis" [PMID:30046662]; de novo dominant mutants: "both recombinant AAC1
  mutant proteins are severely impaired in ADP/ATP transport" [PMID:27693233].

## Location: mitochondrial inner membrane (GO:0005743)

- UniProt SUBCELLULAR LOCATION: "Mitochondrion inner membrane"
  (ECO:0000269|PubMed:21586654); multi-pass membrane protein
  [file:human/SLC25A4/SLC25A4-uniprot.txt].
- Reactome TAS annotations (R-HSA-180905, R-HSA-5250209, R-HSA-5672027,
  R-HSA-9864415) and HPA IDA (GO_REF:0000052) place it in mitochondria/inner
  membrane. A possible minor non-mitochondrial (erythrocyte) membrane pool is
  reported: "May localize to non-mitochondrial membranes (PubMed:27641616)"
  [file:human/SLC25A4/SLC25A4-uniprot.txt] — basis for the general "membrane"
  annotation, but NOT a plasma-membrane function.

## Secondary (non-core) roles — kept as KEEP_AS_NON_CORE

- **mPTP** (GO:0005757, GO:0046902): "Also plays a key role in mPTP opening... a
  non-specific pore that enables free passage of the mitochondrial membranes to
  solutes of up to 1.5 kDa, and which contributes to cell death"; but "It is
  however unclear if SLC25A4/ANT1 constitutes a pore-forming component of mPTP or
  regulates it" [file:human/SLC25A4/SLC25A4-uniprot.txt]. ARHGAP11B interaction
  inhibits the mPTP [PMID:31883789]; cyclophilin D interaction [PMID:16507998].
- **Uncoupling / proton leak / thermogenesis** (GO:0015078, GO:0017077,
  GO:1902600, GO:1990845): "Plays a role in mitochondrial uncoupling by acting
  as a proton transporter: proton transport uncouples the proton flows via the
  electron transport chain and ATP synthase to reduce the efficiency of ATP
  production and cause mitochondrial thermogenesis" (By similarity)
  [file:human/SLC25A4/SLC25A4-uniprot.txt]; Reactome R-HSA-166187 (Mitochondrial
  Uncoupling). Proton-transporter activity is inhibited by antiporter activity.
- **Mitophagy** (GO:1901526): "Acts as a regulator of mitophagy independently of
  ADP:ATP antiporter activity: promotes mitophagy via interaction with TIMM44,
  leading to inhibit the presequence translocase TIMM23, thereby promoting
  stabilization of PINK1" (By similarity)
  [file:human/SLC25A4/SLC25A4-uniprot.txt].
- **Necroptosis/necrosis regulation** (GO:0060546, IMP): "tumor necrosis factor
  alpha induced RIP-dependent inhibition of adenine nucleotide translocase
  (ANT)-conducted transport of ADP into mitochondria, which resulted in reduced
  ATP and necrotic cell death" [PMID:16507998].

## Annotations removed / modified

- GO:0015853 "adenine transport" (IEA, GO_REF:0000108) — REMOVE. Inter-ontology
  inference from the over-broad "adenine transmembrane transporter activity"
  (GO:0015207). ANT1 transports ADP/ATP nucleotides, not free adenine base
  (narrow specificity; PMID:23173940). Wrong electronic inference.
- GO:0015207 "adenine transmembrane transporter activity" (TAS, PMID:2823266) —
  MODIFY → GO:0005471. Legacy 1987-cloning-paper label; the accurate MF is
  ATP:ADP antiporter activity.
- GO:0005886 "plasma membrane" (TAS, PMID:2823266) — UNDECIDED. Legacy TAS; ANT1
  is an inner-membrane carrier and there is no credible plasma-membrane function.
  Cannot be firmly refuted from the abstract-only cache, so UNDECIDED (not core).

## Bare "protein binding" (GO:0005515) IPIs — MARK_AS_OVER_ANNOTATED

Per policy, experimental IPIs are not removed. Partners: LRRK2 (PMID:21370995,
PMID:24725412), NR4A1/TR3 (PMID:24316735), SLC25A6/ANT3 paralog (PMID:33961781,
PMID:40355756), ARHGAP11B (PMID:31883789), cyclophilin D (PMID:16507998).
"protein binding" is uninformative as an MF term; the specific interactions
(esp. ARHGAP11B→mPTP and cyclophilin D→mPTP) are captured in the mPTP/necrosis
BP annotations.

## Disease (context)

- PEOA2 (autosomal dominant PEO with multiple mtDNA deletions) — dominant
  variants (e.g. A114P, V289M) [PMID:10926541, PMID:21586654].
- MTDPS12A/B (mtDNA depletion, cardiomyopathic) — dominant de novo (R80H, R235G)
  and recessive loss-of-function [PMID:27693233, PMID:16155110].
- Mild childhood myopathy — de novo p.Lys33Gln [PMID:30046662].

## Action tally

ACCEPT (core MF/BP/inner-membrane) and KEEP_AS_NON_CORE (mPTP, uncoupling,
thermogenesis, mitophagy, necrosis, generic localizations) dominate. One REMOVE
(adenine transport IEA), one MODIFY (adenine transporter → antiporter), one
UNDECIDED (plasma membrane TAS), seven MARK_AS_OVER_ANNOTATED (bare protein
binding IPIs). No enzymatic/catalytic MF assigned — ANT1 is a transporter.
