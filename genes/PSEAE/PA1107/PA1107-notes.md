# PA1107 / RoeA (Q9I4M8) review notes

## Summary of the literature

PA1107 (RoeA, regulator of exopolysaccharide A) is a 398-aa protein. UniProt
(Phobius) predicts five TM helices (31-197) and a C-terminal GGDEF domain (256-390).
My scan of the UniProt sequence finds the GGEEF motif at 305 and an RxxD I-site
candidate (RSSD) at 296. No EAL domain.

Literature search (Europe PMC "(PA1107 OR RoeA) AND aeruginosa", 2026-11-05; the
service returned 503 errors for most queries that day, and PubMed E-utilities
returned 500 errors). Primary data:

1. Kulasekara et al. 2006 [PMID:16477007]; full text read on PMC (PMC1413825).
   - DGC assay: "To detect DGC activity, cultures overexpressing genes that encode
     DGC-containing proteins were extracted and analyzed for c-di-GMP content".
   - Table 1: "PA1107 GGEEF +(35)" (pmol c-di-GMP per mg wet cell weight; detection
     limit 12).
   - Biofilm: "insertion in PA1107 , PA1181 , PA1433 , PA1727 , and PA3702 resulted
     in biofilm reduction" and overexpression of PA1107 gave pronounced pellicles.
2. Merritt et al. 2010 [PMID:20978535], full text cached. Named RoeA. Plasmid PA1107
   raised c-di-GMP 22-fold in a deletion background, the GGAAF mutant did not, and a
   PleD*-RoeA GGDEF chimera was active in vitro [PMID:20978535 "Both of these
   chimeras could be purified, but only the construct with the WT GGEEF domain
   demonstrated in vitro DGC activity (Fig. 2H)."]. Full-length purified RoeA was
   inactive in vitro. The deletion reduced biofilm and Pel production in PA14, and
   swarmed about 2-fold better than WT [PMID:20978535 "the ∆roeA mutant swarms ~2-fold
   better than the WT"], but flagellar reversal and swimming speed were unchanged.
3. Eilers et al. 2022 [PMID:35935233] (PAO1 deletion library): ΔroeA lowered global
   c-di-GMP but, unlike in PA14, increased flow-cell biomass [PMID:35935233 "Only four
   mutants exhibited elevated biomass measurements, namely PA0847 (Zhang et al.,
   2019), PA1107 (roeA; Cole and Lee, 2016), PA4367 and PA3825"]. The direction of the
   biofilm effect therefore depends on strain and assay.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002895344 | GO:0052621 diguanylate cyclase activity | 19 | 205 (28 taxa) | GO:0052621, IDA, PMID:16477007 and PMID:20978535 (PseudoCAP) | SOUND | Overexpression raised cellular c-di-GMP (35 pmol/mg; full text read). Merritt adds an LC-MS 22-fold rise that a GGAAF mutant abolishes and in vitro activity of a purified chimera carrying the RoeA GGDEF domain (full text read). | E. coli DosC, DgcC, DgcJ, DgcM, DgcN, DgcP, DgcQ, DgcZ (P0AA89, P0AAP1, P76237, P77302, P46139, P76245, P76330, P31129); B. subtilis DgcK, DgcP; Shewanella DgcS; P. aeruginosa PA3177, DgcP (PA5487), WspR, SadC (PA4332), GcbA (PA4843), plus PA3343 and PA2870 | Yes. Many seeds have purified-enzyme evidence (E. coli and B. subtilis DGCs, WspR). No GO_CENTRAL defect for the MF. |

The same verdict applies to PA3343 and PA2870, the other P. aeruginosa seeds in this
batch (see their notes).

### Node-level GO_CENTRAL defect for PTN002895351 (recorded here, once)

PA1107, PA3343 and PA2870 also receive IBAs from PTN002895351 (none of them seeds it):
GO:0043709 cell adhesion involved in single-species biofilm formation, GO:1902201
negative regulation of bacterial-type flagellum-dependent cell motility, and
GO:0005886 plasma membrane. The GO:0043709 IBD has a single seed, E. coli DgcZ
(P31129). A live QuickGO query (2026-11-05,
`annotation/search?geneProductId=P31129&goId=GO:0043709`) returned the seed as
`IMP PMID:19460094 EcoCyc acts_upstream_of_or_within`. The IBD upgrades that to
`involved_in`, which makes every DGC in the clade a participant in cell adhesion.
A DGC makes c-di-GMP that regulates adhesins; it does not adhere. The node term
does not suit the clade. Defect recorded on the PA1107 GO:0043709 row (most direct
evidence among the batch's DGCs), confidence PROBABLE; PA3343 and PA2870 cross-refer
here. The GO:1902201 and GO:0005886 IBDs on the same node are not challenged.

## Annotation decisions

- GO:0052621 (IBA, IEA, IDA x2): ACCEPT; core function.
- GO:0005886 (IBA, IEA): ACCEPT; five predicted TM helices.
- GO:0043709 IBA: MODIFY to GO:1900190 regulation of single-species biofilm
  formation (direction differs between PA14 and PAO1), with the GO_CENTRAL defect.
- GO:1902201 IBA: KEEP_AS_NON_CORE. The deletion swarms 2-fold better, but RoeA's
  main output is Pel production, and flagellar function is unchanged.

## Note on the PTN002895351 cell-adhesion defect (2026-11-05)

The GO_CENTRAL defect for the GO:0043709 IBD at PTN002895351 is recorded once, on genes/PSEAE/wspR, and covers PA1107, PA3343 and PA2870 too.
