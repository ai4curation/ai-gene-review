# Deep research on crcB / fluC

Attempted `deep-research-falcon PSEPK crcB` on 2026-03-21, but the Falcon client did not return output in this environment before timeout/interruption. The summary below is a manual fallback based on UniProt and primary literature.

## Identity

The requested `crcB` gene in *Pseudomonas putida* KT2440 corresponds to UniProt `Q88FT1`, where the standard gene symbol is `fluC` and `crcB` is listed as a synonym; the ordered locus tag is `PP_4001` [UniProt:Q88FT1 "GN   Name=fluC"; "GN   Synonyms=crcB"; "GN   OrderedLocusNames=PP_4001"].

## Core function

FluC/CrcB proteins are fluoride-specific membrane export proteins. Family-level work identified Fluc proteins as fluoride-specific ion channels rather than generic transporters, and structural work showed a dual-topology, double-barrelled channel architecture [PMID:23991286 "A family of fluoride-specific ion channels with dual-topology architecture"; PMID:26344196 "Crystal structures of a double-barrelled fluoride ion channel"].

UniProt annotates Q88FT1 explicitly as a fluoride-specific ion channel, with the physiological reaction `fluoride(in) = fluoride(out)` and with the physiological role of lowering intracellular fluoride toxicity [UniProt:Q88FT1 "Fluoride-specific ion channel. Important for reducing fluoride concentration in the cell, thus reducing its toxicity."; "Reaction=fluoride(in) = fluoride(out)"].

## Localization and mechanism

Q88FT1 is a small 124 aa multi-pass inner-membrane protein with four predicted transmembrane helices [UniProt:Q88FT1 "Cell inner membrane"; "Multi-pass membrane protein"; "TRANSMEM        1..21"; "TRANSMEM        37..57"; "TRANSMEM        69..89"; "TRANSMEM        99..119"].

Although Na(+) is associated with the family, UniProt states that sodium is not transported and instead has an essential structural role; this is consistent with family-level structural work on Fluc channels [UniProt:Q88FT1 "Na(+) is not transported, but it plays an essential structural role"; PMID:31945374 "An interfacial sodium ion is an essential structural feature of Fluc family fluoride channels"].

## Pseudomonas putida-specific evidence

The strongest organism-specific evidence comes from the 2022 *Environmental Microbiology* study on the CrcB transporter in KT2440. The article title itself identifies CrcB as the transporter mediating the fluoride stress response in *P. putida*, and the paper reports that loss of the exporter causes intracellular fluoride accumulation [PMID:35726888 "Role of the CrcB transporter of Pseudomonas putida in the multi-level stress response elicited by mineral fluoride"; PMID:35726888 "knocking out the gene encoding this exporter led to a significant intracellular accumulation"].

Taken together, the organism-specific phenotype data and the family-level structural/function data strongly support the GO core of:

- molecular function: fluoride channel activity
- biological process: fluoride transmembrane transport and cellular detoxification of fluoride
- cellular component: plasma membrane / inner membrane

## Curation implications

For GO review purposes, `GO:0062054 fluoride channel activity` is the most precise molecular-function term. `GO:1903425 fluoride transmembrane transporter activity` is directionally correct but broader and therefore likely over-annotated relative to the channel-specific term. `GO:0016020 membrane` is also broader than the more informative `GO:0005886 plasma membrane`.
