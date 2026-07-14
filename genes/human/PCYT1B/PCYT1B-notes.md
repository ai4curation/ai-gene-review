# PCYT1B (CCTβ / CTP:phosphocholine cytidylyltransferase B) — review notes

UniProt: Q9Y5K3 (PCY1B_HUMAN), 369 aa. Gene on chromosome X. HGNC:8755.
Source of most assertions below: local UniProt record
[file:human/PCYT1B/PCYT1B-uniprot.txt].

## Identity and reaction

- RecName "Choline-phosphate cytidylyltransferase B"; AltNames "CCT-beta",
  "CTP:phosphocholine cytidylyltransferase B" (Short "CCT B"/"CT B").
  [file:human/PCYT1B/PCYT1B-uniprot.txt]
- EC 2.7.7.15; reaction "phosphocholine + CTP + H(+) = CDP-choline +
  diphosphate" (Rhea RHEA:18997), physiological direction left-to-right.
  [file:human/PCYT1B/PCYT1B-uniprot.txt]
- FUNCTION: "Catalyzes the key rate-limiting step in the CDP-choline pathway
  for phosphatidylcholine biosynthesis." (annotated for isoform 1 and isoform
  2). [file:human/PCYT1B/PCYT1B-uniprot.txt]
- PATHWAY: "Phospholipid metabolism; phosphatidylcholine biosynthesis;
  phosphatidylcholine from phosphocholine: step 1/2." (UniPathway
  UPA00753/UER00739). [file:human/PCYT1B/PCYT1B-uniprot.txt]

This is the beta isoform of the rate-limiting enzyme of the CDP-choline
(Kennedy) pathway. The paralog CCTα is PCYT1A (P49585).

## Amphitropic / membrane-activated, lipid-regulated enzyme

- "CCTbeta and CCTalpha proteins share highly related, but not identical,
  catalytic domains followed by three amphipathic helical repeats. Like
  CCTalpha, CCTbeta required the presence of lipid regulators for maximum
  catalytic activity." [PMID:9593753 "CCTbeta and CCTalpha proteins share
  highly related, but not identical, catalytic domains followed by three
  amphipathic helical repeats. Like CCTalpha, CCTbeta required the presence of
  lipid regulators for maximum catalytic activity."]
- The amphipathic helices are the membrane-lipid-sensing element that
  interconverts a soluble inactive form and a membrane-bound active form
  (amphitropic behaviour); GO:0031210 phosphatidylcholine binding (IBA)
  captures this membrane lipid interaction and is shared with the family.

## Localization: cytoplasmic / ER, NOT nuclear (contrast with CCTα)

- CCTβ lacks the CCTα N-terminal nuclear localization signal. "The amino
  terminus of CCTbeta bears no resemblance to the amino terminus of CCTalpha,
  and CCTbeta protein was localized to the cytoplasm as detected by indirect
  immunofluorescent microscopy." [PMID:9593753 "and CCTbeta protein was
  localized to the cytoplasm as detected by indirect immunofluorescent
  microscopy."]
- Both β splice variants are ER-associated, unlike nuclear CCTα: "both
  CCTbeta1 and CCTbeta2 localized to the endoplasmic reticulum of cells, in
  contrast to CCTalpha which resided in the nucleus in addition to associating
  with the endoplasmic reticulum." [PMID:10480912 "both CCTbeta1 and CCTbeta2
  localized to the endoplasmic reticulum of cells, in contrast to CCTalpha
  which resided in the nucleus in addition to associating with the endoplasmic
  reticulum."]
- UniProt SUBCELLULAR LOCATION: isoform 1 Cytoplasm + Endoplasmic reticulum;
  isoform 2 Endoplasmic reticulum. [file:human/PCYT1B/PCYT1B-uniprot.txt]
- Reactome R-HSA-1483081 places the active PCYT1 homodimer at the ER membrane.
  [Reactome:R-HSA-1483081]

## Enzymatic activity confirmed / functional complementation

- "CCTbeta2 protein has enzymatic activity in vitro and was able to complement
  the temperature-sensitive cytidylyltransferase defect in CHO58 cells, just as
  CCTalpha and CCTbeta1 supporting proliferation at the nonpermissive
  conditions." [PMID:10480912 "CCTbeta2 protein has enzymatic activity in vitro
  and was able to complement the temperature-sensitive cytidylyltransferase
  defect in CHO58 cells, just as CCTalpha and CCTbeta1 supporting proliferation
  at the nonpermissive conditions."]
- Overexpression drives pathway flux: "Transfection of COS-7 cells with a
  CCTbeta expression construct led to the overexpression of CCT activity, the
  accumulation of cellular CDP-choline, and enhanced radiolabeling of
  phosphatidylcholine." [PMID:9593753 "Transfection of COS-7 cells with a
  CCTbeta expression construct led to the overexpression of CCT activity, the
  accumulation of cellular CDP-choline, and enhanced radiolabeling of
  phosphatidylcholine."] This supports both the enzyme MF and the BP
  (phosphatidylcholine biosynthesis / CDP-choline pathway).

## Tissue distribution and structure

- Tissue-restricted vs ubiquitous CCTα: "CCTbeta transcripts were detected in
  human adult and fetal tissues, and very high transcript levels were found in
  placenta and testis." [PMID:9593753 "very high transcript levels were found
  in placenta and testis."] UniProt TISSUE SPECIFICITY (isoform 1): "Highly
  expressed in testis, placenta, brain, ovary, liver and fetal lung."
  [file:human/PCYT1B/PCYT1B-uniprot.txt] HPA: tissue enhanced in brain, retina,
  testis. [file:human/PCYT1B/PCYT1B-uniprot.txt]
- SUBUNIT: Homodimer (by similarity to CCTα P19836).
  [file:human/PCYT1B/PCYT1B-uniprot.txt]
- Four alternatively spliced isoforms (β2 displayed = Q9Y5K3-1; β1 =
  Q9Y5K3-2). β2 is heavily phosphorylated in vivo, β1 is not: "Like CCTalpha,
  CCTbeta2 is heavily phosphorylated in vivo, in contrast to CCTbeta1."
  [PMID:10480912 "CCTbeta2 is heavily phosphorylated in vivo, in contrast to
  CCTbeta1."]
- SIMILARITY: cytidylyltransferase family; catalytic Rossmann-like HUP fold
  (Pfam PF01467 CTP_transf_like; CDD cd02174 CCT; PANTHER PTHR10739:SF20).
  [file:human/PCYT1B/PCYT1B-uniprot.txt]

## Curation decisions summary

Core molecular function: GO:0004105 choline-phosphate cytidylyltransferase
activity (verified label current via OLS). Core BP: GO:0006656
phosphatidylcholine biosynthetic process and the more specific GO:0006657
CDP-choline pathway. Membrane-lipid sensing captured by GO:0031210
phosphatidylcholine binding. Locations: cytoplasm (GO:0005737), ER
(GO:0005783), ER membrane (GO:0005789).

- IDA/TAS enzyme + PC-biosynthesis + CDP-choline-pathway + ER/cytoplasm
  annotations: ACCEPT (experimentally grounded in the two Jackowski-lab papers
  and the UniProt record).
- IBA GO:0004105 and GO:0031210: ACCEPT (family-conserved; consistent with the
  amphitropic, lipid-regulated CCT mechanism).
- IEA GO:0003824 catalytic activity: MARK_AS_OVER_ANNOTATED — correct but far
  too general given the specific EC 2.7.7.15 activity is directly annotated.
- IEA duplicates of GO:0004105, GO:0006656, GO:0006657 (GO_REF:0000120):
  ACCEPT (redundant with IDA but not wrong).
- IEA GO:0046470 phosphatidylcholine metabolic process (ARBA): KEEP_AS_NON_CORE
  — true parent of the biosynthetic process but less informative than GO:0006656.
- No experimental annotation is removed. No proposed removals of IEA that are
  biologically wrong (all IEA terms are consistent with the enzyme).
