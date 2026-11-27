# GstO1 (CG6662, Q9VSL6) - manual literature research

No deep-research API provider was available for this review; this file records a manual
literature survey (PubMed searches plus cached full texts in `publications/`).

PubMed query used: `(CG6662 OR GstO1 OR "glutathione S-transferase omega") AND Drosophila`
(13 hits, October 2026).

## Identity and nomenclature (important)

- Q9VSL6 is the product of FlyBase FBgn0035907, gene symbol GstO1, annotation ID CG6662,
  GeneID 38975, on chromosome 3L in the Omega-class GST cluster (66D) together with
  `se` (sepia, CG6781), GstO2 (CG6673) and GstO3 (CG6776).
- **Nomenclature trap.** Kim et al. 2012 (PMID:22219196) called CG6673 "DmGSTO1"
  [PMID:22219196 "CG6673 is also called D. melanogaster GSTO1 (DmGSTO1)"]. CG6673 is now
  FlyBase GstO2 (Q9VSL5/Q9VSL4). Hossain et al. 2023 make this explicit
  [PMID:37389657 "Drosophila GstO1 (CG6662) is 37.3% identical and 62.2% similar to human GSTO1. CG6673 was originally named DmGSTO1 (Kim et al., 2012), but later renamed as GstO2 (Kim and Yim, 2013)."].
  Therefore the parkin / ATP synthase beta glutathionylation / DHAR in vivo findings of
  PMID:22219196 belong to GstO2, not to this gene. The only CG6662 statements in that
  paper are that its function was unknown, that it is mainly expressed in ovary and testis
  [PMID:22219196 "Although the function of CG6662 is not known, CG6662 transcripts are primarily expressed in the ovary and testes"],
  and a negative result
  [PMID:22219196 "Another DmGSTO, CG6662, did not affect glutathionylation of the ATP synthase β subunit"].

## Enzymology

- Kim et al. 2006 (PMID:16712527, full text) cloned five Omega GST candidates from the
  sepia locus, including CG6662, expressed them in E. coli and assayed them:
  [PMID:16712527 "All cloned and expressed candidates exhibited relatively high thiol transferase and dehydroascorbate reductase activities and low activity towards 1-chloro-2,4-dinitrobenzene, characteristic of Omega class GSTs, whereas only CG6781 catalysed the synthesis of PDA in vitro ."]
  So CG6662 has GSH-dependent thiol transferase and dehydroascorbate reductase (DHAR)
  activity, weak CDNB-conjugating activity, and no PDA (pyrimidodiazepine) synthase
  activity. (The per-enzyme values of Table 2 are not in the cached text.)
- Saisawang et al. 2012 (PMID:22082028, abstract only) expressed and kinetically surveyed the
  Drosophila cytosolic GST proteome; FlyBase curated GST activity and glutathione metabolic
  process to GstO1 from this paper
  [PMID:22082028 "The diverse kinetic properties as well as physiological substrate specificity of the DmGSTs are such that each individual enzyme displayed a unique character even compared with members from the same class."].
- Sequence: GstO1 has the Omega-class N-terminal extension and the active-site motif
  C30-P-Y-A (residues 30-33 of Q9VSL6, from the UniProt sequence), consistent with the
  catalytic cysteine of Omega GSTs [PMID:16712527 "Members of this class have a unique N-terminal extension, and a cysteine residue at the active site, rather than the tyrosine and serine residues found in the active sites of other eukaryotic GSTs"].
  InterPro IPR005442 (GST_omega), PANTHER PTHR43968:SF6, CDD cd03184 GST_C_Omega.

## In vivo function

- **Protein S-glutathionylation of the BMP ligand Gbb (Hossain et al. 2023, PMID:37389657, full text).**
  An RNAi screen in postsynaptic muscle identified GstO1; null mutants (CRISPR GstO1[6-11],
  piggyBac insertion) are viable and fertile but have NMJ overgrowth with increased BMP
  signalling (pMad). GstO1 binds Gbb (co-IP with endogenous Flag-GstO1) and is needed for
  Gbb glutathionylation
  [PMID:37389657 "We found that Gbb was glutathionylated in WT (Fig. 6 A), but no glutathionylation of Gbb was detected in the absence of GstO1; conversely, Gbb glutathionylation was elevated when GstO1 was overexpressed in postsynaptic muscles compared with WT (Fig. 6 A)."].
  Glutathionylation at Gbb Cys354/Cys420 promotes Ctrip-dependent ubiquitination and
  proteasomal degradation; Grx1 opposes GstO1. Note that a cell-free assay with
  recombinant GstO1 was not reported; the in vitro glutathionylation of the Gbb fragment
  used diamide/GSH chemically.
- **Localisation.** In larval muscle GstO1 co-localises with the ER marker KDEL and partly
  with Rab5 and Rab11 endosomes
  [PMID:37389657 "These results together show that GstO1 is localized at ER and early/recycling endosomes, but not at late endosomes."].
  The protein has no predicted signal peptide or TM segment in UniProt, so this is most
  likely association with the cytosolic face of these membranes.
- **Oxidative stress (Lee et al. 2015, PMID:26024591, abstract only).** GstO1 is highly
  expressed in adult heads; loss-of-function flies are H2O2-sensitive, rescued by
  neuronal GstO1, with reduced ERK/MAPK activation
  [PMID:26024591 "We further showed that GstO1 inhibits H2O2-mediated activation of the mitogen-activated protein kinase (MAPK) pathway."].
- **Ethanol sedation (Choi et al. 2018, PMID:30347459, abstract only).** GstO1 mutants are
  hypersensitive to ethanol sedation; neuronal (dopaminergic/serotonergic) knockdown
  reproduces it [PMID:30347459 "GstO1 mutant flies showed highly increased ethanol sensitivity."].
- Review (Kim et al. 2017, PMID:29435097) summarises the Drosophila GstOs and states that all
  isoforms have high thiol transferase and DHA reductase activities
  [PMID:29435097 "Furthermore, all isoforms of GSTOs have high thiol transferase and DHA reductase activities, characteristic of GSTOs, and low activity toward 1-chloro-2,4-dinitrobenzene (CDNB), a general GST substrate [27]."].
- Hanna et al. 2015 (PMID:25585352) report "GSTO1" up-regulation in dopamine synthesis
  mutants; gene identity relative to FlyBase GstO1 vs GstO2 was not checked and the paper is
  expression-only, so it is not used for annotation.
- Cha et al. 2022 (PMID:36437507, abstract only; gene name stripped from the abstract text)
  reports GSTO knockdown increasing Cabeza/FUS mislocalisation; which GstO was studied cannot
  be determined from the cached abstract, so it is not used.

## Summary

GstO1 is an Omega-class GST with the classic Omega activities (GSH-dependent thiol
transferase / DHAR, weak CDNB conjugation) and no PDA synthase activity. Its best-characterised
in vivo role is promoting S-glutathionylation of the BMP ligand Gbb in muscle, which targets
Gbb for ubiquitin-proteasome degradation and restrains NMJ growth. Loss-of-function also
causes H2O2 and ethanol hypersensitivity (abstract-level data).
