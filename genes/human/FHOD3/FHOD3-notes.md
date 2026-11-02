# FHOD3 research and annotation review

FHOD3 (HGNC:26178; UniProtKB:Q2V2M9; historical FHOS2/KIAA1695) is an actin-organizing formin with a cardiac myofibril role. The ten incoming GO annotation contexts were reviewed individually. Five are accepted; supported generic protein binding, contextual stress-fiber assembly and broad cytoplasmic localization are retained as non-core; the cytoskeleton IEA is modified to the observed sarcomere location; and Z-disc localization remains undecided. No NEW annotation is proposed.

## Actin organization, assembly and maintenance

Taniguchi and colleagues used mouse FHOD3 constructs in neonatal rat cardiomyocytes. Depletion disrupted sarcomeric actin organization; RNAi-resistant wild-type protein rescued the phenotype, whereas FH2 substitutions that also impaired cellular stress-fiber assembly did not. Construct identity matters: these were not interventions on each natural human splice product. The full-text construct Methods and depletion/rescue Results support an actin-associated mechanism of sarcomere organization rather than a conclusion based solely on disease or necessity. [PMID:19706596](https://pubmed.ncbi.nlm.nih.gov/19706596/)

The purified-protein result in the same paper is a useful boundary: truncated mouse FHOD3 inhibited spontaneous assembly and reduced seeded barbed-end elongation under the reported conditions, including with profilin. The authors infer barbed-end association and discuss missing cellular factors. This does not establish a universal nucleation activity. The selected molecular-function term is the inherited actin filament binding assertion, supported by the phylogeny and compatible mechanism. No new nucleation, elongation or capping term was manufactured from those assays. [PMID:19706596](https://pubmed.ncbi.nlm.nih.gov/19706596/)

Iskratsch and colleagues provide complementary maintenance and recovery experiments. Delayed FHOD3 depletion damages established myofibrils, while latrunculin washout tests actin/myofibril reassembly. Human splice constructs were expressed in neonatal rat cardiomyocytes; human reagent identity does not make these human-cell experiments. Maintenance is distinguished from initial embryonic sarcomerogenesis. The study could not directly compare purified splice-product nucleation because its FH2 preparations aggregated. [PMID:21149568](https://pubmed.ncbi.nlm.nih.gov/21149568/)

The early FHOS2 report describes activated constructs inducing stress fibers in HeLa cells. Its endogenous nestin observations concern rat H9c2 cardiomyoblasts and fetal rat brain. They are not evidence that every human cardiac product universally binds nestin or occupies intermediate filaments. Historical long/short constructs should not be equated automatically with all four present-day human UniProt products. [PMID:15966898](https://pubmed.ncbi.nlm.nih.gov/15966898/)

## SQSTM1 interaction and splice-product boundaries

The human heart-library two-hybrid screen, FH2-bait pull-down from transfected COS-1 lysates, and cellular co-immunoprecipitation support FHOD3 association with SQSTM1/p62. CK2 phosphorylation of the muscle-associated insertion changes binding and targeting/stability in the tested systems. The pull-down is not a purified two-component binding experiment. p62 PB1-containing constructs support association, while p62's own UBA activity cannot be assigned to FHOD3. [PMID:21149568](https://pubmed.ncbi.nlm.nih.gov/21149568/)

LC3/p62-positive aggregates support conditional association with degradation compartments. They do not show that FHOD3 executes autophagy or functions as an autophagy adaptor. The supported generic interaction is retained as non-core under the ClinGen campaign's established treatment of such interactions, without inventing a specific replacement molecular function. [PMID:21149568](https://pubmed.ncbi.nlm.nih.gov/21149568/)

The four natural UniProt products reconstruct to 1,422, 1,401, 1,439 and 1,622 amino acids. The complete seeded VSP lists are preserved. Thr1474 and Thr1476 in the muscle-associated product are coordinates of Q2V2M9-4; they cannot be assigned to the displayed 1,422-residue protein. Tagged constructs, FH2 fragments, N-terminal or DAD deletions, and phosphorylation mutants remain separate from these natural products. The [evidence guide](FHOD3-evidence.yaml) records sequence hashes and exact source provenance.

## Precise sarcomeric localization is unresolved

The broad cytoskeletal location is supported. The Z-disc claim requires more caution. PMID:21149568 reports Z-disc/intercalated-disc staining in adult heart, including human tissue, using an antibody raised against a shared N-terminal region. This is not an isoform-4-specific localization assay. [Iskratsch et al.](https://pubmed.ncbi.nlm.nih.gov/21149568/)

PMID:22509354 instead reports FHOD3 doublets within sarcomeres, away from Z-lines, including human ventricular samples. Its noncardiomyopathic specimen came from a patient with severe aortic stenosis; it is not an uncomplicated healthy-donor control. Rodent experiments used several antibodies and included preadsorption controls. The paper discusses differences in antibody recognition and fixation, while leaving the discrepancy unresolved. These results justify retaining uncertainty rather than selecting a study by date. The human observations and mouse antibody controls are not conflated. [Kan-o et al.](https://pubmed.ncbi.nlm.nih.gov/22509354/)

The same study finds the acidic insertion dispensable for localization in its tested systems. This prevents a universal claim that the insertion determines localization across species, constructs and tissue states. The review records their shared sarcomere location in its core synthesis and leaves the incoming Z-disc IEA as UNDECIDED. No assertion of definitive antibody artifact, universal relocalization, or an isoform-specific GO row is made. [PMID:22509354](https://pubmed.ncbi.nlm.nih.gov/22509354/)

## Human disease evidence

The 2018 clinical abstract reports enrichment of candidate variants and segregation in hypertrophic-cardiomyopathy families. The later family report includes a young unaffected carrier of its reported deletion. These provide human genetic context, not direct biochemical mechanisms or a universal loss-of-function claim. Variant numbering in those reports is not transferred to the displayed protein without sequence mapping. [PMID:30442288](https://pubmed.ncbi.nlm.nih.gov/30442288/), [PMID:31742804](https://pubmed.ncbi.nlm.nih.gov/31742804/)

## Phylogenetic audit

The official PANTHER tree places the exact human FHOD3 leaf PTN002509360 in PTHR45920:SF3. Its complete ungapped MSA sequence matches the displayed Q2V2M9 sequence. Each of the seven incoming IBA origin nodes lies on the actual root-to-target path and joins a positive cached PAINT IBD for the same term. Six other family assertions are off-path. They were not transferred as nuclear, ER, microtubule or actin-cable annotations.

A short donor list does not invalidate PAINT's node judgment. The stress-fiber annotation is non-core because of functional context, not because its donor list is short or because target-specific evolutionary loss was demonstrated. API release 19 and cached PAINT have separate provenance; the target-specific join does not prove whole-release identity. Expanded GO-slim strings and unchecked LLM family metadata were not used as new primary evidence. Exact node joins, source hashes and access limits are in [FHOD3-evidence.yaml](FHOD3-evidence.yaml).

## Research provenance and access limits

On 2026-10-28 the genuine Falcon request failed with HTTP 403 authentication failure; the genuine perplexity-lite fallback failed with HTTP 401 insufficient quota. Neither produced a research report. These notes are manual research, with no provider-labelled replacement.

The full cached text of PMID:21149568 was read selectively for interaction, splice regulation, localization, maintenance/recovery and Methods. PMID:19706596 was read for construct/cell and polymerization Methods, depletion/rescue, mutant comparisons and purified-protein Results. PMID:22509354 was read for localization Results and antibody, human-tissue and construct Methods, with its publisher text also consulted. The four other newly fetched publications are abstract-only. Selected line locators and immutable cache hashes are recorded in the evidence guide. Figure pixels and separate supplements were not inspected; repeated XML-derived paragraphs do not constitute independent replication.

PMID:19413330 is the Lys-N/trypsin phosphoproteomics study, not Taniguchi's functional paper. PMID:16177791 supplies chromosome-sequence provenance, not evidence of a molecular activity. Existing main publication/family files were reused unchanged, and the additional publications were fetched only after exact-path ownership qualification. No publication quotations were added to the review or these notes.

## Independent-review follow-up, 2026-10-28

The independent reviewer on PR #5661 correctly identified that the shared sarcomeric location should be explicit in the machine-readable synthesis even while its subregion remains disputed. The UniProt-sourced cytoskeleton IEA now has MODIFY with GO:0030017 sarcomere as its replacement; its original term, evidence, reference and supporting entity are preserved. The separate cytoskeleton IBA remains accepted. Cytoplasm remains supported but is non-core, without disputing its inherited PAINT placement. Both localization papers support the sarcomere location in the core synthesis. [PR review](https://github.com/ai4curation/ai-gene-review/pull/5661#issuecomment-6461203315)

Official QuickGO confirms sarcomere, myofibril, cytoskeleton and cytoplasm are current cellular-component terms. Its is_a/part_of ancestor closure places GO:0030016 myofibril and GO:0005737 cytoplasm above sarcomere, but does **not** include GO:0005856 cytoskeleton. Accordingly, this MODIFY is an empirical replacement with an observed location, not a formal ontology-child refinement. The biological rationale comes from the two primary localization studies; no missing ontology edge is invented. The exact ontology result and response hashes are recorded in the evidence guide. [Official sarcomere ancestry](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030017/ancestors?relations=is_a,part_of)

The final actions are five ACCEPT, three KEEP_AS_NON_CORE, one MODIFY and one UNDECIDED. The Z-disc uncertainty, natural-product boundaries, reference-only support, and absence of NEW assertions remain intact.

Validation passes with two advisories: the established generic-binding retention exception, and differing actions for the two cytoskeleton sources. The latter is intentional: the inherited broad-location assertion remains supported, while the electronic mapping receives an empirical replacement that records the shared sarcomere observation. This does not declare the broad location false or alter the validator policy. The computed status remains DRAFT.
