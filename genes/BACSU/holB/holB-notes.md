# holB research and annotation review

## 2026-11-06

Identity: P37540, BACSU, B. subtilis strain 168, taxon 224308. Current UniProt response and untouched fetch-gene seed are archived in `.cache/module-audit-logs/chromosomal-replication-20261106/bacillus-baseline.json`. Original 9 annotation payloads and raw files remain unchanged.

HolB is the delta-prime subunit of the Bacillus subtilis DNA clamp loader. Together with three DnaX/tau subunits and HolA/delta, it builds the complex that loads the beta sliding clamp onto primed DNA. Its role is clamp-loader assembly and function, not DNA polymerization or 3′–5′ proofreading catalysis.

The genuine default Falcon attempt failed with HTTP403 authentication/access failure; no provider report was authored or substituted. This document and the review are manual research. PAINT lineage check: no IRD or IKR on the resolved lineage. No donor-count argument was used.

PMID20122408 was fetched normally (abstract-only cache); the full author-hosted PDF including supplement was inspected at https://www.colorado.edu/lab/mchenry/sites/default/files/attached-files/2010_23702_mc_37_273.pdf . Its Methods explicitly specify native strain168 sequences without appended tags. The reconstitution is a PriA-dependent flapped-minicircle replication-fork assay, not oriC initiation or complete Okazaki-fragment maturation. Source-download checksum and provenance are in the shared audit cache; the publisher PDF is not redistributed in this gene directory.

Current GO was checked directly through QuickGO. GO0003896 is obsolete as equivalent to DNA-directed RNA polymerase activity; primase context therefore belongs with GO0003899 and primer synthesis. GO0003689 describes clamp loading, GO0030337 polymerase processivity. GO1990100/1990156 use E. coli protein names; in Bacillus the helicase is DnaC and the AAA+ loader is DnaI. Bacillus DnaB is an accessory loader. GO7770122 is MCM-specific and is not assigned to bacterial loaders.

## Row decisions

- 0: GO:0003677 (IEA, GO_REF:0000002): UNDECIDED. Complex formation and clamp-loading contribution do not establish an autonomous DNA-binding interface on this subunit. The broad domain-based assignment may represent a property of the loader, but the accessible target experiments do not settle it.
- 1: GO:0003887 (IEA, GO_REF:0000120): MODIFY. The biological connection to replication is sound, but nucleotide incorporation belongs to PolC/DnaE. DnaX, HolA and HolB form the tau3–delta–delta-prime loader. The replacement is interpreted as contributes_to at subunit level, as represented in the core function; the preserved machine row is not evidence of autonomous polymerase activity.
- 2: GO:0006260 (IEA, GO_REF:0000002): ACCEPT. HolB is the delta-prime subunit of the Bacillus subtilis DNA clamp loader. Together with three DnaX/tau subunits and HolA/delta, it builds the complex that loads the beta sliding clamp onto primed DNA. Its role is clamp-loader assembly and function, not DNA polymerization or 3′–5′ proofreading catalysis. Purified-component experiments or direct DNA engagement establish a molecular role; process participation is not inferred solely from essentiality. The specific division of labor is retained in the core function.
- 3: GO:0006261 (IBA, GO_REF:0000033): ACCEPT. HolB is the delta-prime subunit of the Bacillus subtilis DNA clamp loader. Together with three DnaX/tau subunits and HolA/delta, it builds the complex that loads the beta sliding clamp onto primed DNA. Its role is clamp-loader assembly and function, not DNA polymerization or 3′–5′ proofreading catalysis. Purified-component experiments or direct DNA engagement establish a molecular role; process participation is not inferred solely from essentiality. The specific division of labor is retained in the core function.
- 4: GO:0008408 (IEA, GO_REF:0000002): REMOVE. HolB is the delta-prime clamp-loader subunit, not PolC or a proofreading exonuclease. The IPR004622 mapping transfers a holoenzyme catalytic property to a structural loading subunit.
- 5: GO:0009295 (IEA, GO_REF:0000044): ACCEPT. This location is consistent with the protein’s chromosome-associated work. The curated target-specific imaging places the delta-prime subunit in nucleoid-associated replication foci.
- 6: GO:0009360 (IEA, GO_REF:0000002): MODIFY. The tau3–delta–delta-prime complex is established directly. Use its specific complex term rather than treating every subunit as the polymerase catalytic core.
- 7: GO:0034061 (IEA, GO_REF:0000116): MODIFY. The biological connection to replication is sound, but nucleotide incorporation belongs to PolC/DnaE. DnaX, HolA and HolB form the tau3–delta–delta-prime loader. The replacement is interpreted as contributes_to at subunit level, as represented in the core function; the preserved machine row is not evidence of autonomous polymerase activity.
- 8: GO:0071897 (IEA, GO_REF:0000120): ACCEPT. HolB is the delta-prime subunit of the Bacillus subtilis DNA clamp loader. Together with three DnaX/tau subunits and HolA/delta, it builds the complex that loads the beta sliding clamp onto primed DNA. Its role is clamp-loader assembly and function, not DNA polymerization or 3′–5′ proofreading catalysis. Purified-component experiments or direct DNA engagement establish a molecular role; process participation is not inferred solely from essentiality. The specific division of labor is retained in the core function.

## Evidence boundaries

- [PMID:23525462] Insights into the structure and assembly of the Bacillus subtilis clamp-loader complex and its interaction with the replicative helicase. B. subtilis tau/clamp-loader experiments are relevant. The helicase used in the mixed-species interaction experiments is Geobacillus stearothermophilus DnaB, not the unrelated B. subtilis DnaB loading accessory. PMID23525462 directly establishes tau3–delta–delta-prime stoichiometry.
- [PMID:28878042] Interactions of the Bacillus subtilis DnaE polymerase with replisomal proteins modulate its activity and fidelity. Full cached text was consulted for the relevant target-specific claims.

Structured InterPro source-defect query records the incorrect catalytic mapping for this target; no upstream report was sent and no other family member is inferred to lack the activity.
