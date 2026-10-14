# CMU1 (UMAG_05731, A0A0D1DWQ2) research notes

## Sources
- UniProt A0A0D1DWQ2 (Swiss-Prot, experimentally annotated).
- PMID:21976020 (Djamei et al. 2011, Nature) - abstract only in cache.
- PMID:30651637 (Han et al. 2019, Nature) - abstract only in cache.
- PMID:34414650 (Bauters et al. 2021, MPP review) - full text cached; used to verify
  the SA/phenylpropanoid phenotypes from Djamei 2011 that are not in the abstract.
- CMU1-deep-research-falcon.md (Falcon deep research; relies on later reviews for the
  2011 quantitative data).

## Findings
- Secreted chorismate mutase (EC 5.4.99.5; signal peptide 1-21; AroQ eukaryotic CM fold).
  Abstract: [PMID:21976020 "Here we show that the chorismate mutase Cmu1 secreted by U. maydis is a virulence factor."]
- Uptake into plant cells and spread: [PMID:21976020 "The enzyme is taken up by plant cells, can spread to neighbouring cells and changes the metabolic status of these cells through metabolic priming."]
- Host cytosol + interaction with plant CMs, SA phenotype: [PMID:34414650 "Cmu1 is secreted by U. maydis to the plant cytosol and nucleus, interacts with plant CMs, and is needed for full virulence of the pathogen."]; [PMID:34414650 "Infecting plants with a Cmu1 deletion mutant of U. maydis resulted in a 10‐fold increase of SA compared to infection with the wild type (Djamei et al., 2011)."]
- Mechanistic model (proposed, not flux-traced): [PMID:34414650 "It was proposed that Cmu1 acts in conjunction with a cytosolic plant CM, thereby extracting more chorismate from the plastids, leading to lower substrate availability for plastidic SA biosynthesis."]
- Kiwellin ZmKWL1 inhibits Cmu1: [PMID:30651637 "Here we show that one of the 20 maize-encoded kiwellins (ZmKWL1) specifically blocks the catalytic activity of Cmu1."]
- UniProt: not allosterically regulated by Trp/Tyr (unlike housekeeping CMs); homodimer;
  heterodimer with ZmCM2; ELR loop 117-140 required for KWL1 binding; R183A/K194A kill activity.

## Curation reasoning
- Chorismate mutase activity: the enzyme's own catalysis, purified-protein assays (2011, 2019
  kinetics KM 0.8 mM). Core MF. All three rows accepted.
- GO:0140502 effector-mediated suppression of host SA-mediated innate immune signaling:
  symbiont-side term; Cmu1 performs the catalytic step that drains chorismate, so it does work
  in the process (participation test passes - this is not a substrate case). Strictly the effect
  is on host SA biosynthesis rather than SA signalling; no symbiont-side "suppression of host SA
  biosynthesis" term exists (QuickGO search), so accept and raise as question.
- Aromatic amino acid biosynthetic process (InterPro2GO IEA): the secreted paralogue is not the
  fungal housekeeping Phe/Tyr pathway enzyme; its prephenate feeds the host phenylpropanoid flux.
  Marked over-annotated.
- Chorismate metabolic process (IEA): literally true (it converts chorismate) - kept non-core.
- Locations: extracellular region, host cell cytosol, host apoplast all consistent with
  secretion into the biotrophic interface and translocation; accepted.
- Comparators: PYRO7/PWL2 and PYRO7/slp1 reviews use symbiont-side effector terms
  (GO:0052034 / GO:0140423), consistent with keeping CMU1 on GO:0140502 rather than any
  plant-side defense term.
- No NEW annotations: CM2 heterodimerization and KWL1 binding would only be "protein binding";
  KWL1 inhibition is a host-side function.
