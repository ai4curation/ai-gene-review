# GATB notes

## Deep research

`GATB-deep-research-claude-code.md` came from `just deep-research-claude-code human GATB --timeout 1700`.
It ran for 39 s with 2 web searches (`web_search_requests: 2`) and 4 citations, and states that it did not
read full texts. It also reports, and declined to follow, an injected "REMINDER" instruction in a search
result. It was used only as a list of leads.

## Function

- GATB (formerly PET112/PET112L) = GatB subunit of mitochondrial GatCAB (QRSL1-GATB-GATC), GatB/GatE family.
- UniProt (HAMAP MF_03147): GatB recognises tRNA(Gln), phosphorylates the tRNA-bound Glu side chain with ATP
  (gamma-phospho-Glu-tRNA(Gln)) and amidates it with ammonia supplied by GatA; binds 2 Mg2+.
- Human GatCAB identified, knockdown of any subunit accumulates Glu-tRNA(Gln), reconstituted in vitro
  [PMID:19805282, abstract only].
- Friederich 2018 [PMID:30283131]: GATB patients (family 1) with lethal cardiomyopathy; reduced GatB protein,
  respiratory chain deficiencies in fibroblasts rescued by GATB-V5 transduction; V5-GatB strictly mitochondrial
  in U2OS; yeast pet112 model.
- Mitochondrial import of human PET112 shown in vitro [PMID:9878253, abstract only].

## Curation decisions

- GO:0070681 obsolete (QuickGO comment: annotations require review rather than migration). Replaced by
  GO:0019988 charged-tRNA amino acid modification, consistent with GATC and QRSL1 reviews.
- GO:0003824 / GO:0016874 / GO:0016884 are all ancestors of GO:0050567 (checked with OAK `ancestors -p i`);
  the IEA rows are MODIFYed to GO:0050567.
- Protein binding: QRSL1 rows reflect GatCAB co-membership; LINC01561 (Q8N1V8) rows are from proteome-scale
  binary screens with no functional link. All removed.
- No NEW annotations proposed. A tRNA binding term (GatB is the tRNA-recognition subunit by homology)
  was considered but there is no direct human binding assay.
