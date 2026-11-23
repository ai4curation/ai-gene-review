# Wnt8 (SpWnt8, Sp-Wnt8; UniProt Q6RFL8) - curation notes

## Identity of the UniProt entry

- Q6RFL8 is an unreviewed TrEMBL entry (358 aa, "Protein Wnt", gene name `Wnt8` taken from the
  EMBL record AAR97610.1). The record carries no PubMed cross-reference: its single reference is
  a direct submission by A.H. Wikramanayake (December 2003) titled "Wnt8 signaling in vegetal cells
  of the early sea urchin embryo mediates primary mesenchyme cell differentiation and endomesoderm
  specification in a nuclear beta-catenin-dependent manner", i.e. the cDNA behind Wikramanayake
  et al. 2004 (Genesis 39:194-205, PMID:15282746, found by eutils search; the UniProt record itself
  has no RX line). The accession is therefore the SpWnt8 of the endomesoderm GRN literature.
  Confidence in the accession-to-gene link: high.
- Domain content: InterPro IPR005817 (Wnt), IPR043158 (Wnt C-terminal), IPR018161 (Wnt conserved
  site); Pfam PF00110; PANTHER PTHR12027 (family) / PTHR12027:SF81 (subfamily). UniProt (RuleBase
  RU003500) describes it as a ligand for members of the frizzled family of seven-transmembrane
  receptors, secreted, extracellular matrix, lipoprotein, disulfide-bonded.

## What the gene is

Wnt8 is a secreted Wnt-family ligand, the zygotic "motor" of the sea urchin endomesoderm gene
regulatory network. It is not a transcription factor: it is the intercellular signal whose
reception drives beta-catenin into the nucleus of the receiving cell, and it is itself
transcribed under control of beta-catenin/Tcf, so that it forms a self-propagating intercellular
positive feedback loop.

- Original description [PMID:15282746 "Here, we show that SpWnt8, a Wnt8 homolog from
  Strongylocentrotus purpuratus, is zygotically activated specifically in 16-cell-stage micromeres
  in a nuclear beta-catenin-dependent manner, and its expression remains restricted to the
  micromeres until the 60-cell stage. At the late 60-cell stage nuclear beta-catenin-dependent
  SpWnt8 expression expands to the veg2 cell tier."].
- Uniqueness of the expression domain [PMID:15282746 "SpWnt8 is the only signaling molecule thus
  far identified with expression localized to the 16-60-cell stage micromeres and the veg2 tier."].
- Signaling logic [PMID:16289024 "Expression of the wnt8 gene is the key transcriptional
  motivator of an intercellular signaling loop which drives endomesoderm specification forward
  early in sea urchin embryogenesis."; "The implication is that zygotic expression of wnt8 is
  stimulated in neighboring cells by its own gene product, since reception of the Wnt8 ligand
  causes beta-catenin nuclearization."].
- Micromere ligand [PMID:18413610 "the micromeres in fact express three different intercellular
  signaling ligands: ( i ) Wnt8, which enhances nuclearization of β-catenin in recipient cells,
  including themselves"].

## Place in the GRN

### Inputs (cis-regulatory evidence)

- Minokawa, Wikramanayake & Davidson 2005 characterized the modular wnt8 cis-regulatory system
  (abstract only in cache) [PMID:16289024 "the modular cis-regulatory system of the wnt8 gene of
  Strongylocentrotus purpuratus was characterized functionally, and shown to respond to blockade
  of both Blimp1/Krox and Tcf1/beta-catenin inputs just as does the endogenous gene."; "The
  Tcf1/beta-catenin and Blimp1/Krox inputs are both necessary for normal endomesodermal expression
  mediated by this cis-regulatory module; thus, the genomic regulatory code underlying the
  predicted signaling loop thus resides in the wnt8 cis-regulatory sequence."].
- Micromere-lineage inputs [PMID:18413610 "By late fourth-cleavage stage the micromeres begin to
  transcribe the wnt8 gene, and both the network perturbation analysis and a direct cis
  -regulatory study ( 15 , 37 ) demonstrate that the inputs required for its expression in the
  micromere lineage are Blimp1 and β-catenin/Tcf."]. Timing [PMID:18061160 "Expression of wnt8
  occurs first, at early 5th cleavage."].
- Blimp1 is an activator at wnt8 and a repressor at its own gene and at hesC [PMID:19104065
  "Blimp1 represses the hesC gene, HesC in turn represses the delta gene, and Blimp1 represses the
  blimp1 gene as well as activating the wnt8 gene."].
- Caveat from the endoderm GRN paper: the Blimp1 requirement holds for a small reporter construct
  but not for the whole-locus BAC [PMID:21623371 "the same mutation does not affect expression of a
  bacterial artificial chromosome expression construct containing the whole genomic wnt8
  cis-regulatory system"; "the expression of wnt8 begins in veg2-derived cells long before the onset
  of blimp1b expression in these cells"; "Our results exclude an earlier model23 proposing that
  clearance of blimp1b expression from the mesodermal domain19,24 is responsible for clearance of
  wnt8 expression from this domain, on the assumption that Blimp1 is a necessary driver of wnt8
  expression."]. So beta-catenin/Tcf is the robust input; the Blimp1 input is module-specific and
  its necessity in vivo is disputed.

### The Blimp1/Wnt8 torus subcircuit

- [PMID:17975065 "Early specification of endomesodermal territories in the sea urchin embryo
  depends on a moving torus of regulatory gene expression."; "A cis-regulatory reconstruction
  experiment revealed that blimp1 autorepression accounts for progressive extinction of expression
  in the center of the torus, whereas its outward expansion follows reception of the Wnt8 ligand by
  adjacent cells."].
- [PMID:18061160 "The immediate controller of the moving torus pattern is the wnt8 gene."; "The wnt8
  gene is functionally linked into the subcircuit in that cells receiving this ligand generate a
  β-catenin/Tcf input required for blimp1 expression, while the wnt8 gene in turn requires a Blimp1
  input"; "an important additional fact is that it is indeed Wnt8 which generates the essential
  β-catenin/Tcf input into the blimp1 gene."].
- [PMID:18413610 "Therefore, an intercellular feedback circuit is set up, as each wnt8 -expressing
  cell also causes the adjacent recipient cells to drive more β-catenin into its nucleus and further
  express wnt8"; "The blimp1 gene plays no other essential early role in the skeletogenic micromere
  lineage other than to provide input into the wnt8 gene."].
- [PMID:19104065 "Meanwhile, Wnt8 diffusion causes expansion of the subcircuit expression torus to
  the adjacent cells of the next domain."]. The torus also sets the position of Delta/Notch
  signaling: wnt8 and delta domains stay complementary as the torus expands [PMID:19104065 "The
  essential developmental result is that Delta and Wnt8 domains remain exclusive and adjacent in the
  NSM and endoderm"].

### Outputs / loss-of-function phenotype

- Wikramanayake et al. 2004 (S. purpuratus, MASO and mRNA overexpression) [PMID:15282746
  "Overexpression of SpWnt8 by mRNA microinjection produced embryos with multiple invagination
  sites and showed that, consistent with its localization, SpWnt8 is a strong inducer of
  endoderm."; "Blocking SpWnt8 function using SpWnt8 morpholino antisense oligonucleotides produced
  embryos that formed micromeres that could transmit the early endomesoderm-inducing signal, but
  these cells failed to differentiate as primary mesenchyme cells."; "SpWnt8-morpholino embryos
  also did not form endoderm, or secondary mesenchyme-derived pigment and muscle cells, indicating a
  role for SpWnt8 in gastrulation and in the differentiation of endomesodermal lineages."].
- [PMID:19104065 "Expression of wnt8 is also essential for specification of both NSM and endoderm.";
  "Thus, blocking Wnt8 translation with morpholino antisense oligonucleotides (MASO), or blocking
  nuclearization of its downstream effector, β-catenin, by overexpression of an intracellular
  fragment of Cadherin ( 15 , 6 ), prevents both NSM and endoderm specification."].
- [PMID:18413610 "blockade of wnt8 expression and disruption of the wnt8 intercellular feedback loop
  plays havoc with endomesodermal specification, including that of the skeletogenic micromere
  lineage"]; [PMID:18061160 "Morpholino-substituted antisense oligonucleotide (MASO) targeting
  blimp1 blocks endomesoderm specification ( Livi and Davidson, 2007 ), just as does MASO directed
  against the wnt8 gene ( Minokawa et al., 2005 ; Wikramanayake et al., 2004 )."].

### Later, non-endomesodermal role: anterior neuroectoderm restriction

- Range, Angerer & Angerer 2013 (full text cached) show that Wnt8, together with Wnt1, acting through
  Fzl5/8 and JNK rather than beta-catenin, restricts the anterior neuroectoderm (ANE, foxq2 domain)
  to the anterior pole [PMID:23335859 "Here we show that the Wnt-dependent restriction of
  neuroectoderm to the anterior pole involves not only Wnt/β-catenin but also a series of linked
  steps mediated by Wnt/JNK signaling through Wnt1, Wnt8, and Fzl5/8, the homolog of vertebrate
  Fzl8."; "embryos injected with either Wnt1 or Wnt8 morpholinos failed to down-regulate foxq2
  expression in posterior ectoderm."]. Later expression moves anteriorly [PMID:23335859 "As
  development progressed, wnt8 expression first moved into the next most anterior tier of
  blastomeres (veg1) and then, during late blastula stages (18 and 24 hpf), into both veg1 and
  overlying posterior ectoderm cells"]. This is an anterior/posterior patterning (regionalization)
  function, not neuron differentiation.

## Curation decisions (summary)

- Electronic rows: frizzled binding (IBA), extracellular region (IBA, IEA) and canonical Wnt
  signaling pathway (IBA) accepted; 'signaling receptor binding' (IEA) and 'Wnt signaling pathway'
  (IEA) modified to the specific receptor-ligand and canonical (beta-catenin) terms; 'cytokine
  activity' (IBA) modified to receptor ligand activity; 'cell fate commitment' (IBA) modified to
  the specific endoderm/mesoderm specification terms; 'neuron differentiation' (IBA) marked as
  over-annotated (sea urchin evidence is for A/P neuroectoderm regionalization, not neuron
  differentiation).
- NEW (IMP): receptor ligand activity; endodermal cell fate specification; mesodermal cell fate
  specification; anterior/posterior pattern specification (non-core).
- Participation test: Wnt8 is the ligand that performs the intercellular step (its reception
  nuclearizes beta-catenin in the recipient), so it does part of the work of the specification
  process. Comparator check (QuickGO): C. elegans mom-2 (a Wnt ligand) carries GO:0001714
  endodermal cell fate specification by IMP; Xenopus wnt8 (P28026) carries mesoderm development by
  IDA; the PAINT IBA already places cell fate commitment on the family node. gocams/index.tsv has
  no entry for this gene or species.
- Not proposed: Wnt-protein binding, morphogen activity (no gradient/concentration-dependence
  data), gastrulation (downstream of endoderm specification), PMC differentiation (executed by the
  skeletogenic GRN, Wnt8 provides input only).
