# arnE manual review notes

Deep research and FEBA fitness output were not available for this arnE pass.
These notes are grounded in the local UniProt record for Q47377, the paired
arnF review, and the cached publications cited by the seeded arnE GOA rows.

## Identity

- UniProt: Q47377, ARNE_ECOLI
- Preferred gene symbol: arnE
- Older names: pmrL, yfbW
- Ordered locus names: b4544, JW2252
- Product: probable 4-amino-4-deoxy-L-arabinose-phosphoundecaprenol flippase
  subunit ArnE
- Protein: 111 aa, inner-membrane multi-pass protein with an EamA domain
- Family context: ArnE-family member in the DMT/SMR transporter superfamily

## Core function

ArnE/PmrL is one of the two small inner-membrane proteins required to flip
undecaprenyl phosphate-alpha-L-Ara4N from the cytoplasmic to periplasmic face of
the inner membrane. Yan, Guan, and Raetz directly analyzed E. coli pmrL/arnE and
pmrM/arnF deletion mutants and concluded that "PmrL and PmrM could specifically
function to flip undecaprenyl phosphate-alpha-L-Ara4N from the cytosolic to the
periplasmic side of the inner membrane, possibly functioning as a heterodimer"
[PMID:17928292].

The lipid-linked L-Ara4N donor is synthesized on the cytoplasmic face and has to
reach the periplasmic face before ArnT can transfer L-Ara4N to lipid A. In the
pmrL or pmrM mutants, more than 95% of L-Ara4N-modified lipid A was missing
[PMID:17928292 "In the pmrL or pmrM deletion mutants, over 95% of each of the
L-Ara4N-modified lipid A species was missing"], but the donor pool itself was not
depleted [PMID:17928292 "undecaprenyl phosphate-alpha-L-Ara4N levels were the
same or slightly higher in the mutants than in the parent"]. The decisive
labeling experiment used membrane-impermeable sulfo-NHS-biotin and found a
4-5-fold reduction in periplasmically accessible donor in the arnE/arnF mutants
[PMID:17928292 "At the 4-h time point, there was a 4-5-fold reduction in ratio
of the monoisotopic peak areas for biotinylated undecaprenyl
phosphate-alpha-L-Ara4N compared with unmodified undecaprenyl
phosphate-alpha-L-Ara4N"].

## Annotation decisions

- `GO:0005886 plasma membrane` is accepted for all IDA/IBA/IEA rows because this
  is the GO component for the E. coli inner membrane. Daley et al. mapped 601
  E. coli inner-membrane proteins by C-terminal PhoA/GFP tagging [PMID:15919996
  "Using C-terminal tagging with the alkaline phosphatase and green fluorescent
  protein, we established the periplasmic or cytoplasmic locations of the C
  termini for 601 inner membrane proteins"].
- `GO:0022857 transmembrane transporter activity` is too generic for the exact
  activity. ArnE/ArnF flips a lipid-linked donor between leaflets of the same
  membrane, so the best existing molecular-function term is `GO:0140303
  intramembrane lipid transporter activity`, matching the already reviewed ArnF
  partner.
- The three `GO:1901505 carbohydrate derivative transmembrane transporter
  activity` rows are retained. They are less exact about lipid flipping than
  `GO:0140303`, but undecaprenyl phosphate-alpha-L-Ara4N carries a carbohydrate
  derivative and the term is not merely a generic SMR transporter mapping.
- `GO:1901264 carbohydrate derivative transport`, `GO:0046493 lipid A metabolic
  process`, `GO:1901760 beta-L-Ara4N-lipid A biosynthetic process`,
  `GO:0009245 lipid A biosynthetic process`, and `GO:0009103
  lipopolysaccharide biosynthetic process` are all accepted because ArnE does the
  flippase step that places the donor for L-Ara4N modification of lipid A.
- The two `GO:0010041 response to iron(III) ion` rows are real regulatory
  observations but over-annotate arnE's protein function. Hagiwara et al. showed
  the yfbE/arn operon is induced by external iron in a BasS-BasR-dependent manner
  [PMID:15322361 "First we showed that the hypothetical yfbE operon that appears
  to be implicated in the modification of lipopolysaccharides is regulated at the
  level of transcription in response to external iron"]; arnE itself is a lipid
  donor flippase subunit, not an Fe(III) sensor or detoxification protein.

## Ontology note

`GO:0140303 intramembrane lipid transporter activity` is the conservative exact
existing term for ArnE. GO has more specific ATP-coupled flippase/floppase
children and a non-selective scramblase branch, but no specific child for an
ATP-independent, directional, substrate-specific transporter of an undecaprenyl
phosphate-linked sugar. The arnF review makes the same call for the same
two-subunit system.
