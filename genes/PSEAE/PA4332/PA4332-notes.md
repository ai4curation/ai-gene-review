# PA4332 / SadC (Q9HW69) review notes

Unreviewed UniProt entry with no gene name, so the folder and gene_symbol use the
locus tag; the literature name is SadC. 487 aa: six UniProt TRANSMEM segments
(133-291) and a C-terminal GGDEF domain (352-483). The Kyte-Doolittle scan run
for wspR in this session (19-residue window, mean above 1.6) also finds these TM
helices (see wspR-notes.md).

## Literature (no deep-research provider available; own reading)

- Merritt et al. 2007 (PMID:17586642). Cached copy abstract only; full text
  (PMC2168701) read on the PMC web page, excerpts verbatim below. SadC is an
  inner-membrane DGC [PMID:17586642 "SadC (PA4332), an inner membrane-localized
  diguanylate cyclase"]. The deletion is defective in biofilm formation and
  hyperswarms; multicopy sadC promotes sessility [PMID:17586642 "Deletion of the
  sadC gene results in a strain that is defective in biofilm formation and a
  hyperswarmer, while multicopy expression of this gene promotes sessility."].
  It is also deficient in EPS production and has altered flagellar reversals.
  DGC activity: about 10-fold more c-di-GMP on overexpression, and a chimera
  carrying the SadC GGDEF domain makes c-di-GMP in vitro.
- McCarthy et al. 2017 (PMID:28263305; abstract only). WarA, a c-di-GMP-binding
  methyltransferase in the LPS O-antigen pathway, is a SadC partner
  [PMID:28263305 "Here, we identify an unrecognized SadC partner, WarA"]. Source
  of the GO:0005515 EXP row.
- Chen et al. 2016 (PMID:26991003; full text cached). The paper is about
  arsenate resistance by GAPDH and the efflux permease ArsJ; SadC, PA4332,
  c-di-GMP and biofilms are not mentioned (grep of the cached text). The
  abstract states the subject outright [PMID:26991003 "Synergistic interaction of
  glyceraldehydes-3-phosphate dehydrogenase and ArsJ, a novel organoarsenical
  efflux permease, confers arsenate resistance."]. The PseudoCAP IDA of
  GO:1900192 citing it is a wrong reference (CONFIRMED). The intended paper is
  unknown; the term itself is supported by PMID:17586642.
- Kulasakara et al. 2006 (PMID:16477007): PA4332 gave no detectable c-di-GMP in
  the PA14 overexpression screen ("PA4332 GGEEF —"), below the 12 pmol/mg
  detection limit; Merritt et al. note the disparity. Not cited by a PA4332 row.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002895344 | GO:0052621 diguanylate cyclase activity | 19 | 205 (28 taxa) | GO:0052621, IDA, PMID:17586642 (PseudoCAP) | SOUND | In vitro c-di-GMP synthesis by a SadC GGDEF chimera and by purified SadC-His, plus 10-fold c-di-GMP rise on overexpression (full text read). | E. coli DosC, DgcC, DgcJ, DgcM, DgcN, DgcQ, DgcZ and others; B. subtilis DgcK, DgcP; Shewanella Q8EGF8; P. aeruginosa dgcP, wspR, PA1107, PA2870, PA3177, PA3343, PA4843 | Yes. No GO_CENTRAL defect. |

Batch consistency: see wspR-notes.md.

## Other PseudoCAP rows (not IBD seeds)

- GO:1900192 IDA (PMID:26991003): wrong reference, PSEUDOCAP defect (CONFIRMED).
  Term kept (ACCEPT) on the strength of PMID:17586642.
- GO:0071978 swarming IMP (PMID:17586642): the deletion hyperswarms, so SadC
  represses swarming. GO has no "negative regulation of swarming motility" term
  (checked in go-basic.obo), so MODIFY to GO:1902201 negative regulation of
  bacterial-type flagellum-dependent cell motility, which the gene already
  carries by IBA. PSEUDOCAP WRONG_TERM defect, CONFIRMED (abstract states the
  hyperswarming outright).
- GO:0044010 biofilm formation IMP: SadC regulates biofilm formation through
  c-di-GMP (EPS production, flagellar reversals); MODIFY to GO:1900192.
  PSEUDOCAP WRONG_TERM defect, PROBABLE (it is a convention question whether a
  DGC is annotated to the process or its regulation).
- GO:0005515 EXP: REMOVE per protein-binding policy.

## Non-seed IBA node PTN002895351

Node-level GO_CENTRAL defects (plasma membrane; GO:0043709) are recorded once, on
wspR. SadC is a genuine inner-membrane protein, so the PM IBA is correct for it.
GO:0043709 IBA: MODIFY to GO:1900189 positive regulation of cell adhesion involved
in single-species biofilm formation (the deletion fails to attach stably).

## Verbatim excerpts from PMID:17586642 full text (PMC2168701, PMC web page)

- In an in vitro DGC assay, we also found that a chimera protein containing the GGDEF domain of SadC is able to generate c-di-GMP compared to a second chimera missing the first 21 amino acids of the cognate GGDEF domain of SadC.
- Expression of the sadC gene from a multicopy plasmid coincides with an approximately 10-fold increase in the amount of c-di-GMP detected compared to the vector control
- We found that SadC-His can be detected in the inner membrane but not the cytoplasmic fraction, in agreement with the computer prediction
- These data indicate that the Δ sadC mutant is defective in forming a stable association with the substratum compared to its parental strain.
