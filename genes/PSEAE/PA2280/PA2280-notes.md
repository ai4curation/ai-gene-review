# PA2280 (Q9I1J5) notes — ArsH

## Identity

- PA2280 is the *arsH* gene of the PAO1 *ars* cluster; UniProt places it in the ArsH family (NCBIfam
  TIGR02690 resist_ArsH; InterPro IPR014063 Arsenate-R_ArsH; Pfam PF03358 FMN_red, an NADPH-dependent
  FMN-containing flavodoxin-like reductase fold). PANTHER PTHR43590 "ARSENIC RESISTANCE PROTEIN ARSH".

## Literature

- The PseudoCAP IDA cites PMID:22304305, which is about **Synechocystis sp. PCC 6803** ArsH, as its
  cached abstract states explicitly: [PMID:22304305 "Here we have expressed and purified Synechocystis
  ArsH and conducted an intensive biochemical study."] and [PMID:22304305 "We present kinetic evidence
  supporting a quinone reductase activity for ArsH, with a preference for quinones with hydrophobic
  substituents."] Nothing in the abstract or MeSH terms indicates that P. aeruginosa ArsH was assayed.
  QuickGO shows UniProt annotated the Synechocystis protein (P74312) with IDA/EXP from this paper, so the
  PseudoCAP row appears to be a transfer of a homolog's result recorded as IDA.
- P. aeruginosa ArsH itself was characterised by Crescente et al. 2016 (PMID:26621870): [PMID:26621870
  "we therefore characterized recombinant enzymes following expression of a group of putative
  azoreductase genes from P. aeruginosa expressed in Escherichia coli."] and [PMID:26621870 "The ArsH,
  MdaB and YieF family members all show azoreductase and NQO activities."] The abstract does not name
  the locus; the companion Crescente PhD thesis (Kingston University, eprints.kingston.ac.uk/33493 and
  related) states that pa2280 was cloned as paArsH, that PA2280 gave higher rates with FMN, and that
  NADPH was the preferred reductant; the thesis names pa2280 explicitly, so the mapping rests on it.
  Abstract only cached for PMID:26621870.
- In vivo role in arsenic resistance in P. aeruginosa: not tested in the papers cached here.

## Annotation decisions

- GO:0016655 (IDA PseudoCAP, PMID:22304305): MODIFY to GO:0003955 NAD(P)H dehydrogenase (quinone)
  activity. The activity is right for PA2280 (PMID:26621870) but the cited paper is about the
  Synechocystis protein; PSEUDOCAP WRONG_REFERENCE defect recorded.
- GO:0016655 (IBA PTN008682975): MODIFY to GO:0003955 for this gene (consistency); the node term is
  appropriate for its clade.
- GO:0016491 oxidoreductase activity (IEA InterPro): MODIFY to GO:0003955.
- GO:0052873 FMN reductase (NADPH) activity (IEA ARBA): UNDECIDED. FMN is the bound cofactor of ArsH;
  reduction of free FMN as a substrate has not been shown for PA2280 in the material I could read.

## PseudoCAP IBA-seed assessment

QuickGO (2026-10-28): PTN008682975 passes GO:0016655 (IBA) to 9 leaves: PA2280, *Gloeobacter* glr0005,
*Klebsormidium* KFL_001110020 and KFL_001820100, and fungal ArsH-like proteins (*A. fumigatus*
AFUA_8G07150, AFUA_1G16120, AFUA_5G15030; *A. nidulans* ANIA_10571; *Sclerotinia* SS1G_02209). The
worklist says 10 leaves in 7 taxa.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN008682975 | GO:0016655 oxidoreductase activity, acting on NAD(P)H, quinone or similar compound as acceptor | 1 (sole) | 10 (7 taxa); 9 in QuickGO | GO:0016655, IDA, PMID:22304305 (PseudoCAP) | WRONG | The cited paper characterises Synechocystis ArsH, not PA2280 (stated in the abstract), so as recorded the seed is a homolog transfer labelled IDA. The term itself is true for PA2280 by PMID:26621870 (recombinant P. aeruginosa ArsH has NQO activity), and quinone reductase activity is shared by characterised ArsH proteins, so the IBD's content is sound for the clade; the seed should be re-cited to PMID:26621870. |
