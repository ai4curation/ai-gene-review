# PIKM1-TS (Pikm-1; UniProt B5UBC1) — research notes

## Identity
- Tsuyuake allele of the sensor NLR of the rice Pik blast-resistance locus (chr 11). 1,143 aa CC-HMA-NB-ARC-LRR protein; HMA (RATX1) domain at residues ~186-264 sits between the CC and NB-ARC (UniProt FT REGION 191..264; PDB 6FU9/6FUB/6FUD are Pikm-HMA/AVR-Pik complexes).
- Paired with the helper/executor NLR Pikm-2 (Pikm2-TS), encoded adjacent.
- Deep research file present: `PIKM1-TS-deep-research-falcon.md` (Falcon). Used as background; claims verified against cached papers where possible.

## Genetics
- Both genes are required; neither alone confers resistance [PMID:18940787 "genetic complementation analysis of transgenic lines individually carrying these two genes negated the possibility that either Pikm1-TS or Pikm2-TS alone was Pikm"; "Pikm-specific resistance is conferred by cooperation of Pikm1-TS and Pikm2-TS"]. Abstract only in cache.

## Effector binding (core MF)
- AVR-Pik physically binds Pik N-terminal region (Y2H, in planta co-IP); binding specificity matches recognition specificity [PMID:22805093 "This binding specificity correlates with the recognition specificity between AVR and R genes"]. Abstract only. (The abstract says "N-terminal coiled-coil domain"; later work maps binding to the integrated HMA domain.)
- Pikm-HMA binds AVR-PikD, E and A with high affinity; Pikm rice resists strains carrying any of the three [PMID:29988155 "Unlike Pikp, the integrated heavy metal-associated (HMA) domain of Pikm binds with high affinity to each of the three recognized effector variants"]. Abstract only.
- SPR: AVR-PikD binds Pikm-1 HMA with KD ~10 nM; no strong binding to AVR-PikC/F [PMID:37486356 "we observed strong binding of AVR-PikD to the Pikm-1 HMA (equilibrium dissociation constant [KD] = ∼10 nM)"].
- Pikm-1 HMA also binds AVR-Mgk1; AVR-Mgk1-expressing M. oryzae triggers resistance in Tsuyuake (Pikm) rice [PMID:36656825 "The integrated HMA domain of Pikm-1 bound AVR-Mgk1 and AVR-PikD, whereas the HMA domain of Piks-1 bound only AVR-Mgk1"; "Furthermore, Sasa2 transformants expressing AVR-Mgk1 triggered resistance in the rice cultivar Tsuyuake (Pikm)."]. Two HMA residues (Q229, V261) distinguishing Pikm from Piks are needed for full AVR-PikD binding.
- UniProt FUNCTION text uses boilerplate "via an indirect interaction" — contradicted by the direct binding data above. Noted, not a GO issue.

## Metal binding
- Pik-1 HMA domains lack the MxCxxC cysteines; Pikp-HMA structure has no metal [PMID:26304198 "these Cys residues are not conserved in Pik-1 HMA domains, including Pikp-1"]. Pikm-1 sequence (from UniProt record) at the β1-α1 loop reads ...KIPMVDDKS..., i.e. no cysteine at all in the motif region; the HMA (186-264) contains no Cys. So the InterPro2GO metal ion binding mapping is unsupported.

## Nucleotide binding / P-loop
- Pikm-1 NB-ARC P-loop GGGKTT intact (residues ~296-301). For the allele Pikp-1, a P-loop mutant chimera still gives reduced effector-independent cell death [PMID:37199729 "suggests that an intact P-loop in Pikp-1 is not essential for Pik-mediated signaling"], while Pik-2 P-loop and MHD are essential. ADP binding plausible but non-core for the sensor.

## Sensor/helper relationship
- Allelic mismatch Pikp-1/Pikm-2 gives autoimmunity; Pikm-1/Pikp-2 reduced response [PMID:36656825 "An allelic mismatch of a receptor pair leads to autoimmunity (Pikp-1/Pikm-2) or reduced response (Pikm-1/Pikp-2) due to allelic specialization [119]."]. Pikm-1 is used as an engineering chassis (HMA swaps with OsHIPP43, RGA5 HMA, nanobodies), typically with Pikp-2 to avoid autoactivity [PMID:37486356; PMID:38968126]. These engineered specificities are not native functions.
- Cell death execution attributed to Pik-2 (P-loop/MHD of Pikp-2 required) [PMID:37199729 "This autoactivity requires an intact P-loop and MHD motif in Pikp-2"]. So hypersensitive response/cell death execution is mainly a helper property — consistent with RGA5/RGA4 treatment.

## Localization
- Not established in rice; only a preliminary N. benthamiana thesis (per deep research). No location annotation proposed.

## Curation decisions (summary)
- defense response (IEA): ACCEPT (same as RGA5).
- ADP binding (IEA): KEEP_AS_NON_CORE (same as RGA5).
- metal ion binding (IEA): REMOVE (degenerate HMA, no Cys; same as RGA5).
- response to other organism (ARBA): MODIFY -> defense response to fungus (GO:0050832).
- NEW: innate immune receptor activity (GO:0140376) and innate immune response-activating signaling pathway (GO:0002758), mirroring RGA5 experimental annotations. Participation test: Pikm-1 is the receptor that binds the ligand, i.e. does the first step of the signaling pathway. Comparator: RGA5 (IDA/EXP) carries both.
- Not proposed: plant-type hypersensitive response (executed by Pikm-2; would make sensor/helper annotations identical), molecular function inhibitor activity (no Pikm-specific data that Pikm-1 represses Pikm-2, unlike RGA5/RGA4; the Pik pair seems to be cooperative rather than negatively regulated).
