# CAL (CAULIFLOWER, AGL10, At1g26310; UniProt Q39081) curation notes

## 2026-10-05 — initial review (floral_meristem_identity module)

- Identity check: `CAL-uniprot.txt` is CAL_ARATH, Q39081, At1g26310, synonym AGL10. Correct protein.
- Falcon deep research was attempted (`just deep-research-falcon ARATH CAL`) but the provider exited with code 1; no deep-research file was produced. Notes below are from cached publications only.

### Core biology

- CAL encodes a MADS-domain protein closely related to AP1; partial redundancy with AP1 in floral meristem formation
  [PMID:7824951 "Genetic studies demonstrate that two Arabidopsis genes, CAULIFLOWER and APETALA1, encode partially redundant activities involved in the formation of floral meristems, the first step in the development of flowers."]
  [PMID:7824951 "Like APETALA1, CAULIFLOWER is expressed in young flower primordia and encodes a MADS-domain, indicating that it may function as a transcription factor."]
- Brassica oleracea var. botrytis curd phenotype linked to non-functional CAL homolog
  [PMID:7824951 "its CAULIFLOWER gene homolog is not functional"].
- ap1 cal ful triple mutant makes leafy shoots instead of flowers; mechanism is failure to up-regulate LFY plus ectopic TFL1
  [PMID:10648231 "We demonstrate that this phenotype is caused both by the lack of LFY upregulation and by the ectopic expression of the TERMINAL FLOWER1 (TFL1) gene."]
- CAL listed among the floral meristem identity genes with LFY and AP1
  [PMID:10368173 "Assignment of floral fate to lateral meristems is primarily due to the cooperative activity of the flower meristem identity genes LEAFY (LFY), APETALA1 (AP1), and CAULIFLOWER."]
- AP1/CAL used as baits in yeast two-hybrid; MADS heterodimers [PMID:11439126]; matrix Y2H gives CAL-SOC1 heterodimer [PMID:15805477].

### Annotation decisions (summary)

- MF: core = GO:0000981 (IBA, accepted). Generic DNA binding / GO:0003700 IEA -> MODIFY to more specific terms.
- protein binding (SOC1 partner) -> MODIFY to GO:0046982 protein heterodimerization activity.
- BP: GO:0010582 floral meristem determinacy (IBA; CAL is in its own WITH/FROM which is expected) ACCEPT; GO:0009911 positive regulation of flower development ACCEPT.
- No GO term exists for "floral meristem identity specification"; AP1 review already proposes one. Not duplicated here.
