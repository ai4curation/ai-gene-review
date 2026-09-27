# ACOX1 (Q15067) — gene review notes

## Identity and core biochemistry

ACOX1 is the human peroxisomal **straight-chain acyl-CoA oxidase 1** (also called
palmitoyl-CoA oxidase / SCOX / AOX), UniProt Q15067, HGNC:119, gene ID 51, on
chromosome 17. It is the **first and rate-limiting enzyme of peroxisomal fatty-acid
β-oxidation**, initiating degradation of very-long-chain fatty acids (VLCFAs).

- UniProt FUNCTION: "Involved in the initial and rate-limiting step of peroxisomal
  beta-oxidation of straight-chain saturated and unsaturated very-long-chain fatty
  acids (VLCFAs)" [file:human/ACOX1/ACOX1-uniprot.txt].
- Mechanism: it is an FAD-dependent oxidase that "Catalyzes the desaturation of fatty
  acyl-CoAs that have a saturated bond between C2 and C3 (2,3-saturated acyl-CoA) to
  2-trans-enoyl-CoAs ((2E)-enoyl-CoAs), and donates electrons directly to molecular
  oxygen (O(2)), thereby producing hydrogen peroxide (H(2)O(2))"
  [file:human/ACOX1/ACOX1-uniprot.txt]. This is the key distinction from the
  mitochondrial acyl-CoA dehydrogenases, which pass electrons to ETF rather than O2.
- Reaction (EC 1.3.3.6, Rhea:RHEA:38959): "a 2,3-saturated acyl-CoA + O2 = a
  (2E)-enoyl-CoA + H2O2" [file:human/ACOX1/ACOX1-uniprot.txt].
- Cofactor: FAD (Name=FAD; Xref=ChEBI:CHEBI:57692) [file:human/ACOX1/ACOX1-uniprot.txt].
  Active site proton acceptor at residue 421; FAD binding at 139 and 178.
- Pathway: "Lipid metabolism; peroxisomal fatty acid beta-oxidation."
  [file:human/ACOX1/ACOX1-uniprot.txt].

The original biochemical characterization confirms straight-chain / eicosanoid substrate
specificity and direct O2 electron transfer: "The palmitoyl-CoA oxidase (ACOX) oxidizes
the CoA esters of straight chain fatty acids and prostaglandins and donates electrons
directly to molecular oxygen, thereby producing H2O2" [PMID:7876265]. The maximal
activities for saturated fatty acids were observed with C12-18 substrates; Km for
palmitoyl-CoA ≈ 10 µM [PMID:7876265].

Human liver actually contains two peroxisomal acyl-CoA oxidases with different substrate
specificities: (i) palmitoyl-CoA oxidase = ACOX1, "oxidizing very long straight-chain
fatty acids and eicosanoids", and (ii) a branched-chain acyl-CoA oxidase (ACOX2)
[PMID:8943006]. This is important for interpreting GOA annotations sourced from
PMID:8943006, which is primarily about the branched-chain oxidase (ACOX2) but confirms
the two-oxidase division of labour.

## Isoforms

Three alternative-splicing isoforms. Isoforms 1 (ACOX1a, exon 3I) and 2 (ACOX1b,
exon 3II) differ in substrate profile: "[Isoform 1]: Shows highest activity against
medium-chain fatty acyl-CoAs" (optimum decanoyl-CoA, C10) vs "[Isoform 2]: Is active
against a much broader range of substrates and shows activity towards long-chain and
very-long-chain fatty acyl-CoAs" [file:human/ACOX1/ACOX1-uniprot.txt]. Both can reverse
the Acox1-null mouse phenotype, isoform 2 more effectively [file:human/ACOX1/ACOX1-uniprot.txt].
The chain-length-specific MF GO terms in GOA (medium/long/very-long-chain fatty acyl-CoA
oxidase activity) reflect this isoform substrate spread and the large Rhea reaction set
in the UniProt record.

## Structure / subunit

Homodimeric FAD-flavoprotein. "The crystal structure of ACOX1 revealed that this enzyme
acts as a homodimer bound to Flavin adenine dinucleotide (FAD)" [PMID:32169171]. UniProt
SUBUNIT: "Homodimer (PubMed:32169171). Interacts with LONP2 (PubMed:18281296)"
[file:human/ACOX1/ACOX1-uniprot.txt]. The 660-aa precursor (component A) is proteolytically
processed into a 51-kDa B chain and 21-kDa C chain; the B+C heterodimer is enzymatically
active [PMID:7876265]. C-terminal SKL is the PTS1 peroxisomal targeting signal
[PMID:8117268; file:human/ACOX1/ACOX1-uniprot.txt MOTIF 658..660].

## Localization

Peroxisome / peroxisomal matrix. UniProt SUBCELLULAR LOCATION: "Peroxisome
{ECO:0000269|PubMed:32169171}" [file:human/ACOX1/ACOX1-uniprot.txt]. In the Bellen paper,
"both hACOX1WT and hACOX1N237S are localized to peroxisomes" (co-expressed eYFP-PTS1
marker) [PMID:32169171]. Import is PTS1/PEX5-dependent (Reactome R-HSA-9033235/9033236
capture the transient cytosolic → matrix translocation step). The single Reactome-sourced
`cytosol` annotation reflects the pre-import state of the newly synthesized protein, not
the site of catalysis.

## Disease

- **Peroxisomal acyl-CoA oxidase deficiency / pseudo-neonatal adrenoleukodystrophy
  (Pseudo-NALD, MIM:264470)**: autosomal-recessive single-enzyme peroxisomal disorder.
  "characterized by increased plasma levels of very-long chain fatty acids, due to
  decreased or absent peroxisome acyl-CoA oxidase activity. Peroxisomes are intact and
  functioning." [file:human/ACOX1/ACOX1-uniprot.txt]. Two new cases with abnormal plasma
  VLCFA and biallelic ACOX1 mutations (homozygous deletion; compound het p.G231V + exon-13
  skipping) [PMID:18536048].
- **Mitchell syndrome (MITCH, MIM:618960)**: a distinct disorder caused by a recurrent
  *de novo* gain-of-function variant (p.N237S) causing episodic demyelination, sensorimotor
  polyneuropathy and hearing loss. The mutant is a stabilized, more-abundant toxic homodimer:
  "the mutant homodimer is clearly much more abundant than the wild type homodimer or the
  heterodimers" and "monomeric ACOX1N237S appears to be resistant to protein turnover, and
  preferentially exists as a mutant homodimer that is a toxic" [PMID:32169171]. Elevated
  peroxisomal H2O2 drives the axonal toxicity; "H2O2 is reduced by peroxisomal catalase, an
  abundant peroxisomal enzyme responsible for the conversion of H2O2 into O2", and catalase
  over-expression rescues the phenotype [PMID:32169171].

## Annotation-review reasoning highlights

- **Core MF**: acyl-CoA oxidase activity (GO:0003997), supported by multiple experimental
  IDA/IMP (PMID:8117268, PMID:7876265, PMID:18536048, PMID:32169171). Chain-length-resolved
  children (GO:0120524 long-chain, GO:0044535 very-long-chain, GO:0120523 medium-chain
  fatty acyl-CoA oxidase activity) are Rhea/IBA refinements consistent with the isoform
  substrate data; kept.
- **Core cofactor MF**: FAD binding (GO:0071949 / GO:0050660) — kept; drug/structure/UniProt
  evidence for FAD.
- **Core BP**: peroxisomal fatty-acid β-oxidation and VLCFA catabolism
  (GO:0006635, GO:0033540, GO:0140493, GO:0000038, GO:0009062, GO:0019395) and the coupled
  H2O2 biosynthetic process (GO:0050665) — kept.
- **`fatty acid binding` (GO:0005504)** IBA + InterPro IEA: over-annotation. ACOX1 acts on
  fatty **acyl-CoA thioesters**, not free fatty acids; there is no evidence it is a
  fatty-acid-binding transport/carrier protein. MARK_AS_OVER_ANNOTATED.
- **`oxidoreductase activity` (GO:0016491) and `oxidoreductase activity, acting on the CH-CH
  group of donors` (GO:0016627)** IEA: correct but uninformative ancestors of the specific
  acyl-CoA oxidase activity. MARK_AS_OVER_ANNOTATED.
- **`generation of precursor metabolites and energy` (GO:0006091)** IMP (PMID:7876265):
  misleading for peroxisomal β-oxidation, which is degradative/chain-shortening and
  H2O2-generating rather than an ATP/energy-yielding pathway (UniProt CAUTION notes products
  are routed to ER/mitochondria). MARK_AS_OVER_ANNOTATED.
- **`lipid metabolic process` (GO:0006629)** IDA (PMID:8117268): correct but too general;
  MODIFY to fatty acid beta-oxidation (GO:0006635).
- **`prostaglandin metabolic process` (GO:0006693)** IMP (PMID:7876265): ACOX1 oxidizes
  prostaglandin CoA esters, but this is a minor/non-core activity → KEEP_AS_NON_CORE.
- **`cytosol` (GO:0005829)** TAS Reactome: reflects the pre-import (PTS1 translocation)
  state, not the catalytic compartment → KEEP_AS_NON_CORE.
- **`membrane` (GO:0016020)** HDA (PMID:19946888, NK-cell membrane proteome): non-specific
  high-throughput hit; ACOX1 is a soluble matrix enzyme → MARK_AS_OVER_ANNOTATED.
- **`PDZ domain binding` (GO:0030165)** IDA (PMID:23209302): that paper is about the
  Radil/KIF14 PDZ interaction and does not (in the cached text) establish an ACOX1 PDZ
  interaction; ACOX1's C-terminus is the PTS1 tripeptide SKL, an atypical PDZ ligand match.
  I cannot verify ACOX1 involvement from the available text → UNDECIDED (do not remove an
  experimental annotation).
- **`protein binding` (GO:0005515)** IPI (LONP2, PMID:18281296): bare protein binding, keep
  the interaction record but MARK_AS_OVER_ANNOTATED per policy (uninformative MF).
- **`protein homodimerization activity` (GO:0042803)** IDA + IEA: ACCEPT — the physiological
  quaternary structure is a homodimer (crystal structure; co-IP) [PMID:32169171].

## 2026-09-26 full annotation re-review

This dated section supersedes conflicting interpretations above; earlier notes remain as provenance. All 49 seeded assertions and three alternative-product records are preserved. The HGNC-approved symbol is ACOX1 (HGNC:119; NCBI Gene51; UniProtQ15067); aliases include AOX, ACOX, SCOX, MITCH and PALMCOX. The parent checked current main488555581d3642ba24843fc05bcb6d6517dabcd9 and found no open ACOX1 PR. Local YAML/HTML/notes blobs matched its verified baseline before editing; baseline copies are retained under `/tmp/acox1-baseline/`.

### Genuine research and access outcomes

The default Falcon request with a1200-second provider timeout and the configured perplexity-lite fallback was attempted with temporary UV tool/cache paths. Both attempts failed while bootstrapping `deep-research-client` from PyPI because of DNS resolution failure (three retries; approximately7.9 and8.7seconds). Neither research provider was invoked and no provider report exists. These notes record manual research, not an impersonated provider artifact. Concurrent normal publication caching found all9 originally cited PMIDs already cached. Separate supported fetches of isoform papers17458872/17603022 and the newly relevant16672280 failed DNS, producing no new cache. No cached publication, UniProt, GOA, citation file or previous history was edited.

The original references were all read; the only cached full research articles among the original9PMIDs are23209302 and32169171. Others were used with explicit abstract limits. Existing cached11734571 and15060085 were added for the previously uncited DHA and dicarboxylic-acid context. Their evidence is deficient fibroblasts plus pathway studies; the latter paper's recombinant experiments are LBP/DBP, not ACOX1. Newly cited16672280 remains uncached after the supported failed fetch. Its PubMed/publisher abstract and RCSB deposition were verified externally; the final PR must remain draft until the mandatory cache is recovered. Availability and identifier verification are different judgments.

### Fatty-acid binding: positive structure changes the assessment

The old claim that an acyl-CoA oxidase cannot bind free fatty acid was too categorical. GO:0005504 does not require a transport/carrier role. The [primary RCSB2DDH record](https://www.rcsb.org/structure/2DDH) identifies rat UniProtP07872 ACOX1, a661-residue wild-type recombinant protein, C2/A2 assembly with FAD and HXD ligand, (3R)-3-hydroxydodecanoic acid. The [PMID16672280 abstract](https://pubmed.ncbi.nlm.nih.gov/16672280/) explains that the crystallization acyl-CoA underwent thioester hydrolysis and the fatty-acid portion remained bound. The historical label ACO-II in this work is a rat ACOX1 isoform, not the ACOX2 paralog. This supports retained orthologous ligand recognition under crystallization conditions, without proving a separate human physiological fatty-acid carrier function. Both the IBA and InterPro binding annotations are now KEEP_AS_NON_CORE. The external abstract excerpt is explicitly identified as such; no unseen full-body evidence is claimed.

PAINT provenance was inspected in `interpro/panther/PTHR10909/PTHR10909-paint.tsv`. Binding IBDPTN000097533 (2025-09-02) draws from rat Acox2/Acox3 annotations. NCBI rat records trace the source binding annotations to PMID8654595 (both donors) and8026493 (Acox3). Their accessible abstracts assay CoA substrates, but do not settle free-acid-binding details; no donor annotation is declared wrong from abstract absence. Independent rat ACOX1 structural evidence resolves the target capability more directly. Other IBA nodes/PTN dates and human self-evidence are recorded per row; self-evidence is legitimate experimental grounding, not circularity. Electronic sources are recorded by actual proximate IDs; ARBA internals and the exact Ensembl donor chains remain explicitly unresolved.

### Radil figure: correct source identity, unresolved domain specificity

The earlier MISCITED classification for PMID23209302 is withdrawn. The [primary JCB PDF](https://rupress.org/jcb/article-pdf/199/6/951/1576653/jcb_201206051.pdf), Figure3B on journalpage955, includes ACOX1 in the Radil interaction screen. Its name is image-only and absent from the cached body extraction. The [primary figure caption](https://pmc.ncbi.nlm.nih.gov/articles/PMC3518219/figure/fig3/) describes FLAG-mRadil versus FLAG-mRadilΔPDZ affinity purification/LC-MS/MS in MDA-MB-231 cells, with identification-frequency colors across three replicates. The indexed author-thesis version independently lists ACOX1 among Figure3-3 proteins. Neither this reviewer nor the parent could read the relevant heat-map colors through the available PDF/image tools; supplementTableS2 was inaccessible. No ACOX1 wild-type/deletion contrast is inferred from unread pixels. GO:0030165 remains UNDECIDED pending that comparison and evidence distinguishing direct PDZ recognition from co-complex recovery. Figure1 direct KIF14 binding does not substitute for an ACOX1 assay.

The old terminal-SKL argument is also withdrawn: the reported Radil phage consensus is [FI]-[FWT]-WV, with a relaxed search [FI]-x-WV. SKL is not that sequence. This alone does not rule out noncanonical PDZ binding. The citation is correct and relevant; the exact annotation mechanism remains unresolved.

### Localization and interaction scope

PMID19946888 describes an NK-cell membrane-enriched proteome with many proteins not predicted to be integral membrane proteins. Its ACOX1-specific peptide/fraction/control data were inaccessible. A soluble matrix enzyme can associate with a membrane during import or other interactions; matrix localization does not disprove membrane association. The prior unsubstantiated contaminant/contradiction rationale is replaced by UNDECIDED. Experimental peroxisome rows sourced to abstract-only papers are retained with curator deference and direct independent ACOX1 targeting evidence, rather than being rejected because a title emphasizes ACOX2 or a tissue study.

PMID18281296 supports Lon/AOX co-immunoprecipitation and impaired processing under dominant-negative pLon, but explicitly reports little if any in-vitro AOX processing by pLon. The earlier assertion of proven direct LONP2 cleavage/activation is withdrawn. Generic GO:0005515 is REMOVE because it adds no informative ACOX1 molecular function; this does not deny the reported physical association or infer that ACOX1 is an adapter/protease.

### Catalytic and disease synthesis

PMID7876265 provides human palmitoyl-CoA kinetics (Km10micromolar, Vmax1.4units/mg), maximal saturated-substrate activities with C12–18, prostaglandin-CoA oxidation and direct oxygen reduction producing H2O2. Thus medium/long substrate classes are supported independently of the inaccessible full isoform-comparison papers. UniProt/Rhea reaction lists support the curated very-long-chain class but are not represented as individually measured purified-human assays. No exclusive family substrate boundary is inferred against ACOX2/ACOX3; paralog side activities do not invalidate ACOX1's established range.

PMID32169171 full text distinguishes fly loss of function (VLCFA accumulation) from humanN237S gain of function (stabilized dimer, about40% greater protein-normalized activity and H2O2-associated toxicity; not the same VLCFA accumulation phenotype). Figure4C localizes expressed human protein with eYFP-PTS1 in flies. Figure6E tests tagged human wild-type/mutant pairings in primary Schwann cells; Methods specify rat-derived cultures. The article cites earlier rat structural work, rather than solving a new human ACOX1 structure itself. These assay-specific results replace introductory or catalase-consumption quotes that did not directly support the annotation under review.

The integrated core is matrix acyl-CoA oxidation with FAD, homodimerization and direct H2O2 production. Separate cofactor-binding and homodimer cores were consolidated without withdrawing those annotations. Full-length componentA is cleaved to complementary B/C chains; it is inaccurate to describe cleavage as creating A/B/C simultaneously. GO:0006091 includes precursor formation, so lack of direct ATP production does not make it false. That broad process and broad fatty-acid/lipid/oxidoreductase annotations are refined using MODIFY. No NEW annotation was introduced. Reactome's C24:6 summary is used for chemistry despite its inconsistent tetracosapentaenoyl display name; fetched source text/title remain untouched.

### Validation and handoff

`just validate human ACOX1` passed with the single expected warning that PMID:16672280 could not be fetched. `just render human ACOX1` and validation of the scaffolded history record passed. The resulting 49 actions are 36 ACCEPT, 5 KEEP_AS_NON_CORE, 5 MODIFY, 2 UNDECIDED and 1 REMOVE. Source assertions and alternative products match the baseline exactly. The rendered HTML was checked for the revised binding, PDZ, localization and integrated-core content. Independent biological review was requested and remains pending at this handoff; no independent sign-off is implied. The missing publication cache keeps the proposed PR in draft. No Git or remote publication actions were performed by this reviewer.

Independent annotation-reviewer consultation subsequently completed: the peer inspected all 49 actions, the integrated core and all 24 reference judgments, and independently checked RCSB 2DDH plus the principal cached human enzyme, patient, interaction and pathway sources. No blocking biological concern was found. The peer also could not read the relevant Radil heat-map pixels, supporting the bounded PDZ uncertainty. Two minor prose changes were adopted: historical rebuttal clauses were removed from current annotation reasons while their history remains here, and expression/C26-oxidation Reactome references received event-specific notes. Actions and source objects remain unchanged.


## 2026-09-26: PR #3159 bounded evidence-provenance follow-up

This dated entry supersedes the earlier final action tally and GO:0006091 replacement, while leaving prior notes as historical provenance. The molecular-function review is complete, but the YAML status is now **DRAFT**, matching the schema definition for reviewed annotations with remaining validation warnings. The PR must remain draft until the required PMID:16672280 cache is recovered by the normal fetch workflow. No publication text was fabricated and no source cache was changed.

### Free-fatty-acid binding and verification route

Re-read the primary [RCSB 2DDH deposition](https://www.rcsb.org/structure/2DDH) and [HXD chemical-component record](https://www.rcsb.org/ligand/HXD) on 2026-09-26. The structure's Literature section explicitly links PMID:16672280, DOI:10.1093/jb/mvj088, and the article title, and reproduces the PubMed abstract. Its macromolecule maps to rat P07872/ACOX1, while the ligand table identifies free (3R)-3-hydroxydodecanoic acid. This is an independently checkable primary route for citation and ligand identity. Direct PubMed access returned a CAPTCHA during this follow-up; the DOI publisher redirect was inaccessible. These current access failures do not reverse the primary-record verification. The earlier normal cache fetch failed DNS and no access change justifies blindly repeating it.

The abstract describes the free carboxyl oxygen hydrogen bonding to the Glu421 backbone and FAD ribityl group after thioester hydrolysis in the crystallization experiment. Those contacts support a bound free acid in the substrate channel. Under the [live GO:0005504 definition](https://amigo.geneontology.org/amigo/term/GO%3A0005504), the ligand's noncovalent binding meets the molecular capability being annotated; the term does not require a distinct carrier site. This is a bounded inference from the rat ortholog, not a human affinity measurement, a second binding site, or a physiological free-acid carrier role. The two rows remain KEEP_AS_NON_CORE. Unresolved Acox2/Acox3 donor assays are not treated as independent proof of free-acid binding.

Because the quotation is an externally read **abstract** excerpt, it is now placed in `supporting_text`, where it can be checked against the normal cache once recovered. Its missing-cache warning remains an explicit publication gate. `reference_review.correctness: VERIFIED` records independently checked identifier/source identity; it does not claim that a cache exists or that the full article body was read. `full_text_unavailable: true` remains in place.

### Other review suggestions

The [live GO:0006635 displayed is_a ancestry](https://amigo.geneontology.org/amigo/term/GO%3A0006635) does not include [GO:0006091](https://amigo.geneontology.org/amigo/term/GO%3A0006091). This checks the displayed relation scope, not every possible ontology relation. The latter term includes pathways forming precursor metabolites; it is broader than direct ATP production. PMID:7876265 directly assays active recombinant human ACOX1. Retain the original broad experimental process as **KEEP_AS_NON_CORE** with a precursor-pathway interpretation and curator deference, alongside the precise beta-oxidation annotations. No claim is made that the oxidase itself releases acetyl-CoA or makes ATP.

The R-HSA-9033236 cytosol row now carries its own exact cached docking-event quote. The membrane HDA remains UNDECIDED: the abstract's aggregate proportions and proposed transient associations do not identify ACOX1's treatment-dependent fraction, peptide evidence or localization controls. Calling the ACOX1 hit an over-annotation solely from those aggregate statistics would exceed the accessible evidence. The current reason explicitly distinguishes this unresolved experiment from the established matrix role.

Final actions are **36 ACCEPT, 6 KEEP_AS_NON_CORE, 4 MODIFY, 2 UNDECIDED and 1 REMOVE**. Only row 45 changed action in this follow-up. All 49 source assertion objects and three alternative products remain unchanged. Prior notes are retained verbatim before this dated entry. Targeted checks, render, append-only history validation and exact four-file publication hashes are supplied in the follow-up manifest; the missing PMID cache remains a blocker even if schema validation otherwise passes.


## 2026-09-27: Required publication cache recovered

Recovered required PMID:16672280 through standard fetch-pmid in read-only Actions run 36286975328 (job 108529455048, artifact 10920674630), transported unchanged by read-only run 36288441414. Verified artifact SHA256 c0ffe4a66b80278af34b44aab6a3ae354ffd5699236b3a486ca95527be5e9713 and every record SHA256/Git blob before importing. Re-read this abstract, confirmed exact citation title and retained full_text_unavailable=true. All annotation decisions, source objects, core functions, reference identities and alternative products remain unchanged from a6069e17b0055b08fea3eba788d759c16318e8a0. Targeted validation passed with 0 warnings; YAML status is COMPLETE. The machine cache requirement is satisfied; source-limited UNDECIDED judgments remain explicit.

This supersedes the earlier missing-cache publication gate. The recovered record is abstract-only; neither its presence nor successful validation establishes access to the full paper. Zero remaining validation warnings permit COMPLETE status and a ready PR.

Final checks: `just validate human ACOX1`, `just render human ACOX1` and the new history validation all passed. The parsed review differs only in source-access notes and, where applicable, status; every biological decision and source field is preserved.
