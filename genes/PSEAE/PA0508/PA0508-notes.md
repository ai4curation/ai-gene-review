# PA0508 / FadE2 manual review

## Identity and frozen seed

The official UniProt locus symbol is PA0508; FadE2 is the paper alias. Current accession Q9I610, PAO1 taxon208964, was verified before normal fetch. Pristine three-row seed and two raw-source hashes were frozen before curation. PTHR42803:SF1 is shared with the other paralog, but does not guarantee substrate identity. Exact PDB mapping and full-sequence comparison, including GH remnant and mutant substitutions, are in ../PA0506/PA0506-source-analysis/identity-bridge.md.

## Primary evidence

PMID40057486 was read in full without refreshing its cache. FadE2 supports C4, C6 and C8 acyl-CoAs; no activity was detected on C16 or C18 under the reported conditions. Full-length PAO1 ORFs were PCR-amplified into pET19m, expressed in E. coli Rosetta2(DE3), and His6-TEV tags removed. Assays use ferrocenium, not demonstrated ETF turnover. FadE2 M130G/E296A/Q303A acquires low C16 activity; that engineered property is not assigned to wild-type FadE2. The FadE1 E441A substrate-bound structure is likewise a mutant. Native residue numbering is verified after removing the GH construct prefix.

## Physiological scope and proposed process

Pa10348 proteomics, PA14 fatty-acid-growth mutants/reporters and PAO1 Galleria mutants are distinct contexts. No PAO1 fatty-acid-growth or CoA-flux profile is reported. One NEW IC GO0006635 proposal uses PAO1 catalytic participation plus PA14 functional-counterpart context; the enzyme performs the oxidation step rather than being a substrate or merely necessary. Same-role QuickGO Q47146 and Q8ZRJ7 comparator query returns seven beta-oxidation annotations; GO parents/definitions and lack of target GO-CAM index hits were checked. This comparison assesses annotation convention, not target truth. No redundant ancestor BP, oxygen-routing-specific0033539, or Galleria-derived virulence BP is added. Involvement in a step is distinct from a claim of complete native oxidation.

## Decisions and uncertainty

Both broad redox rows MODIFY to the shared acceptor-unspecified acyl-CoA dehydrogenase proposal. GO0052890 does not explicitly assert ETF; flavin-dependent chemistry is retained, not disproven. FAD binding is KEEP_AS_NON_CORE because it is an integral cofactor supporting catalysis. No membrane location is inferred solely from a homologous CII domain. The unreviewed database 3-methylmercaptopropionyl-CoA label is not established by this paper; ordinary fatty-acyl-CoA assays do not exclude additional sulfur-substrate activity.

Default Falcon was genuinely attempted and failed HTTP403; no provider report was fabricated. All seed payloads and raw files remain untouched. Focused validation, render, source/sequence checks and helper history are recorded in the ignored pao1-dehydrogenases audit directory.
