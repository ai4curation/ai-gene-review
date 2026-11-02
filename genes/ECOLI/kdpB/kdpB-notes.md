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
