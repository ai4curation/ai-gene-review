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
  inhibition. GO:0046426 is REMOVED (C. elegans has no JAK, PMID:28874466; recorded as a member
  exception in the PTHR10782 family review); GO:0140416 is marked over-annotated.

## Literature review integration (2026-10-04)

- Liongue & Ward 2013 (PMID:24058787) added to the GO:0046426 IBA REMOVE. The canonical JAK-STAT pathway was
  assembled in the bilaterian ancestor [PMID:24058787 "These came together to form the canonical JAK-STAT signaling pathway prior to the divergence of protostomia"],
  so the eumetazoan PIAS node (PTN000845825) is a sound IBD placement, and nematode JAK absence is a
  lineage-specific loss that needs an IRD.
- Palvimo 2007 (PMID:18031232, abstract only) added for PIAS-family background [PMID:18031232 "PIAS proteins were initially named for their ability to interact with STAT proteins and inhibit their activity, but their interactions and functions are not restricted to the STATs."].
  It also says [PMID:18031232 "their co-regulator effects are often independent of their RING finger but dependent on their SIM (SUMO-interacting motif) or SAP (scaffold attachment factor-A/B/acinus/PIAS) domain"].
  This qualifies the GO:0140416 MARK_AS_OVER_ANNOTATED reasoning, which rests on GEI-17 transcriptional
  effects being SUMOylation-dependent. The action is unchanged, but this is worth revisiting.
- No actions changed.

Cross-gene briefing for GO editors and PAINT curators: https://claude.ai/artifact/4MLfbbbWWnLchDvspwdPuM

## OpenScientist: ligase-independent repression via SAP/SIMs? (2026-10-04)

Report: `gei-17-hypotheses/gei17-sap-sim-coregulator/openscientist.md` (neutral framing; the
review's MARK_AS_OVER_ANNOTATED on GO:0140416 was withheld from the run).

- Verdict: refuted as a mechanism for GO:0140416; the over-annotation call stands.
- Checked against repo data before wiring: GEI-17's UniProt entry lists PINIT and the SP-RING
  zinc finger but no SAP domain; human PIAS1's lists IPR003034 SAP_dom and PS50800.
- Human PIAS1 ligase-independent inhibition is SAP-independent [PMID:24036127 "PIAS1 with a
  mutation in the SAP domain retained the inhibitory function in virus-induced IFN
  transcription"] and ligase-independent [PMID:24036127 "SUMO E3 ligase activity dead mutant
  PIAS1/C350S still had the comparable inhibitory function with WT PIAS1"]; for PIASy and Oct4
  [PMID:17991485 "These modes of PIASy action are uncoupled from its sumoylation activity"].
- Worm repression is ligase-dependent [PMID:40316696 "isolated the SUMO E3 ligase GEI-17 as
  inhibiting and the SUMO protease TOFU-3 as promoting piRNA transcription foci formation"].
- From the run, not re-derived: a cryptic SAP-like fold may remain in the N-terminus (AlphaFold),
  but the DNA-binding helix is not conserved. This resolves the Palvimo 2007 caveat recorded
  earlier: RING-independent co-regulation by PIAS proteins does not run through the SAP domain.
- Lead, not acted on: GEI-17's repression of piRNA transcription could be captured as a process
  term downstream of its ligase activity (PMID:40316696, abstract only). Decisive experiment: a
  ligase-dead GEI-17 rescue in the piRNA transcription assay.

## Correction: GO:0140416 is UNDECIDED, not over-annotated (2026-10-05)

The previous section, and the MARK_AS_OVER_ANNOTATED action it supported, misread the term.
GO:0140416 transcription regulator inhibitor activity is defined as inhibiting a transcription
regulator "via direct binding and/or post-translational modification", so inhibition through
GEI-17's SUMO ligase activity is within the term. The OpenScientist run tested a narrower claim,
ligase-independent repression through the SAP domain and SIMs, and its refutation applies only
to that route. It does not refute the term.

- Binding route through the SAP domain: not supported (no SAP domain in GEI-17; PIAS1's
  ligase-independent inhibition does not need it, PMID:24036127).
- Modification route: plausible. GEI-17 inhibits piRNA transcription condensates built by the
  USTC complex (PRDE-1, SNPC-4, TOFU-4, TOFU-5) in a SUMOylation-dependent way [PMID:40316696
  "isolated the SUMO E3 ligase GEI-17 as inhibiting and the SUMO protease TOFU-3 as promoting
  piRNA transcription foci formation"], but the cached abstract does not show direct SUMOylation
  of a USTC component, and the full text is unavailable.
- Action changed to UNDECIDED; propagation_review root cause back to UNRESOLVED. The PTHR10782
  family review's node text was updated to match. Prompted by the ai4c-reviewer finding on
  ai4curation/ai-gene-review#4199, whose suggested fix (a member exception or REMOVE) would
  have hardened the misreading.
- Decisive test: whether GEI-17 SUMOylates PRDE-1 or SNPC-4 directly, and whether that SUMOylation
  is what blocks condensate formation.
