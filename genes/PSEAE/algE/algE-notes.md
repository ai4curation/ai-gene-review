# algE primary-source review notes

## Review session 2026-10-25

Applied review and annotation-reviewer instructions. Verified current UniProt accession, PAO1 organism (NCBITaxon:208964) and gene symbol before normal `just fetch-gene`. Preserved every source annotation field, including evidence, qualifier, supporting entities and reference; only review decisions were added. No GO-CAM index entry was found for this accession. All PMID quotes refer to the normal publication cache; no cached source, GOA or UniProt file was hand-edited. Abstract-only sources were not treated as complete papers. No unsupported NEW process rows were added.

The actual default-provider attempts `just deep-research-falcon PSEAE algE --fallback perplexity-lite` failed: Edison/Falcon HTTP403 and fallback HTTP401 insufficient quota. These notes record manual primary-source research and are not a provider report. `just fetch-fitness PSEAE algE` could not retrieve a local/remote FEBA result and did not establish an organism mapping/result; no fitness phenotype is claimed. Source and provider attempts were performed alongside publication caching. UniProt family/domain memberships are classification evidence, not DE/GO/ARBA predictions used as proof of chemistry.

AlgE is an integral outer-membrane 18-stranded beta-barrel, not merely peripheral membrane protein despite older UniProt location wording. PMID21778407 establishes the structure, electropositive constriction and loop T8 effects on halide flux/in vivo production. Halide flux is not a direct purified alginate-polymer flux assay. PMID23335756 links pore/loop mutations to production and shows stability of AlgK/AlgX/Alg44 depends on proper AlgE assembly. A structural export role can contribute directly to the biosynthetic machinery without assigning polymerase chemistry.

Core polysaccharide transmembrane transporter activity GO:0015159 was checked in QuickGO. No new annotation row is proposed; the independent core synthesis is supported by original publications. Family-specific domains: IPR053728 Alginate_Permeability_Chnl, IPR025388 Alginate_export_dom, PF13372; no UniProt PANTHER entry.

## Sources checked

- [PMID:23335756] Dual roles of Pseudomonas aeruginosa AlgE in secretion of the virulence factor alginate and formation of the secretion complex.: Direct P. aeruginosa evidence; secretion phenotypes do not establish polysaccharide polymerase activity.
- [PMID:21778407] Structural basis for alginate secretion across the bacterial outer membrane.: Direct P. aeruginosa structure and halide-flux experiments; halide flux is not direct reconstitution of alginate-polymer flux.


## PR #5552 follow-up, 2026-10-26

Unified the existing-term representation on GO:0015159, whose live definition explicitly covers transfer of polysaccharides across a membrane. Removed the KT2440 alginate-channel NTR because the evidence does not require an additional channel-specific ontology proposal. Pa structure/halide flux/pore-mutant secretion phenotypes (PMID:21778407; PMID:23335756) support an IC molecular-function recommendation, not direct visualization of polymer passage. KT2440 and Azotobacter assignments remain ISS-level homolog inferences. The missing Pa and KT2440 MF rows are nonredundant with their BP/CC rows; no NEW process was added. Normal refetch of PMID:23335756 still returned abstract only, so no full-text-only assay detail was inferred.
