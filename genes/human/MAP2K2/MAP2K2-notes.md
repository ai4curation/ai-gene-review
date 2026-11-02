# MAP2K2: evidence notes

## Paired horse benchmark evidence review

The human reference supplies mechanistic evidence for the corresponding selected horse protein; the human conclusion alone is not validation of the horse sequence. The exact horse comparison is in `genes/HORSE/MAP2K2/MAP2K2-bioinformatics/RESULTS.md`. Research reports are source leads; annotation decisions cite the underlying publication or experimentally supported UniProt passages. Unresolved source-specific results retain UNDECIDED.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

**Identity.** P36507 is the reviewed, canonical human MEK2 (400 aa, sequence version 1, MANE ENST00000262948). It is not a fragment, isoform or alternative gene model: it carries the full protein kinase domain (72-369), active-site Asp194, ATP-binding loop 78-86 and Lys101, RAF sites Ser222/Ser226, and the C-terminal class I PDZ-binding motif RTAV that MEK1 lacks.

**Evolutionary placement.** UniProt cross-references PTHR47448:SF3 (MITOGEN-ACTIVATED PROTEIN KINASE KINASE 2); the PANTHER 19.0 per-organism file instead places P36507 in PTHR48013:SF8 (also named MAP2K2), and MAP2K1 in PTHR48013:SF5. Both sources keep MEK2 in its own subfamily separate from MEK1, so the disagreement is a family-numbering/release conflict, not a biological one (recorded in `interpro/panther/PTHR47448/PTHR47448-review.yaml` and `panther-members-overrides.tsv`). The IBA rows come from PAINT node PTN000684494 (MAP2K clade, MAPKK activity + MAPK cascade), with P36507 itself among the descendant evidence [PMID:8388392 "The purified MEK2 protein stimulated threonine and tyrosine phosphorylation on ERK1 and concomitantly activated ERK1 kinase activity more than 100-fold"].

**Changes vs previous review.**
- Catalytic rows: generic kinase, Ser/Thr, Ser, Tyr, Ser/Thr/Tyr kinase and Ser/Thr kinase activator rows all MODIFY to GO:0004708 MAP kinase kinase activity (the activator-activity row describes ERK activation by phosphorylation, which is the catalytic MF).
- MAPK cascade IBA -> MODIFY to ERK1 and ERK2 cascade; positive regulation of Ser/Thr kinase activity -> MODIFY to positive regulation of MAP kinase activity.
- Extracellular region (NAS, PMID:8388392) REMOVE: name-derived from "extracellular signal-regulated kinase"; MEK2 is cytosolic.
- Cytoplasm -> MODIFY to cytosol; membrane kept non-core (KSR fractionation [PMID:10409742 "this results in the appearance of MEK in membrane-associated fractions"]).
- MAP kinase scaffold activity (IMP PMID:29433126, full text read) kept non-core: MEK binding to KSR1 drives KSR1-BRAF dimerization [PMID:29433126 "Reducing endogenous MEK1 and/or MEK2 levels by RNA interference (shMEK1 and/or shMEK2) decreases BRAF-KSR1 interaction by BRET"]; the authors frame it as KSR being a MEK-dependent allosteric BRAF activator, so the scaffold term is approximate (suggested question).
- Gene expression / DNA-templated transcription IMPs (PMID:24375836, MEK1/2 inhibitor AZD6244, miR-92a via ERK-AP1) MARK_AS_OVER_ANNOTATED: downstream outputs, not MEK2 work. Regulation of stress-activated MAPK cascade MARK_AS_OVER_ANNOTATED (MEK2 is ERK-specific). Peroxisomal membrane HDA (PEX14 co-purification) MARK_AS_OVER_ANNOTATED.
- Review-derived (PMID:19565474, abstract only) localizations and processes (mitochondrion, early/late endosome, Golgi, focal adhesion, Golgi inheritance, endosome transport) stay UNDECIDED: the best-known endosomal partner LAMTOR3/MP1 was reported as MEK1-selective and MEK2-specific data cannot be checked. DLG1-paper ER/microtubule/junction/Golgi IDAs UNDECIDED (abstract attributes ER/microtubules to hDlg); plasma-membrane inner face and perinuclear IDAs kept non-core (stated for both proteins).
- Protein binding: Q96II5 (an ARAF entry) row changed from REMOVE to MODIFY -> MAPKKK binding, consistent with other ARAF rows; boilerplate UniProt FUNCTION quotes removed from protein-binding rows.
- New description and two core functions (MAPKK activity in the ERK1/2 cascade, cytosol; scaffold protein binding to KSR1/DLG1).

**Relative.** Closest experimentally characterised relative by placement: mouse Map2k2 (Q63932), same MEK2 subfamily (PTHR47448:SF3 in the PANTHER entries list; source of UniProt's "By similarity" ERK1/2 statement). No mouse Map2k2 review exists in the repo. Paralog MAP2K1 (Q02750, different subfamily) has a complete review at `genes/human/MAP2K1/`. Module: `modules/erk_cascade.yaml` (mek_kinase annoton lists P36507).
