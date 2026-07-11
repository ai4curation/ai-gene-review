# ALG13 (Q9NP73) review notes

## Summary of function
ALG13 is the **catalytic (glycosyltransferase) subunit** of the bipartite
**ALG13/ALG14 UDP-N-acetylglucosamine transferase (GnTase)** that catalyses the
**second step of dolichol-linked oligosaccharide (LLO) assembly** in the ER: transfer of
the **second N-acetylglucosamine (β1,4-linked) from UDP-GlcNAc onto GlcNAc-PP-dolichol**
to form the chitobiose core **GlcNAc2-PP-dolichol** (N,N'-diacetylchitobiosyl
diphosphodolichol). EC 2.4.1.141 = GO:0004577.

- ALG13 provides the UDP-GlcNAc-binding/catalytic (GT28) domain but lacks a
  membrane-spanning region; ALG14 is the membrane anchor that recruits ALG13 to the
  **cytosolic face of the ER membrane**. ALG13 has no GnTase activity unless complexed
  with ALG14. [PMID:16100110, PMID:36200043]
- The active complex = **UDP-N-acetylglucosamine transferase complex (GO:0043541)**;
  ALG13 is a peripheral ER-membrane protein.
- Human ALG13 has 4 isoforms. Only the **short isoform 2 (165 aa)** forms a functional
  complex with ALG14 and supports GnTase/LLO synthesis; the long isoform 1 (1137 aa,
  the displayed/canonical sequence) does **not** bind ALG14 and lacks GnTase activity.
  [PMID:36200043] The GT28 catalytic region is at the N-terminus (aa ~1-125, shared by
  isoforms 1 and 2).
- The long isoform 1 additionally contains an **OTU domain** with intact catalytic
  residues, but **no deubiquitinase activity** was detected in vitro (UniProt CAUTION;
  PMID:23827681). This DUB/proteolysis annotation is not a validated function and is not
  in the GOA TSV under review.

## Disease
Pathogenic ALG13 variants cause **X-linked developmental and epileptic encephalopathy 36
(DEE36 / ALG13-CDG)** — infantile spasms / early-onset epileptic encephalopathy with
neurodevelopmental impairment. Some patients show abnormal transferrin isoelectric
focusing (CDG type I biomarker), though many ALG13-CDG variants have near-normal
transferrin. CDG variants (e.g. K94E, N107S) reduce GnTase activity in vitro.
[PMID:22492991, PMID:36200043, PMID:23934111, PMID:26138355]

## GOA annotation review decisions (genes/human/ALG13/ALG13-goa.tsv)
- GO:0004577 N-acetylglucosaminyldiphosphodolichol N-acetylglucosaminyltransferase activity
  — the exact GOA MF term (= EC 2.4.1.141). Multiple lines (IDA PMID:36200043,
  IMP PMID:22492991, IEA GO_REF:0000120). CORE. ACCEPT.
- GO:0006488 dolichol-linked oligosaccharide biosynthetic process — CORE BP. ACCEPT
  (IMP PMID:22492991; IEA InterPro).
- GO:0006487 protein N-linked glycosylation — downstream BP, acts_upstream_of_positive_effect
  IMP. KEEP_AS_NON_CORE (the direct molecular step is LLO GlcNAc2 formation; N-glycosylation
  is the pathway it feeds).
- GO:0005789 endoplasmic reticulum membrane — CORE CC (EXP PMID:16100110, TAS Reactome, IEA
  SubCell). ACCEPT.
- GO:0098554 cytoplasmic side of endoplasmic reticulum membrane — precise CC, is_active_in,
  IGI PMID:16100110. ACCEPT (more specific than ER membrane; matches biology).
- GO:0003824 catalytic activity (IEA ARBA) — root-level MF, uninformative. MARK_AS_OVER_ANNOTATED.
- GO:0016758 hexosyltransferase activity (IEA InterPro) — parent of GO:0004577; correct but
  too general given the specific term is present. MODIFY -> GO:0004577.
- GO:0005737 cytoplasm (IEA ARBA) — over-general/imprecise; the protein acts as a peripheral
  membrane protein on the cytoplasmic face of the ER (GO:0098554), not free cytoplasm.
  MARK_AS_OVER_ANNOTATED.
- GO:0005515 protein binding (IPI PMID:33961781, with SLC2A4/P14672) — bare protein binding
  from a high-throughput AP-MS interactome (BioPlex). Uninformative; not the biologically
  meaningful ALG13-ALG14 interaction. MARK_AS_OVER_ANNOTATED (per policy: do not REMOVE bare
  protein binding IPI).

## Complex membership
UniProt DR block records GO:0043541 (UDP-N-acetylglucosamine transferase complex, IDA) — used
in core_functions in_complex.
