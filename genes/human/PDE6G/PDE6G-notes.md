# PDE6G notes

Session 2026-11-16, review of 26 GOA rows (vision-disorder alignment campaign), after PDE6A, PDE6B, PDE6C.

## Function

- Inhibitory gamma subunit (Pgamma, 87 aa) of rod PDE6; two copies per PDE6A/PDE6B dimer
  [PMID:7828894, human gene]. Its C-terminus blocks the entrance of each catalytic site and its
  N-terminal region contacts the GAFa domain over the allosteric cGMP site [PMID:33007200, bovine
  native PDE6]. Activated transducin alpha displaces the C-terminus ~60 A (same paper).
- GO term: there is no MF term for inhibiting a cyclic-nucleotide phosphodiesterase (searched
  QuickGO "phosphodiesterase inhibitor": only GO:0051344 negative regulation of cyclic-nucleotide
  phosphodiesterase activity, a BP). So the core MF stays GO:0004857 enzyme inhibitor activity, as
  in modules/visual_phototransduction.yaml.
- Positive role: the human splice mutation c.187+1G>T causes recessive early-onset RP, which the
  authors read as a positive role of gamma in maintaining PDE activity [PMID:20655036]; with PDE6C,
  Pgamma acts as a co-chaperone of AIPL1-dependent folding [PMID:28583373, human PDE6C with mouse Pgamma].
- Transducin GTPase acceleration: Reactome R-HSA-2584246 states that PDE-gamma raises the affinity
  of GNAT1-GTP for the RGS9-GNB5-R9AP GAP complex. The primary evidence is bovine biochemistry and
  mouse physiology; no cached paper shows it for the human protein. Not annotated; recorded as a
  suggested question.
- Non-retinal: endogenous Pgamma in human HEK293 cells is needed for EGF- and thrombin-stimulated
  ERK activation via GRK2 [PMID:11502744]. This is the source (curated to mouse Pde6g/Pde6h as IDA)
  of the IBA rows on EGFR and GPCR signalling; kept as non-core.
- SH3 binding: polyproline motif aa 20-28 binds SH3 domains; PACSIN in rat retina [PMID:16357825].
- Spectrin beta-V associates with phototransduction proteins along the transport route (mouse)
  [PMID:23704327, abstract only].

## Questionable rows

- InterPro2GO (IPR006952 PDE6 gamma family) maps cyclic-nucleotide phosphodiesterase activity and
  cGMP binding to this inhibitory subunit. Pgamma has no catalytic domain and no GAF domain;
  both removed.
- Bare protein binding from HuRI screens: removed as uninformative.
