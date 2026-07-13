# COA6 (Q5JTJ3) review notes

Human COA6 (C1orf31), HGNC:18025. 125 aa, ~14 kDa. Chromosome 1.
Belongs to the cytochrome c oxidase subunit 6B family (twin CX9C / CHCH-domain
IMS protein). MANE isoform is Q5JTJ3-2 per UniProt; 3 alternative products.

## Function summary

COA6 is a small mitochondrial intermembrane-space (IMS) / inner-membrane-associated
assembly factor for respiratory chain complex IV (cytochrome c oxidase, CcO). Its
core role is in copper delivery to and maturation of the mtDNA-encoded subunit
MT-CO2/COX2, specifically metallation of the binuclear CuA center.

- COA6 is required for complex IV biogenesis in yeast, zebrafish and human cells
  [PMID:24549041 "shown its requirement for respiratory complex IV biogenesis in
  yeast, zebrafish and human cells"]. Its loss causes accumulation of CcO assembly
  intermediates and destabilization of newly synthesized COX2
  [PMID:26160915 "caused by impaired biogenesis of the copper-bound mitochondrial DNA-encoded subunit COX2 and subsequent accumulation of complex IV assembly intermediates"].
- COA6 is specifically required for COX2 biogenesis and interacts transiently with
  the copper-containing catalytic domain of newly synthesized COX2, functioning as
  a constituent of the mitochondrial copper relay system
  [PMID:25959673 "COA6 is specifically required for COX2 biogenesis"; "COA6 interacts transiently with the copper-containing catalytic domain of newly synthesized COX2"; "define COA6 as a constituent of the mitochondrial copper relay system, linking defects in COX2 metallation to cardiac cytochrome c oxidase deficiency"].
- Structural + biochemical work shows COA6 adopts a CHCH fold typical of IMS redox
  proteins and acts as a thiol-disulfide oxidoreductase toward its clients SCO1 and
  COX2, reducing the copper-coordinating disulfides to allow copper binding; notably
  COA6 itself is NOT a copper-binding protein under physiological conditions
  [PMID:31851937 "COA6 adopts a coiled-coil-helix-coiled-coil-helix (CHCH) domain, preferentially interacts with SCO1, and exhibits thiol-disulfide oxidoreductase activity both in vitro and in vivo, with SCO1 and COX2 being its client proteins. We further demonstrate that COA6 is not a Cu-binding protein under physiological conditions"; "COA6 can reduce the copper-coordinating disulfides of its client proteins, SCO1 and COX2, allowing for copper binding"].
  This qualifies the earlier IDA copper_ion_binding annotation (PMID:26160915 reported
  COA6 "has the capacity to bind copper" in vitro), which the later structural study
  reinterprets as non-physiological.

## Localization

Mitochondrion intermembrane space (UniProt SUBCELLULAR LOCATION,
ECO:0000269|PubMed:25339201, PubMed:25959673). Imported via the MIA pathway
using its twin-CX9C motif [PMID:24549041 "the mitochondrial import of Coa6 is
dependent on MIA import machinery, which utilizes the characteristic twin Cx 9 C motif"].
CC terms: GO:0005758 mitochondrial intermembrane space (IDA/EXP); GO:0005739
mitochondrion (IBA/IEA/IDA/HTP/ISS). Functionally it works at the inner-membrane
face where CcO assembles (GO:0005743 inner membrane / GO:0045277 complex IV).

## Interactions (all IPI GO:0005515 in GOA)

- SCO1 (O75880), PMID:26160915 — copper chaperone client
- SCO2 (O43819) + MT-CO2/COX2 (P00403), PMID:25959673 — copper relay partners/client
- COX20 (Q5RI15), PMID:28330871 and PMID:29154948 — COX2 maturation module chaperone
- COX16 (Q9P0S2), PMID:29381136 — COX2 metallation/assembly
- TTC19 (Q6DKK2), DTX2 (Q86UW9), CABP2 (Q9NPB3), PMID:32296183 — HuRI binary
  interactome hits; biologically non-obvious, likely high-throughput false/indirect;
  treat as protein-binding over-annotation.

Interactions with SCO1/SCO2/COX2/COX20/COX16 are all within the COX2 copper-delivery
module and support the assembly-factor MF/BP rather than being informative "protein
binding" annotations in their own right.

## Disease

Mitochondrial complex IV deficiency, nuclear type 13 (MC4DN13, MIM:616501):
autosomal recessive fatal infantile hypertrophic cardiomyopathy, left-ventricular
non-compaction, lactic acidosis, complex IV deficiency
[PMID:25339201 "neonatal hypertrophic cardiomyopathy and isolated complex IV deficiency ... COA6 is required for complex IV subunit stability"].
Pathogenic variant W59C mistargets COA6 to the matrix and abolishes SCO2/MT-CO2
binding (UniProt VARIANT). Copper supplementation partially rescues the CcO defect
[PMID:24549041; PMID:25339201].

## Schema notes

- core_functions[].directly_involved_in is a LIST of Term.
- suggested_questions is a list of Question objects (key: question, optional experts).
- suggested_experiments is a list of Experiment objects (key: description, optional
  hypothesis/experiment_type).

## Annotation-specific judgments

- GO:0015035 protein-disulfide reductase activity — IDA (PMID:31851937) is the
  experimentally grounded MF; ACCEPT (core). The IBA duplicate ACCEPT.
- GO:0005507 copper ion binding — IDA (PMID:26160915) captures in vitro Cu-binding
  capacity but PMID:31851937 shows COA6 is not a physiological Cu-binding protein;
  MARK_AS_OVER_ANNOTATED (do not REMOVE experimental IDA).
- GO:0033617 / GO:0008535 (complex IV assembly, mito and generic) — ACCEPT; core BP.
  GO:0008535 is the less-specific parent of GO:0033617; keep as-is (GOA), core = 0033617.
- GO:0005515 protein binding (multiple IPI) — MARK_AS_OVER_ANNOTATED per curation
  policy (uninformative bare protein binding); the informative content is captured
  by the assembly-factor MF/BP and the specific partners are noted above.
- GO:0003723 RNA binding — HDA from a global mRNA-interactome capture (PMID:22658674);
  no evidence COA6 is a bona fide RNA-binding protein; MARK_AS_OVER_ANNOTATED.
- GO:0005739 mitochondrion (IBA/IEA/IDA/HTP/ISS) — ACCEPT (broad but correct); the
  more specific GO:0005758 IMS is the informative CC.
