# PP_0063 (Q88RR6) — curation notes

## Identity

`PP_0063` is an inner-membrane acyltransferase of the LpxL/LpxM-like lipid A
acyltransferase family. UniProt gives only an unreviewed `SubName`
[file:PSEPK/PP_0063/PP_0063-uniprot.txt "DE   SubName: Full=Lipid A biosynthesis lauroyl acyltransferase"],
supported by family-level signatures
[file:PSEPK/PP_0063/PP_0063-uniprot.txt "DR   Pfam; PF03279; Lip_A_acyltrans; 1."]
and [file:PSEPK/PP_0063/PP_0063-uniprot.txt "DR   NCBIfam; NF004190; PRK05645.1; 1."].
There is no HAMAP rule and no EC assignment, unlike its paralog `htrB`/`PP_1735`
(Q88M40), which carries `EC=2.3.1.241` and the Kdo(2)-lipid IV(A) acyltransferase
AltName.

## The acceptor is established experimentally in *P. putida*

The physiological acceptor was initially recorded here as unresolved. It is not:
`PMID:28557109` (Zhu et al. 2017, *J Appl Microbiol*) identifies **both** *P. putida*
LpxL homologues and assigns each a position on lipid A.

- Both genes encode lipid A secondary acyltransferases, shown by single-gene deletion
  (strains KWZ001 = ΔPP_0063, KWZ002 = ΔPP_1735) and ESI/MS of the isolated lipid A
  [PMID:28557109 "The results suggest that both PP_0063 and PP_1735 encode"].
- Site specificity was resolved by overexpressing `PP_0063`, `PP_1735` and *E. coli*
  `lpxL` in each deletion background
  [PMID:28557109 "addition of the 2-OH-C12:0 chain at the 2-position and the acyltransferase"].
- Conclusion: the two enzymes install the
  [PMID:28557109 "secondary acyl chains at the 2- and 2'-positions of lipid A in P. putida."]

So `PP_0063` → 2-position (2-OH-C12:0) and `PP_1735`/`htrB` → 2'-position (C12:0).
This is what distinguishes the two annotons of the late-acylation step, which are
otherwise both just "LpxL/LpxM family".

Caveat recorded in the review: the paper works in **KT2442**, whereas the annotated
accession is **KT2440**. KT2442 is a rifampicin-resistant derivative of KT2440, and
the paper cites the locus tags themselves (`PP_0063`, `PP_1735`), which are KT2440
identifiers — but the strain difference is noted rather than glossed. The cached record
is abstract-only (`full_text_available: false`), so only the structured abstract was
read.

## Consequences for the annotations

- `GO:0009245` lipid A biosynthetic process — proposed as `NEW` (IMP, PMID:28557109).
  Not in GOA for this gene, though its paralog `htrB` carries it. `PP_0063` itself
  catalyses the acyl-transfer step, so `involved_in` is the right relation rather than
  a substrate/necessity framing.
- `GO:0009247` glycolipid biosynthetic process — moved from `UNDECIDED` to `ACCEPT`.
  Lipid A is a glycolipid, and `htrB` already `ACCEPT`s this term on exactly this
  reasoning; leaving it `UNDECIDED` here was inconsistent with both the paralog and the
  module's placement of `PP_0063` inside the late-acylation part.
- `GO:0016746` acyltransferase activity — kept as `ACCEPT` and still the most specific
  applicable MF. The substrate-defined children describe other positions:
  `GO:0008913` Kdo2-lipid IVA acyltransferase activity (the `htrB` 2'-position reaction)
  and `GO:0008951` palmitoleoyl-dependent acyltransferase activity. No GO term or EC
  number covers 2-position 2-OH-C12:0 transfer, so nothing more precise is assertable.

## PANTHER subfamily assignment is uninformative here

UniProt assigns `PTHR30606:SF10`
[file:PSEPK/PP_0063/PP_0063-uniprot.txt "DR   PANTHER; PTHR30606:SF10; PHOSPHATIDYLINOSITOL MANNOSIDE ACYLTRANSFERASE; 1."],
versus `SF9` (lipid A biosynthesis lauroyltransferase) for `htrB`. Every reviewed SF10
member in `interpro/panther/PTHR30606/PTHR30606-entries.csv` is an actinobacterial PatA
(*M. smegmatis*, *M. tuberculosis*), and phosphatidylinositol mannoside biosynthesis is
an actinobacterial pathway absent from *P. putida*. The subfamily call therefore carries
no biological information for a gammaproteobacterium and should not be read as evidence
*against* a lipid A role — the family-level call (`PTHR30606`) plus PF03279 and the
experimental result above are what stand.

## Still open

- No structure or in vitro assay for the *P. putida* enzyme; the acyl donor is inferred
  to be acyl-ACP from family membership rather than measured here.
- Whether acylation occurs before or after Kdo transfer in *P. putida* is not addressed
  by PMID:28557109, which is why `GO:0008913` (Kdo2-lipid IVA acceptor) is not asserted.
