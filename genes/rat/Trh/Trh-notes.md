# Trh (rat) review notes

## 2026-10-28 session

- Fetched with `just fetch-gene rat Trh`; UniProt P01150 (TRH_RAT, RGD:3903, GeneID 25569) as
  expected. 20 GOA rows.
- No deep-research provider available; literature synthesis written by hand in
  `Trh-deep-research-manual.md`.
- Only PMID:17760865 has full text cached; all other GOA papers are abstract-only.

### Decisions

- Core: GO:0008437 TRH activity (IBA/IEA/IDA, ACCEPT); secreted hormone (extracellular region rows
  ACCEPTED; GO:0005615 extracellular space is obsolete in the current GO release, so there is no
  more specific replacement); secretory granule IBA ACCEPT.
- NEW GO:2000614 positive regulation of TSH secretion. Comparator check: GHRH carries GO:0060124,
  CRH carries GO:0051461 (both with experimental evidence); the hormone itself is the signal that
  drives secretion (it does the work, unlike a substrate case), so the convention supports a
  ligand-level regulation term. Supported by mouse Trh KO (PMID:10628753) and review PMID:27515033.
- GO:0007189 ISO: REMOVE. Donor human row (UniProt IDA, PMID:35940204) is a TSHR/TSH structure
  paper; TRH is not studied. TRH receptors couple Gq/11. source_defects recorded against UniProt.
- GO:0007628 adult walking behavior ISO: donor is MGI IGI from PMID:8719807, an exogenous TRH
  anti-ataxia drug study in Rolling mouse Nagoya. MARK_AS_OVER_ANNOTATED, source defect (evidence
  code; pharmacology is not genetic interaction).
- GO:0001692 histamine metabolic process IDA: TRH regulates histamine turnover/HDC, it does not
  metabolise histamine; MARK_AS_OVER_ANNOTATED with WRONG_TERM source defect (no regulation-of
  histamine metabolism term found in OLS).
- GO:0042755 eating behavior IDA: MODIFY to positive regulation of feeding behavior GO:2000253
  (brainstem TRH stimulates intake; antibody evidence of endogenous role).
- IEP response-to rows (hypoxia, glucose, ethanol, corticosterone): changes in TRH content/release;
  MARK_AS_OVER_ANNOTATED.
- Neuromodulatory rows (glutamate, GABA, insulin, feeding): KEEP_AS_NON_CORE.
