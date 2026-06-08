# RNF14 (E3 ubiquitin-protein ligase RNF14; ARA54) notes

UniProt: Q9UBS8 (RNF14_HUMAN). RBR (RING-in-between-RING)-type E3 ligase, EC 2.3.2.31.
Legacy name ARA54 (androgen receptor coactivator 54).

## Core function (RNF14-RNF25 translation QC)
RNF14 is the E3 ligase of the RNF14-RNF25 translation quality control pathway that acts on
stalled ribosomes. Recruited by the ribosome collision sensor GCN1, RNF14 catalyzes atypical
K6-linked ubiquitination of translation factors (eEF1A/EEF1A1 and eRF1/ETF1) and ribosomal
proteins on stalled ribosomes, leading to their degradation. It is specifically required to
resolve reactive-aldehyde (e.g. formaldehyde)-induced RNA-protein crosslinks (RPCs) that stall
ribosomes, by K6-ubiquitinating the crosslinks for VCP-dependent extraction and proteasomal
degradation.

- UniProt FUNCTION: "E3 ubiquitin-protein ligase that plays a key role in the RNF14-RNF25
  translation quality control pathway ... promotes ubiquitination and degradation of translation
  factors on stalled ribosomes"
- UniProt FUNCTION: "Recruited to stalled ribosomes by the ribosome collision sensor GCN1 and
  mediates 'Lys-6'-linked ubiquitination of target proteins, leading to their degradation"
- UniProt FUNCTION: "Mediates ubiquitination of EEF1A1/eEF1A and ETF1/eRF1 translation factors
  on stalled ribosomes, leading to their degradation"
- [PMID:36638793 "An E3 ligase network engages GCN1 to promote the degradation of translation factors on stalled ribosomes"]
- [PMID:37651229 "involves the translational stress sensor GCN1 and the catalytic activity of the E3 ubiquitin ligases RNF14 and RNF25"]
- [PMID:37951215 "marked by atypical K6-linked ubiquitylation catalyzed by the RING-in-between-RING (RBR) E3 ligase RNF14, and subsequently resolved by the ubiquitin- and ATP-dependent unfoldase VCP"]
- EC 2.3.2.31 (RBR-type).

## Specific GO annotations (experimental)
- GO:0061630 ubiquitin protein ligase activity (IDA, many) - CORE.
- GO:0072344 rescue of stalled cytosolic ribosome (IDA) - core.
- GO:0085020 protein K6-linked ubiquitination (IDA PMID:27863242, 37951215, 37951216) - core, signature.
- GO:0160127 protein-RNA covalent cross-linking repair (IDA PMID:37951215, 37951216) - core.
- GO:0006511 ubiquitin-dependent protein catabolic process (IDA) - core.
- GO:0022626 cytosolic ribosome (IDA, is_active_in) - core localization.
- GO:0031624 ubiquitin conjugating enzyme binding (IBA) - binds E2; supports ligase role.
- GO:0000151 ubiquitin ligase complex (IBA part_of) - part of RNF14-RNF25 ligase machinery.
- GO:0008270 zinc ion binding (IEA) - RBR/zinc fingers; structural, NON_CORE.

## Legacy androgen receptor / Wnt roles (ARA54)
RNF14/ARA54 was originally described as an androgen-receptor coactivator (PMID:10085091,
PMID:19345326) and later a regulator of TCF/beta-catenin (Wnt) transcription and colon cancer
survival (PMID:23449499). UniProt: "Independently of its function in the response to stalled
ribosomes, acts as a regulator of transcription in Wnt signaling ... May also play a role as a
coactivator for androgen- and ... progesterone-dependent transcription."
- These are genuine but secondary/moonlighting roles, and the legacy refs (PMID:10085091,
  11322894, 19345326, 23449499) are not cached. Keep nuclear/transcription/AR/Wnt annotations as
  KEEP_AS_NON_CORE; the core, mechanistically defined function is the cytosolic RNF14-RNF25 RQC
  ligase activity.
- GO:0003713 transcription coactivator activity (TAS PMID:10085091) - legacy ARA54 role; NON_CORE.
- GO:0050681 nuclear androgen receptor binding (IPI PMID:19345326) - real AR interaction; NON_CORE.
- GO:0060765, GO:0030521 AR signaling; GO:0060828 Wnt; GO:0006355/0045893 transcription - NON_CORE.
- GO:0019787 ubiquitin-like protein transferase activity (IDA PMID:11322894) - older
  characterization of ARA54 E2-dependent ubiquitination; MODIFY/generalize toward the specific
  ubiquitin ligase activity; KEEP or treat as parent of GO:0061630.

## protein binding (IPI) - high-throughput / E2 network
- PMID:19549727 E2 interaction network; PMID:25416956/32296183 HuRI; PMID:31515488 variant
  interactome; PMID:32814053 neurodegeneration interactome; PMID:10085091 AR (ARA54). Bare
  protein binding uninformative -> KEEP_AS_NON_CORE.

## Localization
Nucleus and cytoplasm/cytosol (IDA PMID:11322894; HPA nucleoplasm+cytosol). The RQC ligase role
is cytosolic/ribosome-associated. Cytosol/cytoplasm/cytosolic ribosome -> ACCEPT; nucleus/
nucleoplasm -> KEEP_AS_NON_CORE (genuine, tied to transcriptional moonlighting).

## Actions summary
- Core MF: GO:0061630 ubiquitin protein ligase activity (RBR, EC 2.3.2.31).
- Core BPs: GO:0072344 rescue of stalled ribosome; GO:0085020 K6 ubiquitination; GO:0160127
  protein-RNA crosslink repair; GO:0006511 ubiquitin-dependent catabolism.
- E2 binding / ligase complex -> ACCEPT (support core).
- AR/Wnt/transcription/nucleus -> KEEP_AS_NON_CORE (moonlighting).
- protein binding IPI, zinc ion binding -> KEEP_AS_NON_CORE.
