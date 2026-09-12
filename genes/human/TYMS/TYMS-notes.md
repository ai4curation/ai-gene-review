# TYMS (thymidylate synthase) review notes

UniProtKB:P04818 (TYSY_HUMAN), HGNC:12441, EC 2.1.1.45. 313 aa, homodimer.

Deep research note: falcon provider is out of credits (HTTP 402); no
`-deep-research-falcon.md` was generated. This review is grounded in the cached
UniProt record (`TYMS-uniprot.txt`), the seeded GOA (`TYMS-goa.tsv`), and the cached
abstract-only publications in `publications/PMID_*.md` plus the two Reactome entries.
All 6 cited PMIDs are `full_text_available: false` (abstract-only), so supporting_text
quotes are drawn from those abstracts (verbatim) or from `file:human/TYMS/TYMS-uniprot.txt`.

## Core biology

TYMS catalyses the reductive methylation of dUMP to dTMP, the **sole de novo source of
thymidylate**. It uses (6R)-5,10-methylene-5,6,7,8-tetrahydrofolate (CH2H4folate) as
both the one-carbon donor and the reductant; the folate is oxidised to 7,8-dihydrofolate
(DHF), which DHFR then regenerates to tetrahydrofolate.

- Reaction (UniProt CATALYTIC ACTIVITY / RHEA:12104):
  `dUMP + (6R)-5,10-methylene-5,6,7,8-tetrahydrofolate = 7,8-dihydrofolate + dTMP`
  [file:human/TYMS/TYMS-uniprot.txt].
- FUNCTION: "Catalyzes the reductive methylation of 2'-deoxyuridine 5'-monophosphate
  (dUMP) to thymidine 5'-monophosphate (dTMP), using the cosubstrate, 5,10-
  methylenetetrahydrofolate (CH2H4folate) as a 1-carbon donor and reductant and
  contributes to the mitochondrial and nuclear de novo thymidylate biosynthesis pathway."
- PATHWAY: "Pyrimidine metabolism; dTTP biosynthesis."
- SUBUNIT: "Homodimer." Part of the de novo thymidylate synthesis complex with SHMT1 and
  DHFR (PMID:22235121).
- Active-site nucleophile Cys195 (ACT_SITE 195).

## Localization

- Classic cytosolic enzyme (Reactome R-HSA-73605 "Cytosolic thymidylate synthase ...";
  GOA cytosol IBA + TAS).
- Nucleus during S and G2/M (SUBCELLULAR LOCATION note; IDA PMID:21876188, EXP PMID:22235121).
- Mitochondrion / matrix / inner membrane: a de novo dTMP pathway (SHMT2, TYMS, DHFRL1)
  operates in mitochondria (IDA PMID:21876188). "Human DHFRL1, SHMT2, and TYMS were
  localized to mitochondrial matrix and inner membrane."
- As a component of the de novo thymidylate complex, localizes to replication forks
  during DNA synthesis (PMID:22235121; GOA replication fork IDA).

## Moonlighting / regulation (non-core)

- Translational autoregulation: TS protein binds its own mRNA and represses its
  translation; dUMP/FdUMP/CH2H4folate relieve the repression (PMID:1924359). This grounds
  the GO MF terms mRNA regulatory element binding translation repressor activity
  (GO:0000900), sequence-specific mRNA binding (GO:1990825), and BP negative regulation of
  translation (GO:0017148). RNA-binding is a genuine moonlighting activity but is not the
  core metabolic function -> KEEP_AS_NON_CORE.
- Chemotherapy target: inhibited by the 5-FU metabolite FdUMP and by antifolates
  (raltitrexed, pemetrexed) — many drugs listed in UniProt DrugBank xrefs. TS levels are
  E2F1-regulated (Reactome R-HSA-8962050) and elevated in many cancers; ectopic
  catalytically-active TS is transforming (PMID:15093541).
- Disease: germline TYMS deficiency (with an ENOSF1 haplotype) causes digenic dyskeratosis
  congenita (DKCD, MIM:620040; PMID:35931051) — a nucleotide-metabolism deficiency, not a
  gain of a new function.

## Curation decisions (summary)

- MF thymidylate synthase activity (GO:0004799): ACCEPT (all copies) — core.
- BP dTMP biosynthetic process (GO:0006231), dTTP biosynthetic process (GO:0006235):
  ACCEPT — core pathway.
- GO:0016741 transferase activity, transferring one-carbon groups (IEA): MARK_AS_OVER_ANNOTATED
  — correct but a general parent of GO:0004799 which is already annotated.
- cytosol (GO:0005829) IBA/TAS: ACCEPT — core location.
- nucleus, cytoplasm, mitochondrion, mito inner membrane, mito matrix, replication fork:
  ACCEPT (IDA/EXP-supported) but non-core-flavoured location contexts; keep as documented.
- DNA replication (GO:0006260), 'de novo' pyrimidine nucleobase biosynthetic process
  (GO:0006207): KEEP_AS_NON_CORE — pathway-context BP from the replication-fork complex paper.
- protein binding (GO:0005515) IPI: MARK_AS_OVER_ANNOTATED — bare protein binding
  (SHMT1/DHFR complex); uninformative MF, per curation policy.
- folic acid binding (GO:0005542) IC: ACCEPT — cofactor is a folate (methylene-THF); IC on GO:0004799.
- tetrahydrofolate interconversion (GO:0035999): ACCEPT — reaction converts CH2H4folate to DHF.
- DNA biosynthetic process (GO:0071897) IC: KEEP_AS_NON_CORE — downstream of dTMP supply.
- mRNA binding / translation repressor / negative regulation of translation: KEEP_AS_NON_CORE
  (moonlighting autoregulation).
</content>
</invoke>
