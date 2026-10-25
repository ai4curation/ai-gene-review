# F13A1 database-source evidence

This source guide covers the 13 assigned database contexts. The separate direct-evidence lane retains ownership of its 34 contexts. Publication citations identify evidence without adding quotation strings, following the [campaign instructions](../../../projects/CLINGEN_MENDELIAN.md#curation-instructions).

## Performed chemistry and the ancestral assertions

The genuine author thesis reproduces the complete published [human F13A1 mutation study, PMID:27363989](https://doi.org/10.1002/humu.23041) and its supplement. The inspected Material and Methods identify sequence-verified NM_000129.3, a 732-residue human construct and COS-1 expression. Amine incorporation, alpha2-antiplasmin incorporation and fibrin-chain cross-linking are actual enzyme assays; the Fibrin Crosslinking Analyses section and Figure 4 text describe gamma dimers and alpha multimers. The supplementary recipes distinguish thrombin plus calcium from high-calcium conditions without thrombin. These are expressed-cell-lysate assays with appropriate substrates and deficient plasma, not isolated natural-product equivalence or proof that F13A1 performs thrombin's activating cleavage. No figure pixels were inspected in this lane.

The actual PTHR11590 v19 tree and MSA place P00488 at PTN002480698 with an exact 732-residue sequence. The target descends from the two asserted IBD nodes: PTN000904289 for protein-glutamine gamma-glutamyltransferase activity and PTN002612883 for fibrin-clot formation. The inspected target path has no relevant IBD NOT. The tree service separately exports inconsistent generic negative GO-slim flags; those are preserved as a display discrepancy, not substituted for the actual positive IBD. Target self-WITH is legitimate experimental grounding.

Current ARBA00088940 sets 0/1 and ARBA00090798 set 0 match the actual target FunFam and taxonomic fields. IPR008958, IPR023608 and IPR036238 map to the imported enzyme activity. [EC 2.3.2.13](https://enzyme.expasy.org/EC/2.3.2.13) and [RHEA:54816](https://www.rhea-db.org/rhea/54816) specify glutamine/lysine protein cross-linking. The official Rhea response was real HTML despite a requested TSV format. Mouse Q8BH61, MGI:1921395 and ENSMUSP00000048667 are source-donor identifiers; they are not human assay constructs. Only the original abstracts of [PMID:12529747](https://pubmed.ncbi.nlm.nih.gov/12529747/) and [PMID:18224415](https://doi.org/10.1007/s12185-007-0005-z) were accessible. Their positive knockout/plasma phenotypes are consistent with the transfer, while the independently read human original supplies target-specific performed chemistry.

## Intracellular, granule and extracellular pools

The actual selected author-original Methods and Results of [PMID:25331118](https://doi.org/10.1182/blood-2014-06-583070) describe washed human platelet sonication, a 12,000g clearing step and separation at 100,000g into soluble supernatant and membrane pellet. The soluble fraction contains F13A1 antigen and most measured transglutaminase activity. This supports refining the valid broad cytoplasm mapping to [cytosol, GO:0005829](https://www.ebi.ac.uk/QuickGO/term/GO:0005829). It does not deny membrane, granule or extracellular pools. The inspected thrombus and alpha2-antiplasmin experiments demonstrate functional cross-linking; surface-exposure assays remain distinct from fractionation. Access was to selected author-uploaded original renderings, with no complete-main export, figure pixels or supplement recovery.

The complete original of [PMID:39116293](https://pmc.ncbi.nlm.nih.gov/articles/PMC11459904/) was recovered as XML. Selected main Methods, retention/release Results, caption text and Discussion/limitations were read. Most human platelet F13A1 remained intracellular after the tested dual-agonist stimulation, while smaller surface and released pools persisted. Human and mouse responses differ. Figure 7 uses independently adjusted brightness settings; the equivalent-setting supplement and figure pixels were not inspected because those requests failed. The immunoblot cannot distinguish uncleaved zymogen from nonproteolytically activated F13A1.

The primary abstract of [PMID:8360253](https://doi.org/10.1002/jcp.1041560302) positively reports density-fractionated human alpha granules containing thrombin-inducible activity and both A and B subunits. Its full Methods were unavailable. The later original discussions distinguish this reported minor plasma-type A2B2 granule pool from the major cytoplasmic A-subunit pool. The proposed uptake route and detailed fraction purity were not independently established here. Thus alpha-granule lumen is retained as a non-core context, rather than rejected because cytoplasmic protein is more abundant.

## Exact Reactome roles

The six source graphs contain 247 fully fetched participant objects and six additional inline-only terminal chemical leaves (253 distinct reachable IDs). Eight chemical records occur inline, but two of these were also fetched in full. All participant, catalyst, active-unit, set/complex and regulation routes were replayed. Four sequence entities explicitly identify human P00488. This is source-model verification, not a claim to have read every cited primary paper.

| Source | Actual target role and boundary |
|---|---|
| [140599](https://reactome.org/content/detail/R-HSA-140599) | F13A1 is the extracellular thrombin-cleavage substrate and processed products; thrombin performs the cleavage. |
| [140847](https://reactome.org/content/detail/R-HSA-140847) | Cleaved tetramer dissociation and calcium-associated F13A1 product; the model does not resolve all active-state stoichiometries. |
| [140851](https://reactome.org/content/detail/R-HSA-140851) | Catalyst 140850/140849 contains active P00488 and cross-links fibrin. |
| [481007](https://reactome.org/content/detail/R-HSA-481007) | Alpha-granule entity 349759 and extracellular output 140600; F13A1 is cargo, not the exocytosis performer. |
| [6785895](https://reactome.org/content/detail/R-HSA-6785895) | F13A1 is an extracellular expression product, not the cytokine or transcriptional performer. |
| [9921091](https://reactome.org/content/detail/R-HSA-9921091) | Extracellular F13A1 catalyzes cross-linking of platelet-integrin-associated fibrin; substrate topology is not an integral-membrane assignment to the enzyme. |

The actual coordinate fields are 1–732, 39–732 and 1–38, while several display labels retain 731-based historical numbering. Both representations are preserved; no automatic offset or repair is inferred. The normal UniProt record separately describes initiator-methionine removal and activation-peptide processing. Processing chains and predicted transcript models are not inserted as natural alternative products or assumed functionally equivalent.

## Access and preservation

The five added normal publications were acquired through the genuine frozen fetch command, preserving all 253 preexisting runtime files. All 39 original normal sources and 226 original preimages remain exact. Reference availability flags describe complete-original access, while the immutable normal-cache metadata records what that cache contains. Complete original availability does not imply that every figure or supplement was read. Exact private read ranges, raw failures, source hashes and replayable participant/rule/ancestry proofs accompany this proposal.

# F13A1 direct evidence: chemistry, assemblies and detected locations

F13A1 supplies the catalytic A subunit of factor XIII. Its activation and its subsequent transglutaminase reaction are different events: thrombin cleaves the activation peptide, whereas activated F13A1 forms covalent protein cross-links. The displayed human UniProt sequence contains 732 residues. Removal of the initiator and activation peptide, including the annotated 39–732 chain, describes processing rather than alternative splicing. Separate transcript models and historical constructs are not assumed to have identical activity.

## Human catalytic experiments

The complete [2016 article and supplement](https://doi.org/10.1002/humu.23041) are reproduced in the [official Bonn author thesis](https://bonndoc.ulb.uni-bonn.de/xmlui/bitstream/handle/20.500.11811/7478/4941.pdf?sequence=1&isAllowed=y). Materials and Methods identify human F13A1 cDNA, sequence checking and expression in COS-1 cells. The monkey cell line is the host; the insert is human. Wild-type and patient-variant preparations were assayed for amine incorporation, alpha2-antiplasmin incorporation and fibrin cross-linking. The deficient-plasma experiments and Figure 4 describe gamma-chain dimers, alpha-chain multimers and clot architecture. Supplementary Methods include normal-plasma/recombinant controls and negative-control subtraction. The separate high-calcium experiment without thrombin is an in vitro activation condition. Modeling and docking are not direct binding measurements. Main text and supplementary Methods were read; figure pixels were not inspected. [PMID:27363989](https://pubmed.ncbi.nlm.nih.gov/27363989/)

These experiments support protein-glutamine gamma-glutamyltransferase activity, peptide cross-linking and fibrin-clot formation. The broad coagulation annotation is refined to the current fibrin-clot formation process, which is part of blood coagulation. This specifies the step F13A1 performs without assigning it thrombin's cleavage activity.

The [2000 activation-peptide paper](https://doi.org/10.1074/jbc.M000209200) uses bovine thrombin and synthetic human activation-peptide sequences. Experimental Procedures, HPLC Results and Table II establish the enzyme/substrate distinction. The proposed explanation of V34L cardioprotection remains a hypothesis. Its accessible author-upload original provides operative text, even though the normal publication cache contains an abstract. [PMID:10801785](https://pubmed.ncbi.nlm.nih.gov/10801785/)

## Older protein and cDNA studies

All original pages of the two 1986 PNAS papers were recovered. The placental structural study explicitly reports that it made no activity measurements; the opening page was also visually inspected. Its activity annotation is retained with independent human catalytic evidence, not presented as a new activity assay. Historical protein residue numbering is not silently equated with current sequence numbering. The companion cDNA paper reports human placental cloning, a 732-residue sequence and RNA studies. Its discussion of plasma protein and the absence of an obvious signal peptide does not demonstrate a secretion route. Selected text was read through OCR; sequence figures were not used to reconstruct a current product. [PMID:2877456](https://pmc.ncbi.nlm.nih.gov/articles/PMC386858/), [PMID:2877457](https://pmc.ncbi.nlm.nih.gov/articles/PMC386859/)

The accessible primary summary of the [1973 plasma/platelet study](https://doi.org/10.1016/S0021-9258(19)44312-3) distinguishes plasma A2B2 from platelet A2 and reports activation/cross-linking observations. Complete original Methods remain unavailable. The actual human plasma material in the 1986 structural paper independently corroborates an extracellular pool. A soluble extracellular location does not imply microparticle localization, conventional secretion, or exclusive extracellular residence. [PMID:4405643](https://pubmed.ncbi.nlm.nih.gov/4405643/)

## Twenty-two reported physical associations

The source is **Haenig/NeuroNet**, not the separate HuRI publication. The [main article](https://doi.org/10.1016/j.celrep.2020.108050), STAR Methods and Tables S1/S2 identify F13A1 bait clone CCSB_8309 and human cDNA/fragment fusion screens. Nonautoactivating baits, three yeast reporters, repeated screens and pairwise tests support the reported associations. All 22 imported literal partner accessions have current IntAct array, pooling and validated-two-hybrid records. Those records are not 66 independent biological interactions. [PMID:32814053](https://pubmed.ncbi.nlm.nih.gov/32814053/)

The source partners are O15273, O60636, O60830, P19388, Q14005-2, Q2NKQ1-4, Q6DKI2, Q6NXG1, Q6NXG1-3, Q6P4D5-2, Q6ZMI0-5, Q7Z783, Q8IUR5-4, Q8WXK3-2, Q8WZ73-3, Q96EF9, Q96GL9, Q96MX0, Q99944, Q9BXL8, Q9NZC7-5 and Q9Y2M5. The accession suffixes describe partners, not F13A1 isoforms. Current gene-level joins to the original table do not verify historical insert sequences. Q7Z783 lacks a current GeneID; the original C8orf76 entry and current ZHX1-C8orf76 record retain a naming/version boundary. Positive literal interaction records are retained without inventing cross-version clone equivalence.

Specific functional binding terms were considered. These assays do not establish a coordinated adaptor role, regulation of an enzyme, a physiological transglutaminase substrate or transfer of a partner's activity. The associations therefore remain non-core. Study-wide mammalian validation is not assigned to these pairs without target-specific results.

## Tissue-associated ECM detection

The three studies use ECM enrichment and mass spectrometry, with target-level F13A1/P00488 entries in actual original workbooks. They support the reported tissue-associated locations, retained as non-core, while leaving activation state, cellular origin and tissue-specific causal functions unresolved.

| Source | Actual target support and context |
| --- | --- |
| [PMID:25037231](https://doi.org/10.1186/1471-2407-14-518) | Methods and Additional file 2: human normal colon and colon tumors, sequential depletion of cellular components, F13A1 in the complete and matrisome tables with multiple unique peptides. |
| [PMID:28344315](https://doi.org/10.1038/leu.2017.102) | Methods and Tables S2/S3: human bone marrow, healthy and myeloma groups; P00488 in the complete dataset and matrisome subsets, including 18 unique peptides in the complete dataset. Actual publisher full text is available despite the abstract-limited normal cache. |
| [PMID:28675934](https://doi.org/10.1021/acs.jproteome.7b00191) | Materials and Methods and Supplementary Table S1 C/D: normal and metastatic omental ECM, including P00488 in fractionated normal samples. Both crude and urea-soluble preparations follow ECM enrichment; crude does not mean untreated whole tissue. |

The raw colon, bone-marrow and omentum source extensions are retained separately from the ordinary seeded annotation fields. None of these proteomic identifications measures an active F13A1 molecule or establishes a cancer mechanism.

## Remaining microparticle access gap

The [human-plasma microvesicle survey](https://pubmed.ncbi.nlm.nih.gov/22516433/) is bibliographically verified, but the complete operative Methods and the F13A1-specific table remain unavailable. A previously saved attachment is an error response, not a workbook. The source assertion remains undecided; neither an abstract-only survey nor soluble plasma detection establishes the exact target microparticle assignment.

Publication caches remain immutable. Access flags distinguish the actual external originals available from the narrower passages inspected and from normal-cache metadata. No new publication quotations or process assertions are introduced.

## Core synthesis: reaction, assemblies and compartment limits

The one catalytic unit uses [protein-glutamine gamma-glutamyltransferase activity, GO:0003810](https://www.ebi.ac.uk/QuickGO/term/GO:0003810). Its covalent glutamine/lysine cross-linking directly supports both [peptide cross-linking, GO:0018149](https://www.ebi.ac.uk/QuickGO/term/GO:0018149) and [fibrin-clot formation, GO:0072378](https://www.ebi.ac.uk/QuickGO/term/GO:0072378); current `is_a`/`part_of` ancestry contains neither as an ancestor of the other. The molecular reaction and physiological clot-stabilization setting are facets of one activity. No separate carrier, binding or thrombin-like catalytic unit is inferred.

The decisive human evidence remains [PMID:27363989](https://doi.org/10.1002/humu.23041): Materials and Methods (human construct and COS-1 expression, pentylamine and alpha2-antiplasmin assays), Fibrin Crosslinking Analyses/Figure 4 text, and Supplementary Methods (assay recipes and plasma/recombinant controls). The complete article and supplement are available within the previously linked author thesis; this synthesis reread the operative text, not figure pixels. The older plasma/platelet source's complete main remains unavailable. No new original was acquired.

The broad [transferase complex, GO:1990234](https://www.ebi.ac.uk/QuickGO/term/GO:1990234) identifies the accepted A-subunit-containing catalytic assembly context. It does not name a new complex or prescribe invariant stoichiometry. The plasma A2B2 zymogen contains carrier B subunits; activation and B-subunit dissociation are distinct from F13A1's subsequent cross-linking reaction. The extracellular location attached to this clot-stabilizing core is not a rejection of the independently supported cytosolic pool. Platelet fractionation and induced activity establish that pool; they do not by themselves demonstrate intracellular fibrin catalysis or identify all substrates of retained F13A1. The two proposed experiments distinguish compartment, activation state and substrate cross-linking.

Positive minor alpha-granule localization and contextual ECM detections remain exactly as reviewed. The microparticle assertion remains undecided. The displayed 732-residue protein, proteolytically processed chains, patient variants and separate transcript models are not made functionally equivalent. The selected 23 normal sources and two machine inputs are carried unchanged from the accepted integration; no cache or publication availability flag is changed by synthesis.
