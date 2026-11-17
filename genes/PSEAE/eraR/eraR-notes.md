# eraR (PA1980, Q9I2C7) review notes

## Literature

- The PseudoCAP-cited paper is a short review by Görisch on ethanol oxidation in P. aeruginosa strain ATCC 17933 (not PAO1). It describes a two-component system controlling the quinoprotein ethanol dehydrogenase (exaA) promoter [PMID:12686116 "Transcription from the QEDH (exaA) promoter is regulated by a two component system: a histidine sensor kinase (ExaD), which is presumably located in the cytoplasm, and a response regulator (ExaE)."], within a hierarchy of regulators [PMID:12686116 "seven different genes in an hierarchical organization may be involved in regulating the transcription of the ethanol oxidation system and components of acetate metabolism in P. aeruginosa."].
- The abstract names ExaE, not eraR or PA1980. The PseudoCAP curator attributed the row to PA1980 (EraR), the response regulator adjacent to the sensor kinase in the ethanol-oxidation regulatory locus; the abstract alone cannot confirm that mapping.
- Domain architecture (UniProt Q9I2C7): receiver domain (PF00072) plus LuxR-type HTH (GerE, PF00196); PANTHER PTHR43214 (NarL/FixJ family), the same PAINT node as rocA1.

Search: PubMed metadata for the GOA-cited PMID (abstract only; review article, no PMC copy). NCBI E-utilities and Europe PMC search were unavailable (HTTP 500/503) during this session, so the primary Görisch-laboratory papers on the exa regulators could not be retrieved to confirm the ExaE = PA1980 mapping.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN008449896 | GO:0006355 regulation of DNA-templated transcription | 9 | 167 (26 taxa) | GO:0045893, IMP, PMID:12686116 | UNVERIFIABLE | A review abstract (strain ATCC 17933) stating that the response regulator ExaE controls exaA transcription; the mapping of ExaE to PA1980 and the mutant data behind the IMP are not visible in the abstract. Nothing positively indicates an error, and the claim fits the domain architecture, so the row is kept and no defect is filed. | NarL, NarP, UhpA, RcsB, BglJ (E. coli), DegU (B. subtilis), NarL (P. aeruginosa), rocA1 | Yes |

Node-level verdict for PTN008449896 (IBD sound on seven characterised regulators; no GO_CENTRAL defect) is recorded once in `genes/PSEAE/rocA1/rocA1-notes.md`.
