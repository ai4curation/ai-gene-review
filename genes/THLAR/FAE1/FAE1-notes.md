# FAE1 (Thlaspi arvense, field pennycress) — curation notes

## Identity

- UniProt V9XY07 (TrEMBL, 506 aa), gene name FAE1; cloned in a Brassicaceae-wide FAE1 survey
  [PMID:24358289 "Evolutionary pattern of the FAE1 gene in brassicaceae and its correlation with the erucic acid trait"].
- Chosen over the reference-proteome entry because it carries the gene name and literature. The
  reference proteome (UP000836841) entry is A0AAU9T3A1 / `TAV2_LOCUS26079`; it differs from V9XY07 at
  1 of 506 positions (identical to a third entry, A0A0S2SVW7). All three are the same gene
  (pairwise comparison of UniProt FASTA, this session).
- InterPro IPR012392 (3-ketoacyl-CoA synthase), IPR013601 (FAE1/type III PKS domain), PANTHER
  PTHR31561. Plant KCS family, ortholog of Arabidopsis FAE1/KCS18 (`genes/ARATH/FAE1`).

## Function

- Condensing enzyme (3-ketoacyl-CoA synthase) of the ER acyl-CoA elongase: condenses malonyl-CoA
  with C18:1/C20:1-CoA, the chain-length-determining first step producing eicosenoic (20:1) and
  erucic (22:1) acids.
- Wild pennycress seed oil is ~35-39% erucic acid, mostly in TAG
  [PMID:27889523 "Both lines showed a high amount (35-39%) of erucic acid (22:1Δ13) in their seed oil."].
  TaFAE1 is transcriptionally controlled, highly expressed early in seed development
  [PMID:27889523 "TaFAE1 gene, encoding the fatty acid elongase, seemed to be controlled at the transcriptional level"].
- Heterologous expression: pennycress FAE1 in Arabidopsis Col-0 gave a 3-4-fold increase in erucic acid;
  substrate preference for eicosenoyl over oleoyl
  [PMID:32740897 "Seed-specific expression of the Pennycress FAE1 gene in Col-0 resulted in a 3 to fourfold increase of erucic acid content in the seed oil."]
  (abstract only).
- Loss of function in pennycress itself: CRISPR fae1-3/-4/-5 alleles abolish erucic acid and nearly
  abolish eicosenoic acid in seed TAG
  [PMID:30230695 "The pennycress fae1‐3 mutant harbours a 4‐bp deletion in the TaFAE1 coding sequence, producing seed oil (triacylglycerols; TAG) with undetectable amounts of erucic acid (C22:1) and greatly reduced amounts of eicosenoic acid (C20:1)."].
- fae1 plants grow normally; embryos accumulate more oleic acid and starch; faster germination at 10 °C
  [PMID:39657724 "The results showed minimal differences in plant morphology and physiology between wild-type (WT) plants and the fatty acid elongation 1-3 (fae1-3) and fatty acid elongation 1-4 (fae1-4) knockout mutant alleles."].
- fae1 is the base of stacked high-oleic genotypes (fad2 fae1 ~90% oleic; rod1 fae1 ~60%)
  [PMID:33968108 "fad2 fae1 and rod1 fae1 double mutants produced ∼90% and ∼60% oleic acid in seed oil, respectively"]
  and of the domesticated "double-low" pennycress lines [PMID:41578087].

## Curation decisions (summary)

- MF fatty acid elongase activity (GO:0009922; defined by the KCS condensation reaction): ACCEPT.
- BP fatty acid biosynthetic process: MODIFY to very long-chain fatty acid biosynthetic process (GO:0042761).
  NEW IMP-grounded annotation for GO:0042761 from PMID:30230695.
- CC membrane: MODIFY to ER membrane; ER (ARBA): ACCEPT. No pennycress localization data; inferred
  from the conserved ER elongase complex (Arabidopsis KCS18 review).
- Generic acyltransferase parents: KEEP_AS_NON_CORE (true but uninformative; the specific MF is present).
- Not proposed: triglyceride biosynthetic process. FAE1 makes the acyl-CoA that DGAT1 etc. incorporate;
  FAE1 does none of the acylation steps.
- Not proposed: cuticular wax / suberin. FAE1 is the seed-specific KCS; epidermal VLCFA synthesis uses
  other KCSs (e.g. CER6/KCS6) in Arabidopsis; no pennycress data.
