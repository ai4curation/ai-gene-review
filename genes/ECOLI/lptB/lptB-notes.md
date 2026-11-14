# lptB (E. coli K-12, P0A9V1) review notes

## Sources and provenance

- Provider deep research (`just deep-research`) was **not** run for this gene; no
  `-deep-research-*.md` file exists. The review is built from the UniProt record
  (`lptB-uniprot.txt`), the GOA rows, and the cached publications below.
- Cached full text: PMID:17056748, PMID:24639492, PMID:27795402, PMID:29449493,
  PMID:30894744. Abstract-only: PMID:16079137, PMID:19500581.
- No extra PMIDs were fetched.
- Style/consistency model: `genes/PSEPK/lptB/lptB-ai-review.yaml`.

## Key biology

- LptB is the homodimeric NBD of the LptB2FG ABC transporter; LptC associates to
  form LptB2FGC [PMID:24639492 "Three of these Lpt proteins form an ABC system
  composed of a heteromeric TMD complex (LptF and LptG) and a homodimeric NBD
  complex (LptB)."].
- ATP hydrolysis by LptB is essential in vivo [PMID:24639492 "Our studies establish
  the essentiality of ATP hydrolysis by LptB to power LPS transport in cells"].
- LptB2FG extracts rather than translocates LPS [PMID:30894744 "Unlike most other
  ABC transporters translocating substrates across the membrane, LptB2FG extrudes
  LPS out of the membrane"]. MsbA performs the transmembrane flip
  [PMID:17056748 "Translocation across the IM requires the ABC transporter MsbA"].
- LptF/LptG coupling helices dock in the LptB groove [PMID:27795402 "a specific
  binding site in LptB for the coupling helices of LptFG"].

## Judgment calls

- Core MF kept as GO:0016887 ATP hydrolysis activity, consistent with PSEPK lptB.
  Transporter-class terms (GO:0140359, GO:0042626) are defined as movement across
  a membrane, which LptB2FG does not do; GO:0015437 LPS floppase is MsbA's activity;
  GO:0140332 LPS transfer activity is used for LptC-type LPS-binding proteins. Raised
  as a suggested question instead of asserting a contributes_to MF.
- GO:0055085 transmembrane transport (IEA): MODIFY to GO:0015920, because of the
  extraction mechanism above; the P. putida LptB review now makes the same MODIFY.
- GO:1990351 transporter complex: MODIFY to GO:0062051 lipopolysaccharide transport
  system (its definition cites PMID:29449493, the source paper of the row).
- GO:0016020 membrane (NAS): MODIFY to GO:0005886 plasma membrane.
- GO:0005515 (IPI, LptF/LptG): REMOVE per protein-binding policy; captured by
  ABC transporter complex membership.
- No history record was added (task restricted edits to this folder).

## 2026-11-02 revision (PR review round)

- GO:0043165 Gram-negative-bacterium-type cell outer membrane assembly changed from
  KEEP_AS_NON_CORE to ACCEPT and added to core processes, so all seven E. coli Lpt
  reviews treat the term the same way (each subunit is a required part of the machine
  that builds the LPS outer leaflet).


## 2026-11-07 — cross-taxon Lpt audit, E. coli member consultation

All original annotation rows, reference findings and core roles were reassessed. Source payloads/order, qualifiers and historical NEW lifecycle remain unchanged. Targeted full-primary reading supports the existing division between LptB ATPase, membrane extractor subunit contributions, bridge transfer and terminal LptDE translocation. Abstract-only source details are not treated as disproven or silently relabeled as newly inspected full-text evidence. Generic location/assembly quotations were strengthened where appropriate; no new annotation was added. PMID42844470 updates whole-bridge regulation: E. coli proteins and an engineered LptC-LptA fusion support the structural analysis, with E. coli functional controls; LPS-null A. baylyi is an expression host, not a new organismal activity assay. The normal cache remains abstract-only; independently acquired publisher full text is documented in the shared literature consultation. The normal PAINT-loss check reports no IRD/IKR loss on this target lineage; this is not a whole-family uniformity claim. Default Falcon research was attempted normally and failed HTTP403 authentication; no provider report was created or overwritten. Manual source/ontology/preservation evidence is in analysis/module_audits/bacterial_lps_transport/ecoli-consultation/.
