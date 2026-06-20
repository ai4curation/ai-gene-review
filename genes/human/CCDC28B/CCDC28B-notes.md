# CCDC28B (Q9BUN5) — Gene Review Notes

Human gene, HGNC:28163, GeneID 79140, chromosome 1. Also known historically as MGC1203.
Small protein (200 aa, isoform 1), one C-terminal predicted coiled coil (158–183), two
disordered regions (1–49, 141–164). Part of the "Human BBSome" curation project.

## Summary of biological role

CCDC28B is an accessory/modifier factor of the BBSome and ciliary trafficking machinery,
not a numbered structural BBS subunit. It was identified as a second-site (epistatic)
modifier of Bardet–Biedl syndrome (BBS). It localizes near centrosomes/basal bodies,
interacts with multiple BBSome subunits, and is required for normal ciliogenesis and
control of cilium length.

## Provenance / key findings

- Identified as a novel epistatic modifier locus (MGC1203/CCDC28B) for BBS; encodes a
  pericentriolar protein that interacts and colocalizes with BBS proteins. A heterozygous
  C430T variant enriched in BBS patients reduces steady-state mRNA; zebrafish mgc1203
  knockdown enhances the BBS-morphant developmental phenotype.
  [PMID:16327777 "MGC1203 encodes a pericentriolar protein that interacts and colocalizes with the BBS proteins"]
  [PMID:16327777 "modest suppression of mgc1203 exerts an epistatic effect on the developmental phenotype of BBS morphants"]

- UniProt (from PMID:16327777): "Interacts with BBS1, BBS2, BBS4, BBS5, BBS6, BBS7 and
  TTC8/BBS8." Subcellular location: "Cytoplasm, cytoskeleton, microtubule organizing
  center, centrosome ... localizes near centrosomes and basal bodies."

- First functional characterization: CCDC28B affects ciliogenesis in cultured cells and
  in vivo in zebrafish; homologs restricted to ciliated metazoa. Ccdc28b depletion in
  zebrafish causes defective ciliogenesis with hydrocephalus, left-right axis defects and
  renal impairment — hallmark ciliopathy phenotypes.
  [PMID:23015189 "show it affects ciliogenesis both in cultured cells and in vivo in zebrafish"]
  [PMID:23015189 "the presence of CCDC28B homologous sequences is restricted to ciliated metazoa"]
  [PMID:23015189 "Depletion of Ccdc28b in zebrafish results in defective ciliogenesis"]

- Cilium length control via SIN1/mTORC2 axis: CCDC28B interacts with SIN1 (MAPKAP1),
  positively regulates mTORC2 assembly/stability/activity (not mTORC1), and controls
  ciliary length partly through SIN1 in an mTOR-independent manner. RICTOR depletion does
  NOT shorten cilia, separating the cilia-length role from canonical mTORC2 signaling.
  [PMID:23727834 "CCDC28B is a positive regulator of mTORC2, participating in its assembly/stability and modulating its activity, while not affecting mTORC1 function"]
  [PMID:23727834 "Ccdc28b regulates cilia length in vivo, at least in part, through its interaction with Sin1"]
  [PMID:23727834 "depletion of Rictor ... does not result in shortened cilia"]

- High-throughput binary interactome (Y2H) reports CCDC28B–ATRIP (Q8WXE1) interaction.
  [PMID:25416956 "a systematic map of ~14,000 high-quality human binary protein-protein interactions"]

## GO annotation assessment

Existing GOA (6 stub entries; GOA TSV has more IPI WITH rows collapsed):

1. GO:0005813 centrosome, IBA (GO_REF:0000033) — consistent with localization near
   centrosomes/basal bodies; phylogenetic inference. ACCEPT (non-core localization; the
   functional core is ciliogenesis/BBSome modulation).
2. GO:0005813 centrosome, IEA (GO_REF:0000044, SubCell mapping) — same localization,
   electronic. Redundant with the experimental IDA. ACCEPT / KEEP_AS_NON_CORE.
3. GO:0005515 protein binding, IPI (PMID:16327777, WITH BBS4 Q96RK4 etc.) — uninformative
   MF ("protein binding"). The underlying biology (BBSome subunit binding) is real and is
   better captured by BBSome localization / ciliogenesis terms. MARK_AS_OVER_ANNOTATED
   (protein binding is discouraged per curation guidelines; not a useful MF).
4. GO:0005515 protein binding, IPI (PMID:25416956, WITH ATRIP Q8WXE1) — high-throughput
   binary interactome hit; uninformative term, single Y2H. OVER_ANNOTATED.
5. GO:0005813 centrosome, IDA (PMID:16327777) — direct experimental localization near
   centrosomes. ACCEPT (core localization).
6. GO:0060271 cilium assembly, IMP (PMID:23015189) — strongest functional annotation;
   IMP from loss-of-function in cells and zebrafish. ACCEPT (core function).

GO:0034464 (BBSome) is a cellular_component term for the complex; CCDC28B interacts with
BBSome subunits but is a modifier/accessory factor, not confirmed as a stable BBSome
component, so I do not propose a "part_of BBSome" CC annotation. Could be a question for
experts. Relevant process terms: regulation of cilium length (consider GO:0090660? — not
verified) — left as a suggested area.
