# CLB2 (P24869) — curation notes

Working journal for the GO annotation review of *Saccharomyces cerevisiae* CLB2 / YPR119W,
G2/mitotic-specific cyclin-2. Companion to `CLB2-ai-review.yaml`.

## Identity and gestalt

- UniProt P24869, 491 aa, cyclin A/B subfamily (IPR046965), two cyclin-box folds (CDD
  CYCLIN_CLBs_yeast_rpt1/rpt2). ComplexPortal CPX-1701 "CLB2-CDC28 kinase complex".
- Clb2 is not an enzyme. It is the regulatory subunit of Cdc28 (Cdk1); the Clb2-Cdc28
  (-Cks1) complex is the dominant M-phase CDK of budding yeast
  [file:yeast/CLB2/CLB2-deep-research-falcon.md "Clb2 is not itself an enzyme. Its primary
  function is to bind, activate, spatially direct, and confer substrate preference on the
  serine/threonine kinase Cdc28/Cdk1."].
- Discovery: high-copy suppressor of the mitosis-defective cdc28-1N allele
  [PMID:1849457 "Neither CLB1 nor CLB2 is essential; however, disruption of both is lethal and
  causes a mitotic defect."]; cdc28-1N clb2 is inviable while cdc28-4 clb2 is viable.
- Timing: Clb1/Clb2 expressed and activate Cdc28 from late S to mitosis; Clb2 is "the primary
  mitotic cyclin" and is absent from meiosis [PMID:8455600 "Clb1 and Clb2 were expressed and
  activated p34cdc28 later in the mitotic cell cycle, starting in late S phase and continuing
  up to mitosis."; "Clb2, the primary mitotic cyclin in S. cerevisiae, was not detectable
  during meiosis."].
- All lethal clb deletion combinations include clb2; conditional clb mutants arrest with
  duplicated, unseparated SPBs and no spindle [PMID:1387566 "All lethal combinations included
  the clb2 deletion, whereas the clb1 clb3 clb4 triple mutant was viable, suggesting a key role
  for CLB2."; "Electron microscopy showed that the spindle pole bodies had duplicated but not
  separated, and no spindle had formed."].
- Mechanistic outputs summarised in the deep research (Chee & Haase 2010 kinesin-5 Kip1/Cin8
  phosphosites; Ndd1/Fkh2 positive feedback on the CLB2 cluster; Cdc6 held in a
  licensing-incompetent Clb2-Cdk1-Cks1 complex, Philip et al. 2022; Swe1 docking via Clb2
  N260/K270, Hu et al. 2008). These PMIDs are not in the local cache, so they are cited only via
  the deep-research file.
- Inhibition/destruction: Swe1 Y19 phosphorylation (reversed by Mih1), Sic1, Mck1 GSK-3 binding
  [PMID:22918234 "We observe a direct interaction between Mck1 and Clb2 but not Cdk1 (data not
  shown); therefore, it is most plausible that Mck1 inhibits Clb2-Cdk1 activity through binding
  of Clb2."], and APC/C-Cdc20 then APC/C-Cdh1 proteolysis [PMID:22918234 "the
  anaphase-promoting complex (APC CDC20/CDH1 ) degrades the mitotic cyclin, Clb2"]. Clb2 is the
  APC/C substrate here, not an actor: no destruction-related process term is proposed
  (participation test).

## Localization

- Primarily nuclear at all stages; bipartite NLS (Srp1/Kap95, Ran), leucine-rich NES, Yrb2
  export; NLS deletion increases cytoplasmic and bud-neck signal [PMID:11171327 "Wild-type
  Clb2p is primarily nuclear at all points of the cell."; "Deletion of the Clb2p NLS causes
  increased cytoplasmic localization of the protein, as well as accumulation at the bud neck."].
- Nucleus, mitotic spindle, SPBs and mother-bud neck; neck localization is Clb2-specific and
  Bud3-dependent (residues 213-255 + hydrophobic patch), with a cytokinesis delay when lost
  [PMID:12972503 "The neck localization is specific to Clb2 as Clb1, Clb3 and Clb4 are never
  observed there, even when over-expressed."].

## Annotation decisions (summary)

| Term | Evidence | Action | Note |
|---|---|---|---|
| GO:0000082 G1/S transition | IBA | MARK_AS_OVER_ANNOTATED | deep cyclin node; Clb2 absent in G1, G1/S is Cln/Clb5 territory |
| GO:0000086 G2/M transition | IMP x2 | ACCEPT | core |
| GO:0000307 CDK holoenzyme complex | IBA | ACCEPT | Clb2-Cdc28-Cks1 |
| GO:0005515 protein binding (Cks1 x3, Cdk substrates x4, Nap1 x3) | IPI | REMOVE | uninformative per policy; interactions not disputed |
| GO:0005515 protein binding (Mck1) | IPI | MODIFY -> GO:0019901 protein kinase binding | Mck1 is a kinase and binding is the inhibitory mechanism |
| GO:0005634 nucleus | IBA, IDA x2 | ACCEPT | |
| GO:0005737 cytoplasm | IBA, IDA, IMP | ACCEPT | shuttling pool |
| GO:0005815 MTOC / GO:0005816 SPB / GO:0005819 spindle | IBA/IDA | ACCEPT | |
| GO:0005935 bud neck | IDA | KEEP_AS_NON_CORE | Clb2-specific, peripheral |
| GO:0006974 DNA damage response | IDA | KEEP_AS_NON_CORE | Clb2-Cdk1 at DSBs phosphorylates Fun30; checkpoint activation |
| GO:0007089 traversing Start | IBA | MARK_AS_OVER_ANNOTATED | node seeded only by pombe cdc13 (engineered single-cyclin) |
| GO:0010696 pos. reg. SPB separation | IGI x3 | ACCEPT | Kip1/Cin8 phosphorylation is the mechanism |
| GO:0016538 CDK regulator activity | IBA, IDA, IMP x2, IEA | ACCEPT | regulator term retained on all rows; the more specific GO:0061575 activator activity is used in core_functions (validator notes it is not itself an existing annotation) |
| GO:0032888 reg. of spindle elongation | IMP | MODIFY -> GO:1902846 positive regulation | direction unambiguous, via Net1/FEAR/Cdc14 |
| GO:0044772 mitotic phase transition | IEA | ACCEPT | broad but correct |

## Points to revisit

- The three Xenopus nap1l1 WITH partners on PMID:7622566 cannot be checked from the cached
  abstract; not asserted as mis-attributed, simply uninformative.
- DNA damage response: [PMID:26801641 "the recruitment of Cdk1 and cyclins Clb2 and Clb5
  ensures optimal Fun30 phosphorylation and checkpoint activation"]; clb2Δ has impaired Rad53
  phosphorylation and a higher rate of extensive resection. Kept non-core.
- Spindle elongation: [PMID:23468650 "mitotic CDK promotes spindle elongation by activating
  Cdc14 phosphatase, which reverses the protein phosphorylation imposed by S-phase CDK."].
- No NEW terms proposed. Morphogenesis (isotropic growth switch) and cytokinesis timing are
  downstream outputs and were not added; a curator may wish to consider
  GO:0007117 (budding cell bud growth) only with a direct-substrate argument.
