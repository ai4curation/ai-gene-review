# elo-5 (C. elegans, UniProt Q20300) - manual literature research

No deep-research API provider was available for this session, so this file was
compiled manually from cached full-text publications (publications/PMID_*.md),
PubMed searches and the UniProt record (elo-5-uniprot.txt).

## Identity and family

- ELO-5 (F41H10.7, WBGene00001243) is a 274-aa multi-pass membrane protein of the
  ELO family (Pfam PF01151, InterPro IPR002076; PANTHER PTHR11157:SF29). ELO
  proteins are the condensing enzymes (3-ketoacyl-CoA synthases) of the
  ER-resident fatty acid elongation cycle (elo-5-uniprot.txt, "SIMILARITY:
  Belongs to the ELO family").
- elo-5 lies in tandem with elo-6 (F41H10.8) on chromosome IV.

## Biochemical function

- Kniazeva et al. 2004 identified ELO-5 and ELO-6 as the elongases that produce
  the monomethyl branched-chain fatty acids (mmBCFAs) C15ISO and C17ISO
  [PMID:15340492 "We show that C. elegans synthesizes mmBCFAs de novo and
  utilizes the long-chain fatty acid elongation enzymes ELO-5 and ELO-6 to
  produce two mmBCFAs, C15ISO and C17ISO."].
- RNAi of elo-5 strongly reduced both C15ISO and C17ISO, while elo-6 RNAi
  reduced only C17ISO [PMID:15340492 "The RNAi of elo-6 significantly reduced
  the amount of only C17ISO, while the RNAi of elo-5 dramatically reduced
  quantities of both C15ISO and C17ISO"]. The authors propose ELO-5 elongates
  the C13ISO primer to C15ISO (and may contribute to C17ISO), and ELO-6
  elongates C15ISO to C17ISO.
- Evidence is genetic plus GC lipid profiling; no in vitro enzyme assay with
  purified/heterologously expressed ELO-5 is reported in these papers. UniProt
  nevertheless records the reactions 11-methyldodecanoyl-CoA + malonyl-CoA ->
  3-oxoisopentadecanoyl-CoA (RHEA:35291) and isopentadecanoyl-CoA +
  malonyl-CoA -> 3-oxoisoheptadecanoyl-CoA (RHEA:35335) citing PMID:15340492.
- elo-5 RNAi did not affect straight-chain saturated or polyunsaturated FA
  elongation, which is attributed to elo-1/elo-2 in the same screen
  [PMID:15340492 "suppression of elo-1 (F56H11.4) and elo-2 (F11E6.5) affected
  the elongation of straight long-chain saturated and polyunsaturated FAs"].

## Physiological role

- elo-5(RNAi) progeny and the deletion allele elo-5(gk208) arrest at L1; the
  arrest is rescued by dietary C17ISO (and partially C15ISO), but not by
  straight-chain FAs [PMID:15340492 "This allele phenocopies the L1 arrest
  phenotype of the elo-5(RNAi) animals."; "As predicted, the C17ISO and
  C17anteISO supplements rescued the elo-5 RNAi defects"].
- Expression: elo-5 promoter::GFP in intestine and head cells (amphid
  neurons) [PMID:15340492 "Transcriptional reporter constructs (elo-5Prom::GFP
  and elo-6Prom::GFP) indicated that both genes are expressed in the gut"].
- Regulation: elo-5 transcription is reduced by lpd-1 (SREBP homolog) RNAi
  [PMID:15340492 "We present results suggesting that elo-5 and elo-6 may be
  transcriptional targets of LPD-1."].

## Downstream: mmBCFA-derived sphingolipids

- C15ISO-CoA is the SPT substrate that gives the C. elegans-specific
  d17iso sphingoid base. elo-5 mutants lack d17iso-sphingolipids and make
  abnormal straight d16 sphingoid bases instead [PMID:23705068 "In contrast to
  wild type animals, elo-5(-);ku540 animals had ceramides and
  glucosylceramides containing straight chain d16LCB rather than d17isoLCB"].
- d17iso-sphinganine rescues elo-5 L1 arrest, and the essential mmBCFA role is
  mediated by d17iso-glucosylceramide acting via NPRL-2/3 and TORC1
  [PMID:23705068 "We thus conclude that mmBCFAs promote postembryonic
  development through d17iso-SPA."].
- Lipidomic profiling confirms that elo-5 RNAi reduces nearly all ceramides and
  most sphingomyelins [PMID:38704027 "nearly all 47 quantifiable sphingolipid
  species found in young adult worms were reduced upon RNA interference (RNAi)
  of sptl-1 or elo-5, which are both required for synthesis of the id17:1
  sphingoid base"].

## Other literature (abstract-level, not cached)

- PMID:34826420 (Vieira et al. 2021, J Biol Chem): mmBCFAs (elo-5) required for
  survival under elevated dietary glucose; B. subtilis (mmBCFA-rich) rescues.
- PMID:37245562 (Xatse et al. 2023, J Lipid Res): targeted lipidomics of elo-5
  RNAi animals; changes in mmBCFA-containing and other lipid species, including
  GlcCer 17:1;O2/22:0;O.

## Gaps

- No direct biochemical assay of ELO-5 substrate specificity (e.g. yeast
  expression with iso-branched acyl-CoA primers).
- Subcellular localization of ELO-5 not experimentally shown; ER membrane is
  inferred from the family.
