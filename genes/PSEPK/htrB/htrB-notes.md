# htrB (PP_1735, Q88M40) — Pseudomonas putida KT2440

## Identity

UniProt Q88M40 is `htrB` with synonym `lpxL` and ordered locus name `PP_1735`
[file:PSEPK/htrB/htrB-uniprot.txt "GN   OrderedLocusNames=PP_1735"]. This
matters for the literature: the only experimental paper on this enzyme in
*P. putida* refers to it by locus tag, not by symbol.

UniProt types it by the HtrB/LpxL-specific HAMAP rule MF_01942 as a lipid A
biosynthesis acyltransferase, EC 2.3.1.241, with the alternative name
Kdo(2)-lipid IV(A) acyltransferase
[file:PSEPK/htrB/htrB-uniprot.txt "RecName: Full=Lipid A biosynthesis acyltransferase"].

## Experimental function in P. putida

*P. putida* encodes two LpxL homologues, PP_0063 and PP_1735
[PMID:28557109 "Two homologues of Escherichia coli acyltransferase LpxL,"].
Both were deleted individually in strain KT2442 (mutants KWZ001 and KWZ002) and
the isolated lipid A species analysed by ESI/MS; both loci proved to encode
secondary acyltransferases
[PMID:28557109 "The results suggest that both PP_0063 and PP_1735 encode"].

Site specificity was then resolved by overexpressing PP_0063, PP_1735 and
*E. coli* lpxL in the reciprocal deletion backgrounds: PP_0063 adds the
2-OH-C12:0 chain at the 2-position, and PP_1735 adds the C12:0 chain at the
2'-position
[PMID:28557109 "encoded by PP_1735 catalyses the addition of the C12:0 chain to the 2'-position"].
The conclusion states both assignments together
[PMID:28557109 "secondary acyl chains at the 2- and 2'-positions of lipid A in P. putida."].

The 2'-position is the position LpxL/HtrB acylates on Kdo2-lipid IV(A), so this
work grounds the IEA-derived `GO:0008913` Kdo2-lipid IVA acyltransferase
activity in organism-specific experiment rather than signature match alone.

## Caveats

- The paper used strain KT2442; the UniProt accession is from KT2440. KT2442 is
  a rifampicin-resistant derivative of KT2440, but the strains are not formally
  identical and the review records the distinction rather than glossing it.
- The cached record is abstract-only (`full_text_available: false`), so every
  statement above is taken from the structured abstract. The GOA rows for this
  gene remain IEA; the citation is reviewer-supplied literature support, not a
  re-coding of the evidence code.

## Annotation decisions

- `GO:0008913`, `GO:0009245`, `GO:0036104`, `GO:0009103`, `GO:0009247`,
  `GO:0005886` — kept; `GO:0008913` and `GO:0036104` carry the core function.
- `GO:0016020`, `GO:0016740`, `GO:0016746` — marked over-annotated as generic
  parents of retained, more informative terms.
- No GO molecular-function child describes 2-position 2-OH-lauroyl transfer, so
  the paralog PP_0063 keeps the generic acyltransferase parent while this gene
  takes the position-matched `GO:0008913`. See
  `genes/PSEPK/PP_0063/PP_0063-notes.md`.
