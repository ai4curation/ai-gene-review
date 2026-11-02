# LOXL3 (donkey, A0A9L0K7N3) notes

DONKEY40 cohort review (ProtNLM2 evaluation). Unreviewed TrEMBL entry, 824 aa, "Lysyl oxidase homolog" (UniRule RU367046). A human LOXL3 review exists in this repository (genes/human/LOXL3/LOXL3-ai-review.yaml) and was used for consistency.

## Identity and sequence
- PANTHER PTHR45817:SF2 (LYSYL OXIDASE HOMOLOG 3); four SRCR domains and the C-terminal lysyl oxidase domain [file:EQUAS/LOXL3/LOXL3-uniprot.txt "DR   PANTHER; PTHR45817:SF2; LYSYL OXIDASE HOMOLOG 3; 1."].
- 95.62% identity to human P58215 over the whole human length; copper-binding His and LTQ Lys/Tyr conserved; donkey 52-residue N-terminal extension places the human signal-peptide segment internally [file:EQUAS/LOXL3/LOXL3-bioinformatics/RESULTS.md "Human Met1 aligns to donkey Met53"].

## Function (human ortholog)
- Copper-dependent amine oxidase of the LOX family; human LOXL3 and LOXL3-sv1 oxidize elastin and collagen [PMID:17018530 "The recombinant LOXL3-sv1 protein showed a beta-aminopropionitrile-inhibitable amine oxidase activity toward elastin and collagen with substrate specificity."].
- Domain architecture with copper-binding sequence and LTQ residues; recombinant protein secreted [PMID:11284725 "Recombinant LOXL3, expressed in HT-1080 cells, was secreted into the culture medium but was not detected by immunofluorescence staining in nuclei."].
- Collagen I oxidation by LOXL3-sv2 [PMID:28112368 "The recombinant LOXL3-sv2 protein showed a β-aminopropionitrile-inhibitable amine oxidase activity toward collagen type I."].
- Nuclear Loxl3 deacetylates Stat3 via its SRCR repeats; Loxl3-/- naive CD4+ T cells show enhanced Th17/Treg differentiation [PMID:28065600 "LOX-like 3 (Loxl3) associates with Stat3"; "In Loxl3-/- mice, Stat3 is constitutively acetylated"].

## Annotation decisions (consistent with human LOXL3 review)
- protein-lysine 6-oxidase activity, copper ion binding, extracellular region, collagen fibril organization: ACCEPT.
- oxidoreductase activity acting on CH-NH2 group, oxygen as acceptor: TOO_GENERAL (entailed by protein-lysine 6-oxidase activity).
- nucleus, cytoplasm, inflammatory response, negative regulation of Th17 lineage commitment, tissue development, animal organ development: KEEP_AS_NON_CORE.
- elastic fiber: MARK_AS_OVER_ANNOTATED (substrate relationship, not established residence).
- membrane (InterPro SRCR mapping): REMOVE (soluble secreted protein; SRCR domains are not membrane anchors).

## ProtNLM2
- GO:0018057 peptidyl-lysine oxidation: not in donkey GOA; correct (the enzyme performs this protein modification) -> COR.
- No non-GO ProtNLM2 rows for this accession.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not consulted for this re-review.

### Deep research
- `just deep-research-falcon EQUAS LOXL3 --fallback perplexity-lite` failed (falcon timed out at 600 s, and the perplexity-lite fallback also failed). No deep-research file exists; the review uses the cached publications and the human/mouse LOXL3 annotation record.

### Identity and gene model
- New analysis: `LOXL3-bioinformatics/compare_sequences_rereview.py` and `RESULTS-rereview.md` (the original RESULTS.md is unchanged).
- Donkey A0A9L0K7N3 (824 aa) is identical to horse A0A9L0TKN1 (753 aa) at all 753 aligned positions [file:EQUAS/LOXL3/LOXL3-bioinformatics/RESULTS-rereview.md "Donkey A0A9L0K7N3 (824 aa) is identical to horse A0A9L0TKN1 (753 aa) at all 753 aligned positions."]. The only extra residues are a 52-aa N-terminal extension (donkey 1-52, upstream of the Met equivalent to horse/human Met1) and a 19-aa basic insertion (donkey 283-301, RKLRKRAAKASARRPKPLG) inside SRCR2. Neither is in horse or human, so both are gene-model errors. The benchmark accession is therefore an alternative (erroneous) gene model of the canonical LOXL3 product, not a fragment: all four SRCR domains and the complete catalytic domain are present, and the copper His triad and LTQ Lys/Tyr are conserved. The earlier RESULTS.md called the insertion "~18-residue"; with free end gaps it is 19 residues.
- No reviewed (Swiss-Prot) donkey LOXL3 entry exists; A0A9L0K7N3 is the only donkey LOXL3 product in this folder.

### Phylogenetic grounding
- PANTHER PTHR45817:SF2 (LYSYL OXIDASE HOMOLOG 3) contains donkey, human P58215, mouse Q9Z175 and zebrafish loxl3a/loxl3b, so donkey LOXL3 is the 1:1 ortholog of human/mouse LOXL3.
- PAINT IBDs reaching this subfamily: GO:0004720 and GO:0005576 at PTN002550804 (Bilateria); GO:0030199 and GO:0031012 at PTN008698711 (Chordata). The donkey TreeGrafter rows cite PTN001456249, a node that is not in the repository PAINT table.
- Mouse Loxl3 has IMP for inflammatory response (PMID:28065600) and for negative regulation of Th17 lineage commitment, plus developmental IMPs (PMID:26307084, PMID:26954549, PMID:27645581); PAINT propagated none of them (QuickGO, mouse Q9Z175, 2026-10-21). I treat that omission as deliberate.
- No PANTHER family review YAML exists for PTHR45817 (only metadata, entries and PAINT tables under interpro/panther/PTHR45817/), so there is no subfamily-placement disagreement to report. No module under modules/ mentions LOXL3 or lysyl oxidase. GO-CAM 653b0ce600000016 (human Th17/STAT3 acetylation) contains human LOXL3.

### Changes to annotation decisions
- inflammatory response (TreeGrafter): KEEP_AS_NON_CORE -> MARK_AS_OVER_ANNOTATED. The row rests on an organismal immune phenotype that PAINT did not propagate; the mechanism is captured more precisely by GO:2000329.
- NEW GO:0018057 peptidyl-lysine oxidation (ISS from mouse/human LOXL3, same subfamily). LOXL3 performs the oxidation itself, so it passes the participation test, and it was added to the core function. Mouse Loxl3 directly oxidizes fibronectin [PMID:26954549 "We find that LoxL3 complexes with and directly oxidizes Fibronectin (FN)"].
- Added PAINT-node support and mouse evidence to protein-lysine 6-oxidase activity, extracellular region and collagen fibril organization [PMID:26307084 "We found that the obvious decrease of collagen cross-links in palate and spine that was induced by the lack of LOXL3 resulted in cleft palate and spinal deformity."]. Also added mouse support to the tissue/organ development rows (non-core).
- All other actions are unchanged (copper ion binding ACCEPT; nucleus, cytoplasm, Th17, development terms KEEP_AS_NON_CORE; elastic fiber MARK_AS_OVER_ANNOTATED; membrane REMOVE; CH-NH2 oxidoreductase TOO_GENERAL).
- Description revised to mention the mouse fibronectin and collagen cross-link evidence and the horse-based gene-model diagnosis.

### Relative
- The canonical LOXL3 product is human P58215 (Swiss-Prot, same PANTHER subfamily). Its review, genes/human/LOXL3/LOXL3-ai-review.yaml, is COMPLETE. The horse partner A0A9L0TKN1 (genes/HORSE/LOXL3) is reviewed by its own agent in this run.
