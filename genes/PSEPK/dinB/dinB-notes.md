# dinB (DNA polymerase IV / Pol IV) — Pseudomonas putida KT2440

UniProt: Q88NK4 (DPO4_PSEPK), gene `dinB` (synonym `dinP`), locus PP_1203, 354 aa.
Evidence level PE 3 (Inferred from homology). Annotation governed by HAMAP-Rule MF_01113 (DNApol_IV).

## FUNCTION
DinB is the Y-family translesion DNA polymerase Pol IV.

[UniProt "Poorly processive, error-prone DNA polymerase involved in untargeted mutagenesis."]
[UniProt "Copies undamaged DNA at stalled replication forks, which arise in vivo from mismatched or misaligned primer ends."]
[UniProt "These misaligned primers can be extended by PolIV."]
[UniProt "Exhibits no 3'-5' exonuclease (proofreading) activity."]
[UniProt "May be involved in translesional synthesis, in conjunction with the beta clamp from PolIII."]

## CATALYTIC ACTIVITY
[UniProt "Reaction=DNA(n) + a 2'-deoxyribonucleoside 5'-triphosphate = DNA(n+1) + diphosphate"]
EC 2.7.7.7 (DNA-directed DNA polymerase). Template-directed, primer-extending nucleotidyltransferase.
Catalytic active site residue: ACT_SITE 106. Substrate discrimination residue: SITE 15.

## COFACTOR
[UniProt "Name=Mg(2+); Xref=ChEBI:CHEBI:18420"]
[UniProt "Binds 2 magnesium ions per subunit."]
Mg2+ binding residues: BINDING 10 and BINDING 105 (two-metal-ion mechanism).

## SUBUNIT / LOCALIZATION
[UniProt "Monomer."]
[UniProt "Cytoplasm"]

## FAMILY / DOMAINS
[UniProt "Belongs to the DNA polymerase type-Y family."]
UmuC domain (residues 6..187); InterPro IPR001126 (UmuC), IPR022880 (DNApol_IV),
IPR050116 (DNA_polymerase-Y), little-finger domain (IPR017961/IPR036775).
eggNOG COG0389; PANTHER PTHR11076 (UmuC/DinB family).

## Annotation interpretation notes
- Core MF: DNA-directed DNA polymerase activity (GO:0003887, EC 2.7.7.7); damaged DNA binding (GO:0003684).
- Core BP: DNA repair (GO:0006281); error-prone translesion synthesis (GO:0042276); SOS response (GO:0009432).
- Broad/parent terms present alongside specific terms:
  - GO:0034061 DNA polymerase activity is the parent of GO:0003887 DNA-directed DNA polymerase activity (specific present -> over-annotated).
  - GO:0000287 magnesium ion binding and GO:0003677 DNA binding are generic cofactor/binding terms; damaged DNA binding (GO:0003684) and the polymerase activity already capture the informative function. Mg2+ is the catalytic cofactor (two-metal mechanism) so magnesium ion binding is supportable but non-core relative to the polymerase activity.
  - GO:0006259 DNA metabolic process is a broad parent of DNA repair / DNA replication.
  - GO:0006261 DNA-templated DNA replication: Pol IV is not a replicative polymerase; its role is lesion bypass/untargeted mutagenesis at stalled forks rather than bulk genome replication. The UniRule electronic mapping derives this from the generic polymerase reaction, but DNA repair / translesion synthesis are the biologically accurate BP terms. Treated as over-annotation/non-core.
  - Localization: cytoplasm (GO:0005737) per UniProt SUBCELLULAR LOCATION; cytosol (GO:0005829) is the TreeGrafter equivalent. Both consistent.

## Provenance
All molecular details from `file:PSEPK/dinB/dinB-uniprot.txt` (HAMAP-Rule MF_01113 propagated annotations).
Genome reference: PMID:12534463 (Nelson et al. 2002, complete genome of P. putida KT2440) — establishes the gene locus only, no Pol IV functional characterization.
