# Blimp1 (Sp-blimp1/krox, formerly SpKrox1; UniProt Q2VF23; GeneID 751833) - curation notes

## Identity of the UniProt entry

- Q2VF23 is an unreviewed TrEMBL entry (753 aa) whose single source is the mRNA DQ177152
  "Blimp1/Krox1b", submitted with Livi & Davidson 2007 (`RX PubMed=16798107`). It therefore
  represents the early, cleavage-stage **1b** splice/transcription variant of the
  blimp1/krox gene that is the endomesoderm-GRN node (RefSeq NP_001073021, GeneID 751833).
  The PR/SET domain (aa 86-209) and four C2H2 zinc fingers (aa 458-564) match the
  description of the gene product as "a zinc finger transcription factor of the SET family
  of proteins" [PMID:18061160 "This gene encodes a zinc finger transcription factor of the SET
  family of proteins (for details and sequence analysis, see Livi and Davidson, 2006 , 2007 )"].
- Naming: "The blimp1/krox gene of Strongylocentrotus purpuratus, formerly krox1, encodes zinc
  finger transcription factors which play a central role in both early and late endomesoderm
  specification" [PMID:16581059]. The original cloning paper named it SpKrox1 [PMID:9025071
  "One newly identified clone, named SpKrox1, contained four zinc fingers and a leucine zipper
  domain"]. Peter & Davidson 2011 call the early form `blimp1b` [PMID:21623371].
- Confidence in the accession-to-gene link: high (the accession's own literature citation is
  the Blimp1/Krox isoform paper from the Davidson lab).

## What the gene is

Blimp1/Krox is the sea urchin orthologue of the vertebrate PRDM1/Blimp-1 PR-domain zinc-finger
transcription factor. It is expressed zygotically from cleavage and acts both as a
transcriptional activator and as a transcriptional repressor, depending on the target
cis-regulatory module [PMID:19104065 "members of the Blimp transcription factor family are
well known to act as activators, as we have shown that Blimp1 does in the wnt8 cis
-regulatory system, and also as repressors, as in its own cis -regulatory system"].

Two alternatively transcribed/spliced forms exist: the early 1b form (this accession) and the
late gut-specific 1a form [PMID:16581059 "The blimp/krox1b form was previously unknown, and is
the form expressed during cleavage, beginning 6-9 h postfertilization. This form is required
for the early events of endomesoderm specification. A different splice variant, blimp1/krox1a,
is expressed only from gastrula stage onward"]. The 1a form is driven by a separate midgut/
hindgut module that carries Brn1/2/4, Otx and Blimp1 sites [PMID:16798107 "Its sequence
contains binding sites for Brn1/2/4, Otx, and Blimp1/Krox itself, as predicted in a prior
regulatory network analysis"].

## Expression

- Earliest transcripts in the macromeres/vegetal plate [PMID:9025071 "SpKrox1 mRNA was first
  seen in macromeres of 16-cell stage embryos and was restricted to cells of the developing
  vegetal plate thereafter"]; by the Davidson-lab in situ series, cleavage-stage expression
  is in "the large micromeres and veg2 descendents" [PMID:16581059], then in the ring of
  mesoderm cells, then the blastopore region/posterior archenteron, and finally midgut and
  hindgut of the pluteus [PMID:16581059].
- The pattern is a moving torus: expressed first in skeletogenic micromeres, then the
  non-skeletogenic mesoderm, then veg2 endoderm, shutting off centrally each time
  [PMID:18061160 "Their expression expands out to the presumptive mesodermal cells in early
  blastula stage, following which expression in the micromere descendents is extinguished;
  then expression disappears in mesodermal cells and expands to endodermal cells by early
  mesenchyme blastula stage"].

## Place in the GRN

### Inputs into blimp1b (the early cis-regulatory module)
- beta-catenin/Tcf (from Wnt8 signalling), Otx and Blimp1 itself (autorepression); confirmed by
  site mutagenesis in a BAC-GFP knock-in [PMID:18061160 "Here we confirm by mutation the inputs
  into the blimp1 cis -regulatory module predicted by network analysis. Its essential design
  feature is that it includes both activation and autorepression sites"].
- Tcf sites act as a Groucho-mediated toggle: mutating them causes ectopic ectodermal
  reporter expression [PMID:18061160 "We found that mutations in either one or both of the Tcf
  sites in construct 27 indeed produce a dramatic increase in ectopic gene expression"].
- Autorepression was first inferred from morpholino data [PMID:16581059 "We confirmed
  previously published data that blimp1/krox autoregulates its own expression, but discovered,
  surprisingly, that this gene represses rather than activates itself"] and then reconstructed
  at the cis-regulatory level [PMID:17975065 "A cis-regulatory reconstruction experiment
  revealed that blimp1 autorepression accounts for progressive extinction of expression in the
  center of the torus, whereas its outward expansion follows reception of the Wnt8 ligand by
  adjacent cells"].
- Later (24 h) blimp1b in veg2 endoderm depends on an Eve-controlled signal (V2) from veg1
  [PMID:21623371 "A second putative signal (V2) is expressed under the control of Eve and
  activates expression of blimp1b and gatae in veg2 endoderm precursors"]. Delta/Notch is
  required to clear blimp1b from mesoderm [PMID:21623371 "In embryos with perturbed expression
  of either Delta or Notch, the endodermal regulatory genes foxa, blimp1b and dachshund (dac)
  continue to be expressed in the presumptive mesodermal domain at 24 h"].

### Outputs (direct targets with mapped sites)
- **wnt8** (activation). Predicted from perturbation, then shown by site mutation
  [PMID:16289024 "the modular cis-regulatory system of the wnt8 gene of Strongylocentrotus
  purpuratus was characterized functionally, and shown to respond to blockade of both
  Blimp1/Krox and Tcf1/beta-catenin inputs just as does the endogenous gene. The genomic target
  sites for these factors were demonstrated by mutation in one of the cis-regulatory modules"];
  summarized as "Blimp1 is a direct input essential for wnt8 transcription" [PMID:18061160].
  In the micromere lineage this is Blimp1's only essential early job [PMID:18413610 "The
  blimp1 gene plays no other essential early role in the skeletogenic micromere lineage other
  than to provide input into the wnt8 gene"].
  *Caveat*: Peter & Davidson 2011 found that the Blimp1-site mutation that reduces a small
  wnt8 construct "does not affect expression of a bacterial artificial chromosome expression
  construct containing the whole genomic wnt8 cis-regulatory system" and exclude the model in
  which loss of Blimp1 clears wnt8 from mesoderm [PMID:21623371]. The activator function on
  the wnt8 module is therefore real at the module level but not the sole driver of wnt8 in the
  endogenous locus.
- **otx (beta1/2 module)** (activation, AND logic with Gatae and Otx) [PMID:15110718 "It
  requires gatae, otx, and krox inputs, as predicted, and it operates as an "AND" logic
  processor in that removal of any one of these inputs essentially destroys activity"].
- **hesC** (repression through an intronic Blimp1 site) [PMID:19104065 "Mutation of this site
  in a hesC reporter construct caused expression to remain strong in the NSM territory";
  "blimp1 mRNA overexpression nearly abolished expression of the hesC BAC-GFP reporter"]. This
  permits delta transcription in the NSM ("Blimp1 thus represses the repressor of delta ,
  thereby permitting its transcription").
- **notch** (repression) [PMID:19104065 "Mutation of a cis -regulatory Blimp1 site in the Notch
  gene ( Fig. S1 C ) causes massive vegetal expansion of expression of a Notch:GFP reporter
  construct into the NSM domain"].
- **even-skipped** (activation, with Tcf) [PMID:18061160 "We verify the cis-regulatory inputs
  of even-skipped predicted by network analysis. These include activation by β-catenin/Tcf and
  Blimp1"].
- **blimp1 itself** (autorepression; see above).
- Later endoderm outputs from perturbation (no sites mapped): brn1/2/4 and tgif
  [PMID:21623371 "Blimp1 then activates brn1/2/4 and tgif expression"]; the
  blimp1b-otx-gatae positive feedback loop [PMID:21623371 "The models proposed here include
  previously identified linkages such as the positive feedback circuit between blimp1b, otx
  and gatae"].

### Loss-of-function phenotype
- blimp1 MASO blocks endomesoderm specification [PMID:18061160 "Morpholino-substituted
  antisense oligonucleotide (MASO) targeting blimp1 blocks endomesoderm specification ( Livi
  and Davidson, 2007 ), just as does MASO directed against the wnt8 gene"]; the 1b form "is
  required for the early events of endomesoderm specification" [PMID:16581059]. Blimp1 MASO
  also leaves hesC on in the NSM and lowers delta ~3-fold [PMID:19104065 "these same embryos
  contained ≈3-fold lower levels of endogenous delta mRNA at 21 h by QPCR measurement"].

### Summary of the subcircuit
[PMID:19104065 "A general feature of this subcircuit is the extremely important role in its
logic played by repression: Blimp1 represses the hesC gene, HesC in turn represses the delta
gene, and Blimp1 represses the blimp1 gene as well as activating the wnt8 gene."]

## Other roles
- Germline: Blimp1 isoforms regulate germline determinants (vasa, nanos) in S. purpuratus and
  the sea star [PMID:40024498 "We found that Blimp1 is important for germ cell specification in
  both species and that multiple Blimp1 isoforms result from differential mRNA splicing in each
  animal"]. Abstract only; isoform not mappable to this accession with certainty, so recorded
  as a question rather than an annotation.
- Starfish orthologue AmKrox has a conserved vegetal ring expression [PMID:12915305].

## Curation decisions (2026-09-26)
- IBA/IEA rows for DNA-binding TF activity, cis-regulatory DNA binding, nucleus, regulation/
  negative regulation of Pol II transcription and repressor activity: ACCEPT (all confirmed by
  the cis-regulatory work above).
- cytoplasm IBA: KEEP_AS_NON_CORE (family-level inference, no sea urchin evidence; site of
  action is nuclear).
- cell fate commitment IBA and cellular developmental process IEA: MODIFY to the specific
  GO:0001714 endodermal cell fate specification.
- NEW: GO:0001228 activator activity (IDA; wnt8/otx module site mutagenesis), GO:0045944
  (IDA), GO:0001714 endodermal cell fate specification (IMP; blimp1 MASO). Positive regulation
  of Wnt/Notch signalling deliberately NOT proposed: Blimp1 controls transcription of the
  ligand/receptor genes, one step removed from the pathway, and the wnt8 BAC result makes the
  necessity claim uncertain.
- No GO-CAM contains Q2VF23 (gocams/index.tsv checked).
