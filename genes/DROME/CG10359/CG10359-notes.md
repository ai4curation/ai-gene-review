# CG10359 (B7Z0B2): evidence and ProtNLM claim review

CG10359 is a 485-residue secretory-pathway protein with a fibrinogen-like C-terminal domain. Its architecture supports an extracellular interaction role, while ligand specificity, membrane association, and receptor-mediated signaling remain uncertain.

Exact input: [B7Z0B2](https://www.uniprot.org/uniprotkb/B7Z0B2/entry), 485 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [CG10359-predictions-source.json](CG10359-predictions-source.json). Source features: [CG10359-uniprot.txt](CG10359-uniprot.txt), with an exact extraction in [CG10359-sequence-evidence.json](CG10359-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
DR   InterPro; IPR036056; Fibrinogen-like_C.
DR   InterPro; IPR014716; Fibrinogen_a/b/g_C_1.
DR   InterPro; IPR002181; Fibrinogen_a/b/g_C_dom.
DR   InterPro; IPR050373; Fibrinogen_C-term_domain.
FT   SIGNAL          1..23
FT                   /evidence="ECO:0000256|SAM:SignalP"
FT   DOMAIN          263..477
FT                   /note="Fibrinogen C-terminal"
FT                   /evidence="ECO:0000259|PROSITE:PS51406"
```

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | Fibrinogen C-terminal domain-containing protein | CNN | PROSITE PS51406 and InterPro IPR002181 independently identify the fibrinogen C-terminal domain at residues 263-477. The domain name is accurate without implying a vertebrate coagulation function. |
| Location | Secreted (SL-0243) | CNN | A Phobius signal peptide at residues 1-23 together with the extracellular fibrinogen-like domain supports secretion. Existing curated extracellular-matrix localization is compatible; secretion does not independently establish matrix binding or a GPCR interaction. |

## Literature evidence

No target-specific primary finding is used to establish a molecular activity here. The current assessment is bounded by exact-record architecture and the explicitly identified curated inferences.

## Annotation decisions

- GO:0001664 G protein-coupled receptor binding (ISS): **UNDECIDED**. The ISS assertion is a curated transfer rather than an experiment on this protein. Its fibrinogen-like domain and signal peptide support extracellular biology but do not identify a GPCR partner or establish conserved receptor binding.
- GO:0007186 G protein-coupled receptor signaling pathway (ISS): **UNDECIDED**. The sequence supports a secretory fibrinogen-domain protein but does not establish the receptor or pathway represented by this ISS annotation.
- GO:0008061 chitin binding (ISS): **UNDECIDED**. The extracellular fold permits diverse ligands; target-specific binding or a resolved transfer from a characterized chitin-binding ortholog is needed.
- GO:0016020 membrane (ISS): **UNDECIDED**. The human FIBCD1 source is a type 2 transmembrane receptor, whereas fly CG10359 has a predicted signal peptide and soluble FReD region. Peripheral membrane binding remains possible, but the source/target architecture mismatch leaves the ISS transfer unresolved.
- GO:0031012 extracellular matrix (IBA): **MODIFY** to GO:0005576 extracellular region. PTN000441162 puts `GO:0031012` at a taxon-unrestricted PTHR19143 node, and the cached evidence does not provide the tree divergence or loss evidence needed for a confident propagation failure. PMID:42009678 now supports CG10359/B7Z0B2 as a circulating larval secretome protein assigned to muscle, heart, wing disc and neurons, with a predicted CG10359-Mew interaction in imaginal discs; this supports a broad extracellular placement but not confirmed matrix residence.

## Research assessment

The Falcon report identifies PMID:24675716 as a primary CG10359 lead. The full text describes CG10359 as a predicted angiopoietin homolog and reports a negative deficiency result in the tested protection assay; it does not establish a receptor-binding function. The peer-reviewed PMID:42009678 secretome paper replaces the earlier preprint-only evidence, explicitly states that retained isoform B7Z0B2 was identified from muscle, heart, wing disc and neurons, and predicts muscle-secreted CG10359 binding to imaginal-disc Mew. This supports secretion into larval blood and a possible extracellular receptor interaction, not stable extracellular-matrix residence or receptor specificity.

Provider output: [CG10359-deep-research-falcon.md](CG10359-deep-research-falcon.md). Primary papers and source records, rather than provider verdicts, support the assessment.

The annotation and prediction assessments are complete. UNC/UNDECIDED record delimited scientific or evidence uncertainty. Empty core-function lists indicate that no sufficiently resolved molecular activity can be asserted, rather than an unfinished review.

## 2026-09-28 IBA rereview

Read the cached full texts for PMID:24675716, PMID:35916241, and PMID:42009678 and rechecked the sole CG10359 IBA against `interpro/panther/PTHR19143/PTHR19143-paint.tsv`. The `GO:0031012` row traces to `PANTHER:PTN000441162`, a taxon-unrestricted PAINT matrix-localization node. Because current target evidence supports secretion and extracellular interaction but not matrix retention, and because the PAINT row itself is not refuted by branch-length or target-loss evidence, the IBA is now a `MODIFY` to the broader GO:0005576 extracellular region with `TERM_SCOPING_PROBLEM`.

No `NEW` annotations were added. The 2022 dFibcd1 paper is perturbational and compares the fly FReD structurally to vertebrate FIBCD1, but the CS-4S/GAG binding assays are on vertebrate FIBCD1. The 2026 secretome map identifies CG10359/B7Z0B2 as a circulating larval blood protein and argues for secretion, which is still broader and less specific than the extracellular-matrix component propagated by PAINT.
