# AGPAT2 (LPAAT-beta) review notes

> The initial notes below record the previous review. Their action judgments are
> superseded by the 2026-09-27 audit appended at the end, including the earlier
> broad-term, cytokine, rat-transfer and neutrophil-location exclusions.

UniProt: O15120 (PLCB_HUMAN, "1-acyl-sn-glycerol-3-phosphate acyltransferase beta"),
gene symbol AGPAT2, HGNC:325, human (NCBITaxon:9606), 278 aa precursor.

## Core biology

AGPAT2 (also LPAAT-beta, 1-AGPAT 2) is an endoplasmic-reticulum multi-pass membrane
enzyme that catalyzes the second committed step of the glycerol-phosphate pathway of
glycerolipid biosynthesis: acylation of the sn-2 position of 1-acyl-sn-glycerol-3-phosphate
(lysophosphatidic acid, LPA) using a long-chain acyl-CoA to give 1,2-diacyl-sn-glycerol-3-phosphate
(phosphatidic acid, PA) plus CoA (EC 2.3.1.51).

- FUNCTION (UniProt): "Converts 1-acyl-sn-glycerol-3-phosphate (lysophosphatidic acid or LPA) into 1,2-diacyl-sn-glycerol-3-phosphate (phosphatidic acid or PA) by incorporating an acyl moiety at the sn-2 position of the glycerol backbone." [file:human/AGPAT2/AGPAT2-uniprot.txt]
- CATALYTIC ACTIVITY (UniProt, RHEA:19709, EC 2.3.1.51): "a 1-acyl-sn-glycero-3-phosphate + an acyl-CoA = a 1,2-diacyl-sn-glycero-3-phosphate + CoA". Evidence ECO:0000269 from PubMed:15629135, 19075029, 21873652, 9242711. [file:human/AGPAT2/AGPAT2-uniprot.txt]
- PATHWAY (UniProt): "Phospholipid metabolism; CDP-diacylglycerol biosynthesis; CDP-diacylglycerol from sn-glycerol 3-phosphate: step 2/3." PA is also the branch-point precursor for CDP-DAG, phospholipids (via de novo route), and diacylglycerol/triacylglycerol. [file:human/AGPAT2/AGPAT2-uniprot.txt]
- SUBCELLULAR LOCATION (UniProt): "Endoplasmic reticulum membrane {ECO:0000269|PubMed:21873652}; Multi-pass membrane protein". Two TRANSMEM helices (30-50, 122-142). [file:human/AGPAT2/AGPAT2-uniprot.txt]
- TISSUE SPECIFICITY (UniProt): "Expressed predominantly in adipose tissue, pancreas and liver." (major adipose LPAAT isoform). [file:human/AGPAT2/AGPAT2-uniprot.txt]
- Family (UniProt SIMILARITY): "Belongs to the 1-acyl-sn-glycerol-3-phosphate acyltransferase family." HXXXXD (98-103) catalytic motif and EGTR motif (172-175). [file:human/AGPAT2/AGPAT2-uniprot.txt]

## Disease

Biallelic loss-of-function AGPAT2 mutations cause congenital generalized lipodystrophy type 1
(CGL1 / Berardinelli-Seip), MIM:608594: "A form of congenital generalized lipodystrophy...
near complete absence of adipose tissue, extreme insulin resistance, hypertriglyceridemia,
hepatic steatosis and early onset of diabetes. Inheritance is autosomal recessive."
[file:human/AGPAT2/AGPAT2-uniprot.txt]. Disease gene established in PMID:11967537 (Agarwal et al.
Nat Genet 2002); CGL mutants have reduced enzyme activity (PMID:15629135).

## Key experimental evidence for catalytic activity / localization

- PMID:9242711 (Eberhardt et al., JBC 1997): cloning of human LPAAT; "Recombinant protein produced in COS 7 cells exhibited LPAAT activity with a preference for LPA as the acceptor phosphoglycerol and arachidonyl coenzyme A as the acyl donor." [PMID:9242711]. (This paper's expression-highest-in-liver-and-pancreas Northern is the historical basis; UniProt later says predominant in adipose/pancreas/liver.)
- PMID:9212163 (West et al., DNA Cell Biol 1997): cloned two human LPAAT cDNAs (LPAAT-alpha, LPAAT-beta = AGPAT2); "Expression of these two cDNAs in an Escherichia coli strain with a mutated LPAAT gene (plsC) complements its growth defect and shifts the equilibrium of cellular lipid content from LPA to PA". Also reports that overexpression correlated with enhanced TNF-alpha/IL-6 upon IL-1beta stimulation: "This increase in LPAAT activity correlates with enhancement of transcription and synthesis of tumor necrosis factor-alpha and interleukin-6 from cells upon stimulation with interleukin-1beta, suggesting LPAAT overexpression may amplify cellular signaling responses from cytokines." [PMID:9212163]. NOTE: this cytokine link is an overexpression correlation (indirect, speculative) -> basis for the BHF-UCL positive-regulation-of-cytokine annotations, which are over-annotations of a lipid enzyme.
- PMID:15629135 (Haque et al., BBRC 2005): CGL mutant enzymology; "The AGPATs catalyze acylation of lysophosphatidic acid (LPA) to phosphatidic acid (PA) during the biosynthesis of glycerophospholipids and triglycerides from glycerol-3-phosphate." Measured "conversion of [(3)H]LPA to [(3)H]PA in the presence of oleoyl-coenzyme A"; CGL mutants (G136R, 140delF, L228P) retained 15-40% activity, A239V ~90%. [PMID:15629135].
- PMID:19075029 (Zhao et al., JLR 2009): ALCAT1-focused study; abstract does not describe AGPAT2 assays explicitly (title/abstract about ALCAT1). GOA has AGPAT2 IDA GO:0003841 from this paper (curator read full text). Abstract-only cache -> cannot verify the AGPAT2-specific assay; ACCEPT (defer to curator, function is correct core MF).
- PMID:21873652 (Agarwal et al., JBC 2011): biochemical characterization of human AGPAT1/2 + ER localization; "When co-expressed, both isoforms co-localize to the endoplasmic reticulum." [PMID:21873652]. Also KM/Vmax kinetics in UniProt BIOPHYSICOCHEMICAL PROPERTIES. EXP source for GO:0005789 ER membrane and IDA GO:0003841.
- PMID:9461603 (Aguado & Campbell, JBC 1998): characterizes hLPAATalpha (the MHC class-III / chromosome 6 paralog AGPAT1, "G15"), NOT AGPAT2. "The amino acid sequence of the MHC-encoded human LPAAT (hLPAATalpha) is 48% identical to the recently described hLPAAT". GOA uses this as NAS for AGPAT2 MF/phospholipid-metabolism (family-level assertion). Correctly cited paper but describes the paralog -> keep NAS but note relevance; MF is correct at family level.

## Annotation review summary

Core, well-supported:
- GO:0003841 1-acylglycerol-3-phosphate O-acyltransferase activity (MF) - multiple IDA/IMP/IBA/IEA/TAS/NAS; ACCEPT experimental ones, ACCEPT redundant IEA/IBA (own core function).
- GO:0006654 phosphatidic acid biosynthetic process (BP) - IBA/IGI/TAS; ACCEPT.
- GO:0005789 endoplasmic reticulum membrane (CC) - EXP PMID:21873652 + TAS/IEA; ACCEPT. GO:0005783 ER (parent) IDA/IBA/ISS/IEA - ACCEPT/KEEP_AS_NON_CORE (membrane is more precise).
- GO:0016024 CDP-diacylglycerol biosynthetic process (BP) - IEA UniPathway; matches UniProt PATHWAY; KEEP_AS_NON_CORE (downstream branch role).
- GO:0008654 phospholipid biosynthetic process (BP) IEA InterPro; GO:0006644 phospholipid metabolic process NAS - correct but general parents; KEEP_AS_NON_CORE.
- GO:0016746 acyltransferase activity IEA InterPro - correct general parent of core MF; KEEP_AS_NON_CORE.
- GO:0016020 membrane IEA InterPro - correct general parent of ER membrane; KEEP_AS_NON_CORE.

Over-annotations / mislocalizations:
- GO:0001819 positive regulation of cytokine production (IMP PMID:9212163) - MARK_AS_OVER_ANNOTATED (experimental, keep; indirect overexpression correlation, not core lipid function).
- GO:0001961 positive regulation of cytokine-mediated signaling pathway (IC PMID:9212163) - MARK_AS_OVER_ANNOTATED (same basis).
- GO:0008544 epidermis development (IEA Ensembl, from rat ortholog) - MARK_AS_OVER_ANNOTATED (not a core AGPAT2 function; ortholog-transfer).
- GO:0009410 response to xenobiotic stimulus (IEA Ensembl, from rat ortholog) - MARK_AS_OVER_ANNOTATED.
- GO:0005886 plasma membrane (TAS Reactome R-HSA-6799350) - MARK_AS_OVER_ANNOTATED (neutrophil-degranulation pathway propagation; enzyme is ER).
- GO:0035579 specific granule membrane (TAS Reactome R-HSA-6799350) - MARK_AS_OVER_ANNOTATED (same neutrophil-degranulation propagation).

## Core functions selected
- MF: GO:0003841 1-acylglycerol-3-phosphate O-acyltransferase activity
- BP: GO:0006654 phosphatidic acid biosynthetic process
- CC (location): GO:0005789 endoplasmic reticulum membrane

## 2026-09-27 source-based audit

### Scope and provenance

Read all 31 seeded annotations, the catalytic core, all 16 original references,
the immutable UniProt record, and the prior notes. There were no prior NEW rows.
All 31 source assertions (term, evidence, original reference and qualifiers) and
the original reference id/title pairs are retained. All original publication
caches are abstract-only; external full-text access is recorded separately, and
`full_text_unavailable: true` remains on those reference records.

Official identity: [NCBI Gene 10555](https://www.ncbi.nlm.nih.gov/gene/10555)
identifies AGPAT2, HGNC:325, human UniProt O15120; aliases include BSCL, BSCL1,
LPAAB, LPLAT2, 1-AGPAT2 and LPAAT-beta. Existing isoform records are preserved.
GitHub main file-content checks matched all five local gene files before edits.
The baseline review blob was `20546de7ab0d9fa509590ad2ec13436ca9862743`.
Separate open-PR searches for AGPAT2, LPAAT-beta and the remaining aliases found
no overlapping review. Main at initial assignment was
`795b693f5711c625401d03a755fe937260ae0ac0`; the coordinator subsequently checked
that the advance to `43b6ab10e9d8bc6bf4efb696a3f8ab672a443bfe` had no human-gene
changes. No source refresh or Git mutation was performed in this audit.

The genuine default Falcon invocation used the supported temporary UV tool/bin/
cache directories, a 1200-second timeout and perplexity-lite fallback, concurrent
with normal GOA-publication caching. Both providers failed before research began
because dependency retrieval from PyPI failed DNS. No report was generated or
manually fabricated. All six original publications were already cached. Manual
primary-source research followed; access failures below remain explicit.

### Catalysis, localization and assay scope

- **PMID:21873652**, [full primary PMC3199511](https://pmc.ncbi.nlm.nih.gov/articles/PMC3199511/):
  read Methods, localization Results/Figures 2-4, activity Figure 5 and substrate
  specificity. Human AGPAT2-EGFP co-localizes with ER markers in CHO cells and
  primary mouse hepatocytes; the recombinant protein is human despite the host
  species. Microsomal activity and labeled LPA-to-PA assays support the ER
  membrane catalytic core. The oleoyl-LPA/oleoyl-CoA preference is assay-specific.
  The original organelle-level ER rows remain ACCEPT, preserving their evidence
  resolution rather than demoting them because a membrane term is also present.
- **PMID:19075029**, [full primary PMC2666181](https://pmc.ncbi.nlm.nih.gov/articles/PMC2666181/):
  Methods identify purchased human AGPAT2 cDNA TC116102 and HEK293 membrane
  assays with labeled acyl-CoA and lysophospholipid substrates. Figure 2A includes
  the AGPAT2 control. This directly recovers the experimental basis hidden by the
  ALCAT1-focused abstract; there is no wrong-gene inference. The IDA stays ACCEPT.
- **PMID:15629135**, [PubMed](https://pubmed.ncbi.nlm.nih.gov/15629135/):
  the local primary abstract describes wild-type/variant activity in CHO lysates
  using labeled LPA and oleoyl-CoA. Several variants retain less than 15% activity,
  three retain 15-40%, and A239V retains about 90%. The description of patient
  variants was corrected to avoid treating them all as nulls. This is supporting
  human enzymology, with no claim that its full article was recovered.
- **PMID:9242711**, local primary abstract and UniProt attribution: recombinant
  human protein in COS7 cells prefers LPA and arachidonyl-CoA in that assay.
  The difference from the later oleoyl-CoA preference is retained as assay scope,
  not erased by asserting a universal exclusive donor. The shared reaction is
  well established.
- **PMID:9212163**, [publisher record](https://journals.sagepub.com/doi/10.1089/dna.1997.16.691):
  the cached abstract explicitly separates cell-free fluorescent-LPA conversion
  from complementation of the bacterial `plsC` defect. The former supports the
  IDA activity row, while the latter supports IGI PA synthesis. Both human cDNAs
  were reported. Direct full-text/PDF retrieval did not recover the cytokine
  experiments; that limitation matters for the two contextual BP claims below.
- **PMID:9461603**, local primary abstract: its emphasis is the MHC-encoded alpha
  paralog, and it compares this with the previously described human LPAAT. The
  exact beta-specific passage remains unavailable. Retain both NAS annotations
  because human AGPAT2 activity independently establishes the MF and phospholipid
  metabolism, without asserting that the full original paper lacks beta data.

The live [GO:0003841 definition](https://amigo.geneontology.org/amigo/term/GO:0003841)
specifies acyl-CoA plus 1-acyl-sn-glycerol-3-phosphate yielding CoA plus
1,2-diacyl-sn-glycerol-3-phosphate. Its ancestry includes GO:0016746. Thus the
generic InterPro acyltransferase row is MODIFY to this demonstrated reaction.
The generic InterPro membrane row is ACCEPT at the resolution of the family
mapping, with the separate ER-membrane rows providing finer detail. The catalytic
refinement does not alter the original source fields.

### CDP-diacylglycerol and phospholipid synthesis

**PMID:34824276**, [PubMed identity](https://pubmed.ncbi.nlm.nih.gov/34824276/)
and [full primary PMC8616899](https://pmc.ncbi.nlm.nih.gov/articles/PMC8616899/):
read Results/Figures 4-7 and the corresponding co-purification, endogenous tagging,
activity and flux Methods. Human AGPAT2 co-purifies with CDS1/2, and endogenous
tagged AGPAT2/CDS2 co-immunoprecipitate. AGPAT2 depletion reduces CDS protein and
activity; its manipulation changes oleate flux toward PI/PG in HeLa cells, with
corroborating mouse-liver evidence. The authors explicitly could not visualize
PA channeling; tracer incorporation can also include deacylation/reacylation.
Those limits prevent claiming a resolved channel or new cytidylyltransferase MF.

The existing UniPathway annotation identifies the LPA-acylation step in the
glycerol-3-phosphate-to-CDP-DAG pathway. AGPAT2 **performs** that chemistry, rather
than merely being a substrate or a necessary upstream signal. The
[GO:0016024 definition and parents](https://amigo.geneontology.org/amigo/term/GO:0016024)
describe the reactions/pathways forming CDP-DAG, under glycerophospholipid
biosynthesis; they do not restrict membership to the final CDS reaction.
Retain this existing BP as ACCEPT and include it with PA biosynthesis in the one
catalytic core. Broad phospholipid biosynthesis/metabolism rows also remain core.

The cached Reactome **R-HSA-1483166** and **R-HSA-75885** were read: the first
places LPA acylation in PA synthesis, and the second explicitly assigns the
AGPAT-catalyzed step to the ER membrane. Their MF/BP/CC assertions are retained.

### PAINT, orthology and GO-CAM

Read `interpro/panther/PTHR10434/PTHR10434-paint.tsv`: PTN000046633 carries the
ER IBD, and PTN000046632 carries the LPA acyltransferase/PA-synthesis IBDs. Only
these ancestral nodes appear in IBA `source_entities`. Human self-evidence is
legitimate descendant evidence for ancestral placement, not circular transfer.

The mouse Q8K3K7 / ENSMUSP00000028286 ER transfers are corroborated by direct
human ER experiments. The rat D4AC45 / ENSRNOP00000026408 donor identity is
explicit in GOA. NCBI rat Gene 311821 independently links that accession to
Agpat2. Attempts to retrieve the comparative annotation graph and QuickGO donor
API did not resolve the exact current rat term/reference links.

- **PMID:16150824**, [PubMed](https://pubmed.ncbi.nlm.nih.gov/16150824/)
  and [indexed full JLR primary article](https://www.jlr.org/article/S0022-2275%2820%2932883-2/fulltext):
  Results/Figures 3-4 report fetal-rat epidermal Agpat2/5 transcript changes and
  total AGPAT activity during barrier formation. The activity is measured across
  isoforms. This is relevant evidence, but it does not by itself establish the
  exact donor annotation or conserved human AGPAT2 developmental participation.
  The transferred epidermis-development row is UNDECIDED, not rejected as
  biologically impossible for a biosynthetic enzyme.
- **PMID:19346281**, [PubMed](https://pubmed.ncbi.nlm.nih.gov/19346281/)
  and [author-uploaded primary table indexed at ResearchGate](https://www.researchgate.net/publication/24257630_Proteomic_analysis_of_rat_hippocampus_exposed_to_the_antidepressant_paroxetine):
  the rat hippocampal study used 12-day paroxetine treatment and reports a
  decreased AGPAT2-predicted protein spot. This is a plausible source context,
  not a verified exact annotation chain or a human experiment. The live
  [GO:0009410 definition](https://amigo.geneontology.org/amigo/term/GO:0009410)
  includes gene-expression/enzyme-production changes after xenobiotic exposure,
  so the earlier suggestion that it requires detoxification is not used.
  The human transfer remains UNDECIDED.

Read the actual Agpat2 activity nodes in cached GO-CAMs
`63a86a8600001386/63a86a8600001927` and
`6446bfcb00000006/6446bfcb00000019`. Both place mouse Agpat2 LPA acyltransferase
at the ER membrane in triglyceride synthesis, with explicit downstream activity
edges. No human O15120 activity was found in the local index. These models support
the biochemical role and distinguish precursor-making enzymes from downstream
enzymes; they are not used to manufacture an additional human NEW process row.
This audit adds no NEW annotations or generic interaction terms.

### Cytokine and neutrophil-location uncertainties

The local abstract of PMID:9212163 positively reports enhanced TNF-alpha/IL-6
transcription and synthesis following LPAAT overexpression and IL-1beta
stimulation. The literal definitions of
[GO:0001819](https://amigo.geneontology.org/amigo/term/GO:0001819) and
[GO:0001961](https://www.zfin.org/action/ontology/term-detail-popup?termID=GO%3A0001961)
cover increased cytokine production and increased cytokine-mediated signaling,
respectively. Neither requires the annotated product to be a cytokine receptor.
The full beta-versus-alpha experiment and controls were not recovered. Both rows
are UNDECIDED; the earlier assertion that being a lipid enzyme or being tested by
overexpression makes these annotations excessive is withdrawn.

The live [Reactome R-HSA-6799350 event](https://reactome.org/content/detail/R-HSA-6799350)
explicitly includes AGPAT2 in the
[specific-granule membrane input set](https://reactome.org/content/detail/R-HSA-6799368)
and [plasma-membrane output set](https://reactome.org/content/detail/R-HSA-6806323).
The [AGPAT2 granule entity](https://reactome.org/content/detail/R-HSA-6799353)
is not an inferred identity guess. The primary reference is **PMID:23650620**,
the human neutrophil fraction-proteomics study. Its local abstract and Reactome
link establish the context, but the AGPAT2-specific supplemental assignment and
independent localization confirmation were not recovered. Both locations remain
UNDECIDED. ER localization in other cell types does not refute an additional
neutrophil pool, and no contamination claim is made. The event reference is no
longer marked MISCITED.

### Disease context, current decisions and remaining gates

**PMID:11967537**, [official primary PubMed abstract](https://pubmed.ncbi.nlm.nih.gov/11967537/),
verifies the foundational AGPAT2 association with autosomal-recessive congenital
generalized lipodystrophy. This supports the biological description and disease
context, not a new developmental-process annotation based on necessity alone.

All 31 rows are adjudicated: **24 ACCEPT, 1 MODIFY, 6 UNDECIDED; no NEW**.
The single catalytic core covers LPA acylation at the ER membrane in PA and
CDP-diacylglycerol biosynthesis. All 23 references have manual assessments.

Normal `fetch-pmid` attempts for **11967537, 34824276, 16150824, 19346281 and
41387688** each failed DNS. These five required publication caches remain absent even though
primary web evidence was inspected. The draft must remain explicitly gated on
normal cache recovery; no citation was dropped to conceal that gate and no cache
was hand-written. All original PMID and Reactome caches remain unmodified.

### Newer primary evidence: PA supply and ER tubulation

**PMID:41387688**, [official PubMed](https://pubmed.ncbi.nlm.nih.gov/41387688/)
and [full primary Nature Communications article](https://www.nature.com/articles/s41467-025-66474-5)
([PMC12749901](https://pmc.ncbi.nlm.nih.gov/articles/PMC12749901/)), verified as
*AGPAT2 acts at the crossroads of lipid biosynthesis and DRP1-mediated ER
morphogenesis*. Read Results/Figures 1, 7-8, Discussion and relevant Methods.
Human U2OS knockdown alters ER morphology; endogenous AGPAT2/DRP1 co-IP is
reported in human HEK293T cells. Mouse-MEF knockout/rescue, catalytic mutants and
isolated-ER lipid assays connect AGPAT2 catalysis to tubulation. DRP1 still
associates with the ER without AGPAT2. AGPAT2 supplies PA to the proposed
DRP1/PA membrane-shaping mechanism; these experiments do not give AGPAT2 an
autonomous membrane-remodeling or GTPase MF. Add a bounded cell-model summary
sentence and a question about PA partitioning in human adipocytes, without a NEW
process assertion or an additional core activity. The normal machine cache fetch
for this newly cited paper failed DNS; it is included among the five draft cache
gates above. The external primary read does not create a local full-text cache.

Final checks: `just validate human AGPAT2` passed with one grouped warning for
the five missing PMID caches listed above; authored ontology terms passed with
`--terms --no-references`. All 31 source records, 16 original reference identities,
isoforms and immutable UniProt/GOA files were preserved. Cached supporting-text
checks found no remaining mismatch after selecting an exact contiguous UniProt
pathway fragment. History validation and HTML rendering passed. Trailing YAML
spaces were stripped with parsed-YAML equality asserted. Coordinator independent
review confirmed the biological judgments and the recovered human activity and
CDS-complex sources; its request to retain the broad membrane annotation was
incorporated. No Git, publication or shared-project changes were made.

### 2026-09-27: align review status with remaining validation warnings

Set `status: DRAFT` after checking `GeneReviewStatusEnum`: `COMPLETE` requires
no validation warnings, whereas `DRAFT` permits a fully adjudicated review with
warnings. The five missing publication caches recorded above remain unresolved.
All 31 annotation judgments, source assertions, reference identities and the
single catalytic core are unchanged. This corrects the status label without
claiming that the missing source material has been recovered.


## 2026-09-27: PR 3208 quotation and source-access follow-up

Confirmed canonical files match published head `be63dced1ece9f5f5f2e06a97abf7496f1b12bfc` before editing. All 31 source assertions and 23 reference identities remain unchanged. Actions remain **24 ACCEPT, 1 MODIFY, 6 UNDECIDED**; one integrated core and no NEW.

The reviewer correctly identified a paraphrase presented as a quotation for **PMID:34824276**. Reopened the [official PubMed abstract](https://pubmed.ncbi.nlm.nih.gov/34824276/) and [primary Nature Communications article](https://www.nature.com/articles/s41467-021-27279-4). Two annotation supports and the core now use exact short abstract fragments in ordinary `supporting_text`, not the fulltext exception. These passages describe AGPAT2/CDS interaction and PA metabolism along the CDP-DAG branch. The article is open access; normal-cache recovery remains a DRAFT gate. The reference finding retains the measured complex/flux result and separates it from proposed direct substrate channeling.

For **PMID:19075029**, the original [PMC2666181 article](https://pmc.ncbi.nlm.nih.gov/articles/PMC2666181/) was recovered by indexed query `"PMC2666181" "TC116102"`. Methods subsection *In vitro acyltransferase activity assays* contains the existing HEK293/transfected-construct quotation verbatim. Human AGPAT2 cDNA is TC116102 in *Plasmid construction*; Figure2 documents separate substrate assays. The fragment is Methods text, not a reconstructed caption. Local cache remains abstract-only.

The [primary Nature Communications paper for PMID:41387688](https://www.nature.com/articles/s41467-025-66474-5) was reopened, including Results/Figures1,8,9. It reports human U2OS knockdown and HEK293T interaction assays alongside mouse-MEF experiments. The mechanism remains PA production by AGPAT2 and PA-dependent DRP1 action; no autonomous AGPAT2 membrane-sculpting or GTPase function is added. Indexed [official PubMed](https://pubmed.ncbi.nlm.nih.gov/41387688/) confirms PMID, title, DOI and PMC12749901. Corrected the journal name to Nature Communications.

VERIFIED is retained for those checked primary sources and [11967537](https://pubmed.ncbi.nlm.nih.gov/11967537/), [16150824](https://pubmed.ncbi.nlm.nih.gov/16150824/) and [19346281](https://pubmed.ncbi.nlm.nih.gov/19346281/). This denotes identity and bounded content checked independently, not successful cache retrieval or proof that every human GO annotation is supported.

The broad membrane and phospholipid biosynthesis/metabolism assertions describe source-supported location or direct PA-producing chemistry. Core membership does not require the same broad term to be duplicated in a separate core entry. The specific acyltransferase MF refinement remains. Core prose now includes the DAG/TAG branch, consistent with cached human catalytic evidence, UniProt and previously inspected mouse GO-CAM activities. Downstream PA phosphatases, CDS and DGAT enzymes retain their own chemistry; no additional NEW human process is inferred from adjacency.

Rat Ensembl Compara rows remain UNDECIDED because exact donor-reference linkage and human conservation are unresolved, not because experimental-curator protection applies to IEA. Rechecked [original JLR fetal-skin Results/Figures3-4](https://www.jlr.org/article/S0022-2275%2820%2932883-2/fulltext): Agpat2 transcript changes are distinguished from total multi-isoform activity. The [live GO:0009410 definition](https://amigo.geneontology.org/amigo/term/GO:0009410) includes enzyme-production/expression changes, so the paroxetine-associated spot does not imply a nonexistent detoxification activity. Plausible but unresolved donor context does not establish a demonstrably excessive human transfer.

Cached Reactome6799350 lacks the AGPAT2 participant list. Prior positive identity verification used live sets and the AGPAT2 entity documented above; this distinction is now explicit. Both neutrophil-specific locations remain UNDECIDED while primary AGPAT2 supplementary assignments are unresolved.

All five required missing normal caches remain gates: **11967537,16150824,19346281,34824276,41387688**. No reference or note citation was removed to evade the requirement. Status stays DRAFT. No source cache, provider output, published history, Git state or shared project file was manually altered.

Follow-up normal `fetch-pmid` attempt completed: **Cached 0/5**, with DNS resolution errors for every requested PMID. No publication file was generated. The execution log is `/tmp/AGPAT2-followup-fetch.log`.


## 2026-09-27 normal publication-cache recovery

All five required records are now locally available from standard fetch output:
PMID:11967537, PMID:16150824 and PMID:19346281 are abstract-only;
PMID:34824276 and PMID:41387688 include XML full text. The latter two
`full_text_unavailable` flags are now false. Previously verified external
source readings remain distinct from the newly recovered local records.

The recovered primary abstracts agree with the established pedigree,
epidermal-expression and rat-paroxetine scopes. Relevant cached Results,
Methods and Figures 4-7 of PMID:34824276 support human AGPAT2/CDS complex
formation and altered lipid flux, while leaving direct substrate channeling
as a model. PMID:41387688 Results and Figures 1, 6, 8 and 9 retain the
distinction between human-cell perturbation/interaction experiments and
mouse-MEF rescue or isolated-ER reconstitution. AGPAT2 produces PA; these
experiments do not assign it autonomous DRP1-like membrane shaping. No
annotation action, source assertion, core or biological summary changes follow.
The two rat contextual transfers and the neutrophil locations remain unresolved
for the documented source-specific reasons.

Records were imported verbatim from Actions run 36286975328, head
5946477c8ac79ade0709264c775ea1262b108438, artifact 10920674630. The
transported ZIP SHA-256 is
`c0ffe4a66b80278af34b44aab6a3ae354ffd5699236b3a486ca95527be5e9713`;
`tmp/verified-reference-records/local-import-receipt.json` records the
per-file hashes. The publication manifest includes only these five required
records, without altering their machine-fetched titles or content.

All 31 source assertions and reviews, the integrated core, 23 reference
identifiers/titles, immutable gene files and prior history are preserved. This
entry supersedes the missing-cache status in earlier dated notes. Targeted
validation, rendering and fresh history validation are recorded in the closure
manifest; COMPLETE is used only with zero gene validation warnings.
