# PIEZO1 curation notes

## 2026-11-27

Deep research via Falcon with the Perplexity Lite fallback was attempted but both
providers were unavailable in this checkout, so the review was assembled manually from
GOA, UniProt and primary cached papers.

PIEZO1 is a direct mechanotransduction channel, and its support is much stronger than
the edge cases that motivated the Mechanobiology evidence guide. The assay chain is:

- Coste et al. 2010 identified mouse Piezo1/Fam38A by an siRNA screen for mechanically
  activated currents in Neuro2A cells, verified stretch-activated current loss after
  Piezo1 knockdown, and showed that heterologous mouse Piezo1 or Piezo2 expression
  induces large mechanically activated cation currents [PMID:20813920 "Expression
  profiling and RNA interference knockdown of candidate genes identified Piezo1
  (Fam38A) to be required for MA currents in these cells"].
- Coste et al. 2012 showed that Drosophila Piezo and mouse Piezo1 have different
  pore properties, that purified mouse Piezo1 did not carry another detectable
  channel-like protein, and that purified mouse Piezo1 forms ruthenium-red-sensitive
  channels after reconstitution in asymmetric bilayers and liposomes [PMID:22343900
  "Purified MmPiezo1 reconstituted into asymmetric lipid bilayers and liposomes forms
  ruthenium-red-sensitive ion channels"].
- Gnanasambandam et al. 2015 recorded human PIEZO1 single-channel currents in
  HEK293 cells and directly measured permeation by K+, Na+, Li+, Ca2+, Ba2+ and Mg2+
  [PMID:25955826 "All monovalent ions permeated the channel"].
- Syeda et al. 2016 purified trimeric mouse Piezo1-FLAG, reconstituted it into
  droplet lipid bilayers, and activated it by osmotic-gradient and solvent-injection
  bilayer perturbations with no other cellular component [PMID:27829145 "mechanical
  perturbations of the lipid bilayer alone are sufficient to activate Piezo channels"].
- Li et al. 2014 showed PIEZO1-dependent shear-stress Ca2+ entry and current in human
  and mouse endothelial cells, plus sufficiency of human PIEZO1 for a shear response
  in HEK293 cells [PMID:25119035 "These cells had little or no shear stress response
  unless exogenous wild-type (WT) human Piezo1 was expressed"].

The existing annotations mostly needed granularity fixes rather than removals. Generic
GO:0005261 monoatomic cation channel activity, GO:0008381 mechanosensitive monoatomic
ion channel activity, GO:0006812 monoatomic cation transport and GO:0034220 monoatomic
ion transmembrane transport were refined to mechanosensitive cation-channel or cation
transmembrane-transport descendants where the same evidence supported that refinement.
The old GO:0008381 InterPro2GO mapping is biologically correct for Piezo as a family,
but should now point at GO:0140135.

The GO ion-channel convention from issue #7187 matters for PIEZO1, but the best
fit for human Ca2+ permeation is the stretch-activated Ca2+ child. PMID:25955826
measured inward Ca2+ currents through mechanically stimulated human PIEZO1 single
channels, supporting GO:0015275 as a conservative NEW row.

The ER, ER-membrane, ERGIC-membrane, lamellipodium, stereocilium and cuticular-plate
locations are not used in core functions. The ER/ERGIC rows come from early Fam38A/Mib
localization; the lamellipodium row is a regulated endothelial sublocation under shear;
and the mouse stereocilium/cuticular-plate transfer is a specialized inner-ear
localization rather than a demonstrated human core location.
