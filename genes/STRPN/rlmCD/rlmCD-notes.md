# Streptococcus pneumoniae RlmCD (SP_1029) review notes

## Identity and naming — 2026-10-26

The normal fetch maps Q97R12, Y1029_STRPN, 543 residues, to S. pneumoniae serotype 4 TIGR4 (ATCC BAA-334; taxon 170187), locus SP_1029. The current UniProt record has no primary gene symbol and still describes an uncharacterized RNA methyltransferase. The review uses the experimentally established rlmCD symbol, retaining SP_1029 as an alias and the original accession/taxon/raw files unchanged. This is a justified top-level naming correction from the scaffold's accession fallback, not an alteration of any seeded annotation. PMID:26365244 identifies SP_1029 as RlmCD; PMID:30388185 explicitly clones sp_1029. The UniProt PDB cross-references link the same record to 5XJ1/5XJ2 and 5ZQ0/5ZQ1/5ZQ8/5ZTH. See the adjacent source-analysis identity report for the exact record-to-construct chain.

## Native chemistry and strain limits

PMID:26365244 full text, Figures 2–3: TIGR4 and the SP_1029-disrupted derivative Sp332 were compared by LC/MS and collision-induced dissociation. Native loss of U747 methylation is chemically mapped; the U1939-containing fragment also loses a methyl group. “Therefore, we conclude that S. pneumoniae SP_1029 encodes the dual-specific methyltransferase RlmCD.” These are target-strain chemical results, not an inference solely from another species or from protein-pocket similarity.

The paper also examines the clinical S1 background, RlmAII-dependent G748 methylation and telithromycin susceptibility. These experiments must not be flattened into a universal resistance function: the phenotype is framed in erm(B)-carrying backgrounds, and native TIGR4 without erm(B) remains highly susceptible with or without RlmCD. RlmCD modifies U747, which promotes the neighboring modification; RlmAII performs the G748 chemistry. No antibiotic-response or G748-catalysis annotation was proposed here.

A real source discrepancy is retained. Methods describe pTKY1196 as amplified from TIGR4, whereas Results describe it as carrying SP_1029 from S1. The review does not silently pick a plasmid donor strain or rely on numerical complementation values. Native TIGR4-versus-Sp332 chemistry, separate in vitro assays and the locus/structure mapping provide independent support. This does not justify rejecting the paper's directly observed methylation sites.

## Recombinant biochemistry and engineered structural constructs

PMID:28949991 full text: purified full-length RlmCD and its 1–454 construct methylate an 18-nt helix-35 RNA using tritiated SAM. U747A/C/G substitutions abolish transfer despite other uridines in the substrate, providing site discrimination. The full-length and truncated proteins are not interchangeable for all mechanistic claims: the shorter construct has greater measured activity, and the physiological role of the C-terminal extension remains unresolved. The paper also shows that the RumA-like iron-sulfur cluster is absent in this RlmCD structure; a common RNA m5U family assignment does not establish a shared metal requirement.

PMID:30388185 full text: explicit sp_1029 cloning and recombinant expression in E. coli BL21-Gold are described. The crystallographic complexes use the 1–454 E443Q construct and short U747/U1939 RNA analogues to trap covalent catalytic intermediates. These show the two uridines accommodated in a shared catalytic pocket, with sequence-specific contacts and F145 rearrangement; Figure 4 separately measures methyltransferase activities against U747- and U1939-containing substrates. The combination of native chemistry, separate substrate assays and structure supports dual specificity. Pocket geometry alone would not establish the substrate sites.

Importantly, the authors describe the earlier 18-nt RNA-bound complex as a physiologically irrelevant interaction likely caused by crystal packing. That older pose is not used as evidence for productive substrate recognition. The later engineered intermediates are not claimed to depict full-length RlmCD on an intact native ribosome.

## All-row decisions and core

All six original rows are preserved. Broad RNA processing/modification terms refine to existing GO:0070475 rRNA base methylation. Broad RNA methyltransferase and SAM-dependent methyltransferase activities refine to existing GO:0070041, retaining SAM in the mechanism. The two TreeGrafter annotations (PTN001666536) for the specific activity/process are accepted on independent native and recombinant evidence. Four MODIFY and two ACCEPT decisions; no NEW rows.

The PANTHER subfamily label containing “tRNA” is not used to assign a tRNA substrate: the native and recombinant target evidence establishes rRNA specificity. No family-wide evolutionary activity or exact cellular localization is inferred from the label. The core includes both U747 and U1939 chemistry and explicitly assigns G748 chemistry to RlmAII.

## Retrieval and validation

Actual Falcon and perplexity-lite fallback requests ran in parallel with normal publication retrieval. Falcon failed Edison authentication (403), and fallback failed Perplexity quota/authentication (401). No provider report was produced or fabricated. Normal gene-publication retrieval and additional PMID:26365244/28949991/30388185 caching succeeded; all decisive sources are full text. A real `just fetch-fitness STRPN rlmCD` attempt found no usable organism mapping/local or reachable FEBA source, so no fitness artifact exists. These failures do not supply biological evidence. Logs, baseline and payload proof are under `.cache/module-audit-logs/rlmcd-*`.

Strict/schema/source checks and ontology term validation pass with no warnings. The supported molecular chemistry is settled for this review; remaining questions concern physiological substrate recognition and the role of the C-terminal extension.
