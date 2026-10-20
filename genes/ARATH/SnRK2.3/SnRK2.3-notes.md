# SnRK2.3 (SRK2I, At5g66880, UniProt Q39193) curation notes

## 2026-10-19 Session 1: new review

### Setup and sources

- Folder created with `just fetch-gene ... --alias SnRK2.3`; UniProt names the gene SRK2I.
  The review uses gene_symbol `SnRK2.3` to match the folder, following the
  `genes/ARATH/OST1` precedent (UniProt SRK2E, gene_symbol OST1).
- No deep-research provider is available in this environment; this journal records my own
  literature reading of the cached publications (`just fetch-gene-pmids ARATH SnRK2.3`)
  plus PubMed searches (esearch for "SRK2I", "SnRK2.3 phosphorylation", the 2009 triple
  mutant paper). Additional PMIDs cached: 19420218, 19541597, 22160701, 30962512,
  29659577, 28787436, 26943172.
- Abstract-only in cache: 19805022, 19880399, 10634783, 15292193, 21166475, 19420218,
  19541597, 22160701, 30962512. Full text: 17307925, 19924127, 23290725, 19874541,
  18941053 (introduction and discussion only), 21220313 (discussion), 28438792,
  28887381, 29659577, 28787436, 26943172.

### Identity and family

- 361 aa subclass III SnRK2 (SNF1-related protein kinase 2) with a protein kinase domain
  (22-278), ATP-binding loop 28-36, Lys51 and catalytic Asp141 (UniProt features, PROSITE
  PRU00159). PANTHER PTHR24343:SF566. Crystal structure of full-length SnRK2.3 (PDB 3UC3)
  [PMID:22160701 "we report the crystal structures of full-length Arabidopsis thaliana
  SnRK2.3 and SnRK2.6 at 1.9- and 2.3-Å resolution, respectively"].
- Closest paralogs: SnRK2.2/SRK2D (At3g50500) and SnRK2.6/OST1/SRK2E (At4g33950).

### Activity and activation

- ABA- and osmotic-stress activated kinase [PMID:15292193 "Nine of the 10 SnRK2 were
  activated by hyperosmolarity induced by mannitol, as well as NaCl, indicating an
  important role of the SnRK2 family in osmotic signaling"; "abscisic acid only activated
  five of the nine SnRK2"].
- In-gel kinase assays with ABF2, ABI5 and ABF1 fragments: the 42-kD ABA-induced activity
  is from SnRK2.2/2.3 [PMID:17307925 "these data demonstrate that SnRK2.2 and SnRK2.3 have
  ABA-inducible kinase activity and together are likely to play a major role in
  phosphorylating and activating ABF2, ABI5, ABF1, and possibly other ABFs"].
- Two-step autoactivation: PP2C release, then activation-loop autophosphorylation
  [PMID:22160701 "This stabilization enables SnRK2s to gain full activity by activation
  loop autophosphorylation"; "Autophosphorylation is more efficient in SnRK2.6, which has
  higher stability than SnRK2.3"]. UniProt: "Autophosphorylated in vitro" (ECO:0000269,
  PubMed:22160701).
- Substrates beyond ABFs: AKS bHLH factors [PMID:28438792 "Three ABA-responsive SnRK2s
  (SnRK2.2/SRK2D, SnRK2.3/SRK2I, and SnRK2.6/SRK2E/OST1) phosphorylated AKS1 in vitro"];
  HAT1 HD-ZIP [PMID:29659577 "both protein stability and binding activity of HAT1 was
  repressed by SnRK2.3 phosphorylation"]; FREE1 [PMID:30962512 "Following ABA treatment,
  SNF1-related protein kinase 2 (SnRK2) kinases phosphorylate FREE1, a step requisite for
  ABA-induced FREE1 nuclear import"].

### Negative regulators

- Clade A PP2Cs (ABI1, ABI2, HAB1, AHG1) bind and dephosphorylate it [PMID:19805022 "Group
  A PP2Cs interacted physically with SnRK2s in various combinations, and efficiently
  inactivated ABA-activated SnRK2s via dephosphorylation of multiple Ser/Thr residues in
  the activation loop"]; ABI1 in planta [PMID:19874541 "ABI1 interacts with the
  ABA-signalling kinases OST1, SnRK2.2 and SnRK2.3 in plants"]. Y2H with ABI1/ABI2/HAB1
  [PMID:19924127 "The three clade A PP2Cs (ABI1, ABI2 and HAB1) were each capable of
  interacting with the three SnRK2 kinases (SnRK2.2, SnRK2.3 and SnRK2.6) in yeast
  two-hybrid (Y2H) assays"]. HDX of SnRK2.3-HAB1 (PMID:23290725).
- TOPP1/AtI-2 [PMID:26943172 "TOPP1 and AtI-2 negatively regulated the SnRK2.2/3/6-mediated
  activation of the ABA responsive reporter gene RD29B"].
- SCF(AtPP2-B11) targets SnRK2.3 for proteasomal degradation [PMID:28787436 "AtPP2-B11
  specifically degrades SnRK2.3 to attenuate ABA signaling"].
- All of these regulate SnRK2.3; binding of a PP2C is the target side of the interaction,
  so bare protein binding rows are removed and I do not propose protein phosphatase
  binding as a SnRK2.3 molecular function (consistent with the OST1 review).

### Localization

- Nucleus and cytoplasm (IDA, PMID:19880399) [PMID:19880399 "SRK2D/E/I and AREB1
  co-localize and interact in nuclei in planta"]; in seeds mainly nuclear [PMID:19541597
  "These SnRK2 proteins were mainly expressed in the nucleus during seed development and
  germination"]; BiFC with ABI1 in nucleus and cytosol [PMID:19924127 "ABI1 interacts with
  the SnRK2s in the nucleus as well as the cytosol"].
- NOT cytosol (RCA, PMID:21166475) is an inference from absence in a cell-suspension
  cytosolic proteome; contradicted by the BiFC and IDA data. Remove (as OST1).
- Plastid (HDA, PMID:28887381): membrane-fraction correlation profiling; the cached text
  does not mention SnRK2.3 and no other evidence places it in plastids. Over-annotation
  (same as the other ARATH reviews citing this dataset for plastid).

### Physiology

- snrk2.2 snrk2.3 double mutant: ABA-insensitive germination, root growth, dormancy, Pro
  accumulation and ABRE gene expression [PMID:17307925 "snrk2.2 snrk2.3 plants are
  insensitive to ABA in seed germination, indicating that SnRK2.2 and SnRK2.3 are the
  protein kinases that positively regulate ABA signaling in seed germination"]; only minor
  stomatal role [PMID:17307925 "SnRK2.2 and SnRK2.3 have only minor roles in stomatal
  control and further distinguished their function from that of SnRK2.6"].
- snrk2.2/2.3/2.6 triple mutant nearly ABA-blind [PMID:19420218 "In-gel kinase assays showed
  that all ABA-activated protein kinase activities are eliminated in the triple mutant"];
  drought-sensitive [PMID:19880399 "srk2d srk2e srk2i (srk2d/e/i) triple mutants exhibit
  greatly reduced tolerance to drought stress and highly enhanced insensitivity to ABA"];
  seed development and dormancy (PMID:19541597).
- Osmotic stress (decuple mutant) [PMID:21220313 "These results demonstrate critical
  functions of the SnRK2s in mediating osmotic stress signaling and tolerance"].
- GA/germination IGI from Piskurewicz 2008 (PMID:18941053, with SnRK2.2): cached text
  lacks the Results; abstract says "The endogenous ABI5 phosphorylation and inhibition of
  germination could be recapitulated by the addition of a SnRK2 protein kinase to the ABI5
  overexpression line." Kept the GA row as non-core (deferring to the curator).

### TAS rows from PMID:10634783

- Li et al. 2000 cloned Vicia faba AAPK, an OST1-like SnRK2 [PMID:10634783 "encoding a
  guard cell-specific ABA-activated serine-threonine protein kinase (AAPK)"]. The paper is
  not about SnRK2.3 itself, but the asserted claims (protein kinase activity; ABA
  signaling) are correct for SnRK2.3 and are independently supported by PMID:17307925.
  Accept; worth flagging to TAIR that an SnRK2.3-specific reference would be better.

### Decisions summary

- MF: Ser/Thr protein kinase activity is core (IBA/IEA accept; IDA 'kinase activity' to
  MODIFY -> GO:0004674). ATP binding accept (as OST1). Protein binding: all REMOVE.
- BP: ABA-activated signaling pathway, response to ABA, response to water deprivation,
  response to osmotic stress accepted; salt non-core (as OST1); regulation of seed
  germination MODIFY -> negative regulation of seed germination (GO:0010187), since
  SnRK2.2/2.3 mediate ABA inhibition of germination.
- NEW: protein autophosphorylation (GO:0046777), PMID:22160701 + UniProt PTM; matches
  OST1 accepted IDA row.

## 2026-10-20: ported fixes from the parallel review branch

- Core function 1 now names FREE1 phosphorylation (curated UniProt line, PMID:30962512) and TOPP1/AtI-2 negative regulation [PMID:26943172 "TOPP1 and AtI-2 negatively regulated the SnRK2.2/3/6-mediated activation of the ABA responsive reporter gene RD29B"].
- The eight GO:0005515 rows with clade A PP2C partners changed from REMOVE to MODIFY to GO:0019903, as for SnRK2.2 and matching the OST1 GO:0019903 IPI row. The bHLH122 row stays REMOVE.
- GO:0009737 rows: reason explains why the term is kept alongside GO:0009738.
- Source defect recorded on the NOT located_in cytosol RCA row (PMID:21166475): contradicted by BiFC and IDA cytoplasm evidence.
