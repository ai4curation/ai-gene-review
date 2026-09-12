# NDUFB9 (Complex I-B22 / LYRM3) — review notes

UniProt: Q9Y6M9 (NDUB9_HUMAN). Gene: NDUFB9; synonyms LYRM3, UQOR22.
HGNC:7704. GeneID 4715. Chromosome 8 (8q13). 179 aa.

## Identity and family
- RecName: "NADH dehydrogenase [ubiquinone] 1 beta subcomplex subunit 9";
  AltNames: Complex I-B22 / CI-B22; LYR motif-containing protein 3; NADH-ubiquinone
  oxidoreductase B22 subunit. [file:human/NDUFB9/NDUFB9-uniprot.txt lines 6-11]
- Belongs to the complex I LYR family. [file:human/NDUFB9/NDUFB9-uniprot.txt
  "Belongs to the complex I LYR family."]
- InterPro: Complex1_LYR domain (IPR008011), Complex1_LYR_NDUFB9_LYRM3 (IPR045292),
  NDUFB9 (IPR033034); Pfam PF05347; CDD cd20263. [file:human/NDUFB9/NDUFB9-uniprot.txt lines 312-318]

## Function (core)
- Accessory (supernumerary) subunit of mitochondrial membrane respiratory chain
  NADH dehydrogenase (Complex I), **believed to be NOT involved in catalysis**.
  Complex I transfers electrons from NADH to the respiratory chain; the immediate
  electron acceptor is believed to be ubiquinone.
  [file:human/NDUFB9/NDUFB9-uniprot.txt "involved in catalysis. Complex I functions
  in the transfer of electrons"] (FUNCTION, ECO:0000269|PubMed:27626371)
- Non-catalytic → honest MF is **structural molecule activity (GO:0005198)**,
  contributing to the complex-level NADH dehydrogenase (ubiquinone) activity
  (GO:0008137) via `contributes_to_molecular_function`, NOT a direct `enables`.

## Complex membership
- Mammalian complex I is composed of 45 different subunits.
  [file:human/NDUFB9/NDUFB9-uniprot.txt "Mammalian complex I is composed of 45
  different subunits."] (SUBUNIT; ECO:0000269|PubMed:12611891, PubMed:27626371)
- Direct MS/immunopurification identification of NDUFB9 as a Complex I subunit:
  [PMID:12611891 "we can resolve and identify the human"] — resolved human
  homologues of 42 Complex I polypeptides.
- Systematic knockout / complexome study: accessory subunits integral for assembly
  and function; most "required for assembly of a functional complex and 1 subunit
  is essential for" cell viability; loss of a subunit destabilizes subunits of the
  same structural module. [PMID:27626371 "required for assembly of a functional
  complex and 1 subunit is essential for"]
- Cryo-EM megacomplex I2III2IV2 gives "precise assignment of individual subunits of"
  human CI, placing NDUFB9 in the complex and respirasome. [PMID:28844695]
- part_of GO:0045271 (respiratory chain complex I) is the well-supported core CC:
  evidence IDA (PMID:12611891, PMID:27626371), IPI (PMID:28844695, ComplexPortal),
  IBA (GO_REF:0000033), IEA (Ensembl GO_REF:0000107), NAS (PMID:9878551).

## Localization
- Subcellular: Mitochondrion inner membrane; Peripheral membrane protein; Matrix side.
  [file:human/NDUFB9/NDUFB9-uniprot.txt "Mitochondrion inner membrane"] (SUBCELLULAR
  LOCATION, ECO:0000305|PubMed:12611891)
- Supported by IDA (ComplexPortal PMID:28844695), TAS (Reactome; PMID:8661098),
  HPA IDA (mitochondrion), HTP (PMID:34800366).

## Biological process
- Core BP: mitochondrial electron transport, NADH to ubiquinone (GO:0006120) —
  IEA/NAS/TAS; and Complex I assembly (GO:0032981). NDUFB9 participates via its
  structural contribution to the assembled complex.
- Complex I: "the transport of electrons from NADH to ubiquinone, which is"
  accompanied by proton translocation. [PMID:9878551]

## Disease
- Mitochondrial complex I deficiency, nuclear type 24 (MC1DN24), MIM 618245,
  autosomal recessive; variant p.Leu64Pro. [file:human/NDUFB9/NDUFB9-uniprot.txt
  lines 186-199, 340-343] (ECO:0000269|PubMed:22200994)

## Annotations judged over-broad / over-annotated (subunit-level)
- GO:0008137 "enables NADH dehydrogenase (ubiquinone) activity" (NAS PMID:9878551;
  TAS PMID:8661098): NDUFB9 is non-catalytic → MARK_AS_OVER_ANNOTATED; captured as
  `contributes_to_molecular_function` in core_functions instead of direct enables.
- GO:1902600 proton transmembrane transport (IEA GO_REF:0000108, derived from
  GO:0008137): over-annotation for an accessory subunit → MARK_AS_OVER_ANNOTATED.
- GO:0042776 proton-motive-force-driven mitochondrial ATP synthesis (NAS
  PMID:30030361): downstream OXPHOS outcome, performed by Complex V; over-broad for
  a Complex I accessory subunit → MARK_AS_OVER_ANNOTATED.
- GO:0007605 sensory perception of sound (TAS PMID:8661098): positional-candidate
  inference (NDUFB9 maps to 8q13 BOR region); "this gene should be considered a
  strong candidate for involvement in" hearing loss — not a demonstrated auditory
  function → MARK_AS_OVER_ANNOTATED.
- Bare GO:0005515 protein binding (7× IPI, large-scale interactome/HTT screens):
  retained per policy but MARK_AS_OVER_ANNOTATED; uninformative for MF.
- GO:0009060 aerobic respiration (NAS PMID:30030361): true at pathway level but
  broad/inherited → KEEP_AS_NON_CORE.
- GO:0005739 mitochondrion (IEA/IDA/HTP): correct but general vs inner membrane →
  KEEP_AS_NON_CORE.

## Core functions chosen
- molecular_function: GO:0005198 (structural molecule activity)
- contributes_to_molecular_function: GO:0008137 (NADH dehydrogenase (ubiquinone) activity)
- directly_involved_in: GO:0006120, GO:0032981
- locations: GO:0005743 (mitochondrial inner membrane)
- in_complex: GO:0045271 (respiratory chain complex I)

## Provenance note
- All cited publications in this review are abstract-only in the cache
  (full_text_available: false), except PMID:17500595 (full text; HTT interactome,
  supports IPI protein binding only). No paraphrase used in supporting_text; every
  quote is a verbatim single-line substring of the cited source.
