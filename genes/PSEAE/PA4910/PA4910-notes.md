# PA4910 (Q9HUQ3) notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9HUQ3 --alias PA4910`; accession matches the
worklist. Unreviewed TrEMBL entry with no gene symbol, so the locus tag is the
folder name. No deep-research provider key was available. The only paper on the
gene is the Johnson et al. 2008 transport-gene screen (PMID:18833300, full text
cached).

### Identity and literature

- LivG-type ABC ATPase: PF00005 ABC_tran plus PF12399 BCA_ABC_TP_C, both ABC
  transporter PROSITE signatures, PTHR45772:SF11 (LivG). No TM segments.
- Operon PA4909-PA4913, paralogous to braCDEFG (PA1070-PA1074)
  [PMID:18833300 "Genes PA4910 and PA4912 comprise two genes of a five gene operon predicted to be involved in transport of branched chain amino acids."];
  subunit assignment
  [PMID:18833300 "PA4910 encodes a putative ATP-binding protein, while PA4912 encodes a predicted membrane component of this ABC amino acid transporter."].
- Phenotype
  [PMID:18833300 "Disruption of PA4910 resulted in reduced utilization of D-Alanine (as a nitrogen source), while PA4912 mutants had disrupted D-Alanine and D-Valine utilization (Table 2)."].
  No L-amino acid phenotype was recorded for PA4910, although every bra mutant
  showed L-Ala defects in the same screen.
- Substrate specificity in HAAT importers is set by the periplasmic binding
  protein. PA4910's system has its own (PA4913), uncharacterised; this is why
  the L-amino acid IBAs propagated from E. coli LivG and from BraF are left
  UNDECIDED rather than accepted.

## Consistency with the already-reviewed siblings

- **braG** (P21630) is on a different node (PTN000657089, the LivF ATPase node),
  so it does not share PA4910's node; its notes record that node separately.
- **PA4912** (Q9HUQ1) is the permease of the same operon, on the permease nodes
  PTN000209860 and PTN000765102, not on PTN000656921. So PA4910 shares no node
  with either already-reviewed gene; the shared element is the single seed
  paper.
- **braF** (P21629) is the gene that shares PTN000656921 with PA4910, and the
  node-level assessment was recorded there. The present review follows it: the
  D-alanine rows are UNDECIDED, the phenylalanine rows are
  MARK_AS_OVER_ANNOTATED, and ATP binding/hydrolysis and plasma membrane are
  accepted. braF and PA4912 recorded no source defects for the D-alanine rows,
  and neither does this review.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000656921 | GO:0042941 D-alanine transmembrane transport | 2 (P21629 braF, Q9HUQ3 PA4910) | 25 (15 taxa) | GO:0042941, IMP, PMID:18833300 (PseudoCAP) | INDIRECT-PHENOTYPE | A partial D-alanine nitrogen-source growth defect in one Biolog screen, with no uptake or binding assay and an uncharacterised binding protein for this system. Plausible for a D-amino acid importer, not established. The appearance of PA4910 in its own WITH/FROM is the expected seed self-reference. | braF (P21629), the LIV-I ATPase: the same screen, the same kind of partial phenotype | No independent support — both seeds are the same kind of weak phenotype from the same screen. Not filed as a GO_CENTRAL defect, following braF and PA4912: the claim is plausible and not refuted, and the node also carries well-grounded E. coli LivG-seeded MF IBDs. |

Node composition (from braF's assessment): 25 leaves in 15 taxa, including
E. coli/Salmonella/Yersinia LivG, BraF, PA4910, seven Bradyrhizobium japonicum
HAAT ATPases, Geobacter, Deinococcus, Thermotoga, Chloroflexus, Streptomyces,
Fusobacterium and Streptococcus members — several paralogous systems per genome
whose substrates are unknown. That is the standing caveat on every
substrate-level term at this node.

## Decisions summary

- ACCEPT: ATP binding (IEA), ATP hydrolysis activity (IEA), plasma membrane
  (IBA).
- TOO_GENERAL: nucleotide binding (IEA; ATP binding is asserted).
- MARK_AS_OVER_ANNOTATED: L-phenylalanine transporter activity (IBA),
  phenylalanine transport (IEA).
- UNDECIDED: L-valine and L-isoleucine transporter activity, L-alanine
  transport, L-valine and L-isoleucine import, isoleucine and L-valine
  transmembrane transport (ARBA), D-alanine transmembrane transport (IBA, IMP).
- Counts: ACCEPT 3, TOO_GENERAL 1, MARK_AS_OVER_ANNOTATED 2, UNDECIDED 9.
- Defects: none (PSEUDOCAP 0, GO_CENTRAL 0), consistent with braF, braD, braG
  and PA4912.
- One BIOLOGY knowledge gap recorded: the substrate range of the PA4909-PA4913
  importer is undetermined.
