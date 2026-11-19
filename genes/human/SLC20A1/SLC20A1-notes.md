# SLC20A1 (PiT1 / GLVR1) curation notes

## Identity
UniProt Q8WUM9, "Sodium-dependent phosphate transporter 1"; HGNC SLC20A1; synonyms GLVR1, PIT1. SLC20/PiT family (type III Na-Pi cotransporter), multi-pass plasma-membrane protein, PANTHER PTHR11101.

## Core transport function
Originally cloned as the gibbon ape leukaemia virus receptor and then shown to be a phosphate symporter: [PMID:8041748 "Cell-surface receptors for gibbon ape leukemia virus and amphotropic murine retrovirus are inducible sodium-dependent phosphate symporters"]. Curated UniProt FUNCTION: Na-phosphate symporter, preferentially monovalent phosphate, ~2 Na+ per Pi [file:human/SLC20A1/SLC20A1-uniprot.txt CC:FUNCTION "Sodium-phosphate symporter which preferentially transports"; ECO:0000269 over PubMed:11009570/16790504/17494632/19726692/7929240/8041748]. Plasma membrane [CC:SUBCELLULAR LOCATION "Cell membrane"]. Core MF GO:0005436, core BP GO:0035435.

## Kinetics caveat (affects GO:0005316 high-affinity call)
UniProt records two conflicting phosphate Km values for PiT1: 24.1 uM (PubMed:7929240/8041748, the 1994 "high-affinity" framing) and 322.5 uM (PubMed:16790504, the careful PiT1-vs-PiT2 comparison). The 13-fold discrepancy straddles the high/low-affinity boundary, so the "high-affinity" sub-classification (GO:0005316) is not robustly supported and is marked over-annotated; the substrate-generic GO:0005436 is the solid term. (PiT2 Km 163.5 uM; carries no GO:0005316.)

## Dual function: transport vs retroviral receptor
The phosphate-transport and gammaretroviral-receptor functions are experimentally separable [PMID:12205090 "it is possible to uncouple transport and receptor functions of a type III NaP(i) cotransporter"]. The GOA MF GO:0038023 signaling receptor activity (TAS PMID:8041748) is the wrong MF for a viral entry receptor -> MODIFY to GO:0001618 virus receptor activity (lateral correction; GO:0001618 is NOT an is_a descendant of GO:0038023 per go.db). Non-core incidental activity.

## Other rows
- GO:0008283 cell proliferation: transport-independent role, IDA PubMed:19726692 -> KEEP_AS_NON_CORE (moonlighting).
- GO:0043123 positive regulation of canonical NF-kB (HMP PMID:12761501): a cDNA-overexpression luciferase-reporter screen hit -> MARK_AS_OVER_ANNOTATED (screen artifact; precedent SLC35B2, C18orf32).
- GO:0006796 phosphate-containing compound metabolic process (TAS) -> MARK_AS_OVER_ANNOTATED (PiT1 transports, does not metabolize phosphate).
- Broad substrate-named parents GO:0005315 (phosphate TMT activity) and GO:0006817 (phosphate ion transport) -> KEEP_AS_NON_CORE (not TOO_GENERAL per the 2026-11-14 ruling; they name their substrate). GO:0016020 membrane MODIFY->plasma membrane. Sodium co-transport GO:0035725/GO:0006814 KEEP_AS_NON_CORE.
- propagation_review: the MF IBA (GO:0005436) is placed at PANTHER PTN008512340 (WITH/FROM self-grounds via Q8WUM9/Q08357); the CC/BP IBA rows are placed at PTN000120970.
Batch 26.
