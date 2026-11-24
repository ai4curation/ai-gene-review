# pyrE (PA5331, P50587) review notes

No deep-research provider was available. Sources: reviewed UniProt record (HAMAP MF_01208),
cached abstracts of PMID:25917504 (P. aeruginosa pyrE deletion) and PMID:9222315 (E. coli
OPRTase purification, title only). PubMed and Europe PMC searches failed on 2026-11-05.

## Function

- Orotate phosphoribosyltransferase: PRPP + orotate to OMP, step 1 of UMP synthesis from orotate
  [file:PSEAE/pyrE/pyrE-uniprot.txt "Catalyzes the transfer of a ribosyl phosphate group from 5-phosphoribose 1-diphosphate to orotate, leading to the formation of orotidine monophosphate (OMP)."].
- Deletion of pyrE in PAO1 causes orotate accumulation and altered virulence-factor output
  [PMID:25917504 "The pyrE mutant accumulated orotate and exhibited decreased production of hemolysin, casein protease, and elastase."].
  Orotate accumulation is the direct metabolic signature of losing OPRTase; the virulence changes
  are downstream effects of the accumulated orotate.

## GO term choices

- GO:0044205 'de novo' UMP biosynthetic process (IEA, UniPathway) is the specific process; it is_a
  pyrimidine nucleotide biosynthetic process (GO:0006221), so the GO:0006221 rows are TOO_GENERAL.
- GO:0006207 'de novo' pyrimidine nucleobase biosynthetic process and GO:0046132 pyrimidine
  ribonucleoside biosynthetic process (IBA, from yeast URA5/URA10 seeds) do not describe the OPRTase
  step: orotate is already the nucleobase and the product is a nucleotide, not a nucleoside. Both
  are modified to GO:0044205 at the leaf; neither is a seed from this gene.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002928258 | GO:0004588 orotate phosphoribosyltransferase activity | 5 | 26 (25 taxa) | GO:0004588, IMP, PMID:25917504 (PseudoCAP) | SOUND | The deletion accumulates orotate, the OPRTase substrate; together with the HAMAP family assignment this supports the activity. | E. coli PyrE P0A7E3, S. cerevisiae URA5 and URA10 (SGD:S000004574, S000004884), A. nidulans Q5B0P6 | Yes; E. coli PyrE and the yeast enzymes are biochemically characterised. No GO_CENTRAL defect. |
| PTN002928258 | GO:0006221 pyrimidine nucleotide biosynthetic process | 2 | 26 (25 taxa) | GO:0006221, IMP, PMID:25917504 (PseudoCAP) | SOUND | Correct (general) process for an enzyme of de novo UMP synthesis; the mutant blocks the pathway at orotate. | E. coli PyrE P0A7E3 | Yes, on E. coli PyrE. The term is general (leaf rows judged TOO_GENERAL given GO:0044205) but true for the clade. No GO_CENTRAL defect. |

Defects recorded: PSEUDOCAP 0; GO_CENTRAL 0.
