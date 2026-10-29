# Slik (Drosophila melanogaster) - manual literature review

No deep-research API provider was available in this session. This file is a manual
literature synthesis compiled from cached publications (`publications/PMID_*.md`) and
PubMed searches ("Slik kinase Drosophila", 17 hits). Quotes are verbatim from the
cached text.

## Identity

- UniProt A4UZU8 (TrEMBL, unreviewed, PE 1), 1365 aa; FlyBase FBgn0035001; CG4527;
  GeneID 37893. Synonyms Plkk1/dPlkk.
- Ste20 (GCK-V subfamily, SLK/LOK/STK10-like) Ser/Thr kinase: N-terminal protein kinase
  domain (FT DOMAIN 37..295, PROSITE PS50011; ATP-binding Lys66, proton acceptor 158),
  long disordered middle region, and a C-terminal coiled-coil domain (CCD; SAM:Coils
  1159..1186, 1244..1326) containing the PKK (Pfam PF12474) repeats.
- Orthologs: human SLK and STK10 (LOK). Human STK10 rescues fly slik depletion
  [PMID:37794497 "STK10, the human ortholog of Slik, into Drosophila restores slik"].

## Molecular function: Ser/Thr kinase for ERM-family proteins (Moesin) and Talin

- Moesin T559 is the principal substrate. Genetic: loss of Slik abolishes phospho-Moesin
  in discs [PMID:15371338 "Epithelial integrity fails in slik mutant imaginal discs."]
  and in mitotic S2 cells [PMID:18283112 "Collectively, our data show that Slik-dependent
  phosphorylation of moesin at T559 directs moesin activation and function during mitosis."].
- Biochemical: immunoprecipitated Slik phosphorylates the Moesin C-terminal
  actin-binding domain in vitro and autophosphorylates [PMID:26170449 "wild-type Slik
  phosphorylated a truncated form of Moesin consisting of the C-terminal actin-binding
  domain"; "Slik is capable of phosphorylating itself in in vitro kinase assays"].
  Endogenous Slik IP kinase assays on Moesin C-ERMAD [PMID:32960945 "Next, we
  immunoprecipitated endogenous Slik and measured its kinase activity in vitro on its
  natural substrate, the C-terminal part of moesin"].
- Activation-segment threonines (T186/T192/T196 in the numbering of PMID:26170449) are
  needed for full activity [PMID:26170449 "Slik is auto- and trans-phosphorylated in vivo."].
- Talin T152 is a further substrate at muscle attachment sites [PMID:31511253 "We also
  identify Slik as the kinase phosphorylating Talin"].
- Merlin: Slik promotes Merlin phosphorylation/inactivation in vivo, but direct
  phosphorylation was not shown [PMID:17060498 "It remains unclear whether Slik itself can
  directly phosphorylate either protein or whether there are one or more kinases operating
  downstream of Slik."]. Slik binds GST-Merlin and GST-Moesin in pull-downs.
- All documented phosphoacceptors are threonines; no serine substrate is reported.

## Non-catalytic function

- The CCD mediates apical/cortical localization and a kinase-independent growth-promoting
  activity [PMID:26170449 "necessary and sufficient for apical localization of the kinase
  in epithelial cells"]. Early work placed this growth/survival signalling upstream of Raf
  [PMID:14624240].
- The CCD directly tubulates membranes (GUV assays) and promotes cytoneme formation, which
  is opposed by its kinase activity via Moesin [PMID:40050674 "In these cells without Slik,
  its CCD cannot tubulate the plasma membrane into nascent cytonemes, leading to fewer
  cytonemes per cell."].

## Localization

- Mitotic S2 cells: cortex, paralleling p-Moesin, which is uniform in prometaphase/metaphase
  and later concentrated at the equator / cleavage furrow [PMID:18283112 "Importantly, using
  antibodies to detect the Slik kinase, we found that distribution of the Slik protein
  paralleled p-moesin localization throughout division in wild-type cells"].
- Epithelia: apical cortex [PMID:26170449]; tracheal terminal cells: luminal (apical)
  membrane [PMID:25061859]; muscle attachment sites [PMID:31511253].
- Cortical association is promoted by STRIPAK PP2A-dependent dephosphorylation; Slik
  co-immunoprecipitates with Cka and Strip [PMID:32960945 "Here, we show that Slik is a new
  STRIPAK-associated kinase."].
- No text in PMID:18283112 describes Slik at the mitotic spindle midzone.

## Biological roles

- Mitotic cortical stability: Slik depletion phenocopies Moesin loss (cortical blebbing,
  increased mitotic cell volume, off-centred and unstable spindles, longer metaphase)
  [PMID:18283112 "Finally, Slik inactivation induced moesin-like instability of the F-actin
  cortex during mitosis"; "Therefore, these data show that Slik-mediated activation of
  moesin at the mitotic cortex is required for proper organization of the mitotic
  spindle."]. Spindle and timing defects are downstream of cortical defects
  [PMID:18283112 "It is possible that these spindle defects contribute to extend the
  metaphase stage"].
- Epithelial integrity in imaginal discs via Moesin activation and Rho1 antagonism
  [PMID:15371338].
- Tissue growth and cell survival; suppression of JNK-dependent apoptosis [PMID:14624240;
  PMID:37794497].
- Tracheal terminal cell branching [PMID:25061859], neuroblast apical p-Moesin
  [PMID:29282284], synapse maturation (human SLK NDD rescue model) [PMID:40347834].
