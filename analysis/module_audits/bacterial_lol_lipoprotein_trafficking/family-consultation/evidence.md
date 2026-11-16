# Lol family scope consultation (2026-11-07)

This audit preserves the three published family reviews' twelve PAINT assertions, their node ids, dates, seed sets and original terms. It distinguishes the current PANTHER HMM classifications from the PAINT phylogenetic tree. Original publications and raw family files were not refreshed. `baseline.json` captures the original texts and hashes; `tree-audit.json`, `ontology.json` and `variant-identities.json` contain independently retrieved official source data.

## Actual trees, not inference from missing annotations

Source API: `https://pantherdb.org/services/oai/pantherdb/treeinfo?family=PTHR24220` (and corresponding PTHR30489/PTHR35869 URLs). Retrieved through the repository's normal `panther_trees.load_family` helper; compressed raw API-derived caches remain ignored. The structured audit retains each asserted term separately, its seed leaves and its descendant membership.

PTN000655654 contains 294 leaves, including the E. coli LolD and FtsE leaves and the NikD, YejF and Rv2688c seed leaves.

PTN000656700 contains 15 leaves, including P75957 and Q9HZL7; Q88KY4 is not present in the returned tree.

PTN002383692 contains ten leaves including P33916, but excludes the E. coli LolD and FtsE leaves.

PTN002449941 and its P16679 seed are not in the returned tree. Its immutable PAINT assertion is retained as unresolved; no current HMM or missing-annotation observation is used to infer its historical placement. PTHR30489 PTN002524722 has 46 descendants, including both E. coli LolC and LolE; PTHR35869 PTN002185387 has nine descendants, including E. coli and P. aeruginosa LolA. The KT2440 representatives are not returned as leaves. That does not demonstrate loss, and their current UniProt classifications remain independent membership evidence.

The broad ABC-family knowledge is retained. Different contemporary HMM families for the seed ATPases do not invalidate their observed common PAINT ancestor. Pruning the transmembrane-transport claim from characterized LolD/FtsE branches is a mechanistic scope judgment, not a denial that the donor transporters have transport functions, a criticism of donor count, or a newly inferred evolutionary loss.

## Reaction definitions and assembly scope

Official QuickGO definitions retrieved from `https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0022857` and the analogous URLs saved in `ontology.json`:

- GO:0022857 requires transfer from one side of a membrane to the other.
- GO:0055085 requires transport across a lipid bilayer.
- GO:0140306 recognizes mature lipoproteins in the inner membrane and releases them for periplasmic transport. Its definition attributes the function to LolCDE.
- GO:0140598 means binding and accompanying a lipoprotein between cellular locations. It does not itself assert insertion or a particular LolB partner.

PMID:10783239 is abstract-only in the protected cache. Its explicit mechanistic statement is sufficient for the bounded extraction distinction: “The LolCDE complex differs mechanistically from all other ABC transporters as it is not involved in the transmembrane transport of substrates.” We do not claim unconsulted full-text assay details. PMID:11844772 is full text and establishes native E. coli disruption/release consequences. PMID:17509078 is abstract-only but explicitly reports reconstitution from separately purified subunits, supporting direct functional contribution beyond necessity alone. Its additional LolD+LolE release result is restricted to the phospholipid/proteoliposome reconstitution conditions; it does not contradict the native LolC requirement in PMID:11844772 or prove an alternative wild-type E. coli pathway.

PMID:41557797 full text supports an E. coli-specific substrate-LolE peptide interface. The membrane components jointly create the cargo cavity, while LolD supplies ATP hydrolysis. Family membership or operon order does not independently establish a shared C/E specialization across all lineages. PMID:42091888 directly characterizes Acinetobacter homomeric LolDF. That paper is comparative mechanism evidence; actual member assignments must be verified separately, and a compatible LolDF assembly cannot be manufactured by pairing arbitrary ABC-family hits.

The independent E. coli FtsEX primary PMID:22006326 was consulted through its official PubMed/PMC abstract (https://pubmed.ncbi.nlm.nih.gov/22006326/; https://pmc.ncbi.nlm.nih.gov/articles/PMC3215046/), without creating or altering a publication cache. Exact excerpt: “Here we identify FtsEX as a regulator of cell-wall hydrolysis at the division site.” It reports direct FtsX–EnvC recruitment and a signaling model, rather than substrate translocation. This is used to explain the FtsE branch, not to infer an unmeasured evolutionary loss or universally require ATP hydrolysis in every assay. Later primary PMID:32636250 explicitly distinguishes the NlpD-positive context in which recruitment can suffice; the family review makes no unconditional hydrolysis-requirement claim.

## Carrier versus insertion and exact constructs

PMID:36716372 full text, Methods: “amplify C. vibrioides strain CB15 genomic DNA.” The protein is CC_3705. The key experimental construct was explicitly modified: “we replaced the final 12 residues of cviLolA with those of ecoLolA”. The strongest complementation used permissive E. coli backgrounds including deletion of lpp. The paper also states that native cviLolA was very poor at complementing E. coli lolA deletion. This supports a functionally informative engineered carrier/insertase construct and a bounded native-protein inference; it does not establish an isolated native CB15 insertion assay, NA1000 identity, universal LolA insertion, or universal LolB dispensability. Classical E. coli carrier evidence is retained from PMID:7628437 (abstract-only) and PMID:19307584 (full text).

Current official UniProt search captures independently identify CB15 CC_3705/Q9A261 as PTHR35869:SF1 and F. johnsoniae Fjoh_2111/A5FI22 as the same subfamily. PMID:40050408 is a peer-reviewed full-text study supporting F. johnsoniae LolA1/LolB1 roles with cargo specialization and residual alternative trafficking. This is not a universal inability to exchange proteins, nor proof that every distant LolA copy has the same cargo.

The native F. johnsoniae LolB1 Fjoh_1066/A5FL25 and B. thetaiotaomicron BT_3463/Q8A243 have IPR025634 and PF14125 (DUF4292), with no PANTHER cross-reference in the retrieved records. PMID:41676706 is a preprint, not a peer-reviewed article; its BT_3463 insertion assays are useful additional context but do not replace the peer-reviewed F. johnsoniae evidence. These distinct distant proteins must not be assigned the classical E. coli LolB family by name alone. Frozen E. coli LolB has curated LolB membership plus NCBIfam TIGR00548, IPR004565 and PF03550, without a PANTHER assignment.

## Selector limits reported to module owner

The verified Acinetobacter ADP1 LolD Q9EYM2 is assigned PTHR42798:SF2 rather than PTHR24220:SF689. A separate descriptor combining its actual family and exact supported member/activity is appropriate. No whole-PTHR42798 Lol activity assessment is fabricated here. Likewise a LolF-named protein's shared PTHR30489 membership does not establish a second obligatory membrane paralog. Capacity must depend on the characterized compatible assembly, not a family-only hit or arbitrary cross-species pair.

All three reviews retain their original annotation slice and positive conserved roles. Added prose distinguishes contribution to assembled release, transport versus extraction, actual tree placement, and limited carrier/insertase compatibility. Missing broader experimental or phylogenetic information remains explicit rather than being converted into a false universal statement.

## Additional same-subfamily substrate boundary

F. johnsoniae LolA2/Fjoh_1085/A5FKZ5 is also assigned PTHR35869:SF1 in the official UniProt record. The exact record is preserved in `variant-identities.json`. PMID:40050408 places lolA2/lolB2 in a flexirubin biosynthesis locus and states: “LolA2 and LolB2 might be involved in the synthesis and/or transport of this pigment”. The paper's absence of a gliding/T9SS phenotype in the lolA2 mutant does not prove inability to carry lipoproteins; no biochemical substrate-negative assay is claimed. Conversely, the positive LolA1 results do not establish every SF1 member has the same substrate. The two full-family term scopes therefore remain unresolved, with canonical positive evidence and all gamma-restricted PAINT assertions preserved. There is no justified new loss node or negative member exception.
