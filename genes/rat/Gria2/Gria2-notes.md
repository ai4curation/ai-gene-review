# Gria2 (rat, P19491) review notes

## Setup
- `just fetch-gene rat Gria2` resolved P19491 (RGD:61862, GeneID 29627). 240 GOA rows seeded.
- `just fetch-gene-pmids` cached 84 papers; PMID:19321442 (Dixon et al. 2009, full text) cached
  and read: OGD triggers PICK1-dependent removal of GluA2 from the cell surface (surface
  biotinylation, Fig. 3) [PMID:19321442 "We observed a time-dependent reduction in GluR2 surface
  expression by OGD"].
- No deep-research API; literature synthesis in `Gria2-deep-research-manual.md`.

## Core picture
1. Pore-forming, ligand-binding AMPA receptor subunit (GO:0004971) in the AMPA receptor complex
   (GO:0032281), acting at the postsynaptic density membrane of glutamatergic synapses; the edited
   Q/R site (R607) makes GluA2-containing receptors Ca2+-impermeable [UniProt RNA EDITING;
   PMID:1653450].
2. C-terminal tail is a trafficking hub: PDZ ligand binds GRIP1/ABP/PICK1 (GO:0030165), NSF binds
   a membrane-proximal motif, AP-2 binds a basic motif; this controls synaptic delivery, clustering,
   recycling and LTD-associated endocytosis [PMID:9069286; PMID:9697854; PMID:17289840].

## Upstream problems found
- GO:0015277 kainate selective glutamate receptor activity (UniProt IDA, PMID:21846932): kainate
  is a weak partial agonist at GluA2; the receptor is AMPA-type. -> GO:0004971.
- GO:0019865 immunoglobulin binding (UniProt IPI, PMID:26595655): partner is IgSF11, an Ig
  superfamily adhesion molecule, not an immunoglobulin -> cell adhesion molecule binding.
- GO:0000149 SNARE binding (UniProt IPI, PMID:11931741, with PICK1): PICK1 is not a SNARE; the
  abstract describes GluR2-PICK1 as "a non-SNARE substrate" of NSF.
- GO:0005515 row PMID:16108831 (IGSF11 cancer-vaccine paper) has nothing on GluA2; probably the
  intended reference is PMID:26595655.
- GO:0042802 row PMID:31925409 (GluD1 cryo-EM): full text never mentions GluA2; likely belongs
  to Grid1.
- GO:0099507 (SynGO, PMID:10704491): the paper measures flip/flop kinetics in oocytes; no
  presynaptic data.
- GO:0098793 presynapse (RGD IDA, PMID:21807099): synapsin was used only as a presynaptic marker
  to define synaptic GluA2 puncta.
- GO:0022849 glutamate-gated calcium channel activity (PMID:11773314): Ca2+ permeability measured
  on GluA1(Q) and unedited/mutant GluA2 constructs; native edited GluA2 makes channels
  Ca2+-impermeable.
- Phenotype/expression codes on CC rows (IEP 16903873; IMP 11348590) -> WRONG_EVIDENCE_CODE CHECK.
