# SLC48A1 (HRG1) notes

No deep-research provider was available for this gene; these notes are a manual
literature review (Europe PMC search, PMIDs verified and cached with
`ai-gene-review fetch-pmid`).

## Identity

- Human SLC48A1 / HRG1, UniProt Q6P1K1, 146 aa, four predicted TM helices
  (FT TRANSMEM 12-32, 40-60, 74-94, 110-130), C-terminal di-leucine motif 142-143.
  HRG family (InterPro IPR026218, Pfam PF16954, PANTHER PTHR31525:SF1, TCDB 2.A.110.1.1).
- Mouse ortholog Q9D8M3 (Slc48a1); C. elegans hrg-1 Q21642 (paralog hrg-4 at the
  plasma membrane).

## Function: heme transporter of endolysosomal / phagolysosomal membranes

- Discovery in C. elegans (heme auxotroph); human and worm HRG-1 "bind and transport
  haem" [PMID:18418376 "Human and worm proteins localize together, and bind and transport haem, thus establishing an evolutionarily conserved function for HRG-1."] (abstract only cached).
  Per White et al. citing it, worm and human HRG1 co-localize with LAMP1, Rab7 and Rab11
  in HEK293 cells [PMID:23395172 "worm and human HRG1 proteins co-localize with LAMP1 and the small GTPases Rab7 and Rab11 in HEK293 cells"].
- Conserved transport residues: a TMD2 histidine is required for transport by human
  HRG-1 in a yeast hem1-deletion heme-uptake assay [PMID:22174408 "mutation of the synonymous histidine in TMD2 of hHRG-1 eliminates heme transport activity"].
- Macrophages / erythrophagocytosis (EP): Hrg1 recruited to phagolysosomal membranes
  during EP, not during latex bead phagocytosis [PMID:23395172 "Hrg1 was recruited to the phagolysosomal membranes specifically during phagocytosis of RBCs but not latex beads"];
  knockdown attenuates Hmox1/Fpn1 induction [PMID:23395172 "Hrg1 knockdown resulted in a significant attenuation of Hmox1 and Fpn1 mRNA induction during EP"].
  Human missense variant P36L abolishes transport in yeast [PMID:23395172 "The P36L variant was unable to rescue the growth of hem1Δ, even in the presence of 10 µM heme"].
- Knockout mice: Slc48a1-/- RES macrophages accumulate heme as hemozoin in enlarged
  LAMP1+ lysosomes [PMID:31571584 "These animals are heme tolerant because they sequester heme within enlarged lysosomes in the RES macrophages and form crystalline hemozoin"];
  [PMID:34713217 "SLC48A1-deficient mice are unable to transport heme from RES phagolysosomes into the cytoplasm."].
- Zebrafish: Hrg1a/Hrg1b double KO impairs kidney macrophage heme-iron recycling
  [PMID:30248094 "we show that zebrafish Hrg1a and its paralog Hrg1b are functional heme transporters"].
- Oligodendrocytes: highest Slc48a1 expression in mature OLs; Hrg1 null mice show
  myelin defects; OLs import heme/ZnMP [PMID:39501820 (abstract) "OL Hrg1 encodes a functional heme transporter required for myelin integrity"].

## Disputed / secondary: V-ATPase association (O'Connor lab)

- O'Callaghan et al. 2010 [PMID:19875448 "HRG-1 interacts with the c subunit of the V-ATPase and enhances V-ATPase activity in isolated yeast vacuoles."]
  found HRG-1 in endosomes but not lysosomes and at the plasma membrane after nutrient
  withdrawal [PMID:19875448 "HA-HRG-1 does not colocalize with LAMP-1, which implies no significant expression in lysosomes."].
  They also report the C-terminus to be extracellular/luminal, which conflicts with the
  Hamza lab topology (cytoplasmic C-terminus used as antibody epitope in PMID:23395172).
- Fogarty et al. 2014 [PMID:24141772] (abstract only): plasma membrane HRG-1 with V-ATPase in
  invasive cancer cells.
- Treated as non-core; no GO annotation currently derived from these papers. Not proposed
  as NEW (V-ATPase regulator role not independently replicated).

## Annotation decisions (summary)

- heme transmembrane transporter activity: ACCEPT (core).
- heme transport (all 4 rows): MODIFY to heme transmembrane transport GO:0035351 and,
  where supported, heme export from vacuole to cytoplasm GO:0140357 (lysosome lumen ->
  cytosol, matches topology and knockout phenotype).
- heme binding: KEEP_AS_NON_CORE (substrate binding, IDA in PMID:18418376).
- lysosomal membrane / endosome membrane: ACCEPT; lysosome (root organelle) ACCEPT.
- plasma membrane: KEEP_AS_NON_CORE (minor pool; worm HRG-4 is the plasma membrane paralog).
- phagocytic vesicle membrane: MODIFY -> phagolysosome membrane GO:0061474.
- protein binding x7 (HuRI/Y2H): REMOVE (uninformative).
