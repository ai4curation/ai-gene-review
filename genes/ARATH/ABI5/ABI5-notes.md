# ABI5 (ABSCISIC ACID-INSENSITIVE 5) — curation notes

UniProt: Q9SJN0 (ABI5_ARATH). Locus At2g36270. Synonyms: BZIP39/AtbZIP39, DPBF1/AtDPBF1, GIA1, NEM1.
442 aa. Group-A basic leucine zipper (bZIP) transcription factor, ABI5 subfamily.

## Core identity and molecular function

ABI5 is a group-A bZIP transcription factor that binds the ABA-responsive element (ABRE,
ACGT-containing G-box-like cis-element) of ABA-regulated genes. The bZIP domain (residues
355-418; basic motif 357-376, leucine zipper 383-404) mediates sequence-specific DNA binding
and dimerization.

- It was cloned by positional cloning and shown to encode a bZIP TF; the abi5-1 allele
  encodes a truncated protein lacking the DNA-binding and dimerization domains, demonstrating
  these are required for function [PMID:10760247 "it encodes a member of the basic leucine zipper transcription factor family. The previously characterized abi5-1 allele encodes a protein that lacks the DNA binding and dimerization domains required for ABI5 function"].
- DNA binding (direct): yeast one-hybrid shows ABI5 binds directly to the AtEm6 (LEA gene)
  promoter fragment [PMID:11489176 "only ABI5 binds directly to this promoter fragment"]. ABI5
  also forms homodimers and heterodimer with ABI3 partner loci [PMID:11489176 "only ABI3 and ABI5 physically interact with each other, and ABI5 can form homodimers"].
- UniProt FUNCTION: "Binds to the embryo specification element and the ABA-responsive element
  (ABRE) of the Dc3 gene promoter and to the ABRE of the Em1 and Em6 genes promoters. Can also
  trans-activate its own promoter" — establishes both DNA-binding TF activity and
  transcriptional activation (ABRE-binding). UniProt keyword "Activator".

## Transcriptional activation (direct targets)

- Activates RD29B in seeds via ABREs; transient transactivation: "ABI3, ABI5 and AREB1
  activated transcription of a GUS reporter gene driven by the RD29B promoter strongly"
  [PMID:16463099 "ABI3, ABI5 and AREB1 activated transcription of a GUS reporter gene driven by the RD29B promoter strongly"].
- Activates LEA genes Em1/Em6 conferring osmotolerance [PMID:18941053 "ABI5 activates the transcription of Late Embryonic and Abundant (LEA) genes, whose products confer osmotolerance to the embryo"].
- Directly binds the ABR (LEA) promoter and regulates it (involved in dark-induced leaf
  senescence) [PMID:27095403 "In vitro and in vivo assays showed that ABI5 bind to the ABR promoter, indicating that ABI5 directly regulates the expression of ABR"].
- Coactivator partnership: LEC1/L1L NF-YB act with seed-specific ABRE-binding factors; ABI5
  is a seed ABRE-binding factor in this class [PMID:19207209 "LEC1/L1L-[NF-YC2] can strongly activate the CRC promoter in the absence of ABA when co-expressed with a seed-specific ABA-response element (ABRE)-binding factor, bZIP67"]. (This paper validates bZIP67 specifically; ABI5 was the TAIR-assigned IDA for positive regulation of transcription.)

## Biological roles

- Central effector of ABA signaling in seeds. Mediates ABA inhibition of germination /
  postgermination growth arrest: ABI5 confers enhanced ABA response and is necessary to
  maintain germinated embryos in a quiescent state [PMID:11287670 "ABI5 is necessary to maintain germinated embryos in a quiescent state thereby protecting plants from drought"].
- "final common repressor of germination" in response to ABA/GA balance [PMID:18941053 "These data support the notion that ABI5 acts as the final common repressor of germination in response to changes in ABA and GA levels"]. Negative regulation of seed germination is supported by abi5 mutant analysis [PMID:18941053].
- ABI5 expression is induced by ABA, drought, salt, glucose; autoregulated [PMID:11287670 "ABI5 expression is regulated by drought and salt exposure"]. Note these IEP annotations to response-to-stress terms reflect that ABI5 transcription is regulated by the stress, i.e. ABI5 acts downstream within these responses (acts_upstream_of_or_within).
- Seed development / late embryogenesis: regulates a subset of LEA genes during seed
  maturation [PMID:10760247 "ABI5 regulates a subset of late embryogenesis-abundant genes during both developmental stages"]; expressed in embryo during latest stages of maturation.
- Sugar/glucose signaling: ABI5 is part of the ABA-sugar crosstalk network in seedling
  development [PMID:12663220 — review of sugar-hormone connections]. TAS annotation.
- Gibberellin response: abi5 affects GA-controlled germination via RGL2-ABA-ABI5 module
  [PMID:18941053].

## Subcellular location

- Nucleus. GFP fusions of ABI5-family proteins constitutively localize to nuclei
  [PMID:15642716 "the three fusion proteins were expressed with a largely overlapping pattern and constitutively localized in the nuclei"]. UniProt: SUBCELLULAR LOCATION Nucleus
  (ECO:0000269|PubMed:12410810). Consistent with bZIP TF and PROSITE bZIP NLS rule.

## Protein interactions (mostly regulatory/stability, not core MF)

Many GO:0005515 "protein binding" IPI annotations exist; these capture regulators of ABI5
rather than its own informative molecular function:
- KEG (KEEP ON GOING) RING E3 ligase — mediates ABI5 degradation [PMID:17194765].
- SUMO1 / SIZ1 — sumoylation at Lys-391 protects ABI5 from degradation [PMID:19276109 "Sumoylation of ABI5 by the Arabidopsis SUMO E3 ligase SIZ1 negatively regulates abscisic acid signaling"].
- SRK2A (SnRK2) — kinase, phosphorylates/regulates ABI5 [PMID:32612234 phytohormone network].
- TAP46 / PP2A — phosphatase-related positive regulator [PMID:24357600].
- VQ18/VQ26 — negative modulators of ABA response via ABI5 [PMID:29771466].
- DWA1/DWA2 (CUL4 DWD) — negative regulators [PMID:20525848].
- PP6/FYPP — phosphatase regulating ABI5 phosphorylation [PMID:23404889].
- XIW1 (WD40) — regulates ABI5 stability [PMID:31295628].
- NLP8 — nitrate/ABA crosstalk [PMID:40123384].
Per curation guidance, bare "protein binding" is uninformative as a core MF and these are
marked REMOVE; the biology is retained in the description/notes. The informative MF for ABI5
is sequence-specific DNA-binding transcription factor activity.

## Annotations of concern

- GO:0000976 transcription cis-regulatory region binding (PMID:25533953, PMID:30356219,
  PMID:31806676): these are large high-throughput Y1H network screens (secondary cell wall,
  nitrogen metabolism, vascular development). ABI5 appears as one of dozens of TFs binding
  test promoters in yeast. These do not reflect ABI5's established seed/ABA biology and are
  likely Y1H over-detection (ABI5 is seed-predominant). The generic MF "cis-regulatory region
  binding" is itself acceptable as a DNA-binding term, but the specific biological inference of
  ABI5 regulating cell-wall/nitrogen/vascular genes is weak. Kept as non-core / over-annotated.

## Core function synthesis

1. Sequence-specific DNA-binding transcription factor (ABRE/G-box binding) — GO:0003700 /
   GO:0043565 / GO:0000976 / GO:0000987.
2. Transcriptional activator of ABA/LEA target genes — GO:0045893.
3. Biological process: ABA-activated signaling controlling seed maturation, dormancy,
   negative regulation of germination, postgermination growth arrest — GO:0009737,
   GO:0010187, GO:0048316.
