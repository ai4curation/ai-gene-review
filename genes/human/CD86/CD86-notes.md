# CD86 (B7-2) curation notes

## Deep research status

- 2026-10-05: `just deep-research-falcon human CD86` was launched in the background.
  The Edison/Falcon API returned repeated `429 Too Many Requests` errors during the
  session (shared rate limit with concurrent jobs). No perplexity key is available, so
  no fallback was used. The review below was built from UniProt P42081, the cached
  GOA-cited publications (`publications/PMID_*.md`, mostly abstract-only) and cached
  Reactome entries. If a `CD86-deep-research-falcon.md` file appears later, it was
  not used for this review. Final outcome: the falcon job exited without producing
  an output file (Edison API 429 rate limiting); no deep-research file exists.
- UPDATE 2026-10-05: the statement above is superseded. The falcon job did complete
  late (end_time 01:34) and `CD86-deep-research-falcon.md` now exists; it has been
  reconciled with the review (see "Falcon deep research reconciliation" below).

## Identity

- UniProt P42081 (CD86_HUMAN), "T-lymphocyte activation antigen CD86", alt names
  B7-2, B70, CTLA-4 counter-receptor B7.2; 329 aa type I transmembrane protein of the
  immunoglobulin superfamily (IgV + IgC extracellular domains, short cytoplasmic tail).
- Six splice isoforms, including a soluble deltaTM form and deltaEC form; isoform 2
  reported to interfere with CD86 clustering [file:human/CD86/CD86-uniprot.txt
  "[Isoform 2]: Interferes with the formation of CD86 clusters, and thus acts as a
  negative regulator of T-cell activation."].

## Core molecular function: ligand for CD28 and CTLA4

- Cloned as a second CD28/CTLA4 counter-receptor that costimulates T cells
  [PMID:7694363 "We have cloned a counter-receptor of CD28 and CTLA-4, termed B7-2."];
  [PMID:7694363 "B7-2 also costimulates IL-2 production and T cell proliferation"].
- ETC-1 (identical to B7-2) bound CD28-Ig and CTLA4-Ig and enhanced CD4 T cell
  proliferation [PMID:7513726 "ETC-1 also bound to both CD28-Ig and CTLA4-Ig fusion
  proteins"].
- CD80 and CD86 transfectants costimulate proliferation, IL-2 and IFN-gamma, and CTL
  generation similarly [PMID:7527824 "both CD80 and CD86 transfectants efficiently
  costimulated anti-CD3 mAb-induced proliferation and the secretion of IL-2 and
  IFN-gamma"].
- Biophysics: B7-2 binds both receptors more weakly than B7-1, is monomeric, and is less
  biased toward CTLA4 [PMID:12196291 "B7-2 binds the two receptors more weakly than
  B7-1"]; [PMID:12196291 "unlike B7-1, B7-2 does not self-associate"].
- Crystal structure of CTLA4/B7-2 complex: alternating lattice of bivalent CTLA4 and
  B7-2 dimers proposed as synapse organisation [PMID:11279501 "the 3.2-A resolution
  structure of the complex between the disulphide-linked homodimer of human CTLA-4 and
  the receptor-binding domain of human B7-2"].
- IgC and intracellular domains needed for full co-signaling; CD86 monomeric in living
  cells [PMID:24845157 "We report for the first time the presence of CD80 dimers and
  CD86 monomers in living cells."].
- Signalling differences vs CD80: CD86 does not induce detectable CD28 tyrosine
  phosphorylation but shares CBL/VAV phosphorylation and NFAT activation
  [PMID:9915850 "ligation with CHO-CD86 was unable to induce detectable CD28 tyrosyl
  phosphorylation over a range of stimulation conditions"].
- CTLA4 acts as a decoy/competitive inhibitor for CD86 [Reactome:R-HSA-388808 "CTLA4
  primarily affects CD28 costimulation by acting as a competitive inhibitor."].

## Location

- Plasma membrane, single-pass type I; APC surface (B cells, monocytes, DCs)
  [file:human/CD86/CD86-uniprot.txt "Expressed on the surfaces of antigen-presenting
  cells."]. Also found in exosome proteomes (B-cell exosomes, plasma vesicles) – likely
  passive cargo from APC membranes.
- Regulated by MARCH8 (c-MIR) ubiquitination -> endocytosis/lysosomal degradation
  (UniProt PTM).

## Reverse signalling (mouse, ISS)

- UniProt (By similarity to mouse P42082): CD86 engagement on B cells regulates IgG1
  production and activates NF-kappa-B via PLC/PKC. These ISS-based annotations
  (B cell activation, Ig production, non-canonical NF-kB) are plausible but not core;
  kept as non-core.

## Microbial

- Receptor for adenovirus species B fiber (PMID:16920215, per UniProt); vaccinia M2
  binds CD80/CD86 (PMID:30918073). Not annotated in GOA; not added.

## Curation decisions summary

- Core MF: receptor ligand activity (GO:0048018) — CD28/CTLA4 ligand.
- Core BP: T cell costimulation (GO:0031295), via MODIFY of the T cell activation IDA
  (GO:0042110 is the wrong parent; GO:0031295 is_a positive regulation of T cell
  activation and its definition is literally the provision of a surface-bound
  ligand-receptor second signal). Comparator check: CD80 already carries GO:0031295.
- protein binding IPI rows with CTLA4/CD28 -> MODIFY to signaling receptor binding.
- coreceptor activity / signaling receptor activity -> MODIFY to receptor ligand
  activity (CD86 is the ligand; CD28 is the (co)receptor).

## Falcon deep research reconciliation (2026-10-05)

- `CD86-deep-research-falcon.md` completed after the review was written. It agrees with
  the review's core picture (CD86 = APC-surface ligand for CD28 and CTLA4, not an enzyme;
  signalling is downstream of CD28 in the T cell) and found no contradictions.
- Material additions verified against primary literature and acted on:
  - MARCH1 (not only MARCH8/c-MIR, which UniProt cites) ubiquitinates CD86 via a
    TMD recognition surface centred on Pro254 [PMID:34157285 "We identified a highly
    specific recognition surface in the hydrophobic core of the CD86 transmembrane (TM)
    domain (TMD) that is required for recognition by MARCH1"]. Description updated to
    "MARCH-family E3 ligase (MARCH1 in APCs, also MARCH8)"; reference added.
  - CTLA4-mediated transendocytosis of CD86, with CTLA4 recycling after CD86 release
    [PMID:35999394 "in the presence of CD86, CTLA-4 detached in a pH-dependent manner and
    recycled back to the cell surface to permit further transendocytosis"]. Reference
    added; this is a CTLA4 process (CD86 is its input), so no new CD86 annotation.
- Not acted on: soluble CD86 splice variant costimulation (Jeannin 2000; no PMID
  resolved, already covered by an existing suggested question), 2023-2024 mouse/
  translational studies (context-specific, no GO impact), mouse B-cell reverse
  signalling (already kept as non-core ISS).
- Deep-research file added to references and cited as support on the IBA receptor
  ligand activity annotation. No annotation actions changed.
