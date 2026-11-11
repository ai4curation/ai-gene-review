# Curation Notes for *Variovorax paradoxus* S110 `fetP` (`C5CNX5`, `FETP_VARPS`, `Vapar_2982`)

## Overview
- **UniProt Accession:** `C5CNX5` (`FETP_VARPS`)
- **Ordered Locus Name:** `Vapar_2982`
- **Gene Symbol:** `fetP`
- **Organism:** *Variovorax paradoxus* S110 (`NCBITaxon:543728`)
- **Protein Function:** Probable cytosolic $\text{Fe}^{2+}$-trafficking protein (`FetP` / `YggX`, 90 aa) predicted via HAMAP rule `MF_00686` (`InterPro:IPR007457`) to mediate intracellular iron transactions between iron acquisition and iron-requiring processes such as synthesis and repair of `[Fe-S]` clusters.
- **Disambiguation Note:** `Vapar_2982` (`C5CNX5`) bears the entry name `FETP_VARPS` via the YggX Fe(2+)-trafficking family rule (`HAMAP-Rule:MF_00686`) and is distinct from the uncurated periplasmic FetP-like cupredoxin (`Vapar_3862` / `C5CUI1`) encoded adjacent to the variobactin siderophore locus.

## Literature & Domain Evidence
1. **Genomic Context in *Variovorax paradoxus* S110 (`PMID:21183664`, `UniProtKB:C5CNX5`):**
   - Encoded at locus `Vapar_2982` on Chromosome 1 of *Variovorax paradoxus* S110 ([PMID:21183664 "The complete genome sequence of V. paradoxus S110 is composed of 6,754,997 bp with 6,279 predicted protein-coding sequences within two circular chromosomes."]), adjacent to the alkanesulfonate utilization cluster (`Vapar_2976` `ssuD`).
2. **Conserved YggX/FetP Domain Architecture & Essential `Cys7` (`UniProtKB:C5CNX5`, `PMID:12670952`, `PMID:11416172`):**
   - `C5CNX5` (`FETP_VARPS`) is a 90-aa Swiss-Prot reviewed entry curated under `HAMAP:MF_00686` (`InterPro:IPR007457`, `Pfam:PF04362`, `PANTHER:PTHR36965:SF1`), annotated with `KW   Iron.`, `CC -!- SIMILARITY: Belongs to the Fe(2+)-trafficking protein family. {ECO:0000255|HAMAP-Rule:MF_00686}.`, and `CC -!- FUNCTION: Could be a mediator in iron transactions between iron acquisition and iron-requiring processes, such as synthesis and/or repair of Fe-S clusters in biosynthetic enzymes. {ECO:0000255|HAMAP-Rule:MF_00686}.` (`UniProtKB:C5CNX5`).
   - Direct inspection of the `C5CNX5` sequence (`MARMVQCIKL...` in `SQ`) confirms conservation of `Cys7`, the invariant N-terminal cysteine demonstrated in *Salmonella enterica* YggX to be essential for intracellular $\text{Fe}^{2+}$ chelation/trafficking and protection against Fenton-mediated hydroxyl radical DNA damage ([PMID:12670952 "The ability of purified YggX to protect DNA from Fenton chemistry mediated damage in vitro and to decrease the concentration of Fe(II) ions in solution available for chelation provided a framework for the interpretation of data obtained from in vivo experiments."]) and superoxide inactivation of `[Fe-S]` clusters ([PMID:11416172 "Here it is shown that elevated levels of the YggX protein increase the resistance of Salmonella enterica to superoxide stress, reverse enzymatic defects attributed to oxidized [Fe-S] clusters, and decrease the spontaneous mutation frequency."]).

## Review of Existing GOA Annotations
- `GO:0005506` (`iron ion binding`, IEA via `GO_REF:0000120`: `InterPro:IPR007457`, `InterPro:IPR036766`, `UniRule:UR000033441`) -> **ACCEPT** (core molecular function supported by `HAMAP:MF_00686` / `InterPro:IPR007457` YggX-family classification, `KW Iron.`, and conservation of the essential `Cys7` residue in `C5CNX5`, `PMID:12670952`).
- `GO:0005829` (`cytosol`, IEA via TreeGrafter `GO_REF:0000118` / `PANTHER:PTN002863974`) -> **ACCEPT** (90-aa soluble cytoplasmic YggX-family protein lacking signal peptides or transmembrane helices, `UniProtKB:C5CNX5`).
- `GO:0034599` (`cellular response to oxidative stress`, IEA via TreeGrafter `GO_REF:0000118` / `PANTHER:PTN002863974`) -> **KEEP_AS_NON_CORE** (downstream cellular protection against superoxide and Fenton-mediated hydroxyl radical damage resulting from cytosolic $\text{Fe}^{2+}$ trafficking, characterized in *S. enterica* YggX in `PMID:11416172` and `PMID:12670952`).

## Proposed New Annotations
- `GO:0006879` (`intracellular iron ion homeostasis`) — `involved_in` (`IC`), inferred from `HAMAP:MF_00686` / `InterPro:IPR007457` (`CC -!- FUNCTION` in `UniProtKB:C5CNX5`).
