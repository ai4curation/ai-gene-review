# liuD (PA2014, Q9I299) review notes

## Review session 2026-11-13 (PseudoCAP tier 3, shared-claim group liuB/liuD)

Fetched with `just fetch-gene PSEAE liuD`. No deep-research provider file was generated.

Alpha subunit of MCC, and the domain content matches the mechanism the structure paper describes
exactly: [file:PSEAE/liuD/liuD-uniprot.txt "InterPro; IPR011764; Biotin_carboxylation_dom."],
[file:PSEAE/liuD/liuD-uniprot.txt "InterPro; IPR000089; Biotin_lipoyl."] (the BCCP carrier) and
[file:PSEAE/liuD/liuD-uniprot.txt "InterPro; IPR048429; MCC_alpha_BT."] -- the BT domain the paper
names as mediating the BC-CT contact. Compare
[PMID:22158123 "The α subunit contains the biotin carboxylase (BC) and biotin carboxyl carrier
protein (BCCP) domains"].

So LiuD has a real molecular function of its own, GO:0004075 biotin carboxylase activity, which is
accepted as the most informative row on the entry; the holoenzyme term is scoped with
contributes_to for the same reconstitution reason recorded in the liuB notes.

### Annotation decisions

- ACCEPT: GO:0004075 (the subunit's own activity), GO:0004485 (IDA and IMP, each with a
  WRONG_QUALIFIER PseudoCAP defect at CONFIRMED), GO:0005524, GO:0006552, GO:0046247, GO:1905202.
- TOO_GENERAL, all three verified in QuickGO on 2026-11-13: GO:0000166 (GO:0005524 is_a it),
  GO:0016879 (GO:0004075 is_a it), GO:0008300 (GO:0046247 is_a it).
- KEEP_AS_NON_CORE: GO:0046872 metal ion binding. The reaction is MgATP-dependent so a divalent
  metal is needed, but no metal site is curated on this entry, so refining would assert more than
  is known.
- REMOVE: GO:0005515 protein binding, as on liuB.
- A question is raised about whether LiuD and AtuF cross-pair with the opposite beta subunit, since
  the substrate-specificity paper could not cleanly separate the MCCase and GCCase activities
  in vivo.

## Leucine catabolism module review (merged from a concurrent curation branch)


- Reviewed as an experimentally characterized bacterial exemplar of the distal L-leucine catabolism module
  (`modules/leucine_catabolism.yaml`); the P. aeruginosa liuRABCDE cluster (PA2011-PA2016) carries the
  direct enzymology and genetics that the P. putida KT2440 orthologs lack.
- Deep research: no provider deep-research file was generated for this gene in this session. The review
  rests on the cached PubMed records cited in the review (PMID:16517656, PMID:16820476, PMID:16272386,
  PMID:18469096, PMID:18625020, PMID:19459965, PMID:19597963, PMID:22158123), all abstract-only except
  PMID:22158123, and on the UniProt record.
- Acyclic terpene terms: the Atu pathway joins the Liu pathway at methylcrotonyl-CoA
  [PMID:16272386 "enters that of leucine/isovalerate (Liu, leucine and isovalerate utilization) at the level of methylcrotonyl-CoA"],
  so enzymes downstream of that point perform steps of acyclic monoterpenoid catabolism; PseudoCAP
  isoprenoid/terpene rows are refined to GO:0016100 monoterpenoid catabolic process, matching the liuC review.
