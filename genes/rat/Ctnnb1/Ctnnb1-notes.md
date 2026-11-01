# Ctnnb1 (rat) review notes

## Setup (2026-10-28)

- `just fetch-gene rat Ctnnb1` resolved Q9WU82 (CTNB1_RAT, Swiss-Prot,
  RGD:70487, GeneID 84353). GOA file keyed to Q9WU82; 420 rows seeded.
- `just fetch-gene-pmids rat Ctnnb1` cached 34 papers; PMID:20042609 cached
  (full text). Most rat papers are abstract-only; full text for
  PMID:20042609, 16682528, 16690606, 20097766, 29224185.
- No deep-research provider available; manual synthesis in
  `Ctnnb1-deep-research-manual.md`.

## Annotation profile

- 294 ISO rows (mostly MGI mouse Ctnnb1, some human P35222), 47 ISS, 12 IBA,
  12 IEA, and ~60 rat experimental rows (IDA/IPI/IEP/IMP/EXP/TAS/NAS).
- The existing human and mouse reviews were consulted for consistency.

## Key decisions

- Core: cadherin binding, alpha-catenin binding, transcription coactivator
  activity, RNA Pol II-specific DNA-binding TF binding (TCF/LEF); canonical Wnt
  signalling; positive regulation of transcription by RNA Pol II; cell-cell
  adhesion (cadherin-mediated), adherens junction assembly/organization;
  adherens junction, catenin complex, beta-catenin-TCF complex, nucleus,
  cytoplasm/cytosol, plasma membrane, destruction complex.
- Developmental ISO rows: KEEP_AS_NON_CORE (downstream Wnt-transcription
  consequences; supported in mouse genetics).
- Over-general terms (cell junction, anchoring junction, membrane, cell
  periphery, protein-containing complex, transcription regulator complex,
  DNA-binding TF binding, regulation of transcription by RNA Pol II, positive
  regulation of DNA-templated transcription) -> MODIFY to the specific term.
- Bare protein binding (4 IPI): Fat1 row MODIFY to cadherin binding (Fat1 is
  a cadherin; PMID:16682528); the Axin, p35 and GSK3B rows REMOVE as
  uninformative (the interactions themselves are real).
- Substrate-role process rows (protein polyubiquitination; proteasome-mediated
  ubiquitin-dependent protein catabolic process) REMOVE: beta-catenin is the
  substrate, it does not perform these steps (consistent with the human review).
- IEP rows that only record a change in beta-catenin level after systemic
  manipulation (zinc-deficient diet, treadmill exercise, epididymis
  development) MARK_AS_OVER_ANNOTATED.
- Source defects recorded: TAS cell-cell adhesion from PMID:20299672 (a review
  on coronary vasculogenesis whose abstract does not mention beta-catenin);
  IMP cellular response to IGF stimulus from PMID:20042609 (the paper perturbs
  IGF-IR/AKT/ER pharmacologically, not beta-catenin).
- No NEW terms proposed.
