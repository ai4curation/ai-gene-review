# Lim1 (Sp-Lim1 / lim1, UniProt Q7YT18, GeneID 373522) — curation notes

## Identity

- UniProt Q7YT18 (TrEMBL) is "Lim homeodomain transcription factor 1", 480 aa, cDNA AY339649
  submitted by Oliveri & Davidson (JUL-2003) under the title "SpLim1, a Lim Homeodomain
  Transcription Factor Involved in Sea Urchin Oral Ectoderm Specification", from oral-ectoderm
  tissue (uniprot.txt RN [1]). This is the S. purpuratus gene called lim1 in the Davidson-lab
  ectoderm GRN papers, and the ortholog of Hemicentrotus HpLim1 and vertebrate Lhx1/Lhx5
  (CDD cd09367 LIM1_Lhx1_Lhx5, cd09375 LIM2_Lhx1_Lhx5; InterPro IPR049618/IPR049619
  Lhx1/5 LIM domains; PANTHER PTHR24208, official name "LIM/HOMEOBOX PROTEIN LHX" from
  interpro/panther/panther.obo).
- Domain structure (H. pulcherrimus ortholog): "HpLim1 contains two LIM domains and a LIM-class
  homeodomain, and amino acid sequences of these three domains are highly homologous to
  corresponding domains of Lim1 of other animals." [PMID:10400389]
- GO-CAMs: `gocams/index.tsv` has no S. purpuratus entries, so there is no model to reconcile.

## Place in the GRN — ectoderm/endoderm border, NOT veg2 endoderm

The working brief placed lim1 among the veg2 endoderm genes of Peter & Davidson 2010/2011.
That is not supported by the cached texts: neither PMID:19895806 nor PMID:21623371 mentions
lim1 at all (grep of both full texts). In every paper that does discuss it, lim1 is an
ectodermal regulatory gene expressed in the ring of ectoderm abutting the vegetal
endomesoderm (the "veg1 oral ectoderm" of the Davidson lab; the "border ectoderm", BE, of the
McClay lab; the "lower margin" of the ectoderm in Su et al.).

- Su et al. 2009 (S. purpuratus, oral/aboral ectoderm GRN, full text): "there is a separate
  domain along the interface with the vegetal endomesoderm that extends all across both oral
  and aboral ectoderm, as indicated by expression of the lim1 gene (Kawasaki et al. 1999)"
  [PMID:19268450]; "the lim1 gene, which is expressed along the lower margin of both oral and
  aboral ectoderm" [PMID:19268450]; and, within the aboral ectoderm, "The only subdivision
  within it is that mentioned above, the lim1 domain immediately adjacent to the vegetal
  endomesoderm border." [PMID:19268450]. lim1 is listed among the genes activated the same
  with or without nodal, i.e. it is Nodal-independent in S. purpuratus.
- Li, Materna & Davidson 2012 (S. purpuratus, full text): lim1 is one of the "veg1 oral
  ectoderm regulatory genes"; the Not homeodomain repressor does not control it: "no effects
  were seen on expression of the other veg1 oral ectoderm regulatory genes nk2.2 and lim1"
  [PMID:22771578].
- McIntyre et al. 2013 (Lytechinus variegatus, full text): Lim1 is the earliest BE marker:
  "The earliest marker expressed in the BE was Lim1. It was expressed throughout the BE
  beginning at 8 hpf and was diminished by gastrulation." [PMID:24227654]. The BE genes are
  activated by a short-range Wnt5 signal from the endoderm: "This signal activates a unique
  subcircuit of the ectoderm gene regulatory network, including the transcription factors
  IrxA, Nk1, Pax2/5/8 and Lim1, which are ultimately restricted to subregions of the border
  ectoderm (BE)." [PMID:24227654]; Nodal and BMP2/4 restrict rather than activate the BE genes.
  Note the species: this is L. variegatus, not S. purpuratus, and lim1 itself was not knocked
  down (only Wnt5, Nodal, BMP2/4 were perturbed).
- Saudemont et al. 2010 (Paracentrotus lividus, full text) disputes the "oral-specific"
  reading of Su et al.: "we showed that the expression of onecut/hnf6, otx2, lim1, and foxA in
  the presumptive ectoderm region of Nodal morphants was not regionalized, consistent with the
  absence of any oral territory in these embryos." [PMID:21203442]. Either way lim1 is
  regionalised along the animal-vegetal axis by inputs other than Nodal.
- Kawasaki et al. 1999 (Hemicentrotus pulcherrimus, abstract only) is the founding paper:
  "Accumulation of HpLim1 transcripts begins at hatching, and declines after the mesenchyme
  blastula stage. HpLim1 mRNA was localized in the vegetal plates of hatched blastulae, but it
  was not detectable in primary mesenchyme cells (PMC) ingressed into the blastocele."
  [PMID:10400389]. Gain-of-function: "HpLim1 mRNA-injected embryos became spherical with
  markedly reduced gut formation, failed to express marker proteins for aboral ectoderm and
  mesoderm, and mainly expressed an oral ectoderm marker." [PMID:10400389]. The authors'
  inference is that "ectopic expression of HpLim1 suppresses normal differentiation directing
  all embryonic cells to differentiate into oral ectoderm." [PMID:10400389]. This is the
  likely origin of the "oral ectoderm specification" wording on the UniProt submission.
- Howard-Ashby et al. 2006 (S. purpuratus homeobox survey, abstract only) is the genome-wide
  QPCR/WMISH catalogue of homeobox genes; the abstract does not name lim1, so its lim1 data
  cannot be quoted from the cache [PMID:17055477].
- Li et al. 2014 PNAS (abstract only) maps "all spatially expressed oral ectoderm regulatory
  genes" and the repressors that set the endoderm/ectoderm boundary [PMID:24556994]; lim1 is
  presumably among them but the abstract does not name it.

## What the evidence does and does not support for GO

- MF/CC: LIM-homeodomain TF; GO:0000981 and nucleus are supported by the family (IBA/IEA) and
  by the behaviour of lim1 as a regulatory gene in all GRN papers. No S. purpuratus DNA-binding
  or reporter assay for Lim1 exists in the cached literature.
- BP: the only S. purpuratus-specific evidence is expression (border/veg1 ectoderm) and the
  negative perturbation result (Not-independent). Upstream-input perturbations (Wnt5, Nodal,
  BMP2/4) are from L. variegatus; the gain-of-function phenotype is from H. pulcherrimus. No
  lim1 knockdown has been reported in any sea urchin in the cached papers, so no direct
  cell-fate specification term can be asserted. I propose a single IEP-level NEW row
  (GO:0007398 ectoderm development) and leave fate-specification terms as questions.
- The IBA "neuron differentiation" (GO:0030182) comes from the Lhx1/Lhx5 PAINT node; the
  BE/ciliary-band region where lim1 is expressed is neurogenic in sea urchins, but no
  sea-urchin data test this, so it is kept as non-core.
