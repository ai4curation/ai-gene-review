# Gas7 (mouse, Q60780) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: mouse Gas7 is the experimental seed of the chordate GAS7 PAINT node
PTN001890901 (GO:0048812 neuron projection morphogenesis) and will serve as the
reference for transfer to the fugu PTHR23065:SF57 member A0A674PKV4. No
ProtNLM2 output was consulted.

### Deep research

`just deep-research-falcon mouse Gas7 --fallback perplexity-lite` failed (falcon
and the perplexity-lite fallback both exited non-zero; no deep-research file was
written). The review was built from the cached primary literature below, the
UniProt record and the PANTHER/PAINT files.

### Evolutionary grounding

- PANTHER: PTHR23065:SF57 (GROWTH ARREST-SPECIFIC PROTEIN 7) in the F-BAR family
  PTHR23065 (UniProt DR line). Domain architecture: WW (22-55) + F-BAR (141-401);
  no SH3 in isoform 1, no muHD (the C-terminal mu-homology domain that FCHO1/2 use
  to engage the clathrin/AP2 machinery).
- PAINT nodes behind the IBA rows (interpro/panther/PTHR23065/PTHR23065-paint.tsv):
  - PTN001890901 (taxon:7711 Chordata): GO:0048812 only, seeded by MGI:1202388
    (this gene). The curator propagated neuron projection morphogenesis but none
    of Gas7's actin terms (actin filament binding, polymerization, bundling,
    ruffle); treat that omission as deliberate.
  - PTN002747256 (taxon:2759 Eukaryota): cytoplasm, plasma membrane, seeded broadly
    across F-BAR proteins (PSTPIP, FCHO, Cdc15/Imp2 etc.). Reasonable for GAS7.
  - PTN000552124 (taxon:33213 Bilateria): clathrin-coated pit, clathrin-coated
    vesicle, clathrin coat assembly, clathrin-dependent endocytosis; seeds are
    FCHO1 (O14526), FCHO2 (Q0JRZ9, MGI:3505790) and a worm gene. No GAS7 evidence
    for any clathrin role; GAS7 lacks the muHD on which FCHO function depends and
    its F-BAR forms flat sheets rather than the curved lattice of pits. Marked as
    over-annotation.

### Experimental findings in mouse protein / mouse cells

- Neurite outgrowth: antisense knockdown in embryonic mouse cerebellar cultures
  reduces neurite formation by Purkinje cells; overexpression in Neuro-2a promotes
  neurite-like outgrowth [PMID:9736752 "Interference with GAS7 production in cultured embryonic cerebellar cells by gas7 -specific antisense oligonucleotides inhibits the neurite formation normally observed during development of these neurons."].
- Actin: Gas7 binds F-actin directly (C-terminal region), promotes actin assembly and
  cross-links filaments; localizes with microfilaments in ruffles of NIH3T3
  [PMID:11795944 "direct binding of purified His-Gas7 to actin also was demonstrated and shown to be mediated by the Gas7 C-terminal domain"]. Abstract only.
- N-WASP/Arp2/3: Gas7 WW domain binds N-WASP proline-rich region; Gas7 stimulates
  N-WASP/Arp2/3 actin polymerization in pyrene assays; co-localizes with N-WASP in
  growth-cone filopodia of mouse hippocampal neurons; interaction required for
  neurite outgrowth [PMID:20150425 "The in vitro actin polymerization assay showed clearly that Gas7 induces actin polymerization, and therefore, the subsequent extension of membrane protrusions through an N-WASP-Arp2/3-mediated pathway."].
- Phagocytosis: endogenous GAS7b in mouse RAW264.7 macrophages localizes to
  phagocytic cups with actin; knockout reduces zymosan and IgG-bead uptake and
  lamellipodia; rescue requires the membrane-binding loops, oligomerisation and
  WW domain. Crystal structure of the mouse F-BAR (PDB 6IKN/6IKO) shows a flat
  sheet-forming assembly; binds PS-containing liposomes [PMID:31628328 "the two-dimensional sheet-like assembly of Growth Arrest-Specific 7 (GAS7) plays a critical role in phagocytic cup formation in macrophages"].
- PC12 differentiation: overexpression potentiates NGF-induced differentiation of rat
  PC12 cells; not neuroprotective [PMID:15725398]. Abstract only; acts-upstream
  phenotype, kept as non-core.

### Decisions summary

- Core: F-BAR membrane-sheet scaffold at the cytoplasmic face of plasma membrane
  (phagocytic cups, ruffles, growth cones) coupling membrane to actin, via direct
  F-actin binding/bundling and WW-domain recruitment of N-WASP -> Arp2/3.
- Processes accepted: neuron projection morphogenesis (IMP + IBA), actin filament
  polymerization, actin filament bundle assembly. NEW: phagocytosis (GAS7 itself
  forms the cup scaffold; participation, not just necessity), positive regulation of
  Arp2/3 complex-mediated actin nucleation (in vitro activation of N-WASP/Arp2/3).
- NEW locations: phagocytic cup, growth cone. NEW MF: phospholipid binding
  (liposome co-sedimentation; PS-rich liposomes).
- Clathrin IBA set: MARK_AS_OVER_ANNOTATED (FCHO-specific node function).
- Transfer caution for fugu A0A674PKV4: what is experimentally established is in
  mouse; neuron projection morphogenesis is PAINT-propagated across chordate GAS7.
  Phagocytosis and actin activities are not PAINT-propagated and are mouse
  experimental only.
