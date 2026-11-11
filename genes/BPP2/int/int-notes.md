# Bacteriophage P2 Gene int (Integrase; UniProt P36932)

## Overview
Gene **int** of temperate myovirus *Escherichia phage P2* (`BPP2`) encodes a 337-amino-acid site-specific tyrosine recombinase (integrase; 38.2 kDa; `UniProt:P36932`) (`PMID:2676729`, `PMID:20627350`). During lysogenization, Int catalyzes integrative recombination between the phage attachment site `attP` and the *Escherichia coli* host chromosome attachment site `attB` (requiring host integration host factor, IHF), generating `attL` and `attR` junctions (`PMID:2676729`). During prophage induction/excision, Int works together with the phage excisionase Cox and host IHF to catalyze excisive recombination between `attL` and `attR` (`PMID:2676729`, `PMID:18284484`, `PMID:20627350`). Active site tyrosine is `Tyr-312` (`file:BPP2/int/int-uniprot.txt`).

## Key Literature & Experimental Evidence
- **PMID:2676729** (*Control of prophage integration and excision in bacteriophage P2: nucleotide sequences of the int gene and att sites.*):
  - `"Integration of bacteriophage P2 into the Escherichia coli host genome involves recombination between two specific attachment sites, attP and attB, one on the phage and the other on the host genome, respectively. The reaction is controlled by the product of the phage int gene, a basic polypeptide of about 37 kDa"`
  - `"An open reading frame coding for a polypeptide of 337 amino acids corresponds to the int gene."`
- **PMID:18284484** (*Bacteriophage P2 integrase: another possible tool for site-specific recombination in eukaryotic cells.*):
  - Demonstrated in vitro and in vivo site-specific recombination activity of purified P2 Int: `"We show that the Int protein catalyzes site-specific recombination using a human sequence in Escherichia coli and in vitro although not as efficiently as with the wild-type bacterial sequence"`
- **PMID:20627350** (*Identification of bases required for P2 integrase core binding and recombination.*):
  - Characterized core DNA binding and tyrosine recombinase activity: `"Temperate coliphage P2 integrates its genome into the host chromosome upon lysogenization via a site-specific recombination event mediated by an integrase belonging to the complex family of tyrosine recombinases."`

## Curation Decisions
- **Molecular Function**:
  - `GO:0003677` (`DNA binding`, IEA): **ACCEPT** (binds `attP`/`attB` core and arm DNA sites; `PMID:20627350`).
  - `GO:0016740` (`transferase activity`, IEA) and `GO:0016787` (`hydrolase activity`, IEA): **MODIFY** to `GO:0009037` (`tyrosine-based site-specific recombinase activity`).
  - `GO:0009037` (`tyrosine-based site-specific recombinase activity`): **NEW** supported by `PMID:18284484` and `PMID:20627350`.
- **Biological Process**:
  - `GO:0044826` (`viral genome integration into host DNA`, IEA): **ACCEPT**
  - `GO:0075713` (`establishment of integrated proviral latency`, IEA): **ACCEPT**
  - `GO:0006310` (`DNA recombination`, IEA) and `GO:0015074` (`DNA integration`, IEA): **MODIFY** to `GO:0044826` (`viral genome integration into host DNA`).
  - `GO:0046718` (`symbiont entry into host cell`, IEA): **REMOVE** (false-positive UniProt keyword `KW-1160` mapping; Int integrates viral DNA inside the host cell after genome entry and does not participate in virion entry across the host envelope).
  - `GO:0032359` (`provirus excision`): **NEW** supported by `PMID:2676729` (Int catalyzes both integration and excision of the P2 prophage).
- **Cellular Component**:
  - `GO:0030430` (`host cell cytoplasm`): **NEW** supported by `PMID:2676729`.
