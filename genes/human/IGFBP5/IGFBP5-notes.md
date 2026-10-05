# IGFBP5 (human, P24593) curation notes

## Identity

- Insulin-like growth factor-binding protein 5, 272 aa precursor with signal peptide; secreted.
  N-terminal IGFBP domain carries the single high-affinity IGF-binding site; C-terminal
  thyroglobulin type-1 domain; central linker carries C1s/PAPP-A cleavage sites.
- [PMID:9822601 "We show that the entire IGFBP-5 protein contains only one high-affinity binding site for IGFs, located in mini-IGFBP-5."]
- [PMID:10766744 "residues 68, 69, 70, 73, and 74 in IGFBP-5 appear to be critical for high affinity binding to IGF-I"]

## Core activity: IGF binding, sequestration and delivery

- Binds IGF-I and IGF-II with nanomolar affinity and competes with IGF1R:
  [PMID:9822601 "IGFBP-5 inhibits the binding of IGFs to the IGF-I receptor, resulting in reduction of receptor stimulation and autophosphorylation"]
- IGF-binding-deficient mutant is a weak inhibitor of IGF-I-stimulated migration/DNA synthesis
  (porcine aortic SMC): [PMID:10766744 "the ability of IGFBP-5 to inhibit IGF-I-stimulated receptor phosphorylation was attenuated"]
- Forms ~130 kDa ternary complex with IGF and ALS (IGFALS), like IGFBP3:
  [PMID:9497324 "human IGFBP-5, when occupied by IGF-I or IGF-II, forms ternary complexes of approximately 130 kDa with the acid-labile subunit"]
- mTORC1 feedback: secreted IGFBP5 is an mTORC1/HIF1 downstream effector that blocks IGF-1 signalling
  [PMID:26854565 "identified IGFBP5 as a secreted, mTORC1 downstream effector protein"].
- Review: [PMID:32194505 "IGFBP-5 can exert a range of biological actions including prolonging the half-life of IGFs in the circulation, inhibition of IGF signaling by competing with the IGF-1 receptor for ligand binding, concentrating IGFs in certain cells and tissues, and potentiation of IGF signaling by delivery of IGFs to the IGF-1 receptor."]
- Proteolysis by C1s (OA joint fluid), PAPP-A/PAPP-A2 releases IGF
  [PMID:18930415 "C1s is the protease that accounts for this activity"]; Reactome R-HSA-381537.

## ECM association

- [PMID:7683690 "IGFBP-5 was found to bind to types III and IV collagen, laminin, and fibronectin."]
- ECM-bound IGFBP-5 is protected from degradation and potentiates IGF-I:
  [PMID:7683690 "IGFBP-5 is present in fibroblast ECM, where it is protected from degradation and can potentiate the biologic actions of IGF-I"]
- Profibrotic, IGF-independent ECM induction; ECM IGFBP-5 protects fibronectin
  [PMID:20345844 "IGFBP-5 in the ECM protects fibronectin from proteolytic degradation"];
  [PMID:26103640 "nuclear translocation is not necessary for IGFBP-5 fibrotic activity; neither is IGF binding"].
- MatrisomeDB lists IGFBPs among core-matrisome ECM glycoproteins (PMID:36399478, database).

## Intracellular/nuclear pool (non-core)

- Internalised via caveolin-1/lipid rafts; nuclear import requires NLS and nucleolin
  [PMID:20345844 "In primary fibroblasts, IGFBP-5 bound Cav-1 and both proteins translocated to the nucleus in IGFBP-5-expressing fibroblasts."];
  [PMID:26103640 "IGFBP-5 transport to the nucleus requires an intact NLS and nucleolin."]
- Function of the nuclear pool is unclear (not needed for fibrotic activity).

## IGF-independent ligand activity

- ROR1 ligand in glioblastoma stem-like cells, promoting ROR1/HER2 heterodimerisation and CREB signalling
  [PMID:36949068 "IGFBP5 binds to ROR1 and facilitates ROR1/HER2 heterodimer formation"]. Single study, cancer context.
- Thrombospondin-1 binding modulates TS-1/IAP (CD47)/SHPS-1 crosstalk in SMC
  [PMID:15700281 "IGFBP-5 inhibits the binding of TS-1 to IAP"]. No GO term for thrombospondin binding.

## In vivo genetics

- Igfbp5 KO: no apparent phenotype; triple Igfbp3/4/5 KO growth-reduced
  [PMID:16675541 "New lines of knockout (KO) mice lacking either IGFBP-3, -4, or -5 had no apparent deficiencies in growth or metabolism"].
- Ubiquitous overexpression: neonatal mortality, reduced fertility, growth inhibition, retarded muscle development
  [PMID:15010534 "Significantly increased neonatal mortality, reduced female fertility, whole-body growth inhibition, and retarded muscle development were observed in Igfbp5-overexpressing mice."]
  These mouse IMP rows are the source of several human IEA rows (female pregnancy, lung alveolus
  development, negative regulation of muscle tissue development/skeletal muscle hypertrophy) —
  gain-of-function phenotypes, treated as over-annotation.
- Overexpression reduces BMD [PMID:15550514]; IGF-binding-deficient mutant still inhibits growth [PMID:19332648].

## Smooth muscle context (conflicting direction)

- Negative regulation of SMC migration/proliferation via IGF sequestration (PMID:10766744, porcine SMC)
  vs positive regulation of VSMC proliferation/migration downstream of miR-137 (PMID:29016699,
  "enforced expression of IGFBP-5 reversed the inhibitory effects of miR-137 on cell proliferation and migration of VSMCs").
  Direction is context-dependent; both kept as non-core.

## Deep research

- `just deep-research-falcon human IGFBP5` was run twice (2026-10-05); both runs failed with
  "Provider falcon timed out after 600s" / "All providers failed" (no perplexity key for fallback).
  No deep-research file exists; the review is based on cached publications (fetched via
  `just fetch-gene-pmids` / `just fetch-pmid`), PubMed searches and the UniProt record.

## Interactome rows

- 71 IPI protein-binding rows from HuRI (PMID:32296183) and 2 from CREB3 variant Y2H screens
  (PMID:25910212, PMID:31515488): partners are mostly membrane proteins (claudins, connexins,
  GPCRs, SLCs, TMEMs) — a secreted protein is unlikely to engage these physiologically; uninformative, REMOVE.
