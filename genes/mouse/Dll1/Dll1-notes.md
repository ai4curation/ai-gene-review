# Dll1 (mouse) review notes

UniProt Q61483 (DLL1_MOUSE), Delta-like protein 1, 722 aa, type I transmembrane DSL ligand.
PANTHER PTHR24049 (CRUMBS FAMILY MEMBER) per UniProt DR line. MGI:104659.
Notch-module role: **canonical activating Delta-class (DSL) Notch ligand** (signal-sending cell).

## Molecular function
- Binds Notch1/Notch2 in trans and activates cleavage and RBP-J-dependent transcription
  [PMID:10958687 "All of the three DSL proteins bound to endogenous Notch2 on the surface of BaF3 cells"]
  [PMID:10958687 "binding of DSL proteins to Notch2 also activated the transcription of reporter genes driven by the RBP-Jkappa-responsive promoter."]
- Fringe increases Delta1 binding and Notch1 activation [PMID:15574878 "expression of mammalian fringe proteins (Lunatic [LFng], Manic [MFng], or Radical [RFng] Fringe) increased Delta1 binding and activation of Notch1 signaling"]
- Ubiquitinated by E3 ligases Mib1 and Neurl1/Neurl1b; ubiquitination needed for recycling and Notch-binding
  competence and to drive Notch1 transendocytosis
  [PMID:16000382 "Mib1 interacts with and regulates all of the Notch ligands, jagged 1 and jagged 2, as well as Dll1, Dll3 and Dll4."]
  [PMID:17003037 "Neuralized-2 (Neur2), which is a ubiquitin-protein isopeptide ligase (E3) that interacts with and ubiquitinates Delta."]
  [PMID:18676613 "ubiquitination, although not required for endocytosis, is essential for Dll1 recycling and that recycling is required to acquire affinity for the receptor."]
  [PMID:21985982 "lysine 613 (K613) in the cytoplasmic tail of Dll1 is a key residue necessary for transcellular activation of Notch signaling."]
- Itself a substrate of regulated intramembrane proteolysis (ADAM10 shedding then gamma-secretase); ICD partly nuclear
  [PMID:12794186 "Kuzbanian/ADAM10 is involved in this processing event, but other proteases can probably substitute for it."]
- C-terminal PDZ-binding motif binds MAGI1/MAGI2 (Acvrinp1) PDZ domains; MAGI1 recruits Dll1 to adherens junctions
  [PMID:14529612 "We delimited the fourth PDZ domain of Acvrinp1 and the PDZ-binding domain of Dll1 as major interacting domains."]
  [PMID:15908431 "Dll1 was recruited to these AJs through binding to MAGI1."]
- MT1-MMP (MMP14) cleaves Dll1 on stromal cells to dampen Notch signalling [PMID:21572390].

## Localisation
- Plasma membrane; Mib1-dependent endocytosis to cytoplasmic vesicles
  [PMID:16000382 "in the Mib1-/- mutants, Dll1 accumulated in the plasma membrane, while it was localized in the cytoplasm near the nucleus in the wild types"]
- Adherens junctions/apical endfeet in neural tube [PMID:24715457 "Both Notch1 and its ligand Dll1 are distributed around AJs in the apical endfeet"]
- Lipid rafts [PMID:21985982].

## Biological processes
- Lateral inhibition in neurogenesis, inner ear hair cells, intestinal secretory cells
  [PMID:16495313 "In the absence of Dll1, auditory hair cells develop early and in excess, in agreement with the lateral inhibition hypothesis."]
  [PMID:18997111 "different levels of Dll1 expression determine the fate of NPCs through cell-cell interactions, most likely through the Notch-Delta lateral inhibitory signaling pathway"]
- Somitogenesis (segmentation clock, somite polarity), left-right asymmetry via Nodal
  [PMID:12730124 "Dll1-mediated Notch signaling is essential for generation of left-right asymmetry"]
- Arterial identity (DLL1 activates Notch1 in fetal arteries) [PMID:19144989 "DLL1 is an essential Notch ligand in the vascular endothelium of large arteries to activate Notch1 and maintain arterial identity."]
- Marginal zone B cells, adult neural stem cell quiescence, satellite cells, epidermis: pleiotropic.

## Pathway-variant relevance
- Canonical activating Delta with MNNL/C2, DSL (InterPro IPR001774) and eight EGF repeats. Falcon deep
  research reports a DOS motif in the EGF1-2 region of Dll1 (absent from Dll4), citing Hirano et al. 2020
  [file:mouse/Dll1/Dll1-deep-research-falcon.md "Dll1 also contains a Delta-and-OSM-11-like (DOS) motif within the EGF1–2 region, which is present in Dll1 but absent from Dll4"];
  primary source not independently checked here. Requires Mib1 (and Neurl) ubiquitination to signal. Dll4 paralog partially redundant but
  functionally divergent [PMID:26114479]. Dll3 is the divergent non-activating paralog.

## Deep research
Falcon deep research completed (Dll1-deep-research-falcon.md; the wrapper reported a 600 s timeout but the
orphaned falcon client finished and wrote the file). Also notes cis-inhibition by Dll1
[file:mouse/Dll1/Dll1-deep-research-falcon.md "Dll1 also mediates cis-inhibition when present in the same cell as Notch"].
