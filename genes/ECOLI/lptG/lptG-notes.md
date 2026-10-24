# lptG (P0ADC6) review notes

## 2026-10-23 — initial full review

Provider deep research was **not** run for this gene; no `-deep-research-*.md` file exists.
The review is based on the cached publications below, the UniProt record
(`lptG-uniprot.txt`) and the Pseudomonas putida orthologue reviews
(`genes/PSEPK/PP_0982`, `genes/PSEPK/PP_0983`) used as style models.

Sources used:
- PMID:18375759 (Ruiz et al. 2008, full text): discovery of YjgP/YjgQ as LptF/LptG;
  both essential; depletion blocks LPS reaching the cell surface
  [PMID:18375759, "We conclude that, under these conditions, LPS does not reach the cell surface."].
- PMID:19500581 (Narita & Tokuda 2009, abstract only): LptF and LptG form a complex with
  LptB and LptC [PMID:19500581, "We report here that both LptF and LptG formed a complex with LptB."].
- PMID:27795402 (Simpson et al. 2016, full text): LptF/LptG coupling helices bind the LptB groove.
- PMID:29449493 (Sherman et al. 2018, full text): reconstitution of the LptB2FGC-LptA-LptDE bridge.
- PMID:30894744 (Li, Orlando & Liao 2019, full text): cryo-EM of LptB2FG/LptB2FGC with bound LPS
  [PMID:30894744, "Six lipid acyl chains of LPS tightly fit into a cone-shaped hydrophobic pocket formed by TMs 1, 2, and 5 of LptF and LptG"].
- PMID:15919996, PMID:17309111 (abstract only): inner-membrane topology / proteomics; localization only.

No additional PMIDs were fetched.

## Judgment calls

- Molecular function: core function uses **contributes_to GO:0140332 lipopolysaccharide transfer
  activity** (added as a NEW row), rather than GO:0015221 lipopolysaccharide transmembrane
  transporter activity used in the PSEPK review. Reason: E. coli structures show LptB2FG extrudes
  LPS out of the membrane rather than across it, which matches GO:0140332's definition (removal
  from the donor-membrane outer leaflet) better than a trans-bilayer transporter activity.
  LptG does not have the activity alone, hence contributes_to. Both lptF and lptG reviews use the
  same choice. An ontology question about an "LPS extraction" activity is raised in suggested_questions.
- GO:0055085 transmembrane transport (IEA) -> MODIFY to GO:0015920, for the same mechanistic reason.
- GO:1990351 transporter complex (IDA, PMID:29449493) -> MODIFY to GO:0062051 lipopolysaccharide
  transport system (child term whose definition cites that paper).
- GO:0016020 membrane rows -> MODIFY to GO:0005886 plasma membrane.
- GO:0043165 outer membrane assembly -> KEEP_AS_NON_CORE (broader downstream process).
- Bare GO:0005515 rows -> REMOVE per protein-binding policy (interactions with LptB, LptF, LptC are
  real intra-complex contacts captured by complex terms).
