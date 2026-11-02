# Irak3 (mouse, Q8K4B2) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

No prior review existed for this gene. This review does not use any ProtNLM2 output.

### Process

- `just fetch-gene mouse Irak3` created the UniProt, GOA (91 rows) and stub files.
- `just fetch-gene-pmids mouse Irak3` cached all 7 cited PMIDs.
- Deep research failed. Falcon gave "Exception: Failed to authenticate" and the perplexity-lite fallback gave HTTP 401 for
  insufficient quota, so no deep-research file exists. The review uses the cached primary literature instead: two
  full-text mouse papers (PMID:23376919, PMID:29686383), abstracts of the remaining papers, and the human IRAK3
  structure paper (PMID:33238146, full text).

### Evolutionary grounding

- PANTHER 19.0 HMM classification (`.cache/panther/PTHR19.0_mouse`, `PTHR19.0_human`) puts both mouse Irak3 (Q8K4B2)
  and human IRAK3 (Q9Y616) in PTHR24419:SF7 (INTERLEUKIN-1 RECEPTOR-ASSOCIATED KINASE 3). The UniProt Q8K4B2 DR line
  instead lists PTHR27001:SF929, which is a different cross-reference source; the 19.0 classification is used here.
- The motif comparison (`Irak3-bioinformatics/RESULTS.md`) gives 74.5% identity over the global alignment. Human CGS
  291-293 aligns to mouse CGN 304-306, so the catalytic aspartate is absent and Asn-306 replaces it, as the UniProt
  CAUTION also states. Human DFA 311-313 aligns to mouse DFA 324-326. The VAIK lysine (K205), the death-domain W74 and
  the PIN1 Pro-directed site (mouse Thr110-Pro111, human Ser110-Pro111) are conserved.
- Transfers from human IRAK3 are therefore orthologue transfers within one subfamily. Kinase activity from IRAK1 or
  IRAK4 (other subfamilies) is not transferred.

### What is experimentally established in mouse and what is inferred

Established in mouse:
- [PMID:12150927 "IRAK-M prevented dissociation of IRAK and IRAK-4 from MyD88 and formation of IRAK-TRAF6 complexes."]
  The knockout shows negative regulation of TLR/IL-1R signaling, increased cytokine production, reduced endotoxin
  tolerance, and stronger inflammatory responses to bacterial infection.
- [PMID:23376919 "IRAK-M was also able to interact with MyD88-IRAK-4 to form IRAK-M Myddosome to mediate TLR7-induced
  MEKK3-dependent second wave NFκB activation"]. The paper also reports death-domain W74A loss of IRAK4 binding,
  interaction with TRAF6, MEKK3 and IRAK-2 (not IRAK-1), and an inhibitory effect on cytokine translation.
- [PMID:17379480 "IRAK-M selectively attenuates p38 activation and inhibits innate immunity through stabilizing MKP-1."]
- [PMID:29686383 "Upon IL-33-induced airway inflammation, PIN1 is activated for binding with and isomerization of
  IRAK-M, resulting in IRAK-M nuclear translocation and induction of selected proinflammatory genes in dendritic
  cells."] The paper also shows predominantly cytoplasmic localisation at rest.

Inferred from human IRAK3 (no direct mouse data):
- The head-to-head pseudokinase homodimer, weak ATP binding, the transient complex with phospho-IRAK4 through the
  pseudokinase domain, and the absence of Mg/ATP thermal stabilisation (all from PMID:33238146).
- Guanylate cyclase activity has been reported for human IRAK3 (PMID:31664109, cited in the human review). It has not
  been examined for mouse Irak3, and no annotation is proposed.

Contested:
- PMID:12054681 (abstract only) reports kinase-activity similarity to human IRAK-M. UniProt notes the low-level
  autophosphorylation as discordant. All rows for kinase activity, Mg binding, protein phosphorylation and
  autophosphorylation are REMOVED. The reasons are a contradicted function (no catalytic aspartate, DFA loop,
  negligible autophosphorylation of the orthologue, catalytically inactive in structural work), not a guess about
  what the curator read.

### Decisions worth flagging

- Protein binding rows: TRAF6 is changed to ubiquitin protein ligase binding, IRAK4 (mouse and human) to protein kinase
  binding, and the PIN1 row is removed because Irak3 is the substrate.
- The apoptosis RCA rows (PMID:12819136, a domain inventory) are removed.
- The Toll signaling pathway IBA (Drosophila pelle/tube node) is marked as over-annotated because the vertebrate TLR
  and IL-1R terms already cover the function.
- Positive regulation of canonical NF-kB (the IRAK-M Myddosome second wave) is kept as non-core. Its net output is
  inhibitory gene induction.
- The general terms (MAPK cascade, cytokine-mediated signaling, complex disassembly, innate immune response, NF-kB
  regulation, signal transduction) are refined to p38MAPK, IL-1, negative, and MyD88-dependent TLR terms.
