# Bacteriophage P2 Gene Y (Class I holin gpY; UniProt P51773)

## Overview
Gene **Y** of temperate myovirus *Escherichia phage P2* (`BPP2`) encodes the essential 93-amino-acid class I canonical holin gpY (10.1 kDa; `UniProt:P51773`, `InterPro:IPR007633` / `Pfam:PF04550` `Phage_holin_3_2`) (`PMID:8051010`, `PMID:23335412`). gpY possesses three transmembrane domains with an N-out, C-in topology in the *Escherichia coli* inner (plasma) membrane (`PMID:23335412`). It accumulates harmlessly in the inner membrane during late infection until a genetically programmed time ("lysis clock")—or premature membrane depolarization by energy poisons such as DNP/cyanide—triggers oligomerization into micrometer-scale membrane holes, collapsing the proton motive force and releasing cytoplasmic endolysin gpK into the periplasm to degrade peptidoglycan (`PMID:8051010`, `PMID:23335412`). Unlike phage lambda S (which uses dual-start translation to produce both holin S105 and antiholin S107), P2 Y requires its short cytoplasmic C-terminal domain for lysis and is negatively regulated by a separate antiholin protein, LysA, encoded immediately downstream (`PMID:23335412`).

## Key Literature & Experimental Evidence
- **PMID:8051010** (*Functions involved in bacteriophage P2-induced host cell lysis and identification of a new tail gene.*):
  - `"Gene Y encodes a polypeptide with striking similarities to the family of holin proteins exemplified by gpS of phage lambda, and the Yam mutant displayed the expected properties of a holin mutant."`
- **PMID:23335412** (*Functional analysis of a class I holin, P2 Y.*):
  - `"Here, we used physiological and genetic approaches to show that Y exhibits the essential holin functional criteria, namely, allele-specific delayed-onset lethality and sensitivity to the energization of the membrane."`
  - `"However, Y holin function requires the integrity of its short cytoplasmic C-terminal domain, unlike for S105. Finally, instead of encoding a second translational product of Y as an antiholin, as shown for lambda S107, the P2 lysis cassette encodes another predicted membrane protein, LysA, which is shown here to have a Y-specific antiholin character."`

## Curation Decisions
- **Molecular Function**:
  - `GO:0140911` (`pore-forming activity`, IDA, `PMID:23335412`): **ACCEPT**
- **Biological Process**:
  - `GO:0044660` (`viral release via pore formation in host cell membrane`, IEA): **ACCEPT**
  - `GO:0031640` (`killing of cells of another organism`, IEA): **MODIFY** to `GO:0044660` (`viral release via pore formation in host cell membrane`).
- **Cellular Component**:
  - `GO:0020002` (`host cell plasma membrane`, IEA and ISS): **ACCEPT** both rows.
