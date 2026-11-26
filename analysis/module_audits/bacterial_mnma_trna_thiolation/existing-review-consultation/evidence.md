# KT2440 Tus relay and MnmA consultation

This review preserves six original KT2440 records and all 26 annotation payloads, including three historical NEW proposals. It also inspects the released E. coli and KT2440 IscS reviews without changing them. The mechanistic comparator is E. coli; no direct KT2440 reconstitution, native growth phenotype, or isolated target-enzyme assay is asserted.

## Sequence and role evidence

The frozen KT2440 records identify PP_3993/TusD, PP_3994/TusC, PP_3995/TusB and PP_3996/TusE as consecutive ordered loci. Their distinct InterPro/NCBIfam/PANTHER classifications, rather than a generic Dsr-like fold or submitter protein name, support the proposed Tus complex. Consecutive locus names support genomic neighborhood, not demonstrated cotranscription.

The reproducible BLOSUM62 global alignments in sequence-bridge.yaml use frozen E. coli and KT2440 UniProt sequences. E. coli MnmA D99/C102/C199 align to KT2440 D105/C108/C204; TusA C19 to C17; TusD C78 to C77; TusE C108 to C110. These are homologous residue mappings, not exact experimental-construct identities. Target MnmA ATP sites and TusA/TusE active sites also have curated HAMAP/PIRSR support. The D-type MnmA sequence does not by itself decide Fe-S dependence.

The inferred location of this soluble relay and its tRNA substrate reaction is the cytosol. The inference combines a soluble, structurally characterized homologous complex/reconstitution with target-specific classifications and, for MnmA/TusA, curated HAMAP location statements. It is not a target localization experiment. ARBA-only location text, absent transmembrane annotations alone, and GO cross-references are not the evidence anchors. The localizations do not imply an independent catalytic function for TusB or TusC.

## Primary sources and access limits

PMID16387657 (DOI10.1016/j.molcel.2005.11.001), available abstract: “Efficient 2-thiouridine formation in vitro was reconstituted with recombinant TusA, a TusBCD complex, TusE, and previously identified IscS and MnmA.” It explicitly reports IscS-to-TusA transfer and TusE stimulation of TusA-to-TusD transfer. The source does not establish native KT2440 flux. A web search and the author laboratory's bibliography (https://rna.chem.t.u-tokyo.ac.jp/publications.html) did not yield an accessible primary full text; its link returns to PubMed. No source cache was refreshed.

PMID16472754 (DOI10.1016/j.str.2005.11.009), available abstract: “In vivo mutant analyses revealed that only Cys78, in the TusD subunit, participates in sulfur transfer during the s2U modification process.” The structure is an E. coli TusBCD heterohexamer, not a KT2440 structure. This supports the complex's covalent sulfur-bearing subunit and the conserved-target inference. It does not demonstrate independent purified TusD turnover. The accessible abstract reports the relevant assay; failure to obtain the full text is not contrary evidence.

PMID16871210 (DOI10.1038/nature04896), available abstract: “The adenylated RNA intermediate is trapped.” This supports ATP-dependent substrate activation by the characterized MnmA–tRNA complex. Target ATP binding is inferred using HAMAP ATP-binding features, not independently proved by a GO cross-reference.

PMID33526615 is an E. coli study of indirect translation/regulatory consequences of TusA deficiency. Its abstract says: “the lack of the thiolation status of wobble uridine (U34) nucleotides present on Lys, Gln, or Glu in tRNAs has a major consequence on the translation efficiency of proteins”. This is not direct KT2440 cell-division machinery or a reason to add a cell-division process annotation.

## Terminal chemistry limits and pathway boundary

Full PMID39660893, read in the frozen preflight PMC11784392.txt, explicitly states: “Consequently, proof that TusE transfers the persulfide directly to MnmA in E. coli remains to be definitively provided.” The text extraction contains doubled spaces around italicized names; the reviewed interpretation follows the whole paragraph, including barely labeled MnmA in the original sulfur-relay experiment. TusE therefore supplies sulfur to the terminal MnmA–tRNA reaction, while direct covalent MnmA loading is not described as a demonstrated molecular event.

The review compares conflicting Fe-S-dependent and Fe-S-independent E. coli results and concludes: “These apparent differences in experimental findings need to be investigated and clarified in future studies.” No universal Fe-S requirement or absence is assigned to KT2440 MnmA. ATP-dependent U34/C2 thiolation is retained independently of that unresolved terminal mechanism. C5 modification by MnmE/MnmG/MnmC is a separate branch, not an asserted obligatory downstream sequence of the C2 reaction.

## Ontology and participation

Current official QuickGO definitions and ancestor responses are frozen in go-definitions.yaml. GO0103016 is a sulfurtransferase/transferase descendant; GO0002143 is a tRNA-modification/processing descendant; cytosol is a cytoplasm descendant. Broad true rows are refined accordingly. GO0097163 instead describes covalently binding sulfur and delivering it to an acceptor; it is not a descendant of GO0016783. TusD's existing sulfurtransferase claim is interpreted as the conserved complex-dependent transpersulfidation role, supported by the active-site and relay evidence, not an autonomous tRNA-modifying enzyme. Its carrier core does not imply that these GO terms have a hierarchy they lack.

TusB/TusC contribute the structure of the experimentally characterized relay complex, so their existing process claims describe work by the proteins rather than necessity of an inert substrate. No NEW process or binding assertions are added. The three inherited NEW rows and their TAS/source metadata are preserved; the reasons clearly distinguish authored homolog inference from direct target experiments.

## IscS reuse and research provenance

The released E. coli IscS review distinguishes its cysteine-desulfurase chemistry, TusA/ThiI sulfur delivery, Fe-S assembly and thiamine roles. The KT2440 review explicitly treats partner allocation as unmeasured. Neither is replaced by a Tus-only function. There is no blocking contradiction requiring edits to either frozen IscS review.

Six normal Falcon attempts failed with HTTP403 authentication errors; their exact logs are retained. Existing OpenScientist reports remain discovery provenance and were not overwritten or used as independent experimental evidence. Original notes are append-only; this account supersedes their unsupported claims of established operon expression, obligatory downstream C5 processing, or direct measured KT2440 chemistry.

The existing generated report's mechanistic pointers were checked independently. Its printed MnmA cysteine numbering is one residue lower than the frozen full-sequence positions reproduced here, and its blanket TusA/B/C/D/E carrier recommendation is not adopted for structural TusB/C. Its 'operon' and 'relay-committed' wording exceeds the demonstrated target neighborhood/role evidence. These limitations are recorded without editing the report.

All six PAINT-loss commands completed, but each target accession was absent from its cached family tree. The command's generic 'No IRD or IKR loss' footer is therefore not evidence of a verified loss-free lineage. No invented node placement or evolutionary loss is used in these reviews.
