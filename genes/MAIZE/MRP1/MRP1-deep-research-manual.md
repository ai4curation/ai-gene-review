# MRP1 (ZmMRP1, Q6Y3I1) - manual literature review

No deep-research API was available; this summary was compiled by hand from the
cached publications and a PubMed search ("ZmMRP1 maize", 17 hits, October 2026).

## Identity and name collision

- Q6Y3I1 is the TrEMBL entry for EMBL AAO72316.1 (mRNA AY186245), GeneID
  100037760, the maize ABCC-family "multidrug resistance associated protein 1".
- Most PubMed hits for "ZmMRP1" are about **ZmMRP-1, a MYB-related transcription
  factor of the basal endosperm transfer layer** (e.g. PMID:19636587,
  PMID:18830706, PMID:29071379). That is a different gene and was excluded.
- ZmMRP3 (anthocyanin vacuolar transport) and ZmMRP4/lpa1 (phytic acid) are
  other maize ABCC paralogs; their functions should not be transferred to MRP1.
  The UniProt FUNCTION text about phytic acid is an ARBA rule
  (ARBA00057614), i.e. a family-level prediction derived from lpa1-type genes,
  not evidence about this protein.

## Cloning and structure

[PMID:14557075 "Two genes encoding ATP-binding cassette (ABC) transporters were
isolated from the crop plant Zea mays (maize). The clones, designated ZmMRP1 and
ZmMRP2, were highly homologous to members of the multidrug resistance associated
protein (MRP) subfamily."]

[PMID:14557075 "ZmMRP1 contained an additional N-terminal membrane-spanning domain
(MSD0) that is typical of MRP transporters"]

Abstract only. Sequence: two ABC transmembrane domains and two NBDs (UniProt
features); local motif scan (file:MAIZE/MRP1/MRP1-bioinformatics/RESULTS.md)
finds a consensus NBD2 Walker B (ILVLDE) and a degenerate NBD1 Walker B (VYLLDD).

## Expression / induction

- [PMID:14557075 "ZmMRP1 was induced by aminotriazole and to a lesser extent by
  menadione"]
- Pang et al. 2012 (full text): semi-quantitative RT-PCR in leaves; [PMID:22792398
  "All five compounds significantly increased the amount of ZmMRP1 transcript, but
  at different magnitude and after different time delay."] Compounds: atrazine,
  2,4-D, primisulfuron, metolachlor, dichlormid.
- Pang et al. 2012b (full text): [PMID:23144728 "rac-metolachlor was found to be a
  stronger inducer for ZmMRP1 expression as compared to S-metolachlor"]. A
  vanadate (general ABC/P-type ATPase inhibitor) experiment altered herbicide
  sensitivity, but vanadate is not specific to MRP1, so it is not evidence about
  this gene product.
- Isoxadifen-ethyl safener (abstract only): [PMID:29870861 "ZmGSTIV, ZmGST6, ZmGST31
  and ZmMRP1 could be considered safener-responsive"].

## What is not known

- No transport assay, ATPase assay, substrate, or subcellular localization has been
  reported for ZmMRP1. The glutathione-conjugate (phase III detoxification) role
  is an inference from the plant MRP family and from co-induction with GSTs
  ([PMID:22792398 "Multidrug resistance-associated proteins (MRPs), members of ABC
  transporter family, play a role in the detoxification of xenobiotics by
  transporting GS conjugates into the vacuole"], stated as background on the family).
- No mutant has been described.
