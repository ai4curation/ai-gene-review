# PLN (phospholamban) review notes

UniProt P26678, 52 aa, single-pass SR/ER membrane protein, PE1. Regulin family (PANTHER
node PTN002722410 in the IBA rows). No deep-research file was generated for this gene
(Tier 2/4 microproteins batch; instructions say not to run deep research).

## Core biology

- Reversible SERCA2a inhibitor. "In cardiac muscle, SERCA is regulated by phospholamban (PLB),
  a small inhibitory phosphoprotein that decreases the Ca(2+) affinity of SERCA and attenuates
  contractile strength." [PMID:23996003]
- Crystal structure of the PLB-SERCA complex: "PLB4 as an α-helix bound within a groove formed
  between transmembrane helices M2, M4, M6, and M9 of SERCA" and the two Ca sites "are both
  severely disrupted by PLB4 binding" [PMID:23996003]. The PLB4 construct is a
  monomerising/superinhibitory variant; SERCA1a was used ("regulated identically by PLB").
- Reconstitution kinetics (human-type PLB with SERCA in proteoliposomes): "Only three steps in
  the reaction scheme were affected by the presence of PLB, namely, binding of the first calcium
  ion, a subsequent conformational change in SERCA, and binding of the second calcium ion."
  [PMID:19708671]. This is the IDA source for GO:0042030 and GO:0141110.
- Phosphorylation relief: "Cyclic AMP-dependent phosphorylation of PLN reverses its inhibitory
  effect on the Ca2+ pump." [PMID:22679139]; PKA motif disrupted by R14del:
  "Deletion of Arg(14) disrupts the protein kinase A recognition motif, which abrogates
  phospholamban phosphorylation and results in constitutive SERCA inhibition." [PMID:22707725]
- Pentamer: "Human phospholamban (PLN), expressed in the sarcoplasmic reticulum membrane as a
  30-kDa homopentamer" held together by "leucine/isoleucine zipper motifs" [PMID:16043693].
  Monomer is the inhibitory species; "Phosphorylation of PLN monomers promotes association into
  inactive pentamers." [PMID:22679139]
- Channel claim for the pentamer [PMID:26673394]: GUV patch clamp "highlight a preference for
  Cs(+) over K(+) and do not conduct Ca(2+)". Physiological relevance debated; not in GOA as an
  MF; not proposed.
- Mouse knockout: "phospholamban acts as a critical repressor of basal myocardial contractility"
  and KO mice show "enhanced myocardial performance without changes in heart rate" [PMID:8062415].
  This bears on the "negative regulation of heart rate" rows (both MARK_AS_OVER_ANNOTATED).
- Human disease: R9C [PMID:12610310], R14del [PMID:16432188] dilated cardiomyopathy.
- Hetero-oligomers with other regulins: "PLB was a universal partner for all other micropeptides
  tested" [PMID:36523160].

## Protein-binding rows (63)

- 61 rows come from HT Y2H screens (HuRI PMID:32296183, PMID:25416956, PMID:25910212,
  PMID:31515488, PMID:24722188). Partners are mostly unrelated membrane proteins (EDA, BCL2L13,
  LDLRAD1, TMEMs, SLCs), typical of sticky TM-helix baits in Y2H. REMOVE as uninformative.
- PMID:28890335 ATP2A2 (P16615) row: the paper describes the "SERCA/PLN/SLN inhibitory complex",
  so MODIFY to ATPase inhibitor activity. VMP1 row: REMOVE (VMP1 competes with PLN; binding term
  uninformative).
- PMID:15598648 DMPK: PLN is a kinase substrate; no MF for PLN; REMOVE.

## Other decisions

- Spermatid / sleep / visual learning / locomotor rhythm rows are mouse ISS/IEA transfers of
  indirect or tissue-specific phenotypes; flagged as over-annotation.
- Rat IEA "response to zinc / insulin / testosterone" are expression-response transfers; REMOVE.
- 26673394 (GUV channel paper, abstract only) supports IDA rows for regulation of Ca transport
  and cardiac muscle cell contraction; abstract describes only an isolated vesicle channel
  assay that does not conduct Ca2+. Full text unavailable, so per "do not overrule curators"
  these rows are ACCEPTed or MODIFYed (to the SR Ca2+ import term) because the functions are
  clearly correct for PLN; the mismatch is recorded in the reference_review.

## Regulin MF comparison (Tier 4)

| gene | MF in GOA (non-binding) | MF chosen in repo review |
|------|------------------------|--------------------------|
| PLN | GO:0042030 ATPase inhibitor (IBA/IDA/ISS/IEA), GO:0141110 transporter inhibitor (IDA), GO:0004857 (ISS) | GO:0042030 core; GO:0141110 accepted |
| SLN | GO:0004857 enzyme inhibitor (ISS), GO:0030234 (IEA), GO:0051117 | not yet reviewed in repo |
| MRLN | GO:0004857 (ISS/IEA) | MODIFY -> GO:0042030 |
| ERLN | none | NEW GO:0042030 |
| STRIT1 (DWORF) | GO:0008047 enzyme activator (ISS) | GO:0141109 transporter activator activity |

QuickGO (2026-10-08): GO:0141110 is used on PLN (IDA), CALM, PCSK9, Agrn; GO:0042030 on PLN,
ATP5IF1, FNIP1/2, TSC1. The PLN IBA for GO:0042030 sits on PTN002722410, so the regulin node
already carries the ATPase-inhibitor framing. Recommendation: GO:0042030 for the inhibitory
regulins (PLN, SLN, MRLN, ERLN), GO:0141110 acceptable as a parallel; inconsistency with DWORF
(GO:0141109 rather than GO:0001671 ATPase activator activity) should be resolved one way.
