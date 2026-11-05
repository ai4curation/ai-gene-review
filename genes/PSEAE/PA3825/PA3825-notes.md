# PA3825 (Q9HXH7) review notes

## Summary of the literature

PA3825 is a 526-aa protein. UniProt (Phobius) predicts two TM helices (12-35 and
235-254) flanking a CSS-motif domain (Pfam PF12792), followed by a C-terminal EAL
domain (258-512). The EAL signature is the variant EVL (residues 293-295 in my scan
of the UniProt sequence, "GVEVLMRW"), and the catalytic DDFGTG loop is intact
(residue 414). UniProt FT BINDING rows (ECO:0007829, PDB 4Y9P, 5MF5, 5MFU, 4Y8E)
place c-di-GMP and Mg/Mn/Ca ions in the EAL active site.

Literature search (Europe PMC, query "PA3825 AND aeruginosa", 2026-11-05, 24 hits;
PubMed E-utilities returned server errors that day). Primary data on PA3825:

1. Kulasekara et al. 2006 [PMID:16477007] (PseudoCAP source of the IDA row). Cached
   copy is abstract-only; I read the full text on PMC (PMC1413825). Verbatim excerpts:
   - Assay: "The ability of the PDE-containing proteins to hydrolyze c-di-GMP was
     tested by adding synthetic c-di-GMP to lysates of strains overexpressing these
     proteins and measuring the disappearance of the dinucleotide from the reaction
     mixture".
   - Table 1: "PA3343 GGEEF +(22) PA3702 GGEEF +(445) PA3825 EVL +(27) PA3947 EVL
     +(100)" (PDE activity as percent of added c-di-GMP degraded).
   - Footnote: "Given the limits of sensitivity of the HPLC assay (12 pmol/mg cell
     wet weight), we cannot conclude that any particular DGC or PDE domain does not
     have the corresponding enzymatic activity in vivo".
2. Bellini et al. 2017 [PMID:28186120], full text cached. The purified EAL domain is
   an active c-di-GMP PDE [PMID:28186120 "In vitro PA3825EAL was able to convert
   c-di-GMP to pGpG, with a kcat of 0.35 ± 0.1 s−1, in the presence of Mn2+"]. Crystal
   structures with substrate/product reveal a third metal site. The knockout had no
   motility phenotype [PMID:28186120 "Neither swimming, swarming, nor twitching
   motilities were affected in the PA3825 knockout strain under conditions tested."].
   The paper calls PA3825 "a two-domain cytoplasmic protein", which conflicts with the
   two predicted TM helices; the CSS domain is predicted to resemble periplasmic
   sensor domains, which fits a membrane topology.
3. Eilers et al. 2022 [PMID:35935233], PAO1 deletion library, full text cached.
   Deletion raised early attachment [PMID:35935233 "Out of the 8 proteins in this
   category, deletion of two genes encoding EAL-harboring enzymes, PA2200 and PA3825,
   resulted in elevated attachment levels, as would be expected for genes encoding
   PDEs"] and flow-cell biomass [PMID:35935233 "Only four mutants exhibited elevated
   biomass measurements, namely PA0847 (Zhang et al., 2019), PA1107 (roeA; Cole and
   Lee, 2016), PA4367 and PA3825"]. So PA3825 restrains biofilm formation.
4. Scherhag et al. 2023 (PMID:37441524; PMC10335732 Table 1, read on PMC, not cited
   in the YAML because the cached text omits the table) lists PA3825 as a
   cytoplasmic-membrane ("cm") protein found in their membrane proteome.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002105365 | GO:0071111 cyclic-guanylate-specific phosphodiesterase activity | 18 | 162 (24 taxa) | GO:0071111, IDA, PMID:16477007 (PseudoCAP) | SOUND | Lysates of the overexpressing strain degraded 27% of added c-di-GMP (full text read). Weak and crude, but later confirmed by purified-EAL-domain kinetics and substrate-bound crystal structures (PMID:28186120). | E. coli PdeA/B/C/F/H/I/K/L/N, DosP; Mtb P9WM13; P. aeruginosa bifA, rocR, PA2133, PA2200, nbdA, PA2567 | Yes. Many seeds have purified-enzyme evidence. Node-level defects (degenerate EAL leaves; PM term on soluble members) are recorded once in rocR-ai-review.yaml and not repeated here. |

PA3825 is not a seed of PTN009140332 (GO:1900190), but inherits its IBA. The IBD
stands on bifA (see bifA, PA2133 and arr notes). PA3825 has its own supporting data:
the deletion increases attachment and biomass (PMID:35935233).

No PSEUDOCAP or GO_CENTRAL defects recorded for PA3825.

## Annotation decisions

- GO:0071111 (IBA, IEA, IDA): ACCEPT; core function.
- GO:0005886 (IBA is_active_in, IEA located_in): ACCEPT; two predicted TM helices,
  found in the membrane proteome.
- GO:1900190 IBA: ACCEPT. Deletion phenotypes (more attachment and biomass) show
  that PA3825 regulates (negatively) biofilm formation.
