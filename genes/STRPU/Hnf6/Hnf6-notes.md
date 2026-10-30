# Hnf6 (Sp-Hnf6 / SpOnecut; UniProt Q6UAY6) — curation notes

## Identity

- UniProt Q6UAY6 (TrEMBL) "One cut domain family member", gene `hnf6`, EMBL AAQ81630.1, NCBI GeneID 378468.
  The RX line of the UniProt record cites Otim et al. 2004 (PMID:15328009), i.e. the accession is the
  cDNA cloned by the Davidson lab for the GRN work, so there is no identity doubt between the accession
  and the GRN node.
- The same gene was cloned independently as "SpOnecut" by Poustka et al. 2004
  [PMID:15230963 "The isolated sea urchin gene, named SpOnecut, encodes a protein of 483 amino acids with one cut domain and a homeodomain."].
  The UniProt sequence is 483 aa, matching.
- Domain architecture: one CUT domain (residues 272-358) plus a C-terminal homeodomain (387-447),
  the defining ONECUT-class arrangement [PMID:15328009 "The Strongylocentrotus purpuratus hnf6 (Sphnf6) gene encodes a new member of the ONECUT family of transcription factors."].
  PANTHER PTHR14057 (official name "TRANSCRIPTION FACTOR ONECUT"), subfamily SF47 ("HOMEOBOX PROTEIN ONECUT").
- Sea star orthologue AmHNF6 confirms the family placement
  [PMID:15661644 "The vertebrate and the echinoderm hnf6 and onecut genes belong to the novel ONECUT homeo domain class of transcription factors."].

## Expression (triphasic)

1. Maternal and global: [PMID:15328009 "hnf6 is expressed maternally, and before gastrulation its transcripts are distributed globally."]
2. Oral ectoderm: after gastrulation the gene is part of the oral ectoderm GRN; it is one of the
   nodal-independent early oral ectoderm genes
   [PMID:19268450 "These are the early oral ectoderm and later ciliated band genes hnf6 and otxβ1/2"].
3. Ciliated band: [PMID:15328009 "The third role is in the neurogenic ciliated band, which is foreshadowed exactly by a trapezoidal band of hnf6 expression at the border of the oral ectoderm and where it continues to be expressed through the end of embryogenesis."];
   Poustka et al. independently found [PMID:15230963 "In the sea urchin embryo, expression is first detected in the emerging ciliary band at the late blastula stage. During the gastrula stage, expression is limited to the ciliary band."]
   and called it [PMID:15230963 "the first gene known that exclusively marks the ciliary band and therein the apical organ in a pluteus larva"].
   (Poustka did not detect the earlier ubiquitous maternal phase; Otim et al. did by QPCR/WMISH.)
   The ciliary-band phase is conserved in the sea star
   [PMID:15661644 "As is observed in sea urchin, by the end of gastrulation, the expression of AmHNF6 is distinctly localized to the ciliary bands."].

## Function in the GRN (loss-of-function, morpholino)

- Skeletogenic (PMC) lineage: Hnf6 is an early, ubiquitously present input into the PMC
  differentiation gene battery, but not into the PMC regulatory genes
  [PMID:15328009 "Early in development, its expression is required for the activation of PMC differentiation genes such as sm50, pm27, and msp130, but not for the activation of any known PMC regulatory genes, for example, alx, ets1, pmar1, or tbrain."].
  It is not needed for the micromere signal
  [PMID:15328009 "Micromere transplantation experiments show that the gene is not involved in early micromere signaling."].
  Oliveri et al. 2008 place it in the skeletogenic GRN as a driver of differentiation genes
  [PMID:18413610 "these differentiation genes require as drivers products of all of the now familiar components of the skeletogenic regulatory state ( alx1 , ets1 , tbr , tel , erg , hex , foxb , dri ) and in addition a factor that is at this stage ubiquitously present, Hnf6 ( 42 )."]
  and describe its role as an ancillary booster rather than a lineage-specifying input
  [PMID:18413610 "Indeed one such factor is included in the micromere lineage GRN ( hnf6 ) and its ancillary “booster” function is illustrative."].
  Summarised by the same group as [PMID:15661644 "The sea urchin transcription factor SpHNF6 is an early activator of differentiation genes in skeletogenic lineages and regulatory genes in the oral ectoderm."].
- Mesoderm: [PMID:15328009 "Early hnf6 expression is also required for expression of the mesodermal regulator gatac."]
  (not annotated: single downstream regulatory gene, direct/indirect unknown).
- Oral ectoderm: [PMID:15328009 "The second known role of hnf6 is its participation after gastrulation in the oral ectoderm gene regulatory network (GRN), in which its expression is essential for the maintenance of the state of oral ectoderm specification."].
  In the Su et al. 2009 oral/aboral ectoderm GRN model, hnf6 is one of four early components of the
  oral regulatory state and is nodal-independent
  [PMID:19268450 "there appear to be four early genetic components producing the initial zygotic transcriptional regulatory state in the specification of the oral ectoderm: the nodal independent hnf6, and otxβ1/2 genes; the nodal dependant gsc repressor, and the nodal dependant foxg activator."];
  hnf6 knockdown, like dri or gsc knockdown, lets the aboral marker spec1 spread over the whole ectoderm
  [PMID:19268450 "knock-down of dri (Amore et al., 2003), of hnf6 (Otim et al., 2004), or of gsc (Angerer et al., 2001), all cause expression of spec1 to spread around the whole ectoderm"].
- Ciliated band: [PMID:15328009 "Neither oral ectoderm regulatory functions nor ciliated band formation occur normally in the absence of hnf6 expression."]

## Curation decisions

- GOA has only two IEA rows (DNA binding; nucleus). Both are consistent with a CUT+homeodomain TF.
  `DNA binding` is modified to the more informative GO:0000981; `nucleus` accepted (inferred from
  domain content and TF function; no sea urchin immunolocalisation published).
- NEW: GO:0000981 (IMP, Otim 2004), GO:0045944 positive regulation of transcription by RNA polymerase II
  (IMP; knockdown abolishes activation of sm50/pm27/msp130), GO:0070169 positive regulation of biomineral
  tissue development (IMP; the activated genes are the spicule-matrix/biomineralization battery, as for
  the sibling Dri review), GO:0001715 ectodermal cell fate specification (IMP; maintenance of oral
  ectoderm specification, spec1 spreading on knockdown; same term used for Dri).
- Not annotated: ciliated band formation (no GO term exists; proposed as a new term), gatac
  dependence (single downstream regulatory gene), micromere signaling (explicitly negative).
- The proposed GO:0000981 is used rather than the activator child GO:0001228 because no
  cis-regulatory analysis demonstrates direct binding of Hnf6 to a target module; the activator
  inference rests on loss-of-function.
- Only abstracts are cached for Otim 2004, Otim 2005 and Poustka 2004; Oliveri 2008 and Su 2009 are
  full text. A PubMed search (Otim O[Author] AND Davidson EH[Author]) returned no separate Hnf6
  cis-regulatory paper, so none is cited.
