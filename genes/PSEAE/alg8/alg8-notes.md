# alg8 primary-source review notes

## Review session 2026-10-25

Applied review and annotation-reviewer instructions. Verified current UniProt accession, PAO1 organism (NCBITaxon:208964) and gene symbol before normal `just fetch-gene`. Preserved every source annotation field, including evidence, qualifier, supporting entities and reference; only review decisions were added. No GO-CAM index entry was found for this accession. All PMID quotes refer to the normal publication cache; no cached source, GOA or UniProt file was hand-edited. Abstract-only sources were not treated as complete papers. No unsupported NEW process rows were added.

The actual default-provider attempts `just deep-research-falcon PSEAE alg8 --fallback perplexity-lite` failed: Edison/Falcon HTTP403 and fallback HTTP401 insufficient quota. These notes record manual primary-source research and are not a provider report. `just fetch-fitness PSEAE alg8` could not retrieve a local/remote FEBA result and did not establish an organism mapping/result; no fitness phenotype is claimed. Source and provider attempts were performed alongside publication caching. UniProt family/domain memberships are classification evidence, not DE/GO/ARBA predictions used as proof of chemistry.

Alg8 is the catalytic GDP-mannuronate polymerase. PMID16391057 assays cell-envelope fractions, not a purified isolated enzyme. PMID18524915 provides membrane topology and catalytic-motif mutagenesis. The two hyaluronan IBAs at PTN000530809 cross the demonstrated substrate specificity and are removed; the target in WITH/FROM is not circular evidence. Broad polysaccharide synthesis is refined; ECM assembly is corrected laterally to actual polymer biosynthesis, not claimed as a descendant refinement.

UniProt DR:PANTHER PTHR22913:SF12 has official name MANNURONAN SYNTHASE; the broader PTHR22913 label HYALURONAN SYNTHASE does not establish hyaluronan specificity for this member. PF13641 Glyco_tranf_2_3 is the GT-domain support.

## Sources checked

- [PMID:18524915] Membrane topology and roles of Pseudomonas aeruginosa Alg8 and Alg44 in alginate polymerization.: Direct P. aeruginosa mutagenesis/topology; not a purified Alg44 glycosyltransferase assay.
- [PMID:16391057] In vitro alginate polymerization and the functional role of Alg8 in alginate production by Pseudomonas aeruginosa.: Envelope-fraction polymerization, not an assertion that isolated Alg8 alone is sufficient.

## 2026-10-26 matrix-assembly evidence QA

The prior lateral MODIFY of GO:0085029 is superseded by KEEP_AS_NON_CORE after inspecting full PMID:25968647 (Alginate Polymerization and Modification Are Linked in Pseudomonas aeruginosa), Fig. 9 and Table 2. Native PDO300 alg8 deletion and complementation were compared in continuous-culture flow-cell biofilms: "The PDO300Δalg8(pBBR1MCS-5:alg8) and PDO300Δalg44(pBBR1MCS-5:alg44) strains established heterogeneous highly structured biofilms (Fig. 9)." The deletion control lacked elevated structured architecture. Alg8 performs the polymerization that constructs the matrix component, so this is a participation argument supported by target-specific architecture measurements, not necessity evidence alone. Matrix assembly is a conditional non-core role; alginate polymerization remains core. The term definition concerns aggregation, arrangement and bonding of extracellular matrix. This supports retention more directly than the related-strain mt-2 matrix evidence used for PSEPK; no equivalent native architecture assay was found for AZOVI, whose over-annotation judgment is unchanged. This is an existing IBA review, not a NEW process annotation. PAINT ancestry remains unresolved; no failed node placement is asserted. All original annotation fields are unchanged.


## PR #5552 follow-up, 2026-10-26

Hyaluronan-specific propagation is treated consistently as REMOVE across the three Alg8 reviews; supported alginate roles remain independently represented. Live UniProt PANTHER cross-references show that SF12 itself contains S. pyogenes HasA P0C0H0 (hyaluronan chemistry; PMID:8276791) and NodC P04340/P26024, in addition to the three Alg8 proteins. The SF12 label MANNURONAN SYNTHASE is therefore not a substrate-specific selector. GO:0085029 was checked live: matrix aggregation/arrangement/bonding, with no animal restriction. Retained the evidence gradient: Pa target-specific architecture, KT2440 related-strain inference, Azotobacter over-annotation without a comparable matrix-architecture result. Substituting a biofilm term would change the biological claim rather than simply refine it.
