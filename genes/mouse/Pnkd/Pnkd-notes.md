# Pnkd (mouse, Q69ZP3) review notes

## Deep research

`just deep-research-falcon mouse Pnkd --fallback perplexity-lite` was run on 2026-10-20 and
failed: falcon failed to authenticate ("Exception: Failed to authenticate") and the
perplexity-lite fallback returned HTTP 401 (insufficient quota). No deep-research file exists.
The review is based on the cached primary literature (PMID:21487022, PMID:25730884,
PMID:22214848 abstract only, PMID:18614015), the UniProt record and the GOA rows.

## Evolutionary placement

- UniProt: PANTHER PTHR11935:SF116 "HYDROLASE PNKD-RELATED"; metallo-beta-lactamase
  superfamily, glyoxalase II family; InterPro IPR017782 (Hydroxyacylglutathione hydrolase) and
  Pfam HAGH_C. The PNKD subfamily is distinct from the HAGH (glyoxalase II) subfamily.
- Zinc ligands (by similarity to human HAGH Q16775) H172, H174, D176, H177, H229, D253, H291.
  I checked the sequence: residues 166-180 read VAILCTHKHWDHSGG, so the THxHxDH motif is
  intact. The protein is therefore plausibly catalytically competent.
- PAINT: IBA thiolester hydrolase activity (GO:0016790) from PTN004322580 and IBA mitochondrion
  from PTN000940186. PAINT did NOT propagate hydroxyacylglutathione hydrolase activity
  (GO:0004416) to the PNKD clade, although HAGH carries it. I treat that omission as deliberate:
  the PNKD subfamily is not inferred to be a glyoxalase II.
- Isoform 2 (MR-1S-like short isoform) lacks residues 143-385, i.e. the whole
  metallo-beta-lactamase domain, so it cannot carry the enzymatic activity.

## Experimental evidence: what is established in mouse vs inferred from human

Mouse (experimental):
- Pnkd is neuronal and widely expressed in brain; one isoform is membrane-associated
  [PMID:22214848 "One PNKD isoform is a membrane-associated protein."] (abstract only).
- Pnkd mutant knock-in/transgenic mice show reduced striatal extracellular dopamine and
  enhanced dopamine release on caffeine/ethanol [PMID:22214848]. These are organismal/circuit
  phenotypes; the IMP rows (regulation of dopaminergic transmission, dopamine metabolism,
  posture) are acts_upstream_of_or_within and are not evidence of direct participation.
- Pnkd-L co-immunoprecipitates RIM1 and RIM2 from mouse frontal cortex; Pnkd localises to
  presynaptic terminals by immunogold EM, absent in Pnkd-/-; RIM1/2 levels reduced in Pnkd-/-
  cortex; Pnkd-/- has weaker synaptic strength and increased paired-pulse facilitation
  [PMID:25730884 "We then used a nonspecific anti-RIM antibody and confirmed that both RIM1 and
  RIM2 were pulled down by Pnkd from wild-type but not Pnkd −/− mouse frontal cortex
  homogenates"].
- Overexpressed (human) PNKD suppresses synaptic vesicle exocytosis in cultured hippocampal
  neurons [PMID:25730884 "Overexpressed PNKD protein suppresses release, and mutant PNKD protein
  is less effective than wild-type at inhibiting exocytosis."]. Note the tension with the KO,
  which also weakens synaptic strength; the authors attribute the KO effect to RIM
  destabilisation.
- Pnkd KO and mutant transgenic cortex have ~20% lower glutathione [PMID:21487022 "Figure 6B
  shows that KO and mut-Tg mice have significantly lower glutathione levels (∼20% lower) in the
  frontal cortex compared with WT littermates"].
- MitoCarta mass-spec (mouse tissues) detects Pnkd in mitochondria; per PMID:21487022 the
  peptides support the short isoform [PMID:21487022 "there was strong support for the short
  isoform to be localized to mitochondria"].

Human (experimental, transferable via 1:1 orthology in the same PANTHER subfamily):
- Purified human PNKD-L hydrolyses S-D-lactoylglutathione at an "extremely low but consistent"
  rate, judged not physiological; human PNKD-L fails to rescue Drosophila hagh-null SLG
  hydrolysis [PMID:21487022]. Authors propose an unknown alpha-hydroxythioester substrate.
- Human PNKD-L localises to the cell membrane and late endosomes in SH-SY5Y and Cos7 and does not
  colocalise with mitochondrial markers [PMID:21487022]; another study (Ghezzi 2009, not cached)
  reported mitochondrial localisation of the L and S isoforms and ER/Golgi/PM for the M isoform.
- N-terminal cleavage of PNKD-L (~15-30 aa) is blocked by disease mutations [PMID:21487022].

## Decisions

- GO:0016790 thiolester hydrolase activity (IBA): ACCEPT, core; inferred (not assayed in mouse).
- GO:0004416 HAGH activity (IEA InterPro2GO): MARK_AS_OVER_ANNOTATED; in vitro trace activity
  only on human PNKD-L, not physiological, PAINT declined to propagate it.
- GO:0051596 methylglyoxal catabolic process (IEA): REMOVE; human PNKD-L does not rescue SLG
  metabolism in vivo.
- Protein binding IPI (RIM1/RIM2): REMOVE per GO:0005515 policy; no specific MF term for RIM
  binding; interaction itself is real.
- Mitochondrion: ACCEPT (MitoCarta HDA, IBA, human EXP); likely isoform-dependent.
- Plasma membrane / membrane: ACCEPT/MODIFY to plasma membrane.
- Presynaptic cytosol IDA: ACCEPT (mouse immunogold).
- Cytoplasm: KEEP_AS_NON_CORE (short isoform cytoplasmic; general term).
- ER, Golgi (ISO from human PNKD-M overexpression): KEEP_AS_NON_CORE.
- Complex IV assembly ISO: UNDECIDED. The human source annotation is no longer present in
  current QuickGO for Q8N490 (checked 2026-10-20), and no cached publication supports it.
- Negative regulation of neurotransmitter secretion: KEEP_AS_NON_CORE (overexpression-based; IGI
  with RIM; regulatory role mechanism unclear).
- Dopaminergic transmission, dopamine metabolism, posture IMP: KEEP_AS_NON_CORE for the
  synaptic transmission term; MARK_AS_OVER_ANNOTATED for dopamine metabolic regulation and
  posture (organismal phenotypes of a knock-in mutant).
