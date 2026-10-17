# MBP1 (P39678, YDL056W) — working notes

Journal-style notes for the GO annotation review of *Saccharomyces cerevisiae* MBP1.
Inline citations are `[PMID:NNN "verbatim text"]` where the publication is cached in
`publications/`; uncached papers are cited by PubMed-verified PMID with a paraphrase
(no quotation marks) and are flagged `(not cached)`.

## 2026-09-26 — identity and inputs

- UniProt P39678, Transcription factor MBP1, "MBF subunit p120", 833 aa. Domain 5-111 is the
  APSES/KilA-N HTH DNA-binding domain (IPR018004/IPR036887); central ankyrin repeats
  (IPR002110); UniProt subunit note: MBF = Swi6 + Mbp1; interacts with Msa1 (PMID:18160399,
  not cached). Phosphosites recorded at 110, 325, 326, 330, 827.
- GOA seed: 24 rows (7 IBA, 4 IEA, 4 IPI protein binding with Swi6, 1 HDA nucleus, 1 HDA
  sequence-specific DNA binding, IMP/NAS/IDA rows all from Koch 1993, and one IMP
  "maintenance of translational fidelity" from PMID:30465652).
- Deep research (falcon) is consistent with the textbook picture and adds three points
  worth keeping: (i) Mbp1 nuclear localization is constitutive, with two redundant basic
  NLSs imported by Srp1-Kap95 (PMID:20587033, not cached); (ii) nuclear Mbp1 copy number
  scales with nuclear volume in G1 at roughly constant concentration, 79-248 molecules in
  glucose (PMID:29792825, not cached); (iii) WHI7 is a direct MBF/SBF target with an MCB at
  -217 (PMID:39285615, not cached).
- Cross-checked the paralog review `genes/yeast/SWI4/SWI4-ai-review.yaml` (COMPLETE) so the
  grading of shared IBA, IEA and protein-binding rows is consistent.

## Core biology (with provenance)

- Discovery: MBF (also DSC1) was purified from yeast as Swi6 plus a 120 kDa protein and the
  p120 gene cloned as MBP1
  [PMID:8372350 "MBF contains Swi6 and a 120-kilodalton protein (p120). MBF was purified and
  the gene encoding p120 (termed MBP1) was cloned."]. The complex binds MCB elements
  [PMID:8372350 "A different, but related, complex called MBF binds to MCB elements (Mlu I
  cell cycle box) found in the promoter of most DNA synthesis genes."].
- Mbp1 is the DNA-binding subunit; Swi6 is the shared regulatory/activation subunit of both
  MBF and SBF [PMID:10409718 "Mbp1 and Swi4 are the DNA binding subunits for MBF and SBF,
  while the common subunit, Swi6, is presumed to play a regulatory role in both complexes."]
  [PMID:10490612 "Swi4 and Mbp1 are the DNA binding components of SBF and MBF,
  respectively."]. The N-terminal ~124 residues suffice for DNA binding and the 1.71 A
  crystal structure of the domain shows an HTH-related fold with a six-stranded beta-sheet
  (PMID:9083114, not cached) [PMID:10490612 "crystallographic studies of the Mbp1 DNA
  binding domain have revealed a helix-turn-helix structure"].
- MCB consensus ACGCGTNA; MBF targets include the S-phase cyclins CLB5/CLB6, SWI4 and
  DNA-synthesis genes such as CDC9, POL1 and RNR1 [PMID:10409718 "the consensus is
  ACGCGTNA"] [PMID:10409718 "activates G 1 -specific transcription of the S-phase cyclin
  genes CLB5 and CLB6 , the SWI4 gene, and many genes needed for DNA synthesis such as CDC9
  and POL1"] [PMID:10409718 "RNR1 is controlled through MCB elements that are dependent on
  MBF (Mbp1/Swi6)"].
- Loss-of-function: mbp1 null deregulates DNA-synthesis genes; mbp1 swi4 is lethal
  [PMID:8372350 "A deletion of MBP1 was not lethal but led to deregulated expression of DNA
  synthesis genes, indicating a direct regulatory role for MBF in MCB-driven transcription."]
  [PMID:8372350 "Strains deleted for both MBP1 and SWI4 were inviable, demonstrating that
  transcriptional activation by MBF and SBF has an important role in the transition from G1
  to S phase."] [PMID:10409718 "However, cells lacking both SWI4 and SWI6 or both SWI4 and
  MBP1 are not viable, arresting prior to DNA synthesis"]. Genome-wide, MBF and SBF have
  highly overlapping target sets and largely redundant roles (PMID:15965243, not cached;
  PMID:11206552 ChIP-chip of Mbp1 and Swi4, not cached).
- Corepressors differ between the two complexes: Whi5 binds SBF but not Mbp1/MBF
  [PMID:19745812 "In contrast, we saw no interaction between Whi5-Flag and the Mbp1-Myc
  subunit of MBF"]; MBF is switched off after G1 by the MBF-bound corepressor Nrm1, itself
  an MBF target (negative feedback; PMID:16916637, not cached). Under replication stress
  Rad53 phosphorylates Nrm1 and removes it from MBF-bound promoters, so MBF-specific genes
  stay on (PMID:18682565, PMID:22333915, PMID:22333912, all not cached). The deep research
  is explicit that these papers establish checkpoint control of the Mbp1-containing complex
  via Nrm1, not direct Rad53 phosphorylation of Mbp1.
- Localization: Mbp1 is nuclear throughout the cycle (HA-Mbp1 colocalizes with DAPI at all
  stages; two redundant NLSs; Srp1/Kap95 import; PMID:20587033, not cached), and the HDA
  proteome-localization screen also scores it nuclear
  [PMID:11914276 "By high-throughput immunolocalization of tagged gene products, we have
  determined the subcellular localization of 2744 yeast proteins."]. The nucleocytoplasmic
  cycling described for the family belongs to Swi6, not to the DNA-binding subunits
  [PMID:12697814 "Swi6p was nuclear during most of the cell cycle, aside from a period in the
  G 2 -M phase"] [PMID:12697814 "in mbp1 mutant cells, which contain SBF but no MBF,
  exportation of Swi6p to the cytoplasm in the G 2 -M phase is not affected"].
- Interactome rows: the Swi6 pair is recovered in TAP-MS (PMID:16429126), mChIP-MS
  [PMID:21179020 "mChIP-MS analyses of Swi4-TAP, Swi6-TAP and Mbp1-TAP successfully
  identified known interaction partners (such as Stb1) for both MBF and SBF"] and the 2023
  AE-MS interactome (PMID:37968396; Mbp1 is not discussed in the cached text). Note that
  Lambert et al. misdescribe MBF as Swi4-Mbp1 [PMID:21179020 "Two protein complexes
  essential for this process are the MBF and SBF transcription factors, composed of
  Swi4–Mbp1 and Swi4–Swi6, respectively"]; MBF is Mbp1-Swi6.

## The GO:1990145 "maintenance of translational fidelity" row (PMID:30465652)

- The cited eLife paper is about **Mbf1 = Multi-protein bridging factor 1 (MBF1, YOR298C-A,
  UniProt O14467)**, a ribosome-associated cro-like HTH protein, not Mbp1
  [PMID:30465652 "We demonstrated that mutations in the yeast gene MBF1, Multi-protein
  Bridging Factor 1, were responsible for the defects in reading frame maintenance in
  recessive high GFP mutants."] [PMID:30465652 "MBF1 is a highly conserved gene in eukaryotes
  and archaea, generally less than 160 amino acids with an N-terminal Mbf1-specific domain
  (that differs between archaea and eukaryotes) and a conserved cro-like helix-turn-helix
  (HTH) domain"].
- The full text is cached (`full_text_available: true`); grep for `MBP1`, `Mbp1p` and
  `YDL056W` returns zero hits, while `MBF1`/`Mbf1` occurs 549 times.
- QuickGO (queried 2026-09-26, GO:1990145, taxon 559292) lists MBF1 O14467 IDA
  PMID:30465652, RPS3 IMP and ASC1 IMP from the same paper, and then MBP1 P39678 IMP
  PMID:30465652 — i.e. the MBP1 row duplicates the MBF1 evidence under the confusable
  symbol. This is a demonstrable symbol mix-up from a fully read paper, so REMOVE is
  justified under the project rule (not a title/abstract-only second guess).

## Decisions summary

- ACCEPT: all G1/S, activator MF, cis-regulatory DNA binding, MBF complex, nucleus, DNA
  binding, sequence-specific DNA binding and positive-regulation rows (17 rows).
- MODIFY: GO:0005515 IPI rows from Koch 1993 and Lambert 2010 -> GO:0046982 protein
  heterodimerization activity (the Mbp1-Swi6 heterodimer), mirroring the SWI4 review;
  GO:0006355 NAS -> GO:0045944 (direction/polymerase-specific child already carried).
- REMOVE: two survey-derived protein-binding rows (uninformative, interaction not disputed);
  IBA `is_active_in cytoplasm` (Swi6-specific property propagated across the family node,
  as for SWI4); GO:1990145 (MBF1/MBP1 mix-up).
- No NEW terms proposed. Considered and rejected: a replication-checkpoint process term for
  Mbp1 — the checkpoint acts on Nrm1, and the comparator (Swi6, which shares the complex)
  does not carry one either; raised as a suggested question instead.

## PubMed-verified PMIDs for uncached papers (esummary, 2026-09-26)

- 9083114 Xu et al. 1997 Structure — Mbp1 DBD crystal structure.
- 20587033 Taberner & Igual 2010 BMC Cell Biol — Kap95 import of Mbp1/Swi6.
- 29792825 Dorsey et al. 2018 Cell Syst — G1/S TF copy number.
- 12832490 Costanzo et al. 2003 MCB — Stb1 differentially regulates SBF/MBF.
- 16916637 de Bruin et al. 2006 Mol Cell — Nrm1 corepressor.
- 18682565 de Bruin et al. 2008 PNAS — checkpoint inactivates Nrm1.
- 22333915 Travesa et al. 2012 EMBO J; 22333912 Bastos de Oliveira et al. 2012 EMBO J.
- 11206552 Iyer et al. 2001 Nature — SBF/MBF genomic binding sites.
- 15965243 Bean et al. 2005 Genetics — MBF/SBF functional overlap.
- 10747782 Taylor et al. 2000 Biochemistry — Mbp1/Swi4 DBDs.
- 18160399 Ashe et al. 2008 JBC — Msa1.
- 39285615 Ros-Carrero et al. 2024 Cell Cycle — WHI7 promoter.

## 2026-10-01 IBA alignment refresh

- Rebased from `origin/main` and reran `just fetch-gene yeast MBP1 --force`;
  the current 24-row GOA import matched the review.
- Fetched current PTHR43828 PAINT. All live MBP1 IBA rows still trace to the
  APSES G1/S transcription-regulator node `PTN000917496`: five accepted MBF
  molecular-function, complex and process rows, plus the cytoplasm row already
  marked as a bad Swi6-specific propagation. Added structured
  `propagation_review` blocks for the accepted IBA rows.
- Rechecked 2025-2026 web search results and did not find a newer direct
  *S. cerevisiae* MBP1 functional paper requiring changes.
