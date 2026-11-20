# kdpB (P03960, E. coli K-12) curation notes

## 2026-11-01 review pass

- Provider deep research was not run in this pass; the review is based on cached
  publications (full text: PMID:28636601, PMID:30478378, PMID:34272288; abstracts for the rest)
  and the curated UniProt record.
- KdpB is the ATP-hydrolysing subunit [PMID:30478378 "While ATP hydrolysis is accomplished by the P-type ATPase subunit KdpB"];
  Asp307 is the phosphoenzyme site and Ser162 phosphorylation is inhibitory
  [PMID:28636601 "the inverse correlation between the relative levels of Ser162 phosphorylation and ATPase activity supports the inhibitory nature of this modification"].
- Core MF: GO:0016887 ATP hydrolysis activity, contributes_to GO:0008556 (complex activity; KdpA
  supplies the selectivity filter, KdpB the energy coupling and cytoplasmic release site
  [PMID:34272288 "ATP hydrolysis is coupled to K+ transfer between alternative sites in KdpB"]).
  GOA "enables GO:0008556" rows accepted. Consistent with the Kdp module and PSEPK kdpB.
- GO:1903103 potassium:proton antiporter complex (IBA + ComplexPortal IPI) is a term mis-mapping:
  MODIFY to GO:0031004, source_defects recorded (GO_CENTRAL, INTACT).
- General terms (nucleotide binding, membrane, potassium ion transport, monoatomic cation
  transmembrane transport) MODIFY to their specific descendants already on the gene.


## 2026-11-07 E. coli Kdp module consultation

Reviewed all existing annotation claims against the cached primary literature, UniProt record, and current GO definitions. Original ordered annotation payloads and source files were frozen before editing; no new annotation rows were added. The two inherited KdpD NEW proposals remain present. Detailed decisions and source scope are recorded in `analysis/module_audits/bacterial_kdp_potassium_homeostasis/ecoli-consultation/`.

A genuine configured Falcon research request was attempted for this gene and failed with HTTP 403 authentication; no provider report was fabricated. The exact attempt log is `.cache/module-audit-logs/kdp-20261107/ecoli-consultation/falcon-kdpB.log`. PAINT-loss checking found no IRD/IKR loss on the recorded lineage.

The stale KdpC-at-the-cytoplasmic-nucleotide-pocket assertion was removed from the biological description. PMID:34272288 and PMID:41259220 support KdpB ion transfer and cytoplasmic release as well as ATP catalysis. PMID:38622146 identifies KdpD as the inhibitory Ser162 kinase, resolving the old question. Mg binding supports the catalytic machinery and is core. Three identical UniProt reference entries were consolidated without removing distinct findings. The 2017 nucleotide-empty structure is not described as a bound-ATP assay.
