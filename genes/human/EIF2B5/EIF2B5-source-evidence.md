# EIF2B5 source evidence and access guide

This guide records the evidence used for the 58 imported assertions and the integrated nucleotide-exchange mechanism. Publication-cache flags describe the machine cache; the access statements below describe what was actually inspected. External original sections can therefore be available even when the normal cache is abstract-only. Article bodies are not redistributed in the portable database archive.

The [source-locator inventory](EIF2B5-bioinformatics/original-locators.json) supplies normal-cache hashes, public routes, retained snapshot hashes and precise text scopes. Independent source consultations are identified as such; they are not represented as duplicate original reads. No figure pixels were inspected for these assessments.

## Database evidence

The [reproducer](EIF2B5-bioinformatics/README.md) checks every imported GOA context, the 721-residue official sequence, the PAINT lineage and four positive IBD records, exact ARBA predicates, complete saved donor queries, literal IntAct records and human Reactome paths. The HPA parser preserves the location-specific enhanced Cytosol score and all six antibody/cell-line records. Source absence from a current interaction query does not invalidate a historical curated association.

GO_REF references identify methods and have LOW relevance individually; they do not substitute for target evidence. Physical association and independently verified partner class support the specific binding refinements. No partner activity is attributed to epsilon.

## Primary-source scopes

### PMID:10481074

Engineered epsilon534–547 peptide with substitutions/phosphoserine544 associates with GSK3B in kinase assays; partner class is independently verified.

**Inspected:** Normal abstract, official metadata, both source-specific human IntAct kinase-assay records and explicit target/partner feature fields.

**Limit:** Publisher PDF HTTP403; no intact epsilon/native-complex claim.

Source: https://pubmed.ncbi.nlm.nih.gov/10481074/; cache `publications/PMID_10481074.md`, SHA256 `e01fe6e5e61b5e5f8bc7d33a8dddf8dc6fd88b1ffc35da5202aeb606399aceac`.

### PMID:11323413

Native human five-subunit complex depleted of eIF2 supports exchange and cytoplasmic complex membership.

**Inspected:** Author-uploaded original, selected factor-preparation, chromatography, subunit-analysis and GDP-dissociation Methods/Results (captured text lines 468–721).

**Limit:** Not a full-paper or isolated-epsilon preparation claim.

Source: https://pubmed.ncbi.nlm.nih.gov/11323413/; cache `publications/PMID_11323413.md`, SHA256 `ec823995789c31c53a1f798bf81023d5d4e493a969308461b1b15e80f3bc7337`.

### PMID:11500362

Native human phosphorylation is separate from detailed recombinant rat epsilon mutants. Rat S712/713GA changes eIF2 association/complex exchange; free epsilon activity is very low relative to assembled complex.

**Inspected:** PMC indexed10,16,43–49,54,55,57,61,63,65,67,69.

**Limit:** Rat residue numbers not mapped to human without alignment; no complete supplemental vector inspection.

Source: https://pubmed.ncbi.nlm.nih.gov/11500362/; cache `publications/PMID_11500362.md`, SHA256 `f2a620cd6154034a94b551809898986a63d0f731559eaa98b11baf9b10ef3532`.

### PMID:11756553

Rat epsilon S535A/S539A constructs in Rat1/PC12 preserve translation and resist GSK3/PI3K-inhibitor/serum-withdrawal apoptosis. Phosphorylation inhibits pro-translation activity; no active WT epsilon proapoptotic step established.

**Inspected:** Saved PMC indexed Methods10/17–20, Results23–45/47, Discussion49–54; exact causal reread included resistant-mutant, tau and cycloheximide controls.

**Limit:** No universal antiapoptotic function or opposite NEW. Figure captions/text read, not pixels. MAO is role scope, not a conclusion from WT overexpression alone.

Source: https://pubmed.ncbi.nlm.nih.gov/11756553/; cache `publications/PMID_11756553.md`, SHA256 `aec5cb3341f3305a0fb5a7fcddd61377dd81eccdbf85b5e78b8d9751219fc529`.

### PMID:12388085

Endogenous mouse NIH3T3 epsilon shows nuclear and cytoplasmic staining and stress-granule redistribution; current Q8CHW4 IDA donor is genuine.

**Inspected:** Publisher-indexed original Results, Figures 1–2 captions and Discussion, including the fixation comparison. Direct publisher requests failed; complete Methods and figure pixels were not inspected.

**Limit:** Positive mouse localization is retained; fixation affects relative staining, and this does not establish exclusive human nuclear residence.

Source: https://pubmed.ncbi.nlm.nih.gov/12388085/; cache `publications/PMID_12388085.md`, SHA256 `a2a6881d2c74be404fc22bcb8def4ce8e1b862370b00f9ba58af4fab9269d872`.

### PMID:12426392

Human epsilon-eGFP in BHK cells shows basal cytoplasm/nuclear exclusion; engineered NLS plus leptomycin experiments have different scope.

**Inspected:** Selected original Results, Methods and captions concerning eIF2B-epsilon–eGFP, nuclear-localization-signal constructs and leptomycin B; indexed paragraphs 9,18,49,50,52,53,55,57–60,69–71,90,91.

**Limit:** No complete insert-sequence verification or universal nuclear-exclusion claim; text/captions read, not pixels.

Source: https://pubmed.ncbi.nlm.nih.gov/12426392/; cache `publications/PMID_12426392.md`, SHA256 `58b29f9210cc36331900b9a1caa960ef75dac4896714d6b7578ddca1cb9a89e2`.

### PMID:12499492

Homozygous EIF2B5 severe disease with low uric acid/elevated GDP sugars; heat-specific experiment not exposed.

**Inspected:** Verified abstract; full original unavailable.

**Limit:** Publisher failure; no title/abstract-only wrong-gene claim.

Source: https://pubmed.ncbi.nlm.nih.gov/12499492/; cache `publications/PMID_12499492.md`, SHA256 `efcb1d43c86350b0b95d0fb684be641ebb1ca10b63b2d6af582256727d89b2fe`.

### PMID:12707859

Seven mutated patients include EIF2B5 R113H homozygotes and R113H/R195C; ovarian failure and white-matter disease are positive clinical evidence.

**Inspected:** Normal indexed blocks13–35, human cases/genotyping/clinical findings and Discussion.

**Limit:** No follicle-development assay; complete table cells not reproduced in the normal cache.

Source: https://pubmed.ncbi.nlm.nih.gov/12707859/; cache `publications/PMID_12707859.md`, SHA256 `44f03632f92045e00942a2d3055e3050718af3c394fdec01b4f5623b0db69f71`.

### PMID:12850562

Rat hippocampal eIF2B-subunit expression changes developmentally; no functional hippocampus-development assay reported in inspected scope.

**Inspected:** Official Europe PMC core metadata/abstract, checked against the selected normal cache metadata; no full body inspected.

**Limit:** Donor species and the limited abstract scope retained; normal shared bytes reused where available.

Source: https://pubmed.ncbi.nlm.nih.gov/12850562/; cache `publications/PMID_12850562.md`, SHA256 `8ee4b4d22ba09cefb30535d8971b10903b1a9e4878a0cbef0d10f2ca7a214efe`.

### PMID:14566705

EIF2B5 patients7(V430A/S447L) and8(Y495C homozygous) have severe abnormal myelination/rarefaction.

**Inspected:** Original Methods, clinical/MRI Results and Table 1; indexed paragraphs 14–28, including MRI Results 18, caption 20 and Table 1 at 26.

**Limit:** Clinical/pathological observations do not themselves identify a direct epsilon myelin-sheath formation step.

Source: https://pubmed.ncbi.nlm.nih.gov/14566705/; cache `publications/PMID_14566705.md`, SHA256 `6bd9ac2ef7155c6eb4f57e7490a187758325666c17f77da848671e626e0b536a`.

### PMID:15054402

Patient EBV lymphoblast extracts, rat-liver eIF2 substrate, triplicate GDP dissociation; multiple literal EIF2B5 genotypes reduce complex activity, heterozygotes normal.

**Inspected:** Author-uploaded original, selected Methods, Table 1 and GDP-dissociation Results (captured text lines 336–786).

**Limit:** Patient lysates are not isolated epsilon; no figure pixels.

Source: https://pubmed.ncbi.nlm.nih.gov/15054402/; cache `publications/PMID_15054402.md`, SHA256 `25c3ade454409e484565cfd159428846636bc653117aa2a6a2e02c63d46be939`.

### PMID:15060152

Full-length sequence-verified human clones in HEK293; gamma binds epsilon in a two-subunit expression context, delta is recovered with assembled complex. Human epsilon variants affect exchange/substrate association.

**Inspected:** Partial normal original text plus externally recovered full-length cloning, complex-formation Results and Figure 1 caption. The normal cache does not contain the complete Methods.

**Limit:** Cache flag true does not imply complete Methods; selected recovered sections only. No synthesized insert-to-current-reference equivalence assumed.

Source: https://pubmed.ncbi.nlm.nih.gov/15060152/; cache `publications/PMID_15060152.md`, SHA256 `156d464d437c17d85a21181b9cb56c5a01f86eef50a76d9fa1a267f6de81b1dc`.

### PMID:15217090

Four patients have EIF2B5 and one EIF2B2; oligodendrocyte density, apoptosis-associated staining and myelin pathology measured. Increased density has unresolved proliferation/survival explanations.

**Inspected:** Author-uploaded original, selected autopsy Methods, genotypes, quantification and Discussion; captured text lines 250–661, 477–1200, 1360–1545 and 1864–1882 in the saved views.

**Limit:** Selected original windows, not complete-paper/pixel inspection; no lineage-progress assay inferred.

Source: https://pubmed.ncbi.nlm.nih.gov/15217090/; cache `publications/PMID_15217090.md`, SHA256 `2d08c635e04d508330ae04bbac0a2ff52a48f3b6b47a6b8204a82d8957da940d`.

### PMID:15507143

93 isolated POF women were negative for screened known variants; prior positive ovarioleukodystrophy is discussed, not experimentally recapitulated.

**Inspected:** Original Methods, Results and Discussion; indexed paragraphs 14–34.

**Limit:** No assertion that all ovarian EIF2B5 variants were excluded.

Source: https://pubmed.ncbi.nlm.nih.gov/15507143/; cache `publications/PMID_15507143.md`, SHA256 `fbe1a6164c493f2f8592828e21367e6dae6b5a4ccd50ff92117a0860c5fc0eab`.

### PMID:15723074

Affected human cultures produce few abnormal GFAP-positive astrocytes; normal human glial-progenitor EIF2B5 RNAi impairs GFAP induction. Normal-appearing oligodendrocytes reported.

**Inspected:** Normal abstract, Nature publisher preview, figure titles3/4 and available supplement link metadata.

**Limit:** Full operative main Methods/supplements inaccessible; direct figure-page attempts failed. No heat or sheath-formation experiment reconstructed.

Source: https://pubmed.ncbi.nlm.nih.gov/15723074/; cache `publications/PMID_15723074.md`, SHA256 `88b91229a68d240723900a3d8680e5e9daaa3ee99a22f0a78f5a1cbe257c92bf`.

### PMID:16041584

Patient eIF2B-mutant fibroblasts show heightened ATF4 response with similar broad translational inhibition/upstream kinase activation.

**Inspected:** Normal and official Europe PMC abstracts; publisher payload inspected and identified as HTML challenge.

**Limit:** Specific EIF2B5 genotype and operative experiments unresolved; HTTP200 HTML is not a PDF.

Source: https://pubmed.ncbi.nlm.nih.gov/16041584/; cache `publications/PMID_16041584.md`, SHA256 `b124358737d83cbbcb20f9342a4f2f6da0f4ff33e05dcefe7962b1831e288e31`.

### PMID:16289705

eIF2/eIF2B supplementation improves HeLa-extract translation; the added factor species/preparation is unresolved in this access scope.

**Inspected:** Verified abstract and independent access assessment; complete operative Methods unavailable.

**Limit:** Full operative Methods unavailable; broad complex function has independent support.

Source: https://pubmed.ncbi.nlm.nih.gov/16289705/; cache `publications/PMID_16289705.md`, SHA256 `c62fe42768288a45221c04cf0fec987399e51cf494933d632429092a65121792`.

### PMID:20484009

Rat epsilon-FLAG muscle electroporation increases GEF; restores sepsis-depressed synthesis, while healthy-muscle synthesis need not rise.

**Inspected:** PMC indexed9,10,13–16,20,24,25,28,30,32,36,37.

**Limit:** Rat muscle/homogenate context, not isolated human epsilon activity.

Source: https://pubmed.ncbi.nlm.nih.gov/20484009/; cache `publications/PMID_20484009.md`, SHA256 `bf571a26cf79d435559fd2170986b9de92695434df644606d89122e71b4b6de9`.

### PMID:25858979

Whole-complex GDP release, CHO delta-mutant and mouse-fibroblast contexts are distinct. Purified complex species/construct and the sequence exception cannot be resolved without the missing Methods/table.

**Inspected:** Independent original-source consultation: main text and captions read, with supplementary Table S1 and complete purification details unavailable.

**Limit:** Whole-complex exchange and CHO delta-mutant experiments do not establish an isolated-epsilon assay; unread supplementary sequence details remain unresolved.

Source: https://pubmed.ncbi.nlm.nih.gov/25858979/; cache `publications/PMID_25858979.md`, SHA256 `48e7de1b46a1e59dea4d02c75879e4402e9d957cc202ddf87b844dbe91775dc1`.

### PMID:27023709

Human eIF2/eIF2B reconstituted-translation comparator exists; detailed purification/crystal work is primarily S. pombe.

**Inspected:** Independent original-source consultation: operative Methods/Results, including the human comparator in Methods paragraph 12, Results paragraph 23 and Figure 2h.

**Limit:** Most detailed purification and structural work concerns S. pombe; the human comparator is retained separately.

Source: https://pubmed.ncbi.nlm.nih.gov/27023709/; cache `publications/PMID_27023709.md`, SHA256 `24fbdc63dc56c647ba96c8d3cae410754631c826d7584d48c8456ded906aa52b`.

### PMID:29599213

Five codon-optimized human genes expressed in E. coli; alpha2 plus beta/gamma/delta/epsilon reconstitution and exchange support complex function.

**Inspected:** Independent original-source consultation: printed pages 1–3 and selected Discussion plus cloning, purification and GDP-assay Methods on pages 7–9 of the author-hosted article.

**Limit:** Supplementary exact insert sequence and figure pixels were not inspected; no isolated human epsilon assay claimed.

Source: https://pubmed.ncbi.nlm.nih.gov/29599213/; cache `publications/PMID_29599213.md`, SHA256 `8e41c97522808119bef1e4a699e5da88ae84997783a655d903fcb30f7f84fb22`.

### PMID:31048492

Human epsilon entity5 chains I/J expressed in E. coli has exact official 721-residue sequence; whole-complex identity does not establish contact geometry or isolated activity.

**Inspected:** Verified abstract and official PDB 6K72 entity 5 sequence/organism metadata; full original Methods/Results unavailable.

**Limit:** Full original Methods/Results unavailable; metadata is not operative Methods.

Source: https://pubmed.ncbi.nlm.nih.gov/31048492/; cache `publications/PMID_31048492.md`, SHA256 `afbee8df7ae0688f4a14df19dde73521629405a230f0997e5c36f6380728d1d3`.

### PMID:32296183

Human ORFeome9.1 binary screening with pair verification; exact target pair positive in three Y2H configurations.

**Inspected:** Normal indexed blocks16–19,44–45,50,52; all literal target STX11 IntAct records and features.

**Limit:** Dataset-level orthogonal validation is not assigned to this pair; exact natural isoform insert not proven.

Source: https://pubmed.ncbi.nlm.nih.gov/32296183/; cache `publications/PMID_32296183.md`, SHA256 `de8eeaee8fd10c8537ad6b2f69602d414b6f1896221b208edb8ffbae9eaa263b`.

### PMID:32814053

Positive Y2H screen records support identified dynein-heavy-chain and protease partners.

**Inspected:** All11 normal-cache blocks; human Q13144–Q14204 and Q13144–Q92876 source-specific IntAct records.

**Limit:** No complete Methods or exact insert-sequence proof; reference sequence checksums do not establish assayed inserts.

Source: https://pubmed.ncbi.nlm.nih.gov/32814053/; cache `publications/PMID_32814053.md`, SHA256 `df9eea608bd1079b9e3320715db0c16712ded397fd7cfde26b291d9ad54e6f3b`.

### PMID:33961781

C-terminally tagged STX11 associates with epsilon; syntaxin class is independently verified.

**Inspected:** Selected normal original Introduction/Discussion and exact STX11 anti-tag co-IP record.

**Limit:** Cache flag true does not prove complete Methods; physical association is not necessarily binary binding.

Source: https://pubmed.ncbi.nlm.nih.gov/33961781/; cache `publications/PMID_33961781.md`, SHA256 `4763a1c8018e1b047fc1c2bf3d0e72c837e4b4c3dffbed428befa479e1c92286`.

### PMID:8168527

Rabbit epsilon-directed antibodies inhibit exchange and translation initiation; other-subunit antibodies are distinct.

**Inspected:** Official Europe PMC core metadata/abstract, checked against the selected normal cache metadata; no full body inspected.

**Limit:** Donor species and the limited abstract scope retained; normal shared bytes reused where available.

Source: https://pubmed.ncbi.nlm.nih.gov/8168527/; cache `publications/PMID_8168527.md`, SHA256 `038e6230e9d739b183cae1f98e868c90bbfeac17cb235aebbacbbd3d2f522d65`.

### PMID:8397507

Human-insulin-receptor-transfected CHO cells show insulin-dependent GSK3 inactivation; that kinase phosphorylates the largest eIF2B subunit.

**Inspected:** Complete selected normal abstract.

**Limit:** Host is hamster, receptor human; no direct epsilon hormone-response step or factor preparation species inferred.

Source: https://pubmed.ncbi.nlm.nih.gov/8397507/; cache `publications/PMID_8397507.md`, SHA256 `b2c7296f98bacffcf5fe02c3d8c563d7eb0a863e9aec3566d60325c40570f46d`.

### PMID:8430778

Diabetic rat muscle exchange activity differs by tissue; NADPH/CKII assays reported, explicit peptide-hormone stimulus unresolved.

**Inspected:** Official Europe PMC core metadata/abstract, checked against the selected normal cache metadata; no full body inspected.

**Limit:** Donor species and the limited abstract scope retained; normal shared bytes reused where available.

Source: https://pubmed.ncbi.nlm.nih.gov/8430778/; cache `publications/PMID_8430778.md`, SHA256 `db70d61bfaf724f85a3c21ac95a45e4889d4038509d8f7e5e0d629eb6d5225db`.

### PMID:8567668

Rat pancreatic-islet glucose increase raises exchange activity rapidly; metabolic inhibition blocks the response.

**Inspected:** Official Europe PMC core metadata/abstract, checked against the selected normal cache metadata; no full body inspected.

**Limit:** Donor species and the limited abstract scope retained; normal shared bytes reused where available.

Source: https://pubmed.ncbi.nlm.nih.gov/8567668/; cache `publications/PMID_8567668.md`, SHA256 `f1e63f45add5ce6dfd63eadec562b0e855d8a04db3542ab47e5fd03a6b626bbd`.

### PMID:8626696

Human T-cell activation increases whole-complex eIF2B activity and changes GSK3/beta abundance.

**Inspected:** Verified abstract and independent source consultation covering publisher-indexed selected Results/Discussion; complete Methods unavailable.

**Limit:** Complete Methods and epsilon-specific TCR mechanism unresolved; beta focus is not negative epsilon evidence.

Source: https://pubmed.ncbi.nlm.nih.gov/8626696/; cache `publications/PMID_8626696.md`, SHA256 `396404cd79b61da5068d4b6e5c9e022a60d8d5d38c47a2dfa22214c4c6e1f5e7`.

### PMID:8688466

Rabbit epsilon cloning and human U937 fragment establish identity/conservation; an initially incomplete clone is not a natural product or isolated-human catalytic assay.

**Inspected:** Verified abstract; full publisher text returned HTTP 403.

**Limit:** Full original unavailable; no isolated-human catalytic assay or natural alternative product inferred.

Source: https://pubmed.ncbi.nlm.nih.gov/8688466/; cache `publications/PMID_8688466.md`, SHA256 `bda26f939c869f938da959968fd7e943570a8d5fb170f75324557c19cde12de7`.

### PMID:9139680

Five rat genes expressed in Sf9; epsilon alone has exchange activity in extracts, assembled subunits strongly enhance it; alpha controls phosphorylated-eIF2 inhibition.

**Inspected:** Official Europe PMC core metadata/abstract, checked against the selected normal cache metadata; no full body inspected.

**Limit:** Donor species and the limited abstract scope retained; normal shared bytes reused where available.

Source: https://pubmed.ncbi.nlm.nih.gov/9139680/; cache `publications/PMID_9139680.md`, SHA256 `7817491cd36fd35d28068ff897ebc5ba4cd50a0ed288cfa70c6668497ddbeca9`.

### PMID:9341116

Rat H35 heat exposure changes whole-complex exchange activity and protein synthesis; no epsilon thermosensor assay.

**Inspected:** Official Europe PMC core metadata/abstract, checked against the selected normal cache metadata; no full body inspected.

**Limit:** Donor species and the limited abstract scope retained; normal shared bytes reused where available.

Source: https://pubmed.ncbi.nlm.nih.gov/9341116/; cache `publications/PMID_9341116.md`, SHA256 `4bedb999860ab6aff71a95a5f89b3c7bd45f1c611a64d6f34432084ac707594c`.

## Remaining uncertainty

Rows 47, 49, 51, 52 and 57 remain UNDECIDED. The missing genotype/operative-assay details for ER stress and myelination, the unresolved peptide-hormone stimulus in the rat-muscle donor, and the lack of an epsilon-specific T-cell-receptor step are distinct limitations. They are not negative experiments or evidence of a wrong gene.

The heat annotations are retained as non-core from the combined same-gene evidence, including the direct rat heat donor. Their individual original-source limits remain in the reference assessments. Clinical and perturbation observations are not promoted into autonomous developmental or apoptotic mechanisms.
