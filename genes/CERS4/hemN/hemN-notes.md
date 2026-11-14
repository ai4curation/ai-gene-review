# hemN (Cereibacter sphaeroides 2.4.1) review notes

UniProtKB: P33770 (HEMF_CERS4; mnemonic CERS4), locus RHOS4_19250 / RSP_0317, 452 aa. EC 1.3.98.3.

## Deep research

No `-deep-research-*.md`; deep research was unavailable in this session (provider attempt for
RHOCB/hemA failed: missing template, no keys). Built from UniProt and cached abstracts.

## Biology

- Mutant N1 (hemN) cannot grow photosynthetically, lacks BChl and excretes coproporphyrin III.
  [PMID:1333567 "instead of synthesizing bacteriochlorophyll, N1 excretes coproporphyrin III into the growth medium"]
- Proposed as the anaerobic coproporphyrinogen III oxidase dedicated to BChl synthesis.
  [PMID:1333567 "which is proposed as the anaerobic coproporphyrinogen III oxidase dedicated to bacteriochlorophyll biosynthesis."]
- Separate O2-dependent HemF required for aerobic growth.
  [PMID:16385070 "We found that a HemF- mutant strain is unable to grow under aerobic conditions."]
- Radical SAM chemistry, [4Fe-4S] and two SAM, from the E. coli ortholog structure.
  [PMID:14633981 "HemN, strikingly, binds a second SAM immediately adjacent to the first."]
- UniProt reaction/cofactor/binding sites are by similarity (ECO:0000250) to E. coli P32131.
  No purified R. sphaeroides HemN assay found in cached literature.

## Decisions

Follow genes/ECOLI/hemN and genes/PSEPK/hemN: generic catalytic/Fe-S rows MODIFY to the specific
terms; GO:0004109 (O2-dependent) MODIFY laterally to GO:0051989 with an InterPro2GO source defect;
GO:0006779 MODIFY to bacteriochlorophyll biosynthetic process (genetic evidence) and heme B
biosynthetic process (shared protoporphyrinogen IX pool); NEW SAM binding (IC).
