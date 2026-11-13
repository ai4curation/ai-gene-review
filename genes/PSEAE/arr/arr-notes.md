# arr / PA2818 (Q9I025) review notes

## Summary of the literature

Arr (aminoglycoside response regulator) is a 525-aa protein. UniProt (Phobius)
predicts two TM helices (12-33 and 240-259) flanking a CSS-motif domain (Pfam
PF12792), followed by a C-terminal EAL domain (262-514). My scan of the UniProt
sequence finds an intact EAL motif ("GVEALVRW", E at 297) and DDFGTG loop (416). The
gene lies on a genomic island near tRNA genes and is absent from PA14 and most
strains tested (PMID:16477007).

Literature search (Europe PMC, 2026-11-05; PubMed web search for "aminoglycoside
response regulator arr" returned PMID:16121184 plus two unrelated hits; E-utilities
returned server errors that day).

1. Hoffman et al. 2005 [PMID:16121184], Nature, abstract only (not in PMC). The
   PseudoCAP source of all three experimental rows. The abstract states that arr is
   needed for aminoglycoside-induced biofilm [PMID:16121184 "In P. aeruginosa, a
   gene, which we designated aminoglycoside response regulator (arr), was essential
   for this induction and contributed to biofilm-specific aminoglycoside
   resistance."], that it is a predicted inner-membrane c-di-GMP PDE, and that
   [PMID:16121184 "membranes from arr mutants had diminished c-di-GMP
   phosphodiesterase activity, and P. aeruginosa cells with a mutation changing a
   predicted catalytic residue of Arr were defective in their biofilm response to
   tobramycin."]
2. Kulasekara et al. 2006 [PMID:16477007]; full text read on PMC (PMC1413825).
   Verbatim excerpts:
   - Table 1: "PA2771 GGEEF — PA2818 EAL — PA2870 GGEEF +(96)". So lysates of a
     PA14 strain overexpressing arr showed no detectable c-di-GMP hydrolysis. This is
     the one PDE-only protein with no activity: "c-di-GMP hydrolysis was detected in
     all but one strain expressing genes encoding PDE enzymes".
   - The authors' own caveat: "Given the limits of sensitivity of the HPLC assay (12
     pmol/mg cell wet weight), we cannot conclude that any particular DGC or PDE
     domain does not have the corresponding enzymatic activity in vivo".
   - Phylogeny: "Three of these putative PDE modules, in PA2200, PA2818, and PA3285,
     appear to be more closely related and are not linked to DGCs."
   The negative result does not refute the activity: the motif is intact, Hoffman
   measured loss of membrane PDE activity in the mutant, and the lysate assay may
   miss a membrane protein that is poorly expressed or inactive without its signal.
   It does mean no purified-enzyme or overexpression evidence of activity exists.
3. Eilers et al. 2022 [PMID:35935233]: deletion of PA2818 disrupted mushroom
   structures [PMID:35935233 "deletion of PA2133 (fcsR; Rossello et al., 2017), PA2200
   and PA2818 resulted in the disruption of mushroom-like biofilm structures"].

### Bearing of the Kulasakara negative result on seeding

Arr is NOT a seed of PTN002105365 (GO:0071111): Q9I025 is absent from that IBD's
WITH/FROM in `.cache/paint/IBD.gaf`, because arr's own PDE row is GO:0004114, not
GO:0071111. The lysate result therefore bears only on arr's own MF rows, not on the
PDE IBD. Arr IS one of four seeds of PTN009140332 (GO:1900190), through its
biofilm row; that seeding rests on Hoffman's genetics, not on the lysate assay.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN009140332 | GO:1900190 regulation of single-species biofilm formation | 4 | 84 (9 taxa) | GO:1900190, IDA, PMID:16121184 (PseudoCAP) | SOUND | The abstract states that arr is essential for tobramycin-induced biofilm formation and that a catalytic-residue mutant is defective in this response, so Arr regulates biofilm formation through its own enzyme activity. The evidence described is genetic (IMP rather than IDA), but the term is right. Abstract only; full text not available. | bifA (Q9HW35; SOUND, deletion + complementation + catalytic mutants), PA2133 (Q9I1Y2; INDIRECT-PHENOTYPE), E. coli PdeF (P77172) | Yes. It stands on bifA as well (see bifA and PA2133 notes). No GO_CENTRAL defect. |

Other PseudoCAP row: GO:0004114 3',5'-cyclic-nucleotide phosphodiesterase activity
(IDA, PMID:16121184) is not a seed but uses the wrong term. GO:0004114 is defined on
3',5'-cyclic nucleoside monophosphates and is not an ancestor of GO:0071111
(go-basic.obo: GO:0071111 is_a GO:0008081). The abstract names c-di-GMP as the
substrate. PSEUDOCAP WRONG_TERM defect, CONFIRMED (abstract states the substrate;
term relationship checked in the ontology file).

## Annotation decisions

- GO:0004114 IDA: MODIFY to GO:0071111, with a PSEUDOCAP WRONG_TERM defect.
- GO:0071111 (IBA, IEA): ACCEPT; core function (motif intact, mutant membranes lose
  PDE activity), with the Kulasakara negative result noted.
- GO:0005886 (IBA, IEA): ACCEPT; two TM helices, inner-membrane prediction.
- GO:1900190 (IDA seed, IBA): ACCEPT.
- GO:0046677 response to antibiotic (IMP): ACCEPT; this is the defining phenotype.
