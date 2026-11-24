# EYR15_14300 (A0A4V2JDD3, Hans-LanM) notes

## Identity

- UniProtKB A0A4V2JDD3 (TrEMBL, unreviewed), ORF EYR15_14300, Hansschlegelia quercus
  strain Dub (NCBITaxon:2528245), 133 aa, predicted signal peptide 1-23 (SignalP).
  UniProt records only `FT SIGNAL 1..23 {ECO:0000256|SAM:SignalP}` and `KW Signal`,
  and the paper's Methods say only that signal peptides were predicted with SignalP
  v6.0 and removed; neither names a translocon class, so no Sec assignment is made
  here (an earlier draft said "Sec signal peptide" and that was unsupported).
  Named "EF-hand domain-containing protein" automatically from PROSITE PS50222.
- Folder is named by accession (no gene symbol), with the ORF as gene_symbol, following
  the genes/9BACT/I9U7L5 precedent. No other genes/9HYPH folder existed.
- This is the protein called Hans-LanM in the only primary paper. The UniProt RN line for
  PDB 8DQ2 and 8FNR cites that paper [PMID:37259003 "Here we characterize a new LanM, from
  Hansschlegelia quercus (Hans-LanM)"].
- No deep-research provider was available; notes below are from the full text of
  PMID:37259003 (PMC10232371) and the local sequence analysis. A web search found no
  later primary study of this protein.

## Relation to Mex-LanM (C5B164, genes/METEA/lanM)

- About 33% identity [PMID:37259003 "Hans-LanM features low (33%) sequence identity with
  Mex-LanM"]; the local global alignment gives 33.8% over full length
  (file:9HYPH/A0A4V2JDD3/A0A4V2JDD3-bioinformatics/RESULTS.md).
- LanM hallmarks [PMID:37259003 "Third, at least one EF hand contains proline at the second
  position (in Mex-LanM, all four EF hands feature P2 residues)."]. In Hans-LanM only EF2
  (loop NPDGDTTLESGE, Pro59) has Pro2; EF1 and EF3 have Lys2 and EF4 Ala2. Loops are spaced
  12-13 residues apart, as in Mex-LanM.

## Biochemistry (all on recombinant mature protein, residues 24-133, E. coli)

- Stoichiometry [PMID:37259003 "The protein binds about three equivalents of LaIII and NdIII,
  and slightly less DyIII, by inductively coupled plasma mass spectrometry"].
- Affinity [PMID:37259003 "the Kd,app values are similar, 68 and 91 pM, respectively"]
  (La, Nd); Dy main response at 2.6 nM; Ca(II) [PMID:37259003 "Hans-LanM responds to
  calcium(II) weakly (Kd,app = 60 µM)"].
- Structure: EF1-EF3 hold La(III); EF4 does not [PMID:37259003 "EF4 is structurally
  distinct, does not exhibit anomalous difference density consistent with LaIII and was
  modelled with NaI"].
- Dimerization [PMID:37259003 "Thus, LaIII favours Hans-LanM’s dimerization by >100-fold
  over DyIII."]; interface Arg100 contacts EF3 ligands Asp85 and Glu91 of the partner. Residue
  numbers match the displayed UniProt sequence (checked: D85, E91, D93, R100).
- R100K is monomeric [PMID:37259003 "SEC–MALS analysis indicated MWs of 10–13 kDa for apo,
  LaIII– and DyIII–Hans-LanM(R100K)"].
- Application: immobilized R100K separates Nd/Dy [PMID:37259003 "The immobilized R100K
  variant performed even better, achieving baseline separation of DyIII and NdIII to >98%
  purity and >99% yield in a single stage"].

## Physiology: not studied

No experiment addresses expression, localization or function in H. quercus. Periplasmic
localization is a reasonable expectation (signal peptide, analogy with Mex-LanM), but there is
only one independent line for this protein, so no location term was added. The paper itself
treats residues 1-23 as a signal peptide and omits them from the construct
[PMID:37259003 "codon optimized for expression in E. coli without its native 23-residue signal
peptide"], but its Methods also say signal peptides of LanM sequences were predicted with
SignalP (v6.0) and then removed, i.e. this is the same SignalP call that UniProt records as
FT SIGNAL 1..23. It corroborates the mature-chain boundary; it is not an independent second
line of evidence for export or a periplasmic location. No biological
process term was added: lanthanide uptake or homeostasis roles are inferred for Mex-LanM, not
tested for Hans-LanM.

## Curation decisions

- GO:0005509 calcium ion binding (IEA, InterPro EF-hand): KEEP_AS_NON_CORE. True in vitro
  (60 µM), but the sites are lanthanide sites.
- NEW GO:0046872 metal ion binding (IDA, PMID:37259003): most specific existing GO term for
  lanthanide binding (OLS has no lanthanide ion binding term); lanthanide ion binding proposed,
  matching the Mex-LanM review.
- NEW GO:0042803 protein homodimerization activity (IDA, PMID:37259003): metal-dependent
  dimer shown by SEC, MALS, ITC, SAXS and crystal structure.
- No source defects: the UniProt name is generic but not wrong, and the IEA row is literally
  true.

## CMMMech record check (CultureBotAI/CMMMech repository, `data/records/rare-earth-element-commodities.yaml`)

Paths in this section are relative to the root of the separate CMMMech repository
(CultureBotAI/CMMMech), not to this repository. The grounding to A0A4V2JDD3 is correct (same organism, ORF, PDB entries and paper). Points
where the record says more than the evidence:

- The causal-graph node describes Hans-LanM as having "redox/dimer-sensitive LREE/HREE
  discrimination". The paper reports metal-ion-radius-dependent dimerization; nothing in it
  concerns redox, so "redox" is unsupported.
- "Dimeric EF-hand lanmodulin": the protein is in a monomer/dimer equilibrium that is tight
  only with light lanthanides (apo and Dy forms have Kdimer of about 60-117 µM). And the R100K
  variant used on the column is monomeric, so the separation does not rely on a dimer. The
  authors suggest functional dimers are unlikely on the column at that immobilization density.
- The separation (>98% purity) is an in vitro, engineered, synthetic-feed result with a
  C-terminal Cys variant on agarose. It is not a property of the organism and should not be
  read as industrial performance.
