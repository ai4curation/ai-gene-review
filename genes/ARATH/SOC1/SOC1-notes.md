# SOC1 (AGL20, At2g45660; UniProt O64645) curation notes

## 2026-10-05 — finishing review (floral_meristem_identity module)

- GO:0010077 maintenance of inflorescence meristem identity (IGI with BOP1/BOP2, PMID:20626659, abstract-only):
  UNDECIDED -> KEEP_AS_NON_CORE, deferring to the experimental curator (full text not cached); biologically
  consistent because SOC1/AGL24/SVP promote shoot/inflorescence character and are repressed by AP1 in flowers
  [PMID:17428825].
- protein binding IPI with AP1/CAL from PMID:11439126 (AP1/CAL yeast two-hybrid screen; abstract-only):
  UNDECIDED -> MODIFY to GO:0046982, consistent with the independent matrix MADS interaction map [PMID:15805477].
- Three protein binding rows previously MARK_AS_OVER_ANNOTATED: Pin1At (PMID:20129060) and OXS3 (PMID:31540691)
  -> REMOVE (no SOC1-enabled MF follows); Arabidopsis Interactome-1 (PMID:21798944; partners AP1 and FUL)
  -> MODIFY to GO:0046982.
- SOC1 role in the module: integrator that binds and activates the LFY promoter as a SOC1-AGL24 heterodimer [PMID:18466303].
