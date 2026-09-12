# mei2 (P08965, SPAC27D7.03c) — S. pombe — Curation notes

## Overview
Mei2 is the master RNA-binding regulator of meiosis in the fission yeast *Schizosaccharomyces pombe*.
It is an RRM-containing protein (three RRMs; the C-terminal RRM3 is essential and sufficient for meiRNA
binding) that binds the meiosis-specific long non-coding RNA meiRNA (encoded by *sme2*, PomBase:SPNCRNA.103)
and forms the nuclear "Mei2 dot". Mei2 is required both for premeiotic DNA synthesis and for entry into
meiosis I. It is negatively regulated by Pat1(Ran1) kinase phosphorylation and by the TORC1 system, and
it antagonizes the Mmi1/MTREC-mediated selective elimination of meiotic mRNAs.

## Core function evidence

- **RNA-binding protein essential for premeiotic DNA synthesis and meiosis I**
  [PMID:7520368 "S. pombe mei2, which is essential for the initiation of premeiotic DNA synthesis, encodes an RNA-binding protein"]
  [PMID:7520368 "A temperature-sensitive mei2 mutant performs premeiotic DNA synthesis but does not undergo meiotic divisions, suggesting that Mei2 is required also for meiosis I"]
  [PMID:7520368 "Mutations that apparently block the RNA binding ability of Mei2 inhibit premeiotic DNA synthesis"]

- **Binds the noncoding meiRNA (sme2)**
  [PMID:7520368 "A novel, polyadenylated RNA species (meiRNA), which suppresses this temperature-sensitive defect if overexpressed, specifically binds to Mei2 both in vivo and in vitro"]
  [PMID:35512546 "Mei2 binds to a specific non-coding RNA species, meiRNA, and accumulates at the sme2 gene locus, which encodes meiRNA"]
  RRM3 binds the 5' region of meiRNA; preferentially U-rich (UUC(U)) motifs:
  [PMID:35512546 "We found that Mei2 RRM3 interacted in a sequence-specific manner with a UUC(U) motif of meiRNA"]
  [PMID:24920274 "Mei2 interacts preferentially with the 5′ region of meiRNA-L"]

- **Mei2 dot (nuclear body at sme2 locus)**
  [PMID:9062192 "Mei2 is localized mainly in the cytoplasm of proliferating cells but is seen as a single spot close to the microtubule organizing centre in prophase nuclei during meiosis"]
  [PMID:12808043 "the Mei2p dot is in association with the sme2 gene on the short arm of chromosome II, which encodes meiRNA"]
  [PMID:12808043 "This dot formation requires a meiosis-specific RNA species, meiRNA"]

- **meiRNA-assisted nuclear localization**
  [PMID:9778252 "meiRNA is required for the nuclear localization of Mei2p and is detectable in the dot"]

- **Antagonism of Mmi1-mediated mRNA elimination (mRNA stabilization)**
  [PMID:16823445 "We propose that Mei2 turns off the DSR-Mmi1 system by sequestering Mmi1 to the dot and thereby secures stable expression of meiosis-specific transcripts"]
  [PMID:22144909 "The RRM-type RNA-binding protein Mei2 is a master regulator of meiosis in fission yeast, in which it stabilizes meiosis-specific mRNAs by blocking their destruction"]
  protein sequestering activity (sequesters Mmi1):
  [PMID:16823445 "At meiotic prophase these foci precipitate to a single focus, which coincides with the dot formed by the master meiosis-regulator Mei2. A meiotic arrest due to the loss of the Mei2 dot is released by a reduction in Mmi1 activity"]

## Regulation

- **Pat1(Ran1) phosphorylation inactivates Mei2; dephosphorylation triggers the mitosis-to-meiosis switch**
  [PMID:9062192 "the RNA-binding protein Mei2 is a substrate of Pat1 kinase and that dephosphorylation of Mei2 is sufficient to switch cells from the mitotic cell cycle into meiosis"]

- **14-3-3 (Rad24) binds phospho-Mei2 and blocks RNA binding / dot formation**
  [PMID:11818066 "S. pombe Rad24p, a 14-3-3 protein, functions as a negative factor for meiosis by antagonizing the function of meiRNA to promote the formation of a nuclear Mei2p dot. Rad24p binds preferentially to Mei2p phosphorylated by Pat1 kinase"]
  [PMID:10788621 "Rad24 protein directly associates with Mei2 protein by recognizing Ser-438 which is a phosphorylation target of Pat1 kinase"]

- **TORC1/Tor2 represses Mei2; TORC1 + Pat1 drive ubiquitin-proteasomal degradation**
  [PMID:17046992 "Tor2 ... appears to operate by interfering with the functions of the transcription factor Ste11 and the meiosis-promoting RNA-binding protein Mei2"]
  [PMID:24741065 "fission yeast TORC1 ... can phosphorylate Mei2 ... Mei2 is polyubiquitylated in vivo in a TORC1-dependent manner"]
  Tor2-Mei2-Ste11 complex reported (GO:0034064) from PMID:17046992.

- **Mip1 (WD-repeat protein) facilitates Mei2 function**
  [PMID:10648609 "Mip1p was bound to Mei2p in vivo ... wild-type Mip1p was required for the function of Mei2p to induce meiosis"]

- **mamRNA scaffolds mutual Mmi1–Mei2 inhibition**
  [PMID:33536434 "this regulatory RNA, termed mamRNA, scaffolds the antagonistic RNA-binding proteins Mmi1 and Mei2 to ensure their reciprocal inhibition ... mamRNA allows Mmi1 to target Mei2 for ubiquitin-mediated downregulation, and conversely enables accumulating Mei2 to impede Mmi1 activity"]

- **Stress-responsive MAPK pathway reinforces meiotic commitment via Mei2 feedback**
  [PMID:22144909 "a feedback loop stemming from activated Mei2 to Win1 and Wis4 MAPKKKs operates in this pathway and eventually enhances CTD Ser-2 phosphorylation and ste11 transcription"]

## Cytosolic / zygotic development functions (newer)

- **Cytosolic Mei2 arrests mitotic growth and initiates development; P-body component**
  [PMID:41298081 "using compartment-restricted alleles, we report that Mei2 functions in the cytosol to arrest mitotic growth and initiate development. We found that Mei2 is a zygote-specific component of P-bodies that inhibits the translation of tethered mRNAs"]
  [PMID:41298081 "Mei2 recruitment to P-bodies and its cytosolic functions, including translational repression of tethered RNAs, depend on the RNA-binding domain of Mei2"]

- **Block to re-fertilization / negative regulation of conjugation with zygote**
  [PMID:30089908 "Gamete fusion triggers bipartite transcription factor assembly to block re-fertilization ... The signalling cascade to block re-fertilization shares components with, but bifurcates from, meiotic induction"]
  Note: GOA assigns GO:0140538 (negative regulation of conjugation with zygote) to mei2 via this paper (IMP); zygotic meiotic induction shares components with the re-fertilization block.

## Localization summary
- Cytoplasm/cytosol in proliferating/vegetative cells [PMID:9062192; PMID:10648609; PMID:16823372 (HDA proteome localization)].
- Nucleus + Mei2 dot during meiotic prophase [PMID:9062192; PMID:12808043; PMID:9778252].
- Nuclear chromosome association (at sme2 locus) [PMID:12808043].
- P-body in zygotes [PMID:41298081].

## Domain / structure
- 750 aa; RRM1 (195–270), RRM2 (293–361) per UniProt; RRM3 (C-terminal, ~580–733) is the meiRNA-binding domain.
  [PMID:35512546 "the removal of Mei2 RRM3 inactivated its function completely. A Mei2 derivative consisting of residues 429–733, containing only the Mei2 RRM3, was the shortest construct to be functional in vivo"]
- PDB structures of RRM3: 6YYL, 6YYM, 7DUS, 7EIO, 7EIU.

## Annotation review decisions (summary)
- RNA binding (GO:0003723) and lncRNA binding (GO:0106222), poly(U) RNA binding (GO:0008266): core MF — ACCEPT.
- GO:0003676 nucleic acid binding (IEA): general parent of RNA binding — MARK_AS_OVER_ANNOTATED / accept as non-core (RNA binding is the specific term).
- protein binding (GO:0005515): bare term — MODIFY/over-annotated; keep specific interactions documented but the generic MF is uninformative. Where a more specific MF exists (protein sequestering of Mmi1) use that.
- protein sequestering activity (GO:0140311): core — ACCEPT (sequesters Mmi1).
- Cellular components: nucleus, cytoplasm, cytosol, Mei2 nuclear dot complex, nuclear chromosome, P-body, Tor2-Mei2-Ste11 complex — all experimentally supported; dot/nucleus/cytosol core; complexes accept.
- BP: cell cycle switching mitotic-to-meiotic (GO:0051728), positive regulation of meiotic cell cycle (GO:0051446): core — ACCEPT.
- negative regulation of cytoplasmic translation (GO:2000766), regulation of RNA export from nucleus (GO:0046831): newer cytosolic/zygotic functions from PMID:41298081 — ACCEPT.
- negative regulation of conjugation with zygote (GO:0140538): block to re-fertilization — KEEP_AS_NON_CORE (peripheral relative to the core meiosis-switch role).
