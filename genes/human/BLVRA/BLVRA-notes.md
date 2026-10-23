# BLVRA (Biliverdin reductase A) — review notes

UniProt: P53004 (BIEA_HUMAN). Gene: BLVRA (HGNC:1062). Taxon: Homo sapiens (NCBITaxon:9606).
EC 1.3.1.24. 296 aa; a Precursor (propeptide 1..2 removed, mature chain 3..296).

## Canonical function (primary): biliverdin reductase A

BLVRA catalyzes the **second step of heme catabolism**: reduction of the gamma-methene
bridge of biliverdin IXalpha to bilirubin IXalpha, with concomitant oxidation of NADH or
NADPH. It follows heme oxygenase (HMOX1/HMOX2), which opens the heme ring to biliverdin.

- "Reduces the gamma-methene bridge of the open tetrapyrrole, biliverdin IXalpha, to
  bilirubin with the concomitant oxidation of a NADH or NADPH cofactor"
  [file:human/BLVRA/BLVRA-uniprot.txt FUNCTION, ECO:0000269 PubMed:10858451/7929092/8424666/8631357].
- EC=1.3.1.24; Rhea RHEA:15797 (NAD+) and RHEA:15793 (NADP+); PhysiologicalDirection
  right-to-left (i.e. biliverdin -> bilirubin) [file:human/BLVRA/BLVRA-uniprot.txt CATALYTIC ACTIVITY].
- PATHWAY: "Porphyrin-containing compound metabolism; protoheme degradation"
  [file:human/BLVRA/BLVRA-uniprot.txt PATHWAY].
- Reactome R-HSA-189384 "BLVRA:Zn2+, BLVRB reduce BV to BIL": "BIL is formed from the
  reduction of biliverdin (BV) by bilverdin reductases BLVRA and BLVRB"
  [reactome:R-HSA-189384].

### Dual cofactor / dual pH — unusual property
- "BVR is unique among enzymes characterized to date in that it has dual pH/cofactor
  (NADH, NADPH) specificity" [PMID:8631357 abstract].
- "At pH 6.0-7.0 the NADH was the more effective cofactor, whereas at pH 8.5-8.75 NADPH
  was the preferred cofactor" [PMID:8424666 abstract].
- "It was assumed that NADPH rather than NADH was the physiological electron donor in the
  intracellular reduction of biliverdin" [PMID:7929092 abstract]; UniProt: "NADPH,
  however, is the probable reactant in biological systems (PubMed:7929092)".
- KM: 3.2 uM for NADPH, 50 uM for NADH [file:human/BLVRA/BLVRA-uniprot.txt BIOPHYSICOCHEMICAL PROPERTIES].
- Alpha-isomer specific: "as previously discussed for the rat and ox enzymes, it appears
  that at least one 'bridging propionate' is necessary for optimal binding and catalytic
  activity, whereas two are preferred" (BVR-A prefers IXalpha; BLVRB handles IXbeta)
  [PMID:10858451 abstract]. "Does not reduce bilirubin IXbeta (PubMed:10858451)"
  [file:human/BLVRA/BLVRA-uniprot.txt FUNCTION].

### Zinc metalloprotein
- "Atomic absorption spectroscopy indicates that the protein purified from human liver
  contains Zn at an approximately 1:1 molar ratio" [PMID:8631357 abstract]; UniProt
  COFACTOR "Binds 1 zinc ion per subunit" (Note is ECO:0000305, an inference)
  [file:human/BLVRA/BLVRA-uniprot.txt COFACTOR]. FT BINDING residues 280/281/292/293 for Zn2+
  are annotated with ECO:0000303 (from-statement in the paper), i.e. not a hard structural
  determination. The physiological necessity of Zn is debated (the 2H63 crystal structure
  is with NADP, monomer; no Zn in the FUNCTION statement). Treat zinc binding as
  KEEP_AS_NON_CORE / accept-as-cofactor rather than a core catalytic MF.

### Localization
- Cytosol: "Conversion of biliverdin to bilirubin is catalyzed by the cytosolic enzyme
  biliverdin reductase" [PMID:8424666 abstract]; enzyme isolated from "human liver
  cytosolic fractions" [PMID:7929092 abstract]. UniProt SUBCELLULAR LOCATION "Cytoplasm,
  cytosol" [file:human/BLVRA/BLVRA-uniprot.txt].
- Tissue: Liver [file:human/BLVRA/BLVRA-uniprot.txt TISSUE SPECIFICITY]; HPA "Low tissue
  specificity" (broadly expressed).
- Extracellular exosome (HDA) from two large-scale exosome proteomics datasets
  (PMID:19056867 urinary exosomes; PMID:20458337 B-cell exosomes). These are
  high-throughput MS detections; the protein is a soluble cytosolic enzyme that is a
  common exosome cargo — KEEP_AS_NON_CORE (not a functional location).

## Moonlighting function (genuine second role): kinase / MAPK scaffold

Human BVR-A is a well-documented dual-specificity Ser/Thr/Tyr kinase and signaling
scaffold in insulin/IGF1/MAPK/PI3K and PKC pathways, and a transcriptional regulator
(leucine-zipper) for HMOX1.

- "Human biliverdin reductase (hBVR) is a recently described Ser/Thr/Tyr kinase in the
  MAPK insulin/insulin-like growth factor 1 (IGF1)-signaling cascade" [PMID:18463290
  abstract]. It forms a ternary MEK/ERK/hBVR complex, activates MEK1 and ERK1/2, is an
  ERK nuclear transporter required for Elk1 transcriptional activity, and "in the complex,
  hBVR functions as a scaffold" [PMID:18463290 full text, PMC2383961].
- Also documented (in this paper's discussion) as an activator of PKCbetaII and PKCzeta
  through protein-protein interaction [PMID:18463290].

This role is not present in the curated GOA TSV (BLVRA-goa.tsv). It appears only as
electronic IEA:Ensembl projections in the UniProt DR GO section
(GO:0004674 protein serine/threonine kinase activity; GO:0000978 RNA Pol II CRM
sequence-specific DNA binding; GO:0005634 nucleus; GO:0009986 cell surface). Because it
is a genuine, experimentally described function of the human protein, it is captured as a
**second core function** (protein serine/threonine kinase activity, GO:0004674), grounded
in PMID:18463290, rather than being ignored. NB the kinase/scaffold role has been assayed
almost entirely by one group (Maines lab); flag as an expert question.

## Protein interactions (IPI, GO:0005515) — bare "protein binding"
GOA has four IPI "protein binding" annotations. Per policy these are not removed (they are
experimental IPI); marked MARK_AS_OVER_ANNOTATED because bare protein binding is
uninformative. The with/from partners:
- PMID:18463290 -> UniProtKB:P28482 (MAPK1/ERK2) — meaningful (the ERK-scaffold role);
  UniProt INTERACTION lists P53004–P28482 MAPK1.
- PMID:25416956 / PMID:29892012 / PMID:31515488 -> UniProtKB:Q8TBB1 (LNX1) — large-scale
  Y2H/interactome maps; UniProt INTERACTION lists P53004–Q8TBB1 LNX1 (NbExp=5).
  These interactome papers do not discuss BLVRA specifically in the cached text; they are
  high-throughput screens. Kept as over-annotated bare protein binding.

## Disease
- Hyperbiliverdinemia (HBLVD, MIM:614156) / "green jaundice": "It is due to increased
  biliverdin resulting from inefficient conversion to bilirubin. Affected individuals
  appear to have symptoms only in the context of obstructive cholestasis and/or liver
  failure" [file:human/BLVRA/BLVRA-uniprot.txt DISEASE, ECO:0000269 PubMed:19580635].

## Family
- Gfo/Idh/MocA family, Biliverdin reductase subfamily; NAD(P)-binding Rossmann-fold + C-terminal
  cat domain [file:human/BLVRA/BLVRA-uniprot.txt SIMILARITY]. PANTHER PTHR43377 BILIVERDIN REDUCTASE A.

## Annotation-review summary
- Core MF: GO:0004074 biliverdin reductase [NAD(P)H] activity (ACCEPT experimental IDA;
  the NADH- and NADPH-specific children GO:0106276/GO:0106277 are also experimentally
  supported and ACCEPTed as they capture the dual-cofactor specificity).
- Core BP: GO:0042167 heme catabolic process (ACCEPT IDA).
- Second core MF (moonlighting): GO:0004674 protein serine/threonine kinase activity
  (from PMID:18463290; not in GOA, added as core_function).
- Cytosol IDA (GO:0005829) ACCEPT; cytoplasm IEA / cytosol IEA/TAS ACCEPT or non-core.
- nucleotide binding (GO:0000166), zinc ion binding (GO:0008270): IEA cofactor/ligand-binding,
  KEEP_AS_NON_CORE (real but sub-functional / part of the catalytic mechanism).
- extracellular exosome (GO:0070062, HDA x2): KEEP_AS_NON_CORE (HTP cargo, not functional site).
- protein binding IPI x4 (GO:0005515): MARK_AS_OVER_ANNOTATED (bare protein binding).
- IEA biliverdin reductase duplicates (IBA/IEA of GO:0004074, GO:0106276, GO:0106277):
  ACCEPT / KEEP as they agree with the experimental evidence.


## Independent whole-review audit, 2026-10-01 UTC

All 32 original annotations were reassessed against the 32-row normal GOA source. The source objects and absent alternative-product slot are preserved. Earlier notes mention two cores, but the actual input YAML contains one; this proposal retains one biochemical core. The historical biochemical enzyme forms are not silently converted into modern alternative products.

The human liver and recombinant-enzyme papers support the core reductase, cofactor reactions and cytosolic compartment. Substrate preference replaces the older categorical exclusivity claim: PMID10858451 reports poor activity with other tested synthetic configurations. Human BLVRA itself catalyzes a step of heme breakdown, supporting its existing process annotation. Zinc binding is retained without using a structure’s missing metal to dismiss direct biochemistry. The PAINT PTHR43377 row confirms the legitimate IBD PTN008681150, including human experimental grounding; no circularity is inferred from the target appearing among seeds.

The four generic-binding MOA decisions are replaced by specific binding-class proposals: MAPK binding for MAPK1 and ubiquitin-protein-ligase binding for LNX1. The [GO:0051019](https://amigo.geneontology.org/amigo/term/GO:0051019) and [GO:0031625](https://amigo.geneontology.org/amigo/term/GO:0031625) definitions were checked. The latter requires binding an E3 protein, not a demonstrated effect on ubiquitination. GOA WITH/FROM supplies the partners missing from the historical YAML source projection; those YAML source objects are deliberately preserved. The normal BLVRA and LNX1 UniProt records corroborate their association. LNX1 alternative isoforms and specific screen constructs were not reconstructed; no domain, variant effect or regulatory mechanism is assigned.

PMID18463290 selected [primary Results](https://pmc.ncbi.nlm.nih.gov/articles/PMC2383961/) support MAPK interaction, including kinase-deficient-protein experiments. This is not evidence that BLVRA phosphorylates ERK or MEK. Broad insulin/PKC/PI3K kinase claims have therefore been removed from the standalone summary pending source-specific assessment. No kinase core or NEW annotation is introduced.

Reading covered all ten complete normal PMID abstracts, the complete Reactome summary, normal UniProt function/location/interaction and relevant identity/cofactor fields, and the complete available partial bodies for PMID18463290, PMID25416956 and PMID29892012. The first contains Abstract/Discussion and the latter two contain Abstract/Introduction/Discussion; their full_text_available flags are not changed and do not imply complete extraction. Selected indexed Results and Figure 1–3 legends supplement PMID18463290; no images or full Methods were read. For PMID31515488 only the abstract and selected study-wide Y2H/retest Results were read, not the entire long XML-derived body or pair-level supplements. Curator-supported exosome detections remain non-core; no claim of extracellular catalytic activity or of its impossibility is made from proteomic detection. The saved Reactome summary does not itself state location, so the cytosolic TAS is corroborated by human purification studies. Primary GOA HPA image data were not inspected.

One normal Falcon research command with the configured perplexity-lite fallback was attempted using the writable task UV directories. Both launches failed to resolve deep-research-client[cyberian]==0.2.7rc1 before provider research began (actual cb9e1b); no provider-named output exists and no retry was made. This audit is manual, not a fabricated provider report.

The proposal has 23 ACCEPT, five KEEP_AS_NON_CORE and four MODIFY; no REMOVE, MOA, UNDECIDED or NEW. The retained detections and curated interaction pairs are not rejected merely because pair-level tables were not reconstituted. Their precise verification limits are recorded. All reference identities/titles and 32 source objects remain unchanged. Short cached anchors total at most 20 words per cited source; this is the assistant quotation boundary, not a repository validator rule. Independent ROOT annotation-reviewer consultation and full science peer remain pending. Canonical application, rendering and history have not been performed by this preparation.


2026-10-01 — Independent annotation consultation and whole-science peer passed. The exact proposal was applied, canonical validation passed without advisories, rendering passed, and the new history record validated. All 32 original source assertions and 15 protected source files are unchanged. An initial application-helper syntax error stopped before application, and its premature validation command had no output directory; both were preserved and corrected before the successful checks. The one core function and four binding refinements are now in the canonical review.


## BLVRA evidence and description follow-up, 2026-10-01 UTC

The biochemical summary now gives EC 1.3.1.24 and explains BLVRA's IX-alpha preference relative to BLVRB's IX-beta activity. Preference is not absolute specificity: PMID10858451 reports low activity with other synthetic configurations. PMID8631357 quantifies approximately one zinc per molecule for purified human liver enzyme and separately demonstrates zinc binding in recombinant human protein. The abstract does not quantify a second recombinant stoichiometry. The signaling sentence is explicitly limited to reported human-cell experiments; no kinase or signaling core is added.

The disease association is restored with its biological context. The normal BLVRA UniProt DISEASE record describes hyperbiliverdinemia in cholestasis or liver failure. The complete official indexed [PMID19580635 abstract](https://pubmed.ncbi.nlm.nih.gov/19580635/) was additionally checked: the reported stop-variant carrier had decompensated cirrhosis, while two heterozygous children without liver disease had normal biliverdin. This supports a conditional contribution to green jaundice, not a claim of fully penetrant disease in every carrier. No local cache for that additional paper was created and it is not added to the formal reference list.

The three LNX1 rows change from MODIFY to UNDECIDED. Existing positive IPI assertions and reciprocal BLVRA/LNX1 UniProt records document the gene-level association, which is retained as evidence, but they do not resolve the screened partner construct. [GO:0031625](https://amigo.geneontology.org/amigo/term/GO:0031625) specifies binding an E3 protein; it does not require modulation of ubiquitination. Each row now has exact file-backed pair evidence and canonical partner-class context. The published-head proof shows that genes/human/LNX1/LNX1-uniprot.txt was already in the checkout as an unchanged main reuse (blob c9f9d4cdacc9820e1306562fb0a7e0cf56222b57). Its absence from the PR's changed-file list is not absence from the repository.

The normal source fields still identify the same pair, and its three related screen rows are not three independent physiological confirmations. Paper-specific clone data remain uninspected. LNX1 isoform 2 replaces residues 1–127, including the annotated RING region at 41–79, so no inference about the tested isoform's catalytic competence or the binding interface is made. This isoform ambiguity is material: the gene-level E3 name alone cannot establish that the assayed construct retained that class-defining region. The previously proposed GO:0031625 replacement is therefore withdrawn pending construct-specific evidence, without asserting a false interaction or ubiquitination mechanism. Reference relevance remains MEDIUM because these are the curator's association sources; relevance and completeness of independent verification are separate judgments. Exosome detections were not reassessed in this follow-up.

Disconnected biochemical snippets are replaced by informative source excerpts, including a full reaction-and-compartment sentence in the reductase core. Shared excerpts occur once per biochemical source claim rather than being duplicated across related annotations. Source-specific explanations remain attached to every annotation. Quotation accounting is an assistant constraint, not a repository validation rule; the new ledger is bounded at 25 words per source. This does not require discarding a supported biological claim or inventing text where the pair-level paper table has not been read.

Follow-up reading comprises the complete cached abstracts of PMID7929092, PMID8424666, PMID8631357, PMID10858451, PMID18463290, PMID25416956, PMID29892012 and PMID31515488; the complete available partial bodies for PMID18463290, PMID25416956 and PMID29892012; relevant BLVRA and LNX1 UniProt function, interaction, cofactor, disease and alternative-sequence fields; actual GOA partner fields; and the official GO binding definition. The last interactome paper's full body was not reread, and no paper-specific clone tables, images or supplements were inspected. The earlier provider-startup failure remains the recorded research outcome; no new provider or normal source-fetch attempt was needed. All 32 original source objects, 32 raw rows, reference identities and absent product slots are preserved, with 23 ACCEPT, five KEEP_AS_NON_CORE, one MODIFY, three UNDECIDED and one unchanged biochemical core. The independent follow-up science peer and canonical application are pending.

The initially sealed follow-up V1 retained three binding-class MODIFY decisions. Further explicit assessment of the already-read LNX1 alternative-sequence evidence showed that its gene-level caveat did not resolve which enzyme-class construct was tested. V1 is preserved intact in TMP; V2 makes only this three-row decision correction and matching explanatory changes. No new source retrieval or negative interaction inference was used.


## Follow-up verification

Independent scientific review approved this follow-up, including the material LNX1 construct uncertainty. The exact reviewed proposal was applied, canonical validation passed, the rendered HTML reproduces the review YAML, and the new history record validated. All original source assertions, source files and earlier history remain unchanged. Three LNX1 source assertions remain UNDECIDED; no new annotation or kinase/signaling core was added.


## Concise evidence excerpts, second follow-up, 2026-10-01 UTC

Eight additional exact excerpts improve the evidence displayed beside existing decisions. The urinary- and B-cell-exosome abstracts now identify the preparations and proteomic analyses behind the two retained HDA associations (PMID19056867 and PMID20458337). Neither excerpt identifies BLVRA itself; the existing reasons continue to defer to curator-reported detections and explicitly retain the uninspected peptide/table limitation. PMID19056867 repeats its abstract under a Full Text heading but remains an abstract-only extraction.

The Reactome TAS row now includes its biliverdin-reduction statement. This supports the named reaction, while its existing reason still distinguishes the summary from direct cytosolic-location evidence. UniProt location excerpts are restored to the three relevant broad/mapped/immunofluorescence location rows; the HPA image remains uninspected. A short dual-reactant statement supports the existing NADH electronic reaction without replacing the independent biochemical evidence.

The reductase core gains an exact phrase identifying human IX-alpha-reductase initial-rate kinetics from PMID10858451. This is assay context, not a newly inspected NADH- or NADPH-specific protocol. Accordingly, the two cofactor EXP rows and heme-catabolism row are not supplied with an unrelated abstract phrase merely to increase quote counts. Their original explanations and corroborating primary references remain intact. The three LNX1 pair/class excerpts also remain unchanged; no screened isoform or physiological interaction is newly verified.

All 16 existing excerpts are retained and eight are added, for 24 total. Aggregate quoted words in the candidate YAML remain at most 25 per source. This is an assistant quotation limit, not a repository validation rule; the external request to drop it is not followed. The update improves source-specific context rather than restoring repeated passages for every row. This appendix introduces no additional quoted source text.

For this focused update, the three complete cached abstracts of PMID19056867, PMID20458337 and PMID10858451, the complete normal Reactome reaction summary, and the relevant normal BLVRA UniProt function, cofactor and location fields were read. Existing quote strings across all sources were checked as exact cached substrings. No complete publication, figure image, supplement, BLVRA peptide entry or HPA image was newly inspected, and no source fetch was made. All 32 source objects and annotation decisions, the description, reference objects, one core's biological assignments and absent product slots are preserved. Distinct science peer remains pending; no canonical application, validation, rendering or history creation is claimed by this proposal.


## Evidence-excerpt follow-up verification

Independent scientific review approved the eight added exact excerpts and their stated limits. Canonical validation and history validation passed, and the rendered HTML reproduces the reviewed YAML. All 32 annotation decisions and source assertions, the description, reference objects and sole reductase core assignments remain unchanged. No source cache or prior history record was edited.
