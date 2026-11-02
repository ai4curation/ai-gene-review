# CD40LG evidence and annotation review — 2026-10-09

The human P29965 source seed contains 55 annotations and 24 references. This review preserves every source annotation object outside its `review` field, including GO identifiers, evidence codes, original references, qualifiers and interaction partners. Two normally fetched platelet references are added; no NEW annotation or alternative-product record is manufactured. UniProt records membrane and cleaved soluble products; absence of a seeded `alternative_products` list does not mean that there is only one mature protein form.

This is manual research after a genuine isolated Falcon attempt and its Perplexity fallback failed with network/DNS errors. No provider-named research report was generated or authored. The annotation-reviewer and core-function-synthesizer skills were applied, with the ClinGen project's standing rule retaining supported generic protein binding as KEEP_AS_NON_CORE when a more informative term is not justified.

## Biological synthesis

CD40L is a type II TNF-family membrane ligand. Human TRAP/CD40L bound a soluble CD40 construct in the cloning study [PMID:1280226]. Human T-cell surface expression was demonstrated by FACS [PMID:7678552]. Cleaved soluble human CD40L is trimeric and active, while an uncleavable membrane form also stimulates human B cells with IL-4 [PMID:8626375; PMID:8605945]. The principal activity unit is CD40 binding/activation, with membrane and soluble presentation states.

The review uses the experimentally specific CD40 receptor-binding MF in its core unit and describes agonist action explicitly. It retains cytokine-activity annotations with the soluble-product context; the current GO definition's soluble wording is not grounds to reject a whole-protein annotation when a directly demonstrated soluble form exists. Cached production GO-CAM models `663d668500001599` and `663d668500001704` already represent P29965 as cytokine activity in the CD40 signaling pathway, separate from the CD40 receptor and TRAF enzymatic/adaptor nodes. No missing process annotation is inferred from pathway completeness.

B-cell proliferation and isotype-switching annotations are refined to positive-regulation terms. CD40L supplies an extracellular signal that stimulates these responses; it does not perform the division or switch-DNA-recombination machinery itself. This is a role refinement of an established phenotype, not rejection of the original biological effect. GO:0030890 and GO:0045830 were verified against official ontology services. The core does not assign intracellular TRAF-complex membership, kinase activity, ubiquitin-ligase activity or direct transcriptional regulation to CD40L.

## Exact binding and reverse-signaling evidence

The complete PMID:31331973 abstract explicitly reports alpha5beta1 and CD40 binding simultaneously to human CD40L, alphavbeta3 binding in a KGD-independent manner, and integrin-site mutants that impair signaling while retaining CD40 binding. This supports MODIFY of the three generic binding rows: P06756/P05106 to integrin binding, P08648/P05556 to integrin binding, and P25942 to CD40 receptor binding. Integrin binding is retained as an additional contextual activity, without a claim that all integrins behave alike or that predicted docking established an experimental atomic structure. Original publisher full text remained inaccessible; complete figures and construct controls were not read.

PMID:15067037 was read through Methods, Results/Discussion and the figure legends. CD40L/CD28i coimmunoprecipitation was demonstrated in digitonin extracts of D1.1 transfectants and human peripheral-blood PHA blasts; wild-type CD28 did not associate in the reported normal-cell experiment. The GOA partner P10747 is preserved, and the CD28i/isoform-3 context is documented in the review. A detergent-sensitive receptor/adaptor association supports generic binding NC under the project instruction, not intrinsic adaptor or catalytic activity of CD40L.

The same paper measured phosphorylated JNK/PAK2 after CD40L antibody cross-linking, enhanced by CD28i expression [PMID:15067037]. GO:0043539 requires binding to and increasing serine/threonine-kinase activity. No CD40L–kinase binding or direct biochemical activator assay was demonstrated. The molecular-function annotation is MARK_AS_OVER_ANNOTATED; the downstream signaling response remains supported. Lack of an intrinsic kinase activity is not used as a substitute argument, since activators need not themselves be enzymes.

## Platelet and cell-context distinctions

PMID:9468137's complete abstract describes CD40L on already activated platelets stimulating endothelial chemokine and adhesion-molecule responses. Its exact original platelet-activation IDA provenance remains unverified; no miscitation claim is made from that abstract. Independent primary abstracts resolve the function-level question: PMID:11875495 demonstrates soluble CD40L binding alphaIIbbeta3, spreading and enhanced high-shear aggregation, with distinct KGD and CD40-deficiency controls; PMID:12676820 demonstrates CD40-blockable granule/shape activation without aggregation and no eptifibatide blockade of that response. Both cached primary abstracts were independently read. The source platelet-activation row is retained NC with these independent references and the old source uncertainty explicit. No NEW platelet process assertion is needed.

PMID:12885753 directly states endothelial apoptotic responses in its abstract, whereas CD40L has other survival-promoting contexts. These outcomes are not collapsed into one constitutive death-ligand mechanism. PAINT process assertions are retained with contextual/core distinctions, without treating the count of extant descendants as evidence against an ancestral node or calling target self-evidence circular.

## Unresolved primary assays

Four rows remain UNDECIDED rather than being rejected:

- Row44 (1-based), IL-10 production, PMID:8617933: the accessible abstract demonstrates IL-4, not the exact IL-10 experiment. UniProt and later introductory text are not an independent inspection of that experiment.
- Row45, IL-12 production, PMID:9922218: the abstract describes CD40 cross-linking in human alveolar macrophages. Selected indexed original Methods/Results text specifies immobilized anti-CD40 antibody; the full original body was not retrieved. A direct ligand assay has not been verified. No wrong-gene assertion is made.
- Row48, T-cell proliferation, PMID:8617933: the accessible abstract exposes reverse costimulation and IL-4 output, not the proliferation assay. A publisher PDF request returned403.
- Row49, anti-apoptosis, PMID:12697681: the abstract explicitly names murine recipient bone-cell models and added CD40L, but does not establish the administered ligand's species/construct. Murine recipient cells do not disprove use of human CD40L. The publisher view exposed only the abstract.

The IL-4/costimulation rows from PMID:8617933 are retained because the actual abstract directly supports them. An abstract-only source does not force every assertion to UNDECIDED when the relevant experiment is explicitly described; the unresolved rows above depend on information that was not exposed.

## Access and provenance

All 11 original PMID identifiers/titles were checked against official Europe PMC MED records and all cached abstracts read. PMID:15067037's full cached text was read for its targeted claims. Five cached Reactome summaries were read; downstream ubiquitination/degradation entries support pathway context and do not make the ligand an enzyme. The original UniProt text and GOA seed were not edited. Selected term definitions were checked against official ontology services; no source annotation ID was changed to satisfy validation.

Primary links: [CD28i reverse signaling](https://pmc.ncbi.nlm.nih.gov/articles/PMC2211876/), [integrin/CD40 binding](https://pubmed.ncbi.nlm.nih.gov/31331973/), [platelet integrin agonism](https://pubmed.ncbi.nlm.nih.gov/11875495/), [platelet CD40 responses](https://pubmed.ncbi.nlm.nih.gov/12676820/), [original endothelial inflammation study](https://pubmed.ncbi.nlm.nih.gov/9468137/).

## Adhesion refinement and review follow-up

The leukocyte adhesion row now uses positive regulation of leukocyte cell-cell adhesion (GO:1903039). Independent human CD40L treatment of HUVEC was followed by direct measurements of adherent human leukocytes, supporting regulation beyond adhesion-molecule expression [PMID:10929070]. The original PMID:9468137 NAS provenance is preserved and its detailed assay remains unverified. This does not assert that the original paper lacked an adhesion assay.

Duplicate reference entries within annotation support lists were collapsed, platelet alphaIIbbeta3 evidence was added to integrin-binding support, and the core explicitly includes soluble-trimer cytokine activity in its CD40-binding unit. Reactome location reasons now distinguish the individual recruitment, ubiquitination and degradation events. Notes describe verification directly without pointing to unpublished working files. All 55 source assertions remain unchanged outside their reviews: 26 ACCEPT, 11 KEEP_AS_NON_CORE, 13 MODIFY, four UNDECIDED and one MARK_AS_OVER_ANNOTATED. There are now 27 references; no new annotation or quotation was added.
