> Historical note provenance: the inherited notes below are preserved with source quotations compressed to cited paraphrases. Their generic-binding exclusions, cross-paper partner attribution, source count and unqualified redox-cycle wording are superseded by the current assessment appended below. The original notes remain immutable in the intake baseline; no previous history record was rewritten.

# COA7 (Q96BR5) review notes

Synonyms: C1orf163, RESA1 (RESpiratory chain Assembly 1), SELRC1 / SEL1 repeat-containing 1.
HGNC:25716. MANE NP_075565.2. 231 aa. Belongs to the hcp beta-lactamase family; contains
five Sel1-like repeats (helix-turn-helix α/α). PDB 7MQZ (2.39 Å).

## Core biology (verified)

- **Mitochondrial intermembrane-space (IMS) protein.** Soluble IMS protein; import into the
  IMS is mediated by the MIA pathway (CHCHD4/MIA40) via transient intermolecular disulfide
  bonds. [PMID:24333015]
  [PMID:30885959]. UniProt SubCell: Mitochondrion intermembrane space
  (SL-0169) → GO:0005758.

- **Complex IV (cytochrome c oxidase) assembly factor.** Metazoan-specific. Knockdown reduces
  OXPHOS complex levels; strongest defect is in complex IV assembly (also complex I).
  [PMID:24333015]. Named
  RESA1 for RESpiratory chain Assembly 1. Core BP = mitochondrial respiratory chain complex IV
  assembly (GO:0033617); IBA carries the broader GO:0008535.

- **Acts early in complex IV assembly.** Loss of COA7 blocks assembly after the COX1 module is
  built; progression requires copper incorporation and addition of COX2/COX3 modules.
  [PMID:35210360].

- **Redox / disulfide-reductase role in copper relay (MT-CO2/COX2 maturation).** COA7 is a
  heme-binding protein; heme-COA7 has a reduction potential of −353 mV and reduces the disulfide
  bonds forming the copper-binding sites of the copper metallochaperones SCO1 and SCO2, thereby
  regenerating the copper relay to the CuA site (COX2). This underpins GO:0015035 protein-
  disulfide reductase activity (IDA, PMID:35210360; IBA GO_REF:0000033).
  [PMID:35210360].

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

## Current source-grounded assessment — 2026-10-11

The final review contains 38 decisions: all 14 original source objects, 23 exact partner-scoped current GOA imports, and one proposed heme-binding molecular function. Current GOA contains 33 assertions: 23 screen associations and 10 other unique assertions, including CHCHD4 binding. The four old unscoped screen aggregates remain intact rather than being silently narrowed to one partner. The other 10 historical objects cover the 10 current nonscreen tuples. Imported source rows are not biological NEW proposals. The absent product list and all 11 historical reference identity pairs are preserved; two genuine clinical references make the inherited notes citations explicit.

One integrated core combines protein-disulfide reduction with mitochondrial complex-IV assembly in the IMS. Human HEK293T knockout and rescue place COA7 after the COX1 assembly module, with SCO redox changes and COX2/COX3 instability. Reduced heme-loaded recombinant human COA7 acts on soluble SCO1 and SCO2 domains. The original SI specifies E. coli expression, GST cleavage leaving GPLGS, SCO1 128–301 and SCO2 96–266, and removal of excess dithionite before the reaction. SCO1 SI S17 contains the broader control panel; SCO2 S18 independently compares WT and Y137C. These experiments establish reductase capacity, not an identified physiological electron donor or repeated catalytic turnover. [PMID:35210360]

One NEW GO:0020037 captures direct heme binding within that same core. The purified human protein binds hemin with a micromolar fit, near-stoichiometric loading and ligand-mutant support. Official typed ancestors and descendants show no overlap with any original term or final replacement and no more-specific child. Heme is a cofactor here; the tested incorporation model argues against heme delivery to complex IV. The negative copper competition experiment is limited to its assay and does not create a universal negative annotation. No new biological process, copper-chaperone function or separate heme-binding core is proposed. [PMID:35210360]

The genuine CHCHD4 interaction is refined to enzyme binding. Human cells show a cysteine-dependent COA7–MIA40 complex, and MIA40 promotes import of COA7 as its substrate. COA7 overexpression did not promote import of the tested other MIA substrates or change MIA40 redox state. Import is therefore not a second catalytic or process role of COA7. [PMID:30885959]

Localization is source-specific. The original 2013 abstract positively supports soluble human IMS residence; its full paper remains unrecovered. PMID:27683825 later interpreted its fractionation and trypsin-protection data as predominantly matrix localization. The subsequent human swelling/protease-release experiments and compartment-resolved imaging in PMID:30885959 explicitly address that conflict and favor the IMS. The 2016 finding is marked DISPUTED only for its localization interpretation; patient-cell complex-IV rescue and the underlying observation are retained. Original MitoCoP Table S1 directly identifies COA7/Q96BR5 in all-protein row 222 and mitochondrial-set row 197. That broad proteomic support is accepted without attributing an independent IMS assignment or every individual validation assay to COA7. [PMID:24333015; PMID:27683825; PMID:30885959; PMID:34800366]

All positive screen observations are retained under the campaign supported-binding policy (projects/CLINGEN_MENDELIAN.md, supported experimental generic-binding exception). Genericity and uncertain native colocalization do not make an interaction false. HuRI contributes five exact partner pairs with 15 positive array, pooling and validated Y2H records. The separate neurodegeneration interactome contributes 12 pairs with 36 positive records; its DMWD 316–649 and PRPF40A-2 716–930 regions are explicit. Dataset-wide MAPPIT/GPCA or DULIP validation is not assigned to every COA7 pair. [PMID:32296183; PMID:32814053]

Class refinements identify SUOX, HMOX2, ACOT8 and BKGD as enzymes; CASP6 and DPP8 as proteases; RAN as a small GTPase; FGFR3 as an FGF receptor; TLE5-2 as a corepressor-class protein; and ENKD1 as a microtubule-associated cytoskeletal protein. They do not transfer the partners’ catalytic or signaling activities to COA7. Exact official partner products reconstruct to SNRPB-2 231, TLE5-2 264, PRPF40A-2 930 and LAMP2B 410 residues. The GSN record fingerprint matches the secreted 782-residue precursor rather than the distinct cytoplasmic isoform, so its positive association remains non-core without an unresolved component-class refinement. ENKD1’s class rests on microtubule binding/stabilization plus localization, not an invented part_of record. TLE5-2 class inference is not an isoform-specific repression experiment.

BioPlex contributes three exact human HCT116 anti-tag coimmunoprecipitation records for ACOT8, DPP8 and BKGD/C11orf54. The 2025 paper’s original U2OS AP-MS dataset independently contains those three edges; each partner is marked bait and COA7 prey. These are actual AP-MS edges, not inferred image-proximity links or a reused HEK293 comparison network. Complex-mediated capture does not establish purified binary binding or a native mitochondrial pathway. The current name BKGD is linked to the original C11orf54 label by its official identity. [PMID:33961781; PMID:40205054]

Recessive COA7 disease associations support clinical context. Patient-cell effects vary between complex I and IV, and fly knockdown phenotypes are distinct from human molecular-function assays. None of those observations alone adds a neuronal development, complex-I assembly or other secondary process. [PMID:27683825; PMID:29718187]

Access is recorded precisely. Eight original main publication caches remain unchanged. PMID:32814053 remains abstract-only in the selected cache, with genuine author-repository full-text Methods/Results read separately. The selected HuRI body supplies Results/Discussion and validation legends, not a separate Methods section; the selected BioPlex body supplies Introduction/Discussion and its abstract. Target-specific original interaction records establish their pairs. The two new clinical caches are genuine normal full text. Raw primary responses and long extracts remain in TMP; the published source index contains identifiers, literal record projections, hashes, durable URLs and concise interpretations, without repeated primary quotations.

The authentic Falcon research attempt timed out, and its sole fallback returned an insufficient-quota error. No provider report was invented. Manual primary reading and the separate bounded catalytic and partner-class consultations support this review. Current target self evidence in PAINT is valid experimental grounding, while the historical PTN placement remains uninspected. The GO-CAM index has no COA7 match; that absence is not evidence for a new process.

Normal validation, status consistency and rendering pass. Fourteen advisories concern the deliberately retained positive generic-binding assertions and are dispositioned by the explicit campaign policy. DRAFT is the ordinary tool-derived consistent status. The final ownership census contains 360 complete open-PR inventories with no COA7 overlap; existing source bytes are unchanged. ROOT will authenticate the live publisher application separately.
