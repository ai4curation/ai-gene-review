# PTHR43867 scoped evidence and lineage audit

This analysis separates an ancestral hexosyltransferase claim from product-specific cellulose and OPG claims. The exact PAINT node descent is established from the cached PANTHER tree, not from donor counts. Full acquired records remain in ignored cache; the excerpts below are curated experimental FUNCTION statements, not protein-name predictions.

## P74165
Source: https://rest.uniprot.org/uniprotkb/P74165.json ; acquired 2026-11-06; SHA256 `d82abf80b0ec305f41fb0bfd930bdb247e6d2b02adab620e264f65b1fd867fa1`.
Organism: Synechocystis sp. (strain ATCC 27184 / PCC 6803 / Kazusa); taxon 1111708. Current PANTHER classification: PTHR43867, PTHR43867:SF2.

Curated FUNCTION statement:

Glucosyltransferase involved in the biosynthesis of the non-bilayer-forming membrane lipid beta-monoglucosyldiacylglycerol which contributes to regulate the properties and stability of the membrane. Catalyzes the transfer of a glucosyl residue from UDP-Glc to diacylglycerol (DAG) acceptor to form the corresponding beta-glucosyl-DAG (1,2-diacyl-3-O-(beta-D-glucopyranosyl)-sn-glycerol). It can only use UDP-Glc as sugar donor. Two types of DAG (dipalmitoyl-DAG (DPDAG) and 1-oleoyl-2-palmitoyl-DAG (OPDAG)) can be used as sugar acceptors, but OPDAG is preferred

Experimental attribution: PubMed:16714404, PubMed:19549521.

## P37653
Source: https://rest.uniprot.org/uniprotkb/P37653.json ; acquired 2026-11-06; SHA256 `b9ded8c4666dc3cfd31560700a8d8b8532cf051f408f6d6b54b5e756ea0c6b8d`.
Organism: Escherichia coli (strain K12); taxon 83333. Current PANTHER classification: PTHR43867, PTHR43867:SF2.

Curated FUNCTION statement:

Catalytic subunit of cellulose synthase. It polymerizes uridine 5'-diphosphate glucose to cellulose, which is produced as an extracellular component for mechanical and chemical protection at the onset of the stationary phase, when the cells exhibit multicellular behavior (rdar morphotype). Coexpression of cellulose and thin aggregative fimbriae (curli fimbrae or fibers) leads to a hydrophobic network with tightly packed cells embedded in a highly inert matrix that confers cohesion, elasticity and tissue-like properties to colonies (PubMed:24097954)

Experimental attribution: PubMed:11260463, PubMed:24097954.

## Q9U720
Source: https://rest.uniprot.org/uniprotkb/Q9U720.json ; acquired 2026-11-06; SHA256 `769454853c85044c48cd32d85d0571052ad549b3a6e953276915464f6032c14b`.
Organism: Dictyostelium discoideum; taxon 44689. Current PANTHER classification: PTHR43867, PTHR43867:SF2.

Curated FUNCTION statement:

Catalytic subunit of cellulose synthase. It incorporates glucose from uridine 5'-diphosphate glucose (UDP-alpha-D-glucose) to cellulose (a (1->4)-beta-D-glucan), which is produced as an extracellular component for mechanical and chemical protection at the onset of the stalk formation, when the cells exhibit multicellular behavior during culmination

Experimental attribution: PubMed:10681463.

## Exact tree descent

P62517 is leaf PTN008122828 in PTHR43867:SF5, below PTN002466726, PTN001317543 and PTN005186628. P37653 is leaf PTN000795947 in SF2; P74165 is leaf PTN002466736 in SF2. Both are below PTN002466726 and PTN001317543, but neither is below PTN005186628. Q9U720 is leaf PTN000062565 in SF2, below PTN002466726 but not the other two assessed nodes.

PTN002466726 has 56 sampled descendants across SF2, SF4, SF5, SF7 and SF8. PTN005186628 has eight sampled descendants, all SF5. The machine-readable companion records the precise counts and accession-bearing leaves. These are sampled tree relationships, not a claim that every classification entry has a leaf in this cache.

SF2 contains both cellulose synthases P37653 and Q9U720 and the experimentally characterized beta-monoglucosyldiacylglycerol synthase P74165. Its official cellulose-synthase label is therefore insufficient for a universal cellulose grant. The PAINT broad hexosyltransferase seed P74165 supports sugar transfer but not cellulose production.

## OpgH and taxon limits

The frozen E. coli P62517 record and its reviewed membrane-system and opgH genetic evidence support OPG glucosyltransferase participation, distinct from cellulose synthesis. Its genuine PTN002466726 descent makes this a node-specific product over-propagation concern, not an erroneous membership claim or a donor-count objection.

CERS4 Q9FA52 is the 595-residue OpgH of Cereibacter sphaeroides strain ATH 2.4.1 (taxon 272943), classified SF5 in its frozen UniProt record. PMID12027885 establishes native cyclic OPGs and opgGIH dependence; heterologous opgIHC expression in E. coli produces abnormally long linear glucans. This neither establishes OpgH-alone cyclization nor permits a family-wide linear-product restriction.

CAUVN B8GX72 is the 663-residue OpgH CCNA_02097 of Caulobacter vibrioides NA1000/CB15N (taxon 565050), classified SF5. It is not the CB15 accession Q9A6R5 found in other family membership records. PMID39145657 uses NA1000 and demonstrates morphology and viability defects after OpgH depletion and tests putative active-site variants. It does not directly establish the purified enzyme product or the E. coli N-terminal FtsZ mechanism in Caulobacter.

Neither Q9FA52 nor B8GX72 is present among the cached tree leaves; no PTN or exact node-descent claim is invented for these two accessions. Their subfamily classification rests on the frozen UniProt records.
