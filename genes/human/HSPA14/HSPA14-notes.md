# HSPA14 (HSP70L1 / HSP70-like protein 1) — research notes

UniProt: Q0VDF9 (HSP7E_HUMAN), 509 aa. Gene synonyms HSP60, HSP70L1.

## Core identity
HSP70-family protein and the Hsp70/DnaK-type subunit of the mammalian
ribosome-associated complex (RAC), a heterodimer with the Hsp40/DnaJ-type
co-chaperone DNAJC2 (MPP11). RAC acts at the ribosomal exit tunnel to assist
co-translational folding of nascent polypeptides.

- [file:human/HSPA14/HSPA14-uniprot.txt "FUNCTION: Component of the ribosome-associated complex (RAC), a complex involved in folding or maintaining nascent polypeptides in a folding-competent state. In the RAC complex, binds to the nascent polypeptide chain, while DNAJC2 stimulates its ATPase activity."]
- [file:human/HSPA14/HSPA14-uniprot.txt "SUBUNIT: Component of ribosome-associated complex (RAC), a heterodimer composed of Hsp70/DnaK-type chaperone HSPA14 and Hsp40/DnaJ-type chaperone DNAJC2."]
- [file:human/HSPA14/HSPA14-uniprot.txt "SUBCELLULAR LOCATION: Cytoplasm, cytosol"]

## RAC paper (PMID:16002468, Otto et al. 2005 PNAS)
Identified the mammalian RAC as MPP11(DNAJC2)/Hsp70L1.
- [PMID:16002468 "Purification of MPP11 revealed that it forms a stable complex with Hsp70L1, a distantly related homolog of Ssz1p."]
- [PMID:16002468 "On the sequence level neither peptide binding domain nor ATPase domains of Hsp70L1 are particularly similar to Ssz1p"]
- Important nuance: like its yeast counterpart Ssz1p, Hsp70L1 is an ATYPICAL Hsp70. In yeast RAC, Ssz1p/zuotin (RAC) act to stimulate the ATPase of the ribosome-bound Hsp70 Ssb1/2p; RAC itself is the co-chaperone module. So HSPA14's own ATP-hydrolysis "chaperone" role is not a canonical autonomous foldase.
- [PMID:16002468 "only the complex of zuotin and Ssz1p (RAC) is able to stimulate the ATPase of the yeast ribosome-bound Hsp70 Ssb1/2p"]
- HeLa immunofluorescence + rat liver fractionation: cytosolic, ribosome-associated.
- [PMID:16002468 "Hsp70L1 comigrated with polysomes and ribosomes and was released by high-salt treatment"]

## GO annotation review notes (goa.tsv)
- IBA nucleus / plasma membrane: family-level PANTHER transfers from canonical Hsp70s; no experimental support for HSPA14 in nucleus or PM. UniProt SUBCELLULAR LOCATION = cytoplasm/cytosol only. -> MARK_AS_OVER_ANNOTATED.
- IBA ATP hydrolysis activity / IEA ATP hydrolysis: HSP70 fold present; HSPA14 has nucleotide-binding domain. ATPase is stimulated by DNAJC2 in the RAC. Keep ATP binding (KW) and ATP hydrolysis as supported by fold + UniProt FUNCTION (DNAJC2 stimulates its ATPase activity). Core enzymatic-ish MF.
- IBA heat shock protein binding GO:0031072: as RAC subunit it binds DNAJC2 (an Hsp40); reasonable. ACCEPT non-core? It binds its J-protein partner. Keep as supporting.
- IBA / IEA protein folding chaperone (GO:0044183 / GO:0140662): HSPA14 functions in co-translational folding as part of RAC. GO:0044183 protein folding chaperone is a reasonable core-ish MF. But it is a co-chaperone module (with DNAJC2), assisting nascent-chain folding — keep as core MF (chaperone) with caveat.
- protein refolding GO:0042026 IBA: canonical Hsp70 refolding transferred from family; HSPA14 is specialized for co-translational (de novo) folding, not stress refolding. MARK_AS_OVER_ANNOTATED / KEEP_AS_NON_CORE.
- ribosome (GO:0005840) colocalizes_with IBA + IDA (PMID:16002468): directly shown. ACCEPT.
- cytosol GO:0005829 IBA/IEA/IDA (PMID:21231916, PMID:16002468): ACCEPT (IDA core localization).
- membrane GO:0016020 HDA (PMID:19946888): high-throughput membrane-proteome detection; HSPA14 is cytosolic/ribosome-associated; peripheral. KEEP_AS_NON_CORE.
- protein folding GO:0006457 NAS (ComplexPortal, PMID:16002468): RAC role. KEEP_AS_NON_CORE (downstream process of chaperone module).
- protein folding chaperone complex GO:0101031 part_of IPI (PMID:16002468): the RAC complex. ACCEPT (this is exactly RAC).
- 'de novo' cotranslational protein folding GO:0051083 TAS (PMID:16002468): the precise BP for RAC. ACCEPT as core process.
- protein binding IPI: partners DNAJC2 (Q99543) — informative (RAC partner) -> capture as Hsp70/chaperone binding; NFAM1 (Q8NET5) — HT interactome, not chaperone-related. Keep DNAJC2 ones meaningful, NFAM1 over-annotated.

Partner ID map: Q99543=DNAJC2(MPP11); Q8NET5=NFAM1.

## Immunoadjuvant / DC activation
Hsp70L1 was reported to activate dendritic cells and act as a Th1 adjuvant
(PubMed:14592822, 15930317, 18851947). This is an applied/immunology property,
not a core GO molecular function; not in GOA. Noted, not annotated.

## Core function synthesis
1. Hsp70/DnaK-type chaperone subunit of RAC — ATP-dependent, co-translational
   folding of nascent chains (GO:0044183 protein folding chaperone; process
   GO:0051083 de novo cotranslational protein folding; complex GO:0101031).
2. ATP binding / ATP hydrolysis (HSP70 NBD), stimulated by DNAJC2.

## 2026-09-21 full-gene re-review

All23 original source assertions preserved. Actual PTHR19375 v19 target leafPTN002500131 is below ATPase/refolding IBDPTN000452648 and nuclear IBDPTN002500132. The SSZ1 loss nodePTN001065099 is outside this path. The frozen plasma-membrane IBA citesPTN002500132 but the current path lacks that assertion; this is a version discrepancy, not a biological negative. Nuclear/PM/refolding exclusions based only on primary cytosol/mRAC specialization were replaced with uncertainty.

Full21245388 Methods/Results/Discussion distinguish ATP binding from catalysis: “the rate of ATP hydrolysis was only 0.01 ATP per min, which is very close to background hydrolysis.” Authors conclude “the question of whether Hsp70L1 can hydrolyze ATP cannot be conclusively answered.” Hydrolysis-site mutants complement yeast; binding-defective LKA does not. mRAC stimulates a separate Hsp70, not demonstrably its own Hsp70L1 subunit. Both ATPase rows now UNDECIDED, and description/core no longer assert the unsupported cycle. Full16002468 establishes the heterodimer and ribosome-associated contribution. Direct HSPA14 nascent-chain binding remains proposed.

All source interactions checked:33961781 includes NFAM1 and DNAJC2,35271311/40205054 include DNAJC2, supporting informative HSP-binding replacements. Bare28514442NFAM1 binding is removed as uninformative, not declared false. Broad foldingNAS restored to core. Generic membraneHDA remains contextual; membrane fraction is not proof of PM activity.

Existing SSZ1 ATPase OpenScientist output was read: its claim that metazoan HSPA14 was untested misses21245388. No target report existed in exact repository/global query checks. A distinct focused request includes this assay, the21231916 HSPA14 refolding figures, and secondary compartments. The author manuscript of21231916 was found at https://www.researchgate.net/publication/49752468_The_diverse_members_of_the_mammalian_HSP70_machine_show_distinct_chaperone-like_activities but its body font encoding and inaccessible PDF prevent reliable figure adjudication here. No NEW assertion added.
