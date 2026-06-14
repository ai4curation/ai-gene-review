# pqsB (Q9I4X2, PA0997) — review notes

Part of the **BGC exemplar curation project** (`projects/BGC.md`). MIBiG BGC0000922
(*P. aeruginosa* PAO1, 2-alkyl-4-quinolone / PQS-precursor cluster). GenBank
AAG04386.1 → UniProt **Q9I4X2** (PQSB_PSEAE), gene *pqsB* / PA0997.

## Function

PqsB is the **non-catalytic subunit of the heterodimeric condensing enzyme PqsBC**
that makes 2-heptyl-4(1H)-quinolone (HHQ) in the *pqs* quorum-sensing pathway
(see `pqsC-notes.md` for the full pathway).

- PqsB **lacks the catalytic residues** (the active-site Cys-129/His-269 reside in
  PqsC) but is **tightly associated with PqsC and required for the condensation
  step**; the octanoyl group is carried on PqsC.
  [PMID:24239007 "the decarboxylating coupling of 2-ABA to an octanoate group
  linked to PqsC produces HHQ... PqsB is tightly associated with PqsC and required
  for the second step."]
- Crystal structure (PDB 5DWZ): the PqsBC complex is "unique for its heterodimeric
  arrangement" [PMID:26811339]. PqsB contributes to the structure/stability and
  activity of the assembled heterodimer — a textbook "only functional when
  assembled" complex.
- A *pqsB* mutant is defective in extracellular quinolone signal (PQS) production
  [PMID:12426334 — Gallagher et al. 2002, the IMP source for GO:0044550].

## Annotation issue identified

- **GO:0016746 acyltransferase activity (IEA, enables)** — PqsB has the
  condensing-enzyme (thiolase-like) fold but is **catalytically inactive**; the
  acyltransferase activity is a property of the **PqsBC heterodimer**, catalyzed by
  PqsC. Annotating PqsB with `enables acyltransferase activity` over-attributes the
  catalytic function to the non-catalytic subunit. A `contributes_to` qualifier (or
  annotation to the complex) would be appropriate. → **MARK_AS_OVER_ANNOTATED**.

## Predicted-complex evidence (BGC project)

Moriwaki et al. (bioRxiv 2025.10.26.684697) predict the PqsB–PqsC heterodimer
(BGC0000922; AAG04386.1/AAG04387.1) at **ipTM 0.95**, matching PDB 5DWZ.

## References
- PMID:24239007 — Dulcey et al. 2013, Chem Biol. VERIFIED.
- PMID:26811339 — Drees et al. 2016, JBC (PqsBC structure, 5DWZ). VERIFIED.
- PMID:12426334 — Gallagher et al. 2002, J Bacteriol (IMP source). VERIFIED.
