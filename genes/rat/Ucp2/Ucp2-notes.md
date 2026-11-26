# Ucp2 (rat) review notes

## 2026-10-26 - initial review

- Fetched with `just fetch-gene rat Ucp2`; UniProt P56500 confirmed. 102 GOA rows, most of them ISO/ISS/IEA
  transfers from human (P55851) and mouse (P70406) UCP2; rat experimental rows are IDA (PMID:12372827), IMP
  (PMID:18703058, PMID:21172424) and a set of IEP expression studies.
- Literature synthesis in `Ucp2-deep-research-manual.md` (no deep-research API available).
- Decisions follow the human UCP2 review for consistency across orthologues:
  - Core: dicarboxylate:phosphate antiporter activity (GO:0015364) in the mitochondrial inner membrane;
    malate/oxaloacetate/aspartate transport terms accepted [PMID:24395786 "UCP2 reconstituted in lipid vesicles
    catalyzed the exchange of malate, oxaloacetate, and aspartate for phosphate plus a proton"].
  - Proton transport, chloride, sulfate, phosphate uniport, fatty-acid transport, GDP binding: kept non-core.
  - Oxidative phosphorylation uncoupler activity, response to cold, adaptive thermogenesis (IBA from UCP1 node):
    marked over-annotated.
  - Expression-only IEP rows (lead, dexamethasone, liver regeneration, amino-acid starvation) marked
    over-annotated; nutrient/hormone response IEP rows kept non-core.
  - PMID:18692019 (full text read): glutamine omission lowers UCP2 protein translationally [PMID:18692019
    "Omission of glutamine from the medium resulted in decreases in UCP2 in cells and mitochondria"]; the
    "cellular response to amino acid starvation" IEP was therefore judged over-annotation (UCP2 is regulated,
    not a participant).
  - Negative regulation of calcium import into mitochondrion (from human IDA): UNDECIDED, as in human review.
- No NEW annotations proposed; nothing passed the participation bar beyond existing terms.
