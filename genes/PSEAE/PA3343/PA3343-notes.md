# PA3343 / HsbD (Q9HYQ2) review notes

## Summary of the literature

PA3343 (HsbD) is a 389-aa protein with six predicted TM helices (UniProt Phobius,
52-204; MASE8 domain, Pfam PF20968) and a C-terminal GGDEF domain (252-389). My scan
of the UniProt sequence finds the GGEEF motif at 302 and an RxxD I-site (RPLD) at
293.

Literature search (Europe PMC, 2026-11-05, mostly 503 errors; PubMed web search
"HsbD aeruginosa" returned PMID:27792789). Primary data:

1. Kulasekara et al. 2006 [PMID:16477007]; full text read on PMC (PMC1413825).
   - Table 1: "PA3343 GGEEF +(22) PA3702 GGEEF +(445) PA3825 EVL +(27)" (pmol
     c-di-GMP per mg wet cell weight in extracts of overexpressing PA14; detection
     limit 12).
   - "pellicle formation (hyperbiofilm) was observed for insertions in PA0861 ,
     PA3311 , PA3343 , PA4332 , PA4367 , and PA5017".
   - "P. aeruginosa expressing PA2870 and PA3343, two DGCs that produce high levels
     of c-di-GMP in our assay ( Table 1 ), do not cause an alteration in the biofilm
     phenotype."
2. Valentini et al. 2016 [PMID:27792789], full text cached. Named HsbD; links it to
   the HptB-HsbR-HsbA pathway. Congo-red staining of E. coli expressing HsbD, lost
   with a GGAAF active-site mutant; I-site c-di-GMP binding by DRaCALA. In a ΔhptB
   background hsbD deletion lowers c-di-GMP and abolishes the hyperbiofilm phenotype
   (complemented), and the ΔhptBΔhsbD mutant hyper-swarms about 9-fold. ΔhsbD is
   deficient in chemotaxis and twitching. HsbD-YFP localises to the cell periphery
   with polar foci. Note: the paper states that PA3343 made 445 pmol/mg in
   Kulasekara's assay [PMID:27792789 "with 445 pmol of c-di-GMP produced per mg of
   wet cell weight"]; Table 1 of PMID:16477007 gives 22 for PA3343 and 445 for the
   next row, PA3702 (WspR). The citation misreads the table by one row; it does not
   affect the conclusion that PA3343 is active.
3. Eilers et al. 2022 [PMID:35935233]: ΔhsbD slightly increased attachment
   [PMID:35935233 "Three of the mutants in a putative dgc gene resulted in a slight
   upregulation of attachment (fold change ranging between 1.2 and 1.4): PA2771
   (dcsbis; Chen et al., 2016), PA3343 (hsbD; Valentini et al., 2016) and most
   significantly PA4396."].

The direction of HsbD's effect on biofilm differs by background: positive in ΔhptB
(PMID:27792789), negative or neutral in single mutants (PMID:16477007,
PMID:35935233).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002895344 | GO:0052621 diguanylate cyclase activity | 19 | 205 (28 taxa) | GO:0052621, IDA, PMID:16477007 (PseudoCAP) | SOUND | Extracts of the overexpressing strain contained 22 pmol c-di-GMP/mg, above the 12 pmol detection limit (full text read). Valentini 2016 confirms activity with a GGAAF control in E. coli (full text read). | E. coli DosC, DgcC/J/M/N/P/Q/Z; B. subtilis DgcK, DgcP; Shewanella DgcS; P. aeruginosa WspR, SadC, GcbA, DgcP, PA3177, PA1107, PA2870 | Yes; see PA1107 notes. No GO_CENTRAL defect for the MF. |

PTN002895351 (GO:0043709 IBD): the node-level GO_CENTRAL defect is recorded once in
PA1107-ai-review.yaml (see PA1107 notes); not repeated here.

## Annotation decisions

- GO:0052621 (IBA, IEA, IDA): ACCEPT; core function.
- GO:0005886 (IBA, IEA): ACCEPT; six TM helices, YFP fusion at the cell periphery.
- GO:0043709 IBA: MODIFY to GO:1900190 (sign depends on background).
- GO:1902201 IBA: ACCEPT; ΔhptBΔhsbD hyper-swarms, so HsbD restrains swarming.
