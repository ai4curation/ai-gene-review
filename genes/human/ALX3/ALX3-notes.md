# ALX3 manual review notes

## 2026-09-27 — initial evidence review

Human ALX3 is HGNC:449 / UniProt O95076. The normal seed contains 13 assertions. All original terms, evidence codes, source references, qualifiers and supporting entities are preserved. The immutable UniProt record identifies a paired-class homeodomain at residues 153–212 of the 343-residue protein. No alternative product was seeded.

The normal Falcon attempt with the configured perplexity-lite fallback failed at DNS resolution and produced no report. Ordinary seed-publication caching preserved the existing publication record. One grouped normal fetch of five additional PMIDs also failed at DNS resolution, with zero records recovered. A normal PANTHER/PAINT fetch failed too. These failures concern the local tools; primary article text was accessible separately through web results. No provider report or source-cache text has been authored as a substitute.

## DNA binding and transcription

[PMID:28473536], DOI 10.1126/science.aaj2239, is the source of the existing experimental sequence-specific DNA-binding assertion. The local record is marked full text, but its HTML extraction contains the abstract and concluding discussion rather than the complete Results and target-specific supplement. Its broad human transcription-factor SELEX design is clear. The ALX3 supplemental record and any ALX3-specific methylation preference were not independently verified. This is no basis to accuse the GO curator of attributing a different protein's experiment to ALX3. The measured function is independently corroborated below; no methyl-CpG-specific activity is added.

[PMID:38600112], DOI [10.1038/s41467-024-47396-0](https://doi.org/10.1038/s41467-024-47396-0), examines human homeodomain variants by protein-binding microarrays. Primary Results and Table 1 identify ALX3 L168V and N203S among variants with changed affinity; reduced binding is explicitly reported for L168V. This directly supports ALX3 DNA recognition. The experimental protein is a homeodomain construct, which is distinct from measuring full-length protein occupancy in a native human developmental tissue. Construct-host details and the full Methods were not yet independently inspected.

[PMID:16825292] provides the mechanistic ortholog context. Its primary abstract describes mouse MIN6 cells and pancreatic islets, Alx3 occupancy of insulin promoters, binding to the A3/4 element and transcriptional activation with E47 and NeuroD. Physical interaction is reported with E47, not NeuroD. Reporter experiments in HeLa cells do not make the Alx3 construct a human protein. These data support a conserved nuclear transcription-factor mechanism; they are not used to invent a human insulin-production annotation. The DOI 10.1210/me.2005-0472 was corroborated in a bibliographic index and remains subject to the normal primary-cache metadata check.

## Developmental scope

[PMID:19409524], DOI 10.1016/j.ajhg.2009.04.009, establishes recessive ALX3-related frontorhiny in seven families with homozygous variants. Primary indexed Results were inspected. The paper predicts impaired mutant DNA binding using structural and comparative arguments; it does not directly measure every ALX3 mutant's binding. Human embryonic ALX3 in-situ hybridization did not give signal above background. The ALX4 expression image must not be relabeled as an ALX3 experiment.

[PMID:20534379], DOI 10.1016/j.ydbio.2010.06.002, was accessible as a primary abstract. Mouse Alx3 deficiency affects head mesenchyme, craniofacial midline and neural-tube closure, with apoptosis and folate responsiveness investigated. These observations do not by themselves identify a neuron-maturation step or an ALX3 folate-binding activity.

[PMID:39129011], DOI 10.1007/s00018-024-05384-z, was accessible as a primary abstract. It places mouse Alx3 in hypothalamic arcuate neurons and links deficiency to food-intake and energy-homeostasis phenotypes. Adult neuronal physiology and expression do not directly settle the neuron-development assertion.

The current official [GO:0048666 definition](https://amigo.geneontology.org/amigo/term/GO:0048666) concerns progression from initial neuronal commitment to the mature state. Its PAINT node PTN001216073 is preserved, but the actual ancestral IBD/tree and clade experiments were not recovered. The row is UNDECIDED, without asserting an incorrect node placement, missing donors or loss of function. The other PAINT rows at PTN004692309 agree with the experimentally grounded transcription-factor mechanism. The PTHR24329 family table includes O95076; its unreviewed generated description is not treated as scientific evidence. No ALX3 entry was found in the local GO-CAM index.

## Draft decisions and remaining verification

All 13 seeded assertions have manual judgments: 12 ACCEPT and one UNDECIDED; zero NEW. One core records nuclear DNA-binding transcription-factor activity and regulation of RNA polymerase II transcription. Craniofacial disease effects and mouse endocrine or neuronal phenotypes do not become extra molecular activities. The existing broad DNA-binding and transcription rows are retained alongside their more specific source assertions.

Five required publication caches remain absent at this draft stage: 16825292, 19409524, 20534379, 38600112 and 39129011. They are included in the fixed source25 recovery request; dispatch, artifact retrieval, source assessment and canonical import will be recorded separately. The existing 28473536 cache is preserved, including its extraction limitation. Reference pointers to externally read papers do not pretend to be locally validated quotations. Independent annotation consultation, recovered-source assessment, full validation and rendering remain pending.

## Independent consultation and draft checks

An independent annotation-reviewer consultation covered all 13 decisions, all 11 references, the single core and the complete notes. It found no scientific blocker and confirmed the conserved transcription-factor interpretation and the unresolved neuron-development boundary. It independently inspected the indexed original Methods for [PMID:38600112]: the assays use N-terminal GST-fusion DNA-binding domains expressed by PURExpress in vitro transcription/translation, with matched reference/mutant series at 200 nM in protein-binding microarrays. This updates the earlier Methods-access limitation without turning a domain assay into native full-length chromatin evidence. The official PubMed record also directly confirms DOI 10.1210/me.2005-0472 for [PMID:16825292], closing the earlier DOI-verification caveat.

The two supporting pointers to the existing 28473536 record now agree with its machine access flag; the partial extraction and missing target-supplement limitation remain explicit. Initial full validation passed with only the five missing-publication warning; history validation and rendering passed. The access metadata corrections preserve every action, source assertion and core term. Source25 recovery and final source/quotation verification remain pending.

## Recovery of the five required sources

All five requested records are now cached from the normal fetch output, after archive checksum, source identity and no-overwrite checks. Three remain abstract-only: [PMID:16825292], [PMID:19409524] and [PMID:20534379]. Their complete cached abstracts were read. XML body extractions are available for [PMID:38600112] and [PMID:39129011]; the relevant Results, Methods and interpretive limits were inspected, without claiming every section or supplementary dataset was reviewed.

The recovered human homeodomain study confirms the ALX3 Table 1/Figure 4 result and the GST-fusion/PURExpress/PBM protocol already identified during independent consultation. The metabolic study used male mice aged 16–20 weeks with constitutive Alx3 deficiency; its discussion explicitly calls for neuron-specific inactivation to establish the proposed arcuate-neuron mechanism. It also leaves developmental contributions to peripheral phenotypes open. These limits preserve the existing UNDECIDED neuron-development judgment.

The review now includes source-matched quotations and five reference findings. Access flags reflect the actual caches, and the earlier missing-cache statements describe the historical draft only. The 13 original assertion objects, all 13 actions, all original reference identities and the single core are preserved. No new GO assertion was added. Full validation passes without the earlier missing-reference warnings.
