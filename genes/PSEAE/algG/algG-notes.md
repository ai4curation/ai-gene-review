# algG primary-source review notes

## Review session 2026-10-25

Applied review and annotation-reviewer instructions. Verified current UniProt accession, PAO1 organism (NCBITaxon:208964) and gene symbol before normal `just fetch-gene`. Preserved every source annotation field, including evidence, qualifier, supporting entities and reference; only review decisions were added. No GO-CAM index entry was found for this accession. All PMID quotes refer to the normal publication cache; no cached source, GOA or UniProt file was hand-edited. Abstract-only sources were not treated as complete papers. No unsupported NEW process rows were added.

The actual default-provider attempts `just deep-research-falcon PSEAE algG --fallback perplexity-lite` failed: Edison/Falcon HTTP403 and fallback HTTP401 insufficient quota. These notes record manual primary-source research and are not a provider report. `just fetch-fitness PSEAE algG` could not retrieve a local/remote FEBA result and did not establish an organism mapping/result; no fitness phenotype is claimed. Source and provider attempts were performed alongside publication caching. UniProt family/domain memberships are classification evidence, not DE/GO/ARBA predictions used as proof of chemistry.

AlgG has separable catalytic and noncatalytic roles. PMID8144447 directly demonstrates mature periplasmic AlgG and polymer-level C5 epimerization. PMID12581364 compares complete deletion with S272N (algG4): deletion leads to AlgL digestion, while epimerase-defective protein supports polymer production. Hence epimerization is optional for the structural export contribution; a fully assembled continuous periplasmic conduit is a model, not a direct structural observation in this paper. Historical experiments use P. aeruginosa FRD1-derived material curated into the PAO1 reference record, not a claim that all assays used PAO1.

PMID16401084 shows purified enzyme activity on sufficiently long substrates without Ca2+ and can produce adjacent G residues in vitro; do not claim the enzyme can never make G blocks because native P. aeruginosa alginate usually lacks them. PMID16866359 establishes stereochemical mechanism. Current QuickGO searches for mannuronan/mannuronate/C5-epimerase returned no exact term; propose mannuronan C5-epimerase activity (EC5.1.3.37; RHEA45572) with primary evidence, without inventing a GO ID.

The two ubiquitin/proteasome IBAs at PTN007723485 are incompatible with this bacterial periplasmic carbohydrate-active protein; cytoplasm is corrected laterally to experimentally localized periplasm. No PAINT tree was reconstructed, so this is a target-specific challenge to propagated scope, not a claim to have re-curated the ancestral node. No UniProt PANTHER entry is present; IPR053409 Mannuronan_C5-epimerase provides a precise family descriptor, versus broad PF05048 NosD.

## Sources checked

- [PMID:12581364] The dual roles of AlgG in C-5-epimerization and secretion of alginate polymers in Pseudomonas aeruginosa.: Direct FRD1 genetics distinguish structural function from catalytic epimerization; channeling-scaffold interpretation is a model.
- [PMID:8144447] Pseudomonas aeruginosa AlgG is a polymer level alginate C5-mannuronan epimerase.: P. aeruginosa FRD1-derived AlgG, including recombinant expression; curated into the PAO1 species reference record. Not a PAO1-specific phenotype claim.
- [PMID:16401084] Pseudomonas aeruginosa C5-mannuronan epimerase: steady-state kinetics and characterization of the product.: Do not conflate isolated-enzyme G-block capability with usual native P. aeruginosa polymer composition.
- [PMID:16866359] Chemical mechanism and specificity of the C5-mannuronan epimerase reaction.: Direct enzyme chemistry, distinct from protein-dependent export role.
