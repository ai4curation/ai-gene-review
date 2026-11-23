# PA3177 (Q9HZ57) review notes

Unreviewed UniProt entry, no gene name; folder and gene_symbol use the locus tag.
307 aa, C-terminal GGDEF domain (UniProt DOMAIN 177..307, Pfam PF00990), GGEEF
active-site motif. No TRANSMEM feature; a Kyte-Doolittle scan (19-residue window,
mean above 1.6, run in this session) finds no hydrophobic window, so the protein
is predicted soluble. The UniProt "Cell inner membrane" location rests on an ARBA
rule only.

## Literature (no deep-research provider available; own reading)

- Poudyal & Sauer 2018 (PMID:30082282; full text cached and read).
  - A PA3177 deletion has 5-fold less c-di-GMP in biofilm cells; multicopy
    PA3177 restores it, but the GGAAF active-site mutant does not
    [PMID:30082282 "Inactivation of PA3177 reduced total cellular c-di-GMP levels
    5-fold under biofilm growth conditions"] [PMID:30082282 "In contrast,
    multicopy expression of the variant gene PA3177_GGAAF harboring a
    substitution of the active-site motif, had no effect on the c-di-GMP level
    of PA3177 mutant biofilms"].
  - No effect on planktonic c-di-GMP, and none on attachment or biofilm
    formation [PMID:30082282 "While PA3177 contributed to biofilm drug
    tolerance, inactivation of PA3177 had no effect on attachment and biofilm
    formation."].
  - Motility: the deletion swims and swarms like wild type; only overexpression
    reduces motility, GGEEF-dependently [PMID:30082282 "In contrast,
    overexpression of PA3177 resulted in reduced swarming, while multicopy
    expression of variant gene PA3177_GGAAF harboring a substitution of the
    active-site motif had no effect on swarming"].
  - PA3177-made c-di-GMP is needed for BrlR levels and DNA binding, and so for
    biofilm tolerance to tobramycin and H2O2.
- Kulasakara et al. 2006 (PMID:16477007; full text read on PMC, see
  wspR-notes.md): PA3177 gave no detectable c-di-GMP when overexpressed in PA14
  ("PA3177 GGEEF —"), but the authors note the HPLC detection limit (12 pmol/mg)
  and do not conclude inactivity. Not cited by any PA3177 GOA row.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002895344 | GO:0052621 diguanylate cyclase activity | 19 | 205 (28 taxa) | GO:0052621, IMP, PMID:30082282 (PseudoCAP) | SOUND | Deletion lowers biofilm c-di-GMP 5-fold; complementation restores it, the GGAAF active-site mutant does not (full text read). | E. coli DosC, DgcC, DgcJ, DgcM, DgcN, DgcQ, DgcZ and others; B. subtilis DgcK, DgcP; Shewanella Q8EGF8; P. aeruginosa dgcP, wspR, PA1107, PA2870, PA3343, PA4332, PA4843 | Yes. Many seeds have direct activity evidence (e.g. WspR purified enzyme, PMID:16186483). No GO_CENTRAL defect. |

Batch consistency: all five genes in this batch seed PTN002895344; every seed row
is SOUND except the wspR IMP (PMID:12426335, INDIRECT-PHENOTYPE), which does not
affect the node.

## Non-seed IBA node PTN002895351

PA3177 receives the plasma membrane, GO:0043709 and GO:1902201 IBAs from
PTN002895351 (seeded by E. coli proteins only). The node-level GO_CENTRAL defects
(PM; GO:0043709) are recorded once, on wspR (see wspR-notes.md). For PA3177:

- PM IBA and IEA: MARK_AS_OVER_ANNOTATED (no TM segment).
- GO:0043709 IBA: REMOVE. The deletion has no effect on attachment or biofilm
  formation, so the inferred adhesion role is contradicted for this gene.
- GO:1902201 IBA: KEEP_AS_NON_CORE. Supported only by overexpression; the
  deletion is not hypermotile.
