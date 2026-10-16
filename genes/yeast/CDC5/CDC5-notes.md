# CDC5 (P32562) — working notes

Budding-yeast Polo-like kinase (sole PLK; PANTHER PTHR24345:SF0). N-terminal Ser/Thr
kinase domain, C-terminal polo-box domain (PBD) that docks on CDK-primed phosphosites
[PMID:27325700 "The Cdc5-cohesin association is mediated by direct interaction between the polo-box domain of Cdc5 and Scc1 phosphorylated at multiple sites in its middle region."].
Essential: deletion is lethal with a late-nuclear-division terminal phenotype
[PMID:8321244 "Deletion of CDC5 was lethal and resulted in a dumbbell-shaped terminal morphology, with the nuclei almost divided but still connected."].
Kinase activity confirmed with casein as exogenous substrate [PMID:8321244 "An activity that phosphorylated exogenously added casein was immunoprecipitated by antiserum against a TrpE-Cdc5 fusion protein"].

## Regulation / localisation
- Nuclear in G2/M; levels fall in anaphase/telophase in an APC-dependent manner
  [PMID:9819423 "Cdc5p accumulates in the nuclei of G2/M-phase cells, and its levels decline dramatically as cells progress through anaphase and begin telophase"].
- Polo box directs localisation to spindle poles and the bud neck
  [PMID:10594031 "localizes at spindle poles and the mother bud neck"].
- Metaphase SPB recruitment via the Clb3-Cdk1-primed anchor Csa1/Ypr174c
  [PMID:32553169 "phosphorylated Ypr174c recruits Cdc5 to SPBs in metaphase"].
- Centromeric chromatin association is cohesin-dependent (ChIP), i.e. not direct DNA binding
  [PMID:27226485 "cohesin is required for association of Cdc5 at centromeric chromatin"].

## Core function 1 — mitotic entry (Swe1 / Mih1 / Ndd1)
- Cdc5 interacts with and antagonises Swe1 [PMID:11438652 "These results also suggest that Cdc5 may be a negative regulator of Swe1."].
- Kinase activity drives Swe1 degradation and Mih1 nuclear entry (meiotic prophase I exit paper; same logic as mitosis)
  [PMID:41927924 "Cdc5 promotes Cdk1 activation by inducing Swe1 degradation and facilitating Mih1 nuclear translocation"].
- Cdc5 is recruited to CLB2-cluster promoters via Fkh2 and phosphorylates the co-activator Ndd1
  [PMID:17122856 "GST pulldown assays revealed that Fkh2p, but not Ndd1p, formed a complex with Cdc5p"; "through direct phosphorylation of the coactivator protein Ndd1p"].
  NB: GOA carries no BP term for this transcriptional role (only kinase MF + Fkh2 IPI). Not adding NEW; raised as a question.

## Core function 2 — chromosome segregation (cohesin, SPB separation, catenanes)
- Phosphorylates serines flanking Scc1 separase sites to enhance cleavage
  [PMID:11371343 "the Polo/Cdc5 kinase phosphorylates serine residues adjacent to Scc1 cleavage sites and strongly enhances their cleavage"].
- Pre-deposited on arm cohesin in G2/M via PBD [PMID:27325700 "budding yeast Plk1, Cdc5, is pre-deposited onto cohesin engaged in cohesion on chromosome arms in G2/M phase cells"].
- Cdk1-primed phosphorylation of Cdh1 inactivates APC/C-Cdh1 so Cin8/Kip1 accumulate for SPB separation
  [PMID:18500339 "adequate accumulation of Cin8 and Kip1 requires inactivation of the anaphase-promoting complex-activator Cdh1 through sequential phosphorylation by Cdk1 and polo kinase"].
- With Cdc14, modulates Top2 phosphorylation/SUMOylation/localisation to resolve catenanes; Top2 does the topological work
  [PMID:41533572 "we show that Cdc5 and Cdc14 independently modulate Top2 phosphorylation"].
  -> GOA "DNA conformation change" over-attributes the topological step to Cdc5; proposed MODIFY to mitotic sister chromatid segregation (GO:0000070), which also captures the Scc1 work.

## Core function 3 — mitotic exit (FEAR + MEN)
- FEAR: Cdc5 overexpression releases Cdc14 in S-phase-arrested cells with Cdc14 and Net1 phosphorylation
  [PMID:14551257 "overexpression of CDC5 led to Cdc14 release from the nucleolus in S phase-arrested cells, which correlated with the appearance of phosphorylated forms of Cdc14 and Cfi1/Net1."];
  Net1 phosphorylation state depends on Cdc5 [PMID:12056824 "Here we show that Cdc5 affects the phosphorylation state of Net1."];
  PBD binds Cdc14 directly [PMID:18927509 "we find that Cdc5 physically interacts with Cdc14 and that this association is mediated by Cdc5's Polo-box domain, a phospho-serine/phosphothreonine binding domain"].
- MEN: Bfa1 phosphorylation inhibits Bfa1-Bub2 GAP [PMID:12637549 "when Bfa1 is phosphorylated by Cdc5, its GAP activity with Bub2 is inhibited although its ability to interact with Tem1 is unaffected"];
  Cdc5 + Tem1 recruit Cdc15 to SPBs [PMID:21937712 "both Tem1 and Cdc5 are required to recruit the MEN kinase Cdc15 to spindle pole bodies, which is both necessary and sufficient to induce MEN signaling"];
  Cdc5 priming of Net1 targets Dbf2-Mob1 to the nucleolus [PMID:33481703 "priming phosphorylation of Cfi1/Net1, the nucleolar anchor of Cdc14, by the Polo-like kinase Cdc5 targets Dbf2-Mob1 to the nucleolus"].

## Core function 4 — cytokinesis at the bud neck
- Targets/activates Rho1 via its GEFs Tus1/Rom2 [PMID:16763112 "Cdc5 controls the targeting and activation of Rho1 (RhoA) at the division site via Rho1 guanine nucleotide exchange factors"].
- Primes Hof1 for Dbf2-Mob1 [PMID:21498574 "We show that polo-like kinase Cdc5 first phosphorylates Hof1 to allow subsequent phosphorylation by Dbf2-Mob1."].

## Non-core / context-specific
- Meiosis: JM resolution and monopolin localisation [PMID:12717442 "fail to efficiently resolve recombination intermediates as crossovers"];
  pachytene exit / SC disassembly [PMID:18832066 "Thus, Cdc5 is the only member of the Ndt80 transcriptome required for this critical step in meiotic progression."];
  meiotic spindle efficiency [PMID:24386320 "depletion of Cdc5 polo kinase activity delays spindle formation in DDR-arrested cells"].
- Checkpoint adaptation: attenuates Rad53 hyperphosphorylation [PMID:20126259 "Cdc5 acts to attenuate the DNA damage checkpoint through loss of Rad53 hyperphosphorylation to allow cells to adapt to DNA damage"];
  Rad53 binding is NOT classic PBD docking [PMID:20126259 "Rad53 provides the binding specificity to allow Cdc5 to phosphorylate it, in contrast to the classic model in which polo-like kinases recognize a substrate via their phosphobinding polo-box"].
  No GOA BP term for adaptation exists in the seed; not adding NEW.
- Nuclear-shape "flare" during mitotic arrest [PMID:25454593 "Here we show that mitotic flare formation is dependent on the yeast polo kinase Cdc5. This function of Cdc5 is independent of its known mitotic roles, including rDNA condensation."].

## Curation decisions (summary)
- 7x GO:0004672 protein kinase activity -> MODIFY to GO:0004674 (matches human PLK1 exemplar).
- 9x GO:0005515 protein binding: Cdc14 -> MODIFY GO:0051219 (PBD, phospho-dependent shown); Fkh2 -> MODIFY GO:0140297
  (DNA-binding TF binding; recruitment to promoters shown); Swe1 x2, Cdc7, Spo13, Lrs4, Rad9, Rad53 -> REMOVE as uninformative.
- GO:0019237 centromeric DNA binding -> MODIFY to GO:0000775 chromosome, centromeric region (ChIP, cohesin-dependent; no direct DNA binding assay).
- GO:0071103 DNA conformation change -> MODIFY to GO:0000070 (Cdc5 regulates Top2; does not itself alter topology).
- GO:0019941 modification-dependent protein catabolic process -> MODIFY to GO:0045732 positive regulation of protein catabolic process.
- Meiosis terms, nucleus-shape, Mih1 import, cytoplasm IBA, Rho-GEF localisation sub-step -> KEEP_AS_NON_CORE.
- All IBA rows accepted (PTN000679870 / PTN007795324 / PTN001217810), cytoplasm as non-core, consistent with PTHR24345 review.
