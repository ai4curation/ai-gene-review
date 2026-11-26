# Exact PAO1 FadE1/FadE2 identity and assay scope

Primary source: PMID40057486, Pseudomonas aeruginosa acyl-CoA dehydrogenases and structure-guided inversion of their substrate specificity. The existing full publication cache is unchanged; SHA256 3cdb3fff0346beba46c9d4f7642c6eda3a66ffaf14fcd8af209339df211320e2.

UniProt searches are for organism_id:208964 and gene_exact:PA0506 or PA0508. The records carry locus names, not primary fadE1/fadE2 symbols. Paper aliases are retained separately.

## PA0506 / Q9I612
Current UniProt length 601 residues; taxon 208964 (PAO1). Identity response SHA256 319cbf4962979a458f16b7a476e9faac227f4e168805ab87718c35b2e4b0301b. Both targets classify to PANTHER:PTHR42803:SF1, BROAD-SPECIFICITY LINEAR ACYL-COA DEHYDROGENASE FADE5; parent PTHR42803, ACYL-COA DEHYDROGENASE. This family label does not grant broad substrate scope to every member.

8PNS entity1: 603 residues = GH remnant + the complete 601-residue Q9I612 sequence. Differences after removing GH: none (wild type).
RCSB/SIFTS maps the construct to Q9I612. URL https://data.rcsb.org/rest/v1/core/polymer_entity/8PNS/1 ; response SHA256 672f9fe3f0aad048ef7067afd38f115f4bc1f303a0ffc420f7e23695d654fa65.

8PU5 entity1: 603 residues = GH remnant + the complete 601-residue Q9I612 sequence. Differences after removing GH: E441A.
RCSB/SIFTS maps the construct to Q9I612. URL https://data.rcsb.org/rest/v1/core/polymer_entity/8PU5/1 ; response SHA256 81ef31077486f823b7082cec5131f017fc6c75ad65a8a8bc69f8830d8b1f5c59.

## PA0508 / Q9I610
Current UniProt length 592 residues; taxon 208964 (PAO1). Identity response SHA256 32977b6314b02acdad5ba194274c07e4d0eb21b970bee4e2d2fb085657949b2b. Both targets classify to PANTHER:PTHR42803:SF1, BROAD-SPECIFICITY LINEAR ACYL-COA DEHYDROGENASE FADE5; parent PTHR42803, ACYL-COA DEHYDROGENASE. This family label does not grant broad substrate scope to every member.

8PNG entity1: 594 residues = GH remnant + the complete 592-residue Q9I610 sequence. Differences after removing GH: none (wild type).
RCSB/SIFTS maps the construct to Q9I610. URL https://data.rcsb.org/rest/v1/core/polymer_entity/8PNG/1 ; response SHA256 65c1922597dd1e3edc84d134a682a317ebe82991231b503933b0bdb2872eee62.

8R1E entity1: 594 residues = GH remnant + the complete 592-residue Q9I610 sequence. Differences after removing GH: M130G, E296A, Q303A.
RCSB/SIFTS maps the construct to Q9I610. URL https://data.rcsb.org/rest/v1/core/polymer_entity/8R1E/1 ; response SHA256 f75533bfd457de809090413b107133da20d62cf033c31b48fd21d98e1af66d33.

## Primary methods and limits

The paper explicitly clones full-length PAO1 ORFs into pET19m, expresses them in E. coli Rosetta2(DE3), and cleaves/removes the His6-TEV tag. PDB polymer sequences independently show the remaining GH prefix; experimental residue labels map to native UniProt coordinates after that prefix. The C16-bound FadE1 structure is E441A, and the widened FadE2 structure is the M130G/E296A/Q303A mutant; neither mutant represents wild-type specificity.

The catalytic assays use artificial ferrocenium as electron acceptor. Bound FAD is directly seen structurally, but a physiological ETF or other respiratory partner is not demonstrated. Membrane association of the CII domain is proposed rather than directly measured for these targets.

Table1 reports FadE1 activity on C18, C16, C8 and weaker C6 acyl-CoA; C4 is ND (not determined), not a negative result. FadE2 has measured activity on C8, C6 and C4; C16 and C18 are NA (no activity in the reported assay). Thus the paper's broad use of medium-chain for FadE2 must not hide its measured C4 activity. The positive tested substrates do not establish an uninterrupted chain-length window for every intermediate.

Physiological source contexts differ: Pa10348 (Manchester Epidemic Strain) proteomics; PA14 promoter reporters and fatty-acid-growth deletions; PAO1 recombinant enzymes; PAO1 Galleria infection deletions after PA14 proved too rapidly lethal. The paper does not supply PAO1 fatty-acid-growth curves or CoA-flux endpoints. Sequential long/short-chain cooperation is a mechanistic interpretation, not direct matched-strain full-spiral reconstitution or universal complete oxidation. PAO1 infection effects establish context-dependent necessity, not a new virulence molecular activity.

The frozen UniProt predicted 3-methylmercaptopropionyl-CoA dehydrogenase label is not substantiated by a substrate assay in this paper. Conversely, fatty-acyl-CoA activity does not prove that the sulfur-containing substrate cannot be used. No additional specific substrate annotation is manufactured from the database name.

## NEW process assessment

The enzyme performs the dehydrogenation step itself; it is not a consumed substrate or an upstream regulator. One IC fatty acid beta-oxidation proposal per target is supported by exact PAO1 catalytic chemistry plus strain-qualified PA14 functional counterpart evidence. This does not claim PAO1 growth or flux was measured. GO0006635 describes a complete pathway, but involved_in asserts participation in a step, not enzyme-alone completion; GO0033539 is not added because its extra oxygen-routing context was not resolved here.

QuickGO same-role comparator query on Q47146 (E. coli FadE) and Q8ZRJ7 (LT2 FadE), with GO0006635 descendant matching, returned seven beta-oxidation annotations. This is a convention check, not independent evidence for these PAO1 proteins. gocams/index.tsv has no match for Q9I612 or Q9I610. No ancestor/descendant BP proposal already exists in either three-row seed. No Galleria-derived pathogenesis BP is proposed.
