# SUN2 review notes

## 2026-09-27 (claude-code)

- Identity: human SUN2 / UNC84B / RAB5IP (Q9UH99), type II inner nuclear membrane protein, SUN-domain family.
- Core: SUN-KASH binding across the perinuclear space (LINC complex) [PMID:18396275 "the KASH domains of Nesprins 1, 2 and 3 interact promiscuously with luminal domains of Sun1 and Sun2"]; trimeric SUN2 binds three KASH peptides [PMID:22632968 "The SUN2 domain is rigidly attached to a trimeric coiled coil that prepositions it to bind three KASH peptides."].
- Nucleoplasmic side: lamin A binding [PMID:19933576 "SUN1 and SUN2 interact with lamin A, but lamin A is only required for NE localization of SUN2"].
- Neuronal nucleokinesis (mouse; redundant with SUN1) [PMID:19874786 "These results indicate that SUN1 and SUN2 are essential and mutually redundant for the normal radial neuronal migration in the cerebral cortex."].
- Decisions: GO:0034993 (meiotic LINC) rows MODIFY to non-meiotic parent GO:0106094 (evidence is mostly somatic nesprin-1/2/3 complexes); protein binding rows with nesprin partners MODIFY to GO:0140444, lamin rows to GO:0005521, HTP/viral/targeting-machinery rows REMOVE; TAS microtubule binding and mitotic spindle organization (from worm UNC-84 paper) REMOVE; endosome membrane (overexpressed rab5ip, PMID:10818110) MARK_AS_OVER_ANNOTATED.
- Deep research (falcon) consistent: SUN2 as non-catalytic LINC structural adaptor; 2023-2024 work on luminal disulfide regulation and nuclear actin/RNAPII coupling noted but not used for annotation.
- Module check (modules/nucleokinesis.yaml): GO:0140444 in nuclear inner membrane for SUN1/SUN2 and GO:0106094 LINC complex agree with this review.

## 2026-11-04: DeepTMHMM2 S20 topology audit

Source: [DeepTMHMM2 v1](https://doi.org/10.64898/2026.08.24.746435), supplied workbook `media-1.xlsx`, S20 row 45, Q9UH99. Author evidence category: **?**. These are the authors' predictions, with one-based inclusive coordinates:

`Nucleus matrix(1-197); interfacial(198-203); Nucleus matrix(204-717)`

**Assessment: Reject predicted topology change.** S20 explicitly acknowledges a missed transmembrane helix in this known single-pass protein. Retain the existing inner-nuclear-membrane type II topology and LINC-complex model (PMID:15082709 and the current review). A short adjacent IF198-203 call does not relocate the SUN domain from the perinuclear space or demonstrate a new compartment.

The complete source row, workbook hash and cross-gene decisions are retained in [the audit](../../../projects/DEEPTMHMM2.md). Membrane-contact geometry is considered separately from organelle localization and molecular function; no new function/process annotation is derived from this prediction.
