# rmlC (PA5164, Q9HU21) notes

## Literature

No deep-research provider was available. PMC full text of PMID:17046787 was not returned by the PubMed
tool; the review uses the cached abstracts of PMID:17046787 and PMID:11065359 and the reviewed UniProt
entry (curated FUNCTION and binding sites cite PMID:17046787 as experimental).

- Reaction [PMID:17046787 "RmlC catalyzes the epimerization of the C3' and C5' positions of
  dTDP-6-deoxy-D-xylo-4-hexulose, forming dTDP-6-deoxy-L-lyxo-4-hexulose"]; third enzyme of the rhamnose
  pathway [PMID:17046787 "RmlC is the third enzyme of the rhamnose pathway"].
- LPS core [PMID:11065359 "rmlC mutants of both serotype O5 and serotype O6 synthesized a truncated core
  region which was unable to act as an attachment point for either A-band or B-band O antigen"].

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000471580 | GO:0000271 polysaccharide biosynthetic process | 3 | 38 (30 taxa) | GO:0009244, IDA, PMID:11065359 (PseudoCAP); also UniProt IDA GO:0000271 and GO:0009103, PMID:17046787 | SOUND | rmlC makes the L-Rha donor for the LPS outer core; mutants lack the O-antigen attachment site. Evidence is a mutant phenotype, so IMP not IDA (PROBABLE WRONG_EVIDENCE_CODE defect). | S. enterica RfbC P26394, M. tuberculosis RmlC P9WH11 | Yes. dTDP-L-Rha feeds O antigens and the mycobacterial linker; term suits the clade. |
| PTN000471580 | GO:0016854 racemase and epimerase activity | 3 | 13 (9 taxa) | GO:0008830, EXP, PMID:17046787 (PseudoCAP) and IDA (UniProt) | SOUND | Structure and mutant-assay paper; UniProt cites it as ECO:0000269 for function. Not a leaf row on rmlC (it carries the specific GO:0008830). | P26394, P9WH11 | Yes. |
| PTN000471594 | GO:0008830 dTDP-4-dehydrorhamnose 3,5-epimerase activity | 3 | 25 (21 taxa) | GO:0008830, EXP, PMID:17046787 (PseudoCAP) | SOUND | As above; P. aeruginosa RmlC structures 2IXH-2IXK. | P26394, P9WH11 | Yes. |
| PTN000471594 | GO:0019305 dTDP-rhamnose biosynthetic process | 2 | 25 (21 taxa) | GO:0019305, IDA, PMID:17046787 (PseudoCAP) | SOUND | Characterises the third pathway enzyme; UniProt cites it for function in dTDP-rhamnose biosynthesis. | M. tuberculosis RmlC P9WH11 | Yes, on the single other seed, a characterised RmlC; the term is exact for the clade. |

One PSEUDOCAP defect (WRONG_EVIDENCE_CODE, PROBABLE) on GO:0009244. No GO_CENTRAL defect.

## Other decisions

- GO:0000271 (IBA, IDA) and GO:0009103 (IDA, IEA): TOO_GENERAL, entailed by accepted GO:0009244
  (checked is_a/part_of in the local GO).
- Consistent with the wbp reviews (wbpE, wbpI): nucleotide-sugar precursor enzymes are accepted for the
  specific glycan biosynthesis term and the generic polysaccharide rows are TOO_GENERAL.
