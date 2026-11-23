# EDN2 curation notes (human endothelin-2, UniProtKB:P20800)

No deep-research provider was available for this review (no provider keys in the
batch environment). The literature search below was done by hand with PubMed
(queries: `endothelin-2[Title] AND (knockout OR deficiency OR ovulation OR
photoreceptor)`; `endothelin-2 axon growth neurons mouse`; QuickGO lookup of mouse
Edn2 P22389 annotations to trace the Ensembl Compara IEA rows). Papers cited here
are cached under `publications/`.

## Gene product

- 178-aa preproendothelin-2: signal peptide 1-24, propeptide 25-46, mature
  Endothelin-2 at 49-69 (21 aa, disulfides 49-63 and 51-59), C-terminal propeptide
  70-178 (UniProt P20800 FT lines). UniProt function line is generic ("Endothelins
  are endothelium-derived vasoconstrictor peptides").
- Mature ET-2 is [Trp6,Leu7]endothelin, differing from ET-1 by two residues
  [PMID:2649896 "(ii) [Trp6,Leu7]endothelin (ET-2)"]. Synthetic ET-2 is a strong
  vasoconstrictor and pressor peptide [PMID:2649896 "All these synthetic peptides
  produced strong vasoconstrictor and pressor responses."].
- PANTHER: PTHR13874 (ENDOTHELIN), subfamily PTHR13874:SF9 (ENDOTHELIN-2); PAINT
  root node PTN000356323 carries hormone activity, endothelin B receptor binding,
  extracellular region and the vascular process terms (module
  `endothelin_receptor_signaling`).

## Receptors and signalling

- ET-2 has the same affinity as ET-1 for both ETA (EDNRA) and ETB (EDNRB), unlike
  ET-3 [PMID:22118774 "it has the same affinity as ET-1 for both ET(A) and ET(B)
  receptors"].
- Human melanocytes: ET-2 binds with Kd equal to ET-1 and raises IP3 and
  intracellular Ca2+ [PMID:1917960 "Upon incubation with cultured cells, the mass
  contents of inositol 1,4,5-trisphosphate and intracellular calcium level were
  substantially increased by 10 nM ET-1, ET-2, and ET-3, but not by big-ET"]. This
  is the PLC-activating branch (GO:0160135), not yet annotated to EDN2 in GOA.
- Human umbilical artery/vein: ET-2 is as potent as ET-1, through ETA in artery and
  ETA+ETB in vein [PMID:8982507 "Endothelin-1 (ET-1) and endothelin-2 (ET-2) are
  potent stimulants of both the human umbilical artery (pEC50 7.9 and 7.5) and vein
  (pEC50 8.1 and 8.0)."]; also [PMID:9422810].
- Human atrium: positive inotropic effect [PMID:1652300 "The data show that
  endothelin-2 has a strong positive inotropic effect on the isolated human
  myocardium."].
- Mouse osteoblast-like MC3T3-E1 cells: ET-2 induces PGHS-2/PGE2 via ETA
  [PMID:9492062].
- Macrophages / THP-1: ET-2 is a chemoattractant via ETB and MAPK
  [PMID:12207323 "Experiments with endothelin receptor antagonists showed that
  migration to ET-2 is mediated via the ET-RB receptor."]. GOA records this as
  `cytokine-mediated signaling pathway`; ET-2 is not a cytokine and the receptor is
  EDNRB, so the review MODIFYs it to endothelin receptor signaling pathway.
- Neutrophils: ET-2 activates migration [PMID:9696419].

## Distinctive physiology (mouse genetics)

- Ovulation: EDN2 is transiently expressed by granulosa cells just before
  ovulation and contracts the follicle wall smooth muscle through EDNRA
  [PMID:16410304 "EDN2 induces follicular rupture by constricting periovulatory
  follicles"]; global and granulosa-specific knockouts impair follicle rupture
  [PMID:24763822; PMID:28400616 "These data demonstrate that EDN2-induced
  intraovarian contraction is a critical trigger of normal ovulation and subsequent
  fecundity."]; oviduct contraction via ETA in rat [PMID:17535876].
- Postnatal survival: Edn2 knockout mice show growth retardation, hypothermia,
  internal starvation and emphysema [PMID:23676500 "ET-2 is critical for the growth
  and survival of postnatal mice and plays important roles in energy homeostasis,
  thermoregulation, and the maintenance of lung morphology and function."].
- Retina: overexpression of Edn2 in mouse retina inhibits angiogenesis and promotes
  the endothelial tip-cell state through EDNRA [PMID:24043815]. This overexpression
  study is the source (via Ensembl Compara from mouse Edn2) of the angiogenesis,
  vasculature development, endothelial cell migration and `cell tip growth` IEA rows.
  `GO:0009932 cell tip growth` ("Growth that occurs specifically at the tip of a
  cell") is a polarised-growth term (hyphae, pollen tubes, root hairs) and does not
  describe endothelial tip-cell specification; REMOVE.
- Mouse IEA rows `neuron projection development` (mouse source PMID:24875861) and
  `axon extension` (mouse source PMID:18401410) come from sympathetic axon-guidance
  papers whose abstracts foreground Edn1 and Edn3; the full texts may test Edn2 in
  explants, which we could not read. Left UNDECIDED.

## Curation decisions summary

- Core MF: `GO:0005179 hormone activity` (child of receptor ligand activity), per
  LIGANDS_IN_SIGNALING section 2 decisions. The receptor-specific binding term
  `GO:0031708 endothelin B receptor binding` (IBA, IPI) is MODIFIED to hormone
  activity following decision 4 (ligands go to receptor ligand activity or a child).
- Core BP: `GO:0086100` endothelin receptor signaling pathway (already in GOA by IDA
  and IEA) plus NEW `GO:0160135` PLC-activating endothelin receptor signaling
  pathway (PMID:1917960), matching the endothelin module.
- Ovulation (GO:0030728) is a strong mouse-genetic role but was not added as NEW:
  the evidence is mouse-only and EDN2 is the trigger of follicle-wall contraction
  rather than a participant in follicle rupture itself; raised as a suggested
  question instead.
- Module check: the EDN2 step in `modules/endothelin_receptor_signaling.yaml`
  (hormone activity; GO:0086100, GO:0160135; extracellular region) is consistent
  with this review; no module edit needed.
