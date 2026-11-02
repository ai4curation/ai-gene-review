# TLR4 (human, O00206) review notes

## Provenance of inputs

- Falcon deep research (`TLR4-deep-research-falcon.md`) arrived after the review was written from
  the UniProt record, the 61 cached GOA publications, OLS look-ups and a QuickGO query for
  GO:0001875; see the cross-check section below.
- 275 seeded GOA rows (from 279 tsv lines); 31 are generic `protein binding` IPI rows; 34 are
  Reactome TAS location rows; 1 is a NOT row (row 147, GO:0031663, PMID:10880523).

## Deep-research cross-check (2026-09-30)

The Falcon report is built almost entirely on secondary reviews (2020-2025) and adds little
mechanistic detail beyond what the review already takes from primary papers.
- **Agreement:** type I TM receptor with LRR ectodomain and TIR domain; LPS delivered by LBP/CD14
  to TLR4-MD-2, ligand-induced homodimerisation; MyD88/TIRAP at the plasma membrane and
  CD14-dependent endocytosis then TRAM/TRIF signalling from endosomes; engagement by endogenous
  DAMPs (HMGB1, oxLDL, amyloid-beta). Consistent with all core functions, locations and the
  ACCEPT/KEEP_AS_NON_CORE decisions. The falcon file is cited as context on the two GO:0035666
  TRIF-dependent pathway rows.
- **Additions (not used):** a long list of review-level DAMP "ligands" (HSP60/70/90,
  S100A8/A9, fibrinogen, fibronectin, heparan sulfate, hyaluronan, versican, mtDNA) and
  therapeutic agents (TAK-242, eritoran, AS04/MPLA, neoseptins). The report itself notes that
  direct-ligand claims need exclusion of endotoxin contamination; none was verified in a primary
  paper, so no binding or receptor-activity annotations were added.
- **Apparent conflict, not a real one:** the report lists amyloid-beta as a TLR4 ligand, whereas
  the review REMOVEs GO:0001540 amyloid-beta binding. The report only says amyloid-beta is
  "reported to activate microglial TLR4-associated inflammatory responses" (from a secondary
  review), and the primary paper assigns ligand binding to CD36 [PMID:20037584 "CD36 that acts
  as the common ligand binding receptor for oxLDL and β-amyloid"]. Decision unchanged.
- Changes: falcon file added to references and cited on 2 rows; no action, term, description or
  core-function changes.

## Core biology (with provenance)

- Cloned as the first human homologue of Drosophila Toll; type I transmembrane protein with an
  ectodomain of leucine-rich repeats and a cytoplasmic TIR domain; a constitutively active form
  drives NF-kB and IL-1/IL-6/IL-8 and B7.1 expression [PMID:9237759 "Like Drosophila Toll, human Toll is a type I transmembrane protein"].
- LPS receptor: HEK293 cells transfected with TLR4 respond to LPS/CD14 [PMID:10196138 "TLR4 is involved in lipopolysaccharide signaling and serves as a cell-surface co-receptor for CD14"].
  Human genetic evidence: Asp299Gly blunts inhaled LPS responses [PMID:10835634 "the Asp299Gly mutation (but not the Thr399Ile mutation) interrupts TLR4-mediated LPS signalling"].
- Receptor complex: LPS cross-links to TLR4 and MD-2 only when CD14 is co-expressed [PMID:11274165 "LPS is cross-linked specifically to TLR4 and MD-2 only when co-expressed with CD14"].
- Structure: TLR4 and MD-2 form a heterodimer; LPS five acyl chains sit in the MD-2 pocket and the
  sixth contacts TLR4 phenylalanines; LPS phosphates contact TLR4 and MD-2 positive residues; LPS
  bridges two TLR4-MD-2 units into an m-shaped dimer [PMID:19252480 "LPS binding induced the formation of an m-shaped receptor multimer composed of two copies of the TLR4-MD-2-LPS complex"].
  MD-2 binds the concave face of TLR4 N-terminal/central LRR domains [PMID:17803912 "MD-2 binds to the concave surface of the N-terminal and central domains"].
- MD-2 is required for surface localisation of TLR4 and LPS recognition [PMID:12055629 "MD-2 is essential for correct intracellular distribution and LPS-recognition of TLR4"].
  Human TLR4 alone (no MD-2) in Ba/F3 cells does not respond to lipid A, whereas MD-2 or RP105-MD-1 restore it [PMID:10880523 "the Ba/F3 cells that express human TLR4 alone do not respond to lipid A"].
- Two adaptor branches: MyD88/TIRAP at the plasma membrane; TRAM/TRIF after endocytosis
  [PMID:18222170 "TLR4 activates TRIF-signaling in endosome/lysosome after relocation from the cell surface"];
  TIRAP recruits MyD88 to activated TLR4 [PMID:16751103 "TIRAP then functions to facilitate MyD88 delivery to activated TLR4 to initiate signal transduction"].
  TIR-domain mutations of TLR4 abrogate adaptor binding [PMID:21829704 "Mutations in a protein-protein interaction domain, Toll/IL-1R intracellular domain (TIR), of RAGE and TLR4"].
- Non-LPS ligands / sterile inflammation: oxLDL and amyloid-beta trigger a CD36-dependent TLR4-TLR6
  heterodimer; CD36 is the ligand-binding receptor and MD-2 is not required [PMID:20037584 "CD36 that acts as the common ligand binding receptor for oxLDL and β-amyloid"; "TLR4-TLR6-mediated NF-κB activation occurred in the absence of MD-2"].
  Ni2+/Co2+ drive MD-2-independent TLR4 homodimerisation [PMID:23059983 "only LPS- but not metal-induced dimerization required MD2"]; HMGB1 [PMID:20547845], tenascin-C [PMID:29150600] and PAUF/ZG16B [PMID:36232715] also act through TLR4.
- TLR4 is recruited to the phagocytic cup and TLR4-TRAM-TRIF signalling promotes E. coli phagocytosis [PMID:30883606 "TLR4 is recruited to the phagocytic cup to provide a platform for subsequent TRAM-TRIF signalling"].

## Which MF belongs to TLR4 vs MD-2 (LY96) / CD14

- GO:0001875 LPS immune receptor activity = "Combining with a lipopolysaccharide and transmitting the
  signal across the cell membrane to initiate an innate immune response" (OLS). Only TLR4 spans the
  membrane and carries the TIR domain; MD-2 is secreted/extracellular and CD14 is GPI-anchored. The
  signal-transmitting part of the definition is therefore executed by TLR4 alone.
- LPS contact is shared: most of the lipid A sits in MD-2; TLR4 contributes the contact for the sixth
  acyl chain and phosphate ion pairs, and the dimerisation interface. So GO:0001530 LPS binding on
  TLR4 is defensible, but most binding energy is in MD-2.
- QuickGO (2026-09-30): GO:0001875 is annotated `enables` to TLR4 (IBA, IDA PMID:19252480), LY96
  (IBA, IDA PMID:19252480) and CD14 (IDA PMID:15294986), and `contributes_to` for TLR1/2/6. The LY96
  and CD14 rows use `enables`; given the definition's transmembrane-transmission clause, `contributes_to`
  would describe MD-2 better (question raised in suggested_questions; not edited here, LY96/CD14 are
  other agents' genes).
- GO-CAM models (`gocams/index.tsv`) type TLR4 as GO:0038023 signaling receptor activity in ~10 human
  models (one uses GO:0001875); LY96 appears in none of them.

## Curation decisions of note

- NOT GO:0031663 (IDA, PMID:10880523): the experiment tested human TLR4 expressed without MD-2; the
  same paper (IGI rows) shows TLR4 signals LPS with MD-2 or RP105/MD-1. The negation reflects a missing
  obligate co-receptor, not absence of function -> REMOVE.
- GO:0001540 amyloid-beta binding (IC from PMID:20037584): the paper assigns ligand binding to CD36 ->
  REMOVE.
- GO:0071260 cellular response to mechanical stimulus (IEP, PMID:19593445): the cached full text
  (BAD in prostate cancer) never mentions TLR4, Toll or mechanical stimuli; possible reference error in
  GOA -> UNDECIDED, reference flagged.
- GO:0045671 negative regulation of osteoclast differentiation (NAS PMID:12133979): mouse osteoclast
  precursors, pan-TLR ligands; kept as non-core.
- Mouse-derived negative-regulation cytokine rows (IFN-gamma, IL-17, IL-23, IL-6, TNF) contradict the
  receptor's activating role and are context-specific knockout phenotypes -> MARK_AS_OVER_ANNOTATED.
- Protein binding: REMOVE, except rows where the cited paper documents TIR-mediated adaptor binding
  (PMID:21829704, PMID:19509286) -> MODIFY to GO:0070976 TIR domain binding; TLR6/CD36 row ->
  GO:0035325 Toll-like receptor binding.
- miRNA papers (PMID:30321456, 30233718, 21329689) are knockdown/target studies; accepted as
  non-core cytokine/NF-kB regulation.
