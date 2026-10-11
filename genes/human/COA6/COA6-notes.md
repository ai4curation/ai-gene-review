> Historical note provenance: the inherited entries below are retained with source quotations compressed to cited paraphrases. The current assessment appended below supersedes their universal copper-negative statement, generic-binding exclusions, nonspecific-RNA dismissal, exact twin-CX9C wording and unqualified product claims. The original notes and review are preserved in the immutable intake baseline; no history record was rewritten.

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
  [PMID:24549041]. Its loss causes accumulation of CcO assembly
  intermediates and destabilization of newly synthesized COX2
  [PMID:26160915].
- The original model places COA6 in the pathway that builds the COX2 copper site,
  based on its requirement for COX2 production and its temporary association with
  the emerging subunit
  [PMID:25959673].
- Structural + biochemical work shows COA6 adopts a CHCH fold typical of IMS redox
  proteins and acts as a thiol-disulfide oxidoreductase toward its clients SCO1 and
  COX2, reducing the copper-coordinating disulfides to allow copper binding; notably
  COA6 itself is NOT a copper-binding protein under physiological conditions
  [PMID:31851937].
  This qualifies the earlier IDA copper_ion_binding annotation (PMID:26160915 reported
  COA6 binds copper in the experimental preparation), which the later structural study
  reinterprets as non-physiological.

## Localization

Mitochondrion intermembrane space (UniProt SUBCELLULAR LOCATION,
ECO:0000269|PubMed:25339201, PubMed:25959673). Imported via the MIA pathway
using its twin-CX9C motif [PMID:24549041].
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
[PMID:25339201].
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

## Current source-grounded assessment — 2026-10-11

The source set contains 32 review assertions: all 27 historical objects, including two unscoped aggregates, plus five exact current GOA objects for SCO2, MT-CO2, TTC19, DTX2 and CABP2. These are imported machine assertions, not five proposed biological annotations. All 30 current normal tuples are covered. The original three products and 17 reference identities remain intact.

COA6 has one integrated redox/assembly core: protein-disulfide reduction in the mitochondrial intermembrane space, contributing directly to mitochondrial complex-IV assembly. Recombinant human isoform 3 reduces SCO1, SCO2 and COX2. Patient fibroblasts in PMID:31851937 show a SCO1 redox shift with unchanged SCO2 distribution; complete HEK293T knockout and complementation in PMID:32061935 show effects on both SCO proteins. The latter study could not assess COX2 reduction in vivo because COX2 was depleted. Complex-I and import phenotypes do not establish additional direct COA6 activities.

The copper-binding result is retained as non-core. PMID:31515291 measures human isoform-3 Cu(I) binding after purification and copper loading, with competition and cysteine-mutant controls. Its C58S/C90S mutant fails cell rescue while mislocalizing, so that outcome cannot isolate a copper-binding defect from import or folding. PMID:31851937 compares copper peaks in yeast mitochondrial fractions and separately detects binding after recombinant human protein reconstitution. It therefore challenges an autonomous metallochaperone model without disproving measured human binding. Direct physiological copper carriage remains an open question.

Original human fractionation/protease experiments in PMID:25959673 support soluble IMS localization. Its native and two-dimensional separation supports a COA6/SCO2/nascent-COX2 intermediate; this positive simultaneous association is retained without assuming a four-member complex containing SCO1. The official publisher page for PMID:25339201 exposes the original Supplement Figure S1 localization legend, which was read; its inaccessible supplementary PDF was not counted as inspected. HPA XML and MitoCoP proteomics remain broader mitochondrial evidence. The MitoCoP original Table S1 contains Q5JTJ3-3 and a canonical COA6 consensus-gene row, without proving every product was measured.

Positive protein interactions remain supported even when their native role is unresolved. Human COX20 co-isolation is refined to protein-folding chaperone binding based on its nascent-COX2 stabilization role, retaining complex-mediated assay scope. The HuRI DTX2 pair is refined to ubiquitin protein ligase binding from its verified E3 class; this does not imply COA6 ubiquitination. TTC19 includes a tested 108–380 region, and CABP2 is not calmodulin. The historical aggregate rows remain separate from the exact imported partner-scoped objects. These decisions apply the campaign's supported-binding policy; genericity alone does not negate a positive experiment.

RNA contact is also retained as non-core. The authentic PMID:22658674 supplementary table identifies C1orf31/COA6 in the mRNA-interactome set by significant ion-count analysis, although its DESeq result is not significant. The original procedure combines the two statistical outputs after UV crosslinking and stringent oligo-dT isolation. This evidence does not establish a native RNA-processing function, but the inherited nonspecific-capture dismissal lacked target-level support.

All three official alternative products are preserved. Deterministic reconstruction gives lengths 125, 155 and 79 residues; these are sequence facts, not equivalent functional testing. The structural studies use isoform 3, corresponding to canonical residues 47–125, and keep canonical numbering. The motif is noncanonical C-X9-C-Xn-C-X10-C, rather than an exact twin-CX9C repeat. The historical family/import/disease prose above must be read within this corrected scope; clinical necessity does not supply additional performed biological processes.

Access was checked source by source. Existing main publication caches remain exact. Separate genuine full variants provide the missing Results/Methods for PMID:24549041 and PMID:28330871. PMID:25959673 was read from its authentic repository-hosted publisher article and supplement; PMID:26160915 remains abstract-only. The two new genuine full caches are PMID:31515291 and PMID:32061935. Short literal anchors appear only in the YAML; the source index contains records, URLs, hashes and paraphrases, not duplicate quotations.

The genuine default Falcon attempt timed out, and the recorded fallback returned an insufficient-quota error. No provider report was fabricated. This manual assessment and the original primary evidence underpin the review. The GO-CAM index has no target match; this absence does not justify a new process assertion.
