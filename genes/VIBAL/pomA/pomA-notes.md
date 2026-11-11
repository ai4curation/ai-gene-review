# pomA evidence notes

## 2026-11-06 alternative chemotaxis panel

Identity: O06873; VIBAL/pomA; Vibrio alginolyticus.

The source record labels the sequence strain VI05; later literature commonly writes VIO5. Gene identity is independently anchored to AB004068 and the exact structure sequence rather than spelling equivalence alone. PDB 9IJM is from PMID39793043: PomA is an exact 253-residue match and PomB contains the exact 315-residue target plus HHHHHH. The 2023 PMID37500658 complex was cloned from ATCC17749, has a protease insertion and truncated PomB constructs, and its 8BRD PomB SIFTS mapping names a different accession. It is corroboration, not a full-length identity claim for this PomB. Some functional tests in that paper use a VaPotAB chimera in Salmonella; those are not native Vibrio assays.

PomA is the multi-pass membrane subunit of the sodium-driven polar flagellar stator of Vibrio alginolyticus. Five PomA subunits surround two PomB subunits to form the ion-conducting stator. PomA contributes to sodium permeation and couples ion-driven conformational motion to the rotor through its cytoplasmic interface with FliG.

- [PMID:9260952 Putative channel components for the fast-rotating sodium-driven flagellar motor of a marine bacterium.] Cached text remains abstract-only after normal retrieval and force retry; explicit abstract results are used without inventing methods.
- [PMID:18326582 Roles of charged residues in the C-terminal region of PomA, a stator component of the Na+-driven flagellar motor.] Cached text remains abstract-only after normal retrieval and force retry; explicit abstract results are used without inventing methods.
- [PMID:21642461 Structure of the flagellar motor protein complex PomAB: implications for the torque-generating conformation.] Cached text remains abstract-only after normal retrieval and force retry; explicit abstract results are used without inventing methods. The older A4B2/plugged model is superseded in stoichiometry by later A5B2 cryo-EM structures; it remains informative about membrane and periplasmic organization.
- [PMID:22343296 Characterization of PomA mutants defective in the functional assembly of the Na(+)-driven flagellar motor in Vibrio alginolyticus.] Full cached text inspected. The full article distinguishes polar flagellum motor assays and lateral-flagellum-defective backgrounds. Soft-agar swarm-ring wording does not establish GO surface-swarming motility. It assays PomA-PomB interaction and ion-conductivity effects, so the title focused on PomA does not make PomB interaction citations wrong.
- [PMID:37500658 Ion selectivity and rotor coupling of the Vibrio flagellar sodium-driven stator unit.] Full cached text inspected. ATCC17749 constructs and VaPotAB chimeras in Salmonella are not relabeled as VI05 native assays; the clipped 8BRD PomB chain maps to A0A7Y4B4T7, not a verified full-length O06874 sequence.
- [PMID:39793043 Structural insight into sodium ion pathway in the bacterial flagellar stator from marine Vibrio.] Full cached text inspected. Exact target sequences map to 9IJM (PomA exact; PomB exact plus C-terminal HHHHHH). Five A and two B subunits form the stator. Ion-conductivity experiments use engineered plug-deletion constructs and mutations; these are distinguished from unmodified native behavior.

All original machine fields and raw files are preserved. Normal fetch-gene preceded pristine capture in `.cache/module-audit-logs/chemotaxis-20261106/alternatives-baseline.json`. Default Falcon returned HTTP 403 authorization; this manual journal is not a fabricated provider report. The new proposals reflect chemistry, structure or direct mechanistic participation, not necessity alone. Process comparator results and term ancestry checks are in alternatives-process-comparators.json and alternatives-extra-motor-comparator.json; no matching cached GO-CAM was found.

Ontology scope: GO:0140605 requires a proton gradient, whereas GO:0170085 excludes ion transport. Neither is assigned to sodium-driven PomAB. Sodium channel activity describes the experimentally demonstrated downhill ion-conduction component, with contributes_to for each subunit. GO:0120101 identifies the correct stator complex but its A4B2/nonrotating wording is outdated; this review uses the observed A5B2 architecture. PomB OmpA-like or generic MotB family membership is not evidence of sodium specificity. No unsupported peptidoglycan-binding MF is added from a domain name alone.

Primary strain-table check: PMID22343296 Table 1 on the publisher/PMC article explicitly lists VIO5 as VIK4 laf, Pof+ Laf−, and NMB191 as its ΔpomAB Laf− derivative. This verifies the lateral-flagellum limitation independently of the assay word “swarm.” Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC3318489/ (Table 1).


## 2026-11-06 — PR #6100 review follow-up

Moved the ontology-only knowledge gap to suggested_questions. The GO stator-complex definition retains A4B2/nonrotating wording despite A5B2 structures and models with rotation of the A-subunit ring around the anchored B-subunit dimer. The sodium-driven PomAB stator identity and ion-conducting role are established; this is an ontology-description mismatch rather than uncertainty about the target being a stator. Update the definition of GO:0120101 using modern stator structures while retaining the concept that includes both proton- and sodium-driven stators. Evidence remains in the reference findings: PMID:37500658 (5:2 structure) and PMID:39793043 (sodium pathway). No biological uncertainty about the stator role is implied.


## Preserved parallel flagellar-audit notes from merged main

# pomA research notes


## 2026-11-06 comparative flagellar audit

Current UniProt O06873 is a species-level V.alginolyticus record. Its complete sequence matches RCSB 8ZYW; PomB has only an added C-terminal His6. The alternative SIFTS accession A0A7H8DMV8 differs at residue132 and was rejected as an exact match. PMID39793043 uses recombinant BL21(DE3)/pLysS production and separate functional V.alginolyticus assays. PMID18326582 distinguishes native NMB191 ΔpomAB/VIO5 from an E.coli hybrid. PMID37500658 takes DNA from ATCC17749, inserts a cleavage site in PomB for some structural preparations and tests VaPotAB hybrid function in Salmonella LT2. Those hybrid results are not native Vibrio assays. No NEW biological-process row is needed here. The GO0120101 definition requires a stoichiometry update; the review uses the experimentally resolved A5B2 count.

Default Falcon was attempted once and returned HTTP403 authentication failure; the genuine command log is retained in the ignored comparative-panel audit directory. No provider report was fabricated.

All original annotation payloads, including any inherited NEW proposals, are preserved. Only reviewer-authored judgments and synthesis were updated. Identity bridges and construct limits are recorded under analysis/module_audits/bacterial_flagellar_assembly_export/comparative-panel/.

## 2026-11-06 — PR6138 evidence follow-up

Added motor-level gradient and CheY-control context (PMID27439872; PMID17376072), with the YM4 microfluidic assay distinguished from the selected reference/structural protein. The mechanical-effector inference does not assert a PomA-specific gradient assay.


## 2026-11-11 — reconcile chemotaxis and merged flagellar audits

Retain exact-sequence channel/stator proposals and PomB motility contribution. Use primary swimming and gradient-response evidence from main; chemotaxis is non-core. Preserve main's broader transport and duplicate IC complex proposals as retired historical rows; the more precise channel and target-matched structural IDA remain active. No target-direct flux assay is claimed.
