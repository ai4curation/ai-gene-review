# COX7B (human) — curation notes

UniProtKB:P24311 · HGNC:2291 · X chromosome · 80 aa precursor (24-aa mitochondrial
transit peptide, 56-aa mature chain) · single-pass inner-membrane protein.

## What COX7B is

COX7B is the nuclear-encoded structural subunit 7B (polypeptide VIIb) of mitochondrial
respiratory Complex IV (cytochrome c oxidase, COX / CIV), the terminal enzyme of the
electron transport chain. Complex IV has a mtDNA-encoded catalytic core of three
subunits (MT-CO1, MT-CO2, MT-CO3) plus nuclear-encoded supernumerary subunits; COX7B is
one of the latter and is non-catalytic. It surrounds/supports the catalytic core and
contributes to complex assembly and stability.

- "Human cytochrome c oxidase (COX) is a complex of 13 subunits: three are encoded by
  mitochondrial DNA and ten by nuclear DNA. We have now isolated a full-length cDNA
  specifying subunit VIIb, the last remaining uncharacterized nuclear-encoded subunit
  cDNA of human COX." [PMID:8382530]
- UniProt SUBUNIT: catalytic core MT-CO1/2/3 (mtDNA) + 11 supernumerary subunits
  including COX7B, all nuclear-encoded [PMID:30030519]; complex is a 14-subunit monomer
  (including NDUFA4) that also forms supercomplexes/megacomplexes [PMID:28844695].

## Molecular function

COX7B has no catalytic activity of its own; the catalytic O2-reduction chemistry occurs
at heme a3/CuB in the mtDNA-encoded MT-CO1. As a supernumerary subunit its MF is best
described as **structural molecule activity (GO:0005198)**, contributing to the
integrity/assembly of the holoenzyme (contributes_to cytochrome-c oxidase activity
GO:0004129). The legacy GOA `enables GO:0004129 cytochrome-c oxidase activity` (TAS,
ProtInc/PINC, PMID:8382530) over-attributes whole-complex catalysis to a structural
subunit — MODIFY to GO:0005198.

## Localization

Mitochondrion inner membrane, single-pass membrane protein (topology: matrix 25-32,
TM 33-59, IMS 60-80). GO:0005743 mitochondrial inner membrane is the precise CC term;
GO:0005739 mitochondrion and GO:0031966 mitochondrial membrane are correct but broader;
GO:0016020 membrane is a very broad ARBA IEA.
- SUBCELLULAR LOCATION: "Mitochondrion inner membrane ...; Single-pass membrane protein"
  [PMID:30030519].

## Biological process

Core BP = mitochondrial electron transport, cytochrome c to oxygen (GO:0006123) as part
of complex IV; broader oxidative phosphorylation / cellular respiration. Proton
transmembrane transport (GO:1902600) is inferred by the GOC inter-ontology link from the
complex's cytochrome-c oxidase activity; the proton pumping is a property of the
catalytic core, so keep as non-core for this structural subunit.

## Disease / development

X-linked. Deleterious COX7B mutations cause Linear skin defects with multiple congenital
anomalies 2 (LSDMCA2 / MIM:300887), a microphthalmia-with-linear-skin-defects
(MLS/MIDAS)-spectrum disorder — an "unconventional" mitochondrial disease with a
neurodevelopmental phenotype.
- "we analyzed the X-linked COX7B and found deleterious de novo mutations ... COX7B
  encodes a poorly characterized structural subunit of cytochrome c oxidase (COX), the
  MRC complex IV. We demonstrated that COX7B is indispensable for COX assembly, COX
  activity, and mitochondrial respiration. Downregulation of the COX7B ortholog (cox7B)
  in medaka ... resulted in microcephaly and microphthalmia ... demonstrated an
  essential function of complex IV activity in vertebrate CNS development." [PMID:23122588]

The GOA `involved_in GO:0007417 central nervous system development` (IMP, PMID:23122588)
reflects the medaka knockdown / MLS phenotype: this is a downstream developmental
consequence of loss of complex IV activity, not a distinct molecular role of COX7B →
KEEP_AS_NON_CORE.

## GO:0005515 protein binding (IPI, PMID:32296183, with GNMT/Q14749)

From HuRI (high-throughput binary yeast-two-hybrid interactome map). A single Y2H hit
with GNMT (a cytosolic methyltransferase), no functional context, and bare "protein
binding" is uninformative for this inner-membrane complex subunit →
MARK_AS_OVER_ANNOTATED (do NOT REMOVE per policy).

## Action plan (21 GOA rows)

- GO:0005739 mitochondrion (IBA) — ACCEPT (non-core broad CC, correct)
- GO:0045277 respiratory chain complex IV (IBA) — ACCEPT (core complex membership)
- GO:0005743 mitochondrial inner membrane (IEA SubCell) — ACCEPT (core CC)
- GO:0006123 electron transport c->O2 (IEA InterPro) — ACCEPT (core BP)
- GO:0016020 membrane (IEA ARBA) — MARK_AS_OVER_ANNOTATED (too broad)
- GO:1902600 proton transmembrane transport (IEA GOC link) — KEEP_AS_NON_CORE
- GO:0005515 protein binding (IPI HuRI) — MARK_AS_OVER_ANNOTATED
- GO:0006119 oxidative phosphorylation (IEA UniPathway) — ACCEPT (non-core broader BP)
- GO:0006123 (NAS ComplexPortal) — ACCEPT
- GO:0031966 mitochondrial membrane (IDA ComplexPortal) — ACCEPT (correct, broader than inner mem)
- GO:0045277 (IPI ComplexPortal) — ACCEPT (core complex membership)
- GO:0045333 cellular respiration (NAS ComplexPortal) — ACCEPT (non-core broader BP)
- GO:0005743 (EXP UniProt) — ACCEPT (core CC)
- GO:0005739 mitochondrion (HTP) — ACCEPT (non-core broad CC)
- GO:0005743 x4 (TAS Reactome) — ACCEPT (core CC)
- GO:0007417 CNS development (IMP PMID:23122588) — KEEP_AS_NON_CORE
- GO:0004129 cytochrome-c oxidase activity (TAS PMID:8382530) — MODIFY -> GO:0005198 structural molecule activity

## core_functions

- MF: GO:0005198 structural molecule activity (contributes_to GO:0004129)
- BP: GO:0006123 mitochondrial electron transport, cytochrome c to oxygen
- CC: located_in GO:0005743 mitochondrial inner membrane; in_complex GO:0045277 respiratory chain complex IV
