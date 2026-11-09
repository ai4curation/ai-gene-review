# GBA1 review notes

## Review context

GBA1 is in the proteostasis network under lysosomal lipid catabolism and a no-mapping
autophagic lysosome reformation context. The PN ALR row is useful for literature
triage, but the review decisions below are based on GOA, UniProt, cached publications,
and Reactome rather than PN taxonomy alone.

Falcon deep research: `just deep-research-falcon human GBA1` timed out after 600s
with `Provider falcon timed out after 600s`; no Falcon findings were available to
incorporate into this review.

## Core function synthesis

GBA1 encodes lysosomal acid glucosylceramidase. The UniProt record summarizes the
core activity as lysosomal hydrolysis of glucosylceramides to ceramides and glucose,
with a pH optimum in the acidic lysosomal range and activation by saposins A/C
[UniProt:P04062 "Glucosylceramidase that catalyzes, within the lysosomal compartment,
the hydrolysis of glucosylceramides/GlcCers ... into free ceramides ... and glucose"].

The glucosylceramide catabolic role is repeatedly supported by experimental papers:
saposin A/C assays state that glucosylceramide degradation in lysosomes is accomplished
by glucosylceramidase and that saposin C promotes membrane binding of GCase
[PMID:9201993 "The degradation of glucosylceramide in lysosomes is accomplished by
glucosylceramidase"; PMID:9201993 "saposin C is responsible for the membrane binding
of glucosylceramidase"]. Disease-variant and substrate assays also support
glucosylceramidase activity and glucosylceramide catabolism [PMID:16293621
"Analyses of variant acid beta-glucosidases"; PMID:15916907 "Use of fluorescent
substrates for characterization of Gaucher disease mutations"; PMID:24022302
"Functional analysis of 11 novel GBA alleles"].

GBA1 localizes to the lysosomal lumenal side of the lysosomal membrane. LIMP-2/SCARB2
is the trafficking receptor for M6P-independent lysosomal delivery of GCase
[PMID:18022370 "LIMP-2 is a specific binding partner of beta-glucocerebrosidase";
PMID:18022370 "LIMP-2-deficient mouse tissues ... beta-glucocerebrosidase was
secreted"]. The 2025 cryo-TEM structure supports an ER-to-TGN-to-lysosome transport
complex with LIMP-2 and confirms that GCase remains enzymatically active in that
complex [PMID:40159502 "GCase/LIMP-2 transport complex forms within the endoplasmic
reticulum (ER) and travels through the trans-Golgi network to the lysosome";
PMID:40159502 "GCase remained enzymatically active when in complex with LIMP-2"].

## Proteostasis and ALR context

The key proteostasis-relevant paper reports that GCase deficiency compromises
autophagic lysosome reformation (ALR), lysosomal recycling, endosome maturation, and
mTOR reactivation after starvation/refeeding [PMID:27378698 "autophagy lysosomal
reformation (ALR) is compromised in cells lacking functional GCase"; PMID:27378698
"GCase deficiency affects lysosomal recycling"; PMID:27378698 "Loss of lysosomal
GCase causes impairment of ALR and maturation of endosomes"]. This supports keeping
lysosome organization as a real GBA1 process annotation, but it does not make
generic autophagy or all protein catabolic process terms core molecular functions.

Alpha-synuclein/GCase papers support non-core disease and lysosomal protein-catabolism
contexts. GCase depletion can reduce lysosomal proteolysis affecting alpha-synuclein
and establish a bidirectional pathogenic loop [PMID:21700325 "GCase depletion causes
a decline in lysosomal proteolysis that preferentially affects alpha-syn"], while a
contrasting neuronal-cell study found that strong GCase inhibition was not sufficient
to raise alpha-synuclein or impair lysosomal degradation [PMID:23580063 "GCase
deficiency was not sufficient to either up-regulate ASYN or compromise the lysosomal
degradation machinery"]. These data justify non-core or cautious treatment of
lysosomal protein catabolism annotations.

## Side activities and downstream processes

GBA1 has direct but non-core side activities. It can hydrolyze bile-acid glucosides
and therefore has a beta-glucosidase side activity [PMID:22659419 "GBA1 also
hydrolyses BG"; PMID:22659419 "GBA1 as a bile acid beta-glucosidase"]. It can also
catalyze cholesterol glucosylation by transglucosylation and hydrolyze glucosylated
cholesterol [PMID:24211208 "GBA1 was found to be the responsible enzyme for
cholesterol glucosylation activity"; PMID:26724485 "GBA is able to form GlcChol by
transglucosylation of cholesterol"; PMID:26724485 "GlcChol is ... also an excellent
substrate for hydrolysis by GBA"]. These support non-core cholesterol metabolism,
glycolipid biosynthesis, glucosyltransferase, and steryl-beta-glucosidase annotations.

Ceramide, sphingosine, inflammatory, MAPK, and IL-6 annotations are downstream
cellular consequences of GBA1-generated ceramide rather than the core conserved
activity [PMID:19279011 "GBA1 activation can generate the source (sphingosine) for
PMA-induced formation of ceramide through the salvage pathway"; PMID:19279008
"GBA1-ceramide pathway ... regulating a pro-inflammatory pathway initiated by PKC and
leading to activation of p38 and induction of interleukin 6"].

Generic `protein binding` annotations are not informative GBA1 molecular functions.
The underlying interactions are real in folding, trafficking, or chaperone contexts
[PMID:21098288 "reduced binding of GCase to TCP1 ring complex"; PMID:27789271 "PGRN
binds directly to GCase"; PMID:24162852 "LIMP-2 shows a helical bundle where
beta-glucocerebrosidase binds"], but the more meaningful curation target for the
LIMP-2 interaction is scavenger receptor binding / lysosomal targeting rather than
generic protein binding.


## 2026-11-04 — Enzyme chemistry, cellular consequences and product uncertainty

The principal function is acid glucosylceramide hydrolysis at the lysosomal lumenal lipid surface. Saposin-assisted substrate access and LIMP-2-mediated delivery explain the associated membrane and trafficking evidence without assigning GBA1 a transporter role. Ceramide salvage includes this cleavage, followed by reactions performed by other enzymes. [PMID:9201993](https://pubmed.ncbi.nlm.nih.gov/9201993/); [PMID:19279011](https://pubmed.ncbi.nlm.nih.gov/19279011/); [PMID:18022370](https://pubmed.ncbi.nlm.nih.gov/18022370/).

Measured secondary glycoside chemistry is retained with substrate and assay limits. Its physiological contribution need not equal that of GlcCer turnover, and sterol-glycoside synthesis retains an explicit ontology definition/hierarchy question. [PMID:32144204](https://pubmed.ncbi.nlm.nih.gov/32144204/); [PMID:33361282](https://pubmed.ncbi.nlm.nih.gov/33361282/); [PMID:39395789](https://pubmed.ncbi.nlm.nih.gov/39395789/).

Positive protein-clearance and organelle phenotypes do not by themselves identify the step by which GBA1 affects those processes. The direct protein-catabolism claims remain over-annotated, while regulatory effects are retained. The twin-derived neuronal firing attribution remains uncertain because electrical comparisons and rescue endpoints differ. Both original NOT contexts retain their experimental scope. [PMID:26392287](https://pubmed.ncbi.nlm.nih.gov/26392287/); [PMID:27378698](https://pubmed.ncbi.nlm.nih.gov/27378698/); [PMID:25456120](https://pubmed.ncbi.nlm.nih.gov/25456120/).

All five official products remain represented. The early initiation comparison supports active long and short forms; the 263-residue product's pseudogene-linked citation and sequence differences require genomic reconciliation, not silent deletion or remapping. Product 4/5 functions remain unknown. [PMID:3687939](https://pubmed.ncbi.nlm.nih.gov/3687939/); [PMID:8294033](https://pubmed.ncbi.nlm.nih.gov/8294033/).

Detailed source/construct limits and the vesicle-fraction target row are centralized in [the source guide](GBA1-source-guide.md). The prior GBA/GBA1 reviews, both journals and quotation associations remain preserved. Existing GlcCer catabolism plus location makes the old compartment-specific NTR unnecessary; the old lysosome-reformation NTR is retained historically, with mechanism now expressed as a research question. No new annotation is proposed.

### Neuronal inhibition study and correction

Strong GCase inhibition can coexist with limited alpha-synuclein or proteolysis effects under the tested neuronal conditions. This does not negate the enzyme reaction or establish universal absence of downstream effects. The study has a figure-presentation correction, whose scope is described in the source guide. [PMID:23580063](https://pubmed.ncbi.nlm.nih.gov/23580063/); [2021 correction](https://doi.org/10.1371/journal.pone.0252975).


## 2026-11-04 — Catalytic scope and process specificity after review

GBA1 hydrolysis directly consumes glucosylceramide and produces ceramide, so these two nonredundant process facets now accompany the same lysosomal core. Subsequent reacylation remains the work of ceramide synthases. [PMID:19279011](https://pubmed.ncbi.nlm.nih.gov/19279011/).

The measured C6-NBD-GalCer activity remains positive. Its roughly 200-fold difference is relative to GBA1's GlcCer-analog activity, not GALC. With [lysosomal GALC](https://www.uniprot.org/uniprotkb/P54803/entry) as the dedicated comparator, physiological GalCer clearance by GBA1 remains unestablished and this annotation is marked over-annotated. [PMID:32144204](https://pubmed.ncbi.nlm.nih.gov/32144204/).

The barrier contribution is retained as tissue-specific non-core biology with direct extracellular lipid-processing support, while the membrane-potential annotation is refined to the mitochondrial endpoint actually measured. Neither change assigns GBA1 a hormone receptor or ion-pump activity. [PMID:9101438](https://pubmed.ncbi.nlm.nih.gov/9101438/); [PMID:23707074](https://pubmed.ncbi.nlm.nih.gov/23707074/). Twin-only firing comparisons leave GBA1-specific electrical causality unresolved despite accessible main text. [PMID:25456120](https://pubmed.ncbi.nlm.nih.gov/25456120/).

The sterol-glycoside question is sharpened to causal consequences: bidirectional chemistry and substrate-dependent shifts are supported, whereas a disease contribution from altered glucosylcholesterol requires tests that separate it from glucosylceramide burden. [PMID:26724485](https://pubmed.ncbi.nlm.nih.gov/26724485/). Product 3 remains a suspected provenance concern for database checking, not an established wrong-gene assignment; product 4/5 questions remain limited by the selected evidence. [PMID:8294033](https://pubmed.ncbi.nlm.nih.gov/8294033/).

## 2026-11-04 — Source scope and signaling clarification

The DHT response has a time dependence: rat epidermal GCase activity is unchanged at one day and reduced at two days. The original Results, rather than the abstract’s collective hormone summary, support this context. [PMID:9101438](https://pubmed.ncbi.nlm.nih.gov/9101438/).

GBA1 contributes ceramide-producing chemistry at a signaling control point; downstream phosphatases execute p38 dephosphorylation. This distinguishes its source-specific termination role from protein-phosphatase activity. [PMID:19279008](https://pubmed.ncbi.nlm.nih.gov/19279008/).

The firing question remains unresolved at the level of the annotated GBA1 effect: the inspected twin MEA comparison holds the variant constant, while rescue measures different endpoints. This limits attribution without establishing universal absence of a conditional role. [PMID:25456120](https://pubmed.ncbi.nlm.nih.gov/25456120/). Galactosylcholesterol turnover is now posed separately from the glucosyl branch; direct transfer chemistry does not establish its physiological flux or disease consequences. [PMID:32144204](https://pubmed.ncbi.nlm.nih.gov/32144204/); [PMID:26724485](https://pubmed.ncbi.nlm.nih.gov/26724485/).

## 2026-11-05 ORGANELLES ER batch 2 (endoplasmic reticulum rows)

Rows: GO:0005783 IEA (GO_REF:0000107, Ensembl projection from mouse P17439) and ISS (GO_REF:0000024, P17439), both located_in; no ER sub-compartment rows; no is_active_in. genes/human/GBA (duplicate folder) not touched.

- Source check: QuickGO shows mouse P17439's only ER annotation is IDA from PMID:27789271; mouse UniProt has no ER location line.
- [PMID:27789271 "Double labeling immunogold TEM also showed that PGRN co-localized with GCase in the ER and lysosome"].
- [PMID:40159502 "The GCase/LIMP-2 transport complex forms within the endoplasmic reticulum (ER) and travels through the trans-Golgi network to the lysosome together"].
- GBA1 is a soluble lumenal lysosomal hydrolase (FT SIGNAL 1..39) with no KDEL-like motif; ER = biosynthetic transit where the LIMP-2 receptor complex assembles. ER retention of misfolded Gaucher mutants (PMID:18022370 abstract mentions an "endoplasmic reticulum retention mutant") is mutant quality control and not used as support.
- Outcome: both rows stay KEEP_AS_NON_CORE; supporting_text quotes added to the two bare supported_by entries; dated reason sentence added. No NEW GO:0005788 (transit, not residence).

## 2026-11-06 Retired duplicate review (genes/human/GBA)

`genes/human/GBA`, a duplicate review of the same accession under the old symbol,
was retired in favour of this folder (PR #6088). Its curation calls were weaker on
protein binding and process refinement, but it was systematically stricter on
indirect biological-process rows. These are recorded here so the comparison is not
lost; this review keeps its own calls, which rest on its source guide's rule of
retaining positive effects while separating endpoints from the executed chemistry.

Terms the retired GBA review marked MARK_AS_OVER_ANNOTATED that this review keeps
(KEEP_AS_NON_CORE unless noted): GO:0016241 regulation of macroautophagy,
GO:0006914 autophagy, GO:0007040 lysosome organization, GO:0009267 cellular
response to starvation, GO:0009268 response to pH, GO:0032006 regulation of TOR
signaling, GO:0033574 response to testosterone, GO:0043627 response to estrogen,
GO:0071548 response to dexamethasone, GO:0097066 response to thyroid hormone,
GO:0071356 cellular response to tumor necrosis factor, GO:1905165 regulation of
lysosomal protein catabolic process, GO:0070062 extracellular exosome;
GO:0042176 regulation of protein catabolic process (TOO_GENERAL here);
GO:1904457 positive regulation of neuronal action potential (UNDECIDED here).
For a lysosomal hydrolase the hormone-response and TOR-signalling rows are typical
indirect over-annotations, so these are candidates for a later re-check.
