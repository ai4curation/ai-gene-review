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
