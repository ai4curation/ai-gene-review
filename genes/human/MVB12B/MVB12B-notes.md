# MVB12B review notes

## Scope

MVB12B is reviewed in the PN ESCRT-I branch. PN entries without PMIDs were used as context only. MVB12B is a metazoan fourth subunit of ESCRT-I, closely related to MVB12A, with direct ESCRT-I and HIV-budding evidence from the MVB12 paper and direct MABP-domain lipid-binding evidence. Viral budding and virus maturation are supported but non-core contexts for this proteostasis review.

## Evidence synthesis

MVB12B is a metazoan ESCRT-I fourth subunit. UniProt describes it as a "Component of the ESCRT-I complex" and says it is "Required for the sorting of endocytic ubiquitinated cargos into multivesicular bodies" [file:human/MVB12B/MVB12B-uniprot.txt, "Component of the ESCRT-I complex"; file:human/MVB12B/MVB12B-uniprot.txt, "Required for the sorting of endocytic"]. UniProt also states that ESCRT-I "consists of TSG101, VPS28, a VPS37 protein" plus MVB12A or MVB12B, and that MVB12B interacts with TSG101, VPS28, VPS37B, and VPS37C [file:human/MVB12B/MVB12B-uniprot.txt, "which consists of TSG101, VPS28, a VPS37"; file:human/MVB12B/MVB12B-uniprot.txt, "Interacts with TSG101"; file:human/MVB12B/MVB12B-uniprot.txt, "Interacts with VPS28"; file:human/MVB12B/MVB12B-uniprot.txt, "Interacts with VPS37B"].

The main ESCRT-I/MVB12 paper directly supports MVB12B as an ESCRT-I subunit and viral-budding regulator. It reports that MVB12A and MVB12B "constitute the fourth class of metazoan ESCRT-I subunits", that soluble human ESCRT-I complexes contain one copy of each subunit type, and that MVB12 subunits associate with the TSG101-VPS37 core [PMID:18005716, "constitute the fourth class of metazoan ESCRT-I subunits"; PMID:18005716, "one copy of each of the four subunit types"; PMID:18005716, "associate with the core region of the binary TSG101-VPS37 complex"]. The same abstract says MVB12 depletion or overexpression inhibits HIV-1 infectivity and causes viral assembly defects [PMID:18005716, "MVB12 depletion and overexpression inhibit HIV-1 infectivity"; PMID:18005716, "aberrant virion morphologies and altered viral Gag protein processing"]. This supports viral budding/virus maturation as real but non-core host-pathogen contexts.

MVB12B has MABP-domain lipid-binding evidence. The MABP structural paper reports that MVB12A and MVB12B MABP domains bind acidic-lipid liposomes in vitro, that the MABP domain can autonomously localize to puncta and plasma membrane, and that ESCRT-I can act as a detector for acidic phospholipids and protein ligands [PMID:22232651, "MABP domains of the MVB12A and B subunits"; PMID:22232651, "bind in vitro to liposomes containing acidic lipids"; PMID:22232651, "coincidence detector for acidic phospholipids and protein ligands"]. This argues that broad `lipid binding` should be modified to `phospholipid binding` (GO:0005543).

PMID:20654576 compares post-translational regulation of MVB12A and MVB12B in ESCRT-I. Its abstract says MVB12B is ubiquitinated at Lys264 and Lys290, that these ubiquitinations increase after EGF stimulation, and that this regulates MVB12B stability and inclusion formation [PMID:20654576, "ubiquitination of Lys264 and Lys290 of MVB12B"; PMID:20654576, "increased upon EGF stimulation"; PMID:20654576, "led to the instability and inclusion of MVB12B"]. This supports EGF/ESCRT-I context and MVB12B post-translational regulation, but the cached abstract does not expose a ubiquitin-binding experiment. The `ubiquitin binding` row should therefore remain undecided pending full-text confirmation rather than being accepted from the cached abstract alone.

Nucleus, cytosol/cytoplasm, plasma membrane, vesicle, and extracellular exosome rows are supported localization/context rows but are not the core proteostasis function. The core function remains ESCRT-I-dependent endosomal sorting of ubiquitinated cargo and associated acidic-phospholipid membrane recognition.

## Falcon

Falcon deep research was started for MVB12B on 2026-06-02 but timed out after 600 seconds and did not produce a usable `MVB12B-deep-research-falcon.md` report. The review therefore relies on the local UniProt, GOA, cached-publication, Reactome, and PN-context evidence summarized above.

## Description cleanup note

The YAML `description` field was revised to keep it as a standalone biological summary. Project-specific curation framing moved here instead.

- Moved out of the YAML description: viral budding and virus maturation were described as direct ESCRT contexts but non-core for this proteostasis review.
