# ZDHHC23: evidence notes

## Paired horse benchmark evidence review

The human reference supplies mechanistic evidence for the corresponding selected horse protein; the human conclusion alone is not validation of the horse sequence. The exact horse comparison is in `genes/HORSE/ZDHHC23/ZDHHC23-bioinformatics/RESULTS.md`. Research reports are source leads; annotation decisions cite the underlying publication or experimentally supported UniProt passages. Unresolved source-specific results retain UNDECIDED.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Identity: Q8IYP9 is the reviewed canonical human ZDHHC23 product (409 aa, Swiss-Prot), not a fragment or isoform. It keeps the full DHHC cysteine-rich domain (259-309) with an intact D286-H287-H288-C289 motif; C289 is the S-palmitoyl cysteine intermediate (UniProt FT ACT_SITE, PROSITE-ProRule PRU00067).

Phylogenetic placement: PANTHER PTHR22883:SF475 (PALMITOYLTRANSFERASE ZDHHC23). Mouse Zdhhc23 (Q5Y5T3, MGI:2685625) is in the same subfamily (interpro/panther/PTHR22883/PTHR22883-entries.csv). The plasma-membrane localization IBA comes from PTN008583751, a ZDHHC23-clade node seeded by human ZDHHC23 and mouse Zdhhc23. The other IBAs (MF, ER, Golgi, protein targeting to membrane) come from the deep DHHC-family node PTN000525256.

Evidence:
- [PMID:22399288 "palmitoylation of the intracellular S0-S1 loop of BK channels is controlled by two of the 23 mammalian palmitoyl-transferases, zDHHC22 and zDHHC23."] siRNA screen in HEK293 cells; overexpression raised S0-S1 reporter surface expression to 144% of control.
- [PMID:22399288 "zDHHC23 predominantly co-localized with markers of the Golgi network (GM130, Pearson's R coefficient of 0.71 ± 0.01, n = 15) and TGN (TGN38, Pearson's R coefficient of 0.38 ± 0.02, n = 15)."] ZDHHC23 itself was not co-assayed with the ER marker; only BK channels were.
- [PMID:31213527 "S-acylation is significantly reduced in mice with a genetic deletion of the palmitoyl acyltransferase (Zdhhc23) that controls S-acylation of the S0-S1 loop."] In beta1-expressing smooth muscle, loss of Zdhhc23 lowers BK current without changing surface expression [PMID:31213527 "In the absence of β1-subunits, S-acylation promotes cell surface expression, whereas in its presence, S-acylation controls functional coupling."]. The trafficking role is therefore conditional.
- [PMID:38050183 "palmitoyltransferase ZDHHC23 expression was upregulated, leading to increased palmitoylation levels of GFAP"]: a single mouse study, not used for annotation.
- [PMID:30658672 "ZDHHC18 and ZDHHC23 competitively interact with a BMI1 E3 ligase, RNF144A, to regulate the polyubiquitination and accumulation of BMI1."]: a protein-network effect with no demonstrated catalysis; not annotated.

Changes from the previous review:
- Golgi apparatus (IBA and IEA): ACCEPT changed to MODIFY, replaced by Golgi membrane, which is already present.
- ER (IBA): ACCEPT changed to MARK_AS_OVER_ANNOTATED. This is a family-node propagation that conflicts in compartment with the subfamily-specific Golgi/TGN data.
- protein targeting to membrane (IBA): ACCEPT changed to KEEP_AS_NON_CORE.
- protein binding (GLIS1, HuRI Y2H): KEEP_AS_NON_CORE changed to REMOVE, following the GO:0005515 policy.
- The MF, protein palmitoylation and PM-localization rows are unchanged (ACCEPT). palmitoyltransferase activity stays MODIFY to GO:0019706.
- Rewrote the description and added three references: PMID:31213527, PMID:30658672 and PMID:38050183, located by PubMed title search and cached. Status set to COMPLETE.
- No NEW annotations were added. The GFAP substrate and BMI1 regulation each rest on one study, and in the BMI1 case ZDHHC23 does not catalyse the reported step.

Relative for review next: mouse Zdhhc23 (Q5Y5T3), the ortholog in the same PANTHER subfamily SF475 and PAINT node PTN008583751, which has knockout data. The repo has no review of it.
Family review interpro/panther/PTHR22883 places ZDHHC23 in SF475, which agrees with UniProt. No module in modules/ mentions ZDHHC23 or PTHR22883.
