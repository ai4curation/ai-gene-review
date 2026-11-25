# kdpA (E. coli K-12) curation notes

## 2026-11-01 review pass

- No provider deep-research file exists for this gene; provider deep research was
  not run for this pass. Evidence came from cached publications (full text:
  PMID:28636601, PMID:30478378, PMID:34272288; abstract-only: PMID:7896809,
  PMID:9789555, PMID:356049, PMID:2849541, PMID:8499455, PMID:21711450) and the
  curated UniProt entry.
- GO:1903103 potassium:proton antiporter complex (IBA and ComplexPortal IPI on
  PMID:28636601) is defined by K+/H+ antiporter activity (GO:0015386). KdpFABC is an
  ATP-driven P-type K+ uptake pump [PMID:28636601, "Mutagenesis has been used to
  establish that K+ is transported through KdpA5,6 and that the energy of ATP is
  harnessed by KdpB7."]. Both rows set to MODIFY -> GO:0031004 with source_defects.
- Bare protein binding rows removed per policy; complex membership captured by GO:0031004.


## 2026-11-07 E. coli Kdp module consultation

Reviewed all existing annotation claims against the cached primary literature, UniProt record, and current GO definitions. Original ordered annotation payloads and source files were frozen before editing; no new annotation rows were added. The two inherited KdpD NEW proposals remain present. Detailed decisions and source scope are recorded in `analysis/module_audits/bacterial_kdp_potassium_homeostasis/ecoli-consultation/`.

A genuine configured Falcon research request was attempted for this gene and failed with HTTP 403 authentication; no provider report was fabricated. The exact attempt log is `.cache/module-audit-logs/kdp-20261107/ecoli-consultation/falcon-kdpA.log`. PAINT-loss checking found no IRD/IKR loss on the recorded lineage.

KdpA supplies K+ selectivity and the entry segment of the route, not the whole transmembrane path. PMID:41259220 uses wild-type E. coli pump in nanodiscs plus mutant transport assays to support tunnel transfer into KdpB; PMID:41384914 retains this route while questioning a continuous ion wire and exposing an unresolved interface barrier. The old PMID:7896809 interpretation is retained explicitly as historical. The core retains K+ binding and contribution to pump activity, with no new annotations.
