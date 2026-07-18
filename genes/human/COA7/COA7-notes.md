# COA7 (Q96BR5) review notes

Synonyms: C1orf163, RESA1 (RESpiratory chain Assembly 1), SELRC1 / SEL1 repeat-containing 1.
HGNC:25716. MANE NP_075565.2. 231 aa. Belongs to the hcp beta-lactamase family; contains
five Sel1-like repeats (helix-turn-helix α/α). PDB 7MQZ (2.39 Å).

## Core biology (verified)

- **Mitochondrial intermembrane-space (IMS) protein.** Soluble IMS protein; import into the
  IMS is mediated by the MIA pathway (CHCHD4/MIA40) via transient intermolecular disulfide
  bonds. [PMID:24333015 "C1orf163 is a mitochondrial soluble intermembrane space protein"]
  [PMID:30885959 "COA7 requires the mitochondrial IMS import and assembly (MIA) pathway for
  efficient accumulation in the IMS"]. UniProt SubCell: Mitochondrion intermembrane space
  (SL-0169) → GO:0005758.

- **Complex IV (cytochrome c oxidase) assembly factor.** Metazoan-specific. Knockdown reduces
  OXPHOS complex levels; strongest defect is in complex IV assembly (also complex I).
  [PMID:24333015 "we observe the strongest defects in the assembly of complex IV"]. Named
  RESA1 for RESpiratory chain Assembly 1. Core BP = mitochondrial respiratory chain complex IV
  assembly (GO:0033617); IBA carries the broader GO:0008535.

- **Acts early in complex IV assembly.** Loss of COA7 blocks assembly after the COX1 module is
  built; progression requires copper incorporation and addition of COX2/COX3 modules.
  [PMID:35210360 "acts in the early stages of complex IV assembly"].

- **Redox / disulfide-reductase role in copper relay (MT-CO2/COX2 maturation).** COA7 is a
  heme-binding protein; heme-COA7 has a reduction potential of −353 mV and reduces the disulfide
  bonds forming the copper-binding sites of the copper metallochaperones SCO1 and SCO2, thereby
  regenerating the copper relay to the CuA site (COX2). This underpins GO:0015035 protein-
  disulfide reductase activity (IDA, PMID:35210360; IBA GO_REF:0000033).
  [PMID:35210360 "reduce the disulfide bonds that compose the copper binding sites in the
  assembly factors SCO1 and SCO2, enabling regeneration of the copper relay system"].

## Disease

- **SCAN3** — Spinocerebellar ataxia, autosomal recessive, with axonal neuropathy 3
  (MIM:618387); also described as mitochondrial leukoencephalopathy with complex IV (COX)
  deficiency and peripheral neuropathy. Recessive; variants include Y137C (increased proteasomal
  degradation, reduced IMS import), D6G, R39W, S149I. [PMID:27683825; PMID:29718187; PMID:30885959].
  Not a GO annotation but supports the localization/function calls.

## Annotation-by-annotation dispositions

GOA has 14 lines (mapped to 14 existing_annotations, some IPI rows collapsed by reference).

- GO:0008535 respiratory chain complex IV assembly, IBA — ACCEPT (broader parent of GO:0033617).
- GO:0015035 protein-disulfide reductase activity, IBA — ACCEPT (backed by IDA PMID:35210360).
- GO:0005758 mitochondrial intermembrane space, IBA (is_active_in) — ACCEPT.
- GO:0005758 mitochondrial intermembrane space, IEA (SubCell) — ACCEPT.
- GO:0005515 protein binding IPIs (PMID:32296183, 32814053, 33961781, 40205054) — MARK_AS_OVER_ANNOTATED
  (uninformative bare protein binding from HT interactome screens; many partners are not IMS/mito
  and are likely non-physiological, e.g. FGFR3, RAN, GSN). Per policy NOT removed.
- GO:0033617 mitochondrial respiratory chain complex IV assembly, IMP (PMID:24333015/FlyBase) — ACCEPT (core BP).
- GO:0015035 protein-disulfide reductase activity, IDA (PMID:35210360) — ACCEPT (core MF).
- GO:0005758 mitochondrial intermembrane space, IDA (PMID:24333015) — ACCEPT (core CC).
- GO:0005739 mitochondrion, HTP (PMID:34800366) — KEEP_AS_NON_CORE (correct but less specific than IMS).
- GO:0005515 protein binding IPI (PMID:30885959, with CHCHD4/MIA40 Q8N4Q1) — MARK_AS_OVER_ANNOTATED
  (bare protein binding; the interaction is real and biologically meaningful — MIA40 import — but
  the GO term itself is uninformative; per policy NOT removed).
- GO:0005758 mitochondrial intermembrane space, IDA (PMID:30885959) — ACCEPT.

## Core functions
- MF: GO:0015035 protein-disulfide reductase activity (IDA-supported; the exact GOA MF).
- BP: GO:0033617 mitochondrial respiratory chain complex IV assembly (directly_involved_in).
- CC: GO:0005758 mitochondrial intermembrane space (located_in).
</content>
