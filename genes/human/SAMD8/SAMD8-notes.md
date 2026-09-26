# SAMD8 evidence notes

## 2026-09-20 full-gene IBA re-review

Restored a directly observed wild-type Golgi pool; made plasma membrane, HPA cytosol, specific SM/CDP-choline chemistry and ceramide biosynthesis unresolved. Corrected PE-only and universal apoptosis claims while retaining demonstrated CPE/PLC functions.

GO:0047493 uses CDP-choline, unlike the PC-dependent SMS reaction. Updated the old NEW PLC proposal with direct human assays and its construct limits, and the old apoptosis proposal with PMID:24259670. Removed universal PE-only/predominant-human activity claims and softened an established ceramide sensor into a mechanistic model.

- PMID:28120887: Full text and localization results explicitly show a minor but significant wild-type GFP-SMSr Golgi pool; the signal is not restricted to SAM mutants. Stable SMSr-knockout HeLa cells survive, qualifying universal apoptosis dependence.
- PMID:19506037: Primary CPE assays use PE/PC/CDP-ethanolamine and establish ceramide-homeostasis regulation. They do not directly test the CDP-choline reaction defined by GO:0047493 or establish ceramide biosynthesis merely through consumption.
- PMID:38388831: 2024 human cryo-EM and catalytic study emphasizes CPE chemistry and gain of SMS function; full wild-type residual-activity controls require focused adjudication.
- PMID:33621517: Full primary study: purified human ΔSAM SMSr hydrolyzes several glycerophospholipids; full-length human protein in COS-7 immunoprecipitates has PAP/PI-PLC activity with catalytic-mutant controls.
- PMID:24259670: Direct apoptosis-focused primary abstract supports acute ceramide-dependent apoptosis suppression by catalytic activity and SAM domain; added to correct the previously indirect supporting citation.
- PMID:28659495: Caspase cleavage releases the N-terminal SAM domain, but does not establish the explanation for HPA cytosolic staining or prove that substrate cleavage accelerates apoptosis.

PAINT: {'family': 'PTHR21290', 'nodes': ['PTN000480004', 'PTN000480007'], 'finding': 'Current ancestral MF/CC/BP assertions checked. Target human SAMD8 is valid experimental descendant evidence for ceramide biosynthesis; its self-inclusion is not circular.'}

All 22 rows were assessed, including experimental, electronic, negated and old proposed entries. Source annotation fields and row counts remain unchanged. Remaining questions are recorded in `projects/IBA_REVIEW/rereview-2026-09-20/receptor-and-lipid-claims.yaml`; coordinated reports will be assessed critically when available.

Corrected the source metadata of the remaining old reviewer-authored NEW proposal to IMP/PMID:24259670. Actual GOA rows are unaffected.

## 2026-09-21 reaction-donor and completed-report follow-up

The existing broad GO:0016780 core already matches PE-to-ceramide transfer. No frozen source row asserts GO:0002950; the report recommendation to add/upgrade that CDP-ethanolamine/CMP reaction is rejected. GO:0047493 now changes UNDECIDED to MODIFY (GO:0016780) because the actual source SMS reaction uses a phospholipid donor/DAG, not CDP-choline/CMP. The old CPE ontology proposal now states the PE donor explicitly and has an exact primary quote. All 22 source/proposal objects remain unchanged outside review fields.

Read the completed report and its CSV/HTML/PDF, rejecting its mutant-only Golgi claim and unverified pairwise-tree explanation. Saved actual Q96LT4 leaf PTN002501711 lineage: it descends from PTN000480004/000480005 through PTN000480086; PTN000480007 in the older shorthand is not on this target path. Details, live GO definitions and full response hash are in `SAMD8-reaction-donor-check.json`.

Full PMID:40998032 adds human observational coexpression and mouse conditional PE/SPT regulatory work. Full PMID:34332077 adds recombinant human CPE/PE-PLC positives and condition-specific negative SM assays, with conflicting broader hydrolysis relative to 33621517. These were missing from the report. Updated description/core/references distinguish human association from mouse interventions and avoid a claimed direct binary SPT switch. The complete critique and remaining primary/curator follow-ups are in `SAMD8-report-assessment.md`. No new provider request or redundant NEW row was added.
