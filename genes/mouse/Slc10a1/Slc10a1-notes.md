# Slc10a1 (mouse Ntcp) curation notes

## Provenance of this review

Automated deep research was **not available in this container**, so the literature
synthesis below was assembled by hand from the cached publications in `publications/`
plus the UniProt record (O08705) and the GOA file:

- Falcon/Edison provider returned `402 Payment Required`; OpenAI provider returned
  `401 invalid_api_key`; `perplexity` is not a registered provider in this checkout.
- No `-deep-research-*.md` file was written (per CLAUDE.md, hand-written content must
  never be named as a deep-research provider output).

This review was done immediately after `genes/human/SLC10A1`, and the human notes file
carries the synthesized picture for the orthologue; this file records what is
specifically established for the **mouse** protein and where mouse and human diverge.

## Gene identity

- UniProt: O08705 (NTCP_MOUSE; Hepatic sodium/bile acid cotransporter; Slc10a1 / Ntcp)
- 362 aa, multi-pass membrane protein; bile acid:sodium symporter (BASS, TC 2.A.28)
  family; InterPro IPR002657
- Two alternatively spliced isoforms, both functional transporters
  [PMID:10209268 "we screened a mouse liver cDNA library and identified Ntcp1, encoding
  a 362 amino acid protein and Ntcp2, encoding a 317 amino acid protein which had a
  shorter C-terminal end."]

## Core transport function (direct mouse evidence)

- Both mouse isoforms are Na+-dependent taurocholate transporters
  [PMID:10209268 "Both isoforms mediated saturable Na+-dependent transport of
  taurocholate when expressed in Xenopus laevis oocytes."]
- UniProt records the curated stoichiometry as 2 Na+ per bile salt (RHEA:71875 for
  taurocholate, RHEA:71083 for estrone 3-sulfate) with mouse-specific kinetics:
  KM = 86 uM taurocholate (isoform 1), 14 uM (isoform 2), 104 uM estrone-3-sulfate.
- Mouse Ntcp is functionally close to human NTCP for both a probe substrate and a drug
  [PMID:34060352 "a functional comparison of human NTCP (hNTCP) and mouse Ntcp (mNtcp)
  showed similar Km values of 67 ± 10 µM and 104 ± 9 µM for the probe substrate
  estrone-3-sulfate as well as of 258 ± 42 µM and 199 ± 13 µM for the drug rosuvastatin,
  respectively."]
- Localization and physiological direction of transport
  [PMID:34060352 "The Na+/taurocholate cotransporting polypeptide (NTCP) is located in
  the basolateral membrane of hepatocytes, where it transports bile acids from the portal
  blood back into hepatocytes."]
- In vivo, mouse hepatic Slc10a1 is the basolateral uptake step whose loss of expression
  impairs portal bile acid uptake
  [PMID:11279518 "Tcf1-/- liver has decreased expression of the basolateral membrane bile
  acid transporters Slc10a1, Slc21a3 and Slc21a5, leading to impaired portal bile acid
  uptake and elevated plasma bile acid concentrations."]

## Species divergence: mouse Ntcp is NOT a functional HBV/HDV receptor

This is the point that matters most for judging transfers in this family, because human
NTCP's best-known non-transport property does **not** transfer to mouse.

- Human NTCP is necessary and sufficient to confer susceptibility in culture
  [PMID:23150796 "Silencing NTCP inhibited HBV and HDV infection, while exogenous NTCP
  expression rendered nonsusceptible hepatocarcinoma cells susceptible to these viral
  infections."]
- Mouse Ntcp is not
  [PMID:23678176 "mNTCP was found to be unable to support either HBV or HDV infection,
  although it can bind to pre-S1 of HBV L protein and is functional in transporting
  substrate taurocholate"]
  [PMID:23678176 "mNTCP failed to render HepG2 susceptible for HDV or HBV infection, a
  finding consistent with the host restriction in mouse."]
- The restriction maps to the first extracellular loop and is reversible by humanizing
  four residues
  [PMID:23678176 "Remarkably, when mNTCP residues 84 to 87 were substituted by human
  counterparts, mNTCP can effectively support viral infections."]
- Importantly, the restriction is **not** a loss of transport: mouse Ntcp retains full
  symport activity in the same assay
  [PMID:23678176 "In addition, mNTCP can mediate taurocholate uptake in the presence of
  sodium as efficient as hNTCP"]
- Consequence for curation: the two `NEW` annotations proposed on human SLC10A1
  (`GO:0001618 virus receptor activity`, `GO:0046718 symbiont entry into host cell`) must
  **not** be propagated to mouse Slc10a1. Residual pre-S1 lipopeptide binding is
  documented, but binding without supporting entry is not receptor activity, and GO:0046718
  is contradicted outright. Any future ISO/IBA transfer of those terms onto O08705 should be
  treated as a `FUNCTIONAL_DIVERGENCE` propagation failure.

## Donor tracing for the propagated rows

All 14 GOA rows are propagated except one IDA. Donors traced from the WITH/FROM column of
`Slc10a1-goa.tsv`, with the donor annotations' own evidence checked in the rat and human
GOA files in this repository:

| Donor | Identity | Donor evidence for the transferred term |
|---|---|---|
| RGD:3681 | rat Slc10a1 (P26435) | IDA: GO:0008508 + GO:0015721 (PMID:1961729), GO:0015125 + GO:0016323 (PMID:15297262), GO:0016323 (PMID:17082223) |
| RGD:3682 | rat Slc10a2 (Asbt) | paralog, apical ileal transporter; legitimate co-descendant seed for the symport node, not for basolateral localization |
| MGI:MGI:1201406 | mouse Slc10a2 | paralog; seeds the generic plasma-membrane node only |
| UniProtKB:Q14973 | human SLC10A1 | IDA: GO:0005886 + GO:0015125 (PMID:22029531) |
| UniProtKB:Q96EP9 | human SLC10A4 | paralog; generic plasma-membrane node only |
| UniProtKB:P26435 | rat Ntcp | ISS donor for GO:0016323; rat has IDA for that term |
| PANTHER:PTN000040759 | plasma-membrane node, whole SLC10 family | — |
| PANTHER:PTN000040761 | symport/bile-acid-transport node, NTCP+ASBT clade | — |
| PANTHER:PTN002570905 | NTCP-specific node, basolateral (correctly excludes the apical ASBT branch) | — |

No donor was judged problematic. In particular, none of the ISO rows was marked
`CIRCULAR_OR_REDUNDANT`: mouse Ntcp having its own direct functional evidence
(PMID:10209268, PMID:34060352) does not make a well-grounded experimental transfer
circular — the donor annotations are IDA, not propagations, and the chains contain no
transfer-of-a-transfer. Per CLAUDE.md, that status is reserved for genuine circularity.

## Curation decisions and their reasoning

1. **Transport MF/BP and plasma-membrane CC rows → ACCEPT** (GO:0008508, GO:0015125,
   GO:0015721, GO:0005886, GO:0016323, and the broad GO:0016020 IEA). The node placements
   are sound and the transfers land on a protein whose own experimental data match the
   donors' (Na+-dependent taurocholate symport, basolateral hepatocyte membrane).
   GO:0015125 is the less specific parent of GO:0008508; duplication at two granularities
   is acceptable and both are retained.
2. **`GO:0016020 membrane` IDA (PMID:11279518) → MODIFY → `GO:0016323 basolateral plasma
   membrane`.** The essence is right but the term is uninformative at the level of a
   single IDA, and the cited paper itself places Slc10a1 in the basolateral membrane
   (quote above). The sibling IEA GO:0016020 row is left as ACCEPT, since a broad
   electronic parent of correctly annotated children is harmless.
3. **No `NEW` annotations proposed.** Every activity, process and location that mouse Ntcp
   is known to perform is already represented. The virus-receptor pair is excluded on the
   species-divergence evidence above. Transport of non-bile-acid substrates
   (estrone-3-sulfate, rosuvastatin) is real but was demonstrated in transfected-cell
   uptake assays; whether that warrants a xenobiotic-transport process term is raised in
   `suggested_questions` rather than asserted.

## Open items

- GOA carries **no direct experimental molecular-function annotation** for mouse Ntcp,
  even though PMID:10209268 is a straightforward IDA-grade Xenopus oocyte uptake
  experiment on both mouse isoforms, and PMID:34060352 adds kinetics. The transport terms
  rest entirely on ISO/IBA. A direct IDA from PMID:10209268 would be a strict improvement
  and is raised as a suggested question.
- Isoform 2 (O08705-2, VSP_061644) has a roughly sixfold higher taurocholate affinity than
  isoform 1 (KM 14 vs 86 uM, PMID:10209268) but no isoform-resolved GO annotation exists.
- No GO-CAM model containing mouse Slc10a1 was found in `gocams/index.tsv` at review time.
