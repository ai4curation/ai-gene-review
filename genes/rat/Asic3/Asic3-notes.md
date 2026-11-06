# Asic3 (rat) review notes

- 2026-10-28: Review created. Folder already existed (O35240 confirmed, RGD:708578, GeneID 286920).
  Publications cached with `just fetch-gene-pmids`; additionally cached PMID:19074149 (full text),
  PMID:18923424 and PMID:11528414 (abstracts). No deep-research provider available; see
  `Asic3-deep-research-manual.md`.
- Core function: homo/heterotrimeric proton-gated Na+ channel (GO:0160125) at the neuronal plasma
  membrane; acid sensor in nociceptors [PMID:11120882 "We propose that ASIC3 ... is the sensor of
  myocardial acidity that triggers cardiac pain"], [PMID:18923424 "Peripheral ASIC3 channels are thus
  essential sensors of acidic pain"].
- General MF rows (cation channel, sodium channel, ligand-gated sodium channel, pH-gated monoatomic ion
  channel, ion-gated channel) MODIFY to GO:0160125. Ion-gated (GO:0022839) is lateral: GO places
  pH-gated channels under ligand-gated (checked with OAK).
- Transport rows MODIFY to GO:0035725 sodium ion transmembrane transport.
- PDZ partner rows (CIPP, NHERF-1) MODIFY to GO:0030165 PDZ domain binding; NHERF-2, STOML3 and
  stomatin rows REMOVE as bare protein binding.
- Temperature-detection rows from mouse knockout: ASIC3 is not a temperature sensor; marked
  over-annotated. Mechanical rows kept as non-core (mouse KO mechanoreceptor phenotypes).
- Sour taste ISO from human: no evidence ASIC3 functions in sour taste (OTOP1 is the sour receptor);
  marked over-annotated.
- calcium-mediated signaling (GO_REF:0000108 inference from pH-gated calcium channel activity):
  Ca2+ permeation is minor and no ASIC3-driven Ca2+ signaling shown; over-annotated.
