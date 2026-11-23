# rme-2 (C. elegans; UniProt O44191; WormBase WBGene00004374; T11F8.3) - manual literature synthesis

No deep-research API was available for this session; this synthesis was compiled by hand from the
cached publications in `publications/` and the UniProt record.

## Identity and domain architecture

- 925-aa type I transmembrane protein of the LDL receptor (LDLR) superfamily. UniProt: "Belongs to
  the LDLR family"; signal peptide 1-24 (SignalP), single TM helix 787-811 (Phobius); Pfam
  Ldl_recept_a x4 (PF00057), Ldl_recept_b x1 (PF00058), cEGF; PANTHER PTHR22722:SF14.
- Grant & Hirsh 1999 [PMID:10588660 "C-terminal to the predicted signal sequence are five tandem class A
  ligand-binding repeats, each containing six cysteine residues with characteristic spacing and typical
  anionic SDE or DDE sequences"]; they describe RME-2 as "the first LR5 member" of the family, and
  [PMID:10588660 "These findings are consistent with a typical type I transmembrane protein topology, with a
  large N-terminal extracellular domain and a short (110 aa) intracellular domain."]

## Function: the C. elegans yolk (vitellogenin) receptor

- Identified in a forward screen for oocytes refractory to YP170::GFP (vitellogenin-GFP) uptake
  [PMID:10588660 "We show that RME-2 is the C. elegans yolk receptor."].
- Mutant phenotype: [PMID:10588660 "rme-2 mutants are characterized by slightly small oocytes devoid of yolk,
  otherwise normal germ line morphology, high-level pseudocoelomic yolk accumulation, reduced embryo
  production, and low embryo viability."]
- Sufficiency (gain of function in heterologous cells): [PMID:10588660 "Thus, expression of RME-2 in these
  cells is sufficient to direct the specific binding of yolk particles."]
- Basis of the claim: [PMID:10588660 "We propose that RME-2 is the C. elegans yolk receptor based on its mutant
  phenotype, expression pattern, molecular nature, and sufficiency to induce yolk binding in a heterologous
  cell type."]
- Endocytosis is clathrin- and RAB-5-dependent: [PMID:10588660 "Ce-chc (RNAi) and Ce-rab5 (RNAi) induced
  accumulation of ligand (YP170::GFP) and receptor (RME-2) together at or near the oocyte surface."]
- Ligand: vitellogenins (YP170, YP115, YP88), which are lipoprotein-like yolk particles; there is no
  evidence that RME-2 binds LDL itself. The GO term "low-density lipoprotein particle receptor activity"
  used by WormBase is therefore a lateral mis-fit; GO:0008196 "vitellogenin receptor activity" exists
  and matches the biology.

## Localization and trafficking

- Expression restricted to the proximal germline (oocytes) and early embryos:
  [PMID:10588660 "We found abundant RME-2 in the proximal germ line of adult hermaphrodites and within all cells
  of early embryos. We failed to detect RME-2 in any other cells"].
- Oocyte plasma membrane and cortical puncta; intracellular vesicles: [PMID:10588660 "In later-stage oocytes
  anti-RME-2 antibodies stain many prominent puncta at or near the plasma membrane in addition to the
  intracellular puncta"].
- Recycling between PM and endosomes (immuno-EM): [PMID:15895077 "Since RME-2 constantly cycles between the PM
  and endosomes, most RME-2 in wild-type oocytes at steady-state is found in cortical endocytic membrane
  structures"].
- PM localization used as a reporter in other studies: [PMID:19798448 "RME-2, the yolk receptor, is correctly
  localized and enriched at the plasma membrane."]; [PMID:22768351 "RME-2::GFP was not trafficked to the plasma
  membrane in RME-2::GFP; vha-19(RNAi) adults"].
- After fertilization RME-2 is internalized and degraded: [PMID:23840591 "In wild-type one-cell embryos, RME-2
  is no longer required and therefore quickly endocytosed and subsequently degraded in the lysosome"];
  [PMID:10588660 "All cells of early embryos display prominent anti-RME-2 immunostaining in abundant
  intracellular vesicular structures but lack any apparent RME-2 in the plasma membrane"].

## Developmental phenotypes (downstream consequences)

- Reduced brood, low embryo viability and ovulation defects (spermathecal dilation failures) in rme-2
  mutants [PMID:10588660 "Damaged oocytes and embryos are found in the uterus of rme-2 mutant hermaphrodites,
  consistent with a defect in ovulation."]. These are consequences of yolk-less oocytes rather than a
  direct role of the receptor in ovulation or embryogenesis.

## Papers in the GOA set with abstract only

- PMID:15456850 (cpl-1 / cathepsin L) and PMID:17234175 (PUF-5/6/7): only abstracts cached; neither
  abstract mentions RME-2, so the RME-2 localization data the WormBase curators used (likely figure
  panels using RME-2 as a marker) could not be verified here.
