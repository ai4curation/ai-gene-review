# wzm (Q9HTB8_PSEAE / PA5451) — review notes

## Identity
- **Gene**: `wzm`, ordered locus `PA5451`, *Pseudomonas aeruginosa* PAO1 (taxon 208964).
- **Protein**: Transport permease protein, 265 aa, ~29.5 kDa; polytopic inner-membrane protein.
  UniProt lists 6 predicted transmembrane helices and one "ABC transmembrane type-2" domain
  (PROSITE PS51012). TrEMBL (unreviewed), PE=3 (inferred from homology).
- **Family**: ABC-2 integral membrane protein family (ARBA/RuleBase); PANTHER PTHR30413
  (INNER MEMBRANE TRANSPORT PERMEASE); Pfam PF01061 (ABC2_membrane); InterPro IPR000412
  (ABC_2_transport), IPR013525 / IPR047817 (ABC2_TM). TCDB 3.A.1.103.6 (ABC superfamily).

## Core function (synthesis)
Wzm is the **transmembrane permease (TMD) subunit of the Wzm–Wzt ABC transporter** that
**exports the A-band common polysaccharide antigen (CPA; a D-rhamnan homopolymer) across the
inner (cytoplasmic) membrane** during ABC-transporter-dependent LPS O-antigen assembly in
*P. aeruginosa*. Wzm provides the transmembrane conduit; the cytoplasmic Wzt subunit supplies
ATP binding/hydrolysis (NBD). It is the classic Wzm/Wzt (ABC-transporter-dependent) O-antigen
export pathway, as opposed to the Wzx/Wzy flippase/polymerase pathway used for B-band O antigen.

## Key primary evidence

- **PMID:9244257** (Rocchetta & Lam, J Bacteriol 1997) — *identification & functional
  characterization* of wzm and wzt in the A-band LPS biosynthesis/export cluster.
  - "we report the characterization of two genes within the cluster, designated wzm and wzt.
    The Wzm and Wzt proteins have predicted sizes of 29.5 and 47.2 kDa … homologous to a number
    of proteins that comprise ABC (ATP-binding cassette) transport systems."
  - "Wzm is an integral membrane protein with six potential membrane-spanning domains, while Wzt
    is an ATP-binding protein containing a highly conserved ATP-binding motif."
  - Chromosomal wzm/wzt mutants: "were able to synthesize A-band polysaccharide, although
    transport of the polymer to the cell surface was inhibited. The inability of the polymer to
    cross the inner membrane resulted in the accumulation of cytoplasmic A-band polysaccharide."
  - "Chromosomal mutations in wzm and wzt were found to have no effect on B-band LPS synthesis."
  - Note: cache is **abstract-only** (`full_text_available: false`); full text likely contains
    additional detail. Supports IMP annotations for LPS/O-antigen transport (loss-of-function →
    cytoplasmic accumulation, blocked surface export).

- **PMID:23223798** (Singh et al., Integr Biol 2013) — quaternary structure of the Wzm–Wzt ABC
  transporter (FRET in living cells; heterologous expression in CHO cells).
  - "The polysaccharides in A-band LPSs are synthesized in the cytoplasm and translocated into
    the periplasm via an ATP-binding cassette (ABC) transporter consisting of a transmembrane
    protein, Wzm, and a cytoplasmic nucleotide-binding protein, Wzt."
  - "Wzm forms a square-shaped homo-tetramer both in the presence and absence of Wzt"; Wzt forms
    a rhombus→square tetramer with Wzm; propose a hetero-octameric double-tetramer model.
  - "Wzm is thought to provide a passage for PS during the translocation."
  - Supports: Wzm is a subunit of the ABC transporter complex; oligomerizes; TMD role.

## Annotation review reasoning

Existing GOA annotations (10):
1. GO:0015920 lipopolysaccharide transport — IBA (GO_REF:0000033) — involved_in → **ACCEPT** (core; matches ABC-2 permease phylogeny + experimental data).
2. GO:0005886 plasma membrane — IEA (SubCell) — located_in → **ACCEPT** (bacterial inner/plasma membrane; multipass).
3. GO:0016020 membrane — IEA (InterPro/UniRule) — located_in → **KEEP_AS_NON_CORE / MODIFY** (too general; plasma membrane is more informative and already present).
4. GO:0043190 ABC transporter complex — IEA (InterPro/UniRule) — part_of → **ACCEPT** (Wzm is a bona-fide subunit; supported experimentally by PMID:23223798).
5. GO:0055085 transmembrane transport — IEA (InterPro) — involved_in → **KEEP_AS_NON_CORE** (correct but generic parent of LPS transport).
6. GO:0140359 ABC-type transporter activity — IEA (InterPro) — enables → **ACCEPT** (MF for the transporter; Wzm is the TMD subunit — contributes_to; acceptable at this granularity).
7. GO:0009243 O antigen biosynthetic process — IMP (PMID:9244257) — involved_in → **ACCEPT** (A-band CPA export is part of O-antigen/LPS assembly; mutant phenotype supports).
8. GO:0015920 lipopolysaccharide transport — IMP (PMID:9244257) — involved_in → **ACCEPT** (direct experimental support; this is the core BP).
9. GO:0055085 transmembrane transport — ISS (PMID:9244257, from Q48478) — involved_in → **KEEP_AS_NON_CORE** (generic; redundant with LPS transport).
10. GO:0070258 **inner membrane pellicle complex** — EXP (PMID:23223798) — located_in → **REMOVE**.
    - GO:0070258 def: "A membrane structure formed of two closely aligned lipid bilayers that lie
      beneath the plasma membrane and form part of the **pellicle surrounding an apicomplexan
      parasite cell**." This is a taxon-inappropriate term for a *Pseudomonas* (bacterial)
      protein — an obvious mis-mapping. The paper describes the Wzm–Wzt ABC transporter in the
      bacterial **inner membrane**; the intended concept is the ABC transporter complex /
      plasma membrane, already captured by GO:0043190 and GO:0005886. → REMOVE (mis-annotation).

## Candidate more-specific MF (for core_functions consideration)
- GO:0015221 lipopolysaccharide transmembrane transporter activity — more specific than the
  generic GO:0140359; but Wzm is the membrane channel subunit (contributes_to the ABC transporter).
- No dedicated "O-antigen/CPA ABC exporter permease" MF term found; ABC-type transporter activity
  (GO:0140359) + LPS transmembrane transporter activity (GO:0015221) span the function.

## Notes / caveats
- A-band CPA is a **D-rhamnan homopolymer** ("common polysaccharide antigen"); B-band = serotype-
  specific O antigen exported by the Wzx/Wzy pathway (not Wzm/Wzt).
- No RB-TnSeq/FEBA fitness dataset fetch command available in this repo for PSEAE; step skipped.
