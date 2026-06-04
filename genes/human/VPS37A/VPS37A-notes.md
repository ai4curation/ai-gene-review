# VPS37A review notes

## Scope

VPS37A is reviewed in the PN autophagophore sealing branch as an ESCRT-I component. PN entries without PMIDs were used as context only. Unlike VPS28, VPS37A has direct mammalian phagophore-closure evidence: the VPS37A PUEV-containing isoform recruits ESCRT machinery to phagophores and is required for autophagosome completion.

## Evidence synthesis

VPS37A is a core ESCRT-I subunit. UniProt describes it as a "Component of the ESCRT-I complex" and says it is "Required for the sorting of endocytic ubiquitinated cargos into multivesicular bodies" [file:human/VPS37A/VPS37A-uniprot.txt, "Component of the ESCRT-I complex"; file:human/VPS37A/VPS37A-uniprot.txt, "Required for the sorting of endocytic ubiquitinated cargos into multivesicular bodies"]. UniProt also states that ESCRT-I consists of "TSG101, VPS28, a VPS37 protein" and that VPS37A interacts with TSG101, VPS28, and HGS [file:human/VPS37A/VPS37A-uniprot.txt, "which consists of TSG101, VPS28, a VPS37"; file:human/VPS37A/VPS37A-uniprot.txt, "Interacts with TSG101, VPS28 and HGS"]. These lines support ESCRT-I complex membership and MVB/endosomal cargo-sorting annotations.

The original HCRP1/hVps37A study supports the endosomal sorting role. Its abstract reports that HCRP1/hVps37A "interacts with Tsg101, hVps28, and their upstream regulator Hrs", "cofractionates with Tsg101 and hVps28", "colocalizes with hVps28 on LAMP1-positive endosomes", and that HCRP1 depletion "retards epidermal growth factor (EGF) receptor degradation" [PMID:15240819, "interacts with Tsg101, hVps28, and their upstream regulator Hrs"; PMID:15240819, "cofractionates with Tsg101 and hVps28"; PMID:15240819, "colocalizes with hVps28 on LAMP1-positive endosomes"; PMID:15240819, "retards epidermal growth factor (EGF) receptor degradation"]. The same abstract concludes that HCRP1 is "a subunit of mammalian ESCRT-I" and that its function is "essential for lysosomal sorting of EGF receptors" [PMID:15240819, "a subunit of mammalian ESCRT-I"; PMID:15240819, "essential for lysosomal sorting of EGF receptors"].

The PN-specific autophagy term should be autophagosome assembly/phagophore closure rather than broad macroautophagy. The phagophore closure paper identifies "the ESCRT-I subunit VPS37A as a critical component for phagophore closure", shows that VPS37A localizes on the phagophore through its N-terminal PUEV domain, and says this domain is "required for autophagosome completion but dispensable for ESCRT-I complex formation" [PMID:31519728, "the ESCRT-I subunit VPS37A as a critical component for phagophore closure"; PMID:31519728, "VPS37A localizes on the phagophore"; PMID:31519728, "required for autophagosome completion but dispensable for ESCRT-I complex formation"]. It also reports that loss of VPS37A abrogates phagophore recruitment of VPS28 and CHMP2A and that VPS37A coordinates ESCRT machinery for phagophore closure [PMID:31519728, "loss of VPS37A abrogates the phagophore recruitment"; PMID:31519728, "VPS37A coordinates the recruitment of a unique set of ESCRT machinery components for phagophore closure"].

Protein binding rows should not be accepted as informative molecular functions. They should be marked over-annotated in favor of ESCRT-I complex membership, MVB sorting, and autophagosome assembly. Viral budding rows are supported ESCRT contexts but are non-core for the proteostasis review. Nuclear/nucleoplasm rows are supported in UniProt as localization observations but should be non-core relative to ESCRT-I endosomal and phagophore functions.

## Falcon

Falcon deep research was started for VPS37A on 2026-06-02 but timed out after 600 seconds and did not produce a usable report. The review therefore relies on UniProt, cached primary literature, and PN context rather than Falcon output.

## Description cleanup note

The YAML `description` field was revised to keep it as a standalone biological summary. Project-specific curation framing moved here instead.

- Moved out of the YAML description: the prior wording described VPS37A's phagophore-closure role as PN-relevant.
