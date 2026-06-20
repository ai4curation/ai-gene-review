# VPS37D review notes

## Scope

VPS37D is reviewed in the PN ESCRT-I branch. PN entries without PMIDs were used as context only. The direct phagophore-closure evidence in this ESCRT-I neighborhood is VPS37A-specific, and the ESCRT-I structural/autophagy paper used a VPS37B-containing headpiece. For VPS37D, the supported core is ESCRT-I membership, endosomal MVB cargo sorting, and late-endosome/endosome-membrane localization.

## Evidence synthesis

VPS37D is a VPS37-family ESCRT-I subunit, but it has less direct functional literature than VPS37A, VPS37B, and VPS37C. UniProt describes it as a "Component of the ESCRT-I complex" and says it is "Required for the sorting of endocytic ubiquitinated cargos into multivesicular bodies" [file:human/VPS37D/VPS37D-uniprot.txt, "Component of the ESCRT-I complex"; file:human/VPS37D/VPS37D-uniprot.txt, "Required for the sorting of endocytic"]. UniProt also states that ESCRT-I "consists of TSG101, VPS28, a VPS37 protein" and that VPS37D interacts with TSG101 and MVB12A [file:human/VPS37D/VPS37D-uniprot.txt, "which consists of TSG101, VPS28, a VPS37"; file:human/VPS37D/VPS37D-uniprot.txt, "Interacts with TSG101 and MVB12A"]. These support ESCRT-I complex membership and MVB sorting, but the review should not overstate VPS37D-specific experimental testing.

The original human ESCRT-I paper identified a family of human VPS37 proteins, including VPS37D, by sequence similarity to yeast Vps37p, but the detailed functional experiments were on VPS37B [PMID:15218037, "proteins (VPS37A-D) that share weak but significant sequence similarity"; PMID:15218037, "Detailed studies produced four lines of evidence that human VPS37B is a Vps37p ortholog"]. Thus PMID:15218037 supports VPS37D family membership but is not direct VPS37D functional evidence.

Shared ESCRT-I composition papers support the complex architecture. PMID:18005716 says human ESCRT-I plays roles in HIV budding and endosomal protein sorting and that all ESCRT-I complexes contain TSG101, VPS28, and VPS37 [PMID:18005716, "plays essential roles in HIV budding and endosomal protein sorting"; PMID:18005716, "TSG101, VPS28, and VPS37"]. PMID:22405001 says UBAP1 coassembles in a stable complex with Vps23/TSG101, VPS28, and VPS37 [PMID:22405001, "complex with Vps23/TSG101, VPS28, and VPS37"]. These support a VPS37D ESCRT-I complex annotation when combined with UniProt/ComplexPortal, but they do not provide VPS37D-specific autophagy or membrane-scission assays.

Structural ESCRT-I evidence should not be over-transferred to VPS37D. PMID:32424346 determined a human ESCRT-I headpiece "comprising TSG101-VPS28-VPS37B-MVB12A" and found that ESCRT-I has a scaffolding/mechanical role in reverse-topology scission [PMID:32424346, "comprising TSG101-VPS28-VPS37B-MVB12A"; PMID:32424346, "ESCRT-I is not merely a bridging adaptor"]. This supports the general ESCRT-I mechanism, but for VPS37D it should not be treated as direct support for `membrane fission` or autophagosome closure.

The `macroautophagy` row should be treated cautiously. PMID:20588296 says ESCRT-III-mediated neck cleavage is crucial for MVBs, viral budding, cytokinesis, and "probably, autophagy", and notes that direct ESCRT neck closure in autophagy remained unresolved [PMID:20588296, "viral budding, cytokinesis and, probably, autophagy"; PMID:20588296, "direct neck closure reaction in autophagy"]. The direct mammalian phagophore-closure paper identifies VPS37A, not VPS37D, as the ESCRT-I subunit needed for phagophore closure [PMID:31519728, "identify the ESCRT-I subunit VPS37A as a critical component"; PMID:31519728, "required for autophagosome completion"]. This argues against transferring an autophagosome assembly or macroautophagy core annotation to VPS37D.

The generic `protein binding` row comes from a broad interactome annotation and is not informative for VPS37D function. Extracellular exosome and viral budding rows are supported as ESCRT-I contexts but should remain non-core for this proteostasis review.

## Falcon

Falcon deep research was started for VPS37D on 2026-06-02 but timed out after 600 seconds and did not produce a usable `VPS37D-deep-research-falcon.md` report. The review therefore relies on the local UniProt, GOA, cached-publication, Reactome, and PN-context evidence summarized above.
