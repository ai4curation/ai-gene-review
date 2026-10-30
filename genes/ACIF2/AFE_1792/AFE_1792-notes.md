# AFE_1792 (B7JBP8, SQRD_ACIF2): curation notes

## Identity and SQR type

- Swiss-Prot entry for the Acidithiobacillus ferrooxidans ATCC 23270 sulfide:quinone
  oxidoreductase. Recombinant enzyme crystallized and characterized by Cherney et al.
  [PMID:20303979 "Sulfide:quinone oxidoreductase from the acidophilic and chemolithotrophic
  bacterium Acidithiobacillus ferrooxidans was expressed in Escherichia coli and
  crystallized"].
- **Type I (SqrA).** [PMID:23103448 "The greatest amount of information is available for the
  Type I SQRs (SqrA), which includes those from A. aeolicus and A. ferrooxidans, for which
  structures are known."] Our pairwise analysis agrees: 41.9% identity to the Aquifex Type I
  SQR (O67931), with the cysteine triad (C128, C160, C356) conserved
  (`AFE_1792-bioinformatics/RESULTS.md`).
- Mechanism: [PMID:22542586 "The electrons from sulfides are transferred first to the enzyme
  cofactor, FAD, which, in turn, passes them onto the quinone pool in the membrane."]
  [PMID:20303979 "Cys356 disulfide acts as a nucleophile that attacks the C4A atom of the FAD
  cofactor in electron transfer reaction."]
- Membrane: [PMID:20303979 "a flexible C-terminal domain encompassing two amphipathic helices
  that are thought to provide for membrane anchoring"].

## Paralogs in A. ferrooxidans

- The genome paper names a *different* locus as the sqr implicated in sulfide oxidation
  [PMID:19077236 "a sulfide/quinone oxidoreductase encoded by sqr (AFE0267) suggested to be
  involved in the oxidation of sulfide to sulfur"]. AFE_0267 (B7J411, 375 aa) is only 27.5%
  identical to AFE_1792 and has no residue aligned to Cys160 (RESULTS.md).
- So the in vitro evidence (structure, kinetics, mutagenesis) is for AFE_1792. Physiological
  and genetic evidence for SQR involvement in A. ferrooxidans sulfur oxidation has been
  attached to AFE_0267 or to SQR activity of unspecified origin purified from membranes
  [PMID:21687411 "The enzymatic activity of Sqr (EC 1.8.5.-) has been purified from A.
  ferrooxidans membranes (Wakai et al., 2007)."]. No knockout of AFE_1792 exists.

## PANTHER oddity

- B7JBP8 is in PTHR42913:SF6 (inside an AIF/NDH-2-like family, InterPro IPR051169). Its 87-94%
  identical orthologs in A. caldus (F9ZQD6) and A. ferrivorans (A0A060UVE9) are in
  PTHR43755:SF1 (InterPro IPR052541 SQRD). This inconsistency is the source of the
  TreeGrafter rows "NAD(P)H dehydrogenase (quinone) activity" and "aerobic electron transport
  chain" on this entry only.

## Annotation decisions (summary)

- GO:0070224 (EXP x2, IEA): ACCEPT, core.
- GO:0016020 (IEA, NAS): MODIFY to GO:0005886 plasma membrane (amphipathic anchoring helices
  plus the quinone-pool acceptor).
- GO:0016491: TOO_GENERAL.
- GO:0003955 (TreeGrafter): MARK_AS_OVER_ANNOTATED (family NADH-donor function; enzyme is
  sulfide-dependent; NAD(P)H never shown).
- GO:0019646 (TreeGrafter): KEEP_AS_NON_CORE.
- NEW GO:0071949 FAD binding (crystal structures).

## CMMMech claim check

CMMMech records (orpiment, realgar, zinc, titanium-metal, electroplating-sludge, arsenopyrite,
stannite, anglesite, nickel-flotation-tailings, tetrahedrite-concentrate, ...) use B7JBP8 as
the representative A. ferrooxidans Sqr, with functional_role "Membrane-bound sulfide-quinone
reductase (EC 1.8.5.4; AFE_1792) catalyzing oxidation of sulfide to elemental sulfur/polysulfide
coupled to quinone reduction during acidophilic sulfur/sulfide bioleaching".

- The catalytic part is well supported, though only in vitro (recombinant enzyme).
- "during acidophilic sulfur/sulfide bioleaching" goes beyond the evidence. No study shows
  AFE_1792 expression or function during mineral leaching, and the genome paper ties
  physiological sulfide oxidation to the paralog AFE_0267. The evidence supports the enzyme's
  capability, not its contribution to leaching. The CMMMech `supports: partial` wording is
  appropriate. A stronger claim would need AFE_1792-specific expression or mutant data.
- The record description "Inner-membrane flavoprotein" is consistent with our plasma-membrane
  call. The protein is monotopic/peripheral, not an integral inner-membrane protein.
