> Historical context: the earlier generic-binding exclusions, cross-paper partner attribution and unqualified redox-cycle wording below are superseded by the dated assessments that follow.

# COA7 (Q96BR5) review notes

Synonyms: C1orf163, RESA1 (RESpiratory chain Assembly 1), SELRC1 / SEL1 repeat-containing 1.
HGNC:25716. MANE NP_075565.2. 231 aa. Belongs to the hcp beta-lactamase family; contains
five Sel1-like repeats (helix-turn-helix α/α). PDB 7MQZ (2.39 Å).

## Core biology and short primary anchors

- **Soluble mitochondrial IMS protein.** The original abstract reports a "mitochondrial soluble intermembrane space protein" [PMID:24333015]. Later human-cell affinity purification, disulfide-sensitive interaction and import experiments establish the CHCHD4/MIA40 substrate relationship [PMID:30885959]. This is COA7 import, not import catalysis performed by COA7.
- **Complex-IV assembly.** The original knockdown study reports "strongest defects in the assembly of complex IV" [PMID:24333015]. Its complex-I effects are retained as context, not promoted to a separate core assembly role.
- **COX2/COX3 module maturation.** Human knockout/rescue and assembly-intermediate experiments place COA7 after the COX1 module; the authors describe "maturation of the COX2 and/or COX3 modules" [PMID:35210360, Results on complex-IV assembly]. This does not resolve every direct physical assembly contact.
- **Heme-dependent disulfide reduction.** Reduced, heme-loaded recombinant human COA7 reduces SCO1/SCO2 disulfides, with the authors reporting "disulfide reductase activity" [PMID:35210360, Results and Figure 4]. The measured reduction potential is −353 mV. Cellular redox changes and rescue connect this activity to the copper relay; neither a physiological electron donor nor repeated catalytic turnover was established. COA7 is not asserted to deliver copper or heme to complex IV.

## Disease

- **SCAN3** — Spinocerebellar ataxia, autosomal recessive, with axonal neuropathy 3
  (MIM:618387); also described as mitochondrial leukoencephalopathy with complex IV (COX)
  deficiency and peripheral neuropathy. Recessive; variants include Y137C (increased proteasomal
  degradation, reduced IMS import), D6G, R39W, S149I. [PMID:27683825; PMID:29718187; PMID:30885959].
  Not a GO annotation but supports the localization/function calls.

## Superseded baseline dispositions — historical context only

The following old action list is historical context, not the current assessment. The current partner refinements and retired aggregate flags are described below.

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

## Historical core summary
- MF: GO:0015035 protein-disulfide reductase activity (IDA-supported; the exact GOA MF).
- BP: GO:0033617 mitochondrial respiratory chain complex IV assembly (directly_involved_in).
- CC: GO:0005758 mitochondrial intermembrane space (located_in).

## Current source-grounded assessment — 2026-10-11

The current annotation set has 38 decisions: 33 active source assertions, four retired historical screen aggregates and one proposed heme-binding molecular function. The four old unscoped screen aggregates retain their positive experimental meaning; their retirement distinguishes them from the current partner-scoped successors.

One integrated core combines protein-disulfide reduction with mitochondrial complex-IV assembly in the IMS. Human HEK293T knockout and rescue place COA7 after the COX1 assembly module, with SCO redox changes and COX2/COX3 instability. Reduced heme-loaded recombinant human COA7 acts on soluble SCO1 and SCO2 domains. The original SI specifies E. coli expression, GST cleavage leaving GPLGS, SCO1 128–301 and SCO2 96–266, and removal of excess dithionite before the reaction. SCO1 SI S17 contains the broader control panel; SCO2 S18 independently compares WT and Y137C. These experiments establish reductase capacity, not an identified physiological electron donor or repeated catalytic turnover. [PMID:35210360]

One NEW GO:0020037 captures direct heme binding within that same core. The purified human protein binds hemin with a micromolar fit, near-stoichiometric loading and ligand-mutant support. Official typed ancestors and descendants show no overlap with any original term or final replacement and no more-specific child. Heme is a cofactor here; the tested incorporation model argues against heme delivery to complex IV. The negative copper competition experiment is limited to its assay and does not create a universal negative annotation. No new biological process, copper-chaperone function or separate heme-binding core is proposed. [PMID:35210360]

The genuine CHCHD4 interaction is refined to enzyme binding. Human cells show a cysteine-dependent COA7–MIA40 complex, and MIA40 promotes import of COA7 as its substrate. COA7 overexpression did not promote import of the tested other MIA substrates or change MIA40 redox state. Import is therefore not a second catalytic or process role of COA7. [PMID:30885959]

Localization is source-specific. The original 2013 abstract positively supports soluble human IMS residence; its full paper remains unrecovered. PMID:27683825 later interpreted its fractionation and trypsin-protection data as predominantly matrix localization. The subsequent human swelling/protease-release experiments and compartment-resolved imaging in PMID:30885959 explicitly address that conflict and favor the IMS. The 2016 finding is marked DISPUTED only for its localization interpretation; patient-cell complex-IV rescue and the underlying observation are retained. Original MitoCoP Table S1 directly identifies COA7/Q96BR5 in all-protein row 222 and mitochondrial-set row 197. That broad proteomic support is accepted without attributing an independent IMS assignment or every individual validation assay to COA7. [PMID:24333015; PMID:27683825; PMID:30885959; PMID:34800366]

All positive screen observations are retained at their measured assay scope. Genericity and uncertain native colocalization do not make an interaction false. HuRI contributes five exact partner pairs with 15 positive array, pooling and validated Y2H records. The separate neurodegeneration interactome contributes 12 pairs with 36 positive records; its DMWD 316–649 and PRPF40A-2 716–930 regions are explicit. Dataset-wide MAPPIT/GPCA or DULIP validation is not assigned to every COA7 pair. [PMID:32296183; PMID:32814053]

Class refinements identify SUOX, HMOX2, ACOT8 and BKGD as enzymes; CASP6 and DPP8 as proteases; RAN as a small GTPase; FGFR3 as an FGF receptor; TLE5-2 as a corepressor-class protein; and ENKD1 as a microtubule-associated cytoskeletal protein. They do not transfer the partners’ catalytic or signaling activities to COA7. Exact official partner products reconstruct to SNRPB-2 231, TLE5-2 264, PRPF40A-2 930 and LAMP2B 410 residues. The initial GSN decision was non-core at the component-class boundary; the second follow-up below supersedes it with the supported regulatory-protein-binding child while preserving the exact 782-residue precursor. ENKD1’s class rests on microtubule binding/stabilization plus localization, not an invented part_of record. TLE5-2 class inference is not an isoform-specific repression experiment.

BioPlex contributes three exact human HCT116 anti-tag coimmunoprecipitation records for ACOT8, DPP8 and BKGD/C11orf54. The 2025 paper’s original U2OS AP-MS dataset independently contains those three edges; each partner is marked bait and COA7 prey. These are actual AP-MS edges, not inferred image-proximity links or a reused HEK293 comparison network. Complex-mediated capture does not establish purified binary binding or a native mitochondrial pathway. The current name BKGD is linked to the original C11orf54 label by its official identity. [PMID:33961781; PMID:40205054]

Recessive COA7 disease associations support clinical context. Patient-cell effects vary between complex I and IV, and fly knockdown phenotypes are distinct from human molecular-function assays. None of those observations alone adds a neuronal development, complex-I assembly or other secondary process. [PMID:27683825; PMID:29718187]

Access is recorded precisely. PMID:32814053 remains abstract-only in the selected cache, with author-repository full-text Methods/Results read separately. The selected HuRI body supplies Results/Discussion and validation legends, not a separate Methods section; the selected BioPlex body supplies Introduction/Discussion and its abstract. Target-specific original interaction records establish their pairs. The clinical papers are available as full text. The evidence index provides public source locators and target extracts.

Current target self evidence in PAINT is valid experimental grounding, while the historical PTN placement remains uninspected.

## Follow-up of the published COA7 review

This amendment clarifies source status and evidence access while retaining the positive experiments and the reductase/heme/IMS synthesis. The source union contains 37 historical/current assertions plus the existing heme-binding proposal. Four unscoped historical screen aggregates are now marked `retired: true` because the current source projection contains their partner-scoped successors. Their original fields and positive non-core judgments are preserved; retirement is not experimental refutation. The remaining 33 source assertions and the single reviewer NEW are distinguished in the evidence index.

Supported generic binding remains non-core if no justified refinement exists. Binding to an authenticated receptor, GTPase or catalytic-protein class does not itself assign receptor agonism, signaling, GTPase regulation or catalysis to COA7. The positive binary screens and AP-MS records retain their assay and product limits. Earlier blanket dismissal of these pairs as noise is superseded; absence of an established physiological interaction is not proof that the measured interaction is false.

The exact GO:0008092 definition requires a cytoskeletal protein component, not a filament-forming or mechanically structural molecule. ENKD1's official experimental microtubule-binding/stabilizing and centrosomal/centriolar/spindle evidence supports the retained class refinement. The gelsolin record maps to the 782-residue secreted precursor, whereas the official cytoskeletal location specifically concerns the distinct cytoplasmic product. This first follow-up retained positive actin-modulating capacity but left the component-class refinement unresolved; the second follow-up below resolves the more specific regulatory class. No partner-function paper is represented as newly read merely because an official entry cites it.

The [evidence index](COA7-source-evidence.json) contains the original MitoCoP header/cell values, all 54 complete source MITAB records underlying 20 screen pairs, and the original U2OS nodes, edges and bait attributes for its three pairs. These original-data projections are distinct from the index’s authored interpretations.

The separately read [author-deposited neurodegeneration article](https://edoc.mdc-berlin.de/id/eprint/19322/1/19322oa.pdf) is identified by DOI 10.1016/j.celrep.2020.108050, PDF/text hashes and exact layout-text newline ranges in the index. Its protected publication cache remains abstract-only. The public [MitoCoP Table S1](https://ars.els-cdn.com/content/image/1-s2.0-S1550413121005295-mmc2.xlsx) and [original U2OS AP-MS network](https://www.ndexbio.org/v2/network/95bc75d5-d1d1-11ee-8a40-005056ae23aa) are linked with their original-data hashes.

The more specific mitochondrial assembly replacement retains the independent IBA and IMP sources; convergent reviewed terms are not source duplicates to delete. Its term-scoping root cause concerns the present human assertion, not a reconstructed failure of the historical PAINT node. The active CHCHD4 assertion now carries its current Q8N4Q1 supporting entity; the earlier omission is retained only in historical records. The description now makes the SCO/CuA copper-relay connection explicit without claiming that COA7 transfers copper or delivers heme.

## Second follow-up: binding definitions and source scope

The current [FGFR-binding definition](https://www.ebi.ac.uk/QuickGO/term/GO:0005104), [corepressor-binding definition](https://www.ebi.ac.uk/QuickGO/term/GO:0001222) and [cytoskeletal-protein-binding definition](https://www.ebi.ac.uk/QuickGO/term/GO:0008092) describe the bound partner. Their typed ancestry does not add a requirement that COA7 participates in the partner's native functional module. Exact positive binary records plus authenticated partner class therefore support the retained FGFR3, TLE5-2 and ENKD1 refinements. Processing, isoform and assay limits remain explicit; the partner's activity is not assigned to COA7.

ENKD1 has experimental microtubule-binding/stabilizing and cytoskeletal-component evidence in its official record. Gelsolin is now refined to [cytoskeletal regulatory protein binding](https://www.ebi.ac.uk/QuickGO/term/GO:0005519), a more specific child of GO:0008092. Its three record fingerprints match the 782-residue displayed precursor, whose official actin capping, nucleation and severing function establishes the regulatory class. The distinct 731-residue cytoplasmic isoform's localization does not negate that positive capability. This supersedes the earlier non-core class judgment. No COA7 cytoskeletal process, native interaction, mature processing state or contact with a particular domain is inferred. The positive screen and exact product scope remain unchanged.

The active PMID:30885959 IPI record identifies CHCHD4/MIA40 (UniProtKB:Q8N4Q1) in its supporting-entity field. The earlier review omitted that field even though its notes named the partner. Restoring the exact current source value does not change the positive interaction, enzyme-binding refinement or COA7 substrate interpretation. The evidence index retains the historical object separately.

## ENKD1 regulatory-class clarification

The second follow-up now refines the ENKD1 replacement from GO:0008092 to [cytoskeletal regulatory protein binding](https://www.ebi.ac.uk/QuickGO/term/GO:0005519). The experimentally supported [official ENKD1 record](https://www.uniprot.org/uniprotkb/Q9H0I2/entry) describes regulation of microtubule organization and stability, including astral microtubule stabilization and spindle orientation. This supplies a positive regulatory-class basis beyond component localization. The three positive HuRI records map to the same 346-residue product; MODIFY remains the action. This clarification supersedes the broader ENKD1 replacement discussed above, while preserving the assay, source, product and physiological limits. This does not establish a COA7 cytoskeletal process or contacted interface.

## Current source reconciliation — 2026-10-12

The three inherited PAINT annotations now explicitly carry PANTHER:PTN001016310 and UniProtKB:Q96BR5, and the subcellular-location mapping carries UniProtKB-SubCell:SL-0169. These are the existing GOA source identities, not newly inferred functions or reconstructed historical node placements. Along with the CHCHD4 field repair, all 33 active assertions now match the current source records; the four retired aggregates and single heme-binding proposal remain separate.

The current [cytoskeletal regulatory protein binding definition](https://www.ebi.ac.uk/QuickGO/term/GO:0005519) and typed child response explicitly place GO:0005519 under GO:0008092 by is_a. This supports the existing ENKD1 and gelsolin specificity without adding a COA7 cytoskeletal process. The separate IBA and IMP assembly assertions retain their distinct sources even though their final terms converge.
