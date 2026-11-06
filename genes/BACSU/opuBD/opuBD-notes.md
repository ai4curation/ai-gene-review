# opuBD evidence notes

2026-11-06. Annotation-reviewer and core-function-synthesizer consultation.

Identity: P39775, Bacillus subtilis strain168. The normal fetch was performed before curation; all original row payloads, complete pristine seed document and raw hashes are frozen in `.cache/module-audit-logs/choline-betaine-20261106/bacillus-baseline.yaml`. The Falcon command was attempted and failed HTTP403. These are manual notes, not an invented provider report.

PMID10216873 (Kappes et al.,1999), full author-hosted article inspected: native radiolabeled choline uptake distinguishes OpuB-only RMKB20 and OpuC-only RMKB22, both derived from JH642. OpuB transports choline with approximately1µM apparent affinity; it does not mediate native glycine-betaine uptake. Both complexes have four distinct subunit types: two ATPase copies, two membrane proteins and one tethered substrate-binding protein. PMID10216873 reports the OpuB protein sequences identical to the genome-project sequences; its two-residue discrepancy concerns OpuCC, not OpuBC. Thus the168 target is a justified reference for JH642 assays, without relabeling the actual assay strain. Source: https://www.uni-marburg.de/de/fb17/fachgebiete/mikrobiologie/ag-bremer/pdf-fuer-publikationen/058.pdf.

The earlier proV/proW/proX names and LH45 hybrid-strain sequence history do not establish the native cargo. Choline specificity is based on the1999 native transport tests and2011 binding study. Related OpuC proteins can share the same PANTHER subfamily as these OpuB proteins, so membership alone is not a cargo assignment or a test of native complex identity. An ATPase/permease may be interchangeable experimentally without making the native OpuB system a glycine-betaine importer.

PMID21658392 (Pittelkow et al.,2011) directly measures OpuBC/choline binding (Kd approximately30µM) and solves the ligand-bound binding domain. Its abstract states that the structure explains OpuB's inability to import glycine betaine. The ligand binding constant is not the same parameter as whole-cell OpuB uptake Km. The construct uses JH642 DNA, removes the signal sequence and changes the lipidated terminal cysteine; it is not an unmodified native membrane-tethered protein. The deposited3R6U entity matches canonical Q45462 residues23–306, although the paper-described terminal Cys-to-Gly change is absent from the deposited entity sequence. This construct discrepancy is preserved in opuBC-source-analysis; no unverified residue-specific mechanistic claims are made. Source: https://www.uni-marburg.de/de/fb17/fachgebiete/mikrobiologie/ag-bremer/pdf-fuer-publikationen/093.pdf.

Transport activities are attributed to the assembled importer. The core uses contributes_to_molecular_function GO0033266; OpuBA additionally supplies ATP hydrolysis, and OpuBC directly binds choline. Broad membrane/process/complex terms are refined in place. Missing complex membership and membrane-subunit contribution MF are proposed conservatively; no NEW biological-process row is manufactured from a deletion phenotype.

## PR6108 round1 evidence and ontology follow-up

Retain GO0055085 as ACCEPT alongside cargo transport, consistently with BetT and the other OpuB subunits. GO0015871 is not a membrane-crossing descendant; no suitable choline-specific transmembrane BP exists in the checked ontology. The choline-specific MF and membrane-subunit contribution remain precise. Summaries no longer duplicate their reasons.

All original machine and authored annotation payloads remain unchanged. Exact primary excerpts and source provenance are in BACSU/gbsB/gbsB-source-analysis/round1-primary-excerpts.txt; official term checks are in modules/bacterial_choline_to_glycine_betaine_biosynthesis-source-analysis/round1-ontology-evidence.yaml.
