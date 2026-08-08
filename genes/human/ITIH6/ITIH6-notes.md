# ITIH6 review notes

## 2026-07-18 — retrieval and research boundary

- `just fetch-gene human ITIH6` retrieved reviewed UniProt Q6UXX5 and 11 current GOA rows grouped into four review entries.
- `just fetch-gene-pmids human ITIH6` confirmed one PMID-backed GOA source, PMID:32296183.
- The configured Falcon/Edison deep-research request failed with HTTP 402, and the `perplexity-lite` fallback failed with HTTP 401 because provider quota was exhausted. No provider-named report was created; manual synthesis is recorded in `ITIH6-deep-research-manual.md`.
- Additional primary sources were cached manually: PMID:41109368 (the first ITIH6-focused characterization), PMID:12975309 (the cDNA discovery initiative cited by UniProt), and PMID:2476436 (direct biochemical resolution of inhibitory versus noninhibitory inter-alpha-inhibitor chains).
- The repository cache contains only the abstract of PMID:41109368. Its open-access full text was also checked through the publisher-author manuscript indexed by RWTH Aachen/ResearchGate (DOI:10.1016/j.ijbiomac.2025.148360); full-text-only conclusions are documented here and in the manual synthesis rather than quoted as cached-PMID substrings in the review YAML.

## Protein identity and architecture

- ITIH6 is a 1,313-aa human ITIH-family precursor with a predicted signal peptide at residues 1–23, VIT domain at 24–150, vWA domain at 283–469, and an ITI-heavy-chain C-terminal domain near residues 1,117–1,296. UniProt predicts secretion but annotates only signal-peptide removal; it does not annotate a mature heavy chain, a C-terminal propeptide, bikunin linkage, or an experimentally verified processing site.
- The 2025 primary study describes ITIH6 as previously uncharacterized and most closely related to ITIH5. [PMID:41109368 Characterization of ITIH6, a novel inter-α-inhibitor family member with prognostic significance in cholangiocarcinoma, "ITIH6 is most closely related to ITIH5, forming a separate subfamily"]
- ITIH6 has an unusually expanded central region between the vWA and ITI_HC_C domains. [PMID:41109368, "also harbors a large central region between the vWA domain and the C-terminus that is unique to ITIH6"]
- Full-text sequence analysis identifies a conserved candidate cleavage motif at residues 1,097–1,102 (`DPHFVI`), upstream of the ITI_HC_C domain. This supports structural plausibility of heavy-chain-like processing, but the paper does not experimentally map cleavage or a terminal Asp linkage.

## Protease-inhibitor annotation

- The `serine-type endopeptidase inhibitor activity` IEA is an automated InterPro/domain-family inference and is not an activity of an ITIH heavy chain. Direct biochemical fractionation of human inter-alpha-inhibitor showed one shared inhibitory 30-kDa chain and explicitly described its heavy chains as noninhibitory. [PMID:2476436 Analysis of inter-alpha-trypsin inhibitor and a novel trypsin inhibitor, pre-alpha-trypsin inhibitor, from human plasma, "Inter-alpha-trypsin inhibitor contains noninhibitory heavy chains of 65,000 and 70,000 Da"]
- ITIH6 has no Kunitz/bikunin inhibitor domain and no direct protease-inhibition assay. The IEA conflates an activity of the bikunin light chain or assembled complex with the ITIH6 polypeptide and should be removed.

## Secretion, bikunin coupling, and hyaluronan

- The N-terminal signal peptide, SPDI discovery context, and reviewed UniProt subcellular-location inference support the broad `extracellular region` IEA. However, no ITIH6-specific secretion assay or extracellular-fluid purification was found.
- The 2025 paper does not show ITIH6 incorporation into inter-alpha-inhibitor, covalent coupling to bikunin chondroitin sulfate, transfer by TSG-6, hyaluronan binding, or an effect on hyaluronan metabolism. Instead, its discussion says that HA/PTX3 interaction is "plausible to hypothesize" from structural homology and calls for future investigation of ITIH6 interactions with HA.
- The conserved candidate cleavage motif makes a canonical heavy-chain route plausible, so the hyaluronan-process IEA is not demonstrably false. It remains `UNDECIDED`, pending direct processing, glycosaminoglycan-linkage, or HA-transfer evidence.

## High-throughput binary interactions

- The grouped `protein binding` annotation represents eight HuRI yeast-two-hybrid pairs: ANKS1A, EVX2, KPRP, KRTAP6-1, SMIM29, TLX3, VENTX, and ZNF414.
- PMID:32296183 generated a systematic reference map by repeated Y2H screening and pairwise verification. The assay establishes binary interactions under the screening conditions, but the source does not demonstrate endogenous ITIH6 complexes, secretion-compatible colocalization, or a shared physiological mechanism for these eight partners.
- `protein binding` is too generic to describe a function and the partner set includes proteins whose usual cellular contexts are difficult to reconcile with an extracellular ITIH6 pool. Retain the experimental record as `MARK_AS_OVER_ANNOTATED`; do not infer a specific adaptor or ECM function from it.

## Curation-ready conclusion

ITIH6 is a tissue-restricted, predicted secretory ITIH-family protein with canonical VIT/vWA architecture, a unique expanded central region, and a conserved candidate heavy-chain cleavage motif. Its intrinsic molecular activity and physiological process remain unknown. In particular, neither protease inhibition nor formation of a bikunin-linked, hyaluronan-transferable heavy chain has been demonstrated. Broad extracellular localization is reasonable; serine-protease inhibition should be removed, hyaluronan metabolism should remain undecided, and the generic HuRI protein-binding annotation should be marked over-annotated.
