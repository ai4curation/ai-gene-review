# CSF1 review notes

## Literature synthesis

CSF1 / macrophage colony-stimulating factor is a disulfide-linked helical cytokine
that binds CSF1R/FMS and activates a class III receptor tyrosine kinase signaling
complex. Structural work on the full human extracellular assembly showed that
"dimeric hCSF-1 binds bivalently to two hCSF-1RD1-D5 receptor molecules" and
identified receptor homotypic contacts away from the ligand-binding epitope
[PMID:22153499].

The human CSF1 locus encodes alternatively processed products. Expression of the
human cDNAs in COS-7 cells produced "biologically active M-CSF" and supernatants
stimulated murine marrow proliferation and human monocytic colony formation
[PMID:2460758]. Processing studies support both secreted and membrane-associated
forms: the 1.6 kb precursor was a "membrane-bound glycoprotein at the cell
surface", while the 4 kb precursor was efficiently cleaved and secreted
[PMID:3264877], and a high-molecular-weight human M-CSF species was shown to be
a proteoglycan form [PMID:1531650].

At the cellular-process level, CSF1 is the conserved ligand for mononuclear
phagocyte survival, proliferation, and differentiation. PAINT places cytokine
activity and extracellular localization on PTN002559881, and osteoclast and
macrophage differentiation on PTN001296023. Human and mouse osteoclast-culture
papers use M-CSF together with RANKL to drive osteoclastogenesis; in patients
with TNFRSF11A/RANK mutations, "monocytes failed to differentiate in vitro into
osteoclasts upon exposure to M-CSF and RANKL" [PMID:18606301].

Several GOA rows reflect contextual macrophage phenotypes rather than separate
core functions. M-CSF can induce foam-cell formation in alveolar macrophages
[PMID:18566389] and can drive epithelial-cell-conditioned macrophage migration
in a Salmonella / miR-128 model [PMID:24415783]. Atherosclerotic-vessel
expression and perinuclear-localization rows from PMID:1739124 are based on an
abstract-only cache, so the exact localization and protein-metabolism claims
remain unresolved. The STAP-1 microglia paper [PMID:19100238] studies a
downstream CSF1R adaptor; it should not make CSF1 a positive regulator of its
own M-CSF pathway.

## Source checks

- `PMID:10652277` is a STAT5 paper focused on GM-CSF-dependent maturation in
  chicken and mouse hematopoietic cells, but its mouse cultures used recombinant
  human M-CSF as a dedicated factor arm. The two MGI rows are therefore kept
  without a source-defect query.
- `Reactome:R-HSA-8937656` is an IL10 inflammatory-mediator event. It does not
  support CSF1 plasma-membrane localization, although CSF1 itself is a bona fide
  plasma-membrane protein.
- The IntAct `GO:0005515` rows are either CSF1R/BARF1 binding rows with better
  specific interpretations or large-screen Y2H / cell-surface interactome rows.
  They are all bare protein-binding rows under the repository policy.
