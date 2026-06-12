# SEC62 (Q99442) review notes

## Identity / overview
SEC62 (TLOC1, translocation protein 1) is a multi-pass ER membrane protein and an auxiliary component of
the Sec61 translocon. With SEC63 it forms the SEC62-SEC63 complex that supports translocation of precursor
polypeptides into the ER, particularly the post-translational import of small presecretory proteins with
short, weakly hydrophobic signal peptides. SEC62 also serves as a receptor/regulator that positions
precursors into the Sec61 channel and helps trigger channel opening. Independently, SEC62 acts in
recovery-phase ER-phagy (reticulophagy) via an LC3/GABARAP-interacting region.

- UniProt FUNCTION: "Mediates post-translational transport of precursor polypeptides across endoplasmic
  reticulum (ER). Proposed to act as a targeting receptor for small presecretory proteins containing short
  and apolar signal peptides. Targets and properly positions newly synthesized presecretory proteins into
  the SEC61 channel-forming translocon complex, triggering channel opening for polypeptide translocation
  to the ER lumen" [file:human/SEC62/SEC62-uniprot.txt].
- SUBUNIT: "The ER translocon complex that consists of channel-forming core components SEC61A1, SEC61B and
  SEC61G and different auxiliary components such as SEC62 and SEC63. Interacts with SEC61B"
  [file:human/SEC62/SEC62-uniprot.txt].
- SUBCELLULAR LOCATION: "Endoplasmic reticulum membrane ... Multi-pass membrane protein"
  [file:human/SEC62/SEC62-uniprot.txt]. Topology: cytoplasmic 1-196, TM 197-217, lumenal 218-234, TM
  235-255, cytoplasmic 256-399 (two TM helices).
- INTERACTION: SEC62-GABARAP (O95166) [file:human/SEC62/SEC62-uniprot.txt] — consistent with ER-phagy role.

## Key functional evidence
- Translocation function: PMID:22375059 (Lang et al.) "Different effects of Sec61α, Sec62 and Sec63
  depletion on transport of polypeptides into the endoplasmic reticulum" — FUNCTION evidence.
- Small-precursor import / Sec61 channel gating: PMID:29719251 "Sec62 have all been characterized as
  membrane-targeting components for small presecretory proteins, whereas Sec63 and the lumenal chaperone
  BiP act as auxiliary translocation components" [PMID:29719251].
- ER-phagy (reticulophagy): PMID:31006538 (TEX264 ER-phagy paper; cached abstract is about TEX264, but
  the SEC62 IMP reticulophagy annotation by MGI reflects SEC62's documented recovery-ER-phagy role and its
  GABARAP interaction). Abstract-only cache; defer to curator.
- Original cloning: PMID:9020021 "HTP1 (for human translocation protein 1) ... 36.3% identical ... to
  Drosophila homologue of Sec62p" [PMID:9020021].

## Annotation review decisions
- Core MF: protein transmembrane transporter activity (GO:0008320) as part of translocon-associated
  positioning of precursors; the legacy signaling receptor activity (GO:0038023, TAS, old ProtInc) is a
  mis-framing — SEC62 is a translocon-associated targeting receptor, not a signal-transduction receptor.
  MARK_AS_OVER_ANNOTATED.
- Core BP: post-translational protein targeting to membrane, translocation (GO:0031204) /
  post-translational protein targeting to ER membrane (GO:0006620); cotranslational targeting (GO:0006613,
  TAS) is partially correct but SEC62's hallmark is post-translational small-precursor import — ACCEPT but
  non-primary.
- Core CC: ER membrane (GO:0005789); rough ER (GO:0005791, ISS) and ER (GO:0005783) accepted; generic
  "membrane" (GO:0016020) KEEP_AS_NON_CORE.
- GO:0061709 reticulophagy (IMP): genuine secondary role; KEEP_AS_NON_CORE (not the core translocon
  function).
- protein binding (GO:0005515) IPI rows: high-throughput captures (PMID:33961781, PMID:37219487).
  KEEP_AS_NON_CORE.

## Disease / other
SEC62 is amplified/overexpressed in prostate and lung (and other) cancers (located at 3q26 amplicon);
this is a disease/expression association, not a clean GO biological process.

## Falcon deep-research findings (incorporated 2026-06)
- Substrate-specificity "rules": SEC62/SEC63 clients share signal peptides with longer but
  less hydrophobic H-regions and lower C-region polarity; a slowly gating signal peptide plus
  a downstream positively charged cluster is decisive for SEC62/SEC63 (and BiP) dependence
  [PMID:32133789 "those previously unknown substrates share signal peptides (SP) with comparatively longer but less hydrophobic hydrophobic region of SP and lower carboxy-terminal region of SP (C-region) polarity"].
- 22 novel SEC62/SEC63 substrates identified in intact human cells by unbiased proteomics, in
  addition to ERj3 [PMID:32133789 "we identified 22 novel Sec62/Sec63 substrates under these in vivo-like conditions"].
- Two proposed gating models: the SEC62/SEC63 complex may support Sec61 opening either by direct
  interaction with the cytosolic N-terminus of Sec61alpha or via recruitment of BiP to ER-lumenal
  loop 7 of Sec61alpha [PMID:32133789 "by direct interaction with the cytosolic amino-terminal peptide of Sec61α or via recruitment of BiP and its interaction with the ER-lumenal loop 7 of Sec61α"].
- SEC62 knockdown proteomics altered steady-state levels of ~329 proteins (208 down, 121 up;
  q<0.05), enriched for cleavable signal-peptide and N-glycosylated proteins (Falcon; cf. PMID:32133789).
- Calcium / calmodulin role reaffirmed (already in review via PMID:24304694): SEC62 regulates the
  Sec61 Ca2+ leak via a Ca2+-sensitive interaction; SEC62 depletion >=2-fold increases basal cytosolic
  Ca2+; CaM antagonists (trifluoperazine) phenocopy SEC62 silencing [PMID:24304694, Linxweiler 2013 BMC Cancer, doi:10.1186/1471-2407-13-574].
- recovER-phagy reaffirmed (already in review via GO:0061709): SEC62 acts as an ER-phagy receptor
  during recovery from ER stress, distinct from starvation-induced ER-phagy (Falcon review framing).
- Pan-cancer context (3q26 amplicon): SEC62 alterations (mostly amplifications) reported in 2,595 of
  >72,000 cancer patients; SEC62-altered median survival 54.2 vs 95.6 months unaltered
  [Sicking et al. 2021 Cells, doi:10.3390/cells10051036 — not added as ref (disease/expression context)].
- Zimmermann 2025 review frames SEC62 as a substrate-selective Sec61 translocon effector
  [PMID:41009394, doi:10.3390/ijms26188823] — added as reference.
- No new mechanistic structural finding for SEC62 itself beyond the substrate-specificity work;
  Falcon's 2023-2024 "novelty" for SEC62 is mainly conceptual integration into ER-phagy/Ca2+ frameworks.
