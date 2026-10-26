# FASTKD2 database evidence guide

This guide records the database-source portion of the FASTKD2 review. The fourteen database contexts are retained in their original order: twelve ACCEPT, one KEEP_AS_NON_CORE and one UNDECIDED. The direct experimental sources are documented in the accompanying direct evidence guide. The decision records and primary-paper scope notes distinguish a database assertion from the experiment supporting it.

## Phylogenetic inference: GO_REF:0000033

The actual PANTHER PTHR21228 version 19 tree and multiple sequence alignment place human Q9NYY8 at PTN002501556, below ancestral node PTN000477113. The target's ungapped alignment is the complete 710-residue canonical sequence. Five literal IBD records match the current target IBA terms: RNA binding, mitochondrial RNA processing, mitochondrial matrix, mitochondrial RNA granule and regulation of mitochondrial mRNA stability. Seven family IBD records were inspected; two plant chloroplast assertions lie off the target path. No family NOT record interrupts the target path. This is a check of actual ancestry and assertions, not a judgment based on the number of donors. The target appears among the experimental descendants for RNA binding, matrix and granule; that self-WITH is legitimate.

Human FASTKD2 iCLIP directly identifies both rRNA and ND6 mRNA contacts (PMID:26370583). Thus RNA binding has useful scope beyond the narrower rRNA-binding term. Target perturbation changes mitochondrial RNA abundance and processing, supporting participation in RNA maturation without assigning autonomous nuclease or kinase activity. Endogenous imaging in PMID:25683715 supports mitochondrial RNA granules with partial nucleoid colocalization; matrix is the surrounding RNA-handling compartment rather than a claim of exclusive localization to one structure.

The mRNA-stability inference is experimentally grounded in FASTKD3 (PMID:27789713) and FASTKD1/TBRG4, also called FASTKD4 (PMID:28335001). The FASTKD3 study uses human U2OS knockout, full-length and RAP-deletion rescue, and a transcription-block decay time course. Loss of FASTKD3 increases the half-lives of selected mRNAs. FASTKD1/4 have distinct and sometimes opposing transcript effects; precursor accumulation also makes processing relevant. The GO term accommodates both stabilization and destabilization. These results support the actual ancestral placement without transferring identical substrates or direction to FASTKD2.

Human FASTKD2 binds mature ND6 coding-region RNA and its loss reduces mature ND6 (PMID:26370583). These observations corroborate the inherited regulatory claim, but target RNA contact and steady-state abundance are not an isolated measurement of FASTKD2-dependent decay. PMID:29617655 explicitly raises secondary ND6 destabilization when mitochondrial large-subunit assembly or translation fails. This alternative remains open. Predominant 16S-rRNA and ribosome-assembly biology is not evidence of loss of the ancestral mRNA function.

## Human Protein Atlas: GO_REF:0000052

The actual ENSG00000118246 XML record reports supported mitochondrial localization using antibody HPA067191 in CACO-2, Hep-G2, U2OS and KOLF2.1J cells. The selected U2OS immunofluorescence image was inspected. Its epitope spans residues 299–394. This supports the organelle-level location; it does not establish matrix localization, a natural isoform-specific distribution or a mature cleavage site. The GO_REF title describes the annotation method, not gene-specific assay evidence. Mitochondrion remains informative under the organelle-location policy.

## ARBA: GO_REF:0000117

The actual ARBA00026962 rule has GO:0005739 as a consequent. All 380 condition sets were inspected against the available target domain and family information. A complete matching clause for Q9NYY8 was not independently reproduced: the captured InterPro/PANTHER matches do not identify one, and FunFam conditions remain unresolved. This is an explicit provenance limit. The mitochondrial prediction is retained because independent human HPA and FASTKD2-GFP localization evidence supports it (PMID:26370583); the rule is not presented as an independent experiment.

## Combined electronic mapping: GO_REF:0000120

The actual UniProt SL-0170 mapping is mitochondrial matrix. Ensembl identifies mouse ENSMUSG00000025962 / ENSMUSP00000027103, UniProt Q922E6, as a one-to-one ortholog of human ENSG00000118246 / ENSP00000385990. Mouse GOA contains a matrix IDA source to PMID:29617655 as well as propagated human-derived rows. The chain therefore has experimental grounding and is not exclusively reciprocal propagation. The original mouse-heart fractionation and PTCD1/RPUSD4 association data provide context, while human RNA-granule/module studies independently support the compartment (PMID:25683715; PMID:27974379). No human natural-isoform cleavage boundary is inferred.

## Reactome matrix assertions

All three source events have an actual protein route to FASTKD2, not merely a suggestive title. The recursively inspected closure contains 35 objects and 40 typed edges. Protein entity 9837146 points through reference entity 229275 to Q9NYY8 and carries mitochondrial matrix compartment GO:0005759.

- R-HSA-9837212 has FASTKD2 as input; its output complex 9837175 also contains that same protein.
- R-HSA-9936243 reaches FASTKD2 through catalyst activity 9936263 and module 9936292.
- R-HSA-9937369 reaches FASTKD2 through catalyst activity 9937392 and the same module 9936292.

These paths support the cellular-component annotations. They do not assign the event's pseudouridine-synthase chemistry to FASTKD2. The 1–710 sequence range is a database representation, not a measured mature processing boundary. Human module studies support association with RNA-modification machinery, but do not isolate the FASTKD2-specific chemical step (PMID:27667664; PMID:27974379).

## Nucleoid mapping: GO_REF:0000044

The actual SL-0269 mapping is mitochondrial nucleoid, GO:0042645, and the official UniProt record connects the location to PMID:20869947 and PMID:25683715. The latter original paper was recovered beyond its abstract-only normal cache. Endogenous 143B-cell imaging reports substantial overlap with GRSF1 and BrU-labeled mitochondrial RNA, and partial overlap with anti-DNA nucleoids across the assayed granule proteins. Most granules are distinguishable from nucleoids; the authors also discuss diffraction-limited resolution and dynamic proximity. Both observations are retained. The direct and mapped nucleoid annotations are consistently kept as non-core because they describe a secondary localization. Granule predominance does not negate nucleoid association, and the location mapping does not establish DNA binding, an exclusive nucleoid role or a nucleoid structural activity.

## InterPro mapping: GO_REF:0000002

The current IPR010622 entry maps to regulation of mitochondrial mRNA stability, GO:0044528. The actual Q9NYY8 match spans residues 456–529. This agrees with the inherited function and the target/donor RNA evidence described above, with the same unresolved distinction between a direct turnover effect and secondary RNA loss. The historic FAST kinase domain name is not evidence of kinase activity, and a RAP-domain fold is not by itself a demonstrated nuclease mechanism.

## Orthology and chemical RNA modification: GO_REF:0000107

The actual mouse Q922E6 donor carries a FlyBase IPI annotation to GO:1900864 from PMID:29617655, with PTCD1/Q8C2E4. The full original paper demonstrates mouse-heart PTCD1–Fastkd2 co-immunoprecipitation and co-fractionation with RPUSD4. The perturbation directly measuring 16S-rRNA pseudouridylation is Ptcd1 loss. Figure 6's BioID confirmation is in HeLa cells and is kept distinct from the mouse-heart assays. Human studies place FASTKD2 in an RNA-handling module with pseudouridine synthases (PMID:27667664; PMID:27974379), while also leaving aspects of complex organization and FASTKD2's molecular role unresolved.

The transferred modification row remains UNDECIDED. The available assays do not isolate whether FASTKD2 supplies a structural or regulatory contribution specifically to chemical modification. Such a contribution is possible, and absence of a catalytic domain is not disproof. Positive association evidence is retained without inferring a wrong-gene annotation or biological absence.

## Source access and product limits

Actual Methods, Results, relevant discussion and captions were read for the bounded scopes recorded in the private provenance packet. No primary-paper figure pixels or supplements were independently read in this database lane; the HPA microscopy image is the sole image inspection. PMID:25683715 was read through original author-uploaded text despite its abstract-only cache. PMID:29617655 was read from the author-deposited full PDF; its authentic normal cache remains abstract-only. The authored reference therefore does not label the full paper unavailable. Initial XML, publisher and anti-bot failures for donor recovery are retained alongside successful original recovery and genuine fetch receipts.

Both curated natural products remain unchanged. The canonical precursor has 710 residues; the alternative product has 648 residues. UniProt leaves the transit-peptide endpoint and chain start unknown. Transcript models and tagged experimental constructs are distinct from these curated products. No cleavage boundary, product-specific function or extra annotation is introduced by this database review.
