# GstO1 (DROME, Q9VSL6) review notes

## Session 1

- `just fetch-gene DROME GstO1` resolved Q9VSL6 (FlyBase FBgn0035907, GeneID 38975, CG6662);
  14 GOA rows. First two attempts timed out on rest.uniprot.org, third succeeded.
- No deep-research provider available; manual literature work recorded in
  `GstO1-deep-research-manual.md`.

### Nomenclature

PMID:22219196 (Kim et al. 2012, "Glutathione s-transferase omega 1 activity is sufficient to
suppress neurodegeneration in a Drosophila model of Parkinson disease") is about **CG6673**,
which that paper calls DmGSTO1 [PMID:22219196 "CG6673 is also called D. melanogaster GSTO1 (DmGSTO1)"].
CG6673 is FlyBase **GstO2** (already reviewed at `genes/DROME/GstO2`). The paper's only
GstO1 (CG6662) data are a negative result for ATP synthase beta glutathionylation
[PMID:22219196 "Another DmGSTO, CG6662, did not affect glutathionylation of the ATP synthase β subunit"].
Hossain et al. 2023 confirm the renaming [PMID:37389657 "CG6673 was originally named DmGSTO1 (Kim et al., 2012), but later renamed as GstO2 (Kim and Yim, 2013)."].
No GOA row for GstO1 cites PMID:22219196, so there is no source defect to report, but the
paper must not be used as evidence for GstO1 function.

### Annotation decisions

- GST activity (IBA/IDA x2/IEA): ACCEPT. Recombinant CG6662 had GSH-dependent thiol
  transferase and DHAR activity [PMID:16712527].
- DHAR, GO:0045174 (IBA/IDA/IEA): ACCEPT; directly assayed in PMID:16712527.
- NOT pyrimidodiazepine synthase (IDA, PMID:16712527): ACCEPT; only CG6781 (sepia) made PDA.
- Cytoplasm (IBA/IEA/ISS): ACCEPT; soluble Omega GST; in muscle it decorates ER/endosome
  membranes (PMID:37389657) which are cytoplasmic structures.
- Glutathione metabolic process (IBA/IDA): KEEP_AS_NON_CORE; GSH is consumed (oxidised) by its
  DHAR/thiol transferase chemistry, but the term is a broad metabolic umbrella.
- Cellular oxidant detoxification (IEA from DHAR): KEEP_AS_NON_CORE; H2O2 sensitivity of the
  mutant (PMID:26024591, abstract) is consistent, but GstO1 does not itself reduce H2O2.

### NEW proposals

- GO:0010731 protein glutathionylation (IMP, PMID:37389657). Comparator check: GstO2
  carries this term in its review (ATP synthase beta); human GSTO1 is also annotated to
  glutathionylation-related processes. GstO1 is the proposed catalyst (it binds Gbb and is
  required for Gbb-SSG); this is participation evidence (enzyme acting on the modified protein)
  rather than mere necessity, although a cell-free assay with recombinant GstO1 is lacking.
- GO:0005783 endoplasmic reticulum (IDA, PMID:37389657): near-perfect co-localisation with
  KDEL in larval muscle. Single assay type; kept as non-core location. Early/recycling
  endosome overlap was described as "substantial overlap", not added.
- Not added: negative regulation of BMP signaling / synapse growth at NMJ. These are
  downstream consequences of Gbb degradation; raised as a suggested question.
- Not added: response to ethanol, H2O2 response (mutant phenotypes, abstract-only).
