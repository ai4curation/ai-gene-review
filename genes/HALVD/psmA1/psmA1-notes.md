# psmA1 (HVO_1091, Q9V2V6) — Haloferax volcanii DS2 — review notes

Automated deep research was unavailable for this gene; these notes were compiled
manually from PubMed (NCBI E-utilities searches for "Haloferax volcanii proteasome"),
the cached publications in `publications/`, and the UniProt record
(`psmA1-uniprot.txt`). No `-deep-research-*.md` file was generated.

## Identity

- Proteasome subunit alpha 1 (alpha1, PsmA1), 252 aa, peptidase T1A family
  (non-catalytic alpha-type subunit). InterPro IPR019982 (Proteasome alpha subunit,
  archaeal family), IPR000426 (Proteasome alpha-subunit N-terminal domain), IPR023332
  (Proteasome alpha-type). [file:HALVD/psmA1/psmA1-uniprot.txt "Belongs to the peptidase T1A family"]
- H. volcanii encodes two alpha-type subunits (alpha1 = psmA, alpha2 = psmC) and one
  beta (psmB), plus two PAN AAA+ ATPases (panA, panB).

## Structure and assembly (the core of what alpha1 does)

- First purification: alpha1 + beta form a 600-kDa four-ring barrel
  [PMID:10482525 "A 20S proteasome, composed of alpha(1) and beta subunits arranged in a barrel-shaped structure of four stacked rings, was purified from a halophilic archaeon Haloferax volcanii."].
- Catalysis lies in beta: [PMID:10482525 "a 49-residue propeptide is removed to expose a highly conserved N-terminal threonine which is proposed to serve as the catalytic nucleophile"] — this is the beta subunit; alpha1 has no N-terminal Thr nucleophile (UniProt has no active-site feature on alpha1).
- Activity of the alpha1-beta particle: chymotrypsin-like peptide hydrolysis, insulin
  B-chain hydrolysis, salt-dependent [PMID:10482525 "The alpha(1)beta-proteasome also hydrolyzed insulin B-chain protein."].
- Two CP subtypes in vivo: alpha1-beta (symmetric) and alpha1-alpha2-beta (asymmetric,
  homo-oligomeric alpha rings at opposite ends)
  [PMID:12486053 "The alpha1 and beta proteins alone form active 20S proteasomes"];
  [PMID:12486053 "the alpha1-beta proteasome was a symmetrical cylinder with alpha1 rings on each end"].
- Cross-linking/MS modelling: [PMID:22623373 "The α-type subunits form the outer rings and the β-type subunits form the two inner rings which harbor the proteolytic active sites"].
- The alpha1 N terminus forms the CP "gate"; deleting it raises CP peptidase activity
  [PMID:19376868 "unregulated opening of the CP \"gate\" impairs the ability of cells to overcome salt stress"].

## Post-translational modifications of alpha1 (PTMs OF the subunit, not functions of it)

- N-terminal acetylation [PMID:16950923 "alpha1 and alpha2 contained N-terminal acetyl groups"];
  Met1-acetylated form dominant [PMID:19376868 "Quantitative mass spectrometry revealed this was the dominant N-terminal form of alpha1 in H. volcanii cells."].
- Phosphorylation at Ser/Thr, growth-phase dependent; Rio1p kinase homolog (HVO_0135)
  phosphorylates alpha1 in vitro [PMID:20671954 "provide evidence that Rio1p Ser/Thr kinase phosphorylates α1"].
- SAMPylation: the task brief notes alpha1 is SAMPylated. I could not verify that
  alpha1 is itself a SAMP conjugate from the cached text of PMID:20054389 (Table 1, the
  conjugate list, is not in the cached text). Not used in the review.
- None of these PTM papers are cited in GOA for alpha1, and none would justify a GO
  annotation of alpha1's own function (they are annotations about alpha1 as a substrate).

## Physiology / genetics

- Knockouts [PMID:18931121 "Our results demonstrate that 20S proteasomes are required for growth."];
  [PMID:18931121 "conditional depletion of either beta alone or alpha1 and alpha2 together rendered the cells inviable"];
  psmA deletion sensitizes to hypo-osmotic stress, organic N, L-canavanine, heat. Pleiotropic
  phenotypes — not used for NEW process terms.
- In vivo proteasome-dependent proteolysis of short-lived GFP reporters [PMID:15574956 "This inhibitor was highly specific for H. volcanii 20S proteasomes"].
- SAMP link (indirect): [PMID:20054389 "The enhanced levels of SAMP1-conjugates in the ΔpanA ΔpsmA mutant suggest SAMP1 targets proteins for destruction by proteasomes."]
  Suggestive only; whether SAMP conjugation actually targets substrates to the PAN-20S
  proteasome (a "modification-dependent protein catabolic process") remains
  unestablished. H. volcanii has no ubiquitin.

## GO term checks (QuickGO, 2026-10-15)

- GO:0019773 proteasome core complex, alpha-subunit complex: "The proteasome core
  subcomplex that constitutes the two outer rings of the proteasome core complex." No
  taxon constraint; the Mus musculus mention is only an example. Applies to archaea.
- GO:0006511 ubiquitin-dependent protein catabolic process: defined as initiated by
  covalent attachment of ubiquitin. Not applicable (no ubiquitin in H. volcanii).
  QuickGO: 910 archaeal GO:0006511 rows, 888 of them via InterPro:IPR000426 (alpha
  N-terminal domain) InterPro2GO mapping.
- GO:0004298 threonine-type endopeptidase activity: 786 archaeal rows via IPR019982,
  an alpha-subunit-specific entry; alpha subunits have no catalytic Thr1. These
  "enables" catalytic-activity rows are a systematic InterPro2GO error for alpha subunits.
- GO:0140756 structural constituent of proteasome — what alpha1 enables (used for the
  human PSMA1 review in this repo as well).

## Calibration verdict

- 6 IDA rows from 2 papers (1999, 2003), both from the Maupin-Furlow lab and both
  biochemical characterizations of purified CPs. Coverage of the complex and the process
  is right; the MF is assigned with "enables" to a catalytic activity that belongs to
  beta. Nothing captures the structural role, gate function or the 2008 genetics.
- IEA layer adds two eukaryote/catalysis-biased errors (ubiquitin-dependent, threonine-type
  endopeptidase).
