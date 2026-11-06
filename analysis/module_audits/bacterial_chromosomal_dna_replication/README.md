# Bacterial chromosomal DNA replication audit

The original seven-part replisome omitted helicase loading, RNA-primer replacement and topological separation. Twelve required roles now retain the chromosome-duplication boundary, with separate optional HolC/HolD and tau-coupling context. Bacteria denotes a reusable mechanism, not universal possession of one enzyme set. The sampled route is DnaA-initiated replication with circular-chromosome topology; conditional fork traps, lesion bypass and dimer resolution are described separately.

Thirty-seven curated references provide mined findings and step-level evidence. Fifty-two completed reviews cover E. coli, Pseudomonas, Bacillus, Mycobacterium and Vibrio. DnaC, DnaI/DnaD/DnaB and DciA are distinct loader implementations. DnaE1/DnaQ, active-PHP DnaE1 and PolC/DnaE3 have different proofreading and primer-handoff architectures. The literature's PolC/DnaE1 combination remains an explicitly unsampled alternative; no Bacillus DnaE3 mechanism is generalized to it.

RNA-primer removal and DNA gap filling remain separate required roles. Bacillus PolA has demonstrated in-vitro capacity, while its dominant native gap-filling assignment remains unresolved. GyrAB and ParCE are assembled-complex implementations of generic topology roles. H37Rv GyrAB directly supercoils and decatenates model DNA; native daughter-chromosome unlinking is a physiological inference. No M. smegmatis rate claim is transferred to H37Rv. Verified DciA is Q9KPH3/VC_2395, not an invented PAO1/KT2440 accession; KT2440 HolD is PP_0696/Q88Q02 with native-start and construct caveats.

The PTHR32294 family review now distinguishes experimentally active MYCTU PHP from DnaQ-dependent alpha implementations and Bacillus DnaE3. Broad exonuclease transfer remains unresolved without a finer clade/residue model. The original polymerase PAINT node and its SOUND judgment are unchanged. Literal surprising PANTHER labels, including organellar gyrase labels and the PolA family name, retain database identity rather than implying biological localization.

Run `uv run python modules/bacterial_chromosomal_dna_replication-source-analysis/check_audit.py`.
All 97 production-compiler/oracle cases pass. They reject missing mandatory roles, incomplete complexes, cross-taxon mixtures, generic family/ATPase substitutions, split-polypeptide PHP/PolC activities, and unsupported native gap-filler inference. Stoichiometric capacity does not measure abundance, expression or replication sufficiency. False means unresolved panel coverage, not pathway absence.

The immutable baseline preserves 1,067 historical rows (1,065 machine assertions and two inherited proposals) and 104 raw UniProt/GOA files. Fourteen new proposals give 1,081 current rows. Falcon attempts failed with HTTP403; manual evidence and construct/identity notes record the work actually done. Focused gene, family, module, history and source checks pass. Eight module advisories retain missing exact GO loader terms and unresolved broad family-scope adjudications. Full-corpus validation terminated with exit 1: 19 unrelated reference failures in 17 yeast reviews, with all 23 affected review/source/validation-input blobs unchanged from the pinned base. Schema and term checks passed; best-practices validation reported zero errors. Exact tuples, log SHA256 and input-blob proof are in `preexisting-reference-failures.yaml`. The module is COMPLETE and focused schema/semantic/render plus all 97 capacity cases pass. Module PR publication, external review/CI and actual merge remain pending.

## PR #6117 review follow-up

Eleven gene reviews now record the HolD start-site discrepancy and exact construct
coordinates, source-specific polymerase-mapping defects, consistent removal of bare
protein-binding terms, and specific replication/proofreading activities. Historical
NEW proposals remain intact; their more precise core activities retain three
explicit coverage advisories. The epsilon module annoton now uses DNA-specific
3′–5′ exonuclease activity, matching the gene cores. All 97 pathway cases pass.

The prior full-corpus result above is historical. Fresh full validation of these
scientific corrections, renewed independent review/CI and actual merge remain
pending. See round1-followup.yaml and round1-gene-review-proof.yaml.

## Round 2 proposal specificity

PR #6117 round 2 refines two proposals authored within this PR, with both prior versions archived and independently verified against git and the pristine seed: HolD now uses DNA-templated DNA replication, while Bacillus DnaB has separate single- and double-stranded DNA-binding activities. Three DnaQ exonuclease rows refine directly to DNA-specific proofreading activity. DnaB membrane evidence explicitly distinguishes wild-type enrichment from mutant DnaD recruitment. Four focused review validations, renders and histories pass without curation warnings. All 1,067 original seed rows, including two inherited NEW rows, and 104 raw sources remain preserved across 52 COMPLETE reviews; the final count is 1,082 rows. The module remains unchanged. The capacity checker recognizes only the two independently verified DNA-binding descendant relationships and passes 100 cases, including removal and one-way entailment controls. Fresh full validation, publication, renewed review/CI and actual merge remain pending.
