# Curation Notes: Bacteriophage T4 `adfA` (UniProt P39229)

## Identity and Nomenclature
- **Gene symbol:** `adfA` (synonyms: `61.2`, `y01L`)
- **UniProt accession:** `P39229` (`ADFA_BPT4`)
- **Protein name:** Anti-DarT factor A
- **Length:** 208 AA (24,332 Da)
- **Organism:** Enterobacteria phage T4 (`NCBITaxon:10665`)

## Summary of Experimental Evidence
- **Discovery of `adfA` (gp61.2) as an Anti-DarT Counter-Defense Factor:** LeRoux et al. 2022 (*Nature Microbiology*; DOI `10.1038/s41564-022-01153-5`) showed that bacterial DarTG toxin-antitoxin systems defend against bacteriophages by ADP-ribosylating viral DNA via the DNA ADP-ribosyltransferase toxin DarT, blocking phage DNA replication. Experimental evolution of the T-even phage RB69 on DarTG1-expressing *Escherichia coli* selected for escape mutations in gene `61.2` (specifically `R164H` and `R164S`), which was renamed `adfA` ("anti-DarT factor A"). Bacteriophage T4 naturally encodes histidine at the equivalent position in its `adfA` (`61.2`) homolog (`P39229`), and ectopic expression of either RB69 `adfA(R164H)` or the T4 `adfA` homolog improved RB69 plating efficiency on DarTG1-containing hosts and prevented DarT-mediated DNA ADP-ribosylation.
- **Mechanism and Redundancy in T4:** AdfA (`Pfam:PF23813`, `InterPro:IPR055608`) lacks catalytic domains and functions as a direct antitoxin-like protein inhibitor that associates with DarT to block viral DNA ADP-ribosylation (`Plays a role in counteracting the host DarT defense system. {ECO:0000250|UniProtKB:Q7Y5A4}.`). Follow-up studies (Johannesman et al. 2025 preprint) indicate that while AdfA interacts with DarT1, T4 also encodes a NADAR-family enzymatic DNA ADP-ribosylglycohydrolase (AdfN), making `adfA` part of a multi-layered anti-DarTG counter-defense arsenal in T4.

## Review of Existing GO Annotations
1. `GO:0052170` (`symbiont-mediated suppression of host innate immune response`, IEA `GO_REF:0000043`): **ACCEPT**. Because GO does not currently have a more specific child term for suppression of the bacterial DarTG toxin-antitoxin defense system, `GO:0052170` is the most specific available biological process term describing AdfA's role in counteracting the host DarT innate anti-phage defense system.
2. `GO:0052031` (`symbiont-mediated perturbation of host defense response`, IEA `GO_REF:0000043`): **MODIFY** to `GO:0052170` (`symbiont-mediated suppression of host innate immune response`), which is already annotated to the gene and more specific (`suppression` rather than general `perturbation`).
