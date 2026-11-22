# fliI (Helicobacter pylori J99, Q9ZJJ3, jhp_1315) — review notes

## Identity
- UniProt Q9ZJJ3 (FLII_HELPJ), 434 aa, locus jhp_1315. Same-species ortholog in strain 26695 is
  O07025 (HP_1420); the two UniProt entries carry identical (template) annotation text.
- UniProt RecName "Flagellum-specific ATP synthase", EC=7.1.2.2 (H+-transporting two-sector
  ATPase), catalytic activity RHEA:57720 (ATP + H2O + 4 H+(in) = ADP + Pi + 5 H+(out)),
  evidence ECO:0000255 PROSITE-ProRule PRU10106 (ATPase alpha/beta chain signature). This is a
  family-signature transfer from F1-beta; the appropriate EC for a T3SS/flagellar export ATPase is
  EC 7.4.2.8 "protein-secreting ATPase" (ExPASy ENZYME; comment lists Type III secretion ATPases).
- The UniProt FUNCTION text ("...or a proton translocase involved in local circuits at the
  flagellum") is a historical speculation predating the Salmonella energetics work.
- Domains: IPR005714 (ATPase_T3SS_FliI/YscN), IPR000194 (F1/V1/A1 a/b nucleotide-binding),
  IPR020003 (ATPase a/b active site), IPR040627 (T3SS ATPase C-term). PANTHER PTHR15184:SF9
  ("SPI-1 TYPE 3 SECRETION SYSTEM ATPASE" — a T3SS/FliI subfamily, not the F1-beta subfamily).

## H. pylori experimental evidence (not J99 specifically)
- Jenks et al. 1997 (strain N6 per UniProt O07025 citation): fliI isogenic mutant non-motile,
  >99% aflagellate, reduced flagellin and hook [PMID:9231413 "An isogenic mutant of fliI was
  non-motile and synthesised reduced amounts of flagellin and hook protein subunits. The majority
  (> 99%) of mutant cells were completely aflagellate."]
- Porwollik et al. 1999 (strain CCUG 17874): fliI in operon with virB11, fliQ; fliI mutant
  aflagellate [PMID:10225855 "Engineered fliI and fliQ mutant strains were completely aflagellate
  and nonmotile"].
- Lane et al. 2006: FliI residues 1-18 bind FliH; residues 21-91 resemble the F1 N-terminal
  oligomerization domain; FliH suggested to act as a stator-like component [PMID:16260786
  "residues 1-18 of FliI were essential for the FliI/FliH interaction"; "This similarity suggests
  that FliH may function as a molecular stator."]
- Dhindwal et al. 2024: H. pylori FlgN (HP1120) chaperone binds FliI and FliI(2-92) with
  sub-micromolar Kd [PMID:38151822 "FlgN Δ 126–144 , like FliT, binds with sub‐micromolar affinity
  to the flagellum ATPase FliI or its N‐terminal domain"].
- No ATPase kinetics measured for H. pylori FliI in cached literature. Deep research (falcon)
  reports a thesis in which H. pylori FliI(E193Q) was monomeric by SEC; not a peer-reviewed source.

## Homolog (Salmonella) evidence used for inference
- ATPase activity, Mg2+-dependent, insensitive to F/V/P-type inhibitors; Walker mutants block
  assembly [PMID:8943245 "The activity was not affected by inhibitors of the F-, V- or P-type
  ATPases"].
- Crystal structure: F1 alpha/beta-like fold, hexamer model [PMID:17202259 "a similarity in the
  mechanism between FliI and F1-ATPase despite the apparently different functions of these
  proteins"].
- ATP-induced hexamerization [PMID:19665005 "ATP-binding induces FliI hexamerization"].
- FliJ is gamma-like and binds the centre of the FliI ring [PMID:21278755 "FliJ promotes the
  formation of FliI hexamer rings by binding to the center of the ring"].
- Energetics: export is PMF-driven, FliI dispensable (weak export without it) [PMID:18216858
  "The rest of the successive unfolding/translocation process of the substrates is driven by proton
  motive force."; PMID:18216859 "the flagellar secretion apparatus functions as a proton-driven
  protein exporter and that ATP hydrolysis is not essential for type III secretion"].
- The proton-conducting element is the membrane export gate (FlhA etc.), which is intrinsically a
  proton–protein antiporter; FliH-FliI brings FliJ to FlhA [PMID:21934659 "the export gate complex
  by itself is a proton-protein antiporter"].

## Conclusions on ATP-synthase-family GO terms
- GO:0046933 (TreeGrafter IEA, PTN002689426): QuickGO shows PTN002689426 used only for GO:0046933
  IEA TreeGrafter rows (165 rows, all epsilonproteobacterial FliI: Helicobacter, Campylobacter,
  Arcobacter, Sulfurospirillum etc.). i.e. the target is grafted into an epsilonproteobacterial
  FliI clade, and GO:0046933 has been inherited from a deeper node spanning the whole PTHR15184
  family. The function (ATP synthesis via rotary H+ transport through an Fo sector) arose in the
  F1-beta lineage; FliI has no Fo partner, hydrolyses ATP, and protons flow through FlhA.
  -> REMOVE.
- GO:0015986 (GO_REF:0000108 from GO:0046933) -> REMOVE (FliI consumes ATP; no synthesis).
- A "proton transmembrane transport" term would also be wrong for FliI itself (the gate conducts
  protons); not present in this GOA set.

## Positive terms
- Keep GO:0016887 ATP hydrolysis; GO:0005524 ATP binding (non-core); GO:0005737 cytoplasm;
  GO:0030254 T3SS secretion; GO:0030257 T3SS complex.
- NEW: GO:0008564 protein-exporting ATPase activity (definition covers Type III ATPases);
  GO:0044780 bacterial-type flagellum assembly (H. pylori mutants aflagellate; FliI does export
  work); GO:0120102 bacterial-type flagellum secretion apparatus (definition names FliI).
