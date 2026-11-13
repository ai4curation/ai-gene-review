# MTHFR2 (At2g44160, UniProtKB:O80585) curation notes

## Deep research status

`just deep-research-falcon ARATH MTHFR2` was attempted on 2026-11-13 and failed
(Edison API 403, "Failed to authenticate"). No provider deep-research file exists.
These notes are a manual literature survey instead.

Literature search performed (PubMed E-utilities, 2026-11-13):

- `methylenetetrahydrofolate reductase Arabidopsis` -> PMIDs 42590837, 41937012,
  39450434, 30653319, 28939595, 23116396, 12937179, 11729203, 10593891.
- `MTHFR2 nonhost resistance Magnaporthe` -> 42590837, 41937012, 39450434.

Papers read (abstracts; no cached full text): PMID:10593891, PMID:11729203,
PMID:39450434, PMID:41937012. HDA proteomics papers PMID:25293756 and
PMID:28887381 are cached with full text (protein lists are in supplements).

## Biochemistry

- Roje et al. 1999 cloned two Arabidopsis MTHFR cDNAs and a maize cDNA; they complement
  yeast met12 met13 [PMID:10593891 "These cDNAs encode functional MTHFRs,
  as evidenced by their ability to complement a yeast met12 met13 mutant"].
- Recombinant His-tagged Arabidopsis MTHFR is a dimer of ~66 kDa subunits
  [PMID:10593891 "it exists as a dimer of approximately 66-kDa subunits"].
- Key distinguishing property: NADH preference and lack of AdoMet inhibition
  [PMID:10593891 "Unlike mammalian MTHFR, the plant enzymes strongly prefer NADH to
  NADPH, and are not inhibited by S-adenosylmethionine"].
- Polypeptides lack targeting sequences [PMID:10593891 "lack obvious targeting
  sequences"], and the reaction may be reversible in the cytosol
  [PMID:10593891 "An NADH-dependent MTHFR reaction could be reversible in plant
  cytosol"].
- UniProt attributes EC 1.5.1.54 / RHEA:19821 to MTHFR2 with ECO:0000269 from
  PMID:10593891. Which of the two Arabidopsis isozymes was His-tagged and purified
  is not stated in the abstract; Roje et al. 2002 used AtMTHFR-1 for yeast
  engineering [PMID:11729203 "replaced by an Arabidopsis MTHFR cDNA (AtMTHFR-1)"].
  Plant MTHFR properties are stated for "the plant enzymes" generally.
- Roje 2002: plant MTHFRs are NADH-dependent and AdoMet-insensitive; the C-terminal
  domain confers AdoMet inhibition in yeast/mammal enzymes
  [PMID:11729203 "This contrasts with plant MTHFRs, which are NADH-dependent and
  AdoMet-insensitive"].
- FAD cofactor and binding residues in UniProt are by similarity (ECO:0000250).

## Physiology

- MTHFR2 loss of function (forward-genetic mosA = mthfr2 pen2-3, and T-DNA lines)
  reduces nonhost resistance to rice blast [PMID:39450434 "MTHFR2 is a positive
  modulator of NHR against M. oryzae"]. This is an indirect, metabolic effect; no
  immune signalling activity of MTHFR2 itself is shown.
- Pati et al. 2026: mthfr2 mutants have altered methionine and homocysteine and
  accumulate homocysteine thiolactone [PMID:41937012 "loss-of-function mutation in
  MTHFR2 disturbs methionine and homocysteine concentrations"]. Supports a role in
  supplying methyl groups (5-methyl-THF) for methionine synthesis in planta.

## Localization

- Cytosolic: no targeting sequence (PMID:10593891); HDA in crude cytosolic fraction
  SEC-MS (PMID:25293756) and in the soluble fraction of membrane profiling
  (PMID:28887381). The nucleus row is an AtSubP prediction (ISM) with no supporting
  data.

## Family

- DR PANTHER: PTHR45754 (METHYLENETETRAHYDROFOLATE REDUCTASE); PTHR45754:SF3
  (METHYLENETETRAHYDROFOLATE REDUCTASE (NADPH)). The family review
  `interpro/panther/PTHR45754/PTHR45754-review.yaml` originally said plant MTHFR is SF4;
  the member table places MTHFR1 (Q9SE60) in SF4 and O80585 in SF3, and the family
  review was corrected accordingly. The SF3 name (NADPH) does not match the NADH-preferring
  plant enzyme.
- InterPro: IPR029041, IPR004621 (Fadh2_euk), IPR003171, IPR053806 (MTHFR_C).

## Curation decisions

- GO:0004489 [NAD(P)H] rows: MODIFY to GO:0106312 (NADH) — the child term, already
  carried via the EC mapping, and specifically supported by the NADH preference.
- GO:0006555 L-methionine metabolic process: MODIFY to GO:0071265 (already carried).
- Nucleus (ISM): MARK_AS_OVER_ANNOTATED.
- No NEW rows for immunity: the defense phenotype is a downstream metabolic effect.
