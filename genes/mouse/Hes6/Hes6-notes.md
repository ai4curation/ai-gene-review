# Hes6 (mouse, Q9JHE6) review notes

## Provenance / process

- 2026-10-20: `just fetch-gene mouse Hes6` (27 GOA rows). `just deep-research-falcon mouse Hes6 --fallback perplexity-lite`
  FAILED (falcon failed; perplexity-lite fallback timed out after 600 s). No deep-research file exists; the review is
  built from primary literature retrieved by a PubMed search (`Hes6[tiab] AND (mouse OR mice OR murine)`) and cached
  with `just fetch-pmid`.
- Evolutionary grounding: mouse Hes6 is in PANTHER PTHR10985 (HES-related bHLH), subfamily SF11 (TRANSCRIPTION
  COFACTOR HES-6), together with human HES6 (Q96HZ4) and zebrafish hes6 (Q6P0J1). IBA rows come from PAINT nodes
  PTN004213585 (family-wide: nucleus, RNAPII cis-regulatory DNA binding, DNA-binding TF activity, negative regulation
  of RNAPII transcription) and PTN000105428 (anterior/posterior pattern specification, regulation of neurogenesis).
  Mouse Hes6 (MGI:1859852) is itself a seed for the PTN004213585 IBDs on GO:0000981 and GO:0000122.
- Several of the key papers are abstract-only in the cache (PMID:10851137, PMID:11959828, PMID:11076679,
  PMID:17868320, PMID:23689134, PMID:21501606). Full text: PMID:11551980, PMID:12972610, PMID:17065448,
  PMID:26105991, PMID:26435136, PMID:29404444, PMID:22114720 (Xenopus).

## What is experimentally established in MOUSE (Hes6 protein or mouse cells)

- Heterodimerises with / binds Hes1 and antagonises Hes1 repression; relieves Hes1 inhibition of Mash1-E47
  [PMID:10851137 "Hes6 alone does not bind to the DNA but suppresses Hes1 from repressing transcription. In addition,
  Hes6 suppresses Hes1 from inhibiting Mash1-E47 heterodimer and thereby enables Mash1 and E47 to upregulate
  transcription in the presence of Hes1."]
- Two further anti-Hes1 mechanisms: blocks Hes1-Gro/TLE interaction and promotes Hes1 proteolysis
  [PMID:12972610 "Hes6 inhibits the interaction of Hes1 with its transcriptional corepressor Gro/TLE. Moreover, it
  promotes proteolytic degradation of Hes1."]
- Binds Groucho/TLE corepressors through WRPW [PMID:11551980 "HES6 interacted with the corepressor transducin-like
  Enhancer of split 1 in yeast and mammalian cells through its WRPW COOH-terminal motif."] (mouse HES6 cDNA,
  C2C12 myoblasts).
- Homodimerises (preferentially) [PMID:17868320 "It is reported that Hes6 preferentially forms homodimers."]
- DNA binding: CONTESTED. Bae et al. found no DNA binding by Hes6 alone (short loop); Cossins et al. found binding to
  the ESE box and repression of an ESE reporter [PMID:11959828 "Hes6 binds DNA containing the Enhancer of Split E box
  (ESE) motif, the preferred binding site of Drosophila EoS proteins, and represses transcription of an ESE box
  reporter."]; Gao et al. infer N-box binding in myoblasts from a HES6-VP16 fusion [PMID:11551980 "These results
  confirm that HES6 binds to N boxes in myoblasts."], probably via heterodimers. Biological activities (myogenic,
  proneural, anti-gliogenic) do NOT require Hes6's own DNA-binding basic arm [PMID:11959828; PMID:17065448].
- Nuclear protein [PMID:11551980 "localized to the nucleus in transfected cells"; PMID:17065448 nuclear localisation
  required].
- Neurogenesis: promotes cortical neuron differentiation [PMID:12972610], knockdown in cortical progenitors yields
  supernumerary astrocytes [PMID:17065448]; Hes6 knockout mice show impaired neuroblast differentiation in adult dentate
  gyrus [PMID:26105991 "Hes6 knockout negatively affects neuroblast differentiation based on DCX
  immunohistochemistry."]; retinal misexpression promotes rod differentiation [PMID:10851137].
- Myogenesis: C2C12 overexpression can induce (Gao) or impair (Cossins) differentiation; knockdown disrupts actin and
  fusion [PMID:21501606]. Direction is context-dependent, so "regulation of myoblast differentiation" is the safe level.
- Other (not core): represses hepatic Pparg2 via HNF4a (adenoviral over/under-expression; PMID:29404444); sumoylation
  at K27/K30 regulates stability (PMID:26435136, HeLa / NIH3T3); interacts with RelA/NF-kB in cortical progenitors
  (PMID:23689134); oscillates antiphasically to Hes1 in liver (PMID:22913986, not cited in review).

## Inferred only (no mouse experimental evidence)

- Anterior/posterior pattern specification (IBA, PTN000105428). The zebrafish ortholog acts in the segmentation clock
  (Her7:Hes6 heterodimers), but no mouse Hes6 somitogenesis data were found; kept as non-core, flagged as inferred.

## Decisions summary

- Core MF: transcription regulator inhibitor activity (GO:0140416; antagonising Hes1), binding to Hes1
  (GO:0061629), transcription corepressor binding (GO:0001222, NEW; TLE via WRPW), dimerisation.
- DNA-binding / DNA-binding TF rows: kept as non-core (contested), general ones MODIFIED to the specific
  IDA-supported terms (GO:0000977, GO:0001227).
- Generic development/differentiation rows MODIFIED to positive regulation of neuron differentiation /
  positive regulation of neurogenesis / regulation of myoblast differentiation.
