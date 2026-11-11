# EFEMP2 source guide

This guide records the evidence supporting the review and its access limits. The review YAML retains every imported assertion, including source references and partner lists. Source-row numbers below are zero-based. No excerpt is used as a substitute for the actual assay scope.

## Main mechanism

The one integrated core is enzyme-substrate adaptor activity: fibulin-4 positions pro-lysyl oxidase with tropoelastin during elastic-fiber assembly. LOX performs oxidation. PMID19570982 and PMID19855011 provide complementary binding/organization evidence with the historical construct and conditioned-medium limitations described in the notes. No second catalytic activity is assigned to EFEMP2, and no NEW row is added.

## Interaction and sequence evidence

The [binding decision index](EFEMP2-evidence/binding-decisions.tsv) links every generic-binding source to its final disposition. [Raw-derived interaction records](EFEMP2-evidence/interactions.json) preserve methods, partner accessions, ROGIDs, features and source publications. [Official partner records](EFEMP2-evidence/official-partners.json) provide class/sequence evidence, while [alternative-sequence reconstruction](EFEMP2-evidence/alternative-sequences.json) shows which product edits were verified. These are complementary sources: a full-reference checksum is not an experimental fragment boundary.

GO binding refinements concern the partner class alone. They do not require that EFEMP2 catalyze the partner reaction, activate its receptor, regulate its transcription or occupy its native compartment. Conversely, an explicit assayed fragment that excludes the relevant domain cannot inherit the intact protein's class without further evidence. The project's supported-generic-binding exception applies where no informative refinement is established.

The current [term definitions](EFEMP2-evidence/ontology.json) were checked. Keratin-associated hair-matrix proteins are not automatically assigned cytoskeletal-protein class from family-based filament localization. Human SLC16A5 drug transport supports its transporter class even though its physiological substrate is unresolved. CNNM3 regulation of TRPM7 does not resolve its independent transporter status in these data; both positive association and uncertainty are preserved.

## Primary and secondary source assessments

“Normal cache” below describes the unmodified committed or proposed normal publication cache. A separately recovered original does not change that flag. Bibliographic verification concerns the paper identity; unresolved target attribution is stated explicitly in each assessment. Original article bodies are not bundled; [source URLs and hashes](EFEMP2-evidence/original-source-locators.yaml) expose the independently recovered routes.

### [PMID:10601734](https://pubmed.ncbi.nlm.nih.gov/10601734/)

Normal cache: abstract-only flag. Reference assessment: VERIFIED; relevance: HIGH.

The bibliographic identity and complete abstract were checked. The paper introduces fibulin-3 and fibulin-4, but the target-specific full localization experiment was not recovered. Its abstract does not settle the narrower basement-membrane assignment. Historical construct lengths are not assumed to equal the current 443-residue EFEMP2 sequence.

### [PMID:16174808](https://pubmed.ncbi.nlm.nih.gov/16174808/)

Normal cache: abstract-only flag. Reference assessment: VERIFIED; relevance: MEDIUM.

The complete primary abstract reports transport of bumetanide and other drugs by human MCT6/SLC16A5 expressed in Xenopus oocytes. This supports the partner transporter class despite an unresolved physiological substrate; full Methods and the exact experimental insert were not recovered. It is not evidence that EFEMP2 transports drugs.

### [PMID:16189514](https://pubmed.ncbi.nlm.nih.gov/16189514/)

Normal cache: abstract-only flag. Reference assessment: VERIFIED; relevance: MEDIUM.

The bibliographic record and source-linked IntAct records were checked. The selected human interaction records identify their detection methods and reference sequences. Screen associations support the assayed binding context; they do not establish a native extracellular complex or transfer a partner activity to EFEMP2.

### [PMID:16478991](https://pubmed.ncbi.nlm.nih.gov/16478991/)

Normal cache: abstract-only flag. Reference assessment: VERIFIED; relevance: HIGH.

Selected original Methods, Results and captions were read. Mouse Efemp2 disruption establishes an elastic-fiber assembly defect. The human EFEMP2/elastin cell-lysate coimmunoprecipitation is distinct from the purified mouse fibulin-4/bovine elastin experiment. Neither assay makes EFEMP2 a cross-linking enzyme.

### [PMID:16713569](https://pubmed.ncbi.nlm.nih.gov/16713569/)

Normal cache: abstract-only flag. Reference assessment: VERIFIED; relevance: MEDIUM.

The bibliographic record and exact source-linked interaction records were checked. Pair identities, methods, reference-sequence checksums and recorded features are retained. An interaction in the reported assay does not establish the same association in extracellular matrix or imply EFEMP2 has a neuronal disease-protein activity.

### [PMID:17324935](https://pubmed.ncbi.nlm.nih.gov/17324935/)

Normal cache: abstract-only flag. Reference assessment: VERIFIED; relevance: MEDIUM.

The complete comparative-family abstract and the literal mouse Efemp2 donor annotation were inspected. The abstract supports microfibril-associated matrix localization, but the target-specific basement-membrane images and assay were not recovered. Bibliographic verification does not resolve that narrower location.

### [PMID:18973305](https://pubmed.ncbi.nlm.nih.gov/18973305/)

Normal cache: full-text flag true. Reference assessment: VERIFIED; relevance: HIGH.

Original Methods, Results and Discussion were read. The study tests matrix proteins in an in-vitro recombinant elastin-like-polypeptide self-assembly system. Its kinetic and morphological effects support matrix organization within that reconstituted context, not autonomous EFEMP2 catalysis or identical behavior of all native elastic tissues.

### [PMID:19199708](https://pubmed.ncbi.nlm.nih.gov/19199708/)

Normal cache: full-text flag true. Reference assessment: VERIFIED; relevance: MEDIUM.

The archived article sections and original supplementary workbook were inspected. The Paratid Exosomes sheet contains an EFEMP2 precursor record at physical row 284 with three sequences, five spectra and 0.063 sequence coverage. This is positive parotid exosome proteomic detection, not proof of an essential vesicle function. The available article cache does not expose the complete operative Methods.

### [PMID:19349279](https://pubmed.ncbi.nlm.nih.gov/19349279/)

Normal cache: abstract-only flag. Reference assessment: VERIFIED; relevance: HIGH.

Selected original Methods and Results establish binding-site specificity and competition among fibrillins, fibulins and latent TGF-beta-binding proteins. The fibulin-4/fibrillin-1 SPR evidence supports matrix-protein binding; the assay and reagent scope are retained without implying an independently demonstrated cellular signaling pathway.

### [PMID:19570982](https://pubmed.ncbi.nlm.nih.gov/19570982/)

Normal cache: full-text flag true. Reference assessment: VERIFIED; relevance: HIGH.

The operative original Methods, Results and Discussion support fibulin-4 binding to pro-lysyl oxidase and tropoelastin and concentration-dependent ternary organization. Literal human constructs are reported as residues 26–418, 26–217 and 98–303 and are not equated to the current 443-residue reference sequence. Human ARPE19 fibulin-4 knockdown modestly increased desmosine; rat RFL6 knockdown concerned fibulin-5. The evidence supports an assembly adaptor, not EFEMP2 oxidase activity.

### [PMID:19855011](https://pubmed.ncbi.nlm.nih.gov/19855011/)

Normal cache: abstract-only flag. Reference assessment: VERIFIED; relevance: HIGH.

Operative original Methods and Results support pro-lysyl oxidase recruitment, mouse elastic-fiber phenotypes and human fibroblast localization. The ternary assay combined purified tropoelastin with HEK293T-conditioned pro-lysyl oxidase; it was not a fully purified three-component system. Supplementary construct details were not recovered, so the tested preparations are not assigned to an exact current natural product.

### [PMID:20019329](https://pubmed.ncbi.nlm.nih.gov/20019329/)

Normal cache: full-text flag true. Reference assessment: VERIFIED; relevance: MEDIUM.

Selected original mouse knockout Methods and Results show disrupted elastic laminae, smooth-muscle organization and aortic pathology after germline or smooth-muscle Efemp2 loss. These support the donor developmental and morphogenetic associations while leaving extracellular matrix effects distinct from cell-intrinsic transcription or catalysis.

### [PMID:22919265](https://pubmed.ncbi.nlm.nih.gov/22919265/)

Normal cache: full-text flag true. Reference assessment: MISCITED; relevance: HIGH.

The complete operative target experiment was recovered: the EFEMP2 association in this paper is with PITX2, including a Delta-N36 EFEMP2 construct and reciprocal COS-7 coimmunoprecipitation. The imported GOA partner is LOX/P28300, which is not the partner tested in these experiments. The imported partner and citation remain unchanged, and the actual generic protein-binding result is retained. Independent LOX evidence in PMID19570982 and PMID19855011 is not contradicted.

### [PMID:23088713](https://pubmed.ncbi.nlm.nih.gov/23088713/)

Normal cache: abstract-only flag. Reference assessment: VERIFIED; relevance: MEDIUM.

The original Methods, target tables and relevant Results were read. EFEMP2 appears in both target screens; co-purification is positive and BiFC is recorded as not determined. The assay uses mouse Hoxa1 coding sequence and human ORFeome partners in tagged-cell systems. It supports the measured association, not an extracellular Hoxa1 complex or EFEMP2 transcription-factor activity.

### [PMID:23533145](https://pubmed.ncbi.nlm.nih.gov/23533145/)

Normal cache: full-text flag true. Reference assessment: VERIFIED; relevance: MEDIUM.

The original exosome preparation, proteomic Methods and Results were read, but the EFEMP2-specific supplementary target record was not recovered. The general study design cannot substitute for confirming the imported target observation; the source-specific exosome annotation remains undecided rather than being labeled contamination.

### [PMID:23636094](https://pubmed.ncbi.nlm.nih.gov/23636094/)

Normal cache: full-text flag true. Reference assessment: VERIFIED; relevance: MEDIUM.

Selected original mouse Results and Methods distinguish angiotensin-pathway-dependent hyperproliferation and aneurysm phenotypes from the elastic-fiber defect. Pathway inhibition suppresses the former without repairing the latter. This supports contextual regulation by the extracellular matrix organizer, not a direct antiproliferative enzyme activity.

### [PMID:23782690](https://pubmed.ncbi.nlm.nih.gov/23782690/)

Normal cache: full-text flag true. Reference assessment: VERIFIED; relevance: HIGH.

Operative original Methods and Results establish fibulin proteolysis susceptibility, multimerization, heparin interactions and cell-adhesion assay behavior. Effects are retained within the tested protein preparations and cell conditions. An unidentified receptor mechanism is not inferred from adhesion, and protease susceptibility is not protease activity.

### [PMID:23962539](https://pubmed.ncbi.nlm.nih.gov/23962539/)

Normal cache: abstract-only flag. Reference assessment: VERIFIED; relevance: MEDIUM.

The relevant sections of this review were read as secondary context for elastic-fiber biology. Primary fibulin-4 binding and knockout studies provide the decisive evidence; a review statement is not treated as a new EFEMP2-specific experiment or as resolution of an inaccessible target assay.

### [PMID:24769233](https://pubmed.ncbi.nlm.nih.gov/24769233/)

Normal cache: abstract-only flag. Reference assessment: VERIFIED; relevance: MEDIUM.

The bibliographic record and available study account concern cerebrospinal-fluid extracellular-vesicle proteomics. The EFEMP2-specific target table was not recovered. Its imported positive location is preserved as undecided; general secretion or extracellular-matrix residence is not a disproof of vesicle detection.

### [PMID:25416956](https://pubmed.ncbi.nlm.nih.gov/25416956/)

Normal cache: full-text flag true. Reference assessment: VERIFIED; relevance: MEDIUM.

The bibliographic identity and source-specific human interaction records were checked. Exact partner accessions, sequence references and any reported fragment features are preserved separately. These data support their experimental association scope, not a claim that each pair forms a native extracellular complex.

### [PMID:25885889](https://pubmed.ncbi.nlm.nih.gov/25885889/)

Normal cache: full-text flag true. Reference assessment: VERIFIED; relevance: MEDIUM.

The original ovarian-carcinoma immunohistochemistry Methods and Results were read. Scored cytoplasmic granular and perivascular staining does not specifically resolve the non-collagenous compartment of basement-membrane extracellular matrix. This is a limitation of the narrower location attribution, not evidence that the staining experiment was false.

### [PMID:25910212](https://pubmed.ncbi.nlm.nih.gov/25910212/)

Normal cache: full-text flag true. Reference assessment: VERIFIED; relevance: MEDIUM.

Bibliographic identity and literal source-linked interaction records were checked. The reference protein checksum and experimental feature intervals are reported separately; a full reference checksum does not prove a full-length experimental insert. Binding-class refinements describe the demonstrated partner class without transferring its catalytic or transcriptional activity.

### [PMID:26178373](https://pubmed.ncbi.nlm.nih.gov/26178373/)

Normal cache: full-text flag true. Reference assessment: VERIFIED; relevance: MEDIUM.

Selected original Methods and Results on mouse Efemp2 E57K and tissue phenotypes were read. Changes in collagen fibril organization and maturation support contextual collagen-assembly regulation. Tissue-dependent phenotypes are not converted into a universal EFEMP2 catalytic activity.

### [PMID:26220971](https://pubmed.ncbi.nlm.nih.gov/26220971/)

Normal cache: abstract-only flag. Reference assessment: VERIFIED; relevance: MEDIUM.

The separately recovered original Methods and Results show mouse aortic collagen disorganization and reduced mature cross-links. LOX processing was largely retained, and fibulin-4 did not stimulate the tested PCOLCE/BMP1 cleavage reaction. Purified-protein assays and rat smooth-muscle-cell association are kept distinct. These findings support matrix organization without assigning the other proteins' chemistry to EFEMP2.

### [PMID:26711913](https://pubmed.ncbi.nlm.nih.gov/26711913/)

Normal cache: full-text flag true. Reference assessment: VERIFIED; relevance: MEDIUM.

Selected original Methods and Results describe mouse Efemp2-dependent collagen assembly and tissue-specific fibril phenotypes. They support the literal ortholog donor process assertions, with direct versus matrix-mediated mechanisms left unresolved where the experiments do not separate them.

### [PMID:26871637](https://pubmed.ncbi.nlm.nih.gov/26871637/)

Normal cache: full-text flag true. Reference assessment: VERIFIED; relevance: MEDIUM.

The bibliographic identity and source-specific alternative-splicing interaction records were checked. Official alternative-sequence edits were independently reconstructed and matched to FASTA records. This authenticates reference sequences, not archived experimental inserts or functional equivalence of natural products.

### [PMID:27339457](https://pubmed.ncbi.nlm.nih.gov/27339457/)

Normal cache: abstract-only flag. Reference assessment: VERIFIED; relevance: HIGH.

The complete primary abstract supports biochemical effects of fibulin-4 missense variants and interactions with several extracellular partners. Full target-specific Methods and tables were not recovered. LTBP1, LTBP3, LTBP4, LOX and LOXL1 are described, whereas the imported aggregate also contains TGFB1 and LOXL2, whose exact assay support remains unresolved. The aggregate source is preserved without fabricating separate imported records or declaring those interactions false.

### [PMID:28327460](https://pubmed.ncbi.nlm.nih.gov/28327460/)

Normal cache: full-text flag true. Reference assessment: VERIFIED; relevance: HIGH.

Original preparation/proteomic Methods and the publisher workbook were read. Table I row 29 identifies EFEMP2 in five of six donor-derived matrices; donor 1 is not detected. Values summarize repeated experiments, so the fractional peptide value is not recast as an integer unique-peptide count. Table VII row 95 is expression-cluster context, not an additional protein measurement.

### [PMID:29892012](https://pubmed.ncbi.nlm.nih.gov/29892012/)

Normal cache: full-text flag true. Reference assessment: VERIFIED; relevance: MEDIUM.

The bibliographic record and selected source-linked interaction records were checked. Their assay contexts and literal partner features are retained. Variant or interaction-screen evidence does not by itself establish an extracellular physiological role for every detected pair.

### [PMID:32296183](https://pubmed.ncbi.nlm.nih.gov/32296183/)

Normal cache: full-text flag true. Reference assessment: VERIFIED; relevance: MEDIUM.

The bibliographic identity and exact HuRI/IntAct pair records were checked. Binary assay evidence is distinguished from native-cell or extracellular-complex evidence. Supported partner classes can refine generic binding, while correctly supported associations without an informative class remain non-core under the project policy.

### [PMID:32814053](https://pubmed.ncbi.nlm.nih.gov/32814053/)

Normal cache: abstract-only flag. Reference assessment: VERIFIED; relevance: MEDIUM.

The bibliographic identity and exact source-linked interaction records were checked. Recorded fragments and alternative products are assessed against official sequence features rather than assuming every screen clone is canonical and full length. No aggregation or neurological activity is transferred from the partner to EFEMP2.

### [PMID:34928937](https://pubmed.ncbi.nlm.nih.gov/34928937/)

Normal cache: full-text flag true. Reference assessment: VERIFIED; relevance: MEDIUM.

The original human CNNM3 construct and TRPM7-associated transport experiments were inspected. The study distinguishes CNNM-dependent regulation of TRPM7 from separate CNNM transport questions; independent efflux evidence principally concerns CNNM2 and CNNM4. It does not unambiguously establish CNNM3 as a standalone transporter for the EFEMP2 partner-class refinement.

### [PMID:36399478](https://pubmed.ncbi.nlm.nih.gov/36399478/)

Normal cache: full-text flag true. Reference assessment: VERIFIED; relevance: MEDIUM.

The original database pipeline and relevant Methods were read, but the target-level interstitial-matrix record underlying the imported EFEMP2 annotation was not recovered. Authentication of the paper and its workflow does not authenticate that specific target measurement; the narrow source assertion remains undecided.

### [PMID:36972446](https://pubmed.ncbi.nlm.nih.gov/36972446/)

Normal cache: full-text flag true. Reference assessment: VERIFIED; relevance: MEDIUM.

The original human CNNM construct, Results and Methods were inspected. CNNM-dependent TRPM7 regulation and the discussion of differing transport results preserve uncertainty about standalone CNNM3 transport. The partner association remains positive; transporter-class refinement is withheld without rejecting the curated phylogenetic inference as biologically false.

## Locations and unresolved source claims

The [workbook extract](EFEMP2-evidence/workbooks.json) contains the exact positive EFEMP2 matrix and parotid-exosome records. General matrix membership is not used to deny a narrower location. The following source-specific decisions preserve uncertainty or limit an over-specific attribution:

- Row 125, GO:0005604 basement membrane, GO_REF:0000120: **UNDECIDED**. The literal ortholog source is mouse Efemp2/Q9WVJ9. Its curated location and PMID:17324935 comparative-family abstract were inspected, but the target-specific basement-membrane images/assay were not recovered. The abstract establishes microfibril-associated localization and matrix interactions, which do not alone resolve this narrower compartment. Preserve the positive imported assertion pending that source rather than treating general extracellular localization as proof or disproof.
- Row 126, GO:0005604 basement membrane, GO_REF:0000024: **UNDECIDED**. The literal ortholog source is mouse Efemp2/Q9WVJ9. Its curated location and PMID:17324935 comparative-family abstract were inspected, but the target-specific basement-membrane images/assay were not recovered. The abstract establishes microfibril-associated localization and matrix interactions, which do not alone resolve this narrower compartment. Preserve the positive imported assertion pending that source rather than treating general extracellular localization as proof or disproof.
- Row 127, GO:0005604 basement membrane, PMID:10601734: **UNDECIDED**. PMID:10601734 is bibliographically authenticated but remains abstract-only in the available source set. Its fibulin-family characterization does not expose the target-specific localization experiment needed to distinguish basement membrane from other extracellular matrix. Preserve the source assertion without declaring it false.
- Row 142, GO:0070062 extracellular exosome, PMID:23533145: **UNDECIDED**. The PMID:23533145 main text describes pooled expressed-prostatic-secretion urine, differential ultracentrifugation and LC-MS/MS with FDR below 1%, but the EFEMP2-specific Supplementary Table 2 measurement was not recovered. A known secreted matrix location neither proves exosome association in this experiment nor establishes contamination. Preserve the source assertion as unresolved.
- Row 149, GO:0140144 non-collagenous component of basement membrane, PMID:25885889: **MARK_AS_OVER_ANNOTATED**. The full operative PMID:25885889 Methods define positive immunostaining as cytoplasmic granules, and Results report strong cancer-cell cytoplasmic staining plus perivascular signal in ovarian stroma. These are real EFEMP2 observations, but they do not establish the particular basement-membrane compartment named by GO:0140144. Mark the specific location over-annotated rather than deny the measured protein or infer that EFEMP2 cannot occur in basement membrane.
- Row 150, GO:0140144 non-collagenous component of basement membrane, GO_REF:0000117: **UNDECIDED**. ARBA00096893 outputs GO:0140144 from domain/taxonomic or FunFam combinations. The rule was inspected, but its target-specific location support was not recovered; broad fibulin/ECM membership and perivascular staining do not resolve the non-collagenous compartment. Preserve the inference pending a directly informative localization source.
- Row 151, GO:0140149 non-collagenous component of interstitial matrix, PMID:36399478: **UNDECIDED**. The database paper and its proteomics inclusion/search pipeline were inspected. The EFEMP2-specific record linking its measurements to the interstitial rather than another ECM compartment was not recovered. Retain the TAS assertion as unresolved without treating broad ECM detection as proof of this finer location.
- Row 152, GO:1903561 extracellular vesicle, PMID:24769233: **UNDECIDED**. PMID:24769233 is bibliographically authenticated, but the EFEMP2-specific vesicle preparation and target-table record were unavailable. The positive imported HDA assertion is preserved; general extracellular secretion cannot establish the assay’s vesicle association, and no contamination claim is made.

GO:0140144 names a non-collagenous compartment of solid-phase basement-membrane extracellular matrix. It does not require an anatomically distinct layer. The limiting issue is the source's resolution of that specific compartment, not a fabricated anatomical requirement.

## Propagation and curated assembly models

The [phylogeny extract](EFEMP2-evidence/phylogeny.json) authenticates the target sequence and both literal IBD placements in the current tree/MSA. It preserves donor paths and distinguishes curated ancestral inference from independent target assays. The normal PTHR24050 lookup is unchanged; the current target tree is PTHR24034:SF96. No family identity was guessed from a label.

The mouse Efemp2/Q9WVJ9 donor evidence supports conserved elastic-fiber and contextual vascular/collagen roles. Where the target-specific donor images or assay were inaccessible, the uncertainty remains. Self-inclusion in PAINT evidence is not circularity, and donor count is not a measure of the curator's phylogenetic judgment.

The [Reactome extract](EFEMP2-evidence/reactome.json) retains these paths: reaction 1592387 input 2395327 hasMember 2161231; reaction 2161282 input 2396077 hasComponent 2395337 hasComponent 2395327 hasMember 2161231. Entity 2161231 references human O95967, residues 24–443. Set membership is curator-model evidence, not a purified binding assay.

## Product and source preservation

The official human record contains a single 443-residue reference product. No unsupported alternative product object or isoform-specific functional equivalence is introduced. Historical construct numbering and partner alternative sequences are kept separate from the target natural product.

The original GOA, UniProt, publication caches and their flags are immutable. The complete source inventory, cache choices and raw SHA-256 hashes are recorded in [source provenance](EFEMP2-source-provenance.yaml) and the extract's [source manifest](EFEMP2-evidence/source-manifest.json). The extraction script requires exact recorded bytes and fails on mismatches. No failed HTML challenge, XML error or supplementary-download attempt is treated as usable binary evidence.

## Source and claim distinctions after review

The paired-protein annotations describe measured association and the independently supported class of the partner. They do not assign that partner's transcriptional or enzymatic activity to EFEMP2, establish a native intracellular complex, or show that every recombinant fragment autonomously performs the full protein's function. The project's [binding policy](../../../projects/CLINGEN_MENDELIAN.md) retains a supported generic association as non-core when no justified informative refinement is available, and permits an informative refinement when the evidence supports it. The annotation below is assessed at that scope rather than rejected solely because the normal secreted protein and a partner usually occupy different compartments.

The 39 challenged annotations represent 125 selected interaction records and 36 distinct partner accessions; 30 annotations cite HuRI. The 24 transcription-factor-binding, six corepressor-binding and nine other class refinements remain. Pair-record identity/method, gene-level class, and native biological context are separate questions. Reference-sequence checksums authenticate the database reference associated with each record, not the experimental insert or vial. Recorded fragment intervals and tags are retained separately in [interactions.json](EFEMP2-evidence/interactions.json); official functional/domain evidence is in [official-partners.json](EFEMP2-evidence/official-partners.json), and alternative sequences in [alternative-sequences.json](EFEMP2-evidence/alternative-sequences.json).

| Annotation index (zero-based) | Partner accession | Source | Refined term | Selected record lines (one-based) | Recorded method(s) |
|---|---|---|---|---|---|
| 5 | Q9BQY4 | PMID:16189514 | GO:0140297 | 6, 26 | psi-mi:"MI:0096"(pull down); psi-mi:"MI:0398"(two hybrid pooling approach) |
| 8 | P54253 | PMID:16713569 | GO:0001222 | 28, 34 | psi-mi:"MI:0018"(two hybrid); psi-mi:"MI:0397"(two hybrid array) |
| 9 | P54259 | PMID:16713569 | GO:0001222 | 31, 32, 33 | psi-mi:"MI:0018"(two hybrid) |
| 18 | P09022 | PMID:23088713 | GO:0140297 | 39, 40, 41 | psi-mi:"MI:0018"(two hybrid); psi-mi:"MI:0096"(pull down) |
| 20 | O75716 | PMID:25416956 | GO:0019901 | 304, 332, 346 | psi-mi:"MI:0397"(two hybrid array); psi-mi:"MI:1112"(two hybrid prey pooling approach); psi-mi:"MI:1356"(validated two hybrid) |
| 22 | P50222 | PMID:25416956 | GO:0140297 | 305, 334, 344 | psi-mi:"MI:0397"(two hybrid array); psi-mi:"MI:1112"(two hybrid prey pooling approach); psi-mi:"MI:1356"(validated two hybrid) |
| 23 | P56524 | PMID:25416956 | GO:0042826 | 309, 316, 347 | psi-mi:"MI:0397"(two hybrid array); psi-mi:"MI:1112"(two hybrid prey pooling approach); psi-mi:"MI:1356"(validated two hybrid) |
| 24 | Q02930-3 | PMID:25416956 | GO:0140297 | 307, 328, 336, 340, 348 | psi-mi:"MI:0397"(two hybrid array); psi-mi:"MI:1112"(two hybrid prey pooling approach); psi-mi:"MI:1356"(validated two hybrid) |
| 39 | O43711 | PMID:32296183 | GO:0140297 | 206, 272, 368 | psi-mi:"MI:0397"(two hybrid array); psi-mi:"MI:1112"(two hybrid prey pooling approach); psi-mi:"MI:1356"(validated two hybrid) |
| 41 | O75360 | PMID:32296183 | GO:0140297 | 188, 279, 367 | psi-mi:"MI:0397"(two hybrid array); psi-mi:"MI:1112"(two hybrid prey pooling approach); psi-mi:"MI:1356"(validated two hybrid) |
| 42 | O75716 | PMID:32296183 | GO:0019901 | 50, 159, 249 | psi-mi:"MI:0397"(two hybrid array); psi-mi:"MI:1112"(two hybrid prey pooling approach); psi-mi:"MI:1356"(validated two hybrid) |
| 47 | P32242 | PMID:32296183 | GO:0140297 | 63, 242, 376 | psi-mi:"MI:0397"(two hybrid array); psi-mi:"MI:1112"(two hybrid prey pooling approach); psi-mi:"MI:1356"(validated two hybrid) |
| 51 | P50539-3 | PMID:32296183 | GO:0140297 | 55, 203, 261 | psi-mi:"MI:0397"(two hybrid array); psi-mi:"MI:1112"(two hybrid prey pooling approach); psi-mi:"MI:1356"(validated two hybrid) |
| 53 | P52954 | PMID:32296183 | GO:0140297 | 162, 247, 382 | psi-mi:"MI:0397"(two hybrid array); psi-mi:"MI:1112"(two hybrid prey pooling approach); psi-mi:"MI:1356"(validated two hybrid) |
| 56 | P78337 | PMID:32296183 | GO:0140297 | 196, 267, 364 | psi-mi:"MI:0397"(two hybrid array); psi-mi:"MI:1112"(two hybrid prey pooling approach); psi-mi:"MI:1356"(validated two hybrid) |
| 57 | Q02930-3 | PMID:32296183 | GO:0140297 | 167, 179, 298 | psi-mi:"MI:0397"(two hybrid array); psi-mi:"MI:1112"(two hybrid prey pooling approach); psi-mi:"MI:1356"(validated two hybrid) |
| 58 | Q08117-2 | PMID:32296183 | GO:0001222 | 99, 135, 146, 166, 178, 297 | psi-mi:"MI:0397"(two hybrid array); psi-mi:"MI:1112"(two hybrid prey pooling approach); psi-mi:"MI:1356"(validated two hybrid) |
| 60 | Q12829 | PMID:32296183 | GO:0031267 | 97, 138, 281 | psi-mi:"MI:0397"(two hybrid array); psi-mi:"MI:1112"(two hybrid prey pooling approach); psi-mi:"MI:1356"(validated two hybrid) |
| 61 | Q13351 | PMID:32296183 | GO:0140297 | 52, 199, 280 | psi-mi:"MI:0397"(two hybrid array); psi-mi:"MI:1112"(two hybrid prey pooling approach); psi-mi:"MI:1356"(validated two hybrid) |
| 63 | Q14585 | PMID:32296183 | GO:0140297 | 71, 74, 144 | psi-mi:"MI:0397"(two hybrid array); psi-mi:"MI:1112"(two hybrid prey pooling approach); psi-mi:"MI:1356"(validated two hybrid) |
| 66 | Q32M78 | PMID:32296183 | GO:0140297 | 165, 253, 374 | psi-mi:"MI:0397"(two hybrid array); psi-mi:"MI:1112"(two hybrid prey pooling approach); psi-mi:"MI:1356"(validated two hybrid) |
| 75 | Q68EA5 | PMID:32296183 | GO:0140297 | 85, 213, 290 | psi-mi:"MI:0397"(two hybrid array); psi-mi:"MI:1112"(two hybrid prey pooling approach); psi-mi:"MI:1356"(validated two hybrid) |
| 76 | Q6NSM0 | PMID:32296183 | GO:0140297 | 104, 221, 234 | psi-mi:"MI:0397"(two hybrid array); psi-mi:"MI:1112"(two hybrid prey pooling approach); psi-mi:"MI:1356"(validated two hybrid) |
| 78 | Q6NX45 | PMID:32296183 | GO:0140297 | 93, 133, 152 | psi-mi:"MI:0397"(two hybrid array); psi-mi:"MI:1112"(two hybrid prey pooling approach); psi-mi:"MI:1356"(validated two hybrid) |
| 87 | Q8IWZ5 | PMID:32296183 | GO:0031625 | 69, 72, 87, 224, 235 | psi-mi:"MI:0397"(two hybrid array); psi-mi:"MI:1112"(two hybrid prey pooling approach); psi-mi:"MI:1356"(validated two hybrid) |
| 89 | Q8TBB1 | PMID:32296183 | GO:0031625 | 174, 207, 275 | psi-mi:"MI:0397"(two hybrid array); psi-mi:"MI:1112"(two hybrid prey pooling approach); psi-mi:"MI:1356"(validated two hybrid) |
| 90 | Q8WVD3 | PMID:32296183 | GO:0031625 | 177, 212, 301 | psi-mi:"MI:0397"(two hybrid array); psi-mi:"MI:1112"(two hybrid prey pooling approach); psi-mi:"MI:1356"(validated two hybrid) |
| 94 | Q96E40 | PMID:32296183 | GO:0008092 | 57, 195, 271 | psi-mi:"MI:0397"(two hybrid array); psi-mi:"MI:1112"(two hybrid prey pooling approach); psi-mi:"MI:1356"(validated two hybrid) |
| 95 | Q96EG3 | PMID:32296183 | GO:0140297 | 205, 266, 366 | psi-mi:"MI:0397"(two hybrid array); psi-mi:"MI:1112"(two hybrid prey pooling approach); psi-mi:"MI:1356"(validated two hybrid) |
| 99 | Q96NG5 | PMID:32296183 | GO:0140297 | 101, 215, 292 | psi-mi:"MI:0397"(two hybrid array); psi-mi:"MI:1112"(two hybrid prey pooling approach); psi-mi:"MI:1356"(validated two hybrid) |
| 100 | Q96RU7 | PMID:32296183 | GO:0001222 | 95, 139, 283 | psi-mi:"MI:0397"(two hybrid array); psi-mi:"MI:1112"(two hybrid prey pooling approach); psi-mi:"MI:1356"(validated two hybrid) |
| 101 | Q96SQ5 | PMID:32296183 | GO:0140297 | 58, 157, 300 | psi-mi:"MI:0397"(two hybrid array); psi-mi:"MI:1112"(two hybrid prey pooling approach); psi-mi:"MI:1356"(validated two hybrid) |
| 105 | Q9BS34 | PMID:32296183 | GO:0140297 | 98, 134, 145 | psi-mi:"MI:0397"(two hybrid array); psi-mi:"MI:1112"(two hybrid prey pooling approach); psi-mi:"MI:1356"(validated two hybrid) |
| 106 | Q9BT49 | PMID:32296183 | GO:0001222 | 192, 269, 370 | psi-mi:"MI:0397"(two hybrid array); psi-mi:"MI:1112"(two hybrid prey pooling approach); psi-mi:"MI:1356"(validated two hybrid) |
| 113 | Q9H5H4 | PMID:32296183 | GO:0140297 | 187, 218, 230 | psi-mi:"MI:0397"(two hybrid array); psi-mi:"MI:1112"(two hybrid prey pooling approach); psi-mi:"MI:1356"(validated two hybrid) |
| 115 | Q9NYW8 | PMID:32296183 | GO:0140297 | 170, 181, 273 | psi-mi:"MI:0397"(two hybrid array); psi-mi:"MI:1112"(two hybrid prey pooling approach); psi-mi:"MI:1356"(validated two hybrid) |
| 116 | Q9P0T4 | PMID:32296183 | GO:0140297 | 86, 214, 291 | psi-mi:"MI:0397"(two hybrid array); psi-mi:"MI:1112"(two hybrid prey pooling approach); psi-mi:"MI:1356"(validated two hybrid) |
| 119 | Q9UK80 | PMID:32296183 | GO:1990381 | 64, 243, 378 | psi-mi:"MI:0397"(two hybrid array); psi-mi:"MI:1112"(two hybrid prey pooling approach); psi-mi:"MI:1356"(validated two hybrid) |
| 122 | P54253 | PMID:32814053 | GO:0001222 | 384, 385, 386, 387, 388, 389 | psi-mi:"MI:0397"(two hybrid array); psi-mi:"MI:0398"(two hybrid pooling approach); psi-mi:"MI:1356"(validated two hybrid) |

The mouse Hoxa1–human EFEMP2 record is explicitly cross-species: the original study's Tables 1 and 2 report two EFEMP2 hits and copurification confirmation, with bimolecular fluorescence complementation not determined. This does not establish a native human HOXA1 complex. For C2H2 partners whose class is phylogenetically inferred, the inference and intact domain architecture are disclosed rather than presented as an independently repeated transcription assay. ZNF558 additionally has a specific transcriptional-repressor functional account; ZNF837's class remains inferred. A partner's IBA annotation is a phylogenetic judgment and is not invalid merely because a second experiment measures association with that partner.

The alternative reference sequences CREB5 Q02930-3, MXI1 P50539-3 and TLE5 Q08117-2 were checked separately from their recorded interaction fragments. The LNX1 record maps to the canonical reference, not automatically to its noncatalytic isoform 2. TRIB3 is an inactive kinase with a corepressor role and was not assigned kinase binding. SPACA9's cytoskeletal classification has direct structural support; it is not inferred merely from an ability to bind microtubules. These distinctions are preserved in the existing official-partner and interaction extracts. None supplies evidence that the reported EFEMP2 association takes place in the native human compartment.

PMID:27339457 supports extracellular matrix binding through its reported LTBP1/3/4 interactions. The imported seven-partner aggregate is unchanged; not every member is asserted to share the same class. The paper's full target-specific Methods and tables remain unavailable. UniProt's curated SUBUNIT account also attributes TGFB1 and LOXL2 comparisons to the paper, but their exact construct/comparison scope is not independently reconstructed. No additional TGF-beta-binding refinement or invented split record is proposed.

The gene-level exosome association is retained as non-core on the positive parotid-fraction measurement in PMID:19199708. This does not authenticate the separately unrecovered urinary EFEMP2 row from PMID:23533145. The original parotid worksheet is spelled `Paratid Exosomes` [sic]; its spelling is preserved in the extract and replay. Physical workbook row 284 reports IPI00296058.1/EFEMP2 with 3 sequences, 5 spectra and 6.3% coverage. The table's location descriptions are annotations, not additional localization measurements.

For GO:0140144, the original ovarian-tissue staining and the inspected ARBA rule do not establish the gene-specific non-collagenous basement-membrane compartment. Both annotations therefore remain unresolved at the gene-claim level. Cytoplasmic granular/perivascular signal is retained as positive evidence at its actual resolution. A difference between current rule conditions and a current target-feature snapshot is not treated as proof of biological absence or as a reconstructed historical rule application.

### Exact publication-cache and original-access locators

These checksums identify the publication bytes used for this review. An abstract-only cache is not a complete article; separately read originals and access limits remain identified in the source-specific sections above and [original-source-locators.yaml](EFEMP2-evidence/original-source-locators.yaml). The header line is a navigation point, not a claim that the full file or all figures establish every assertion. Reference-only support is retained without reproducing further paper quotations.

| Reference | Published cache | SHA-256 | Cache access | Header line(s), one-based | Original identifier |
|---|---|---|---|---|---|
| PMID:10601734 | [PMID_10601734.md](../../../publications/PMID_10601734.md) | `6216d14b0e29554ae09eff810012fe37b6cb87bf2127e5b38d974bcfceb4d96a` | Abstract only | 25 | [DOI](https://doi.org/10.1016/s0945-053x(99)00038-4) |
| PMID:16478991 | [PMID_16478991.md](../../../publications/PMID_16478991.md) | `28d92b612c63473bda1c39e890477670e8206ea41ce98d5eb74dd18eb26539ab` | Abstract only | 35 | [DOI](https://doi.org/10.1128/MCB.26.5.1700-1709.2006) |
| PMID:17324935 | [PMID_17324935.md](../../../publications/PMID_17324935.md) | `d936165fc89887e96950ebf85906f1df3306561275f8d6da7affd386bb9b5091` | Abstract only | 34 | [DOI](https://doi.org/10.1074/jbc.M611029200) |
| PMID:18973305 | [PMID_18973305.md](../../../publications/PMID_18973305.md) | `31d3441cd4ee56f35dfe1480b46a010d3b6f256a1140fbcdc3ee1559aeebfca1` | Full-text cache; section limits still apply | 32, 69 | [DOI](https://doi.org/10.1021/bi8005384) |
| PMID:19570982 | [PMID_19570982.md](../../../publications/PMID_19570982.md) | `c9e9b1dff9639cc3350a81e9e8fabe8f5b6589f1ef4180bec52c4e5670723d46` | Full-text cache; section limits still apply | 36, 69 | [DOI](https://doi.org/10.1074/jbc.M109.019364) |
| PMID:19855011 | [PMID_19855011.md](../../../publications/PMID_19855011.md) | `b4fd2d178af7e321c726c212950c61f565e4eb6ea1dc00352d2af11962fcdbd8` | Abstract only | 35 | [DOI](https://doi.org/10.1073/pnas.0908268106) |
| PMID:23962539 | [PMID_23962539.md](../../../publications/PMID_23962539.md) | `036018c43c2a01870325ec24993b644e27a0ece99a67ff83f42d274f81ebdbdf` | Abstract only | 26 | [DOI](https://doi.org/10.1017/erm.2013.9) |
| PMID:25885889 | [PMID_25885889.md](../../../publications/PMID_25885889.md) | `2b15d9f267380d515999cf2896b4697e586c4795afb9a0029388b7cb7de379d7` | Full-text cache; section limits still apply | 33, 92 | [DOI](https://doi.org/10.1186/s12885-015-1100-9) |
| PMID:27339457 | [PMID_27339457.md](../../../publications/PMID_27339457.md) | `da8c5f41db74c69cbc7618888b58904ecd32c5632f5a8531628882432ec44395` | Abstract only | 31 | [DOI](https://doi.org/10.1016/j.matbio.2016.06.003) |
| PMID:28327460 | [PMID_28327460.md](../../../publications/PMID_28327460.md) | `a021b53941828f6e09153db1bf711ce0ddd15601b10db91603cbfba0206d5d89` | Full-text cache; section limits still apply | 30, 98 | [DOI](https://doi.org/10.1016/j.biomaterials.2017.03.008) |

## Second-review evidence clarification

The records below separate measured association, partner identity and native-context uncertainty. Annotation indices are zero-based in the review YAML. The original source fields, actions, replacement terms, core and product are unchanged.

| Issue | Evidence and boundary | Disposition |
|---|---|---|
| Hoxa1, row 18 | [PMID:23088713 original](https://pmc.ncbi.nlm.nih.gov/articles/PMC3514159/), Tables 1/2 EFEMP2/O95967 rows and Methods for mouse Hoxa1 cloning, GST human-ORF expression and pull-downs. Both screen configurations list EFEMP2; co-purification is positive and BiFC is not determined. Tagged proteins were coexpressed in COS-7 or HEK293T cells and recovered from lysates. | Human EFEMP2 is measured directly with a mouse transcription-factor partner. Retain the binding-class refinement while making explicit that an endogenous human HOXA1 complex, physiological co-localization and purified binary affinity are not established. |
| PITX2/LOX, row 17 | [PMID:22919265](https://pubmed.ncbi.nlm.nih.gov/22919265/) concerns the PITX2 association, including the EFEMP2 ΔN36 construct and COS-7 co-IP. Its imported partner is P28300/LOX. | This partner mismatch is different from a documented cross-species experiment. The generic non-core result and original partner provenance remain; independent LOX evidence is not refuted. |
| SGTA and SGTB | [SGTA O43765](https://www.uniprot.org/uniprotkb/O43765/entry) FUNCTION specifies client binding and targeting; [SGTB Q96EQ0](https://www.uniprot.org/uniprotkb/Q96EQ0/entry) FUNCTION specifies HSC70/HSP70 association and regulation, with additional IBA adaptor/TRC/ER-targeting context. [GO:0051087](https://www.ebi.ac.uk/QuickGO/term/GO:0051087) includes nascent or unfolded polypeptide binding for folding or transport. | Retain SGTA class refinements and SGTB non-core associations. The missing resolution is SGTB's narrower partner-class property, not the validity of phylogenetic inference or a requirement that EFEMP2 be a chaperone client. |
| Basement membrane, rows 149/150 | [PMID:25885889 original](https://doi.org/10.1186/s12885-015-1100-9), immunohistochemistry Methods and expression Results/Figure 1; separate ARBA rule and target-feature audit described above. | Retain both UNDECIDED. The positive staining is not compartment-resolved support for GO:0140144 and does not establish exclusion from that compartment. |

### HuRI denominator and ascertainment

The 86 published GOA-linked PMID:32296183 assertions contain the following dispositions. This is an annotation subset, not all screened ORFs or a nuclear-localization census.

| Subset | Rows |
|---|---:|
| DNA-binding transcription-factor binding refinement | 20 |
| Corepressor-binding refinement | 3 |
| Other partner-class refinements | 16 |
| Generic binding retained non-core | 47 |
| Total | 86 |

The 23 TF/corepressor refinements are 26.7% of this defined subset. Selecting rows by a transcription-factor or corepressor class cannot independently test nuclear enrichment. No matched assay-background comparison is available here, so neither enrichment nor its absence, and no false-positive rate, is estimated. The source snapshot contains 276 PMID:32296183 records: 93 array, 93 prey-pooling and 90 validated-two-hybrid records. These are records across assay configurations, not independent biological replications. They span 89 primary partner identifiers; 265 records join the 86 imported partners, while 11 records carry three additional IntAct identifiers (EBI-14123856, EBI-16439879 and EBI-22367043). These additional identifiers are retained without forcing a gene assignment. A partner's class is grounded separately from its pair detection; neither establishes the endogenous compartment in which the interaction occurs.

### Exact locators without additional quotations

The committed cache remains distinct from a separately recovered original. The source hashes below identify unchanged bytes; a hash authenticates the file, while the locator identifies the evidence to inspect.

| Claim | Exact source and locator |
|---|---|
| Parotid target measurement | PMID:19199708 supplementary Table 2 workbook `pr800658c_si_002.xls`, SHA-256 `400bc2387e70720f3b2ee7c17830f98cf1fa5ad0329bc1c3fee97887ee8ea6b3`; sheet `Paratid Exosomes` [sic], physical row 284, columns A:J. C:E hold sequence count, spectrum count and coverage; the coverage cell is 0.063. The existing [workbook projection](EFEMP2-evidence/workbooks.json) and [replay instructions](EFEMP2-evidence/README.md) reproduce the values. |
| Historical fibulin-4 constructs and knockdown | [PMID:19570982 cache](../../../publications/PMID_19570982.md), SHA-256 `c9e9b1dff9639cc3350a81e9e8fabe8f5b6589f1ef4180bec52c4e5670723d46`, Methods lines 81–95 and Results lines 129–149. Historical 26–418/26–217/98–303 construct labels remain unreconciled to the current 443-aa reference. Human ARPE-19 fibulin-4 knockdown and rat RFL6 fibulin-5 experiments remain distinct. |
| Positive staining and its resolution | [PMID:25885889 cache](../../../publications/PMID_25885889.md), SHA-256 `2b15d9f267380d515999cf2896b4697e586c4795afb9a0029388b7cb7de379d7`, immunohistochemistry Methods lines 134–142 and expression Results line 178; original Methods and Figure 1 are linked above. This is a full-text cache, not an access failure. |
| Human EFEMP2/mouse Hoxa1 | The [normal cache](../../../publications/PMID_23088713.md), SHA-256 `454acbc564312ac549cc16829eed9bcf95fa08b08647f8673364e87ebd85a457`, is abstract-only. The separately recovered original linked above contains Tables 1/2 and operative Methods. Its original XML SHA-256 is `c23822772a64d253222ef9f0e904808f4fedafd3dcfd343d8db8252e202a8881`; the independent PMC HTML SHA-256 is `e3be16778ad7d547be562c1a549bcf50216694752c317c109defa2e915af6fdf`. |
| Mixed extracellular interaction report | [PMID:27339457 cache](../../../publications/PMID_27339457.md), SHA-256 `da8c5f41db74c69cbc7618888b58904ecd32c5632f5a8531628882432ec44395`, abstract begins line 31. The curated SUBUNIT evidence and the unavailable target-specific Methods remain distinguished as above; no original-access upgrade is implied. |

The raw interaction snapshot used for the denominator has SHA-256 `3691cf639909b3d201496e7c21d03ce495f8b49b71a256739bde0ab636e343be`. Its source URL and all original fields remain in the existing [source manifest](EFEMP2-evidence/source-manifest.json) and [interaction projection](EFEMP2-evidence/interactions.json). The prior 39-row table remains the construct/method index; the new counts do not reinterpret every partner as nuclear or infer a native complex.
