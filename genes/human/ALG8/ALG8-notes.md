# ALG8 review notes

## 2026-09-27 — full source-specific audit

Identity and baseline: approved human ALG8, HGNC:23161, UniProt Q9BVK2; HGNC alias MGC2840, no previous symbol. Separate canonical/alias open-PR searches were empty, and no alias directory was found. The four original files matched fresh main `21364698b8b0c1099c7f26384bfd35b13596d282`; root independently matched them to publication base `ba3ff58d7d2de76dbe3c24b16e05e12369f463fc`. The starting INITIALIZED document already contained 24 decisions, 15 references, two overlapping catalytic cores and two alternative products. Every source annotation, original reference identity, qualifier and alternative product is preserved. No provider artifacts or prior notes existed.

Applied the review, annotation-reviewer and core-function-synthesizer skills. The default Falcon launch with Perplexity-lite fallback ran concurrently with normal seeded publication caching. An initial offline dependency-resolution failure was followed by one justified online attempt using writable temporary UV tool/cache directories. That attempt and its fallback both failed DNS while resolving the pinned deep-research-client dependency; neither reached a provider or generated a report. Logs: `/tmp/ALG8-provider-attempt.log`, `/tmp/ALG8-provider-online-attempt.log`. `just fetch-gene-pmids human ALG8` succeeded with all five already-cached sources; log `/tmp/ALG8-seeded-fetch.log`. No provider report was authored or relabeled.

### Function and original experiments

ALG8 performs the second of three glucose transfers during ER lipid-linked oligosaccharide assembly. The donor is Dol-P-Glc; the acceptor is Glc1Man9GlcNAc2-PP-Dol and the product is the diglucosylated intermediate. This direct catalytic step supports both the specific precursor-synthesis process and its broader N-glycosylation context. One integrated catalytic core replaces two descriptions of the same reaction; its location specifies the lumenal membrane face. Broader seeded membrane annotations retain their source resolution.

[PMID:12480927], DOI [10.1074/jbc.M211950200](https://doi.org/10.1074/jbc.M211950200): read the cached abstract and independently checked PubMed identity. Human patient fibroblasts accumulated Man9-containing LLO, shifting toward Glc1 after castanospermine; the abstract describes low ALG8 transcript abundance, frameshifting alleles and wild-type cDNA complementation. These support the retained IMP activity/process assertions. Original JBC/ScienceDirect full-text attempts did not recover the body; no purified turnover measurement is claimed. Exact result-bearing snippets in the YAML come from the cached abstract, rather than its title or the fragment “which catalyzes this reaction.”

[PMID:15235028], DOI [10.1136/jmg.2003.016923](https://doi.org/10.1136/jmg.2003.016923), PMCID PMC1735831: the canonical cache is bibliographic-only, although it has an Abstract heading and an automated COMMENT_EDITORIAL classification. The full original research letter was recovered from the [author-uploaded article](https://www.researchgate.net/publication/8473940_Clinical_and_molecular_features_of_three_patients_with_congenital_disorders_of_glycosylation_type_Ih_CDG-Ih_ALG8_deficiency), J Med Genet 41:550–556. Read Methods, Results, Figure 4 and the topology Discussion. Patient fibroblast glycan profiling complements yeast assays of human constructs. Figure 4 compares wild-type/T47P/G275D complementation in Δalg8 and Δalg8 wbp1–1 backgrounds; Discussion calls the assays nonquantitative. Exact result excerpts and the original source URL are attached to the IGI localization and IMP activity reasons. Topology is predicted, not directly imaged. These distinctions preserve IMP/IGI and the curator's lumenal-side IC while correcting previous isolated-enzyme and abstract-only claims. Local `full_text_unavailable` remains true; external access does not modify machine cache metadata. The title-only support snippets were withdrawn; no external passage is falsely attributed to the cache.

[PMID:28375157](https://www.jci.org/articles/view/90129), DOI [10.1172/JCI90129](https://doi.org/10.1172/JCI90129): independently read original Figure 2 and surrounding Results. Human heterozygous loss-of-function genetics informs the polycystic liver disease summary. Mechanistic work used engineered mouse epithelial cells, where Alg8 loss changed PC1 glycosylation, abundance and trafficking, and re-expression rescued the phenotype. Human clinical evidence and mouse cell mechanisms are kept distinct. This does not add a ciliary-localization, protein-folding or trafficking function to ALG8. The normal request for this missing publication terminated with DNS failure (0/1, exit 1; `/tmp/ALG8-new-fetch.log`), leaving an explicit required cache gate.

### Interaction evidence

Read all three interaction caches. PMID:25910212 ([10.1016/j.cell.2015.04.013](https://doi.org/10.1016/j.cell.2015.04.013), PMC4441215) and PMID:33961781 ([10.1016/j.cell.2021.04.011](https://doi.org/10.1016/j.cell.2021.04.011), PMC8165030) contain partial full bodies, chiefly Introduction/Discussion, despite `full_text_available: true`; their reference flags remain false, with extraction limits explicitly recorded. The curated UniProt/IntAct pairs ground target attribution. PMID:32296183 ([10.1038/s41586-020-2188-x](https://doi.org/10.1038/s41586-020-2188-x), PMC7169983) includes primary HuRI Results and validation descriptions: complementary Y2H formats, repeated screening and pairwise retesting. No claim is made that every ALG8 pair received every orthogonal test.

Rows 7–9 now REMOVE GO:0005515 because it is uninformative. The prior MARK_AS_OVER_ANNOTATED reasons misdescribed repository policy. Removal does not deny CREB3, HuRI partner or ALG6 associations. In particular, ALG6 copurification is compatible with neighboring pathway enzymes but does not establish channeling, a fixed complex, or a new adaptor activity. The source's throughput is not itself grounds for rejection.

### Propagation, ontology and pathway review

IBA rows preserve their PTN sources only: PTN000275691 for membrane/process and PTN000275692 for the exact activity. Full ancestral IBD/tree reconstruction was not recovered; source status records that limit while positive human evidence supports the target assertions. Neither donor count nor human self-evidence is treated as circularity.

Mouse donor [Q6P8H8](https://www.uniprot.org/uniprotkb/Q6P8H8/entry) is independently identified as Alg8 by UniProt and [MGI](https://www.informatics.jax.org/sequence/Q6P8H8). Current [MGI annotation graph](https://www.informatics.jax.org/marker/gograph/MGI:2141959) includes an IMP glycosylation assertion linked to J:269547, the 2017 study above. The exact historical Ensembl/ISS transfer chain remains unresolved; compatible current mouse evidence is not retroactively substituted for that chain. Human chemistry and patient evidence independently support retained rows 10 and 21.

Live ontology checks: [GO:0004583](https://amigo.geneontology.org/amigo/term/GO:0004583) defines transfer from dolichyl-phosphate D-glucose to a membrane lipid-linked oligosaccharide and explicitly lists GO:0042283 as a child, with the specific official label. [GO:0006488](https://amigo.geneontology.org/amigo/term/GO:0006488) covers stepwise LLO formation and has a `part_of` relationship to protein N-linked glycosylation. [GO:0098553](https://amigo.geneontology.org/amigo/term/GO:0098553) includes proteins embedded in the lumen-facing ER leaflet, not only soluble lumenal proteins. Direct retrieval of the GO:0042283 definition through AmiGO/QuickGO/OLS failed, so no unsupported claim of having read that definition is made; its parentage/label were visible on the parent page, and its reaction is independently checked in UniProt/EC/Rhea. The specific term is already source-seeded and used in the prior core. The InterPro family mapping remains true, with target-specific refinement to the exact activity.

Read cached [R-HSA-446189](https://reactome.org/content/detail/R-HSA-446189), [R-HSA-446193](https://reactome.org/content/detail/R-HSA-446193) and [R-HSA-4724330](https://reactome.org/content/detail/R-HSA-4724330), with official-page checks. The specific normal event assigns second glucose addition to ALG8. The disease event first states this normal activity and then describes defective variants; normal gene function is distinguished from mutant capacity. The broad pathway summary's “3 terminal GlcNAcs” is a wording error; the normal precursor has three terminal glucoses. All machine records remain unchanged. Ancillary pathway bibliography was not adopted as evidence for extra gene functions.

GO-CAM `65c57c3400000687`, activity `65c57c3400001190`, already represents Q9BVK2 enabling GO:0042283, occurring on the lumenal ER membrane side, and participating in GO:0006488. It cites the same two human primary studies, so it corroborates curator role assignment without becoming an independent experiment. No NEW annotation or new core term is introduced. The core retains the most informative existing process; no ancestor/descendant coverage is manufactured.

### Decisions and source census

All 24 source rows were individually adjudicated: 18 ACCEPT, 3 MODIFY and 3 REMOVE; zero NEW. Broad source compartment/process assertions remain valid. The three MF refinements are the existing InterPro hexosyltransferase and two Reactome donor-specific parent activities. Sixteen references have source-specific assessments, preserving all 15 original identities; the only added source is the verified 2017 PCLD paper.

The finite authored citation census is six PMIDs: 12480927, 15235028, 25910212, 28375157, 32296183, 33961781; three Reactome records: R-HSA-446189, R-HSA-446193, R-HSA-4724330. The six DOI links and four PMC identifiers refer to those same papers. There are no provider files or provider raw artifacts. Unused bibliography in immutable UniProt or pathway source records is not adopted as an authored citation. Five PMID caches and all three Reactome caches are present; PMID:28375157 is the sole missing required cache. DRAFT records this source gate rather than concealing it.

### Verification and independent consultation

Full `just validate human ALG8` completed with exit 0 and one warning: the required PMID:28375157 cache could not be fetched. Render completed successfully. All 42 ordinary supporting snippets pass case-sensitive substring checks after whitespace normalization; none requires case folding. Parsed checks preserve all 24 source objects, 15 original reference identities and both alternative products. There are no YAML anchors/aliases or trailing spaces. Aars1 independently read the full original PMID:15235028 Results/Figure 4 and topology Discussion and confirmed the human-construct/yeast-host and nonquantitative-assay bounds. Root received the stable full draft for independent review; final coordinator signoff is tracked separately.

Root independently read all 24 decisions, all reference assessments, the integrated core and notes and found no biological blocker. At its request, the IGI ER and IMP activity reasons now contain short exact original Results excerpts plus the full primary route. These excerpts are explicitly external; the canonical cache remains bibliographic-only. The specialized `supporting_text_fulltext` field was not used because inability to share the full paper publicly has not been established. The only YAML delta after the full validation was these two reason attachments; source fields, actions and cores are unchanged.


## 2026-09-27 source recovery and evidence-attachment follow-up

The normal PMID:28375157 record is now present unchanged from recovery run `36313594604`,
source commit `408e7c41d93c2fd63f54ac1da5d7201edbc901bb`. Actual contents are an abstract,
not the full article; the PMC identifier does not alter this distinction. This closes that
specific cache gate and supersedes the earlier absence statement without rewriting its history.
The abstract establishes human PCLD gene discovery and cell-model perturbations but does not
identify every construct or host species. The official [JCI Results and Figure 2](https://www.jci.org/articles/view/90129)
were reread: CRISPR-inactivated Alg8 in mouse kidney epithelial cells expressing tagged Pkd1,
re-expression rescue, glycosidase-dependent PC1 migration and ciliary PC1 staining are separate
from human family genetics. ALG8 supplies glycan-precursor chemistry; those experiments do not
turn it into a PC1 protease, chaperone or trafficking motor. No new process is proposed.

The imported original record explicitly links a corrigendum, [PMID:28862642], DOI
[10.1172/JCI96729](https://doi.org/10.1172/JCI96729). The [official notice](https://www.jci.org/articles/view/96729)
was independently read: the listed RT-PCR primers had been mislabeled as Pkd1, and the notice
provides the correct Pkd1 quantitative-PCR sequences and points to the separate published Xbp1
RT-PCR primers. It does not retract the paper, replace an ALG8 activity result or supply a new
mechanism. The already-completed normal fetch failed DNS (0/1, exit 1; receipt
`tmp/ALG8-correction-fetch-receipt.json`), and recovery is assigned to fixed source18. There is
no retry or fabricated cache here. The review and PR remain DRAFT until this required correction
record is normally recovered.

### Public primary excerpt receipt: PMID:15235028

Canonical identity: Schollen et al., *Clinical and molecular features of three patients with
congenital disorders of glycosylation type Ih (CDG-Ih) (ALG8 deficiency)*, J Med Genet 41:550–556,
DOI [10.1136/jmg.2003.016923](https://doi.org/10.1136/jmg.2003.016923),
[PMC1735831](https://pmc.ncbi.nlm.nih.gov/articles/PMC1735831/).
The actual successful full-article retrieval was the author-uploaded original linked earlier;
the canonical links identify the paper without falsely changing which route supplied the body.
The original Results, p. 553, Figure 4B, include this short excerpt:

> human ALG8 cDNA conferred a marked restoration of the glycosylation

The assay is human ALG8 construct complementation of yeast CPY glycosylation, including
wild-type versus T47P/G275D comparisons in the stated mutant backgrounds. It supports genetic
function and compartment context; it is not direct human localization or purified-enzyme
turnover. This receipt preserves the previously independently read primary excerpt, with
page and route provenance. It is the same study, not independent evidence. The canonical normal
PMID cache remains bibliographic-only.

The two annotation reasons point to this source-access receipt. The public excerpt stays in
these notes with its original primary attribution; it is not attached as a separate notes-file
evidence reference or validated as an independent primary source.
The specialized `supporting_text_fulltext` field is deliberately not used: its schema specifies
full text that cannot be committed/shared publicly, not every publicly accessible passage that
is absent from a local extraction. No source cache was hand-edited or refetched to satisfy a
quotation. Access-only primary reference entries remain honest availability records rather
than being filled with irrelevant or invented excerpts.

The specific UniProt variant-activity, N-linked precursor, ALG6/ALG8-family and multipass
snippets requested by the reviewer were restored as exact cached quotes. The variant note is
curated corroboration linked to the same patient study, not a second kinetic experiment. Human
T47P/G275D identities and the eight HuRI partners are visible in the relevant summaries; no
interaction is denied by removing an uninformative generic binding label. All 24 original
source objects and actions, both alternative products, the description and integrated
core are unchanged. All 16 prior reference identities remain. One reference was
added for the explicitly uncached correction.

The recursive authored/provider census now requires seven PMIDs (six cached, correction
28862642 missing) and three cached Reactome entries. There are no provider artifacts. DOI,
PubMed, PMC and actual author-upload links were reconciled to those same studies; the
ResearchGate numeric article identifier is not a PMID. An incidental commentary bibliography
inside the original normal PubMed record is not adopted as evidence for an authored claim.
Earlier statements identifying PMID:28375157 as the sole missing record are superseded here.
