# rhgf-2 review notes

## Session 1

- fetch-gene resolved Q22354 (unreviewed TrEMBL, T08H4.1a, 862 aa). GOA has 13 rows, 12 from
  PMID:22363657 (WormBase), plus one InterPro2GO IEA.
- Literature: only two papers mention rhgf-2 in PubMed. PMID:22363657 (Lin et al. 2012), with full
  text cached, and PMID:26188247 (Chan et al. 2015, Dev Biol), cached as abstract only. See
  rhgf-2-deep-research-manual.md.
- Key synthesis: RHGF-2 is a RHO-1-specific DH-PH RhoGEF (PLEKHG5/Syx/Tech ortholog). Its essential role is
  RHO-1/LET-502-dependent embryonic elongation in the lateral epidermis [PMID:26188247 "Genetically, rhgf-2 acts as an activator of let-502/Rho-binding kinase, in parallel to fem-2/PP2c phosphatase."].
  The GEF step is something RHGF-2 itself performs, so embryonic body morphogenesis passes the
  participation test (the gene product catalyses the RHO-1 activation step of the pathway).
- Decisions:
  - GEF activity (IDA, IEA): ACCEPT. GO:0005089 Rho GEF activity has been merged into GO:0005085,
    so GO:0005085 is the most specific available MF term.
  - Small GTPase binding (RHO-1 IPI): ACCEPT (substrate binding of a GEF).
  - Protein binding to MPZ-1: MODIFY to GO:0030165 PDZ domain binding (C-terminal SDV motif binds MPZ-1 PDZ8).
  - Rho protein signal transduction: ACCEPT.
  - Embryonic body morphogenesis: ACCEPT. Cell morphogenesis: KEEP_AS_NON_CORE (seam-cell shape defect).
  - Negative regulation of neuron projection development: MARK_AS_OVER_ANNOTATED. This rests only on
    overexpression in mouse N1E-115 cells, and there is no worm neuronal morphology phenotype.
  - Regulation of locomotion: MARK_AS_OVER_ANNOTATED (overexpression-only, and the authors call it preliminary).
  - Positive regulation of transcription by RNA pol II: REMOVE. The SRE-luciferase assay is explicitly a
    readout of RhoA activation in HEK293T cells. The GEF is not a transcription regulator.
  - Axon: KEEP_AS_NON_CORE. Neuron projection: MODIFY to axon. Cell body: MODIFY to neuronal cell body.
- No NEW annotations. Cytokinesis or cleavage furrow ingression (Chan 2015) is a phenotype only, and the
  abstract-only source cannot support a NEW term under the strict NEW bar.
