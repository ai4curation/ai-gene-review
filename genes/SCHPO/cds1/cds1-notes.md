# cds1 (S. pombe) — gene review notes

UniProt: Q09170 (RAD53_SCHPO). Gene: cds1 / SPCC18B5.11c. 460 aa Ser/Thr kinase, EC 2.7.11.1.
Ortholog of human CHK2 and budding-yeast Rad53 (CHEK2 subfamily). Domain architecture:
N-terminal FHA domain (res ~60-116) + C-terminal protein kinase domain (res ~167-433);
SQ/TQ regulatory motif near the N-terminus (T11Q12). Active-site proton acceptor Asp294.

## Core identity / function

Cds1 is the **effector Ser/Thr protein kinase of the DNA replication (intra-S) checkpoint**
in fission yeast. It is the major effector of the replication checkpoint, activated
specifically in S phase when replication forks stall (e.g. hydroxyurea/HU, nucleotide
depletion, or replication encountering DNA damage). It is distinct from Chk1, the G2 DNA-damage
checkpoint effector kinase.

- Original discovery as a multicopy suppressor of a DNA pol-alpha ts mutant; "checking DNA synthesis";
  blocks mitosis in S phase: [PMID:7723827 "This gene, named cds1+ (checking DNA synthesis), encodes a typical protein kinase. Here we report that this protein kinase is a key component of the DNA replication-monitoring S/G2 checkpoint system."]
- Cds1 enforces the S-M checkpoint coupling mitosis to completion of S phase, and controls
  replicational stress tolerance: [PMID:11313465 "Cds1 enforces the S-M checkpoint that couples mitosis (M) to the completion of DNA synthesis (S). Cds1 also controls replicational stress tolerance mechanisms."]
- Major effector of replication checkpoint: [PMID:16618806 "In Schizosaccharomyces pombe the major effector of the replication checkpoint is the protein kinase Cds1."]
- Ortholog of Chk2: [PMID:19357077 "Cds1 is the ortholog of Chk2 and the major effector of the DNA replication checkpoint in Schizosaccharomyces pombe."]

## Activation mechanism (MF = protein Ser/Thr kinase; activation regulation)

Two-stage activation: priming by Rad3(ATR) via mediator Mrc1, then FHA-dependent dimerization
and autophosphorylation.
- T11 phosphorylated by Rad3/ATM required for activation: [PMID:11313465 "Substitution of threonine-11 with alanine (T11A) abolished Cds1 activation that occurs when DNA replication is inhibited by hydroxyurea (HU) treatment... Cds1(T11A) was unable to enforce the S-M checkpoint."]
- Mrc1 recruits Cds1 via FHA-phospho-Mrc1, then dimerization/autophosphorylation: [PMID:16618806 "In the first stage, Mrc1 recruits Cds1 to stalled replication forks by interactions between the FHA domain of Cds1 and specific phosphorylated Rad3 consensus sites in Mrc1. Cds1 is then primed for activation by Rad3-dependent phosphorylation. In the second stage, primed Cds1 molecules dimerize via phospho-specific interactions mediated by the FHA domains and are activated by autophosphorylation."]
- Autoactivation requires autophosphorylation of activation-loop Thr328; C-terminal tail autoinhibits: [PMID:19357077 "phosphorylation of a highly conserved threonine residue (Thr(328)) in the activation loop is the only covalent modification required for kinase activation in vitro and in vivo. Autophosphorylation of Thr(328) and kinase activation in unprimed, monomeric Cds1 are strongly inhibited by the C-terminal 27-amino acid tail of the enzyme."]
- Interacts with Rad26 (Rad3 partner); autophosphorylated (UniProt; PMID:9450932, PMID:18257517).

## Direct substrates / downstream targets

- **Cdc25** phosphatase — Cds1 (or Chk1) phosphorylates Cdc25 on S99/S192/S359, creating 14-3-3 binding sites, keeping Cdc2 inhibited: [PMID:9774107 "We show by mutagenesis that Chk1 functions redundantly with the kinase Cds1 at the replication checkpoint and that both kinases phosphorylate Cdc25 on the same sites, which include serine residues at positions 99, 192 and 359. Mutation of these residues reduces binding of 14-3-3 proteins to Cdc25 in vitro and disrupts the replication checkpoint in vivo."]
- **Hsk1** (Cdc7 ortholog) — Cds1-dependent phosphorylation in vivo and direct substrate in vitro: [PMID:11027263 "We demonstrate that Hsk1p undergoes Cds1p-dependent phosphorylation in response to HU and that it is a direct substrate of purified Cds1p kinase in vitro."]
- **Dna2** — Cds1 phosphorylates Dna2-S220 to prevent stalled fork reversal: [PMID:22682245 "the Cds1(Chk2) effector kinase targets Dna2 on S220 to regulate, both in vivo and in vitro, Dna2 association with stalled replication forks in chromatin. We demonstrate that Dna2-S220 phosphorylation and the nuclease activity of Dna2 are required to prevent fork reversal."]
- **Nrm1** (MBF repressor) — Cds1 phosphorylates Nrm1, relieving MBF repression to drive G1-S transcription of replication/repair genes: [PMID:18682565 "Phosphorylation of Nrm1 by the Cds1 (Chk2) checkpoint protein kinase, which is activated in response to DNA replication stress, promotes its dissociation from the MBF transcription factor. This leads to the expression of genes encoding components that function in DNA replication and repair pathways important for cell survival in response to arrested DNA replication."] (This is the PMID:18682565 IPI "protein binding" annotation partner = Nrm1/O42913; also the IntAct nrm1 interaction.)
- **Mcm4** — binds Cds1 and is Cds1-dependently phosphorylated upon checkpoint activation: [PMID:18180284 "In cells where the checkpoint is activated, Mcm4 binds the Cds1 kinase and undergoes Cds1-dependent phosphorylation."] (PMID:18180284 IPI partner SPCC16A11.17 = mcm4/cdc21.)
- **Rgf1** (Rho1 GEF) — Cds1- and Rad24-dependent nuclear accumulation under chronic replication stress: [PMID:24478458 "Rgf1p nuclear accumulation during replication arrest depends on the 14-3-3 chaperone Rad24p and the DNA replication checkpoint kinase Cds1p... A mutant, Rgf1p-9A, that substitutes nine serine potential phosphorylation Cds1p sites for alanine fails to accumulate in the nucleus in response to replication stress."]
- Downstream Mus81 / Rqh1 / Rhp51 pathway for S-phase damage slowing: [PMID:19037101 "We have identified proteins downstream of Cds1 required for checkpoint-dependant slowing, including the structure-specific endonuclease Mus81 and the helicase Rqh1."]
- UniProt also lists Rad60 as a Cds1 phosphorylation target (PMID:12897162).

## Biological processes

- **Mitotic DNA replication checkpoint signaling** (GO:0033314): [PMID:11313465] (S-M checkpoint).
- **Mitotic intra-S DNA damage checkpoint signaling** (GO:0031573): replication slowing on damage:
  [PMID:19037101 "Cds1, the S-phase-specific checkpoint effector kinase, is required for checkpoint signaling and replication slowing; upon treatment with the alkylating agent methyl methane sulfonate, cds1Delta mutants display a complete checkpoint defect."]
  [PMID:12032307 "The slowing of S phase depends strongly on the six checkpoint-Rad proteins, on Cds1, and on Rad4/Cut5..."]
  Original IGI (with hus1/SPAC3H5.06c) blocking mitosis in S: [PMID:7723827].
- **Meiotic G2/MI DNA replication checkpoint signaling** (GO:0033315): Cds1 absolutely required, plays a more prominent role than in mitosis: [PMID:10521402 "The mitotic checkpoint Rad genes and the Cds1 protein kinase are required for the DNA replication checkpoint during meiosis, with Cds1 playing a more prominent role than it does during mitosis."]
  Downstream Mei4 regulation of nuclear movements: [PMID:25492408 "this prolongation was caused by the Cds1-dependent replication checkpoint, which represses expression of the mei4(+) gene encoding a meiosis-specific transcription factor."]
- **Fork stabilization / protection** — preventing fork reversal via Dna2: [PMID:22682245]. NOTE: the
  precise GO term "replication fork protection" (GO:0048478) is OBSOLETE; GO:0031297 (replication
  fork processing) is the recommended live term.

## Localization

- IDA nucleus: [PMID:24478943 - Cds1 chromatin recruitment/activity, nuclear]. Also HDA global
  localization (nucleus, cytosol, cell division site) from ORFeome study [PMID:16823372] - large-scale
  GFP localization, lower confidence for site-of-action.
- IBA nucleus + cytoplasm from GO_Central.

## NOT in GOA review list but in UniProt DR
- GO:0051598 meiotic recombination checkpoint signaling (IBA) — present in uniprot but not in goa.tsv list.
- Mek1 (PMID:21084840) is a Cds1/Rad53-related kinase that is itself studied; the PomBase IDA assigns
  protein Ser/Thr kinase activity to cds1 from this paper's context — kinase activity is well-supported regardless.

## Curation conclusions
- Core MF: protein serine/threonine kinase activity (GO:0004674), ATP binding (GO:0005524).
- Core BP: mitotic DNA replication checkpoint signaling (GO:0033314), mitotic intra-S DNA damage
  checkpoint signaling (GO:0031573); meiotic counterpart GO:0033315 (core in meiosis).
- "protein binding" (GO:0005515) IPI annotations are uninformative per curation guidance; partners are
  substrates (Nrm1, Mcm4) so MARK_AS_OVER_ANNOTATED / not core.
- "mitotic DNA damage checkpoint signaling" (GO:0044773, IBA) is imprecise for Cds1, whose role is the
  intra-S / replication checkpoint, not the G2 DNA-damage checkpoint (that is Chk1). MODIFY to intra-S.
- HDA cytosol / cell division site likely reflect bulk localization, not site of action — non-core.
