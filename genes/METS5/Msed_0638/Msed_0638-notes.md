# Msed_0638 (A4YEG1) notes — methylmalonyl-CoA mutase, catalytic (alpha) subunit

Automated deep research was unavailable for this gene (no `*-deep-research-*.md`
file). The literature below was located manually (Europe PMC / NCBI E-utilities /
web search) and the cited PMIDs are cached in `publications/`.

## Identity and structure

- UniProt A4YEG1 (unreviewed), 553 aa, "Methylmalonyl-CoA mutase", EC 5.4.99.2.
  InterPro IPR006099 / IPR006098 / IPR016176 (MCM alpha/beta catalytic TIM-barrel),
  NCBIfam TIGR00641 (acid_CoA_mut_N), PANTHER PTHR48101:SF1 (MCM large subunit),
  CDD cd03680 (MM_CoA_mutase_ICM_like). The protein contains only the N-terminal
  substrate-binding TIM-barrel domain (Pfam PF01642, residues 31-546) and lacks the
  C-terminal Rossmann-type B12-binding domain that is fused to the catalytic domain in
  bacterial/human MCM alpha chains [file:METS5/Msed_0638/Msed_0638-uniprot.txt
  "Methylmalonyl-CoA mutase alpha/beta chain catalytic"].
- The B12-binding domain is encoded separately by Msed_2055 (UniProt A4YIE3,
  155 aa, "Cobalamin B12-binding domain protein", PANTHER PTHR48101:SF3; UniProt REST
  query 2026-11-01). Msed_2056 (A4YIE4, 314 aa, "LAO/AO transport system ATPase",
  PANTHER PTHR43087) is a MeaB/ArgK-like G-protein chaperone homolog.
- This split architecture (catalytic TIM-barrel subunit + separate B12-binding
  subunit) resembles isobutyryl-CoA mutase IcmA/IcmB rather than the classic bacterial
  MCM alpha/beta, in which the alpha chain carries both domains.

## Literature

- Ramos-Vera et al. 2011 assigned the M. sedula MCM genes by genomics:
  [PMID:21169482 "M. sedula as well as the other autotrophic members of the Sulfolobales clearly encode MCMs in their genome (e.g., small subunit Msed_2055 and large subunit Msed_0638)."]
  and noted the overlap with the ArgK-like gene
  [PMID:21169482 "Msed_2056 (ArgK-like) overlaps with the ORF encoding the small MCM subunit (cobalamin B12-binding domain protein Msed_2055), indicating the potential for cotranscription"].
  They also rebutted the suggestion that crenarchaeal MCM-like proteins are
  isobutyryl-CoA mutases [PMID:21169482 "This is clearly not true for Sulfolobales"].
  Note: their general statement that in bacterial MCMs "the small subunit binds the
  substrate and the cofactor" is not how classic heterodimeric MCMs work (the alpha
  subunit is catalytic); in M. sedula the substrate-binding TIM barrel is the large
  subunit Msed_0638.
- Han et al. 2012 (PMID:22752162) is the decisive paper: it named the genes, showed
  autotrophic upregulation of all three (Msed_0639, Msed_0638, Msed_2055), and made
  recombinant enzymes [PMID:22752162 "the gene encoding MCE (Msed_0639) is adjacent to that encoding the catalytic subunit of MCM-α (Msed_0638), while the gene for the coenzyme B(12)-binding subunit of MCM (MCM-β) is located remotely (Msed_2055)"];
  [PMID:22752162 "The expression of all three genes was significantly upregulated under autotrophic compared to heterotrophic growth conditions, implying a role in CO(2) fixation."];
  [PMID:22752162 "soluble, active MCM was produced only if MCM-α and MCM-β were coexpressed"];
  [PMID:22752162 "MCM is a heterotetramer (α(2)β(2))"];
  [PMID:22752162 "The conserved coenzyme B(12)-binding motif (DXHXXG-SXL-GG) was identified in M. sedula MCM-β."];
  [PMID:22752162 "The two enzymes together catalyzed the two-step conversion of (S)-methylmalonyl-CoA to succinyl-CoA, consistent with their proposed role in the 3-HP/4-HB cycle."]
  Only the abstract could be read (PMC full text blocked by captcha; Europe PMC
  full-text endpoint returned HTTP 500).
- Loder et al. 2016 (kinetic model of the cycle) relied on Han 2012 for MCE and MCM:
  [PMID:27771364 "characterization of MCE and MCM was reported previously (Han et al., 2012)"].
- Berg et al. 2007 (PMID:18079405) defined the cycle in M. sedula; its cached copy is
  abstract-only, which does not mention the mutase. Whether that paper's tables report
  MCM activity in M. sedula extracts could not be verified.

## Conclusions

- Msed_0638 is the catalytic (alpha, large) subunit of a B12-dependent alpha2beta2
  methylmalonyl-CoA mutase; Msed_2055 is the B12-binding beta subunit. Activity was
  shown for the coexpressed recombinant complex, and transcription is induced under
  autotrophy, so the enzyme acts in the 3HP/4HB cycle (recombinant activity + expression,
  not genetic proof).
- GO: GO:0004494 accepted (catalytic subunit carrying the substrate-binding site,
  active only within the alpha2beta2 complex). Cobalamin binding: the cofactor sits at the
  interface of the TIM barrel and the separate B12-binding subunit; the His ligand motif is
  on Msed_2055. Kept as non-core. Carbon fixation GO:0015977 added (NEW) as for siblings.
- Module change needed: the mcm annotons should include Msed_2055 (A4YIE3) as the
  B12-binding subunit (complex), and the knowledge gap about these steps should be revised
  given PMID:22752162.
