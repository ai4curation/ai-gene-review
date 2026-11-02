# Slc25a4 (rat, UniProt Q05962) -- manual literature synthesis

No deep-research API was available for this review; this synthesis was
compiled by hand from the cached publications in `publications/` and the
UniProt record `Slc25a4-uniprot.txt`.

## Identity

- Rat Slc25a4 (RGD:620352, GeneID 85333) encodes ADP/ATP translocase 1
  (ANT1, AAC1), a 298-aa member of the mitochondrial carrier family
  (TC 2.A.29), with three Solcar repeats (Pfam PF00153 x3), six
  transmembrane helices and the nucleotide-carrier signature motif
  (residues 235-240) [Slc25a4-uniprot.txt: "Belongs to the mitochondrial
  carrier (TC 2.A.29) family."].
- Rat ANT paralogs: Slc25a5 (ANT2, RGD:620353), Slc25a31 (ANT4).
  ANT1 is the heart/skeletal-muscle isoform; adult liver expresses ANT2
  [PMID:9468308 "in contrast to adult liver, perinatal liver expressed the
  ANT1 isoform at the mRNA and protein level"].

## Core activity: ADP/ATP exchange across the inner membrane

- The mammalian carrier imports ADP into the matrix and exports ATP
  [PMID:37278158 "imports ADP into the mitochondrial matrix and exports ATP,
  which are key steps in oxidative phosphorylation"]; it is a monomer with a
  single substrate-binding site and operates by a ping-pong alternating-access
  mechanism [PMID:37278158 "the carrier operates with a ping-pong kinetic
  mechanism in which substrate exchange across the membrane occurs
  consecutively rather than simultaneously"]. This work was done on human
  SLC25A4; rat Q05962 shares the conserved substrate-binding residues
  (UniProt FT BINDING 80, 92, 235, by similarity to bovine P02722).
- Rat-specific functional data come from transgenic overexpression in rat
  heart: [PMID:21325829 "These data reveal a close association of elevated
  mitochondrial ATP/ADP transportation via ANT1 with increased contractile
  function."].

## Second transport mode: fatty-acid-dependent H+ leak (uncoupling)

- Patch-clamp of mouse inner membranes showed AAC carries a fatty-acid-
  dependent H+ current that is negatively regulated by ADP/ATP exchange
  [PMID:31341297 "The AAC-mediated H+ current requires free fatty acids and
  resembles the H+ leak via the thermogenic uncoupling protein 1 found in brown
  fat."]; the current was largely lost in heart and skeletal muscle of
  AAC1-/- mice.
- In rat skeletal-muscle mitochondria, energization-induced proton conductance
  is partly carboxyatractylate/bongkrekate sensitive, i.e. ANT-catalysed
  [PMID:18251717 "an endogenously generated activator stimulates proton
  conductance catalysed partly by UCP3 and partly by the adenine nucleotide
  translocase"]. The inhibitors do not distinguish ANT1 from ANT2.

## Permeability transition pore (mPTP)

- ANT binds cyclophilin D in inner-membrane preparations, CsA-sensitively
  [PMID:9820802 "Immobilized GST-CyP-D avidly bound a single 30 kDa protein
  present in Triton X-100-solubilized IMMs; immunoblotting showed this to be
  the adenine nucleotide translocase (ANT)."] -- liver IMM, so isoform
  identity (ANT2 dominates adult liver) is not established.
- Lin & Lechleiter also detected CyPD-ANT binding [PMID:12077116 "CyPD binding
  to the adenine nucleotide translocator (ANT), which is considered to be the
  core component of the mPTP, is not affected by the loss of PPIase
  activity"].
- Genetic ablation of Ant1+Ant2 in mouse liver shows ANTs are not essential for
  the pore but regulate it [PMID:14749836 "ANTs are non-essential structural
  components of the mtPTP, although they do contribute to its regulation."].
- Rat ANT1 transgenic cardiomyocytes resist TGFb1-induced apoptosis and MPTP
  opening [PMID:22564366 "Heart-specific overexpression of ANT1 leads to a
  reduced apoptotic response to TGFβ(1) by preservation of the mitochondrial
  membrane potential, resistance to MPTP opening and altered TGFβ
  signaling."] -- an overexpression phenotype.

## Mitophagy

- ANT promotes PINK1/parkin mitophagy independent of nucleotide exchange, via
  TIM44 and inhibition of TIM23 [PMID:31618756 "ANT promotes mitophagy
  independently of its nucleotide translocase catalytic activity."] (human
  cells and Ant1-/- mice).

## Localization

- Mitochondrial inner membrane, multi-pass (UniProt by similarity to human).
  Rat kidney/testis fractionation used ANT as the IM marker and noted it also
  appears in OM fractions at contact sites [PMID:18385140 "The mitochondrial OM
  marker VDAC and the IM marker adenine nucleotide transporter (ANT) are both
  found at OM/IM contact sites; therefore, they can be found in both membrane
  fractions."].

## Expression studies (no mechanistic role)

- Postnatal rise in heart [PMID:12676547], transient perinatal liver expression
  [PMID:9468308], IL-1beta induction in brain [PMID:15950780]. These are
  expression correlations only.

## Caveats on rat experimental rows

- The membrane-raft proteomics paper (PMID:14499952) is available only as an
  abstract that does not mention ANT. No other source places ANT1 in
  plasma-membrane rafts; detergent-resistant membrane preparations commonly
  co-purify abundant mitochondrial inner-membrane carriers, so the raft
  assignment cannot be verified here.
- Necroptosis: TNF-induced, RIP-dependent inhibition of ANT ADP import causes
  necrosis, and ectopic ANT prevents it [PMID:16507998 "the ectopic expression
  of ANT or cyclophilin D was effective at preventing cell death"].
