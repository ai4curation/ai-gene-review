# Curation Notes: Bacteriophage T4 `t` (Holin / Protein rV, P06808)

## Overview
- **Gene symbol:** `t` (synonyms: `rV`, `T4p247`)
- **UniProt ID:** `P06808` (`HOLIN_BPT4`)
- **Length:** 218 amino acids
- **Function:** Canonical class III holin that serves as the lysis timer and inner-membrane pore-forming protein during late T4 infection.

## Biological Role and Mechanism
- Holin T is a single-pass type II inner-membrane protein with a short N-terminal cytoplasmic tail, a single transmembrane helix, and a large C-terminal periplasmic globular domain (PubMed 11255004, PubMed 16166524).
- During late infection, holin T accumulates harmlessly in the *Escherichia coli* inner (cytoplasmic) membrane until it reaches a critical allele-specific concentration, at which point it triggers the formation of micron-scale holes in the inner membrane (PubMed 11255004).
- Inner membrane permeabilization collapses the proton motive force and allows the cytoplasmic endolysin (gp*e*, lysozyme) to escape into the periplasm and degrade the peptidoglycan cell wall, initiating host cell lysis and phage release.
- The periplasmic C-terminal domain of holin T is the direct target of the soluble periplasmic antiholin RI (`rI`), which forms a 2:2 heterotetramer (`T2-RI2`) with holin T to prevent holin oligomerization and impose lysis inhibition (LIN) in response to superinfection (PubMed 16166524, PubMed 17693511, PubMed 34456892).

## Review of Existing GO Annotations
- `GO:0140911` (pore-forming activity, IEA, GO_REF:0000104): **ACCEPT**. Directly captures the molecular function of holin T in forming large micron-scale lesions in the host inner membrane.
- `GO:0044659` (viral release from host cell by cytolysis, IEA, GO_REF:0000002): **ACCEPT**. Accurately describes the core biological process mediated by holin T.
- `GO:0031640` (killing of cells of another organism, IEA, GO_REF:0000043): **MODIFY** to `GO:0044659` (viral release from host cell by cytolysis). The broad UniProt keyword-derived term is less informative than the specific viral cytolytic release process already present.
- `GO:0020002` (host cell plasma membrane, IEA, GO_REF:0000120): **ACCEPT**. In Gram-negative bacteria such as *E. coli*, the inner (cytoplasmic) membrane corresponds to `GO:0020002` (host cell plasma membrane).
- `GO:0016020` (membrane, IEA, GO_REF:0000104): **MODIFY** to `GO:0020002` (host cell plasma membrane), which more specifically captures localization to the host cytoplasmic membrane.
