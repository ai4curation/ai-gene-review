# SWE1 (YJL187C, UniProt P32944) — curation notes

## 2026-09-25 — first full review

### Identity and family
- Swe1 = *S. cerevisiae* Wee1 homologue, 819 aa, C-terminal kinase domain 444-794, ATP-binding Lys473,
  catalytic Asp579 (UniProt features). Long, disordered, heavily phosphorylated N-terminal regulatory
  region (UniProt lists >30 phosphosites, by Cdc28, Cdc5 and Cla4).
- PANTHER PTHR11042:SF196; the family name is dominated by eIF2-alpha kinases (GCN2 is the fungal
  cytoplasm-IBA donor). `modules/g2_m_transition.yaml` uses Swe1 as the budding-yeast Wee1 exemplar in the
  `wee1_kinase` annoton (PAINT nodes PTN000113601, PTN008315181, PTN000867899).
- UniProt gives EC 2.7.11.1 (Ser/Thr), whereas *S. pombe* wee1 carries EC 2.7.10.2 (Tyr). The
  physiologically defined reaction is tyrosine phosphorylation of Cdc28 Tyr19.

### Core biology
- Founding paper: [PMID:8253069 "Swe1 immunoprecipitates were capable of tyrosine phosphorylating and
  inactivating p34CDC28 complexed with Clb2, a G2-type cyclin, but not p34CDC28 complexed with Cln2, a
  G1-type cyclin"]; [PMID:8253069 "SWE1 overexpression arrests cells in G2 with short spindles whereas
  deletion of SWE1 did not alter the cell cycle but did eliminate the G2 delay observed in mih1- mutants"].
  So: dispensable in an unperturbed cycle, opposed by Mih1 (Cdc25).
- Morphogenesis checkpoint effector: [PMID:8930890 "We show that the ability of this checkpoint to delay
  nuclear division requires the SWE1 gene, encoding a protein kinase that inhibits the master cell cycle
  regulatory kinase Cdc28."]; the checkpoint monitors actin: [PMID:9744879 "Thus, myo2-66 and tpm1Δ
  mutants experienced a cell cycle delay resulting from Cdc28p tyrosine phosphorylation (reversible by
  Swe1p elimination or Mih1p overexpression)."] and Lat-A arrest is Swe1-dependent [PMID:9744879 "This
  block to nuclear division was Swe1p dependent because swe1Δ cells completed nuclear division by 2 h"].
- Localisation: [PMID:10805747 "In budded wild-type cells, Swe1p was detected only in the nucleus (12% of
  the cells examined), only at the neck (23% of the cells), or at both locations (39% of the cells)"];
  [PMID:10805747 "the neck localization of Swe1p requires both Hsl1p and Hsl7p, as well as the septins"];
  [PMID:10805747 "The stabilized Swe1p in hsl1 and hsl7 mutants accumulated in the nucleus, which
  presumably facilitates its inhibition of nuclear Clb-Cdc28p complexes."]. The neck is where Swe1 is
  inactivated/degraded; the nucleus is where it acts on Clb-Cdc28.
- Feedback with its substrate: [PMID:16096060 "Phosphorylation of Swe1 by Cdk1 activates Swe1 and is
  required for formation of a stable Swe1-Cdk1 complex that maintains Cdk1 in the inhibited state."]
- Cdc5 (Polo) interaction: [PMID:11438652 "Our work shows that Cdc5, the Polo kinase in budding yeast,
  interacts with Swe1."]; Cdc5 overproduction modifies Swe1 and suppresses Swe1-dependent hsl1/hsl7
  phenotypes. Later work (Asano 2005, Sakchaisri 2004 — not cached) shows Cla4 -> Clb2-Cdc28 -> Cdc5
  sequential phosphorylation drives SCF(Met30)-dependent degradation (UniProt PTM section).

### Secondary roles
- Meiosis: pachytene checkpoint [PMID:10619027 "In S. cerevisiae, this checkpoint requires Swe1, which
  phosphorylates and inactivates the cyclin-dependent kinase Cdc28."]; 2026 update [PMID:41927924 "We
  show that Swe1 is required for checkpoint maintenance but not activation."], with zip1Δ swe1Δ genetics
  [PMID:41927924 "checkpoint signaling is initially triggered in zip1Δ swe1Δ, but it is prematurely
  downregulated, allowing faster and more efficient meiotic progression compared to zip1Δ"]. Cdc5 drives
  Swe1 degradation independently of CDK in meiosis (unlike mitosis).
- SPB separation: [PMID:8887667 "We also find that the overexpression of SWE1, the budding-yeast homolog
  of wee1, also leads to a failure to segregate SPBs."] — overexpression phenotype, downstream of Cdc28
  Tyr19 inhibition.
- Cell size: swe1Δ scored in the genome-wide size screen [PMID:12089449]; abstract does not name SWE1.
  Harvey & Kellogg 2003 (PMID:12593792, not cached) show swe1Δ cells are smaller — real but modest effect
  in budding yeast, where Start dominates size control.
- Re-entry after G1 arrest: [PMID:15107621 "Our data suggest that Swe1 is required for timely entry into
  cell cycle after a G1 arrest caused by impairment in pre-60S biogenesis and in protein synthesis."],
  and [PMID:15107621 "such a prolonged delay is independent of the Tyr19 phosphorylation in Cdc28"].
  Mechanism unknown.
- Sphingolipids: [PMID:26634277 "Deletion of the Swe1 kinase renders mutant cells sensitive to serine
  palmitoyltransferase inhibition due to impaired sphingoid long-chain base synthesis."]; orm1Δ orm2Δ
  suppresses; cdc28-Y19F phenocopies swe1Δ; the Orm2-phosphorylation mechanism is "presumably"
  [PMID:26634277 "Here we show that the Swe1 checkpoint kinase positively regulates SPT, presumably by
  phosphorylating Orm2, independently of Ypk1."]. Genetic, not biochemical; possibly routed through CDK.

### Grading decisions (42 GOA rows)
- ACCEPT (19): tyrosine kinase (IBA/IDA/IEA), protein kinase (HDA/IEA), ATP binding, nucleus (x4), bud
  neck (x3), GO:0010972 IBA, GO:0044879 IDA+IMP, GO:0051598 IGI, GO:0110031 IBA, GO:0051447 IEA.
- MODIFY (4): GO:0000086 IDA+IMP -> GO:0010972 (Swe1 opposes the transition; the negative-regulation
  child is the accurate term). GO:0040020 IMP -> GO:0051598 / GO:0110031 (too general). GO:0106310 IEA
  -> GO:0004674 (term usage note: serine-specific kinases only; Swe1 is dual-specificity/Tyr-directed;
  same call as on human PKMYT1).
- KEEP_AS_NON_CORE (10): cytoplasm IBA; Ser/Thr kinase IEA (EC); cell size HMP; re-entry IGI x3;
  sphingolipid IMP + IGI x3.
- MARK_AS_OVER_ANNOTATED (2): GO:0010697 negative regulation of SPB separation (IMP/IGI) — overexpression
  readout of CDK inhibition, not a separate Swe1 process.
- REMOVE (7): all bare GO:0005515 protein-binding IPI rows (Hsl7 x3, Cdc5 x2, Kin1, Cdc14) per repository
  policy — interactions are real regulators OF Swe1 but no informative MF term for Swe1 follows from them.

### Open points
- Is Swe1 -> Orm2 phosphorylation direct? Would upgrade GO:0090154 from non-core if shown.
- Should the UniProt EC be 2.7.10.2 (as for pombe wee1) rather than 2.7.11.1?
- Nothing NEW proposed: the DNA-replication-stress and filamentous-growth roles (UniProt FUNCTION, papers
  not cached) reuse the same Cdc28-Tyr19 activity and are not represented in GOA; not added without
  cached primary evidence.
