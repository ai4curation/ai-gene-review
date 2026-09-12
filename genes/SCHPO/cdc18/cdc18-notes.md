# cdc18 (Cdc6/Cdc18) — S. pombe — Review notes

UniProt: P41411 (CDC18_SCHPO), 577 AA. PomBase SPBC14C8.07c. Member of CDC6/cdc18 family (AAA+ ATPase).
Human/budding-yeast ortholog: Cdc6 / CDC6.

## Core biology
Cdc18 is the fission-yeast ortholog of Cdc6, an AAA+ ATPase pre-replicative complex (pre-RC)
component essential for DNA replication licensing. It is recruited to ORC-bound origins and, with
Cdt1, loads the MCM2-7 replicative helicase onto origins, licensing them for a single round of
firing. Cdc18 is the rate-limiting S-phase initiator; its abundance is tightly cell-cycle-controlled
at the level of transcription (MBF/Cdc10 at START) and proteolysis (CDK phosphorylation → SCF^Pop1/Pop2
ubiquitination → 26S proteasome). Overexpression drives re-replication. Cdc18 also contributes to the
S-phase/replication checkpoint by anchoring Rad3-Rad26 to chromatin at stalled forks.

## Key evidence

- Essential for DNA replication; couples S phase to START and mitosis; overexpression drives repeated
  rounds of DNA synthesis without mitosis; protein periodic, peaks at G1/S; nuclear localization.
  [PMID:8521469 "the fission yeast gene cdc18 is required for DNA replication and is transcriptionally activated by the cdc10/res1/res2 control acting at START in late G1"]
  [PMID:8521469 "overexpressing cdc18 is able to bring about repeated rounds of DNA synthesis in the absence of mitosis and of continuing protein synthesis"]
  [PMID:8521469 "The level of the cdc18-encoded protein p65cdc18 is periodic in the cell cycle, peaking at the G1 to S phase transition, and p65cdc18 is located in the nucleus"]
  [PMID:8521469 "p65cdc18 acts at the initiation of DNA replication and plays a major role in controlling the onset of S phase"]

- MCM loading / pre-RC: chromatin binding of mcm4 requires orc1 and cdc18 (= Cdc6 ortholog); occurs at
  anaphase B; mcm4 release during S phase requires replication; cdc18 overexpression drives re-replication
  with mcm4 chromatin-bound.
  [PMID:10747035 "Binding of mcm4 to chromatin requires orc1 and cdc18 (homologous to Cdc6 in budding yeast)"]
  [PMID:10747035 "Upon overexpressing cdc18, we show that mcm4 is required for re-replication of the genome in the absence of mitosis and is associated with chromatin in cells undergoing re-replication"]
  [PMID:10747035 "The assembly of pre-RCs requires Cdc6 and involves the assembly of six minichromosome maintenance (MCM) proteins around origins"]

- Degradation by SCF^Pop1: pop1 binds Cdc18 in vivo; pop1 mutant accumulates Cdc18 (ubiquitinated forms);
  controls genome ploidy.
  [PMID:9203581 "in a pop1 mutant Rum1 and Cdc18 proteins become accumulated to high levels"]
  [PMID:9203581 "Pop1 binds Cdc18 in vivo"]
  [PMID:9203581 "Pop1 functions as a recognition factor for Rum1 and Cdc18, which are subsequently ubiquitinated and targeted to the 26S proteasome for degradation"]

- Degradation by Sud1/Pop2: sud1+ binds Cdc18 in a phosphorylation-dependent manner; prevents re-replication.
  [PMID:9653157 "Sud1 itself is associated with the ubiquitin pathway in fission yeast and binds to Cdc18 in vivo"]
  [PMID:9653157 "Sud1-Cdc18 binding requires prior phosphorylation of the Cdc18 polypeptide at CDK consensus sites"]
  [PMID:9653157 "S phase is limited to a single round per cell cycle through cyclin-dependent kinase phosphorylation of critical replication factors, including the Cdc18 replication initiator protein"]

- Pop1/Pop2 form SCF complex that binds and directs proteolysis of Cdc18; Cdc18 binding to Pop2 depends on Pop1.
  [PMID:10209119 "pop1 and pop2 genes ... regulate the stability of the replication initiator Cdc18p and the Cdk inhibitor Rum1p"]
  [PMID:10209119 "binding of Cdc18p to Pop2p was dependent on Pop1p"]

- SCF^Pop1/Pop2 also degrades S-phase cyclin Cig2 (this is the substrate in PMID:14970237; Cdc18 is a
  known substrate of the same ligase but the Cdc18-Pop1 IPI is annotated to this paper as physical interaction).
  [PMID:14970237 "Two F-box/WD proteins Pop1 and Pop2 ... are responsible for Cig2 instability. Pop1 binds Cig2 in vivo"]

- Re-replication control via redundant CDK phosphorylation of Cdc18 and Orp2/Orc2; deregulated (overexpressed,
  phospho-site mutant) Cdc18 drives re-replication.
  [PMID:11486016 "A mutant lacking Cdc2 phosphorylation sites in Orp2 (orp2-T4A) allowed greater rereplication of DNA than congenic orp2 wild-type strains when the limiting replication initiation factor Cdc18 was deregulated"]
  [PMID:11486016 "Cdc2 phosphorylation of Orp2 may be redundant with regulation of Cdc18 for preventing reinitiation of DNA synthesis"]

- S-phase checkpoint maintenance: at stalled forks Cdc18 persists in a chromatin-bound complex with Rad3-Rad26;
  Rad26 directly binds Cdc18; Cdc18 anchors Rad3-Rad26 to chromatin (basis for GO:0140463 chromatin-protein
  adaptor activity IPI with rad3 SPAC9E9.08 and rad26 SPBC216.05; GO:0000785 chromatin IDA; GO:0033314 checkpoint).
  [PMID:17531813 "when DNA replication stalls, Cdc18 persists in a chromatin-bound complex including the checkpoint kinases Rad3 and Rad26"]
  [PMID:17531813 "Rad26 directly binds Cdc18 and is required for Rad3 recruitment to chromatin"]
  [PMID:17531813 "Cdc18 plays a pivotal role in checkpoint maintenance by anchoring the Rad3-Rad26 complex to chromatin"]

- Meiosis: Cdc18 protein synthesis is down-regulated during meiosis; lack of cdc18 prevents DNA replication
  in spores (nuclear localization assayed in S. pombe).
  [PMID:15278909 "in S. pombe cdc18 (the S. pombe CDC6 homologue), CDC6 protein synthesis is down regulated during meiosis. As such, the lack of cdc18 prevents DNA replication from occurring in spores"]

## GO annotation review reasoning

- GO:0005634 nucleus (IBA + IDA PMID:15278909): ACCEPT. Nuclear localization is well supported.
- GO:0006270 DNA replication initiation (IBA + IEA): ACCEPT (IBA core), the IEA is redundant — keep.
- GO:0003688 DNA replication origin binding (IBA): Cdc18 is recruited to origins via ORC; ACCEPT (origin-associated).
- GO:0033314 mitotic DNA replication checkpoint signaling (IBA): ACCEPT, supported by PMID:17531813 (checkpoint maintenance).
- GO:0005524 ATP binding (IEA/ISM): ACCEPT — AAA+ ATPase, Walker A P-loop FT BINDING 199..206.
- GO:0016887 ATP hydrolysis activity (IEA): ACCEPT (AAA+ ATPase); ATPase activity is core to Cdc6 family.
- GO:0006325 chromatin organization (IEA, from GO:0140463 link): over-broad; the real function is checkpoint
  anchoring, not chromatin organization. MARK_AS_OVER_ANNOTATED.
- GO:0051301 cell division (IEA keyword/InterPro): generic; KEEP_AS_NON_CORE.
- GO:0005515 protein binding (IPI x4): bare protein binding, uninformative. The interactors are pop1, pop2
  (degradation) and via 14970237. Replace with more informative terms / mark over-annotated; recommend MODIFY
  to ubiquitin-dependent context is not an MF; best practice: NON_CORE or note. Use MARK_AS_OVER_ANNOTATED with
  note to prefer adaptor/specific terms (the informative MF GO:0140463 already captured separately).
- GO:1902975 mitotic DNA replication initiation (IMP PMID:8521469): ACCEPT — core.
- GO:0140463 chromatin-protein adaptor activity (IPI PMID:17531813, with rad3/rad26): ACCEPT — informative MF
  for anchoring Rad3-Rad26 to chromatin.
- GO:0140530 MCM complex loading (IMP PMID:10747035, PMID:11532929): ACCEPT — core helicase-loading function.
- GO:0000785 chromatin (IDA PMID:17531813): ACCEPT — chromatin-bound at stalled forks/origins.
- GO:0005656 nuclear pre-replicative complex (ISO): ACCEPT — Cdc18 is a pre-RC component.
- GO:0043596 nuclear replication fork (IC from pre-RC): plausible but indirect; KEEP_AS_NON_CORE.
- GO:1902985 mitotic pre-replicative complex assembly (ISO): ACCEPT — core.

PMID:11532929 not in cache; title (PomBase): MCM complex loading paper. Defer/ACCEPT per PomBase IMP.
