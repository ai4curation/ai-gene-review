# FD (bZIP14; At4g35900; UniProtKB:Q84JK2) notes

## Identity check (2026-10-05)

- Fetched by accession (`just fetch-gene ARATH Q84JK2 --alias FD`); uniprot.txt reads `FD_ARATH`,
  `Name=FD; Synonyms=BZIP14; OrderedLocusNames=At4g35900`.
- Falcon deep research failed (HTTP 402); notes are from cached publications.

## Function summary with provenance

- FD is the shoot-apex partner of FT: [PMID:16099979 "A bZIP transcription factor, FD, preferentially
  expressed in the shoot apex is required for FT to promote flowering."] [PMID:16099979 "FD and FT are
  interdependent partners through protein interaction and act at the shoot apex to promote floral
  transition"]
- FT-FD complex activates AP1: [PMID:16099980 "A complex of FT and FD proteins in turn can activate floral
  identity genes such as APETALA1 (AP1)."]
- Phosphorylation and 14-3-3 bridge: [PMID:25661797 "phosphorylates a threonine residue at position 282 of
  FD (FD T282), which is a crucial residue for the complex formation with FT via 14-3-3."]; nuclear
  [PMID:25661797 "These results indicate that FD is constitutively localized in the nucleus in a
  phosphorylation-independent manner."]
- Genome-wide binding: [PMID:30770462 "Importantly, we observed direct binding of FD to targets involved in
  several aspects of plant development."] [PMID:32492426 "Identical G-box sequences are enriched at FD and
  FDP binding sites, but only FD binds to genes involved in flowering and only fd alters their
  transcription."]
- TFL1 antagonism: [PMID:33046692 "Here, we show that TFL1 is recruited to thousands of loci by the bZIP
  transcription factor FD."]
- Floral meristem role: [PMID:40326559 "Binding of FD to SEP genes suggests that diminished SEP gene
  expression is a primary defect in the mutants."]
- FD/FDP heterodimer in vivo doubtful: [PMID:32492426 "The proposed heterodimerization partner of FDP is
  unlikely to be FD"]

## Curation decisions

- FT protein-binding rows -> MODIFY to GO:0001223 transcription coactivator binding (FT = non-DNA-binding
  co-activator; matches FT review's GO:0003713 / GO:0140297).
- FDP row -> MODIFY to GO:0046982 protein heterodimerization activity, non-core.
- NEW GO:0001228 (activator, RNA pol II-specific) IDA from ChIP-seq/target activation.
- Photoperiodism IMP (PMID:9615462) kept as non-core: FD acts downstream of photoperiod perception.
