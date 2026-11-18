# PTO1356 (UniProt Q6KZB1) - Picrophilus torridus DSM 9790

## 2026-11-18 review notes

### Naming and taxon

- UniProt OS: Picrophilus torridus (strain ATCC 700027 / DSM 9790 / JCM 10055 / NBRC 100828 /
  KAW 2/3), NCBI_TaxID 1122961. NCBI Taxonomy now labels taxid 1122961 "Picrophilus oshimae
  DSM 9789" (the stub label follows NCBI). The literature uses P. torridus throughout. No
  standard gene symbol exists; the folder uses the ordered locus name PTO1356 (GenBank
  AAT43941).

### Literature search

No deep-research provider was available. PubMed (NCBI E-utilities) queries:

- `Picrophilus AND (mevalonate OR isobutene)` via Europe PMC (34 hits, before the service began
  returning 503) and PubMed `Thermoplasma[tiab] AND mevalonate[tiab]` (11 hits).
- `"mevalonate 3-kinase"[tiab] OR "mevalonate-3-kinase"[tiab]` (6 hits).
- `PTO1356 OR Ta0893 OR SSO2989 OR HVO_1412` (no hit for PTO1356).

Only one paper assays PTO1356 itself: PMID:25636853 (Rossoni et al. 2015, full text cached).
Patents on isobutene production also use it (cited in that paper, not retrieved).

### Reaction

- Mevalonate 3-kinase (EC 2.7.1.185, RHEA:42884): (R)-mevalonate + ATP =
  (R)-3-phosphomevalonate + ADP + H+.
  [PMID:25636853 "We discovered that it is not a decarboxylase per se but an ATP-dependent
  enzyme, mevalonate-3-kinase (M3K), which catalyzes the phosphorylation of MVA to
  mevalonate-3-phosphate."]
- Position of phosphorylation: C3 (tertiary hydroxyl), by 13C-31P coupling.
  [PMID:25636853 "13C NMR spectrum of the product mixture after phosphorylation of MVA by pure
  putPtMVD showed splitting at carbons 2 to 4 and 6, consistent with phosphorylation at
  position 3"]
- No decarboxylation: [PMID:25636853 "Even after a long incubation time (96 h), isoprenol was
  not observed, suggesting that putPtMVD does not catalyze MVA decarboxylation per se."]
- Substrate range: inactive on MVAPP and MVA-5P; active on MVA (3.01 U/mg).
  [PMID:25636853 "There was no activity when MVAPP was tested as the substrate."]
  [PMID:25636853 "However, there was no detectable activity on MVA-5P."]
- Kinetics (UniProt, ECO:0000269 PubMed:25636853): Km MVA 131 uM; Km ATP 23 uM; kcat 1.9 s-1
  (MVA). 3-hydroxyisovalerate: Km 2348 uM, kcat 0.1 s-1; 3-hydroxybutyrate: Km 3163 uM, kcat
  0.1 s-1.
- Side activity: isobutene from 3-HIV via spontaneous decarboxylation of the 3-phospho product.
  [PMID:25636853 "The enzyme's potential in isobutene formation is due to the conversion of 3-HIV
  to an unstable 3-phosphate intermediate that undergoes consequent spontaneous decarboxylation
  to form isobutene."] Roughly 200-fold lower kcat/Km than with mevalonate; judged a promiscuous
  activity of biotechnological rather than physiological interest. No GO row exists for it and
  none was added.

### Pathway context

- T. acidophilum ortholog Ta1305 (Q9HIN1) is the founding M3K [PMID:24914732 "The product of
  Ta1305 activity, however, showed splitting at carbons 2–4 and 6, which is consistent with
  phosphorylation at the 3-OH position (Figure 3C)."]. PTO1356 is 38% identical to TaM3K and
  only 18-21% to classical MVDs (PMID:25636853).
- Thermoplasma-type pathway: M3K -> M3P5K (Ta0762) -> MBD (Ta0893; P. torridus PTO0478) -> IPK.
  [PMID:28004831 "mevalonate 3-kinase (Ta1305) has equally strong homologs (39–67% ID) in all 8
  thermoplasmatales yet has no detectable homologs in any other organism, suggesting that this
  pathway is unique to thermoplasmatales."] The P. torridus MBD is UniProt Q6L1T9 (PTO0478), not
  PTO1356; its crystal structure is PDB 7T71 (PMID:35690147).
- In P. torridus the pathway is inferred, not shown in vivo [PMID:25636853 "P. torridus is also
  likely to contain this new type of MVA pathway (Fig. 7)."].

### Family placement

- PANTHER PTHR10977:SF3 ("DIPHOSPHOMEVALONATE DECARBOXYLASE") by HMM, but InterPro places it in
  the M3K family (IPR048471 M3K, IPR048470 M3K_C; NCBIfam NF040848 mev_kinase) and NOT in
  IPR005935 (Mev_decarb). It therefore receives no carboxy-lyase InterPro2GO row.
- Not a leaf of the PANTHER 19 tree and no tree leaf shares its UniRef50 cluster
  (`../../HALVD/mvaD/mvaD-bioinformatics/RESULTS.md`); no IBA from PTHR10977 reaches it.
- T. acidophilum Ta1305 (Q9HIN1) has no PANTHER assignment at all in UniProt, while PTO1356 is in
  PTHR10977:SF3: the two M3K orthologs are classified inconsistently.
- Any family-level decarboxylase term (GO:0004163, GO:0016831) would be wrong for this protein.

### Annotation decisions

| Term | Evidence | Action | Note |
|---|---|---|---|
| GO:0019287 IPP biosynthesis, mevalonate pathway | IEA (UniPathway) | ACCEPT | core BP |
| GO:0016773 phosphotransferase activity, alcohol group as acceptor | IDA PMID:25636853 | NEW | most specific existing MF; matches Ta1305 convention |
| NTR mevalonate 3-kinase activity | - | proposed_new_terms | EC 2.7.1.185 / RHEA:42884, no GO term |
