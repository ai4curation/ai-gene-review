# Pld (B7YZT5, Drosophila melanogaster) review notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

This is a full review of the UniProt gene-centric canonical entry B7YZT5 (1364 aa) for FlyBase gene
FBgn0286511 (CG12110). The folder is `Pld__B7YZT5` because `genes/DROME/Pld` is keyed to the
isoform/related entry A4UZ54. No ProtNLM2 output or prediction-evidence file was opened or used.

### Deep research
- `just deep-research-falcon DROME B7YZT5 --alias Pld__B7YZT5 --fallback perplexity-lite` failed.
  Falcon returned 403 "Failed to authenticate" (Edison), and the perplexity-lite fallback returned
  401 insufficient_quota. No deep-research file was written for this folder.
- Instead I read the full text of the primary literature directly:
  PMID:17156430, PMID:15883198, PMID:27848911 and PMID:30369483 (newly cached). I also consulted the
  existing falcon report for the same gene (`genes/DROME/Pld/Pld-deep-research-falcon.md`) to find
  literature. Every claim below was checked against the cached papers.

### Evolutionary grounding
- PANTHER: B7YZT5 is in PTHR18896:SF76; human PLD1 (Q13393) is in SF57 and PLD2 (O14939) in SF121
  (`interpro/panther/PTHR18896/PTHR18896-entries.csv`). These are different subfamilies, so
  PLD1-subfamily-specific functions were not transferred.
- PAINT, read from QuickGO IBA WITH/FROM: PTN004499769 is a deep, pan-PLD node (plants, fungi,
  bacteria, animals) and carries D-type glycerophospholipase activity and phospholipid catabolic
  process. PTN001051940 is the animal PLD1/PLD2 node; fly Pld, PLD1 and PLD2 all descend from it. It
  carries plasma membrane, cytoplasmic vesicle and regulation of vesicle-mediated transport. PAINT did
  not propagate PLD1's many other experimental process terms, and I treat that as deliberate.
- Panda et al. 2018 (PMID:30369483) built an ML phylogeny in which insect PLDs group nearer chordate
  PLD1. In their rescue experiments hPLD1 fully rescued dPLD3.1 retinal degeneration and hPLD2 did so
  only partly.
- Catalytic HKD motifs are intact: UniProt ACT_SITE H701/K703/D708 and H1181/K1183/D1188, which I
  confirmed in the sequence.

### Experimentally established in Drosophila
- PLD activity: transphosphatidylation by expressed Pld, abolished by the H1095N HKD mutation and
  stimulated by ARF1 [PMID:17156430 "Taken together, these findings demonstrate that Pld is a bona fide PLD and can be regulated by ARF GTPases"].
  In vivo, dPLD3.1 flies make no PEth and have less PA [PMID:27848911 "Under these conditions, multiple species of PEth were detected in wild-type flies, no PEth could be detected in dPLD3"].
- Localization: small cytoplasmic vesicles in embryos (endogenous protein). In photoreceptors it sits at
  the base of the rhabdomere microvilli; whether it is on the SMC or the plasma membrane is unresolved
  [PMID:30369483 "Presently it is unclear if dPLD is localized to the membrane of the SMC or to the microvillar plasma membrane in this area"].
- Photoreceptor membrane recycling: depends on catalytic activity and needs Arf1-GTP and retromer
  [PMID:27848911 "suggesting that the ability of dPLD to regulate RLV turnover is dependent on its catalytic activity"].
  This paper is not reflected in GOA. I added NEW GO:2001137 positive regulation of endocytic
  recycling as a regulation term, because Pld supplies PA while Arf1 and retromer do the sorting.
- Embryonic cellularization: Golgi structures are enlarged and Golgi-derived vesicles are not inserted
  into the plasma membrane (PMID:17156430).

### Inferred only (not established for the fly protein)
- Plasma membrane as the site of action. This comes from the IBA plus COS7 overexpression; in
  embryos Pld is explicitly not at the plasma membrane. Kept as non-core.
- Phosphatidylinositol binding comes only from the PX-domain InterPro2GO mapping; no peer-reviewed
  fly lipid-binding data exist. Kept as non-core.
- Intracellular signal transduction is a family-level mapping and was marked over-annotated.

### Decisions on phenotype-derived rows
- Phototransduction (IMP, 2005) was marked over-annotated. Pld is not a cascade component, and the
  later dPLD3.1 study found no primary ERG defect
  [PMID:27848911 "photoreceptors did not exhibit a primary defect in the electrical response to light in electroretinograms"].
- Gastrulation involving germ band extension was marked over-annotated. The authors attribute it to
  defects that begin at cellularization.
- Golgi organization, cellularization and positive regulation of Golgi vesicle fusion were kept as
  non-core. They are embryonic contexts of the trafficking role.

### Validation
- `just validate DROME Pld__B7YZT5` passes; `just validate-references` reports 0 issues.
