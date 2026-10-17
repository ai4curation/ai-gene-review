# P12 (P12_BPPH6, P07580) — Curation Notes

## Overview
- **Organism:** *Pseudomonas* phage phi6 (`NCBITaxon:2928686`, *Cystovirus phi6*)
- **Gene / Protein:** `P12` / Morphogenetic protein P12 (`UniProtKB:P07580`, 195 AA)
- **Genomic Segment:** Encoded on the small (S) dsRNA segment (co-translated/regulated with P8 and P9).

## Biological Role in the Cystovirus Lifecycle
1. **Nonstructural Viral Envelope Morphogenesis Factor (`GO:0019068`, `GO:0030430`):**
   - P12 is a 20.3 kDa nonstructural protein synthesized in the host cell cytoplasm (`GO:0030430`) that is essential for acquisition of the viral lipid-containing envelope around the mature nucleocapsid (`GO:0019068` virion assembly) [file:BPPH6/P12/P12-uniprot.txt; PMID:8021194].
   - Plasmid co-expression of `P9` and `P12` in *Pseudomonas syringae* pv. *phaseolicola* in the absence of phage infection demonstrates that P12 stabilizes major envelope protein P9 against proteolytic degradation and promotes the formation of low-density phospholipid-P9 precursor vesicles (`PMID:8021194`).
   - Together, P9 and P12 are necessary and sufficient for assembly of the phi6 lipid-protein membrane precursor structures [PMID:8021194].

## Curation Decisions
- **Existing GOA Annotations:** None (`P12-goa.tsv` is empty).
- **New Annotations (`action: NEW`):**
  - `GO:0019068` (`virion assembly`, `involved_in`, `IDA` from `PMID:8021194`): Directly supported by plasmid co-expression experiments showing P12 is required to stabilize P9 and assemble lipid-P9 viral envelope precursor particles.
  - `GO:0030430` (`host cell cytoplasm`, `located_in`, `IC` from `PMID:8021194` and `file:BPPH6/P12/P12-uniprot.txt`): P12 is a nonstructural morphogenetic assembly factor acting inside the infected host cell to mediate intracellular envelope biogenesis.
- **Core Function & Proposed Molecular Function:**
  - Because GO currently lacks a specific molecular function term for nonstructural viral membrane-morphogenesis factors that stabilize and insert viral envelope proteins into lipid vesicles without being incorporated into the mature virion, we use `proposed_molecular_function: viral envelope morphogenesis factor activity` paired with a top-level `proposed_new_terms` entry.
