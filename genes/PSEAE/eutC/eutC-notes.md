# PAO1 eutC (Q9HX02) review

## 2026-11-06 evidence and identity

Official UniProt identifies this target as PAO1 taxon208964, PA4025,273aa. The matched native pair is Q9HX03/Q9HX02. Normal accession-aware fetch seeded the review; pristine text/payloads/raw hashes were frozen before curation in the ignored pao1-eutbc/seed-baseline.json.

PMID27325678 full PMC source identifies the native loci and genomic operon constructs. The eutB deletion eliminates growth on ethanolamine as carbon and nitrogen source and operon complementation restores function. It does not provide isolated PAO1 EutB/EutC kinetics or a eutC-specific deletion. Exact excerpts and source hashes are in the shared eutB-source-analysis/identity-and-native-scope.yaml. PMID19762342 purification and PMID20519496 structure are Ecoli comparisons; their stoichiometry, truncated beta-subunit construct and kinetic properties are not direct PAO1 results.

## Row and core decisions

All seeded payloads remain unchanged. The amino-acid-process mapping is corrected to ethanolamine catabolism because GO0006520 specifies amino carboxylic acids, whereas ethanolamine is an amino alcohol. Activity is reviewed as a property of the assembled EutBC enzyme; EutC receives a contributes_to core and EutB is not claimed to function autonomously. Binding is the conserved cobalamin-interface role. PAINT lineage checks report no IRD/IKR. No NEW GO rows are needed.

The complete PAO1 reference proteome has zero matches for PF00936,PF03319,IPR000249 and IPR004992; the Ecoli positive control recovers4 BMC-domain proteins and1 vertex protein. The automatic microcompartment/polyhedral-organelle assignments are removed as inappropriate organism-level transfers and flagged for UniProt review. This signature inventory does not rule out hypothetical novel shells and does not itself prove a freely soluble cytosol localization. The existing EutB cytosol IBA is retained as a phylogenetic inference; no native localization assay is invented and no cytosol core location is added.

## Research limits

A normal Falcon attempt failed with HTTP403 authentication/access error; details are recorded in ignored pao1-eutbc/falcon-eutC.log. No provider report was fabricated. Existing publication caches were not refreshed. AdoCbl availability and expression/context are necessary for meaningful native flux; genetic capacity is not an unrestricted carbon-growth guarantee.
