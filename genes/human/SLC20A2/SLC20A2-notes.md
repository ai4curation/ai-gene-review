# SLC20A2 (PiT2 / GLVR2) curation notes

## Identity
UniProt Q08357, "Sodium-dependent phosphate transporter 2"; HGNC SLC20A2; synonyms GLVR2, PIT2. SLC20/PiT family, multi-pass plasma-membrane protein, PANTHER PTHR11101.

## Core transport function
Na-phosphate symporter, preferentially monovalent phosphate, ~2 Na+ per Pi [file:human/SLC20A2/SLC20A2-uniprot.txt CC:FUNCTION "Sodium-phosphate symporter which preferentially transports"]. The symporter MF is grounded in many disease loss-of-function studies: [PMID:22327515 "significantly impaired phosphate transport activity for all assayed PiT2 mutants"; encodes "the type III sodium-dependent phosphate transporter 2 (PiT2), in IBGC-affected families"] and conserved-residue mutagenesis [PMID:15955065 "highly conserved aspartic acids critical for sodium-dependent phosphate transport function of human PiT2"]. Core MF GO:0005436, core BP GO:0035435, at the plasma membrane [CC:SUBCELLULAR LOCATION "Cell membrane"].

## Disease / selectivity puzzle
SLC20A2 loss-of-function causes primary familial brain calcification (familial idiopathic basal ganglia calcification) [PMID:22327515]. Open BIOLOGY question (-> suggested_questions/experiments/knowledge_gaps): why does losing a broadly expressed housekeeping Na-Pi symporter give region-selective brain calcification? The CSF-phosphate role is inferred from mouse (UniProtKB:Q80UP8, By similarity) with no human GOA row.

## Locations
Apical/brush-border (GO:0016324, GO:0031526) rest on ISS from the rat ortholog (UniProtKB:Q63488); Q08357 has no human brush-border statement [CC:SUBCELLULAR LOCATION "Apical cell membrane"]. Retained as plasma-membrane sub-locations on by-similarity evidence; NOT listed in core_functions.locations (apical is ISS-only and PiT2's principal site, the brain, is not polarized epithelium).

## Dual function and other rows
Gammaretroviral entry receptor (amphotropic MuLV etc.) [CC:FUNCTION (Microbial infection) "Functions as a retroviral receptor and"; GO:0001618 IMP PubMed:12205090/15955065] -> KEEP_AS_NON_CORE; transport/receptor functions are separable [PMID:12205090 "it is possible to uncouple transport and receptor functions of a type III NaP(i) cotransporter"]. GO:0038023 signaling receptor activity (TAS PMID:8302848) -> MODIFY to GO:0001618 (already carried by IMP). GO:0046718 symbiont entry KEEP_AS_NON_CORE. GO:0030501 bone mineralization (phosphate supply, indirect) KEEP_AS_NON_CORE. GO:0070062 exosome (HDA) KEEP_AS_NON_CORE. Broad substrate-named parents GO:0005315/GO:0006817 KEEP_AS_NON_CORE (not TOO_GENERAL per the 2026-11-14 ruling); GO:0016020 MODIFY->plasma membrane; GO:0035725 sodium co-transport KEEP_AS_NON_CORE. Batch 26.
