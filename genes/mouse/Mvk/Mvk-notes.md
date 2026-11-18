# Mvk (mouse) review notes

UniProt Q9R008 (KIME_MOUSE), MGI:107624, 395 aa. PANTHER PTHR43290:SF2 (MEVALONATE KINASE).
GHMP kinase family. No deep-research provider file was generated (no provider keys in this
environment); these notes are my own literature work.

## Literature search (2026-11-18)

Europe PMC queries run:

- `(TITLE:"mevalonate kinase" OR TITLE:"Mvk") AND (mouse OR mice OR murine)`: 59 hits. Mouse-specific
  primary papers: Hager 2007 (PMID:18008182), Munoz 2022 (PMID:36189795), Mvk+/- immunophenotype
  (PMID:21607759), the 2026 NK-cell MKD paper (PMID:42066777), and two tumour papers that propose
  non-metabolic MVK functions (PMID:39725712 STAT1, PMID:39844257 TBK1). The rest are human MKD,
  trypanosomatid MVK, or aminobisphosphonate "MKD models" that do not touch the Mvk gene
  (PMID:24292573, PMID:23760140).
- `ABSTRACT:"Mvk" AND (conditional OR knockout OR floxed) AND mice`: 4 hits, none a conditional
  Mvk allele.
- `"mevalonate kinase" AND peroxisom* AND (mouse OR mice OR murine) AND (localization ...)`:
  152 hits, mostly reviews; no mouse MVK localization study found.
- Peroxisome proteomics: `(TITLE:peroxisom*) AND (TITLE:proteom*) AND (mouse OR mice)` found the
  2024 mouse liver peroxisome SWATH-MS study (PMID:38247867). Its text names PMVK, not MVK, among
  the pathway enzymes in the peroxisome cluster; I could not see the supplementary table, so I make
  no claim about whether MVK was detected.
- Rat and human sources behind the ISO/ISS rows were retrieved from QuickGO (P17256, Q03426) and
  read: PMID:1312092, PMID:7904598, PMID:17180682 (peroxisome, Krisans lab), PMID:14730012 (human
  cytosol, Hogenboom), PMID:11877411 (rat MK structure), PMID:14749336 and PMID:16263716 (rat MVK
  as LH-receptor mRNA-binding protein), PMID:23376535.

All cached copies are abstract-only except PMID:36189795, PMID:21607759, PMID:36378328,
PMID:39844257, PMID:38247867, PMID:42240661 and PMID:23376535 (full text).

## Mouse biology

- Catalytic activity in mouse tissue. Mvk+/- mice have about half of liver MK activity and no
  Mvk-/- pups are born [PMID:18008182 "Deletion of one Mvk allele (Mvk (+/-)) yielded viable mice
  with significantly reduced liver Mvk enzyme activity; multiple matings failed to produce Mvk (-/-)
  mice"]. CRISPR alleles (V377I, frameshifts) titrate MK activity in liver and bone marrow
  [PMID:36189795 "Consistent with the Δ91 mutation causing complete loss of function, heterozygous
  Mvk+/Δ91 mice had approximately 50% normal MK activity in liver homogenates compared with wild-type
  counterparts"]. Activity was assayed in a 10,000 g supernatant of tissue homogenate
  [PMID:36189795 "After centrifuging (10,000g for 30 minutes, 4°C), MK activity in the supernatant
  was measured"], which is not a subcellular localization experiment.
- Pathway consequence in vivo. Low-activity mice accumulate mevalonic acid and unprenylated small
  GTPases [PMID:36189795 "Compound heterozygous mice recapitulated the characteristic biochemical
  phenotype of MKD, with increased plasma mevalonic acid and clear buildup of unprenylated GTPases in
  PBMCs, splenocytes, and bone marrow"]; elevated body temperature worsens the defect
  [PMID:36189795 "Elevated temperature dramatically but reversibly exacerbated the deficit in the
  mevalonate pathway and the defective prenylation in vitro and in vivo"]. Inflammation is a
  downstream consequence [PMID:36189795 "The inflammatory response to LPS was enhanced in compound
  heterozygous mice"].
- Peroxisome independence. In Pex5-/- (Zellweger) mouse liver the cholesterol-pathway enzymes keep
  their activity [PMID:11792727 "We found that all enzymes measured, including putative peroxisomal
  enzymes, are at least as active in the peroxisome-deficient Zellweger mice as in control mice"].

## Localization: the peroxisome rows

- Every peroxisome row on mouse Mvk is synthesis (ISS and ISO from rat P17256/RGD:621295, and the
  UniProt SubCell keyword IEA, which itself rests on the rat by-similarity line). No mouse
  experiment places MVK in peroxisomes.
- The rat source is direct but disputed: [PMID:1312092 "we demonstrate the presence of mevalonate
  kinase in rat liver peroxisomes and in the cytosol"], [PMID:7904598 "there is only one mevalonate
  kinase protein that is predominantly localized in peroxisomes"]; the same lab later reported
  human cells too [PMID:17180682]. Human MK was found only in the cytosol by fractionation,
  digitonin, IF and immuno-EM [PMID:14730012 "No indication of a peroxisomal localisation was
  obtained"], and a 2026 historical review frames rat and human as differing
  [PMID:42240661 "In contrast to rat liver (Krisans 1996) the three enzymes of mevalonate metabolism
  (i.e. mevalonate kinase, mevalonate pyrophosphate decarboxylase, and phosphomevalonate kinase)
  were, in human liver, observed in the cytosol, not in peroxisomes"].
- Mouse MVK has no C-terminal PTS1 (ends ...QALGL). Its N-terminus contains K13-V14-x5-H20-A21,
  which fits the PTS2 consensus pattern; that is a sequence observation only, not shown to target.
- Decision: MARK_AS_OVER_ANNOTATED on all three peroxisome rows (not REMOVE, because the rat source
  is an experimental IDA we cannot read in full and no mouse experiment contradicts it directly).
  Cytosol accepted as the core location by orthology to human plus the PAINT node.

## Rat moonlighting: LH-receptor mRNA binding

- Rat ovarian LRBP was identified as MVK [PMID:14749336 "the data support the novel function of rat
  mevalonate kinase as a LHR mRNA-binding protein in the post-transcriptional regulation of LH
  receptor expression in the ovary"], binding is sequence-specific [PMID:16263716 "This mutation of
  LBS has been shown to render it incapable of interacting with LRBP"] and it inhibits translation
  in vitro [PMID:16263716 "The addition of LRBP inhibited LHR mRNA translation"]. Later work frames
  the effect as decapping and P-body decay [PMID:23376535]. All of this is rat (and some human
  granulosa-cell) work; no mouse study was found. Kept the binding rows as non-core, the
  translation-regulation row as over-annotated for mouse.

## GO-CAM-derived pathway rows

The IMP/IDA rows to cholesterol, geranylgeranyl diphosphate and zymosterol biosynthesis come from
MGI GO-CAM models 67c10cc400008232 (via desmosterol), 682fbcd000004876 (via lathosterol) and
68b0f0d000003768 (GGPP). In those models the evidence for "IPP biosynthesis part_of zymosterol
biosynthesis part_of cholesterol biosynthesis" sits on the process-to-process edges, and the GAF
export gives that evidence to every enzyme in the model. The papers are about other genes:
Hsd17b7 knockout [PMID:18669642 "we generated a knockout mouse model with targeted deletions of
exons 1-4 of this gene"], HMGCS1 inhibition by ursolic acid (PMID:35671633), liver Hmgcr deletion
(PMID:33109681) and hepatic Acat2 overexpression (PMID:36378328). The WITH allele MGI:3811923 is
Hsd17b7<tm1Gibo> (Alliance allele API, 2026-11-18). The claims (Mvk acts in the pathway that feeds
cholesterol and GGPP) are right; the evidence code IMP is not about an Mvk mutant. Recorded once,
for the cohort, as a source defect on the Mvk PMID:18669642 row.

## Non-canonical claims not in GOA (not annotated)

- MVK binds STAT1 and dampens tumour-intrinsic IFN signalling (PMID:39725712, abstract only).
- MVK binds TBK1 and represses cGAS-STING in lung adenocarcinoma (PMID:39844257).
Both are single reports in cancer models; no NEW rows proposed.
