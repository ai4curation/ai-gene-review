# SBP1 review notes

## Identity correction

The canonical *S. cerevisiae* gene symbol for UniProt P10080 / YHL034C is **SBP1**.
Older literature used **SSB1** or **SSB-1** for this single-stranded RNA-binding
protein. That historical synonym caused this review to be stored under `SSB1`,
colliding with the unrelated ribosome-associated Hsp70 gene **SSB1** (P11484).
This review and its source files were therefore moved to the canonical `SBP1`
path; fetched and provider-generated content was retained unchanged.

## Evidence re-audit

- The historical nucleolar annotations remain credible but non-core. The original
  study reports that SSB-1/Sbp1 colocalized with fibrillarin in the yeast nucleolus
  and co-immunoprecipitated snR10 and snR11 [PMID:2121740, "SSB-1 colocalized with
  fibrillarin in a double-label immunofluorescence mapping experiment to the yeast
  nucleolus"].
- Cytoplasmic translation control is the best-established core role, but the directness
  of the eIF4G interaction is disputed. Rajyaguru et al. reported RGG-dependent direct
  binding and repression [PMID:22284680, "Npl3 and Sbp1, also directly bind eIF4G and
  repress translation in a manner dependent on their RGG motifs"]. A later full-text
  study using purified RNA-free proteins found no direct Sbp1-eIF4G interaction and
  concluded that the earlier association was probably mediated by endogenous RNA or a
  ternary protein [PMID:28986506, "Using purified RNA-free proteins, we observed no
  direct interactions between eIF4G1 and Sbp1, and between eIF4G1 and the RGG domain of
  Sbp1 (Sbp1RGG)"]. That later work instead demonstrates direct RGG-dependent Sbp1-Pab1
  binding, cooperative binding of the two RRMs to the A-rich region in the PAB1 5' UTR,
  and inhibition of both cap-dependent and cap-independent initiation.
- The PMID:35440550 evidence is specifically for **P-body** disassembly, not stress
  granule disassembly: the abstract identifies Sbp1 as a P-body disassembly factor,
  reports defective disassembly in `sbp1`-null cells, and shows that Sbp1 competes
  with Edc3 self-interaction [PMID:35440550, "Sbp1-Edc3 interaction competes with
  Edc3-Edc3 interaction"]. The existing `MODIFY` decision to replace stress granule
  disassembly with protein-containing complex disassembly is retained. The related
  core function is localized only to the P-body; stress-granule localization remains
  a valid, condition-dependent non-core annotation.

## Review outcome

The existing annotation decisions remain evidence-consistent after re-audit: RNA
and mRNA binding, translation repression, the curator's disputed eIF4G-association
annotation, and cytoplasmic localization are retained as core; P-body localization is accepted as the site of the core disassembly function,
whereas stress-granule and historical nucleolar localizations remain non-core; generic
protein-binding annotations remain uninformative. No experimental
annotation was removed on the basis of incomplete full text.

## 2026-09-29 IBA re-review

- The four `GO_REF:0000033` IBA rows were checked against the local PTHR23003
  PAINT export. `GO:0003729` mRNA binding, `GO:0005634` nucleus, and
  `GO:0005737` cytoplasm all descend from `PANTHER:PTN002345455`; the first and
  third are core, while the nuclear placement is credible but non-core because
  the better-characterized SBP1 program is cytoplasmic mRNP/translation control.
  `GO:1990904` ribonucleoprotein complex descends from `PANTHER:PTN000543776`
  and remains consistent with Sbp1 mRNP membership.
- Three legacy `GO:0005515` protein-binding rows from high-throughput interactome
  screens were converted from `MARK_AS_OVER_ANNOTATED` to `REMOVE`, following the
  current IPI review policy for generic protein binding. Sbp1 has a more
  informative retained molecular-function proposal for competitive Edc3
  sequestration, `GO:0140311` protein sequestering activity.
- A fresh PubMed/web search for 2023-2026 Sbp1 papers recovered one new direct
  yeast paper after the cached 2025 JMB study: Mohanan et al. 2026, which
  reports that Sbp1 localizes to reversible RGG-dependent cytoplasmic granules
  under hydroxyurea and negatively regulates translation of `ATG1`, `ATG2`, and
  `ATG9` [PMID:42371698, "Loss of Sbp1 leads to selective translational
  upregulation of key autophagy genes ATG1, ATG2, and ATG9."]. The same PubMed
  search also found a 2026 goji-berry `SBP1` paper; that hit concerns an
  unrelated plant RING-finger self-incompatibility protein and was not used.

## 2026-10-01 current GOA refresh

- The current GOA refresh adds two PTN000543777 process IBAs: `GO:0006364`
  rRNA processing and `GO:0071028` nuclear mRNA surveillance. The first is seeded
  from SGD:S000006316/MRD1 and zebrafish evidence, while the second is seeded from
  GBP2/HRB1-like SF3 RRM proteins rather than SBP1/SF56. `GO:0006364` was marked
  `MARK_AS_OVER_ANNOTATED` and `GO:0071028` was marked `REMOVE`, both with
  `FUNCTIONAL_DIVERGENCE`: the direct Sbp1 literature supports a cytoplasmic mRNA-binding,
  translation-repression and P-body/stress-granule program, while the older SSB-1/snR10/snR11
  nucleolar evidence is indirect and does not establish that Sbp1 executes an rRNA-processing
  step.
- A new current-GOA InterPro2GO `GO:0003723` RNA-binding row and UniProt EXP
  `GO:0005737` cytoplasm row were accepted. Four now-absent exact source rows
  were retained but marked `retired: true`: one old GO_REF:0000120 RNA-binding
  row and three IntAct `GO:0005515` protein-binding rows that were already
  reviewed as uninformative.
