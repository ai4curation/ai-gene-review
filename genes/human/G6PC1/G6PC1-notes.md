# G6PC1 (Glucose-6-phosphatase catalytic subunit 1) — review notes

UniProt: P35575 (G6PC1_HUMAN); formerly G6PC / G6PC1; EC 3.1.3.9.
HGNC:4056. 357 aa. Chromosome 17.

## Core biology

G6PC1 is the liver/kidney/intestine catalytic subunit of glucose-6-phosphatase, a
multi-pass integral endoplasmic reticulum (ER) membrane protein (nine transmembrane
helices) whose catalytic active site faces the ER lumen. It hydrolyzes
D-glucose-6-phosphate + H2O -> D-glucose + phosphate (Rhea:16689), the terminal,
committed step shared by gluconeogenesis and glycogenolysis, thereby enabling
hepatic/renal glucose output into blood. It functions together with the ER
glucose-6-phosphate transporter SLC37A4/G6PT, which supplies luminal G6P.

Key UniProt FUNCTION line:
"Hydrolyzes glucose-6-phosphate to glucose in the endoplasmic reticulum. Forms with
the glucose-6-phosphate transporter (SLC37A4/G6PT) the complex responsible for glucose
production in the terminal step of glycogenolysis and gluconeogenesis. Hence, it is the
key enzyme in homeostatic regulation of blood glucose levels."
(ECO:0000269|PubMed:10960498, 12093795, 15542400, 9332655, 9497333)

## Structure / topology / active site (PMID:9497333, PMID:12093795)

- Nine transmembrane helices; N terminus lumenal, C terminus cytoplasmic (odd number of
  TM helices). Active-site residues Arg-83, His-119, His-176 reside on the luminal side.
- His-176 is the nucleophile that forms the phosphohistidine-enzyme intermediate;
  His-119 is the proton donor (ACT_SITE 119 proton donor, 176 nucleophile in UniProt FT).
- PAP2 phosphatase superfamily fold (InterPro IPR016275 Glucose-6-phosphatase;
  IPR000326 PAP2/HPO). N-glycosylated at Asn-96 (PMID:9705299, 19159218).

## Disease: Glycogen storage disease type Ia (GSD1A / von Gierke disease, MIM:232200)

Autosomal recessive; deficiency of G6Pase impairs the terminal steps of glycogenolysis
and gluconeogenesis. Fasting hypoglycemia, severe hepatomegaly (glycogen accumulation),
kidney enlargement, growth retardation, lactic acidemia, hyperlipidemia, hyperuricemia.
Dozens of loss-of-function missense variants characterized (e.g. R83C prevalent in
Ashkenazi Jews; V166G, T16R, Y209C, G188R, K76N, R170Q — several show complete loss of
enzyme activity in expression assays). GSD1b (a distinct entity) is caused by SLC37A4/G6PT
transporter defects, not G6PC1.

## Existing-annotation notes / provenance issues

- PMID:10318794 ("Transmembrane topology of human glucose 6-phosphate transporter")
  is primarily about the G6P transporter (SLC37A4/G6PT). GOA carries three P35575
  annotations citing it (GO:0004346 IDA, GO:0016020 IDA, GO:0005789 TAS). Per curation
  policy I do NOT REMOVE experimental annotations on the basis of the abstract
  foregrounding the transporter; the MF/location are correct for G6PC1. Marked
  MF-IDA as ACCEPT; the generic GO:0016020 membrane IDA marked as over-annotated in favor
  of the specific ER membrane term.
- PMID:15661744 ("Brain contains a functional glucose-6-phosphatase complex...") abstract
  foregrounds glucose-6-phosphatase-beta (G6PC3), but MGI assigned an IDA GO:0004346 to
  P35575. Function is correct for the gene; ACCEPT (defer to curator; do not REMOVE on
  abstract alone).
- GO:0042301 phosphate ion binding (IMP, PMID:12093795): the paper shows His-176 is the
  covalent phosphate acceptor (phosphohistidine intermediate) and Arg-83 positions the
  phosphate; "phosphate ion binding" is a mechanistic sub-aspect of catalysis rather than
  a standalone core MF. Kept as non-core.
- IEA GO:1904638 response to resveratrol, GO:0032094 response to food, GO:0009743 response
  to carbohydrate, GO:0032868/GO:0032869 response to insulin, GO:0031667 response to
  nutrient levels: all Ensembl-projected from rat P43428. These reflect transcriptional
  regulation of the gene (G6PC1 is a canonical insulin/gluconeogenic transcriptional
  target), not molecular functions of the protein; kept as non-core.
- GO:0005515 protein binding (IPI, PMID:32814053; partners WFS1/O76024 and RNF11/Q9Y3C5
  via IntAct Y2H): uninformative bare protein-binding; MARK_AS_OVER_ANNOTATED per policy.

## Core functions

- MF: GO:0004346 glucose-6-phosphatase activity (EC 3.1.3.9)
- BP: GO:0006094 gluconeogenesis; GO:0042593 glucose homeostasis
- CC: GO:0005789 endoplasmic reticulum membrane (active site luminal)
</content>
</invoke>
