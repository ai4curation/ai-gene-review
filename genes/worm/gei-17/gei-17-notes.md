# gei-17 (C. elegans, UniProt Q94361) - curation notes

## Sources used

- `gei-17-uniprot.txt` (Swiss-Prot entry GEI17_CAEEL, 780 aa, six isoforms)
- `gei-17-deep-research-openscientist.md` (not edited; claims checked below)
- Cached primary papers (full text unless noted): PMID:15654100, PMID:16549501,
  PMID:19111656, PMID:22761594, PMID:25475837, PMID:25873636, PMID:27939944,
  PMID:24297748; abstract only: PMID:16701625, PMID:40316696.
- Fetched with `just fetch-pmid` during this review: PMID:34003111 (PIE-1 SUMOylation),
  PMID:34003109 (HDAC1 SUMOylation), PMID:31243051 (BUB-1/CLS-2 in meiosis),
  PMID:35666766 (tissue-specific SUMO inhibition, vulva), PMID:17908915 (SMK-1/PPH-4.1),
  PMID:40316696 (piRNA condensates; abstract only).

## Identity and domains

- PIAS family; sole PIAS/Siz-type E3 in the worm, co-ortholog of human PIAS1/PIAS2
  (PANTHER PTHR10782:SF94) and fly Su(var)2-10.
- PINIT domain aa 203-367; SP-RING zinc finger aa 400-485 with Zn(2+) ligands at
  431/433/454/457 [file:worm/gei-17/gei-17-uniprot.txt "L->A: Greatly reduces E3 ligase activity and"]
- C-terminal SIMs (aa 423-602 of isoform f) bind SUMO-modified proteins
  [PMID:27939944 "a fragment containing the two predicted high-affinity SIMs in GEI-17 (aa 423–602 in isoform f), pulled down higher molecular weight forms of both sumoylated GEI-17 and sumoylated KLP-19"]

## Molecular function: SUMO E3 ligase (strong, multiple IDA)

- MUS-101/TopBP1 SUMOylation in vitro [PMID:15654100 "The appearance of these bands was dependent on the presence of both GEI-17 and SUMO in the reaction mixture"]
- POLH-1 SUMOylation in vitro and in vivo [PMID:19111656 "These data demonstrate that recombinant GEI-17 stimulates SUMOylation of POLH-1 in vitro."]
  [PMID:19111656 "These data show that POLH-1 is SUMOylated in vivo, in a manner dependent on DNA damage and GEI-17."]
- AIR-2 SUMOylation, SUMO chain formation, SP-RING L417A mutant
  [PMID:25475837 "Moreover, the L/A mutation of the SP-RING within GEI-17 drastically diminishes its SUMO E3 activity."]
- KLP-19 SUMOylation, auto-SUMOylation [PMID:27939944 "Full-length, untagged KLP-19 is efficiently modified by SUMO in a GEI-17-dependent manner"]
- BUB-1 SUMOylation dose-dependent [PMID:31243051 "BUB-1 SUMO modification was increased by GEI-17 in a dose-dependent manner"]

## Biological roles

### DNA damage tolerance / TLS (core)
- GEI-17 SUMOylates POLH-1 at damaged chromatin and protects it from CRL4-Cdt2 degradation
  [PMID:19111656 "Based on these data, we conclude that the major function of GEI-17 during the early embryonic DNA damage response is to protect POLH-1 from the CRL4-Cdt2 pathway."]
- Suppression by cdt-2 co-depletion; GEI-17 is not needed for POLH-1 catalysis per se
  [PMID:19111656 "GEI-17 is not directly required for POLH-1 to performs its function"]
- Epistatic with polh-1;polk-1 [PMID:22761594 "Our results suggest that GEI-17 is implicated in TLS mediated by both POLH-1 and POLK-1."]
- Note: PMID:22761594 twice miscalls gei-17 a "SUMO protease"; this is a slip in that paper.

### Checkpoint silencing in embryos (indirect consequence)
- [PMID:16549501 "This result demonstrates that gei-17 activity suppresses checkpoint activation in response to DNA damage in the early embryo."]
- Mechanism is suppression of fork stalling, i.e. removal of the activating signal
  rather than action on ATL-1/CHK-1: [PMID:16549501 "These results provide further evidence that loss of gei-17 causes replication fork stalling in MMS-exposed embryos."]
  -> keep GO:1904290 as non-core.

### Mitotic and meiotic chromosome segregation
- Mitosis: [PMID:25475837 "Altogether, SUMO conjugates accumulate on chromatin during metaphase in a manner dependent on not only UBC-9 but also on the E3 ligase GEI-17."]
  GEI-17 at metaphase plate [PMID:25475837 "Immunostaining showed that, like SUMO, GEI-17 is localized to the metaphase plate"]
- Oocyte meiosis: GEI-17 assembles the midbivalent ring complex by SUMO conjugation + SIM
  binding [PMID:27939944 "We identified GEI-17/PIAS as the key SUMO E3 ligase required for this complex to assemble and show that it is directly involved in SUMO modification of KLP-19."]
  [PMID:27939944 "In the absence of GEI-17, chromosome alignment was compromised"]
- Anaphase I: BUB-1 and CLS-2 dynamics [PMID:31243051 "In addition, we have shown that BUB-1 is a SUMO substrate and its modification is determined by GEI-17-mediated conjugation and ULP-1-mediated deconjugation."]
- Possible NEW for mitotic metaphase chromosome alignment (GO:0007080) not proposed:
  the mitotic alignment phenotype is described mainly for UBC-9/SUMO; kept as a question.

### Transcriptional repression (non-core)
- tbx-2 autorepression requires SUMO pathway incl. GEI-17 [PMID:25873636 "SUMOylation is required for tbx-2 repression, as RNAi knockdown of the UBC-9 E2 SUMO-conjugating enzyme, the GEI-17 E3 SUMO-ligase, or the SMO-1 SUMO peptide also resulted in ectopic Ptbx-2::gfp expression."]
- TBX-2 Y2H interaction [PMID:25873636 "TBX-2 binds the E2 SUMO-conjugating enzyme UBC-9 and the E3 SUMO ligase GEI-17 in yeast 2-hybrid assays"]
- GEI-17-dependent SUMOylation of TBX-2 itself in worms was not shown; deep research
  overstates "GEI-17 SUMOylates ... TBX-2".
- Vulva: LIN-1 K169 SUMOylation is required for vulA contraction (PMID:35666766); AID of
  GEI-17 phenocopies SUMO loss in VPCs.

### Germline piRNA/nuclear silencing (redundant with PIE-1)
- gei-17 nulls alone do not desilence the piRNA sensor; with pie-1[K68R] they cause
  complete desilencing and sterility [PMID:34003111 "Thus PIE-1 and GEI-17 appear to function redundantly to promote piRNA surveillance and fertility in the adult germline."]
- HDA-1 SUMOylation/NuRD formation depend redundantly on PIE-1 and GEI-17
  [PMID:34003109 "SUMOylation of HDA-1, formation of an adult NuRD complex, and piRNA-mediated silencing depend redundantly on PIE-1"]
- GEI-17 inhibits piRNA transcription foci (PMID:40316696 abstract only).
- No GOA annotation currently; not proposed as NEW: genetic redundancy evidence and
  no direct demonstration that GEI-17 (rather than PIE-1) SUMOylates HDA-1 in vivo.
  Raised as a suggested question.

### Nuclear organization
- Telomere anchoring at the nuclear periphery in embryos requires GEI-17
  [PMID:24297748 "Telomere anchoring in embryos depends on GEI-17, SUN-1, and POT-1."]
  Substrate unknown; no NEW proposed.

## Deep research (openscientist) check

Verified against primary papers: E3 activity (PMID:15654100, 19111656, 25475837, 27939944),
POLH-1 protection (19111656), checkpoint silencing (16549501), meiotic ring complex
(27939944, 31243051), telomeres (24297748), LIN-1 K169 (35666766). Overstatements: TBX-2
SUMOylation by GEI-17 (only Y2H + RNAi). Omission: PIE-1/HDA-1 germline silencing
(PMID:34003111, PMID:34003109).

## IBA notes

- JAK-STAT (GO:0046426) and transcription regulator inhibitor activity (GO:0140416) IBAs
  come from a PIAS1/Su(var)2-10 node (PTN000845825). No gei-17 evidence for STAT
  inhibition; worm STAT signalling is non-canonical. Marked over-annotated, not removed.
