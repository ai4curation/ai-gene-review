# CD5 (human, P06127) curation notes

## Deep research status

- 2026-10-05: `just deep-research-falcon human CD5` failed. The Edison API returned
  repeated `429 Too Many Requests` errors and the recipe exited with "All providers failed".
  No perplexity key is available, so no fallback was run. The review below is based on the
  UniProt record and on primary literature found via PubMed and cached in `publications/`.
- UPDATE 2026-10-05: the failure statement above is superseded. The falcon job completed
  late (end_time 01:31) and `CD5-deep-research-falcon.md` now exists; it has been reconciled
  with the review (see "Falcon deep research reconciliation" below).

## Protein

- Single-pass type I transmembrane glycoprotein, 495 aa. Signal peptide 1-24, extracellular
  25-372 with three group B scavenger receptor cysteine-rich (SRCR) domains, TM 373-402,
  cytoplasmic tail 403-495 [file:human/CD5/CD5-uniprot.txt].
- Structures exist for SRCR domain 1 (NMR, PMID:18339402) and domain 3 (X-ray, PMID:17322294).
- Expressed on all T cells and on B1a B cells [file:human/CD5/CD5-uniprot.txt "Lymphoid-specific receptor expressed by all T-cells and in a subset of B-cells known as B1a cells."].

## Core biology: an inhibitory coreceptor of antigen-receptor signalling

- Mouse knockout: thymocytes become hyperresponsive to TCR stimulation and thymic selection is
  altered [PMID:7542801 "These observations indicate that CD5 can influence the fate of developing thymocytes by acting as a negative regulator of TCR-mediated signal transduction."].
- CD5 surface level scales with TCR signal strength and the cytoplasmic tail is needed for
  inhibition [PMID:11313384 "Substitution of endogenous CD5 with a transgene encoding a truncated form of the protein failed to rescue the CD5(-/-) phenotype, demonstrating that the cytoplasmic domain of CD5 is required for its inhibitory function."];
  [PMID:9858516 "CD5 surface expression on mature SP thymocytes and T cells was found to directly parallel the avidity or signaling intensity of the positively selecting TCR-MHC-ligand interaction."].
- Physical association with TCR/CD3-zeta, LCK and FYN in human T cells; CD5 is an early tyrosine
  kinase substrate [PMID:1384049 "CD5 was found to act as a tyrosine kinase substrate induced by TCR/CD3 ligation"];
  [PMID:1385158 "between 10%-20% of cell surface CD5 was associated with the TcR/CD3 complex"].
- Mechanism: phospho-CD5 docks c-CBL, CIN85, CRKL, PI3K, UBASH3A, SHIP1
  [PMID:32434911 "TCR engagement induces the selective phosphorylation of CD5 tyrosine 429, which serves as a docking site for proteins with adaptor functions (c-Cbl, CIN85, CRKL)"];
  c-CBL-mediated VAV degradation needs the CD5 C-terminus [PMID:23376399 "The carboxy-terminal region of CD5 was also required for Vav degradation"].
- B-1 B cells: CD5 negatively regulates BCR growth signalling, in part via SHP-1
  [PMID:8943203 "Thus the B cell receptor-mediated signaling is negatively regulated by CD5 in normal B-1 cells."];
  [PMID:10540344 "These data support a model whereby CD5 negatively regulates antigen receptor-mediated growth signals by recruiting SHP-1 into the BCR complex in B-1 cells."].
- Human B cells: CD5 expression drives ERK1/2 activation and IL-10 production via TRPC1,
  independent of BCR engagement [PMID:27499044].

## Ligands (contested)

- CD72 proposed as ligand [PMID:1711157 "Here we report that CD5 specifically interacts with the cell-surface protein CD72 exclusive to B cells."].
- Later work found CD5-Ig did not bind CD72 transfectants and identified a distinct B-cell ligand
  [PMID:9723705 "Also, CD5-Ig did not bind to CD72+-transfected cells."]. The CD72 interaction is
  therefore disputed. (Note: the "CD5L" ligand in that paper is a B-cell surface protein, not the
  secreted CD5L/AIM gene product.)
- The CD5 ectodomain binds fungal (1->3)-beta-D-glucan with nM affinity
  [PMID:19141631 "The K(d) of the rshCD5/(1-->3)-beta-d-glucan phosphate interaction is 3.7 +/- 0.2 nM"].

## Annotation decisions (summary)

- Plasma membrane / external side / membrane: accept.
- protein binding (CD72, IPI): remove as uninformative (interaction disputed anyway).
- cell recognition (NAS): over-annotation inferred from the ligand claim.
- signaling receptor activity (NAS): accept as broad MF; CD5 is a receptor/coreceptor.
- negative regulation of BCR signalling (IDA, PMID:1711157): biology is well supported
  (PMID:8943203, PMID:10540344); the cited abstract does not show it, but the curator
  read the full text; accept.
- T cell costimulation (IBA): historically CD5 antibodies costimulate, but genetic data point to
  an inhibitory role; keep as non-core.
- NEW: negative regulation of T cell receptor signalling pathway (GO:0050860), ISS from mouse.
  Participation test: CD5 itself recruits the inhibitory effectors (SHP-1, c-CBL, UBASH3A, SHIP1) through
  its phosphorylated cytoplasmic tail, so it does part of the work. Mouse Cd5 in QuickGO has no
  GO:0050860 annotation despite the knockout data, which looks like a curation gap rather than
  a convention, because the parallel BCR term is annotated.

## Falcon deep research reconciliation (2026-10-05)

- `CD5-deep-research-falcon.md` completed after the review was written. It agrees with the
  review: CD5 is a non-catalytic, TCR/BCR-associated inhibitory signalling scaffold at the
  plasma membrane/immunological synapse; CD72 as ligand is unresolved; the ectodomain binds
  fungal (1->3)-beta-glucan (Kd 3.7 nM, PMID:19141631); the CD5-TRPC1-ERK-IL-10 pathway in
  B cells (PMID:27499044). It also stresses that SHP-1 dependence is disputed, consistent with
  the review restricting SHP-1 to B-1 cells. No contradictions found.
- Material addition verified and acted on: human CRISPR CD5 knockout in CAR/TCR-engineered
  T cells enhances activation and effector function [PMID:39028827 "In this study, we found
  that CD5 inhibits CAR T cell activation and that knockout (KO) of CD5 using CRISPR-Cas9
  enhances the antitumor effect of CAR T cells"]. Added as reference and as supporting
  evidence for the NEW GO:0050860 (negative regulation of TCR signalling) annotation; action
  unchanged.
- Not acted on: clinical/translational items (anti-CD5 CAR-T trials, lymphoma prevalence,
  CD5-derived antifungal peptides, BTLA regulating CD5 levels in mouse) - no GO impact.
- Deep-research file added to references. Status set to COMPLETE.
