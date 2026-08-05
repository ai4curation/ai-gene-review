# ELAVL1 (HuR) review notes

## Review scope and research provenance

This review covers all 93 grouped GOA records seeded for human ELAVL1 (UniProtKB Q15717). I inspected the reviewed UniProt record, the complete GOA table, all 28 cached PMID records, the available full text for PMID:16126846, PMID:21266579, PMID:23056314, PMID:25416956, PMID:25959826, PMID:26595526, and PMID:27974568, and the abstracts for the remaining cited papers. The configured Falcon deep-research request failed with HTTP 402 and the Perplexity-lite fallback failed with HTTP 401. No provider-named research file was authored; the manual synthesis is in ELAVL1-deep-research-manual.md.

## Identity, architecture, and localization

ELAVL1 encodes the ubiquitously expressed ELAV-family RNA-binding protein HuR, a 326-residue protein with three RNA recognition motifs (RRMs). RRM1 and RRM2 form the principal tandem AU-rich-element recognition module; RRM3 also contacts RNA and contributes to oligomerization. The reviewed UniProt record describes a predominantly nuclear protein that shuttles to the cytoplasm after stimulus-dependent phosphorylation. Nuclear/nucleoplasmic and cytoplasmic/cytosolic locations are therefore integral to its post-transcriptional function, whereas P-body, stress-granule, nucleolar, and membrane observations are contextual rather than defining steady-state locations.

The founding study directly established that recombinant HuR binds AU-rich elements: [PMID:8626503, "The purified recombinant protein binds avidly to the AU-rich element in c-fos and interleukin-3 mRNAs."] Structural work showed why the more specific GO molecular-function term is appropriate: [PMID:23519412, "Both the structure and the FPA analysis indicated that RRM1 is the primary ARE-binding domain in HuR"]

## Core molecular mechanism

HuR recognizes U-rich and AU-rich elements, usually in target mRNA 3-prime UTRs, and protects many bound transcripts from degradation. Direct experiments on uPA/uPAR mRNAs combine binding, in-vitro stabilization, cellular stabilization, depletion, and regulated cytoplasmic accumulation: [PMID:14517288, "HuR stabilized an ARE(uPA)-containing RNA substrate in vitro and stabilized in HeLa Tet-off cells both endogenous uPA and uPAR mRNAs"]

The same mechanism is supported across iNOS, COX-2, GATA3, PDCD4, VASH1, leptin, and m5C-marked oncogenic transcripts, although the affected physiological outputs are target- and cell-context-dependent. For iNOS, HuR competes with the destabilizing factor KSRP at a shared ARE: [PMID:16126846, "We were able to demonstrate that KSRP and HuR compete for this binding site"] For PDCD4, HuR occupancy antagonizes miR-21 silencing, while ERK8 phosphorylation displaces HuR: [PMID:26595526, "phosphorylation of HuR by ERK8 prevents it from binding to PDCD4 mRNA and allows miR-21-mediated degradation of PDCD4."]

HuR can also promote translation of selected bound messages. This is a consequence of its post-transcriptional RNA regulation rather than a catalytic activity, and target-specific phenotypes should not be mistaken for separate core molecular functions.

## Protein interactions and oligomerization

Low-molecular-weight inhibitor studies support functional HuR homodimerization before RNA binding: [PMID:17632515, "A mathematical and experimental analysis of the compounds' mode of action suggests that HuR homodimerizes before RNA binding"] Homodimerization is therefore retained, but it is subordinate to RNA recognition and stabilization.

The GOA set contains numerous generic protein-binding annotations from targeted and high-throughput interaction studies (UBC, SDCBP, ATXN1, TARDBP, YBX1, SHFL, PLEKHN1, DHX36, ILF3, AGO proteins, and HuR itself). These interactions may be experimentally real, but GO:0005515 does not state the functional consequence. All exact GO:0005515 duplicates are treated consistently as over-annotations. The phylogenetic protein-RNA adaptor term is retained because ELAVL-family proteins bind RNA while coordinating additional proteins; the term definition specifically requires bringing a protein and an RNA together. Individual interactions are not promoted to new GO functions without direct mechanistic evidence.

## Boundaries on broad and transferred terms

- Generic nucleic-acid, RNA, mRNA, and 3-prime-UTR binding terms are biologically true but less informative than GO:0035925, so they are modified to the experimentally established AU-rich-region binding activity.
- The broad regulation-of-mRNA-stability term is modified to mRNA stabilization, which is the dominant, direct biochemical outcome.
- Orthology-propagated autophagy, glucose response, proliferation, superoxide generation, stem-cell maintenance, and silencing terms are retained only as non-core/contextual processes.
- Orthology-propagated mRNA destabilization is retained as non-core because HuR effects can be transcript- and partner-dependent, but it is not used in the core-function synthesis.
- Endoplasmic-reticulum membership is removed: HuR is a soluble nucleocytoplasmic shuttling protein without a signal peptide or transmembrane segment, and no direct human ER-residence evidence was identified.
- The membrane HDA record is treated as over-annotation because it arose from a broad NK-cell membrane proteome and does not establish a functional membrane location for soluble HuR.
- The double-stranded-RNA-binding IDA record from PMID:21266579 remains UNDECIDED. The cached full text is available but does not name HuR/ELAVL1 in the searchable article body; the evidence may reside in supplementary proteomic material, so it is not appropriate to remove an experimental curator annotation.

## Existing annotation decisions

All 93 grouped annotations were adjudicated. Exact duplicate GO terms use compatible actions: all GO:0005515 records are MARK_AS_OVER_ANNOTATED; all GO:0035925 and GO:0070935 records are ACCEPT; all GO:0003723 records are MODIFY to GO:0035925; all GO:0003729 and GO:0003730 records are MODIFY to GO:0035925; all nucleus, nucleoplasm, cytoplasm, and cytosol records are ACCEPT; all stress-granule records are KEEP_AS_NON_CORE; and all GO:1990904 records are KEEP_AS_NON_CORE.

## Proposed additions and omissions

No conservative NEW term is necessary. The unusually rich GOA set already captures the specific core activity, stabilization process, miRNA-antagonism mechanism, oligomerization, shuttling locations, and major contextual processes. Adding target-by-target downstream phenotypes would amplify pleiotropic consequences rather than improve the core functional model.

## Open questions

- Which RNA sequence/structure features, beyond U-richness, determine whether HuR stabilizes, destabilizes, or changes translation of a target?
- Which protein partners are directly recruited by HuR as an adaptor rather than merely co-recovered through shared RNA?
- Does isoform 2 alter target specificity, oligomerization, localization, or stimulus-dependent shuttling?
- Can the reported double-stranded-RNA-binding activity be verified from the supplementary evidence for PMID:21266579?
