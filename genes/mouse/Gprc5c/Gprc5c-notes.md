# Gprc5c (mouse, Q8K3J9) review notes

Deep research via `just deep-research-falcon` was not available in this session
(authentication failure), so literature research was done directly from PubMed
(39 hits for Gprc5c/GPRC5C/RAIG3, 2026-10-19) and the cached publications below.
Context: [RAR_MISANNOTATION](../../../projects/RAR_MISANNOTATION.md), re-examining
the `GO:0005118 sevenless binding` flag from Wei et al. 2020
[PMID:32470107 "We proposed a new approach to detect potentially incorrect Gene Ontology (GO) annotations by comparing the ratio of annotation rates (RAR)"].

## Identity and family

- Gprc5c (RAIG-3) is a retinoic-acid-inducible class C (family 3) orphan GPCR
  with a short N-terminus, unlike other class C receptors
  [PMID:10945465 "in contrast to other type 3 GPCRs, RAIG-1, RAIG-2, and RAIG-3 have only short N-terminal domains"].
  Epitope-tagged human RAIG-3 reached the cell surface in HEK293T cells and is
  induced by all-trans retinoic acid
  [PMID:10945465 "Transient transfection experiments in HEK239T cells using these constructs demonstrated RAIG-2 and RAIG-3 expression at the cell surface"].
- UniProt Q8K3J9: 440 aa, signal peptide 1-22, extracellular N-terminus 23-49,
  7TM (TM1 50-70 ... TM6 241-261); "Belongs to the G protein-coupled receptor 3 family".
- GPRC5 receptors are chordate-specific; invertebrate "GPRC5-like" sequences,
  including Drosophila BOSS, are only distantly related and have long N-termini
  [PMID:21827690 "Invertebrates have sequences that were previously classified as GPRC5-like, e.g. BOSS in D. melanogaster and other insects"]
  [PMID:21827690 "The invertebrate receptors have long N-termini, like other class C GPCRs and unlike GPRC5 receptors in Chordata"]
  [PMID:21827690 "Together our results suggest that GPRC5 receptors seem to be a chordate specific class of GPCRs."].

## The sevenless-binding question (IPR002956)

- IPR002956 = "Bride of sevenless protein" family, built from a single PRINTS
  fingerprint (PR01223 BRIDEOF7LESS). Its InterPro2GO mappings are
  GO:0005118 sevenless binding, GO:0007601 visual perception, GO:0016020 membrane
  [file:mouse/Gprc5c/Gprc5c-bioinformatics/RESULTS.md "InterPro2GO terms: GO:0005118 sevenless binding; GO:0007601 visual perception; GO:0016020 membrane"].
- Among Swiss-Prot entries, only the two Drosophila BOSS proteins and mouse Gprc5c
  match it; human GPRC5C, mouse/human GPRC5A/B and human GPRC5D do not
  [file:mouse/Gprc5c/Gprc5c-bioinformatics/RESULTS.md "Q9NQ84 human GPRC5C: IPR002956 match = no"].
  The match on mouse Gprc5c is two fingerprint segments (48-73, 241-265),
  essentially TM1 and TM6, i.e. generic 7TM sequence, not the BOSS ectodomain.
- BOSS binds Sevenless through its large extracellular region; the binding
  epitope is a C-terminal peptide of the BOSS ECR
  [PMID:39827240 "Activation of dROS1 is mediated by binding to the extracellular region (ECR) of the GPCR (G protein coupled receptor) BOSS (Bride Of Sevenless) on adjacent cells."]
  [PMID:39827240 "This includes beta-strands in dROS1's third Fibronectin type III (FNIII) domain and a C-terminal peptide in BOSS' ECR."].
  Gprc5c has a 27-residue extracellular N-terminus and therefore lacks the
  structure that does the binding.
- BOSS orthologs are recognisable outside Diptera only by the 7TM domain; the ECR
  co-evolves fast with Sevenless, and vertebrate c-Ros ligands were unknown
  [PMID:18392882 "The extracellular region, however, is only detectably conserved within but not outside Diptera."]
  [PMID:18392882 "Remarkably, vertebrate ligands of c-Ros as well as non-Drosophila orthologs of the Sevenless ligand Bride of sevenless have remained elusive."].
- The mammalian ROS1 ligand turned out to be NELL2, a secreted EGF-like protein,
  not a GPCR [PMID:32499443 "neural epidermal growth factor-like-like 2 (NELL2), specifically binds to an orphan receptor tyrosine kinase, c-ros oncogene 1 (ROS1)"].
- PubMed search "(ROS1 OR c-ros) AND (GPRC5C OR GPRC5B OR GPRC5A OR bride of sevenless OR RAIG)"
  returned only Drosophila Sevenless/BOSS papers and an unrelated rat colon study:
  no evidence links any GPRC5 receptor to ROS1.
- Verdict: the Wei et al. flag holds, but for the reason the project page
  anticipated: it is the InterPro2GO mapping on a weak, species-idiosyncratic
  PRINTS hit, not the taxon. GO:0005118 and GO:0007601 on Q8K3J9 should be
  removed; the IPR002956 hit on Q8K3J9 is a false-positive family assignment
  (the human ortholog does not get it).

## Experimental biology (mostly mouse)

- HSC dormancy: GPRC5C marks dormant human HSCs; loss/gain of function; hyaluronic
  acid acts through GPRC5C
  [PMID:35725769 "we show that hyaluronic acid, a bone marrow extracellular matrix component, preserves dormancy through GPRC5C"].
  Gprc5c-KO HSCs divide faster
  [PMID:35725769 "In vitro single-cell cultivation of HSCs confirmed that Gprc5c KO had an accelerated division rate compared with wild-type (WT) control"];
  HA/NAG effects on HSCs need Gprc5c
  [PMID:35725769 "However, in vitro HA and NAG treatment of Gprc5c-KO HSCs did not affect quiescence, in vitro self-renewal capacity or in vivo self-renewal capacity compared with WT HSCs"].
  HA and NAG raise Ca2+ in GPRC5C-overexpressing cells
  [PMID:35725769 "Addition of HA and NAG induced an increase in intracellular calcium levels, indicating that both activate GPRC5C signalling"].
  Ligand evidence is docking + Ca2+ + PLA proximity, not direct binding.
  Earlier: a Gprc5c-controlled reporter mouse was used to track dormant HSCs
  [PMID:28479188 "a Gprc5c-controlled reporter mouse was established"].
- AML: Gprc5c drives NF-kB/BCAA metabolism in leukemia
  [PMID:37639313 "Ectopic Gprc5c expression increased AML aggression through the activation of NF-κB"].
- Vascular smooth muscle: GPRC5C dimerizes with AT1 and facilitates Ang II binding
  and signaling; SMC-specific KO mice have reduced Ang II hypertension
  [PMID:38597112 "GPRC5C and the Ang II receptor AT1 dimerize, and knockdown of GPRC5C resulted in reduced binding of Ang II to AT1 receptors"].
  GPRC5C, like GPRC5B, also dimerizes with EP2 and IP
  [PMID:42544579 "The related receptor GPRC5C can also dimerize with prostanoid receptors IP and EP2, and, in addition, it interacts with the Angiotensin II (AngII) receptor AT1, resulting in a facilitation of ligand binding and AT1-dependent signaling (15)."].
- Olfactory cilia: GPRC5C at the ciliary transition zone of olfactory sensory neurons
  [PMID:38110903 "In closer examination, GPRC5C was found in the ciliary transition zone."];
  KO alters cilia composition.
- Kidney: apical membrane of proximal tubule; KO alters acid-base balance;
  alkaline pH triggers internalization; increases NHE3 activity
  [PMID:29196502 "Gprc5c localized to the apical membrane of renal proximal tubules (PTs) in mice, rats, and humans."].
- Pancreatic islets: knockdown lowers GSIS and cAMP
  [PMID:28228611 "Down-regulation of Gprc5c led to both moderately reduced glucose-stimulated insulin release and also reduced cAMP content in mouse islets."] (abstract only).
- Saccharide 'off' response in heterologous cells
  [PMID:37418589 "Our findings suggest that GPRC5C has receptor properties which lead to novel 'off' responses to saccharide detachment"] (abstract only).
- Osteoblasts: knockdown reduces BMP2/GSK126-induced mineralization
  [PMID:37558192 "Loss of function analyses revealed that shRNA-mediated depletion of GPRC5C decreases expression of bone markers (e.g., BGLAP and IBSP) and mineral deposition in response to BMP2 or GSK126."].
- Gprc5c-deficient mice are viable with no behavioral phenotype
  [PMID:21840300 "GPRC5C-deficient mice have no apparent behavioral deficits"].

## Other annotations

- Mitochondrion HDA (PMID:14651853, Mootha 2003 proteome, abstract only): no
  supporting biology; Gprc5c is a plasma-membrane/cilium GPCR. Likely contaminant.
- Signaling receptor complex (ISO/IBA from human GPRC5C IDA, PMID:23382219 PX-FERM
  cargo screen): the cached text does not show GPRC5C data. GPCR heterodimers with
  AT1/EP2/IP would independently fit "signaling receptor complex".
- Protein kinase activator activity (IBA, donor GPRC5B Q9NZH0): GPRC5B activates Fyn;
  no GPRC5C data.
- Centriolar satellite (ISO from human Q9NQ84): the human annotation no longer
  appears in QuickGO (2026-10-19); source not traceable.
