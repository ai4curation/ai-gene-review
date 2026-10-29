# arcD (PA5170, P18275) notes

## Identity

- UniProt P18275 (ARCD_PSEAE), 482 aa, Swiss-Prot reviewed. Arginine:ornithine
  antiporter of the APC superfamily, basic amino acid/polyamine antiporter (APA)
  family, TC 2.A.3.2.3 (InterPro IPR022461 Arg/Orn_antiprt_ArcD, NCBIfam TIGR03810,
  PANTHER PTHR42770:SF4). Thirteen hydrophobic segments; inner membrane.
- First gene of the anaerobically induced arcDABC operon (arcA PA5171 ADI, arcB
  catabolic OTC, arcC carbamate kinase).

## Biology (literature)

- Discovery: arcD ORF upstream of arcABC encodes a hydrophobic membrane protein;
  arcD mutants cannot use external arginine as an energy source; antiport was
  *proposed* from the coupling of arginine uptake and ornithine release
  [PMID:2158926 "Mutations in arcD rendered the cells unable to utilize extracellular arginine as an energy source."];
  [PMID:2158926 "it is proposed that arcD specifies an arginine: ornithine antiporter or a part thereof"].
- Direct transport assays: E. coli membrane vesicles carrying arcD and
  proteoliposomes with reconstituted ArcD
  [PMID:1311296 "These proteoliposomes mediate a stoichiometric exchange between arginine and ornithine."];
  exchange is much faster than PMF-driven uptake
  [PMID:1311296 "The exchange was several orders of magnitude faster than proton motive force-driven transport."];
  lysine can also exchange [PMID:1311296 "Accumulated ornithine was readily exchangeable for external arginine or lysine."].
- Localization and topology: Caa-tagged ArcD in the P. aeruginosa inner membrane;
  N terminus cytoplasmic, C terminus periplasmic
  [PMID:8449902 "permitted the localization, by immunoblotting, of the hybrid protein in the inner membrane of P. aeruginosa"].
- Relevant comparator: Chlamydophila pneumoniae AaxC, a member of the same clade,
  exchanges arginine for agmatine and is not inhibited by ornithine
  [PMID:18790867 "The chlamydial AaxC transporter was resistant to cadaverine, L-lysine and L-ornithine, which inhibit the E. coli AdiC antiporter."].

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN008675589 | GO:0022857 transmembrane transporter activity | 7 | 70 (24 taxa) | GO:0043858 arginine:ornithine antiporter activity, IMP, PMID:1311296 (PseudoCAP); also UniProt EXP PMID:2158926, PMID:8449902 | SOUND | The PseudoCAP paper directly measures arginine/ornithine exchange by ArcD (vesicles, proteoliposomes). The generic term is right for an APC-superfamily node that also holds E. coli AdiC, CadB, PotE, PuuP and YjeH seeds. The IMP code is probably IDA (the abstract describes direct assays, not a mutant; full text not read), which does not affect the IBD. |
| PTN000208945 | GO:0043858 arginine:ornithine antiporter activity | 1 (sole seed) | 16 (11 taxa) | GO:0043858 arginine:ornithine antiporter activity, IMP, PMID:1311296 (PseudoCAP); also UniProt EXP PMID:8449902 and PMID:2158926 | SOUND | The seed is well supported for ArcD itself by two direct studies (PMID:1311296 reconstitution; PMID:8449902 exchange activity in P. aeruginosa). Of the two UniProt EXP rows, PMID:2158926 only proposes the antiport from a mutant phenotype, so it is the weakest support, but the IBD does not depend on it. The node term mostly suits the clade (ArcD-type exchangers from ADI-pathway organisms: Clostridium, Bacillus, Staphylococcus, Vibrio, Bradyrhizobium). One leaf is doubtful: C. trachomatis AaxC (O84379), whose C. pneumoniae ortholog is an arginine:agmatine exchanger insensitive to ornithine (PMID:18790867). That IBA is probably an over-propagation, and a NOT (or GO:0043862 arginine:agmatine antiporter activity) should be considered for the chlamydial subclade. |

## Decisions summary

- ACCEPT: arginine:ornithine antiporter activity (IBA, IEA, EXP x2, IMP), plasma
  membrane (IBA, IEA, EXP x2), L-arginine transmembrane transport (IEA, EXP).
- MODIFY: amino acid transport and transmembrane transport to L-arginine and
  L-ornithine transmembrane transport; membrane to plasma membrane; generic MF
  rows (transmembrane transporter, antiporter, amino acid and carboxylic acid
  transmembrane transporter activity) to arginine:ornithine antiporter activity.
- KEEP_AS_NON_CORE: L-arginine catabolic process (IEA, IMP) and generation of
  precursor metabolites and energy (IMP): ArcD supplies substrate and removes
  product of the ADI pathway but performs no catabolic step.
- NEW: L-ornithine transmembrane transport (IDA, PMID:1311296).
- Source defects: PSEUDOCAP WRONG_EVIDENCE_CODE CHECK (PROBABLE; IMP should probably be IDA);
  UNIPROT WRONG_REFERENCE CHECK (SUSPECTED) on the EXP MF row citing PMID:2158926,
  which proposes but does not measure antiport; GO_CENTRAL CHECK (SUSPECTED) for
  C. trachomatis AaxC under PTN000208945.
