# ftrC (sll0554, Q55389) — Synechocystis sp. PCC 6803

## Provenance and process

- 2026-10-19: `just fetch-gene SYNY3 ftrC --uniprot-id Q55389` (32 GOA rows).
- Deep research: `just deep-research SYNY3 ftrC --provider falcon` failed (the Edison falcon
  service is currently returning auth errors); not retried. No deep-research file exists. The
  review is grounded in the UniProt record, GOA, and primary literature cached in `publications/`.
- Additional papers found by PubMed search and cached: PMID:18003670 (FTR and NTR disruptants in
  Synechocystis), PMID:33599267 and PMID:35453339 (cyanobacterial Fdx-dependent Trx reductases;
  full text).
- Most FTR primary papers are abstract-only in the cache (PMID:10649999, 14769790, 17134703,
  17611542, 19908864, 19825613); PMID:19132843 has full text.

## Identity

- Catalytic chain (FTR-C, also called FTR-B) of ferredoxin:thioredoxin reductase, EC 1.8.7.2;
  118 aa. Partner: variable chain FtrV (Q55781). [file:SYNY3/ftrC/ftrC-uniprot.txt "Catalytic subunit of the ferredoxin-thioredoxin reductase"]
- UniProt numbering includes the initiator Met, so the literature residues Cys57, His86 and Cys87
  are UniProt Cys58, His87 and Cys88 (active-site nucleophile Cys58; Cys58-Cys88 redox-active
  disulfide; [4Fe-4S] ligands Cys56, Cys75, Cys77, Cys86).

## Molecular function

- FTR catalyses two-electron reduction of the thioredoxin disulfide using electrons from reduced
  plant-type [2Fe-2S] ferredoxin, via a [4Fe-4S] cluster next to a redox-active disulfide.
  [PMID:14769790 "It catalyzes the two-electron reduction of the disulfide of thioredoxins with electrons from ferredoxin involving a 4Fe-4S cluster and an adjacent active-site disulfide."]
- Mutating either active-site cysteine of Synechocystis FTR gives inactive enzyme; His86 (UniProt
  His87) strongly reduces activity. [PMID:14769790 "Mutation of either of the active-site cysteines yields inactive enzymes"]
- Crystal structure of the Synechocystis heterodimer: thin flat molecule; Trx docks on one side
  (mixed disulfide), Fdx on the other. [PMID:10649999 "The thin, flat FTR molecule makes the two-electron reduction possible by forming on one side a mixed disulfide with thioredoxin and by providing on the opposite side access to ferredoxin for delivering electrons."]
- Structures of the one- and two-electron intermediates and of Fdx-FTR, FTR-Trx and the ternary
  Fdx-FTR-Trx complexes. [PMID:17611542 "We determined the structures of FTR in both its one- and its two-electron-reduced intermediate states and of four complexes in the pathway, including the ternary Fdx-FTR-Trx complex."]
- His86 is needed for the valence-localized [Fe4S4]2+ intermediate. [PMID:19132843 "His86 is required for formation of the partially valence-localized [Fe4S4]2+ cluster that is the hallmark of two-electron-reduced intermediate."]
- NMR: FTR binds Fdx and Trx-m at distinct sites, forming a noncovalent ternary complex.
  [PMID:19908864 "FTR uses distinct sites to bind Fd and Trx simultaneously to form a noncovalent ternary complex."]

## Heterodimer, enables vs contributes_to

- FTR is a heterodimer; the redox chemistry (cluster and active-site disulfide) is on FTRC, and Fdx
  and Trx contact only FTRC. FTRV may protect the cluster.
  [PMID:35453339 "FTR is a heterodimeric enzyme composed of an approximately 13 kDa catalytic subunit (FTRC), which contains a 4Fe-4S cluster and a redox-active site, and a variable subunit (FTRV) with a molecular mass ranging from 7 to 13 kDa, which may protect the 4Fe-4S cluster of FTRC from oxidative inactivation [16,17,18]."]
  [PMID:35453339 "Crystallographic structures showed that ferredoxin (Fd) and Trxs interact exclusively with the catalytic subunit of FTR [19,20,21]."]
- Decision: `enables` GO:0103012 is appropriate for the catalytic chain, which carries every
  catalytic element. `contributes_to` would fit FtrV (Q55781), which currently has no MF
  annotation in GOA besides protein binding.

## GO term notes

- GO:0103012 is placed under GO:0016673 (sulfur group of donors, iron-sulfur protein as acceptor),
  following the EC direction. The InterPro2GO term GO:0016730 (iron-sulfur proteins as donors)
  describes the physiological direction but is not an ancestor of GO:0103012.
- GO:0009055 electron transfer activity is meant for carriers; the electron flow through FTR is
  its catalytic reaction, so GO:0103012 is the better term for those IDA rows.
- GO:0030386 ferredoxin-thioredoxin reductase complex exists but has zero annotations in QuickGO
  and carries `part_of chloroplast` in GO, so annotating a cyanobacterial subunit to it would
  imply a chloroplast location. Not proposed; raised as a question.

## Biological role

- In plants and cyanobacteria FTR links light (via PSI-reduced Fdx) to thiol redox regulation of
  target enzymes. [PMID:17611542 "Oxygen-evolving photosynthetic organisms regulate carbon metabolism through a light-dependent redox signalling pathway."]
- Synechocystis disruptant analysis: NTR-Trx important for antioxidant defence, FTR-Trx more
  important for growth-rate control. [PMID:18003670 "we found that the NTR-Trx pathway is important for the antioxidant system, whereas the FTR-Trx pathway may play a more important role in the control of cell growth rate."]
- ftrC and ftrV expression falls in the dark and is down-regulated by DCMU and DBMIB.
  [PMID:19825613 "whereas trxA, trxB, and the ftr genes are down-regulated."]
- FTR is not present in all cyanobacteria; some (Gloeobacter, Prochlorococcus) use a flavin FFTR
  instead. [PMID:33599267 "Remarkably, though FTR was long considered a hallmark of light regulation in oxygenic photosynthesis, this enzyme is not present in all cyanobacteria"]

## Annotation decisions (summary)

- GO:0103012 (5 IDA + IEA): ACCEPT.
- GO:0051539 4Fe-4S binding (6 IDA): ACCEPT.
- GO:0009055 electron transfer activity (3 IDA): MODIFY -> GO:0103012.
- GO:0016730 (IEA InterPro): MODIFY -> GO:0103012.
- GO:0015979 photosynthesis (IBA, IEP): KEEP_AS_NON_CORE.
- GO:0005515 (14 IPI): MODIFY. FtrV partner -> GO:0046982 protein heterodimerization activity;
  Fdx (P27320) and spinach Trx-m/Trx-f (P07591, P09856) partners are the enzyme's substrates
  -> GO:0103012.

## PGAP

- WP_010873706.1 is named "ferredoxin:thioredoxin reductase" but has no naming evidence, so PGAP
  assigns no GO and no EC. NF014939 (domain HMM, GO:0016730) matches but is not the naming model.
  This is a recall gap: well-established EC 1.8.7.2 / GO:0103012 is absent.
