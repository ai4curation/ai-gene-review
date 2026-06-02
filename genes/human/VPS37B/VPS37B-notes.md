# VPS37B review notes

## Scope

VPS37B is reviewed in the PN ESCRT-I branch. PN entries without PMIDs were used as context only. The direct phagophore-closure evidence in this ESCRT-I neighborhood is VPS37A-specific; for VPS37B the supported core is ESCRT-I membership, endosomal MVB cargo sorting, and ESCRT-I membrane-remodeling context.

## Evidence synthesis

VPS37B is a VPS37-family ESCRT-I subunit. UniProt describes it as a "Component of the ESCRT-I complex" and says it is "Required for the sorting of endocytic ubiquitinated cargos into multivesicular bodies" [file:human/VPS37B/VPS37B-uniprot.txt, "Component of the ESCRT-I complex"; file:human/VPS37B/VPS37B-uniprot.txt, "Required for the sorting of endocytic"]. UniProt also states that the ESCRT-I complex "consists of TSG101, VPS28, a VPS37 protein" and that VPS37B interacts with TSG101, VPS28, MVB12A, and MVB12B [file:human/VPS37B/VPS37B-uniprot.txt, "which consists of TSG101, VPS28, a VPS37"; file:human/VPS37B/VPS37B-uniprot.txt, "Interacts with TSG101, VPS28, MVB12A and MVB12B"]. This supports accepting ESCRT-I complex and MVB sorting rows.

The core VPS37B experimental paper defines it as a human Vps37 ortholog in ESCRT-I. The abstract reports that "VPS37A and VPS37B bind TSG101", that "TSG101 and VPS28 co-immunoprecipitated with VPS37B-FLAG", that the proteins "comigrated together in soluble complexes of the correct size for human ESCRT-I", and that VPS37B becomes trapped on aberrant endosomal compartments in the presence of ATPase-defective VPS4A [PMID:15218037, "VPS37A and VPS37B bind TSG101"; PMID:15218037, "TSG101 and VPS28 co-immunoprecipitated with VPS37B-FLAG"; PMID:15218037, "complexes of the correct size for human ESCRT-I"; PMID:15218037, "VPS37B became trapped on aberrant endosomal compartments"]. This supports endosome/endosome membrane localization and ESCRT-I complex membership. The same paper also supports viral budding, but that is a non-core host-pathogen context for this proteostasis review.

Structural ESCRT-I evidence supports VPS37B as part of the ESCRT-I headpiece. The human ESCRT-I structural paper describes the headpiece as "comprising TSG101-VPS28-VPS37B-MVB12A" and says ESCRT-I is "not merely a bridging adaptor" but forms assemblies that template membrane remodeling [PMID:32424346, "comprising TSG101-VPS28-VPS37B-MVB12A"; PMID:32424346, "ESCRT-I is not merely a bridging adaptor"]. This supports accepting membrane fission as a complex-level ESCRT-I remodeling annotation, but it does not make VPS37B itself a directly tested autophagosome-closure factor.

The `macroautophagy` rows should be treated cautiously. PMID:20588296 says ESCRT-III-mediated neck cleavage is important for MVBs, viral budding, cytokinesis, and "probably, autophagy" [PMID:20588296, "viral budding, cytokinesis and, probably, autophagy"]. The direct mammalian phagophore-closure study identifies VPS37A as the VPS37 subunit required for phagophore closure and says VPS37A is "required for autophagosome completion but dispensable for ESCRT-I complex formation" [PMID:31519728, "the ESCRT-I subunit VPS37A as a critical component for phagophore closure"; PMID:31519728, "required for autophagosome completion but dispensable for ESCRT-I complex formation"]. This argues against transferring the autophagosome assembly conclusion to VPS37B without additional evidence.

VPS37B and VPS37C have a secondary calcium-dependent ALIX/ALG-2 interaction context. PMID:23924735 reports that VPS37B and VPS37C interact with ALG-2 more strongly than TSG101 and that ALG-2 acts as a Ca2+-dependent adaptor bridging ALIX and ESCRT-I [PMID:23924735, "VPS37B and VPS37C appeared to interact with ALG-2"; PMID:23924735, "Ca²⁺-dependent adaptor protein that bridges ALIX and ESCRT-I"]. This supports keeping calcium-dependent protein binding as non-core rather than making it the main molecular function.

Generic `protein binding` rows are over-annotated. The meaningful curation targets are ESCRT-I complex membership, MVB/endosomal sorting, and ESCRT-I membrane remodeling. Viral budding, viral release, positive regulation of viral budding, exosome, plasma membrane, cytoplasm, and midbody rows are supported contexts but should remain non-core for the proteostasis review.

## Falcon

Falcon deep research was started for VPS37B on 2026-06-02 but timed out after 600 seconds and did not produce a usable `VPS37B-deep-research-falcon.md` report. The review therefore relies on the local UniProt, GOA, cached-publication, and PN-context evidence summarized above.
