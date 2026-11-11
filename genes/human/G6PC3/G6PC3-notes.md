# G6PC3 biological notes

## 2026-11-01 — Catalysis and physiological substrates

G6PC3/Q9BUM1 is a 346-residue, nine-transmembrane ER phosphatase. Its active site faces the lumen, and His167 forms the covalent phosphohistidine intermediate. The authentic abstract of [PMID:14718531](https://pubmed.ncbi.nlm.nih.gov/14718531/) establishes that chemistry and topology; it does not identify the dominant physiological substrate. Selected original human wild-type/variant experiments in [PMID:25492228](https://pubmed.ncbi.nlm.nih.gov/25492228/) establish glucose-6-phosphate hydrolysis with mock and expression controls. The supplied assay substrate and a disease association are insufficient to settle physiological substrate preference.

The direct mechanism established in [PMID:30626647](https://pubmed.ncbi.nlm.nih.gov/30626647/) is clearance of 1,5-anhydroglucitol 6-phosphate. Hexose-phosphorylating enzymes generate this side product from 1,5-anhydroglucitol, a largely food-derived polyol. Accumulation inhibits hexokinases and interferes with cellular glucose utilization. Recombinant human G6PC3 hydrolyzes the phosphate ester, with a catalytic H167A control; deficient human cells accumulate the inhibitor. The ER transporter SLC37A4 supplies the transport step. These are two distinct gene-product activities, and G6PC3 performs the detoxifying chemical step itself. Neutrophil dysfunction and death are consequences of the metabolic defect, without establishing a separate apoptosis-regulator molecular activity.

The 2019 work uses several systems that must remain distinct: human enzyme membrane preparations, human HAP1 cells, mouse neutrophil models, rat microsomal transport measurements and limited human patient neutrophil observations. One G6PC3-deficient patient contributed to the reported human metabolite data. Recombinant membrane preparations are not purified protein. Selected text and construct Methods were read; every figure image and supplementary experiment was not independently inspected.

[PMID:39548727](https://pubmed.ncbi.nlm.nih.gov/39548727/) extends the measured sugar-phosphate substrate range in human G6PC3-expressing HEK-cell lysates with empty-vector controls. Rat liver microsomal transport and HL-60 differentiation are separate experiments. The broad in-vitro activity does not establish that every tested sugar phosphate is an important substrate in intact human cells. The table and discussion disagree in the approximate assignment of fructose-6-phosphate versus mannose-6-phosphate Km values, so those numbers are not used to support a physiological ranking.

## Pathway and ontology scope

Glucose-6-phosphate hydrolysis remains a demonstrated capability. Mouse astrocyte evidence in [PMID:15661744](https://pubmed.ncbi.nlm.nih.gov/15661744/) supports local G6PC3/G6PT-dependent glucose production. The actual PAINT family tree places the human G6PC3 target beneath the gluconeogenesis assertion and its experimental descendant evidence. The target's occurrence in an activity or localization donor list is legitimate self-grounding, not circular transfer. The original rat-kidney source [PMID:4303362](https://pubmed.ncbi.nlm.nih.gov/4303362/) does not resolve the molecular isoenzyme in the accessible abstract; that limitation does not justify an assertion that the experimental curation is wrong.

The official [normal Reactome reaction](https://reactome.org/content/detail/R-HSA-3262512) explicitly names G6PC3 as catalyst and places its glucose-6-phosphate dephosphorylation within Gluconeogenesis. The [disease reaction](https://reactome.org/content/detail/R-HSA-3282876) instead models defective variants and links the normal enzyme/reaction. Its title is not a negation of wild-type activity. Neither pathway placement nor glucose-6-phosphate turnover alone quantifies net human tissue gluconeogenic flux from noncarbohydrate precursors.

Cellular detoxification is supported by the direct chemical step and cellular metabolite evidence. The current narrower GO metabolite-repair definitions require a useful product, while the 2019 paper reports no established physiological role for the resulting 1,5-anhydroglucitol. The synthesis therefore uses the cellular-detoxification process and retains the narrower term question explicitly. Human PGP, CLYBL and MAPDA provide same-role enzyme comparators annotated to a descendant of that process. The retained local GO-CAM index contains no literal G6PC3/Q9BUM1 match; this is a scoped index result, not a claim of global absence.

## Evidence retained from the earlier review

The earlier review and journal are preserved as historical provenance. They contain 23 quotation associations; 13 are exact substrings of the retained source bytes, and ten do not match exactly in that comparison. Those historical quotations are not reused as newly verified active evidence. The present core uses one short excerpt verified both in the original source and in the genuine native publication cache. All 17 original contexts and their donor identifiers have been reconciled with the actual native export and parser, and publication titles and cache access metadata have been checked. The [source guide](G6PC3-source-guide.md) explains the scientific access limits; the [source archive](G6PC3-source-evidence.yaml) records actual row joins, the 29 normal sources and the quotation offsets. The [inherited archive](G6PC3-inherited-review-archive.yaml) preserves the earlier review and all 23 historical quotation associations.

<details>
<summary>Historical journal (unchanged text)</summary>

```text
# G6PC3 (Q9BUM1) review notes

## Identity
- Glucose-6-phosphatase 3 / glucose-6-phosphatase-beta (G6Pase-β) / ubiquitous
  glucose-6-phosphatase catalytic subunit-related protein (UGRP). EC 3.1.3.9.
- 346 aa, integral ER membrane protein, 9 transmembrane helices with the active
  site (Arg79, His114, His167) on the lumenal side of the ER membrane
  [UniProt Q9BUM1; PMID:14718531].
- Paralog of the liver/kidney/intestine-restricted G6PC1 (G6Pase-α). ~8x less
  active than G6Pase-α under the same conditions
  [PMID:25492228 "G6Pase-α is eight times more active than G6Pase-β"].

## Molecular function (well supported, experimental)
- Hydrolyzes glucose-6-phosphate (G6P) to glucose + inorganic phosphate in the ER
  [UniProt CATALYTIC ACTIVITY: RHEA:16689, EC 3.1.3.9].
- Forms a covalent phosphohistidine enzyme intermediate at His167 during catalysis;
  active-site mutants R79A, H114A, H167A abolish the intermediate/activity
  [PMID:14718531].
- Disease mutations abolish or reduce phosphohydrolase activity in a sensitive
  rAd/COS-1 assay: 14/16 missense mutants had complete loss; S139I and R189Q
  retained ~49%/45% (and are argued non-pathogenic) [PMID:25492228].
- UniProt CAUTION notes PubMed:12370122 (the original UGRP cloning paper) reported
  no hydrolytic activity, but later studies (PubMed:12965222, 13129915) established
  bona fide G6P hydrolase activity; the catalytic function is now well established.

## Cellular component
- ER membrane, multi-pass; active site in the ER lumen [UniProt SUBCELLULAR
  LOCATION; PMID:14718531; PMID:25492228 "an enzyme embedded in the endoplasmic
  reticulum membrane"]. HPA IDA supports ER localization.
- Membrane (GO:0016020) HDA from an NK-cell membrane-proteome MS survey
  (PMID:19946888) — generic membrane, less informative than ER membrane.

## Biological process
- Directly hydrolyzes G6P → glucose 6-phosphate metabolic process (GO:0051156)
  and intracellular glucose production.
- Works with the ER G6P transporter SLC37A4 (G6PT); the ubiquitous G6Pase-β/G6PT
  complex "maintains energy homeostasis and functionality in neutrophils and
  macrophages" [PMID:25492228].
- Gluconeogenesis (GO:0006094): G6PC3 is ubiquitously expressed and, unlike the
  hepatic G6PC1, is not a classic gluconeogenic/glucose-homeostasis enzyme; its
  clinical phenotype is neutropenia, not fasting hypoglycemia. Gluconeogenesis is
  an IBA/IEA/Reactome pathway-level assignment shared with the family; kept as
  non-core rather than a core function.

## Disease
- Severe congenital neutropenia type 4 (SCN4, MIM 612541), autosomal recessive;
  maturation arrest of granulopoiesis, ER stress and enhanced neutrophil apoptosis
  [UniProt DISEASE; PMID:25492228]. Also Dursun syndrome (DURSS).
- Non-hematological features: prominent superficial venous pattern, congenital
  cardiac anomaly, urogenital malformations [PMID:25492228].

## Curation decisions summary
- Core MF: GO:0004346 glucose-6-phosphatase activity (multiple lines: EXP/IMP/IBA).
- Core CC: GO:0005789 endoplasmic reticulum membrane.
- Core-adjacent process: GO:0051156 glucose 6-phosphate metabolic process.
- Gluconeogenesis annotations kept as non-core.
- GO:0016020 membrane (HDA) marked over-annotated (generic, superseded by ER membrane).
- GO:0005783 endoplasmic reticulum (IBA/IEA/IDA) accepted as correct but non-core
  parent of ER membrane where applicable.

```

</details>

## Validation outcomes on 2026-11-01

Default schema, ontology, reference and best-practice validation passed. Strict GOA reconciliation confirms all 17 incoming contexts alongside the separate cellular-detoxification assertion, giving 18 stored annotations. The native status audit computes DRAFT with one advisory: the core phosphatase activity is not separately present in the incoming annotations. No redundant annotation was added to suppress that advisory. Native EDIT history, the final status audit and the private rendered review passed. All 29 normal sources remain unchanged by authored curation. The single current excerpt is an exact native-cache substring, while all 23 inherited quotation associations remain labeled historical.

## 2026-11-01 — Review follow-up: specific reaction and clinical evidence

The core reaction is represented as proposed 1,5-anhydro-D-glucitol-6-phosphate phosphatase activity, supported by the direct human enzyme experiments in [PMID:30626647](https://pubmed.ncbi.nlm.nih.gov/30626647/). Phosphatase activity is its proposed parent; no GO identifier is invented. The 17 incoming judgments and the separate cellular-detoxification assertion remain unchanged.

Broad expression is supported by the RNA-blot evidence in [PMID:12370122](https://pubmed.ncbi.nlm.nih.gov/12370122/), whose early negative catalytic result is distinguished from later direct assays. Human genetics, mutant enzymatic testing and patient-cell reconstitution in [PMID:19118303](https://pubmed.ncbi.nlm.nih.gov/19118303/) support recessive disease causation, while [PMID:22050868](https://pubmed.ncbi.nlm.nih.gov/22050868/) documents variable nonhematological features. The latter and the expression paper were read as authentic abstracts; selected original Methods and Results were read for the 2009 disease study. These findings support the standalone description without adding phenotype-derived process annotations.

Three focused native-source excerpts now anchor the two experimental glucose-6-phosphatase rows and the detoxification assertion. They supplement the existing core excerpt. The earlier quotation and validation counts above describe the initial published revision. All 23 inherited associations and the complete earlier journal remain unchanged historical records; a source-text match alone is not treated as evidence for a new target-specific claim. The source guide and archive distinguish original reading scope from cache availability.


## 2026-11-01: glucose-6-phosphatase molecular activity

The renewed review of the same commit prompted a distinction between established molecular capability and demonstrated physiological substrate priority. The five existing GO:0004346 rows now use ACCEPT, and a second core entry records glucose-6-phosphate hydrolysis at the ER membrane. Direct human biochemical and variant-control experiments support that capability alongside the verified conserved assignment. The earlier non-core judgments remain in the preceding journal and Git history as historical decisions.

The physiological qualification remains explicit. PMID:30626647 favors 1,5-anhydroglucitol 6-phosphate after comparing recombinant human proteins and rat tissue microsomes, while also measuring transport-dependent G6P hydrolysis. PMID:39548727 uses recombinant human enzyme for kinetics and rat liver microsomes for transport; its Conclusions leave additional physiological substrate roles unresolved. Rat substrate accessibility is not a measurement of human G6PC3-dependent flux. No gluconeogenesis core or new process annotation is added. The 1,5AG6P detoxification core, proposed term, separate cellular-detoxification annotation, all four existing excerpts, and all 23 inherited quotation associations are retained.

Default schema, ontology, reference and best-practice validation passed with zero advisories. Strict GOA reconciliation passed for all 17 originals plus the separate NEW annotation. The native status audit confirms COMPLETE. Native EDIT history, private target rendering and scoped whitespace checks passed. All 29 scientific sources, the compact evidence archive, the complete inherited archive and prior history records remain unchanged.
