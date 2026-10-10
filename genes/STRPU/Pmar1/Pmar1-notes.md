# Pmar1 (Q8WRE9, Strongylocentrotus purpuratus) — curation notes

## Identity

- UniProt Q8WRE9 (unreviewed, TrEMBL) is the original *pmar1* cDNA clone
  (EMBL AAL38537, "Paired class homeodomain repressor", gene name PMAR1) reported
  by Oliveri, Carrick & Davidson 2002. 237 aa; homeobox at residues 19-79
  (PROSITE PS50071); PANTHER PTHR45793 / SF5 (id not asserted in the review, see
  CLAUDE.md rule on PANTHER labels).
- *pmar1* is not a single-copy gene: "there is a cluster of several very similar
  pmar1 genes" [PMID:18413610 "The first genes in the sequence are the pmar1 genes
  (there is a cluster of several very similar pmar1 genes)."]. The euechinoid
  *hbox12/pmar1/micro1* family shows extensive copy-number variation and
  species-specific divergence in *Paracentrotus* [PMID:28350855 "Diversification
  of spatiotemporal expression and copy number variation of the echinoid
  hbox12/pmar1/micro1 multigene family."]. The *Hemicentrotus* orthologue is
  *micro1* [PMID:16078091, title]. Q8WRE9 therefore stands for one member of a
  near-identical cluster; the perturbation literature (mRNA injection, En-fusion,
  chimera rescue) addresses the family product, not a specific copy.

## What the gene does (GRN placement)

- Paired-class homeodomain **transcriptional repressor**, expressed only in
  micromeres during cleavage/early blastula: "pmar1 is expressed only during
  cleavage and early blastula stages, and exclusively in micromeres. It is
  initially activated as soon as the micromeres are formed, in response to Otx and
  beta-Catenin/Tcf inputs." [PMID:12027443].
- Timing: "Expression of pmar1 in the micromere lineage ( Fig. 2 B ) is specific
  and transient, detectable initially right at late fourth cleavage, and gone 12–15
  h later." [PMID:18413610]; peak transcript at 8 h post-fertilization
  [PMID:18413610 "the peak of pmar1 transcript accumulation in the skeletogenic
  micromeres is at 8 h"].
- Inputs: nuclear beta-catenin/Tcf plus Otx [PMID:18413610 "The pmar1 genes are
  activated by the β-catenin/Tcf transcription complex plus Otx"].
- Output: the **double-negative gate**. Pmar1 represses *hesC*, the globally
  expressed second repressor; hesC in turn represses *delta*, *alx1*, *ets1*,
  *tbr*, *tel* everywhere except the micromeres [PMID:17636127 "A gene encoding a
  transcriptional repressor, pmar1 , is activated specifically in micromeres,
  where it represses transcription of a second repressor that is otherwise active
  globally."; PMID:18413610 "HesC is expressed zygotically early in cleavage, in
  all cells of the embryo except the micromeres, where Pmar1 prevents its
  expression."].

## Key evidence

### Repressor function (PMID:12027443, abstract only)

- Forced global expression of Pmar1 mRNA and of an Engrailed-Pmar1 repressor
  fusion have identical effects, i.e. derepression of *delta* and of the
  skeletogenic gene battery, converting most of the embryo into skeletogenic
  mesenchyme: "The repressive nature of the interactions mediated by the pmar1
  gene product was shown by the identical effect of introducing mRNA encoding the
  Pmar1 factor, and mRNA encoding an Engrailed-Pmar1 (En-Pmar1) repressor domain
  fusion. In both cases, the effects are derepression: of the delta gene; and of
  skeletogenic genes" [PMID:12027443]. "This results in transformation of much of
  the embryo into skeletogenic mesenchyme cells that express skeletogenic
  markers." [PMID:12027443].
- Revilla-i-Domingo 2007 restates the inference: "It follows that the pmar1 gene
  product naturally acts as a repressor (also indicated by its sequence)"
  [PMID:17636127].

### Pmar1 is necessary and sufficient for micromere specification (PMID:12781680, abstract only; PMID:18413610 full text)

- Chimera/transplant rescue: beta-catenin-blocked micromeres are unspecified;
  adding Pmar1 rescues all micromere functions: "When such beta-catenin-blocked
  micromeres also express Pmar1, all observed micromere functions are rescued.
  The rescue includes expression of the primary mesenchyme cell (PMC)
  differentiation program, expression and execution of the Delta signal to induce
  secondary mesoderm cell (SMC) specification in macromere progeny, and expression
  of the early endomesoderm induction signal" [PMID:12781680].
- Conclusion: "Pmar1 is an important transcription factor necessary for
  initiating the micromere specification program and for the expression of two
  inductive signals produced by micromeres." [PMID:12781680].
- "So pmar1 is necessary and sufficient; no other β-catenin/Tcf target need be
  involved." [PMID:18413610]. Ectopic-fated cells work too: "This transplantation
  experiment can even be done successfully with cells from the part of the embryo
  normally fated to become ectoderm providing they contain pmar1 mRNA."
  [PMID:18413610].

### hesC is the Pmar1 target (PMID:17636127, full text)

- Screen: 46 regulatory genes assayed by QPCR after pmar1 mRNA overexpression;
  *hesC* among the five down-regulated at 9 and 12 h: "Five of the 46 regulatory
  genes tested were found to be significantly down-regulated at both time points
  in the two experiments performed. These genes were six3 , smadIP , awh , hesC ,
  and foxJ1" [PMID:17636127].
- hesC MASO phenocopies pmar1 MOE: "As logically required, blockade of hesC mRNA
  translation and global overexpression of pmar1 mRNA have the same effect, which
  is to cause all of the cells of the embryo to express micromere-specific
  genes." [PMID:17636127].
- Directness caveat: "Although this remains to be finally authenticated by
  identification of the cis -regulatory target sites, HesC interactions with the
  target genes of Fig. 1 D are likely to be direct, as is likely to be the
  interaction of Pmar1 with the hesC regulatory apparatus." [PMID:17636127]. No
  Pmar1 binding site on hesC has been mapped in any cached paper.

### delta cis-regulation responds to the Pmar1 system (PMID:15385170, abstract only)

- R11 element ~13 kb downstream of delta "responds to the pmar1 repression system
  just as predicted for the delta gene in the endomesoderm GRN" [PMID:15385170].
  This is an indirect readout (Pmar1 -| HesC -| delta), useful for the repressor
  logic but not for a direct Pmar1 target.

### Complications to the simple gate (PMID:20181745, abstract only; PMID:32001441, abstract only)

- Sharma & Ettensohn 2010: alx1 and delta are activated before hesC is
  downregulated; "We postulate the existence of additional, unidentified
  repressors that are controlled by pmar1, and propose that the ability of pmar1
  to derepress alx1 and delta is regulated by the unequal division of vegetal
  blastomeres." [PMID:20181745]. So Pmar1 likely has hesC-independent repressive
  targets.
- Yamazaki 2020: cidaroid pmar1 and starfish phb "promote activation of
  endomesoderm regulatory gene orthologs via an unknown repressor that is not
  HesC" [PMID:32001441] — the Pmar1-hesC link is a euechinoid innovation.

## Curation decisions

- IEA `DNA binding` (homeobox InterPro/UniRule): ACCEPT — correct domain-level
  inference for a homeodomain protein; the informative claim (repressor activity)
  is added as NEW rather than by rewriting the IEA row.
- IEA `nucleus`: ACCEPT — a transcriptional repressor acting on hesC
  transcription; no direct localization data, but the inference is sound.
- NEW GO:0001227 (DNA-binding transcription repressor activity, RNA polymerase
  II-specific), IMP, PMID:12027443 (+17636127): sign of activity established by
  En-Pmar1 equivalence and hesC down-regulation.
- NEW GO:0000122 (negative regulation of transcription by RNA polymerase II),
  IMP, PMID:17636127: hesC transcript falls on forced Pmar1 expression.
- NEW GO:0007501 (mesodermal cell fate specification), IMP, PMID:12781680
  (+18413610, 12027443): Pmar1 is the lineage-initiating regulator whose
  expression is necessary and sufficient to specify skeletogenic (mesodermal)
  micromere fate; passes the participation test because Pmar1 itself performs
  the first regulatory step of the specification circuit.
- Not proposed: Notch signalling / Delta expression, endoderm induction,
  skeletogenesis — downstream consequences of the gate, performed by other gene
  products (Delta, HesC targets, ES ligand).
- gocams/index.tsv has no entry for Q8WRE9.
