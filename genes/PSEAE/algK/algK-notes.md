# algK primary-source review notes

## Review session 2026-10-25

Applied review and annotation-reviewer instructions. Verified current UniProt accession, PAO1 organism (NCBITaxon:208964) and gene symbol before normal `just fetch-gene`. Preserved every source annotation field, including evidence, qualifier, supporting entities and reference; only review decisions were added. No GO-CAM index entry was found for this accession. All PMID quotes refer to the normal publication cache; no cached source, GOA or UniProt file was hand-edited. Abstract-only sources were not treated as complete papers. No unsupported NEW process rows were added.

The actual default-provider attempts `just deep-research-falcon PSEAE algK --fallback perplexity-lite` failed: Edison/Falcon HTTP403 and fallback HTTP401 insufficient quota. These notes record manual primary-source research and are not a provider report. `just fetch-fitness PSEAE algK` could not retrieve a local/remote FEBA result and did not establish an organism mapping/result; no fitness phenotype is claimed. Source and provider attempts were performed alongside publication caching. UniProt family/domain memberships are classification evidence, not DE/GO/ARBA predictions used as proof of chemistry.

AlgK is an outer-membrane-anchored periplasmic scaffold, not a glycosyltransferase. PMID9457868 genetics demonstrates normal-polymer production depends on AlgK but does not establish catalysis. PMID20159471 directly examines P. aeruginosa lipidation and AlgE mislocalization after algK disruption/C28S substitution. Its crystallized repeat-rich AlgK is P. fluorescens WCS374r, not P. aeruginosa.

PMID36494359 contains direct P. aeruginosa AlgK–AlgX interaction/interface-mutant evidence, but the AlgKX crystal structure and purified polymer-binding assays use P. putida KT2440. PMID42766672 directly reconstitutes P. aeruginosa AlgK/AlgX and shows individual proteins are MucD protease substrates, while their assembled complex is protected. AlgK is acted on in these assays; do not propose proteolysis participation for a substrate.

UniProt PTHR11102:SF160 official name ERAD-ASSOCIATED E3 UBIQUITIN-PROTEIN LIGASE COMPONENT HRD3 is a surprising but real membership. Do not infer eukaryotic ERAD chemistry from it. More specific AlgK descriptors include IPR053440 Alginate_biosynth_AlgK, IPR050767 Sel1_AlgK and IPR060023 TPR_AlgK_middle.

## Sources checked

- [PMID:9457868] Deletion of algK in mucoid Pseudomonas aeruginosa blocks alginate polymer formation and results in uronic acid secretion.: Supports an export/assembly contribution; the original polymerization interpretation does not establish AlgK catalysis.
- [PMID:20159471] AlgK is a TPR-containing protein and the periplasmic component of a novel exopolysaccharide secretin.: The crystallized TPR-rich AlgK is from P. fluorescens WCS374r; P. aeruginosa lipidation/localization experiments are separate.
- [PMID:36494359] Structure of the AlgKX modification and secretion complex required for alginate production and biofilm attachment in Pseudomonas aeruginosa.: The AlgKX crystal structure and purified polymer-binding assays use P. putida KT2440 proteins, not P. aeruginosa proteins.
- [PMID:42766672] MucD regulates alginate biosynthesis through the proteolytic control of AlgX and AlgK in Pseudomonas aeruginosa.: Direct P. aeruginosa reconstitution and proteolysis; being a protease substrate does not make AlgK an enzyme or participant in proteolysis.
