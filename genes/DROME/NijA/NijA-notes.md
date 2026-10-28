# NijA review notes

## Session 1 (2026-10-28)

- `just fetch-gene DROME NijA` resolved Q8MPP0 (NIJA_DROME, FlyBase FBgn0036101, GeneID
  39215). GOA: 19 rows. First attempt timed out on UniProt; retry succeeded.
- Publications: PMID:16815999 (abstract only; PMC PDF extraction failed), PMID:23028562
  (full text, read), PMID:33472215 (abstract only), plus PMID:41448502 (Neurobiol Dis 2026,
  full text) and PMID:40777432 (its bioRxiv preprint) found by PubMed search.
- No deep-research provider available; see `NijA-deep-research-manual.md`.

### Key evidence

- Cell-surface multipass protein: [PMID:23028562 "NijA protein is redistributed to the
  cell surface in larval immune tissues after septic injury and is upregulated by the Toll
  pathway"]; [PMID:16815999 "the endogenous proteins were found to colocalize at the
  tracheal cell surface in larvae"].
- Overexpression kills cells nonapoptotically and cell-autonomously; needs surface
  localization; ectodomain alone does not kill [PMID:23028562].
- Null mutant has no phenotype [PMID:23028562 "NijAD3 homozygous mutants were viable and
  fertile with no obvious developmental abnormalities"].
- Mmp1 cleaves NijA; the released ectodomain causes loss of S2 cell adhesion to surfaces,
  nonautonomously [PMID:16815999 "This liberated ectodomain promotes the loss of cell
  adhesion in a cell-nonautonomous manner."].
- Family mechanism (NINJ1): membrane-inserting amphipathic helices drive oligomerization
  and plasma membrane rupture [PMID:33472215].

### Decisions

- Plasma membrane rows: ACCEPT (IDA x2, IBA, IEA all agree).
- Extracellular region: KEEP_AS_NON_CORE (the Mmp1-released ectodomain is secreted; a
  real but peripheral location of the cleavage product).
- membrane (IEA InterPro): MODIFY -> plasma membrane.
- cell adhesion: the fly experimental evidence is for loss of adhesion (anti-adhesive
  ectodomain), so the IDA/IMP/IGI rows are MODIFY -> GO:0010812 negative regulation of
  cell-substrate adhesion (S2 cells "lose adhesion to surfaces"). The IBA/IEA cell
  adhesion rows are MODIFY to the same replacement, so all rows on the term agree. The
  IBA cell-cell adhesion mediator activity and the derived IEA cell-cell adhesion rest on
  mammalian NINJ1 homophilic adhesion assays; nothing shows NijA mediates homophilic
  adhesion, and the one fly adhesion study shows the opposite effect.
  MARK_AS_OVER_ANNOTATED, not REMOVE (the family trait may hold; not tested).
- programmed cell death and cytolysis: ACCEPT. The fly evidence is gain-of-function
  (null has no phenotype), but it is consistent with the conserved family role of NINJ1 as
  the effector of plasma membrane rupture, and PAINT placed both at the ninjurin node. The
  Kayagaki 2021 IDA row for cytolysis cannot be verified from the cached abstract; deferred
  to the curator and flagged.
- tissue regeneration (IEA InterPro2GO): MARK_AS_OVER_ANNOTATED; rests on injury-induced
  expression of rat Ninj1, no regeneration evidence in fly.
- NEW: membrane destabilizing activity (GO:0140912), ISS to NINJ1, as the molecular
  activity underlying cytolysis. Added because the human NINJ1 review uses this term as
  NINJ1's core MF and NijA's cell-killing activity requires surface localization and is
  nonapoptotic. No NEW process terms: the glial nerve-injury phenotype [PMID:41448502] is
  a mutant phenotype and does not identify the step NijA performs.

## 2026-10-28 review fixes

GO:0019835 cytolysis IDA (PMID:33472215) changed ACCEPT -> UNDECIDED; added a SUSPECTED UniProt source_defects CHECK on the evidence code (no mis-attribution asserted). Dropped GO:0012501 from core function directly_involved_in. NEW GO:0140912 row: added supporting_entities UniProtKB:Q92982 (human NINJ1, verified) and a clause on why the ISS is used while the adhesion IBA is rejected. Status DRAFT because the IBA (ACCEPT) and IDA (UNDECIDED) cytolysis rows now differ, which validation warns on.
