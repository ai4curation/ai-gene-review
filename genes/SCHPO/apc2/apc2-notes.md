# apc2 (SPBP23A10.04, UniProt Q874R3) - curation notes

Fission yeast Apc2, the cullin-family subunit of the anaphase-promoting
complex/cyclosome (APC/C). Ortholog of S. cerevisiae Apc2 (Q12440) and human
ANAPC2 (Q9UJX6). Not to be confused with S. cerevisiae APC2, which has its own
completed review in `genes/yeast/APC2/`, nor with the metazoan adenomatous
polyposis coli paralog "APC2".

## Sources used

- `apc2-uniprot.txt` (entry version 135, 681 aa; "Belongs to the cullin family";
  SUBUNIT lists the 13-subunit S. pombe APC/C from PMID:12477395).
- `apc2-deep-research-falcon.md` (Edison; 33 citations, mainly Yoon 2002, Ohi
  2007, Tang 2001, Ors 2009, Hofler 2024). Ohi et al. 2007 (Mol Cell 28:871)
  and Ors et al. 2009 (JBC 284:23989) are NOT in the publications cache, so
  statements from them are cited through the deep-research file.
- Cached publications: PMID:12477395 (abstract only), PMID:15060174 (full text),
  PMID:16823372 (abstract only), PMID:20924356 (full text, S. pombe Cut9
  structure paper with an APC/C architecture introduction), PMID:9264466
  (abstract only, S. pombe 20S APC/cyclosome), PMID:11739784 (abstract only,
  human APC2/APC11 minimal ligase), PMID:10888670 (full text, budding yeast
  Apc11 RING), PMID:19822757 (full text, human E2 module, comments on yeast).

## Identity and complex membership

- Yoon et al. 2002 (PMID:12477395) used TAP purification and DALPC mass
  spectrometry on the S. pombe APC/C and raised the subunit count to 13 in both
  yeasts [PMID:12477395 "Our data increase the total number of identified APC
  subunits to 13 in both yeasts and indicate that previous approaches were
  biased against the identification of small subunits."]. The deep research
  records that Apc2 was recovered with 19 and 24 unique peptides in Lid1-TAP
  and Apc13-TAP preparations [file:SCHPO/apc2/apc2-deep-research-falcon.md
  "Apc2 yielded 19 unique tryptic peptides in a Lid1-TAP preparation and 24 in
  an independent Apc13-TAP preparation."].
- Schwickart et al. 2004 (PMID:15060174) purified Cut9-TAP and Apc13-TAP from
  fission yeast and recovered the same set of known/predicted APC/C subunits
  [PMID:15060174 "Mass spectrometric analysis of the Cut9-TAP purification
  identified 10 proteins known or predicted to be APC/C subunits"]. This is
  the basis of the second PomBase IDA for GO:0005680.
- UniProt SUBUNIT: "The APC/C is composed of at least 13 subunits: apc1, apc2,
  nuc2, apc4, apc5, cut9, apc8, apc10, apc11, hcn1, apc13, apc14 and apc15."
- Ohi et al. 2007 (via deep research): one Apc2 copy per particle (differently
  tagged Apc2 did not self-co-IP); 27 A cryo-EM map of APC/C-Slp1 places the
  Apc2-Apc11-Apc10 catalytic region on the lower/right side with Slp1 nearby
  [file:SCHPO/apc2/apc2-deep-research-falcon.md "Mapping placed the
  Apc2–Apc11–Apc10 catalytic region along the right/lower side of the complex,
  with Apc11 near the cavity lip and Slp1 near the lower horn-like region."].

## Molecular role: cullin scaffold of the catalytic module

- Zhang et al. 2010 (PMID:20924356, S. pombe Cut9 paper): "The catalytic centre
  of the APC/C is formed from the cullin and RING subunits Apc2 and Apc11,
  analogous to Cul1 and Rbx1, respectively, of the SCF cullin RING ligase." and
  "the N-terminus of Apc2 comprises three consecutive ∼130 residue cullin
  repeats"; Apc1 "links the catalytic subcomplex formed from Apc2, Apc11 and
  Apc10/Doc1 with the TPR subunits".
- Schwickart 2004: "Apc11 is anchored to the complex through Apc2, a subunit
  distantly related to cullins".
- Tang et al. 2001 (PMID:11739784, human): "Both APC11 and UbcH10 bind to the
  C-terminal cullin homology domain of APC2, whereas Ubc4 interacts with APC11
  directly." and the APC2/APC11 module "does not possess substrate specificity".
- Leverson et al. 2000 (PMID:10888670, budding yeast): "While Apc2p was not
  required to effect ubiquitin transfer in vitro, it may function in a cellular
  context to tether Apc11p to APC core proteins, and to properly position the
  Apc11p RING-H2 finger with respect to its substrates."
- Conclusion: Apc2 has no catalytic chemistry of its own; it is the cullin-like
  platform that holds the Apc11 RING (and, via the Apc1 bridge, the rest of the
  complex) so that E2~Ub can be presented to coactivator-bound substrates. The
  matching GO MF is GO:0160072 ubiquitin ligase complex scaffold activity, with
  Apc2 contributing to (not enabling) GO:0061630. Comparator check: GO:0160072
  is carried by the canonical cullins CUL1-5 (PAINT IBA, node PTN002631076) and
  was adopted for human ANAPC2 and S. cerevisiae Apc2 in this repository.

## Process

- The S. pombe 20S APC/cyclosome "contains ubiquitin ligase activity required
  for cyclin and Cut2 destruction" [PMID:9264466].
- Coactivators: Slp1 (Cdc20) in mitosis, Ste9/Srw1 (Cdh1) in G1, Mfr1 in
  meiosis (ComplexPortal variants CPX-764/765/766 listed in UniProt).
- E2s: fission yeast Ubc4 and Ubc11 (UbcP4, the UbcH10/UBE2C orthologue)
  [file:SCHPO/apc2/apc2-deep-research-falcon.md "In fission yeast, Ubc4 and
  Ubc11 contribute to different aspects of cyclin-B ubiquitylation."]. No
  Ube2S-type K11 chain-elongating E2 has been characterised for the fission
  yeast APC/C, and the ubiquitin-chain linkage built by the S. pombe complex has
  not been determined. In budding yeast the APC/C-Ubc4/Ubc1 system makes
  K48-linked chains [PMID:19822757 "However, Ubc4 and Ubc1 function
  sequentially to assemble K48-linked ubiquitin chains, whereas human UbcH10
  and Ube2S most likely bind APC/C at the same time."].
- Atf1 binds and stimulates the APC/C in vitro (Ors 2009, via deep research);
  regulatory, not an Apc2-specific function.

## Localisation

- HDA rows (nucleus, cytosol) come from the Matsuyama 2006 ORFeome YFP atlas
  (PMID:16823372), which is abstract-only in the cache. Fission yeast has a
  closed mitosis and the obligatory substrates Cut2/securin and Cdc13/cyclin B
  are nuclear at metaphase, so the nucleus is the compartment of core activity;
  the cytosolic signal is real for a soluble 1 MDa complex but is not linked to
  a characterised Apc2 function, so it is kept as non-core. The deep research
  explicitly cautions against claiming an exclusive localisation for Apc2.

## Decisions on the GOA rows (14 rows)

| term | evidence | action | note |
|---|---|---|---|
| GO:0000151 ubiquitin ligase complex | IEA ARBA | ACCEPT | correct parent of GO:0005680 |
| GO:0003674 molecular_function | ND | MODIFY -> GO:0160072 | MF is now assignable (cullin scaffold, ISS/IC) |
| GO:0005634 nucleus | HDA | ACCEPT | closed mitosis, nuclear substrates |
| GO:0005634 nucleus | IEA ARBA | ACCEPT | |
| GO:0005680 APC/C | IBA | ACCEPT | target in own WITH/FROM is expected |
| GO:0005680 APC/C | IDA PMID:12477395 | ACCEPT | |
| GO:0005680 APC/C | IDA PMID:15060174 | ACCEPT | Cut9-TAP / Apc13-TAP |
| GO:0005680 APC/C | IPI PMID:12477395 (ComplexPortal) | ACCEPT | |
| GO:0005829 cytosol | HDA | KEEP_AS_NON_CORE | |
| GO:0006511 Ub-dependent catabolic process | IEA ARBA | ACCEPT | general but correct |
| GO:0007091 metaphase/anaphase transition | IBA | ACCEPT | core |
| GO:0031145 APC/C-dependent catabolic process | NAS (ComplexPortal) | ACCEPT | most precise process term |
| GO:0043161 proteasome-mediated Ub-dependent catabolic process | IC | ACCEPT | |
| GO:0070979 protein K11-linked ubiquitination | IBA | MODIFY -> GO:0000209 | K11 specificity is UBE2S-dependent and metazoan; linkage in S. pombe not determined |

No NEW process terms proposed: every process the Apc2-containing ligase executes
(GO:0031145, GO:0007091) is already annotated, and GO:0010458 exit from mitosis
would be a complex-level inference that PomBase has not made for the core
subunits (checked against nuc2, which also lacks it).

## Open questions

- Chain linkage assembled by the S. pombe APC/C with Ubc4/Ubc11 (K48? K11?
  mixed?) - not determined.
- Does the human APC2 zinc-binding module (Hofler 2024) have a counterpart in
  fission yeast Apc2? Absent from budding yeast; untested in S. pombe.
- Cell-cycle-resolved localisation of endogenous Apc2 (only the ORFeome
  overexpression atlas exists).
