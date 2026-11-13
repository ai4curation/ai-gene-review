# metF (P0AEZ1, b3941) notes

## Deep research status

`just deep-research ECOLI folD --provider perplexity` failed in this session
("Provider 'perplexity' not available. Available: falcon, openscientist,
claude_code"; no provider API key configured), so deep research was not
attempted again for metF. These notes are my own reading of the UniProt record
and cached publications.

## Literature reviewed

- Sheppard, Trimmer & Matthews 1999 (abstract only; PMC93435 returned HTTP 403).
  Purified MetF (native and His-tagged) is a homotetramer of 33 kDa subunits,
  each with one noncovalent FAD; catalyses NADH-dependent reduction of
  CH2-H4folate to CH3-H4folate; NADPH works with much higher Km
  [PMID:9922232 "The native protein comprises four identical 33-kDa subunits,
  each of which contains a molecule of noncovalently bound flavin adenine
  dinucleotide (FAD)."] [PMID:9922232 "NADPH also serves as a reductant, but
  exhibits a much higher Km."].
- Trimmer et al. 2001 (abstract only). Asp120 and Glu28 roles; Glu28Gln is
  inactive in the physiological NADH-CH2-H4folate oxidoreductase reaction
  [PMID:11371182].
- Lee et al. 2009 (full text). Phe223 mutants; ping-pong bi-bi mechanism; E. coli
  enzyme is a catalytic-domain-only homotetramer, prefers NADH, lacks the AdoMet
  regulatory domain of eukaryotic MTHFRs; each monomer a beta8alpha8 barrel
  [PMID:19610625 "E. coli and plant MTHFRs prefer NADH, whereas the mammalian and
  yeast enzymes prefer NADPH."] [PMID:19610625 "The reaction provides
  CH3-H4folate, which is the sole methyl donor to homocysteine in the production
  of methionine by methionine synthase."].
- Kerner et al. 2005 (abstract only). Proteome-wide GroEL substrate
  identification; TIM barrels enriched [PMID:16051146]. The EcoCyc IPI to GroEL
  (P0A6F5) reflects MetF being a GroEL folding client.

## Synthesis

MetF is the committed step providing the methyl group for de novo methionine
synthesis (MetE/MetH use CH3-H4folate). The physiological reaction is
irreversible in vivo (PhysiologicalDirection right-to-left in RHEA:19821, i.e.
CH2-THF -> CH3-THF). Specific term GO:0106312 (NADH) is a child of GO:0004489
[NAD(P)H] (checked in OLS 2026-11-13), so the NAD(P)H rows are refined to
GO:0106312. Cytosolic, soluble.
