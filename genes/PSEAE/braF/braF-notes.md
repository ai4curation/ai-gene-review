# braF (PA1071, P21629) notes

## Identity

- UniProt P21629 (Swiss-Prot, PE 3), 255 aa, gene braF, locus PA1071,
  P. aeruginosa PAO1. Fetched accession matches the worklist entry (rank 13).
- ABC transporter nucleotide-binding domain (PF00005) plus the C-terminal
  BCA_ABC_TP_C extension (PF12399) typical of LivG; CDD cd03219
  ABC_Mj1267_LivG_branched; PANTHER PTHR45772:SF11 (LIVG subfamily).
  Walker A ATP-binding site 38..45 (PROSITE ProRule).
- One of two ATPase subunits (BraF, BraG) of the LIV-I high-affinity
  branched-chain amino acid ABC importer encoded by the braC-braD-braE-braF-braG
  operon (PA1074-PA1070). BraC is the periplasmic binding protein, BraD/BraE
  the permeases. TCDB 3.A.1.4.8 (HAAT family).

## Literature

- Hoshino 1979: LIV-I is the Na+-independent, shock-sensitive system that
  carries Leu/Ile/Val and also Ala/Thr
  [PMID:113383 "The former system seemed to serve not only for the entry of leucine, isoleucine, and valine, but also for that of alanine and threonine, although less effectively."].
- Hoshino & Kageyama 1980: the periplasmic binding protein (later BraC/LIVAT-BP)
  [PMID:6767701 "The protein also bound alanine and threonine with lower affinity."].
  No phenylalanine binding was reported for the P. aeruginosa protein.
- Hoshino & Kose 1990a: cloning; braF and braG encode ATP-binding proteins
  found in the cell membrane
  [PMID:2120183 "both containing amino acid sequences typical of proteins with ATP-binding sites"]
  [PMID:2120183 "These proteins were found among cell membrane proteins"].
- Hoshino & Kose 1990b: complementation of azaleucine-resistant LIV-I mutants
  [PMID:2120184 "confirming that the braD, braE, braF, and braG genes are required for the LIV-I transport system"].
- Hoshino et al. 1992: reconstitution of BraDEFG with BraC in proteoliposomes
  [PMID:1400443 "In this reconstituted system, leucine transport was completely dependent on the presence of all five Bra components and on ATP loaded internally to the proteoliposomes."]
  [PMID:1400443 "Alanine and threonine in addition to branched-chain amino acids were transported by the proteoliposomes, reflecting the substrate specificity of the BraC protein."]
  [PMID:1400443 "indicating that the LIV-I transport system has an ATPase activity coupled to translocation of branched-chain amino acids across the membrane"].
  This is the direct evidence that BraF is part of an ATP-driven importer of
  Leu/Ile/Val/Ala/Thr.
- Johnson et al. 2008 (PMID:18833300, full text): Biolog phenotype-microarray
  screen of 78 PathoGenesis Mini-Tn5 transporter mutants (most in strain PAK,
  PA1071 included), confirmed by growth on minimal plates. For PA1071: reduced
  (+/-) growth on D-Ala (C), L-Ala (C), L-Ile (C), L-Val (N) and
  delta-aminovalerate (C) (Table 2). Text:
  [PMID:18833300 "In this work, mutants for each of these genes were found to be defective in Alanine metabolism, while utilization of L-Valine and L-Isoleucine was also altered in some cases"].
  These are growth phenotypes, not uptake assays; the insertions are in an
  operon and may be polar on braG.

## Interpretation

- Leu/Ile/Val/Ala/Thr import by the BraCDEFG complex is directly established
  (reconstitution). The PseudoCAP L-Ile, L-Val and L-Ala IMP rows from the
  growth screen are indirect on their own, but they agree with that biochemistry,
  so the claims are sound.
- D-alanine: all bra mutants and the paralogous PA4910/PA4912 mutants grow less
  well on D-Ala in the screen, but no D-Ala uptake or binding has been measured
  for LIV-I or BraC. Plausible, not established.
- Phenylalanine (IBA from E. coli LivG, P0A9S7): E. coli has two binding
  proteins feeding LivHMGF (LivJ and the leucine-specific LivK), and the E. coli
  Phe annotation comes from that system. I have not checked a cached paper for
  which binding protein carries Phe. P. aeruginosa has the single BraC (LIVAT)
  binding protein, and none of the P. aeruginosa LIV-I or BraC specificity
  studies (PMID:113383, PMID:6767701, PMID:1400443) lists Phe as a substrate.
  Over-annotation for P. aeruginosa.
- Leucine, the best-characterised LIV-I substrate, is missing from braF's
  process annotations; added as NEW (IDA, PMID:1400443).

## PseudoCAP IBA-seed assessment

PTN000656921 is the LivG ATPase node. Its 25 leaves (15 taxa) include
E. coli/Salmonella/Yersinia LivG, P. aeruginosa BraF and its paralog PA4910,
seven Bradyrhizobium japonicum HAAT ATPases, three Geobacter, two Deinococcus,
and Thermotoga, Chloroflexus, Streptomyces, Fusobacterium and Streptococcus
members. The same node already carries E. coli-seeded (P0A9S7) IBDs for
L-valine, L-isoleucine and L-phenylalanine transmembrane transporter activity.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN000656921 | GO:1903805 L-valine import across plasma membrane | 1 (sole) | 25 (15 taxa) | GO:1903805, IMP, PMID:18833300 (PseudoCAP) | SOUND | The screen shows only a partial N-source growth defect on L-Val, which on its own is an indirect phenotype. But LIV-I Val transport is established biochemically (PMID:113383, PMID:1400443), and the term matches the E. coli-seeded L-valine transporter activity IBD on the same node. Clade caveat: substrate specificity is set by each system's binding protein, and the node includes several paralogous HAAT ATPases per genome (7 in B. japonicum) whose substrates are unknown. This is the same caveat that applies to the existing MF IBDs. |
| PTN000656921 | GO:1903806 L-isoleucine import across plasma membrane | 1 (sole) | 25 (15 taxa) | GO:1903806, IMP, PMID:18833300 (PseudoCAP) | SOUND | Reduced growth on L-Ile as a C source, corroborated by the LIV-I reconstitution and binding data. It matches the E. coli-seeded L-isoleucine transporter activity IBD. The same clade caveat applies as for valine. |
| PTN000656921 | GO:0015808 L-alanine transport | 1 (sole) | 25 (15 taxa) | GO:0015808, IMP, PMID:18833300 (PseudoCAP) | SOUND | The claim is correct for P. aeruginosa LIV-I, which transports Ala in proteoliposomes (PMID:1400443). Ala is a secondary LIV-I substrate, though, and none of the E. coli seeds supports it. Propagating it to the whole LivG clade, including uncharacterised paralogs, is a stretch. GO:1904273 L-alanine import across plasma membrane is the more precise term. |
| PTN000656921 | GO:0042941 D-alanine transmembrane transport | 2 (PA1071, PA4910) | 25 (15 taxa) | GO:0042941, IMP, PMID:18833300 (PseudoCAP) | INDIRECT-PHENOTYPE | Both seeds rest on partial growth defects on D-Ala in the same Biolog screen. No D-Ala uptake or binding has been shown for LIV-I or BraC. D-Ala transport is plausible but not established, and the node propagates it to 25 proteins. |

The PseudoCAP rows are not wrong enough to file as defects: the L-Ile, L-Val
and L-Ala claims are true of the bra system. The D-Ala rows are recorded as
UNDECIDED, with a suggested question, rather than as a defect.

## Decisions summary

- ACCEPT: plasma membrane (IBA, IEA), ATP binding, ATP hydrolysis activity,
  L-valine and L-isoleucine transporter activity (IBA), L-valine import (IBA, IMP),
  L-isoleucine import (IBA, IMP).
- MODIFY: L-alanine transport (IBA, IMP) -> L-alanine import across plasma
  membrane; isoleucine transmembrane transport (ARBA IEA) -> L-isoleucine import
  across plasma membrane; L-valine transmembrane transport (ARBA IEA) -> L-valine
  import across plasma membrane.
- MARK_AS_OVER_ANNOTATED: L-phenylalanine transmembrane transporter activity
  (IBA), phenylalanine transport (IEA).
- UNDECIDED: D-alanine transmembrane transport (IBA, IMP).
- NEW: L-leucine import across plasma membrane (IDA, PMID:1400443).
