# dlg1 review notes

## Session 1 (create review)

- `just fetch-gene DROME dlg1` resolved P31007 (DLG1_DROME), 97 GOA rows.
- No deep-research API; literature summary written by hand in `dlg1-deep-research-manual.md`.
- Added references beyond GOA: PMID:8830775 (Woods 1996, SJ/polarity), PMID:9390515 (Zito 1997,
  Fas2/Shaker clustering), PMID:15638945 (Chen & Featherstone 2005, GluRIIB), PMID:19766567
  (Johnston 2009, Pins/Dlg/Khc-73), PMID:19769408 (SH3-GK regulation), PMID:26740169 (GK domain
  evolution; enzyme to protein-binding).

### Key decisions

- GMP kinase activity (TAS x2) and the derived IEA GMP/GDP metabolic process rows: REMOVE.
  The MAGUK GUK is a protein-interaction domain [PMID:26740169 "Anc-GK1PID has no detectable
  guanylate kinase activity, but it binds Pins"]; no Dlg kinase assay supports catalysis.
- Bare protein binding: Shaker rows -> MODIFY to transmembrane transporter binding (GO:0044325);
  GukH rows -> REMOVE (uninformative; no specific MF term for the GUK-GukH contact).
- Follicle-cell patterning, EGFR, germ plasm and fate-specification rows from PMID:19948068 are
  downstream effects of polarity loss: MARK_AS_OVER_ANNOTATED, except follicle cell development
  (KEEP_AS_NON_CORE).
- Behavioural rows (courtship, phototaxis, locomotor rhythm, gravitaxis, ethanol): KEEP_AS_NON_CORE.
- NEW: protein-macromolecule adaptor activity (GO:0030674), the Pins-Dlg-Khc-73 bridge
  [PMID:19766567]. This is MF, not a process; no NEW process terms proposed.
- Apical cortex rows (all three): KEEP_AS_NON_CORE. Neuroblast apical enrichment is transient
  (prophase/metaphase) before Dlg becomes uniformly cortical. In disc epithelia (PMID:29378849) Dlg
  is apicolateral (SJ), and "apical cortex" there reflects the confocal plane, not the apical domain.
- Plasma membrane rows (all six): ACCEPT. Dlg is a peripheral PM scaffold in several cell types;
  the specific sub-membranes are accepted in their own rows.
- IBA cell-cell adhesion: MARK_AS_OVER_ANNOTATED (role conflation). IBA postsynaptic density
  membrane: MODIFY to postsynaptic membrane, because the fly NMJ has no vertebrate-type PSD.

### Open questions

- Whether Dlg has a direct molecular activity in basolateral polarity beyond stabilizing Scrib
  cortically (Khoury & Bilder 2020, PMID:32414916).
