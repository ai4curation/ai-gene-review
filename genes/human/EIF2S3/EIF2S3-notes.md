# EIF2S3 evidence notes

EIF2S3 encodes the 472-residue gamma subunit of eIF2. Gamma supplies the nucleotide-binding/GTPase center and engages initiator methionyl-tRNA; alpha and beta complete the ternary-complex delivery factor. The eIF2B exchange factor recycles eIF2 and is a separate complex. The integrated core combines gamma's direct molecular work with its contribution to translation initiation.

## Human assays, model organisms and constructs

Human gamma association and patient-cell experiments support eIF2 integrity and translation (PMID:23063529; PMID:31836389). The human I259M reporter phenotype and purified yeast I318M tRNA-binding measurement are separate experimental contexts (PMID:30517694). They motivate the question about reconstituted human eIF2 without asserting that the human variant has already been measured in the same purified assay.

Human CDC123 association, the gamma C-terminal truncation comparison, and the human fragment structure support an assembly-related chaperone interaction (PMID:35031321; PMID:37507029). The ordered assembly mechanism is predominantly yeast-derived, and the reported human relative co-IP enrichment has n = 1. Experimental gamma 1–457 or 362–471 constructs are not natural isoforms. The cytosolic Reactome chain 2–472 records initiator-methionine processing.

The localization experiment with a human gamma construct in BHK cells supports its reported cytoplasmic restriction and negative nuclear result (PMID:12426392). It does not establish universal nuclear exclusion. A cytosol refinement also uses independently target-resolved localization, while preserving the original assay's broader resolution.

## Interaction evidence and unresolved observations

All 28 Y2H screen pairs from PMID:32814053 remain positive generic non-core observations. A partner's class by itself does not establish a specific functional interaction or native complex. The alpha/beta eIF2 and CDC123 refinements instead have independent complex or mechanistic support. AP-MS, co-complex recovery, Y2H and direct fragment-structure observations remain distinct.

Three assertions remain unresolved: gamma-specific regulation in PMID:18639529, cadherin binding in PMID:25468996, and exosome localization in PMID:20458337. The latter two lack recovered target-specific supplementary evidence; proximity is not silently converted to direct binding. Their positive curator assertions are retained, and the inaccessible experiments are not described as disproved.

## Reproducible provenance and access

[The source guide](EIF2S3-source-evidence.yaml) gives normal-cache hashes, public original locators and source-specific access limits. Some abstract-only normal caches have separately recovered original material; a nominal full-text flag likewise does not guarantee a complete target supplement. No publication quotations are added. Reference-only support is intentional.

[The offline database analysis](EIF2S3-bioinformatics/README.md) reconstructs the four PAINT joins, exact 472-residue MSA match, 41 source-pair joins and 15 Reactome component paths. It preserves mixed accession groups, assay metadata and forward graph directions. No original article bodies are redistributed in that analysis.

There are 81 reviewed source contexts: 31 ACCEPT, 19 MODIFY, 28 KEEP_AS_NON_CORE and 3 UNDECIDED. Original qualifiers, the negative nuclear assertion and the normal GOA multiplicities are preserved. No new annotation or lifecycle retirement is proposed. Automated research-provider attempts did not produce a usable report; these conclusions use the cited primary, curated and independently reconstructed evidence.

## Follow-up: source-specific binding and ontology scope

This entry supersedes the earlier CDC123 refinement and action-count statements. Four CDC123 observations now retain generic non-core binding: source-specific AP-MS association and the direct human gamma-domain interface remain positive. UniProt does classify CDC123 as a protein-folding chaperone. The inspected human assembly/fragment evidence, however, does not resolve the narrower GO:0051087 nascent/unfolded-client criterion; a folded domain structure alone is not a disproof of chaperoning. Intracomplex alpha/beta refinements are unchanged.

The PMID:10900014 RNA-binding review instead proposes translation initiation factor activity (GO:0003743), because the gamma perturbation tests initiation and its ribozymes cleave the target transcript. The PMID:8106381 context retains the methionyl-initiator tRNA-binding correction supported by reported crosslinking, with unresolved full preparation/species details. Both are lateral changes from GO:0008135, not descendant refinements. Current official ancestry is reproducible through https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0003743/ancestors?relations=is_a%2Cpart_of and the corresponding GO%3A1990856 endpoint; neither response contains GO:0008135.

Reference-only anchors now accompany the three formerly GO_REF-only ACCEPT reviews: the literal yeast experimental donor paper PMID:3888990 for GTPase rows and PMID:8106381 for the human nucleotide-binding architecture. Their distinct assay and access scopes are recorded in the source guide; no quotation is added.

The normal raw GOA has 82 records and the normal fetch generated 81 review contexts. Raw zero-based records46 and55 both map to review48 (GO:0005515/IPI/PMID:37507029/CDC123/enables), differing in assigned-by/date: IntAct20260725 versus UniProt20231006. Both raw records remain byte-exact in the GOA file; one normalized review context is intentional. This clarifies the earlier multiplicity wording without inventing or removing an annotation.

The proposed counts are 31 ACCEPT, 15 MODIFY, 32 KEEP_AS_NON_CORE and 3 UNDECIDED. All81 source objects, the472-residue natural product, the existing core, other reviews and zero-quotation inventory remain unchanged. The separate independent tRNA-binding core consultation is pending integration by ROOT.

The independent core synthesis is now integrated: GO:1990856 records the gamma-centered initiator-tRNA-binding surface within eIF2. The original GTPase core is preserved exactly; no biological-process or localization fields are duplicated in the added core. Human complex recovery, abstract-only crosslinking and selective yeast biochemical evidence retain their distinct assay limits. [PMID:8106381](https://pubmed.ncbi.nlm.nih.gov/8106381/), [PMID:30517694](https://pubmed.ncbi.nlm.nih.gov/30517694/), [PMID:31836389](https://pubmed.ncbi.nlm.nih.gov/31836389/).
