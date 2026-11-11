# Comparative module audit notes

## 2026-10-26 initial audit

The scope is chain-elongated methionine glucosinolates, not all glucosinolates. The 2025 critical review (DOI:10.1016/j.bse.2025.105033) concludes that evidence is conclusive within Brassicaceae and isolated reports elsewhere require independent confirmation. DOI metadata and the full author-deposited abstract were inspected at https://researchprofiles.ku.dk/en/publications/inconclusive-evidence-for-chain-elongated-methionine-derived-gluc/; the PDF returned 403, so no full-text-specific claims are made. Normal reference fetching preserves the DOI metadata and portal abstract separately. The broad order-wide template was narrowed accordingly, without claiming every species has every decoration/specifier branch.

PMID:20303821 is an older three-phase synthesis. PMID:36823985 compares crop implementations; PMID:40157132 emphasizes duplication, loss and balanced phylogenetic sampling. PMID:42123309 supplies recent Brassica context but its broad exclusivity wording and CYP83F1 nomenclature are not adopted uncritically. Native assays, heterologous reconstruction and sequence inference are distinguished.

The IPMI reaction belongs to a heterodimer with large and small subunits from different families. Arabidopsis IIL1 and Thlaspi TAV2_LOCUS24872 match PTHR43822:SF2 despite its surprising HOMOACONITASE, MITOCHONDRIAL label. Arabidopsis SSU3 is SF8; Thlaspi TAV2_LOCUS13090 is SF7 and an SSU2/3 co-ortholog. Their common family is constrained by the contributing role, not interpreted as universal glucosinolate specificity.

Exact MF semantics matter. GO:0003862 is the leucine substrate reaction, not a generic IPMDH descriptor; GO:0010326 is unelongated methionine transamination, not all elongated homologs. These module activities are free text pending specific GO terms. Conversely, live GO:0120526 explicitly uses L-polyhomomethionine, so its label does not restrict CYP79F chemistry to one chain length. FMO GS-OX1 has a broader substrate range than GO:0080102. Target source and chain length are recorded in the individual review.

GSTU20 and GSTF11 are separate families. Their genetics supports a native conjugation role but the actual intermediate reaction has not been reconstituted. GGP1 forms a Cys-Gly conjugate; PMID:21712415 explicitly leaves Cys-Gly versus Cys usage by SUR1 unresolved. The internal edge remains a knowledge gap. UGT74C1 is an accessory route, not the only glucosyltransferase. Decoration can occur in more than one order, and specifier branches are optional.

Thlaspi mappings are not uniformly one-to-one: MAM and SSU are co-ortholog cases, the SUR1 model is marked Fragment, and localization is inferred. Native gene symbols use TAV2 loci. A directly assayed Brassica juncea MAM1-A exemplar is being reviewed separately (C5J4P1; PMID:31023839); PMID:39322014 concerns the distinct MAM2-A isoform.

Status: literature, family and member reconciliation remains in progress. No PR has yet been opened for this module. Existing module changes in broadPR5076 were inspected as overlap leads, not assumed to complete this audit.

## 2026-10-26 final integration and independent QA

The module now has 31 curated references and 35 member reviews (453 rows:444 original assertions, seven retained prior proposals and two comparative contributes_to MF proposals for Thlaspi IPMI subunits). Twenty activity annotons include a heterodimer with two family-grounded active units and alternative UGT74B1/C1 routes. All member validations pass. Independent scientific QA corrected copied location citations, made AOP2 optional within decoration, qualified modeled TFP iron coordination, and added target-direct CYP79F2 and GGP1 substrate evidence. No additional scientific blocker remains. Full validation is running; the audit is incomplete until its separate PR passes checks and merges.
