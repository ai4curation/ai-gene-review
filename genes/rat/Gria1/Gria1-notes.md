# Gria1 (rat) review notes

## Session 1 (2026-10-28)

- `just fetch-gene rat Gria1` resolved P19490 (GRIA1_RAT, RGD:621531, GeneID 50592);
  GOA file keyed to P19490, 277 rows. `just fetch-gene-pmids` cached 95 papers;
  PMID:19321442 was already cached (full text).
- No deep-research API keys; literature synthesis written by hand to
  `Gria1-deep-research-manual.md`.
- Template: the sibling review `genes/rat/Gria2` was used for consistency of actions on
  shared AMPA-receptor terms. Key difference from GluA2: GluA1 is not Q/R edited, so
  GluA1-containing GluA2-lacking receptors are Ca2+-permeable
  [PMID:1709304 "At physiological resting potentials, KA and AMPA elicited inward calcium currents in oocytes expressing GluR1, GluR3, and GluR1 plus GluR3."].
  GO:0022849 glutamate-gated calcium ion channel activity is therefore accepted here,
  whereas it was flagged for Gria2.

### Decisions worth flagging

- Bare GO:0005515 rows removed (policy). The IPI row PMID:16108831 (with Q5U2P2) cites
  a human cancer-immunotherapy paper on IGSF11 that does not mention AMPA receptors;
  the GluA1-IgSF11 interaction is from PMID:26595655 (WRONG_REFERENCE source defect).
- GO:0019865 immunoglobulin binding (IgSF11 partner) is a term error: IgSF11 is an Ig
  superfamily adhesion molecule, not an immunoglobulin. MODIFY to GO:0050839 cell adhesion
  molecule binding, with a WRONG_TERM source defect.
- GO:0005829 cytosol (PMID:34742997, full text): the "cytosolic" fraction is the
  non-synaptosomal Syn-PER supernatant; GluA1 is a multi-pass membrane protein. Removed,
  WRONG_TERM source defect.
- GO:0071359 cellular response to dsRNA (PMID:19958814): the "dsRNA" was a transfected
  miR-132 duplex mimic, not a dsRNA stimulus in the GO sense; WRONG_TERM defect.
- CC rows carried by IEP (PMID:16903873, SynGO) and IMP (PMID:10731148 SynGO,
  PMID:12536214 UniProt, PMID:27307232 UniProt) evidence: location supported by other
  evidence, so the rows take the same action as their term siblings, with
  WRONG_EVIDENCE_CODE / CHECK defects.
- Most IEP "response to X" rows (drugs, toxins, hormones, diet) are expression readouts
  and are marked as over-annotations.
- GO:0099507 (presynaptic membrane potential channel activity, ISO/IEA from human):
  no evidence that presynaptic GluA1 regulates presynaptic potential; generalised to
  AMPA glutamate receptor activity with the presynaptic context dropped.
- No NEW terms proposed: the core activities, complex and locations are all already
  present in GOA.
