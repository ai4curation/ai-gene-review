# ANXA1 (Annexin A1; lipocortin 1) review notes

UniProt: P04083. Human, NCBITaxon:9606. PANTHER PTHR10502:SF17 (ANNEXIN A1).

## Deep research status

- 2026-10-05: `just deep-research-falcon human ANXA1` failed with Edison API
  `429 Too Many Requests` (no perplexity key available for fallback). Retried once.
  Review proceeds from cached GOA-cited publications, the UniProt record and a few
  additional PubMed-retrieved papers (PMID:19104500, PMID:12475898, PMID:32272059,
  PMID:10673436, PMID:8425544, PMID:9425121), fetched with `just fetch-pmid`.

## Molecular properties

- Classical annexin: N-terminal ~40 aa unique domain + four ~70 aa annexin repeats
  (IPR001464, IPR018502); ANXA1-specific IPR002388.
- Calcium binding and Ca2+-dependent binding to anionic phospholipids
  [UniProt P04083 "Displays Ca(2+)-dependent binding to phospholipid membranes"].
  - Ca2+ requirement lowest for phosphatidic acid, then PS, then PI; no PC binding
    [PMID:2138016 "The Ca2+ requirement for all of the proteins was lowest for binding to vesicles composed of phosphatidic acid, followed by phosphatidylserine and then phosphatidylinositol."]
  - Placental transglutaminase-crosslinked dimer also binds PS vesicles
    [PMID:2532504 "display Ca2+-dependent binding to phosphatidylserine-containing vesicles"].
  - Promotes aggregation and fusion of liposomes in vitro
    [PMID:2138016 "Lipocortin I promoted fusion of liposome membranes by lowering threshold Ca2+ concentrations."].
- N-terminal tail binds S100A11 (S100C) in Ca2+-dependent manner; heterotetramer model
  [PMID:8557678 "the 10-kDa protein bound specifically to a site within the first 12 amino acids of annexin I"]
  [PMID:10673436 "We have solved the crystal structure of a complex of calcium-loaded S100C with a synthetic peptide that corresponds to the first 14 residues of the annexin I N terminus"].
- Substrate of EGFR kinase, PKC; transglutaminase cross-linking on Gln18
  [PMID:3013422 "lipocortin I and the 35 kd substrate for the EGF-receptor/kinase from A431 cells are the same protein"].
- Cleaved by cathepsin G to release the bioactive N-terminal Ac2-26 peptide
  [PMID:22879591 "In vitro , CG efficiently cleaved AnxA1, releasing the active N-terminal peptide Ac2-26"].

## "Phospholipase A2 inhibitor" history

- Originally cloned as a glucocorticoid-induced PLA2 inhibitor
  [PMID:2936963 "Our studies confirm that lipocortin is a potent inhibitor of phospholipase A2 activity."].
- The in vitro inhibition is now generally explained by substrate (phospholipid
  interface) sequestration rather than direct enzyme binding
  [PMID:9425121 "a substrate depletion mechanism is now widely accepted as the explanation for most inhibitory studies"];
  UniProt: "Inhibition of phospholipase activity is mediated via its phospholipid binding activity that limits the access of phospholipase to its substrates."
- Conclusion: the GO MF "phospholipase A2 inhibitor activity" (binds to and inhibits
  the enzyme) over-states the mechanism; not chosen as a core function.

## Extracellular ligand of formyl peptide receptors (core function)

- ANXA1 N-terminal peptides are FPR ligands on human neutrophils, inhibit
  transendothelial migration [PMID:10882119 "Peptides derived from the unique N-terminal domain of annexin I serve as FPR ligands and trigger different signaling pathways in a dose-dependent manner."]
- Ac2-26 activates FPR1, FPR2 (FPRL1) and FPR3 (FPRL2); chemotaxis then desensitisation
  [PMID:15187149 "a peptide derived from the N-terminal domain of the anti-inflammatory protein annexin 1 (lipocortin 1) can activate all three FPR family members at similar concentrations."]
- Inhibits ACTH exocytosis via FPR and Rho kinase / actin polymerisation
  [PMID:19625660 "annexin A1-dependent inhibition of adrenocorticotrophin release involves the enhancement of actin polymerization to prevent exocytosis via formyl peptide receptor and Rho kinase signaling pathways"].
- Secreted in EVs from intestinal epithelium, promotes wound repair
  [PMID:25664854 "endogenous annexin A1 (ANXA1) is released as a component of extracellular vesicles (EVs) derived from intestinal epithelial cells, and these ANXA1-containing EVs activate wound repair circuits"].
- Leaderless secretion via TMED10 channel into ERGIC [PMID:32272059 "We identify TMED10 as a protein channel for the vesicle entry and secretion of many leaderless cargoes."]
  (ANXA1 is named as a cargo in the UniProt record citing this paper).
- Externalised from neutrophil gelatinase granules on adhesion
  [PMID:10772777 "Neutrophil adhesion to monolayers of endothelial cells, but not phagocytosis of particles of opsonized zymosan, provoked an intense mobilization of annexin I, with a marked externalization on the outer leaflet of the plasma membrane."]

## Anti-inflammatory / pro-resolving physiology

- Glucocorticoid effector [PMID:19104500 "we propose a model in which glucocorticoids regulate the expression and function of annexin A1 in opposing ways in innate and adaptive immune cells to mediate the resolution of inflammation."]
- Knockout mice: exaggerated inflammation, increased leukocyte emigration and IL-1beta,
  glucocorticoid resistance, phagocytosis anomalies
  [PMID:12475898 "Anx-1-/- mice exhibit an exaggerated response to the stimuli characterized by an increase in leukocyte emigration and IL-1beta generation and a partial or complete resistance to the antiinflammatory effects of glucocorticoids."]
- Bone-marrow neutrophil clearance by macrophages requires AnxA1
  [PMID:21957127 "we conclude that expression of AnxA1 by resident macrophages is a critical determinant for neutrophil clearance in the bone marrow."]
- Apoptotic-cell surface ANXA1 suppresses macrophage IL-8/MIP-2 [PMID:22056994].

## Adaptive immunity

- Recombinant ANXA1 enhances TCR signalling, IL-2, proliferation, Th1 skewing
  [PMID:17008549 "differentiation of naive T cells in the presence of annexin-1 increased skewing in Th1 cells"]. Non-core, context dependent.

## Other reported roles (non-core)

- Cornified envelope component of oral keratinocytes [PMID:10908733].
- Endothelial migration downstream of VEGF, regulated by miR-196a [PMID:22773844].
- Co-occupies SNX3/ANXA2-positive endosomes [PMID:18767904].
- NEMO/RIP1 interaction and NF-kB activity in breast cancer cells [PMID:21383699].
- Many HDA proteomic detections: exosomes, tears, ECM, focal adhesion, E-cadherin interactome.

## Curation decisions summary

- Core MF: calcium-dependent phospholipid binding (PS), receptor ligand activity (FPR agonist).
- Core BP: negative regulation of inflammatory response / regulation of leukocyte
  migration via FPR (GPCR) signalling.
- Generic protein binding IPI rows: REMOVE per project policy (uninformative); S100A11
  binding proposed as NEW GO:0044548 S100 protein binding.
- GO:0007187 (GPCR signalling coupled to cyclic nucleotide second messenger): FPR signalling
  is Gi/Ca2+/MAPK; generalise to GO:0007186.
- No GO-CAM model in gocams/index.tsv contains P04083.
