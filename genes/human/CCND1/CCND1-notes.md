# CCND1 (cyclin D1, P24385) — curation working notes

## Identity

Human CCND1 at 11q13.3 encodes cyclin D1 (295 aa), historically BCL-1 and PRAD1; one of
three mammalian D-type cyclins (CCND1/2/3). UniProt P24385 CHAIN 1..295 with a
Cyclin N-terminal domain at 28..152, a disordered C-terminal region 262..295, and
MOD_RES 286 phosphothreonine. Not to be confused with CCND2/CCND3 or the cyclin D1b
splice variant, whose altered C terminus removes the Thr286 degron
(CCND1-deep-research-falcon.md, "Alternative splicing produces cyclin D1b, whose altered
C terminus removes important localization and degradation controls").

## Core molecular function: non-catalytic CDK4/6 activator

Cyclin D1 is a regulatory subunit with **no intrinsic catalytic activity**; the kinase
chemistry is done by CDK4/CDK6 within the holoenzyme.

- UniProt FUNCTION: "Regulatory component of the cyclin D1-CDK4 (DC) complex that
  phosphorylates and inhibits members of the retinoblastoma (RB) protein family including
  RB1 and regulates the cell-cycle during G(1)/S transition".
- UniProt SUBUNIT: "Interacts with either CDK4 or CDK6 protein kinase to form a
  serine/threonine kinase holoenzyme complex ... The cyclin subunit imparts substrate
  specificity to the complex".
- [PMID:8114739 "The cdk6 kinase is associated with cyclins D1, D2, and D3 in lysates of
  human cells and is activated by coexpression with D-type cyclins in Sf9 insect cells"]
  and [PMID:8114739 "endogenous cdk6 from human cell extracts is an active kinase which
  can phosphorylate pRB, the product of the retinoblastoma tumor suppressor gene"].
- [PMID:19237565 "we report the crystal structure of CDK4 in complex with cyclin D1 at a
  resolution of 2.3 A"] — direct structural evidence for the cyclin D1-CDK4 complex.
- [PMID:7603984 "the pRB is the critical target acted upon by cyclin D-dependent kinases
  in the G1 phase of the cell cycle"].
- [PMID:33854239 "Increased levels of cyclin D promote cell division by activating
  cyclin-dependent kinases 4 and 6 (hereafter, CDK4/6), which in turn phosphorylate and
  inactivate the retinoblastoma tumour suppressor"].
- Deep research: "cyclin D1 has no intrinsic kinase activity, and RB is phosphorylated by
  CDK4/6 within the complex".

Consequence for review: the two orthology-transferred catalytic annotations
(GO:0004672 protein kinase activity, GO:0016301 kinase activity, both IEA from mouse
Ccnd1 P25322) are **wrong in kind** and were removed. The activator/regulator terms
(GO:0061575, GO:0016538, GO:0043539) and the complex terms (GO:0000307, GO:0097128,
GO:0097131) carry the real biology. GO:0043539 (generic protein Ser/Thr kinase activator
activity) was modified to the CDK-specific child GO:0061575.

GO-CAM agreement: `gocams/index.tsv` types CCND1 in both the AMBRA1 model
(61e0e55600000624) and the FBXO32 model (680ad14200006016) as
GO:0061575 cyclin-dependent protein serine/threonine kinase activator activity acting in
GO:0000082 G1/S transition of mitotic cell cycle — the same MF/BP pair adopted in
`core_functions`.

## Assembly, localization and turnover

- CIP/KIP proteins promote assembly and nuclear import: [PMID:9106657 "we find that all
  three CIP/KIP inhibitors target cdk4 and cyclin D1 to the nucleus"] and [PMID:9106657
  "cyclin D1 and p21 bind concomitantly to cdk4 during the in vivo assembly of
  cdk4/cyclin D1 complexes"]. UniProt: ternary CCND1/CDK4/CDKN1B complex "required for
  nuclear translocation and modulation of CDK4-mediated kinase activity"; complexes
  "accumulate at the nuclear membrane and are then translocated to the nucleus".
- Nucleus, cytoplasm and nuclear membrane are all UniProt-supported locations; the
  cytoplasmic pool reflects Thr286-dependent export and degradation
  [PMID:29279382 "cyclin D1 levels are maintained at steady state by
  phosphorylation-dependent nuclear export and subsequent proteolysis in the cytoplasm"].
- Degradation: CRL4(AMBRA1) is the principal G1/S ligase [PMID:33854235 "we identify
  CRL4AMBRA1 (also known as CRL4DCAF3) as the ubiquitin ligase that targets all three
  D-type cyclins for degradation"]; [PMID:33854239 "AMBRA1 mediates ubiquitylation and
  proteasomal degradation of cyclin D as a substrate receptor for the cullin 4 E3 ligase
  complex"]; SCF(FBXO31) after DNA damage [PMID:19412162 "ectopic expression of FBXO31
  acts through a proteasome-directed pathway to mediate the degradation of cyclin D1, an
  important regulator of progression from G1 to S phase, resulting in arrest in G1"];
  APC/C-CDC27 [PMID:20439707 "Cdc27 directs cyclin D1 to alternative degradation by
  APC/C"]; UHRF2/NIRF [PMID:21952639 "ubiquitinates cyclins D1 and E1"]; FBXO32 gives
  K27-linked stabilizing ubiquitination [PMID:40307251 "FBXO32 catalyzes the lysine
  (Lys/K)27-linked polyubiquitination of cyclin D1 at the K58 site and subsequent
  stabilization"].

Consequence for review: in all of these, cyclin D1 is the **substrate** of the ligase, not
a participant in the ubiquitination process, so no ubiquitination/catabolism process term
was proposed (`proposed_new_terms: []`). The machine-readable substrate relationship
belongs on the ligases as `has input`; this is raised in `suggested_questions`.

## CDK-independent transcriptional corepressor role

Genuine second function, explicitly curated by UniProt: "Exhibits transcriptional
corepressor activity with INSM1 on the NEUROD1 and INS promoters in a cell
cycle-independent manner (PubMed:16569215, PubMed:18417529)".

- [PMID:16569215 "Cyclin D1 co-operates with INSM1 and suppresses neuroD/beta2 promoter
  activity"] and [PMID:16569215 "INSM1 interacts with HDAC-1 and -3 and that this
  interaction is mediated through cyclin D1"].
- [PMID:18417529 "The mechanism for transcriptional repression of the insulin gene by
  INSM1 is mediated through the recruitment of cyclin D1 and histone deacetylase-3 to the
  insulin promoter"].
- Binding determinant: [PMID:19124461 "The proline-rich N-terminal portion of INSM1 is
  required for cyclin D1 binding"] — supports GO:0070064 proline-rich region binding.
- Other repression targets: NRF-1 [PMID:16864783 "Nuclear respiratory factor 1 (NRF-1),
  which induces nuclear-encoded mitochondrial genes, was repressed in expression and
  activity by cyclin D1"]; androgen receptor [PMID:16461912 "In the prostate, cyclin D1a
  acts through discrete mechanisms to negatively regulate androgen receptor (AR) activity
  and thus limit androgen-dependent proliferation"].

So GO:0000122, GO:0003714 and GO:0017053 were accepted, and the corepressor role appears
as a second `core_functions` entry.

## Reviewing the bare `protein binding` (GO:0005515) block — 76 rows

Repository practice: resolve to an informative MF where the cited evidence supports one,
otherwise REMOVE as uninformative (which does not assert the interaction is false).
Applied by partner:

| WITH/FROM partner | action |
|---|---|
| CDK4 (P11802), CDK6 (Q00534), CDK2 (P24941), mouse Cdk4 (P30285) | MODIFY → GO:0019901 protein kinase binding |
| FBXO31 (Q5XUX0), UHRF2 (Q96PU4), CDC27/APC3 (P30260) | MODIFY → GO:0031625 ubiquitin protein ligase binding |
| HDAC3 (O15379) | MODIFY → GO:0042826 histone deacetylase binding |
| AR (P10275) | MODIFY → GO:0035257 nuclear receptor binding |
| INSM1 (Q01101), NRF1 (Q16656) | MODIFY → GO:0008134 transcription factor binding |
| p21/CDKN1A (P38936), p27/CDKN1B (P46527, Q96TE0), BRCA1, SARS-CoV N, Ralbp1, SMARCA4, SMAD4, FBXW7 | REMOVE (uninformative) |

Notes on two of these: GO:0050681 "nuclear androgen receptor binding" is **obsolete**
(QuickGO), hence GO:0035257 nuclear receptor binding for the AR row. The three rows from
[PMID:35512704] come from a *mutation-directed neo-interaction* screen, so they are not
evidence for a wild-type molecular function and were removed rather than resolved.
GO:0019899 enzyme binding (WITH USP2, O75604) was modified to the informative child
GO:1990381 ubiquitin-specific protease binding (UniProt: "Interacts with USP2").

## Substrate-of-a-process vs participant: the DNA-damage rows

[PMID:19412162] supports IDA rows for GO:0006974 DNA damage response and GO:0031571
mitotic G1 DNA damage checkpoint signaling. The mechanism is that damage stabilizes
FBXO31, which degrades cyclin D1, producing G1 arrest — i.e. cyclin D1 is the *terminal
target* whose removal implements the arrest, not a transducer of checkpoint signalling.
Per the CLAUDE.md participation rule (being required for, consumed by, or acted on by a
process is not participation) both were marked over-annotated rather than accepted;
neither was removed, since the observation itself is sound and the papers' full text was
not consulted beyond the abstract. The CDK-independent HR/RAD51 role reported in the deep
research ("Reducing cyclin D1, but not merely inhibiting CDK4/6, decreased RAD51
recruitment after DNA damage") is a *different* claim, not evidenced by this reference,
and was not used to accept these rows.

## Pleiotropic / propagated rows

- **Rat-derived "response to X" cluster** (GO:0009410, GO:0010039, GO:0010165, GO:0032026,
  GO:0032355, GO:0033197, GO:0043627, GO:0045471, GO:0048545, GO:0051384, GO:0051412,
  GO:0051592, GO:0071456; IEA from rat Ccnd1 P39948): these are expression-response
  annotations. CCND1 transcription is the canonical downstream readout of mitogenic,
  hormonal and stress signalling, so upregulation does not make cyclin D1 an executor of
  each response. All marked over-annotated (matching the CDK4 review's treatment of
  GO:0009410 IEP). The human IEP row from [PMID:18291362 "The transcriptional targets of
  beta-catenin, c-myc, cyclin D1 and cdk 4 were also dramatically downregulated"] is the
  same pattern. Similarly GO:0044321 response to leptin (IDA, [PMID:17344214 "leptin
  induced increase in CYCLIN D1 promoter activity is mediated through binding of activated
  Stat3 at the Stat binding sites"]) — CCND1 is the promoter being acted on.
- **GO:0070141 response to UV-A** (IDA, [PMID:18483258]) is the exception kept as
  non-core: knockdown, not just induction, was tested — "siRNA knockdown of cyclin D1
  blocked the UVA-induced cell cycle progression, indicating that this process is mediated
  by cyclin D1".
- **Developmental/tissue rows** (GO:0001889 liver development, GO:0031100 animal organ
  regeneration, GO:0033327 Leydig cell differentiation) are plausible proliferation-driven
  contributions and kept as non-core.
- **GO:0005815 microtubule organizing center (IBA)** removed. Arguing the node placement,
  as required for IBA: the donor set is PANTHER:PTN007424001 plus human CCNB1 (P14635),
  CCNB2 (O95067), CCNF (P41002), *S. pombe* SPBC2G2.09c/SPBC582.03 and SGD S000006323 —
  all mitotic B-/F-type cyclins and their fungal counterparts, for which
  centrosome/spindle-pole-body localization is a class-specific property. The assertion
  sits at a node ancestral to the D-cyclins, but no human, mouse or rat literature places
  cyclin D1 activity at the MTOC, and D-cyclin function (mitogen sensing in G1) is not the
  mitotic-cyclin function that localization serves.
- **GO:0005923 bicellular tight junction (IEA from mouse Ccnd1)** marked over-annotated:
  the donor annotation could not be traced in the cached record and no human evidence
  places cyclin D1 at tight junctions.
- **GO:0010971 positive regulation of G2/M transition (IDA, [PMID:19124461])** modified to
  GO:1900087 positive regulation of G1/S transition: the cited paper is about G1 —
  "INSM1 binding to cyclin D1 interrupts its association with CDK4 and induces
  hypophosphorylation of the retinoblastoma protein" — so the phase is wrong while the
  sign and the regulated-transition essence are right.
- Generic **GO:0044877 protein-containing complex binding** (IEA, rat) marked
  over-annotated as uninformative.

## Not proposed as new terms

Comparator check run before declining a ubiquitination/catabolism term for the substrate
role: GO's convention places the process on the enzyme. Cyclin D1's own GO-CAM
appearances (`gocams/61e0e55600000624`, `gocams/680ad14200006016`) already model it in the
role GO intends — as the CDK activator and as the ligases' input molecule — so there is no
gap to fill. `proposed_new_terms: []`.
