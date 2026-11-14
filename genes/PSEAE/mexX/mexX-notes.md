# mexX (PA2019, G3XD21) notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE G3XD21 --alias mexX`; accession matches the
worklist. Reviewed Swiss-Prot entry. No deep-research provider was used. Cached
papers: PMID:10543738 and PMID:16030228 have full text; PMID:10952562,
PMID:11083635 and PMID:15325256 are abstract-only (the PMC copies returned no
text). The PubMed MCP search returned API errors.

### Literature

- MexX is the periplasmic adaptor (membrane fusion protein, MFP) of the tripartite
  MexXY-OprM RND pump; it is a predicted inner-membrane lipoprotein (signal
  peptide 1-23, lipidated Cys24, UniProt).
- Discovery as an aminoglycoside efflux system in PAO1
  [PMID:10543738 "Antibiotic accumulation studies confirmed that this new system is an energy-dependent active efflux system that pumps out aminoglycosides."].
- Isogenic deletion mutants
  [PMID:10952562 "Loss of either MexXY or OprM from the MexAB-deficient mutant increased susceptibility to all agents tested"];
  MexX protein is induced by antibiotics
  [PMID:10952562 "Immunoblot analysis using anti-MexX polyclonal rabbit serum generated against synthetic oligopeptides detected expression of MexX in the PAO1 cells grown in medium containing tetracycline, erythromycin, or gentamicin"].
- Induction by ribosome-targeting antibiotics
  [PMID:16030228 "MexXY is an inducible efflux system that contributes to the natural resistance of Pseudomonas aeruginosa to antibiotics."].
  The assay measured mexY mRNA; mexX and mexY are one operon, so the induction
  applies to MexX (MexX protein induction is shown in PMID:10952562).
- Substrate range
  [PMID:11083635 "Extrusion of aminoglycosides is specific to MexXY-OprM"].
- Assembly specificity
  [PMID:15325256 "These results implied that the membrane fusion protein is central to the tripartite xenobiotic transporter assembly."].
- Repressed by MexZ (reviewed separately in `genes/PSEAE/mexZ`).

### Decisions

- ACCEPT: plasma membrane (IBA, IDA x2, IEA); efflux transmembrane transporter
  activity (IBA; MexX contributes as the adaptor); transmembrane transporter
  binding (IPI, MexY); xenobiotic detoxification by transmembrane export across the
  cell outer membrane (IBA); efflux pump complex (IDA).
- KEEP_AS_NON_CORE: response to antibiotic (6 rows: EXP x2, IMP x2, IBA, IEA),
  consistent with PA3677 (mexJ); periplasmic space (IEA).
- TOO_GENERAL: membrane (IDA, IEA); transmembrane transporter activity (IEA);
  transmembrane transport (IEA).
- REMOVE: protein binding (IPI, OprM), per the protein-binding policy.
- Counts: ACCEPT 8, KEEP_AS_NON_CORE 7, TOO_GENERAL 4, REMOVE 1.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001249140 | GO:0046677 response to antibiotic | 6 | 38 (12 taxa) | GO:0046677, IMP, PMID:10952562 (PseudoCAP) | SOUND | Abstract: isogenic mexXY deletion increases susceptibility of a MexAB-deficient strain to all agents tested. | E. coli AcrA (P0AE06; EcoCyc IMP PMID:8407802, IGI PMID:7651136), E. coli MdtE (P37636; EcoCyc IMP PMID:11566977, PMID:12937021), MexE (Q9I0Y9; UniProt IGI PMID:34680745), MexC (G3XD25; UniProt IGI PMID:12654738), MexA (P52477) | Yes |
| PTN001249140 | GO:0046677 response to antibiotic | 6 | 38 (12 taxa) | GO:0046677, EXP, PMID:10952562 (PseudoCAP) | SOUND | Same paper and claim as the IMP row; also shows MexX protein induced by tetracycline, erythromycin and gentamicin. EXP is a valid, less specific code. | as above | Yes |
| PTN001249140 | GO:0046677 response to antibiotic | 6 | 38 (12 taxa) | GO:0046677, EXP, PMID:16030228 (PseudoCAP) | SOUND | Full text read: mexXY is induced by ribosome-targeting antibiotics (mexY RT-PCR; operon). A genuine response to antibiotic. | as above | Yes |

The UniProt IMP row (PMID:10543738, full text read) supports the same term
independently. No PSEUDOCAP and no GO_CENTRAL defect. The node is a clade of
membrane fusion proteins of RND multidrug pumps (AcrA, AcrE, MdtE, MexA, MexC,
MexE, MexX); a resistance-phenotype process term suits it and rests on several
independent E. coli and P. aeruginosa seeds. This is the node-level assessment for
the batch; mexA (`genes/PSEAE/mexA/mexA-notes.md`) cross-references it.
